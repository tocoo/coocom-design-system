# Travel Service Design Alignment Assessment

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Service Design 横断的設計責務 (SD-001〜SD-005・SD-007) と既存 Design System 4 成果物 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) の対応を、Repository 内の直接証拠だけで静的評価した記録。Alignment Plan §10 推奨作業順 2 の実行。個別 Screen Requirement の評価・Design System の修正・UX Decision の追加は行わない。
- Position in Repository: `services/travel/design-system/service-design-alignment-assessment.md` — Design System レイヤー (travel サービス配下)。Design System README の Reference Order 上で自身より前に配置される上流成果物は、レイヤー入口 [README.md](README.md)・Alignment 計画 [alignment-plan.md](alignment-plan.md)・Baseline 評価 [baseline-assessment.md](baseline-assessment.md)。評価対象の Service Design 成果物および既存 Design System 4 成果物との関係は本文 Assessment Sources (§4) / Method (§5) / Service Design Alignment Assessment (§8) 等に記載し、Position の上流成果物へ混在させない。下流成果物 (Assets / Implementation) との関係は §13 を参照。

本文書は評価記録であり、Design System 仕様・Design Decision の正本ではない。評価上の観察区分 (Alignment Plan §8) を Repository 成果物の正式 Status と混同しない。ファイル名 `service-design-alignment-assessment.md` は暫定識別子であり、正式な評価体系名・命名規則・評価 ID を確定しない。本評価は Repository 内文書の静的評価であり、実装検証ではない。Fact / Decision / Hypothesis / Open Issue を区別し、新しい Decision を追加しない。

## 1. Purpose

- Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 2「Service Design の横断原則と既存 Design System の対応確認」を実行する。
- Service Design 成果物 (SD-001〜SD-005・SD-007) に定義された横断的設計責務が、既存 Design System 4 成果物によって「対応を直接確認できる / 一部のみ確認できる / 対応する定義を確認できない / 過剰 / 矛盾 / placeholder / 実査待ち / provenance 未確認 / 参照切れ / 評価対象外」のどれに該当するかを、Repository 内の直接証拠だけで記録する。
- 評価結果は、後続の個別 Screen Requirement 整合性評価 (Work Order 3) と改定候補整理 (Work Order 5) の入力とする。
- 「対応を確認・記録する」ことと「Design System を修正する / 適合を判定する / 改定要否を決める」ことを区別する。後者は本文書では行わない (§17)。

## 2. Assessment Snapshot

- Assessment target: 作業開始時点の `main`。
- Assessment snapshot (main commit SHA): `835c42791cb3256e5085ddc8dc1fc278b5d68cb3` (PR #47 merge)。
- 評価日: 2026-07-16。
- Baseline source: [baseline-assessment.md](baseline-assessment.md) (評価 commit `0d446152`)。既存 4 資産はいずれも Draft・version `0.3.0-draft`。
- 本評価は Repository 内文書の静的評価であり、実装検証ではない。評価中に main の更新はない。

## 3. Scope

- Service Design 横断的設計責務の評価対象: SD-001 Service Design Principles ([../service-design/principles.md](../service-design/principles.md))・SD-002 Information Architecture ([../service-design/information-architecture.md](../service-design/information-architecture.md))・SD-003 Navigation ([../service-design/navigation.md](../service-design/navigation.md))・SD-004 Content Principles ([../service-design/content-principles.md](../service-design/content-principles.md))・SD-005 CTA Principles ([../service-design/cta-principles.md](../service-design/cta-principles.md))・SD-007 UX Decision Records ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md))。
- SD-006 Screen Matrix ([../service-design/screen-matrix.md](../service-design/screen-matrix.md)) は、画面候補・責務・状態および個別 Screen Requirement との境界を確認するコンテキストとしてのみ参照する。
- 評価対象の既存 Design System 成果物: `design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`。

## 4. Out of Scope

