#!/usr/bin/env python3
"""Deterministic regression checks for the grill-me convergence contract.

The validator protects the v0.2.0 behavior that separates conversation exit from
artifact readiness. It does not attempt to simulate language-model reasoning; it
checks required contract text and runs small decision fixtures against the
explicit convergence rules.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "grill-me" / "SKILL.md"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "grill-me-exit"

REQUIRED_SKILL_MARKERS = [
    'version: "0.2.1"',
    "## Two independent gates",
    "### Gate A — Conversation Exit Gate",
    "### Gate B — Artifact Readiness Gate",
    "Conversation exit does not imply `PASS`",
    "## Value-of-information gate",
    "## Stable decision policy compression",
    "## Mandatory convergence checkpoint",
    "Default budget",
    "Hard limit",
    "Reaching the hard limit forces synthesis",
    "Treat user fatigue and explicit convergence requests as strong exit signals",
]

VALID_ACTIONS = {"CONTINUE", "SYNTHESIZE", "HANDOFF", "STOP"}
VALID_VERDICTS = {"PASS", "PASS_WITH_WARNINGS", "REVISE", "INCONCLUSIVE", "STOP"}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError(f"expected true/false, got {value!r}")


def parse_fixture(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def decide_action(data: dict[str, str]) -> str:
    questions_answered = int(data["questions_answered"])
    default_budget = int(data["default_budget"])
    hard_limit = int(data["hard_limit"])
    extension_count = int(data.get("extension_count", "0"))
    no_change_streak = int(data.get("no_change_streak", "0"))

    user_exit_signal = parse_bool(data.get("user_exit_signal", "false"))
    p0_blocker = parse_bool(data.get("p0_blocker", "false"))
    next_question_material = parse_bool(data.get("next_question_material", "false"))
    stable_policy_resolves = parse_bool(data.get("stable_policy_resolves", "false"))
    extension_justified = parse_bool(data.get("extension_justified", "false"))
    ready_for_handoff = parse_bool(data.get("ready_for_handoff", "false"))

    if p0_blocker:
        return "STOP"
    if ready_for_handoff and not next_question_material:
        return "HANDOFF"
    if user_exit_signal:
        return "SYNTHESIZE"
    if questions_answered >= hard_limit:
        return "SYNTHESIZE"
    if stable_policy_resolves:
        return "SYNTHESIZE"
    if no_change_streak >= 2:
        return "SYNTHESIZE"
    if not next_question_material:
        return "SYNTHESIZE"
    if questions_answered >= default_budget:
        if not extension_justified or extension_count >= 2:
            return "SYNTHESIZE"
    return "CONTINUE"


def main() -> int:
    if not SKILL.is_file():
        fail("missing grill-me/SKILL.md")

    skill_text = SKILL.read_text(encoding="utf-8")
    missing_markers = [marker for marker in REQUIRED_SKILL_MARKERS if marker not in skill_text]
    if missing_markers:
        fail("grill-me exit contract is missing markers:\n" + "\n".join(f"- {m}" for m in missing_markers))

    if not FIXTURE_DIR.is_dir():
        fail("missing tests/fixtures/grill-me-exit")

    failures: list[str] = []
    fixture_count = 0
    saw_exit_with_nonpass = False
    saw_material_continue = False
    saw_p0_stop = False

    required_fields = {
        "questions_answered",
        "default_budget",
        "hard_limit",
        "expected_action",
        "expected_artifact_verdict",
    }

    for path in sorted(FIXTURE_DIR.glob("*.md")):
        fixture_count += 1
        try:
            data = parse_fixture(path)
            missing = sorted(required_fields - data.keys())
            if missing:
                raise ValueError(f"missing fields: {', '.join(missing)}")

            expected_action = data["expected_action"]
            expected_verdict = data["expected_artifact_verdict"]
            if expected_action not in VALID_ACTIONS:
                raise ValueError(f"invalid expected_action: {expected_action}")
            if expected_verdict not in VALID_VERDICTS:
                raise ValueError(f"invalid expected_artifact_verdict: {expected_verdict}")

            actual_action = decide_action(data)
            if actual_action != expected_action:
                failures.append(f"{path.relative_to(ROOT)}: expected {expected_action}, got {actual_action}")

            if expected_action in {"SYNTHESIZE", "HANDOFF"} and expected_verdict in {"REVISE", "INCONCLUSIVE", "STOP"}:
                saw_exit_with_nonpass = True
            if expected_action == "CONTINUE" and parse_bool(data.get("next_question_material", "false")):
                saw_material_continue = True
            if expected_action == "STOP" and parse_bool(data.get("p0_blocker", "false")):
                saw_p0_stop = True
        except (KeyError, ValueError) as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")

    if fixture_count < 6:
        failures.append(f"expected at least 6 grill-me exit fixtures, found {fixture_count}")
    if not saw_exit_with_nonpass:
        failures.append("fixtures must prove that conversation exit can retain a non-PASS artifact verdict")
    if not saw_material_continue:
        failures.append("fixtures must include a material question that legitimately continues")
    if not saw_p0_stop:
        failures.append("fixtures must include a P0 blocker that forces STOP")

    if failures:
        print("FAIL: grill-me exit contract regression", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"PASS: grill-me exit contract checked {fixture_count} fixtures and required v0.2.1 markers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
