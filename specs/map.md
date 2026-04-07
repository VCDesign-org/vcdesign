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
- **[Policies](core/policies.yaml)**: Governance, AI boundaries, LLM placement constraints, haltability, and control rules.
- **[Metrics](core/metrics.yaml)**: Responsibility metrics, Δ detection, and growth measurement as operational fit under responsibility constraints.
- **[AI Adaptive Loop Model](core/ai-adaptive-loop-model.md)**: A readable guide that explains how the authority connects to real AI operating loops without becoming a new authority.
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
- **[RCL (Responsibility Closure Loop)](patterns/rcl/responsibility_closure_loop.yaml)**: The design pattern for ensuring responsibility closure.

## 4. Chapters (The "When" - Narratives)
*Read this to understand how value, meaning, and responsibility erode or shift over time.*
- **[Chapter Definitions](chapters/chapter-pattern.yaml)**: The structure of a Chapter.
- **[C1: Purpose Drift](chapters/c1-purpose-drift.yaml)**: The silent rewriting of purpose.
- **[C2: Automation Burden](chapters/c2-automation-burden.yaml)**: When automation increases manual workload.
- **[C3: Trust & Responsibility Erosion](chapters/c3-trust-erosion.yaml)**: When opaque judgments cause rejection.
- **[C4: Reality Drift](chapters/c4-reality-drift.yaml)**: When model reference diverges from reality (B16).

## 5. Reference
- **[Boundary Taxonomy](boundaries/taxonomy.md)**: **The Types.** A catalog of known responsibility boundaries (B1-B17).
- **[Boundary Cases](boundaries/)**: **Knowledge Base.** Raw case studies.
  - [Purpose Shift](boundaries/purpose-shift.yaml)
  - [Automation Manual](boundaries/automation-manual.yaml)
  - [Data Meaning](boundaries/data-meaning.yaml)
  - [Impact Accountability](boundaries/impact-accountability.yaml) (B17)
- **[Glossary](glossary/glossary.md)**: Terminology definitions.
- **[Schemas](schemas/)**: Machine-readable schemas and validation tools.
- **[Examples](examples/llm-change-approval.md)**: Concrete applications.
