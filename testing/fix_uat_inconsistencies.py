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

# ============================================================================
#  STANDARDIZATION MAP
#  For each inconsistency, define the correct standard name.
#  Format: (module, wrong_name) -> correct_name
#
#  Review and edit these before running!
# ============================================================================
FIXES = {
    # base: KKUH has hyphens, Alibaba/WAVE1 have dots -> standardize to hyphens
    ("base", "csi.uif.admin.ui"):       "csi-uif-admin-ui",
    ("base", "csi.uif.settings"):       "csi-uif-settings",

    # bloodbank: KKUH has hyphen, Alibaba/WAVE1 have underscore -> standardize to hyphen
    ("bloodbank", "bb-donation_srv"):    "bb-donation-srv",

    # econsent: KKUH has hyphens, Alibaba/WAVE1 don't -> standardize to hyphens
    ("econsent", "econsent"):            "e-consent",
    ("econsent", "econsentui"):          "e-consent-ui",

    # empi: KKUH/Alibaba have standardized name, WAVE1 has old name
    ("empi", "empicrsintegration"):      "csi-empi-crs-integration",

    # lab: KKUH has hyphen, Alibaba/WAVE1 have underscore -> standardize to hyphen
    ("lab", "lab-labmgt_srv"):           "lab-labmgt-srv",

    # rms: Alibaba has standardized name, KKUH/WAVE1 still have old names
    ("rms", "rmsmorgue"):               "csi-rms-morgue-java-service",
    ("rms", "rmsrules"):                "csi-rms-rules-java-sev",

    # dms: WAVE1 has old names, others have standardized
    ("dms", "dmsmiddleware"):           "document-management-middleware",
    ("dms", "dmsstorageengine"):        "document-management-engine",

    # ehr: WAVE1 has old name still present
    ("ehr", "ehrcommonjava"):           "csi-ehr-common-java-sev",

    # base: WAVE1 has old name still present
    ("base", "configui"):              "csi-uif-settings",
}


def main():
    dry_run = "--dry-run" in sys.argv

    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"Mode: {mode}\n")

    total_fixed = 0
    total_skipped = 0
    log_entries = []

    for repo_name, repo_path in DEFAULT_REPOS.items():
        uat_dir = Path(repo_path) / "UAT"
        print(f"[{repo_name}]")

        if not uat_dir.exists():
            print(f"  UAT not found at {uat_dir}")
            continue

        for (module, wrong_name), correct_name in FIXES.items():
            wrong_path = uat_dir / module / wrong_name
            correct_path = uat_dir / module / correct_name

            if not wrong_path.exists():
                continue

            if correct_path.exists():
                # Target already exists - this is a duplicate/conflict
                print(f"  CONFLICT: {module}/{wrong_name} -> {correct_name} (target already exists)")
                log_entries.append(f"CONFLICT | {repo_name} | `{module}/{wrong_name}` -> `{module}/{correct_name}` | target already exists")
                total_skipped += 1
                continue

            if dry_run:
                print(f"  WOULD RENAME: {module}/{wrong_name} -> {module}/{correct_name}")
                log_entries.append(f"WOULD RENAME | {repo_name} | `{module}/{wrong_name}` -> `{module}/{correct_name}`")
            else:
                correct_path.parent.mkdir(parents=True, exist_ok=True)
                os.rename(wrong_path, correct_path)
                print(f"  RENAMED: {module}/{wrong_name} -> {module}/{correct_name}")
                log_entries.append(f"RENAMED | {repo_name} | `{module}/{wrong_name}` -> `{module}/{correct_name}`")
                total_fixed += 1

        print()

    # Write log
    log_file = OUTPUT_DIR / "uat_fix_log.md"
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("# UAT Inconsistency Fix Log\n\n")
        f.write(f"Mode: {mode}\n\n")
        f.write("| Action | Repo | Rename | Note |\n")
        f.write("|---|---|---|---|\n")
        for entry in log_entries:
            parts = entry.split(" | ")
            if len(parts) == 4:
                f.write(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} |\n")
            else:
                f.write(f"| {parts[0]} | {parts[1]} | {parts[2]} | |\n")
        f.write(f"\n**Total: {total_fixed} renamed, {total_skipped} skipped**\n")

    print(f"Total: {total_fixed} renamed, {total_skipped} skipped")
    print(f"Log saved to {log_file}")


if __name__ == "__main__":
    main()
