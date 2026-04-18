# Use Case: Factory Operations Agent — Safe Loop Design

## 概要

製造・工場運用環境において AI Agent を導入する際の VCDesign 適用例。

センサーデータを解釈し、異常検知・設備制御提案・保全スケジューリングを
おこなう Agent を想定する。物理系（Physical Loop）と AI 推論（Semantic Loop）の
境界設計が最重要課題となる。

対象：製造 DX チーム、OT（Operational Technology）エンジニア、保全担当者。

---

## 典型的なシナリオ

```
センサーデータ（温度・振動・電流等）
  → AI が異常パターンを検出
  → 異常スコアと原因仮説を生成
  → 対応提案（速度下げ / 停止 / 保全スケジュール）を出力
  → (場合により) 制御系への直接パラメータ送信
  → 現場オペレーターへの通知
```

製造環境の特性：判断が遅れると物理的被害・人身事故・生産損失が発生する。
逆に誤判断による不要停止は生産コストに直結する。
**速さと安全の両方を設計で担保しなければならない。**

---

## 製造 Agent 固有のリスク

| リスク | 製造特有の文脈 |
|---|---|
| Physical Loop への直接介入 | AI が制御パラメータを直接変更すると安全インターロックが無効化される可能性 |
| 速度圧力と停止コスト | 「止めると損失が出る」という圧力が defer を困難にする |
| 現場知識のブラックボックス化 | ベテランの経験がAI推論に暗黙的に置き換えられ、引き継げなくなる |
| 時間的整合性の欠如 | 短期センサー異常と長期機器劣化を同じ優先度で扱ってしまう |
| 責任の現場押し付け | AI が提案し、現場オペレーターが「承認」させられる構造 |

---

## 発火する主要境界

| B# | 境界 | 製造 Agent での発火条件 |
|----|------|------------------------|
| B2 | Automation ↔ Manual | 自動化が現場判断負荷を増大させる |
| B3 | System ↔ Reality | センサー値が現実の機器状態を反映していない |
| B6 | Responsibility Assignment | AI 提案を「承認」する現場オペレーターに実質的責任が押し付けられる |
| B9 | Expertise | ベテランの暗黙知が AI に置き換えられ、判断根拠が失われる |
| B10 | Temporal | 即時異常と長期劣化傾向が区別されない |
| B15 | Design ↔ Emergence | 想定外の機器挙動が「AI が処理できなかった事象」として片付けられる |

---

## VCDesign 設計決定

### 1. Physical Loop と Semantic Loop の厳格な分離（最重要）

AI は Physical Loop（制御系）を直接操作しない。

```
[Physical Loop]
  センサー → PLC/DCS → アクチュエーター
  ↑ AI はここに直接アクセスしない

[境界: Discrete-to-Continuous Boundary]
  ← AI 提案がここを越える場合は必ずゲートを通過する

[Semantic Loop]
  センサーデータ → AI 解釈 → 異常候補 → 対応提案
                                         ↓
                              オペレーター判断（Judgment Closure）
                                         ↓
                              制御系への指示（Resolution Handshake）
```

`core.yaml / adaptive_loop_model` の `physical_loop.forbidden_components: llm_as_direct_controller` の実装。

---

### 2. 異常の深刻度による判断分岐（Decision Posture の実装）

すべての異常を同じフローで処理しない。深刻度と時間緊急性で posture を事前設計する。

```yaml
anomaly_response_design:

  immediate_safety_risk:
    examples:
      - "Temperature exceeds safety threshold"
      - "Pressure beyond design limit"
      - "Vibration indicates imminent bearing failure"
    posture: commit
    owner: on_site_operator
    rationale: >
      Physical loop の安全を守るため、現場オペレーターが
      証拠確認後に即時 commit する。停止の遅延は物理損傷・
      人身事故リスクを高める。
    required_before_commit:
      - sensor_reading_verified_not_faulty
      - operator_physically_present_or_reachable
      - action_within_operator_authority
    log_required: true

  operational_degradation:
    examples:
      - "Efficiency dropping but within safe range"
      - "Wear pattern suggests maintenance in 2 weeks"
    posture: defer
    owner: maintenance_engineer
    rationale: >
      安全上のリスクはないため、次の保全サイクルまで
      責任者への移送と計画的対応が可能。
    next_review_at: "+7d"

  ambiguous_signal:
    examples:
      - "Anomaly score elevated but cause unclear"
      - "Multiple competing hypotheses"
    posture: reconsider
    owner: senior_engineer
    rationale: >
      追加情報収集と専門家による再評価が必要。
      AI の仮説は参考情報として提示するが、
      確定判断は証拠が揃うまで保留。
    idg_required: true   # Interface Determinability Gate を通す
```

---

### 3. Sensor ↔ Reality の検証（B3 対応）

センサー値が現実を反映しているかを判断の前提として明示する。

```yaml
sensor_validity_check:
  required_before_ai_interpretation: true
  checks:
    - sensor_last_calibrated_within: "30d"
    - no_sensor_fault_flag_active: true
    - cross_validation_with_adjacent_sensors: recommended

  failure_handling:
    sensor_fault_detected:
      action: halt_ai_interpretation
      posture: defer
      reason: >
        B3 違反の可能性。センサー値の信頼性が確認されるまで
        AI 解釈を停止し、現場確認に切り替える。
      owner: maintenance_engineer
```

「センサーが正常」を前提として AI が判断を出すと、
障害の本当の原因（センサー故障）を見逃す。

---

