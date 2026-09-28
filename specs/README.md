# VCDesign Specifications

VCDesign v2 は、[Value Continuity](https://github.com/value-continuity/value-continuity) を
「判断と責任」の面から実装する方法論です。全体像は **[Specification Map](map.md)** を参照してください。

## Directory Structure

- **[core/](core/)** — 芯。authority は `core.yaml`、`policies.yaml`、`metrics.yaml`。ほかに `axioms.yaml`、`schema_case.yaml`、`schema_log.yaml`、読解補助の `implementation.md`、`glossary.md`。
- **[patterns/](patterns/)** — core を実装する構造（Boundary）。
- **[catalog/](catalog/)** — 領域の事例集（chapters、責任境界 B1〜B17）。芯ではない。
- **[examples/](examples/)** — 適用例3本。
- **[validation/](validation/)** — 適合チェック。
- **[schemas/](schemas/)** — 検査ツール。

## Status

v2.0。v1 とは互換性がありません。読み替えは `core/implementation.md` の「v1 からの移行」を参照してください。
