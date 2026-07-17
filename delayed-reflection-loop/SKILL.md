---
name: delayed-reflection-loop
version: "0.2.0"
status: beta
description: Privacy-first daily reflection workflow that preserves the user's same-day voice, delays evaluation, tracks one reversible action, and optionally persists concise Markdown records with explicit state and write gates.
triggers:
  - delayed reflection
  - daily reflection
  - next-day review
  - journal workflow
  - diary workflow
  - growth log
  - 每日日记
  - 次日复盘
  - 延迟复盘
  - 成长记录
do_not_use_for:
  - immediate safety or crisis response
  - therapy, diagnosis, or medical assessment
  - raw conversation archiving
  - covert monitoring or background surveillance
  - storing secrets or sensitive employer data
requires:
  web: false
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Delayed Reflection Loop

## Purpose

Turn an ongoing personal conversation into a concise, privacy-bounded reflection record without allowing the assistant's same-day interpretation to replace the user's own voice.

Priority order:

1. Improve decision and action quality.
2. Detect recurring concerns, emotions, judgment patterns, and execution friction.
3. Preserve a compact, authentic growth record.

This is not a full chat archive, therapy system, personality diagnosis, mood scorecard, streak tracker, or continuous-monitoring agent.

## Core model

Use four layers:

1. **D0 capture** — preserve the user's experience, feelings, judgments, uncertainty, and accepted decisions from the current day.
2. **Delayed review** — on a later active turn, examine what changed, what evidence appeared, and whether the original judgment still holds.
3. **Minimal action** — when genuinely useful, choose one reversible action that can be completed or tested quickly.
4. **Weekly and monthly synthesis** — identify patterns only after minimum sample thresholds and actively search for counterexamples.

Do not collapse D0 capture and delayed review into one interpretation, except for explicitly marked retrospective entries.

## Required configuration

Collect or infer the following once, then keep it stable until the user changes it:

- Fixed IANA timezone.
- Dedicated conversation or clearly delimited reflection context.
- Optional durable-state location.
- Optional GitHub repository and target root.
- Daily closing phrase.
- Manual confirmation phrase.
- Automatic-mode enable phrase.
- Manual-mode restore phrase.
- Character limit.
- Backfill window.

Recommended defaults:

| Setting | Default |
|---|---|
| Timezone | `Asia/Shanghai` |
| Closing phrase | `今天就这些，生成日记。` |
| Confirmation phrase | `确认提交` |
| Enable automatic mode | `启用自动提交` |
| Restore manual mode | `恢复人工确认` |
| Daily body limit | 300 non-whitespace Unicode code points |
| Backfill window | Previous two calendar dates |
| Initial permission mode | Manual confirmation |

If the user already supplied a setting, do not ask again. Never infer the business date from VPN location, repository locale, or device metadata when a fixed timezone has been configured.

## Durable workflow state

The workflow must have a durable source of truth before it claims that automatic mode is active, that a review is pending, or that a weekly or monthly synthesis is due.

Recommended state contract:

```yaml
manual_phase_started_at: ISO-8601 timestamp or null
permission_mode: manual | automatic
automatic_enabled_at: ISO-8601 timestamp or null
last_weekly_period: YYYY-Www or null
last_monthly_period: YYYY-MM or null
pending_review_dates: []
last_updated_at: ISO-8601 timestamp
```

Rules:

- `manual_phase_started_at` begins when the first valid D0 is successfully persisted, not when the skill is first mentioned or configured.
- `permission_mode: automatic` is valid only after the thirty-day quality audit passes and the configured enable phrase is received.
- `pending_review_dates` contains only successfully persisted D0 dates that are still pending review.
- A skipped review remains pending unless the user explicitly abandons it.
- Weekly and monthly period markers prevent duplicate synthesis generation.
- Durable files and current blob SHAs outrank conversational memory.
- If durable state is absent, unreadable, stale, or contradictory, fall back to manual confirmation and do not claim that an item is due.
- Manual fallback still allows the user to request and confirm a new D0; it does not authorize automatic review scheduling or automatic writes.
- Do not silently reconstruct permission state from previous chat wording.

## Dedicated-conversation boundary

Treat only the configured reflection conversation, or content explicitly marked for this workflow, as input.

Do not silently collect material from unrelated technical, work, shopping, health, or project conversations. Do not reconstruct or persist the full chat transcript.

## Same-day interaction policy

