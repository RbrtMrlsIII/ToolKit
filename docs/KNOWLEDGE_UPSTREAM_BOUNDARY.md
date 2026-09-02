# Knowledge Upstream Boundary

**Status:** Canonical Toolkit policy addendum.

## Direction

```text
Project using Toolkit
      │
      │ validated + generalized lesson only
      ▼
   Universal Toolkit
```

There is **no automatic downstream flow** from Toolkit into an existing project after the project has established its own canonical authority.

## What may move upstream

Only a lesson that is:

- observed in a real project;
- recorded with evidence;
- validated against the project's tests/behavior;
- generalized so it applies beyond one product;
- stripped of product-specific identifiers, secrets, pricing, architecture commitments, and UI assumptions;
- reviewed as a reusable skill, anti-pattern, pattern, or safety rule.

## What must stay in the project

Project laws, product requirements, provider selections, payment rules, user experience decisions, domain schemas, project-specific architecture, credentials, and implementation details remain downstream/project-owned.

## No downstream overwrite

A Toolkit template or integration recipe must never override a consuming project's canonical backend, security, provider, or data-ownership decision merely because the recipe already exists.

Before using a reusable integration, the consuming project must reconcile it against its own authority and current field/project-type profile.

## Learning loop

```text
Project mistake/finding
      ↓
validated evidence
      ↓
project knowledge
      ↓
generalization review
      ↓
Toolkit skill/pattern/anti-pattern
      ↓
future projects only
```

## Permanent lesson

A technology can be correctly labeled `legacy` yet remain dangerous if repository structure still makes it discoverable as the easiest implementation path. Safe retirement therefore requires structural barriers and explicit re-entry gates, not labels alone.
