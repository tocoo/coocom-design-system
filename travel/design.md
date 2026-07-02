# 国内宿泊予約 Design System (travel)

- 種別: DS 成果物 (design.md = 統合文書)
- 状態: Draft
- 作成日: 2026-07-02
- 対象: 顧客向け UI のみ (P3/ADR-0012。管理画面は対象外)
- 実装の所在: GitHub `tocoo/tocoo_travel` (P6/ADR-0004)
- 独立性: 本 DS は国内レンタカー・インバウンドレンタカーと Foundation/Semantic/design.md を共有しない (P1/ADR-0022)。命名・運用規約のみ3サービス共通 (P2)

---

## 1. 概要・ブランド位置づけ

- [事実] サービス: ToCoo! 宿泊予約 (tocoo.jp)。国内宿泊予約の顧客向けサイト
- [事実] 主色: 紺 `#283593`。本番実測で揺れなし=確定 (C-01/layerB §1)
- [事実] 固有要素: 星評価 (TR-i1)・価格強調タイポ (TR-i2)。レンタカー2サービスには無い
- [観察] コピートーンは実用・価格訴求 (CP-01)。CTA 文言例「プラン選択へ」(CP-02)
- [事実] 負債の非持込: Bootstrap 残骸 `--primary:#007bff` (C-11/D-5)・foundation/spa の変数二重定義 (D-2)・管理画面系の色 (teal `#1798A5` 等) は本 DS に持ち込まない
- [事実] 非構築: 会員ランク色 (C-10 破棄=2026-06-26 オーナー訂正)

## 2. カラー

正: `semantic.travel.json` (用途) → `primitive.travel.json` (値)。以下は要約。

