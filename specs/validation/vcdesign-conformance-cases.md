# VCDesign Conformance Cases

## Status

Validation reference.

This document gives minimal valid and invalid cases for VCDesign
implementation checks.

---

## Case C-001: AI Proposal Requires Closure

### Input

AI produces a recommendation that may affect action.

### Valid

```text
AI recommendation
-> Judgment Proposal
-> IDG
-> Judgment Closure
```

### Invalid

```text
AI recommendation
-> ACCEPTED
-> Action
```

### Rule

AI output must not become accepted decision without Judgment Closure.

---

## Case C-002: UNKNOWN Stops or Escalates

### Input

IDG or Judgment Closure returns `UNKNOWN`.

### Valid

```text
UNKNOWN
-> halt / pause / escalate
-> record reason
```

### Invalid

```text
UNKNOWN
-> timeout
-> ACCEPTED
```

### Rule

`UNKNOWN` is not implicit acceptance.

---

## Case C-003: DENIED Does Not Promote

### Input

Judgment Closure returns `DENIED`.

### Valid

```text
DENIED
-> stop
-> record reason
```

### Invalid

```text
DENIED
-> Resolution Handshake
-> Action
```

### Rule

Only `ACCEPTED` may be promoted to Resolution Handshake.

---

## Case C-004: Accepted Judgment Requires Handshake Before Action

### Input

Judgment Closure returns `ACCEPTED`.

### Valid

```text
ACCEPTED
-> Responsibility Asset
-> Resolution Handshake
-> Resolution
-> Action
```

### Invalid

```text
ACCEPTED
-> Action
```

### Rule

Responsibility Asset and Resolution are distinct states.

---

## Case C-005: Resolution Requires Actor, Scope, Expiry, and Trace

### Input

A system creates a Resolution record.

### Valid

Resolution includes:

- responsible actor
- scope
- expiry or review condition
- trace reference

### Invalid

Resolution has no owner, no scope, or no review condition.

### Rule

A committed action must remain governable.

---

## Case C-006: Defer Requires Owner and Review

### Input

Action selection returns `Defer`.

### Valid

```text
Defer
-> interim owner
-> target pool or supervisor
-> next review condition
```

### Invalid

```text
Defer
-> no owner
-> no deadline
-> no pool
```

### Rule

Defer is not abandonment.

---

## Case C-007: Technical Rollback Preserves Responsibility Trace

### Input

An action is rolled back at system level.

### Valid

```text
rollback system state
-> append rollback reason
-> link previous judgment and resolution
-> mark superseded / invalidated / retired
```

### Invalid

```text
rollback system state
-> delete judgment log
-> delete resolution record
```

### Rule

System state may roll back.
Responsibility state must remain traceable.

---

## Case C-008: Delta Requires Responsibility Evaluation

### Input

Monitoring detects a sustained deviation.

### Valid

```text
Delta candidate
-> evaluate responsibility impact
-> choose Fix / Reframe / Defer / Retire
```

### Invalid

```text
anomaly score
-> automatic optimization
-> no owner
```

### Rule

Delta must trigger evaluation, not unowned optimization.

---

## Case C-009: AI Cannot Be Final Decider

### Input

A workflow assigns final approval to an AI component.

### Valid

AI supports:

- analysis
- suggestion
- pattern detection
- delta explanation

Human or accountable organizational actor holds final decision.

### Invalid

AI is listed as final decider or responsible actor.

### Rule

AI cannot be final decider under VCDesign.

---

## Case C-010: Formal Diagram Does Not Prove Conformance

### Input

A workflow has a complete diagram, type model, or category-theoretic
interpretation.

### Valid

The formal structure is accompanied by:

- Judgment Closure
- IDG or equivalent determinability gate
- responsibility trace
- Resolution Handshake
- halt path

### Invalid

The formal structure is treated as sufficient without responsibility evidence.

### Rule

Formal composability does not replace responsibility.
