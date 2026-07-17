# Travel Design System

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Design System レイヤーの入口・共通管理構造。既存 Design System 資産と、上流 Service Design / Screen Requirements との関係を管理する基盤を定義する。
- Position in Repository: `services/travel/design-system/README.md` — Design System レイヤー (travel サービス配下)。サービス入口は [../README.md](../README.md)。上流成果物は Governance の実在成果物 ([../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md))、Service Design (SD-001〜SD-007, [../service-design/README.md](../service-design/README.md))、Screen Requirements (入口 [../screen-requirements/README.md](../screen-requirements/README.md)・作成順序評価 [../screen-requirements/creation-plan.md](../screen-requirements/creation-plan.md)・作成済みの個別 Screen Requirement)。同一 Design System レイヤーの既存資産 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) との関係は §6 Existing Artifact Inventory・§7 Reference Order を参照。下流成果物 (Assets / Implementation) との関係は §12 を参照。

本 README は Design System レイヤーの入口文書であり、個別のトークン・Component・ブランド値・Design Decision そのものは定義・変更しない。既存 Design System 資産と上流成果物の関係を管理するための責務・原則・境界・Open Issue を定義する。具体的な Alignment Assessment (上流要件と既存資産の対応評価) は後続タスクとし、本文書では実施しない。

## 1. Purpose

- Design System レイヤーの目的・責務と、既存 Design System 資産の位置づけを定義する。
- 上流 Service Design (SD-001〜SD-007) と Screen Requirements (入口 README・Creation Plan・作成済みの個別 Screen Requirement) を、既存 Design System 資産へ接続する際の管理原則・参照方法・境界を定義する。
- 「関係・境界・管理原則を定義する」ことと「実際の Alignment Assessment・対応表・gap 判定・改訂を行う」ことを区別する。後者は本文書では確定しない。
- 既存 Design System が上流成果物と整合しているか、作成済みの個別 Screen Requirement を満たせるかは、本文書では判定しない (未評価として保持する)。

## 2. Scope

### Managed

- Design System レイヤーの目的・責務・管理対象。
- 既存 Design System 資産の一覧化 (実在ファイル名・各正本から引用した Status / version)。
- 上流 Service Design / Screen Requirements と Design System の関係・境界。
- 後続 Alignment Assessment が扱う範囲と、本 README が決めない範囲の境界。
- Alignment Assessment の評価方法・証拠規則・記録構造・推奨実行順の計画 ([alignment-plan.md](alignment-plan.md), Draft)。
- 既存 Design System 文書が参照する外部・内部の出典 (provenance) の追跡方法と Open Issue 管理。
- 既存資産の Status / version の扱い方。
- 下流 Assets / Implementation との関係。
- 未確認・不足・矛盾・未検証事項を Open Issue として保持する方法。

### Not Managed

- トークン・Component・ブランド値・Design Decision の追加・変更・削除。
- 既存 Design System 文書 (`design.md` / JSON / `components.md`) の内容修正・version bump。
- 上流要件と既存資産の具体的な対応表・gap 一覧・traceability の作成。
- ADR・命名規則・用語定義の正本作成、Decision ID の再認定。
- UI・レイアウト・画面構成・URL・route・実装仕様の定義。
- Service Design / Screen Requirements / Governance の内容変更。
- SCR-006〜SCR-012 の Design System 要件の作成。
- Repository 内に正本が存在しない方針名・略称・Decision・Phase・ゲート名・正式な評価 ID の創作。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- Screen Requirements レイヤー入口 README が `In preparation` として存在し、作成順序評価 [../screen-requirements/creation-plan.md](../screen-requirements/creation-plan.md) が Draft として存在する。
- SCR-001〜SCR-005・SCR-013・SCR-014 の個別 Screen Requirement が Draft として存在する。SCR-006〜SCR-012 は未作成 (`Not started`) である ([../screen-requirements/README.md](../screen-requirements/README.md) §14・§15)。
- 国内宿泊サービスの Design System は、Service Design / Screen Requirements 構築以前から存在する既存 Draft 資産である。実在ファイルは `design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md` (§6)。
- 既存 Design System 資産の Status は各正本ファイル上で Draft、version は `0.3.0-draft` である (§6 に各ファイルからの引用を記載)。
- 既存 Design System が SD-001〜SD-007 と整合しているか、作成済みの個別 Screen Requirement を満たせるかは未評価である。
- Alignment Assessment の計画文書 [alignment-plan.md](alignment-plan.md) が Draft として存在する。具体的な Alignment Assessment 自体は未実施である。
- 既存 Design System 文書は、Repository 内に正本が確認できない参照 (`brand-content.md`・`governance/naming-rules.md`・GOV / TVL 等の Decision ID・GitHub URL・follow-up 番号) を含む (§8)。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。

