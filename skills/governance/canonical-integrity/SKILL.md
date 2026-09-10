---
name: canonical-integrity
description: Protect canonical knowledge structures from unexplained deletion or section loss. Use before merge or release when canonical documents change.
scope: UNIVERSAL
project_types: ALL
phase: governance / validation
authorization: none
---

# Canonical Integrity Skill

## Authority
`PRODUCT_LAW.md` defines product meaning. `POLICY.md` defines governance discipline. This skill only verifies structural integrity and never grants permission.

## Use when

- a canonical document changes;
- a Masterplan or policy section is edited;
- a knowledge index is synchronized;
- a release/merge includes governance-layer changes.

## Required checks

1. Identify the declared semantic change scope.
2. Compare the target canonical file against the base revision.
3. Verify that unrelated headings still exist.
4. Detect unexplained deleted blocks or suspiciously large deletions.
5. Check historical files for deletion or relocation without explicit archival authority.
6. Record intentional structural changes in the change contract.
7. Fail closed when canonical section loss is unexplained.

## Result classes

`PASS` = changes remain inside declared scope and no protected structure was lost.

`BLOCKED` = unexplained section loss, historical deletion, or structural drift requires investigation or explicit authorization.

## Principle

Presence of a requested new claim is not proof of document integrity. The validator must prove both addition/change correctness and preservation of unrelated canonical structure.

## Related

- `docs/CHANGE_CONTRACT.md`
- `docs/TOOLKIT_ARCHITECTURE.md`
- `scripts/canonical-integrity.py`
