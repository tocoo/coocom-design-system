# Travel Screen Matrix

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の画面候補管理表の初版 Draft
- Position in Repository: `services/travel/service-design/screen-matrix.md` — Service Design レイヤー (travel サービス配下)。入口は [README.md](README.md)、参照する上流成果物は [principles.md](principles.md) / [information-architecture.md](information-architecture.md) / [navigation.md](navigation.md) / [content-principles.md](content-principles.md)、横断共通は [Governance](../../../governance/README.md)。

## 1. Purpose

本文書は、国内宿泊サービスに必要となり得る画面・画面群 (画面候補) と、その責務・関連成果物を管理する Draft 正本である。

- 画面候補を、利用者タスク・情報責務・IA オブジェクト・Navigation 分類・Content Category・Navigation State の観点で整理する。
- 後続の Screen Requirements を作成するための管理表とする。
- 具体的な UI・画面遷移・URL・機能仕様・業務仕様は確定しない。

## 2. Preconditions

### Facts

- [Service Design Principles](principles.md) は Draft として存在する。
- [Information Architecture](information-architecture.md) は Draft として存在する。
- [Navigation](navigation.md) は Draft として存在する。
- [Content Principles](content-principles.md) は Draft として存在する。
- Screen Matrix は本タスク以前には未作成だった。
- 正式な画面一覧、URL、画面遷移、業務仕様は未定義である。

### Decisions

- 14 画面候補 (SCR-001〜014) を初版 Draft の管理対象とする。
- Screen Matrix は画面責務と関連成果物を管理する。
- 具体的な画面仕様は Screen Requirements で定義する。
- 未定義事項を推測で補完しない。

### Hypothesis

- なし。

### Open Issues

- 画面候補の正式承認。
- 画面候補の分割・統合。
- 正式なサイトマップ。
- 検索・予約・管理フロー。
- MyPage・会員領域。
- 認証・決済。
- 宿泊以外サービスとの統合。

## 3. Screen Candidate Principles

- 画面候補は利用者タスクと情報責務を基準に分ける。
- URL、既存ページ、組織構造だけを根拠に分けない。
- 1 画面候補が必ず 1 実装画面になるとは限らない。
- 画面候補間で責務を不必要に重複させない。
- 上位要求が未定義の場合は Open Issue を維持する。
- Screen Requirements 策定前に具体 UI を確定しない。

`SCR-001`〜`SCR-014` は管理用の暫定識別子であり、正式な恒久採番として確定したものではない。本 Draft では画面候補を独断で追加・統合・削除せず、不足や重複は Open Issues に記載する。

## 4. Screen Matrix

Navigation Types は [navigation.md](navigation.md) の NAV ID、Content Categories は [content-principles.md](content-principles.md) の分類、Navigation States は [navigation.md](navigation.md) の状態名を用いる。Screen Requirements は全件 `Not started`。

