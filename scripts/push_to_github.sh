#!/bin/bash
set -euo pipefail

REPO="pratham-vishk/pega-interview-romance-guide"

if [ -z "${GH_TOKEN:-}" ]; then
  echo "Error: GH_TOKEN is not set. Add a GitHub Personal Access Token with repo scope."
  exit 1
fi

export GH_TOKEN
cd /agent

# Create repo if it doesn't exist
if ! gh repo view "$REPO" &>/dev/null; then
  echo "Creating repository $REPO..."
  gh repo create "$REPO" --public --description "Complete Pega interview prep PDF - 32 chapters, 23 diagrams, Top 50 Q&A"
fi

# Set remote and push
if ! git remote get-url origin &>/dev/null; then
  git remote add origin "https://github.com/${REPO}.git"
fi

git push -u origin main
echo ""
echo "✅ Published: https://github.com/${REPO}"
echo "📥 PDF: https://github.com/${REPO}/blob/main/pega-interview-prep/Pega_Interview_Romance_Guide.pdf"
echo "⬇️  Raw download: https://github.com/${REPO}/raw/main/pega-interview-prep/Pega_Interview_Romance_Guide.pdf"
