# Cultural Aesthetic Design — Core Protocol

Use this reference for Standard and Deep executions. The protocol converts cultural, scientific, behavioral and embodied evidence into falsifiable design decisions without treating consensus as universal truth.

## 1. Intake record

Create an intake record before research:

```yaml
intake:
  decision_question:
  deliverable:
  domain:
  lifecycle_stage:
  target_segments:
  geography:
  public_or_private_use:
  core_tasks:
  failure_consequences:
  brand_worldview:
  requested_style_terms:
  body_profiles:
  constraints:
  budget_and_reversibility:
  decision_owner:
  available_evidence:
  evidence_date:
```

Resolve only high-impact ambiguity. When a safe and explicit assumption is possible, state it and proceed. Do not create fictional personas or pretend the target segment is known.

## 2. Risk and depth routing

Assess each dimension as low, medium or high:

- decision irreversibility;
- safety and bodily consequence;
- accessibility and dignity consequence;
- financial and manufacturing exposure;
- cultural distance and symbolic sensitivity;
- brand exposure and persistence;
- evidence uncertainty;
- user vulnerability;
- novelty and analogy distance;
- likelihood of manipulation or information asymmetry.

Route:

| Condition | Mode | State |
|---|---|---|
| Low consequence, reversible, familiar context | Quick | `PROCEED_EXPLORATORY` or `PROCEED` |
| Normal product or interface decision | Standard | Evidence gate required |
| Hardware, public, assistive, global or costly decision | Deep | Decision-grade evidence required |
| Hard boundary cannot be assessed | Hold | `STOP` |
| Target, task or cultural meaning materially unknown | Hold | `RESEARCH_ONLY` |

## 3. Evidence inventory

Every source receives:

```yaml
evidence_item:
  id:
  claim:
  evidence_type: behavioral | authority | cultural_text | scientific | self_report | analogy | designer_observation
  source:
  source_date:
  access_date:
  population_or_segment:
  geography:
  domain:
  method_or_sample:
  directness:
  strength: strong | moderate | weak | anecdotal
  evidence_role: supports | partially_supports | context_only | contradicts | unverified
  mechanism:
  conditions:
  confounders:
  source_position_or_conflict:
  counterevidence:
  transfer_distance:
  applicable_scope:
  invalidators:
  freshness_status: fresh | review_due | stale | invalidated
```

### Evidence-type cautions

- **Behavioral evidence**: check price, channel, default, availability, switching cost, lock-in, institutional mandate, advertising, habit and social pressure.
- **Authority evidence**: check domain relevance, consequence ownership, consistency, conflicts and recency.
- **Cultural texts**: useful for shared meaning and transmission, not direct proof of preference or behavior.
- **Scientific evidence**: record population, method, effect conditions, replication/corroboration and external-validity limits.
- **Self-report**: useful for language and conscious explanation; not identical to private choice or sustained behavior.
- **Analogy**: record source domain, target domain, shared mechanism, material differences and confidence reduction.
- **Designer observation**: hypothesis input only until independently supported.

## 4. Cultural consensus map

Create one row per candidate signal or design language:

```yaml
consensus_signal:
  signal:
  target_segment:
  authority_support:
  behavioral_support:
  cultural_text_support:
  identity_constraint:
  stability:
  cross_context_reach:
  transmission_power:
  availability_confound:
  lock_in_confound:
  status_coercion_confound:
  current_state: stable | emerging | residual | declining | contested | segment_specific | artificially_amplified
  confidence:
  evidence_refs:
```

A signal normally needs support from at least two evidence types before it reaches `L2 Directional`.

Do not average incompatible segments. Preserve contradictions such as:

- public display versus private ownership;
- visual admiration versus usage preference;
- professional choice versus symbolic choice;
- hereditary elite versus new wealth;
- local authority versus global platform amplification;
- disabled users versus assumed average-body users.

## 5. Authority qualification

Evaluate authority by dimension rather than social rank:

```yaml
authority_record:
  actor_or_group:
  authority_type: epistemic | practice | cultural | behavioral | institutional
  qualified_dimension:
  domain_relevance:
  practice_depth:
  outcome_responsibility:
  peer_recognition:
  behavioral_consistency:
  track_record:
  cultural_influence:
  conflict_of_interest:
  recency:
  evidence_transparency:
  verdict: qualified | partially_qualified | context_only | not_qualified
```

Issue decomposition rules:

