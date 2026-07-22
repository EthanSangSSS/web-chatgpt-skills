# Example: Professional Operations Dashboard

> Fictional specification example. No real user research, analytics or validation is claimed.

## Input

Design an operations dashboard for experienced supply-chain analysts in Shanghai and Singapore. The product should feel precise, calm and premium. Existing screens are dense. New analysts struggle, while experienced analysts dislike simplified consumer-style interfaces.

## Human decision layer

### Verdict

`PROCEED_EXPLORATORY` — Candidate B is the recommended prototype direction. Evidence is L1-L2 because the segment conflict is supplied as context but not supported by source material or task data.

### Target and intent

**Primary segment:** experienced supply-chain analysts using the dashboard daily.

**Secondary segment:** new analysts during onboarding.

**Primary perceptions:** precise, controlled, reliable.

**Secondary perceptions:** calm, professional, learnable.

**Forbidden perceptions:** toy-like, empty, decorative, opaque, low-control.

**Embodied intent:** low visual fatigue, clear state changes, predictable keyboard use, fast interruption recovery.

### Evidence limits

- The supplied expert/new-user conflict is an unverified project statement.
- No direct task metrics, interviews or analytics are available.
- “Premium” has been decomposed into control, precision and restraint rather than a named-brand visual style.

### Candidate A — Consensus-stable

Use familiar enterprise navigation, persistent filters, compact tables and restrained neutral surfaces. Improve grouping and spacing without changing density materially.

**Benefit:** lowest expert-disruption risk.

**Risk:** onboarding difficulty may remain.

### Candidate B — Utility-enhanced

Retain expert density but add progressive disclosure, role-based presets, keyboard-first navigation, persistent system state, stronger error recovery and an optional guided onboarding layer.

**Benefit:** protects expert efficiency while reducing new-user failure.

**Risk:** higher system and design complexity.

### Candidate C — Brand-expression

Introduce a distinctive command-center composition, stronger typography, selective translucent layering and motion for system transitions.

**Benefit:** strongest brand differentiation.

**Risk:** visual effects may reduce readability, performance and state clarity; keep them away from dense data and critical alerts.

### Recommendation

Prototype Candidate B first. Candidate A is the control. Use selected Candidate C treatments only after readability, contrast, performance and reduced-motion review.

### Required validation

1. Expert and new-user task completion, time and error recovery.
2. Keyboard, zoom, screen-reader and reduced-motion behavior.
3. Blind comparison of hierarchy and calmness without brand labels.
4. Repeated-use fatigue rather than screenshot preference alone.
5. Expert efficiency countermetric so onboarding improvements do not degrade high-frequency work.

## Machine-readable excerpt

```yaml
project:
  project_id: fictional-ops-dashboard
  domain: digital_product_ui
  research_depth: standard
  status: exploratory

risk_routing:
  irreversibility: low
  accessibility_and_dignity_consequence: medium
  evidence_uncertainty: high
  execution_state: PROCEED_EXPLORATORY

perceptual_intent:
  primary: [precise, controlled, reliable]
  secondary: [calm, professional, learnable]
  forbidden: [toy_like, decorative, opaque, low_control]

candidates:
  - id: A
    strategy: consensus_stable
    confidence: low
  - id: B
    strategy: utility_enhanced
    confidence: moderate
  - id: C
    strategy: brand_expression
    confidence: low

gates:
  gate_0_hard_constraints:
    accessibility_and_dignity: not_tested
    core_task: not_tested
    verdict: not_tested

decision:
  verdict: INCONCLUSIVE
  selected_candidate: B_for_prototype
  rationale: best current Pareto hypothesis; no user validation yet
```

## Why this example is compliant

- It preserves the conflict between experts and new users.
- It does not use mean preference to overrule task outcomes.
- It treats premium perception as a semantic objective, not style copying.
- It separates a prototype recommendation from a validation verdict.
- It does not call static render review a usability test.
