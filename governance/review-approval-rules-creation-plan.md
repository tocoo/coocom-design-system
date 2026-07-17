# Governance Review and Approval Rules Creation Plan

- Status: Draft
- Scope: Governance レイヤーが不足成果物として明記する「レビュー・承認規則の正本」を作成するための計画。正本作成前に、オーナー確認が必要な事項・必要な証拠・責務境界・作成順を整理する。本文書自体は Review / Approval Rules の正本ではなく、規則本文・承認主体・改定開始の承認を定義しない。
- Position in Repository: `governance/review-approval-rules-creation-plan.md` — Governance レイヤー (全サービス横断共通)。上流入口は リポジトリ全体入口 [../README.md](../README.md) と Governance レイヤー入口 [README.md](README.md)。`owner-decisions.md`・Travel の Work Order 6 成果物・各サービス成果物との関係は、Position の上流成果物へ混在させず、本文 Sources (§6)・Relationship to Travel Work Order 6 (§14)・Downstream Impact (§15) に分離して記載する。

本文書は計画 (Creation Plan) であり、Review / Approval Rules の正本ではない。ファイル名 `review-approval-rules-creation-plan.md` は記述的な暫定識別子であり、正式な命名規則・分類体系・評価 ID を確定しない (命名規則の正本は Governance に未整備、[README.md](README.md))。本文書は人・部署・役職を承認主体・反映主体・解決主体へ割り当てず、規則の具体本文を書かず、GitHub 上の review / approval / merge という操作を設計上の承認と自動的に同一視しない。Travel の Work Order 6 の判断を変更・再評価せず、Design System 改定の開始を承認しない。新しい Decision・UX Decision・正式 ID・Phase・Gate・Task 番号を採番・定義しない。Fact / Decision / Hypothesis / Open Issue を区別する。

## 1. Purpose

- Governance README ([README.md](README.md)) が「現在不足している成果物」として明記する **レビュー・承認規則の正本** を、将来作成するための準備計画を定義する。
- Travel の Work Order 6 (改訂着手可否評価, [../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)) で全候補共通の阻害 Fact として確認された「実際の改訂タスクの承認・反映・解決主体が Repository 内で未定義であること」と、本計画の関係を明示する。
- 正本作成の前段として、(a) オーナー確認が必要な事項、(b) 正本作成前に必要な証拠、(c) 分離して扱う責務境界、(d) 提案する作成順を整理する。
- 「確認事項を記録・整理すること」と「規則正本を作成し承認すること」を区別する。本 PR では前者 (作成順 §12 の手順 1「確認事項の記録」) までとし、回答・規則作成・承認・再評価へ進まない。

## 2. Status

- 本 Creation Plan の Status は `Draft`。
- 本文書の追加だけでは、Review / Approval Rules の正本は作成されず、全候補共通の阻害 Fact も解決されない。
- 本文書は Review / Approval Rules を作成済み・承認済み・適用中として扱わない。

## 3. Position

- 上流入口: リポジトリ全体入口 [../README.md](../README.md)、Governance レイヤー入口 [README.md](README.md)。
- 本文書は Governance の横断共通レイヤーに属し、特定サービス配下の成果物ではない。
- `owner-decisions.md`・Travel Work Order 6 成果物・各サービス成果物は、上流入口 (Position) ではなく Sources (§6)・Relationship (§14)・Downstream Impact (§15) で扱う。

## 4. Scope

- Review / Approval Rules 正本を作成する **前に** オーナー確認が必要な事項の整理と記録 (`owner-decisions.md` の独立節への追加)。
- 正本作成前に Repository 内で確認すべき証拠 (Evidence) の種類の整理。
- 「改訂候補の採用・却下」「改訂タスク開始の承認」「内容レビュー」「Repository 反映」「上流 Open Issue 解決」「Governance / provenance / 正本参照の未解決事項解決」「placeholder / 実査待ちの調査」「改訂後 Alignment 再評価」「GitHub 操作 (commit / push / PR / merge)」といった責務の区別 (§7)。
- Review / Approval Rules 正本の想定境界 (§10 Proposed Document Boundary) と、提案する作成順 (§12 Ordered Creation Steps) の記録。

## 5. Out of Scope

