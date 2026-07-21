# Governance Review and Approval Rules

- Status: 承認済み・適用中
- Scope: Review / Approval Rules の正本。オーナー（Web部責任者）による明示的承認済み（2026-07-17、Task 009-4）。既存の 3 サービス識別子 `travel` / `rental-car` / `inbound` を含む Repository 全体を対象とする Repository 横断規則である。適用開始条件（本承認記録 PR (Task 009-4) の main マージ）は PR #67 のマージ（merge commit d095ded）で成立し、現在は適用中である。
- Position in Repository: `governance/review-approval-rules.md` — Governance レイヤー (全サービス横断共通)。上流入口は リポジトリ全体入口 [../README.md](../README.md) と Governance レイヤー入口 [README.md](README.md)。`owner-decisions.md`・Creation Plan・Travel の Work Order 6 成果物・各サービス成果物との関係は、Position の上流入口へ混在させず、本文 Sources (§6)・Relationship to Service Artifacts (§20)・Alignment Reassessment (§18) に分離して記載する。

本文書は Review / Approval Rules の**正本**であり、オーナー（Web部責任者）による明示的承認を 2026-07-17 (Task 009-4) に得た。承認の直接証拠は [owner-decisions.md](owner-decisions.md) の設計承認ログである。**Status（承認）と適用開始は分離する**: 本規則は Task 009-4 で承認済みであり、適用開始条件（本承認記録 PR (Task 009-4) の main マージ）は PR #67 のマージ（merge commit d095ded）で成立したため、現在は**適用中**である。GitHub PR の approval または merge は設計承認と同一ではない（設計承認は上記承認ログに記録済み）。PR #67 のマージは既に承認された適用開始条件を満たした Fact であって、それ自体が設計承認ではない。本規則の承認は、Travel の Work Order 6 の評価結果を自動的に変更せず、適用開始前に共通阻害 Fact を全面解消しない。本文書は個別候補の採用・却下、Design System の改定要否、改訂着手を承認しない。ファイル名 `review-approval-rules.md` は記述的な暫定識別子であり、命名規則の正本・恒久的な文書命名規則を確定しない (命名規則の正本は Governance に未整備、[README.md](README.md))。サービス識別子 `travel` / `rental-car` / `inbound` は暫定であり、正式名称・正式 ID として確定しない ([../README.md](../README.md) §5、[owner-decisions.md](owner-decisions.md) 確認事項 #8)。Fact / Decision / Hypothesis / Open Issue を区別する。

## 1. Purpose

- Governance README ([README.md](README.md)) が不足成果物として挙げていた **レビュー・承認規則の正本** を提示する。本文書は当該正本であり、Task 009-4 で承認され、PR #67 の main マージで適用開始した。
- Travel の Work Order 6 (改訂着手可否評価, [../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)) が全候補共通の阻害 Fact として記録した「実際の改訂タスクの承認・反映・解決主体が Repository 内で未定義」に対し、[owner-decisions.md](owner-decisions.md) §4 に記録されたオーナー回答 (2026-07-17 取得) を規則として構造化する。
- 「規則正本候補 Draft を作成すること」と「規則を承認・適用すること」を区別する。工程を次のとおり区別して記録する: **Task 009-3** が Creation Plan ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md)) の Ordered Creation Steps 手順 3「正本 Draft 作成」と手順 4「整合確認」、**Task 009-4** がオーナー（Web部責任者）による明示的承認と Status・適用範囲の反映（手順 5・6）、**PR #67 の main マージ** が承認済み規則の適用開始条件（本承認記録 PR の main マージ）の成立である。手順 7（Travel Work Order 6 再評価）は **Task 009-6 (2026-07-21) で実施済み**（[../services/travel/design-system/alignment-amendment-readiness-reassessment.md](../services/travel/design-system/alignment-amendment-readiness-reassessment.md)、§18）。

## 2. Status

