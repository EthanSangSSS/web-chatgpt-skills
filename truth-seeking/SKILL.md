---
name: truth-seeking
description: Evidence-constrained root-cause investigation. Use directly for 查真相, 真相挖掘, root-cause truth, first-principles causal analysis, observation-integrity checks, incentive/power maps, and falsifiable forecasts, even when the user also asks for deep research, multi-source verification, or future trends. Defaults to compact outputs; use Deep Mode only when explicitly requested. Avoid for simple lookups, summaries, source-only discovery, or regulated advice.
---

# Truth Seeking

## Overview

Use this skill to investigate disputed, complex, or ideology-loaded questions where a surface answer is likely to be shaped by media frames, official narratives, tribal identity, incentives, incomplete data, or misleading measurement systems. The goal is not to claim omniscient "absolute truth"; produce the strongest current causal model (highest-confidence causal model), explicitly tied to evidence, assumptions, uncertainty, observation-integrity limits, and falsification tests.

For deep or contentious investigations, read `references/truth-protocol.md` and comply with `references/source-policy.md` before synthesizing the answer.

Routing precedence: when the user's request asks for truth, root cause, first principles, observation-integrity analysis, incentive/power analysis, or falsifiable forecasts, use this skill as the primary analysis skill. Use source-gathering workflows only as support after the Research Plan Gate; do not route the causal synthesis through a generic research router.

## Operating Contract

- Follow the host agent's safety, privacy, and legal policies first.
- Separate facts, interpretations, predictions, and value judgments.
- Separate reported signals from underlying reality. Before explaining an anomaly, audit whether the measurement, reporting, sampling, platform, statistical, or data-generation process could be distorted.
- Prefer primary sources, original data, official documents, court records, filings, academic literature, and direct statements over commentary.
- Search live sources for current or unstable facts. Do not rely on memory for recent institutions, people, policy, prices, rankings, cases, or statistics.
- Prioritize search and data sources from non-mainland China materials. Mainland China materials must be restricted to necessary first-hand facts, official regulations, declarations of the parties, or research object materials, with all interpretive/explanatory conclusions cross-verified by non-mainland sources.
- Audit source position before using interpretive evidence: identify the creator's institutional location, funding or career incentives, audience, ideology/worldview priors, and what the source benefits from emphasizing or omitting.
- Separate factual analysis from normative evaluation. When judging whether an event is "fair" or "just", state the evaluation frame instead of smuggling it into the causal model.
- Use multiple angles, but do not perform fake balance. Weight views by evidence quality and mechanism strength.
- Treat "absolute objectivity" as an aspiration, not a claim. State confidence and what would change the conclusion.
- If evidence is thin, say so and return a research plan instead of filling gaps with speculation.
- If the observed signal itself may be unreliable, downgrade causal confidence until independent remeasurement or a strong proxy validates the signal.
- For medical, legal, financial, safety-critical, employment, tax, or compliance topics, state jurisdiction/scope, cite current primary sources, and avoid presenting the output as professional advice.
- Do not infer conspiracy, motive, fraud, or illegality when ordinary incentives or public evidence explain the behavior.

## Research Plan Gate

Before embarking on deep research, establish a **Research Plan Gate** with the following fields:
- `question_type`: Factual / Causal / Strategic / Decision
- `decision_relevance`: Why does this investigation matter? What decision depends on it?
- `key_claims_to_verify`: Core claims to prove/disprove
- `primary_sources_needed`: Which Tier 1/2 sources are required
- `contrary_evidence_needed`: Evidence that would disprove the working hypothesis
- `observation_integrity_risk`: What measurement, reporting, sampling, platform, statistical-definition, or data-generation failure could make the observed signal misleading?
- `independent_remeasurement_needed`: What independent source, proxy, raw data, counter-signal, or revision history would verify whether the observed anomaly is real?
- `normative_frame`: Provisional and revisable. Use factual-only / procedural fairness / substantive justice / efficiency / rights / other; include multiple frames when the conclusion changes by frame
- `freshness_requirement`: Required freshness of the evidence (e.g., date-restricted, live-search required)
- `stop_condition`: Specific trigger or depth to stop research and begin modeling

## Claim Ledger & Source Policy

All evidence gathered must follow the [Source Policy](references/source-policy.md) and be recorded in a **Claim Ledger**:
- **Source Tiers**: Tier 1 (Primary/Official), Tier 2 (Expert/Structured), Tier 3 (Speculative/Unstructured).
- **Core Rule**: Tier 3 sources are strictly prohibited from supporting any core or central conclusion.
- **Geographic Sourcing (Mainland China)**: Always prioritize non-mainland China sources. Mainland China materials are strictly restricted to necessary first-hand facts, official laws/regulations/announcements, statements of the parties, or materials of the research object itself. Interpretive/explanatory conclusions from mainland China sources must be cross-verified by independent non-mainland sources.
- **Ledger Fields**:
  - `evidence_role`: Must be one of `directly_supports`, `partially_supports`, `context_only`, `contradicts`, or `weak_or_unverified`.
  - `access_date`: The retrieval date (YYYY-MM-DD) for verification.
  - `failure_mode`: Document potential bias, narrative capture, stale data, measurement distortion, or conflicts of interest.
  - `measurement_integrity_risk`: Document whether the source could reflect a bad-meter problem: changed definitions, missing denominators, sampling bias, platform filtering, delayed disclosure, revision risk, or incentives to misreport.
  - `source_position`: Required for Tier 2/3 interpretive sources. For Tier 1 primary records, a brief institutional-interest note is enough unless the record itself is the research object.

