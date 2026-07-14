# Travel Information Architecture

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の情報構造 (Information Architecture) の初版 Draft
- Position in Repository: `services/travel/service-design/information-architecture.md` — Service Design レイヤー (travel サービス配下)。入口は [README.md](README.md)、上位原則は [principles.md](principles.md)、横断共通は [Governance](../../../governance/README.md) を参照。

## 1. Purpose

本文書は、国内宿泊サービスにおける情報構造 (Information Architecture) の Draft 正本を管理する。

- 主要な情報オブジェクト、その責務、オブジェクト間の概念関係、分類、境界を整理する。
- 後続成果物 (Navigation / Content Principles / CTA Principles / Screen Matrix / Screen Requirements) および Design System のレビューに、共通の情報構造を提供する。
- 画面構成・具体的な導線・UI・機能仕様・業務モデルは決定しない。これらは下流成果物および実装設計の責務である。

## 2. Preconditions

### Facts

- [Service Design Principles](principles.md) は Draft として存在する。
- Information Architecture は本タスク以前には未作成だった。
- 既存 Design System は存在する ([design-system/](../design-system/))。
- 上位事業要求と業務モデルの多くは未定義である。
- 実装側のデータモデルは本タスクでは確認していない。

### Decisions

- 12 の主要情報オブジェクト (IA-OBJ-001〜012) を初版 Draft の分析対象とする。
- IA は概念モデルであり、画面・API・DB を定義しない。
- 未定義事項を推測で補完しない。
- 具体的な業務モデルへ踏み込まない。

### Hypothesis

- なし。

### Open Issues

- 宿泊施設・客室・プラン・在庫・料金の正式な業務関係。
- Destination の正式な階層。
- User の正式な分類。
- Booking の正式な状態と構造。
- Content の正式な分類。
- 実装データモデルとの対応関係。

## 3. IA Principles

本 IA の分類・関係・責務の判断基準として、以下の [Service Design Principles](principles.md) を主に参照する。

- SDP-001 User Task Clarity
- SDP-003 Transparent Conditions
- SDP-004 Consistent Mental Model
- SDP-008 Evidence over Assumption
- SDP-009 Service-wide Coherence
- SDP-010 Incremental Definition

その他の原則も関連する場合は参照する。ただし、Principles から具体的な仕様が自動的に決まるわけではない。

## 4. Information Classification

本文書内の情報は以下に区別する。確認できない情報を Fact または Decision として扱わない。

- **Fact** — 確認済みの事実
- **Decision** — 本タスクで採用する設計判断
- **Hypothesis** — 検証が必要な仮説
- **Open Issue** — 未決事項

本タスクで定義する IA モデルは、上位要求と業務モデルが未定義であるため全体として `Draft` とする。

## 5. Core Information Objects

オブジェクト ID `IA-OBJ-001`〜`IA-OBJ-012` は管理用の暫定識別子であり、正式な恒久採番として確定したものではない (正式な命名規則は未整備 = Open Issue)。本 Draft では主要オブジェクトを独断で追加せず、不足が疑われる点は Open Issues に記載する。

## IA-OBJ-001: Destination

### Definition

宿泊先を探すための地理的・目的地的な情報単位。

### Responsibility

利用者が「どこに泊まるか」を検討・指定するための地理/目的地の観点を提供する。

### Includes

- 都道府県 / 市区町村 / エリア / 駅 / 観光地 / ランドマーク (含み得る概念)

### Relationships

- Search Criteria が Destination を参照する。
- Accommodation は Destination に所在する。
- Content は Destination の評価を支援する。

### Does Not Decide

- 正式な階層構造 (都道府県〜ランドマークの包含関係) は確定しない。

### Status

Draft (階層構造は Open Issue)

## IA-OBJ-002: Search Criteria

### Definition

利用者が宿泊候補を絞り込むための条件。

### Responsibility

利用者の探索意図を条件として保持し、候補の絞り込み・評価の入力となる。

