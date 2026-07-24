# 国内宿泊予約 Design System (travel) — design.md

- 種別: DS 成果物 (design.md = 統合文書)
- 状態: Draft (0.3.0-draft)
- 作成日: 2026-07-09
- Source of Truth: https://github.com/tocoo/coocom-design-system/tree/main/services/travel/design-system (R3-10)
- 対象: 顧客向け UI のみ (管理画面は対象外)
- 実装の所在: GitHub `tocoo/tocoo_travel`
- 独立性: 本 DS は国内レンタカー・インバウンドレンタカーと Foundation/Semantic/Component/design.md を共有しない (要求仕様 R1)。命名・運用規約のみ3サービス共通 (`governance/` 参照 = R2)

---

## 1. 概要・ブランド位置づけ

- [事実] サービス: ToCoo! 宿泊予約 (tocoo.jp)。国内宿泊予約の顧客向けサイト
- [決定] 主色=メイン: ロイヤルブルー `#2C50C8` (brand.primary)。サブ: ヴィヴィッドインディゴ `#4845D4` (brand.secondary)。オーナー決定 2026-07-10 (TVL-0010)。旧 主色 紺 `#283593` (navy) から変更
- [事実] 固有要素: 星評価 (ReviewStars)・価格強調タイポ (PriceTag)。レンタカー2サービスには無い
- [観察] コピートーンは実用・価格訴求。CTA 文言例「プラン選択へ」→ 詳細は `brand-content.md`
- [事実] 負債の非持込: Bootstrap 残骸 `--primary:#007bff`・変数二重定義・管理画面系の色 (teal `#1798A5` 等) は本 DS に持ち込まない
- [事実] 非構築: 会員ランク色 (破棄済)

## 2. カラー

正: `semantic.travel.json` (用途) → `primitive.travel.json` (値)。以下は要約。配色は **共有ファウンデーション＋ブランド2スキーム** の二層 (TVL-0010)。全スキーム共通 (共有) は器/ニュートラル (白基調 warm-gray)・テキスト・境界のみ (surface/text/border)。状態色 (success/error)・特集アクセント・評価色 (星)・リンクは **per-scheme** = 各スキームが自スキームの値を保持 (TVL-0011。正式採用時に共通化): `color.scheme.main` = メイン(royal) / `color.scheme.sub` = サブ(indigo)。各スキームは tint(50)/soft(300)/base(500)/hover(600)/pressed(700)/ink(900)/**inverse(逆色)**/error/accent。

| 用途 (Semantic) | 参照 | 値 | 状態 |
| --- | --- | --- | --- |
| `color.scheme.main.*` (メイン=royal) | royal.50/300/500/600/700/900 + amber.500 + red.400 + orange.400 | tint #E8EDFB / soft #8E9EE6 / base #2C50C8 / hover #2340A6 / pressed #1B3488 / ink #14224A / **inverse #C8912C (アンバー・逆色)** / error #D23A3A / accent #E4572E | bound (TVL-0010/0011) |
| `color.scheme.sub.*` (サブ=indigo) | indigo.50/300/500/600/700/900 + gold.500 + rose.500 + coral.500 | tint #EDECFB / soft #928EE4 / base #4845D4 / hover #3936B0 / pressed #2C2A8C / ink #191840 / **inverse #C8B12C (ゴールド・逆色)** / error #D2405F / accent #E0553C | bound (TVL-0010/0011) |
| `color.brand.primary` (メイン) | scheme.main.base | `#2C50C8` | bound (白背景 ≈6.8:1) |
| `color.brand.primaryHover` | scheme.main.hover | `#2340A6` | bound |
| `color.brand.secondary` (サブ) | scheme.sub.base | `#4845D4` | bound (白背景 ≈6.8:1) |
| `color.brand.secondaryHover` | scheme.sub.hover | `#3936B0` | bound |
| `color.text.strong` / `body` | gray.900 / 800 | `#212121` / `#424242` | **bound (TVL-0003)** |
| `color.text.muted` | gray.600 | `#9e9e9e` | bound |
| `color.text.link` | scheme.main.base (副色=sub.base) | `#2C50C8` / `#4845D4` | bound (TVL-0011・リンク=主色。TVL-0005 解決) |
| `color.surface.default/subtle/muted` | white / gray.50 / 100 | `#fff` / `#f9f9f9` / `#f5f5f5` | bound |
| `color.border.subtle/default/strong` | gray.300/400/500 | `#e0e0e0` / `#ccc` / `#bcbcbc` | bound |
| `color.state.success` | scheme.main.base (副色=sub.base) | `#2C50C8` / `#4845D4` | bound (TVL-0011・成功=各パレット主色。専用緑廃止) |
| `color.state.error` | scheme.main.error (副色=sub.error) | `#D23A3A` / `#D2405F` | bound (TVL-0011・per-scheme・正式採用時共通化) |
| `color.accent.campaign` | scheme.main.accent (副色=sub.accent) | `#E4572E` / `#E0553C` | bound (TVL-0011・per-scheme・正式採用時共通化) |
| `color.focus.ring` | brand.primary | `#2C50C8` | bound (白背景 ≈6.8:1) |
| `color.icon.rating` | scheme.main.inverse (副色=sub.inverse) | `#C8912C` / `#C8B12C` | bound (TVL-0011・評価色=各パレット逆色) |

