import sys
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path(__file__).parent.parent / "output"
REPO_NAMES = ["KKUH", "Alibaba", "WAVE1"]


def parse_history(history_file):
    """Parse folder_history.md and return dict of {current_rel_path: previous_rel_path}
    Only includes subfolder-level services (depth >= 2, e.g. billing/csi-bm-xxx).
    Skips entries where current == previous (no rename happened).
    Strips the UAT/ prefix.
    """
    renames = {}
    current = None

    with open(history_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Current Folder:"):
                current = line.replace("Current Folder:", "").strip()
            elif line.startswith("Previous Name:"):
                previous = line.replace("Previous Name:", "").strip()
                if current and previous:
                    # Strip UAT/ prefix
                    curr_rel = current.replace("UAT/", "", 1) if current.startswith("UAT/") else current
                    prev_rel = previous.replace("UAT/", "", 1) if previous.startswith("UAT/") else previous

                    # Only include subfolder-level (module/service), not top-level modules
                    # and not deeper nested paths (like base/medispan/overlays/PROD)
                    parts = curr_rel.split("/")
                    if len(parts) == 2:
                        renames[curr_rel] = prev_rel

                    current = None

    return renames


def main():
    # Parse all 3 repos
    repo_data = {}
    for repo in REPO_NAMES:
        history_file = OUTPUT_DIR / repo / "folder_history.md"
        if history_file.exists():
            repo_data[repo] = parse_history(history_file)
            print(f"[{repo}] Loaded {len(repo_data[repo])} service entries")
        else:
            repo_data[repo] = {}
            print(f"[{repo}] folder_history.md not found - skipping")

    # Collect all unique service paths (current standardized names) across all repos
    all_services = set()
    for repo in REPO_NAMES:
        all_services.update(repo_data[repo].keys())

    # Group by module (top-level folder)
    by_module = defaultdict(list)
    for svc in sorted(all_services):
        module = svc.split("/")[0]
        by_module[module].append(svc)

    # Build the comparison table
    output_file = OUTPUT_DIR / "service_name_comparison.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Service Name Comparison Across Repos\n\n")
        f.write("Shows the **current UAT name** (standardized) and the **previous name** in each repo.\n\n")
        f.write("- **Same** = previous name was the same across repos (consistent)\n")
        f.write("- **-** = service does not exist in that repo's UAT history\n")
        f.write("- **=** = no rename happened (was always this name)\n\n")

        # Stats
        total = len(all_services)
        renamed_in_any = 0
        consistent = 0
        inconsistent = 0

        for module in sorted(by_module.keys()):
            services = by_module[module]
            f.write(f"## {module}\n\n")
            f.write("| Current Standardized Name | KKUH (previous) | Alibaba (previous) | WAVE1 (previous) | Status |\n")
            f.write("|---|---|---|---|---|\n")

            for svc in services:
                svc_name = svc.split("/", 1)[1]  # just the service name part

                prev_names = {}
                for repo in REPO_NAMES:
                    if svc in repo_data[repo]:
                        prev = repo_data[repo][svc]
                        prev_svc = prev.split("/", 1)[1] if "/" in prev else prev
                        if prev_svc == svc_name:
                            prev_names[repo] = "="  # no rename
                        else:
                            prev_names[repo] = prev_svc
                    else:
                        prev_names[repo] = "-"

                # Determine status
                actual_renames = {r: n for r, n in prev_names.items() if n not in ("-", "=")}
                no_rename = {r: n for r, n in prev_names.items() if n == "="}
                missing = {r: n for r, n in prev_names.items() if n == "-"}

                if not actual_renames:
                    status = "No rename"
                else:
                    unique_prev = set(actual_renames.values())
                    if len(unique_prev) == 1:
                        status = "Consistent"
                        consistent += 1
                    else:
                        status = "**INCONSISTENT**"
                        inconsistent += 1
                    renamed_in_any += 1

                kkuh_val = prev_names.get("KKUH", "-")
                ali_val = prev_names.get("Alibaba", "-")
                wave_val = prev_names.get("WAVE1", "-")

                f.write(f"| `{svc_name}` | `{kkuh_val}` | `{ali_val}` | `{wave_val}` | {status} |\n")

            f.write("\n")

        # Summary
        f.write("---\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Total unique services:** {total}\n")
        f.write(f"- **Renamed in at least one repo:** {renamed_in_any}\n")
        f.write(f"- **Consistent previous names:** {consistent}\n")
        f.write(f"- **Inconsistent previous names:** {inconsistent}\n")

    print(f"\nSaved to {output_file}")
    print(f"Total: {total} services, {renamed_in_any} renamed, {consistent} consistent, {inconsistent} inconsistent")


if __name__ == "__main__":
    main()
