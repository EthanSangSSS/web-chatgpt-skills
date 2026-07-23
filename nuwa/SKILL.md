---
name: nuwa
version: "0.3.0"
status: stable
description: Build high-fidelity, evidence-grounded perspective skills from a real person, school of thought, or book without deceptive impersonation, protected-style imitation, or private-motive claims.
triggers:
  - nuwa
  - perspective skill
  - mental model
  - high-fidelity perspective
  - 思维方式
  - 名人思维
  - 学派
  - 书籍蒸馏
do_not_use_for:
  - deceptive impersonation
  - claiming private access or endorsement
  - private motive inference
  - protected expressive-style imitation
  - company-style reconstruction as a primary subject
  - generic decision-method synthesis
  - therapeutic replacement
  - regulated professional advice as the subject
requires:
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Nuwa High-Fidelity Perspective Builder

## Purpose

Use Nuwa to build a reusable, source-traceable reasoning framework from one of three supported subject types:

1. a real person;
2. a school of thought;
3. a book.

The formal output reconstructs publicly evidenced reasoning patterns, priorities, trade-offs, activation conditions, exceptions, and blind spots. It is not the subject, not a simulation of private consciousness, not an endorsement, and not a claim that the subject would give an exact answer in a new situation.

Nuwa optimizes for **source fidelity**, **behavioral fidelity**, and **distinctiveness**. It does not optimize for fast roleplay, surface resemblance, quotation density, or stylistic imitation.

## Product boundary

### Supported primary subjects

- `person`: a real living or deceased person with sufficient public material;
- `school`: a named school, tradition, or intellectual movement with traceable texts and interpreters;
- `book`: one identifiable book treated as an explicit reasoning system.

A book may also serve as primary evidence for a person or school.

### Out of scope as primary subjects

- company, brand, or organizational style;
- generic decision methods without a bounded source corpus;
- fictional characters as if they were real authorities;
- anonymous internet archetypes;
- private individuals without a substantial public evidence base.

Route company-style work to organizational or cultural research. Route generic methods to framework synthesis or requirement engineering.

## Definition of high fidelity

A formal Nuwa skill must satisfy all three dimensions.

### 1. Source fidelity

- Every core heuristic is traceable to an evidence ledger.
- Every core heuristic has at least two independent supporting evidence points unless it is explicitly marked as a single-source claim.
- Counterevidence, conflicts, and source limitations remain visible.
- Quotes are used sparingly; reasoning should be paraphrased and cited.

### 2. Behavioral fidelity

- The framework preserves stable priorities and trade-off logic across novel scenarios.
- Similar cases should activate similar rules unless a documented contextual trigger changes the result.
- Counterfactual input changes should produce explainable changes in judgment.

### 3. Distinctiveness

- The result must differ meaningfully from a generic competent advisor.
- Differences must arise from traceable priorities, causal models, decision rules, or blind spots—not from catchphrases or theatrical tone.
- A subject label attached to generic advice is a validation failure.

## Output states

Return exactly one build state before presenting a formal skill:

- `QUALIFIED`: the subject and evidence base support formal construction;
- `RESEARCH_INCOMPLETE`: the subject is in scope, but the evidence gate is not met;
- `OUT_OF_SCOPE`: the requested primary subject is unsupported by Nuwa;
- `BLOCKED`: the request requires impersonation, private claims, protected-style imitation, unsafe professional substitution, or another prohibited behavior.

Only `QUALIFIED` may produce a formal reusable perspective skill.

## Required input

Collect or infer:

- subject name and subject type;
- intended use;
- applicable domains and explicit non-domains;
- desired output surface: advisor framework, reusable skill, study guide, or scenario evaluator;
- available user-provided materials;
- expected research depth or explicit research budget;
- recency requirements;
- whether the subject is living;
- validation scenarios or target decisions, when available.

Do not ask the user to repeat facts already available in supplied files, GitHub content, or credible sources.

## Web ChatGPT execution boundary

Nuwa may reason from conversation context, uploaded files, GitHub connector data, and current web sources when available.

