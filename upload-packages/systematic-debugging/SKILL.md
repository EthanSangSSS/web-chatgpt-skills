---
name: systematic-debugging
description: Diagnose bugs through evidence, competing hypotheses, and minimal discriminating tests.
---
# Systematic Debugging
## Rules
Do not patch before understanding the failure. Separate observed behavior, expected behavior, and assumptions.
## Workflow
1. Capture a minimal reproducible symptom and environment facts.
2. Map the smallest relevant execution path.
3. Form ranked hypotheses with predicted observations.
4. Propose one discriminating test per hypothesis.
5. Use user-provided logs or results to update the hypothesis ranking.
6. Recommend the smallest safe fix and regression tests.
## Output
Symptom, evidence, hypotheses, next test, diagnosis confidence, fix plan, and regression guard.
## Boundaries
Never fabricate logs or claim reproduction. If evidence is insufficient, request the single most informative artifact.
