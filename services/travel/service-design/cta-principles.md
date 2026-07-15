# Travel CTA Principles

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の CTA 設計原則の初版 Draft
- Position in Repository: `services/travel/service-design/cta-principles.md` — Service Design レイヤー (travel サービス配下)。入口は [README.md](README.md)、参照する上流成果物は [principles.md](principles.md) / [information-architecture.md](information-architecture.md) / [navigation.md](navigation.md) / [content-principles.md](content-principles.md)、横断共通は [Governance](../../../governance/README.md)。下流の [Screen Matrix](screen-matrix.md) との関係は §7 を参照。

## 1. Purpose

本文書は、国内宿泊サービスにおける CTA (利用者へ行動を求める要素) の設計原則の Draft 正本である。

- どの行動を CTA として扱うか、複数行動の優先順位、確約を伴う行動の扱い、条件・結果・影響の提示、状態、Navigation との境界を定義する。
- 後続の Screen Matrix / Screen Requirements、および Design System のレビューに、共通の CTA 基準を提供する。
- 対象はボタンの見た目ではなく設計判断である。具体的な CTA 文言・UI Component・レイアウト・画面別配置は決定しない。

## 2. Preconditions

### Facts

- [Service Design Principles](principles.md) は Draft として存在する。
- [Information Architecture](information-architecture.md) は Draft として存在する。
- [Navigation](navigation.md) は Draft として存在する。
- [Content Principles](content-principles.md) は Draft として存在する。
- [Screen Matrix](screen-matrix.md) は Draft として存在する。
- CTA Principles は本タスク以前には未作成だった。
- 正式な CTA 文言、画面別 CTA、予約・決済フローは未定義である。

### Decisions

- 10 の CTA Principles を初版 Draft の判断基準とする。
- 5 つの CTA 分類を初版 Draft として扱う。
- Commitment Level Model と CTA State Model を定義する。
- 具体的な CTA 文言・UI・画面仕様は定義しない。
- 未定義事項を推測で補完しない。

### Hypothesis

- なし。

### Open Issues

- 画面別主要 CTA。
- 予約・決済・取消の正式な確約レベル。
- CTA ラベル。
- 会員登録・ログイン誘導。
- モバイル CTA。
- 法務・同意表現。
- Design System との対応。

## 3. CTA Principles

判断基準として、以下の [Service Design Principles](principles.md) を主に参照する: SDP-001〜010。原則から具体的な仕様が自動的に決まるわけではない。本文書内で新しい原則を独断で追加・統合・削除しない。

## CTA-001: Action Clarity

### Decision

利用者が、行動の内容と結果を実行前に理解できること。

### Rationale

行動の内容・結果が不明なままの実行は誤操作と不信を招く (SDP-001)。

### Application

- 行動の対象を明確にする。
- 実行後に起きることを予測可能にする。
- 対象不明な「次へ」「送信」等を無条件に使用しない。

### Does Not Decide

- 具体文言 / ボタンサイズ / 配置 / アイコン。

### Related Artifacts

- Content Principles / Screen Requirements / Design System

## CTA-002: One Clear Primary Action

### Decision

同一の判断文脈では、主要行動を明確にし、複数の行動を同等に競合させないこと。

### Rationale

主要行動が埋没すると判断が困難になり、サービス全体の一貫性も損なう (SDP-001 / SDP-009)。

### Application

- 主要行動と補助行動を区別する。
- 同一文脈で主要 CTA を過剰に複数化しない。
- 主要性は事業都合だけで決定しない。

### Does Not Decide

- 画面別の主要 CTA / 色 / 視覚階層 / CTA 数の上限。

### Related Artifacts

- Screen Matrix / Screen Requirements / Design System

## CTA-003: Commitment-aware Emphasis

### Decision

確約、予約、支払、取消等の影響が大きい行動ほど、条件と結果を明確にすること。

### Rationale

影響の大きい行動での誤解は回復困難な結果を招く (SDP-002 / SDP-003)。

### Application

