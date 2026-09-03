---
name: target-project-handover
description: Universal rule for mandatory target-project handover after every completed gate. ToolKit itself never hands over a consuming project.
---

# Target-Project Handover

A completed gate in a consuming project is not complete until the target project surrenders a handover package.

## Hard rule
After each completed gate, the target project MUST produce a handover package/ZIP containing the current canonical state needed by a continuation agent. The package scope may be a complete project snapshot or a precisely declared gate packet when a full snapshot is not available.

## Minimum packet
Include, as applicable:
- current Product Law / Masterplan / Agent Read Me;
- current machine continuity state;
- gate finding and validation evidence;
- checkpoint and handover record;
- relevant source/configuration files;
- explicit blockers, open gates, and next action;
- manifest identifying source revision and packet scope.

## Boundary
ToolKit provides the rule/skill only. It MUST NOT be treated as the handover owner and MUST NOT move project-specific files or decisions upstream as a handover.

## Completion test
No Advance claim for a consuming project gate is complete without the target-project handover artifact, plus the other required evidences.
