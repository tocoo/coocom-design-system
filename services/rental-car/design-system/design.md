# 国内レンタカー Design System (rental-car)

- 種別: DS 成果物 (design.md = 統合文書)
- 状態: Draft (0.3.0-draft)
- 作成日: 2026-07-02 / 更新日: 2026-09-07
- 対象: 顧客向け UI のみ (P3/ADR-0012。管理画面は対象外)
- 実装の所在: GitHub `tocoo/tocoo_rental_car` の `japan` ゾーン (P6/ADR-0004)。インバウンドと同一リポだが DS は独立 (P1)
- 独立性: 本 DS は国内宿泊・インバウンドレンタカーと Foundation/Semantic/design.md の**ファイルと値**を共有しない (P1/ADR-0022)。0.3.0-draft では国内宿泊 (travel) 0.3.0-draft の**定義体系** (スキーム二層・per-scheme の役割色・2 書体・4px 系) を採用するが、値は本 DS のファイルに独立して持つ (オーナー判断 2026-08-18・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §25)。**2026-09-07 に travel の最新版 (Task 009-58〜009-62 時点) の定義体系を追加で採用した** — 面と文字色の組み合わせ規則・リンクの装飾と状態・プレースホルダの文字色・文書レベルの見出しスケール・ラベルの用途色・Modal の表示形態 (form)・表記規則 3 節。これは §25 からの自動適用ではなく、rental-car について**別途取得した判断**である ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §29・[Issue #170](https://github.com/tocoo/coocom-design-system/issues/170))
- 非構築: 100選 (must-visit ゾーン) は DS 対象外 (2026-07-01 オーナー確認)
- 実装の旧値との対応: [migration-map.md](migration-map.md) (12 項目)。ラベル・タグ定義は [labels-tags.rental-car.md](labels-tags.rental-car.md)。トークンを実際に描画した見本は [preview.rental-car.html](preview.rental-car.html) (非正本)
- **節番号について**: 本書の §2 は既存の §2.1 スキーム / §2.2 用途 / §2.3 品質下限を保持したまま、travel `design.md` §2.1〜§2.3 に対応する 3 節を **§2.4〜§2.6** として新設している。travel と本書で節番号が 1 対 1 に対応しないのはこの §2 のみで、§3.1・§7.1・§8.1〜§8.3 は travel と同じ番号である

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
| `color.text.strong` / `body` / `mutedStrong` / `muted` | gray.900 `#212121` / gray.800 `#424242` / gray.700 `#616161` / gray.600 `#9E9E9E` (`muted` は装飾用途に加え**未入力状態の案内文字**も担う = §2.6・**AA 未達明示**) | bound |
| `color.text.inverse` (inverse 面の主要文字) | `#FFFFFF` (inverse 面 `#212121` 上 16.10:1) | bound |
| `color.text.inverseMuted` (inverse 面の補助情報) | gray.600 `#9E9E9E` (inverse 面 `#212121` 上 6.01:1・**明色面には使用しない**) | bound (§2.4) |
| `color.text.onAccent` (campaign accent 面の文字) | `#FFFFFF` (accent 面 `#E4572E` 上 3.68:1・**条件付き**) | bound (§2.4) |
| `color.text.link` | 主色 (per-scheme) `#2C50C8` (白背景 6.80:1) | bound (実装の `#0050a0` / hover `#06f` は廃止) |
| `color.text.linkHover` / `linkActive` | `{color.scheme.main.hover}` `#2340A6` (8.92:1) / `{color.scheme.main.pressed}` `#1B3488` (11.09:1) | bound (§2.5) |
| `color.surface.default` / `subtle` / `muted` / `inverse` | `#FFFFFF` / `#F9F9F9` / `#F5F5F5` / `#212121` | bound |
| `color.border.subtle` / `default` / `strong` | `#E0E0E0` / `#CCCCCC` / `#BCBCBC` | bound |
| `color.state.success` | 主色 (専用の緑 `#43a047` / `#58b85d` は廃止) | bound |
| `color.state.error` | `{color.scheme.main.error}` `#D23A3A` | bound (sub 採用時は参照先の差し替えが必要) |
| `color.accent.campaign` | `{color.scheme.main.accent}` `#E4572E` | bound (点専用・塗りボタン禁止。sub 採用時は参照先の差し替えが必要) |
| `color.accent.campaignTint` / `campaignInk` | `{color.scheme.main.accentTint}` `#F9CDBC` / `{color.scheme.main.accentInk}` `#8A2E11` (淡色面上 5.84:1・概算) | placeholder `🚧` (濃色段が仮色) |
| `color.label.discount.surface` / `text` | `{color.scheme.main.inverse}` `#C8912C` / `{color.text.inverse}` `#FFFFFF` (2.78:1 = **AA 未達**・§2.4 の例外) | bound |
| `color.label.category.surface` / `text` / `icon` / `border` | `{color.surface.default}` `#FFFFFF` / `{color.text.strong}` `#212121` (16.10:1) / `{color.accent.campaign}` `#E4572E` (3.68:1・アイコンのみ) / `{color.border.default}` `#CCCCCC` (1.61:1) | bound |
| `color.label.stock` | `{color.state.error}` `#D23A3A` (白背景 4.77:1・面なし) | bound |
| `color.membership.paid.surface` / `text` | `{color.accent.campaignTint}` / `{color.accent.campaignInk}` | placeholder `🚧` (濃色段が仮色) |
| `color.membership.free.surface` / `text` | `{color.scheme.main.tint}` `#E8EDFB` / `{color.scheme.main.ink}` `#14224A` (13.21:1) | bound |
| `color.tag.neutral.surface` / `text` | `{color.surface.muted}` `#F5F5F5` / `{color.text.body}` `#424242` (9.22:1) | bound |
| `color.focus.ring` | 主色 | bound |
| `color.mask.secret` | `{color.scheme.main.tint}` `#E8EDFB` (SecretPrice のマスク面 = B-2 無料会員の面色。グレー板 `#7f7f7f` は廃止) | bound |
| `color.overlay.backdrop` | `{color.palette.blackAlpha.45}` `rgba(0,0,0,0.45)` | placeholder `🚧` (実査待ち) |

[事実] `color.state.success` / `color.text.link` / `color.text.linkHover` / `linkActive` / `color.state.error` / `color.accent.campaign` / `campaignTint` / `campaignInk` / `color.label.discount.surface` / `color.membership.free.*` / `color.mask.secret` は現在 `main` を参照して固定されており、スキームの切替に自動追随しない。sub を正式採用する場合は `semantic.rental-car.json` の当該箇所を差し替える。

[事実] テキスト色 4 段 (`strong` / `body` / `mutedStrong` / `muted`) は文字色の**濃度段**であり、特定の用途に固定した別名は 4 段とは別に定義する。`color.text.link` / `linkHover` / `linkActive` (リンク = §2.5)・`color.text.inverse` / `inverseMuted` (inverse 面 = §2.4)・`color.text.onAccent` (campaign accent 面 = §2.4) がこれに該当する。用途別名が同じ primitive を参照する場合でも、一方の値の変更が他方へ自動的に及ぶ設計にはしない。

### 2.3 品質下限

WCAG 2.2 AA・タップ領域 44px・代替テキスト・色だけで伝えないを下限とする。例外は本書と [labels-tags.rental-car.md](labels-tags.rental-car.md) に明示したものに限る。

- [事実] テキスト色は `strong` `#212121` / `body` `#424242` / `mutedStrong` `#616161` / `muted` `#9E9E9E` の 4 段。判読性を要する補助情報 — 価格の補助テキスト (税込 / 日数 / 1 日あたり)・フォームの補足と任意表記・店舗のアクセスと営業時間・オプションの注記・未到達ステップのラベル — は `color.text.mutedStrong` (白背景 6.19:1) を使用する。`color.text.muted` (白背景 **2.68:1**) は通常テキストに求められる 4.5:1 に達しないため、判読性を要する情報には用いず、区切り記号等の装飾に限る
- [事実] A 割引率の逆色面 + 白文字は **main `#C8912C` 上 2.78:1 / sub `#C8B12C` 上 2.15:1** であり、両スキームとも通常テキスト 4.5:1 だけでなく大きなテキスト 3:1 も満たさない。2 スキームは値が異なるため、コントラスト比を伴う記述をワイルドカード表記で 1 行に束ねない
- [事実] 上記の白文字を成立させる例外条項は **§2.4「A 割引率ラベルに限る白文字の例外」として明文化した** (Task 009-63・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。[governance/owner-decisions.md](../../../governance/owner-decisions.md) §25 の Does Not Authorize が「例外条項の明文化は未了」としていた状態は解消した。**AA 未達であることは明示したうえで許容するものであり、適合宣言ではない**
- 本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない

### 2.4 面 (背景) と文字色の組み合わせ規則

色を**面 (背景)** として使う場合、許可される文字色と文字サイズ・ウェイトの条件は面ごとに異なる。

#### 用語の定義 (本節で用いる条件)

- **ウェイトの境界**: 「**bold**」は `typography.fontWeight.bold` (`700`) 以上を指す (`black` `900` を含む)。「**通常ウェイト**」は `700` 未満を指す (`regular` `400`・`medium` `500` を含む)。この 2 語で全ウェイトを排他的に二分する
- **条件 (a)**: `24px` 以上 (**ウェイトを問わない**) — WCAG 2.2 の大きなテキスト
- **条件 (b)**: `20px` 以上かつ **bold** (`700` 以上) — WCAG 2.2 上の bold 側の下限は約 `18.7px` だが、実運用上の誤差・フォント差を避けるため DS では `20px` を下限とする
- **(a) (b) のいずれも満たさない文字**: **(i) `20px` 未満のすべて** および **(ii) `20px` 以上 `24px` 未満かつ通常ウェイト** — (a) (b) (i) (ii) で全サイズ・全ウェイトを網羅する
- **「大きなテキスト相当」**: (a) (b) のいずれかを満たす文字を指す — **サイズ・ウェイトの条件**。**WCAG 2.2 の大きなテキストより DS の範囲は狭い** (bold 側の下限を約 `18.7px` から `20px` へ引き上げているため)。WCAG の語をそのまま適用しない
- **「大きなテキスト基準」**: WCAG 2.2 が大きなテキストに求める**コントラスト比 `3:1`** を指す — 下表「大きなテキスト (3:1)」列の判定。**コントラスト比の基準であり、サイズ・ウェイトの条件ではない**
- 上記 2 語は別概念であり混用しない。**コントラスト比が「大きなテキスト基準」を満たすことは、その文字を使用してよいことを意味しない** (使用可否はサイズ・ウェイトの条件 = 「大きなテキスト相当」で決まる)

#### 検証した組み合わせ

下表は本書で検証した組み合わせであり、**表に無い組み合わせを検証済みとして扱わない**。本表は**単色面のみ**を対象とし、画像・グラデーションを面 (背景) とする場合の文字色とコントラスト確保の方法 (scrim の要否・評価方法) は本表の対象外で**未定義**である (未確定事項の一覧)。コントラスト比はいずれも本 Repository で WCAG 2.x 標準式により実測した値である。

| 面 (背景) | 文字 | 実測 | 通常テキスト (4.5:1) | 大きなテキスト (3:1) | 扱い |
| --- | --- | ---: | --- | --- | --- |
| `color.accent.campaign` `#E4572E` | `color.text.onAccent` `#FFFFFF` | 3.68:1 | 未達 | 達成 | **条件付きで許可** ((a) (b) を満たす文字のみ) |
| `color.accent.campaign` `#E4572E` | `color.text.strong` `#212121` | 4.37:1 | 未達 | 達成 | **規則としては使用しない** (面上の文字色は `color.text.onAccent` に限定。本行は参考値) |
| `color.surface.inverse` `#212121` | `color.text.inverse` `#FFFFFF` | 16.10:1 | 達成 | 達成 | 許可 |
| `color.surface.inverse` `#212121` | `color.text.inverseMuted` `#9E9E9E` | 6.01:1 | 達成 | 達成 | 許可 (補助情報) |
| `color.surface.inverse` `#212121` | `color.text.mutedStrong` `#616161` | 2.60:1 | 未達 | 未達 | **禁止** (`mutedStrong` は明色面用) |
| `color.scheme.main.inverse` `#C8912C` | `#FFFFFF` | 2.78:1 | 未達 | 未達 | **禁止** (例外は下記「A 割引率ラベルに限る白文字の例外」のみ) |
| `color.scheme.main.inverse` `#C8912C` | `color.text.strong` `#212121` | 5.78:1 | 達成 | 達成 | 許可 |
| `color.scheme.sub.inverse` `#C8B12C` | `#FFFFFF` | 2.15:1 | 未達 | 未達 | **禁止** (同上) |
| `color.scheme.sub.inverse` `#C8B12C` | `color.text.strong` `#212121` | 7.50:1 | 達成 | 達成 | 許可 |
| `color.surface.default` `#FFFFFF` | `color.text.strong` `#212121` | 16.10:1 | 達成 | 達成 | 許可 (C カテゴリ・特集ラベルの面 + 文字 = `color.label.category`。サイズ・ウェイトの条件を伴わない) |
| `color.surface.default` `#FFFFFF` | `color.accent.campaign` `#E4572E` (文字色として) | 3.68:1 | 未達 | 達成 | 条件付き ((a) (b) を満たす文字のみ) |
| `color.surface.subtle` `#F9F9F9` | `color.accent.campaign` `#E4572E` (文字色として) | 3.50:1 | 未達 | 達成 | 条件付き ((a) (b) を満たす文字のみ) |
| `color.surface.muted` `#F5F5F5` | `color.accent.campaign` `#E4572E` (文字色として) | 3.38:1 | 未達 | 達成 | 条件付き ((a) (b) を満たす文字のみ) |
| `color.surface.muted` `#F5F5F5` | `color.tag.neutral.text` `#424242` | 9.22:1 | 達成 | 達成 | 許可 (D 中立タグの面 + 文字) |
| `color.scheme.main.tint` `#E8EDFB` | `color.scheme.main.ink` `#14224A` | 13.21:1 | 達成 | 達成 | 許可 (B-2 無料会員ラベル・SecretPrice のマスク面) |
| `color.accent.campaignTint` `#F9CDBC` (accent 淡色段・面) | `color.accent.campaignInk` `#8A2E11` (🚧 仮色) | 5.84:1 (概算・🚧) | 達成 (概算・🚧) | 達成 | **条件付き** (b2 = 小サイズ非操作ラベルの面 + 濃色文字。濃色段が **🚧 仮色**のため実色値確定後に本 Repository で検証・確定する) |
| `color.accent.campaignTint` `#F9CDBC` (accent 淡色段・面) | `color.text.strong` `#212121` | 11.11:1 | 達成 | 達成 | 許可 (淡色面 + 既存の濃色文字。b2 の代替として成立) |
| `color.surface.default` `#FFFFFF` | `color.state.error` `#D23A3A` | 4.77:1 | 達成 | 達成 | 許可 (E1 在庫僅少 = `color.label.stock`・面なしの文字) |

- [事実] 上表は**文字と面の**組み合わせを対象とする。C カテゴリ・特集ラベルの枠線 (`color.label.category.border` = `color.border.default` `#CCCCCC`) は非テキストの境界であり本表の対象外だが、実測値を記録する — 白面 (`#FFFFFF`) 上 **1.61:1**・`color.surface.subtle` (`#F9F9F9`) 上 **1.53:1**。いずれも**非テキスト UI 要素の 3:1 に達しない**。枠線は、白系の面の上では面のみで境界が生じないこと (白 × 白 1.00:1・白 × `surface.subtle` 1.05:1・同実測) に対する分離の補助であり、ラベルの識別は文字 (16.10:1) が担う。適合宣言は行わない。既存の border 3 段はいずれも白面上 3:1 に達しない (`subtle` `#E0E0E0` 1.32:1 / `default` `#CCCCCC` 1.61:1 / `strong` `#BCBCBC` 1.90:1 = 同実測)

#### campaign accent 面上の文字

- [事実] `color.accent.campaign` (`#E4572E`) 上では、白文字 3.68:1・濃色文字 `#212121` 4.37:1 のいずれも通常テキストの 4.5:1 に達しない。**既存色の範囲では、campaign accent 面上で任意サイズの通常テキストを成立させる文字色は存在しない**
- [決定] campaign accent 面上の文字色は **`color.text.onAccent` のみ**を使用する。`color.text.strong` (`#212121`・4.37:1) は大きなテキスト基準は満たすが、面上の文字色を 1 つに定めるため**規則としては使用しない** (表の値は参考)
- [決定] campaign accent を**面として使用できるのは、条件 (a) (b) のいずれかを満たす文字に限る** ((a) `24px` 以上・ウェイトを問わない／(b) `20px` 以上かつ bold)
- [決定] **(a) (b) のいずれも満たさない文字 ((i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト) には面として使用しない**。ウェイトを上げれば自動的に適合するという定義にはしない (`20px` 未満は bold でも不可)
- [決定] `color.text.onAccent` の存在は「白であれば常にアクセシブル」を意味しない。背景色と文字サイズ・ウェイトの確認を省略しない

#### campaign accent を面として使用できない場合の代替規則

(a) (b) のいずれも満たさない文字 — すなわち (i) `20px` 未満のすべて、および (ii) `20px` 以上 `24px` 未満かつ通常ウェイト — には次を用いる。

1. **[既定] neutral dark 面へ切り替える** — 背景 `color.surface.inverse` (`#212121`) + 文字 `color.text.inverse` (16.10:1)。**既存トークンの範囲で通常テキスト基準 4.5:1 を満たす唯一の面**である
2. accent を**非テキスト要素**に限定する — 境界色・アイコン・点的装飾 (非テキスト UI 要素の 3:1 は満たす)。**accent を文字色として明色面に置く方法は、この場合の代替にならない** (`default` 3.68:1 / `subtle` 3.50:1 / `muted` 3.38:1 はいずれも通常テキスト 4.5:1 に達しない。**accent 淡色面 (`color.accent.campaignTint` `#F9CDBC`) 上ではさらに下がり 2.54:1 となる** — 淡色面は白面から離れる分だけ分母が増える。これは accent を**文字色**として淡色面に置く場合であり、b2 = 淡色面 + accent **濃色段**文字 (別トークン `campaignInk`) とは区別する)
3. **accent 淡色面 (b2)** — 面 `color.accent.campaignTint` (`#F9CDBC`) + 文字 `color.accent.campaignInk` (`#8A2E11`)。小サイズ (12px) ラベル向け。**accent 濃色段が 🚧 仮色**のため、成立は実色値確定後に検証する。**それまでは 1 (neutral dark 面) を用いる**

(a) (b) を満たす文字については、accent 面を用いない次の構成も選べる。

4. accent を**文字色**として明色面に置く — `color.surface.default` 3.68:1 / `subtle` 3.50:1 / `muted` 3.38:1。いずれも大きなテキスト基準のみを満たすため、**(a) (b) を満たす文字に限る**

- [事実] 上記はいずれも既存 palette の組み合わせで成立するため、代替背景色の primitive を新設していない (accent の 4 段は b2 のために追加したものであり代替背景ではない)
- [決定] 禁止: campaign accent 面上に **(a) (b) を満たさない白文字** を置く / `onAccent` の存在だけを理由にコントラスト確認を省略する / AA 未達を「ブランド表現」で自動的に許容する / 文字へ縁取り・影を付けることでコントラスト不足を解決したものとして扱う

#### scheme inverse 色を面として使用する場合

- [事実] 白文字は `color.scheme.main.inverse` (`#C8912C`) 上で 2.78:1、`color.scheme.sub.inverse` (`#C8B12C`) 上で 2.15:1 であり、**両スキームとも**通常テキスト 4.5:1 だけでなく大きなテキスト 3:1 も満たさない
- [決定] 両スキームの逆色を面として使用する場合の文字色は `color.text.strong` (`#212121`) を原則とする (main `#C8912C` 上 5.78:1・sub `#C8B12C` 上 7.50:1)。白文字は正式な通常利用として許可しない
- [事実] 逆色の値は本 DS では**割引ラベル背景としての面用途**を持つ (`color.label.discount.surface`)。専用の semantic alias (`color.text.onSchemeInverse` 等) は追加していない
- [事実] 本 DS には評価色 (`color.icon.rating` = ReviewStars 星の色) が存在しない。ReviewStars は国内宿泊 (travel) 固有の Component であり、rental-car に対象の Component がないため用途トークンを持たない。したがって travel §2.1 が定める「評価色と販促面色の用途境界」は本 DS では成立しない
- [決定] 2 スキームは値が異なるため、値やコントラスト比を伴う記述でワイルドカード表記を用いて 1 行に束ねない

#### A 割引率ラベルに限る白文字の例外

上記の「campaign accent 面上の文字」「scheme inverse 色を面として使用する場合」は、いずれも白文字を通常利用として許可しない。このうち **scheme inverse 面**についてのみ、次の限定条件を**すべて**満たす場合に限り、白文字を**例外**として許容する (AA 未達を明示する)。**campaign accent 面は本例外の対象ではない**。

- [決定] **用途 = A 割引率ラベル (`color.label.discount`)** に限る。非操作の点的ラベルであっても、A 割引率ラベル以外 (B 会員種別・**C カテゴリ・特集**・D 中立タグ・E 在庫/販売状態・G 写真枚数) は本例外の対象外とする。操作可能なバッジは badge ではなく action 系 Component として扱い、同じく対象外とする
- [決定] **面 = scheme 逆色 (`color.scheme.main.inverse` `#C8912C` / `color.scheme.sub.inverse` `#C8B12C`)** に限る。`color.surface.inverse` (`#212121`・16.10:1) 以外へ拡大せず、**`color.accent.campaign` (`#E4572E`) 面 + 白文字も本例外に含めない** (白文字が通常テキスト 4.5:1 を満たす面は `surface.inverse` の 1 面のみ)
- [決定] サイズ・ウェイトは**不問** (小サイズ・通常ウェイトを含む)。ただし**コントラストが AA (通常テキスト 4.5:1) に未達であることを明示する** (main 逆色 × 白 2.78:1・sub 逆色 × 白 2.15:1)。適合宣言は行わない
- [決定] 本例外は「`color.scheme.*.inverse` を面として使用する場合の文字色は `color.text.strong` に固定・白文字を使用しない」原則に対する**限定的な例外**であり、原則そのものは維持する。**campaign accent 面の (i) (ii) 白文字禁止は例外なく維持する**
- [決定] 禁止: 本例外を A 割引率ラベル以外 (本文・操作要素・大面積・他カテゴリのラベル) へ適用する / 指定面以外へ拡大する / 縁取り・影でコントラスト不足を解決したものとして扱う / AA 未達を明示せずに用いる
- [事実] 本条項は継承元である国内宿泊 (travel) `design.md` §2.1 の同名条項 (Task 009-60R で「非操作の点的ラベルに限る白文字の例外」から改称・適用範囲を A 割引率ラベル + 逆色面へ縮小したもの) を、**縮小後の形で** rental-car の規則として明文化したものである。縮小前の形は本 DS に持ち込まない

#### accent の帰属

- [決定] **accent を面として持つのは B 会員種別 (`color.membership.paid` = accent 淡色段) のみ**とし、**C カテゴリ・特集 (C1 企画名 / C2 販売条件) は accent を「アイコン (点)」として持つ** (`color.label.category.icon`)。C の面は白 (`color.surface.default`) とし accent で塗らない
- [決定] C の 12px (`label.fontSize.sm`) ラベルは **白面 × `color.text.strong` = 16.10:1 で成立する**。サイズ・ウェイトの条件を伴わないため、C については上記代替規則の 1 (neutral dark 面) / 3 (accent 淡色面) を要しない
- [決定] accent アイコン (`#E4572E`) は白面上 3.68:1 で、**非テキスト UI 要素の 3:1 は満たすが通常テキスト 4.5:1 には達しない**ため、**アイコンに限り**用いて文字色・面色には用いない
- [決定] **白系の面 (`color.surface.default` `#FFFFFF` / `color.surface.subtle` `#F9F9F9`) の上に C を置く場合にのみ**、`color.label.category.border` (= `color.border.default` `#CCCCCC`) の枠線を `border.width.thin` (1px) で引く。**写真の上・有色面の上では枠線を引かず**面のみで分離する (影・スクリムは用いない)
- [事実] 本項により、[labels-tags.rental-car.md](labels-tags.rental-car.md) C1 が置いていた「accent の帰属が確定するまで面色は暫定」の `🚧` と、本書の未確定事項にあった「accent の帰属」の `🚧` は解消した

### 2.5 リンクの装飾と状態

リンクの**色**は `color.text.link` (= 各スキームの主色) で確定済み。本節は**色以外の装飾 (下線) と、状態 (hover / visited / active / focus) ごとの取り扱い**を定める。`color.text.link` の値・参照先は本節で変更しない。状態語そのものを新設するものではない (状態の固定リストは [components.md](components.md) §1 が正)。`visited` について本節が定めるのは「専用色を設けない = 既定と同じ」という取り扱いであり、固定リストへの追加ではない。

文字色の列は対象を限定しない (standalone なリンクを含む)。下線の列は**文中リンクのみ**を対象とする。

| 状態 | 文字色 (対象を限定しない) | 下線 (文中リンクのみ) |
| --- | --- | --- |
| 既定 | `color.text.link` (`#2C50C8`・白背景 6.80:1) | あり |
| hover | `color.text.linkHover` (`scheme.main.hover` `#2340A6`・8.92:1) | あり (維持) |
| active (押下中) | `color.text.linkActive` (`scheme.main.pressed` `#1B3488`・11.09:1) | あり (維持) |
| visited | `color.text.link` (既定と同じ・専用色を設けない) | 既定と同じ |
| focus | `color.text.link` (既定と同じ) | 既定と同じ + `color.focus.ring` の `outline` |

- [決定] 本文・説明文などの**文中リンクには下線を付す**。リンクであることを色だけで伝えない。**下線を外す既定は置かない**
- [決定] hover は**下線を維持したまま文字色を `color.text.linkHover` へ変更する**。hover で下線を外さない (下線の消失はリンクでなくなったように読める)
- [決定] active (押下中) は `color.text.linkActive` を使用する
- [決定] visited に**専用色を設けない**。訪問済みリンクは `color.text.link` を維持する。理由: 既存 palette に visited 用の色値が無く、本書では新しい色値 (primitive) を追加しないため。visited を色で区別する要否は未確定事項へ残す
- [決定] focus は Component 共通の `color.focus.ring` による `outline` を用いる ([components.md](components.md) §1)。hover の色変更で focus 表現を代替しない
- [決定] **リンクの状態表現に `opacity` を用いない**。`opacity` は色トークンで表現できず、状態の識別が色・下線・不透明度へ分散する。[components.md](components.md) §1 は「hover は `opacity` 約 .85 の暫定 `🚧`」を全 Component の暫定参照として定めているが、**リンクの hover は本節が定める色変更 (`color.text.linkHover`) を用い、同暫定参照の対象外とする** (同 §1 にリンクを対象外とする除外を置いている)
- [事実] 実装 (japan ゾーン) の旧リンク色 `#0050a0` と hover `#06f` は廃止済みであり ([migration-map.md](migration-map.md))、本節はこれらを DS 規則として採らない
- [注意] 本節が定める**下線の既定は文中リンクを対象とする**。カード全体リンク・ナビゲーション項目・パンくずなど、領域とレイアウトでリンクであることが成立する standalone なリンクへ下線の既定を及ぼすかは未判定 (未確定事項の一覧)。**状態ごとの文字色 (hover / active / visited) と focus の取り扱いは対象を文中リンクに限定しない**ため、standalone なリンクにも適用される

### 2.6 未入力状態の文字色

- [決定] **未入力状態の案内文字の色は `color.text.muted` (`#9E9E9E`・白背景 2.68:1) に統一する。** 対象は `input` / `textarea` の `::placeholder`、Select の未選択値 (選択前の `option` に相当する表示)、およびその他の入力フィールドの未入力表示であり、**UI の種別で限定しない** (判断 C-5・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)
- [決定] **`color.text.muted` は通常テキストに求められる 4.5:1 に達しない。AA 未達であることを明示する。** 適合宣言は行わない。本節は §2.3 の品質下限に対する明示的な例外であり、未入力状態以外の用途へ拡張しない (判読性を要する補助情報は `color.text.mutedStrong` `#616161`・6.19:1)
- [決定] 上記は**色の許容であって、未入力であることを色だけで伝えてよいという意味ではない**。未入力の識別は文言 (「選択してください」「出発エリア・空港名」等) が担う (色だけで伝えない = §2.3 の品質下限)
- [決定] 未入力の案内文字と入力済みテキスト (`color.text.body` `#424242`) の判別を色の差のみに依存させない。入力済みかどうかの識別は実際の文字列の有無で成立する
- [決定] 案内文字を必須項目・ラベル・エラーメッセージ・入力形式の説明の代替として用いない
- [決定] **プレースホルダ専用の用途トークン (`color.text.placeholder`) は定義しない。** 未入力状態を UI の種別で分けない以上、専用の別名を設ける必要がない。**新しい色値 (primitive) は追加していない**
- [事実] 継承元の travel は §22 (2026-08-04・Web部責任者判断) で **Select の未選択値に限る**例外として記録しており、通常の `input` / `textarea` の `::placeholder` は `color.text.placeholder` (`#616161`・6.19:1) を維持している。**rental-car は本節で UI の種別による限定を置かない判断 (2026-09-07・§29) を採った**。3 独立 DS の原則 (P1/ADR-0022) により、本判断は travel・inbound の成果物へ及ばない
- 🚧 未入力状態を含むフォーム入力の状態一式 (枠色・背景色・必須表現・検証表示) は実査待ち (follow-up #2)。本節は**文字色のみ**を定義する

## 3. タイポグラフィ

明朝とゴシックの 2 書体で構成する。

| 用途 | 値 | 状態 |
| --- | --- | --- |
| 本文・UI (`font.body`) | LINE Seed JP (フォールバック Noto Sans JP) / 1rem (16px) / lh 1.8 | bound |
| 見出し (`font.heading`。文書レベル h1〜h6 の**既定**。役割による書体の選択・幅による段下げは §3.1) | LINE Seed JP・`font.heading.weight` 700 / `font.heading.lineHeight` 1.3。h1 2.5rem 〜 h6 1rem (既定 = `breakpoint.lg` 1024px 以上) | bound (§3.1) |
| display・hero・車種クラス名 (`font.display`。書体選択の規則 = §3.1) | 明朝 Noto Serif JP。`lgSize` 3rem (Hero) / `mdSize` 1.125rem (車種クラス名) | bound |
| 数字・価格 (`font.price`) | 本文と同族・700・tabular-nums。数字 1.25rem / 補助 0.75rem | bound |

- 文字サイズ: root 16px・rem 基準。xs .75 / sm .875 / md 1 / lg 1.125 / xl 1.25 / 2xl 1.5 / 3xl 2 / 4xl 2.5 / display-lg 3rem
- ウェイト: 400 / 500 / 700 / 900。行高: tight 1.3 (見出し = `font.heading.lineHeight`) / normal 1.5 / relaxed 1.8 (本文 = `font.body.lineHeight`)
- [事実] **見出しの semantic は h1〜h6 の 6 段を定義する** (Task 009-63)。旧版が「h1 / h2 / h3 の 3 段のみ定義し h4 以下は未定義」としていた状態は §3.1 の新設により解消した。追加した `h4Size` / `h5Size` / `h6Size` はいずれも既存スケールへの割当であり、新しいサイズ値 (primitive) は追加していない
- [事実] 車種クラス名は明朝 `font.display.mdSize` (18px) を使用する。**書体は要素ではなく役割で選ぶ** (§3.1) — 車種クラス名は Display の役割として明朝を明示的に選択したものである。Task 009-63 で `font.heading.h3Size` が `lg` (18px) から `2xl` (24px) へ変わったため、**`font.display.mdSize` (18px) とゴシックの `h3Size` (24px) は同値でなくなった** (旧版が「同一要素へ 2 系統を割り当てない」と書いていた同値衝突は解消した)
- [事実] 旧 Q4 (本文 15px / lh 1.4・Kozuka Gothic Pro と游ゴシックの混在) は本判断により解消した。実装値は [migration-map.md](migration-map.md) を参照

### 3.1 文書レベルの見出しスケール (h1〜h6)

Component に属さない**文書レベルの見出し** (`h1`〜`h6` そのもの) に適用する既定値を定義する。本節が定めるのは `h1`〜`h6` の各要素に当てる既定値 (サイズ・太さ・行間・書体) のみであり、**どの画面のどのコンテンツを `h1` / `h2` とするかという画面別の見出し階層・semantic role の割当は定めない** (本 DS の Screen Requirements レイヤーは未着手)。**本節の既定値は `breakpoint.lg` (1024px) 以上に適用される値であり、1024px 未満の幅では下表の「狭い幅」列の段を用いる。**

| 要素 | サイズ (semantic) | 参照先 | 既定 (`breakpoint.lg` 1024px 以上) | 狭い幅 (1024px 未満) | 太さ | 行間 |
| --- | --- | --- | --- | --- | ---: | ---: |
| `h1` | `font.heading.h1Size` | `typography.size.4xl` | 2.5rem (40px相当) | `typography.size.3xl` 2rem (32px相当) | 700 | 1.3 |
| `h2` | `font.heading.h2Size` | `typography.size.3xl` | 2rem (32px相当) | `typography.size.2xl` 1.5rem (24px相当) | 700 | 1.3 |
| `h3` | `font.heading.h3Size` | `typography.size.2xl` | 1.5rem (24px相当) | `typography.size.xl` 1.25rem (20px相当) | 700 | 1.3 |
| `h4` | `font.heading.h4Size` | `typography.size.xl` | 1.25rem (20px相当) | `typography.size.md` 1rem (16px相当) | 700 | 1.3 |
| `h5` | `font.heading.h5Size` | `typography.size.md` | 1rem (16px相当) | 同左 (段を下げない) | 700 | 1.3 |
| `h6` | `font.heading.h6Size` | `typography.size.md` | 1rem (16px相当) | 同左 (段を下げない) | 700 | 1.3 |

- [決定] **本節の既定値が適用される幅は `breakpoint.lg` (1024px) 以上とする。** 1024px 未満では上表の「狭い幅」列の段を用いる。段を移す境界は `breakpoint.lg` の **1 つのみ**とし、`breakpoint.sm` (640px) / `breakpoint.md` (768px) / `breakpoint.xl` (1280px) では見出しのサイズ段を変えない。**根拠** = §4 の代表 viewport `390 / 768 / 1280 / 1440px` を 1024px がちょうど 2 対 2 に分ける (狭 = 390・768 / 広 = 1280・1440)
- [決定] **上表の 2 列は一意の規則であり、どの breakpoint でどの段へ移すかを画面ごとの裁量に委ねない。** 画面ごとに境界・段数を選ぶことは認めない
- [決定] **上表の範囲内での段下げは、後述の「既定から外れる」に該当しない。** したがって画面ごとの都度の承認を要しない。承認を要するのは上表の外に出る場合 — 境界を `breakpoint.lg` 以外に置く／上表と異なる段を用いる／§3 のスケールに無い値を用いる／幅が広がるとサイズが小さくなる — に限る
- [決定] **文書レベルの見出しには、実寸が 4 の倍数である段のみを用いる** (判断 D-4)。`typography.size` の 9 段のうち 4 の倍数でないのは `sm` (14px) と `lg` (18px) の 2 段であり、いずれも文書レベルの見出しには用いない。本規則により `font.heading.h3Size` の参照先を `lg` (1.125rem・18px) から `2xl` (1.5rem・24px) へ改めた (判断 D-2)。**根拠** = `spacing` 全 11 段・`iconSize` 全 4 段・`breakpoint` 全 4 段・`radius` の実寸 3 段はいずれも 4 の倍数であり (`radius.full` 9999px は pill の番兵値)、4 の倍数でない段は `typography.size` の上記 2 段のみである (本 Repository の実測)
- [決定] **本規則の対象は文書レベルの見出しに限る。** `font.display.mdSize` (`lg` 1.125rem・18px・車種クラス名) は**対象外**であり、値・参照先とも変更しない (判断 D-4)。`sm` (14px) も対象外である — 同段は `label.fontSize.md` / `label.numberSize.sm` として §8.1 の「数字は `%OFF` より §3 のスケールで 1 段上」の規則および `label.*` の器トークンに組み込まれ、見出し以外の用途で確定済みである。**4px 系 (§4) の適用範囲を `typography` 全体へ拡げない** — §4 の記述は引き続きスペーシングを対象とする
- [事実] 上記の結果、`h5` と `h6` はいずれの幅でも同値 (1rem) となり、文書レベルの見出しのサイズ段は実質 **5 段** (2.5rem / 2rem / 1.5rem / 1.25rem / 1rem) になる
- [事実] 1024px 未満では `h4` / `h5` / `h6` がいずれも 1rem となり、本文 (`font.body.size` 1rem) とも同値になる。**狭い幅で寸法によって区別できる文書レベルの見出しは `h1` / `h2` / `h3` の 3 段である。** 太さによる区別は本書の根拠としない (本文のウェイトが正本上定義されていないため。後述の [事実])
- [決定] 書体は `font.heading.family` (LINE Seed JP・ゴシック) を文書レベルの既定とする。明朝 (`font.display.family`) は Display・Hero・車種クラス名で**明示的に選択する**書体であり、文書レベルの見出しの既定ではない (§3)
- [決定] **本節が定めるのは既定値であり、要素 (`h1`〜`h6`) と書体の対応を固定しない。** 書体の選択は**役割** (表現 = Display / 機能 = UI・文書構造。§3 の 2 書体構成) によって決まり、要素名によっては決まらない。したがって文書レベルの見出しの役割が §3 の Display・Hero・車種クラス名にあたる場合は、その要素が `h1` であっても `font.display.family` (明朝) を**明示的に選択してよい**。既定 (`font.heading.family`) は、役割による明示的な選択がない場合に適用される値である
- [決定] 上記の明示的な選択の結果、サイズ・太さ・行間が本節の既定 (上表の「既定」列・「狭い幅」列の双方を含む) から外れることは**原則として認めない**。認めるのは、**利用目的とデザイン上の必然性が明確に示され、承認を得た場合**に限る (**承認主体 = Web部責任者**)。§8.3 が定める**適用外 (クリエイティブ)** にあたるもの (PR 帯・特集帯・キービジュアル・支給バナー) や LP はこれにあたる**例**であり、許容される場面をこの 2 つに限定するものではない。§8.3 の適用外にあたる場合は、あわせて同節の扱い (必然性・デザイン上の制約・目的の提示／**カラーは厳守**／品質の下限／どちらの段かの事前の宣言・宣言がなければ適用とみなす) に従う
- [決定] **サイズ・太さ・行間の既定は書体の選択と独立に定める。** 書体として明朝 (`font.display.family`) を明示的に選択しても、本節の既定 (上表の各段・太さ 700・行間 1.3) はそのまま適用される
- [事実] 本節が定めるのは書体の**選択規則**であり、個々の見出しが Display・Hero・車種クラス名にあたるか否かの**該当判断は本書では行わない**
- [決定] 太さは `font.heading.weight` (`typography.fontWeight.bold` = 700) を h1〜h6 共通の既定とする
- [決定] 行間は `font.heading.lineHeight` (`typography.lineHeight.tight` = 1.3) を h1〜h6 共通の既定とする。`relaxed` (1.8) は本文の値であり見出しへ適用しない
- [決定] **文書レベルの見出しと Component の見出しは同一トークン群 (`font.heading.*`) を共用する**。文書レベル用の別系統を設けない。Component 側で文書レベルの既定から外れる値が必要な場合は当該 Component 仕様に**明示的に**記載する (暗黙の上書きを認めない)
- [決定] **新しいサイズ値・行間値・ウェイト値 (primitive) は追加しない**。h1〜h6 はいずれも既存スケール (`4xl` / `3xl` / `2xl` / `xl` / `md`) への割当である。狭い幅の段も同じスケール内の既存段への割当である。**幅ごとの値を持つ semantic トークンも新設しない** — 狭い幅の段は上表で既存 primitive 段への割当として示す
- [事実] `h5` / `h6` は本文と同サイズ (1rem) となる。本文との差はウェイトと行間だが、**本文のウェイトは正本上定義されていない** (`font.body` は `family` / `size` / `lineHeight` の 3 トークンのみで `weight` を持たず、§3 の表の本文行にもウェイトの記載がない)。したがって**ウェイトによる区別を本書の根拠としない**。行間の差 (見出し 1.3 / 本文 1.8) は折り返しが生じる場合にのみ視覚差となる。書体も `typography.fontFamily.heading` と `sans` はいずれも同じフォントスタックを先頭に持つため差がない。`h5` / `h6` と本文の区別根拠、および `h5` と `h6` の相互の区別根拠が不足していることは未確定事項の一覧に起票している
- [決定] 見出しサイズを UA 既定に委ねない。理由は次のとおり
  - HTML 標準の Rendering セクションが定める見出しサイズは `em` 基準 (親の `font-size` に対する相対値) であり、親の `font-size` が異なる文脈で実寸が変わる。§3 が定める **rem 基準と整合しない**
  - 同セクションには `:is(article, aside, nav, section)` の入れ子段数に応じて `h1` のサイズを変える規則があり、`h1` の実寸が文書構造に依存する
  - `h5` 0.83em / `h6` 0.67em は本文 1rem 基準で 13.3px / 10.7px となり、本文より小さい
- [注意] 本節の既定を実装へ反映すると文書レベルの見出しの実寸が従来の実装値から変わる。反映の範囲・順序・期限は本書では決定しない (実装側タスクの範囲)。実装 (japan ゾーン) の見出し実測値は本 Repository で実査していない

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: **4px (0.25rem) 系** `spacing.1`〜`16`。旧 Q3 (5px 刻みユーティリティ) は解消し、実装値は [migration-map.md](migration-map.md) に記録した
- コンテナ幅: **975 / 1195 / 1425px** (`size.container.sm` / `md` / `lg`)
- ブレークポイント: **`640 / 768 / 1024 / 1280`** (Q5 決定 2026-07-24: 3DS 共通値。0.3.0-draft で `$status` を bound へ)。japan ゾーン実装は 2段 (959/960) のみで、置換の扱いは [migration-map.md](migration-map.md)
- 代表 viewport (画面設計・HTML 確認用の表示幅): **`390 / 768 / 1280 / 1440px`** (3DS 横断・Web部責任者判断 2026-07-24・Task 009-18-BP1)。**表示確認用の代表幅であり breakpoint token ではない**

## 5. 角丸・シャドウ・モーション

- 角丸: `sm` 4px / `md` 8px / `lg` 16px / `full` (pill)。用途トークンは **4 系統** (action / card / badge / overlay)
  - `radius.action` = full (pill) — **ボタン・CTA・入力要素 (Input / Select / SearchForm のフィールド)・チップ型操作要素**。旧 R-01 (4px 固有形状を国内の意匠とする) は**廃止**した。縦グラデ・emboss 影・text-shadow も廃止 ([migration-map.md](migration-map.md))
  - `radius.badge` = **sm (4px)** — 非操作のバッジ・ラベル (A〜G の全ラベル。器 `label.radius` が本トークンを参照)
  - `radius.card` = 暫定 `md` `🚧` (ResultCard の実 px 未取得)
  - `radius.overlay` = 暫定 `lg` (16px) `🚧` — オーバーレイの角丸 (Modal の表示形態 form = sheet の上端 2 隅等・§7.1)
- [決定] **入力要素の角丸を `radius.action` (pill) へ統一し、`radius.input` (4px) を廃止した** (判断 F-5・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。操作要素の角丸を 1 つに定め、同一フォーム内でボタン (pill) と入力欄 (4px) が異なる形状を持つ状態を解消する。`semantic.rental-car.json` から `radius.input` を削除し、[components.md](components.md) の Input / Select / SearchForm の意匠記述を `radius.action` へ改めた。用途トークンは 5 系統から **4 系統**へ
- [決定] 割引率ラベル・状態バッジへ `radius.action` (pill) を使用しない。pill 形状は操作要素のシグネチャであり、非操作のラベルに用いると操作要素と誤認される。**バッジが操作可能な場合は badge ではなく action 系 Component として扱う** (その場合の角丸は `radius.action`)
- シャドウ: primitive に 3 段 (`sm` / `md` / `lg`) を暫定値で置くのみで、**用途 semantic は未定義**である `🚧` (follow-up #13。実値未抽出)。実値が確定するまで Component 仕様で個別の段を指定しない
- モーション: 300ms ease を暫定とする `🚧` (follow-up #3。実装は 0.3s ease-in-out と 0.35s ease が混在)
- z 軸: dropdown 1000 / sticky 1100 / overlay 1200 / modal 1300 / toast 1400

## 6. アイコン・画像・オーバーレイ

- アイコン体系: **Font Awesome 6**。サイズ 16 / 20 / 24 / 32px (既定 20px)。旧 Q8 (slick 等・「新規制作分のみ統一」) は本判断により解消した。実装の FontAwesome 4 記法は [migration-map.md](migration-map.md)
- 画像なし表現: No Image fallback (`surface.muted` 面 + `text.mutedStrong` の文字・比率 4:3)。ロゴ素材 (ToCoo!・レンタカー各社) は未提供 `🚧` であり、ワードマークで代用する。**記憶からの再構築は行わない**
- 画像比率・トリミング基準: 車両写真の選定基準は未定義 `🚧` (Assets レイヤー着手時)
- オーバーレイ: **表示形態 (form) は `drawer` (既定) / `sheet` / `popover` の 3 値**をとる (§7.1 が正)。backdrop は `color.overlay.backdrop` (`🚧` 暫定値 `rgba(0,0,0,0.45)`) を 3 形態すべてで使用する。同時に開くオーバーレイは 1 つに限る
  - `🚧` **3 DS 横断の Modal 実装基盤は未決**である ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §1 Q9)。本 DS で drawer を既定形態とし §7.1 の form 軸を正式仕様とする判断は **rental-car に限定**して取得したものであり ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §29 判断 F-1)、横断の実装基盤を確定しない
  - **BottomSheet / Popover は「未承認の拡張候補」ではなくなった** — §7.1 の表示形態 (form) `sheet` / `popover` として本文へ統合した (判断 F-1)。実装基盤は drawer 単一を維持し、**第 3 の Modal 実装基盤を導入しない**
  - remodal / LightBox など別のオーバーレイ基盤を新規に追加しない

## 7. コアコンポーネント

正: [components.md](components.md)。travel と同型 7 + 本 DS で先行定義 3 + レンタカー固有 8 の計 18 で構成する。

- travel と同型 (7 件・定義体系の採用。**意匠と値は本 DS のファイルで定義し、travel のファイルを参照・共有しない** = 上記「独立性」): Button / Input / PriceTag / Header / Breadcrumb / Footer / Modal
- 本 DS で先行定義 (3 件・travel 側は未着手): Select / FormLabel / Label・Tag
- レンタカー固有 (8 件): SearchForm / ResultCard / SecretPrice / Options / StorePicker / StepIndicator / Filter / Sort・Pagination
- ラベル・タグ (A〜H) の定義本体は [labels-tags.rental-car.md](labels-tags.rental-car.md)
- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- ボタンのバリアントは `primary` / `secondary` / `ghost` / `text` の 4 語で、4 語すべてに意匠と参照トークンを [components.md](components.md) §2 で与える。`campaign` は廃止 (accent は塗りボタン禁止)
- [決定] **主 CTA の個数制約は設けない** (判断 F-4・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。CTA の優先度は `primary` / `secondary` / `ghost` / `text` の強弱階層で表現する。繰り返し要素 (ResultCard 等) 内で各項目が `primary` を持つことを妨げない。旧「1 画面の主 CTA は `primary` 1 つに絞る」は本 DS では採らない。**適用判断が未取得 `🚧` であった状態は解消した**
- [決定] **PriceTag は背景文脈を明示的に選択する軸 (`tone`) を持つ** — `default` (明色面) / `inverse` (inverse 面) の 2 値。inverse 面では主要価格 `color.text.inverse`・補助価格/価格条件注記 `color.text.inverseMuted` を使用する (対応関係の正は [components.md](components.md))。**背景色を検知して自動反転する仕様・Component 内部の固定色だけで複数背景へ対応する仕様は採らない**。`tone` はバリアント語彙とは**別軸**であり語彙への追加ではない。実装 API 名 (prop 名) は未確定 `🚧`
- [決定] **Badge (単体) の切り出し境界**: 既に定義済みのラベル・タグ (A〜H = [labels-tags.rental-car.md](labels-tags.rental-car.md)・器 `label.*`・角丸 `radius.badge`・用途色 `color.label.*`) と、単体 Component として追加で必要になる範囲 (カード外での配置・サイズ段階・操作可能な場合の扱い) を分離する。**操作可能なバッジは badge ではなく action 系 Component として扱う** (角丸は `radius.action`)。Badge 単体 Component の仕様定義は本版に含めない
- 未着手: Tabs / Toast / Table / Accordion / Badge (単体) (follow-up #1)

### 7.1 Modal の表示形態 (form)

Modal に**表示形態 (form) 軸**を定義する。form は `drawer` (既定) / `sheet` / `popover` の 3 値をとる (判断 F-1・[governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。旧版が「拡張候補 (未承認)」として [components.md](components.md) の独立節に分離していた BottomSheet / Popover は、本節の `sheet` / `popover` として本文へ統合し、同節を廃止した (これに伴い `components.md` の §7 レスポンシブ → §6、§8 変更履歴 → §7 が繰り上がっている)。

- [決定] **実装基盤は drawer 単一を維持し、第 3 の Modal 実装基盤を導入しない**。`popover` は overlay の z 軸・backdrop・dismiss を drawer / sheet と共有する**同一基盤上の表示形態**であり、第 3 の実装基盤に当たらない。`popover` の配置方式 (基準要素への相対配置) が drawer / sheet と異なることは、実装基盤の相違としない
- [決定] form はバリアント語彙とは**別軸**であり語彙への追加ではない (PriceTag の `tone` と同じ扱い)
- [決定] **配置規則**:
  - `drawer` (既定): PC は右から 420px / SP は全幅・高さ 90vh まで (§6・[components.md](components.md))
  - `sheet`: 画面下端に貼り付き・全幅・上端 2 隅のみ角丸 (`radius.overlay` = 暫定 lg 16px)・ハンドル・行 48px・高さは内容なり
  - `popover`: 基準要素 (トリガー) を起点に配置し、下方に余地がなければ上方向へ反転する。**基準要素を必要とする** (drawer / sheet は不要)
- [決定] **切替規則**: `breakpoint.lg` (1024px) 未満は `sheet`、以上は `popover` を用いる。`drawer` は form の既定であり本切替規則の対象ではない (用途に応じて明示選択する)
- [決定] backdrop (`color.overlay.backdrop` = `🚧` 暫定 `rgba(0,0,0,0.45)`) は **3 形態すべてで使用する**。z 軸は既存 `elevation.overlay` (1200) / `elevation.modal` (1300) を用いる。**開閉遷移 (`motion.transition.*`) と影 (`shadow.*`) は既存 placeholder を参照するのみ**で値・`$status` を変更しない
- [決定] 表示形態は**明示的に選択する**。背景・文脈を検知して自動で形態を切り替える仕様は採らない。実装 API 名 (prop 名) は未確定 `🚧` (form の値・`popover` の基準要素指定の prop 名を含む)

**本節で定義しない事項**:

- a11y の `role` / `aria-modal` / フォーカストラップ / 復帰先・背面スクロールロック・閉じる操作の実装方式 — DS 層で決定しない (実装 Repository 側)
- 最小タップ領域 (44px) の spacing トークン — `spacing` に 44px の段が存在せず (段は 0/4/8/12/16/20/24/32/40/48/64px)、44px は WCAG 2.2 の 2.5.5 Target Size (Enhanced) 相当で §2.3 が最低ラインとする AA (2.5.8 = 24×24 CSS px) からは導けない。**トークンを追加せず、未確定事項として残す** (品質下限としての 44px そのものは §2.3 で維持する)
- `sheet` の最大高・`popover` の幅段階の実 px — 本 Repository で実査していない。未確定として残す
- 3 DS 横断の Modal 実装基盤 ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §1 Q9) — 本節は rental-car の表示形態を定めるものであり、横断の実装基盤を確定しない

## 8. ブランド・クリエイティブガイド

- [観察] 実用・価格訴求トーン (CP-01)。「卸価格」の直接的な価格優位訴求
- [事実] 特集アクセントは per-scheme (`#E4572E` / `#E0553C`) であり、主色と分離して管理する。**「点」専用** (ラベルの面・アイコン) で塗りボタンに使わない。accent を**面**として持つのは B 会員種別のみ、C カテゴリ・特集は**アイコン (点)** として持つ (§2.4「accent の帰属」)
- [事実] 写真選定基準は要確認 (BR-01/D-9) `🚧`
- [事実] 適用範囲は 2 段とする (詳細は §8.3・[labels-tags.rental-car.md](labels-tags.rental-car.md) H)
- [事実] 広告/SNS/メールは資産提供待ち (AD-02/follow-up #11) — 本版スコープ外

### 8.1 割引率の表記規則

**本節は「表示 (表記) 規則」のみを定義し、割引率の算出方法・端数処理・上限値といった事業・価格仕様は定義しない。** 算出規則と表示規則を混同しない。適用対象は A 割引率ラベル (`color.label.discount`・[labels-tags.rental-car.md](labels-tags.rental-car.md) A)。

#### 表示形式

- [決定] 基本形は `NN%OFF` (半角数字 + `%OFF`)。例: `5%OFF` / `20%OFF` / `35%OFF`。**数字部分を `%OFF` 部分より視覚的に強調する** (下記「数字の強調」)
- [決定] 原則として使用しない表記: `-NN%` (マイナス付与)・`20％引き` (全角パーセント)・`▲20%`。同一の意味へ複数表記を混在させない
- [決定] 「最大NN%OFF」等の条件付き表現は、対象範囲 (対象プラン・対象車種等) における最大値であり、かつ文脈で「最大」と判別可能な場合にのみ使用する。無条件の既定使用はしない
- [決定] マイナス記号は付さない。旧「符号」規則 (割引率であることを示すため数値の前に半角マイナスを付す) は本 DS では採らない
- [事実] 上記と異なる明示的な規則が Owner 決定またはブランドガイドラインに新たに存在する場合はそれを優先し根拠を記録する (上書き機構)

#### 数字の強調

- [決定] `NN%OFF` の**数字部分を `%OFF` 部分より視覚的に強調する**。強調は**サイズ**で行い、**数字部分は `%OFF` 部分より §3 の既存タイポグラフィスケールで 1 段上のサイズ段を用いる** (例: `%OFF` が `xs` 12px なら数字は `sm` 14px、`%OFF` が `sm` 14px なら数字は `md` 16px)。**新しいサイズ値 (primitive) は追加しない**
- [決定] 書体は数字・`%OFF` とも `font.price` (本文と同族 `700` + tabular-nums) を用いる。ウェイトによる強調は行わず、**サイズ段の差のみ**で強調する
- [事実] 実サイズ段の割当 (器の 2 サイズ = sm: `%OFF` 12px / 数字 14px、md: `%OFF` 14px / 数字 16px)・箱の高さ・余白は semantic の器トークン (`label.fontSize.*` / `label.numberSize.*` / `label.height.*` / `label.paddingInline.*`) が正

#### 桁

- [決定] 半角数字を使用する / 原則として整数表示 / 不要な先頭ゼロを付けない (`05%OFF` は不可) / 小数点以下を表示しない

#### 端数処理 (未確定)

- 🚧 **表示上の暫定案**: 小数点以下切り捨て
- ❓ **未確定事項**: 正式な算出式と端数処理
- **決定主体**: 価格・商品仕様の Owner
- [決定] DS は事業上の価格算出方法を新規決定しない。上記の暫定案を DS の正式規則として扱わない

#### 上限および異常値

割引ラベルを**表示しない**条件 (DS の表示規則として定義):

- [決定] 算出結果が `0%` 以下の場合
- [決定] 算出不能の場合
- [決定] 元価格が存在しない場合
- [決定] 販売価格が元価格以下でない場合 (= 値引きが成立しない場合)

DS では確定しない事項 (Owner判断事項):

- ❓ `100%` 以上となるデータの扱い
- ❓ 表示可能な上限値
- ❓ 「最大」「〜」等の条件付き表現を使用する条件
- [決定] 上限値・異常値処理が上流仕様に無い状態で、DS が任意の数値を決定しない

#### 表示内容の真実性 (表示成立条件)

- [決定] 割引率は、比較対象となる価格・対象条件・税条件・日数・車種等が**一致する場合にのみ**表示できる
- [決定] DS は価格計算ロジックを定義しない。上記は表示が成立するために必要な前提の記載である
- [決定] 根拠・対象・期間・基準が不明な場合は確定表現にしない
- [決定] 割引率は販促表現であり、車両・料金・条件等の Fact と区別できる表現とする

#### 割引率と値引額

- ❓ **未確定事項**: 割引率と値引額 (金額) の使い分け基準。値引額を表示する場合の通貨記号・桁区切り等の表記も未決
- [Owner判断事項] 使い分け基準の決定主体は価格・商品仕様の Owner および ブランド Owner
- [事実] **割引率等のコンテンツ表記規則の管理正本は本書 §8 系とする。独立文書 (`brand-content.md` 等) は新設しない** — 継承元である国内宿泊 (travel) が Task 009-45 ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §21) で独立文書の新設方向を**撤回**し §8 系へ集約する方向を確定しているため、撤回済みの方向を本 DS へ持ち込まない

### 8.2 予約条件の表示規則

予約条件 (決済手段・返金可否・ポイント付与) の表示規則。**色値もトークンも新設せず、既存色の割り当て規則のみ**を定める。適用は予約条件 (F) に限る ([labels-tags.rental-car.md](labels-tags.rental-car.md) F と同内容であり、本節は `design.md` 側に規則として持つ)。

1. [決定] 予約条件は**面を持たないテキストの行**で示し、意味ごとのスロットに固める (キャンセル条件 → 支払い → 特典)。バッジの器 (面あり) には乗せない
2. [決定] ラベルの文字色を **4 役**に割り当てる (既存トークンの定義は変えない):
   - **得** (無料キャンセル・ポイント付与等) = `color.scheme.main.base` (暫定・現行踏襲)
   - **損** (キャンセル不可・在庫僅少等) = `color.state.error`
   - **中立** (決済手段等) = `color.text.mutedStrong`
   - **操作** (キャンセル規定を見る等) = `color.text.link`
3. [決定] **色だけで伝えず、文言を必ず併記する**
4. [決定] アイコンは意味ごとに固定する (現地決済 = `yen-sign` / カード決済 = `credit-card` / 無料キャンセル = `circle-check` / キャンセル不可 = `circle-xmark` / ポイント付与 = `coins`)。**アイコンに意味色は当てない** (アイコンの色は文字色に従う)
5. [決定] 並びを固定する: **キャンセル条件 → カード決済 → 現地決済 → ポイント**
6. [決定] この行に車種クラス (D) や企画ラベル (C) を混ぜない
7. [決定] `color.state.error` の用途に「**利用者に不利な事実の明示**」を含める (E1 在庫僅少と共通・`color.label.stock` と同じ用途拡張)

得・損の判定基準 (適用は F の予約条件に限る):

- [決定] 問い 1: 利用者が**選べるか** → 選べる (支払い方法等) なら**中立**で判定終了
- [決定] 問い 2: 素の予約と比べ、①支出 ②取り消し・変更の自由 ③時間の拘束 ④人数・人選びの制限 の 4 軸のいずれかが**緩むなら得・厳しくなるなら損**

- [事実] 「得」= `color.scheme.main.base` は `color.text.link` (= 主色) と同値 (`#2C50C8`) であり、**リンクとの見分けは未解決** (暫定)。見分けの手だて (非リンク文脈・下線の有無・アイコン併用等) は Owner / 設計判断事項として残す (未確定事項の一覧)
- [事実] 本規則は既存トークン (`scheme.main.base` / `state.error` / `text.mutedStrong` / `text.link`) の範囲で成立し、新色値・新トークンを伴わない

### 8.3 クリエイティブへの DS 適用範囲

PR 帯・特集帯・支給バナー等のクリエイティブに対する DS の適用範囲を **2 段**に分ける ([labels-tags.rental-car.md](labels-tags.rental-car.md) H)。

- [決定] **適用** (トークンのみ・逸脱なし): UI 部品・カード・ラベル全般 (A〜G)。ヒーローと ResultCard の割引率もこちら (A の決定がそのまま適用)
- [決定] **適用外** (クリエイティブ): PR 帯・特集帯・企画のキービジュアル・支給バナー・テーマタイル。DS を**ガイドライン**として使う
- [決定] 適用外での扱い: 書体・文字サイズ・ウェイト・器の形 (角丸・余白・マージン)・傾きは、**必然性・デザイン上の制約・目的を示せば外せる** (規則ではなくガイドライン)。ただし「なんとなく」では外さない
- [決定] **カラーは厳守**: 基調となるカラーは例外なく守る (必然性を示しても外せない)。文字色・面色は基調カラーの範囲内で選ぶ
- [決定] 品質の下限 (適用外でも守る): コントラスト AA (支給画像内の文字を除く)・タップ領域 `44px`・代替テキスト・色だけで伝えない
- [決定] **グラデーションは審査対象**とする (一律禁止でも一律許可でもなく場合による)。使う側が用途と範囲を出して判断を仰ぐ。**適用側 (UI) に対しては現行の「グラデーションなし」がそのまま残る** (実装の縦グラデは廃止済 = [migration-map.md](migration-map.md))
- [決定] 運用: 新しい帯やバナーを作るときに**どちらの段かを先に宣言する**。**宣言がなければ適用とみなす**。適用外を選んだ場合はガイドラインを外れる項目ごとに理由を添える
- [事実] グラデーションの**審査基準の策定と審査主体の設置**は運用体制の問題として未着手である。本節は「審査対象とする」までを定め、審査基準・審査主体は本節に含めない (未確定事項の一覧)
- [事実] 非 UI クリエイティブへの適用範囲の例外を **Governance 横断ルール (3 サービス共通) として新設する方向**が [governance/owner-decisions.md](../../../governance/owner-decisions.md) §23 に記録されている (2026-08-05・受理と分類の工程)。同 §23 の「カラーもトークン指定外を許容」(ⓑ) と本節の「カラーは厳守」は**差分があり未調整**である。原則正本の置き場所 (Governance 横断 vs 本節) と当該差分の解消は §23 の設計承認プロセスの範囲であり、**本節は rental-car `design.md` への明文化に留める** (本節が Governance 横断ルールを先取りして確定するものではない)

## 9. Agent Prompt Guide

1. `semantic.rental-car.json` を読み、Semantic トークン名で指定 (HEX 直書き・primitive 直接参照は禁止)
2. [components.md](components.md) の固定フォーマットに従う。ラベル・タグは [labels-tags.rental-car.md](labels-tags.rental-car.md) を参照する
3. `$status=placeholder` は `$note` の follow-up 番号を確認し「`🚧` 暫定」を生成物に伝播させる
4. **ボタンと入力要素は pill (`radius.action`)**。4px の旧固有形状・グラデ・影を再現しない。非操作のラベルは `radius.badge` (4px) で、pill を使わない
4-1. 面 (背景) の上に文字を置くときは §2.4 の検証表で組み合わせを確認する。**表に無い組み合わせを検証済みとして扱わない**。リンクは §2.5 (文中は下線あり・hover で外さない・`opacity` を使わない)、未入力状態の文字色は §2.6、文書レベルの見出しは §3.1 (1024px 未満は段を 1 つ下げる) に従う
5. 禁止: 他サービスのトークン値の流用 (P1。インバウンドの blue `#064f9e` 等)・100選ゾーンの素材利用・会員ランク色 (階級表現。会員種別 2 値は [labels-tags.rental-car.md](labels-tags.rental-car.md) B で別途定義)
6. 禁止 (廃止値): 赤 `#9E2334` / `#9B2030` / `#9F1E30`・紺 `#283593`・link `#0050a0` と hover `#06f`・CTA 緑 `#43A047`・`$tocooBlue` `#2B4B65`・マスクのグレー板 `#7F7F7F`・`.cat-label` の分類色 `#060` / `#C90` と尾 `#8C4801`・5px 刻みユーティリティ・本文 15px / lh 1.4・Bootstrap 残骸 `#007BFF`。これらは [migration-map.md](migration-map.md) の左列 (実装の事実値) にのみ現れる
7. 迷ったら: `01_共通アセット/命名規則.md` §9 → `デザイン原則.md`

## 未確定事項の一覧 (`🚧`)

旧 Q1 / Q2 / Q3 / Q4 / Q8 は 2026-08-18 のオーナー判断により解消した。本版で残る未確定は次のとおりである。

| 論点 | 内容 | 次アクション |
| --- | --- | --- |
| accent 濃色段・サブスキーム (coral) 2 段の実色 | **primitive に段を追加済み** (Task 009-63) — `orange.100` `#F9CDBC` のみ bound、`orange.800` `#8A2E11`・`coral.100` `#F8CBC2`・`coral.800` `#8A2C18` は **🚧 仮色 placeholder**。B-1 の淡色面 + 濃色文字 (5.84:1) は概算であり成立検証は実色値確定後 | 実査 (§14 = 依頼元提出値の受領・作業担当者照合 + Web部責任者確認)。実色を発明しない |
| accent の帰属 | ✅ **確定** (Task 009-63・判断は [governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。accent を**面**として持つのは B 会員種別のみ、**C カテゴリ・特集はアイコン (点)** として持つ。C の面は白 (`color.label.category.surface`)。白系の面の上に置く場合のみ枠線 1px (`color.label.category.border` = 白面上 1.61:1・非テキスト 3:1 未達を明示) | — |
| A 割引率のコントラスト | 逆色面 + 白文字は main 2.78:1 / sub 2.15:1 で、**両スキームとも**通常テキスト 4.5:1 だけでなく大きなテキスト 3:1 も未達。**例外条項は §2.4「A 割引率ラベルに限る白文字の例外」として明文化済み** (Task 009-63)。**AA 未達を明示したうえでの許容であり適合宣言ではない** | 白文字 (例外) と b2 (accent 淡色面) のどちらを最終解とするかはオーナー判断 |
| C カテゴリ・特集ラベルのアイコンの字形とサイズ | ❓ 未定義。字形は C1 = `fa-bolt` / C2 = `fa-clock` を [labels-tags.rental-car.md](labels-tags.rental-car.md) が示すが、**サイズ**は `iconSize` の最小段が 16px で、器 sm (高さ `label.height.sm` 20px・文字 `label.fontSize.sm` 12px) に当てる値が本書・[components.md](components.md) のいずれにも無い。継承元の travel 側でも未定義 | 決定主体 = Web部責任者・チーフデザイナー |
| 未入力状態への `color.text.muted` 適用 | ✅ **確定** (Task 009-63 判断 C-5・§2.6。適用範囲は 2026-09-07 に UI 種別非限定へ変更)。`input` / `textarea` の `::placeholder`・Select の未選択値・その他の入力フィールドの未入力表示のすべてに `color.text.muted` (2.68:1・**AA 未達明示**) を用いる。プレースホルダ専用トークンは定義しない | — |
| フォーム入力の状態一式 | 🚧 実査待ち (follow-up #2)。§2.6 は**文字色のみ**を bound として確定させたものであり、枠色・背景色・必須表現・検証表示は未解決 | 実装実査 |
| 訪問済みリンク (`visited`) を色で区別する要否 | ❓ 未確定。既存 palette に visited 用の色値が無く primitive を追加しないため、現在は `color.text.link` を維持する決定のみ (§2.5) | オーナー判断 |
| standalone なリンクへ下線の既定を及ぼすかの区分 | ❓ 未判定。§2.5 が定めた**下線**の既定は文中リンクを対象とする (状態ごとの文字色と focus は対象を限定しないため standalone にも適用される)。カード全体リンク・ナビゲーション項目・パンくずの下線の扱いは判定していない | 設計判断 |
| `h5` / `h6` (いずれも 1rem) と本文 (1rem) の区別根拠 | ❓ 未判定。本文のウェイトが正本上不在 (`font.body` は family / size / lineHeight のみ) でウェイトによる区別が成立しない。行間差 (1.3 / 1.8) は折り返し時のみ視覚差となり、書体も同一スタック (§3.1)。1024px 未満では `h4` も 1rem となり同じ問題に含まれる | 設計判断 |
| 4 の倍数規則を見出し以外の `typography` 用途へ及ぼすか | ❓ 未判定 (Task 009-63 で見出しのみに限定して確定)。`typography.size` で 4 の倍数でないのは `sm` (14px) と `lg` (18px)。`sm` は `label.fontSize.md` / `label.numberSize.sm`、`lg` は `font.display.mdSize` (車種クラス名) が参照しており、及ぼす場合はこれらに波及する | 設計判断 |
| 文書レベルの見出し既定 (§3.1) を実装へ反映する範囲・順序・期限 | ❓ 未確定。本書は既定値のみを定義し反映計画を決定しない。実装 (japan ゾーン) の見出し実測値は本 Repository で実査していない | 実装側タスク |
| 画像・グラデーションを面 (背景) とする場合の文字色と scrim | ❓ 未定義。§2.4 の検証表は**単色面のみ**を対象とし、画像・グラデーション面のコントラスト評価方法を持たない | 設計判断 |
| Modal の form の a11y・`sheet` の最大高・`popover` の幅段階・実装 API 名 | ❓ 未定義 (§7.1)。a11y は DS 層で決定しない。最大高・幅段階の実 px は本 Repository で実査していない。最小タップ領域 44px の spacing トークンは追加しない | 実装実査 / 実装側タスク |
| クリエイティブのグラデーション審査基準・審査主体 | 🚧 未策定 (§8.3)。「審査対象とする」までが確定。審査基準の策定と審査主体の設置は運用体制の問題。[governance/owner-decisions.md](../../../governance/owner-decisions.md) §23 (Governance 横断) との原則正本の置き場所・「カラー厳守」vs §23ⓑ の差分も未調整 | §23 の設計承認プロセス |
| 割引率の算出式・端数処理・上限値 | ❓ 未確定 (§8.1)。DS の表示上の暫定案は「小数点以下切り捨て」(正式規則ではない)。決定主体 = 価格・商品仕様の Owner | オーナー判断 |
| PriceTag の `tone` の実装 API 名 (prop 名) | ❓ 未確定。DS は `default` / `inverse` の 2 値と色の対応関係のみ定義する (§7・[components.md](components.md)) | 実装側タスク |
| E2 満車・受付終了 | CTA の非活性へ集約する方向のみ確定。面色・文字色・高さ・文言は未定 | Button の disabled 定義が先 |
| ResultCard の実 px | 角丸・影・行高・列幅が未取得。`radius.card` は暫定 `md` | 実装実査 |
| 料金列の実ラベル | 6 列構造の文言が CSS から取得できず、責務名ベースの暫定 | テンプレート実査 |
| モーション実値 | 実装は 0.3s ease-in-out と 0.35s ease が混在。DS は 300ms ease を暫定 | follow-up #3 |
| シャドウ実値 | primitive に 3 段を暫定値で置くのみで用途 semantic は未定義。Component 仕様では段を指定しない | follow-up #13 (実値抽出後に用途トークンを設計) |
| ロゴ素材 | ToCoo! ロゴ・レンタカー各社ロゴが未提供。ワードマークと No Image で代用 | 素材提供後に差し替え。記憶からの再構築は禁止 |
| 写真選定基準 | 車両写真の比率・トリミング基準が未定義 | Assets レイヤー着手時 |
| サービス識別子 | `rental-car` は暫定。正式識別子 (`drc` / `japan` 等) は未決 | governance 確認事項 #8 |
| Filter の件数算出 | facet 型の絞り込みは実装に未確認。件数の算出仕様が未定義 | 要件定義 |
| Modal 実装基盤 | 3 DS 横断の基盤は未決 (§1 Q9)。**rental-car の表示形態 (form) は §7.1 で確定した**が、これは横断の実装基盤を確定するものではない | オーナー判断 (3 DS 横断) |
| 主 CTA の個数制約 | ✅ **確定** (Task 009-63 判断 F-4・§7)。**個数制約を設けない**ことを rental-car の判断として確定した。「適用判断は未取得 `🚧`」の状態は解消した | — |
| BottomSheet / Popover の採否 | ✅ **確定** (Task 009-63 判断 F-1・§7.1)。Modal の**表示形態 (form) `sheet` / `popover`** として本文へ統合し正式仕様とした。実装基盤は drawer 単一を維持し第 3 の実装基盤を導入しない。**3 DS 横断の Modal 実装基盤 (§1 Q9) は引き続き未決** | — |
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
| 2026-09-07 | Task 009-63: 国内宿泊 (travel) の最新版 (Task 009-58〜009-62) の定義体系を適用 ([Issue #170](https://github.com/tocoo/coocom-design-system/issues/170)・記録 = [governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。**節の新設**: §2.4 面 (背景) と文字色の組み合わせ規則 (用語の定義・検証した組み合わせの表 18 行・campaign accent 面の条件と代替規則・scheme inverse 面・**A 割引率ラベルに限る白文字の例外**・accent の帰属)、§2.5 リンクの装飾と状態、§2.6 プレースホルダの文字色、§3.1 文書レベルの見出しスケール (h1〜h6・幅 2 列・4 の倍数規則)、§7.1 Modal の表示形態 (form = drawer / sheet / popover)、§8.1 割引率の表記規則、§8.2 予約条件の表示規則、§8.3 クリエイティブへの DS 適用範囲。**既存節の是正**: §2.2 用途表に新規 semantic 12 行を追加しテキスト用途別名の区別を明記／§2.3 の「例外条項は未明文化」を解消／§3 の「見出しは h1〜h3 の 3 段のみ・h4 以下は未定義」を 6 段へ、車種クラス名の**要素固定**の書き方を**役割ベース**へ是正 (`h3Size` が 24px へ変わり `font.display.mdSize` 18px との同値衝突が消えたため)／§5 の入力角丸を `radius.input` (4px) から `radius.action` (pill) へ統一し用途トークンを 5 系統から 4 系統へ／§6 のオーバーレイを form 3 値へ／§7 に主 CTA 個数制約の不設置・PriceTag の `tone` 軸・Badge (単体) の切り出し境界を追加／§9 に §2.4〜§3.1 への参照を追加／未確定事項の一覧を全面更新 (解決 4 件・新規 11 件)。**トークン**: semantic 40 件追加・`radius.input` 1 件削除・`font.heading.h3Size` の参照先を `{typography.size.lg}` (18px) から `{typography.size.2xl}` (24px) へ変更、primitive 4 件追加 (`orange.100` / `orange.800` / `coral.100` / `coral.800`。`orange.100` のみ bound・他 3 段は 🚧 仮色)。**不変**: スキームの値・ブレークポイント・スペーシング・z 軸・コンテナ幅・`font.display.*` の値と参照先・`color.mask.secret`・§1 概要・§2.1 スキーム表・§4・migration-map.md。**節番号**: 既存 §2.1〜§2.3 は保持し新設分を §2.4〜§2.6 とした (travel との対応は §2 のみ 1 対 1 でない) | Claude Code |
| 2026-09-07 | Task 009-63R の記述是正: PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) コードレビュー ([issuecomment-5565532746](https://github.com/tocoo/coocom-design-system/pull/171#issuecomment-5565532746)) の指摘に対応。①§2.2・§2.4 の `color.surface.muted` × `color.tag.neutral.text` のコントラスト値を 5.68:1 から実測値 **9.22:1** へ是正 (誤値・本 Task で新規に混入)。②未入力状態の文字色を **UI の種別で限定せず `color.text.muted` に統一する** Web部責任者判断 (2026-09-07・§29 判断 C-5 の適用範囲変更) を反映し、§2.6 を「プレースホルダの文字色」から「未入力状態の文字色」へ改題・全面改訂、§2.2 の `color.text.placeholder` 行と用途別名の列挙から同トークンを削除、未確定事項の一覧の該当行を書き換えた。これに伴い `semantic.rental-car.json` の `color.text.placeholder` の追加を取り下げた (semantic 追加 40 件 → **39 件**)。③未確定事項の一覧の A 割引率のコントラスト行を「sub は 3:1 も未達」から「**両スキームとも** 3:1 も未達」へ是正 (main 2.78:1 も 3:1 に達しない)。**不変**: スキームの値・ブレークポイント・スペーシング・z 軸・§2.4 の例外条項・§3.1 の見出し表・§7.1 Modal の form・§8 ブランド・§9 Agent Prompt Guide | Claude Code |
