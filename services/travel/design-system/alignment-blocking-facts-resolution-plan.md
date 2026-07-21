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
- **Remaining Blocking Fact**: 状態の業務定義 (Pending Confirmation・空結果/在庫切れ挙動・予約状態) が上流 Open Issue。ボタン状態 follow-up #4 の実査待ち、motion の placeholder。個別確認主体は未定。
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
- **Remaining Blocking Fact**: IA Object の業務モデル (内容・関係・業務仕様) が information-architecture.md §11 Open Issue、SCR-005/SCR-006 境界も未定義。Content 文言正本 `brand-content.md` の参照切れ。
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
| Q1 | 上流 Open Issue を全体共通・成果物別・論点別のどの単位で扱うか | 規則 §12・§21②、owner-decisions.md §4「上流 Open Issue の解決単位」残 Open Issue | 該当する後続解決タスクの起票単位。本計画は反映せず、後続タスクの計画/Issue が参照 |
| Q2 | placeholder / 実査待ちの確認方法 (検査方法・合格基準) | 規則 §14、owner-decisions.md §4「placeholder / 実査待ちの確認主体」 | placeholder / 実査待ち確認の後続タスク手順。確認方法の記録先は Web部責任者が定める |
| Q3 | 個別の placeholder / 実査待ちについて誰が確認するか (個別確認主体) | 規則 §14・§21③ (確認ルール制定まで未定) | 各 placeholder / 実査待ち項目の担当。本計画は未定のまま保持 |
| Q4 | 上流 Open Issue・provenance 未確認を再評価の必須トリガーとするか | 規則 §18・§21④ | Work Order 6 相当の再評価 (R-H) の起動条件 |
| Q5 | 各後続タスク (R-C/R-D/R-E 等) の影響度判定 (高／低) | 規則 §8 (判定主体=Web部責任者の都度判断) | 各後続タスクの必要レビュー主体 (§10・§11・§12・§13) と Wiki 影響度判定ログ (非正本) |

- Q1〜Q5 はいずれも Review / Approval Rules・owner-decisions.md §4 が「承認後も残る Open Issue」として明示した事項から導出したものであり、本計画が新設した質問ではない。
- 回答は Repository 内の追跡可能な直接証拠として取得・記録する必要がある (規則 §16 の承認ログ・§8 の Wiki 影響度判定ログ等、各事項の性質に応じた記録先)。本計画は回答を補完しない。

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
