# Security Policy

`web-chatgpt-skills` is a public repository for reusable AI-agent skills, prompts, templates, and validation boundaries. Its main security risks are prompt-instruction abuse, secret leakage, unsafe automation instructions, and unsupported claims about execution.

## Supported scope

Security reports are in scope when they involve:

- secret, credential, token, private-key, or private-data exposure;
- prompt or skill instructions that encourage unsafe tool use;
- instructions that bypass explicit user authorization;
- workflows that could delete, overwrite, publish, scan, or exfiltrate data unexpectedly;
- false local-execution claims or false validation claims;
- public packages that accidentally include private source, local paths, employer/customer material, or sensitive runtime logs.

Out of scope:

- requests for private credentials or private repository access;
- reports requiring access to systems not owned or administered by the maintainer;
- speculative issues without a concrete file path, behavior, or reproduction path;
- attempts to use this repository to scan third-party systems without authorization.

## Reporting

Open a GitHub issue if the report contains no sensitive data. If sensitive data is involved, do not paste it into the issue. Instead, open a minimal issue stating that a sensitive security report exists and include only:

- affected path or package name;
- risk category;
- safe reproduction outline;
- whether any secret or private data was exposed.

The maintainer will request a safe redacted artifact if needed.

## Maintainer handling SOP

1. Confirm the affected path and classify the risk.
2. Preserve evidence without copying secrets into durable public docs.
3. Remove or rewrite unsafe content.
4. Add or update a regression check where feasible.
5. Document the fix without exposing sensitive details.

## Codex Security / API-credit boundary

Codex Security or API credits, if granted, must only be used on repositories and code that the maintainer owns, maintains, or is explicitly authorized to review. Do not use project benefits to probe third-party repositories, services, or systems without permission.
