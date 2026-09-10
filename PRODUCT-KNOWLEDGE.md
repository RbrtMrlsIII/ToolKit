# PRODUCT-KNOWLEDGE.md — Permanent Distilled Memory

> **LONG-TERM BRAIN of the project.** `docs/findings/` = transient working memory. This file = permanent, dense, searchable knowledge. If an AI repeats a dead end already recorded here, it violated continuity.

**Machine + Human readable.** Keep the main section headings stable because tools may parse them.

---

## Purpose

- Prevent repeat trial-and-error across sessions and AI instances.
- Keep the active project minimal while knowledge grows.
- Explain validated relationships between fields, responsibilities, skills, artifacts, tools, runtime/provider constraints, and verification.
- Serve as a high-authority reusable knowledge layer below Product Law and POLICY.

**Mandatory:** Read the Anti-Patterns section before every Classify step.

---

## 1. Validated Patterns [DO]

| XXX | Pattern | Why It Works | Evidence | Applies To |
|-----|---------|--------------|----------|------------|
| 000 | Use machine state + canonical files as source of truth, never agent memory | Prevents drift across mobile apps and sessions | docs/findings/000-scaffold-toolkit.md | all projects |
| 000 | Keep strict Layer Separation (`src/` = product code only) | Prevents governance noise in product and product code in governance | POLICY.md §2 | all projects |
| 000 | Always run anti-pattern check before Classify | Stops repeating known dead ends | AI_ASSISTANT_READ_ME.md | all projects |
| 003 | Treat the user's approved vision as the highest product authority and reconstruct it into Product Law before planning execution | Prevents Agent interpretation from silently becoming product truth | PRODUCT_LAW.md §0–2; docs/TOOLKIT_ARCHITECTURE.md §6 | all projects |
| 003 | Define Agent work as Responsibility Units and allocate those units across Seats instead of duplicating skills per Agent | Scales from small to larger Agent populations without skill-library multiplication | PRODUCT_LAW.md §4–5; docs/WEB_AI_SEAT_FOUNDATION.md | all projects / WebAi seats |
| 003 | Treat each validated baseline freeze as a trigger for skill-coverage review | Skills evolve with repeatable execution instead of remaining a static catalog | PRODUCT_LAW.md §5; AI_ASSISTANT_READ_ME.md §6 | all projects |
| 003 | Protect canonical document structure as part of knowledge integrity | A present new claim does not prove unrelated canonical content was preserved | docs/history/TEAMAI_CANONICAL_STRUCTURE_FAILURE_2026-09-10.md; skills/governance/canonical-integrity/SKILL.md | canonical governance docs |
| 003 | Promote only validated, generalized lessons upstream | Prevents a consumer project from contaminating a universal toolkit with product-specific assumptions | docs/KNOWLEDGE_UPSTREAM_BOUNDARY.md; docs/history/TEAMAI_CANONICAL_STRUCTURE_FAILURE_2026-09-10.md | Toolkit + consuming projects |

---

## 2. Anti-Patterns & Dead Ends [DONT] — MOST IMPORTANT

| XXX | Anti-Pattern / Dead End | What Failed | Evidence | Never Retry Unless |
|-----|-------------------------|-------------|----------|--------------------|
| 000 | Creating `patch1.md`, `final.md`, `fix.md`, `temp.md`, etc. | Violates naming policy, breaks census, loses traceability | POLICY.md §4 | POLICY itself changes |
| 000 | Skipping PRODUCT-KNOWLEDGE Anti-Patterns read | Repeats dead ends, wastes cycles | AI_ASSISTANT_READ_ME.md | — |
| 000 | Putting builds inside `src/` or `docs/` | Breaks Layer Separation and census | POLICY.md §13 | — |
| 000 | Changing files without updating the required File Update chain | Lost trace, census FAIL, broken continuity | POLICY.md §12 | — |
| 000 | Starting to code / restructure before Observe + anti-pattern check | Creates avoidable discrepancies and rework | AI_ASSISTANT_READ_ME.md | — |
| 003 | Updating a narrow canonical frontier while deleting unrelated canonical sections | The requested claim can remain present while valuable knowledge structure disappears | docs/history/TEAMAI_CANONICAL_STRUCTURE_FAILURE_2026-09-10.md | Explicitly authorized structural change + preserved evidence |
| 003 | Treating historical material as cleanup because newer wording exists | Historical evidence is not obsolete merely because current state changed | docs/TOOLKIT_ARCHITECTURE.md §7 | Explicit archival/deletion authority and proof |
| 003 | Copying a useful consumer-project rule upstream without generalization | Toolkit becomes project-specific and can incorrectly affect unrelated consumers | docs/KNOWLEDGE_UPSTREAM_BOUNDARY.md | Validated reusable generalization |
| 003 | Treating a growing skill count as permission growth | More tools can accidentally imply more authority | PRODUCT_LAW.md §5; AI_ASSISTANT_READ_ME.md §8 | Never; authority must remain separately authorized |

