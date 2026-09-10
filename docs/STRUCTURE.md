# STRUCTURE.md — Repo-Wide Canonical Wiring & Descriptions

> Single map of every important folder and file in the Universal AGENT Toolkit. Machine + human readable. Update this when the structure itself changes.

---

## 1. Root — Governance Layer (Canonical)

| Path | Type | Description |
|---|---|---|
| `README.md` | Canonical | Front-door only. Pure wiring + status. < 80 lines. |
| `PRODUCT_LAW.md` | Canonical | User-approved product meaning, invariants, and authority boundaries. |
| `AI_ASSISTANT_READ_ME.md` | Canonical | Agent Operating System. Reading order, gates, constraints. |
| `MASTERPLAN.md` | Canonical | Conceptual map + only source of XXX numbers + current focus. |
| `POLICY.md` | Canonical | Constitution, execution rules, change protocol, enforcement. |
| `PRODUCT-KNOWLEDGE.md` | Canonical | Permanent distilled brain and conceptual relationship map. |
| `ENDORSEMENT.md` | Canonical | Approval ledger. Drafts vs Approved. Knowledge proof required. |
| `skills-loader.mjs` | Tool | Loads the correct skill for the current XXX / phase. |

## 2. `.agent/` — Machine-Readable State (when instantiated in a consuming project)

| Path | Description |
|---|---|
| `.agent/continuity/registry.json` | Machine source of truth for current XXX, todo, completed, knowledge_index. |
| `.agent/continuity/state.json` | Last good state, active findings count, status. |
| `.agent/continuity/checkpoint-XXX.md` | Per-XXX checkpoint. |
| `.agent/sessions/*.json` | Timestamped session logs. |
| `.agent/dictionary/dictionary.json` | Machine dictionary of entities. |
| `.agent/builds/builds.json` | Machine registry of builds. |
| `.agent/census/census.config.json` | Config for universal census inventory. |

Toolkit contains templates and resolver support for this state; consuming projects instantiate their own runtime state.

## 3. `docs/` — Human-Readable Working + Permanent Knowledge

| Path | Description |
|---|---|
| `docs/findings/` | Transient working memory. Max 10 active files. |
| `docs/handover/` | Handover notes per XXX. |
| `docs/sessions/` | Human-readable session logs. |
| `docs/archive/` | Distilled findings after endorsement. |
| `docs/knowledge-archive/` | Compressed old knowledge. |
| `docs/contracts/` | Source-of-Truth contracts and interfaces. |
| `docs/dependencies/` | Dependency map. |
| `docs/investigation/` | Blocked approaches and discrepancies. |
| `docs/reconciliation/` | State/document/knowledge reconciliation. |
| `docs/census/` | Census reports and inventory. |
| `docs/dictionary/DICTIONARY.md` | Human view of machine dictionary. |
| `docs/architecture-map.md` | Authority → consumers architecture map. |
| `docs/TOOLKIT_ARCHITECTURE.md` | Universal architecture, scope boundaries, responsibility and growth model. |
| `docs/CHANGE_CONTRACT.md` | Meaningful-change declaration and preservation contract. |
| `docs/WEB_AI_SEAT_FOUNDATION.md` | Responsibility Unit, Seat, Agent, scale and skill-growth model. |
| `docs/USER_MANUAL_DEPLOYMENT.md` | Single generic human deployment/adoption guide. |
| `docs/KNOWLEDGE_UPSTREAM_BOUNDARY.md` | Consumer → Toolkit promotion boundary. |
| `docs/STRUCTURE.md` | This file — repo-wide wiring. |
| `docs/history/` | Historical discussion and generalized learning cases. |

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

**Governance & integrity**
`census-runner`, `reconciliation-manager`, `investigation-manager`, `contract-manager`, `canonical-integrity`

**Continuity & structure**
`session-logger`, `file-update-protocol`, `canonical-build`, `dictionary-manager`, `target-project-handover`

See `skills/SKILLS_INDEX.md` and `docs/SKILL_SCOPE_INDEX.md` for scope and load order.

## 5. `scripts/` — Executable Tools

| Script | Purpose |
|---|---|
| `census.py` | Universal inventory and cleanliness checks |
| `knowledge-search.py` | Search PRODUCT-KNOWLEDGE and anti-pattern score |
| `new-xxx.py` | Scaffold next finding correctly |
| `auto-distill.py` | Help distill findings |
| `dictionary-generator.py` | Regenerate DICTIONARY.md |
| `architecture-map-generator.py` | Regenerate architecture map |
| `sync-knowledge.py` | Promote validated/generalized knowledge from another project |
| `sync-cloud.py` | Optional knowledge transport |
| `canonical-integrity.py` | Fail-closed structural check for canonical document changes |
| `pre-commit` | Hook for governance checks |
| `skills-loader.mjs` | Auto-load current phase skill |

## 6. `builds/` — Only Allowed Place for Build Outputs

```text
builds/
├── latest/
├── XXX-phase-target/
└── archive/
```

Never put builds inside product source or knowledge documents.

## 7. Project-Development Layer

In a consuming project, `src/` or its declared equivalent (`app/`, `lib/`, `packages/`) contains product code and product tests only.

No findings, knowledge, session logs, canonical rules, or build outputs belong there.

## 8. Optional Modules

| Path | Description |
|---|---|
| `backend-integrations-repo/` | Reusable integration recipes. |
| `test-files-repo/` | Fast validation scripts and test fixtures. |
| `prompts/` | Mobile-ready prompts per phase. |
| `validation/evidence/` | Per-XXX validation evidence. |

## 9. Authority and Learning Boundary

```text
USER / PROJECT OWNER INTENT
        ↓
PRODUCT_LAW.md
        ↓
POLICY.md
        ↓
MASTERPLAN.md
        ↓
skills + PRODUCT-KNOWLEDGE
        ↓
execution / verification / evidence
        ↓
endorsement
        ↓
knowledge evolution
```

Toolkit remains universal. A consuming project retains product/domain/provider/credential/authorization ownership. Only validated and generalized lessons move upstream.

## 10. Quick Mental Model

```text
Governance
  Product Law + Policy + Masterplan + Knowledge + Endorsement
  .agent/ + docs/ + skills/ + scripts/ + validation/ + builds/
       ↓
Responsibility Units → Seats → assigned Agents
       ↓
Consuming project
```

Keep authority boundaries, knowledge state, and structural integrity explicit.
