#!/usr/bin/env python3
"""
Audit UAT folder renames by cross-referencing git history against final.md.

For each repo, discovers folder renames from git history and compares them
to the known mappings in final.md. Logs:
  1. Matches (git agrees with final.md)
  2. Git-only renames (not documented in final.md)
  3. final.md-only renames (not found in git history for this repo)
  4. Mismatches (same current folder, different previous name)
"""

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

FINAL_MD = Path(__file__).parent.parent / "output" / "final.md"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

REPOS = {
    "KKUH": "/home/verosha/Documents/gittea/KKUH",
    "Alibaba": "/home/verosha/Documents/gittea/Alibaba",
    "WAVE1": "/home/verosha/Documents/gittea/WAVE1",
    "CS": "/home/verosha/Documents/gittea/CS",
    "KAUH": "/home/verosha/Documents/gittea/KAUH",
    "S2": "/home/verosha/Documents/gittea/S2",
    "S3": "/home/verosha/Documents/gittea/S3",
    "HMG": "/home/verosha/Documents/gittea/HMG",
}


def parse_final_md(filepath: Path) -> dict:
    """
    Parse final.md to extract {current_folder: previous_folder} mappings.
    Format:
        Current Folder: UAT/base/base-utility-service-java-sev
        Previous Name:  UAT/base/baseutilityservicejava
    """
    content = filepath.read_text(encoding="utf-8")
    mappings = {}

    current = None
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("Current Folder:"):
            current = line.split(":", 1)[1].strip()
        elif line.startswith("Previous Name:") and current:
            previous = line.split(":", 1)[1].strip()
            mappings[current] = previous
            current = None

    return mappings


def get_dir_from_filepath(filepath: str) -> str:
    """Extract directory path (UAT/module/service) from a file path."""
    parts = filepath.split("/")
    if len(parts) >= 3:
        return "/".join(parts[:3])
    return filepath


def get_git_renames(repo_path: str) -> dict:
    """
    Discover folder renames from git history.
    Returns {current_folder: previous_folder}.

    Process per-commit to avoid cross-matching in batch renames.
    Uses majority voting: for each source dir in a commit,
    the target dir with the most file renames wins.
    """
    try:
        result = subprocess.run(
            [
                "git", "-C", repo_path,
                "log", "--all", "--format=COMMIT %H",
                "--diff-filter=R", "--name-status", "-M",
                "--", "UAT/",
            ],
            capture_output=True, text=True, timeout=120,
        )
        output = result.stdout
    except Exception as e:
        print(f"  ERROR running git: {e}")
        return {}

    # Parse per-commit rename pairs
    all_renames = {}  # {current_dir: previous_dir}

    # Group file renames by commit
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

    # Process each commit: majority vote per source dir
    for commit_renames in commits:
        # Group by source dir
        src_to_targets = defaultdict(lambda: defaultdict(int))
        for old_dir, new_dir in commit_renames:
            src_to_targets[old_dir][new_dir] += 1

        for src_dir, targets in src_to_targets.items():
            # Pick the target with most file renames
            best_target = max(targets, key=targets.get)
            # Only record if it's a real rename (different dirs)
            if src_dir != best_target:
                # Store as {new_dir: old_dir} (current: previous)
                # If we already have a mapping for this new_dir, keep the one
                # with more evidence (or the first one found, which is most recent)
                if best_target not in all_renames:
                    all_renames[best_target] = src_dir

    return all_renames


def audit_repo(repo_name: str, repo_path: str, final_mappings: dict) -> dict:
    """Audit a single repo. Returns stats dict."""
    print(f"\n[{repo_name}]")

    git_renames = get_git_renames(repo_path)
    print(f"  Found {len(git_renames)} folder renames in git history")

    matches = []
    mismatches = []
    git_only = []
    final_only = []

    # Compare git renames against final.md
    all_current_dirs = set(git_renames.keys()) | set(final_mappings.keys())

    for current_dir in sorted(all_current_dirs):
        in_git = current_dir in git_renames
        in_final = current_dir in final_mappings

        if in_git and in_final:
            git_prev = git_renames[current_dir]
            final_prev = final_mappings[current_dir]
            if git_prev == final_prev:
                matches.append({
                    "current": current_dir,
                    "previous": git_prev,
                })
            else:
                mismatches.append({
                    "current": current_dir,
                    "git_previous": git_prev,
                    "final_previous": final_prev,
                })
        elif in_git and not in_final:
            git_only.append({
                "current": current_dir,
                "previous": git_renames[current_dir],
            })
        elif in_final and not in_git:
            final_only.append({
                "current": current_dir,
                "previous": final_mappings[current_dir],
            })

    print(f"  Matches: {len(matches)}")
    print(f"  Git-only: {len(git_only)}")
    print(f"  final.md-only: {len(final_only)}")
    print(f"  Mismatches: {len(mismatches)}")

    return {
        "repo": repo_name,
        "git_total": len(git_renames),
        "matches": matches,
        "mismatches": mismatches,
        "git_only": git_only,
        "final_only": final_only,
    }


