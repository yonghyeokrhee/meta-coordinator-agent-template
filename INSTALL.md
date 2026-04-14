# INSTALL

## Option 1 — Use as an OpenClaw agent workspace

1. Copy this folder to your OpenClaw workspace location.

Example:
```bash
cp -R meta-coordinator-template ~/.openclaw/workspace-meta-coordinator
```

2. Add the agent in OpenClaw.

Example:
```bash
openclaw agents add meta-coordinator \
  --workspace ~/.openclaw/workspace-meta-coordinator \
  --model openai-codex/gpt-5.4 \
  --non-interactive
```

3. Open the workspace files and customize:
- `USER.md`
- `TOOLS.md`
- tracker or logging mappings in `references/`
- owner team names
- product-specific module names

4. Test the agent.

Example:
```bash
openclaw agent --agent meta-coordinator --message "Customer says payment confirmation is delayed and webhook processing seems broken since this morning."
```

## Option 2 — Use as a template repository

1. Create a new GitHub repository.
2. Copy these files into the repo root.
3. Commit and push.
4. Clone into the target machine and use it as the workspace for your triage agent.

## Optional tracker integration

If you want durable issue tracking in an issue tracker such as Linear:
- map TRIAGED / ASSIGNED / RESOLVED to your workflow states
- update tracker labels and priority mapping
- keep issue descriptions for initial triage
- keep comments for assignment, no-response follow-up, and resolution updates

If you do not use a tracker:
- use the log-only workflow in `references/log-only-workflow.md`
- store events in `cases.jsonl` or daily markdown logs

## Suggested first test prompts
- `Customer says payment confirmation is delayed and webhook processing seems broken since this morning.`
- `Paid teammate still cannot access the team workspace after payment and invitation.`
- `Customer asks how to change the billing email on the invoice.`