### Decisions

- 本レイヤーの入口・共通管理構造を定義する (個別のトークン・Component・Design Decision は定義・変更しない)。
- 既存 Design System 資産の内容を「正しい」「承認済み」「上流整合済み」「Complete」として扱わない。既存資産が Draft であることと、上流整合性が未評価であることを区別する。
- 上流 Service Design / Screen Requirements を上流成果物として扱い、既存 Design System の記述を上流要求へ昇格させない。
- 未確認・不足・矛盾・未検証・由来不明の事項を推測で補完せず Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 と一致)。
- 具体的な Alignment Assessment (対応・gap・改訂・追加・廃止) は後続タスクで行う。

### Hypotheses

- なし。

### Open Issues

- Alignment 評価方法・評価単位・記録構造・観察区分は [alignment-plan.md](alignment-plan.md) で Draft 定義済み。その妥当性・評価/承認主体・Alignment 完了条件は未決。
- 既存 Design System 文書が参照する不足ファイル・Decision ID・外部参照の正本と有効性。
- （詳細は §16 に集約）

## 4. Layer Responsibility

Design System レイヤーは、上流要求を UI 設計語彙へ接続する下流レイヤーである。責務は以下とする。

- 上流の Service Design / Screen Requirements を変更・再定義しない。
- 上流に存在する要求を、視覚・token・Component・状態・パターン等の設計語彙へ接続する。
- 既存 Design System の記述を上流要求へ昇格させない。
- 上流にない業務仕様・画面仕様・UI 要件を Design System から逆算しない。
- Design System に存在する Component を理由に、利用する UI や画面構成を決定しない。
- 不足は不足として、矛盾は矛盾として、未検証は未検証として、由来不明は由来不明として保持する。
- 具体的な Alignment・改訂・追加・廃止は後続タスクで行う (§10)。

本レイヤーは新しい設計原則 ID や正式な Alignment 方針名を定義しない。

## 5. Relationship with Upstream Artifacts

Design System の上流成果物は、Repository の参照順序 (Governance → Service Design → Screen Requirements → Design System → Assets) 上で先行する実在成果物とする。各成果物の定義を Design System 側で変更・再定義しない。

- **Governance** ([../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md)) — 横断共通の規約・確認事項。ただし命名規則・ADR・レビュー規則・用語定義・Repository principles の正本は未整備である (Governance README が明記)。
- **SD-001 [Service Design Principles](../service-design/principles.md)** (Draft) — 体験設計の上位基準。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** (Draft) — 情報オブジェクトと概念関係。
- **SD-003 [Navigation](../service-design/navigation.md)** (Draft) — 現在地・移動・文脈保持の基準。
- **SD-004 [Content Principles](../service-design/content-principles.md)** (Draft) — 情報表現・状態・不確実性の基準。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** (Draft) — 行動・確約・優先順位の基準。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** (Draft) — 画面候補 (SCR-001〜SCR-014) と責務。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** (Draft) — Accepted な UX 判断の制約。
- **Screen Requirements** — 入口 [README.md](../screen-requirements/README.md) (`In preparation`) / 作成順序評価 [creation-plan.md](../screen-requirements/creation-plan.md) (Draft) / 作成済みの個別 Screen Requirement (§9)。

同一 Design System レイヤーの既存資産 (`design.md` / JSON / `components.md`) は上流成果物ではない。それらとの関係は §6・§7 で扱う。Assets / Implementation は下流成果物であり §12 で扱う。

## 6. Existing Artifact Inventory

最新 main 上で確認できる既存 Design System 資産を、実在ファイル名で一覧化する。Status / version は各正本ファイルから引用する。本文書は既存資産の内容を「正しい」「承認済み」「上流整合済み」と判定しない。