| 用途 (Semantic) | 参照 | 値 | 状態 |
| --- | --- | --- | --- |
| `color.brand.primary` | `{color.palette.navy.500}` | `#283593` | bound |
| `color.brand.primaryHover` | `{color.palette.navy.700}` | null | 🚧 hover 暗色未抽出 |
| `color.text.strong` / `body` | gray.900 / gray.800 | `#212121` / `#424242` | 🚧 Q2 (2段を暫定共通) |
| `color.text.muted` | gray.600 | `#9e9e9e` | bound |
| `color.text.link` | red.500 | `#d10000` | 🚧 placeholder (R-2。コード値 #d10000 と実測 #283593 の揺れ。owner-decisions #5) |
| `color.surface.default/subtle/muted` | white / gray.50 / gray.100 | `#fff` / `#f9f9f9` / `#f5f5f5` | bound |
| `color.border.subtle/default/strong` | gray.300/400/500 | `#e0e0e0` / `#ccc` / `#bcbcbc` | bound |
| `color.state.success` | green.500 | `#58b85d` | 🚧 follow-up #5 (IB 暫定参照) |
| `color.state.error` | red.500 | `#d10000` | bound |
| `color.accent.campaign` | orange.500 | `#EF4123` | bound (特集専用・主色と分離) |
| `color.focus.ring` | brand.primary | `#283593` | bound (A-02 未監査) |

- [推奨] リンク色は用途トークンで管理する。layerB では TOP リンクに主色紺の使用も観測されており、`text.link` (赤) との使い分けは DS 内正規化候補 🟢 ❓ (検討トリガー: リンク UI 着手時)

## 3. タイポグラフィ

| 用途 | 値 | 状態 |
| --- | --- | --- |
| 本文 | Noto Sans JP 系 / 16px / lh 1.8 (layerB 実測) | family bound / size・lh 🚧 Q4 |
| 見出し | Murecho + Noto Sans JP / h2 32px | family bound / size 🚧 Q4 |
| 欧文 | Roboto | bound |
| 数字 (価格) | Barlow/Roboto・weight 900 (実測 Roboto 900) | bound |
| 明朝 (限定用途) | Ryumin / 游明朝 | bound (travel 固有) |

- [観察] 特集頁で h2 が Noto 14px の頁あり=見出しフォント不一致 (D-3)。DS 内正規化候補 🟢
- [観察] 壊れた font stack (h3 に sans-serif 混入 = T-07/D-3) は新規制作で再生産しない

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: 刻み体系 (spacing.0〜16) は確定、px 値は 🚧 Q3 (現状は 16px map `$PADDING`。8px 寄せ/5px/4px ハイブリッドは未決)
- コンテナ幅: `975 / 1195 / 1425px` (S-03 bound)
- ブレークポイント: `600 / 768 / 992 / 1200px` (B-01。宿泊 foundation 自身の実装値=bound。3サービス統一の批准は Q5)

## 5. 角丸・シャドウ

- 角丸: `radius.sm 4 / md 8 / lg 16 / full 9999px` (bound)。ボタンは pill (`radius.action` = full。layerB 実測)。カードは 🚧 実 px 未取得 (暫定 md)
- シャドウ: 定義はあるが実値未抽出 🚧 (follow-up #13。暫定3段で据置き)

## 6. アイコン・画像

- アイコン体系: Material + FA 混在 (I-01) ❓ Q8 未決。暫定運用 =「新規制作分のみ統一・既存維持」(段階導入 P4)。サイズスケールは `iconSize.sm〜xl` (bound)
- 画像比率: object-fit 制御あり (I-03 🟢)
- 画像なし・在庫ゼロ時の表現: 未定義 (D-6) ❓ 検討トリガー: Card 実装着手時

## 7. コアコンポーネント

正: `components.md`。定義済: Button / Input / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal。

- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- 状態リストは固定 (hover/active/focus/disabled/loading/error/success)。宿泊のボタン状態は未取得 🚧 (follow-up #4)
- 未着手: Select / Tabs / Toast / Table / Accordion (follow-up #1・実体皆無)

## 8. ブランド・クリエイティブガイド

- [観察] 価格中心・実用トーン (CP-01)。数字を大きく強調する価格タイポ (TR-i2) がブランド表現の中核
- [事実] 特集 (ultra-tocoo) は `#EF4123` を面で多用 (layerB §2: 最頻出18回)。通常導線と特集を色で分離する現状構造を維持
- [事実] 写真選定基準は未明文化 (BR-01/D-9) ❓ 検討トリガー: ブランドルール整理時 (オーナー/マーケ判断)
- [事実] 広告/SNS/メールの外部クリエイティブは資産提供待ち (AD-02/follow-up #11) — 本版のスコープ外

## 9. Agent Prompt Guide

AI に本 DS で UI を生成させる際の読み順と規則:

1. `semantic.travel.json` を読み、色・フォントは Semantic トークン名で指定する (HEX 直書き・primitive 直接参照は禁止)
2. `components.md` の該当 Component の固定フォーマット (用途/バリアント/状態/Do・Don't) に従う
3. 値が `$status=placeholder` のトークンは `$note` の Q/follow-up 番号を確認し、生成物にも「🚧 暫定」を伝播させる
4. 宿泊固有要素: 評価は ReviewStars、価格は PriceTag (数字900+円+補助) を必ず使う
5. 禁止: `--primary:#007bff` (D-5)・会員ランク色 (破棄済)・他サービス (レンタカー) のトークン値の流用 (P1)
6. 迷ったら: `01_共通アセット/命名規則.md` §9 のフローチャート → `デザイン原則.md` (原則1から優先)

## 未確定事項の一覧 (オーナー確認待ち = 分類C)

| 論点 | 内容 | 暫定運用 |
| --- | --- | --- |
| Q2 | テキスト主色 (1段/2段/各維持) | 2段 (#424242 + #212121) |
| Q3 | base unit (8/5/4px) | 刻み体系先行・4px 系で仮バインド |
| Q4 | root 基準・本文サイズ | 実測値 (16px/1.8) で仮バインド |
| Q5 | breakpoint 統一の批准 | 宿泊 foundation 値 (自身の実装値) |
| Q8 | アイコン体系 | 新規のみ統一・既存維持 |
| Q9 | モーダル基盤 | 新規は drawer 方向・既存併存 |
| — | navy hover 暗色 / shadow 実値 / ボタン状態 / フォーム実体 / success 色 | follow-up #4/#13/#2/#5 参照 |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Ph-E: Foundation/Semantic/Component/固有要素/Agent Prompt Guide を統合) | Claude Design (Builder) |
| 2026-07-02 | 是正 R-2: §2 カラー表の `color.text.link` を bound→🚧 placeholder に更新 (コード値と本番実測の揺れ。$value 不変) | Claude Design (Builder) |