| Screen ID | Screen Candidate | Responsibility | Primary Task | Primary IA Objects | Navigation Types | Content Categories | Navigation States | Screen Requirements | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCR-001 | Service Entry | サービスへの入口を提供する | 探索の起点に立つ | Destination / Search Criteria / Content | NAV-001 / 004 / 006 | Identification / Task Guidance / Editorial and Support | Entry, Exploring | Not started | Draft |
| SCR-002 | Destination Discovery | 目的地・エリア・関連 Content を発見する | 目的地を発見する | Destination / Content | NAV-001 / 002 / 003 | Identification / Editorial and Support | Exploring | Not started | Draft |
| SCR-003 | Accommodation Search | Search Criteria を入力・確認・変更する | 検索条件を指定する | Search Criteria / Destination | NAV-004 / 005 | Task Guidance / Identification | Entry, Exploring, Error / Interrupted | Not started | Draft |
| SCR-004 | Search Results | Accommodation 候補を確認・比較する | 候補を比較する | Search Criteria / Accommodation | NAV-002 / 003 / 004 / 005 | Identification / Decision Support / Conditions and Policies | Exploring, Evaluating, Error / Interrupted | Not started | Draft |
| SCR-005 | Accommodation Detail | 施設と関連情報を確認する | 施設を評価する | Accommodation | NAV-002 / 003 / 004 / 006 | Identification / Decision Support / Conditions and Policies / Editorial and Support | Evaluating, Error / Interrupted | Not started | Draft |
| SCR-006 | Room and Plan Selection | Room・Stay Plan を比較・選択する | 客室・プランを選ぶ | Room / Stay Plan | NAV-002 / 003 / 004 / 005 | Decision Support / Conditions and Policies / Identification | Evaluating, Committing, Error / Interrupted | Not started | Draft |
| SCR-007 | Booking Details | 予約条件・当事者情報を確認・入力する | 予約情報を入力する | Booking / User | NAV-004 / 005 / 006 | Task Guidance / Conditions and Policies / Identification | Committing, Error / Interrupted | Not started | Draft |
| SCR-008 | Booking Review | 確約前に予約内容を確認する | 予約前に確認する | Booking | NAV-004 / 005 / 006 | Identification / Conditions and Policies / Task Guidance | Committing, Error / Interrupted | Not started | Draft |
| SCR-009 | Booking Result | 予約結果と次の行動を確認する | 結果を確認する | Booking | NAV-003 / 004 / 006 | Status and Feedback / Task Guidance / Identification | Completed, Error / Interrupted | Not started | Draft |
| SCR-010 | Booking Management | 成立した Booking を確認・管理する | 予約を管理する | Booking | NAV-001 / 002 / 003 / 004 / 006 | Identification / Status and Feedback / Conditions and Policies / Task Guidance | Entry, Evaluating, Completed, Error / Interrupted | Not started | Draft |
| SCR-011 | Booking Change or Cancellation | Booking の変更・取消を検討・実行する | 変更・取消する | Booking / Policy | NAV-002 / 004 / 005 / 006 | Conditions and Policies / Task Guidance / Status and Feedback | Evaluating, Committing, Completed, Error / Interrupted | Not started | Draft |
| SCR-012 | User Access | 認証・識別に関連する入口を提供する | サービスにアクセスする | User | NAV-001 / 004 / 006 | Task Guidance / Identification | Entry, Committing, Error / Interrupted | Not started | Draft |
| SCR-013 | Help and Support | 問題解決・条件確認を支援する | 支援を得る | Content / Policy | NAV-001 / 002 / 003 / 006 | Editorial and Support / Conditions and Policies | Entry, Exploring, Error / Interrupted | Not started | Draft |
| SCR-014 | Editorial Content | 特集・ガイド等の Content を提供する | 情報を読む | Content | NAV-001 / 002 / 003 | Editorial and Support / Identification | Entry, Exploring, Evaluating | Not started | Draft |

## 5. Screen Candidates

## SCR-001: Service Entry

### Purpose

国内宿泊サービスへの入口。

### Primary User Tasks

- サービスの主要な選択肢を理解し、探索の起点に立つ。

### Primary IA Objects

- Destination / Search Criteria / Content

### Supporting IA Objects

- なし

### Navigation Types

- NAV-001 Global Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation

### Content Categories

- Identification / Task Guidance / Editorial and Support

### Navigation States

- Entry, Exploring

### Does Not Decide

- 具体的な入口 UI・レイアウト・遷移・URL。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-002: Destination Discovery

### Purpose

目的地・エリア・関連 Content を発見する画面または画面群。

### Primary User Tasks

- 目的地やエリアを発見し、候補探索へ進む。

### Primary IA Objects

- Destination / Content

### Supporting IA Objects

- Accommodation

### Navigation Types

- NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation

### Content Categories

- Identification / Editorial and Support

### Navigation States

- Exploring

### Does Not Decide

- 目的地の階層 UI・一覧構成・遷移。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-003: Accommodation Search

### Purpose

Search Criteria を入力・確認・変更する画面または画面群。

### Primary User Tasks

- 検索条件を指定・確認・変更する。

### Primary IA Objects

- Search Criteria / Destination

### Supporting IA Objects

- User

### Navigation Types

- NAV-004 Task Navigation / NAV-005 History and Recovery Navigation

### Content Categories

- Task Guidance / Identification

### Navigation States

- Entry, Exploring, Error / Interrupted

### Does Not Decide

- 入力項目・必須条件・バリデーション・UI。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-004: Search Results

### Purpose

検索条件に対応する Accommodation 候補を確認・比較する画面または画面群。

### Primary User Tasks

- 候補を確認・比較し、詳細検討へ進む。

### Primary IA Objects

- Search Criteria / Accommodation

### Supporting IA Objects

- Availability / Price / Review / Policy

### Navigation Types

- NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-005 History and Recovery Navigation

### Content Categories

- Identification / Decision Support / Conditions and Policies

### Navigation States

- Exploring, Evaluating, Error / Interrupted

### Does Not Decide

- 一覧・並び替え・絞り込み UI・遷移。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-005: Accommodation Detail

