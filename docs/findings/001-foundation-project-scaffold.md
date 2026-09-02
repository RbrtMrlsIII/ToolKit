# 001-foundation-project-scaffold

**Field:** Foundation  
**Phase:** foundation  
**Target:** project-scaffold  
**Impact:** BOUNDED  
**Status:** VALIDATED  
**Date:** 2026-09-01

## Goal
Create a practical `scripts/new-project.py` that turns this toolkit into an easy-to-use project starter.

## What the script should do
1. Accept a project name
2. Copy the clean toolkit structure
3. Initialize the 6 canonical files with the project name
4. Create empty `src/` with a short README
5. Initialize `.agent/continuity/` with starter registry + state
6. Create the first session log + checkpoint-000
7. Optionally include backend-integrations and test-files
8. Print clear next steps

## Success Criteria
- One command creates a ready-to-use project
- New project follows all canonical rules
- No manual cleanup needed after scaffolding
