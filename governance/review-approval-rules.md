# Governance Review and Approval Rules

- Status: Draft
- Scope: Review / Approval Rules の**正本候補 Draft**。既存の 3 サービス識別子 `travel` / `rental-car` / `inbound` を含む Repository 全体を対象とする Repository 横断規則の Draft である。
- Position in Repository: `governance/review-approval-rules.md` — Governance レイヤー (全サービス横断共通)。上流入口は リポジトリ全体入口 [../README.md](../README.md) と Governance レイヤー入口 [README.md](README.md)。`owner-decisions.md`・Creation Plan・Travel の Work Order 6 成果物・各サービス成果物との関係は、Position の上流入口へ混在させず、本文 Sources (§6)・Relationship to Service Artifacts (§20)・Alignment Reassessment (§18) に分離して記載する。

本文書は Review / Approval Rules の**正本候補 Draft** であり、承認済み・適用中の規則正本ではない。Draft の作成だけでは Status は Draft から変わらず、規則は承認済み・適用中にならない。オーナーによる別途の明示的承認を必要とする。GitHub PR の approval または merge は設計承認と同一ではない。正式な設計承認は [owner-decisions.md](owner-decisions.md) の承認ログへ記録する。本 PR のマージだけでは Status を Draft から変更せず、Travel の Work Order 6 で確認された共通阻害 Fact を全面解消しない。本文書は個別候補の採用・却下、Design System の改定要否、改訂着手を承認しない。ファイル名 `review-approval-rules.md` は記述的な暫定識別子であり、命名規則の正本・恒久的な文書命名規則を確定しない (命名規則の正本は Governance に未整備、[README.md](README.md))。サービス識別子 `travel` / `rental-car` / `inbound` は暫定であり、正式名称・正式 ID として確定しない ([../README.md](../README.md) §5、[owner-decisions.md](owner-decisions.md) 確認事項 #8)。Fact / Decision / Hypothesis / Open Issue を区別する。

## 1. Purpose

- Governance README ([README.md](README.md)) が「現在不足している成果物」として明記する **レビュー・承認規則の正本** の正本候補 Draft を提示する。
- Travel の Work Order 6 (改訂着手可否評価, [../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)) が全候補共通の阻害 Fact として記録した「実際の改訂タスクの承認・反映・解決主体が Repository 内で未定義」に対し、[owner-decisions.md](owner-decisions.md) §4 に記録されたオーナー回答 (2026-07-17 取得) を規則として構造化する。
- 「規則正本候補 Draft を作成すること」と「規則を承認・適用すること」を区別する。本 PR (Task 009-3) は Creation Plan ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md)) の Ordered Creation Steps 手順 3「正本 Draft 作成」と手順 4「既存 Governance・各レイヤー境界との整合確認」までを行い、手順 5 以降 (明示的承認・Status/適用範囲の反映・適用開始・再評価) へ進まない。

## 2. Status

- 本文書の Status は `Draft` (正本候補)。
- 本文書の追加・本 PR のマージだけでは、規則は承認済み・適用中にならず、Status は Draft から変わらない。
- 本文書は Review / Approval Rules を承認済み・適用中として扱わない。全候補共通の阻害 Fact も本 Draft の作成だけでは全面解消されない。

## 3. Position

- 上流入口: リポジトリ全体入口 [../README.md](../README.md)、Governance レイヤー入口 [README.md](README.md)。
- 本文書は Governance の横断共通レイヤーに属し、特定サービス配下の成果物ではない。
- [owner-decisions.md](owner-decisions.md)・Creation Plan ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md))・Travel Work Order 6 成果物・各サービス成果物は、上流入口 (Position) ではなく Sources (§6)・Relationship to Service Artifacts (§20)・Alignment Reassessment (§18) で扱う。

## 4. Scope

