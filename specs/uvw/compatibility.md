# Compatibility with UVW

Since UVW is a set of conditions (Axioms), "compatibility" means **non-contradiction**, not "implementation".

## Definition
A system or design is **UVW-Compatible** if and only if:

1. **It does not deny the Axioms.**
   - It does not assume value is static.
   - It does not assume context is fixed.
2. **It deals with the consequences.**
   - It has a mechanism to handle Judgment Decay (review or expire).
   - It has a mechanism to bridge the Responsibility Gap (explicit assignment).

## Non-Compatible Examples
- A system that stores "goodness" as a static boolean flag forever.
- A system that allows AI to finalize high-risk decisions without a human responsibility sink.
