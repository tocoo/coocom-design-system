# Travel Screen Requirements Alignment Assessment

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の作成済み 7 個別 Screen Requirement (SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014) ごとに、上流で確認できる設計責務と既存 Design System 4 成果物 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) の対応を、Repository 内の直接証拠だけで個別に静的評価した記録。Alignment Plan §10 Recommended Work Order の 3 の実行。Screen Requirement 間の横断集約 (Work Order 4)・改訂候補整理 (Work Order 5)・Design System 修正・UX Decision 追加は行わない。
- Position in Repository: `services/travel/design-system/screen-requirements-alignment-assessment.md` — Design System レイヤー (travel サービス配下)。Design System README の Reference Order 上で自身より前に配置される上流成果物は、レイヤー入口 [README.md](README.md)・Alignment 計画 [alignment-plan.md](alignment-plan.md)・Baseline 評価 [baseline-assessment.md](baseline-assessment.md)・Service Design 横断整合性評価 [service-design-alignment-assessment.md](service-design-alignment-assessment.md)。評価対象の Screen Requirements、参照する Service Design 成果物、評価対象となる既存 Design System 4 成果物との関係は本文 Assessment Sources (§5) / Method (§6) / 各 SCR 節 (§12〜§18) に記載し、Position の上流成果物へ混在させない。下流成果物 (Assets / Implementation) との関係は §20 を参照。

本文書は評価記録であり、Design System 仕様・Design Decision の正本ではない。評価上の観察区分 (Alignment Plan §8) を Repository 成果物の正式 Status・優先度・severity と混同しない。ファイル名 `screen-requirements-alignment-assessment.md` は記述的な暫定識別子であり、正式な評価体系名・評価 ID・命名規則を確定しない。SCR ID は Screen Matrix 上の画面候補 ID であり、Screen Requirement 文書 ID・実装画面 ID・URL・route と同一視しない。Fact / Decision / Hypothesis / Open Issue を区別し、新しい Decision を追加しない。

## 1. Purpose

- Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 3「作成済み 7 個別 Screen Requirement ごとの対応確認」を実行する。
- 各 Screen Requirement の設計責務 (User Tasks / Information Responsibilities / Functional / Content / Navigation / CTA / State and Feedback / Accessibility / Constraints / Does Not Decide / Downstream Impact / Open Issues) と既存 Design System 4 成果物の対応を、Alignment Plan §8 の観察区分で記録する。
- 評価結果は Work Order 4 (横断集約) 以降の入力とする。
- 「対応を確認・記録する」ことと「gap を統合する / 改定要否を決める / Design System を修正する」ことを区別する。後者は本文書では行わない (§22)。

## 2. Assessment Snapshot

