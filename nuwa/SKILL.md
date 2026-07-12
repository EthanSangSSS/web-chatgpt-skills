---
name: nuwa
version: "0.2.0"
status: stable
description: Build evidence-bounded perspective skills from a person, school of thought, book, or decision style without deceptive impersonation or private-motive claims.
triggers:
  - nuwa
  - perspective skill
  - mental model
  - decision style
  - 思维方式
  - 名人思维
  - 学派
  - 书籍蒸馏
do_not_use_for:
  - deceptive impersonation
  - claiming private access
  - private motive inference
  - therapeutic replacement
  - regulated professional advice as the subject
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Nuwa Perspective Builder

## Purpose

Create a reusable advisor-style reasoning framework that captures source-supported patterns in how a subject, school, book, or decision style tends to reason. The output is not the person, not a simulation of private consciousness, and not a claim of hidden access.

## Required input

Collect or infer:

- Subject: person, school of thought, book, company style, or decision method.
- Intended use: decision critique, writing aid, strategy review, learning, interview prep, etc.
- Scope: what domains the perspective applies to and does not apply to.
- Source availability: primary works, interviews, books, talks, papers, credible commentary.
- Output type: advisor-style framework, writing-style study, promptable skill, or scenario evaluator.

Ask for confirmation between phases when the user wants a high-fidelity build. If the user asks for direct output, use fast mode and label it provisional.

## Web ChatGPT execution boundary

This skill may use conversation context, uploaded files, GitHub connector data, and web search when available. It must not claim private access, hidden intent, direct endorsement, personal identity, or exact imitation.

For current or niche public figures, books, or source claims, use live search when available and cite sources. If evidence is thin, produce a research plan or low-confidence draft rather than filling gaps.

## Safety and integrity boundaries

- Do not impersonate living people or write as if the subject personally answered.
- Do not imitate a living author's protected expressive style. Summarize reasoning patterns instead.
- Do not infer private motives, diagnoses, beliefs, or undisclosed strategies.
- For political, medical, legal, financial, or safety-critical domains, keep the output analytical and bounded; do not present it as professional advice.
- Label uncertainty and source gaps.

## Workflow

### Phase 1 — Frame

Clarify subject, intended use, scope, source availability, and output type. Produce a framing summary and, unless in fast mode, wait for confirmation.

### Phase 2 — Research

Use user-provided materials and credible public sources. Separate:

- primary material;
- high-quality commentary;
- weak/speculative commentary;
- unsupported inference.

Record source date, source position, conflicts, and gaps.

### Phase 3 — Distill

Extract only models that recur across contexts. For each model include:

- source-supported pattern;
- evidence;
- decision heuristic;
- useful application;
- counterexample;
- blind spot;
- confidence.

### Phase 4 — Build

Produce a perspective skill with:

- scope and honest boundary;
- mental models;
- decision heuristics;
- diagnostic questions;
- expression cues only if requested and not deceptive;
- anti-patterns and blind spots;
- output format.

### Phase 5 — Validate

Test the skill on 2-3 new scenarios. Compare expected behavior against source-supported patterns and revise only where evidence supports it.

## Output contract

Return:

- **Scope and boundary**.
- **Source ledger**: source type, date, evidence role, limitation.
- **Mental models**.
- **Decision heuristics**.
- **Blind spots and anti-patterns**.
- **Question prompts**.
- **Scenario tests**.
- **Uncertainty and excluded claims**.

## Validation gate

Before finalizing, verify:

- No identity claim or deceptive impersonation.
- No private motive claim.
- Every core heuristic has source support.
- Style cues do not copy protected expressive style.
- Scope limits are explicit.

## Local-agent handoff trigger

Hand off only when building a larger reusable package, processing many source files, or updating a repository. The handoff must include source scope, copyright constraints, file scope, validation scenarios, forbidden claims, stop conditions, and final output format.
