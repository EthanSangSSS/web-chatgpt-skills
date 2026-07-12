# Web ChatGPT Skills

Single-file, Web ChatGPT-oriented skills. Every package is self-contained at:

```text
upload-packages/<skill>/SKILL.md
```

Use this repository as a **remote-readable skill registry** for Web ChatGPT. The canonical machine-readable entrypoint is:

```text
CATALOG.yaml
```

A Web ChatGPT run should first read `CATALOG.yaml`, select the most relevant skill, then read the selected `SKILL.md`. These packages are designed for conversations, uploaded material, GitHub connector data, and optional web search. They do **not** assume a local terminal, local filesystem, MCP server, credentials, or background agent.

## Remote execution contract

Every skill in this repository follows these defaults:

- ChatGPT may reason from the conversation, uploaded files, GitHub connector data, and web search when available.
- ChatGPT must not claim it ran commands, tests, local builds, local scripts, or background checks unless a tool call actually produced that evidence.
- ChatGPT must not request or store secrets, tokens, credentials, private keys, or private source dumps.
- If the task requires local edits, shell commands, build/test execution, local services, credentials, or multi-file repository changes beyond safe GitHub connector edits, ChatGPT must produce a bounded local-agent handoff instead of pretending to execute locally.
- Human review remains required before production use of generated diagrams, tests, code plans, visual assets, security conclusions, and quality gates.

## Recommended invocation

```text
Use EthanSangSSS/web-chatgpt-skills.
First read CATALOG.yaml, choose the best matching skill, then read that SKILL.md.
Apply the skill's execution boundary, output contract, validation gate, and local-agent handoff rules.
Do not claim local execution or test pass without tool evidence.
```

## Software and architecture

- `architecture-diagram` — creates readable SVG, HTML, Mermaid, C4-style, deployment, data-flow, or trust-boundary diagrams.
- `systematic-debugging` — evidence-led debugging with symptom ledgers, competing hypotheses, discriminating tests, and handoff rules.
- `test-driven-development` — test design and RED-GREEN-REFACTOR with user-supplied test evidence.

## Product and project management

- `requirement-engineering` — turns ambiguity into testable requirements with explicit acceptance evidence.
- `kanban-orchestrator` — decomposes an outcome into dependency-aware work packages, validation gates, and local-agent handoff cards.

## Research and perspective modeling

- `customer-research` — synthesizes interviews, feedback, reviews, and web evidence into decision-ready insight.
- `research-paper-writing` — plans and reviews technical research manuscripts without fabricating claims, results, or citations.
- `nuwa` — builds evidence-bounded perspective skills without deceptive impersonation.

## Visual and creative design

- `baoyu-article-illustrator` — plans article visuals and image prompts with accessibility and IP boundaries.
- `baoyu-comic` — creates educational comic storyboards with source boundaries and panel-level prompts.
- `baoyu-infographic` — creates evidence-aware infographic specifications with data-audit and misleading-chart checks.

## Writing, safety, and quality

- `content-polishing-workflow` — improves clarity, voice, structure, and evidence fidelity while preserving factual boundaries.
- `skill-vetter` — security-first review for skills and workflows, including permissions, red flags, and adoption verdicts.
- `industrial-self-audit-protocol` — evidence-based final quality gate using PASS / PASS_WITH_WARNINGS / INCONCLUSIVE / FAIL / BLOCKED.

## Repository status

These are portable adaptations of local workflows for Web ChatGPT. They intentionally favor explicit evidence, bounded assumptions, user-visible uncertainty, and safe escalation over autonomous execution.
