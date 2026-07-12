---
name: architecture-diagram
description: Produce readable, self-contained architecture diagrams as SVG or single-file HTML.
---
# Architecture Diagram
## Intake
Collect components, data flows, trust boundaries, deployment environment, audience, and the question the diagram must answer.
## Design
- Group components by boundary or layer.
- Use consistent shapes, colors, labels, and directional arrows.
- Put trust boundaries, external systems, and failure-critical paths first.
- Minimize crossings; prefer left-to-right or top-to-bottom flow.
## Deliver
Return either:
1. a self-contained SVG/HTML file in one code block, or
2. Mermaid when the user explicitly prefers editable text diagrams.
Include a concise legend and assumptions.
## Validation
Check every named component has a purpose, every arrow has a direction, and data/security boundaries are visible. Flag unknown integrations rather than inventing them.
