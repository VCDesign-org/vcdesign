# VCDesign Maturity Profile

## Status

Normative reference for organizational diagnosis.

---

## 目的

VCDesign Maturity Profile は、組織・システムが AI ガバナンスの各層において
どの段階にあるかを診断するためのフレームワークである。

**2種類の使い方：**
- **簡易診断（外部説明・経営層向け）**: 共通4段階で5層を評価する
- **精密診断（内部設計・改善向け）**: 層別ルーブリックで具体的な証拠と欠損を特定する

---

## 共通成熟度スケール

全5層に共通して使用できる4段階のスケール。

| Level | 意味 | VCDesign 内の対応 |
|---|---|---|
| **Unstructured** | 構造なし。設計上の対応物が存在しない | チャプターなし、境界未定義 |
| **Defined** | 文書・設計上は存在するが、実運用では強制されていない | taxonomy に境界記述あり、チャプター存在 |
| **Enforced** | 実運用で機能しており、違反時に制御が発動する | Judgment Closure + RCA 稼働、policies.yaml 適用 |
| **Governed** | 監査・改善・再評価まで回っており、継続的に維持される | metrics.yaml 発火、supervisor ループ + 定期レビュー稼働 |

### 簡易診断の出力例

```
Organization: XYZ Corp — AI Platform Team

Model Layer:            Enforced
Agent Layer:            Defined
Responsibility Layer:   Unstructured
Time Layer:             Defined
Human Sovereignty:      Enforced
```

**読み方:** 最も低いレベルがシステム全体のガバナンス限界を決める。
上の例では Responsibility Layer が Unstructured であるため、
他層がいかに整っていても組織全体として Unstructured に近い状態と判断する。

---

## 層別ルーブリック（精密診断）

各層の Unstructured〜Governed の判定基準。

---

### Layer 1: Model Layer
*AI が解釈・分析・提案をおこなう層（Semantic Loop）*

#### Unstructured
**状態:** AI モデルの役割と制約が設計上存在しない

Required evidence (none expected):
- なし

Failure signals:
- AI 出力がそのまま最終判断として扱われている
- モデルの利用範囲が定義されていない
- AI の自信度が表示されていない

Blocking conditions:
- AI が final decision を出力している
- AI の出力に Judgment Proposal のラベルがない

---

#### Defined
**状態:** AI の役割・許可・禁止が文書化されているが、実運用では強制されていない

Required evidence:
- AI の allowed / forbidden リストが存在する
- LLM が Semantic Loop に配置されていることが文書化されている

Failure signals:
- 文書はあるが実装に反映されていない
- レビュープロセスが形骸化している

Blocking conditions:
- AI が物理制御または最終責任を担っている

---

#### Enforced
**状態:** IDG が稼働し、AI 出力が Judgment Closure を通過してから実行に移る

Required evidence:
- IDG（Interface Determinability Gate）が B1・B4 境界に実装されている
- AI 出力が Judgment Proposal としてログされている
- Judgment Closure の記録が存在する

Failure signals:
- IDG が迂回されるケースがある
- AI 推薦の自動承認率が高い（`ai_overreach` メトリクス参照）

Blocking conditions:
- Judgment Closure なしに AI 出力が実行されるパスが存在する

---

#### Governed
**状態:** Semantic Loop の品質が継続的に観測・改善されている

Required evidence:
- `delta_detection_quality` / `semantic_interpretation_quality` メトリクスが定期観測されている
- モデル更新・切替時に再判断プロセスが存在する
- AI 利用の採用理由が記録されている（high_impact 操作）

Failure signals:
- メトリクスが収集されているが改善アクションに繋がっていない

Blocking conditions:
- なし（Enforced の blocking 条件が残っていないこと前提）

---

### Layer 2: Agent Layer
*AI がツールを実行し外部システムへ作用する層*

#### Unstructured
**状態:** Agent の実行境界が定義されておらず、何をしていいかが不明

Required evidence (none expected):
- なし

Failure signals:
- Agent がアクセスできるリソースの範囲が宣言されていない
- Agent の実行ログが存在しない
- 「とりあえず動かしてみる」から始まっている

Blocking conditions:
- Agent が本番データを無制限に読み書きできる
- 実行に対する責任者が不在

---

#### Defined
**状態:** 実行境界・許可操作・禁止操作が文書化されている

