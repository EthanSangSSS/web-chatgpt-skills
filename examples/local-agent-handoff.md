# Example: Bounded Local-Agent Handoff

Use this pattern when Web ChatGPT or a connector-backed assistant cannot safely run local commands, edit many files, build an app, access a simulator, or validate a local environment.

## Handoff packet

```text
/goal
Repository: owner/repo
Branch: feature/example
Expected remote HEAD: <sha>
Task: Make the smallest change needed to fix <issue>.

Version-sync gate:
1. git fetch origin
2. git status --short
3. git branch --show-current
4. git rev-parse HEAD
5. git rev-parse origin/<branch>
6. If the worktree is dirty, stop and report.
7. If the branch is wrong, stop and report.
8. If local HEAD != origin/<branch>, run git pull --ff-only origin <branch>.
9. If fast-forward fails, stop and report.

Allowed files:
- path/to/file_a.md
- path/to/file_b.py

Forbidden actions:
- Do not edit unrelated files.
- Do not read secrets, tokens, browser profiles, SSH keys, or private logs.
- Do not force-push, rewrite history, or delete branches.
- Do not claim tests passed unless commands actually ran and output is captured.

Validation commands:
- python3 scripts/validate_catalog.py
- python3 scripts/check_public_safety.py
- git diff --check
- git status --short

Stop conditions:
- Dirty worktree before sync.
- Branch mismatch.
- Non-fast-forward state.
- Validation requires out-of-scope changes.
- Suspected secret or private-data exposure.

Final output:
1. Verdict
2. Starting and final HEAD
3. Files changed
4. Exact validation outputs
5. Risks / limitations
```

## Why this matters

A bounded handoff is safer than telling an AI agent to "fix everything". It makes state, scope, forbidden actions, validation, and stop conditions explicit.
