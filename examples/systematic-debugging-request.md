# Example: Systematic Debugging Request

## User request

```text
Use EthanSangSSS/web-chatgpt-skills. A GitHub Actions job fails at the public-safety scan step after a documentation PR. Help debug the failure from the PR metadata and workflow logs only. Do not assume local reproduction.
```

## Expected skill selection

- Read `CATALOG.yaml`.
- Select `systematic-debugging`.
- Read `systematic-debugging/SKILL.md` before diagnosing.

## Expected assistant behavior

The assistant should:

1. create a symptom ledger from the visible job steps and logs;
2. separate facts from hypotheses;
3. identify discriminating tests or additional logs needed;
4. avoid claiming local reproduction unless command output exists;
5. propose the smallest safe fix and a verification plan.

## Example symptom ledger

| Observation | Source | Status |
|---|---|---|
| Catalog validation step succeeded | GitHub Actions job steps | fact |
| Public-safety scan step failed | GitHub Actions job steps | fact |
| Failure may be a false positive on a denylist pattern | inference from script behavior | hypothesis |
| Local reproduction unavailable | tool boundary | limitation |

## Safe fix pattern

Prefer tightening the validator scope or fixture expectations over disabling the check entirely. Keep CI read-only and preserve evidence boundaries.

## Evidence boundary

Allowed evidence:

- PR metadata;
- changed files and patches;
- GitHub Actions jobs, steps, and logs;
- repository files fetched from GitHub.

Not allowed:

- claiming local reproduction without command output;
- assuming logs not retrieved;
- marking the PR as PASS before CI success is verified.
