#!/bin/bash
# Fast census — universal inventory + cleanliness
set -e
BASE_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
# Try find census.py
CENSUS=""
for p in "$BASE_DIR/scripts/census.py" "$BASE_DIR/.agent/census/census.py" "$BASE_DIR/agent-repo-template/scripts/census.py" "$BASE_DIR/agent-complete/agent-repo-template/scripts/census.py"; do
  if [ -f "$p" ]; then CENSUS="$p"; break; fi
done
if [ -z "$CENSUS" ]; then echo "census.py not found"; exit 1; fi
python3 "$CENSUS" --base "$BASE_DIR" --write
echo "Census done — check docs/census/census-report-*.md"
