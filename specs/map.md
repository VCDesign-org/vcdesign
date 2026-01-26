# VCDesign Specification Map

## 1. The World (Problem Space)
If you want to understand **why** we need this, start here.
This layer defines the problem condition (UVW) that cannot be ignored.

- **[Definition](uvw/uvw.yaml)**: Machine-readable definition of the Unstable Value World.
  > Upstream: [unstable-value-world/unstable-value-world](https://github.com/unstable-value-world/unstable-value-world)
- **[Axioms](uvw/axioms.md)**: The 5 observation baselines (Value Instability, Responsibility Gap, etc.).
- **[Governance](uvw/GOVERNANCE.md)**: Why changing these axioms is a breaking change.

## 2. The Core (Response)
If you want to understand **how** we respond to the world, read this.
This layer defines the minimal unavoidable response.

- **[Assumption](vcdesign_core/vcdesign_uvw_assumption.md)**: Explicit declaration that we assume UVW.
- **[Core Spec](vcdesign_core/vsdesign_core.yaml)**: The "Stop or Review" Rule.
- **[Constitution](vcdesign_core/constitution.yaml)**: Our current stance and worldview (mutable).

## 3. The Implementation (Mechanism)
If you want to **build** or **verify** a system, read this.
This layer defines one valid mechanism (BOA) that satisfies the Core.

- **[Positioning](boa_core/boa_position.md)**: Why BOA is a cold mechanism.
- **[BOA Core](boa_core/boa_core.yaml)**: The authoritative spec of the architecture.
- **[Protocols](boa_core/protocols/)**:
  - **[RCA](boa_core/protocols/responsibility_closure_agent.yaml)**: How responsibility is signed.
  - **[RP](boa_core/protocols/resolution_protocol.yaml)**: How judgments are promoted.

## 4. Optional Extensions
- **[CCP](optional/ccp/ccp_handshake.yaml)**: External handshake protocol (Optional).
