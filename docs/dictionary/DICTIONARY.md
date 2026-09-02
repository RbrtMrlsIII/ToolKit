# Dictionary — Human Readable (Auto-Generated from dictionary.json)

Last Updated: 2026-08-31T18:41:38.666282
Last XXX: 000
Total Entities: 0
Total Terms: 5

## Terms (Machine Readable Dictionary)

| Term | Definition | File | XXX | Created At |
|------|------------|------|-----|------------|
| PRODUCT-KNOWLEDGE | Permanent distilled memory — Validated Patterns, Anti-Patterns, Gotchas, Quirks, Minimalism Log | PRODUCT-KNOWLEDGE.md | 000 | 2026-08-31T18:41:38.666292 |
| census | Universal inventory + cleanliness tool — counts tabs, UI, 3D before converting to 3D | scripts/census.py | 000 | 2026-08-31T18:41:38.666294 |
| registry | Machine-readable continuity | .agent/continuity/registry.json | 000 | 2026-08-31T18:41:38.666295 |
| session-log | Timestamped complete tracing | .agent/sessions/ | 000 | 2026-08-31T18:41:38.666297 |
| canonical-build | Canonical building skill and where to put builds | builds/ | 000 | 2026-08-31T18:41:38.666298 |

## Entities

### Tabs (0) — How many tabs do we have
| ID | Name | Path | File | XXX | Created At |
|----|------|------|------|-----|------------|
| - | - | - | - | - | - |

### UI Screens (0) — Before converting to 3D
| ID | Name | File | XXX | Created At |
|----|------|------|-----|------------|
| - | - | - | - | - |

### UI Components (0)
| ID | Name | File | XXX | Created At |
|----|------|------|-----|------------|
| - | - | - | - | - |

### 3D Models (0)
| ID | Name | File | Converted From | XXX | Created At |
|----|------|------|---------------|-----|------------|
| - | - | - | - | - | - |

### Backend Endpoints (0)
| ID | Method | Path | File | XXX | Created At |
|----|--------|------|------|-----|------------|
| - | - | - | - | - | - |

### Data Models (0)
| ID | Name | Table | File | XXX | Created At |
|----|------|-------|------|-----|------------|
| - | - | - | - | - | - |

## Relationships

| From | To | Type | Description |
|------|----|------|-------------|
| tabs | ui_screens | navigates_to | Tab navigates to UI screen |
| ui_screens | models_3d | converts_to | UI screen converts to 3D model |
| ui_screens | backend_endpoints | calls | UI screen calls backend endpoint |

## Stats

- Total Entities: 0
- Total Terms: 5
- Last Growth: Initial dictionary created with 5 terms

## How to Update

When project grows larger (new tab, UI screen, 3D model, endpoint, term), update `.agent/dictionary/dictionary.json` with timestamp, then run `python scripts/dictionary-generator.py` to regenerate this MD.
