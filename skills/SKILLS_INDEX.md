# SKILLS_INDEX — Universal AGENT Skills

## Scale & Adaptation
- **scale-adapter** — Adapt toolkit behaviour according to project size (S/M/L/XL)

## Upstream Definition
- **roots-definer** — First checks for an existing root, then defines (or validates) core problem, inputs/outputs, scope, architecture, data model, metrics, risks, and breakdown strategy *before* any phase planning

## Planning & Safety
- **phase-planner** — Propose execution phase → wait for approval → plant or branch on MASTERPLAN.md
- **backend-first-clarifier** — Clarify the backend authority model with the user after an idea is established and before implementation begins
- **safety-reporter** — Warn on destructive / high-impact / SYSTEMIC actions

## Core Execution (O-R-U-C-A-V-E-A)
observe → record → understand → classify → align → validate → endorse → advance

## Knowledge & Minimalism
anti-pattern-checker, knowledge-distiller, minimalism-enforcer, checkpoint-creator

## Governance
census-runner, reconciliation-manager, investigation-manager, contract-manager

## Continuity & Handover
session-logger, file-update-protocol, target-project-handover, canonical-build, dictionary-manager

## High-level Grok Skills (absorbed)
Located in `skills/_grok-high-level/`:
- agent-orucavea
- agent-knowledge
- agent-continuity
- agent-census
- agent-structure

These are the condensed, always-available versions used by Grok.

## Scope and fast-switching
See `docs/SKILL_SCOPE_INDEX.md` for the field + project-type classification of every skill currently indexed here. The index is the switching map; each skill's `SKILL.md` remains the behavioral authority.

## Recommended Load Order

1. `session-logger` (session start)
2. `scale-adapter` (when size/complexity is a concern)
3. `roots-definer` (when problem / architecture may be unclear or already exists)
4. `phase-planner` (once roots are approved)
5. `backend-first-clarifier` (before implementation)
6. `safety-reporter` (before high-impact actions)
7. `observe` + `anti-pattern-checker`
8. `record` → `understand` → `classify`
9. `align` (+ `file-update-protocol`)
10. `validate` → `census-runner`
11. `endorse` → `advance` → `knowledge-distiller` → `minimalism-enforcer`
12. `target-project-handover` + `checkpoint-creator`

## Knowledge direction

Toolkit is a reusable upstream knowledge system. Consuming-project findings flow here only after validation + generalization. Toolkit does not automatically overwrite or push project-specific decisions downstream.

Each skill lives at `skills/<id>/SKILL.md`.
