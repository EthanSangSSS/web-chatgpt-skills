#!/usr/bin/env python3
"""Public-safety scan for review-facing repository files.

This dependency-free check scans public review, governance, documentation, and
example files. It uses two severity levels:

- blockers: private-key blocks and common credential/token markers;
- warnings: local-user paths and assertive adoption / endorsement wording.

It is not a full secret scanner and does not replace gitleaks or human review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = [
    "README.md",
    "CATALOG.yaml",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs",
    "examples",
    ".github/PULL_REQUEST_TEMPLATE.md",
]
SCAN_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}

BLOCKING_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("OpenAI project key", re.compile(r"sk-proj-[A-Za-z0-9_-]{20,}")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
]

WARNING_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("macOS user path", re.compile(r"/Users/[A-Za-z0-9._-]+")),
    ("Linux home path", re.compile(r"/home/[A-Za-z0-9._-]+")),
    ("Windows user path", re.compile(r"[A-Za-z]:\\\\Users\\\\[A-Za-z0-9._-]+")),
    ("large user-base claim", re.compile(r"\b(we|this project|the project)\s+(has|serves|supports)\s+(thousands|millions)\s+of\s+users\b", re.I)),
    ("production adoption claim", re.compile(r"\b(we|this project|the project)\s+(has|shows|demonstrates)\s+production\s+adoption\b", re.I)),
    ("endorsement claim", re.compile(r"\b(we are|this project is|the project is)\s+(openai[- ]endorsed|an?\s+official\s+openai\s+(project|repo|repository|skill))\b", re.I)),
]

ALLOWED_LOCAL_PATH_EXAMPLES = {
    "examples/local-agent-handoff.md",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_scan_files() -> list[Path]:
    files: list[Path] = []
    for entry in SCAN_ROOTS:
        target = ROOT / entry
        if target.is_file():
            files.append(target)
            continue
        if target.is_dir():
            files.extend(path for path in target.rglob("*") if path.is_file() and path.suffix in SCAN_SUFFIXES)
    return sorted(set(files))


def main() -> int:
    blockers: list[str] = []
    warnings: list[str] = []

    for path in iter_scan_files():
        relative = rel(path)
        text = path.read_text(encoding="utf-8", errors="replace")

        for label, pattern in BLOCKING_PATTERNS:
            if pattern.search(text):
                blockers.append(f"{relative}: matched {label}")

        for label, pattern in WARNING_PATTERNS:
            if relative in ALLOWED_LOCAL_PATH_EXAMPLES and "path" in label:
                continue
            if pattern.search(text):
                warnings.append(f"{relative}: matched {label}")

    if blockers:
        print("FAIL: public-safety scan found blocking secret/key patterns", file=sys.stderr)
        for blocker in blockers:
            print(f"- {blocker}", file=sys.stderr)
        return 1

    for warning in warnings:
        print(f"WARN: {warning}")

    print(f"PASS: public-safety scan checked {len(iter_scan_files())} review-facing files with {len(warnings)} warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
