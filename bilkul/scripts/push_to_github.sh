#!/bin/bash
set -euo pipefail

# Push Bilkul as standalone repo to pratham-vishk/bilkul
# Create the repo first: https://github.com/new → name: bilkul

REPO="pratham-vishk/bilkul"
DIR="$(cd "$(dirname "$0")/.." && pwd)/bilkul"

if [ ! -d "$DIR" ]; then
  echo "Error: bilkul/ not found at $DIR"
  exit 1
fi

cd "$DIR"

if [ ! -d .git ]; then
  git init
  git branch -M main
fi

git add -A
git diff --cached --quiet || git commit -m "Update Bilkul Interview OS"

if ! git remote get-url origin &>/dev/null; then
  git remote add origin "https://github.com/${REPO}.git"
fi

if gh repo view "$REPO" &>/dev/null; then
  git push -u origin main
  echo ""
  echo "✅ Published: https://github.com/${REPO}"
  echo "📥 HTML: https://github.com/${REPO}/blob/main/google-swe-interview-os.html"
  echo "📄 PDF:  https://github.com/${REPO}/raw/main/Google_SWE_Interview_OS.pdf"
else
  echo "Create repo first:"
  echo "  gh repo create $REPO --public --description 'Google SWE 90-Day Interview OS'"
  echo "Then re-run: ./scripts/push_bilkul.sh"
fi
