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

- [owner-decisions.md](owner-decisions.md) — オーナー確認事項 (分類C) の一覧。既存資産として移行済。§4 に Review / Approval Rules 作成前に必要な確認事項を独立節として記録し、**2026-07-17 に全 11 項目のオーナー明示的回答を「オーナー回答」列へ記録済み**（残る条件・未定は「残る Open Issue」列へ分離）。**§5 に設計承認ログ (Design Approval Log) を §1〜§4 と分離して追加し、Task 009-4 (2026-07-17) の Review / Approval Rules 承認を記録**（設計承認の直接証拠の正本。GitHub merge を設計承認と同一視しない）。**§6 に適用開始の事実記録 (Activation Record) を追加し、PR #67 の main マージ（merge commit d095ded）で適用開始条件が成立した Fact を設計承認と分離して記録**（merge は設計承認ではなく適用開始条件成立の Fact）。
- [review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) (Draft) — レビュー・承認規則の**正本を作成するための計画**。正本作成前に必要なオーナー確認事項・証拠・責務境界・作成順を整理する。§8 に回答取得状況、§11 Entry Conditions に正本作成前提の項目別評価を反映済み。§12・§13・§16 に Task 009-3 (正本候補 Draft 作成・整合確認)・Task 009-4 (明示的承認・Status 反映)・Task 009-5 (適用開始条件成立) の進捗を反映済み。本文書は計画であって正本そのものではなく、規則の作成・承認・適用開始そのものは [review-approval-rules.md](review-approval-rules.md) と [owner-decisions.md](owner-decisions.md) §5・§6 に記録される。
- [review-approval-rules.md](review-approval-rules.md) (承認済み・適用中) — レビュー・承認規則の正本。owner-decisions.md §4 の 11 件のオーナー回答を根拠に構造化し、Task 009-3 で正本候補 Draft を作成、**Task 009-4 (2026-07-17) でオーナー (Web部責任者) が Repository 横断規則として明示的に承認**、**PR #67 の main マージ（merge commit d095ded）で適用開始条件が成立し適用中**となった (Status = 承認済み・適用中)。承認の直接証拠は [owner-decisions.md](owner-decisions.md) §5 設計承認ログ、適用開始の事実記録は §6。影響度の判定主体は Web部責任者の都度判断として定義済み、明文の判定基準は承認後も残る Open Issue、Alignment 完了条件 (§19 6 観点) は承認済み。Work Order 6 は Task 009-6 (2026-07-21) で再評価済み ([../services/travel/design-system/alignment-amendment-readiness-reassessment.md](../services/travel/design-system/alignment-amendment-readiness-reassessment.md), Draft): 旧共通阻害 Fact は規則で定義された範囲において解消したが候補固有の阻害 Fact が残り全 12 候補「現時点では開始できない」・Alignment は未完了。Design System 改定は未着手。承認・適用開始だけでは他の不足成果物は整備されない。

## 現在不足している成果物

以下は正本が存在しない。本 bootstrap では新規作成しない。**不足している成果物を、存在するものとして扱ってはならない。**

- Repository principles の正本
- 命名規則の正本 (例: 既存 Design System 文書が参照する `governance/naming-rules.md` は未作成)
- ADR の正本
- 用語定義の正本

レビュー・承認規則については、**Task 009-4 (2026-07-17) でオーナー (Web部責任者) が [review-approval-rules.md](review-approval-rules.md) を Repository 横断規則として明示的に承認**し ([owner-decisions.md](owner-decisions.md) §5 設計承認ログ)、**適用開始条件（本承認記録 PR の main マージ）は PR #67 のマージ（merge commit d095ded）で成立した**ため、現在は**適用中**である ([owner-decisions.md](owner-decisions.md) §6 適用開始の事実記録)。GitHub の merge は設計承認と同一視しない (設計承認は §5、merge は適用開始条件成立の Fact)。影響度の判定主体は Web部責任者の都度判断として定義済みだが、明文の判定基準・上流 Open Issue の具体的解決単位・placeholder/実査待ちの個別確認主体・再評価の一部トリガーは「承認後も残る Open Issue」として未解決である。**Repository principles・命名規則・ADR・用語定義の正本は依然として未整備**であり、空の ADR ファイルや内容を推測した規約は作成していない。Review / Approval Rules の承認・適用開始だけでは他の不足成果物は整備されず、Travel Work Order 6 で確認された共通阻害 Fact も全面解消されるものではない (**Work Order 6 は Task 009-6 (2026-07-21) で再評価済み: 旧共通阻害 Fact は規則で定義された範囲において解消したが、候補固有の阻害 Fact が残り全 12 候補「現時点では開始できない」・Alignment は未完了。Design System 改定は未着手**)。
