# String-Diagram Style Reading of VCDesign

## Status

Draft / Explanatory Note

This document is a reading aid for people who already know category theory,
string diagrams, or process diagrams.

It does not claim that VCDesign is fully formalized as a strict monoidal
category. VCDesign includes gates, halts, ownership, evidence, and human
commitment. Those are operational structures, not only algebraic ones.

The useful claim is narrower:

> VCDesign responsibility flow can be drawn in a string-diagram style, as long
> as explicit closure, haltability, and temporal trace are treated as part of
> the diagram.

---

## 1. Legend

In this document:

```text
wire      = value, state, context, or responsibility-bearing value
box       = transformation, interpretation, check, or action
gate      = boundary that may allow, deny, or halt continuation
trace     = append-only responsibility history
R(A)      = value A with responsibility context
```

`R(A)` should not be read as a fully proven monad in the mathematical sense.
It is a monad-like wrapper used to explain why VCDesign composes operations
through responsibility context rather than through bare values.

---

## 2. Minimal Responsibility Flow

```text
Sensor data
    |
    v
[Interpretation / AI]
    |
    v
Judgment proposal
    |
    v
[IDG: determinable?]
    | yes                         no
    v                             v
[Judgment Closure]             UNKNOWN / halt / escalate
    |
    v
Closed judgment
    |
    v
[Resolution Handshake]
    |
    v
Resolution / committed action
```

The important separation is:

- AI may produce interpretation, classification, or proposal.
- IDG exposes indeterminacy and blocks forced decisions under uncertainty.
- Judgment Closure produces `ACCEPTED`, `DENIED`, or `UNKNOWN`.
- Only `ACCEPTED` may be promoted by Resolution Handshake into a Resolution.

So the diagram is not only a data-flow diagram.
It is a flow of permission to continue under explicit responsibility.

---

## 3. Kleisli-Style Reading

A normal pipeline might be written:

```text
A -> B -> C
```

VCDesign usually needs:

```text
A -> R(B) -> R(C)
```

Where `R(B)` carries at least:

- value or proposal
- closure state
- owner or responsible actor when closed
- evidence
- timestamp and expiry/review condition
- trace reference

Composition is therefore closer to responsibility-preserving composition:

```text
f : A -> R(B)
g : B -> R(C)

g <=< f : A -> R(C)
```

But the composition is partial or gated in practice.
It is valid only when the previous step is allowed to continue.

```text
A --f--> R(B, proposed)
          |
          v
       [Closure]
          |
          +--> ACCEPTED --g--> R(C)
          |
          +--> DENIED -------> stop
          |
          +--> UNKNOWN ------> halt / escalate
```

This is why VCDesign should not be described as ordinary function composition.
It is composition through an explicit responsibility context.

---

## 4. IDG as a Gate on Composition

IDG is not a decision maker.
It is a gate that prevents indeterminacy from being silently collapsed into a
decision.

```text
R(B, proposed)
    |
    v
[IDG]
    | determinable                 indeterminate
    v                              v
[Closure possible]              UNKNOWN / halt / escalate
```

In category-theoretic language, this is best read as a restriction on
composition, not as an ordinary morphism that always returns a usable output.

The practical rule is:

> If determinability is absent, the system must not pretend that composition
> can continue normally.

---

## 5. Temporal Irreversibility

Judgment Closure creates a time-stamped commitment.
After an `ACCEPTED` judgment is operationalized, VCDesign does not model
correction as erasing the old judgment.

```text
t1
A --AI--> R(B, proposed)

t2
R(B, proposed) --Human Closure--> R(B, accepted)

t3
R(B, accepted) --Resolution Handshake--> R(C, committed)
```

There is no governance-level inverse path that returns the system to a history
where the accepted judgment never existed.

Correction is additive:

```text
R(C, committed) --Fix/Reframe/Defer/Retire--> R(C', committed)
```

Technical rollback may still exist at the system level.
Responsibility rollback must remain traceable at the governance level.

---

## 6. Delta as Non-Commutativity

Delta can be explained as a failure of expected and actual paths to coincide.

```text
Expected:

A --f--> B --g--> C

Actual:

A --f'-> B' --g'-> C'
```

The observed difference is:

```text
Delta = difference(expected path, actual path)
```

In diagrammatic terms, the square does not commute:

```text
        f
   A ------> B
   |         |
h  |         | k
   v         v
   B' -----> C'
        g'
```

This does not mean every non-commuting square is a VCDesign Delta.
In VCDesign, Delta matters when the deviation affects chapter validity,
responsibility placement, value continuity, or safe operation.

When Delta is significant, continuation requires explicit Action:

```text
Delta detected
    |
    v
[Evaluate responsibility impact]
    |
    v
Action: Fix / Reframe / Defer / Retire
```

---

## 7. Four-Loop Reading

The four-loop model is not four independent control systems.
It is a decomposition of PDΔA across time scales and responsibility placement.

```text
Responsibility Loop  final decision / halt / accountability
        ^
        |
Value Loop           objectives / constraints / value review
        ^
        |
Semantic Loop        interpretation / delta-to-meaning / AI assistance
        ^
        |
Physical Loop        sensors / actuators / continuous operation
```

Interpretation pressure moves upward.
Execution pressure moves downward.
Responsibility governance must be able to interrupt lower loops.

This can be read as double-category-like because there are two distinct kinds
of structure:

- horizontal process flow, such as sensing, interpretation, closure, and action
- vertical responsibility mediation across physical, semantic, value, and
  responsibility layers

The phrase "double-category-like" is intentionally modest.
It indicates a useful analogy, not a completed formal construction.

---

## 8. Complete Process Diagram

```text
Physical        Semantic             Value                  Responsibility
--------        --------             -----                  --------------

Sensor
  |
  v
[AI / Interpretation]
  |
  v
Judgment proposal
  |
  v
[IDG: determinable?] --no--> UNKNOWN / halt / escalate
  |
 yes
  v
[Judgment Closure] --DENIED--> stop
  |
 ACCEPTED
  v
Responsibility Asset
  |
  v
[Resolution Handshake]
  |
  v
Resolution / Action
  |
  v
Reality

Delta detection may feed back into evaluation and trigger
Fix / Reframe / Defer / Retire.
```

The central question is not only:

> How are operations connected?

It is:

> Under what responsibility context is continuation allowed?

---

## 9. What the Diagram Captures

This diagrammatic reading captures:

- responsibility-bearing values, written as `R(A)`
- gated composition through IDG and Judgment Closure
- `UNKNOWN` as halt/escalation, not implicit acceptance
- `ACCEPTED` as a distinct operational state
- Resolution Handshake as promotion from closed judgment to committed action
- Delta as responsibility-relevant path divergence
- temporal irreversibility as append-only responsibility trace
- four-loop separation across time scales

---

## 10. Summary

VCDesign can be usefully drawn as a responsibility-flow diagram.

For a category-theory reader, the closest intuition is:

> VCDesign composes operations in a Kleisli-like, gated, time-aware process
> structure where values may continue only when responsibility remains explicit.

That is the intended meaning of a "string-diagram style" reading of VCDesign.
