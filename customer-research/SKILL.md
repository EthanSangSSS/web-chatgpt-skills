---
name: customer-research
version: "0.2.0"
status: stable
description: Turn interviews, feedback, reviews, support tickets, and web evidence into decision-ready customer insight with source labels and evidence strength.
triggers:
  - customer research
  - interviews
  - reviews
  - user feedback
  - JTBD
  - 用户研究
  - 客户反馈
  - 访谈
do_not_use_for:
  - inventing personas without evidence
  - treating anecdotes as market truth
  - regulated medical legal or financial advice
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Customer Research

## Purpose

Convert qualitative and public evidence into product decisions. Separate what customers actually said or did from inference, hypothesis, and strategy.

## Required input

Collect or infer:

- Decision question.
- Target audience and segment assumptions.
- Evidence available: interviews, surveys, reviews, support tickets, analytics summaries, competitor feedback, public web sources.
- Product stage: idea, MVP, launch, growth, retention, repositioning.
- Desired decision: build, cut, delay, test, position, interview more.

If the decision cannot be inferred, ask one high-impact clarification. Otherwise state assumptions and proceed.

## Web ChatGPT execution boundary

This skill may analyze provided material, uploaded files, GitHub connector content, and web search results. It must not claim survey representativeness, analytics access, user identity verification, or private customer knowledge without evidence.

Protect personal data. Remove or generalize names, emails, phone numbers, addresses, internal IDs, and sensitive health/financial/identity details unless strictly necessary and user-authorized.

## Evidence grading

Use this rubric:

- **Strong**: direct primary evidence from multiple relevant users or reliable quantitative source with clear denominator.
- **Moderate**: repeated pattern from credible but limited sample or strong public evidence with known bias.
- **Weak**: small sample, unclear segment, indirect signal, or single-source inference.
- **Anecdotal**: isolated quote/comment; useful for language, not market truth.

Never average incompatible segments. If segments disagree, preserve the disagreement.

## Workflow

1. Define decision question and audience.
2. Inventory sources with date, source type, sample, bias, and evidence strength.
3. Extract with source labels:
   - jobs to be done;
   - pains;
   - triggers;
   - objections;
   - alternatives;
   - desired outcomes;
   - customer language.
4. Separate direct evidence, inference, and hypothesis.
5. Identify segment differences and contradictions.
6. Translate findings into product, positioning, or research actions.

## Output contract

Return:

1. **Decision question**.
2. **Evidence inventory**: source, date, segment, sample/bias, strength.
3. **Top findings** ranked by decision impact and evidence strength.
4. **Customer-language table**: quote/paraphrase, source, segment, implication, confidence.
5. **JTBD / pain / trigger / objection map**.
6. **Segment differences and contradictions**.
7. **Evidence gaps**.
8. **Recommended next action**: build / cut / delay / test / interview more, with rationale.

## Validation gate

Before finalizing, verify:

- No invented quotes.
- Every core finding has a source label.
- Evidence strength is not inflated.
- Segment conflict is preserved.
- Personal data is minimized.
- Recommendation follows from evidence, not preference.

## Local-agent handoff trigger

Hand off only when the task requires processing large local datasets, scripts, private data cleaning, repository changes, or repeated analysis runs. The handoff must include data scope, privacy constraints, forbidden exports, validation checks, stop conditions, and final output format.
