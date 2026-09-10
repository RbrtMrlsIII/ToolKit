# SKILLS_INDEX — Universal AGENT Skills

Skills are reusable operational instructions. They do not define product authority and never grant authorization. The catalog is expected to grow as validated execution baselines freeze.

## Scale & Adaptation
- **scale-adapter** — Adapt Toolkit behaviour according to project size (S/M/L/XL)

## Upstream Definition
- **roots-definer** — Establish/validate core problem, inputs/outputs, scope, architecture, data model, metrics, risks, and breakdown strategy before phase planning

## Planning & Safety
- **phase-planner** — Propose execution phase, wait for approval, then plant/branch on MASTERPLAN.md
- **backend-first-clarifier** — Clarify backend authority model with the user before implementation
- **safety-reporter** — Warn on destructive / high-impact / SYSTEMIC actions

## Core Execution (O-R-U-C-A-V-E-A)
`observe → record → understand → classify → align → validate → endorse → advance`

## Knowledge & Minimalism
- **anti-pattern-checker** — prevent known failure repetition
- **knowledge-distiller** — generalize validated lessons upstream
- **minimalism-enforcer** — keep durable knowledge compact and purposeful
- **checkpoint-creator** — preserve a durable stopping point

## Governance & Integrity
- **census-runner** — inventory and cleanliness enforcement
- **reconciliation-manager** — resolve state/registry/document drift
- **investigation-manager** — contain uncertainty and discrepancies
- **contract-manager** — maintain authority and dependency contracts
- **canonical-integrity** — fail closed on unexplained canonical section loss or deletion-heavy structural drift

## Continuity & Handover
- **session-logger** — start/close durable session evidence
- **file-update-protocol** — keep related governed artifacts synchronized
- **target-project-handover** — preserve consumer-project boundary and handover completeness
- **canonical-build** — construct canonical deliverables in allowed build locations
- **dictionary-manager** — maintain machine/human entity dictionary

## High-level Grok Skills (absorbed)
Located in `skills/_grok-high-level/`:
- agent-orucavea
- agent-knowledge
- agent-continuity
- agent-census
- agent-structure

These are condensed high-level versions used by Grok.

## Scope and fast-switching

See `docs/SKILL_SCOPE_INDEX.md` for scope, field, project-type, phase, dependency, provider/runtime, and task classification.

## Recommended Load Order

1. `session-logger` (session start)
2. `scale-adapter` (when size/complexity matters)
3. `roots-definer` (when problem/root architecture may be unclear)
4. `phase-planner` (once roots and material direction are approved)
5. `backend-first-clarifier` (before backend implementation when applicable)
6. `safety-reporter` (before high-impact actions)
7. `observe` + `anti-pattern-checker`
8. `record` → `understand` → `classify`
9. `align` + `file-update-protocol`
10. `canonical-integrity` for governed/canonical document changes
11. `validate` → `census-runner`
12. `endorse` → `advance` → `knowledge-distiller` → `minimalism-enforcer`
13. `target-project-handover` + `checkpoint-creator`

## Baseline-driven catalog growth

Every validated execution baseline should trigger a skill-coverage review. Create or refine a skill only when a repeatable procedure is sufficiently understood and has a verification path.

A healthy growth sequence is:

`baseline freeze → skill coverage review → scope classification → skill/extension candidate → validation → endorsement → index update`.

Skill growth changes execution precision, not authority.

## Upstream learning boundary

Consuming-project findings flow here only after validation + generalization. Product-specific law, provider choices, credentials, domain rules, and implementation details remain downstream. Toolkit does not automatically overwrite consumer projects.