### Includes

- 目的地 / 宿泊日 / 泊数 / 人数 / 部屋数 / 条件指定 (含み得る概念)

### Relationships

- User が Search Criteria を使用する。
- Search Criteria は Destination を参照する。
- Search Criteria は Accommodation を絞り込む。
- Stay Plan は Search Criteria の下で評価される。

### Does Not Decide

- 具体的な入力項目や必須条件は確定しない。

### Status

Draft

## IA-OBJ-003: Accommodation

### Definition

宿泊施設そのものを表す情報単位。

### Responsibility

利用者が施設を識別・比較・評価するための中心的な情報単位を提供する。

### Includes

- 施設名 / 所在地 / 施設種別 / 設備 / 特徴 / 写真 / 評価 / アクセス情報 (含み得る概念)

### Relationships

- Accommodation は Destination に所在する。
- Accommodation は Room を含む/提供する。
- Accommodation は Stay Plan を提供する。
- Accommodation は Policy によって制約され得る。
- Accommodation は Review によって評価される。
- Search Criteria が Accommodation を絞り込む。
- Content は Accommodation の評価を支援する。
- Booking は Accommodation を参照する。

### Does Not Decide

- 正式な属性一覧は確定しない。

### Status

Draft

## IA-OBJ-004: Room

### Definition

宿泊施設内の客室または宿泊単位。

### Responsibility

施設内で提供される宿泊の単位を表し、条件・提供内容の適用先となる。

### Includes

- 客室種別 / 定員 / 設備 / 広さ / ベッド構成 / 禁煙・喫煙 (含み得る概念)

### Relationships

- Accommodation は Room を含む/提供する。
- Stay Plan は Room に適用され得る。
- Booking は Room を参照する。

### Does Not Decide

- Accommodation との正式なデータ関係は確定しない。

### Status

Draft (業務関係は Open Issue)

## IA-OBJ-005: Stay Plan

### Definition

宿泊条件・提供内容・料金条件を組み合わせた販売単位。

### Responsibility

利用者が選択・比較・予約する対象となる、提供内容と条件の組み合わせを表す。

### Includes

- 食事条件 / 宿泊条件 / 特典 / 取消条件 / 支払条件 / 適用人数 / 適用期間 (含み得る概念)

### Relationships

- Accommodation は Stay Plan を提供する。
- Stay Plan は Room に適用され得る。
- Stay Plan は Availability を持つ。
- Stay Plan は Price を持つ/Price で評価される。
- Stay Plan は Policy によって制約され得る。
- Stay Plan は Search Criteria の下で評価される。
- Booking は Stay Plan を参照する。

### Does Not Decide

- 「プラン」「部屋」「料金」「在庫」の正式な業務モデルは確定しない。

### Status

Draft (業務モデルは Open Issue)

## IA-OBJ-006: Availability

### Definition

特定条件に対して予約可能かどうかを表す情報。

### Responsibility

条件に応じた予約可否を示し、選択・予約の成立可能性の判断材料となる。

### Includes

- 日付 / 人数 / 部屋数 / 在庫状態 / 受付可否 (含み得る概念)

### Relationships

- Stay Plan は Availability を持つ。
- Availability は Search Criteria の条件と併せて評価される。

### Does Not Decide

- リアルタイム性・更新方式・保持主体は確定しない。

### Status

Draft

## IA-OBJ-007: Price

### Definition

利用者が判断するための料金情報。

### Responsibility

利用者が費用を理解・比較・判断するための料金の観点を提供する。

### Includes

- 基本料金 / 税 / 手数料 / 割引 / 合計 / 1名あたり / 1室あたり (含み得る概念)

### Relationships

- Stay Plan は Price を持つ/Price で評価される。
- Booking は Price を記録する。

### Does Not Decide

- 正式な料金構造や表示単位は確定しない。

### Status

Draft

## IA-OBJ-008: Policy

