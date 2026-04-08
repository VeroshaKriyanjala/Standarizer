import re
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

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
FINAL_MD = OUTPUT_DIR / "final.md"
SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode", "PreSync"}


def parse_final_md(filepath: Path) -> dict:
    """Parse final.md to extract {current_folder: [previous_folders]} mappings."""
    content = filepath.read_text(encoding="utf-8")
    mappings = defaultdict(list)
    current = None
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("Current Folder:"):
            current = line.split(":", 1)[1].strip()
        elif line.startswith("Previous Name:") and current:
            previous = line.split(":", 1)[1].strip()
            mappings[current].append(previous)
            current = None
    return dict(mappings)


def build_rename_map(final_mappings: dict) -> dict:
    """Build {old_name: new_name} from final.md mappings (strip UAT/ prefix).

    Handles multiple previous names per current folder (intermediate renames).
    """
    rename_map = {}
    for current, previous_list in final_mappings.items():
        curr = current.replace("UAT/", "", 1)
        for previous in previous_list:
            prev = previous.replace("UAT/", "", 1)
            if curr != prev:
                rename_map[prev] = curr
    return rename_map


def get_prod_services(prod_dir: Path) -> dict:
    """Get all module/service pairs in PROD. Returns {relative_path: absolute_path}."""
    services = {}
    if not prod_dir.exists():
        return services
    for module in sorted(prod_dir.iterdir()):
        if not module.is_dir() or module.name in SKIP:
            continue
        subdirs = [d for d in module.iterdir() if d.is_dir() and d.name not in SKIP]
        if subdirs:
            for sub in sorted(subdirs):
                rel = f"{module.name}/{sub.name}"
                services[rel] = sub
        else:
            services[module.name] = module
    return services


def get_dir_from_filepath(filepath: str) -> str:
    """Extract directory path (PROD/module/service) from a file path."""
    parts = filepath.split("/")
    if len(parts) >= 3:
        return "/".join(parts[:3])
    return filepath


def get_git_renames_prod(repo_path: str) -> dict:
    """
    Discover PROD folder renames from git history.
    Returns {current_folder: previous_folder}.
    Uses per-commit majority voting to avoid cross-matching.
    """
    try:
        result = subprocess.run(
            [
                "git", "-C", repo_path,
                "log", "--all", "--format=COMMIT %H",
                "--diff-filter=R", "--name-status", "-M",
                "--", "PROD/",
            ],
            capture_output=True, text=True, timeout=120,
        )
        output = result.stdout
    except Exception as e:
        print(f"  ERROR running git: {e}")
        return {}

    all_renames = {}
    commits = []
    current_commit_renames = []

    for line in output.splitlines():
        line = line.strip()
        if line.startswith("COMMIT "):
            if current_commit_renames:
                commits.append(current_commit_renames)
            current_commit_renames = []
        elif line.startswith("R"):
            match = re.match(r"R\d+\t(.+)\t(.+)", line)
            if match:
                old_file, new_file = match.group(1), match.group(2)
                old_dir = get_dir_from_filepath(old_file)
                new_dir = get_dir_from_filepath(new_file)
                if old_dir != new_dir:
                    current_commit_renames.append((old_dir, new_dir))

    if current_commit_renames:
        commits.append(current_commit_renames)

    for commit_renames in commits:
        src_to_targets = defaultdict(lambda: defaultdict(int))
        for old_dir, new_dir in commit_renames:
            src_to_targets[old_dir][new_dir] += 1

        for src_dir, targets in src_to_targets.items():
            best_target = max(targets, key=targets.get)
            if src_dir != best_target:
                if best_target not in all_renames:
                    all_renames[best_target] = src_dir

    return all_renames


