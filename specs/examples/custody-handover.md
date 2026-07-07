# Custody Handover Example: 担当交代をまたぐ責任の継承

## Status

Example (workshop-ready).

このドキュメントは、承認の一点（Gate）を通過した決定が、
**担当交代・自律運用・環境変化**をまたいで責任を保有され続ける（Tenure）様子を示す
エンドツーエンドの実例である。

背景の設計原則は `../core/value-tenure-model.md`、
フィールド定義は `../core/schema_case.yaml` (v0.2) を参照。
本例の機械可読データは `custody-handover-case.yaml` にあり、
`../schemas/tenure_check.py` で責任空白リスクの検査対象になる。

---

## Scenario

ある企業が、顧客問い合わせの一次対応を LLM ベースの自動応答に委ねている。
自動応答は夜間・休日も**誰も見ていない状態で**稼働する。

2025 年 11 月、情報システム部の田中は次の決定を閉じた（Judgment Closure = ACCEPTED）:

```text
決定: 返金・解約に関する問い合わせは、自動応答で完結させず必ず人間へエスカレーションする
```

これは一度きりの承認では終わらない決定である。
モデルが入れ替われば、分類の挙動が変わる。
田中が異動すれば、決定の根拠を知る人間がいなくなる。

---

## 1. Gate: 決定の成立（2025-11）

通常の VCDesign ライフサイクル（Judgment Closure → Responsibility Asset → Resolution）で決定が成立する。
ここまでは点の責任であり、既存仕様の範囲である。

Tenure はここから始まる。成立と同時に、継続保有のための記録を作る:

```yaml
value_intent: >
  顧客の金銭に関わる判断で誤案内を出さない。
  守っているのは応答の自動化率ではなく、顧客からの信頼の継続である。

original_author:
  actor: tanaka（情報システム部）
  at: 2025-11-10

re_derivation_basis:
  premises:
    - 返金・解約は金銭影響があり、誤案内が顧客離反に直結する
    - 当時の分類モデルは返金意図の検出精度が 92% であり、8% の取りこぼしを人間側で吸収する必要があった
  context:
    - 2025-10 に競合他社で自動応答の誤案内が炎上した事案を受けた判断
  evidence_refs:
    - jc-20251110-004（Judgment Closure トレース）

review_triggers:
  - 応答・分類モデルの入れ替えまたはメジャーアップデート
  - 返金・解約ポリシー自体の改定
  - エスカレーション率が 2 週間平均で 50% 以上変動
  - 特定商取引法など前提規制の改定
```

**ポイント:** `review_triggers` はカレンダーではなく事象で書かれている。
「四半期ごとに見直す」ではなく「何が変われば見直すべきか」を決定時点で宣言する。

---

## 2. 無人運用中のドリフト候補（2026-02）

夜間帯にエスカレーション率が緩やかに低下していることを metrics が検出する。

```text
observed: escalation_rate_drop（warning レベル）
attribution: boundary の accountability_on_cross = 情報システム部（事前宣言済み）
```

誰も見ていない時間帯の逸脱だが、責任の帰属は事前に宣言されているため、
「誰の問題か」の議論から始める必要がない。
調査の結果、この時点ではノイズ（季節性）と判断され、判断自体が記録される。

---

## 3. Custody Transfer: 担当交代（2026-03）

田中が異動する。ここが Tenure の最初の試練である。
多くの組織ではここで責任が**静かに無所有になる**（A1 違反だが、検知されない）。

VCDesign では、交代は append-only の責任イベントとして記録される:

```yaml
custody_chain:
  - from: tanaka
    to: sato
    date: 2026-03-31
    reason: 組織異動（情報システム部の再編）
    re_derivation_confirmed: yes
```

`re_derivation_confirmed: yes` は形式ではない。
佐藤が `re_derivation_basis` を読み、
「なぜ 92% という数字がエスカレーション必須の根拠になったのか」を
**自分で再導出できることを確認した**という記録である。

これができない場合（`no` / `partial`）、引き渡しは完了せず、
custody_gap メトリクスの対象になる。

---

## 4. Review Trigger 発火（2026-06）

ベンダーが応答モデルを新世代に入れ替える。
`review_triggers` の第 1 条件が成立する。

```yaml
tenure_event:
  event_type: review_trigger_fired
  case_ref: case-refund-escalation-001
  detail:
    fired_trigger: 応答・分類モデルの入れ替えまたはメジャーアップデート
    evaluation: >
      新モデルの返金意図検出精度は 97%。
      ただし value_intent は「誤案内を出さない」であり精度向上は緩和の十分条件ではない。
      誤案内 1 件の影響評価が未実施のため、エスカレーション必須を維持。
    resulting_action: fix（決定を維持、根拠を更新）
```

**ポイント:** 佐藤は田中ではないが、`value_intent` と `re_derivation_basis` があるため、
「精度が上がったから自動化してよい」という短絡を退けられた。
守っているのは精度ではなく信頼だからである。

---

## 5. Reaffirmation: 保有の更新（2026-06）

見直しの結果が記録され、保有が更新される:

```yaml
last_reaffirmed:
  by: sato
  at: 2026-06-15
  basis: review_trigger（モデル入れ替え）の評価結果。jc-20260615-002 参照。
```

この決定はいま、次のすべてに答えられる状態にある:

1. 現在の保有者は誰か → sato（custody_chain の末尾）
2. 後任は何から再導出できるか → re_derivation_basis
3. 何が変われば見直すか → review_triggers
4. 最後に有効性が確認されたのはいつか → 2026-06-15

---

## Counterfactual: Tenure フィールドが無かった場合

同じ 2026-06 のモデル入れ替えで、何が起きたかを比較する:

```text
owner: tanaka（3ヶ月前に異動済み。記録上は今も owner）
決定の根拠: 田中の頭の中と、散逸した議事録
モデル入れ替え: 見直しのトリガーとして誰も認識しない
新モデル: 返金問い合わせの一部を自動応答で完結し始める
発覚: 顧客クレームが SNS に投稿された時点
```

この状態こそが「レガシー」である。
技術は動き続けていた。消えていたのは責任の所在だった。

---

## Summary Flow

```text
Judgment Closure（Gate: 点の責任）
-> value_intent / re_derivation_basis / review_triggers を決定時点で記録
-> 無人運用（accountability_on_cross が帰属を事前宣言）
-> custody_transfer（append-only の責任イベント、再導出確認つき）
-> review_trigger 発火（カレンダーではなく事象で見直しが起動）
-> reaffirmation（last_reaffirmed 更新 = Tenure の保有更新）
```

- Gate は Tenure の開始点であり、代替ではない。
- 交代の記録がなければ、A1（責任非消失）は交代をまたいで検証できない。
- 見直しは「いつ」ではなく「何が変われば」で定義する。
- 本例は人間の担当交代を扱った。同じ構造は AI Agent の長期運用にもそのまま適用される。
