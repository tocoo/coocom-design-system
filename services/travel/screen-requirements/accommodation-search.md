# Travel Accommodation Search Screen Requirement

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補 SCR-003 Accommodation Search に対応する個別 Screen Requirement の初版 Draft
- Position in Repository: `services/travel/screen-requirements/accommodation-search.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)、作成順序評価は [creation-plan.md](creation-plan.md)、先行する個別要件例は [service-entry.md](service-entry.md) / [help-and-support.md](help-and-support.md) / [editorial-content.md](editorial-content.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Design System / Implementation) との関係は §15 Downstream Impact を参照。

本文書はファイル名 `accommodation-search.md` で作成する。これは記述的な暫定ファイル名であり、正式なファイル命名規則を確定するものではない (§16 Open Issues)。文書は Title およびファイル名で識別し、`SCR-003` を Screen Requirement 文書 ID として再定義しない。

## 1. Purpose

- 画面候補 SCR-003 Accommodation Search ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) の責務を、Repository 内の既存上流成果物 (SD-001〜SD-007, Governance) から確認できる範囲で個別 Screen Requirement として記述する。
- 利用者が Search Criteria を指定・確認・変更するための要件を定義する。
- 未定義の入力項目・必須条件・バリデーション・検索ロジック等は補完せず、Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- SCR-003 の責務を具体的な検索フォーム・入力項目・検索ロジックへ具体化しない。SCR-003 を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

## 2. Related Screen Matrix Candidates

- **SCR-003 Accommodation Search** ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5) — 唯一の対応画面候補。
- 本文書は SCR-003 に既に定義された責務と利用者タスクのみを扱う。
- 条件入力・確認・変更が同一画面になるか複数画面へ分かれるか、およびエラー・中断専用画面の要否は確定しない (§16 Open Issues)。
- User は Supporting IA Object として参照し、認証・会員・履歴保存の機能を取り込まない。
- SCR-001 Service Entry からの入口や SCR-004 Search Results への接続可能性と、具体的な画面遷移を混同しない。SCR-001・SCR-004 の内部要件を取り込まない (§16 Open Issues)。
- 本文書の作成単位 (SCR-003 単独) は、未決事項を保持したまま作成可能な範囲を文書化するための暫定的な作成単位であり、将来の分割・統合判断により文書構成が変更され得る。本文書の作成順は、探索候補群の正式な作成順を確定するものではない ([creation-plan.md](creation-plan.md) §10)。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は SCR-003 Accommodation Search を画面候補 (Status: Draft) として管理する。
- レイヤー入口 [README.md](README.md)、作成順序評価 [creation-plan.md](creation-plan.md)、先行する個別要件 [service-entry.md](service-entry.md) (SCR-001) / [help-and-support.md](help-and-support.md) (SCR-013) / [editorial-content.md](editorial-content.md) (SCR-014) が存在する。
- [creation-plan.md](creation-plan.md) は SCR-003 を `Partial` / `Near-term`、分割/統合の指摘なし、SCR-004 の前提と評価する (§6・§10)。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は SCR-003 の要件を、上流成果物から確認できる範囲で記述する。
- 作成単位を SCR-003 単独とする (暫定。§2)。
- Search Criteria・Destination を Primary IA Objects、User を Supporting IA Object として扱い、主従を逆転しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-003)。
- 未定義の入力項目・必須条件・バリデーション・検索ロジックは推測で補完せず Open Issue として保持する (UXDR-TRAVEL-001)。
- Navigation と CTA を別責務として記述する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities と一致)。
- ファイル名 `accommodation-search.md` は暫定であり、正式命名規則を確定しない。

### Hypotheses

- なし。

### Open Issues

- Search Criteria を構成する入力項目・必須条件・バリデーション。
- 条件保持・復元の方式と期間。
- SCR-001 からの接続、SCR-004 への接続。
- Screen Requirement ID 体系・ファイル命名規則。
- (詳細は §16 に集約)

## 4. User Tasks

[Screen Matrix](../service-design/screen-matrix.md) §5 SCR-003 の Primary User Tasks を上流参照する (再定義しない)。

- 検索条件を指定・確認・変更する。

上位基準として SDP-001 User Task Clarity (利用者が現在何を行い、次に何を行えるかを理解できる) と SDP-002 Progressive Commitment (必要以上に早い入力・確約を求めない) を適用する。どの検索条件を扱うかは確定しない (§16 Open Issues)。

## 5. Information Responsibilities

[Information Architecture](../service-design/information-architecture.md) (SD-002) を上流参照する。IA オブジェクトの定義・追加・変更は行わない。Screen Matrix §5 SCR-003 の Primary / Supporting の区別を保つ。

### Primary IA Objects

- **IA-OBJ-002 Search Criteria** — 利用者の探索意図を条件として保持し、候補の絞り込み・評価の入力となる観点を扱う。具体的な入力項目・必須条件は確定しない (IA-OBJ-002 Does Not Decide)。
- **IA-OBJ-001 Destination** — Search Criteria が参照する地理/目的地の観点を扱う。階層構造・指定方法は確定しない (IA-OBJ-001 Open Issue)。

### Supporting IA Objects

- **IA-OBJ-011 User** — Search Criteria を使用する主体として補助的に参照する。会員制度・認証・識別方法・履歴保存を前提にしない (IA-OBJ-011 Open Issue)。

Supporting IA Object (User) から、認証・会員・履歴保存の機能を取り込まない。Primary と Supporting の主従を逆転しない ([../service-design/information-architecture.md](../service-design/information-architecture.md) §5 IA-OBJ-002 Relationships「User が Search Criteria を使用する / Search Criteria は Destination を参照する」)。

## 6. Functional Requirements

上流成果物から確認できる能力・責務のみを記述する。業務仕様が未定義の事項は要件化せず Open Issue とする ([README.md](README.md) §6)。

- 利用者が Search Criteria を指定できること (SDP-001, NAV-004 Task Navigation)。
- 利用者が現在指定されている Search Criteria を確認できること (SDP-005 State Visibility, NVP-001 Current Location Visibility)。
- 利用者が Search Criteria を変更できること (SDP-002 Progressive Commitment, NAV-004)。
- Search Criteria と関連する Destination を識別できること (IA-OBJ-002 / IA-OBJ-001, CTP-005 Consistent Terminology)。
- 検索開始前に、現在の条件と実行する行動を理解できること (CTA-001 Action Clarity, CTA-005 Conditions Before Action)。
- 条件変更時に、既存の文脈を不必要に失わせないこと (NVP-003 Preserved Context, NAV-005 History and Recovery Navigation)。
- 中断または誤操作後に、条件指定・確認・変更へ戻れること (SDP-006 Recoverability, NVP-004 Reversible Movement)。
- 利用不能・未確定・不正な状態がある場合、その状態を識別できること (SDP-005, CTA-007 Explicit State and Availability)。
- User を参照する場合も、認証・会員・履歴保存を前提にしないこと (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。

以下は要件として確定しない (Open Issue として §16 で扱う)。

- Search Criteria を構成する具体的項目。
- 各項目の必須・任意。
- 入力形式・選択肢・初期値。
- 項目間依存。
- バリデーション条件。
- 検索成立条件。
- 条件の保存方式・保存期間。
- 検索結果へ渡す具体的なデータ。

## 7. Content Requirements

[Content Principles](../service-design/content-principles.md) (SD-004) の Content Category と原則を上流参照する。SCR-003 の Content Categories は Task Guidance / Identification ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-003)。

- **Task Guidance** — 利用者が次に可能な操作を理解できる案内を提供する (CTP-001 Purpose Before Detail, CTP-002 Plain and Direct Language, CTP-007 Actionable Error and Recovery)。
- **Identification** — 現在の検索条件と、その目的を識別可能にする (CTP-002, CTP-005 Consistent Terminology)。
- 条件名・状態・行動の用語を一貫させる (CTP-005 Consistent Terminology, NVP-005 Consistent Meaning)。
- 必須・任意、利用可能・利用不能、未確定等の状態を、定義されていないまま確定表現しない (CTP-006 Explicit State and Uncertainty)。
- 入力や選択の結果を予測可能にする (CTP-001, NVP-002 Predictable Destination)。
- エラー・中断時に、問題と回復可能な行動を理解可能にする (CTP-007 Actionable Error and Recovery)。
- 情報の意味を色・アイコン・位置だけに依存させない (CTP-008 Accessible and Scannable Content)。

具体的なラベル・プレースホルダー・説明文・エラー文言・ブランドトーンは決定しない (§13 Does Not Decide)。

## 8. Navigation Requirements

[Navigation](../service-design/navigation.md) (SD-003) を上流参照する。SCR-003 の Navigation Types は NAV-004 / NAV-005 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-003)。2 分類を責務として区別して記述する。

- **NAV-004 Task Navigation**
  - 条件指定・確認・変更・検索開始というタスク進行を理解可能にする。
  - 現在の段階と次に可能な行動を理解可能にする (NVP-001 Current Location Visibility)。
  - 必要以上に早い入力・登録・確約を要求しない (SDP-002 Progressive Commitment)。正式なタスク一覧は確定しない (NAV-004 Does Not Decide)。
- **NAV-005 History and Recovery Navigation**
  - 条件変更時に既存の探索文脈を不必要に失わせない (NVP-003 Preserved Context)。
  - 誤操作・中断後に合理的な前状態へ戻れるようにする (NVP-004 Reversible Movement)。
  - 再入力が必要になる場合も、その理由や影響を確認可能にする。保持方式は確定しない (NAV-005 Does Not Decide)。
- 移動先または行動結果を事前に予測可能にする (NVP-002 Predictable Destination)。
- 内部組織やシステム都合ではなく利用者タスクを基準にする (NVP-006 Task over Organization)。
- Navigation と CTA を同一責務として扱わない (UXDR-TRAVEL-003, §9)。

具体的な戻る操作・履歴 UI・ステップ表示・画面遷移は決定しない (§13 Does Not Decide)。

## 9. CTA Requirements

[CTA Principles](../service-design/cta-principles.md) (SD-005) を上流参照する。SCR-003 に関する記述は [../service-design/cta-principles.md](../service-design/cta-principles.md) §7 Relationship with Screen Matrix の SCR-003 行 (CTA Consideration「条件入力・変更・検索開始を明確にする」)。Navigation と CTA は別責務とする (UXDR-TRAVEL-003)。

- 条件入力・変更・検索開始の行動を区別する (CTA-001 Action Clarity)。
- 行動の対象と結果を実行前に理解可能にする (CTA-001)。
- 検索開始前に、適用される Search Criteria を確認可能にする (CTA-005 Conditions Before Action)。
- 理解・確認より前に不要な入力・登録・確約を要求しない (CTA-004 Progressive Commitment)。
- 利用不能な行動の状態を曖昧にしない (CTA-007 Explicit State and Availability)。
- 入力項目や成立条件が未定義の場合、具体的な主要 CTA を確定しない (SDP-010 Incremental Definition)。
- Navigation Action を自動的に主要 CTA として扱わない ([../service-design/cta-principles.md](../service-design/cta-principles.md) §8 Boundary between CTA and Navigation)。
- CTA の意味・状態・実行可能性を視覚だけに依存させない (CTA-009 Accessible Activation)。

具体的な CTA 文言・数・優先順位・配置・色・Component は決定しない (§13 Does Not Decide)。

## 10. State and Feedback Requirements

対象状態は [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-003 に存在する Entry, Exploring, Error / Interrupted のみとする。[Navigation](../service-design/navigation.md) §6 Navigation State Model を上流参照する。`Error / Interrupted` は上流 Navigation State の複合名として扱い、`Error` と `Interrupted` という別々の新規状態へ再定義しない。

- **Entry** — 条件指定タスクへ到達したことを理解できること。
- **Exploring** — 条件を指定・確認・変更している状態を理解できること (NVP-003 Preserved Context)。
- **Error / Interrupted** — タスクが進行できない、または中断したことと、回復可能な行動を理解できること (SDP-006 Recoverability, CTP-007 Actionable Error and Recovery)。
- 条件変更後に、現在適用されている状態を確認できること (SDP-005 State Visibility)。
- 状態変化を色・位置・アニメーションだけで伝えないこと (SDP-007, CTP-008)。
- `Evaluating`・`Committing`・`Completed` 等を、SCR-003 の確定状態として独断で追加しないこと ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-003 は Entry, Exploring, Error / Interrupted のみを定義)。

具体的なエラー種別・検証条件・処理状態は決定しない (§13 Does Not Decide)。

## 11. Accessibility Requirements

SDP-007 Accessibility by Default / NVP-008 Accessible Navigation / CTP-008 Accessible and Scannable Content / CTA-009 Accessible Activation の範囲で記述する。

- キーボード・支援技術・異なる画面サイズを例外扱いしない (SDP-007, NVP-008)。
- 条件の名称・入力/選択の目的・現在値・状態を支援技術で理解可能にする (CTP-008)。
- Navigation と CTA の意味・状態を視覚だけで伝えない (NVP-008, CTA-009)。
- エラー・中断時に問題と回復方法を理解可能にする (CTP-007)。
- 読む順序・操作順序・意味の関係を画面サイズによって失わせない (CTP-008)。
- モバイルでも条件指定・確認・変更・回復を可能にする (SDP-007)。

具体的な規格・達成レベル・HTML 属性・フォーカス実装・Component 仕様は決定しない (§13 Does Not Decide)。

## 12. Constraints

- 上流成果物 (SD-001〜SD-007) の定義を再定義・変更しない ([README.md](README.md) §9)。
- 作成単位は SCR-003 単独に限定し、Supporting IA Object (User) から認証・会員・履歴保存機能を、SCR-001・SCR-004 から内部要件を取り込まない (§2, §5)。
- 未定義事項を Fact または Decision として扱わず、Open Issue として保持する (SDP-008 Evidence over Assumption, UXDR-TRAVEL-001)。
- 確定可能な範囲からのみ記述し、未決事項へ依存する要件を確定しない (SDP-010 Incremental Definition)。
- サービス全体の整合性と一貫した概念・用語を優先する (SDP-004 Consistent Mental Model, SDP-009 Service-wide Coherence)。

## 13. Does Not Decide

本文書だけでは以下を確定しない。

- 具体的な検索フォーム・入力項目・必須条件・バリデーション・UI ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-003 Does Not Decide)。
- 各項目の必須・任意、初期値・選択肢・入力形式、項目間依存。
- バリデーション条件・エラーメッセージ、検索ロジック・検索 API・DB。
- 在庫・料金との照合、検索履歴・保存条件・保存期間。
- 認証・会員との関係、SCR-004 へ渡す具体的なデータ。
- 条件入力・確認・変更の画面分割/統合、モーダル・ドロワー・フォーム・検索バー等の UI。
- URL・route・クエリパラメータ・サイトマップ・画面遷移、エラー・中断専用画面の要否。
- CTA 文言・配置・色・数・Component。
- Screen Requirement ID 体系・ファイル命名規則。

## 14. Upstream References

上流成果物は [README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。定義を本文書で変更しない。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — SDP-001 User Task Clarity / SDP-002 Progressive Commitment / SDP-004 Consistent Mental Model / SDP-005 State Visibility / SDP-006 Recoverability / SDP-007 Accessibility by Default / SDP-008 Evidence over Assumption / SDP-009 Service-wide Coherence / SDP-010 Incremental Definition。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — Primary: IA-OBJ-002 Search Criteria / IA-OBJ-001 Destination。Supporting: IA-OBJ-011 User。
- **SD-003 [Navigation](../service-design/navigation.md)** — NAV-004 Task Navigation / NAV-005 History and Recovery Navigation、NVP-001 Current Location Visibility / NVP-002 Predictable Destination / NVP-003 Preserved Context / NVP-004 Reversible Movement / NVP-005 Consistent Meaning / NVP-006 Task over Organization / NVP-008 Accessible Navigation、Navigation State Model (Entry, Exploring, Error / Interrupted)。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Categories: Task Guidance / Identification、CTP-001 Purpose Before Detail / CTP-002 Plain and Direct Language / CTP-005 Consistent Terminology / CTP-006 Explicit State and Uncertainty / CTP-007 Actionable Error and Recovery / CTP-008 Accessible and Scannable Content。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA-001 Action Clarity / CTA-004 Progressive Commitment / CTA-005 Conditions Before Action / CTA-007 Explicit State and Availability / CTA-009 Accessible Activation、§7 Relationship with Screen Matrix の SCR-003 行、§8 Boundary between CTA and Navigation。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — SCR-003 Accommodation Search の責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements / UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens / UXDR-TRAVEL-003 Keep Navigation and CTA as Separate Design Responsibilities。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 15. Downstream Impact

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 本 Screen Requirement の下流に位置する。既存 Design System を参照して実現可能性や未整備箇所を確認できるが、既存の Input・Select・Button 等を前提に上流要件を変形しない。具体的な Component・レイアウト・トークン・入力形式を指定しない。既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。
- **Implementation** — Repository の管理対象外。本文書だけで実装仕様を確定しない。SCR-003 を実装 1 画面・URL・route と同一視しない (UXDR-TRAVEL-002)。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。各 Open Issue が影響する要件節を可能な範囲で示す。

- **Search Criteria を構成する入力項目** — §5 Information Responsibilities, §6 Functional Requirements。
- **各項目の必須・任意** — §6, §7 Content Requirements。
- **初期値** — §6。
- **入力形式・選択肢** — §6。
- **項目間依存** — §6。
- **バリデーション条件** — §6, §10 State and Feedback Requirements。
- **検索成立条件** — §6, §9 CTA Requirements。
- **エラー種別・エラー文言** — §7, §10。
- **Destination の指定方法** — §5, §6。
- **条件の確認・変更単位** — §6, §8 Navigation Requirements。
- **条件保持・復元の方式と期間** — §8 (NAV-005)。
- **Search Criteria と User の関係** — §5。
- **認証前後・会員種別による差** — §5, §6。
- **SCR-001 からの接続** — §2, §8。
- **SCR-004 への接続** — §2, §6, §8。
- **エラー・中断専用画面の要否** — §2, §10。
- **URL・route・クエリパラメータ・画面遷移** — §6, §13。
- **モバイル時の具体的な入力・選択方式** — §8, §11 Accessibility Requirements。
- **Screen Requirement ID 体系** — 文書全体 ([README.md](README.md) §7)。
- **ファイル命名規則** — 本文書のファイル名 `accommodation-search.md` は暫定 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — §17 Acceptance Criteria。
- **Design System への反映確認方法** — §15 Downstream Impact ([README.md](README.md) §17)。

## 17. Acceptance Criteria

未定義の UI・業務仕様を確定しない範囲で記述する。最終確定主体は Open Issue として維持する (§16)。

- 文書が [README.md](README.md) §6 Common Document Structure を満たしている。
- Related Screen Matrix Candidate が SCR-003 として追跡可能であり、SCR-003 のみである。
- [Screen Matrix](../service-design/screen-matrix.md) §5 SCR-003 の Responsibility・Primary User Tasks・Primary IA Objects・Supporting IA Objects・Navigation Types・Content Categories・Navigation States と一致している。
- Search Criteria・Destination を Primary、User を Supporting として扱い、主従を逆転していない (§5)。
- User の補助参照から認証・会員・履歴保存機能を推測していない (§5)。
- Navigation と CTA の要件が別節・別責務として記述されている (§8, §9)。
- NAV-004 と NAV-005 の責務を混同していない (§8)。
- 状態が Entry, Exploring, Error / Interrupted のみであり、`Error / Interrupted` を複合状態名として扱い、未定義状態を独断で追加していない (§10)。
- 入力項目・必須条件・バリデーションを確定していない (§6, §13)。
- SCR-001・SCR-004 の内部要件を取り込んでいない (§2)。
- URL・route・UI・Component・API・DB を確定していない (§13, §15)。
- 未定義の要求が Open Issue として追跡でき、上流成果物の ID・正式名称を追跡できる (§14, §16)。
- 下流 Design System との関係が Downstream Impact へ分離されている (§15)。
- 文書 Status が Draft である。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial draft of Travel Accommodation Search Screen Requirement (SCR-003) | Draft |