### Purpose

Accommodation の情報と関連 Room、Stay Plan、Review、Policy を確認する画面または画面群。

### Primary User Tasks

- 施設情報と関連情報を確認し、評価する。

### Primary IA Objects

- Accommodation

### Supporting IA Objects

- Destination / Room / Stay Plan / Review / Policy / Content

### Navigation Types

- NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation

### Content Categories

- Identification / Decision Support / Conditions and Policies / Editorial and Support

### Navigation States

- Evaluating, Error / Interrupted

### Does Not Decide

- 詳細レイアウト・情報構成・遷移。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-006: Room and Plan Selection

### Purpose

Room、Stay Plan、Availability、Price、Policy を比較・選択する画面または画面群。

### Primary User Tasks

- 客室・プランを比較し、選択する。

### Primary IA Objects

- Room / Stay Plan

### Supporting IA Objects

- Accommodation / Availability / Price / Policy

### Navigation Types

- NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-005 History and Recovery Navigation

### Content Categories

- Decision Support / Conditions and Policies / Identification

### Navigation States

- Evaluating, Committing, Error / Interrupted

### Does Not Decide

- 選択 UI・価格表示・在庫表示・遷移。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-007: Booking Details

### Purpose

予約条件、予約者・宿泊者情報等を確認・入力する画面または画面群。

### Primary User Tasks

- 予約条件と当事者情報を確認・入力する。

### Primary IA Objects

- Booking / User

### Supporting IA Objects

- Accommodation / Room / Stay Plan / Price / Policy

### Navigation Types

- NAV-004 Task Navigation / NAV-005 History and Recovery Navigation / NAV-006 Utility Navigation

### Content Categories

- Task Guidance / Conditions and Policies / Identification

### Navigation States

- Committing, Error / Interrupted

### Does Not Decide

- 入力項目・バリデーション・認証・決済・UI。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-008: Booking Review

### Purpose

予約対象、Price、Policy、入力内容を確約前に確認する画面または画面群。

### Primary User Tasks

- 確約前に予約内容を確認する。

### Primary IA Objects

- Booking

### Supporting IA Objects

- User / Accommodation / Room / Stay Plan / Price / Policy

### Navigation Types

- NAV-004 Task Navigation / NAV-005 History and Recovery Navigation / NAV-006 Utility Navigation

### Content Categories

- Identification / Conditions and Policies / Task Guidance

### Navigation States

- Committing, Error / Interrupted

### Does Not Decide

- 確認画面構成・確約操作・遷移。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-009: Booking Result

### Purpose

予約処理の結果と次の行動を確認する画面または画面群。

### Primary User Tasks

- 予約結果と次の行動を確認する。

### Primary IA Objects

- Booking

### Supporting IA Objects

- Accommodation / Room / Stay Plan / Price / Policy

### Navigation Types

- NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation

### Content Categories

- Status and Feedback / Task Guidance / Identification

### Navigation States

- Completed, Error / Interrupted

### Does Not Decide

- 結果表示・後続導線・UI。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-010: Booking Management

### Purpose

成立した Booking の確認・管理を行う画面または画面群。

### Primary User Tasks

- 成立済みの予約を確認・管理する。

### Primary IA Objects

- Booking

### Supporting IA Objects

- User / Accommodation / Room / Stay Plan / Price / Policy

### Navigation Types

- NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation

### Content Categories

- Identification / Status and Feedback / Conditions and Policies / Task Guidance

### Navigation States

- Entry, Evaluating, Completed, Error / Interrupted

### Does Not Decide

- MyPage 構成・会員範囲・提供機能・UI。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-011: Booking Change or Cancellation

### Purpose

Booking の変更・取消を検討・実行する画面または画面群。

### Primary User Tasks

- 予約の変更・取消を検討・実行する。

### Primary IA Objects

- Booking / Policy

### Supporting IA Objects

- User / Accommodation / Room / Stay Plan / Price

### Navigation Types

- NAV-002 Local Navigation / NAV-004 Task Navigation / NAV-005 History and Recovery Navigation / NAV-006 Utility Navigation

### Content Categories

- Conditions and Policies / Task Guidance / Status and Feedback

### Navigation States

- Evaluating, Committing, Completed, Error / Interrupted

### Does Not Decide

- 変更・取消の業務範囲・条件・手数料・UI。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-012: User Access

### Purpose

認証、識別、会員・非会員に関連し得る入口。正式な会員仕様は決定しない。

### Primary User Tasks

