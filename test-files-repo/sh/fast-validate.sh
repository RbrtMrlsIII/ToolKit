#!/bin/bash
# Fast validate: census + knowledge + minimalism + skills
set -e
echo "Fast validate for any project type"
./test-files-repo/sh/run-census.sh
python3 test-files-repo/py/test_knowledge_distill.py
python3 test-files-repo/py/test_minimalism.py
node test-files-repo/mjs/test-skills-loader.mjs
echo "FAST VALIDATE PASS"
