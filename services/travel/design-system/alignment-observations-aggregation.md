# Travel Alignment Observations Aggregation

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Alignment Assessment のうち、Work Order 2 (Service Design 横断整合性評価) と Work Order 3 (作成済み 7 個別 Screen Requirement ごとの整合性評価) で記録された Observation を、Work Order 1 (Baseline) の証拠制約を保持しながら横断集約した記録。Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 4 の実行。改訂候補と未解決事項の分離 (Work Order 5)・改訂着手可否の判断 (Work Order 6)・Design System の修正・UX Decision の追加は行わない。
- Position in Repository: `services/travel/design-system/alignment-observations-aggregation.md` — Design System レイヤー (travel サービス配下)。Design System README の Reference Order 上で自身より前に配置される上流成果物は、レイヤー入口 [README.md](README.md)・Alignment 計画 [alignment-plan.md](alignment-plan.md)・Baseline 評価 [baseline-assessment.md](baseline-assessment.md)・Service Design 横断整合性評価 [service-design-alignment-assessment.md](service-design-alignment-assessment.md)・Screen Requirements 個別整合性評価 [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md)。集約対象の入力評価文書、参照する Service Design 成果物・Screen Requirements 成果物、および評価対象であった既存 Design System 4 成果物との関係は本文 Aggregation Sources (§8) / Method (§9) / Source Traceability Index (§12) / 各集約節 (§13〜§18) に記載し、Position の上流成果物へ混在させない。下流成果物 (Assets / Implementation) との関係は §21 を参照。

本文書は集約記録であり、Design System 仕様・Design Decision・改訂候補一覧の正本ではない。集約は入力評価文書に既に記録された Observation の横断的な整理であり、新しい Observation・分類・Decision を追加しない。評価上の観察区分 (Alignment Plan §8) を Repository 成果物の正式 Status・優先度・severity と混同しない。ファイル名 `alignment-observations-aggregation.md` は記述的な暫定識別子であり、正式な評価体系名・分類体系・集約 ID・命名規則を確定しない。`Descriptive Topic` および本文書内の行番号を新しい恒久 ID として採番しない。SCR ID は Screen Matrix 上の画面候補 ID であり、Screen Requirement 文書 ID・実装画面 ID・URL・route と同一視しない。Fact / Decision / Hypothesis / Open Issue を区別し、新しい Decision を追加しない。

## 1. Purpose

- Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 4「観察結果の横断集約」を実行する。
- Work Order 2 ([service-design-alignment-assessment.md](service-design-alignment-assessment.md)) と Work Order 3 ([screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md)) が記録した Observation を、元の出典・観察区分・provenance・placeholder・実査待ち・参照切れ・Open Issue・Does Not Decide を失わずに、設計責務に対する Observation の単位で横断的に整理する。
- 共通する Observation・異なる Observation・個別スコープに限定される Observation を区別し、元 Observation へ追跡可能な状態を作る (§12 Source Traceability Index)。
- 「Observation を横断的に整理する」ことと「改訂候補と未解決事項を分離する / 優先順位を付ける / Design System を改定する / 着手可否を判断する」ことを区別する。後者は本文書では行わない (§20・§23)。
- 集約結果は Work Order 5 (改訂候補と未解決事項の分離) 以降の入力とする。

## 2. Status

- 本文書の Status は `Draft` である。
- 集約対象・継承源はいずれも Draft の評価記録である。集約が入力評価文書の Status を昇格させることはない。
- Work Order 4 を Draft として実施済みと記載する条件は §20 Work Order 4 Completion Boundary に定義する。

## 3. Position

- 本文書は Design System レイヤー (travel サービス配下) の成果物であり、Alignment Assessment の 5 番目の評価/集約記録である。
- Design System README の Reference Order 上で自身より前にある上流成果物として本文書が参照できるのは、[README.md](README.md)・[alignment-plan.md](alignment-plan.md)・[baseline-assessment.md](baseline-assessment.md)・[service-design-alignment-assessment.md](service-design-alignment-assessment.md)・[screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) のみ。
- Service Design 成果物 (SD-001〜SD-007)・Screen Requirements 成果物 (作成済み 7 個別 Screen Requirement)・既存 Design System 4 成果物 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) との関係は、上流 Position へ混在させず、本文 Aggregation Sources (§8)・Method (§9)・Source Traceability Index (§12)・各集約節 (§13〜§18) に記載する。
- Assets と Implementation は下流成果物であり Downstream Impact (§21) に分離する。

## 4. Purpose Boundary（集約と再評価の区別）

- 本文書は入力評価文書に記録済みの Observation を集約する。既存 Design System 4 成果物・Service Design・Screen Requirements・Governance を再評価しない。
- 入力評価文書と矛盾する可能性を確認した場合は、本文書内で不一致 (Conflict or Gap) として記録し、元文書を修正しない (§9・§18)。
- 集約によって元 Observation の観察区分・provenance・placeholder・実査待ち・参照切れ・Open Issue・Does Not Decide を変更・解決・昇格させない。

## 5. Aggregation Snapshot

