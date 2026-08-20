# 国内レンタカー Design System (rental-car)

- 種別: DS 成果物 (design.md = 統合文書)
- 状態: Draft (0.3.0-draft)
- 作成日: 2026-07-02 / 更新日: 2026-08-20
- 対象: 顧客向け UI のみ (P3/ADR-0012。管理画面は対象外)
- 実装の所在: GitHub `tocoo/tocoo_rental_car` の `japan` ゾーン (P6/ADR-0004)。インバウンドと同一リポだが DS は独立 (P1)
- 独立性: 本 DS は国内宿泊・インバウンドレンタカーと Foundation/Semantic/design.md の**ファイルと値**を共有しない (P1/ADR-0022)。0.3.0-draft では国内宿泊 (travel) 0.3.0-draft の**定義体系** (スキーム二層・per-scheme の役割色・2 書体・4px 系) を採用するが、値は本 DS のファイルに独立して持つ (オーナー判断 2026-08-18・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §25)
- 非構築: 100選 (must-visit ゾーン) は DS 対象外 (2026-07-01 オーナー確認)
- 実装の旧値との対応: [migration-map.md](migration-map.md) (12 項目)。ラベル・タグ定義は [labels-tags.rental-car.md](labels-tags.rental-car.md)

---

## 1. 概要・ブランド位置づけ

- [事実] サービス: ToCoo! 国内レンタカー (www2.tocoo.jp/jp/)
- [事実] 配色は**共有ファウンデーション** (白・グレー・テキスト・境界) + **ブランド 2 スキーム**の二層で構成する。既定は main
  - main (第 1 候補) = ロイヤル `#2C50C8` / sub (第 2 候補) = インディゴ `#4845D4`
  - [事実] 旧 Q1 (赤 3 候補 `#9E2334` / `#9B2030` / `#9F1E30`) は 2026-08-18 のオーナー判断により**解消**した。旧実装値は [migration-map.md](migration-map.md) に事実として記録し、DS の正値としない
  - [事実] スキームの正式採用 (main / sub のいずれか) は未決である。per-scheme の役割色はいずれかが採用された時点で共通化する
- [観察] コピートーンは実用・価格訴求 (CP-01)。CTA 文言例「卸価格を検索」(CP-02)
- [観察] 3サービス中で素材が最も揃うが、ボタンの disabled・ResultCard の実 px・料金列の実ラベルが未取得である

## 2. カラー

正: `semantic.rental-car.json` → `primitive.rental-car.json`。以下は要約であり、JSON と食い違った場合は JSON を正とする。

### 2.1 スキーム (per-scheme)

| 段 | main (ロイヤル) | sub (インディゴ) |
| --- | --- | --- |
| `tint` | `#E8EDFB` | `#EDECFB` |
| `soft` | `#8E9EE6` | `#928EE4` |
| `base` | `#2C50C8` | `#4845D4` |
| `hover` | `#2340A6` | `#3936B0` |
| `pressed` | `#1B3488` | `#2C2A8C` |
| `ink` | `#14224A` | `#191840` |
| `inverse` (逆色・評価色) | `#C8912C` | `#C8B12C` |
| `error` | `#D23A3A` | `#D2405F` |
| `accent` (特集) | `#E4572E` | `#E0553C` |

### 2.2 用途 (Semantic)

| 用途 | 参照 | 状態 |
| --- | --- | --- |
| `color.brand.primary` | `{color.scheme.main.base}` | bound |
| `color.action.primary.bg` | 主色 | bound |
| `color.text.strong` / `body` / `mutedStrong` / `muted` | gray.900 `#212121` / gray.800 `#424242` / gray.700 `#616161` / gray.600 `#9E9E9E` | bound |
| `color.text.inverse` | `#FFFFFF` | bound |
| `color.text.link` | 主色 (per-scheme) | bound (実装の `#0050a0` / hover `#06f` は廃止) |
| `color.surface.default` / `subtle` / `muted` / `inverse` | `#FFFFFF` / `#F9F9F9` / `#F5F5F5` / `#212121` | bound |
| `color.border.subtle` / `default` / `strong` | `#E0E0E0` / `#CCCCCC` / `#BCBCBC` | bound |
| `color.state.success` | 主色 (専用の緑 `#43a047` / `#58b85d` は廃止) | bound |
| `color.state.error` | `{color.scheme.main.error}` `#D23A3A` | bound (sub 採用時は参照先の差し替えが必要) |
| `color.accent.campaign` | `{color.scheme.main.accent}` `#E4572E` | bound (バッジ専用・塗りボタン禁止。sub 採用時は参照先の差し替えが必要) |
| `color.focus.ring` | 主色 | bound |
| `color.mask.secret` | `{color.scheme.main.tint}` `#E8EDFB` (SecretPrice のマスク面 = B-2 無料会員の面色。グレー板 `#7f7f7f` は廃止) | bound |
| `color.overlay.backdrop` | `{color.palette.blackAlpha.45}` `rgba(0,0,0,0.45)` | placeholder `🚧` (実査待ち) |

