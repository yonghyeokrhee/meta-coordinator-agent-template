# Notion schema

## Databases

### CS Knowledge Sources
Purpose: store durable source material and routing notes.

Common fields:
- `Title`
- `Status`: inbox / reviewing / distilled / blocked
- `Source Type`: issue / doc / runbook / policy / notion / slack / MR
- `Product Area`
- `Feature / Module`
- `Customer Impact`
- `Keywords`
- `Source URL`
- `Confidence`
- `Last Reviewed`
- `Owner`
- `Summary`
- `CS Notes`

Recommended page-body sections:
- `Distill Summary`
- `Canonical Reference`
- `Use This Source When`
- `Do Not Use Alone For`

### CS Answer Cards
Purpose: store reusable customer-safe answer patterns.

Common fields:
- `Title`
- `Status`: draft / ready / needs-review
- `Topic`
- `Audience`: customer / internal-cs / both
- `Keywords`
- `Source Links`
- `Last Updated`
- `Answer TL;DR`
- `When to Use`
- `Do Not Say`
- `Escalate If`

## Distill conventions

### Source precedence
Prefer canonical markdown first.
Use the original public/share URL as secondary context only.

### Source typing
Choose `Source Type` by usage:
- `runbook`: operational response guide, escalation guide, batch schedule
- `doc`: feature guide, onboarding manual, glossary, FAQ
- `issue`: backlog, known issues, roadmap, bug tracker
- `policy`: public official wording that should be quoted closely

### Answer-card quality bar
Promote to `ready` only when:
- wording is reusable across multiple cases
- escalation threshold is explicit
- overclaims are removed
- the source of truth is stable

## Routing pattern

Use this default precedence unless the workspace says otherwise:
- public usage / policy / billing wording → help-center or public policy source first
- failures / delays / ingestion / system state → runbook first
- feature definitions / FAQ / metric explanations → integrated manual first
- roadmap / ETA / known issue / release status → backlog first

## Canonical-source habit

When a markdown mirror exists, set `Source URL` to that markdown path.
Examples:
- `file:///.../01_system_operations_manual...md`
- `file:///.../02_optapex_manual.md`
- `file:///.../03_optapex_backlog.md`
- `file:///.../04_help_center/00_Index.md` (섹션별 접근)

Keep the external source URL in page body notes if it helps trace origin.
