# Release Checklist

Use this checklist before publishing a tagged release or announcing a new skill package baseline.

## 1. Scope

- [ ] Release scope is clearly named.
- [ ] Changed skills are listed.
- [ ] Catalog changes are listed.
- [ ] Governance, CI, or validation changes are listed.
- [ ] The release does not claim unverified stars, downloads, production adoption, or external users.

## 2. Repository state

- [ ] Work is merged through a pull request unless an emergency direct commit is explicitly documented.
- [ ] `main` is clean and synchronized with `origin/main`.
- [ ] The release commit SHA is recorded.
- [ ] No force-push, history rewrite, or unrelated branch deletion is required.

## 3. Validation evidence

Run and paste outputs into release notes or the release PR:

```bash
python3 scripts/validate_catalog.py
python3 scripts/check_public_safety.py
git diff --check
git status --short
```

Expected results:

- `validate_catalog.py` exits 0.
- `check_public_safety.py` exits 0.
- `git diff --check` has no output.
- `git status --short` has no output after merge/sync.

## 4. Skill quality gate

For every changed skill:

- [ ] Trigger and non-trigger boundaries are clear.
- [ ] Output contract is clear.
- [ ] Evidence requirements are explicit.
- [ ] Local execution claims are forbidden unless backed by actual tool or command output.
- [ ] Handoff rules are bounded and reproducible.
- [ ] Examples are synthetic or public-safe.
- [ ] No secrets, credentials, private logs, private source, local-user paths, or employer/customer data are present.

## 5. Security gate

- [ ] `docs/SECURITY_THREAT_MODEL.md` still matches the changed surface.
- [ ] New instructions do not ask for credential discovery, broad filesystem scans, browser data, private keys, or destructive operations.
- [ ] CI permissions remain minimal.
- [ ] Any new script is dependency-light or justifies dependencies explicitly.
- [ ] Any Codex/local-agent handoff includes repo, branch, HEAD, file scope, forbidden actions, validation commands, stop conditions, and final output format.

## 6. Release notes template

```markdown
## vX.Y.Z — <release title>

### Summary

- <one-sentence purpose>

### Changed

- <catalog / skill / docs / CI changes>

### Validation

- `python3 scripts/validate_catalog.py`: <PASS / output>
- `python3 scripts/check_public_safety.py`: <PASS / output>
- `git diff --check`: <PASS / output>
- GitHub Actions: <run URL and conclusion>

### Security and honesty boundary

- No unverified adoption, stars, downloads, or production-use claims.
- No secrets, private logs, local paths, or private source intentionally included.
- Human review remains required before production use.
```

## 7. v0.1.0 candidate

Recommended first release title:

```text
v0.1.0 — Public OSS readiness baseline
```

Recommended first release scope:

- canonical skill catalog;
- public governance files;
- maintainer runbook;
- Codex for OSS application evidence;
- security threat model;
- release checklist;
- catalog validation;
- public-safety validation.
