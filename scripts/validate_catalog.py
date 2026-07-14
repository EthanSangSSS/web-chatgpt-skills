#!/usr/bin/env python3
"""Validate the public skill catalog without third-party dependencies.

This intentionally avoids PyYAML so the check can run on a clean GitHub Actions
Python environment. It validates the conventions this repository depends on:

- CATALOG.yaml exists and declares the expected repository.
- Each catalog item has an id and path.
- Each referenced skill path exists.
- Each referenced skill file contains a visible skill title / content.
- README and governance files required for public OSS review exist.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "CATALOG.yaml"
REQUIRED_FILES = [
    "README.md",
    "CATALOG.yaml",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/CODEX_FOR_OSS_APPLICATION.md",
    "docs/MAINTAINER_RUNBOOK.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")


def extract_catalog_entries(text: str) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    current_id: str | None = None

    for line in text.splitlines():
        id_match = re.match(r"\s*-\s+id:\s*([^#\s]+)\s*$", line)
        if id_match:
            current_id = id_match.group(1).strip().strip('"\'')
            continue

        path_match = re.match(r"\s+path:\s*([^#\s]+)\s*$", line)
        if path_match and current_id:
            path = path_match.group(1).strip().strip('"\'')
            entries.append((current_id, path))
            current_id = None

    return entries


def main() -> int:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"required public-review file missing: {relative}")

    catalog_text = read(CATALOG)

    if "repository: EthanSangSSS/web-chatgpt-skills" not in catalog_text:
        fail("CATALOG.yaml must declare repository: EthanSangSSS/web-chatgpt-skills")

    if "evidence_rule: do_not_claim_unverified_execution" not in catalog_text:
        fail("CATALOG.yaml must preserve the unverified-execution evidence rule")

    entries = extract_catalog_entries(catalog_text)
    if not entries:
        fail("no skill entries found in CATALOG.yaml")

    seen_ids: set[str] = set()
    missing_paths: list[str] = []
    invalid_skill_files: list[str] = []

    for skill_id, skill_path in entries:
        if skill_id in seen_ids:
            fail(f"duplicate skill id: {skill_id}")
        seen_ids.add(skill_id)

        target = ROOT / skill_path
        if not target.is_file():
            missing_paths.append(f"{skill_id}: {skill_path}")
            continue

        body = read(target).strip()
        if len(body) < 40 or "#" not in body:
            invalid_skill_files.append(f"{skill_id}: {skill_path}")

    if missing_paths:
        fail("catalog paths do not exist:\n" + "\n".join(f"- {p}" for p in missing_paths))

    if invalid_skill_files:
        fail("skill files look incomplete:\n" + "\n".join(f"- {p}" for p in invalid_skill_files))

    print(f"PASS: validated {len(entries)} catalog skill entries and {len(REQUIRED_FILES)} public-review files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
