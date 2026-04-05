#!/usr/bin/env bash

set -euo pipefail

check_contains() {
  local file="$1"
  local pattern="$2"
  local message="$3"

  if ! grep -Eq "$pattern" "$file"; then
    echo "$message"
    exit 1
  fi
}

check_legacy_notice() {
  local root="$1"
  local pattern="$2"
  local label="$3"
  shift 3

  local missing=()
  local file
  while IFS= read -r file; do
    local skip=false
    local excluded
    for excluded in "$@"; do
      if [[ "$file" == "$excluded" ]]; then
        skip=true
        break
      fi
    done
    if [[ "$skip" == true ]]; then
      continue
    fi
    if ! grep -Eq "$pattern" "$file"; then
      missing+=("$file")
    fi
  done < <(find "$root" -name "index.html" | sort)

  if ((${#missing[@]} > 0)); then
    printf 'Missing legacy warning in %s pages:\n' "$label"
    printf '  %s\n' "${missing[@]}"
    exit 1
  fi
}

check_contains README.md "Authority Declaration" \
  "Authority Declaration not found in README.md"
check_contains README.md "core/core.yaml" \
  "core/core.yaml not referenced in README.md"
check_contains README.md "core/policies.yaml" \
  "core/policies.yaml not referenced in README.md"
check_contains README.md "core/metrics.yaml" \
  "core/metrics.yaml not referenced in README.md"

check_contains specs/map.md "Authority Declaration" \
  "Authority Declaration not found in specs/map.md"
check_contains specs/map.md "core/core.yaml" \
  "core/core.yaml not referenced in specs/map.md"
check_contains specs/map.md "core/policies.yaml" \
  "core/policies.yaml not referenced in specs/map.md"
check_contains specs/map.md "core/metrics.yaml" \
  "core/metrics.yaml not referenced in specs/map.md"

check_contains site/en/index.html "Authority Declaration" \
  "Authority Declaration not found in site/en/index.html"
check_contains site/en/index.html "core/core.yaml" \
  "core/core.yaml not referenced in site/en/index.html"
check_contains site/en/index.html "core/policies.yaml" \
  "core/policies.yaml not referenced in site/en/index.html"
check_contains site/en/index.html "core/metrics.yaml" \
  "core/metrics.yaml not referenced in site/en/index.html"

check_contains site/ja/index.html "Authority (Declaration|宣言)" \
  "Authority heading not found in site/ja/index.html"
check_contains site/ja/index.html "core/core.yaml" \
  "core/core.yaml not referenced in site/ja/index.html"
check_contains site/ja/index.html "core/policies.yaml" \
  "core/policies.yaml not referenced in site/ja/index.html"
check_contains site/ja/index.html "core/metrics.yaml" \
  "core/metrics.yaml not referenced in site/ja/index.html"

check_legacy_notice site/en/legacy "Historical Document Notice" "en" \
  "site/en/legacy/yaml/index.html" \
  "site/en/legacy/validation/index.html"

check_legacy_notice site/ja/legacy "歴史的ドキュメントのお知らせ" "ja" \
  "site/ja/legacy/yaml/index.html" \
  "site/ja/legacy/validation/index.html"
