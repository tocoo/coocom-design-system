# Travel Screen Requirement Creation Plan

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の個別 Screen Requirement 作成に先立つ、Screen Matrix 14 画面候補 (SCR-001〜SCR-014) の作成単位・着手可否・作成順序の評価
- Position in Repository: `services/travel/screen-requirements/creation-plan.md` — Screen Requirements レイヤー (travel サービス配下)。レイヤー入口は [README.md](README.md)。上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Design System / Implementation) との関係は §14 を参照。

本文書は評価・計画文書であり、個別の画面要件そのものは定義しない。評価上の着手可否と、画面候補・個別要件の正式 Status を混同しない。

## 1. Purpose

- 個別 Screen Requirement の作成を開始する前に、[Screen Matrix](../service-design/screen-matrix.md) (SD-006) の 14 画面候補 (SCR-001〜SCR-014) を、上流成果物の充足状況・未定義事項への依存・候補間依存・分割/統合の未決度の観点で評価する。
- 評価結果から、推測を伴わずに個別要件を作成できる最初の対象と、後続の作成順序を判断できる状態を作る。
- 「作成順序を評価する」ことと「画面仕様・分割/統合・作成単位を確定する」ことを区別する。後者は本文書では確定しない。

本文書は、レイヤー入口 [README.md](README.md) §12 Creation Order が「作成順そのものを Open Issue とする」とした未決事項に対し、確定ではなく評価と推奨を与える。正式な確定は上流・業務要求の充足後に別途行う。

## 2. Scope

### Assessed

- SCR-001〜SCR-014 の全件評価。
- 各候補が利用可能な上流根拠 (SD-001〜SD-007, Governance)。
- 各候補が依存する未定義事項。
- 候補間の依存関係。
- 分割・統合判断の必要性の有無。
- 現時点で推測なく文書化できる範囲。
- 個別要件作成の着手可否。
- 推奨作成順序と最初に作成すべき候補。
- 着手前に解決が必要な Open Issue と後続タスクの開始条件。

### Not Assessed / Not Decided

- 個別 Screen Requirement 文書の作成。
- Screen Requirement ID・ファイル命名規則の正式採用。
- Screen Matrix の 14 候補の追加・削除・改名。
- 分割・統合の正式決定。
- 実装画面数・URL・route・サイトマップ・画面遷移の確定。
- UI・レイアウト・ワイヤーフレーム・Component 仕様。
- 入力項目・バリデーション・API・DB・状態遷移の補完。
- 予約・決済・認証・会員・変更・取消等の業務仕様の補完。
- 上位事業要求・KPI・マーケティング要求の推測。
- Service Design / Design System / Governance 本文の変更、UX Decision Record の追加。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- [Screen Matrix](../service-design/screen-matrix.md) (SD-006) は 14 画面候補 (SCR-001〜SCR-014) を Draft として管理する。
- レイヤー入口 [README.md](README.md) は `In preparation` として存在する。着手可能候補の個別 Screen Requirement (SCR-001〜SCR-005・SCR-013・SCR-014) が `Draft` として存在し、SCR-006〜SCR-012 は未作成 (`Not started`) である。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §2 Facts)。
- Design System は既存資産 (Draft) として存在する ([../design-system/](../design-system/))。

### Decisions

- 本文書は評価と推奨を管理する。個別画面仕様・分割/統合・作成単位・ID 体系・命名規則は確定しない。
- 評価は上流成果物 (SD-001〜SD-007) と Governance の実在する記述のみを根拠とする。
- 未定義の事業・業務・機能・画面仕様は、推測で補完せず Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 Preserve Unknowns Instead of Inventing Requirements と一致)。
- 画面候補を実装上の 1 画面・URL・route と同一視しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002 Separate Conceptual Screen Candidates from Implemented Screens と一致)。

### Hypotheses

- なし。

### Open Issues

- 個別 Screen Requirement 文書の作成単位。
- 各候補の分割・統合。
- 個別文書の作成順の正式確定。
- Screen Requirement ID 体系とファイル命名規則。
- (詳細は §15 に集約)

## 4. Assessment Method

- [README.md](README.md) §12 Creation Order が列挙する 7 つの決定基準 (§5) を、各画面候補へ記述で適用する。
- 各評価の根拠として、[Screen Matrix](../service-design/screen-matrix.md) の該当行・節と、参照する上流成果物のファイル・ID・正式名称を明示する。
- 上流成果物にない要求を評価者が補完しない。根拠が確認できない事項は Open Issue とする。
- Screen Matrix の記載 (責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States) を変更・拡張せず、評価根拠として引用する。
- Design System は下流成果物として、既存の実現可能性や未整備箇所を確認する場合に限り参照し、その記述を上流要求へ昇格させない ([README.md](README.md) §10)。

## 5. Assessment Criteria

[README.md](README.md) §12 Creation Order に存在する以下の基準を使用する。新しい評価方針名や正式なスコアリング制度は作らない。Repository 内に根拠となる数値尺度が存在しないため、数値評価は用いず、各項目を根拠付きの記述で評価する。

1. 上流成果物の定義充足度。
2. 未定義の事業要求・業務仕様への依存度。
3. 他候補との依存関係。
4. 分割・統合の未決度。
5. 利用者タスク上の位置。
6. 下流設計へ与える影響。
7. Open Issue の数と重大性。

### Draftable Without Assumption の区分

§6 の `Draftable Without Assumption` 列および §7 では、次の 3 区分で説明する。これは評価上の区分であり、正式な Status 名や個別成果物の Status として登録しない。画面候補の Status は Screen Matrix の `Draft` である。個別要件の Status は評価当初 (2026-07-15) には全件 `Not started` であったが、現在は §10・§11 の実行状況注記のとおり一部が `Draft` である (SCR-006〜SCR-012 は `Not started`)。`Draftable Without Assumption` の区分 (Mostly / Partial / Premature) は評価当時の着手可否の説明であり、成果物の Status ではない。

- **Mostly** — 現在の上流根拠だけで [README.md](README.md) §6 Common Document Structure の大部分を推測なく記述できる。
- **Partial** — 一部は記述できるが、重要部分が Open Issue になる。
- **Premature** — 中核要件が未定義であり、現時点の着手は適切でない。

## 6. Candidate Assessment Matrix

SCR ID・Screen Candidate・責務は [Screen Matrix](../service-design/screen-matrix.md) §4 の記載を引用する (変更しない)。Navigation States の値 `Error / Interrupted` は複合名であり、区切りのスラッシュではない。

