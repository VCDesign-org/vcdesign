# VCDesign v2 Conformance

## Status

**Normative checklist** derived from `core/axioms.yaml`, `core/core.yaml` and `core/policies.yaml`.
It adds no new rules. A check that fails here is a failure of the rule it cites.

判定は Value Continuity の Review Output と同じく `ok` / `warning` / `blocking` で示し、必ず根拠を付ける。
blocking は Negative Δ に対してのみ用いる。

---

## 1. Axioms

| # | チェック | 失敗時 | 根拠 |
| --- | --- | --- | --- |
| A1 | 確定した Δ（負・正とも）に、名前のある owner（Positive Δ では holder）がいる | Negative Δ は blocking、Positive Δ は warning | axioms A1 |
| A2 | すべての実行が、人間が閉じた判断で許可された範囲（宣言）の内側にある。範囲を越える変化は Δ として再判断されている。越えた境界で pass があり、unknown を pass として扱っていない | blocking | axioms A2 |
| A3 | すべての decision の decided_by が人間である | blocking | axioms A3 |
| A4 | 速いループが遅いループの制約を書き換える前に、再判断の機会がある | blocking | axioms A4 |
| A5 | 責任保有者の負荷が宣言した容量の範囲内にある | warning | axioms A5 |

## 2. 判断ゲート（5原則の順）

| 原則 | チェック | 失敗時 |
| --- | --- | --- |
| 残す | value_intent と residual_assets（holder 付き）が宣言されている | warning |
| 見つける | spread_signals.expected が宣言され、観測が平均的な効果と別に記録されている | warning |
| 閉じる | blast_radius が宣言されている。不可逆な案件では max_loss が必須 | 不可逆で未宣言なら blocking |
| 閉じる | 上流の結論が境界で確かめ直されている（upstream_basis_refs） | warning |
| 試す | reversibility が宣言され、停止責任者がいる | 停止経路なしは blocking |
| 伝える | decision.basis が Upside / Downside / Continuity / Asymmetry の観点で記録されている | warning |

## 3. 判断ごと

| 判断 | チェック | 失敗時 |
| --- | --- | --- |
| Expand | 観測された Positive Δ を参照し、拡大後も復旧でき、blast_radius の before / after がある | blocking（Expand を止める。観測と保有は止めない） |
| Limit | blast_radius を狭める before / after がある | warning（なければ Proceed として記録し直す） |
| Reframe | 新しい前提・境界・責任者・宣言がある | blocking |
| Defer | 暫定責任者と next_review_at がある | blocking |
| Retire | 依存先への通知と、残すものの保有者の移管がある | warning |

## 4. 語彙

- 判断の語彙が6語（proceed / expand / limit / reframe / defer / retire）以外に使われていない
- Value Continuity の定義文が VCDesign 側で再定義されていない（正本を参照している）
