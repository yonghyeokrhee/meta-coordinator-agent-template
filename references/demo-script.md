# meta-coordinator demo script

## Scenario A — billing/webhook incident
- CS intake: Customer reports payment confirmation delays and webhook failures starting this morning.
- Ops evidence: Same symptom appears across Stripe card payments after 09:05.
- No response: No engineering update for 1 hour.
- Recovery: Processing backlog drained and recent test payment confirmations are normal.

## Scenario B — permission/access issue
- CS intake: Payment succeeded but an invited teammate still cannot access the team workspace.
- Evidence: payment captured, entitlement record exists, workspace membership sync failed.
- No response: No assignee update for 3 hours.
- Resolution: membership sync replay completed and Support verified access.
