#!/usr/bin/env python3
"""
Generate PROD_NEW from UAT for a given repo.

Takes UAT as source of truth, copies it to PROD_NEW, and applies transformation rules:
  Rule 1: bases CENTRAL-BASE-REPO -> DEPLOYMENT-BASE-REPO
  Rule 2: images section left untouched
  Rule 3: patchesJson6902 target name for kind:Deployment -> deployment name from DEPLOYMENT-BASE-REPO
  Rule 4: patch-hpa.yaml metadata.name -> deployment name from DEPLOYMENT-BASE-REPO
  Rule 5: namespace vida-uat -> vida-prod

PROD-only services (not in UAT) are copied as-is.
"""

import os
import re
import shutil
import sys
from pathlib import Path

# --- Configuration ---
DEPLOYMENT_BASE_REPO = Path("/home/verosha/Documents/gittea/DEPLOYMENT-BASE-REPO")

REPOS = {
    "Alibaba": Path("/home/verosha/Documents/gittea/Alibaba"),
}

SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode"}


# --- Step 1: Build deployment name lookup ---

def build_deployment_lookup(base_repo: Path) -> dict:
    """Scan DEPLOYMENT-BASE-REPO for Deployment.yaml files, return {relative_path: metadata_name}."""
    lookup = {}
    for dep_file in base_repo.rglob("Deployment.yaml"):
        rel = dep_file.parent.relative_to(base_repo)
        try:
            content = dep_file.read_text(encoding="utf-8")
            # metadata.name may not be the first field under metadata
            # (labels, annotations etc. can come before name)
            match = re.search(r"metadata:\s*\n(?:\s+\S.*\n)*?\s+name:\s*(.+)", content)
            if match:
                lookup[str(rel)] = match.group(1).strip()
        except Exception as e:
            print(f"  WARNING: Could not read {dep_file}: {e}")
    return lookup


def resolve_deployment_name(kustomization_content: str, service_rel_path: str, lookup: dict) -> str:
    """
    Resolve the deployment name for a service.
    First try extracting the path from bases URL, then fall back to folder path matching.
    """
    # Try to extract path from bases URL
    # Match: .../DEPLOYMENT-BASE-REPO/module/service or .../CENTRAL-BASE-REPO/module/service
    bases_match = re.search(
        r"(?:DEPLOYMENT-BASE-REPO|CENTRAL-BASE-REPO)/(.+)",
        kustomization_content
    )
    if bases_match:
        base_path = bases_match.group(1).strip()
        if base_path in lookup:
            return lookup[base_path]

    # Fall back to folder path (module/service)
    if service_rel_path in lookup:
        return lookup[service_rel_path]

    return ""


# --- Step 3: Transform kustomization.yaml ---

def transform_kustomization(content: str, dep_name: str) -> str:
    """Apply Rules 1, 3, 5 to a kustomization.yaml content string. Rule 2: images untouched."""

    # Rule 1: Replace CENTRAL-BASE-REPO with DEPLOYMENT-BASE-REPO in bases URLs
    content = content.replace("CENTRAL-BASE-REPO", "DEPLOYMENT-BASE-REPO")

    # Rule 5: Replace namespace vida-uat -> vida-prod (top-level namespace line)
    content = re.sub(
        r"^(namespace:\s*)vida-uat",
        r"\1vida-prod",
        content,
        flags=re.MULTILINE,
    )

    # Rule 3: In patchesJson6902, update target name for kind: Deployment
    if dep_name:
        content = _update_patches_deployment_name(content, dep_name)

    return content


def _update_patches_deployment_name(content: str, dep_name: str) -> str:
    """
    Find patchesJson6902 targets with kind: Deployment and update their name field.
    Handles both patchesJson6902 and patchesJSON6902 (case-insensitive key).
    """
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        result.append(line)

        # Detect a target block with kind: Deployment
        # We need to look for a sequence like:
        #   - target:
        #       ...
        #       kind: Deployment
        #       name: <old_name>
        # The target block is within patchesJson6902 section
        if re.match(r"\s*-\s*target:\s*$", line):
            # Collect the target block lines until we hit the next section
            target_lines = []
            has_deployment_kind = False
            name_line_idx = None
            j = i + 1

            while j < len(lines):
                tline = lines[j]
                # Check if we've left the target block
                # A target block ends when we see a line at the same or lower indent as "- target:"
                # or a "patch:" line at the same level
                stripped = tline.strip()
                if stripped and not stripped.startswith("#"):
                    # Check indent level - target fields are indented more than "- target:"
                    target_indent = len(line) - len(line.lstrip())
                    current_indent = len(tline) - len(tline.lstrip())
                    if current_indent <= target_indent and stripped not in (""):
                        break

                if re.match(r"\s*kind:\s*Deployment\s*$", tline):
                    has_deployment_kind = True
                if re.match(r"\s*name:\s*\S+", tline) and not re.match(r"\s*name:\s*\.\*", tline):
                    name_line_idx = len(target_lines)

                target_lines.append(tline)
                j += 1

            # If this target is for a Deployment, update the name
            if has_deployment_kind and name_line_idx is not None:
                old_line = target_lines[name_line_idx]
                new_line = re.sub(r"(name:\s*)\S+", rf"\g<1>{dep_name}", old_line)
                target_lines[name_line_idx] = new_line

            result.extend(target_lines)
            i = j
            continue

        i += 1

    return "\n".join(result)


