---
name: safety-reporter
description: Warn the user when a requested command or change is destructive, high-impact, or will affect Source-of-Truth, canonical files, Layer Separation, or large parts of the system. Use before any SYSTEMIC change, deletion, restructuring, or when the user asks for something that can break continuity or the product.
---

# Safety Reporter — Destructive / High-Impact Guard

Before executing any command or change that can cause significant damage or break continuity, surface a clear warning and require explicit confirmation.

## When to Trigger

Trigger this skill (and pause) when the user request involves any of:

- Deleting or overwriting findings, knowledge, contracts, or canonical files
- Changing Source-of-Truth or POLICY.md
- Large restructuring of `src/` or moving code across the Layer boundary
- Force-push, reset, or destructive git operations
- Mass deletion of files
- Changing many consumers at once (SYSTEMIC impact)
- Anything that would violate Layer Separation (`src/` vs Governance)
- Removing or weakening Anti-Patterns / endorsement requirements
- Any action the agent judges as high-risk or irreversible

## Required Warning Format

```markdown
## ⚠️ Safety Warning

**Requested action:** [short summary]

**Impact level:** SYSTEMIC / DESTRUCTIVE / HIGH

**What will be affected:**
- [list files, contracts, layers, or knowledge that will change]

**Risks:**
- [clear list of what can go wrong]

**Recommended safer alternative (if any):**
- [suggestion]

**Required to proceed:** Explicit confirmation from you (e.g. “yes, proceed with the deletion” or “approved”).
```

## Rules

- Always stop and show the warning **before** making the change.
- Do not proceed on silence or weak confirmation (“ok”, “sure”). Require clear language.
- Log the warning and the user’s confirmation in the session log.
- If the action touches Source-of-Truth or canonical files, also recommend creating an investigation or a dedicated XXX first.
- After confirmation, still follow normal File Update Protocol and Five Evidences.

## Integration with Other Skills

- Runs **before** Align when impact is SYSTEMIC or destructive
- Works together with `phase-planner` (a high-impact phase should be proposed + safety-checked)
- Complements `anti-pattern-checker` and `investigation-manager`
