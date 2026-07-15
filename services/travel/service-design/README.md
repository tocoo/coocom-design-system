# Travel Service Design

- Status: In preparation
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Service Design 領域の入口文書
- Position in Repository: `services/travel/service-design/` — Service Design レイヤー (travel サービス配下)。横断共通は [Governance](../../../governance/README.md)、サービス入口は [services/travel/README.md](../README.md) を参照。

本 README は入口文書であり、Service Design の具体的な内容 (原則・IA・ナビゲーション等の本文) は策定しない。ここでは、この領域が「何を管理し／何を管理せず／どの成果物を作り／どの順で参照し／現在どこまで決まっているか」を定義する。

## 1. Purpose

この領域は、国内宿泊サービスの体験設計に関する成果物を管理する。Screen Requirements および Design System に対して**上流基準**を提供することを目的とする。

- 体験設計の原則・情報構造・ナビゲーション・コンテンツ/CTA 方針・画面の全体像・UX 設計判断を、後続レイヤーが参照できる形で集約する。
- 個々の画面の詳細要件や UI 実装語彙は下流レイヤーに委ね、本領域では扱わない。

## 2. Scope

### 管理する対象

- Service Design Principles (サービス体験設計の原則)
- Information Architecture (情報構造と主要オブジェクトの関係)
- Navigation (グローバル・ローカル・文脈ナビゲーション方針)
- Content Principles (コンテンツ設計の原則)
- CTA Principles (CTA の役割・優先順位・利用原則)
- Screen Matrix (画面一覧・責務・関係)
- UX Decision Records (UX 設計判断の記録)
- 上記に関する Service Design の未決事項

### 管理しない対象

- 画面単位の詳細要件 (→ [screen-requirements/](../screen-requirements/README.md))
- UI Component 仕様 (→ [design-system/](../design-system/components.md))
- Design Tokens (→ [design-system/](../design-system/))
- 実装コード (本リポジトリの管理対象外)
- 事業・財務・マーケティング上の未確定戦略
- 推測による利用者像や事業目標

## 3. Information Classification

本領域の各成果物では、情報を以下に区別する。これらを混同しないこと。

- **Fact** — 観察・実測・既存資料で確認できる事実
- **Decision** — 本領域で確定した設計判断
- **Hypothesis** — 暫定的な仮説・仮運用 (未確定)
- **Open Issue** — 未決事項 (確定していない論点)

## 4. Planned Artifacts

今後作成を予定する成果物の一覧。**ID (SD-001 等) は管理用の暫定識別子**であり、正式な恒久採番として確定したものではない (正式採用可否は Open Issues を参照)。

| ID | Artifact | Responsibility | Status |
| --- | --- | --- | --- |
| SD-001 | Service Design Principles | サービス体験設計の原則 | Draft |
| SD-002 | Information Architecture | 情報構造と主要オブジェクトの関係 | Draft |
| SD-003 | Navigation | グローバル・ローカル・文脈ナビゲーション方針 | Draft |
| SD-004 | Content Principles | コンテンツ設計の原則 | Draft |
| SD-005 | CTA Principles | CTA の役割・優先順位・利用原則 | Draft |
| SD-006 | Screen Matrix | 画面一覧・責務・関係の管理 | Draft |
| SD-007 | UX Decision Records | UX 設計判断の記録 | Not started |

SD-001〜SD-006 は Draft として実在する ([principles.md](principles.md) / [information-architecture.md](information-architecture.md) / [navigation.md](navigation.md) / [content-principles.md](content-principles.md) / [cta-principles.md](cta-principles.md) / [screen-matrix.md](screen-matrix.md))。SD-007 (UX Decision Records) は未作成であり、実ファイルは存在しない。

## 5. Reference Order

推奨参照順序は以下とする。未作成の成果物にはリンクを作成せず、未作成である旨を明記する。