[事実] `color.state.success` / `color.text.link` / `color.state.error` / `color.accent.campaign` の 4 件は現在 `main` を参照して固定されており、スキームの切替に自動追随しない。sub を正式採用する場合は `semantic.rental-car.json` の当該 4 箇所を差し替える。

### 2.3 品質下限

WCAG 2.2 AA・タップ領域 44px・代替テキスト・色だけで伝えないを下限とする。例外は本書と [labels-tags.rental-car.md](labels-tags.rental-car.md) に明示したものに限る。

- [事実] テキスト色は `strong` `#212121` / `body` `#424242` / `mutedStrong` `#616161` / `muted` `#9E9E9E` の 4 段。判読性を要する補助情報 — 価格の補助テキスト (税込 / 日数 / 1 日あたり)・フォームの補足と任意表記・店舗のアクセスと営業時間・オプションの注記・未到達ステップのラベル — は `color.text.mutedStrong` (白背景 6.19:1) を使用する。`color.text.muted` (白背景 **2.68:1**) は通常テキストに求められる 4.5:1 に達しないため、判読性を要する情報には用いず、区切り記号等の装飾に限る
- [事実] A 割引率の逆色面 + 白文字は **main `#C8912C` 上 2.78:1 / sub `#C8B12C` 上 2.15:1** であり、両スキームとも通常テキスト 4.5:1 だけでなく大きなテキスト 3:1 も満たさない `🚧`。2 スキームは値が異なるため、コントラスト比を伴う記述をワイルドカード表記で 1 行に束ねない
- [事実] 上記の白文字を成立させる「非操作の点的ラベルに限る例外条項」は本 DS では**未明文化**である ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §25 の Does Not Authorize)。条項が確定するまで A の意匠は暫定として扱う
- 本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない

## 3. タイポグラフィ

明朝とゴシックの 2 書体で構成する。

| 用途 | 値 | 状態 |
| --- | --- | --- |
| 本文・UI (`font.body`) | LINE Seed JP (フォールバック Noto Sans JP) / 1rem (16px) / lh 1.8 | bound |
| 見出し (`font.heading`) | LINE Seed JP・`font.heading.weight` 700。h1 2.5rem / h2 2rem / h3 1.125rem | bound |
| display・hero・車種クラス名 (`font.display`) | 明朝 Noto Serif JP。`lgSize` 3rem (Hero) / `mdSize` 1.125rem (車種クラス名) | bound |
| 数字・価格 (`font.price`) | 本文と同族・700・tabular-nums。数字 1.25rem / 補助 0.75rem | bound |

- 文字サイズ: root 16px・rem 基準。xs .75 / sm .875 / md 1 / lg 1.125 / xl 1.25 / 2xl 1.5 / 3xl 2 / 4xl 2.5 / display-lg 3rem
- ウェイト: 400 / 500 / 700 / 900。行高: 1.3 / 1.5 / 1.8
- [事実] 見出しの semantic は h1 / h2 / h3 の 3 段のみ定義する。h4 以下は本版では未定義であり、必要になった時点で追加する (推測で段を作らない)
- [事実] 車種クラス名は明朝 `font.display.mdSize` (18px) を使用する。ゴシックの `font.heading.h3Size` (18px) はカード見出し用であり、同一要素へ 2 系統を割り当てない
- [事実] 旧 Q4 (本文 15px / lh 1.4・Kozuka Gothic Pro と游ゴシックの混在) は本判断により解消した。実装値は [migration-map.md](migration-map.md) を参照

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: **4px (0.25rem) 系** `spacing.1`〜`16`。旧 Q3 (5px 刻みユーティリティ) は解消し、実装値は [migration-map.md](migration-map.md) に記録した
- コンテナ幅: **975 / 1195 / 1425px** (`size.container.sm` / `md` / `lg`)
- ブレークポイント: **`640 / 768 / 1024 / 1280`** (Q5 決定 2026-07-24: 3DS 共通値。0.3.0-draft で `$status` を bound へ)。japan ゾーン実装は 2段 (959/960) のみで、置換の扱いは [migration-map.md](migration-map.md)
- 代表 viewport (画面設計・HTML 確認用の表示幅): **`390 / 768 / 1280 / 1440px`** (3DS 横断・Web部責任者判断 2026-07-24・Task 009-18-BP1)。**表示確認用の代表幅であり breakpoint token ではない**

