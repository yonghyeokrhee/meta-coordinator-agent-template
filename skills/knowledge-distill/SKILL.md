---
name: knowledge-distill
description: Distill markdown, docs, issue logs, help-center pages, or internal notes into a Notion knowledge system with separate Source and Answer Card databases. Use when a user asks to ingest knowledge into Notion, normalize references to canonical markdown files, update CS Knowledge Sources, derive reusable CS Answer Cards, or maintain a routing/index page for support knowledge.
---

# Knowledge Distill

Distill source material into a stable Notion knowledge base.
Prefer canonical markdown files over unstable external URLs, then derive reusable answer cards from those sources.

## Workflow

1. Identify the canonical source set.
2. Normalize each source into one `CS Knowledge Sources` row.
3. Distill reusable customer-facing patterns into `CS Answer Cards`.
4. Update the routing/index page if source precedence changed.
5. Verify the final Notion state.

## 1. Identify the canonical source set

Prefer the most stable readable artifact.

Priority order:
- canonical markdown file
- internal mirrored document
- original external URL as secondary metadata only

Do not use unstable public/share links as the primary reference when a markdown mirror exists.

If the workspace already contains a knowledge model or schema note, read `references/notion-schema.md` first.

## 2. Update `CS Knowledge Sources`

Create or update one row per durable source.

For each row:
- set a clear `Title`
- set `Source Type` based on how the document is used, not where it came from
- set `Source URL` to the canonical markdown path when possible
- keep the original external URL in notes/body only if still useful
- fill `Summary` with 1-2 operational sentences
- fill `CS Notes` with routing cautions, precedence, and escalation limits
- update `Last Reviewed`

After properties, add a short page body with these sections:
- `Distill Summary`
- `Canonical Reference`
- `Use This Source When`
- `Do Not Use Alone For`

Keep each section short and operational.

## 3. Derive `CS Answer Cards`

Create cards only for patterns that are likely to repeat.

Good card candidates:
- common support questions
- known misleading symptoms
- policy/plan wording that must stay consistent
- “when to escalate” decision points
- timeline/ETA communication rules

For each card:
- write `Answer TL;DR` in customer-safe language
- write `When to Use` as a trigger description
- write `Do Not Say` to prevent overclaiming
- write `Escalate If` with concrete thresholds
- link the relevant source titles in `Source Links`
- mark broadly reusable cards as `ready`

Prefer fewer strong cards over many narrow duplicates.
Merge with existing cards when the intent is already covered.

## 4. Maintain routing precedence

If multiple source types exist, keep an index/routing page current.
Use this pattern:
- public usage/policy questions → public help source first
- system failures, delays, ingestion issues → runbook first
- feature definitions, glossary, FAQ enrichment → integrated manual first
- known issues, roadmap, ETA questions → backlog/issue source first

## 5. Use tools

Preferred execution order:
- use file tools to inspect markdown sources
- use an existing Notion API script if the workspace provides one
- otherwise call the Notion API directly
- use browser automation only when API access is unavailable or page-body editing must be done interactively

If browser automation is required, keep actions narrow and verify the resulting page/database state after edits.

## Verification

Before finishing, verify all of the following:
- target source rows exist exactly once
- `Source URL` points to canonical markdown for mirrored sources
- summary/notes reflect current routing rules
- new answer cards appear in Notion with the intended status
- index/routing guidance still matches the current source set

## Reference

Read `references/notion-schema.md` for the current Notion database shape, field intent, and distill conventions.
