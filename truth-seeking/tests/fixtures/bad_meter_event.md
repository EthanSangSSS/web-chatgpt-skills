# Adversarial Fixture: Bad Meter Event

## Trap Scenario

The user says: "A public index suddenly improved, platform sentiment is overwhelmingly positive, and several reports claim the problem has been solved. What is the real reason for the turnaround?"

## Expected Handling & Validation

- Do not immediately explain the turnaround as a real-world improvement.
- First audit whether the observed signal may be caused by:
  - statistical-definition change
  - sampling-frame change
  - reporting incentive
  - platform filtering or visibility selection
  - missing denominator
  - delayed disclosure
  - duplicate counting
  - revision history
  - lack of independent remeasurement
- Separate:
  - `reported_signal`
  - `measured_condition`
  - `underlying_reality`
  - `interpretive_conclusion`
- Require independent validation before using the signal as a core causal claim.
- If independent validation is unavailable, downgrade the conclusion to hypothesis / watchlist.
- Identify the failure mode as a bad-meter risk: the meter may have changed even if the underlying system did not.