def write_report(all_results: list, final_mappings: dict, output_file: Path):
    """Write the audit report."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# UAT Rename Audit: Git History vs final.md\n\n")
        f.write(f"Cross-references git rename history against {len(final_mappings)} mappings in `final.md`.\n\n")

        total_matches = 0
        total_mismatches = 0
        total_git_only = 0
        total_final_only = 0

        for result in all_results:
            repo = result["repo"]
            f.write(f"## {repo}\n\n")
            f.write(f"Git renames found: **{result['git_total']}**\n\n")

            # Matches
            if result["matches"]:
                f.write(f"### Matches ({len(result['matches'])})\n\n")
                f.write("| Current Folder | Previous Name |\n")
                f.write("|---|---|\n")
                for m in result["matches"]:
                    f.write(f"| `{m['current']}` | `{m['previous']}` |\n")
                f.write("\n")
            total_matches += len(result["matches"])

            # Mismatches
            if result["mismatches"]:
                f.write(f"### Mismatches ({len(result['mismatches'])})\n\n")
                f.write("| Current Folder | Git Previous | final.md Previous |\n")
                f.write("|---|---|---|\n")
                for m in result["mismatches"]:
                    f.write(f"| `{m['current']}` | `{m['git_previous']}` | `{m['final_previous']}` |\n")
                f.write("\n")
            total_mismatches += len(result["mismatches"])

            # Git-only
            if result["git_only"]:
                f.write(f"### Git-only renames ({len(result['git_only'])})\n\n")
                f.write("Renames found in git history but **NOT** in `final.md`.\n\n")
                f.write("| Current Folder | Previous Name |\n")
                f.write("|---|---|\n")
                for m in result["git_only"]:
                    f.write(f"| `{m['current']}` | `{m['previous']}` |\n")
                f.write("\n")
            total_git_only += len(result["git_only"])

            # final.md-only
            if result["final_only"]:
                f.write(f"### final.md-only ({len(result['final_only'])})\n\n")
                f.write("Renames in `final.md` but **NOT** found in this repo's git history.\n\n")
                f.write("| Current Folder | Previous Name (from final.md) |\n")
                f.write("|---|---|\n")
                for m in result["final_only"]:
                    f.write(f"| `{m['current']}` | `{m['previous']}` |\n")
                f.write("\n")
            total_final_only += len(result["final_only"])

            f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write("| Metric | Count |\n")
        f.write("|---|---|\n")
        f.write(f"| Repos scanned | {len(all_results)} |\n")
        f.write(f"| final.md mappings | {len(final_mappings)} |\n")
        f.write(f"| Total matches (across all repos) | {total_matches} |\n")
        f.write(f"| Total mismatches | {total_mismatches} |\n")
        f.write(f"| Total git-only renames | {total_git_only} |\n")
        f.write(f"| Total final.md-only | {total_final_only} |\n")
        f.write("\n")

        # Cross-repo summary: which renames appear in most repos
        rename_repo_count = defaultdict(set)
        for result in all_results:
            for m in result["matches"] + result["mismatches"]:
                rename_repo_count[m["current"]].add(result["repo"])
            for m in result["git_only"]:
                rename_repo_count[m["current"]].add(result["repo"])

        f.write("## Rename Coverage Across Repos\n\n")
        f.write("| Current Folder | Repos with this rename |\n")
        f.write("|---|---|\n")
        for folder in sorted(rename_repo_count.keys()):
            repos = sorted(rename_repo_count[folder])
            f.write(f"| `{folder}` | {', '.join(repos)} ({len(repos)}/{len(all_results)}) |\n")
        f.write("\n")


def main():
    repo_names = sys.argv[1:] if len(sys.argv) > 1 else list(REPOS.keys())

    print("Parsing final.md...")
    final_mappings = parse_final_md(FINAL_MD)
    print(f"  Found {len(final_mappings)} rename mappings in final.md")

    all_results = []
    for repo_name in repo_names:
        if repo_name not in REPOS:
            print(f"Unknown repo: {repo_name}")
            continue
        result = audit_repo(repo_name, REPOS[repo_name], final_mappings)
        all_results.append(result)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / "uat_rename_audit.md"
    write_report(all_results, final_mappings, output_file)
    print(f"\nReport saved to {output_file}")


if __name__ == "__main__":
    main()