- Aggregation target: 作業開始時点の `main`。
- Aggregation snapshot (main commit SHA): `e2d984179b6ea84250e0a8b3828a9491f8b668d3` (PR #51 merge)。
- 集約日: 2026-07-17。
- 本集約は Repository 内文書の静的集約であり、実装検証ではない。既存 Design System 4 成果物は再評価せず、入力評価文書の直接証拠を追跡する。集約中に main の更新はなく、異なる snapshot を混在させていない。

### 入力評価文書 (blob SHA @ `e2d9841`)

| 入力 | ファイル | Work Order | blob SHA |
| --- | --- | --- | --- |
| 主な集約対象 | [service-design-alignment-assessment.md](service-design-alignment-assessment.md) | Work Order 2 | `6ffb827d43b854fab81fafd54c3daa12fdcce3f4` |
| 主な集約対象 | [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) | Work Order 3 | `574ae39d4372df060bdf293eb04383f29cf1dade` |
| 証拠品質・制約の継承源 | [baseline-assessment.md](baseline-assessment.md) | Work Order 1 | `89ea9d17257cf2e5b162dc702944b21033ef71e2` |
| 評価方法・分類・順序の継承源 | [alignment-plan.md](alignment-plan.md) | — | `7c9d35fbacd03f522fc06ca375ae80c0edbcca9a` |

### 集約が追跡する既存 Design System 4 成果物 (再評価しない)

- [design.md](design.md) / [semantic.travel.json](semantic.travel.json) / [primitive.travel.json](primitive.travel.json) / [components.md](components.md)。いずれも Draft・version `0.3.0-draft`。本文書はこれらを再評価せず、入力評価文書が記録した直接証拠を追跡する。

## 6. Scope

- Work Order 2 の主要 Observation (SD-001〜SD-005・SD-007 の横断的設計責務に対する対応・部分対応・gap) の横断集約。
- Work Order 3 の 7 個別 Screen Requirement (SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014) の主要 Observation の横断集約。
- Work Order 3 の個別 Observation を横断集約することが本工程の中心である。Work Order 2 は、その Observation がすでに Service Design 横断の責務として確認されているかを追跡するための入力として関係づける。
- 集約単位は Component 名・token 名・SCR 番号だけではなく、入力評価文書で確認された「設計責務に対する Observation」とする (§9)。
- Work Order 1 の Baseline 由来の証拠制約 (token 参照内部整合性・placeholder・実査待ち・provenance・参照切れ) を、関係する集約 Observation へ関連づける (§17)。

## 7. Out of Scope

- 改訂候補と未解決事項の分離、gap の原因責任の決定 (Work Order 5)。
- 優先順位・重要度・severity・対応順の決定。
- 新規 Component・token・pattern・文書の提案、不足を埋める解決策の提案。
- 改訂着手可否の判断、承認主体の推測 (Work Order 6)。
- 数値スコア・適合率・カバレッジ率・出現件数によるランキング・pass/fail・severity の導入。
- 既存 Design System 4 成果物・Service Design・Screen Requirements・Governance の再評価・修正。
- SCR-006〜SCR-012 の評価・要求定義。
- Screen Matrix の画面候補を実装画面・URL・route とみなすこと。
- 新しい Observation 分類・正式な集約 ID・評価体系名・ファイル名の確定・UX Decision の追加。

## 8. Aggregation Sources

Position の上流成果物 (README / alignment-plan / baseline-assessment / service-design-alignment-assessment / screen-requirements-alignment-assessment) と区別し、本集約が対象・継承源とする成果物を示す。

- **主な集約対象**: [service-design-alignment-assessment.md](service-design-alignment-assessment.md) (Work Order 2)・[screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) (Work Order 3)。両者に記録された Observation・出典・観察区分・provenance・placeholder・実査待ち・参照切れ・Open Issue・Does Not Decide を集約対象とする。
- **証拠品質・制約の継承源**: [baseline-assessment.md](baseline-assessment.md) (Work Order 1)。token 参照内部整合性・placeholder・実査待ち・provenance・参照切れ等を、集約結果の証拠品質・解釈上の制約として継承する (再決定しない)。
- **評価方法・分類・順序の継承源**: [alignment-plan.md](alignment-plan.md) (§5 Assessment Unit / §6 Evidence Rules / §8 Observation Classification / §9 Assessment Dimensions / §10 Recommended Work Order)。
- **入力評価文書を通じて追跡される成果物 (再評価しない)**: Service Design SD-001〜SD-007 ([../service-design/README.md](../service-design/README.md))・作成済み 7 個別 Screen Requirement ([../screen-requirements/README.md](../screen-requirements/README.md))・既存 Design System 4 成果物。本文書はこれらを直接再評価せず、入力評価文書が記録した実在記述への参照を保持する。

役割の混同を避けるため以下を守る。

- Work Order 3 の個別 Observation を横断集約することが中心である。
- Work Order 2 は、Observation がすでに Service Design 横断の責務として確認されているかを追跡するための入力である。
- Work Order 1 は token・placeholder・実査待ち・provenance・参照切れ等の証拠制約である。
- 既存 Design System 4 成果物は再評価対象ではない。

## 9. Method

以下の手順で集約する (Alignment Plan §5・§6・§8・§9 を継承)。

1. Work Order 2 と Work Order 3 に存在する Observation を出典付きで棚卸しする (§12 Source Traceability Index)。
2. 各 Observation について、入力ファイル・節・対象 Service Design ID または SCR・設計責務・DS 側の直接証拠・元の Observation 分類・provenance・placeholder / 実査待ち・Open Issue・Does Not Decide を保持する。
3. 同じまたは密接に関連する設計責務に対する Observation を、Descriptive Topic (§13〜§15) としてまとめる。集約軸は Alignment Plan §9 の Assessment Dimension (Foundation / token・Component / pattern・Cross-cutting) を整理軸として使用する。
4. まとめた後も、すべての元出典を Source Assessment / Source Section / Related SD ID / Related SCR に列挙し、追跡可能性を保持する。元レコードを削除しない。
5. 同一テーマ内で Observation が異なる場合、どちらかへ統一せず Source-specific Variation として差異を記録する (§16)。
6. 個別 Screen Requirement だけに適用される Observation を、無理に共通 Observation へ昇格させず、スコープ固有の観察として保持する (§16)。
7. Baseline 由来の placeholder・実査待ち・provenance 未確認・参照切れを、関係する集約 Observation へ関連づける (§17)。
8. Work Order 5 の判断 (改訂候補と未解決事項の分離) に踏み込まず、未解決の依存関係として記録する (§19)。

集約は単なる文章の連結やコピーではなく、重複する観察の関係が理解できる形にする。ただし重複する元レコードを削除せず、Source Traceability (§12) で保持する。入力評価文書と矛盾する可能性を確認した場合は本文書内で不一致として記録し、元文書を修正しない。

## 10. Evidence Rules

Alignment Plan §6 と入力評価文書 (§7 Evidence Rules) を継承する。

- 集約の証拠は、入力評価文書に実在する Observation・出典・観察区分・provenance・placeholder・実査待ち・参照切れ・Open Issue・Does Not Decide に限定する。入力評価文書が記録していない対応・不足・矛盾を本集約で新たに作らない。
- 既存 Design System 4 成果物の記述は、入力評価文書が引用した範囲で追跡する。本集約が独自に成果物を再走査して新しい直接証拠を追加しない。
- ファイル名・Component 名の推測、一般慣行、実装仕様の推測、不在文書の内容、正本のない ADR の想定、Decision ID の存在のみを根拠とする再認定、Downstream Impact の Component 例、Component 存在のみを根拠とする利用要求、Open Issue / Does Not Decide を確定要件へ変換した内容は証拠として扱わない。
- 上流の名称 (token 名・Component 名・NAV/CTA ID・follow-up 番号・外部 URL) だけを根拠に Observation を作らず、必ず入力評価文書の実在記述へ追跡する。

## 11. Aggregation Boundary（必ず保持する境界）

集約後も以下を保持する。

- Navigation と CTA を別の設計責務として集約する (UXDR-TRAVEL-003)。
- Header や Breadcrumb の存在だけで NAV ID 対応済みとしない。
- Button の存在だけで CTA 対応済みとしない。
- IA Object を Component・表示項目・データモデルと同一視しない。
- Content Category を Component・掲載枠と同一視しない。
- Navigation State Model を Component state と同一視しない。
- `Error / Interrupted` は 1 つの複合状態名として扱い、状態間はカンマで区切る。
- SCR ごとに異なる Navigation States を共通状態一覧へ正規化しない。
- SCR-014 に存在しない `Error / Interrupted` を追加しない。
- Screen Requirement の Downstream Impact にある Component 例を採用 Decision へ変換しない。
- 未着手 Component を必要 Component または改訂候補へ変換しない。
- Open Issue と Does Not Decide を確定要件へ変換しない。
- provenance 未確認を適合確認済みへ昇格させない。
- placeholder または実査待ちを「対応済み」へ統合しない。

観察区分は Alignment Plan §8 の 10 分類だけを使用する: 対応を直接確認できる / 一部のみ確認できる / 対応する定義を確認できない / 過剰 / 矛盾 / placeholder / 実査待ち / provenance 未確認 / 参照切れ / 評価対象外。元レコードに複数分類がある場合は単一分類へ丸めず併記する。集約上の共通性やスコープ差は説明できるが、新しい Observation 分類として登録しない。数値スコア・適合率・カバレッジ率・件数によるランキング・pass/fail・severity は導入しない。

§13〜§15 で用いる見出し (Navigation・CTA・IA Object・Content・State and Feedback・Accessibility 等) および `Descriptive Topic` は、文書内の説明用整理軸であり、新しい正式分類・評価体系・Decision ではない。

## 12. Source Traceability Index

集約によって元の Observation が失われていないことを確認するための索引。網羅性確認のための索引であり、数値カバレッジ・得点・適合率を算出しない。「集約先 Topic」列は §13〜§15 の Descriptive Topic ID (T-xx / C-xx / X-xx) を指す。スコープ固有として保持したものは §16 に再掲する。

### 12.1 Work Order 2 (service-design-alignment-assessment.md) の主要 Observation

| 出典節 | 対象 SD ID / モデル | 主要 Observation (元分類) | 集約先 Topic |
| --- | --- | --- | --- |
| §8.1 | SDP-001 User Task Clarity | 一部のみ確認できる (Button 主 CTA primary 1 つ・Breadcrumb 現在地非リンク) | C-01・C-06 |
| §8.1 | SDP-002 Progressive Commitment | 対応する定義を確認できない | X-03 |
| §8.1 | SDP-003 Transparent Conditions | 一部のみ確認できる, provenance 未確認 (PriceTag 税条件併記・accent.campaign 点専用 TVL-0012) | C-04・X-02 |
| §8.1 | SDP-004 Consistent Mental Model | 一部のみ確認できる, 参照切れ (用途ベース命名・状態固定リスト・naming-rules.md 不在) | T-02・X-07 |
| §8.1 | SDP-005 State Visibility | 一部のみ確認できる, placeholder (状態固定リスト・state.success/error・ボタン状態 follow-up #4・motion placeholder) | T-02・T-06・X-03 |
| §8.1 | SDP-006 Recoverability | 一部のみ確認できる, 実査待ち (Input エラーテキスト併記・Modal/Overlay・Input follow-up #2) | C-02・C-07 |
| §8.1 | SDP-007 Accessibility by Default | 対応を直接確認できる / 一部のみ確認できる (WCAG 2.2 AA 最低ライン・focus.ring・色のみで伝えない・一部コントラスト未達可能性) | T-01・X-04 |
| §8.1 | SDP-008 Evidence over Assumption | 対応を直接確認できる (placeholder + $note 維持・根拠なき人気非確定) | X-05・X-02 |
| §8.1 | SDP-009 Service-wide Coherence | 対応を直接確認できる (内部整合 63/63・独立 DS R1) | T-07 |
| §8.1 | SDP-010 Incremental Definition | 対応を直接確認できる, provenance 未確認 (placeholder 維持 TVL-0008) | X-05 |
| §8.2 | IA-OBJ-002 Search Criteria | 一部のみ確認できる (SearchForm) | C-02・X-06 |
| §8.2 | IA-OBJ-003 Accommodation | 一部のみ確認できる (Card 8 スロット) | C-03・X-06 |
| §8.2 | IA-OBJ-007 Price | 一部のみ確認できる (PriceTag・font.price.*) | C-04・T-05・X-06 |
| §8.2 | IA-OBJ-009 Review | 一部のみ確認できる (ReviewStars・color.icon.rating) | C-05・T-05・X-06 |
| §8.2 | IA-OBJ-001/004/005/006/008/010/011/012 | 対応する定義を確認できない (専用表現語彙なし) | C-10・X-06 |
| §8.3 | NVP-001 Current Location Visibility | 一部のみ確認できる (Breadcrumb) | C-06 |
| §8.3 | NVP-005 Consistent Meaning | 一部のみ確認できる, 参照切れ (用途ベース命名・naming-rules.md 不在) | X-07・T-02 |
| §8.3 | NVP-008 Accessible Navigation | 一部のみ確認できる (focus.ring) | T-01・X-04 |
| §8.3 | NAV-001〜006 | 一部のみ確認できる / 対応する定義を確認できない (Header/Breadcrumb/Footer 実在・NAV-ID 対応記述なし) | C-06・X-01 |
| §8.3 | Navigation State Model (Entry, Exploring, Evaluating, Committing, Completed, Error / Interrupted) | 対応する定義を確認できない (elevation.sticky 以外なし) | X-03 |
| §8.4 | CTP-006 Explicit State and Uncertainty | 一部のみ確認できる, placeholder (state.success/error 中心・Status and Uncertainty Model 不足) | X-03・T-02 |
| §8.4 | CTP-008 Accessible and Scannable Content | 対応を直接確認できる / 一部のみ確認できる (typography スケール・視覚のみ非依存) | T-03・X-04 |
| §8.4 | CTP-010 Separate Fact, Decision, and Promotion | 対応を直接確認できる, provenance 未確認 (accent.campaign 点専用 TVL-0012・特集色分離) | X-02・T-04 |
| §8.4 | CTP-002/005 Plain Language / Consistent Terminology | 参照切れ (brand-content.md 不在) | X-07 |
| §8.4 | Content Categories (6) | 対応する定義を確認できない | X-06 |
| §8.5 | CTA-001 Action Clarity | 一部のみ確認できる (Button) | C-01 |
| §8.5 | CTA-002 One Clear Primary Action | 対応を直接確認できる, provenance 未確認 (Button Do 主 CTA primary 1 つ・variant GOV-0002) | C-01・X-01 |
| §8.5 | CTA-005 Conditions Before Action | 一部のみ確認できる (PriceTag 税条件併記) | C-04・X-02 |
| §8.5 | CTA-006 Reversible Before Irreversible | 対応する定義を確認できない, provenance 未確認 (可逆/不可逆区別規則なし・TVL-0007) | C-07・X-03 |
| §8.5 | CTA-007 Explicit State and Availability | 一部のみ確認できる, placeholder (状態固定リスト・Pending Confirmation 対応なし・ボタン状態 follow-up #4) | X-03・T-02 |
| §8.5 | CTA-009 Accessible Activation | 一部のみ確認できる (focus.ring) | T-01・X-04 |
| §8.5 | CTA-010 No Unsupported Pressure | 対応を直接確認できる (根拠なき人気/ランキング/限定/緊急性非確定・accent 点専用) | X-02 |
| §8.6 | UXDR-TRAVEL-001 Preserve Unknowns | 対応を直接確認できる (placeholder + $note 維持) | X-05 |
| §8.6 | UXDR-TRAVEL-002 Separate Conceptual Screen Candidates | 対応を直接確認できる (token/component 単位構成) | X-06 |
| §8.6 | UXDR-TRAVEL-003 Keep Navigation and CTA Separate | 一部のみ確認できる / 対応する定義を確認できない (component 単位では別扱い・責務分離の本文規則不在) | X-01 |

### 12.2 Work Order 3 (screen-requirements-alignment-assessment.md) の主要 Observation

| 出典節 (SCR) | 対象責務 / SD ID | 主要 Observation (元分類) | 集約先 Topic |
| --- | --- | --- | --- |
| §12 SCR-001 | 探索起点 (SDP-001) | 一部のみ確認できる (Button/Header) | C-01・C-06 |
| §12 SCR-001 | Info Resp. Destination/Search Criteria/Content (IA-OBJ-001/002/012) | 一部のみ確認できる (SearchForm)・Destination/Content 専用表現語彙は確認できない | C-02・C-10・X-06 |
| §12 SCR-001 | NAV-001 Global / NAV-004 Task / NAV-006 Utility | 一部のみ確認できる / 対応する定義を確認できない (Header・NAV-ID 対応記述なし) | C-06・X-01 |
| §12 SCR-001 | CTA-002 探索開始と補助導線を競合させない | 対応を直接確認できる, provenance 未確認 (Button Do・GOV-0002) | C-01・X-01 |
| §12 SCR-001 | CTA-009 / Accessibility (SDP-007/NVP-008/CTP-008) | 一部のみ確認できる (focus.ring・色のみで伝えない) | T-01・X-04 |
| §12 SCR-001 | Content Identification/Task Guidance/Editorial (CTP-002/005/010) | 対応を直接確認できる / 参照切れ (特集色分離・accent.campaign・brand-content.md 不在) | X-02・X-07・T-04 |
| §12 SCR-001 | State Entry, Exploring (Navigation State Model) | 対応する定義を確認できない (elevation.sticky 以外なし) | X-03 |
| §13 SCR-002 | Destination の発見表現 (IA-OBJ-001) | 対応する定義を確認できない | C-10・X-06 |
| §13 SCR-002 | Content の発見表現 (IA-OBJ-012) | 対応する定義を確認できない, 参照切れ (brand-content.md 不在) | C-10・X-07 |
| §13 SCR-002 | Supporting Accommodation (IA-OBJ-003) | 一部のみ確認できる (Card) | C-03 |
| §13 SCR-002 | NAV-001/002/003 | 一部のみ確認できる / 対応する定義を確認できない (Header/Breadcrumb) | C-06・X-01 |
| §13 SCR-002 | CTA 発見と販促を混同しない (CTA-010/CTP-010) | 対応を直接確認できる, provenance 未確認 (accent 点専用・特集色分離・TVL-0011/0012) | X-02・T-04 |
| §13 SCR-002 | State Exploring (Navigation State Model) | 対応する定義を確認できない | X-03 |
| §13 SCR-002 | Accessibility (CTP-008/SDP-007) | 一部のみ確認できる | T-01・X-04 |
| §14 SCR-003 | Search Criteria 指定・確認・変更 (IA-OBJ-002) | 一部のみ確認できる, 実査待ち (SearchForm/Input・Input follow-up #2) | C-02 |
| §14 SCR-003 | 条件確認 / 状態可視 (SDP-005/CTA-007) | 一部のみ確認できる, placeholder (状態固定リスト・Input error 暫定・disabled/success 未取得) | T-02・X-03 |
| §14 SCR-003 | Error / Interrupted 回復 (SDP-006/CTP-007/NAV-005) | 一部のみ確認できる (Input error text 併記) | C-02・X-03 |
| §14 SCR-003 | NAV-004 Task / NAV-005 History and Recovery | 対応する定義を確認できない | C-06・X-01 |
| §14 SCR-003 | CTA 検索開始 (CTA-001/005) | 対応を直接確認できる, provenance 未確認 (SearchForm 検索実行 CTA Button.primary・GOV-0002) | C-01・C-02 |
| §14 SCR-003 | Supporting User (IA-OBJ-011) | 対応する定義を確認できない (認証/会員 component なし) | C-10・X-06 |
| §14 SCR-003 | Accessibility (CTP-008/CTA-009) | 一部のみ確認できる | T-01・X-04 |
| §15 SCR-004 | Accommodation 候補の確認・比較 (IA-OBJ-003) | 一部のみ確認できる, 実査待ち, placeholder (Card 8 スロット・実 px 実査待ち・radius.card/shadow placeholder) | C-03・T-05・T-06 |
| §15 SCR-004 | Decision Support Price/Review (IA-OBJ-007/009) | 一部のみ確認できる, 実査待ち (PriceTag/ReviewStars・「円」weight ❓) | C-04・C-05・T-05 |
| §15 SCR-004 | Conditions and Policies (IA-OBJ-008) | 対応する定義を確認できない | C-10・X-06 |
| §15 SCR-004 | 根拠のない人気/希少性を表現しない (CTP-004/006) | 対応を直接確認できる | X-02 |
| §15 SCR-004 | NAV-002/003/004/005 | 対応する定義を確認できない / 一部のみ確認できる | C-06・X-01 |
| §15 SCR-004 | State Exploring, Evaluating, Error / Interrupted (Navigation State/CTP-006) | 一部のみ確認できる, placeholder (状態固定リスト・color.state.*・motion placeholder) | X-03・T-06 |
| §15 SCR-004 | CTA 比較・詳細・条件変更・選択の優先関係 (CTA-002/005) | 一部のみ確認できる, provenance 未確認 (Button・PriceTag 条件併記・GOV-0002) | C-01・C-04・X-02 |
| §16 SCR-005 | Accommodation 情報確認・評価 (IA-OBJ-003) | 一部のみ確認できる, 実査待ち (Card は検索結果向け) | C-03 |
| §16 SCR-005 | Decision Support Review (IA-OBJ-009) | 一部のみ確認できる, 実査待ち (ReviewStars・星実寸実査待ち) | C-05 |
| §16 SCR-005 | Conditions and Policies (IA-OBJ-008/CTP-003) | 対応する定義を確認できない | C-10・X-06 |
| §16 SCR-005 | Room/Stay Plan の確認 (IA-OBJ-004/005) | 対応する定義を確認できない (業務モデル Open Issue) | C-10・X-06 |
| §16 SCR-005 | NAV-002/003/004/006 関連情報への移動 | 一部のみ確認できる / 対応する定義を確認できない (Breadcrumb/Header) | C-06・X-01 |
| §16 SCR-005 | CTA 情報確認と Room/Stay Plan 選択を区別 (CTA-002/004) | 一部のみ確認できる, provenance 未確認 (Button variant・GOV-0002) | C-01・X-01 |
| §16 SCR-005 | Editorial and Support 事実と販促分離 (CTP-010) | 対応を直接確認できる, provenance 未確認 (accent 点専用・特集色分離・TVL-0012) | X-02・T-04 |
| §16 SCR-005 | State Evaluating, Error / Interrupted (Navigation State) | 対応する定義を確認できない | X-03 |
| §17 SCR-013 | 支援への到達 / 補助情報 (NAV-006) | 対応する定義を確認できない | C-06・X-01 |
| §17 SCR-013 | Editorial and Support / Conditions and Policies (CTP-003/006/010) | 参照切れ / 対応する定義を確認できない (brand-content.md 不在・専用 component なし) | X-07・C-09 |
| §17 SCR-013 | CTA Recovery Action (CTA-TYPE-004/CTA-007) | 対応する定義を確認できない / 一部のみ確認できる (error/loading は fixed list・Recovery 用 component/規則なし・ボタン状態 follow-up #4) | C-08・X-03 |
| §17 SCR-013 | NAV-001/002/003/006 | 一部のみ確認できる / 対応する定義を確認できない (Header/Breadcrumb) | C-06・X-01 |
| §17 SCR-013 | Does Not Decide の Accordion 等 | 対応する定義を確認できない (Accordion 未着手明記・未着手を必要性へ変換しない) | C-09 |
| §17 SCR-013 | State Entry, Exploring, Error / Interrupted (Navigation State/CTP-007) | 対応する定義を確認できない | X-03 |
| §17 SCR-013 | Accessibility (CTP-008/CTA-009) | 一部のみ確認できる | T-01・X-04 |
| §18 SCR-014 | Content の発見・理解 (IA-OBJ-012) | 参照切れ / 対応する定義を確認できない (brand-content.md 不在・専用 component なし) | X-07・C-10 |
| §18 SCR-014 | Supporting Destination/Accommodation (IA-OBJ-001/003) | 一部のみ確認できる (Card) | C-03 |
| §18 SCR-014 | 編集情報と販促の区別 (CTP-010/CTA-010) | 対応を直接確認できる, provenance 未確認 (accent 点専用・特集色分離・TVL-0011/0012) | X-02・T-04 |
| §18 SCR-014 | CTP-004 根拠のない優位性/人気を表現しない | 対応を直接確認できる | X-02 |
| §18 SCR-014 | NAV-001/002/003 | 一部のみ確認できる / 対応する定義を確認できない (Header/Breadcrumb) | C-06・X-01 |
| §18 SCR-014 | State Entry, Exploring, Evaluating (Navigation State・Error / Interrupted 非含有) | 対応する定義を確認できない (Error / Interrupted を独断追加しない) | X-03 |
| §18 SCR-014 | Accessibility 画像/装飾なしでも理解可能 (CTP-008) | 一部のみ確認できる, 実査待ち (色・画像・位置非依存・画像欠落 fallback ❓) | X-04 |

### 12.3 索引の網羅性メモ

- Work Order 2 は SD-001 (SDP-001〜010)・SD-002 (IA-OBJ 評価 5 行)・SD-003 (NVP/NAV/State)・SD-004 (CTP/Categories)・SD-005 (CTA/State)・SD-007 (UXDR-TRAVEL-001〜003) の主要 Observation を上表に含む。
- Work Order 3 は SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014 の各節 (§12〜§18) の主要 Observation を上表に含む。
- 上表は網羅性確認のための索引であり、件数の多寡を優先度・severity として解釈しない。

## 13. Foundation / Token Observations

Assessment Dimension: Foundation / token (Alignment Plan §9 の整理軸)。以下の Descriptive Topic は説明用の整理単位であり、正式分類・Decision ではない。各 Topic は入力評価文書の元 Observation を横断集約したものであり、元出典・観察区分を §12 で追跡できる。

### T-01 Focus リング token とアクセシビリティ基盤

- **Assessment Dimension**: Foundation / token (Accessibility 整理軸に関係)。
- **Design Responsibility**: 操作要素の focus 可視化 (キーボード操作・視覚のみ非依存の一部)。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-007)・§8.3 (NVP-008)・§8.5 (CTA-009)・§8.4 (CTP-008)、WO3 §12・§13・§14・§17 (Accessibility 行)。
- **Related Service Design ID**: SDP-007・NVP-008・CTA-009・CTP-008。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-013 (Accessibility 節)。
- **Original Observation Classification**: 一部のみ確認できる (WO2 では SDP-007 に「対応を直接確認できる / 一部のみ確認できる」を併記)。
- **Direct Evidence Referenced by Source**: semantic `color.focus.ring` (outline ベース)・components.md focus 適用。
- **Shared Observation**: focus リング token が存在し、Navigation・CTA・Content・Accessibility の複数責務にまたがって「一部のみ確認できる」と観察されている。
- **Source-specific Variation**: WO2 は横断責務 (SDP-007/NVP-008/CTA-009) として、WO3 は各 SCR の Accessibility 節として記録。差異は §16 に再掲しない (責務が同一の focus 可視化であり、記録位置のみ異なる)。
- **Provenance**: 適用規格・達成レベルが未定義 (具体規格未定義は各元評価が Does Not Decide とする)。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 一部のコントラストが用途により未達可能性を JSON `$note` が自認 (WO2 §8.1 `color.border.default`)。矛盾ではなく DS 側自認の未確定。
- **Unresolved Dependency**: 適用規格・達成レベルの確定主体 (§19)。
- **Downstream Impact**: Implementation の focus 実装方式 (Repository 管理対象外)。
- **Open Issue**: 具体規格・達成レベル未定義。
- **Does Not Decide**: 適用規格・達成レベル・実装方式は本集約で決めない。

### T-02 状態色 token と状態表現の一部対応

- **Assessment Dimension**: Foundation / token (State and Feedback 整理軸に関係)。
- **Design Responsibility**: 状態 (success/error 等) の色による表現。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-005)・§8.4 (CTP-006)・§8.5 (CTA-007)・§8.1 (SDP-004 用途ベース命名)、WO3 §14 (SCR-003 状態可視)・§15 (SCR-004 State)。
- **Related Service Design ID**: SDP-005・SDP-004・CTP-006・CTA-007・NVP-005。
- **Related SCR**: SCR-003・SCR-004。
- **Original Observation Classification**: 一部のみ確認できる, placeholder (併記)。
- **Direct Evidence Referenced by Source**: semantic `color.state.success`/`color.state.error`・components.md 状態固定リスト (hover/active/focus/disabled/loading/error/success)・Input error (`color.state.error` 🚧暫定)。
- **Shared Observation**: success/error 中心の状態色 token は存在するが、上流の状態モデル全体 (Status and Uncertainty Model・CTA State Model の Pending Confirmation 等) には「一部のみ確認できる」。
- **Source-specific Variation**: SCR-003 は Input の disabled/success が未取得、SCR-004 は motion placeholder を伴う。差異は §16 に再掲。
- **Provenance**: 用途ベース命名の正本 `governance/naming-rules.md` は参照切れ (X-07 と関係)。
- **Placeholder / Inspection Pending**: ボタン状態は未取得 (follow-up #4)・Input error は暫定 placeholder・disabled/success 実査待ち。
- **Broken Reference**: `governance/naming-rules.md` 不在 (命名規則の正本)。
- **Conflict or Gap**: 上流状態モデルの網羅と DS 側 success/error 中心との差 (対応する定義を確認できない部分は X-03 に集約)。
- **Unresolved Dependency**: 状態モデル (Navigation State / CTA State / Content Status) と DS 状態表現の対応整理 (§19)。
- **Downstream Impact**: Implementation の状態表示 (Repository 管理対象外)。
- **Open Issue**: 状態一覧・状態表示 Component の確定。
- **Does Not Decide**: 状態の具体一覧・業務定義・token 名/値は本集約で決めない。

### T-03 Typography スケール

- **Assessment Dimension**: Foundation / token。
- **Design Responsibility**: 可読性・スキャン容易性を支えるタイポグラフィスケール。
- **Source Assessment / Source Section**: WO2 §8.4 (CTP-008)。
- **Related Service Design ID**: CTP-008。
- **Related SCR**: — (WO3 の各 Accessibility 節は focus/非視覚依存が中心で、typography スケールは主に WO2 横断責務として記録)。
- **Original Observation Classification**: 対応を直接確認できる / 一部のみ確認できる (併記)。
- **Direct Evidence Referenced by Source**: design.md §3 タイポグラフィスケール (rem 基準)・primitive `typography.size.*`。
- **Shared Observation**: タイポグラフィスケールの記述は確認できる (対応を直接確認できる) が、文字数制限・具体規格は未定義 (一部のみ確認できる)。
- **Source-specific Variation**: 該当なし (WO2 横断責務として単一記録)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 具体規格・文字数制限の不足 (一部のみ確認できる)。
- **Unresolved Dependency**: タイポグラフィ具体仕様の確定主体。
- **Downstream Impact**: Implementation のタイポグラフィ適用 (Repository 管理対象外)。
- **Open Issue**: タイポグラフィ・文字数制限・Component 仕様 (CTP-008 Does Not Decide)。
- **Does Not Decide**: タイポグラフィ仕様は本集約で決めない。

### T-04 Accent/campaign 色 token による Fact/Promotion 分離の基盤

- **Assessment Dimension**: Foundation / token (Cross-cutting の X-02 と密接に関係)。
- **Design Responsibility**: 販促・キャンペーン表現を色の点使用に限定し、通常導線と分離する token 基盤。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-003)・§8.4 (CTP-010)・§8.5 (CTA-010)、WO3 §12 (SCR-001)・§13 (SCR-002)・§16 (SCR-005)・§18 (SCR-014)。
- **Related Service Design ID**: SDP-003・CTP-010・CTA-010。
- **Related SCR**: SCR-001・SCR-002・SCR-005・SCR-014。
- **Original Observation Classification**: 対応を直接確認できる, provenance 未確認 (併記)。
- **Direct Evidence Referenced by Source**: semantic `color.accent.campaign`「バッジ/割引ラベルの点専用・ボタン塗り禁止 (TVL-0012)」・design.md「特集と通常導線を色で分離」。
- **Shared Observation**: accent 点専用 token は複数 SCR/SD で「対応を直接確認できる」として一致し、Fact/Promotion 分離の X-02 を token 面から支える。
- **Source-specific Variation**: 参照する TVL Decision ID が文書により TVL-0012 単独 (SCR-001/005) または TVL-0011/0012 (SCR-002/014) と異なる。差異は §16 に再掲。
- **Provenance**: TVL-0011・TVL-0012 の ADR 正本なし → provenance 未確認 (適合確定にしない)。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし (accent token 自体は実在)。
- **Conflict or Gap**: 該当なし (直接的矛盾は入力評価で確認されていない)。
- **Unresolved Dependency**: TVL Decision ID の provenance と有効性 (§17・§19)。
- **Downstream Impact**: Implementation の販促表示 (Repository 管理対象外)。
- **Open Issue**: 広告表示ルール・キャンペーン方針は各元評価が Does Not Decide とする。
- **Does Not Decide**: 販促施策・token 値は本集約で決めない。

### T-05 Price/Review 表現 token

- **Assessment Dimension**: Foundation / token (Component C-04/C-05 と関係)。
- **Design Responsibility**: 価格・評価の視覚表現を支える token。
- **Source Assessment / Source Section**: WO2 §8.2 (IA-OBJ-007/009)、WO3 §15 (SCR-004)。
- **Related Service Design ID**: IA-OBJ-007・IA-OBJ-009。
- **Related SCR**: SCR-004。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち (併記)。
- **Direct Evidence Referenced by Source**: semantic `font.price.*`・`color.icon.rating`・`icon.reviewSize`。
- **Shared Observation**: 価格・評価用の token が存在し「一部のみ確認できる」。表現語彙であり業務モデル (料金構造・評価対象) の決定ではない。
- **Source-specific Variation**: SCR-004 では PriceTag「円」weight 正規化が ❓ 実査待ち。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 「円」weight は ❓ 実査待ち。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 該当なし。
- **Unresolved Dependency**: 料金構造・評価対象の業務モデル (上流 IA Open Issue)。
- **Downstream Impact**: Implementation の価格/評価表示 (Repository 管理対象外)。
- **Open Issue**: 料金構造・表示単位・Review 提供元 (IA-OBJ-007/009 の扱い)。
- **Does Not Decide**: 料金/評価の業務モデル・token 値は本集約で決めない。

### T-06 radius / shadow / motion placeholder token 群

- **Assessment Dimension**: Foundation / token。
- **Design Responsibility**: 角丸・影・モーションの視覚表現 (未確定値を含む)。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-005)・§11、WO3 §15 (SCR-004)・§11 Baseline Constraints。
- **Related Service Design ID**: SDP-005 (State Visibility の一部)。
- **Related SCR**: SCR-004 (Card/State の placeholder 影響)。
- **Original Observation Classification**: placeholder。
- **Direct Evidence Referenced by Source**: semantic `radius.card`・`motion.transition.duration`・`motion.transition.easing`、primitive `shadow.sm/md/lg`・`motion.duration.fast/base/slow`・`motion.easing.standard` (計 10、baseline 継承)。
- **Shared Observation**: motion/shadow/radius の placeholder token は Card 表現 (C-03) と状態遷移表現 (T-02/X-03) に影響する未確定要素として複数評価で参照される。
- **Source-specific Variation**: 該当なし (baseline 由来の共通制約)。
- **Provenance**: `radius.card` は TVL 由来の follow-up を伴う (baseline 記録)。
- **Placeholder / Inspection Pending**: 計 10 の placeholder token (§17 に集約)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 該当なし。
- **Unresolved Dependency**: placeholder token の解決主体 (§19)。
- **Downstream Impact**: Implementation のモーション/影適用 (Repository 管理対象外)。
- **Open Issue**: placeholder / 実査待ちトークンの解決。
- **Does Not Decide**: placeholder の解消方法・token 値は本集約で決めない。

### T-07 token 参照内部整合性と DS 独立性

- **Assessment Dimension**: Foundation / token。
- **Design Responsibility**: サービス全体の一貫性 (SDP-009) を支える DS 内部整合。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-009)・§9、WO3 §11 Baseline Constraints。
- **Related Service Design ID**: SDP-009。
- **Related SCR**: — (baseline 継承の DS 内部整合であり、個別 SCR 固有ではない)。
- **Original Observation Classification**: 対応を直接確認できる。
- **Direct Evidence Referenced by Source**: baseline で確認した semantic→primitive 参照 63/63 解決・design.md「独立 DS・他サービスと値を共有しない (R1)」。
- **Shared Observation**: DS 内部の token 参照は整合しており (対応を直接確認できる)、SDP-009 の一貫性を内部整合の面から支える。
- **Source-specific Variation**: 該当なし。
- **Provenance**: 該当なし (baseline で機械確認済み)。
- **Placeholder / Inspection Pending**: 該当なし (内部整合は解決済み)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 該当なし。
- **Unresolved Dependency**: 該当なし (本集約は再決定しない)。
- **Downstream Impact**: 該当なし。
- **Open Issue**: 該当なし (内部整合は baseline で確認済み)。
- **Does Not Decide**: token 階層・命名規則の正式確定は本集約で決めない。

## 14. Component / Pattern Observations

Assessment Dimension: Component / pattern (Alignment Plan §9 の整理軸)。既存 Component 名を必要 Component 一覧・利用要求へ変換しない。Component 存在を CTA/NAV 対応の確定としない。

### C-01 Button と CTA の明確性・主要行動

- **Assessment Dimension**: Component / pattern (CTA 整理軸)。
- **Design Responsibility**: 行動の明確性・1 画面 1 主 CTA・情報確認と選択の区別。
- **Source Assessment / Source Section**: WO2 §8.5 (CTA-001/002)、WO3 §12 (SCR-001 CTA-002)・§14 (SCR-003 CTA)・§15 (SCR-004 CTA-002)・§16 (SCR-005 CTA-002/004)。
- **Related Service Design ID**: CTA-001・CTA-002・CTA-004。
- **Related SCR**: SCR-001・SCR-003・SCR-004・SCR-005。
- **Original Observation Classification**: CTA-002「主 CTA は primary 1 つ」は対応を直接確認できる、CTA-001/004 等は一部のみ確認できる (併記)。いずれも variant 語彙は provenance 未確認。
- **Direct Evidence Referenced by Source**: components.md Button Do「1 画面の主 CTA は primary 1 つに絞る」・variant primary/secondary/ghost/text。
- **Shared Observation**: 「主 CTA を primary 1 つに絞る」責務は Button の Do 記述と複数評価で「対応を直接確認できる」として一致する。
- **Source-specific Variation**: SCR-005 は情報確認と Room/Stay Plan 選択の区別 (CTA-004) を Button variant で「一部のみ」表現、SCR-004 は比較・選択の優先関係を「一部のみ」とする。差異は §16 に再掲。
- **Provenance**: Button variant 語彙は GOV-0002 由来だが ADR 正本なし → provenance 未確認 (適合確定にしない)。
- **Placeholder / Inspection Pending**: ボタン状態は未取得 (follow-up #4, C-08/T-02 と関係)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 該当なし (直接的矛盾は入力評価で確認されていない)。
- **Unresolved Dependency**: 主要 CTA の確定 (各 SCR で主要行動が未定義)・GOV-0002 provenance (§19)。
- **Downstream Impact**: 各 SCR §15 Downstream Impact の Button 例を採用決定と解釈しない。
- **Open Issue**: 主要 CTA の確定・variant 語彙の provenance。
- **Does Not Decide**: 主要 CTA の確定・variant の追加改廃は本集約で決めない。

### C-02 SearchForm / Input と検索・入力責務

- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 検索条件の指定・確認・変更、入力の状態表現・回復。
- **Source Assessment / Source Section**: WO2 §8.2 (IA-OBJ-002)・§8.1 (SDP-006)、WO3 §12 (SCR-001 Info Resp.)・§14 (SCR-003 §5/§6・CTA・Error 回復)。
- **Related Service Design ID**: IA-OBJ-002・SDP-006・CTA-001/005・CTP-007。
- **Related SCR**: SCR-001・SCR-003。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち (併記)。SearchForm の検索開始 CTA は対応を直接確認できる (SCR-003)。
- **Direct Evidence Referenced by Source**: components.md SearchForm「Input 群 + 主 CTA」「検索実行 CTA は Button.primary」・Input.default・Input error text 併記。
- **Shared Observation**: SearchForm/Input は検索起点の表現語彙として複数評価で「一部のみ確認できる」。検索開始 CTA (Button.primary) は「対応を直接確認できる」。
- **Source-specific Variation**: SCR-001 は入口の探索起点、SCR-003 は入力項目・バリデーション・条件保持が Open Issue で Input 状態一式が実査待ち。差異は §16 に再掲。
- **Provenance**: Button variant GOV-0002 provenance 未確認。
- **Placeholder / Inspection Pending**: Input 状態一式は follow-up #2 実査待ち・error は暫定 placeholder。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 入力項目・必須条件・バリデーションが上流 Open Issue のため DS 対応を確定できない (一部のみ確認できる)。
- **Unresolved Dependency**: 入力項目・バリデーション・条件保持方式の未定義 (§19)。
- **Downstream Impact**: Implementation の検索/入力実装 (Repository 管理対象外)。
- **Open Issue**: 入力項目・必須条件・バリデーション・履歴保持 UI の未定義。
- **Does Not Decide**: 入力項目・必須条件・バリデーション・履歴保持の確定は本集約で決めない。

### C-03 Card と Accommodation の表現

- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 宿泊施設候補・関連施設の視覚表現。
- **Source Assessment / Source Section**: WO2 §8.2 (IA-OBJ-003)、WO3 §13 (SCR-002 Supporting)・§15 (SCR-004)・§16 (SCR-005)・§18 (SCR-014 Supporting)。
- **Related Service Design ID**: IA-OBJ-003。
- **Related SCR**: SCR-002・SCR-004・SCR-005・SCR-014。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち, placeholder (併記)。
- **Direct Evidence Referenced by Source**: components.md Card (ResultCard, 8 スロット media/title/meta/rating/price/badge/description/actions)。
- **Shared Observation**: Card は Accommodation の表現語彙として複数 SCR で「一部のみ確認できる」。IA Object を Component と同一視しない。
- **Source-specific Variation**: SCR-004 は Card の実 px・8 スロット対応付けが実査待ち・`radius.card`/shadow が placeholder。SCR-005 は Card が検索結果向けで詳細用途は実査待ち。SCR-002/014 は Supporting としての一部表現。差異は §16 に再掲。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: Card 実 px・8 スロット対応付けは実査待ち・`radius.card`/shadow placeholder (T-05/T-06 と関係)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 表示項目・表示順が上流 Open Issue のため DS 対応を確定できない。Downstream Impact の Card 例を採用決定としない。
- **Unresolved Dependency**: 表示項目・表示順・比較成立基準の未定義 (§19)。
- **Downstream Impact**: 各 SCR Downstream Impact の Card 例を採用決定と解釈しない。
- **Open Issue**: 表示項目・表示順・詳細用途の対応。
- **Does Not Decide**: 一覧/詳細 UI・表示項目・Card の採用決定は本集約で決めない。

### C-04 PriceTag と価格・条件の表現

- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 価格および税・条件の併記表現 (行動前の条件提示)。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-003)・§8.2 (IA-OBJ-007)・§8.5 (CTA-005)、WO3 §15 (SCR-004)。
- **Related Service Design ID**: IA-OBJ-007・CTA-005・SDP-003・CTP-003。
- **Related SCR**: SCR-004。
- **Original Observation Classification**: 一部のみ確認できる (併記, 実査待ちを伴う)。
- **Direct Evidence Referenced by Source**: components.md PriceTag「税・条件の補助テキストを必ず併記できる構造」・semantic `font.price.*`。
- **Shared Observation**: PriceTag は価格表現と条件併記構造を持ち「一部のみ確認できる」。条件提示 (CTA-005) を構造面から支える。
- **Source-specific Variation**: SCR-004 では「円」weight 正規化が ❓ 実査待ち (T-05 と関係)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 「円」weight は ❓ 実査待ち。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 価格構造・表示位置は上流 Does Not Decide。
- **Unresolved Dependency**: 料金構造・表示単位の業務モデル (§19)。
- **Downstream Impact**: Implementation の価格表示 (Repository 管理対象外)。
- **Open Issue**: 価格構造・表示位置。
- **Does Not Decide**: 価格構造・表示位置・token 値は本集約で決めない。

### C-05 ReviewStars と評価の表現

- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 評価 (レビュー) の視覚表現 (数値併記による非視覚依存)。
- **Source Assessment / Source Section**: WO2 §8.2 (IA-OBJ-009)、WO3 §15 (SCR-004)・§16 (SCR-005)。
- **Related Service Design ID**: IA-OBJ-009。
- **Related SCR**: SCR-004・SCR-005。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち (併記)。
- **Direct Evidence Referenced by Source**: components.md ReviewStars (表示のみ・数値併記)・semantic `color.icon.rating`・`icon.reviewSize`。
- **Shared Observation**: ReviewStars は評価表現語彙として「一部のみ確認できる」。数値併記は非視覚依存 (X-04) を支える。
- **Source-specific Variation**: SCR-005 では星実寸が実査待ち。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 星実寸は実査待ち (SCR-005)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: Review の提供元・評価対象・信頼性は上流 Open Issue。
- **Unresolved Dependency**: Review の業務モデル (§19)。
- **Downstream Impact**: Implementation の評価表示 (Repository 管理対象外)。
- **Open Issue**: Review 提供元・評価対象・信頼性。
- **Does Not Decide**: Review の業務モデル・token 値は本集約で決めない。

### C-06 Header / Breadcrumb / Footer と Navigation component

- **Assessment Dimension**: Component / pattern (Navigation 整理軸)。
- **Design Responsibility**: 現在地の可視化・移動を表現し得る component (Navigation 責務)。CTA とは別責務 (X-01)。
- **Source Assessment / Source Section**: WO2 §8.3 (NVP-001・NAV-001〜006)、WO3 §12 (SCR-001 NAV-001/004/006)・§13 (SCR-002 NAV-001/002/003)・§14 (SCR-003 NAV-004/005)・§15 (SCR-004 NAV-002/003/004/005)・§16 (SCR-005 NAV-002/003/004/006)・§17 (SCR-013 NAV-001/002/003/006)・§18 (SCR-014 NAV-001/002/003)。
- **Related Service Design ID**: NVP-001・NAV-001〜006。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: 一部のみ確認できる / 対応する定義を確認できない (併記)。
- **Direct Evidence Referenced by Source**: components.md Header (ロゴ/ナビゲーション/会員導線)・Breadcrumb (階層ナビゲーション・現在地非リンク `color.text.muted`)・Footer。DS 側に NAV-ID との対応記述はない。
- **Shared Observation**: 移動を表現し得る component は存在する (一部のみ確認できる) が、NAV-001〜006 分類との明示的対応は DS に記述がない (対応する定義を確認できない)。component 存在を NAV-ID 対応と判定しない。
- **Source-specific Variation**: SCR ごとに参照する NAV 分類が異なる (SCR-001 は NAV-001/004/006、SCR-003 は NAV-004/005 の History and Recovery 等)。SCR ごとに異なる Navigation Types を共通一覧へ正規化しない。差異は §16 に再掲。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし (component は実在)。
- **Conflict or Gap**: NAV 分類との対応記述の不在 (対応する定義を確認できない)。Global Navigation 対象領域・History and Recovery 保持方式は各 NAV/SCR の Open Issue。
- **Unresolved Dependency**: Navigation State モデル・NAV 分類と DS 表現の対応整理 (§19、X-01/X-03 と関係)。
- **Downstream Impact**: Implementation のナビゲーション実装 (Repository 管理対象外)。
- **Open Issue**: NAV 分類対応・Global Nav 対象領域・History and Recovery 保持方式。
- **Does Not Decide**: Navigation component と NAV-ID の対応確定は本集約で決めない。

### C-07 Modal / Overlay と可逆操作・回復

- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 可逆操作・回復可能性 (Recoverability) の表現。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-006)・§8.5 (CTA-006)。
- **Related Service Design ID**: SDP-006・CTA-006。
- **Related SCR**: — (WO3 では SCR-003 の Error 回復が Input 中心で C-02 に集約。Modal/Overlay 自体は WO2 横断責務として記録)。
- **Original Observation Classification**: SDP-006 は一部のみ確認できる、CTA-006 は対応する定義を確認できない (併記)。
- **Direct Evidence Referenced by Source**: components.md Modal / Overlay (drawer 統一 TVL-0007)・Input「エラーはテキストメッセージ併記」。
- **Shared Observation**: Modal/Overlay は存在するが、可逆/不可逆を区別する DS 側の明示規則は確認できない (CTA-006 は対応する定義を確認できない)。
- **Source-specific Variation**: 該当なし。
- **Provenance**: drawer 統一の TVL-0007 は provenance 未確認。
- **Placeholder / Inspection Pending**: Input 状態一式は実査待ち (follow-up #2, C-02 と関係)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 可逆/不可逆区別規則の不在 (対応する定義を確認できない)。保存期間・Undo・エラー処理仕様は上流 Does Not Decide。
- **Unresolved Dependency**: 可逆/不可逆の区別規則の扱い (§19)。
- **Downstream Impact**: Implementation の回復フロー (Repository 管理対象外)。
- **Open Issue**: 可逆/不可逆区別・保存期間・Undo・エラー処理。
- **Does Not Decide**: 可逆/不可逆規則・エラー処理仕様は本集約で決めない。

### C-08 Recovery Action 用 component / 規則の不在

- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 中断・エラーからの回復行動 (Recovery Action) の表現。
- **Source Assessment / Source Section**: WO3 §17 (SCR-013 CTA Recovery Action)。関連: WO2 §8.5 (CTA-007 の Pending Confirmation・状態)。
- **Related Service Design ID**: CTA-TYPE-004・CTA-007。
- **Related SCR**: SCR-013。
- **Original Observation Classification**: 対応する定義を確認できない / 一部のみ確認できる (併記)。
- **Direct Evidence Referenced by Source**: components.md 状態固定リストに error/loading はあるが、Recovery Action 用の component/規則は確認できない。
- **Shared Observation**: error/loading 状態表現は一部あるが、Recovery Action (CTA-TYPE-004) に対応する DS 側の component/規則は「対応する定義を確認できない」。
- **Source-specific Variation**: SCR-013 固有 (支援領域の回復行動)。§16 に再掲。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: ボタン状態は未取得 (follow-up #4)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: Recovery Action 用の DS 規則の不在 (対応する定義を確認できない)。問い合わせ手段・処理フローは上流 Open Issue。
- **Unresolved Dependency**: 問い合わせ手段・処理フローの未定義 (§19)。
- **Downstream Impact**: Implementation の回復動線 (Repository 管理対象外)。
- **Open Issue**: 問い合わせ手段・処理フロー・サポート対象範囲。
- **Does Not Decide**: Recovery Action の component/規則は本集約で決めない。

### C-09 支援・FAQ・Policy 表現 component の不在 (未着手 component)

- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 支援 (FAQ/問い合わせ/Support)・Policy 本文の表現。
- **Source Assessment / Source Section**: WO3 §17 (SCR-013 §7・Does Not Decide の Accordion 等)。
- **Related Service Design ID**: CTP-003・CTP-006・CTP-010 (Editorial and Support / Conditions and Policies)。
- **Related SCR**: SCR-013。
- **Original Observation Classification**: 対応する定義を確認できない (Accordion 等は未着手と明記)。
- **Direct Evidence Referenced by Source**: components.md 未着手 component 一覧に Accordion (実体皆無と明記)。SR も Downstream Impact で Accordion 等を指定しないと明記。
- **Shared Observation**: 支援領域の表現語彙に対応する DS component は確認できない。未着手 component (Accordion 等) の存在を必要 Component または改訂候補へ変換しない。
- **Source-specific Variation**: SCR-013 固有。§16 に再掲。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし (未着手 = 成果物不在であり placeholder とは区別)。
- **Broken Reference**: 文言正本 brand-content.md 不在 (X-07 と関係)。
- **Conflict or Gap**: 支援・Policy 表現 component の不在 (対応する定義を確認できない)。未着手を必要性へ変換しない。
- **Unresolved Dependency**: サポート対象範囲・FAQ 構成の未定義 (§19)。
- **Downstream Impact**: Implementation の支援 UI (Repository 管理対象外)。未着手 component の必要性評価は後続。
- **Open Issue**: 未着手 component (Accordion 等) の必要性評価・サポート範囲・FAQ 構成。
- **Does Not Decide**: Accordion/フォーム/チャット/モーダル等の採用・追加は本集約で決めない。

### C-10 Destination / Room / Stay Plan / Policy / Content 等の専用表現語彙の不在

- **Assessment Dimension**: Component / pattern (IA Object 整理軸、X-06 と密接)。
- **Design Responsibility**: 宿泊領域の IA Object を UI として表現する専用語彙。
- **Source Assessment / Source Section**: WO2 §8.2 (IA-OBJ-001/004/005/006/008/010/011/012)、WO3 §12 (SCR-001 Destination/Content)・§13 (SCR-002 Destination/Content)・§14 (SCR-003 User)・§15 (SCR-004 Policy)・§16 (SCR-005 Room/Stay Plan/Policy)。
- **Related Service Design ID**: IA-OBJ-001・IA-OBJ-004・IA-OBJ-005・IA-OBJ-006・IA-OBJ-008・IA-OBJ-010・IA-OBJ-011・IA-OBJ-012。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-004・SCR-005。
- **Original Observation Classification**: 対応する定義を確認できない。
- **Direct Evidence Referenced by Source**: 専用 component を確認できない (WO2 §8.2)。認証/会員 component なし (SCR-003 User)。Policy/Room/Stay Plan の専用 component なし。
- **Shared Observation**: SearchForm/Card/PriceTag/ReviewStars が対応する IA Object は一部のみで、Destination/Room/Stay Plan/Availability/Policy/Booking/User/Content の専用表現語彙は「対応する定義を確認できない」。専用語彙の不在は 1 対 1 対応の欠如であり、直ちに component 追加を要する結論ではない。
- **Source-specific Variation**: SCR-005 は Room/Stay Plan/Policy の業務モデルが Open Issue、SCR-003 は User (認証・会員・履歴保存) を上流制約で取り込まない。差異は §16 に再掲。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: Content 文言は brand-content.md 参照切れ (X-07 と関係)。
- **Conflict or Gap**: 専用表現語彙の不在 (対応する定義を確認できない)。IA Object の内容・関係・業務仕様は IA §11 Open Issue。
- **Unresolved Dependency**: IA Object の業務モデル・SCR-005/SCR-006 境界の未定義 (§19)。
- **Downstream Impact**: Implementation の各領域表現 (Repository 管理対象外)。
- **Open Issue**: 専用表現語彙の扱い・業務モデルの未定義。
- **Does Not Decide**: 専用 component の要否・IA Object と Component の同一視は本集約で決めない。

## 15. Cross-cutting Observations

Assessment Dimension: Cross-cutting (Alignment Plan §9 の整理軸)。複数の Service Design 責務・SCR にまたがる関係を可視化する。以下の見出しは説明用整理軸であり新しい正式分類・Decision ではない。

### X-01 Navigation と CTA の責務分離

- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: Navigation 要素と CTA 要素を別 Pattern・別評価軸で扱う (UXDR-TRAVEL-003)。
- **Source Assessment / Source Section**: WO2 §8.6 (UXDR-TRAVEL-003)・§8.3 (NAV)・§8.5 (CTA-002)、WO3 全 SCR の Navigation 節と CTA 節 (§12〜§18)。
- **Related Service Design ID**: UXDR-TRAVEL-003・NAV-001〜006・CTA-002。
- **Related SCR**: SCR-001〜SCR-005・SCR-013・SCR-014 (Navigation と CTA を各節で別責務として評価)。
- **Original Observation Classification**: 一部のみ確認できる / 対応する定義を確認できない (併記)。
- **Direct Evidence Referenced by Source**: components.md は Button (CTA) と Header/Breadcrumb (Navigation) を別 component として定義するが、NAV/CTA の責務分離を述べる DS 本文規則は確認できない (WO2 §8.6)。
- **Shared Observation**: component 単位では Navigation と CTA が別扱い (一部のみ確認できる) だが、責務分離を述べる DS 側の本文規則は不在 (対応する定義を確認できない)。集約でも両責務を混同せず、Header/Breadcrumb 存在で NAV 対応済み・Button 存在で CTA 対応済みとしない。
- **Source-specific Variation**: 該当なし (全 SCR で一貫して別責務として集約)。
- **Provenance**: Button variant GOV-0002 provenance 未確認 (C-01 と関係)。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: NAV/CTA 責務分離を述べる DS 本文規則の不在 (対応する定義を確認できない)。
- **Unresolved Dependency**: 責務分離規則の扱い (§19)。
- **Downstream Impact**: Implementation の Navigation/CTA 実装 (Repository 管理対象外)。
- **Open Issue**: NAV/CTA 責務分離規則の DS 側記述の扱い。
- **Does Not Decide**: 責務分離規則の追加は本集約で決めない。

### X-02 Fact / Decision / Promotion の分離

- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: 事実・判断・販促を分離し、根拠のない優位性/人気/緊急性を確定情報として扱わない。
- **Source Assessment / Source Section**: WO2 §8.4 (CTP-010)・§8.5 (CTA-010)・§8.1 (SDP-003/008)、WO3 §12 (SCR-001)・§13 (SCR-002)・§15 (SCR-004 CTP-004/006)・§16 (SCR-005)・§18 (SCR-014 CTP-010/CTA-010/CTP-004)。
- **Related Service Design ID**: CTP-010・CTA-010・CTP-004・SDP-003・SDP-008。
- **Related SCR**: SCR-001・SCR-002・SCR-004・SCR-005・SCR-014。
- **Original Observation Classification**: 対応を直接確認できる (accent 点専用・根拠なき人気非確定)、一部に provenance 未確認 (TVL)。
- **Direct Evidence Referenced by Source**: design.md「根拠のない人気・ランキング・限定・希少性・緊急性を確定情報として扱わない」・semantic `color.accent.campaign` 点専用 (TVL-0011/0012)・「特集と通常導線を色で分離」。
- **Shared Observation**: Fact/Promotion 分離と根拠なき表現の排除は複数 SCR/SD で「対応を直接確認できる」として一致する最も広く共有された Observation。token 面は T-04 が支える。
- **Source-specific Variation**: 参照する TVL Decision ID が文書により異なる (T-04 と同じ差異)。§16 に再掲。
- **Provenance**: TVL-0011・TVL-0012 の ADR 正本なし → provenance 未確認。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 販促と対になる文言正本 brand-content.md 不在 (X-07 と関係)。
- **Conflict or Gap**: 該当なし (直接的矛盾は入力評価で確認されていない)。
- **Unresolved Dependency**: TVL provenance・広告表示ルール (§19)。
- **Downstream Impact**: Implementation の販促/編集表示 (Repository 管理対象外)。
- **Open Issue**: 広告表示ルール・キャンペーン方針・ランキング基準。
- **Does Not Decide**: 販促施策・ランキング基準は本集約で決めない。

### X-03 状態・不確実性モデルと DS 状態表現

- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: Navigation State Model・CTA State Model・Status and Uncertainty Model の表現。
- **Source Assessment / Source Section**: WO2 §8.3 (Navigation State Model)・§8.4 (CTP-006)・§8.5 (CTA-007)・§8.1 (SDP-002/005)、WO3 §12〜§18 の State 節。
- **Related Service Design ID**: Navigation State Model・CTA State Model・Status and Uncertainty Model・CTP-006・CTA-007・SDP-002/005。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014 (State 節)。
- **Original Observation Classification**: 対応する定義を確認できない (状態モデル全体)、一部は一部のみ確認できる, placeholder (success/error)。
- **Direct Evidence Referenced by Source**: semantic `color.state.success`/`error`・components.md 状態固定リスト・`elevation.sticky` (Header sticky)。CTA State Model の Pending Confirmation・Navigation State 各状態に対応する DS 定義は確認できない (WO2)。
- **Shared Observation**: DS 側は success/error 中心の状態色 (一部のみ確認できる) を持つが、Navigation State Model の各状態・CTA State Model の Pending Confirmation・Status and Uncertainty Model の網羅には「対応する定義を確認できない」。状態モデルを Component state と同一視しない。
- **Source-specific Variation**: SCR ごとに宣言される Navigation States が異なる (SCR-001 Entry/Exploring、SCR-004 Exploring/Evaluating/Error / Interrupted、SCR-014 Entry/Exploring/Evaluating で Error / Interrupted 非含有 等)。SCR ごとに異なる状態を共通一覧へ正規化せず、SCR-014 に存在しない `Error / Interrupted` を追加しない。差異は §16 に再掲。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: ボタン状態 follow-up #4・motion placeholder (T-02/T-06 と関係)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 状態モデルと DS 状態表現の対応不足 (対応する定義を確認できない / 一部のみ確認できる)。
- **Unresolved Dependency**: 状態モデル (Navigation State / CTA State / Content Status) と DS 状態表現の対応整理 (§19)。
- **Downstream Impact**: Implementation の状態遷移表示 (Repository 管理対象外)。
- **Open Issue**: 状態一覧・状態表示 Component・空結果/在庫切れ挙動。
- **Does Not Decide**: 状態の具体一覧・業務定義・UI 表現は本集約で決めない。

### X-04 Accessibility の非依存原則

- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: 色・アイコン・位置・画像だけに意味を依存させない (アクセシビリティ既定)。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-007)・§8.4 (CTP-008)・§8.3 (NVP-008)・§8.5 (CTA-009)、WO3 各 SCR の Accessibility 節 (§12・§13・§14・§17・§18)。
- **Related Service Design ID**: SDP-007・NVP-008・CTP-008・CTA-009。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-013・SCR-014。
- **Original Observation Classification**: 対応を直接確認できる (方針の記述あり) / 一部のみ確認できる (具体規格未定義) の併記。
- **Direct Evidence Referenced by Source**: design.md §2「WCAG 2.2 AA を最低ライン」・components.md「色/アイコン/位置だけに意味を依存させない」(ReviewStars 数値併記・Input エラーテキスト併記)・semantic `color.focus.ring`・design.md 画像比率 (object-fit)。
- **Shared Observation**: 非視覚依存の方針記述は複数評価で「対応を直接確認できる」だが、適用規格・達成レベルは未定義で「一部のみ確認できる」。focus token 面は T-01 が支える。
- **Source-specific Variation**: SCR-014 は画像欠落 fallback が ❓ 実査待ち。差異は §16 に再掲。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 画像欠落 fallback は ❓ 実査待ち (SCR-014)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 一部コントラスト未達可能性を JSON `$note` が自認 (T-01 と関係)。具体規格未定義。
- **Unresolved Dependency**: 適用規格・達成レベル・画像 fallback の確定 (§19)。
- **Downstream Impact**: Implementation のアクセシビリティ実装 (Repository 管理対象外)。
- **Open Issue**: 適用規格・達成レベル・画像仕様。
- **Does Not Decide**: 適用規格・達成レベル・実装方式・画像仕様は本集約で決めない。

### X-05 未確定事項の保持 (placeholder / 実査待ちの伝播)

- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: 未取得を確定値化せず placeholder / Open Issue として保持する (UXDR-TRAVEL-001)。
- **Source Assessment / Source Section**: WO2 §8.1 (SDP-008/010)・§8.6 (UXDR-TRAVEL-001)、WO3 §11 Baseline Constraints・各 SCR の Provenance/Placeholder 節。
- **Related Service Design ID**: UXDR-TRAVEL-001・SDP-008・SDP-010。
- **Related SCR**: SCR-001・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014 (placeholder/実査待ちを記録する SCR)。
- **Original Observation Classification**: 対応を直接確認できる (DS が未取得を placeholder として保持し推測補完していない)。
- **Direct Evidence Referenced by Source**: JSON `$status: placeholder` + `$note`・design.md 未確定事項一覧 (🚧/❓) の維持 (TVL-0008 は provenance 未確認)。
- **Shared Observation**: DS が未確定を placeholder/実査待ちとして保持する運用は「対応を直接確認できる」。この運用が §17 の placeholder/実査待ち影響の前提となる。
- **Source-specific Variation**: 該当なし (横断的な運用)。
- **Provenance**: TVL-0008・TVL-0010 等 placeholder に紐づく Decision ID は provenance 未確認。
- **Placeholder / Inspection Pending**: 計 10 の placeholder token (§17)。
- **Broken Reference**: 該当なし。
- **Conflict or Gap**: 該当なし。
- **Unresolved Dependency**: placeholder / 実査待ちの解決主体 (§19)。
- **Downstream Impact**: 未確定事項が下流へ引き継がれること (Assets/Implementation)。
- **Open Issue**: placeholder / 実査待ちの解決。
- **Does Not Decide**: placeholder の解消方法は本集約で決めない。

### X-06 IA Object と表現語彙の非 1 対 1

- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: IA Object を UI/Component/データモデルと同一視せず、表現語彙として扱う (UXDR-TRAVEL-002・IA §9/§10)。
- **Source Assessment / Source Section**: WO2 §8.2 (IA 全般)・§8.6 (UXDR-TRAVEL-002)・§8.4 (Content Categories)、WO3 §12〜§18 の Info Responsibilities / Content 節。
- **Related Service Design ID**: IA-OBJ-001〜012・Content Categories (6)・UXDR-TRAVEL-002。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: 一部のみ確認できる (対応する語彙がある IA Object) / 対応する定義を確認できない (専用語彙のない IA Object・Content Category) の併記。
- **Direct Evidence Referenced by Source**: design.md/components.md は token・component 単位で構成され画面候補単位の固定 UI 定義を持たない (UXDR-TRAVEL-002)。IA §10「Design System は各情報オブジェクトや状態を UI として表現する設計語彙を提供する」。Content Category 名との対応記述は DS になし。
- **Shared Observation**: IA Object・Content Category は DS の component/token と 1 対 1 対応しない。専用語彙が存在する IA Object は一部のみ (C-02〜C-05)、他は C-10 に集約。Content Category を Component/掲載枠と同一視しない。
- **Source-specific Variation**: 該当なし (横断原則)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: Content 文言は brand-content.md 参照切れ (X-07)。
- **Conflict or Gap**: Content Category・IA Object と DS 分類の非対応 (対応する定義を確認できない部分)。
- **Unresolved Dependency**: IA Object の内容・関係・業務仕様 (IA §11 Open Issue, §19)。
- **Downstream Impact**: Implementation の情報表現 (Repository 管理対象外)。
- **Open Issue**: IA Object・Content Category と DS 表現の対応整理。
- **Does Not Decide**: IA Object/Content Category と Component の同一視は本集約で決めない。

### X-07 文言表現の正本不在

- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: 平易な言葉・一貫した用語・文言表現 (Content 表現の正本)。
- **Source Assessment / Source Section**: WO2 §8.4 (CTP-002/005)・§11、WO3 §13 (SCR-002 Content)・§17 (SCR-013 Editorial/Policy)・§18 (SCR-014 Content)。
- **Related Service Design ID**: CTP-002・CTP-005・CTP-003・CTP-010。
- **Related SCR**: SCR-002・SCR-013・SCR-014。
- **Original Observation Classification**: 参照切れ。
- **Direct Evidence Referenced by Source**: 文言・コピーの正本 `brand-content.md` が design.md から参照されるが Repository 内に不在。命名規則正本 `governance/naming-rules.md` も不在。
- **Shared Observation**: 文言表現の直接証拠 (brand-content.md) は複数 SCR で「参照切れ」として一致し、Content 発見・理解・支援・編集の文言責務の DS 対応を確定できない。存在しない文書の内容は推測しない。
- **Source-specific Variation**: 該当なし (共通の参照切れ)。
- **Provenance**: 該当なし (存在自体が不在)。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: `brand-content.md` 不在・`governance/naming-rules.md` 不在。
- **Conflict or Gap**: 文言正本の不在により Content 表現の DS 対応を確定できない (参照切れ)。
- **Unresolved Dependency**: `brand-content.md`・`governance/naming-rules.md`・ADR 正本の不足の解決主体 (§19)。
- **Downstream Impact**: Implementation の文言適用 (Repository 管理対象外)。
- **Open Issue**: 文言正本・命名規則正本の不足。
- **Does Not Decide**: 参照切れ文書の内容・作成は本集約で決めない。

## 16. Source-specific Variations

以下は共通 Observation へ昇格させず、スコープ固有として保持する差異である。共通化した集約 Topic 内でも元の SCR・Service Design ID・節・分類を失わない。

- **T-02 状態色**: SCR-003 は Input の disabled/success が未取得 (follow-up #2)・error は暫定 placeholder。SCR-004 は状態表現に motion placeholder を伴う。両者を単一の状態対応へ統一しない。
- **T-04 / X-02 Accent・Fact/Promotion 分離**: 参照する TVL Decision ID が SCR-001/SCR-005 は TVL-0012 単独、SCR-002/SCR-014 は TVL-0011/0012。いずれも provenance 未確認であり、片方へ正規化しない。
- **C-01 Button**: SCR-005 の CTA-004 (情報確認と Room/Stay Plan 選択の区別) は SCR-005 固有。SCR-004 の比較・選択の優先関係も SCR-004 固有。他 SCR の CTA-002 (主 CTA 1 つ) と役割が異なるため統合しない。
- **C-02 SearchForm/Input**: SCR-001 は入口の探索起点としての SearchForm、SCR-003 は検索実行の入力項目・バリデーション・条件保持 (Input 状態実査待ち)。スコープが異なる。
- **C-03 Card**: SCR-004 は検索結果カード (実 px・8 スロット実査待ち)、SCR-005 は詳細用途 (検索結果向け Card の流用は実査待ち)、SCR-002/SCR-014 は Supporting としての一部表現。用途差を保持する。
- **C-06 Navigation component**: 各 SCR が宣言する Navigation Types が異なる (SCR-001: NAV-001/004/006、SCR-002: NAV-001/002/003、SCR-003: NAV-004/005 (History and Recovery)、SCR-004: NAV-002/003/004/005、SCR-005: NAV-002/003/004/006、SCR-013: NAV-001/002/003/006、SCR-014: NAV-001/002/003)。共通一覧へ正規化しない。
- **C-08 Recovery Action / C-09 支援 component**: SCR-013 固有 (支援・回復領域)。他 SCR へ拡張しない。
- **C-10 専用表現語彙の不在**: SCR-005 は Room/Stay Plan/Policy の業務モデルが Open Issue、SCR-003 は User (認証・会員・履歴保存) を上流制約で取り込まない。IA Object ごとに事情が異なる。
- **X-03 状態モデル**: SCR ごとに宣言される Navigation States が異なる。SCR-004 は `Error / Interrupted` を含み、SCR-014 は含まない。SCR-014 に `Error / Interrupted` を追加せず、各 SCR の State 宣言を正規化しない。`Error / Interrupted` は 1 つの複合状態名として扱う。
- **X-04 Accessibility**: SCR-014 の画像欠落 fallback (❓ 実査待ち) は SCR-014 固有 (Editorial Content の画像依存)。

## 17. Provenance, Placeholder, Inspection-pending, and Broken Reference Effects

Baseline (Work Order 1) 由来の証拠制約を、関係する集約 Observation へ関連づける。これらは再決定せず、影響範囲の整理にとどめる。

### 17.1 Provenance 未確認

- **GOV-0002 (Button variant 語彙)**: C-01・C-02・X-01 に影響。Button/variant を用いた CTA 対応の「対応を直接確認できる」観察を、上流適合の確定へ昇格させない。
- **TVL-0001〜TVL-0012 (TVL-0009 は 4 資産に未出現)**: T-04・X-02 (accent 点専用 TVL-0011/0012)・C-07 (drawer 統一 TVL-0007)・X-05 (placeholder 維持 TVL-0008) に影響。ADR 正本なし。
- **Source of Truth GitHub URL・実装 Repository `tocoo/tocoo_travel`**: 記載のみで内容未検証。Downstream Impact (§21) の Implementation は Repository 管理対象外。

### 17.2 Placeholder / 実査待ち

- **placeholder token 計 10** (semantic `radius.card`・`motion.transition.duration`・`motion.transition.easing`、primitive `shadow.sm/md/lg`・`motion.duration.fast/base/slow`・`motion.easing.standard`): T-06・C-03 (radius.card/shadow)・X-03 (motion) に影響。
- **ボタン状態 (follow-up #4)**: T-02・C-01・C-08・X-03 に影響 (状態表現・Recovery)。
- **Input 状態一式 (follow-up #2)**: C-02・C-07 に影響。
- **Card 実 px・8 スロット対応付け・ReviewStars 星実寸・PriceTag「円」weight (❓)**: C-03・C-04・C-05・T-05 に影響。
- **画像欠落 fallback (❓)**: X-04 (SCR-014) に影響。

### 17.3 参照切れ

- **`brand-content.md` 不在**: X-07・X-02 (販促と対の文言)・C-09/C-10 (Content/支援文言)・SCR-001/002/013/014 の Content 責務に影響。
- **`governance/naming-rules.md` 不在**: X-07・T-02 (用途ベース命名の正本)・NVP-005 に影響。

### 17.4 扱いの原則

- provenance 未確認を適合確認済みへ昇格させない。placeholder / 実査待ちを「対応済み」へ統合しない。参照切れ文書の内容を推測しない。
- 上記の影響関連づけは、gap の原因責任・解決策・優先順位を決めない (Work Order 5)。

## 18. Conflict and Over-coverage Observations

- **矛盾 (矛盾)**: 入力評価文書 (Work Order 2・Work Order 3) の範囲では、上流 Service Design / Screen Requirements の定義と DS 記述の直接的矛盾は確認されていない。Work Order 2 §10 は「SD 側が具体値を定義していないため DS の具体値と上流原則が矛盾するかは直接証拠から確認できない」と記録する。本集約はこの対象 snapshot・入力評価の範囲に限定して「直接的矛盾は確認されていない」と記載し、再評価により新しい矛盾を創作しない。
- **過剰 (過剰)**: 入力評価文書に「過剰」と明示された Observation は確認されない。上流に対応要求が確認できない DS 記述・Component・token を本集約で新たに「過剰」と判定しない。
- **集約上の不一致 (Conflict or Gap)**: 集約の過程で、入力評価文書間・元評価内で相互に矛盾する記述は確認されなかった。Work Order 2 の横断責務観察と Work Order 3 の各 SCR 観察は、同一設計責務について整合的 (同方向) であり、片方が「対応を直接確認できる」他方が「矛盾」といった食い違いは見られない。将来そのような不一致を確認した場合は、本節に不一致として記録し、元文書は修正しない。

## 19. Unresolved Dependencies

以下は集約 Observation に関係する未解決の依存関係である。Work Order 5 の判断 (改訂候補と未解決事項の分離) に踏み込まず、依存関係として記録する。「DS 側に定義がない」と「上流 Open Issue により確定できない」が同じ Observation に関係する場合、両方の事実を保持する。

- **状態モデルの対応整理** (X-03・T-02・C-08): Navigation State Model・CTA State Model (Pending Confirmation)・Status and Uncertainty Model と DS 状態表現の対応。DS 側は success/error 中心で対応する定義を確認できない部分があり、かつ状態の業務定義は上流 Open Issue。両方の事実を保持する。
- **Navigation 分類の対応整理** (C-06・X-01): NAV-001〜006 と DS component の対応記述が DS 側にない。Global Navigation 対象領域・History and Recovery 保持方式は上流 NAV/SCR Open Issue。
- **IA Object の業務モデル** (C-10・X-06): Destination/Room/Stay Plan/Availability/Policy/Booking/User/Content の専用表現語彙が DS 側になく、かつ内容・関係・業務仕様は IA §11 Open Issue。SCR-005/SCR-006 境界も未定義。
- **入力・検索仕様** (C-02): 入力項目・必須条件・バリデーション・条件保持方式が上流 Open Issue のため、SearchForm/Input の具体対応を確定できない。
- **表示仕様** (C-03・C-04・C-05): 表示項目・表示順・比較成立基準・料金構造・Review 提供元が上流 Open Issue。
- **可逆/不可逆・回復** (C-07・C-08): 可逆/不可逆の区別規則・Recovery Action の component/規則が DS 側になく、問い合わせ手段・処理フローは上流 Open Issue。
- **文言・命名の正本** (X-07・T-02): `brand-content.md`・`governance/naming-rules.md`・ADR 正本の不在。
- **provenance** (§17.1): GOV-0002・TVL Decision ID・外部 URL の provenance と有効性。
- **placeholder / 実査待ちの解決** (§17.2・T-06・X-05): 計 10 の placeholder token・ボタン状態 (#4)・Input 状態 (#2)・Card 実 px・星実寸・「円」weight・画像 fallback。
- **承認・反映主体**: 本集約結果の承認・反映主体、および Work Order 5 への引き継ぎ方法。

## 20. Work Order 4 Completion Boundary

- Work Order 2 の主要 Observation (SD-001〜SD-005・SD-007 の横断責務) と Work Order 3 の 7 個別 Screen Requirement (SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014) の主要 Observation を、Source Traceability Index (§12) で追跡できる形に集約した。共通 Observation (§13〜§15) とスコープ固有 Observation (§16) を区別し、元の Observation 分類・provenance・placeholder・実査待ち・参照切れ (§11・§17) を保持した。よって Work Order 4 を Draft として実施済みとする。
- 本文書は次を実施していない: Work Order 5 (改訂候補と未解決事項の分離)・gap の原因責任の決定・優先順位/重要度/severity/対応順の決定・新規 Component/token/pattern/文書の提案・解決策の提案。Work Order 6 (改訂着手可否の判断)・承認主体の推測も行っていない。
- 「Work Order 4 実施済み」は、Alignment 全体の完了・Design System 適合・改定可能・承認済みを意味しない。

## 21. Downstream Impact

- **Assets** ([../assets/README.md](../assets/README.md)) — `Not started`。本集約の対象外。
- **Implementation** — Repository 管理対象外。本集約は静的集約であり実装検証ではない。DS から実装画面・URL・route を導出しない。各 Screen Requirement の Downstream Impact に列挙された Component 例を採用決定と解釈しない。

## 22. Open Issues

以下は未決である。解決策は推測して記載しない。

- 本集約結果の承認・反映主体、および Work Order 5 (改訂候補と未解決事項の分離) への引き継ぎ方法。
- §19 に整理した未解決の依存関係 (状態モデル・Navigation 分類・IA 業務モデル・入力/表示仕様・可逆/回復・文言/命名正本・provenance・placeholder/実査待ち) の解決主体。
- 対象 snapshot・入力評価の範囲を超えた矛盾・過剰の有無 (本集約では新規に判定しない)。
- 正式な集約 ID・評価体系名・分類体系・ファイル名の確定 (本ファイル名 `alignment-observations-aggregation.md` は暫定)。

## 23. Does Not Decide

- 改訂候補と未解決事項の分類・分離 (Work Order 5)・gap の原因責任。
- Design System の改定要否・token 値/名/階層/命名規則・placeholder の解消方法。
- gap の優先順位・重要度・severity・対応順。
- Component の追加/削除/統合/分割・Component API/variant/state/実装仕様。
- Service Design または Screen Requirement の修正・SCR-006〜SCR-012 の要求。
- UI 構造・表示項目・表示順・情報密度・API/DB/URL/route・実装 Repository との適合。
- 参照切れ文書の内容・provenance 未確認事項の正当性・正式な評価 ID/ファイル名/評価体系・UX Decision の追加。
- 改訂着手可否 (Work Order 6)・承認主体。
- 「対応を直接確認できる」を要件充足・承認完了へ、「対応する定義を確認できない」を新規 Component 追加 Decision へ、「過剰」を削除 Decision へ、placeholder / 実査待ちを「対応済み」へ、provenance 未確認を適合確認済みへ変換しない。

## 24. Relationship to Subsequent Work

- 本集約 (Work Order 4) は、Alignment Plan §10 の次段である Work Order 5「改訂候補と未解決事項の分離」の入力となる。
- Work Order 5 は本 PR のマージ前には開始しない。
- 改訂着手可否の判断 (Work Order 6) は、Work Order 5 の後に成立する。
- 本集約は Design System の修正・新しい Decision・UX Decision を含まない。改定は後続タスクの承認を前提とする。

## 25. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-17 | Initial aggregation (Work Order 4): Work Order 2 (Service Design 横断整合性評価) と Work Order 3 (作成済み 7 個別 Screen Requirement ごとの整合性評価) の Observation を、Work Order 1 の証拠制約を保持しながら設計責務単位で横断集約。共通 Observation・スコープ固有 Observation・provenance/placeholder/実査待ち/参照切れの影響・未解決依存を分離し、Source Traceability Index で元 Observation を追跡可能にした。改訂候補整理・改定着手可否判断・DS 修正・UX Decision 追加は未実施 | Draft |
