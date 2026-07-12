---
name: research-paper-writing
version: "0.2.0"
status: beta
description: Plan, draft, and review rigorous technical manuscripts with claim-evidence ledgers, novelty boundaries, reproducibility checks, and no fabricated results or citations.
triggers:
  - paper
  - manuscript
  - abstract
  - related work
  - reviewer simulation
  - 论文
  - 技术白皮书
do_not_use_for:
  - fabricating results
  - inventing citations
  - overstating incomplete experiments
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Research Paper Writing

## Purpose

Help plan, draft, revise, or review a technical paper from evidence. The goal is a defensible argument, not persuasive overclaiming.

## Required input

Collect or infer:

- Venue or target audience.
- Central claim and intended contribution.
- Available evidence: experiments, ablations, baselines, datasets, proofs, user studies, citations.
- Novelty boundary: what is new, borrowed, reproduced, or speculative.
- Reproducibility status: code/data/config availability, seeds, environment, limitations.
- Desired output: outline, section draft, reviewer critique, related work map, checklist.

Ask one clarification only if the target venue, central claim, or available evidence is materially unclear.

## Web ChatGPT execution boundary

This skill may analyze provided text, uploaded material, GitHub connector data, and web search results. It must not claim to run experiments, reproduce results, inspect private datasets, or verify citations unless a tool result or supplied evidence proves it.

For current literature, use live search when available and cite sources. Do not invent papers, DOIs, authors, benchmark scores, or author contributions.

## Workflow

1. State one falsifiable contribution claim.
2. Build a claim-evidence ledger:
   - claim;
   - required evidence;
   - available evidence;
   - missing evidence;
   - confidence;
   - where it appears in the paper.
3. Build the argument: problem, gap, method, evidence, limitations, and implications.
4. Check novelty boundary and baselines.
5. Review reproducibility and ethics/limitations.
6. Draft or revise sections with calibrated language.
7. Run reviewer simulation: novelty, correctness, baselines, clarity, reproducibility, limitations, ethics.

## Output contract

Return the relevant subset:

- **Paper objective and venue assumptions**.
- **Central contribution claim**.
- **Claim-evidence ledger**.
- **Outline or revised section**.
- **Related work / baseline gaps**.
- **Reviewer simulation**.
- **Reproducibility checklist**.
- **Unsupported claims to remove or qualify**.

## Validation gate

Before finalizing, verify:

- Every major claim has evidence or is labeled incomplete/speculative.
- Abstract and conclusion do not exceed available evidence.
- Baselines and comparisons are fair and current enough for the venue.
- Limitations are concrete.
- Citations are not fabricated.

## Local-agent handoff trigger

Hand off when experiments, scripts, data processing, LaTeX builds, citation database edits, or repository changes are needed. The handoff must include repo/path, file scope, commands, data privacy constraints, forbidden actions, stop conditions, and final output format.