- 本規則 Draft の適用範囲は、[owner-decisions.md](owner-decisions.md) §4「適用範囲」のオーナー回答どおり **Repository 横断規則** とする。既存の 3 サービス識別子 `travel` / `rental-car` / `inbound` を含む Repository 全体を対象とする。
- 対象論理レイヤー: Governance / Service Design / Screen Requirements / Design System / Assets ([../README.md](../README.md) §4)。各レイヤーの内容・仕様は本規則で再定義しない。
- 本規則は、改訂候補採否・改訂着手承認・内容レビュー・Repository 反映・未解決事項解決・GitHub 操作・設計承認記録・再評価といった**責務の区別と経路**を対象とする。

## 5. Out of Scope

- 個別の改訂内容、Design System の token / Component / version、特定候補の採否結果、上流業務仕様そのもの、実装仕様。
- Implementation (実装コード・URL・route・API・DB) は Repository 管理対象外 ([../README.md](../README.md) §10) であり、規則対象へ追加しない。
- 影響度・高／低の判定基準・判定主体の確定 (未定義。§8・§21 の Open Issue)。
- 改訂候補の採用・却下、Design System の改定要否、改訂着手の承認、候補の優先順位付け。
- ADR・命名規則・用語定義・Repository principles の正本内容 (別成果物、未整備)。
- Alignment 完了条件の確定 (本文書は記録先だが、内容は Draft 提案にとどめる。§19)。
- Travel Work Order 6 の判断の変更・再評価、Travel 固有 Work Order 6 の他サービスへの適用。
- GitHub Wiki の作成・更新、branch protection・Repository 設定の変更。
- 新しい Decision・UX Decision・正式 ID・Phase・Gate・Task 番号 (Task 009-3 を除く) の採番・定義。

## 6. Sources

規則本文は次の Repository 内直接証拠だけを根拠とする。これら以外の主体・役職・部署・承認経路を追加しない。一般的な RACI・法務承認・経営承認・事業部承認・開発承認を独自に導入しない。

- [owner-decisions.md](owner-decisions.md) §4 の 11 件のオーナー回答 (2026-07-17 取得)。
- [review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) (Creation Plan, Draft)。
- Governance レイヤー入口 [README.md](README.md)。
- リポジトリ全体入口 [../README.md](../README.md)。
- Travel の Work Order 6 成果物 [../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)。

## 7. Terms and Responsibility Separation

本規則では次の責務を**別々**に定義する。同一人物・同一部署が担うと自動的に仮定しない。「承認」「レビュー」「反映」「解決」「確認」「実行」「マージ」を同義語として扱わない。

- **改訂候補採用責務** — 改訂候補の採用・却下を決定する。
- **改訂着手承認責務** — 実際の Design System 改訂タスクの開始を承認する (候補採否とは別の判断)。
- **内容レビュー責務** — 成果物の内容をレビューする。
- **Repository 反映責務** — Repository への変更反映を確定する。
- **上流 Open Issue 解決責務** — Service Design / Screen Requirements 等の上流 Open Issue を解決・解決確認する。
- **Governance 未解決事項解決責務** — Governance・ADR・provenance・参照切れの正本作成または有効性確認を行う。
- **placeholder / 実査待ち調査責務** — placeholder・実査待ちの調査結果を確認する。
- **Alignment 再評価責務** — 改訂後の Alignment を再評価する。
- **GitHub 操作責務** — GitHub 上で commit・push・PR 作成・merge を実行する。
- **設計承認記録責務** — 設計承認の結果を承認ログへ記録する。

GitHub 上の review / approval / merge という**操作**を、設計上の**承認**と自動的に同一視しない (§15)。

## 8. Applicability

- 適用範囲は Repository 横断 (§4)。対象論理レイヤーは Governance / Service Design / Screen Requirements / Design System / Assets。各レイヤーの内容・仕様は再定義しない。
- 本規則の多くの経路は**影響度・高／低**で分岐する (§10)。ただし影響度の**判定基準**および**判定主体**は [owner-decisions.md](owner-decisions.md) §4 で未定義である。
- したがって本規則は、影響度が明示されていない変更を、いずれかの経路でレビュー済み・反映可能として扱わない。影響度の判定基準・判定主体は、本 Draft の承認前に解決が必要な Open Issue として §21 に記録する。
- 「迷ったら高」「複数サービスに及ぶなら高」等の補完ルールは追加しない (オーナー回答に存在しない)。

