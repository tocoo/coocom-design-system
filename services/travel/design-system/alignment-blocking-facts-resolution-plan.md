# Travel Alignment Blocking Facts Resolution Plan

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Alignment Assessment において、Task 009-6 の Work Order 6 再評価 ([alignment-amendment-readiness-reassessment.md](alignment-amendment-readiness-reassessment.md)) が「現時点では開始できない」と記録した全 12 候補側面の**候補固有阻害 Fact**を、推測で解消したり Design System の改定へ進めたりせず、後続タスクとして安全に解決するための計画。全 12 候補と残る阻害 Fact の対応関係・必要な直接証拠・既存規則 ([../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md)) 上の解決経路・判断が必要な事項・依存関係を整理する。
- Position in Repository: `services/travel/design-system/alignment-blocking-facts-resolution-plan.md` — Design System レイヤー (travel サービス配下)。上流成果物は レイヤー入口 [README.md](README.md)・Alignment 計画 [alignment-plan.md](alignment-plan.md)・Baseline 評価 [baseline-assessment.md](baseline-assessment.md)・Service Design 横断整合性評価 [service-design-alignment-assessment.md](service-design-alignment-assessment.md)・Screen Requirements 個別整合性評価 [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md)・Observation 横断集約 [alignment-observations-aggregation.md](alignment-observations-aggregation.md)・改訂候補と未解決事項の分離 [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md)・改訂着手可否評価 [alignment-amendment-readiness-assessment.md](alignment-amendment-readiness-assessment.md)・その再評価 [alignment-amendment-readiness-reassessment.md](alignment-amendment-readiness-reassessment.md)。Governance の Review / Approval Rules・owner-decisions.md との関係は本文 Sources (§5 相当) と各節に記載し、Position の上流成果物へ混在させない。下流成果物 (Assets / Implementation) との関係は Downstream Impact (§11) を参照。

本文書は**解決計画**であり、次のいずれでもない: Task 009-6 再評価の上書き、改訂候補の採否判断、改定・非改定・継続保留の設計判断、改訂着手承認、Design System 改定仕様、上流 Open Issue の解決記録、調査結果の記録、優先順位・severity の決定。ファイル名 `alignment-blocking-facts-resolution-plan.md` は記述的な暫定識別子であり、新しい正式 ID・分類体系・Phase・Gate・Status 体系を確定しない。Task 009-6 の T/C/X ラベル・候補見出しは説明用の参照であり、正式 ID へ昇格させない。SCR ID は Screen Matrix 上の画面候補 ID であり、Screen Requirement 文書 ID・実装画面 ID・URL・route と同一視しない。Fact / Decision / Hypothesis / Open Issue を区別し、新しい Design Decision・UX Decision を追加しない。Task 009-6 の再評価 snapshot (`e0880d8`) と本計画の snapshot (§1) を混在させない。

## 1. Plan Snapshot

