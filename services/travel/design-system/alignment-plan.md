# Travel Design System Alignment Assessment Plan

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の作成済み上流 Screen Requirements と既存 Design System 資産の Alignment を評価するための計画。評価方法・対象・証拠規則・記録構造・観察区分・推奨実行順を定義する。具体的な対応評価・gap 判定・token / Component 改訂は本文書では実施しない。
- Position in Repository: `services/travel/design-system/alignment-plan.md` — Design System レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)。上流・前提は Governance の実在成果物 ([../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md))、Service Design (SD-001〜SD-007, [../service-design/README.md](../service-design/README.md))、Screen Requirements (入口 [../screen-requirements/README.md](../screen-requirements/README.md)・作成順序評価 [../screen-requirements/creation-plan.md](../screen-requirements/creation-plan.md)・作成済みの個別 Screen Requirement)、Design System 入口 [README.md](README.md)。同一 Design System レイヤーの評価対象は `design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md` (§15)。下流成果物 (Assets / Implementation) との関係は §16 を参照。

本文書は評価・計画文書であり、Alignment 評価結果・Design Decision・token / Component 仕様の正本ではない。評価上の観察区分と、Repository 成果物の正式 Status を混同しない。ファイル名 `alignment-plan.md` は記述的な暫定名であり、正式な評価体系名・恒久的な文書命名規則・Alignment ID 体系を確定しない (§17 Open Issues)。

## 1. Purpose

