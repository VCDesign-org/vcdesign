# VCDesign Specifications

VCDesign (Value Continuity Design) implements
[Value Continuity](https://github.com/value-continuity/value-continuity) on the side of
**judgment and responsibility**.

Value Continuity is *keeping the ability to create the next value, even through change and failure*.
Its central principle, the **Value Asymmetry Principle**, is: *make upside propagable; do not let downside propagate.*
Those definitions live in the canonical repository and are not redefined here.
VCDesign specifies who decides, on what basis, with which of the six decisions, and who keeps holding what remains.

> VCDesign is law; VC-AD is its implementation at the current technical level.

These specifications are an **executable design language** for humans and automation:
design assistance, judgment support, and code generation.
Implementation must not begin unless the locus of judgment and the attribution of responsibility are explainable
(**Implementation Boundary Predefinition**).

### VCDesign Authority Declaration

The current authority of VCDesign v2 is:

- core/core.yaml
- core/policies.yaml
- core/metrics.yaml

`core/axioms.yaml` (A1–A5) is the starting point of conformance. Schemas define the records;
the boundary pattern implements the core; the catalog is a collection of domain cases.

## The core in six parts

| Part | What VCDesign specifies |
| --- | --- |
| Δ | The gap from the declared expectation (premises and value), with polarity: Negative Δ is not propagated; Positive Δ is made propagable |
| Responsibility | Owner, human final decider, custody across handovers (gate starts responsibility; tenure sustains it) |
| Boundary | Losses are stopped (containment), basis passes (basis_flow), conclusions are revalidated |
| Decision | Only the six words — Proceed, Expand, Limit, Reframe, Defer, Retire — through one judgment gate |
| Declaration | Per case: what remains (with a holder), spread signals, max loss, reversibility, dependencies |
| Metrics | Seventeen core metrics ordered by the five principles: keep, find, close, try, pass on |

AI governance (AI never holds final responsibility, LLM placement, temporal separation, agent execution gates)
is kept as a VCDesign-specific **extension** outside the core.

## Where to start?

See the **[Specification Map](specs/map.md)**.

1. [Value Continuity](https://github.com/value-continuity/value-continuity) — the principle
2. [specs/core/implementation.md](specs/core/implementation.md) — how VCDesign implements it, and the migration table from v1
3. [specs/core/core.yaml](specs/core/core.yaml), [policies.yaml](specs/core/policies.yaml), [metrics.yaml](specs/core/metrics.yaml) — the authority
4. [specs/examples/](specs/examples/) — three worked examples

## Directory Structure

- **[specs/core/](specs/core/)** — authority, axioms, schemas, implementation guide, glossary
- **[specs/patterns/](specs/patterns/)** — the boundary pattern (guard, containment, basis_flow, revalidation)
- **[specs/catalog/](specs/catalog/)** — chapters and responsibility boundaries (B1–B17)
- **[specs/examples/](specs/examples/)** — applications
- **[specs/validation/](specs/validation/)** — conformance checklist
- **[docs/](docs/)** — explanatory frame for the AI extension (not authority)

## Status

**v2.0.** Not compatible with v1. See the migration table in `specs/core/implementation.md`.

## License

This repository is licensed under the **MIT License**. See `LICENSE`.
