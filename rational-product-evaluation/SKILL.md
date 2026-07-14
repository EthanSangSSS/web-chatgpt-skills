---
name: rational-product-evaluation
description: Use when evaluating consumer products before purchase, especially electronics, appliances, digital hardware, TVs, monitors, phones, laptops, headphones, routers, cameras, smart-home devices, GPUs, or AI hardware. Trigger for "值不值得买", "帮我选", "产品评估", "购买建议", "对比一下", "避坑", "这个型号靠谱吗", "现在能不能买", "选品方案", "真实需求", "AI显卡", "consumer product review", "purchase decision", and "compare products". Do not use for B2B procurement, regulated professional advice, investment analysis, or pure troubleshooting unless the user is deciding whether to return, repair, or replace.
metadata:
  version: "1.4"
  triggers:
    - rational-product-evaluation
    - 值不值得买
    - 帮我选
    - 产品评估
    - 购买建议
    - 对比一下
    - 避坑
    - 这个型号靠谱吗
    - 现在能不能买
    - consumer product review
    - purchase decision
    - compare products
    - 选品方案
    - 真实需求
    - AI显卡
  do_not_use_for:
    - B2B/vendor procurement, contracts, or enterprise RFPs; use a procurement or due-diligence workflow.
    - Medical, legal, financial, insurance, or regulated advice.
    - Investment/startup viability analysis; use startup-pitfall-analyzer.
    - Pure technical troubleshooting after purchase unless the user is deciding whether to return, repair, or replace.
---

# Rational Product Evaluation

## Core Principle

评测不是为了种草，而是为了判断这个产品是否适合这个人、这个预算、这个时间点。用户问的常常是一个产品，但真正要解决的是一个 job、一个约束系统、一个时机选择。

Two default suspicions:

- Review independence is a baseline, not a marketing claim. Treat ads, affiliate links, and manufacturer access as possible bias.
- A review unit may not match the retail unit. Prefer retail-purchased evidence, long-term user feedback, and post-launch firmware history.

## When To Use

Use this skill when the user asks whether to buy, compare, wait, return, replace, or avoid a consumer product. If the product is current or price-sensitive, browse or otherwise verify fresh facts before giving a recommendation.

Do not give a confident recommendation until the minimum context is known. If context is missing, ask only the missing high-impact questions first.

If the user asks "should I buy X", first decide whether this is really:

- product validation: X is probably the right category, evaluate the model
- option design: X may be the wrong solution, build a better option set
- timing decision: category is right, but market cycle may dominate
- TCO decision: purchase competes with renting, cloud usage, repairing, waiting, or doing nothing

## Minimum Input

Collect or infer these before analysis:

| Field | Required? | Notes |
|---|---:|---|
| Product/category | Yes | Exact model, category, or shortlist. |
| Budget and region | Yes | Region matters for price, warranty, channels, and model variants. |
| Primary use | Yes | Rank the top 2-3 jobs-to-be-done. |
| Success metric | Yes | FPS, latency, model size, daily time saved, comfort, reliability, cost per use, etc. |
| Current device/ecosystem | Usually | Apple/Android/Windows, console, smart-home platform, router, TV box, etc. |
| Time window | Usually | Buy now, wait for sale, replace urgently, return window. |
| Utilization | Usually | How often the product will be used; critical for high-ticket items. |
| Constraints | Usually | Size, weight, noise, heat, privacy, repairability, brand blacklist, installation limits. |
| Opportunity cost | Usually | What else the same budget could solve: accessories, RAM/SSD, cloud rental, used market, travel, time. |

If the user only wants a quick take, state the assumptions and mark the result as provisional.

## Freshness Gate

Before finalizing any recommendation for current or fast-moving products, run a freshness gate. If any gate item is unresolved, lower confidence and put it in `仍需核验`.

| Gate | Required check |
|---|---|
| Product lifecycle | Is the product launched, discontinued, refreshed, recalled, or replaced as of today? |
| Alternatives lifecycle | Are named alternatives actually available now, not merely expected? |
| Current price | What is the current street price in the user's region and at least one non-local reference market? |
| Performance claims | Are performance deltas supported by current independent benchmarks for the exact comparison? |
| Market regime | Are shortage, demand, tariff, memory/storage, or supply-chain claims current and sourced? |
| Compatibility | Are power, connector, size, OS, firmware, and SKU assumptions verified? |

Hard rule: do not use phrases like "预计上市", "首发早期", "还没发布", "价格稳定后", or "缺货溢价" without a current-date check. If stale data is discovered, correct it before drawing the conclusion.

