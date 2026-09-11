# インバウンドレンタカー (inbound)

- サービス名: インバウンドレンタカー
- 暫定サービス識別子: `inbound`
- 注記: このディレクトリ名 (`inbound`) は**暫定の識別子**である。正式なサービス識別子は未決 (他の表記例として `irc` 等が確認されている)。確定まで既存識別子で運用する。確定した識別子として扱わないこと。詳細は [governance/owner-decisions.md](../../governance/owner-decisions.md) 確認事項 #8 を参照。

このディレクトリは、インバウンドレンタカーサービスの設計資産の入口である。

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

Design System 内の推奨読み順: `design.md` → `semantic.inbound.json` → `primitive.inbound.json` → `components.md`

## 現在存在する成果物

- **Design System (既存資産)** — トークン現行版: primitive 0.2.2-draft / semantic 0.1.1-draft (Draft、各 JSON の `$meta.version` 準拠)。semantic は移行前に新規生成された経緯を持つ。
  - [design-system/design.md](design-system/design.md)
  - [design-system/semantic.inbound.json](design-system/semantic.inbound.json)
  - [design-system/primitive.inbound.json](design-system/primitive.inbound.json)
  - [design-system/components.md](design-system/components.md)

Design System は本 bootstrap 以前から存在する既存資産である。bootstrap 後の変更は 1 件で、**2026-07-24 (Task 009-18-BP1) に `breakpoint` を旧暫定値 600/768/992/1200 から 3DS 共通値 640/768/1024/1280 へ変更した** (Q5 決定 2026-07-24・Web部責任者。Travel `TVL-0004` の現行 bound 値を 3DS 共通値として再認定したもの = [governance/owner-decisions.md](../../governance/owner-decisions.md) Q5。primitive 0.2.1-draft → 0.2.2-draft、`$status` は placeholder 維持)。あわせて `design.md` の記述を同値へ是正し、表示確認用の代表 viewport (390/768/1280/1440px) を追記した。それ以外の内容は変更していない。

## 現在存在しない成果物

- Service Design: 未着手 (`Status: Not started`)
- Screen Requirements: 未着手 (`Status: Not started`)
- Assets: 未着手 (`Status: Not started`)

未着手の領域について、要求・仕様を推測して記載しないこと。