- Plan target: 作業開始時点の最新 `main`。
- Plan snapshot (main commit SHA): `293357db05e8861d10fa53cdb410aaa46d104c88` (PR #71 merge、Task 009-6 の状態同期を含む現 main HEAD)。
- 作成日: 2026-07-21。
- **snapshot の分離**: Task 009-6 の再評価 ([alignment-amendment-readiness-reassessment.md](alignment-amendment-readiness-reassessment.md)) は snapshot `e0880d8` の記録、元 Work Order 6 ([alignment-amendment-readiness-assessment.md](alignment-amendment-readiness-assessment.md)) は snapshot `eb0b891` の記録である。本計画はこれらを**変更せず**、当時の記録として引用する。本計画は snapshot `293357d` の記録であり、各 snapshot を混在させない。
- 本計画は Repository 内文書の静的な整理であり、実装検証・調査の実施・Design System の改定ではない。作成中に main の更新はない。

### 入力文書 (blob SHA @ `293357d`)

| 入力 | ファイル | 役割 | blob SHA |
| --- | --- | --- | --- |
| 主入力 (Task 009-6) | [alignment-amendment-readiness-reassessment.md](alignment-amendment-readiness-reassessment.md) | 全 12 候補の Current Judgment・残る阻害 Fact (§9・§12・§16) | `2ea43285dd762da2ce57bd69b82ab0f7459419b0` |
| 正本入力 (Work Order 5) | [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md) | 候補側面 (§13)・未解決事項 (§14)・相互リンク (§16) | `bbe0faf8e3b3d6d2318bf41fbf19a3002e8de188` |
| 集約 (Work Order 4) | [alignment-observations-aggregation.md](alignment-observations-aggregation.md) | 集約 Topic・Unresolved Dependencies | `89ef99de6da00b226bb12445d7dfe253e49a2e84` |
| 証拠制約 (Work Order 1) | [baseline-assessment.md](baseline-assessment.md) | token/placeholder/provenance/参照切れ | `89ea9d17257cf2e5b162dc702944b21033ef71e2` |
| 追跡確認 (Work Order 2) | [service-design-alignment-assessment.md](service-design-alignment-assessment.md) | SD 横断責務の元 Observation | `528b3cccc0bb0c91ec3a1a8a233f8ff28152475b` |
| 追跡確認 (Work Order 3) | [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) | 7 SCR の元 Observation | `521d3b54d9cba455c2b07db4edfb059865447a28` |
| 方法・境界 | [alignment-plan.md](alignment-plan.md) | 評価方法・分類・順序・§10 Work Order | `fcf9ec146c6bbf6b70c20d07520012df96fd1cf9` |
| 入口 (DS レイヤー) | [README.md](README.md) | Reference Order・現在状態 | `79df343e0aab8558064e2dd450d459058c368009` |
| Governance 規則 | [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) | 責務・経路 (§7〜§19) | `e8a27283825db87e0201d56ed036943b8b6bb72a` |
| Governance 承認/適用記録 | [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) | §4 回答・§5 承認ログ・§6 適用開始記録 | `7a35addad17d480c2ab7866ef45468dc60a7ab31` |
| Governance 計画 | [../../../governance/review-approval-rules-creation-plan.md](../../../governance/review-approval-rules-creation-plan.md) | 手順の完了状況 | `aba117496baffe7e34afcac8c5975b53fea37293` |
| Governance 入口 | [../../../governance/README.md](../../../governance/README.md) | 不足成果物・正本整備状況 | `e13acbfc9a9076d6d92f386aa0ee175eee9245fb` |
| サービス入口 | [../README.md](../README.md) | サービス状態 | `cccf66272a196aa7da0fec6b953a08be16fb21ce` |
| リポジトリ入口 | [../../../README.md](../../../README.md) | 全体状態 | `fef100e60a2454763e35fa264ce2b4249b7b024e` |

### 変更しない成果物

- Task 009-6 の再評価 ([alignment-amendment-readiness-reassessment.md](alignment-amendment-readiness-reassessment.md))・元 Work Order 6 ([alignment-amendment-readiness-assessment.md](alignment-amendment-readiness-assessment.md))・既存 Design System 4 成果物 ([design.md](design.md) / [semantic.travel.json](semantic.travel.json) / [primitive.travel.json](primitive.travel.json) / [components.md](components.md))・Service Design・Screen Requirements・Governance 規則・owner-decisions.md。

## 2. Purpose

- Task 009-6 の再評価が全 12 候補側面を「現時点では開始できない」とした際に保持した**候補固有阻害 Fact** (再評価 §9・§12) と、規則で定義された範囲を超えて残る事項 (再評価 §8.3 残余・§16) を、後続タスクとして安全に解決するための整理を行う。
- 各阻害 Fact の直接証拠・正本所在・不足証拠、既存 Review / Approval Rules 上の解決経路、解決前に必要な Web部責任者の判断、後続タスク間の依存関係、再評価へ戻せる条件を記録する。
- 「整理・計画すること」と「解決すること・採否や改定を判断すること」を区別する。後者は本文書では行わない (§3・§12)。

## 3. Scope

- Work Order 5・Task 009-6 の全 12 候補側面 (§6)。
- Task 009-6 §12・§16 に残った阻害 Fact。
- 各阻害 Fact の直接証拠・正本所在・不足証拠 (§5・§6)。
- Review / Approval Rules 上の解決経路 (§6・§7)。
- 解決前に必要な Web部責任者の判断 (§8)。
- 後続タスク間の依存関係 (§7)。
- 再評価へ戻せる条件 (§6 各候補 Reassessment Condition・§7)。

## 4. Out of Scope

- 候補採否、改定・非改定・継続保留の決定、改訂着手承認。
- Design System 本体の変更、上流 Service Design・Screen Requirements の変更。
- Governance 正本の新規作成・改定。
- placeholder 値の確定、実査の実施、provenance・参照切れの推測解消。
- 優先順位・重要度・severity・工数・期限の決定。
- SCR-006〜SCR-012 の作成・評価。
- UI・画面・URL・route・API・DB・Implementation 仕様。
- 数値スコア・適合率・pass/fail・合否点の導入、新しい正式 ID・分類体系・Phase・Gate・Status 体系の作成。

## 5. Blocking Fact Classification

Task 009-6 で確認された阻害 Fact を、少なくとも次の種別へ分ける。これは本計画内の**説明用の整理**であり、正式な分類体系・恒久 ID へ昇格させない。種別 6〜8 は複数候補に横断して現れるが、候補別の影響を消さない (§6)。種別 6 は「主体が未定である」という Fact であって、主体が定義済みであることを意味しない。

1. **上流 Service Design / Screen Requirements の Open Issue** — 業務仕様・画面仕様・設計判断が上流で未確定 (例: Navigation 分類・状態モデル業務定義・IA Object 業務モデル・入力/表示仕様・可逆/回復フロー・支援範囲・タイポグラフィ具体規格・アクセシビリティ適用規格)。
2. **provenance 未確認** — GOV-0002・TVL 群 (TVL-0007 等) の ADR 正本が Repository 内に不在で、Decision ID の裏付けを直接確認できない。
3. **参照切れ・正本不在** — `brand-content.md`・`governance/naming-rules.md`・ADR 正本が Repository 内に不在。
4. **placeholder token** — `radius.card`・`motion.*`・`shadow.*` 等の placeholder token (計 10) が未確定 (Work Order 1・4 §17.2)。
5. **follow-up / 実査待ち** — ボタン状態 follow-up #4・Input 状態 follow-up #2・Card 実 px/8 スロット・星実寸・「円」weight・画像 fallback が未取得。
6. **placeholder / 実査待ちの個別確認主体未定** — 確認方法を決める主体は Web部責任者と定義済み (Review / Approval Rules §14) だが、**個別項目の確認主体は確認ルール制定まで未定** (§14・§21③)。定義済みと誤記しない。
7. **上流 Open Issue の具体的解決単位未定** — 全体共通／成果物別／論点別のどの単位で扱うかは案件ごと・未定 (Review / Approval Rules §12・§21②)。
8. **再評価トリガー未確定** — 改訂着手可否の再評価で、上流 Open Issue・provenance 未確認を必須トリガーとするかは未確定 (Review / Approval Rules §18・§21④)。

種別 1〜5 は候補固有の阻害 Fact、種別 6〜8 は規則の承認・適用開始だけでは解決しない横断的な残余 (Task 009-6 §8.3・§10) である。種別 1〜5 と 6〜8 のいずれも、規則上の責任経路が存在すること (§7) と論点の内容が解決済みであることは別である (§12)。

## 6. Candidate-by-candidate Correspondence

全 12 候補を漏れなく記録する。各 Current Judgment は Task 009-6 の記録 (すべて `現時点では開始できない`)。`Existing Rule / Responsibility Route` は Review / Approval Rules (以下「規則」) の該当節。`現時点では開始できない` を却下・不要・継続保留へ変換しない。上流 Open Issue と Design System 側の不足を混同しない。規則上の責任経路の存在と論点の内容の解決を区別する。未着手 Component を必要 Component・改訂候補へ変換しない。

### 6.1 NAV 分類と DS Navigation component の対応の明文化

- **Candidate Aspect**: 上流 Navigation Types (NAV-001〜006) の責務と DS 側 Navigation component の対応関係の明文化余地 (Task 009-6 §9.1、WO5 C-06/X-01)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: Global Navigation 対象領域・History and Recovery (NAV-005) 保持方式が上流 NAV/SCR Open Issue として未解決。加えて種別 7 (解決単位未定)。
- **Blocking Fact Type**: 1 (上流 Open Issue)。横断: 7・8。
- **Direct Source**: navigation.md §10 Open Issue、各 SCR §16 Open Issue (WO5 §14「Navigation 分類・Global Nav・History and Recovery の上流未定義」)。
- **Missing Evidence or Decision**: Global Nav 対象領域・History and Recovery 保持方式の上流での確定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決・解決確認 = 規則 §12 (影響度別: 高＝Web部責任者・チーフデザイナー／低＝Web部レビュー担当者)。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、当該解決タスクの影響度判定 (§8)。
- **Eligible Follow-up Work**: Service Design / Screen Requirements 側での明示的判断・更新 (navigation.md §10・各 SCR §16 の Open Issue 解決)。
- **Reassessment Condition**: 当該上流 Open Issue が解決され、規則 §18 に基づき Web部責任者が再評価をトリガーしたとき (上流 Open Issue を必須トリガーとするかは §21④ 未確定)。
- **Does Not Decide**: Navigation Types と component の対応内容・保持方式・改定要否。
- **Does Not Authorize**: NAV 分類対応の明文化・component 追加。

### 6.2 Navigation と CTA の責務分離を述べる DS 本文規則の明文化

- **Candidate Aspect**: UXDR-TRAVEL-003 が求める Navigation/CTA 責務分離を DS 本文規則として明文化する余地 (Task 009-6 §9.2、WO5 X-01)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: Button variant 語彙 GOV-0002 の provenance 未確認。
- **Blocking Fact Type**: 2 (provenance 未確認)。横断: 8。
- **Direct Source**: WO5 §14「Decision ID の provenance 未確認 (GOV-0002・TVL 群)」、Baseline (Work Order 1) の provenance 未確認記録。GOV-0002 の ADR 正本は Repository 内に不在。
- **Missing Evidence or Decision**: GOV-0002 を裏付ける ADR 正本の作成または有効性確認 (owner-decisions.md は確認事項一覧であり ADR ではない)。
- **Existing Rule / Responsibility Route**: Governance・ADR・provenance の正本作成/有効性確認 = 規則 §13 (影響度別)。
- **Prerequisite Owner Judgment**: 当該 provenance 確認タスクの影響度判定 (§8)、provenance 未確認を再評価の必須トリガーとするかの扱い (§21④)。
- **Eligible Follow-up Work**: Governance / ADR / provenance の正本確認 (GOV-0002 の ADR 正本作成または有効性確認)。provenance 未確認を肯定的根拠に使用しない。
- **Reassessment Condition**: GOV-0002 の provenance が Repository 内で確認可能になり、規則 §18 に基づき再評価がトリガーされたとき (provenance を必須トリガーとするかは §21④ 未確定)。
- **Does Not Decide**: 責務分離規則の内容・改定要否・GOV-0002 の再認定。
- **Does Not Authorize**: 責務分離規則の追加。

### 6.3 上流状態モデルと DS 状態表現の対応の明文化

- **Candidate Aspect**: Navigation State Model・CTA State Model・Status and Uncertainty Model と DS 状態表現の対応関係の明文化余地 (Task 009-6 §9.3、WO5 X-03/T-02/C-08)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: 状態の業務定義 (Pending Confirmation・空結果/在庫切れ挙動・予約状態) が上流 Open Issue。ボタン状態 follow-up #4 の実査待ち、motion の placeholder。個別確認主体は未定。〔Task 009-11 で精密化 (§8D)〕この一括表現を次の粒度へ改める — (i) Pending Confirmation は cta-principles §6 に既定義 (既存原則で充足・新規業務定義ではない)、(ii) 空結果・在庫切れは発生条件が実行時・実装で Repository 対象外、状態伝達は既存原則 (CTP-006/CTP-007・SDP-005/SDP-006・Status Model の Unavailable/Unknown) で充足、ただし画面別の具体的扱いは SCR-004 §16 の Open Issue として残り、特定状態への割当は直接証拠がなく判定保留、(iii) 予約業務状態は現行 3 State Model の責務外かつ Booking 系 Screen Requirements (SCR-006〜012 未作成)・業務/製品仕様側で本工程の対象外。ボタン状態 follow-up #4・motion placeholder・確認方法・個別確認主体は未解決/未定のまま保持し、DS 側状態表現との対応 (X-03) は T2 再分類だけでは自動解決しない。
- **Blocking Fact Type**: 1・4・5・6。横断: 7・8。
- **Direct Source**: WO5 §14「上流状態モデルの業務定義」「placeholder / 実査待ちの未取得」、WO4 X-03/T-02、owner-decisions.md §3 follow-up #4。
- **Missing Evidence or Decision**: 上流での状態業務定義、follow-up #4 の実査結果、motion placeholder の確定、確認方法・個別確認主体の決定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12 (影響度別)。placeholder / 実査待ちの確認方法決定 = 規則 §14 (Web部責任者)、個別確認主体は未定 (§14・§21③)。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、placeholder / 実査待ちの確認方法と個別確認主体 (§14)、各タスクの影響度判定 (§8)。
- **Eligible Follow-up Work**: SD/SR 側での状態業務定義の判断・更新、Web部責任者による placeholder / 実査待ち確認方法の決定、決定後の実査。
- **Reassessment Condition**: 状態業務定義が解決され、placeholder/実査待ちの確認方法・個別確認主体が定義され結果が記録され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 状態の業務定義・UI 表現・token 値。Navigation State Model・CTA State Model・Component state を同一視しない。SCR-014 に `Error / Interrupted` を追加しない。
- **Does Not Authorize**: 状態の具体一覧・状態表示 component の追加。

### 6.4 Recovery Action 責務と DS 側の対応の明文化

- **Candidate Aspect**: 中断・エラーからの回復行動 (CTA-TYPE-004) の責務と DS 側の対応関係の明文化余地 (Task 009-6 §9.4、WO5 C-08)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: 問い合わせ手段・処理フロー・サポート対象範囲が SCR-013 §16 の上流 Open Issue。ボタン状態 follow-up #4 の実査待ち。個別確認主体は未定。
- **Blocking Fact Type**: 1・5・6。横断: 7・8。
- **Direct Source**: WO5 §14「可逆/不可逆・回復フローの上流未定義」、SCR-013 §16 Open Issue、owner-decisions.md §3 follow-up #4。
- **Missing Evidence or Decision**: サポート対象範囲・FAQ 構成・問い合わせ手段の上流確定、follow-up #4 の実査結果、確認方法・個別確認主体の決定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。placeholder / 実査待ち確認方法決定 = 規則 §14 (個別確認主体は未定)。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、placeholder / 実査待ちの確認方法・個別確認主体 (§14)、影響度判定 (§8)。
- **Eligible Follow-up Work**: SCR-013 側での回復フロー・サポート範囲の判断・更新、確認方法決定後の実査。
- **Reassessment Condition**: 回復フロー Open Issue が解決され、follow-up #4 の確認方法・主体が定義され結果が記録され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: Recovery Action の component/規則。未着手 component を必要 component へ変換しない。
- **Does Not Authorize**: Recovery Action 用 component/規則の追加。

### 6.5 IA Object・Content Category の表現責務と DS 表現語彙の対応の明文化

- **Candidate Aspect**: 宿泊領域の IA Object と Content Category を UI として表現する責務と DS 表現語彙の対応関係の明文化余地 (Task 009-6 §9.5、WO5 C-10/X-06)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: IA Object の業務モデル (内容・関係・業務仕様) が information-architecture.md §11 Open Issue、SCR-005/SCR-006 境界も未定義。Content 文言正本 `brand-content.md` の参照切れ。〔Task 009-12 で精密化 (§8E)〕この一括表現を次の粒度へ改める — (i) 12 IA Object の定義・責務・概念関係・Relationship Matrix は information-architecture.md §5〜§7 に既に Draft で存在し (既存 Draft で明示)、「何も定義されていない」ではない、(ii) 業務上の正式関係 (Room⇔Stay Plan⇔Availability⇔Price 等)・Destination 階層・Policy 個別規則・Review 提供元/信頼性・User/会員区別・Booking 業務構造/状態は事業・商品・業務仕様側の判断であり IA §11 Open Issue かつ本レイヤーで推測しない、(iii) 運用データ・API・DB・外部システム対応は information-architecture.md §8/§9 により Repository 全体の対象外、(iv) 12 Object の正式承認・正式用語・IA Object ID・`brand-content.md` 正本は Governance/命名規則側 (未整備)、(v) IA Object・Content Category と DS 表現語彙の対応 (C-10/X-06) は DS 内部整合課題で T3 再分類だけでは自動解決しない、(vi) SCR-005/SCR-006 境界は Screen Requirements 課題で未確定 (SCR-006〜012 未作成)。詳細は §8E。
- **Blocking Fact Type**: 1・3。横断: 7・8。
- **Direct Source**: WO5 §14「IA Object の業務モデル」「文言・命名の正本不在」、information-architecture.md §11 Open Issue。
- **Missing Evidence or Decision**: IA Object 業務モデルの上流確定、`brand-content.md` の正本作成または有効性確認 (SCR-006〜012 は対象外領域)。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。参照切れ・正本作成/有効性確認 = 規則 §13 (影響度別)。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、参照切れ正本の扱いの影響度判定 (§8)。
- **Eligible Follow-up Work**: IA 側での業務モデルの判断・更新、Governance / 正本 (`brand-content.md`) の作成または有効性確認。参照切れ文書の想定内容を根拠にしない。
- **Reassessment Condition**: IA §11 Open Issue が解決され、`brand-content.md` の正本が Repository 内で確認可能になり、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 専用 component の要否・業務モデル・文言。IA Object を Component、Content Category を掲載枠と同一視しない。
- **Does Not Authorize**: 専用表現語彙・component の追加。

### 6.6 可逆/不可逆区別責務と DS 側規則の対応の明文化

- **Candidate Aspect**: 可逆操作・回復可能性 (SDP-006)・不可逆前の可逆 (CTA-006) を UI として区別する責務と DS 側規則の対応関係の明文化余地 (Task 009-6 §9.6、WO5 C-07)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: 保存期間・Undo・エラー処理が上流 Does Not Decide。Input 状態一式 follow-up #2 の実査待ち。drawer 統一 TVL-0007 の provenance 未確認。個別確認主体は未定。
- **Blocking Fact Type**: 1・2・5・6。横断: 7・8。
- **Direct Source**: WO5 §14「可逆/不可逆・回復フローの上流未定義」「Decision ID の provenance 未確認」「placeholder / 実査待ちの未取得」、owner-decisions.md §3 follow-up #2。
- **Missing Evidence or Decision**: 保存期間・Undo・エラー処理の上流確定、follow-up #2 の実査結果、TVL-0007 の ADR 正本、確認方法・個別確認主体の決定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。provenance 確認 = 規則 §13。placeholder / 実査待ち確認方法決定 = 規則 §14 (個別確認主体は未定)。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、provenance を再評価の必須トリガーとするか (§21④)、placeholder / 実査待ちの確認方法・個別確認主体 (§14)、影響度判定 (§8)。
- **Eligible Follow-up Work**: SD 側での可逆/回復仕様の判断、TVL-0007 の provenance 確認、follow-up #2 の実査。provenance 未確認を肯定的根拠に使用しない。
- **Reassessment Condition**: 上流仕様が解決され、TVL-0007 provenance と follow-up #2 が確認され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 可逆/不可逆規則・エラー処理仕様。
- **Does Not Authorize**: 可逆/不可逆規則の追加。

### 6.7 アクセシビリティ適用規格・達成レベルと focus/非依存表現の対応の明文化

- **Candidate Aspect**: アクセシビリティの適用規格・達成レベルと DS の focus/非依存表現の対応関係の明文化余地 (Task 009-6 §9.7、WO5 T-01/X-04)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: 適用規格・達成レベルの内容が上流未定義 (design.md §2 は「WCAG 2.2 AA を最低ライン」と記述するが適用規格・達成レベルは未確定)。画像欠落 fallback (SCR-014) の実査待ち。個別確認主体は未定。JSON `$note` がコントラスト未達可能性を自認。
- **Blocking Fact Type**: 1・5・6。横断: 7・8。
- **Direct Source**: WO5 §14「アクセシビリティ適用規格・達成レベルの未定義」、design.md §2、WO4 T-01/X-04。
- **Missing Evidence or Decision**: 適用規格・達成レベルの上流/Governance 定義、画像 fallback の実査結果、確認方法・個別確認主体の決定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。適用規格・達成レベルの正本が Governance に関わる場合は §13。placeholder / 実査待ち確認方法決定 = 規則 §14。
- **Prerequisite Owner Judgment**: 適用規格・達成レベルをどのレイヤー (上流/Governance) で確定するかを含む解決単位 (§21②)、画像 fallback の確認方法・個別確認主体 (§14)、影響度判定 (§8)。
- **Eligible Follow-up Work**: 上流/Governance での適用規格・達成レベルの判断・記録、画像 fallback の実査。主体の定義は内容の確定を意味しない。
- **Reassessment Condition**: 適用規格・達成レベルの内容が定義され、画像 fallback が確認され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 適用規格・達成レベル・実装方式・画像仕様・達成基準値。
- **Does Not Authorize**: 達成基準値・実装方式の確定。

### 6.8 情報確認と選択の区別・CTA 主要行動責務と DS Button 定義の対応の明文化

- **Candidate Aspect**: 情報確認と選択の区別 (CTA-004)・主要行動の優先関係 (CTA-001) の責務と DS Button 定義の対応関係の明文化余地 (Task 009-6 §9.8、WO5 C-01)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: 各 SCR で主要行動が上流未定義。ボタン状態 follow-up #4 の実査待ち。Button variant 語彙 GOV-0002 の provenance 未確認。個別確認主体は未定。
- **Blocking Fact Type**: 1・2・5・6。横断: 7・8。
- **Direct Source**: WO5 §14「入力・検索仕様/表示仕様の上流未定義」相当の主要行動未定義、「Decision ID の provenance 未確認」「placeholder / 実査待ちの未取得」、SCR-004/SCR-005 §16、owner-decisions.md §3 follow-up #4。
- **Missing Evidence or Decision**: 各 SCR の主要行動の上流確定、follow-up #4 の実査結果、GOV-0002 の ADR 正本、確認方法・個別確認主体の決定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。provenance 確認 = 規則 §13。placeholder / 実査待ち確認方法決定 = 規則 §14。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、provenance を必須トリガーとするか (§21④)、確認方法・個別確認主体 (§14)、影響度判定 (§8)。
- **Eligible Follow-up Work**: 各 SCR での主要行動の判断・更新、GOV-0002 provenance 確認、follow-up #4 実査。
- **Reassessment Condition**: 主要行動が解決され、GOV-0002 provenance と follow-up #4 が確認され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 主要 CTA・variant の改廃。Navigation と CTA を混同しない。各 SCR Downstream Impact の Button 例を採用決定と解釈しない。
- **Does Not Authorize**: 主要 CTA の確定・variant 追加。

### 6.9 入力の状態表現・回復責務と DS Input 定義の対応の明文化

- **Candidate Aspect**: 検索条件の入力・状態表現・回復 (IA-OBJ-002/SDP-006/CTP-007) の責務と DS Input/SearchForm 定義の対応関係の明文化余地 (Task 009-6 §9.9、WO5 C-02)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: 入力項目・必須条件・バリデーション・条件保持方式が SCR-003 §16 の上流 Open Issue。Input 状態一式 follow-up #2 の実査待ち。GOV-0002 provenance 未確認。個別確認主体は未定。
- **Blocking Fact Type**: 1・2・5・6。横断: 7・8。
- **Direct Source**: WO5 §14「入力・検索仕様の上流未定義」「Decision ID の provenance 未確認」「placeholder / 実査待ちの未取得」、SCR-003 §16、owner-decisions.md §3 follow-up #2。
- **Missing Evidence or Decision**: 入力仕様の上流確定、follow-up #2 の実査結果、GOV-0002 の ADR 正本、確認方法・個別確認主体の決定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。provenance 確認 = 規則 §13。placeholder / 実査待ち確認方法決定 = 規則 §14。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、provenance を必須トリガーとするか (§21④)、確認方法・個別確認主体 (§14)、影響度判定 (§8)。
- **Eligible Follow-up Work**: SCR-003 側での入力仕様の判断・更新、GOV-0002 provenance 確認、follow-up #2 実査。
- **Reassessment Condition**: 入力仕様が解決され、GOV-0002 provenance と follow-up #2 が確認され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 入力項目・必須条件・バリデーション・履歴保持。
- **Does Not Authorize**: 入力項目・バリデーション・Input 状態の追加。

### 6.10 表示責務 (候補/価格/評価) と DS component (Card/PriceTag/ReviewStars) の対応の明文化

- **Candidate Aspect**: 宿泊施設候補・価格と条件・評価を UI として表現する責務と DS component の対応関係の明文化余地 (Task 009-6 §9.10、WO5 C-03/C-04/C-05/T-05)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: 表示項目・表示順・比較成立基準・料金構造・Review 提供元が SCR-004/SCR-005 §16・IA §11 の上流 Open Issue。Card 実 px/8 スロット・星実寸・「円」weight の実査待ち。`radius.card`・`shadow` の placeholder。個別確認主体は未定。
- **Blocking Fact Type**: 1・4・5・6。横断: 7・8。
- **Direct Source**: WO5 §14「表示仕様の上流未定義」「placeholder / 実査待ちの未取得」、SCR-004/SCR-005 §16、IA §11、WO4 §17.2。
- **Missing Evidence or Decision**: 表示仕様の上流確定、Card 実 px/8 スロット・星実寸・「円」weight の実査結果、`radius.card`/`shadow` placeholder の確定、確認方法・個別確認主体の決定。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。placeholder / 実査待ち確認方法決定 = 規則 §14 (個別確認主体は未定)。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、placeholder / 実査待ちの確認方法・個別確認主体 (§14)、影響度判定 (§8)。
- **Eligible Follow-up Work**: SCR-004/SCR-005/IA 側での表示仕様の判断・更新、確認方法決定後の実査 (Card 実 px 等) と placeholder 確定。
- **Reassessment Condition**: 表示仕様が解決され、実査待ち・placeholder が確認方法・主体の定義のもとで確定され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 一覧/詳細 UI・表示項目・token 値・Card の採用。IA Object を Component と同一視しない。
- **Does Not Authorize**: 表示項目・token 値・Card 採用の確定。

### 6.11 タイポグラフィ具体規格と CTP-008 責務の対応の明文化

- **Candidate Aspect**: タイポグラフィの具体規格・文字数制限と CTP-008 責務の対応関係の明文化余地 (Task 009-6 §9.11、WO5 T-03)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: タイポグラフィの具体規格・文字数制限が CTP-008 Does Not Decide の範囲であり、上流で内容が確定していない。主体の定義は内容の確定を意味しない。
- **Blocking Fact Type**: 1 (上流 Does Not Decide/Open Issue)。横断: 7・8。
- **Direct Source**: WO5 §14「表示仕様の上流未定義 (…CTP-008 Does Not Decide)」、content-principles.md CTP-008、design.md §3 タイポグラフィスケール。
- **Missing Evidence or Decision**: タイポグラフィ具体規格・文字数制限を上流で確定するか否かの判断 (現状は CTP-008 が Does Not Decide)。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12 (影響度別)。ただし CTP-008 が Does Not Decide とする範囲を上流で扱うかどうか自体が判断対象。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②) の中で、CTP-008 Does Not Decide の範囲を上流仕様として扱うかの判断、影響度判定 (§8)。
- **Eligible Follow-up Work**: 上流 (Service Design) での具体規格を扱うか否かの判断・記録。存在しない上流仕様への対応明文化を内容補完せずに開始しない。
- **Reassessment Condition**: タイポグラフィ具体規格の扱いが上流で判断・記録され、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: タイポグラフィ仕様・token 値・CTP-008 の範囲変更。
- **Does Not Authorize**: タイポグラフィ仕様・token 値の確定。