- 本文書の Status は `承認済み・適用中`。オーナー（Web部責任者）による明示的承認を 2026-07-17 (Task 009-4) に取得し、適用開始条件（本承認記録 PR の main マージ）は PR #67 のマージ（merge commit d095ded）で成立した。承認の直接証拠は [owner-decisions.md](owner-decisions.md) の設計承認ログ。
- **承認と適用開始は分離する**。承認 (Task 009-4) と適用開始（適用開始条件＝本承認記録 PR の main マージの成立）は別事象である。適用開始条件は PR #67 のマージ（merge commit d095ded）で成立し、現在は適用中である。
- 承認は Review / Approval Rules を Repository 横断規則として有効化する意思決定であり、適用開始（実運用）とは別事象である。全候補共通の阻害 Fact は、規則の適用開始後に当該範囲で解消へ進むものであり、承認・適用開始だけで自動的に全面解消されるものではない（Work Order 6 は Task 009-6 (2026-07-21) で再評価済み: 旧共通阻害 Fact は規則で定義された範囲において解消したが、候補固有の阻害 Fact が残り全 12 候補「現時点では開始できない」を維持・Alignment は未完了。[../services/travel/design-system/alignment-amendment-readiness-reassessment.md](../services/travel/design-system/alignment-amendment-readiness-reassessment.md)）。

## 3. Position

- 上流入口: リポジトリ全体入口 [../README.md](../README.md)、Governance レイヤー入口 [README.md](README.md)。
- 本文書は Governance の横断共通レイヤーに属し、特定サービス配下の成果物ではない。
- [owner-decisions.md](owner-decisions.md)・Creation Plan ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md))・Travel Work Order 6 成果物・各サービス成果物は、上流入口 (Position) ではなく Sources (§6)・Relationship to Service Artifacts (§20)・Alignment Reassessment (§18) で扱う。

## 4. Scope

- 本規則の適用範囲は、[owner-decisions.md](owner-decisions.md) §4「適用範囲」のオーナー回答どおり **Repository 横断規則** とする。既存の 3 サービス識別子 `travel` / `rental-car` / `inbound` を含む Repository 全体を対象とする。
- 対象論理レイヤー: Governance / Service Design / Screen Requirements / Design System / Assets ([../README.md](../README.md) §4)。各レイヤーの内容・仕様は本規則で再定義しない。
- 本規則は、改訂候補採否・改訂着手承認・内容レビュー・Repository 反映・未解決事項解決・GitHub 操作・設計承認記録・再評価といった**責務の区別と経路**を対象とする。

## 5. Out of Scope

- 個別の改訂内容、Design System の token / Component / version、特定候補の採否結果、上流業務仕様そのもの、実装仕様。
- Implementation (実装コード・URL・route・API・DB) は Repository 管理対象外 ([../README.md](../README.md) §10) であり、規則対象へ追加しない。
- 影響度・高／低の明文判定基準の確定 (現時点では設けられない。§8・§21 の Open Issue。判定主体は Web部責任者の都度判断として定義済み)。
- 改訂候補の採用・却下、Design System の改定要否、改訂着手の承認、候補の優先順位付け。
- ADR・命名規則・用語定義・Repository principles の正本内容 (別成果物、未整備)。
- Alignment 完了判定・Work Order 6 相当の再評価の実施 (§19 の完了条件は承認済みだが、判定は本規則では行わない)。
- Travel Work Order 6 の判断の変更・再評価、Travel 固有 Work Order 6 の他サービスへの適用。
- branch protection・Repository 設定の変更。
- 新しい Decision・UX Decision・正式 ID・Phase・Gate・Task 番号 (Task 009-3・Task 009-4 を除く) の採番・定義。

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
- 本規則の多くの経路は**影響度・高／低**で分岐する (§10)。
- **影響度の判定主体**: 各変更を影響度・高／低へ分類する判定は **Web部責任者が案件ごとに都度行う**（判定に異議・不明点がある場合の最終判断主体も Web部責任者）。この判定主体は Task 009-4 (2026-07-17) のオーナー回答により定義済みである。
- **影響度の判定結果の記録**: Web部責任者による判定結果は Wiki（非正本、[../README.md](../README.md) §3）に、変更対象・影響度（高／低）・判定日・判定者・参照（PR／成果物）とともに記録する。影響度が明示（判定・記録）されていない変更を、いずれかの経路でレビュー済み・反映可能として扱わない。
- **影響度の明文判定基準**: 高／低を分ける明文の内容基準は現時点では設けられない（Task 009-4 オーナー回答）。これは承認後も残る Open Issue として §21 に保持する。判定主体（Web部責任者の都度判断）が定義済みであるため、明文基準の不在は規則の運用停止要因とはしない。
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

