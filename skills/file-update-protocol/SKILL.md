# SKILL: File Update Protocol — When Changing Something Update All Related Files

> Universal skill — fixes AI mostly forgot how to update files when they change something.

### Metadata
- ID: file-update-protocol
- Phase: Advance (but applies to any file change)
- Type: governance
- Applies To: All projects

### When To Use
- When you change ANY source file (src/, docs/contracts/, etc.)
- When you update registry, state, checkpoint, etc.
- Always — every file change must follow this protocol

### Prerequisites
- POLICY.md section 8 and 11 (File Update Checklist)
- Session logger skill already started session log

### Steps — File Update Chain (Mandatory)

When you change source file e.g., `src/backend/auth.ts`:

1. **Source file** — change it, add timestamp comment if code: `// Updated: 2026-09-01 10:35:00 XXX 006 by AgentMobile1`

2. **Session Log** — `.agent/sessions/session-YYYY-MM-DD-HHMMSS.json` — add to actions {timestamp, action: Align, file: src/backend/auth.ts, xxx: 006} + add to files_changed {file, change_type: modified, timestamp, xxx}

3. **Registry** — `.agent/continuity/registry.json` — update current_xxx, todo, completed, last_updated: timestamp ISO 8601

4. **State** — `.agent/continuity/state.json` — update last_good_state, last_updated timestamp, active_findings count

5. **Checkpoint** — `.agent/continuity/checkpoint-XXX.md` — update with timestamp, what changed, files_changed list, next actions

6. **Handover** — `docs/handover/XXX-phase-target-handover.md` — update with timestamp, knowledge proof, files_changed

7. **PRODUCT-KNOWLEDGE.md** — if new pattern learned, add row to Validated Patterns or Anti-Patterns with XXX + evidence link + timestamp in Minimalism Log

8. **Dictionary** — if new entity (tab, UI screen, 3D model, endpoint, term), update `.agent/dictionary/dictionary.json` with id, name, path, file, xxx, created_at timestamp

9. **Dictionary MD** — run `python scripts/dictionary-generator.py` to regenerate `docs/dictionary/DICTIONARY.md` from JSON

10. **Build** — if buildable, run canonical-build skill: place build in `builds/XXX-phase-target/` + `builds/latest/` + build log with timestamp + update `.agent/builds/builds.json`

11. **Census** — run `python scripts/census.py --base . --write` — updates inventory (tabs, UI, 3D counts) + cleanliness + dashboard

12. **Architecture Map** — if structure changed (new contract, new dependency), run `python scripts/architecture-map-generator.py`

13. **Session Log End** — update end_timestamp, duration, complete_trace

### Output Template

All files updated with timestamp. Example:

- src/backend/auth.ts — modified 2026-09-01T10:35:00+08:00 XXX 006
- .agent/sessions/session-2026-09-01-103000.json — updated with files_changed
- .agent/continuity/registry.json — last_updated 2026-09-01T10:40:00+08:00 current_xxx 006
- etc.

### Validation Checklist
- [ ] Source file has timestamp comment
- [ ] Session log has files_changed entry with timestamp, change_type, xxx
- [ ] Registry updated with last_updated timestamp
- [ ] State updated
- [ ] Checkpoint updated with timestamp + what changed
- [ ] Handover updated
- [ ] PRODUCT-KNOWLEDGE.md updated if pattern learned (with Minimalism Log timestamp)
- [ ] Dictionary updated if new entity (with created_at timestamp)
- [ ] Build placed in builds/XXX/ + builds/latest/ + .agent/builds/builds.json updated if buildable
- [ ] Census run --write, dashboard generated
- [ ] Architecture map regenerated if needed
- [ ] Session log end_timestamp + complete_trace updated

### Anti-Patterns
- Changing source file without updating registry/state/checkpoint/session log → census FAIL + reconciliation required
- No timestamp — file update invalid
- Only updating source file, forgetting related files — AI mostly forgot, now enforced

### Distillation
Pattern: "File update chain with timestamp ensures complete tracing from start"
Anti-Pattern: "Changed file without updating registry/state/checkpoint → lost trace"
