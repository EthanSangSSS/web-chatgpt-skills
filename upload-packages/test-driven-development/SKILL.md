---
name: test-driven-development
description: Design tests before implementation and guide RED-GREEN-REFACTOR with user-supplied execution evidence.
---
# Test-Driven Development
## Workflow
1. Restate the behavior and acceptance criteria.
2. Enumerate examples, edge cases, failure modes, and invariants.
3. Draft the smallest failing tests first.
4. Specify the minimal implementation needed to pass them.
5. Refactor only after behavior is protected.
## Evidence loop
The user runs tests in their environment and supplies results. Diagnose failures from the actual output; never claim tests passed without evidence.
## Output
- Test matrix
- Test code or pseudocode appropriate to the stack
- Minimal implementation plan
- Refactoring checks
- Commands the user can run, clearly marked as not executed by ChatGPT
