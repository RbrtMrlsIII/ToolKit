# Universal AGENT Toolkit — User Manual & Manual Deployment

**Canonical single file:** `docs/USER_MANUAL_DEPLOYMENT.md`

This is the human-operated guide for adopting, configuring, validating, and manually deploying the Toolkit into a consuming project. Provider-specific secrets, URLs, billing values, domain credentials, and production commands belong in the consuming project's own manual, not here.

## 1. Human authority first

```text
User vision / command
      ↓
consult Agents
      ↓
user approval of material direction
      ↓
PRODUCT_LAW.md
      ↓
MASTERPLAN.md slice/checklist
      ↓
skills + knowledge
      ↓
O-R-U-C-A-V-E-A
      ↓
implementation
      ↓
validation + evidence
      ↓
complete log / handover
      ↓
endorsement
      ↓
PRODUCT-KNOWLEDGE.md
```

The user remains the highest product authority. The Toolkit must never treat an Agent interpretation, existing code, provider default, or historical document as a replacement for explicit user intent.

## 2. What to copy

A consuming project should receive the Toolkit governance and skill structure appropriate to its project type, then define its own product authority and domain-specific extensions.

Keep these conceptual components together:

- Product Law / user-approved product authority
- POLICY and execution rules
- PRODUCT-KNOWLEDGE
- MASTERPLAN and slice checklist
- Agent operating guide
- skills and skill scope index
- `.agent/` machine state
- docs for findings, handover, history, contracts, reconciliation, and validation
- scripts for census, skill loading, knowledge operations, and integrity checks

Do not copy TeamAi-specific domain rules merely because TeamAi uses the Toolkit.

## 3. Bootstrap sequence

### A. Establish authority

Create or confirm the consuming project's `PRODUCT_LAW.md` from the user's approved product vision. Record what is non-negotiable, what is explicitly excluded, and which authority boundaries matter.

### B. Establish the execution map

Use `MASTERPLAN.md` to create the first approved slice. The slice identifies Field, XXX, target, impact, dependencies, and evidence requirements.

### C. Establish skill coverage

Resolve the smallest sufficient skill bundle from:

```text
project type
+ field
+ slice / XXX
+ task/domain
+ provider/runtime
+ tools/plugins
+ project guidance
+ permissions/policy
```

A frozen baseline should trigger a skill-coverage review. Repeated validated procedures should become candidate skills or skill extensions rather than repeated ad-hoc instructions.

### D. Start continuity state

Initialize machine state, session logging, checkpoint/handover structure, and census configuration before substantive work begins.

## 4. Manual deployment procedure

Manual deployment is a human-controlled release action. Agents may prepare and validate the deployment package when authorized, but they must not invent provider URLs, credentials, secret values, account identities, billing settings, or production assumptions.

### Step 1 — Confirm release authority

Verify:

- the intended deployment target;
- the approved Product Law and Masterplan slice;
- the user authorization for deployment;
- the exact artifact/build to deploy;
- rollback/recovery expectation;
- required human-only steps.

### Step 2 — Validate the repository state

Confirm the selected branch/ref, working tree cleanliness, expected commit, required checks, and current canonical state. Do not deploy from an unreviewed working tree or a stale ref.

### Step 3 — Validate the artifact

Confirm that the artifact was produced in an allowed build location, corresponds to the intended slice, passed the required tests/checks, and has durable evidence.

### Step 4 — Perform human-only provider actions

The human operator performs any step requiring credentials, account ownership, console access, production confirmation, billing authority, secret entry, or provider-side approval.

Agents may provide the exact guide and verification criteria. They must not fabricate values or claim completion for steps they cannot observe.

### Step 5 — Verify deployment

After the human action, capture:

- deployed version/commit if exposed;
- environment or target identifier;
- smoke-test result;
- expected reachability;
- relevant provider console confirmation;
- rollback signal if verification fails.

### Step 6 — Record evidence and close the slice

Update validation evidence, session log, checkpoint/handover, machine state, and Product Knowledge when a reusable lesson was learned. Only after verification may the slice advance or be endorsed according to policy.

## 5. Secrets and credentials

Toolkit documentation must never contain live secrets. Consumer projects should store credentials in their approved secret-management surface. Public client configuration may be documented only when the consumer's security model explicitly allows it.

Never paste provider private keys into chat, README files, skills, PRODUCT-KNOWLEDGE, or canonical planning documents.

## 6. Rollback / recovery

If deployment verification fails:

```text
STOP promotion
  ↓
record failure
  ↓
compare deployed state vs expected artifact
  ↓
restore last known good state when authorized
  ↓
validate recovery
  ↓
open investigation if cause is unclear
```

Do not silently rewrite Product Law, history, or evidence to make a failed deployment appear successful.

## 7. User-facing manual contract

This single file is the generic operating guide. Consumer projects may link provider-specific operational details from their own manual, but Toolkit itself should keep one canonical human deployment guide rather than fragmenting operator instructions across many near-duplicate files.

## 8. Completion definition

A manual deployment is complete only when:

`authorized → artifact identified → human-only steps completed → deployment verified → evidence recorded → log/checkpoint complete → endorsement/advance state updated`

A deployment is not complete merely because a provider accepted an upload or command.
