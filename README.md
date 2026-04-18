# VCDesign Specifications

VCDesign (Value Continuity Design) is a set of specifications not for "how to build," but for designing how to protect the created value throughout time.

> VCDesign is law; VC-AD is its implementation at the current technical level.

## What is VCDesign?
VCDesign is a design specification to prevent the loss of continuity in **Judgment**, **Responsibility**, and **Time / Operations** in highly automated systems.
Core term: **Implementation Boundary Predefinition** (boundaries must be intentionally defined before implementation starts).

As a core start condition, implementation must not begin unless the locus of judgment and the attribution of responsibility are explainable.

It aims to explicitly structure where individual judgments are closed, who takes responsibility, and how they evolve over time during operations, even as the system scales.

These specifications are not merely reading material. They are defined as an **executable design language** intended to be used by humans and advanced automation support for **design assistance**, **judgment support**, and **code generation**.

### VCDesign Authority Declaration
VCDesignの現行authorityは以下で構成される
- core/core.yaml
- core/policies.yaml
- core/metrics.yaml
- core/axioms.yaml（A1〜A5：すべての仕様の基底となる公理）
- core/decision-posture.yaml（defer/commit/reconsider/abandon の規範的定義）
- patterns（RCL等）は「Coreへの適用構造」
- legacy配下は「歴史的ドキュメントであり現行仕様ではない」

### VCDesign Core Principles
VCDesign is a development OS that structures systems through chapter and responsibility transitions for the purpose of value continuity.
In real AI operations, this is read as a responsibility-governed separation of four loops: Physical, Semantic, Value, and Responsibility.
LLMs belong primarily in the Semantic Loop, while growth is defined as improved operational fit under responsibility constraints rather than mere model capability increase.

#### Basic Principles
- **Responsibility Non-Disappearance Principle**: Responsibility must always exist somewhere.
- **Explainability Principle**: All judgments must be explainable by humans.
- **AI Non-Responsibility Principle**: AI assists but does not hold responsibility.
- **Δ-Driven Principle**: Systems operate based on detecting deviations (Δ) from preconditions.
- **Capability ≠ Authority Principle**: High model capability does not grant decision authority. Every agent action requires an explicitly declared boundary and a named responsible actor.

## Where to start?
See the **[Specification Map](specs/map.md)** for the full overview.

We recommend reading in the following order:
1. **[specs/core/](specs/core/)** (Authority): Why this design is necessary, what must be protected.
   - **[ai-adaptive-loop-model.md](specs/core/ai-adaptive-loop-model.md)**: How Core / Policies / Metrics connect to real AI operating loops.
   - **[agent-era-model.md](specs/core/agent-era-model.md)**: 5-layer external explanation frame and 12 principles for governing AI agents (2026+).
2. **[specs/protocols/](specs/protocols/)** (How / Operations): When to close judgments and how to hand off responsibility.
3. **[specs/chapters/](specs/chapters/)** (When): Which designs are necessary at what point in the timeline.
4. **[specs/examples/](specs/examples/)** (Applied): Concrete use cases — AI coding agent, security agent, factory operations agent.

## Directory Structure

* **[specs/core/](specs/core/)**: **The Authority.** The minimal, unavoidable definitions of VCDesign.
* **[specs/protocols/](specs/protocols/)**: **The Procedures.** Standardized ways to close judgments and hand off responsibility.
* **[specs/patterns/](specs/patterns/)**: **The Structures.** Reference patterns (Boundary, RCA, IDG, RCL) to implement the core.
* **[specs/chapters/](specs/chapters/)**: **The Narratives (The "When").** Time-based design units describing how judgment and responsibility shift over time.
* **[specs/boundaries/](specs/boundaries/)**: **The Boundary Taxonomy.** Canonical registry (B1–B17) and case studies of responsibility boundaries.
* **[specs/glossary/](specs/glossary/)**: Terminology, including the normative action mapping (Legacy / RCL / Core).
* **[specs/validation/](specs/validation/)**: Conformance cases, anti-patterns, and the **[Maturity Profile](specs/validation/vcdesign-maturity-profile.md)** for organizational diagnosis.
* **[specs/examples/](specs/examples/)**: Concrete applications — minimal lifecycle, LLM approval workflow, and three agent governance use cases.

## Status
Core specifications are **Stable**.
Protocols, Patterns, and Chapters are **Stable** but extensible.

## License
This repository is licensed under the **MIT License**. See `LICENSE`.