Default to listening and necessary clarification.

- Do not provide unsolicited analysis, advice, personality interpretation, or long-term pattern claims.
- The user may explicitly ask for analysis or advice; respond normally when asked.
- Advice from the assistant is not automatically part of D0.
- Record advice only when the user explicitly accepts it as a decision or intended action.
- Do not write a diary merely to preserve a streak.

If the day contains no material experience, concern, decision, insight, or change worth preserving, skip the entry.

## D0 generation trigger

Generate a draft only after the user invokes the configured closing phrase or gives an equivalent explicit instruction.

The D0 draft must:

- use the user's perspective and language level;
- preserve uncertainty rather than resolving it artificially;
- separate observed facts from feelings and judgments when the distinction matters;
- omit assistant reasoning, hidden analysis, and unaccepted advice;
- avoid personality labels and long-term conclusions;
- contain only enough context for future decisions and review.

## Draft identity and authorization

Every persistable draft must have a unique revision identifier:

```text
draft_id: YYYY-MM-DD-d0-rN
```

Use `review` or `weekly` / `monthly` in the identifier for those artifact types.

Authorization rules:

- The configured confirmation phrase authorizes only the latest complete draft shown to the user.
- The authorization must bind to the current `draft_id`.
- A safer accepted form is `确认提交 <draft_id>` when the surface supports it.
- Any edit, regenerated wording, date change, privacy change, metadata change, or artifact-type change creates a new revision and invalidates the prior authorization.
- A confirmation from an earlier message must not authorize a later revision.
- Silence, vague approval, or phrases such as “差不多” do not authorize persistence.
- An unconfirmed draft is not a durable record and must not enter `pending_review_dates`.
- Repeated generation for the same date must resolve to one of: `NO_OP`, revised unpersisted draft, or conflict. It must not create a duplicate file.

## Canonical daily record

When Markdown persistence is configured, use one file per business date:

```text
entries/YYYY/MM/YYYY-MM-DD.md
```

Recommended schema:

```yaml
---
date: YYYY-MM-DD
timezone: Asia/Shanghai
status: pending_review
entry_mode: current
captured_at: ISO-8601 timestamp
themes: []
privacy: anonymized
reviewed_at:
review_lag_days:
review_mode:
action_status: none
action_text:
action_created_at:
action_reviewed_at:
action_result:
action_source_date:
---

## 当日记录

## 次日 Review
```

Allowed values:

- `status`: `pending_review | reviewed`
- `entry_mode`: `current | retrospective`
- `review_mode`: `d1 | delayed | retrospective_same_session`
- `privacy: no_identifiers | anonymized | user_approved_identifiers`
- `action_status`: `none | open | completed | adjusted | abandoned | not_done`

Consistency rules:

- A reviewed entry must contain a non-empty review plus `reviewed_at`, `review_lag_days`, and `review_mode`.
- A pending entry must not contain populated review metadata.
- `privacy: user_approved_identifiers` requires explicit user acceptance of the identifiers retained.
- `action_status: open` requires `action_text`, `action_created_at`, and `action_source_date`.
- A closed action requires `action_reviewed_at` and a short `action_result`.
- The Chinese action labels map as follows: `完成 → completed`, `调整 → adjusted`, `放弃 → abandoned`, `未执行 → not_done`.

## Valid recorded day

A valid recorded day is a successfully persisted daily file that:

- has a non-empty D0 body;
- passes the schema and privacy rules;
- passes the deterministic character gate;
- has a unique business date within the target root;
- has a tool-supported successful write result.

Review completion is not required for the day to count as a valid D0 sample. Review coverage is measured separately.

## Character gate

Count only the body under:

- `## 当日记录`
- `## 次日 Review`

Exclude:

- YAML front matter;
- Markdown headings;
- spaces;
- tabs;
- line breaks.

Count Chinese characters, Latin characters, digits, and punctuation as Unicode code points. The combined body must be no more than 300 characters.

Use a deterministic counter when an available tool or validator can provide one. Do not claim an exact character count based only on visual estimation. If deterministic counting is unavailable, shorten conservatively, label the count as estimated, and keep automatic submission disabled.

Use a soft D0 budget of approximately 220 characters to preserve room for review. The combined hard gate remains authoritative.

Do not remove a load-bearing fact solely to satisfy the limit. Redraft for density instead.

## Delayed-review trigger

