#!/usr/bin/env bash
# Sync this fork with upstream fg-zettelkasten — the ONLY supported way to
# bring in code changes (see CLAUDE.md fork policy).
#
# Content protection: upstream main contains fg's own vault/ and data/, so a
# naive merge would import fg's notes into the team kasten. Two defenses:
#   1. .gitattributes marks vault/** and data/** merge=ours (needs the local
#      driver below).
#   2. This script force-restores both paths after the merge regardless.
#
# One-time local setup:
#   git remote add upstream https://github.com/fabiogiglietto/fg-zettelkasten.git
#   git config merge.ours.driver true
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

if ! git remote get-url upstream >/dev/null 2>&1; then
  echo "Adding upstream remote..."
  git remote add upstream https://github.com/fabiogiglietto/fg-zettelkasten.git
fi
git config merge.ours.driver true

if [ -n "$(git status --porcelain)" ]; then
  echo "Working tree not clean — commit or stash first." >&2
  exit 1
fi

git fetch upstream
tag="pre-sync-$(date -u +%Y%m%dT%H%M%SZ)"
git tag "$tag"
echo "Rollback point: git reset --hard $tag"

git merge upstream/main --no-edit || {
  echo "Merge stopped with conflicts. Resolve rule of thumb:"
  echo "  take upstream: src/ tests/ schema/ scripts/ quartz/ .github/ requirements*"
  echo "  keep ours:     config.yml vault/ data/ README.md CLAUDE.md CONTRIBUTING.md .gitattributes"
  echo "Then: git checkout HEAD -- vault data && git commit"
  exit 1
}

# Belt and braces: content/state must never move on a sync.
git checkout HEAD -- vault data 2>/dev/null || true
if ! git diff --quiet HEAD -- vault data; then
  git commit -am "Restore vault/data after upstream sync"
fi

echo "Synced. Review 'git log --oneline -5', run pytest, then push."