| Artifact | 種別 | Status (実ファイル引用) | version (実ファイル引用) |
| --- | --- | --- | --- |
| [design.md](design.md) | 統合文書 (design.md) | Draft | 0.3.0-draft |
| [semantic.travel.json](semantic.travel.json) | Semantic token | Draft (`$meta.status`) | 0.3.0-draft (`$meta.version`) |
| [primitive.travel.json](primitive.travel.json) | Primitive token | Draft (`$meta.status`) | 0.3.0-draft (`$meta.version`) |
| [components.md](components.md) | Component 仕様 | Draft | 0.3.0-draft |

各成果物について、以下を区別する。

- **確認できる Fact**: 4 ファイルが実在し、各ファイルが自身の Status を Draft、version を `0.3.0-draft` と記載している。JSON 2 ファイルには `$status: placeholder` のトークンが含まれる (例: `radius.card`・`motion.*`・`shadow.*` に follow-up 番号・TVL-0008 の `$note`)。
- **文書自身が主張している Decision / 状態**: 既存文書は TVL-0001〜0012・GOV-0002 等の Decision ID、実測値、placeholder / 実査待ちの区別を自ら記載する。これらは「文書がそう記載している」という Fact であり、Repository 内の正本による裏付けとは区別する (§8)。
- **Repository 内の正本による裏付け**: 既存文書が参照する命名規則・ADR・`brand-content.md` 等の正本は Repository 内に確認できない (§8)。裏付けの有無は後続評価で扱う。
- **後続評価が必要な事項**: 上流 SD-001〜SD-007・作成済みの個別 Screen Requirement との対応、placeholder / 実査待ちトークンの解決、Decision ID の正本確認 (§10・§16)。

## 7. Reference Order

Design System レイヤーの推奨参照順序は以下とする。未作成の成果物にはリンクを作成しない。

1. 本 README (レイヤー入口・共通管理構造)
2. [alignment-plan.md](alignment-plan.md) (Alignment Assessment の計画: 評価方法・証拠規則・記録構造・推奨実行順, Draft)
3. [baseline-assessment.md](baseline-assessment.md) (既存 4 資産の Baseline Assessment: 内部整合性・provenance・placeholder の read-only 確認結果, Draft)
4. [service-design-alignment-assessment.md](service-design-alignment-assessment.md) (Service Design 横断原則と既存 Design System の整合性評価: Work Order 2 の結果, Draft)
5. [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) (作成済み 7 個別 Screen Requirement ごとの整合性評価: Work Order 3 の結果, Draft)
6. [alignment-observations-aggregation.md](alignment-observations-aggregation.md) (Work Order 2・3 の Observation の横断集約: Work Order 4 の結果, Draft)
7. [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md) (集約 Observation の改訂候補と未解決事項の分離: Work Order 5 の結果, Draft)
8. [alignment-amendment-readiness-assessment.md](alignment-amendment-readiness-assessment.md) (改訂候補の改訂着手可否評価: Work Order 6 の結果, Draft)
9. [design.md](design.md) (統合文書, Draft 0.3.0-draft)
10. [semantic.travel.json](semantic.travel.json) (Semantic token, Draft 0.3.0-draft)
11. [primitive.travel.json](primitive.travel.json) (Primitive token, Draft 0.3.0-draft)
12. [components.md](components.md) (Component 仕様, Draft 0.3.0-draft)

この順序は参照上の読み順であり、依存関係・生成順・優先度・実装順を自動的に意味しない。上流 Service Design / Screen Requirements との対応関係は本順序では確定せず、後続 Alignment Assessment で扱う (§10)。

## 8. Source and Provenance Handling

既存 Design System 文書には、Repository 内で正本が確認できない参照が含まれる。最新 main 上で確認した状況は以下のとおり。既存文書の参照切れ自体は本タスクでは修正しない。

- **`brand-content.md`** — `design.md` が §8 等でライティング・価格表記の「正」として参照するが、`services/travel/design-system/` に当該ファイルは存在しない。
- **`governance/naming-rules.md`** — `design.md` §9・`components.md` (§1・§2・§7・§8 等) が命名規則の参照先とするが、当該ファイルは存在しない。Governance README も「既存 Design System 文書が参照する `governance/naming-rules.md` は未作成」と明記する。
- **GOV / TVL 等の Decision ID** — 既存文書は GOV-0002・TVL-0001〜0012 等を参照するが、Governance README は「ADR の正本は未作成」としており、これらを Accepted Decision として裏付ける ADR 正本が Repository 内に確認できない。[owner-decisions.md](../../../governance/owner-decisions.md) は「オーナー確認事項 (分類C)」の一覧であり、ADR 正本ではない。
- **GitHub URL・実装 Repository・follow-up 番号** — 既存文書は Source of Truth の GitHub URL、実装 Repository (`tocoo/tocoo_travel`)、follow-up #2 / #3 / #4 / #5 / #13 等を参照するが、Repository 内の追跡可能な正本への接続は確認できない。

