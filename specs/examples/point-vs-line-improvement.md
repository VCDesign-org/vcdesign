# Point vs Line Improvement Example: 業務が変わったら何が残るか

## Status

Example (workshop-ready). 登場する工場・組織・人物・数値はすべて架空である。

このドキュメントは、同じ工場で起きた二つの改善を並べ、
**点の改善**と**線の改善**の違い、そして上に開き下を閉じる判断（value asymmetry）が
どう記録されるかを示す実例である。

背景の設計原則は `../core/implementation.md`、
フィールド定義は `../core/schema_case.yaml` (v1.0) と `../core/schema_log.yaml` (v1.0) を参照。

---

## Scenario

架空の部品工場「北原工場」には 4 本の加工ラインがある。
ある年、二つの改善が同時に始まった。

- **改善 A**: 1 号ラインの日報作成を表計算マクロで自動化する
- **改善 B**: 1 号ラインの設備稼働データを小型の産業用 PC で収集し、停止要因を見える化する

どちらも 3 か月後のレビューで「効果あり」と判定された。
改善 A は日報作成を 1 日 30 分短縮し、改善 B は停止要因の集計を 1 日 20 分短縮した。
平均的な効果だけを見れば、改善 A のほうが大きい。

---

## 1 年後に起きたこと

### 改善 A

翌年、全社で日報の様式が変わった。マクロは新様式に合わず動かなくなった。
作った担当者は異動しており、直せる人がいなかった。日報作成は元の手作業に戻った。

削れた 30 分は、その 1 年間、数人に数分ずつ散らばっていただけで、何にも積み上がっていなかった。
**業務が変わったとき、何も残らなかった。**

### 改善 B

改善 B では、開始時に次を決めていた。

- 産業用 PC は標準 OS イメージから構築し、構成を記録する
- 故障時に現場の保全担当が予備機へ切り替えられる手順を作り、一度は実際に切替訓練をする
- 収集データの形式と停止要因のコード体系を、ライン固有ではなく工場共通の型として定める

2 号ラインへの展開は、1 号ラインの約半分の工数で終わった。
3 号ラインではさらに短くなった。
品質管理課から「不良の発生時刻と停止要因を突き合わせたい」という依頼が来た。
依頼していない部署からの引き合いである。

途中で PC の OS がサポート終了を迎えたが、標準イメージと切替訓練の経験があったため、
現場が止めずに順次更新できた。**壊れても戻せると分かっていたから、変更できた。**

---

## 記録の比較

### 改善 A（点の改善）

```yaml
case_id: kitahara-2025-017
chapter_id: line1-daily-report
owner: {role: line1_leader}
final_decider: {role: section_manager}
residual_assets: []                 # 何も宣言されていない → 点の改善として扱う
spread_signals:
  expected: []
  observed: []
  average_outcome: met
reversibility:
  class: reversible
  reversal_path: 手作業に戻す
blast_radius:
  scope: line1 日報のみ
  max_loss: {unit: hours_rework, value: 4}
```

様式変更の時点で `one_shot_improvement` が Negative Δ として検知される。
これは「改善が失敗した」ことではなく、「価値が継続しなかった」ことの検知である。

### 改善 B（線の改善）

```yaml
case_id: kitahara-2025-021
chapter_id: line1-downtime-visibility
owner: {role: production_engineering}
final_decider: {role: plant_manager}
residual_assets:
  - kind: standard
    description: 標準 OS イメージと構築手順
    survives: [technology_change, owner_change]
    holder: {role: production_engineering}
  - kind: standard
    description: 工場共通の停止要因コード体系とデータ形式
    survives: [work_change]
    holder: {role: production_engineering}
  - kind: capability
    description: 現場保全担当による予備機切替・復旧の技能
    survives: [owner_change, technology_change]
    holder: {role: maintenance_team}
  - kind: record
    description: 機器構成と変更履歴
    survives: [owner_change]
    holder: {role: maintenance_team}
spread_signals:
  expected: [reuse_cost_decline, unsolicited_pull]
  observed:
    - signal: reuse_cost_decline
      evidence: 2 号ライン展開工数が 1 号ラインの約 50%、3 号ラインは約 35%
      observed_at: 2026-03-31
    - signal: unsolicited_pull
      evidence: 品質管理課から停止要因データ連携の依頼
      observed_at: 2026-05-12
  average_outcome: met
reversibility:
  class: reversible
  reversal_path: 予備機へ切替、標準イメージから再構築
  reversal_window: 常時
  reversal_owner: {role: maintenance_team}
blast_radius:
  scope: 対象ラインのデータ収集のみ（制御系には書き込まない）
  max_loss: {unit: hours_data_gap, value: 8}
  on_exceed: escalate
failure_domain: line-local-data-collection
```

