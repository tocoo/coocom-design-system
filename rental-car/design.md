# 国内レンタカー Design System (rental-car)

- 種別: DS 成果物 (design.md = 統合文書)
- 状態: Draft
- 作成日: 2026-07-02
- 対象: 顧客向け UI のみ (P3/ADR-0012。管理画面は対象外)
- 実装の所在: GitHub `tocoo/tocoo_rental_car` の `japan` ゾーン (P6/ADR-0004)。インバウンドと同一リポだが DS は独立 (P1)
- 独立性: 本 DS は国内宿泊・インバウンドレンタカーと Foundation/Semantic/design.md を共有しない (P1/ADR-0022)。命名・運用規約のみ共通 (P2)
- 非構築: 100選 (must-visit ゾーン) は DS 対象外 (2026-07-01 オーナー確認)

---

## 1. 概要・ブランド位置づけ

- [事実] サービス: ToCoo! 国内レンタカー (www2.tocoo.jp/jp/)
- [事実] 主色: 赤系。ただし正値は3候補で未確定 ❓ Q1 (分類C・オーナー判断)
  - 候補: (a) `#9E2334` (b) `#9B2030` (c) `#9F1E30`。暫定運用 = `#9E2334`
  - [事実] japan ゾーンの本番実装値は `#9B2030` (layerB §3-2 実測: 検索ボタン)。暫定値と実装値の差を認識して扱う
  - [事実] Q1 の選定はインバウンドの赤 (`#9E2334`) へ自動適用しない (Q1 注記 2026-07-01)
- [観察] コピートーンは実用・価格訴求 (CP-01)。CTA 文言例「卸価格を検索」(CP-02)
- [観察] 3サービス中で素材が最も揃うが、ボタン状態・フォーム実体・リンク色が未取得/未確定

## 2. カラー

正: `semantic.rental-car.json` → `primitive.rental-car.json`。以下は要約。

