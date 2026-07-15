# Travel Navigation

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Navigation 設計の初版 Draft
- Position in Repository: `services/travel/service-design/navigation.md` — Service Design レイヤー (travel サービス配下)。入口は [README.md](README.md)、上位原則は [principles.md](principles.md)、情報構造は [information-architecture.md](information-architecture.md)、横断共通は [Governance](../../../governance/README.md) を参照。

## 1. Purpose

本文書は、国内宿泊サービスにおける Navigation 設計の Draft 正本を管理する。

- 利用者が情報を発見し、現在地を理解し、関連情報や次の行動へ移動するための Navigation の原則と分類を定義する。
- 後続成果物 (Content Principles / CTA Principles / Screen Matrix / Screen Requirements) および Design System のレビューに、共通の Navigation 基準を提供する。
- Navigation は [Information Architecture](information-architecture.md) で定義した情報オブジェクトへの到達・移動・関係理解を支援するが、IA 自体を変更しない。
- 具体的な画面一覧・URL・サイトマップ・画面遷移・UI 仕様は確定しない。

## 2. Preconditions

### Facts

- [Service Design Principles](principles.md) は Draft として存在する。
- [Information Architecture](information-architecture.md) は Draft として存在する。
- Navigation 成果物は本タスク以前には未作成だった。
- 正式な画面一覧・URL・サイトマップ・画面遷移は未定義である。
- 既存 Design System は存在する ([design-system/](../design-system/))。

### Decisions

- 6 つの Navigation 分類 (NAV-001〜006) を初版 Draft として扱う。
- 8 つの Navigation Principle (NVP-001〜008) を判断基準として扱う。
- Navigation は IA オブジェクトへの到達・移動・文脈理解を支援する。
- 具体的な画面・URL・UI は定義しない。
- 未定義事項を推測で補完しない。

### Hypothesis

- なし。

### Open Issues

- 正式なサイト構造。
- Global Navigation の対象領域。
- 会員・非会員の Navigation 差。
- 宿泊以外サービスとの関係。
- MyPage の Navigation 範囲。
- モバイル Navigation。
- 検索・予約フロー。
- Navigation ラベル。
- 履歴・文脈保持方式。

## 3. Navigation Principles

Navigation の判断基準として、以下の [Service Design Principles](principles.md) を主に参照する: SDP-001 / SDP-002 / SDP-004 / SDP-005 / SDP-006 / SDP-007 / SDP-009 / SDP-010。原則から具体的な仕様が自動的に決まるわけではない。本文書内で新しい Navigation Principle を独断で追加しない。

## NVP-001: Current Location Visibility

### Decision

利用者が現在どの情報・対象・タスクにいるか理解できること。

### Rationale

現在地が不明だと誤操作・離脱を招く (SDP-001 / SDP-005)。画面が未確定でも適用できる基準が必要である。

### Application

各 Navigation 分類・State で現在地の表現を要件化する基準として使用する。Screen Matrix / Screen Requirements で現在地の把握可能性を評価する。

### Does Not Decide

- パンくず等の具体的な UI、ラベル、表示位置。

## NVP-002: Predictable Destination

### Decision

Navigation の選択前に、移動先や結果を合理的に予測できること。

### Rationale

予測できない遷移は信頼性を損なう (SDP-001)。

### Application

リンク・導線の意味づけと表現原則 (Content Principles / CTA Principles) の上位基準として使用する。

### Does Not Decide

- 具体的な文言、リンク配置、遷移の実装。

## NVP-003: Preserved Context

### Decision

移動によって、検索条件、比較文脈、対象オブジェクト等を不必要に失わせないこと。

### Rationale

文脈の喪失は再入力・離脱を招く (SDP-002 / SDP-006 / SDP-009)。

### Application

Context Preservation and Recovery および Navigation State Model の要件を判断する基準として使用する。

### Does Not Decide

- 保持方式、保存期間、セッション仕様。

