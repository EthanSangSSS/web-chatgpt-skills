# Truth-Seeking Protocol

Use this reference for deep investigations where the user rejects surface explanations and wants a first-principles, multi-disciplinary, prediction-oriented answer.

## Core Promise

Truth-seeking does not mean claiming final truth. It means producing the strongest evidence-constrained causal model available now, plus the uncertainty, observation-integrity limits, missing evidence, and observations that could overturn it.

## Truth Types

| Type | Question | Output |
|---|---|---|
| Factual truth | What happened? | Timeline, facts, source tiers |
| Observational truth | Is the signal real? | Measurement method, sample frame, denominator, revision risk |
| Causal truth | Why did it happen? | Mechanism, bottleneck, causal graph |
| Strategic truth | What will happen next? | Scenarios, leading indicators |
| Decision truth | What should the user do? | Options, tradeoffs, triggers |

Do not mix these types. A true fact can support a false causal story; a reported signal can be a misleading measurement; a good causal model can still produce uncertain forecasts.

## Fast Classification

Before doing a full investigation, classify the request:

| User need | Use full protocol? | Response mode |
|---|---:|---|
| One factual answer | No | Direct answer with source if needed |
| Current legal/tax/medical/financial fact | Partial | Primary-source verification + scope warning |
| "Why is this really happening?" | Yes | Causal model |
| "Is this sudden change real?" | Partial/Yes | Observation Integrity Gate + evidence check |
| "What will happen next?" | Yes | Mechanism-based forecast |
| "What should I do?" | Yes | Decision implications with assumptions |
| "Is this rumor true?" | Partial | Rumor/fact separation |

## Research Plan Gate

Before starting deep research, formulate a Research Plan Gate using the following fields:
- `question_type`: Factual / Observational / Causal / Strategic / Decision
- `decision_relevance`: Why does this matter? What decision is riding on this?
- `key_claims_to_verify`: Core claims that must be proved/disproved to evaluate the model
- `primary_sources_needed`: Which Tier 1 / official sources are required
- `contrary_evidence_needed`: What evidence would disprove the main hypothesis
- `observation_integrity_risk`: What measurement, reporting, sampling, platform, statistical-definition, or data-generation failure could make the observed signal misleading?
- `independent_remeasurement_needed`: What independent source, proxy, raw data, counter-signal, or revision history would verify whether the observed anomaly is real?
- `normative_frame`: Provisional and revisable. Use factual-only / procedural fairness / substantive justice / efficiency / rights / other; include multiple frames when the conclusion changes by frame
- `freshness_requirement`: Required freshness of the evidence (e.g., date-restricted, live-search required)
- `stop_condition`: When to stop researching (e.g., finding the primary filing, resolving the bottleneck, running out of search depth)

## Lens Checklist

Use only lenses that improve explanatory power.

1. First principles: what is the outcome's production function?
2. Incentives: who is rewarded, punished, protected, or made disposable?
3. Institutions: what rules exist, who enforces them, and where is discretion hidden?
4. Power: who can block change, allocate resources, grant access, or bury evidence?
5. Money: where are revenue, debt, subsidies, rents, and externalized costs?
6. Selection effects: who enters, exits, survives, and gets counted?
7. Psychology: what fears, status pressures, biases, or identity costs shape behavior?
8. Information: who knows what, who can verify what, and where are feedback loops broken?
9. Observation integrity: what produced the signal, what could distort it, and how can it be independently remeasured?
10. Time horizon: which actors optimize for weeks, quarters, election cycles, career cycles, or decades?
11. Comparative cases: where did a similar system succeed or fail, and which variable differs?
12. Historical path dependence: what earlier decisions locked in today's constraints?
13. Narrative incentives: why is the popular explanation emotionally or politically convenient?
14. Source position: how do creator background, institutional location, funding, audience, and worldview priors shape the interpretation? Apply proportionally to the degree of interpretation embedded in the source.
15. Normative frame: is the evaluation based on factual accuracy, procedural fairness, substantive justice, efficiency, rights, legitimacy, or another standard?

## Observation Integrity Gate

Before explaining an anomaly, verify whether the observed signal is a valid reading of underlying reality or a bad-meter event produced by the measurement system.

Use this gate whenever the claim depends on a sudden change, official statistic, platform trend, media-visible sample, corporate disclosure, survey result, sensor/model output, benchmark, ranking, or KPI.

