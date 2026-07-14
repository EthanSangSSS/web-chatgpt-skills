# Contributing

Thank you for helping improve `web-chatgpt-skills`.

This repository is a public skill registry and package collection for Web ChatGPT, Codex, and local-agent workflows. Contributions should improve reusable, evidence-bounded AI-agent behavior rather than encode private local context.

## Contribution priorities

High-value contributions include:

1. New or improved skills with clear triggers, boundaries, output contracts, and validation gates.
2. Safer execution rules for ChatGPT, Codex, or local agents.
3. Regression fixtures that prevent unsafe claims, secret leakage, or unsupported local-execution claims.
4. Documentation that helps maintainers review pull requests, triage issues, and package releases.
5. Compatibility improvements for remote-readable skill usage.

## Required boundaries

Do not include:

- secrets, tokens, credentials, private keys, provisioning profiles, or browser/session data;
- private source code or proprietary customer / employer material;
- personal identity documents, production logs, or unredacted local paths;
- instructions that ask an AI system to claim it ran commands, tests, builds, or checks unless tool evidence exists;
- destructive automation that can delete, overwrite, publish, scan, or exfiltrate user data without explicit authorization.

## Skill quality checklist

A skill package should define:

- intended trigger cases and non-trigger cases;
- allowed inputs and source policy;
- execution boundaries for Web ChatGPT, Codex, local agents, and connectors;
- output contract;
- validation or review gates;
- safe escalation path when local files, credentials, shell commands, or multi-file repository edits are required.

## Pull request process

1. Keep the scope narrow and explain the maintenance problem being solved.
2. Update `CATALOG.yaml` when adding, renaming, moving, or changing the status of a skill.
3. Run `python3 scripts/validate_catalog.py` when available.
4. Use the pull request template and state exactly what was validated.
5. Do not mark a result as `PASS` unless it is backed by actual tool output, command output, or direct repository inspection.

## Issue triage

Issues should include:

- the skill or file path involved;
- the observed failure or requested improvement;
- expected behavior;
- evidence, logs, screenshots, or concrete examples when available;
- whether the issue requires local execution or can be handled from GitHub / uploaded files / web evidence.

## Maintainer response policy

Maintainers may close issues that require private credentials, private data exposure, unsupported impersonation, unsafe automation, or unverifiable claims. Safe alternatives or bounded local-agent handoffs should be provided when possible.
