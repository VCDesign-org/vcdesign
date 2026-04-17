# Responsibility Monad

## Status

Draft / Explanatory Note

This document is a theoretical companion to VCDesign.
It is not an authority file and does not override:

- `specs/core/core.yaml`
- `specs/core/policies.yaml`
- `specs/core/metrics.yaml`
- `specs/protocols/judgment-closure.yaml`
- `specs/protocols/resolution-handshake.yaml`

Its purpose is to provide a category-theoretic reading of existing VCDesign
structures, especially Judgment Closure, Responsibility Asset, Resolution
Handshake, and temporally irreversible commitment.

The term "Responsibility Monad" is used as a reading aid. This document does
not prove the monad laws for a formal category of VCDesign systems.

---

## 1. Why this document exists

VCDesign already defines:

- explicit Judgment Closure
- Responsibility Asset
- `UNKNOWN` as a stopping or escalation state
- Resolution Handshake
- temporal separation across Physical, Semantic, Value, and Responsibility loops

This document does not introduce a new governing rule.
It explains one formal interpretation of those existing structures.

In that interpretation, VCDesign operates over responsibility-bearing values:
values are not handled as bare outputs, but as outputs carried together with
ownership, evidence, temporal validity, and closure state.

---

## 2. Core Intuition

A normal computational pipeline often treats outputs as plain values:

```text
A -> B
```

VCDesign does not.

VCDesign treats meaningful operational outputs as requiring an explicit
responsibility context:

```text
A -> R(B)
```

`R(B)` is not only a value.
It is a value wrapped with responsibility conditions.

---

## 3. Responsibility-Bearing Value

A responsibility-bearing value may be read as:

```yaml
Responsibility<B>:
  value: B
  owner: optional
  evidence: set
  timestamp: time
  expiry_or_review: optional
  status: proposed | accepted | denied | unknown | expired
  trace: history
```

The same value with a different responsibility state is not the same
operational object.

For example:

```text
"stop line 3" as a proposal
"stop line 3" as an accepted responsibility asset
```

These are operationally different things.

---

## 4. Relation to Existing VCDesign Concepts

### 4.1 Judgment Closure

Judgment Closure is the gate by which a proposal is explicitly closed as:

- `ACCEPTED`
- `DENIED`
- `UNKNOWN`

In Responsibility Monad terms, this is the point where a
responsibility-bearing value is either promoted, blocked, or held in
indeterminacy.

### 4.2 Responsibility Asset

An `ACCEPTED` judgment effectively creates what VCDesign calls a
Responsibility Asset.

In monadic reading, this is not just a value.
It is a value lifted into a signed and accountable operational context.

### 4.3 UNKNOWN

`UNKNOWN` must not be treated as implicit acceptance.

In this reading, `UNKNOWN` blocks unsafe composition.
It preserves indeterminacy instead of crushing it into a false decision.

### 4.4 Resolution Handshake

Resolution Handshake promotes an accepted closed judgment into a committed
Resolution.

It is the bridge from:

```text
closed judgment -> committed action
```

The prerequisite is not merely that a value exists.
The prerequisite is that Judgment Closure is `ACCEPTED` and a responsible actor
is identified.

---

## 5. Lift and Closure

A plain value may be lifted into responsibility context:

```text
eta : A -> R(A)
```

In VCDesign, this initial lifted state should normally be treated as proposed,
not as accepted.

This matters especially for AI outputs.

AI may produce:

- interpretation
- proposal
- recommendation
- delta explanation

But AI does not produce final responsibility by itself.
Closure requires explicit ownership, sufficient evidence, and a valid closure
state.

---

## 6. Responsibility-Preserving Composition

A responsibility-bearing transition may be written as:

```text
f : A -> R(B)
```

A following transition may be written as:

```text
g : B -> R(C)
```

These may compose in a Kleisli-like way only when the prior result remains
acceptable for continuation.

Operationally, this means:

- responsibility trace must not disappear
- evidence must remain available
- `UNKNOWN` must block or escalate flow
- detected Delta may invalidate continuation
- accepted responsibility must be promoted through Resolution Handshake before
  committed action

So composition is not merely value-flow.
It is responsibility-preserving flow.

---

## 7. Why "Monad-Like"

The point of the Responsibility Monad reading is not abstract elegance.
It is practical discipline.

It explains why VCDesign insists that:

- AI output is not silently treated as decision
- accepted judgment is distinguishable from suggestion
- operational action remains connected to accountable ownership
- responsibility trace survives across composed steps
- unsafe indeterminacy stops or escalates rather than continuing as if it were
  accepted

This is monad-like because continuation happens through a wrapper `R`.
It is not asserted here as a complete formal monad unless a specific category,
unit, bind, and laws are later defined.

---

## 8. Time and Irreversibility

Responsibility in VCDesign is temporal.

An accepted judgment is not a timeless truth.
It is a time-bound commitment.

This means responsibility-bearing values are not just wrapped with owner and
evidence, but also with:

- timestamp
- expiry or review condition
- historical trace
- lifecycle state

Once a judgment is accepted and operationalized, it should not be modeled as a
reversible transformation back to a neutral proposal.

Instead, any correction should be modeled as a new responsibility-bearing
transition.

This is why VCDesign is naturally compatible with a temporally irreversible
interpretation.

---

## 9. What This Document Does Not Claim

This document does not claim that:

- VCDesign is reducible to category theory
- category theory is required to use VCDesign
- all VCDesign structures are fully captured by monads alone
- AI can hold final responsibility
- technical rollback is forbidden

VCDesign still includes practical elements beyond abstract structure,
including:

- human sovereignty
- haltability
- organizational reassignment
- chapter-based operational drift
- multi-timescale responsibility governance

The Responsibility Monad is a reading aid, not a replacement for VCDesign
authority files.

---

## 10. Practical Value

This interpretation is useful when designing:

- AI review gates
- approval workflows
- audit trails
- responsibility-preserving orchestration
- systems where proposal, closure, and execution must remain distinct

It clarifies that the key operational object is not "output", but accountable
output with explicit closure state.

---

## 11. Summary

VCDesign can be read as operating on responsibility-bearing values rather than
plain values.

This reading helps explain:

- why Judgment Closure is essential
- why `ACCEPTED` creates a distinct operational state
- why `UNKNOWN` must stop or escalate flow
- why Resolution Handshake is required before committed action
- why responsibility must survive across transitions
- why accepted commitments are temporal and not fully reversible

That formal reading is what this document calls the Responsibility Monad.
