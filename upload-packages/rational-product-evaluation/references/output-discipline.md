# Output Discipline

Use this reference to prevent verbose, duplicated product-evaluation answers.

## Default Rule

The 8-step flow is an internal checklist, not the default output. The user usually wants the decision, not the transcript of the decision process.

Default output mode: **Standard final answer only**.

## Modes

| Mode | Use when | Max shape |
|---|---|---|
| Quick | User wants a quick take. | 4 short sections. |
| Standard | Normal buying advice. | Conclusion, fit, source posture, evidence, market/TCO, alternatives, thresholds, unresolved checks. |
| Audit Trace | User asks to evaluate an output. | Findings first; cite the failing lines/claims; no full recommendation unless asked. |
| Full 8-Step | User explicitly asks for all steps. | Show each step once; no duplicated final tables. |

## Anti-Duplication Rules

- Do not print "Step 0...Step 8" and then repeat the same tables under "Output".
- If `选品空间` already lists alternatives, `替代选择` should add only new tradeoffs or can be omitted.
- If `证据表` already states a claim and confidence, `评分` should only state the score implication.
- If `市场环境与TCO` already lists market factors, `最大风险` should name only the top 3 consequences.
- `仍需核验` should include only facts that could change the recommendation, not every missing detail.

## Audit Trace Format

When evaluating another generated output:

```markdown
**结论**
[usable / needs revision / not reliable] — one sentence.

**Findings**
1. [Severity] [Issue] — [why it matters].
2. ...

**What to fix**
- ...

**Residual risk**
- ...
```

## Freshness Language

Avoid stale lifecycle phrases unless verified on today's date:

- "首发早期"
- "还没发布"
- "预计 3-6 个月上市"
- "价格稳定后"
- "缺货溢价"
- "竞品未发布"

If a claim is not verified, write: `unverified as of today` or put it under `仍需核验`.
