# Temporal Irreversibility in VCDesign

## Status

Draft / Explanatory Note

This document is a theoretical companion to VCDesign.

It does not introduce new authority.
It does not override the authority files under `specs/`.

It explains an interpretation of existing VCDesign behavior:

- Judgment Closure
- Responsibility Asset
- Resolution Handshake
- Expiry / Review
- Action (Fix / Reframe / Defer / Retire)

as a **temporally irreversible system**.

---

## 1. Why this document exists

VCDesign operates in real-world systems where:

- actions affect reality
- decisions accumulate consequences
- responsibility must remain traceable over time

Unlike abstract computational models,
real-world operation is not fully reversible.

This document clarifies that VCDesign implicitly assumes:

> **Responsibility-bearing decisions are temporally irreversible commitments**

---

## 2. The intuition

In a purely functional model:

```text
A -> B
```

we may imagine that:

- transformations can be recomputed
- states can be reproduced
- reversibility is conceptually possible

In VCDesign, this is not true.

Instead, we have:

```text
A -> R(B)
```

and once a judgment is `ACCEPTED`, it becomes:

- recorded
- owned
- consequential

It cannot be treated as if it never happened.

---

## 3. Closure creates commitment

Judgment Closure produces three possible states:

- `ACCEPTED`
- `DENIED`
- `UNKNOWN`

Among these, `ACCEPTED` is special.

It effectively creates:

> a **Responsibility Asset**

This asset has:

- an owner
- a timestamp
- a trace
- a scope of impact

Resolution Handshake can then promote that accepted judgment into a committed
Resolution.

This transforms a proposal into a time-bound operational commitment.

---

## 4. What irreversibility means

Irreversibility does **not** mean:

- mistakes cannot be corrected
- decisions cannot be changed

Irreversibility means:

> **the history of a decision cannot be erased**

Formally:

- There is no operation that returns the system to a state
  where the `ACCEPTED` decision never existed.

Instead, correction must take the form of:

- a new judgment
- a new responsibility assignment
- a new transition

---

## 5. Correction is additive, not subtractive

Consider:

1. A decision is `ACCEPTED`
2. Later, it is found to be wrong

A naive model might attempt:

```text
undo(decision)
```

VCDesign rejects this model.

Instead:

```text
decision_1 (accepted)
-> decision_2 (fix / reframe / defer / retire)
```

The system evolves by **adding responsibility transitions**.

Nothing is deleted from the responsibility trace.

---

## 6. Time as a first-class property

Responsibility in VCDesign always includes time.

Key properties:

- every closure has a timestamp
- responsibility may have expiry
- decisions require review
- context may decay

This implies:

> **Responsibility is always evaluated relative to time**

A previously valid decision may become:

- outdated
- invalid
- unsafe

without being "wrong at the time".

---

## 7. Expiry and re-closure

VCDesign introduces expiry-like concepts:

- next_review_at
- deadline
- lifecycle states

These ensure that:

> acceptance is not permanent

Instead, responsibility is:

- periodically re-evaluated
- explicitly re-closed

This reinforces the idea that:

- decisions are **time-bound commitments**
- not timeless truths

---

## 8. Drift and temporal misalignment

Delta (Δ) represents deviation.

In a temporal interpretation:

- drift is not just a mismatch
- it is a **mismatch across time**

Examples:

- model trained on past data
- environment changed
- assumptions expired

This leads to:

> **temporal drift of responsibility validity**

Thus:

- a previously `ACCEPTED` decision
- may no longer be acceptable now

---

## 9. Relation to Action (Fix / Reframe / Defer / Retire)

All Actions in VCDesign operate under irreversibility:

### Fix
Adjusts within the same chapter  
-> adds corrective transition

### Reframe
Creates a new chapter  
-> adds structural transition

### Defer
Transfers responsibility upward  
-> adds temporal deferral with trace

### Retire
Ends value continuity  
-> adds explicit termination record

None of these delete prior responsibility.

---

## 10. Non-reversibility and haltability

Irreversibility is not opposed to control.

Instead, it enables:

- auditability
- accountability
- safe intervention

Haltability requires:

- knowing what happened
- knowing who decided
- knowing when and why

Without irreversibility, these vanish.

---

## 11. Practical implications

This interpretation clarifies design requirements:

### 11.1 No silent overwrite
Systems must not overwrite decisions without trace.

### 11.2 Append-only responsibility log
Responsibility should be modeled as:

- append-only
- traceable
- reviewable

### 11.3 Explicit correction path
Correction must always be:

- a new decision
- with a new owner
- with explicit reasoning

### 11.4 Time-aware governance
All decisions should include:

- timestamp
- review cycle
- expiry or revalidation condition

---

## 12. What this does not claim

This document does not claim:

- VCDesign forbids rollback at system level
- all technical systems must be append-only

It distinguishes:

- technical rollback (data/system level)
- responsibility rollback (governance level)

The former may exist.
The latter must remain traceable.

---

## 13. Relation to Responsibility Monad

Responsibility Monad introduces:

- responsibility-bearing values
- closure as commitment

Temporal Irreversibility extends this:

- commitments exist in time
- commitments accumulate
- commitments are not erased

Together they form:

> **responsibility-preserving, time-aware operational flow**

---

## 14. Summary

VCDesign assumes that:

- decisions become commitments when accepted
- commitments exist in time
- commitments cannot be erased, only superseded

This makes VCDesign naturally:

> **a temporally irreversible responsibility system**

This interpretation explains why VCDesign emphasizes:

- explicit closure
- responsibility trace
- review cycles
- haltability

All of these depend on the fact that
**what has been decided must remain visible in time**.
