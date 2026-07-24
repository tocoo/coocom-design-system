# インバウンドレンタカー Design System (inbound)

- 種別: DS 成果物 (design.md = 統合文書)
- 状態: Draft
- 作成日: 2026-07-02
- 対象: 顧客向け UI のみ (P3/ADR-0012)
- 実装の所在: GitHub `tocoo/tocoo_rental_car` の `inbound` ゾーン (P6/ADR-0004)。国内レンタカーと同一リポだが DS は独立 (P1)
- 独立性: 本 DS は国内レンタカー・国内宿泊と Foundation/Semantic/design.md を共有しない (P1/ADR-0022)。命名・運用規約のみ共通 (P2)

---

## 1. 概要・ブランド位置づけ

- [事実] サービス: ToCoo! インバウンドレンタカー (www2.tocoo.jp/en/ ほか)。訪日客向け・4言語 (en/cn/kr/th)
- [事実] 主色: 赤 `#9E2334` ($color-main。layerB §3 本番確証)。国内レンタカーの `#9B2030` とは本番でも別値。Q1 (国内の正値選定) を本 DS へ自動適用しない
- [事実] i18n が構造の中核 (IB-i1〜i5): 言語切替 UI・多言語 fallback・通貨/法表記スロット・文言長可変・locale 格納
- [観察] コピートーンは英語・短文・情緒/旅情訴求 ("Japan is all yours.") — 国内と共通化すべきでない (CP-01 = 実装事実として国内と別トーン)
- [事実] Semantic トークンは素材に不在だったため、本 DS で新規生成した (実装着手ガイド§2 の生成手引きに準拠。要調査項目は値を作らず placeholder)

## 2. カラー

正: `semantic.inbound.json` → `primitive.inbound.json`。以下は要約。

