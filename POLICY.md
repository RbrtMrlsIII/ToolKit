# POLICY.md — Universal Project Constitution

> The hard rules that every AI agent and human must obey. Applicable to all project types (web, mobile, backend, 3D, game, generic).

---

## 0. Human User Authority

The **user / project owner is the highest product authority**.

The Toolkit must interpret and preserve the user's approved vision rather than replacing it with the newest Agent output, code state, provider default, historical wording, or implementation preference.

Material direction follows this chain:

```text
user command / vision
→ consult Agents
→ user approval
→ PRODUCT_LAW.md reconstruction
→ MASTERPLAN.md slice / checklist
→ skills + knowledge
→ O-R-U-C-A-V-E-A
→ action
→ validation
→ evidence
→ complete log / handover
→ endorsement
→ PRODUCT-KNOWLEDGE.md growth
```

Agents may analyze and propose before approval. They may not silently convert their proposal into product authority.

## 1. Product Law / Source-of-Truth

`PRODUCT_LAW.md` is the canonical reconstruction of the user's approved product meaning, purpose, invariants, boundaries, and non-negotiable outcomes for the current Toolkit project.

Product Law is the highest **project artifact authority**. It sits below the user's direct authority and above POLICY, MASTERPLAN, skills, tools, implementation, and historical material.

Rules:

- No code, finding, skill, tool, provider, or decision may permanently violate Product Law.
- When conflict arises, stop and investigate. Do not silently override Product Law.
- Changing Product Law requires explicit user approval and a recorded change scope.
- POLICY governs safe execution; it must not redefine product meaning.
- MASTERPLAN translates approved Product Law into ordered slices/checklists; it must not silently change product intent.

## 2. Layer Separation (Critical)

The project has two strictly separated layers.

### A. Governance / Canonical Layer
Contains:
- root canonical files;
- `.agent/` machine state;
- `docs/` findings, knowledge, contracts, history, handover, validation;
- `skills/`, `scripts/`, `prompts/`, `validation/`, `builds/`.

Purpose: continuity, authority, knowledge, discipline, inventory, evidence, reusable execution.

### B. Project-Development Layer
Contains product code in `src/` or the consuming project's equivalent (`app/`, `lib/`, `packages/`, etc.) plus product-specific configuration and tests that belong to the product.

Hard rules:

- Never put product business logic, UI components, or domain code into the governance layer.
- Never put findings, knowledge, session logs, or canonical rules into product code.
- Builds belong only in allowed build locations.
- New top-level folders require explicit endorsement.

## 3. Canonical Root Structure

The Toolkit core has these seven canonical root files:

```text
/README.md                  ← Front door, wiring + status only
/PRODUCT_LAW.md             ← User-approved product meaning + invariants
/AI_ASSISTANT_READ_ME.md    ← Agent Operating System
/MASTERPLAN.md              ← Conceptual map + XXX checklist
/POLICY.md                  ← Governance constitution
/PRODUCT-KNOWLEDGE.md       ← Permanent distilled brain
/ENDORSEMENT.md             ← Approval ledger
```

Supporting canonical structure:

```text
/.agent/                     ← machine state
/docs/                       ← human-readable working/permanent knowledge
/skills/                     ← loadable procedures
/scripts/                    ← executable governance helpers
/prompts/                    ← mobile-ready prompts
/validation/                 ← validation evidence
/builds/                     ← build outputs only
```

No other root files or folders without endorsement.

## 4. File Naming — Anti-Chaos

**Forbidden names:** `patch*`, `final*`, `fix*`, `temp*`, `backup*`, `old*`, `new*`, `v1*`, `copy*`, `test2*`, `dd*`.

Findings / handover / evidence use `XXX-phase-target.md`.

XXX is the 3-digit execution identifier from MASTERPLAN. One XXX is active at a time.

## 5. Role of the Canonical Files

| File | MUST contain | MUST NOT contain |
|---|---|---|
| `README.md` | Front-door purpose, navigation, status | Findings, logs, code, raw knowledge, patch notes |
| `PRODUCT_LAW.md` | User-approved product meaning, invariants, authority boundaries | Raw execution logs, unapproved implementation detail |
| `AI_ASSISTANT_READ_ME.md` | Reading order, execution gates, evidence and continuity rules | Product implementation detail |
| `MASTERPLAN.md` | Vision map, fields, current XXX, checklist, ordered slices | Raw findings, session logs |
| `POLICY.md` | Rules, authority, structure, change protocol, enforcement | Temporary project status |
| `PRODUCT-KNOWLEDGE.md` | Dense validated patterns, anti-patterns, conceptual relationships, minimalism history | Unvalidated guesses, raw logs |
| `ENDORSEMENT.md` | Human/authorized approval ledger | Self-approved drafts |