影響度・高では、Web部責任者・チーフデザイナー双方のレビューを欠く場合、内容レビュー完了として扱わない。影響度の判定主体は Web部責任者の都度判断として定義済みであり、明文の判定基準は未整備の Open Issue (§8・§21)。

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
- 影響度判定結果 (§8) および利用者向けの規則説明は Wiki (非正本) に記録しうる。Wiki への記録は正本の記録ではなく、設計承認の直接証拠とはならない (設計承認の直接証拠は owner-decisions.md の承認ログ)。

## 16. Approval Record

設計承認ログの正本を [owner-decisions.md](owner-decisions.md) とする ([owner-decisions.md](owner-decisions.md) §4「承認結果の記録先」)。利用者向けに示すべき内容は別途 Wiki に文書として記録しうるが、Wiki は非正本である (§15)。

承認ログの記録項目は次のとおりとする (これらは追跡項目であり、新しい Decision ID 体系・正式 Status 体系ではない)。

- 承認対象
- 承認内容
- 承認日
- 承認主体
- 適用範囲
- 根拠となる成果物または PR
- 適用開始条件
- 条件付き承認の場合の条件
- 承認後も残る Open Issue

本規則自体の設計承認ログは、Task 009-4 (2026-07-17) に [owner-decisions.md](owner-decisions.md) の設計承認ログへ記録した。

## 17. Rule Draft / Approval / Application Lifecycle

規則の状態遷移を次のとおり区別する。正式 Status 体系は新設しない（Status は運用状態を表す記述であり、番号化された正式体系ではない）。

1. Draft 作成。
2. 既存 Governance・各レイヤー境界との整合確認。
3. オーナーによる明示的承認。
4. Status・適用範囲を承認結果どおり反映。
5. 規則の適用開始。
6. 規則の変更。
7. 規則の廃止。

Task 009-3 は手順 1 (Draft 作成) と手順 2 (整合確認) を実施した。**Task 009-4 (2026-07-17) は手順 3 (オーナー＝Web部責任者による明示的承認) と手順 4 (Status・適用範囲を承認結果どおり反映) を実施した**。手順 5 (規則の適用開始) は**本承認記録 PR の main マージ**を条件とし、この条件は PR #67 のマージ（merge commit d095ded）で成立したため、規則は現在**適用中**である。手順 6・7 (変更・廃止) は将来。PR #67 のマージは手順 5 (適用開始) の条件を満たした Fact であって、設計承認そのものではない（設計承認は手順 3 で取得済み・[owner-decisions.md](owner-decisions.md) 承認ログに記録）。

### 整合確認結果 (手順 2, 2026-07-17)

既存 Governance・各レイヤー境界と本 Draft の整合を確認した (Task 009-3 手順 4 に対応)。

- **適用範囲 (Repository 横断)** — Governance が全サービス横断共通レイヤーである点 ([README.md](README.md)、[../README.md](../README.md) §4) と整合する。矛盾なし。
- **承認ログ = owner-decisions.md / Wiki = 非正本** — Repository 本体を正本、Wiki を非正本とする root README §2・§3 と整合する。矛盾なし。
- **サービス識別子の暫定扱い** — `travel` / `rental-car` / `inbound` を暫定識別子とし確定しない点は root README §5・owner-decisions.md 確認事項 #8 と整合する。矛盾なし。
- **各レイヤー内容を再定義しない** — 対象レイヤーの内容・仕様を本規則で再定義せず、責務・経路のみを扱う点は各サービス配下で内容を管理する構造 ([../README.md](../README.md) §4) と整合する。矛盾なし。
- **影響度判定** — 影響度・高／低の判定主体は Web部責任者の都度判断として定義済みである (§8、Task 009-4 オーナー回答)。明文の判定基準は未整備だが、承認前の解決を要さず、承認後も残る Open Issue として保持する (§21)。

## 18. Alignment Reassessment

Travel Work Order 6 の再評価に関する規則を、[owner-decisions.md](owner-decisions.md) §4「再評価の条件」に基づき記録する。

- 再評価は暫定的に**全候補一括**で行う。
- 最初の再評価トリガーは、承認・反映・解決主体の**定義・Repository 内記録**である (全候補共通の阻害 Fact の解消)。
- 参照切れ・placeholder / 実査待ちの解消は、最初の再評価の**必須条件ではない**。
- 上流 Open Issue・provenance 未確認を必須トリガーとするかは**未確定** (§21)。