- [事実] 品質基準: WCAG 2.2 AA を最低ラインとし DS には違反値を入れない (要求仕様 R9)。本文 #424242 ≈9.7:1・主色 royal #2C50C8 ≈6.8:1・副色 indigo #4845D4 ≈6.8:1 いずれも AA 適合 (AAA 7:1 は未達)

## 3. タイポグラフィ

root 16px・**rem 基準** (TVL-0001)。2 書体構成 = 明朝 (表現) + ゴシック (機能)。タイポグラフィ設計方針 (共有 dc) 2026-07-10 の決定を反映。

| 用途 | 値 | 状態 |
| --- | --- | --- |
| 本文・UI | LINE Seed JP / 1rem / lh 1.8 | **bound (Q1)** |
| 見出し (一覧・カード) | LINE Seed JP 700 / h2 2rem | **bound (Q2)** |
| Display・Hero・詳細施設名 | Noto Serif JP (明朝) 500–600 | **bound (Q8)** |
| 欧文 | LINE Seed JP に統合 (旧 Roboto 廃止) | bound |
| 数字 (価格) | LINE Seed JP 700・tabular-nums (旧 Barlow 900 廃止) | **bound (Q3)** |

- サイズスケール: xs 0.75 / sm 0.875 / md 1 / lg 1.125 / xl 1.25 / 2xl 1.5 / 3xl 2 / 4xl 2.5 / display-lg 3rem (48px・Q4)
- 行間: tight 1.3 / normal 1.5 / relaxed 1.8 (本文)
- [注意] 実装移行時に px→rem の書き換えが発生する (TVL-0001 Consequences)
- [観察] 特集頁の見出しフォント不一致・壊れた font stack は新規制作で再生産しない

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: **4px (0.25rem) 系で確定** (TVL-0002)。spacing.0〜16 全段 bound
- コンテナ幅: `975 / 1195 / 1425px` (宿泊実装値・bound)
- ブレークポイント: **`640 / 768 / 1024 / 1280px`** (TVL-0004。現代標準へ更新 — 旧実装値 600/992/1200 からの変更。移行方針は TVL-0004 参照)。**本値は 3DS 共通 breakpoint として再認定** (owner-decisions.md Q5 決定・2026-07-24・Task 009-18-BP1)。ADR 正本・provenance は未確認 (009-19 provenance トラックへ残す)
- 代表 viewport (画面設計・Claude Design・HTML 確認用の表示幅): **`390 / 768 / 1280 / 1440px`** (3DS 横断・Web部責任者判断 2026-07-24・Task 009-18-BP1)。**これは表示確認用の代表幅であり responsive breakpoint token ではない** (breakpoint は上記・`breakpoint.*` token が正)

## 5. 角丸・シャドウ