## 9. Decision and Approval Responsibilities

[owner-decisions.md](owner-decisions.md) §4 の回答に基づく。候補採否と改訂着手承認は**別の判断**として記録する。

- **改訂候補の採用・却下** — 決定主体: `Web部の責任者`。
- **改訂着手承認** — 承認主体: `Web部の責任者` (候補採否の決定主体と同一だが、判断としては別)。

本規則は、いずれかの候補を採用・却下しない。改訂着手を承認しない (§22)。

## 10. Content Review Rules

内容レビュー責務を影響度別に定義する ([owner-decisions.md](owner-decisions.md) §4「責務の分割」)。

- **影響度・高**: `Web部責任者` および `チーフデザイナー`。両者のレビューを必要とする。
- **影響度・低**: `Web部レビュー担当者`。

影響度・高では、Web部責任者・チーフデザイナー双方のレビューを欠く場合、内容レビュー完了として扱わない。影響度の判定基準・判定主体は未定義 (§8・§21)。

## 11. Repository Reflection Rules

Repository 反映責務を影響度別に定義する ([owner-decisions.md](owner-decisions.md) §4「責務の分割」)。

- **影響度・高**: Web部責任者・チーフデザイナーの必須レビュー (§10) を反映確定の前提 (ゲート) とする。
- **影響度・低**: Web部レビュー担当者のレビューを反映確定の前提とする (Web部責任者・チーフデザイナーの必須レビューは前提としない)。

反映確定 (前提となるレビューの充足) と、GitHub 上の merge 操作 (§14) と、設計承認 (§15) は別の事象として扱う。

## 12. Unresolved Issue Handling

上流 Open Issue (Service Design / Screen Requirements 等) の解決・解決確認主体を影響度別に定義する ([owner-decisions.md](owner-decisions.md) §4「上流 Open Issue の解決単位」)。

- **影響度・高**: Web部責任者・チーフデザイナー。
- **影響度・低**: Web部レビュー担当者。

解決単位 (全体共通／成果物別／論点別) は案件ごとに決定する。全体共通・成果物別・論点別のいずれかを自動適用しない。案件ごとの具体的な振り分けは未定であり、Open Issue として残る (§21)。

## 13. Governance / ADR / Provenance Handling

Governance・ADR・provenance・参照切れについて、正本作成または有効性確認の主体を影響度別に定義する ([owner-decisions.md](owner-decisions.md) §4「Governance 正本の担当」)。

- **影響度・高**: Web部責任者・チーフデザイナー。
- **影響度・低**: Web部レビュー担当者。

本規則は、ADR・命名規則の具体的な形式・内容を作成しない (別成果物・未整備)。

## 14. Placeholder / Inspection-Pending Handling

placeholder・実査待ちの取り扱いを定義する ([owner-decisions.md](owner-decisions.md) §4「placeholder / 実査待ちの確認主体」)。

- 確認方法を決める主体: `Web部責任者`。
- 個別項目の確認主体: 確認ルールが制定されるまで未定。

Web部責任者が確認方法および個別項目の確認主体を明示し、その記録が Repository 内に存在するまで、placeholder・実査待ちの項目を解決済みとして扱わない。具体的な検査方法・合格基準・担当者は本規則で推測・確定しない (§21)。

## 15. GitHub Operations and Design Approval

GitHub 操作と設計承認を分離する ([owner-decisions.md](owner-decisions.md) §4「GitHub 操作と設計承認の関係」、[../README.md](../README.md) §2・§3)。

- GitHub 操作責務の割当: commit・push・PR 作成 = `作業担当者` (改訂作業の実施者)。merge = レビュー後にレビュアーが実行する (影響度・高 = Web部責任者・チーフデザイナー、影響度・低 = Web部レビュー担当者)。
- GitHub PR の approval・merge は Repository 操作であり、設計承認とは別責務である。merge だけでは設計承認済みにならない。merge を設計承認記録の代替にしない。
- 設計承認の直接証拠は [owner-decisions.md](owner-decisions.md) の承認ログである (§16)。
- GitHub Wiki は利用者向け説明の**非正本**であり、設計判断・正式仕様・ADR・Design System の正本を置かない ([../README.md](../README.md) §3)。Repository 本体と Wiki が矛盾する場合は Repository 本体を優先する。
- 本規則は Wiki を作成・更新しない。

