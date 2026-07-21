# Web ChatGPT Skills

[![Catalog check](https://github.com/EthanSangSSS/web-chatgpt-skills/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/EthanSangSSS/web-chatgpt-skills/actions/workflows/catalog-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Scope](https://img.shields.io/badge/scope-Web%20ChatGPT%20%7C%20Codex%20%7C%20local%20agents-blue)](CATALOG.yaml)

`web-chatgpt-skills` is a public, remote-readable skill registry for Web ChatGPT, Codex, and local-agent workflows.

The repository packages reusable skills that make AI-assisted work safer and more repeatable: each skill should define when to use it, when not to use it, what evidence it may rely on, what output it should produce, and when it must stop and hand work to a local agent instead of pretending it executed locally.

## Reviewer fast path

Start here if you are evaluating the project as an OSS repository or OpenAI Codex for Open Source candidate:

- [`CATALOG.yaml`](CATALOG.yaml) — machine-readable skill registry and execution defaults.
- [`docs/CODEX_FOR_OSS_APPLICATION.md`](docs/CODEX_FOR_OSS_APPLICATION.md) — evidence packet and application wording.
- [`ROADMAP.md`](ROADMAP.md) — staged OSS maintenance plan.
- [`docs/SECURITY_THREAT_MODEL.md`](docs/SECURITY_THREAT_MODEL.md) — instruction-level security model for AI-agent skills.
- [`docs/PROMPT_SECURITY_REVIEW.md`](docs/PROMPT_SECURITY_REVIEW.md) — reviewer checklist for prompt-injection and unsafe tool-use patterns.
- [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md) — release-readiness checklist and `v0.1.0` candidate scope.
- [`docs/releases/v0.1.0.md`](docs/releases/v0.1.0.md) — prepared first public release notes and `gh release create` command.
- [`docs/MAINTAINER_RUNBOOK.md`](docs/MAINTAINER_RUNBOOK.md) — maintainer SOP for triage, review, validation, and local-agent handoff.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution rules and skill quality checklist.
- [`SECURITY.md`](SECURITY.md) — security scope and reporting policy.
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — PR checklist for maintenance evidence and safety boundaries.
- [`scripts/validate_catalog.py`](scripts/validate_catalog.py) — dependency-free catalog and public-review file validator.
- [`scripts/check_public_safety.py`](scripts/check_public_safety.py) — dependency-free scan that blocks credential/private-key markers and reports local-path or unsupported-claim wording as review warnings.
- [`scripts/check_unsafe_claims.py`](scripts/check_unsafe_claims.py) — regression check for unsupported execution and validation claims.
- [`scripts/check_delayed_reflection_contract.py`](scripts/check_delayed_reflection_contract.py) — deterministic authorization, state, privacy, idempotency, and crisis-stop checks for the delayed-reflection workflow.
- [`scripts/list_changed_skills.py`](scripts/list_changed_skills.py) — reviewer aid that lists changed skill entrypoints.
- [`examples/`](examples/) — public-safe examples for GitHub Reality Audit, bounded handoff, unsafe-claim review, architecture diagrams, TDD, and systematic debugging.
- [`tests/fixtures/unsafe-claims/`](tests/fixtures/unsafe-claims/) — PASS / FAIL fixtures for validation-claim discipline.
- [`tests/fixtures/delayed-reflection-loop/`](tests/fixtures/delayed-reflection-loop/) — deterministic workflow-contract fixtures for state and write gating.

## Why this exists

AI coding agents can reduce maintenance load, but unmanaged workflows often create new review risks:

- stale or oversized context;
- hidden assumptions about local files, shell state, credentials, or background work;
- false claims that tests, builds, or security checks ran;
- unsafe tool instructions;
- leaked local paths, private logs, private source, or secrets;
- handoffs that cannot be reproduced by another maintainer.

This repository turns those recurring risks into public, inspectable skill packages and operating rules.

## Core contract

Every skill in this repository follows these defaults:

- Web ChatGPT may reason from the conversation, uploaded files, GitHub connector data, and web search when available.
- A skill must not claim it ran commands, tests, local builds, local scripts, or background checks unless a tool call or command output actually produced that evidence.
- A skill must not request or store secrets, tokens, credentials, private keys, private source dumps, browser data, or private logs.
- If a task requires local edits, shell commands, build/test execution, local services, credentials, or multi-file repository changes beyond safe GitHub connector edits, the assistant should produce a bounded local-agent handoff.
- Human review remains required before production use of generated diagrams, tests, code plans, visual assets, security conclusions, and quality gates.

## Repository layout

```text
CATALOG.yaml                         Machine-readable skill registry
<skill>/SKILL.md                     Canonical self-contained skill package entrypoint
ROADMAP.md                           Staged OSS maintenance plan
docs/                                Reviewer evidence, threat model, release checklist, maintainer SOP
examples/                            Public-safe usage and review examples
scripts/                             Lightweight validation scripts
tests/fixtures/                      Regression and deterministic skill-contract fixtures
.github/workflows/                   CI validation
.github/PULL_REQUEST_TEMPLATE.md     PR safety and maintenance checklist
```

## Recommended invocation

```text
Use EthanSangSSS/web-chatgpt-skills.
First read CATALOG.yaml, choose the best matching skill, then read that SKILL.md.
Apply the skill's execution boundary, output contract, validation gate, and local-agent handoff rules.
Do not claim local execution or test pass without tool evidence.
```

## Available skills

### Software and architecture

- `architecture-diagram` — creates readable SVG, HTML, Mermaid, C4-style, deployment, data-flow, or trust-boundary diagrams.
- `systematic-debugging` — evidence-led debugging with symptom ledgers, competing hypotheses, discriminating tests, and handoff rules.
- `test-driven-development` — test design and RED-GREEN-REFACTOR with user-supplied test evidence.

### Product, planning, and project management

- `requirement-engineering` — turns ambiguity into testable requirements with explicit acceptance evidence.
- `kanban-orchestrator` — decomposes an outcome into dependency-aware work packages, validation gates, and local-agent handoff cards.
- `grill-me` — adversarially stress-tests plans, specs, tickets, handoffs, and decisions with ambiguity scoring before execution.
- `delayed-reflection-loop` — runs a privacy-first daily capture, delayed review, minimal-action loop, and sample-gated weekly or monthly synthesis.

### Spreadsheet and business operations

- `call-off-cost-breakdown-excel` — converts a structured price workbook into a visually faithful call-off and quotation template with three-level dependent dropdowns, formula-driven pricing, source-sheet preservation, and strict no-invention rules for absent fields.

### Research and perspective modeling

- `customer-research` — synthesizes interviews, feedback, reviews, and web evidence into decision-ready insight.
- `research-paper-writing` — plans and reviews technical research manuscripts without fabricating claims, results, or citations.
- `nuwa` — builds evidence-bounded perspective skills without deceptive impersonation.
- `truth-seeking` — evidence-constrained causal investigation, source policy, observation integrity, and adversarial validation fixtures.
- `rational-product-evaluation` — consumer purchase evaluation by fit, timing, evidence quality, alternatives, and TCO.

### Market data and quantitative research

- `unified-stock-data-web` — retrieves and normalizes current public-market evidence across A-shares, US equities, and Hong Kong equities within Web ChatGPT's verified tool boundary.
- `vibe-trading-web` — audits and plans Vibe-Trading workflows, reviews uploaded backtest artifacts, and produces bounded local-agent handoffs without pretending to run the local runtime.

### Visual and creative design

- `baoyu-article-illustrator` — plans article visuals and image prompts with accessibility and IP boundaries.
- `baoyu-comic` — creates educational comic storyboards with source boundaries and panel-level prompts.
- `baoyu-infographic` — creates evidence-aware infographic specifications with data-audit and misleading-chart checks.

### Writing, safety, and quality

- `content-polishing-workflow` — improves clarity, voice, structure, and evidence fidelity while preserving factual boundaries.
- `skill-vetter` — security-first review for skills and workflows, including permissions, red flags, and adoption verdicts.
- `industrial-self-audit-protocol` — evidence-based final quality gate using PASS / PASS_WITH_WARNINGS / INCONCLUSIVE / FAIL / BLOCKED.

## Validation

Run the public-review validators:

```bash
python3 scripts/validate_catalog.py
python3 scripts/check_public_safety.py
python3 scripts/check_unsafe_claims.py
python3 scripts/check_delayed_reflection_contract.py
python3 scripts/list_changed_skills.py
```

The validators check that:

- required public-review and maintenance-readiness files exist;
- `CATALOG.yaml` declares this repository;
- the unverified-execution evidence rule remains present;
- each catalog skill has a unique id and a canonical `<skill>/SKILL.md` path;
- deprecated package-layer paths are absent;
- referenced skill files are non-empty and look like readable Markdown skill files;
- credential, private-key, and token markers are absent from review-facing files;
- local-path and unsupported-claim patterns are surfaced as review warnings;
- unsafe execution and validation claim fixtures behave as expected;
- delayed-reflection authorization, state, privacy, idempotency, and safety fixtures behave as expected;
- changed skill entrypoints are listed for reviewer attention.

GitHub Actions runs the same checks on pushes to `main` and pull requests.

## OpenAI Codex for OSS fit

This is an early-stage public project. It should not be evaluated on unverified stars, downloads, or external adoption claims. Its application case is based on:

- ecosystem importance: reusable public rules for safer AI-agent maintenance;
- active maintenance evidence: catalog updates, PR checklist, governance files, validation scripts, CI workflow, maintainer runbook, roadmap, threat model, release checklist, prompt-security review, release notes, regression fixtures, and public-safe examples;
- Codex fit: PR review, issue triage, catalog validation, release-readiness checks, and skill safety review are exactly the type of recurring OSS maintainer work Codex can reduce.

See [`docs/CODEX_FOR_OSS_APPLICATION.md`](docs/CODEX_FOR_OSS_APPLICATION.md) for the application evidence packet and 500-character form drafts.

## Contributing

Contributions are welcome when they improve skill correctness, safety, validation, documentation, or reusability. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Security

Do not disclose secrets or private data in issues or pull requests. See [`SECURITY.md`](SECURITY.md), [`docs/SECURITY_THREAT_MODEL.md`](docs/SECURITY_THREAT_MODEL.md), and [`docs/PROMPT_SECURITY_REVIEW.md`](docs/PROMPT_SECURITY_REVIEW.md).

## License

MIT. See [`LICENSE`](LICENSE).