Required evidence:
- Agent ごとに実行スコープ（読み取り可/書き込み可/禁止）が宣言されている
- Multi-agent 構成の場合、優先順位と衝突解決ルールが文書化されている

Failure signals:
- 文書はあるが実装（API スコープ、権限設定）と乖離している
- 境界が「全体的に許可」から始まっており制限が後付け

Blocking conditions:
- 実行境界の宣言なしに Agent が本番環境へ作用している

---

#### Enforced
**状態:** Execution Gate が稼働し、Agent の計画が policy チェックを通過してから実行される

Required evidence:
- policy チェックの記録が Agent 実行ログに残っている
- halt_owner が Agent 起動前に指定されている
- 不可逆操作前に責任者承認が取得されている

Failure signals:
- `missing_execution_gate` メトリクスが発火している
- `missing_halt_owner` メトリクスが発火している
- Agent 障害時の停止手順が実際には動作しない

Blocking conditions:
- halt_owner が存在しない Agent が本番稼働している
- Policy チェックを迂回する実行パスが存在する

---

#### Governed
**状態:** Agent の動作が継続的に観測・監査され、スコープ逸脱が検知される

Required evidence:
- `autonomous_scope_expansion_detected` / `policy_bypass_attempt_detected` メトリクスが観測されている
- Agent のスコープが定期的に再審査されている
- Multi-agent 間の責任境界が明文化されており、審査される

Failure signals:
- メトリクスは収集されているが逸脱への対応が遅い

Blocking conditions:
- なし（Enforced の blocking 条件が解消されていること前提）

---

### Layer 3: Responsibility Layer
*誰が何を保持し、誰が最終判断するかの構造*

#### Unstructured
**状態:** 責任の所在が不明。誰も明示的に持っていない

Required evidence (none expected):
- なし

Failure signals:
- 問題が起きたとき「誰の責任か」が事後に議論される
- `owner_missing` メトリクスが常時発火している
- 判断の承認者が「チーム全体」

Blocking conditions:
- human final decider が存在しない
- 責任経路が追跡不能

---

#### Defined
**状態:** Owner・final decider が文書上は定義されている

Required evidence:
- チャプターごとに owner が指定されている
- final decider が人間ロールまたは人物で指定されている

Failure signals:
- Owner が実際には機能していない（`owner_missing` シグナル）
- 文書上の owner と実際の意思決定者が異なる

Blocking conditions:
- AI が final decider として記録されている

---

#### Enforced
**状態:** 承認ログ・halt owner・エスカレーション経路が実運用で必須化されている

Required evidence:
- 判断ごとに承認トレースが記録されている
- halt owner が各操作・Agent に対して named かつ operational
- エスカレーション経路が定義されており、実際に使われた記録がある

Failure signals:
- `owner_conflict` が繰り返し発生している
- Defer が owner・期限なしで積み上がっている（`defer_stagnation`）

Blocking conditions:
- Traceable な責任経路がない
- halt owner が unstaffed または untested

---

#### Governed
**状態:** 責任メトリクスが定期観測され、過負荷・枯渇への対応手順が存在する

Required evidence:
- `operator_overload` / `defer_stagnation` メトリクスが定期観測されている
- 責任の再配分手順（supervisor によるレビュー）が定期的に実施されている
- 責任移転が明示的なハンドシェイクで記録されている

Failure signals:
- メトリクスは収集されているが責任配分が改善されていない

Blocking conditions:
- なし（Enforced の blocking 条件が解消されていること前提）

---

### Layer 4: Time Layer
*時間スケールの分離と、速いループが遅いループを上書きしないための構造*

#### Unstructured
**状態:** 時間スケールの分離が設計されておらず、実行系が判断系を上書きする

Required evidence (none expected):
- なし

Failure signals:
- 自動化処理が方針を暗黙的に書き換えている
- 「昨日の判断」が永続的に有効とみなされている
- Resolution に有効期限がない

Blocking conditions:
- Physical loop が Value Loop の制約を自律的に変更できる

---

#### Defined
**状態:** 時間スケールと再評価サイクルが文書化されている

Required evidence:
- 各ループ（Physical/Semantic/Value/Responsibility）の時間スケールが文書化されている
- Resolution に next_review_at が設定されている

Failure signals:
- 文書化されているが実際の運用で守られていない
- 期限切れの Resolution が放置されている

Blocking conditions:
- Fast loop が slow loop の目標を承認なしに変更できる

