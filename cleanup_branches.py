import subprocess
import sys

DEFAULT_REPOS = {
    "KKUH": "/home/verosha/Documents/gittea/KKUH",
    # "Alibaba": "/home/verosha/Documents/gittea/Alibaba",
    # "WAVE1": "/home/verosha/Documents/gittea/WAVE1",
    # "CS": "/home/verosha/Documents/gittea/CS",
    # "KAUH": "/home/verosha/Documents/gittea/KAUH",
    # "S2": "/home/verosha/Documents/gittea/S2",
    # "S3": "/home/verosha/Documents/gittea/S3",
    # "HMG": "/home/verosha/Documents/gittea/HMG",
}
BRANCH_NAME = "PROD-standardize-folder-names"


def git_run(repo_path, *args):
    result = subprocess.run(
        ["git", "-C", repo_path] + list(args),
        capture_output=True, text=True,
    )
    return result


def cleanup_repo(repo_name, repo_path):
    # Checkout main
    result = git_run(repo_path, "checkout", "main")
    if result.returncode != 0:
        print(f"  ERROR checking out main: {result.stderr.strip()}")
        return
    print(f"  Checked out main")

    # Delete branch
    result = git_run(repo_path, "branch", "-D", BRANCH_NAME)
    if result.returncode != 0:
        print(f"  Branch '{BRANCH_NAME}' not found or already deleted")
    else:
        print(f"  Deleted branch '{BRANCH_NAME}'")


def main():
    repo_names = sys.argv[1:] if len(sys.argv) > 1 else None
    if repo_names:
        repos = {name: DEFAULT_REPOS[name] for name in repo_names if name in DEFAULT_REPOS}
    else:
        repos = DEFAULT_REPOS

    for repo_name, repo_path in repos.items():
        print(f"[{repo_name}]")
        cleanup_repo(repo_name, repo_path)
        print()

    print("Done!")


if __name__ == "__main__":
    main()
