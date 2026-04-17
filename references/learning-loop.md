# Learning loop workflow

Use this lightweight loop to improve triage quality from past resolved cases without slowing active incident handling.

## When to run
- minimum: once per week
- recommended: after high-impact incidents

## Input sources
- tracker issues/comments (if using a tracker)
- `cases.jsonl` or daily logs (if using log-only mode)

## Review template (per case)
1. Which first signal best predicted the true module?
2. Was the initial severity too high / too low / appropriate?
3. Did primary owner routing work on first try?
4. Which missing-info question would have changed the outcome fastest?
5. Should we update module-owner fallback mapping?

## Output artifacts
- short “routing improvements” note
- updated module-owner mapping in local ops docs
- optional prompt tweak in `AGENTS.md` / `SKILL.md`

## Guardrails
- avoid hindsight blame
- keep changes incremental
- do not rewrite historical facts; append corrective notes
