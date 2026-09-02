# ENDORSEMENT.md — Approval Ledger

> **Legal / continuity ledger** of what has been approved.  
> Only a human (or explicitly validated advance gate) may move an entry from Draft → Approved.  
> AI agents may only create Drafts.

---

## Rules

- AI may create a **Draft** section.
- AI may **NOT** mark anything as Approved without validation evidence + human/authorized endorsement.
- Every Approved entry must include:
  - XXX
  - Title
  - Endorsed By (human or authorized agent ID)
  - Date
  - Validation evidence path
  - Checkpoint path
  - Handover path
  - Knowledge distillation proof (link to PRODUCT-KNOWLEDGE.md row or Minimalism Log)
- Deletion of any finding also requires an endorsement that explicitly approves the deletion and proves distillation.

---

## Approved Endorsements

| XXX | Title                    | Endorsed By     | Date       | Validation Evidence                  | Checkpoint                              | Handover                              | Knowledge Proof                  |
|-----|--------------------------|-----------------|------------|--------------------------------------|-----------------------------------------|---------------------------------------|----------------------------------|
| 000 | Scaffold toolkit baseline | Toolkit refine  | 2026-09-01 | docs/findings/000-scaffold-toolkit.md | (to be created)                         | (to be created)                       | PRODUCT-KNOWLEDGE.md §1 + §2     |

---

## Pending Drafts (AI — Awaiting Endorsement)

<!-- AI agents add new drafts below this line. Do NOT approve yourself. -->

#### Draft: (none currently)

---

## Endorsement Template (copy for new entries)

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

---

## Deletion Approval Template (required before any finding is deleted)

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

**Related:** POLICY.md (knowledge lifecycle), PRODUCT-KNOWLEDGE.md (Minimalism Log), AI_ASSISTANT_READ_ME.md (Five Evidences)
