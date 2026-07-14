# Truth Seeking Skill

Evidence-constrained root-cause investigation for AI agents.

This skill helps an agent investigate disputed, complex, or narrative-heavy questions without collapsing into media summaries, moralizing, conspiracy overreach, or false certainty. It produces the strongest current causal model (highest-confidence causal model), tied to source tiers, roles, assumptions, uncertainty, falsification tests, and leading indicators.

By default, outputs are compact. Full tables and Deep Mode reports are reserved for explicit requests.

## Use Cases

- "What is the real root cause behind this issue?"
- "Analyze this from first principles, not media narratives."
- "Map incentives, power, money, psychology, and institutional constraints."
- "Check whether a source creator's background, incentives, audience, and worldview shape the interpretation."
- "Separate factual causality from fairness, justice, efficiency, or rights-based evaluation."
- "What is most likely to happen next, and what should we watch?"
- "Separate facts, interpretations, predictions, and value judgments."

## Routing Priority

Use this skill directly when a request asks for root-cause truth, first-principles causal analysis, incentive/power analysis, or falsifiable forecasts. Generic research routers and source-discovery workflows should support evidence gathering, not replace the causal analysis frame.

## What It Produces

Mini Mode (default):

1. Highest-confidence causal model
2. Why surface explanations are insufficient
3. Key evidence (complying with Source Policy, including access dates)
4. First-principles mechanism
5. Prediction and leading indicators

Compact Standard Mode:

- Executive summary
- Research Plan Gate only when it affects scope or uncertainty
- Common narratives and why they are incomplete
- Key Evidence with evidence roles and access dates
- Source-position audit and normative-frame audit when sources or conclusions are value-laden
- First-principles model and incentive map
- Forecast with leading indicators

Deep Mode (explicit request only):

- Research Plan Gate
- Executive summary
- Claim map
- Claim Ledger with source tiers, roles, access dates, and failure modes
- First-principles model
- Incentive and power map
- Psychology and economics lens
- Competing explanations
- Causal graph or causal chain
- Confidence matrix
- Source-position audit
- Normative-frame audit
- Falsification tests
- Future scenarios and leading indicators
- Source gaps

## Installation

### Codex / OpenAI skills-compatible layout

Copy this repository folder into your skills directory:

```bash
cp -R truth-seeking-skill ~/.codex/skills/truth-seeking
```

Then invoke it with:

```text
Use $truth-seeking to build an evidence-constrained causal model for [topic].
```

### Other agent frameworks

If your agent framework does not support Codex-style skills, use:

- `SKILL.md` as the system or developer instruction.
- `references/truth-protocol.md` as the detailed reference file.
- `references/source-policy.md` as the source quality policy.
- `templates/truth-seeking-report.md` as the output template.

## Validation

Run the repository validation checks:

```bash
bash tests/validate.sh
```

The script checks required files, runs the adversarial fixture suite, checks for banned absolute phrasings, and flags private/local coupling.

## File Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── source-policy.md
│   └── truth-protocol.md
├── templates/
│   └── truth-seeking-report.md
├── examples/
│   └── fictional-platform-decline.md
├── tests/
│   ├── check_fixtures.sh
│   ├── validate.sh
│   └── fixtures/
│       ├── conspiracy_bait.md
│       ├── high_stakes_advice.md
│       ├── moralization_bait.md
│       ├── mainland_media_trap.md
│       ├── overconfident_forecast.md
│       ├── rumor.md
│       ├── stale_facts.md
│       └── stance_frame_trap.md
├── LICENSE
└── README.md
```

## Safety Boundaries

This skill is for analysis, not professional advice. For medical, legal, tax, employment, finance, safety, or compliance questions:

- State jurisdiction, date, and scope.
- Prefer current primary sources.
- Separate legal/tax/compliance facts from business judgment.
- Avoid presenting conclusions as professional advice.
- State what a qualified professional would need to verify before action.

## Design Principles

- Evidence over vibe.
- Mechanisms over narratives.
- Compact answer first; full audit trail only when requested.
- Source position over source neutrality assumptions.
- Normative frame disclosure over hidden value judgments.
- Geographic constraints: Prioritize non-mainland China sources; restrict mainland sources to primary/official facts, and cross-verify interpretive conclusions.
- Confidence labels over absolute certainty.
- Incentives before moral blame.
- Falsification before prediction.
- Weighted alternatives before single-cause certainty.
- Base-rate calibration before probability language.
- Source gaps before strong conclusions.

## Example Prompt

```text
Use $truth-seeking to investigate why [organization/market/system] is failing.

Requirements:
- Do not repeat media narratives.
- Use source tiers and roles.
- Audit interpretive sources for creator background, incentives, audience, worldview priors, and omissions.
- State whether evaluative claims use procedural fairness, substantive justice, efficiency, rights, or another frame.
- Weight competing explanations and state the counterfactual test.
- Anchor forecasts with a reference class or state that no credible base rate exists.
- Build a first-principles causal model.
- Map incentives, institutions, money, power, psychology, and information asymmetry where relevant.
- Reject weak common narratives.
- State confidence, unknowns, falsification tests, and leading indicators.
- Do not claim absolute truth.
```

## License

MIT