- 作成済みの 7 個別 Screen Requirement (SCR-001〜SCR-005・SCR-013・SCR-014, すべて Draft) と、既存 Design System 4 資産 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`, すべて Draft 0.3.0-draft) の Alignment を評価するための、評価方法・評価単位・証拠規則・記録構造・観察区分・評価観点・推奨実行順を定義する。
- 評価から確認できる対応・不足・過剰・矛盾・placeholder・provenance 未確認等を、推測を伴わずに記録できる状態を作る。
- 「評価方法を定義する」ことと「実際の対応評価・gap 判定・改訂を行う」ことを区別する。後者は本文書では実施しない ([README.md](README.md) §10 Alignment Assessment Boundary と一致)。

本文書は、Design System 入口 [README.md](README.md) §10 が後続タスクとした Alignment Assessment に対し、実行前の評価計画と推奨実行順を与える。実際の評価は上流成果物と既存資産を read-only で確認する後続タスクで行う。

## 2. Scope

### Assessed

- 作成済み 7 個別 Screen Requirement (SCR-001〜SCR-005・SCR-013・SCR-014) と既存 Design System 4 資産の対応を評価するための方法・単位・証拠・記録・観点・順序の定義。
- 各 Screen Requirement が直接参照する Service Design の実在 ID・正式名称まで遡って確認する計画。
- 既存 Design System 4 資産の内部整合性・provenance・placeholder / 実査待ち状況を確認する計画。
- 評価の推奨実行順と最初に実行すべき評価対象。
- 評価開始条件と、評価記録上の観察区分。

### Not Assessed / Not Decided

- Alignment Assessment の実施・対応表への実データ記入・gap 一覧の作成。
- SCR-006〜SCR-012、および未定義の予約・決済・認証・会員・変更・取消要件。
- token / Component の追加・変更・削除、JSON・`design.md`・`components.md` の変更、version bump。
- ADR・命名規則・`brand-content.md` の作成、provenance 不足の解決、Decision ID の再認定。
- 実装 Repository の実査、Assets の評価。
- UI・画面構成・URL・route の定義。
- 数値スコア・適合率・カバレッジ率・合否点の導入。
- 新しい正式 Phase・Decision・評価 ID・恒久的なファイル命名規則の確定。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。各文書は ID 体系を持つ: SDP-001〜010 ([../service-design/principles.md](../service-design/principles.md)) / IA-OBJ-001〜012 ([../service-design/information-architecture.md](../service-design/information-architecture.md)) / NVP-001〜008・NAV-001〜006 ([../service-design/navigation.md](../service-design/navigation.md)) / CTP-001〜010・Content Categories ([../service-design/content-principles.md](../service-design/content-principles.md)) / CTA-001〜010・CTA-TYPE-001〜005・Commitment Level Model・CTA State Model ([../service-design/cta-principles.md](../service-design/cta-principles.md)) / SCR-001〜SCR-014 画面候補 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md)) / UXDR-TRAVEL-001〜003 (Accepted, [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md))。
- 作成済みの個別 Screen Requirement SCR-001〜SCR-005・SCR-013・SCR-014 が Draft として存在する。SCR-006〜SCR-012 は未作成 (`Not started`) である ([../screen-requirements/README.md](../screen-requirements/README.md))。
- 既存 Design System 4 資産 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) が Draft・version `0.3.0-draft` として存在する ([README.md](README.md) §6)。JSON には `$status: placeholder` のトークン (`radius.card` / `motion.*` / `shadow.*` に follow-up 番号・TVL-0008 の `$note`) が含まれる。
- 既存 Design System と上流 (SD-001〜SD-007・作成済みの個別 Screen Requirement) の Alignment は、Work Order (§10) の 1〜4 (Baseline 確認・Service Design 横断整合性評価・作成済み 7 個別 Screen Requirement ごとの整合性評価・Work Order 2・3 の Observation の横断集約) が Draft として実施済みである。横断集約された Observation を入力とする改訂候補と未解決事項の分離 (Work Order 5)・改訂着手可否の判断 (Work Order 6)、および Design System の改定は未着手であり、改訂候補一覧・優先順位・改定要否はまだ存在しない (これは状態整合性の Fact 記述であり、新しい Decision を追加しない)。
- 既存 Design System 文書は、Repository 内に正本が確認できない参照 (`brand-content.md`・`governance/naming-rules.md`・GOV / TVL 等の Decision ID・GitHub URL・follow-up 番号) を含む ([README.md](README.md) §8)。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- 実行状況: Work Order (§10) の 1 (Baseline 確認, [baseline-assessment.md](baseline-assessment.md))・2 (Service Design 横断整合性評価, [service-design-alignment-assessment.md](service-design-alignment-assessment.md))・3 (作成済み 7 個別 Screen Requirement ごとの整合性評価, [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md))・4 (Work Order 2・3 の Observation の横断集約, [alignment-observations-aggregation.md](alignment-observations-aggregation.md)) が Draft として実施済みである。Work Order 4 は Observation の集約のみであり、改訂候補と未解決事項の分離は行っていない。Work Order 5〜6 は未着手。本計画の評価方法・評価単位・証拠規則・記録構造・観察区分・推奨順・推薦理由は変更していない。

### Decisions

- 本文書は評価方法・記録構造・推奨順を定義する。対応評価・gap 判定・改訂は実施しない。
- 評価は上流成果物と既存 Design System 資産の実在する記述のみを証拠とする (§6 Evidence Rules)。
- 評価対象の上流は作成済み 7 個別 Screen Requirement に限定する。SCR-006〜SCR-012 を先取りしない。
- 未確認・不足・矛盾・未検証・由来不明の事項を推測で補完せず Open Issue または観察として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 と一致)。
- 既存 Design System 資産を read-only で評価し、本文書および後続評価で変更しない。
- 既存 Design System 資産を上流要求として扱わず、Component が存在することを利用要求へ昇格させない (UXDR-TRAVEL-002)。

### Hypotheses

- なし。

### Open Issues

- Alignment 評価の評価単位・記録構造・観察区分の妥当性、評価・承認主体、Alignment 完了条件。
- provenance 未確認 (不足ファイル・Decision ID・外部参照) の解決主体と方法。
- （詳細は §17 に集約）

## 4. Assessment Inputs

評価は以下の実在成果物を入力とする。最新 main から取得し、対象ファイルと commit を記録する (§12 Entry Conditions)。

### 上流・前提

- Governance: [../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md)。
- Service Design SD-001〜SD-007: [principles.md](../service-design/principles.md) / [information-architecture.md](../service-design/information-architecture.md) / [navigation.md](../service-design/navigation.md) / [content-principles.md](../service-design/content-principles.md) / [cta-principles.md](../service-design/cta-principles.md) / [screen-matrix.md](../service-design/screen-matrix.md) / [ux-decision-records.md](../service-design/ux-decision-records.md)。
- Screen Requirements: 入口 [README.md](../screen-requirements/README.md) / [creation-plan.md](../screen-requirements/creation-plan.md)。
- Design System 入口: [README.md](README.md)。

### 評価対象の作成済み個別 Screen Requirement (すべて Draft)

| SCR 候補 | 個別 Screen Requirement | Primary IA Objects | Supporting IA Objects |
| --- | --- | --- | --- |
| SCR-001 Service Entry | [service-entry.md](../screen-requirements/service-entry.md) | IA-OBJ-001 / IA-OBJ-002 / IA-OBJ-012 | なし |
| SCR-002 Destination Discovery | [destination-discovery.md](../screen-requirements/destination-discovery.md) | IA-OBJ-001 / IA-OBJ-012 | IA-OBJ-003 |
| SCR-003 Accommodation Search | [accommodation-search.md](../screen-requirements/accommodation-search.md) | IA-OBJ-002 / IA-OBJ-001 | IA-OBJ-011 |
| SCR-004 Search Results | [search-results.md](../screen-requirements/search-results.md) | IA-OBJ-002 / IA-OBJ-003 | IA-OBJ-006 / IA-OBJ-007 / IA-OBJ-009 / IA-OBJ-008 |
| SCR-005 Accommodation Detail | [accommodation-detail.md](../screen-requirements/accommodation-detail.md) | IA-OBJ-003 | IA-OBJ-001 / IA-OBJ-004 / IA-OBJ-005 / IA-OBJ-009 / IA-OBJ-008 / IA-OBJ-012 |
| SCR-013 Help and Support | [help-and-support.md](../screen-requirements/help-and-support.md) | IA-OBJ-012 / IA-OBJ-008 | IA-OBJ-011 / IA-OBJ-010 |
| SCR-014 Editorial Content | [editorial-content.md](../screen-requirements/editorial-content.md) | IA-OBJ-012 | IA-OBJ-001 / IA-OBJ-003 |

上表の Primary / Supporting は各 Screen Requirement §5 の記述を引用する (再定義しない)。Supporting IA Object を根拠に業務モデル・表示項目・機能を追加しない。

### 同一レイヤーの評価対象 (既存 Design System 資産, すべて Draft 0.3.0-draft)

- [design.md](design.md) — 統合文書。
- [semantic.travel.json](semantic.travel.json) — Semantic token (color / font / radius / motion / icon / elevation 等)。
- [primitive.travel.json](primitive.travel.json) — Primitive token (color.palette / typography / spacing / size / radius / shadow / border / elevation / motion / iconSize / breakpoint)。
- [components.md](components.md) — Component 仕様 (Button / Input / SearchForm / Card / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal。未着手: Select / Tabs / Toast / Table / Accordion)。

## 5. Assessment Unit

評価単位は、Screen Requirement 文書全体または Component 名単位だけにしない。「上流で確認できる設計責務」を単位とする。各 Screen Requirement の以下の節に現れる責務を追跡できる単位とする ([README.md](../screen-requirements/README.md) §6 Common Document Structure、および作成済み 7 文書の共通 18 節構造)。

- User Tasks (§4)
- Information Responsibilities (§5)
- Functional Requirements (§6)
- Content Requirements (§7)
- Navigation Requirements (§8)
- CTA Requirements (§9)
- State and Feedback Requirements (§10)
- Accessibility Requirements (§11)
- Constraints (§12)
- Does Not Decide (§13)
- Downstream Impact (§15)
- Open Issues (§16)

各 Screen Requirement の全文章を機械的に 1 行ずつ分解することは求めない。評価単位の運用規則は以下とする。

- UI へ変換できない抽象原則を、無理に単一 token や Component へ割り当てない。
- 1 つの要件責務が複数の token / Component / pattern へ関係し得る。
- 1 つの Design System 資産が複数の要件責務へ関係し得る。
- 1 対 1 対応を前提としない。
- Open Issue を Design System 要件へ変換しない。
- Does Not Decide に含まれる事項を評価対象の確定要件として扱わない (観察・Open Issue として記録し得るが確定要件としない)。

## 6. Evidence Rules

Alignment Assessment で使用できる証拠を以下に限定する。

### 上流要求の証拠

- Service Design の実在する ID (SDP / IA-OBJ / NVP / NAV / CTP / CTA / CTA-TYPE / UXDR-TRAVEL)・正式名称・本文。
- Screen Matrix の実在する SCR 候補・責務・Primary / Supporting IA Objects・Navigation Types・Content Categories・Navigation States。
- 個別 Screen Requirement の実在する節・記述。
- Governance の実在成果物 ([../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md))。

### Design System 側の証拠

- `design.md` の実在する節・記述。
- JSON の実在する token path・value 参照 (`$value`)・`$status`・`$note`・`$meta`。
- `components.md` の実在する Component・variant・状態・Do / Don't・未確定事項。
- Design System 入口 [README.md](README.md) で確認された現在状態。

### 証拠として扱わないもの

- ファイル名・Component 名からの推測。
- 一般的な旅行予約サイトの慣例。
- 実装を確認していない状態での実装仕様の推測。
- Repository 内に存在しない文書 (`brand-content.md`・`governance/naming-rules.md` 等) の内容。
- 正本が存在しない ADR の想定内容。
- GOV / TVL 等の Decision ID が存在することだけを根拠とした Decision の再認定。
- Screen Requirement の Downstream Impact に記載された例 (例: `search-results.md` の Card / PriceTag / ReviewStars 等) を、そのまま採用決定とすること。
- Design System に Component が存在することを、その Component の利用要求とすること。

出典が確認できない記述は、正しいものとして補完せず `provenance 未確認` として記録する (§8)。

## 7. Traceability Record Structure

後続評価で使用する記録構造を定義する。最低限、以下の項目を追跡できる列・フィールドを持つ。

| 項目 | 内容 |
| --- | --- |
| 対象 Screen Requirement | 例: SCR-004 Search Results (`search-results.md`) |
| 上流ファイル | 参照した実在ファイル |
| 上流節 | 参照した §番号・見出し |
| 関連 Service Design ID・正式名称 | 例: CTA-002 One Clear Primary Action |
| 評価対象となる設計責務 | §5 の単位で記述 |
| 既存 Design System 成果物 | design.md / JSON / components.md のいずれか |
| DS 内の節 / token path / Component 名 | 例: `color.action.primary.bg` / Button.primary |
| 確認できた直接証拠 | 実ファイルの記述 (引用元を特定できる形) |
| 観察結果 | §8 の観察区分 |
| provenance 状況 | 確認済み / 未確認 |
| placeholder / 実査待ちの有無 | `$status: placeholder`・🚧 実査待ち等 |
| 矛盾または不足 | 有無と内容 |
| 影響する下流 | Assets / Implementation 等 (§16) |
| Open Issue | 未決事項 |
| Does Not Decide | 該当する上流の非決定事項 |
| 備考 | 補足 |

記録行に新しい恒久 ID を採番しない。行を識別する必要がある場合も、文書内の行番号や暫定識別子を正式な Alignment ID として採用しない。

## 8. Observation Classification

後続評価で使用する観察上の分類を定義する。Design System 入口 [README.md](README.md) §10 の観点を基礎とする。

- **対応を直接確認できる** — 上流責務に対応する DS 側の記述を実ファイルで確認できる。
- **一部のみ確認できる** — 一部は確認できるが、重要部分が未確認・placeholder・Open Issue になる。
- **対応する定義を確認できない** — 対応する DS 側の記述を確認できない。
- **過剰** — 上流に対応する要求が確認できない DS 側の記述・Component・token。
- **矛盾** — 上流と DS 側、または DS 内部で記述が食い違う。
- **placeholder** — `$status: placeholder` 等の未確定トークン。
- **実査待ち** — 🚧 実査待ち・follow-up 番号等で実測未取得。
- **provenance 未確認** — 出典・正本が Repository 内で確認できない。
- **参照切れ** — 参照先ファイル・ID が Repository 内に存在しない。
- **評価対象外** — SCR-006〜SCR-012 依存・未定義業務仕様・Assets・実装等。

これらの扱いを以下のとおり明記する。

- これらは評価記録上の観察区分であり、Repository 成果物の正式 Status ではない。
- token / Component の採用・廃止 Decision ではない。
- 「対応を確認できる」は、要件充足・品質保証・承認完了を意味しない。
- 「対応する定義を確認できない」は、直ちに新規 Component を追加すべきという結論を意味しない。
- 「過剰」は、直ちに削除すべきという意味ではない。
- provenance 未確認の記述を、対応確認済みへ昇格させない。

数値スコア・適合率・カバレッジ率・合否点は導入しない (Repository 内に根拠となる尺度が存在しない)。

## 9. Assessment Dimensions

評価は少なくとも以下の観点で行えるものとする。既存 Component 名をそのまま必要 Component 一覧へ変換しない。上流に具体値要求がない場合、token 値の良否を上流適合として評価しない。

### Foundation / token

- 色 (color.*)・Typography (font / typography)・spacing・radius・elevation / shadow・motion・icon・focus・状態表現。
- 上流 (SD-004 Content Principles・SD-005 CTA Principles・各 Screen Requirement の Accessibility / State) が具体値を要求していない場合、token 値そのものの良否を Alignment として判定しない (観察・Open Issue として記録し得る)。

### Component / pattern

- CTA / 操作・入力・Navigation・Content 表示・状態 / feedback・Recovery・Accommodation 情報・Review・Policy・Support・Editorial Content。
- 既存 Component (Button / Input / SearchForm / Card / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal 等) の存在を、必要 Component 一覧・利用要求へ自動変換しない。

### Cross-cutting

- Navigation と CTA の責務分離 (UXDR-TRAVEL-003)。
- 状態と不確実性 (SD-004 CTP-006・各 Screen Requirement の State and Feedback)。
- 条件・制約の提示 (CTA-005 Conditions Before Action・CTP-003)。
- Fact / Decision / Promotion の分離 (CTP-010)。
- Accessibility (SDP-007 / NVP-008 / CTP-008 / CTA-009)。
- responsive への非依存・未定義保持 (breakpoint 等を確定要求として扱わない)。
- 未確定事項の表現 (placeholder / 実査待ちの伝播)。
- 上流 Does Not Decide の保持 (UXDR-TRAVEL-001)。

## 10. Recommended Work Order

後続評価の推奨実行順を以下とする。正式な Phase や新しい分類体系として登録しない。本計画では 1〜6 を実行せず、順序と理由のみを定義する。

1. **既存 Design System 4 資産の内部整合性・provenance・placeholder 状況の確認** — 上流対応を断定する前に、評価の土台となる DS 側の記述の信頼性を確認する (§11 First Assessment Recommendation)。
2. **Service Design の横断原則と既存 Design System の対応確認** — SDP / IA-OBJ / NVP・NAV / CTP / CTA・CTA-TYPE / UXDR-TRAVEL の横断原則と DS 側の対応を確認する。個別 Screen Requirement より先に横断原則を見ることで、後続の個別評価の観点を揃える。
3. **作成済み 7 個別 Screen Requirement ごとの対応確認** — 各 Screen Requirement の設計責務 (§5) と DS 側の対応を、§7 の記録構造・§8 の観察区分で確認する。
4. **観察結果の横断集約** — 個別評価で得た観察を横断的に集約し、重複・共通の不足・矛盾を整理する。
5. **改訂候補と未解決事項の分離** — 改訂を検討し得る候補と、上流・業務仕様・provenance の未解決に依存し確定できない事項を分離する。
6. **実際の改訂タスクを開始できるかの判断** — 改訂の着手可否を、Open Issue の解決状況と承認主体の有無から判断する。

順序の理由: DS 側の信頼性 (1) を確認せずに上流対応 (2・3) を断定すると、未検証・placeholder・provenance 未確認の DS 記述を「正しい実現手段」として扱う危険がある。横断原則 (2) を個別評価 (3) より先に置くのは、個別評価の観点を統一するため。集約 (4)・分離 (5)・判断 (6) は観察が揃った後に成立する。

実行状況: 1 (既存 4 資産の Baseline 確認) は [baseline-assessment.md](baseline-assessment.md) (Draft)、2 (Service Design 横断原則と既存 Design System の対応確認) は [service-design-alignment-assessment.md](service-design-alignment-assessment.md) (Draft)、3 (作成済み 7 個別 Screen Requirement ごとの対応確認) は [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) (Draft)、4 (観察結果の横断集約) は [alignment-observations-aggregation.md](alignment-observations-aggregation.md) (Draft) として実施済み。3 は 7 件の個別評価であり、4 の横断集約は含まない。4 は 2・3 の Observation を設計責務単位で横断集約し元 Observation への追跡可能性を保持したものであり、5 の改訂候補と未解決事項の分離は含まない。5〜6 は未着手。この実行状況は上記の順序・理由・分類を変更しない。Work Order 1〜4 の実施をもって Alignment 全体を完了扱いしない。

## 11. First Assessment Recommendation

最初に実行すべき評価対象を 1 件推薦する。

- **推薦対象**: 既存 Design System 4 資産 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) の内部整合性・provenance・placeholder / 実査待ち状況の Baseline 確認 (§10 Work Order の 1)。
- **推薦理由** (単一の理由に還元しない):
  1. `brand-content.md` が不在である ([README.md](README.md) §8)。`design.md` が「正」として参照するが Repository 内に存在しない。
  2. `governance/naming-rules.md` が不在である。`design.md`・`components.md` が命名規則の参照先とするが存在しない (Governance README も未作成と明記)。
  3. ADR 正本が不在である。GOV / TVL の Decision ID を Accepted Decision として裏付ける ADR 正本が Repository 内に確認できない。
  4. GOV / TVL Decision ID の裏付けが未確認である ([../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) は「オーナー確認事項」一覧であり ADR 正本ではない)。
  5. JSON 内に placeholder / follow-up note が存在する (`radius.card` / `motion.*` / `shadow.*` 等)。
  6. `design.md`・JSON・`components.md` 間の整合性が未確認である。
  7. この状態で Screen Requirement との対応を断定すると、未検証の DS 記述を正しい実現手段として扱う危険がある。
- **位置づけ**: 「最初に行うこと」であり、正式な Phase・成果物名・ファイル名・評価 ID を確定するものではない。推薦対象の正式名称は本文書で確定しない。
- **実行状況**: 本推薦は実行され、Baseline 確認結果が [baseline-assessment.md](baseline-assessment.md) (Draft) として存在する。これは推薦の実行状況の注記であり、上記の推薦理由を事後的に変更するものではない。

## 12. Entry Conditions for Assessment

後続評価を開始できる条件を、確定ではなく前提整理として示す。

- 評価対象が最新 main から取得されていること。
- 対象ファイルと commit が記録されていること。
- 上流・前提と、同一レイヤーの評価対象 (既存 DS 4 資産) が区別されていること (§4)。
- 評価対象が作成済み 7 個別 Screen Requirement に限定されていること。SCR-006〜SCR-012 を先取りしないこと。
- 評価記録構造 (§7) と観察区分 (§8) が使用できること。
- provenance 未確認を未確認のまま記録できること。
- gap の解決策を同じタスクで決定しないこと。
- 既存資産を変更せず read-only で評価できること。
- 不明事項を Open Issue として保持できること。

評価・承認主体が未定義であることを理由に、事実確認 (read-only の観察記録) まで停止しない。ただし未定義の承認主体を推測しない。

実行状況: Work Order 1 の Baseline 確認 ([baseline-assessment.md](baseline-assessment.md), Draft) は、上記の開始条件を満たした上で実施した (評価対象 commit `0d446152` と 4 ファイルの blob SHA を記録・上流と同一レイヤーを区別・作成済み 7 個別 Screen Requirement 以外を評価せず・read-only・provenance 未確認を未確認のまま記録)。条件自体は変更していない。

## 13. Quality Criteria

本計画および後続評価には、以下を適用する。

- 単独で読んでも理解できる。
- 責務が明確で、上流・同一レイヤー・下流を混同しない。
- Fact / Decision / Hypothesis / Open Issue、および観察区分と正式 Status を区別する。
- 証拠を実在する Repository 成果物に限定し、推測で補完しない。
- 上流成果物の定義を再定義せず参照する。
- 既存 Design System の記述を上流要求へ昇格させない。
- provenance 未確認を対応確認済みへ昇格させない。
- 1 対 1 対応を前提とせず、Open Issue / Does Not Decide を確定要件へ変換しない。
- 数値スコア・合否点を導入しない。

## 14. Relationship with Upstream Artifacts

本文書の上流成果物は、Repository の参照順序上で先行する Governance の実在成果物・Service Design SD-001〜SD-007・Screen Requirements (入口 README・Creation Plan・作成済みの個別 Screen Requirement)・Design System 入口 README とする。上流の定義を本文書で変更・再定義しない。

- **Governance** — [../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md)。命名規則・ADR・レビュー規則の正本は未整備。
- **Service Design SD-001〜SD-007** — [principles.md](../service-design/principles.md) (SDP) / [information-architecture.md](../service-design/information-architecture.md) (IA-OBJ) / [navigation.md](../service-design/navigation.md) (NVP・NAV) / [content-principles.md](../service-design/content-principles.md) (CTP・Content Categories) / [cta-principles.md](../service-design/cta-principles.md) (CTA・CTA-TYPE) / [screen-matrix.md](../service-design/screen-matrix.md) (SCR 候補) / [ux-decision-records.md](../service-design/ux-decision-records.md) (UXDR-TRAVEL, Accepted)。
- **Screen Requirements** — 入口 [README.md](../screen-requirements/README.md) / [creation-plan.md](../screen-requirements/creation-plan.md) / 作成済みの個別 Screen Requirement (§4)。
- **Design System 入口** — [README.md](README.md) (§10 Alignment Assessment Boundary が本計画の位置づけを定義)。

## 15. Relationship with Existing Design System Assets

既存 Design System 4 資産は本評価の対象 (同一レイヤー) であり、上流成果物ではない。

- [design.md](design.md) / [semantic.travel.json](semantic.travel.json) / [primitive.travel.json](primitive.travel.json) / [components.md](components.md) — すべて Draft・version `0.3.0-draft`。
- これらを read-only で評価し、本文書および後続評価で変更しない (token / Component / JSON / `design.md` / `components.md` の追加・変更・削除・version bump を行わない)。
- 既存資産の記述を上流要求へ昇格させない。Component が存在することを利用要求へ変換しない。
- 既存資産を「正しい」「承認済み」「上流整合済み」「Complete」として扱わない (Draft であることと上流整合性未評価を区別する)。

## 16. Relationship with Downstream Artifacts

下流成果物を Position ヘッダーの「上流・前提」に含めない。

- **Assets** ([../assets/README.md](../assets/README.md)) — `services/travel/assets/` に位置し、現在 `Not started`。本評価の対象に含めない。接続方法は Open Issue。
- **Implementation** — Repository の管理対象外。本計画・後続評価で実装仕様を確定しない。既存文書に実装 Repository の記述があっても実装状態を確認済みとみなさない。Design System から実装画面・URL・route を導出しない。

## 17. Open Issues

以下は未決である。解決策は推測して記載しない。

- Baseline Assessment ([baseline-assessment.md](baseline-assessment.md)) の結果の承認・解決・反映は未決 (Baseline 実施は Alignment 全体の完了を意味しない)。
- Alignment 評価の評価単位・記録構造・観察区分の妥当性。
- 評価・承認主体。
- traceability の記録の保存場所・形式。
- gap の分類方法の詳細。
- Design System への反映確認方法。
- version bump の条件。
- 既存 Decision ID (GOV / TVL 等) の正本と有効性。
- Governance の命名規則正本 (`governance/naming-rules.md`) が存在しないこと。
- ADR 正本が存在しないこと。
- `brand-content.md` の参照と実在状況 (存在しない)。
- 既存 follow-up 番号 (#2 / #3 / #4 / #5 / #13 等) の追跡先。
- 既存 GitHub / 実装 Repository 参照の検証方法。
- placeholder / 実査待ちトークンの解決主体。
- SCR-006〜SCR-012 を評価対象へ加える条件。
- Assets への接続方法。
- Alignment 完了条件。
- 評価体系名・文書命名規則・Alignment ID 体系の正式確定 (本ファイル名 `alignment-plan.md` は暫定)。

## 18. Acceptance Criteria

本計画文書の受入基準。評価結果ではなく、計画としての完成条件を示す。

- 文書 Status が Draft である。
- 評価対象が作成済み 7 個別 Screen Requirement (SCR-001〜SCR-005・SCR-013・SCR-014) と既存 Design System 4 資産に限定され、SCR-006〜SCR-012 を評価対象・DS 要件へ変換していない。
- 上流・前提、同一レイヤーの評価対象、下流が区別されている。
- Assessment Unit が UI・Component の 1 対 1 対応を前提としていない。
- Evidence Rules が実在する Repository 成果物に限定され、provenance 未確認を対応確認済みへ昇格させない規則を含む。
- Traceability Record Structure・Observation Classification が定義され、観察区分を正式 Status・Design Decision として扱っていない。
- 数値スコア・適合率・合否点を導入していない。
- Recommended Work Order が正式 Phase として登録されず、順序と理由のみを定義している。
- 最初の評価対象が根拠付きで 1 件推薦されている。
- 具体的な評価結果・gap・対応表を記載していない。
- Open Issue / Does Not Decide を確定要件として扱っていない。
- 受入基準の最終確定主体は Open Issue として保持する (§17)。

## 19. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial draft: Design System Alignment Assessment の評価方法・対象・証拠規則・記録構造・観察区分・評価観点・推奨実行順・最初の評価対象を定義 (評価自体は未実施) | Draft |
| 2026-07-16 | 実行状況を同期: Work Order 1 (Baseline 確認) を baseline-assessment.md (Draft) として実施済みと §3/§10/§11/§12/§17 へ注記。評価方法・分類・順序・推薦理由は不変。Work Order 2〜6 は未実施 | Draft |
| 2026-07-16 | 実行状況を同期: Work Order 2 (Service Design 横断整合性評価) を service-design-alignment-assessment.md (Draft) として実施済みと §3/§10 へ注記。Work Order 3〜6 は未着手。評価方法・分類・順序・証拠規則・推薦理由は不変 | Draft |
| 2026-07-16 | 実行状況を同期: Work Order 3 (作成済み 7 個別 Screen Requirement ごとの整合性評価) を screen-requirements-alignment-assessment.md (Draft) として実施済みと §3/§10 へ注記。Work Order 4〜6 は未着手。評価方法・分類・順序・証拠規則・推薦理由は不変 | Draft |
| 2026-07-17 | 実行状況を同期: Work Order 4 (観察結果の横断集約) を alignment-observations-aggregation.md (Draft) として実施済みと §3/§10 へ注記。§3 Facts の「Alignment は未評価」を Work Order 1〜4 の実態と整合する Fact へ是正 (状態整合性修正であり新しい Decision を追加しない)。Work Order 4 は集約のみであり改訂候補と未解決事項の分離は未実施。Work Order 5〜6 は未着手。評価方法・分類・順序・証拠規則・Assessment Unit・Traceability Record Structure・Observation Classification・Quality Criteria・推薦理由・Decision は不変 | Draft |
