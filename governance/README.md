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
- [review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) (Draft) — レビュー・承認規則の**正本を作成するための計画**。正本作成前に必要なオーナー確認事項・証拠・責務境界・作成順を整理する。§8 に回答取得状況、§11 Entry Conditions に正本作成前提の項目別評価を反映済み。§12・§13・§16 に Task 009-3 (正本候補 Draft 作成・整合確認) の進捗を反映済み。これは正本そのものではなく、Review / Approval Rules を作成済み・承認済み・適用中とはしない。
- [review-approval-rules.md](review-approval-rules.md) (Draft) — レビュー・承認規則の**正本候補 Draft** (Task 009-3, 2026-07-17)。owner-decisions.md §4 の 11 件のオーナー回答を根拠に、責務区別・影響度別のレビュー/反映/GitHub 操作経路・設計承認と GitHub 操作の分離・承認ログ正本・ライフサイクル・再評価条件・Alignment 完了条件の Draft 提案を構造化した Repository 横断規則の Draft。**明示的なオーナー承認を経ておらず、適用中の規則正本としては成立していない** (Status = Draft)。影響度・高／低の判定基準・判定主体は未定義の Open Issue。この Draft の追加だけでは Work Order 6 の共通阻害 Fact を全面解消しない。

## 現在不足している成果物

以下は正本が存在しない。本 bootstrap では新規作成しない。**不足している成果物を、存在するものとして扱ってはならない。**

- Repository principles の正本
- 命名規則の正本 (例: 既存 Design System 文書が参照する `governance/naming-rules.md` は未作成)
- ADR の正本
- レビュー・承認規則の**適用中の正本** (作成計画 [review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) と正本候補 Draft [review-approval-rules.md](review-approval-rules.md) は Draft で存在するが、**明示的なオーナー承認を経ておらず、適用中の規則正本としては成立していない**)
- 用語定義の正本

これらの正本の作成・承認フローは未決である。空の ADR ファイルや、内容を推測した規約は作成していない。レビュー・承認規則については、作成・承認フローの検討事項を Creation Plan (Draft) と [owner-decisions.md](owner-decisions.md) §4 に整理し、**2026-07-17 に §4 の全 11 確認事項へオーナー明示的回答を記録**、続いて **Task 009-3 で正本候補 Draft [review-approval-rules.md](review-approval-rules.md) を作成し、既存 Governance・各レイヤー境界との整合を確認した**。これにより正本作成の前提のうち「回答の取得・記録」と「Draft の作成・整合確認」は行われたが、上流 Open Issue の具体的解決単位・placeholder/実査待ちの個別確認主体・再評価の一部トリガー・**影響度・高／低の判定基準および判定主体**等は「残る Open Issue」として未解決である。**正本候補 Draft は存在するが、明示的なオーナー承認を経ておらず、適用中の規則正本としては成立していない。他の不足成果物 (Repository principles・命名規則・ADR・用語定義の正本) は未整備であり、正本候補 Draft の追加だけでは Travel Work Order 6 で確認された共通阻害 Fact は全面解消されない**。
