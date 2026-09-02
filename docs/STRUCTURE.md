# STRUCTURE.md — Repo-Wide Canonical Wiring & Descriptions

> Single map of every important folder and file in the Universal AGENT Toolkit.  
> Machine + human readable. Update this when the structure itself changes.

---

## 1. Root — Governance Layer (Canonical)

| Path | Type | Description |
|------|------|-------------|
| `README.md` | Canonical | Front-door only. Pure wiring + status. < 80 lines. |
| `AI_ASSISTANT_READ_ME.md` | Canonical | Agent Operating System. Mandatory reading order, gates, constraints. |
| `MASTERPLAN.md` | Canonical | Conceptual map + **only** source of XXX numbers + current focus. |
| `POLICY.md` | Canonical | Constitution. Source-of-Truth, Layer Separation, rules, enforcement. |
| `PRODUCT-KNOWLEDGE.md` | Canonical | Permanent brain. Validated Patterns + Anti-Patterns (most important). |
| `ENDORSEMENT.md` | Canonical | Approval ledger. Drafts vs Approved. Knowledge proof required. |
| `skills-loader.mjs` | Tool | Loads the correct skill for the current XXX / phase. |

---

## 2. `.agent/` — Machine-Readable State (always tracked)

| Path | Description |
|------|-------------|
| `.agent/continuity/registry.json` | Machine source of truth for current XXX, todo, completed, knowledge_index. |
| `.agent/continuity/state.json` | Last good state, active findings count, status. |
| `.agent/continuity/checkpoint-XXX.md` | Per-XXX checkpoint (human + machine readable). |
| `.agent/sessions/*.json` | Timestamped session logs (must start at beginning of session). |
| `.agent/dictionary/dictionary.json` | Machine dictionary of entities (tabs, screens, 3D, endpoints, terms…). |
| `.agent/builds/builds.json` | Machine registry of builds. |
| `.agent/census/census.config.json` | Config for the universal census inventory tool. |

---

## 3. `docs/` — Human-Readable Working + Permanent Knowledge

| Path | Description |
|------|-------------|
| `docs/findings/` | **Transient** working memory. Max 10 active files. Lifetime = one XXX. |
| `docs/handover/` | Handover notes per XXX (for next agent / human). |
| `docs/sessions/` | Human-readable session logs (pair with `.agent/sessions/`). |
| `docs/archive/` | Distilled findings after endorsement. |
| `docs/knowledge-archive/` | Compressed old knowledge (after 2 checkpoints). |
| `docs/contracts/` | Source-of-Truth contracts and interfaces. |
| `docs/dependencies/` | Dependency map. |
| `docs/investigation/` | Blocked approaches, discrepancies, anti-pattern hits. |
| `docs/reconciliation/` | When state ≠ registry or knowledge conflicts. |
| `docs/census/` | Census reports, inventory, dashboard. |
| `docs/dictionary/DICTIONARY.md` | Human view of the machine dictionary. |
| `docs/architecture-map.md` | Visual / textual map of authority → consumers. |
| `docs/STRUCTURE.md` | **This file** — repo-wide wiring. |
| `docs/history/` | Historical discussion / evolution notes. |

---

## 4. `skills/` — Loadable Agent Skills

Each skill lives at `skills/<id>/SKILL.md`.

**Scale & Adaptation**  
`scale-adapter`

**Upstream Definition**  
`roots-definer`

**Planning & Safety**  
`phase-planner`, `safety-reporter`

**Core execution (O-R-U-C-A-V-E-A)**  
`observe`, `record`, `understand`, `classify`, `align`, `validate`, `endorse`, `advance`

**Knowledge & minimalism**  
`anti-pattern-checker`, `knowledge-distiller`, `minimalism-enforcer`, `checkpoint-creator`

**Governance**  
`census-runner`, `reconciliation-manager`, `investigation-manager`, `contract-manager`

**Continuity & structure**  
`session-logger`, `file-update-protocol`, `canonical-build`, `dictionary-manager`

See `skills/SKILLS_INDEX.md` for load order.

---

## 5. `scripts/` — Executable Tools

| Script | Purpose |
|--------|---------|
| `census.py` | Universal inventory (tabs, UI, 3D…) + cleanliness checks |
| `knowledge-search.py` | Search PRODUCT-KNOWLEDGE + anti-pattern score |
| `new-xxx.py` | Scaffold next finding correctly |
| `auto-distill.py` | Help distill findings |
| `dictionary-generator.py` | Regenerate DICTIONARY.md from JSON |
| `architecture-map-generator.py` | Regenerate architecture map |
| `sync-knowledge.py` | Copy patterns from another project |
| `sync-cloud.py` | Push/pull knowledge to cloud backend |
| `pre-commit` | Hook that enforces minimalism / census rules |
| `skills-loader.mjs` | Auto-load current phase skill |

---

## 6. `builds/` — Only Allowed Place for Build Outputs

```
builds/
├── latest/                 ← points to latest successful build
├── XXX-phase-target/       ← per-XXX builds (web/, mobile/, backend/, 3d/, artifacts/)
└── archive/                ← compressed after 2 checkpoints
```

Never put builds inside `src/` or `docs/`.

---

## 7. `src/` — Project-Development Layer (Product Code Only)

**This is where the actual product lives.**

- Backend, frontend, domain logic, UI components, etc.
- No findings, no knowledge, no session logs, no canonical rules.
- No build outputs.

(Currently empty — toolkit baseline has no product code yet.)

---

## 8. Optional Modules

| Path | Description |
|------|-------------|
| `backend-integrations-repo/` | Ready-to-copy integrations (Supabase, Firebase, Stripe, PayPal, auth, storage, etc.) |
| `test-files-repo/` | Fast validation scripts (py, mjs, sh) |
| `prompts/` | Mobile-ready paste prompts per phase |
| `validation/evidence/` | Per-XXX validation evidence |

---

## 9. Hierarchy of Authority (Reminder)

1. Source-of-Truth (POLICY.md §1)
2. POLICY.md
3. PRODUCT-KNOWLEDGE.md (especially Anti-Patterns)
4. MASTERPLAN.md + endorsed contracts
5. Current checkpoint + registry
6. Everything else

---

## 10. Quick Mental Model

```
Governance Layer          Project-Development Layer
─────────────────         ─────────────────────────
6 Canonical Files         src/   ← product code only
.agent/ (machine)
docs/   (human knowledge)
skills/ + scripts/
builds/ (outputs only)
```

Keep the wall between the two layers clean.