# --- Step 4: Transform patch-hpa.yaml ---

def transform_patch_hpa(content: str, dep_name: str) -> str:
    """Rule 4: Update metadata.name in patch-hpa.yaml to match deployment name."""
    if not dep_name:
        return content

    # Match the metadata > name field
    content = re.sub(
        r"(metadata:\s*\n\s*name:\s*)\S+",
        rf"\g<1>{dep_name}",
        content,
    )
    return content


# --- Main logic ---

def get_all_services(folder: Path) -> dict:
    """
    Get all services in a UAT/PROD folder.
    Returns {relative_path: absolute_path} where relative_path is like 'module/service' or 'service' (top-level).
    """
    services = {}
    if not folder.exists():
        return services

    for item in sorted(folder.iterdir()):
        if item.name in SKIP or not item.is_dir():
            continue

        # Check if this is a module (has subdirectories that are services) or a standalone service
        has_kustomization = (item / "kustomization.yaml").exists()
        subdirs = [d for d in item.iterdir() if d.is_dir() and d.name not in SKIP]

        if has_kustomization or not subdirs:
            # Standalone service (e.g., otp-service/, superset/)
            services[item.name] = item
        else:
            # Module with sub-services
            for sub in sorted(item.iterdir()):
                if sub.is_dir() and sub.name not in SKIP:
                    services[f"{item.name}/{sub.name}"] = sub

    return services


def copy_service(src: Path, dst: Path):
    """Copy a service directory, preserving all files."""
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def process_repo(repo_name: str, repo_path: Path, lookup: dict):
    """Process a single repo: generate PROD_NEW from UAT."""
    uat_dir = repo_path / "UAT"
    prod_dir = repo_path / "PROD"
    prod_new_dir = repo_path / "PROD_NEW"

    if not uat_dir.exists():
        print(f"  ERROR: UAT folder not found at {uat_dir}")
        return

    # Clean PROD_NEW if it exists
    if prod_new_dir.exists():
        shutil.rmtree(prod_new_dir)
    prod_new_dir.mkdir()

    print(f"  Scanning UAT services...")
    uat_services = get_all_services(uat_dir)
    print(f"  Found {len(uat_services)} services in UAT")

    prod_services = get_all_services(prod_dir) if prod_dir.exists() else {}
    print(f"  Found {len(prod_services)} services in PROD")

    # Identify PROD-only services
    prod_only = {k: v for k, v in prod_services.items() if k not in uat_services}
    print(f"  Found {len(prod_only)} PROD-only services to copy as-is")

    transformed = 0
    warnings = []

    # Step 2 & 3: Copy UAT services to PROD_NEW and transform
    for rel_path, src_path in uat_services.items():
        dst_path = prod_new_dir / rel_path
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        copy_service(src_path, dst_path)

        # Resolve deployment name
        kust_file = dst_path / "kustomization.yaml"
        dep_name = ""
        if kust_file.exists():
            kust_content = kust_file.read_text(encoding="utf-8")
            dep_name = resolve_deployment_name(kust_content, rel_path, lookup)

            if not dep_name:
                warnings.append(f"    WARNING: No deployment name found for {rel_path}")

            # Transform kustomization.yaml
            new_content = transform_kustomization(kust_content, dep_name)
            kust_file.write_text(new_content, encoding="utf-8")

        # Transform patch-hpa.yaml if it exists
        hpa_file = dst_path / "patch-hpa.yaml"
        if hpa_file.exists() and dep_name:
            hpa_content = hpa_file.read_text(encoding="utf-8")
            new_hpa = transform_patch_hpa(hpa_content, dep_name)
            hpa_file.write_text(new_hpa, encoding="utf-8")

        transformed += 1

    # Step 5: Copy PROD-only services as-is
    for rel_path, src_path in prod_only.items():
        dst_path = prod_new_dir / rel_path
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        copy_service(src_path, dst_path)
        print(f"    Copied PROD-only: {rel_path}")

    print(f"\n  Transformed {transformed} services from UAT")
    print(f"  Copied {len(prod_only)} PROD-only services")
    if warnings:
        print(f"\n  Warnings ({len(warnings)}):")
        for w in warnings:
            print(w)

    print(f"\n  PROD_NEW created at: {prod_new_dir}")


def main():
    # Usage: python generate_prod_from_uat.py [repo_name]
    # Default: all repos in REPOS dict
    repo_names = sys.argv[1:] if len(sys.argv) > 1 else list(REPOS.keys())

    print("Building deployment name lookup from DEPLOYMENT-BASE-REPO...")
    lookup = build_deployment_lookup(DEPLOYMENT_BASE_REPO)
    print(f"  Found {len(lookup)} deployment mappings\n")

    for repo_name in repo_names:
        if repo_name not in REPOS:
            print(f"Unknown repo: {repo_name}")
            continue

        print(f"[{repo_name}]")
        process_repo(repo_name, REPOS[repo_name], lookup)
        print()

    print("Done!")


if __name__ == "__main__":
    main()