The assistant cannot act merely because the user opened a page. A review becomes eligible on the user's next active message in the configured reflection context.

Before new daily capture, read durable state when available. Do not infer a pending review solely from chat memory.

Ask one high-information question:

> 回看那天，当时的判断、感受或情况后来有什么变化？

The user may answer that nothing changed. Do not invent a correction just because a review is due.

When multiple reviews are pending, start with the earliest. Propose at most one backlog review per active turn unless the user explicitly asks to process more. The user may skip a review without being blocked from recording the current day.

## Review rules

Append review content to the original file. Do not rewrite the D0 body.

Record:

```yaml
reviewed_at: ISO-8601 timestamp
review_lag_days: integer
review_mode: d1 | delayed | retrospective_same_session
```

Evidence weighting:

- D1: normal delayed-review weight.
- D2-D7: delayed; note that later events may influence interpretation.
- More than seven days: treat as retrospective explanation, not as a reliable immediate cooling-off judgment.

The review may state:

- what changed;
- what did not change;
- evidence that strengthened or weakened the original view;
- whether the issue remains unresolved;
- one minimal action, or `继续观察`.

## Minimal-action loop

Generate an action only when it is genuinely useful.

A valid minimal action should be:

- reversible;
- low cost;
- feasible the same day or in one short cycle;
- specific enough to verify;
- proportionate to the evidence.

Otherwise write `继续观察`.

On the next relevant review, close the action using one state:

- `完成`
- `调整`
- `放弃`
- `未执行`

Add one short statement about actual effect or execution friction. Do not treat non-execution as moral failure. Distinguish poor action design, changed priorities, and practical barriers.

Do not stack a new action by default while an old action remains unresolved. When an action is adjusted, close the old action as `adjusted` and create a new action with a new source date rather than silently replacing it.

## Retrospective entries

Allow backfill only within the configured window: Previous two calendar dates in the configured timezone.

A retrospective entry must:

- use `entry_mode: retrospective`;
- record the actual `captured_at` time;
- generate capture and review in the same session;
- use `review_mode: retrospective_same_session`;
- avoid any claim that the record was written contemporaneously;
- receive lower evidence weight in weekly and monthly synthesis.

Do not create a daily file outside the backfill window. Important older material may be referenced in a later synthesis as retrospective context, clearly labeled as such.

## Weekly synthesis

Offer a weekly synthesis on the first active reflection turn after the week closes.

Require at least five valid recorded days. If the threshold is not met, mark `样本不足` and do not force a pattern claim.

Canonical path:

```text
weekly/YYYY/YYYY-Www.md
```

Recommended metadata:

```yaml
period: YYYY-Www
generated_at: ISO-8601 timestamp
valid_entry_days: integer
reviewed_entry_days: integer
evidence_dates: []
counterexample_dates: []
status: draft | confirmed
```

A weekly synthesis should contain:

- repeated themes;
- unresolved decisions;
- effective and ineffective actions;
- execution friction;
- one focus for the next week;
- supporting dates;
- at least one searched-for counterexample when making a pattern claim.

Weekly synthesis is not subject to the 300-character daily limit, but it should remain concise.

## Monthly synthesis

Offer a monthly synthesis on the first active reflection turn after the month closes.

Require at least fifteen valid recorded days. If the threshold is not met, mark `样本不足` and avoid stable-personality or long-term-trend claims.

Canonical path:

```text
monthly/YYYY/YYYY-MM.md
```

Recommended metadata:

```yaml
period: YYYY-MM
generated_at: ISO-8601 timestamp
valid_entry_days: integer
reviewed_entry_days: integer
evidence_dates: []
counterexample_dates: []
status: draft | confirmed
```

A monthly synthesis should contain:

- recurring patterns and their confidence;
- counterexamples;
- possible judgment biases, phrased as hypotheses rather than diagnoses;
- action follow-through and observed results;
- one strategy adjustment for the next month;
- supporting dates.

## Synthesis idempotency

For each weekly or monthly period:

- there may be at most one confirmed durable file;
- read the canonical path and durable period marker before generating;
- identical existing content is `NO_OP`;
- a changed confirmed file requires a new explicit draft and confirmation;
- unexpected existing content or stale remote state is a conflict and must not be overwritten;
- update the durable period marker only after a successful confirmed write.

## Due-item order

When multiple items are due, use this order:

1. Earliest pending daily review.
2. Weekly synthesis.
3. Monthly synthesis.
4. Current-day capture.

