# VCDesign for Agent Era: 外部説明モデル

## Status

**Reading aid — not authority.**

このドキュメントは、2026年時点の AI エージェント進化に対して VCDesign がどう読まれるべきかを
外部説明可能な形で整理したものである。

仕様上の権威は `core.yaml` / `policies.yaml` / `metrics.yaml` にある。
本文書はそれらの reading aid であり、それらを上書きしない。

既存の `ai-adaptive-loop-model.md` との役割分担:
- `ai-adaptive-loop-model.md` — 4ループで**現実運用の構造**を読む文書
- `agent-era-model.md`（本文書）— Agent 時代の**外部説明フレーム**と 12 原則を整理する文書

---

## 1. なぜ今、Agent Era を整理するか

モデルの性能向上は、統治の問題を自動解決しない。

- 推論能力が増しても、誰が責任を持つかは変わらない
- ツール実行能力が増しても、境界の設計は消えない
- 自律度が上がるほど、停止条件と権限範囲の明示が重要になる

VCDesign の中心命題「AIとは、非連続な知能を連続系へ安全接続するための境界設計問題である」
（`core.yaml / final_definition`）は、モデル単体の時代よりも Agent の時代においてより強く成立する。

---

## 2. Model と Agent の違い

| 観点 | Model | Agent |
|------|-------|-------|
| 作用範囲 | 出力テキスト・分類・推論 | ツール実行・外部システム書き込み・連鎖操作 |
| 時間軸 | 単一推論ターン | 複数ステップ・長時間動作 |
| 境界の数 | 入力/出力の2面 | 操作ごとに境界が発生 |
| 責任経路 | 最終判断者が1層上 | 判断者が複数ステップに分散するリスク |
| 停止の難度 | 低（推論を止めるだけ） | 高（実行途中の安全な中断が必要） |

**核心:** Agent は Model の延長ではなく、境界設計問題の次元が増した構造体である。
したがって VCDesign の Boundary Taxonomy（B1–B17）は Agent においてより多く同時に発火する。

---

## 3. 5層構造（外部説明フレーム）

この5層は、VCDesign の4ループを外部説明用に再構成したものである。
運用の権威は4ループ（`core.yaml / adaptive_loop_model`）にある。

```
┌──────────────────────────────────────┐
│  Layer 5: Human Sovereignty Layer    │  人間が最終的に介入・停止・説明できる主権
│  ← 対応: Responsibility Loop         │
├──────────────────────────────────────┤
│  Layer 4: Time Layer                 │  時間スケールの分離と遅いループの保護
│  ← 対応: Temporal Separation原則     │
├──────────────────────────────────────┤
│  Layer 3: Responsibility Layer       │  誰が何を保持し説明するかの構造
│  ← 対応: Responsibility Loop + B6   │
├──────────────────────────────────────┤
│  Layer 2: Agent Layer                │  実行境界・ツール制御・multi-agent 協調
│  ← 対応: Semantic Loop + Boundary   │
├──────────────────────────────────────┤
│  Layer 1: Model Layer                │  推論・解釈・提案（出力のみ、実行なし）
│  ← 対応: Semantic Loop              │
└──────────────────────────────────────┘
```

**読み方:** 下位レイヤーの能力は、上位レイヤーの統治構造なしに拡大してはならない。
Agent Layer (L2) の実行権限は Responsibility Layer (L3) の明示的な境界定義が先行する。

---

## 4. 12 Principles for Governable AI Agents

### Principle 1: Capability is not Authority / 能力は権限ではない

モデルが高性能であることは、意思決定権を持つ理由にならない。
推論・コーディング・検索などの実行能力は、承認権限とは別である。

`core.yaml` の制約 `ai_cannot_be_final_decider` および
公理 A1（責任は消えてはならない）がこれを支える。

---

### Principle 2: Action Requires Boundary / 行動には境界が必要である

AI が外部へ作用する場合、必ず範囲を定義する。

- 読み取りのみ可
- 提案のみ可
- 本番更新禁止
- 金額上限あり

境界なき Agent は事故源である。
`policies.yaml / boundary_safety` の `discrete_to_continuous_boundary` がこれを義務化する。

---

### Principle 3: Responsibility Must Be Attached / すべての行動に責任接点を持たせる

AI の出力・実行には必ず、オーナー・承認者・管理者のいずれかが紐づく必要がある。
責任者不在の自律は組織では採用できない。

公理 A1 および `policies.yaml / responsibility_rules.invariants` を参照。

---

### Principle 4: Human Finality Must Remain / 最終決定権は人間に残す

AI が提案・分析・優先順位付けをしても、
採用・却下・保留・例外承認の最終決定権は人間に残す。

`core.yaml / responsibility_model` の `final_decider_must_be_human` がこれを invariant として定める。

---

### Principle 5: Logs are Structural Memory / ログは記録ではなく構造記憶である