- 個別 Screen Requirement 7 件 (SCR-001〜SCR-005・SCR-013・SCR-014) との整合性評価、SCR 単位の対応表 (Work Order 3 以降)。
- SCR-006〜SCR-012 の要求定義。
- Screen Matrix の各画面候補を Design System component へ割り当てること。
- Screen Matrix の画面候補を実装画面・URL・route とみなすこと。
- Service Design の未解決 Open Issue を Design System 要求へ変換すること。
- Design System の改定要否・token/component の追加削除・version bump・UX Decision の追加 (§17)。

## 5. Assessment Sources

Position の上流成果物 (§Position: README / alignment-plan / baseline-assessment) と区別し、本評価が参照する成果物を以下に列挙する。

### 上流 Service Design (評価の基準)

- SD-001〜SD-005・SD-007 (§3)。SD-006 はコンテキスト参照のみ。各文書はすべて文書全体 Status が Draft。含まれる横断的 ID: SDP-001〜010 / IA-OBJ-001〜012 / NVP-001〜008・NAV-001〜006・Navigation State Model / CTP-001〜010・Content Categories (6)・Status and Uncertainty Model / CTA-001〜010・CTA-TYPE-001〜005・Commitment Level Model・CTA State Model / UXDR-TRAVEL-001〜003 (いずれも Record Status Accepted)。

### 評価対象 既存 Design System (直接証拠の対象)

- [design.md](design.md)・[semantic.travel.json](semantic.travel.json)・[primitive.travel.json](primitive.travel.json)・[components.md](components.md)。すべて Draft 0.3.0-draft。

### 前提 (証拠品質・制約)

- [alignment-plan.md](alignment-plan.md) (§6 Evidence Rules / §8 Observation Classification / §10 Work Order)。
- [baseline-assessment.md](baseline-assessment.md) (§11 Baseline Constraints で継承)。

## 6. Method

- Alignment Plan §6 Evidence Rules と §5 Assessment Unit に従い、評価単位を「上流で定義された設計責務」とする (文書または component の一対一対応ではない)。
- 各 Service Design 成果物の横断的責務 (ID・節) を起点に、既存 Design System 側の直接証拠 (design.md の節・JSON の token path/`$status`/`$note`・components.md の Component/規則) を照合し、Alignment Plan §8 の観察区分で記録する (§8)。
- 実在する ID と正式名称を直接引用し、存在しない ID・方針名・略称を作らない。
- 一般的な UX 慣行を補完根拠にしない。上流に具体値要求がない場合、token 値の良否を上流適合として評価しない。
- component が存在することを、その component の利用要求・上流適合の確定としない。一致して見えても provenance 未確認の事項を適合確定にしない。
- Navigation と CTA を別の設計責務として評価する (UXDR-TRAVEL-003)。`Error / Interrupted` は 1 つの複合状態名として扱い、状態間はカンマで区切る。

## 7. Evidence Rules

Alignment Plan §6 を継承する。上流証拠 = Service Design の実在 ID・正式名称・本文、Screen Matrix の画面候補・責務 (コンテキスト)、Governance 実在成果物。Design System 側証拠 = design.md の節、JSON の token path/`$value`/`$status`/`$note`、components.md の Component/variant/状態/Do・Don't/未確定事項。証拠として扱わないもの = ファイル名/component 名からの推測、一般慣行、実装仕様の推測、不在文書の内容、正本のない ADR の想定、Decision ID の存在のみを根拠とする再認定、component 存在の利用要求化。

## 8. Service Design Alignment Assessment

観察区分は Alignment Plan §8 のもののみ使用する。複数該当時は直接証拠との関係を説明して併記する。数値スコア・適合率・pass/fail・severity は導入しない。

### 8.1 SD-001 Service Design Principles (SDP-001〜010)

