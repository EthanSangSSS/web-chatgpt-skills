---
name: delayed-reflection-loop
version: "0.1.0"
status: beta
description: Privacy-first daily reflection workflow that preserves the user's same-day voice, delays evaluation, tracks one reversible action, and optionally persists concise Markdown records with explicit write gates.
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

The priority order is:

1. Improve decision and action quality.
2. Detect recurring concerns, emotions, judgment patterns, and execution friction.
3. Preserve a compact, authentic growth record.

This is not a full chat archive, therapy system, personality diagnosis, mood scorecard, or continuous-monitoring agent.

## Core model

Use four layers:

1. **D0 capture** — preserve the user's experience, feelings, judgments, and accepted decisions from the current day.
2. **Delayed review** — on a later active turn, examine what changed, what evidence appeared, and whether the original judgment still holds.
3. **Minimal action** — when genuinely useful, choose one reversible action that can be completed or tested quickly.
4. **Weekly and monthly synthesis** — identify patterns only after minimum sample thresholds and actively search for counterexamples.

Do not collapse D0 capture and delayed review into one interpretation, except for explicitly marked retrospective entries.

## Required configuration

Collect or infer the following once, then keep it stable until the user changes it:

- Fixed IANA timezone.
- Dedicated conversation or clearly delimited reflection context.
- Optional GitHub repository and target root.
- Daily closing phrase.
- Manual confirmation phrase.
- Automatic-mode enable phrase.
- Manual-mode restore phrase.
- Character limit.
- Backfill window.

Recommended defaults for this workflow:

| Setting | Default |
|---|---|
| Timezone | `Asia/Shanghai` |
| Closing phrase | `今天就这些，生成日记。` |
| Confirmation phrase | `确认提交` |
| Enable automatic mode | `启用自动提交` |
| Restore manual mode | `恢复人工确认` |
| Daily body limit | 300 non-whitespace Unicode code points |
| Backfill window | Previous two calendar days |
| Initial permission mode | Manual confirmation |

If the user already supplied a setting, do not ask again. Never infer the business date from VPN location, repository locale, or device metadata when a fixed timezone has been configured.

## Dedicated-conversation boundary

Treat only the configured reflection conversation, or content explicitly marked for this workflow, as input.

Do not silently collect material from unrelated technical, work, shopping, health, or project conversations. Do not reconstruct or persist the full chat transcript.

The state source should be the configured durable records when available, not the assistant's conversational memory alone.

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
---

## 当日记录