### 6.12 支援領域の表現責務と DS 対応の明文化 (限定的)

- **Candidate Aspect**: 支援 (FAQ/問い合わせ/Support)・Policy 本文 (CTP-003/006/010) を UI として表現する責務と DS 対応の関係の明文化余地 (Task 009-6 §9.12、WO5 C-09)。
- **Task 009-6 Current Judgment**: `現時点では開始できない`。
- **Remaining Blocking Fact**: サポート対象範囲・FAQ 構成・問い合わせ手段が SCR-013 §16 の上流 Open Issue。文言正本 `brand-content.md` の参照切れ。Accordion 等は未着手 (成果物不在)。
- **Blocking Fact Type**: 1・3。横断: 7・8。（未着手 Component は阻害 Fact 種別ではなく成果物不在であり、必要 Component・改訂候補へ変換しない）
- **Direct Source**: WO5 §14「可逆/不可逆・回復フローの上流未定義 (サポート範囲・FAQ 構成)」「文言・命名の正本不在」、SCR-013 §16、components.md 未着手一覧。
- **Missing Evidence or Decision**: サポート範囲・FAQ 構成の上流確定、`brand-content.md` の正本作成または有効性確認。
- **Existing Rule / Responsibility Route**: 上流 Open Issue 解決 = 規則 §12。参照切れ・正本作成/有効性確認 = 規則 §13。
- **Prerequisite Owner Judgment**: 上流 Open Issue の解決単位 (§21②)、参照切れ正本の扱いの影響度判定 (§8)。
- **Eligible Follow-up Work**: SCR-013 側でのサポート範囲・FAQ 構成の判断・更新、`brand-content.md` の正本確認。未着手 Component を必要 Component・改訂候補へ変換しない。
- **Reassessment Condition**: サポート範囲 Open Issue が解決され、`brand-content.md` の正本が確認可能になり、規則 §18 に基づき再評価がトリガーされたとき。
- **Does Not Decide**: 支援 component の採用・追加。未着手 component を改訂候補へ変換しない。
- **Does Not Authorize**: Accordion/フォーム/チャット/モーダル等の追加。

### 6.13 対応の網羅性 (Fact)

- 上記 6.1〜6.12 で Work Order 5・Task 009-6 の全 12 候補側面を漏れなく記録した。各候補の Current Judgment はすべて `現時点では開始できない` である。
- 種別 6 (placeholder/実査待ちの個別確認主体未定)・種別 7 (上流 Open Issue の解決単位未定)・種別 8 (再評価トリガー未確定) は複数候補に横断して現れる (共通性)。ただし各候補の具体的な上流 Open Issue・provenance・placeholder・実査待ち・参照切れは候補ごとに異なり、共通性を理由に候補別の影響を消していない。

## 7. Resolution Routes and Dependencies

後続作業を、依存関係に基づく解決経路として整理する。順序は証拠・判断の依存関係であり、ビジネス上の優先順位・重要度・対応期限ではない。各経路の主体は Review / Approval Rules の該当節による (影響度別の主体は各案件の影響度判定 §8 に従う)。

- **R-A: Web部責任者による経路・単位・確認方法の判断が先に必要なもの** — 上流 Open Issue の解決単位 (全体共通／成果物別／論点別、§21②)、placeholder / 実査待ちの確認方法と個別確認主体 (§14・§21③)、上流 Open Issue・provenance を再評価の必須トリガーとするか (§21④)、各後続タスクの影響度判定 (§8)。**これらは他の多くの経路の前提となる** (§8)。
- **R-B: Repository 内の直接証拠確認で進められる read-only 調査** — 各阻害 Fact の直接証拠・正本所在の再確認 (本計画が §6 で整理済み)。新しい直接証拠を生む read-only 調査は現時点では確認できない (参照切れ文書・placeholder・実査待ちは Repository 内に値/正本が存在せず、read-only では解決しない)。
- **R-C: Service Design / Screen Requirements 側で明示的な判断・更新が必要なもの** — Navigation 分類・状態モデル業務定義・IA Object 業務モデル・入力仕様・表示仕様・可逆/回復フロー・サポート範囲・タイポグラフィ具体規格の扱い・アクセシビリティ適用規格の扱い (規則 §12、R-A の解決単位判断に依存)。
- **R-D: Governance / ADR / provenance / 参照切れの正本確認が必要なもの** — GOV-0002・TVL-0007 の provenance (ADR 正本作成/有効性確認)、`brand-content.md`・`governance/naming-rules.md`・ADR 正本の不在解消 (規則 §13、R-A の影響度判定に依存)。
- **R-E: 実装・現行画面等の実査が必要なもの** — follow-up #2 (Input 状態)・#4 (ボタン状態)・Card 実 px/8 スロット・星実寸・「円」weight・画像 fallback・motion/shadow/radius placeholder (規則 §14 の確認方法決定と個別確認主体の定義=R-A に依存)。
- **R-F: 証拠取得後に候補採否または改定判断が必要なもの** — R-C/R-D/R-E で証拠が揃った候補について、Web部責任者が候補採否・改定要否・継続保留を判断 (規則 §9。本計画では判断しない)。
- **R-G: 設計判断後に改訂着手承認が必要なもの** — R-F の後、Web部責任者が改訂着手を承認 (規則 §9。本計画では承認しない)。
- **R-H: Work Order 6 相当の再評価へ戻すもの** — R-C/R-D/R-E で候補固有阻害 Fact が解決された後、規則 §18 に基づき全候補一括で再評価 (トリガー起点は主体定義=充足済み、上流 Open Issue・provenance を必須トリガーとするかは §21④ 未確定)。

**依存関係の要約 (順序ではなく依存)**: R-A (オーナー判断) → R-C / R-D / R-E (証拠取得、影響度別主体) → R-H (再評価) → R-F (採否・改定判断) → R-G (改訂着手承認) → 実際の Design System 改定 (別タスク・本計画外)。R-B は現時点で新たな進展を生まない。R-F・R-G・改定は本計画で決定・実施しない。

## 8. Owner Judgments Required

後続工程で Web部責任者の明示的回答が必要な事項を、既存 Open Issue から直接導出して整理する。**本計画では回答を推測・補完せず、質問候補と回答後の反映先だけを記録する。**