- engineers may judge physical feasibility and reliability;
- users with lived bodily consequences judge access, fatigue, pain and independence;
- cultural authorities may judge meaning and legitimacy;
- target-user behavior calibrates actual adoption;
- brand leadership owns worldview trade-offs only within hard constraints.

No authority can overrule a dimension outside its qualification.

## 6. Scientific prior calibration

For psychology, perception, biology or neuroscience evidence, create:

```yaml
scientific_prior:
  claim:
  proposed_mechanism:
  population:
  sample_and_method:
  domain:
  stimulus_and_context:
  effect_direction:
  effect_size_if_known:
  replication_or_corroboration:
  cultural_conditions:
  boundary_conditions:
  counterevidence:
  evidence_strength:
  design_implication:
  invalidators:
  evidence_date:
```

Use research as a conditional prior, not a universal design law. Never infer a specific target segment's preference solely from general perceptual research.

## 7. Perceptual and embodied intent

Create intent before form:

```yaml
perceptual_intent:
  primary:
  secondary:
  forbidden:
  embodied:
    approach:
    reach_and_access:
    touch_and_grip:
    operation:
    movement:
    waiting_and_feedback:
    maintenance_and_cleaning:
    long_term_use:
```

Examples of embodied intent:

- stable;
- effortless;
- reachable;
- reassuring;
- controllable;
- comfortable;
- independently operable.

Forbidden embodied perceptions may include fragile, slippery, exhausting, painful, dependent, excluding, unstable or deceptive.

## 8. Design grammar

Translate evidence into parameters, not style imitation:

```yaml
design_grammar:
  hierarchy:
  geometry:
  proportion:
  density:
  rhythm:
  contrast:
  material_or_surface:
  typography_or_labeling:
  interaction_or_mechanism:
  visibility_of_structure:
  accessibility_affordances:
  aging_and_wear:
  controlled_deviation:
  forbidden_combinations:
```

Every grammar rule must reference an intended perception, task effect or cultural mechanism.

Bad rule:

> Use more whitespace because premium brands do it.

Acceptable hypothesis:

> For the specified target segment and decision context, reduce simultaneous visual competition to support calm control and premium restraint, while preserving task scanning and state visibility. Validate against the counterfactual with equal content and brand cues.

## 9. Candidate construction

Construct three strategic candidates:

### Candidate A — Consensus-stable

- established, legible cultural signals;
- low interpretive risk;
- limited novelty;
- suitable for core brand or irreversible layers.

### Candidate B — Utility-enhanced

- task, embodiment, independence and accessibility prioritized;
- culture remains legible;
- may redefine practical performance as engineering elegance.

### Candidate C — Brand-expression

- highest controlled deviation and distinctive worldview;
- stronger novelty and misreading risk;
- should be applied to reversible layers unless evidence is decision-grade.

Candidate record:

```yaml
candidate:
  id:
  strategy:
  perceptual_intent_refs:
  design_grammar:
  expected_functional_value:
  expected_emotional_value:
  expected_symbolic_value:
  expected_aesthetic_value:
  expected_cultural_value:
  expected_long_term_value:
  evidence_refs:
  utility_cost:
  accessibility_cost:
  cultural_risk:
  manipulation_risk:
  permission_risk:
  similarity_risk:
  maintenance_and_aging:
  confidence:
  counterexamples:
  validation:
  invalidation_conditions:
```

## 10. Power, harm and cultural-permission audit

### Power and harm

```yaml
power_harm_audit:
  consensus_signal:
  source_group:
  affected_groups:
  historical_origin:
  legitimate_meaning:
  status_or_identity_function:
  power_asymmetry:
  dependence_on_exclusion:
  dependence_on_shame:
  dependence_on_dehumanization:
  dependence_on_inaccessibility:
  information_or_economic_coercion:
  harmful_mechanism:
  transformable_elements:
  prohibited_elements:
  verdict: allow | transform | context_only | prohibit
```

### Cultural permission

```yaml
cultural_permission_record:
  cultural_asset:
  source_community:
  classification: open | shared_tradition | community_governed | restricted | sacred | uncertain
  governance_status:
  intended_use:
  commercial_context:
  representative_consultation:
  permission_evidence:
  attribution_required:
  benefit_sharing:
  distortion_risk:
  community_harm_risk:
  verdict: allow | transform | research_only | prohibit
```

Do not use abstraction as a way to launder restricted or sacred meaning.

## 11. Influence audit

