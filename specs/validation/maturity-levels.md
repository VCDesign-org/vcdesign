---
meta:
  id: MATURITY_LEVELS
  title: VCDesign Maturity Levels — Canonical Definitions
  layer: validation
  status: stable
  authority: normative
---

# VCDesign Maturity Levels

Canonical definitions for the four levels used across all VCDesign Maturity Profile assessments.

All five layers (Model, Agent, Responsibility, Time, Human Sovereignty) use this shared vocabulary.
Layer-specific rubrics are defined in `vcdesign-maturity-profile.md`.

---

## Level Definitions

| Level | Definition | VCDesign Correspondence |
|---|---|---|
| **Unstructured** | No structure exists. No design element addresses this layer. | No chapter, no boundary defined, no owner |
| **Defined** | Documented in design or policy, but not enforced in operations. | Boundary named in taxonomy, chapter exists on paper |
| **Enforced** | Operational and active; violations trigger controls or halt. | Judgment Closure + RCA active, policies applied, blocking conditions checked |
| **Governed** | Audited, improved, and re-evaluated on a continuing cycle. | metrics.yaml firing, supervisor loop active, periodic review scheduled |

---

## Level Progression Rules

1. **Enforced requires Defined to be true first.** A layer cannot be Enforced if its boundaries are not documented.
2. **Governed requires Enforced to be true first.** A layer cannot be Governed if its controls are not operational.
3. **Regression is normal.** A layer that was Enforced can revert to Defined when enforcement tooling is removed, key personnel leave, or process shortcuts accumulate. See `vcdesign-maturity-profile.md` for regression signals per layer.
4. **Blocking conditions override level.** If any blocking condition for a layer is unresolved, the layer cannot be rated above Unstructured regardless of other evidence.

---

## Evidence Validity Rules

Evidence must be:
- **Observable**: An assessor must be able to verify it independently, not just accept a claim.
- **Current**: Evidence from more than one review cycle ago is stale and does not count.
- **Specific**: "Logs exist" is not sufficient. The log must contain the required fields (actor, timestamp, decision reason).

These rules prevent the common failure mode of self-certified assessments where documentation is presented as operational evidence.

---

## Normative Reference

- `vcdesign-maturity-profile.md` — Layer-by-layer rubrics with evidence, failure signals, blocking conditions, and regression signals
- `core/metrics.yaml` — Metrics that operationalize Enforced and Governed level observation
- `core/policies.yaml` — Policy enforcement levels (advisory / warning / blocking) that map to this scale