- Assessment target: 作業開始時点の `main`。
- Assessment snapshot (main commit SHA): `f89ede437a308e716e087d4538455997d9f3e7f3` (PR #49 merge。レビュー対応 `c6c6f76ea5636b4deacb2ca5bd9bb4f7861751ff` を含む)。
- 評価日: 2026-07-16。
- Baseline source: [baseline-assessment.md](baseline-assessment.md)。Cross-cutting source: [service-design-alignment-assessment.md](service-design-alignment-assessment.md)。
- 本評価は Repository 内文書の静的評価であり、実装検証ではない。評価中に main の更新はなく、異なる snapshot を混在させていない。

### 対象 7 個別 Screen Requirement (blob SHA @ `f89ede4`)

| SCR | ファイル | blob SHA |
| --- | --- | --- |
| SCR-001 Service Entry | [../screen-requirements/service-entry.md](../screen-requirements/service-entry.md) | `a389d8e61a95533e72908f8506cbb7a5aa9b220d` |
| SCR-002 Destination Discovery | [../screen-requirements/destination-discovery.md](../screen-requirements/destination-discovery.md) | `e33b3b206961e08670991ee4c8cb7517018e76f0` |
| SCR-003 Accommodation Search | [../screen-requirements/accommodation-search.md](../screen-requirements/accommodation-search.md) | `b90709675e329b304c02dc8dcde8987fe3d2c515` |
| SCR-004 Search Results | [../screen-requirements/search-results.md](../screen-requirements/search-results.md) | `e13c1ec7a63f5548cecb2f108817c1c1bf568ecd` |
| SCR-005 Accommodation Detail | [../screen-requirements/accommodation-detail.md](../screen-requirements/accommodation-detail.md) | `6cf5a6c9317d75d02937b9aa4f2a640ae5a194b0` |
| SCR-013 Help and Support | [../screen-requirements/help-and-support.md](../screen-requirements/help-and-support.md) | `5b8d6f0507681beb0290483b87c2f8bfd8acb212` |
| SCR-014 Editorial Content | [../screen-requirements/editorial-content.md](../screen-requirements/editorial-content.md) | `085faf39856315ea99bb976535b2be4b89f20be6` |

### 対象 Design System 4 成果物 (blob SHA @ `f89ede4`)

| 成果物 | blob SHA |
| --- | --- |
| [design.md](design.md) | `cb9edc16ec1329e33ea0b64fb9789f060ba8bfe9` |
| [semantic.travel.json](semantic.travel.json) | `812c9741343d5f642c9e369fb8d11a398389f474` |
| [primitive.travel.json](primitive.travel.json) | `7dc8f7889a33627370d5b280d486c37b8403ba8b` |
| [components.md](components.md) | `8fa20b88b773c8f302c22728cf46a95549ab458d` |

いずれの Design System 成果物も Draft・version `0.3.0-draft`。

## 3. Scope

- 作成済み 7 個別 Screen Requirement を、すべて独立した対象として評価する。7 件を同一文書に収録するが、評価結果は SCR ごとに分離する (§12〜§18)。
- 各 SCR について、User Tasks / Information Responsibilities / Functional / Content / Navigation / CTA / State and Feedback / Accessibility / Constraints / Does Not Decide / Downstream Impact / Open Issues に現れる設計責務を確認する。
- 各 SCR が参照する Service Design の実在 ID・正式名称 (SDP / IA-OBJ / NVP・NAV / CTP・Content Category / CTA・CTA-TYPE / UXDR-TRAVEL) と、既存 Design System 4 成果物を照合する。

## 4. Out of Scope

- Screen Requirement 間の共通 gap の統合・重複除去・横断的結論・優先順位付け (Work Order 4 以降)。
- gap の severity・対応順、Design System の改定要否、token/component の追加削除、version bump。
- SCR-006〜SCR-012 の評価・要求定義。
- Screen Requirement または Service Design の修正、UX Decision の追加。
- UI 構造・表示項目・表示順・情報密度・API/DB/URL/route。
- 実装 Repository との適合、外部 Repository/実装コード/Assets の調査。

## 5. Assessment Sources

Position の上流成果物 (README / alignment-plan / baseline-assessment / service-design-alignment-assessment) と区別し、本評価が参照する成果物を示す。

- **評価対象の上流 (基準)**: 作成済み 7 個別 Screen Requirement (§2)。各 SCR が §14 Upstream References で参照する Service Design 成果物 SD-001〜SD-007 ([../service-design/](../service-design/README.md))。SD-006 Screen Matrix は画面候補・責務・IA Objects・Navigation Types・Content Categories・Navigation States の確認に参照。
- **評価対象の既存 Design System (直接証拠の対象)**: [design.md](design.md) / [semantic.travel.json](semantic.travel.json) / [primitive.travel.json](primitive.travel.json) / [components.md](components.md)。
- **前提 (証拠品質・制約)**: [alignment-plan.md](alignment-plan.md) (§6 Evidence Rules / §7 Traceability Record Structure / §8 Observation Classification)、[baseline-assessment.md](baseline-assessment.md) (§11 Placeholder and Inspection-Pending Inventory・§12 Provenance and Broken Reference Inventory)、[service-design-alignment-assessment.md](service-design-alignment-assessment.md) (SD 横断責務の対応・部分対応・gap)。

## 6. Method

- Alignment Plan §5 Assessment Unit に従い、評価単位を「上流で確認できる設計責務」とする (Screen Requirement 文書全体・文章 1 行・Component 名の一対一対応ではない)。全文章を機械的に分解しないが、重要な設計責務を省略しない。
- 各 SCR について Alignment Plan §7 の記録構造で Traceability Record を作成し、DS 側の直接証拠 (design.md の節・JSON の token path/`$status`/`$note`・components.md の Component/規則) を照合する。対応する DS 定義が存在しない場合も記録から除外せず該当 Observation として残す。
- 実在する ID・正式名称を直接引用し、存在しない ID・方針名・略称・成果物を作らない。記録行へ新しい恒久 ID を採番しない。
- baseline-assessment.md / service-design-alignment-assessment.md の結論だけを引用して済ませず、各 SCR の責務と DS 側の直接証拠を照合する。ただし横断評価の Observation を全 SCR へ機械的に複製せず、各 SCR の責務に実際に関係するものだけを記録する。

## 7. Evidence Rules

Alignment Plan §6 を厳守する。証拠 = Service Design の実在 ID/正式名称/本文、Screen Matrix の実在記述、個別 Screen Requirement の実在節、Governance 実在成果物、design.md の節、JSON の token path/`$value`/`$status`/`$note`/`$meta`、components.md の Component/variant/状態/Do・Don't/未確定事項、Design System README の現在状態、Baseline/Service Design 評価で記録済みの Fact と制約。証拠として扱わない = ファイル名/Component 名の推測、一般慣行、実装仕様の推測、不在文書の内容、正本のない ADR の想定、Decision ID の存在のみを根拠とする再認定、Downstream Impact の Component 例、Component 存在のみを根拠とする利用要求、Open Issue/Does Not Decide を確定要件へ変換した内容。

## 8. Observation Classification

Alignment Plan §8 の分類だけを使用する: 対応を直接確認できる / 一部のみ確認できる / 対応する定義を確認できない / 過剰 / 矛盾 / placeholder / 実査待ち / provenance 未確認 / 参照切れ / 評価対象外。複数該当時は直接証拠との関係を説明して併記する。

- 「対応を直接確認できる」は要件充足・品質保証・承認完了を意味しない。
- 「対応する定義を確認できない」は新規 Component 追加の Decision を意味しない。
- 「過剰」は削除の Decision を意味しない。
- provenance 未確認の記述を適合確認済みへ昇格させない。
- 数値スコア・適合率・カバレッジ率・件数による合否・pass/fail・severity は導入しない。

### 評価上の必須境界 (全 SCR 共通)

Navigation と CTA を別責務として評価する。Navigation component の存在だけで NAV ID 対応を確定しない。Button の存在だけで CTA 要件対応を確定しない。IA Object を Component/表示項目/データモデルと同一視しない。Content Category を特定 Component/掲載枠と同一視しない。Screen Requirement と Component の 1 対 1 対応を前提としない。上流に具体値要求がない場合、token 値の良否を上流適合として判定しない。`Error / Interrupted` は 1 つの複合状態名として扱い、状態間はカンマで区切る。未定義の状態・業務仕様・表示仕様を追加しない。Acceptance Criteria は各 SCR 文書の整合性確認に参照できるが新しい要件/合否尺度へ変換しない。

## 9. (欠番)

（本文書は §10 を Method 補足に用いず、§11 以降を各 SCR 評価に充てる。以下 §11 Baseline and Cross-cutting Constraints、§12〜§18 が各 SCR 評価。）

## 10. (欠番)

## 11. Baseline and Cross-cutting Constraints

以下を再決定せず、各 SCR 評価の証拠品質・制約として継承する (baseline-assessment.md §11/§12・service-design-alignment-assessment.md)。各 SCR 節では、その SCR の責務に実際に関係する制約のみを記録する。

- **token 参照の内部整合性**: semantic 参照 63/63 解決 (未解決 0)。DS 内部整合は確認済み。
- **placeholder token (計 10)**: semantic `radius.card`/`motion.transition.duration`/`motion.transition.easing`、primitive `shadow.sm/md/lg`/`motion.duration.fast/base/slow`/`motion.easing.standard`。
- **参照切れ**: `brand-content.md` 不在、`governance/naming-rules.md` 不在。
- **provenance 未確認**: GOV-0002・TVL-0001〜TVL-0012 (TVL-0009 は 4 資産に未出現) の ADR 正本なし。Source of Truth URL・実装 Repository `tocoo/tocoo_travel` は外部未検証。
- **component 内部整合性**: 定義済 10 (Button/Input/SearchForm/Card/PriceTag/ReviewStars/Header/Footer/Breadcrumb/Modal)・未着手 5 (Select/Tabs/Toast/Table/Accordion)。
- **SD 横断評価の要点**: CTA State の Pending Confirmation・Navigation State 各状態・NAV/CTA 責務分離の DS 本文規則は「対応する定義を確認できない」。ボタン状態は未取得 (follow-up #4)。

provenance 未確認の記述は、内容が正しい・承認済み・上流適合済みという意味にしない。

## 12. SCR-001 Service Entry Assessment

### Scope and Sources

上流: [service-entry.md](../screen-requirements/service-entry.md) (blob `a389d8e`)。Primary IA: IA-OBJ-001 Destination / IA-OBJ-002 Search Criteria / IA-OBJ-012 Content (Supporting なし)。Navigation Types: NAV-001 / NAV-004 / NAV-006。Content Categories: Identification / Task Guidance / Editorial and Support。Navigation States: Entry, Exploring。DS 側: components.md・semantic/primitive・design.md。

### Traceability Records

| 上流節 / 責務 | 関連 SD ID | DS 側 (節 / token / component) | 直接証拠 | Observation | provenance / placeholder | 矛盾・不足 / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- |
| §4 User Tasks 探索起点 | SDP-001 | components.md Button・Header | Header「ロゴ/ナビゲーション/会員導線」・Button「主 CTA は primary 1 つ」 | 一部のみ確認できる | — | 主要探索行動は SCR-001 §16 Open Issue / §13 Does Not Decide |
| §5 Info Resp. Destination/Search Criteria/Content | IA-OBJ-001/002/012 | components.md SearchForm | SearchForm (検索の起点フォーム) は Search Criteria の表現語彙 | 一部のみ確認できる | — | Destination/Content の専用表現語彙は確認できない。IA Object を Component と同一視しない |
| §8 Nav NAV-001 Global Navigation | NAV-001 | components.md Header | Header 実在。ただし DS に NAV-ID 対応記述なし | 一部のみ確認できる / 対応する定義を確認できない | — | component 存在で NAV-001 対応を確定しない。Global Nav 対象領域は SCR-001 §16 Open Issue |
| §8 Nav NAV-004 Task / NAV-006 Utility | NAV-004/006 | 専用 component の対応記述なし | — | 対応する定義を確認できない | — | Utility/Task Navigation の DS 分類記述なし |
| §9 CTA 探索開始と補助導線を競合させない | CTA-002 | components.md Button Do「主 CTA は primary 1 つに絞る」・variant primary/secondary/ghost/text | Do 記述と責務が一致 | 対応を直接確認できる | variant 語彙 GOV-0002 は provenance 未確認 (適合確定にしない) | 主要 CTA 確定は §13 Does Not Decide |
| §9/§11 CTA-009 / Accessibility 視覚のみ依存しない | CTA-009/SDP-007/NVP-008/CTP-008 | semantic `color.focus.ring`・components.md focus/「色のみで伝えない」 | focus.ring (outline)・数値/テキスト併記 | 一部のみ確認できる | 具体規格未定義 | 適用規格は §13 Does Not Decide |
| §7 Content Identification/Task Guidance/Editorial | CTP-002/005/010 | design.md「特集と通常導線を色で分離」・semantic `color.accent.campaign` 点専用 | Fact/Promotion 分離の記述 | 対応を直接確認できる / 参照切れ | TVL-0012 provenance 未確認。文言正本 `brand-content.md` 不在 | 具体コピーは §13 Does Not Decide |
| §10 State Entry/Exploring | Navigation State Model | semantic `elevation.sticky` 以外に状態表現なし | — | 対応する定義を確認できない | — | 状態 UI 表現は下流後続判断 |

### Observations

- 入口としての役割表現 (Header・Button・SearchForm) は一部のみ確認できる。CTA-002「主 CTA を絞る」は Button の Do 記述と直接一致 (対応を直接確認できる)。NAV-001/004/006 は component 存在のみで NAV-ID 対応を確定できない (対応する定義を確認できない/一部のみ)。

### Provenance / Placeholder / Reference Issues

- GOV-0002 (Button variant)・TVL-0012 (accent) は provenance 未確認。文言表現の正本 `brand-content.md` は参照切れ。ボタン状態は未取得 (follow-up #4, placeholder)。

### Open Issues

- Global Navigation 対象領域 (SCR-001 §16) と DS の Navigation 表現の対応整理。主要探索行動が未定義のため主要 CTA の DS 対応を確定できない。

### Does Not Decide

- Navigation component と NAV-ID の対応確定・主要 CTA の確定・token 値の良否判定は本評価で行わない。

## 13. SCR-002 Destination Discovery Assessment

### Scope and Sources

上流: [destination-discovery.md](../screen-requirements/destination-discovery.md) (blob `e33b3b2`)。Primary IA: IA-OBJ-001 Destination / IA-OBJ-012 Content。Supporting: IA-OBJ-003 Accommodation。Navigation Types: NAV-001 / NAV-002 / NAV-003。Content Categories: Identification / Editorial and Support。Navigation States: Exploring。

### Traceability Records

| 上流節 / 責務 | 関連 SD ID | DS 側 | 直接証拠 | Observation | provenance / placeholder | 矛盾・不足 / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- |
| §5 Destination の発見表現 | IA-OBJ-001 | 専用 component の対応記述なし | — | 対応する定義を確認できない | — | Destination 階層は SCR-002 §16 Open Issue。IA Object を Component と同一視しない |
| §5 Content の発見表現 | IA-OBJ-012 | 専用 component の対応記述なし | — | 対応する定義を確認できない | 文言正本 brand-content.md 参照切れ | Content 分類は SCR-002 §16 Open Issue |
| §5 Supporting Accommodation | IA-OBJ-003 | components.md Card (ResultCard) | Card は Accommodation の表現語彙 | 一部のみ確認できる | — | Supporting を根拠に表示項目を追加しない |
| §8 Nav NAV-001/002/003 | NAV-001/002/003 | components.md Header/Breadcrumb | Header/Breadcrumb 実在だが NAV-ID 対応記述なし | 一部のみ確認できる / 対応する定義を確認できない | — | component 存在で NAV 対応を確定しない |
| §9 CTA 発見と販促を混同しない | CTA-010/CTP-010 | semantic `color.accent.campaign`「点専用・ボタン塗り禁止」・design.md「特集を色で分離」 | 発見と販促の分離を支える記述 | 対応を直接確認できる | TVL-0011/0012 provenance 未確認 | 具体 CTA は §13 Does Not Decide |
| §10 State Exploring | Navigation State Model | 状態表現の対応記述なし | — | 対応する定義を確認できない | — | — |
| §11 Accessibility 視覚のみ依存しない | CTP-008/SDP-007 | components.md「色/アイコン/位置だけに依存させない」・`color.focus.ring` | 記述あり | 一部のみ確認できる | 具体規格未定義 | — |

### Observations

- 発見対象 (Destination/Content) の専用表現語彙は確認できない (対応する定義を確認できない)。Supporting の Accommodation は Card として一部表現可。発見と販促の分離 (CTA-010/CTP-010) は accent 点専用・特集色分離の記述と直接一致 (対応を直接確認できる)。

### Provenance / Placeholder / Reference Issues

- accent 関連 TVL-0011/0012 は provenance 未確認。Content 文言正本 brand-content.md は参照切れ。

### Open Issues

- Destination 階層・Content 分類が未定義のため、発見 UI の DS 対応を確定できない。

### Does Not Decide

- 専用 component の要否・掲載枠と Content Category の同一視は行わない。

## 14. SCR-003 Accommodation Search Assessment

### Scope and Sources

上流: [accommodation-search.md](../screen-requirements/accommodation-search.md) (blob `b907096`)。Primary IA: IA-OBJ-002 Search Criteria / IA-OBJ-001 Destination。Supporting: IA-OBJ-011 User。Navigation Types: NAV-004 / NAV-005。Content Categories: Task Guidance / Identification。Navigation States: Entry, Exploring, Error / Interrupted。

### Traceability Records

| 上流節 / 責務 | 関連 SD ID | DS 側 | 直接証拠 | Observation | provenance / placeholder | 矛盾・不足 / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- |
| §5/§6 Search Criteria 指定・確認・変更 | IA-OBJ-002 | components.md SearchForm・Input | SearchForm「Input 群 + 主 CTA」・Input.default | 一部のみ確認できる | Input 状態一式は実査待ち (follow-up #2) | 入力項目・必須条件・バリデーションは SCR-003 §16 Open Issue |
| §6 条件確認 / 状態可視 | SDP-005/CTA-007 | components.md 状態固定リスト・Input error | error=`color.state.error` 🚧暫定 | 一部のみ確認できる, placeholder | disabled/success は未取得 | — |
| §6/§10 Error / Interrupted 回復 | SDP-006/CTP-007/NAV-005 | components.md Input error text 併記 | 「エラーはテキストメッセージ併記」 | 一部のみ確認できる | — | エラー種別・検証条件は §13 Does Not Decide |
| §8 Nav NAV-004 Task / NAV-005 History and Recovery | NAV-004/005 | 専用 component/history UI の対応記述なし | — | 対応する定義を確認できない | — | 保持方式は NAV-005 Does Not Decide |
| §9 CTA 条件入力・変更・検索開始を明確に | CTA-001/005 | components.md SearchForm「検索実行 CTA は Button.primary」 | 検索開始 CTA の記述 | 対応を直接確認できる | Button variant GOV-0002 provenance 未確認 | 主要 CTA 確定は §13 Does Not Decide |
| §5 Supporting User | IA-OBJ-011 | 認証/会員 component なし (未着手にも該当なし) | — | 対応する定義を確認できない | — | 認証・会員・履歴保存を取り込まない (上流制約) |
| §11 Accessibility | CTP-008/CTA-009 | `color.focus.ring`・「色のみで伝えない」 | 記述あり | 一部のみ確認できる | 具体規格未定義 | — |

### Observations

- 検索起点の表現 (SearchForm/Input) と検索開始 CTA (Button.primary) は直接証拠あり (SearchForm の記述は対応を直接確認できる)。ただし Input の状態一式・入力仕様は実査待ち/Open Issue で一部のみ。NAV-004/005 の DS 対応記述はない。

### Provenance / Placeholder / Reference Issues

- Input 状態は follow-up #2 実査待ち・error は暫定 placeholder。Button variant GOV-0002 provenance 未確認。

### Open Issues

- 入力項目・バリデーション・条件保持方式が未定義のため、SearchForm/Input の具体対応を確定できない。

### Does Not Decide

- 入力項目・必須条件・バリデーション・履歴保持 UI の確定は行わない。

## 15. SCR-004 Search Results Assessment

### Scope and Sources

上流: [search-results.md](../screen-requirements/search-results.md) (blob `e13c1ec`)。Primary IA: IA-OBJ-002 Search Criteria / IA-OBJ-003 Accommodation。Supporting: IA-OBJ-006 Availability / IA-OBJ-007 Price / IA-OBJ-009 Review / IA-OBJ-008 Policy。Navigation Types: NAV-002 / NAV-003 / NAV-004 / NAV-005。Content Categories: Identification / Decision Support / Conditions and Policies。Navigation States: Exploring, Evaluating, Error / Interrupted。

### Traceability Records

| 上流節 / 責務 | 関連 SD ID | DS 側 | 直接証拠 | Observation | provenance / placeholder | 矛盾・不足 / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- |
| §5/§6 Accommodation 候補の確認・比較 | IA-OBJ-003 | components.md Card (ResultCard, 8 スロット) | Card「検索結果の宿泊施設カード」slot media/title/meta/rating/price/badge/description/actions | 一部のみ確認できる | 実 px・8 スロット対応付けは実査待ち (🚧)・`radius.card` placeholder・shadow placeholder | 表示項目・表示順は SCR-004 §16 Open Issue。Downstream Impact の Card 例を採用決定としない |
| §7 Decision Support Price/Review | IA-OBJ-007/009 (Supporting) | components.md PriceTag・ReviewStars・semantic `color.icon.rating` | PriceTag (価格表現)・ReviewStars (評価表現) | 一部のみ確認できる | 「円」weight 正規化は ❓ | Supporting を根拠に業務モデルを追加しない |
| §7 Conditions and Policies | IA-OBJ-008 (Supporting) | 専用 component の対応記述なし | — | 対応する定義を確認できない | — | Policy 分類は取り込まない |
| §7 根拠のない人気/希少性を表現しない | CTP-004/CTP-006 | design.md「根拠のない人気・ランキング・限定・希少性を確定情報として扱わない」 | 記述あり | 対応を直接確認できる | — | ランキング基準は §13 Does Not Decide |
| §8 Nav NAV-002/003/004/005 | NAV-002/003/004/005 | Breadcrumb 等はあるが NAV-ID 対応記述なし | — | 対応する定義を確認できない / 一部のみ | — | component 存在で NAV 対応を確定しない |
| §10 State Exploring/Evaluating/Error / Interrupted | Navigation State/CTP-006 | components.md 状態固定リスト・`color.state.*` | error/success token | 一部のみ確認できる | motion placeholder | 空結果・在庫切れ挙動は §13 Does Not Decide |
| §9 CTA 比較・詳細確認・条件変更・選択の優先関係 | CTA-002/005 | components.md Button・PriceTag (条件併記構造) | Button・条件併記 | 一部のみ確認できる | GOV-0002 provenance 未確認 | 主要 CTA 確定は §13 Does Not Decide |

### Observations

- 候補提示・価格・評価の表現語彙 (Card/PriceTag/ReviewStars) が存在し一部のみ確認できる。ただし Card の実 px/8 スロット対応付けは実査待ち・`radius.card`/shadow は placeholder。根拠なき人気表現の排除 (CTP-004) は design.md 記述と直接一致。並び替え/絞り込み/ランキング基準は Open Issue のため DS 対応を確定できない。Downstream Impact に列挙された Card/PriceTag/ReviewStars を採用決定と解釈しない。

### Provenance / Placeholder / Reference Issues

- `radius.card`・shadow・motion は placeholder。Card 8 スロット・実 px は実査待ち。PriceTag「円」weight は ❓。

### Open Issues

- 表示基準・並び替え・絞り込み・比較成立基準が未定義のため、候補一覧 UI の DS 対応を確定できない。

### Does Not Decide

- 一覧 UI・表示項目・ランキングの確定、Card の採用決定は行わない。

## 16. SCR-005 Accommodation Detail Assessment

### Scope and Sources

上流: [accommodation-detail.md](../screen-requirements/accommodation-detail.md) (blob `6cf5a6c`)。Primary IA: IA-OBJ-003 Accommodation。Supporting: IA-OBJ-001 Destination / IA-OBJ-004 Room / IA-OBJ-005 Stay Plan / IA-OBJ-009 Review / IA-OBJ-008 Policy / IA-OBJ-012 Content (Price/Availability は非追加)。Navigation Types: NAV-002 / NAV-003 / NAV-004 / NAV-006。Content Categories: Identification / Decision Support / Conditions and Policies / Editorial and Support。Navigation States: Evaluating, Error / Interrupted。

### Traceability Records

| 上流節 / 責務 | 関連 SD ID | DS 側 | 直接証拠 | Observation | provenance / placeholder | 矛盾・不足 / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- |
| §5/§6 Accommodation 情報確認・評価 | IA-OBJ-003 | components.md Card | Card は Accommodation の表現語彙 (検索結果向け) | 一部のみ確認できる | Card 実査待ち | 施設詳細の表示項目は SCR-005 §16 Open Issue |
| §7 Decision Support Review | IA-OBJ-009 (Supporting) | components.md ReviewStars・`color.icon.rating` | ReviewStars (表示のみ・数値併記) | 一部のみ確認できる | 星実寸は実査待ち | 提供元・評価対象は取り込まない |
| §6/§7 Conditions and Policies (Policy) | IA-OBJ-008 (Supporting)/CTP-003 | 専用 component の対応記述なし | — | 対応する定義を確認できない | — | Policy 分類は取り込まない |
| §5 Room/Stay Plan の確認 | IA-OBJ-004/005 (Supporting) | 専用 component の対応記述なし | — | 対応する定義を確認できない | — | 業務モデルは Open Issue。SCR-006 選択を取り込まない |
| §8 Nav NAV-002/003/004/006 関連情報への移動 | NAV-002/003 | components.md Breadcrumb/Header | 実在だが NAV-ID 対応記述なし | 一部のみ確認できる / 対応する定義を確認できない | — | Utility Nav 対象は Open Issue |
| §9 CTA 情報確認と Room/Stay Plan 選択を区別 | CTA-002/CTA-004 | components.md Button variant | Button (variant で主/補助区別) | 一部のみ確認できる | GOV-0002 provenance 未確認 | 選択・確約・予約開始は SCR-005 で定義しない (上流) |
| §7 Editorial and Support 事実と販促分離 | CTP-010 | semantic accent 点専用・design.md 特集色分離 | 記述あり | 対応を直接確認できる | TVL-0012 provenance 未確認 | — |
| §10 State Evaluating/Error / Interrupted | Navigation State | 状態表現の対応記述なし | — | 対応する定義を確認できない | — | — |

### Observations

- 施設・評価の表現語彙 (Card/ReviewStars) は一部のみ確認できる (Card は検索結果向けで詳細用途は実査待ち)。事実/販促分離 (CTP-010) は直接一致。Room/Stay Plan/Policy の専用表現は確認できない (業務モデルが Open Issue のため妥当)。情報確認と選択の区別 (CTA) は Button variant で一部表現可だが GOV-0002 provenance 未確認。

### Provenance / Placeholder / Reference Issues

- ReviewStars 星実寸・Card は実査待ち。accent TVL-0012・Button GOV-0002 provenance 未確認。

### Open Issues

- Room/Stay Plan/Price/Availability の業務モデルと SCR-005/SCR-006 境界が未定義のため、関連情報表現の DS 対応を確定できない。

### Does Not Decide

- Room/Stay Plan 選択 UI・Policy 分類の確定は行わない (上流でも Open Issue)。

## 17. SCR-013 Help and Support Assessment

### Scope and Sources

上流: [help-and-support.md](../screen-requirements/help-and-support.md) (blob `5b8d6f0`)。Primary IA: IA-OBJ-012 Content / IA-OBJ-008 Policy。Supporting: IA-OBJ-011 User / IA-OBJ-010 Booking。Navigation Types: NAV-001 / NAV-002 / NAV-003 / NAV-006。Content Categories: Editorial and Support / Conditions and Policies。Navigation States: Entry, Exploring, Error / Interrupted。

### Traceability Records

| 上流節 / 責務 | 関連 SD ID | DS 側 | 直接証拠 | Observation | provenance / placeholder | 矛盾・不足 / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- |
| §6 支援への到達 / 補助情報 | NAV-006 | 専用 component の対応記述なし | — | 対応する定義を確認できない | — | サポート対象範囲は SCR-013 §16 Open Issue |
| §7 Editorial and Support / Conditions and Policies | CTP-003/006/010 | 文言正本 brand-content.md 不在・専用 component なし | — | 参照切れ / 対応する定義を確認できない | brand-content.md 参照切れ | FAQ/Policy 本文は §13 Does Not Decide |
| §9 CTA Recovery Action | CTA-TYPE-004/CTA-007 | components.md 状態 (error/loading) は fixed list にあるが Recovery Action 用の component/規則なし | — | 対応する定義を確認できない / 一部のみ | ボタン状態未取得 (follow-up #4) | 問い合わせ手段・処理フローは Open Issue |
| §8 Nav NAV-001/002/003/006 | NAV-001/002/003/006 | Header/Breadcrumb 実在だが NAV-ID 対応記述なし | — | 一部のみ確認できる / 対応する定義を確認できない | — | component 存在で NAV 対応を確定しない |
| §13 Does Not Decide の Accordion 等 | — | components.md 未着手: Accordion | Accordion は未着手 (実体皆無) と明記 | 対応する定義を確認できない | — | SR §15 で Accordion 等を指定しない。未着手を必要性へ変換しない |
| §10 State Entry/Exploring/Error / Interrupted | Navigation State/CTP-007 | 状態表現の対応記述なし | — | 対応する定義を確認できない | — | — |
| §11 Accessibility | CTP-008/CTA-009 | `color.focus.ring`・「色のみで伝えない」 | 記述あり | 一部のみ確認できる | 具体規格未定義 | — |

### Observations

- 支援領域の表現語彙 (FAQ/問い合わせ/Support) に対応する DS component は確認できない (Accordion 等は未着手と明記。SR も Downstream Impact で Accordion 等を指定しないと明記)。未着手 component の存在を必要性へ変換しない。Recovery Action (CTA-TYPE-004) に対応する DS 側の Recovery 用 component/規則は確認できない。文言表現の正本 brand-content.md は参照切れ。

### Provenance / Placeholder / Reference Issues

- brand-content.md 参照切れ。ボタン状態未取得 (follow-up #4)。

### Open Issues

- サポート対象範囲・問い合わせ手段・FAQ 構成が未定義のため、支援 UI の DS 対応を確定できない。

### Does Not Decide

- Accordion/フォーム/チャット/モーダル等の採用・追加は行わない (未着手 component の必要性評価は後続)。

## 18. SCR-014 Editorial Content Assessment

### Scope and Sources

上流: [editorial-content.md](../screen-requirements/editorial-content.md) (blob `085faf3`)。Primary IA: IA-OBJ-012 Content。Supporting: IA-OBJ-001 Destination / IA-OBJ-003 Accommodation。Navigation Types: NAV-001 / NAV-002 / NAV-003。Content Categories: Editorial and Support / Identification。Navigation States: Entry, Exploring, Evaluating (Error / Interrupted 非含有)。

### Traceability Records

| 上流節 / 責務 | 関連 SD ID | DS 側 | 直接証拠 | Observation | provenance / placeholder | 矛盾・不足 / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- |
| §5/§6 Content の発見・理解 | IA-OBJ-012 | 文言正本 brand-content.md 不在・専用 component なし | — | 参照切れ / 対応する定義を確認できない | brand-content.md 参照切れ | Content 分類は SCR-014 §16 Open Issue |
| §5 Supporting Destination/Accommodation | IA-OBJ-001/003 | components.md Card | Card は Accommodation の表現語彙 | 一部のみ確認できる | — | 施設詳細機能を取り込まない |
| §7/§9 編集情報と販促の区別 | CTP-010/CTA-010 | semantic accent 点専用・design.md 特集色分離 | 「編集情報と予約・販促 CTA の性質を区別」に対応する記述 | 対応を直接確認できる | TVL-0011/0012 provenance 未確認 | 販促施策は §13 Does Not Decide |
| §7 CTP-004 根拠のない優位性/人気を表現しない | CTP-004 | design.md「根拠のない人気・ランキングを確定情報として扱わない」 | 記述あり | 対応を直接確認できる | — | — |
| §8 Nav NAV-001/002/003 | NAV-001/002/003 | Header/Breadcrumb 実在だが NAV-ID 対応記述なし | — | 一部のみ確認できる / 対応する定義を確認できない | — | component 存在で NAV 対応を確定しない |
| §10 State Entry/Exploring/Evaluating | Navigation State | 状態表現の対応記述なし | — | 対応する定義を確認できない | — | Error / Interrupted を独断追加しない (上流に非含有) |
| §11 Accessibility 画像/装飾なしでも理解可能 | CTP-008 | components.md「色・画像・位置だけに意味を依存させない」・design.md 画像比率 (object-fit) | 記述あり | 一部のみ確認できる | 画像欠落 fallback は ❓ 実査待ち | 画像仕様は §13 Does Not Decide |

### Observations

- 編集情報と販促の区別 (CTP-010/CTA-010)・根拠なき人気表現の排除 (CTP-004) は accent 点専用・特集色分離・design.md 記述と直接一致 (対応を直接確認できる)。Content の発見・理解の文言表現の正本 brand-content.md は参照切れ。Supporting の Accommodation は Card として一部表現可。画像欠落 fallback は実査待ち。

### Provenance / Placeholder / Reference Issues

- brand-content.md 参照切れ。accent TVL-0011/0012 provenance 未確認。画像欠落 fallback は ❓ 実査待ち (design.md §6)。

### Open Issues

- Content 分類・編集方針が未定義のため、Content 表現の DS 対応を確定できない。

### Does Not Decide

- Content 分類・掲載枠と Content Category の同一視・画像仕様の確定は行わない。

## 19. Work Order 3 Completion Boundary

- 上記 7 件 (SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014) すべての独立評価を §12〜§18 に記録した。よって Work Order 3 を Draft として実施済みとする。
- 本文書は 7 件の評価結果を横断集約する節を持たない。共通 gap の統合・重複除去・優先順位付けは行っていない。
- 次は本文書で実施しない: Work Order 4 (観察結果の横断集約) / Work Order 5 (改訂候補と未解決事項の分離) / Work Order 6 (実際の改訂タスクを開始できるかの判断)。
- 「Work Order 3 実施済み」は、Alignment 全体の完了・Design System 適合・改定可能・承認済みを意味しない。

## 20. Downstream Impact

- **Assets** ([../assets/README.md](../assets/README.md)) — `Not started`。本評価の対象外。
- **Implementation** — Repository 管理対象外。本評価は静的評価であり実装検証ではない。DS から実装画面・URL・route を導出しない。各 SCR の Downstream Impact に列挙された Component 例を採用決定と解釈しない。

## 21. Open Issues

以下は未決である。解決策は推測して記載しない。

- 各 SCR 節に記録した個別 Open Issue の承認・反映主体、および Work Order 4 (横断集約) への引き継ぎ方法。
- 各 SCR で「対応する定義を確認できない」とした責務 (専用表現語彙の不在・NAV/CTA/Content 分類との対応・状態表現) の扱い。
- placeholder / 実査待ち (Card 実 px・ボタン状態 follow-up #4・motion・shadow 等) の解決。
- 参照切れ (`brand-content.md`・`governance/naming-rules.md`)・provenance 未確認 (GOV-0002・TVL) の解決主体。
- 未着手 component (Accordion 等) の必要性評価 (Work Order 以降)。

## 22. Does Not Decide

- Screen Requirement 間の共通 gap/重複の統合、gap の優先順位・severity・対応順。
- Design System の改定要否・token 値/名/階層/命名規則・placeholder の解消方法。
- component の追加/削除/統合/分割・component API/variant/state/実装仕様。
- Screen Requirement または Service Design の修正・SCR-006〜SCR-012 の要求。
- UI 構造・表示項目・表示順・情報密度・API/DB/URL/route・実装 Repository との適合。
- 参照切れ文書の内容・provenance 未確認事項の正当性・正式な評価 ID/ファイル名/評価体系・UX Decision の追加。
- 「対応を直接確認できる」を要件充足・承認完了へ、「対応する定義を確認できない」を新規 component 追加 Decision へ、「過剰」を削除 Decision へ変換しない。

## 23. Relationship to Subsequent Work

- 本評価 (Work Order 3) は、Alignment Plan §10 の次段である Work Order 4「観察結果の横断集約」の入力となる。
- Work Order 4 は本 PR のマージ前には開始しない。
- 改訂候補と未解決事項の分離 (Work Order 5)・改訂着手可否の判断 (Work Order 6) は、Work Order 4 の後に成立する。
- 本評価は Design System の修正・新しい UX Decision を含まない。改定は後続タスクの承認を前提とする。

## 24. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial assessment (Work Order 3): 作成済み 7 個別 Screen Requirement (SCR-001/002/003/004/005/013/014) ごとに設計責務と既存 Design System 4 成果物の対応を Repository 内直接証拠だけで個別に静的評価。横断集約・改定・UX Decision 追加は未実施 | Draft |
| 2026-07-17 | 用語統一: Work Order 5 を指す概念語 (候補) の「改訂」表記を正式名称 (alignment-plan.md §10) へ揃えた (§3 Scope)。DS 変更行為・状態を指す用法 (要否・可能・Design System の改定) は維持。評価内容・観察区分・各 SCR の Traceability は不変 | Draft |
