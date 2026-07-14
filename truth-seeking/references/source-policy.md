# Source Policy & Credibility Guide

This policy establishes strict standards for source evaluation, evidence role assignment, observation-integrity review, and validation requirements for all evidence-constrained causal models.

## 1. Source Hierarchy (Tiers)

- **Tier 1 (Primary/Official)**: Primary records, court filings, audited financial statements, direct statistics from official agencies, statutes, regulations, peer-reviewed academic literature with named authors and open datasets.
- **Tier 2 (Expert/Structured)**: Expert analysis, specialist industry reports, reputable investigative journalism with named sources, industry databases, and credible books.
- **Tier 3 (Speculative/Unstructured)**: Social media posts, forum discussions, anonymous claims, rumors, partisan commentary, single anecdotes, and self-published opinions.
  - **CRITICAL RULE**: Tier 3 evidence is strictly prohibited from supporting any core or central conclusion of a causal model. Tier 3 may only be used for narrative maps, early signaling, or hypothesis generation, and must be explicitly labeled as speculative or excluded entirely from the final Claim Ledger.

## 2. Evidence Roles (`evidence_role`)

Every source listed in the Claim Ledger must be explicitly classified under one of the following roles:
- `directly_supports`: The source provides direct, verifiable evidence for the specific causal claim.
- `partially_supports`: The source supports elements of the claim, but requires inference or additional data to connect fully.
- `context_only`: The source provides background context, historical framing, or base rates, but does not prove the specific claim.
- `contradicts`: The source provides evidence that directly opposes the claim (essential for adversarial testing).
- `weak_or_unverified`: The source is speculative, uncorroborated, or lacks sufficient credibility (typical for Tier 3).

## 3. Metadata Requirements

To prevent quote laundering and stale analysis, all claims in the Claim Ledger must include:
- **Access Date (`access_date`)**: The exact date the information was retrieved or verified (format: YYYY-MM-DD). Crucial for live/unstable facts.
- **Failure Mode (`failure_mode`)**: A brief description of how or why the source could fail or be misleading (e.g., selection bias, conflict of interest, narrative capture, stale facts, regulatory capture, measurement distortion).
- **Measurement Integrity Risk (`measurement_integrity_risk`)**: A brief review of whether the source may reflect a bad-meter problem rather than underlying reality, such as changed definitions, missing denominators, sample-selection bias, platform filtering, delayed disclosure, duplicate counting, revision history, or incentives to misreport.
- **Source Position (`source_position`)**: For interpretive sources, identify the creator or institution's relevant background, funding or career incentives, target audience, worldview priors, and known unknowns. This is not a guilt-by-association test; it is a lens for detecting hidden assumptions, omissions, and narrative incentives.

## 4. Verification Gate

Before completing an investigation, the agent must check if:
1. Every core claim has at least one Tier 1 source or two independent Tier 2 sources.
2. Any core claim relying solely on Tier 3 evidence is demoted or flagged.
3. Every entry in the ledger has an assigned `evidence_role`, `access_date`, `failure_mode`, and `measurement_integrity_risk`.
4. Any core claim based on an observed anomaly has passed an observation-integrity check: the signal's measurement method, sample frame, denominator, definition stability, reporting incentive, and revision risk have been reviewed.
5. Any mainland China source used is strictly limited to necessary first-hand facts, official laws/regulations/announcements, statements by the parties involved, or materials of the research object itself, with any interpretive/explanatory conclusions cross-verified by independent non-mainland sources.
6. Any interpretive source used for a core claim includes a `source_position` audit or is downgraded to context/hypothesis status.
7. Two Tier 2 sources count as independent only if they have different funders, methodologies, primary datasets, or direct access paths. Two reports repeating the same original dataset, sponsor, or press release do not count as independent corroboration.

## 5. Observation Integrity Gate

Before explaining an anomaly, audit whether the observed signal could be a bad-meter event: a misleading reading produced by the measurement, reporting, sampling, platform, statistical, or data-generation process.

Ask:
1. **Meter**: What produced the signal: official statistic, survey, platform ranking, corporate disclosure, sensor, model output, media selection, or user-visible sample?
2. **Definition Stability**: Did the metric definition, reporting threshold, classification rule, or time window change?
3. **Denominator Integrity**: Is the base population known, complete, and comparable across time?
4. **Sampling Frame**: Who or what is missing, excluded, delayed, duplicated, or overrepresented?
5. **Reporting Incentive**: Who benefits if the signal looks better, worse, larger, smaller, more urgent, or more stable?
6. **Independent Remeasurement**: Can the signal be validated through raw data, external proxies, independent datasets, comparable cases, or later revisions?

If observation integrity is weak, treat the signal as a reported observation, not as confirmed underlying reality. Downgrade causal confidence until independent remeasurement or a strong proxy supports it.

## 6. Geographic Sourcing Constraints (Mainland China)

To prevent narrative capture, single-source inducement, and government-guided bias:
- **Prioritize Non-Mainland Sources**: When conducting web searches, the agent must always prioritize and favor sources and materials from outside mainland China (e.g., global databases, international media, independent research institutions, non-mainland expert analysis).
- **Restricted Use of Mainland China Sources**: Materials from mainland China are strictly restricted. They are ONLY permitted to be used for:
  1. Necessary first-hand factual sources (e.g., original local statistics, raw data).
  2. Official laws, regulations, and government policy announcements.
  3. Declarations or statements of the parties involved (e.g., official corporate releases, public statements of key figures).
  4. Materials of the research object itself (e.g., local company reports, product specifications).
- **Mandatory Cross-Verification**: Any interpretive or explanatory conclusions contained in mainland China sources must NOT be accepted as objective fact. They must be cross-verified and validated using high-quality, independent non-mainland sources before being incorporated into the causal model.
- **Reported Signal Rule**: Mainland official, platform, corporate, or media data should be treated as reported signals rather than automatically as complete ground truth. Before using them for causal modeling, audit the data-generation process: statistical definition, reporting incentive, sample frame, platform filtering risk, revision history, and independent remeasurement availability.

## 7. Source Position Audit

Apply this audit to commentary, expert analysis, investigative reporting, think-tank reports, institutional narratives, creator posts, and any source whose value comes from interpretation rather than raw facts.

Record the shortest useful answer to:
1. **Creator / Institution**: Who produced it, and what relevant role, employer, funder, community, or historical position might shape its frame?
2. **Payoff Function**: What does the creator gain or risk by emphasizing this interpretation?
3. **Audience Incentive**: Which audience is the source written for, and what belief would satisfy that audience?
4. **Worldview Priors**: What assumptions about markets, state power, rights, equality, hierarchy, identity, security, or progress are embedded in the framing?
5. **Omissions**: Which facts, counterexamples, or affected groups are easy for this source to ignore?
6. **Corroboration Need**: Which independent sources would weaken or confirm the interpretation?

Use the audit to weight interpretive claims, not to automatically reject sources. A biased source can still provide accurate facts; an aligned source can still smuggle weak interpretation into the conclusion. Downgrade interpretive claims to context/hypothesis status when the source position is undisclosed, untestable, unsupported, or doing hidden normative work.