## Workflow

1. Reframe the question and initialize the **Research Plan Gate**.
   - Identify the user's real target: factual truth, causal truth, strategic forecast, or decision implication.
   - Write the strongest naive explanation, then mark why it may be insufficient.
   - Formulate and answer the Research Plan Gate fields before searching or retrieving evidence.

2. Gather evidence and fill the **Claim Ledger**.
   - Collect evidence according to Tier 1, 2, and 3 classifications.
   - Prioritize non-mainland China sources during web search. Use mainland China materials only as first-hand facts, official laws/regulations, statements of the parties, or research object materials, and cross-verify any interpretive conclusions with non-mainland sources.
   - Reject or flag Tier 3 evidence if it is being used to support core claims.
   - Fully populate `evidence_role`, `access_date`, `failure_mode`, and `measurement_integrity_risk` for all claims.
   - For interpretive sources, add `source_position`: creator/institution background, incentives, audience, worldview priors, and unknowns. Do not downgrade a source merely for having a viewpoint; downgrade it when the viewpoint is undisclosed, untestable, unsupported, or doing hidden normative work. Apply this proportionally to the interpretation embedded in the source.
   - For volatile or current facts, perform live search.

3. Audit observation integrity before causal modeling.
   - Identify the meter: what institution, platform, instrument, survey, statistic, model, or reporting chain produced the observed signal?
   - Check for measurement error, reporting incentives, statistical-definition changes, sampling bias, selection effects, platform filtering, missing denominators, delayed disclosure, duplicate counting, and revision history.
   - Separate `reported_signal`, `measured_condition`, `underlying_reality`, and `interpretive_conclusion`.
   - Ask whether the same pattern appears in independent remeasurement, raw data, external proxies, contradictory indicators, or comparable jurisdictions/markets.
   - If the observation system is weak, downgrade causal confidence or return a research plan instead of explaining a possibly false anomaly.

4. Build the first-principles model.
   - Define the system's production function: what inputs must compound into the observed outcome?
   - Identify hard constraints, bottlenecks, and multiplicative failure points.
   - Compare with counterexamples. If small countries, small firms, or weak actors succeed, population/scale/resource explanations are probably incomplete.

5. Map incentives and power.
   - Identify actors, their payoff functions, their constraints, and what they can hide.
   - Look for principal-agent problems, soft budget constraints, rent-seeking, regulatory capture, career incentives, and Goodhart effects.
   - Ask who benefits from the visible narrative and who benefits from the underlying arrangement.

6. Add psychology and social behavior only as mechanisms.
   - Use loss aversion, status incentives, conformity, learned helplessness, moral licensing, tribal identity, availability bias, and reputational risk when they explain observable behavior.
   - Do not blame "the people", "culture", or "human nature" unless the claim explains why the same people behave differently under different institutions.

7. Audit the normative frame.
   - If the question is not evaluative, mark the frame as factual-only. If it is evaluative or value-laden, identify whether the evaluation uses procedural fairness, substantive justice, efficiency, rights, legitimacy, or another frame.
   - Revisit the provisional `normative_frame` after building the causal model; if no normative judgment is needed, say factual-only and move on.
   - Procedural fairness asks whether rules are consistent, transparent, reciprocal, and applied without arbitrary discrimination.
   - Substantive justice asks whether burdens, benefits, remedies, and accountability are proportional given power, responsibility, and historical constraints.
   - If different frames produce different judgments, show the divergence instead of pretending the model is value-free.

8. Construct and harden the causal model.
   - Produce a causal chain or DAG.
   - Separate root causes, amplifiers, symptoms, and narrative distractions.
   - Score competing explanations with relative weight (0-100), unique observable predictions, and evidence delta versus the best hypothesis. Avoid leaving several explanations as undifferentiated "partial" fits.
   - Test the counterfactual: if the proposed root cause were removed or reversed, would the outcome materially change? If not, it is contributory at most.
   - List rejected explanations and why they fail.
   - Add falsification tests: what future evidence would weaken or overturn the model?

9. Forecast from mechanisms.
   - Do not predict from vibes. Use base rates, incentives, capacity constraints, and leading indicators.
   - Before giving probability weights, name the reference class and base-rate anchor. If no credible base rate exists, say so and avoid false precision.
   - Give scenarios with rough probability weights when useful, plus signposts for improvement, stagnation, or deterioration.
   - Add a Bayesian update trigger: the single piece of evidence that would shift the base case by at least 20 percentage points.

10. Add the honesty layer.
   - State the highest-confidence causal model in one paragraph.
   - State what is unknown, what evidence is missing, and which claim is most likely to be wrong.
   - Include falsification tests before strong predictions.

