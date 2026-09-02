---
name: agent-orucavea
description: Apply the O-R-U-C-A-V-E-A execution discipline (Observe Record Understand Classify Align Validate Endorse Advance) and its 9-step inner loop for any structured agent work. Use when starting a new XXX task, continuing a project with continuity requirements, enforcing smallest-bounded-change, or when the user mentions ORUCAVEA, execution discipline, phase gates, or agent continuity protocol.
---

# Agent ORUCAVEA — Execution Discipline

Apply this 8-gate outer loop and 9-step inner loop on every significant piece of work in an agent-managed project.

## Outer 8-Gate Loop (O-R-U-C-A-V-E-A)

1. **Observe** — Read authorities, consumers, contracts, and PRODUCT-KNOWLEDGE Anti-Patterns. Never guess.
2. **Record** — Create a finding file `docs/findings/XXX-phase-target.md`.
3. **Understand** — Map contracts, dependencies, and impact surface.
4. **Classify** — LOCAL | BOUNDED | SYSTEMIC. Prefer LOCAL or BOUNDED.
5. **Align** — Make the smallest bounded change that satisfies the goal.
6. **Validate** — Produce evidence in `validation/evidence/XXX-...md`.
7. **Endorse** — Draft approval in ENDORSEMENT.md and update registry.
8. **Advance** — Distill knowledge → update machine state + docs → checkpoint/handover → archive finding.

## Inner 9-Step Loop (runs inside Align → Advance)

1. Identify authority (source of truth)
2. Identify consumers
3. Classify impact (LOCAL / BOUNDED / SYSTEMIC)
4. Record contract / dependency impact
5. Make the smallest bounded change
6. Validate source and all consumers
7. Distill learnings into PRODUCT-KNOWLEDGE.md
8. Update machine-readable state (registry.json, state.json) + documentation
9. Create checkpoint / handover + archive the finding

## Five Required Evidences

Every completed XXX must leave all five:

1. Human findings (`docs/findings/XXX-...md`) — transient
2. Machine state (`.agent/continuity/registry.json` + `state.json`)
3. Validation evidence (`validation/evidence/XXX-...md`)
4. Handover / checkpoint (`docs/handover/` + `.agent/continuity/checkpoint-XXX.md`)
5. Knowledge distillation (row in PRODUCT-KNOWLEDGE.md + Minimalism Log)

Missing the 5th evidence = incomplete even if tests pass.

## Naming Rules

- Use only `XXX-phase-target` form (e.g. `006-backend-auth-api`).
- Never create `patch1.md`, `final.md`, `fix.md`, `temp.md`, etc.
- One XXX at a time. Finish and advance before starting the next.

## Critical Rules

- Before Classify, always run anti-pattern check against PRODUCT-KNOWLEDGE.md.
- Prefer the smallest possible change that is still correct.
- After endorsement, distill → archive → only then delete (with proof).
- Session logging and file-update protocol are mandatory (see agent-continuity skill).

## When to Load Next Skills

After Observe → load anti-pattern-checker / agent-knowledge  
After Align → load agent-continuity (file-update protocol)  
Before Advance → load knowledge-distiller  
At session start → load agent-continuity (session-logger)