### 4. 現場知識の保全（B9 対応）

ベテランの判断を AI に置き換えるのではなく、AI が提案・ベテランが評価する構造を維持する。

```yaml
expertise_preservation:
  principle: >
    AI は候補仮説と証拠を提示する。
    経験ある技術者が文脈・機器履歴・感覚的情報を加えて最終判断する。

  judgment_log_requirements:
    - "AI hypothesis presented: <cause_candidate>"
    - "Human assessment: <what the engineer observed or added>"
    - "Final judgment: <decided_by: engineer_name>"
    - "Evidence basis: <sensor data + human observation>"

  anti_pattern: >
    「AI が 0.87 の確信度で bearing failure と判断したため承認」
    → これは B1 + B9 の同時違反。
    承認者は evidence を独立に評価していなければならない。
```

---

### 5. 時間スケールの分離（B10 対応）

即時異常と長期劣化傾向を別のループとして設計する。

```yaml
temporal_separation:
  physical_loop:
    timescale: "ms to seconds"
    role: "安全インターロック・即時停止"
    ai_role: "リアルタイム異常スコア提供（参考情報のみ）"
    ai_cannot: "制御パラメータを直接変更する"

  semantic_loop:
    timescale: "minutes to hours"
    role: "異常解釈・原因仮説・対応提案"
    ai_role: "ログ解析・パターン検出・提案生成"
    human_required: "Judgment Closure before action"

  value_loop:
    timescale: "weeks to months"
    role: "保全方針・設備投資判断・AI モデルの妥当性評価"
    ai_role: "傾向分析・コスト試算（参考情報）"
    human_required: "方針変更は技術管理者の判断"
```

---

### 6. Halt 設計（Human Sovereignty Layer）

物理系では「止め方」が最も重要な設計要素。

```yaml
halt_design:
  halt_owner: on_site_operator    # 現場に必ず在席している役割

  halt_triggers:
    - "Operator manual trigger (physical button or SCADA interface)"
    - "AI interpretation halted by IDG (indeterminate signal)"
    - "Sensor validity check failed"
    - "Scope boundary crossed by AI recommendation"

  halt_execution:
    - Step 1: AI 推論・提案の送信を停止
    - Step 2: 現在の推奨アクションをキャンセル（未実行のもの）
    - Step 3: Physical Loop は安全状態へ（AI とは独立に機能）
    - Step 4: オペレーターに制御を明示的に戻す
    - Step 5: 停止理由をログに記録

  critical_note: >
    Physical Loop の安全インターロックは AI の halt とは独立して機能する。
    AI が停止しても物理的安全機構は動作し続けることを設計上保証する。
```

---

### 7. 現場負荷の設計（B2 対応）

AI 導入が現場オペレーターの判断負荷を増大させないことを設計上確認する。

```yaml
operator_load_check:
  before_deployment:
    question: "AI 導入後、オペレーターが対応すべきアラート数は増えるか？"
    if_yes:
      - AI の感度を調整する
      - アラートの優先度分類を再設計する
      - 「AI が処理する」アラートと「人間が判断する」アラートを明確に分離する

  metric: operator_overload
  threshold: >
    オペレーター1名あたりの Judgment Closure 要求が
    シフトあたり X 件を超えた場合、AI の自律範囲を拡大するのではなく
    フィルタリング精度を改善する。
```

---

## Maturity Profile（製造業典型例）

```yaml
profile:
  context: Factory Operations Agent — Process Manufacturing

  layers:
    model:            Defined      # AI は提案のみ、但し IDG 未実装
    agent:            Unstructured # AI から制御系への直接パスが存在する
    responsibility:   Defined      # 現場責任者は定義済み、承認トレースなし
    time:             Partial      # 即時異常と長期劣化の分離が不完全
    human_sovereignty: Enforced   # 物理的停止ボタンは機能、AI 停止経路は別途必要

  limiting_layer: agent
  blocking_conditions:
    - agent: "Direct path exists from AI recommendation to PLC parameter write"
    - agent: "No halt_owner named for AI interpretation system (physical halt owner exists separately)"

  recommended_action: >
    CRITICAL: Remove direct AI-to-PLC path immediately.
    All AI outputs must pass through operator Judgment Closure before physical actuation.
    Name halt_owner for AI system (separate from physical safety officer).
```

---

## 「Governed」に到達した状態

- AI と Physical Loop の間に Discrete-to-Continuous Boundary が実装されており、直接パスが存在しない
- すべての設備制御提案に Judgment Closure 記録があり、オペレーター名・証拠・リスク承認が含まれる
- `operator_overload` メトリクスがシフトごとに観測され、AI のアラート粒度が調整されている
- センサー較正履歴と AI 解釈の妥当性が月次でレビューされている
- Halt drill（AI 停止・Physical Loop 継続）が定期的に実施されている
- ベテランオペレーターの判断履歴がログとして蓄積され、AI モデルの改善に繋がっている

---

## 関連仕様

- `core/core.yaml` — adaptive_loop_model（Physical/Semantic/Value/Responsibility の分離）
- `core/decision-posture.yaml` — commit（即時安全対応）/ defer（計画的保全）/ reconsider（曖昧信号）
- `patterns/idg-pattern.yaml` — 曖昧センサーシグナルのゲート
- `policies.yaml` — boundary_safety.discrete_to_continuous_boundary
- `boundaries/taxonomy.md` — B2, B3, B6, B9, B10, B15
- `validation/vcdesign-maturity-profile.md` — 診断フレームワーク
