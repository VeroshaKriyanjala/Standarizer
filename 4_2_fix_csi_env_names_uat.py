#!/usr/bin/env python3
"""CSI Environment Variable Name Fixer

Scans kustomization.yaml files in each repo's PROD/UAT and updates
CSI_PROJECT_NAME, CSI_MODULENAME, CSI_MODULE_NAME values in Job patches
to use the correct onering repo name from onering_repo_names.txt.

Also fixes before-{name} and after-{name} Job metadata name replacements
to use the correct deployment/onering name.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install it with: pip install pyyaml")
    sys.exit(1)

DEFAULT_REPOS = {
    # "KKUH": "/home/verosha/Documents/gittea/KKUH",
    # "Alibaba": "/home/verosha/Documents/gittea/Alibaba",
    # "WAVE1": "/home/verosha/Documents/gittea/WAVE1",
    # "CS": "/home/verosha/Documents/gittea/CS",
    # "KAUH": "/home/verosha/Documents/gittea/KAUH",
    # "S2": "/home/verosha/Documents/gittea/S2",
    # "S3": "/home/verosha/Documents/gittea/S3",
    # "HMG": "/home/verosha/Documents/gittea/HMG",
    "RSG": "/home/verosha/Documents/gittea/RSG",
}

ONERING_NAMES_FILE = Path(__file__).parent / "onering_repo_names.txt"
OUTPUT_DIR = Path(__file__).parent / "output"
DEPLOYMENT_BASE_REPO_PATH = Path("/home/verosha/Documents/gittea/DEPLOYMENT-BASE-REPO")
BRANCH_NAME = "fix-csi-env-names"

# Env var names to fix in Job patches
CSI_ENV_NAMES = {"CSI_PROJECT_NAME", "CSI_MODULENAME", "CSI_MODULE_NAME"}


def git_run(repo_path, *args, check=True):
    """Run a git command in the given repo."""
    result = subprocess.run(
        ["git", "-C", str(repo_path)] + list(args),
        capture_output=True, text=True,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


def load_onering_names():
    """Load repo names from onering_repo_names.txt."""
    names = set()
    if not ONERING_NAMES_FILE.exists():
        print(f"WARNING: {ONERING_NAMES_FILE} not found")
        return names
    with open(ONERING_NAMES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("=") and not line.startswith("OneRing"):
                names.add(line)
    return names


def find_onering_name(service_folder_name, onering_names):
    """Find the matching onering repo name for a service folder.

    Tries:
    1. Exact match
    2. Hyphen/underscore/dot substitution
    3. Normalized comparison (strip hyphens/underscores/dots)
    4. Partial/substring match (longest wins)
    """
    if service_folder_name in onering_names:
        return service_folder_name

    # Hyphen <-> underscore
    alt = service_folder_name.replace("-", "_")
    if alt in onering_names:
        return alt
    alt = service_folder_name.replace("_", "-")
    if alt in onering_names:
        return alt

    # Dot <-> hyphen (e.g. csi.uif.admin.ui -> csi-uif-admin-ui)
    alt = service_folder_name.replace("-", ".")
    if alt in onering_names:
        return alt

    # Normalized comparison
    best_match = None
    best_score = 0
    norm_folder = service_folder_name.replace("-", "").replace("_", "").replace(".", "").lower()
    for name in onering_names:
        norm_name = name.replace("-", "").replace("_", "").replace(".", "").lower()
        if norm_folder == norm_name:
            return name
        if norm_folder in norm_name or norm_name in norm_folder:
            score = min(len(norm_folder), len(norm_name))
            if score > best_score:
                best_score = score
                best_match = name

    return best_match


def build_deployment_name_map():
    """Build a map from DEPLOYMENT-BASE-REPO relative path -> deployment metadata name."""
    deploy_map = {}
    for deploy_file in DEPLOYMENT_BASE_REPO_PATH.rglob("Deployment.yaml"):
        try:
            with open(deploy_file, "r", encoding="utf-8") as f:
                docs = list(yaml.safe_load_all(f))
            for doc in docs:
                if not doc:
                    continue
                if doc.get("kind") == "Deployment":
                    name = doc.get("metadata", {}).get("name")
                    if name:
                        rel_path = deploy_file.parent.relative_to(DEPLOYMENT_BASE_REPO_PATH)
                        deploy_map[str(rel_path)] = name
        except Exception as e:
            print(f"  WARN: Could not parse {deploy_file}: {e}")
    return deploy_map


def get_deployment_name(rel_path, deploy_map):
    """Get deployment name for a service path, with fallback."""
    deployment_name = deploy_map.get(rel_path)

    if not deployment_name:
        parts = rel_path.split("/")
        if len(parts) >= 2:
            module = parts[0]
            service = parts[-1]
            for key, name in deploy_map.items():
                key_parts = key.split("/")
                if len(key_parts) >= 2 and key_parts[0] == module and key_parts[-1] == service:
                    deployment_name = name
                    break

    if not deployment_name:
        deployment_name = rel_path.split("/")[-1]

    return deployment_name


def fix_csi_env_values(content, onering_name, deployment_name, parent_module):
    """Fix CSI_PROJECT_NAME, CSI_MODULENAME, CSI_MODULE_NAME values in Job patches.

    Also fixes before-{name} and after-{name} Job metadata name values.

    Returns (new_content, changed, list_of_changes)
    """
    lines = content.split("\n")
    new_lines = []
    changes = []
    in_job_patch = False
    in_patches_section = False
    current_target_kind = None
    patches_key_pattern = re.compile(r'^(patchesJSON6902|patchesJson6902)\s*:\s*$', re.IGNORECASE)

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track patchesJson6902 section
        if not stripped.startswith("#") and patches_key_pattern.match(stripped):
            in_patches_section = True
            current_target_kind = None
            in_job_patch = False
            new_lines.append(line)
            i += 1
            continue

        # End of patches section (top-level key)
        if in_patches_section and stripped and not stripped.startswith("#") and not stripped.startswith("-") and not line.startswith(" ") and not line.startswith("\t"):
            in_patches_section = False
            in_job_patch = False
            current_target_kind = None

        if in_patches_section:
            # Detect target kind
            kind_match = re.match(r'\s*kind:\s*(\S+)', stripped)
            if kind_match:
                current_target_kind = kind_match.group(1)
                if current_target_kind == "Job":
                    in_job_patch = True
                else:
                    in_job_patch = False

            # New target block resets kind
            if re.match(r'\s*-\s*target:\s*$', line):
                current_target_kind = None
                in_job_patch = False

            if in_job_patch:
                # Fix before-{name} and after-{name} in value: lines
                before_match = re.match(r'(\s*value:\s*)before-(.*)', line)
                if before_match:
                    old_name = before_match.group(2).strip()
                    if old_name != deployment_name:
                        indent_part = before_match.group(1)
                        new_lines.append(f"{indent_part}before-{deployment_name}")
                        changes.append(f"Fixed Job name: before-{old_name} -> before-{deployment_name}")
                        i += 1
                        continue

                after_match = re.match(r'(\s*value:\s*)after-(.*)', line)
                if after_match:
                    old_name = after_match.group(2).strip()
                    if old_name != deployment_name:
                        indent_part = after_match.group(1)
                        new_lines.append(f"{indent_part}after-{deployment_name}")
                        changes.append(f"Fixed Job name: after-{old_name} -> after-{deployment_name}")
                        i += 1
                        continue

                # Fix data-migration-presync-{name} and data-migration-postsync-{name}
                dm_presync_match = re.match(r'(\s*value:\s*)data-migration-presync-(.*)', line)
                if dm_presync_match:
                    old_name = dm_presync_match.group(2).strip()
                    if old_name != deployment_name:
                        indent_part = dm_presync_match.group(1)
                        new_lines.append(f"{indent_part}data-migration-presync-{deployment_name}")
                        changes.append(f"Fixed Job name: data-migration-presync-{old_name} -> data-migration-presync-{deployment_name}")
                        i += 1
                        continue

                dm_postsync_match = re.match(r'(\s*value:\s*)data-migration-postsync-(.*)', line)
                if dm_postsync_match:
                    old_name = dm_postsync_match.group(2).strip()
                    if old_name != deployment_name:
                        indent_part = dm_postsync_match.group(1)
                        new_lines.append(f"{indent_part}data-migration-postsync-{deployment_name}")
                        changes.append(f"Fixed Job name: data-migration-postsync-{old_name} -> data-migration-postsync-{deployment_name}")
                        i += 1
                        continue

                # Fix CSI env var values
                # Check if previous line(s) contain a CSI env var name
                # Pattern: name: CSI_PROJECT_NAME (or similar) followed by value: "xxx"
                if re.match(r'\s*value:\s*".*"', stripped) or re.match(r'\s*value:\s*\S+', stripped):
                    # Look back for the env var name
                    env_name = None
                    for back in range(1, min(4, i + 1)):
                        prev_line = lines[i - back].strip()
                        for csi_name in CSI_ENV_NAMES:
                            if f"name: {csi_name}" in prev_line:
                                env_name = csi_name
                                break
                        if env_name:
                            break

                    if env_name and onering_name:
                        # Extract current value
                        val_match = re.match(r'(\s*value:\s*)"?([^"]*)"?', line)
                        if val_match:
                            old_val = val_match.group(2).strip()
                            indent_part = val_match.group(1)

                            if old_val != onering_name:
                                new_lines.append(f'{indent_part}"{onering_name}"')
                                changes.append(f"Fixed {env_name}: \"{old_val}\" -> \"{onering_name}\"")
                                i += 1
                                continue

                # Fix CSI_PARENT_MODULE_NAME value
                if re.match(r'\s*value:\s*".*"', stripped) or re.match(r'\s*value:\s*\S+', stripped):
                    env_name = None
                    for back in range(1, min(4, i + 1)):
                        prev_line = lines[i - back].strip()
                        if "name: CSI_PARENT_MODULE_NAME" in prev_line:
                            env_name = "CSI_PARENT_MODULE_NAME"
                            break
                    if env_name and parent_module:
                        val_match = re.match(r'(\s*value:\s*)"?([^"]*)"?', line)
                        if val_match:
                            old_val = val_match.group(2).strip()
                            indent_part = val_match.group(1)
                            if old_val != parent_module:
                                new_lines.append(f'{indent_part}"{parent_module}"')
                                changes.append(f"Fixed CSI_PARENT_MODULE_NAME: \"{old_val}\" -> \"{parent_module}\"")
                                i += 1
                                continue

        new_lines.append(line)
        i += 1

    new_content = "\n".join(new_lines)
    return new_content, bool(changes), changes


def process_kustomization_file(kust_file, onering_name, deployment_name, parent_module, dry_run=False):
    """Process a single kustomization.yaml file to fix CSI env names."""
    with open(kust_file, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    content, changed, changes = fix_csi_env_values(content, onering_name, deployment_name, parent_module)

    if content != original and not dry_run:
        with open(kust_file, "w", encoding="utf-8") as f:
            f.write(content)

    return changes


def process_repo(repo_name, repo_path, deploy_map, onering_names, env_name, dry_run=False):
    """Process a single repo to fix CSI env variable names."""
    repo_path = Path(repo_path)
    env_dir = repo_path / env_name  # PROD or UAT

    if not env_dir.exists():
        print(f"  {env_name} directory not found")
        return []

    # Git: checkout appropriate source branch, create fix branch
    if not dry_run:
        # Try to checkout the base branch
        source_branch = f"{env_name}-dm-initiator-update"
        fallback_branch = f"{env_name}-standardize-folder-names"
        checked_out = False

        for branch in [source_branch, fallback_branch, "main", "master"]:
            result = git_run(repo_path, "checkout", branch, check=False)
            if result.returncode == 0:
                print(f"  Checked out {branch}")
                checked_out = True
                break

        if not checked_out:
            print(f"  ERROR: Could not checkout any source branch")
            return []

        # Delete old fix branch if exists
        branch_name = f"{env_name}-{BRANCH_NAME}"
        result = git_run(repo_path, "branch", "--list", branch_name, check=False)
        if branch_name in result.stdout:
            git_run(repo_path, "branch", "-D", branch_name, check=False)
            print(f"  Deleted old branch '{branch_name}'")

        try:
            git_run(repo_path, "checkout", "-b", branch_name)
            print(f"  Created branch '{branch_name}'")
        except RuntimeError as e:
            print(f"  ERROR creating branch: {e}")
            return []

    # Find all kustomization files
    kust_files = sorted(env_dir.rglob("kustomization.yaml"))
    print(f"  Found {len(kust_files)} kustomization files in {env_name}")

    log_entries = []
    total_changes = 0

    for kust_file in kust_files:
        rel_path = str(kust_file.parent.relative_to(env_dir))
        parts = rel_path.split("/")
        service_folder = parts[-1]
        parent_module = parts[0] if len(parts) >= 2 else ""

        # Find onering name for this service
        onering_name = find_onering_name(service_folder, onering_names)

        # Find deployment name
        deployment_name = get_deployment_name(rel_path, deploy_map)

        if not onering_name:
            # No onering match - skip but log
            log_entries.append((rel_path, f"NO ONERING MATCH for folder '{service_folder}'"))
            continue

        changes = process_kustomization_file(
            kust_file, onering_name, deployment_name, parent_module, dry_run
        )

        if changes:
            total_changes += len(changes)
            for change in changes:
                print(f"    [{rel_path}] {change}")
                log_entries.append((rel_path, change))

    print(f"\n  Total changes: {total_changes}")

    # Commit
    if total_changes > 0 and not dry_run:
        try:
            git_run(repo_path, "add", "-A")
            commit_msg = (
                f"Fix CSI env variable names in {env_name} Job patches\n\n"
                f"- Updated CSI_PROJECT_NAME values to match onering repo names\n"
                f"- Updated CSI_MODULENAME values to match onering repo names\n"
                f"- Updated CSI_MODULE_NAME values to match onering repo names\n"
                f"- Fixed before-/after- Job metadata names\n"
                f"\n{total_changes} changes across {len(set(e[0] for e in log_entries if 'NO ONERING' not in e[1]))} services"
            )
            git_run(repo_path, "commit", "-m", commit_msg)
            print(f"  Committed changes")
        except RuntimeError as e:
            if "nothing to commit" in str(e):
                print(f"  No changes to commit")
            else:
                print(f"  ERROR committing: {e}")

    return log_entries


def write_log(repo_name, env_name, log_entries, dry_run):
    """Write execution log for a repo."""
    log_dir = OUTPUT_DIR / repo_name
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"fix_csi_env_names_{env_name.lower()}.md"

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# CSI Env Name Fix Log - {repo_name} ({env_name})\n\n")
        f.write(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}\n\n")

        if log_entries:
            # Separate changes from warnings
            changes = [(p, c) for p, c in log_entries if "NO ONERING" not in c]
            warnings = [(p, c) for p, c in log_entries if "NO ONERING" in c]

            if changes:
                f.write(f"## Changes ({len(changes)} total)\n\n")
                f.write("| Service | Change |\n")
                f.write("|---------|--------|\n")
                for rel_path, change in changes:
                    f.write(f"| `{rel_path}` | {change} |\n")

            if warnings:
                f.write(f"\n## Warnings ({len(warnings)})\n\n")
                f.write("| Service | Warning |\n")
                f.write("|---------|--------|\n")
                for rel_path, warning in warnings:
                    f.write(f"| `{rel_path}` | {warning} |\n")
        else:
            f.write("## No changes needed\n")

    print(f"  Log saved to {log_file}")


def main():
    dry_run = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    # Parse env (PROD/UAT) and repo names
    env_name = "UAT"
    repo_names = []
    for a in args:
        if a.upper() in ("PROD", "UAT"):
            env_name = a.upper()
        else:
            repo_names.append(a)

    if repo_names:
        repos = {name: DEFAULT_REPOS[name] for name in repo_names if name in DEFAULT_REPOS}
        if not repos:
            print(f"Unknown repo(s): {repo_names}")
            print(f"Available: {list(DEFAULT_REPOS.keys())}")
            return
    else:
        repos = DEFAULT_REPOS

    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"{'=' * 60}")
    print(f"  CSI Env Name Fixer - {env_name} - Mode: {mode}")
    print(f"{'=' * 60}\n")

    print("Loading onering repo names...")
    onering_names = load_onering_names()
    print(f"Loaded {len(onering_names)} repo names\n")

    print("Scanning DEPLOYMENT-BASE-REPO for deployment names...")
    deploy_map = build_deployment_name_map()
    print(f"Found {len(deploy_map)} deployments\n")

    print(f"Env vars to fix: {', '.join(sorted(CSI_ENV_NAMES))}")
    print(f"Target env: {env_name}\n")

    for repo_name, repo_path in repos.items():
        print(f"\n{'=' * 40}")
        print(f"[{repo_name}] - {env_name}")
        print(f"{'=' * 40}")

        log_entries = process_repo(repo_name, repo_path, deploy_map, onering_names, env_name, dry_run)
        write_log(repo_name, env_name, log_entries, dry_run)

    print(f"\n{'=' * 60}")
    print("Done!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
