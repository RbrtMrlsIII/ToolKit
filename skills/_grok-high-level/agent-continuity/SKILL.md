---
name: agent-continuity
description: Enforce continuity reading order, timestamped session logging, and the mandatory file-update protocol across agent sessions. Use at the start of any session in an agent-managed project, when changing files, creating checkpoints, or when the user mentions continuity, session log, file update protocol, registry, or checkpoint.
---

# Agent Continuity Protocol

Every AI instance is a CONTINUATION agent, not a new agent. Trust files, not memory.

## Mandatory Reading Order (Start of Every Session)

Read in this exact order before any action:

1. `POLICY.md` — Constitution
2. `PRODUCT-KNOWLEDGE.md` — especially Anti-Patterns section
3. `.agent/continuity/registry.json` — machine truth
4. `.agent/continuity/state.json` — last good state
5. Latest `checkpoint-XXX.md`
6. `MASTERPLAN.md` — current XXX row
7. `ENDORSEMENT.md` — what is already approved

Skipping PRODUCT-KNOWLEDGE Anti-Patterns is a hard violation.

## Session Logger (Must Start Immediately)

At the very beginning of the session:

1. Create `.agent/sessions/session-YYYY-MM-DD-HHMMSS.json` with:
   - session_id, start_timestamp (ISO 8601 + timezone), agent_id, previous_checkpoint, current_xxx
   - empty actions[] and files_changed[]
2. Create matching human file `docs/sessions/session-YYYY-MM-DD-HHMMSS.md`
3. Log every significant action with timestamp as you go
4. On every file change, immediately append to files_changed with {file, change_type, timestamp, xxx}
5. At end of session, fill end_timestamp, duration_seconds, and complete_trace (full narrative from start reading to final census)

Session log must be complete from the start. Logging only at the end = invalid session + census FAIL.

## File Update Protocol (When Changing ANY File)

Changing one file requires updating the whole chain with timestamps:

1. Source file itself (add timestamp comment when practical)
2. Session log (actions + files_changed)
3. registry.json + state.json (last_updated)
4. checkpoint-XXX.md
5. docs/handover/XXX-...md
6. PRODUCT-KNOWLEDGE.md (if a pattern was learned) + Minimalism Log
7. dictionary.json + regenerate DICTIONARY.md (if new entity)
8. builds/XXX/ + builds/latest/ + .agent/builds/builds.json (if buildable)
9. Run census.py --write
10. Regenerate architecture-map if structure changed
11. Finalize session log (end_timestamp + complete_trace)

Missing steps cause census FAIL and require reconciliation.

## Checkpoint & Handover

- Create or update `.agent/continuity/checkpoint-XXX.md` with timestamp, what changed, files_changed, next recommended actions
- Create matching `docs/handover/XXX-phase-target-handover.md` that includes knowledge proof

## Key Files

| Purpose              | Location                                      |
|----------------------|-----------------------------------------------|
| Machine registry     | `.agent/continuity/registry.json`             |
| Last good state      | `.agent/continuity/state.json`                |
| Checkpoints          | `.agent/continuity/checkpoint-XXX.md`         |
| Session logs         | `.agent/sessions/` + `docs/sessions/`         |
| Dictionary           | `.agent/dictionary/dictionary.json`           |
| Builds registry      | `.agent/builds/builds.json`                   |

Never put builds in `src/` or `docs/`. Use only `builds/` and `.agent/builds/`.
