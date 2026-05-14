#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=0
if [[ "${1-}" == "--dry-run" ]]; then
  DRY_RUN=1
fi

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: not a git repository: $ROOT_DIR" >&2
  exit 2
fi

branch="$(git branch --show-current)"
if [[ -z "$branch" ]]; then
  echo "ERROR: detached HEAD; refusing autosync" >&2
  exit 2
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "ERROR: remote 'origin' is missing" >&2
  exit 2
fi

status_before="$(git status --short)"
if [[ -z "$status_before" ]]; then
  echo "NO_CHANGES"
  exit 0
fi

if [[ "$DRY_RUN" == "1" ]]; then
  echo "WOULD_COMMIT"
  printf '%s
' "$status_before"
  exit 0
fi

git add -A

if git diff --cached --quiet; then
  echo "NO_CHANGES"
  exit 0
fi

ts="$(TZ=Asia/Seoul date '+%Y-%m-%d %H:%M KST')"
commit_msg="chore: workspace autosync ${ts}"

git commit -m "$commit_msg" >/tmp/git_autosync_commit.log 2>&1 || {
  cat /tmp/git_autosync_commit.log >&2
  exit 1
}

git push origin "$branch" >/tmp/git_autosync_push.log 2>&1 || {
  cat /tmp/git_autosync_push.log >&2
  exit 1
}

commit_sha="$(git rev-parse --short HEAD)"
echo "SYNCED $commit_sha $branch"
