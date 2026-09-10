---
name: dynamic-skill-resolution
description: Resolve the smallest sufficient reusable skill bundle from project, task, runtime, governance, and capacity context without granting authorization.
---

# Dynamic Skill Resolution + Scale Adaptation

## Contract

Resolve skills from the full execution context:

```text
project type + field + phase/XXX + task/domain
+ provider/service/runtime + tools/plugins
+ project guidance + permissions/policy
+ capacity
= effective skill set
```

The resolver is deterministic and auditable. Capacity and Agent count may change allocation profile, but never change skill meaning, Product Law, policy, or authorization.

## Rules

1. Prefer the smallest sufficient bundle.
2. A missing or contradictory authorization context never becomes permission through skill resolution.
3. Skill metadata describes applicability, not authority.
4. Agent count changes allocation profile only.
5. Consumer-specific rules remain outside universal skill authority.
6. Unknown context must be represented explicitly rather than guessed.

## Scale profiles

- 2 Agents: broad discovery/planning and implementation/verification units.
- 4 Agents: split specialist/integration responsibilities where justified.
- 8 Agents: partition discovery, planning, research, design, implementation, verification, operations, and review/coordination.

Scaling must not duplicate the underlying skill library.

## Verification

For the same execution context, resolving at 2, 4, and 8 Agents must return the same skill identifiers and only vary allocation metadata.
