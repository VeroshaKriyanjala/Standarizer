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
    "KKUH": "/home/verosha/Documents/gittea/KKUH",
    "Alibaba": "/home/verosha/Documents/gittea/Alibaba",
    "WAVE1": "/home/verosha/Documents/gittea/WAVE1",
    "CS": "/home/verosha/Documents/gittea/CS",
    "KAUH": "/home/verosha/Documents/gittea/KAUH",
    "S2": "/home/verosha/Documents/gittea/S2",
    "S3": "/home/verosha/Documents/gittea/S3",
    "HMG": "/home/verosha/Documents/gittea/HMG",
}

DEPLOYMENT_BASE_REPO_PATH = Path("/home/verosha/Documents/gittea/DEPLOYMENT-BASE-REPO")
OUTPUT_DIR = Path(__file__).parent / "output"

CENTRAL_BASE_URL = "https://git.cloudsolutions.com.sa/BASE/CENTRAL-BASE-REPO"
DEPLOYMENT_BASE_URL = "https://git.cloudsolutions.com.sa/BASE/DEPLOYMENT-BASE-REPO"
BRANCH_NAME = "PROD-standardize-folder-names"


def git_run(repo_path, *args, check=True):
    """Run a git command in the given repo."""
    result = subprocess.run(
        ["git", "-C", str(repo_path)] + list(args),
        capture_output=True, text=True,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


def build_deployment_name_map():
    """Build a map from DEPLOYMENT-BASE-REPO relative path -> deployment metadata name.

    Scans all Deployment.yaml files in DEPLOYMENT-BASE-REPO and extracts
    metadata.name for kind: Deployment.

    Returns dict like: {"pharmacy/csi-phr-base": "csi-phr-base", ...}
    """
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


def build_deployment_base_folders():
    """Build a set of all folder relative paths in DEPLOYMENT-BASE-REPO that have a Deployment.yaml."""
    folders = set()
    for deploy_file in DEPLOYMENT_BASE_REPO_PATH.rglob("Deployment.yaml"):
        rel_path = deploy_file.parent.relative_to(DEPLOYMENT_BASE_REPO_PATH)
        folders.add(str(rel_path))
    return folders


def find_matching_deployment_path(prod_rel_path, deploy_folders):
    """Find the matching DEPLOYMENT-BASE-REPO path for a PROD service folder.

    prod_rel_path: e.g. "pharmacy/csi-phr-base"
    deploy_folders: set of paths in DEPLOYMENT-BASE-REPO

    Returns the matching path or None.
    """
    # Direct match
    if prod_rel_path in deploy_folders:
        return prod_rel_path

    # Try matching by service name (last component) within the same module
    parts = prod_rel_path.split("/")
    if len(parts) >= 2:
        module = parts[0]
        service = parts[-1]
        for folder in deploy_folders:
            folder_parts = folder.split("/")
            if len(folder_parts) >= 2 and folder_parts[0] == module and folder_parts[-1] == service:
                return folder

    return None


def apply_rule1_base_url(content, new_base_path):
    """Rule 1: Replace CENTRAL-BASE-REPO base URL with DEPLOYMENT-BASE-REPO.

    Replaces the base URL line while preserving formatting and comments.
    new_base_path: the relative path in DEPLOYMENT-BASE-REPO (e.g. "pharmacy/csi-phr-base")
    """
    new_url = f"{DEPLOYMENT_BASE_URL}/{new_base_path}"

    # Match lines with CENTRAL-BASE-REPO URL (with optional leading whitespace and -)
    pattern = re.escape(CENTRAL_BASE_URL) + r"/[^\s#]+"
    new_content = re.sub(pattern, new_url, content)
    return new_content


def apply_rule3_patches_json(content, deployment_name):
    """Rule 3: Update patchesJson6902 Deployment target name.

    Finds patchesJson6902 blocks targeting kind: Deployment and updates the name.
    Uses a state-machine approach to preserve formatting.
    """
    lines = content.split("\n")
    result = []
    in_patches_json = False
    in_target = False
    found_deployment_kind = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Detect patchesJson6902 section (not commented out)
        if stripped == "patchesJson6902:" or stripped.startswith("patchesJson6902:"):
            if not stripped.startswith("#"):
                in_patches_json = True
                result.append(line)
                i += 1
                continue

        if in_patches_json:
            # Detect end of patchesJson6902 section (new top-level key)
            if stripped and not stripped.startswith("#") and not stripped.startswith("-") and not line.startswith(" ") and not line.startswith("\t"):
                in_patches_json = False
                in_target = False
                found_deployment_kind = False
                result.append(line)
                i += 1
                continue

            # Detect new "- target:" block
            if re.match(r"\s*-\s*target:\s*$", line):
                in_target = True
                found_deployment_kind = False
                result.append(line)
                i += 1
                continue

            if in_target:
                # Check for kind: Deployment
                if re.match(r"\s*kind:\s*Deployment\s*$", stripped):
                    found_deployment_kind = True
                    result.append(line)
                    i += 1
                    continue

                # Check for name: line within target that has Deployment kind
                name_match = re.match(r"(\s*name:\s*)(.*)", line)
                if name_match and found_deployment_kind:
                    old_name = name_match.group(2).strip()
                    if old_name != deployment_name:
                        indent_part = name_match.group(1)
                        result.append(f"{indent_part}{deployment_name}")
                        i += 1
                        continue

                # Detect end of target block (patch: or new - target:)
                if stripped.startswith("patch:"):
                    in_target = False
                    found_deployment_kind = False
                elif re.match(r"\s*-\s*target:\s*$", line):
                    found_deployment_kind = False

        result.append(line)
        i += 1

    return "\n".join(result)


def apply_rule4_metadata_name(file_path, deployment_name, dry_run=False):
    """Rule 4: Update metadata.name and spec.containers[].name in hpa.yaml, patch-hpa.yaml, patch-pod.yaml.

    Reads the file, updates metadata.name and container names to deployment_name, writes back.
    Preserves all other content.
    """
    if not file_path.exists():
        return False, "file not found"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    new_lines = []
    in_metadata = False
    in_containers = False
    changed = False

    for line in lines:
        stripped = line.strip()

        if stripped == "metadata:":
            in_metadata = True
            new_lines.append(line)
            continue

        if in_metadata:
            name_match = re.match(r"(\s*name:\s*)(.*)", line)
            if name_match:
                old_name = name_match.group(2).strip()
                if old_name != deployment_name:
                    new_lines.append(f"{name_match.group(1)}{deployment_name}")
                    changed = True
                else:
                    new_lines.append(line)
                in_metadata = False
                continue
            # If we hit a non-indented line, we've left metadata
            if stripped and not line.startswith(" ") and not line.startswith("\t"):
                in_metadata = False

        # Track containers section (e.g. "containers:" or "- name:" under containers)
        if stripped == "containers:":
            in_containers = True
            new_lines.append(line)
            continue

        if in_containers:
            # Match "- name: xxx" inside containers list
            container_name_match = re.match(r"(\s*-\s*name:\s*)(.*)", line)
            if container_name_match:
                old_name = container_name_match.group(2).strip()
                if old_name != deployment_name:
                    new_lines.append(f"{container_name_match.group(1)}{deployment_name}")
                    changed = True
                else:
                    new_lines.append(line)
                in_containers = False
                continue
            # If we hit a non-indented/non-list line, we've left containers
            if stripped and not line.startswith(" ") and not line.startswith("\t"):
                in_containers = False

        new_lines.append(line)

    if changed:
        new_content = "\n".join(new_lines)
        if not dry_run:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
        return True, f"updated name to '{deployment_name}'"
    return False, "name already correct"


def process_kustomization(kust_file, deployment_name, deploy_base_path, dry_run=False):
    """Process a single kustomization.yaml applying Rules 1 and 3."""
    with open(kust_file, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []

    # Rule 1: Replace base URL
    if "CENTRAL-BASE-REPO" in content:
        content = apply_rule1_base_url(content, deploy_base_path)
        if content != original:
            changes.append("Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO")

    # Rule 3: Update patchesJson6902 Deployment target name
    if "patchesJson6902:" in content and deployment_name:
        before = content
        content = apply_rule3_patches_json(content, deployment_name)
        if content != before:
            changes.append(f"Rule 3: Updated patchesJson6902 Deployment target name to '{deployment_name}'")

    if changes and not dry_run:
        with open(kust_file, "w", encoding="utf-8") as f:
            f.write(content)

    return changes


def commit_rule(repo_path, rule_name, commit_msg, change_count, dry_run=False):
    """Stage and commit changes for a single rule."""
    if change_count == 0 or dry_run:
        return
    try:
        git_run(repo_path, "add", "-A")
        git_run(repo_path, "commit", "-m", commit_msg)
        print(f"  Committed: {rule_name} ({change_count} changes)")
    except RuntimeError as e:
        # No changes to commit is fine
        if "nothing to commit" in str(e):
            print(f"  No changes to commit for {rule_name}")
        else:
            print(f"  ERROR committing {rule_name}: {e}")


def execute_for_repo(repo_name, repo_path, deploy_map, deploy_folders, dry_run=False):
    """Process all service folders in a repo's PROD directory."""
    prod_dir = Path(repo_path) / "PROD"

    if not prod_dir.exists():
        print(f"  PROD directory not found at {prod_dir}")
        return

    # Checkout the branch (stay on it throughout)
    if not dry_run:
        try:
            git_run(repo_path, "checkout", BRANCH_NAME)
            print(f"  On branch '{BRANCH_NAME}'")
        except RuntimeError as e:
            print(f"  ERROR checking out branch: {e}")
            return

    # Find all service folders (contain kustomization.yaml or other target files)
    service_dirs = set()
    for pattern in ["kustomization.yaml", "hpa.yaml", "patch-hpa.yaml", "patch-pod.yaml"]:
        for f in prod_dir.rglob(pattern):
            service_dirs.add(f.parent)

    service_dirs = sorted(service_dirs)
    print(f"  Found {len(service_dirs)} service folders to process")

    # Build per-service deployment info
    service_info = {}
    for service_dir in service_dirs:
        prod_rel_path = str(service_dir.relative_to(prod_dir))
        deploy_path = find_matching_deployment_path(prod_rel_path, deploy_folders)
        deployment_name = deploy_map.get(deploy_path) if deploy_path else None
        service_info[service_dir] = (prod_rel_path, deploy_path, deployment_name)

    total_changes = 0
    log_entries = []

    # --- Rule 1: Replace CENTRAL-BASE-REPO with DEPLOYMENT-BASE-REPO in bases ---
    print("\n  === Rule 1: Update base URLs ===")
    rule1_changes = 0
    for service_dir in service_dirs:
        prod_rel_path, deploy_path, deployment_name = service_info[service_dir]
        kust_file = service_dir / "kustomization.yaml"
        if not kust_file.exists() or not deploy_path:
            continue
        with open(kust_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "CENTRAL-BASE-REPO" not in content:
            continue
        new_content = apply_rule1_base_url(content, deploy_path)
        if new_content != content:
            if not dry_run:
                with open(kust_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
            print(f"    [{prod_rel_path}] Updated base URL")
            log_entries.append((prod_rel_path, "Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO"))
            rule1_changes += 1

    print(f"  Rule 1: {rule1_changes} changes")
    total_changes += rule1_changes
    commit_rule(repo_path, "Rule 1",
                f"Rule 1: Replace CENTRAL-BASE-REPO with DEPLOYMENT-BASE-REPO in bases\n\n"
                f"Updated {rule1_changes} kustomization.yaml files to use DEPLOYMENT-BASE-REPO.",
                rule1_changes, dry_run)

    # --- Rule 3: Update patchesJson6902 Deployment target name ---
    print("\n  === Rule 3: Update patchesJson6902 targets ===")
    rule3_changes = 0
    for service_dir in service_dirs:
        prod_rel_path, deploy_path, deployment_name = service_info[service_dir]
        if not deployment_name:
            continue
        kust_file = service_dir / "kustomization.yaml"
        if not kust_file.exists():
            continue
        with open(kust_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "patchesJson6902:" not in content:
            continue
        new_content = apply_rule3_patches_json(content, deployment_name)
        if new_content != content:
            if not dry_run:
                with open(kust_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
            print(f"    [{prod_rel_path}] Updated target name to '{deployment_name}'")
            log_entries.append((prod_rel_path, f"Rule 3: Updated patchesJson6902 Deployment target name to '{deployment_name}'"))
            rule3_changes += 1

    print(f"  Rule 3: {rule3_changes} changes")
    total_changes += rule3_changes
    commit_rule(repo_path, "Rule 3",
                f"Rule 3: Update patchesJson6902 Deployment target names\n\n"
                f"Updated {rule3_changes} kustomization.yaml files to match DEPLOYMENT-BASE-REPO deployment names.",
                rule3_changes, dry_run)

    # --- Rule 4: Update metadata.name and containers name in hpa/patch files ---
    print("\n  === Rule 4: Update metadata and container names ===")
    rule4_changes = 0
    for service_dir in service_dirs:
        prod_rel_path, deploy_path, deployment_name = service_info[service_dir]
        if not deployment_name:
            continue
        for yaml_name in ["hpa.yaml", "patch-hpa.yaml", "patch-pod.yaml"]:
            yaml_file = service_dir / yaml_name
            if yaml_file.exists():
                changed, msg = apply_rule4_metadata_name(yaml_file, deployment_name, dry_run)
                if changed:
                    print(f"    [{prod_rel_path}] {yaml_name} - {msg}")
                    log_entries.append((prod_rel_path, f"Rule 4: {yaml_name} - {msg}"))
                    rule4_changes += 1

    print(f"  Rule 4: {rule4_changes} changes")
    total_changes += rule4_changes
    commit_rule(repo_path, "Rule 4",
                f"Rule 4: Update metadata and container names in hpa/patch files\n\n"
                f"Updated {rule4_changes} files to match DEPLOYMENT-BASE-REPO deployment names.",
                rule4_changes, dry_run)

    print(f"\n  Total changes: {total_changes}")

    # Write log
    log_file = OUTPUT_DIR / repo_name / "more_rules_log.md"
    (OUTPUT_DIR / repo_name).mkdir(parents=True, exist_ok=True)
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# More Rules Execution Log - {repo_name}\n\n")
        f.write(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}\n\n")
        f.write(f"## Rules Applied\n\n")
        f.write("- **Rule 1**: Replace CENTRAL-BASE-REPO with DEPLOYMENT-BASE-REPO in bases\n")
        f.write("- **Rule 2**: Do not change images section (preserved)\n")
        f.write("- **Rule 3**: Update patchesJson6902 Deployment target name\n")
        f.write("- **Rule 4**: Update metadata.name and container name in hpa.yaml, patch-hpa.yaml, patch-pod.yaml\n\n")
        f.write(f"## Changes ({total_changes} total)\n\n")
        f.write(f"- Rule 1: {rule1_changes} changes\n")
        f.write(f"- Rule 3: {rule3_changes} changes\n")
        f.write(f"- Rule 4: {rule4_changes} changes\n\n")

        for rel_path, change_desc in log_entries:
            f.write(f"- `{rel_path}`: {change_desc}\n")

    print(f"  Log saved to {log_file}")


def main():
    dry_run = "--dry-run" in sys.argv
    repo_names = [a for a in sys.argv[1:] if a != "--dry-run"]

    if repo_names:
        repos = {name: DEFAULT_REPOS[name] for name in repo_names if name in DEFAULT_REPOS}
        if not repos:
            print(f"Unknown repo(s): {repo_names}")
            print(f"Available: {list(DEFAULT_REPOS.keys())}")
            return
    else:
        repos = DEFAULT_REPOS

    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"Mode: {mode}")
    print(f"Scanning DEPLOYMENT-BASE-REPO for deployment names...")

    deploy_map = build_deployment_name_map()
    deploy_folders = build_deployment_base_folders()
    print(f"Found {len(deploy_map)} deployments in DEPLOYMENT-BASE-REPO\n")

    for repo_name, repo_path in repos.items():
        print(f"[{repo_name}]")
        execute_for_repo(repo_name, repo_path, deploy_map, deploy_folders, dry_run=dry_run)
        print()

    print("Done!")


if __name__ == "__main__":
    main()