| SCR ID | Screen Candidate | Available Upstream Evidence | Undefined Dependencies | Cross-candidate Dependencies | Split / Merge Consideration | Draftable Without Assumption | Remaining Open Issues | Suggested Sequence | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCR-001 | Service Entry | SDP-001/009, IA-OBJ-001/002/012, NAV-001/004/006, Content: Identification・Task Guidance・Editorial and Support, States: Entry・Exploring, CTA §7 SCR-001 | Global Navigation 対象領域, 会員・非会員の Navigation 差 | SCR-002/SCR-003 へ導線を持つが、それらの内部要件確定を前提としない | SCR-002 との境界が Open Issue (Matrix §9) | Mostly | Global Nav 対象領域, SCR-001/002 境界 | First | 上流充足度が高く、状態が Entry・Exploring に限られ予約・決済・認証・会員の業務仕様に依存しない。他候補の確定を待たずに共通構造の大部分を記述できる |
| SCR-002 | Destination Discovery | SDP-001, IA-OBJ-001/012, NAV-001/002/003, Content: Identification・Editorial and Support, States: Exploring, CTA §7 SCR-002 | Destination の階層構造 (IA-OBJ-001 Open Issue), Content の分類 (IA-OBJ-012 Open Issue) | SCR-001 と入口責務が隣接, SCR-004 へ探索を接続 | SCR-001 との境界が Open Issue (Matrix §9) | Partial | Destination 階層, Content 分類, SCR-001/002 境界 | Near-term | 探索段階で業務仕様に依存しないが、中核の Destination 階層と Content 分類が未定義 |
| SCR-003 | Accommodation Search | SDP-001/002, IA-OBJ-002/001, NAV-004/005, Content: Task Guidance・Identification, States: Entry・Exploring・Error / Interrupted, CTA §7 SCR-003 | 入力項目・必須条件・バリデーション (Matrix SCR-003 Does Not Decide) | SCR-004 へ検索結果を接続 | 単独。分割/統合の指摘なし | Partial | 検索の入力項目・必須条件・バリデーション | Near-term | Search Criteria オブジェクトと Task Navigation は定義済だが、Functional Requirements に相当する入力仕様が未定義で Open Issue になる |
| SCR-004 | Search Results | SDP-001/003/009, IA-OBJ-002/003 (+006/007/009/008 supporting), NAV-002/003/004/005, Content: Identification・Decision Support・Conditions and Policies, States: Exploring・Evaluating・Error / Interrupted, CTA §7 SCR-004 | 一覧・並び替え・絞り込み (Matrix SCR-004 Does Not Decide), Price/Availability/Review の表示基準 | SCR-003 の検索条件に依存, SCR-005 へ詳細を接続 | 単独。分割/統合の指摘なし | Partial | 並び替え・絞り込み基準, 評価/価格/在庫の表示基準 | Near-term | 候補比較の責務は上流で定義されるが、比較を成立させる並び替え・絞り込み・表示基準が未定義 |
| SCR-005 | Accommodation Detail | SDP-001/003, IA-OBJ-003 (+001/004/005/009/008/012 supporting), NAV-002/003/004/006, Content: Identification・Decision Support・Conditions and Policies・Editorial and Support, States: Evaluating・Error / Interrupted, CTA §7 SCR-005 | Room/Stay Plan/Price の業務モデル (IA Open Issue), Review の提供元・評価対象 (IA-OBJ-009 Open Issue) | SCR-004 から遷移, SCR-006 へ選択を接続 | SCR-006 との境界が Open Issue (Matrix §9) | Partial | Room/Stay Plan/Price 業務モデル, Review 基準, SCR-005/006 境界 | Near-term | 中核の Accommodation は定義が厚いが、詳細で扱う関連オブジェクトの業務モデルが未定義で、SCR-006 との境界も未決 |
| SCR-006 | Room and Plan Selection | SDP-002/003, IA-OBJ-004/005 (+003/006/007/008 supporting), NAV-002/003/004/005, Content: Decision Support・Conditions and Policies・Identification, States: Evaluating・Committing・Error / Interrupted, CTA §7 SCR-006 | Room/Stay Plan/Availability/Price の正式業務関係 (IA Open Issue), 選択・在庫・価格提示 | SCR-005 から遷移, SCR-007 へ予約を接続 | SCR-005 との境界が Open Issue (Matrix §9) | Premature | Stay Plan/Room/Price/Availability 業務モデル, 選択の確約レベル | Await business spec | Committing へ入る中核選択が Stay Plan・在庫・料金の業務モデルに依存し、いずれも IA で Open Issue |
| SCR-007 | Booking Details | SDP-002/005, IA-OBJ-010/011 (+003/004/005/007/008 supporting), NAV-004/005/006, Content: Task Guidance・Conditions and Policies・Identification, States: Committing・Error / Interrupted, CTA §7 SCR-007 | 入力項目・バリデーション・認証・決済 (Matrix SCR-007 Does Not Decide), User 分類 (IA-OBJ-011 Open Issue) | SCR-006 から遷移, SCR-008 へ接続 | Booking Details/Review 境界が Open Issue (Matrix §9) | Premature | 認証・決済・入力仕様, 会員/非会員の区別 | Await business spec | 予約情報入力の中核が認証・決済・会員仕様に依存し、いずれも未定義 |
| SCR-008 | Booking Review | SDP-002/003, IA-OBJ-010 (+011/003/004/005/007/008 supporting), NAV-004/005/006, Content: Identification・Conditions and Policies・Task Guidance, States: Committing・Error / Interrupted, CTA §7 SCR-008 | 確約操作・予約成立条件 (CTA-003 Does Not Decide), Price/Policy 表示基準 | SCR-007 から遷移, SCR-009 へ結果を接続 | Booking Details/Review 境界が Open Issue (Matrix §9) | Premature | 確約レベル, 予約成立条件, Price/Policy 表示 | Await business spec | 確約前確認の中核が予約成立条件・確約レベルに依存し未定義 |
| SCR-009 | Booking Result | SDP-005/006, IA-OBJ-010 (+003/004/005/007/008 supporting), NAV-003/004/006, Content: Status and Feedback・Task Guidance・Identification, States: Completed・Error / Interrupted, CTA §7 SCR-009 | 予約処理結果・後続導線 (Matrix SCR-009 Does Not Decide), Booking の状態 (IA-OBJ-010 Open Issue) | SCR-008 の確約結果に依存, SCR-010 へ接続し得る | Booking Result 後の Navigation が Open Issue (Matrix §9) | Premature | 予約処理結果, Booking 状態, 後続 Navigation | Await business spec | 結果表示の中核が Booking の状態・予約処理結果に依存し未定義 |
| SCR-010 | Booking Management | SDP-004/009, IA-OBJ-010 (+011/003/004/005/007/008 supporting), NAV-001/002/003/004/006, Content: Identification・Status and Feedback・Conditions and Policies・Task Guidance, States: Entry・Evaluating・Completed・Error / Interrupted, CTA §7 SCR-010 | MyPage 構成・会員範囲・提供機能 (Matrix SCR-010 Does Not Decide) | SCR-009/SCR-011/SCR-012 と関連 | Booking Management の提供範囲が Open Issue (Matrix §9) | Premature | MyPage 構成, 会員範囲, 認証との関係 | Await business spec | 管理領域の中核が MyPage 構成・会員範囲・認証に依存し未定義 |
| SCR-011 | Booking Change or Cancellation | SDP-003/006, IA-OBJ-010/008 (+011/003/004/005/007 supporting), NAV-002/004/005/006, Content: Conditions and Policies・Task Guidance・Status and Feedback, States: Evaluating・Committing・Completed・Error / Interrupted, CTA §7 SCR-011 | 変更・取消の業務範囲・条件・手数料 (Matrix SCR-011 Does Not Decide), Policy 分類 (IA-OBJ-008 Open Issue) | SCR-010 と関連 | 変更・取消の業務範囲が Open Issue (Matrix §9) | Premature | 変更・取消の業務範囲・手数料, Policy 分類 | Await business spec | 変更・取消の中核が業務範囲・手数料・Policy 分類に依存し未定義 |
| SCR-012 | User Access | SDP-002, IA-OBJ-011 (+010 supporting), NAV-001/004/006, Content: Task Guidance・Identification, States: Entry・Committing・Error / Interrupted, CTA §7 SCR-012 | 認証方式・会員制度・識別方法 (Matrix SCR-012 は Status に「会員仕様は Open Issue」と明記) | SCR-010/SCR-007 の会員前提に影響し得る | 単独。ただし会員制度の要否が全 Booking 系へ波及 | Premature | 認証方式, 会員制度, 識別方法 | Await business spec | 中核が認証・会員制度に依存し、Matrix 自身が会員仕様を Open Issue と明記 |
| SCR-013 | Help and Support | SDP-001/006, IA-OBJ-012/008 (+011/010 supporting), NAV-001/002/003/006, Content: Editorial and Support・Conditions and Policies, States: Entry・Exploring・Error / Interrupted, CTA §7 SCR-013 | サポートチャネル・FAQ 構成・問い合わせ手段 (Matrix SCR-013 Does Not Decide) | 補助領域として独立性が高い。Booking/User は supporting 参照のみ | 対象範囲が Open Issue (Matrix §9) | Mostly | サポート対象範囲, 問い合わせ手段 | Near-term (independent) | 補助領域で予約チェーンの業務仕様に中核依存せず、上流の Content Category と Utility Navigation で責務を記述できる |
| SCR-014 | Editorial Content | SDP-003/008, IA-OBJ-012 (+001/003 supporting), NAV-001/002/003, Content: Editorial and Support・Identification, States: Entry・Exploring・Evaluating, CTA §7 SCR-014 | Content の分類・編集方針 (IA-OBJ-012 Open Issue) | 予約チェーンから独立。Destination/Accommodation は supporting 参照のみ | 分類が Open Issue (Matrix §9) | Mostly | Content 分類・編集方針 | Near-term (independent) | 予約チェーンから独立し、編集情報と販促の区別 (CTP-010) 等を上流で記述できる。ただし Content 分類は未定義 |

