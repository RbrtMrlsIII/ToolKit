---
name: canonical-evolution-integrity
description: Protect canonical knowledge lineage while allowing explicitly authorized migration and retirement.
---

# Canonical Evolution Integrity

## Objective

Protect canonical knowledge from accidental or silent loss without freezing canonical documents forever.

## Classification

Every canonical structural change is classified as one of:

- PRESERVE: existing canonical content remains intact.
- MIGRATE: canonical content is intentionally replaced and has an authorized successor/target.
- RETIRE: canonical content is intentionally removed with an explicit authorized retirement reason.

## Hard invariants

1. Unexplained canonical loss remains fail-closed.
2. Intentional migration or retirement must declare the exact canonical source path and removed heading/section.
3. MIGRATE requires a successor/target and evidence of coverage.
4. RETIRE requires an explicit retirement reason and evidence.
5. Authority and scope must be declared in a machine-readable change record.
6. Historical evidence is never silently deleted.
7. The validator protects knowledge lineage, not permanent document shape.

## Relationship to canonical-integrity

`canonical-integrity.py` remains the fail-closed execution guard. This skill supplies the governed migration record that permits an authorized evolution while retaining structural protection.

## Verification

The same validator must reject an unexplained canonical heading deletion, accept a fully declared migration/retirement, reject missing successor/reason, and reject missing evidence or authority.
