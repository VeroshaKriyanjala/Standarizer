import os
import sys
from pathlib import Path
from collections import defaultdict

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
SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode", "PreSync"}

# DEPLOYMENT-BASE-REPO has no UAT folder - services are at root level
REPOS_WITHOUT_UAT = {"DEPLOYMENT-BASE-REPO"}


def get_uat_services(repo_name, repo_path):
    """Get all module/service pairs (depth=2 subfolders only)."""
    if repo_name in REPOS_WITHOUT_UAT:
        base_dir = Path(repo_path)
    else:
        base_dir = Path(repo_path) / "UAT"

    services = set()

    if not base_dir.exists():
        return services

    for module in sorted(base_dir.iterdir()):
        if not module.is_dir() or module.name in SKIP:
            continue
        for service in sorted(module.iterdir()):
            if not service.is_dir() or service.name in SKIP:
                continue
            services.add(f"{module.name}/{service.name}")

    return services


def main():
    # Short display names for the table header
    short_names = {
        "KKUH": "KKUH",
        "Alibaba": "ALI",
        "WAVE1": "W1",
        "CS": "CS",
        "KAUH": "KAUH",
        "S2": "S2",
        "S3": "S3",
        "HMG": "HMG",
        "DEPLOYMENT-BASE-REPO": "BASE",
    }

    # Collect services from each repo
    repo_services = {}
    for repo_name, repo_path in DEFAULT_REPOS.items():
        repo_services[repo_name] = get_uat_services(repo_name, repo_path)
        source = "root" if repo_name in REPOS_WITHOUT_UAT else "UAT"
        print(f"[{repo_name}] {len(repo_services[repo_name])} services from {source}")

    # Collect all unique service paths
    all_services = set()
    for repo in REPO_NAMES:
        all_services.update(repo_services[repo])

    # Group by module
    by_module = defaultdict(list)
    for svc in sorted(all_services):
        module = svc.split("/")[0]
        by_module[module].append(svc)

    # Stats
    total_repos = len(REPO_NAMES)
    total_services = len(all_services)
    count_distribution = defaultdict(int)  # count -> number of services

    output_file = OUTPUT_DIR / "all_repos_uat_comparison.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# UAT Service Names - All Repos Comparison\n\n")
        f.write(f"Compares current UAT subfolder names across all {total_repos} repos.\n\n")
        f.write("| Symbol | Meaning |\n")
        f.write("|---|---|\n")
        f.write("| Y | Exists with this exact name |\n")
        f.write("| - | Does not exist |\n\n")
        f.write(f"**Repos:** {', '.join(REPO_NAMES)}\n\n")
        f.write(f"*Note: DEPLOYMENT-BASE-REPO uses root level (no UAT folder)*\n\n")

        # Build header
        header_names = [short_names[r] for r in REPO_NAMES]
        header = "| Service Name | " + " | ".join(header_names) + " | Count |"
        separator = "|---|" + "|".join([":---:" for _ in REPO_NAMES]) + "|:---:|"

        for module in sorted(by_module.keys()):
            services = by_module[module]

            # Count per-repo for this module
            module_counts = []
            for r in REPO_NAMES:
                cnt = sum(1 for s in services if s in repo_services[r])
                module_counts.append(f"{short_names[r]}:{cnt}")

            f.write(f"## {module} ({', '.join(module_counts)})\n\n")
            f.write(header + "\n")
            f.write(separator + "\n")

            for svc in services:
                svc_name = svc.split("/", 1)[1]
                count = 0
                cells = []
                for repo in REPO_NAMES:
                    if svc in repo_services[repo]:
                        cells.append("Y")
                        count += 1
                    else:
                        cells.append("-")

                count_distribution[count] += 1

                # Bold services not in all repos
                name_display = f"`{svc_name}`"
                if count < total_repos:
                    name_display = f"**`{svc_name}`**"

                f.write(f"| {name_display} | " + " | ".join(cells) + f" | {count}/{total_repos} |\n")

            f.write("\n")

        # Summary
        f.write("---\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Metric | Count |\n")
        f.write(f"|---|---|\n")
        f.write(f"| Total unique services | {total_services} |\n")
        for c in sorted(count_distribution.keys(), reverse=True):
            f.write(f"| In {c}/{total_repos} repos | {count_distribution[c]} |\n")
        f.write("\n")

        # Services not in all repos
        f.write("## Services NOT in all repos\n\n")
        f.write(header + "\n")
        f.write(separator + "\n")

        for module in sorted(by_module.keys()):
            for svc in by_module[module]:
                count = sum(1 for r in REPO_NAMES if svc in repo_services[r])
                if count < total_repos:
                    svc_name = svc.split("/", 1)[1]
                    cells = []
                    for repo in REPO_NAMES:
                        cells.append("Y" if svc in repo_services[repo] else "-")
                    f.write(f"| `{module}/{svc_name}` | " + " | ".join(cells) + f" | {count}/{total_repos} |\n")

        f.write("\n")

        # Name inconsistencies
        f.write("## Potential Name Inconsistencies\n\n")
        f.write("Services under the same module with similar but different names across repos.\n\n")

        inconsistencies = []
        for module in sorted(by_module.keys()):
            svc_names = [s.split("/", 1)[1] for s in by_module[module]]

            for i, name_a in enumerate(svc_names):
                for j, name_b in enumerate(svc_names):
                    if i >= j:
                        continue
                    svc_a = f"{module}/{name_a}"
                    svc_b = f"{module}/{name_b}"

                    repos_a = {r for r in REPO_NAMES if svc_a in repo_services[r]}
                    repos_b = {r for r in REPO_NAMES if svc_b in repo_services[r]}

                    if repos_a and repos_b and not (repos_a & repos_b):
                        norm_a = name_a.replace("-", "").replace("_", "").replace(".", "").lower()
                        norm_b = name_b.replace("-", "").replace("_", "").replace(".", "").lower()

                        if norm_a == norm_b or norm_a in norm_b or norm_b in norm_a:
                            inconsistencies.append({
                                "module": module,
                                "name_a": name_a,
                                "repos_a": sorted(repos_a),
                                "name_b": name_b,
                                "repos_b": sorted(repos_b),
                            })

        if inconsistencies:
            f.write("| Module | Name Variant A | In Repos | Name Variant B | In Repos |\n")
            f.write("|---|---|---|---|---|\n")
            for inc in inconsistencies:
                f.write(f"| `{inc['module']}` | `{inc['name_a']}` | {', '.join(inc['repos_a'])} | `{inc['name_b']}` | {', '.join(inc['repos_b'])} |\n")
        else:
            f.write("No inconsistencies detected.\n")

        f.write(f"\n**Total name inconsistencies: {len(inconsistencies)}**\n")

    print(f"\nSaved to {output_file}")
    print(f"Total: {total_services} services")
    for c in sorted(count_distribution.keys(), reverse=True):
        print(f"  In {c}/{total_repos} repos: {count_distribution[c]}")


if __name__ == "__main__":
    main()
