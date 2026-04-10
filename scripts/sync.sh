#!/bin/bash
# swiftlang-wiki sync script
# Usage: .wiki/scripts/sync.sh [commit message]
# If no message provided, auto-generates from changed files.

set -euo pipefail

WIKI_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$WIKI_DIR"

# Check if inside git repo
if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "❌ .wiki/ is not a git repository. Run 'git init' first."
  exit 1
fi

# Check for changes
if git diff --quiet HEAD -- . 2>/dev/null && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "✅ Wiki is up to date — no changes to sync."
  exit 0
fi

# Count changes
PAGES_CHANGED=$(git diff --name-only HEAD -- pages/ 2>/dev/null | wc -l | tr -d ' ')
PAGES_NEW=$(git ls-files --others --exclude-standard -- pages/ | wc -l | tr -d ' ')
SOURCES_NEW=$(git ls-files --others --exclude-standard -- sources/ | wc -l | tr -d ' ')
TOTAL_PAGES=$(find pages -type f -name '*.md' 2>/dev/null | wc -l | tr -d ' ')

# Build commit message
if [ $# -gt 0 ]; then
  MSG="$*"
else
  PARTS=""
  [ "$PAGES_NEW" -gt 0 ] && PARTS="${PARTS}+${PAGES_NEW} pages, "
  [ "$PAGES_CHANGED" -gt 0 ] && PARTS="${PARTS}~${PAGES_CHANGED} updated, "
  [ "$SOURCES_NEW" -gt 0 ] && PARTS="${PARTS}+${SOURCES_NEW} sources, "
  PARTS="${PARTS%%, }"  # trim trailing comma
  MSG="Wiki sync: ${PARTS:-minor updates} (${TOTAL_PAGES} total pages)"
fi

# Stage, commit, push
git add -A
git commit -m "$MSG"

if git remote get-url origin >/dev/null 2>&1; then
  git push origin main
  echo "✅ Synced to GitHub: $(git remote get-url origin)"
else
  echo "✅ Committed locally (no remote configured)."
fi

echo "   Pages: $TOTAL_PAGES | Commit: $(git rev-parse --short HEAD)"
