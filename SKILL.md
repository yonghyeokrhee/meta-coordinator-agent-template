---
name: meta-coordinator
description: Lightweight CS and engineering issue triage with skeleton-first intake, conservative severity/category routing, ownership recommendation, no-response follow-up handling, and durable case tracking through either an issue tracker such as Linear or plain log files. Use when handling customer-reported incidents, payment confirmation delays, entitlement or permission propagation issues, billing/webhook problems, support triage, or when converting loose CS notes into structured issue records and lifecycle updates.
---

# Meta Coordinator

Turn raw CS or ops input into a durable, operationally useful issue record.

## Core workflow
1. Build the issue skeleton first.
2. Summarize and classify the issue.
3. Estimate severity conservatively.
4. Infer the most likely module.
5. Recommend a primary owner and backup owner.
6. Move the issue through NEW -> TRIAGED -> ASSIGNED -> RESOLVED.
7. If the issue is quiet, generate explicit no-response follow-up guidance.
8. Keep a durable handling record either in an issue tracker or in plain logs.

## Skeleton-first structure
- Customer Issue
- Reported Symptom
- Product/Plan
- Time First Noticed
- Scope
- Payment/Order Reference
- Customer Identifier
- Current Impact
- Known Signals
- Missing Critical Info

## Durable record options
- Tracker-based workflow: see `references/tracker-workflow.md`
- Log-only workflow: see `references/log-only-workflow.md`

## Example prompts
- Customer says payment confirmation is delayed and webhook processing seems broken since this morning.
- Paid teammate still cannot access the team workspace after payment and invitation.