It must not claim that it has:

- accessed private papers, communications, thoughts, memories, or motives;
- received endorsement from the subject;
- reproduced local commands, private repositories, or unavailable files;
- completed background research outside the current response;
- verified a source it did not actually inspect.

For current, niche, or contested subjects, use live search when available. Cite factual and interpretive claims. When evidence remains thin, stop at `RESEARCH_INCOMPLETE` rather than filling gaps.

## Safety, integrity, and copyright boundaries

- Never write as though a living person personally answered the user.
- Do not imply identity, consciousness, endorsement, or hidden access.
- Do not infer undisclosed motives, diagnoses, beliefs, loyalties, or strategies.
- Do not imitate a living author's protected expressive style. Model reasoning patterns at a higher level of abstraction.
- Do not reproduce long copyrighted passages. Prefer short compliant excerpts and paraphrase.
- Do not use charisma, fame, authority, or user admiration as evidence.
- For political, medical, legal, financial, security-critical, or other regulated domains, keep the perspective analytical and bounded. It does not replace qualified professional advice.
- When a subject's public record includes harmful, discriminatory, deceptive, or illegal behavior, preserve analytical distance and do not turn the skill into operational enablement.

## Workflow

### Phase 0 — Qualification

Determine whether the task can enter formal construction.

Check:

1. Is the primary subject a person, school, or book?
2. Is there a plausible public or user-provided evidence base?
3. Can the intended use be separated from deceptive impersonation or protected-style imitation?
4. Is the requested domain within an analytically safe boundary?
5. Is the research surface accessible with current tools?

Return a build state. For `RESEARCH_INCOMPLETE`, provide the missing evidence classes and a bounded research plan. Do not publish a formal skill.

### Phase 1 — Frame

Define:

- subject identity and type;
- intended use;
- domain scope and non-goals;
- expected fidelity;
- source cutoff date;
- research budget;
- formal deliverable;
- major risks of misrepresentation.

A high-fidelity build may pause for confirmation when a scope choice would materially change the resulting model. Do not require confirmation for low-risk formatting or implementation details.

### Phase 2 — Research design by subject type

#### Person route

Seek evidence across:

- multiple time periods;
- multiple decision contexts;
- first-person books, essays, speeches, interviews, testimony, or official records;
- reliable observations of actual decisions when relevant;
- counterexamples, reversals, and public criticism.

Do not treat curated interviews, biographies, ghostwritten material, or retrospective stories as transparent access to internal thought. Record their limitations.

#### School route

Seek:

- foundational texts;
- central concepts and explicit normative commitments;
- major branches or interpretive traditions;
- internal disputes;
- external criticism;
- common modern simplifications or misreadings.

Never flatten materially different branches into a single voice.

#### Book route

Use:

- the book as the primary bounded corpus;
- author explanations or revisions when available;
- related works only when their relationship is explicit;
- serious criticism and counterexamples;
- evidence about application limits.

Do not silently import the author's entire worldview into a skill nominally based on one book.

### Phase 3 — Evidence ledger

Classify each source as:

- `primary`: direct work, statement, or record attributable to the subject;
- `secondary`: credible interpretation, biography, scholarship, or reporting;
- `critical`: credible counterargument, critique, failure evidence, or competing interpretation;
- `weak`: low-quality, derivative, promotional, speculative, or unverifiable material.

Use a ledger equivalent to:

```yaml
evidence_item:
  id: E001
  subject_type: person | school | book
  source_type: primary | secondary | critical | weak
  source_title: ""
  source_date: YYYY-MM-DD | unknown
  source_position: "chapter, section, timestamp, or page when available"
  context: ""
  claim_supported: ""
  directness: direct | interpreted | contextual
  independence_group: ""
  reliability: high | medium | low
  conflict_ids: []
  limitations: []
```

`independence_group` is mandatory for evidence counting. Reposts, summaries, quotations of the same interview, and articles derived from one original event count as one evidence family, not multiple independent supports.

### Phase 4 — Hybrid evidence gate

