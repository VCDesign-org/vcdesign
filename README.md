# VCDesign Specifications

VCDesign (Value Continuity Design) is a set of specifications not for "how to build," but for designing how to protect the created value throughout time.

> VCDesign is law; VC-AD is its implementation at the current technical level.

## What is VCDesign?
VCDesign is a design specification to prevent the loss of continuity in **Judgment**, **Responsibility**, and **Time / Operations** in highly automated systems.
Core term: **Implementation Boundary Predefinition** (boundaries must be intentionally defined before implementation starts).

As a core start condition, implementation must not begin unless the locus of judgment and the attribution of responsibility are explainable.

It aims to explicitly structure where individual judgments are closed, who takes responsibility, and how they evolve over time during operations, even as the system scales.

These specifications are not merely reading material. They are defined as an **executable design language** intended to be used by humans and advanced automation support for **design assistance**, **judgment support**, and **code generation**.

## Where to start?
See the **[Specification Map](specs/map.md)** for the full overview.

We recommend reading in the following order:
1. **[specs/core/](specs/core/)** (Authority): Why this design is necessary, what must be protected.
2. **[specs/protocols/](specs/protocols/)** (How / Operations): When to close judgments and how to hand off responsibility.
3. **[specs/chapters/](specs/chapters/)** (When): Which designs are necessary at what point in the timeline.

## Directory Structure

* **[specs/core/](specs/core/)**: **The Authority.** The minimal, unavoidable definitions of VCDesign. 思想を知りたければ各YAMLの冒頭コメントを読み、実装したければスキーマに従う。
* **[specs/protocols/](specs/protocols/)**: **The Procedures.** Standardized ways to close judgments and hand off responsibility.
* **[specs/patterns/](specs/patterns/)**: **The Structures.** Reference patterns (like Boundary Structures and RCA) to implement the core.
* **[specs/chapters/](specs/chapters/)**: **The Narratives (The "When").** Time-based design units describing how judgment and responsibility shift over time (not phases or versions).
* **[specs/glossary/](specs/glossary/)**: Terminology.

## Status
Core specifications are **Stable**.
Protocols and Patterns are **Stable** but extensible.

## License
This repository is licensed under the **MIT License**. See `LICENSE`.