def plan_for_repo(repo_name, repo_path, rename_map, final_mappings):
    out_dir = OUTPUT_DIR / repo_name
    prod_dir = Path(repo_path) / "PROD"
    output_file = out_dir / "prod_rename_plan.md"

    if not prod_dir.exists():
        print(f"  PROD directory not found at {prod_dir}")
        return

    # Get current PROD services
    prod_services = get_prod_services(prod_dir)
    print(f"  Found {len(prod_services)} services in PROD")

    # Get git rename history for PROD
    git_renames = get_git_renames_prod(repo_path)
    print(f"  Found {len(git_renames)} folder renames in PROD git history")

    # --- Section 1: Planned renames from final.md ---
    planned_renames = []
    already_correct = []
    not_in_prod = []

    for old_name, new_name in sorted(rename_map.items()):
        if old_name in prod_services:
            planned_renames.append((old_name, new_name))
        elif new_name in prod_services:
            already_correct.append((old_name, new_name))
        else:
            not_in_prod.append((old_name, new_name))

    # --- Section 2: Git history analysis (matches, git-only, mismatches) ---
    # Build final.md mappings with PROD/ prefix for comparison
    # Maps {prod_current: [prod_previous_list]}
    final_prod_mappings = defaultdict(list)
    for current, previous_list in final_mappings.items():
        prod_current = current.replace("UAT/", "PROD/", 1)
        for previous in previous_list:
            prod_previous = previous.replace("UAT/", "PROD/", 1)
            final_prod_mappings[prod_current].append(prod_previous)

    matches = []
    mismatches = []
    git_only = []

    all_dirs = set(git_renames.keys()) | set(final_prod_mappings.keys())
    for current_dir in sorted(all_dirs):
        in_git = current_dir in git_renames
        in_final = current_dir in final_prod_mappings

        if in_git and in_final:
            git_prev = git_renames[current_dir]
            final_prev_list = final_prod_mappings[current_dir]
            if git_prev in final_prev_list:
                matches.append({"current": current_dir, "previous": git_prev})
            else:
                mismatches.append({
                    "current": current_dir,
                    "git_previous": git_prev,
                    "final_previous": ", ".join(final_prev_list),
                })
        elif in_git and not in_final:
            git_only.append({
                "current": current_dir,
                "previous": git_renames[current_dir],
            })

    print(f"  Planned renames: {len(planned_renames)}")
    print(f"  Already correct: {len(already_correct)}")
    print(f"  Not in PROD: {len(not_in_prod)}")
    print(f"  Git matches: {len(matches)}")
    print(f"  Git-only renames: {len(git_only)}")
    print(f"  Mismatches: {len(mismatches)}")

    # Find unaffected PROD folders
    all_old = set(rename_map.keys())
    all_new = set(rename_map.values())
    unaffected = sorted([s for s in prod_services if s not in all_old and s not in all_new])

    # Write report
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# PROD Folder Rename Plan - {repo_name}\n\n")
        f.write("Based on UAT rename history (`final.md`) and PROD git history.\n\n")

        # Planned Renames
        f.write(f"## Planned Renames ({len(planned_renames)})\n\n")
        f.write("Old name found in PROD, will be renamed to new standard name.\n\n")
        if planned_renames:
            f.write("| Old Name (in PROD) | New Name (standard) |\n")
            f.write("|---|---|\n")
            for prev, curr in planned_renames:
                f.write(f"| `PROD/{prev}` | `PROD/{curr}` |\n")
        else:
            f.write("No matching folders found to rename.\n")
        f.write("\n")

        # Already Correct
        f.write(f"## Already Correct ({len(already_correct)})\n\n")
        f.write("PROD already has the new standard name.\n\n")
        if already_correct:
            f.write("| Service Name |\n")
            f.write("|---|\n")
            for _, new_name in already_correct:
                f.write(f"| `PROD/{new_name}` |\n")
        else:
            f.write("None.\n")
        f.write("\n")

        # Not in PROD
        f.write(f"## Not in PROD ({len(not_in_prod)})\n\n")
        f.write("Neither old nor new name exists in this repo's PROD.\n\n")
        if not_in_prod:
            f.write("| Old Name | Expected New Name |\n")
            f.write("|---|---|\n")
            for prev, curr in not_in_prod:
                f.write(f"| `{prev}` | `{curr}` |\n")
        else:
            f.write("All services accounted for.\n")
        f.write("\n")

        f.write("---\n\n")

        # Git History: Matches
        f.write(f"## Git History - Matches ({len(matches)})\n\n")
        f.write("PROD git rename history **agrees** with `final.md`.\n\n")
        if matches:
            f.write("| Current Folder | Previous Name |\n")
            f.write("|---|---|\n")
            for m in matches:
                f.write(f"| `{m['current']}` | `{m['previous']}` |\n")
        else:
            f.write("No matches found.\n")
        f.write("\n")

        # Git History: Git-only renames
        f.write(f"## Git History - Git-only Renames ({len(git_only)})\n\n")
        f.write("Renames found in PROD git history but **NOT** in `final.md`.\n\n")
        if git_only:
            f.write("| Current Folder | Previous Name |\n")
            f.write("|---|---|\n")
            for m in git_only:
                f.write(f"| `{m['current']}` | `{m['previous']}` |\n")
        else:
            f.write("None.\n")
        f.write("\n")

        # Git History: Mismatches
        f.write(f"## Git History - Mismatches ({len(mismatches)})\n\n")
        f.write("Same current folder, but git and `final.md` disagree on previous name.\n\n")
        if mismatches:
            f.write("| Current Folder | Git Previous | final.md Previous |\n")
            f.write("|---|---|---|\n")
            for m in mismatches:
                f.write(f"| `{m['current']}` | `{m['git_previous']}` | `{m['final_previous']}` |\n")
        else:
            f.write("No mismatches.\n")
        f.write("\n")

        f.write("---\n\n")

        # Unaffected
        f.write(f"## Unaffected PROD Folders ({len(unaffected)})\n\n")
        f.write("Exist in PROD but have no matching rename in `final.md`. May need manual review.\n\n")
        if unaffected:
            for p in unaffected:
                f.write(f"- `PROD/{p}`\n")
        else:
            f.write("None.\n")
        f.write("\n")

    print(f"  Saved to {output_file}")


def main():
    if len(sys.argv) > 1:
        repo_names = sys.argv[1:]
        repos = {name: DEFAULT_REPOS[name] for name in repo_names if name in DEFAULT_REPOS}
    else:
        repos = DEFAULT_REPOS

    if not FINAL_MD.exists():
        print(f"final.md not found at {FINAL_MD}")
        return

    print("Parsing final.md...")
    final_mappings = parse_final_md(FINAL_MD)
    rename_map = build_rename_map(final_mappings)
    print(f"  {len(final_mappings)} entries, {len(rename_map)} unique renames\n")

    for repo_name, repo_path in repos.items():
        print(f"\n[{repo_name}]")
        plan_for_repo(repo_name, repo_path, rename_map, final_mappings)

    print("\nDone!")


if __name__ == "__main__":
    main()
