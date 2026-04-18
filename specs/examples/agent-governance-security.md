# Use Case: Security Agent Governance

## 概要

AI を活用したセキュリティ運用 Agent（脅威検知・アラート分類・インシデント対応・
自動遮断を連鎖的に実行するもの）を組織で運用する際の VCDesign 適用例。

いわゆる「Mythos 型」：大量のログ・アラートを LLM が解釈し、
対応アクション（IP 遮断・アカウント停止・通知送信・チケット起票等）まで
自律的に実行しようとする Agent を想定する。

対象：SOC（Security Operations Center）チーム、セキュリティプラットフォームチーム。

---

## 典型的なシナリオ

```
大量セキュリティアラート
  → Agent がアラートを分類・優先度付け
  → 高リスク判定 → 自動対応候補を生成
  → (場合により) IP 遮断・アカウント停止・外部通知を自動実行
  → インシデントチケット起票
  → アナリストへのエスカレーション（または省略）
```

このシナリオにおいて VCDesign が問うのは：
「誰が遮断の責任を持ち、誰が止められるか」である。

---

## セキュリティ Agent 固有のリスク

通常の業務 Agent と比較して、セキュリティ Agent は以下の点で統治が難しい。

| リスク | 理由 |
|---|---|
| 影響の即時性 | 遮断・停止は即座に現実へ作用し、ロールバックが難しい |
| 誤検知のコスト | 正常ユーザーや重要インフラを誤遮断する可能性 |
| 判断の高速化圧力 | 「速く対応しなければ被害が拡大する」という圧力が commit を急がせる |
| 責任の拡散 | SOC・法務・経営が関与するインシデントでは誰が最終判断者か不明になりがち |
| ブラックボックス化 | 「AI が危険と判断した」だけでは B14（Accountability ↔ Blame）が成立しない |

---

## 発火する主要境界

| B# | 境界 | セキュリティ Agent での発火条件 |
|----|------|-------------------------------|
| B1 | Human ↔ AI Judgment | AI の脅威判定が人間の確認なく「確定」として扱われる |
| B6 | Responsibility Assignment | インシデント対応の責任者が SOC/法務/経営に拡散する |
| B11 | Risk Acceptance | 遮断による副作用リスクを誰も明示的に引き受けていない |
| B14 | Accountability ↔ Blame | 誤検知時に「AI が判断した」として責任が隠蔽される |
| B17 | Impact ↔ Accountability | Agent の遮断影響が担当アナリストの権限を超える |

---

## VCDesign 設計決定

### 1. 影響水準による実行境界の階層化（Agent Layer）

すべての対応アクションを影響水準で分類し、実行境界を設計する。

```yaml
agent_scope:
  id: security-response-agent

  autonomous_allowed:           # Execution Gate なしで実行可（低影響・可逆）
    - create_incident_ticket
    - add_alert_tag
    - notify_analyst_slack

  gated_execution:              # 責任者承認後に実行（中影響）
    - rate_limit_ip
    - send_external_notification
    - escalate_to_management

  human_decision_required:      # Agent は提案のみ、実行不可（高影響・不可逆）
    - block_ip_permanently
    - suspend_user_account
    - notify_regulatory_body
    - engage_legal_team

  halt_owner: <soc-lead-role>
```

「自動対応できる」と「自動対応してよい」は別問題。
高影響操作は Agent の実行境界外として設計する。

---

### 2. 脅威判定の Judgment Closure 設計（B1・B14）

AI の脅威スコアは Judgment Proposal であり、Judgment Closure ではない。

```
AI Alert Score: 0.94 (HIGH)  ← Judgment Proposal
  → IDG: 証拠は「確定的」か？
       - Indeterminate → アナリストへエスカレーション（posture: defer）
       - Determinable  → アナリストが ACCEPTED/DENIED を明示
  → Judgment Closure 記録:
       decided_by: <analyst-name>
       decided_at: 2026-04-19T14:32:00Z
       evidence_reviewed: [log_ref_001, pcap_ref_002]
       risk_accepted: "Blocking may affect VPN users in APAC region"
  → Resolution Handshake → 実行
```

「AI スコアが 0.9 超なので自動遮断」は B1 + B14 の同時違反。
アナリストが証拠を見て判断した記録が B14 の成立条件。

---

### 3. インシデント対応の責任構造（B6・B17）

大規模インシデントでは責任が拡散しやすい。事前に責任構造を設計する。

