# 国内宿泊 (travel)

- サービス名: 国内宿泊
- 暫定サービス識別子: `travel`
- 注記: このディレクトリ名 (`travel`) は**暫定の識別子**である。正式なサービス識別子は未決 (他の表記例として `tvl` 等が確認されている)。確定まで既存識別子で運用する。確定した識別子として扱わないこと。詳細は [governance/owner-decisions.md](../../governance/owner-decisions.md) 確認事項 #8 を参照。

このディレクトリは、国内宿泊サービスの設計資産の入口である。

## レイヤーの責務とリンク

| レイヤー | 責務 | リンク | 状態 |
| --- | --- | --- | --- |
| Service Design | サービスの設計意図・方針 | [service-design/](service-design/README.md) | Draft (SD-001〜SD-007) |
| Screen Requirements | 画面要件 | [screen-requirements/](screen-requirements/README.md) | In preparation |
| Design System | 視覚・トークン・コンポーネント定義 | [design-system/](design-system/) | 既存資産 (Draft) |
| Assets | 設計に付随する資産 | [assets/](assets/README.md) | Not started |

横断の共通規約は [governance/](../../governance/README.md) を参照。

## 推奨参照順序

1. 本 README
2. Service Design → Screen Requirements → Design System → Assets

Design System 内の推奨読み順: `design.md` → `semantic.travel.json` → `primitive.travel.json` → `components.md`

## 現在存在する成果物

- **Service Design** — SD-001〜SD-007 が Draft として存在する。入口: [service-design/README.md](service-design/README.md)
  - [principles.md](service-design/principles.md) (SD-001) / [information-architecture.md](service-design/information-architecture.md) (SD-002) / [navigation.md](service-design/navigation.md) (SD-003) / [content-principles.md](service-design/content-principles.md) (SD-004) / [cta-principles.md](service-design/cta-principles.md) (SD-005) / [screen-matrix.md](service-design/screen-matrix.md) (SD-006) / [ux-decision-records.md](service-design/ux-decision-records.md) (SD-007)
- **Screen Requirements (入口)** — 入口・共通管理構造を定義済 (`In preparation`)。個別 Screen Requirement 文書は未作成。入口: [screen-requirements/README.md](screen-requirements/README.md)
- **Design System (既存資産)** — トークン現行版: primitive 0.3.0 / semantic 0.3.0-draft (Draft)
  - [design-system/design.md](design-system/design.md)
  - [design-system/semantic.travel.json](design-system/semantic.travel.json)
  - [design-system/primitive.travel.json](design-system/primitive.travel.json)
  - [design-system/components.md](design-system/components.md)

Design System は本 bootstrap 以前から存在する既存資産であり、内容は変更していない (移行に伴う参照パス修正を除く)。

## 現在存在しない成果物

- Screen Requirements 個別文書: 未作成 (レイヤー入口は `In preparation`)
- Assets: 未着手 (`Status: Not started`)

未着手・未定義の領域について、要求・仕様を推測して記載しないこと。
