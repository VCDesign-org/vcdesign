# CCP (Continuity Claim Protocol)

## Status
**Optional / Non-required**

CCP is **NOT required** for BOA operation.

---

## What CCP Is

CCP (Continuity Claim Protocol) is an **external handshake specification**  
used to explicitly agree on:

- scope and context
- decision authority
- risk and trust assumptions
- reversibility and continuity claims

**before** an external actor (AI, human, system) participates in a judgment flow.

---

## What CCP Is NOT

- CCP is **not part of BOA core**
- CCP does **not affect** BOA internal procedures
- CCP does **not participate** in:
  - judgment logic
  - responsibility closure
  - resolution promotion

Removing CCP does **not change** the BOA procedure.

---

## Relationship to BOA

BOA operates with the following required components only:

- Boundary
- Responsibility Closure Agent (RCA)
- Resolution Protocol (RP)

CCP exists **outside** this boundary.

If used, CCP only provides a *prior agreement* layer  
for external participants interacting **with** BOA, not **inside** BOA.

---

## When CCP Is Useful

CCP may be useful when:

- interacting with external or third-party AI systems
- delegating judgment authority across organizational boundaries
- requiring explicit continuity / reversibility guarantees
- formalizing cost, trust, and escalation assumptions

---

## Design Principle

CCP is intentionally separated to preserve:

- minimal BOA core
- clear responsibility boundaries
- safe deletion without breaking procedures

Optional protocols must remain optional.

---

## Provenance

This CCP specification was originally developed alongside BOA,
and later **separated intentionally** to keep BOA minimal and stable.

See migration notes for details.
