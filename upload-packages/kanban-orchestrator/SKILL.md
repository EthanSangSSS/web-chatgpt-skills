---
name: kanban-orchestrator
version: "0.2.0"
status: stable
description: Decompose outcomes into bounded, dependency-aware work packages with validation evidence, review gates, and local-agent handoff contracts.
triggers:
  - kanban
  - work packages
  - roadmap
  - execution plan
  - Codex handoff
  - local agent
  - 看板
  - 任务拆解
  - 本地 agent
do_not_use_for:
  - simple one-step tasks
  - unbounded brainstorming
  - unverifiable status reporting
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Kanban Orchestrator

## Purpose

Turn an outcome into small, independently verifiable work packages. This skill is optimized for Web ChatGPT supervising remote/GitHub work and handing bounded execution to local agents when needed.

## Required input

Collect or infer:

- Outcome and deadline.
- Constraints and must-not-do items.
- Available evidence and current state.
- Dependencies, irreversible actions, and review gates.
- Repo/branch/PR metadata if this is a software task.
- Validation evidence required for done.

If a missing input changes sequencing materially, ask one high-impact question. Otherwise state assumptions and proceed.

## Web ChatGPT execution boundary

This skill may decompose work and review evidence from conversation, uploaded files, GitHub connector data, and web search. It must not claim that tasks are done, tests passed, branches synced, or files changed unless there is tool or user evidence.

## Workflow

1. Define the outcome, scope, constraints, and acceptance evidence.
2. Identify dependency graph and high-risk irreversible actions.
3. Split work into small packages with a single clear deliverable.
4. Assign validation to each package.
5. Sequence work to reduce blocked time and preserve rollback options.
6. Add review gates and stop conditions.
7. Review package status only from actual evidence.

## Board format

| ID | Work package | Depends on | Deliverable | Validation evidence | Risk | Owner | Status |
|---|---|---|---|---|---|---|---|

Status must be one of: `not_started`, `ready`, `blocked`, `in_progress`, `review_needed`, `done_evidence_attached`, `inconclusive`.

## Local-agent package format

For each local-agent package, include:

- Repository and local path if known.
- Branch and PR number if applicable.
- Version sync gate:
  - `git fetch origin`;
  - confirm current branch;
  - confirm worktree clean;
  - confirm local HEAD;
  - confirm PR headRefOid/baseRefOid when available;
  - if local HEAD differs from PR headRefOid, `git pull --ff-only origin <branch>`;
  - stop if fast-forward fails, PR is merged, branch mismatches, or worktree is dirty.
- File scope.
- Forbidden actions.
- Fix goal.
- Validation commands.
- Stop conditions.
- Final output format.

## Output contract

Return:

- **Outcome**.
- **Assumptions**.
- **Dependency-aware board**.
- **Critical path**.
- **Risk and rollback notes**.
- **Review gates**.
- **Local-agent handoff blocks** when needed.

## Validation gate

Before finalizing, verify:

- No package is vague or outcome-only.
- Every package has validation evidence.
- Dependencies are explicit.
- High-risk/irreversible actions require human review.
- Status is evidence-based, not optimistic.

## Rules

Do not create work merely to fill a board. Do not mark work as done without evidence. Re-plan when a dependency, scope, PR state, or acceptance criterion changes.
