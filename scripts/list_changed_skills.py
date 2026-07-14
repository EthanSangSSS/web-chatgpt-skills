#!/usr/bin/env python3
"""List skill packages affected by a PR or push.

This script is a reviewer aid, not a blocker. It prints changed `<skill>/...`
paths so maintainers can apply the release checklist to skill-affecting PRs.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_git(args: list[str]) -> list[str]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"WARN: git {' '.join(args)} failed; falling back to catalog-wide review")
        if exc.stderr:
            print(exc.stderr.strip())
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def changed_files() -> list[str]:
    base_ref = os.environ.get("GITHUB_BASE_REF")
    if base_ref:
        return run_git(["diff", "--name-only", f"origin/{base_ref}...HEAD"])
    return run_git(["diff", "--name-only", "HEAD~1..HEAD"])


def is_skill_path(path: str) -> bool:
    parts = path.split("/")
    if len(parts) < 2:
        return False
    if parts[0] in {".github", "docs", "examples", "scripts", "tests", "schemas", "tools"}:
        return False
    return parts[1] == "SKILL.md" or path.endswith("/SKILL.md")


def main() -> int:
    files = changed_files()
    skill_paths = sorted(path for path in files if is_skill_path(path))

    if not skill_paths:
        print("INFO: no changed skill entrypoints detected")
        return 0

    print("INFO: changed skill entrypoints detected; apply release checklist:")
    for path in skill_paths:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
