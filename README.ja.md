# VCDesign 仕様群

VCDesign（Value Continuity Design）は、
「どう作るか」ではなく、作られた後の価値を
時間の中でどう守り抜くかを設計するための仕様群です。

> VCDesignは法則であり、VC-ADはその現在技術水準における具体化である。

## VCDesign とは何か

VCDesign は、**高度な自動化を含むシステム**において、
**判断 (Judgment)**、**責任 (Responsibility)**、そして
**時間 (Time / Operations)** の連続性を失わないための設計仕様です。
Core用語: **実装境界事前定義**（実装開始前に境界を意図的に定義すること）。

Core の開始条件として、判断の所在と責任の帰属が説明できない状態で
実装を開始してはなりません。

システム規模が拡大しても、
個々の判断がどこで閉じられ、
誰が責任を引き受け、
運用の時間の中でどのように変化していくのかを
明示的に構造化することを目的としています。

これらの仕様は、単なる読み物ではありません。
人間や高度な自動化支援が**設計支援・判断支援・コード生成**に利用できる、
**実行可能な設計言語**として定義されています。

### VCDesign Authority 宣言
VCDesignの現行authorityは以下で構成される
- core/core.yaml
- core/policies.yaml
- core/metrics.yaml
- core/axioms.yaml（A1〜A5：すべての仕様の基底となる公理）
- core/decision-posture.yaml（defer/commit/reconsider/abandon の規範的定義）
- patterns（RCL等）は「Coreへの適用構造」
- legacy配下は「歴史的ドキュメントであり現行仕様ではない」

### VCDesign の中核原則
VCDesign は、価値の連続性を目的として、章と責任の遷移によってシステムを構造化するための開発 OS です。
現実のAI運用では、これは Physical / Semantic / Value / Responsibility の4ループを時間スケールごとに分離し、責任統治の下で接続する構造として読まれます。
LLMは主としてSemantic Loopに配置され、成長はモデル性能の増加ではなく、責任制約下での運用整合の改善として定義されます。

#### 基本原則
- **責任非消失原則**: 責任は常にどこかに存在しなければならない。
- **説明可能性原則**: すべての判断は人間に説明可能でなければならない。
- **AI 非責任原則**: AI は支援するが、責任は負わない。
- **Δ 駆動原則**: システムは前提条件からの逸脱（Δ）を検出して作動する。
- **点と線の責任原則（Gate / Tenure）**: 承認の一点（点の責任:「今これは正しいか」）は責任の開始であって維持ではない。価値の継続には、担当交代・無人の自律運用・時間経過を生き延びる継続保有（線の責任）が必要である。自律化が進むほど、線の責任は不要になるのではなく重要になる。[specs/core/value-tenure-model.md](specs/core/value-tenure-model.md) を参照。

## どこから読むか (Where to start?)
全体の俯瞰図については **[Specification Map](specs/map.md)** を参照してください。

以下の順序で読むことを推奨します。
1. **[specs/core/](specs/core/)** (Authority): なぜこの設計が必要か、何を守るべきか。
   - **[ai-adaptive-loop-model.md](specs/core/ai-adaptive-loop-model.md)**: Core / Policies / Metrics が実際のAI運用ループにどうつながるかを読みやすく説明した補助文書。
   - **[agent-era-model.md](specs/core/agent-era-model.md)**: 2026年以降のAIエージェント統治に向けた5層フレームと12原則。
2. **[specs/protocols/](specs/protocols/)** (How / Operations): 判断をいつ閉じ、どう責任を引き渡すか。
3. **[specs/chapters/](specs/chapters/)** (When): 時間軸の中で、どの設計がいつ必要になるか。
4. **[specs/examples/](specs/examples/)** (Applied): 具体的な適用例 — AIコーディングエージェント、セキュリティエージェント、工場オペレーションエージェントなど。

## ディレクトリ構造 (Directory Structure)

* **[specs/core/](specs/core/)**: **The Authority.** VCDesign の最小限かつ不可避な定義。
* **[specs/protocols/](specs/protocols/)**: **The Procedures.** 判断を閉じ、責任を引き渡すための標準的な手順。
* **[specs/patterns/](specs/patterns/)**: **The Structures.** コアを実装するための参照パターン（境界構造、RCA、IDG、RCLなど）。
* **[specs/chapters/](specs/chapters/)**: **The Narratives (The "When").** フェーズやバージョンではなく、判断や責任の時間的変化（When）を扱う設計単位。
* **[specs/boundaries/](specs/boundaries/)**: **The Boundary Taxonomy.** 責任境界の正規レジストリ（B1〜B17）とケーススタディ。
* **[specs/glossary/](specs/glossary/)**: 用語集（Legacy / RCL / Core の対応表を含む）。
* **[specs/validation/](specs/validation/)**: 適合性ケース、アンチパターン、組織診断のための **[Maturity Profile](specs/validation/vcdesign-maturity-profile.md)**。
* **[specs/examples/](specs/examples/)**: 具体的な適用例 — 最小ライフサイクル、LLM変更承認ワークフロー、3つのエージェント統治ユースケース。

詳細な全体像は **[Specification Map](specs/map.md)** を正とします。上記は概要です。

## ステータス (Status)
Core 仕様は **Stable**（安定）です。
Protocols と Patterns は **Stable** ですが、拡張可能です。

## ライセンス
本リポジトリは **MIT License** です。`LICENSE` を参照してください。