## 7. Candidate Assessments

各評価は [Screen Matrix](../service-design/screen-matrix.md) §5 の該当候補を引用根拠とし、記載を変更・拡張しない。Screen Matrix に定義済の責務・Primary User Tasks・Primary / Supporting IA Objects・Navigation Types・Content Categories・Navigation States は同文書 §4・§5 の値を引用する。

### SCR-001: Service Entry

- **Screen Matrix 定義済の責務**: サービスへの入口を提供する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-001)。
- **Primary User Tasks**: サービスの主要な選択肢を理解し、探索の起点に立つ。
- **Primary / Supporting IA Objects**: Primary = Destination (IA-OBJ-001) / Search Criteria (IA-OBJ-002) / Content (IA-OBJ-012)。Supporting = なし。
- **Navigation Types**: NAV-001 Global Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Identification / Task Guidance / Editorial and Support。
- **Navigation States**: Entry, Exploring。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「探索開始と補助導線を競合させない」。CTA-002 One Clear Primary Action / CTA-004 Progressive Commitment を上位基準として参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-002 により入口を実装 1 画面・URL と同一視しない。UXDR-TRAVEL-003 により入口の Navigation と CTA を別責務として扱う。
- **現時点で要件化できる事項**: 入口としての責務、探索起点の User Tasks、Identification / Task Guidance / Editorial and Support の Content 要件、Global/Task/Utility Navigation の要件、Entry・Exploring 状態の要件、アクセシビリティ (SDP-007 / NVP-008 / CTP-008 / CTA-009)。
- **要件化できない事項**: Global Navigation の対象領域 (NAV-001 Open Issue)、会員・非会員の Navigation 差、具体的な入口 UI・レイアウト・遷移・URL (Matrix SCR-001 Does Not Decide)。
- **必要な Open Issues**: Global Navigation 対象領域、SCR-001/SCR-002 の境界。
- **他候補より先または後に扱う理由**: 状態が Entry・Exploring に限られ、予約・決済・認証・会員の業務仕様に依存しない。他候補の内部要件確定を前提とせず着手でき、共通構造の大部分を推測なく記述できる。

### SCR-002: Destination Discovery

- **Screen Matrix 定義済の責務**: 目的地・エリア・関連 Content を発見する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-002)。
- **Primary User Tasks**: 目的地やエリアを発見し、候補探索へ進む。
- **Primary / Supporting IA Objects**: Primary = Destination (IA-OBJ-001) / Content (IA-OBJ-012)。Supporting = Accommodation (IA-OBJ-003)。
- **Navigation Types**: NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation。
- **Content Categories**: Identification / Editorial and Support。
- **Navigation States**: Exploring。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「発見・探索と販促誘導を混同しない」。CTP-010 / CTA-010 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の Destination 階層を推測しない。
- **現時点で要件化できる事項**: 発見・探索の責務、関連 Content への Contextual Navigation 要件、探索状態の要件。
- **要件化できない事項**: Destination の正式な階層構造 (IA-OBJ-001 Open Issue)、Content の分類 (IA-OBJ-012 Open Issue)、目的地の階層 UI・一覧構成・遷移 (Matrix SCR-002 Does Not Decide)。
- **必要な Open Issues**: Destination 階層、Content 分類、SCR-001/SCR-002 境界。
- **他候補より先または後に扱う理由**: 探索段階で業務仕様に依存しないが、中核の Destination 階層が未定義であり、SCR-001 と入口責務が隣接するため境界確認を要する。SCR-001 の後に扱うのが妥当。

