# QUICKSTART.md — Universal AGENT Toolkit

> Short, exact guide for humans and machines.  
> Read this first when exploring or starting a project.

---

## 1. What This Toolkit Is

A reusable **agent operating system** for any software project.  
It enforces continuity, prevents repeated mistakes, keeps files minimal, and gives clear structure so any AI (or human) can continue work without losing context.

**Core idea:**  
Minimal active files + increasing permanent knowledge + strict execution discipline.

---

## 2. Two Layers (Never Mix Them)

| Layer | Location | Contains |
|-------|----------|----------|
| **Governance** | Root + `.agent/` + `docs/` + `skills/` + `scripts/` | Rules, knowledge, plans, skills, status |
| **Project-Development** | `src/` only | Real product code |

`src/` = product code only.  
Everything else is governance.

---

## 3. The 6 Canonical Files (Root)

| File | Purpose |
|------|---------|
| `README.md` | Front-door. Wiring + status only. |
| `AI_ASSISTANT_READ_ME.md` | Agent Operating System (reading order + rules). |
| `MASTERPLAN.md` | Expandable plan by Field + XXX checklist. |
| `POLICY.md` | Constitution + Source-of-Truth + Layer Separation. |
| `PRODUCT-KNOWLEDGE.md` | Permanent brain (Validated Patterns + Anti-Patterns). |
| `ENDORSEMENT.md` | Approval ledger. |

---

## 4. How to Start a New Project

```bash
# From the toolkit directory
python scripts/new-project.py my-project-name

# Optional extras
python scripts/new-project.py my-project-name --with-integrations --with-tests

cd my-project-name
python scripts/status.py          # see health
```

Then decide:

1. **Brand-new product?** → Use `roots-definer` skill first.
2. **Roots already exist?** → Use `phase-planner` skill.

---

## 5. What Type of Project Should We Use?

The toolkit is **stack-agnostic**. Use it for any of these:

| Project Type | How the Toolkit Helps |
|--------------|-----------------------|
| **Web App** (React, Next, Vue, etc.) | Tracks UI screens, components, routes. Census counts tabs & screens before 3D conversion. Clear Frontend field in MASTERPLAN. |
| **Mobile App** (React Native, Flutter, Expo) | Same as web + mobile build locations in `builds/`. Continuity across devices. |
| **Backend / API** | Strong contract support (`docs/contracts/`), endpoint tracking, data model in roots + dictionary. |
| **Full-stack** | Separate Backend / Frontend / 3rd-Party fields in MASTERPLAN. Layer Separation keeps code clean. |
| **3D / Game / Creative** | Census tracks 3D models (glb, gltf, etc.) and conversion progress from UI → 3D. |
| **Internal Tool / Script Collection** | Still benefits from knowledge anti-patterns, session logging, and status command. |
| **Multi-agent / Long-running AI projects** | This is the original strength — continuity, anti-repeat, endorsement, and file-update protocol. |

**Recommendation:**  
Start with whatever your actual product is. The toolkit adapts. Do not force a type — just declare the Fields you need in MASTERPLAN.

---

## 6. Essential Commands

```bash
python scripts/status.py                    # Project health (start here)
python scripts/census.py --base . --write   # Inventory + cleanliness
python scripts/new-project.py <name>        # Scaffold new project
python scripts/knowledge-search.py "query"  # Search anti-patterns & patterns
```

---

## 7. Recommended Skill Order

1. `roots-definer`     → define or validate the root
2. `phase-planner`     → propose → approve → plant on MASTERPLAN
3. `safety-reporter`   → before high-impact changes
4. O-R-U-C-A-V-E-A     → execute with discipline
5. `status.py` + census → check health often

Full list: `skills/SKILLS_INDEX.md`

---

## 8. Key Folders (Quick Map)

```
.agent/          → machine state (registry, sessions, dictionary)
docs/            → findings, contracts, handover, STRUCTURE.md
skills/          → loadable skills
scripts/         → status, census, new-project, etc.
builds/          → only place for build outputs
src/             → product code only
```

Full wiring: `docs/STRUCTURE.md`

---

## 9. Golden Rules (Never Break)

- Never put product code outside `src/`
- Never create `patch1.md`, `final.md`, `temp.md` — only `XXX-phase-target`
- Always check PRODUCT-KNOWLEDGE Anti-Patterns before classifying
- Session log must start at the beginning of the session
- Max 10 active findings
- High-impact changes require `safety-reporter` + explicit approval

---

## 10. First 5 Minutes Checklist

1. `python scripts/status.py`
2. Read `README.md` + this `QUICKSTART.md`
3. Skim `MASTERPLAN.md` (Current Focus)
4. Decide: roots-definer or phase-planner?
5. Start work.

That’s it.
