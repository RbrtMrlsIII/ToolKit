# MASTERPLAN.md — Expandable Project Planning System

> **Single source of truth for XXX numbering and progress.** Structured so any human or machine can open this file and see where development stopped in each field. No raw logs or findings here: only vision, map, and checklist.

---

## 1. Project Vision (tied to Product Law)

**What is this project?**
Universal AGENT Toolkit: a reusable operating system for AI-assisted projects with strong continuity, user-first authority, anti-repeat knowledge, disciplined execution, dynamic skills, and scalable responsibility allocation.

**Source-of-Truth statement**
The user's approved product vision is highest authority. `PRODUCT_LAW.md` is its canonical project reconstruction. `POLICY.md`, `MASTERPLAN.md`, skills, tools, implementation, and evidence must serve that authority and may not silently redefine it.

**Primary Authority → Consumers**
- Authority: User intent → `PRODUCT_LAW.md` → `POLICY.md` → approved `MASTERPLAN.md`
- Consumers: all future Agents, WebAi seats, and projects using the Toolkit
- Ownership: Toolkit maintainers / project leads; consuming projects retain their own product/domain/provider authority

---

## 2. Layer Map

```text
Governance / Canonical Layer          Project-Development Layer
────────────────────────────          ─────────────────────────
Product Law + canonical files         src/ / app/ / lib/ / packages/
.agent/ machine state                 product code + product tests
docs/ knowledge + working memory
skills/ reusable procedures
scripts/ governance tools
builds/ outputs only
```

---

## 3. Field-Based Conceptual Map

> Keep every phase grouped under its field. Cross-field relationships belong in `PRODUCT-KNOWLEDGE.md` and architecture docs.

### Field 0 — Foundation / Toolkit
```text
000-scaffold-toolkit
  Authority : POLICY.md + toolkit itself
  Consumers : All future agents + projects
  Impact    : SYSTEMIC
  Status    : ADVANCED

001-foundation-project-scaffold
  Authority : MASTERPLAN.md + scripts/
  Consumers : All future projects created from this toolkit
  Impact    : BOUNDED
  Status    : ADVANCED

002-foundation-project-status
  Authority : scripts/ + continuity state
  Consumers : All agents + humans opening any project
  Impact    : BOUNDED
  Status    : ALIGNED

003-self-protecting-universal-foundation
  Authority : PRODUCT_LAW.md + POLICY.md
  Consumers : Toolkit governance, skills, WebAi seats, consuming projects
  Impact    : SYSTEMIC
  Status    : RECORDED

004-responsibility-unit-seat-model
  Authority : PRODUCT_LAW.md + WEB_AI_SEAT_FOUNDATION
  Consumers : WebAi seats and scalable Agent populations
  Impact    : BOUNDED
  Status    : TODO

005-dynamic-skill-resolution-and-scale
  Authority : Skill scope contracts + MASTERPLAN
  Consumers : all project/field/task combinations
  Impact    : SYSTEMIC
  Status    : TODO

006-knowledge-promotion-and-generalization
  Authority : PRODUCT-KNOWLEDGE + endorsement rules
  Consumers : Toolkit learning loop + consuming projects
  Impact    : BOUNDED
  Status    : TODO

007-canonical-change-integrity
  Authority : POLICY + CHANGE_CONTRACT + integrity validator
  Consumers : canonical documentation and governance merges
  Impact    : SYSTEMIC
  Status    : TODO

008-bidirectional-evidence-claim-validation
  Authority : Product Law + evidence contracts
  Consumers : skills, docs, implementation, verification
  Impact    : SYSTEMIC
  Status    : TODO

009-multi-agent-responsibility-allocation
  Authority : responsibility model + authorization
  Consumers : 2–8 Agent/WebAi populations
  Impact    : BOUNDED
  Status    : TODO

010-cross-project-learning-feedback
  Authority : upstream boundary + endorsement
  Consumers : Toolkit + multiple consuming projects
  Impact    : SYSTEMIC
  Status    : TODO
```

### Field 1 — Backend
```text
(empty — Toolkit supplies patterns; concrete backend remains consumer-specific unless generalized)
```

### Field 2 — 3rd-Party / Integrations
```text
(empty)
```

### Field 3 — Frontend / UI
```text
(empty)
```

### Field 4 — Shared / Domain
```text
(empty)
```

### Field 5 — Integration & Validation
```text
(empty — universal validation mechanisms are developed under Field 0 and later consumed here)
```

### Field 6 — Release / Operations
```text
(empty — human deployment guide is defined under Field 0; provider details remain downstream)
```

> New work is planted only after approval and must be assigned to the correct Field and XXX.

---

## 4. Execution Checklist (THE only source for XXX numbers)

