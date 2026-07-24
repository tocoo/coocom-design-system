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
- **Remaining Blocking Fact**: 問い合わせ手段・処理フロー・サポート対象範囲が SCR-013 §16 の上流 Open Issue。ボタン状態 follow-up #4 の実査待ち。個別確認主体は未定。〔Task 009-16 で精密化 (§8I)〕この一括表現を次の粒度へ改める — (i) Recovery Action の責務 (CTA-TYPE-004・CTA-006・SDP-006・NVP-004・SCR-013 §9) は既存 Draft で明示、(ii) サポート対象範囲・FAQ 要否/分類/構成・問い合わせ手段/チャネル・SLA/運用体制/担当/エスカレーション・問題種別ごとの処理フローは事業・商品・業務仕様 (SCR-013 §13/§16)、(iii) 再試行/修正/戻る/問い合わせの具体割当・具体文言は Content・State・CTA 課題 (CTP-007・SCR-013 §9)、戻り先・回復手段の具体条件は Navigation 課題 (SCR-013 §8・NAV-005/NVP-004)、(iv) Recovery Action と Button/Component/variant の対応は DS 内部整合課題で T7 再分類だけでは自動解決しない、(v) Button state follow-up #4 は実査/provenance トラック (R-E・Q2/Q3) として未解決保持、(vi) Accordion/フォーム/チャット/モーダル等の UI・モバイル支援導線は UI・Implementation 下流課題、(vii) URL/route/画面遷移/API/DB/認証/処理は Repository 全体の対象外。詳細は §8I。
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
- **Remaining Blocking Fact**: 保存期間・Undo・エラー処理が上流 Does Not Decide。Input 状態一式 follow-up #2 の実査待ち。drawer 統一 TVL-0007 の provenance 未確認。個別確認主体は未定。〔Task 009-16 で精密化 (§8I)〕この一括表現を次の粒度へ改める — (i) 可逆性・回復可能性の原則と可逆/不可逆区別 (SDP-006・CTA-006・NVP-004・Commitment Level Model の Reversible/High Commitment/Destructive) は既存 Draft で明示、(ii) 保存期間・キャンセル可否・Undo 要否・取消期限・High Commitment/Destructive の業務区分は事業・商品・業務仕様 (SDP-006・CTA-006 Does Not Decide)、(iii) Undo 実装・エラー処理仕様・状態遷移・ブラウザバック/履歴保存/セッション管理は Repository 全体の対象外、(iv) Input 状態一式 follow-up #2・TVL-0007 provenance は実査/provenance トラック (R-D/R-E・Q2〜Q4) として未解決保持、(v) 確認ダイアログの UI は UI・Implementation 下流課題、(vi) NAV-005 の保持方式は T1 論点であり本工程で再判断しない (接点と境界のみ記録)。詳細は §8I。
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
- **Remaining Blocking Fact**: 適用規格・達成レベルの内容が上流未定義 (design.md §2 は「WCAG 2.2 AA を最低ライン」と記述するが適用規格・達成レベルは未確定)。画像欠落 fallback (SCR-014) の実査待ち。個別確認主体は未定。JSON `$note` がコントラスト未達可能性を自認。〔Task 009-18 で精密化 (§8K)〕この一括表現を次の粒度へ改める — (i) SDP-007・NVP-008・CTP-008・CTA-009 の理解可能性・操作可能性・非視覚依存・キーボード・支援技術・異なる画面サイズ・後工程限定にしない責務は既存 Draft で明示、(ii) 作成済み 7 SCR (SCR-001〜005・013・014) §11 Accessibility Requirements は画面候補ごとの差異を保って明示 (SCR-006〜012 未作成)、(iii) 具体的な規格・達成レベル・実装方式・Component 仕様・focus 実装・HTML 属性・画像/地図仕様は Service Design / Screen Requirements の Does Not Decide、(iv) design.md §2「WCAG 2.2 AA を最低ライン」記述・要求仕様 R9・`color.focus.ring`・text/brand コントラスト・Input error 非色依存・semantic color token・`bound` は既存 Design System に存在、(v) 正式な適用規格・達成レベル・適用範囲・対象画面/Component・例外・Success Criteria・達成基準値・適合判定・適合宣言・検証方法/主体/時点・正本/正式命名/確定主体・Acceptance Criteria は規格・Governance 課題、(vi) 既存値と上流責務の対応・design.md/JSON/components.md 間整合は DS 内部整合課題、(vii) HTML/ARIA・name/role/state・focus 順序・live region・zoom/reflow・target size・responsive UI・motion/reduced motion・skip link/landmark・代替テキスト・画像/地図/アイコン仕様は UI・Implementation 下流、(viii) 実装 Repository・API/DB/認証等の業務実装は Repository 全体の対象外、(ix) 現行画面・keyboard・支援技術・画像 fallback・contrast の実査は実査・検証トラック (R-E)、(x) コントラスト未達可能性の `$note` 自認・Button/Input の hover/active/disabled state (follow-up #4)・画像欠落 fallback は既存 placeholder・実査待ち、(xi) font size/line-height 等 T8 の論点および T4〜T7 の論点は他 Task 境界 (再判断しない)、(xii) 判定保留は該当なし。詳細は §8K。
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
- **Remaining Blocking Fact**: 各 SCR で主要行動が上流未定義。ボタン状態 follow-up #4 の実査待ち。Button variant 語彙 GOV-0002 の provenance 未確認。個別確認主体は未定。〔Task 009-15 で精密化 (§8H)〕この一括表現を次の粒度へ改める — (i) CTA-001〜010・5 つの CTA 分類・Commitment Level Model・CTA State Model・Navigation と CTA の責務境界・画面候補ごとの CTA Consideration・作成済み各 SCR の CTA Requirements・情報確認と選択/確約の区別責務は cta-principles.md §3〜§8・screen-matrix.md §5・各 SCR §4/§6/§9・UXDR-TRAVEL-003 に既に Draft で存在 (既存 Draft で明示)、(ii) 画面別の具体的な主要行動・主要/補助行動の優先関係は各 SCR §9/§16 Open Issue・cta §11 の Screen Requirements 課題、(iii) 会員登録・ログイン誘導・予約/決済/取消/同意/法務表現・Destructive/High-impact の業務行動・確約レベルは事業・商品・業務仕様 (cta §11・CTA-003/004/005・SCR-006〜012 未作成)、(iv) CTA 文言・ラベル・状態伝達・販促圧力の区別は Content・State・CTA 課題で既存原則 (CTA-001/007/008/010・CTA State Model §6) により責務は充足し具体文言/ライティング規則を確定せず新 State を追加せず `Error / Interrupted` を分割しない、(v) CTA 数/表示順/視覚的優先順位・モバイル/sticky/固定配置・色・サイズは UI・Implementation 下流課題、(vi) Button/SearchForm との対応・Primary/Secondary と Button variant の対応・token は DS 内部整合課題で T6 再分類だけでは自動解決しない、(vii) GOV-0002 provenance・Button state follow-up #4・state/サイズ段階の実測は実査/provenance トラック (R-D/R-E・Q2/Q3) として未解決保持 (§6.2 を §6.8 へ統合しない)、(viii) URL/route/画面遷移/API/DB/処理/認証実装は Repository 全体の対象外、(ix) SCR-006〜012 未作成は Screen Requirements 課題 (作成・推測しない)、(x) 正式命名・Screen Requirement ID・Acceptance Criteria 確定主体は Governance 課題。詳細は §8H。
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
- **Remaining Blocking Fact**: 入力項目・必須条件・バリデーション・条件保持方式が SCR-003 §16 の上流 Open Issue。Input 状態一式 follow-up #2 の実査待ち。GOV-0002 provenance 未確認。個別確認主体は未定。〔Task 009-13 で精密化 (§8F)〕この一括表現を次の粒度へ改める — (i) Search Criteria の指定・確認・変更・検索前確認・文脈保持・回復・状態識別の責務は information-architecture.md §5 (IA-OBJ-002/001/011)・navigation.md §6/§7 (NAV-004/005)・accommodation-search.md §6/§8 に既に Draft で存在 (既存 Draft で明示)、(ii) 具体的入力項目・必須/任意・初期値・入力形式・選択肢・項目間依存・検索成立条件・Destination 指定方式・会員差分は事業・商品・業務仕様 (SCR-003 §16・§13 Does Not Decide)、(iii) 検索ロジック・API・DB・検索エンジン・セッション・URL・条件保持の実装方式は Repository 全体の対象外 (SCR-003 §13・navigation.md §7)、(iv) 具体的フォーム・Widget・モーダル/ドロワー・モバイル UI は UI・Implementation 下流課題、(v) バリデーションは業務有効条件/状態伝達/エラー文言/Component state/実装検証へ分解し `Error / Interrupted` を分割せず新規 Navigation State を追加しない (Content・State・CTA 課題)、(vi) Input 状態一式 follow-up #2・GOV-0002 provenance・確認方法・個別確認主体は実査/provenance トラック (R-D/R-E・Q2〜Q4) として未解決保持、(vii) DS Input/SearchForm との対応は DS 内部整合課題で T4 再分類だけでは自動解決しない。詳細は §8F。
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
- **Remaining Blocking Fact**: 表示項目・表示順・比較成立基準・料金構造・Review 提供元が SCR-004/SCR-005 §16・IA §11 の上流 Open Issue。Card 実 px/8 スロット・星実寸・「円」weight の実査待ち。`radius.card`・`shadow` の placeholder。個別確認主体は未定。〔Task 009-14 で精密化 (§8G)〕この一括表現を次の粒度へ改める — (i) Accommodation を識別・比較・評価する責務・SCR-004 の候補確認/比較・SCR-005 の施設確認/評価の責務は information-architecture.md §5 (IA-OBJ-003)・§6/§7・search-results.md §2/§4/§6・accommodation-detail.md §2/§4/§6・screen-matrix.md §5 に既に Draft で存在 (既存 Draft で明示)、(ii) 具体的属性・表示項目・表示範囲/単位/順序/情報密度・比較成立基準・並び替え/絞り込み/ランキング/掲載順の基準・Availability 状態/粒度/表示基準・Price 構造/対象/表示単位/税/手数料/割引/合計・会員差分/販売条件・Review 提供元/評価対象/信頼性/尺度/集計・Policy 分類/表示基準は事業・商品・業務仕様 (IA-OBJ-003/006/007/008/009 の Does Not Decide/Open Issue・SCR-004/005 §16。うち具体的属性・表示項目・Price は §13 も、Availability・Review・Policy は §16 のみ = §8G.4 の直接証拠列に一致)、(iii) 料金計算・API・DB・在庫処理・Review 取得/集計・URL/route/キャッシュ/外部サービスは Repository 全体の対象外 (IA §8/§9・SCR-004/005 §13/§15)、(iv) 事実/条件/販促の区別・情報の更新時点/不確実性/変動可能性・空結果/在庫切れ/料金変更との関係は Content・State・CTA 課題で既存原則 (CTP-004/006/010・SDP-005) により充足し `Error / Interrupted` を分割せず新規 State を追加せず Task 009-11 の状態再分類を保持、(v) SCR-004↔SCR-005 接続・SCR-005↔SCR-006 責務境界・画面間受け渡し文脈は Screen Requirements 課題で具体データ/遷移は対象外・SCR-006 を作成/推測しない、(vi) モバイル比較/情報構成の具体 UI は UI・Implementation 下流課題、(vii) Card/PriceTag/ReviewStars との対応・Card の一覧/詳細用途差は DS 内部整合課題で T5 再分類だけでは自動解決しない、(viii) Card 実 px/8 スロット・`radius.card`/`shadow`・ReviewStars 星実寸・PriceTag「円」weight は実査/placeholder トラック (R-E・Q2/Q3) として未解決保持、(ix) 正式命名・Screen Requirement ID・Acceptance Criteria 確定主体は Governance 課題。詳細は §8G。
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
- **Remaining Blocking Fact**: タイポグラフィの具体規格・文字数制限が CTP-008 Does Not Decide の範囲であり、上流で内容が確定していない。主体の定義は内容の確定を意味しない。〔Task 009-17 で精密化 (§8J)〕この阻害 Fact を次の粒度へ改める — (i) CTP-008 の理解可能性・構造・簡潔さ・非視覚依存の責務 (CTP-008 Decision/Application) と SDP-007 は既存 Draft で明示、(ii) root 16px/rem 基準・2 書体・font family/weight・size scale/line-height scale・用途別 `font.body/heading/display/price`・bound 値は既存 Design System に存在 (design.md §3・semantic.travel.json)、(iii) 具体的タイポグラフィ・文字数制限・アクセシビリティ規格・Component 仕様は CTP-008 Does Not Decide (不足・欠陥と即断しない)、(iv) 具体的文字数/推奨文章量/コピー/ブランドトーン/SEO・法務文言は Content・Editorial 課題、行数/行長/改行/禁則/truncation/line-clamp/overflow/responsive/PC・SP 別値/Component 内表示は UI・Implementation 下流、CSS/HTML markup/フォント配信/API・DB・CMS 文字数/パフォーマンス/多言語は Repository 対象外、(v) 画面別情報構造・見出し階層は Screen Requirements 課題 (SCR-006〜012 未作成)、(vi) 上流責務と既存 token の正式対応・semantic role/Component 利用は DS 内部整合課題、(vii) 具体的アクセシビリティ適用規格・達成レベルは T9 論点、(viii) 正式規格/命名/確定主体/Acceptance Criteria は Governance 課題 (未整備)。既存 bound token の存在を上流承認へ昇格せず・値を変更しない。価格表示タイポは T5 論点、支援/Policy 本文/トーンは T7 論点で再判断しない。詳細は §8J。
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
- **Remaining Blocking Fact**: サポート対象範囲・FAQ 構成・問い合わせ手段が SCR-013 §16 の上流 Open Issue。文言正本 `brand-content.md` の参照切れ。Accordion 等は未着手 (成果物不在)。〔Task 009-16 で精密化 (§8I)〕この一括表現を次の粒度へ改める — (i) SCR-013 の支援・問題解決・条件確認の責務 (SCR-013 §4/§6/§7/§9・CTP-003/006/007/010) は既存 Draft で明示、(ii) サポート対象範囲・FAQ 要否/分類/構成・問い合わせ手段/チャネル・SLA/運用体制・Policy 分類/情報源・認証前後差は事業・商品・業務仕様 (SCR-013 §13/§16・IA-OBJ-008 Open Issue)、(iii) FAQ 文言・問い合わせ案内・法務文言・ブランドトーンは Content・State・CTA 課題で具体文言/ライティング規則を確定せず、(iv) Accordion/フォーム/チャット/モーダル等の UI は UI・Implementation 下流課題 (未着手 Component を必要 Component・改訂候補へ変換しない)、(v) `brand-content.md` 参照切れ・正式命名・Screen Requirement ID・Acceptance Criteria 確定主体は Governance 課題 (参照切れの正本作成/有効性確認は規則 §13、参照切れ文書の想定内容を採用根拠にしない)。詳細は §8I。
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

> **注記 (Task 009-13, 2026-07-22)**: 本 §8E.6 が推薦した次工程 (T4) は Task 009-13 で着手した。ただし Task 009-13 は指示者判断により「T4 入力・検索仕様」から **「T4 入力・検索論点のスコープ選別・再分類」** へ再定義され、入力・検索仕様を一括新規定義せず、T4 に集約された論点の現在位置を選別・記録する工程となった。結果は §8F。本 §8E.6 は Task 009-12 時点の推薦記録として保持する。

## 8F. T4 の結果 (Task 009-13): 入力・検索論点のスコープ選別・再分類

### 8F.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T4 入力・検索仕様」ではなく **「T4 入力・検索論点のスコープ選別・再分類」** とする。入力項目・必須条件・検索成立条件・バリデーション・条件保持・会員差分・検索ロジック等を推測で新規設計せず、T4 に集約された論点の現在位置を選別・記録する。T4 固有の根拠 = accommodation-search.md が既に「Search Criteria の指定・確認・変更／検索前の条件確認／条件変更時の文脈保持／エラー・中断時の回復」の責務 (§6・§8) と「入力項目・必須条件・バリデーション・検索ロジック等の未確定事項」(§13・§16)・「UI・API・DB・URL 等の対象外」(§13・§15) を区別していること。これは T2・T3 の結果を自動適用したものではなく、T4 固有の直接証拠に基づく。
- **着手根拠**: §8E.6 が T4 を未着手一覧の次項として機械的に推薦したことによる (owner-decisions.md §8「どれからでも構わない」・一覧上 T3 の次項)。優先順位・重要度判断ではない。
- **影響度**: 高 (Web部責任者判定、2026-07-22、本件として明示取得)。理由 = 阻害 Fact の意味・分類・後続工程・Design System 候補側面 §6.9 との関係に影響し得る実質的変更のため。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8F.2 分類方法

各論点を 21 観点へ分解した (Search Criteria の概念責務／SCR-003 既存責務／具体的入力項目／必須・任意・初期値／入力形式・選択肢・項目間依存／バリデーション条件／検索成立条件・検索ロジック／Destination 指定方法／条件の確認・変更単位／条件保持・復元の責務／保持の方式・期間／エラー種別・文言・回復行動／User・会員制度との関係／SCR-001・SCR-004 接続／画面間受け渡しデータ／モバイル入力・選択方式／URL・route・クエリ／API・DB・検索エンジン・セッション／DS の Input・SearchForm・Button 対応／follow-up #2・GOV-0002／命名・ID・Acceptance Criteria 確定主体)。これらを 10 区分 (既存 Draft で明示 / 事業・商品・業務仕様 / Screen Requirements 課題 / Content・State・CTA 課題 / Governance 課題 / Repository 全体の対象外 / UI・Implementation 下流課題 / DS 内部整合課題 / 実査・provenance トラック / 判定保留) のいずれかへ分類した。

### 8F.3 Search Criteria と SCR-003 の既存状態 (直接証拠に基づく確認)

- information-architecture.md §5 が IA-OBJ-002 Search Criteria (探索意図を条件として保持・Destination を参照・Accommodation を絞り込む)・IA-OBJ-001 Destination・IA-OBJ-011 User を Draft 定義。accommodation-search.md §6 が「Search Criteria を指定・確認・変更できる／検索開始前に現在の条件と行動を理解できる／条件変更時に文脈を不必要に失わせない／中断・誤操作後に戻れる／利用不能・未確定・不正な状態を識別できる」を既に要求として記載。同 §8 が NAV-004/NAV-005 (定義は navigation.md §4、accommodation-search.md §8 は SCR-003 への適用) の責務を記載し、同 §10 が Entry/Exploring/Error / Interrupted を State として記載。
- したがって「入力・検索に関する要求が何も定義されていない」とは扱わない (分類 = 既存 Draft で明示)。同時に、SCR-003 を新規作成せず、既存責務・要求を正式承認済みとみなさず、Search Criteria をフォーム・URL パラメータ・DB entity と同一視せず、SCR-003 を実装上の単一画面と同一視しない。「Draft として存在すること」と「入力・検索仕様が確定していること」を区別する。

### 8F.4 論点別の再分類結果

| 論点 | 主な観点 | 分類結果 | 直接証拠 | §6.9 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| Search Criteria の指定・確認・変更・文脈保持・回復・状態識別の**責務** | (1)(2)(9)(10)(12) | 既存 Draft で明示 | IA §5 (IA-OBJ-002)・navigation.md §4 (NAV-004/NAV-005 の定義)・§6 (Navigation State Model)・§7 (Context Preservation、いずれも適用先)・accommodation-search.md §6/§8/§10 | 残さない (既定義。正式承認は別) |
| 具体的**入力項目・必須/任意・初期値・入力形式・選択肢・項目間依存・検索成立条件・Destination 指定方式** | (3)(4)(5)(7)(8) | 事業・商品・業務仕様 | SCR-003 §16 Open Issue・§13 Does Not Decide・IA-OBJ-001 Does Not Decide | 事業・業務仕様側として整理 (SCR-003 §16 に保持)。推測しない |
| **検索ロジック・API・DB・検索エンジン・セッション・条件保持の実装方式・URL/route/クエリ** | (17)(18)(11) | Repository 全体の対象外 | accommodation-search.md §13 (検索ロジック・検索 API・DB・保存方式)・§15 Implementation・navigation.md §7 (保持方式・期間・セッションは決定しない) | 対象外として整理 |
| **具体的フォーム・Widget・モーダル/ドロワー・検索バー・モバイル入力方式・レイアウト** | (16) | UI・Implementation 下流課題 | accommodation-search.md §13 (フォーム・検索バー等 UI は決定しない)・§11 (モバイルは可能にするが具体 UI 未定) | 下流課題として整理 |
| **バリデーション** (業務有効条件／状態伝達／エラー文言／Component state／実装検証) | (6)(12) | 分解: 業務条件=事業・業務仕様／状態伝達・回復=Content・State・CTA 課題／実装検証=対象外 | accommodation-search.md §7/§10 (状態・回復は責務として存在)・§13 (検証条件・エラー文言は決定しない) | 分解して残す。`Error / Interrupted` を分割せず新規 State を追加しない |
| **条件保持・復元の方式・期間** | (10)(11) | 責務=既存 Draft／方式・期間=事業・法務・セキュリティ判断＋実装 (対象外) | navigation.md §7 (文脈保持責務あり・保持期間/方式/セッションは決定しない)・SCR-003 §16 | 方式・期間は保持 (責務の存在を確定とみなさない) |
| **User・会員差分** (会員種別で条件差／認証前後で差／自動入力／個人情報) | (13) | 事業・会員・認証仕様 | IA-OBJ-011 Does Not Decide・accommodation-search.md §5/§16 (User は Supporting・認証/会員/履歴を取り込まない) | 事業・会員・認証仕様側。SCR-003 へ機能を取り込まない |
| **SCR-001・SCR-004 との接続** (接続責務 vs 具体データ・画面遷移) | (14)(15) | 接続責務=既存 Draft/Screen Requirements 課題／具体データ・遷移=対象外 | accommodation-search.md §2/§16 (接続可能性と具体遷移を混同しない・内部要件を取り込まない) | Screen Requirements 課題 (接続単位は未確定)。空結果は Task 009-11 の再分類を保持し T4 で再判断しない |
| **DS の Input・SearchForm・Button との対応** | (19) | DS 内部整合課題 | WO4 C-02・accommodation-search.md §15 | §6.9 の DS 対応整理として残る (T4 再分類で自動解決しない) |
| **Input 状態一式 follow-up #2・GOV-0002 provenance・確認方法・個別確認主体** | (20) | 実査・provenance トラック (R-D/R-E・Q2〜Q4) | WO4 C-02・owner-decisions.md §3 follow-up #2・§6.9 Direct Source | 未解決のまま保持 (実査せず・provenance を肯定的根拠にしない) |
| **正式命名・Screen Requirement ID・Acceptance Criteria 確定主体** | (21) | Governance 課題 | accommodation-search.md §16・§17・README §7 | Governance 側 (未整備) |

### 8F.5 §6.9・§8A.2 T4・§8E.6 との関係、保持事項

- **§6.9 との関係**: §6.9 の Remaining Blocking Fact を本再分類の粒度へ精密化した (§6.9 に注記)。§6.9 の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。
- **§8A.2 T4 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T4 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8F は現在状態の再分類記録である。
- **§8E.6 との関係**: §8E.6 が推薦した次工程が本 Task で着手されたことを §8E.6 に注記した (推薦記録は保持)。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-12 の snapshot/履歴は監査証跡として変更しない (本 §8F から参照するのみ)。
- **保持事項**: T5〜T9 は未着手・未解決。Q2〜Q4 は未回答。Q5 は T1〜T3・Task 009-4-F1 の既存記録を変更せず T4 の影響度「高」を追加。Input 状態 follow-up #2・その確認方法・個別確認主体・GOV-0002 provenance 未確認・provenance の再評価トリガー扱い・SCR-003 §16 の Open Issues・`brand-content.md` 参照切れ・正式命名規則・Screen Requirement ID の未確定・SCR-006〜012 未作成は保持。Task 009-6 の全 12 候補「現時点では開始できない」は不変。空結果は Task 009-11 の再分類結果を保持し T4 で再判断しない。
- **本 Task の完了の意味**: 「Task 009-13 という再分類作業の完了」であり、「入力・検索仕様の確定」「SCR-003 §16 の全 Open Issues の解決」「検索項目・必須条件・バリデーションの確定」「条件保持方式・期間の確定」「SearchForm・Input 仕様の確定」「§6.9 阻害 Fact の全解消」「Design System 改定開始可能」「Alignment 完了条件充足」のいずれも宣言しない。

### 8F.6 次工程の推薦 (Task 009-13 後)

- **推薦対象**: T5「表示項目・料金・評価仕様」(§8A.2 T5)。未着手一覧の次項として**機械的に選択**したものである。
- **推薦理由**: owner-decisions.md §8「どれからでも構わない」により着手順の制約がなく、一覧上 T4 の次項が T5 であるため。**優先順位・重要度判断ではない**。T4 の結果を T5 へ一般化しない。T5 も着手時に個別のスコープ選別が必要となり得る (先回りして決めない)。
- **前提条件**: 本 §8F の記録が Repository に存在すること。T5 着手前に T5 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T5 の影響度判定 = Web部責任者 (規則 §8)。上流 (表示項目・料金・評価仕様) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T5 の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Screen Requirements (SCR-004/SCR-005)・IA。ただし T5 も対象外・既存 Draft・事業仕様・実査/provenance の選別を要し得る。Design System 本体は変更しない。
- **対象上流成果物・必要な直接証拠**: §8A.2 T5 記載のとおり (SCR-004/SCR-005 §16・IA §11)。
- **完了条件**: T5 の各論点が指定観点へ分解され、直接証拠付きで分類され、元記録との関係が追跡でき、§6.10 の該当 Remaining Blocking Fact が精密化されること (内容は着手時に確定)。
- **対象外**: T1〜T4 の再判断、T5 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答、T6〜T9 の着手順序。
- **Q4・再評価の前後**: Repository 内の依存関係 (§7) 上、上流論点の整理 (R-C) は再評価 (R-H) の前段であり、Q4・Work Order 6 相当の再評価は T5 着手の前提ではない。
- **完了しても Design System 改定を開始できるとは限らない**: T5 の整理が記録されても、他論点・provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

> **注記 (Task 009-14, 2026-07-23)**: 本 §8F.6 が推薦した次工程 (T5) は Task 009-14 で着手した。ただし Task 009-14 は指示者判断により「T5 表示項目・料金・評価仕様」から **「T5 表示・料金・評価論点のスコープ選別・再分類」** へ再定義され、表示・料金・評価仕様を一括新規確定せず、T5 に集約された論点の現在位置を選別・記録する工程となった。結果は §8G。本 §8F.6 は Task 009-13 時点の推薦記録として保持する。

## 8G. T5 の結果 (Task 009-14): 表示・料金・評価論点のスコープ選別・再分類

### 8G.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T5 表示項目・料金・評価仕様」ではなく **「T5 表示・料金・評価論点のスコープ選別・再分類」** とする。宿泊施設一覧・詳細の表示項目・表示順・情報密度・比較基準・料金体系・価格計算・表示単位・Review 提供元・評価方式・Card/PriceTag/ReviewStars の採否・一覧/詳細 UI を推測で新規設計・確定せず、T5 に集約された論点の現在位置を選別・記録する。T5 固有の根拠 = search-results.md (SCR-004)・accommodation-detail.md (SCR-005)・information-architecture.md が既に、Accommodation を識別・比較・評価する責務／Price・Review 等を判断材料として参照する責務 (SCR-004 §4/§5/§6・SCR-005 §4/§5/§6・IA §5/§6) と、具体的な表示項目・表示順・比較基準等の未確定事項・料金構造・Review 提供元等の事業/業務仕様 (SCR-004/005 §16・§13・IA §11)・UI/Component/API/DB 等の対象外 (SCR-004/005 §13/§15・IA §8/§9) を区別し、SCR-004 と SCR-005 で異なる IA Object・責務 (SCR-004 Supporting = Availability/Price/Review/Policy、SCR-005 は Price・Availability を IA Object としない) を持つこと。これは T2・T3・T4 の結果を自動適用したものではなく、T5 固有の直接証拠に基づく。
- **着手根拠**: §8F.6 が T5 を未着手一覧の次項として機械的に推薦したことによる (owner-decisions.md §8「どれからでも構わない」・一覧上 T4 の次項)。優先順位・重要度判断ではない。
- **影響度**: 高 (Web部責任者判定、2026-07-23、本件として明示取得)。理由 = 阻害 Fact の意味・分類・後続工程・Design System 候補側面 §6.10 との関係に影響し得る実質的変更のため。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8G.2 分類方法

各論点を 28 観点へ分解した (Accommodation の識別・比較・評価責務／SCR-004 の候補確認・比較責務／SCR-005 の施設情報確認・評価責務／具体的属性・表示項目／表示範囲・単位・順・情報密度／比較成立基準／並び替え・絞り込み・ランキング・掲載順／Availability の状態・粒度・表示基準・更新時点／Price の構造・対象・表示単位／税・手数料・割引・合計／料金計算・会員差分・販売条件／Review の提供元・評価対象・信頼性／評点尺度・件数・投稿日・集計・表示基準／Policy の分類・適用対象・表示基準／事実・条件・販促の区別／更新時点・不確実性・変動可能性／SCR-004↔SCR-005 接続／SCR-005↔SCR-006 責務境界／画面間受け渡しデータ・文脈／空結果・在庫切れ・料金変更との関係／モバイル比較・情報構成／Card・PriceTag・ReviewStars との対応／Card の一覧用途と詳細用途の差／radius.card・shadow・Card 実 px・8 スロット／ReviewStars 星実寸・PriceTag「円」weight／API・DB・料金計算・在庫・Review 取得処理／URL・route・キャッシュ・外部サービス／正式命名・ID・Acceptance Criteria 確定主体)。これらを 10 区分 (既存 Draft で明示 / 事業・商品・業務仕様 / Screen Requirements 課題 / Content・State・CTA 課題 / Governance 課題 / Repository 全体の対象外 / UI・Implementation 下流課題 / DS 内部整合課題 / 実査・placeholder トラック / 判定保留) へ分類した。1 観点が分類先の異なる構成要素を束ねる場合は要素へ分解して分類する (観点 (11)「料金計算・会員差分・販売条件」は、料金計算 = Repository 全体の対象外、会員差分・販売条件 = 事業・商品・業務仕様、へ分解する)。

### 8G.3 SCR-004・SCR-005・IA の既存状態 (直接証拠に基づく確認)

- information-architecture.md §5 が IA-OBJ-003 Accommodation (識別・比較・評価の中心的情報単位)・IA-OBJ-006 Availability・IA-OBJ-007 Price・IA-OBJ-008 Policy・IA-OBJ-009 Review 等を Draft 定義し、§6/§7 が概念関係 (Stay Plan は Price を持つ/Price で評価される・Review は Accommodation/Stay Plan を評価する等) を Draft で示す。search-results.md (SCR-004) §2/§4/§6 が「Search Criteria に対応する Accommodation 候補を確認・比較し詳細検討へ進む」を既に要求として記載し、§5 が Primary = Search Criteria/Accommodation・Supporting = Availability/Price/Review/Policy を、§10 が Exploring/Evaluating/Error / Interrupted を定義。accommodation-detail.md (SCR-005) §2/§4/§6 が「施設情報と関連情報を確認し評価する」を既に要求として記載し、§5 が Primary = Accommodation・Supporting = Destination/Room/Stay Plan/Review/Policy/Content を定義し、**Price (IA-OBJ-007)・Availability (IA-OBJ-006) を SCR-005 の IA Object としない**ことを明示 (§5・§12・§17)。screen-matrix.md §5 が SCR-004/SCR-005/SCR-006 の責務・IA Objects・States を管理。
- したがって「候補・施設・価格・評価の表示に関する要求が何も定義されていない」とは扱わない (分類 = 既存 Draft で明示)。同時に、SCR-004/SCR-005 を新規作成せず、既存責務・要求を正式承認済みとみなさず、Accommodation を Card・表示項目・DB model と同一視せず、Price・Availability を SCR-005 へ追加せず、PriceTag/ReviewStars の存在を料金構造・評価制度の根拠にしない。「Draft として存在すること」と「表示・料金・評価仕様が確定していること」を区別する。

### 8G.4 論点別の再分類結果

| 論点 | 主な観点 | 分類結果 | 直接証拠 | §6.10 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| Accommodation の識別・比較・評価責務／SCR-004 の候補確認・比較／SCR-005 の施設確認・評価の**責務** | (1)(2)(3) | 既存 Draft で明示 | IA §5 (IA-OBJ-003)・§6/§7・SCR-004 §2/§4/§6・SCR-005 §2/§4/§6・screen-matrix.md §5 | 残さない (既定義。正式承認は別) |
| 具体的**属性・表示項目・表示範囲/単位/順序/情報密度・比較成立基準・並び替え/絞り込み/ランキング/掲載順の基準** | (4)(5)(6)(7) | 事業・商品・業務仕様 (具体 UI 表現・ロジックは UI 下流/対象外) | IA-OBJ-003 Does Not Decide (属性一覧)・SCR-004 §16・§13・SCR-005 §16・§13 | 事業・業務仕様側 (SCR §16 に保持)。IA の Includes 語を正式表示項目に承認しない・推測しない |
| **Availability の状態・粒度・表示基準・更新時点** | (8) | 事業・商品・業務仕様 | IA-OBJ-006 Does Not Decide (リアルタイム性・更新方式)・SCR-004 §16 | 事業・業務仕様側。Availability は SCR-004 Supporting のみ・SCR-005 へ追加しない |
| **Price の構造・対象・表示単位・税/手数料/割引/合計・会員差分・販売条件** | (9)(10)(11 のうち会員差分・販売条件) | 事業・商品・業務仕様 (料金計算は対象外) | IA-OBJ-007 Does Not Decide (料金構造・表示単位)・SCR-004 §16・§13 | 事業・業務仕様側。IA Includes 語を正式料金仕様に承認せず・PriceTag の存在を課金モデルの根拠にしない |
| **料金計算・API・DB・在庫処理・Review 取得/集計・URL/route/キャッシュ/外部サービス** | (11 のうち料金計算)(26)(27) | Repository 全体の対象外 | IA §8/§9 (料金計算・在庫管理・API/DB は含まない)・SCR-004 §13/§15・SCR-005 §13/§15 | 対象外として整理 |
| **Review の提供元・評価対象・信頼性・評点尺度・件数・投稿日・集計・表示基準** | (12)(13) | 事業・商品・業務仕様 | IA-OBJ-009 Open Issue (提供元・評価対象・信頼性)・SCR-004 §16・SCR-005 §16 | 事業・業務仕様側。ReviewStars の存在を 5 段階星評価・評価制度の根拠にしない |
| **Policy の分類・適用対象・表示基準** | (14) | 事業・商品・業務仕様 | IA-OBJ-008 Open Issue (分類)・SCR-004 §7/§16・SCR-005 §7/§16 | 事業・業務仕様側 |
| **事実/条件/販促の区別・情報の更新時点/不確実性/変動可能性・空結果/在庫切れ/料金変更との関係** | (15)(16)(20) | Content・State・CTA 課題 (既存原則で充足・保持) | CTP-004/006/010・SDP-005・SCR-004 §7/§10・SCR-005 §7/§10・Task 009-11 の状態再分類 | 分解して保持。`Error / Interrupted` を分割せず新規 State を追加せず・料金変更を業務状態に創作せず・Task 009-11 を再判断しない |
| **SCR-004↔SCR-005 接続・SCR-005↔SCR-006 責務境界・画面間受け渡し文脈** | (17)(18)(19) | Screen Requirements 課題 (具体データ・遷移は対象外) | SCR-004 §2/§16・SCR-005 §2/§16・screen-matrix.md §9 (境界 Open Issue)・SCR-006 未作成 | Screen Requirements 課題 (境界未確定)。SCR-006 を作成・内容推測せず・内部要件を相互取り込みしない |
| **モバイル比較・情報構成** | (21) | UI・Implementation 下流課題 (「モバイルでも比較・確認・評価可能」の要求は既存 Draft) | SCR-004 §11/§16・SCR-005 §11/§16 | 下流課題として整理 |
| **Card・PriceTag・ReviewStars との対応・Card の一覧/詳細用途差** | (22)(23) | DS 内部整合課題 | WO5 C-03/C-04/C-05・alignment-observations-aggregation.md §15/§16・components.md Card (ResultCard)/PriceTag/ReviewStars | §6.10 の DS 対応整理として残る (T5 再分類で自動解決しない) |
| **Card 実 px・8 スロット・`radius.card`・shadow・ReviewStars 星実寸・PriceTag「円」weight** | (24)(25) | 実査・placeholder トラック (R-E・Q2/Q3) | components.md Card/ReviewStars/PriceTag 未確定事項・WO5 T-05/T-06・§6.10 | 未解決のまま保持 (実査せず・placeholder を改定根拠にしない) |
| **正式命名・Screen Requirement ID・Acceptance Criteria 確定主体** | (28) | Governance 課題 | SCR-004/005 §16・§17・README §7・IA §11 | Governance 側 (未整備) |

- **判定保留**: 本工程では該当なし (28 観点はいずれも直接証拠に基づき上記区分へ分類した)。

### 8G.5 §6.10・§8A.2 T5・§8F.6 との関係、保持事項

- **§6.10 との関係**: §6.10 の Remaining Blocking Fact を本再分類の粒度へ精密化した (§6.10 に注記)。§6.10 の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。
- **§8A.2 T5 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T5 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8G は現在状態の再分類記録である。
- **§8F.6 との関係**: §8F.6 が推薦した次工程が本 Task で着手されたことを §8F.6 に注記した (推薦記録は保持)。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-13-F1 の snapshot/履歴は監査証跡として変更しない (本 §8G から参照するのみ)。
- **保持事項**: T6〜T9 は未着手・未解決。Q2〜Q4 は未回答。Q5 は T1〜T4・Task 009-4-F1 の既存記録を変更せず T5 の影響度「高」を追加。Card 実 px・8 スロット実査待ち・ReviewStars 星実寸実査待ち・PriceTag「円」weight 実査待ち・`radius.card`/`shadow` placeholder・placeholder/実査待ちの確認方法・個別確認主体・SCR-004/SCR-005 §16 Open Issues・IA §11 Open Issues・SCR-006〜012 未作成・正式命名規則・Screen Requirement ID 未確定・`brand-content.md` 参照切れは保持。Task 009-6 の全 12 候補「現時点では開始できない」は不変。空結果・在庫切れ・料金変更は Task 009-11 の状態再分類結果を保持し T5 で再判断しない。一般的なタイポグラフィ具体規格・文字数制限は T8 の論点であり T5 へ取り込まない (ただし PriceTag「円」weight という T5 固有の実査待ちは追跡する)。
- **本 Task の完了の意味**: 「Task 009-14 という再分類作業の完了」であり、「表示・料金・評価仕様の確定」「SCR-004/SCR-005 §16 の全 Open Issues の解決」「料金構造・比較基準・Review 提供元の確定」「SCR-005/SCR-006 境界の確定」「Card・PriceTag・ReviewStars 仕様の確定」「§6.10 阻害 Fact の全解消」「Design System 改定開始可能」「Alignment 完了条件充足」のいずれも宣言しない。

### 8G.6 次工程の推薦 (Task 009-14 後)

- **推薦対象**: T6「主要行動・CTA」(§8A.2 T6)。未着手一覧の次項として**機械的に選択**したものである。
- **推薦理由**: owner-decisions.md §8「どれからでも構わない」により着手順の制約がなく、一覧上 T5 の次項が T6 であるため。**優先順位・重要度判断ではない**。T5 の結果を T6 へ一般化しない。T6 も着手時に個別のスコープ選別が必要となり得る (先回りして決めない)。T5 固有の直接依存 (再分類を確定するために不可欠な直接証拠・オーナー判断) は本工程で新たに特定されておらず、多数の事業判断が未確定であることを理由に一括仕様確定タスクは推薦しない。
- **前提条件**: 本 §8G の記録が Repository に存在すること。T6 着手前に T6 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T6 の影響度判定 = Web部責任者 (規則 §8)。上流 (各 SCR の主要行動・情報確認と選択の区別) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T6 の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Screen Requirements (各 SCR)。ただし T6 も対象外・既存 Draft・事業仕様・実査/provenance の選別を要し得る。Design System 本体は変更しない。
- **対象上流成果物・必要な直接証拠**: §8A.2 T6 記載のとおり (各 SCR §16 の主要行動に関する Open Issue、対応 DS 候補側面 §6.8)。
- **完了条件**: T6 の各論点が指定観点へ分解され、直接証拠付きで分類され、元記録との関係が追跡でき、§6.8 の該当 Remaining Blocking Fact が精密化されること (内容は着手時に確定)。
- **対象外**: T1〜T5 の再判断、T6 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答、T7〜T9 の着手順序。
- **Q4・再評価の前後**: Repository 内の依存関係 (§7) 上、上流論点の整理 (R-C) は再評価 (R-H) の前段であり、Q4・Work Order 6 相当の再評価は T6 着手の前提ではない。
- **完了しても Design System 改定を開始できるとは限らない**: T6 の整理が記録されても、他論点・provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

> **注記 (Task 009-15, 2026-07-23)**: 本 §8G.6 が推薦した次工程 (T6) は Task 009-15 で着手した。ただし Task 009-15 は指示者判断により「T6 主要行動・CTA」から **「T6 主要行動・CTA 論点のスコープ選別・再分類」** へ再定義され、各画面の主要 CTA を一括新規確定せず、T6 に集約された論点の現在位置を選別・記録する工程となった。結果は §8H。本 §8G.6 は Task 009-14 時点の推薦記録として保持する。

## 8H. T6 の結果 (Task 009-15): 主要行動・CTA 論点のスコープ選別・再分類

### 8H.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T6 主要行動・CTA」ではなく **「T6 主要行動・CTA 論点のスコープ選別・再分類」** とする。各画面の主要行動・Primary/Secondary CTA の割当・CTA 文言/数/順序/優先順位・予約/決済/取消/会員登録等の業務行動・CTA の表示位置/色/サイズ/モバイル UI・Button variant の採否・SCR-006〜SCR-012 の作成・予約導線/画面遷移/実装を推測で新規設計・確定せず、T6 に集約された論点の現在位置を選別・記録する。T6 固有の根拠 = cta-principles.md が既に CTA-001〜010 (§3)・5 つの CTA 分類 (§4)・Commitment Level Model (§5)・CTA State Model (§6)・Navigation と CTA の責務境界 (§8)・画面候補ごとの CTA Consideration (§7) を区別し、作成済み Screen Requirements 各 §9 が CTA Requirements を記載し、画面別主要 CTA・確約レベル・ラベル等を Open Issue (cta §11・各 SCR §16) として保持していること。これは T2〜T5 の結果を自動適用したものではなく、T6 固有の直接証拠に基づく。
- **着手根拠**: §8G.6 が T6 を未着手一覧の次項として機械的に推薦したことによる (owner-decisions.md §8「どれからでも構わない」・一覧上 T5 の次項)。優先順位・重要度判断ではない。
- **影響度**: 高 (Web部責任者判定、2026-07-23、本件として明示取得)。理由 = 阻害 Fact の意味・分類・後続工程・Design System 候補側面 §6.8 との関係に影響し得る実質的変更のため。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8H.2 分類方法

各論点を 39 観点へ分解した (CTA Principles の横断責務／CTA-001 Action Clarity／CTA-002 One Clear Primary Action／CTA-003 Commitment-aware Emphasis／CTA-004 Progressive Commitment／CTA-005 Conditions Before Action／CTA-006 Reversible Before Irreversible／CTA-007 Explicit State and Availability／CTA-008 Consistent Meaning／CTA-009 Accessible Activation／CTA-010 No Unsupported Pressure／Primary Task Action／Secondary Task Action／Navigation Action／Recovery Action／Destructive or High-impact Action／Commitment Level Model／CTA State Model／画面候補ごとの User Task・CTA 責務／作成済み各 SCR の CTA Requirements／画面別の具体的な主要行動／主要行動と補助行動の優先関係／情報確認・比較・評価と選択・入力・確約の区別／Navigation と CTA の責務境界／行動の対象・結果・遷移先／CTA 文言・ラベル・コピー／CTA 数・表示順・優先順位／利用可能・利用不能・処理中等の状態／会員登録・ログイン誘導／予約・決済・取消・同意・法務表現／モバイル CTA・sticky 等の具体 UI／Button・SearchForm との対応／Primary・Secondary 等と Button variant の対応／Button state・サイズ・色・配置・token／GOV-0002 の provenance／Button state follow-up #4／SCR-006〜SCR-012 未作成との関係／URL・route・画面遷移・API・DB・処理／正式命名・ID・Acceptance Criteria 確定主体)。これらを 10 区分 (既存 Draft で明示 / 事業・商品・業務仕様 / Screen Requirements 課題 / Content・State・CTA 課題 / Governance 課題 / Repository 全体の対象外 / UI・Implementation 下流課題 / DS 内部整合課題 / 実査・provenance トラック / 判定保留) へ分類した。1 観点が分類先の異なる構成要素を束ねる場合は要素へ分解して分類する (観点 (16) Destructive/High-impact Action は分類責務 = 既存 Draft／業務行動・確約レベル = 事業仕様、観点 (25) 行動の対象・結果・遷移先は具体的対象・結果 = Screen Requirements 課題／遷移先 = 対象外、観点 (34) Button state・サイズ・色・配置・token は state 実測 = 実査トラック／サイズ・色・配置 = UI 下流／token = DS 内部整合、へ分解する)。

### 8H.3 CTA Principles・作成済み Screen Requirements の既存状態 (直接証拠に基づく確認)

- cta-principles.md §3 が CTA-001〜010 を Decision/Rationale/Application/Does Not Decide 付きで Draft 定義し、§4 が 5 つの CTA 分類 (Primary/Secondary/Navigation/Recovery/Destructive or High-impact)、§5 が Commitment Level Model (Informational/Reversible/Conditional/High Commitment/Destructive)、§6 が CTA State Model (Available/Unavailable/Loading/Success/Error/Pending Confirmation)、§7 が 14 画面候補ごとの CTA Consideration、§8 が Navigation と CTA の責務境界を Draft で示す。作成済み Screen Requirements (SCR-001/002/003/004/005/013/014) の各 §9 CTA Requirements が当該 SCR の CTA 責務を上流参照で記載し、いずれも「具体的行動・内容が未定義の場合、主要 CTA を確定しない」(SDP-010) と明記。cta §11・各 SCR §16 が画面別主要 CTA・確約レベル・ラベル・会員登録/ログイン CTA・モバイル CTA・法務同意等を Open Issue として保持。
- したがって「CTA に関する上流要求が何も定義されていない」とは扱わない (分類 = 既存 Draft で明示)。同時に、CTA-001〜010 を新規作成・再定義せず、既存責務・原則を正式承認済みとみなさず、User Task を具体的 CTA 文言へ変換せず、Navigation Action を主要 CTA へ自動昇格せず、Button・`primary` variant・SearchForm の存在を画面別主要 CTA の確定根拠にしない。「Draft として存在すること」と「画面別 CTA 仕様が確定していること」を区別する。

### 8H.4 論点別の再分類結果

| 論点 | 主な観点 | 分類結果 | 直接証拠 | §6.8 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| CTA-001〜010 の**横断責務・原則** | (1)〜(11) | 既存 Draft で明示 | cta-principles.md §3 (CTA-001〜010) | 残さない (既定義。正式承認は別。適用規格 = T9・可逆/回復の詳細 = T7 は取り込まない) |
| 5 つの **CTA 分類・Commitment Level Model・CTA State Model** | (12)〜(15)(16 の分類責務)(17)(18) | 既存 Draft で明示 | cta §4 (CTA-TYPE-001〜005)・§5・§6 | 残さない (既定義。新 CTA Type/State を追加せず・確約レベルの正式業務区分化は事業仕様へ) |
| **画面候補ごとの User Task・CTA 責務／作成済み各 SCR の CTA Requirements／情報確認と選択・確約の区別／Navigation↔CTA 責務境界** | (19)(20)(23)(24) | 既存 Draft で明示 | cta §7/§8・screen-matrix.md §5・各 SCR §4/§6/§9・UXDR-TRAVEL-003 | 残さない (既定義。User Task を具体 CTA 文言化せず・Navigation Action を主要 CTA へ昇格しない) |
| **画面別の具体的な主要行動／主要・補助行動の優先関係／行動の具体的対象・結果** | (21)(22)(25 の具体的対象・結果) | Screen Requirements 課題 | 各 SCR §9・§16 Open Issue (画面別主要 CTA 未確定)・cta §11・SDP-010 | Screen Requirements 課題 (各 SCR §16 で未決)。SCR を実装 1 画面/URL と同一視せず・SCR 間の内部要件を相互取り込みしない |
| **会員登録・ログイン誘導／予約・決済・取消・同意・法務表現／Destructive・High-impact の業務行動・確約レベル** | (16 の業務行動・確約レベル)(29)(30) | 事業・商品・業務仕様 | cta §11 (予約確約レベル・会員登録/ログイン CTA・法務同意)・CTA-003/004/005・SCR-006〜012 未作成 | 事業・業務仕様側 (推測しない)。SCR-006〜012 を作成/推測せず・予約責務を既存 SCR へ移管しない |
| **CTA 文言・ラベル・コピー／利用可能・利用不能・処理中等の状態伝達／販促圧力の区別** | (26)(28) | Content・State・CTA 課題 (既存原則で責務充足・保持) | CTA-001/007/008/010・cta §6 CTA State Model・各 SCR §7/§10/§13 | 分解して保持。CTA State Model と Navigation State・Component state を同一視せず・新 State を追加せず `Error / Interrupted` を分割せず・具体文言/ライティング規則を確定せず・T2 状態論点/T7 回復論点を再判断しない |
| **CTA 数・表示順・視覚的優先順位／モバイル CTA・sticky 等の具体 UI／配置・色・サイズ** | (27)(31)(34 のサイズ・色・配置) | UI・Implementation 下流課題 (「意味・実行可能性を失わせない」要求は既存 Draft) | 各 SCR §11/§13・cta §11 (モバイル固定 CTA) | 下流課題として整理 (sticky/bottom bar/固定配置/PC・SP 順/ワイヤーフレームを決定せず・適用規格は T9) |
| **Button・SearchForm との対応／Primary・Secondary と Button variant の対応／token 対応** | (32)(33)(34 の token) | DS 内部整合課題 | WO5 C-01・components.md Button (variant primary/secondary/ghost/text・GOV-0002)/SearchForm・cta §10 | §6.8 の DS 対応整理として残る (T6 再分類で自動解決しない)。Button の存在→主要 CTA 確定にせず・`primary` variant→画面別 primary 確定にせず・SearchForm 記述→正式検索 CTA へ昇格しない |
| **GOV-0002 の provenance／Button state follow-up #4／Button state・サイズ段階の実測** | (35)(36)(34 の state 実測) | 実査・provenance トラック (R-D/R-E・Q2/Q3) | components.md (follow-up #4・GOV-0002)・§6.2・owner-decisions.md §3 follow-up #4 | 未解決のまま保持 (実査せず・provenance 未確認を採用根拠にしない・§6.2 を §6.8 へ統合しない) |
| **URL・route・画面遷移・API・DB・処理・認証実装／行動の遷移先** | (38)(25 の遷移先) | Repository 全体の対象外 | 各 SCR §13/§15・IA §8/§9 | 対象外として整理 |
| **SCR-006〜SCR-012 未作成との関係** | (37) | Screen Requirements 課題 | screen-matrix.md §5 (SCR-006〜012 Not started)・各 SCR §2 | 未作成 (作成・内容推測せず・「CTA 不要」と判定せず・Booking 系 CTA を具体化しない) |
| **正式命名・Screen Requirement ID・Acceptance Criteria 確定主体** | (39) | Governance 課題 | 各 SCR §16/§17・README §7・cta §11 | Governance 側 (未整備) |

- **判定保留**: 本工程では該当なし (39 観点はいずれも直接証拠に基づき上記区分へ分類した)。

### 8H.5 §6.8・§8A.2 T6・§8G.6 との関係、保持事項

- **§6.8 との関係**: §6.8 の Remaining Blocking Fact を本再分類の粒度へ精密化した (§6.8 に注記)。§6.8 の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。§6.2 (GOV-0002 provenance) を §6.8 へ統合しない。
- **§8A.2 T6 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T6 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8H は現在状態の再分類記録である。
- **§8G.6 との関係**: §8G.6 が推薦した次工程が本 Task で着手されたことを §8G.6 に注記した (推薦記録は保持)。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-14-F1 の snapshot/履歴は監査証跡として変更しない (本 §8H から参照するのみ)。
- **保持事項**: T7〜T9 は未着手・未解決。Q2〜Q4 は未回答。Q5 は T1〜T5・Task 009-4-F1 の既存記録を変更せず T6 の影響度「高」を追加。画面別主要 CTA・予約/決済/取消の確約レベル・CTA ラベル・会員登録/ログイン誘導・モバイル CTA・法務/同意表現・GOV-0002 provenance 未確認・Button state follow-up #4 未取得・placeholder/実査待ちの確認方法・個別確認主体・SCR-006〜012 未作成・正式命名規則・Screen Requirement ID 未確定・`brand-content.md` 参照切れは保持。Task 009-6 の全 12 候補「現時点では開始できない」は不変。State 論点は Task 009-11 (T2)、Recovery・可逆/不可逆・サポート範囲は T7 の論点であり本工程で再判断・取り込みしない。アクセシビリティ適用規格は T9 の論点であり取り込まない。
- **本 Task の完了の意味**: 「Task 009-15 という再分類作業の完了」であり、「各画面の主要 CTA の確定」「CTA 文言・数・優先順位の確定」「予約・決済・取消の行動仕様の確定」「SCR-006〜012 の CTA 要件の確定」「Button variant との対応の確定」「GOV-0002 provenance の確認」「Button state の確定」「§6.8 阻害 Fact の全解消」「Design System 改定開始可能」「Alignment 完了条件充足」のいずれも宣言しない。

### 8H.6 次工程の推薦 (Task 009-15 後)

- **推薦対象**: T7「可逆・回復フロー・サポート範囲」(§8A.2 T7)。未着手一覧の次項として**機械的に選択**したものである。
- **推薦理由**: owner-decisions.md §8「どれからでも構わない」により着手順の制約がなく、一覧上 T6 の次項が T7 であるため。**優先順位・重要度判断ではない**。T6 の結果を T7 へ一般化しない。T7 も着手時に個別のスコープ選別が必要となり得る (Recovery Action や可逆/不可逆の具体的扱いを先回りして決めない)。T6 固有の直接依存 (再分類を確定するために不可欠な直接証拠・オーナー判断) は本工程で新たに特定されておらず、画面別主要 CTA・予約/決済・会員登録等の多数の事業判断が未確定であることを理由に一括 CTA 仕様確定タスクは推薦しない。
- **前提条件**: 本 §8H の記録が Repository に存在すること。T7 着手前に T7 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T7 の影響度判定 = Web部責任者 (規則 §8)。上流 (可逆/回復フロー・サポート範囲) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T7 の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Service Design (SDP-006・CTA-006)・Screen Requirements (SCR-013 等)。ただし T7 も対象外・既存 Draft・事業仕様・実査/provenance の選別を要し得る。Design System 本体は変更しない。
- **対象上流成果物・必要な直接証拠**: §8A.2 T7 記載のとおり (SDP-006 の Does Not Decide 記述・SCR-013 §16 Open Issue、対応 DS 候補側面 §6.4・§6.6・§6.12)。
- **完了条件**: T7 の各論点が指定観点へ分解され、直接証拠付きで分類され、元記録との関係が追跡でき、§6.4・§6.6・§6.12 の該当 Remaining Blocking Fact が精密化されること (内容は着手時に確定)。
- **対象外**: T1〜T6 の再判断、T7 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答、T8〜T9 の着手順序。
- **Q4・再評価の前後**: Repository 内の依存関係 (§7) 上、上流論点の整理 (R-C) は再評価 (R-H) の前段であり、Q4・Work Order 6 相当の再評価は T7 着手の前提ではない。
- **完了しても Design System 改定を開始できるとは限らない**: T7 の整理が記録されても、他論点・provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

> **注記 (Task 009-16, 2026-07-23)**: 本 §8H.6 が推薦した次工程 (T7) は Task 009-16 で着手した。ただし Task 009-16 は指示者判断により「T7 可逆・回復フロー・サポート範囲」から **「T7 可逆・回復・支援論点のスコープ選別・再分類」** へ再定義され、可逆・回復フローやサポート業務を一括新規確定せず、T7 に集約された論点の現在位置を選別・記録する工程となった。結果は §8I。本 §8H.6 は Task 009-15 時点の推薦記録として保持する。

## 8I. T7 の結果 (Task 009-16): 可逆・回復・支援論点のスコープ選別・再分類

### 8I.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T7 可逆・回復フロー・サポート範囲」ではなく **「T7 可逆・回復・支援論点のスコープ選別・再分類」** とする。可逆・回復フロー・サポート業務そのもの・保存期間/取消可否/Undo/エラー処理・FAQ/問い合わせ/SLA/運用体制・Recovery Action の具体割当・確認ダイアログ/モーダル等の UI・SCR-006〜SCR-012 の作成を推測で新規設計・確定せず、T7 に集約された論点の現在位置を選別・記録する。T7 固有の根拠 = principles.md SDP-006・cta-principles.md CTA-006/CTA-TYPE-002/004/005/Commitment Level Model/CTA State Model (§3〜§6)・navigation.md NVP-004/NAV-005・content-principles.md CTP-003/006/007/010・SCR-013 §4〜§17 が既に可逆・回復・支援の責務と、保存期間/取消可否/Undo/エラー処理等の Does Not Decide・サポート範囲/FAQ/問い合わせ等の Open Issue を区別していること。これは T2〜T6 の結果を自動適用したものではなく、T7 固有の直接証拠に基づく。
- **着手根拠**: §8H.6 が T7 を未着手一覧の次項として機械的に推薦したことによる (owner-decisions.md §8「どれからでも構わない」・一覧上 T6 の次項)。優先順位・重要度判断ではない。
- **影響度**: 高 (Web部責任者判定、2026-07-23、本件として明示取得)。理由 = 阻害 Fact の意味・分類・後続工程・Design System 候補側面 §6.4/§6.6/§6.12 との関係に影響し得る実質的変更のため。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8I.2 分類方法

各論点を 60 観点へ分解した (SDP-006 の Decision・「やり直し/修正/戻る」・「原因と次の行動」・「途中入力を失わせない」・「回復不可能な操作の事前確認」／保存期間／キャンセル可否／Undo 機能・仕様／エラー処理仕様／CTA-006／修正可能と取消困難の区別／取消期限／確認ダイアログ／状態遷移／CTA-TYPE-004 Recovery Action／CTA-TYPE-002 との境界／CTA-TYPE-003 との境界／CTA-TYPE-005 との境界／Commitment Level Reversible／Commitment Level High Commitment・Destructive／CTA State Unavailable/Error/Pending Confirmation／NVP-004／NAV-005／戻り先・再探索・回復手段／履歴・入力・文脈の保持／ブラウザバック・履歴保存・セッション管理／CTP-003／CTP-006／CTP-007／CTP-010／SCR-013 の支援責務／SCR-013 の Recovery Action 責務／Help and Support 対象範囲／FAQ 要否・分類・構成／問い合わせ手段・チャネル／サポート提供時間・SLA・運用体制・担当・エスカレーション／Policy 分類・情報源・本文／User・Booking との関係／認証前後の提供差／Contextual/Local/Utility Navigation の具体条件／問題解決後の戻り先／エラー・中断専用画面の要否／問題種別ごとの処理フロー／再試行・修正・戻る・問い合わせの具体割当／CTA 文言・数・配置・優先順位／FAQ 文言・問い合わせ案内・法務文言・ブランドトーン／モバイル支援導線／Accordion・フォーム・チャット・モーダル等 UI／Button/Input/Modal/Overlay との対応／Recovery Action と Component/variant の対応／Component state・token・値／TVL-0007 provenance／GOV-0002 provenance／Button state follow-up #4／Input state follow-up #2／`brand-content.md` 参照切れ／SCR-003 の Error・入力回復との境界／SCR-006〜012 未作成との関係／URL・route・画面遷移・API・DB・認証・処理／正式命名・ID・Acceptance Criteria 確定主体)。これらを 11 区分 (既存 Draft で明示 / 事業・商品・業務仕様 / Screen Requirements 課題 / Navigation 課題 / Content・State・CTA 課題 / Governance 課題 / Repository 全体の対象外 / UI・Implementation 下流課題 / DS 内部整合課題 / 実査・provenance トラック / 判定保留) へ分類した。1 観点が分類先の異なる構成要素を束ねる場合は要素へ分解して分類する (観点 (8) Undo は要否 = 事業仕様／実装 = 対象外、観点 (20) High Commitment・Destructive はモデル上の分類 = 既存 Draft／業務区分 = 事業仕様、観点 (25) 履歴・入力・文脈の保持は責務 = 既存 Draft/Navigation 課題／保持方式 = T1 論点・対象外、観点 (37) Policy は分類/情報源 = 事業仕様／本文正本 = Governance、観点 (45) CTA は文言 = Content・State・CTA／数・配置・優先順位 = UI 下流、観点 (51) は Component 対応/token = DS 内部整合／state 実測 = 実査、へ分解する)。

### 8I.3 SDP-006・CTA-006 等・SCR-013 の既存状態 (直接証拠に基づく確認)

- principles.md §SDP-006 Recoverability が「やり直し・修正・戻る手段を可能な範囲で提供／エラー時に原因と次の行動を理解可能に／途中入力を不必要に失わせない／回復不可能な操作には事前確認」を Application として、保存期間・キャンセル可否・Undo 実装・エラー処理仕様を Does Not Decide として Draft 定義。cta-principles.md が CTA-006 Reversible Before Irreversible (§3)・CTA-TYPE-002/004/005 (§4)・Commitment Level Model の Reversible/High Commitment/Destructive (§5)・CTA State Model の Unavailable/Error/Pending Confirmation (§6) を、navigation.md が NVP-004 Reversible Movement・NAV-005 History and Recovery Navigation を、content-principles.md が CTP-003/006/007/010 を Draft 定義。SCR-013 §4/§6/§9 が問題解決・条件確認の支援と Recovery Action 責務を記載し、§16 が Help 対象範囲・FAQ 要否/分類/構成・問い合わせ手段・サポートチャネル・提供時間/運用体制・Policy 分類/情報源・認証前後差・問題解決後の戻り先・エラー中断専用画面の要否を Open Issue として保持。
- したがって「可逆・回復・支援に関する上流要求が何も定義されていない」とは扱わない (分類 = 既存 Draft で明示)。同時に、Recoverability の原則を新規作成・再定義せず、SDP-006/CTA-006 だけから予約取消可否・取消期限・手数料・Undo 仕様・確認方式を確定せず、SCR-013 の User Task から FAQ 構成・問い合わせ方法・チャネル・SLA・担当部門・処理フローを創作せず、Navigation Action を Recovery Action・主要 CTA へ昇格しない。「Draft として存在すること」と「可逆・回復・支援仕様が確定していること」を区別する。

### 8I.4 論点別の再分類結果

| 論点 | 主な観点 | 分類結果 | 直接証拠 | §6.4/§6.6/§6.12 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| **SDP-006 Recoverability の Decision・Application** (やり直し/修正/戻る・原因と次の行動・途中入力を失わせない・不可逆前の事前確認) | (1)(2)(3)(4)(5) | 既存 Draft で明示 | principles.md §SDP-006 (Decision/Application) | 残さない (既定義。正式承認は別) |
| **CTA-006・可逆/不可逆区別・Recovery/Secondary/Navigation/Destructive Action 分類・Commitment Level・CTA State** | (10)(11)(15)(16)(17)(18)(19)(20 のモデル上の分類)(21) | 既存 Draft で明示 | cta-principles.md §3 (CTA-006)・§4・§5・§6・§8 | 残さない (既定義。新 CTA Type/State/Commitment Level を追加せず・High Commitment/Destructive の業務区分化は事業仕様へ) |
| **NVP-004・NAV-005 の責務・CTP-003/006/007/010・SCR-013 の支援/Recovery 責務** | (22)(23 の責務)(27)(28)(29)(30)(31)(32) | 既存 Draft で明示 | navigation.md NVP-004/NAV-005・content-principles.md CTP-003/006/007/010・SCR-013 §4/§6/§9 | 残さない (既定義。NAV-005 の保持方式は T1 論点で再判断しない) |
| **保存期間・キャンセル可否・Undo 要否・取消期限・High Commitment/Destructive の業務区分・Help 対象範囲・FAQ 要否/分類/構成・問い合わせ手段/チャネル・SLA/運用体制/担当/エスカレーション・Policy 分類/情報源・User/Booking 関係・認証前後差・問題種別ごとの処理フロー** | (6)(7)(8 の要否)(12)(20 の業務区分)(33)(34)(35)(36)(37 の分類・情報源)(38)(39)(43) | 事業・商品・業務仕様 | SDP-006・CTA-006 Does Not Decide・SCR-013 §13/§16・IA-OBJ-008 Open Issue | 事業・業務仕様側 (推測しない)。SCR-006〜012 を作成/推測せず・キャンセルポリシーを創作しない |
| **エラー・中断専用画面の要否・SCR-003 の Error/入力回復との境界・SCR-006〜012 未作成との関係** | (42)(57)(58) | Screen Requirements 課題 | SCR-013 §2/§16・accommodation-search.md (SCR-003) §10・screen-matrix.md §5 (SCR-006〜012 Not started) | Screen Requirements 課題。SCR-003 を境界確認以上に取り込まず (T4/入力論点を再判断しない)・SCR-006〜012 を作成/推測せず・「回復不要/サポート不要」と判定しない |
| **戻り先・再探索・回復手段の具体条件・履歴/入力/文脈保持・Contextual/Local/Utility Navigation の具体条件・問題解決後の戻り先** | (24)(25 の保持責務)(40)(41) | Navigation 課題 | SCR-013 §8・navigation.md NAV-005/NVP-003/NVP-004 Does Not Decide | Navigation 課題 (具体条件は未確定)。NAV-005 の保持方式は T1 論点で再判断しない・T7 は接点と境界のみ記録 |
| **再試行/修正/戻る/問い合わせの具体割当 (Recovery Action 具体)・CTA 文言・FAQ 文言/問い合わせ案内/法務文言/ブランドトーン** | (44)(45 の文言)(46) | Content・State・CTA 課題 (既存原則で責務充足・保持) | CTP-007・CTA-007・SCR-013 §7/§9/§13 | 分解して保持。具体文言/ライティング規則/FAQ/Policy 本文を確定せず・新 State を追加せず `Error / Interrupted` を分割せず・T2 状態論点を再判断せず・`brand-content.md` 参照切れを採用根拠にしない |
| **確認ダイアログ・CTA 数/配置/優先順位・モバイル支援導線・Accordion/フォーム/チャット/モーダル等 UI** | (13)(45 の数/配置)(47)(48) | UI・Implementation 下流課題 (「回復手段の意味・実行可能性を失わせない」要求は既存 Draft) | CTA-006 Does Not Decide・SCR-013 §11/§13/§15・components.md 未着手一覧 | 下流課題として整理 (sticky support CTA/bottom bar/チャット固定/PC・SP 順/ワイヤーフレームを決定せず・適用規格は T9) |
| **Undo 実装・エラー処理仕様・状態遷移・ブラウザバック/履歴保存/セッション管理・URL/route/画面遷移/API/DB/認証/処理** | (8 の実装)(9)(14)(26)(59) | Repository 全体の対象外 | SDP-006・CTA-006 Does Not Decide・navigation.md §7・SCR-013 §13/§15 | 対象外として整理 |
| **Button/Input/Modal/Overlay との対応・Recovery Action と Component/variant の対応・Component state/token** | (49)(50)(51 の Component 対応/token) | DS 内部整合課題 | WO5 C-07/C-08/C-09・§6.4/§6.6/§6.12・components.md Button/Input/Modal/Overlay | §6.4/§6.6/§6.12 の DS 対応整理として残る (T7 再分類で自動解決しない)。Component の存在/不在を採用根拠にせず・未着手 Component (Accordion 等) を必要 Component へ変換せず・Downstream Impact 例を採用決定にしない |
| **TVL-0007 provenance・GOV-0002 provenance・Button state follow-up #4・Input state follow-up #2・Component state 実測** | (51 の state 実測)(52)(53)(54)(55) | 実査・provenance トラック (R-D/R-E・Q2/Q3) | components.md (TVL-0007/GOV-0002/follow-up #2・#4)・§6.2/§6.6 | 未解決のまま保持 (実査せず・provenance 未確認を採用根拠にしない) |
| **Policy 本文正本・`brand-content.md` 参照切れ・正式命名・Screen Requirement ID・Acceptance Criteria 確定主体** | (37 の本文正本)(56)(60) | Governance 課題 | IA-OBJ-008 Open Issue・SCR-013 §16/§17・README §7・`brand-content.md` 参照切れ | Governance 側 (未整備・Policy 本文/文言の正本は `brand-content.md` 等 Governance 側で未整備・参照切れの正本作成/有効性確認は規則 §13・想定内容を採用根拠にしない) |

- **判定保留**: 本工程では該当なし (60 観点はいずれも直接証拠に基づき上記区分へ分類した)。

### 8I.5 §6.4・§6.6・§6.12・§8A.2 T7・§8H.6 との関係、保持事項

- **§6.4・§6.6・§6.12 との関係**: 3 候補側面の Remaining Blocking Fact を本再分類の粒度へ精密化した (各節に注記)。3 候補の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。§6.2 (GOV-0002 provenance) を §6.4/§6.6/§6.12 へ統合しない。
- **§8A.2 T7 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T7 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8I は現在状態の再分類記録である。
- **§8H.6 との関係**: §8H.6 が推薦した次工程が本 Task で着手されたことを §8H.6 に注記した (推薦記録は保持)。
- **他論点との境界**: NAV-005 の保持方式は T1 論点、State は T2 論点 (Task 009-11)、SCR-003 の入力回復は T4/入力論点、CTA 分類は T6 論点 (Task 009-15)、アクセシビリティ適用規格は T9 論点であり、本工程で再判断・取り込みしない。T7 では可逆・回復・支援との接点と境界のみを記録する。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-15-F1 の snapshot/履歴は監査証跡として変更しない (本 §8I から参照するのみ)。
- **保持事項**: T8〜T9 は未着手・未解決。Q2〜Q4 は未回答。Q5 は T1〜T6・Task 009-4-F1 の既存記録を変更せず T7 の影響度「高」を追加。サポート対象範囲・FAQ 要否/分類/構成・問い合わせ手段/チャネル・サポート時間/SLA/運用体制・Policy 分類/情報源/本文・認証前後差・問題解決後の戻り先・保存期間/Undo/キャンセル可否/エラー処理仕様・TVL-0007 provenance・GOV-0002 provenance・Button state follow-up #4・Input state follow-up #2・`brand-content.md` 参照切れ・placeholder/実査待ちの確認方法/個別確認主体・SCR-006〜012 未作成・正式命名規則・Screen Requirement ID は保持。Task 009-6 の全 12 候補「現時点では開始できない」は不変。
- **本 Task の完了の意味**: 「Task 009-16 という再分類作業の完了」であり、「可逆・回復フローの確定」「サポート対象範囲の確定」「FAQ・問い合わせ手段・サポートチャネルの確定」「SLA・運用体制・担当部門の確定」「取消可否・取消期限・Undo 仕様の確定」「予約変更・取消仕様の確定」「Recovery Action の具体割当の確定」「Button/Input/Modal/Accordion との対応の確定」「TVL-0007/GOV-0002 provenance の確認」「Button/Input state の確定」「`brand-content.md` 正本の確認」「§6.4/§6.6/§6.12 阻害 Fact の全解消」「Design System 改定開始可能」「Alignment 完了条件充足」のいずれも宣言しない。

### 8I.6 次工程の推薦 (Task 009-16 後)

- **推薦対象**: T8「タイポグラフィ具体規格の扱い」(§8A.2 T8)。未着手一覧の次項として**機械的に選択**したものである。
- **推薦理由**: owner-decisions.md §8「どれからでも構わない」により着手順の制約がなく、一覧上 T7 の次項が T8 であるため。**優先順位・重要度判断ではない**。T7 の結果を T8 へ一般化しない。T8 も着手時に個別のスコープ選別が必要となり得る (具体的な font size・line-height・文字数制限等を先回りして決めない)。T7 固有の直接依存 (再分類を確定するために不可欠な直接証拠・オーナー判断) は本工程で新たに特定されておらず、多数のサポート業務判断が未確定であることを理由に一括サポート仕様確定タスクは推薦しない。
- **前提条件**: 本 §8I の記録が Repository に存在すること。T8 着手前に T8 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T8 の影響度判定 = Web部責任者 (規則 §8)。上流 (タイポグラフィ具体規格の扱い) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T8 の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: Service Design (content-principles.md CTP-008)。ただし T8 も対象外・既存 Draft・事業仕様・実査/provenance の選別を要し得る。Design System 本体は変更しない。
- **対象上流成果物・必要な直接証拠**: §8A.2 T8 記載のとおり (CTP-008 の Does Not Decide 記述、対応 DS 候補側面 §6.11)。
- **完了条件**: T8 の各論点が指定観点へ分解され、直接証拠付きで分類され、元記録との関係が追跡でき、§6.11 の該当 Remaining Blocking Fact が精密化されること (内容は着手時に確定)。
- **対象外**: T1〜T7 の再判断、T8 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答、T9 の着手順序。
- **Q4・再評価の前後**: Repository 内の依存関係 (§7) 上、上流論点の整理 (R-C) は再評価 (R-H) の前段であり、Q4・Work Order 6 相当の再評価は T8 着手の前提ではない。
- **完了しても Design System 改定を開始できるとは限らない**: T8 の整理が記録されても、他論点・provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

> **注記 (Task 009-17, 2026-07-23)**: 本 §8I.6 が推薦した T8 は Task 009-17「タイポグラフィ論点のスコープ選別・再分類」として着手した (結果は §8J)。本推薦記録は Task 009-16 時点の記録として保持する。

## 8J. T8 の結果 (Task 009-17): タイポグラフィ論点のスコープ選別・再分類

### 8J.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T8 タイポグラフィ具体規格の扱い」ではなく **「T8 タイポグラフィ論点のスコープ選別・再分類」** とする。font size・font family・font weight・line-height・文字数制限・行数・行長・改行/禁則・truncation/ellipsis/line-clamp・overflow・可変/レスポンシブタイポグラフィ・PC/SP 別値・モバイル具体値等を推測で新規設計・確定せず、T8 に集約された論点の現在位置を選別・記録する。T8 固有の根拠 = content-principles.md CTP-008 が理解可能性・構造・簡潔さ・非視覚依存の**責務**を Decision/Application として定めつつ、具体的なアクセシビリティ規格・タイポグラフィ・文字数制限・Component 仕様を **Does Not Decide** として明示的に区別していること、および design.md §3・semantic.travel.json `font.*` が root 16px・rem 基準・2 書体・font family/weight・size scale・line-height scale・`font.body/heading/display/price` の用途を **bound** 値として既に保持していること。これは T2〜T7 の結果を自動適用したものではなく、T8 固有の直接証拠に基づく。「上流で具体規格が未定義」と「Design System にもタイポグラフィが存在しない」を同一視しない。
- **着手根拠**: §8I.6 が T8 を未着手一覧の次項として機械的に推薦したことによる (owner-decisions.md §8「どれからでも構わない」・一覧上 T7 の次項)。優先順位・重要度判断ではない。
- **影響度**: 高 (Web部責任者判定、2026-07-23、本件として明示取得)。理由 = 阻害 Fact の意味・分類・後続工程・Design System 候補側面 §6.11 との関係に影響し得る実質的変更のため (ルール制定・再分類段階の決裁として本件で「高」と取得)。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8J.2 分類方法

各論点を 70 観点へ分解した (CTP-008 Decision／CTP-008 Rationale／見出しによる構造理解／情報順序による構造理解／簡潔さ／長文を必要以上に連続させない責務／色だけに意味を依存させない責務／アイコンだけに意味を依存させない責務／位置だけに意味を依存させない責務／支援技術で意味を失わせない責務／CTP-008 のタイポグラフィ Does Not Decide／CTP-008 の文字数制限 Does Not Decide／CTP-008 のアクセシビリティ規格 Does Not Decide／CTP-008 の Component 仕様 Does Not Decide／SDP-007 との関係／T9 アクセシビリティ論点との境界／root font size／px・rem 基準／font family／font fallback／font weight／font size scale／line-height scale／本文・UI 用途／見出し用途／Display・Hero 用途／詳細施設名用途／数字・価格用途／semantic typography token／primitive typography token／`bound` 状態の意味／TVL-0001 等の記録との関係／上流要求と既存 token の対応／画面別の semantic role 割当／h1〜h6 等の具体階層／文字数制限／最小・最大文字数／推奨文字数／行数制限／一行当たりの文字数・行長／改行規則／禁則処理／truncation・ellipsis・line-clamp／overflow／可変・レスポンシブタイポグラフィ／PC・SP 別の font size／モバイル時の具体値／コンテンツ種別ごとの文章量／見出し文言・コピー／ブランドトーン／SEO 上の文字数／法務・Policy 文言／Component 内のテキスト制約／Button・Input・Card・PriceTag 等との関係／Component 固有の font・line-height・文字数／HTML 見出しレベル・semantic markup／CSS・クラス・実装方式／フォント配信・読み込み・fallback 実装／パフォーマンス／API・DB・CMS 上の文字数制約／多言語・翻訳時の文字量／現行画面の実測／Design System 内部整合／Screen Requirements への反映要否／Content・Editorial 成果物への反映要否／正式な規格・命名・確定主体／Acceptance Criteria／Task 009-14・T5 の価格・表示論点との境界／Task 009-16・T7 の支援・Content 論点との境界／T9 へ残す事項)。これらを 12 区分 (既存 Draft で明示 / 既存 Design System で明示 / Service Design の Does Not Decide / Screen Requirements 課題 / Content・Editorial 課題 / アクセシビリティ論点 / DS 内部整合課題 / UI・Implementation 下流課題 / Repository 全体の対象外 / Governance 課題 / 実査トラック / 判定保留) へ分類した。1 観点が分類先の異なる構成要素を束ねる場合は要素へ分解して分類する (観点 (6) 長文を連続させない = 責務は既存 Draft／具体文章量は観点 (48) Content・Editorial、観点 (13) アクセシビリティ規格 Does Not Decide = DND 宣言は Service Design の Does Not Decide／具体的適用規格・達成レベルは観点 (16)(70) の T9 論点、観点 (28) 数字・価格用途 = token の存在は既存 Design System／価格表示仕様は Task 009-14・T5 論点 (観点 (68)) で再判断しない、観点 (34) 画面別 semantic role 割当 = 責務と token の対応は DS 内部整合／画面別の具体割当は Screen Requirements 課題で font size を確定しない、観点 (50) ブランドトーン = Content・Editorial／T7 (観点 (69)) で扱ったトーンを再判断しない、観点 (52) 法務・Policy 文言 = Content・Editorial の文言量／Policy 本文正本は T7 Governance 課題 (観点 (69)) で再判断しない、へ分解する)。

### 8J.3 CTP-008・SDP-007・既存 Design System の既存状態 (直接証拠に基づく確認)

- content-principles.md §CTP-008 Accessible and Scannable Content が「視覚表現だけに意味を依存せず、見出し・順序・簡潔さにより理解しやすくする」を Decision、「見出しと情報順序で構造を理解できるように／長い文章を必要以上に連続させない／色・アイコン・位置だけに意味を依存させない／支援技術で意味が失われない表現を考慮」を Application、「具体的なアクセシビリティ規格 / タイポグラフィ / 文字数制限 / Component 仕様」を Does Not Decide として Draft 定義。principles.md §SDP-007 Accessibility by Default が「色だけに意味を依存させない／読みやすさ・操作可能性・情報理解を視覚表現より優先／キーボード・支援技術・異なる画面サイズを例外としない」を Application、「適用する具体的な規格 / 達成レベル / 実装方式 / 個別 Component の仕様」を Does Not Decide として Draft 定義。design.md §3 と semantic.travel.json `font.*` が root 16px・rem 基準 (TVL-0001)・明朝 (Noto Serif JP) ＋ ゴシック (LINE Seed JP) の 2 書体・font family (sans/heading/mincho/number)・font weight (bold 700)・font size scale (xs 0.75〜display-lg 3rem)・line-height scale (tight 1.3/normal 1.5/relaxed 1.8)・`font.body` (Q1)・`font.heading` h2 (Q2)・`font.display` (Q8/Q4)・`font.price` (Q3・tabular-nums) を `bound` 値として保持 (PriceTag 等での利用を含む)。
- したがって「タイポグラフィに関する上流要求が何も存在しない」とは扱わない (CTP-008 の理解可能性・構造・簡潔さ・非視覚依存の責務は既存 Draft で明示)。同時に「既存 Design System にタイポグラフィが存在しない」とも扱わない (root/rem・2 書体・token・scale・用途・bound 値が存在)。一方で、CTP-008 の責務と具体的なタイポグラフィ値を区別し、CTP-008 が具体規格・文字数制限を Does Not Decide としていることを直ちに「不足」「欠陥」「新規定義が必要」と判定せず、既存 bound token が存在することと上流要求との正式な対応・承認が確定していることを区別する。「Draft/bound として存在すること」と「画面別タイポグラフィ仕様・文字数制限・アクセシビリティ適用規格が確定していること」を区別する。

### 8J.4 論点別の再分類結果

| 論点 | 主な観点 | 分類結果 | 直接証拠 | §6.11 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| **CTP-008 の Decision・Rationale・Application (見出し・情報順序による構造理解・簡潔さ・長文を連続させない責務・色/アイコン/位置だけに意味を依存させない・支援技術で意味を失わせない)・SDP-007 との関係** | (1)(2)(3)(4)(5)(6 の責務)(7)(8)(9)(10)(15) | 既存 Draft で明示 | content-principles.md CTP-008 (Decision/Rationale/Application)・principles.md SDP-007 | 残さない (既定義。正式承認は別)。責務を新規作成・再定義しない |
| **root 16px・px/rem 基準・font family・font weight・size scale・line-height scale・本文/UI・見出し・Display/Hero・詳細施設名・数字/価格の用途・semantic/primitive token・`bound` の意味・TVL-0001 記録・T5 価格/表示境界** | (17)(18)(19)(21)(22)(23)(24)(25)(26)(27)(28 の token 存在)(29)(30)(31)(32)(68 の T5 価格・表示境界) | 既存 Design System で明示 | design.md §3・semantic.travel.json `font.body/heading/display/price`・primitive typography scale・TVL-0001 | 残さない (既存 bound)。既存 token の存在を上流承認へ昇格せず・font family/size/weight/line-height/semantic/primitive token・`bound` 状態・値・version を変更しない。価格表示タイポ (PriceTag/「円」weight) は T5 論点 (観点 68) で再判断しない |
| **CTP-008 のタイポグラフィ・文字数制限・アクセシビリティ規格・Component 仕様の Does Not Decide** | (11)(12)(13 の DND 宣言)(14) | Service Design の Does Not Decide | content-principles.md CTP-008 Does Not Decide | Does Not Decide として保持 (不足・欠陥・新規定義必要と即断しない)。上流で扱うか否かは §6.11 Prerequisite Owner Judgment。具体的適用規格・達成レベルは T9 論点 (観点 16/70) へ |
| **h1〜h6 等の具体階層 (画面別情報構造)・画面別 semantic role の具体割当・Screen Requirements への反映要否** | (34 の画面別具体割当)(35)(64) | Screen Requirements 課題 | 作成済み 7 SCR (見出し・構造・順序で理解可能にする責務)・screen-matrix.md §5 (SCR-006〜012 Not started) | Screen Requirements 課題。画面別 font size・見出し階層を新規設計せず・line-clamp/PC・SP 値/文字数を追加せず・SCR-006〜012 を作成/推測せず・作成済み SCR の Content Requirements を書き換えない |
| **文字数制限・最小/最大/推奨文字数・コンテンツ種別ごとの文章量・見出し文言/コピー・SEO 文字数・法務/Policy 文言・ブランドトーン・Content/Editorial 反映要否・T7 支援/Content 境界** | (36)(37)(38)(48)(49)(50 のトーン)(51)(52 の文言)(65)(69 の T7 支援・Content 境界) | Content・Editorial 課題 | CTP-008 Application (簡潔さ・長文を連続させない)・CTP-010・brand-content.md (正本・参照切れ) | Content・Editorial 課題。CTP-008 だけから具体的文字数/推奨文章量/コピー/行数を確定せず・T7 (観点 69) で扱ったブランドトーン/Policy 本文を再判断せず・brand-content.md 参照切れを採用根拠にしない |
| **T9 アクセシビリティ論点との境界・T9 へ残す事項 (具体的適用規格・達成レベル)** | (16)(70) | アクセシビリティ論点 (T9 との境界を保持) | design.md §2「WCAG 2.2 AA を最低ライン」・§8A.2 T9・SDP-007/CTP-008 Does Not Decide | T9 論点として保持。T8 で適用規格・達成レベル・最小 font size・contrast 基準・zoom/reflow 基準を確定せず・T9 の着手/完了を判断しない |
| **上流要求と既存 token の対応・画面別 semantic role 割当の対応・Button/Input/Card/PriceTag 等との関係・Design System 内部整合** | (33)(34 の責務と token の対応)(54)(63) | DS 内部整合課題 | design.md §3/§7・components.md (Button/Input/Card/PriceTag)・§6.11 | §6.11 の DS 対応整理として残る (T8 再分類で自動解決しない)。既存 token の存在を上流正式対応へ昇格せず・semantic role/Component 利用の正式対応は未確定・token/Component/値を変更しない |
| **行数制限・行長・改行/禁則・truncation/ellipsis/line-clamp・overflow・可変/レスポンシブタイポグラフィ・PC/SP 別 font size・モバイル具体値・Component 内テキスト制約/font/line-height/文字数** | (39)(40)(41)(42)(43)(44)(45)(46)(47)(53)(55) | UI・Implementation 下流課題 | CTP-008 Does Not Decide・SDP-007 Does Not Decide (実装方式)・components.md | 下流課題として整理 (responsive/fluid/clamp/省略/PC・SP 値/Component 内配置を決定せず・適用規格は T9)。文字数制限の責務 (観点 6) と line-clamp・行数・CMS 入力上限を混同しない |
| **font fallback 実装・CSS/クラス/実装方式・HTML 見出しレベル/semantic markup・フォント配信/読み込み・パフォーマンス・API/DB/CMS 文字数制約・多言語/翻訳時文字量** | (20)(56)(57)(58)(59)(60)(61) | Repository 全体の対象外 | design.md ヘッダー「実装の所在: GitHub `tocoo/tocoo_travel`」・本計画 §11 Downstream Impact「Implementation — Repository 管理対象外」 | 対象外として整理。CMS/DB 入力上限・SEO 実装を文字数制限の責務と混同しない |
| **正式な規格・命名・確定主体・Acceptance Criteria** | (66)(67) | Governance 課題 | governance/naming-rules.md (参照)・README §7・Review/Approval Rules §13 | Governance 側 (未整備)。正式命名・タイポグラフィ規格の確定主体・Acceptance Criteria は未確定・想定内容を採用根拠にしない・Wiki をタイポグラフィ仕様の正本にしない |
| **現行画面・実装値の実測** | (62) | 実査トラック (該当なし) | T-03 監査証跡 (placeholder/inspection pending/broken reference = 該当なし)・design.md §3 (typography は TVL-0001 で「実測」・bound) | 該当なし。タイポグラフィ値は既に bound (実測済み) ゆえ新規実査・provenance 問題を T8 へ追加しない (§7 R-E 実査トラック・T-03 監査証跡)。現行画面・CSS の実査は行わない |

- **判定保留**: 本工程では該当なし (70 観点はいずれも直接証拠に基づき上記各区分へ分類・整理した)。境界観点は主題の属する行に境界として明示している — (68) T5 価格・表示境界は既存 Design System 行、(69) T7 支援・Content 境界は Content・Editorial 行、(70) T9 へ残す事項はアクセシビリティ論点行 — うえで、§8J.5 で T5/T7/T9 の分類結果を変更せず接点のみ記録する。直接証拠がないため保留すべき観点は特定されず、タイポグラフィ値は bound・CTP-008 の Does Not Decide も明示のため保留に該当する事項はない。

### 8J.5 §6.11・§8A.2 T8・§8I.6 との関係、境界、保持事項

- **§6.11 との関係**: §6.11 の Remaining Blocking Fact を本再分類の粒度へ精密化した (同節に注記)。§6.11 の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。
- **§8A.2 T8 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T8 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8J は現在状態の再分類記録である。
- **§8I.6 との関係**: §8I.6 が推薦した次工程が本 Task で着手されたことを §8I.6 に注記した (推薦記録は保持)。
- **他論点との境界**: T5 (価格・表示論点 — PriceTag の価格タイポ・「円」weight・Card 表示・情報密度・価格/Review 表示仕様、観点 (68))、T7 (支援・FAQ・Policy 本文・ブランドトーン、観点 (69))、T9 (アクセシビリティ適用規格・達成レベル、観点 (16)(70)) は本工程で再判断・取り込みしない。必要な場合は接点のみ記録し、T5/T7/T9 の分類結果を変更しない。NAV/CTA/State 等の他論点も同様に再判断しない。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-16-F1 の snapshot/履歴は監査証跡として変更しない (本 §8J から参照するのみ)。§8A.2 T8 の Task 009-8 時点の記述は不変。
- **保持事項**: T9 は未着手・未解決。Q2〜Q4 は未回答。Q5 は T1〜T7・Task 009-4-F1 の既存記録を変更せず T8 の影響度「高」を追加。画面別 font size・line-height・文字数制限・responsive/省略方式・具体的アクセシビリティ規格/達成レベル・正式命名規則・Acceptance Criteria 確定主体は未確定。CTP-008 の Status は Draft。Task 009-6 の全 12 候補「現時点では開始できない」は不変。Design System 本体 4 資産 (components.md/design.md/primitive.travel.json/semantic.travel.json)・token・Component・値・status・version は不変。
- **本 Task の完了の意味**: 「Task 009-17 という再分類作業の完了」であり、「タイポグラフィ具体規格の確定」「文字数制限の確定」「画面別タイポグラフィの確定」「responsive typography・省略方式の確定」「既存 token の正式承認」「アクセシビリティ適合の確認」「§6.11 阻害 Fact の全解消」「Design System 改定開始可能」「Alignment 完了条件充足」のいずれも宣言しない。

### 8J.6 次工程の推薦 (Task 009-17 後)

- **推薦対象**: T9「アクセシビリティ適用規格の扱い」(§8A.2 T9)。未着手一覧の次項として**機械的に選択**したものである。
- **推薦理由**: owner-decisions.md §8「どれからでも構わない」により着手順の制約がなく、一覧上 T8 の次項が T9 であるため。**優先順位・重要度判断ではない**。T8 の結果を T9 へ一般化しない。T9 も着手時に個別のスコープ選別が必要となり得る (WCAG の具体的規格・達成レベル・最小 font size・contrast 等の基準値を先回りして決めない)。T8 固有の直接依存 (再分類を確定するために不可欠な直接証拠・オーナー判断) は本工程で新たに特定されていない (タイポグラフィ値は bound・CTP-008 の責務と Does Not Decide は明示)。したがって T8 固有の解消タスクは推薦せず、未着手一覧の次項 T9 を推薦する。
- **前提条件**: 本 §8J の記録が Repository に存在すること。T9 着手前に T9 の**影響度判定 (Q5)** を Web部責任者から取得すること。
- **必要な判断主体**: T9 の影響度判定 = Web部責任者 (規則 §8)。上流/Governance (アクセシビリティ適用規格・達成レベルをどのレイヤーで扱うか) の判断 = 影響度別 (規則 §12)。
- **必要レビュー主体**: T9 の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **想定する変更レイヤー**: 適用規格・達成レベルをどのレイヤー (Service Design・Governance) で扱うかを含む整理。ただし T9 も対象外・既存 Draft・事業/Governance・実査/provenance の選別を要し得る。Design System 本体は変更しない。
- **対象上流成果物・必要な直接証拠**: §8A.2 T9 記載のとおり (design.md §2「WCAG 2.2 AA を最低ライン」記述・各 SCR §11・適用規格未定義の Open Issue、対応 DS 候補側面 §6.7)。
- **完了条件**: T9 の各論点が指定観点へ分解され、直接証拠付きで分類され、元記録との関係が追跡でき、§6.7 の該当 Remaining Blocking Fact が精密化されること (内容は着手時に確定)。WCAG 規格・達成レベル・具体的基準値を先回りして決めない。
- **対象外**: T1〜T8 の再判断、T9 の上流内容そのものの解決の当否、候補採否・改定要否・改訂着手、Q2〜Q4 の回答。
- **Q4・Work Order 6 相当の再評価の前後**: Repository 内の依存関係 (§7) 上、上流/Governance 論点の整理 (R-C/R-D) は再評価 (R-H) の前段であり、Q4・Work Order 6 相当の再評価は T9 着手の前提ではない。推測で順序を変更しない。
- **完了しても Design System 改定を開始できるとは限らない**: T9 の整理が記録されても、provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

> **注記 (Task 009-18, 2026-07-24)**: 本 §8J.6 が推薦した T9 は Task 009-18「T9 アクセシビリティ論点のスコープ選別・再分類」として着手した (結果は §8K)。本 §8J.6 は Task 009-17 時点の推薦記録として保持する。

## 8K. T9 の結果 (Task 009-18): アクセシビリティ論点のスコープ選別・再分類

### 8K.1 工程の再定義・着手根拠・影響度

- **工程の再定義**: 指示者判断により、本工程は「T9 アクセシビリティ適用規格の扱い」ではなく **「T9 アクセシビリティ論点のスコープ選別・再分類」** とする。適用規格・達成レベル・Success Criteria・基準値・検証方法・適合判定・適合宣言を新規策定・確定せず、T9 に集約された論点の現在位置を直接証拠に基づき選別・記録する。T9 固有の根拠 = principles.md SDP-007・navigation.md NVP-008・content-principles.md CTP-008・cta-principles.md CTA-009 が理解可能性・操作可能性・非視覚依存・キーボード・支援技術・異なる画面サイズを例外扱いしない**責務**を Decision/Application として定めつつ、具体的な適用規格・達成レベル・実装方式・Component 仕様・focus 実装・HTML 属性・画像仕様を **Does Not Decide** として明示的に区別していること、作成済み 7 SCR §11 Accessibility Requirements が画面候補ごとの差異を保って責務を明示していること、および design.md §2「WCAG 2.2 AA を最低ライン」記述・`color.focus.ring`・text/brand コントラスト・Input error 非色依存・semantic color token・`bound` が既に存在すること。これは T2〜T8 の結果を自動適用したものではなく、T9 固有の直接証拠に基づく。「WCAG 2.2 AA という記述が存在する」ことと「適用規格・達成レベルが上流または Governance で正式確定している」ことを同一視しない。「アクセシビリティの上流責務が何も存在しない」とも記載しない。
- **着手根拠**: §8J.6 が T9 を未着手一覧の次項として機械的に推薦したことによる (owner-decisions.md §8「どれからでも構わない」・一覧上 T8 の次項)。優先順位・重要度判断ではない。T9 が最優先・最重要であること、WCAG 2.2 AA が正式承認済みであること、Success Criteria を確定できること、既存 Design System のアクセシビリティ適合が確認済みであること、T8 の分類結果を T9 へ一般化できること、Design System 改定を開始できること、Alignment が完了することのいずれも意味しない。
- **影響度**: 高 (Web部責任者判定、2026-07-24、本件として明示取得)。理由 = 阻害 Fact の意味・分類・後続工程・Design System 候補側面 §6.7 との関係に影響し得る実質的変更のため (ルール制定・再分類段階の決裁として本件で「高」と取得)。PR #83 の「編集的訂正＝低」carve-out は本工程に適用しない。過去 Task の影響度や前工程が「高」であったことから自己導出したものではない。必要レビュー主体 = Review / Approval Rules §10 既定の Web部責任者 ＋ チーフデザイナー。

### 8K.2 分類方法

各論点を 100 観点へ分解した (SDP-007 Decision／SDP-007 Rationale／SDP-007 Application／SDP-007 Does Not Decide／NVP-008 Decision／NVP-008 Application／NVP-008 Does Not Decide／CTP-008 Decision／CTP-008 Application／CTP-008 Does Not Decide／CTA-009 Decision／CTA-009 Application／CTA-009 Does Not Decide／後工程だけの検査項目にしない責務／キーボード利用／支援技術／異なる画面サイズ／モバイルでの意味・操作可能性／色だけに依存させない責務／アイコンだけに依存させない責務／位置だけに依存させない責務／画像だけに依存させない責務／状態を視覚だけで伝えない責務／Navigation の認識・理解・実行可能性／CTA の意味・状態・実行可能性／見出し・情報構造・読む順序／入力目的・現在値・状態／候補識別・比較関係／エラー・中断・回復方法／支援情報への到達・閲覧・行動／画像・地図・装飾がない場合の理解／作成済み 7 SCR §11 の共通責務／SCR ごとに異なる Accessibility Requirements／SCR の具体規格 DND／SCR の達成レベル DND／SCR の HTML 属性 DND／SCR のフォーカス実装 DND／SCR の Component 仕様 DND／SCR の画像・地図仕様 DND／SCR-006〜012 未作成／design.md「WCAG 2.2 AA を最低ライン」／要求仕様 R9 との関係／正式な適用規格／正式な達成レベル／適用範囲／対象画面・対象 Component／例外・適用除外／Success Criteria／達成基準値／適合判定／適合宣言／検証方法／検証主体／検証時点・再検証トリガー／検証環境／`color.focus.ring`／focus 可視化／focus 順序／Button・Input 等の focus 状態／Input error の非色依存表現／text 色コントラスト／brand 色コントラスト／非テキストコントラスト／semantic color token／`bound` の意味／placeholder・実査待ち状態／`$note` コントラスト未達監査記録／design.md・JSON・components.md 間整合／既存値と上流責務の対応／画像欠落 fallback／SCR-014 固有の画像依存／代替テキスト／画像・地図・アイコン仕様／HTML semantic markup／name・role・state 実装／フォーム label・説明・エラー関連付け／status message・live region 実装／zoom・reflow／target size・タップ領域／responsive UI／motion・animation／reduced motion 実装／読み上げ・操作順序／skip link・landmark 実装／font size・line-height／T8 タイポグラフィ境界／T4 入力・検索境界／T5 表示・料金・評価境界／T6 CTA 境界／T7 回復・支援境界／Component state 実査境界／現行画面の実測／keyboard 実査／支援技術実査／画像 fallback 実査／Repository 外 Implementation／API・DB・認証等の業務実装／正本・正式命名・確定主体／Acceptance Criteria／次工程へ残す事項)。これらを 13 区分 (既存 Service Design Draft で明示 / 既存 Screen Requirements で明示 / Service Design の Does Not Decide / Screen Requirements の Does Not Decide / 既存 Design System で明示 / アクセシビリティ規格・Governance 課題 / DS 内部整合課題 / UI・Implementation 下流課題 / Repository 全体の対象外 / 実査・検証トラック / 既存 placeholder・実査待ち / 他 Task 境界 / 判定保留) へ分類した。1 観点が分類先の異なる構成要素を束ねる場合は要素へ分解して分類する — 観点 (18) モバイルでの意味・操作可能性 = 到達可能性・意味を失わせない責務は既存 SCR §11／具体的な responsive・モバイル UI は UI・Implementation 下流、観点 (41) design.md の WCAG 2.2 AA 記述 = 記述の存在は既存 Design System／正式承認・適用範囲の確定は規格・Governance 課題、観点 (57) focus 可視化 = `color.focus.ring`・outline ベースの token 存在は既存 Design System／具体的な focus 実装は UI・Implementation 下流、観点 (59) Button・Input の focus 状態 = focus.ring outline の暫定適用は既存 Design System／hover・active・disabled の未取得 (follow-up #4) は既存 placeholder・実査待ち、観点 (63) 非テキストコントラスト = コントラスト記述の存在は既存 Design System／`border.default` の AA 3:1 未達可能性の個別確認は既存 placeholder・実査待ち、観点 (71) SCR-014 固有の画像依存 = 画像・地図・装飾がなくても理解可能にする責務は既存 SCR §11／画像欠落 fallback の実査待ちは既存 placeholder・実査待ち (観点 70)、へ分解する。説明なく複数分類へ二重計上しない。

### 8K.3 SDP-007・NVP-008・CTP-008・CTA-009・作成済み SCR・既存 Design System の既存状態 (直接証拠に基づく確認)

- principles.md §SDP-007 Accessibility by Default が「特定の利用条件を前提にせず、幅広い利用者・環境で理解・操作できる」を Decision、「色だけに意味を依存させない／読みやすさ・操作可能性・情報理解を視覚表現より優先／キーボード・支援技術・異なる画面サイズを設計上の例外としない／アクセシビリティを後工程だけの検査項目にしない」を Application、「適用する具体的な規格 / 達成レベル / 実装方式 / 個別 Component の仕様」を Does Not Decide として Draft 定義。navigation.md §NVP-008 Accessible Navigation が「キーボード・支援技術・異なる画面サイズ等を例外扱いしない」を Decision、「適用する具体的な規格・達成レベル・実装方式」を Does Not Decide。content-principles.md §CTP-008 Accessible and Scannable Content が「視覚表現だけに意味を依存せず、見出し・順序・簡潔さにより理解しやすくする」を Decision、「見出しと情報順序で構造理解／長文を連続させない／色・アイコン・位置だけに意味を依存させない／支援技術で意味が失われない表現」を Application、「具体的なアクセシビリティ規格 / タイポグラフィ / 文字数制限 / Component 仕様」を Does Not Decide。cta-principles.md §CTA-009 Accessible Activation が「キーボード・支援技術・異なる画面サイズでも行動の意味と実行可能性を失わせない」を Decision、「視覚表現だけで主要性や状態を伝えない／支援技術で役割・状態・結果を理解可能に／操作対象として認識・実行できるように」を Application、「適用規格 / サイズ基準 / フォーカス実装 / Component 仕様」を Does Not Decide として Draft 定義。
- 作成済み 7 SCR (SCR-001 service-entry・SCR-002 destination-discovery・SCR-003 accommodation-search・SCR-004 search-results・SCR-005 accommodation-detail・SCR-013 help-and-support・SCR-014 editorial-content) の §11 Accessibility Requirements が SDP-007/NVP-008/CTP-008/CTA-009 の範囲で「キーボード・支援技術・異なる画面サイズを例外扱いしない／Navigation・CTA・状態を視覚だけで伝えない／情報構造・見出し・読む順序を支援技術で理解可能に／モバイルでも意味・操作可能性を失わせない／検索条件の名称・目的・現在値・状態を理解可能に／候補の識別・比較関係を理解可能に／エラー・中断時に問題と回復方法を理解可能に／支援情報へ到達し読み行動を実行可能に／画像・地図・装飾がなくても対象・関係を理解可能に」を画面候補ごとの差異を保って明示し、「具体的な規格・達成レベル・HTML 属性・focus 実装・Component・画像/地図仕様は決定しない (§13 Does Not Decide)」と区別 (SCR-006〜SCR-012 は未作成 `Not started`)。design.md §2 が「WCAG 2.2 AA を最低ラインとし DS には違反値を入れない (要求仕様 R9)」を記述し本文 #424242 ≈9.7:1・主色 #2C50C8 ≈6.8:1 の AA 適合を併記、semantic.travel.json が `color.focus.ring` (≈10.4:1)・`color.text.body`・`color.state`・`color.border`・`color.icon` を `bound` 値として保持、components.md が状態固定リスト (hover/active/focus/disabled/loading/error/success)・focus outline (`color.focus.ring`)・Input「エラーはテキストメッセージ併記 (色のみで伝えない = WCAG 2.2 AA / R9)」を記述。
- したがって「アクセシビリティに関する上流責務が何も存在しない」とは扱わない (SDP-007/NVP-008/CTP-008/CTA-009 の責務・作成済み SCR §11 の責務は既存 Draft で明示)。同時に「既存 Design System にアクセシビリティ表現が存在しない」とも扱わない (focus.ring・コントラスト記述・非色依存記述・state・token が存在)。一方で、これらの責務・記述・値と、適用規格・達成レベルの正式確定・適合確認を区別し、SDP-007 等が具体規格・達成レベル・実装方式を Does Not Decide としていることを直ちに「不足」「欠陥」「新規定義が必要」と判定せず、既存 bound token・「WCAG 2.2 AA を最低ライン」記述が存在することと、適用規格・達成レベル・適用範囲・Success Criteria が上流/Governance で正式確定し既存 DS が適合済みであることを区別する。「Draft/bound/記述として存在すること」と「適用規格・達成レベル・適合が確定・検証・宣言されていること」を区別する。

### 8K.4 論点別の再分類結果

| 論点 | 主な観点 | 分類結果 | 直接証拠 | §6.7 阻害 Fact に残すか |
| --- | --- | --- | --- | --- |
| **SDP-007／NVP-008／CTP-008／CTA-009 の Decision・Rationale・Application (理解可能性・操作可能性・非視覚依存・キーボード・支援技術・異なる画面サイズ・後工程限定にしない・見出し/構造/順序・Navigation/CTA の認識・状態を視覚だけで伝えない)** | (1)(2)(3)(5)(6)(8)(9)(11)(12)(14)(15)(16)(17)(19)(20)(21)(23)(24)(25)(26) | 既存 Service Design Draft で明示 | principles.md SDP-007・navigation.md NVP-008・content-principles.md CTP-008・cta-principles.md CTA-009 (Decision/Rationale/Application) | 残さない (既定義。正式承認・適用規格は別)。責務を新規作成・再定義しない |
| **作成済み 7 SCR §11 の共通責務・画面候補ごとの差異・入力目的/現在値/状態・候補識別/比較・エラー/回復・支援情報到達・画像/地図/装飾非依存・モバイル到達可能性・SCR-014 の画像依存責務・SCR-006〜012 未作成** | (18 の責務)(22)(27)(28)(29)(30)(31)(32)(33)(40)(71 の SCR-014 責務) | 既存 Screen Requirements で明示 | 作成済み 7 SCR §11 Accessibility Requirements (SCR-001/002/003/004/005/013/014)・screen-requirements README (SCR-006〜012 Not started) | 残さない (既存 SCR 責務)。画面候補ごとの差異を保持・一律正規化せず・HTML/ARIA/focus 順序/target size/画像仕様を追加せず・SCR-006〜012 を作成/推測しない |
| **SDP-007／NVP-008／CTP-008／CTA-009 の Does Not Decide (適用規格・達成レベル・実装方式・Component 仕様・サイズ基準・フォーカス実装・HTML 属性)** | (4)(7)(10)(13) | Service Design の Does Not Decide | 各 Principle の Does Not Decide (適用する具体的な規格 / 達成レベル / 実装方式 / 個別 Component / サイズ基準 / フォーカス実装) | Does Not Decide として保持 (不足・欠陥・新規定義必要と即断しない)。具体的適用規格・達成レベルは規格・Governance 課題 (観点 43〜51) へ |
| **SCR の具体規格・達成レベル・HTML 属性・フォーカス実装・Component 仕様・画像/地図仕様の Does Not Decide** | (34)(35)(36)(37)(38)(39) | Screen Requirements の Does Not Decide | 作成済み SCR §11/§13「具体的な規格・達成レベル・HTML 属性・Component 実装・画像/地図仕様は決定しない」 | Does Not Decide として保持。HTML/ARIA・focus 順序・target size・画像/地図仕様を SCR へ追加せず・作成済み SCR を書き換えない |
| **design.md「WCAG 2.2 AA を最低ライン」記述・要求仕様 R9・`color.focus.ring`・focus outline token・Input error 非色依存・text/brand コントラスト・非テキストコントラスト記述・semantic color token・`bound` の意味** | (41 の記述の存在)(42)(56)(57 の token 存在)(59 の focus.ring outline)(60)(61)(62)(63 の記述の存在)(64)(65) | 既存 Design System で明示 | design.md §2 (WCAG 2.2 AA 最低ライン・R9・コントラスト比)・semantic.travel.json `color.focus.ring` (≈10.4:1)・`color.text.body` (≈9.7:1)・`color.state`・`color.border`・components.md (Input エラーはテキスト併記・focus outline・状態固定リスト) | 残さない (既存記述・token)。既存値・記述を適合確認済み・上流正式承認へ昇格せず・color/focus/contrast token・Component・`$status`・`$note`・`bound`・version を変更しない |
| **WCAG 2.2 AA の正式承認・適用範囲・正式な適用規格/達成レベル・対象画面/Component・例外・Success Criteria・達成基準値・適合判定・適合宣言・検証方法/主体/時点/再検証トリガー・正本/正式命名/確定主体・Acceptance Criteria** | (41 の正式承認・適用範囲)(43)(44)(45)(46)(47)(48)(49)(50)(51)(52)(53)(54)(98)(99) | アクセシビリティ規格・Governance 課題 | design.md §2「WCAG 2.2 AA を最低ライン」(記述のみ)・§8A.2 T9・§6.7・SDP-007/NVP-008/CTP-008/CTA-009 Does Not Decide・Review/Approval Rules §12/§13・governance/naming-rules.md (参照) | アクセシビリティ規格・Governance 課題として残る (§6.7)。WCAG 2.2 AA を正式承認・昇格せず・削除/変更/否定せず・規格/版/達成レベル/適用範囲/Success Criteria/基準値/適合判定/適合宣言/検証方法を確定せず・確定主体を定義しない |
| **既存値と上流責務の対応・design.md/JSON/components.md 間の記述整合** | (68)(69) | DS 内部整合課題 | design.md §2/§3・semantic.travel.json・components.md・§6.7 | §6.7 の DS 対応整理として残る (T9 再分類で自動解決しない)。既存値と上流責務の正式対応は未確定・token/値/記述を変更しない |
| **モバイル具体 UI・focus 実装/順序・代替テキスト・画像/地図/アイコン仕様・HTML markup・name/role/state・フォーム label/説明/エラー関連付け・live region・zoom/reflow・target size・responsive UI・motion/reduced motion・読み上げ/操作順序・skip link/landmark** | (18 の具体 UI)(57 の focus 実装)(58)(72)(73)(74)(75)(76)(77)(78)(79)(80)(81)(82)(83)(84) | UI・Implementation 下流課題 | SDP-007/CTA-009/CTP-008 Does Not Decide (実装方式・フォーカス実装)・SCR §13 Does Not Decide (HTML 属性・Component)・components.md・design.md ヘッダー (実装の所在) | 下流課題として整理 (HTML/ARIA・name/role/state・focus 順序・live region・zoom/reflow・target size・responsive・motion・skip link・代替テキストを決定せず・適用規格は規格課題)。具体実装を新規設計しない |
| **実装 Repository・API/DB/認証等の業務実装** | (96)(97) | Repository 全体の対象外 | design.md ヘッダー「実装の所在: GitHub `tocoo/tocoo_travel`」・本計画 §11 Downstream Impact「Implementation — Repository 管理対象外」 | 対象外として整理。実装 Repository・API/DB/認証を本工程で扱わない |
| **検証環境・Component state 実査境界・現行画面/keyboard/支援技術/画像 fallback の実査** | (55)(91)(92)(93)(94)(95) | 実査・検証トラック | §7 R-E 実査トラック・design.md §6/未確定事項 (画像欠落 fallback 実査待ち)・components.md follow-up #4 (Button/Input state 未取得)・§6.7 | 実査・検証トラックとして残る (R-E)。現行画面・keyboard・支援技術・画像 fallback・contrast の新規実査を行わず・既存の実査待ち記録のみを直接証拠として扱う |
| **placeholder・実査待ち状態・`$note` コントラスト未達監査記録・非テキストコントラスト未達の個別確認・Button/Input の hover/active/disabled 未取得・画像欠落 fallback** | (59 の hover・active・disabled 未取得)(63 の未達可能性の個別確認)(66)(67)(70)(71 の画像 fallback) | 既存 placeholder・実査待ち | semantic.travel.json `$note` (`border.default`「非テキスト UI 境界の AA 3:1 は用途により未達の可能性・個別確認」・focus/state)・components.md follow-up #4 (Button/Input state 未取得)・design.md §6/未確定事項 (画像欠落 fallback 🚧 実査待ち) | 既存 placeholder・実査待ちとして保持 (T9 の再分類だけで解消しない)。画像 fallback を解消済みにせず・コントラスト未達可能性の自認を適合確認へ変換せず・`$status`/`$note` を変更しない |
| **font size/line-height・T8 タイポグラフィ境界・T4 入力/検索境界・T5 表示/料金/評価境界・T6 CTA 境界・T7 回復/支援境界** | (85)(86)(87)(88)(89)(90) | 他 Task 境界 | §8J (T8)・§8F (T4)・§8G (T5)・§8H (T6)・§8I (T7)・各 Change Log | 他 Task 境界として保持。T4〜T8 で扱った論点を再判断せず・最小 font size/line-height をアクセシビリティ規格として新規確定せず・接点のみ記録 |

- **判定保留**: 本工程では該当なし (100 観点はいずれも直接証拠に基づき上記各区分へ分類・整理した)。境界観点は主題の属する行に境界として明示している — (85)(86) font size/line-height・T8 境界は他 Task 境界行、(87)(88)(89)(90) は他 Task 境界行、(71) は既存 SCR 責務 (画像非依存) と既存 placeholder・実査待ち (画像 fallback) へ分解 — うえで、§8K.5 で T4〜T8 の分類結果を変更せず接点のみ記録する。観点 (100) 次工程へ残す事項は §8K.6 で扱う。直接証拠がないため保留すべき観点は特定されず、責務・記述・token は既存 Draft/SCR/DS に明示、Does Not Decide も明示のため保留に該当する事項はない。

### 8K.5 §6.7・§8A.2 T9・§8J.6 との関係、境界、保持事項

- **§6.7 との関係**: §6.7 の Remaining Blocking Fact を本再分類の粒度へ精密化した (同節に注記)。§6.7 の **Task 009-6 Current Judgment「現時点では開始できない」は変更しない**。候補採否・改定要否・改訂着手可否も変更しない。
- **§8A.2 T9 との関係**: §8A.2 (Task 009-8 時点の論点別展開) の T9 記述・完了条件は**遡及変更しない** (当時の記録として保持)。本 §8K は現在状態の再分類記録である。
- **§8J.6 との関係**: §8J.6 が推薦した次工程が本 Task で着手されたことを §8J.6 に注記した (推薦記録は保持)。
- **他論点との境界**: T8 (font size/line-height・font family・文字数制限 等、観点 (85)(86))、T4 (入力・検索、観点 (87))、T5 (表示・料金・評価、観点 (88))、T6 (主要行動・CTA、観点 (89))、T7 (可逆・回復・支援、観点 (90)) は本工程で再判断・取り込みしない。必要な場合は接点のみ記録し、T4〜T8 の分類結果を変更しない。NAV/State 等の他論点も同様に再判断しない。最小 font size・line-height をアクセシビリティ規格として新規確定しない。
- **過去成果物の不変**: Work Order 2〜5・Task 009-6・Task 009-7〜009-17-F1 の snapshot/履歴は監査証跡として変更しない (本 §8K から参照するのみ)。§8A.2 T9 の Task 009-8 時点の記述は不変。service-design-alignment-assessment.md・screen-requirements-alignment-assessment.md・alignment-observations-aggregation.md (T-01/X-04)・alignment-amendment-candidate-separation.md・alignment-amendment-readiness-reassessment.md (§9.7) の過去時点の評価・集約・分離・再評価の監査証跡は変更しない。
- **保持事項**: Q2〜Q4 は未回答。Q5 は T1〜T8・Task 009-4-F1 の既存記録を変更せず T9 の影響度「高」を追加。正式な適用規格・達成レベル・適用範囲・対象画面/Component・例外・Success Criteria・達成基準値・検証方法・検証主体・適合判定・適合宣言は未確定。画像欠落 fallback は実査待ち。Component state・focus 等の既存実査待ちは保持。SCR-006〜012 は未作成。SDP-007・NVP-008・CTP-008・CTA-009 は Draft。Task 009-6 の全 12 候補「現時点では開始できない」は不変。Design System 本体 4 資産 (components.md/design.md/primitive.travel.json/semantic.travel.json)・token・Component・値・status・version は不変。
- **本 Task の完了の意味**: 「Task 009-18 という再分類作業の完了」であり、「アクセシビリティ適用規格の確定」「達成レベルの確定」「WCAG 2.2 AA の正式承認」「Success Criteria の確定」「既存 DS の適合」「実装の適合」「画像 fallback の確定」「§6.7 阻害 Fact の全解消」「Design System 改定開始可能」「Alignment 完了条件充足」のいずれも宣言しない。

### 8K.6 次工程の推薦 (Task 009-18 後)

- **推薦対象**: `alignment-blocking-facts-resolution-plan.md` に記録された依存関係の再確認に基づく **provenance / 参照切れの確認トラック (R-D) の整理** を 1 件推薦する。T1〜T9 の論点別スコープ選別・再分類が一巡した (§8C〜§8K) ことを踏まえた推薦であり、着手の可否・順序・優先度の判断ではない。
- **T9 固有の直接依存の有無**: T9 の再分類自体を確定するために不可欠な直接証拠・オーナー判断は本工程で新たに特定されていない (SDP-007/NVP-008/CTP-008/CTA-009 の責務・作成済み SCR §11・design.md の WCAG 記述・focus/コントラスト token は既存 Draft/SCR/DS に明示、適用規格・達成レベルの内容未定義・画像 fallback 実査待ち・コントラスト未達可能性の自認は既に §6.7・R-D/R-E トラックに整理済み)。したがって T9 固有の解消タスクは推薦しない。
- **推薦理由** (Repository 内の依存関係に基づく。優先順位・重要度・効果・工数を推測しない): T1〜T9 の一巡により上流 Open Issue の論点別整理 (R-C) は各論点で記録されたが、複数候補に共通して残る非上流の阻害 Fact のうち **provenance 未確認・参照切れ/正本不在** (GOV-0002 の ADR 正本・TVL-0007・`brand-content.md`・`governance/naming-rules.md` 等) は、規則 §13 の provenance/正本確認トラック (R-D) に属し、いずれの論点の再分類でも解消されていない (§6.2・§8A.3・§8B.3)。依存グラフ上、これらは実査 (R-E)・再評価 (R-H)・候補採否 (R-F) の前段に位置する。どの非上流トラック (provenance/参照切れ/placeholder/実査待ち) を先に扱うかの選定基準は Repository 内に存在しないため、単一トラックの整理として R-D を推薦し、着手の可否・順序は Web部責任者判断に委ねる。
- **前提条件**: 本 §8K の記録が Repository に存在すること。次工程着手前に当該工程の**影響度判定 (Q5)** を Web部責任者から個別取得すること (本 Task の影響度とは別)。
- **必要な判断主体**: 次工程の影響度判定 = Web部責任者 (規則 §8)。provenance/正本の有効性確認主体 = 規則 §13。
- **必要レビュー主体**: 次工程の影響度判定 (Q5) 前は未確定 (高＝Web部責任者＋チーフデザイナー／低＝Web部レビュー担当者、規則 §10)。
- **守る事項**: Q4・Work Order 6 相当の再評価 (R-H) を自動的に開始しない。provenance/参照切れ/placeholder/実査待ちのどれを先に扱うかを推測で確定しない (R-D を単一トラックとして推薦するに留め、内部の着手順は選定しない)。候補採否・改定要否・改訂着手へ飛ばない。優先順位・重要度・効果・工数を推測しない。後続 Issue は作成しない。
- **完了しても Design System 改定を開始できるとは限らない**: 次工程の整理が記録されても、provenance/参照切れ・placeholder/実査待ち・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、実際の Design System の改定は開始できない。

## 8L. Task 009-19: provenance・参照切れ確認トラック (R-D) の整理

### 8L.1 目的・R-D 対象範囲・着手根拠・影響度

- **目的**: Travel Alignment に残る provenance 未確認・参照切れ・正本不在を、Repository 内の直接証拠に基づき全数調査し、後続で個別解消できる単位へ整理する。**ADR・正本文書の新規作成による解消は行わない**。placeholder/実査待ちトラック (R-E)・Work Order 6 相当の再評価 (R-H)・候補採否 (R-F)・Design System 改定は開始しない。
- **R-D 対象範囲**: §8K.6 および PR #101 が Task 009-19 へ残した provenance/参照切れ確認トラック (R-D)。対象は Travel と Travel から直接参照される Governance 成果物。Rental Car/Inbound は Task 009-18-BP1 による TVL-0004 の直接参照確認の範囲に限定し、両サービスの provenance 全体へ一般化しない。
- **着手根拠**: §8K.6 が T1〜T9 再分類完了後の次工程として R-D 整理を推薦したことによる (owner-decisions.md §8「どれからでも構わない」)。優先順位・重要度判断ではない。
- **影響度**: 低 (Web部責任者判定、2026-07-24、本件として明示取得)。理由 = 本工程は既存の直接証拠の全数調査・整理であり、Decision 内容・token・正本・値を変更しないため。必要レビュー主体 = Review/Approval Rules §10 の低 = Web部レビュー担当者。過去 Task の影響度や前工程からの自己導出ではない。

### 8L.2 全数調査方法・区別する状態

- **調査方法**: 最新 main (`736e7dec`) を対象に `GOV-`・`TVL-`・`ADR`・`Decision ID`・`provenance`・`正本`・`Source of Truth`・`brand-content.md`・`naming-rules.md`・`follow-up #`・`basedOn`・`参照切れ`・`MISSING`・`未確認`・`不在` を全数検索し、現行 DS 4 資産 (design.md/primitive.travel.json/semantic.travel.json/components.md)・Governance (README/owner-decisions.md/review-approval-rules.md)・過去評価成果物を突合した。baseline-assessment.md §12 (Provenance and Broken Reference Inventory)・§13・§16 が既に本トラックの権威記録を持ち、本節はその現在状態を確認・整理したものである (baseline は変更しない)。
- **区別する状態 (10 区分)**: ① Decision ID 記述あり + ADR 正本確認可、② Decision ID 記述あり + ADR 正本未確認、③ 文書参照あり + 参照先不在 (参照切れ)、④ 追跡番号あり + 追跡先不明 (追跡先不足)、⑤ 現オーナー判断は記録済 + 過去 Decision の provenance 未確認、⑥ Repository 内で追跡可、⑦ 外部 Repository/URL 参照 (本工程で内容未検証)、⑧ 過去成果物/snapshot にのみ残る記述、⑨ placeholder/実査待ち (R-E へ残す)、⑩ 証拠不足で判定保留。**「正本がない」と「Decision 内容が無効」を同一視しない。**

### 8L.3 項目別調査表

| 対象 | 種別 | 出現箇所 (現行)・主張役割 | 参照先/実在確認 | 現在の直接証拠・状態 | 関連候補・論点 | 解消に必要なもの (本工程では実施しない) | Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **GOV-0002** (Button variant 5 語彙 primary/secondary/ghost/campaign/text) | ADR provenance | design.md §7・components.md 共通事項/Button・semantic.travel.json (語彙の正) | ADR 正本 **不在** | 複数文書で語彙一致は確認可。ADR 正本を Repository 内に確認できない → **provenance 未確認** | §6.2 (Nav/CTA 責務 DS 本文規則の provenance)・T6 (§6.8)。§8A.3 で §6.2 は R-D トラック | ADR 正本の作成/有効性確認 (影響度別・規則 §13)・Web部責任者判断 | Button variant の採否・有効性・語彙を再決定しない |
| **TVL-0001〜0003・0005・0006・0008・0010〜0012** | ADR provenance | design.md・components.md・JSON 全体 (bound 値・記述の根拠として参照) | ADR 正本 **不在** | 各 Decision の記述・bound 値は確認可。ADR 正本を確認できない → **provenance 未確認** (記述一致 ≠ 正本確認) | T1〜T8 の再分類 (§8C〜§8J) で扱った DS 内部整合。§6 各候補 | ADR 正本の作成/有効性確認 (規則 §13)・Web部責任者判断 | Decision ID を再認定しない・内容を変更しない |
| **TVL-0004** (breakpoint 640/768/1024/1280) | ADR provenance (特記) | primitive.travel.json `breakpoint.*` (bound)・design.md §4 | ADR 正本 **不在** | (a) Travel DS に 640/768/1024/1280 が `bound` として存在、(b) Task 009-18-BP1 で 3DS 共通値として再認定、(c) owner-decisions.md Q5 に 2026-07-24 判断が記録済 — の 3 事実は**有効**。一方 (d) 元 TVL-0004 の ADR 正本・当初 Decision の provenance は **未確認**。(a)〜(c) と (d) を区別する | Task 009-18-BP1・owner-decisions.md Q5・§6.7 (T9 境界) | 元 ADR provenance の確認 (規則 §13)。現 Q5 判断は取得済 | 現 Q5 判断を無効・未決へ戻さない。現在値の再認定を元 ADR provenance 確認済みの証拠に使わない |
| **TVL-0007** (drawer 全面統一・centered dialog deprecated) | ADR provenance (特記) | design.md §7・components.md §Modal (§7/§8) | ADR 正本 **不在** | drawer 全面統一・centered dialog deprecated の現在記述は複数文書で一致。ADR 正本は未確認 → **provenance 未確認** (記述一致 ≠ 正本確認) | §6.4/§6.6/§6.12 (T7 Recovery の Modal/Overlay)・C-07/08/09 | ADR 正本の確認 (規則 §13) | Modal/drawer 仕様を変更・再決定しない |
| **TVL-0009** | 追跡参照 (特記) | **4 資産のどこにも出現しない** | — | TVL 連番上、0001〜0008・0010〜0012 は出現するが **0009 は出現しない**という観測事実のみ | TVL 連番 (baseline §13 観察 #7) | 欠番/未記録/予約番号等の意味の確認 (Web部責任者判断) | 連番上存在するはずと推測しない。欠番・削除・未記録・予約の意味を推測しない |
| **brand-content.md** | 文書参照 (参照切れ) | design.md §1/§8 (「正: brand-content.md」ライティング・価格表記)・DS README §7 等 | **不在 (MISSING)** | design.md が「正」と参照するが Repository 内に不在 → **参照切れ**。過去評価 (baseline §12・WO 集約/分離) でも参照切れとして継承記録 | §6.5 (T3 IA/Content)・§6.4/6.6/6.12 (T7 Policy/トーン)・CTP-002/005 | 正本作成の要否・参照の扱いの判断 (規則 §13・Web部責任者) | 内容を推測・新規作成しない。別文書を代替正本へ昇格しない。参照を一括削除・置換しない |
| **governance/naming-rules.md** | 文書参照 (参照切れ) | design.md §9 (Agent Prompt Guide)・components.md §1/§2/§7/§8・governance/README.md | **不在 (MISSING)**。governance/README.md も「未作成/未整備」と明記 | 命名規則の正本として参照されるが不在 → **参照切れ (命名規則正本の不足)** | GOV-0002 の正式命名・§6 全般の命名・ID provenance | 正本作成の要否・参照の扱いの判断 (規則 §13・Web部責任者) | 内容を推測・新規作成しない。別文書を代替正本へ昇格しない。参照を一括削除・置換しない |
| **follow-up #3** (motion 実値: transition/duration/easing) | 追跡参照 (追跡先不足) | design.md §未確定事項一覧・primitive/semantic の motion `$note`/`$status: placeholder` | owner-decisions.md §3 の follow-up 一覧に **記載なし** | DS は follow-up #3 を参照するが owner-decisions §3 に追跡記述がない → **追跡先不足 (provenance 未確認)**。motion の値自体は placeholder/実査待ち = **R-E** | R-E (motion placeholder)・baseline §13 観察 #8 | 追跡先の確認 (owner-decisions §3 への追加要否・Web部責任者判断) | 新しい追跡番号へ付け替えない。motion 値・easing・duration を確定しない |
| **Source of Truth URL・実装 Repository `tocoo/tocoo_travel`** | 外部参照 | 4 資産 header・primitive.travel.json `$meta`・design.md 実装の所在 | 自己参照 URL / 外部 Repository | 記載がある Fact のみ確認。接続先内容は **本工程で未検証 = 外部参照** | Implementation (Repository 管理対象外) | 接続先内容の検証方法の決定 (本工程外) | 外部内容を検証しない・確認済みへ昇格しない |
| **follow-up #2 / #4 / #5 / #13** | placeholder/実査待ち (R-E 境界) | design.md・components.md・JSON | owner-decisions.md §3 に「未取得データ」として **記載あり** (解決値ではない) | 追跡は Repository 内にあり (#3 と異なり追跡先不足ではない)。値は未取得・実査待ち → **R-E** | R-E (placeholder/実査待ち)・#4=Button state・#13=shadow・#5=success(解決済)・#2=フォーム | R-E トラックで扱う (本 R-D の対象外) | placeholder を解消しない・実査しない |

- **判定保留**: 本工程では該当なし (上記各項目はいずれも直接証拠に基づき provenance 未確認/参照切れ/追跡先不足/外部参照/R-E 境界のいずれかへ整理した)。証拠不足で保留すべき項目は特定されなかった。

### 8L.4 個別状態の補足 (§6 の注意に対応)

- **GOV-0002**: 複数文書で同じ語彙が記述されていても、それだけで ADR 正本確認済みとしない。Button variant の採否・有効性・語彙を再決定しない。§6.2・T4・T6・T7 等との接点を記録しても各論点を再判断しない。
- **TVL-0004**: 現在値の `bound`・3DS 再認定 (BP1)・Q5(2026-07-24) の 3 事実と、元 ADR 正本・当初 Decision の provenance 未確認を区別する。現 Q5 判断を無効・未決へ戻さない。現在値の再認定を元 TVL-0004 の ADR 正本が確認済みである証拠に使用しない。
- **TVL-0007**: drawer 全面統一・centered dialog deprecated という現在記述を確認する。記述の一致と ADR 正本の確認を区別する。Modal/drawer 仕様を変更・再決定しない。
- **TVL-0009**: 連番上存在するはずと推測しない。欠番・削除済み・未記録・予約番号等の意味を推測しない。「4 資産に出現しない」という観測事実だけを記録する。
- **brand-content.md・governance/naming-rules.md**: 不在を確認しても内容を推測・新規作成しない。別文書を自動的な代替正本へ昇格しない。正本が必要か・参照を削除すべきかを本工程で決定しない。過去文書の参照を一括置換しない。
- **follow-up #3**: DS 内の参照箇所と owner-decisions.md 等の追跡記録を照合した結果、owner-decisions §3 に追跡先がないため「追跡先不足」と記録する。新しい追跡番号へ付け替えない。motion 値・easing・duration を確定しない。

### 8L.5 R-D と R-E の境界・関連 §6 候補・本工程で決定しない事項

- **R-D と R-E の境界**: R-D = provenance 未確認 (GOV-0002・TVL 群)・参照切れ (brand-content.md・naming-rules.md)・追跡先不足 (follow-up #3 の追跡欠落)・外部参照。R-E = placeholder/実査待ちの**値**の取得 (motion follow-up #3 の値・Button state follow-up #4・shadow follow-up #13・radius.card 等)。follow-up #3 は R-D (追跡先不足) と R-E (値 placeholder) の両面を持つため双方に記録し、本工程では R-D 面 (追跡先の確認) のみ整理し値は決定しない。
- **関連 §6 候補**: §6.2 (GOV-0002 provenance = R-D、§8A.3 で明示)・§6.4/§6.6/§6.12 (T7、brand-content.md/TVL-0007)・§6.5 (T3、brand-content.md)・§6.7 (T9、TVL-0004)・§6.8 (T6、GOV-0002)。いずれも本工程で再判断しない。
- **各項目の解消に必要なもの**: ADR 正本 (GOV-0002・TVL 群・TVL-0004 元 provenance・TVL-0007) の作成/有効性確認、参照切れ 2 文書の正本要否・参照の扱い、follow-up #3 の追跡先確認、TVL-0009 の欠番の意味、外部参照の検証方法 — いずれも規則 §13 の Governance/ADR/provenance/参照切れの正本作成/有効性確認主体 (影響度別) の判断を要する。本工程では特定・記録のみで実施しない。
- **本工程で決定しない事項**: ADR 正本の新規作成、GOV-0002・TVL 群の再認定、Decision 内容の変更、Decision ID の新規採番/改番、brand-content.md/naming-rules.md の作成、不在文書の内容推測、参照の一括削除/置換、follow-up #3 の解消値、placeholder token の解消、実査、外部 Repository の内容確認、token/Component/値/status/version の変更、T1〜T9 の再判断、R-E/R-H/R-F の開始、候補採否/改定要否/継続保留/改訂着手/設計承認。

### 8L.6 次工程の推薦 (Task 009-19 後)

- **推薦対象**: R-D 項目の**解消の着手単位・最初に扱う対象**についての Web部責任者判断の取得。
- **推薦理由** (Repository 内の直接証拠と依存関係に基づく。重要度・効果・工数を推測しない): 本 §8L で R-D 対象は追跡可能な単位へ整理されたが、どの項目 (ADR provenance / 参照切れ / 追跡先不足 / 外部参照) から着手するか・解消単位をどう採るかの選定基準は Repository 内に存在しない。規則 §13 の Governance/ADR/provenance/参照切れ正本作成・有効性確認は影響度別のオーナー判断を要する。したがって単一の解消作業を直接証拠から選べないため、着手単位・対象の Web部責任者判断の取得を 1 件推薦する。
- **守る事項**: R-D 項目の解消順を重要度・効果・工数から推測しない。ADR 作成を自動的な次工程にしない。brand-content.md/naming-rules.md 作成を自動的に優先しない。R-E/R-H/R-F へ自動的に進まない。後続 Issue は作成しない。
- **前提条件**: 本 §8L の記録が Repository に存在すること。着手する工程の影響度 (Q5) を別途取得すること (本 Task の影響度ではない)。
- **完了しても Design System 改定を開始できるとは限らない**: R-D 整理の記録は、ADR 正本作成・参照切れ解消・実査 (R-E)・再評価 (R-H)・候補採否/改定判断 (R-F)・改訂着手承認 (R-G) を経ない限り、Design System の改定開始を意味しない。

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
| 2026-07-22 | T4 入力・検索論点のスコープ選別・再分類 (Task 009-13): 旧「T4 入力・検索仕様」を指示者判断で **「T4 入力・検索論点のスコープ選別・再分類」** へ再定義 (T4 固有の根拠 = accommodation-search.md が既に責務〈§6/§8〉と未確定事項〈§13/§16〉・対象外〈§13/§15〉を区別。T2/T3 の自動適用でない)。T4 の論点を 21 観点へ分解し 10 区分へ個別分類 (§8F 新設)。直接証拠に基づき、Search Criteria の指定・確認・変更・文脈保持・回復・状態識別の責務=既存 Draft で明示 (IA §5・navigation §4〈NAV-004/005 定義〉・§6/§7〈適用先〉・SCR-003 §6/§8/§10)、具体的入力項目・必須/初期値/形式/依存・検索成立条件・Destination 指定方式・会員差分=事業・商品・業務仕様 (SCR-003 §16・§13)、検索ロジック/API/DB/検索エンジン/セッション/URL/保持実装方式=Repository 対象外 (SCR-003 §13/§15・navigation §7)、具体フォーム/Widget/モバイル UI=UI・Implementation 下流、バリデーション=業務条件/状態伝達/エラー文言/Component state/実装検証へ分解 (Error / Interrupted 分割せず新規 State 追加せず)、条件保持の方式・期間=事業・法務・セキュリティ判断＋実装、User 会員差分=事業・会員・認証仕様、SCR-001/004 接続=接続責務は既存/具体データ・遷移は対象外 (空結果は Task 009-11 の再分類を保持し再判断せず)、DS Input/SearchForm 対応=DS 内部整合課題 (T4 で自動解決しない)、follow-up #2・GOV-0002・確認方法・個別確認主体=実査/provenance トラック (R-D/R-E・Q2〜Q4) として保持、正式命名・ID・Acceptance Criteria 確定主体=Governance 課題、と整理。§6.9 の Remaining Blocking Fact を本粒度へ精密化 (§6.9 の Current Judgment「現時点では開始できない」は不変)。§8E.6 に着手済み注記。入力項目・必須条件・検索成立条件・バリデーション・条件保持・会員差分・検索ロジックを推測で新規設計せず、入力・検索仕様の確定・SCR-003 §16 全解決・§6.9 全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-22、本件明示取得、PR #83 carve-out 不適用)。遡及は T4 と直接出所に限定し T1〜T3・T5〜T9・他サービスへ一般化しない。§8A.2 T4 (Task 009-8 時点) の記述・Work Order 2〜5・Task 009-6〜009-12 の snapshot/履歴・accommodation-search.md/service-entry.md/search-results.md/information-architecture.md/navigation.md/content-principles.md/cta-principles.md/screen-matrix.md/ux-decision-records.md・Screen Requirements README・owner-decisions §1〜§9・Review/Approval Rules 本文・Design System 本体 4 資産・token・Component・JSON・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=T5 を機械的推薦 (§8F.6) | Draft |
| 2026-07-22 | T4 記述の正本整合補正 (Task 009-13-F1): PR #89 コードレビュー (issuecomment-5044681317) の 3 指摘に対応。(1) §8F.1 の影響度「高」の根拠を、正本 (review-approval-rules.md §8) に存在しない恒常方針「ルール制定段階で軽微でなければすべて高」の自己導出から、先行 T2 (§8D.1)・T3 (§8E.1) と同一の「本件として明示取得」基準へ修正。(2) §8F.6 の T5 前提条件から「軽微でなければ高が既定」を削除 (review-approval-rules.md §21「高/低の一般的明文判定基準は設けない・本規則で推測補完しない」と整合させ、未取得の Q5 を「既定＝高」と述べない)。同節の必要レビュー主体行も先行推薦節と同じく「Q5 前は未確定 (高/低併記)」へ修正。(3) §8F.3・§8F.4 の NAV-004/NAV-005 の帰属を、定義は navigation.md §4、§6 (Navigation State Model)・§7 (Context Preservation) は適用先である旨を明示するよう精密化。Change Log の T4 行 (本表) の同一表現も本補正に整合。**再分類結果・区分・分類判断・§6.9 精密化・Current Judgment「現時点では開始できない」・保持事項・次工程推薦は変更していない** (記述精度・正本整合の補正のみ)。影響度=高 (Web部責任者、2026-07-22、本件明示取得)。owner-decisions.md・Review/Approval Rules 本文・navigation.md/accommodation-search.md 等の上流成果物・Design System 本体 4 資産・token・Component・JSON・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない | Draft |
| 2026-07-23 | T5 表示・料金・評価論点のスコープ選別・再分類 (Task 009-14): 旧「T5 表示項目・料金・評価仕様」を指示者判断で **「T5 表示・料金・評価論点のスコープ選別・再分類」** へ再定義 (T5 固有の根拠 = SCR-004/SCR-005/IA が既に責務〈SCR-004 §4/§6・SCR-005 §4/§6・IA §5/§6〉と未確定事項/事業仕様〈SCR §16・§13・IA §11〉・対象外〈SCR §13/§15・IA §8/§9〉・SCR-004/005 で異なる IA Object〈SCR-005 は Price/Availability を IA Object としない〉を区別。T2〜T4 の自動適用でない)。T5 の論点を 28 観点へ分解し 10 区分へ個別分類 (§8G 新設)。直接証拠に基づき、Accommodation 識別・比較・評価責務/SCR-004 候補確認・比較/SCR-005 施設確認・評価責務=既存 Draft で明示 (IA §5・SCR-004/005 §2/§4/§6・screen-matrix §5)、具体的属性・表示項目・表示範囲/単位/順序/情報密度・比較成立基準・並び替え/絞り込み/ランキング/掲載順基準=事業・商品・業務仕様 (IA-OBJ-003 Does Not Decide・SCR §16/§13)、Availability 状態/粒度/表示基準/更新時点=事業・商品・業務仕様 (IA-OBJ-006 Does Not Decide・SCR-004 §16、SCR-005 へ追加せず)、Price 構造/対象/表示単位/税/手数料/割引/合計/会員差分/販売条件=事業・商品・業務仕様 (IA-OBJ-007 Does Not Decide・SCR-004 §16、料金計算は対象外)、料金計算/API/DB/在庫/Review 取得/URL/route/キャッシュ/外部サービス=Repository 対象外 (IA §8/§9・SCR §13/§15)、Review 提供元/評価対象/信頼性/尺度/集計=事業・商品・業務仕様 (IA-OBJ-009 Open Issue・SCR §16)、Policy 分類/適用対象/表示基準=事業・商品・業務仕様 (IA-OBJ-008 Open Issue)、事実/条件/販促区別・更新時点/不確実性/変動可能性・空結果/在庫切れ/料金変更=Content・State・CTA 課題 (CTP-004/006/010・SDP-005・Task 009-11 の状態再分類を保持し Error / Interrupted 分割せず新規 State 追加せず)、SCR-004↔005 接続/SCR-005↔006 境界/画面間文脈=Screen Requirements 課題 (SCR §2/§16・screen-matrix §9・SCR-006 未作成、具体データ・遷移は対象外)、モバイル比較/情報構成=UI・Implementation 下流 (既存要求は既存 Draft)、Card/PriceTag/ReviewStars 対応・Card 一覧/詳細用途差=DS 内部整合課題 (C-03/04/05・§6.10、T5 で自動解決しない)、Card 実 px/8 スロット/radius.card/shadow/星実寸/「円」weight=実査/placeholder トラック (R-E・Q2/Q3) として保持、正式命名/ID/Acceptance Criteria 確定主体=Governance 課題、と整理。§6.10 の Remaining Blocking Fact を本粒度へ精密化 (§6.10 の Current Judgment「現時点では開始できない」は不変)。§8F.6 に着手済み注記。表示項目・表示順・情報密度・比較基準・料金体系・価格計算・Review 提供元・評価方式・Card/PriceTag/ReviewStars 採否・一覧/詳細 UI を推測で新規設計せず、表示・料金・評価仕様の確定・SCR-004/005 §16 全解決・SCR-005/006 境界確定・§6.10 全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-23、本件明示取得、PR #83 carve-out 不適用)。遡及は T5 と直接出所に限定し T1〜T4・T6〜T9・他サービスへ一般化しない。§8A.2 T5 (Task 009-8 時点) の記述・Work Order 2〜5・Task 009-6〜009-13-F1 の snapshot/履歴・search-results.md/accommodation-detail.md/information-architecture.md/principles.md/navigation.md/content-principles.md/cta-principles.md/screen-matrix.md/ux-decision-records.md・Screen Requirements README・owner-decisions §1〜§9・Review/Approval Rules 本文・Design System 本体 4 資産 (components.md/design.md/primitive.travel.json/semantic.travel.json)・token・Component・値・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=T6 を機械的推薦 (§8G.6) | Draft |
| 2026-07-23 | T5 記述の整合補正 (Task 009-14-F1): PR #91 コードレビュー (issuecomment-5053501635) の 2 指摘に対応。(1) §8G.4 で観点 (11)「料金計算・会員差分・販売条件」が Price 行 (事業・商品・業務仕様) と料金計算行 (Repository 全体の対象外) の 2 区分へ二重出現していた点を、要素へ分解して精密化 (Price 行の主な観点を「(11 のうち会員差分・販売条件)」、料金計算行を「(11 のうち料金計算)」へ)。§8G.2 に「1 観点が分類先の異なる構成要素を束ねる場合は要素へ分解する」旨と観点 (11) の分解例を明記 (「いずれか」の一括表現を修正)。(2) §6.10 追記 (ii) が Availability・Review・Policy にも「§13」を付与していた点を、§8G.4 の直接証拠列に一致させ「具体的属性・表示項目・Price は §13 も、Availability・Review・Policy は §16 のみ」へ精密化。**再分類結果・区分・分類判断・§6.10 精密化の趣旨・Current Judgment「現時点では開始できない」・保持事項・次工程 (T6) 推薦は変更していない** (記述精度・要約と詳細表の整合補正のみ)。影響度=高 (Web部責任者、2026-07-23、本件明示取得)。owner-decisions.md・Review/Approval Rules 本文・上流成果物・Design System 本体 4 資産・token・Component・値・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない | Draft |
| 2026-07-23 | T6 主要行動・CTA 論点のスコープ選別・再分類 (Task 009-15): 旧「T6 主要行動・CTA」を指示者判断で **「T6 主要行動・CTA 論点のスコープ選別・再分類」** へ再定義 (T6 固有の根拠 = cta-principles.md が既に CTA-001〜010〈§3〉・5 つの CTA 分類〈§4〉・Commitment Level Model〈§5〉・CTA State Model〈§6〉・Navigation↔CTA 境界〈§8〉・画面別 CTA Consideration〈§7〉を区別し、作成済み各 SCR §9 が CTA Requirements を記載、画面別主要 CTA 等を Open Issue〈cta §11・各 SCR §16〉として保持。T2〜T5 の自動適用でない)。T6 の論点を 39 観点へ分解し 10 区分へ個別分類 (§8H 新設)。直接証拠に基づき、CTA-001〜010 の横断責務・5 分類・Commitment Level・CTA State・画面別 CTA 責務・作成済み各 SCR CTA Requirements・情報確認と選択/確約の区別・Navigation↔CTA 境界=既存 Draft で明示 (cta §3〜§8・screen-matrix §5・各 SCR §4/§6/§9・UXDR-TRAVEL-003)、画面別の具体的主要行動・主要/補助の優先関係・具体的対象/結果=Screen Requirements 課題 (各 SCR §9/§16・SDP-010)、会員登録/ログイン誘導・予約/決済/取消/同意/法務表現・Destructive/High-impact の業務行動/確約レベル=事業・商品・業務仕様 (cta §11・CTA-003/004/005・SCR-006〜012 未作成)、CTA 文言/ラベル・状態伝達・販促圧力区別=Content・State・CTA 課題 (CTA-001/007/008/010・CTA State Model、既存原則で責務充足・新 State 追加せず・Error/Interrupted 分割せず・T2/T7 論点を再判断せず)、CTA 数/表示順/視覚的優先順位・モバイル/sticky/固定配置・色/サイズ=UI・Implementation 下流 (既存要求は既存 Draft)、Button/SearchForm 対応・Primary/Secondary↔variant 対応・token=DS 内部整合課題 (C-01・GOV-0002、T6 で自動解決しない。Button/primary variant/SearchForm の存在を主要 CTA 確定根拠にしない)、GOV-0002 provenance・Button state follow-up #4・state/サイズ段階の実測=実査/provenance トラック (R-D/R-E・Q2/Q3、§6.2 を §6.8 へ統合しない)、URL/route/画面遷移/API/DB/処理/認証実装・遷移先=Repository 対象外、SCR-006〜012 未作成=Screen Requirements 課題 (作成/推測せず・CTA 不要と判定せず)、正式命名/ID/AC 確定主体=Governance 課題、と整理。§6.8 の Remaining Blocking Fact を本粒度へ精密化 (§6.8 の Current Judgment「現時点では開始できない」は不変)。§8G.6 に着手済み注記。各画面の主要 CTA・CTA 文言/数/優先順位・予約/決済/取消の行動仕様・SCR-006〜012 の CTA 要件・Button variant 対応・GOV-0002 provenance・Button state を推測で新規設計/確定せず、§6.8 全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-23、本件明示取得、PR #83 carve-out 不適用)。遡及は T6 と直接出所に限定し T1〜T5・T7〜T9・他サービスへ一般化しない。§8A.2 T6 (Task 009-8 時点) の記述・Work Order 2〜5・Task 009-6〜009-14-F1 の snapshot/履歴・cta-principles.md/principles.md/navigation.md/screen-matrix.md/ux-decision-records.md・作成済み 7 件の SCR・Screen Requirements README・owner-decisions §1〜§9・Review/Approval Rules 本文・Design System 本体 4 資産 (components.md/design.md/primitive.travel.json/semantic.travel.json)・token・Component・値・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=T7 を機械的推薦 (§8H.6) | Draft |
| 2026-07-23 | T6 記述の整合補正 (Task 009-15-F1): PR #93 コードレビュー (issuecomment-5054283978) の 1 指摘に対応。§8H.4「Content・State・CTA 課題」行の主な観点に含まれていた誤った観点番号 `(7 の状態伝達適用分)` を削除した (観点 (7) = CTA-006 Reversible Before Irreversible〈可逆性〉であり「状態伝達」に対応しない。状態伝達は観点 (8) CTA-007 Explicit State and Availability)。ただし観点 (8) は横断責務行の (1)〜(11) に既に含まれ、当該行の「状態」は観点 (28)「利用可能・利用不能・処理中等の状態」が表し、CTA-007 は同行の直接証拠列 (CTA-001/007/008/010・CTA State Model) に記載済みであるため、`(8)` へ差し替えると観点 (8) が横断責務行と本行へ二重出現する (009-14-F1 で解消した二重分類の再発)。よって番号誤りの解消と二重分類回避を両立するため冗長な当該サブ参照を削除し、当該行の主な観点を `(26)(28)` とした。**分類結果・区分・分類判断・§6.8 精密化の趣旨・Current Judgment「現時点では開始できない」・保持事項・次工程 (T7) 推薦は変更していない** (観点番号の記述精度補正のみ)。影響度=高 (Web部責任者、2026-07-23、本件明示取得)。owner-decisions.md・Review/Approval Rules 本文・上流成果物・Design System 本体 4 資産・token・Component・値・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない | Draft |
| 2026-07-23 | T7 可逆・回復・支援論点のスコープ選別・再分類 (Task 009-16): 旧「T7 可逆・回復フロー・サポート範囲」を指示者判断で **「T7 可逆・回復・支援論点のスコープ選別・再分類」** へ再定義 (T7 固有の根拠 = principles.md SDP-006・cta-principles.md CTA-006/CTA-TYPE-002/004/005/Commitment Level/CTA State〈§3〜§6〉・navigation.md NVP-004/NAV-005・content-principles.md CTP-003/006/007/010・SCR-013 §4〜§17 が既に可逆・回復・支援の責務と Does Not Decide・Open Issue を区別。T2〜T6 の自動適用でない)。T7 の論点を 60 観点へ分解し 11 区分へ個別分類 (§8I 新設、観点 8/20/25/37/45/51 は要素分解して二重分類回避)。直接証拠に基づき、SDP-006 の Decision/Application・CTA-006・可逆/不可逆区別・Recovery/Secondary/Navigation/Destructive 分類・Commitment Level・CTA State・NVP-004・NAV-005 責務・CTP-003/006/007/010・SCR-013 支援/Recovery 責務=既存 Draft で明示 (principles SDP-006・cta §3〜§8・navigation・content・SCR-013 §4/§6/§9)、保存期間/取消可否/Undo 要否/取消期限/High Commitment・Destructive 業務区分/Help 対象範囲/FAQ/問い合わせ手段/SLA/運用体制/Policy 分類/情報源/User・Booking 関係/認証前後差/処理フロー=事業・商品・業務仕様 (SDP-006・CTA-006 DND・SCR-013 §13/§16・IA-008 OI)、エラー中断専用画面要否/SCR-003 境界/SCR-006〜012 未作成=Screen Requirements 課題 (SCR-003 を境界確認以上に取り込まず・T4 再判断せず・SCR-006〜012 作成/推測せず)、戻り先/再探索/回復手段の具体条件/文脈保持/Contextual・Local・Utility Nav の具体条件/問題解決後の戻り先=Navigation 課題 (NAV-005 保持方式は T1 論点で再判断せず)、再試行/修正/戻る/問い合わせの具体割当/CTA 文言/FAQ 文言/法務文言=Content・State・CTA 課題 (既存原則充足・新 State 追加せず Error/Interrupted 分割せず・T2 再判断せず・brand-content 参照切れを根拠にせず)、確認ダイアログ/CTA 数・配置/モバイル支援導線/Accordion 等 UI=UI・Implementation 下流、Undo 実装/エラー処理仕様/状態遷移/ブラウザバック/セッション/URL/route/API/DB/認証/処理=Repository 対象外、Button/Input/Modal/Overlay 対応/Recovery Action と Component 対応/token=DS 内部整合課題 (C-07/08/09、自動解決せず・未着手 Component を必要 Component へ変換せず)、TVL-0007/GOV-0002 provenance/follow-up #2・#4/Component state 実測=実査・provenance トラック (R-D/R-E・Q2/Q3、§6.2 を統合せず)、brand-content 参照切れ/正式命名/ID/AC 確定主体=Governance 課題、と整理。§6.4/§6.6/§6.12 の Remaining Blocking Fact を本粒度へ精密化 (3 候補の Current Judgment「現時点では開始できない」は不変)。§8H.6 に着手済み注記。可逆・回復フロー・サポート対象範囲・FAQ・問い合わせ・SLA・取消可否・Undo・Recovery Action の具体割当・Button/Input/Modal/Accordion 対応・TVL-0007/GOV-0002 provenance・Button/Input state・brand-content 正本を推測で新規設計/確定/解決せず、§6.4/§6.6/§6.12 全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-23、本件明示取得、PR #83 carve-out 不適用)。遡及は T7 と直接出所に限定し T1〜T6・T8〜T9・他サービスへ一般化しない。§8A.2 T7 (Task 009-8 時点) の記述・Work Order 2〜5・Task 009-6〜009-15-F1 の snapshot/履歴・principles.md/cta-principles.md/navigation.md/content-principles.md/screen-matrix.md/ux-decision-records.md・help-and-support.md/accommodation-search.md・Screen Requirements README・owner-decisions §1〜§9・Review/Approval Rules 本文・Design System 本体 4 資産 (components.md/design.md/primitive.travel.json/semantic.travel.json)・token・Component・値・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=T8 を機械的推薦 (§8I.6) | Draft |
| 2026-07-23 | T7 記述の整合補正 (Task 009-16-F1): PR #95 コードレビュー (issuecomment-5054956880) の 1 指摘に対応。§8I.2 で宣言した観点 (37) の分解「本文正本 = Governance」が §8I.4 の Governance 課題行に反映されておらず (`(37 の本文正本)` が欠落し、事業・商品・業務仕様行には `(37 の分類・情報源)` が存在) 追跡不能だった点を補正。Governance 課題行の主な観点へ `(37 の本文正本)` を追加し、論点に「Policy 本文正本」、直接証拠に「IA-OBJ-008 Open Issue」を追記して、宣言した分解を表で追跡可能にした (009-14-F1・009-15-F1 で確立した「宣言した分解を表で追跡可能にする」原則との整合)。**分類結果・区分・分類判断・§6.4/§6.6/§6.12 精密化の趣旨・3 候補の Current Judgment「現時点では開始できない」・保持事項・次工程 (T8) 推薦は変更していない** (観点分解の追跡漏れの記述精度補正のみ)。影響度=高 (Web部責任者、2026-07-23、本件明示取得)。owner-decisions.md・Review/Approval Rules 本文・上流成果物・Design System 本体 4 資産・token・Component・値・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない | Draft |
| 2026-07-23 | T8 タイポグラフィ論点のスコープ選別・再分類 (Task 009-17): 旧「T8 タイポグラフィ具体規格の扱い」を指示者判断で **「T8 タイポグラフィ論点のスコープ選別・再分類」** へ再定義 (T8 固有の根拠 = content-principles.md CTP-008 が理解可能性・構造・簡潔さ・非視覚依存の責務を Decision/Application として定めつつ具体的アクセシビリティ規格・タイポグラフィ・文字数制限・Component 仕様を Does Not Decide として明示区別し、design.md §3・semantic.travel.json `font.*` が root 16px/rem・2 書体・font family/weight・size scale・line-height scale・`font.body/heading/display/price` を bound 値として既に保持。T2〜T7 の自動適用でない。「上流で具体規格が未定義」と「Design System にもタイポグラフィが存在しない」を同一視しない)。T8 の論点を 70 観点へ分解し 12 区分へ個別分類 (§8J 新設、観点 6/13/28/34/50/52 は要素分解して二重分類回避)。直接証拠に基づき、CTP-008 Decision/Rationale/Application (見出し・情報順序による構造理解・簡潔さ・長文を連続させない責務・色/アイコン/位置の非依存・支援技術での意味保持)・SDP-007=既存 Draft で明示 (CTP-008・SDP-007)、root/rem・font family/weight・size/line-height scale・本文/見出し/Display/詳細施設名/価格の用途・semantic/primitive token・bound の意味・TVL-0001=既存 Design System で明示 (design.md §3・semantic.travel.json)、タイポグラフィ/文字数制限/アクセシビリティ規格/Component 仕様 DND=Service Design の Does Not Decide (不足・欠陥と即断せず)、h1〜h6 具体階層/画面別情報構造/SR 反映要否=Screen Requirements 課題 (画面別 font size・見出し階層を新規設計せず・SCR-006〜012 作成/推測せず)、文字数制限/最小最大/推奨文字数/文章量/見出し文言・コピー/SEO 文字数/法務・Policy 文言/ブランドトーン/Content・Editorial 反映=Content・Editorial 課題 (CTP-008 だけから具体文字数/コピーを確定せず・T7 のトーン/Policy 本文を再判断せず・brand-content 参照切れを根拠にせず)、T9 境界/T9 へ残す具体的適用規格・達成レベル=アクセシビリティ論点 (T9 で確定・T8 で規格/達成レベル/最小 font size/contrast/zoom-reflow を決めず)、上流責務と既存 token の対応/画面別 semantic role 割当/Button・Input・Card・PriceTag 関係/DS 内部整合=DS 内部整合課題 (T8 で自動解決せず・token の存在を上流承認へ昇格せず・token/値を変更せず)、行数/行長/改行/禁則/truncation/line-clamp/overflow/responsive/PC・SP 別値/モバイル具体値/Component 内テキスト制約=UI・Implementation 下流課題 (文字数制限の責務と line-clamp・行数・CMS 入力上限を混同しない)、font fallback 実装/CSS/HTML markup/フォント配信/パフォーマンス/API・DB・CMS 文字数/多言語文字量=Repository 全体の対象外、正式規格・命名・確定主体・Acceptance Criteria=Governance 課題 (未整備・Wiki を正本にしない)、現行画面の実測=実査トラック該当なし (タイポグラフィは TVL-0001 で実測済み・bound ゆえ新規実査/provenance を追加せず・T-03 該当なしと整合)、と整理。判定保留=該当なし。§6.11 の Remaining Blocking Fact を本粒度へ精密化 (§6.11 の Current Judgment「現時点では開始できない」は不変)。§8I.6 に着手済み注記。font size・font family・font weight・line-height・文字数制限・行数・行長・改行/禁則・truncation/line-clamp・responsive/PC・SP 別値を推測で新規設計/確定せず、既存 token を上流承認へ昇格せず・アクセシビリティ適合を確認せず・§6.11 全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-23、本件明示取得、PR #83 carve-out 不適用)。遡及は T8 と直接出所に限定し T1〜T7・T9・他サービスへ一般化しない。§8A.2 T8 (Task 009-8 時点) の記述・Work Order 2〜5・Task 009-6〜009-16-F1 の snapshot/履歴・content-principles.md/principles.md/screen-matrix.md/design.md・作成済み 7 件の SCR・Screen Requirements README・owner-decisions §1〜§9・Review/Approval Rules 本文・Design System 本体 4 資産 (components.md/design.md/primitive.travel.json/semantic.travel.json)・token・Component・値・status・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=T9 を機械的推薦 (§8J.6) | Draft |
| 2026-07-23 | T8 記述の整合補正 (Task 009-17-F1): PR #97 コードレビュー (issuecomment-5055734176) の 3 指摘に対応。(1) §8J.2 で宣言した分解・境界観点が §8J.4 表に未反映で「70 観点はいずれも…分類した」結びと不整合だった点を補正 — (a) 境界観点 (68) T5 価格・表示境界を既存 Design System 行、(69) T7 支援・Content 境界を Content・Editorial 行の主な観点へ明示追加 (各行の残すか列は従前より T5/T7 非再判断を記載済)、(b) 観点 (34) の宣言分解を表で追跡可能化 (DS 内部整合行を `(34 の責務と token の対応)`、Screen Requirements 行へ `(34 の画面別具体割当)` を追加)。判定保留の結びを境界観点の配置明示へ更新 (009-14-F1/009-15-F1/009-16-F1 で確立した「宣言した分解を表で追跡可能にする」原則との整合)。(2) §8J.4 実査トラック行の参照 `§7.9` (文書に存在しない節・Task 仕様側の節番号の誤引用) を `§7 R-E 実査トラック` へ修正。(3) §8J.4 Repository 全体の対象外行の直接証拠を、design.md の実態に合わせて「design.md ヘッダー『実装の所在: GitHub tocoo/tocoo_travel』・本計画 §11 Downstream Impact」へ修正 (design.md §9 は Agent Prompt Guide で実装の所在ではなく、design.md に §11 は存在しないため。結論=Implementation は Repository 対象外は不変)。**分類結果・区分・分類判断・§6.11 精密化の趣旨・Current Judgment「現時点では開始できない」・保持事項・次工程 (T9) 推薦は変更していない** (観点分解の追跡漏れ・参照精度の記述補正のみ)。影響度=高 (Web部責任者、2026-07-23、本件明示取得)。owner-decisions.md・Review/Approval Rules 本文・上流成果物・Design System 本体 4 資産・token・Component・値・status・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない | Draft |
| 2026-07-24 | T9 アクセシビリティ論点のスコープ選別・再分類 (Task 009-18): 旧「T9 アクセシビリティ適用規格の扱い」を指示者判断で **「T9 アクセシビリティ論点のスコープ選別・再分類」** へ再定義 (T9 固有の根拠 = principles.md SDP-007・navigation.md NVP-008・content-principles.md CTP-008・cta-principles.md CTA-009 が理解可能性・操作可能性・非視覚依存・キーボード・支援技術・異なる画面サイズを例外扱いしない責務を Decision/Application として定めつつ、適用規格・達成レベル・実装方式・Component 仕様・focus 実装・HTML 属性・画像仕様を Does Not Decide として明示区別し、作成済み 7 SCR §11 Accessibility Requirements が画面候補ごとの差異を保って責務を明示、design.md §2「WCAG 2.2 AA を最低ライン」記述・`color.focus.ring`・text/brand コントラスト・Input error 非色依存・semantic token・`bound` が既に存在。T2〜T8 の自動適用でない。「WCAG 2.2 AA という記述が存在する」と「適用規格・達成レベルが正式確定している」を同一視せず、「アクセシビリティの上流責務が何も存在しない」とも記載しない)。T9 の論点を 100 観点へ分解し 13 区分へ個別分類 (§8K 新設、観点 18/41/57/59/63/71 は要素分解して二重分類回避)。直接証拠に基づき、SDP-007/NVP-008/CTP-008/CTA-009 の Decision/Rationale/Application (理解可能性・操作可能性・非視覚依存・キーボード・支援技術・異なる画面サイズ・後工程限定にしない・見出し/構造/順序・Navigation/CTA の認識・状態を視覚だけで伝えない)=既存 Draft で明示、作成済み 7 SCR §11 の共通責務・画面候補ごとの差異・入力目的/現在値/状態・候補識別/比較・エラー/回復・支援情報到達・画像/地図/装飾非依存・モバイル到達可能性・SCR-014 画像依存責務・SCR-006〜012 未作成=既存 Screen Requirements で明示、各 Principle の適用規格/達成レベル/実装方式/Component/サイズ基準/フォーカス実装 DND=Service Design の Does Not Decide、SCR の具体規格/達成レベル/HTML 属性/focus 実装/Component/画像・地図仕様 DND=Screen Requirements の Does Not Decide、design.md「WCAG 2.2 AA を最低ライン」記述・R9・`color.focus.ring`・focus outline token・Input error 非色依存・text/brand/非テキストコントラスト記述・semantic color token・`bound`=既存 Design System で明示、WCAG 2.2 AA の正式承認/適用範囲・正式な適用規格/達成レベル・対象画面/Component・例外・Success Criteria・達成基準値・適合判定・適合宣言・検証方法/主体/時点・正本/正式命名/確定主体/AC=アクセシビリティ規格・Governance 課題、既存値と上流責務の対応・design.md/JSON/components.md 間整合=DS 内部整合課題 (T9 で自動解決しない)、モバイル具体 UI・focus 実装/順序・代替テキスト・画像/地図/アイコン仕様・HTML markup・name/role/state・フォーム label/エラー関連付け・live region・zoom/reflow・target size・responsive・motion/reduced motion・読み上げ/操作順序・skip link/landmark=UI・Implementation 下流、実装 Repository・API/DB/認証=Repository 全体の対象外、検証環境・Component state 実査境界・現行画面/keyboard/支援技術/画像 fallback 実査=実査・検証トラック (R-E)、placeholder・実査待ち状態・`$note` コントラスト未達監査・非テキスト未達の個別確認・Button/Input の hover/active/disabled 未取得 (follow-up #4)・画像欠落 fallback=既存 placeholder・実査待ち (T9 の再分類だけで解消しない)、font size/line-height・T8/T4/T5/T6/T7 境界=他 Task 境界 (再判断しない)、と整理。判定保留=該当なし。§6.7 の Remaining Blocking Fact を本粒度へ精密化 (§6.7 の Current Judgment「現時点では開始できない」は不変)。§8J.6 に着手済み注記。適用規格・達成レベル・Success Criteria・基準値・検証方法・適合判定・適合宣言・focus/contrast/keyboard/支援技術の具体仕様を推測で新規策定/確定せず、WCAG 2.2 AA 記述を正式承認済み規格へ昇格せず・既存 DS 表現を適合確認済みへ昇格せず・画像 fallback を解消済みにせず・§6.7 全解消・Alignment 完了・Design System 改定開始可能を宣言しない。影響度=高 (Web部責任者、2026-07-24、本件明示取得、PR #83 carve-out 不適用)。遡及は T9 と直接出所に限定し T1〜T8・他サービスへ一般化しない。§8A.2 T9 (Task 009-8 時点) の記述・Work Order 2〜5・Task 009-6〜009-17-F1 の snapshot/履歴・service-design-alignment-assessment.md/screen-requirements-alignment-assessment.md/alignment-observations-aggregation.md/alignment-amendment-candidate-separation.md/alignment-amendment-readiness-reassessment.md・principles.md/navigation.md/content-principles.md/cta-principles.md・作成済み 7 件の SCR・Screen Requirements README・design.md・owner-decisions §1〜§9・Review/Approval Rules 本文・Design System 本体 4 資産 (components.md/design.md/primitive.travel.json/semantic.travel.json)・token・Component・値・status・version は不変。候補採否・改定要否・改訂着手・設計承認は行っていない。次工程=provenance/参照切れ確認トラック (R-D) を推薦 (§8K.6) | Draft |
| 2026-07-24 | provenance・参照切れ確認トラック (R-D) の整理 (Task 009-19): T1〜T9 再分類一巡後、§8K.6・PR #101 が R-D へ残した provenance 未確認・参照切れ・正本不在を最新 main で全数調査し §8L を新設。GOV-0002・TVL-0001〜0012 は ADR 正本不在ゆえ provenance 未確認 (記述一致を正本確認と同一視しない)、TVL-0004 は現行 bound＋3DS 再認定 (BP1)＋Q5(2026-07-24) が有効だが元 ADR provenance は未確認と区別、TVL-0007 は drawer 統一記述一致だが provenance 未確認 (Modal/drawer 再決定せず)、TVL-0009 は 4 資産に出現せず連番欠落 (意味は推測しない)、brand-content.md・governance/naming-rules.md は不在=参照切れ (作成・置換・代替昇格しない)、follow-up #3 は DS 参照ありだが owner-decisions §3 に記載なし=追跡先不足 (motion 値自体は R-E placeholder)、Source of Truth URL・tocoo/tocoo_travel は外部参照 (内容未検証)、follow-up #2/#4/#5/#13 は owner-decisions §3 に追跡あり値未取得=R-E と整理。provenance 未確認を採用根拠にせず・参照切れを不要参照と即断せず・R-D と R-E を区別。影響度=低 (Web部レビュー担当者、2026-07-24 本件明示取得)。baseline-assessment.md §12 等の過去評価成果物・Work Order 2〜6・Task 009-6〜009-18-BP1 の snapshot/履歴・Service Design/Screen Requirements・design.md/components.md/primitive.travel.json/semantic.travel.json・Rental Car/Inbound DS・owner-decisions.md・review-approval-rules.md は不変。ADR/正本の新規作成・Decision 再認定・Decision ID 採番・token/値/status/version 変更・T1〜T9 再判断・R-E/R-H/R-F 開始・候補採否/改定要否/改訂着手/設計承認は行っていない。次工程=R-D 解消の着手単位・最初に扱う対象の Web部責任者判断の取得を推薦 (§8L.6) | Draft |
