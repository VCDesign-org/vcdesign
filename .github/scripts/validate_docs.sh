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

check_legacy_structure() {
  local root="$1"
  local notice_pattern="$2"
  local superseded_pattern="$3"
  local lineage_pattern="$4"
  shift 4

  local invalid=()
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

    if ! python3 - "$file" "$notice_pattern" "$superseded_pattern" "$lineage_pattern" <<'PY'
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
notice_pattern = sys.argv[2]
superseded_pattern = sys.argv[3]
lineage_pattern = sys.argv[4]
text = path.read_text()

m = re.search(r'<div class="warning-box">(.*?)</div>\s*(<p><em>.*?</em></p>)\s*(<p><em>.*?</em></p>)', text, re.S)
if not m:
    raise SystemExit(1)

warning_inner = m.group(1)
if "<p><em>" in warning_inner:
    raise SystemExit(1)

if not re.search(notice_pattern, warning_inner, re.S):
    raise SystemExit(1)
if not re.search(superseded_pattern, m.group(2), re.S):
    raise SystemExit(1)
if not re.search(lineage_pattern, m.group(3), re.S):
    raise SystemExit(1)
PY
    then
      invalid+=("$file")
    fi
  done < <(find "$root" -name "index.html" | sort)

  if ((${#invalid[@]} > 0)); then
    printf 'Invalid legacy intro structure in pages:\n'
    printf '  %s\n' "${invalid[@]}"
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

check_legacy_structure \
  site/en/legacy \
  "Historical Document Notice" \
  "This concept has been superseded by the Core \\+ Policies \\+ Metrics model" \
  "This document represents the conceptual lineage that led to the current model" \
  "site/en/legacy/yaml/index.html" \
  "site/en/legacy/validation/index.html"

check_legacy_notice site/ja/legacy "歴史的ドキュメントのお知らせ" "ja" \
  "site/ja/legacy/yaml/index.html" \
  "site/ja/legacy/validation/index.html"

check_legacy_structure \
  site/ja/legacy \
  "歴史的ドキュメントのお知らせ" \
  "本概念は現在、Core \\+ Policies \\+ Metrics モデルに統合されています" \
  "このドキュメントは現在のモデルに至る概念的系譜を表しています" \
  "site/ja/legacy/yaml/index.html" \
  "site/ja/legacy/validation/index.html"
