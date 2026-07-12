# Source Policy

Use this policy whenever the product decision depends on web search, media reviews, community user feedback, research, market interpretation, or prediction.

## Jurisdiction Priority

Default source priority:

1. Primary technical sources: official specs, manuals, regulatory filings, warranty terms, driver/firmware release notes.
2. Non-mainland-China independent reviews and testing: retail-unit reviews, lab tests, teardown sites, long-term reviews, international specialist forums.
3. Non-mainland community feedback: Reddit, overseas forums, GitHub issues, repair forums, owner communities, marketplace reviews with clear purchase signals.
4. Mainland China local signals: ecommerce prices, local stock, warranty/channel constraints, Xiaohongshu/Tieba/Bilibili/Zhihu sentiment, mainland KOL/media.
5. Manufacturer marketing, sponsored content, affiliate listicles, reposted summaries.

The user's local market may be mainland China, but explanatory analysis should not be built only from mainland narratives.

## Hard Rule

For media reviews, community feedback, online research, and explanatory analysis:

- Always prefer non-mainland-China independent sources first.
- Mainland Chinese media, comments, official interpretations, ecommerce pages, and KOL narratives cannot alone support explanatory conclusions or forecasts.
- If only mainland sources are available, label the claim `local narrative / weakly verified`.
- Use mainland sources mainly for local price, availability, SKU differences, warranty/channel policy, and local user complaints.

## Claim Labels

| Label | Meaning |
|---|---|
| `verified` | Supported by primary sources or multiple independent sources, including non-mainland evidence when interpretive. |
| `mixed` | Credible sources disagree or evidence differs by region/SKU/batch. |
| `local narrative / weakly verified` | Supported mainly by mainland Chinese media/community/official interpretation and not cross-verified independently. |
| `unverified` | Plausible but not supported by adequate evidence. |
| `false / contradicted` | Stronger evidence contradicts it. |

## Search Pattern

For a product or market claim, search in this order:

1. Official spec/support pages: `<model> official specs`, `<model> firmware issue`, `<model> warranty`.
2. Independent non-mainland reviews: `<model> review retail unit`, `<model> long term review`, `<model> teardown`, `<model> latency thermal power`.
3. Non-mainland communities: `<model> reddit problems`, `<model> forum issue`, `<model> owner review`.
4. Market context: `<category> shortage`, `<component> price trend`, `<component> supply demand`, `<category> tariff`, `<category> recall`.
5. Mainland/local sources for local reality: `<model> 京东 价格`, `<model> 淘宝 现货`, `<model> 国行 保修`, `<model> 通病`, `<model> 翻车`.

## Output Requirement

When evidence quality matters, include a short source posture:

```markdown
**来源姿态**
- Non-mainland independent sources checked: ...
- Mainland/local narrative used for: ...
- Weakly verified claims: ...
```

If the final conclusion depends on a weakly verified claim, say so directly and lower confidence.