```yaml
influence_audit:
  intended_user_action:
  claim_verifiability:
  information_symmetry:
  option_visibility:
  refusal_and_exit_cost:
  identity_pressure:
  vulnerability_exploitation:
  delayed_costs:
  accessibility_impact:
  reversibility:
  verdict: acceptable_persuasion | revise | prohibit
```

Apply four tests:

1. informed understanding;
2. easy refusal and exit;
3. balanced visibility of material benefits and limits;
4. post-decision reasonableness when the user is calm and informed.

## 12. Diffusion and forecast model

```yaml
diffusion_record:
  signal:
  origin_group:
  current_adopters:
  adoption_sequence:
  utility_driver:
  identity_driver:
  authority_support:
  commercial_amplification:
  imitation_cost:
  saturation:
  signal_dilution:
  authority_exit:
  counter_movement:
  geographic_spread:
  state:
  evidence_date:
```

Forecast separately:

- visual diffusion;
- behavioral adoption;
- identity adoption;
- utility persistence;
- authority retention.

Scenario record:

```yaml
forecast:
  horizon:
  geography:
  segment:
  base_case:
  expansion_case:
  reversal_case:
  confidence: very_low | low | moderate | high | very_high
  drivers:
  counter_signals:
  saturation_risk:
  authority_exit_risk:
  invalidators:
```

## 13. Validation plan

Freeze success and failure criteria before reviewing the final candidate.

### Gate 0 — hard constraints

Any material failure produces `STOP` or `REJECT`:

- safety;
- law and ethics;
- accessibility and dignity;
- factual and material truth;
- informed autonomy;
- reliability and maintainability;
- core task;
- cultural permission.

### Gate 1 — task and embodiment

Possible measures:

- independent completion rate;
- time and action count;
- error and recovery rate;
- reach and grip demand;
- posture burden;
- fatigue and pain;
- help required;
- learning and recall;
- maintenance and cleaning effort;
- reliability under realistic conditions.

### Gate 2 — perceptual intent

Use semantic differential, forced comparison, free-response interpretation, misreading rate and forbidden-perception incidence. Avoid using one mean score when segments conflict.

### Gate 3 — behavior

Use realistic choice, sustained use, willingness to switch, abandonment, return, private choice, public-display choice and price-controlled preference.

### Gate 4 — long term

Use longitudinal exposure, simulated wear, real maintenance, novelty-decay check, cultural saturation and brand-coherence review.

### Bias controls

Use when material:

- blind versus branded comparison;
- wrong-brand or no-brand counterfactual;
- static render versus interactive or physical prototype;
- first impression versus repeated exposure;
- public interview versus anonymous/private choice;
- target users versus designers or experts;
- segmented results rather than global average;
- AI review explicitly separated from human evidence.

## 14. Verdict logic

- `PASS`: all required gates supported by evidence; no material unresolved risk.
- `PASS_WITH_WARNINGS`: usable with explicit non-blocking residual risks.
- `REVISE`: direction is plausible but a material design or evidence issue needs correction.
- `INCONCLUSIVE`: evidence is insufficient for the requested certainty.
- `STOP`: hard boundary or permission failure blocks design.

No scoring system may override Gate 0.

## 15. Versioned evidence ledger

Each reusable record needs:

```yaml
ledger_record:
  id:
  record_type: observed_pattern | hypothesis | validated_rule | forecast
  claim:
  scope:
  evidence_refs:
  confidence:
  status: draft | active | validated | contested | degraded | superseded | retired
  created_at:
  last_verified_at:
  review_due_at:
  invalidators:
  counterevidence:
  supersedes:
  superseded_by:
```

Review priority increases with:

- high change velocity;
- high irreversibility;
- high potential harm;
- high uncertainty;
- new contradiction signals.

Do not silently replace old records. Preserve the reason for change.

## 16. Role handoff

```yaml
role_handoff:
  from_role:
  to_role:
  artifact:
  claims:
  evidence_refs:
  known_tradeoffs:
  untested_assumptions:
  prohibited_inferences:
  required_checks:
```

The red team begins from untested assumptions and frozen criteria, not from the generator's persuasive rationale.

## 17. Compactness rule

Default outputs should support a decision, not display the entire method. Include full ledgers, matrices and schemas only when:

- the user asks for a deep report;
- the output is a durable project artifact;
- another agent requires structured handoff;
- the decision is high-risk or contested;
- the evidence needs auditability.
