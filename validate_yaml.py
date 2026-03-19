#!/usr/bin/env python3
"""YAML Validator for Kustomization files across all repos.

Scans PROD and UAT kustomization.yaml files for:
- YAML syntax errors
- Duplicate top-level keys (e.g. two patchesJson6902: sections)
- Missing required fields (apiVersion, kind, bases/resources)
- Invalid indentation
- Inconsistent patchesJson6902 casing
- Empty/missing image tags
- Mismatched target kinds in patchesJson6902
- Trailing whitespace issues
"""

import argparse
import re
import subprocess
import sys
from collections import Counter
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

OUTPUT_DIR = Path(__file__).parent / "output"

# Severity levels
ERROR = "ERROR"
WARNING = "WARNING"
INFO = "INFO"


class Issue:
    def __init__(self, severity, message, line=None):
        self.severity = severity
        self.message = message
        self.line = line

    def __str__(self):
        loc = f" (line {self.line})" if self.line else ""
        return f"[{self.severity}]{loc} {self.message}"


def check_yaml_syntax(file_path, content):
    """Check if the file is valid YAML syntax."""
    issues = []
    try:
        yaml.safe_load(content)
    except yaml.YAMLError as e:
        line = None
        if hasattr(e, 'problem_mark') and e.problem_mark:
            line = e.problem_mark.line + 1
        issues.append(Issue(ERROR, f"YAML syntax error: {e}", line))
    return issues


def check_duplicate_keys(file_path, content):
    """Check for duplicate top-level YAML keys (text-based, since PyYAML silently merges them)."""
    issues = []
    lines = content.split("\n")
    top_level_keys = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip empty lines, comments, list items, indented lines
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue

        # Top-level key: "keyname:" or "keyname: value"
        key_match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*:', line)
        if key_match:
            top_level_keys.append((key_match.group(1), i + 1))

    key_counts = Counter(k for k, _ in top_level_keys)
    for key, count in key_counts.items():
        if count > 1:
            lines_at = [str(ln) for k, ln in top_level_keys if k == key]
            issues.append(Issue(ERROR,
                f"Duplicate top-level key '{key}' found {count} times at lines {', '.join(lines_at)}"))

    return issues


def check_required_fields(file_path, content):
    """Check for required kustomization fields."""
    issues = []
    lines = content.split("\n")
    top_keys = set()

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue
        key_match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*:', line)
        if key_match:
            top_keys.add(key_match.group(1))

    if "apiVersion" not in top_keys:
        issues.append(Issue(WARNING, "Missing 'apiVersion' field"))

    if "kind" not in top_keys:
        issues.append(Issue(WARNING, "Missing 'kind' field"))

    has_bases = "bases" in top_keys or "resources" in top_keys
    if not has_bases:
        issues.append(Issue(WARNING, "Missing both 'bases' and 'resources' fields"))

    return issues


def check_indentation(file_path, content):
    """Check for tab indentation and inconsistent indent levels."""
    issues = []
    lines = content.split("\n")

    for i, line in enumerate(lines):
        if "\t" in line and not line.strip().startswith("#"):
            issues.append(Issue(WARNING, f"Tab character found (use spaces)", i + 1))

    return issues


def check_patches_casing(file_path, content):
    """Check for inconsistent patchesJson6902 casing."""
    issues = []
    lines = content.split("\n")
    casings_found = {}

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        match = re.match(r'^(patchesJSON6902|patchesJson6902|patchesjson6902)\s*:', stripped, re.IGNORECASE)
        if match:
            casing = match.group(1)
            if casing not in casings_found:
                casings_found[casing] = []
            casings_found[casing].append(i + 1)

    if len(casings_found) > 1:
        details = ", ".join(f"'{c}' at line(s) {','.join(str(l) for l in lns)}"
                           for c, lns in casings_found.items())
        issues.append(Issue(WARNING, f"Inconsistent patchesJson6902 casing: {details}"))

    # Standard casing is patchesJson6902
    for casing, line_nums in casings_found.items():
        if casing != "patchesJson6902":
            for ln in line_nums:
                issues.append(Issue(INFO, f"Non-standard casing '{casing}' (expected 'patchesJson6902')", ln))

    return issues


