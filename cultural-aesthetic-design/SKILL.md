---
name: cultural-aesthetic-design
version: "0.1.0"
status: beta
description: Evidence-calibrated cross-domain aesthetic design using target-group cultural consensus, psychology and biology research, utility, brand meaning, embodied experience, accessibility, and falsifiable validation. Use for aesthetic strategy, design direction, UI/product form language, cultural fit, premium perception, and evidence-based design review.
triggers:
  - aesthetic design
  - aesthetic strategy
  - cultural consensus design
  - design language
  - premium perception
  - UI aesthetic direction
  - hardware form language
  - evidence-based design
  - 审美设计
  - 审美策略
  - 文化共识
  - 设计语言
  - 高级感
  - 产品美学
  - UI 美学
  - 硬件外观
  - 无障碍美学
do_not_use_for:
  - copying a living artist or identifiable contemporary designer style
  - treating dominant taste as universal truth
  - bypassing safety accessibility legality or informed autonomy
  - claiming user validation or scientific proof without evidence
  - decorative image generation with no product or decision context
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Cultural Aesthetic Design

## Purpose

Create and evaluate aesthetic directions that are culturally legible, useful, embodied, inclusive, brand-coherent, and evidence-bounded. Strong target-group cultural consensus is a major input, but never an automatic truth or moral permission.

The skill optimizes perceived value across six layers:

1. functional value;
2. emotional value;
3. symbolic and identity value;
4. aesthetic value;
5. cultural legitimacy;
6. long-term ownership and use value.

Beauty is modeled as an interaction among bio-perceptual priors, cultural-semantic priors, identity and consensus, personal relevance, utility, embodiment, and controlled deviation. Do not reduce the method to fixed rules such as symmetry, minimalism, luxury materials, or majority preference.

For Standard or Deep work, read `references/core-protocol.md`. Read only the relevant adapter:

- digital interfaces and software: `adapters/digital-product-ui.md`;
- physical products, hardware, furniture, mobility or assistive products: `adapters/physical-product-accessibility.md`.

Use `templates/design-decision-record.yaml` when a machine-readable handoff is useful. Use `references/acceptance-cases.md` for adversarial validation.

## Routing and orchestration

This is the primary skill when the user needs a design direction or design evaluation grounded in target culture, evidence, utility, brand meaning, and embodied use.

Reuse other catalog skills when available:

- `customer-research`: interviews, reviews, support evidence, JTBD and segment contradictions;
- `truth-seeking`: disputed causal claims, power and incentive maps, observation-integrity review;
- `grill-me`: unresolved high-impact assumptions before implementation;
- `nuwa`: bounded perspective models, never as real authority evidence;
- `skill-vetter`: external design skill or workflow review;
- `industrial-self-audit-protocol`: final evidence-based release gate.

Record every module call, purpose, expected output, authority limit, and fallback. No supporting module may select or certify the final design by itself.

## Execution boundary

This skill may analyze conversation context, uploaded files, GitHub-visible material, public web evidence, images, prototypes, and user-supplied results. It must not claim:

- access to private analytics, interviews or customer records;
- scientific causality from a single study or analogy;
- cultural permission from public visibility alone;
- user validation from AI review;
- local build, test, rendering, fabrication or deployment without tool evidence;
- future trend certainty.

When evidence is insufficient, lower the maturity label or return `RESEARCH_ONLY`; do not manufacture completeness.

## Core operating principles

### 1. Utility and aesthetics are coupled

Extreme utility can override prior aesthetic or brand barriers and may be reinterpreted as engineering beauty. Aesthetic treatment that harms utility becomes decorative interference.

Optimize for Pareto-efficient candidates rather than a weighted average that allows severe task, safety or accessibility failure to be hidden by visual appeal.

### 2. Cultural consensus is multidimensional

Evaluate:

- relevant authority choices;
- actual behavior;
- identity and status constraints;
- stability over time;
- cross-context reach;
- transmission power;
- availability, lock-in and coercion confounders.

Prefer triangulation among behavior, domain-relevant authority and cultural texts. Self-report and designer intuition are supporting evidence only.

### 3. Authority is domain-bounded

Authority is not a social identity. Grade domain relevance, practice depth, outcome responsibility, peer recognition, behavioral consistency, track record, cultural influence, conflict of interest, recency and evidence transparency.

Separate epistemic, practice, cultural, behavioral and institutional authority. Do not collapse them into one global authority score.

### 4. Consensus does not grant moral permission

Describe harmful consensus when relevant, but do not operationalize mechanisms that depend on humiliation, dehumanization, exclusion, deception, unnecessary inaccessibility or loss of autonomy.

Prestige may differentiate; it may not dehumanize.

### 5. Inclusive mainline by default

Body differences are primary design inputs, not end-stage accommodations. Prefer one high-quality inclusive main solution. When a genuine technical conflict requires an adaptation, preserve equivalent quality, brand dignity, feature support, maintainability and non-stigmatizing presentation.

