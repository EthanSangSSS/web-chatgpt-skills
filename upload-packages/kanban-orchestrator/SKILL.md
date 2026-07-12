---
name: kanban-orchestrator
description: Decompose a goal into bounded, independently verifiable work packages and dependency-aware execution order.
---
# Kanban Orchestrator
## Workflow
1. Define outcome, constraints, deadline, and acceptance evidence.
2. Split work into small packages with a single owner, clear inputs, outputs, and stop conditions.
3. Mark dependencies, risks, irreversible actions, and review gates.
4. Sequence work to reduce blocked time and preserve rollback options.
5. Review package status only from actual evidence.
## Board format
| ID | Work package | Depends on | Deliverable | Validation | Risk | Status |
|---|---|---|---|---|---|---|
## Rules
Do not create work merely to fill a board. Keep high-risk decisions under explicit human review. Re-plan when a dependency or acceptance criterion changes.
