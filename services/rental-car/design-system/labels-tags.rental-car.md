# ラベル・タグ定義 — 国内レンタカー (rental-car)

- 種別: DS 成果物 (Component 仕様の付属定義)
- 状態: Draft
- 作成日: 2026-08-19
- 継承元: 国内宿泊 (travel) 「ラベル・タグ定義シート」(2026-08-10)。器の考え方とカテゴリ体系 A〜H をそのまま継承し、レンタカーの用途へ割り当てた
- 参照トークン: `semantic.rental-car.json` のみ

## 1. 器の統一

結論: 器 (高さ・左右余白・文字サイズ・行高・角丸・ウェイト) は全カテゴリ共通に固定する。器が決まれば、カテゴリごとの判断は面色と文字色だけに閉じる。

| 項目 | トークン | sm | md |
| --- | --- | --- | --- |
| 高さ | `label.height.sm` / `md` | 20px (`spacing.5`) | 24px (`spacing.6`) |
| 左右余白 | `label.paddingInline.sm` / `md` | 8px (`spacing.2`) | 12px (`spacing.3`) |
| 文字サイズ | `label.fontSize.sm` / `md` | 12px (`typography.size.xs`) | 14px (`typography.size.sm`) |
| 数字 (A のみ 1 段上) | `label.numberSize.sm` / `md` | 14px (`typography.size.sm`) | 16px (`typography.size.md`) |
| 行高・配置 | `label.lineHeight` | 1 に固定・上下中央 (上下余白は指定しない) | 同左 |
| 角丸 | `label.radius` (= `radius.badge`) | 4px | 同左。押せるものだけ `radius.action` (pill) |
| ウェイト | `label.weight.emphasis` / `neutral` | 面のあるラベル 700 / 中立タグ (D) 400 | 同左 |

2 段を持つのは A (割引率) だけである。他カテゴリは 12px 単一で運用する。

- [事実] 上記の器トークン (`label.*` 12 件) は **Task 009-63 で `semantic.rental-car.json` に定義済み**である。仕様書の数値のみで運用していた状態は解消した。いずれも既存の `spacing` / `typography.size` / `typography.fontWeight` / `radius` への割当であり、新しい数値は追加していない
- [決定] **押せるものだけ pill**。操作可能なバッジは badge ではなく action 系 Component として扱う (その場合の角丸は `radius.action`)

## 2. カテゴリ定義

結論: 8 カテゴリ。1 カテゴリに 2 つ以上の意匠を作らない。カテゴリをまたいで意匠を揃えない。

### A 割引率