## NVP-004: Reversible Movement

### Decision

可能な限り、前の状態や関連する戻り先へ回復できること。

### Rationale

誤操作・中断からの回復を可能にする (SDP-006)。

### Application

History and Recovery Navigation の要件、および回復手段の要否を判断する基準として使用する。

### Does Not Decide

- ブラウザバックの実装、Undo 仕様、履歴保存方式。

## NVP-005: Consistent Meaning

### Decision

同じラベル、位置、Navigation パターンはサービス内で一貫した意味を持つこと。

### Rationale

不整合は学習コストと誤解を生む (SDP-004 / SDP-009)。

### Application

分類間・画面間で Navigation パターンの一貫性を評価する基準として使用する。

### Does Not Decide

- 正式なラベル、命名規則、Component 仕様。

## NVP-006: Task over Organization

### Decision

内部組織やシステム都合ではなく、利用者が理解できる情報・タスク単位で Navigation を構成すること。

### Rationale

組織都合の構造は利用者に推測を強いる (SDP-001)。

### Application

Navigation 分類・Screen Matrix の構成が利用者タスク基準になっているかを評価する基準として使用する。

### Does Not Decide

- 具体的なメニュー構成、画面分割。

## NVP-007: Progressive Disclosure

### Decision

現在の判断に不要な Navigation 選択肢を過剰に提示しないこと。

### Rationale

過剰な提示は判断負荷を高める (SDP-002 / SDP-007)。

### Application

各 State・分類で提示する選択肢の範囲を判断する基準として使用する。

### Does Not Decide

- 表示件数、段階、UI。

## NVP-008: Accessible Navigation

### Decision

キーボード、支援技術、異なる画面サイズ等を例外扱いしないこと。

### Rationale

アクセシビリティを後工程限定にしない (SDP-007)。

### Application

すべての Navigation 分類・状態表現をアクセシビリティの観点でレビューする基準として使用する。

### Does Not Decide

- 適用する具体的な規格、達成レベル、実装方式。

## 4. Navigation Classification

6 分類を Draft として定義する。新しい分類を独断で追加・統合・削除しない。不足や重複が疑われる場合は Open Issue として記載する。`NAV-001`〜`NAV-006` は管理用の暫定識別子であり、正式な恒久採番として確定したものではない。

## NAV-001: Global Navigation

### Definition

サービス全体または主要領域へ移動する Navigation。

### Responsibility

- 主要領域への一貫した入口を提供する。
- サービス内の大きな位置関係を理解できるようにする。
- 特定画面の内部構造に依存しない移動を提供する。

### Related IA Objects

- 特定オブジェクトに限定しない (主要領域への入口)。関連し得る: Destination / Content。

### Application

主要領域の入口をどこに設けるかを Screen Matrix / Screen Requirements で判断する際の基準として使用する。

### Does Not Decide

- 具体的なメニュー項目 / ヘッダー構成 / 表示順 / 会員メニュー / 他サービスとの統合。

### Status

Draft (対象領域は Open Issue)

## NAV-002: Local Navigation

### Definition

現在の情報領域または対象オブジェクト内を移動する Navigation。

### Responsibility

- 同一領域内の関連情報へ移動できるようにする。
- 現在の対象と関連情報の関係を理解できるようにする。
- Accommodation、Booking、Content 等の内部情報を整理する。

### Related IA Objects

- Accommodation / Booking / Content (各オブジェクト内部の情報)。

### Application

各領域内の情報整理の単位を Screen Matrix / Screen Requirements で判断する際の基準として使用する。

### Does Not Decide

- タブ UI / アンカーリンク / 項目名 / 具体的な情報構成。

### Status

Draft (単位は Open Issue)

## NAV-003: Contextual Navigation

### Definition

現在表示している情報や利用者の文脈に関連する情報へ移動する Navigation。

### Responsibility

