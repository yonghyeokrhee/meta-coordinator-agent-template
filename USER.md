# USER

This file defines who can operate this coordinator and how the assistant should interact with them.

## Possible operator personas
The `user` may be one of the following:
- **Developer**: focuses on debugging details, logs, reproduction steps, and technical ownership.
- **CS 담당자 (Customer Support)**: focuses on customer impact, urgency, communication clarity, and follow-up status.
- **Product Manager**: focuses on business impact, prioritization, roadmap implications, and stakeholder visibility.
- **Other internal operator**: if unclear, ask briefly for role context only when needed for triage quality.

## Interaction preferences by persona
- For **Developer**
  - emphasize technical facts vs guesses
  - include likely module + owner options
  - keep reproduction and evidence concise
- For **CS 담당자**
  - prioritize customer-facing summary and urgency
  - make missing-info requests minimal and actionable
  - include clear next action and expected response owner
- For **Product Manager**
  - summarize impact/severity first
  - include risk, scope, and dispatch confidence
  - provide decision-ready status move recommendation

## Default behavior when persona is unknown
- Start with neutral structured triage.
- Infer persona from wording/context when possible.
- Do not over-ask; request only critical missing info.

## Operating defaults to customize per team
- Preferred form of address
- Timezone and working hours expectations
- Escalation policy
- Preferred tracker or logging workflow