- 確約レベルを行動前に理解可能にする。
- 予約成立、支払、取消等を曖昧な表現にしない。
- 影響が大きい行動は確認可能性を高める。

### Does Not Decide

- 確認画面の有無 / 法務文言 / 決済仕様 / 予約成立条件。

### Related Artifacts

- Content Principles / Screen Matrix / Screen Requirements

## CTA-004: Progressive Commitment

### Decision

理解・比較・確認より前に、必要以上の入力・登録・確約を求めないこと。

### Rationale

早すぎる確約要求は離脱を招き、判断の前提を損なう (SDP-002)。

### Application

- 情報理解前の会員登録や入力強制を避ける。
- 比較・確認の前に確約を求めない。
- タスク進行に必要な段階でのみ行動を要求する。

### Does Not Decide

- 会員登録の有無 / 入力項目 / 正式なフロー / ゲスト予約可否。

### Related Artifacts

- Navigation / Screen Matrix / Screen Requirements

## CTA-005: Conditions Before Action

### Decision

Price、Policy、Availability、変更・取消条件等を、行動前に確認可能にすること。

### Rationale

重要条件が行動後に判明すると透明性を損なう (SDP-003)。

### Application

- CTA 対象に関連する Price、Policy、Availability を確認可能にする。
- 重要条件を実行後に初めて示さない。
- 条件変更の可能性を必要に応じて明示する。

### Does Not Decide

- 表示位置 / 価格構造 / Policy 分類 / 更新頻度。

### Related Artifacts

- Information Architecture / Content Principles / Screen Requirements

## CTA-006: Reversible Before Irreversible

### Decision

修正可能な行動と取消困難な行動を区別し、回復可能性を明確にすること。

### Rationale

不可逆な行動を軽い行動と誤認すると回復できない (SDP-006)。

### Application

- 修正、戻る、取消可能性を理解できるようにする。
- 不可逆な行動を軽い行動のように見せない。
- 取消困難な行動では影響を確認可能にする。

### Does Not Decide

- Undo 仕様 / 取消期限 / 確認ダイアログ / 状態遷移。

### Related Artifacts

- Navigation / Screen Requirements / Design System

## CTA-007: Explicit State and Availability

### Decision

利用可能、利用不能、処理中、完了、失敗等の状態を曖昧にしないこと。

### Rationale

状態が曖昧だと多重実行や誤認が生じる (SDP-005)。

### Application

- Disabled、Loading、Success、Error 等を区別する。
- 利用不能理由を可能な範囲で示す。
- 多重実行や処理中の誤認を防ぐ。

### Does Not Decide

- 技術的な状態管理 / Component 仕様 / タイムアウト / 再試行ロジック。

### Related Artifacts

- Content Principles / Screen Requirements / Design System

## CTA-008: Consistent Meaning

### Decision

同じ役割・結果を持つ CTA は、一貫した意味と扱いを持つこと。

### Rationale

同一ラベルが異なる結果を生むと学習コストと誤操作を招く (SDP-004 / SDP-009)。

### Application

- 同じラベルが異なる結果を生まないようにする。
- 同じ役割の CTA を画面ごとに別概念として扱わない。
- Navigation と CTA の意味を混同しない。

### Does Not Decide

- 正式な用語集 / Component 名 / 視覚スタイル / 画面別ラベル。

### Related Artifacts

- Navigation / Content Principles / Design System

## CTA-009: Accessible Activation

### Decision

キーボード、支援技術、異なる画面サイズ等でも、行動の意味と実行可能性を失わせないこと。

### Rationale

視覚のみに依存する CTA は環境・支援技術で意味を失う (SDP-007)。

### Application

- 視覚表現だけで主要性や状態を伝えない。
- 支援技術で役割・状態・結果を理解可能にする。
- 操作対象として認識・実行できるようにする。

### Does Not Decide

- 適用規格 / サイズ基準 / フォーカス実装 / Component 仕様。

### Related Artifacts

- Content Principles / Design System / Screen Requirements

## CTA-010: No Unsupported Pressure

### Decision

根拠のない緊急性、希少性、損失回避、過度な販促圧力で行動を誘導しないこと。

