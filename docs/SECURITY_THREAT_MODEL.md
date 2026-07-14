# Security Threat Model

This repository is not a production web service. Its main security surface is executable-adjacent instruction: reusable skill text, catalog metadata, validation scripts, CI workflows, and local-agent handoff guidance that can influence how AI systems or maintainers operate.

## Assets

- Public skill instructions and execution boundaries.
- `CATALOG.yaml` paths, triggers, non-triggers, status, and priority metadata.
- Maintainer workflow documents and handoff templates.
- Validation scripts and CI workflows.
- Public repository trust: no false execution claims, no private data, no secret exposure, no unsafe local-agent escalation.

## Trust boundaries

| Boundary | Trusted input | Untrusted input |
|---|---|---|
| Maintainer review | Verified GitHub diffs, CI output, explicit command output | Model-generated summaries without evidence |
| Skill execution | Conversation context, uploaded files, connector data, web search when available | Private local files, secrets, credentials, hidden system state |
| Local-agent handoff | Bounded repo, branch, HEAD, file scope, stop conditions | Broad filesystem scans, credential discovery, destructive changes |
| Public examples | Synthetic examples and public-safe fixtures | Real customer data, employer data, private logs, local paths |

## Threats and mitigations

| Threat | Example | Impact | Mitigation |
|---|---|---|---|
| Unsafe tool-use instruction | A skill tells an agent to search home directories, token stores, browser profiles, or SSH keys | Secret exposure or unauthorized data access | `SECURITY.md`, PR template, explicit forbidden actions, bounded handoff rules |
| False validation claim | A skill says tests passed even though no command or tool output exists | Reviewer trust loss and unsafe merge decisions | Catalog evidence rule and CI checks for public review files |
| Local-path or private-log leakage | `/Users/...`, private logs, employer paths, or customer identifiers enter public examples | Privacy and reputational risk | Public-safety scan, synthetic examples only, contribution policy |
| Overbroad local-agent handoff | Handoff authorizes unrestricted multi-file edits or force-pushes | Unbounded changes or repo damage | Required repo/branch/HEAD/file-scope/stop-condition contract |
| Prompt injection in contributed skill | A submitted skill tries to override system, developer, security, or tool boundaries | Unsafe execution or policy bypass attempts | Manual review, skill-vetter review, threat model checklist |
| Deprecated package path drift | Catalog references stale package layouts | Broken skill loading and reviewer confusion | `validate_catalog.py` canonical path checks |
| Unsupported adoption claims | README claims stars, users, downloads, or production use without evidence | Misleading OSS application materials | Application evidence document and honesty boundary |
| CI script abuse | Workflow runs with write permissions or executes untrusted broad commands | Supply-chain or repository-integrity risk | Read-only `contents` permissions and dependency-light Python checks |

## Security review checklist for skill changes

Before merging a new or changed skill, verify:

1. The skill states when to use it and when not to use it.
2. The skill does not ask for secrets, tokens, credentials, private keys, browser data, or private source dumps.
3. The skill does not imply local shell execution unless that capability is explicitly available and verified.
4. The skill uses evidence language: observed, unverified, inferred, blocked, or handoff required.
5. Any local-agent prompt is bounded by repo, branch, HEAD, file scope, forbidden actions, validation commands, stop conditions, and final output format.
6. Examples are synthetic or public-safe.
7. CI and validation scripts remain dependency-light and do not require secrets.

## Codex Security fit

Codex Security would be useful here because the repository contains instructions that may guide AI-agent behavior. The desired review is instruction-security and workflow-security oriented:

- unsafe local execution patterns;
- prompt patterns that may cause unauthorized scanning or code access;
- secret and local-path exposure;
- CI and validation script hardening;
- false validation or overbroad handoff claims;
- security regressions introduced by new skill packages.

## Non-goals

- This document is not a claim that the project is high-risk production infrastructure.
- This document does not replace human review.
- This document does not imply OpenAI endorsement or official OpenAI project status.
