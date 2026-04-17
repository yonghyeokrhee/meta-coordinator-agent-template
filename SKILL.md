---
name: meta-coordinator
description: Lightweight CS and engineering issue triage with skeleton-first intake, conservative severity/category routing, ownership recommendation, no-response follow-up handling, strict state management (NEW/TRIAGED/ASSIGNED/RESOLVED), and continuous learning from resolved cases through either an issue tracker or plain logs.
---

# Meta Coordinator

Turn raw CS or ops input into a durable, operationally useful issue record.

## Core workflow
1. Build the issue skeleton first.
2. Summarize and classify the issue.
3. Estimate severity conservatively.
4. Infer up to 2 likely modules.
5. Recommend one primary owner and one backup owner.
6. Move the issue through `NEW -> TRIAGED -> ASSIGNED -> RESOLVED`.
7. If the issue is quiet, generate explicit no-response follow-up guidance.
8. Keep a durable handling record in an issue tracker or plain logs.
9. After confirmed resolution, append compact learning notes for future routing quality.

## Required output structure
- Issue Skeleton
- Quick Triage
- Facts / Guesses / Missing Info
- Likely Module
- Owner Suggestion
- Next Actions
- Status Move

## Resolution gate
Use `RESOLVED` only when recovery is confirmed by a human or explicit message.
No-response is never equal to resolution.

## Durable record options
- Tracker-based workflow: see `references/tracker-workflow.md`
- Log-only workflow: see `references/log-only-workflow.md`
- Learning loop workflow: see `references/learning-loop.md`

## Example prompts
- Customer says payment confirmation is delayed and webhook processing seems broken since this morning.
- Paid teammate still cannot access the team workspace after payment and invitation.
- Customer asks how to change the billing email on the invoice.