- Review / Approval Rules の具体的な規則本文の作成。
- 承認者・レビュー担当者・反映担当者・解決担当者の特定、特定人物・部署・役職への責務割当。
- 改訂候補の採用・却下、Design System の改定要否、Design System 改訂タスクの開始、候補の優先順位付け。
- Open Issue の解決内容、ADR・命名規則・用語定義の正本内容、Alignment 完了条件の確定。
- Travel Work Order 6 の判断 (全 12 候補側面・総合判断) の変更・再評価。
- 国内レンタカー (`rental-car`)・インバウンドレンタカー (`inbound`) への適用可否の決定 (適用範囲自体がオーナー確認事項, §8)。
- 新しい Decision・UX Decision・正式 ID・Phase・Gate・Task 番号の採番・定義。

## 6. Current Repository Facts

Repository 内で直接確認できる Fact を引用する (解決策・推奨案は記入しない)。

- Governance README ([README.md](README.md) 「現在不足している成果物」) は、**レビュー・承認規則の正本が存在しない**と明記している。
- 同 README は、不足成果物の**正本の作成・承認フローも未決である**と明記している。
- [owner-decisions.md](owner-decisions.md) は「オーナー確認事項 (分類C) の一覧」であり、レビュー・承認規則の正本ではない。
- Travel の Work Order 6 ([../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)) は、Work Order 5 の全 12 候補側面すべてを `現時点では開始できない` と判断した。
- 全候補共通の阻害 Fact は、**実際の改訂タスクの承認・反映・解決主体が Repository 内で定義されていない**ことである (同文書 §8.3・§10・§11)。
- 候補固有の阻害 Fact として、上流 Open Issue・provenance 未確認・参照切れ・placeholder・実査待ちが存在する (同文書 §11)。
- Work Order 6 の実施は、候補採用・改定要否決定・改訂着手承認・Alignment 承認/完了を意味しない (同文書 §10・§13 相当の Does Not Decide)。

会話上の役割分担は Repository 内の正式な Governance Fact として転記しない。承認・反映・解決主体は「Repository 内で確認できない / 未定義」という Fact として扱う。

## 7. Responsibility Separation

Review / Approval Rules 正本が将来扱うべき責務を、少なくとも次のとおり区別する。これらを同一人物・同一部署が担うと仮定しない。「承認」「レビュー」「反映」「解決」「実行」「マージ」を同義語として扱わない。

- **改訂候補採用責務** — 改訂候補の採用・却下を決定する。
- **改訂着手承認責務** — 実際の Design System 改訂タスクの開始を承認する。
- **内容レビュー責務** — 成果物の内容をレビューする。
- **Repository 反映責務** — Repository へ変更を反映する。
- **上流 Open Issue 解決責務** — 上流の事業・業務・画面仕様に関する Open Issue を解決する。
- **Governance 未解決事項解決責務** — Governance・provenance・正本参照に関する未解決事項を解決する。
- **placeholder / 実査待ち調査責務** — placeholder・実査待ちを調査する。
- **Alignment 再評価責務** — 改訂後の Alignment を再評価する。
- **GitHub 操作責務** — GitHub 上で commit・push・PR・merge を実行する。

本文書はこれらの責務を特定の主体へ割り当てず、区別すべき責務の一覧として記録するにとどめる。GitHub 上の review / approval / merge という**操作**を、設計上の**承認**と自動的に同一視しない (両者の関係自体がオーナー確認事項, §8)。

## 8. Owner Confirmation Required

Review / Approval Rules 正本の作成前に、オーナー確認が必要な事項を整理する。恒久 ID・Decision ID は採番せず、説明用の項目名で記録する。回答・推奨案は推測して記入しない。**これらの確認事項の記録先は [owner-decisions.md](owner-decisions.md) の独立節**であり、本節はその整理・参照である (既存のオーナー確認事項の番号・内容・暫定運用案は変更しない)。

