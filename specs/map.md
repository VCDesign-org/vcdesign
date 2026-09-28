# VCDesign Specification Map

## VCDesign Authority Declaration

VCDesign v2 は、[Value Continuity](https://github.com/value-continuity/value-continuity)
を「判断と責任」の面から実装する方法論である。定義と原則の正本は Value Continuity にあり、ここでは再定義しない。

VCDesign の現行 authority は次の3ファイルである。

- core/core.yaml
- core/policies.yaml
- core/metrics.yaml

axioms.yaml は適合判定の起点、schema は記録の形、boundary pattern は core を実装する構造である。
catalog は領域の事例集であり、芯ではない。

## 1. Core — 芯

- **[Core](core/core.yaml)**: 章・責任・Δ（向き付き）・判断6語・ライフサイクル・宣言・境界の規則。
- **[Axioms](core/axioms.yaml)**: A1〜A5。いずれかに反する実装は、他を満たしていても非適合。
- **[Policies](core/policies.yaml)**: 判断ゲート1つ（5原則の順のレビュー、判断ごとの必須項目、停止条件）、責任・説明・停止の規則、拡張としての AI 統制。
- **[Metrics](core/metrics.yaml)**: 5原則を骨格にした芯の指標17件と、拡張としての AI 統制・運用適合の指標。
- **[Case Schema](core/schema_case.yaml)** / **[Log Schema](core/schema_log.yaml)**: 案件の宣言（Upside / Downside / Continuity）と、判断の根拠の記録。
- **[Implementation](core/implementation.md)**: 読解補助。Value Continuity の各要素を VCDesign のどこで実装しているかの対応表と、v1 からの移行表。
- **[Glossary](core/glossary.md)**: 用語集。

## 2. Pattern

- **[Boundary](patterns/boundary-pattern.yaml)**: VCDesign 唯一の構造パターン。guard（越境を pass / deny / unknown で判定）、containment（損失を止める）、basis_flow（根拠を通す）、revalidation（結論を確かめ直す）、tenure（境界を持ち続ける）、external_crossing（組織をまたぐ越境）。

## 3. Catalog — 領域の事例集

- **[Chapters](catalog/chapters/)**: 価値・意味・責任が時間とともにずれていく典型（C1 目的のずれ、C2 自動化の負担、C3 信頼と責任の侵食、C4 現実とのずれ）。
- **[Boundary Registry](catalog/boundaries/registry.md)** / **[Taxonomy](catalog/boundaries/taxonomy.md)**: 責任境界 B1〜B17 の正本と、事例。

## 4. Examples

- [Point vs Line Improvement](examples/point-vs-line-improvement.md): 業務変更で消える改善と、残るものを持つ改善。広がりの兆候、判断ゲート、Expand の宣言更新。
- [Custody Handover](examples/custody-handover.md): 担当交代をまたいで判断が保有され続ける様子（[機械可読の案件](examples/custody-handover-case.yaml)）。
- [Factory Operations Agent](examples/factory-agent-safe-loop.md): 製造業の AI エージェント。物理と意味のループの分離と、停止の設計。

## 5. Validation and tools

- **[Conformance](validation/conformance.md)**: v2 の適合チェック（axioms と Review Output に沿う）。
- **[Schemas](schemas/)**: 案件の責任空白を検査する tenure_check など。

## Outside specs

- [docs/ai-extension.md](../docs/ai-extension.md): AI 拡張の外部向け説明枠（4つのループ、5層、12原則）。authority ではない。
