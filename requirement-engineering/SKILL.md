---
name: requirement-engineering
version: "0.2.0"
status: stable
description: Turn ambiguous requests into bounded, testable specifications with acceptance evidence and explicit non-goals.
triggers:
  - requirements
  - PRD
  - spec
  - acceptance criteria
  - 需求
  - 需求分析
  - 产品规格
  - 验收标准
do_not_use_for:
  - implementation when requirements are already clear
  - certifying completed work
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Requirement Engineering

## Purpose

Convert ambiguity into a specification that can be implemented, tested, reviewed, and handed off. Prefer observable acceptance evidence over adjectives such as fast, simple, robust, safe, or polished.

## Required input

Clarify or infer:

- User, problem, and decision context.
- Desired outcome and failure condition.
- In scope and out of scope.
- Functional and non-functional requirements.
- Constraints: time, platform, privacy, security, accessibility, budget, dependencies.
- Acceptance evidence and review owner.

## Clarification policy

Ask one high-impact question only when a missing answer changes the required output materially. If the ambiguity is manageable, state assumptions and proceed. If the user asks for a local-agent/Codex handoff, do not block on minor ambiguity; include assumptions and stop conditions in the handoff.

## Web ChatGPT execution boundary

This skill may reason from conversation context, uploaded files, GitHub connector data, and web search. It must not claim local repo inspection, implementation, validation, or stakeholder confirmation unless tool or user evidence proves it.

## Workflow

1. Reframe the request as a decision or delivery problem.
2. Identify stakeholders and user outcome.
3. Split requirements into:
   - functional requirements;
   - non-functional requirements;
   - constraints;
   - explicit non-goals.
4. Convert vague adjectives into measurable acceptance criteria.
5. Add edge cases, failure modes, privacy/security/accessibility requirements, and dependencies.
6. Produce a mini-spec and mark unresolved questions.

## Output contract

Return:

- **Goal and user outcome**.
- **Scope**: in / out.
- **Assumptions** and their risk level.
- **Functional requirements**.
- **Non-functional requirements**.
- **User flows / system flows**.
- **Edge cases and failure modes**.
- **Acceptance criteria** with evidence source.
- **Dependencies and open questions**.
- **Implementation handoff** when requested.

## Validation gate

Before finalizing, verify:

- Every requirement is observable or testable.
- Non-goals prevent scope creep.
- Acceptance criteria are not merely restated requirements.
- Privacy, security, accessibility, and rollback are considered where relevant.
- Assumptions are labeled, not smuggled in as facts.

## Local-agent handoff trigger

Hand off when the specification must be implemented, repo state must be inspected, code/files must be changed, validation commands must run, or multiple work packages must be generated. The handoff must include repo, branch, file scope, forbidden actions, validation commands, stop conditions, and final output format.
