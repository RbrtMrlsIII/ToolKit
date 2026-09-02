# AI_ASSISTANT_READ_ME.md — Universal Operating System for AI Agents

> **MANDATORY READ FOR EVERY AI INSTANCE.**  
> You are a CONTINUATION agent, not a new agent. Trust files, not memory.  
> Applies to all projects.

---

## 0. Highest Authority

1. **Source-of-Truth** (Product Law) — see POLICY.md §1
2. POLICY.md (this constitution)
3. PRODUCT-KNOWLEDGE.md (especially Anti-Patterns)
4. MASTERPLAN.md + endorsed contracts
5. Current checkpoint + registry
6. Everything else

Never permanently contradict the Source-of-Truth.

---

## 1. Layer Separation (Critical)

| Layer | Location | What belongs here | What does NOT belong here |
|-------|----------|-------------------|---------------------------|
| **Governance / Canonical** | Root 6 files + `.agent/` + `docs/` + `skills/` + `scripts/` | Continuity, knowledge, rules, findings, skills | Product business logic, UI components, domain code |
| **Project-Development** | `src/` (or `app/`, `lib/`, `packages/`) | **Product code only** | Findings, knowledge, session logs, canonical rules, builds |

`src/` is the product code structure. Nothing else.

---

## 2. Continuity Reading Order (Non-Negotiable)

Before **any** action, read in this exact order:

1. `POLICY.md` — Constitution + Source-of-Truth + Layer Separation
2. `PRODUCT-KNOWLEDGE.md` — **Anti-Patterns section first** (prevents repeat dead ends)
3. `.agent/continuity/registry.json` — Machine truth
4. `.agent/continuity/state.json` — Last good state
5. Latest `checkpoint-XXX.md`
6. `MASTERPLAN.md` — Your assigned XXX row
7. `ENDORSEMENT.md` — What is already approved
8. Relevant contracts in `docs/contracts/` and existing structure in `src/`

Skipping PRODUCT-KNOWLEDGE Anti-Patterns = hard violation.

---

## 3. Before Any Change (Editing, Debugging, Adding, Deduping, Fixing Discrepancies)

You MUST:

1. Complete the reading order above
2. Observe existing authorities, consumers, and **current canonical structures**
3. Run anti-pattern check against PRODUCT-KNOWLEDGE.md
4. Only then Classify impact (LOCAL | BOUNDED | SYSTEMIC)
5. Make the **smallest bounded change**

Never start coding or restructuring until the above is done.

---

## 4. Execution Discipline — O-R-U-C-A-V-E-A

**Outer 8-Gate Loop**  
Observe → Record → Understand → Classify → Align → Validate → Endorse → Advance

**Inner 9-Step Loop** (inside Align → Advance)  
1. Identify authority  
2. Identify consumers  
3. Classify impact  
4. Record contract / dependency impact  
5. Make smallest bounded change  
6. Validate source + all consumers  
7. Distill to PRODUCT-KNOWLEDGE.md  
8. Update machine state + docs  
9. Checkpoint / handover + archive

---

## 5. Five Required Evidences

Every completed XXX must leave all five:

1. Human findings → `docs/findings/XXX-….md` (transient)
2. Machine state → `registry.json` + `state.json`
3. Validation evidence → `validation/evidence/XXX-….md`
4. Handover / checkpoint → `docs/handover/` + `.agent/continuity/checkpoint-XXX.md`
5. Knowledge distillation → row in PRODUCT-KNOWLEDGE.md + Minimalism Log

Missing the 5th = incomplete even if tests pass.

---

## 6. Minimalism Principle

- `docs/findings/` = transient (max 10 files)
- `PRODUCT-KNOWLEDGE.md` = permanent dense brain
- After endorsement → distill → archive → later compress/delete only with proof
- Goal: Active project = 6 canonical files + ≤ 10 findings + code in `src/`

---

## 7. File Update Protocol + Session Logging

**Session log must be created at the START of every session**, not at the end.

When you change **any** file, update the full chain with timestamps (see POLICY.md §7):

Source → Session log → registry + state → checkpoint + handover → PRODUCT-KNOWLEDGE (if pattern) → dictionary (if entity) → builds (if buildable) → census → architecture map → finalize session log

Incomplete session log or missing updates = census FAIL.

---

## 8. Canonical Build Locations

Only allowed places for builds:

- `builds/XXX-phase-target/` and `builds/latest/`
- `.agent/builds/`

**Never** put builds inside `src/` or `docs/`.  
Use skill: `skills/canonical-build/SKILL.md`

---

## 9. Machine + Human Readable Pairs

| Machine (always tracked) | Human (generated / readable) |
|--------------------------|------------------------------|
| `.agent/continuity/registry.json` | `MASTERPLAN.md`, checkpoints |
| `.agent/continuity/state.json` | `docs/handover/` |
| `.agent/sessions/*.json` | `docs/sessions/*.md` |
| `.agent/dictionary/dictionary.json` | `docs/dictionary/DICTIONARY.md` |
| `.agent/builds/builds.json` | `builds/` + build logs |
| `docs/census/*.json` | `docs/census/*-report.md` + dashboard |

Always keep both sides in sync.

---

## 10. Hard Constraints (Mobile & Continuity)

- Trust files, never memory
- Never create `patch1.md`, `final.md`, `fix.md`, `temp.md` — only `XXX-phase-target`
- Never edit README.md beyond wiring
- Never add unvalidated guesses to PRODUCT-KNOWLEDGE.md
- When uncertain → create investigation file and stop
- Before deleting any finding → prove distillation (Minimalism Log + archive + endorsement)

---

## 11. Quick Load Skills

| Moment | Load this skill |
|--------|-----------------|
| Session start | `session-logger` |
| Before Classify | `anti-pattern-checker` |
| Every file change | `file-update-protocol` |
| Before / during build | `canonical-build` |
| At Advance | `knowledge-distiller` + `minimalism-enforcer` + `checkpoint-creator` |

Full index: `skills/SKILLS_INDEX.md`
