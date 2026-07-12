---
name: content-polishing-workflow
version: "0.2.0"
status: stable
description: Multi-pass editing for clearer, more human, evidence-faithful writing while preserving factual meaning, confidence level, and user intent.
triggers:
  - polish
  - rewrite
  - edit
  - resume
  - interview material
  - 润色
  - 改写
  - 求职材料
do_not_use_for:
  - inventing credentials
  - fabricating citations
  - changing factual claims without evidence
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Content Polishing Workflow

## Purpose

Improve clarity, structure, tone, and precision without fabricating facts, anecdotes, credentials, citations, or personal experience.

## Required input

Collect or infer:

- Audience and purpose.
- Desired tone and length.
- Surface: email, resume/interview material, technical document, proposal, social post, legal/business draft, article.
- Must-preserve facts, phrases, examples, and constraints.
- Whether voice matching is required; if yes, ask for a representative sample when material.

If the user asks for a direct rewrite and missing context is not blocking, state assumptions and produce a polished version.

## Web ChatGPT execution boundary

This skill may rewrite or edit text in the conversation, uploaded files, GitHub connector content, and web-sourced context when cited. It must not verify external facts without sources, claim stakeholder approval, or invent personal history.

## Editing modes

Select one or combine:

- **professional-email**: concise, specific, action-oriented.
- **resume-interview**: factual, evidence-backed, STAR-aware, no credential inflation.
- **technical-doc**: precise terminology, clear structure, explicit assumptions.
- **legal-business-draft**: risk-aware wording, no legal-advice overclaim.
- **public-article**: coherent thesis, readable flow, source fidelity.
- **chat-message**: natural, brief, intent-preserving.

## Passes

1. Diagnose unclear logic, repetition, generic claims, tone drift, and unsupported assertions.
2. Structure thesis, sequencing, headings, transitions, and paragraph purpose.
3. Voice: replace stock phrasing with concrete language while preserving meaning and confidence level.
4. Precision: distinguish fact, inference, recommendation, and uncertainty.
5. Final QA: consistency, terminology, length, formatting, duplication, and accidental factual drift.

## Output contract

Return:

- **Polished version first**.
- **Material edits**: only changes that affect meaning, structure, evidence, or tone.
- **Unresolved factual gaps**.
- **Optional alternatives** when tone/length choices are material.

When delivering a finished reusable message, email, post, or document, put the finished text in the host's required artifact/writing-block format if applicable.

## Validation gate

Before finalizing, verify:

- Meaning and factual claims are preserved unless explicitly changed.
- No invented anecdotes, citations, credentials, results, or personal experience.
- Confidence level is not inflated.
- Tone matches audience and surface.
- User's must-preserve content remains intact.

## Local-agent handoff trigger

Hand off when editing requires batch file changes, repository updates, document export, formatting validation, or review across many files. Include file scope, preservation rules, forbidden changes, validation checks, stop conditions, and final output format.
