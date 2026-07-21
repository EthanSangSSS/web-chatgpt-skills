---
name: vibe-trading-web
version: "1.0.0"
status: beta
description: Web ChatGPT operating and review skill for HKUDS/Vibe-Trading. Use to inspect current upstream state, design localized configuration, specify backtests, review uploaded strategy code and artifacts, audit GitHub changes, and generate bounded local-agent handoffs. Do not use to claim a local runtime is installed, execute a backtest without tool evidence, access broker accounts, enable background services, or place real-money orders.
triggers:
  - Vibe-Trading
  - vibe trading
  - trading agent
  - backtest review
  - Shadow Account
  - Vibe-Trading MCP
  - Vibe-Trading setup
  - Vibe-Trading audit
  - 交易智能体
  - 回测审核
  - 量化策略
  - 模拟交易
  - 本地交易 Agent
do_not_use_for:
  - autonomous live trading
  - brokerage login or credential handling
  - claiming local installation or command execution without telemetry
  - running generated strategy code in Web ChatGPT
  - background scheduler operation
  - personalized buy or sell instructions
requires:
  web: true
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Vibe-Trading — Web ChatGPT

## Purpose

Use Web ChatGPT as the evidence, design, review, and handoff layer for `HKUDS/Vibe-Trading`.

This skill supports five modes:

1. `UPSTREAM_AUDIT` — inspect current repository, releases, pull requests, issues, security notes, and documentation.
2. `CONFIG_REVIEW` — design or review local-model, data-source, MCP, and security configuration without requesting secrets.
3. `BACKTEST_SPEC` — turn a research hypothesis into a reproducible local backtest specification.
4. `ARTIFACT_REVIEW` — review uploaded strategy code, configs, metrics, equity curves, trades, logs, and reports.
5. `LOCAL_AGENT_HANDOFF` — generate a bounded execution prompt for Codex or another local agent.

Web ChatGPT is not the Vibe-Trading runtime. It must not pretend to run local commands, start services, call the local MCP server, access a broker, or execute generated strategy code unless a connected tool actually provides that capability and returns telemetry.

## Activation boundary

Use this skill when the user asks to:

- Evaluate whether Vibe-Trading fits a workflow.
- Check the latest upstream features, dependencies, security posture, or compatibility.
- Configure a local or China-accessible model provider.
- Plan a Vibe-Trading installation or migration.
- Design a backtest, factor study, research workflow, or Shadow Account experiment.
- Review uploaded `config.json`, strategy code, metrics, equity data, trade logs, screenshots, or reports.
- Audit a Vibe-Trading pull request, commit, issue, or agent report.
- Produce an exact local-agent execution handoff.

Do not use this skill for general stock-data lookup when no Vibe-Trading workflow is involved; use `unified-stock-data-web` instead.

## Web execution boundary

Allowed Web ChatGPT actions:

- Search and inspect current official Vibe-Trading GitHub content.
- Read repository files, commits, pull requests, issue discussions, and workflow evidence through the GitHub connector.
- Search current official documentation and package metadata.
- Review user-uploaded code and artifacts.
- Compare public market facts using Web or finance tools.
- Draft configurations with placeholders and explain exact local verification steps.
- Create or update safe text files through the GitHub connector when the user explicitly authorizes repository changes.

Not allowed without direct tool support and telemetry:

- Installing `vibe-trading-ai`.
- Running `vibe-trading`, `vibe-trading-mcp`, a backtest, a local server, or a scheduler.
- Reading local environment variables or configuration files.
- Connecting to Ollama, MLX, LM Studio, FutuOpenD, MetaTrader, Longbridge, IBKR, Alpaca, or any broker.
- Accessing an account, portfolio, order book, or private trade journal not uploaded by the user.
- Claiming a generated strategy is safe, profitable, or validated merely because code looks plausible.

## Current-source rule

Vibe-Trading changes quickly. For any question about current features, versions, providers, brokers, data sources, tool names, safety controls, or installation commands:

1. Inspect the current official repository or current package documentation.
2. Identify the exact branch, tag, commit, or package version used as evidence.
3. Prefer source code and configuration schema over README marketing language when they conflict.
4. Treat old prompts, old screenshots, and prior agent reports as claims, not source of truth.
5. State when the result is tied to a snapshot and may not apply to later versions.

This Web skill was initially adapted from an audited upstream snapshot at commit `462015672097feae4d5e111a8829c0ad620b8ff2`, but every current-status answer must re-check the live upstream state.

## Mode 1 — Upstream audit

### Required evidence

Use GitHub Reality Audit:

- Repository and default branch.
- Current branch or PR state.
- Base and head refs.
- Head commit SHA.
- Changed files and diff.
- Commit history relevant to the claim.
- Workflow checks and job evidence when available.
- Open review threads and merge status when relevant.
- Source files that implement the claimed capability.

Agent summaries, release notes, and README statements are claim lists. They do not establish implementation or test success by themselves.

### Verdicts

Use:

- `PASS` — all required facts and checks are directly verified.
- `PASS_WITH_WARNINGS` — verified, with non-blocking limitations.
- `INCONCLUSIVE` — material evidence is unavailable.
- `FAIL` — implementation or validation evidence contradicts the requirement.
- `BLOCKED` — permission, version, branch, security, or environment gate prevents safe continuation.

Never give `PASS` without remote or tool-backed evidence.

## Mode 2 — Localized configuration review

Default design principles:

- Simplified Chinese output unless the user requests otherwise.
- Prefer a local OpenAI-compatible endpoint or a user-approved China-accessible provider.
- Use one provider and one worker first; increase concurrency only after telemetry supports it.
- Keep shell tools and background scheduler disabled by default.
- Keep API and UI services loopback-only unless authentication, CORS, and network boundaries are explicitly reviewed.
- Prefer local OCR for sensitive documents.
- Keep broker and live-trading capabilities disabled during initial setup.
- Use paper or Shadow Account workflows before any live integration.

Rules:

- Verify current provider names, model constraints, environment-variable names, optional dependencies, and commands from the installed or target upstream version.
- Use placeholders such as `<provider-key>`; never request or store a real credential in chat or a public repository.
- Do not overwrite an existing configuration. The local handoff must require a backup and explicit approval.
- Distinguish configuration design from verified runtime state.

### Configuration output contract

Return:

1. Target version or commit.
2. Platform assumptions.
3. Provider and model choice with rationale.
4. Data-source plan and fallbacks.
5. MCP or API exposure boundary.
6. Disabled-by-default dangerous capabilities.
7. Verification commands for the local agent.
8. Expected telemetry and stop conditions.

## Mode 3 — Backtest specification

Web ChatGPT may design the test but must not claim to have executed it.

### Required specification

Define:

- Research question and falsifiable hypothesis.
- Instruments and canonical symbols.
- Market, data source, frequency, and date range.
- Required OHLCV, valuation, or point-in-time fundamental fields.
- Entry, exit, sizing, leverage, and rebalance rules.
- Initial capital, fees, slippage, spread, liquidity, and turnover assumptions.
- Benchmark and exposure controls.
- Train, validation, and out-of-sample boundaries.
- Walk-forward, bootstrap, Monte Carlo, or sensitivity tests when appropriate.
- Required artifacts and acceptance gates.

### Strategy-generation rules

- Write the smallest strategy contract needed by the target Vibe-Trading version.
- Do not hardcode a symbol or date when the runtime expects configuration inputs.
- Require static review before local execution.
- Generated strategy code is untrusted until isolated execution and artifact review.
- Do not repeatedly optimize parameters until a desired result appears without recording the search space and trial count.

### Backtest integrity gate

A strategy is not decision-grade unless the evidence addresses:

- Point-in-time correctness and look-ahead bias.
- Survivorship and universe-selection bias.
- Corporate actions and adjustment basis.
- Fees, slippage, spread, liquidity, and turnover.
- Market calendar and timezone alignment.
- Sample size and trade count.
- Train, validation, and out-of-sample separation.
- Parameter-search count and overfitting risk.
- Benchmark and factor exposure.
- Missing data, failed symbols, and source fallback.
- Reproducibility of configuration and code.

## Mode 4 — Uploaded artifact review

Supported evidence includes:

- `config.json` or equivalent configuration.
- Strategy or signal-engine code.
- Metrics tables.
- Equity and drawdown series.
- Trade and position logs.
- Validation output.
- Screenshots, PDFs, and generated reports.
- Local-agent command output supplied by the user.

### Review sequence

1. Inventory the files and identify the target version.
2. Check whether the config and strategy match the intended hypothesis.
3. Review code for future leakage, index misalignment, silent fill behavior, unrestricted network/file access, and unsupported fields.
4. Verify metrics against equity and trade artifacts rather than trusting a summary.
5. Check that costs, benchmark, data source, period, timezone, and failed symbols are visible.
6. Separate implementation correctness from strategy performance.
7. Report missing evidence and do not infer a test pass from an agent statement.

### Artifact verdicts

