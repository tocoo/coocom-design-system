# Travel Search Results Screen Requirement

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補 SCR-004 Search Results に対応する個別 Screen Requirement の初版 Draft
- Position in Repository: `services/travel/screen-requirements/search-results.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)、作成順序評価は [creation-plan.md](creation-plan.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Design System / Implementation) との関係は §15 Downstream Impact を参照。

本文書はファイル名 `search-results.md` で作成する。これは記述的な暫定ファイル名であり、正式なファイル命名規則を確定するものではない (§16 Open Issues)。文書は Title およびファイル名で識別し、`SCR-004` を Screen Requirement 文書 ID として再定義しない。

## 1. Purpose

- 画面候補 SCR-004 Search Results ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) の責務を、Repository 内の既存上流成果物 (SD-001〜SD-007, Governance) から確認できる範囲で個別 Screen Requirement として記述する。
- 検索条件に対応する Accommodation 候補を確認・比較し、詳細検討へ進むための要件を定義する。
- 未定義の一覧仕様・並び替え・絞り込み・ランキング・表示項目・Price/Availability/Review/Policy の表示基準等は補完せず、Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- SCR-004 の責務を具体的な一覧・カード・表等の UI へ具体化しない。SCR-004 を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

## 2. Related Screen Matrix Candidates

- **SCR-004 Search Results** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) — 唯一の対応画面候補。責務は「Accommodation 候補を確認・比較する」(Matrix 表)、詳細は「検索条件に対応する Accommodation 候補を確認・比較する画面または画面群」(§5)。
- 本文書は SCR-004 に既に定義された責務と利用者タスクのみを扱う。
- 候補の表示単位・表示順・一覧仕様、およびエラー・中断専用画面の要否は確定しない (§16 Open Issues)。
- SCR-003 Accommodation Search と SCR-005 Accommodation Detail は関係する候補として参照できるが、SCR-004 の Related Screen Matrix Candidate へ追加せず、それらの内部要件も取り込まない。
- 本文書の作成単位 (SCR-004 単独) は、未決事項を保持したまま作成可能な範囲を文書化するための暫定的な作成単位であり、将来の分割・統合判断により文書構成が変更され得る。本文書の作成順は、探索候補群の正式な作成順を確定するものではない ([creation-plan.md](creation-plan.md) §10)。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は SCR-004 Search Results を画面候補 (Status: Draft) として管理する。
- レイヤー入口 [README.md](README.md)、作成順序評価 [creation-plan.md](creation-plan.md)、先行する個別要件 ([service-entry.md](service-entry.md) SCR-001 / [accommodation-search.md](accommodation-search.md) SCR-003 / [help-and-support.md](help-and-support.md) SCR-013 / [editorial-content.md](editorial-content.md) SCR-014) が存在する。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は SCR-004 の要件を、上流成果物から確認できる範囲で記述する。
- 作成単位を SCR-004 単独とする (暫定。§2)。
- Search Criteria・Accommodation を Primary IA Objects、Availability・Price・Review・Policy を Supporting IA Objects として扱い、主従を逆転しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-004)。
- 未定義の一覧仕様・並び替え・絞り込み・ランキング・表示基準は推測で補完せず Open Issue として保持する (UXDR-TRAVEL-001)。
- Navigation と CTA を別責務として記述する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities と一致)。
- ファイル名 `search-results.md` は暫定であり、正式命名規則を確定しない。

### Hypotheses

- なし。

### Open Issues

- 候補として表示する Accommodation の属性・表示単位・表示順。
- 並び替え・絞り込み・ランキングの有無と基準。
- Availability・Price・Review・Policy の状態・構造・提供元・表示基準。
- SCR-003 から引き継ぐ条件と文脈、SCR-005 への接続。
- (詳細は §16 に集約)

## 4. User Tasks

[Screen Matrix](../service-design/screen-matrix.md) §5 SCR-004 の Primary User Tasks を上流参照する (再定義しない)。

- 候補を確認・比較し、詳細検討へ進む。

上位基準として SDP-001 User Task Clarity (利用者が現在何を行い、次に何を行えるかを理解できる) を適用する。比較を成立させる具体的な基準・表示項目は確定しない (§16 Open Issues)。

## 5. Information Responsibilities

[Information Architecture](../service-design/information-architecture.md) (SD-002) を上流参照する。IA オブジェクトの定義・追加・変更は行わない。Screen Matrix §5 SCR-004 の Primary / Supporting の区別を保つ。

### Primary IA Objects

- **IA-OBJ-002 Search Criteria** — 現在の探索意図を表す条件を、候補提示の文脈として扱う。入力項目・確認/変更単位は確定しない (IA-OBJ-002 Does Not Decide)。
- **IA-OBJ-003 Accommodation** — 利用者が識別・比較・評価する中心的な情報単位として扱う。属性一覧は確定しない (IA-OBJ-003 Does Not Decide)。

### Supporting IA Objects

- **IA-OBJ-006 Availability** — 条件に応じた予約可否を、候補評価の補助として参照する。リアルタイム性・更新方式は取り込まない (IA-OBJ-006 Does Not Decide)。
- **IA-OBJ-007 Price** — 費用の観点を候補評価の補助として参照する。料金構造・表示単位は取り込まない (IA-OBJ-007 Does Not Decide)。
- **IA-OBJ-009 Review** — 第三者的な評価の観点を候補評価の補助として参照する。提供元・評価対象・信頼性は取り込まない (IA-OBJ-009 Open Issue)。
- **IA-OBJ-008 Policy** — 判断に影響する条件・制約を候補評価の補助として参照する。正式な分類は取り込まない (IA-OBJ-008 Open Issue)。

Supporting IA Objects (Availability / Price / Review / Policy) を根拠として、在庫・料金・レビュー・ポリシーの業務モデルや具体的表示項目を追加しない。Primary と Supporting の主従を逆転しない ([../service-design/information-architecture.md](../service-design/information-architecture.md) §5 IA-OBJ-003 Relationships「Search Criteria が Accommodation を絞り込む」)。

## 6. Functional Requirements

上流成果物から確認できる能力・責務のみを記述する。業務仕様が未定義の事項は要件化せず Open Issue とする ([README.md](README.md) §6)。

- 現在の Search Criteria の文脈を識別できること (IA-OBJ-002, NVP-001 Current Location Visibility)。
- Search Criteria に対応する Accommodation 候補を確認できること (IA-OBJ-002 / IA-OBJ-003, SDP-001)。
- 候補を比較し、詳細検討へ進むタスクを支援すること (SDP-001, SDP-004 Consistent Mental Model)。
- 比較に必要な情報の意味・状態・不確実性を理解可能にすること (SDP-003 Transparent Conditions, SDP-005 State Visibility)。
- 条件変更や再探索時に、既存の探索文脈を不必要に失わせないこと (NVP-003 Preserved Context, NAV-005 History and Recovery Navigation)。
- Accommodation の詳細に関係する関連情報へ移動し得ること (NAV-003 Contextual Navigation)。
- エラーまたは中断時に、状態と回復可能な行動を理解可能にすること (SDP-006 Recoverability, CTP-007 Actionable Error and Recovery)。
- 利用不能・未確定・条件付きの情報を確定事項として扱わないこと (SDP-008 Evidence over Assumption, CTP-006 Explicit State and Uncertainty)。

以下は要件として確定しない (Open Issue として §16 で扱う)。

- 候補として表示する Accommodation の属性・表示単位・表示順。
- 並び替え・絞り込みの有無と基準。
- ランキング・掲載順の基準。
- Availability・Price・Review・Policy の具体的な値・分類・表示基準・更新頻度。
- 候補が存在しない場合の扱い。
- SCR-003 から引き継ぐ具体的なデータ、SCR-005 へ渡す具体的なデータ。

## 7. Content Requirements

[Content Principles](../service-design/content-principles.md) (SD-004) の Content Category と原則を上流参照する。SCR-004 の Content Categories は Identification / Decision Support / Conditions and Policies ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-004)。

- **Identification** — 各候補と現在の検索条件を識別可能にする (CTP-002 Plain and Direct Language, CTP-005 Consistent Terminology)。
- **Decision Support** — 比較・評価・選択を支援する情報を、目的を先に理解できる形で示す (CTP-001 Purpose Before Detail, CTP-003 Conditions Near Decisions, CTP-004 Evidence-backed Claims, CTP-006 Explicit State and Uncertainty)。
- **Conditions and Policies** — 条件・制約・例外を判断へ影響する位置・時点で示す (CTP-003 Conditions Near Decisions, CTP-005, CTP-006)。
- 根拠のない優位性・限定性・人気・希少性を表現しない (CTP-004 Evidence-backed Claims)。
- 情報の更新時点・不確実性・変動可能性を確定情報として表現しない (CTP-006 Explicit State and Uncertainty)。
- 事実・条件・販促表現を混同しない (CTP-010 Separate Fact, Decision, and Promotion)。
- 情報の意味を色・アイコン・位置だけに依存させない (CTP-008 Accessible and Scannable Content)。
- 同じ概念に一貫した用語を用いる (CTP-005 Consistent Terminology, NVP-005 Consistent Meaning)。

具体的なラベル・表示項目・説明文・エラー文言・ブランドトーンは決定しない (§13 Does Not Decide)。

## 8. Navigation Requirements

[Navigation](../service-design/navigation.md) (SD-003) を上流参照する。SCR-004 の Navigation Types は NAV-002 / NAV-003 / NAV-004 / NAV-005 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-004)。4 分類を責務として区別して記述する。

- **NAV-002 Local Navigation** — 候補領域内部の関連情報へ移動し得るようにする。分類単位・タブ等は確定しない (NAV-002 Does Not Decide)。
- **NAV-003 Contextual Navigation** — 現在の候補と関連する Accommodation 詳細等へ移動し得るようにする。表示条件は確定しない (NAV-003 Does Not Decide)。
- **NAV-004 Task Navigation** — 確認・比較・詳細検討というタスク進行と、次に可能な行動を理解可能にする。必要以上に早い確約を求めない (NAV-004 Does Not Decide, SDP-002 Progressive Commitment)。
- **NAV-005 History and Recovery Navigation** — 条件変更・再探索時に既存の探索文脈を不必要に失わせず、前状態へ戻れるようにする。保持方式は確定しない (NAV-005 Does Not Decide, NVP-003 Preserved Context)。
- 移動先または結果を事前に予測可能にする (NVP-002 Predictable Destination)。
- 現在の判断に不要な選択肢を過剰に提示しない (NVP-007 Progressive Disclosure)。
- 内部組織やシステム都合ではなく利用者タスクを基準にする (NVP-006 Task over Organization)。
- Navigation と CTA を同一責務として扱わない (UXDR-TRAVEL-003, §9)。

具体的なメニュー・タブ・リンク・ラベル・配置・表示条件・画面遷移は確定しない (§13 Does Not Decide)。

## 9. CTA Requirements

[CTA Principles](../service-design/cta-principles.md) (SD-005) を上流参照する。SCR-004 に関する記述は [../service-design/cta-principles.md](../service-design/cta-principles.md) §7 Relationship with Screen Matrix の SCR-004 行 (CTA Consideration「比較・詳細確認・条件変更・選択の優先関係を整理する」)。Navigation と CTA は別責務とする (UXDR-TRAVEL-003)。

- 比較・詳細確認・条件変更・選択の優先関係を整理する。ただし主要 CTA を確定しない (CTA-002 One Clear Primary Action)。
- 候補の評価・選択に関わる行動の前に、関連する Price・Policy・Availability を確認可能にする (CTA-005 Conditions Before Action)。
- 行動の対象と結果を実行前に理解可能にする (CTA-001 Action Clarity)。
- 利用可能・利用不能・未確定の状態を曖昧にしない (CTA-007 Explicit State and Availability)。
- Navigation Action を自動的に主要 CTA として扱わない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §8 Boundary between CTA and Navigation)。
- 具体的な選択行動や成立条件が未定義の場合、主要 CTA を確定しない (SDP-010 Incremental Definition)。
- CTA の意味・状態・実行可能性を視覚だけに依存させない (CTA-009 Accessible Activation)。

具体的な CTA 文言・数・優先順位・配置・色・Component は決定しない (§13 Does Not Decide)。

## 10. State and Feedback Requirements

対象状態は [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-004 に存在する Exploring, Evaluating, Error / Interrupted のみとする。[Navigation](../service-design/navigation.md) §6 Navigation State Model を上流参照する。`Error / Interrupted` は上流 Navigation State の複合名として扱い、`Error` と `Interrupted` という別々の新規状態へ再定義しない。

- **Exploring** — 候補・情報を探索している状態を理解できること (NVP-003 Preserved Context)。
- **Evaluating** — 候補・条件を比較・確認している状態と、対象・条件の文脈を理解できること (SDP-005 State Visibility)。
- **Error / Interrupted** — エラー・中断の発生と、原因・回復可能な行動・戻り先を理解できること (SDP-006 Recoverability, CTP-007 Actionable Error and Recovery)。
- 情報の状態・不確実性・変動可能性を確定情報として示さないこと (CTP-006 Explicit State and Uncertainty)。
- 状態変化を色・位置・アニメーションだけで伝えないこと (SDP-007, CTP-008)。
- `Entry`・`Committing`・`Completed` 等を、SCR-004 の確定状態として独断で追加しないこと ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-004 は Exploring, Evaluating, Error / Interrupted のみを定義)。

具体的な空結果・在庫切れ・料金変更等の業務状態や挙動は決定しない (§13 Does Not Decide)。

## 11. Accessibility Requirements

SDP-007 Accessibility by Default / NVP-008 Accessible Navigation / CTP-008 Accessible and Scannable Content / CTA-009 Accessible Activation の範囲で記述する。

- キーボード・支援技術・異なる画面サイズを例外扱いしない (SDP-007, NVP-008)。
- 候補の識別・比較に必要な情報の構造・順序・関係を支援技術で理解可能にする (CTP-008)。
- Navigation と CTA の意味・状態を視覚だけで伝えない (NVP-008, CTA-009)。
- エラー・中断時に問題と回復方法を理解可能にする (CTP-007)。
- 読む順序・比較の関係を画面サイズによって失わせない (CTP-008)。
- モバイルでも候補の確認・比較・条件変更・回復を可能にする (SDP-007)。

具体的な規格・達成レベル・HTML 属性・フォーカス実装・Component 仕様は決定しない (§13 Does Not Decide)。

## 12. Constraints

- 上流成果物 (SD-001〜SD-007) の定義を再定義・変更しない ([README.md](README.md) §9)。
- 作成単位は SCR-004 単独に限定し、Supporting IA Objects から業務モデル・表示項目を、SCR-003・SCR-005 から内部要件を取り込まない (§2, §5)。
- 未定義事項を Fact または Decision として扱わず、Open Issue として保持する (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。
- 確定可能な範囲からのみ記述し、未決事項へ依存する要件を確定しない (SDP-010 Incremental Definition)。
- サービス全体の整合性と一貫した概念・用語を優先する (SDP-004 Consistent Mental Model, SDP-009 Service-wide Coherence)。

## 13. Does Not Decide

本文書だけでは以下を確定しない。

- 一覧・カード・表等の具体的 UI・レイアウト・ワイヤーフレーム ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-004 Does Not Decide)。
- 表示項目・表示順・情報密度。
- 並び替え・絞り込み・条件変更の具体的 UI・基準、ランキング・レコメンド・広告・掲載順ロジック。
- 結果件数・ページネーション・無限スクロール。
- Price・Availability・Review・Policy の具体的な値・分類・表示基準・更新頻度。
- 空結果・在庫切れ・料金変更等の業務状態や挙動、Accommodation 選択の意味・確約レベル。
- SCR-003 から渡されるデータ・SCR-005 へ渡すデータ、API・DB・検索エンジン・キャッシュ。
- URL・route・クエリパラメータ・サイトマップ・画面遷移。
- CTA 文言・数・配置・色・Component。
- Screen Requirement ID 体系・ファイル命名規則。

## 14. Upstream References

上流成果物は [README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。定義を本文書で変更しない。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — SDP-001 User Task Clarity / SDP-002 Progressive Commitment / SDP-003 Transparent Conditions / SDP-004 Consistent Mental Model / SDP-005 State Visibility / SDP-006 Recoverability / SDP-007 Accessibility by Default / SDP-008 Evidence over Assumption / SDP-009 Service-wide Coherence / SDP-010 Incremental Definition。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — Primary: IA-OBJ-002 Search Criteria / IA-OBJ-003 Accommodation。Supporting: IA-OBJ-006 Availability / IA-OBJ-007 Price / IA-OBJ-009 Review / IA-OBJ-008 Policy。
- **SD-003 [Navigation](../service-design/navigation.md)** — NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-005 History and Recovery Navigation、NVP-001 Current Location Visibility / NVP-002 Predictable Destination / NVP-003 Preserved Context / NVP-005 Consistent Meaning / NVP-006 Task over Organization / NVP-007 Progressive Disclosure / NVP-008 Accessible Navigation、Navigation State Model (Exploring, Evaluating, Error / Interrupted)。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Categories: Identification / Decision Support / Conditions and Policies、CTP-001 Purpose Before Detail / CTP-002 Plain and Direct Language / CTP-003 Conditions Near Decisions / CTP-004 Evidence-backed Claims / CTP-005 Consistent Terminology / CTP-006 Explicit State and Uncertainty / CTP-007 Actionable Error and Recovery / CTP-008 Accessible and Scannable Content / CTP-010 Separate Fact, Decision, and Promotion。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA-001 Action Clarity / CTA-002 One Clear Primary Action / CTA-005 Conditions Before Action / CTA-007 Explicit State and Availability / CTA-009 Accessible Activation、§7 Relationship with Screen Matrix の SCR-004 行、§8 Boundary between CTA and Navigation。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — SCR-004 Search Results の責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements / UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens / UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 15. Downstream Impact

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 本 Screen Requirement の下流に位置する。既存 Design System (例: Card (ResultCard)・PriceTag・ReviewStars) を参照して実現可能性や未整備箇所を確認できるが、既存 Component を上流要求へ昇格させない。具体的な Component・レイアウト・トークン・表示項目を指定しない。既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。
- **Implementation** — Repository の管理対象外。本文書だけで実装仕様を確定しない。SCR-004 を実装 1 画面・URL・route と同一視しない (UXDR-TRAVEL-002)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。各 Open Issue が影響する要件節を可能な範囲で示す。

- **候補として表示する Accommodation の属性** — §5 Information Responsibilities, §6 Functional Requirements。
- **候補の表示単位と表示順** — §6, §7 Content Requirements。
- **並び替えの有無と基準** — §6, §8 Navigation Requirements。
- **絞り込みの有無と基準** — §6, §8。
- **ランキング・掲載順の基準** — §6, §7 (CTP-004)。
- **Search Criteria の表示・確認・変更単位** — §5, §6, §8。
- **SCR-003 から引き継ぐ条件と文脈** — §2, §6。
- **Accommodation 比較を成立させる基準** — §4 User Tasks, §6, §7。
- **Availability の状態・粒度・表示基準** — §5, §7, §10 State and Feedback Requirements。
- **Price の構造・対象・表示基準** — §5, §7。
- **Review の提供元・評価対象・表示基準** — §5, §7。
- **Policy の分類・表示基準** — §5, §7。
- **情報の更新時点と不確実性の伝達方法** — §7 (CTP-006), §10。
- **候補が存在しない場合の扱い** — §6, §10。
- **エラー・中断の種別と回復方法** — §10, §11 Accessibility Requirements。
- **SCR-005 への接続と引き渡す情報** — §2, §6, §8。
- **条件変更時の保持・復元方式** — §8 (NAV-005)。
- **詳細確認・条件変更・比較・選択の優先関係** — §9 CTA Requirements。
- **Accommodation 選択の意味と確約レベル** — §9。
- **URL・route・クエリパラメータ・画面遷移** — §6, §13。
- **モバイルでの比較・条件変更方法** — §8, §11。
- **Screen Requirement ID 体系** — 文書全体 ([README.md](README.md) §7)。
- **ファイル命名規則** — 本文書のファイル名 `search-results.md` は暫定 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — §17 Acceptance Criteria。
- **Design System への反映確認方法** — §15 Downstream Impact ([README.md](README.md) §17)。

## 17. Acceptance Criteria

未定義の UI・業務仕様を確定しない範囲で記述する。最終確定主体は Open Issue として維持する (§16)。

- 文書が [README.md](README.md) §6 Common Document Structure を満たしている。
- Related Screen Matrix Candidate が SCR-004 として追跡可能であり、SCR-004 のみである。
- [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-004 の Responsibility・Primary User Tasks・Primary IA Objects・Supporting IA Objects・Navigation Types・Content Categories・Navigation States と一致している。
- Search Criteria・Accommodation を Primary、Availability・Price・Review・Policy を Supporting として扱い、主従を逆転していない (§5)。
- Supporting IA Objects から未定義の業務仕様や表示項目を導出していない (§5)。
- Navigation と CTA の要件が別節・別責務として記述され、NAV-002・NAV-003・NAV-004・NAV-005 を混同していない (§8, §9)。
- 状態が Exploring, Evaluating, Error / Interrupted のみであり、`Error / Interrupted` を複合状態名として扱い、未定義状態を独断で追加していない (§10)。
- 一覧・並び替え・絞り込み・ランキング・表示基準を確定していない (§6, §13)。
- SCR-003・SCR-005 の内部要件を取り込んでいない (§2)。
- URL・route・UI・Component・API・DB を確定していない (§13, §15)。
- 未定義の要求が Open Issue として追跡でき、上流成果物の ID・正式名称を追跡できる (§14, §16)。
- 下流 Design System との関係が Downstream Impact へ分離されている (§15)。
- 文書 Status が Draft である。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial draft of Travel Search Results Screen Requirement (SCR-004) | Draft |
