# POLICY.md — Universal Project Constitution

> The hard rules that every AI agent and human must obey.  
> Applicable to all project types (web, mobile, backend, 3D, game, generic).

---

## 1. Source-of-Truth (Product Law)

**This is the highest law of the project.**

The Source-of-Truth is the single, authoritative foundation that all other canonical files, decisions, code, and knowledge must ultimately serve and never contradict.

### What counts as Source-of-Truth
- Product vision and non-negotiable product constraints (usually expressed in MASTERPLAN + contracts)
- Approved contracts (`docs/contracts/`)
- Validated Patterns and Anti-Patterns in `PRODUCT-KNOWLEDGE.md` (once endorsed)
- The 6 Canonical Files themselves (once endorsed)

### Rules
- No code, finding, or decision may permanently violate the Source-of-Truth.
- When conflict arises, Source-of-Truth wins. Create an investigation, do not silently override.
- Changing the Source-of-Truth itself requires explicit endorsement and a new XXX.

The Source-of-Truth is the foundation upon which every canonical file rests.

---

## 2. Layer Separation (Critical)

The project has two strictly separated layers:

### A. Governance / Canonical Layer (this toolkit)
Contains only:
- The 6 Canonical Files at root
- `.agent/` (machine state)
- `docs/` (findings, knowledge, handover, contracts, census, etc.)
- `skills/`, `scripts/`, `prompts/`, `validation/`, `builds/`

**Purpose:** Continuity, discipline, knowledge, approval, inventory.

### B. Project-Development Layer (the actual product)
Contains only:
- `src/` (or equivalent: `app/`, `lib/`, `packages/`, etc.)
- Product-specific configuration that is **not** governance
- Tests that belong to the product code

**Purpose:** The real software being built.

### Hard Rules
- **Never** put product business logic, UI components, or domain code into the Governance layer.
- **Never** put findings, knowledge, session logs, or canonical rules into `src/`.
- `builds/` is the only allowed place for build outputs (never inside `src/` or `docs/`).
- New top-level folders require endorsement.

This separation keeps the agent operating system clean and the product code free of governance noise.

---

## 3. Canonical Structure — Only These at Root

```
/README.md                  ← Front-door (wiring + status only)
/AI_ASSISTANT_READ_ME.md    ← Agent Operating System
/MASTERPLAN.md              ← Conceptual map + XXX checklist
/POLICY.md                  ← This constitution
/PRODUCT-KNOWLEDGE.md       ← Permanent distilled brain
/ENDORSEMENT.md             ← Approval ledger

/.agent/                    ← Machine-readable state
/docs/                      ← Human-readable working + permanent knowledge
/skills/                    ← Loadable skills
/scripts/                   ← Census, knowledge tools, etc.
/prompts/                   ← Mobile paste prompts
/validation/                ← Evidence
/builds/                    ← Only place for build outputs
/src/                       ← Project-Development Layer (code only)
```

No other root files or folders without endorsement.

---

## 4. File Naming — Anti-Chaos

**FORBIDDEN names:**  
`patch*`, `final*`, `fix*`, `temp*`, `backup*`, `old*`, `new*`, `v1*`, `copy*`, `test2*`, `dd*`

**REQUIRED form for findings / handover / evidence:**  
`XXX-phase-target.md`  
Examples: `006-backend-auth-api.md`, `000-scaffold-toolkit.md`

XXX is the 3-digit number from MASTERPLAN. One XXX at a time.

---

## 5. Role of the Six Canonical Files

| File | MUST contain | MUST NOT contain |
|------|--------------|------------------|
| README.md | Title, purpose (1–2 lines), links to the other 5, current status. < 80 lines | Findings, logs, code, TODOs, knowledge |
| AI_ASSISTANT_READ_ME.md | Reading order, O-R-U-C-A-V-E-A, 5 evidences, minimalism, mobile constraints | Business logic, product details |
| MASTERPLAN.md | Vision, authority→consumer map, impact definitions, current XXX focus, checklist | Execution logs, raw findings |
| POLICY.md | Structure, naming, knowledge lifecycle, file-update protocol, enforcement | Current status or temporary notes |
| PRODUCT-KNOWLEDGE.md | Dense tables only: Validated Patterns, Anti-Patterns, Gotchas, Quirks, Minimalism Log | Unvalidated guesses, raw logs |
| ENDORSEMENT.md | Human-approved XXX entries + knowledge-distillation proof | Self-approved drafts |

---

## 6. Knowledge Minimalism Lifecycle

**Goal:** Active project = 6 canonical files + ≤ 10 findings + code.  
Knowledge increases. Files stay minimal.

1. **Transient** — `docs/findings/XXX-….md` (max 10, lifetime = one XXX)
2. **Distill** (mandatory at Advance) — Add row(s) to PRODUCT-KNOWLEDGE.md + Minimalism Log entry
3. **Archive** — Move finding to `docs/archive/` with distillation proof header
4. **Compress / Delete** — After 2 checkpoints + endorsement + Minimalism Log proof, may compress to `docs/knowledge-archive/` or delete

Anti-Patterns section of PRODUCT-KNOWLEDGE.md is the most important. Skipping the anti-pattern check before Classify is a hard violation.

---

## 7. File Update Protocol (Mandatory)

When you change **any** file you MUST update the full chain in the same session, with timestamps:

1. Source file (timestamp comment when practical)
2. Session log (`.agent/sessions/` + `docs/sessions/`) — must be started at the beginning of the session
3. `registry.json` + `state.json`
4. Checkpoint + handover
5. PRODUCT-KNOWLEDGE.md (if a pattern was learned)
6. Dictionary (if new entity)
7. Builds (if buildable)
8. Census (`python scripts/census.py --base . --write`)
9. Architecture map (if structure changed)
10. Finalize session log (end timestamp + complete_trace)

Session logs that only appear at the end of a session are invalid → census FAIL.

---

## 8. Builds

Only allowed locations:
- `builds/XXX-phase-target/` (and `builds/latest/`)
- `.agent/builds/` (machine state)

Never put builds inside `src/` or `docs/`.

---

## 9. Dictionary

When the project grows (many tabs, screens, 3D models, endpoints, terms):
- Maintain `.agent/dictionary/dictionary.json`
- Auto-generate `docs/dictionary/DICTIONARY.md`
- Update in the same session as the change (File Update Protocol)

---

## 10. Enforcement (Census)

Census FAIL conditions include:
- Forbidden filenames
- Active findings > 10
- Missing distillation
- Incomplete session log
- File changed without updating registry / state / checkpoint
- Repeating a recorded Anti-Pattern without investigation
- Builds placed in forbidden locations
- Dictionary missing when entity count is high

---

## 11. Hierarchy of Authority

1. **Source-of-Truth** (Product Law)
2. **POLICY.md** (this constitution)
3. **Endorsed PRODUCT-KNOWLEDGE.md** (especially Anti-Patterns)
4. **MASTERPLAN.md** + approved contracts
5. Current checkpoint + registry
6. Everything else

When in doubt, stop and create an investigation file rather than guessing.
