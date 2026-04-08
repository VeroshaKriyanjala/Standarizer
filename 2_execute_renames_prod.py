import os
import subprocess
import sys
from pathlib import Path

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
OUTPUT_DIR = Path(__file__).parent / "output"
BRANCH_NAME = "PROD-standardize-folder-names"


def parse_rename_plan(plan_file):
    """Parse prod_rename_plan.md and extract only the Planned Renames."""
    renames = []
    in_planned_section = False

    with open(plan_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("## Planned Renames"):
                in_planned_section = True
                continue
            elif line.startswith("## ") or line.startswith("---"):
                in_planned_section = False
                continue

            if in_planned_section and "PROD/" in line:
                # Table format: | `PROD/old_name` | `PROD/new_name` |
                parts = line.split("|")
                if len(parts) >= 3:
                    old_cell = parts[1].strip().strip("`").strip()
                    new_cell = parts[2].strip().strip("`").strip()
                    if old_cell.startswith("PROD/") and new_cell.startswith("PROD/"):
                        old_rel = old_cell.replace("PROD/", "", 1)
                        new_rel = new_cell.replace("PROD/", "", 1)
                        if old_rel != new_rel:
                            renames.append((old_rel, new_rel))

    return renames


def git_run(repo_path, *args, check=True):
    """Run a git command in the given repo."""
    result = subprocess.run(
        ["git", "-C", str(repo_path)] + list(args),
        capture_output=True, text=True,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


def create_branch(repo_path, branch_name):
    """Create a new branch from main. Returns True on success."""
    try:
        git_run(repo_path, "checkout", "main")
        git_run(repo_path, "branch", "-D", branch_name, check=False)
        git_run(repo_path, "checkout", "-b", branch_name)
        return True
    except RuntimeError as e:
        print(f"  ERROR creating branch: {e}")
        return False


def execute_for_repo(repo_name, repo_path, dry_run=False):
    plan_file = OUTPUT_DIR / repo_name / "prod_rename_plan.md"
    prod_dir = Path(repo_path) / "PROD"

    if not plan_file.exists():
        print(f"  prod_rename_plan.md not found. Run plan_prod_renames.py first.")
        return

    if not prod_dir.exists():
        print(f"  PROD directory not found at {prod_dir}")
        return

    # Parse the rename plan
    renames = parse_rename_plan(plan_file)
    if not renames:
        print(f"  No planned renames found in {plan_file}")
        return

    print(f"  Found {len(renames)} planned renames")

    if dry_run:
        print(f"  [DRY RUN] Would create branch '{BRANCH_NAME}' and apply:")
        for old_rel, new_rel in renames:
            print(f"    PROD/{old_rel} -> PROD/{new_rel}")
        return

    # Step 1: Create branch from main
    if not create_branch(repo_path, BRANCH_NAME):
        return
    print(f"  Created branch '{BRANCH_NAME}'")

    # Step 2: Execute renames in PROD on the new branch
    # Sort by depth (deepest first) to avoid renaming a parent before its child
    renames.sort(key=lambda x: x[0].count("/"), reverse=True)

    success = 0
    failed = 0
    renamed_list = []
    skipped_list = []

    for old_rel, new_rel in renames:
        old_path = prod_dir / old_rel
        new_path = prod_dir / new_rel

        if not old_path.exists():
            print(f"  SKIP (not found): {old_rel}")
            skipped_list.append((old_rel, new_rel, "not found"))
            failed += 1
            continue

        if new_path.exists():
            print(f"  SKIP (target exists): {new_rel}")
            skipped_list.append((old_rel, new_rel, "target exists"))
            failed += 1
            continue

        # Ensure parent directory exists
        new_path.parent.mkdir(parents=True, exist_ok=True)

        os.rename(old_path, new_path)
        print(f"  RENAMED: {old_rel} -> {new_rel}")
        renamed_list.append((old_rel, new_rel))
        success += 1

    print(f"\n  Result: {success} renamed, {failed} skipped")

    # Step 3: Commit changes on the branch
    if success > 0:
        try:
            git_run(repo_path, "add", "-A")
            git_run(repo_path, "commit", "-m",
                    f"Standardize PROD folder names\n\nRenamed {success} folders to match DEPLOYMENT-BASE-REPO structure.")
            print(f"  Committed changes on branch '{BRANCH_NAME}'")
        except RuntimeError as e:
            print(f"  ERROR committing: {e}")

    # Switch back to main
    git_run(repo_path, "checkout", "main", check=False)
    print(f"  Switched back to main")

    # Write execution log
    log_file = OUTPUT_DIR / repo_name / "rename_execution_log.md"
    (OUTPUT_DIR / repo_name).mkdir(parents=True, exist_ok=True)
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# Rename Execution Log - {repo_name}\n\n")
        f.write(f"Branch: `{BRANCH_NAME}`\n")
        f.write(f"Source: `{prod_dir}`\n\n")
        f.write(f"Renamed: {success}, Skipped: {failed}\n\n")

        if renamed_list:
            f.write("## Renamed\n\n")
            f.write("| Old Name | New Name |\n")
            f.write("|---|---|\n")
            for old_rel, new_rel in renamed_list:
                f.write(f"| `{old_rel}` | `{new_rel}` |\n")
            f.write("\n")

        if skipped_list:
            f.write("## Skipped\n\n")
            f.write("| Old Name | New Name | Reason |\n")
            f.write("|---|---|---|\n")
            for old_rel, new_rel, reason in skipped_list:
                f.write(f"| `{old_rel}` | `{new_rel}` | {reason} |\n")
            f.write("\n")

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
    print(f"Branch: {BRANCH_NAME}\n")

    for repo_name, repo_path in repos.items():
        print(f"[{repo_name}]")
        execute_for_repo(repo_name, repo_path, dry_run=dry_run)
        print()

    print("Done!")


if __name__ == "__main__":
    main()
