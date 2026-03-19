#!/usr/bin/env python3
"""DM-Initiator Updater

Checks version conditions in each repo's PROD and replaces Sync-new/Sync-DM/Sync
references with DM-Initiator. Replaces old Job patches with new standardized
sync-presync/sync-postsync format with CSI_PROJECT_NAME from onering_repo_names.txt.
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
    "KKUH": "/home/verosha/Documents/gittea/KKUH",
    "Alibaba": "/home/verosha/Documents/gittea/Alibaba",
    "WAVE1": "/home/verosha/Documents/gittea/WAVE1",
    "CS": "/home/verosha/Documents/gittea/CS",
    "KAUH": "/home/verosha/Documents/gittea/KAUH",
    "S2": "/home/verosha/Documents/gittea/S2",
    "S3": "/home/verosha/Documents/gittea/S3",
    "HMG": "/home/verosha/Documents/gittea/HMG",
}

ONERING_NAMES_FILE = Path(__file__).parent / "onering_repo_names.txt"
OUTPUT_DIR = Path(__file__).parent / "output"
DEPLOYMENT_BASE_REPO_PATH = Path("/home/verosha/Documents/gittea/DEPLOYMENT-BASE-REPO")
BRANCH_NAME = "PROD-dm-initiator-update"

# Threshold versions - DM-Initiator can be added if both are >= these
BASE_UTILITY_THRESHOLD = "V4.0.2510_W1-4893_prod"
CSI_IAM_THRESHOLD = "V4.0.2510_W4_14_prod"


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
            # Skip header and empty lines
            if line and not line.startswith("=") and not line.startswith("OneRing"):
                names.add(line)
    return names


def find_csi_project_name(service_folder_name, onering_names):
    """Find the CSI_PROJECT_NAME for a service by matching against onering repo names.

    Tries:
    1. Exact match
    2. Match with hyphen/underscore substitution
    3. Partial match (service name contained in onering name or vice versa)
    """
    # Exact match
    if service_folder_name in onering_names:
        return service_folder_name

    # Try hyphen <-> underscore substitution
    alt_name = service_folder_name.replace("-", "_")
    if alt_name in onering_names:
        return alt_name
    alt_name = service_folder_name.replace("_", "-")
    if alt_name in onering_names:
        return alt_name

    # Try dot <-> hyphen substitution (e.g., csi.uif.admin.ui -> csi-uif-admin-ui)
    alt_name = service_folder_name.replace("-", ".")
    if alt_name in onering_names:
        return alt_name

    # Partial match: find onering name that best matches
    # Prioritize longer matches
    best_match = None
    best_score = 0
    for name in onering_names:
        # Normalize both for comparison
        norm_folder = service_folder_name.replace("-", "").replace("_", "").replace(".", "").lower()
        norm_name = name.replace("-", "").replace("_", "").replace(".", "").lower()
        if norm_folder == norm_name:
            return name
        # Check if one contains the other
        if norm_folder in norm_name or norm_name in norm_folder:
            score = min(len(norm_folder), len(norm_name))
            if score > best_score:
                best_score = score
                best_match = name

    return best_match  # Could be None if no match found


def parse_version_tag(tag):
    """Parse a version tag into a comparable tuple.

    Returns (format_type, comparable_tuple) where:
    - format_type: 'new' for V4.0.YYWW format, 'old' for 4.x.y.z format
    - comparable_tuple: tuple that can be compared with < > ==

    The V4.0.YYMM format (e.g., V4.0.2510_W1-4893_prod) came AFTER the
    old 4.x.y.z format (e.g., 4.3.0.11_prod), so old format is always
    considered older than any V4.0.YYMM tag with YYMM >= 2500.
    """
    tag = tag.strip()

    # Try V4.0.YYMM format: V4.0.2510_W1-4893_prod or V4.0.2510_W4_14_prod
    # YYMM = year + month (2510 = year 25, month 10)
    # WX = week number of the month
    m = re.match(r'V4\.0\.(\d{4})_W(\d+)[-_](\d+)', tag)
    if m:
        yymm = int(m.group(1))
        week = int(m.group(2))
        build = int(m.group(3))
        return ('new', (yymm, week, build))

    # Try V4.0.YYMM_Int format (older): V4.0.0425_Int-2743_hf
    m = re.match(r'V4\.0\.(\d{4})_Int[-_](\d+)', tag)
    if m:
        yymm = int(m.group(1))
        build = int(m.group(2))
        return ('new', (yymm, 0, build))

    # Try old 4.x.y.z format: 4.3.0.11_prod
    m = re.match(r'4\.(\d+)\.(\d+)\.(\d+)', tag)
    if m:
        major_minor = int(m.group(1))
        patch = int(m.group(2))
        build = int(m.group(3))
        # Old format is always older than V4.0.25xx+ tags
        return ('old', (major_minor, patch, build))

    # Unknown format
    return ('unknown', (0, 0, 0))


def is_version_newer_or_equal(current_tag, threshold_tag):
    """Check if current_tag is >= threshold_tag.

    Returns True if the version is newer than or equal to the threshold.
    """
    curr_fmt, curr_tuple = parse_version_tag(current_tag)
    thresh_fmt, thresh_tuple = parse_version_tag(threshold_tag)

    # If threshold is 'new' format (V4.0.YYMM)
    if thresh_fmt == 'new':
        if curr_fmt == 'new':
            return curr_tuple >= thresh_tuple
        elif curr_fmt == 'old':
            # Old format (4.x.y.z) is always older than V4.0.25xx+ new format
            return False
        else:
            return False  # Unknown format, assume not newer

    # Shouldn't happen since our thresholds are 'new' format
    return False


def get_image_tag(kust_path):
    """Extract the current newTag from a kustomization.yaml file.

    Returns the first newTag value found (before any # comments).
    """
    if not kust_path.exists():
        return None
    with open(kust_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match newTag: VALUE (take only the actual tag, not comments)
    m = re.search(r'newTag:\s*([^\s#]+)', content)
    if m:
        return m.group(1)
    return None


def check_version_conditions(repo_path):
    """Check if both base-utility and csi-iam version conditions are met.

    Returns (met, base_tag, iam_tag, details_str)
    """
    prod_dir = Path(repo_path) / "PROD"

    # Find base-utility-service-java-sev kustomization
    base_kust = prod_dir / "base" / "base-utility-service-java-sev" / "kustomization.yaml"
    base_tag = get_image_tag(base_kust)

    # Find csi-iam-service kustomization
    iam_kust = prod_dir / "security" / "csi-iam-service" / "kustomization.yaml"
    iam_tag = get_image_tag(iam_kust)

    if not base_tag:
        return False, base_tag, iam_tag, "base-utility-service-java-sev tag not found"
    if not iam_tag:
        return False, base_tag, iam_tag, "csi-iam-service tag not found"

    base_ok = is_version_newer_or_equal(base_tag, BASE_UTILITY_THRESHOLD)
    iam_ok = is_version_newer_or_equal(iam_tag, CSI_IAM_THRESHOLD)

    details = []
    details.append(f"base-utility: {base_tag} {'>=':} {BASE_UTILITY_THRESHOLD} -> {'PASS' if base_ok else 'FAIL'}")
    details.append(f"csi-iam: {iam_tag} {'>=':} {CSI_IAM_THRESHOLD} -> {'PASS' if iam_ok else 'FAIL'}")

    return (base_ok and iam_ok), base_tag, iam_tag, "\n    ".join(details)


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


def replace_sync_with_dm_initiator(content):
    """Task 1: Replace Sync-new/Sync-DM/Sync references with DM-Initiator.

    Handles both active and commented-out references.
    Preserves comment state: if Sync was commented, DM-Initiator stays commented too.
    If Sync was active, DM-Initiator is active.

    Returns (new_content, changed, details)
    """
    lines = content.split("\n")
    new_lines = []
    found_sync = False
    dm_initiator_added = False
    already_has_dm = False
    changes = []

    # Check if already has DM-Initiator (active or commented)
    for line in lines:
        stripped = line.strip().lstrip("#").strip()
        if "DM-Initiator" in stripped:
            already_has_dm = True
            break

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        stripped_no_comment = stripped.lstrip("#").strip()

        # Check if this line references Sync-new, Sync-DM, or Sync/
        is_sync_ref = False
        for sync_name in ["../../../Sync-new/", "../../../Sync-DM/", "../../../Sync/"]:
            if sync_name in stripped_no_comment:
                is_sync_ref = True
                break

        if is_sync_ref:
            found_sync = True
            is_commented = stripped.startswith("#")

            # Replace first Sync reference with DM-Initiator (if not already added)
            if not dm_initiator_added and not already_has_dm:
                if is_commented:
                    # Preserve comment state: keep DM-Initiator commented too
                    # Determine the comment prefix and indentation from original line
                    indent = ""
                    for ch in line:
                        if ch in (' ', '\t'):
                            indent += ch
                        else:
                            break
                    # Keep the same comment style
                    new_lines.append(f"{indent}#- ../../../DM-Initiator/")
                    changes.append("Replaced commented Sync reference with commented DM-Initiator")
                else:
                    # Active Sync -> active DM-Initiator
                    indent = ""
                    for ch in line:
                        if ch in (' ', '\t'):
                            indent += ch
                        else:
                            break
                    new_lines.append(f"{indent}- ../../../DM-Initiator/")
                    changes.append("Replaced Sync reference with DM-Initiator")
                dm_initiator_added = True
            else:
                # Skip additional Sync references (DM-Initiator replaces all of them)
                changes.append(f"Removed extra Sync reference: {stripped}")
            i += 1
            continue

        new_lines.append(line)
        i += 1

    if found_sync and not already_has_dm:
        return "\n".join(new_lines), True, changes
    elif found_sync and already_has_dm:
        # Remove Sync references but DM-Initiator already exists
        return "\n".join(new_lines), True, changes
    return content, False, []


def generate_new_job_patches(deployment_name, csi_project_name):
    """Generate the new standardized Job patch YAML block.

    Returns the YAML text for the two Job targets (sync-presync and sync-postsync).
    """
    project_name_val = csi_project_name if csi_project_name else ""

    patch_block = f"""- target:
    group: batch
    version: v1
    kind: Job
    name: sync-presync
  patch: |-
    - op: replace
      path: /metadata/name
      value: before-{deployment_name}
    - op: add
      path: /spec/template/spec/containers/0/env/-
      value:
        name: CSI_PROJECT_NAME
        value: "{project_name_val}"
- target:
    group: batch
    version: v1
    kind: Job
    name: sync-postsync
  patch: |-
    - op: add
      path: /spec/template/spec/containers/0/env/-
      value:
        name: CSI_PROJECT_NAME
        value: "{project_name_val}"
    - op: replace
      path: /metadata/name
      value: after-{deployment_name}"""
    return patch_block


def replace_job_patches(content, deployment_name, csi_project_name):
    """Task 3: Replace all Job targets in patchesJSON6902/patchesJson6902 with new format.

    If multiple patchesJSON6902 sections exist (duplicate YAML key), merges them into one.
    Comments out existing Job targets and adds new sync-presync/sync-postsync targets.
    Preserves Deployment targets untouched.

    Returns (new_content, changed, details)
    """
    lines = content.split("\n")
    changes = []
    patches_key_pattern = re.compile(r'^(patchesJSON6902|patchesJson6902)\s*:\s*$', re.IGNORECASE)

    # First pass: find ALL patchesJson6902 section start lines and their boundaries
    sections = []  # List of (start_idx, end_idx, [(target_start, target_end, kind, name)])

    section_starts = []
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if patches_key_pattern.match(stripped):
            section_starts.append(idx)

    if not section_starts:
        return content, False, ["No patchesJson6902 section found"]

    for sec_start in section_starts:
        # Section ends at: next top-level key or EOF
        section_end = len(lines) - 1
        for idx in range(sec_start + 1, len(lines)):
            line = lines[idx]
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not line.startswith(" ") and not line.startswith("\t") and not stripped.startswith("-"):
                section_end = idx - 1
                break

        # Parse targets within this section
        targets = []
        current_target_start = None
        current_kind = None
        current_name = None

        for idx in range(sec_start + 1, section_end + 1):
            line = lines[idx]
            stripped = line.strip()

            if re.match(r'\s*-\s*target:\s*$', line):
                if current_target_start is not None:
                    targets.append((current_target_start, idx - 1, current_kind, current_name))
                current_target_start = idx
                current_kind = None
                current_name = None
                continue

            if current_target_start is not None:
                kind_match = re.match(r'\s*kind:\s*(\S+)', stripped)
                if kind_match:
                    current_kind = kind_match.group(1)
                name_match = re.match(r'\s*name:\s*(.+)', stripped)
                if name_match and current_kind and not current_name:
                    current_name = name_match.group(1).strip()

        if current_target_start is not None:
            targets.append((current_target_start, section_end, current_kind, current_name))

        sections.append((sec_start, section_end, targets))

    # Collect all Job targets across all sections
    all_job_targets = []
    has_jobs = False
    for sec_start, sec_end, targets in sections:
        for t in targets:
            if t[2] == "Job":
                all_job_targets.append(t)
                has_jobs = True

    if not has_jobs:
        return content, False, ["No Job targets found to replace"]

    # Check if already in new format
    has_sync_presync = any(n == "sync-presync" for _, _, _, n in all_job_targets)
    has_sync_postsync = any(n == "sync-postsync" for _, _, _, n in all_job_targets)
    if has_sync_presync and has_sync_postsync:
        return content, False, ["Already has sync-presync/sync-postsync format"]

    # If there are multiple sections, merge them into one:
    # - Keep the FIRST section's key line
    # - Remove duplicate section key lines
    # - Move non-Job targets from later sections into the first section
    # - Comment out all old Job targets
    # - Add new Job targets after the first section key

    first_sec_start = sections[0][0]
    first_sec_end = sections[0][1]
    duplicate_key_lines = set()  # lines to remove (duplicate patchesJson6902: keys)
    non_job_targets_to_move = []  # (lines_text) from later sections to append to first
    all_job_line_ranges = set()

    for i, (sec_start, sec_end, targets) in enumerate(sections):
        if i > 0:
            # Mark duplicate key line for removal
            duplicate_key_lines.add(sec_start)
            changes.append(f"Merged duplicate patchesJson6902 section (line {sec_start + 1})")

        for t_start, t_end, kind, name in targets:
            if kind == "Job":
                # Mark Job lines for commenting out
                for line_num in range(t_start, t_end + 1):
                    all_job_line_ranges.add(line_num)
            elif i > 0:
                # Non-Job target from a later section -> collect to move to first section
                target_lines = []
                for line_num in range(t_start, t_end + 1):
                    target_lines.append(lines[line_num])
                non_job_targets_to_move.append(target_lines)
                # Mark these lines for removal (they'll be moved)
                for line_num in range(t_start, t_end + 1):
                    duplicate_key_lines.add(line_num)

    # Generate new job block
    new_job_block = generate_new_job_patches(deployment_name, csi_project_name)

    # Build result
    result_lines = []
    for idx, line in enumerate(lines):
        # Skip duplicate key lines and moved target lines
        if idx in duplicate_key_lines:
            continue

        if idx in all_job_line_ranges:
            # Comment out old Job target lines (preserve indentation)
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                lstripped = line.lstrip()
                indent = line[:len(line) - len(lstripped)]
                result_lines.append(f"{indent}# {lstripped}")
                changes.append(f"Commented out line {idx + 1}: {stripped[:60]}")
            else:
                result_lines.append(line)
        else:
            result_lines.append(line)

        # After the first section key, insert new Job targets
        if idx == first_sec_start:
            for new_line in new_job_block.split("\n"):
                result_lines.append(new_line)
            changes.append("Added new sync-presync/sync-postsync Job patches")

        # After the first section ends, insert non-Job targets moved from duplicate sections
        if idx == first_sec_end and non_job_targets_to_move:
            for target_lines in non_job_targets_to_move:
                for tl in target_lines:
                    result_lines.append(tl)
                changes.append("Moved non-Job target from duplicate section into merged section")

    new_content = "\n".join(result_lines)
    return new_content, True, changes


def update_deployment_target_name(content, deployment_name):
    """Task 2: Update Deployment target name in patchesJSON6902.

    Returns (new_content, changed, details)
    """
    lines = content.split("\n")
    result = []
    in_patches_json = False
    in_target = False
    found_deployment_kind = False
    changes = []

    patches_key_pattern = re.compile(r'(patchesJSON6902|patchesJson6902)\s*:', re.IGNORECASE)

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Detect patchesJson6902 section (not commented out)
        if not stripped.startswith("#") and patches_key_pattern.search(stripped):
            in_patches_json = True
            result.append(line)
            i += 1
            continue

        if in_patches_json:
            # Detect end of section
            if stripped and not stripped.startswith("#") and not stripped.startswith("-") and not line.startswith(" ") and not line.startswith("\t"):
                in_patches_json = False
                in_target = False
                found_deployment_kind = False
                result.append(line)
                i += 1
                continue

            # Detect new "- target:" block
            if re.match(r'\s*-\s*target:\s*$', line):
                in_target = True
                found_deployment_kind = False
                result.append(line)
                i += 1
                continue

            if in_target:
                if re.match(r'\s*kind:\s*Deployment\s*$', stripped):
                    found_deployment_kind = True
                    result.append(line)
                    i += 1
                    continue

                name_match = re.match(r'(\s*name:\s*)(.*)', line)
                if name_match and found_deployment_kind:
                    old_name = name_match.group(2).strip()
                    if old_name != deployment_name:
                        indent_part = name_match.group(1)
                        result.append(f"{indent_part}{deployment_name}")
                        changes.append(f"Updated Deployment target name: {old_name} -> {deployment_name}")
                        i += 1
                        continue

                if stripped.startswith("patch:"):
                    in_target = False
                    found_deployment_kind = False
                elif re.match(r'\s*-\s*target:\s*$', line):
                    found_deployment_kind = False

        result.append(line)
        i += 1

    new_content = "\n".join(result)
    return new_content, bool(changes), changes


def process_kustomization_file(kust_file, deployment_name, csi_project_name, dry_run=False):
    """Process a single kustomization.yaml file for DM-Initiator update.

    Applies:
    - Task 1: Replace Sync references with DM-Initiator
    - Task 2: Update Deployment target names
    - Task 3: Replace Job patches with new format
    """
    
    with open(kust_file, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    all_changes = []

    # Task 1: Replace Sync references
    content, changed, changes = replace_sync_with_dm_initiator(content)
    if changed:
        all_changes.extend(changes)

    # Task 2: Update Deployment target name
    if deployment_name:
        content, changed, changes = update_deployment_target_name(content, deployment_name)
        if changed:
            all_changes.extend(changes)

    # Task 3: Replace Job patches with new format
    if deployment_name and csi_project_name:
        # Only replace Job patches if there are Sync/DM-Initiator resources
        has_sync_or_dm = ("Sync-new" in original or "Sync-DM" in original or
                          "Sync/" in original or "DM-Initiator" in original or
                          "DM-Initiator" in content)
        if has_sync_or_dm:
            content, changed, changes = replace_job_patches(content, deployment_name, csi_project_name)
            if changed:
                all_changes.extend(changes)

    if content != original and not dry_run:
        with open(kust_file, "w", encoding="utf-8") as f:
            f.write(content)

    return all_changes


def process_repo(repo_name, repo_path, deploy_map, onering_names, dry_run=False):
    """Process a single repo for DM-Initiator update."""
    repo_path = Path(repo_path)
    prod_dir = repo_path / "PROD"

    if not prod_dir.exists():
        print(f"  PROD directory not found")
        return False, []

    # Check 1: DM-Initiator folder exists
    dm_initiator_dir = repo_path / "DM-Initiator"
    if not dm_initiator_dir.exists():
        print(f"  SKIP: No DM-Initiator folder in repo root")
        return False, []

    # Check 2: Version conditions
    conditions_met, base_tag, iam_tag, details = check_version_conditions(repo_path)
    print(f"    {details}")

    if not conditions_met:
        print(f"  SKIP: Version conditions not met")
        return False, []

    print(f"  Version conditions MET - proceeding with DM-Initiator update")

    # Git: checkout PROD-standardize-folder-names, delete old branch if exists, create new branch
    if not dry_run:
        try:
            git_run(repo_path, "checkout", "PROD-standardize-folder-names")
            print(f"  Checked out PROD-standardize-folder-names")
        except RuntimeError as e:
            print(f"  ERROR checking out PROD-standardize-folder-names: {e}")
            return False, []

        # Delete old branch if exists
        result = git_run(repo_path, "branch", "--list", BRANCH_NAME, check=False)
        if BRANCH_NAME in result.stdout:
            git_run(repo_path, "branch", "-D", BRANCH_NAME, check=False)
            print(f"  Deleted old branch '{BRANCH_NAME}'")

        try:
            git_run(repo_path, "checkout", "-b", BRANCH_NAME)
            print(f"  Created branch '{BRANCH_NAME}'")
        except RuntimeError as e:
            print(f"  ERROR creating branch: {e}")
            return False, []

    # Find all kustomization files in PROD
    kust_files = sorted(prod_dir.rglob("kustomization.yaml"))
    print(f"  Found {len(kust_files)} kustomization files")

    log_entries = []
    total_changes = 0

    for kust_file in kust_files:
        rel_path = str(kust_file.parent.relative_to(prod_dir))

        # Determine deployment name for this service
        deployment_name = deploy_map.get(rel_path)

        # If no direct match, try matching by service folder name
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

        # If still no deployment name, use service folder name as fallback
        if not deployment_name:
            deployment_name = rel_path.split("/")[-1]

        # Find CSI_PROJECT_NAME
        service_folder = rel_path.split("/")[-1]
        csi_project_name = find_csi_project_name(service_folder, onering_names)

        changes = process_kustomization_file(kust_file, deployment_name, csi_project_name, dry_run)

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
                f"Add DM-Initiator and replace Sync references in PROD\n\n"
                f"- Replaced Sync-new/Sync-DM/Sync resources with DM-Initiator\n"
                f"- Replaced old Job patches with standardized sync-presync/sync-postsync format\n"
                f"- Updated CSI_PROJECT_NAME from onering repo names\n"
                f"- Updated Deployment target names\n"
                f"\n{total_changes} changes across {len(set(e[0] for e in log_entries))} services"
            )
            git_run(repo_path, "commit", "-m", commit_msg)
            print(f"  Committed changes")
        except RuntimeError as e:
            if "nothing to commit" in str(e):
                print(f"  No changes to commit")
            else:
                print(f"  ERROR committing: {e}")

    return True, log_entries


def write_log(repo_name, log_entries, conditions_met, base_tag, iam_tag, dry_run):
    """Write execution log for a repo."""
    log_dir = OUTPUT_DIR / repo_name
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "dm_initiator_log_prod.md"

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# DM-Initiator Update Log - {repo_name}\n\n")
        f.write(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}\n\n")
        f.write(f"## Version Check\n\n")
        f.write(f"- base-utility-service-java-sev: `{base_tag or 'N/A'}`\n")
        f.write(f"  - Threshold: `{BASE_UTILITY_THRESHOLD}`\n")
        f.write(f"- csi-iam-service: `{iam_tag or 'N/A'}`\n")
        f.write(f"  - Threshold: `{CSI_IAM_THRESHOLD}`\n")
        f.write(f"- **Conditions met: {'YES' if conditions_met else 'NO'}**\n\n")

        if log_entries:
            f.write(f"## Changes ({len(log_entries)} total)\n\n")
            f.write("| Service | Change |\n")
            f.write("|---------|--------|\n")
            for rel_path, change in log_entries:
                f.write(f"| `{rel_path}` | {change} |\n")
        else:
            f.write("## No changes applied\n")

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
    print(f"{'=' * 60}")
    print(f"  DM-Initiator Updater - Mode: {mode}")
    print(f"{'=' * 60}\n")

    print("Loading onering repo names...")
    onering_names = load_onering_names()
    print(f"Loaded {len(onering_names)} repo names\n")

    print("Scanning DEPLOYMENT-BASE-REPO for deployment names...")
    deploy_map = build_deployment_name_map()
    print(f"Found {len(deploy_map)} deployments\n")

    print(f"Thresholds:")
    print(f"  base-utility: >= {BASE_UTILITY_THRESHOLD}")
    print(f"  csi-iam:      >= {CSI_IAM_THRESHOLD}\n")

    for repo_name, repo_path in repos.items():
        print(f"\n{'=' * 40}")
        print(f"[{repo_name}]")
        print(f"{'=' * 40}")

        # Check DM-Initiator existence first
        dm_exists = (Path(repo_path) / "DM-Initiator").exists()
        print(f"  DM-Initiator folder: {'EXISTS' if dm_exists else 'NOT FOUND'}")

        if not dm_exists:
            print(f"  SKIP: No DM-Initiator folder")
            write_log(repo_name, [], False, None, None, dry_run)
            continue

        # Check versions
        conditions_met, base_tag, iam_tag, details = check_version_conditions(repo_path)
        print(f"    {details}")

        if not conditions_met:
            print(f"  SKIP: Version conditions not met")
            write_log(repo_name, [], False, base_tag, iam_tag, dry_run)
            continue

        print(f"  PASS: Both version conditions met")

        # Process the repo
        processed, log_entries = process_repo(repo_name, repo_path, deploy_map, onering_names, dry_run)
        write_log(repo_name, log_entries, conditions_met, base_tag, iam_tag, dry_run)

    print(f"\n{'=' * 60}")
    print("Done!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
