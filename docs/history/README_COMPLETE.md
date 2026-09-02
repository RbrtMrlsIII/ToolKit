# Complete Discussion Summary — Universal AGENT Repo

Date: 2026-08-31
This zip contains entire evolution from our discussion.

## Evolution

### Phase 1: Initial Request
User: Help to create well structured AGENT repo, for canonical structuring, continuity architecture, execution discipline (Observe → Record → Understand → Classify → Align → Validate → Endorse → Advance), (identify authority → identify consumers → classify impact → record contract/dependency impact → make smallest bounded change → validate source and consumers → update machine-readable state → update documentation → checkpoint/handover it applies to all fields from backend to frontend Human-readable findings, Machine-readable registry/state, Validation/test evidence, Team handover/checkpoint), proper usage of document files (AI_ASSISTANT_READ_ME.md, ENDORSEMENT.md, MASTERPLAN.md and wired by front-door README.md) and POLICY.md etc.

Solution: Created canonical structure with 5 main files, .agent/continuity, docs/findings, validation/evidence, quadruple evidence, XXX naming like 001-executionphase-target.

### Phase 2: Universal + PRODUCT-KNOWLEDGE.md
User: Make it applicable for all projects and future projects. Additional repository for documentation findings and how to convert findings in PRODUCT-KNOWLEDGE.md before deletion and support in AI_ASSISTANT_READ_ME.md, to ensure minimalistic approach while making knowledge increasing. Because AI are still making trial and errors that was already passed by previous agents.

Solution:
- Made MASTERPLAN generic for any stack (web, mobile, backend, 3d, game, generic)
- Added PRODUCT-KNOWLEDGE.md as permanent brain: Validated Patterns, Anti-Patterns & Dead Ends (most important), Gotchas, Quirks, Minimalism Log
- Transient findings (docs/findings/ max 10 files) -> Distill to PRODUCT-KNOWLEDGE.md -> Archive to docs/archive/ -> Compress to docs/knowledge-archive/ or delete (with endorsement)
- Updated AI_ASSISTANT_READ_ME.md: mandatory read order includes PRODUCT-KNOWLEDGE.md Anti-Patterns check before Observe, anti-repeat rule
- Updated POLICY.md with knowledge lifecycle: Distillation mandatory, deletion requires proof
- 5 evidences now: findings + registry/state + validation evidence + handover/checkpoint + knowledge distillation

### Phase 3: Census Script + Skills Repo
User: Yes please and also suggest skills (all possible skills using md files) and make it a repository too.

Solution:
- Created scripts/census.py — checks forbidden names, findings count, missing distillation, registry vs fs, PK size
- Created 16 skills as MD files: observe, record, understand, classify, align, validate, endorse, advance (8 core) + knowledge-distiller, anti-pattern-checker, minimalism-enforcer, checkpoint-creator + census-runner, reconciliation-manager, investigation-manager, contract-manager
- Each skill: Metadata, When To Use, Prerequisites, Steps, Validation Checklist, Anti-Patterns, Distillation
- Skills repo standalone: agent-skills-repo/
- Skills also copied to main repo: skills/ and .agent/skills/

### Phase 4: Final Universal Census as Project Tool (Current)
User: census is the project tool like how many tabs do we have how many UI before converting to 3D, make it applicable to all project type then produce one zip only containing all of these our entire discussions.

Solution (this version):
- Census now counts project inventory applicable to ALL project types:
  - tabs: how many tabs do we have (files + config entries)
  - ui_screens: how many UI screens/pages before converting to 3D
  - ui_components: reusable components
  - routes, backend_endpoints, models_3d (glb, gltf, obj, fbx, usd), textures_materials, data_models
  - conversion_tracking: tabs_total, ui_screens_total, total_ui_before_3d, models_3d_total, conversion_progress
- Configurable via .agent/census/census.config.json — edit file_patterns to match your stack (web, mobile, backend, 3d, game, generic)
- Still does cleanliness checks: forbidden, findings <=10, missing distillation, registry
- Generates 3 files: census-YYYY-MM-DD.json (full), census-report-YYYY-MM-DD.md (human), inventory-YYYY-MM-DD.json (inventory only)
- Example report shows: Tabs: X, UI Screens: Y, UI Components: Z, 3D Models: W, before converting to 3D

## Canonical Files (6) — Universal

1. README.md — front-door wiring only, <80 lines, links to other 5
2. AI_ASSISTANT_READ_ME.md — OS for AI, reading order, minimalism, anti-repeat, 5 evidences, inner loop with distill step
3. MASTERPLAN.md — generic conceptual map, XXX checklist, impact definitions, current focus
4. POLICY.md — constitution: structure, naming (XXX-phase-target), knowledge lifecycle (transient->distill->archive->compress/delete), 4 D's + knowledge, enforcement
5. PRODUCT-KNOWLEDGE.md — permanent brain: Validated Patterns, Anti-Patterns (critical), Gotchas, Quirks, Minimalism Log
6. ENDORSEMENT.md — approval ledger with knowledge distillation proof, deletion approval template

## Execution Discipline

Outer: Observe → Record → Understand → Classify → Align → Validate → Endorse → Advance (O-R-U-C-A-V-E-A)
Inner: identify authority → identify consumers → classify impact → record contract/dependency impact → smallest bounded change → validate source and consumers → distill to PRODUCT-KNOWLEDGE.md → update machine state + docs → checkpoint/handover + archive

Quadruple + Knowledge = 5 evidences: findings (transient), registry/state (machine), validation evidence, handover/checkpoint, knowledge distillation (permanent)

## Minimalism Principle

- docs/findings/ = transient working memory, max 10, lifetime 1 XXX
- PRODUCT-KNOWLEDGE.md = permanent, grows dense
- After endorsement: distill -> archive -> after 2 checkpoints compress to knowledge-archive or delete (with endorsement)
- Goal: active project = 6 files + <10 findings + code. Knowledge increases.

## Skills Catalog (16)

Core: observe, record, understand, classify, align, validate, endorse, advance
Knowledge: knowledge-distiller, anti-pattern-checker, minimalism-enforcer, checkpoint-creator
Governance: census-runner, reconciliation-manager, investigation-manager, contract-manager + extended: naming-enforcer, archiving-manager, etc.

Each skill is MD file: load by reading skills/<id>/SKILL.md before executing phase.

## Census as Project Tool

Now applicable to all project types: web (tabs, pages, components), mobile (screens, tabs), backend (endpoints, models), 3d (models, textures), game, generic.

Before converting to 3D: census tells you how many tabs, how many UI screens before conversion, how many 3D assets you have, conversion progress.

Config file: .agent/census/census.config.json — edit patterns per stack.

## How to Use on Mobile AI Apps

Paste this starter into any AI app:

Read AI_ASSISTANT_READ_ME.md, then POLICY.md, then PRODUCT-KNOWLEDGE.md Anti-Patterns, then .agent/census/census.config.json, then registry.json, state.json, latest checkpoint-XXX.md, then MASTERPLAN.md row current_xxx, then load skill skills/<phase>/SKILL.md for current phase. Check Anti-Patterns before Classify. Run census.py --write before checkpoint. Distill to PRODUCT-KNOWLEDGE.md before archiving.

## Contents of This Zip

- agent-repo-template/ — Final universal repo with census inventory tool, skills, PRODUCT-KNOWLEDGE.md, etc.
- agent-skills-repo/ — Standalone skills repo (16 skills as MD)
- census.config.json — Universal census config
- This README_COMPLETE.md — Entire discussion summary
