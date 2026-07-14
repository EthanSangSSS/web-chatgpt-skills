# Codex for Open Source Application Evidence

This document is a reviewer-facing evidence packet for the OpenAI Codex for Open Source program. It is intentionally factual and conservative: it does not claim stars, downloads, or external adoption that have not been verified.

## Repository

- Repository: `EthanSangSSS/web-chatgpt-skills`
- Visibility: public
- Maintainer role: primary maintainer / repository owner
- License: MIT
- Primary entrypoint: `CATALOG.yaml`
- Runtime surfaces: Web ChatGPT, GitHub connector, uploaded files, optional web search, Codex / local-agent handoff workflows

## Why this project matters

`web-chatgpt-skills` provides a public, remote-readable registry of reusable skill packages for AI-assisted software work. Its main purpose is to make ChatGPT, Codex, and local-agent workflows safer and more repeatable by packaging:

- explicit trigger and non-trigger rules;
- execution boundaries for web-only, connector-backed, Codex, and local-agent surfaces;
- evidence rules that prevent false claims about local execution or test results;
- reusable handoff contracts for work that requires shell commands, credentials, local files, or multi-file edits;
- validation gates for debugging, TDD, architecture diagrams, adversarial review, truth-seeking, product evaluation, and release-quality audits.

The ecosystem problem is practical: AI coding agents can be effective, but unmanaged workflows often drift into stale context, unsafe assumptions, missing validation evidence, secret exposure, or unreviewable handoffs. This repository turns those recurring risks into public, inspectable, reusable operating rules.

## Current adoption status

This is an early-stage public project. The current application should be evaluated primarily on ecosystem importance, active maintenance evidence, and suitability for Codex-assisted maintainer workflows, not on unverified usage metrics.

Current status:

- Star / download metrics: not claimed.
- External production adoption: not claimed.
- Maintainer activity: active repository updates, pull request review process, skill catalog maintenance, governance files, and validation automation.
- Ecosystem relevance: public AI-agent workflow safety, reusable skill packaging, review discipline, and remote-readable execution contracts.

## Active maintenance evidence

The repository includes:

- machine-readable registry: `CATALOG.yaml`;
- public README with skill list and invocation contract;
- contribution rules: `CONTRIBUTING.md`;
- security reporting and handling policy: `SECURITY.md`;
- pull request review template: `.github/PULL_REQUEST_TEMPLATE.md`;
- catalog validation script: `scripts/validate_catalog.py`;
- GitHub Actions validation workflow: `.github/workflows/catalog-check.yml`;
- maintainer runbook: `docs/MAINTAINER_RUNBOOK.md`.

Maintenance duties include:

1. Reviewing skill changes for unsafe execution claims.
2. Keeping `CATALOG.yaml` aligned with package paths and skill status.
3. Preventing secrets, local paths, or private source material from entering public packages.
4. Maintaining output contracts and validation gates for reusable skills.
5. Producing safe local-agent handoffs when web-only execution is insufficient.

## Best-fit Codex use cases

If selected, Codex and API credits would be used for OSS maintainer work only:

- pull request review assistance for skill and catalog changes;
- automated validation of catalog path integrity and skill metadata;
- regression checks for unsafe local-execution claims;
- release-readiness summaries for new skill packages;
- security review of public skill instructions and CI scripts;
- issue triage and bounded repair plans;
- documentation consistency checks across README, CATALOG, and skill packages.

## Codex Security fit

Codex Security would be useful for this repository because the main risk is not a traditional app vulnerability alone. The repository contains executable-adjacent instructions for AI systems. Useful checks include:

- prompt-instruction patterns that could cause unsafe tool use;
- workflows that imply unauthorized scanning, credential access, destructive file operations, or false validation claims;
- accidental inclusion of secrets, private logs, or local paths;
- CI and validation script hardening.

## Application form draft

### Why does this repository qualify? 500 characters max

```text
web-chatgpt-skills is a public MIT skill registry for ChatGPT, Codex, and local-agent workflows. It packages reusable skills for debugging, TDD, architecture diagrams, adversarial review, truth-seeking, and release-quality audits. Its ecosystem value is safer AI-agent maintenance: explicit execution boundaries, no false local-test claims, no secret exposure, and bounded handoffs when local work is required.
```

### How would API credits be used? 500 characters max

```text
I would use API credits for OSS maintainer workflows: PR review assistance, catalog validation, unsafe-claim regression checks, release-readiness summaries, security review of skill instructions, and issue triage. The goal is to make public ChatGPT/Codex skill packages safer, easier to review, and reusable without relying on private local context or unverifiable execution claims.
```

### Additional notes 500 characters max

```text
The project is early-stage, so I am not claiming stars or download volume. The application is based on ecosystem importance and active maintenance evidence: a public remote-readable registry, MIT license, contribution/security policies, validation automation, and a maintainer runbook for evidence-bounded AI-agent workflows.
```

## Non-goals and honesty boundary

This repository does not claim to be an official OpenAI project, does not grant access to private ChatGPT or Codex features, and does not replace human review. Program benefits, if granted, would be used only for repositories and code the maintainer owns, maintains, or is authorized to review.
