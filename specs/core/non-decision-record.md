# VCDesign Non-Decision Record

## Status

**Design concept — not yet integrated into a normative schema.**

This document defines the *concept* and *required fields* of a non-decision
record. It intentionally does **not** decide where the record lives (inside
`schema_log.yaml` / `decision-posture.yaml`, or as a separate schema file).
That placement question is open — see [Open Questions](#open-questions) below.
Do not resolve it silently in an implementation; surface it for an explicit
decision first.

---

## 1. What this records

VCDesign already records decisions: a chosen posture (`decision-posture.yaml`),
a chosen action (`schema_log.yaml` / `why_action`), a chosen boundary
(`boundaries/`). All of these record something that *was* decided.

A non-decision record captures the other half: **the boundary someone chose
not to close** — a range deliberately left unformalized, at the same
granularity and with the same durability as a decision.

This is not a placeholder for a future decision. It is the record of a
decision *about scope*: "we decided not to write a rule here, and this is
why."

## 2. Why this needs its own record, not just a comment

An intentionally-left-open boundary and a boundary nobody got around to
defining look identical from the outside. Both show up as "no rule here."
An audit cannot tell them apart by inspecting the gap itself — only a record
made *at the time the gap was created* can.

Without that record, an intentional gap decays into an accidental one the
first time the person who left it open changes roles. Nothing about the gap
changes; only the ability to explain it disappears. See
[Re-derivation Layer](../../site/ja/re-derivation-layer/) for a concrete
instance: the B-layer (ROS2 ↔ equipment responsibility/meaning conversion)
is deliberately left unformalized, and that decision itself needs the record
this document defines — not just the observation that no standard exists
there yet.

## 3. Required fields

A non-decision record must include:

| Field | Description |
|---|---|
| `unformalized_scope` | The boundary of what was left unformalized — where it starts and where it ends. Must be specific enough that someone else could tell whether a given case falls inside it. |
| `left_open_by` | Who (role, not necessarily name) decided to leave this scope open. |
| `reason` | Why formalizing this scope was rejected — e.g., codifying it would become an optimization target, or closing it now would remove a decision that must stay with a human. |
| `reevaluation_trigger` | The event or condition that should prompt re-examining whether this should still be left open. Not a calendar date — see `review_triggers` in `value-tenure-model.md` for the same event-driven-over-calendar-driven principle. |

These four fields are structurally the non-decision analog of a Judgment
Closure: instead of `ACCEPTED` / `DENIED` / `UNKNOWN`, the record closes the
question "was this gap decided or merely absent?" as decided, with an owner,
a reason, and a re-open condition.

## 4. Relation to existing records

A non-decision record must be **readable alongside decisions**, not
archived separately where it will not be seen when the corresponding
decision is reviewed. This is a hard condition regardless of where the
record ends up living (see below): if a decision log entry and the
non-decision that bounds it cannot be read from the same place, the
non-decision record has already failed its purpose.

It complements, and does not replace:

- `decision-posture.yaml` — records a posture chosen *for a given Delta*.
  A non-decision record is not tied to a single Delta; it records a scope
  boundary that may apply across many future Deltas.
- `schema_log.yaml` (`why_action`) — records why an action was chosen.
  A non-decision record explains why *no* criterion was written for a class
  of judgments in the first place.
- `value-tenure-model.md` (`re_derivation_basis`, `review_triggers`) — these
  fields let a successor re-derive a *decision that was made*. The
  non-decision record is the parallel structure for a *decision not to
  decide*, at the same tenure discipline: it decays without an owner and a
  reaffirmation path exactly as tenure does.

## 5. Open Questions

- **Where does this record live?** Integrated as an optional block in the
  existing decision log schema (`schema_log.yaml`), or as its own schema
  file cross-referenced from decisions? Left unresolved by design — this is
  not a decision this document makes, and it should not be made silently by
  whoever implements this next. It must be raised for explicit sign-off
  before being coded into a schema.
- Whether `unformalized_scope` needs a machine-checkable shape (like a
  boundary reference to `boundaries/registry.md`) or remains free text is
  also open, pending the placement decision above.
