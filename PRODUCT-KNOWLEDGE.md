# PRODUCT-KNOWLEDGE.md — Permanent Distilled Memory

> **LONG-TERM BRAIN of the project.**  
> `docs/findings/` = transient working memory (max 10).  
> This file = permanent, dense, searchable knowledge.  
> If an AI repeats a dead end already recorded here, it violated continuity.

**Machine + Human readable.** Do not change the main section headings (they are machine-parsable).

---

## Purpose

- Prevent repeat trial-and-error across sessions and different AI instances
- Keep the active project minimal while knowledge grows
- Serve as the third-highest authority (after Source-of-Truth and POLICY)

**Mandatory:** Read the Anti-Patterns section before every Classify step.

---

## 1. Validated Patterns [DO]

| XXX | Pattern | Why It Works | Evidence | Applies To |
|-----|---------|--------------|----------|------------|
| 000 | Use `.agent/continuity/registry.json` + files as source of truth, never agent memory | Prevents drift across mobile apps and sessions | docs/findings/000-scaffold-toolkit.md | all projects |
| 000 | Keep strict Layer Separation (`src/` = product code only) | Prevents governance noise in product and product code in governance | POLICY.md §2 | all projects |
| 000 | Always run anti-pattern check before Classify | Stops repeating known dead ends | AI_ASSISTANT_READ_ME.md | all projects |

---

## 2. Anti-Patterns & Dead Ends [DONT] — MOST IMPORTANT

| XXX | Anti-Pattern / Dead End | What Failed | Evidence | Never Retry Unless |
|-----|-------------------------|-------------|----------|--------------------|
| 000 | Creating `patch1.md`, `final.md`, `fix.md`, `temp.md`, etc. | Violates naming policy, breaks census, loses traceability | POLICY.md §4 | POLICY itself changes |
| 000 | Skipping PRODUCT-KNOWLEDGE Anti-Patterns read | Repeats dead ends, wastes cycles | AI_ASSISTANT_READ_ME.md | — |
| 000 | Putting builds inside `src/` or `docs/` | Breaks Layer Separation and census | POLICY.md §8 | — |
| 000 | Changing files without updating the full File Update chain | Lost trace, census FAIL, broken continuity | POLICY.md §7 | — |
| 000 | Starting to code / restructure before Observe + anti-pattern check | Creates avoidable discrepancies and rework | AI_ASSISTANT_READ_ME.md §3 | — |

---

## 3. Contract & Dependency Gotchas

| Authority | Consumer | Gotcha | Resolution | XXX |
|-----------|----------|--------|------------|-----|
| — | — | (none yet) | — | — |

---

## 4. Environment & Tool Quirks

| Quirk | Impact | Workaround | Discovered In |
|-------|--------|------------|---------------|
| Mobile AI apps may truncate very long files | Registry or knowledge becomes unreadable | Keep registry and key tables dense but under practical size limits; use census reports | 000 |
| Multiple AI instances = no shared memory | Continuity breaks if files are not trusted | Always re-read the Continuity Reading Order | 000 |

---

## 5. Minimalism Log [Distill → Archive → Delete Trail]

| Date | Source Finding | Distilled To | Archived To | XXX | Notes |
|------|----------------|--------------|-------------|-----|-------|
| 2026-09-01 | docs/findings/000-scaffold-toolkit.md | Validated Patterns + Anti-Patterns | (pending archive) | 000 | Toolkit baseline |

---

## Rules (Hard)

- **MUST** be read (especially §2) before Observe / Classify
- **MUST** be updated during every Advance (no XXX is complete without distillation)
- **MUST NOT** contain raw logs, TODOs, or unvalidated guesses — only endorsed, distilled knowledge
- **NEVER** delete rows. Only add new rows or mark superseded with a reference
- Target size: keep dense. If approaching 500 lines, compress oldest entries to `docs/knowledge-archive/` and leave an index row here

## Distillation Procedure (Mandatory at Advance)

1. Read the completed finding + validation evidence
2. Extract: What worked? What failed? Any gotcha or quirk?
3. Add row(s) to the correct section above (include XXX + evidence link)
4. Add entry to Minimalism Log
5. Update `registry.json` knowledge_index if present
6. Move finding to `docs/archive/XXX-….md` with header  
   `> DISTILLED TO: PRODUCT-KNOWLEDGE.md §X`
7. Only after 2 checkpoints + endorsement may compress or delete (deletion requires explicit endorsement)

---

**Related skills:** `knowledge-distiller`, `anti-pattern-checker`, `minimalism-enforcer`
