# Maintainer Runbook

This runbook defines the recurring maintenance workflow for `web-chatgpt-skills`.

## Maintainer principles

1. Verify repository state before editing.
2. Prefer small pull requests with narrow scope.
3. Preserve public-safe boundaries: no secrets, no private source, no employer/customer material.
4. Do not claim local execution, tests, builds, or background work unless tool evidence exists.
5. Use bounded local-agent handoffs when a task requires local shell access, credentials, generated artifacts, or multi-file changes beyond safe connector edits.

## Routine maintenance loop

### 1. Triage

For each issue or PR:

- identify affected skill/package/path;
- classify the request as documentation, skill behavior, validation, safety, or governance;
- decide whether it can be handled from GitHub-visible evidence or requires local execution;
- reject or redirect requests that require secrets, private data, unauthorized scans, or unsafe impersonation.

### 2. Review

For PRs, verify:

- `CATALOG.yaml` matches any added/moved/renamed skill package;
- skill trigger rules are specific enough to prevent accidental invocation;
- `do_not_use_for` boundaries are present for high-risk skills;
- output contracts avoid fabricated citations, hidden execution, or unsupported PASS verdicts;
- local-agent handoff text includes repo, branch, HEAD/PR metadata when available, file scope, forbidden actions, validation commands, stop conditions, and final output format.

### 3. Validate

Run when local shell is available:

```bash
python3 scripts/validate_catalog.py
```

If using Codex or another local agent, require a version-sync gate before edits:

```bash
git fetch origin
git status --short
git branch --show-current
git rev-parse HEAD
git rev-parse origin/main
```

Stop if the worktree is dirty, the branch is unexpected, or the local branch cannot fast-forward safely.

### 4. Merge readiness

Before merge:

- no test-only placeholder text;
- no local path leakage;
- no secrets or credentials;
- validation evidence is recorded;
- docs and catalog agree;
- PR body explains user impact and safety boundary.

### 5. Release notes

For a release, summarize:

- new / changed skills;
- compatibility impact;
- known limitations;
- validation performed;
- safe upgrade instructions for Web ChatGPT and local Codex users.

## Local-agent handoff template

Use this when web-only or connector-only execution is insufficient.

```text
/goal
Repository: EthanSangSSS/web-chatgpt-skills
Branch: <branch>
Expected HEAD: <sha>
Base: origin/main@<sha>
Task: <bounded objective>

Version-sync gate:
1. git fetch origin
2. git status --short
3. git branch --show-current
4. git rev-parse HEAD
5. git rev-parse origin/main
6. If HEAD != expected HEAD, run git pull --ff-only only when explicitly authorized. If fast-forward is impossible, stop and report.
7. If worktree is dirty, branch is wrong, PR is merged/closed unexpectedly, or remote HEAD differs from expected metadata, stop and report.

Allowed files:
- <paths>

Forbidden actions:
- Do not modify unrelated files.
- Do not add secrets, private logs, local paths, or private source.
- Do not claim tests passed unless commands actually ran and output is captured.
- Do not force-push, delete branches, or rewrite history.

Fix target:
- <specific expected change>

Validation commands:
- python3 scripts/validate_catalog.py
- git diff --check

Stop conditions:
- validation failure that cannot be fixed inside allowed scope;
- dirty worktree before starting;
- branch / HEAD mismatch;
- need for credentials or private files;
- uncertainty about public-safety boundary.

Final output format:
1. Verdict: PASS / PASS_WITH_WARNINGS / INCONCLUSIVE / FAIL / BLOCKED
2. Repository / branch / starting HEAD / final HEAD
3. Files changed
4. Validation commands and exact results
5. Risks / limitations
6. Follow-up required
```
