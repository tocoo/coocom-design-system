# Travel Help and Support Screen Requirement

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補 SCR-013 Help and Support に対応する個別 Screen Requirement の初版 Draft
- Position in Repository: `services/travel/screen-requirements/help-and-support.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)、作成順序評価は [creation-plan.md](creation-plan.md)、先行する個別要件例は [service-entry.md](service-entry.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Design System / Implementation) との関係は §15 Downstream Impact を参照。

本文書はファイル名 `help-and-support.md` で作成する。これは記述的な暫定ファイル名であり、正式なファイル命名規則を確定するものではない (§16 Open Issues)。文書は Title およびファイル名で識別し、`SCR-013` を Screen Requirement 文書 ID として再定義しない。

## 1. Purpose

- 画面候補 SCR-013 Help and Support ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) の責務を、Repository 内の既存上流成果物 (SD-001〜SD-007, Governance) から確認できる範囲で個別 Screen Requirement として記述する。
- 利用者が問題解決・条件確認の支援を得るための要件を定義する。
- 未定義のサポート対象範囲・FAQ 構成・問い合わせ手段等は補完せず、Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- SCR-013 の責務を具体的なサポート業務・FAQ サイト・問い合わせフォーム・チャット等の画面仕様へ変換しない。SCR-013 を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

## 2. Related Screen Matrix Candidates

- **SCR-013 Help and Support** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) — 唯一の対応画面候補。
- 本文書は SCR-013 に既に定義された責務と利用者タスクのみを扱う。
- FAQ・問い合わせ・Policy 確認・問題解決が同一画面になるか別画面になるか、およびエラー・中断専用画面の要否は確定しない (§16 Open Issues)。
- 本文書の作成単位 (SCR-013 単独) は、未決事項を保持したまま作成可能な範囲を文書化するための暫定的な作成単位であり、将来の分割・統合判断により文書構成が変更され得る。本文書の作成順は、探索・補助候補群の正式な作成順を確定するものではない ([creation-plan.md](creation-plan.md) §10)。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は SCR-013 Help and Support を画面候補 (Status: Draft) として管理する。
- レイヤー入口 [README.md](README.md)、作成順序評価 [creation-plan.md](creation-plan.md)、先行する個別要件 [service-entry.md](service-entry.md) (SCR-001) が存在する。
- [creation-plan.md](creation-plan.md) は SCR-013 を「その次に作成可能な候補群」(独立性が高い) と評価する (§10)。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は SCR-013 の要件を、上流成果物から確認できる範囲で記述する。
- 作成単位を SCR-013 単独とする (暫定。§2)。
- Content・Policy を Primary IA Objects、User・Booking を Supporting IA Objects として扱い、主従を逆転しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-013)。
- 未定義の事業・業務・機能・画面仕様は推測で補完せず Open Issue として保持する (UXDR-TRAVEL-001)。
- Navigation と CTA を別責務として記述する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities と一致)。
- ファイル名 `help-and-support.md` は暫定であり、正式命名規則を確定しない。

### Hypotheses

- なし。

### Open Issues

- Help and Support の対象範囲。
- FAQ の要否・分類・構成、問い合わせ手段。
- Screen Requirement ID 体系・ファイル命名規則。
- (詳細は §16 に集約)

## 4. User Tasks

[Screen Matrix](../service-design/screen-matrix.md) §5 SCR-013 の Primary User Tasks を上流参照する (再定義しない)。

- 問題解決・条件確認の支援を得る。

上位基準として SDP-001 User Task Clarity (利用者が現在何を行い、次に何を行えるかを理解できる) を適用する。どの問題種別・支援内容を対象とするかは確定しない (§16 Open Issues)。

## 5. Information Responsibilities

[Information Architecture](../service-design/information-architecture.md) (SD-002) を上流参照する。IA オブジェクトの定義・追加・変更は行わない。Screen Matrix §5 SCR-013 の Primary / Supporting の区別を保つ。

### Primary IA Objects

- **IA-OBJ-012 Content** — 発見・理解・問題解決を支援する説明・案内的情報を、支援の文脈で扱う。正式な分類は確定しない (IA-OBJ-012 Open Issue)。
- **IA-OBJ-008 Policy** — 予約や宿泊に適用される条件・制約を、条件確認の文脈で扱う。正式な分類は確定しない (IA-OBJ-008 Open Issue)。

### Supporting IA Objects

- **IA-OBJ-011 User** — 支援を求める主体として補助的に参照する。会員制度・認証・識別方法を前提にしない (IA-OBJ-011 Open Issue)。
- **IA-OBJ-010 Booking** — 支援対象となり得る予約として補助的に参照する。予約管理機能・予約状態を取り込まない (IA-OBJ-010 Open Issue)。

Supporting IA Objects (User / Booking) から、認証・会員・予約管理の機能を推測しない。Primary と Supporting の主従を逆転しない。

## 6. Functional Requirements

上流成果物から確認できる能力・責務のみを記述する。業務仕様が未定義の事項は要件化せず Open Issue とする ([README.md](README.md) §6)。

- 利用者が、問題解決または条件確認のための支援へ到達できること (SDP-001, NAV-006 Utility Navigation)。
- 利用可能な支援内容と、その目的を理解できること (SDP-001, NVP-002 Predictable Destination)。
- Content および Policy を、問題解決・条件確認の文脈で参照できること (IA-OBJ-012 / IA-OBJ-008, SDP-003 Transparent Conditions)。
- 現在の情報・対象・タスクに関連する支援へ移動できること (NAV-003 Contextual Navigation, NVP-003 Preserved Context)。
- 問題発生または中断時に、回復可能な次の行動を理解できること (SDP-006 Recoverability, NVP-004 Reversible Movement)。
- 支援が利用できない・未定義・条件付きの場合、その状態を利用者が識別できること (SDP-005 State Visibility)。
- User または Booking に関係する支援を扱う場合も、未定義の認証・予約機能を前提にしないこと (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。

以下は決定しない (Open Issue として §16 で扱う)。

- 具体的なサポートチャネル、問い合わせ方法。
- FAQ 構成、Policy 分類。
- 利用者ごとの提供範囲。
- Booking との具体的連携。
- 問題種別ごとの処理フロー。

## 7. Content Requirements

[Content Principles](../service-design/content-principles.md) (SD-004) の Content Category と原則を上流参照する。SCR-013 の Content Categories は Editorial and Support / Conditions and Policies ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-013)。

- **Editorial and Support** — 発見・理解・問題解決を支援する情報を提供する (CTP-004 Evidence-backed Claims, CTP-008 Accessible and Scannable Content, CTP-009 Context-preserving References)。
- **Conditions and Policies** — 条件・制約・利用可否を、判断へ影響する位置・時点で理解可能にする (CTP-003 Conditions Near Decisions, CTP-005 Consistent Terminology, CTP-006 Explicit State and Uncertainty)。
- Editorial and Support と Conditions and Policies を区別する。
- 状態・不確実性・未定義事項を確定情報として表現しない (CTP-006)。
- 問題解決に必要な情報と、販促・編集情報を混同しない (CTP-010 Separate Fact, Decision, and Promotion)。
- 利用者が次に可能な行動を理解できる案内を、必要に応じて提供する (CTP-001 Purpose Before Detail)。
- 情報の意味を色・アイコン・位置だけに依存させない (CTP-008)。

具体的な FAQ 文言・問い合わせ案内・Policy 本文・法務文言・ブランドトーンは決定しない (§13 Does Not Decide)。

## 8. Navigation Requirements

[Navigation](../service-design/navigation.md) (SD-003) を上流参照する。SCR-013 の Navigation Types は NAV-001 / NAV-002 / NAV-003 / NAV-006 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-013)。4 分類を責務として区別して記述する。

- **NAV-001 Global Navigation** — 主要領域から支援へ到達し得るようにする。対象領域・項目・配置は確定しない (NAV-001 Does Not Decide, §16 Open Issues)。
- **NAV-002 Local Navigation** — 支援領域内部の関連情報へ移動し得るようにする。分類単位は確定しない (NAV-002 Does Not Decide)。
- **NAV-003 Contextual Navigation** — 現在の情報・対象・タスクに関連する支援へ移動し得るようにする。表示条件は確定しない (NAV-003 Does Not Decide)。
- **NAV-006 Utility Navigation** — 主要タスクを阻害せず、補助的な支援へ到達し得るようにする。対象項目は確定しない (NAV-006 Does Not Decide)。
- 移動先と目的を事前に予測可能にする (NVP-002 Predictable Destination)。
- 現在が支援領域のどこであるかを理解可能にする (NVP-001 Current Location Visibility)。
- 問題解決後または誤った移動後に、合理的な戻り先を理解可能にする (NVP-004 Reversible Movement, NVP-003 Preserved Context)。
- 内部組織やシステム都合ではなく利用者タスクを基準にする (NVP-006 Task over Organization)。
- Navigation と CTA を同一責務として扱わない (UXDR-TRAVEL-003, §9)。

具体的なメニュー・リンク・ラベル・配置・表示条件は確定しない (§13 Does Not Decide)。

## 9. CTA Requirements

[CTA Principles](../service-design/cta-principles.md) (SD-005) を上流参照する。SCR-013 に関する記述は [../service-design/cta-principles.md](../service-design/cta-principles.md) §7 Relationship with Screen Matrix の SCR-013 行 (CTA Consideration「問題解決・問い合わせ・戻り先を明確にする」)。Navigation と CTA は別責務とする (UXDR-TRAVEL-003)。

- 問題解決または回復を進める行動と、単なる情報間移動を区別する (CTA-TYPE-004 Recovery Action, [../service-design/cta-principles.md](../service-design/cta-principles.md) §8 Boundary between CTA and Navigation)。
- Recovery Action に該当する場合、行動内容と期待される結果を理解可能にする (CTA-TYPE-004 Recovery Action)。
- 利用可能・利用不能・処理中等の状態を曖昧にしない (CTA-007 Explicit State and Availability)。
- 利用不能な場合、理由または次に可能な行動を、確認可能な範囲で示す (CTA-007)。
- CTA の意味・状態・実行可能性を視覚だけに依存させない (CTA-009 Accessible Activation)。
- 問い合わせ手段や処理フローが未定義の場合、具体的な CTA を確定しない (SDP-010 Incremental Definition)。

具体的な CTA 文言・数・配置・優先順位・Component は決定しない (§13 Does Not Decide)。

## 10. State and Feedback Requirements

対象状態は [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-013 に存在する Entry / Exploring / Error / Interrupted のみとする。[Navigation](../service-design/navigation.md) §6 Navigation State Model を上流参照する。`Error / Interrupted` は上流 Navigation State の複合名として扱い、`Error` と `Interrupted` という別々の新規状態へ再定義しない。

- **Entry** — 支援領域へ到達したことと、利用可能な支援の目的を理解できること。
- **Exploring** — 関連する支援情報を探索している状態を理解できること (NVP-003 Preserved Context)。
- **Error / Interrupted** — 問題または中断の発生を理解し、回復可能な行動または支援情報を確認できること (SDP-006 Recoverability, CTP-007 Actionable Error and Recovery)。
- 状態変化を色・位置・アニメーションだけで伝えないこと (SDP-007, CTP-008)。
- 未定義の Loading・Success・Completed 等を、SCR-013 の確定状態として独断で追加しないこと ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-013 は Entry・Exploring・Error / Interrupted のみを定義)。

## 11. Accessibility Requirements

SDP-007 Accessibility by Default / NVP-008 Accessible Navigation / CTP-008 Accessible and Scannable Content / CTA-009 Accessible Activation の範囲で記述する。

- キーボード・支援技術・異なる画面サイズを例外扱いしない (SDP-007, NVP-008)。
- 支援内容・Navigation・CTA・状態を視覚だけで伝えない (CTA-009, CTP-008)。
- 問題発生時の説明と回復行動を、支援技術で理解可能にする (CTP-008, SDP-006)。
- 支援情報へ到達し、内容を読み、必要な行動を実行できること (NVP-008, CTA-009)。
- モバイルでも支援への到達可能性と意味を失わせないこと (SDP-007)。

具体的な規格・達成レベル・HTML 属性・Component 実装は決定しない (§13 Does Not Decide)。

## 12. Constraints

- 上流成果物 (SD-001〜SD-007) の定義を再定義・変更しない ([README.md](README.md) §9)。
- 作成単位は SCR-013 単独に限定し、Supporting IA Objects (User / Booking) から認証・会員・予約管理機能を取り込まない (§2, §5)。
- 未定義事項を Fact または Decision として扱わず、Open Issue として保持する (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。
- 確定可能な範囲からのみ記述し、未決事項へ依存する要件を確定しない (SDP-010 Incremental Definition)。
- サービス全体の整合性を優先し、支援領域単体の最適化で他画面・全体導線を損なわない (SDP-009 Service-wide Coherence)。

## 13. Does Not Decide

本文書だけでは以下を確定しない。

- 具体的なサポート業務・FAQ サイト・問い合わせフォーム・チャット等の画面仕様・UI・レイアウト・ワイヤーフレーム ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-013 Does Not Decide)。
- サポート対象範囲、FAQ のカテゴリ・記事・構成。
- 問い合わせ手段 (電話・メール・フォーム・チャット等)、サポート対応時間・SLA・担当部門・エスカレーション。
- 問い合わせ入力項目・バリデーション。
- Policy の正式分類・内容。
- Booking に連動するサポート機能、認証済み利用者向け機能。
- FAQ・問い合わせ・Policy 確認・問題解決の画面分割/統合、エラー・中断専用画面の要否。
- URL・route・サイトマップ・画面遷移。
- CTA 文言・配置・色・数・Component。
- Screen Requirement ID 体系・ファイル命名規則。

## 14. Upstream References

上流成果物は [README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。定義を本文書で変更しない。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — SDP-001 User Task Clarity / SDP-003 Transparent Conditions / SDP-005 State Visibility / SDP-006 Recoverability / SDP-007 Accessibility by Default / SDP-008 Evidence over Assumption / SDP-009 Service-wide Coherence / SDP-010 Incremental Definition。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — Primary: IA-OBJ-012 Content / IA-OBJ-008 Policy。Supporting: IA-OBJ-011 User / IA-OBJ-010 Booking。
- **SD-003 [Navigation](../service-design/navigation.md)** — NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-006 Utility Navigation、NVP-001 Current Location Visibility / NVP-002 Predictable Destination / NVP-003 Preserved Context / NVP-004 Reversible Movement / NVP-006 Task over Organization / NVP-008 Accessible Navigation、Navigation State Model (Entry / Exploring / Error / Interrupted)。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Categories: Editorial and Support / Conditions and Policies、CTP-001 Purpose Before Detail / CTP-003 Conditions Near Decisions / CTP-004 Evidence-backed Claims / CTP-005 Consistent Terminology / CTP-006 Explicit State and Uncertainty / CTP-007 Actionable Error and Recovery / CTP-008 Accessible and Scannable Content / CTP-009 Context-preserving References / CTP-010 Separate Fact, Decision, and Promotion。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA-007 Explicit State and Availability / CTA-009 Accessible Activation、CTA-TYPE-004 Recovery Action、§7 Relationship with Screen Matrix の SCR-013 行、§8 Boundary between CTA and Navigation。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — SCR-013 Help and Support の責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements / UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens / UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 15. Downstream Impact

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 本 Screen Requirement の下流に位置する。既存 Design System を参照して実現可能性や未整備箇所を確認できるが、既存 Component の有無から上流要件を変更しない。Accordion・フォーム・チャット・モーダル等の具体 Component を指定しない。既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。
- **Implementation** — Repository の管理対象外。本文書だけで実装仕様を確定しない。SCR-013 を実装 1 画面・URL・route と同一視しない (UXDR-TRAVEL-002)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。各 Open Issue が影響する要件節を可能な範囲で示す。

- **Help and Support の対象範囲** — §4 User Tasks, §6 Functional Requirements。
- **FAQ の要否・分類・構成** — §6, §7 Content Requirements。
- **問い合わせ手段** — §6, §9 CTA Requirements。
- **サポートチャネル** — §6, §9。
- **サポート提供時間・運用体制** — §6。
- **Policy の分類・情報源** — §5 Information Responsibilities, §7。
- **User および Booking との具体的な関係** — §5。
- **認証前後の提供差** — §5, §6。
- **Contextual Navigation の表示条件** — §8 Navigation Requirements。
- **Local Navigation の分類単位** — §8。
- **Utility Navigation の対象** — §8。
- **問題解決後の戻り先** — §8, §10 State and Feedback Requirements。
- **エラー・中断専用画面の要否** — §2, §10。
- **URL・route・サイトマップ・画面遷移** — §6, §13。
- **モバイル時の具体的な支援導線** — §8, §11 Accessibility Requirements。
- **Screen Requirement ID 体系** — 文書全体 ([README.md](README.md) §7)。
- **ファイル命名規則** — 本文書のファイル名 `help-and-support.md` は暫定 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — §17 Acceptance Criteria。
- **Design System への反映確認方法** — §15 Downstream Impact ([README.md](README.md) §17)。

## 17. Acceptance Criteria

未定義の UI・業務仕様を確定しない範囲で記述する。最終確定主体は Open Issue として維持する (§16)。

- 文書が [README.md](README.md) §6 Common Document Structure を満たしている。
- Related Screen Matrix Candidate が SCR-013 として追跡可能であり、SCR-013 のみである。
- [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-013 の Responsibility・Primary User Tasks・Primary IA Objects・Supporting IA Objects・Navigation Types・Content Categories・Navigation States と一致している。
- Primary IA Objects (Content / Policy) と Supporting IA Objects (User / Booking) を混同・逆転していない (§5)。
- Navigation と CTA の要件が別節・別責務として記述されている (§8, §9)。
- `Error / Interrupted` を上流の複合状態名として扱い、Entry・Exploring・Error / Interrupted 以外の状態を独断で追加していない (§10)。
- 未定義のサポートチャネル・FAQ 構成・問い合わせ方法を確定していない (§13)。
- User・Booking の補助参照から認証・予約機能を推測していない (§5)。
- URL・route・UI・Component・業務運用を確定していない (§13, §15)。
- 未定義の要求が Open Issue として追跡できる (§16)。
- 上流成果物の ID・正式名称を追跡できる (§14)。
- 下流 Design System との関係が Downstream Impact へ分離されている (§15)。
- 文書 Status が Draft である。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Initial draft of Travel Help and Support Screen Requirement (SCR-013) | Draft |