これらの扱いは以下とする。

- 存在しないファイルへのリンクを本 README に作成しない。
- 正本がない Decision ID を Accepted Decision として再認定しない。
- 「既存文書がそのように記載している」という Fact と、「その根拠が Repository 内で確認できる」ことを分離する。
- 不足・参照切れ・由来未確認として Open Issue へ記録する (§16)。
- 本タスクで代替文書・ADR・命名規則・`brand-content.md` を推測作成しない。

## 9. Relationship with Screen Requirements

作成済みの個別 Screen Requirement は、上流 Screen Matrix (SD-006) の画面候補に対応する。現在の上流対象は以下 (すべて Draft)。

| SCR 候補 | 個別 Screen Requirement (実在ファイル) | Status |
| --- | --- | --- |
| SCR-001 Service Entry | [service-entry.md](../screen-requirements/service-entry.md) | Draft |
| SCR-002 Destination Discovery | [destination-discovery.md](../screen-requirements/destination-discovery.md) | Draft |
| SCR-003 Accommodation Search | [accommodation-search.md](../screen-requirements/accommodation-search.md) | Draft |
| SCR-004 Search Results | [search-results.md](../screen-requirements/search-results.md) | Draft |
| SCR-005 Accommodation Detail | [accommodation-detail.md](../screen-requirements/accommodation-detail.md) | Draft |
| SCR-013 Help and Support | [help-and-support.md](../screen-requirements/help-and-support.md) | Draft |
| SCR-014 Editorial Content | [editorial-content.md](../screen-requirements/editorial-content.md) | Draft |

これらについて以下を守る。

- これらはすべて Draft である。
- 作成済み 7 個別 Screen Requirement については、Work Order 3 で個別に整合性評価済み、Work Order 4 で横断集約済み、Work Order 5 で改訂候補と未解決事項へ分離済みである (いずれも Draft, §10)。これは対応関係の記録・整理であり、改訂内容・改定要否・改訂着手可否の決定ではない。
- 各 Screen Requirement の Downstream Impact に記載された例や既存 Component 名を、採用決定と解釈しない。
- 具体的な Component 対応・token 対応・状態対応の記録と改訂候補/未解決事項の整理は Work Order 3〜5 で実施済み。改訂内容・改定要否・改訂着手可否の判断は Work Order 6 以降 (§10) であり、本 README では決定しない。
- 1 つの Screen Requirement と 1 つの Component を 1 対 1 で前提としない。

SCR-006〜SCR-012 は未作成 (`Not started`) であり、依存する業務仕様が未解決である ([../screen-requirements/creation-plan.md](../screen-requirements/creation-plan.md) §10・§12)。これらについて以下を守る。

- 未作成要件を推測して Design System 要件を作らない。
- 予約・決済・認証・会員・変更・取消等を先取りしない。
- 既存 Design System に関連しそうな Component があっても、上流要求として採用しない。
- 後続評価の対象範囲外または未評価として保持する。

## 10. Alignment Assessment Boundary

後続の Alignment Assessment が扱い得る事項と、本 README が決めない範囲を定義する。評価方法・記録構造・推奨実行順は [alignment-plan.md](alignment-plan.md) で Draft として定義された。Work Order 1 の Baseline 確認は [baseline-assessment.md](baseline-assessment.md) (Draft) として、Work Order 2 の Service Design 横断整合性評価は [service-design-alignment-assessment.md](service-design-alignment-assessment.md) (Draft) として、Work Order 3 の作成済み 7 個別 Screen Requirement ごとの整合性評価は [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) (Draft) として、Work Order 4 の Work Order 2・3 の Observation の横断集約は [alignment-observations-aggregation.md](alignment-observations-aggregation.md) (Draft) として、Work Order 5 の集約 Observation の改訂候補と未解決事項の分離は [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md) (Draft) として、Work Order 6 の改訂着手可否の判断は [alignment-amendment-readiness-assessment.md](alignment-amendment-readiness-assessment.md) (Draft) として実施された。これにより Alignment Plan §10 Recommended Work Order 1〜6 が Draft として実施済みである。Work Order 6 の総合判断: Work Order 5 の全 12 候補側面はいずれも「現時点では開始できない」であり、実際の Design System 改訂タスクは現時点では開始できない (共通の阻害 Fact = 改訂タスクの承認・反映・解決主体が Repository 内で未定義。加えて各候補固有の上流 Open Issue・provenance 未確認・placeholder/実査待ち・参照切れ)。Work Order 6 の完了は「着手可否評価を記録したこと」であり、改定開始・Alignment 承認・Alignment 完了ではない。Design System の改定は未着手であり、改定を既定路線としない。実際の改定は本 PR のマージとユーザーの明示的承認を経た別タスクでのみ扱う。