| 用途 (Semantic) | 参照 | 値 | 状態 |
| --- | --- | --- | --- |
| `color.brand.primary` | `{color.palette.red.700}` | `#9E2334` | bound (最終確定は分類C) |
| `color.brand.primaryHover` | — | null | 🚧 hover は opacity のみ確認 (follow-up #4) |
| `color.text.strong` / `body` | gray.900 | `#212121` | 🚧 Q2 (実装 #333 は旧値=正規化候補🟢) |
| `color.text.muted` | gray.700 | `#616161` | bound (実装 #999 は正規化候補🟢) |
| `color.text.link` | blue.500 | `#064f9e` | bound (ゾーン実装値。赤系へ寄せる議論は分類C) |
| `color.surface.default/subtle/muted` | white / gray.50 / gray.200 | `#fff` / `#f9f9f9` / `#eee` | bound |
| `color.border.*` | gray.300/400/500 | `#e0e0e0` / `#ccc` / `#bcbcbc` | bound (#c6c6c6 は正規化候補🟢) |
| `color.state.success` | green.500 | `#58b85d` | bound (本 DS 自身の実装値) |
| `color.state.error` | red.500 | `#ff0000` | 🚧 要精査 (生成手引き) |
| `color.form.errorBg` / `focusBg` | pink.100/200 | `#ffd6de` / `#f3c8d0` | 🚧 follow-up #2 |
| `color.focus.ring` | brand.primary | `#9E2334` | 🚧 A-02 未監査 |

- [事実] campaign accent は素材に色値なし (AD-01 IB 列は構造のみ) — 定義せず。要実査 ❓

## 3. タイポグラフィ (多言語 fallback 体系 = D-10 解消設計)

### 許可リスト (これ以外を新規採用しない)

| 役割 | フォント | 状態 |
| --- | --- | --- |
| 和文 base | Noto Sans JP 系 | bound (現状本文 Arial は踏襲しない = D-3) |
| 見出し | Murecho + Noto Sans JP | bound |
| 欧文基準 | Roboto | bound |
| 欧文装飾 | Outfit | 🚧 付随論点 (たたき台: Roboto 基準・Outfit は装飾用途で保留) |
| 数字 (価格) | Roboto 700 (JPY~ 実測) | bound |
| th fallback | Prompt (base 末尾に追加) | bound |
| cn / kr fallback | 未定 | 🚧 follow-up #10 (実画面確認後に追加判断) |

- [事実] 許可リスト外の単発フォント (Quicksand・Salesforce Sans 等) と FA5/6 混在 (T-07) は整理対象。新規採用しない
- 適用規則: base スタックは全 locale 共通、locale 固有フォントは `font.locale.{lang}` として**末尾に追加**する (層を増やさず fallback で吸収 = 判断基準§3)。言語追加時は許可リストへの追加を ADR で判断 (D-10 の再発防止)

### スケール

- 本文 14px / lh 1.5 (実測)。h2 36px / h3 16px (実測)。すべて 🚧 Q4 (root 現状 62.5%=10px 基準の再定義未決)

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: 刻み体系は確定、px 値は 🚧 Q3 (現状実装は 5px 刻み15段のユーティリティ生成)
- コンテナ幅: 🚧 未抽出 (follow-up #6。宿泊値を暫定参照)
- ブレークポイント: **`640 / 768 / 1024 / 1280`** (Q5 決定 2026-07-24: 3DS 共通値 = Travel `TVL-0004` を再認定。旧暫定 600/768/992/1200 から変更・`$status` placeholder 維持)。実装は6段 (320/520/692/800/960/961) で、実装との移行整理は使用件数集計 (follow-up #8) 待ち。ADR 正本・provenance は未確認 (009-19)
- 代表 viewport (画面設計・HTML 確認用の表示幅): **`390 / 768 / 1280 / 1440px`** (3DS 横断・Web部責任者判断 2026-07-24・Task 009-18-BP1)。**表示確認用の代表幅であり breakpoint token ではない**

## 5. 角丸・シャドウ

- 角丸: CTA は pill (`radius.action` = 実測 999px)。小型ボタンは実装 3px → `radius.actionCompact` (4px) へ正規化候補 🟢。使い分け基準は未明文化 ❓
- シャドウ: アドホック実装・実値未抽出 🚧 (follow-up #13)

## 6. アイコン・画像

- アイコン体系: FA5 + FA6 混在 (I-01/T-07) ❓ Q8。暫定 =「新規制作分のみ統一・既存維持」
- 画像なし表現: noimage.jpg 多発 (D-1/D-6 重大負債)。media スロットの fallback 設計を Card 着手時に行う ❓
- 写真選定: 地域景観 (俯瞰/自然/街並み)。基準未明文化 (BR-01/D-9)

## 7. コアコンポーネント

正: `components.md`。定義済: Button / Input / SearchForm / Card (Result/Plan) / PriceTag / LanguageSwitcher / Header / Footer / Breadcrumb / Modal。

- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- 全 Component 共通の i18n 制約: 文言長可変 (IB-i4)・locale 供給 (IB-i5)・fallback フォント適用 (IB-i2)
- inbound 固有: LanguageSwitcher (N-03)・PriceTag の通貨/法表記スロット (IB-i3)
- 未着手: Select / Tabs / Toast / Table / Accordion (follow-up #1)

## 8. ブランド・クリエイティブガイド

- [観察] 英語・短文・情緒/旅情訴求のトーン ("Japan is all yours." "Dive into the blue.")
- [観察] CTA は動詞先頭 ("Book Now" / "View details" = 🟢 原則候補)
- [事実] 価格表記は `{金額} JPY~ (tax included)` で統一済 (CP-03 表記揺れなし)
- [事実] 写真選定基準は未明文化 (D-9) ❓ 検討トリガー: ブランドルール整理時
- [事実] 広告/SNS/メールは資産提供待ち (follow-up #11) — 本版スコープ外

## 9. Agent Prompt Guide

1. `semantic.inbound.json` を読み、Semantic トークン名で指定 (HEX 直書き・primitive 直接参照は禁止)
2. `components.md` の固定フォーマットと「共通事項 (i18n 構造制約)」に従う。**テキストは必ず4言語で成立する前提で組む**
3. `$status=placeholder` は `$note` の Q/follow-up 番号を確認し「🚧 暫定」を伝播させる
4. 価格は PriceTag (amount/currency/legal の3スロット) を必ず使う。固定文字列にしない
5. フォントは許可リスト + `font.locale.*` fallback のみ。新フォントの継ぎ足し禁止 (D-10)
6. 禁止: 国内レンタカーの赤 `#9B2030`・宿泊の紺 `#283593` の流用 (P1)・会員ランク色・Q1 の結論の自動適用
7. 迷ったら: `01_共通アセット/命名規則.md` §9 → `デザイン原則.md`

## 未確定事項の一覧 (オーナー確認待ち = 分類C)

| 論点 | 内容 | 暫定運用 |
| --- | --- | --- |
| — | brand primary の公式値確認 (`#9E2334`) | ゾーン実装値で bound (Q1 とは独立に扱う) |
| — | link 色 blue `#064f9e` を赤系へ寄せるか | 現状値で bind |
| Q2 / Q3 / Q4 / Q5 | text 主色 / base unit (5px系) / root 基準 / BP (6段) | 各暫定運用案 |
| Q8 / Q9 | アイコン体系 (FA5/6) / モーダル基盤 (remodal) | 新規のみ統一 / drawer 方向 |
| 付随論点 | Outfit の採否 | Roboto 基準・装飾用途で保留 |
| — | エラー赤 #f00 精査・フォーム実体・cn/kr fallback・campaign 色 | follow-up #2/#10・要実査 |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Ph-E: Foundation/Semantic 新規生成/Component/i18n 固有構造/Agent Prompt Guide を統合) | Claude Design (Builder) |
| 2026-07-24 | Task 009-18-BP1: breakpoint 記述を是正。旧「foundation 4段 (600/768/992/1200)」の参照を、Q5 決定 (2026-07-24, Web部責任者) の 3DS 共通値 640/768/1024/1280 (Travel TVL-0004 再認定) へ更新。primitive.inbound.json の breakpoint 値も同値へ変更 ($status placeholder 維持)。代表 viewport 390/768/1280/1440px を §4 に追加 (breakpoint とは別概念)。実装値 (320/520/692/800/960/961)・follow-up #8・provenance 未確認は保持 | Claude Code |