def check_images(file_path, content):
    """Check for empty or missing image tags."""
    issues = []
    lines = content.split("\n")
    in_images = False
    current_image_line = None
    has_name = False
    has_new_tag = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if re.match(r'^images\s*:', stripped) and not stripped.startswith("#"):
            in_images = True
            continue

        if in_images:
            # End of images section
            if stripped and not stripped.startswith("#") and not stripped.startswith("-") \
                    and not line.startswith(" ") and not line.startswith("\t"):
                in_images = False
                continue

            if re.match(r'-\s*name:', stripped):
                # Check previous image
                if current_image_line is not None and not has_new_tag:
                    issues.append(Issue(WARNING, "Image entry missing 'newTag'", current_image_line))
                current_image_line = i + 1
                has_name = True
                has_new_tag = False

            if re.match(r'newTag:\s*$', stripped):
                issues.append(Issue(ERROR, "Empty 'newTag' value", i + 1))
                has_new_tag = True
            elif re.match(r'newTag:', stripped):
                has_new_tag = True
                # Check for tag value
                tag_match = re.match(r'newTag:\s*(.+)', stripped)
                if tag_match:
                    tag_val = tag_match.group(1).strip()
                    # Strip inline comments
                    tag_val = tag_val.split("#")[0].strip()
                    if not tag_val:
                        issues.append(Issue(ERROR, "Empty 'newTag' value (only comment)", i + 1))

    # Check last image
    if in_images and current_image_line is not None and not has_new_tag:
        issues.append(Issue(WARNING, "Image entry missing 'newTag'", current_image_line))

    return issues


def check_namespace(file_path, content, env):
    """Check that namespace matches the expected environment."""
    issues = []
    lines = content.split("\n")

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        match = re.match(r'^namespace:\s*(.+)', stripped)
        if match:
            ns = match.group(1).strip()
            if env == "PROD" and "prod" not in ns.lower():
                issues.append(Issue(WARNING, f"Namespace '{ns}' doesn't contain 'prod' but file is in PROD", i + 1))
            elif env == "UAT" and "uat" not in ns.lower():
                issues.append(Issue(WARNING, f"Namespace '{ns}' doesn't contain 'uat' but file is in UAT", i + 1))
            break

    return issues


def check_patches_targets(file_path, content):
    """Check patchesJson6902 targets for common issues."""
    issues = []
    lines = content.split("\n")
    patches_key_pattern = re.compile(r'^(patchesJSON6902|patchesJson6902)\s*:\s*$', re.IGNORECASE)
    in_patches = False
    in_target = False
    target_line = None
    has_kind = False
    has_name = False
    has_patch = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if stripped.startswith("#"):
            continue

        if patches_key_pattern.match(stripped):
            in_patches = True
            continue

        if in_patches:
            # End of section
            if stripped and not line.startswith(" ") and not line.startswith("\t") and not stripped.startswith("-"):
                # Check last target
                if target_line is not None and not has_patch:
                    issues.append(Issue(WARNING, f"Target block missing 'patch:' field", target_line))
                in_patches = False
                in_target = False
                continue

            if re.match(r'\s*-\s*target:\s*$', line):
                # Check previous target
                if target_line is not None:
                    if not has_kind:
                        issues.append(Issue(WARNING, "Target block missing 'kind'", target_line))
                    if not has_name:
                        issues.append(Issue(WARNING, "Target block missing 'name'", target_line))
                    if not has_patch:
                        issues.append(Issue(WARNING, "Target block missing 'patch:' field", target_line))

                target_line = i + 1
                has_kind = False
                has_name = False
                has_patch = False
                in_target = True
                continue

            if in_target:
                if re.match(r'\s*kind:\s*\S+', stripped):
                    has_kind = True
                    kind_match = re.match(r'\s*kind:\s*(\S+)', stripped)
                    if kind_match:
                        kind = kind_match.group(1)
                        valid_kinds = {"Deployment", "Job", "StatefulSet", "DaemonSet",
                                      "CronJob", "Service", "ConfigMap", "Secret",
                                      "Ingress", "HorizontalPodAutoscaler", "PersistentVolumeClaim"}
                        if kind not in valid_kinds:
                            issues.append(Issue(INFO, f"Unusual target kind '{kind}'", i + 1))

                if re.match(r'\s*name:\s*\S+', stripped):
                    has_name = True

                if stripped.startswith("patch:"):
                    has_patch = True

    # Check last target
    if in_patches and target_line is not None and not has_patch:
        issues.append(Issue(WARNING, f"Target block missing 'patch:' field", target_line))

    return issues


def check_trailing_whitespace(file_path, content):
    """Check for excessive trailing whitespace."""
    issues = []
    lines = content.split("\n")
    trailing_count = 0

    for i, line in enumerate(lines):
        if line != line.rstrip() and line.strip():
            trailing_count += 1

    if trailing_count > 0:
        issues.append(Issue(INFO, f"{trailing_count} line(s) have trailing whitespace"))

    return issues