---

## 判断ゲートでの判断

| | 平均的な効果 | 広がりの兆候 | residual_assets | 復旧能力 | Decision |
|---|---|---|---|---|---|---|
| 改善 A | あり（30 分） | なし | なし | 手作業に戻せるだけ | Proceed（小さく留める）、様式変更時に Retire |
| 改善 B | あり（20 分） | reuse_cost_decline, unsolicited_pull | 4 件、保有者あり | 予備機切替・再構築を訓練済み | Expand（4 号ライン・品質管理連携） |

平均的な効果だけで順位をつけると、改善 A が上になる。
広がりの兆候と残るものを見ると、広げるべきは改善 B である。

改善 A のような「成功したが広がらない」改善は、`success_without_spread_signal` として
拡大の前に識別される。改善 A を悪い改善として扱う必要はない。
小さく留めるか、次に様式が変わるときに終了すると、先に決めておけばよい。

### Positive Δ としての記録

改善 B の `spread_signals.observed` は Positive Δ である。停止・隔離の流れには入れず、
観測 → 意味づけ → 再利用可能にする（`residual_assets` に保有者付きで記録する）の順で扱う。
品質管理課からの引き合いは宣言していた兆候（`unsolicited_pull`）だったが、
宣言していない兆候が出た場合も `spread_signals.unexpected` として記録し、捨てない。

Expand は、章を替えずに `blast_radius` の宣言を更新する判断として記録する。

```yaml
log_id: kitahara-log-2026-061
case_id: kitahara-2025-021
decision:
  value: expand
  basis:
    upside: >
      平均的な効果に加え、reuse_cost_decline と unsolicited_pull を観測。
      2 号ライン以降の展開工数が下がり、依頼していない部署から引き合いが来た。
    downside: >
      予備機切替・再構築は訓練済みで、拡大後も復旧できる。制御系には書き込まない。
    continuity: 標準 OS イメージ、共通の停止要因コード、切替技能が保有者付きで残る。
    asymmetry: 収集データと根拠は他部署へ流し、制御への影響は区画内に閉じる。
  positive_delta_refs: [reuse_cost_decline, unsolicited_pull]
  declaration_update:
    before:
      scope: 1〜3 号ラインのデータ収集のみ（制御系には書き込まない）
      max_loss: {unit: hours_data_gap, value: 8}
    after:
      scope: 1〜4 号ラインのデータ収集と品質管理課への読み取り連携（制御系には書き込まない）
      max_loss: {unit: hours_data_gap, value: 8}
      approved_by: {role: plant_manager}
  decided_by: {role: plant_manager}
```

---

## 上と下のつながり

改善 B で拡大を正当化したのは、広がりの兆候だけではない。
**拡大しても戻せる**ことが確認されていたことが、拡大の前提になっている
（`policies.yaml judgment_gate.per_decision.expand` の recovery_capability_confirmed）。

- 切替訓練（下を閉じる仕組み）があったから、OS 更新という変更に踏み出せた
- 変更できたから、システムは古びずに次のラインへ持っていけた
- 次のラインへ持っていけたから、展開のたびにコストが下がった

下を閉じる仕組みが、上に賭ける回数を生んでいる。
逆に、復旧能力を超えて展開を急げば `expand_beyond_recovery` が検知される。

---

## 読み方のまとめ

- 改善の開始時に「業務が変わったら何が残るか」を `residual_assets` として宣言する
- 広げる兆候を `spread_signals.expected` として先に決め、平均的な効果とは別に観測する
- 広げる前に、広げた後も戻せるかを確認する
- 改善が業務変更で消えたら、それを Δ として扱い、次の改善の設計に反映する
