# Log-only workflow

Use this pattern when no issue tracker is available or when a lightweight local workflow is preferred.

## Storage options
- `cases.jsonl` with one case event per line
- `cases/YYYY-MM-DD.md` daily markdown logs

## Recording pattern
1. Create a case record when the issue reaches TRIAGED.
2. Append new events for ASSIGNED, no-response follow-up, mitigation, and RESOLVED.
3. Keep a stable case id across all updates.
4. Never overwrite earlier reasoning without leaving a new event.
5. Keep the log factual and operational.