| Check | Question | Typical Failure Mode |
|---|---|---|
| Meter | What produced the signal? | Treating a platform/media/statistical reading as direct reality |
| Definition | Did the metric definition, threshold, or classification change? | Definition drift mistaken for real change |
| Denominator | Is the base population known and comparable? | Missing denominator or moving denominator |
| Sample frame | Who is excluded, delayed, duplicated, or overrepresented? | Selection bias / survivorship bias |
| Reporting incentive | Who benefits from a better/worse/louder/quieter reading? | Incentive-compatible misreporting or selective disclosure |
| Revision history | Has the number been revised before? | Current reading may be provisional |
| Independent remeasurement | What external proxy or raw data can check it? | No independent way to distinguish signal from measurement artifact |

Required distinction:

| Layer | Meaning |
|---|---|
| Reported signal | What a source, platform, statistic, or institution says is happening |
| Measured condition | What the measurement process can actually observe |
| Underlying reality | The real-world condition the user cares about |
| Interpretive conclusion | The causal or predictive story built on top of the signal |

If observation integrity is weak, do not immediately explain the anomaly. State that the signal may be measurement-driven, downgrade confidence, and specify what independent remeasurement would be needed.

## Causal Hardening Questions

- If this explanation is true, what else should be observable?
- If this explanation is false, what evidence would likely exist?
- What does the explanation fail to explain?
- What counterexample is most damaging?
- If two explanations both partially fit, which one predicts more unique observable implications?
- What is the evidence delta or rough likelihood ratio between the best hypothesis and the runner-up?
- Counterfactual test: if the proposed root cause were removed or reversed, would the outcome materially change?
- Does the model explain why this problem happens in this domain but not adjacent domains?
- Does it explain why small or weak actors can outperform large or rich actors?
- Does it distinguish root cause from symptom, amplifier, and trigger?
- Could ordinary incentives explain the behavior without assuming secret coordination?
- Are there missing base rates or denominators?
- Are we overweighting visible scandals because invisible normal operation is harder to observe?
- Are we explaining a real change, or a change in measurement, reporting, sampling, visibility, or platform selection?

## Evidence Discipline & Source Policy

All evidence collection and evaluation must follow the [Source Policy](source-policy.md):
- **Tiers**: Tier 1 (Primary/Official), Tier 2 (Expert/Structured), Tier 3 (Speculative/Unstructured).
- **Core Rule**: Tier 3 evidence is strictly prohibited from supporting any core/central conclusions.
- **Geographic Sourcing (Mainland China)**: Always prioritize non-mainland China sources. Mainland China materials are strictly restricted to necessary first-hand facts, official laws/regulations/announcements, statements by the parties involved, or materials of the research object itself. Interpretive/explanatory conclusions from mainland China sources must be cross-verified by independent non-mainland sources.
- **Claim Ledger Requirements**:
  - Assign `evidence_role`: `directly_supports`, `partially_supports`, `context_only`, `contradicts`, or `weak_or_unverified`.
  - Record `access_date` (YYYY-MM-DD) for all evidence.
  - Identify `failure_mode` (potential bias, narrative capture, stale data, measurement distortion, etc.) for each source.
  - Identify `measurement_integrity_risk` when a source is used to support an observed anomaly, trend, benchmark, ranking, or KPI.
  - For interpretive sources, identify `source_position` (creator/institution background, incentives, audience, worldview priors, and unknowns).

| Evidence type | Use | Risk |
|---|---|---|
| Primary records | Anchor facts, dates, numbers, formal positions | Can reflect institutional self-presentation or reported-signal limits |
| Court/discipline records | Strong for proven misconduct | Reveals detected cases, not full prevalence |
| Academic papers | Mechanism and historical analysis | May lag current facts or use narrow datasets |
| Industry data | Market structure and incentives | May be proprietary, incomplete, or biased |
| Investigative reporting | Hidden mechanisms and actor detail | Needs cross-checking |
| Opinion/commentary | Narrative map | Weak evidence for truth claims |
| Social media | Early signal and sentiment | High noise, manipulation risk |

## Normative Frame Audit

Facts and causal mechanisms do not automatically answer whether an event is fair, just, efficient, legitimate, or rights-respecting. When the user asks for an evaluation, or when the topic is value-laden, state the frame being used:

