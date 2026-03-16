import os
import sys
from pathlib import Path
from collections import defaultdict

DEFAULT_REPOS = {
    "KKUH": "/home/verosha/Documents/gittea/KKUH",
    "Alibaba": "/home/verosha/Documents/gittea/Alibaba",
    "WAVE1": "/home/verosha/Documents/gittea/WAVE1",
}
REPO_NAMES = ["KKUH", "Alibaba", "WAVE1"]
OUTPUT_DIR = Path(__file__).parent.parent / "output"
SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode"}


def get_uat_services(repo_path):
    """Get all module/service pairs from UAT (depth=2 subfolders only)."""
    uat_dir = Path(repo_path) / "UAT"
    services = set()

    if not uat_dir.exists():
        return services

    for module in sorted(uat_dir.iterdir()):
        if not module.is_dir() or module.name in SKIP:
            continue
        for service in sorted(module.iterdir()):
            if not service.is_dir() or service.name in SKIP:
                continue
            services.add(f"{module.name}/{service.name}")

    return services


def main():
    # Collect services from each repo
    repo_services = {}
    for repo_name, repo_path in DEFAULT_REPOS.items():
        repo_services[repo_name] = get_uat_services(repo_path)
        print(f"[{repo_name}] {len(repo_services[repo_name])} services in UAT")

    # Collect all unique service paths
    all_services = set()
    for repo in REPO_NAMES:
        all_services.update(repo_services[repo])

    # Group by module
    by_module = defaultdict(list)
    for svc in sorted(all_services):
        module = svc.split("/")[0]
        by_module[module].append(svc)

    # For matching: build a map of service_name -> {repo: full_path}
    # to detect name mismatches across repos
    # We need to identify "same service, different name" cases
    # A service is the same if it exists under the same module in multiple repos

    # Stats
    total_services = len(all_services)
    in_all_3 = 0
    in_2_only = 0
    in_1_only = 0
    name_mismatch_count = 0

    output_file = OUTPUT_DIR / "uat_current_names_comparison.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# UAT Current Folder Names - Cross Repo Comparison\n\n")
        f.write("Compares the **actual current** UAT subfolder names across all 3 repos.\n\n")
        f.write("| Symbol | Meaning |\n")
        f.write("|---|---|\n")
        f.write("| Y | Exists with this exact name |\n")
        f.write("| - | Does not exist |\n\n")

        for module in sorted(by_module.keys()):
            services = by_module[module]

            # Count per-repo for this module
            module_counts = {r: 0 for r in REPO_NAMES}
            for svc in services:
                for repo in REPO_NAMES:
                    if svc in repo_services[repo]:
                        module_counts[repo] += 1

            f.write(f"## {module} (KKUH: {module_counts['KKUH']}, Alibaba: {module_counts['Alibaba']}, WAVE1: {module_counts['WAVE1']})\n\n")
            f.write("| Service Name | KKUH | Alibaba | WAVE1 | Count |\n")
            f.write("|---|:---:|:---:|:---:|:---:|\n")

            for svc in services:
                svc_name = svc.split("/", 1)[1]
                present = {}
                count = 0
                for repo in REPO_NAMES:
                    if svc in repo_services[repo]:
                        present[repo] = "Y"
                        count += 1
                    else:
                        present[repo] = "-"

                if count == 3:
                    in_all_3 += 1
                elif count == 2:
                    in_2_only += 1
                else:
                    in_1_only += 1

                # Highlight rows not in all 3
                name_display = f"`{svc_name}`"
                if count < 3:
                    name_display = f"**`{svc_name}`**"

                f.write(f"| {name_display} | {present['KKUH']} | {present['Alibaba']} | {present['WAVE1']} | {count}/3 |\n")

            f.write("\n")

        # Summary
        f.write("---\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Metric | Count |\n")
        f.write(f"|---|---|\n")
        f.write(f"| Total unique services | {total_services} |\n")
        f.write(f"| In all 3 repos | {in_all_3} |\n")
        f.write(f"| In 2 repos only | {in_2_only} |\n")
        f.write(f"| In 1 repo only | {in_1_only} |\n\n")

        # Services only in specific repos
        f.write("## Services NOT in all 3 repos\n\n")
        f.write("These exist in some repos but not others - may need attention.\n\n")
        f.write("| Service | KKUH | Alibaba | WAVE1 |\n")
        f.write("|---|:---:|:---:|:---:|\n")

        for module in sorted(by_module.keys()):
            for svc in by_module[module]:
                count = sum(1 for r in REPO_NAMES if svc in repo_services[r])
                if count < 3:
                    present = {r: ("Y" if svc in repo_services[r] else "-") for r in REPO_NAMES}
                    f.write(f"| `{svc}` | {present['KKUH']} | {present['Alibaba']} | {present['WAVE1']} |\n")

        f.write("\n")

        # Name inconsistencies: same module, similar names that differ slightly
        # e.g. bb-donation-srv vs bb-donation_srv, econsent vs e-consent
        f.write("## Potential Name Inconsistencies\n\n")
        f.write("Services under the same module with similar but not identical names across repos.\n\n")

        inconsistencies = []
        for module in sorted(by_module.keys()):
            services = by_module[module]
            svc_names = [s.split("/", 1)[1] for s in services]

            # Find names that exist in some repos but not all,
            # and have a "similar" counterpart in another repo
            for i, name_a in enumerate(svc_names):
                for j, name_b in enumerate(svc_names):
                    if i >= j:
                        continue
                    svc_a = f"{module}/{name_a}"
                    svc_b = f"{module}/{name_b}"

                    # Check if they're in different repos (not overlapping)
                    repos_a = {r for r in REPO_NAMES if svc_a in repo_services[r]}
                    repos_b = {r for r in REPO_NAMES if svc_b in repo_services[r]}

                    if repos_a and repos_b and not (repos_a & repos_b):
                        # Normalize names for comparison
                        norm_a = name_a.replace("-", "").replace("_", "").replace(".", "").lower()
                        norm_b = name_b.replace("-", "").replace("_", "").replace(".", "").lower()

                        if norm_a == norm_b or norm_a in norm_b or norm_b in norm_a:
                            inconsistencies.append({
                                "module": module,
                                "name_a": name_a,
                                "repos_a": repos_a,
                                "name_b": name_b,
                                "repos_b": repos_b,
                            })

        if inconsistencies:
            f.write("| Module | Name Variant A | In Repos | Name Variant B | In Repos |\n")
            f.write("|---|---|---|---|---|\n")
            for inc in inconsistencies:
                f.write(f"| `{inc['module']}` | `{inc['name_a']}` | {', '.join(sorted(inc['repos_a']))} | `{inc['name_b']}` | {', '.join(sorted(inc['repos_b']))} |\n")
                name_mismatch_count += 1
        else:
            f.write("No inconsistencies detected.\n")

        f.write(f"\n**Total name inconsistencies: {name_mismatch_count}**\n")

    print(f"\nSaved to {output_file}")
    print(f"Total: {total_services} services | All 3: {in_all_3} | 2 only: {in_2_only} | 1 only: {in_1_only} | Name mismatches: {name_mismatch_count}")


if __name__ == "__main__":
    main()
