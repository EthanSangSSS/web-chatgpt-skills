# Adapter: Digital Product / UI

Use this adapter for apps, websites, dashboards, operating-system surfaces, software tools, digital services and interactive prototypes.

## Adapter objective

Translate cultural and perceptual intent into interface hierarchy, interaction behavior, state communication and inclusive visual language without confusing screenshot appeal with real task quality.

## Required UI intake

Add to the core intake:

```yaml
ui_context:
  platform:
  device_classes:
  input_methods:
  primary_flows:
  frequency_of_use:
  novice_or_expert_mix:
  environmental_conditions:
  localization_scope:
  state_complexity:
  error_consequence:
  assistive_technology:
  existing_design_system:
```

## UI-specific cultural evidence

Investigate:

- category conventions and platform expectations;
- target-group use of density, hierarchy, navigation, motion and feedback;
- expert versus novice interpretation of compactness and visible complexity;
- public-facing identity signals versus private productivity preference;
- local reading direction, typography, numerals, symbols and formality;
- authority choices from relevant practitioners, not generic design celebrity status;
- behavior evidence such as successful completion, return use, customization and abandonment.

Do not infer preference from the popularity of one platform when switching cost, ecosystem lock-in or mandatory enterprise procurement explains adoption.

## UI perceptual-intent dimensions

Common dimensions include:

- calm versus energetic;
- precise versus approachable;
- dense versus spacious;
- professional versus playful;
- stable versus exploratory;
- transparent versus mysterious;
- premium restraint versus expressive abundance;
- human warmth versus technical neutrality.

Specify forbidden perceptions, such as fragile, toy-like, deceptive, inaccessible, unfinished, bureaucratic, noisy or over-simplified.

## UI design grammar

Translate intent into:

```yaml
ui_grammar:
  information_hierarchy:
  navigation_model:
  content_density:
  typography:
  spacing_and_rhythm:
  color_and_contrast:
  icon_and_symbol_language:
  component_shape:
  elevation_and_material_effect:
  motion_and_transition:
  state_visibility:
  error_and_recovery:
  personalization:
  accessibility_affordances:
  responsive_behavior:
  localization_behavior:
```

Every rule needs a task, cultural or perceptual rationale.

## Inclusive-mainline requirements

Check the primary interface, not only a separate accessibility mode:

- sufficient text and state contrast;
- visible focus and keyboard navigation where applicable;
- target sizes and spacing suitable for motor variability;
- labels not dependent on color, gesture or icon recognition alone;
- scalable text without clipping or broken hierarchy;
- predictable reading and navigation order;
- reduced-motion support without loss of information;
- screen-reader semantics and meaningful control names;
- recoverable errors and reversible actions;
- low dependence on precision timing or drag-only interaction;
- cognitive load, fatigue and interruption recovery.

A separate adaptation is acceptable only when one unified solution is technically irreconcilable. It must remain equal in quality and brand dignity.

## Screenshot-bias controls

Never validate a digital product only through static renders. Compare:

- screenshot versus interactive prototype;
- first impression versus repeated task use;
- ideal empty state versus realistic content and error states;
- marketing animation versus reduced-motion behavior;
- desktop versus small-screen and zoomed layouts;
- light/dark or environmental variants where material;
- branded versus blind form evaluation.

## UI Pareto candidates

### A — Convention-stable

Preserve platform and category expectations. Use for high-frequency or high-consequence flows where predictability matters.

### B — Utility-enhanced

Prioritize task efficiency, state clarity, accessibility and recovery. Allow useful controls to remain visible even when extreme visual minimalism would hide them.

### C — Brand-expression

Use distinctive motion, typography, composition or material treatment primarily in reversible and non-critical layers. Core controls, state, refusal and exit remain explicit.

## UI hard-stop conditions

Return `STOP` or `RESEARCH_ONLY` when:

- the primary task is unknown;
- critical states or consequences are missing;
- the design requires hiding price, consent, cancellation, refusal or error information;
- essential controls rely on low contrast, inaccessible gestures or precision timing;
- a named style request requires direct imitation;
- localization or cultural-symbol risk is material but unresearched.

## UI validation

Freeze criteria before final visual review.

### Task and embodied measures

- completion and recovery rate;
- time, steps and unnecessary navigation;
- error incidence and comprehension;
- keyboard, screen reader, zoom and reduced-motion behavior;
- motor precision demand;
- cognitive load and interruption recovery;
- fatigue in repeated use.

### Perceptual measures

- intended quality recognition;
- forbidden-perception incidence;
- hierarchy and state comprehension;
- trust and control;
- difference between brand halo and interface-form effect.

### Behavioral measures

- real or simulated task choice;
- sustained use;
- feature discovery without coercion;
- abandonment and return;
- customization and preference persistence.

## UI output additions

Include:

```yaml
ui_output:
  primary_flows_reviewed:
  critical_states:
  component_and_token_implications:
  interaction_rules:
  responsive_and_localization_rules:
  accessibility_status:
  screenshot_bias_controls:
  prototype_tests_required:
```
