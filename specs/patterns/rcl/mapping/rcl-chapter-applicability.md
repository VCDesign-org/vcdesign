# RCL ↔ Chapter / Applicability Mapping

This document clarifies how Responsibility Closure Loop (RCL)
aligns with Chapter structure and Applicability clauses in VCDesign.

RCL does not determine applicability by itself.
Instead, it exposes factual conditions (Δ → R failure)
that justify Applicability or Non-Applicability judgments.

---

## 1. Mapping RCL Elements to Chapter Structure

| RCL Element | Meaning | Chapter Field | Failure Mode |
|------------|--------|---------------|--------------|
| P (Preconditions / Promise) | What must be true / what must not be auto-decided | decision_basis | Chapter loses purpose; AI or ops decide implicitly |
| D (Do / Display / Assist) | Execution, UI, AI assistance (not final judgment) | carry_forward_state | Execution overrides judgment |
| Δ (Delta) | Facts where P is not fulfilled | open_deltas | Gaps become invisible |
| R (Resolution) | Close / Defer (Pool) / Abort | resolution_log, pool_entries | Responsibility evaporates |

Note: Assigning Δ to Pool is a valid Resolution.

---

## 2. Relationship to Applicability Clauses

| Applicability Clause | Observed via RCL | Meaning |
|---------------------|------------------|---------|
| VC-AP-001 | P defined, Δ resolvable to R | VCDesign applicable |
| VC-NAP-001 | Δ indicates scope overflow without responsibility escalation | Non-applicable |
| VC-NAP-002 | Δ accumulates, Pool cannot resolve | Value continuity impossible |
| VC-NAP-003 | Abort structurally disallowed | VCDesign must advise non-applicability |

RCL provides evidence.
Applicability judgment remains a constitutional decision.
