# VCDesign Implementation of Value Continuity

## Status

**Reading aid — not authority.**

Value Continuity の定義、Value Asymmetry Principle、5原則、Δ、Decision は正本
（[value-continuity/value-continuity](https://github.com/value-continuity/value-continuity)）にある。
VCDesign の規範は `core.yaml` / `policies.yaml` / `metrics.yaml` にある。
この文書は、正本の各要素を VCDesign がどの仕組みで実装しているかを対応づけるだけで、新しい規範を置かない。

---

## 1. 位置づけ

VCDesign は、Value Continuity を **判断と責任** の面から実装する方法論である。
正本が問う「価値が次の価値を生み、失敗してもその活動を続けられるか」に対して、
VCDesign は「誰が、何を根拠に、どの判断で閉じ、何を保有し続けるか」を記録し、検査する。

| 正本の要素 | VCDesign での実装 |
| --- | --- |
| Δ（期待との差） | `core.yaml delta`：前提（precondition）と価値（value_intent）を基準線に、向き（negative / positive）を付けて観測する |
| Value Asymmetry Principle | `core.yaml delta.asymmetry_rules`、`patterns/boundary-pattern.yaml` の containment と basis_flow |
| Decision（6語） | `core.yaml decision`、`policies.yaml judgment_gate`、`schema_log.yaml decision` |
| Review Output | `policies.yaml judgment_gate.review` と `schema_log.yaml decision.basis` |
| 5原則 | 下の2章。`metrics.yaml core_metrics` の principle も同じ順に並ぶ |

---

## 2. 5原則ごとの実装

### 残す

- **residual_assets**：業務・担当・技術が変わっても残るものを、保有者（holder）付きで宣言する。空の案件は点の改善として扱う。
- **点の責任と線の責任**：承認の一点（Gate：「今これは正しいか」）は責任の開始であって、維持ではない。価値を残すには、担当交代・無人の自律運用・時間経過を生き延びる継続保有（Tenure：「誰がこれを持ち続けるか」）が要る。VCDesign はこれを `custody_chain`（担当交代の追記記録）、`re_derivation_basis`（後任が判断を再導出できる根拠）、`review_triggers`（何が変われば見直すか）、`last_reaffirmed`（今も有効という確認）で記録する。
- 自律化が進むほど人はループの外に出るので、継続保有の必要は減らずに増える。
- 指標：`owner_missing`、`custody_gap`、`one_shot_improvement`、`positive_delta_without_holder`

### 見つける

- **Positive Δ**：期待を上回る差も Δ として観測し、異常として扱わない。観測 → 意味づけ → 保有者付きで再利用可能にする、の順で扱う。
- **spread_signals**：広がりの兆候（二回目が安くなる、頼んでいない所から引き合いが来る、別の判断の材料になる、接続するほど一件あたりの価値が上がる）を、開始時に `expected` として宣言し、`observed` と `unexpected` で記録する。平均的な効果（`average_outcome`）とは別に評価する。
- 原因が特定できない上振れは IDG で UNKNOWN とし、拡大の根拠にしない。
- 指標：`spread_signal_observed`、`success_without_spread_signal`、`reuse_cost_trend`

### 閉じる

極端な下振れは、連鎖・再利用・集中・フィードバックによって一つの失敗が次の失敗を生むことで起きる。
VCDesign は分布を予測せず、その増幅を次の4つで切る。

| 機構 | 何を切るか | 宣言・仕組み |
| --- | --- | --- |
| 区画を分ける | 区画をまたぐ伝播 | `failure_domain`、boundary の `containment` |
| 上限を宣言する | 損失の大きさ | `blast_radius`（scope と max_loss） |
| 境界で確かめ直す | 上流の誤りの増幅 | boundary の `revalidation`、`upstream_basis_refs` |
| 集中を避ける | 共通原因による同時故障 | `depends_on`、指標 `concentration` |

外から来る極端な事象は消せない。扱うのは、それが内部でどこまで広がるかである。
致命的な下振れは、責任者の有無によらず停止する（`policies.yaml judgment_gate.hard_stops`）。

- 指標：`precondition_broken`、`blast_radius_undeclared`、`blast_radius_exceeded`、`transitive_trust`、`concentration`

### 試す

- **reversibility**：撤回・縮小・修正できるかを宣言する。状態は戻せるが、責任記録は追記のみ（`policies/temporal-governance.md`）。
- **Expand の条件**：拡大後の範囲でも復旧できること。復旧できる範囲でしか変更に賭けない。復旧能力を上げることが、賭けられる回数を増やす。
- **停止可能性**：すべての運用経路に停止責任者がいる（`policies.yaml haltability`）。
- 指標：`expand_beyond_recovery`、`halt_readiness`

### 伝える

- **basis_flow**：境界は損失を止めるが、根拠と残るものは通す。結論は受け手の境界で確かめ直す（`revalidation`）。
- **decision.basis**：判断ごとに、Upside / Downside / Continuity / Asymmetry の観点で根拠を残す。
- **re_derivation_basis**：担当交代をまたいで、後任が判断を再導出できる根拠を残す。
- 指標：`decision_without_basis`、`review_trigger_missing`

---

## 3. 判断6語と宣言

判断は必ず人間が閉じ、6語以外の語彙は使わない。

| 判断 | 宣言の扱い | 次の状態 |
| --- | --- | --- |
| Proceed | 現在の宣言を維持する。章を替えない修正を含む | active |
| Expand | `blast_radius` を広げる（before / after）。Positive Δ の観測と復旧能力の確認が必須 | active |
| Limit | `blast_radius` を狭める（before / after） | active |
| Reframe | 新しい章として前提・境界・責任者・宣言を定め直す | reframed |
| Defer | 暫定責任者と次回判断時刻を置いて保留する | deferred |
| Retire | 責任を解放し、残すものの保有者を移す。開始前の案件では開始しない判断を含む | retired |

宣言の更新を伴わない「小さな試行」は Limit ではない。上限のない試行として判断ゲートで止める。

---

## 4. 境界の3つの働き

| 働き | 対象 | 既定 |
| --- | --- | --- |
| containment | 失敗・指令 | 通さない（deny） |
| basis_flow | 根拠・残るもの | 通す（allow） |
| revalidation | 上流の結論 | 引き継がず、確かめ直す |

「境界」という語は、責任境界（B1〜B17、`catalog/boundaries/`）、判断の受け渡し点（`patterns/boundary-pattern.yaml`）、障害区画（`failure_domain`）でも使われる。区別は `glossary.md` の Boundary を参照。

---

## 5. VCDesign 固有の拡張：AI 統制

正本の5原則の外側に、VCDesign の強みとして AI 統制を置く（`policies.yaml ai_extension`、`metrics.yaml ai_extension`）。

- AI は判断を支援するが、責任を持たない（axioms A3）
- LLM は意味のループに置き、物理・価値・責任のループを直接操作しない
- 速いループは遅いループの制約を書き換えない（axioms A4、`docs/ai-adaptive-loop-model.md`）
- エージェントの実行前に、権限・責任者・可逆性・停止責任者を確認する
- supervisor が責任の最終収束点になる

---

## 6. v1 からの移行

v2 は互換性を切っている。v1 の語彙と記録は次のように読み替える。

| v1 | v2 |
| --- | --- |
| action: fix | decision: proceed |
| action: reframe / defer / retire | decision: reframe / defer / retire |
| decision posture: commit | proceed（範囲を狭めて即時に止める場合は limit） |
| decision posture: reconsider | defer（IDG で UNKNOWN） |
| decision posture: abandon | retire |
| decision_size: no_go / small_go / scale_go | retire（開始しない）／ proceed または limit ／ expand |
| 長期判断の姿勢（small_go / defer_or_experiment / deny_or_reframe） | 判断ゲートで6語のいずれかに確定する |
| RCL: Close / DeferToPool / Abort | proceed / defer / 停止のあと retire または defer |
| long_term_decision_gate、scale_gate、reframe / defer / retire_control | `policies.yaml judgment_gate` |
| tail_signals | spread_signals |
| action_history | decision_history |
| why_action | decision.basis |
| promise_broken | precondition_broken |
| unresolved_duration_exceeded、defer_stagnation、retirement_pending_too_long | stagnation |
| dependency_concentration、judgment_concentration | concentration |
| upside_signal_observed、tail_signal_absent_on_success、scale_beyond_recovery | spread_signal_observed、success_without_spread_signal、expand_beyond_recovery |
| long_term_judgment_metrics、repeated_reframe、reaffirmation_decay | 削除（判断ゲートと芯の指標で代替） |
