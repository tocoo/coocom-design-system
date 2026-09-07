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
| Design System | 視覚・トークン・コンポーネント定義 | [design-system/](design-system/README.md) | 既存資産 (Draft) |
| Assets | 設計に付随する資産 | [assets/](assets/README.md) | Not started |

横断の共通規約は [governance/](../../governance/README.md) を参照。

## 推奨参照順序

1. 本 README
2. Service Design → Screen Requirements → Design System → Assets

Design System 内の推奨読み順: [design-system/README.md](design-system/README.md) → `design.md` → `semantic.rental-car.json` → `primitive.rental-car.json` → `components.md` → `labels-tags.rental-car.md` → `migration-map.md`

見た目を確認するときは `design-system/preview.rental-car.html` (DS 見本ページ・**非正本**) を開く。

## 現在存在する成果物

- **Design System** — トークン現行版: primitive / semantic ともに 0.3.0-draft (Draft)
  - [design-system/README.md](design-system/README.md) — **Design System レイヤーの入口** (成果物の一覧・読み順・正本の所在・責務の境界)
  - [design-system/design.md](design-system/design.md)
  - [design-system/semantic.rental-car.json](design-system/semantic.rental-car.json)
  - [design-system/primitive.rental-car.json](design-system/primitive.rental-car.json)
  - [design-system/components.md](design-system/components.md)
  - [design-system/labels-tags.rental-car.md](design-system/labels-tags.rental-car.md) — ラベル・タグ定義 (A〜H)
  - [design-system/migration-map.md](design-system/migration-map.md) — 実装値から DS 正値への移行対照表 (12 項目)
  - [design-system/preview.rental-car.html](design-system/preview.rental-car.html) — DS 見本ページ (**非正本**。正本のトークンを実際に描画したもの)

Design System は本 bootstrap 以前から存在する既存資産である。0.3.0-draft で国内宿泊 (travel) 0.3.0-draft の Foundation 定義体系を採用し (オーナー判断 2026-08-18・[governance/owner-decisions.md](../../governance/owner-decisions.md) §25)、**2026-09-07 に travel の最新版 (Task 009-58〜009-62) の定義体系を追加で採用した** (同 §29・[Issue #170](https://github.com/tocoo/coocom-design-system/issues/170))。いずれも travel からの自動適用ではなく、rental-car について別途取得した判断である。3 独立 DS の原則は維持し、値は本 DS のファイルに独立して持つ。

## 現在存在しない成果物

- Service Design: 未着手 (`Status: Not started`)
- Screen Requirements: 未着手 (`Status: Not started`)
- Assets: 未着手 (`Status: Not started`)

未着手の領域について、要求・仕様を推測して記載しないこと。
