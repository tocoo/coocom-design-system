# 移行対照表 — 国内レンタカー (rental-car)

- 種別: DS 成果物 (移行資料)
- 状態: Draft
- 作成日: 2026-08-19
- 目的: 実装 (`tocoo/tocoo_rental_car` の japan ゾーン) に残る旧値を事実として記録し、DS の正値との対応を示す

## 1. 位置づけ

結論: 左列は実装から実測した事実値であり、DS の正値ではない。新規制作では右列だけを使う。

旧値を DS のトークンに含めない (実装の値をそのまま正としない)。既存画面の置換は段階導入とし、本表を差し替えの単位として使う。

## 2. 対照表

結論: 12 項目。いずれも 2026-08-18 のオーナー判断「国内宿泊で新たに定義されたものを適用する」により右列が正となった。

| 対象 | 実装の事実値 (廃止) | DS の正値 | 出典 |
| --- | --- | --- | --- |
| 主色 | #9E2334 (DS 暫定) / #9B2030 ($tocooRed・検索ボタン) / #9F1E30 (お知らせ見出し) | `color.brand.primary` = スキーム主色 (#2C50C8 / #4845D4) | `gulp/scss/japan/mixin/_mixin.scss`, `webroot/japan/css/files/assets/css/rentacar_top.scss` |
| リンク | $linkColor #0050a0 / hover $hoverColor #06f | `color.text.link` = 主色 (per-scheme) | `webroot/japan/css/files/assets/css/mixin/_mixin.scss` |
| ヘッダー / フッター | 紺 #283593 (リンク色・フッター背景ベタ塗り) | `surface.default` / `surface.subtle` + `border.subtle`。強調は主色 | `gulp/scss/japan/header_new.scss`, `footer_new.scss` |
| CTA・状態色 | $ctaColor 緑 #43a047 / $tocooBlue #2b4b65 | `action.primary` = 主色 / `state.success` = 主色 (専用の緑は廃止) | `webroot/japan/css/files/assets/css/mixin/_mixin.scss` |
| ボタン | 角丸 4px + 縦グラデ (gradient-top-lighten) + emboss 影 + text-shadow | `radius.action` = pill・単色・影なし。hover は opacity .85 | `contents_search.scss` #BtnSearch, mixin `buttonRed()` |
| 本文 | 15px / lh 1.4 / Kozuka Gothic Pro・游ゴシック・Roboto 混在 | 1rem (16px) / lh 1.8 / LINE Seed JP | `rentacar_top.scss` #copy, layerB §3-2 |
| スペーシング | 5px 刻みユーティリティ (5 / 10 / 15 / 20 / 30 / 50px) | 4px (0.25rem) 系 `spacing.1`〜`16` | `contents_search.scss`, `rentacar_top.scss` |
| ブレークポイント | 2 段 (pc: max 959px / pc_min: min 960px) + 576 / 992 / 1200 の混在 | 640 / 768 / 1024 / 1280 | `gulp/scss/japan/mixin/_mixin.scss`, `header_new.scss` |
| コンテナ | 960px (旧) / 1280px (新ヘッダー) の二重基準 | 975 / 1195 / 1425px | `contents_new.scss`, `header_new.scss` |
| 並び替え | 常時展開の帯 `.sort` (#f9f9f9 + 上下境界 #f1f1f1・高さ 56px / 選択は下線 4px #000 + bold / 右トグル #ededed・選択 #e1e1e1) | トリガー (pill 44px) + 並び替えパネル。SP は追従バーに絞り込み (件数バッジ) と並置 | 実装: `import_rent.css` (`.sort` L2628-2678 / L4123-4176)。移行先: 国内宿泊 search-result |
| ラベル・タグ | `.cat-label` 92x25px 固定・三角の尾 #8C4801・分類色 #060 (kusairo) / #c90 (oudoiro)。器の統一なし | 器を 1 つに固定 (sm 20 / md 24px・左右 8 / 12・角丸 4px・行高 1) し、カテゴリ A〜H は面と文字だけで区別 | 実装: `rentacar_top.scss` (`.cat-label` / `.kusairo` / `.oudoiro`)。移行先: 国内宿泊 ラベル・タグ定義シート (2026-08-10) |
| アイコン / オーバーレイ | FontAwesome 4 記法・slick 由来 / remodal (LightBox) | Font Awesome 6 / オーバーレイは drawer 系に統一 (`🚧` 3 DS 横断の実装基盤は未決) | mixin `fa()`, `rentacar_top.scss` `.remodal` |

## 3. 置換の順序

結論: 色とトークン参照を先に通し、形状と構造の置換を後に回す。

1. 変数層の差し替え (主色・リンク・状態色・テキスト・境界)。ここだけで大半の画面の色が正値へ寄る
2. 書体と本文サイズ・行高。段組の高さが動くため、色の後に単独で行う
3. 形状 (ボタンの pill 化・影とグラデの除去)・スペーシングの 4px 化
4. 構造 (検索の多経路集約・並び替えのトリガー + パネル化・ラベルの器統一)。画面単位で段階導入する

## 4. 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-08-19 | 初版 (12 項目)。実装実測値と 0.3.0-draft の正値の対応を記録 | Claude Design |
| 2026-08-20 | 本 Repository へ新設 (0.3.0-draft)。実装 (japan ゾーン) の旧値 12 項目と DS 正値の対応を記録。根拠はオーナー判断 2026-08-18 (記録 = [governance/owner-decisions.md](../../../governance/owner-decisions.md) §25) | Claude Code |
