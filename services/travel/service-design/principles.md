# Travel Service Design Principles

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Service Design に適用する最上位原則
- Position in Repository: `services/travel/service-design/principles.md` — Service Design レイヤー (travel サービス配下)。入口は [README.md](README.md)、横断共通は [Governance](../../../governance/README.md) を参照。

## 1. Purpose

本文書は、国内宿泊サービスの体験設計に適用する上位原則 (Service Design Principles) を管理する。

- これらの原則は、今後策定する Information Architecture / Navigation / Content Principles / CTA Principles / Screen Matrix / Screen Requirements、および Design System のレビューに共通して適用する**判断基準**である。
- 個別の解決策 (具体的な画面・導線・文言・仕様) ではなく、**設計判断を行う際の原則**を扱う。
- 上位の事業・ブランド・利用者要求の多くが未定義である状況でも適用できるよう、画面・機能に依存しない抽象度で定義する。

## 2. Preconditions

### Facts

- 国内宿泊サービスの Service Design 成果物は、本タスク以前には未作成だった。
- 既存 Design System は存在する ([design-system/](../design-system/))。
- 上位事業要求 (KPI・事業目標・マネタイズ・会員制度・課金モデル・ロイヤリティ設計・ブランド戦略・コンテンツ戦略・マーケティング戦略・競合戦略) の多くは未定義である。
- Repository は設計の Single Source of Truth として構築されている。

### Decisions

- 本文書の 10 原則を、後続 Service Design 成果物の Draft 判断基準として使用する。
- 各原則は具体的な仕様を直接決めるものではない。
- 未定義事項を推測で補完しない。

### Hypothesis

- なし。

### Open Issues

- 原則の正式承認状態。
- Governance の Repository Principles との関係。
- アクセシビリティ規格・達成基準。
- Evidence の記録方法。
- 原則間の優先順位。

## 3. How to Use These Principles

- 各原則は本タスクで採用する **Decision** として記述する。ただし、原則から具体的な仕様が自動的に確定するわけではない。各原則の `Does Not Decide` に、その原則だけでは決まらない事項を明示する。
- 後続成果物 (IA・Navigation・Content・CTA・Screen Matrix・Screen Requirements) を策定・レビューする際、および Design System をレビューする際の判断基準として使用する。
- 文書内の情報は **Fact / Decision / Hypothesis / Open Issue** に区別する。未確定の前提を事実として扱わない。
- 原則同士が競合した場合は §5 Conflict Resolution に従う。
- 原則は 10 件で固定であり、本文書内で新しい原則を追加しない。重複が疑われる場合も独断で統合・削除せず、Open Issue として扱う。

## 4. Principles

## SDP-001: User Task Clarity

### Decision

利用者が現在何を行い、次に何を行えるかを理解できることを優先する。

### Rationale

複数の後続成果物 (IA・Navigation・Screen) が個別に設計されても、利用者が役割・現在地・次の行動を理解できる状態をサービス共通の下限として保つため。未定義の利用者像に依存せずに適用できる基準が必要である。

### Application

- 各画面・情報・操作の役割を明確にする。
- 利用者に内部構造や運営都合を推測させない。
- 選択肢・現在地・次の行動を曖昧にしない。

### Does Not Decide

- 具体的な導線
- CTA 文言
- 画面数
- 予約フローの詳細

### Related Artifacts

- Information Architecture / Navigation / Screen Matrix / Screen Requirements

## SDP-002: Progressive Commitment

### Decision

利用者へ、必要以上に早い判断・入力・確約を求めない。

### Rationale

会員制度・課金モデル・入力項目などの上位要求が未定義であるため、特定の確約フローを前提にできない。判断・入力の要求時期を後続設計が判断する際の共通基準として必要である。

### Application

- 情報理解の前に会員登録や入力を強制しない。
- 判断に必要な情報は、その判断より前に提示する。
- 費用・条件・制約を、取消困難な操作の後に初めて示さない。

### Does Not Decide

- 会員登録の有無
- 課金モデル
- 入力項目
- 予約確定条件

