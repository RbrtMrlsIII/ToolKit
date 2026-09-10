# WebAi Seat Foundation

## Purpose

Universal AGENT ToolKit is the reusable operating foundation from which WebAi seats can be equipped. It is not a TeamAi-specific product implementation and it is not merely a collection of skills.

## Responsibility Unit first

ToolKit defines work by responsibility rather than by Agent identity.

```text
Responsibility Unit
= objective
+ scope
+ required knowledge
+ required skills
+ authority boundary
+ inputs
+ dependencies
+ outputs
+ verification
+ handover
```

A **Seat** is a configurable responsibility boundary:

```text
Seat
= responsibility units
+ workspace governance
+ project adaptation
+ applicable skill bundle
+ execution capacity
```

An **Agent** is a currently assigned worker for one or more responsibility units.

This means the skill library does not need to be copied or multiplied when Agent count changes.

## Seat equipment

ToolKit supplies reusable:

- skills and skill-resolution rules;
- workspace governance, continuity, validation, reconciliation, and knowledge discipline;
- project/field adaptation and scale adaptation;
- responsibility allocation patterns;
- rules for distinguishing reusable lessons from project-specific knowledge.

A seat loads the smallest sufficient skill bundle for its current project, phase, task, runtime, tools, and capacity. Skills instruct; Product Law, policy, permissions, and project authorization determine whether action is allowed.

## User-first operating chain

```text
user command / vision
  ↓
consult Agents
  ↓
user approval for material direction
  ↓
PRODUCT_LAW.md
  ↓
MASTERPLAN.md slice / checklist
  ↓
skills + PRODUCT-KNOWLEDGE.md
  ↓
O-R-U-C-A-V-E-A
  ↓
action
  ↓
validation + evidence
  ↓
complete log / checkpoint / handover
  ↓
endorsement
  ↓
PRODUCT-KNOWLEDGE.md growth
```

Agents can analyze and recommend before approval. They do not convert their recommendation into authority.

## Two-axis growth

ToolKit grows in two dimensions:

1. **Technical growth:** reusable skills, adapters, tools, supported project/field types, and integration mechanisms.
2. **Operational growth:** stronger authority resolution, canonical integrity, evidence discipline, anti-pattern detection, knowledge promotion, responsibility allocation, recovery, and scale adaptation.

The goal is disciplined capability, not capability growth alone.

## Baseline freeze → skill growth

A validated execution baseline or frozen slice is a signal to inspect skill coverage:

```text
baseline freeze
      ↓
repeatable procedure identified
      ↓
existing skill sufficient?
   ┌──┴──┐
  yes   no
   │     │
 reuse  candidate skill / extension / validator
          ↓
   scope + dependencies + verification
          ↓
       endorsement
          ↓
  future slice execution
```

Skills are living infrastructure. As more execution baselines become stable, the skill system may grow. Skills may also be split, refined, deprecated, or retired. Skill growth must never create implicit authorization or duplicate consumer-specific product law.

## Agent-count scaling

Agent count is a resource-allocation variable.

**2 Agents:** broader Responsibility Units may be combined per Agent, with integration and verification responsibility still explicit.

**3–4 Agents:** responsibilities can be separated into major specialist and integration roles.

**5–8 Agents:** responsibilities can be partitioned into discovery, planning, research, design, implementation, verification, operations, and review/coordination where the project's authority model supports it.

The same universal skills should remain reusable across all sizes. More Agents mean more parallel responsibility allocation, not eight copies of the skill system.

## Scope-aware skill bundle

```text
project type
+ field
+ current slice / XXX
+ task/domain
+ provider/runtime
+ tools/plugins
+ project guidance
+ permissions/policy
= effective skill set
```

Load the smallest sufficient bundle. A skill never grants authorization.

## Consuming-project boundary

Consuming projects retain authority over their own Product Law, domain rules, provider choices, implementation details, credentials, authorization, and user-facing product semantics. ToolKit knowledge never changes a consuming project automatically.

## Upstream learning loop

```text
ToolKit mechanism
  → consuming project / WebAi seat
  → real execution + evidence
  → validated finding
  → generalization review
  ├─ reusable → Toolkit candidate
  └─ specific → remains consumer knowledge
  → endorsement
  → Toolkit evolution
```

Only validated and generalized lessons move upstream.
