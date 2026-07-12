---
name: test-driven-development
version: "0.2.0"
status: stable
description: Design tests before implementation and guide RED-GREEN-REFACTOR using only user-supplied or tool-verified execution evidence.
triggers:
  - TDD
  - tests first
  - unit test
  - integration test
  - regression test
  - 测试驱动
  - 回归测试
do_not_use_for:
  - claiming tests passed without evidence
  - broad project planning without behavior under test
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Test-Driven Development

## Purpose

Turn behavior into executable checks before implementation. In Web ChatGPT, this means designing tests, test matrices, minimal implementation plans, and validation commands while clearly marking what has not been executed.

## Required input

Collect or infer:

- Behavior under test and user-visible outcome.
- Acceptance criteria.
- Stack/language/framework if code is involved.
- Existing failure or feature request.
- Constraints: speed, determinism, external services, mocks/fakes, golden files, accessibility, security.

Ask one clarifying question only when the expected behavior is materially ambiguous. Otherwise state assumptions and proceed.

## Web ChatGPT execution boundary

This skill may draft tests and implementation plans from conversation, uploaded files, GitHub connector data, and web search. It must not claim tests passed, builds succeeded, or code executed unless a tool result or user-provided output proves it.

Commands must be labeled as **not executed by ChatGPT** unless actually run by an available tool.

## Workflow

1. Restate behavior and acceptance criteria.
2. Identify examples, edge cases, invariants, and failure modes.
3. Choose test layers:
   - unit for pure logic;
   - integration for component boundaries;
   - golden/snapshot for stable rendering or output shape;
   - property/fuzz for invariant-heavy logic;
   - manual exploratory checks only when automation is disproportionate.
4. Draft the smallest failing tests first.
5. Specify the minimal implementation needed to pass them.
6. Refactor only after behavior is protected.
7. Add regression guards for every bug fix.

## Output contract

Return:

- **Behavior statement**.
- **Acceptance criteria**.
- **Test matrix**: case, type, setup, expected result, why it matters.
- **Test code or pseudocode** appropriate to the stack.
- **Minimal implementation plan**.
- **Commands to run** clearly marked as not executed by ChatGPT.
- **Evidence loop**: what output the user/local agent should return.
- **Refactor checks**.

## Validation gate

Before finalizing, verify:

- Each acceptance criterion has at least one test or explicit manual check.
- Tests avoid depending on live services unless the behavior requires it.
- Mocks/fakes preserve the contract being tested.
- Failure messages would help diagnose regressions.
- No test pass is claimed without evidence.

## Local-agent handoff trigger

Hand off when tests must be written into a repository, dependencies must be installed, commands must run, fixtures/golden files must be generated, or code must change. The handoff must include repo, branch, file scope, test files to add/update, validation commands, forbidden actions, stop conditions, and final output format.