### Related Artifacts

- Navigation / CTA Principles / Screen Requirements

## SDP-003: Transparent Conditions

### Decision

価格、条件、制約、例外を、判断可能な時点で理解できる状態にする。

### Rationale

表示と実際の条件の不整合は、サービス全体の信頼性と長期運用上の整合性を損なう。価格構成やポリシーが未確定の段階でも、情報提示の透明性を判断する基準が必要である。

### Application

- 重要条件を意図的に隠さない。
- 表示上の優位性と実際の条件を矛盾させない。
- 「安い」「おすすめ」などの評価表現には根拠が必要である。
- 未取得・未確定の情報は確定情報のように見せない。

### Does Not Decide

- 価格構成
- キャンセルポリシー
- ランキング基準
- 表示する具体的な項目

### Related Artifacts

- Content Principles / Screen Requirements / Design System

## SDP-004: Consistent Mental Model

### Decision

同じ概念・状態・操作は、サービス全体で一貫した意味を持つことを優先する。

### Rationale

Repository を Single Source of Truth とし、複数の成果物・レイヤーを横断して整合させる長期運用要件があるため。概念・用語・操作の不整合は後続成果物間の矛盾を生む。

### Application

- 同じ言葉を異なる意味で使用しない。
- 同じ状態を異なる表現で混在させない。
- 画面ごとに異なる操作原則を独自に導入しない。
- IA、Navigation、Content、CTA、Design System 間の不整合を避ける。

### Does Not Decide

- 正式な用語
- Component 仕様
- ビジュアルの統一方法
- 命名規則

### Related Artifacts

- Information Architecture / Navigation / Content Principles / CTA Principles / Design System

## SDP-005: State Visibility

### Decision

現在の状態、処理結果、変更の影響を利用者が把握できることを優先する。

### Rationale

状態表示とシステム実態の不整合は、回復性や信頼性に影響する。予約状態の業務定義が未確定でも、状態の可視性を設計判断する基準が必要である。

### Application

- 読み込み中・成功・失敗・在庫変動などの状態を隠さない。
- 操作が受け付けられたかを利用者に伝える。
- 元に戻せない変更や影響範囲を事前に示す。
- システム上の状態と画面表示を矛盾させない。

### Does Not Decide

- 状態の具体的な一覧
- エラー文言
- Loading Component 仕様
- 予約状態の業務定義

### Related Artifacts

- Screen Requirements / Design System

## SDP-006: Recoverability

### Decision

誤操作・入力ミス・一時的な失敗から回復できる設計を優先する。

### Rationale

回復性は特定の機能仕様に依存しない体験品質であり、保存期間やキャンセル可否が未確定でも、回復手段の要否を判断する共通基準として必要である。

### Application

- 可能な範囲で、やり直し・修正・戻る手段を提供する。
- エラー時に原因と次の行動を理解できるようにする。
- 途中入力を不必要に失わせない。
- 回復不可能な操作には、それに見合う事前確認を設ける。

### Does Not Decide

- 保存期間
- キャンセル可否
- Undo 機能の実装
- エラー処理仕様

### Related Artifacts

- Navigation / Screen Requirements / Design System

## SDP-007: Accessibility by Default

### Decision

特定の利用条件を前提にせず、可能な限り幅広い利用者・環境で理解し操作できることを基本とする。

### Rationale

アクセシビリティを後工程の検査項目に限定すると、後続成果物と Design System 全体での担保が困難になる。適用する具体規格が未確定でも、設計初期からの基準として必要である。

### Application

- 色だけに意味を依存させない。
- 読みやすさ・操作可能性・情報理解を視覚表現より優先する。
- キーボード・支援技術・異なる画面サイズを設計上の例外としない。
- アクセシビリティを後工程だけの検査項目にしない。

### Does Not Decide

- 適用する具体的な規格
- 達成レベル
- 実装方式
- 個別 Component の仕様

### Related Artifacts

- Content Principles / Screen Requirements / Design System

## SDP-008: Evidence over Assumption

### Decision