- **適用範囲** — Review / Approval Rules を国内宿泊 (`travel`) だけに適用するか、Repository 横断規則とするか。
- **候補採否の決定主体** — 改訂候補の採用・却下を誰が決定するか。
- **改訂着手の承認主体** — Design System 改訂タスクの開始を誰が承認するか。
- **責務の分割** — 内容レビュー・Repository 反映・未解決事項解決の責務をどう分けるか。
- **上流 Open Issue の解決単位** — Service Design / Screen Requirements の Open Issue について、解決主体をどの単位で定義するか。
- **Governance 正本の担当** — Governance・ADR・provenance・参照切れについて、正本作成または有効性確認を誰が担うか。
- **placeholder / 実査待ちの確認主体** — placeholder・実査待ちの調査結果を誰が確認するか。
- **GitHub 操作と設計承認の関係** — GitHub PR の approval または merge を設計承認として扱うか、別の明示的承認記録を必要とするか。
- **承認結果の記録先** — 承認結果をどの Repository 成果物へ、どの状態表現で記録するか。
- **再評価の条件** — 阻害 Fact 解消後に Work Order 6 相当の再評価をどの条件で行うか。
- **Alignment 完了条件の所在** — Alignment 完了条件をこの規則で扱うか、別の Governance 成果物で扱うか。

**回答取得状況 (2026-07-17)**: 上記 11 項目すべてへオーナーの明示的回答を **2026-07-17** に取得し、[owner-decisions.md](owner-decisions.md) §4 の各項目「オーナー回答」列へ記録した (Ordered Creation Steps §12 手順 1 の実行)。回答は本 Repository 内の追跡可能な直接証拠として存在する (手順 2 の確認範囲)。回答に残る条件・未定は同 §4「残る Open Issue」列へ分離した (適用範囲＝Repository 横断、主体は Web部の責任者・Web部責任者/チーフデザイナー・Web部レビュー担当者・作業担当者を影響度等に応じて割当、GitHub の merge は設計承認と同一視せず別途明示記録が必要、承認結果は owner-decisions.md にログ記録、再評価は暫定的に全候補一括、Alignment 完了条件は将来の正本内に置く)。本記録は Review / Approval Rules 正本の作成・承認・適用を意味しない (正本は未作成)。

## 9. Evidence Required Before Rule Creation

Review / Approval Rules 正本を作成する前に、Repository 内の直接証拠として確認が必要な事項を整理する (本 PR では証拠の確認自体は行わない)。

- §8 の各オーナー確認事項に対する **明示的な回答が Repository 内成果物に記録されていること**。
- その回答が、会話・口頭・外部連絡ではなく、Repository 内で追跡可能な直接証拠として存在すること。
- 回答が既存の Governance 記述・各レイヤー境界と矛盾しないこと。
- 承認・反映・解決主体が「未定義」から「Repository 内で定義済み」へ変わったことが確認できること。
- 上記が満たされない項目は、未解決 (未定義) の Fact として保持し、正本作成の肯定的根拠に使用しないこと。

## 10. Proposed Document Boundary

将来作成する Review / Approval Rules 正本が扱う想定範囲と、扱わない想定範囲を提案として記録する (正本の内容は本文書で確定しない)。

- **扱う想定**: 改訂候補の採否・改訂着手承認・内容レビュー・Repository 反映・未解決事項解決・再評価といった責務の**規則**と、その承認記録の所在・状態表現。
- **扱わない想定**: 個別の改訂内容、Design System の token / Component / version、特定候補の採否結果、上流業務仕様そのもの、実装仕様。
- **他 Governance 成果物との境界**: 命名規則・ADR・用語定義・Repository principles の正本は別成果物であり、本規則で兼ねない。Alignment 完了条件をこの規則で扱うかは未決 (§8)。
- 本 Proposed Document Boundary は提案であり、正式な Scope 確定・Decision ではない。

## 11. Entry Conditions

Review / Approval Rules 正本の Draft 作成 (§12 手順 3) に着手してよいかの前提を条件として記録し、2026-07-17 時点で項目ごとに直接証拠で評価する。本 PR は正本作成に進まない (評価の記録のみ)。