### SCR-003: Accommodation Search

- **Screen Matrix 定義済の責務**: Search Criteria を入力・確認・変更する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-003)。
- **Primary User Tasks**: 検索条件を指定・確認・変更する。
- **Primary / Supporting IA Objects**: Primary = Search Criteria (IA-OBJ-002) / Destination (IA-OBJ-001)。Supporting = User (IA-OBJ-011)。
- **Navigation Types**: NAV-004 Task Navigation / NAV-005 History and Recovery Navigation。
- **Content Categories**: Task Guidance / Identification。
- **Navigation States**: Entry, Exploring, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「条件入力・変更・検索開始を明確にする」。CTA-001 / CTA-005 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の入力項目を推測しない。
- **現時点で要件化できる事項**: 条件指定・確認・変更の責務、条件保持と再探索の History and Recovery Navigation 要件、Error / Interrupted 状態の回復要件。
- **要件化できない事項**: 入力項目・必須条件・バリデーション・UI (Matrix SCR-003 Does Not Decide)。これらは Functional Requirements に相当し、業務仕様が未定義のため Open Issue となる ([README.md](README.md) §6)。
- **必要な Open Issues**: 検索の入力項目・必須条件・バリデーション。
- **他候補より先または後に扱う理由**: Search Criteria と Task Navigation は定義済だが、条件入力の中核仕様が未定義。SCR-004 の前提を提供するため、探索群の中で早い位置にあり得るが Functional Requirements は Open Issue となる。

### SCR-004: Search Results

- **Screen Matrix 定義済の責務**: 検索条件に対応する Accommodation 候補を確認・比較する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-004)。
- **Primary User Tasks**: 候補を確認・比較し、詳細検討へ進む。
- **Primary / Supporting IA Objects**: Primary = Search Criteria (IA-OBJ-002) / Accommodation (IA-OBJ-003)。Supporting = Availability (IA-OBJ-006) / Price (IA-OBJ-007) / Review (IA-OBJ-009) / Policy (IA-OBJ-008)。
- **Navigation Types**: NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-005 History and Recovery Navigation。
- **Content Categories**: Identification / Decision Support / Conditions and Policies。
- **Navigation States**: Exploring, Evaluating, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「比較・詳細確認・条件変更・選択の優先関係を整理する」。CTA-002 / CTA-005 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の並び替え・絞り込み基準を推測しない。
- **現時点で要件化できる事項**: 候補の確認・比較の責務、Decision Support の Content 要件、条件保持と再探索の Navigation 要件、Error / Interrupted 状態の要件。
- **要件化できない事項**: 一覧・並び替え・絞り込み UI・遷移 (Matrix SCR-004 Does Not Decide)、Price/Availability/Review の表示基準 ([../service-design/content-principles.md](../service-design/content-principles.md) Open Issues)。
- **必要な Open Issues**: 並び替え・絞り込み基準、評価・価格・在庫の表示基準。
- **他候補より先または後に扱う理由**: SCR-003 の検索条件に依存し、SCR-005 へ詳細を接続する。比較の責務は上流で定義されるが、比較を成立させる表示基準が未定義のため、SCR-003 の後に扱う。

### SCR-005: Accommodation Detail

- **Screen Matrix 定義済の責務**: Accommodation の情報と関連 Room、Stay Plan、Review、Policy を確認する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-005)。
- **Primary User Tasks**: 施設情報と関連情報を確認し、評価する。
- **Primary / Supporting IA Objects**: Primary = Accommodation (IA-OBJ-003)。Supporting = Destination (IA-OBJ-001) / Room (IA-OBJ-004) / Stay Plan (IA-OBJ-005) / Review (IA-OBJ-009) / Policy (IA-OBJ-008) / Content (IA-OBJ-012)。
- **Navigation Types**: NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Identification / Decision Support / Conditions and Policies / Editorial and Support。
- **Navigation States**: Evaluating, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「情報確認と Room / Stay Plan 選択を区別する」。CTA-004 / CTA-005 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の業務関係を推測しない。
- **現時点で要件化できる事項**: 施設の識別・評価の責務、関連情報への Contextual Navigation 要件、Decision Support / Conditions and Policies の Content 要件。
- **要件化できない事項**: Room/Stay Plan/Price の業務モデル (IA Open Issue)、Review の提供元・評価対象 (IA-OBJ-009 Open Issue)、詳細レイアウト・情報構成・遷移 (Matrix SCR-005 Does Not Decide)。
- **必要な Open Issues**: Room/Stay Plan/Price 業務モデル、Review 基準、SCR-005/SCR-006 境界。
- **他候補より先または後に扱う理由**: 中核の Accommodation は定義が厚いが、詳細で扱う関連オブジェクトの業務モデルが未定義で、SCR-006 との境界も未決。SCR-004 の後、SCR-006 の前に位置し得る。

### SCR-006: Room and Plan Selection

- **Screen Matrix 定義済の責務**: Room、Stay Plan、Availability、Price、Policy を比較・選択する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-006)。
- **Primary User Tasks**: 客室・プランを比較し、選択する。
- **Primary / Supporting IA Objects**: Primary = Room (IA-OBJ-004) / Stay Plan (IA-OBJ-005)。Supporting = Accommodation (IA-OBJ-003) / Availability (IA-OBJ-006) / Price (IA-OBJ-007) / Policy (IA-OBJ-008)。
- **Navigation Types**: NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-005 History and Recovery Navigation。
- **Content Categories**: Decision Support / Conditions and Policies / Identification。
- **Navigation States**: Evaluating, Committing, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「条件確認前に予約確約へ進ませない」。CTA-003 / CTA-004 / CTA-005 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の業務モデルを推測しない。
- **現時点で要件化できる事項**: 選択前の条件確認の責務 (CTA-005 Conditions Before Action)、Decision Support の Content 要件。
- **要件化できない事項**: Room/Stay Plan/Availability/Price の正式業務関係 (IA Open Issue)、選択 UI・価格表示・在庫表示・遷移 (Matrix SCR-006 Does Not Decide)。
- **必要な Open Issues**: Stay Plan/Room/Price/Availability 業務モデル、選択の確約レベル、SCR-005/SCR-006 境界。
- **他候補より先または後に扱う理由**: Committing へ入る中核選択が Stay Plan・在庫・料金の業務モデルに依存し、いずれも IA で Open Issue。業務仕様の確定を待つ。

### SCR-007: Booking Details