本規則の作成だけで再評価トリガーが満たされたとは判定しない。本規則の明示的承認・適用開始の**前**に Work Order 6 を再評価しない。Travel 固有の Work Order 6 を他サービスへ適用しない。Work Order 6 成果物は評価 snapshot の記録として保持し、本タスクで書き換えない。

## 19. Alignment Completion Conditions

Fact: Alignment 完了条件の記録先は本文書である ([owner-decisions.md](owner-decisions.md) §4「Alignment 完了条件の所在」)。

以下の 6 観点を Alignment 完了条件として、オーナー（Web部責任者）が 2026-07-17 (Task 009-4) に**承認**した。

- 対象範囲が明示されている。
- 対象範囲の評価記録が存在する。
- 阻害 Fact と未解決事項の状態が追跡可能である。
- 改定・非改定・継続保留の判断が記録されている。
- 必要な設計承認が承認ログ ([owner-decisions.md](owner-decisions.md)) に存在する。
- 完了後も残る Open Issue が明示されている。

数値スコア・適合率・pass/fail・severity・優先順位は導入しない。上記は承認済みの完了条件の観点であり、将来 Work Order 6 相当の Alignment 再評価で「完了」を判定する際の基準となる。本規則の承認および本 Task では Work Order 6 の再評価・Alignment 完了判定は行わない（完了条件を定めるにとどめる）。

## 20. Relationship to Service Artifacts

- 本規則は Repository 横断であり、各サービス (`travel` / `rental-car` / `inbound`) 配下の成果物 (Service Design / Screen Requirements / Design System / Assets) の**内容を再定義しない**。責務と経路のみを対象とする。
- Travel の Work Order 6 成果物は、全候補共通の阻害 Fact「承認・反映・解決主体が Repository 内で未定義」の出所であり (§6)、本規則はその主体をオーナー回答に基づき定義する。Work Order 6 の判断そのものは変更・再評価しない (§18)。
- 各サービスの Design System 改訂タスクは、本規則が明示的に承認・適用されるまで、承認・反映・解決主体の定義を根拠に開始できない (Travel Work Order 6 の総合判断)。本規則の承認・適用（PR #67 マージ）だけでは改訂着手を承認しない（改訂着手可否は Work Order 6 の再評価で判断される。Work Order 6 は Task 009-6 (2026-07-21) で再評価済みであり、全 12 候補「現時点では開始できない」・実際の Design System 改訂タスクは現時点では開始できない = 各候補固有の阻害 Fact が残るため。改訂着手の承認は行われていない）。
- 本規則の追加は、下流の Design System・token・Component・version に変更を与えない。

## 21. Open Issues

本規則の承認後も残る Open Issue を記録する。オーナー (Web部責任者) は Task 009-4 (2026-07-17) で、以下をいずれも**承認後に持ち越す Open Issue** として扱うことを承認した（承認前の追加解決を要求しない）。

- **影響度・高／低の明文判定基準は現時点では設けられない** (§8)。判定主体は Web部責任者の都度判断として定義済みだが、明文の内容基準は未整備であり承認後も残る。判定基準を本規則で推測・補完しない。
- 上流 Open Issue の具体的な**解決単位** (全体共通／成果物別／論点別) は案件ごと・未定 (§12)。
- placeholder / 実査待ちの**個別項目の確認主体**は、Web部責任者が確認方法を定めるまで未定 (§14)。
- 改訂着手可否の再評価で、**上流 Open Issue・provenance 未確認を必須トリガーとするか**は未確定 (§18)。
- 命名規則・ADR・用語定義・Repository principles の正本不在 ([README.md](README.md)) は本規則では解決しない。
- **適用開始は PR #67 の main マージ（merge commit d095ded）で成立済み**であり、現在は適用中である。ただし承認・適用開始だけで、Work Order 6 共通阻害 Fact が全面解消されるわけではない（Work Order 6 は Task 009-6 (2026-07-21) で再評価済み、§18。旧共通阻害 Fact は規則で定義された範囲において解消したが、候補固有の阻害 Fact — 上流 Open Issue・provenance 未確認・参照切れ・placeholder・実査待ち・placeholder/実査待ちの個別確認主体の未定 — が残り、全 12 候補「現時点では開始できない」を維持）。

