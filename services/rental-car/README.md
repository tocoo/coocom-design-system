# 国内レンタカー (rental-car)

- サービス名: 国内レンタカー
- 暫定サービス識別子: `rental-car`
- 注記: このディレクトリ名 (`rental-car`) は**暫定の識別子**である。正式なサービス識別子は未決 (他の表記例として `drc` / `japan` 等が確認されている)。確定まで既存識別子で運用する。確定した識別子として扱わないこと。詳細は [governance/owner-decisions.md](../../governance/owner-decisions.md) 確認事項 #8 を参照。

このディレクトリは、国内レンタカーサービスの設計資産の入口である。

## レイヤーの責務とリンク

| レイヤー | 責務 | リンク | 状態 |
| --- | --- | --- | --- |
| Service Design | サービスの設計意図・方針 | [service-design/](service-design/README.md) | Not started |
| Screen Requirements | 画面要件 | [screen-requirements/](screen-requirements/README.md) | Not started |
| Design System | 視覚・トークン・コンポーネント定義 | [design-system/](design-system/) | 既存資産 (Draft) |
| Assets | 設計に付随する資産 | [assets/](assets/README.md) | Not started |

横断の共通規約は [governance/](../../governance/README.md) を参照。

## 推奨参照順序

1. 本 README
2. Service Design → Screen Requirements → Design System → Assets

Design System 内の推奨読み順: `design.md` → `semantic.rental-car.json` → `primitive.rental-car.json` → `components.md`

## 現在存在する成果物

- **Design System (既存資産)** — トークン現行版: primitive 0.2.0 / semantic 0.2.1-draft (Draft)
  - [design-system/design.md](design-system/design.md)
  - [design-system/semantic.rental-car.json](design-system/semantic.rental-car.json)
  - [design-system/primitive.rental-car.json](design-system/primitive.rental-car.json)
  - [design-system/components.md](design-system/components.md)

Design System は本 bootstrap 以前から存在する既存資産であり、内容は変更していない。

## 現在存在しない成果物

- Service Design: 未着手 (`Status: Not started`)
- Screen Requirements: 未着手 (`Status: Not started`)
- Assets: 未着手 (`Status: Not started`)

未着手の領域について、要求・仕様を推測して記載しないこと。