### 後続評価で扱い得る事項

- 作成済みの 7 個別 Screen Requirement と既存 Design System 資産の追跡。
- 要件ごとに必要な設計責務。
- 既存 token / Component / 状態 / pattern で確認できる対応。
- 不足・過剰・矛盾・placeholder・実査待ち・根拠不明・参照切れ。
- 下流反映方法の Open Issue。

### 本 README で決定しない事項

- 具体的な対応表・gap の解決策。
- token の追加・変更・削除。
- Component の追加・変更・削除。
- version bump。
- Design Decision・ADR・命名規則・実装仕様。
- UI・レイアウト・画面構成。
- SCR-006〜SCR-012 の Design System 要件。
- 評価結果の承認・Alignment 完了条件の正式確定。

後続評価用の新規ファイル名・正式な評価 ID は本タスクで確定しない。

## 11. Status and Version Handling

- 本入口 README 自身の Status は `Draft` である。
- 既存資産の Status / version は各正本ファイル (`design.md` / JSON / `components.md`) から引用する。本 README は既存資産の version 正本にならない。
- Alignment 評価 (Work Order 1〜5 は Draft で実施済み) の有無にかかわらず、評価・集約・分離文書の追加だけでは既存資産の version を変更しない。version bump は Work Order 6 以降の改訂着手可否の判断と、その後の承認された改訂タスク (実際の Design System の改定) で扱う。
- 文書追加 (本 README の新設) だけで token package の version を上げない。
- 後続の変更で version bump が必要かは Open Issue とする (§16)。
- `Draft`・placeholder・実査待ち・未着手を混同しない (Draft = 文書全体の状態、placeholder / 実査待ち = 個別トークンの未確定、未着手 = 成果物が存在しない)。
- 入口・要約文書が正本ファイルと異なる version 文字列を記載している誤記は、正本ファイルの表記へ揃える (資産の version 自体は変更しない)。[../README.md](../README.md) の要約が primitive を「0.3.0」と記載していた点は、`primitive.travel.json` の `$meta.version`「0.3.0-draft」へ揃えた。正本ファイルどうしの version 値が乖離している場合は、独断で統一せず Open Issue として記録する (§16)。

## 12. Relationship with Downstream Artifacts

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Assets** ([../assets/README.md](../assets/README.md)) — `services/travel/assets/` に位置し、現在 `Not started`。ロゴ・フォント・アイコン等の実体資産を管理する別レイヤー。Design System との接続方法は Open Issue (§16)。
- **Implementation** — Repository の管理対象外。Design System README だけで実装仕様を確定しない。既存文書に実装 Repository (`tocoo/tocoo_travel`) の記述があっても、実装状態を確認済みとみなさない。Design System から実装画面・URL・route を導出しない。

## 13. Open Issue Handling

- 未確認・不足・矛盾・未検証・由来不明の事項は、推測で補完せず Open Issue として保持する。
- 各事項は本 README の §16、および後続 Alignment Assessment で扱う。
- Open Issue が解決されるまで、それに依存する対応・改訂・version bump・承認を確定しない。
- 既存文書にない回答を推測して付与しない。

## 14. Quality Criteria

本レイヤーおよび後続の成果物には、以下を適用する。

- 単独で読んでも理解できる。
- 責務が明確で、上流・同一レイヤー・下流の関係を混同しない。
- Fact / Decision / Hypothesis / Open Issue が区別されている。
- 既存資産の Status / version を正本ファイルから引用し、二重管理しない。
- 上流成果物 (SD-001〜SD-007・Screen Requirements) の定義を再定義せず参照する。
- 既存 Design System の記述を上流要求へ昇格させない。
- 未確認・不足・矛盾を推測で補完せず Open Issue として扱う。
- 下流 (Assets・Implementation) への関係を分離する。

