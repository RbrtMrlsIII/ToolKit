# Backend Integrations Repo — Supabase, Firebase, WowSQL, GitHub, PayPal, etc.

> **Purpose:** Ready-to-copy backend integration files for any project type. Supabase, Firebase, WowSQL (MySQL variant), GitHub, PayPal, Stripe, Auth, Storage. Linked from front-door README.md.

**Main Use:** Don't write integration from scratch. Copy from here, adapt to your project. Works with universal AGENT repo census + skills.

## Quick Start — Use Faster

### Supabase
```bash
cp -r backend-integrations-repo/supabase/* your-project/src/backend/supabase/
# Edit .env with SUPABASE_URL, SUPABASE_ANON_KEY
```
Files: `client.ts`, `schema.sql`, `auth.ts`, `realtime.ts`

### Firebase
```bash
cp -r backend-integrations-repo/firebase/* your-project/src/backend/firebase/
```
Files: `firebase-config.ts`, `firestore.ts`, `auth.ts`, `storage.ts`

### WowSQL (MySQL/WowSQL)
```bash
cp backend-integrations-repo/wowsql/schema.sql your-project/
cp backend-integrations-repo/wowsql/connection.py your-project/src/backend/
```
Files: `schema.sql`, `connection.py`, `queries.py`, `migrations/`

### GitHub
```bash
cp -r backend-integrations-repo/github/.github your-project/
```
Files: `.github/workflows/census.yml`, `deploy.yml`, `issues/`

### PayPal + Stripe
```bash
cp backend-integrations-repo/paypal/paypal-client.ts your-project/src/backend/payments/
cp backend-integrations-repo/stripe/stripe-client.ts your-project/src/backend/payments/
```

## Structure

| Folder | Main Use | Key Files |
|--------|----------|-----------|
| `supabase/` | Supabase backend as authority | client.ts, schema.sql, auth.ts, realtime.ts, policies.sql |
| `firebase/` | Firebase auth, firestore, storage | firebase-config.ts, firestore.ts, auth.ts, storage.ts |
| `wowsql/` | WowSQL/MySQL — data models, tables, census inventory | schema.sql, connection.py, connection.mjs, queries.py, census-tables.sql |
| `github/` | GitHub integration — actions, workflows for census + validation | workflows/census.yml, workflows/deploy.yml, ISSUE_TEMPLATE/ |
| `paypal/` | PayPal payments | paypal-client.ts, paypal-webhook.ts, paypal-config.json |
| `stripe/` | Stripe payments (extra) | stripe-client.ts, webhook.ts |
| `auth/` | Generic auth patterns (validated pattern from PRODUCT-KNOWLEDGE.md) | auth-middleware.ts, jwt.ts, session.ts |
| `storage/` | Storage for 3D assets, UI assets | storage-client.ts, upload-3d.ts |

## Linking

- Front-door: `../README.md` (main front-door README links here)
- Main repo: `../agent-repo-template/README.md` → links to this backend repo
- Test repo: `../test-files-repo/README.md` → tests for backend (test-supabase.js etc.)
- Skills: `skills/contract-manager/SKILL.md` uses these as authority examples

## Census Integration

Census counts backend endpoints from this repo patterns:
- `backend_endpoints`: `src/backend/routes/**`, `api/**`, `server/routes/**`
- `data_models`: `**/models/**`, `**/schemas/**`, `**/*.sql` (from wowsql/)

Before converting UI to 3D, census tells you how many backend endpoints, how many data models you have.

## For Mobile AI — Fast Copy

Don't reinvent. When MASTERPLAN says `005-align-core-1` needs backend:

1. Read skill `skills/contract-manager/SKILL.md`
2. Copy from `backend-integrations-repo/supabase/` or `firebase/` or `wowsql/`
3. Adapt to `docs/contracts/` authority
4. Validate with `test-files-repo/js/test-supabase.js`

Date: 2026-08-31
