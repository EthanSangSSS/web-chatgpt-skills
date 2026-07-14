# Rational Product Evaluation Skill

A Codex skill for rational consumer product evaluation before purchase.

This skill turns product-shaped questions into decision-quality answers. It is designed for consumer electronics, gaming hardware, local AI hardware, appliances, and other purchase decisions where price, lifecycle timing, compatibility, total cost of ownership, and evidence quality matter more than generic review scores.

## What problem it solves

Most purchase advice collapses into one of three weak modes:

1. spec-sheet comparison;
2. review-score aggregation;
3. uncalibrated buy / wait opinions.

This skill instead asks: **what job is the user hiring this product to do, what alternatives satisfy that job, and what current evidence is strong enough to act on?**

## Best-fit questions

Use this skill for questions like:

- "Should I buy this product now?"
- "Compare these models for my use case."
- "Is this product worth it at this price?"
- "What should I buy instead?"
- "Should I wait, buy used, rent, subscribe, or do nothing?"
- "Is this upgrade actually useful, or just marketing?"

## What it does

- Reframes product-shaped questions into need-shaped decisions.
- Separates must-have requirements from nice-to-have preferences.
- Checks lifecycle, price, availability, alternatives, compatibility, warranty, support horizon, and market regime.
- Builds a broader option set: target product, lower tier, previous generation, used market, adjacent upgrade, rental / cloud / service path, wait path, and do-nothing path.
- Adds market-regime analysis for volatile categories such as GPUs, AI hardware, memory, SSDs, phones, laptops, handheld gaming devices, and large appliances.
- Labels weak claims, forecasts, and community narratives instead of treating them as facts.
- Avoids duplicated "reasoning trace plus final answer" output unless the user explicitly asks for a full audit trail.

## Output contract

Default output should be compact and decision-oriented:

1. **Decision** — buy / wait / buy used / choose alternative / do nothing.
2. **Reason** — the strongest product-fit and timing logic.
3. **Best alternatives** — cheaper, safer, older-generation, used, service-based, or wait-path options.
4. **Evidence quality** — strong facts vs weak market claims vs speculation.
5. **Invalidators** — what new fact would change the recommendation.
6. **Action** — what to check before purchase.

## Example prompt

```text
Use rational-product-evaluation: Should I buy an RTX 5090 now for 4K gaming and local AI inference?

Context:
- I care about local model inference, 4K gaming, noise, and resale value.
- I can wait three months if the market is overheated.
- Compare buy-now, previous-gen, used, cloud, and do-nothing options.
```

## Source policy

For media reviews, community feedback, online research, market interpretation, and forecasts, the skill prioritizes non-mainland-China independent sources.

Mainland China sources can still be useful for local price, stock, SKU, warranty, channel reality, and local owner complaints. However, mainland media, comments, official interpretations, ecommerce pages, and KOL narratives should not be the sole basis for explanatory conclusions or predictions. If they are the only evidence, the claim should be labeled `local narrative / weakly verified`.

This is an evidence-quality rule, not a claim that any single jurisdiction is always right or wrong.

## Install

Clone the repository directly into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/EthanSangSSS/rational-product-evaluation-skill.git ~/.codex/skills/rational-product-evaluation
```

If you already have a local copy, copy this directory directly:

```bash
mkdir -p ~/.codex/skills
rsync -a --exclude .git rational-product-evaluation-skill/ ~/.codex/skills/rational-product-evaluation/
```

Then ask Codex product-purchase questions such as:

```text
Use rational-product-evaluation: Should I buy an RTX 5090 now for 4K gaming and local AI inference?
```

## Files

- `SKILL.md`: main skill instructions and output contract.
- `references/category-matrix.md`: category-specific evaluation dimensions.
- `references/selection-strategy.md`: first-principles need discovery and option-space design.
- `references/market-regime.md`: timing, shortages, demand shocks, and TCO.
- `references/source-policy.md`: source jurisdiction and weak-verification policy.
- `references/output-discipline.md`: concise output and anti-duplication rules.
- `agents/openai.yaml`: UI metadata for skill lists and implicit invocation policy.
- `evals/smoke-prompts.md`: lightweight prompts for forward-testing behavior.

## Boundaries

This skill is for consumer purchase decisions. It is not financial, legal, medical, insurance, investment, procurement, or regulated professional advice.

Current products, prices, availability, recalls, firmware status, and market conditions can change quickly. The skill intentionally requires fresh verification before confident recommendations.

## License

MIT
