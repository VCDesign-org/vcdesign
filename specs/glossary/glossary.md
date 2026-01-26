# Glossary (VCDesign)

Definitions of terms used in VCDesign and UVW.

## Section 1: The Problem (UVW)
*Neutral terms regarding the state of the world.*

### Value
A perceived benefit or meaningfulness arising from the interaction between an Artifact and a Context. Not a static property.

### Artifact
Any output (code, text, data, model) produced by a system or worker.

### Judgment
The act of asserting that an Artifact satisfies a Value criterion.

### Decay
The natural loss of validity of a Judgment over time due to Context Drift.

### Responsibility
The state of being answerable for the consequences of a Judgment. In UVW, this is a scarce resource.

---

## Section 2: The Response (VCDesign Core)
*Terms defining the VCDesign stance.*

### Continuity
The state of value being maintained over time through active re-verification. The primary goal of VCDesign.

### Decision Posture
The rule "Stop or Review" applied when judgment confidence is lost.

### Boundary
An explicit interface where Judgment is attempted and protected from implicit values leaking in.

---

## Section 3: The Mechanism (Protocols & Patterns)
*Terms defining implementation details.*

### Judgment Closure
The act of explicitly signing (Accepted), denying (Denied), or declaring unknown (Unknown) on a specific Judgment Proposal.

### Resolution
A committed Action with a specified Responsible Actor, Scope, and Expiry. The output of a successful Judgment Closure.

### RCA (Responsibility Closure Agent)
A structural pattern for an agent that guards a Boundary and performs Judgment Closure.

### RP (Resolution Protocol)
A protocol that defines how a Closed Judgment is promoted to a Resolution Handshake.