1. 本 README
2. [Service Design Principles](principles.md) (SD-001) — Draft
3. [Information Architecture](information-architecture.md) (SD-002) — Draft
4. [Navigation](navigation.md) (SD-003) — Draft
5. [Content Principles](content-principles.md) (SD-004) — Draft
6. [CTA Principles](cta-principles.md) (SD-005) — Draft
7. [Screen Matrix](screen-matrix.md) (SD-006) — Draft
8. UX Decision Records (SD-007) — 未作成
9. Screen Requirements — [screen-requirements/](../screen-requirements/README.md) (未着手)
10. Design System — [design-system/](../design-system/) (既存資産)

## 6. Relationship with Other Layers

### Governance

Service Design は、[Governance](../../../governance/README.md) の原則・規約・決定に従う。ただし、現在 Governance の正本の一部 (Repository principles・命名規則・ADR・レビュー規則・用語定義) は未整備である。参照方法の確定は Open Issues を参照。

### Screen Requirements

Service Design は [Screen Requirements](../screen-requirements/README.md) の上流基準となる。画面単位の詳細要件は Screen Requirements 側で扱い、Service Design 側には記載しない。

### Design System

[Design System](../design-system/) は、Service Design および Screen Requirements を下流で実現する設計語彙である。既存 Design System に記載された内容と Service Design が矛盾する場合、独断でどちらかを正とせず、**Open Issue** として扱う。

### Assets

[Assets](../assets/README.md) は、確定したデザイン資産を管理する別レイヤーである。ロゴ・フォント・アイコン等の実体は Service Design 側で管理しない。

## 7. Current Status

- Service Design Principles (SD-001) が **Draft** として存在する ([principles.md](principles.md))。
- Information Architecture (SD-002) が **Draft** として存在する ([information-architecture.md](information-architecture.md))。
- Navigation (SD-003) が **Draft** として存在する ([navigation.md](navigation.md))。
- Content Principles (SD-004) が **Draft** として存在する ([content-principles.md](content-principles.md))。
- CTA Principles (SD-005) が **Draft** として存在する ([cta-principles.md](cta-principles.md))。
- Screen Matrix (SD-006) が **Draft** として存在する ([screen-matrix.md](screen-matrix.md))。
- UX Decision Records (SD-007) は未作成。
- 国内宿泊サービスの **Design System は既存資産**として存在する ([design-system/](../design-system/))。
- **Screen Requirements は未着手**。
- **Assets は未着手**。
- 上位の事業・ブランド・マーケティング要求 (KPI・事業目標・マネタイズ・会員制度・課金モデル・ロイヤリティ設計・ブランド戦略・コンテンツ戦略・マーケティング戦略・競合戦略) は**未定義**である。
- 未定義事項を AI が推測・補完してはならない。

```text
Status: In preparation
```

## 8. Quality Criteria

今後この領域で作成する成果物には、以下の品質基準を適用する。

- 単独で読んでも理解できる
- 責務が明確
- 他成果物との重複がない
- Fact / Decision / Hypothesis / Open Issue が区別されている
- 設計判断の根拠を追跡できる
- AI が誤読しにくい
- 国内宿泊サービスを最優先とする
- 将来の別サービスでも参考にできる汎用性を意識する
- 未決事項を無理に確定しない

## 9. Open Issues

現時点で確定していない事項。解決策は推測して記載しない。

- Service Design 成果物の正式なファイル名 (命名規則の正本が未整備のため未確定)
- 暫定 ID (SD-001 等) の正式採用可否
- UX Decision Records の記録形式 (ADR との関係・粒度・テンプレート)
- Governance 正本との参照方法 (正本の一部が未整備のため未確定)
- 上位事業要求 (KPI・事業目標・ブランド/マーケティング戦略等) が決定した際の反映方法
- 既存 Design System 文書 (design.md 等) 内に含まれるブランド・体験方針の帰属整理 (Service Design と Design System のどちらの責務とするか)