---

## 3. Contract & Dependency Gotchas

| Authority | Consumer | Gotcha | Resolution | XXX |
|-----------|----------|--------|------------|-----|
| User / Product Law | MASTERPLAN | Planning may reinterpret intent unless user-approved meaning is reconstructed first | Reconcile Product Law before creating/advancing slices | 003 |
| MASTERPLAN baseline | Skills | Frozen execution baselines can create new repeatable procedures that are not yet represented as skills | Trigger skill-coverage review at each baseline freeze | 003 |
| Canonical document | Governance validator | New expected strings do not prove unrelated structure survived | Run structural integrity check in addition to semantic checks | 003 |
| Toolkit | Consumer project | Universal mechanism can be mistaken for consumer authority | Require explicit consumer adaptation and permission reconciliation | 003 |

---

## 4. Environment & Tool Quirks

| Quirk | Impact | Workaround | Discovered In |
|-------|--------|------------|---------------|
| Mobile AI apps may truncate very long files | Registry or knowledge becomes unreadable | Keep machine state and dense tables compact; use generated reports | 000 |
| Multiple AI instances have no shared conversation memory | Continuity breaks if files are not trusted | Always re-read the authoritative continuation order | 000 |
| Canonical documents are frequently edited as large prose blocks | Narrow changes can accidentally delete unrelated sections | Use change contracts + structural heading/deletion validation | 003 |
| Skill catalogs grow as execution baselines freeze | Static indexes become stale and may under-equip later slices | Re-run scope classification and coverage review after each baseline freeze | 003 |

---

## 5. Minimalism Log [Distill → Archive → Delete Trail]

| Date | Source Finding | Distilled To | Archived To | XXX | Notes |
|------|----------------|--------------|-------------|-----|-------|
| 2026-09-01 | docs/findings/000-scaffold-toolkit.md | Validated Patterns + Anti-Patterns | (pending archive) | 000 | Toolkit baseline |
| 2026-09-10 | TeamAi governance/index drift + canonical section-loss case | §1 pattern, §2 anti-pattern, §3 gotchas, §4 quirk | docs/history/TEAMAI_CANONICAL_STRUCTURE_FAILURE_2026-09-10.md | 003 | Generalized upstream learning only; TeamAi product rules remain downstream |
| 2026-09-10 | WebAi seat/responsibility scaling model | §1 responsibility + baseline/skill growth patterns | docs/WEB_AI_SEAT_FOUNDATION.md | 003 | Responsibility allocation, not skill duplication |

---

## Conceptual Connection Map

This section is the durable relationship map, not a session log:

```text
USER AUTHORITY
   ↓
PRODUCT_LAW
   ↓
MASTERPLAN SLICE / BASELINE
   ↓
FIELD / RESPONSIBILITY UNIT
   ↓
SKILL SCOPE + REQUIRED KNOWLEDGE
   ↓
TOOLS / WORKSPACE / RUNTIME ADAPTATION
   ↓
AUTHORIZED ACTION
   ↓
VERIFICATION / EVIDENCE
   ↓
HANDOVER / ENDORSEMENT
   ↓
VALIDATED KNOWLEDGE
   ↓
SKILL / GOVERNANCE EVOLUTION
```

`PRODUCT-KNOWLEDGE.md` should grow primarily by strengthening this map: when a field, skill, provider/runtime, artifact, or verification dependency becomes clearer, record the relationship in the smallest useful durable form.

---

## Rules (Hard)

- **MUST** be read, especially §2, before Observe / Classify.
- **MUST** be updated when a validated reusable lesson is promoted.
- **MUST NOT** contain raw logs, TODOs, secrets, or unvalidated guesses.
- **NEVER** delete a knowledge row. Add, supersede, or archive by reference.
- Consumer-specific lessons remain downstream unless they pass validation + generalization.
- Knowledge growth must increase conceptual coverage without becoming an unbounded log.
- Target size: remain dense; when approaching practical size limits, compress oldest knowledge into `docs/knowledge-archive/` and leave an index reference.

## Distillation Procedure (Mandatory at Advance)

1. Read the completed finding and validation evidence.
2. Extract what worked, what failed, the dependency/relationship, and any reusable constraint.
3. Decide the scope class: UNIVERSAL, ADAPTABLE, CONSUMER-SPECIFIC, EPHEMERAL, HISTORICAL, or CANDIDATE.
4. Add the smallest durable row(s) here when the lesson is validated for retention.
5. Add a Minimalism Log entry.
6. Update machine knowledge indexes where present.
7. Archive the source finding with a distillation proof when lifecycle rules require it.
8. Promote into a universal skill or governance rule only after generalization and endorsement.

---

**Related skills:** `anti-pattern-checker`, `knowledge-distiller`, `minimalism-enforcer`, `canonical-integrity`.
