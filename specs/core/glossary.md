# VCDesign Core Glossary

## Status

Core terminology reference.

This file defines terms whose distinction affects VCDesign conformance.
It complements the broader glossary in `../glossary/glossary.md`.

---

## Judgment Proposal

A proposed judgment that may be reviewed but is not yet closed.

AI may produce or assist with a Judgment Proposal.
AI must not convert its own proposal into final responsibility.

---

## Judgment Closure

The explicit act of closing a Judgment Proposal as:

- `ACCEPTED`
- `DENIED`
- `UNKNOWN`

Judgment Closure is defined by `../protocols/judgment-closure.yaml`.

---

## Closed Judgment

A Judgment Proposal after Judgment Closure.

A Closed Judgment has an explicit closure state.
Only `ACCEPTED` is promotable to Resolution Handshake.

---

## Responsibility Asset

A responsibility-bearing judgment effectively created by:

```text
Judgment Closure = ACCEPTED
```

A Responsibility Asset contains or refers to:

- accepted judgment content
- owner or responsible actor
- evidence
- timestamp
- trace
- scope or applicability

A Responsibility Asset is not the same as a Resolution.
It is an accepted responsibility-bearing judgment, not yet necessarily an
executable committed action.

---

## Resolution

A Responsibility Asset promoted by Resolution Handshake into an executable
commitment.

```text
Responsibility Asset
  -> Resolution Handshake
  -> Resolution
```

A Resolution must include:

- responsible actor
- scope
- expiry or review condition
- trace reference
- committed Action when execution is required

Resolution is defined by `../protocols/resolution-handshake.yaml`.

---

## Action

The executable response to a Delta.

Canonical Action types are:

- Fix
- Reframe
- Defer
- Retire

Action terms are defined in `core.yaml` and clarified by
`../glossary/action-mapping.md`.

---

## Delta

A sign that a chapter's validity condition or responsibility placement may no
longer hold.

Delta is not only numerical deviation.
For VCDesign conformance, Delta must be evaluated for responsibility impact.

---

## IDG

Interface Determinability Gate.

IDG determines whether an interface is determinate enough for judgment to
continue.

IDG is not a decision maker.
If indeterminacy remains, the flow must halt, pause, or escalate rather than
continue as implicit acceptance.

---

## RCA

Responsibility Closure Agent.

An RCA guards a boundary and performs or supports Judgment Closure.
It must not replace human final responsibility where VCDesign requires a human
final decider.

---

## RCL

Responsibility Closure Loop.

RCL ensures that every open Delta is assigned to an explicit Resolution path,
including closure, deferral to a pool, or abort/termination according to the
applicable pattern.

RCL is a design-completion structure and does not bypass Judgment Closure or
Resolution Handshake.

---

## Gate Responsibility（点の責任）

Responsibility anchored to the moment of approval: "Is this correct now?"

Judgment Closure, IDG, and execution gates implement gate responsibility.
Passing a gate starts responsibility; it does not sustain it.

Defined in `value-tenure-model.md`.

---

## Tenure（線の責任・継続責任）

Responsibility as continued custody over time: "Who holds this, and how does it
survive handovers, unattended autonomous operation, and drift?"

Tenure is recorded through the tenure fields of `schema_case.yaml` (v0.2):
`value_intent`, `custody_chain`, `re_derivation_basis`, `review_triggers`,
`last_reaffirmed`. Tenure decays unless reaffirmed.

Defined in `value-tenure-model.md`.

---

## Custody Chain

The append-only record of responsibility handovers for a case or decision:
who transferred to whom, when, why, and whether the successor confirmed they
can re-derive the judgment from its recorded basis.

A custody transfer is a responsibility event under `../policies/temporal-governance.md`
and must not be overwritten or deleted.

---

## Reaffirmation

The explicit act of confirming that a standing decision is still valid,
recorded in `last_reaffirmed` (by whom, when, on what basis).

Reaffirmation must name a human confirmer. A decision that has passed its
gate but is never reaffirmed is not held — it is only approved.