- 現在の対象と関連性のある情報への移動を提供する。
- IA オブジェクト間の概念関係を利用者が辿れるようにする。
- 無関係な誘導を避ける。

### Related IA Objects

- 含み得る関係例: Destination → Accommodation / Accommodation → Room・Stay Plan・Review・Policy / Booking → Accommodation・Room・Stay Plan・Policy / Content → Destination・Accommodation。

### Application

IA の概念関係に沿った関連情報への導線を Screen Requirements で判断する際の基準として使用する。具体的なリンク配置は確定しない。

### Does Not Decide

- 具体的なリンク配置 / 表示条件。

### Status

Draft (表示条件は Open Issue)

## NAV-004: Task Navigation

### Definition

利用者が特定の目的を進めるための Navigation。

### Responsibility

- 探索・比較・確認・予約・変更等のタスク進行を支援する。
- 現在の段階と次に可能な行動を理解できるようにする。
- 必要以上に早い確約を求めない。

### Related IA Objects

- Search Criteria / Accommodation / Stay Plan / Availability / Price / Booking。

### Application

タスク進行段階と次に可能な行動を Screen Matrix / CTA Principles で判断する際の基準として使用する。

### Does Not Decide

- 正式なタスク一覧 / 予約ステップ / 画面数 / CTA / 業務フロー。

### Status

Draft (タスク一覧は Open Issue)

## NAV-005: History and Recovery Navigation

### Definition

前の状態、以前の探索条件、やり直し可能な位置へ戻るための Navigation。

### Responsibility

- 戻る・修正・再探索を可能にする。
- 利用者の入力や文脈を不必要に失わせない。
- エラーや中断からの回復を支援する。

### Related IA Objects

- Search Criteria / Accommodation / Stay Plan / Booking。

### Application

戻り先・再探索・回復手段の要件を Screen Requirements で判断する際の基準として使用する。

### Does Not Decide

- ブラウザバックの実装 / 履歴保存方式 / 保存期間 / Undo 仕様 / セッション管理。

### Status

Draft (保持方式は Open Issue)

## NAV-006: Utility Navigation

### Definition

主要タスクを補助する情報・機能へ移動する Navigation。

### Responsibility

- 主要タスク外の補助情報へ一貫して到達できるようにする。
- 問題解決や条件確認を支援する。
- 主要タスクの Navigation と混同させない。

### Related IA Objects

- 含み得る概念: FAQ / サポート / お知らせ / 利用条件 / Policy / 言語・表示設定 / アカウント関連。関連し得る IA オブジェクト: Policy / Content / User。

### Application

補助情報への一貫した到達手段を Screen Matrix で判断する際の基準として使用する。

### Does Not Decide

- Utility 項目一覧 / 会員機能 / 表示位置 / フッター構造 / サポートチャネル。

### Status

Draft (対象項目は Open Issue)

## 5. Relationship with IA Objects

以下は [Information Architecture](information-architecture.md) の 12 オブジェクトに対する Navigation 上の考慮点である。Navigation 文書内で IA オブジェクトを追加・変更しない。

| IA Object | Navigation Consideration | Status |
| --- | --- | --- |
| Destination | 探索開始・絞り込み・関連 Content への移動を支援する | Draft |
| Search Criteria | 条件の確認・変更・再利用時に文脈を保持する | Draft |
| Accommodation | Room / Stay Plan / Review / Policy 等との関係理解を支援する | Draft |
| Room | 所属 Accommodation および関連 Stay Plan との関係を示す | Draft |
| Stay Plan | Room / Availability / Price / Policy との関係を示す | Draft |
| Availability | 対象条件との関係を失わず確認できるようにする | Draft |
| Price | 対象・条件・単位との関係を保つ | Draft |
| Policy | 適用対象へ戻れる文脈を維持する | Draft |
| Review | 評価対象との関係を明確にする | Draft |
| Booking | 予約対象・条件・状態・関連 Policy へ到達可能にする | Draft |
| User | 会員モデルを前提とせず、利用者タスクとの関係で扱う | Draft |
| Content | 関連 Destination / Accommodation への文脈的移動を支援する | Draft |

