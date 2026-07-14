#!/usr/bin/env python3
"""Regression validator for unsupported execution and validation claims.

This script checks curated fixtures under `tests/fixtures/unsafe-claims/`.
It is intentionally small and conservative. The goal is not to classify every
possible sentence; the goal is to keep the repository's strongest safety rule
from regressing: do not claim local execution, tests, builds, scans, or
background work without evidence.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "unsafe-claims"

UNSUPPORTED_CLAIM_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("unverified tests passed", re.compile(r"\b(I|we)\s+ran\s+.+tests?.+passed\b", re.I | re.S)),
    ("unverified local build", re.compile(r"\blocal\s+build\s+passed\b", re.I)),
    ("unavailable background work", re.compile(r"\bmonitor\s+.+\bbackground\b|\bbackground\s+.+\bnotify\s+you\s+later\b", re.I | re.S)),
]

EVIDENCE_PATTERNS = [
    re.compile(r"GitHub Actions run\s+`?\d+`?", re.I),
    re.compile(r"job\s+completed\s+with\s+conclusion\s+`?success`?", re.I),
    re.compile(r"tool output included", re.I),
    re.compile(r"command output", re.I),
]


def markdown_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    start = text.find("\n", start)
    if start == -1:
        return ""
    next_heading = text.find("\n## ", start + 1)
    if next_heading == -1:
        next_heading = len(text)
    return text[start:next_heading].strip()


def expected_result(path: Path, text: str) -> str:
    if "Expected validator result\n\n`PASS`" in text:
        return "PASS"
    if "Expected validator result\n\n`FAIL`" in text:
        return "FAIL"
    raise ValueError(f"fixture missing expected result marker: {path}")


def has_positive_evidence(evidence: str) -> bool:
    normalized = evidence.strip().lower()
    if not normalized or normalized.startswith("no "):
        return False
    return any(pattern.search(evidence) for pattern in EVIDENCE_PATTERNS)


def classify(text: str) -> str:
    claim = markdown_section(text, "User-visible claim") or text
    evidence = markdown_section(text, "Evidence")

    has_unsupported_claim = any(pattern.search(claim) for _, pattern in UNSUPPORTED_CLAIM_PATTERNS)
    has_evidence = has_positive_evidence(evidence)

    if has_unsupported_claim and not has_evidence:
        return "FAIL"
    return "PASS"


def main() -> int:
    if not FIXTURE_DIR.is_dir():
        print(f"FAIL: missing fixture directory: {FIXTURE_DIR.relative_to(ROOT)}", file=sys.stderr)
        return 1

    failures: list[str] = []
    fixture_count = 0

    for path in sorted(FIXTURE_DIR.glob("*.md")):
        fixture_count += 1
        text = path.read_text(encoding="utf-8")
        expected = expected_result(path, text)
        actual = classify(text)
        if actual != expected:
            failures.append(f"{path.relative_to(ROOT)}: expected {expected}, got {actual}")

    if fixture_count == 0:
        print("FAIL: no unsafe-claim fixtures found", file=sys.stderr)
        return 1

    if failures:
        print("FAIL: unsafe-claim fixture regression", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"PASS: unsafe-claim validator checked {fixture_count} fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
