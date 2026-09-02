---
name: scale-adapter
description: Adapt the AGENT Toolkit behaviour according to project size and complexity. Use when a project grows large, when starting a new project of unknown size, when the user mentions scale, large codebase, many files, many tests, monorepo, or asks how the toolkit should behave at different sizes.
---

# Scale Adapter — Adapt the Toolkit to Project Size

The same toolkit must behave differently at different scales.  
This skill tells you how to adapt rules, tools, and focus as the project grows.

## Scale Levels

| Level | Rough Size | Typical Situation |
|-------|------------|-------------------|
| **S – Small** | < 200 files, < 30 tests | Prototype, MVP, single developer or single agent |
| **M – Medium** | 200–1500 files, 30–200 tests | Normal product, small team |
| **L – Large** | 1500–5000+ files, 200–800+ tests | Serious product, multiple agents/teams |
| **XL – Very Large** | 5000+ files, monorepo, many packages | Platform / multi-product |

Use `python scripts/status.py` + census to help judge the current level.

---

## Adaptation Rules by Scale

### S – Small
- Keep everything simple.
- Census + status.py are enough.
- Dictionary is optional.
- Findings can stay closer to the limit of 10.
- Focus on speed of delivery and clear roots.

### M – Medium
- Start using the Dictionary (`.agent/dictionary/`) for entities.
- Run census more regularly.
- Be stricter about distilling findings.
- Use Field-based MASTERPLAN clearly (Backend / Frontend / 3rd-Party…).
- Product tests live inside `src/` or normal `tests/` folders.

### L – Large
- **Dictionary becomes mandatory.**
- Run `status.py` at the start of every session.
- Enforce minimalism harder (findings should usually stay well under 10).
- Split MASTERPLAN Fields more finely if needed.
- Consider package boundaries inside `src/`.
- Census config should be tuned to the real stack.
- Product test files (hundreds) stay in the Project-Development layer — never in `test-files-repo/`.

### XL – Very Large / Monorepo
- Treat each major package as having its own lightweight continuity if needed.
- Keep a top-level MASTERPLAN that points to package-level plans.
- Dictionary and architecture-map become critical navigation tools.
- Status + census should support `--package` or path filtering (future improvement).
- Strong Layer Separation is non-negotiable.

---

## Key Distinctions at Any Scale

| Concern | Toolkit / Governance | Product Code |
|---------|----------------------|--------------|
| Test files | `test-files-repo/` = fast *toolkit* validation only | Real product tests live under `src/` or `tests/` |
| File count | Governance stays small | Product can grow to thousands of files |
| Knowledge | PRODUCT-KNOWLEDGE + Dictionary | Domain knowledge inside code + docs/contracts |
| Continuity | registry, sessions, checkpoints | Normal git + code structure |

---

## When to Invoke This Skill

- Project just crossed into a new size band
- User says “the repo is getting big”
- Starting a project that is expected to become large
- Deciding how strict to be with minimalism / dictionary / census frequency
- Planning monorepo or multi-package structure

---

## Recommended Actions by Scale

**S → M**
- Introduce Dictionary
- Tighten findings discipline
- Make Fields in MASTERPLAN explicit

**M → L**
- Make Dictionary mandatory
- Increase status.py + census frequency
- Review architecture-map and contracts
- Consider package splits inside `src/`

**L → XL**
- Design top-level vs package-level continuity
- Strengthen navigation tools (dictionary, architecture-map, status)
- Keep governance layer extremely lean

---

## Output When Using This Skill

When asked about scale, respond with:

1. Current estimated scale level
2. What should change (or stay the same)
3. Concrete next actions (dictionary, census config, Field structure, etc.)
4. Any risks if the project continues growing without adaptation

---

**Related skills:** `status.py` (via scripts), `roots-definer`, `phase-planner`, `agent-census`, `dictionary-manager`
