# Selection Strategy

This reference turns product review into product selection. Use it when the user asks about an expensive item, a confusing category, or a named product that may not be the best solution.

## Community-Agent Patterns To Absorb

Mature shopping agents tend to share the same workflow:

1. Collect user needs into explicit state.
2. Convert needs into structured filters and scoring dimensions.
3. Retrieve current listings, reviews, specs, and common issues.
4. Map raw data into a schema before comparing.
5. Compare candidates against the user's needs, not against generic "best product" lists.
6. Present a recommendation plus evidence, alternatives, and next action.
7. Let the user refine requirements and rerun the comparison.

Use these ideas as behavior, not as dependencies. For this skill, the "state" can be a compact table in the answer.

## First-Principles Need Discovery

Before recommending, identify the actual system:

| Lens | Ask | Why it matters |
|---|---|---|
| Job | What job does this purchase do? | Prevents category lock-in. |
| Bottleneck | What currently blocks the user? | The best purchase removes the binding constraint. |
| Success metric | What measurable outcome matters? | FPS, model size, latency, time saved, comfort, reliability, cost/use. |
| Frequency | How often will the product be used? | High capex needs utilization. |
| Constraint | What cannot change? | Budget, space, power, OS, portability, warranty, noise. |
| Reversibility | Can it be returned, resold, rented, or delayed? | Changes risk tolerance. |
| Opportunity cost | What else could the money solve? | Avoids local optimization. |

## Option-Space Ladder

For every serious purchase, build at least four of these paths:

| Path | Use when |
|---|---|
| Buy target product | Fit is high, price is below threshold, risk is acceptable. |
| Buy lower tier | User is overbuying for the real bottleneck. |
| Buy previous-gen or used | Mature reliability data and better value matter. |
| Upgrade adjacent bottleneck | RAM, SSD, monitor, network, PSU, chair, workflow, software, etc. |
| Rent or use cloud/service | Utilization is low or demand is spiky. |
| Wait | Launch volatility, upcoming replacement, bug fixes, or seasonal pricing dominate. |
| Do nothing | Current setup already meets the success metric. |

## Recommendation Modes

Use one of these labels:

| Mode | Meaning |
|---|---|
| Buy now | Fit is high and market/timing is acceptable. |
| Buy if threshold met | Good product, price-sensitive decision. |
| Wait with trigger | Waiting is rational only until a specific event or price. |
| Choose different tier | Target product is overkill or misaligned. |
| Rent/cloud first | Need is real but utilization or model fit is uncertain. |
| Avoid | Core claim fails, risk is high, or better alternatives dominate. |

## Threshold Design

Avoid vague "wait" when the decision is price-sensitive. Produce thresholds:

| Condition | Action |
|---|---|
| Price below fair value | Buy. |
| Price between fair and stretch | Buy only if use is urgent/high-utilization. |
| Price above stretch | Do not buy; use fallback path. |
| New evidence appears | Re-evaluate: defect fixed, firmware update, price shock, new model, recall. |

## Stress Test

Before finalizing, ask:

- If the named product vanished, what would solve the job?
- If the budget were cut by 40%, what would still work?
- If the product price rose 20%, would the recommendation change?
- If the user only used it twice per month, would the recommendation change?
- If renting/cloud/service were available, how many months until buying wins?