| 設計責務 (ID) | DS 側直接証拠 (artifact / path・component) | 観察区分 | provenance / placeholder | Conflict or gap / Does Not Decide |
| --- | --- | --- | --- | --- |
| SDP-001 User Task Clarity | components.md Button「1 画面の主 CTA は primary 1 つに絞る」・Breadcrumb「現在地はリンク化しない」 | 一部のみ確認できる (役割表現の語彙はあるが、タスク明確性の成立は画面単位) | — | 画面別のタスク明確性は Screen Requirements 側 (SDP-001 Does Not Decide: 導線/CTA 文言/画面数) |
| SDP-002 Progressive Commitment | DS 側に確約時期を扱う横断 token/component を確認できない | 対応する定義を確認できない | — | フロー・確約時期は DS が決めない (SDP-002 Does Not Decide) |
| SDP-003 Transparent Conditions | components.md PriceTag「税・条件の補助テキストを必ず併記できる構造」・semantic `color.accent.campaign`「バッジ/割引ラベルの点専用・ボタン塗り禁止 (TVL-0012)」 | 一部のみ確認できる | TVL-0012 は provenance 未確認 (ADR 正本なし) | 価格構造・Policy 分類は決めない (SDP-003 Does Not Decide) |
| SDP-004 Consistent Mental Model | semantic token の用途ベース命名・components.md「状態の固定リスト hover/active/focus/disabled/loading/error/success」 | 一部のみ確認できる | 命名規則正本 `governance/naming-rules.md` が参照切れ (§14) | 正式な用語・命名規則は決めない (SDP-004 Does Not Decide) |
| SDP-005 State Visibility | components.md 状態固定リスト・semantic `color.state.success`/`color.state.error` | 一部のみ確認できる, placeholder | ボタン状態は未取得 (follow-up #4)・motion は placeholder | 状態の具体一覧・予約状態の業務定義は決めない (SDP-005 Does Not Decide) |
| SDP-006 Recoverability | components.md Input「エラーはテキストメッセージ併記」・Modal / Overlay | 一部のみ確認できる | Input 状態一式は実査待ち (follow-up #2) | 保存期間・Undo・エラー処理仕様は決めない (SDP-006 Does Not Decide) |
| SDP-007 Accessibility by Default | design.md §2「WCAG 2.2 AA を最低ライン」・semantic `color.focus.ring`・components.md「色のみで伝えない (ReviewStars 数値併記 / Input エラーテキスト併記)」 | 対応を直接確認できる (DS 内部に既定としての記述あり), 一部のみ確認できる (具体規格・達成レベルは未定義) | 一部コントラストは用途により未達可能性を JSON `$note` が自認 (`color.border.default`) | 適用規格・達成レベル・実装方式は決めない (SDP-007 Does Not Decide) |
| SDP-008 Evidence over Assumption | JSON `$status: placeholder` + `$note` (未取得を確定値化しない)・design.md「根拠のない人気・ランキングを確定情報として扱わない」 | 対応を直接確認できる (DS 内部の運用) | placeholder token 計 10 (baseline 継承) | 調査方法・Evidence 保存形式は決めない (SDP-008 Does Not Decide) |
| SDP-009 Service-wide Coherence | baseline で確認した DS 内部整合性 (semantic→primitive 参照 63/63 解決)・design.md「独立 DS・他サービスと値を共有しない (R1)」 | 対応を直接確認できる (DS 内部整合) | — | 画面構成・共通 Component 範囲は決めない (SDP-009 Does Not Decide) |
| SDP-010 Incremental Definition | design.md「実査待ち placeholder 維持 (TVL-0008)」・JSON placeholder を維持 | 対応を直接確認できる (DS 内部の運用) | TVL-0008 は provenance 未確認 | 優先順位・暫定仕様の期限は決めない (SDP-010 Does Not Decide) |

### 8.2 SD-002 Information Architecture (IA-OBJ-001〜012)

IA Object を UI・component・データモデルと同一視しない。IA §8「実装側が本 IA をそのまま DB モデルとして使用してはならない」・§9 Boundary「IA に含まない: UI/Component/API/DB」・§10「Design System は各情報オブジェクトや状態を UI として表現する設計語彙を提供する」。以下は横断的な表現責務に関する直接証拠のみを評価する。既存 Design System が IA Object の内容・属性・関係・業務仕様を決定しているとは推測しない。

| 設計責務 (IA-OBJ) | DS 側直接証拠 | 観察区分 | 備考 |
| --- | --- | --- | --- |
| IA-OBJ-002 Search Criteria の表現 | components.md SearchForm (検索の起点フォーム) | 一部のみ確認できる | SearchForm の存在は表現語彙であり、Search Criteria の入力項目・業務仕様の決定ではない (IA-OBJ-002 Does Not Decide) |
| IA-OBJ-003 Accommodation の表現 | components.md Card (ResultCard, 8 スロット) | 一部のみ確認できる | Card の存在は表現語彙であり、Accommodation の正式属性一覧の決定ではない (IA §11 Open Issue) |
| IA-OBJ-007 Price の表現 | components.md PriceTag・semantic `font.price.*` | 一部のみ確認できる | 表現語彙。料金構造・表示単位は決定しない (IA-OBJ-007 Does Not Decide) |
| IA-OBJ-009 Review の表現 | components.md ReviewStars・semantic `color.icon.rating`/`icon.reviewSize` | 一部のみ確認できる | 表現語彙。Review の提供元・評価対象・信頼性は決定しない (IA-OBJ-009 Open Issue) |
| IA-OBJ-001/004/005/006/008/010/011/012 (Destination/Room/Stay Plan/Availability/Policy/Booking/User/Content) の表現 | 専用 component を確認できない | 対応する定義を確認できない | 専用表現語彙の不在は 1 対 1 対応の欠如であり、直ちに component 追加を要する結論ではない (§14)。IA Object の内容・関係・業務仕様は IA §11 Open Issue |

### 8.3 SD-003 Navigation (NVP-001〜008 / NAV-001〜006 / Navigation State Model)

Navigation と CTA を別責務として評価する。Header・Breadcrumb 等の component が存在することだけを理由に特定 NAV ID へ対応すると判定しない。

| 設計責務 (ID) | DS 側直接証拠 | 観察区分 | Conflict or gap / Does Not Decide |
| --- | --- | --- | --- |
| NVP-001 Current Location Visibility | components.md Breadcrumb「リンク + 区切り + 現在地 (`color.text.muted`)、現在地はリンク化しない」 | 一部のみ確認できる | 具体的な UI/ラベル/表示位置は NVP-001 Does Not Decide |
| NVP-005 Consistent Meaning | components.md「状態の固定リスト」・semantic 用途ベース命名 | 一部のみ確認できる | 正式ラベル・命名規則・Component 仕様は NVP-005 Does Not Decide (naming-rules.md 参照切れ) |
| NVP-008 Accessible Navigation | semantic `color.focus.ring` (outline ベース)・components.md focus 適用 | 一部のみ確認できる | 適用規格・達成レベルは NVP-008 Does Not Decide |
| NAV-001〜006 (6 分類) | components.md Header (ロゴ/ナビゲーション/会員導線)・Breadcrumb (階層ナビゲーション)・Footer が存在するが、DS 側に NAV-ID との対応記述はない | 一部のみ確認できる (移動を表現し得る component は存在), 対応する定義を確認できない (NAV 分類との明示的対応は DS に記述なし) | component 存在を特定 NAV ID への対応と判定しない。Global Navigation 対象領域等は NAV 側 Open Issue |
| Navigation State Model (Entry, Exploring, Evaluating, Committing, Completed, Error / Interrupted) | semantic `elevation.sticky` (Header sticky) 以外に navigation 状態を表現する定義を確認できない | 対応する定義を確認できない | 状態の UI 表現は Screen Requirements / Design System の後続判断。navigation.md §10 Open Issue「既存 Design System の Navigation 関連 Component との整合性」 |

### 8.4 SD-004 Content Principles (CTP-001〜010 / Content Categories / Status and Uncertainty Model)

typography・color・content に関する既存定義を確認する。`brand-content.md` が存在しないことは baseline-assessment.md の参照切れとして継承し、存在しない文書の内容を推測しない (§14)。

| 設計責務 (ID) | DS 側直接証拠 | 観察区分 | 備考 |
| --- | --- | --- | --- |
| CTP-006 Explicit State and Uncertainty | semantic `color.state.success`/`error`・components.md 状態固定リスト | 一部のみ確認できる, placeholder | Status and Uncertainty Model (Confirmed/Provisional/Loading-Updating/Unavailable/Error/Unknown) に対し DS 側は success/error 中心。状態一覧・状態表示 Component は CTP-006 Does Not Decide |
| CTP-008 Accessible and Scannable Content | design.md §3 タイポグラフィスケール (rem 基準)・primitive `typography.size.*`・components.md「色/アイコン/位置だけに意味を依存させない」 | 対応を直接確認できる (視覚のみ依存しない方針の記述あり), 一部のみ確認できる (具体規格未定義) | タイポグラフィ・文字数制限・Component 仕様は CTP-008 Does Not Decide |
| CTP-010 Separate Fact, Decision, and Promotion | semantic `color.accent.campaign`「点専用・ボタン塗り禁止 (TVL-0012)」・design.md「特集と通常導線を色で分離」 | 対応を直接確認できる, provenance 未確認 (TVL-0012 の ADR 正本なし) | 広告表示ルール・キャンペーン方針は CTP-010 Does Not Decide |
| CTP-002/005 Plain Language / Consistent Terminology (文言表現) | 文言・コピーの正本 `brand-content.md` が参照切れ (不在) | 参照切れ | 文言表現の直接証拠を Repository 内で確認できない。存在しない文書の内容は推測しない (baseline 継承) |
| Content Categories (Identification / Decision Support / Conditions and Policies / Task Guidance / Status and Feedback / Editorial and Support) | DS 側に Content Category 名との対応記述はない | 対応する定義を確認できない | Content Category は Content 表現の分類であり、DS の component 分類と 1 対 1 ではない |

### 8.5 SD-005 CTA Principles (CTA-001〜010 / CTA-TYPE-001〜005 / Commitment Level Model / CTA State Model)

CTA Principles と Button 記載の関係は直接証拠に基づいて評価し、一致して見えても provenance 未確認の事項を上流要求への適合確定としない。Screen Requirement 別の行 (cta-principles.md §7) は今回の個別評価対象に含めない。

| 設計責務 (ID) | DS 側直接証拠 | 観察区分 | provenance / placeholder |
| --- | --- | --- | --- |
| CTA-001 Action Clarity | components.md Button (用途: 予約導線の主 CTA・補助操作) | 一部のみ確認できる | — |
| CTA-002 One Clear Primary Action | components.md Button Do「1 画面の主 CTA は primary 1 つに絞る」・variant primary/secondary/ghost/text | 対応を直接確認できる (DS の Do 記述と責務が一致) | variant 語彙は GOV-0002 由来だが ADR 正本なし → provenance 未確認 (適合確定にしない) |
| CTA-005 Conditions Before Action | components.md PriceTag「税・条件の補助テキスト併記構造」 | 一部のみ確認できる | 表示位置・価格構造は CTA-005 Does Not Decide |
| CTA-006 Reversible Before Irreversible | components.md Modal / Overlay (drawer 統一 TVL-0007)・design.md | 対応する定義を確認できない (可逆/不可逆を区別する DS 側の明示規則なし) | TVL-0007 は provenance 未確認 |
| CTA-007 Explicit State and Availability | components.md 状態固定リスト (disabled/loading/error/success 等) | 一部のみ確認できる, placeholder | CTA State Model の Available/Unavailable/Loading-Processing/Success/Error/Pending Confirmation のうち Pending Confirmation に対応する DS 状態を確認できない。ボタン状態は未取得 (follow-up #4) |
| CTA-009 Accessible Activation | semantic `color.focus.ring` (outline)・components.md focus 適用 | 一部のみ確認できる | 適用規格は CTA-009 Does Not Decide |
| CTA-010 No Unsupported Pressure | design.md/semantic「根拠のない人気・ランキング・限定・緊急性を確定情報として扱わない」「accent は点専用」 | 対応を直接確認できる | — |

### 8.6 SD-007 UX Decision Records (UXDR-TRAVEL-001〜003, いずれも Record Status Accepted)

UX Decision Record の Decision Status (Accepted) と成果物自体の Status (Draft) を混同しない。NavigationとCTAの責務分離は component 名だけでなく本文の規則から評価する。

| Decision (Status) | Downstream Impact (SD-007 記載) | DS 側直接証拠 | 観察区分 |
| --- | --- | --- | --- |
| UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements (Accepted) | 「Design System は未定義事項に依存する要件・仕様を確定せず Open Issue を引き継ぐ」 | JSON `$status: placeholder` + `$note`・design.md 未確定事項一覧 (🚧/❓) を維持 (baseline 継承) | 対応を直接確認できる (DS が未取得を placeholder として保持し、推測補完していない) |
| UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens (Accepted) | 「Design System は画面候補単位の固定 UI を前提としない」 | design.md/components.md は token・component 単位で構成され、画面候補単位の固定 UI 定義を持たない | 対応を直接確認できる |
| UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities (Accepted) | 「Design System は Navigation 要素と CTA 要素 (Button / Link 等) を別 Pattern・評価軸で扱う」 | components.md は Button (CTA) と Header/Breadcrumb (Navigation) を別 component として定義するが、NAV/CTA の責務分離を述べる本文規則は確認できない。cta-principles.md §8「具体的な UI 分類は Design System 側で定義する」に対応する DS 側の分類規則は未記述 | 一部のみ確認できる (component 単位では別扱い), 対応する定義を確認できない (責務分離を述べる DS 本文規則は不在) |

## 9. Cross-cutting Observations

- **Fact**: 既存 Design System は token・component の設計語彙を提供し、その内部整合性は baseline-assessment.md で確認済み (semantic 参照 63/63 解決)。SD-001 の SDP-008/009/010、SD-007 の UXDR-TRAVEL-001/002 は DS 内部の運用 (placeholder 保持・独立性・非画面単位構成) として対応を直接確認できる。
- **Fact**: SD-003/SD-005 の状態モデル (Navigation State Model・CTA State Model) と DS 側の状態表現は一部のみ一致し、Pending Confirmation・navigation 状態など DS 側に対応する定義を確認できない領域がある。ボタン状態は未取得 (follow-up #4, placeholder)。
- **Fact**: IA Object・Content Category・NAV 分類・CTA 種別は、DS の component/token と 1 対 1 対応しない。専用表現語彙 (SearchForm/Card/PriceTag/ReviewStars) が存在する IA Object は一部のみで、他は対応する定義を確認できない。
- **Observation**: SD 各文書の Design System 関連 Open Issue (principles §7「既存 Design System との不整合確認」/ IA §11 / navigation §10 / content §10 / cta §11) は本 Baseline 段階でも未解決のまま継承される。
- 数値スコア・適合率・pass/fail・severity は付与しない (Alignment Plan §8)。

## 10. Conflicts and Gaps

以下は観察であり、修正・追加・削除の Decision ではない (§17)。

- **Gap (対応する定義を確認できない)**: SDP-002 Progressive Commitment / SDP-006 Recoverability の一部・CTA-006 Reversible Before Irreversible を横断的に表現する DS 側の規則を確認できない。これらは主にフロー・画面単位の責務であり、DS が決めない範囲を含む。
- **Gap (一部のみ確認できる / placeholder)**: CTA State Model の Pending Confirmation・Navigation State Model の各状態に対応する DS 側の状態表現を確認できない。ボタン状態一式・motion は placeholder / 実査待ち。
- **Gap (対応する定義を確認できない)**: UXDR-TRAVEL-003 の NAV/CTA 責務分離を述べる DS 側の本文規則が不在 (component 単位の区別はある)。
- **明確な矛盾 (矛盾)**: 上流 Service Design の定義と DS 記述の直接的な矛盾は、本評価段階の直接証拠では確認されなかった。SD 側が具体値 (色値・breakpoint 値等) を定義していないため、DS の具体値と上流原則が矛盾するかは直接証拠からは確認できない (上流に具体値要求がないため token 値の良否を上流適合として評価しない)。
- 上記 Gap は、専用 component/token の不在を「直ちに追加すべき」という結論に変換しない。改定候補の整理は Work Order 5、着手可否は Work Order 6 で扱う。

## 11. Provenance and Reference Issues

baseline-assessment.md §12 を証拠品質・制約として継承する (再決定しない)。provenance 未確認の記載は、内容が正しい・承認済み・上流要求へ適合済みという意味にしない。

- **参照切れ**: `brand-content.md` (design.md 参照) 不在・`governance/naming-rules.md` (design.md/components.md 参照) 不在。SD-004 の文言表現 (CTP-002/005) の直接証拠を Repository 内で確認できない。
- **provenance 未確認**: GOV-0002 (Button variant 語彙)・TVL-0001〜TVL-0012 (TVL-0009 は 4 資産に未出現) の ADR 正本なし。SD-005 の Button 関連記述が CTA Principles と一致して見えても、GOV-0002/TVL の provenance が未確認のため上流適合の確定としない。
- **placeholder / 実査待ち**: semantic `radius.card`/`motion.transition.*`・primitive `shadow.*`/`motion.*` (計 10)。follow-up #2/#4/#13 は owner-decisions.md §3 に記載、follow-up #3 は同 §3 に未記載。
- **外部参照 (未検証)**: Source of Truth GitHub URL・実装 Repository `tocoo/tocoo_travel` は記載のみで内容を検証していない。
- **DS 内部整合性 (継承)**: token 参照解決・component 一覧・未着手 component (Select/Tabs/Toast/Table/Accordion) の内部整合は baseline で確認済み。本評価はこれを再決定しない。

## 12. Downstream Impact

- **Assets** ([../assets/README.md](../assets/README.md)) — `Not started`。本評価の対象外。
- **Implementation** — Repository 管理対象外。本評価は静的評価であり実装検証ではない。DS から実装画面・URL・route を導出しない。

## 13. Open Issues

以下は未決である。解決策は推測して記載しない。

- 本評価結果の承認・反映主体、および後続 Work Order (3〜6) への引き継ぎ方法。
- SD 各文書の「既存 Design System との整合性確認」Open Issue の解決主体。
- 対応する定義を確認できない責務 (SDP-002/006 の一部・CTA-006・Navigation/CTA State の一部・NAV/CTA 責務分離規則・IA/Content/NAV/CTA 分類との対応) の扱い。
- placeholder / 実査待ち token (計 10)・ボタン状態未取得 (follow-up #4) の解決。
- `brand-content.md`・`governance/naming-rules.md`・ADR 正本の不足の解決主体。
- GOV-0002・TVL Decision ID の provenance と有効性。
- 状態モデル (Navigation State / CTA State / Content Status) と DS 状態表現の対応整理。

## 14. Does Not Decide

- Design System の改定要否・token 値/名/階層/命名規則・placeholder の解消方法。
- component の追加/削除/統合/分割・component API/variant/state/実装仕様。
- Service Design または Screen Requirement の修正・SCR-006〜SCR-012 の要求。
- UI 構造・表示順・情報密度・API/DB/URL/route。
- 正式な ID/ファイル名・実装 Repository との適合・参照切れ文書の内容・provenance 未確認事項の正当性・UX Decision の追加。
- 「対応する定義を確認できない」「一部のみ確認できる」を、component/token の追加・改定の Decision へ変換しない。

## 15. Relationship to Subsequent Work

- 本評価 (Work Order 2) は、Alignment Plan §10 の次段である Work Order 3「作成済み 7 個別 Screen Requirement ごとの対応確認」の入力となる。
- Work Order 3 は本 PR のマージ前には開始しない。
- 改定候補と未解決事項の分離 (Work Order 5)・改定着手可否の判断 (Work Order 6) は、本評価と Work Order 3 の観察が揃った後に成立する。
- 本評価は Design System の修正・新しい UX Decision を含まない。改定は後続タスクの承認を前提とする。

## 16. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial assessment (Work Order 2): SD-001〜SD-005・SD-007 の横断的設計責務と既存 Design System 4 成果物の対応を Repository 内直接証拠だけで静的評価。個別 Screen Requirement 評価・DS 修正・UX Decision 追加は未実施 | Draft |