## 6. Knowledge Lifecycle and Growth

Toolkit knowledge grows while active documents remain controlled and compact.

```text
EPHEMERAL finding
   → validated evidence
   → generalized lesson
   → CANDIDATE
   → endorsement
   → ENDORSED knowledge
   → skill / governance evolution
```

Scope classes are:

`UNIVERSAL | ADAPTABLE | CONSUMER-SPECIFIC | EPHEMERAL | HISTORICAL | CANDIDATE | ENDORSED`.

Only validated and generalized consumer lessons may become Toolkit knowledge. Product-specific rules remain downstream.

`PRODUCT-KNOWLEDGE.md` must grow in conceptual depth: it records how fields, responsibilities, skills, artifacts, providers/runtime constraints, verification, and consumer patterns connect. It must not become a dump of raw logs.

Never delete a knowledge row. Supersede by reference when necessary. Compress/archive only with explicit proof.

## 7. Baseline Freezes Drive Skill Growth

A validated execution baseline or frozen slice triggers a skill-coverage review.

```text
baseline freezes
   ↓
repeatable procedure
   ↓
skill coverage review
   ↓
reuse existing skill OR create/refine skill
   ↓
scope + dependencies + verification recorded
   ↓
future slices use smallest sufficient bundle
```

Skills are living infrastructure. They may be added, split, refined, deprecated, or retired as validated execution pressure grows.

A new skill does not create new authority. Skill count may grow; authority remains stable.

## 8. Canonical Change Contract

Every meaningful change declares:

1. user objective;
2. authority / Product Law scope;
3. current Masterplan XXX;
4. affected canonical artifacts;
5. affected skills and knowledge;
6. protected unrelated structure;
7. verification plan;
8. evidence target;
9. endorsement requirement.

See `docs/CHANGE_CONTRACT.md`.

## 9. Canonical Structure Preservation

Canonical documents are knowledge structures, not disposable prose.

When changing a canonical document:

1. preserve all unrelated canonical content;
2. change only the authorized semantic scope;
3. detect unexpected deletions;
4. detect unexpected section loss;
5. verify structure before merge/release;
6. fail closed on unexplained canonical deletion.

The existence of a new expected claim does not prove document integrity.

The reusable guard is `skills/governance/canonical-integrity/SKILL.md` with `scripts/canonical-integrity.py`.

## 10. Instruction vs Authorization

```text
Skill                 → HOW
Policy / workspace    → WHETHER
Permission             → WHETHER THE Agent MAY ACT
PRODUCT_LAW            → WHAT IS TRUE
MASTERPLAN             → WHAT APPROVED SLICE IS NEXT
Evidence               → WHAT WAS PROVEN
```

A skill never grants authorization for repository mutation, deployment, billing, production access, credentials, or other privileged operations.

## 11. Five Evidences and Completion

Every completed XXX must leave:

1. human finding;
2. machine state;
3. validation evidence;
4. checkpoint + handover;
5. knowledge distillation.

A passing test without complete evidence is not a complete slice.

## 12. File Update Protocol

When changing any governed artifact, synchronize the applicable chain in the same session:

`source → session log → registry/state → checkpoint/handover → knowledge (when learned) → dictionary (when needed) → build evidence (when buildable) → census → architecture map (when structure changes) → finalized log`.

Session logging begins at session start, not at the end.

## 13. Builds

Allowed build locations:

- `builds/XXX-phase-target/`
- `builds/latest/`
- `.agent/builds/`

Never put builds into product source or knowledge documents.

## 14. Dictionary

As project entities grow, maintain machine dictionary plus generated human dictionary. Update both in the same governed change.

## 15. Enforcement

Census and governance validation must fail on:

- forbidden filenames;
- uncontrolled active findings;
- missing knowledge distillation;
- incomplete session logs;
- file changes without required continuity updates;
- repeated recorded anti-patterns without investigation;
- builds in forbidden locations;
- missing dictionary where required;
- unexplained canonical section loss;
- suspicious canonical deletion;
- claim/evidence or scope/skill inconsistency when those relationships are declared.

Default posture is **fail closed** when authority, current state, or structural integrity cannot be established.

## 16. Hierarchy of Authority

1. User / project owner intent
2. `PRODUCT_LAW.md`
3. `POLICY.md`
4. Endorsed `PRODUCT-KNOWLEDGE.md`
5. `MASTERPLAN.md` + endorsed contracts
6. Current checkpoint + machine state
7. Everything else

When uncertain: stop, preserve the current state, record an investigation, and ask for the missing authority rather than guessing.
