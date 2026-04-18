# VCDesign Specification Map

## VCDesign Authority Declaration
VCDesignの現行authorityは以下で構成される
- core/core.yaml
- core/policies.yaml
- core/metrics.yaml
- patterns（RCL等）は「Coreへの適用構造」
- legacy配下は「歴史的ドキュメントであり現行仕様ではない」

## 1. The Core (The "Why" and "What")
*Start here. This defines the problem and the unavoidable response.*
- **[Core](core/core.yaml)**: The basic OS, PDΔA flow, responsibility model, and the reality-fit definition that separates physical / semantic / value / responsibility loops across time scales.
- **[Axioms](core/axioms.yaml)**: The five irreducible commitments (A1–A5) underlying all of VCDesign. Non-conformance with any axiom overrides conformance with other specs.
- **[Decision Posture](core/decision-posture.yaml)**: Normative definition of the four postures (defer / commit / reconsider / abandon), selection criteria, and anti-defer-abuse guard.
- **[Policies](core/policies.yaml)**: Governance, AI boundaries, LLM placement constraints, haltability, and control rules.
- **[Metrics](core/metrics.yaml)**: Responsibility metrics, Δ detection, and growth measurement as operational fit under responsibility constraints.
- **[Core Glossary](core/glossary.md)**: Canonical distinctions that affect conformance, especially Judgment Proposal, Responsibility Asset, Resolution, Delta, IDG, RCA, and RCL.
- **[AI Adaptive Loop Model](core/ai-adaptive-loop-model.md)**: A readable guide that explains how the authority connects to real AI operating loops without becoming a new authority.
- **[Agent Era Model](core/agent-era-model.md)**: Reading aid for 2026 agent governance. Defines the 5-layer external explanation frame and 12 principles for governable AI agents. Connects to existing 4-loop model without replacing it.
- **[Case Schema](core/schema_case.yaml)**: Data structure for cases.
- **[Log Schema](core/schema_log.yaml)**: Data structure for decision logs.

> **Note**: **[RCL (Responsibility Closure Loop)](patterns/rcl/responsibility_closure_loop.yaml)** is a cross-cutting Standard.
> It is not part of explicit Core/Protocols/Patterns layers, but guarantees design completion
> by ensuring every Δ (Definition Gap) is assigned to an explicit R (Close / Defer to Pool / Abort).


## 2. Protocols (The "How" - Procedures)
*Read this to understand the rules of engagement.*
- **[Judgment Closure](protocols/judgment-closure.yaml)**: How to close a judgment (Accept/Deny/Unknown).
- **[Resolution Handshake](protocols/resolution-handshake.yaml)**: How to turn a judgment into a committed resolution.

## 3. Patterns (The "How" - Structures)
*Read this to implement the system.*
- **[Boundary Structure](patterns/boundary-pattern.yaml)**: The generic structure of an Explicit Verification Point.
- **[RCA Pattern](patterns/rca-pattern.yaml)**: The structure of a Responsibility Closure Agent.
- **[IDG Pattern](patterns/idg-pattern.yaml)**: The Interface Determinability Gate — blocks forced decisions under uncertainty. Required at B1, B4, and B13 boundaries.
- **[RCL (Responsibility Closure Loop)](patterns/rcl/responsibility_closure_loop.yaml)**: The design pattern for ensuring responsibility closure.

## 4. Chapters (The "When" - Narratives)
*Read this to understand how value, meaning, and responsibility erode or shift over time.*
- **[Chapter Definitions](chapters/chapter-pattern.yaml)**: The structure of a Chapter.
- **[C1: Purpose Drift](chapters/c1-purpose-drift.yaml)**: The silent rewriting of purpose.
- **[C2: Automation Burden](chapters/c2-automation-burden.yaml)**: When automation increases manual workload.
- **[C3: Trust & Responsibility Erosion](chapters/c3-trust-erosion.yaml)**: When opaque judgments cause rejection.
- **[C4: Reality Drift](chapters/c4-reality-drift.yaml)**: When model reference diverges from reality (B16).

## 5. Reference
- **[Boundary Registry](boundaries/registry.md)**: **The canonical B-number registry.** All B-numbers are assigned and tracked here. Consult before using any B-number.
- **[Boundary Taxonomy](boundaries/taxonomy.md)**: **The Types.** Authoritative definitions of each boundary (B1-B17).
- **[Boundary Cases](boundaries/)**: **Knowledge Base.** Raw case studies.
  - [Purpose Shift](boundaries/purpose-shift.yaml)
  - [Automation Manual](boundaries/automation-manual.yaml)
  - [Data Meaning](boundaries/data-meaning.yaml)
  - [Impact Accountability](boundaries/impact-accountability.yaml) (B17)
- **[Glossary](glossary/glossary.md)**: Terminology definitions.
- **[Action Mapping](glossary/action-mapping.md)**: **Normative.** Canonical mapping between Legacy / RCL / Core action terms (Close→Fix/Retire, Defer→Defer, Abort→Retire). Must be consulted when translating between RCL and PDΔA vocabulary.
- **[Schemas](schemas/)**: Machine-readable schemas and validation tools.
- **[Examples](examples/llm-change-approval.md)**: Concrete applications.
  - [Minimal Lifecycle Example](examples/vcdesign-minimal-lifecycle.md)
  - [AI Coding Agent](examples/coding-agent-boundary.md): Execution gate, Judgment Closure, and responsibility assignment for LLM-powered coding agents.
  - [Security Agent](examples/agent-governance-security.md): Governance for autonomous threat-response agents (Mythos-type). Includes commit posture under high-velocity incidents.
  - [Factory Operations Agent](examples/factory-agent-safe-loop.md): Physical Loop / Semantic Loop separation for manufacturing AI. Safety-critical halt design.
- **[Validation](validation/)**: Conformance and anti-pattern checks.
  - [Maturity Profile](validation/vcdesign-maturity-profile.md): Organizational diagnosis framework. 4-level scale × 5 layers with evidence, regression signals, and per-layer rubrics. **Start here if you want to evaluate your current AI governance posture before reading the full spec.**
  - [Maturity Levels](validation/maturity-levels.md): Canonical definitions of Unstructured / Defined / Enforced / Governed shared across all profile assessments.
  - [Conformance Cases](validation/vcdesign-conformance-cases.md)
  - [Anti-Patterns](validation/vcdesign-anti-patterns.md)
- **[Temporal Governance](policies/temporal-governance.md)**: Boundary between technical rollback and append-only responsibility trace.
