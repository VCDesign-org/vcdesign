# AI Adaptive Loop Model

This document explains how VCDesign authority connects to real AI operations.

- Authority remains:
  - `core/core.yaml`
  - `core/policies.yaml`
  - `core/metrics.yaml`
- This document is a structural reading aid for those authority files.
- It is not a fourth authority and not an independent theory.

## Overview

VCDesign defines value continuity as a responsibility-governed operating structure.
In real AI systems, that structure appears as separated but connected loops with different timescales.
The point is not to celebrate "autonomy" as unconstrained model behavior.
The point is to preserve value continuity while allowing adaptation under human accountability.

## Basic Definition

VCDesign treats AI deployment as a boundary design problem.
The central problem is how to connect discontinuous intelligence to continuous real-world systems without losing explainability, haltability, or responsibility.

PDΔA remains the minimal operating cycle:

- Precondition
- Do
- Delta
- Action

The adaptive loop model explains where that cycle appears and how it is governed.
The four-loop structure is not an independent control model.
It is a decomposition of the PDDeltaA cycle across time scales and responsibilities.

## Four Loop Structure

### 1. Physical Loop

- Role: stability, execution, continuous dynamics
- Main concern: whether the real system keeps operating safely
- Typical components: sensors, actuators, services, deterministic controllers
- Main risk: real-world instability or irreversible harm

### 2. Semantic Loop

- Role: interpretation, delta-to-meaning conversion, discontinuous inference
- Main concern: what the observed deviation means
- Typical components: LLMs, classifiers, analyzers, review tools
- Main risk: misreading noise as delta, or missing meaningful change

### 3. Value Loop

- Role: objective setting, constraints, direction of optimization
- Main concern: what should continue and what counts as success
- Typical components: explicit policy, value review, human goal-setting
- Main risk: hidden goal drift or unauthorized objective rewriting

### 4. Responsibility Loop

- Role: final decision, halt, accountability
- Main concern: who can decide, stop, explain, and bear consequences
- Typical components: human final decider, supervisor, audit trail, escalation path
- Main risk: unstoppable operation or responsibility disappearance

## Structure Diagram

```text
        Responsibility Governance
    [surrounds and can intervene in all loops]

Physical Loop <-> Semantic Loop <-> Value Loop

[all loop crossings require explicit boundaries]
```

Interpretation happens upward and execution pressure happens downward.
Responsibility is not a computational loop.
It is a governance layer that can intervene in all loops.

## Time Scale

The loops must not be collapsed into one clock.

- Physical Loop: milliseconds to hours
- Semantic Loop: seconds to days
- Value Loop: days to quarters
- Responsibility Loop: immediate intervention to lifecycle-wide governance

Temporal separation matters because a fast execution loop must not silently rewrite a slower value or responsibility loop.

## Design Principles

- Value continuity is realized through loop coordination, not raw model capability.
- Delta detection must be connected to responsibility impact, not only anomaly score.
- Adaptation is valid only when it remains explainable and reviewable.
- A slower governance loop must always be able to stop a faster execution loop.

## LLM Placement Constraints

LLMs belong primarily in the Semantic Loop.

- Allowed: interpretation, classification, recommendation, delta explanation
- Not allowed: direct physical control
- Not allowed: autonomous value objective setting
- Not allowed: final authority in the Responsibility Loop

If LLM output can affect the world, it must first pass through explicit policy and safety gates.

## Boundary Design

Two boundary classes matter.

Boundaries are not only transformation layers.
They are points where responsibility must be explicitly reassigned or reaffirmed.

### Continuous to Discrete Boundary

Transforms real-world change into delta candidates and interpretable meaning.

### Discrete to Continuous Boundary

Transforms judgments, recommendations, or policies into real execution.

At both boundaries, the system must preserve:

- traceability
- policy checks
- human override
- halt path

## Growth Definition

In VCDesign, AI growth does not mean only better model benchmarks.
Growth means improved operational fit under responsibility constraints.

Representative growth signals:

- better delta detection quality
- better semantic interpretation quality
- better value alignment quality
- better judgment consistency
- better halt readiness
- fewer boundary violations

## Haltability

Haltability is a design requirement, not an operational afterthought.

A system is not governable unless:

- human intervention is possible
- arbitrary halt is possible
- decision accountability is traceable
- a safe-state path exists after halt

## VCDesign Core / Policies / Metrics Mapping

- `core/core.yaml`
  - adaptive loop model
  - temporal separation
  - boundary mediation
  - final definition of AI as a boundary design problem
- `core/policies.yaml`
  - LLM placement constraints
  - boundary safety gates
  - haltability and override requirements
- `core/metrics.yaml`
  - growth as operational fit
  - loop-linked quality indicators
  - boundary and haltability observation

## Conclusion

VCDesign does not define AI growth as unconstrained autonomous capability.
It defines growth as a responsibility-governed improvement of operational fit across separated loops.
That is how value continuity connects to real AI operations without creating a new authority outside Core, Policies, and Metrics.
