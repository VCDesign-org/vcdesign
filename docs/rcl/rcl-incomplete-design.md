# RCL and Incomplete Design State

Not all projects can operate RCL from the beginning.
VCDesign explicitly distinguishes between:

- Non-Applicability
- Incomplete Design

---

## 1. Incomplete Design (RCL Not Operated)

A design is considered INCOMPLETE when:

- Δ exists
- Δ is not assigned to any Resolution (Close / Pool / Abort)
- RCL loop is not executed

This state is NOT automatically non-applicable.

---

## 2. Consequences

- Responsibility is not closed
- RCA cannot function correctly
- VCDesign must not be claimed as achieved

However:
- Design support may still conclude
- Open Δ must be explicitly listed
- Future RCL operation may be planned

---

## 3. Acceptable Design Support Conclusion

A valid VCDesign support outcome may state:

- What the design result is
- What is currently in Responsibility Pools
- What Δ remains unresolved
- Suggested review timing based on P

Execution is optional.
Closure of responsibility is mandatory for claiming VCDesign compliance.

---

## 4. Summary

| State | VCDesign Claim |
|------|----------------|
| RCL operated | VCDesign applicable |
| RCL planned | Design incomplete |
| RCL impossible | VCDesign non-applicable |
