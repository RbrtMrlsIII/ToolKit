# Test Files Repo — Fast Testing for Universal Agent Repo

> **Purpose:** Centralized test files (py, mjs, js, ts, sh) to test agent repo faster. Use this repo to validate census, knowledge distillation, minimalism, skills, backend integrations.

**Main Use:** Speed up validation. Instead of writing tests from scratch, copy from here.

## Quick Start — Use This Repo Faster

### 1. Fast Census Test (All Project Types)
```bash
# From any project root that has scripts/census.py
python test-files-repo/py/test_census_fast.py --base . --write
# or
node test-files-repo/mjs/test-inventory.mjs --base .
```

### 2. Fast Knowledge Distillation Test
```bash
python test-files-repo/py/test_knowledge_distill.py
# Checks if finding was distilled to PRODUCT-KNOWLEDGE.md
```

### 3. Fast Minimalism Check
```bash
python test-files-repo/py/test_minimalism.py
# Fails if docs/findings/ >10 or forbidden files exist
```

### 4. Fast Skills Load Test
```bash
node test-files-repo/mjs/test-skills-loader.mjs
# Verifies all 16 skills exist and have required sections
```

## Structure

| Folder | Main Use | Files |
|--------|----------|-------|
| `py/` | Python tests — census, knowledge, minimalism, registry | test_census_fast.py, test_knowledge_distill.py, test_minimalism.py, test_registry.py |
| `mjs/` | Node/MJS tests — inventory, UI tabs count, 3D assets, skills loader | test-inventory.mjs, test-tabs-counter.mjs, test-3d-inventory.mjs, test-skills-loader.mjs |
| `js/` | JS helpers for backend/frontend quick tests | test-supabase.js, test-firebase.js |
| `ts/` | TS helpers | test-contract.ts, test-dependency-map.ts |
| `sh/` | Shell shortcuts | run-census.sh, run-all-tests.sh, fast-validate.sh |
| `templates/` | Templates for new tests | TEMPLATE-test-XXX.py, TEMPLATE-test-XXX.mjs |

## How to Use Faster (3 Commands)

**Fastest validation for any project:**
```bash
# 1. Census (tabs, UI, 3D inventory + cleanliness)
./test-files-repo/sh/run-census.sh

# 2. All tests
./test-files-repo/sh/run-all-tests.sh

# 3. Full validation (census + knowledge + minimalism)
./test-files-repo/sh/fast-validate.sh
```

## Linking

- Linked from front-door README.md: `../README.md`
- Linked from main repo: `../agent-repo-template/README.md`
- Linked from backend repo: `../backend-integrations-repo/README.md`

## For Mobile AI

When you need to test quickly, don't write new test. Copy from this repo:

- Need to test census? Copy `py/test_census_fast.py`
- Need to count tabs? Copy `mjs/test-tabs-counter.mjs`
- Need to test 3D inventory? Copy `mjs/test-3d-inventory.mjs`

All tests follow XXX naming: `001-test-census-fast`, but stored here as reusable library.

Date: 2026-08-31
