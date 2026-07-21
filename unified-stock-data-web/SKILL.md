---
name: unified-stock-data-web
version: "1.0.0"
status: beta
description: Web ChatGPT workflow for evidence-bounded public-market data research across mainland China A-shares, US equities, and Hong Kong equities. Use for current quotes, K-lines, filings, fundamentals, announcements, options, technical calculations, market screening, and cross-market comparisons when live web or finance tools are available. Do not use for brokerage access, real-money order execution, personalized buy/sell instructions, or claims of bulk/local data extraction without tool evidence.
triggers:
  - stock data
  - market data
  - stock quote
  - K-line
  - financial statements
  - SEC filing
  - HKEX announcement
  - A-share data
  - US stock data
  - Hong Kong stock data
  - 股票数据
  - 行情
  - K线
  - 财报
  - 公告
  - 资金流
  - 美股
  - 港股
  - A股
do_not_use_for:
  - generic finance concepts without a data request
  - brokerage login or account access
  - real-money trading or order placement
  - personalized investment advice
  - high-volume scraping that requires local code execution
  - claiming an endpoint works without observed tool telemetry
requires:
  web: true
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Unified Stock Data — Web ChatGPT

## Purpose

Use Web ChatGPT's available public-information tools to retrieve, normalize, compare, and explain stock-market data for:

- Mainland China A-shares, listed ETFs, indices, and publicly disclosed exchange/company information.
- US equities, ETFs, listed options, SEC filings, and public fundamentals.
- Hong Kong equities, HKEX filings, company announcements, and public fundamentals.

This is a research and evidence-routing skill. It is not a brokerage connector, autonomous trading agent, or substitute for regulated financial advice.

## Web execution boundary

Web ChatGPT may use only capabilities actually available in the current conversation, including:

- Dedicated finance or market-price tools.
- Web search and page retrieval.
- Official-company, exchange, regulator, and filing websites.
- PDF parsing and page screenshots when a PDF contains tables, charts, or figures.
- GitHub connector data for reviewing public source code or upstream data-tool documentation.
- User-uploaded files for comparison or analysis.

Web ChatGPT must not claim that it:

- Ran arbitrary Python against public APIs unless an actual execution tool returned the result.
- Accessed the user's local terminal, local database, local cache, browser session, or private credentials.
- Queried a brokerage account or placed an order.
- Completed a bulk market crawl, backtest, or local export without direct tool evidence.

When the task requires those capabilities, produce a bounded local-agent handoff instead.

## Activation boundary

Use this skill when the answer depends on actual public-market data, including:

- Current or historical price, volume, market cap, valuation, or technical indicators.
- Financial statements, earnings releases, guidance, analyst estimates, or institutional holdings.
- SEC, HKEX, SSE, SZSE, BSE, CNINFO, or company announcements.
- Options chains, expiries, open interest, implied volatility, or contract comparisons.
- Capital-flow, margin-financing, northbound-flow, sentiment, or market-ranking data.
- Cross-market comparisons requiring currency, timezone, calendar, or accounting normalization.

Do not activate for a simple explanation such as "what is PE" unless live data is also requested.

## Required request model

Infer or obtain the minimum required fields:

1. Instrument, company, index, ETF, or search term.
2. Market: `A_SHARE`, `US`, `HK`, or `CROSS_MARKET`.
3. Capability: quote, K-line, technical calculation, fundamentals, filing, announcement, options, flow, news, sentiment, or screen.
4. Time range and interval when material.
5. Adjustment basis, currency, and output format when material.
6. Freshness requirement: current, latest filing, specified date, or historical period.

Do not block on optional details. Use conservative defaults and state them.

## Step 1 — Resolve the instrument

Never assume a market solely from an ambiguous company name or numeric code.

| Input pattern | Likely market | Canonical examples |
|---|---|---|
| Six-digit mainland code or `.SH` / `.SZ` / `.BJ` | A-share | `600519.SH`, `000001.SZ`, `430047.BJ` |
| Three-to-five-digit code or `.HK` | Hong Kong | `0700.HK`, `9988.HK` |
| Alphabetic exchange ticker | US | `AAPL`, `TSLA`, `BRK-B` |

Rules:

- Confirm ambiguous symbols through an official listing page, exchange page, or reliable symbol-search source.
- Preserve class-share punctuation and exchange suffixes.
- Record the user's original symbol separately from the resolved canonical symbol.
- If symbol resolution remains uncertain, stop and state the ambiguity instead of returning another security's data.

## Step 2 — Choose sources by evidence role

### Source hierarchy

Use the strongest source appropriate to the field:

1. **Dedicated market-price tool** for current price or price chart when supported.
2. **Primary official source**: regulator, exchange, filing system, issuer investor-relations page, or official announcement.
3. **Structured market-data source** with visible timestamp, field definitions, and coverage.
4. **Reputable financial media** for event context, not as the sole source for primary financial fields.
5. **Community or social sources** only as discovery leads; never use them alone for a core conclusion.

When a dedicated price tool and a normal webpage disagree on a current quote, treat the dedicated price tool as the current-price source of truth and explain likely delay, session, currency, or symbol differences.

### A-share route

Prefer:

- SSE, SZSE, and BSE for listing status, exchange notices, and official market documents.
- CNINFO and issuer announcements for filings and corporate actions.
- Official reports or issuer disclosures for financial statements.
- Public quote sources only with explicit timestamp, market session, unit, and delay caveats.

A-share-specific checks:

- Distinguish Shanghai, Shenzhen, Beijing, index, ETF, and convertible-bond codes.
- Label price-adjustment basis.
- Do not treat incomplete intraday northbound-flow data as a complete historical series.
- Treat research ratings, popularity rankings, and capital-flow classifications as provider-defined signals.

