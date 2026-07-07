# VCDesign Schemas

This directory contains machine-readable schemas to validate the specifications.
These schemas act as "guardrails" to ensure the specs maintain a consistent structure, but they are not the specification itself (the Prose/YAML in `../core` is authoritative).

## Available Schemas
- **[Judgment Closure](judgment-closure.schema.json)**: Validates `../protocols/judgment-closure.yaml`.

## Tools
- **[Tenure Check](tenure_check.py)**: Scans case instances (see `../core/schema_case.yaml` v0.2)
  for responsibility blank risk — empty `owner`, custody transfers without trace,
  missing `review_triggers`. Background: `../core/value-tenure-model.md`.

  Severity model (reaffirmation is **event-driven**, not calendar-driven):
  - `ERROR` — responsibility blank: empty owner, custody entry missing required fields,
    custody without `re_derivation_basis`. Non-zero exit.
  - `WARN` — event-driven obligations missed: no reaffirmation after a custody transfer,
    unconfirmed re-derivation, missing `review_triggers`.
  - `INFO` — weak signal only: pure time decay of `last_reaffirmed` (`--max-age-days`,
    default 180). Deliberately not WARN — see the decay note in
    `../core/value-tenure-model.md` §5.

  ```bash
  python3 specs/schemas/tenure_check.py specs/examples [--max-age-days 180]
  python3 specs/schemas/tenure_check.py --self-test   # clean/dirty fixtures under fixtures/
  ```

  CI runs the self-test and then scans `specs/examples`.

## How to Validate

### Using NPM (Recommended)
```bash
npm install
npm run validate
```

### Using script
```bash
./validate.sh
```

### CI/CD
Validation runs automatically on Pull Requests via GitHub Actions (`.github/workflows/validate.yml`).