### Rationale

根拠のない圧力は誤認を招き、事実と販促の区別を損なう (SDP-003 / SDP-008)。

### Application

- 根拠のない残数・期限・人気表現を CTA 近辺で使用しない。
- 行動しないことへの不当な不利益を示唆しない。
- 販促表現と事実・条件を区別する。

### Does Not Decide

- キャンペーン方針 / 根拠基準 / ランキングロジック / マーケティングコピー。

### Related Artifacts

- Content Principles / Screen Requirements

## 4. CTA Classification

5 分類を Draft として定義する。`CTA-TYPE-001`〜`005` は暫定識別子である。分類の追加・変更は行わない。

- **CTA-TYPE-001: Primary Task Action** — 利用者の主要タスクを前進させる行動。
- **CTA-TYPE-002: Secondary Task Action** — 主要タスクを補助、比較、修正、保留する行動。
- **CTA-TYPE-003: Navigation Action** — 情報や別領域への移動を主目的とする行動。Navigation と重なるため、CTA として強調する必要性を別途判断する。
- **CTA-TYPE-004: Recovery Action** — エラー、中断、入力不備、利用不能状態から回復する行動。
- **CTA-TYPE-005: Destructive or High-impact Action** — 取消、削除、確約、支払等、影響が大きい行動。

Key Principles は §3 の CTA を参照する。

| CTA Type | Purpose | Typical Context | Key Principles | Status |
| --- | --- | --- | --- | --- |
| Primary Task Action | 主要タスクを前進させる | 探索・選択・予約 | CTA-001 / 002 / 003 / 004 / 005 | Draft |
| Secondary Task Action | 比較・修正・保留を支援する | 条件変更・戻る・再検討 | CTA-001 / 002 / 006 / 008 | Draft |
| Navigation Action | 情報や別領域へ移動する | 詳細・Policy・Review・Support | CTA-001 / 008 / 009 | Draft |
| Recovery Action | 問題から回復する | Error / Interrupted | CTA-001 / 006 / 007 / 009 | Draft |
| Destructive or High-impact Action | 影響が大きい行動を扱う | 予約確定・支払・取消 | CTA-003 / 005 / 006 / 007 | Draft |

## 5. Commitment Level Model

これは業務上の正式な状態遷移や法務上の同意区分を定義するものではない。

| Commitment Level | Meaning | CTA Requirement | Status |
| --- | --- | --- | --- |
| Informational | 情報確認のみで状態を変更しない | 移動先・対象を明確にする | Draft |
| Reversible | 後から容易に修正・取消できる | 戻り方・変更可能性を理解可能にする | Draft |
| Conditional | 条件により結果や費用が変わり得る | 条件・Price・Policy を行動前に確認可能にする | Draft |
| High Commitment | 予約成立・支払等の重要な確約 | 結果・影響・条件を明確にし、誤操作を防ぐ | Draft |
| Destructive | 取消・削除等、既存状態を失わせる | 影響と回復不能性を明確にする | Draft |

## 6. CTA State Model

システム実装上の状態一覧や Component 仕様は定義しない。

| CTA State | Meaning | Required Communication | Status |
| --- | --- | --- | --- |
| Available | 実行可能 | 行動内容と結果を理解できる | Draft |
| Unavailable | 現在実行できない | 利用不能理由または必要条件を可能な範囲で示す | Draft |
| Loading / Processing | 実行を受け付け処理中 | 処理中であることと多重実行防止を示す | Draft |
| Success | 行動が完了した | 結果と次に可能な行動を示す | Draft |
| Error | 行動が完了しなかった | 問題概要と再試行・修正・戻る等を示す | Draft |
| Pending Confirmation | 追加確認が必要 | 確約前に対象・条件・影響を確認可能にする | Draft |

## 7. Relationship with Screen Matrix

[Screen Matrix](screen-matrix.md) の 14 画面候補について、CTA 上の主な考慮事項を整理する。具体的な CTA ラベルや画面別主要 CTA は決定しない。

