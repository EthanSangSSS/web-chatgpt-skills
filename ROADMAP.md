# Roadmap

This roadmap keeps `web-chatgpt-skills` focused on maintainable, evidence-bounded AI-agent workflows. It is intentionally conservative: no milestone should claim adoption, safety, or compatibility that has not been verified.

## v0.1.x — Public readiness baseline

Goal: make the repository easy to review, validate, and maintain as an early-stage OSS skill registry.

- Keep `CATALOG.yaml` as the canonical registry entrypoint.
- Keep every skill package at the canonical `<skill>/SKILL.md` path.
- Preserve the evidence rule: do not claim local execution, tests, builds, scans, or background work without tool or command evidence.
- Maintain public governance files: `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, pull request template, CODEOWNERS, maintainer runbook, and application evidence.
- Run `scripts/validate_catalog.py` in CI for pushes to `main` and pull requests.
- Add public-safety checks for secrets, private-key markers, local-user paths, and unsupported adoption claims.

## v0.2.x — Safety and regression fixtures

Goal: turn the skill safety model into repeatable review evidence.

- Add regression fixtures for unsafe local-execution claims.
- Add examples of bounded local-agent handoffs.
- Add prompt-security review guidance for executable-adjacent instructions.
- Add catalog metadata checks for status, priority, category, trigger coverage, and non-trigger boundaries.
- Add release-readiness checks for new skills and migrated packages.
- Add issue labels and triage categories for skill bugs, safety risks, documentation debt, and validation gaps.

## v0.3.x — Contributor workflow and release discipline

Goal: make outside review possible without relying on private context.

- Publish a `v0.1.0` release baseline once the roadmap, threat model, release checklist, and safety checks have landed.
- Add a release checklist for each new or changed skill package.
- Add self-contained usage examples for debugging, TDD, GitHub review, architecture diagrams, and local-agent handoff.
- Add compatibility notes for Web ChatGPT, Codex, local Codex skill sync, and GitHub connector usage.
- Add a lightweight changelog convention for catalog changes.

## Out of scope

- Do not claim official OpenAI support or endorsement.
- Do not include private prompts, credentials, proprietary source, private logs, local paths, employer data, or customer data.
- Do not optimize for synthetic stars, forks, or usage metrics.
- Do not merge skills that require unsafe permissions, broad local filesystem access, credential discovery, destructive operations, or unverifiable execution claims.
