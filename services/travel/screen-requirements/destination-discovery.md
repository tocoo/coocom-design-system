# Travel Destination Discovery Screen Requirement

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補 SCR-002 Destination Discovery に対応する個別 Screen Requirement の初版 Draft
- Position in Repository: `services/travel/screen-requirements/destination-discovery.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)、作成順序評価は [creation-plan.md](creation-plan.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。同一レイヤーの関係候補との関係は §2、下流成果物 (Design System / Implementation) との関係は §15 Downstream Impact を参照。

本文書はファイル名 `destination-discovery.md` で作成する。これは記述的な暫定ファイル名であり、正式なファイル命名規則を確定するものではない (§16 Open Issues)。文書は Title およびファイル名で識別し、`SCR-002` を Screen Requirement 文書 ID として再定義しない。

## 1. Purpose

- 画面候補 SCR-002 Destination Discovery ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) の責務を、Repository 内の既存上流成果物 (SD-001〜SD-007, Governance) から確認できる範囲で個別 Screen Requirement として記述する。
- 利用者が目的地・エリア・関連 Content を発見し、候補探索へ進むための要件を定義する。
- 未定義の Destination の正式な階層・分類、Content の正式分類、目的地階層 UI・一覧構成・遷移、発見と販促の具体的境界等は補完せず、Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- SCR-002 の責務を具体的な目的地階層 UI・一覧構成・遷移へ具体化しない。SCR-002 を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

## 2. Related Screen Matrix Candidates

- **SCR-002 Destination Discovery** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) — 唯一の対応画面候補。責務は「目的地・エリア・関連 Content を発見する」。
- 本文書は SCR-002 に既に定義された責務と利用者タスクのみを扱う。目的地の階層 UI・一覧構成・遷移は確定しない (§13 Does Not Decide)。
- SCR-001 Service Entry・SCR-003 Accommodation Search・SCR-004 Search Results・SCR-014 Editorial Content は関係する候補として参照できるが、SCR-002 の Related Screen Matrix Candidate へ追加せず、それらの内部要件も取り込まない。
- 本文書の作成単位 (SCR-002 単独) は、未決事項を保持したまま作成可能な範囲を文書化するための暫定的な作成単位であり、SCR-001 との責務境界・SCR-014 との Content 責務境界・分割・統合は確定しない (§16 Open Issues)。本文書の作成順は、探索・補助候補群の正式な作成順を確定するものではない ([creation-plan.md](creation-plan.md) §10)。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は SCR-002 Destination Discovery を画面候補 (Status: Draft) として管理する。
- レイヤー入口 [README.md](README.md)、作成順序評価 [creation-plan.md](creation-plan.md)、先行する個別要件 ([service-entry.md](service-entry.md) SCR-001 / [accommodation-search.md](accommodation-search.md) SCR-003 / [search-results.md](search-results.md) SCR-004 / [accommodation-detail.md](accommodation-detail.md) SCR-005 / [help-and-support.md](help-and-support.md) SCR-013 / [editorial-content.md](editorial-content.md) SCR-014) が存在する。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は SCR-002 の要件を、上流成果物から確認できる範囲で記述する。
- 作成単位を SCR-002 単独とする (暫定。§2)。
- Destination・Content を Primary IA Objects、Accommodation を Supporting IA Object として扱い、主従を逆転しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-002)。
- 発見・探索と販促誘導を区別し、編集情報・事実・推奨・販促表現を混同しない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §7 SCR-002 行, [../service-design/content-principles.md](../service-design/content-principles.md) CTP-010)。
- Destination・Content の「含み得る概念」の例示を、正式な分類・階層・掲載枠として確定しない (IA-OBJ-001 / IA-OBJ-012 Open Issue)。
- 未定義の分類・階層・業務仕様は推測で補完せず Open Issue として保持する (UXDR-TRAVEL-001)。
- Navigation と CTA を別責務として記述する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities と一致)。
- ファイル名 `destination-discovery.md` は暫定であり、正式命名規則を確定しない。

### Hypotheses

- なし。

### Open Issues

- Destination の正式な分類・階層構造。
- Content の正式分類・責務。
- SCR-001 / SCR-014 との責務境界。
- (詳細は §16 に集約)

## 4. User Tasks

[Screen Matrix](../service-design/screen-matrix.md) §5 SCR-002 の Primary User Tasks を上流参照する (再定義しない)。

- 目的地やエリアを発見し、候補探索へ進む。

上位基準として SDP-001 User Task Clarity (利用者が現在何を行い、次に何を行えるかを理解できる) を適用する。どの目的地・エリア・Content を対象とするかは確定しない (§16 Open Issues)。

## 5. Information Responsibilities

[Information Architecture](../service-design/information-architecture.md) (SD-002) を上流参照する。IA オブジェクトの定義・追加・変更は行わない。Screen Matrix §5 SCR-002 の Primary / Supporting の区別を保つ。

### Primary IA Objects

- **IA-OBJ-001 Destination** — 「どこに泊まるか」を検討・指定するための地理/目的地の観点を、発見の対象として扱う。都道府県・市区町村・エリア・駅・観光地・ランドマークは IA-OBJ-001 の「含み得る概念」の例示であり、正式な分類・固定階層・親子関係・検索単位・Navigation 単位として確定しない (IA-OBJ-001 の階層構造は Open Issue)。
- **IA-OBJ-012 Content** — 発見・理解を支援する説明・案内的情報を、発見の対象として扱う。特集・ガイド・お知らせ・FAQ・説明コンテンツ・サポート情報は IA-OBJ-012 の「含み得る概念」の例示であり、正式な Content 分類・掲載枠・画面種別・優先順位として確定しない (IA-OBJ-012 の分類・責務は Open Issue)。

### Supporting IA Objects

- **IA-OBJ-003 Accommodation** — Destination との関連を辿るための補助として参照する (IA-OBJ-003 Relationships「Accommodation は Destination に所在する」)。Accommodation の正式な属性一覧・表示項目・掲載単位・並び順・評価基準を SCR-002 で定義しない。

Supporting IA Object (Accommodation) から、検索結果・施設一覧・施設詳細・料金・在庫・Review・Policy 等の機能や表示要件を取り込まない。Primary と Supporting の主従を逆転しない。

## 6. Functional Requirements

上流成果物から確認できる能力・責務のみを記述する。業務仕様が未定義の事項は要件化せず Open Issue とする ([README.md](README.md) §6)。

- 利用者が目的地・エリアを発見できること (IA-OBJ-001, SDP-001)。
- 利用者が発見に関連する Content を発見できること (IA-OBJ-012, SDP-001)。
- 発見した目的地・エリア・Content から、候補探索へ進み得ること (IA-OBJ-001 Relationships「Search Criteria が Destination を参照する / Accommodation は Destination に所在する」)。
- Destination と関連する Content・Accommodation を、概念関係の範囲で認識できること (IA-OBJ-001 / IA-OBJ-012 / IA-OBJ-003 Relationships)。
- 現在の探索対象と、関連情報への移動先を理解できること (NVP-001 Current Location Visibility, NVP-002 Predictable Destination)。
- 発見・探索の情報と、販促・推奨表現を区別できること (CTP-010 Separate Fact, Decision, and Promotion, SDP-008 Evidence over Assumption)。
- 根拠のない人気・ランキング・おすすめ・限定・希少性・緊急性を確定情報として扱わないこと (CTP-004 Evidence-backed Claims, CTA-010 No Unsupported Pressure)。

以下は決定しない (Open Issue として §16 で扱う)。

- Destination の正式な分類・階層・識別/表示単位。
- Content の正式分類・掲載枠・優先順位。
- 目的地階層 UI・一覧構成・表示項目・表示順・情報密度。
- Destination と Content・Accommodation の具体的な関連付け規則。
- 人気順・おすすめ順・ランキング・レコメンド。
- SCR-003・SCR-004 へ渡すデータ、候補探索への具体的な遷移先。

## 7. Content Requirements

[Content Principles](../service-design/content-principles.md) (SD-004) の Content Category と原則を上流参照する。SCR-002 の Content Categories は Identification / Editorial and Support ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-002)。

- **Identification** — 目的地・エリア・Content の対象を識別可能にする (CTP-002 Plain and Direct Language, CTP-005 Consistent Terminology)。
- **Editorial and Support** — 発見・理解を支援する編集・案内的情報を提供する (CTP-004 Evidence-backed Claims, CTP-008 Accessible and Scannable Content, CTP-009 Context-preserving References, CTP-010 Separate Fact, Decision, and Promotion)。
- 事実・サービス上の推奨・販促表現を区別し、混同しない (CTP-010 Separate Fact, Decision, and Promotion)。
- 根拠のない優位性・人気・ランキング・おすすめ・限定・希少性を表現しない (CTP-004 Evidence-backed Claims)。
- 関連する Destination・Content・Accommodation への参照時に、対象と元の文脈を失わせない (CTP-009 Context-preserving References)。
- 見出し・構造・順序で理解しやすくし、色・画像・位置だけに意味を依存させない (CTP-008 Accessible and Scannable Content)。
- 同じ概念に一貫した用語を用いる (CTP-005 Consistent Terminology, NVP-005 Consistent Meaning)。

具体的なコピー・見出し・特集名・ブランドトーン・SEO 文言・販促表現は決定しない (§13 Does Not Decide)。

## 8. Navigation Requirements

[Navigation](../service-design/navigation.md) (SD-003) を上流参照する。SCR-002 の Navigation Types は NAV-001 / NAV-002 / NAV-003 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-002)。3 分類を別責務として区別して記述し、単一のメニューや UI へ統合して定義しない。

- **NAV-001 Global Navigation** — 主要領域への一貫した入口と、サービス内の大きな位置関係の理解に関する責務。具体的なメニュー項目・ヘッダー構成・表示順・対象領域は決定しない (NAV-001 Does Not Decide, §16 Open Issues)。
- **NAV-002 Local Navigation** — 現在の Destination または Content 領域内の関連情報への移動に関する責務。タブ・アンカー・項目名・具体的な情報構成は決定しない (NAV-002 Does Not Decide)。
- **NAV-003 Contextual Navigation** — Destination・Content・Accommodation 間の実在する IA 関係を辿る責務。具体的なリンク配置・表示条件・遷移先は決定しない (NAV-003 Does Not Decide)。
- 移動先または結果を事前に予測可能にする (NVP-002 Predictable Destination)。
- 現在の探索対象・位置を理解可能にする (NVP-001 Current Location Visibility)。
- 移動時に探索の文脈を不必要に失わせない (NVP-003 Preserved Context)。
- 現在の判断に不要な選択肢を過剰に提示しない (NVP-007 Progressive Disclosure)。
- 内部組織やシステム都合ではなく利用者タスクを基準にする (NVP-006 Task over Organization)。
- Navigation と CTA を同一責務として扱わない (UXDR-TRAVEL-003, §9)。

具体的なメニュー・タブ・地図・リンク・ラベル・配置・表示条件・画面遷移は確定しない (§13 Does Not Decide)。

## 9. CTA Requirements

[CTA Principles](../service-design/cta-principles.md) (SD-005) を上流参照する。SCR-002 に関する記述は [../service-design/cta-principles.md](../service-design/cta-principles.md) §7 Relationship with Screen Matrix の SCR-002 行 (CTA Consideration「発見・探索と販促誘導を混同しない」)。Navigation と CTA は別責務とする (UXDR-TRAVEL-003)。SCR-002 へ直接適用できる原則のみを参照する。

- 目的地・エリア・関連 Content を発見する行動と、広告・キャンペーン・予約促進等の販促誘導を区別する (CTA-010 No Unsupported Pressure, CTP-010 Separate Fact, Decision, and Promotion)。
- 根拠のない人気・ランキング・おすすめ・限定・希少性・緊急性で行動を誘導しない (CTA-010 No Unsupported Pressure)。
- 行動の対象と結果を実行前に理解可能にする (CTA-001 Action Clarity)。
- Content を Primary IA Object とすることを、販促施策や広告枠の要件と解釈しない。
- Navigation Action を自動的に主要 CTA として扱わない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §8 Boundary between CTA and Navigation)。
- 具体的な行動や遷移先が未定義の場合、主要 CTA を確定しない (SDP-010 Incremental Definition)。
- CTA の意味・実行可能性を視覚だけに依存させない (CTA-009 Accessible Activation)。

具体的な CTA 文言・数・優先順位・配置・色・Component は決定しない (§13 Does Not Decide)。

## 10. State and Feedback Requirements

対象状態は [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-002 に存在する Exploring のみとする。[Navigation](../service-design/navigation.md) §6 Navigation State Model を上流参照する。

- **Exploring** — 目的地・エリア・関連 Content を探索している状態と、現在の探索対象・位置・関連情報を理解できること (NVP-001 Current Location Visibility, NVP-003 Preserved Context)。
- 探索中に現在の対象・文脈を不必要に失わせないこと (NVP-003 Preserved Context)。
- 状態や現在地を色・位置・アニメーションだけで伝えないこと (SDP-007, CTP-008)。
- `Entry`・`Evaluating`・`Committing`・`Completed`・`Error / Interrupted` 等を、SCR-002 の確定状態として独断で追加しないこと。エラー・中断が一般に起こり得ることを理由に上流にない状態を追加しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-002 は Exploring のみを定義)。

## 11. Accessibility Requirements

SDP-007 Accessibility by Default / NVP-008 Accessible Navigation / CTP-008 Accessible and Scannable Content / CTA-009 Accessible Activation の範囲で記述する。

- キーボード・支援技術・異なる画面サイズを例外扱いしない (SDP-007, NVP-008)。
- 目的地・エリア・Content の構造・見出し・関係を支援技術で理解可能にする (CTP-008)。
- Navigation と CTA の意味を視覚だけで伝えない (NVP-008, CTA-009)。
- 画像・地図等がなくても発見対象と関連性を理解可能にする (CTP-008)。
- 異なる画面サイズでも読む順序と意味を失わせない (CTP-008)。
- モバイルでも目的地・エリア・Content の発見と関連情報への移動を可能にする (SDP-007)。

具体的な規格・達成レベル・HTML 属性・地図/画像仕様・Component 実装は決定しない (§13 Does Not Decide)。

## 12. Constraints

- 上流成果物 (SD-001〜SD-007) の定義を再定義・変更しない ([README.md](README.md) §9)。
- 作成単位は SCR-002 単独に限定し、Supporting IA Object (Accommodation) から検索・施設詳細等の機能を、SCR-001・SCR-003・SCR-004・SCR-014 から内部要件を取り込まない (§2, §5)。
- Destination・Content の「含み得る概念」の例示を、正式な分類・階層・掲載枠として確定しない (§5, §6, §7)。
- 未定義事項を Fact または Decision として扱わず、Open Issue として保持する (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。
- 確定可能な範囲からのみ記述し、未決事項へ依存する要件を確定しない (SDP-010 Incremental Definition)。
- サービス全体の整合性と一貫した概念・用語を優先する (SDP-004 Consistent Mental Model, SDP-009 Service-wide Coherence)。

## 13. Does Not Decide

本文書だけでは以下を確定しない。

- 目的地の階層 UI・一覧構成・遷移 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-002 Does Not Decide)。
- Destination の正式な分類・階層・親子関係、都道府県・市区町村・エリア・駅・観光地・ランドマークの正式な包含関係。
- Content の正式分類・役割・優先順位、特集・ガイド・お知らせ・FAQ 等の正式な区分。
- 一覧・カード・地図・タブ・メニュー等の UI、一覧構成・表示項目・表示順・情報密度。
- 人気順・おすすめ順・ランキング・レコメンド、広告枠・キャンペーン枠・販促導線。
- SEO キーワード・構造化データ・メタ情報。
- Destination と Content・Accommodation の具体的な関連付け・掲載規則。
- SCR-001 との責務境界や分割・統合、SCR-003・SCR-004 へ渡すデータ、SCR-014 との Content 責務境界。
- Global Navigation の対象領域、エラー・中断専用状態や画面。
- API・DB・検索エンジン・データモデル、URL・route・クエリパラメータ・サイトマップ・画面遷移。
- CTA 文言・数・配置・色・Component。
- Screen Requirement ID 体系・ファイル命名規則。

## 14. Upstream References

上流成果物は [README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。定義を本文書で変更しない。SCR-002 へ直接適用できる ID のみを参照する。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — SDP-001 User Task Clarity / SDP-004 Consistent Mental Model / SDP-007 Accessibility by Default / SDP-008 Evidence over Assumption / SDP-009 Service-wide Coherence / SDP-010 Incremental Definition。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — Primary: IA-OBJ-001 Destination / IA-OBJ-012 Content。Supporting: IA-OBJ-003 Accommodation。
- **SD-003 [Navigation](../service-design/navigation.md)** — NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation、NVP-001 Current Location Visibility / NVP-002 Predictable Destination / NVP-003 Preserved Context / NVP-005 Consistent Meaning / NVP-006 Task over Organization / NVP-007 Progressive Disclosure / NVP-008 Accessible Navigation、Navigation State Model (Exploring)。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Categories: Identification / Editorial and Support、CTP-002 Plain and Direct Language / CTP-004 Evidence-backed Claims / CTP-005 Consistent Terminology / CTP-008 Accessible and Scannable Content / CTP-009 Context-preserving References / CTP-010 Separate Fact, Decision, and Promotion。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA-001 Action Clarity / CTA-009 Accessible Activation / CTA-010 No Unsupported Pressure、§7 Relationship with Screen Matrix の SCR-002 行、§8 Boundary between CTA and Navigation。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — SCR-002 Destination Discovery の責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements / UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens / UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 15. Downstream Impact

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 本 Screen Requirement の下流に位置する。既存 Design System を参照して実現可能性や未整備箇所を確認できるが、既存 Component を上流要求へ昇格させない。具体的な Component・レイアウト・地図・トークン・表示項目を指定しない。既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。
- **Implementation** — Repository の管理対象外。本文書だけで実装仕様を確定しない。SCR-002 を実装 1 画面・URL・route と同一視しない (UXDR-TRAVEL-002)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。各 Open Issue が影響する要件節を可能な範囲で示す。

- **Destination の正式な分類と階層構造** — §5 Information Responsibilities, §6 Functional Requirements, §8 Navigation Requirements。
- **地理・交通・観光・ランドマーク等の概念関係** — §5, §8。
- **Destination の識別・表示単位** — §5, §6。
- **Content の正式分類と責務** — §5, §7 Content Requirements。
- **Destination と Content の関連付け** — §5, §6, §8。
- **Destination と Accommodation の関連付け** — §5, §8。
- **Accommodation を SCR-002 でどこまで扱うか** — §5。
- **SCR-001 Service Entry との責務境界および分割・統合** — §2, §13。
- **SCR-003 Accommodation Search への接続と引き渡す情報** — §2, §6。
- **SCR-004 Search Results との関係** — §2, §6。
- **SCR-014 Editorial Content との責務境界** — §2, §7。
- **発見・探索と編集情報・販促誘導の境界** — §7, §9 CTA Requirements。
- **推奨・人気・ランキング等を扱う場合の根拠と責任主体** — §6, §7, §9。
- **Global Navigation の対象領域** — §8。
- **Local Navigation の分類単位** — §8。
- **Contextual Navigation の表示条件** — §8。
- **URL・route・サイトマップ・画面遷移** — §6, §13。
- **モバイル・レスポンシブ時の探索方法** — §8, §11 Accessibility Requirements。
- **Screen Requirement ID 体系** — 文書全体 ([README.md](README.md) §7)。
- **ファイル命名規則** — 本文書のファイル名 `destination-discovery.md` は暫定 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — §17 Acceptance Criteria。
- **Design System への反映確認方法** — §15 Downstream Impact ([README.md](README.md) §17)。

## 17. Acceptance Criteria

未定義の UI・分類・階層・業務仕様を確定しない範囲で記述する。最終確定主体は Open Issue として維持する (§16)。

- 文書が [README.md](README.md) §6 Common Document Structure を満たしている。
- Related Screen Matrix Candidate が SCR-002 として追跡可能であり、SCR-002 のみである。
- [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-002 の Responsibility・Purpose・Primary User Tasks・Primary IA Objects・Supporting IA Objects・Navigation Types・Content Categories・Navigation States と一致している。
- Destination・Content を Primary、Accommodation を Supporting として扱い、主従を逆転していない (§5)。
- Supporting IA Object (Accommodation) から検索結果・施設詳細等の内部要件を導出していない (§5)。
- Destination・Content の例示を正式な分類・階層として扱っていない (§5, §6, §7)。
- Navigation と CTA の要件が別節・別責務として記述され、NAV-001・NAV-002・NAV-003 を混同していない (§8, §9)。
- Navigation State が Exploring のみであり、Entry・Evaluating・Error / Interrupted 等を独断で追加していない (§10)。
- 発見・探索と販促誘導を区別し、事実・編集情報・推奨・販促表現を混同していない (§7, §9)。
- SCR-001・SCR-003・SCR-004・SCR-014 の内部要件を取り込んでいない (§2)。
- UI・階層・分類・掲載順・ランキング・URL・route・API・DB・CTA 文言・Component を確定していない (§13, §15)。
- 未定義の要求が Open Issue として追跡でき、上流成果物の ID・正式名称を追跡できる (§14, §16)。
- 下流 Design System との関係が Downstream Impact へ分離されている (§15)。
- 文書 Status が Draft である。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial draft of Travel Destination Discovery Screen Requirement (SCR-002) | Draft |