### US route

Prefer:

- SEC EDGAR and issuer investor-relations pages for filings and reported fundamentals.
- The dedicated finance tool for current price and chart data when supported.
- Exchange or issuer sources for corporate actions.
- Listed-options sources with explicit expiry, strike, quote time, and contract multiplier.

US-specific checks:

- Separate GAAP reported values, non-GAAP measures, analyst estimates, and guidance.
- Distinguish annual, quarterly, TTM, and point-in-time values.
- Treat options Greeks and implied volatility as model-dependent fields.

### Hong Kong route

Prefer:

- HKEXnews and issuer investor-relations pages for announcements and reports.
- The dedicated finance tool or structured public source for current price when supported.
- Official documents for share counts, corporate actions, and reporting periods.

Hong Kong-specific checks:

- Preserve leading-zero semantics where relevant.
- Label HKD and any alternate trading currency.
- Distinguish fiscal-year reporting periods from calendar-year periods.

## Step 3 — Retrieve and verify

For every material claim:

1. Verify current or unstable facts with live search.
2. Inspect the returned timestamp, trading date, market session, currency, unit, and source.
3. Open the primary document when a search result only summarizes it.
4. For PDFs containing tables, charts, or figures, inspect the relevant page with a screenshot rather than relying only on parsed text.
5. Cross-check material values with an independent source when practical.
6. Record disagreement rather than averaging incompatible values.

A failed search or empty page is not evidence that no data exists. Classify the failure:

- `NO_PUBLIC_DATA_FOUND`
- `SOURCE_BLOCKED`
- `RATE_LIMITED`
- `SCHEMA_OR_PAGE_CHANGED`
- `INVALID_OR_AMBIGUOUS_SYMBOL`
- `DATE_OR_COVERAGE_GAP`
- `TOOL_NOT_AVAILABLE`

## Step 4 — Normalize before comparison

Before comparing instruments or markets, normalize:

- Currency and FX date.
- Market timezone and trading session.
- Trading calendar and observation date.
- Raw, forward-adjusted, or backward-adjusted price basis.
- Volume, turnover, shares, market-cap, and monetary-unit scaling.
- Annual, quarterly, TTM, forecast, and point-in-time periods.
- GAAP, IFRS, local accounting standards, and company-defined non-GAAP measures.
- Split, dividend, rights issue, and other corporate actions.

Preserve raw source values. Put conversions and calculations in a separate `derived` section.

## Step 5 — Separate evidence from interpretation

Use four labels when useful:

- `FACT`: directly observed public data or filing content.
- `DERIVED`: deterministic calculation from stated inputs.
- `THIRD_PARTY_SIGNAL`: analyst rating, provider-defined flow, ranking, sentiment, or model output.
- `INTERPRETATION`: a reasoned explanation with uncertainty.

Technical indicators are calculations over a selected series. They are not predictions. One indicator, one news item, or one analyst target must not be converted into a certain buy/sell conclusion.

## Result envelope

For structured work, use:

```json
{
  "request": {
    "market": "A_SHARE|US|HK|CROSS_MARKET",
    "input_symbol": "...",
    "canonical_symbol": "...",
    "capability": "quote|kline|fundamentals|filing|options|..."
  },
  "data": {},
  "provenance": [
    {
      "source": "official or structured source",
      "source_role": "primary|price_tool|secondary|discovery",
      "as_of": "ISO-8601, trading date, or null",
      "timezone": "Asia/Shanghai|America/New_York|Asia/Hong_Kong|unknown",
      "currency": "CNY|USD|HKD|unknown",
      "delay_status": "real_time|delayed|end_of_day|unknown",
      "coverage": "...",
      "status": "ok|partial|empty|blocked|changed|invalid"
    }
  ],
  "derived": {},
  "caveats": [],
  "errors": []
}
```

Do not fabricate metadata. Use `null` or `unknown` and explain the limitation.

## User-facing output contract

Return:

1. Resolved instrument and market.
2. Requested data with units and period.
3. Source, timestamp or trading date, timezone, currency, and delay caveats.
4. Any fallback, disagreement, or missing coverage.
5. A clear boundary between facts, calculations, third-party signals, and interpretation.
6. A financial-risk boundary when the user may act on the result.

Use citations for all non-trivial current facts. Do not provide unsupported precision.

## Bulk-data and local-agent handoff

Hand off when the task requires:

- Running third-party endpoint code.
- Fetching many instruments or long high-frequency histories.
- Local caching, database writes, or large exports.
- Authentication-bound datasets.
- Repeated retries, scraping, or provider-specific session handling.
- Backtesting or executing generated strategy code.

The handoff must include:

- Goal and exact instruments.
- Required fields, period, interval, and adjustment basis.
- Preferred and fallback sources.
- Rate-limit and write constraints.
- Validation checks.
- Expected output schema.
- Stop conditions for blocks, schema changes, ambiguous symbols, or missing coverage.

Never ask the user to paste credentials into chat.

## Validation gate

Before completion, verify:

- The market and symbol are resolved.
- Current facts were checked live.
- Primary documents were opened when material.
- PDF visuals were inspected when relevant.
- Source timestamps, units, currencies, periods, and adjustment basis are explicit.
- Source disagreement and missingness are visible.
- No local execution, bulk extraction, endpoint availability, or test result was claimed without tool evidence.
- No brokerage access, real-money order, or personalized investment instruction was performed.

## Lineage

This Web ChatGPT skill is adapted from the unified routing and integrity model developed from:

- `simonlin1212/a-stock-data`
- `simonlin1212/global-stock-data`

Those upstream projects contain local executable endpoint implementations. This Web version does not embed or claim to execute those implementations; it applies their market-routing concepts within the verified Web ChatGPT capability boundary.