Independence is an aesthetic value. Reduced friction, autonomy, emotional security and control can produce embodied elegance.

### 6. Persuasion must track reality

Allow brand narrative and persuasion, but prohibit false scarcity, hidden cost, identity shame, material misrepresentation, obstruction of refusal or exit, and exploitation of vulnerability.

### 7. Originality must be traceable

Transfer mechanisms and cultural meanings, not recognizable combinations. Record source lineage, inferred principle, transformation, context shift, differentiation and similarity risk. Reject high-risk imitation.

## Required intake

Collect or infer:

- decision question and deliverable;
- domain and lifecycle stage;
- target segments, geography and cultural context;
- core task and failure consequences;
- public versus private use and identity exposure;
- brand worldview and current constraints;
- body profiles, use posture, reach, grip, vision, hearing, fatigue, cognition, assistive technology and duration where relevant;
- budget, reversibility and decision owner;
- requested style terms and their intended meaning;
- available evidence and freshness.

Decompose vague style labels such as `Apple-like`, `aristocratic`, `premium`, `minimal`, `industrial` or `friendly` into intended perceptions, utility implications, cultural signals and forbidden perceptions. Do not imitate a named brand or creator by surface copying.

## Risk routing and research depth

Choose one mode:

- `Quick`: low-risk, reversible, short-lived work;
- `Standard`: normal product, UI, brand or packaging decision;
- `Deep`: hardware, public space, assistive product, global brand, costly or hard-to-reverse decision;
- `Hold`: blocking uncertainty or hard-boundary risk.

Escalate depth when safety, accessibility, cultural distance, irreversible manufacturing, vulnerable users, identity manipulation, sacred or restricted culture, or major brand exposure is involved.

Execution states:

- `PROCEED`;
- `PROCEED_EXPLORATORY`;
- `RESEARCH_ONLY`;
- `STOP`.

The user may accept aesthetic, novelty or market uncertainty. The user may not waive safety, accessibility, legality, factual integrity or informed autonomy.

## Evidence maturity

Use these levels:

- `L0 No evidence`: output only missing inputs and research questions;
- `L1 Exploratory`: analogies and low-confidence hypotheses, with minimal tests;
- `L2 Directional`: at least two supporting evidence types; candidates allowed;
- `L3 Decision-grade`: clear segment, two strong support types, freshness and confounder review, basic tests;
- `L4 Validation-grade`: all applicable gates passed with direct evidence.

Keep these maturity labels distinct:

- `Observed Pattern`;
- `Design Hypothesis`;
- `Candidate`;
- `Validated Rule`;
- `Rejected`.

A biological tendency is not automatically a psychological response; a psychological response is not automatically a cultural meaning; a cultural meaning is not automatically a behavior.

## Perceptual intent

Before generating a design, define:

- `primary_perceptions`: what the target should feel or infer first;
- `secondary_perceptions`: useful supporting qualities;
- `forbidden_perceptions`: meanings the design must not produce;
- `embodied_intent`: how approach, touch, operation, movement, waiting, maintenance and long-term use should feel.

Do not generate before the intent is sufficiently clear for the risk level.

## Workflow and role separation

Use the state machine:

```text
INTAKE
→ RISK_ROUTING
→ RESEARCH
→ EVIDENCE_GATE
   ├─ insufficient → RESEARCH_ONLY
   ├─ unsafe       → STOP
   └─ sufficient   → DESIGN_GRAMMAR
                    → DOMAIN_ADAPTER
                    → PARETO_CANDIDATES
                    → RED_TEAM_REVIEW
                    → VALIDATION
                    → PASS / PASS_WITH_WARNINGS / REVISE / INCONCLUSIVE / STOP
```

Maintain role boundaries:

- **Researcher** owns evidence collection and scoped interpretation, not final design selection.
- **Generator** owns candidate construction, not certification.
- **Red Team** owns failure discovery, not silent redesign.
- **Validator** owns test-result interpretation, not subjective preference substitution.
- **Decision Owner** resolves remaining value trade-offs.

Where one model performs several roles, explicitly reset the role, expose prior assumptions, freeze criteria before review, and state that AI role separation is not independent user validation.

## Candidate generation contract

Generate three materially different Pareto candidates:

- **A — Consensus-stable**: lowest cultural risk, strongest established legibility;
- **B — Utility-enhanced**: strongest task, embodied and accessibility improvement while retaining cultural fit;
- **C — Brand-expression**: strongest distinctive worldview and controlled deviation.

Candidates must differ in strategic trade-offs, not only color, typography or decoration. For each candidate record:

- design grammar;
- intended perceptions;
- supporting evidence;
- utility and accessibility effect;
- cultural and brand risk;
- novelty and similarity risk;
- expected aging and maintenance behavior;
- confidence;
- counterexamples;
- validation and invalidation conditions.

When the user supplies a preferred style, preserve its semantic direction in one candidate, provide an evidence-calibrated alternative, and add a utility-enhanced alternative when relevant. Hard-boundary violations do not enter the candidate set.