def check_bases_url(file_path, content):
    """Check that bases URLs use the correct domain."""
    issues = []
    lines = content.split("\n")
    in_bases = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue

        if re.match(r'^bases\s*:', stripped):
            in_bases = True
            continue

        if in_bases:
            if stripped and not line.startswith(" ") and not line.startswith("\t") and not stripped.startswith("-"):
                in_bases = False
                continue

            if stripped.startswith("- http"):
                url = stripped[2:].strip()
                if "DEPLOYMENT-BASE-REPO" not in url and "CENTRAL-BASE-REPO" not in url:
                    issues.append(Issue(WARNING, f"Base URL doesn't reference known BASE repos: {url}", i + 1))

    return issues


def check_sync_and_dm(file_path, content):
    """Check for mixed Sync and DM-Initiator references."""
    issues = []
    lines = content.split("\n")
    has_sync = False
    has_dm = False
    sync_lines = []
    dm_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip comments
        if stripped.startswith("#"):
            continue

        if re.search(r'Sync-new|Sync-DM|Sync/', stripped):
            has_sync = True
            sync_lines.append(i + 1)
        if "DM-Initiator" in stripped:
            has_dm = True
            dm_lines.append(i + 1)

    if has_sync and has_dm:
        issues.append(Issue(WARNING,
            f"Both Sync and DM-Initiator references found (Sync at line(s) {','.join(str(l) for l in sync_lines)}, "
            f"DM-Initiator at line(s) {','.join(str(l) for l in dm_lines)})"))

    return issues


def validate_file(file_path, env):
    """Run all validation checks on a single kustomization.yaml file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [Issue(ERROR, f"Cannot read file: {e}")]

    if not content.strip():
        return [Issue(ERROR, "File is empty")]

    all_issues = []
    all_issues.extend(check_yaml_syntax(file_path, content))
    all_issues.extend(check_duplicate_keys(file_path, content))
    all_issues.extend(check_required_fields(file_path, content))
    all_issues.extend(check_indentation(file_path, content))
    all_issues.extend(check_patches_casing(file_path, content))
    all_issues.extend(check_images(file_path, content))
    all_issues.extend(check_namespace(file_path, content, env))
    all_issues.extend(check_patches_targets(file_path, content))
    all_issues.extend(check_trailing_whitespace(file_path, content))
    all_issues.extend(check_bases_url(file_path, content))
    all_issues.extend(check_sync_and_dm(file_path, content))

    return all_issues


def git_run(repo_path, *args, check=True):
    """Run a git command in the given repo."""
    result = subprocess.run(
        ["git", "-C", str(repo_path)] + list(args),
        capture_output=True, text=True,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


def checkout_branch(repo_path, branch):
    """Checkout the specified branch in the repo."""
    git_run(repo_path, "fetch", "--all", check=False)
    result = git_run(repo_path, "checkout", branch, check=False)
    if result.returncode != 0:
        print(f"  WARNING: Could not checkout branch '{branch}': {result.stderr.strip()}")
        return False
    print(f"  Checked out branch: {branch}")
    return True


def process_repo(repo_name, repo_path, folders=None):
    """Validate all kustomization.yaml files in a repo's specified dirs."""
    repo_path = Path(repo_path)
    results = {}  # {relative_path: [issues]}

    envs = folders if folders else ["PROD", "UAT"]

    for env in envs:
        env_dir = repo_path / env
        if not env_dir.exists():
            print(f"  Folder '{env}' not found, skipping")
            continue

        kust_files = sorted(env_dir.rglob("kustomization.yaml"))
        for kust_file in kust_files:
            rel_path = str(kust_file.relative_to(repo_path))
            issues = validate_file(kust_file, env)
            if issues:
                results[rel_path] = issues

    return results


