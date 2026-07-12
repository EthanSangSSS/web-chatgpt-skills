---
name: baoyu-comic
version: "0.2.0"
status: beta
description: Turn educational ideas, biographies, or tutorials into concise comic storyboards with source boundaries, panel-level prompts, and accessibility notes.
triggers:
  - comic
  - storyboard
  - educational comic
  - 漫画
  - 分镜
  - 知识漫画
do_not_use_for:
  - unverified historical claims
  - copyrighted character copying
  - deceptive impersonation
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Knowledge Comic

## Purpose

Convert a concept into a short visual narrative that teaches one idea at a time. The comic should improve comprehension, not just decorate content.

## Required input

Collect or infer:

- Learning objective.
- Target reader and knowledge level.
- Key misconception or tension.
- Desired emotional payoff.
- Length/platform constraints.
- Source material for factual or biographical claims.

If factual claims are central and sources are missing, ask for sources or mark the output as fictionalized/provisional.

## Web ChatGPT execution boundary

This skill may create storyboards and image prompts from conversation, uploaded files, GitHub connector content, and web evidence. It must not claim to generate final images unless an image tool actually runs. It must not claim historical accuracy without source evidence.

## IP and factual boundaries

- Do not copy copyrighted characters, distinctive franchises, or living artists' styles.
- For biographies/history, separate documented facts, interpretation, and dramatized scenes.
- Avoid putting dense text inside generated panels.
- Do not impersonate real living people or fabricate quotes.

## Workflow

1. Define learning objective, reader, misconception, and emotional payoff.
2. Reduce the topic to a narrative arc:
   - hook;
   - tension;
   - explanation;
   - example;
   - resolution.
3. Create a character and visual bible.
4. Build a panel-by-panel storyboard with:
   - panel goal;
   - visual action;
   - dialogue/narration;
   - transition;
   - prompt notes;
   - alt text.
5. Keep each panel focused on one concept.

## Output contract

Return:

- **Premise and learning objective**.
- **Reader assumptions**.
- **Narrative arc**.
- **Character and visual bible**.
- **Panel storyboard table**.
- **Image prompts**.
- **Alt text and accessibility notes**.
- **Factual/source caveats**.

## Validation gate

Before finalizing, verify:

- Every panel earns its place.
- Text per panel is short.
- One concept is taught at a time.
- Factual claims are sourced or labeled provisional/fictionalized.
- No copyrighted character copying or deceptive impersonation.

## Local-agent handoff trigger

Hand off when final image generation, layout export, asset insertion, or repository updates are required. The handoff must include panel count, visual bible, file scope, source constraints, validation checks, stop conditions, and final output format.