A formal build requires both a subject-specific baseline and heuristic-level support.

#### Person baseline

Require, where available:

- at least three independent primary evidence families;
- coverage across at least two time periods or two materially different contexts;
- at least one credible critical or counterexample source;
- explicit treatment of public evolution or inconsistency.

#### School baseline

Require, where available:

- at least one foundational primary text or corpus;
- at least two independent scholarly or authoritative interpretive sources;
- representation of major branches relevant to the scope;
- at least one credible critique or rival interpretation.

#### Book baseline

Require:

- inspection of the book or sufficiently complete user-provided extracts;
- coverage of the central argument, not isolated quotations;
- at least one credible critical or comparative source when the output will be reused beyond summary;
- explicit separation between the book's claims and later extrapolation.

#### Heuristic-level requirements

Each core heuristic must have:

- two independent supporting evidence points; or
- one direct, unusually strong primary source plus a `single_source` warning;
- at least one attempted search for counterevidence;
- known scope, activation conditions, and exceptions;
- calibrated confidence.

#### Saturation and budget

Stop research when either:

- new high-quality sources no longer create, split, contradict, or materially revise a core model; or
- the explicit research budget is reached.

Reaching a budget is not evidence saturation. If the evidence baseline remains unmet, return `RESEARCH_INCOMPLETE`.

### Phase 5 — Conflict classification

Do not resolve conflicts by source count alone. Classify each material conflict:

```yaml
conflict_types:
  evolution: the subject changed over time
  context: different situations activate different priorities
  branch: schools or interpretations materially diverge
  source_quality: weaker and stronger evidence conflict
  irreducible: high-quality evidence remains inconsistent
```

Apply these rules:

- `evolution`: preserve chronological versions and transition evidence;
- `context`: define activation conditions and boundary variables;
- `branch`: build separate variants; do not merge them into one voice;
- `source_quality`: down-rank weaker material and explain why;
- `irreducible`: preserve the contradiction, lower confidence, and prevent deterministic output.

Never use vague language to fabricate consistency.

### Phase 6 — Distill the reasoning model

Extract models that recur across sources or are explicitly central to the bounded corpus.

Use a model equivalent to:

```yaml
mental_model:
  id: M01
  name: ""
  proposition: ""
  decision_function: "how this model changes prioritization or choice"
  activation_conditions: []
  decision_priority: ""
  tradeoffs: []
  evidence_ids: []
  counterevidence_ids: []
  conflict_type: null
  temporal_scope: ""
  known_exceptions: []
  blind_spots: []
  neighboring_model_difference: ""
  confidence: high | medium | low
```

Reject a candidate model when it is:

- supported only by slogans or isolated quotations;
- indistinguishable from generic advice;
- derived mainly from fandom, branding, or hindsight;
- contradicted by stronger evidence without an explicit conflict model;
- too broad to produce testable decisions.

### Phase 7 — Build the executable perspective skill

Separate the formal output into five layers.

#### 1. Research facts layer

- source ledger;
- evidence quality;
- conflicts;
- temporal versions;
- confidence and exclusions.

#### 2. Reasoning rules layer

- priorities;
- causal assumptions;
- diagnostic variables;
- decision heuristics;
- trade-off rules;
- failure conditions.

#### 3. Runtime layer

For each user problem, the generated skill should:

1. classify whether the problem is in scope;
2. identify the variables the perspective treats as load-bearing;
3. activate relevant models and explain why;
4. expose internal tensions or branch differences;
5. produce a recommendation or critique with confidence;
6. separate source-supported reasoning from present-day inference;
7. state what evidence could change the result.

#### 4. Boundary layer

Define when the skill must:

- decline the perspective framing;
- switch to ordinary analysis;
- present multiple branches instead of one answer;
- lower confidence;
- request evidence;
- state that the source corpus does not cover the question.

#### 5. Expression layer

Expression cues are optional and secondary. They may describe abstraction level, structure, directness, or preferred analytical vocabulary. They must not imitate protected prose, signature phrasing, vocal mannerisms, or identity.

## Formal output contract

Return:

1. **Build state**.
2. **Scope and non-goals**.
3. **Subject-type research design**.
4. **Source ledger**.
5. **Conflict map**.
6. **Mental models**.
7. **Decision heuristics and runtime procedure**.
8. **Blind spots, exceptions, and anti-patterns**.
9. **Diagnostic questions**.
10. **Validation matrix and results**.
11. **Uncertainty and excluded claims**.
12. **Reusable skill text**, only when the release gate passes.

## Validation matrix

A formal build must use new scenarios that were not directly copied from the source examples.

Minimum coverage:

| Category | Minimum scenarios | Purpose |
|---|---:|---|
| Typical in-scope | 2 | Confirm expected activation and priorities. |
| Principle conflict | 2 | Test trade-offs and internal tension. |
| Neighboring perspective comparison | 2 | Demonstrate source-grounded distinctiveness. |
| Counterfactual input change | 2 | Confirm causal responsiveness. |
| Out-of-scope boundary | 1 | Confirm degradation or refusal. |
| Adversarial integrity | 2 | Resist worship, quotation mining, impersonation, and conflict concealment. |

Minimum total: 11 scenarios.

### Required tests

#### Traceability test

Every core conclusion identifies the model and evidence family supporting it.

#### Behavioral consistency test

Similar scenarios produce stable priorities unless a documented trigger changes the result.

#### Distinctiveness test

Compare the output with:

- a generic competent advisor; and
- a neighboring but materially different perspective.

Differences must be explainable through evidence-backed models.

#### Counterfactual test

Change one load-bearing input at a time. The judgment should change—or remain stable—for a reason encoded in the model.

#### Boundary test

The skill must detect unsupported domains, evidence gaps, and requests requiring impersonation or professional substitution.

#### Adversarial test

Test resistance to:

- invented quotations;
- selective evidence;
- fame or authority bias;
- requests to reveal private motives;
- requests to speak as the subject;
- pressure to hide contradictions;
- pressure to give false certainty.

## Release gate

A formal reusable skill is blocked when any condition is true:

- a core heuristic lacks traceable support;
- the subject-specific evidence baseline is unmet;
- a material conflict is hidden or flattened;
- the output exceeds its scope without explicit degradation;
- the framework relies on deceptive impersonation or protected-style imitation;
- two consecutive critical validation scenarios collapse into generic advice;
- neighboring-perspective differences cannot be explained from evidence;
- counterfactual behavior is arbitrary or inconsistent;
- uncertainty is materially understated.

When blocked by evidence, return `RESEARCH_INCOMPLETE`, not a low-confidence formal skill.

## Provisional scoping mode

When the user requests immediate output or research tools are insufficient, Nuwa may produce a **provisional research-scoping brief** containing:

- candidate source classes;
- candidate models labeled as hypotheses;
- likely conflicts;
- proposed validation scenarios;
- missing evidence;
- a research plan.

This mode must not:

- call itself high fidelity;
- publish a reusable perspective skill;
- present candidate heuristics as established;
- bypass the evidence or release gates.

## Interaction discipline

- Ask only questions that materially change subject identity, scope, evidence access, safety boundary, or validation design.
- Use professional defaults for reversible formatting and file-layout choices.
- Do not repeatedly ask for confirmation after the user delegates execution.
- Distinguish `source-supported`, `inferred`, `contested`, and `unknown` throughout.

## Local-agent handoff trigger

Use a bounded local-agent handoff only when the task requires processing many local source files, running repository validation, generating a multi-file package, or changing files beyond safe connector edits.

The handoff must include:

- repository, branch, current HEAD, and PR metadata when available;
- source corpus and cutoff date;
- subject route and scope;
- allowed file paths;
- copyright and impersonation constraints;
- evidence schema and conflict rules;
- minimum validation matrix;
- forbidden claims and actions;
- validation commands;
- stop conditions;
- final output format.

Require the agent to verify branch synchronization and a clean worktree before modification. Agent claims are not final evidence; verify the remote branch, diff, checks, and merge state through GitHub before approval.