---

#### Enforced
**状態:** Temporal Separation が実装されており、ループ間の越境が制御されている

Required evidence:
- Fast loop から slow loop への書き込みに明示的なゲートが存在する
- Resolution の有効期限が強制される
- 価値目標の変更に Value Loop の審査が必要

Failure signals:
- `autonomous_scope_expansion_detected` が temporal 文脈で発火している
- 期限切れ Resolution が自動延長されている

Blocking conditions:
- Temporal Separation が実装されていない経路で fast loop が slow loop を変更できる

---

#### Governed
**状態:** 時間的な逸脱が観測・是正され、Judgment Decay が制度化されている

Required evidence:
- 時間経過による判断の陳腐化（Judgment Decay）が定期的にスキャンされている
- 期限切れ Resolution が supervisor によりレビューされている
- 季節・環境変動による Reference Drift が監視されている

Failure signals:
- Decay スキャンは実施されているが再判断に繋がっていない

Blocking conditions:
- なし（Enforced の blocking 条件が解消されていること前提）

---

### Layer 5: Human Sovereignty Layer
*人間が最終的に介入・停止・説明できる主権構造*

#### Unstructured
**状態:** 人間の介入経路が存在しない、または機能しない

Required evidence (none expected):
- なし

Failure signals:
- 緊急停止の手順が存在しない、または誰も知らない
- AI の判断を人間がキャンセルできない
- 「止め方がわからない」システムが本番稼働している

Blocking conditions:
- 任意の操作を人間が halt できない
- 緊急停止が AI の協力を必要とする

---

#### Defined
**状態:** 人間介入の経路が文書化されているが、実際には未検証

Required evidence:
- 緊急停止手順が文書化されている
- human override の操作手順が存在する

Failure signals:
- 手順が実際に試されたことがない
- Override 後の復帰手順が不明確

Blocking conditions:
- Override が機能的に実装されていない（書類上のみ）

---

#### Enforced
**状態:** Override と halt が実運用で機能することが検証されており、人間が実際に行使できる

Required evidence:
- halt drill の成功記録が存在する
- 部分的な Agent 障害時にも halt が機能することが確認されている
- Override 後の安全復帰手順が存在し、訓練されている
- `halt_readiness` メトリクスが観測されている

Failure signals:
- Drill が実施されていない
- Override が技術的には可能だが現場が使い方を知らない

Blocking conditions:
- Degraded 状態（部分障害）で override が機能しない
- halt_owner が operational でない

---

#### Governed
**状態:** 主権行使の記録が蓄積され、介入の質が継続的に改善されている

Required evidence:
- override 行使の記録とその後のレビューが存在する
- `human_override_recovery_quality` メトリクスが追跡されている
- 主権の範囲（何を止められるか）が定期的に審査されている
- 説明責任（外部責任説明）が high_impact 操作に対して完備されている

Failure signals:
- Override 記録はあるが改善に繋がっていない

Blocking conditions:
- なし（Enforced の blocking 条件が解消されていること前提）

---

## 介入ガイド

| 現在のレベル | 優先アクション |
|---|---|
| **Unstructured** | blocking 条件を即時解消。chapter 作成・owner 指定・halt path 確立が最初のステップ |
| **Defined** | 文書と実装の乖離を特定し、最も高リスクな境界から Enforced へ引き上げる |
| **Enforced** | metrics を導入し、発火パターンを観測する。改善サイクルを設計する |
| **Governed** | 継続維持。新しい章・Agent・境界が追加されるたびに同じプロファイルで再診断する |

---

## 診断の使い方

1. 各層を独立して評価する（最初は簡易診断で十分）
2. 最低レベルの層を特定する → そこが組織のガバナンス限界
3. blocking 条件を優先的に解消する
4. Enforced→Governed の移行は metrics 導入が前提

診断結果の出力形式：

```yaml
profile:
  organization: <name>
  evaluated_at: <iso8601>
  evaluator: <human role>

  layers:
    model:      Defined
    agent:      Unstructured
    responsibility: Defined
    time:       Unstructured
    human_sovereignty: Enforced

  limiting_layer: agent  # 最低レベルの層
  blocking_conditions:
    - agent: "No halt_owner for production agent"
    - time:  "Physical loop can overwrite Value objectives without gate"

  recommended_action: Fix blocking conditions in Agent and Time layers before advancing other layers.
```