| 用途 (Semantic) | 参照 | 値 | 状態 |
| --- | --- | --- | --- |
| `color.brand.primary` | `{color.palette.red.700}` | `#9E2334` (暫定) | 🚧 Q1 |
| `color.brand.primaryHover` | `{color.palette.red.800}` | `#9B2030` (暫定) | 🚧 Q1 / follow-up #4 |
| `color.text.strong` / `body` | gray.900 / gray.800 | `#212121` / `#424242` | 🚧 Q2 (国内実測は `#1F1F1F` = 第3のテキスト色) |
| `color.text.muted` | gray.600 | `#9e9e9e` (実装 #999 系) | bound |
| `color.text.link` | — | null | 🚧 分類C (実体は既定青 `#0000EE` 未スタイル = 負債 A-01/D-3) |
| `color.surface.default/subtle/muted` | white / gray.50 / gray.100 | `#fff` / `#f9f9f9` / `#f5f5f5` | bound (実装 #f1f1f1/#ededed は正規化候補🟢) |
| `color.border.*` | gray.300/400/500 | `#e0e0e0` / `#ccc` / `#bcbcbc` | bound |
| `color.state.success` | green.500 | `#58b85d` | 🚧 follow-up #5 (IB 暫定参照) |
| `color.state.error` | red.500 | `#d10000` | 🚧 follow-up #2 (暫定バインド) |
| `color.accent.campaign` | orange.500 | `#EF4123` | bound (キャンペーン専用) |
| `color.focus.ring` | brand.primary | (Q1 連動) | 🚧 |

## 3. タイポグラフィ

| 用途 | 値 | 状態 |
| --- | --- | --- |
| 本文 | Noto Sans JP 系 (収束候補) / 実測 15px / lh 1.4 | family bound / size 🚧 Q4 (15px はスケール外 ❓) |
| 見出し | Murecho + Noto (収束候補) / h1 40px / h2 18px | family bound / size 🚧 Q4 |
| 欧文 | Roboto | bound |
| 数字 (価格) | Barlow/Roboto (宿泊由来の暫定継承) | 🚧 要実査 (K-03 国内 = 未取得) |

- [事実] 現状実装は h1 Kozuka Gothic Pro・h2/h3 游ゴシック系の混在 (layerB §3-2 = D-3)。和文書体の収束は DS 内正規化候補 🟢 (採否は Q4 と併せ判断)

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: 刻み体系は確定、px 値は 🚧 Q3 (現状実装は 5px 刻みユーティリティ。8px 寄せの判断は移行コスト試算 = follow-up #8 待ち)
- コンテナ幅: 🚧 未抽出 (follow-up #6)。宿泊値 (975/1195/1425) を暫定参照
- ブレークポイント: 🚧 Q5。japan ゾーン実装は 2段 (959/960) のみ。Q5 暫定運用案 (600/768/992/1200) を本 DS の暫定値として独自定義

## 5. 角丸・シャドウ

- 角丸: ボタンは `radius.sm` (4px = 本番実測)。**pill 非採用が国内の固有形状** (R-01 🟡 = IB/宿泊との差は許容差でなく本 DS の意匠)。カードは 🚧 実 px 未取得
- シャドウ: 実値未抽出 🚧 (follow-up #13)

## 6. アイコン・画像

- アイコン体系: slick 等 (I-01) ❓ Q8 未決。暫定 =「新規制作分のみ統一・既存維持」
- 画像なし表現: noimage (I-02 = D-1/D-6) ❓ fallback 設計は Card 着手時
- 画像比率: 🚧 未抽出 (follow-up #6。宿泊の object-fit 制御を暫定参照)

## 7. コアコンポーネント

正: `components.md`。定義済: Button / Input / SearchForm / Card (ResultCard) / PriceTag / Header / Footer / Breadcrumb (保留 ❓) / Modal。

- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- ボタン階層体系は現状なし (BT-02)。第一版は `primary` のみ定義し、拡張は ADR (原則6: 投機的 API を作らない)
- 未着手: Select / Tabs / Toast / Table / Accordion (follow-up #1)

## 8. ブランド・クリエイティブガイド

- [観察] 実用・価格訴求トーン (CP-01)。「卸価格」の直接的な価格優位訴求
- [事実] 写真選定基準は要確認 (BR-01/D-9) ❓
- [事実] キャンペーン accent `#EF4123` は主色と分離管理 (付随論点のたたき台に従う)
- [事実] 広告/SNS/メールは資産提供待ち (AD-02/follow-up #11) — 本版スコープ外

## 9. Agent Prompt Guide

1. `semantic.rental-car.json` を読み、Semantic トークン名で指定 (HEX 直書き・primitive 直接参照は禁止)
2. `components.md` の固定フォーマットに従う
3. `$status=placeholder` は `$note` の Q/follow-up 番号を確認し「🚧 暫定」を生成物に伝播させる。特に主色 (Q1)・リンク色 (null) は確定値が存在しないことを明示する
4. ボタンの角丸は 4px (`radius.action`)。pill を使わない
5. 禁止: 他サービスのトークン値の流用 (P1。特にインバウンドの blue #064f9e・宿泊の紺 #283593)・100選ゾーンの素材利用・会員ランク色
6. 迷ったら: `01_共通アセット/命名規則.md` §9 → `デザイン原則.md`

## 未確定事項の一覧 (オーナー確認待ち = 分類C)

| 論点 | 内容 | 暫定運用 |
| --- | --- | --- |
| Q1 | 主色赤の正値 (3候補) | `#9E2334` 暫定。ゾーン実装値 `#9B2030` は現状維持 |
| Q2 | テキスト主色 (実測 #1F1F1F の扱い含む) | 2段を暫定共通 |
| Q3 | base unit (実装は 5px 系) | 刻み体系先行・4px 系で仮バインド |
| Q4 | root 基準・本文 15px の正規化 | スケール先行・root 未確定 |
| Q5 | breakpoint (実装は 2段) | foundation 4段を暫定基準 |
| Q8 / Q9 | アイコン体系 / モーダル基盤 | 新規のみ統一 / drawer 方向 |
| — | link 正値・ボタン状態・フォーム実体・コンテナ幅・価格書体 | 分類C / follow-up #4/#2/#6 |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Ph-E: Foundation/Semantic/Component/固有要素/Agent Prompt Guide を統合) | Claude Design (Builder) |
