# VCDesign Downside Containment Model: 上に開き、下を閉じる

## Status

**Design principle / Reading aid — not authority.**

このドキュメントは、VCDesign が扱う「下振れ」を
**裾を切る（打ち切る）設計**として定義し、その 4 機構と既存仕様の対応を固定する設計原則である。

仕様上の権威は `core.yaml`（`downside_containment`）/ `policies.yaml` / `metrics.yaml` にある。
本文書で導入する概念の規範的な実体は
`schema_case.yaml`（v0.3 containment フィールド群）、
`patterns/boundary-pattern.yaml`（v1.2.0 containment / revalidation）、
`metrics.yaml`（containment_metrics）にあり、本文書はその読み方を固定する。

既存文書との役割分担:

- `value-tenure-model.md` — 責任の**時間軸上の性質**（点か線か）を定義する文書
- `value-asymmetry-model.md` — 上に開き下を閉じる、価値の非対称を定義する親文書
- `downside-containment-model.md`（本文書）— 親文書の下側。失敗の**広がり方**（足し算か掛け算か）を定義する文書

---

## 1. なぜこの区別が必要か

成果や損失の分布は、生成の仕組みで形が決まる。

| 生成の仕組み | 分布の形 | 裾 |
|---|---|---|
| 独立した要因が**足し算**で効く | 正規分布に近い | 薄い（極端な事象はほぼ起きない） |
| 要因が**掛け算**で効く、失敗が**連鎖・伝播**する、依存が**一点に集まる** | 対数正規・べき乗に近い | 厚い（極端な事象が現実的な頻度で起きる） |

システムがつながり、AI が判断を連鎖させるほど、下振れは後者の形になる。
一つの誤判断が下流で増幅され、共通の依存先を通って複数の区画に同時に波及する。

VCDesign の根にある問い ——「その初動しか取れない設計だったのではないか」—— は、
裾の事象そのものではなく、**裾の事象が内部で増幅される構造**を設計の責任として扱う問いである。

---

## 2. 上に開き、下を閉じる

価値の複利や接続による正のフィードバック（上振れ）は、開いたままにしておきたい。
下振れの裾だけを切りたい。この非対称を一つの設計判断として扱う。

上下を同時に扱う全体像は親文書 `value-asymmetry-model.md` に定義する。
本文書はその**下を閉じる側**の詳細である。上振れ（業務が変わっても残るもの、裾の兆候）は
親文書と `core.yaml value_accumulation` を参照。

目標は「正規分布にすること」ではなく「**裾を切ること**」である。
外から来る裾（自然災害・突発故障）は消せない。
制御できるのは、それが内部でどこまで増幅・伝播するかだけである。

---

## 3. 4 つの機構

べき乗的な裾は「掛け算」と「連鎖」から生まれるので、封じ込めはそれを足し算に戻す操作になる。

| 機構 | 何を切るか | 宣言する場所 | 観測する metric |
|---|---|---|---|
| **isolate** 結合を切る | 区画をまたぐ伝播 | `schema_case.failure_domain` / `boundary-pattern.containment` | `blast_radius_exceeded`（区画外伝播） |
| **cap** 上限の宣言 | 損失の大きさ | `schema_case.blast_radius` / `resolution_object.blast_radius` | `blast_radius_undeclared` / `blast_radius_exceeded` |
| **revalidate** 連鎖のリセット | 上流の誤りの掛け算 | `schema_case.upstream_basis_refs` / `boundary-pattern.revalidation` | `transitive_trust` |
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
- **single owner と single point**: owner が 1 人であること（A5）は義務。
  判断経路や依存先が一点に集まることは検知の対象。両者は矛盾しない。

---

## 5. 未整備の事項

- 判断の選択肢の語彙（decision posture / 長期判断の姿勢 / decision_size / action / VMS）が複数系統あり、
  上限の宣言をどれに紐づけるかは未統一。本版では schema_case（案件）単位で宣言する。
- `schemas/tenure_check.py` に相当する containment の検査ツールは未実装。
  宣言項目（本版）を先に固め、検査は後から追加する。
- VC-AD（architecture-yaml-protocols リポジトリ）側の境界定義ファイル構成との対応は本リポジトリの範囲外。