### Definition

予約や宿泊に適用される条件・制約。

### Responsibility

利用者の判断・予約・宿泊に影響する条件や制約を表す。

### Includes

- キャンセル条件 / 支払条件 / チェックイン・チェックアウト / 年齢制限 / 子ども条件 / 追加料金 / 施設固有ルール (含み得る概念)

### Relationships

- Accommodation / Room / Stay Plan / Booking は Policy によって制約され得る。

### Does Not Decide

- 正式な分類は確定しない。

### Status

Draft (分類は Open Issue)

## IA-OBJ-009: Review

### Definition

宿泊施設または宿泊体験に対する評価情報。

### Responsibility

利用者の評価判断を支援する第三者的な評価の観点を提供する。

### Includes

- 評点 / 投稿内容 / 投稿者属性 / 投稿日 / 評価対象 (含み得る概念)

### Relationships

- Review は Accommodation を評価する (宿泊体験・Stay Plan の評価支援を含み得る)。

### Does Not Decide

- レビューの提供元、信頼性、表示基準は確定しない。

### Status

Draft (提供元・評価対象・信頼性は Open Issue)

## IA-OBJ-010: Booking

### Definition

利用者と宿泊サービスの間で成立する予約情報。

### Responsibility

予約対象・条件・当事者・料金・状態を束ねる、予約の情報単位を表す。

### Includes

- 予約対象 / 宿泊条件 / 予約者 / 宿泊者 / 料金 / 支払 / 状態 / 変更・取消 (含み得る概念)

### Relationships

- User は Booking を作成/保持する。
- Booking は Accommodation / Room / Stay Plan を参照する。
- Booking は Price を記録する。
- Booking は Policy によって制約され得る。

### Does Not Decide

- 正式な予約状態や業務処理は確定しない。

### Status

Draft (構造・状態は Open Issue)

## IA-OBJ-011: User

### Definition

サービスを利用する主体。

### Responsibility

検索・予約・宿泊などの行為を行う主体を表す。

### Includes

- 検索者 / 予約者 / 宿泊者 / 会員 / 非会員 (含み得る概念)

### Relationships

- User は Search Criteria を使用する。
- User は Booking を作成/保持する。

### Does Not Decide

- 会員制度や識別方法は未定義であるため、正式なユーザーモデル (検索者/予約者/宿泊者/会員/非会員の区別) を確定しない。

### Status

Draft (分類は Open Issue)

## IA-OBJ-012: Content

### Definition

宿泊予約の判断や利用を支援する情報。

### Responsibility

オブジェクト評価や利用を補助する説明・案内的な情報を提供する。

### Includes

- 特集 / ガイド / お知らせ / FAQ / 説明コンテンツ / サポート情報 (含み得る概念)

### Relationships

- Content は Destination の評価を支援する。
- Content は Accommodation の評価を支援する (Stay Plan の評価支援を含み得る)。

### Does Not Decide

- コンテンツ戦略が未定義であるため、正式な分類・優先順位は確定しない。

### Status

Draft (分類・責務は Open Issue)

## 6. Conceptual Relationship Model

以下は概念関係であり、DB リレーション、API 構造、業務処理を意味しない。

### Search relationship

```text
User
  uses Search Criteria
  to discover Accommodation
  within Destination
```

### Offering relationship

```text
Accommodation
  contains or provides Room
  offers Stay Plan
```

### Availability and price relationship

```text
Stay Plan
  is evaluated with Availability
  and Price
  under Search Criteria
```

### Condition relationship

```text
Accommodation / Room / Stay Plan / Booking
  may be constrained by Policy
```

### Decision support relationship

```text
Review and Content
  support evaluation of Accommodation and Stay Plan
```

### Booking relationship

```text
User
  creates or holds Booking
  for Accommodation / Room / Stay Plan
```

## 7. Relationship Matrix

関係の正式性が不明なものは `Draft` または `Open Issue` とする。

