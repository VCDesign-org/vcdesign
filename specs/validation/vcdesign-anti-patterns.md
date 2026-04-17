# VCDesign Anti-Patterns

## Status

Validation reference.

This document lists designs that should be treated as non-conforming or unsafe
under VCDesign.

The purpose is practical: VCDesign is often more effective at preventing broken
responsibility flows than at prescribing one universal correct design.

---

## AP-001: AI Emits Accepted Judgment

### Pattern

An AI system directly returns `ACCEPTED`, final approval, or final
responsibility.

### Why It Fails

AI may assist interpretation and proposal.
It must not hold final responsibility.

### Required Correction

Route AI output as a Judgment Proposal.
Pass it through IDG and Judgment Closure with an accountable responsible actor.

---

## AP-002: UNKNOWN Becomes Automatic Acceptance

### Pattern

`UNKNOWN` is converted to `ACCEPTED` after timeout, lack of response, or
operational pressure.

### Why It Fails

`UNKNOWN` preserves indeterminacy.
It must pause, halt, or escalate rather than become implicit yes.

### Required Correction

Escalate to a responsible actor, fallback path, or safe halt.
Record the reason for indeterminacy.

---

## AP-003: Resolution Without Handshake

### Pattern

A closed judgment is sent to execution without Resolution Handshake.

### Why It Fails

Judgment and committed action are different states.
Resolution requires responsible actor, scope, expiry, and trace.

### Required Correction

Promote only `ACCEPTED` closed judgments through Resolution Handshake.

---

## AP-004: Ownerless Defer

### Pattern

A decision is deferred without owner, target pool, deadline, or next review
condition.

### Why It Fails

Defer without responsibility is abandonment disguised as governance.

### Required Correction

Assign an interim owner, escalation pool, and review condition.

---

## AP-005: Rollback Deletes Responsibility Trace

### Pattern

A technical rollback removes the judgment, approval, owner, or reason that led
to the rolled-back action.

### Why It Fails

Technical state may roll back.
Responsibility history must remain append-only.

### Required Correction

Record rollback as a new responsibility event that supersedes or invalidates
the prior action without deleting it.

---

## AP-006: Delta Treated as Anomaly Score Only

### Pattern

Delta is detected as a metric deviation but never evaluated for chapter
validity, responsibility placement, or value continuity.

### Why It Fails

VCDesign Delta is responsibility-relevant deviation, not just numerical error.

### Required Correction

Connect Delta detection to responsibility impact assessment and Action
selection.

---

## AP-007: Hidden Responsibility Transfer

### Pattern

Work is shifted to operators, users, vendors, or downstream systems without
explicit reassignment.

### Why It Fails

Responsibility disappears from the designed structure and reappears as
unowned operational burden.

### Required Correction

Treat the transfer as a Boundary and require explicit responsibility
reassignment or reaffirmation.

---

## AP-008: Formal Structure Replaces Responsibility

### Pattern

A system is considered valid because a diagram, type, workflow, or formal model
composes, even though ownership, haltability, or trace is missing.

### Why It Fails

VCDesign is not justified by formal structure.
Formal structure may explain responsibility flow but cannot replace it.

### Required Correction

Verify Judgment Closure, responsible actor, trace, halt path, and Resolution
Handshake independently of the formal model.