## Special cultural mechanisms

### Anti-aesthetic and controlled imperfection

Distinguish execution failure, utility residue, authenticity signal, identity signal, strategic anti-aesthetic and artificial roughness. Intentional imperfection must be more controlled than accidental imperfection and must survive real use, aging, safety and maintenance review.

### Dynamic diffusion and counter-distinction

Track origin group, adoption sequence, utility driver, identity driver, commercial amplification, saturation, signal dilution, authority exit, reverse diffusion and geographic spread.

Use states such as `Incubating`, `Emerging`, `Accelerating`, `Mainstream`, `Saturated`, `Fragmenting`, `Elite Exit`, `Residual` and `Reviving`.

Availability is not adoption; adoption is not preference; preference is not identity internalization.

Forecast only through scenarios with horizon, drivers, counter-signals and invalidators. Avoid false numerical precision when no reference class exists.

### Cultural permission

Classify cultural assets as open expression, shared tradition, community-governed, restricted knowledge, sacred/ceremonial or uncertain. Public visibility is not commercial permission. When authorization, representative consultation or fair benefit arrangements are missing, use the material only for contextual research.

## Validation gates

Run gates in order. A hard-gate failure cannot be offset by other scores.

### Gate 0 — Hard constraints

- safety;
- legality and ethical boundary;
- accessibility and dignity;
- factual and material truth;
- reliability and maintainability;
- core task completion;
- informed autonomy;
- cultural permission where required.

Failure verdict: `STOP` or `REJECT`.

### Gate 1 — Task and embodied value

Measure task success, time, errors, learning, reach, grip, posture burden, fatigue, pain, need for assistance, maintenance and reliability.

### Gate 2 — Perceptual intent

Test whether target segments perceive the intended primary and secondary qualities without triggering forbidden perceptions.

### Gate 3 — Behavior

Check actual choice, sustained use, willingness to adopt, switching, abandonment, return and identity display. Control for price, channel, lock-in, social pressure, defaults and availability.

### Gate 4 — Long-term stability

Check aging, wear, maintenance, novelty decay, cultural saturation, brand coherence and reversibility.

### Bias controls

Where material, use blind versus branded tests, counterfactual variants, realistic context, longitudinal exposure, segment analysis, private versus public choice, and media-control tests. AI evaluation is not a substitute for target-user evidence.

Verdicts:

- `PASS`;
- `PASS_WITH_WARNINGS`;
- `REVISE`;
- `INCONCLUSIVE`;
- `STOP`.

Pair every target metric with a countermetric to reduce Goodhart effects.

## Evidence ledger and freshness

Use a versioned evidence ledger. Every reusable claim needs source, mechanism, population, method, domain, conditions, culture, replication or corroboration status, strength, counterevidence, implication, invalidators, evidence date, applicable scope and review status.

Statuses:

- `Draft`;
- `Active`;
- `Validated`;
- `Contested`;
- `Degraded`;
- `Superseded`;
- `Retired`.

Do not silently overwrite prior records. New evidence should supersede, split or contest the old record with an explicit reason.

Set review timing from change velocity, decision irreversibility, potential harm, evidence uncertainty and contradiction signals. Stale evidence may support historical context, not a critical current decision.

## Output contract

Default to a layered dual output.

### Human decision layer

Return only the stage-relevant items:

1. verdict and execution state;
2. decision question and scope;
3. target segment and perceptual intent;
4. evidence level, freshness and main uncertainty;
5. recommended direction or research-only conclusion;
6. three Pareto candidates when allowed;
7. critical trade-offs and hard-gate status;
8. required validation and next decision.

### Machine-readable layer

Use `templates/design-decision-record.yaml` when the output will be handed to another agent, repository or tool. Unknown fields must remain `unknown` with reason and impact. Never convert `not tested` into `passed`, `inferred` into `observed`, AI review into user validation, or design intent into measured outcome.

## Common failure modes

- copying surface style instead of identifying the underlying cultural mechanism;
- treating developed-country, wealthy or highly educated groups as universal taste;
- double-counting correlated elite signals;
- using stated preference as behavior without confounder review;
- letting brand narrative override operational truth;
- creating a separate stigmatizing accessibility version by default;
- average-score approval that hides a hard-gate failure;
- circular self-certification by the generator;
- trend chasing without saturation or authority-exit analysis;
- using public sacred or community-governed culture without permission;
- false precision in forecasts or evidence scores;
- producing a long methodology report when a decision summary is sufficient.

## Local-agent handoff trigger

Hand off when work requires private research data, local repository edits beyond safe connector writes, automated large-scale evidence processing, interactive prototype instrumentation, accessibility lab testing, physical fabrication, build execution or repeated longitudinal analysis.

The handoff must include repository/project, branch or version, allowed files and artifacts, target segment and body profiles, hard boundaries, evidence requirements, validation commands or study protocol, forbidden claims, stop conditions and final output format. Do not claim the handoff work has run until evidence is returned.
