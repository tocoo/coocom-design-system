# Travel Accommodation Detail Screen Requirement

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補 SCR-005 Accommodation Detail に対応する個別 Screen Requirement の初版 Draft
- Position in Repository: `services/travel/screen-requirements/accommodation-detail.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)、作成順序評価は [creation-plan.md](creation-plan.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。同一レイヤーの関係候補との関係は §2、下流成果物 (Design System / Implementation) との関係は §15 Downstream Impact を参照。

本文書はファイル名 `accommodation-detail.md` で作成する。これは記述的な暫定ファイル名であり、正式なファイル命名規則を確定するものではない (§16 Open Issues)。文書は Title およびファイル名で識別し、`SCR-005` を Screen Requirement 文書 ID として再定義しない。

## 1. Purpose

- 画面候補 SCR-005 Accommodation Detail ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) の責務を、Repository 内の既存上流成果物 (SD-001〜SD-007, Governance) から確認できる範囲で個別 Screen Requirement として記述する。
- 利用者が Accommodation の情報と関連情報を確認し、評価するための要件を定義する。
- 未定義の詳細レイアウト・情報構成・遷移、Room/Stay Plan/Price/Availability の業務モデル、Review/Policy/Content の表示基準等は補完せず、Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- SCR-005 の責務を具体的な詳細レイアウト・情報構成・UI へ具体化しない。SCR-005 を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

## 2. Related Screen Matrix Candidates

- **SCR-005 Accommodation Detail** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) — 唯一の対応画面候補。責務は「施設と関連情報を確認する」、Purpose は「Accommodation の情報と関連 Room、Stay Plan、Review、Policy を確認する画面または画面群」。
- 本文書は SCR-005 に既に定義された責務と利用者タスクのみを扱う。詳細レイアウト・情報構成・遷移は確定しない (§13 Does Not Decide)。
- SCR-004 Search Results と SCR-006 Room and Plan Selection は関係する候補として参照できるが、SCR-005 の Related Screen Matrix Candidate へ追加せず、それらの内部要件も取り込まない。特に SCR-006 の Room / Stay Plan 選択・確約・在庫・料金・予約開始を SCR-005 へ取り込まない。
- 本文書の作成単位 (SCR-005 単独) は、未決事項を保持したまま作成可能な範囲を文書化するための暫定的な作成単位であり、SCR-005 と SCR-006 の責務境界・分割・統合は確定しない (§16 Open Issues)。本文書の作成順は、探索候補群の正式な作成順を確定するものではない ([creation-plan.md](creation-plan.md) §10)。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は SCR-005 Accommodation Detail を画面候補 (Status: Draft) として管理する。
- レイヤー入口 [README.md](README.md)、作成順序評価 [creation-plan.md](creation-plan.md)、先行する個別要件 ([service-entry.md](service-entry.md) SCR-001 / [accommodation-search.md](accommodation-search.md) SCR-003 / [search-results.md](search-results.md) SCR-004 / [help-and-support.md](help-and-support.md) SCR-013 / [editorial-content.md](editorial-content.md) SCR-014) が存在する。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は SCR-005 の要件を、上流成果物から確認できる範囲で記述する。
- 作成単位を SCR-005 単独とする (暫定。§2)。
- Accommodation を Primary IA Object、Destination・Room・Stay Plan・Review・Policy・Content を Supporting IA Objects として扱い、主従を逆転しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-005)。
- 情報確認と Room / Stay Plan 選択を区別し、選択・確約・在庫・料金・予約開始を SCR-005 で定義しない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §7 SCR-005 行)。
- 未定義の業務モデル・表示基準は推測で補完せず Open Issue として保持する (UXDR-TRAVEL-001)。
- Navigation と CTA を別責務として記述する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities と一致)。
- ファイル名 `accommodation-detail.md` は暫定であり、正式命名規則を確定しない。

### Hypotheses

- なし。

### Open Issues

- Accommodation の正式な属性一覧、施設情報の表示範囲・単位・順。
- Room・Stay Plan と Accommodation の正式な業務関係、SCR-005/SCR-006 の責務境界。
- Review・Policy・Content の表示基準。
- (詳細は §16 に集約)

## 4. User Tasks

[Screen Matrix](../service-design/screen-matrix.md) §5 SCR-005 の Primary User Tasks を上流参照する (再定義しない)。

- 施設情報と関連情報を確認し、評価する。

上位基準として SDP-001 User Task Clarity (利用者が現在何を行い、次に何を行えるかを理解できる) を適用する。評価を成立させる具体的な表示項目・基準は確定しない (§16 Open Issues)。

## 5. Information Responsibilities

[Information Architecture](../service-design/information-architecture.md) (SD-002) を上流参照する。IA オブジェクトの定義・追加・変更は行わない。Screen Matrix §5 SCR-005 の Primary / Supporting の区別を保つ。

### Primary IA Objects

- **IA-OBJ-003 Accommodation** — 利用者が施設を識別・比較・評価するための中心的な情報単位として扱う。正式な属性一覧は確定しない (IA-OBJ-003 Does Not Decide)。

### Supporting IA Objects

- **IA-OBJ-001 Destination** — 施設が所在する地理/目的地の観点を、施設評価の補助として参照する (IA-OBJ-003 Relationships「Accommodation は Destination に所在する」)。
- **IA-OBJ-004 Room** — 施設が含む/提供する宿泊単位を、確認の補助として参照する。正式な業務関係は取り込まない (IA-OBJ-004 Open Issue)。
- **IA-OBJ-005 Stay Plan** — 施設が提供する販売単位を、確認の補助として参照する。業務モデルは取り込まない (IA-OBJ-005 Open Issue)。
- **IA-OBJ-009 Review** — 施設に対する第三者的評価の観点を補助として参照する。提供元・評価対象・信頼性は取り込まない (IA-OBJ-009 Open Issue)。
- **IA-OBJ-008 Policy** — 施設に適用される条件・制約を補助として参照する。正式な分類は取り込まない (IA-OBJ-008 Open Issue)。
- **IA-OBJ-012 Content** — 施設評価を支援する説明・案内的情報を補助として参照する。分類は取り込まない (IA-OBJ-012 Open Issue)。

Supporting IA Objects を根拠として、具体的な表示項目や業務仕様を導出しない。Primary と Supporting の主従を逆転しない。**Price (IA-OBJ-007) と Availability (IA-OBJ-006) は SCR-005 の IA Objects として定義されていないため、本文書の情報責務・要件へ追加しない** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-005)。

## 6. Functional Requirements

上流成果物から確認できる能力・責務のみを記述する。業務仕様が未定義の事項は要件化せず Open Issue とする ([README.md](README.md) §6)。

- 利用者が Accommodation を識別できること (IA-OBJ-003, SDP-001)。
- 利用者が Accommodation の情報を確認できること (IA-OBJ-003, SDP-001)。
- 利用者が施設情報と関連情報 (Destination / Room / Stay Plan / Review / Policy / Content) を確認し、評価できること (IA-OBJ-003 Relationships, SDP-004 Consistent Mental Model)。
- 施設に適用される条件・制約 (Policy) を、判断へ影響する位置・時点で確認できること (SDP-003 Transparent Conditions, CTP-003 Conditions Near Decisions)。
- 関連情報 (Room / Stay Plan / Review / Policy 等) を確認した後、対象 Accommodation の文脈へ戻れること (NVP-003 Preserved Context, NAV-003 Contextual Navigation)。
- 情報が利用不能・未確定・条件付きの場合、その状態を確定情報と区別して識別できること (SDP-005 State Visibility, CTP-006 Explicit State and Uncertainty)。
- エラーまたは中断時に、状態と回復可能な行動を理解できること (SDP-006 Recoverability, CTP-007 Actionable Error and Recovery)。
- 情報の確認・評価と、Room / Stay Plan の選択を区別すること。選択・確約・予約開始を本画面候補で成立させない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §7 SCR-005 行, §9)。

以下は決定しない (Open Issue として §16 で扱う)。

- Accommodation の具体的な表示項目・属性一覧・表示順・情報密度。
- 写真・設備・アクセス情報等の表示方式。
- Room / Stay Plan の表示単位・確認範囲、SCR-006 での選択との境界。
- Room / Stay Plan / Price / Availability の業務モデル、Price・Availability の表示・状態。
- Review・Policy・Content の表示基準。
- SCR-004 から受け取るデータ、SCR-006 へ渡すデータ。
- 情報確認から Room / Stay Plan 選択へ進む条件。

## 7. Content Requirements

[Content Principles](../service-design/content-principles.md) (SD-004) の Content Category と原則を上流参照する。SCR-005 の Content Categories は Identification / Decision Support / Conditions and Policies / Editorial and Support ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-005)。

- **Identification** — Accommodation と関連対象を識別可能にする (CTP-002 Plain and Direct Language, CTP-005 Consistent Terminology)。
- **Decision Support** — 施設評価に必要な情報を、目的を先に理解できる形で示す (CTP-001 Purpose Before Detail, CTP-003 Conditions Near Decisions, CTP-004 Evidence-backed Claims, CTP-006 Explicit State and Uncertainty)。
- **Conditions and Policies** — 施設に適用される条件・制約・例外を、判断へ影響する位置・時点で示す (CTP-003 Conditions Near Decisions, CTP-005, CTP-006)。
- **Editorial and Support** — 施設評価を支援する編集・案内的情報を提供し、事実・条件と混同させない (CTP-004 Evidence-backed Claims, CTP-008 Accessible and Scannable Content, CTP-009 Context-preserving References, CTP-010 Separate Fact, Decision, and Promotion)。
- 根拠のない優位性・限定性・人気・希少性を表現しない (CTP-004)。
- 情報の不確実性・変動可能性を確定情報として表現しない (CTP-006)。
- Review・Policy 等の参照時に、対象と元の文脈を失わせない (CTP-009 Context-preserving References)。
- 事実・条件・販促表現を混同しない (CTP-010)。
- 情報の意味を色・アイコン・位置だけに依存させない (CTP-008)。

具体的な表示項目・ラベル・説明文・Review/Policy 本文・ブランドトーンは決定しない (§13 Does Not Decide)。

## 8. Navigation Requirements

[Navigation](../service-design/navigation.md) (SD-003) を上流参照する。SCR-005 の Navigation Types は NAV-002 / NAV-003 / NAV-004 / NAV-006 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-005)。4 分類を責務として区別して記述する。

- **NAV-002 Local Navigation** — 施設内部の関連情報 (Room / Stay Plan / Review / Policy 等) への移動と関係理解を支援する。情報構成・タブ等は確定しない (NAV-002 Does Not Decide)。
- **NAV-003 Contextual Navigation** — Accommodation と概念関係のある対象 (Room・Stay Plan・Review・Policy・Destination) へ辿れるようにする。表示条件は確定しない (NAV-003 Does Not Decide)。
- **NAV-004 Task Navigation** — 確認・評価というタスク進行と、次に可能な行動を理解可能にする。必要以上に早い確約を求めない (NAV-004 Does Not Decide, SDP-002 Progressive Commitment)。
- **NAV-006 Utility Navigation** — 主要タスクを阻害せず、補助的な情報・機能へ到達可能にする。対象範囲は確定しない (NAV-006 Does Not Decide)。
- 移動先または結果を事前に予測可能にする (NVP-002 Predictable Destination)。
- 補助情報を確認した後、元の対象へ戻れる文脈を維持する (NVP-003 Preserved Context)。
- 現在の判断に不要な選択肢を過剰に提示しない (NVP-007 Progressive Disclosure)。
- 内部組織やシステム都合ではなく利用者タスクを基準にする (NVP-006 Task over Organization)。
- Navigation と CTA を同一責務として扱わない (UXDR-TRAVEL-003, §9)。

具体的なタブ・アンカー・リンク・ラベル・配置・表示条件・画面遷移は確定しない (§13 Does Not Decide)。

## 9. CTA Requirements

[CTA Principles](../service-design/cta-principles.md) (SD-005) を上流参照する。SCR-005 に関する記述は [../service-design/cta-principles.md](../service-design/cta-principles.md) §7 Relationship with Screen Matrix の SCR-005 行 (CTA Consideration「情報確認と Room / Stay Plan 選択を区別する」)。Navigation と CTA は別責務とする (UXDR-TRAVEL-003)。SCR-005 へ直接適用できる原則のみを参照する。

- 情報確認・評価の行動と、Room / Stay Plan 選択の行動を区別する (CTA-002 One Clear Primary Action)。選択・確約・予約開始は SCR-005 で定義しない。
- 理解・確認・評価より前に、選択・入力・確約を求めない (CTA-004 Progressive Commitment)。
- 行動の対象と結果を実行前に理解可能にする (CTA-001 Action Clarity)。
- CTA の意味・状態・実行可能性を視覚だけに依存させない (CTA-009 Accessible Activation)。
- Navigation Action を自動的に主要 CTA として扱わない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §8 Boundary between CTA and Navigation)。
- 情報確認から Room / Stay Plan 選択へ進む具体的な行動・条件が未定義の場合、主要 CTA を確定しない (SDP-010 Incremental Definition)。

具体的な CTA 文言・数・優先順位・配置・色・Component は決定しない (§13 Does Not Decide)。

## 10. State and Feedback Requirements

対象状態は [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-005 に存在する Evaluating, Error / Interrupted のみとする。[Navigation](../service-design/navigation.md) §6 Navigation State Model を上流参照する。`Error / Interrupted` は上流 Navigation State の複合名として扱い、`Error` と `Interrupted` という別々の新規状態へ再定義しない。

- **Evaluating** — 施設・関連情報を比較・確認・評価している状態と、対象・条件・現在地を理解できること (SDP-005 State Visibility, NVP-001 Current Location Visibility)。
- **Error / Interrupted** — エラー・中断の発生と、原因・回復可能な行動・戻り先を理解できること (SDP-006 Recoverability, CTP-007 Actionable Error and Recovery)。
- 情報の状態・不確実性・変動可能性を確定情報として示さないこと (CTP-006 Explicit State and Uncertainty)。
- 状態変化を色・位置・アニメーションだけで伝えないこと (SDP-007, CTP-008)。
- `Exploring`・`Committing`・`Completed` 等を、SCR-005 の確定状態として独断で追加しないこと ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-005 は Evaluating, Error / Interrupted のみを定義)。

具体的なエラー・中断の業務状態や挙動は決定しない (§13 Does Not Decide)。

## 11. Accessibility Requirements

SDP-007 Accessibility by Default / NVP-008 Accessible Navigation / CTP-008 Accessible and Scannable Content / CTA-009 Accessible Activation の範囲で記述する。

- キーボード・支援技術・異なる画面サイズを例外扱いしない (SDP-007, NVP-008)。
- 施設情報・関連情報の構造・見出し・関係を支援技術で理解可能にする (CTP-008)。
- Navigation と CTA の意味・状態を視覚だけで伝えない (NVP-008, CTA-009)。
- エラー・中断時に問題と回復方法を理解可能にする (CTP-007)。
- 読む順序・情報の関係を画面サイズによって失わせない (CTP-008)。
- モバイルでも施設情報・関連情報の確認・評価・回復を可能にする (SDP-007)。

具体的な規格・達成レベル・HTML 属性・フォーカス実装・Component 仕様は決定しない (§13 Does Not Decide)。

## 12. Constraints

- 上流成果物 (SD-001〜SD-007) の定義を再定義・変更しない ([README.md](README.md) §9)。
- 作成単位は SCR-005 単独に限定し、Supporting IA Objects から業務モデル・表示項目を、SCR-004・SCR-006 から内部要件を取り込まない (§2, §5)。
- Price・Availability を SCR-005 の IA Objects・要件へ追加しない (§5)。
- 未定義事項を Fact または Decision として扱わず、Open Issue として保持する (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。
- 確定可能な範囲からのみ記述し、未決事項へ依存する要件を確定しない (SDP-010 Incremental Definition)。
- サービス全体の整合性と一貫した概念・用語を優先する (SDP-004 Consistent Mental Model, SDP-009 Service-wide Coherence)。

## 13. Does Not Decide

本文書だけでは以下を確定しない。

- 詳細レイアウト・情報構成・遷移 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-005 Does Not Decide)、ワイヤーフレーム。
- 施設情報の具体的な表示項目・属性一覧・表示順・情報密度。
- 写真・設備・アクセス情報等の具体的な表示方式。
- タブ・アンカー・アコーディオン・ギャラリー等の UI。
- Room / Stay Plan の表示単位・選択方法・比較方法。
- Room / Stay Plan / Price / Availability の正式な業務モデル、Price・Availability の表示や状態。
- Review の提供元・評価対象・信頼性・表示基準、Policy の正式分類・表示基準、Content の分類・編集方針・優先順位。
- SCR-004 から受け取るデータ、SCR-006 へ渡すデータ。
- SCR-005 と SCR-006 の分割・統合・責務境界の正式確定、情報確認から Room / Stay Plan 選択へ進む具体的な条件。
- エラー・中断の具体的な業務状態、API・DB・キャッシュ・データモデル。
- URL・route・クエリパラメータ・サイトマップ・画面遷移、CTA 文言・数・配置・色・Component。
- Screen Requirement ID 体系・ファイル命名規則。

## 14. Upstream References

上流成果物は [README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。定義を本文書で変更しない。SCR-005 へ直接適用できる ID のみを参照する。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — SDP-001 User Task Clarity / SDP-002 Progressive Commitment / SDP-003 Transparent Conditions / SDP-004 Consistent Mental Model / SDP-005 State Visibility / SDP-006 Recoverability / SDP-007 Accessibility by Default / SDP-008 Evidence over Assumption / SDP-009 Service-wide Coherence / SDP-010 Incremental Definition。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — Primary: IA-OBJ-003 Accommodation。Supporting: IA-OBJ-001 Destination / IA-OBJ-004 Room / IA-OBJ-005 Stay Plan / IA-OBJ-009 Review / IA-OBJ-008 Policy / IA-OBJ-012 Content。
- **SD-003 [Navigation](../service-design/navigation.md)** — NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation、NVP-001 Current Location Visibility / NVP-002 Predictable Destination / NVP-003 Preserved Context / NVP-006 Task over Organization / NVP-007 Progressive Disclosure / NVP-008 Accessible Navigation、Navigation State Model (Evaluating, Error / Interrupted)。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Categories: Identification / Decision Support / Conditions and Policies / Editorial and Support、CTP-001 Purpose Before Detail / CTP-002 Plain and Direct Language / CTP-003 Conditions Near Decisions / CTP-004 Evidence-backed Claims / CTP-005 Consistent Terminology / CTP-006 Explicit State and Uncertainty / CTP-007 Actionable Error and Recovery / CTP-008 Accessible and Scannable Content / CTP-009 Context-preserving References / CTP-010 Separate Fact, Decision, and Promotion。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA-001 Action Clarity / CTA-002 One Clear Primary Action / CTA-004 Progressive Commitment / CTA-009 Accessible Activation、§7 Relationship with Screen Matrix の SCR-005 行、§8 Boundary between CTA and Navigation。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — SCR-005 Accommodation Detail の責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements / UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens / UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 15. Downstream Impact

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 本 Screen Requirement の下流に位置する。既存 Design System (例: ReviewStars・Card 等) を参照して実現可能性や未整備箇所を確認できるが、既存 Component を上流要求へ昇格させない。具体的な Component・レイアウト・トークン・表示項目を指定しない。既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。
- **Implementation** — Repository の管理対象外。本文書だけで実装仕様を確定しない。SCR-005 を実装 1 画面・URL・route と同一視しない (UXDR-TRAVEL-002)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。各 Open Issue が影響する要件節を可能な範囲で示す。

- **Accommodation の正式な属性一覧** — §5 Information Responsibilities, §6 Functional Requirements。
- **施設情報の表示範囲・表示単位・表示順** — §6, §7 Content Requirements。
- **Destination 情報を施設評価に用いる範囲** — §5, §8 Navigation Requirements。
- **Room と Accommodation の正式な業務関係** — §5, §6。
- **Stay Plan と Accommodation の正式な業務関係** — §5, §6。
- **Room / Stay Plan を SCR-005 でどこまで確認し、SCR-006 でどこから選択するか** — §2, §6, §9 CTA Requirements。
- **SCR-005 と SCR-006 の責務境界および分割・統合** — §2, §13。
- **Review の提供元・評価対象・信頼性・表示基準** — §5, §7。
- **Policy の分類・適用対象・表示基準** — §5, §7。
- **Content の分類・編集方針・施設情報との関係** — §5, §7。
- **SCR-004 から引き継ぐ情報と文脈** — §2, §6。
- **SCR-006 へ引き渡す情報と文脈** — §2, §6, §9。
- **情報確認と Room / Stay Plan 選択の優先関係** — §9。
- **エラー・中断の種別と回復方法** — §10 State and Feedback Requirements, §11 Accessibility Requirements。
- **Utility Navigation の対象範囲** — §8。
- **URL・route・画面遷移** — §6, §13。
- **モバイル・レスポンシブ時の情報構成** — §8, §11。
- **Screen Requirement ID 体系** — 文書全体 ([README.md](README.md) §7)。
- **ファイル命名規則** — 本文書のファイル名 `accommodation-detail.md` は暫定 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — §17 Acceptance Criteria。
- **Design System への反映確認方法** — §15 Downstream Impact ([README.md](README.md) §17)。

## 17. Acceptance Criteria

未定義の UI・業務仕様を確定しない範囲で記述する。最終確定主体は Open Issue として維持する (§16)。

- 文書が [README.md](README.md) §6 Common Document Structure を満たしている。
- Related Screen Matrix Candidate が SCR-005 として追跡可能であり、SCR-005 のみである。
- [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-005 の Responsibility・Purpose・Primary User Tasks・Primary IA Objects・Supporting IA Objects・Navigation Types・Content Categories・Navigation States と一致している。
- Accommodation を Primary、Destination・Room・Stay Plan・Review・Policy・Content を Supporting として扱い、主従を逆転していない (§5)。
- Supporting IA Objects から具体的な表示項目や業務仕様を導出していない (§5)。
- Price・Availability を SCR-005 の IA Objects・要件へ追加していない (§5)。
- Navigation と CTA の要件が別節・別責務として記述され、NAV-002・NAV-003・NAV-004・NAV-006 を混同していない (§8, §9)。
- 情報確認と Room / Stay Plan 選択を区別し、選択・確約・在庫・料金・予約開始を定義していない (§6, §9)。
- 状態が Evaluating, Error / Interrupted のみであり、`Error / Interrupted` を複合状態名として扱い、未定義状態を独断で追加していない (§10)。
- SCR-004・SCR-006 の内部要件を取り込んでいない (§2)。
- 詳細レイアウト・情報構成・業務モデル・URL・route・UI・Component・CTA 文言を確定していない (§13, §15)。
- 未定義の要求が Open Issue として追跡でき、上流成果物の ID・正式名称を追跡できる (§14, §16)。
- 下流 Design System との関係が Downstream Impact へ分離されている (§15)。
- 文書 Status が Draft である。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial draft of Travel Accommodation Detail Screen Requirement (SCR-005) | Draft |