| # | 質問候補 (既存 Open Issue から導出) | 導出元 | 回答後の反映先 |
| --- | --- | --- | --- |
| Q1 | 上流 Open Issue を全体共通・成果物別・論点別のどの単位で扱うか | 規則 §12・§21②、owner-decisions.md §4「上流 Open Issue の解決単位」残 Open Issue | **回答済み (Task 009-8, 2026-07-21): 「論点別」。正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §7。論点別後続タスク候補への展開は §8A** |
| Q2 | placeholder / 実査待ちの確認方法 (検査方法・合格基準) | 規則 §14、owner-decisions.md §4「placeholder / 実査待ちの確認主体」 | placeholder / 実査待ち確認の後続タスク手順。確認方法の記録先は Web部責任者が定める |
| Q3 | 個別の placeholder / 実査待ちについて誰が確認するか (個別確認主体) | 規則 §14・§21③ (確認ルール制定まで未定) | 各 placeholder / 実査待ち項目の担当。本計画は未定のまま保持 |
| Q4 | 上流 Open Issue・provenance 未確認を再評価の必須トリガーとするか | 規則 §18・§21④ | Work Order 6 相当の再評価 (R-H) の起動条件 |
| Q5 | 各後続タスク (R-C/R-D/R-E 等) の影響度判定 (高／低) | 規則 §8 (判定主体=Web部責任者の都度判断) | 各後続タスクの必要レビュー主体 (§10・§11・§12・§13) と Wiki 影響度判定ログ (非正本) |

- Q1〜Q5 はいずれも Review / Approval Rules・owner-decisions.md §4 が「承認後も残る Open Issue」として明示した事項から導出したものであり、本計画が新設した質問ではない。
- 回答は Repository 内の追跡可能な直接証拠として取得・記録する必要がある (規則 §16 の承認ログ・§8 の Wiki 影響度判定ログ等、各事項の性質に応じた記録先)。本計画は回答を補完しない。

## 8A. Q1 回答と論点別後続タスク候補への展開 (Task 009-8)

### 8A.1 Q1 の回答

