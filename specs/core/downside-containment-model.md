# VCDesign Downside Containment Model: 増幅を切る

## Status

**Design principle / Reading aid — not authority.**

このドキュメントは、Value Continuity 正本の5原則のうち「閉じる」を VCDesign がどう実装しているかを、
**増幅を切る設計**の 4 機構と既存仕様の対応として固定する設計原則である。
Negative Δ（`core.yaml delta_definition.polarity.negative`）の扱い（局所化 → 緩和 → 必要なら閉じる）の詳細にあたる。

仕様上の権威は `core.yaml`（`downside_containment`）/ `policies.yaml` / `metrics.yaml` にある。
本文書で導入する概念の規範的な実体は
`schema_case.yaml`（v0.3 containment フィールド群）、
`patterns/boundary-pattern.yaml`（v1.2.0 containment / revalidation）、
`metrics.yaml`（containment_metrics）にあり、本文書はその読み方を固定する。

既存文書との役割分担:

- `value-continuity-implementation.md` — 正本の5原則と VCDesign の要素の対応をまとめる親文書
- `value-tenure-model.md` — 「残す」「伝える」のうち時間方向（点の責任と線の責任）
- `downside-containment-model.md`（本文書）— 親文書のうち「閉じる」。失敗の**広がり方**（増幅されるか、その場に留まるか）を扱う文書

---

## 1. なぜこの区別が必要か

連鎖・再利用・集中・フィードバックがあると、一つの結果が次の結果を生む。
一つの失敗が次の失敗を生む経路があるとき、極端な下振れは無視できなくなる。

システムがつながり、AI が判断を連鎖させるほど、そうした経路は増える。
一つの誤判断が下流で増幅され、共通の依存先を通って複数の区画に同時に波及する。

本文書は結果の出方を予測しない。扱うのは**増幅機構の設計**である。

VCDesign の根にある問い ——「その初動しか取れない設計だったのではないか」—— は、
極端な事象そのものではなく、**極端な事象が内部で増幅される構造**を設計の責任として扱う問いである。

---

## 2. 本文書が扱う範囲

上に開き下を閉じるという非対称そのものは正本の Value Asymmetry Principle であり、
VCDesign での実装の全体像は親文書 `value-continuity-implementation.md` にある。
本文書は**下を閉じる側**だけを扱う。上振れ（残るもの、広がりの兆候、Positive Δ）は
親文書と `core.yaml value_accumulation` を参照。

封じ込めは失敗の伝播だけを対象とし、根拠や残るものの流れは止めない
（`boundary-pattern.yaml` の `containment` と `basis_flow` の区別）。

目標は「**増幅を切ること**」である。
外から来る事象（自然災害・突発故障）は消せない。
制御できるのは、それが内部でどこまで増幅・伝播するかだけである。

---

## 3. 4 つの機構

極端な下振れは、一つの失敗が次の失敗を生む仕組みから起きるので、封じ込めはその増幅を切る操作になる。

| 機構 | 何を切るか | 宣言する場所 | 観測する metric |
|---|---|---|---|
| **isolate** 結合を切る | 区画をまたぐ伝播 | `schema_case.failure_domain` / `boundary-pattern.containment` | `blast_radius_exceeded`（区画外伝播） |
| **cap** 上限の宣言 | 損失の大きさ | `schema_case.blast_radius` / `resolution_object.blast_radius` | `blast_radius_undeclared` / `blast_radius_exceeded` |
| **revalidate** 連鎖のリセット | 上流の誤りの増幅 | `schema_case.upstream_basis_refs` / `boundary-pattern.revalidation` | `transitive_trust` |
| **deconcentrate** 集中を避ける | 共通原因による同時故障 | `schema_case.depends_on` / `containment.shared_dependencies` | `dependency_concentration` / `judgment_concentration` |

加えて、全機構の前提として**可逆性**を記録する（`schema_case.reversibility`）。
可逆な判断は失敗を後から小さくできるので、上限の宣言は不可逆な判断で必須、可逆な判断では任意とする。

### 停止条件

`policies.yaml` の長期判断ゲートでは、致命的な下振れ（`fatal_downside`）は
**責任者の有無にかかわらず停止する**。
責任者がいることは下振れを許容する理由にならない。
責任者の不在は別の停止条件（`downside_without_owner`）として扱う。

---

## 4. 用語の対応

### 同じ軸を別の層で呼んでいる用語

| 軸 | 判断基準（core） | ゲート手順（policies） | 停止条件（policies） | 指標（metrics） | 記録（schema_case） |
|---|---|---|---|---|---|
| 下振れ | `survive_downside` | `downside_review` | `fatal_downside` | `downside_survivability` | `blast_radius` |
| 可逆性 | `reversible` | `reversibility_assessed` / `reversibility_declared` | `*_and_irreversible` | `reversibility_score` | `reversibility` |

### 混同しやすい区別

- **scope と max_loss**: scope は影響の**範囲**、max_loss は損失の**大きさの上限**。
  `resolution_object.scope` は後者を代替しない。
- **re-derivation と revalidation**:
  `re_derivation_basis`（tenure）は担当交代をまたぐ**時間方向**の再導出、
  `revalidation`（boundary）は境界をまたぐ**空間方向**の再検証。
  Re-derivation Layer（動作を業務上の意味・権限・根拠に翻訳する層）とも別概念である。
  三つとも「伝える」の実装である（`glossary.md`「Re-derivation Layer」）。
- **境界の意味**: 本文書の境界は、判断の受け渡し点（boundary-pattern）と障害区画（failure_domain）を指す。
  責任境界（B1–B17）や `boundary_mediation` との区別は `glossary.md`「Boundary（曖昧さ回避）」を参照。
- **single owner と single point**: owner が 1 人であること（A5）は義務。
  判断経路や依存先が一点に集まることは検知の対象。両者は矛盾しない。

---

## 5. 未整備の事項

- 上限の宣言は schema_case（案件）単位で行う。宣言の更新（Expand / Limit）は
  `core.yaml decision_vocabulary` と `schema_log.decision.blast_radius_update` で記録する。
- `schemas/tenure_check.py` に相当する containment の検査ツールは未実装。
  宣言項目（本版）を先に固め、検査は後から追加する。
- VC-AD（architecture-yaml-protocols リポジトリ）側の境界定義ファイル構成との対応は本リポジトリの範囲外。
