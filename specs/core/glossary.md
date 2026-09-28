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

Δ itself is defined in the Value Continuity canonical repository: the
difference between the expectation declared at the start (both preconditions
and intended value) and what actually happened. VCDesign declares the
expectation as `precondition` and `value_intent`. Delta has a polarity
(`core.yaml delta_definition.polarity`). A Delta without a recorded polarity
is treated as negative. See "Positive Δ / Negative Δ".

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

---

## Downside Containment（下振れの封じ込め）

Design for cutting the amplification of downside outcomes, not for predicting
them. Extreme downside arises when one failure produces the next through
chaining, reuse, concentration, and feedback; containment cuts that
amplification through four mechanisms: isolate (failure domains), cap
(declared max loss), revalidate (no inherited upstream acceptance), and
deconcentrate (detect single points of dependency or judgment).

This is VCDesign's implementation of "close" (閉じる) among the five
principles of Value Continuity, and the handling of Negative Δ.

Terms on the same axis at different layers: `survive_downside` (criterion),
`downside_review` (gate step), `fatal_downside` (hard stop, regardless of owner),
`downside_survivability` (metric), `blast_radius` (record).

Defined in `downside-containment-model.md`.

---

## Blast Radius

The pre-declared ceiling of how far a decision may fail: `scope` (range of
impact) and `max_loss` (size of loss). Scope does not substitute for max loss.
A long-term decision's bet size is a kind of max loss. An undeclared blast
radius is treated as high impact.

---

## Revalidation

Re-checking upstream basis at a boundary so that upstream ACCEPTED is not
inherited downstream as-is (spatial, across boundaries). Distinct from
`re_derivation_basis` in tenure (temporal, across handovers) and from the
Re-derivation Layer.

---

## Reversibility

Whether a decision can be withdrawn, reduced, or corrected, recorded in
`schema_case.yaml` as `reversibility` (class, reversal_path, reversal_window,
reversal_owner). Same axis as `reversible` (criterion), `reversibility_assessed`
(gate check), and `reversibility_score` (metric). System state may be reverted;
responsibility records remain append-only.

---

## Value Asymmetry（価値の非対称）

The Value Asymmetry Principle — make upside propagable; do not let downside
propagate — is defined in the Value Continuity canonical repository
(https://github.com/value-continuity/value-continuity), not here. VCDesign
implements it by handling `value_accumulation` (upside) and
`downside_containment` (downside) on the same judgment record, and by treating
Positive Δ and Negative Δ asymmetrically (`delta_definition.polarity`).

See `value-continuity-implementation.md`.

---

## Point Improvement / Line Improvement（点の改善・線の改善）

A point improvement is anchored to the work as it is now; when the work
changes, it is invalidated and nothing remains. A line improvement leaves
residual assets (record, standard, basis, connection, capability) that survive
changes of work, owner, or technology and are reused. The test question:
"When the work changes, what of this improvement remains?"

An improvement invalidated by a work change is treated as a Negative Δ
(`one_shot_improvement`).

---

## Tail Signal（広がりの兆候）

Observable business facts suggesting that an improvement can spread through
reuse and connection: `reuse_cost_decline`, `unsolicited_pull`,
`output_as_input`, `value_per_connection`, and `other` (the list is not
exhaustive). Signals declared in advance are recorded in
`tail_signals.observed`; undeclared ones in `tail_signals.unexpected`. Both
are Positive Δ. Recorded separately from average outcome. Scaling
(`scale_gate`) requires an observed tail signal, not average success alone.

---

## Positive Δ / Negative Δ

Defined in the Value Continuity canonical repository: a Negative Δ falls
below the declared expectation (preconditions and value) and must not
propagate; a Positive Δ exceeds it and is made propagable. Both are measured
against the same baseline (`precondition` and `value_intent`, plus
`tail_signals.expected` when declared).

In VCDesign, a Negative Δ appears as a break in a chapter's validity
condition, responsibility placement, or value; it is localized, mitigated,
and closed if needed (RCA / IDG → containment → action). A Positive Δ is
observed, interpreted, and made reusable (recorded in `residual_assets` with a
holder), and is expanded only through `scale_gate`.

The two are asymmetric: a Positive Δ never triggers halt, quarantine, or
blocking, and an observation containing both is split into two Deltas.
Defined in `core.yaml delta_definition.polarity`.

---

## Decision（判断の選択肢）

The decision options Proceed / Expand / Reframe / Limit / Defer / Retire,
defined in the Value Continuity canonical repository. Recorded in
`schema_log.yaml decision`, separately from Action (a lifecycle transition).
The mapping to Action, decision posture, `decision_size`, and `scale_gate`
outcomes is normative in `core.yaml decision_vocabulary`. Expand and Limit
have no Action counterpart; both are defined as updates of the
`blast_radius` declaration.

---

## Re-derivation Layer

The layer, in physical AI / OT integration, that translates a machine's action
(e.g. a navigation or capture command) into business meaning, authority, and
basis — so that a successor can later reconstruct why the result was valid.
It is an application of `re_derivation_basis`, not a separate primitive.

Three terms share the word "re-derive / re-validate" and must not be
confused:

- `re_derivation_basis` (tenure): temporal — across handovers
- `revalidation` (boundary-pattern): spatial — across boundaries
- Re-derivation Layer: translation from machine action to business meaning

All three implement "pass on" (伝える): pass basis, not conclusions, and let
the receiver re-judge in its own context.

---

## Boundary（曖昧さ回避）

"Boundary" has several meanings in VCDesign. State which one is meant.

- **Responsibility boundary (B1–B17)**: a type of point where responsibility
  must be made explicit. Defined in `../boundaries/taxonomy.md`.
- **Boundary structure (Explicit Verification Point)**: the pattern that
  implements a responsibility boundary with a guard (RCA), handshake,
  tenure, containment, revalidation, and basis_flow. Defined in
  `../patterns/boundary-pattern.yaml`.
- **Boundary mediation**: the continuous ↔ discrete connection between AI
  inference and real-world execution. Defined in `core.yaml
  boundary_mediation` and `policies.yaml boundary_safety`.
- **Failure domain**: the compartment outside which a failure must not
  propagate (`failure_domain`). Its edge need not coincide with a
  responsibility boundary.
- **VC-AD boundary**: code-level constraints in the architecture-yaml-protocols
  repository. Outside this repository's scope.

At a boundary structure, failures are stopped by default
(`containment.propagation: deny`), conclusions are not inherited
(`revalidation`), and basis and residual assets pass by default
(`basis_flow`).
