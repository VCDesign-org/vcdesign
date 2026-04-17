# VCDesign Minimal Lifecycle Example

## Status

Example.

This document gives a minimal end-to-end lifecycle showing how VCDesign connects
AI assistance, Judgment Closure, Responsibility Asset, Resolution Handshake,
Action, and Delta response.

---

## Scenario

A monitoring system detects abnormal vibration on a production line.
An AI assistant interprets the signal and recommends stopping the line.

---

## 1. Physical Event

```text
sensor event: vibration exceeds expected range
```

The event is not yet a judgment.
It is a physical signal.

---

## 2. Semantic Interpretation

```text
AI interpretation:
  "Pattern resembles bearing failure risk."
```

The AI output is treated as interpretation and proposal support.
It is not an accepted decision.

---

## 3. Judgment Proposal

```text
proposal:
  "Stop line 3 for inspection."
evidence:
  - vibration trend
  - recent maintenance history
  - AI interpretation
```

---

## 4. IDG

The system checks whether the interface is determinate enough for judgment.

```text
IDG result: determinable
```

If the result were indeterminate, the flow would move to `UNKNOWN`, halt, or
escalate.

---

## 5. Judgment Closure

A responsible human closes the proposal.

```text
closure_state: ACCEPTED
owner: shift_supervisor
reason: risk exceeds allowed operating condition
timestamp: 2026-04-17T09:00:00Z
```

This creates a Responsibility Asset.

---

## 6. Responsibility Asset

```text
responsibility_asset:
  judgment: "Stop line 3 for inspection."
  owner: shift_supervisor
  evidence:
    - vibration trend
    - maintenance history
    - AI interpretation
  closure_state: ACCEPTED
  trace_reference: jc-20260417-001
```

The Responsibility Asset is an accepted responsibility-bearing judgment.
It is not yet the committed execution record.

---

## 7. Resolution Handshake

The accepted judgment is promoted to a Resolution.

```text
resolution:
  action: Fix
  responsible_actor: shift_supervisor
  scope: line_3
  expiry: inspection_complete_or_2_hours
  trace_reference: jc-20260417-001
```

---

## 8. Action

```text
action:
  type: Fix
  command: stop line 3 and inspect bearing assembly
```

The action is now executable because responsibility, scope, and trace are
explicit.

---

## 9. Delta After Action

Inspection finds that the bearing is normal but the sensor mount is loose.

```text
delta:
  expected: bearing failure risk
  actual: sensor mount loosened
  responsibility_impact: previous proposal was too narrow
```

---

## 10. New Action Selection

The correction is additive, not history-erasing.

```text
new_action: Reframe
reason: problem is measurement reliability, not bearing health
owner: maintenance_lead
trace_reference: delta-20260417-002
```

The prior accepted judgment remains visible.
The new transition supersedes it for future operation.

---

## Summary Flow

```text
Physical event
-> AI interpretation
-> Judgment Proposal
-> IDG
-> Judgment Closure
-> Responsibility Asset
-> Resolution Handshake
-> Resolution / Action
-> Delta
-> Fix / Reframe / Defer / Retire
```

This is the minimal VCDesign lifecycle:

- AI assists but does not close responsibility.
- `UNKNOWN` would stop or escalate.
- `ACCEPTED` creates a Responsibility Asset.
- Resolution Handshake turns accepted judgment into committed action.
- Delta triggers explicit Action selection.
- Correction adds trace rather than deleting history.
