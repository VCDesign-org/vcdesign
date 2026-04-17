# Temporal Governance Policy

## Status

Policy clarification.

This document clarifies the boundary between technical rollback and
responsibility trace.

---

## Core Rule

System state may be rolled back.
Responsibility state must remain append-only.

```text
System State:
  rollback allowed

Responsibility State:
  append-only
```

---

## What May Roll Back

Technical rollback may affect:

- deployment state
- runtime configuration
- database contents
- generated artifacts
- external commands when reversal is technically possible

Rollback is allowed when it is part of a governed Resolution or emergency halt
path.

---

## What Must Not Be Deleted

Responsibility history must not delete:

- Judgment Proposal
- Judgment Closure result
- owner or responsible actor
- evidence available at the time
- Resolution record
- reason for rollback
- supersession, invalidation, or retirement event

---

## Required Pattern

Rollback must be recorded as a new responsibility event.

```text
original judgment
-> resolution
-> action
-> rollback event
-> superseded / invalidated / retired
```

The rollback event must point to the prior trace.

---

## Invalid Pattern

```text
original judgment
-> resolution
-> action
-> rollback
-> delete judgment and resolution
```

This is invalid because it erases why the system acted and who accepted
responsibility at the time.

---

## Relation to Temporal Irreversibility

Temporal irreversibility does not mean mistakes cannot be corrected.

It means that accepted responsibility cannot be made historically nonexistent.

Correction is represented by adding a new responsibility-bearing transition,
not by erasing the prior one.
