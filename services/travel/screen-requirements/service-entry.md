# Travel Service Entry Screen Requirement

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補 SCR-001 Service Entry に対応する個別 Screen Requirement の初版 Draft
- Position in Repository: `services/travel/screen-requirements/service-entry.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)、作成順序評価は [creation-plan.md](creation-plan.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Design System / Implementation) との関係は §15 Downstream Impact を参照。

本文書はファイル名 `service-entry.md` で作成する。これは記述的な暫定ファイル名であり、正式なファイル命名規則を確定するものではない (§16 Open Issues)。文書は Title およびファイル名で識別し、`SCR-001` を Screen Requirement 文書 ID として再定義しない。

## 1. Purpose

- 画面候補 SCR-001 Service Entry ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) の責務を、Repository 内の既存上流成果物 (SD-001〜SD-007, Governance) から確認できる範囲で個別 Screen Requirement として記述する。
- 国内宿泊サービスの入口として、利用者が探索の起点に立つための要件を定義する。
- 未定義の事業要求・業務仕様・画面仕様は補完せず、Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- 画面候補の責務を具体的な画面構成・UI へ変換しない。SCR-001 を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

## 2. Related Screen Matrix Candidates

- **SCR-001 Service Entry** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) — 唯一の対応画面候補。
- 本文書は SCR-001 に既に定義された責務と利用者タスクのみを扱い、SCR-002 Destination Discovery の内部要件を取り込まない。
- SCR-001 と SCR-002 の境界、および両者の分割・統合は確定しない (§16 Open Issues)。SCR-002 へ接続し得ることと、同一画面・同一文書へ統合することを混同しない。
- 本文書の作成単位 (SCR-001 単独) は、未決事項を保持したまま作成可能な範囲を文書化するための暫定的な作成単位であり、SCR-001/SCR-002 の恒久的な分離を決定するものではない。将来の分割・統合判断により文書構成が変更され得る。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は SCR-001 Service Entry を画面候補 (Status: Draft) として管理する。
- レイヤー入口 [README.md](README.md) と作成順序評価 [creation-plan.md](creation-plan.md) が存在し、[creation-plan.md](creation-plan.md) §10・§11 は最初に作成する候補を SCR-001 とする。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は SCR-001 の要件を、上流成果物から確認できる範囲で記述する。
- 作成単位を SCR-001 単独とする (暫定。§2)。
- 未定義の事業・業務・機能・画面仕様は推測で補完せず Open Issue として保持する (UXDR-TRAVEL-001)。
- Navigation と CTA を別責務として記述する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities と一致)。
- ファイル名 `service-entry.md` は暫定であり、正式命名規則を確定しない。

### Hypotheses

- なし。

### Open Issues

- SCR-001/SCR-002 の境界と将来の分割・統合。
- Global Navigation の対象領域。
- Screen Requirement ID 体系・ファイル命名規則。
- (詳細は §16 に集約)

## 4. User Tasks

[Screen Matrix](../service-design/screen-matrix.md) §5 SCR-001 の Primary User Tasks を上流参照する (再定義しない)。

- サービスの主要な選択肢を理解し、探索の起点に立つ。

上位基準として SDP-001 User Task Clarity (利用者が現在何を行い、次に何を行えるかを理解できる) を適用する。具体的な探索行動 (検索・目的地探索・特集閲覧等) のどれを主要とするかは確定しない (§16 Open Issues)。

## 5. Information Responsibilities

[Information Architecture](../service-design/information-architecture.md) (SD-002) を上流参照し、扱う情報オブジェクトを示す。IA オブジェクトの定義・追加・変更は行わない。

- **IA-OBJ-001 Destination** — 「どこに泊まるか」を検討・指定するための地理/目的地の観点を、探索起点として扱う。
- **IA-OBJ-002 Search Criteria** — 利用者の探索意図を条件として保持する起点を扱う。入力項目は確定しない (IA-OBJ-002 Does Not Decide)。
- **IA-OBJ-012 Content** — 発見・理解を支援する説明・案内的情報の入口を扱う。正式な分類は確定しない (IA-OBJ-012 Open Issue)。

Supporting IA Objects は Screen Matrix §5 SCR-001 において「なし」であり、本文書でも追加しない。Destination の階層構造、Search Criteria の入力項目、Content の分類は未定義であり Open Issue として保持する (§16)。

## 6. Functional Requirements

上流成果物から確認できる能力・責務のみを記述する。業務仕様が未定義の事項は要件化せず Open Issue とする ([README.md](README.md) §6)。

- 利用者が、現在地が国内宿泊サービスの入口であることを識別できること (SDP-001, NVP-001 Current Location Visibility)。
- 利用者が、探索を開始するために利用可能な行動を理解できること (SDP-001, NAV-004 Task Navigation)。
- Destination、Search Criteria、Content に関係する探索起点を扱えること (IA-OBJ-001 / IA-OBJ-002 / IA-OBJ-012)。
- 入口の主要な探索行動と、補助的な移動・支援行動を区別できること (CTA-002 One Clear Primary Action, NAV-006 Utility Navigation)。
- Entry から Exploring へ進む際、不要な入力・登録・確約を先行要求しないこと (SDP-002 Progressive Commitment, CTA-004 Progressive Commitment)。
- Navigation の選択前に、移動先または結果を合理的に予測できること (NVP-002 Predictable Destination)。
- 利用不能・未確定の行動や情報がある場合、その状態を利用者が識別できること (SDP-005 State Visibility の範囲。なお SCR-001 の確定状態は Entry・Exploring に限る。§10)。

以下は決定しない (Open Issue として §16 で扱う)。

- どの Destination を提示するか。
- Search Criteria の入力項目。
- Content の具体分類・掲載内容。
- 主要行動が検索・目的地探索・特集閲覧等のどれであるか。
- 具体的な機能数や表示順。
- 遷移先・URL・route。

## 7. Content Requirements

[Content Principles](../service-design/content-principles.md) (SD-004) の Content Category と原則を上流参照する。SCR-001 の Content Categories は Identification / Task Guidance / Editorial and Support ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-001)。

- **Identification** — サービスと入口の役割を識別可能にする (CTP-002 Plain and Direct Language, CTP-005 Consistent Terminology)。
- **Task Guidance** — 利用者が次に可能な行動を理解できる案内を提供する (CTP-001 Purpose Before Detail, CTP-002)。
- **Editorial and Support** — 発見・理解を支援する情報を、予約・確約済みの情報と混同させない (CTP-010 Separate Fact, Decision, and Promotion)。
- Fact・Decision・Hypothesis・Open Issue または未確定情報を混同しない (CTP-004 Evidence-backed Claims, CTP-006 Explicit State and Uncertainty)。
- 利用できない・未確定・条件付きの情報を確定事項として表現しない (CTP-006)。
- 視覚表現だけに依存せず意味を理解できるようにする (CTP-008 Accessible and Scannable Content)。

具体的なコピー・ブランドトーン・SEO 文言・販促メッセージは決定しない (§13 Does Not Decide)。

## 8. Navigation Requirements

[Navigation](../service-design/navigation.md) (SD-003) を上流参照する。SCR-001 の Navigation Types は NAV-001 / NAV-004 / NAV-006 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-001)。3 分類を責務として区別して記述する。

- **NAV-001 Global Navigation** — 主要領域への一貫した入口を提供する。対象領域・項目・ラベル・配置・会員メニュー・他サービス統合は確定しない (NAV-001 Does Not Decide, §16 Open Issues)。
- **NAV-004 Task Navigation** — 探索を開始・進行するための行動を理解可能にする。正式なタスク一覧は確定しない (NAV-004 Does Not Decide)。
- **NAV-006 Utility Navigation** — 主要タスクを阻害せず、補助的な情報・機能へ到達可能にする。対象項目は確定しない (NAV-006 Does Not Decide)。
- 現在が国内宿泊サービスの入口であることを理解可能にする (NVP-001 Current Location Visibility)。
- 移動先または結果を事前に予測可能にする (NVP-002 Predictable Destination)。
- 内部組織やシステム都合ではなく利用者タスクを基準にする (NVP-006 Task over Organization)。
- 現在の判断に不要な選択肢を過剰に提示しない (NVP-007 Progressive Disclosure)。
- Navigation と CTA を同一責務として扱わない (UXDR-TRAVEL-003, §9)。

## 9. CTA Requirements

[CTA Principles](../service-design/cta-principles.md) (SD-005) を上流参照する。SCR-001 に関する記述は [../service-design/cta-principles.md](../service-design/cta-principles.md) §7 Relationship with Screen Matrix の SCR-001 行 (CTA Consideration「探索開始と補助導線を競合させない」)。Navigation と CTA は別責務とする (UXDR-TRAVEL-003)。

- 同一の判断文脈で、主要な探索行動と補助行動を競合させない (CTA-002 One Clear Primary Action)。
- 理解・探索より前に、入力・登録・確約を要求しない (CTA-004 Progressive Commitment)。
- CTA の意味と実行可能性を視覚だけに依存させない (CTA-009 Accessible Activation)。
- Navigation Action を自動的に主要 CTA として扱わない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §8 Boundary between CTA and Navigation)。
- 行動の具体的内容と結果が未定義の場合、主要 CTA を確定しない (SDP-010 Incremental Definition)。

具体的な CTA 行動・ラベル・配置・色・Component・数の上限は決定しない (§13 Does Not Decide)。

## 10. State and Feedback Requirements

対象状態は [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-001 に存在する Entry と Exploring のみとする。[Navigation](../service-design/navigation.md) §6 Navigation State Model を上流参照する。

- Entry (サービスまたは領域へ入った状態) と Exploring (候補・情報を探索している状態) の違いを、利用者が理解できること。
- 探索開始後に、現在の状態または文脈を不必要に失わせないこと (NVP-003 Preserved Context)。
- 状態変化を色・位置・アニメーションだけで伝えないこと (SDP-007, CTP-008)。
- 未定義の Loading・Success・Error 等を、SCR-001 の確定状態として追加しないこと。SCR-001 に `Error / Interrupted` を独断で追加しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-001 は Entry・Exploring のみを定義)。

## 11. Accessibility Requirements

SDP-007 Accessibility by Default / NVP-008 Accessible Navigation / CTP-008 Accessible and Scannable Content / CTA-009 Accessible Activation の範囲で記述する。

- キーボード・支援技術・異なる画面サイズを例外扱いしない (SDP-007, NVP-008)。
- 行動の意味・役割・状態を視覚だけで伝えない (CTA-009, CTP-008)。
- Navigation および CTA を認識・理解・実行可能にする (NVP-008, CTA-009)。
- 情報の階層と探索開始の選択肢を、支援技術で理解可能にする (CTP-008)。
- モバイルでも要件の意味を失わせない (SDP-007)。

具体的な規格・達成レベル・HTML 属性・Component 実装は決定しない (§13 Does Not Decide)。

## 12. Constraints

- 上流成果物 (SD-001〜SD-007) の定義を再定義・変更しない ([README.md](README.md) §9)。
- 作成単位は SCR-001 単独に限定し、SCR-002 の内部要件を取り込まない (§2)。
- 未定義事項を Fact または Decision として扱わず、Open Issue として保持する (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。
- 確定可能な範囲からのみ記述し、未決事項へ依存する要件を確定しない (SDP-010 Incremental Definition)。
- サービス全体の整合性を優先し、入口単体の最適化で他画面・全体導線を損なわない (SDP-009 Service-wide Coherence)。

## 13. Does Not Decide

本文書だけでは以下を確定しない。

- 具体的な入口 UI・レイアウト・ワイヤーフレーム・遷移・URL・route ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-001 Does Not Decide)。
- ヘッダー・メニュー・検索フォーム等の具体構成。
- Global Navigation の具体的な対象領域・項目・表示順・ラベル。
- 主要 CTA の具体的な行動・文言・配置・数・視覚階層。
- Destination・Search Criteria・Content の具体的な選択肢や分類。
- 会員・非会員の画面差、認証・決済・会員・予約の業務仕様。
- モバイル時の具体的な Navigation UI。
- SCR-001/SCR-002 の統合・分割、Screen Requirement ID 体系・ファイル命名規則。

## 14. Upstream References

上流成果物は [README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。定義を本文書で変更しない。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — SDP-001 User Task Clarity / SDP-002 Progressive Commitment / SDP-007 Accessibility by Default / SDP-008 Evidence over Assumption / SDP-009 Service-wide Coherence / SDP-010 Incremental Definition。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — IA-OBJ-001 Destination / IA-OBJ-002 Search Criteria / IA-OBJ-012 Content。
- **SD-003 [Navigation](../service-design/navigation.md)** — NAV-001 Global Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation、NVP-001 Current Location Visibility / NVP-002 Predictable Destination / NVP-003 Preserved Context / NVP-006 Task over Organization / NVP-007 Progressive Disclosure / NVP-008 Accessible Navigation、Navigation State Model (Entry / Exploring)。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Categories: Identification / Task Guidance / Editorial and Support、CTP-001 Purpose Before Detail / CTP-002 Plain and Direct Language / CTP-004 Evidence-backed Claims / CTP-005 Consistent Terminology / CTP-006 Explicit State and Uncertainty / CTP-008 Accessible and Scannable Content / CTP-010 Separate Fact, Decision, and Promotion。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA-002 One Clear Primary Action / CTA-004 Progressive Commitment / CTA-009 Accessible Activation、§7 Relationship with Screen Matrix の SCR-001 行、§8 Boundary between CTA and Navigation。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — SCR-001 Service Entry の責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements / UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens / UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 15. Downstream Impact

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 本 Screen Requirement の下流に位置する。既存 Design System を参照して実現可能性や未整備箇所を確認できるが、既存 Component・Button variant・レイアウト・トークン・ブレークポイントを前提に要件を変形しない。既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。本文書は具体的な Component・トークンを指定しない。
- **Implementation** — Repository の管理対象外。本文書だけで実装仕様を確定しない。SCR-001 を実装 1 画面・URL・route と同一視しない (UXDR-TRAVEL-002)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。各 Open Issue が影響する要件節を可能な範囲で示す。

- **SCR-001 と SCR-002 の境界** — §2 Related Screen Matrix Candidates, §5 Information Responsibilities。
- **将来の分割・統合** — §2。
- **Global Navigation の対象領域** — §8 Navigation Requirements。
- **Global Navigation の具体項目・表示順・ラベル** — §8。
- **会員・非会員の Navigation 差** — §8, §13。
- **他サービスとの Navigation 統合** — §8。
- **主要な探索行動の具体内容** — §4 User Tasks, §6 Functional Requirements, §9 CTA Requirements。
- **Destination の階層・提示範囲** — §5, §6。
- **Search Criteria の入力項目** — §5, §6。
- **Content の分類・編集方針** — §5, §7 Content Requirements。
- **Utility Navigation の対象** — §8。
- **モバイル Navigation の具体方式** — §8, §11 Accessibility Requirements。
- **URL・route・サイトマップ・遷移先** — §6, §13。
- **Screen Requirement ID 体系** — 文書全体 ([README.md](README.md) §7)。
- **ファイル命名規則** — 本文書のファイル名 `service-entry.md` は暫定 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — §17 Acceptance Criteria。
- **Design System への反映確認方法** — §15 Downstream Impact ([README.md](README.md) §17)。

## 17. Acceptance Criteria

未定義の UI・業務仕様を確定しない範囲で記述する。最終確定主体は Open Issue として維持する (§16)。

- 文書が [README.md](README.md) §6 Common Document Structure を満たしている。
- Related Screen Matrix Candidate が SCR-001 として追跡可能である。
- [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-001 の Responsibility・Primary User Tasks・Primary / Supporting IA Objects・Navigation Types・Content Categories・Navigation States と一致している。
- Navigation と CTA の要件が別節・別責務として記述されている (§8, §9)。
- Entry と Exploring 以外の状態を独断で追加していない (§10)。
- 未定義の要求が Open Issue として記録されている (§16)。
- URL・route・UI・Component・業務仕様を確定していない (§13, §15)。
- 上流成果物の ID・正式名称を追跡できる (§14)。
- 下流 Design System との関係が Downstream Impact へ分離されている (§15)。
- 文書 Status が Draft である。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Initial draft of Travel Service Entry Screen Requirement (SCR-001) | Draft |