```yaml
incident_responsibility:
  tier_1_response:              # アナリストが独立して判断できるスコープ
    owner: <soc-analyst>
    scope: "rate_limit, ticket, notify_internal"
    authority_limit: "Impact confined to single system"

  tier_2_response:              # SOC リードの承認が必要
    owner: <soc-lead>
    scope: "block_ip, suspend_account"
    authority_limit: "Impact may affect multiple users or systems"

  tier_3_response:              # 経営層・法務の判断が必要
    owner: <ciso>
    final_decider: <executive-team>
    scope: "regulatory_notification, legal_engagement, public_disclosure"
    authority_limit: "External impact or regulatory obligation"
```

Agent の対応提案が tier を跨ぐ場合は自動的に上位 owner へエスカレーション。

---

### 4. 誤検知時の責任トレース（B14）

「AI が間違えた」ではなく「誰がその判断を承認したか」を記録する。

```yaml
judgment_log:
  incident_id: INC-2026-0419-001
  ai_proposal:
    score: 0.94
    recommended_action: block_ip
    target: 203.0.113.42
  human_closure:
    decided_by: analyst-tanaka
    decided_at: 2026-04-19T14:35:00Z
    decision: ACCEPTED
    note: "Confirmed C2 pattern in packet capture. Risk accepted: may affect shared NAT."
  outcome:
    result: false_positive_confirmed_post_incident
    review_required: true
    review_owner: soc-lead
```

誤検知が判明した場合、「AI の失敗」ではなく「analyst-tanaka の判断を支援した AI が誤った提案をした」として記録する。
これにより懲罰的にならず、改善サイクルが回る（B14 の対処例）。

---

### 5. 高速化圧力への対応（Physical Loop vs Responsibility Loop）

「今すぐ止めないと被害が拡大する」という状況は physical loop の圧力。
しかし遮断は responsibility loop の判断が必要な操作。

VCDesign の posture 設計：

```yaml
high_velocity_incident_posture:
  when: "Attack actively ongoing, data exfiltration detected"
  posture: commit
  rationale: >
    Physical loop の安定を守るため、tier_2 owner が証拠確認後に即時 commit。
    但し commit の前提条件:
      - tier_2 owner が在席・承認済み
      - 対象 IP のスコープが tier_2 authority 内
      - 決定ログへの即時記録
  not_acceptable: >
    Agent が「攻撃継続中」を理由に自律的に commit すること。
    速度は commit の理由になるが、authority 委譲の理由にはならない。
```

これは `decision-posture.yaml` の commit ポスチャー定義の実装例：
「物理ループの安定が halting より重要なとき、authority 内で即時 commit」。

---

## Maturity Profile（SOC 典型例）

```yaml
profile:
  context: Security Response Agent — SOC Environment

  layers:
    model:            Enforced    # 脅威スコアは Proposal として扱われる
    agent:            Defined     # 影響水準分類は文書化、Gate 未実装
    responsibility:   Defined     # tier 構造は定義済み、承認トレース未徹底
    time:             Unstructured # インシデント判断に有効期限の概念がない
    human_sovereignty: Enforced   # halt 手順あり、drill 実施済み

  limiting_layer: time
  blocking_conditions:
    - agent: "high_impact operations lack enforcement gate in current tooling"
    - time:  "No expiry on deferred incidents — some sit unreviewed for weeks"

  recommended_action: >
    Enforce execution gate for tier_2+ operations in SOAR platform.
    Add mandatory review cycle (72h) for all deferred incidents.
```

---

## 「Governed」に到達した状態

- すべての高影響対応に Judgment Closure 記録が存在し、アナリスト名・証拠・リスク承認が含まれる
- `authority_confusion_detected` メトリクスがゼロを維持している
- 誤検知のレビューが改善サイクル（AI モデルの再評価・境界の更新）に繋がっている
- インシデント対応の責任 tier が定期的に審査・更新されている
- Halt drill が四半期ごとに実施され、`halt_readiness` が Governed レベルを維持している

---

## 関連仕様

- `core/decision-posture.yaml` — commit（高速対応）と defer（エスカレーション）の使い分け
- `patterns/idg-pattern.yaml` — 脅威スコアの不確実性ゲート
- `protocols/judgment-closure.yaml` — アナリスト判断の記録
- `core/axioms.yaml` — A3（AI は最終責任を持たない）、A5（責任は希少資源）
- `boundaries/taxonomy.md` — B1, B6, B11, B14, B17
- `validation/vcdesign-maturity-profile.md` — 診断フレームワーク
