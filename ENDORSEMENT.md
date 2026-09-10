# ENDORSEMENT.md — Approval Ledger

> Legal / continuity ledger of what has been approved. Only a human (or explicitly validated advance gate authorized by policy) may move an entry from Draft → Approved. AI agents may create Drafts but must not self-approve them.

---

## Rules

- AI may create a **Draft** section.
- AI may **NOT** mark anything as Approved without validation evidence + human/authorized endorsement.
- Every Approved entry must include XXX, title, endorsing authority, date, validation evidence, checkpoint, handover, and knowledge proof.
- Deletion of any finding requires explicit deletion approval and proof of distillation.
- A promoted Toolkit lesson must prove that it is validated, generalized, correctly scoped, and does not import consumer-specific authority.

---

## Approved Endorsements

| XXX | Title | Endorsed By | Date | Validation Evidence | Checkpoint | Handover | Knowledge Proof |
|---|---|---|---|---|---|---|---|
| 000 | Scaffold toolkit baseline | Toolkit refine | 2026-09-01 | docs/findings/000-scaffold-toolkit.md | (to be created) | (to be created) | PRODUCT-KNOWLEDGE.md §1 + §2 |

---

## Pending Drafts (AI — Awaiting Endorsement)

<!-- AI agents add new drafts below this line. Do NOT approve yourself. -->

#### Draft: 003-self-protecting-universal-foundation
- **Status:** AWAITING VALIDATION + USER / AUTHORIZED ENDORSEMENT
- **Date:** 2026-09-10
- **Impact:** SYSTEMIC
- **Authority:** `PRODUCT_LAW.md` + `POLICY.md`
- **Scope:** user-first authority chain, responsibility model, baseline-driven skill growth, knowledge promotion boundary, canonical structure preservation, bidirectional consistency, single-file human deployment guide.
- **Evidence:** `docs/history/TEAMAI_CANONICAL_STRUCTURE_FAILURE_2026-09-10.md` + `skills/governance/canonical-integrity/SKILL.md`
- **Checkpoint:** to be created at Advance
- **Handover:** to be created at Advance
- **Knowledge Proof:** `PRODUCT-KNOWLEDGE.md` §1–§4 + Minimalism Log 2026-09-10
- **Notes:** TeamAi was used only as a generalized case study. TeamAi product/domain/provider rules remain downstream.

---

## Endorsement Template

```markdown
#### Approved: XXX-phase-target
- **Date:** YYYY-MM-DD
- **Endorsed By:** [Human name or authorized ID]
- **Impact:** LOCAL | BOUNDED | SYSTEMIC
- **Authority Validated:** [file or contract]
- **Consumers Validated:** [list]
- **Evidence:** `validation/evidence/XXX-….md`
- **Checkpoint:** `.agent/continuity/checkpoint-XXX.md`
- **Handover:** `docs/handover/XXX-….md`
- **Knowledge Proof:** PRODUCT-KNOWLEDGE.md §X (row …) + Minimalism Log entry
- **Notes:** [short human-readable summary]
```

## Deletion Approval Template

```markdown
#### Approved Deletion: XXX-phase-target
- **Date:** YYYY-MM-DD
- **Endorsed By:** [Human name or authorized ID]
- **Distilled To:** PRODUCT-KNOWLEDGE.md §X
- **Archived To:** docs/archive/XXX-….md
- **Minimalism Log Entry:** [date / row]
- **Reason:** [why safe to delete]
```

---

**Related:** `PRODUCT_LAW.md`, `POLICY.md`, `PRODUCT-KNOWLEDGE.md`, `docs/CHANGE_CONTRACT.md`, `AI_ASSISTANT_READ_ME.md`
