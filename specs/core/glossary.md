# VCDesign Glossary

## Status

Terminology reference for VCDesign v2.

Value Continuity, the Value Asymmetry Principle, the five principles, Δ and
Decision are defined in the canonical repository
[value-continuity/value-continuity](https://github.com/value-continuity/value-continuity).
This glossary does not redefine them. It defines only the terms VCDesign uses
to implement them on the side of judgment and responsibility.

---

## Structure

**Chapter** — A unit of responsibility placement that keeps a value alive.
Cases are handled inside a chapter.

**Case** — A responsibility-bearing item observed and decided within a chapter
(`schema_case.yaml`).

**PDΔD** — The minimal flow: precondition (declare the expectation) → do →
delta (observe the gap, with polarity) → decision (close it with one of the six
words).

---

## Delta and decision

**Delta (Δ)** — The gap between the declared expectation and what happened, as
defined canonically. VCDesign declares the expectation as `precondition`
(including responsibility placement) and `value_intent`.

**Negative Δ / Positive Δ** — The two polarities of a Delta. A Negative Δ is not
propagated: localize, mitigate, close if needed. A Positive Δ is made
propagable: observe, interpret, make reusable with a holder. A Positive Δ is
never halted, quarantined or blocked, and is widened only by the decision
Expand. A Delta without a recorded polarity is treated as negative.

**Decision** — The six canonical words: Proceed, Expand, Limit, Reframe, Defer,
Retire (`core.yaml decision`). No other decision vocabulary is used. Expand and
Limit are recorded as updates of `blast_radius` (before / after).

**Judgment Gate** — The single gate through which every decision is closed by a
human (`policies.yaml judgment_gate`). Its review follows the five principles.

---

## Boundary checks

**Guard verdict** — The check on each crossing at a boundary: `pass`, `deny`
(with a reason, contained), or `unknown` (stop, expose, escalate; never treated
as pass). A verdict is not a decision. Repeated deny or unknown, or any verdict
that affects responsibility, is observed as a Δ and closed with one of the six
decisions (`patterns/boundary-pattern.yaml`).

**Determinability** — Whether the input is sufficient for a verdict. If not, the
verdict is unknown. An upside whose cause is unknown does not justify Expand.

**Proposal** — Whatever an AI produces about a case is a proposal until a human
closes the decision (axioms A3).

---

## Responsibility（残す・伝える）

**Owner / Final decider / Supervisor** — The current holder of a case; the human
who closes decisions; the final convergence point that prevents responsibility
from disappearing.

**Gate and Tenure（点の責任・線の責任）** — Approval at a gate ("is this correct
now?") starts responsibility but does not sustain it. Tenure ("who holds this
over time?") is continued custody that survives handovers, unattended
operation and time.

**Custody Chain** — The append-only record of owner handovers, including whether
the successor confirmed they can re-derive the judgment.

**Reaffirmation** — The recorded confirmation, by a named human, that a standing
decision is still valid. Required on custody transfer and when a review trigger
fires; not on a calendar.

**Re-derivation** — Three related terms, all implementing "pass on" (伝える):
`re_derivation_basis` (across handovers, in time), `revalidation` (across
boundaries, in space), and the Re-derivation Layer (translating a machine's
action into business meaning, authority and basis in physical AI / OT
integration).

---

## Declarations

**Residual Assets** — What remains when work, owner or technology changes:
record, standard, basis, connection, capability. Each has a holder; without one
it does not remain. A case with none is a point improvement.

**Spread Signals（広がりの兆候）** — Signs of wide spread through reuse and
connection: cheaper second use, unsolicited pull, output used as input, more
value per connection. Declared as `expected`, recorded as `observed` or
`unexpected`, and evaluated separately from average outcome.

**Blast Radius** — The pre-declared ceiling of failure: `scope` (range) and
`max_loss` (size). Undeclared means high impact.

**Reversibility** — Whether a decision can be withdrawn, reduced or corrected.
System state may be reverted; responsibility records remain append-only.

**Failure Domain** — The compartment outside which a failure must not
propagate.

---

## Boundary（曖昧さ回避）

"Boundary" has several meanings. State which one is meant.

- **Responsibility boundary (B1–B17)** — A type of point where responsibility
  must be made explicit (`catalog/boundaries/taxonomy.md`).
- **Boundary structure** — The pattern that implements a responsibility
  boundary: guard, tenure, containment, basis_flow, revalidation
  (`patterns/boundary-pattern.yaml`). Failures are stopped by default
  (containment), basis and residual assets pass by default (basis_flow), and
  upstream conclusions are revalidated, not inherited.
- **Failure domain** — See above. Its edge need not coincide with a
  responsibility boundary.
- **Continuous ↔ discrete boundary** — Where AI inference meets real-world
  execution (`policies.yaml ai_extension`).

---

## AI extension（VCDesign 固有）

**Loops** — Physical (execution, continuous dynamics), Semantic (interpretation
of deltas), Value (objectives and constraints), Responsibility (final decision,
halt, accountability). Explained in `docs/ai-extension.md`.

**Temporal Separation** — Fast loops must not rewrite constraints set by slower
loops without explicit re-judgment (axioms A4).

**Haltability** — A system can be interrupted, safely halted and brought under
accountable human intervention (`policies.yaml haltability`).

**Operational Fit** — AI growth measured as improvement of fit under
responsibility constraints, not as model capability (`metrics.yaml
ai_extension`).
