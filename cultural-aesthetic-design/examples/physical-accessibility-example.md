# Example: Wheelchair Footrest Height Adapter

> Fictional specification example. Dimensions, materials, safety and user validation are intentionally unresolved.

## Input

Create a height adapter for a wheelchair footrest for a user whose feet do not rest securely on the current platform. The product should look integrated and premium rather than medicalized.

## Human decision layer

### Verdict

`RESEARCH_ONLY` — the problem and embodied intent are clear, but geometry and safety cannot be designed from the available information.

### Target and intent

**Primary user:** wheelchair user with insufficient foot support on the current footrest.

**Primary perceptions:** secure, integrated, stable, dignified.

**Secondary perceptions:** precise, easy to clean, repairable.

**Forbidden perceptions:** improvised, medicalized, slippery, unstable, bulky without purpose.

**Embodied intent:** feet remain supported without painful pressure, sliding or unwanted leg movement; the adapter can be installed, adjusted and maintained with minimal assistance.

### Blocking evidence gaps

- wheelchair and footrest model and geometry;
- seat-to-footrest relationship;
- required height range;
- foot length, footwear and preferred ankle position;
- lower-limb movement, sensation, spasticity, pain and pressure risk;
- transfer, folding, caster and ground-clearance interactions;
- load cases, mounting points and failure consequences;
- cleaning, weather, transport and long-term wear;
- whether the user or another person must adjust it.

### Candidate directions allowed at research stage

These are mechanism hypotheses, not finished designs.

#### A — Consensus-stable

A visually quiet platform insert that follows the wheelchair's existing geometry and finish.

**Question:** can it provide enough support without reducing clearance or interfering with folding?

#### B — Utility-enhanced

An adjustable, tactile, high-friction support with visible secure mounting and easy cleaning.

**Question:** can the adjustment remain independent, stable and low-force without creating pinch points?

#### C — Brand-expression

A structural module that deliberately integrates support ribs or mounting hardware as an engineering feature.

**Question:** will visible structure communicate reliability rather than improvised modification, and does it remain safe?

### Recommendation

Do not choose geometry yet. Collect the missing body and wheelchair measurements, define the required motion and clearance envelope, and create low-risk fit prototypes before material or aesthetic refinement.

### Required validation

1. Qualified review of mounting, load and failure behavior.
2. Fit and clearance through normal movement, transfer, folding and transport.
3. Foot stability, pressure, pain, fatigue and unwanted movement over realistic duration.
4. Independent adjustment, installation and cleaning where intended.
5. Slip, edge, pinch, entrapment and collision review.
6. Perceptual test for integrated, dignified and non-medicalized appearance after functional safety is established.

## Machine-readable excerpt

```yaml
project:
  project_id: fictional-wheelchair-footrest-adapter
  domain: physical_product_accessibility
  research_depth: deep
  status: research_only

risk_routing:
  irreversibility: medium
  safety_and_bodily_consequence: high
  accessibility_and_dignity_consequence: high
  evidence_uncertainty: high
  execution_state: RESEARCH_ONLY

perceptual_intent:
  primary: [secure, integrated, stable, dignified]
  secondary: [precise, cleanable, repairable]
  forbidden: [improvised, medicalized, slippery, unstable]
  embodied:
    reach_and_access: unknown
    operation: low_force_and_independent_where_possible
    long_term_use: supported_without_pain_or_pressure_injury

evidence:
  level: L0
  confidence: very_low
  missing_evidence:
    - wheelchair_geometry
    - body_and_foot_position
    - load_and_failure_requirements
    - clearance_and_transfer
    - pain_pressure_and_sensation

gates:
  gate_0_hard_constraints:
    safety: not_tested
    accessibility_and_dignity: not_tested
    reliability_and_maintainability: not_tested
    core_task: not_tested
    verdict: not_tested

decision:
  verdict: INCONCLUSIVE
  selected_candidate: none
  rationale: geometry and safety evidence missing
```

## Why this example is compliant

- It treats lived bodily experience as consequence authority.
- It does not assume one standard wheelchair user or body.
- It keeps inclusive dignity inside the main design intent.
- It does not let “integrated and premium” override support, pressure, clearance or safety.
- It avoids exact dimensions and fabrication claims without measurements and qualified review.
