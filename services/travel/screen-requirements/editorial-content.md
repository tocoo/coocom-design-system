# Travel Editorial Content Screen Requirement

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補 SCR-014 Editorial Content に対応する個別 Screen Requirement の初版 Draft
- Position in Repository: `services/travel/screen-requirements/editorial-content.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)、作成順序評価は [creation-plan.md](creation-plan.md)、先行する個別要件例は [service-entry.md](service-entry.md) / [help-and-support.md](help-and-support.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Design System / Implementation) との関係は §15 Downstream Impact を参照。

本文書はファイル名 `editorial-content.md` で作成する。これは記述的な暫定ファイル名であり、正式なファイル命名規則を確定するものではない (§16 Open Issues)。文書は Title およびファイル名で識別し、`SCR-014` を Screen Requirement 文書 ID として再定義しない。

## 1. Purpose

- 画面候補 SCR-014 Editorial Content ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) の責務を、Repository 内の既存上流成果物 (SD-001〜SD-007, Governance) から確認できる範囲で個別 Screen Requirement として記述する。
- 利用者が特集・ガイド・案内等の Content を読み、発見・理解するための要件を定義する。
- 未定義の Content 分類・編集方針・掲載対象・販促との関係等は補完せず、Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- SCR-014 の責務を具体的な特集・記事・コンテンツ分類・編集計画・SEO 施策・販促施策へ具体化しない。SCR-014 を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

## 2. Related Screen Matrix Candidates

- **SCR-014 Editorial Content** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) — 唯一の対応画面候補。
- 本文書は SCR-014 に既に定義された責務と利用者タスクのみを扱う。
- 特集・ガイド・案内等が同一画面になるか複数画面へ分かれるか、Content の種類やテンプレート数は確定しない (§16 Open Issues)。
- Destination・Accommodation は Supporting IA Objects として参照し、それらの詳細要件を取り込まない。SCR-002 Destination Discovery や SCR-005 Accommodation Detail との統合・境界を独断で決めない (§16 Open Issues)。
- 本文書の作成単位 (SCR-014 単独) は、未決事項を保持したまま作成可能な範囲を文書化するための暫定的な作成単位であり、将来の分割・統合判断により文書構成が変更され得る。本文書の作成順は、探索・補助候補群の正式な作成順を確定するものではない ([creation-plan.md](creation-plan.md) §10)。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は SCR-014 Editorial Content を画面候補 (Status: Draft) として管理する。
- レイヤー入口 [README.md](README.md)、作成順序評価 [creation-plan.md](creation-plan.md)、先行する個別要件 [service-entry.md](service-entry.md) (SCR-001) と [help-and-support.md](help-and-support.md) (SCR-013) が存在する。
- [creation-plan.md](creation-plan.md) は SCR-014 を「その次に作成可能な候補群」(予約チェーンから独立) と評価する (§10)。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は SCR-014 の要件を、上流成果物から確認できる範囲で記述する。
- 作成単位を SCR-014 単独とする (暫定。§2)。
- Content を Primary IA Object、Destination・Accommodation を Supporting IA Objects として扱い、主従を逆転しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-014)。
- 未定義の事業・業務・機能・画面仕様は推測で補完せず Open Issue として保持する (UXDR-TRAVEL-001)。
- Navigation と CTA を別責務として記述する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities と一致)。
- ファイル名 `editorial-content.md` は暫定であり、正式命名規則を確定しない。

### Hypotheses

- なし。

### Open Issues

- Content の正式分類・編集方針。
- SCR-002 Destination Discovery / SCR-005 Accommodation Detail との境界。
- Screen Requirement ID 体系・ファイル命名規則。
- (詳細は §16 に集約)

## 4. User Tasks

[Screen Matrix](../service-design/screen-matrix.md) §5 SCR-014 の Primary User Tasks を上流参照する (再定義しない)。

- 特集・ガイド等の情報を読み、発見・理解する。

上位基準として SDP-001 User Task Clarity (利用者が現在何を行い、次に何を行えるかを理解できる) を適用する。どの特集・ガイド・案内を対象とするかは確定しない (§16 Open Issues)。

## 5. Information Responsibilities

[Information Architecture](../service-design/information-architecture.md) (SD-002) を上流参照する。IA オブジェクトの定義・追加・変更は行わない。Screen Matrix §5 SCR-014 の Primary / Supporting の区別を保つ。

### Primary IA Objects

- **IA-OBJ-012 Content** — 宿泊予約の判断や利用を支援する説明・案内的情報を、発見・理解の文脈で扱う。正式な分類は確定しない (IA-OBJ-012 Open Issue)。

### Supporting IA Objects

- **IA-OBJ-001 Destination** — Content が評価を支援する対象として補助的に参照する。階層構造・提示範囲を取り込まない (IA-OBJ-001 Open Issue)。
- **IA-OBJ-003 Accommodation** — Content が評価を支援する対象として補助的に参照する。施設詳細要件 (SCR-005) を取り込まない。

Supporting IA Objects (Destination / Accommodation) から、検索・施設詳細の機能を取り込まない。Primary と Supporting の主従を逆転しない ([../service-design/information-architecture.md](../service-design/information-architecture.md) §5 IA-OBJ-012 Relationships「Content は Destination / Accommodation の評価を支援する」)。

## 6. Functional Requirements

上流成果物から確認できる能力・責務のみを記述する。業務仕様が未定義の事項は要件化せず Open Issue とする ([README.md](README.md) §6)。

- 利用者が、特集・ガイド・案内等の Content を発見できること (SDP-001, NAV-001 Global Navigation)。
- Content の対象・目的・性質を理解できること (SDP-001, CTP-010 Separate Fact, Decision, and Promotion)。
- 利用者が Content を読み、関連情報を理解できること (SDP-001, NVP-007 Progressive Disclosure)。
- Content と関連する Destination または Accommodation を、概念関係の範囲で認識できること (IA-OBJ-012 Relationships)。
- 関連する Destination・Accommodation へ移動し得ること (NAV-003 Contextual Navigation, NVP-003 Preserved Context)。
- 編集情報と、事実・条件・販促表現を混同しないこと (CTP-010, SDP-003 Transparent Conditions)。
- 情報の根拠または不確実性を確認可能にすること (CTP-004 Evidence-backed Claims, CTP-006 Explicit State and Uncertainty)。
- 利用不能・未確定・条件付きの関連情報を確定事項として扱わないこと (CTP-006, SDP-008 Evidence over Assumption)。

以下は決定しない (Open Issue として §16 で扱う)。

- 具体的な Content 分類。
- 掲載する特集・ガイド・案内。
- Destination・Accommodation との紐付け条件。
- レコメンド条件。
- 編集・更新・承認フロー。
- 具体的な遷移先。

## 7. Content Requirements

[Content Principles](../service-design/content-principles.md) (SD-004) の Content Category と原則を上流参照する。SCR-014 の Content Categories は Editorial and Support / Identification ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-014)。

- **Editorial and Support** — 発見・理解を支援する情報を提供する (CTP-004 Evidence-backed Claims, CTP-008 Accessible and Scannable Content, CTP-009 Context-preserving References, CTP-010 Separate Fact, Decision, and Promotion)。
- **Identification** — Content の対象・目的・情報の性質を識別可能にする (CTP-002 Plain and Direct Language, CTP-005 Consistent Terminology)。
- Editorial and Support と Identification の責務を区別する。
- 事実・判断・仮説・販促表現を混同しない (CTP-010)。
- 根拠のない優位性・限定性・人気・緊急性を表現しない (CTP-004)。
- 不確実性・未確定事項・更新状態を確定情報として表現しない (CTP-006 Explicit State and Uncertainty)。
- 関連 Destination・Accommodation への参照時に文脈を失わせない (CTP-009 Context-preserving References)。
- 見出し・構造・文章を読み取りやすくする (CTP-008)。
- 色・画像・位置だけに意味を依存させない (CTP-008)。
- 同じ概念に一貫した用語を用いる (CTP-005 Consistent Terminology, NVP-005 Consistent Meaning)。

具体的なコピー・記事本文・ブランドトーン・SEO 文言・販促表現は決定しない (§13 Does Not Decide)。

## 8. Navigation Requirements

[Navigation](../service-design/navigation.md) (SD-003) を上流参照する。SCR-014 の Navigation Types は NAV-001 / NAV-002 / NAV-003 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-014)。3 分類を責務として区別して記述する。

- **NAV-001 Global Navigation** — 主要領域から Editorial Content へ到達し得るようにする。対象領域・項目は確定しない (NAV-001 Does Not Decide, §16 Open Issues)。
- **NAV-002 Local Navigation** — Content 領域内部の関連情報へ移動し得るようにする。分類単位は確定しない (NAV-002 Does Not Decide)。
- **NAV-003 Contextual Navigation** — Content と関連する Destination・Accommodation へ移動し得るようにする。表示条件は確定しない (NAV-003 Does Not Decide)。
- 現在閲覧している Content とその位置を理解可能にする (NVP-001 Current Location Visibility)。
- 移動先の対象と目的を予測可能にする (NVP-002 Predictable Destination)。
- 移動時に Content の文脈を不必要に失わせない (NVP-003 Preserved Context)。
- 現在の判断に不要な選択肢を過剰に提示しない (NVP-007 Progressive Disclosure)。
- 内部組織や編集体制ではなく、利用者が理解できる情報単位で構成する (NVP-006 Task over Organization)。
- Navigation と CTA を同一責務として扱わない (UXDR-TRAVEL-003, §9)。

具体的なメニュー・カテゴリ・パンくず・リンク・ラベル・配置・表示条件は確定しない (§13 Does Not Decide)。

## 9. CTA Requirements

[CTA Principles](../service-design/cta-principles.md) (SD-005) を上流参照する。SCR-014 に関する記述は [../service-design/cta-principles.md](../service-design/cta-principles.md) §7 Relationship with Screen Matrix の SCR-014 行 (CTA Consideration「編集情報と予約・販促 CTA の性質を区別する」)。Navigation と CTA は別責務とする (UXDR-TRAVEL-003)。

- 編集情報と予約・販促 CTA の性質を区別する (CTA-010 No Unsupported Pressure, CTP-010 Separate Fact, Decision, and Promotion)。
- 情報間の移動を自動的に CTA として扱わない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §8 Boundary between CTA and Navigation)。
- 行動の対象と結果を実行前に理解可能にする (CTA-001 Action Clarity)。
- 根拠のない緊急性・限定性・人気・損失回避を用いて行動を促さない (CTA-010 No Unsupported Pressure)。
- 具体的な行動や遷移先が未定義の場合、主要 CTA を確定しない (SDP-010 Incremental Definition)。
- CTA の意味と実行可能性を視覚だけに依存させない (CTA-009 Accessible Activation)。

具体的な CTA 文言・数・優先順位・配置・色・Component は決定しない (§13 Does Not Decide)。

## 10. State and Feedback Requirements

対象状態は [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-014 に存在する Entry, Exploring, Evaluating のみとする。[Navigation](../service-design/navigation.md) §6 Navigation State Model を上流参照する。

- **Entry** — Editorial Content 領域または対象 Content へ到達したことを理解できること。
- **Exploring** — 関連する Content・Destination・Accommodation を探索している状態を理解できること (NVP-003 Preserved Context)。
- **Evaluating** — Content と関連情報を読み、判断材料として評価している状態を理解できること。
- 状態または現在地を視覚表現だけで伝えないこと (SDP-007, CTP-008)。
- 状態間の文脈を不必要に失わせないこと (NVP-003)。
- `Error / Interrupted`・`Committing`・`Completed` 等を、SCR-014 の確定状態として独断で追加しないこと ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-014 は Entry, Exploring, Evaluating のみを定義)。

## 11. Accessibility Requirements

SDP-007 Accessibility by Default / NVP-008 Accessible Navigation / CTP-008 Accessible and Scannable Content / CTA-009 Accessible Activation の範囲で記述する。

- キーボード・支援技術・異なる画面サイズを例外扱いしない (SDP-007, NVP-008)。
- Content の構造・見出し・関連性を支援技術で理解可能にする (CTP-008)。
- Navigation および CTA の意味を視覚だけで伝えない (NVP-008, CTA-009)。
- 画像や装飾がなくても情報の目的・関係を理解可能にする (CTP-008)。
- 異なる画面サイズでも読む順序と意味を失わせない (CTP-008)。
- モバイルでも Content の発見・閲覧・関連情報への移動を可能にする (SDP-007)。

具体的な規格・達成レベル・HTML 属性・画像仕様・Component 実装は決定しない (§13 Does Not Decide)。

## 12. Constraints

- 上流成果物 (SD-001〜SD-007) の定義を再定義・変更しない ([README.md](README.md) §9)。
- 作成単位は SCR-014 単独に限定し、Supporting IA Objects (Destination / Accommodation) から検索・施設詳細の機能を取り込まない (§2, §5)。
- 未定義事項を Fact または Decision として扱わず、Open Issue として保持する (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。
- 確定可能な範囲からのみ記述し、未決事項へ依存する要件を確定しない (SDP-010 Incremental Definition)。
- サービス全体の整合性と一貫した概念・用語を優先する (SDP-004 Consistent Mental Model, SDP-009 Service-wide Coherence)。

## 13. Does Not Decide

本文書だけでは以下を確定しない。

- 具体的なコンテンツ分類・編集方針・UI ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-014 Does Not Decide)。
- 掲載する特集・ガイド・記事・案内の種類や件数。
- 編集テーマ・掲載計画・更新頻度・運用体制・作成者・承認者・情報源。
- Destination・Accommodation との具体的な紐付け規則、レコメンド・パーソナライズ。
- SEO キーワード・構造化データ・メタ情報、販促キャンペーン・広告・CV 設計。
- 具体的なコピー・見出し・ブランドトーン、画像・動画・アイコン制作仕様。
- 特集・ガイド・案内の画面分割/統合、SCR-002・SCR-005 との境界。
- URL・route・サイトマップ・画面遷移、CTA 文言・配置・色・数・Component。
- Screen Requirement ID 体系・ファイル命名規則。

## 14. Upstream References

上流成果物は [README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。定義を本文書で変更しない。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — SDP-001 User Task Clarity / SDP-003 Transparent Conditions / SDP-004 Consistent Mental Model / SDP-007 Accessibility by Default / SDP-008 Evidence over Assumption / SDP-009 Service-wide Coherence / SDP-010 Incremental Definition。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — Primary: IA-OBJ-012 Content。Supporting: IA-OBJ-001 Destination / IA-OBJ-003 Accommodation。
- **SD-003 [Navigation](../service-design/navigation.md)** — NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation、NVP-001 Current Location Visibility / NVP-002 Predictable Destination / NVP-003 Preserved Context / NVP-005 Consistent Meaning / NVP-006 Task over Organization / NVP-007 Progressive Disclosure / NVP-008 Accessible Navigation、Navigation State Model (Entry, Exploring, Evaluating)。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Categories: Editorial and Support / Identification、CTP-002 Plain and Direct Language / CTP-004 Evidence-backed Claims / CTP-005 Consistent Terminology / CTP-006 Explicit State and Uncertainty / CTP-008 Accessible and Scannable Content / CTP-009 Context-preserving References / CTP-010 Separate Fact, Decision, and Promotion。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA-001 Action Clarity / CTA-009 Accessible Activation / CTA-010 No Unsupported Pressure、§7 Relationship with Screen Matrix の SCR-014 行、§8 Boundary between CTA and Navigation。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — SCR-014 Editorial Content の責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements / UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens / UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 15. Downstream Impact

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 本 Screen Requirement の下流に位置する。既存 Design System を参照して実現可能性や未整備箇所を確認できるが、既存の Card・画像・リンク等の Component を前提に上流要件を変形しない。具体的な Component・レイアウト・画像比率・トークンを指定しない。既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。
- **Implementation** — Repository の管理対象外。本文書だけで実装仕様を確定しない。SCR-014 を実装 1 画面・URL・route と同一視しない (UXDR-TRAVEL-002)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。各 Open Issue が影響する要件節を可能な範囲で示す。

- **Content の正式分類** — §5 Information Responsibilities, §7 Content Requirements。
- **Editorial Content の対象範囲** — §4 User Tasks, §6 Functional Requirements。
- **特集・ガイド・案内等の区別** — §6, §7。
- **編集方針・コンテンツ戦略との関係** — §7。
- **情報源・根拠・更新日の管理方法** — §6, §7 (CTP-004 / CTP-006)。
- **作成・編集・承認・更新の責任主体** — §6。
- **Destination との関連付け** — §5, §8 Navigation Requirements。
- **Accommodation との関連付け** — §5, §8。
- **SCR-002 Destination Discovery との境界** — §2, §5, §8。
- **SCR-005 Accommodation Detail との境界** — §2, §5, §8。
- **編集情報と販促施策の具体的な境界** — §7, §9 CTA Requirements。
- **Navigation の分類単位・表示条件** — §8。
- **CTA の具体的な対象** — §9。
- **URL・route・サイトマップ・画面遷移** — §6, §13。
- **モバイル時の具体的な Content 構造** — §8, §11 Accessibility Requirements。
- **Screen Requirement ID 体系** — 文書全体 ([README.md](README.md) §7)。
- **ファイル命名規則** — 本文書のファイル名 `editorial-content.md` は暫定 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — §17 Acceptance Criteria。
- **Design System への反映確認方法** — §15 Downstream Impact ([README.md](README.md) §17)。

## 17. Acceptance Criteria

未定義の UI・業務仕様を確定しない範囲で記述する。最終確定主体は Open Issue として維持する (§16)。

- 文書が [README.md](README.md) §6 Common Document Structure を満たしている。
- Related Screen Matrix Candidate が SCR-014 として追跡可能であり、SCR-014 のみである。
- [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-014 の Responsibility・Primary User Tasks・Primary IA Objects・Supporting IA Objects・Navigation Types・Content Categories・Navigation States と一致している。
- Content を Primary、Destination・Accommodation を Supporting として扱い、主従を逆転していない (§5)。
- Supporting IA Objects から検索・施設詳細機能を取り込んでいない (§5)。
- Editorial and Support と Identification を区別している (§7)。
- 編集情報・事実・条件・販促表現を混同していない (§7, §9)。
- Navigation と CTA の要件が別節・別責務として記述されている (§8, §9)。
- 状態が Entry, Exploring, Evaluating のみであり、未定義状態を独断で追加していない (§10)。
- Content 分類・編集方針・掲載内容を確定していない (§13)。
- SCR-002・SCR-005 との境界を確定していない (§2, §16)。
- URL・route・UI・Component・SEO・販促施策を確定していない (§13, §15)。
- 未定義の要求が Open Issue として追跡できる (§16)。
- 上流成果物の ID・正式名称を追跡できる (§14)。
- 下流 Design System との関係が Downstream Impact へ分離されている (§15)。
- 文書 Status が Draft である。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial draft of Travel Editorial Content Screen Requirement (SCR-014) | Draft |