| XXX | Field | Phase | Target | Impact | Status | Evidence |
|-----|---|---|---|---|---|---|
| 000 | Foundation | scaffold | toolkit | SYSTEMIC | ADVANCED | 000-scaffold-toolkit.md |
| 001 | Foundation | foundation | project-scaffold | BOUNDED | ADVANCED | 001-foundation-project-scaffold.md |
| 002 | Foundation | foundation | project-status | BOUNDED | ALIGNED | 002-foundation-project-status.md |
| 003 | Foundation | governance | self-protecting-universal-foundation | SYSTEMIC | VALIDATED_STATIC | validation/evidence/003-self-protecting-universal-foundation.md |
| 004 | Foundation | responsibility | responsibility-unit-seat-model | BOUNDED | TODO | docs/WEB_AI_SEAT_FOUNDATION.md |
| 005 | Foundation | skills | dynamic-skill-resolution-and-scale | SYSTEMIC | TODO | docs/SKILL_SCOPE_INDEX.md |
| 006 | Foundation | knowledge | promotion-and-generalization | BOUNDED | TODO | PRODUCT-KNOWLEDGE.md |
| 007 | Foundation | governance | canonical-change-integrity | SYSTEMIC | TODO | skills/governance/canonical-integrity/SKILL.md |
| 008 | Foundation | validation | bidirectional-evidence-claim-validation | SYSTEMIC | TODO | docs/TOOLKIT_ARCHITECTURE.md |
| 009 | Foundation | responsibility | multi-agent-responsibility-allocation | BOUNDED | TODO | docs/WEB_AI_SEAT_FOUNDATION.md |
| 010 | Foundation | learning | cross-project-learning-feedback | SYSTEMIC | TODO | docs/KNOWLEDGE_UPSTREAM_BOUNDARY.md |

**Status values:** `TODO → OBSERVED → RECORDED → UNDERSTOOD → CLASSIFIED → ALIGNED → VALIDATED_STATIC → VALIDATED → ENDORSED → ADVANCED`.

**Rules**
- Never invent an XXX that is not first proposed and approved.
- Never skip XXXs.
- One active XXX at a time.
- Every completed XXX must produce the Five Evidences.
- Baseline freezes must trigger skill-coverage review.
- Mobile / continuation agents pick the first non-ADVANCED row and read the current authority chain before acting.

---

## 5. Impact Classification

| Impact | Meaning | Example |
|---|---|---|
| LOCAL | Single file/internal with no consumer impact | comment, purely local refactor |
| BOUNDED | One authority + limited consumers, contract recorded | skill extension, responsibility unit |
| SYSTEMIC | Product Law, POLICY, registry/state, canonical structure, or many consumers | authority model, canonical integrity |

Prefer LOCAL or BOUNDED. SYSTEMIC work requires explicit attention to user authority, safety, reconciliation, and evidence.

---

## 6. Current Focus

| Item | Value |
|---|---|
| **Current XXX** | 003 |
| **Status** | VALIDATED_STATIC |
| **Current Field** | Foundation |
| **Next XXX** | 004 |
| **Open Investigations** | none |
| **Baseline focus** | self-protecting universal operating foundation |
| **Knowledge transfer** | TeamAi canonical-structure lesson generalized upstream |
| **Validation** | Static governance/evidence validation complete; GitHub Actions execution pending |
| **Deployment guide** | `docs/USER_MANUAL_DEPLOYMENT.md` |

---

## 7. Dependency & Contract Pointers

- Product Law → `PRODUCT_LAW.md`
- Execution policy → `POLICY.md`
- Knowledge → `PRODUCT-KNOWLEDGE.md`
- Responsibility / seats → `docs/WEB_AI_SEAT_FOUNDATION.md`
- Architecture → `docs/TOOLKIT_ARCHITECTURE.md`
- Change contract → `docs/CHANGE_CONTRACT.md`
- Skill scope → `docs/SKILL_SCOPE_INDEX.md`
- Full repo wiring → `docs/STRUCTURE.md`
- User deployment → `docs/USER_MANUAL_DEPLOYMENT.md`
- Upstream boundary → `docs/KNOWLEDGE_UPSTREAM_BOUNDARY.md`

---

## 8. How to Add a New XXX (Mandatory Process)

1. Use `phase-planner` to propose Field + XXX + Target + Impact.
2. Obtain explicit user approval for material direction.
3. Reconcile `PRODUCT_LAW.md` when product meaning changes.
4. Plant or branch the approved row here.
5. Identify the smallest sufficient skill bundle and check whether the frozen baseline requires a new skill.
6. Complete Observe + Anti-Pattern check before implementation.
7. Execute through O-R-U-C-A-V-E-A and produce the Five Evidences.
8. Distill validated/generalized lessons into `PRODUCT-KNOWLEDGE.md`.
9. Endorse / Advance only after verification and continuity state are complete.

---

**Related skills:** `phase-planner`, `scale-adapter`, `canonical-integrity`, `safety-reporter`, `agent-orucavea`.