- **Screen Matrix 定義済の責務**: 予約条件、予約者・宿泊者情報等を確認・入力する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-007)。
- **Primary User Tasks**: 予約条件と当事者情報を確認・入力する。
- **Primary / Supporting IA Objects**: Primary = Booking (IA-OBJ-010) / User (IA-OBJ-011)。Supporting = Accommodation (IA-OBJ-003) / Room (IA-OBJ-004) / Stay Plan (IA-OBJ-005) / Price (IA-OBJ-007) / Policy (IA-OBJ-008)。
- **Navigation Types**: NAV-004 Task Navigation / NAV-005 History and Recovery Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Task Guidance / Conditions and Policies / Identification。
- **Navigation States**: Committing, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「入力継続・修正・中断の扱いを明確にする」。CTA-004 / CTA-006 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の認証・決済・入力仕様を推測しない。
- **現時点で要件化できる事項**: 入力途中の回復 (SDP-006) と状態可視性 (SDP-005) の方針レベルの考慮。
- **要件化できない事項**: 入力項目・バリデーション・認証・決済・UI (Matrix SCR-007 Does Not Decide)、User の分類 (IA-OBJ-011 Open Issue)。
- **必要な Open Issues**: 認証・決済・入力仕様、会員/非会員の区別。
- **他候補より先または後に扱う理由**: 予約情報入力の中核が認証・決済・会員仕様に依存し、いずれも未定義。業務仕様の確定を待つ。

### SCR-008: Booking Review

- **Screen Matrix 定義済の責務**: 予約対象、Price、Policy、入力内容を確約前に確認する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-008)。
- **Primary User Tasks**: 確約前に予約内容を確認する。
- **Primary / Supporting IA Objects**: Primary = Booking (IA-OBJ-010)。Supporting = User (IA-OBJ-011) / Accommodation (IA-OBJ-003) / Room (IA-OBJ-004) / Stay Plan (IA-OBJ-005) / Price (IA-OBJ-007) / Policy (IA-OBJ-008)。
- **Navigation Types**: NAV-004 Task Navigation / NAV-005 History and Recovery Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Identification / Conditions and Policies / Task Guidance。
- **Navigation States**: Committing, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「確約前に Price・Policy・対象・入力内容を確認可能にする」。CTA-003 / CTA-005 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の確約レベル・成立条件を推測しない。
- **現時点で要件化できる事項**: 確約前確認の責務 (CTA-003 Commitment-aware Emphasis) の方針レベルの考慮。
- **要件化できない事項**: 確認画面構成・確約操作・遷移 (Matrix SCR-008 Does Not Decide)、予約成立条件・確約レベル ([../service-design/cta-principles.md](../service-design/cta-principles.md) Open Issues)。
- **必要な Open Issues**: 確約レベル、予約成立条件、Price/Policy 表示。
- **他候補より先または後に扱う理由**: 確約前確認の中核が予約成立条件・確約レベルに依存し未定義。SCR-007 と連続し、業務仕様の確定を待つ。

### SCR-009: Booking Result

- **Screen Matrix 定義済の責務**: 予約処理の結果と次の行動を確認する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-009)。
- **Primary User Tasks**: 予約結果と次の行動を確認する。
- **Primary / Supporting IA Objects**: Primary = Booking (IA-OBJ-010)。Supporting = Accommodation (IA-OBJ-003) / Room (IA-OBJ-004) / Stay Plan (IA-OBJ-005) / Price (IA-OBJ-007) / Policy (IA-OBJ-008)。
- **Navigation Types**: NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Status and Feedback / Task Guidance / Identification。
- **Navigation States**: Completed, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「結果確認と次の行動を明確にする」。CTA-007 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の Booking 状態を推測しない。
- **現時点で要件化できる事項**: 結果と状態の可視性 (SDP-005 / CTP-006) の方針レベルの考慮。
- **要件化できない事項**: 結果表示・後続導線・UI (Matrix SCR-009 Does Not Decide)、Booking の状態 (IA-OBJ-010 Open Issue)。
- **必要な Open Issues**: 予約処理結果、Booking 状態、Booking Result 後の Navigation。
- **他候補より先または後に扱う理由**: 結果表示の中核が Booking の状態・予約処理結果に依存し未定義。SCR-008 の後続で、業務仕様の確定を待つ。

### SCR-010: Booking Management

- **Screen Matrix 定義済の責務**: 成立した Booking の確認・管理を行う ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-010)。
- **Primary User Tasks**: 成立済みの予約を確認・管理する。
- **Primary / Supporting IA Objects**: Primary = Booking (IA-OBJ-010)。Supporting = User (IA-OBJ-011) / Accommodation (IA-OBJ-003) / Room (IA-OBJ-004) / Stay Plan (IA-OBJ-005) / Price (IA-OBJ-007) / Policy (IA-OBJ-008)。
- **Navigation Types**: NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Identification / Status and Feedback / Conditions and Policies / Task Guidance。
- **Navigation States**: Entry, Evaluating, Completed, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「確認・変更・取消・Support を競合させない」。CTA-002 / CTA-006 を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の会員範囲を推測しない。
- **現時点で要件化できる事項**: 確認・管理・支援の Navigation を競合させない方針レベルの考慮。
- **要件化できない事項**: MyPage 構成・会員範囲・提供機能・UI (Matrix SCR-010 Does Not Decide)。
- **必要な Open Issues**: MyPage 構成、会員範囲、認証との関係。
- **他候補より先または後に扱う理由**: 管理領域の中核が MyPage 構成・会員範囲・認証に依存し未定義。SCR-012 の会員制度確定にも影響を受ける。業務仕様の確定を待つ。

### SCR-011: Booking Change or Cancellation

- **Screen Matrix 定義済の責務**: Booking の変更・取消を検討・実行する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-011)。
- **Primary User Tasks**: 予約の変更・取消を検討・実行する。
- **Primary / Supporting IA Objects**: Primary = Booking (IA-OBJ-010) / Policy (IA-OBJ-008)。Supporting = User (IA-OBJ-011) / Accommodation (IA-OBJ-003) / Room (IA-OBJ-004) / Stay Plan (IA-OBJ-005) / Price (IA-OBJ-007)。
- **Navigation Types**: NAV-002 Local Navigation / NAV-004 Task Navigation / NAV-005 History and Recovery Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Conditions and Policies / Task Guidance / Status and Feedback。
- **Navigation States**: Evaluating, Committing, Completed, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「影響が大きい行動を明確に区別する」。CTA-006 Reversible Before Irreversible / CTA-TYPE-005 Destructive or High-impact Action を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の変更・取消業務範囲を推測しない。
- **現時点で要件化できる事項**: 不可逆行動の区別 (CTA-006) と条件提示 (SDP-003) の方針レベルの考慮。
- **要件化できない事項**: 変更・取消の業務範囲・条件・手数料・UI (Matrix SCR-011 Does Not Decide)、Policy 分類 (IA-OBJ-008 Open Issue)。
- **必要な Open Issues**: 変更・取消の業務範囲・手数料、Policy 分類。
- **他候補より先または後に扱う理由**: 変更・取消の中核が業務範囲・手数料・Policy 分類に依存し未定義。業務仕様の確定を待つ。

