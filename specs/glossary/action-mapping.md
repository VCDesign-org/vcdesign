# Action Mapping: Legacy vs. RCL vs. Core

## Overview
This document clarifies the mapping between terms used in legacy documents, RCL (Responsibility Closure Loop), and the current Core specifications. It aims to eliminate confusion in terminology and establish the canonical terms for VCDesign.

## Canonical Terms (Core)
The authoritative terms are defined in `core/core.yaml` and are as follows:
- **Action (A)**: The response to a Delta (Δ). Types include Fix, Reframe, Defer, Retire.

## Term Mapping Table

| Legacy Term | RCL Term | Core Term | Meaning Difference | Canonical? |
|-------------|----------|-----------|-------------------|------------|
| Resolve     | Close    | Action(A) | Legacy/RCL focus on closure; Core emphasizes action type | No (use Action) |
| Reject      | Abort    | Action(A) | Legacy/RCL imply rejection; Core specifies action as Abort | No (use Action) |
| Return      | Defer    | Action(A) | Legacy/RCL focus on deferral; Core specifies action as Defer | No (use Action) |

## Meaning Differences
- **Legacy Terms**: Focused on immediate resolution outcomes (resolve/reject/return).
- **RCL Terms**: Emphasize closure mechanisms (close/abort/defer).
- **Core Terms**: Define specific action types (Fix/Reframe/Defer/Retire) that ensure value continuity.

## Canonical Usage
- Always use **Action (A)** and specify the type (Fix, Reframe, Defer, Retire) when referring to responses in VCDesign.
- Legacy and RCL terms should be avoided in new documentation; use this mapping for historical references.

## Key Principle
Action(A) is the only executable form of Responsibility closure.