| Source Object | Relationship | Target Object | Status | Notes |
| --- | --- | --- | --- | --- |
| User | uses | Search Criteria | Draft | |
| Search Criteria | references | Destination | Draft | |
| Search Criteria | filters | Accommodation | Draft | |
| Accommodation | located in | Destination | Draft | 階層構造は Open Issue |
| Accommodation | contains/provides | Room | Draft | 業務関係は Open Issue |
| Accommodation | offers | Stay Plan | Draft | |
| Stay Plan | may apply to | Room | Draft | 業務モデルは Open Issue |
| Stay Plan | has | Availability | Draft | |
| Stay Plan | has/is evaluated with | Price | Draft | |
| Stay Plan | is constrained by | Policy | Draft | |
| Accommodation | is constrained by | Policy | Draft | |
| Room | is constrained by | Policy | Draft | |
| Accommodation | is evaluated by | Review | Draft | 評価対象・信頼性は Open Issue |
| Content | supports evaluation of | Destination | Draft | |
| Content | supports evaluation of | Accommodation | Draft | |
| User | creates/holds | Booking | Draft | |
| Booking | references | Accommodation | Draft | |
| Booking | references | Room | Draft | |
| Booking | references | Stay Plan | Draft | |
| Booking | records | Price | Draft | |
| Booking | is constrained by | Policy | Draft | |

## 8. Ownership and Source of Truth

情報の「正本」を以下の 2 つに分けて考える。

### Repository 上の設計正本

本ファイルは、情報オブジェクトの定義・責務・関係についての Service Design 上の正本となる。

### 運用データの正本

施設・在庫・料金・予約などの実データの正本は本 Repository では管理しない。実データの保持システム・API・DB・外部サービスは未確認であり、本タスクでは決定しない。

以下を明記する。

- 設計上の情報構造と運用データ構造は同一とは限らない。
- 実装側が本 IA をそのまま DB モデルとして使用してはならない。
- 実装との対応は別途確認・設計が必要。

## 9. Boundary

### IA に含む

- 情報オブジェクト
- オブジェクトの責務
- オブジェクト間の概念関係
- 情報分類
- 上流・下流成果物との関係

### IA に含まない

- 画面 / URL / ナビゲーション / UI / Component / API / DB / データ型 / 処理フロー / 権限 / 料金計算 / 在庫管理 / 予約状態遷移 / 決済処理

## 10. Relationship with Other Artifacts

- **Service Design Principles** — IA の分類・関係・責務を判断する上位基準として参照する。
- **Navigation** — 本 IA で定義した情報オブジェクトへの到達・移動方法を設計する。IA 側では具体的なナビゲーションを決定しない。
- **Content Principles** — 各オブジェクトの情報をどのように表現・提示するかを定義する。
- **CTA Principles** — オブジェクトに対して利用者へ求める行動の原則を定義する。
- **Screen Matrix** — 各画面がどの情報オブジェクトを扱うかを整理する。
- **Screen Requirements** — 画面単位で必要なオブジェクト・状態・操作を定義する。
- **Design System** — 各情報オブジェクトや状態を UI として表現する設計語彙を提供する。

## 11. Open Issues

以下は未決である。解決策は推測して記載しない。

- 主要オブジェクト 12 件の正式承認。
- オブジェクト名の正式な日本語・英語用語。
- IA オブジェクト ID の正式採用。
- Accommodation / Room / Stay Plan / Availability / Price の業務上の正式関係。
- Destination の階層構造。
- Policy の分類。
- Review の提供元・評価対象・信頼性。
- User / Booker / Guest / Member の区別。
- Booking の構造と状態。
- Content の分類と責務。
- 外部システム・API・DB との対応。
- 既存 Design System 内の概念との整合性確認。
- Navigation・Screen Matrix で追加オブジェクトが必要になる可能性。

## 12. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-14 | Initial draft of Travel Information Architecture | Draft |