The user may explicitly skip any due review or synthesis. Skipping must not block the current conversation or daily record.

## Privacy policy

Persist only the concise diary, review, and approved synthesis. Do not persist raw chat, hidden reasoning, or a detailed reconstruction of venting.

Default to anonymization:

- colleague;
- family member;
- a project;
- an interview;
- a supplier or external party.

Use privacy states consistently:

- `no_identifiers`: no person, organization, project, or account identifiers are retained.
- `anonymized`: generalized relational labels are retained.
- `user_approved_identifiers`: specific identifiers are retained only because they are necessary for a future decision or action and the user explicitly accepted them.

Do not store:

- credentials, tokens, keys, account data, or contact details;
- unreleased employer or customer information;
- supplier quotations, contract terms, or proprietary source material;
- precise medical records;
- identifying details about another person when abstraction is sufficient;
- crisis-response details unless the user later gives explicit, informed permission for a highly redacted note.

A private GitHub repository is access-restricted version control, not an end-to-end encrypted diary vault. Say this when the user is choosing or changing persistence.

## Safety override

If the conversation suggests immediate danger, serious health risk, self-harm risk, or another urgent safety issue:

1. Pause diary generation and delayed evaluation.
2. Follow the platform's current safety-response requirements.
3. Prioritize immediate help and risk reduction.
4. Do not persist sensitive crisis details by default.
5. Resume reflection only after the urgent issue has been addressed sufficiently for normal conversation.

Do not wait until the next day to respond to an urgent risk.

## Permission lifecycle

### Manual-confirmation phase

Use manual confirmation for at least the first 30 calendar days beginning at `manual_phase_started_at`.

Present the complete draft, `draft_id`, privacy transformations, and deterministic character count before any write.

Only the exact configured confirmation phrase bound to the current `draft_id` authorizes the write. When the user requests edits, create a new revision and request confirmation again. Do not persist superseded drafts.

### Thirty-day quality audit

Thirty days trigger an audit, not an automatic permission change.

Recommended minimum gate:

| Metric | Requirement |
|---|---:|
| Valid daily entries | at least 15 |
| Reviews | at least 10 |
| Factual misstatements | 0 |
| Sensitive-data capture incidents | 0 |
| Unsupported personality judgments | 0 |
| Daily body-limit violations | 0 |
| Entries needing substantive user rewrite | no more than 10% |
| Persistence failures | no more than 1, with cause resolved |

Even after the gate passes, automatic mode begins only after the exact configured enable phrase is received and durable state is successfully updated.

### Automatic mode

Automatic mode may cover only:

- current daily entries;
- delayed reviews appended to existing entries.

Weekly and monthly synthesis always require explicit confirmation.

Any uncertainty about privacy, factual fidelity, identity, draft identity, durable state, path conflicts, stale remote state, or validation must fall back to manual confirmation.

The exact configured restore phrase immediately returns the workflow to manual mode and updates durable state.

## GitHub execution boundary

GitHub persistence is optional. Use it only when:

- the repository and target root are configured;
- the connector exposes the required read and write capabilities;
- durable permission state is readable;
- the user has authorized the current permission mode;
- content passes privacy and validation gates.

For a new daily file:

1. Read durable state.
2. Read the target path or confirm it does not exist.
3. If identical content already exists, return `NO_OP`.
4. If conflicting content exists, stop.
5. Create one UTF-8 Markdown file.
6. Update durable state only after the write succeeds.
7. Return the path and commit SHA from tool evidence.

For a review append:

1. Fetch the current file and blob SHA.
2. Verify that D0 remains byte-for-byte unchanged.
3. Verify the review is not already present.
4. Append the review and update metadata.
5. Update using the current blob SHA.
6. Update durable state only after the write succeeds.
7. Stop on stale SHA, remote divergence, duplicate review, or unexpected content.

For weekly or monthly synthesis:

1. Read the canonical period path and durable period marker.
2. Require explicit confirmation bound to the current synthesis `draft_id`.
3. Treat identical content as `NO_OP`.
4. Stop on conflicting existing content.
5. Update the period marker only after a successful write.

Do not overwrite a conflicting file. Do not claim a write succeeded without a tool result.

Use direct connector writes only for bounded single-file operations. Initial directory setup, validators, schemas, batch migrations, or other multi-file changes should use a branch and pull request or a bounded local-agent handoff.

