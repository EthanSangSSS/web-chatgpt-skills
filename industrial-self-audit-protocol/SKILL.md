---
name: industrial-self-audit-protocol
version: "0.2.0"
status: stable
description: Evidence-based final quality gate for plans, code, documents, and deliverables, using explicit scope, severity, evidence, residual risk, and revalidation checks.
triggers:
  - final audit
  - quality gate
  - release readiness
  - review deliverable
  - 最终审核
  - 质量门禁
  - 验收
do_not_use_for:
  - certifying uninspected work
  - replacing required professional compliance review
  - claiming tests passed without evidence
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Industrial Self-Audit

## Purpose

Perform a final, evidence-based quality gate for a deliverable. The audit should identify whether the work is ready, conditionally ready, inconclusive, failed, or blocked. Missing evidence is uncertainty, not success.

## Required evidence package

Collect or infer:

- Deliverable under review.
- Stated requirements or intended outcome.
- Source material and constraints.
- Validation results, logs, screenshots, tests, PR/diff/commit data, or user-provided evidence.
- Known limitations and excluded scope.
- Production risk tolerance.

If evidence is missing, proceed with an `INCONCLUSIVE` or conditional verdict rather than asking many questions, unless one artifact would materially change the result.

## Web ChatGPT execution boundary

This skill may inspect conversation content, uploaded files, GitHub connector data, and web evidence. It must not claim local execution, local inspection, build success, test pass, deployment, or stakeholder approval without actual evidence.

## Audit dimensions

Review independently across:

- **Correctness**: satisfies stated requirements and user intent.
- **Completeness**: covers required scope and edge cases.
- **Robustness**: failure modes, privacy, security, accessibility, reversibility, maintenance.
- **Evidence integrity**: validation quality, source reliability, stale data, uninspected scope.
- **Elegance**: simplicity, consistency, unnecessary complexity.
- **Operational readiness**: rollback, monitoring, documentation, owner, next validation.

## Severity taxonomy

- **P0**: blocker; unsafe, incorrect, destructive, leaking secrets, or invalidates release/use.
- **P1**: major issue; likely failure, misleading claim, missing required validation.
- **P2**: moderate issue; quality or maintainability risk with workaround.
- **P3**: minor polish or documentation improvement.

## Verdict taxonomy

Return one:

- `PASS`: evidence supports release/use; no material open risk.
- `PASS_WITH_WARNINGS`: usable with explicit residual risks or non-blocking fixes.
- `INCONCLUSIVE`: insufficient evidence to certify.
- `FAIL`: inspected evidence shows requirements are not met.
- `BLOCKED`: cannot proceed due to missing access, unsafe state, policy, or dependency.

## Output contract

Return:

- **Verdict**.
- **Scope reviewed**.
- **Evidence package**.
- **Uninspected scope**.
- **Findings table**: ID, severity, evidence, impact, required fix, confidence.
- **Residual risks**.
- **Required fixes**.
- **Revalidation checklist**.
- **Decision recommendation**.

## Validation gate

Before finalizing, verify:

- Every finding has evidence.
- Missing evidence is labeled, not treated as pass.
- Scope reviewed and uninspected scope are explicit.
- Verdict follows the severity taxonomy.
- Required fixes have revalidation steps.

## Local-agent handoff trigger

Hand off when the audit requires local tests, build execution, repo-wide scans, generated artifact inspection, screenshots, or multi-file validation. The handoff must include repo, branch, HEAD/PR metadata if available, file/artifact scope, validation commands, forbidden actions, stop conditions, and final output format.
