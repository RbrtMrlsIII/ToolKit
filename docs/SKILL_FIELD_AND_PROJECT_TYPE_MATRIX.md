# Skill Field & Project-Type Matrix

**Purpose:** fast, deterministic skill loading across different project types and work domains.

Toolkit is project-agnostic. Skills are reusable operating capabilities, not product features. A consuming project selects skills by **field** and **project type**, then further constrains them by task, domain, provider/service/runtime, tools/plugins, permissions, and project policy.

## Field taxonomy

| Field | Covers | Examples of skills |
|---|---|---|
| Foundation / Governance | authority, scope, planning, safety, continuity | roots-definer, phase-planner, safety-reporter, canonical-build |
| Knowledge / Continuity | findings, anti-patterns, distillation, checkpoints | anti-pattern-checker, knowledge-distiller, checkpoint-creator |
| Engineering / Structure | repository hygiene, census, file update, dictionaries | census-runner, file-update-protocol, dictionary-manager |
| Backend | APIs, persistence, auth, server execution, jobs | backend-operations, relevant backend integration skills |
| 3rd-Party / Integrations | provider/vendor adapters and external systems | connector/provider-specific skills |
| Frontend / UI | interaction, responsive behavior, accessibility, browser QA | frontend-implementation |
| Domain / Spatial | project-domain modeling and spatial/3D work | spatial/domain-profile |
| Collaboration / Team | team coordination, leadership, repository handoff | team-coordination, repository-handoff, team-lead |
| Release / Operations | deployment, monitoring, compatibility, recovery | release/ops skills as added |

## Project-type profiles

Minimum profile classes:

- **WEB** — browser application, web APIs, frontend/backend boundary, browser verification.
- **MOBILE** — mobile UI, device lifecycle, platform permissions, mobile release checks.
- **BACKEND** — server/API/data/queues/auth/runtime without assuming a specific UI.
- **3D / SPATIAL** — geometry, scene/state, spatial interaction, rendering and asset handling.
- **GAME** — gameplay/runtime state, content pipeline, input, performance, release.
- **GENERIC / MIXED** — project that does not fit one dominant profile; load only the fields required by the current task.

A project may activate multiple profiles, but the current task must still identify its primary field.

## Resolution order

```text
Project type profile
  + primary field
  + task/domain
  + provider/service/runtime
  + tools/plugins
  + project-specific guidance
  + policy/permission constraints
  = effective skill set
```

Skills never grant authorization. Project permissions and backend policy remain authoritative.

## Fast-switch rule

At session start, a consuming agent should identify:

1. project type profile;
2. current field;
3. current phase/XXX;
4. task/domain;
5. required provider/service/runtime skills.

Then load the smallest sufficient skill bundle. Do not load every skill merely because it exists.

## Universal vs project-specific

Toolkit skills must remain reusable across projects. A TeamAi-only product rule, provider decision, UI convention, or backend architecture must stay in TeamAi unless generalized, validated, and intentionally promoted upstream.

## Canonical anti-pattern learned from project work

A technology can be labeled `legacy` and still be dangerous when the repository structure makes its implementation path easy to rediscover. Retirement therefore requires structural exclusion from active implementation paths, not documentation labels alone.
