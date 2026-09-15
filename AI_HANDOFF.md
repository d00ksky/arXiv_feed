# AI Handoff

Updated: 2026-09-15. Keep this file concise; replace outdated state rather than appending a diary.

## Current objective

Prepare the existing digest application for its first private AWS run, then scheduled delivery. The immediate outcome is a reproducible installation and a complete digest run in a fresh environment.

Give the user this outcome and completion criteria, leaving the implementation approach to them. Detailed guidance is available for concrete questions.

## Current repository state

Confirmed by static inspection of main at `ef3cc2bac80e65cf312e69b7667eff1203695e50`:

- The CLI connects fetching and normalization to ranking, AI summaries, rendering, and optional email delivery.
- Ranking already returns `RankedPaper` objects with `paper`, `score`, and `reasons`; zero-score results are excluded.
- Negative selection limits raise `ValueError`; a zero limit returns an empty list.
- Both title and paper scoring return zero for an empty query.
- There is no dependency manifest or AWS deployment configuration yet.

The user previously reported successful CLI/email delivery and passing tests after the ranking fixes. Those reports are not a fresh test run.

## Last completed work

- Updated collaboration rules to favor independent, useful tasks and proportionate verification.
- Replaced obsolete ranking instructions in this handoff.
- Aligned README and V1 delivery stages with the private digest objective.
- Added copyable ChatGPT project instructions.

The initial assessment is closed. Further learning and assessment happen during feature work.

## Verification

Documentation was checked against the current source and reviewed for consistency. No application tests or live API/email calls were run for this documentation change.

## Recommended next action

Make the application installable and runnable in a fresh environment using repository-defined dependencies and documented configuration.

Completion criteria:

- Runtime dependencies and the working Python version are documented.
- A fresh environment can install those dependencies and start the CLI.
- With the required configuration and network access, a real digest is generated and delivered.

The manifest format and implementation approach are left to the user. Local dependency versions are not yet recorded.

## Delivery order and deferred work

Follow the stages in `docs/v1.md`: reproducible local run, first manual AWS run, schedule and usefulness review, then remaining V1 requirements.

The local report fallback is deferred until the later V1 stage, not removed from scope. Whitespace-only queries and cosmetic changes are nonblocking follow-ups, not the next assignment.

## Remaining setup

The owner must paste `docs/chatgpt-project-instructions.md` into the ChatGPT project's instruction field. This PR does not update that setting. Remove this note once the owner confirms it is done.
