#!/usr/bin/env python3
"""Public-safety scan for review-facing repository files.

This check is intentionally conservative and dependency-free. It looks for
patterns that should not appear in public skill packages or application evidence:

- private-key blocks;
- common cloud / GitHub token markers;
- local-user paths;
- unsupported adoption claims.

It is not a full secret scanner and does not replace gitleaks or human review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".sh", ".txt"}
EXCLUDED_DIRS = {".git", ".venv", "node_modules", "dist", "build", "__pycache__"}

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("OpenAI project key", re.compile(r"sk-proj-[A-Za-z0-9_-]{20,}")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("macOS user path", re.compile(r"/Users/[A-Za-z0-9._-]+")),
    ("Linux home path", re.compile(r"/home/[A-Za-z0-9._-]+")),
    ("Windows user path", re.compile(r"[A-Za-z]:\\\\Users\\\\[A-Za-z0-9._-]+")),
]

UNSUPPORTED_CLAIMS = [
    "thousands of users",
    "millions of users",
    "production adoption",
    "widely adopted",
    "official openai",
    "openai endorsed",
]

ALLOWED_LOCAL_PATH_EXAMPLES = {
    "examples/local-agent-handoff.md",
}


def should_scan(path: Path) -> bool:
    relative_parts = path.relative_to(ROOT).parts
    if any(part in EXCLUDED_DIRS for part in relative_parts):
        return False
    return path.is_file() and path.suffix in SCAN_SUFFIXES


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    findings: list[str] = []

    for path in sorted(ROOT.rglob("*")):
        if not should_scan(path):
            continue

        relative = rel(path)
        text = path.read_text(encoding="utf-8", errors="replace")

        for label, pattern in PATTERNS:
            if relative in ALLOWED_LOCAL_PATH_EXAMPLES and "path" in label:
                continue
            if pattern.search(text):
                findings.append(f"{relative}: matched {label}")

        lowered = text.lower()
        for claim in UNSUPPORTED_CLAIMS:
            if claim in lowered:
                findings.append(f"{relative}: unsupported adoption/endorsement claim: {claim}")

    if findings:
        print("FAIL: public-safety scan found review blockers", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1

    print("PASS: public-safety scan found no blocked token, private-key, local-path, or unsupported-adoption patterns")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
