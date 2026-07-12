#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required=(
  "SKILL.md"
  "references/truth-protocol.md"
  "references/source-policy.md"
  "agents/openai.yaml"
  "templates/truth-seeking-report.md"
  "examples/fictional-platform-decline.md"
  "README.md"
  "LICENSE"
  "tests/check_fixtures.sh"
)

for file in "${required[@]}"; do
  test -f "$ROOT/$file" || {
    echo "Missing required file: $file" >&2
    exit 1
  }
done

grep -q '^---$' "$ROOT/SKILL.md"
grep -q '^name: truth-seeking$' "$ROOT/SKILL.md"
grep -q '^description: ' "$ROOT/SKILL.md"
grep -q 'Use directly' "$ROOT/SKILL.md"
grep -q 'generic research router' "$ROOT/SKILL.md"
grep -q 'Default Compact Rule' "$ROOT/SKILL.md"
grep -q 'Defaults to compact outputs' "$ROOT/SKILL.md"
grep -q 'Relative Weight (0-100)' "$ROOT/templates/truth-seeking-report.md"
grep -q 'Base-rate / reference-class anchor' "$ROOT/templates/truth-seeking-report.md"
grep -q 'Bayesian update trigger' "$ROOT/templates/truth-seeking-report.md"
grep -q 'Two Tier 2 sources count as independent' "$ROOT/references/source-policy.md"

# Run fixture validation
bash "$ROOT/tests/check_fixtures.sh"

# Ban absolute truth phrasings in core files
forbidden_patterns=(
  "root truth"
  "most likely truth"
  "最可能的真相"
)

echo "Checking for banned absolute truth phrasings..."
for pattern in "${forbidden_patterns[@]}"; do
  if grep -rn -i "$pattern" "$ROOT/SKILL.md" "$ROOT/README.md" "$ROOT/references/truth-protocol.md" "$ROOT/references/source-policy.md" "$ROOT/templates/truth-seeking-report.md" "$ROOT/agents/openai.yaml" >/dev/null 2>&1; then
    echo "Error: Banned absolute phrasing '$pattern' detected in core skill files:" >&2
    grep -rn -i "$pattern" "$ROOT/SKILL.md" "$ROOT/README.md" "$ROOT/references/truth-protocol.md" "$ROOT/references/source-policy.md" "$ROOT/templates/truth-seeking-report.md" "$ROOT/agents/openai.yaml" || true
    exit 1
  fi
done

if grep -R -nE 'deep-research-router|deep-mining-automation|reliable-signal-gathering|/Users/[^[:space:]]+|AI Agent Database|Feishu|Obsidian' "$ROOT" \
  --exclude-dir=.git \
  --exclude='validate.sh'; then
  echo "Private/local coupling detected." >&2
  exit 1
fi

echo "truth-seeking-skill validation passed"