## Evidence Rules

1. Separate marketing claims from verifiable product facts.
2. For current products, verify price, availability, model variants, firmware/recall issues, and recent user complaints with fresh sources.
3. For web search, media reviews, community feedback, research, and explanatory analysis, prioritize non-mainland-China independent sources first. Mainland Chinese media, comments, official interpretations, ecommerce pages, and KOL narratives may support local price/channel sentiment, but they cannot alone support explanatory conclusions or forecasts.
4. If a conclusion or prediction relies only on mainland Chinese sources, label it `local narrative / weakly verified` and lower confidence until cross-validated by non-mainland independent sources.
5. Use at least three independent evidence streams when available:
   - official specs/manuals/warranty terms
   - retail-purchased reviews or long-term reviews
   - owner feedback from forums, ecommerce reviews, Reddit, international forums, Xiaohongshu/Tieba, or repair communities
   - price history and second-hand value
   - teardown, latency, thermal, acoustic, power, or calibration data when relevant
6. Prefer retail-unit and long-term data over launch reviews.
7. Treat single-source praise, launch-only reviews, unverified benchmark screenshots, affiliate-heavy content, and single-jurisdiction narratives as weak evidence.
8. Mention evidence gaps explicitly instead of filling them with confidence.

See `references/category-matrix.md` for category-specific criteria and source prompts.
Use `references/selection-strategy.md` for first-principles need discovery and option-space design.
Use `references/market-regime.md` when price, supply, AI demand, memory/storage costs, tariffs, platform cycles, or resale value may dominate the decision.
Use `references/source-policy.md` for source jurisdiction, media/community feedback, and weak-verification labeling.
Use `references/output-discipline.md` to avoid repeated step-by-step and final-answer duplication.

## Evaluation Flow

### 0. Real Need Discovery

Before comparing specs, translate the user's product-shaped question into a need-shaped brief:

| Question | Purpose |
|---|---|
| What job must this purchase do? | Avoid optimizing for the wrong category. |
| What is the bottleneck today? | The best purchase removes the binding constraint. |
| What result would make the user satisfied in 30 days? | Makes the decision measurable. |
| What is non-negotiable? | Separates hard constraints from preferences. |
| What can be rented, delayed, repaired, upgraded, or ignored? | Expands the option space. |

If the true need is unclear, answer with a provisional decision and list the two or three questions that could change it.

### 1. Fit Before Specs

Map the product to the user's actual use:

- What problem does it solve?
- Which feature will be used weekly?
- Which praised feature is irrelevant to this user?
- What existing device or cheaper alternative already covers the job?

If the product does not fit the user's primary use, downgrade the recommendation even if reviews are strong.

### 2. Option Space Design

Do not only compare the user's named product against nearby models. Build a small but complete option set:

| Option type | Examples |
|---|---|
| Target product | The product the user asked about. |
| Lower-cost fit | Cheaper model that solves the real bottleneck. |
| Previous generation / used | Mature product with better value or reliability data. |
| Adjacent category | Different form factor, service, rental, cloud, repair, or accessory. |
| Wait path | Upcoming launch, price normalization, sale window, post-fix batch. |
| Do nothing | Keep current device if the bottleneck is not severe. |

Use community-agent best practice: collect requirements, map them into structured fields, retrieve options, compare in a schema, then generate the recommendation. Do not jump from search results directly to a narrative answer.

### 3. Market Regime Check

Run this step for cyclic, constrained, or high-ticket categories: GPUs, CPUs, memory, SSDs, phones, laptops, cars, cameras, consoles, and appliances with volatile rebates.

Classify the market:

| Regime | Meaning | Decision effect |
|---|---|---|
| Normal depreciation | Price likely falls with time. | Waiting has positive expected value. |
| Launch/scalper spike | Early supply is distorted. | Wait unless urgency or threshold price is met. |
| Structural shortage | Supply is constrained by upstream capacity. | Waiting may increase total cost. |
| Demand shock | New use case or hype absorbs supply. | Evaluate whether user benefits from the shock or pays for it. |
| Replacement-cycle cliff | New generation or regulation is near. | Avoid buying obsolete inventory unless discounted. |

For GPUs and AI hardware, explicitly evaluate AI infrastructure demand, memory/GDDR/HBM supply, PSU/cooling/DDR5/SSD basket cost, cloud rental alternatives, and resale value.

### 4. Claim Verification

List the top vendor/reviewer claims and classify each:

| Claim | User impact | Evidence status | Risk |
|---|---|---|---|
| Marketing claim | High/Medium/Low | Verified / mixed / unverified / false | Practical consequence |

Use search patterns like:

- `<model> retail unit review`
- `<model> long term review`
- `<model> common problems`
- `<model> firmware issue`
- `<model> recall`
- `<model> quality problem`
- `<model> 零售机 送测机 差异`
- `<model> 通病 翻车 售后`

### 5. Category Scoring

Score only dimensions that matter for the category and user. Use a 1-5 scale:

- 5: clear strength, independently verified
- 4: good, minor caveats
- 3: acceptable but not a reason to buy
- 2: meaningful weakness
- 1: deal-breaker for this user

Always include:

- fit for primary use
- value versus alternatives
- reliability/quality risk
- ownership cost
- purchase timing

### 6. Anti-Manipulation Check

Look for review/benchmark manipulation:

| Risk | Checks |
|---|---|
| Tuned review unit | Retail unit results, owner reports, post-launch revisions. |
| Benchmark whitelist | Real workload/game results, 1% low, sustained performance, nonstandard test tools. |
| Spec trick | Native vs interpolated, peak vs sustained, HDR label vs real brightness/zones, refresh rate vs response time. |
| Firmware change | Launch results vs current firmware, regressions, removed features. |
| Region/model mismatch | Same name with different panel, chip, warranty, charger, ads, OS, or bands. |

### 7. TCO And Decision Threshold

For expensive or productivity-related products, compute or estimate total cost of ownership:

| Cost/benefit | Include |
|---|---|
| Purchase cost | Street price, tax, shipping, warranty, accessories. |
| Enabling upgrades | PSU, case, cooling, RAM, SSD, adapters, software. |
| Operating cost | Power, consumables, subscription, maintenance. |
| Utilization | Hours per week, workload criticality, replacement urgency. |
| Resale/depreciation | Expected exit value and liquidity. |
| Substitute cost | Cloud/rental/service cost, outsourcing, keeping current device. |

Convert the recommendation into thresholds when possible:

| Price band | Action |
|---|---|
| Below fair-value threshold | Buy if fit is high. |
| Between fair and stretch | Buy only if primary use is urgent or high-utilization. |
| Above stretch threshold | Wait, rent, buy used/previous-gen, or choose a lower tier. |

### 8. Alternatives And Timing

Compare against:

- cheaper previous-generation flagship
- same-price competitor
- better-fit niche product
- "do nothing / keep current device"
- upcoming replacement if the product cycle is near

Timing defaults:

| Situation | Default recommendation |
|---|---|
| Launch week with little retail feedback | Wait unless urgent. |
| Known quality controversy | Wait or avoid until fixed with evidence. |
| Stable product at historical low price | Buy if fit is high. |
| Replacement cycle imminent | Buy discounted older model or wait for next gen. |
| Return window still open and major risk found | Recommend return/exchange path. |

## Output Contract

Use the shortest structure that answers the decision. Default mode is **final answer only**. Do not print the full 8-step working process and then repeat it in the final output. The 8 steps are an internal analysis checklist unless the user explicitly asks for an audit trace, debug output, or "按 8 步展开".

Standard output should fit in 4-6 compact sections. Include a table only when it changes the decision or prevents ambiguity.

```markdown
**结论**
[Buy / Buy if / Wait / Avoid / Return or replace] — one sentence.

**为什么**
- Real need / bottleneck:
- Decision driver:
- Biggest caveat:

**选品空间** *(required for expensive, confusing, or overbuy-prone decisions)*
| Path | When it wins | Why it may lose |
|---|---|---|

**关键证据** *(use bullets for simple cases; use a table only for contested claims)*
| Claim or concern | Evidence | Confidence | Impact |
|---|---|---|---|

**来源姿态** *(required when web/media/community evidence matters)*
- Non-mainland independent sources checked:
- Mainland/local narrative used for:
- Weakly verified claims:

**市场环境与TCO** *(required for volatile or high-ticket categories)*
| Factor | Current signal | Decision effect |
|---|---|---|

**价格阈值 / 购买时机**
| Price or condition | Action |
|---|---|

**风险与替代**
- Top risk:
- Better fallback:
- Re-evaluate when:

**仍需核验**
- [Only list unresolved facts that could change the decision.]
```

Avoid emitting both `评分` and `证据表` by default. Use `评分` only when the user asks for ranking or when comparing three or more candidates. If `选品空间` already covers alternatives, omit `替代选择`.

For quick answers, compress to: `结论 / 理由 / 风险 / 什么时候买`.