## 22. Does Not Decide

本規則は以下を決定・実施しない。

- 規則の適用開始そのものの宣言（適用開始は PR #67 の main マージで成立した Fact であり、本文書自体が適用開始を宣言・決定するものではない）。
- 影響度・高／低の明文判定基準の確定、および個別変更の影響度判定そのもの（実際の分類は Web部責任者が案件ごとに都度行う）。
- 改訂候補の採用・却下、Design System 改定要否の決定、改訂着手承認。
- Work Order 6 の再評価、Alignment 完了判定、Design System 改定。
- ADR・命名規則・用語定義・Repository principles の作成。
- branch protection・Repository 設定の変更。
- Task 009-4 以外の新しい Task 番号・Decision・UX Decision・正式 ID・Phase・Gate の追加。

## 23. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-17 | Task 009-3: Review / Approval Rules の正本候補 Draft を作成。[owner-decisions.md](owner-decisions.md) §4 の 11 件のオーナー回答 (2026-07-17) を根拠に、責務区別・影響度別のレビュー/反映/GitHub 操作経路・設計承認と GitHub 操作の分離・承認ログ正本・ライフサイクル・再評価条件・Alignment 完了条件の Draft 提案を構造化。Creation Plan Ordered Creation Steps 手順 3 (Draft 作成)・手順 4 (整合確認) に対応。規則は未承認・未適用 (Status = Draft)、影響度判定基準・判定主体は未定義の Open Issue、Work Order 6 は未再評価、Design System 改定は未着手 | Draft |
| 2026-07-17 | Task 009-4: オーナー（Web部責任者）が Review / Approval Rules を Repository 横断規則として明示的に承認 (Creation Plan 手順 5 相当・本文書ライフサイクル手順 3)。Status を「承認済み（未適用・main マージ後に適用開始）」へ変更し適用範囲を反映 (手順 4)。影響度の判定主体を Web部責任者の都度判断として定義 (§8)、判定結果は Wiki（非正本）に記録、明文の判定基準は承認後も残る Open Issue。§19 Alignment 完了条件の 6 観点を承認済みへ格上げ。設計承認ログは owner-decisions.md へ記録。適用開始は本承認記録 PR の main マージ後（現時点では未適用）、Work Order 6 は未再評価、Design System 改定は未着手 | 承認済み（未適用・main マージ後に適用開始） |
| 2026-07-17 | Task 009-5: PR #67（Task 009-4 承認記録）の main マージ（merge commit d095ded2998e0180ae6836747e8fbbd95a7a2ef1）により、承認時に定めた適用開始条件が成立した事実を反映。Status を「承認済み・適用中」へ同期し、「未適用」「main マージ後に適用開始」等のマージ前表現を現在状態へ更新。§1 Purpose を Task 009-3（Draft 作成・整合確認）／Task 009-4（明示的承認・反映）／PR #67 マージ（適用開始条件成立）に区別。承認内容・責務・影響度別経路・Alignment 完了条件・残る Open Issue は不変。PR #67 のマージは設計承認ではなく適用開始条件成立の Fact。Work Order 6 は未再評価、Design System 改定は未着手 | 承認済み・適用中 |
| 2026-07-21 | Task 009-6: Travel Work Order 6 の再評価 ([../services/travel/design-system/alignment-amendment-readiness-reassessment.md](../services/travel/design-system/alignment-amendment-readiness-reassessment.md), Draft, snapshot `e0880d8`) を実施したことに伴い、§1・§2・§20・§21 の現在状態記述（「Work Order 6 は未再評価」「手順 7 は未実施」）を再評価済みの状態へ同期。**規則本文・責務 (§7〜§16)・承認内容 (§9・§16)・§18 の再評価規則・§19 Alignment 完了条件・Status（承認済み・適用中）は不変。** 再評価では旧共通阻害 Fact が規則で定義された範囲において解消したが候補固有の阻害 Fact が残り全 12 候補「現時点では開始できない」・Alignment 未完了 (§19 観点 4・5 未充足)。owner-decisions.md §5/§6・設計承認は不変。候補採否・改定要否・改訂着手・設計承認・Design System 改定は行っていない（状態同期のみ） | 承認済み・適用中 |