## 15. Current Status

- 本レイヤー入口 README が `Draft` として存在する (本タスクで新設)。
- 既存 Design System 資産 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) が Draft (`0.3.0-draft`) として存在する (§6)。
- 上流 Service Design 成果物 SD-001〜SD-007 が Draft として存在する。
- Screen Requirements は入口 README (`In preparation`)・Creation Plan (Draft)・作成済みの個別 Screen Requirement (SCR-001〜SCR-005・SCR-013・SCR-014 は Draft、SCR-006〜SCR-012 は `Not started`) として存在する。
- Alignment Assessment の計画文書 [alignment-plan.md](alignment-plan.md) が Draft として存在する (評価方法・記録構造・推奨順を定義)。
- 既存 Design System 4 資産の Baseline Assessment (内部整合性・provenance・placeholder の read-only 確認) が [baseline-assessment.md](baseline-assessment.md) として Draft で実施済みである (Work Order 1)。
- Service Design の横断原則と既存 Design System の整合性評価が [service-design-alignment-assessment.md](service-design-alignment-assessment.md) として Draft で完了した (Work Order 2)。
- 作成済み 7 個別 Screen Requirement ごとの整合性評価が [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) として Draft で完了した (Work Order 3。7 件の個別評価であり横断集約ではない)。
- Work Order 2・3 の Observation の横断集約が [alignment-observations-aggregation.md](alignment-observations-aggregation.md) として Draft で完了した (Work Order 4。Observation の横断集約であり、改訂候補整理・優先順位付け・改定要否判断ではない)。
- 集約 Observation の改訂候補と未解決事項の分離が [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md) として Draft で完了した (Work Order 5。改訂を検討し得る候補と、上流・provenance 等の未解決に依存し確定できない事項へ設計責務の側面単位で分離。改定要否・改訂内容・優先順位・改訂着手可否は決定していない)。
- 改訂候補の改訂着手可否の判断が [alignment-amendment-readiness-assessment.md](alignment-amendment-readiness-assessment.md) として Draft で完了した (Work Order 6)。全 12 候補側面は「現時点では開始できない」であり、実際の Design System 改訂タスクは現時点では開始できない (共通阻害 = 承認・反映・解決主体の未定義、加えて各候補固有の上流 Open Issue・provenance 未確認・placeholder/実査待ち・参照切れ)。これにより Alignment Plan §10 の Work Order 1〜6 が Draft で実施済み。
- Design System の改定は未着手である。着手可否評価の記録は改定開始・Alignment 承認・Alignment 完了を意味しない。実際の改定は本 PR のマージとユーザーの明示的承認を経た別タスクでのみ扱う。
- 下流 Assets は `Not started`、Implementation は Repository 管理対象外。
- 既存文書が参照する一部の出典 (`brand-content.md`・`governance/naming-rules.md`・ADR 正本) は Repository 内に存在しない (§8)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。