### SCR-012: User Access

- **Screen Matrix 定義済の責務**: 認証、識別、会員・非会員に関連し得る入口を提供する。正式な会員仕様は決定しない ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-012)。
- **Primary User Tasks**: サービスへアクセスする (識別・認証に関連し得る)。
- **Primary / Supporting IA Objects**: Primary = User (IA-OBJ-011)。Supporting = Booking (IA-OBJ-010)。
- **Navigation Types**: NAV-001 Global Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Task Guidance / Identification。
- **Navigation States**: Entry, Committing, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「認証・登録を必要以上に早く要求しない」。CTA-004 Progressive Commitment を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の会員制度・認証方式を推測しない。
- **現時点で要件化できる事項**: 早すぎる確約を求めない方針 (SDP-002 / CTA-004) の考慮。
- **要件化できない事項**: 認証方式・会員制度・識別方法・UI (Matrix SCR-012 Does Not Decide)。Matrix SCR-012 の Status 自身が「会員仕様は Open Issue」と明記する。
- **必要な Open Issues**: 認証方式、会員制度、識別方法。
- **他候補より先または後に扱う理由**: 中核が認証・会員制度に依存し、Matrix 自身が会員仕様を Open Issue と明記。会員制度の要否は Booking 系候補 (SCR-007/SCR-010) にも波及するため、業務・事業判断の確定を待つ。

### SCR-013: Help and Support

- **Screen Matrix 定義済の責務**: FAQ、問い合わせ、問題解決、Policy 確認等を支援する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-013)。
- **Primary User Tasks**: 問題解決・条件確認の支援を得る。
- **Primary / Supporting IA Objects**: Primary = Content (IA-OBJ-012) / Policy (IA-OBJ-008)。Supporting = User (IA-OBJ-011) / Booking (IA-OBJ-010)。
- **Navigation Types**: NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-006 Utility Navigation。
- **Content Categories**: Editorial and Support / Conditions and Policies。
- **Navigation States**: Entry, Exploring, Error / Interrupted。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「問題解決・問い合わせ・戻り先を明確にする」。CTA-TYPE-004 Recovery Action / CTA-007 Explicit State and Availability を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義のサポートチャネルを推測しない。
- **現時点で要件化できる事項**: 問題解決・条件確認の支援の責務、Utility Navigation による補助情報への到達要件、Editorial and Support / Conditions and Policies の Content 要件、回復可能な行動の提示 (CTP-007)。
- **要件化できない事項**: サポートチャネル・FAQ 構成・問い合わせ手段・UI (Matrix SCR-013 Does Not Decide)。
- **必要な Open Issues**: サポート対象範囲、問い合わせ手段。
- **他候補より先または後に扱う理由**: 補助領域で予約チェーンの業務仕様に中核依存せず、Booking/User は supporting 参照のみ。上流の Content Category と Utility Navigation で責務を記述できるため、探索群と並行して独立に着手し得る。

### SCR-014: Editorial Content

- **Screen Matrix 定義済の責務**: 特集、ガイド、案内等の Content を提供する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §5 SCR-014)。
- **Primary User Tasks**: 特集・ガイド等の情報を読み、発見・理解する。
- **Primary / Supporting IA Objects**: Primary = Content (IA-OBJ-012)。Supporting = Destination (IA-OBJ-001) / Accommodation (IA-OBJ-003)。
- **Navigation Types**: NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation。
- **Content Categories**: Editorial and Support / Identification。
- **Navigation States**: Entry, Exploring, Evaluating。
- **CTA Principles との関係**: [../service-design/cta-principles.md](../service-design/cta-principles.md) §7「編集情報と予約・販促 CTA の性質を区別する」。CTP-010 Separate Fact, Decision, and Promotion / CTA-010 No Unsupported Pressure を参照できる。
- **UX Decision Records から受ける制約**: UXDR-TRAVEL-001 により未定義の Content 分類を推測しない。
- **現時点で要件化できる事項**: 編集情報提供の責務、編集情報と販促の区別 (CTP-010)、関連 Destination/Accommodation への Contextual Navigation 要件。
- **要件化できない事項**: コンテンツ分類・編集方針・UI (Matrix SCR-014 Does Not Decide)、Content の正式な分類・優先順位 (IA-OBJ-012 Open Issue)。
- **必要な Open Issues**: Content 分類・編集方針。
- **他候補より先または後に扱う理由**: 予約チェーンから独立し、Destination/Accommodation は supporting 参照のみ。編集情報と販促の区別を上流で記述できるため、探索群と並行して独立に着手し得る。ただし Content 分類は未定義。

## 8. Cross-candidate Dependencies

以下は候補間の依存関係の整理である。分割・統合や作成単位を確定するものではない。

- **探索・比較の連鎖**: SCR-001 → SCR-002 → SCR-003 → SCR-004 → SCR-005 は、入口から発見・条件指定・比較・詳細評価へと利用者タスクが接続する ([../service-design/information-architecture.md](../service-design/information-architecture.md) §6 Search relationship / Offering relationship)。後段の候補は前段の出力 (探索条件・候補) を前提とする。
- **予約の連鎖**: SCR-005 → SCR-006 → SCR-007 → SCR-008 → SCR-009 は、選択から予約入力・確認・結果へ接続する ([../service-design/information-architecture.md](../service-design/information-architecture.md) §6 Booking relationship)。SCR-006 以降は Stay Plan/Price/Availability/Booking の業務モデルに依存し、いずれも IA で Open Issue。
- **予約後の管理**: SCR-010 は SCR-009 の成立結果を前提とし、SCR-011 は SCR-010 の管理から変更・取消へ接続する。
- **会員制度の波及**: SCR-012 User Access の会員制度の要否は、SCR-007 (当事者情報入力)・SCR-010 (会員範囲) の前提に波及する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9「User Access と会員制度の関係」)。
- **補助領域の独立性**: SCR-013 Help and Support と SCR-014 Editorial Content は、Booking/User/Accommodation を supporting としてのみ参照し、予約チェーンの業務仕様に中核依存しない。相対的に独立して着手し得る。
- **入口責務の隣接**: SCR-001 Service Entry と SCR-002 Destination Discovery、および SCR-001 と SCR-003 (検索起点) は入口責務が隣接し、境界が Open Issue ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9)。

