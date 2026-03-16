import os
import sys
import subprocess
from pathlib import Path

# Default values - can be overridden via CLI args
DEFAULT_REPOS = {
    "KKUH": "/home/verosha/Documents/gittea/KKUH",
    "Alibaba": "/home/verosha/Documents/gittea/Alibaba",
    "WAVE1": "/home/verosha/Documents/gittea/WAVE1",
    "CS": "/home/verosha/Documents/gittea/CS",
    "KAUH": "/home/verosha/Documents/gittea/KAUH",
    "S2": "/home/verosha/Documents/gittea/S2",
    "S3": "/home/verosha/Documents/gittea/S3",
    "HMG": "/home/verosha/Documents/gittea/HMG",
    "DEPLOYMENT-BASE-REPO": "/home/verosha/Documents/gittea/DEPLOYMENT-BASE-REPO",
}

TARGET_DIR = "UAT"
OUTPUT_DIR = Path(__file__).parent.parent / "output"


def run_for_repo(repo_name, repo_path):
    repo = Path(repo_path).resolve()
    target_path = repo / TARGET_DIR

    if not (repo / ".git").exists() and not (repo.parent / ".git").exists():
        print(f"  Could not find a git repository at {repo}")
        return

    print(f"  Scanning Git history for folder renames in '{TARGET_DIR}' ...")

    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "log", "--name-status", "--diff-filter=R", "--format="],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"  Git command failed: {e}")
        print(e.stderr)
        return

    lines = result.stdout.strip().split('\n')

    # Store unique directory renames: new_dir_path -> old_dir_path
    dir_renames = {}

    for line in lines:
        if not line.strip():
            continue

        parts = line.split('\t')
        if len(parts) >= 3 and parts[0].startswith('R'):
            old_file = parts[1]
            new_file = parts[2]

            if f"{TARGET_DIR}/" in new_file or f"{TARGET_DIR}/" in old_file:
                old_dir = os.path.dirname(old_file)
                new_dir = os.path.dirname(new_file)

                if old_dir != new_dir:
                    dir_renames[new_dir] = old_dir

    # Simplify to find the overarching folder rename
    simplified = {}

    for new_d, old_d in dir_renames.items():
        new_parts = new_d.split('/')
        old_parts = old_d.split('/')

        min_len = min(len(new_parts), len(old_parts))
        diverge_idx = -1
        for i in range(min_len):
            if new_parts[i] != old_parts[i]:
                diverge_idx = i
                break

        if diverge_idx != -1:
            changed_new_folder = "/".join(new_parts[:diverge_idx+1])
            changed_old_folder = "/".join(old_parts[:diverge_idx+1])
            simplified[changed_new_folder] = changed_old_folder
        else:
            if len(new_parts) > len(old_parts):
                changed_new_folder = "/".join(new_parts[:len(old_parts)+1])
                simplified[changed_new_folder] = old_d
            else:
                changed_old_folder = "/".join(old_parts[:len(new_parts)+1])
                simplified[new_d] = changed_old_folder

    # Find all current directories inside TARGET_DIR
    current_dirs = set()
    skip = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode"}

    if target_path.exists() and target_path.is_dir():
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if d not in skip]
            for d in dirs:
                full_path = Path(root) / d
                try:
                    rel = full_path.relative_to(repo)
                    current_dirs.add(str(rel))
                except ValueError:
                    pass

    # Combine renamed and unrenamed
    all_history = {}

    for new_folder, old_folder in simplified.items():
        if TARGET_DIR in new_folder.split('/'):
            all_history[new_folder] = old_folder

    for curr_dir in current_dirs:
        parts = curr_dir.split('/')
        is_renamed = False
        for i in range(1, len(parts) + 1):
            parent_path = "/".join(parts[:i])
            if parent_path in simplified:
                is_renamed = True
                break
        if not is_renamed:
            all_history[curr_dir] = curr_dir

    # Write output
    out_dir = OUTPUT_DIR / repo_name
    out_dir.mkdir(parents=True, exist_ok=True)
    output_file = out_dir / "folder_history.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write(f"  FOLDER RENAMES IN {TARGET_DIR} ({repo_name})\n")
        f.write("=" * 80 + "\n\n")

        if not all_history:
            f.write("No folders found matching your criteria.\n")
        else:
            for new_folder, old_folder in sorted(all_history.items()):
                f.write(f"Current Folder: {new_folder}\n")
                f.write(f"Previous Name:  {old_folder}\n")
                f.write("-" * 60 + "\n")

    renamed_count = sum(1 for k, v in all_history.items() if k != v)
    unchanged_count = sum(1 for k, v in all_history.items() if k == v)
    print(f"  Found {renamed_count} renames, {unchanged_count} unchanged folders")
    print(f"  Saved to {output_file}")


def main():
    if len(sys.argv) > 1:
        # Run for specific repos passed as args: python script.py Alibaba KKUH
        repo_names = sys.argv[1:]
        repos = {name: DEFAULT_REPOS[name] for name in repo_names if name in DEFAULT_REPOS}
        if not repos:
            print(f"Unknown repo(s): {repo_names}")
            print(f"Available: {list(DEFAULT_REPOS.keys())}")
            return
    else:
        repos = DEFAULT_REPOS

    for repo_name, repo_path in repos.items():
        print(f"\n[{repo_name}]")
        run_for_repo(repo_name, repo_path)

    print("\nDone!")


if __name__ == "__main__":
    main()
