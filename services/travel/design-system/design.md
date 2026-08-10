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
- [観察] コピートーンは実用・価格訴求。CTA 文言例「プラン選択へ」。**詳細の委任先として記載されていた `brand-content.md` は Repository 内に存在しない** (参照切れ = [README.md](README.md) §8・§16)。現時点で確認できるブランド／コンテンツ規則の記載箇所は §8
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
| `color.text.mutedStrong` | gray.700 | `#616161` | bound (白背景 ≈6.2:1) |
| `color.text.muted` | gray.600 | `#9e9e9e` | bound (白背景 ≈2.7:1) |
| `color.text.inverse` (inverse 面の主要文字) | white | `#ffffff` | bound (inverse 面 #212121 上 ≈16.10:1) |
| `color.text.inverseMuted` (inverse 面の補助情報) | gray.600 | `#9e9e9e` | bound (inverse 面 #212121 上 ≈6.01:1・明色面には使用しない) |
| `color.text.onAccent` (campaign accent 面の文字) | white | `#ffffff` | bound (accent 面 #E4572E 上 ≈3.68:1・**§2.1 の (a) (b) を満たす文字のみ**) |
| `color.text.placeholder` (入力欄のプレースホルダ) | gray.700 | `#616161` | bound (白背景 ≈6.2:1・§2.3) |
| `color.text.link` | scheme.main.base (副色=sub.base) | `#2C50C8` / `#4845D4` | bound (TVL-0011・リンク=主色。TVL-0005 解決) |
| `color.text.linkHover` | scheme.main.hover (副色=sub.hover) | `#2340A6` / `#3936B0` | bound (§2.2) |
| `color.text.linkActive` | scheme.main.pressed (副色=sub.pressed) | `#1B3488` / `#2C2A8C` | bound (§2.2) |
| `color.surface.default/subtle/muted` | white / gray.50 / 100 | `#fff` / `#f9f9f9` / `#f5f5f5` | bound |
| `color.border.subtle/default/strong` | gray.300/400/500 | `#e0e0e0` / `#ccc` / `#bcbcbc` | bound |
| `color.state.success` | scheme.main.base (副色=sub.base) | `#2C50C8` / `#4845D4` | bound (TVL-0011・成功=各パレット主色。専用緑廃止) |
| `color.state.error` | scheme.main.error (副色=sub.error) | `#D23A3A` / `#D2405F` | bound (TVL-0011・per-scheme・正式採用時共通化) |
| `color.accent.campaign` | scheme.main.accent (副色=sub.accent) | `#E4572E` / `#E0553C` | bound (TVL-0011・per-scheme・正式採用時共通化) |
| `color.focus.ring` | brand.primary | `#2C50C8` | bound (白背景 ≈6.8:1) |
| `color.icon.rating` | scheme.main.inverse (副色=sub.inverse) | `#C8912C` / `#C8B12C` | bound (TVL-0011・評価色=各パレット逆色) |
| `color.overlay.backdrop` (Modal backdrop) | palette.blackAlpha.45 | `rgba(0,0,0,0.45)` | 🚧 placeholder (Modal / Overlay の backdrop・form 3形態共通・§7。暫定値=実装バンドル観測値を暫定参照・実査待ち) |

- [事実] 品質基準: WCAG 2.2 AA を最低ラインとし DS には違反値を入れない (要求仕様 R9)。本文 #424242 ≈10.0:1 (AAA 7:1 も満たす)・主色 royal #2C50C8 ≈6.8:1・副色 indigo #4845D4 ≈6.8:1 いずれも AA 適合 (主色・副色は AAA 7:1 未達)
- [事実] テキスト色は 4 段構成 (`strong` #212121 / `body` #424242 / `mutedStrong` #616161 / `muted` #9e9e9e)。判読性を必要とする補助情報 — 補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件 — は `color.text.mutedStrong` (白背景 ≈6.2:1) を使用する。`color.text.muted` (白背景 ≈2.7:1) は通常テキストに求められる 4.5:1 に達しないため、判読性を要する情報には用いない。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (適用規格・達成レベルは未確定)
- [事実] 上記 4 段は文字色の**濃度段**であり、特定の用途に固定した別名は 4 段とは別に定義する。`color.text.link` / `linkHover` / `linkActive` (リンク = §2.2)・`color.text.placeholder` (入力欄のプレースホルダ = §2.3)・`color.text.inverse` / `inverseMuted` (inverse 面 = §2.1)・`color.text.onAccent` (campaign accent 面 = §2.1) がこれに該当する。用途別名が同じ primitive を参照する場合でも、一方の値の変更が他方へ自動的に及ぶ設計にはしない

### 2.1 面 (背景) と文字色の組み合わせ規則

色を**面 (背景)** として使う場合、許可される文字色と文字サイズ・ウェイトの条件は面ごとに異なる。

#### 用語の定義 (本節で用いる条件)

- **ウェイトの境界**: 「**bold**」は `typography.fontWeight.bold` (`700`) 以上を指す (`black` `900` を含む)。「**通常ウェイト**」は `700` 未満を指す (`regular` `400`・`medium` `500`・§3 の明朝 Display で用いる `600` 相当を含む)。この 2 語で全ウェイトを排他的に二分する
- **条件 (a)**: `24px` 以上 (**ウェイトを問わない**) — WCAG 2.2 の大きなテキスト
- **条件 (b)**: `20px` 以上かつ **bold** (`700` 以上) — WCAG 2.2 上の bold 側の下限は約 `18.7px` だが、実運用上の誤差・フォント差を避けるため DS では `20px` を下限とする
- **(a) (b) のいずれも満たさない文字**: **(i) `20px` 未満のすべて** および **(ii) `20px` 以上 `24px` 未満かつ通常ウェイト** — (a) (b) (i) (ii) で全サイズ・全ウェイトを網羅する
- **「大きなテキスト相当」**: (a) (b) のいずれかを満たす文字を指す — **サイズ・ウェイトの条件**。**WCAG 2.2 の大きなテキストより DS の範囲は狭い** (bold 側の下限を約 `18.7px` から `20px` へ引き上げているため)。WCAG の語をそのまま適用しない
- **「大きなテキスト基準」**: WCAG 2.2 が大きなテキストに求める**コントラスト比 `3:1`** を指す — 下表「大きなテキスト (3:1)」列の判定。**コントラスト比の基準であり、サイズ・ウェイトの条件ではない**
- 上記 2 語は別概念であり混用しない。**コントラスト比が「大きなテキスト基準」を満たすことは、その文字を使用してよいことを意味しない** (使用可否はサイズ・ウェイトの条件 = 「大きなテキスト相当」で決まる)

#### 検証した組み合わせ

下表は本書で検証した組み合わせであり、**表に無い組み合わせを検証済みとして扱わない**。本表は**単色面のみ**を対象とし、画像・グラデーションを面 (背景) とする場合の文字色とコントラスト確保の方法 (scrim の要否・評価方法) は本表の対象外で未定義である (依頼 E-1・未確定事項の一覧)。

| 面 (背景) | 文字 | 概算 | 通常テキスト (4.5:1) | 大きなテキスト (3:1) | 扱い |
| --- | --- | ---: | --- | --- | --- |
| `color.accent.campaign` `#E4572E` | `color.text.onAccent` `#FFFFFF` | 3.68:1 | 未達 | 達成 | **条件付きで許可** (§2.1 の (a) (b) を満たす文字のみ) |
| `color.accent.campaign` `#E4572E` | `color.text.strong` `#212121` | 4.37:1 | 未達 | 達成 | **規則としては使用しない** (面上の文字色は `color.text.onAccent` に限定。本行は参考値) |
| `color.surface.inverse` `#212121` | `color.text.inverse` `#FFFFFF` | 16.10:1 | 達成 | 達成 | 許可 |
| `color.surface.inverse` `#212121` | `color.text.inverseMuted` `#9E9E9E` | 6.01:1 | 達成 | 達成 | 許可 (補助情報) |
| `color.scheme.main.inverse` `#C8912C` | `#FFFFFF` | 2.78:1 | 未達 | 未達 | **禁止** |
| `color.scheme.main.inverse` `#C8912C` | `color.text.strong` `#212121` | 5.78:1 | 達成 | 達成 | 許可 |
| `color.scheme.sub.inverse` `#C8B12C` | `#FFFFFF` | 2.15:1 | 未達 | 未達 | **禁止** |
| `color.scheme.sub.inverse` `#C8B12C` | `color.text.strong` `#212121` | 7.50:1 | 達成 | 達成 | 許可 |
| `color.surface.default` `#FFFFFF` | `color.accent.campaign` `#E4572E` (文字色として) | 3.68:1 | 未達 | 達成 | 条件付き (§2.1 の (a) (b) を満たす文字のみ) |
| `color.surface.subtle` `#F9F9F9` | `color.accent.campaign` `#E4572E` (文字色として) | 3.50:1 | 未達 | 達成 | 条件付き (§2.1 の (a) (b) を満たす文字のみ) |
| `color.surface.muted` `#F5F5F5` | `color.accent.campaign` `#E4572E` (文字色として) | 3.38:1 | 未達 | 達成 | 条件付き (§2.1 の (a) (b) を満たす文字のみ) |

#### campaign accent 面上の文字

- [事実] `color.accent.campaign` (`#E4572E`) 上では、白文字 3.68:1・濃色文字 `#212121` 4.37:1 のいずれも通常テキストの 4.5:1 に達しない。**既存色の範囲では、campaign accent 面上で任意サイズの通常テキストを成立させる文字色は存在しない**
- [決定] campaign accent 面上の文字色は **`color.text.onAccent` のみ**を使用する。`color.text.strong` (`#212121`・4.37:1) は大きなテキスト基準は満たすが、面上の文字色を 1 つに定めるため**規則としては使用しない** (表の値は参考)
- [決定] campaign accent を**面として使用できるのは、§2.1 の条件 (a) (b) のいずれかを満たす文字に限る** ((a) `24px` 以上・ウェイトを問わない／(b) `20px` 以上かつ bold)
- [決定] **(a) (b) のいずれも満たさない文字 ((i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト) には面として使用しない**。ウェイトを上げれば自動的に適合するという定義にはしない (`20px` 未満は bold でも不可)
- [決定] `color.text.onAccent` の存在は「白であれば常にアクセシブル」を意味しない。背景色と文字サイズ・ウェイトの確認を省略しない

#### campaign accent を面として使用できない場合の代替規則

§2.1 の (a) (b) のいずれも満たさない文字 — すなわち (i) `20px` 未満のすべて、および (ii) `20px` 以上 `24px` 未満かつ通常ウェイト — には次を用いる。

1. **[既定] neutral dark 面へ切り替える** — 背景 `color.surface.inverse` (`#212121`) + 文字 `color.text.inverse` (16.10:1)。**既存トークンの範囲で通常テキスト基準 4.5:1 を満たす唯一の面**であり、(i) (ii) に該当する割引率ラベルの既定とする
2. accent を**非テキスト要素**に限定する — 境界色・アイコン・点的装飾 (非テキスト UI 要素の 3:1 は満たす)。**accent を文字色として明色面に置く方法は、この場合の代替にならない** (`default` 3.68:1 / `subtle` 3.50:1 / `muted` 3.38:1 はいずれも通常テキスト 4.5:1 に達しない)

(a) (b) を満たす文字については、accent 面を用いない次の構成も選べる。

3. accent を**文字色**として明色面に置く — `color.surface.default` 3.68:1 / `color.surface.subtle` 3.50:1 / `color.surface.muted` 3.38:1。いずれも大きなテキスト基準のみを満たすため、**(a) (b) を満たす文字に限る**

- [事実] 上記はいずれも既存 palette の組み合わせで成立するため、代替背景色の primitive を新設していない
- [事実] 依頼元 (2026-08-03) の依頼 B に対し、Web部責任者は小サイズ (例 12px) のバッジについて **accent 淡色面 (淡色面 + 濃色文字) を新設する方向 (b2)** を選択した (正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §13)。ただし accent 淡色段 (50 / 100 相当。現行 palette に不在) の**実色値は未取得**であり、本書では新規 primitive・semantic を追加していない。実色値の取得後に「淡色面 + `color.text.strong` (濃色文字) のコントラスト 4.5:1 以上」を検証して確定する (別作業)。実色値の取得までは現行の代替規則が有効であり、(i) に該当する 12px のバッジは既定 (neutral dark 面 `color.surface.inverse` + `color.text.inverse`) を用い、campaign accent を面として使用しない
- [決定] 禁止: campaign accent 面上に **(a) (b) を満たさない白文字 ((i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト)** を置く / `onAccent` の存在だけを理由にコントラスト確認を省略する / AA 未達を「ブランド表現」で自動的に許容する / 文字へ縁取り・影を付けることでコントラスト不足を解決したものとして扱う

#### scheme inverse 色を面として使用する場合

- [事実] 白文字は `color.scheme.main.inverse` (`#C8912C`) 上で 2.78:1、`color.scheme.sub.inverse` (`#C8B12C`) 上で 2.15:1 であり、**両スキームとも**通常テキスト 4.5:1 だけでなく大きなテキスト 3:1 も満たさない
- [決定] 両スキームの逆色を面として使用する場合の文字色は `color.text.strong` (`#212121`) を原則とする (main `#C8912C` 上 5.78:1・sub `#C8B12C` 上 7.50:1)。白文字は正式な通常利用として許可しない
- [事実] semantic alias (`color.text.onSchemeInverse` 等) は追加していない。`color.scheme.*.inverse` の用途は、評価色 (`color.icon.rating` = 文字/アイコン色) に加え、**割引ラベル背景としての面用途**を持つ (面用途は c1 = Web部責任者判断 2026-08-03 で定義。正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §13)。面用途に対応する専用の semantic 用途トークンは追加せず、`color.scheme.*.inverse` を面として参照する (新しい色値・alias は追加していない)
- [決定] `color.scheme.*.inverse` を面として使用する場合の文字色は `color.text.strong` に固定する (c1・Web部責任者判断 2026-08-03。main `#C8912C` 上 5.78:1・sub `#C8B12C` 上 7.50:1)。**白文字は使用しない** (main 2.78:1・sub 2.15:1 で通常・大きなテキストのいずれも未達)。依頼元が根拠とする `#C8912C` 面上の白文字運用は本決定に反する例外運用であり、DS 規則としては採らない。「Owner 指示」を理由に AA 適合済みとして扱わない (§2.1 冒頭の品質基準)
- [事実] 副色スキームの `#C8B12C` 上のコントラスト比も本書で検証済み (白 2.15:1・`#212121` 7.50:1)。上表には `main` と `sub` の行を個別に記載する。**2 スキームは値が異なるため、値やコントラスト比を伴う記述でワイルドカード表記を用いて 1 行に束ねない**

#### 評価色と販促面色の用途境界

- [事実] `{color.scheme.main.inverse}` / `{color.scheme.sub.inverse}` を `$value` で参照する semantic トークンは `color.icon.rating` (ReviewStars 星の色) の 1 件のみである (`semantic.travel.json` 全文検索で確認)。`color.brand.*` / `color.state.*` / `color.accent.campaign` はいずれも scheme の `base` / `error` / `accent` を参照し、`inverse` は参照していない。`color.scheme.sub.inverse` を参照する semantic トークンは存在しない (副色文脈での適用は per-scheme の記述として保持されている)
- [決定] 評価色 (`color.icon.rating`)・割引/販促色 (`color.accent.campaign`)・ブランド補色 (`color.scheme.*.inverse`)・状態色 (`color.state.*`) を同一用途へ統合しない (上流 `../service-design/content-principles.md` CTP-010「事実・条件・サービス上の判断・販促表現を混同しない」と整合)
- [決定] 評価用途は既存定義を維持する。**`color.icon.rating` トークンを割引ラベル・販促面・状態色へ流用しない** (面用途では逆色を `color.icon.rating` 経由で参照しない)
- [決定] **`color.scheme.*.inverse` を割引ラベル背景 (面) として使用できる** (c1・Web部責任者判断 2026-08-03、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §13)。文字色は `color.text.strong` に固定する (main `#C8912C` 上 5.78:1・sub `#C8B12C` 上 7.50:1)。白文字は使用しない (2.78:1 / 2.15:1)。逆色の値は評価色 (文字/アイコン色) と割引ラベル背景 (面 + `color.text.strong`) の 2 用途に用いるが、**用途は分離**し `color.icon.rating` トークンを面として再束縛しない。割引/販促の面は引き続き `color.accent.campaign` も選べる (§2.1 の代替規則)。campaign accent との役割は明確に分離する (割引/販促 = `color.accent.campaign` または scheme 逆色面、評価 = scheme 逆色を `color.icon.rating` として使用)

### 2.2 リンクの装飾と状態

リンクの**色**は `color.text.link` (= 各スキームの主色) で確定済み (TVL-0011・Owner決定 [m0046]。TVL-0005 解決)。本節は**色以外の装飾 (下線) と、状態 (hover / visited / active / focus) ごとの取り扱い**を定める。`color.text.link` の値・参照先は本節で変更しない。状態語そのものを新設するものではない (状態の固定リストは `components.md` 共通事項が正・追加は ADR 必須)。`visited` について本節が定めるのは「専用色を設けない = 既定と同じ」という取り扱いであり、固定リストへの追加ではない。

文字色の列は対象を限定しない (standalone なリンクを含む)。下線の列は**文中リンクのみ**を対象とする。

| 状態 | 文字色 (対象を限定しない) | 下線 (文中リンクのみ) |
| --- | --- | --- |
| 既定 | `color.text.link` (`#2C50C8`) | あり |
| hover | `color.text.linkHover` (`scheme.main.hover` `#2340A6`) | あり (維持) |
| active (押下中) | `color.text.linkActive` (`scheme.main.pressed` `#1B3488`) | あり (維持) |
| visited | `color.text.link` (既定と同じ・専用色を設けない) | 既定と同じ |
| focus | `color.text.link` (既定と同じ) | 既定と同じ + `color.focus.ring` の `outline` |

- [決定] 本文・説明文などの**文中リンクには下線を付す**。リンクであることを色だけで伝えない。**下線を外す既定は置かない**
- [決定] hover は**下線を維持したまま文字色を `color.text.linkHover` へ変更する**。hover で下線を外さない (下線の消失はリンクでなくなったように読める)
- [決定] active (押下中) は `color.text.linkActive` を使用する
- [決定] visited に**専用色を設けない**。訪問済みリンクは `color.text.link` を維持する。理由: 既存 palette に visited 用の色値が無く、本書では新しい色値 (primitive) を追加しないため。visited を色で区別する要否は Owner判断事項として未確定事項へ残す
- [決定] focus は Component 共通の `color.focus.ring` による `outline` を用いる (`components.md` 共通事項)。hover の色変更で focus 表現を代替しない
- [決定] リンクの状態表現に `opacity` を用いない。`opacity` は色トークンで表現できず、状態の識別が色・下線・不透明度へ分散する。`components.md` 共通事項は「**全 Component の** hover は `opacity` 変化 (≈0.85) を暫定参照とし `🚧 暫定` を付す」と定めているが、**リンクの hover は本節が定める色変更 (`color.text.linkHover`) を用い、同暫定参照の対象外とする** (同共通事項にリンクを対象外とする除外を置いている)
- [事実] 実装側 (`webroot/assets_s/css/common.css`) は次の宣言を持つ (実装 Repository `tocoo/tocoo_travel` の確認時点)。**いずれも DS 規則として採らない**
  - `a,a:hover,button,button:hover{color:#283593;transition:.5s ease}` — 旧主色 `#283593` を `a` と `button` へ同一セレクタで与えている。`#283593` は TVL-0010 以前の旧主色であり `color.text.link` はこれへ追随しない。リンクの規則とボタンの規則が分離されていない
  - `a:hover,button:hover{opacity:.75;text-decoration:none}` — hover を `opacity` で表し下線を解除している
  - `a:active,a:focus,a:visited,button:active,button:focus,button:visited{outline:none!important;text-decoration:none}` — 本節が下線を維持すると定めた `active` / `visited` で下線を解除し、`focus` の `outline` を `!important` 付きで無効化している。**とくに `outline: none !important` は本節の focus の決定と直接衝突し、特異度と `!important` の面で base 層からの `outline` 供給を妨げる**
- [注意] 同ファイルは Bootstrap v4.6.2 を含み、`a{color:#007bff;text-decoration:none}` / `a:hover{color:#0056b3;text-decoration:underline}` が上記と併存する。同一要素に対して複数の宣言が重なっているため、**本書は同ファイルの計算値 (実際に適用される値) を実測として扱わない**。上記は宣言の存在を記録したものである
- [注意] 本節が定める**下線の既定は文中リンクを対象とする**。カード全体リンク・ナビゲーション項目・パンくずなど、領域とレイアウトでリンクであることが成立する standalone なリンクへ下線の既定を及ぼすかは未判定 (未確定事項の一覧に起票)。**状態ごとの文字色 (hover / active / visited) と focus の取り扱いは対象を文中リンクに限定しない**ため、standalone なリンクにも適用される

### 2.3 プレースホルダの文字色

- [決定] 入力欄のプレースホルダ (`input` / `textarea` の `::placeholder`、および選択前の `option` に相当する表示) の文字色は `color.text.placeholder` (`gray.700` `#616161`・白背景 ≈6.2:1) を使用する
- [決定] `color.text.muted` (`#9e9e9e`・白背景 ≈2.7:1) を**プレースホルダへ流用しない**。プレースホルダは入力補助として読まれる文字であり判読性を要するため、通常テキストに求められる 4.5:1 に達しない値を用いない (§2 のテキスト色規則と同じ扱い)
- [決定] `color.text.mutedStrong` と同じ primitive (`gray.700`) を参照するが、**別の用途トークンとして定義する**。判読性を要する補助情報 (補助価格・価格条件注記等) と入力補助テキストは用途が異なり、一方の値を変えたときに他方が追随しない形にする。用途ベース命名の原則 (`semantic.travel.json` `$description`) に従う。**新しい色値 (primitive) は追加していない**
- [事実] 実装側 (`common.css`) は `input::placeholder,option,textarea::placeholder{color:#9e9e9e;font-family:Roboto,sans-serif;font-size:14px;font-weight:400}` を持つ (実装 Repository `tocoo/tocoo_travel` の確認時点)。`#9e9e9e` と同値の semantic (`color.text.muted`) は存在するが、上記の理由により**本書はこの色を正としない**。同宣言の `Roboto` は §3 で廃止された旧欧文フェイスであり、本節は文字色のみを定義し書体・サイズ・ウェイトを定義しない
- [決定] プレースホルダと入力済みテキスト (`color.text.body` `#424242`) の判別を色の差のみに依存させない。入力済みかどうかの識別は実際の文字列の有無で成立する
- [決定] プレースホルダを必須項目・ラベル・エラーメッセージ・入力形式の説明の代替として用いない
- 🚧 プレースホルダを含むフォーム入力の状態一式 (枠色・背景色・必須表現・検証表示) は実査待ち (`follow-up #2`)。本節は**文字色のみ**を定義する
- [注意] 本節は `follow-up #2` の範囲のうち文字色のみを `bound` として確定させたものであり、`follow-up #2` 全体を解決済みとして扱わない。この部分確定が [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §14 (実査待ちの項目の取り扱い) に該当するかは本書では判定しない (未確定事項の一覧に起票)

## 3. タイポグラフィ

root 16px・**rem 基準** (TVL-0001)。2 書体構成 = 明朝 (表現) + ゴシック (機能)。タイポグラフィ設計方針 (共有 dc) 2026-07-10 の決定を反映。

| 用途 | 値 | 状態 |
| --- | --- | --- |
| 本文・UI | LINE Seed JP / 1rem / lh 1.8 | **bound (Q1)** |
| 見出し (文書レベル h1〜h6) | LINE Seed JP 700 / h1 2.5rem〜h6 1rem / lh 1.3 | **bound (§3.1)** |
| 見出し (一覧・カード) | LINE Seed JP 700 / h2 2rem (= 文書レベル h2 と同値・同一トークン) | **bound (Q2)** |
| Display・Hero・詳細施設名 | Noto Serif JP (明朝) 500–600 | **bound (Q8)** |
| 欧文 | LINE Seed JP に統合 (旧 Roboto 廃止) | bound |
| 数字 (価格) | LINE Seed JP 700・tabular-nums (旧 Barlow 900 廃止) | **bound (Q3)** |

- サイズスケール: xs 0.75 / sm 0.875 / md 1 / lg 1.125 / xl 1.25 / 2xl 1.5 / 3xl 2 / 4xl 2.5 / display-lg 3rem (48px・Q4)
- 行間: tight 1.3 (見出し = §3.1) / normal 1.5 / relaxed 1.8 (本文)
- [注意] 実装移行時に px→rem の書き換えが発生する (TVL-0001 Consequences)
- [観察] 特集頁の見出しフォント不一致・壊れた font stack は新規制作で再生産しない

### 3.1 文書レベルの見出しスケール (h1〜h6)

Component に属さない**文書レベルの見出し** (`h1`〜`h6` そのもの) に適用する既定値を定義する。本節が定めるのは `h1`〜`h6` の各要素に当てる既定値 (サイズ・太さ・行間・書体) のみであり、**どの画面のどのコンテンツを `h1` / `h2` とするかという画面別の見出し階層・semantic role の割当は定めない** (画面別情報構造は Screen Requirements 側の課題 = [alignment-blocking-facts-resolution-plan.md](alignment-blocking-facts-resolution-plan.md) §8J.4)。本節と同 §8J.4 の分類との関係は未確定事項の一覧に起票している。

| 要素 | サイズ (semantic) | 参照先 | 値 | 太さ | 行間 |
| --- | --- | --- | --- | ---: | ---: |
| `h1` | `font.heading.h1Size` | `typography.size.4xl` | 2.5rem (40px相当) | 700 | 1.3 |
| `h2` | `font.heading.h2Size` | `typography.size.3xl` | 2rem (32px相当) | 700 | 1.3 |
| `h3` | `font.heading.h3Size` | `typography.size.2xl` | 1.5rem (24px相当) | 700 | 1.3 |
| `h4` | `font.heading.h4Size` | `typography.size.xl` | 1.25rem (20px相当) | 700 | 1.3 |
| `h5` | `font.heading.h5Size` | `typography.size.lg` | 1.125rem (18px相当) | 700 | 1.3 |
| `h6` | `font.heading.h6Size` | `typography.size.md` | 1rem (16px相当) | 700 | 1.3 |

- [決定] 書体は `font.heading.family` (LINE Seed JP・ゴシック) を文書レベルの既定とする。明朝 (`font.display.family`) は Display・Hero・特集・詳細施設名で**明示的に選択する**書体であり、文書レベルの見出しの既定ではない (§3)
- [決定] 太さは `font.heading.weight` (`typography.fontWeight.bold` = 700) を h1〜h6 共通の既定とする
- [決定] 行間は `font.heading.lineHeight` (`typography.lineHeight.tight` = 1.3) を h1〜h6 共通の既定とする。`relaxed` (1.8) は本文の値であり見出しへ適用しない
- [決定] **文書レベルの見出しと Component の見出しは同一トークン群 (`font.heading.*`) を共用する**。`font.heading.h2Size` は従来「一覧・カード見出し h2 = 2rem (実測)」として bound 済みであり本節の h2 と同値であるため、文書レベル用の別系統を設けない。Component 側で文書レベルの既定から外れる値が必要な場合は当該 Component 仕様に**明示的に**記載する (暗黙の上書きを認めない)
- [決定] **新しいサイズ値・行間値・ウェイト値 (primitive) は追加しない**。h1〜h6 はいずれも既存スケール (`4xl` / `3xl` / `2xl` / `xl` / `lg` / `md`) への割当である
- [事実] `h6` は本文と同サイズ (1rem) となる。本文との差はウェイトと行間だが、**本文のウェイトは正本上定義されていない** (`font.body` は `family` / `size` / `lineHeight` の 3 トークンのみで `weight` を持たず、§3 の表の本文行にもウェイトの記載がない)。したがって**ウェイトによる区別を本書の根拠としない**。行間の差 (見出し 1.3 / 本文 `font.body.lineHeight` = `relaxed` 1.8) は値としては定義済みだが、折り返しが生じる場合にのみ視覚差となる。書体も `typography.fontFamily.heading` と `sans` はいずれも同じフォントスタックを先頭に持つため差がない。`h6` と本文の区別根拠が不足していることは未確定事項の一覧に起票している
- [決定] 見出しサイズを UA 既定に委ねない。理由は次のとおり
  - HTML 標準の Rendering セクションが定める見出しサイズは `em` 基準 (親の `font-size` に対する相対値) であり、親の `font-size` が異なる文脈で実寸が変わる。§3 が定める **rem 基準 (TVL-0001) と整合しない**
  - 同セクションには `:is(article, aside, nav, section)` の入れ子段数に応じて `h1` のサイズを変える規則があり、`h1` の実寸が文書構造に依存する
  - `h5` 0.83em / `h6` 0.67em は本文 1rem 基準で 13.3px / 10.7px となり、本文より小さい
- [事実] 実装側 (`webroot/assets_s/css/common.css`) は文書レベルの `h1`〜`h6` に対して次の宣言を持つ (実装 Repository `tocoo/tocoo_travel` の確認時点)。`h1{font-size:24px}` / `h2{font-size:20px}` / `h3,h4{font-size:16px}` / `h5{font-size:14px}` / `h6{font-size:12px}` / `h1,h2,h3,h4,h5,h6{font-weight:500}`。**本節はこれらを正としない**。理由は次のとおり
  - `h3` と `h4` が同一の宣言で同値に設定されており、段が一意に定まらない (§3 のサイズスケールは段ごとに異なる値を持つ)
  - `h6` 12px が本文 16px より小さい
  - `font-weight: 500` が §3 の見出し 700 と一致しない
  - 同ファイルには Bootstrap v4.6.2 由来の `h1{font-size:2.5rem}` 等と `h1,h2,h3,h4,h5,h6{font-size:100%;font-weight:400}` が併存し、同一要素に対して複数の宣言が重なっている。**本書は同ファイルの計算値 (実際に適用される値) を実測として扱わない**
  - 同ファイルは DS 準拠の reset / base 層へ置き換える対象として実装側で扱われている (実装 Repository `tocoo/tocoo_travel` #6635 / PR #6643)。**撤去の範囲・完了状況は実装 Repository 側の事実であり本書では確定しない** (確認時点では会員系テンプレートの一部が同ファイルの読み込みを保持していた)
- [注意] 同ファイルは §1 が持ち込まないと定める Bootstrap 残骸 (`--primary:#007bff`) を保持している。ただし上記 `h1`〜`h6` の宣言は Bootstrap 由来ではないため、**§1「負債の非持込」の列挙 3 項目 (Bootstrap 残骸 `--primary:#007bff`・変数二重定義・管理画面系の色) への該当性は本書では判定しない**
- [事実] §3 の「見出し (一覧・カード) h2 2rem」は一覧・カードの実測値であり、`common.css` の `h2{font-size:20px}` は文書レベルの `h2` 要素に対する宣言である。両者は対象が異なるため同じ h2 の値として比較できない
- [決定] 文書レベル h2 は `font.heading.h2Size` (2rem) を用いる。`common.css` の `h2{font-size:20px}` は採らない (理由は上記のとおり)
- [注意] 本節の既定を実装へ反映すると文書レベルの見出しの実寸が従来の実装値から変わる (例: `h1` 24px → 40px)。反映の範囲・順序・期限は本書では決定しない (実装側タスクの範囲)
- 🚧 Component 内の見出しが文書レベル既定から外れている箇所の洗い出しは実査待ち

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: **4px (0.25rem) 系で確定** (TVL-0002)。spacing.0〜16 全段 bound
- コンテナ幅: `975 / 1195 / 1425px` (宿泊実装値・bound)
- ブレークポイント: **`640 / 768 / 1024 / 1280px`** (TVL-0004。現代標準へ更新 — 旧実装値 600/992/1200 からの変更。移行方針は TVL-0004 参照)。**本値は 3DS 共通 breakpoint として再認定** (owner-decisions.md Q5 決定・2026-07-24・Task 009-18-BP1)。ADR 正本・provenance は未確認 (009-19 provenance トラックへ残す)
- 代表 viewport (画面設計・Claude Design・HTML 確認用の表示幅): **`390 / 768 / 1280 / 1440px`** (3DS 横断・Web部責任者判断 2026-07-24・Task 009-18-BP1)。**これは表示確認用の代表幅であり responsive breakpoint token ではない** (breakpoint は上記・`breakpoint.*` token が正)

## 5. 角丸・シャドウ

- 角丸: `radius.sm 4 / md 8 / lg 16 / full 9999px` (bound)。用途トークンは 4 系統 (action / card / badge / overlay)
  - `radius.action` = full (pill) — ボタン・CTA・入力要素・チップ型操作要素。宿泊のサービスシグネチャ
  - `radius.card` = 暫定 md (8px) — カード外形。🚧 実px未取得
  - `radius.badge` = 暫定 sm (4px) — **非操作**のバッジ・ラベル (割引率ラベル・状態バッジ・カテゴリラベル・短い補助ラベル)。🚧 実px未取得
  - `radius.overlay` = 暫定 lg (16px) — オーバーレイの角丸 (Modal の表示形態 form = sheet の上端2隅等・§7)。🚧 実px未取得 (依頼元固有値は未実査)
- [決定] 割引率ラベル・状態バッジへ `radius.action` (pill) を使用しない。pill 形状はボタン・操作要素のシグネチャであり、非操作のラベルに用いると操作要素と誤認される。**バッジが操作可能な場合は badge ではなく action 系 Component として扱う** (その場合の角丸は `radius.action`)
- [事実] `radius.badge` の参照先 sm (4px) は既存 primitive radius scale からの暫定選定であり、新しい数値は追加していない。選定根拠は ①`radius.action` (pill) との形状差別化 ②`radius.card` (暫定 md) との階層差 ③寸法の小さいラベルでも形状が安定する。実確定は `radius.card` と同じ実査待ち区分
- シャドウ: 実値未抽出 🚧 (follow-up #13。暫定3段で据置き = TVL-0008)
- [事実] 上記 placeholder (`radius.card`・`radius.badge`・`shadow.*`・`motion.*`) の**確認方法と個別確認主体**は Web部責任者判断 2026-08-03 で定義済み (確認方法 = 依頼元 (画面設計) の提出値を受領して確定・個別確認主体 = 作業担当者が照合し Web部責任者が確認。正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §14)。ただし実査 (提出値の受領) は未実施であり placeholder は維持する (bound 昇格・暫定値の確定は行わない)。placeholder 11 件 (semantic 4・primitive 7) の確定リストと追跡先区分 (`follow-up #13` = shadow / `follow-up #3` = motion / follow-up 番号なし = radius.card・radius.badge) は owner-decisions.md §14

## 6. アイコン・画像

- アイコン体系: **Font Awesome 6 で確定** (TVL-0006)。新規制作は FA6 に統一、既存 Material 混在箇所は改修時に置換。サイズスケールは `iconSize.sm〜xl` (bound)
- 画像比率: object-fit 制御あり
- 画像なし・在庫ゼロ時の表現: 未定義 ❓ 検討トリガー: Card 実装着手時

## 7. コアコンポーネント

正: `components.md`。定義済: Button / Input / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal。

- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- 状態リストは固定 (hover/active/focus/disabled/loading/error/success)。宿泊のボタン状態は未取得 🚧
- Button variant 語彙は GOV-0002 (cross-service 5語)。**travel の Button 実装は4語 (primary/secondary/ghost/text)**。campaign(accent 塗りボタン)は廃止し accent はバッジ/割引ラベルの点専用 (TVL-0012)
- PriceTag は背景文脈を**明示的に選択する軸 (tone)** を持ち、`default` (明色面) と `inverse` (inverse 面) の 2 値を定義する。inverse 面では主要価格 `color.text.inverse`・補助価格/価格条件注記/割引前価格 `color.text.inverseMuted` を使用する (対応関係の正は `components.md`)。背景色を検知して自動反転する仕様・コンポーネント内部の固定色だけで複数背景へ対応する仕様は採らない。**tone は variant 語彙 (GOV-0002) とは別軸であり、variant 語彙への追加ではない**。実装 API 名 (prop 名) は未確定 ❓
- モーダルは **最終的に drawer へ全面統一**。centered dialog は deprecated・段階移行 (移行期間中は併存)。現在の方針根拠は `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**)。3DS 横断の Modal 実装基盤 (同 §1 Q9) は**未決**。`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認のため、現在の仕様根拠として参照しない (R-D provenance トラック)
- 未着手: Select / Tabs / Toast / Table / Accordion / Pagination / Badge (単体) / Stepper / Empty state (実体皆無)。Pagination / Badge (単体) / Stepper / Empty state は依頼元 (2026-08-03・依頼 D) の指摘で受理 (Task 009-39・受理と分類のみ・仕様定義は別 Task。正は `components.md` 共通事項)。新規 Component 定義工程への着手は Web部責任者判断 2026-08-03 で可 (`governance/owner-decisions.md` §15。依頼 D の新規 Component は Work Order 6 の 12 候補とは別)

### 7.1 Modal の表示形態 (form)

依頼元 (2026-08-03・依頼 D-6) に対応し、Modal に**表示形態 (form) 軸**を定義する。form は `drawer` (既定) / `sheet` / `popover` の 3 値をとる。

- [決定] **実装基盤は drawer 単一を維持し、第3の Modal 実装基盤を導入しない** (`governance/owner-decisions.md` §11 判断ⓑ)。`popover` が §11 判断ⓑ の「第3の Modal 実装基盤」に当たるかは、Web部責任者判断 2026-08-03 で「**当たらない (drawer / sheet と overlay の z 軸・backdrop・dismiss を共有する同一基盤上の表示形態である)**」と確定した (`governance/owner-decisions.md` §17)。`popover` の配置方式 (基準要素への相対配置) が drawer / sheet と異なることは、実装基盤の相違としない
- [決定] form は variant 語彙 (GOV-0002 の 5 語) とは**別軸**であり語彙への追加ではない (PriceTag の `tone` と同じ扱い)
- [決定] **配置規則**:
  - `drawer` (既定): 既存記述 (§7・`components.md`) を変更しない
  - `sheet`: 画面下端に貼り付き・全幅・上端 2 隅のみ角丸 (`radius.overlay` = 暫定 lg 16px)
  - `popover`: 基準要素 (トリガー) を起点に配置し、下方に余地がなければ上方向へ反転する。**基準要素を必要とする** (drawer / sheet は不要)
- [決定] **切替規則**: `{breakpoint.lg}` (1024px) 未満は `sheet`、以上は `popover` を用いる。`drawer` は form の既定であり本切替規則の対象ではない (用途に応じて明示選択する)
- [決定] backdrop (`color.overlay.backdrop` = 暫定 rgba(0,0,0,0.45)) は 3 形態すべてで使用する。z 軸は既存 `elevation.overlay` / `elevation.modal` を用いる。**開閉遷移 (`motion.transition.*`) と影 (`shadow.*`) は既存 placeholder を参照するのみ**で値・`$status` を変更しない
- [決定] 実装 API 名 (prop 名) は未確定 ❓ (form の値・`popover` の基準要素指定の prop 名を含む)。form は明示的に選択する軸であり、背景・文脈を検知して自動で形態を切り替える仕様は採らない

**本節で定義しない事項** (form 軸に付随して受領したが本 Task で定義せず理由を記録する):

- a11y の `role` / `aria-modal` / フォーカストラップ / 復帰先・背面スクロールロック・閉じる操作の実装方式 — [alignment-blocking-facts-resolution-plan.md](alignment-blocking-facts-resolution-plan.md) §8K が HTML・ARIA / name・role・state / focus 順序を UI・Implementation 下流課題に分類済み。DS 層で決定しない
- 最小タップ領域 (44px) の spacing トークン — ①§8K が target size・タップ領域を下流課題に分類済み ②44px は WCAG 2.2 の 2.5.5 Target Size (Enhanced) 相当で、§2 が最低ラインとする AA (2.5.8 Target Size (Minimum) = 24×24 CSS px) からは導けない ③`spacing` に step 11 (44px) が存在しない (step は 0/1/2/3/4/5/6/8/10/12/16 = 0/4/8/12/16/20/24/32/40/48/64px)。以上より**トークンを追加せず、未確定事項として残す**
- `sheet` の最大高・`popover` の幅段階 — 依頼元の画面固有実装値 (85% / 420px / 680px) であり本 Repository で実査していない。未確定として残す
- ADR (TVL-NNNN) の発行 — ADR / Decision ID の採番規則・正本体系が Repository 内に未整備 ([../../../governance/README.md](../../../governance/README.md))。恒久 ID を推測で採番しない
- `_adherence.oxlintrc.json` / `components/overlay/Modal.jsx` の変更 — 本 Repository のトラッキング対象外 (実装 Repository `tocoo/tocoo_travel` 側の別作業)

## 8. ブランド・クリエイティブガイド

- [事実] **ライティング・価格表記の正本として参照されていた `brand-content.md` は Repository 内に存在しない** (参照切れ。[README.md](README.md) §8・§16 が「`brand-content.md` の参照と実在状況 (存在しない)」を未決 Open Issue として保持)。**存在しない参照を確認済みの正本として扱わない**。本節が現時点で確認できるブランド／コンテンツ規則の記載箇所であり、`brand-content.md` の新規作成は行っていない (作成の要否は §8.1 末尾の Owner判断事項)
- [事実] 上流のコンテンツ規則正本 [../service-design/content-principles.md](../service-design/content-principles.md) は Draft として存在するが、§10 Open Issues で「正式な用語集・表記規則」「価格・税・手数料等の表示基準」をいずれも**未決**として保持し、§8 Boundary で具体的な文言・キャンペーンコピーを対象外としている。[../service-design/information-architecture.md](../service-design/information-architecture.md) IA-OBJ-007 Price も「正式な料金構造や表示単位は確定しない」と明記する
- [観察] 価格中心・実用トーン。数字を大きく強調する価格タイポがブランド表現の中核
- [事実] 特集は `#EF4123` を面で多用。通常導線と特集を色で分離する現状構造を維持
- [事実] 写真選定基準は未明文化 ❓ 検討トリガー: ブランドルール整理時
- [事実] ロゴファイルは未提供。プレーンな "ToCoo!" ワードマーク (見出しフォント + brand primary) で代用中。実ロゴ提供時に差し替え

### 8.1 割引率の表記規則

**本節は「表示 (表記) 規則」のみを定義し、割引率の算出方法・端数処理・上限値といった事業・価格仕様は定義しない。** 算出規則と表示規則を混同しない。

#### 表示形式

- [決定] 基本形は `-NN%` (半角マイナス + 半角数字 + 半角パーセント)。例: `-5%` / `-20%` / `-35%`
- [決定] 原則として使用しない表記: `20%OFF` / `20％引き` (全角パーセント) / `▲20%` / `最大20%OFF` (条件付き表現の既定使用)。同一の意味へ複数表記を混在させない (CTP-005 Consistent Terminology)
- [事実] 上記と異なる明示的な規則が Owner 決定またはブランドガイドラインに存在する場合はそれを優先し根拠を記録する。**現時点で Repository 内に該当する Owner 決定は確認できない** ([../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) に割引率表記の決定記録なし)

#### 符号

- [決定] 割引率であることを視覚的に示すため、数値の前に半角マイナス `-` を付す
- [決定] これは**表示規則として付与する記号**であり、計算上の負数をそのまま出力するものではない

#### 桁

- [決定] 半角数字を使用する / 原則として整数表示 / 不要な先頭ゼロを付けない (`-05%` は不可) / 小数点以下を表示しない

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
- [決定] 販売価格が元価格以下でない場合 (=値引きが成立しない場合)

DS では確定しない事項 (Owner判断事項):

- ❓ `100%` 以上となるデータの扱い
- ❓ 表示可能な上限値
- ❓ 「最大」「〜」等の条件付き表現を使用する条件
- [決定] 上限値・異常値処理が上流仕様に無い状態で、DS が任意の数値を決定しない

#### 表示内容の真実性 (表示成立条件)

- [決定] 割引率は、比較対象となる価格・対象条件・税条件・人数・日程等が**一致する場合にのみ**表示できる
- [決定] DS は価格計算ロジックを定義しない。上記は表示が成立するために必要な前提の記載である
- [決定] 根拠・対象・期間・基準が不明な場合は確定表現にしない (CTP-004 Evidence-backed Claims)
- [決定] 割引率は販促表現であり、施設・料金・条件等の Fact と区別できる表現とする (CTP-010)

#### 割引率と値引額

- ❓ **未確定事項**: 割引率 (`-NN%`) と値引額 (金額) の使い分け基準。値引額を表示する場合の通貨記号・桁区切り等の表記も未決 (上流の価格表記基準そのものが未決 = `content-principles.md` §10)
- [Owner判断事項] 使い分け基準の決定主体は価格・商品仕様の Owner および ブランド Owner
- [決定] 割引率等のコンテンツ表記規則を管理する正本は**独立した文書 (`brand-content.md` 等) を新設する方向を確定**する (依頼 E-4・Web部責任者判断 2026-08-03、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §16)。**実際の文書作成・中身・文書体系上の位置づけ・管理責務・既存正本との関係は別 Task**であり、本タスクでは推測で新規正本を作成しない (参照切れの `brand-content.md` は README.md §16 の Open Issue)。価格の単位表記 (1 名あたり・合計人数で割った旨等) の文言規則 (依頼 E-4) も本管理正本の対象に加わる (§8.1 は割引率の表記規則のみを定義し単位表記は対象外)

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
| follow-up #2 | フォーム入力/エラー/必須・検証 (枠色・背景色・必須表現・検証表示。プレースホルダを含む) | 🚧 実査待ち。**プレースホルダの文字色 `color.text.placeholder` のみ §2.3 で確定**し、それ以外は未解決 |
| — | カード実px・8スロット対応付け・画像欠落 fallback | 🚧 実査待ち / ❓ Card 着手時 |
| Q6 | 実装クラス命名方法論 (FLOCSS 等) | ❓ 検討トリガー: Component 実装着手時 |
| — | Breadcrumb 現在地への `color.text.muted` (白背景 ≈2.7:1) 適用の可否 | ❓ 未判定。価格・補助情報の用途に該当せず、上流 NVP-001 (現在地の可視性) と全ページ共通 Component の影響範囲を伴うため本書では判定しない |
| — | `color.text.muted` の適用可能範囲 (装飾的・非必須の弱表現に限るか) の明文化 | ❓ 未判定。判読性を要する補助情報が `mutedStrong` を使用することのみ確定 |
| — | select の未選択値 (プレースホルダ相当) への `color.text.muted` 使用 | 🚧 方向確定 (依頼元 2026-08-04・§4.5 + 判断点6・Web部責任者判断 2026-08-04、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §22)。**select の未選択値のみ** `color.text.muted` (`#9e9e9e`・≈2.7:1) を例外許容する方向 (AA 未達明示)。通常 `input` / `textarea` の placeholder は `color.text.placeholder` (gray.700・≈6.2:1) を維持。§2.3 は「`color.text.muted` をプレースホルダへ流用しない」(L157)・「選択前 `option` → `color.text.placeholder`」(L156) と定めるが、本例外の実規則化 (§2.3 への例外条項) は改訂着手の設計承認 (§9・§20) を経た別 Task・現時点では §2.3 本体は未改訂。`color.text.placeholder` / `color.text.muted` トークンは不変 |
| — | 割引率の正式な算出式・端数処理 | ❓ 未確定。決定主体 = 価格・商品仕様の Owner。DS の表示上の暫定案は「小数点以下切り捨て」(§8.1・正式規則ではない) |
| — | 割引率の表示可能な上限値・`100%` 以上のデータの扱い・「最大」等の条件付き表現を使用する条件 | ❓/🚧 (§8.1)。上限値・`100%` 以上の扱い・算出式は ❓ 未確定 (DS では任意の数値を決定しない・上流未決)。「最大NN%OFF」等の条件付き表現の**使用条件は Task 009-45 (Web部責任者判断 2026-08-04・[../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §21) で定める方向を確定** = 対象範囲の最大値かつ文脈で「最大」と判別可能な場合のみ (CTP-004)。§8.1 本体の実改訂は別 Task |
| — | 割引率 (`-NN%`) と値引額 (金額) の使い分け基準・値引額の表記 | ❓ 未確定。上流の価格表記基準そのものが未決 (`../service-design/content-principles.md` §10) |
| — | 割引率の表記の基本形 (§8.1) — `-NN%` から `NN%OFF` への変更 | 🚧 方向確定 (依頼元 2026-08-04・DS-REQUEST「割引率の表記規則 (§8.1)」・Web部責任者判断 2026-08-04、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §21)。§8.1 の基本形を **`-NN%` → `NN%OFF`** へ変更し、マイナス付与規則 (「符号」節) を**撤回**する方向。全角 `％`・`▲NN%` の禁止は維持・半角 `%`。§8.1 L293 の上書き機構 (Owner 決定を優先) に沿い §21 が根拠。**§8.1 本体 (L287-338) の実改訂は改訂着手の設計承認 (§9・§20) を経た別 Task**・現時点では §8.1 の基本形は `-NN%` のまま。components.md の §8.1 参照 (`-NN%`) も実改訂時に整合 |
| — | 割引率等のコンテンツ表記規則の管理正本 | 🚧 方向転換 (依頼 E-4・Web部責任者判断 2026-08-03 → 2026-08-04)。当初は独立文書 (`brand-content.md` 等) を新設する方向 (§16・2026-08-03) だったが、**Task 009-45 (Web部責任者判断 2026-08-04・[../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §21) で §16 の新設方向を撤回し、割引率等のコンテンツ表記規則は design.md §8 系に集約する方向を確定**。§8.1 L338・§16 本体・README.md §16 の実改訂は改訂着手の設計承認 (§9・§20) を経た別 Task であり現時点では未改訂 (§8.1 L338 は現在も新設方向を記す)。`brand-content.md` は新規作成しない |
| — | `color.scheme.*.inverse` を面 (背景) として使用する正式用途 (割引ラベル背景等) | ✅ 解決 (c1・Web部責任者判断 2026-08-03、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §13)。割引ラベル背景として使用可・文字色 `color.text.strong` 固定 (main 5.78:1 / sub 7.50:1)。評価色 `color.icon.rating` トークンは面へ流用しない (§2.1) |
| — | `#C8912C` 面上に白文字を指定する既存 Owner 指示が存在する場合の解消 | ✅ 解決 (c1・Web部責任者判断 2026-08-03)。`color.scheme.*.inverse` 面の文字色は `color.text.strong` に固定し白文字は使用しない (main 2.78:1・sub 2.15:1 で未達)。依頼元の白文字運用は本決定に反する例外運用として採らない (§2.1)。**ただし Task 009-44 (Web部責任者判断 2026-08-04・[../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §20) で、非操作の点的ラベル (campaign accent / scheme 逆色面) に限り白文字を例外として許容する方向を確定** (AA 未達明示・実規則化は §2.1・components.md への例外条項追加として別 Task・それまで現行規則 = 白文字禁止 を維持。下記「白文字非準拠運用の扱い」行) |
| — | campaign accent 面上で §2.1 の (a) (b) を満たさない文字 ((i) 20px 未満のすべて／(ii) 20px 以上 24px 未満かつ通常ウェイト) を成立させる濃色背景の追加要否 | 🚧 b2 選択済み・実色値取得待ち (Web部責任者判断 2026-08-03、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §13)。小サイズバッジ向けに accent 淡色面 (淡色面 + 濃色文字) を新設する方向を確定。淡色段 (50/100 相当) の実色値が未取得のため新規 primitive・semantic は未追加。取得後に 4.5:1 以上を検証して確定 (§2.1)。Task 009-44 (§20) は同一問題への別経路として**白文字非準拠の例外許容**の方向も確定しており、b2 (淡色面追加) と併存し b2 は実色値取得まで保留 (下記「白文字非準拠運用の扱い」行) |
| — | バッジ/ラベルの白文字非準拠運用 (割引率 `#C8912C` 面/白 14px・小サイズ campaign accent 面/白 12px) の扱い | 🚧 方向確定 (依頼元 2026-08-04・依頼B + 判断点2/4・Web部責任者判断 2026-08-04、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §20)。実装側の (i)(ii) は現行規則 (`Card.slot.badge`・§2.1) に**不適合** (`#C8912C`×白 2.78:1・`#C8B12C`×白 2.15:1・accent×白 3.68:1 で 4.5:1 未達)。**非操作の点的ラベル + campaign accent/scheme 逆色面 に限り白文字を例外として許容する方向**を確定 (サイズ/ウェイト不問・AA 未達明示)。白文字が成立する面は `color.surface.inverse` (16.10:1) の 1 面のみ。**例外の実規則化 (§2.1・components.md への例外条項) は改訂着手の設計承認 (§9・§20) を経た別 Task**・それまで現行規則 (白文字禁止) を維持し実装非準拠は未是正扱い。b2 (§13・accent 淡色面) は保留・併存 |
| — | `radius.badge` の実px | 🚧 実査待ち。暫定 sm (4px)。`radius.card` と同じ区分 (§5) |
| — | PriceTag の tone (背景文脈) の実装 API 名 (prop 名) | ❓ 未確定。DS は default / inverse の 2 値と色の対応関係のみ定義 (`components.md`) |
| — | `color.text.inverseMuted` を inverse 以外の暗色面へ適用する場合の可否 | ❓ 未判定。検証済みは inverse surface `#212121` 上 (≈6.01:1) のみ |
| — | 訪問済みリンク (`visited`) を色で区別する要否 | ❓ 未確定。Owner判断事項。現在は `color.text.link` を維持する決定のみ (§2.2)。既存 palette に visited 用の色値が無く、本書では primitive を追加しない |
| — | standalone なリンク (カード全体リンク・ナビゲーション項目・パンくず) へ下線の既定を及ぼすかの区分 | ❓ 未判定。§2.2 が定めた**下線**の既定は文中リンクを対象とする (状態ごとの文字色と focus の取り扱いは対象を限定しないため standalone にも適用される)。領域・レイアウトでリンクが成立する場合の下線の扱いは判定していない |
| — | 文書レベルの見出し既定 (§3.1) を実装へ反映する範囲・順序・期限 | ❓ 未確定。本書は既定値のみを定義し反映計画を決定しない。実装値からの実寸変化 (例 `h1` 24px → 40px) を伴う |
| — | Component 内の見出しが文書レベル既定 (§3.1) から外れている箇所の洗い出し | 🚧 実査待ち。外れる場合は当該 Component 仕様へ明示記載する規則のみ確定 (§3.1) |
| — | 文書レベルの `h6` (1rem) と本文 (1rem) の区別根拠 | ❓ 未判定。本文のウェイト (`font.body.weight` 相当) が正本上不在で、ウェイトによる区別が成立しない。行間差 (1.3 / 1.8) は折り返し時のみ視覚差となり、書体も同一スタック (§3.1) |
| — | `follow-up #2` のうち文字色のみを `bound` として確定させたことが [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §14 (実査待ちの項目の取り扱い) に該当するか | ❓ 未判定。判定主体 = Web部責任者。同 §14 が求める確認方法・個別項目の確認主体は **owner-decisions.md §14 で定義済み** (Web部責任者判断 2026-08-03。確認方法 = 依頼元提出値の受領・確認主体 = 作業担当者照合 + Web部責任者確認)。`follow-up #2` の文字色確定が §14 に該当するかの判定自体は本書では引き続き判定しない (§2.3) |
| — | §3.1 の文書レベル見出しスケールが [alignment-blocking-facts-resolution-plan.md](alignment-blocking-facts-resolution-plan.md) §8J.4 の Screen Requirements 分類 (観点「h1〜h6 等の具体階層」) に抵触するか | ❓ Owner判断事項。同表は size scale・line-height scale・見出しの用途・token を「既存 Design System で明示」側へ分類する一方、観点の文言に「画面別」の限定が付いていない。§3.1 は既存スケールの文書レベル既定への割当であり画面別の見出し階層・semantic role の割当を定めていないが、抵触の有無は本書では判定しない |
| — | 実装が文書レベルの既定値 (base 層) をどこで供給すべきかという層の責務そのものの方針 | ❓ 未定義。本書・`components.md`・`README.md` に記載がなく、reset CSS への言及も無い。§2.2・§2.3・§3.1 は値を定義したものであり供給箇所の方針を策定していない |
| — | 画像を面 (背景) とする場合の文字色とコントラスト確保の方法 (scrim の要否・実現方式・評価方法) | ❓ 未定義 (依頼元 2026-08-03・依頼 E-1)。§2.1 の検証表は**単色面のみ**を対象とし (`scrim` / `グラデーション` / `gradient` は travel 配下 0 件)、画像・グラデーションを面とする場合のコントラスト評価方法が正本上未定義。依頼元の暫定実装 (`color-mix` による scrim) を DS 規則として追認しない |
| — | 会員限定で情報 (料金等) をマスクする表現の構成 (アイコン・文言・CTA の配置) | ❓ 未定義 (依頼元 2026-08-03・依頼 E-2。`会員限定` / `マスク` は travel 配下 0 件)。マスク表現の視覚構成は DS/UI に関わるが、会員限定の業務条件・料金非公開の業務ルールは上流 (Service Design / Screen Requirements) の未定義業務仕様に依存する (`../service-design/screen-matrix.md` §2 = 正式な画面一覧・業務仕様未定義)。DS 層で先行して構成を確定しない。`semantic.travel.json` `$meta.notes` の「会員ランク色は構築しない (破棄済)」とは別論点 |
| — | 価格の単位表記 (1 名あたり・合計人数で割った旨等) の文言規則 | ❓ 未定義 (依頼元 2026-08-03・依頼 E-4)。§8.1 は割引率の表記規則のみを定義し**単位表記は対象外**。上流 `../service-design/content-principles.md` §10 が価格・税・手数料等の表示基準を未決として保持。管理正本は当初 独立文書 (`brand-content.md` 等) 新設の方向 (§16・2026-08-03) だったが Task 009-45 (§21・2026-08-04) で design.md §8 系集約へ方向転換 (§16 の新設方向を撤回)。単位表記もこの集約先の対象。実改訂は別 Task |
| — | Modal の表示形態 (form = sheet / popover) の a11y (`role` / `aria-modal` / フォーカストラップ / 復帰先・背面スクロールロック・閉じる操作の実装方式) | ❓ 未定義 (依頼 D-6・§7.1)。[alignment-blocking-facts-resolution-plan.md](alignment-blocking-facts-resolution-plan.md) §8K が HTML・ARIA / name・role・state / focus 順序を UI・Implementation 下流課題に分類済み。DS 層で決定しない |
| — | セクション間・ブロック間の余白の用途 semantic トークンと 36px 段 (`spacing.9`) | 🚧 方向確定 (依頼元 2026-08-04・依頼 Doc1・Web部責任者判断 2026-08-04、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §18)。「セクション間」のみ用途 semantic トークン化・primitive `spacing.9` = 2.25rem (36px・`8` と `10` の間・`$status = bound`) を追加する方向。「セクション内ブロック間」「面色セクション内側 padding」の 2 区分は据置。**実追加 (primitive/semantic の編集) は改訂着手の設計承認 (§9・§20) を経た別 Task**・用途トークンの命名は参照切れの `governance/naming-rules.md` 整備に依存。既存段の値・参照・`$status` は不変。依頼元の暫定実装 (`--spacing-9` 一斉化) は追認しない |
| — | Modal の form 切替・タップ操作の最小タップ領域 (44px) の spacing トークン | ❓ 未追加 (依頼 D-6・§7.1)。§8K が target size を下流課題に分類済み・44px は WCAG 2.2 の 2.5.5 (Enhanced) 相当で §2 の AA 最低ライン (2.5.8 = 24×24 CSS px) から導けない・`spacing` に step 11 (44px) が不在。§7.1 は「トークンを追加せず、未確定事項として残す」と定める。**依頼元 2026-08-04 (依頼 Doc1) は 44px 段の追加要否を挙げたが、Web部責任者判断 2026-08-04 は §7.1 の現状 (トークンを追加せず・未確定事項として残す) を維持する (追加しない・現状維持)** ([../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §18)。タップ領域の target size そのものは §8K の下流課題として継続 (本行は spacing 段の追加要否のみを扱う)。既存 48px (`spacing.12`) 代替運用は追認しない |
| — | Modal の form = sheet の最大高・form = popover の幅段階 | ❓ 未確定 (依頼 D-6・§7.1)。依頼元の画面固有実装値 (85% / 420px / 680px) であり本 Repository で実査していない |
| — | 会員限定 (有料会員限定) ラベルをカテゴリラベルと区別するか (`Card.slot.badge`) | 🚧 方向確定 (依頼元 2026-08-04・依頼A・Web部責任者判断 2026-08-04、正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §19)。**区別する**・手段 = 面色の使い分け (基本 neutral 面 / 特集紐づき accent 面 / 例外 inverse 面)・**既存トークンの範囲で成立する組み合わせに限定**。面色・文字色の成立条件は §2.1 の検証表が正で、小サイズ (例 12px) の accent 面/白文字の適否は Task 009-44 と重なる。写真上への配置は E-1 (画像を面とする場合の scrim・Task 009-40 起票・上記の E-1 行) と関連 (Task 009-46 は未選択値 muted の別論点で scrim ではない)。`会員限定` の**マスク表現** (E-2・上記行) とは別論点。用途トークン・区別規則の実定義は改訂着手の設計承認 (§9・§20) を経た別 Task |
| — | 会員種別語 (無料 / 有料会員) の表記管轄 | ❓ コンテンツ表記規則の管轄 (DS の token 管轄外・依頼元 2026-08-04・依頼A)。参照切れの `brand-content.md` は README.md §16 が未決保持・独立文書新設の方向は [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §16 に記録。管理正本の所在 (design.md §8 系集約か独立文書新設か) は Task 009-45 が扱う論点。本書では会員種別語の具体表記を確定しない (§19) |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-09 | 0.3.0-draft: 独立DS再構築 (要求仕様 R1〜R10)。TVL-0001〜0008 反映 (rem化・4px系・テキスト2段・BP現代標準・FA6・drawer統一・リンク色保留・実査待ちplaceholder維持) | Claude Design (Builder) |
| 2026-07-24 | Task 009-18-BP1: §4 に記述追加。ブレークポイント `640/768/1024/1280px` (TVL-0004) を 3DS 共通 breakpoint として再認定した旨を注記 (owner-decisions.md Q5 決定・2026-07-24。Travel token 値は不変)。代表 viewport (画面設計・HTML 確認用) `390/768/1280/1440px` を breakpoint とは別概念として §4 に追加 (3DS 横断・正本=各 design.md)。ADR 正本・provenance 未確認は 009-19 へ残す旨を明記。token・値・status・version は不変 | Claude Code |
| 2026-07-28 | Task 009-28R: §7 のモーダル記述について、`TVL-0007` を現在の仕様根拠として参照する表現を補正。現在の方針根拠は `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**) であること、3DS 横断の Modal 実装基盤 (同 §1 Q9) は**未決**であること、`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認であるため現在の仕様根拠として参照しないことを明記した。**現行仕様そのものは不変** (drawer への全面統一・centered dialog の deprecated・段階移行はいずれも維持)。判断日 (2026-07-27) と本反映日 (2026-07-28) は別の事象として区別している。本工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-07-28、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。§7 の他記述・§1〜§6・§8〜§9・未確定事項の一覧・token・値・`$status`・version・Component の実装要件・rental-car / inbound の成果物は不変。`TVL-0007` の historical provenance 未確認と `alignment-blocking-facts-resolution-plan.md` §8L の R-D 分類は変更していない。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-28 | Task 009-28R の記述是正: PR [#107](https://github.com/tocoo/coocom-design-system/pull/107) コードレビュー (issuecomment-5098867540) の指摘に対応し、§7 のモーダル記述の冒頭を是正。**「モーダルは drawer に全面統一」という、統一が完了済みと読める記述を撤回**し、「モーダルは最終的に drawer へ全面統一」へ変更した。同 PR 内で `components.md` の実装基盤行を「最終的に drawer へ全面統一」へ補正した一方、本ファイルは補正前の表現のままとしていたため、**本 PR によって 2 文書間に表現の分岐が生じていた**。あわせて「段階移行」に「(移行期間中は併存)」を補い、`governance/owner-decisions.md` §11 の判断ⓐ (最終到達方針であり既存 centered dialog の即時廃止・一括置換を意味しない)・判断ⓒ (deprecated だが移行期間中の併存を認める) と読み取りを一致させた。**是正対象は §7 の当該 1 行のみ**。方針そのものは不変 (最終的に drawer へ統一する現行方針・centered dialog の deprecated・段階移行はいずれも維持) であり、即時廃止・一括置換・移行対象・順序・期限・完了条件を決定していない。§7 の他記述・§1〜§6・§8〜§9・未確定事項の一覧・token・値・`$status`・version・Component の実装要件・rental-car / inbound の成果物は不変 | Claude Code |
| 2026-07-29 | Task 009-33: §2 の表に semantic トークン `color.text.mutedStrong` (gray.700 `#616161`・bound・白背景 ≈6.2:1) の行を追加し、`color.text.muted` の行に白背景コントラスト値 (≈2.7:1) を補記した。§2 にテキスト色の 4 段構成 (`strong` `#212121` / `body` `#424242` / `mutedStrong` `#616161` / `muted` `#9e9e9e`) と、判読性を必要とする補助情報 (補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件) が `color.text.mutedStrong` を使用すること、`color.text.muted` は通常テキストに求められる 4.5:1 に達しないため判読性を要する情報には用いないことを [事実] として 1 行追加した。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない。未確定事項の一覧に 2 行追加した (Breadcrumb 現在地への `color.text.muted` 適用の可否・`color.text.muted` の適用可能範囲の明文化。いずれも本書では判定しない)。**不変**: §1・§3〜§9、§2 表の他の行、`color.text.muted` の参照先 gray.600 と値 `#9e9e9e` と `bound`、`color.text.body`、primitive の色値、他の token・`$status`、version 表記、Component の実装要件、rental-car / inbound の成果物。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-34: **§2 の表**に `color.text.inverse` / `color.text.inverseMuted` / `color.text.onAccent` の 3 行を追加した。**§2.1「面 (背景) と文字色の組み合わせ規則」を新設**し、§2.1 冒頭に用語の定義 (本節で用いる条件) を置き (ウェイトの境界 = bold は `700` 以上・通常ウェイトは `700` 未満で全ウェイトを排他的に二分する／条件 (a) = `24px` 以上でウェイトを問わない／条件 (b) = `20px` 以上かつ bold／(a) (b) を満たさない文字 = (i) `20px` 未満のすべてと (ii) `20px` 以上 `24px` 未満かつ通常ウェイト／「大きなテキスト相当」= (a) (b) を満たす文字 (サイズ・ウェイトの条件・WCAG 2.2 の大きなテキストより狭い)／「大きなテキスト基準」= コントラスト比 3:1 で 2 語は別概念)、検証した 11 組み合わせの表 (背景・文字・概算・通常テキスト 4.5:1 判定・大きなテキスト 3:1 判定・扱い。`color.scheme.main.inverse` `#C8912C` と `color.scheme.sub.inverse` `#C8B12C` は値が異なるためワイルドカード表記で束ねず個別に記載。表は `#### 検証した組み合わせ` 節に置き、検証範囲を限定する前文を表の直前に配置した)、campaign accent 面上の文字色は `color.text.onAccent` のみとし `color.text.strong` (4.37:1) は規則としては使用しないこと、campaign accent を面として使用できるのは (a) (b) のいずれかを満たす文字に限り、(a) (b) のいずれも満たさない文字 ((i) (ii)) には面として使用しないこと、その場合の代替 2 案 (既定 = `color.surface.inverse` 面 + `color.text.inverse` / accent を非テキスト要素に限定。accent を文字色として明色面に置く方法は代替にならない) と (a) (b) を満たす文字に限り選べる第 3 の構成 (accent を文字色として明色面に置く)、禁止事項 4 件 ((a) (b) を満たさない文字への白文字・`onAccent` を理由としたコントラスト確認の省略・AA 未達のブランド表現としての自動許容・縁取り/影による代替)、両スキームの逆色を面として使う場合は `color.text.strong` を原則とし白文字 (main 2.78:1・sub 2.15:1) を正式な通常利用として許可しないこと、評価色・割引/販促色・ブランド補色・状態色を同一用途へ統合しない用途境界を記載した。**§5** に `radius.badge` (暫定 sm 4px) と非操作ラベルへ pill を使わない規則を追記した。**§7** に PriceTag の tone (default / inverse) を追記した。**§8** の「正: `brand-content.md`」を撤回し、同ファイルが Repository 内に存在しないこと・存在しない参照を正本として扱わないこと・現時点で確認できる記載箇所が §8 であることへ改めた。§1 の同ファイルへの委任表現も同様に改めた。**§8.1「割引率の表記規則」を新設**し、表示形式 (`-NN%`・原則使用しない表記)・符号 (表示規則として付与する記号)・桁 (半角/整数/先頭ゼロなし/小数非表示)・端数処理 (表示上の暫定案 = 小数点以下切り捨て／未確定事項 = 正式な算出式と端数処理／決定主体 = 価格・商品仕様の Owner を区別して記録し暫定案を正式規則として扱わない)・表示しない条件 4 件 (0% 以下・算出不能・元価格なし・販売価格が元価格以下でない)・DS で確定しない事項 3 件 (100% 以上の扱い・上限値・条件付き表現の使用条件)・表示成立条件 (比較対象価格・対象条件・税条件・人数・日程等の一致。DS は価格計算ロジックを定義しない)・割引率と値引額の使い分けが未決であることを記載した。**未確定事項の一覧に 10 行追加**した。**不変**: §3・§4・§6・§9、§2 表の他の行、§2 の既存 2 行 ([事実] 品質基準・テキスト 4 段)、既存 token の値・参照先・`$status`、primitive の色値、version 表記、Component の実装要件、rental-car / inbound の成果物。**作成していないもの**: `brand-content.md` (新設の要否・管理正本の所在は §8.1 に Owner判断事項として記載)、価格算出ロジック、事業上の割引率算出式、新規 primitive、`color.text.onSchemeInverse` 相当の alias。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (§2.1 のコントラスト比は概算の記録)。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。改訂着手の設計承認は取得していない (同 §9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-35: 文書レベルの既定値 (base 層) として参照されたが正本に記載が無かった 3 件を補完した。**§2 の表**に `color.text.placeholder` (gray.700 `#616161`・白背景 ≈6.2:1)・`color.text.linkHover` (scheme.main.hover `#2340A6`)・`color.text.linkActive` (scheme.main.pressed `#1B3488`) の 3 行を追加し、§2 に「テキスト色 4 段は濃度段であり、用途に固定した別名 (`link` / `linkHover` / `linkActive` / `placeholder` / `inverse` / `inverseMuted` / `onAccent`) は 4 段とは別に定義する。用途別名が同じ primitive を参照しても一方の値の変更が他方へ及ぶ設計にはしない」旨の [事実] を 1 行追加した。**§2.2「リンクの装飾と状態」を新設**し、本節が定めるのは色以外の装飾 (下線) と状態 (hover / visited / active / focus) ごとの取り扱いであって状態語そのものの新設ではないこと (固定リストは `components.md` 共通事項が正)、状態別の文字色と下線の表 (文字色の列は対象を限定せず standalone なリンクを含む・下線の列は文中リンクのみ)、文中リンクに下線を付し下線を外す既定を置かないこと、hover は下線を維持したまま `color.text.linkHover` へ変更すること、active は `color.text.linkActive` を使用すること、visited に専用色を設けず `color.text.link` を維持すること (既存 palette に visited 用色値が無く primitive を追加しない)、focus は `color.focus.ring` の `outline` を用い hover の色変更で代替しないこと、状態表現に `opacity` を用いず `components.md` 共通事項の「全 Component の hover は opacity 変化 (≈0.85) を暫定参照とし `🚧 暫定` を付す」からリンクを除外すること、実装側 `common.css` の 3 宣言 (`a,a:hover,button,button:hover` の旧主色 `#283593`／`a:hover,button:hover` の `opacity:.75` と下線解除／`a:active,a:focus,a:visited,button:active,button:focus,button:visited` の `outline:none!important` と下線解除。最後の 1 件は本節の focus の決定と直接衝突し base 層からの `outline` 供給を特異度と `!important` の面で妨げる) をいずれも DS 規則として採らないこと、同ファイルが Bootstrap v4.6.2 を含み `a{color:#007bff;…}` 等が併存するため計算値を実測として扱わないこと、下線の既定は文中リンクを対象とし standalone なリンクへの適用は未判定である一方で状態ごとの文字色と focus の取り扱いは対象を限定しないことを記載した。**§2.3「プレースホルダの文字色」を新設**し、`color.text.placeholder` を使用すること、`color.text.muted` (`#9e9e9e`・≈2.7:1) を流用しないこと、`color.text.mutedStrong` と同じ primitive (gray.700) を参照しつつ用途が異なるため別トークンとすること、実装側 `common.css` の `input::placeholder,option,textarea::placeholder` の宣言 (`#9e9e9e`・`Roboto`・14px・weight 400) のうち色を正とせず、本節は文字色のみを定義して書体・サイズ・ウェイトを定義しないこと、入力済みテキスト (`color.text.body`) との判別を色差のみに依存させないこと、必須項目・ラベル・エラーメッセージ・入力形式の説明の代替に用いないこと、文字色のみを定義し枠色・背景色・必須表現・検証表示は `follow-up #2` の実査待ちであること、`follow-up #2` 全体を解決済みとして扱わず文字色のみの `bound` 化が [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §14 に該当するかは判定しないことを記載した。**§3 の表**の見出し行を「文書レベル h1〜h6」と「一覧・カード」の 2 行に分け、行間行に「tight 1.3 (見出し = §3.1)」を補記した。**§3.1「文書レベルの見出しスケール (h1〜h6)」を新設**し、本節が定めるのは `h1`〜`h6` の各要素に当てる既定値のみであり画面別の見出し階層・semantic role の割当は定めないこと、h1 `4xl` 2.5rem / h2 `3xl` 2rem / h3 `2xl` 1.5rem / h4 `xl` 1.25rem / h5 `lg` 1.125rem / h6 `md` 1rem の割当表 (太さ 700・行間 1.3)、書体は `font.heading.family` を文書レベルの既定とし明朝は明示的に選択する書体であること、太さ `font.heading.weight` (700) と行間 `font.heading.lineHeight` (tight 1.3) を h1〜h6 共通の既定とすること、文書レベルと Component の見出しは同一トークン群 `font.heading.*` を共用し Component 側の逸脱は当該仕様へ明示記載すること、新しいサイズ値・行間値・ウェイト値 (primitive) を追加せず既存スケールへの割当のみであること、`h6` は本文と同サイズ (1rem) となるが本文のウェイトが正本上不在のためウェイトによる区別を根拠とせず行間差は折り返し時のみ視覚差となり書体も同一スタックであること、UA 既定に委ねない理由 3 点 (`em` 基準で rem 基準 TVL-0001 と不整合・入れ子段数で `h1` 実寸が変わる・`h5` `h6` が本文より小さい)、実装側 `common.css` の文書レベル `h1`〜`h6` の宣言 (`h1` 24px / `h2` 20px / `h3,h4` 16px / `h5` 14px / `h6` 12px / `h1〜h6` weight 500) を正としない理由 (`h3` と `h4` が同一宣言で同値のため段が一意に定まらない・`h6` が本文より小さい・weight 500 が §3 の 700 と不一致・同ファイル内に Bootstrap v4.6.2 由来の宣言が併存し同一要素へ複数の宣言が重なるため計算値を実測として扱わない・同ファイルは DS 準拠の reset / base 層へ置き換える対象として実装側で扱われており撤去の範囲・完了状況は本書では確定しない)、同ファイルが §1 の Bootstrap 残骸 (`--primary:#007bff`) を保持する一方で `h1`〜`h6` の宣言は Bootstrap 由来でないため §1 の列挙 3 項目への該当性を判定しないこと、§3 の「見出し (一覧・カード) h2 2rem」と `common.css` の `h2{font-size:20px}` は対象が異なり同じ h2 の値として比較できないこと、文書レベル h2 は `font.heading.h2Size` (2rem) を用いること、反映により実寸が変わること (例 `h1` 24px → 40px) と反映の範囲・順序・期限は本書で決定しないことを記載した。**未確定事項の一覧**は既存の `follow-up #2` 行の内容欄・状態欄を更新し (対象に枠色・背景色・必須表現・検証表示・プレースホルダを明記し、プレースホルダの文字色のみ §2.3 で確定・それ以外は未解決と記載)、**8 行追加**した (visited を色で区別する要否・standalone リンクへの下線既定の区分・§3.1 の実装反映の範囲/順序/期限・Component 内見出しの逸脱箇所の洗い出し・`h6` と本文の区別根拠・`follow-up #2` の部分確定と §14 該当性・§3.1 と `alignment-blocking-facts-resolution-plan.md` §8J.4 の Screen Requirements 分類との関係・実装が base 層をどこで供給すべきかという層の責務の方針)。**不変**: §1・§2.1・§4〜§9、§2 表の他の行、§2 の既存 2 行、`color.text.link` の `$value`・参照先・`$status`、`color.text.muted` / `mutedStrong` の値・参照先・用途、`font.heading.family` / `h2Size` の `$value`・参照先・`$status`、`font.body.*` / `font.display.*` / `font.price.*`、primitive の色値・サイズ値・行間値・ウェイト値、他の token・`$status`、version 表記、rental-car / inbound の成果物。**作成・追加していないもの**: 新規 primitive (サイズ・行間・ウェイト・色値のいずれも)、visited 用の色、状態の固定リストへの追加、reset / base 層の CSS 実装方針、実装ファイル、`brand-content.md`、画面別の見出し階層・semantic role の割当。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (コントラスト比は概算の記録)。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-38: 依頼元 (2026-08-03) の依頼 B / C に対応し §2.1 を更新。**C (c1)**: 「scheme inverse 色を面として使用する場合」の [事実] を、`color.scheme.*.inverse` の用途が評価色 (`color.icon.rating`) に加え割引ラベル背景の面用途を持つこと (面用途は Web部責任者判断 2026-08-03 で定義・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §13) へ更新し、面用途に専用 semantic 用途トークンを追加せず `color.scheme.*.inverse` を面として参照する旨を明記。同節に文字色を `color.text.strong` に固定する [決定] (main `#C8912C` 5.78:1 / sub `#C8B12C` 7.50:1・白文字は 2.78:1 / 2.15:1 で不可・依頼元の白文字運用は本決定に反する例外運用として採らない) を追加 (旧「両スキームの逆色を面として使用する場合の文字色は…を原則とする」[決定] の趣旨を固定化)。「評価色と販促面色の用途境界」の [Owner判断事項] (割引ラベル背景への使用可否は未定義) を [決定] (割引ラベル背景として使用可・文字色 `color.text.strong` 固定・逆色の値は評価と割引ラベルの 2 用途に用いるが用途は分離し `color.icon.rating` トークンを面へ再束縛しない) へ変更し、`color.icon.rating` を流用しない [決定] にトークン再束縛の禁止を補記。**B (b2)**: 「代替規則」に、Web部責任者が小サイズ (例 12px) バッジへ accent 淡色面 (淡色面 + 濃色文字) を新設する方向 (b2) を選択したが accent 淡色段 (50/100 相当) の実色値が未取得のため新規 primitive・semantic を追加していないこと・取得後に「淡色面 + `color.text.strong` の 4.5:1 以上」を検証して確定すること・実色値取得までは現行の代替規則が有効であること (12px は既定の neutral dark 面) を [事実] として追加。**未確定事項の一覧**を 3 件更新 (`color.scheme.*.inverse` の面用途 = ✅ 解決 c1・`#C8912C` 面上の白文字 Owner 指示の解消 = ✅ 解決 c1・campaign accent 面上濃色背景の追加要否 = 🚧 b2 選択済み・実色値取得待ち)。**不変**: §2.1 の検証した組み合わせの表 (概算値・扱い)・用語の定義・campaign accent 面上の文字の [決定]、§1〜§9 の他記述、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の色値、Component の実装要件、rental-car / inbound の成果物。**追加していないもの**: 新規 primitive・新規 semantic 用途トークン・`color.text.onSchemeInverse` 相当の alias。引用したコントラスト比は §2.1 の表と一致 (main `#C8912C` = 5.78:1・sub `#C8B12C` = 7.50:1 を取り違えない)。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-41: 依頼元 (2026-08-03) の依頼 F「placeholder の解決」に対応。§5 に、placeholder (`radius.card`・`radius.badge`・`shadow.*`・`motion.*`) の確認方法・個別確認主体が Web部責任者判断 2026-08-03 で定義済み (確認方法 = 依頼元提出値の受領・確認主体 = 作業担当者照合 + Web部責任者確認・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §14) であること、実査 (提出値の受領) は未実施のため placeholder を維持すること、placeholder 11 件 (semantic 4・primitive 7) の確定リストと追跡先区分 (`follow-up #13` = shadow / `follow-up #3` = motion / follow-up 番号なし = radius.card・radius.badge) は owner-decisions.md §14 にあることを [事実] として 1 行追加した。未確定事項の一覧の `follow-up #2` 文字色確定の §14 該当性の行を、同 §14 が求める確認方法・個別確認主体が owner-decisions.md §14 で定義済みになった旨へ更新した (該当性の判定自体は引き続き本書で行わない)。**不変**: §5 の角丸/シャドウの token・値・`$status`・暫定値、§1〜§4・§6〜§9 の他記述、既存 token の値・参照先・`$status`・`$note`・`$meta.version`・version、primitive の色値、Component の実装要件、rental-car / inbound の成果物。placeholder の bound 昇格・暫定値の確定・実査の実施は行っていない。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-39: 依頼元 (2026-08-03) の依頼 D「Component の不足」に対応 (受理と分類のみ)。§7 コアコンポーネントの未着手一覧に Pagination / Badge (単体) / Stepper / Empty state を追加し (依頼 D で受理・仕様定義は別 Task・正は `components.md` 共通事項)、新規 Component 定義工程への着手が Web部責任者判断 2026-08-03 で可 (`governance/owner-decisions.md` §15・Work Order 6 の 12 候補とは別) である旨を併記した。**不変**: §7 の他記述 (定義済み Component・実装は Semantic のみ参照・状態リスト・Button variant 語彙・PriceTag tone・Modal)、§1〜§6・§8〜§9・未確定事項の一覧、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の色値、rental-car / inbound の成果物。**新設していないもの**: Component 仕様・variant 語彙・状態固定リスト・新規 primitive/semantic トークン。D-8 (横並び結果カード) は components.md Card の未確定事項へ 1 件追加した (本書では追加しない)。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-40: 依頼元 (2026-08-03) の依頼 E「規定の不足」に対応 (受理と分類)。**未確定事項の一覧に 3 件追加**した — E-1 (画像を面とする場合の文字色とコントラスト確保の方法・scrim の要否/実現方式/評価方法。§2.1 の検証表は単色面のみ対象で `scrim`/`グラデーション`/`gradient` は travel 配下 0 件)・E-2 (会員限定で情報をマスクする表現の構成。`会員限定`/`マスク` は 0 件・マスクの視覚構成は DS/UI だが会員限定の業務条件・料金非公開の業務ルールは上流の未定義業務仕様に依存し DS で先行確定しない)・E-4 の (iii) 価格の単位表記 (1 名あたり等) の文言規則 (§8.1 は割引率のみ定義し単位表記は対象外・上流 content-principles.md §10 未決)。**§2.1** の検証表前文に本表が単色面のみを対象とし画像・グラデーション面は対象外で未定義である旨 (E-1) を補記。**§8.1** 末尾の Owner判断事項 (管理正本を §8 に置くか独立文書を新設するか) を、独立文書 (brand-content.md 等) を新設する方向を確定 (Q11・作成/中身/管理責務は別 Task・推測で新規正本を作成しない) へ改め、対応する未確定事項の行も方向確定へ更新。E-3 (施設名の省略規則) は §8J の UI・Implementation 下流課題分類を維持し DS 層で定めないこと、E-5 (繰り返し内 CTA) の Button Do の撤回はいずれも Owner 判断として governance/owner-decisions.md §16 に記録 (E-5 の components.md 反映は同 Task の components.md 変更履歴)。**不変**: §1〜§7・§9、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の色値、Component の実装要件、rental-car / inbound の成果物。**行っていないもの**: brand-content.md の新規作成・§8J 分類の変更・依頼元暫定実装の追認・新規 primitive/semantic トークン。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-36: 依頼元の依頼 D-6「ボトムシート / アンカー付きポップオーバーの定義追加」に対応。**§7.1「Modal の表示形態 (form)」を新設**し、form 軸 = drawer (既定) / sheet / popover の 3 値を定義 (実装基盤は drawer 単一を維持・第3の Modal 実装基盤を導入しない・popover は同一基盤上の表示形態で第3基盤に当たらない = governance/owner-decisions.md §17・form は variant 語彙とは別軸)、配置規則 (sheet = 下端貼付き全幅・上端2隅角丸 `radius.overlay` / popover = 基準要素起点で下方余地なしなら上反転・基準要素が必要 / drawer = 不変)、切替規則 (`{breakpoint.lg}` 1024px 未満 = sheet・以上 = popover)、backdrop (`color.overlay.backdrop`) を 3 形態共通で使用・遷移 (`motion.transition.*`) と影 (`shadow.*`) は既存 placeholder を参照するのみ、実装 API 名は未確定、および本節で定義しない事項 5 件 (a11y = §8K 下流課題 / 最小タップ領域 44px の spacing トークンは追加せず = §8K + WCAG AA 24px + spacing step11 不在 / sheet 最大高・popover 幅段階 = 依頼元固有値・未実査 / ADR 未発行 / oxlintrc・Modal.jsx はトラッキング対象外) を記載。**§5** の角丸を 3→4 系統へ (`radius.overlay` 追加)。**§2 表**に `color.overlay.backdrop` 行を追加。**未確定事項の一覧**に 3 件追加 (form の a11y・最小タップ領域 44px の spacing トークン・sheet 最大高/popover 幅段階)。**不変**: §1〜§4・§6・§8〜§9 の他記述、§7 の既存 Modal 記述 (drawer 統一・centered dialog deprecated・移行未決)、既存 token の値・参照先・`$status`・`$meta.version`・version、`shadow.*` / `motion.transition.*` の placeholder、rental-car / inbound の成果物。**追加した token**: semantic `radius.overlay` (`{radius.lg}` 参照・placeholder)・`color.overlay.backdrop` (primitive `blackAlpha.45` 参照・placeholder)、primitive `color.palette.blackAlpha.45` (`rgba(0,0,0,0.45)`・placeholder・暫定値)。追加した semantic トークンの参照はすべて既存 primitive で解決 (未解決 0・循環 0)。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-42: 依頼元 (2026-08-04・DS-REQUEST「セクション間余白の規定と 36px 段」) に対応 (受理と分類)。**未確定事項の一覧を更新**した — セクション間・ブロック間の余白の用途 semantic トークンと 36px 段 (`spacing.9`) の行を追加 (Web部責任者判断 2026-08-04 で「セクション間」のみ用途トークン化・`spacing.9` = 2.25rem を `8` と `10` の間へ `$status = bound` で追加する方向を確定・他 2 区分据置・実追加は別 Task・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §18)、既存の 44px の spacing トークンの行に、Web部責任者判断 2026-08-04 で 44px 段は §7.1 の現状 (トークンを追加せず) を維持する (追加しない・現状維持) 旨を追記 (§7.1 本体は不変)。**不変**: §1〜§9 の本文 (§4 スペーシング本体を含む)、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の spacing スケール (`spacing.9` は未追加)、位置用途 semantic トークン (未追加)、Component の実装要件、rental-car / inbound の成果物。**行っていないもの**: `spacing.9`・位置用途トークンの実追加・§4 の改訂・`governance/naming-rules.md` の新規作成・依頼元暫定実装の追認。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。改訂着手の設計承認は取得していない (§9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-43: 依頼元 (2026-08-04・依頼A + 判断点7) に対応 (受理と分類)。**未確定事項の一覧に 2 件追加**した — 会員限定 (有料会員限定) ラベルをカテゴリラベルと区別するか (🚧 方向確定 = 区別する・手段 = 面色使い分け 基本 neutral / 特集 accent / 例外 inverse・既存トークン範囲・実定義は別 Task・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §19)・会員種別語 (無料 / 有料会員) の表記管轄 (❓ コンテンツ表記規則の管轄・管理正本の所在 = design.md §8 系集約か独立文書新設かは Task 009-45 が扱う論点・本書で確定しない)。**不変**: §1〜§9 の本文 (§2.1 面色規則・§8 系を含む)、既存 token の値・参照先・`$status`・`$meta.version`・version、`color.text.onAccent` (既 `bound`)、primitive の色値、Component の実装要件、rental-car / inbound の成果物。**行っていないもの**: 会員限定ラベルの用途トークン・区別規則の実定義・`Card.slot.badge` 規範規則の変更・新色値/新面色用途の追加・`brand-content.md` の新規作成・依頼元実装の追認。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。改訂着手の設計承認は取得していない (§9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-44: 依頼元 (2026-08-04・依頼B + 判断点2/4) に対応 (受理と分類)。**未確定事項の一覧を更新**した — バッジ/ラベルの白文字非準拠運用 (割引率 `#C8912C` 面/白 14px・小サイズ campaign accent 面/白 12px) の扱いの行を追加 (🚧 方向確定 = 非操作の点的ラベル + campaign accent/scheme 逆色面 に限り白文字を例外として許容する方向・サイズ/ウェイト不問・AA 未達明示・白文字成立面は `surface.inverse` の 1 面のみ・実規則化は別 Task・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §20)、既存の「`#C8912C` 面上の白文字指示の解消」行 (§13/c1) と「campaign accent 面上の濃色背景の追加要否」行 (b2) に Task 009-44 の例外許容方向 (§20) を追記 (b2 と併存・b2 は保留)。**不変**: §1〜§9 の本文 (§2.1 の面色・コントラスト規則 = 白文字禁止・(i)(ii) 代替・逆色面 `color.text.strong` 固定 を含む)、§13 の記述、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の色値、Component の実装要件、rental-car / inbound の成果物。**行っていないもの**: §2.1・components.md の面色規則の実緩和・例外条項の実追加・新規 primitive/面色用途トークンの追加・b2 実色値の発明・依頼元実装の追認。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。改訂着手の設計承認は取得していない (§9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-45: 依頼元 (2026-08-04・判断点5 + DS-REQUEST「割引率の表記規則 (§8.1)」) に対応 (受理と分類)。**未確定事項の一覧を更新**した — 割引率の表記の基本形 (§8.1) の `-NN%` → `NN%OFF` への変更の行を追加 (🚧 方向確定 = 基本形変更・マイナス付与規則撤回・全角 `％`/`▲` 禁止維持・半角 `%`・§8.1 本体の実改訂は別 Task・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §21)、「上限値・最大条件」行に「最大NN%OFF」の使用条件を定める方向 (§21) を追記 (上限値/算出は据置)、「管理正本」行を §16 の `brand-content.md` 新設方向の撤回・design.md §8 系集約方向 (§21) へ更新、「価格の単位表記」行の管理正本も同方向転換へ更新。**不変**: §1〜§9 の本文 (**§8.1 本体 L287-338 = 基本形 `-NN%`・符号・「最大」条件・管理正本 L338 を含む**)、§8 (管理正本の記述)、§16 本体・README、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の色値、Component の実装要件、rental-car / inbound の成果物。**行っていないもの**: §8.1・§16・README の実改訂・`brand-content.md` の新規作成・割引率の算出式/端数処理/上限値の決定・依頼元実装の追認。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。改訂着手の設計承認は取得していない (§9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-46: 依頼元 (2026-08-04・§4.5 + 判断点6) に対応 (受理と分類)。**未確定事項の一覧に 1 件追加**した — select の未選択値 (プレースホルダ相当) への `color.text.muted` 使用 (🚧 方向確定 = select の未選択値のみ `color.text.muted` (`#9e9e9e`・≈2.7:1) を例外許容・AA 未達明示・通常 `input` / `textarea` の placeholder は gray.700 維持・§2.3 への例外条項の実規則化は別 Task・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §22)。**不変**: §1〜§9 の本文 (**§2.3 本体 L154-163 = `color.text.muted` の流用禁止・選択前 `option` → `color.text.placeholder` を含む**)、既存 token の値・参照先・`$status`・`$meta.version`・version (`color.text.placeholder` / `muted` は `bound`)、primitive の色値、Component の実装要件、rental-car / inbound の成果物。**行っていないもの**: §2.3 の実改訂・muted 流用禁止規則の実緩和・トークンの変更・依頼元の未選択値 muted 使用/ラベル gray.700 変更の追認。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。改訂着手の設計承認は取得していない (§9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-10 | 品質基準の記述の是正 (Issue #152・検出元 = PR #150 独立レビュー issuecomment-5238944304 / 訂正 issuecomment-5239063979)。§「品質基準」[事実] 行の本文 `#424242` のコントラスト値を「≈9.7:1」→「≈10.0:1」(白背景・実測 10.05:1) へ是正し、括弧書き「(AAA 7:1 は未達)」の帰属を是正した — 本文 `#424242` は 10.05:1 で AAA 7:1 を満たすため「(AAA 7:1 も満たす)」と明記し、AAA 7:1 未達の注記を主色 royal `#2C50C8` (実測 6.80:1)・副色 indigo `#4845D4` (実測 6.82:1) に限定した (旧記述は「いずれも…AAA 7:1 は未達」で本文行に不整合。本行が自称する 9.7:1 でも 9.7 > 7 のため本文は当初から AAA 7:1 を満たしていた)。「いずれも AA 適合」の結論は不変 (3 色とも 4.5:1 以上)。コントラスト比は WCAG 2.x 標準式で相対輝度から実測した記録であり、適用規格・達成レベルの正式確定・適合判定・適合宣言は行わない。**不変**: 本文行の色値 (`#424242` / `#2C50C8` / `#4845D4`)・royal / indigo の値 (≈6.8:1)・§1〜§9 の他記述・§2 表・未確定事項の一覧・token の値/参照先/`$status`/`$meta.version`・primitive の色値・Component の実装要件・rental-car / inbound の成果物。**Task 009-48〜009-56 (ラベル・タグ定義) とは独立**した是正であり、当該バッチ (PR #149 / #150 / #151) の変更行ではない既存記述を対象とする。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-10、本件について明示取得。必要レビュー主体 = Web部レビュー担当者 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8・§10。事実記述の是正であり意匠・設計判断・token 値に及ばない)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