## 9. Split and Merge Considerations

[README.md](README.md) §8 の通り、画面候補と Screen Requirement 文書は 1 対 1 を前提としない。以下は分割・統合を検討する必要がある候補の整理であり、本文書では確定しない ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-002)。

- **SCR-001 / SCR-002 の境界**: 入口と目的地発見の責務が隣接する ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9)。1 文書に統合するか分割するかは未決。
- **SCR-005 / SCR-006 の境界**: 施設詳細と客室・プラン選択の境界が Open Issue ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9)。
- **SCR-007 / SCR-008 の境界**: 予約情報入力と確約前確認の境界が Open Issue ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9)。
- **エラー・中断専用画面の要否**: 複数候補が `Error / Interrupted` 状態を持つが、専用画面とするか各候補内で扱うかは未決 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9)。
- **会員・非会員の画面差**: SCR-012 と Booking 系候補で会員・非会員の画面差が生じ得るが未決 ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9)。

分割・統合は正式な画面構成・業務要求が不足しているため確定せず、各判断を Open Issue とする ([README.md](README.md) §8 Traceability Rules)。

## 10. Creation Order

14 候補を SCR 番号順へ機械的に並べない。以下の粒度で提示する。候補群は正式な Phase や新しい分類体系として登録しない。

### 最初に作成する候補

- **SCR-001 Service Entry** (§11 参照)。

実行状況: SCR-001 の個別 Screen Requirement [service-entry.md](service-entry.md) が `Draft` として存在する。

### その次に作成可能な候補群 (探索・補助領域、予約業務仕様に中核依存しない)

- SCR-002 Destination Discovery
- SCR-003 Accommodation Search
- SCR-004 Search Results
- SCR-005 Accommodation Detail
- SCR-013 Help and Support (予約チェーンから独立)
- SCR-014 Editorial Content (予約チェーンから独立)

この群の内部順序は確定しない。探索連鎖 (SCR-002 → SCR-003 → SCR-004 → SCR-005) は利用者タスク上の接続順があるが、各候補の重要部分が Open Issue (Destination 階層・入力仕様・表示基準・業務モデル) であり、先後を確定する根拠が不足する。SCR-013・SCR-014 は独立性が高く、探索連鎖と並行し得る。順序の確定は各 Open Issue の解決状況に依存するため、現時点では未確定とする。

実行状況: この群の全候補の個別 Screen Requirement が `Draft` として存在する — SCR-002 [destination-discovery.md](destination-discovery.md) / SCR-003 [accommodation-search.md](accommodation-search.md) / SCR-004 [search-results.md](search-results.md) / SCR-005 [accommodation-detail.md](accommodation-detail.md) / SCR-013 [help-and-support.md](help-and-support.md) / SCR-014 [editorial-content.md](editorial-content.md)。作成された事実は上記の内部順序の未確定・各 Open Issue を確定するものではない。

### 上流または業務仕様の確定を待つ候補群 (予約・会員・認証の業務仕様に中核依存)

- SCR-006 Room and Plan Selection
- SCR-007 Booking Details
- SCR-008 Booking Review
- SCR-009 Booking Result
- SCR-010 Booking Management
- SCR-011 Booking Change or Cancellation
- SCR-012 User Access

この群は Stay Plan/Room/Price/Availability の業務モデル、認証・決済、会員制度、予約変更・取消の業務範囲に中核依存し、いずれも未定義 ([../service-design/information-architecture.md](../service-design/information-architecture.md) §11 / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) §9)。業務仕様が確定するまで着手しない。群内の順序は予約連鎖の接続順を持つが、業務仕様未確定のため確定しない。

実行状況: この群 (SCR-006〜SCR-012) の個別 Screen Requirement は未作成 (`Not started`) である。依存する業務仕様が Open Issue から解決へ移っていないため、着手条件 (§12) を満たさない。

上記の各実行状況は現時点の作成状態の注記であり、正式な作成順・新しい Phase・Decision として扱わない。候補群の区分と §6・§7 の評価は変更していない。

## 11. First Candidate Recommendation

- **SCR ID と正式名称**: SCR-001 Service Entry ([../service-design/screen-matrix.md](../service-design/screen-matrix.md) §4・§5)。
- **推薦理由** (§5 の基準に基づく。単一の理由に還元しない):
  1. **上流成果物の定義充足度**: Screen Matrix の該当行の全列 (責務・Primary User Tasks・IA Objects・Navigation Types・Content Categories・Navigation States) が実在する上流定義で埋まっており、[README.md](README.md) §6 Common Document Structure の大部分を推測なく記述できる。
  2. **未定義の業務仕様への依存度**: 状態が Entry・Exploring に限られ、予約・決済・認証・会員・変更・取消の業務仕様に中核依存しない。
  3. **他候補との依存関係**: 入口として他候補へ導線を持つが、他候補の内部要件確定を前提としない (inbound 依存が小さい)。
  4. **Open Issue の性質**: 残る Open Issue (Global Navigation 対象領域、SCR-001/SCR-002 境界) は Navigation スコープの未決であり、業務仕様の推測を要しない。UXDR-TRAVEL-001 に従い Open Issue として保持したまま共通構造を記述できる。
  - 利用者タスク上の位置が最初であることは補足的要因にとどめ、推薦理由の主根拠としない。
- **利用可能な上流根拠**: SDP-001 User Task Clarity / SDP-009 Service-wide Coherence、IA-OBJ-001 Destination / IA-OBJ-002 Search Criteria / IA-OBJ-012 Content、NAV-001 Global Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation、Content Categories = Identification / Task Guidance / Editorial and Support、Navigation States = Entry / Exploring、[../service-design/cta-principles.md](../service-design/cta-principles.md) §7 SCR-001、UXDR-TRAVEL-002 / UXDR-TRAVEL-003。
- **未解決の Open Issues**: Global Navigation の対象領域 (NAV-001 Open Issue)、会員・非会員の Navigation 差、SCR-001/SCR-002 の境界 (作成単位に関わる)。
- **現時点で定義可能な範囲**: 入口の責務、探索起点の User Tasks、Identification / Task Guidance / Editorial and Support の Content 要件、Global/Task/Utility Navigation の要件、Entry・Exploring 状態の要件、アクセシビリティ要件 (SDP-007 / NVP-008 / CTP-008 / CTA-009)、下流影響の分離。
- **定義してはならない範囲**: 具体的な入口 UI・レイアウト・遷移・URL、Global Navigation の確定した対象領域、会員・非会員の画面差、予約・決済・認証・会員の業務仕様。
- **個別要件作成タスクを開始できるか**: 条件付きで開始できる。ただし SCR-001/SCR-002 の境界 (作成単位) を確定できないため、後続タスクは「SCR-001 の作成単位を SCR-001 単独とするか SCR-002 を含めるか」を先頭で扱い、境界を Open Issue として保持したまま SCR-001 の責務範囲を記述する必要がある。
- **開始できない場合の停止要因**: 後続タスクで作成単位・ID 体系・ファイル命名規則 (いずれも Open Issue) を確定せずに個別要件を作成する方針が取れない場合、または Global Navigation 対象領域を推測しなければ記述できないと判断される場合は、着手せず Open Issue の解決を求める。

