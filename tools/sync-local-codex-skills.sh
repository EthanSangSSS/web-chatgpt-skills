#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
truth_source="$repo_root/truth-seeking"
rational_source="$repo_root/rational-product-evaluation"
codex_root="$HOME/.codex/skills"

for package_source in "$truth_source" "$rational_source"; do
  if [[ ! -f "$package_source/SKILL.md" ]]; then
    printf 'refusing to sync: missing %s/SKILL.md\n' "$package_source" >&2
    exit 1
  fi
done

mkdir -p "$codex_root"
rsync -a --delete "$truth_source/" "$codex_root/truth-seeking/"
rsync -a --delete "$rational_source/" "$codex_root/rational-product-evaluation/"

printf 'Synced %s\n' "$codex_root/truth-seeking"
printf 'Synced %s\n' "$codex_root/rational-product-evaluation"
