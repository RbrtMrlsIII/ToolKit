# MASTERPLAN.md — Expandable Project Planning System

> **Single source of truth for XXX numbering and progress.**  
> Structured so any human or machine can open this file and instantly see  
> where development stopped in each field (Foundation, Backend, 3rd-Party, Frontend, etc.).  
> No raw logs or findings here — only vision, map, and checklist.

---

## 1. Project Vision (tied to Source-of-Truth)

**What is this project?**  
Universal AGENT Toolkit — reusable operating system for AI-assisted projects with strong continuity, anti-repeat knowledge, and disciplined execution.

**Source-of-Truth statement**  
The 6 Canonical Files + Layer Separation (`src/` = product code only) + PRODUCT-KNOWLEDGE Anti-Patterns form the non-negotiable foundation (see POLICY.md §1).

**Primary Authority → Consumers**  
- Authority: POLICY.md + this MASTERPLAN + docs/contracts/  
- Consumers: All future agents and all projects built with this toolkit  
- Ownership: Toolkit maintainers / project leads

---

## 2. Layer Map

```
Governance / Canonical Layer          Project-Development Layer
────────────────────────────          ─────────────────────────
6 Canonical Files (root)              src/   ← PRODUCT CODE ONLY
.agent/   (machine state)
docs/     (knowledge & working memory)
skills/ + scripts/
builds/   (outputs only)
```

---

## 3. Field-Based Conceptual Map

> Keep every phase grouped under its field.  
> This is what makes progress and stopping points obvious at a glance.

### Field 0 — Foundation / Toolkit
```
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
  Authority : scripts/ + .agent/continuity/
  Consumers : All agents + humans opening any project
  Impact    : BOUNDED
  Status    : ADVANCED

003-self-protecting-universal-foundation
  Authority : PRODUCT_LAW.md + POLICY.md + governance contracts
  Consumers : Toolkit governance + WebAi seats + consuming projects
  Impact    : SYSTEMIC
  Status    : ADVANCED

004-responsibility-unit-seat-model
  Authority : PRODUCT_LAW.md + POLICY.md + approved 004 contract
  Consumers : WebAi seats + future agents/projects
  Impact    : SYSTEMIC
  Status    : ADVANCED / FROZEN

005-dynamic-skill-resolution-scale-adaptation
  Authority : PRODUCT_LAW.md + POLICY.md + approved 005 contract
  Consumers : WebAi seats + future agents/projects
  Impact    : SYSTEMIC
  Status    : ADVANCED / FROZEN

006-knowledge-promotion-and-generalization
  Authority : PRODUCT_LAW.md + POLICY.md + approved 006 contract
  Consumers : Toolkit knowledge system + future consumer projects
  Impact    : SYSTEMIC
  Status    : ADVANCED / FROZEN

007-canonical-evolution-integrity
  Authority : PRODUCT_LAW.md + POLICY.md + approved 007 contract
  Consumers : Toolkit canonical governance + future agents/projects
  Impact    : SYSTEMIC
  Status    : OBSERVED / ACTIVE
```

### Field 1 — Backend
```
(empty — plant new XXXs here via phase-planner)
```

### Field 2 — 3rd-Party / Integrations
```
(empty — plant new XXXs here via phase-planner)
```

### Field 3 — Frontend / UI
```
(empty — plant new XXXs here via phase-planner)
```

### Field 4 — Shared / Domain
```
(empty)
```

### Field 5 — Integration & Validation
```
(empty)
```

### Field 6 — Release / Operations
```
(empty)
```

> When a new phase is approved, add it under the correct Field above  
> and also add the corresponding row in the Execution Checklist below.

---

## 4. Execution Checklist (THE only source for XXX numbers)

| XXX | Field              | Phase     | Target                         | Impact    | Status   | Evidence |
|-----|--------------------|-----------|--------------------------------|-----------|----------|----------|
| 000 | Foundation         | scaffold  | toolkit                        | SYSTEMIC  | ADVANCED | 000-scaffold-toolkit.md |
| 001 | Foundation         | foundation| project-scaffold               | BOUNDED   | ADVANCED | 001-foundation-project-scaffold.md |
| 002 | Foundation         | foundation| project-status                 | BOUNDED   | ADVANCED | 002-foundation-project-status.md |
| 003 | Foundation         | governance| self-protecting-universal-foundation | SYSTEMIC | ADVANCED | 003-self-protecting-universal-foundation.md |
| 004 | Foundation         | foundation| responsibility-unit-seat-model | SYSTEMIC  | ADVANCED | 004-responsibility-unit-seat-model.md |
| 005 | Foundation         | foundation| dynamic-skill-resolution-scale-adaptation | SYSTEMIC | ADVANCED | 005-dynamic-skill-resolution-scale-adaptation.md |
| 006 | Foundation         | knowledge | knowledge-promotion-and-generalization | SYSTEMIC | ADVANCED | 006-knowledge-promotion-and-generalization.md |
| 007 | Foundation         | governance | canonical-evolution-integrity | SYSTEMIC | OBSERVED | 007-canonical-evolution-integrity.md |

**Status values (strict order):**  
`TODO → OBSERVED → RECORDED → UNDERSTOOD → CLASSIFIED → ALIGNED → VALIDATED → ENDORSED → ADVANCED`

**Rules**
- Never invent an XXX that is not first proposed via `phase-planner` and approved.
- Never skip XXXs.
- One active XXX at a time.
- Every XXX must produce the Five Evidences.
- Group rows by Field so progress per area is obvious at a glance.
- Mobile / continuation agents: always pick the first non-ADVANCED row.

---

## 5. Impact Classification

| Impact    | Meaning                                                      | Example                          |
|-----------|--------------------------------------------------------------|----------------------------------|
| LOCAL     | Single file / internal, no consumer impact                   | Comment, pure refactor           |
| BOUNDED   | One authority + limited consumers, contract recorded         | New endpoint, new UI screen     |
| SYSTEMIC  | Touches Source-of-Truth, POLICY, registry, or many consumers | Auth model, new major field      |

Prefer LOCAL or BOUNDED. Use SYSTEMIC only when necessary (and trigger `safety-reporter`).

---

## 6. Current Focus (update every session)

| Item                    | Value                                      |
|-------------------------|--------------------------------------------|
| **Current XXX**         | 007                                        |
| **Status**              | OBSERVED                                   |
| **Current Field**       | Foundation                                 |
| **Next XXX**            | 008 (after 007 is advanced)                |
| **Open Investigations** | none                                       |
| **Last Checkpoint**     | 006 frozen baseline                        |
| **Active Findings**     | 1                                          |

---

## 7. Dependency & Contract Pointers

- Contracts          → `docs/contracts/`
- Dependency map     → `docs/dependencies/`
- Architecture map   → `docs/architecture-map.md`
- Dictionary         → `.agent/dictionary/dictionary.json` + `docs/dictionary/DICTIONARY.md`
- Full repo wiring   → `docs/STRUCTURE.md`

---

## 8. How to Add a New XXX (Mandatory Process)

1. Use **phase-planner** skill → propose Field + XXX + Target + Impact
2. Wait for explicit user approval
3. Plant (new Field) or Branch (existing Field) on this file:
   - Add entry under the correct Field in §3
   - Add row in the Execution Checklist (§4)
   - Update Current Focus (§6)
4. Only then create the finding and begin Observe
5. Never start coding until the row exists and anti-pattern check is done

---

**Related skills:** `phase-planner`, `safety-reporter`, `agent-orucavea`, `knowledge-distiller`, `knowledge-promotion`, `canonical-evolution-integrity`