## 次日 Review
```

Allowed values:

- `status`: `pending_review | reviewed`
- `entry_mode`: `current | retrospective`
- `review_mode`: `d1 | delayed | retrospective_same_session`
- `privacy`: `anonymized`
- `action_status`: `none | open | completed | adjusted | abandoned | not_done`

A reviewed entry must contain a non-empty review plus `reviewed_at`, `review_lag_days`, and `review_mode`.

A pending entry must not pretend that review metadata exists.

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

A practical drafting budget is approximately 210 characters for D0 and 90 for the later review, but the combined hard gate is authoritative.

Do not remove a load-bearing fact solely to satisfy the limit. Redraft for density instead.

## Delayed-review trigger

The assistant cannot act merely because the user opened a page. A review becomes eligible on the user's next active message in the configured reflection context.

Before new daily capture, check for pending reviews in the durable state source when available.

Ask one high-information question:

> 回看那天，当时的判断、感受或情况后来有什么变化？

The user may answer that nothing changed. Do not invent a correction just because a review is due.

When multiple reviews are pending, start with the earliest. The user may skip a review without being blocked from recording the current day.

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

Do not stack a new action by default while an old action remains unresolved.

## Retrospective entries

Allow backfill only within the configured window, recommended as the previous two business dates.

A retrospective entry must:

- use `entry_mode: retrospective`;
- record the actual `captured_at` time;
- generate capture and review in the same session;
- use `review_mode: retrospective_same_session`;
- state or imply no false claim that the record was written contemporaneously;
- receive lower evidence weight in weekly and monthly synthesis.

Do not create a daily file outside the backfill window. Important older material may be referenced in a later synthesis as retrospective context, clearly labeled as such.

## Weekly synthesis

Offer a weekly synthesis on the first active reflection turn after the week closes.

Require at least five valid recorded days. If the threshold is not met, mark `样本不足` and do not force a pattern claim.

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

A monthly synthesis should contain:

- recurring patterns and their confidence;
- counterexamples;
- possible judgment biases, phrased as hypotheses rather than diagnoses;
- action follow-through and observed results;
- one strategy adjustment for the next month;
- supporting dates.

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

Retain a real name only when identity is necessary for a future decision or action and the user explicitly accepts it.

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

Use manual confirmation for at least the first 30 calendar days.

Present the complete draft, privacy transformations, and deterministic character count before any write.

Only the exact configured confirmation phrase authorizes the write. Silence, vague approval, or statements such as “差不多” do not authorize persistence.

When the user requests edits, replace the draft and request confirmation again. Do not persist superseded drafts.

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

Even after the gate passes, automatic mode begins only after the exact configured enable phrase.

### Automatic mode

Automatic mode may cover only:

- current daily entries;
- delayed reviews appended to existing entries.

Weekly and monthly synthesis always require explicit confirmation.

Any uncertainty about privacy, factual fidelity, identity, path conflicts, stale remote state, or validation must fall back to manual confirmation.

The exact configured restore phrase immediately returns the workflow to manual mode.

## GitHub execution boundary

GitHub persistence is optional. Use it only when:

- the repository and target root are configured;
- the connector exposes the required read and write capabilities;
- the user has authorized the current permission mode;
- content passes privacy and validation gates.

For a new daily file:

1. Read the target state or confirm the target path does not exist.
2. Create one UTF-8 Markdown file.
3. Use a small, topic-scoped commit.
4. Return the path and commit SHA from tool evidence.

For a review append:

1. Fetch the current file and blob SHA.
2. Verify that D0 remains unchanged.
3. Append the review and update metadata.
4. Update using the current blob SHA.
5. Stop on stale SHA, remote divergence, duplicate review, or unexpected content.

Do not overwrite a conflicting file. Do not claim a write succeeded without a tool result.

Use direct connector writes only for bounded single-file operations. Initial directory setup, validators, schemas, batch migrations, or other multi-file changes should use a branch and pull request or a bounded local-agent handoff.

## Output contract

### D0 draft

Return:

- business date and timezone;
- complete Markdown draft;
- D0 body character count;
- privacy substitutions made;
- action state, if any;
- persistence mode and required next instruction.

### Review draft

Return:

- source date;
- review lag;
- complete proposed appended review;
- updated combined body character count;
- action closure or `继续观察`;
- persistence mode and required next instruction.

### Successful persistence

Return only claims supported by connector evidence:

- repository-relative path;
- operation: create or update;
- commit SHA;
- combined deterministic character count;
- state: pending review or reviewed.

### Failure

State what failed and stop. Do not describe a draft as committed. Do not retry by overwriting remote changes.

## Validation gate

Before presenting or persisting any daily entry, verify:

- the business date follows the configured timezone;
- the content came only from the permitted conversation scope;
- the user's voice was not replaced by assistant interpretation;
- no fact, decision, advice acceptance, or action was invented;
- privacy substitutions are sufficient;
- prohibited sensitive content is absent;
- the combined body is within the deterministic limit;
- metadata and body state are consistent;
- D0 remains unchanged during review append;
- the action is minimal and proportionate, or the record says `继续观察`;
- the required write authorization exists;
- the remote path and blob state are current;
- no background execution claim is made.

If any check fails, revise the draft or stop the write.

## Common failure modes

### Assistant voice takeover

Failure: the record sounds polished but no longer represents the user.

Mitigation: preserve uncertainty, use the user's framing, and exclude unaccepted advice.

### Outcome-biased review

Failure: later results are used to rewrite the original judgment as obviously right or wrong.

Mitigation: preserve D0, record review lag, and reduce the weight of long-delayed reviews.

### Low-value streak logging

Failure: empty entries accumulate to protect continuity metrics.

Mitigation: skip days without meaningful content and use valid-record-day thresholds.

### Privacy drift

Failure: repeated summaries gradually retain names or identifying details.

Mitigation: anonymize by default and fall back to manual confirmation on uncertainty.

### Permission drift

Failure: automatic mode expands from daily records to high-impact monthly judgments.

Mitigation: keep weekly and monthly synthesis permanently confirmation-gated.

### State drift

Failure: chat memory and repository state disagree.

Mitigation: treat current durable files and blob SHAs as the source of truth before writes.

## Local-agent handoff trigger

Produce a bounded local-agent handoff when the task requires:

- initial multi-file project setup;
- a deterministic repository validator;
- batch repair or migration;
- local filesystem inspection;
- shell-based tests;
- repository-wide privacy scanning;
- credentials or services unavailable in the current surface.

The handoff must include repository, branch, current remote HEAD when available, file scope, forbidden actions, goal, validation commands, stop conditions, and final output format. Do not claim the handoff was executed.