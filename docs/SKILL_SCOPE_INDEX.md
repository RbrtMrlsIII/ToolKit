# Skill Scope Index — Universal AGENT Toolkit

**Purpose:** deterministic fast-switching across project types, fields, phases, tasks, runtimes, tools, and scale. This index classifies skills; each skill's `SKILL.md` remains its behavioral authority.

## Scope classes

`UNIVERSAL` = reusable across projects and fields.

`ADAPTABLE` = universal mechanism with project/field/runtime parameters.

`CONSUMER-SPECIFIC` = belongs in the consuming project, not Toolkit core.

A skill does not grant authorization.

## Project-type codes

`WEB` browser/web application · `MOBILE` mobile application · `BACKEND` server/data/runtime · `3D` spatial/3D · `GAME` game/runtime · `GENERIC` any project type.

## Skill field/type matrix

| Skill | Primary field | Scope | Project types | Fast-switch role |
|---|---|---|---|---|
| scale-adapter | Foundation | UNIVERSAL | ALL | choose project scale and constraints |
| roots-definer | Foundation | UNIVERSAL | ALL | establish/validate root architecture before planning |
| phase-planner | Planning | UNIVERSAL | ALL | plant/branch the next approved XXX |
| safety-reporter | Safety | UNIVERSAL | ALL | gate high-impact/destructive work |
| observe | Core execution | UNIVERSAL | ALL | inspect current reality |
| record | Core execution | UNIVERSAL | ALL | preserve evidence/findings |
| understand | Core execution | UNIVERSAL | ALL | establish meaning/relationships |
| classify | Core execution | UNIVERSAL | ALL | classify status/impact |
| align | Core execution | UNIVERSAL | ALL | align authority and implementation |
| validate | Verification | UNIVERSAL | ALL | execute verification |
| endorse | Governance | UNIVERSAL | ALL | close approval gate |
| advance | Governance | UNIVERSAL | ALL | advance checkpoint and continuity |
| anti-pattern-checker | Knowledge | UNIVERSAL | ALL | prevent known failure repetition |
| knowledge-distiller | Knowledge | UNIVERSAL | ALL | generalize validated lessons upstream |
| minimalism-enforcer | Knowledge | UNIVERSAL | ALL | prevent unnecessary growth/noise |
| checkpoint-creator | Continuity | UNIVERSAL | ALL | preserve durable stopping point |
| census-runner | Governance/Structure | UNIVERSAL | ALL | inventory/cleanliness/enforcement |
| reconciliation-manager | Reconciliation | UNIVERSAL | ALL | resolve state/registry/document drift |
| investigation-manager | Investigation | UNIVERSAL | ALL | contain uncertainty/discrepancy |
| contract-manager | Contracts | UNIVERSAL | ALL | maintain source-of-truth contracts |
| session-logger | Continuity | UNIVERSAL | ALL | start/close durable session evidence |
| file-update-protocol | Structure/Continuity | UNIVERSAL | ALL | keep related-document chain synchronized |
| canonical-integrity | Governance/Validation | UNIVERSAL | ALL | protect canonical sections from unexplained loss |
| canonical-build | Engineering | UNIVERSAL | ALL | construct canonical deliverables |
| dictionary-manager | Structure/Knowledge | UNIVERSAL | ALL | maintain machine/human entity dictionary |
| target-project-handover | Continuity/Handover | UNIVERSAL | ALL | preserve downstream handover boundary |
| agent-orucavea | High-level execution | UNIVERSAL | ALL | condensed O-R-U-C-A-V-E-A guidance |
| agent-knowledge | High-level knowledge | UNIVERSAL | ALL | condensed knowledge guidance |
| agent-continuity | High-level continuity | UNIVERSAL | ALL | condensed continuity guidance |
| agent-census | High-level governance | UNIVERSAL | ALL | condensed census guidance |
| agent-structure | High-level structure | UNIVERSAL | ALL | condensed structure guidance |

## Dynamic extension rule

Field-specific or provider-specific skills may be added only when their scope is explicit and the dependency boundary is recorded. Every skill extension declares:

- scope class;
- field;
- supported project types;
- task/domain scope;
- current phase/XXX relevance;
- dependencies/prerequisites;
- instructional / validation / governance / integration-facing role;
- provider/service/runtime constraints when applicable;
- authorization boundary;
- verification method.

## Baseline-driven skill growth

Every validated baseline freeze triggers a skill-coverage review. The question is not “how many skills should exist?” but “what repeatable execution is now stable enough to deserve reusable equipment?”

```text
baseline freeze
→ repeatable procedure
→ reuse current skill OR candidate skill/extension/validator
→ define scope/dependencies/verification
→ validate + endorse
→ add to index
```

Skills are living infrastructure. Their count may increase as execution baselines accumulate. Skill proliferation without reusable evidence is a governance smell.

## Resolution rule

```text
project type
  + field
  + current phase/XXX
  + task/domain
  + provider/service/runtime
  + tools/plugins
  + project guidance
  + permissions/policy
  + current skill coverage
  = effective skill set
```

**Load the smallest sufficient bundle.** A skill never grants authorization.

## Upstream-only knowledge rule

Project findings are not copied into Toolkit verbatim. Only validated and generalized lessons become Toolkit skills, patterns, anti-patterns, validators, or safety rules. Toolkit changes do not automatically flow back into a consuming project.
