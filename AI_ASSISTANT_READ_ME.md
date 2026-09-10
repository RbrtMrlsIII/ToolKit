# AI_ASSISTANT_READ_ME.md — Universal Operating System for AI Agents

> **MANDATORY READ FOR EVERY AI INSTANCE.** You are a CONTINUATION agent, not a new agent. Trust files, not memory. Applies to all projects.

---

## 0. Highest Authority and User-First Chain

1. **User / project owner intent**
2. **`PRODUCT_LAW.md`** — canonical reconstruction of approved product meaning
3. **`POLICY.md`** — governance constitution
4. **`PRODUCT-KNOWLEDGE.md`** — endorsed permanent knowledge, Anti-Patterns first
5. **`MASTERPLAN.md` + endorsed contracts** — ordered execution slices
6. Current checkpoint + registry/state
7. Everything else

Universal execution chain:

```text
user command
→ consult Agents
→ user approval
→ reconstruct PRODUCT_LAW.md
→ MASTERPLAN.md checklist / slice
→ skills + PRODUCT-KNOWLEDGE
→ O-R-U-C-A-V-E-A
→ action / implementation
→ validation
→ evidence
→ complete log / handover
→ endorsement
→ PRODUCT-KNOWLEDGE growth
```

An Agent may propose before approval. It may not promote its proposal to product truth silently.

## 1. Layer Separation

| Layer | Location | What belongs here | What does NOT belong here |
|---|---|---|---|
| Governance / Canonical | root canonical files + `.agent/` + `docs/` + `skills/` + `scripts/` | authority, continuity, knowledge, rules, skills, evidence | product business logic, UI components, domain code |
| Project-Development | `src/` or project equivalent | product code and product tests | findings, knowledge, session logs, canonical rules |

## 2. Continuity Reading Order

Before any action, read:

1. `PRODUCT_LAW.md`
2. `POLICY.md`
3. `PRODUCT-KNOWLEDGE.md` — Anti-Patterns first
4. `.agent/continuity/registry.json` and `state.json`
5. latest checkpoint / handover
6. `MASTERPLAN.md` current XXX
7. `ENDORSEMENT.md`
8. relevant contracts, structure, and product source

Skipping Anti-Patterns is a hard violation.

## 3. Before Any Change

You MUST:

1. observe current authority and canonical structure;
2. check known anti-patterns;
3. identify the current slice and responsibility;
4. declare a change contract for meaningful changes;
5. preserve unrelated canonical structure;
6. load the smallest sufficient skill bundle;
7. only then act.

## 4. Execution Discipline — O-R-U-C-A-V-E-A

Observe → Record → Understand → Classify → Align → Validate → Endorse → Advance.

Inside Align → Advance:

1. identify authority;
2. identify consumers;
3. classify impact;
4. record dependency/contract impact;
5. make the smallest bounded change;
6. validate source + consumers + structure;
7. distill reusable knowledge;
8. update machine state + docs;
9. checkpoint / handover / archive as required.

## 5. Five Evidences

Every completed XXX must leave:

1. human finding;
2. machine state;
3. validation evidence;
4. checkpoint + handover;
5. knowledge distillation.

## 6. Baseline Freezes and Skill Growth

A validated frozen baseline triggers skill coverage review.

```text
baseline freeze
→ identify repeatable procedure
→ reuse existing skill OR create/refine skill
→ define scope + dependencies + verification
→ endorse
→ future slices consume smallest sufficient bundle
```

Skills are living infrastructure. More frozen baselines may create more skills, but never more authority.

## 7. Canonical Structure Preservation

Canonical documents are protected knowledge structures.

- Keep all unrelated canonical sections.
- Do not treat a narrow request as permission to rewrite the whole document.
- Detect removed headings, large deletion blocks, and unrelated structural drift.
- Fail closed on unexplained canonical loss.

Use `skills/governance/canonical-integrity/SKILL.md` and `scripts/canonical-integrity.py`.

## 8. Instruction vs Authorization

```text
Skill              → HOW
Policy / workspace → WHETHER
Permission          → WHETHER THE Agent MAY ACT
PRODUCT_LAW         → WHAT IS TRUE
MASTERPLAN          → WHAT APPROVED SLICE IS NEXT
Evidence            → WHAT WAS PROVEN
```

Skills never grant authorization.

## 9. Knowledge State Classes

Use explicit state distinctions:

`CURRENT | DERIVED | HISTORICAL | CANDIDATE | ENDORSED`

Historical material is preserved, not silently cleaned up. Candidate knowledge is not authoritative until validated and endorsed.

## 10. Upstream / Downstream Boundary

```text
consumer finding
→ evidence + validation
→ generalization
→ Toolkit candidate
→ endorsement
→ universal knowledge / skill
```

Consumer-specific law, architecture, provider choices, credentials, and domain details stay downstream. Toolkit changes never silently overwrite an existing project.

## 11. Human Deployment

Human-only deployment guidance lives in the single canonical file:
`docs/USER_MANUAL_DEPLOYMENT.md`.

Agents may prepare and verify. They must not invent secrets, URLs, account authority, billing settings, or production state.

## 12. Hard Constraints

- Trust files, not memory.
- Never create forbidden patch/final/fix/temp/backup/old/new/v1/copy/test2/dd names.
- Never put product details or raw findings into README.
- Never add unvalidated guesses to PRODUCT-KNOWLEDGE.
- Never silently delete historical evidence.
- Never bypass Product Law, policy, permissions, or required approval.
- When uncertain, stop and create an investigation.

## 13. Quick Load Skills

| Moment | Load |
|---|---|
| Session start | `session-logger` |
| Before Classify | `anti-pattern-checker` |
| Canonical change | `file-update-protocol` + `canonical-integrity` |
| Before build | `canonical-build` |
| At Advance | `knowledge-distiller` + `minimalism-enforcer` + `checkpoint-creator` |
| Handover | `target-project-handover` |

Full index: `skills/SKILLS_INDEX.md`.
