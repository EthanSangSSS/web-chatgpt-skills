# Example: Architecture Diagram Request

## User request

```text
Use EthanSangSSS/web-chatgpt-skills. Create a C4-style diagram for a small issue-triage bot that reads GitHub issues, labels them, and drafts maintainer handoffs. Do not assume local filesystem access.
```

## Expected skill selection

- Read `CATALOG.yaml`.
- Select `architecture-diagram`.
- Read `architecture-diagram/SKILL.md` before drafting the diagram.

## Expected assistant behavior

The assistant should:

1. identify system boundary, users, external systems, and data flows;
2. distinguish GitHub connector access from local shell access;
3. avoid claiming it inspected local files or ran build commands;
4. produce a readable diagram specification, Mermaid diagram, SVG plan, or implementation-ready diagram brief depending on the user request;
5. call out trust boundaries and sensitive data surfaces.

## Evidence boundary

Allowed evidence:

- user-provided system description;
- GitHub connector data, if explicitly available;
- uploaded files, if supplied;
- web sources, if current public documentation is required.

Not allowed:

- private repository contents unless retrieved through an authorized connector;
- local command execution claims;
- unverified production topology claims.

## Review checklist

- The diagram labels external systems and trust boundaries.
- Data flows do not imply unauthorized credential access.
- The output does not claim deployment, tests, or runtime verification without evidence.