根拠上 SCR-001 に絞れるが、探索・補助群 (§10) の内部順序は絞り込めないため、そちらは順序未確定として明記する。

実行状況: 本推薦は実行され、SCR-001 の個別 Screen Requirement [service-entry.md](service-entry.md) が `Draft` として存在する。これは推薦の実行状況の注記であり、上記の推薦理由・根拠を事後的に変更するものではない。

## 12. Entry Conditions for Individual Requirements

個別 Screen Requirement 作成タスクを開始する条件を、確定ではなく前提整理として示す。

- 後続タスクで、少なくとも当該候補の作成単位 (1 文書の範囲) を、当該候補の Open Issue を保持したまま暫定的に定められること ([README.md](README.md) §5)。
- 作成対象候補が §10 の「最初に作成する候補」または「その次に作成可能な候補群」に属すること。「上流または業務仕様の確定を待つ候補群」は、依存する業務仕様が Open Issue から解決へ移るまで着手しない。
- 個別文書が [README.md](README.md) §6 Common Document Structure と §7 ID and Status Model に従うこと。ID 体系・ファイル命名規則が未確定の場合、placeholder であることを明示する ([README.md](README.md) §7)。
- 未定義事項を推測で補完せず Open Issue として保持すること (UXDR-TRAVEL-001)。
- 画面候補を URL・route・実装画面と同一視しないこと (UXDR-TRAVEL-002)。

現時点の適用状況 (条件自体は変更しない): §10「最初に作成する候補」および「その次に作成可能な候補群」(SCR-001〜SCR-005・SCR-013・SCR-014) は上記条件を満たし、個別要件が `Draft` として存在する。「上流または業務仕様の確定を待つ候補群」(SCR-006〜SCR-012) は、依存する業務仕様 — §6・§7 の各候補「必要な Open Issues」および §10 の当該群・§15 Open Issues に記載する Stay Plan/Room/Price/Availability の業務モデル、認証・決済・会員仕様、予約変更・取消の業務範囲等 — が Open Issue から解決へ移っていないため、現時点で着手条件を満たさない。

## 13. Relationship with Upstream Artifacts

本文書の上流成果物は、[README.md](README.md) の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) と Governance の実在成果物とする。上流の定義を本文書で変更・再定義しない。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — 評価の上位基準 (SDP-001〜010)。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — 各候補が扱う情報オブジェクト (IA-OBJ-001〜012) と Open Issue。
- **SD-003 [Navigation](../service-design/navigation.md)** — Navigation 分類 (NAV-001〜006)・原則 (NVP-001〜008)・状態。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — Content Category と原則 (CTP-001〜010)。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — CTA 原則 (CTA-001〜010)・分類・§7 の画面候補別考慮。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — 評価対象の画面候補と責務。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — Accepted な UXDR-TRAVEL-001/002/003 の制約。
- **[Governance](../../../governance/README.md)** — サービス識別子 `travel` は暫定であり要 ADR ([owner-decisions.md](../../../governance/owner-decisions.md) 確認事項#8)。命名規則・ADR・レビュー規則の正本は未整備 ([governance/README.md](../../../governance/README.md))。

## 14. Relationship with Downstream Artifacts

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — 下流に位置する。既存 Design System を参照して実現可能性や未整備箇所 (例: [../design-system/components.md](../design-system/components.md) が Select / Tabs / Toast / Table / Accordion を未着手と明記、Button 状態一式が実査待ち) を確認できるが、既存 Design System の記述を上流要求へ昇格させない ([README.md](README.md) §10)。本文書の評価は Design System の記述を根拠に用いない。
- **Implementation** — Repository の管理対象外。本文書では扱わない。実装画面数・URL・route を確定しない (UXDR-TRAVEL-002)。

## 15. Open Issues

以下は未決である。解決策は推測して記載しない。影響する SCR ID を可能な範囲で示す。

- **Screen Requirement 文書の作成単位** — 全候補。特に SCR-001/SCR-002、SCR-005/SCR-006、SCR-007/SCR-008 の境界。
- **候補ごとの分割・統合** — SCR-001/SCR-002、SCR-005/SCR-006、SCR-007/SCR-008 (§9)。
- **個別文書の作成順の正式確定** — 全候補。特に §10「その次に作成可能な候補群」の内部順序。
- **Screen Requirement ID 体系の正式採用** — 全候補 ([README.md](README.md) §7)。
- **ファイル命名規則** — 全候補 ([README.md](README.md) §17)。
- **Acceptance Criteria の確定主体** — 全候補 ([README.md](README.md) §17)。
- **業務要求・機能要求の提供元** — 特に SCR-003 (入力仕様)、SCR-004 (表示基準)、SCR-006〜SCR-011 (予約業務)。
- **認証・決済・会員仕様** — SCR-007, SCR-010, SCR-012。
- **予約変更・取消の業務範囲** — SCR-011 (関連: SCR-010)。
- **URL・ルート・画面遷移との対応** — 全候補 (UXDR-TRAVEL-002 により本文書で確定しない)。
- **エラー・中断専用画面の要否** — `Error / Interrupted` 状態を持つ全候補 (SCR-003, SCR-004, SCR-005, SCR-006, SCR-007, SCR-008, SCR-009, SCR-010, SCR-011, SCR-012, SCR-013)。
- **Design System への反映確認方法** — 全候補 ([README.md](README.md) §17)。
- **Destination の階層構造** — SCR-002 (関連: SCR-001, SCR-004)。
- **Content の分類・編集方針** — SCR-014 (関連: SCR-002, SCR-013)。
- **Global Navigation の対象領域** — SCR-001, SCR-010, SCR-012。

## 16. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Initial draft: assess SCR-001〜SCR-014 creation order, first candidate recommendation, and entry conditions | Draft |
| 2026-07-16 | Sync execution status into §3 / §5 / §10 / §11 / §12 (SCR-001〜SCR-005・SCR-013・SCR-014 individual requirements Draft, SCR-006〜SCR-012 Not started). Assessment results, recommendation rationale, and the `Draftable Without Assumption` classification are unchanged | Draft |