- **Q1「上流 Open Issue の解決単位」は Task 009-8 (2026-07-21) で回答済み**: Web部責任者の判断は **「論点別」**。
- 回答の正本は [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §7 (Review / Approval Rules §12・§21② に基づく案件別のプロセス判断記録)。設計承認ではない。
- **採用された解決単位**: 論点別。§6 で整理した上流 Open Issue を、論点 (テーマ) ごとの単位で後続解決タスクとして起票・追跡する。
- 本節は起票可能な単位への展開であり、実際の後続 Issue をすべて作成することではない。本 Task の Issue 以外の後続 Issue は作成しない。上流 Open Issue は解決済みにしない。Task 009-6 の判断 (全 12 候補「現時点では開始できない」) を変更しない。論点別のため、関連論点の優先順位は推測しない。

### 8A.2 論点別後続タスク候補 (9 論点)

各候補は上流 Service Design / Screen Requirements 側で明示的な判断・更新が必要なもの (§7 R-C)。**内容は SD/SR 側・Web部責任者が決めるものであり、本計画では決めない**。完了条件は「当該論点の上流 Open Issue について明示的判断・更新が該当上流成果物へ記録されること」であり、内容の当否・DS 対応は含まない。

#### T1. Navigation 分類・Global Navigation・History and Recovery
- **対象上流成果物・論点**: SD-003 navigation.md §10 (Global Navigation 対象領域・History and Recovery (NAV-005) 保持方式)、各 SCR §16。
- **対応する DS 候補側面**: §6.1。
- **必要な直接証拠**: navigation.md §10 Open Issue・各 SCR §16 の当該記述。
- **完了条件**: Global Nav 対象領域・History and Recovery 保持方式についての上流判断・更新が navigation.md / 該当 SCR に記録されること。
- **決定・承認しない**: NAV 分類の DS 対応・component 追加・候補採否・改定・改訂着手。Navigation と CTA を混同しない。

#### T2. 状態モデルの業務定義
- **対象上流成果物・論点**: SD-003/SD-004/SD-005 の Navigation State Model・CTA State Model・Status and Uncertainty Model、各 SCR §10 (Pending Confirmation・空結果/在庫切れ挙動・予約状態)。
- **対応する DS 候補側面**: §6.3。
- **必要な直接証拠**: 各 State Model 記述・各 SCR §10 の当該 Open Issue。
- **完了条件**: 状態の業務定義についての上流判断・更新が該当上流成果物へ記録されること。
- **決定・承認しない**: 状態の UI 表現・token 値・component。Navigation State Model・CTA State Model・Component state を同一視しない。SCR-014 に `Error / Interrupted` を追加しない。

#### T3. IA Object の業務モデル
- **対象上流成果物・論点**: SD-002 information-architecture.md §11 (IA Object の内容・関係・業務仕様、SCR-005/SCR-006 境界)。
- **対応する DS 候補側面**: §6.5。
- **必要な直接証拠**: information-architecture.md §11 Open Issue。
- **完了条件**: IA Object 業務モデルについての上流判断・更新が information-architecture.md へ記録されること。
- **決定・承認しない**: 専用表現語彙・component の要否。IA Object を Component/表示項目/データモデルと同一視しない。SCR-006〜012 を先取りしない。

#### T4. 入力・検索仕様
- **対象上流成果物・論点**: SCR-003 §16 (入力項目・必須条件・バリデーション・条件保持方式)。
- **対応する DS 候補側面**: §6.9。
- **必要な直接証拠**: SCR-003 §16 Open Issue。
- **完了条件**: 入力・検索仕様についての上流判断・更新が SCR-003 へ記録されること。
- **決定・承認しない**: Input 項目・バリデーション・状態の DS 追加・候補採否・改定。

#### T5. 表示項目・料金・評価仕様
- **対象上流成果物・論点**: SCR-004/SCR-005 §16・IA §11 (表示項目・表示順・比較成立基準・料金構造・Review 提供元)。
- **対応する DS 候補側面**: §6.10。
- **必要な直接証拠**: SCR-004/SCR-005 §16・IA §11 Open Issue。
- **完了条件**: 表示・料金・評価仕様についての上流判断・更新が該当 SCR / IA へ記録されること。
- **決定・承認しない**: 一覧/詳細 UI・表示項目・token 値・Card 採用。IA Object を Component と同一視しない。

#### T6. 主要行動・CTA
- **対象上流成果物・論点**: 各 SCR (SCR-004/SCR-005 等) の主要行動・情報確認と選択の区別 (CTA-001/CTA-004)。
- **対応する DS 候補側面**: §6.8。
- **必要な直接証拠**: 各 SCR §16 の主要行動に関する Open Issue。
- **完了条件**: 各 SCR の主要行動についての上流判断・更新が該当 SCR へ記録されること。
- **決定・承認しない**: 主要 CTA・variant の改廃・候補採否。Navigation と CTA を混同しない。

#### T7. 可逆・回復フロー・サポート範囲
- **対象上流成果物・論点**: SDP-006 (可逆/回復可能性、上流 Does Not Decide の範囲)・CTA-006・SCR-013 §16 (問い合わせ手段・処理フロー・サポート対象範囲・FAQ 構成)。
- **対応する DS 候補側面**: §6.4 (Recovery Action)・§6.6 (可逆/不可逆区別)・§6.12 (支援領域)。
- **必要な直接証拠**: SDP-006 の Does Not Decide 記述・SCR-013 §16 Open Issue。
- **完了条件**: 可逆/回復フロー・サポート範囲についての上流判断・更新が該当上流成果物へ記録されること。
- **決定・承認しない**: 可逆/不可逆規則・Recovery Action・支援 component の DS 追加。未着手 component を必要 component・改訂候補へ変換しない。

#### T8. タイポグラフィ具体規格の扱い
- **対象上流成果物・論点**: SD-004 content-principles.md CTP-008 (具体規格・文字数制限を上流で扱うか否か。現状 Does Not Decide)。
- **対応する DS 候補側面**: §6.11。
- **必要な直接証拠**: CTP-008 の Does Not Decide 記述。
- **完了条件**: タイポグラフィ具体規格を上流で扱うか否かの判断が content-principles.md へ記録されること。
- **決定・承認しない**: タイポグラフィ仕様・token 値・CTP-008 の範囲変更。

#### T9. アクセシビリティ適用規格の扱い
- **対象上流成果物・論点**: アクセシビリティの適用規格・達成レベル (SDP-007/NVP-008/CTP-008/CTA-009 の責務に対する規格・達成レベルを上流/Governance のどこで扱うか)。
- **対応する DS 候補側面**: §6.7。
- **必要な直接証拠**: design.md §2「WCAG 2.2 AA を最低ライン」記述・各 SCR §11・適用規格未定義の Open Issue。
- **完了条件**: 適用規格・達成レベルの扱い (どのレイヤーで確定するかを含む) についての判断が該当成果物へ記録されること。
- **決定・承認しない**: 達成基準値・実装方式・画像仕様。主体の定義を内容の確定と解釈しない。

### 8A.3 全 12 候補側面との対応 (網羅確認)

- 上流 Open Issue を含む 11 候補は上記 9 論点タスク候補へ対応する: §6.1→T1／§6.3→T2／§6.5→T3／§6.9→T4／§6.10→T5／§6.8→T6／§6.4・§6.6・§6.12→T7／§6.11→T8／§6.7→T9。
- **§6.2 (Navigation と CTA の責務分離を述べる DS 本文規則) の残る阻害 Fact は上流 Open Issue ではなく GOV-0002 の provenance 未確認 (種別 2) である**。したがって §6.2 は 9 論点の上流 Open Issue 解決タスク (R-C) では解消されず、provenance 確認トラック (§7 R-D、規則 §13) に属する。§6.2 の Navigation/CTA 責務の文脈は T1・T6 に隣接するが、混同しない。
- 上記 11 候補も、上流 Open Issue 以外の残る阻害 Fact (provenance 未確認・参照切れ・placeholder・実査待ち・placeholder/実査待ちの個別確認主体の未定) を併せ持つものがある (§6 各候補参照)。これらは論点別の上流 Open Issue 解決タスク (R-C) では解消されず、それぞれ provenance/参照切れトラック (R-D)・実査/placeholder トラック (R-E) に残り、Q2〜Q5 の未回答に依存する。論点別の起票単位は上流 Open Issue の解決タスクに適用されるものであり、これら非上流トラックを解決済みにしない。
- 以上により、全 12 候補側面の対応が失われていない (11 候補が 9 論点へ、§6.2 が provenance トラックへ、各候補の非上流残余が R-D/R-E トラックへ、それぞれ追跡可能)。

### 8A.4 未回答の Q2〜Q5 と次工程へ進めるために残る判断

- **未回答のまま保持 (§8)**: Q2 placeholder・実査待ちの確認方法／Q3 個別 placeholder・実査待ちの確認主体 (規則 §21③ で確認ルール制定まで未定)／Q4 上流 Open Issue・provenance を再評価の必須トリガーとするか／Q5 各後続タスクの影響度判定。本 Task ではこれらを推測・補完しない。
- **次工程へ進めるために残る判断**: 9 論点タスク候補の**どの論点 (単位) から着手するか** (owner-decisions.md §7「回答後も未決の事項」)。Repository 内に着手対象・優先順位の選定基準は存在しないため、本計画で「最優先」を決めない。加えて各論点タスク着手時に Q5 (当該タスクの影響度) が必要。

### 8A.5 次工程の推薦 (Task 009-8 後)

Q1 回答 (論点別) により後続解決タスクの起票単位は確定したが、9 論点タスク候補の着手対象・順序を選ぶ直接証拠 (選定基準・優先順位) は Repository 内に存在しない (§8A.4)。したがって直接証拠に基づき単一の上流 Open Issue 解決タスクを選べないため、**Web部責任者から最初に取得すべき判断を 1 件推薦する**。

- **推薦対象**: 9 論点タスク候補 (§8A.2 T1〜T9) の**どの論点 (単位) から着手するか**の Web部責任者判断。
- **推薦理由** (依存関係に基づく。優先順位・重要度をこちらで推測しない): 起票単位は論点別に確定したが、着手対象の選定基準が Repository 内に存在しないため、着手対象を Web部責任者が明示しない限り個々の上流 Open Issue 解決タスク (R-C) を開始できない。
- **前提条件**: 本 Task (Task 009-8) の owner-decisions.md §7 記録が Repository に存在すること。回答は Repository 内の追跡可能な直接証拠として記録すること。
- **必要な判断主体**: Web部責任者 (規則 §12・§8)。
- **想定する変更レイヤー**: Governance / プロセス上の判断の記録 (記録先は Web部責任者が定める)。着手判断自体は Design System 本体・上流成果物を変更しない。
- **対象外**: 各上流 Open Issue の内容そのものの解決、候補採否・改定要否・改訂着手、Q2〜Q5 の回答。着手論点が定まっても、その論点の内容解決・(該当すれば) provenance/参照切れ確認・実査・再評価・採否/改定判断・改訂着手承認を経ない限り、実際の Design System 改定は開始できない。
- **完了しても Design System 改定を開始できるとは限らない**: 本推薦の判断取得は着手対象を定めるのみであり、Design System 改定の開始を意味しない。

> **注記 (Task 009-9, 2026-07-21)**: 本 §8A.5 が推薦した「どの論点 (単位) から着手するか」の Web部責任者判断は取得済みである (回答「どれからでも構わない」、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §8)。本 §8A.5 は Task 009-8 時点の推薦記録として保持する。回答の反映は §8B を参照。

## 8B. 初回着手論点の回答と反映 (Task 009-9)

### 8B.1 Task 009-9 の回答取得

- **§8A.5 が推薦した「最初にどの論点から着手するか」の Web部責任者判断を Task 009-9 (2026-07-21) で取得済み**。
- **Web部責任者へ提示した論点**: T1〜T9 (§8A.2 の 9 論点。各の対象上流成果物・論点／対応する Design System 候補側面／完了条件／決定・承認しない事項を省略せず中立に提示)。推奨順位・重要度・効果・難易度・工数・期限は補完していない。
- **取得した回答 (原文の意味を変えず記録)**: **「どれからでも構わない」**。
- **最初に扱う論点**: 特定の 1 件に限定されず、T1〜T9 の**いずれからでも着手してよい**というオーナー判断 (初回着手論点の優先順位・限定は付与されない)。単一指定・順序付き・並行着手の明示・条件付き・現時点で選ばない、のいずれとも異なる。
- **回答の正本**: [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §8 (Review / Approval Rules §8・§12 に基づく案件別のプロセス判断記録。設計承認ではない)。本 §8B は現在状態の反映であり、§8A の履歴 (Q1 展開・§8A.5 推薦) を保持したまま追記する。

### 8B.2 選択された論点と対応 (現在状態)

- 特定の初回論点は指定されていない (「どれからでも構わない」)。したがって単一の「選択された論点」は存在せず、T1〜T9 のいずれもが最初の着手対象となり得る。
- 各論点と対象上流成果物・対応 Design System 候補側面の既存対応は §8A.2・§8A.3 のとおり (T1→§6.1／T2→§6.3／T3→§6.5／T4→§6.9／T5→§6.10／T6→§6.8／T7→§6.4・§6.6・§6.12／T8→§6.11／T9→§6.7)。本回答はこの対応を変更しない。
- **選択されなかった論点は存在しない** (どの論点も却下・不要・継続保留とされていない)。「どれからでも構わない」は残り論点の却下・不要・継続保留を意味しない。

### 8B.3 後続の上流 Open Issue 解決タスクに必要な事項 (現在状態)

- **必要な直接証拠**: 着手する論点に応じ §8A.2 記載の直接証拠 (該当 SD/SR の Open Issue 箇所)。
- **後続タスクの起票前・開始前に必要な影響度判定**: 各後続の上流 Open Issue 解決タスクは、その**影響度判定 (Q5, 規則 §8。Web部責任者の都度判断)** を取得しない限り、規則 §10・§11・§12 の必要レビュー・反映経路が確定しない。**Q5 は本 Task (Task 009-9) の影響度 (＝高) とは別であり、各後続タスクごとに未回答のまま保持する**。
- **後続タスクが完了しても残る阻害 Fact**: ある論点の上流 Open Issue が解決 (R-C) されても、対応候補には上流 Open Issue 以外の阻害 Fact が残り得る — provenance 未確認 (GOV-0002・TVL-0007 等, R-D)・参照切れ/正本不在 (`brand-content.md`・`governance/naming-rules.md`・ADR 正本, R-D)・placeholder・実査待ち (R-E)・placeholder/実査待ちの個別確認主体の未定 (Q3)。さらに他論点の上流 Open Issue、Work Order 6 相当の再評価 (R-H)、候補採否/改定判断 (R-F)、改訂着手承認 (R-G) が未了である。§6.2 は上流 Open Issue ではなく provenance トラック (R-D) に属し、いずれの論点解決でも解消されない。

### 8B.4 未回答の Q2〜Q5 と保持事項

- **未回答のまま保持 (§8)**: Q2 placeholder・実査待ちの確認方法／Q3 個別確認主体 (規則 §21③ で確認ルール制定まで未定)／Q4 上流 Open Issue・provenance を再評価の必須トリガーとするか／**Q5 各後続タスクの影響度判定 (本 Task の影響度ではない)**。本 Task ではこれらを推測・補完しない。
- **不変**: Task 009-6 の全 12 候補「現時点では開始できない」は変わらない。§7「解決単位＝論点別」は変わらない。**本回答により Design System 改定を開始できる状態になったとは限らない** (各論点の内容解決・provenance/参照切れ確認・実査・再評価・候補採否/改定判断・改訂着手承認を経ない限り開始できない)。

### 8B.5 次工程の推薦 (Task 009-9 後)

Web部責任者は初回着手論点を特定の 1 件に限定せず「どれからでも構わない」とした (優先順位・限定を付与しない)。これにより「どの論点から着手するか」という選択の制約は外れ、T1〜T9 のいずれからでも上流 Open Issue 解決タスクを開始してよい。したがって次工程として**単一の上流 Open Issue 解決タスク (Task 009-10 を使用可能) を推薦する**。ただし特定の論点はオーナーが限定していないため、本計画では独自に 1 件を選定しない (どの論点を取り上げるかは着手時に特定される)。

- **推薦対象**: T1〜T9 のうち 1 論点の上流 Open Issue 解決タスク (Task 009-10)。オーナーはいずれからでも着手してよいとしており、具体の論点は着手時に特定する (本計画では独自に選定しない)。実際の後続 Issue は本 Task 内では作成しない。
- **推薦理由** (依存関係に基づく。優先順位・重要度・効果を推測しない): 解決単位は論点別に確定 (§7)、初回着手論点はオーナーが「どれからでも構わない」とし選択制約が外れたため、上流 Open Issue 解決タスク (R-C) を開始できる状態にある。着手対象の限定はオーナーが付与していないため、こちらから 1 件へ絞り込まない。
- **前提条件**: owner-decisions.md §8 の本判断が Repository に存在すること。着手する論点の**影響度判定 (Q5)** を、その後続タスクの起票・レビュー・反映の前に Web部責任者から取得すること。
- **必要な判断主体**: 着手論点の影響度判定 = Web部責任者 (規則 §8)。上流 Open Issue 内容の解決確認 = 影響度別 (規則 §12)。
- **必要レビュー主体**: **後続タスクの影響度判定 (Q5) 前は未確定** (影響度・高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Service Design / Screen Requirements (該当論点の上流成果物での明示的判断・更新)。Design System 本体は変更しない。
- **対象となる上流成果物・対応する Design System 候補側面・必要な直接証拠・完了条件**: 着手する論点に応じ §8A.2 の該当行 (T1〜T9) を参照。特定の論点が未限定のため、本推薦では単一に絞らず §8A.2 を正とする。
- **対象外**: 上流 Open Issue の内容そのものの解決の当否、候補採否・改定要否・継続保留・改訂着手、Q2〜Q4 の回答、他論点の着手順序。
- **完了しても Design System 改定を開始できるとは限らない**: 着手した論点の上流 Open Issue が解決されても、§8B.3 の残る阻害 Fact・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。選択された論点の内容・解決案を先回りして補完しない。

## 8C. T1 の結果 (Task 009-10)

### 8C.1 着手根拠と影響度

- **着手根拠**: owner-decisions.md §8「どれからでも構わない」。T1 は §8A.2 の一覧先頭を**機械的に選択**したものであり、優先順位・重要度判断ではない。
- **影響度**: 高 (Web部責任者判定、2026-07-21。付言「ルール制定段階では以降すべて高」)。必要レビュー主体 = Review / Approval Rules §10 既定 = Web部責任者 ＋ チーフデザイナー。

### 8C.2 取得した回答と確定した整理

- **Global Navigation (3.2)**: 本案件では現行の対象領域・導線を維持し新規追加しない旨は「はい」。ただし機能・コンテンツ変更可否は案件によるため横断ルール化しない。
- **History and Recovery (3.3)**: 「いいえ」。案件次第であり、現行動作の変更を今後一切受け付けないという趣旨ではない。
- **確定した整理 (Web部責任者)**: Global Navigation の対象領域・History and Recovery の保持方式は、**Service Design 層で固定する必要のない事項**である (案件ごと・実装レベルで扱い、上流仕様として確定しないのが適切)。「案件次第」「本案件では現行維持」といった案件ごとの判断・運用は Service Design の正本 (`navigation.md`) へ書き込まない (設計正本を案件判断へ結合させ、変更のたびに設計正本の保守が必要になる事態を避けるため)。

### 8C.3 上流成果物の扱い

- **上流成果物は本案件で変更しない**: [../service-design/navigation.md](../service-design/navigation.md) および Screen Requirements は変更しない。NAV-001 Global Navigation・NAV-005 History and Recovery Navigation・NVP-003 Preserved Context・NVP-004 Reversible Movement・§7 Context Preservation and Recovery の設計責務は現状のまま (現行の Draft を維持)。
- **定義化・変更しない理由**: Design System を含むアプリケーション仕様の変更は案件次第であるため、Global Navigation の対象領域・History and Recovery の保持方式は本工程では定義化しない。この立場は本項に限らず全域に及ぶ一般的な理由であり、T1 限定の例外ではない。よって上流成果物 (`navigation.md`・Screen Requirements) を変更しない。なお §8A.2 T1 の完了条件文言「上流判断・更新が `navigation.md` / 該当 Screen Requirements へ記録されること」は、上流で定義化する場合を想定した記述であり、定義化しない本件には字義どおりには当てはまらない (§8A.2 は Task 009-8 時点の記述として変更しない)。〔Task 009-10-F1〕当初 §8C.3 にあった「T1 完了」の宣言・完了条件の充足評価・「例外」という枠組みは、案件次第ゆえ定義化しないという上記の位置づけと字義上食い違い、かつ本項の趣旨に照らして不要であるため、削除した。
- **`navigation.md` §10 Open Issue の扱い**: `navigation.md` §10 の Open Issue「Global Navigation の対象領域」「履歴・文脈保持方式」は、本工程では定義化しない (上流仕様として確定を要しない) 位置づけである。設計正本を触らない方針のため、`navigation.md` 本文の Open Issue 記載自体は本案件で変更しない。
- **未確認として残る事項 (推測しない)**: 現行 Global Navigation の具体的な対象領域・項目・表示順・ラベル・遷移先／History and Recovery の現行実装が実際に保持する条件・文脈・保存方式・保存期間・セッション仕様・ブラウザバック等の具体挙動。いずれも直接証拠がない。ただし「本工程では定義化しない」という位置づけのため、これらは上流確定の前提条件ではない。

### 8C.4 §6.1 との対応・全体状態

- **§6.1 との対応**: T1 の DS 候補側面 §6.1 (NAV 分類と DS Navigation component の対応の明文化) は、上流の対象領域が上流で固定されない (固定不要) ため、その明文化を上流固定に基づいて進めることはできない。§6.1 の Task 009-6 Current Judgment「現時点では開始できない」は**変わらない** (Task 009-6 の再評価成果物は不変)。
- **T2〜T9**: 未解決 (未着手)。
- **Q2〜Q4**: 未回答。**Q5**: T1 について「高」取得済み。T2〜T9 では未回答。
- **Task 009-6 の判断**: T1 の本結果は、Task 009-6 の全 12 候補「現時点では開始できない」を自動的に変更しない。
- **T1 以外の残る阻害 Fact**: provenance 未確認 (GOV-0002・TVL-0007 等)・参照切れ (`brand-content.md`・`governance/naming-rules.md`・ADR 正本)・placeholder・実査待ち・placeholder/実査待ちの個別確認主体の未定・Work Order 6 相当の再評価 (R-H) 未実施。
- **Design System 改定を開始できる状態になったとは限らない**: T1 の整理は上流成果物の変更不要を結論づけたのみであり、DS 改定の開始を意味しない。
- 機能・コンテンツ変更可否・「案件次第」を横断ルールとして codify していない。6 分類の正式承認・NAV ID 正式採用・Navigation Principle 正式承認は行っていない。

### 8C.5 次工程の推薦 (Task 009-10 後)

- **T1 の状態と残る依存関係の評価**: T1 は「本工程では定義化しない (Service Design 層で固定する必要のない事項)」と整理され、上流成果物の変更は不要と結論づけた (「完了」という宣言・完了条件の充足評価は用いない。§8C.3・Task 009-10-F1)。T1 固有に残る未確認事項 (現行仕様の直接証拠) はあるが、「定義化しない」という位置づけにより、それらを解消しないと T1 を先へ進められない、という依存関係は生じない (上流固定を前提としないため)。よって T1 固有の追加解消タスクを優先候補としない。
- **推薦対象**: T2〜T9 の未着手論点から 1 件。owner-decisions.md §8「どれからでも構わない」により、§8A.2 の未着手一覧の次項 **T2「状態モデルの業務定義」** を**機械的に選択**する (Task 009-11 を使用可能)。
- **推薦理由** (優先順位・重要度・効果を推測しない): 「どれからでも構わない」により着手順の制約がなく、一覧先頭 T1 の次項が T2 であるため機械的に選択したものである。T2 を最優先・最重要とする判断ではない。なお T1 の結果 (上流で固定する必要のない事項という整理) は、残る論点にも同種の整理があり得ることを示唆するが、各論点の扱いは着手時に個別確認するものであり、本推薦で先回りして決めない。
- **前提条件**: 本 §8C の記録が Repository に存在すること。T2 着手前に T2 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T2 の影響度判定 = Web部責任者 (規則 §8)。上流 (状態モデル業務定義) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T2 の影響度判定 (Q5) 前は未確定 (影響度・高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Service Design / Screen Requirements (T2 に該当する上流成果物)。ただし T1 と同様、案件判断を設計正本へ結合させない方針は維持する。Design System 本体は変更しない。
- **対象上流成果物**: §8A.2 T2 記載のとおり (SD-003/004/005 の各 State Model・各 SCR §16)。
- **必要な直接証拠**: §8A.2 T2 記載の該当 Open Issue 箇所。
- **完了条件**: T2 の上流 Open Issue についての明示的判断が記録されること (内容は SD/SR 側・Web部責任者が決める。本計画では決めない)。
- **対象外**: T1 の再判断、T2 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答、T3〜T9 の着手順序。
- **Q4・再評価の前後関係**: Repository 内の依存関係 (§7) 上、上流論点の解決 (R-C) は再評価 (R-H) の前段であり、Q4 (再評価トリガー扱い) や Work Order 6 相当の再評価は T2 着手の前提ではない。したがって T2 着手前に Q4・再評価を要求しない。
- **完了しても Design System 改定を開始できるとは限らない**: T2 の上流判断が記録されても、他論点・provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

> **注記 (Task 009-11, 2026-07-22)**: 本 §8C.5 が推薦した次工程 (T2) は Task 009-11 で着手した。ただし Task 009-11 は指示者判断により「T2 状態モデルの業務定義」から **「T2 状態論点のスコープ選別・再分類」** へ再定義され、状態の業務仕様を新規定義せず、T2 に集約された論点の現在位置を選別・記録する工程となった。結果は §8D。本 §8C.5 は Task 009-10 時点の推薦記録として保持する。

## 8D. T2 の結果 (Task 009-11): 状態論点のスコープ選別・再分類

### 8D.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T2 状態モデルの業務定義」ではなく **「T2 状態論点のスコープ選別・再分類」** とする。T2 に集約された論点を直接証拠に基づき分解し、現在位置 (対象外・既存原則で充足・画面別未解決・上流設計課題・DS 内部整合・判定保留) を個別に選別・記録する。状態名・状態遷移・予約フロー・空結果/在庫切れの具体挙動を新たに設計・創作しない。
- **着手根拠**: owner-decisions.md §8「どれからでも構わない」により、§8A.2 の未着手一覧の次項 T2 を**機械的に選択**した (優先順位・重要度・効果の判断ではない)。T1 の「本工程では定義化しない」という結果を T2 へ自動適用していない (T2 として個別に点検した)。
- **影響度**: 高 (Web部責任者判定、2026-07-22、本件として明示取得)。理由 = 阻害 Fact の意味・解決計画上の分類・後続工程の扱い・Design System 候補側面との依存関係に影響し得る実質的変更のため。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8D.2 分類方法

各論点を次の 6 観点へ分解し、7 区分のいずれかへ分類した。

- **分解観点**: (1) 発生条件・判定ロジック、(2) 利用者への状態伝達、(3) 利用者が取れる次の行動、(4) 業務状態・業務フロー、(5) 3 つの State Model 間の責務、(6) Design System 側の表現責務。
- **分類区分**: Repository 全体の対象外 / 本工程・本レイヤーの対象外 / 既存原則で明示的に充足 / 原則のみ充足 (画面別未確定) / 未解決の上流設計課題 / DS 内部整合課題 / 判定保留。

### 8D.3 3 つの State Model の責務関係 (直接証拠に基づく確認)

現行正本に既に明示されている責務であり、新規の未解決業務定義ではない (分類 = 既存原則で明示的に充足)。

- **Navigation State Model** ([../service-design/navigation.md](../service-design/navigation.md) §6): 利用者タスク上の段階・文脈を扱う。冒頭に「業務上の予約状態や画面遷移を定義するものではない」と明記。
- **Status and Uncertainty Model** ([../service-design/content-principles.md](../service-design/content-principles.md) §7): 情報の確定度・利用可能性・不確実性を扱う。冒頭に「システム状態一覧や業務状態遷移を定義するものではない」と明記。
- **CTA State Model** ([../service-design/cta-principles.md](../service-design/cta-principles.md) §6): 行動の実行可否・処理・結果・追加確認を扱う。冒頭に「システム実装上の状態一覧や Component 仕様は定義しない」と明記。
- **確認事項 (直接証拠あり)**: 3 モデルは異なる観点を扱い、1 対 1 対応ではなく、単一の共通状態一覧ではない。Navigation State と予約業務状態を同一視しない。CTA State と Component state を同一視しない。Status and Uncertainty Model を予約状態一覧として使用しない。以上は上記各正本に既に記載されており、本工程で新たに定義・変更しない。

### 8D.4 論点別の再分類結果

| 論点 | 主な分解観点 | 分類結果 | 直接証拠 | §6.3 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| Pending Confirmation | (5)(6) | 既存原則で明示的に充足 | cta-principles §6「追加確認が必要／確約前に対象・条件・影響を確認可能にする」 | 残さない (新規業務定義ではない) |
| 空結果: 発生条件・判定ロジック | (1) | Repository 全体の対象外 | SCR-004 §13/§15 (API/DB/検索エンジンは Implementation)、SCR-003 §13 | 対象外として整理 |
| 空結果: 状態伝達・次の行動 | (2)(3)(6) | 原則のみ充足 + 未解決の上流設計課題 (画面別) / 判定保留 | 一般原則 CTP-006/CTP-007・SDP-005/SDP-006 は存在。画面別は SCR-004 §16「候補が存在しない場合の扱い」が Open Issue。状態割当の直接証拠なし | 画面別 Open Issue と判定保留を残す |
| 在庫切れ: 判定ロジック | (1)(4) | Repository 全体の対象外 (実行時) または業務・製品仕様 | SCR-004 §13、SCR-005 §5 は Price/Availability を IA object から除外 | 対象外として整理 |
| 在庫切れ: 状態伝達・次の行動 | (2)(3)(6) | 原則のみ充足 + 未解決の上流設計課題 (画面別) / 判定保留 | SCR-004 §16「Availability の状態・粒度・表示基準」が Open Issue。状態割当の直接証拠なし | 画面別 Open Issue と判定保留を残す |
| 予約業務状態 | (4)(5) | 本工程・本レイヤーの対象外 | navigation §6「業務上の予約状態…を定義しない」、screen-matrix §7 は「予約状態遷移」を対象外、help-and-support §5「予約管理機能・予約状態を取り込まない」、SCR-006〜012 未作成 | 対象外 (将来 Booking SR・業務/製品仕様側)。解決済みとは記載しない |
| Error / Interrupted の扱い | (5) | 既存原則で明示的に充足 | navigation §6・各 SCR §10 で「複合状態名として扱い分割しない」、SCR-014/001/002 §10「独断で追加しない」 | 残さない (分割・追加は行わない) |
| SCR-014 への Error / Interrupted 追加 | (5) | 本工程では追加しない (直接証拠・回答なし) | screen-matrix §5 SCR-014 = Entry/Exploring/Evaluating、editorial-content §10 | 現状維持 |

- **空結果・在庫切れの補足**: 発生条件が対象外であることだけを理由に、画面別の伝達・次の行動まで「解決済み」「対象外」とはしない。一般原則が存在すること (CTP-006/CTP-007 等) と、SCR-004 の画面別の具体的扱いが確定していることは別であり、後者は Open Issue として残る。直接証拠がないため、空結果・在庫切れを `Error / Interrupted`・`Unavailable`・`Unknown` 等の特定状態へ確定しない (判定保留)。
- **予約業務状態の補足**: 予約業務状態一覧・遷移 (予約前・予約中・予約済み・取消済み・変更中・返金中 等) は創作しない。対象外へ再分類することは、予約業務状態そのものが解決済みであることを意味しない。

### 8D.5 §6.3・§8A.2・§8C.5 との関係、保持事項

- **§6.3 との関係**: §6.3 の Remaining Blocking Fact を本再分類の粒度へ精密化した (§6.3 に注記)。§6.3 の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。
- **§8A.2 T2 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T2 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8D は現在状態の再分類記録である。
- **§8C.5 との関係**: §8C.5 が推薦した次工程が本 Task で着手されたことを §8C.5 に注記した (推薦記録は保持)。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-10-F1 の snapshot/履歴は監査証跡として変更しない (本 §8D から参照するのみ)。
- **保持事項**: T3〜T9 は未着手・未解決。Q2〜Q4 は未回答。Q5 は T1・Task 009-4-F1 の既存記録を変更せず T2 の影響度「高」を追加。ボタン状態 follow-up #4・motion placeholder・placeholder/実査待ちの確認方法・個別確認主体・DS 側状態表現との対応は未解決/未定のまま保持。Task 009-6 の全 12 候補「現時点では開始できない」は不変。
- **本 Task の完了の意味**: 「Task 009-11 という再分類作業の完了」であり、「T2 に含まれた全仕様の解決」ではない。状態モデルの業務定義完了・全画面別状態の確定・§6.3 阻害 Fact の全解消・Design System 改定開始可能・Alignment 完了条件充足のいずれも宣言しない。

### 8D.6 次工程の推薦 (Task 009-11 後)

- **推薦対象**: T3「IA Object の業務モデル」(§8A.2 T3)。未着手一覧の次項として**機械的に選択**したものである。
- **推薦理由**: owner-decisions.md §8「どれからでも構わない」により着手順の制約がなく、一覧上 T2 の次項が T3 であるため。**優先順位・重要度判断ではない**。T2 の結果 (スコープ選別により多くが対象外・既存原則充足) を T3 へ一般化しない。T3 も着手時に個別のスコープ選別が必要となり得る (先回りして決めない)。
- **前提条件**: 本 §8D の記録が Repository に存在すること。T3 着手前に T3 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T3 の影響度判定 = Web部責任者 (規則 §8)。上流 (IA Object 業務モデル) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T3 の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Service Design / Screen Requirements (T3 該当の上流成果物)。ただし T3 も対象外・既存充足の選別を要し得る。Design System 本体は変更しない。
- **対象上流成果物・必要な直接証拠**: §8A.2 T3 記載のとおり (SD-002 information-architecture.md §11 Open Issue)。
- **完了条件**: T3 の各論点が指定観点へ分解され、直接証拠付きで分類され、元記録との関係が追跡でき、§6.3 の該当 Remaining Blocking Fact が精密化されること (内容は着手時に確定)。
- **対象外**: T2 の再判断、T3 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答、T4〜T9 の着手順序。
- **Q4・再評価の前後**: Repository 内の依存関係 (§7) 上、上流論点の整理 (R-C) は再評価 (R-H) の前段であり、Q4・Work Order 6 相当の再評価は T3 着手の前提ではない。
- **完了しても Design System 改定を開始できるとは限らない**: T3 の整理が記録されても、他論点・provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

> **注記 (Task 009-12, 2026-07-22)**: 本 §8D.6 が推薦した次工程 (T3) は Task 009-12 で着手した。ただし Task 009-12 は指示者判断により「T3 IA Object の業務モデル」から **「T3 IA 論点のスコープ選別・再分類」** へ再定義され、IA 業務モデルを新規定義せず、T3 に集約された論点の現在位置を選別・記録する工程となった。結果は §8E。本 §8D.6 は Task 009-11 時点の推薦記録として保持する。

## 8E. T3 の結果 (Task 009-12): IA 論点のスコープ選別・再分類

### 8E.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T3 IA Object の業務モデル」ではなく **「T3 IA 論点のスコープ選別・再分類」** とする。IA Object・業務関係・予約構造・会員分類・料金/在庫モデル等を推測で新規設計せず、T3 に集約された論点の現在位置を選別・記録する。T3 固有の根拠 = information-architecture.md が「IA は概念モデルであり画面・API・DB を定義しない／具体的な業務モデルへ踏み込まない」(§1・§2) と明記し、12 IA Object には既に Draft の定義・責務・概念関係が存在する (§5〜§7) こと。これは T2 の結果を自動適用したものではなく、T3 固有の直接証拠に基づく。
- **着手根拠**: §8D.6 が T3 を未着手一覧の次項として機械的に推薦したことによる (owner-decisions.md §8「どれからでも構わない」・一覧上 T2 の次項)。優先順位・重要度判断ではない。
- **影響度**: 高 (Web部責任者判定、2026-07-22、本件として明示取得)。理由 = 阻害 Fact の意味・分類・後続工程・Design System 候補側面 §6.5 との関係に影響し得る実質的変更のため。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8E.2 分類方法

各論点を 10 観点へ分解し、8 区分のいずれかへ分類した。

- **分解観点**: (1) IA Object の存在・識別、(2) Object の定義・責務、(3) Object が含み得る概念、(4) Object 間の概念関係、(5) 正式な業務関係・業務処理、(6) 画面単位の Primary/Supporting 責務、(7) SCR-005/SCR-006 境界、(8) 運用データ・API・DB・外部システムとの対応、(9) Design System 上の表現責務、(10) 命名・正式 ID・用語の正本。
- **分類区分**: 既存 Draft で明示 / 未解決の IA 概念設計 / 事業・商品・業務仕様 / Screen Requirements 課題 / Governance 課題 / Repository 全体の対象外 / DS 内部整合課題 / 判定保留。

### 8E.3 12 Core Information Objects の既存状態 (直接証拠に基づく確認)

- information-architecture.md §5 は IA-OBJ-001〜012 について **Definition・Responsibility・Includes・Relationships・Does Not Decide・Status を Draft で既に定義**している。§6 Conceptual Relationship Model・§7 Relationship Matrix に概念関係が、§8 Ownership and Source of Truth に「運用データ (施設・在庫・料金・予約の実データ) の正本は本 Repository で管理しない／実装が本 IA をそのまま DB モデルとして使用してはならない／API・DB・外部サービスは未確認」が、§9 Boundary に除外範囲 (画面・URL・API・DB・料金計算・在庫管理・予約状態遷移・決済処理) が、§11 に Open Issues が記載されている。
- したがって「IA Object の内容・関係が何も定義されていない」とは扱わない (分類 = 既存 Draft で明示)。同時に、12 Object を正式承認済みとみなさず、既存 Object を新規定義として再作成せず、Object を Component・表示項目・DB entity と同一視せず、新しい Object を推測で追加せず、暫定 ID を恒久 ID として承認しない。「Draft として存在すること」と「正式な業務モデルが確定していること」を区別する。

### 8E.4 論点別の再分類結果

| 論点 (対象 Object) | 主な観点 | 分類結果 | 直接証拠 | §6.5 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| 12 Object の定義・責務・概念関係 | (1)(2)(3)(4) | 既存 Draft で明示 | information-architecture.md §5・§6・§7 | 残さない (既定義。正式承認は別) |
| Accommodation/Room/Stay Plan/Availability/Price の**正式な業務関係**・料金計算・在庫更新・販売単位 | (5) | 事業・商品・業務仕様 | IA §5 各 Object Does Not Decide (「業務モデルは確定しない」)・§11・§7 Notes「業務関係は Open Issue」 | 事業・業務仕様側として整理 (IA §11 に保持)。推測しない |
| 同上の **API・DB・データ構造** | (8) | Repository 全体の対象外 | IA §8 (運用データ正本は Repository 外・実装 DB に使うな)・§9 Boundary | 対象外として整理 |
| Destination の**正式階層** | (5)(8) | 事業・商品・業務仕様 (+ URL/検索index/DB は対象外) | IA-OBJ-001 Does Not Decide (階層構造は確定しない)・§11 | 事業・業務仕様側。階層を推測せず URL/DB へ展開しない |
| Policy の**正式分類・個別業務規則** | (2)(5) | 事業・商品・業務仕様 (分類の一部は未解決 IA 概念設計) | IA-OBJ-008 Does Not Decide (分類は確定しない)・§11 | 事業・業務仕様側。Policy Object の存在を個別規則の確定とみなさない |
| Review の**評価対象・提供元・信頼性・表示基準** | (2)(5)(8) | 事業・商品・業務仕様 / データ源は対象外 | IA-OBJ-009 Does Not Decide (提供元・信頼性・表示基準は確定しない)・§11 | 事業・業務仕様側。ReviewStars Component と同一視しない (DS 内部整合は別) |
| User/Booker/Guest/Member の**正式分類・会員・認証** | (2)(5) | 事業・会員・認証仕様 | IA-OBJ-011 Does Not Decide (会員制度・識別方法未定義・正式ユーザーモデル確定しない)・§11 | 事業・会員・認証仕様側。IA 上の主体表現と分離 |
| Booking の**業務構造・状態・変更/取消/返金・決済** | (5) | 事業・商品・業務仕様 | IA-OBJ-010 Does Not Decide (正式な予約状態・業務処理は確定しない)・§11。Task 009-11 で予約業務状態は本レイヤー対象外と整理済み | 事業・業務仕様側。状態一覧・フローを創作しない |
| Content の**正式分類・責務・戦略** | (2)(5) | 事業・コンテンツ戦略 (+ `brand-content.md` は Governance/正本) | IA-OBJ-012 Does Not Decide (分類・優先順位は確定しない)・§11 | 事業・戦略側 + 参照切れは Governance。想定内容を補完しない |
| 12 Object の**正式承認・正式用語・IA Object ID**・`brand-content.md` 正本 | (10) | Governance 課題 | IA §5・§11 (正式命名規則は未整備)・governance/README 未整備 | Governance/命名規則側 (未整備) |
| IA Object・Content Category と **DS 表現語彙の対応** (C-10/X-06) | (9) | DS 内部整合課題 | WO4 C-10/X-06・IA §10 | §6.5 の DS 対応整理として残る (T3 再分類で自動解決しない) |
| **SCR-005/SCR-006 境界** | (6)(7) | Screen Requirements 課題 | accommodation-detail.md §2/§5/§16 (SCR-005 は Accommodation 確認・評価、Room/Stay Plan 選択・確約・在庫・料金・予約開始を取り込まない／SCR-005⇔SCR-006 境界は Open Issue)。SCR-006〜012 未作成 | Screen Requirements 課題 (未確定)。推測せず統合・分割しない |

### 8E.5 §6.5・§8A.2 T3・§8D.6 との関係、保持事項

- **§6.5 との関係**: §6.5 の Remaining Blocking Fact を本再分類の粒度へ精密化した (§6.5 に注記)。§6.5 の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。
- **§8A.2 T3 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T3 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8E は現在状態の再分類記録である。
- **§8D.6 との関係**: §8D.6 が推薦した次工程が本 Task で着手されたことを §8D.6 に注記した (推薦記録は保持)。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-11 の snapshot/履歴は監査証跡として変更しない (本 §8E から参照するのみ)。
- **保持事項**: T4〜T9 は未着手・未解決。Q2〜Q4 は未回答。Q5 は T1・Task 009-4-F1・T2 の既存記録を変更せず T3 の影響度「高」を追加。`brand-content.md` 参照切れ・正式命名規則・IA Object ID の未確定・SCR-006〜012 未作成・§6.5 の DS 表現語彙との対応に残る未確認事項は保持。Task 009-6 の全 12 候補「現時点では開始できない」は不変。
- **本 Task の完了の意味**: 「Task 009-12 という再分類作業の完了」であり、「IA Object の業務モデルの確定」「12 Object の正式承認」「IA §11 の全 Open Issues の解決」「SCR-005/SCR-006 境界の確定」「§6.5 阻害 Fact の全解消」「Design System 改定開始可能」「Alignment 完了条件充足」のいずれも宣言しない。

### 8E.6 次工程の推薦 (Task 009-12 後)

- **推薦対象**: T4「入力・検索仕様」(§8A.2 T4)。未着手一覧の次項として**機械的に選択**したものである。
- **推薦理由**: owner-decisions.md §8「どれからでも構わない」により着手順の制約がなく、一覧上 T3 の次項が T4 であるため。**優先順位・重要度判断ではない**。T3 の結果 (スコープ選別により多くが事業・業務仕様/対象外/既存 Draft) を T4 へ一般化しない。T4 も着手時に個別のスコープ選別が必要となり得る (先回りして決めない)。
- **前提条件**: 本 §8E の記録が Repository に存在すること。T4 着手前に T4 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T4 の影響度判定 = Web部責任者 (規則 §8)。上流 (入力・検索仕様) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T4 の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Screen Requirements (SCR-003)。ただし T4 も対象外・既存充足・事業仕様の選別を要し得る。Design System 本体は変更しない。
- **対象上流成果物・必要な直接証拠**: §8A.2 T4 記載のとおり (SCR-003 §16 Open Issue)。
- **完了条件**: T4 の各論点が指定観点へ分解され、直接証拠付きで分類され、元記録との関係が追跡でき、§6.9 の該当 Remaining Blocking Fact が精密化されること (内容は着手時に確定)。
- **対象外**: T3 の再判断、T4 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答、T5〜T9 の着手順序。
- **Q4・再評価の前後**: Repository 内の依存関係 (§7) 上、上流論点の整理 (R-C) は再評価 (R-H) の前段であり、Q4・Work Order 6 相当の再評価は T4 着手の前提ではない。
- **完了しても Design System 改定を開始できるとは限らない**: T4 の整理が記録されても、他論点・provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

## 9. Recommended Next Work

直接証拠と依存関係 (§7) から、Task 009-7 後に最初に着手できる単一の後続作業を検討した。§6 のとおり全 12 候補の候補固有阻害 Fact の解決 (R-C/R-D/R-E) は、いずれも R-A のオーナー判断 (解決単位・確認方法・個別確認主体・トリガー扱い・影響度) を前提とする。read-only 調査 (R-B) は現時点で新たな進展を生まない (参照切れ・placeholder・実査待ちは Repository 内に値/正本が存在しない)。したがって直接証拠から単一の後続「作業」を推薦できないため、Review / Approval Rules §6.7 の代替に従い、**最初に取得すべき Web部責任者の判断を 1 件推薦する**。

- **推薦対象**: §8 Q1「上流 Open Issue を全体共通・成果物別・論点別のどの単位で扱うか」の Web部責任者判断 (規則 §12・§21②)。
- **推薦理由** (依存関係に基づく。優先順位・重要度ではない):
  1. 全 12 候補のうち大多数の候補固有阻害 Fact は上流 Service Design / Screen Requirements の Open Issue (種別 1) を含む (§6)。
  2. 上流 Open Issue の解決タスク (R-C) は、規則 §12 の解決経路を起票する前に、解決単位が未定 (§21②) であると起票単位を確定できない。
  3. 解決単位の判断は、後続タスクの影響度判定 (Q5) や再評価トリガー (Q4) の検討にも先立つ土台であり、依存グラフ上で最も広い範囲を解く前提となる。
- **前提条件**: Task 009-7 (本計画) が Repository に存在すること (Q1 の質問候補と導出元・反映先が記録済み)。回答は Repository 内の追跡可能な直接証拠として記録すること。
- **必要な判断主体**: Web部責任者 (規則 §12・§21②・§8)。
- **想定する変更レイヤー**: Governance / プロセス上の判断の記録 (owner-decisions.md 等、記録先は Web部責任者が定める)。本推薦自体は Design System 本体・上流成果物を変更しない。
- **対象外**: 上流 Open Issue の内容そのものの解決、候補採否・改定要否・改訂着手、placeholder/実査待ちの確認方法 (Q2)・個別確認主体 (Q3)・トリガー扱い (Q4)・影響度 (Q5) の回答 (いずれも本推薦の判断内容ではなく、別途取得する)。
- **完了しても Design System 改定を開始できるとは限らない**: Q1 の判断が得られても、各上流 Open Issue の内容解決 (R-C)・provenance/参照切れ確認 (R-D)・実査 (R-E)・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。本推薦は候補採否・優先順位・改訂着手を先回りしない。判断内容そのものは本計画で補完しない。

> **注記 (Task 009-8, 2026-07-21)**: 本 §9 が Task 009-7 時点で推薦した Q1「上流 Open Issue の解決単位」の Web部責任者判断は取得済みである (回答「論点別」、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §7)。その回答に基づく論点別後続タスク候補への展開と、Task 009-8 後の次工程推薦は §8A に記録した。本 §9 は Task 009-7 時点の推薦記録として保持する。

## 10. Completion Conditions

本計画の完了条件を次のとおりとする (達成の判定・確定は本文書では行わない)。

- 全 12 候補と残る阻害 Fact の対応が追跡可能である (§6)。
- 共通阻害 Fact (Task 009-6 で規則の定義範囲において解消) と候補固有阻害 Fact (残存) が区別されている (§5・§6)。
- 各 Fact に必要な証拠・判断・既存責任経路が記録されている (§6・§7)。
- 個別確認主体など未定事項を未定のまま保持している (§5 種別 6・§8 Q3)。
- 後続作業の依存関係が確認できる (§7)。
- 最初の後続作業または最初に必要なオーナー判断が 1 件推薦されている (§9)。
- 候補採否・改定要否・継続保留・改訂着手を決定していない (§4・§12)。
- Design System 本体と上流成果物を変更していない (§4・§12)。

## 11. Downstream Impact

- **Assets** ([../assets/README.md](../assets/README.md)) — `Not started`。本計画の対象外。
- **Implementation** — Repository 管理対象外。本計画は静的な整理であり、実装検証・実査の実施・Design System の改定ではない。DS から実装画面・URL・route を導出しない。各 Screen Requirement の Downstream Impact に列挙された Component 例を採用決定と解釈しない。

## 12. Does Not Authorize / Does Not Decide

- 本文書は改訂候補の採用・却下、Design System の改定要否・非改定・継続保留、改訂着手を決定・承認しない。
- Design System 本体 4 資産・token・Component・値・version を変更しない。Service Design・Screen Requirements・Assets・Governance 規則・承認ログを変更しない。
- 上流 Open Issue・provenance・参照切れ・placeholder・実査待ちを推測で解消しない。個別確認主体・担当者・期限・工数を推測しない。
- 優先順位・重要度・severity・数値スコア・合否点を導入しない。新しい恒久 Decision ID・UX Decision・正式 Status・Phase・Gate を追加しない。
- `現時点では開始できない` を却下・不要・継続保留へ変換しない。規則上の責任経路が存在することを論点の解決済みと解釈しない。placeholder / 実査待ちの個別確認主体を定義済みとしない。
- §8 の質問候補への回答を補完しない。§9 の推薦は判断内容そのものを補完しない。
- GitHub の approval・merge を設計承認と同一視しない。Wiki (影響度判定ログ等) を正本として扱わない。
- Travel 固有の本計画を他サービス (rental-car / inbound) へ適用しない。

## 13. Open Issues

以下は未決である。解決策は推測して記載しない。

- §8 Q1〜Q5 の Web部責任者判断 (解決単位・確認方法・個別確認主体・再評価トリガー扱い・各タスク影響度)。
- 各候補の候補固有阻害 Fact (上流 Open Issue の内容・provenance 未確認・参照切れ・placeholder・実査待ちの実値) の解決 (§6)。
- 候補採否・改定要否・継続保留・改訂着手・設計承認 (規則 §9。本計画外)。
- 正式な計画 ID・分類体系・ファイル名の確定 (本ファイル名 `alignment-blocking-facts-resolution-plan.md` は暫定)。

## 14. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-21 | Initial resolution plan (Task 009-7): Task 009-6 の Work Order 6 再評価 (snapshot `e0880d8`) が「現時点では開始できない」とした全 12 候補側面の候補固有阻害 Fact を、8 種別へ分類 (§5)、全 12 候補との対応表 (§6)、Review / Approval Rules 上の解決経路と依存関係 (§7、R-A〜R-H)、Web部責任者へ確認が必要な事項 (§8、Q1〜Q5)、最初に必要なオーナー判断 1 件 (§9、上流 Open Issue の解決単位) として整理。共通阻害 Fact (規則の定義範囲で解消) と候補固有阻害 Fact (残存)・種別 6〜8 の横断残余を区別。個別確認主体は未定のまま保持。候補採否・改定要否・継続保留・改訂着手・設計承認は決定・実施していない。Task 009-6 成果物・元 Work Order 6・Design System 本体 4 資産・token・Component・JSON・version・Service Design・Screen Requirements・Governance 規則・owner-decisions.md は不変 | Draft |
| 2026-07-21 | Q1 回答反映 (Task 009-8): Q1「上流 Open Issue の解決単位」の Web部責任者判断「論点別」を取得 (正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §7)。§8 Q1 行を回答済みへ更新し、§8A を追加して論点別後続タスク候補 9 件 (T1〜T9) へ展開 (各: 対象上流成果物・論点／対応する DS 候補側面／必要な直接証拠／完了条件／決定・承認しない事項)、全 12 候補側面との対応を網羅確認 (§6.2 は provenance トラック・各候補の非上流残余は R-D/R-E トラックと明記)、未回答の Q2〜Q5 を保持、Task 009-8 後の次工程 (どの論点から着手するかの Web部責任者判断) を推薦。上流 Open Issue は未解決・後続 Issue は未作成・Task 009-6 の全 12 候補「現時点では開始できない」は不変。候補採否・改定要否・継続保留・改訂着手・設計承認は決定・実施していない。§9 は Task 009-7 時点の推薦記録として保持。Design System 本体・元 Work Order 6・Task 009-6 成果物は不変 | Draft |
| 2026-07-21 | 初回着手論点の回答反映 (Task 009-9): §8A.5 が推薦した「どの論点から着手するか」の Web部責任者判断「どれからでも構わない」(特定の 1 件に限定せず T1〜T9 のいずれからでも着手してよい) を取得 (正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §8)。§8A.5 に取得済み注記を追記 (推薦記録は保持) し、§8B を追加して回答・正本参照・提示した T1〜T9・選択された論点と対応 (§8A.2/§8A.3 の対応不変)・後続タスクに必要な直接証拠/影響度判定 (Q5)/残る阻害 Fact・未回答の Q2〜Q5・Task 009-9 後の次工程 (T1〜T9 のうち 1 論点の上流 Open Issue 解決タスク = Task 009-10、論点は着手時特定・独自選定しない) を記録。選択されなかった論点を却下・不要・継続保留とせず、独自に論点を選定していない。上流 Open Issue は未解決・後続 Issue は未作成・Task 009-6 の全 12 候補「現時点では開始できない」・§7「解決単位＝論点別」は不変。候補採否・改定要否・継続保留・改訂着手・設計承認は決定・実施していない。§8A の履歴・Task 009-7/009-8 の snapshot は改変せず保持。Design System 本体・元 Work Order 6・Task 009-6 成果物は不変 | Draft |
| 2026-07-21 | T1 の結果反映 (Task 009-10): owner-decisions.md §8「どれからでも構わない」を根拠に一覧先頭 T1 を機械的に選択 (優先順位判断でない) し、Global Navigation・History and Recovery の上流 Open Issue を扱った。Web部責任者との一問一答 (影響度=高／Global Nav 現行維持=はい／History=いいえ〈案件次第〉) を経て、**Global Navigation の対象領域・History and Recovery の保持方式は Service Design 層で固定する必要のない事項**と整理 (案件ごと・実装レベル、上流仕様として確定しないのが適切)。§8C を追加して着手根拠・影響度・回答・整理・上流成果物の扱い (`navigation.md`・Screen Requirements は変更しない)・T1 完了条件の評価・§6.1 対応 (Current Judgment「現時点では開始できない」不変)・残る未確認事項・T2〜T9 未解決・Q2〜Q4 未回答・Q5 は T1 のみ回答済み・次工程 (T2 を機械的に選択・Task 009-11) を記録。機能・コンテンツ変更可否・「案件次第」を横断ルール化せず、案件判断を Service Design 正本へ書かない。上流成果物・Task 009-6 成果物・元 Work Order 6・§8A/§8B 履歴・Task 009-7/009-8 snapshot・owner-decisions §1〜§8・Review/Approval Rules 本文・Design System 本体 4 資産・token・Component・JSON・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない | Draft |
| 2026-07-21 | T1 完了条件の整合補正 (Task 009-10-F1): PR #79 補足コメント (issuecomment-5033633200) の指摘 — §8A.2 の T1 完了条件 (上流成果物へ記録) と §8C.3 の T1 完了宣言 (トラッキング文書への記録で充足) が字義上食い違い、完了判定主体も未明記 — に対応。Web部責任者の判断により、「例外扱いとして完了と判定する」枠組みは誤りで、正しくは「Design System を含むアプリケーション仕様の変更は案件次第ゆえ本工程では定義化しない」(この立場は全域に及ぶ一般的な理由・T1 限定の例外ではない) と確認。追記ではなく、§8C.3/§8C.5 から「T1 完了」宣言・完了条件の充足評価・「例外」という枠組みを**削除**し、事実 (本工程では定義化しない・上流成果物は変更しない) のみ残す形で不整合を解消。§8C.3 見出しを「上流成果物の扱い」に変更し、§8A.2 との関係を一文で明記 (§8A.2 の文言は上流で定義化する場合を想定・定義化しない本件には字義どおり当てはまらない)。完了宣言を置かないため完了判定主体の記載も不要。§8A.2 は Task 009-8 時点の記述として変更しない。この整理を T2〜T9・他サービスへ一般化せず codified rule 化しない。navigation.md・Screen Requirements・owner-decisions §1〜§8・Review/Approval Rules 本文・Task 009-7〜009-9 の snapshot/履歴・Design System 本体 4 資産・Task 009-6 再評価成果物は不変。影響度=高 (Web部責任者、本件として明示取得) | Draft |
| 2026-07-22 | T2 状態論点のスコープ選別・再分類 (Task 009-11): 旧「T2 状態モデルの業務定義」を指示者判断で **「T2 状態論点のスコープ選別・再分類」** へ再定義。T2 に集約された状態論点を 6 観点へ分解し 7 区分へ個別分類 (§8D 新設)。直接証拠に基づき、Pending Confirmation=既存原則で充足 (cta §6)、空結果・在庫切れ=発生条件は実行時・実装で Repository 対象外/状態伝達は既存原則 (CTP-006/007・SDP-005/006・Status Model) で充足/画面別扱いは SCR-004 §16 Open Issue・状態割当は判定保留、予約業務状態=現行 3 State Model 責務外かつ Booking 系 SR (SCR-006〜012 未作成)・業務/製品仕様側で本レイヤー対象外、Error / Interrupted=複合状態名のまま分割せず SCR-014 へ追加しない、と整理。3 State Model の責務・非同一視は現行正本 (navigation §6・content §7・cta §6) に既記載ゆえ新規業務定義でない。§6.3 の Remaining Blocking Fact を本粒度へ精密化 (§6.3 の Current Judgment「現時点では開始できない」は不変)。§8C.5 に着手済み注記。状態名・状態遷移・予約フロー・空結果/在庫切れ挙動を創作せず、業務仕様の解決・完了・§6.3 阻害 Fact の全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-22、本件明示取得、PR #83 carve-out 不適用)。遡及は T2 と直接出所に限定し T3〜T9・他候補・他サービスへ一般化しない。§8A.2 T2 (Task 009-8 時点) の記述・完了条件・Work Order 2〜5・Task 009-6〜009-10-F1 の snapshot/履歴・owner-decisions §1〜§9・Review/Approval Rules 本文・navigation.md/content-principles.md/cta-principles.md/screen-matrix.md・作成済み Screen Requirements・Design System 本体 4 資産・token・Component・JSON・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=T3 を機械的推薦 (§8D.6) | Draft |
| 2026-07-22 | T3 IA論点のスコープ選別・再分類 (Task 009-12): 旧「T3 IA Object の業務モデル」を指示者判断で **「T3 IA 論点のスコープ選別・再分類」** へ再定義 (T3 固有の根拠 = information-architecture.md が IA は概念モデル・画面/API/DB を定義しない・具体業務モデルに踏み込まないと明記し 12 Object は既に §5〜§7 で Draft 定義済み。T2 の自動適用ではない)。T3 の論点を 10 観点へ分解し 8 区分へ個別分類 (§8E 新設)。直接証拠に基づき、12 Object の定義・責務・概念関係=既存 Draft で明示 (IA §5/§6/§7)、正式業務関係・料金/在庫/販売・Destination 階層・Policy 個別規則・Review 提供元/信頼性・User 会員/認証・Booking 業務構造/状態/決済=事業・商品・業務仕様 (IA 各 Does Not Decide・§11)、API/DB/外部対応=Repository 対象外 (IA §8/§9)、12 Object 正式承認・正式用語・IA Object ID・brand-content.md 正本=Governance 課題、IA Object/Content Category と DS 表現語彙の対応 (C-10/X-06)=DS 内部整合課題 (T3 再分類で自動解決しない)、SCR-005/SCR-006 境界=Screen Requirements 課題 (SCR-006〜012 未作成) と整理。§6.5 の Remaining Blocking Fact を本粒度へ精密化 (§6.5 の Current Judgment「現時点では開始できない」は不変)。§8D.6 に着手済み注記。IA Object・業務モデル・予約構造・会員分類・料金/在庫モデルを推測で新規設計せず、12 Object の正式承認・IA §11 全解決・SCR 境界確定・§6.5 全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-22、本件明示取得、PR #83 carve-out 不適用)。遡及は T3 と直接出所に限定し T2・T4〜T9・他サービスへ一般化しない。§8A.2 T3 (Task 009-8 時点) の記述・Work Order 2〜5・Task 009-6〜009-11 の snapshot/履歴・information-architecture.md/service-design README/screen-matrix.md・作成済み Screen Requirements・owner-decisions §1〜§9・Review/Approval Rules 本文・Design System 本体 4 資産・token・Component・JSON・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=T4 を機械的推薦 (§8E.6) | Draft |
