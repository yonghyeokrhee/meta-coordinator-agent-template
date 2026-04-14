# meta-coordinator-agent-template

A GitHub-ready OpenClaw agent workspace template for customer support and engineering issue triage.

`meta-coordinator` is a lightweight triage and dispatch agent that helps teams turn raw CS or ops input into structured, actionable issue handling.

It is designed for workflows such as:
- payment confirmation delays
- billing and webhook incidents
- entitlement and permission propagation failures
- support request triage
- engineering handoff and escalation
- no-response follow-up on active issues

## What this template gives you
- an agent workspace layout ready for OpenClaw
- skeleton-first intake behavior
- conservative category and severity routing
- owner and module recommendation patterns
- no-response handling guidance
- two durable record patterns:
  - issue tracker workflow
  - log-only workflow

## Included files
- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `TOOLS.md`
- `SKILL.md`
- `INSTALL.md`
- `references/tracker-workflow.md`
- `references/log-only-workflow.md`
- `references/demo-script-ko.md`

## Recommended use
Use this repo as a starter workspace for a dedicated triage agent such as `meta-coordinator`.

## Quick start
```bash
cp -R meta-coordinator-agent-template ~/.openclaw/workspace-meta-coordinator

openclaw agents add meta-coordinator \
  --workspace ~/.openclaw/workspace-meta-coordinator \
  --model openai-codex/gpt-5.4 \
  --non-interactive
```

Then test with:
```bash
openclaw agent --agent meta-coordinator --message "Customer says payment confirmation is delayed and webhook processing seems broken since this morning."
```

## Installation
See [INSTALL.md](INSTALL.md).

## Design principles
- build the issue skeleton first
- keep facts, guesses, and missing info separate
- stay conservative when evidence is weak
- do not resolve without explicit recovery confirmation
- do not confuse silence with progress

## Durable record options
### Tracker-based
Use `references/tracker-workflow.md` if you want to manage cases in Linear or another issue tracker.

### Log-only
Use `references/log-only-workflow.md` if you want to manage cases locally with files such as `cases.jsonl` or daily markdown logs.

## Example prompts
- `Customer says payment confirmation is delayed and webhook processing seems broken since this morning.`
- `Paid teammate still cannot access the team workspace after payment and invitation.`
- `Customer asks how to change the billing email on the invoice.`

## License
MIT
