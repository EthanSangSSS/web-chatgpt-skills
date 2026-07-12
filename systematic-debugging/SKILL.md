---
name: systematic-debugging
version: "0.2.0"
status: stable
description: Diagnose failures through evidence, competing hypotheses, discriminating tests, and explicit reproduction confidence in Web ChatGPT.
triggers:
  - bug
  - error
  - crash
  - traceback
  - log analysis
  - startup failure
  - 报错
  - 启动失败
  - 崩溃
do_not_use_for:
  - feature planning without a failure
  - product purchase decision
  - unsupported test-pass certification
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Systematic Debugging

## Operating rule

Do not patch before understanding the failure. Separate observed behavior, expected behavior, assumptions, and speculation. Treat logs, stack traces, screenshots, test output, GitHub diffs, and exact environment facts as evidence; treat user summaries and agent reports as claims until verified.

## Required input

Collect or infer:

- Minimal reproducible symptom.
- Expected behavior.
- Actual behavior and exact error text.
- Environment: OS, app/runtime version, dependency versions, device, branch/commit if relevant.
- Recent changes.
- Available evidence: logs, stack trace, screenshot, test output, diff, config.

If evidence is insufficient, ask for the single most discriminating artifact. If the user wants an immediate best-effort answer, state assumptions and mark confidence.

## Web ChatGPT execution boundary

This skill may analyze provided evidence, uploaded files, GitHub connector data, and web search results. It must not claim to reproduce, run commands, inspect local processes, edit local files, or pass tests unless an actual tool result proves it.

If local repo state, local logs, shell commands, build/test execution, app launch, simulator/device inspection, or credentials are required, stop direct execution and produce a local-agent handoff.

## Workflow

1. Build a **symptom ledger**:
   - observed symptom;
   - expected behavior;
   - first known bad point;
   - evidence source;
   - reproduction confidence: confirmed / partial / unverified.
2. Map the smallest relevant execution path.
3. Rank competing hypotheses. For each hypothesis, state:
   - mechanism;
   - supporting evidence;
   - contradictory evidence;
   - predicted observation if true;
   - confidence.
4. Choose the next discriminating test with the highest information value and lowest risk.
5. Update ranking only from actual new evidence.
6. Recommend the smallest safe fix and regression guard.

## Output contract

Return:

- **Verdict**: diagnosis / likely cause / inconclusive.
- **Symptom ledger**.
- **Evidence reviewed**.
- **Hypothesis table**: hypothesis, mechanism, evidence, contradiction, next test, confidence.
- **Most informative next test**.
- **Fix plan**: smallest safe change, blast radius, rollback.
- **Regression guard**: unit/integration/manual check.
- **Local-agent handoff** when needed.

## Validation gate

Before recommending a fix, check:

- Is the failure real or could it be a stale/filtered/partial signal?
- Does the hypothesis explain all known symptoms?
- What evidence would falsify the hypothesis?
- Is the proposed fix smaller than alternative fixes?
- Is there a regression test or guard?

## Local-agent handoff trigger

Hand off when resolving the issue requires local command execution, repository edits, build/test runs, simulators, devices, logs not present in chat, or multi-file changes. The handoff must include repo, branch, HEAD/PR metadata if available, file scope, forbidden actions, validation commands, stop conditions, and final output format.
