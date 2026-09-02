---
name: agent-knowledge
description: Manage permanent product knowledge, anti-patterns, distillation, and minimalism in agent-managed projects. Use when reading or updating PRODUCT-KNOWLEDGE.md, checking for repeated mistakes, distilling findings, enforcing max-10 findings rule, or when the user mentions anti-patterns, knowledge lifecycle, distillation, or minimalism.
---

# Agent Knowledge Lifecycle

PRODUCT-KNOWLEDGE.md is the permanent brain of the project. Findings are transient working memory. Knowledge must increase while active files stay minimal.

## Core Principle

**Minimal files, increasing knowledge.**

- `docs/findings/` = transient (max 10 active files, lifetime = one XXX)
- `PRODUCT-KNOWLEDGE.md` = permanent distilled memory (dense tables)
- After endorsement → distill → archive → after 2 checkpoints may compress or delete (with endorsement proof)

## PRODUCT-KNOWLEDGE.md Structure

Maintain these tables:

1. **Validated Patterns (DO)** — approaches that worked, with XXX + evidence link
2. **Anti-Patterns & Dead Ends (DONT)** — most important section. Prevents repeat trial-and-error
3. **Gotchas** — surprising behaviors
4. **Quirks** — non-obvious project-specific facts
5. **Minimalism Log** — proof of every distillation / archive / deletion (timestamp + XXX + action)

Keep the file dense. Aim for under 500 lines before compressing older rows into `docs/knowledge-archive/`.

## Anti-Pattern Check (Mandatory before Classify)

Before classifying any planned approach:

1. Extract keywords from the planned approach
2. Search PRODUCT-KNOWLEDGE.md Anti-Patterns section
3. If match found → STOP. Create `docs/investigation/XXX-blocked-by-knowledge.md` and propose alternative from Validated Patterns
4. Document the check in the finding file

Skipping this check is itself an anti-pattern.

## Distillation Process

When advancing a completed XXX:

1. Extract what worked, what failed, and any gotchas from the finding + evidence
2. Add one row to the appropriate table in PRODUCT-KNOWLEDGE.md (include XXX + evidence link + short reason)
3. Add a Minimalism Log row with timestamp
4. Update knowledge_index in registry.json if present
5. Only then move the finding to `docs/archive/`

Never add unvalidated guesses.

## Minimalism Rules

- Active findings ≤ 10. If more, distill or archive oldest first.
- Never leave findings forever. Every finding must eventually be distilled or explicitly retained with reason.
- Deletion of any finding requires:
  - Distillation proof (row in PRODUCT-KNOWLEDGE.md)
  - Archive link
  - Endorsement entry
  - Minimalism Log entry

## When to Use This Skill

- At the start of every session (read Anti-Patterns)
- Before every Classify step
- During every Advance step
- When the project feels noisy or findings are accumulating
- When starting a new project (optionally sync knowledge from a previous project)