def write_log(all_results):
    """Write validation report to output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    log_file = OUTPUT_DIR / "yaml_validation_report.md"

    total_files = 0
    total_errors = 0
    total_warnings = 0
    total_info = 0
    files_with_issues = 0

    with open(log_file, "w", encoding="utf-8") as f:
        f.write("# YAML Validation Report\n\n")

        # Summary table per repo
        f.write("## Summary\n\n")
        f.write("| Repo | Files Scanned | Errors | Warnings | Info |\n")
        f.write("|------|--------------|--------|----------|------|\n")

        for repo_name, results in all_results.items():
            file_issues = {k: v for k, v in results.items() if k != "_total_files"}
            repo_errors = sum(1 for issues in file_issues.values() for i in issues if i.severity == ERROR)
            repo_warnings = sum(1 for issues in file_issues.values() for i in issues if i.severity == WARNING)
            repo_info = sum(1 for issues in file_issues.values() for i in issues if i.severity == INFO)
            repo_files = results.get("_total_files", 0)
            f.write(f"| {repo_name} | {repo_files} | {repo_errors} | {repo_warnings} | {repo_info} |\n")
            total_files += repo_files
            total_errors += repo_errors
            total_warnings += repo_warnings
            total_info += repo_info
            files_with_issues += len([k for k in results if k != "_total_files" and results[k]])

        f.write(f"| **Total** | **{total_files}** | **{total_errors}** | **{total_warnings}** | **{total_info}** |\n\n")
        f.write(f"Files with issues: {files_with_issues}\n\n")

        # Detailed results
        for repo_name, results in all_results.items():
            file_results = {k: v for k, v in results.items() if k != "_total_files"}
            if not file_results:
                continue

            f.write(f"## {repo_name}\n\n")
            for rel_path, issues in sorted(file_results.items()):
                if not issues:
                    continue
                f.write(f"### `{rel_path}`\n\n")
                for issue in issues:
                    icon = "x" if issue.severity == ERROR else "!" if issue.severity == WARNING else "i"
                    f.write(f"- [{icon}] {issue}\n")
                f.write("\n")

    print(f"\nReport saved to {log_file}")
    return total_errors, total_warnings, total_info


def main():
    parser = argparse.ArgumentParser(
        description="Validate kustomization.yaml files across repos",
        epilog="Examples:\n"
               "  python3 validate_yaml.py\n"
               "  python3 validate_yaml.py Alibaba HMG\n"
               "  python3 validate_yaml.py --branch PROD-standardize-folder-names\n"
               "  python3 validate_yaml.py --folder PROD\n"
               "  python3 validate_yaml.py --branch PROD-dm-initiator-update --folder PROD Alibaba\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("repos", nargs="*", help="Repo names to validate (default: all)")
    parser.add_argument("--branch", "-b", help="Git branch to checkout before validating")
    parser.add_argument("--folder", "-f", action="append",
                        help="Folder(s) to scan, e.g. PROD, UAT (default: both). Can be repeated: -f PROD -f UAT")

    args = parser.parse_args()

    if args.repos:
        unknown = [r for r in args.repos if r not in DEFAULT_REPOS]
        if unknown:
            print(f"Unknown repo(s): {unknown}")
            print(f"Available: {list(DEFAULT_REPOS.keys())}")
            return
        repos = {name: DEFAULT_REPOS[name] for name in args.repos}
    else:
        repos = DEFAULT_REPOS

    folders = args.folder  # None means both PROD and UAT

    print(f"{'=' * 60}")
    print(f"  YAML Validator for Kustomization Files")
    if args.branch:
        print(f"  Branch: {args.branch}")
    if folders:
        print(f"  Folder(s): {', '.join(folders)}")
    print(f"{'=' * 60}\n")

    all_results = {}

    for repo_name, repo_path in repos.items():
        print(f"[{repo_name}]")
        repo_path = Path(repo_path)

        if not repo_path.exists():
            print(f"  Repository path not found: {repo_path}")
            all_results[repo_name] = {"_total_files": 0}
            continue

        # Checkout branch if specified
        if args.branch:
            if not checkout_branch(repo_path, args.branch):
                all_results[repo_name] = {"_total_files": 0}
                continue

        results = process_repo(repo_name, repo_path, folders)

        # Count total files scanned
        envs = folders if folders else ["PROD", "UAT"]
        total_files = 0
        for env in envs:
            env_dir = repo_path / env
            if env_dir.exists():
                total_files += len(list(env_dir.rglob("kustomization.yaml")))

        results["_total_files"] = total_files

        errors = sum(1 for issues in results.values() if isinstance(issues, list) for i in issues if i.severity == ERROR)
        warnings = sum(1 for issues in results.values() if isinstance(issues, list) for i in issues if i.severity == WARNING)
        files_with_issues = len([k for k in results if k != "_total_files" and results.get(k)])

        print(f"  Scanned {total_files} files | {files_with_issues} with issues | {errors} errors, {warnings} warnings")

        all_results[repo_name] = results

    total_errors, total_warnings, total_info = write_log(all_results)

    print(f"\n{'=' * 60}")
    print(f"  Total: {total_errors} errors, {total_warnings} warnings, {total_info} info")
    print(f"{'=' * 60}")

    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
