---
name: industrial-self-audit-protocol
description: Evidence-based final quality gate for plans, code, documents, and deliverables.
---
# Industrial Self-Audit
## Evidence package
Collect the deliverable, stated requirements, relevant source material, validation results, and known limitations.
## Audit
Review independently across:
- Correctness: does it satisfy stated requirements?
- Robustness: edge cases, failure modes, privacy, security, reversibility, and maintenance.
- Elegance: simplicity, consistency, and unnecessary complexity.
For each finding, attach evidence and severity.
## Release gate
Return one of: ready, ready with conditions, revise, or blocked.
## Output
- Scope reviewed
- Findings by severity
- Evidence and confidence
- Required fixes
- Residual risks
- Revalidation checklist
## Rules
Do not certify what was not inspected. Treat missing evidence as uncertainty, not success.
