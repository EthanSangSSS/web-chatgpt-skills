#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

fixtures=(
  "rumor.md"
  "conspiracy_bait.md"
  "high_stakes_advice.md"
  "stale_facts.md"
  "moralization_bait.md"
  "overconfident_forecast.md"
  "mainland_media_trap.md"
  "stance_frame_trap.md"
  "bad_meter_event.md"
)

echo "Checking adversarial fixtures..."

for fixture in "${fixtures[@]}"; do
  path="$ROOT/tests/fixtures/$fixture"
  if [ ! -f "$path" ]; then
    echo "Error: Missing fixture $fixture at $path" >&2
    exit 1
  fi
  if ! grep -q "Trap Scenario" "$path"; then
    echo "Error: Fixture $fixture does not contain 'Trap Scenario'" >&2
    exit 1
  fi
  if ! grep -q "Expected Handling" "$path"; then
    echo "Error: Fixture $fixture does not contain 'Expected Handling'" >&2
    exit 1
  fi
done

grep -q "weak_or_unverified" "$ROOT/tests/fixtures/rumor.md"
grep -q "access_date" "$ROOT/tests/fixtures/stale_facts.md"
grep -q "Bayesian update trigger" "$ROOT/tests/fixtures/overconfident_forecast.md"
grep -q "Source Position Audit" "$ROOT/tests/fixtures/stance_frame_trap.md"
grep -q "Normative Frame Audit" "$ROOT/tests/fixtures/stance_frame_trap.md"
grep -q "statistical-definition change" "$ROOT/tests/fixtures/bad_meter_event.md"
grep -q "reported_signal" "$ROOT/tests/fixtures/bad_meter_event.md"
grep -q "independent validation" "$ROOT/tests/fixtures/bad_meter_event.md"
grep -q "bad-meter risk" "$ROOT/tests/fixtures/bad_meter_event.md"

echo "All 9 adversarial fixtures successfully verified!"
