# Governance

- 種別: 論理レイヤー入口 (Governance)
- 位置づけ: 全サービスを横断する共通領域

## 目的

全サービスに共通して適用される、設計運用上の規約・原則・決定記録を管理する横断領域。個々のサービス (Service Design / Screen Requirements / Design System / Assets) は、この領域の共通規約に従う。

## 管理対象

- リポジトリ運用の原則
- 命名規則
- ADR (設計判断の決定記録)
- レビュー・承認規則
- 用語定義
- オーナー確認事項 (未決事項の集約)

## 管理しない対象

- 特定サービス固有の設計・仕様・資産 (各サービス配下で管理)
- 実装コード

## リポジトリ全体に対する位置づけ

- 5 論理レイヤーのうち唯一の横断共通レイヤー。
- 参照順序上は、各サービスの設計を読む前提となる共通ルールを提供する位置にある。

## 現在存在する成果物

- [owner-decisions.md](owner-decisions.md) — オーナー確認事項 (分類C) の一覧。既存資産として移行済。§4 に Review / Approval Rules 作成前に必要な確認事項を独立節として記録し、**2026-07-17 に全 11 項目のオーナー明示的回答を「オーナー回答」列へ記録済み**（残る条件・未定は「残る Open Issue」列へ分離）。
- [review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) (Draft) — レビュー・承認規則の**正本を作成するための計画**。正本作成前に必要なオーナー確認事項・証拠・責務境界・作成順を整理する。§8 に回答取得状況、§11 Entry Conditions に正本作成前提の項目別評価を反映済み。これは正本そのものではなく、Review / Approval Rules を作成済み・承認済み・適用中とはしない。

## 現在不足している成果物

以下は正本が存在しない。本 bootstrap では新規作成しない。**不足している成果物を、存在するものとして扱ってはならない。**

- Repository principles の正本
- 命名規則の正本 (例: 既存 Design System 文書が参照する `governance/naming-rules.md` は未作成)
- ADR の正本
- レビュー・承認規則の正本 (作成計画 [review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) は Draft で存在するが、**正本は依然として存在しない**)
- 用語定義の正本

これらの正本の作成・承認フローは未決である。空の ADR ファイルや、内容を推測した規約は作成していない。レビュー・承認規則については、作成・承認フローの検討事項を Creation Plan (Draft) と [owner-decisions.md](owner-decisions.md) §4 に整理し、**2026-07-17 に §4 の全 11 確認事項へオーナー明示的回答を記録した**。これにより正本作成の前提のうち「回答の取得・記録」は満たされたが（Creation Plan §11 Entry Conditions 参照）、上流 Open Issue の具体的解決単位・placeholder/実査待ちの個別確認主体・再評価の一部トリガー等は「残る Open Issue」として未解決である。**Review / Approval Rules の正本は依然として作成されておらず（承認済み・適用中でもない）、Creation Plan と回答の記録だけでは Travel Work Order 6 で確認された共通阻害 Fact は全面解消されない**。