| Entry Condition | 直接証拠 | 充足評価 (2026-07-17) |
| --- | --- | --- |
| 本 Creation Plan が Draft として Repository に存在する | 本文書 (PR #61 マージ済み) | 満たす |
| §8 の確認事項が [owner-decisions.md](owner-decisions.md) の独立節に記録されている | owner-decisions.md §4 | 満たす |
| §8 の各確認事項へオーナーの明示的回答が Repository 内直接証拠として記録されている | owner-decisions.md §4「オーナー回答」列 (2026-07-17 取得) | 満たす (11 項目すべてに明示回答を記録) |
| 回答が既存 Governance 記述・各レイヤー境界と矛盾しない | 横断規則化は Governance 横断レイヤーと整合、承認記録の Wiki 非正本方針は root README §3 と整合 | 満たす (矛盾なし) |
| 承認・反映・解決主体が「未定義」から「Repository 内で定義済み」へ変わった | owner-decisions.md §4 | 一部満たす (候補採否・改訂着手承認・レビュー・反映・GitHub 操作・Governance 正本担当の主体は定義済み。上流 Open Issue の具体的解決単位、placeholder/実査待ちの個別確認主体、再評価の②③トリガー扱いは「残る Open Issue」として未定) |

**評価の結論**: §8 への明示的回答が Repository 内直接証拠として記録された点で、正本作成の主要な前提 (回答の取得・記録) は満たされた。ただし上表の「残る Open Issue」(上流 Open Issue の具体的単位・placeholder/実査待ちの個別確認主体・再評価の②③トリガー・Alignment 完了条件の内容) は未解決のまま残る。これらは正本作成時に未解決事項として持ち越し、解決済みの肯定的根拠に使用しない (§9)。正本 Draft 作成の実際の着手は本 PR では行わず、別タスクで扱う。

## 12. Ordered Creation Steps

実行順の**提案**として記録する。正式 Phase や Gate へ昇格させない。番号は読み順の目安であり、確定した運用フロー・Gate ではない。

1. [owner-decisions.md](owner-decisions.md) に記録した確認事項 (§8) への明示的回答。
2. 回答を Repository 内の直接証拠として確認。
3. Review / Approval Rules 正本の Draft 作成。
4. Draft と既存 Governance・各レイヤー境界の整合確認。
5. オーナーによる明示的な承認。
6. 正本の Status と適用範囲を承認結果どおり反映。
7. 解決された阻害 Fact だけを対象に、別タスクで改訂着手可否を再評価。

**進捗 (2026-07-17)**: 手順 1 (確認事項への明示的回答) を実施し [owner-decisions.md](owner-decisions.md) §4 へ記録、手順 2 (回答を Repository 内直接証拠として確認) を実施した。**Task 009-3 で手順 3 (Review / Approval Rules 正本候補 Draft の作成, [review-approval-rules.md](review-approval-rules.md)) と手順 4 (Draft と既存 Governance・各レイヤー境界の整合確認, 同文書 §17 に結果を記録) を実施した。** 手順 5 以降 (オーナーによる明示的承認・Status/適用範囲の反映・適用開始・改訂着手可否の再評価) は本 PR では実施しない。正本候補 Draft は未承認・未適用 (Status = Draft) であり、本 PR のマージだけでは Status を Draft から変更せず、Work Order 6 の共通阻害 Fact を全面解消しない。

## 13. Completion Conditions

本 Creation Plan の目的が達成されたと言える条件を記録する (達成の判定・確定は本文書では行わない)。

- §8 の全確認事項へオーナーの明示的回答が Repository 内に記録され、§9 の証拠要件が満たされていること。**(2026-07-17 充足: owner-decisions.md §4)**
- Review / Approval Rules 正本が Draft として作成され、既存 Governance・各レイヤー境界と整合が確認されていること。**(Task 009-3 で充足: [review-approval-rules.md](review-approval-rules.md) 作成・同 §17 に整合確認結果)**
- 正本がオーナーの明示的承認を経て、Status と適用範囲が承認結果どおり反映されていること。**(未達: 明示的承認・Status/適用範囲反映は未実施)**
- 上記により、Work Order 6 で確認された共通阻害 Fact (承認・反映・解決主体の未定義) が、当該範囲について解消されたと確認できること。**(未達: 規則が未承認・未適用のため)**
- これらの Completion Conditions は本文書では**未達**である。正本候補 Draft は作成・整合確認済みだが、オーナーの明示的承認・Status/適用範囲の反映が未実施であり、Review / Approval Rules は未承認・未適用である。

## 14. Relationship to Travel Work Order 6

- Travel Work Order 6 ([../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)) は、全 12 候補側面を `現時点では開始できない` と判断し、全候補共通の阻害 Fact として「承認・反映・解決主体が Repository 内で未定義」を記録した (§8.3・§10・§11)。
- 本 Creation Plan は、その共通阻害 Fact のうち **Governance 側の欠落 (レビュー・承認規則の正本と承認主体の不在)** を解消するための計画であり、Work Order 6 の判断そのものを変更・再評価しない。
- 候補固有の阻害 Fact (上流 Open Issue・provenance 未確認・参照切れ・placeholder・実査待ち) は本計画の対象外であり、別の解決主体・別タスクで扱う (責務区別は §7)。
- Work Order 6 成果物は評価 snapshot の記録として保持し、本タスクで書き換えない。

## 15. Downstream Impact

- 本 Creation Plan は、将来の Review / Approval Rules 正本作成 (別タスク) の入力となる。
- 各サービスの Design System 改訂タスクは、承認・反映・解決主体が Repository 内で定義されるまで開始できない (Travel Work Order 6 の総合判断)。本計画はその前提整理であり、改訂着手を承認しない。
- 本計画の追加は、下流の Design System・token・Component・version に変更を与えない。

## 16. Open Issues

- §8 の全確認事項はオーナー回答を取得・記録済み ([owner-decisions.md](owner-decisions.md) §4、2026-07-17)。以下は回答に残る、または本計画で解決しない Open Issue である。
- 上流 Open Issue の具体的な解決単位 (全体共通／成果物別／論点別のいずれを採るか) は案件ごと・未定。
- placeholder / 実査待ちの個別項目の確認主体は、確認ルール制定まで未定。
- 改訂着手可否の再評価で、上流 Open Issue・provenance 未確認を必須トリガーとするかは未確定。
- Alignment 完了条件の内容自体は未定義 (置き場所は将来の Review / Approval Rules 正本内と決定済み)。
- Review / Approval Rules 正本候補 Draft は Task 009-3 で作成された ([review-approval-rules.md](review-approval-rules.md)) が、**未承認・未適用** (Status = Draft) である。加えて、影響度・高／低の判定基準・判定主体が未定義であり、同 Draft の承認前に解決が必要な Open Issue として残る (同文書 §8・§21)。Draft の作成・本 PR のマージは、規則の承認・適用や Work Order 6 共通阻害 Fact の全面解消を意味しない。
- 候補固有の阻害 Fact (上流 Open Issue の内容・provenance 未確認・参照切れ・placeholder/実査待ちの実値) は未解決 (本計画の対象外)。
- 命名規則・ADR・用語定義・Repository principles の正本不在 (Governance README) は本計画では解決しない。

## 17. Does Not Decide

本文書は以下を決定しない。

- 実際の承認者・レビュー担当者・反映担当者・解決担当者、および特定人物・部署・役職への責務割当。
- Review / Approval Rules の具体的な規則本文。
- 改訂候補の採用・却下、Design System の改定要否、Design System 改訂タスクの開始、候補の優先順位。
- Open Issue の解決内容、ADR・命名規則・用語定義の正本内容、Alignment 完了条件。
- Travel Work Order 6 の再評価。
- 国内レンタカー・インバウンドレンタカーへの適用。
- 新しい Decision・UX Decision・正式 ID・Phase・Gate・Task 番号。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-17 | Create Governance Review and Approval Rules Creation Plan (Draft)。Travel Work Order 6 の共通阻害 Fact「承認・反映・解決主体が Repository 内で未定義」に対し、Review / Approval Rules 正本作成前に必要なオーナー確認事項・証拠・責務境界・作成順を整理。手順 1「確認事項の記録」まで (回答・規則作成・承認・再評価は未実施)。規則正本は未作成、主体は未割当 | Draft |
| 2026-07-17 | §8 全 11 項目へのオーナー明示的回答を 2026-07-17 に取得し owner-decisions.md §4 へ記録 (Ordered Creation Steps 手順 1)、手順 2 の直接証拠確認を本 PR 範囲で実施。§8 に回答取得状況、§11 Entry Conditions に項目別の充足評価、§12 に進捗、§16 に残る Open Issue を反映。Review / Approval Rules 正本は未作成・未承認、Work Order 6 の再評価・Design System 改定は未実施。手順 3 以降へ進まない | Draft |
| 2026-07-17 | Task 009-3: Review / Approval Rules 正本候補 Draft ([review-approval-rules.md](review-approval-rules.md)) を作成 (Ordered Creation Steps 手順 3)、既存 Governance・各レイヤー境界との整合確認を実施 (手順 4、結果は Draft §17)。§12 進捗・§13 Completion Conditions・§16 Open Issues を更新。手順 5 (オーナー明示的承認) は未実施、Completion Conditions 未達、規則は未承認・未適用、Work Order 6 は未再評価、Design System 改定は未着手 | Draft |
