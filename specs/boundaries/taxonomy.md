# VCDesign Responsibility Boundary Taxonomy (Draft v0.1)

この taxonomy は、
「この文章は *どの責任境界* の話か？」
「その境界に *どう対処するか* を述べているか？」
を明示するための分類である。

---

## B1. Human ↔ AI Judgment Boundary
**説明:**  
AIの出力を「判断」として成立させるかどうかの境界。

**典型トリガー:**  
- LLMが結論・提案・診断を出す  
- 自動生成コードを採用する

**主なFailure Mode:**  
- AIの出力が“誰の判断か”不明になる  
- 暗黙承認（silent commit）

**推奨対処（典型）:**  
- Judgment Closure を必須化  
- Unknown をデフォルトにする Decision Posture

---

## B2. Automation ↔ Manual Intervention Boundary
**説明:**  
自動処理を続けるか、人に渡すかを切り替える境界。

**Failure Mode:**  
- 自動化が止まらない  
- 逆に人が常時張り付く

**対処例:**  
- Expiry 付き Resolution  
- 閾値超過時の強制ハンドオフ

---

## B3. System ↔ Reality Boundary
**説明:**  
システム内部の状態と、現実世界の状態がズレる境界。

**Failure Mode:**  
- 「動いていることになっている」  
- センサ値・ログが真実でない

**対処例:**  
- 再検証ポイントを Boundary として明示  
- Judgment Decay を前提にする

---

## B4. Data ↔ Meaning Boundary
**説明:**  
データが「意味を持つ」と判断される瞬間の境界。

**Failure Mode:**  
- 数値が意味を持っている前提で話が進む  
- Context Drift が無視される

**対処例:**  
- Judgment Proposal を明示  
- Context を logging に含める

---

## B5. Decision ↔ Action Boundary
**説明:**  
判断（Judgment）が行動（Resolution）に変換される境界。

**Failure Mode:**  
- 判断しただけで実行された扱いになる  
- 誰も責任を持たない Action

**対処例:**  
- Resolution Handshake を必須化  
- Responsible Actor を明示

---

## B6. Responsibility Assignment Boundary
**説明:**  
「誰が責任を持つか」が確定する境界。

**Failure Mode:**  
- 組織・AI・プロセスに責任が拡散  
- “みんなの判断”になる

**対処例:**  
- RCA Pattern  
- 単一 Owner 原則

---

## B7. Organizational Boundary
**説明:**  
チーム・部署・会社をまたぐ責任境界。

**Failure Mode:**  
- 暗黙の合意  
- 引き継ぎ時の責任消失

**対処例:**  
- Resolution Handshake を契約的に扱う  
- Expiry を必ず設定

---

## B8. Policy ↔ Practice Boundary
**説明:**  
規約・ルールと、実際の運用が乖離する境界。

**Failure Mode:**  
- 「ルール上はOK」だが現場が破綻  
- 形骸化したコンプライアンス

**対処例:**  
- Judgment を Policy 適合として閉じない  
- 実運用を Artifact として再判断

---

## B9. Expertise Boundary
**説明:**  
専門家の判断と非専門家の判断の境界。

**Failure Mode:**  
- 権威への丸投げ  
- 専門性のブラックボックス化

**対処例:**  
- Judgment Proposal を言語化  
- Evidence を必須化

---

## B10. Temporal Boundary (Now ↔ Later)
**説明:**  
「今の判断」が将来も有効だと誤解される境界。

**Failure Mode:**  
- 永久決定扱い  
- 再判断されない

**対処例:**  
- Expiry を必須  
- Continuity Claim を明示

---

## B11. Risk Acceptance Boundary
**説明:**  
リスクを許容するか否かを決める境界。

**Failure Mode:**  
- リスクの黙認  
- 誰もリスクを引き受けていない

**対処例:**  
- Risk を Judgment Proposal に含める  
- Responsible Actor に明示的承認

---

## B12. Knowledge Validity Boundary
**説明:**  
知識・前提が「まだ有効か」を問う境界。

**Failure Mode:**  
- 古い知識の継続使用  
- 更新されない前提

**対処例:**  
- Judgment Decay を前提に設計  
- 定期的再Closure

---

## B13. Interpretation Boundary
**説明:**  
同じ Artifact が複数の意味に解釈される境界。

**Failure Mode:**  
- 解釈違いによる事故  
- 後出し解釈

**対処例:**  
- Judgment の解釈枠を明示  
- Notes / Context をログ化

---

## B14. Accountability ↔ Blame Boundary
**説明:**  
説明責任と責任追及が混同される境界。

**Failure Mode:**  
- 判断が隠蔽される  
- 振り返り不能

**対処例:**  
- Judgment と Outcome を分離  
- ログを非懲罰的に扱う

---

## B15. Design ↔ Emergence Boundary
**説明:**  
設計された振る舞いと、創発的振る舞いの境界。

**Failure Mode:**  
- 「想定外」で片付けられる  
- 設計責任が消える

**対処例:**  
- Unknown を正規の結果として扱う  
- 再設計トリガーにする

---

## B16. Model ↔ Reality Boundary
**説明:**  
モデルが前提とする「現実」と、実際の現実が乖離する境界。

**Failure Mode:**  
- 再学習データが汚染される（自家中毒）  
- ドリフト検知が働かない

**対処例:**  
- Ground Truth の定期的再取得  
- Model Decay の明示的監視

---

## B17. Impact ↔ Accountability Boundary
**説明:**  
システムの影響範囲（Impact）と、責任者の権限（Accountability）がズレる境界。

**Failure Mode:**  
- 権限を超えた影響が発生する  
- 誰も止められない

**対処例:**  
- 責任範囲の再定義（Resolution Handshake）  
- 影響範囲の明示的クローズ
