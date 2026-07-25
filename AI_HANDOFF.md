# AI Handoff

This file is the shared project state between ChatGPT and local Codex.
Keep it concise and replace outdated information instead of creating a long diary.

## Current objective

Introduce a ranking result containing:

- `paper`
- `score`
- `reasons`

Start with a failing test in `tests/test_ranking.py`.

## Current repository state

- 27 tests were passing before the current task.
- Existing ranking returns `Paper` objects.
- `paper_match_score()` and `explain_paper_match()` already exist.
- CLI works with cached data.
- No files have been changed for the current task yet.

## Last completed work

- Repository structure and V1 scope were audited.
- Ranking was selected as the first implementation step.

## Current changes

None.

## Verification

```text
pytest: 27 passed
```

## Open questions or blockers

None.

## Recommended next action

Write one failing test proving that a ranked result contains:

- the original `Paper`,
- its score,
- its matching reasons.

## Notes for the other assistant

- Do not implement the feature for the user.
- The user should write the test and implementation.
- Give one small hint at a time.
- Review the result afterward.
- Update this file at the end of the local session.
