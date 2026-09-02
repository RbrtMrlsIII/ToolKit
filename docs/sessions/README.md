# Sessions — Timestamped Complete Tracing

> **Fixes AI forgetting to update files when changing something**

## Locations

- `.agent/sessions/session-YYYY-MM-DD-HHMMSS.json` — Machine-readable, complete from start
- `docs/sessions/session-YYYY-MM-DD-HHMMSS.md` — Human-readable

## Must Be Complete From Start for Tracing

Every AI session MUST create session log at START, not at end.

**Start:** When AI starts, before reading POLICY, create session-*.json with start_timestamp, agent_id, previous_checkpoint

**During:** Log every action with timestamp: Read POLICY, Read PRODUCT-KNOWLEDGE Anti-Patterns, Observe authority, Align file, etc. When changing file, add to files_changed {file, change_type, timestamp, xxx}

**End:** Update end_timestamp, duration, complete_trace (full sentence from start reading to end census), files_changed includes ALL files updated (registry, state, checkpoint, handover, PRODUCT-KNOWLEDGE, dictionary, builds, census)

If session log only at end → invalid → census FAIL

## Example

Machine: session-2026-09-01-103000-example.json
Human: session-2026-09-01-103000-example.md

## Enforcement

Census checks: session log exists for last XXX, has start+end timestamp, files_changed includes all changed files, complete_trace from start.

If AI changes file without updating registry/state/checkpoint/session log → census FAIL + reconciliation required.
