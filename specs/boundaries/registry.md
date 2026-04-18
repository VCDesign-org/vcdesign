# VCDesign Boundary Registry

## Status

Normative. This file is the canonical source of truth for all B-number assignments.

All boundary definitions must be registered here before use in any spec, chapter,
or boundary case file. B-numbers are permanent: retired boundaries must remain in
the registry with status `retired`, not be deleted or renumbered.

---

## Registration Table

| B#  | Name                          | Status  | Defined In                        | Used In |
|-----|-------------------------------|---------|-----------------------------------|---------|
| B1  | Human ↔ AI Judgment           | active  | boundaries/taxonomy.md            | c1, c3 |
| B2  | Automation ↔ Manual           | active  | boundaries/taxonomy.md            | c2, boundaries/automation-manual.yaml |
| B3  | System ↔ Reality              | active  | boundaries/taxonomy.md            | c3, c4 |
| B4  | Data ↔ Meaning                | active  | boundaries/taxonomy.md            | c1, c3, boundaries/data-meaning.yaml, boundaries/purpose-shift.yaml |
| B5  | Decision ↔ Action             | active  | boundaries/taxonomy.md            | — |
| B6  | Responsibility Assignment     | active  | boundaries/taxonomy.md            | c1, c2, c3, c4, boundaries/purpose-shift.yaml |
| B7  | Organizational                | active  | boundaries/taxonomy.md            | c1 |
| B8  | Policy ↔ Practice             | active  | boundaries/taxonomy.md            | c2 |
| B9  | Expertise                     | active  | boundaries/taxonomy.md            | c2 |
| B10 | Temporal (Now ↔ Later)        | active  | boundaries/taxonomy.md            | c4 |
| B11 | Risk Acceptance               | active  | boundaries/taxonomy.md            | — |
| B12 | Knowledge Validity            | active  | boundaries/taxonomy.md            | — |
| B13 | Interpretation                | active  | boundaries/taxonomy.md            | c4 |
| B14 | Accountability ↔ Blame        | active  | boundaries/taxonomy.md            | — |
| B15 | Design ↔ Emergence            | active  | boundaries/taxonomy.md            | — |
| B16 | Model ↔ Reality               | active  | boundaries/taxonomy.md + boundaries/model-reality.yaml | c4 |
| B17 | Impact ↔ Accountability       | active  | boundaries/taxonomy.md + boundaries/impact-accountability.yaml | c4 |

---

## How to Register a New Boundary

1. Assign the next sequential B-number (currently B18).
2. Add a row to the Registration Table above.
3. Define the boundary in `boundaries/taxonomy.md` (authoritative definition).
4. Optionally create a detailed case file in `boundaries/`.
5. Update `Used In` as chapters and cases reference the boundary.

A B-number may not be used in any spec before it appears in this registry.

---

## Retired Boundaries

_(none as of v0.1)_

Retired boundaries keep their number and row in the table with `status: retired`.
The definition in taxonomy.md is preserved with a retirement note.

---

## Notes

- B16 and B17 were defined in separate boundary case files before this registry existed.
  Their definitions in taxonomy.md are now the authoritative source; the case files
  provide extended detail only.
- taxonomy.md was the de facto registry prior to v0.1 of this document. All B1–B17
  definitions there remain canonical.