| Screen ID | Screen Candidate | CTA Consideration | Status |
| --- | --- | --- | --- |
| SCR-001 | Service Entry | 探索開始と補助導線を競合させない | Draft |
| SCR-002 | Destination Discovery | 発見・探索と販促誘導を混同しない | Draft |
| SCR-003 | Accommodation Search | 条件入力・変更・検索開始を明確にする | Draft |
| SCR-004 | Search Results | 比較・詳細確認・条件変更・選択の優先関係を整理する | Draft |
| SCR-005 | Accommodation Detail | 情報確認と Room / Stay Plan 選択を区別する | Draft |
| SCR-006 | Room and Plan Selection | 条件確認前に予約確約へ進ませない | Draft |
| SCR-007 | Booking Details | 入力継続・修正・中断の扱いを明確にする | Draft |
| SCR-008 | Booking Review | 確約前に Price・Policy・対象・入力内容を確認可能にする | Draft |
| SCR-009 | Booking Result | 結果確認と次の行動を明確にする | Draft |
| SCR-010 | Booking Management | 確認・変更・取消・Support を競合させない | Draft |
| SCR-011 | Booking Change or Cancellation | 影響が大きい行動を明確に区別する | Draft |
| SCR-012 | User Access | 認証・登録を必要以上に早く要求しない | Draft |
| SCR-013 | Help and Support | 問題解決・問い合わせ・戻り先を明確にする | Draft |
| SCR-014 | Editorial Content | 編集情報と予約・販促 CTA の性質を区別する | Draft |

## 8. Boundary between CTA and Navigation

- Navigation は情報・領域・文脈間の移動を支援する。
- CTA は利用者に特定の行動を求め、タスクや状態を前進・変更させる。
- すべてのリンクを CTA として強調しない。
- Navigation Action を主要 CTA として扱うかは、利用者タスクと画面責務に基づき判断する。
- CTA と Navigation で同じ表現を使う場合も、役割と結果を混同しない。
- 具体的な UI 分類は Design System 側で定義する。

## 9. Relationship with Content Principles

- CTA ラベルは行動と結果を予測可能にする。
- 条件、Price、Policy、Availability を必要な位置で確認可能にする。
- Fact、条件、販促表現を混同しない。
- CTA の状態と利用不能理由を曖昧にしない。
- エラー時は回復可能な行動を示す。
- 具体的な文言は本タスクで決定しない。

## 10. Relationship with Other Artifacts

- **Service Design Principles** — CTA 判断の上位基準。
- **Information Architecture** — CTA が対象とする情報オブジェクトを提供する。CTA 側で IA を変更しない。
- **Navigation** — 移動を主目的とする行動との境界を提供する (§8)。
- **Content Principles** — CTA の表現・状態・条件提示の原則を提供する (§9)。
- **Screen Matrix** — 各画面候補での CTA 考慮を整理する (§7)。
- **Screen Requirements** — 画面単位の具体的な CTA 要件を別タスクで定義する。
- **Design System** — CTA を UI (Button / Link / State 等) として実現する設計語彙を提供する。

## 11. Open Issues

以下は未決である。解決策は推測して記載しない。

- 10 原則の正式承認。
- CTA ID の正式採用。
- CTA 分類の正式承認。
- Commitment Level の正式承認。
- CTA State の正式承認。
- 画面別主要・副次 CTA。
- CTA と Navigation Action の正式な区別。
- Booking Details / Booking Review / Booking Result の CTA 責務。
- 予約成立・支払・変更・取消の確約レベル。
- 会員登録・ログイン CTA の扱い。
- MyPage・予約管理領域の CTA。
- モバイル・固定 CTA。
- CTA ラベル・用語集。
- Price・Policy・Availability の近接表示基準。
- 根拠ある緊急性・希少性表現の基準。
- 法務・広告・同意要件との整合性。
- アクセシビリティの具体基準。
- 既存 Design System の Button / Link / State との整合性。
- Screen Requirements 策定時に追加分類が必要になる可能性。

## 12. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Initial draft of Travel CTA Principles | Draft |
