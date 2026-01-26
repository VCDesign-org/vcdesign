# VCDesign Glossary

Definitions of terms used in VCDesign and UVW (Unstable Value World).

---

## Term: Artifact
**EN:** Any output (code, text, data, model) produced by a system or worker.  
**JA:** システムや作業者が生成したあらゆる出力（コード、テキスト、データ、モデルなど）。「成果物」とも呼ぶ。  
**Notes:** In UVW, an artifact has no intrinsic value until judged.  
**References:** [A1: Value Instability](../core/axioms.yaml)  

## Term: Boundary
**EN:** An explicit interface where Judgment is attempted and protected from implicit values leaking in.  
**JA:** 判断（Judgment）が試みられる明示的なインターフェース。暗黙的な価値観の流入を防ぐ防壁として機能する。  
**Notes:** Formerly associated with "BOA" (Boundary-Oriented Architecture), now a generic pattern.  
**References:** [Boundary Pattern](../patterns/boundary-pattern.yaml), [Decision Posture](../core/decision-posture.yaml)  
**Aliases:** Explicit Verification Point, Closure Point

## Term: Continuity (Value Continuity)
**EN:** The state of value being maintained over time through active re-verification. The primary goal of VCDesign.  
**JA:** 能動的な再検証によって、時間の経過に関わらず価値が維持されている状態。VCDesignの主要な目的。  
**References:** [Continuity Claim](../core/continuity-claim.yaml)  

## Term: Context Drift
**EN:** The phenomenon where the context that makes a value valid changes over time (technological shift, social shift, user belief shift).  
**JA:** 価値を有効にしていた文脈（コンテキスト）が、時間経過とともに変化する現象（技術変化、社会変化、ユーザーの信念の変化など）。  
**References:** [A2: Context Drift](../core/axioms.yaml)  
**Aliases:** Value Drift

## Term: Decision Posture
**EN:** The rule "Stop or Review" applied when judgment confidence is lost.  
**JA:** 判断の確信が失われた際に適用される「停止またはレビュー（Stop or Review）」という規則。  
**References:** [Decision Posture](../core/decision-posture.yaml)  

## Term: Decay (Judgment Decay)
**EN:** The natural loss of validity of a Judgment over time due to Context Drift.  
**JA:** コンテキストドリフト（文脈の変化）により、過去の判断の有効性が自然に失われていくこと。  
**References:** [A3: Judgment Decay](../core/axioms.yaml)  

## Term: Judgment
**EN:** The act of asserting that an Artifact satisfies a Value criterion.  
**JA:** あるアーティファクト（成果物）が価値基準を満たしていると断言する行為。  
**Notes:** Judgment requires an external interpretive frame (Binding).  
**References:** [A4: Non-Self-Evidence](../core/axioms.yaml)  

## Term: Judgment Closure
**EN:** The act of explicitly signing (Accepted), denying (Denied), or declaring unknown (Unknown) on a specific Judgment Proposal.  
**JA:** 特定の判断提案に対して、明示的に署名（承認）、拒否（否認）、または不明（判断不能）を宣言する行為。  
**References:** [Judgment Closure Protocol](../protocols/judgment-closure.yaml)  

## Term: RCA (Responsibility Closure Agent)
**EN:** A structural pattern for an agent that guards a Boundary and performs Judgment Closure.  
**JA:** 境界（Boundary）を監視し、判断の閉包（Judgment Closure）を実行するエージェントの構造パターン。  
**References:** [RCA Pattern](../patterns/rca-pattern.yaml)  

## Term: Resolution
**EN:** A committed Action with a specified Responsible Actor, Scope, and Expiry. The output of a successful Judgment Closure.  
**JA:** 責任ある主体（Responsible Actor）、適用範囲（Scope）、有効期限（Expiry）が明記されたコミット済みの行動（Action）。正常な Judgment Closure の出力。  
**References:** [Resolution Handshake Protocol](../protocols/resolution-handshake.yaml)  

## Term: Resolution Handshake
**EN:** A protocol that defines how a Closed Judgment is promoted to a Resolution (Responsibility Commitment).  
**JA:** 閉じた判断（Closed Judgment）を解決（Resolution / 責任のコミットメント）へと昇格させるためのプロトコル。  
**References:** [Resolution Handshake Protocol](../protocols/resolution-handshake.yaml)  
**Aliases:** RP (Resolution Protocol), Handshake

## Term: Responsibility
**EN:** The state of being answerable for the consequences of a Judgment. In UVW, this is a scarce resource.  
**JA:** 判断の結果に対して説明責任を負う状態。UVWにおいて、これは希少なリソースである。  
**References:** [A5: Responsibility Gap](../core/axioms.yaml)  

## Term: UVW (Unstable Value World)
**EN:** The problem space assumption that value is not static and decays over time.  
**JA:** 価値は静的ではなく、時間とともに劣化するという問題空間の前提。  
**References:** [Axioms](../core/axioms.yaml)  

## Term: Value
**EN:** A perceived benefit or meaningfulness arising from the interaction between an Artifact and a Context. Not a static property.  
**JA:** アーティファクトとコンテキストの相互作用から生じる、知覚された利益または意味。静的な性質ではない。  
**References:** [A1: Value Instability](../core/axioms.yaml)  