## 5. 角丸・シャドウ・モーション

- 角丸: `sm` 4px / `md` 8px / `lg` 16px / `full` (pill)
  - ボタンは **pill** (`radius.action`)。旧 R-01 (4px 固有形状を国内の意匠とする) は**廃止**した。縦グラデ・emboss 影・text-shadow も廃止 ([migration-map.md](migration-map.md))
  - 入力は `radius.input` (4px)。ラベルは `radius.badge` (4px)。オーバーレイの上端 2 隅は `radius.overlay` (16px `🚧`)
  - カードは `radius.card` = 暫定 `md` `🚧` (ResultCard の実 px 未取得)
- シャドウ: primitive に 3 段 (`sm` / `md` / `lg`) を暫定値で置くのみで、**用途 semantic は未定義**である `🚧` (follow-up #13。実値未抽出)。実値が確定するまで Component 仕様で個別の段を指定しない
- モーション: 300ms ease を暫定とする `🚧` (follow-up #3。実装は 0.3s ease-in-out と 0.35s ease が混在)
- z 軸: dropdown 1000 / sticky 1100 / overlay 1200 / modal 1300 / toast 1400

## 6. アイコン・画像・オーバーレイ

- アイコン体系: **Font Awesome 6**。サイズ 16 / 20 / 24 / 32px (既定 20px)。旧 Q8 (slick 等・「新規制作分のみ統一」) は本判断により解消した。実装の FontAwesome 4 記法は [migration-map.md](migration-map.md)
- 画像なし表現: No Image fallback (`surface.muted` 面 + `text.mutedStrong` の文字・比率 4:3)。ロゴ素材 (ToCoo!・レンタカー各社) は未提供 `🚧` であり、ワードマークで代用する。**記憶からの再構築は行わない**
- 画像比率・トリミング基準: 車両写真の選定基準は未定義 `🚧` (Assets レイヤー着手時)
- オーバーレイ: 既定形態は **drawer** (PC は右から 420px / SP は全幅・高さ 90vh まで)。backdrop は `color.overlay.backdrop` (`🚧` 暫定値 `rgba(0,0,0,0.45)`)。同時に開くオーバーレイは 1 つに限る
  - `🚧` **3 DS 横断の Modal 実装基盤は未決**である ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §1 Q9)。travel の drawer 全面統一は **travel 限定の現在判断**であり、本 DS で drawer を既定とする記述は本書の提案である
  - BottomSheet / Popover は**未承認の拡張候補**であり、既定仕様として扱わない ([components.md](components.md) §6)
  - remodal / LightBox など別のオーバーレイ基盤を新規に追加しない

## 7. コアコンポーネント

正: [components.md](components.md)。travel と同型 7 + 本 DS で先行定義 3 + レンタカー固有 8 の計 18 で構成する。

- travel と同型 (7 件・定義体系の採用。**意匠と値は本 DS のファイルで定義し、travel のファイルを参照・共有しない** = 上記「独立性」): Button / Input / PriceTag / Header / Breadcrumb / Footer / Modal
- 本 DS で先行定義 (3 件・travel 側は未着手): Select / FormLabel / Label・Tag
- レンタカー固有 (8 件): SearchForm / ResultCard / SecretPrice / Options / StorePicker / StepIndicator / Filter / Sort・Pagination
- ラベル・タグ (A〜H) の定義本体は [labels-tags.rental-car.md](labels-tags.rental-car.md)
- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- ボタンのバリアントは `primary` / `secondary` / `ghost` / `text` の 4 語で、4 語すべてに意匠と参照トークンを [components.md](components.md) §2 で与える。`campaign` は廃止 (accent は塗りボタン禁止)。主 CTA の個数制約は設けない (適用判断は未取得 `🚧`)
- 未着手: Tabs / Toast / Table / Accordion (follow-up #1)

## 8. ブランド・クリエイティブガイド

- [観察] 実用・価格訴求トーン (CP-01)。「卸価格」の直接的な価格優位訴求
- [事実] 特集アクセントは per-scheme (`#E4572E` / `#E0553C`) であり、主色と分離して管理する。**バッジ専用**で塗りボタンに使わない
- [事実] 写真選定基準は要確認 (BR-01/D-9) `🚧`
- [事実] 適用範囲は 2 段とする ([labels-tags.rental-car.md](labels-tags.rental-car.md) H)
  - 適用: UI 部品・カード・ラベル全般
  - 適用外: PR 帯・特集帯・キービジュアル・支給バナー
  - 適用外でも**カラーは厳守**する。品質下限 (AA・44px・代替テキスト・色だけで伝えない) は維持する
- [事実] 広告/SNS/メールは資産提供待ち (AD-02/follow-up #11) — 本版スコープ外

## 9. Agent Prompt Guide

1. `semantic.rental-car.json` を読み、Semantic トークン名で指定 (HEX 直書き・primitive 直接参照は禁止)
2. [components.md](components.md) の固定フォーマットに従う。ラベル・タグは [labels-tags.rental-car.md](labels-tags.rental-car.md) を参照する
3. `$status=placeholder` は `$note` の follow-up 番号を確認し「`🚧` 暫定」を生成物に伝播させる
4. **ボタンは pill (`radius.action`)**。4px の旧固有形状・グラデ・影を再現しない
5. 禁止: 他サービスのトークン値の流用 (P1。インバウンドの blue `#064f9e` 等)・100選ゾーンの素材利用・会員ランク色 (階級表現。会員種別 2 値は [labels-tags.rental-car.md](labels-tags.rental-car.md) B で別途定義)
6. 禁止 (廃止値): 赤 `#9E2334` / `#9B2030` / `#9F1E30`・紺 `#283593`・link `#0050a0` と hover `#06f`・CTA 緑 `#43A047`・`$tocooBlue` `#2B4B65`・マスクのグレー板 `#7F7F7F`・`.cat-label` の分類色 `#060` / `#C90` と尾 `#8C4801`・5px 刻みユーティリティ・本文 15px / lh 1.4・Bootstrap 残骸 `#007BFF`。これらは [migration-map.md](migration-map.md) の左列 (実装の事実値) にのみ現れる
7. 迷ったら: `01_共通アセット/命名規則.md` §9 → `デザイン原則.md`

## 未確定事項の一覧 (`🚧`)

旧 Q1 / Q2 / Q3 / Q4 / Q8 は 2026-08-18 のオーナー判断により解消した。本版で残る未確定は次のとおりである。

| 論点 | 内容 | 次アクション |
| --- | --- | --- |
| accent 淡色段・濃色段の実色 | B-1 プライムラベルの面 `#F9CDBC` と文字 `#8A2E11` はいずれも**仮色**である (本 DS の primitive に orange の淡色段・濃色段が存在しない) | 実査後に `accent.campaignTint` / `accent.campaignInk` を新設 |
| accent の帰属 | 有料会員 (B) と特集 (C) のどちらが accent を持つか未確定。C の面色は暫定 | オーナー判断 |
| A 割引率のコントラスト | 逆色面 + 白文字は main 2.78:1 / sub 2.15:1 で AA 未達 (sub は大きなテキスト 3:1 も未達)。非操作の点的ラベルに限る例外条項が前提だが本 DS では未明文化 | 例外条項の明文化 (オーナー判断) |
| E2 満車・受付終了 | CTA の非活性へ集約する方向のみ確定。面色・文字色・高さ・文言は未定 | Button の disabled 定義が先 |
| ResultCard の実 px | 角丸・影・行高・列幅が未取得。`radius.card` は暫定 `md` | 実装実査 |
| 料金列の実ラベル | 6 列構造の文言が CSS から取得できず、責務名ベースの暫定 | テンプレート実査 |
| モーション実値 | 実装は 0.3s ease-in-out と 0.35s ease が混在。DS は 300ms ease を暫定 | follow-up #3 |
| シャドウ実値 | primitive に 3 段を暫定値で置くのみで用途 semantic は未定義。Component 仕様では段を指定しない | follow-up #13 (実値抽出後に用途トークンを設計) |
| ロゴ素材 | ToCoo! ロゴ・レンタカー各社ロゴが未提供。ワードマークと No Image で代用 | 素材提供後に差し替え。記憶からの再構築は禁止 |
| 写真選定基準 | 車両写真の比率・トリミング基準が未定義 | Assets レイヤー着手時 |
| サービス識別子 | `rental-car` は暫定。正式識別子 (`drc` / `japan` 等) は未決 | governance 確認事項 #8 |
| Filter の件数算出 | facet 型の絞り込みは実装に未確認。件数の算出仕様が未定義 | 要件定義 |
| Modal 実装基盤 | 3 DS 横断の基盤は未決 (Q9)。drawer 既定は本書の提案 | オーナー判断 |
| 主 CTA の個数制約 | travel は §16 (Web部責任者判断 2026-08-03) で「1 画面 primary 1 つ」を撤回したが、同記録は適用範囲を travel に限定している。rental-car への適用は未取得 | オーナー判断 |
| BottomSheet / Popover の採否 | 未承認の拡張候補。既定仕様は Modal の drawer に寄せている | オーナー判断 |
| backdrop の実値 | `rgba(0,0,0,0.45)` はハンドオフバンドル記載値の暫定参照であり本 Repository で実査していない | 実装実査 (§14) |
| スキームの正式採用 | main / sub のいずれを正式採用するか未決 | オーナー判断 |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Ph-E: Foundation/Semantic/Component/固有要素/Agent Prompt Guide を統合) | Claude Design (Builder) |
| 2026-07-24 | Task 009-18-BP1: breakpoint 記述を是正。旧「宿泊 foundation 基準 (600/768/992/1200)」の参照を、Q5 決定 (2026-07-24, Web部責任者) の 3DS 共通値 640/768/1024/1280 (Travel TVL-0004 再認定) へ更新。primitive.rental-car.json の breakpoint 値も同値へ変更 ($status placeholder 維持)。代表 viewport 390/768/1280/1440px を §4 に追加 (breakpoint とは別概念) | Claude Code |
| 2026-08-20 | 0.3.0-draft: 国内宿泊 0.3.0-draft の Foundation 定義体系を採用 (オーナー判断 2026-08-18・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §25)。ラベル・タグ定義 (A〜H) と移行対照表を新設。旧実装値 (赤 3 候補・紺 #283593・link #0050a0・CTA 緑・5px 刻み) を廃止し [migration-map.md](migration-map.md) へ移した。§2 をスキーム二層 + 用途の 2 表へ、§5 を pill 既定へ、§6 に画像・オーバーレイを統合。未確定事項一覧を Q 番号ベースから `🚧` 論点ベースへ差し替え | Claude Code |
| 2026-08-20 | Task 009-57R の記述是正: PR [#156](https://github.com/tocoo/coocom-design-system/pull/156) コードレビュー ([issuecomment-5353729542](https://github.com/tocoo/coocom-design-system/pull/156#issuecomment-5353729542)) の指摘に対応。§2.2 に `mutedStrong` 行と `color.overlay.backdrop` 行を追加し、`{color.scheme.*.error}` / `{color.scheme.*.accent}` のワイルドカード表記を実バインド (`main` 固定) へ是正、`color.mask.secret` の参照先を `{color.scheme.main.tint}` へ変更。§2.3 にテキスト 4 段の使い分け・A 割引率の main / sub 両コントラスト (2.78:1 / 2.15:1)・例外条項が未明文化である事実を追記。§3 に h1 と `font.heading.weight`・`font.display.mdSize` を反映し h4 以下が未定義である事実を明記。§5 のシャドウを「用途 semantic 未定義」へ、§5・§6 の角丸と backdrop をトークン参照へ是正。§7 の「継承 8 + 固有 9」を「travel と同型 7 + 先行定義 3 + 固有 8」へ是正し、travel のファイルを参照しない旨を明示。未確定事項に主 CTA 個数制約・BottomSheet / Popover の採否・backdrop の実値の 3 行を追加し、accent 段・A コントラスト・シャドウの 3 行を是正。**不変**: スキームの値・ブレークポイント・スペーシング・z 軸・§8 ブランド・§9 Agent Prompt Guide | Claude Code |
