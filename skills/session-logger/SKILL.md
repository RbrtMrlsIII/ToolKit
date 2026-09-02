# SKILL: Session Logger — Timestamped Complete Tracing

> Universal skill — session logging with timestamp, must be complete from start for tracing. Fixes AI forgetting to update files.

### Metadata
- ID: session-logger
- Phase: Session (runs entire session from start to end)
- Type: governance
- Applies To: All projects

### When To Use
- At START of every AI session on mobile, before any other action
- At END of session after census
- When AI changes any file — log files_changed with timestamp

### Prerequisites
- POLICY.md section 8 (File Update Protocol)
- .agent/sessions/ and docs/sessions/ folders exist

### Steps

1. **At START (first action):**
   - Generate session_id: YYYY-MM-DD-HHMMSS-AgentID (e.g., 2026-09-01-103000-AgentMobile1)
   - Create `.agent/sessions/session-YYYY-MM-DD-HHMMSS.json` with:
     - session_id, start_timestamp ISO 8601 with timezone, agent_id, previous_checkpoint, current_xxx
     - actions: [] empty initially
     - files_changed: [] empty initially
     - complete_trace: "" empty initially
   - Also create `docs/sessions/session-YYYY-MM-DD-HHMMSS.md` human version with same info

2. **During session — log every action with timestamp:**
   - Read POLICY.md → add action {timestamp, action: Read, file: POLICY.md}
   - Read PRODUCT-KNOWLEDGE.md Anti-Patterns → action Read
   - Observe authority → action Observe with xxx
   - Record finding → action Record
   - Align (change file) → action Align + add to files_changed {file, change_type: modified, timestamp, xxx}
   - Every file change must be logged immediately with timestamp

3. **At END (last action before checkpoint):**
   - Update end_timestamp, duration_seconds = end - start
   - Update complete_trace: full sentence from start reading to end census, e.g., "Start: Read POLICY, PRODUCT-KNOWLEDGE Anti-Patterns, registry, checkpoint-005 → Observe api-v1.yaml → Record 006 → ... → Census → End"
   - Update files_changed with all files updated in this session (registry, state, checkpoint, handover, PRODUCT-KNOWLEDGE, dictionary, builds, census)
   - Write final JSON + MD

4. **Validation:**
   - Session log must have start and end timestamp
   - Must have at least 5 actions
   - Must have files_changed that includes all changed files in this session
   - Must have complete_trace from start
   - If missing, census FAIL + session invalid

### Output Template

Machine: .agent/sessions/session-YYYY-MM-DD-HHMMSS.json
```json
{
  "session_id": "2026-09-01-103000-AgentMobile1",
  "start_timestamp": "2026-09-01T10:30:00+08:00",
  "end_timestamp": "2026-09-01T10:45:00+08:00",
  "agent_id": "AgentMobile1",
  "previous_checkpoint": "checkpoint-005.md",
  "current_xxx": "006",
  "actions": [...],
  "files_changed": [...],
  "complete_trace": "Start: ... → End",
  "duration_seconds": 900
}
```

Human: docs/sessions/session-YYYY-MM-DD-HHMMSS.md
```markdown
# Session 2026-09-01-103000-AgentMobile1
Start: 2026-09-01T10:30:00+08:00
End: 2026-09-01T10:45:00+08:00
Agent: AgentMobile1
Previous Checkpoint: checkpoint-005.md
Current XXX: 006

Actions:
- 10:30:05 Read POLICY.md
- 10:30:10 Read PRODUCT-KNOWLEDGE.md Anti-Patterns
...

Files Changed:
- src/backend/auth.ts modified 10:35:00 XXX 006
...

Complete Trace: Start: Read POLICY... → End: Census
```

### Validation Checklist
- [ ] Session log created at START, not just at end
- [ ] Has start_timestamp and end_timestamp ISO 8601
- [ ] Has agent_id, previous_checkpoint, current_xxx
- [ ] Actions logged with timestamp for every Read, Observe, Record, etc.
- [ ] files_changed includes all changed files with timestamp, change_type, xxx
- [ ] complete_trace is complete from start reading to end census
- [ ] Duration calculated
- [ ] Both machine JSON and human MD created

### Anti-Patterns
- Creating session log only at end — must be at start for tracing
- Forgetting to log file changes — census will detect files_changed mismatch
- No timestamp — session invalid

### Distillation
If session logging pattern works, distill to PRODUCT-KNOWLEDGE.md Validated Patterns: "Session log at start with timestamp prevents lost tracing"
If AI forgets, distill to Anti-Patterns: "No session log at start → lost trace"