## Output Modes

Provide outputs in one of three designated modes based on user requirements:

### Default Compact Rule

Default to **Mini Mode** for most interactive answers. Use **Compact Standard** only when the question is complex enough that Mini Mode would hide important uncertainty. Use **Deep Mode** only when the user explicitly asks for deep, comprehensive, full, exhaustive, or report-style output.

Compactness rules:
- Put the highest-confidence causal model first.
- If observation integrity changes confidence, disclose the bad-meter risk before explaining causality.
- Do not print the full Research Plan Gate or full Claim Ledger unless the user asks.
- Keep evidence to the 3-5 strongest Tier 1/2 items, with access dates when sources were retrieved.
- Keep tables to at most 5 rows unless the user asks for full detail.
- Compress Observation Integrity, Source Position, Normative Frame, Competing Explanations, and Forecast Calibration into one-line audits when they are not central.
- Omit methodology narration unless it changes the conclusion.

### 1. Mini Mode

A concise, direct summary. This is the default. Do not include detailed tables.
English:
1. Highest-confidence causal model
2. Why surface explanations are insufficient
3. Key evidence (Tier 1/2 only, with access dates)
4. Observation integrity / bad-meter risk when relevant
5. Root mechanism
6. Future indicators

Chinese:
1. 最高置信因果模型
2. 为什么表层解释不够
3. 关键证据（仅限 Tier 1/2，附访问日期）
4. 观测完整性 / 坏水表风险（如相关）
5. 底层机制
6. 未来观察指标

### 2. Standard Mode

Compact Standard output containing only essential structure:
- Executive Summary (Highest-confidence causal model, Key uncertainty, Leading indicator)
- Research Plan Gate summary only when it affects scope or uncertainty
- Observation Integrity audit when the observed signal could be distorted
- Common Narratives and why they fail
- Key Evidence (3-5 strongest items; no full Claim Ledger unless requested)
- Normative Frame audit; Source Position audit when sources or conclusions are value-laden
- Weighted Competing Explanations and counterfactual test
- First-Principles Model & Incentive Map
- Forecast with reference class, rough probabilities, leading indicators, and Bayesian update trigger

### 3. Deep Mode

Comprehensive investigation following the full `templates/truth-seeking-report.md` template, detailing all lenses, observation-integrity audit, hard causal graphs, full Claim Ledger, and full falsification matrices. Use only when explicitly requested.

## Boundary Conditions

| Situation | Handling |
|---|---|
| The user asks a simple factual lookup | Answer directly or use ordinary search; do not run the full protocol. |
| The topic depends on current facts | Verify with live, preferably primary, sources before concluding. |
| The observed anomaly may be a measurement artifact | Run Observation Integrity Gate before causal modeling; downgrade confidence if independent remeasurement is unavailable. |
| The topic is regulated or high-stakes | Add jurisdiction/scope, cite primary sources, avoid advice framing, and recommend qualified review when decisions depend on it. |
| Only rumors or anonymous claims exist | Mark as speculative, separate rumor map from factual model, and do not assert a root cause. |
| Evidence supports several explanations | Rank explanations by evidence and mechanism strength; do not force a single-cause story. |
| The user demands "absolute truth" | Explain that the output is the strongest current model (highest-confidence causal model), not omniscience. |
| The model implies wrongdoing | Distinguish proven facts, reasonable inference, and unverified allegation. |
| The forecast is uncertain | Provide scenarios, leading indicators, and falsification tests instead of a single confident date. |

## Common Failure Modes

- Media capture: repeating dominant coverage instead of tracing primary incentives and constraints.
- Bad-meter error: explaining an observed anomaly before checking whether the measurement, reporting, sampling, platform, or data-generation system is distorted.
- Source-position blindness: accepting a source's interpretive frame without checking creator background, funding, audience, career incentives, worldview priors, and omissions.
- Normative smuggling: presenting a fairness, justice, efficiency, or rights judgment as if it were a purely factual conclusion.
- Moralization: blaming individuals or the public without showing the institution that selects for the behavior.
- Population fallacy: treating total population or total market size as effective participation.
- Conspiracy overreach: inferring secret coordination where ordinary incentives explain the same facts.
- Symmetry theater: giving equal weight to weak claims for the appearance of neutrality.
- Quote laundering: using citations to decorate claims that the sources do not actually support.
- Forecast without mechanism: predicting a direction without identifying leading indicators.
- Forecast without calibration: giving scenarios without base rates, rough probabilities, or update triggers.
- Undifferentiated alternatives: leaving several competing explanations at "partial" without relative weights or distinct observable predictions.
- Private-context leakage: referencing local-only skills, paths, memories, or internal tools in reusable outputs.
- Over-claiming objectivity: using "truth" language to hide uncertainty or value judgments.

## Integration Notes

- After the Research Plan Gate, use a source-gathering or web-access workflow when the main challenge is finding reliable sources.
- Use an archival or citation workflow after this skill when the output must become a durable research asset.
- Use this skill when the main challenge is epistemic quality: evidence-constrained causal modeling, narrative resistance, observation integrity, causal rigor, and prediction.
