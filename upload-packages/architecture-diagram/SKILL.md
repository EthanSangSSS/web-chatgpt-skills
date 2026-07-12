---
name: architecture-diagram
version: "0.2.0"
status: stable
description: Produce readable, evidence-bounded architecture diagrams as SVG, single-file HTML, Mermaid, or structured diagram specifications for Web ChatGPT execution.
triggers:
  - architecture diagram
  - system diagram
  - C4 diagram
  - deployment diagram
  - data flow
  - trust boundary
  - 架构图
  - 系统图
do_not_use_for:
  - decorative illustration
  - pure UI mockup
  - product purchase decision
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Architecture Diagram

## Purpose

Create diagrams that answer an architectural question, not decorative drawings. Optimize for correctness, readability, trust-boundary visibility, and remote reproducibility in Web ChatGPT.

## Required input

Collect or infer:

- Diagram purpose and audience.
- Components, systems, actors, data stores, external services, and deployment environment.
- Data flows, control flows, authentication/authorization paths, and trust boundaries.
- Known risks, unclear integrations, and whether the output should be SVG/HTML/Mermaid/spec.

If a missing detail changes the architecture materially, ask one high-impact question. If not, state assumptions and proceed.

## Web ChatGPT execution boundary

This skill may use conversation context, uploaded files, GitHub connector data, and web search when available. It must not claim to inspect local runtime, execute code, render locally, or validate browser output unless an actual tool result proves it.

If final rendering requires local assets, build tools, repository integration, screenshots, or multi-file updates, produce a local-agent handoff instead of pretending to complete local work.

## Diagram selection

Choose the lowest-complexity diagram that answers the question:

- C4 Context: actors, external systems, product boundary.
- C4 Container: apps, APIs, databases, queues, jobs, devices.
- Component: modules and internal responsibilities.
- Sequence: request/response, async flows, failure path.
- Deployment: environments, regions, runtimes, network zones.
- Data-flow / threat-boundary: sensitive data, trust zones, auth, storage.
- Roadmap / migration: current state, transition state, target state.

Avoid one mega-diagram when two focused diagrams are clearer.

## Design rules

- Group components by boundary, layer, ownership, or runtime.
- Label every component with its purpose.
- Label every arrow with direction and payload/action.
- Make trust boundaries, external systems, and failure-critical paths explicit.
- Use consistent shapes and a concise legend.
- Mark unknown integrations as `unknown` or `assumption`; do not invent them.
- Prefer left-to-right or top-to-bottom flow and minimize crossings.
- For security-relevant diagrams, show auth boundary, data classification, secrets path, and external ingress/egress.

## Output contract

Return:

1. **Diagram choice** — selected diagram type and why.
2. **Assumptions and unknowns** — bounded, explicit, and revisable.
3. **Diagram artifact** — one of:
   - self-contained SVG in one code block;
   - single-file HTML in one code block;
   - Mermaid when editable text is preferred;
   - structured production spec when rendering is not appropriate.
4. **Legend** — shape/color/line meaning.
5. **Validation checklist** — component coverage, arrow direction, boundary visibility, and unknowns.

## Validation gate

Before final answer, verify:

- Every named component has a purpose.
- Every arrow has a direction and meaning.
- Each external dependency is outside the system boundary.
- Sensitive data and trust boundaries are visible when relevant.
- The diagram answers the user's stated question.

## Local-agent handoff trigger

Escalate to local Codex / Claude Code when the task requires repository file edits, generated assets, browser screenshot verification, build integration, or multiple diagram files. The handoff must include repo, branch, file scope, target diagram format, validation command or manual check, forbidden actions, stop conditions, and final output format.
