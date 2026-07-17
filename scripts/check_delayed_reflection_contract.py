#!/usr/bin/env python3
"""Validate the delayed-reflection-loop skill contract and public fixtures.

This check is intentionally dependency-free. It does not simulate an LLM. It
verifies deterministic authorization, state-consistency, idempotency, privacy,
and crisis-stop rules that must not be left to free-form interpretation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "delayed-reflection-loop" / "SKILL.md"
CASES = ROOT / "tests" / "fixtures" / "delayed-reflection-loop" / "cases.json"

PRIVACY_VALUES = {
    "no_identifiers",
    "anonymized",
    "user_approved_identifiers",
}

REQUIRED_SKILL_MARKERS = [
    'version: "0.2.0"',
    "## Durable workflow state",
    "manual_phase_started_at",
    "permission_mode: manual | automatic",
    "draft_id",
    "Previous two calendar dates",
    "privacy: no_identifiers | anonymized | user_approved_identifiers",
    "weekly/YYYY/YYYY-Www.md",
    "monthly/YYYY/YYYY-MM.md",
    "valid recorded day",
    "tests/fixtures/delayed-reflection-loop/cases.json",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def decide(case: dict[str, Any]) -> str:
    if case.get("crisis"):
        return "STOP"

    if int(case.get("char_count", 0)) > 300:
        return "DENY"

    privacy = case.get("privacy")
    if privacy not in PRIVACY_VALUES:
        return "DENY"

    status = case.get("status")
    review_metadata_present = bool(case.get("review_metadata_present"))
    if status == "pending_review" and review_metadata_present:
        return "DENY"
    if status == "reviewed" and not review_metadata_present:
        return "DENY"

    if case.get("entry_mode") == "retrospective":
        if case.get("review_mode") != "retrospective_same_session":
            return "DENY"

    if case.get("operation") == "update_review" and not case.get("d0_unchanged", True):
        return "DENY"

    if case.get("path_exists"):
        return "NO_OP" if case.get("identical_content") else "STOP"

    if not case.get("durable_state"):
        return "MANUAL_ONLY"

    artifact_type = case.get("artifact_type")
    explicit_confirmation = bool(case.get("explicit_confirmation"))

    if artifact_type in {"weekly", "monthly"}:
        return "ALLOW" if explicit_confirmation else "DENY"

    permission_mode = case.get("permission_mode")
    if permission_mode == "manual":
        if not explicit_confirmation:
            return "DENY"
        if case.get("draft_id") != case.get("current_draft_id"):
            return "DENY"
        return "ALLOW"

    if permission_mode == "automatic":
        if not case.get("automatic_enabled"):
            return "MANUAL_ONLY"
        if artifact_type not in {"daily", "review"}:
            return "DENY"
        return "ALLOW"

    return "DENY"


def main() -> int:
    try:
        skill_text = SKILL.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing skill file: {SKILL.relative_to(ROOT)}")

    missing_markers = [marker for marker in REQUIRED_SKILL_MARKERS if marker not in skill_text]
    if missing_markers:
        fail("missing required skill markers:\n" + "\n".join(f"- {m}" for m in missing_markers))

    try:
        cases = json.loads(CASES.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing fixture file: {CASES.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid fixture JSON: {exc}")

    if not isinstance(cases, list) or not cases:
        fail("fixture file must contain a non-empty list")

    names: set[str] = set()
    failures: list[str] = []
    for raw_case in cases:
        if not isinstance(raw_case, dict):
            failures.append("fixture entry is not an object")
            continue
        name = str(raw_case.get("name", "")).strip()
        if not name:
            failures.append("fixture missing name")
            continue
        if name in names:
            failures.append(f"duplicate fixture name: {name}")
            continue
        names.add(name)

        inputs = raw_case.get("input")
        expected = raw_case.get("expected")
        if not isinstance(inputs, dict):
            failures.append(f"{name}: input must be an object")
            continue

        actual = decide(inputs)
        if actual != expected:
            failures.append(f"{name}: expected {expected}, got {actual}")

    if failures:
        fail("contract fixture failures:\n" + "\n".join(f"- {item}" for item in failures))

    print(f"PASS: validated delayed reflection contract with {len(cases)} fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