## 6. Navigation State Model

Navigation に関係する状態を Draft として整理する。これは業務上の予約状態や画面遷移を定義するものではない。

| State | Meaning | Navigation Requirement | Status |
| --- | --- | --- | --- |
| Entry | サービスまたは領域へ入った状態 | 主要な選択肢と現在地を理解できる | Draft |
| Exploring | 候補・情報を探索している状態 | 条件変更と関連情報への移動を支援する | Draft |
| Evaluating | 候補・条件を比較・確認している状態 | 対象と条件の文脈を維持する | Draft |
| Committing | 予約等の確約へ進む状態 | 前段の条件・影響・戻り先を理解できる | Draft |
| Completed | タスクが完了した状態 | 結果、次の行動、関連情報への移動を提供する | Draft |
| Error / Interrupted | エラー・中断状態 | 原因、回復方法、戻り先を提供する | Draft |

## 7. Context Preservation and Recovery

- 検索条件や対象オブジェクトを、不必要な画面移動で失わせない。
- Policy や Review 等の補助情報を確認した後、元の対象へ戻れる文脈を維持する。
- エラー・中断時には、利用者が継続、修正、再試行、離脱を判断できるようにする。
- 戻る操作の具体的な実装方法は定義しない。
- 保持期間、保存方式、セッション仕様は定義しない。
- 文脈保持が法務・セキュリティ・事業要件と競合する場合は Open Issue とする。

## 8. Boundary

### Navigation に含む

- Navigation の分類
- Navigation 原則
- IA オブジェクトへの到達・移動の考え方
- 現在地・移動先・戻り先・文脈保持
- Navigation 状態
- 後続成果物への判断基準

### Navigation に含まない

- 画面一覧 / サイトマップ / URL / ルーティング / 画面遷移 / CTA / 文言 / UI Component / レイアウト / ヘッダー・フッター項目 / モバイルメニュー / 認証 / 予約業務フロー / 実装仕様

## 9. Relationship with Other Artifacts

- **Service Design Principles** — Navigation 判断の上位基準として使用する。
- **Information Architecture** — Navigation の対象となる情報オブジェクトと概念関係を提供する。Navigation 側で IA オブジェクトの定義を変更しない。
- **Content Principles** — Navigation ラベル、説明、リンク文脈の表現原則を提供する。本タスクでは具体的な文言を定義しない。
- **CTA Principles** — タスク進行において利用者へ求める行動の優先順位と表現原則を提供する。Navigation と CTA を同一視しない。
- **Screen Matrix** — 各画面がどの Navigation 分類・状態・IA オブジェクトを扱うか整理する。
- **Screen Requirements** — 画面単位の Navigation 要件を具体化する。
- **Design System** — Navigation を UI として表現する Component や状態表現を提供する。

## 10. Open Issues

以下は未決である。解決策は推測して記載しない。

- 6 分類の正式承認。
- NAV ID の正式採用。
- Navigation Principle の正式承認。
- Global Navigation の対象領域。
- Local Navigation の単位。
- Contextual Navigation の表示条件。
- Task Navigation の正式なタスク一覧。
- Utility Navigation の対象項目。
- 会員・非会員の Navigation 差。
- MyPage・予約管理領域の Navigation。
- 宿泊以外のサービスとの横断 Navigation。
- URL・サイトマップ・画面遷移との対応。
- モバイル・レスポンシブ時の Navigation。
- アクセシビリティの具体基準。
- 検索条件・比較文脈・履歴の保持方法。
- 既存 Design System の Navigation 関連 Component との整合性。
- Screen Matrix 策定時に不足分類が判明する可能性。

## 11. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-14 | Initial draft of Travel Navigation | Draft |