## 16. Approval Record

設計承認ログの正本を [owner-decisions.md](owner-decisions.md) とする ([owner-decisions.md](owner-decisions.md) §4「承認結果の記録先」)。利用者向けに示すべき内容は別途 Wiki に文書として記録しうるが、Wiki は非正本である (§15)。

承認ログの記録項目として、Draft 提案として少なくとも次を提案する (これらは追跡項目であり、新しい Decision ID 体系・正式 Status 体系ではない)。

- 承認対象
- 承認内容
- 承認日
- 承認主体
- 適用範囲
- 根拠となる成果物または PR
- 条件付き承認の場合の条件
- 残る Open Issue

本 PR では承認ログの実データを追加しない。上記は将来のオーナー承認時に記録される項目の提案である。

## 17. Rule Draft / Approval / Application Lifecycle

規則の状態遷移を次のとおり区別する。正式 Status 体系は新設せず、現在 Status は `Draft` のみとする。

1. Draft 作成。
2. 既存 Governance・各レイヤー境界との整合確認。
3. オーナーによる明示的承認。
4. Status・適用範囲を承認結果どおり反映。
5. 規則の適用開始。
6. 規則の変更。
7. 規則の廃止。

Task 009-3 は手順 1 (Draft 作成) と手順 2 (整合確認) までを行う。手順 3 以降 (明示的承認・Status/適用範囲の反映・適用開始・変更・廃止) には進まない。本 PR のマージだけでは Status を Draft から変更しない。

### 整合確認結果 (手順 2, 2026-07-17)

既存 Governance・各レイヤー境界と本 Draft の整合を確認した (Task 009-3 手順 4 に対応)。

- **適用範囲 (Repository 横断)** — Governance が全サービス横断共通レイヤーである点 ([README.md](README.md)、[../README.md](../README.md) §4) と整合する。矛盾なし。
- **承認ログ = owner-decisions.md / Wiki = 非正本** — Repository 本体を正本、Wiki を非正本とする root README §2・§3 と整合する。矛盾なし。
- **サービス識別子の暫定扱い** — `travel` / `rental-car` / `inbound` を暫定識別子とし確定しない点は root README §5・owner-decisions.md 確認事項 #8 と整合する。矛盾なし。
- **各レイヤー内容を再定義しない** — 対象レイヤーの内容・仕様を本規則で再定義せず、責務・経路のみを扱う点は各サービス配下で内容を管理する構造 ([../README.md](../README.md) §4) と整合する。矛盾なし。
- **影響度判定の未定義** — 影響度・高／低の判定基準・判定主体が未定義である点は、既存記述と矛盾しないが、本 Draft の承認前に解決が必要な Open Issue として残る (§21)。

## 18. Alignment Reassessment

Travel Work Order 6 の再評価に関する規則を、[owner-decisions.md](owner-decisions.md) §4「再評価の条件」に基づき記録する。

- 再評価は暫定的に**全候補一括**で行う。
- 最初の再評価トリガーは、承認・反映・解決主体の**定義・Repository 内記録**である (全候補共通の阻害 Fact の解消)。
- 参照切れ・placeholder / 実査待ちの解消は、最初の再評価の**必須条件ではない**。
- 上流 Open Issue・provenance 未確認を必須トリガーとするかは**未確定** (§21)。

本 Draft の作成だけで再評価トリガーが満たされたとは判定しない。本規則の明示的承認・適用開始の**前**に Work Order 6 を再評価しない。Travel 固有の Work Order 6 を他サービスへ適用しない。Work Order 6 成果物は評価 snapshot の記録として保持し、本タスクで書き換えない。

## 19. Alignment Completion Conditions

Fact: Alignment 完了条件の記録先は本文書である ([owner-decisions.md](owner-decisions.md) §4「Alignment 完了条件の所在」)。ただし完了条件の**具体的内容は未定義**である。