確認できていない利用者・事業・運用上の前提を、事実として扱わない。

### Rationale

上位要求の多くが未定義であり、Fact / Decision / Hypothesis / Open Issue の区別は Repository 運営方針である。根拠の追跡可能性を保つために必要である。

### Application

- 未定義の要求を AI や設計者が補完しない。
- 仮説は Hypothesis として明示する。
- 設計判断の根拠を追跡できる状態にする。
- 根拠が不足している場合は Open Issue として保持する。

### Does Not Decide

- 必要な調査方法
- Evidence の保存形式
- 意思決定者
- 承認フロー

### Related Artifacts

- Screen Matrix / Screen Requirements (全成果物に横断して適用する)

## SDP-009: Service-wide Coherence

### Decision

画面単体の最適化より、サービス全体の整合性を優先する。

### Rationale

上流の Service Design と下流成果物を分断しないことは、Repository を横断整合させる長期運用要件である。局所最適が全体導線や他画面を損なう事態を避ける。

### Application

- 一画面の利便性向上が、別画面や全体導線を損なわないか確認する。
- 同じ情報・判断を複数画面で矛盾させない。
- 上流の Service Design と下流成果物を分断しない。
- 変更時は影響する画面・情報・Component を確認する。

### Does Not Decide

- 画面構成
- 共通 Component の範囲
- 変更管理手順
- レビュー体制

### Related Artifacts

- Information Architecture / Screen Matrix / Screen Requirements / Design System

## SDP-010: Incremental Definition

### Decision

未決事項を無理に確定せず、確定可能な範囲から設計を積み上げる。

### Rationale

上位要求が未定義でも作業を停止しない一方、未決事項へ依存する設計を確定しない運営方針が必要である。後から変更可能な構造を保つことは長期運用要件である。

### Application

- 上位要求が未定義でも、依存しない範囲の設計は進める。
- 未決事項を理由に全作業を停止しない。
- 一方で、未決事項へ依存する設計を確定しない。
- 後から変更可能な構造を維持する。

### Does Not Decide

- 優先順位
- スケジュール
- リリース単位
- 暫定仕様の期限

### Related Artifacts

- Screen Matrix / Screen Requirements

## 5. Conflict Resolution

原則同士が競合する場合の扱いを以下とする。

1. 原則間に固定の優先順位は設定しない。
2. 対象となる利用者タスクと影響範囲を明確にする。
3. どの原則をどの理由で優先したかを記録する。
4. 根拠不足の場合は Open Issue として保持する。
5. 画面単体ではなく、サービス全体への影響を確認する。
6. 事業判断が必要な場合は、Service Design 内で推測して決めない。

具体的な UX Decision Records の記録形式は本タスクで決定しない (Open Issue)。

## 6. Relationship with Other Artifacts

具体的な下流仕様は本文書に記載しない。各原則は以下の判断基準として使用する。

- **Information Architecture** — 情報の分類・関係・構造を判断する基準として使用する。
- **Navigation** — 現在地・選択肢・移動可能性を設計する際の基準として使用する。
- **Content Principles** — 情報の明確性、透明性、一貫性を判断する上位基準として使用する。
- **CTA Principles** — 利用者へ求める判断・行動の時期や明確性を判断する上位基準として使用する。
- **Screen Matrix** — 各画面の責務とサービス全体の整合性を評価する基準として使用する。
- **Screen Requirements** — 画面要件を定義・レビューする際の上位基準として使用する。
- **Design System** — Component や Token が利用者の理解・状態把握・アクセシビリティを支えるかをレビューする基準として使用する。

## 7. Open Issues

以下は未決である。解決案は推測して記載しない。

- 10 原則の正式承認。
- Governance の Repository Principles との重複・関係。
- 各原則の優先順位を設けるか。
- Accessibility の具体的な基準。
- Evidence の定義と記録方法。
- 原則違反をどのレビュー工程で判定するか。
- UX Decision Records との接続方法。
- 既存 Design System との不整合確認。

## 8. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-14 | Initial draft of Travel Service Design Principles | Draft |
