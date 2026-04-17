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