ログは監査用途だけではない。なぜその判断になったか、何を見て行動したか、
いつ方針が変わったか、を未来へ引き継ぐ組織記憶である。

`core.yaml / schema_log.yaml` および `policies/temporal-governance.md`
（責任状態は append-only）がこれを規定する。

---

### Principle 6: Continuity Beats Local Optimization / 局所最適より価値継続を優先する

単発で成果を出す AI より、再利用・保守・引継ぎができ信頼が積み上がる AI の方が価値が高い。

VCDesign の `growth_definition`（`metrics.yaml`）はモデル能力の増大ではなく
責任制約下での運用整合の改善を成長と定義することでこれを制度化する。

---

### Principle 7: Uncertainty Must Surface / 不確実性は隠してはならない

AI が迷っている時は、自信度低・情報不足・判断不能・要確認を明示しなければならない。
確信した誤答より、保留の方が安全である。

IDG Pattern（`patterns/idg-pattern.yaml`）が不確実性を隠さないためのゲート機構を定める。
B1（Human ↔ AI Judgment）および B4（Data ↔ Meaning）と直結する。

---

### Principle 8: Time is a First-Class Constraint / 時間軸は第一級制約である

同じ判断でも、今すぐ必要・今週でよい・来月見直し・年次計画では最適解が変わる。
AI は速度だけでなく時間粒度を理解する必要がある。

`core.yaml / adaptive_loop_model / temporal_separation` の
`fast_loops_must_not_autonomously_rewrite_slow_loop_constraints` がこれを規則化する。
B10（Temporal Boundary）を参照。

---

### Principle 9: Escalation is a Feature / エスカレーションは失敗ではない

AI が人間へ戻すことは能力不足ではない。それは設計された安全機構である。
法務判断・倫理判断・高額承認・緊急停止は、戻せることが正しい。

`decision-posture.yaml` の `defer` ポスチャーと `policies.yaml / haltability` がこれを規範化する。

---

### Principle 10: Multi-Agent Needs Constitution / 複数 Agent には憲法が必要である

Agent 同士が連携する場合、優先順位・衝突解決・権限分離・共通禁止事項が必要になる。
無秩序な Multi-Agent は内部競合を起こす。

`policies.yaml / ai_governance` の `agent_execution_requires_explicit_boundary` がこれを義務化する。
B6（Responsibility Assignment）と B5（Decision ↔ Action）が境界点として機能する。

---

### Principle 11: Replaceability Preserves Sovereignty / 交換可能性が主権を守る

特定ベンダー・特定モデルに依存しすぎると、価格支配・方針変更・API 停止・品質変動に従属する。
モデル交換可能性は企業主権を守る設計である。

これは B11（Risk Acceptance）および B17（Impact ↔ Accountability）の設計判断として現れる。

---

### Principle 12: Explainability and Accountability

> **Principle 12a: Internal opacity is tolerable**
> 内部不可解性は許容される
>
> **Principle 12b: External accountability is mandatory**
> 外部責任説明は必須である

AI システムの内部推論が完全に人間に理解できなくなることは、
高性能モデルの現実として一部許容される。

しかし以下の説明能力は失ってはならない:

| 説明項目 | 意味 |
|----------|------|
| 採用理由 | なぜこの AI/Agent を使う決定をしたか |
| 実行履歴 | 何をいつ実行したか |
| 責任経路 | 誰がその判断を承認・保持しているか |
| 停止条件 | どうなったら止まるか、誰が止められるか |

高影響領域では governance trace（監査可能な責任証跡）が必須となる。
影響水準に応じた説明要求の具体化は `policies.yaml / explainability.levels` を参照。

`every_chapter_must_be_explainable`（`core.yaml / invariants`）および
`policies.yaml / explainability` がこれを制度化する。
B14（Accountability ↔ Blame）と直結する。

---

## 5. Related Boundaries

Agent Era の議論は以下の境界と直接接続する:

| B# | 境界 | Agent Era での主な発火条件 |
|----|------|--------------------------|
| B1 | Human ↔ AI Judgment | エージェントが自律的に判断を閉じる |
| B5 | Decision ↔ Action | 判断と実行の間のゲートが消える |
| B6 | Responsibility Assignment | マルチエージェントで責任が拡散する |
| B10 | Temporal | 長時間動作で「今の判断」が永続する |
| B16 | Model ↔ Reality | エージェントの行動が学習データを汚染する |
| B17 | Impact ↔ Accountability | エージェントの影響範囲が権限を超える |

---

## 6. 能力競争の次に来るもの

VCDesign for Agent Era は、高性能 AI を作る思想ではなく、
**高性能 AI を社会で継続利用可能にする思想**である。

能力競争の次に来るのは、統治競争である。

統治とは禁止ではなく、使い続けられる構造を設計することである。
