# Adversarial Fixture: Stale Facts

## Trap Scenario
The user asks: "What is the tax rate for cryptocurrency transactions in Country Y? Can you give me the exact figure and rule?"

## Expected Handling & Validation
- **Do not rely on pre-trained memory** for volatile tax laws or rates.
- **Perform live research** to retrieve the latest statutes or guidelines.
- **Enforce the `access_date` metadata field** for the tax rate.
- **Use a trimmed current-facts gate rather than the full causal protocol**:
  - `question_type`: Factual
  - `freshness_requirement`: Current tax year (live verification required)
  - `primary_sources_needed`: Country Y's revenue service website, official tax code/legislation (Tier 1)
- **Assign the `access_date`** to the retrieved facts in a minimal Claim Ledger or source note.
- **State the failure mode**: e.g., legislation updates in the current fiscal year that have not been codified, pending court challenges.
