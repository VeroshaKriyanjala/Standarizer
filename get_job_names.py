"""Scan every PROD service kustomization file and extract Job target names from patchesJson6902."""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install it with: pip install pyyaml")
    sys.exit(1)

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

OUTPUT_DIR = Path(__file__).parent / "output"


def extract_job_names(kust_file):
    """Parse a kustomization.yaml and return list of Job target names from patchesJson6902."""
    job_names = []
    try:
        with open(kust_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"  WARN: Could not parse {kust_file}: {e}")
        return job_names

    if not data or not isinstance(data, dict):
        return job_names

    # Handle both casings: patchesJson6902 and patchesJSON6902
    patches = data.get("patchesJson6902") or data.get("patchesJSON6902") or []

    for patch_entry in patches:
        if not isinstance(patch_entry, dict):
            continue
        target = patch_entry.get("target", {})
        if not isinstance(target, dict):
            continue
        if target.get("kind") == "Job":
            name = target.get("name", "")
            if name:
                job_names.append(name)

    return job_names


def scan_repo(repo_name, repo_path):
    """Scan all PROD kustomization files in a repo and collect Job target names."""
    prod_dir = Path(repo_path) / "PROD"
    results = []

    if not prod_dir.exists():
        print(f"  PROD directory not found at {prod_dir}")
        return results

    for kust_file in sorted(prod_dir.rglob("kustomization.yaml")):
        job_names = extract_job_names(kust_file)
        if job_names:
            service_rel = str(kust_file.parent.relative_to(prod_dir))
            results.append((service_rel, job_names))

    return results


def main():
    repo_names = [a for a in sys.argv[1:] if not a.startswith("--")]

    if repo_names:
        repos = {name: DEFAULT_REPOS[name] for name in repo_names if name in DEFAULT_REPOS}
        if not repos:
            print(f"Unknown repo(s): {repo_names}")
            print(f"Available: {list(DEFAULT_REPOS.keys())}")
            return
    else:
        repos = DEFAULT_REPOS

    all_results = {}
    total_jobs = 0

    for repo_name, repo_path in repos.items():
        print(f"\n[{repo_name}]")
        results = scan_repo(repo_name, repo_path)
        all_results[repo_name] = results

        if not results:
            print("  No Job targets found")
            continue

        for service_rel, job_names in results:
            for name in job_names:
                print(f"  {service_rel} -> Job: {name}")
                total_jobs += 1

    print(f"\n{'='*60}")
    print(f"Total Job targets found: {total_jobs}")

    # Write report
    report_file = OUTPUT_DIR / "job_names_report.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# Job Target Names from PROD Kustomization Files\n\n")
        f.write(f"Total Job targets found: {total_jobs}\n\n")

        for repo_name, results in all_results.items():
            f.write(f"## {repo_name}\n\n")
            if not results:
                f.write("No Job targets found.\n\n")
                continue

            f.write("| Service | Job Target Name |\n")
            f.write("|---------|----------------|\n")
            for service_rel, job_names in results:
                for name in job_names:
                    f.write(f"| `{service_rel}` | `{name}` |\n")
            f.write("\n")

    print(f"Report saved to {report_file}")


if __name__ == "__main__":
    main()