### Output Modes

| Mode | When to use | Sections |
|---|---|---|
| Quick | User asks for quick take or low-stakes product | `结论 / 关键理由 / 最大风险 / 仍需核验` |
| Standard | Default | Output Contract above, but keep tables short and do not repeat the 8-step trace. |
| Audit Trace | User asks to inspect reasoning, compare skill behavior, or debug an output | Brief finding list, then only the failed/important steps. |
| Full 8-Step | User explicitly asks "按 8 步流程完整展开" | Show all steps once; do not append a duplicate final answer with the same tables. |

Deduplication rule: if a fact appears in `证据表`, do not repeat the same sentence in `评分`, `最大风险`, and `替代选择`; refer to the evidence row or summarize the implication.

## Boundary Conditions

| Scenario | Handling |
|---|---|
| Missing budget or region | Ask for it before detailed recommendation; if quick take requested, state assumptions. |
| Current price or availability matters | Browse or use current sources; never rely on stale memory. |
| Product has regional variants | Verify exact SKU/model code before comparing evidence. |
| Only launch reviews exist | Mark confidence low and recommend waiting unless urgency is high. |
| User already owns it | Shift decision to keep/return/repair/replace and consider return window. |
| Evidence conflicts | Explain the conflict, prefer retail/long-term evidence, and lower confidence. |
| Only mainland Chinese sources support an explanatory claim or forecast | Label `local narrative / weakly verified`; do not use it as the sole basis for the conclusion. |
| Non-mainland sources conflict with mainland narratives | Surface the disagreement, prefer independent non-mainland evidence for explanation/forecast, and use mainland sources only for local price/channel color. |
| User asks about a product but need is unclear | Reframe into real need, constraints, and success metric before recommending. |
| Product is in a volatile market | Run market-regime check and include wait-risk, not only current price. |
| Product requires enabling upgrades | Include basket cost, not just product price. |
| Product can be rented or replaced by cloud/service | Compare TCO against rental/cloud/service when utilization is uncertain. |
| User may be overbuying | Present a lower-cost path and the exact capability being sacrificed. |
| Regulated or safety-critical product | Avoid professional advice claims; focus on consumer decision factors and recommend qualified sources where needed. |
| User asks for one-line answer | Give one-line answer plus the single biggest caveat. |
| User asks to evaluate another output | Use audit-trace mode: findings first, no full product recommendation unless requested. |
| Model starts producing both step trace and final answer | Stop and collapse to standard output; keep only one canonical version of each table. |

## Common Mistakes To Prevent

| Mistake | Correction |
|---|---|
| Comparing spec sheets before use case | Start with user fit and constraints. |
| Trusting launch reviews | Prefer retail and long-term evidence. |
| Treating peak benchmark as real performance | Check sustained performance, 1% lows, noise, heat, and throttling. |
| Ignoring ownership cost | Include accessories, subscriptions, repair, warranty, resale, consumables. |
| Treating wait as always good | In shortages or rising input-cost cycles, waiting can increase total cost. |
| Accepting the user's named product as the only solution | Build an option set from the underlying need. |
| Ignoring utilization | Expensive products need cost-per-use or TCO thinking. |
| Using mainland narratives as global explanation | Cross-check with non-mainland independent sources or mark weakly verified. |
| Comparing different regional SKUs | Verify exact model code and market. |
| Recommending the "best" product | Recommend the best fit for this user and timing. |
| Duplicating the analysis trace in the final answer | Use one output mode; step trace is internal unless explicitly requested. |
| Letting stale lifecycle facts drive the conclusion | Run freshness gate before conclusion. |

## Final Check

Before finalizing, verify:

- The conclusion follows from the user's stated use case.
- The user's real need, bottleneck, and success metric were identified or explicitly marked unknown.
- The option space includes target product, lower-cost path, previous-gen/used path, wait/do-nothing path, and adjacent/rental/cloud path when relevant.
- Market regime and wait-risk were considered for volatile categories.
- TCO and threshold price were included for expensive or productivity-linked products.
- Fresh facts were checked when the decision depends on current price, availability, firmware, recalls, or recent complaints.
- Product and alternative lifecycle facts were current as of today's date.
- Explanatory claims and forecasts were supported by non-mainland independent sources, or clearly labeled `local narrative / weakly verified`.
- Evidence confidence is visible.
- Alternatives include at least one cheaper or "do nothing" option when reasonable.
- Output uses one mode only and does not duplicate the 8-step analysis in the final answer.
- Any unresolved fact that could change the decision is listed under `仍需核验`.
