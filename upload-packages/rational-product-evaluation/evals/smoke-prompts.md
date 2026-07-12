# Smoke Prompts

Use these prompts as lightweight forward tests after changing the skill. They are not factual goldens; they check behavior and output discipline.

## 1. Volatile GPU Purchase

```text
Use rational-product-evaluation: Should I buy an RTX 5090 now for 4K gaming and local AI inference? Budget is 20000 RMB. I have an RTX 4060 now.
```

Expected behavior:

- Mentions real need, bottleneck, and utilization uncertainty.
- Includes market-regime/TCO analysis for GPU and AI hardware.
- Avoids relying only on mainland sources for explanatory claims or forecasts.
- Gives threshold-based timing rather than a vague "wait".
- Does not print the full 8-step trace plus a duplicate final answer.

## 2. Named Product May Be Overkill

```text
Use rational-product-evaluation: I want to buy the most expensive mesh router for a 90 square meter apartment. Is that sensible?
```

Expected behavior:

- Reframes the purchase around coverage, wall material, device count, ISP speed, and wired backhaul.
- Presents a lower-cost path or do-nothing path if the bottleneck is unclear.
- Keeps the answer compact unless the user asks for a full comparison.

## 3. Output Audit

```text
Use rational-product-evaluation to evaluate this output: "Buy now, it is the best product. Reviews say it is amazing. No need to wait."
```

Expected behavior:

- Uses audit-trace mode.
- Findings lead the answer.
- Flags missing use case, price, region, alternatives, evidence quality, and timing.
- Does not produce a full product recommendation unless asked.