- サービスへアクセスする (識別・認証に関連し得る)。

### Primary IA Objects

- User

### Supporting IA Objects

- Booking

### Navigation Types

- NAV-001 Global Navigation / NAV-004 Task Navigation / NAV-006 Utility Navigation

### Content Categories

- Task Guidance / Identification

### Navigation States

- Entry, Committing, Error / Interrupted

### Does Not Decide

- 認証方式・会員制度・識別方法・UI。

### Screen Requirements Status

Not started

### Status

Draft (会員仕様は Open Issue)

## SCR-013: Help and Support

### Purpose

FAQ、問い合わせ、問題解決、Policy 確認等を支援する画面または画面群。

### Primary User Tasks

- 問題解決・条件確認の支援を得る。

### Primary IA Objects

- Content / Policy

### Supporting IA Objects

- User / Booking

### Navigation Types

- NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation / NAV-006 Utility Navigation

### Content Categories

- Editorial and Support / Conditions and Policies

### Navigation States

- Entry, Exploring, Error / Interrupted

### Does Not Decide

- サポートチャネル・FAQ 構成・問い合わせ手段・UI。

### Screen Requirements Status

Not started

### Status

Draft

## SCR-014: Editorial Content

### Purpose

特集、ガイド、案内等の Content を提供する画面または画面群。

### Primary User Tasks

- 特集・ガイド等の情報を読み、発見・理解する。

### Primary IA Objects

- Content

### Supporting IA Objects

- Destination / Accommodation

### Navigation Types

- NAV-001 Global Navigation / NAV-002 Local Navigation / NAV-003 Contextual Navigation

### Content Categories

- Editorial and Support / Identification

### Navigation States

- Entry, Exploring, Evaluating

### Does Not Decide

- コンテンツ分類・編集方針・UI。

### Screen Requirements Status

Not started

### Status

Draft

## 6. Relationship with Screen Requirements

- Screen Matrix は Screen Requirements 作成対象を管理する。
- Screen Matrix だけでは画面要件は確定しない。
- 各画面候補の詳細は、別タスクで Screen Requirements として定義する。
- 画面候補が複数画面へ分割される可能性がある。
- 複数の画面候補が 1 画面へ統合される可能性がある。
- 分割・統合は正式な画面構成と業務要件を確認した上で決定する。

## 7. Boundary

### Screen Matrix に含む

- 画面候補
- 画面候補の責務
- 利用者タスク
- IA オブジェクトとの関係
- Navigation 分類との関係
- Content Category との関係
- Navigation State との関係
- Screen Requirements 作成状況

### Screen Matrix に含まない

- 具体的な画面構成 / UI / レイアウト / ワイヤーフレーム / URL / 画面遷移 / CTA / コピー / 入力項目 / バリデーション / Component / API / DB / 業務処理 / 権限・認証 / 予約状態遷移

## 8. Relationship with Other Artifacts

- **Service Design Principles** — 画面候補の分け方・責務判断の上位基準。
- **Information Architecture** — 各画面候補が扱う情報オブジェクトを提供する。Screen Matrix で IA オブジェクトの定義変更・追加は行わない。
- **Navigation** — 各画面候補が関わる Navigation 分類・状態を提供する。
- **Content Principles** — 各画面候補で扱う Content Category を提供する。
- **CTA Principles** — 利用者へ求める行動の原則を提供する (本タスクでは作成・変更しない)。
- **Screen Requirements** — 各画面候補の具体的な要件を別タスクで定義する。
- **Design System** — 画面を UI として実現する設計語彙を提供する。

## 9. Open Issues

以下は未決である。解決策は推測して記載しない。

- 14 画面候補の正式承認。
- SCR ID の正式採用。
- 各候補の分割・統合。
- Service Entry と Destination Discovery の境界。
- Accommodation Detail と Room and Plan Selection の境界。
- Booking Details と Booking Review の境界。
- Booking Result 後の Navigation。
- Booking Management の提供範囲。
- Booking Change or Cancellation の業務範囲。
- User Access と会員制度の関係。
- Help and Support の対象範囲。
- Editorial Content の分類。
- MyPage の正式構成。
- 会員・非会員の画面差。
- 認証・決済画面の扱い。
- エラー・中断専用画面の要否。
- モバイル・レスポンシブ時の画面分割。
- URL・サイトマップ・画面遷移との対応。
- 既存 Design System との整合性。
- Screen Requirements 策定時に追加候補が必要になる可能性。

## 10. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Initial draft of Travel Screen Matrix | Draft |
