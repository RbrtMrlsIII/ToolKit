# builds/ — Canonical Build Outputs

**Only allowed place for build artifacts.**

```
builds/
├── latest/               ← always points to latest successful build
├── XXX-phase-target/     ← one folder per XXX
│   ├── web/
│   ├── mobile/
│   ├── backend/
│   ├── 3d/
│   ├── artifacts/
│   └── build-log-*.md/json
└── archive/              ← compressed after 2 checkpoints
```

Rules:
- Never put builds inside `src/` or `docs/`
- Every build must have a timestamped log
- Use skill `skills/canonical-build/SKILL.md`