- 角丸: `radius.sm 4 / md 8 / lg 16 / full 9999px` (bound)。ボタンは pill (`radius.action` = full) = 宿泊のサービスシグネチャ。カードは 🚧 実px未取得 (暫定 md)
- シャドウ: 実値未抽出 🚧 (follow-up #13。暫定3段で据置き = TVL-0008)

## 6. アイコン・画像

- アイコン体系: **Font Awesome 6 で確定** (TVL-0006)。新規制作は FA6 に統一、既存 Material 混在箇所は改修時に置換。サイズスケールは `iconSize.sm〜xl` (bound)
- 画像比率: object-fit 制御あり
- 画像なし・在庫ゼロ時の表現: 未定義 ❓ 検討トリガー: Card 実装着手時

## 7. コアコンポーネント

正: `components.md`。定義済: Button / Input / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal。

- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- 状態リストは固定 (hover/active/focus/disabled/loading/error/success)。宿泊のボタン状態は未取得 🚧
- Button variant 語彙は GOV-0002 (cross-service 5語)。**travel の Button 実装は4語 (primary/secondary/ghost/text)**。campaign(accent 塗りボタン)は廃止し accent はバッジ/割引ラベルの点専用 (TVL-0012)
- モーダルは **drawer に全面統一** (TVL-0007)。centered dialog は deprecated・段階移行
- 未着手: Select / Tabs / Toast / Table / Accordion (実体皆無)

## 8. ブランド・クリエイティブガイド

正: `brand-content.md` (ライティング・価格表記)。

- [観察] 価格中心・実用トーン。数字を大きく強調する価格タイポがブランド表現の中核
- [事実] 特集は `#EF4123` を面で多用。通常導線と特集を色で分離する現状構造を維持
- [事実] 写真選定基準は未明文化 ❓ 検討トリガー: ブランドルール整理時
- [事実] ロゴファイルは未提供。プレーンな "ToCoo!" ワードマーク (見出しフォント + brand primary) で代用中。実ロゴ提供時に差し替え

## 9. Agent Prompt Guide

AI に本 DS で UI を生成させる際の読み順と規則:

1. `semantic.travel.json` を読み、色・フォントは Semantic トークン名で指定する (HEX 直書き・primitive 直接参照は禁止)
2. `components.md` の該当 Component の固定フォーマット (用途/バリアント/状態/Do・Don't) に従う
3. `$status=placeholder` のトークンは `$note` を確認し、生成物にも「🚧 暫定」を伝播させる
4. 宿泊固有要素: 評価は ReviewStars、価格は PriceTag (数字900+円+補助) を必ず使う
5. 禁止: `--primary:#007bff`・会員ランク色・**他サービスのトークン値の流用 (R1-6)**
6. 迷ったら: `governance/naming-rules.md` → 本書 §1〜8

## 未確定事項の一覧

| 論点 | 内容 | 状態 |
| --- | --- | --- |
| TVL-0005 | リンク色 (赤 #d10000 / 紺 #283593) | ✅ 解決 (TVL-0011・リンク=各スキーム主色) |
| follow-up #4 | ボタンの hover 以外の状態 (active/focus/disabled/loading) 一式 | 🚧 実査待ち (TVL-0008)。※ brand primaryHover は TVL-0010 で解決 (royal.600) |
| follow-up #13 | shadow 実値 | 🚧 実査待ち |
| follow-up #3 | motion 実値 | 🚧 実査待ち |
| follow-up #5 | success 色 | ✅ 解決 (TVL-0011・成功=各パレット主色) |
| follow-up #2 | フォーム入力/エラー/必須・検証 | 🚧 実査待ち |
| — | カード実px・8スロット対応付け・画像欠落 fallback | 🚧 実査待ち / ❓ Card 着手時 |
| Q6 | 実装クラス命名方法論 (FLOCSS 等) | ❓ 検討トリガー: Component 実装着手時 |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-09 | 0.3.0-draft: 独立DS再構築 (要求仕様 R1〜R10)。TVL-0001〜0008 反映 (rem化・4px系・テキスト2段・BP現代標準・FA6・drawer統一・リンク色保留・実査待ちplaceholder維持) | Claude Design (Builder) |
| 2026-07-24 | Task 009-18-BP1: §4 に記述追加。ブレークポイント `640/768/1024/1280px` (TVL-0004) を 3DS 共通 breakpoint として再認定した旨を注記 (owner-decisions.md Q5 決定・2026-07-24。Travel token 値は不変)。代表 viewport (画面設計・HTML 確認用) `390/768/1280/1440px` を breakpoint とは別概念として §4 に追加 (3DS 横断・正本=各 design.md)。ADR 正本・provenance 未確認は 009-19 へ残す旨を明記。token・値・status・version は不変 | Claude Code |