| Frame | Core question | Typical evidence |
|---|---|---|
| Factual accuracy | What happened, and what caused it? | Records, timelines, mechanisms |
| Procedural fairness | Were rules consistent, transparent, reciprocal, and non-arbitrary? | Rules, process records, access criteria, comparables |
| Substantive justice | Are burdens, benefits, remedies, and accountability proportional given power and responsibility? | Distributional impact, harmed groups, power asymmetry, remedy design |
| Efficiency | Does the arrangement produce more value than alternatives after costs and externalities? | Costs, incentives, opportunity costs, counterfactuals |
| Rights / legitimacy | Does the action respect basic rights, consent, representation, and due process? | Legal principles, rights standards, consent and appeal mechanisms |

If two frames produce different conclusions, report both. Do not hide a normative judgment inside causal language.

## Regulated And High-Stakes Topics

For medical, legal, tax, employment, finance, safety, or compliance questions:

1. State the jurisdiction, date, and scope.
2. Prefer current primary sources: statutes, regulations, official agencies, filings, court records, or authoritative standards.
3. Separate legal/tax/compliance facts from business judgment.
4. Avoid "you should" unless the action is low-risk and clearly supported.
5. Tell the user what a qualified professional would need to verify before action.

## Confidence Labels

| Label | Meaning |
|---|---|
| High | Primary sources or strong multi-source evidence directly support the claim |
| Medium-high | Evidence is strong, but some mechanism links are inferred |
| Medium | Plausible model with partial evidence or imperfect comparables |
| Low | Hypothesis only; useful for monitoring, not conclusion |
| Unknown | Evidence is insufficient or contradictory |

## Output Template

Use this structure for substantial reports:

```markdown
## Research Plan Gate
- **Question Type**: ...
- **Decision Relevance**: ...
- **Key Claims to Verify**: ...
- **Primary Sources Needed**: ...
- **Contrary Evidence Needed**: ...
- **Observation Integrity Risk**: ...
- **Independent Remeasurement Needed**: ...
- **Normative Frame**: ...
- **Freshness Requirement**: ...
- **Stop Condition**: ...

## Executive Summary
最高置信因果模型: ...
关键不确定性: ...
观测完整性风险: ...
未来最重要观察点: ...

## Common Narratives And Why They Are Incomplete
| Narrative | What it gets right | Where it fails |

## Claim Ledger
*All sources must comply with the Source Policy. Tier 3 sources are strictly prohibited from supporting core/central conclusions.*
| Claim | Source | Tier | Evidence Role | Access Date | Failure Mode | Measurement Integrity Risk | Source Position | Confidence |

## Observation Integrity Audit
| Reported Signal | Meter / Data-Generation Process | Distortion Risk | Independent Remeasurement Needed | Confidence Impact |
|  |  |  |  |  |

## Source Position Audit
| Source | Creator / Institution | Incentives | Audience | Worldview Priors | Omissions / Risk |
|  |  |  |  |  |  |

## Normative Frame Audit
Primary frame:
Alternative frames:
Where conclusions diverge by frame:

## Unknowns And Assumptions
Known unknowns:
Assumptions:
Most fragile claim:

## First-Principles Model
Production function:
Outcome = A x B x C x D

Binding bottleneck:
...

## Incentive And Power Map
| Actor | Public goal | Private payoff | Constraint | Observable behavior |

## Causal Model
Root causes:
Amplifiers:
Symptoms:
Narrative distractions:

## Competing Explanations
| Explanation | Verdict | Relative Weight (0-100) | Unique Observable Predictions | Evidence Delta vs. Best Hypothesis | Reason |

## Falsification Tests
1. ...

## Forecast
Base case:
Base-rate / reference-class anchor:
Rough probability weights:
Upside case:
Downside case:
Leading indicators:
Bayesian update trigger:

## Source Gaps
...
```

## Output Modes

Choose the output mode based on the user's preference or the depth of the investigation:

### Default Compact Rule

Default to Mini Mode for most interactive answers. Use Compact Standard only when a concise answer would hide important uncertainty. Use Deep Mode only when the user explicitly requests a comprehensive, exhaustive, full-report, or full-template answer.

Compact outputs should:
- State the highest-confidence causal model first.
- State observation-integrity risk early when the observed signal may be distorted.
- Include only the evidence and caveats that change the conclusion.
- Avoid printing full ledgers unless requested.