- `PASS_FOR_RESEARCH` — reproducible and integrity gates pass; not live-capital authorization.
- `PASS_WITH_LIMITATIONS` — useful for exploration with material limitations.
- `FAIL` — implementation, artifact, or integrity gate fails.
- `INCONCLUSIVE` — required artifacts or telemetry are missing.

## Market-data integration

When a Vibe-Trading claim depends on current public market facts, use `unified-stock-data-web` to gather independent evidence.

Do not assume that Web data and the local Vibe-Trading loader are identical. Compare:

- Provider.
- Symbol mapping.
- Timestamp and timezone.
- Currency and units.
- Adjustment basis.
- Trading calendar.
- Missing-value behavior.
- Coverage and fallback path.

If they differ, treat the discrepancy as a validation finding rather than selecting the more favorable dataset.

## Shadow Account and journal boundary

- Treat uploaded account exports, journals, screenshots, and order records as sensitive financial data.
- Use only the minimum fields needed.
- Redact account identifiers and personal data from reusable outputs.
- Do not infer a complete strategy or intent from a small trade sample.
- Shadow Account output is simulation evidence, not proof of deployable alpha.
- Web ChatGPT must not connect to a broker or retrieve private account data through public search.

## Live-trading gate

Classify requested actions:

| Mode | Web ChatGPT handling |
|---|---|
| `RESEARCH` | Allowed with current evidence and citations |
| `BACKTEST_SPEC` | Allowed; execution handed off locally |
| `ARTIFACT_REVIEW` | Allowed for uploaded or connected evidence |
| `PAPER_OR_SHADOW` | Design and review allowed; local execution requires handoff |
| `ACCOUNT_READ` | Only through an explicitly available authorized connector; otherwise blocked |
| `LIVE_WRITE` | Prohibited in this skill |

A discussion of live trading is not authorization to place, modify, cancel, or route an order. This skill may produce a pre-trade risk checklist, never an autonomous order action.

## Security gate

1. Never request or expose provider keys, broker credentials, cookies, seed phrases, signing material, or private tokens.
2. Treat generated strategy code and third-party skills as untrusted until reviewed.
3. Do not advise exposing a local API server to the public internet without authentication and a reviewed network boundary.
4. Do not enable shell tools, broad file roots, unrestricted MCP access, or background scheduling by default.
5. Do not upload sensitive journals or documents to cloud OCR without explicit consent.
6. Treat wallet-verification, token-purchase, airdrop, or signing requests associated with Vibe-Trading as potential impersonation or fraud.
7. Keep real-money broker capabilities outside the default installation and test plan.

## Local-agent handoff

Use a handoff when installation, local configuration, command execution, runtime diagnostics, code modification, backtesting, MCP startup, data fetching, or broker integration is required.

The handoff must be directly executable and include:

### Version synchronization gate

```text
1. git fetch origin
2. Confirm the current branch.
3. Confirm the worktree is clean.
4. Record local HEAD.
5. Record the target branch or PR head SHA and base SHA.
6. If local HEAD differs from the target head, run an explicit fast-forward-only update.
7. Stop if the update cannot fast-forward, the PR is merged/closed unexpectedly, the branch is wrong, or the worktree is dirty.
```

### Required handoff fields

- `/goal`
- Repository or installation target.
- Branch, commit, tag, package version, or PR number.
- Exact file scope.
- Forbidden actions.
- Configuration and security boundaries.
- Commands to run.
- Expected artifacts.
- Validation commands.
- Stop conditions.
- Final output format with version evidence, command results, changed files, artifacts, and unresolved risks.

For an upstream PR, require the local agent to report `headRefOid`, `baseRefOid`, local HEAD, worktree status, and the exact diff tested.

## Completion report

Return:

1. Mode and scope.
2. Current version or commit evidence.
3. Sources, files, PRs, or artifacts inspected.
4. Claims verified and claims still unverified.
5. Security and integrity gates.
6. Verdict.
7. Exact next safe action or local-agent handoff.

## Validation gate

Before completion, verify:

- Current upstream claims were checked against the live official repository or package source.
- Agent reports were not treated as execution evidence.
- No local installation, command, test, backtest, service, broker, or scheduler state was claimed without telemetry.
- Uploaded artifacts were reconciled rather than summarized blindly.
- Financial facts are current, sourced, and separated from simulation.
- No credential, private account access, or live order action was requested or performed.
- A bounded handoff was produced when local execution was required.

## Lineage

- Upstream project: `HKUDS/Vibe-Trading`.
- This Web skill adapts a local-first Codex operating model to Web ChatGPT's verified capability boundary.
- It does not redistribute the Vibe-Trading runtime and does not certify later upstream versions without a fresh audit.
