# VCDesign 仕様群

VCDesign（Value Continuity Design）は、
[Value Continuity](https://github.com/value-continuity/value-continuity) を
**判断と責任** の面から実装する方法論です。

Value Continuity とは、*変化や失敗があっても、次の価値を生み出せる状態を継続すること* です。
その中心原則である **Value Asymmetry Principle** は、*upside は伝播可能にする。downside は伝播させない。* です。
これらの定義は正本にあり、ここでは再定義しません。
VCDesign が定めるのは、誰が、何を根拠に、6つの判断のどれで閉じ、残ったものを誰が持ち続けるか、です。

> VCDesignは法則であり、VC-ADはその現在技術水準における具体化である。

これらの仕様は、人間や高度な自動化支援が **設計支援・判断支援・コード生成** に利用できる
**実行可能な設計言語** です。
判断の所在と責任の帰属が説明できない状態で、実装を開始してはなりません（**実装境界事前定義**）。

### VCDesign Authority 宣言

VCDesign v2 の現行 authority は次の3ファイルです。

- core/core.yaml
- core/policies.yaml
- core/metrics.yaml

`core/axioms.yaml`（A1〜A5）は適合判定の起点です。schema は記録の形、patterns と protocols は core を実装する構造、
catalog は領域の事例集です。

## 芯の6つ

| 芯 | VCDesign が定めること |
| --- | --- |
| Δ | 宣言した期待（前提と価値）との差。向きを持つ。Negative Δ は伝播させず、Positive Δ は伝播可能にする |
| 責任 | owner、人間の最終判断者、担当交代をまたぐ継続保有（点の責任は開始、線の責任が維持） |
| 境界 | 損失は止め（containment）、根拠は通し（basis_flow）、結論は確かめ直す（revalidation） |
| 判断 | 6語（Proceed / Expand / Limit / Reframe / Defer / Retire）だけを使い、判断ゲート1つで閉じる |
| 宣言 | 案件ごとに、残すもの（保有者付き）、広がりの兆候、最大損失、可逆性、依存先 |
| 指標 | 5原則（残す・見つける・閉じる・試す・伝える）の順に並ぶ芯の17件 |

AI 統制（AI は最終責任を持たない、LLM の配置、時間定数の分離、エージェントの実行ゲート）は、
VCDesign 固有の **拡張** として芯の外に置いています。

## どこから読むか

全体像は **[Specification Map](specs/map.md)** を参照してください。

1. [Value Continuity](https://github.com/value-continuity/value-continuity) — 思想
2. [specs/core/implementation.md](specs/core/implementation.md) — VCDesign での実装と、v1 からの移行表
3. [specs/core/core.yaml](specs/core/core.yaml)、[policies.yaml](specs/core/policies.yaml)、[metrics.yaml](specs/core/metrics.yaml) — authority
4. [specs/examples/](specs/examples/) — 適用例4本

## ディレクトリ構造

- **[specs/core/](specs/core/)** — authority、axioms、schema、実装ガイド、用語集
- **[specs/protocols/](specs/protocols/)** — 判断を閉じ、コミットに昇格させる手順
- **[specs/patterns/](specs/patterns/)** — Boundary、RCA、IDG
- **[specs/catalog/](specs/catalog/)** — chapters と責任境界 B1〜B17
- **[specs/examples/](specs/examples/)** — 適用例
- **[specs/validation/](specs/validation/)** — 適合チェック
- **[docs/](docs/)** — 説明枠と解釈の読み物（authority ではない）

## ステータス

**v2.0**。v1 とは互換性がありません。読み替えは `specs/core/implementation.md` の移行表を参照してください。

## ライセンス

本リポジトリは **MIT License** です。`LICENSE` を参照してください。
