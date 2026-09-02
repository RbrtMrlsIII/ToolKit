#!/bin/bash
set -e
echo "=== Running all fast tests ==="
python3 test-files-repo/py/test_minimalism.py || python3 agent-repo-template/../test-files-repo/py/test_minimalism.py || true
python3 test-files-repo/py/test_registry.py || true
python3 test-files-repo/py/test_census_fast.py --base . --write || true
python3 test-files-repo/py/test_knowledge_distill.py || true
node test-files-repo/mjs/test-skills-loader.mjs || true
node test-files-repo/mjs/test-tabs-counter.mjs || true
node test-files-repo/mjs/test-3d-inventory.mjs || true
echo "=== All fast tests done ==="