以下は**オーナーレビュー対象の Draft 提案**であり、承認済みの完了条件ではない。

- 対象範囲が明示されている。
- 対象範囲の評価記録が存在する。
- 阻害 Fact と未解決事項の状態が追跡可能である。
- 改定・非改定・継続保留の判断が記録されている。
- 必要な設計承認が承認ログ ([owner-decisions.md](owner-decisions.md)) に存在する。
- 完了後も残る Open Issue が明示されている。

数値スコア・適合率・pass/fail・severity・優先順位は導入しない。上記は観点の Draft 提案であり、確定・承認された完了条件ではない。

## 20. Relationship to Service Artifacts

- 本規則は Repository 横断であり、各サービス (`travel` / `rental-car` / `inbound`) 配下の成果物 (Service Design / Screen Requirements / Design System / Assets) の**内容を再定義しない**。責務と経路のみを対象とする。
- Travel の Work Order 6 成果物は、全候補共通の阻害 Fact「承認・反映・解決主体が Repository 内で未定義」の出所であり (§6)、本規則はその主体をオーナー回答に基づき定義する。Work Order 6 の判断そのものは変更・再評価しない (§18)。
- 各サービスの Design System 改訂タスクは、本規則が明示的に承認・適用されるまで、承認・反映・解決主体の定義を根拠に開始できない (Travel Work Order 6 の総合判断)。本 Draft の作成だけでは改訂着手を承認しない。
- 本規則の追加は、下流の Design System・token・Component・version に変更を与えない。

## 21. Open Issues

本 Draft の承認前または将来解決すべき Open Issue を記録する。

- **影響度・高／低の判定基準および判定主体が未定義** (§8)。本 Draft の承認前に解決が必要。判定基準・判定主体を本規則で推測・確定しない。
- 上流 Open Issue の具体的な**解決単位** (全体共通／成果物別／論点別) は案件ごと・未定 (§12)。
- placeholder / 実査待ちの**個別項目の確認主体**は、確認ルール制定まで未定 (§14)。
- 改訂着手可否の再評価で、**上流 Open Issue・provenance 未確認を必須トリガーとするか**は未確定 (§18)。
- Alignment 完了条件の**具体的内容**は未定義。本文書の §19 は Draft 提案であり承認済みではない。
- 本規則は未承認・未適用。本 Draft の作成・本 PR のマージは、規則の承認・適用や Work Order 6 共通阻害 Fact の全面解消を意味しない。
- 命名規則・ADR・用語定義・Repository principles の正本不在 ([README.md](README.md)) は本規則では解決しない。

## 22. Does Not Decide

本文書は以下を決定・実施しない。

- Draft のオーナー承認、Status の昇格、規則の適用開始。
- 影響度・高／低の判定基準・判定主体の確定、個別変更の影響度判定。
- 改訂候補の採用・却下、Design System 改定要否の決定、改訂着手承認。
- Work Order 6 の再評価、Alignment 完了判定、Design System 改定。
- ADR・命名規則・用語定義・Repository principles の作成。
- GitHub Wiki の作成・更新、branch protection・Repository 設定の変更。
- 承認ログの実データの追加。
- Task 009-3 以外の新しい Task 番号・Decision・UX Decision・正式 ID・Phase・Gate の追加。

## 23. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-17 | Task 009-3: Review / Approval Rules の正本候補 Draft を作成。[owner-decisions.md](owner-decisions.md) §4 の 11 件のオーナー回答 (2026-07-17) を根拠に、責務区別・影響度別のレビュー/反映/GitHub 操作経路・設計承認と GitHub 操作の分離・承認ログ正本・ライフサイクル・再評価条件・Alignment 完了条件の Draft 提案を構造化。Creation Plan Ordered Creation Steps 手順 3 (Draft 作成)・手順 4 (整合確認) に対応。規則は未承認・未適用 (Status = Draft)、影響度判定基準・判定主体は未定義の Open Issue、Work Order 6 は未再評価、Design System 改定は未着手 | Draft |
