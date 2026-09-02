---
name: agent-structure
description: Apply or scaffold the canonical agent toolkit structure with 6 core files, skills, scripts, .agent machine state, and docs layout. Use when creating a new project from the agent toolkit, auditing structure of an existing agent-managed repo, or when the user mentions canonical files, agent-repo-template, or toolkit structure.
---

# Agent Canonical Structure

Every project managed by this toolkit has the same shape so any AI can hop in and continue.

## Six Canonical Files (Always Present)

1. **README.md** — Front-door only. Wiring and status. Keep under 80 lines. Never put findings, TODOs, or logs here.
2. **AI_ASSISTANT_READ_ME.md** — Operating system for AI agents. Reading order, discipline, constraints.
3. **MASTERPLAN.md** — Conceptual map + current focus + XXX checklist.
4. **POLICY.md** — Constitution (structure rules, naming, knowledge lifecycle, file-update protocol).
5. **PRODUCT-KNOWLEDGE.md** — Permanent brain (Validated Patterns + Anti-Patterns + Gotchas + Minimalism Log).
6. **ENDORSEMENT.md** — Human-validated approval ledger.

## Standard Directory Layout

```
.
├── README.md
├── AI_ASSISTANT_READ_ME.md
├── MASTERPLAN.md
├── POLICY.md
├── PRODUCT-KNOWLEDGE.md
├── ENDORSEMENT.md
├── skills/                     # Loadable SKILL.md files
├── scripts/                    # census.py, knowledge-search.py, etc.
├── prompts/                    # Mobile paste-ready prompts
├── .agent/
│   ├── continuity/             # registry.json, state.json, checkpoint-*.md
│   ├── sessions/
│   ├── dictionary/
│   ├── builds/
│   └── census/
├── docs/
│   ├── findings/               # Transient, max 10
│   ├── handover/
│   ├── sessions/
│   ├── archive/
│   ├── knowledge-archive/
│   ├── dictionary/
│   ├── census/
│   └── architecture-map.md
├── validation/evidence/
├── builds/                     # Only place for build outputs
│   ├── latest/
│   ├── XXX-phase-target/
│   └── archive/
├── backend-integrations/       # Optional copy-paste modules
└── test-files/                 # Optional fast validation scripts
```

## Scaffolding a New Project

1. Copy the clean template
2. Fill the 6 canonical files with project-specific content
3. Run initial census
4. Create first session log and checkpoint-000
5. Optionally sync knowledge from a previous project via `scripts/sync-knowledge.py`

## Rules Enforced by Structure

- No builds inside `src/` or `docs/`
- No long-lived findings (distill or archive)
- No free-form patch files — only XXX-phase-target naming
- README stays a pure front-door

When auditing an existing repo, check presence and health of the 6 canonical files first, then `.agent/continuity/`, then findings count.
