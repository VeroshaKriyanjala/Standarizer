import os
import sys
from pathlib import Path

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

REPO_NAMES = ["KKUH", "Alibaba", "WAVE1", "CS", "KAUH", "S2", "S3", "HMG", "DEPLOYMENT-BASE-REPO"]

OUTPUT_DIR = Path(__file__).parent.parent / "output"

# Folders to skip
SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode"}

REPOS_WITHOUT_UAT = {"DEPLOYMENT-BASE-REPO"}

def print_tree(directory: Path, prefix: str = "", is_last: bool = True, file=sys.stdout):
    connector = "└── " if is_last else "├── "
    print(f"{prefix}{connector}{directory.name}/", file=file)

    new_prefix = prefix + ("    " if is_last else "│   ")

    items = []
    try:
        for item in sorted(directory.iterdir()):
            if item.name in SKIP:
                continue
            items.append(item)
    except PermissionError:
        print(f"{new_prefix}└── [permission denied]", file=file)
        return

    dirs = [i for i in items if i.is_dir()]
    for i, item in enumerate(dirs):
        is_last_item = (i == len(dirs) - 1)
        print_tree(item, new_prefix, is_last_item, file=file)


def generate_tree(folder_path: Path, output_file: Path, label: str = ""):
    root = folder_path.resolve()

    if not root.exists():
        print(f"  Path not found: {root}")
        return
    if not root.is_dir():
        print(f"  Not a directory: {root}")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        total_dirs = 0
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP]
            total_dirs += len(dirnames)

        header = f"{label + ' - ' if label else ''}{root.name}"
        print(f"\n{header}", file=f)
        print(f"   ({total_dirs} folders)\n", file=f)

        items = []
        for item in sorted(root.iterdir()):
            if item.name in SKIP:
                continue
            items.append(item)

        dirs = [i for i in items if i.is_dir()]
        for i, item in enumerate(dirs):
            is_last = (i == len(dirs) - 1)
            print_tree(item, "", is_last, file=f)

        print("", file=f)
    print(f"  Saved to {output_file}")


def main():
    # Usage: python script.py [repo_names...] [--section UAT|PROD|both]
    # Default: all repos, both sections
    section = "both"
    repo_names = []

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--section" and i + 1 < len(args):
            section = args[i + 1]
            i += 2
        else:
            repo_names.append(args[i])
            i += 1

    if repo_names:
        repos = {name: DEFAULT_REPOS[name] for name in repo_names if name in DEFAULT_REPOS}
    else:
        repos = DEFAULT_REPOS

    sections = ["UAT", "PROD"] if section == "both" else [section]

    for repo_name, repo_path in repos.items():
        print(f"\n[{repo_name}]")
        out_dir = OUTPUT_DIR / repo_name
        out_dir.mkdir(parents=True, exist_ok=True)

        if repo_name in REPOS_WITHOUT_UAT:
            # No UAT/PROD structure — generate tree from root
            output_file = out_dir / "nofiles_structure.md"
            print(f"  Generating root tree...")
            generate_tree(Path(repo_path), output_file, label=repo_name)
        else:
            for sec in sections:
                folder = Path(repo_path) / sec
                if folder.exists():
                    output_file = out_dir / f"nofiles_structure_{sec.lower()}.md"
                    print(f"  Generating {sec} tree...")
                    generate_tree(folder, output_file, label=f"{repo_name} {sec}")
                else:
                    print(f"  {sec} folder not found at {folder}")

    print("\nDone!")


if __name__ == "__main__":
    main()
