# VCDesign Value Continuity Implementation: 判断と責任で Value Continuity を実装する

## Status

**Design principle / Reading aid — not authority.**

このドキュメントは、Value Continuity を VCDesign が**判断と責任の面から**どう実装しているかを、
既存仕様の対応として固定する読み方の文書である。

Value Continuity の定義、Value Asymmetry Principle、5原則、Decision は
正本 [value-continuity/value-continuity](https://github.com/value-continuity/value-continuity) にある。
本文書はそれらを再定義しない。定義や原則の説明が必要な場合は、正本の README.md と
`value-continuity-system-design.md`（システム設計への適用）を読むこと。

仕様上の権威は `core.yaml`（`value_accumulation` / `downside_containment` / `value_asymmetry` /
`delta_definition.polarity` / `decision_vocabulary`）、`policies.yaml`（`scale_gate` / `long_term_decision_gate`）、
`metrics.yaml`（`accumulation_metrics` / `containment_metrics` / `evaluation_model.polarity`）にある。
フィールド定義は `schema_case.yaml` (v0.3) と `schema_log.yaml` (v0.3)、
境界の構造は `patterns/boundary-pattern.yaml` (v1.3.0) にあり、本文書はその読み方を固定する。

既存文書との役割分担:

- `value-continuity-implementation.md`（本文書）— 正本の5原則と VCDesign の要素の対応、Positive Δ / Negative Δ、判断語彙の対応をまとめる親文書
- `value-tenure-model.md` — 「残す」「伝える」のうち、担当交代をまたぐ時間方向（点の責任と線の責任）
- `downside-containment-model.md` — 「閉じる」の詳細（増幅を切る 4 機構）

---

## 1. 5原則と VCDesign の要素

正本の5原則を、同じ順番で VCDesign の要素に割り付ける。

| 原則 | VCDesign での主な実装 | 規範の置き場所 |
|---|---|---|
| **残す** | 残るものを保有者付きで宣言する。担当交代をまたいで根拠を保有する | `schema_case.residual_assets`、tenure フィールド群、`tenure_metrics` |
| **見つける** | 広がりの兆候を Positive Δ として観測する | `delta_definition.polarity.positive`、`schema_case.tail_signals`、`upside_signal_observed` |
| **閉じる** | Negative Δ を局所化・緩和し、必要なら閉じる。増幅を切る 4 機構 | `downside_containment`、containment フィールド群、`containment_metrics`、RCA / IDG |
| **試す** | 戻せる範囲で変更し、広げるときは上限と復旧能力の範囲に留める | `schema_case.reversibility`、`scale_gate`、`scale_beyond_recovery` |
| **伝える** | 結論ではなく根拠を境界の向こうへ渡し、受け手が再判断する | `boundary-pattern.basis_flow` / `revalidation`、`re_derivation_basis` |

正本の5原則に直接対応しない要素（AI の非責任、ループと時間定数の分離、supervisor、
AI の成長の定義など）は、正本を判断と責任で実装するための VCDesign 固有の手段である。
仕様上は `implementation_specific` の注記で区別している。

---

## 2. Positive Δ と Negative Δ

Δ と Positive Δ / Negative Δ の定義は正本（README.md「Δ（期待との差）」）にある。
期待は前提と価値の両方を含み、Negative Δ は伝播させず、Positive Δ は伝播可能にする。
VCDesign はもともと前提からのズレを検知して作動する仕組みであり、期待の前提を `precondition`、
価値を `value_intent` として宣言する。向きによる扱いの区別は `core.yaml delta_definition.polarity` に実装する。

| | Negative Δ | Positive Δ |
|---|---|---|
| 期待との差の向き | 下回る（章の成立条件・責任配置・価値が崩れる） | 上回る |
| 基準線 | precondition / `value_intent` | precondition / `value_intent`（宣言した場合は `tail_signals.expected` も） |
| 扱い | 局所化 → 緩和 → 必要なら閉じる | 観測 → 意味づけ → 再利用可能にする |
| 流れ | RCA / IDG → containment → action | semantic loop → value loop → responsibility loop（`residual_assets` に holder 付きで記録） |
| 広げるとき | — | decision expand として `scale_gate` を通す |
| 責任の問い | どの責任配置が崩れるか | 誰がその上振れを保有するか |

「すべての Δ は責任に割り当てる」という VCDesign の原則は、Positive Δ にも同じく適用される。
保有者のいない上振れは残らない。これを検知するのが `positive_delta_without_holder` である。

### 非対称をどこで保証するか

Positive Δ を Negative Δ と同じ停止・隔離の流れに入れないことは、次の場所で保証する。

- `core.yaml delta_definition.polarity.asymmetry_rules` — 規範。停止・隔離しない、containment に流さない、scale_gate 以外で広げない、両方の向きを含む観測は分ける
- `metrics.yaml evaluation_model.polarity` — positive の metric は warning を上限とし、blocking にしない
- `policies.yaml policy_enforcement.asymmetry_note` — blocking は Negative Δ に対してのみ用いる
- `patterns/boundary-pattern.yaml basis_flow` — 失敗は既定で止め（containment: deny）、根拠と残るものは既定で通す（basis_flow: allow）
- IDG — 原因の分からない上振れは UNKNOWN とし、拡大の根拠にしない

---

## 3. 残す：業務が変わったら何が残るか

判定の問い（「業務が変わったら、この改善の何が残るか」）と点の改善の扱いは、正本に従う。
VCDesign はこの問いへの答えを `schema_case.residual_assets` として記録する。

- 種類は `core.yaml value_accumulation.residual_asset_kinds`（record / standard / basis / connection / capability）
- 各項目は `survives`（どの変化をまたいで残るか）と `holder`（保有し続ける主体）を持つ
- 宣言が空の改善は点の改善として扱う。業務変更で改善が消えたことは Negative Δ（`one_shot_improvement`）として検知する

実例は `../examples/point-vs-line-improvement.md` を参照。

---

## 4. 見つける：広がりの兆候

正本「見つける」の例示を、`tail_signals` の既定の種類として持つ。網羅ではない。

| 兆候 | 観察できる事実 |
|---|---|
| `reuse_cost_decline` | 同じ仕組みを別の場所に入れるコストが、回を追って下がる |
| `unsolicited_pull` | 依頼していない部署・主体から「うちでも使いたい」が来る |
| `output_as_input` | 成果が別の判断・システムの材料として使われ始める |
| `value_per_connection` | 利用やデータが増えるほど、一件あたりの価値が上がる |
| `other` | 上記に当たらないが、再利用・接続によって次の価値を生む兆候 |

開始時に `tail_signals.expected` を宣言し、レビュー時に `observed` を記録する。
宣言していなかった兆候は `unexpected` に記録し、宣言外であることを理由に捨てない。
いずれも Positive Δ であり、平均的な効果（`average_outcome`）とは独立に記録する。

---

## 5. 閉じる

`downside-containment-model.md` を参照。
Negative Δ を局所化し、損失に上限を置き、上流の誤りを境界で増幅させず、一点への集中を検知する。

---

## 6. 試す：scale_gate と Expand / Limit

正本の「変更に賭けられる回数は、復旧能力で決まる」を、VCDesign は次の形で判断に組み込む。

- 宣言した `blast_radius.max_loss` が、試行の予算になる
- 広げる前に、広げた後も戻せること（`reversibility`）を確認する
- 復旧能力を超えた拡大は `scale_beyond_recovery` で検知する

小さく始めた判断を広げるときの門が `policies.yaml scale_gate` である。

| 平均的な効果 | 広がりの兆候 | scale_gate outcome | Decision |
|---|---|---|---|
| あり | あり | `scale_go_within_declared_max_loss` | Expand |
| あり | なし | `keep_small_or_retire` | Proceed / Limit、または Retire |
| なし | あり | `reframe_and_retry_small` | Reframe |
| なし | なし | `retire` | Retire |

Expand と Limit は、章を替えずに `blast_radius` の宣言を更新する判断である。
Expand は scope と max_loss を広げて再宣言し、Limit は対象・権限・規模・期間を縮めて再宣言する。
更新は `schema_log.decision.blast_radius_update` に before / after で残す。

---

## 7. 伝える：根拠を流し、判断は受け手が再生成する

VCDesign には、根拠を次の判断へ渡す経路が三つある。いずれも「結論ではなく根拠を渡す」の実装だが、別の概念である。

| 経路 | 方向 | 仕様 |
|---|---|---|
| `re_derivation_basis` | 時間方向（担当交代をまたぐ） | `schema_case.yaml`、`value-tenure-model.md` |
| `revalidation` / `basis_flow` | 空間方向（境界をまたぐ） | `patterns/boundary-pattern.yaml` |
| Re-derivation Layer | 機械の動作を業務上の意味・権限・根拠へ翻訳する層 | `glossary.md`「Re-derivation Layer」 |

`basis_flow` は根拠と残るものを既定で通し、`revalidation` は上流の結論をそのまま引き継がない。
二つを組にすることで、価値は越境でき、誤りは越境しにくくなる。

---

## 8. 判断の選択肢

正本の Decision と VCDesign の既存語彙の対応は `core.yaml decision_vocabulary` に規範として置く。
読みやすさのための要約を示す。

| Decision | action | decision posture | decision_size | scale_gate |
|---|---|---|---|---|
| Proceed | なし / fix | commit | small_go | keep_small の側 |
| Expand | なし | なし | scale_go | tail_signal_observed |
| Reframe | reframe | reconsider（再検討の段階） | なし | no_success_with_tail_signal |
| Limit | なし / fix | commit（狭めた範囲で） | small_go（blast_radius を狭める宣言更新を伴うもの） | keep_small の側 |
| Defer | defer | defer | defer | なし |
| Retire | retire | abandon | no_go（開始前の案件で、開始しない判断） | neither |

Limit は blast_radius を狭める宣言更新を伴う判断である。宣言更新を伴わない small_go は Proceed として記録する。
長期判断の姿勢 `defer_or_experiment` は、狭めた blast_radius の宣言があれば Limit、なければ Defer として記録する
（`core.yaml decision_vocabulary.long_term_posture_resolution`）。

action は章のライフサイクル上の遷移であり、Decision とは別の軸である。
Decision は `schema_log.decision` に、遷移の理由は `why_action` に記録する。

---

## 9. 観測

| 原則 | metric | polarity | 見ていること |
|---|---|---|---|
| 見つける | `upside_signal_observed` | positive | 広がりの兆候が観測された |
| 見つける | `reuse_cost_trend` | positive | 再利用のコストが下がっているか |
| 残す | `positive_delta_without_holder` | negative | 上振れに保有者がいない |
| 残す | `one_shot_improvement` | negative | 業務変更で改善が消えた |
| 試す | `tail_signal_absent_on_success` | none | 成功したが広がる兆候がない（scale_gate への入力） |
| 試す | `scale_beyond_recovery` | negative | 拡大が復旧能力を超えていないか |
| 閉じる | `containment_metrics` 一式 | negative | 下振れが増幅・伝播する条件 |

---

## 10. 未整備の事項

- VMS（別リポジトリ）の判断語彙（Instant / Pending / Discard）と Decision の対応は本版の範囲外。
- RCL の Resolution 語彙（Close / DeferToPool / Abort）と Decision の対応は未整理。
- `tail_signals` と Positive Δ の観測を支援する検査ツールは未実装。
- 兆候の定量化（特に `reuse_cost_trend` のコスト単位）は章ごとの定義に委ねている。