- Baseline Assessment ([baseline-assessment.md](baseline-assessment.md)) で確認された Open Issues (placeholder / 実査待ち token・参照切れ・provenance 未確認等) の承認・解決・反映方法。`brand-content.md`・`governance/naming-rules.md`・ADR 正本の不足は解決済みではない。
- 改訂着手可否評価 ([alignment-amendment-readiness-assessment.md](alignment-amendment-readiness-assessment.md), Work Order 6) の承認・反映主体、および Work Order 6 が「現時点では開始できない」とした各候補の未解決事項の解決主体。Work Order 6 は着手可否を記録したのみであり、改訂候補の採用・却下・改定要否・改訂内容・優先順位・実際の改定は決定・実施していない。Work Order 1〜6 の実施は Design System 適合・改定要否決定・改定可能・改訂着手可能・承認済み・Alignment 完了を意味しない。分離・評価された未解決事項 (状態モデル業務定義・Navigation 分類・IA 業務モデル・入力/表示仕様・可逆/回復・文言/命名正本・provenance・placeholder/実査待ち・アクセシビリティ規格) の解決主体、および実際の改訂タスクの承認・反映・解決主体はいずれも Repository 内で未定義。
- Alignment 評価方法・記録構造・観察区分は [alignment-plan.md](alignment-plan.md) で Draft 定義済み。その妥当性・評価/承認主体・実行結果・Alignment 完了条件は未決。
- 評価単位の妥当性。
- traceability の記録方法。
- gap の分類方法。
- 評価・承認主体。
- Design System への反映確認方法。
- version bump の条件。
- 既存 Decision ID (GOV / TVL 等) の正本と有効性。
- Governance の命名規則正本 (`governance/naming-rules.md`) が存在しないこと。
- ADR 正本が存在しないこと。
- `brand-content.md` の参照と実在状況 (存在しない)。
- `governance/naming-rules.md` の参照と実在状況 (存在しない)。
- 既存 follow-up 番号 (#2 / #3 / #4 / #5 / #13 等) の追跡先。
- 既存 GitHub / 実装 Repository 参照の検証方法。
- placeholder / 実査待ちトークンの解決主体。
- 正本ファイルどうしの version 値が乖離した場合の統一方法 (入口・要約文書の誤記は §11 のとおり正本表記へ揃える。[../README.md](../README.md) の primitive 表記は本 PR で「0.3.0-draft」へ是正済み)。
- SCR-006〜SCR-012 を評価対象へ加える条件。
- Assets への接続方法。
- Alignment 完了条件。

## 17. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Define Design System layer foundation (entry README: responsibility, upstream/downstream relationships, existing artifact inventory, provenance handling, and alignment assessment boundary) | Draft |
| 2026-07-16 | Align `../README.md` の primitive version 要約表記を正本 `primitive.travel.json` の `$meta.version`「0.3.0-draft」へ是正し、§11・§16 の記述を更新 (資産 version は不変。PR #43 レビュー対応) | Draft |
| 2026-07-16 | Add alignment-plan.md (Draft) to Scope, Preconditions/Current Status, Reference Order, Alignment Assessment Boundary, and Open Issues (評価計画の追加。評価自体は未実施) | Draft |
| 2026-07-16 | Add baseline-assessment.md (Draft) to Reference Order, Current Status, Alignment Assessment Boundary, and Open Issues (Work Order 1 の Baseline 確認を実施。Work Order 2 以降の上流 Alignment は未実施) | Draft |
| 2026-07-16 | Add service-design-alignment-assessment.md (Draft) to Reference Order, Current Status, and Alignment Assessment Boundary (Work Order 2 の Service Design 横断整合性評価を実施。Work Order 3 の個別 Screen Requirement 整合性評価は未着手) | Draft |
| 2026-07-16 | Add screen-requirements-alignment-assessment.md (Draft) to Reference Order, Current Status, Alignment Assessment Boundary, and Open Issues (Work Order 3 の作成済み 7 個別 Screen Requirement ごとの整合性評価を実施。7 件の個別評価であり横断集約ではない。Work Order 4〜6 と Design System 改定は未着手) | Draft |
| 2026-07-17 | Add alignment-observations-aggregation.md (Draft) to Reference Order, Current Status, Alignment Assessment Boundary, and Open Issues (Work Order 4 の Work Order 2・3 の Observation の横断集約を実施。Observation の横断集約であり改訂候補整理ではない。Work Order 5〜6 と Design System 改定は未着手) | Draft |
| 2026-07-17 | Add alignment-amendment-candidate-separation.md (Draft) to Reference Order, Current Status, Alignment Assessment Boundary, and Open Issues (Work Order 5 の改訂候補と未解決事項の分離を実施。設計責務の側面単位で分離し、改定要否・改訂内容・優先順位・改訂着手可否は未決定)。§9 の「対応評価は未実施」を Work Order 3〜5 実施済みの Fact へ、§11 の「上流との Alignment 未実施を理由に」を現在の version 責務へ状態整合是正。Work Order 6 と Design System 改定は未着手 | Draft |
| 2026-07-17 | Add alignment-amendment-readiness-assessment.md (Draft) to Reference Order, Current Status, Alignment Assessment Boundary, and Open Issues (Work Order 6 の改訂着手可否の判断を実施。全 12 候補側面は「現時点では開始できない」、実際の Design System 改訂タスクは現時点では開始できない = 承認/解決主体の未定義と各候補固有の上流 Open Issue・provenance・placeholder/実査待ち・参照切れ)。これにより Work Order 1〜6 が Draft で実施済み。着手可否評価の記録は改定開始・Alignment 承認・完了ではない。Design System 本体は未変更 (Status Draft・version 0.3.0-draft を維持)・改定は未着手 | Draft |
