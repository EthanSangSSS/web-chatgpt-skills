# Example: GitHub Reality Audit

This example shows how a reviewer should treat a local-agent report as a claim list, not as evidence.

## User request

```text
Review this local agent report and tell me whether the PR is ready to merge.
```

## Required reviewer behavior

1. Extract claims from the local-agent report.
2. Verify the actual GitHub state:
   - repository;
   - branch;
   - PR number;
   - PR head SHA;
   - base SHA;
   - changed files;
   - checks / workflow runs;
   - mergeability;
   - unresolved review threads.
3. Compare claims against GitHub evidence.
4. Return `PASS`, `PASS_WITH_WARNINGS`, `INCONCLUSIVE`, `FAIL`, or `BLOCKED`.
5. Do not treat "agent says tests passed" as a verified test pass.

## Safe output pattern

```text
Verdict: INCONCLUSIVE

Verified:
- PR exists.
- Head SHA matches the reported SHA.
- Changed files are within the claimed scope.

Not verified:
- Test command output was not available in GitHub Actions or attached logs.

Next action:
- Ask the local agent to provide exact command output or push CI-backed validation.
```

## Anti-pattern

```text
PASS. The local agent said all tests passed.
```

Why this is wrong: the statement relies on an unverified claim instead of GitHub telemetry.
