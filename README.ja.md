# VCDesign 仕様群

VCDesign（Value Continuity Design）は、
「どう作るか」ではなく、作られた後の価値を
時間の中でどう守り抜くかを設計するための仕様群です。

## VCDesign とは何か

VCDesign は、**AIや自動化システム**において、
**判断 (Judgment)**、**責任 (Responsibility)**、そして
**時間 (Time / Operations)** の連続性を失わないための設計仕様です。

システム規模が拡大しても、
個々の判断がどこで閉じられ、
誰が責任を引き受け、
運用の時間の中でどのように変化していくのかを
明示的に構造化することを目的としています。

これらの仕様は、単なる読み物ではありません。
人間や生成AIが**設計支援・判断支援・コード生成**に利用することを前提とした、
**実行可能な設計言語**として定義されています。

## どこから読むか (Where to start?)
全体の俯瞰図については **[Specification Map](specs/map.md)** を参照してください。

以下の順序で読むことを推奨します。
1. **[specs/core/](specs/core/)** (Authority): なぜこの設計が必要か、何を守るべきか。
2. **[specs/protocols/](specs/protocols/)** (How / Operations): 判断をいつ閉じ、どう責任を引き渡すか。
3. **[specs/chapters/](specs/chapters/)** (When): 時間軸の中で、どの設計がいつ必要になるか。

## ディレクトリ構造 (Directory Structure)

* **[specs/core/](specs/core/)**: **The Authority.** VCDesign の最小限かつ不可避な定義。
* **[specs/protocols/](specs/protocols/)**: **The Procedures.** 判断を閉じ、責任を引き渡すための標準的な手順。
* **[specs/patterns/](specs/patterns/)**: **The Structures.** コアを実装するための参照パターン（境界構造やRCAなど）。
* **[specs/chapters/](specs/chapters/)**: **The Narratives (The "When").** フェーズやバージョンではなく、判断や責任の時間的変化（When）を扱う設計単位。
* **[specs/glossary/](specs/glossary/)**: 用語集。

## ステータス (Status)
Core 仕様は **Stable**（安定）です。
Protocols と Patterns は **Stable** ですが、拡張可能です。
