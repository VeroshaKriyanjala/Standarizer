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
SHORT_NAMES = {
    "KKUH": "KKUH", "Alibaba": "ALI", "WAVE1": "W1", "CS": "CS",
    "KAUH": "KAUH", "S2": "S2", "S3": "S3", "HMG": "HMG",
    "DEPLOYMENT-BASE-REPO": "BASE",
}
OUTPUT_DIR = Path(__file__).parent.parent / "output"
SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode", "PreSync"}
REPOS_WITHOUT_UAT = {"DEPLOYMENT-BASE-REPO"}


def normalize(name):
    """Normalize a service name for fuzzy matching."""
    return name.replace("-", "").replace("_", "").replace(".", "").replace(" ", "").lower()


def get_services_by_module(repo_name, repo_path):
    """Return dict of {module: {service_name, ...}}."""
    if repo_name in REPOS_WITHOUT_UAT:
        base_dir = Path(repo_path)
    else:
        base_dir = Path(repo_path) / "UAT"

    result = defaultdict(set)
    if not base_dir.exists():
        return result

    for module in sorted(base_dir.iterdir()):
        if not module.is_dir() or module.name in SKIP:
            continue
        for service in sorted(module.iterdir()):
            if not service.is_dir() or service.name in SKIP:
                continue
            result[module.name].add(service.name)

    return result


def main():
    # Collect per-repo data
    repo_data = {}
    for repo_name, repo_path in DEFAULT_REPOS.items():
        repo_data[repo_name] = get_services_by_module(repo_name, repo_path)
        total = sum(len(v) for v in repo_data[repo_name].values())
        print(f"[{repo_name}] {total} services")

    # Collect all modules
    all_modules = set()
    for repo in REPO_NAMES:
        all_modules.update(repo_data[repo].keys())

    total_repos = len(REPO_NAMES)
    header_names = [SHORT_NAMES[r] for r in REPO_NAMES]
    header = "| # | Service Identity | " + " | ".join(header_names) + " | Match |"
    separator = "|---|---|" + "|".join(["---" for _ in REPO_NAMES]) + "|---|"

    output_file = OUTPUT_DIR / "all_repos_actual_names.md"

    stats_all_same = 0
    stats_mismatch = 0
    stats_partial = 0
    mismatch_rows = []

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# UAT Actual Service Names - All Repos\n\n")
        f.write("Shows the **actual folder name** each repo uses for each service.\n\n")
        f.write("| Symbol | Meaning |\n")
        f.write("|---|---|\n")
        f.write("| `-` | Service does not exist in this repo |\n")
        f.write("| Folder name | The actual folder name used |\n")
        f.write("| **Match** column | ALL SAME = identical across all repos that have it |\n")
        f.write("| | MISMATCH = different names detected across repos |\n\n")

        for module in sorted(all_modules):
            # Gather all service names across repos for this module
            all_names_in_module = set()
            for repo in REPO_NAMES:
                all_names_in_module.update(repo_data[repo].get(module, set()))

            # Group by normalized name to identify "same service, different name"
            norm_groups = defaultdict(list)
            for name in sorted(all_names_in_module):
                norm_groups[normalize(name)].append(name)

            # Build rows: one row per normalized group (= one logical service)
            rows = []
            for norm_key in sorted(norm_groups.keys()):
                variants = norm_groups[norm_key]

                # For each repo, find which variant (if any) it has
                repo_values = {}
                for repo in REPO_NAMES:
                    repo_svcs = repo_data[repo].get(module, set())
                    found = [v for v in variants if v in repo_svcs]
                    if found:
                        repo_values[repo] = found[0]
                    else:
                        repo_values[repo] = "-"

                # Determine the "identity" name (most common variant, or the standardized one)
                present_names = [v for v in repo_values.values() if v != "-"]
                if not present_names:
                    continue

                # Pick the most common name as identity
                from collections import Counter
                name_counts = Counter(present_names)
                identity = name_counts.most_common(1)[0][0]

                # Check match status
                unique_names = set(present_names)
                if len(unique_names) == 1:
                    match_status = "ALL SAME"
                    stats_all_same += 1
                else:
                    match_status = "**MISMATCH**"
                    stats_mismatch += 1

                count = len(present_names)
                rows.append((identity, repo_values, match_status, count))

            if not rows:
                continue

            # Module header with counts
            module_counts = []
            for r in REPO_NAMES:
                cnt = len(repo_data[r].get(module, set()))
                module_counts.append(f"{SHORT_NAMES[r]}:{cnt}")

            f.write(f"## {module} ({', '.join(module_counts)})\n\n")
            f.write(header + "\n")
            f.write(separator + "\n")

            row_num = 0
            for identity, repo_values, match_status, count in rows:
                row_num += 1
                cells = []
                for repo in REPO_NAMES:
                    val = repo_values[repo]
                    if val == "-":
                        cells.append("-")
                    elif val == identity:
                        cells.append(f"`{val}`")
                    else:
                        # Different from identity - highlight it
                        cells.append(f"**`{val}`**")

                f.write(f"| {row_num} | `{identity}` | " + " | ".join(cells) + f" | {match_status} |\n")

                if match_status == "**MISMATCH**":
                    mismatch_rows.append((module, identity, repo_values))

            f.write("\n")

        # Summary
        f.write("---\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Metric | Count |\n")
        f.write(f"|---|---|\n")
        f.write(f"| Total logical services | {stats_all_same + stats_mismatch} |\n")
        f.write(f"| All repos use same name | {stats_all_same} |\n")
        f.write(f"| Name mismatch across repos | {stats_mismatch} |\n\n")

        # Mismatch detail
        if mismatch_rows:
            f.write("## All Mismatches Detail\n\n")
            f.write("| Module | Service | " + " | ".join(header_names) + " |\n")
            f.write("|---|---|" + "|".join(["---" for _ in REPO_NAMES]) + "|\n")
            for module, identity, repo_values in mismatch_rows:
                cells = []
                for repo in REPO_NAMES:
                    val = repo_values[repo]
                    if val == "-":
                        cells.append("-")
                    elif val == identity:
                        cells.append(f"`{val}`")
                    else:
                        cells.append(f"**`{val}`**")
                f.write(f"| `{module}` | `{identity}` | " + " | ".join(cells) + " |\n")
            f.write("\n")

    print(f"\nSaved to {output_file}")
    print(f"Logical services: {stats_all_same + stats_mismatch} | Same: {stats_all_same} | Mismatch: {stats_mismatch}")


if __name__ == "__main__":
    main()
