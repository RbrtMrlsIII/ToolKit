# SKILL: Dictionary Manager — Machine Readable Dictionary for Large Projects

> Universal skill — machine readable dictionary once project grew larger. Tracks tabs, UI, 3D, endpoints, terms.

### Metadata
- ID: dictionary-manager
- Phase: Dictionary (when project grows larger, after Align, before Advance)
- Type: knowledge
- Applies To: All projects, especially large projects with many tabs, UI, 3D, endpoints

### When To Use
- When project grows larger: many tabs, UI screens, components, 3D models, endpoints, tables
- When new tab, UI screen, component, 3D model, endpoint, table, term added
- When census inventory count != dictionary count → need update
- During file update protocol (when changing something that adds entity)

### Prerequisites
- POLICY.md section 10 (Machine Readable Dictionary)
- .agent/dictionary/dictionary.json exists
- Census inventory available

### Steps

1. **Read Current Dictionary:**
   - `.agent/dictionary/dictionary.json` — version, last_updated, last_xxx, entities {tabs, ui_screens, ui_components, models_3d, backend_endpoints, data_models, terms}, relationships, stats

2. **Read Census Inventory:**
   - `.agent/census/census-*.json` or `docs/census/inventory-*.json` — tabs count, ui_screens count, etc.

3. **Compare Counts:**
   - If inventory tabs count != dictionary.entities.tabs.count → need update
   - If inventory ui_screens count != dictionary.entities.ui_screens.count → need update
   - etc.

4. **Update Dictionary JSON with Timestamp:**
   - For each new entity:
     - tabs: {id, name, path, file, xxx, created_at: timestamp ISO 8601, updated_at}
     - ui_screens: {id, name, file, xxx, created_at}
     - ui_components: {id, name, file, xxx, created_at}
     - models_3d: {id, name, file, path, xxx, created_at, converted_from}
     - backend_endpoints: {id, method, path, file, xxx, created_at}
     - data_models: {id, name, table, file, xxx, created_at}
     - terms: {definition, file, xxx, created_at}
   - Update last_updated: now timestamp
   - Update last_xxx: current XXX
   - Update stats: total_entities = sum of all entity counts, total_terms, last_growth description

5. **Update Relationships:**
   - tabs → ui_screens: navigates_to
   - ui_screens → models_3d: converts_to
   - ui_screens → backend_endpoints: calls
   - etc.

6. **Save History:**
   - `.agent/dictionary/history/dict-YYYY-MM-DD-HHMMSS.json` — snapshot of dictionary before change with timestamp, XXX, agent_id, changes

7. **Generate Human-Readable DICTIONARY.md:**
   - Run `python scripts/dictionary-generator.py` or manually generate `docs/dictionary/DICTIONARY.md` from JSON
   - Contains tables: Tabs, UI Screens, Components, 3D Models, Endpoints, Data Models, Terms, Relationships, Stats

8. **Census Counts Dictionary:**
   - Census now counts dictionary entries: total_entities, total_terms
   - If inventory != dictionary → census WARN

### Output Template

Machine: .agent/dictionary/dictionary.json
```json
{
  "version": "1.0.0",
  "last_updated": "2026-09-01T10:45:00+08:00",
  "last_xxx": "006",
  "entities": {
    "tabs": {"description": "UI tabs", "count": 5, "items": [{"id": "tab-home", "name": "Home", "path": "/home", "file": "src/navigation/tabs.ts", "xxx": "002", "created_at": "2026-09-01T10:00:00+08:00"}]},
    "ui_screens": {"count": 12, "items": [...]},
    "terms": {"PRODUCT-KNOWLEDGE": {"definition": "Permanent brain", "file": "PRODUCT-KNOWLEDGE.md", "xxx": "000", "created_at": "..."}}
  },
  "relationships": [{"from": "tabs", "to": "ui_screens", "type": "navigates_to"}],
  "stats": {"total_entities": 45, "total_terms": 20, "last_growth": "Added 3 tabs, 2 UI screens in XXX 006"}
}
```

Human: docs/dictionary/DICTIONARY.md
```markdown
# Dictionary — Human Readable

Last Updated: 2026-09-01T10:45:00+08:00
Last XXX: 006
Total Entities: 45
Total Terms: 20

## Tabs (5)
| ID | Name | Path | File | XXX | Created At |
|----|------|------|------|-----|------------|
| tab-home | Home | /home | src/navigation/tabs.ts | 002 | 2026-09-01T10:00:00+08:00 |

## UI Screens (12)
...
```

### Validation Checklist
- [ ] dictionary.json exists, has version, last_updated timestamp ISO 8601, last_xxx
- [ ] entities counts match census inventory counts (tabs, ui_screens, etc.) or WARN if not
- [ ] New entities have id, name, file, xxx, created_at timestamp
- [ ] Terms have definition, file, xxx, created_at
- [ ] Relationships updated
- [ ] Stats updated: total_entities, total_terms, last_growth
- [ ] History snapshot saved in .agent/dictionary/history/dict-YYYY-MM-DD-HHMMSS.json with timestamp, XXX, agent_id, changes
- [ ] Human DICTIONARY.md generated from JSON
- [ ] Census counts dictionary entries

### Anti-Patterns
- Project grew larger (>20 entities) but no dictionary → census FAIL
- Inventory count != dictionary count → WARN, need update
- No timestamp in dictionary → invalid
- Only human DICTIONARY.md, no machine JSON → invalid, need machine-readable

### Distillation
Validated Pattern: "Machine-readable dictionary.json with timestamp + human DICTIONARY.md auto-generated ensures scalability when project grew larger"
