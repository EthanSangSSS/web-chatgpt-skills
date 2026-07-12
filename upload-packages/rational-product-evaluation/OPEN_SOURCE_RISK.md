# Open Source Risk Review

Review date: 2026-07-04

## Scope

Only the standalone `rational-product-evaluation` skill package is intended for publication:

- `SKILL.md`
- `references/*.md`
- repository documentation and license files

The following local/global materials are intentionally excluded:

- Codex global skill manifest
- local memories
- attachments
- shell history
- credentials
- private repo metadata
- machine-specific configuration

## Risk Assessment

| Risk | Status | Notes |
|---|---|---|
| Secrets or API keys | No finding in scoped scan | No token-like or credential strings were found in the publish package. |
| Local filesystem paths | No finding in scoped scan | No absolute home-directory paths, SSH paths, or local service paths are present in the skill content. Generic Codex skill install paths are documented in the README. |
| Private/personally identifying context | No finding in scoped scan | The package contains generic product-evaluation instructions, not private user data. |
| Proprietary source material | Low observed risk | Content is original workflow guidance and short generic examples. |
| Public controversy or misinterpretation | Documented | The source-jurisdiction rule is framed as evidence-quality discipline and not as a political or identity claim. |
| Regulated advice risk | Documented | The skill excludes medical, legal, financial, insurance, investment, and regulated procurement advice. |
| Stale factual claims | Managed by skill behavior | The skill requires freshness checks for current products, prices, lifecycle, recalls, and market conditions. |
| Behavior regression coverage | Lightweight coverage added | Smoke prompts cover volatile GPU purchases, overbuy-prone router choices, and output-audit mode. |

## Residual Risks

- Public users may apply the skill to regulated or high-stakes domains despite the stated boundary.
- Source-quality rules may be misunderstood if quoted without the surrounding context.
- Market-regime judgments are inherently probabilistic and require current sources.
- The package includes lightweight smoke prompts, but not an automated evaluator or factual golden set.

## Publication Decision

No P0/P1 open-source blockers were found in the scoped package. Publish is acceptable if the repository contains only the standalone skill package and this risk note.
