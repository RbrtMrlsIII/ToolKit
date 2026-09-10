# 004-responsibility-unit-seat-model

**Field:** Foundation  
**Phase:** foundation  
**Target:** responsibility-unit-seat-model  
**Status:** OBSERVED

## Observation

The existing WebAi Seat Foundation defines Responsibility Units, Seats, Agent assignment, scope-aware skill loading, and 2/3–4/5–8 scaling. The next slice needs to make those relationships a durable universal model rather than leaving them only as conceptual foundation text.

## Known baseline

003 established the self-protecting universal foundation, canonical-integrity enforcement, machine continuity, and the consuming-project boundary. The 004 model must build on that baseline and must not weaken canonical protection or introduce consumer-specific authority.

## Scope

- formalize Responsibility Unit structure;
- formalize Seat composition and adaptation;
- separate responsibility definition from Agent identity;
- define scale allocation rules;
- preserve skill authority boundaries;
- define verification and handover invariants.

## Anti-pattern check

Known dead ends reviewed before implementation: duplicate skill systems per Agent, implicit authorization through skills, consumer-specific rules entering universal Toolkit, governance content entering product code, and changing canonical structure without synchronized state/evidence.

## Five-evidence target

1. finding;
2. implementation/model artifact;
3. validation evidence;
4. continuity checkpoint + session;
5. handover/advancement record.

## Gate

004 remains OBSERVED until static validation and real CI validation are recorded. It must not advance to 005 without evidence and endorsement.
