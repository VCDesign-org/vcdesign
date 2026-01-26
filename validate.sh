#!/bin/bash
# Validate specs against their schemas using ajv-cli

set -e

echo "Validating judgment-closure.yaml..."
npx ajv -s specs/schemas/judgment-closure.schema.json -d specs/protocols/judgment-closure.yaml

echo "Validation Passed!"