- 意匠: 逆色面 `color.label.discount.surface` (= `color.scheme.main.inverse` `#C8912C` / 副色文脈は `color.scheme.sub.inverse` `#C8B12C`) + 白文字 `color.label.discount.text`。数字は `font.price` 700 + tabular-nums で 1 段上
- 固定 = 面・文字色・書体・角丸。箱ごとに選べる = サイズ・表記・余白
- 用途: 卸価格の割引率。**表記規則の正は [design.md](design.md) §8.1** (基本形 `NN%OFF`・数字は `%OFF` より 1 段上・半角/整数/先頭ゼロなし・表示しない条件 4 件・表示成立条件)。幅が取れないときのみ「NN%OFF」の 1 サイズ
- 写真の上でも意匠を変えない (スクリムを敷かない)。**写真の上に置けるのは A 割引率と C カテゴリ・特集 (C1 企画名 / C2 販売条件)** である (判断 F-7・2026-09-07・[../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §29-3)。C は写真の上・有色面の上では枠線を引かず面のみで分離する (本書 C1・[design.md](design.md) §2.4)。他のカテゴリ (B / D / E / F / G / H) は写真の上に置かない
- 白文字のコントラストは **main `#C8912C` 上 2.78:1 / sub `#C8B12C` 上 2.15:1** で、両スキームとも通常テキスト 4.5:1 だけでなく、大きなテキスト 3:1 も満たさない (main 2.78 / sub 2.15 はいずれも 3 未満)。2 スキームは値が異なるため 1 行に束ねない
- ✅ これを成立させる例外条項は **[design.md](design.md) §2.4「A 割引率ラベルに限る白文字の例外」として明文化済み**である (Task 009-63・[../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。用途は **A 割引率ラベルに限り**、面は **scheme 逆色に限る** (campaign accent 面 + 白文字は例外に含めない)。サイズ・ウェイトは不問。**AA 未達を明示したうえでの許容であり、適合宣言ではない**。§25 の Does Not Authorize が「例外条項の明文化は未了」としていた状態は解消した
- ✅ 用途色トークン `color.label.discount.surface` / `text` は **Task 009-63 で定義済み**である

### B-1 会員種別 / 有料 (`membership.paid`)

- 意匠: 淡色面 + 同じ色相の濃色段文字。面 = `color.membership.paid.surface` (= accent 淡色段 `color.accent.campaignTint` `#F9CDBC`) / 文字 = `color.membership.paid.text` (= accent 濃色段 `color.accent.campaignInk` `🚧` 仮 `#8A2E11`・淡色面上 5.84:1 の概算)
- `🚧` **面の値 (`orange.100` `#F9CDBC`) は bound、濃色段 (`orange.800` `#8A2E11`) は仮色**である。面 + 文字の 4.5:1 成立は実色値確定後に検証する。**実色を発明しない**
- **accent を面として持つのは本カテゴリ (B 会員種別) のみ**である ([design.md](design.md) §2.4「accent の帰属」)。C カテゴリ・特集は accent をアイコン (点) として持つ
- サイズ: 12px 単一・bold (`label.weight.emphasis`)・器は共通 sm (A のような 2 段は設けない)
- 出現箱: ヘッダーナビ / トップのヒーロー / 検索結果カード / 車両・プラン行 / モバイルドロワー
- 文言は幅で切替 (1024px 未満「プライム限定」・以上「プライム」)
- 12px では accent 濃色面 + 白文字は使わない。**濃色段の実色値が確定するまでは、12px の代替の既定 (neutral dark 面 `color.surface.inverse` + `color.text.inverse` = 16.10:1) を用いる** ([design.md](design.md) §2.4 の代替規則)
- ✅ トークン `color.accent.campaignTint` / `campaignInk`・`color.scheme.{main,sub}.accentTint` / `accentInk`・`color.membership.paid.surface` / `text` は **Task 009-63 で定義済み** (いずれも `$status: placeholder` = 🚧 仮色を伝播)

### B-2 会員種別 / 無料 (`membership.free`)

- 意匠: B-1 と同じ型で色相だけを主色に変える。面 = `color.membership.free.surface` (= `color.scheme.main.tint` `#E8EDFB`) / 文字 = `color.membership.free.text` (= `color.scheme.main.ink` `#14224A`・13.21:1)。✅ トークンは **Task 009-63 で定義済み** (bound)
- ラベルは既定では出さない (無印 = 無料会員)。定義は残し、出す判断になった場合はこの定義に従う
- 役割は「会員になれば見られる」という誘導の印であり、ログイン後の会員限定情報には使わない
- 色の適用先は 2 箱のみ: (1) 卸価格の解放訴求ブロック (2) 価格のマスク表示
- 会員登録・ログイン導線は操作要素のため適用外 (Button の面色規定と衝突する)

### C1 企画名

- 意匠: 白面 `color.label.category.surface` (`#FFFFFF`) + 文字 `color.label.category.text` (`#212121`・16.10:1) + **アイコンのみ accent** `color.label.category.icon` (`#E4572E`・白面上 3.68:1)。面を accent で塗らない。器は共通 sm・ウェイトは `label.weight.emphasis` (700)
- 用途: 商品の所属 (タイムセール・特集企画)。アイコンは `fa-bolt`
- **白系の面 (`color.surface.default` `#FFFFFF` / `color.surface.subtle` `#F9F9F9`) の上に置く場合にのみ**、`color.label.category.border` (= `color.border.default` `#CCCCCC`) の枠線を `border.width.thin` (1px) で引く。白面が背景と同色・近似色になり面のみでは境界が生じないため (白 × 白 1.00:1・白 × `surface.subtle` 1.05:1・本 Repository で実測)。枠線は白面上 **1.61:1** で**非テキスト UI 要素の 3:1 に達しない** — 分離の補助であり、ラベルの識別は文字 (16.10:1) が担う。適合宣言は行わない
- 写真の上・有色面の上では**枠線を引かず**面のみで分離し、影・スクリムは使わない
- ✅ **accent の帰属は確定した** (Task 009-63・[../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。accent を**面**として持つのは B 会員種別のみ、**C は accent をアイコン (点) として持つ**。C の面は白で固定であり、旧「仮決定・面色は暫定 `🚧`」の状態は解消した
- ✅ 用途色トークン `color.label.category.surface` / `text` / `icon` / `border` は **Task 009-63 で定義済み**である。**旧記述の是正**: 旧版は「用途色トークンは追加しない。**国内宿泊 (travel) でも C 特集は据え置き**であり」と記載していたが、travel は Task 009-60 (2026-09-05・[../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §27) で `color.label.category` を確定しており、当該記述は**現在の事実に反していた**ため削除した
- 12px (`label.fontSize.sm`) でも**白面 × `color.text.strong` = 16.10:1 で成立する**ため、C には [design.md](design.md) §2.4 の代替 2 択 (neutral dark 面 / accent 淡色面) を要しない
- **C に campaign accent 面 + 白文字を用いない** — §2.4「A 割引率ラベルに限る白文字の例外」の対象は A 割引率ラベルであり C は対象外である
- `🚧` アイコンの**サイズ**は未定義である。`iconSize` の最小段は 16px で、器 sm (高さ 20px・文字 12px) に当てる値が本書・[design.md](design.md)・[components.md](components.md) のいずれにも無い (継承元の travel 側でも未定義)

### C2 販売条件

- 意匠: C1 と同一 (`color.label.category.*`)。区別はアイコンのみ (`fa-clock`)
- 用途: 価格の条件 (直前割)。C1 と性質が違うため 1 つの意匠に畳まず 2 区分で持つ
- 枠線・アイコンサイズの扱いは C1 と同一

### D1 車種クラス (`tag.neutral`)

- 意匠: 中立タグ = `color.tag.neutral.surface` (= `surface.muted` `#F5F5F5`) 面 + `color.tag.neutral.text` (= `text.body` `#424242`・9.22:1)・ウェイト `label.weight.neutral` (400。面ありラベルの 700 と区別)。✅ トークンは **Task 009-63 で定義済み** (bound)
- D1〜D3 は同じ器で、区分は順序で読ませる
- 用途: 1 台に必ず 1 つだけ (排他)。検索の絞り込み条件と 1 対 1。タグ列の先頭に置く

### D2 装備

- 意匠: D1 と同じ器。0 個から多数の列挙
- 用途: 車両に「ある」もの (カーナビ・ETC・バックカメラ・AT)
- タグは真偽の要約だけを担う。値を持つ情報 (排気量・燃費・給油の条件) は表に残す

### D3 利用条件

- 意匠: D1・D2 と同じ器。順序だけ装備より前に置く
- 用途: 利用者の行為の可否 (禁煙車・乗り捨て可・ペット同乗可・送迎あり)
- 境界は「あるか」対「してよいか」。可否判断に直結するため、色ではなく順序で優先を示す

### D4 格付け

- 廃止。グレードの定義が事業区分に存在しないため表示ごと廃止する
- 廃止するのは格付けのみで D1〜D3 は対象外。tint 面は B 無料会員の専用になる

### E1 在庫僅少 (`label.stock`)

- 意匠: 面を持たない文字のみ・12px bold。色は `color.label.stock` (= `state.error` `#D23A3A`) を参照。✅ トークンは **Task 009-63 で定義済み** (bound)
- 置き場所は情報欄の価格の直上。**白背景に限る** (白背景 4.77:1・本 Repository で実測)。写真の上には置かない (= [design.md](design.md) §2.4 の検証表の対象外)
- D との見分けは面の有無、A との見分けは置き場所

### E2 満車・受付終了

- 方向のみ確定: ラベルを増やさず CTA の非活性状態に集約する (価格・写真はそのまま残す)
- `🚧` 面色・文字色・高さ・形・文言は未確定。DS に Button の disabled 定義がないため、そちらが先に必要
- 写真を opacity で落とす旧実装は採らない

### F 予約条件

- 意匠: 面を持たないテキストの行。バッジの器に乗せない。**規則の正は [design.md](design.md) §8.2**
- スロット構造: (1) キャンセル条件 (必ず 1 つ出る 2 値: 無料キャンセル / キャンセル不可) (2) 支払い (あるものだけ: カード決済可・現地決済可・事前払い) (3) 特典 (あれば: ポイント付)
- 同じ意味の情報は値が変わっても常に同じ位置に出す
- 4 役の色: 得 = 主色 (`🚧` 暫定。リンクと同値のため「押せないのにリンクに見える」論点は未解決) / 損 = `state.error` / 中立 = `text.mutedStrong` / 操作 = `text.link`
- 得・損の判定: 問い 1 = 利用者が選べるか (選べる = 中立で終了。支払い手段はここ)。問い 2 = 素の予約と比べ (1) 支出 (2) 取り消し・変更の自由 (3) 時間の拘束 (4) 人数・人選び の 4 軸のいずれかが緩む = 得 / 厳しくなる = 損
- アイコンは意味ごとに固定 (`circle-check` / `circle-xmark` / `credit-card` / `yen-sign` / `coins`)。アイコンに意味色は当てず文字色に従う
- この行に車種クラス (D) や企画ラベル (C) を混ぜない

### G 写真枚数

- 意匠: `surface.inverse` 面 + `color.text.inverse` の白文字 (`#212121` 上 16.10:1)・角丸は他カテゴリと同じ `label.radius` (= `radius.badge` 4px)。非操作のラベルに `radius.action` (pill) を使わない (操作要素との誤認防止)
- 用途: 車両写真の枚数。トークンの追加なし

### H 適用範囲

- 適用: UI 部品・カード・ラベル全般 (A〜G)
- 適用外: PR 帯・特集帯・企画のキービジュアル・支給バナー・テーマタイル
- 適用外でもカラーは厳守する。AA・44px・代替テキスト・色だけで伝えないは下限
- **詳細の正は [design.md](design.md) §8.3** (適用外で外せる項目 = 書体・文字サイズ・ウェイト・器の形・傾き／グラデーションは審査対象／新規制作時にどちらの段かを先に宣言し、宣言がなければ適用とみなす)

## 3. Do / Don't

結論: 判断を器へ戻さず、面と文字の色だけで区別する。

- Do: 器 (高さ・左右余白・角丸・ウェイト) は全カテゴリ共通。押せるものだけ pill (`radius.action`)
- Don't: カテゴリをまたいで意匠を揃えない。1 カテゴリに 2 つ以上の意匠を作らない
- Don't: 実装の `.cat-label` (92x25px 固定・三角の尾・分類色 #060 / #c90) は踏襲しない

## 4. 追加したトークン

結論: **旧版が「要追加 6 件」として挙げていた分は、Task 009-63 ですべて `semantic.rental-car.json` に定義した** (C カテゴリ・特集の用途色と accent の淡色段・濃色段を支える primitive 4 件を含む)。値は本 DS のファイルに独立して持ち、travel のファイルを参照・共有しない ([design.md](design.md) 独立性)。実色が未取得の 3 段は `$status: placeholder` として `🚧` を伝播させる。

`radius.badge` は従前から定義済み (`{radius.sm}` = 4px・`$status: bound`) であり、本表の対象ではない。

| 項目 | 追加したトークン | 件数 | 状態 |
| --- | --- | ---: | --- |
| `label.*` の器 | `height.sm` / `md`・`paddingInline.sm` / `md`・`fontSize.sm` / `md`・`numberSize.sm` / `md`・`lineHeight`・`radius`・`weight.emphasis` / `neutral` | 12 | bound |
| A 割引率 | `color.label.discount.surface` / `text` | 2 | bound (白文字は AA 未達を明示・§2.4 の例外) |
| B-1 / B-2 会員種別 | `color.membership.paid.surface` / `text`・`free.surface` / `text` | 4 | paid = placeholder `🚧` / free = bound |
| accent の淡色段・濃色段 | `color.accent.campaignTint` / `campaignInk`・`color.scheme.main.accentTint` / `accentInk`・`color.scheme.sub.accentTint` / `accentInk` | 6 | placeholder `🚧` |
| 同 (primitive) | `color.palette.orange.100` / `orange.800`・`coral.100` / `coral.800` | 4 | `orange.100` のみ bound・他 3 段は 🚧 仮色 |
| E1 在庫僅少 | `color.label.stock` | 1 | bound |
| D1〜D3 中立タグ | `color.tag.neutral.surface` / `text` | 2 | bound |
| C1 / C2 カテゴリ・特集 | `color.label.category.surface` / `text` / `icon` / `border` | 4 | bound (枠線は白面上 1.61:1 = 非テキスト 3:1 未達を明示) |

- [事実] semantic の追加は計 **31 件** (上表)。本 Task ではこのほかに面と文字色・リンク・文書レベル見出しの 8 件を追加しており、`semantic.rental-car.json` 全体では 39 件の追加・1 件の削除 (`radius.input`)・1 件の参照先変更 (`font.heading.h3Size`) となる ([design.md](design.md) 変更履歴)
- `🚧` **残る実査待ち**: accent 濃色段 (`orange.800` `#8A2E11`) とサブスキーム coral の 2 段の実色値。B-1 の淡色面 + 濃色文字 (5.84:1) は概算であり、成立検証は実色値確定後に行う。**実色を発明しない** (確認方法・個別確認主体 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §14)
- `🚧` **残る未定義**: C カテゴリ・特集ラベルのアイコンのサイズ (C1)・E2 満車・受付終了の意匠値 (Button の disabled 定義が先)・F 予約条件「得」の文字色とリンクの見分け

## 5. 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-08-19 | 初版。国内宿泊の定義シート (2026-08-10) を継承し A〜H をレンタカーの用途へ割り当て。D4 廃止・B-2 は既定非表示・要追加トークン 5 件を明示 | Claude Design |
| 2026-08-20 | 本 Repository へ新設 (0.3.0-draft)。あわせて記述是正 3 件: (1) §1 角丸行の「`radius.badge` 未定義のため `radius.sm` で代用」を削除 (`semantic.rental-car.json` に `{radius.sm}` = 4px・`$status: bound` で定義済のため事実に反する)。(2) C1 見出しの `label.category` を除去し、用途色を追加しない旨を明記 (未定義かつ国内宿泊でも C 特集は据え置き)。(3) §4 要追加トークン表から `radius.badge` を外し、未定義の `tag.neutral` を追加 (計 5 件は不変) | Claude Code |
| 2026-08-20 | Task 009-57R の記述是正: PR [#156](https://github.com/tocoo/coocom-design-system/pull/156) コードレビュー ([issuecomment-5353729542](https://github.com/tocoo/coocom-design-system/pull/156#issuecomment-5353729542)) の指摘に対応。①A のコントラストを main 2.78:1 / sub 2.15:1 と個別に記載し、例外条項が本 DS では未明文化である事実と `label.discount` 未定義を明記した。②B-1 の面 `#F9CDBC` の「(確定)」を「仮色」へ是正した (§4 の「primitive に段がなく仮色」と矛盾していた)。③G 写真枚数の角丸を `radius.action` (pill) から `radius.badge` へ改めた (「押せるものだけ pill」と矛盾していた)。④F の中立色を `text.muted` から `text.mutedStrong` へ変更した。⑤§4 の結論文を是正し `label.discount` を追加して 6 件とした (旧文は 5 件のうち 4 件が travel でも未追加であるかのように読ませていたが、実際は 6 件すべて travel に実装済みである)。**不変**: 器の寸法・カテゴリ体系 A〜H・D4 廃止・B-2 の既定非表示・Do / Don't | Claude Code |
| 2026-09-07 | Task 009-63: 国内宿泊 (travel) の最新版 (Task 009-58〜009-62) の定義体系を適用 ([Issue #170](https://github.com/tocoo/coocom-design-system/issues/170)・記録 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。①§1 の器の表に**トークン列**を追加し、寸法を `label.*` (12 件・定義済み) への参照として書き換えた。②A の「例外条項は未明文化 `🚧`」を解消し [design.md](design.md) §2.4「A 割引率ラベルに限る白文字の例外」への参照へ、表記の 1 行を §8.1 への参照へ改めた。③B-1 を `color.membership.paid` 参照へ改め、**面 (`orange.100`) は bound・濃色段のみ仮色**であることを明記し、濃色段が確定するまで 12px は neutral dark 面を用いる旨を追記した。④B-2 / D1 / E1 / G を用途色トークン参照へ書き換えた。⑤**C1 の記述を是正**した — 旧「用途色トークンは追加しない。国内宿泊 (travel) でも C 特集は据え置きであり」は、travel が Task 009-60 (2026-09-05・同 §27) で `color.label.category` を確定しているため**現在の事実に反していた**。あわせて **accent の帰属を確定** (面 = B のみ / C はアイコン) し、白系の面の上での枠線 1px (`color.label.category.border`・白面上 1.61:1 = 非テキスト 3:1 未達を明示) を定め、`🚧` 2 箇所を解消した。C2 も同参照へ揃えた。⑥F を §8.2、H を §8.3 への参照へ揃えた。⑦§4 を「要追加トークン 6 件」から**「追加したトークン」**へ書き換え、semantic 31 件 + primitive 4 件の消し込みと残る実査待ち・未定義を明記した。**不変**: 器の寸法値・カテゴリ体系 A〜H・D4 廃止・B-2 の既定非表示・D1〜D3 の区分・E2 の方向・F のスロット構造と判定基準・Do / Don't | Claude Code |
| 2026-09-07 | Task 009-63R の記述是正: PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) コードレビュー ([issuecomment-5565532746](https://github.com/tocoo/coocom-design-system/pull/171#issuecomment-5565532746)) の指摘に対応。①A 割引率の白文字のコントラスト記述を「sub は大きなテキスト 3:1 も満たさない」から「**両スキームとも** 3:1 も満たさない」へ是正した (main 2.78:1 も 3:1 に達しないため、従前の記述は main が 3:1 を満たすと読めた)。**例外条項そのもの ([design.md](design.md) §2.4) は不変**。②D1 中立タグのコントラスト値を 5.68:1 から実測値 **9.22:1** へ是正した。③`color.text.placeholder` の追加取り下げ (§29 判断 C-5 の適用範囲変更) に伴い、§4 の件数を semantic 40 件 → **39 件**・本 Task の追加 9 件 → **8 件**へ是正した。**不変**: ラベル A〜H の器・用途色・角丸・書体・用途区分 | Claude Code |
| 2026-09-07 | Task 009-63R3: **判断 F-7 を追加取得**して A 節の記述を是正した (Web部責任者判断 2026-09-07・明示取得・記録 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §29-3)。契機は PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) コードレビュー 3 回目 ([issuecomment-5567573901](https://github.com/tocoo/coocom-design-system/pull/171#issuecomment-5567573901)) が検出した、[design.md](design.md) §2.4 の [決定]「写真の上・有色面の上では枠線を引かず面のみで分離する」(= C を写真の上に置く前提) と、本書 A 節の「**写真の上に置けるのは A だけ**」との食い違いである。判断は「**写真の上に置けるのは A 割引率と C カテゴリ・特集 (C1 / C2) の 2 カテゴリ**」で、他のカテゴリ (B / D / E / F / G / H) は写真の上に置かない。C は写真の上・有色面の上では枠線を引かず面のみで分離する (影・スクリムは用いない)。当該食い違いは**本 PR 以前から本書内に存在**した (`origin/main` の同ファイルで A 節・C1 節の双方を実測)。ラベル・タグ定義シート原本との照合は本 Repository では行っていない (**未検証**)。**不変**: A の意匠 (面・文字色・書体・角丸)・表記規則・コントラスト実測値、C1 / C2 の意匠と枠線規則、その他のカテゴリの記述、トークンの値・参照先・`$status` | Claude Code |
