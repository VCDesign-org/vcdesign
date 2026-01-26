# VCDesign Schemas

This directory contains machine-readable schemas to validate the specifications.
These schemas act as "guardrails" to ensure the specs maintain a consistent structure, but they are not the specification itself (the Prose/YAML in `../core` is authoritative).

## Available Schemas
- **[Judgment Closure](judgment-closure.schema.json)**: Validates `../protocols/judgment-closure.yaml`.

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
