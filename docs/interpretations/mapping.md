# Interpretation to Authority Mapping

## Status

Explanatory traceability note.

This document maps claims made in `docs/interpretations/` back to the
authoritative VCDesign specifications.

It does not add new VCDesign rules.
It exists to prevent retrospective interpretation from being mistaken for
authority.

---

## Mapping Rule

Every interpretation claim should be read in this direction:

```text
specs authority -> interpretation
```

not:

```text
interpretation -> specs authority
```

The interpretation documents may explain existing VCDesign structures through
category theory or diagrammatic language, but they do not justify, replace, or
modify those structures.

---

## Claim Mapping

| Interpretation claim | Authority source | What the interpretation must not add |
| --- | --- | --- |
| AI output is proposal, interpretation, or recommendation, not final responsibility. | `specs/core/core.yaml`, `specs/core/policies.yaml` | AI must not become final decider or responsible actor. |
| `UNKNOWN` must halt, pause, or escalate rather than become implicit acceptance. | `specs/protocols/judgment-closure.yaml`, `specs/patterns/idg-pattern.yaml` | Indeterminacy must not be collapsed into acceptance for compositional convenience. |
| Judgment Closure has explicit states: `ACCEPTED`, `DENIED`, `UNKNOWN`. | `specs/protocols/judgment-closure.yaml` | Additional closure states must not be assumed by interpretation documents. |
| `ACCEPTED` effectively creates a Responsibility Asset. | `specs/protocols/judgment-closure.yaml`, `specs/core/glossary.md` | Responsibility Asset must not be treated as already executable action. |
| Resolution requires Resolution Handshake after accepted closure. | `specs/protocols/resolution-handshake.yaml`, `specs/core/glossary.md` | Closed judgment must not be promoted to execution without handshake. |
| Responsibility must not disappear across transitions. | `specs/core/core.yaml`, `specs/core/policies.yaml` | Formal composition must not hide ownership, final decider, or trace. |
| Delta indicates a responsibility-relevant deviation. | `specs/core/core.yaml`, `specs/core/metrics.yaml` | Delta must not be reduced to a numeric anomaly score alone. |
| Fix / Reframe / Defer / Retire are the executable Action types. | `specs/core/core.yaml`, `specs/glossary/action-mapping.md` | Interpretation documents must not introduce new executable action classes. |
| Responsibility trace is append-only at governance level. | `specs/policies/temporal-governance.md`, `specs/core/schema_log.yaml` | Technical rollback must not erase responsibility history. |
| Category theory is an explanatory lens. | `docs/interpretations/README.md` | Category theory must not become VCDesign authority. |

---

## Boundary of This Mapping

This mapping is intentionally conservative.

If an interpretation claim cannot be traced to `specs/`, it should be treated
as commentary, not as a VCDesign requirement.

If a future formalization defines actual categories, objects, morphisms,
composition, identity, and laws, it should be added as a separate formal work
and should still not override `specs/` unless VCDesign authority is explicitly
updated.
