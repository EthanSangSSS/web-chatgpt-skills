## Summary

<!-- Explain what changed and why it matters for skill users or maintainers. -->

## Scope

- [ ] Skill package change
- [ ] Catalog / registry change
- [ ] Documentation / governance change
- [ ] Validation / CI change
- [ ] Example / fixture change
- [ ] Release-readiness change
- [ ] Other:

## Maintenance evidence

- Related issue or maintenance task:
- Expected user impact:
- Backward-compatibility notes:
- Release checklist impact:

## Safety and execution-boundary checklist

- [ ] No secrets, tokens, credentials, private keys, private logs, or private source dumps are included.
- [ ] The change does not claim local execution, tests, builds, or background work without evidence.
- [ ] New or changed skill instructions define tool boundaries and escalation rules.
- [ ] Any local-agent handoff instructions include repo, branch, HEAD/PR metadata when available, file scope, forbidden actions, validation commands, stop conditions, and final output format.
- [ ] Any web-facing or reusable text avoids unverifiable claims about project adoption, downloads, or external usage.
- [ ] Prompt-security review was applied when skill instructions, examples, CI scripts, or local-agent handoffs changed.

## Validation performed

<!-- Replace with actual evidence. Do not write PASS unless the command or review was actually performed. -->

- [ ] `python3 scripts/validate_catalog.py`
- [ ] `python3 scripts/check_public_safety.py`
- [ ] `python3 scripts/check_unsafe_claims.py`
- [ ] `python3 scripts/list_changed_skills.py`
- [ ] Manual README / catalog review
- [ ] Manual prompt-security review
- [ ] Not run; reason:

## Reviewer notes

<!-- Call out risks, known limitations, or follow-up work. -->
