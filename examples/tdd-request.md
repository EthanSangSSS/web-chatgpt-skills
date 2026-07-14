# Example: Test-Driven Development Request

## User request

```text
Use EthanSangSSS/web-chatgpt-skills. Design tests first for a validator that rejects skill catalog entries whose path is not `<skill>/SKILL.md`. I only need the test plan and expected fixtures; do not claim to run the tests.
```

## Expected skill selection

- Read `CATALOG.yaml`.
- Select `test-driven-development`.
- Read `test-driven-development/SKILL.md` before producing the test plan.

## Expected assistant behavior

The assistant should:

1. define RED tests before proposing implementation;
2. list positive and negative fixtures;
3. specify exact validation commands only as commands to run, not as commands already run;
4. avoid claiming PASS without command output;
5. include a local-agent handoff if actual file edits or test execution are required.

## Example test matrix

| Case | Catalog path | Expected result |
|---|---|---|
| canonical path | `truth-seeking/SKILL.md` | pass |
| deprecated package layer | `upload-packages/truth-seeking/SKILL.md` | fail |
| missing skill file | `missing-skill/SKILL.md` | fail |
| duplicate skill id | two `id: truth-seeking` entries | fail |

## Evidence boundary

The assistant may design tests from the request and visible repository rules. It must not say the tests passed unless it has command output or CI evidence.