## Output contract

### D0 draft

Return:

- `draft_id`;
- business date and timezone;
- complete Markdown draft;
- D0 body character count;
- privacy substitutions made;
- action state, if any;
- persistence mode and required next instruction.

### Review draft

Return:

- `draft_id`;
- source date;
- review lag;
- complete proposed appended review;
- updated combined body character count;
- action closure or `继续观察`;
- persistence mode and required next instruction.

### Synthesis draft

Return:

- `draft_id`;
- period and canonical path;
- valid and reviewed sample counts;
- evidence dates and counterexample dates;
- complete draft;
- required confirmation instruction.

### Successful persistence

Return only claims supported by connector evidence:

- repository-relative path;
- operation: create, update, or `NO_OP`;
- commit SHA when a write occurred;
- combined deterministic character count for daily files;
- state: pending review, reviewed, or confirmed synthesis;
- durable-state update result when separately stored.

### Failure

State what failed and stop. Do not describe a draft as committed. Do not retry by overwriting remote changes.

## Validation gate

Before presenting or persisting an artifact, verify:

- the business date follows the configured timezone;
- the content came only from the permitted conversation scope;
- the user's voice was not replaced by assistant interpretation;
- no fact, decision, advice acceptance, or action was invented;
- privacy substitutions and privacy enum are consistent;
- prohibited sensitive content is absent;
- the daily combined body is within the deterministic limit;
- metadata and body state are consistent;
- the `draft_id` is current and authorization is bound to it;
- durable permission and due-item state are readable;
- D0 remains unchanged during review append;
- action metadata identifies the action being closed;
- weekly or monthly paths are idempotent for the period;
- the action is minimal and proportionate, or the record says `继续观察`;
- the remote path and blob state are current;
- no background execution claim is made.

If any check fails, revise the draft, fall back to manual mode, or stop the write.

## Contract fixtures

The repository contract fixtures are stored at:

```text
tests/fixtures/delayed-reflection-loop/cases.json
```

The dependency-free checker is:

```text
python3 scripts/check_delayed_reflection_contract.py
```

The fixtures must cover at least:

- current-draft authorization and stale-draft rejection;
- the 300-character hard gate;
- pending/reviewed metadata consistency;
- retrospective same-session review;
- all privacy enum states;
- D0 immutability during review append;
- duplicate-path `NO_OP` versus conflict stop;
- missing durable-state fallback;
- permanent confirmation for weekly/monthly synthesis;
- urgent-safety persistence stop.

## Common failure modes

### Assistant voice takeover

Failure: the record sounds polished but no longer represents the user.

Mitigation: preserve uncertainty, use the user's framing, and exclude unaccepted advice.

### Outcome-biased review

Failure: later results are used to rewrite the original judgment as obviously right or wrong.

Mitigation: preserve D0, record review lag, and reduce the weight of long-delayed reviews.

### Stale-draft authorization

Failure: an old confirmation phrase is applied to a revised draft.

Mitigation: bind authorization to the current `draft_id` and invalidate it on any revision.

### Low-value streak logging

Failure: empty entries accumulate to protect continuity metrics.

Mitigation: skip days without meaningful content and use valid-record-day thresholds.

### Privacy drift

Failure: repeated summaries gradually retain names or identifying details.

Mitigation: use the explicit privacy enum and fall back to manual confirmation on uncertainty.

### Permission drift

Failure: automatic mode expands from daily records to high-impact monthly judgments.

Mitigation: keep weekly and monthly synthesis permanently confirmation-gated.

### State drift

Failure: chat memory and durable records disagree.

Mitigation: treat durable workflow state, current files, and blob SHAs as the source of truth; otherwise fall back to manual mode.

### Duplicate-period synthesis

Failure: repeated conversation entry creates multiple weekly or monthly files for the same period.

Mitigation: use canonical paths, durable period markers, and `NO_OP` / conflict handling.

## Local-agent handoff trigger

Produce a bounded local-agent handoff when the task requires:

- initial multi-file project setup;
- a deterministic repository validator not already available;
- batch repair or migration;
- local filesystem inspection;
- shell-based tests;
- repository-wide privacy scanning;
- credentials or services unavailable in the current surface.

The handoff must include repository, branch, current remote HEAD when available, file scope, forbidden actions, goal, validation commands, stop conditions, and final output format. Do not claim the handoff was executed.
