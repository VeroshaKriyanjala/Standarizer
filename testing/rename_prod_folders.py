#!/usr/bin/env python3
"""
Rename PROD service folders to match the current UAT standard names.

Reads final.md for rename mappings (Previous Name → Current Name).
For each repo, creates a new branch from main, then renames PROD folders
that still use old names to the new standard names.

Logs: what was renamed, what was already correct, mismatches, and errors.
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

FINAL_MD = Path(__file__).parent.parent / "output" / "final.md"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

REPOS = {
    "KKUH": Path("/home/verosha/Documents/gittea/KKUH"),
    "Alibaba": Path("/home/verosha/Documents/gittea/Alibaba"),
    "WAVE1": Path("/home/verosha/Documents/gittea/WAVE1"),
    "CS": Path("/home/verosha/Documents/gittea/CS"),
    "KAUH": Path("/home/verosha/Documents/gittea/KAUH"),
    "S2": Path("/home/verosha/Documents/gittea/S2"),
    "S3": Path("/home/verosha/Documents/gittea/S3"),
    "HMG": Path("/home/verosha/Documents/gittea/HMG"),
}

SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode", "PreSync"}
BRANCH_NAME = "PROD-standardize-folder-names"


def parse_final_md(filepath: Path) -> list:
    """
    Parse final.md to extract rename mappings.
    Returns list of (current_path, previous_path) tuples.
    Some current folders have multiple previous names (multi-step renames).
    """
    content = filepath.read_text(encoding="utf-8")
    mappings = []

    current = None
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("Current Folder:"):
            current = line.split(":", 1)[1].strip()
        elif line.startswith("Previous Name:") and current:
            previous = line.split(":", 1)[1].strip()
            mappings.append((current, previous))
            current = None

    return mappings


def build_rename_map(mappings: list) -> dict:
    """
    Build {old_service_name: new_service_name} from the mappings.
    Handles both module/service level and module-level renames.

    For service-level: UAT/module/old-name → module/old-name: module/new-name
    For module-level: UAT/api-gateway → api-gateway: apigateway (the current is apigateway)
    """
    rename_map = {}

    for current, previous in mappings:
        # Strip "UAT/" prefix
        curr = current.replace("UAT/", "", 1)
        prev = previous.replace("UAT/", "", 1)

        # Skip if they're the same
        if curr == prev:
            continue

        # Map old name → new name
        # If old name already has a mapping, keep the latest (could be multi-step)
        rename_map[prev] = curr

    return rename_map


def get_prod_services(prod_dir: Path) -> dict:
    """
    Get all services in PROD folder.
    Returns {relative_path: absolute_path} for both module-level and service-level.
    """
    services = {}
    if not prod_dir.exists():
        return services

    for module in sorted(prod_dir.iterdir()):
        if not module.is_dir() or module.name in SKIP:
            continue

        subdirs = [d for d in module.iterdir() if d.is_dir() and d.name not in SKIP]
        if subdirs:
            # Module with sub-services
            for sub in sorted(subdirs):
                rel = f"{module.name}/{sub.name}"
                services[rel] = sub
        else:
            # Standalone (could be module-level like otp-service)
            services[module.name] = module

    return services


def create_branch(repo_path: Path, branch_name: str) -> bool:
    """Create a new branch from main. Returns True on success."""
    try:
        # Make sure we're on main
        subprocess.run(
            ["git", "-C", str(repo_path), "checkout", "main"],
            capture_output=True, text=True, check=True,
        )
        # Delete branch if it already exists
        subprocess.run(
            ["git", "-C", str(repo_path), "branch", "-D", branch_name],
            capture_output=True, text=True,
        )
        # Create new branch
        subprocess.run(
            ["git", "-C", str(repo_path), "checkout", "-b", branch_name],
            capture_output=True, text=True, check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ERROR creating branch: {e.stderr}")
        return False


def process_repo(repo_name: str, repo_path: Path, rename_map: dict) -> dict:
    """Process a single repo: rename PROD folders that match old names."""
    print(f"\n[{repo_name}]")

    prod_dir = repo_path / "PROD"
    if not prod_dir.exists():
        print(f"  ERROR: PROD folder not found at {prod_dir}")
        return {"repo": repo_name, "renamed": [], "already_correct": [],
                "not_found": [], "errors": []}

    # Create branch
    if not create_branch(repo_path, BRANCH_NAME):
        return {"repo": repo_name, "renamed": [], "already_correct": [],
                "not_found": [], "errors": [{"msg": "Failed to create branch"}]}

    # Get current PROD services
    prod_services = get_prod_services(prod_dir)
    print(f"  Found {len(prod_services)} services in PROD")

    renamed = []
    already_correct = []
    not_found = []
    errors = []

    # Check each rename mapping
    processed_current = set()
    for old_name, new_name in rename_map.items():
        # Check if the old name exists in PROD
        if old_name in prod_services:
            old_path = prod_services[old_name]

            # Determine the new path
            if "/" in new_name:
                new_module, new_service = new_name.split("/", 1)
                new_path = prod_dir / new_module / new_service
            else:
                new_path = prod_dir / new_name

            # Check if new name already exists
            if new_path.exists():
                errors.append({
                    "old": old_name,
                    "new": new_name,
                    "msg": f"Target path already exists: {new_path.name}",
                })
                continue

            # Rename
            try:
                new_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(old_path), str(new_path))
                renamed.append({"old": old_name, "new": new_name})
                print(f"  RENAMED: {old_name} → {new_name}")
            except Exception as e:
                errors.append({
                    "old": old_name,
                    "new": new_name,
                    "msg": str(e),
                })
            processed_current.add(new_name)

        elif new_name in prod_services:
            # Already has the correct name
            already_correct.append({"name": new_name})
            processed_current.add(new_name)

    # Check for old names not found in this repo's PROD
    all_old_names = set(rename_map.keys())
    all_new_names = set(rename_map.values())
    for old_name in sorted(all_old_names):
        new_name = rename_map[old_name]
        if old_name not in prod_services and new_name not in prod_services:
            not_found.append({"old": old_name, "new": new_name})

    print(f"  Renamed: {len(renamed)}")
    print(f"  Already correct: {len(already_correct)}")
    print(f"  Not in PROD: {len(not_found)}")
    print(f"  Errors: {len(errors)}")

    # Switch back to main after processing
    subprocess.run(
        ["git", "-C", str(repo_path), "checkout", "main"],
        capture_output=True, text=True,
    )

    return {
        "repo": repo_name,
        "renamed": renamed,
        "already_correct": already_correct,
        "not_found": not_found,
        "errors": errors,
    }


def write_report(all_results: list, rename_map: dict, output_file: Path):
    """Write the rename report."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# PROD Folder Rename Report\n\n")
        f.write(f"Renames PROD service folders from old names to current UAT standard names.\n")
        f.write(f"Based on {len(rename_map)} rename mappings from `final.md`.\n\n")
        f.write(f"Branch: `{BRANCH_NAME}`\n\n")

        total_renamed = 0
        total_correct = 0
        total_not_found = 0
        total_errors = 0

        for result in all_results:
            repo = result["repo"]
            f.write(f"## {repo}\n\n")

            # Renamed
            if result["renamed"]:
                f.write(f"### Renamed ({len(result['renamed'])})\n\n")
                f.write("| Old Name | New Name |\n")
                f.write("|---|---|\n")
                for r in result["renamed"]:
                    f.write(f"| `{r['old']}` | `{r['new']}` |\n")
                f.write("\n")
            total_renamed += len(result["renamed"])

            # Already correct
            if result["already_correct"]:
                f.write(f"### Already Correct ({len(result['already_correct'])})\n\n")
                f.write("| Service Name |\n")
                f.write("|---|\n")
                for r in result["already_correct"]:
                    f.write(f"| `{r['name']}` |\n")
                f.write("\n")
            total_correct += len(result["already_correct"])

            # Not found
            if result["not_found"]:
                f.write(f"### Not in PROD ({len(result['not_found'])})\n\n")
                f.write("Neither old nor new name exists in this repo's PROD.\n\n")
                f.write("| Old Name | Expected New Name |\n")
                f.write("|---|---|\n")
                for r in result["not_found"]:
                    f.write(f"| `{r['old']}` | `{r['new']}` |\n")
                f.write("\n")
            total_not_found += len(result["not_found"])

            # Errors
            if result["errors"]:
                f.write(f"### Errors ({len(result['errors'])})\n\n")
                f.write("| Old Name | New Name | Error |\n")
                f.write("|---|---|---|\n")
                for r in result["errors"]:
                    f.write(f"| `{r['old']}` | `{r['new']}` | {r['msg']} |\n")
                f.write("\n")
            total_errors += len(result["errors"])

            f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write("| Metric | Count |\n")
        f.write("|---|---|\n")
        f.write(f"| Repos processed | {len(all_results)} |\n")
        f.write(f"| Total renames applied | {total_renamed} |\n")
        f.write(f"| Already correct | {total_correct} |\n")
        f.write(f"| Not in PROD | {total_not_found} |\n")
        f.write(f"| Errors | {total_errors} |\n")
        f.write("\n")

        # Per-repo summary table
        f.write("### Per-Repo Breakdown\n\n")
        f.write("| Repo | Renamed | Already Correct | Not in PROD | Errors |\n")
        f.write("|---|:---:|:---:|:---:|:---:|\n")
        for result in all_results:
            f.write(f"| {result['repo']} | {len(result['renamed'])} | "
                    f"{len(result['already_correct'])} | {len(result['not_found'])} | "
                    f"{len(result['errors'])} |\n")
        f.write("\n")


def main():
    repo_names = sys.argv[1:] if len(sys.argv) > 1 else list(REPOS.keys())

    print("Parsing final.md...")
    mappings = parse_final_md(FINAL_MD)
    print(f"  Found {len(mappings)} rename entries")

    rename_map = build_rename_map(mappings)
    print(f"  Built {len(rename_map)} unique old→new mappings")

    # Show the mappings
    print("\n  Rename mappings:")
    for old, new in sorted(rename_map.items()):
        print(f"    {old} → {new}")

    all_results = []
    for repo_name in repo_names:
        if repo_name not in REPOS:
            print(f"Unknown repo: {repo_name}")
            continue
        result = process_repo(repo_name, REPOS[repo_name], rename_map)
        all_results.append(result)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / "prod_rename_report.md"
    write_report(all_results, rename_map, output_file)
    print(f"\nReport saved to {output_file}")


if __name__ == "__main__":
    main()
