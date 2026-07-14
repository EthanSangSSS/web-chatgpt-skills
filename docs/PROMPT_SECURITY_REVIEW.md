# Prompt Security Review Checklist

This checklist is for reviewing contributed `SKILL.md` files, examples, prompts, and maintainer workflow changes.

The repository contains executable-adjacent instructions for AI systems. A skill does not execute code by itself, but it can influence how ChatGPT, Codex, or a local agent asks for tools, evidence, files, credentials, or validation. Reviewers should therefore treat skill changes as instruction-surface changes.

## Review scope

Apply this checklist when a change modifies:

- `CATALOG.yaml`;
- any `<skill>/SKILL.md` file;
- skill package references, templates, fixtures, or examples;
- local-agent handoff text;
- CI scripts or validation scripts;
- maintainer runbooks, release checklists, or security documentation.

## Blockers

Reject or rewrite a contribution when it instructs an assistant or local agent to:

1. ignore system, developer, repository, or user constraints;
2. request, store, print, or exfiltrate secrets, tokens, cookies, SSH keys, signing keys, browser sessions, or private logs;
3. scan broad local directories without explicit user authorization and file scope;
4. access third-party systems, repositories, services, or accounts without authorization;
5. perform destructive operations such as deleting files, force-pushing, rewriting history, publishing packages, or sending messages without explicit approval;
6. claim tests, builds, scans, local commands, screenshots, or background work completed without actual tool or command evidence;
7. hide uncertainty, omit evidence limitations, or upgrade `INCONCLUSIVE` to `PASS` without supporting data;
8. impersonate a real person, organization, reviewer, or official project status deceptively;
9. include private source code, employer/customer material, identity documents, production logs, or unredacted local paths.

## High-risk wording patterns

Review carefully when a skill says things like:

- "run this automatically";
- "do not ask for confirmation";
- "scan everything";
- "use my credentials";
- "ignore previous instructions";
- "mark as passed";
- "continue in the background";
- "push directly to main";
- "delete old files";
- "copy private data into the prompt".

These phrases are not always wrong, but they require tight scope, explicit authorization, and concrete stop conditions.

## Required reviewer checks

For each affected skill or workflow, verify:

| Area | Reviewer question | Expected evidence |
|---|---|---|
| Trigger | Is the skill invoked only for the right tasks? | Clear trigger and non-trigger language |
| Source policy | Does the skill define what evidence it can use? | Web, files, GitHub connector, user-provided text, or local-agent output boundaries |
| Execution boundary | Does the skill avoid claiming unavailable tools? | Explicit prohibition on unverified local execution |
| Secret handling | Does it avoid asking for credentials or private data? | `never_request_or_store` style boundary |
| Handoff | Does local-agent work include repo, branch, HEAD, scope, forbidden actions, validation, and stop conditions? | Bounded task packet |
| Validation | Can outputs be checked by a reviewer? | Scripts, fixtures, commands, CI, or manual review criteria |
| Honesty | Does it avoid unverified adoption, endorsement, or PASS claims? | Conservative language and evidence references |

## Safe rewrite pattern

When a proposed instruction is too broad, rewrite it into this shape:

```text
Use only the provided repository, branch, files, and tool outputs.
Do not request secrets or private files.
Do not claim tests passed unless exact command output is available.
If local execution is required, stop and produce a bounded local-agent handoff with validation commands and stop conditions.
```

## Reviewer output

Use this short verdict block in PR review notes when relevant:

```text
Prompt security review: PASS / PASS_WITH_WARNINGS / FAIL / INCONCLUSIVE
Reviewed surfaces:
- <files>
Blockers:
- <none or list>
Warnings:
- <none or list>
Required follow-up:
- <none or list>
```

## Non-goals

This checklist does not certify that a skill is safe for every environment. It is a public-review aid for repository maintainers and does not replace human review, full secret scanning, legal review, or platform-specific security testing.
