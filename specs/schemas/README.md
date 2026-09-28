# VCDesign Tools

Tools that check case records against the specifications. They are guardrails, not the specification itself (`../core` is authoritative).

## Tools
- **[Tenure Check](tenure_check.py)**: Scans case instances (see `../core/schema_case.yaml` v1.0)
  for responsibility blank risk — empty `owner`, custody transfers without trace,
  missing `review_triggers`. Background: `../core/implementation.md` (残す・伝える).

  Severity model (reaffirmation is **event-driven**, not calendar-driven):
  - `ERROR` — responsibility blank: empty owner, custody entry missing required fields,
    custody without `re_derivation_basis`. Non-zero exit.
  - `WARN` — event-driven obligations missed: no reaffirmation after a custody transfer,
    unconfirmed re-derivation, missing `review_triggers`.
  - `INFO` — weak signal only: pure time decay of `last_reaffirmed` (`--max-age-days`,
    default 180). Deliberately not WARN: reaffirmation is required on custody transfer and
    when a review trigger fires, not on a calendar (`../core/glossary.md`, Reaffirmation).

  ```bash
  python3 specs/schemas/tenure_check.py specs/examples [--max-age-days 180]
  python3 specs/schemas/tenure_check.py --self-test   # clean/dirty fixtures under fixtures/
  ```

  CI runs the self-test and then scans `specs/examples`.

## How to Validate

The same checks run in CI (`.github/workflows/validate.yml`):

```bash
yamllint -c .yamllint specs/**/*.yaml
python3 specs/schemas/tenure_check.py --self-test
python3 specs/schemas/tenure_check.py specs/examples
bash .github/scripts/validate_docs.sh
```
