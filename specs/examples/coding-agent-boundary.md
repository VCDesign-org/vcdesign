# Use Case: AI Coding Agent Governance

## 概要

LLM を利用したコーディング Agent（コード生成・テスト実行・PR 作成・デプロイ操作を
連鎖的に実行するもの）を組織で導入する際の VCDesign 適用例。

対象：開発チーム・プラットフォームチームが AI コーディング支援を本番フローに組み込む場面。

---

## 典型的なシナリオ

```
ユーザー指示 → Agent が仕様解釈
            → コード生成
            → テスト実行
            → PR 作成
            → (場合により) マージ・デプロイ実行
```

各ステップで Agent は外部システム（リポジトリ・CI・本番環境）へ作用する。
ステップが連鎖するほど、最初の判断誤りが下流で増幅される。

---

## 発火する主要境界

| B# | 境界 | コーディング Agent での発火条件 |
|----|------|-------------------------------|
| B1 | Human ↔ AI Judgment | 生成コードの採用判断が暗黙承認になる |
| B5 | Decision ↔ Action | PR レビュー = 実行承認として扱われる |
| B6 | Responsibility Assignment | 「Agent が書いたコード」の責任者が不明 |
| B11 | Risk Acceptance | セキュリティリスクを誰も明示的に引き受けていない |
| B17 | Impact ↔ Accountability | Agent の影響範囲（デプロイ先）が担当者の権限を超える |

---

## VCDesign 設計決定

### 1. 実行スコープの宣言（Agent Layer）

Agent 起動前に実行境界を明示する。

```yaml
agent_scope:
  id: coding-agent-prod
  read_allowed:
    - repository/*
    - ci_logs/*
  write_allowed:
    - repository/feature-branches/*
    - pull_requests/*
  write_forbidden:
    - repository/main
    - repository/release/*
    - production_deployments/*
  halt_owner: <engineering-lead-role>
```

`main` へのマージとデプロイは Agent の実行境界外とする。
これは B17 への対応：Agent の影響範囲を権限の範囲内に制限する。

---

### 2. Judgment Closure の配置（B1・B5）

コード採用はAgentの出力を Judgment Proposal として扱い、
人間による Judgment Closure を必須化する。

```
Agent Output (Proposal)
  → IDG: 生成コードは「確定的」か？（テスト未通過・依存関係未確認 → Indeterminate）
  → Judgment Closure: レビュワーが ACCEPTED / DENIED を明示
  → Resolution Handshake: 承認者・スコープ・有効期限を記録
  → 実行（PR マージ）
```

「PR を開いた = 承認した」は B5 違反（Decision ↔ Action の間のゲートがない）。
PR オープンと Judgment Closure は別のアクションとして設計する。

---

### 3. 責任者の明示（B6）

Agent が生成したコードの責任者を設計上決定する。

```yaml
responsibility:
  owner: <requesting-engineer>       # 指示を出した人間
  final_decider: <engineering-lead>  # マージの最終承認者
  supporters:
    - <agent-system>                 # 提案者（責任は持たない）
    - <code-reviewer>
```

Agent は supporters に位置づけ、owner は指示を出した人間に固定する。
「Agent が書いたから責任の所在が不明」という状態を設計上禁止する。

---

### 4. セキュリティリスクの明示的引き受け（B11）

Agent が生成するコードに含まれうるリスク（依存関係の脆弱性・認証処理等）を
Judgment Closure の中で明示的に扱う。

```yaml
judgment_proposal:
  content: "Agent generated authentication handler"
  risk_flags:
    - "External library not pinned to version"
    - "Input validation not verified"
  required_from_approver:
    - "Explicit acceptance of listed risks OR request for revision"
```

「リスクがあることを知った上で承認した」という記録を残す。

---

### 5. Halt 設計（Human Sovereignty Layer）

Agent が連鎖実行中に halt できる設計にする。

```yaml
halt_conditions:
  - condition: "Test failure rate > 20%"
    action: pause_and_notify_halt_owner
  - condition: "Scope boundary crossed"
    action: immediate_halt
  - condition: "halt_owner manual trigger"
    action: immediate_halt_any_state

halt_owner: <engineering-lead-role>
halt_path: "Slack command / dashboard button / CLI override"
```

「Agent が途中まで実行した状態」での安全な中断と復帰手順を事前に設計する。

---

## Maturity Profile（典型的な導入初期）

```yaml
profile:
  context: AI Coding Agent — Initial Deployment

  layers:
    model:            Enforced    # LLM は提案のみ、Judgment Closure あり
    agent:            Defined     # スコープ文書化済みだが Execution Gate 未実装
    responsibility:   Defined     # Owner 定義済みだが承認トレース未記録
    time:             Unstructured # Resolution に有効期限なし
    human_sovereignty: Defined    # Halt 手順文書化済みだが未訓練

  limiting_layer: time
  blocking_conditions:
    - agent: "Execution gate not yet enforced in CI pipeline"
    - time:  "No expiry on code review judgments — stale approvals remain valid"

  recommended_action: >
    Implement execution gate in CI before expanding agent scope.
    Add expiry to all Judgment Closures (recommended: 7d for feature work).
```

---

## 「Governed」に到達した状態

- Agent のすべての本番操作に policy チェック記録が存在する
- コードレビューが Judgment Closure として記録され、有効期限がある
- 月次でスコープ逸脱メトリクスをレビューし、Agent の境界を更新する
- Halt drill を四半期ごとに実施し、`halt_readiness` を確認する
- 「なぜこの Agent を採用したか」の採用理由が記録されており、更新される

---

## 関連仕様

- `core/decision-posture.yaml` — commit/defer の選択（CI 失敗時は commit して止める）
- `patterns/idg-pattern.yaml` — コード生成出力の不確実性ゲート
- `protocols/judgment-closure.yaml` — PR 承認を Judgment Closure として設計
- `boundaries/taxonomy.md` — B1, B5, B6, B11, B17
- `validation/vcdesign-maturity-profile.md` — 診断フレームワーク
