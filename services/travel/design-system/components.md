# Component 仕様 — 国内宿泊予約 (travel)

- 種別: DS 成果物 (Component 仕様。R3-4)
- 状態: Draft (0.3.0-draft)
- 作成日: 2026-07-09
- Source of Truth: https://github.com/tocoo/coocom-design-system/blob/main/services/travel/design-system/components.md
- 参照トークン: `semantic.travel.json` のみ (primitive 直接参照は禁止 = 命名規則§1)

---

## 共通事項

- [事実] 状態の固定リスト: `hover / active / focus / disabled / loading / error / success` (命名規則§2)。追加は ADR 必須
- [事実] ボタン状態 (hover/active/disabled/focus) は宿泊で未取得 (follow-up #4 / TVL-0008)。全 Component の hover は「opacity 変化 (≈0.85)」を暫定参照とし `🚧 暫定` を付す。**ただしリンクの hover は対象外** — リンクは `design.md` §2.2 が定める色変更 (`{color.text.linkHover}`) を用い、`opacity` を状態表現に使わない (確定値のため `🚧 暫定` を付さない)
- [事実] フォーカスは `outline` ベースで `{color.focus.ring}` を使用 (命名規則§8)
- [事実] テキスト色は `{color.text.strong}` / `{color.text.body}` / `{color.text.mutedStrong}` / `{color.text.muted}` の4段。判読性を必要とする補助情報 (補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件) は `{color.text.mutedStrong}` (#616161・白背景 ≈6.2:1) を使用する。`{color.text.muted}` (#9e9e9e・白背景 ≈2.7:1) は通常テキストに求められる 4.5:1 に達しないため、判読性を要する情報には用いない。適用規格・達成レベルの正式確定・適合判定・適合宣言は本書では行わない (design.md §2)
- [事実] 上記4段は**明色面 (`{color.surface.default}` / `subtle` / `muted`) 用**である。inverse 面 (`{color.surface.inverse}` #212121) 上のテキストは `{color.text.inverse}` (主要文字・≈16.10:1) と `{color.text.inverseMuted}` (補助情報・≈6.01:1) の2段を使用する。`{color.text.inverseMuted}` (#9e9e9e) を明色面へ使用しない (白背景 ≈2.7:1)。`{color.text.mutedStrong}` を inverse 面へ使用しない (#616161 は #212121 上 ≈2.60:1)
- [事実] 面 (背景) として色を使う場合の許可される文字色・文字サイズ条件は面ごとに異なる。組み合わせ一覧・campaign accent を面として使用できる条件 ((a) `24px` 以上 (ウェイトを問わない) または (b) `20px` 以上かつ bold)・(a) (b) を満たさない場合 ((i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト) の代替規則・ウェイトの境界 (bold = `700` 以上／通常ウェイト = `700` 未満)・scheme inverse 面 (main `#C8912C` / sub `#C8B12C`) の文字色は `design.md` §2.1 が正。**`{color.text.onAccent}` の存在を理由にコントラスト確認を省略しない**
- [事実] 背景文脈は**明示的な tone / variant として選択できる**ようにする。背景色を検知して自動反転する仕様・コンポーネント内部の固定色だけで複数背景へ対応する仕様は採らない。禁止: primitive の直接参照 / 利用側による任意 HEX 指定 / global token のローカル再束縛を正式仕様とすること
- [事実] 角丸の用途トークンは `{radius.action}` (pill・操作要素)・`{radius.card}` (カード外形)・`{radius.badge}` (非操作のバッジ/ラベル) の3系統。非操作の割引率ラベル・状態バッジへ `{radius.action}` を使用しない (操作要素との誤認防止)。**操作可能なバッジは badge ではなく action 系 Component として扱う**
- [事実] 割引率のコンテンツ表記規則 (`-NN%`・符号・桁・端数処理の未確定・上限/異常値・表示成立条件) は `design.md` §8.1 が正。Component 仕様では表記規則そのものを再定義しない
- [事実] 見出しは**文書レベル (h1〜h6) と Component の見出しで同一トークン群 `{font.heading.*}` を共用する**。割当 (h1 2.5rem / h2 2rem / h3 1.5rem / h4 1.25rem / h5 1.125rem / h6 1rem・ウェイト `{font.heading.weight}` 700・行間 `{font.heading.lineHeight}` 1.3) は `design.md` §3.1 が正。Component が文書レベルの既定から外れる値を必要とする場合は**当該 Component の項へ明示的に記載する** (暗黙の上書きを認めない)。明朝 `{font.display.family}` は Display/Hero/特集/詳細施設名で明示的に選択する書体であり見出しの既定ではない
- [事実] リンクは色 `{color.text.link}` (= 主色・TVL-0011) に加え、状態ごとの文字色 (hover = `{color.text.linkHover}` / active = `{color.text.linkActive}` / visited = 専用色を設けず `{color.text.link}` を維持 / focus = `{color.focus.ring}` の `outline`) を使用する。**文中リンクには下線を付し、hover で下線を外さない**。standalone なリンク (カード全体リンク・ナビゲーション項目・パンくず) への下線の既定は未判定であり、状態ごとの文字色は対象を限定せず適用される。**リンクの状態表現に `opacity` を用いない** — 上記の「全 Component の hover は opacity 変化 (≈0.85) を暫定参照」からリンクを除外している。正は `design.md` §2.2
- [事実] 入力欄のプレースホルダ文字色は `{color.text.placeholder}` (#616161・白背景 ≈6.2:1) を使用する。`{color.text.muted}` (#9e9e9e・≈2.7:1) を流用しない。プレースホルダを必須項目・ラベル・エラーメッセージ・入力形式の説明の代替として用いない。正は `design.md` §2.3
- [事実] variant 語彙は `primary / secondary / ghost / campaign / text` の5語で確定 (GOV-0002)。語彙外の新設は ADR 必須。**travel の Button 実装は4語 (primary/secondary/ghost/text)**— campaign (accent 塗りボタン) は廃止 (TVL-0012)、accent はバッジ/割引ラベルの「点」専用 (Card badge)
- [事実] 未着手 Component: Select / Tabs / Toast / Table / Accordion — 実体データ皆無。本仕様に含めない

---

## Button

- ステータス: Draft
- 用途: 画面内の操作起点。予約導線の主 CTA・補助操作
- バリアント:
  - `Button.primary` — bg `{color.action.primary.bg}` (主色=ロイヤル) / 文字 `{color.action.primary.text}` / 角丸 `{radius.action}` (pill)
  - `Button.secondary` — 白CTA (名称は GOV-0002 で正式確定)。bg `{color.action.secondary.bg}` / 文字 `{color.action.secondary.text}` / pill。実測 (bg白・#212121・999px)
  - `Button.ghost` — 透明地 + `{color.text.strong}` 枠/文字。特集を見る等の低強調ナビ
  - `Button.text` — 透明地 + `{color.text.link}` (=主色・TVL-0011)。キャンセル・ログイン等の低強調テキスト操作
  - （campaign バリアントは廃止―TVL-0012。特集/セールの accent は Card のバッジ/割引ラベル等の「点」でのみ使用）
- 状態:
  - hover: 🚧 暫定 opacity 変化 (navy 暗色未抽出)。`Button.text` は文字色に `{color.text.link}` を用いるが、**その hover を `{color.text.linkHover}` と同一視しない** — `design.md` §2.2 はリンク要素の規則であり、ボタンの hover は共通事項の暫定参照に従う (hover 以外の状態一式は follow-up #4 で未取得)
  - active / disabled / loading: 🚧 未取得。focus は `{color.focus.ring}` outline を暫定適用
- Do / Don't:
  - Do: 1画面の主 CTA は `primary` 1つに絞る
  - Do: 実装は Semantic のみ参照する
  - Don't: accent (`{color.accent.campaign}`) をボタン塗りに使わない (バッジ/割引ラベル等の「点」専用・TVL-0012)
  - Don't: `--primary:#007bff` (Bootstrap 残骸) を参照しない
- 関連トークン: `color.action.*` / `radius.action` / `color.focus.ring` / `motion.transition.*`
- 未確定事項: 状態一式 (follow-up #4)・サイズ段階 sm/md/lg の実測なし (暫定 md のみ)

## Input

- ステータス: Draft 🚧
- 用途: フォームの単一入力 (テキスト/日付/数値)
- バリアント: `Input.default` のみ (実体不足のため最小定義)
- 構成: 入力値の文字色 `{color.text.body}` / プレースホルダの文字色 `{color.text.placeholder}` (#616161・白背景 ≈6.2:1。`design.md` §2.3 が正)
- 状態: error = 文字/枠 `{color.state.error}` 🚧 暫定 / focus = `{color.focus.ring}` outline 🚧 / disabled・success 🚧 未取得
- Do / Don't:
  - Do: エラーはテキストメッセージ併記 (色のみで伝えない = WCAG 2.2 AA / R9)
  - Do: プレースホルダは入力の補助にとどめ、必須項目・ラベル・エラーメッセージ・入力形式の説明の代替にしない
  - Don't: 未取得の必須表現 (アスタリスク等) を推測で固定しない
  - Don't: プレースホルダへ `{color.text.muted}` (#9e9e9e・白背景 ≈2.7:1) を使わない (判読性を要する文字であり 4.5:1 に達しない)
- 関連トークン: `color.border.*` / `color.state.error` / `color.text.body` / `color.text.placeholder` / `color.focus.ring`
- 未確定事項: 入力/エラー/必須・検証の実体一式 (follow-up #2)

## SearchForm

- ステータス: Draft
- 用途: 宿泊検索の起点フォーム (`_search_form.ejs` を正とする)
- バリアント: `SearchForm.default` (TOP/一覧共用)
- 構成: Input 群 + 主 CTA (`Button.primary`)。フィールド構成の確定は実装実査が必要 🚧
- Do / Don't:
  - Do: 検索実行 CTA は `Button.primary` を使用
  - Don't: フォーム構造を新規に再発明しない
- 未確定事項: フィールド構成・レイアウト実測 (要実査)

## Card (ResultCard)

- ステータス: Draft
- 用途: 検索結果の宿泊施設カード (8スロット構造)
- スロット (責務名 = 命名規則§2。8スロットへの対応付けは実査で確定 🚧):
  `Card.slot.media` / `title` / `meta` / `rating` / `price` / `badge` / `description` / `actions`
- バリアント: `Card.search` (検索結果) / `Card.plan` ❓ (実体は要実査)
- Do / Don't:
  - Do: 評価は `Card.slot.rating` に ReviewStars を配置 (宿泊固有)
  - Do: 価格は `Card.slot.price` に PriceTag を配置
  - Do: バッジは `Card.slot.badge` に集約
  - Don't: スロットを位置名 (top-left 等) で命名しない
- `Card.slot.badge` (割引率ラベル・状態バッジ・カテゴリラベル等の非操作ラベル) の規則:
  - 角丸: `{radius.badge}` 🚧 (暫定 sm 4px)。`{radius.action}` (pill) を使用しない — 操作要素との誤認防止
  - 面と文字色は文字サイズ・ウェイトで分岐する (境界の定義は `design.md` §2.1 が正)
    - **(a) `24px` 以上 (ウェイトを問わない)、または (b) `20px` 以上かつ bold (`700` 以上)**: 面 `{color.accent.campaign}` (#E4572E) + 文字 `{color.text.onAccent}` (≈3.68:1・大きなテキスト基準 3:1 のみ達成)
    - **上記以外** (= (i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト (`700` 未満)): 面 `{color.accent.campaign}` を使用しない。既定は 面 `{color.surface.inverse}` (#212121) + 文字 `{color.text.inverse}` (≈16.10:1)。accent は境界色・アイコン・点的装飾に限定する (**accent を文字色として明色面に置く方法はこの場合の代替にならない** = 明色面上 3.38〜3.68:1 で通常テキスト 4.5:1 未達)
  - Do: 割引率の表記は `design.md` §8.1 に従う (`-NN%`)。表示成立条件を満たさない場合はラベル自体を表示しない
  - Do: 状態・カテゴリを色のみで伝えずテキストを併記する (R9)
  - Don't: campaign accent 面上に (a) (b) を満たさない白文字 ((i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト) を置く
  - Don't: 縁取り・影でコントラスト不足を解決したものとして扱う
  - Don't: 評価色 (`{color.icon.rating}` = スキーム逆色) を割引ラベル・販促面へ流用する (用途境界は `design.md` §2.1)
  - Don't: バッジを操作可能にする場合に badge のまま扱う — action 系 Component として扱い `{radius.action}` を使用する
- 関連トークン: `radius.card` 🚧 / `radius.badge` 🚧 / `color.surface.default` / `color.surface.inverse` / `color.border.subtle` / `color.accent.campaign` / `color.text.onAccent` / `color.text.inverse` / shadow 🚧
- 未確定事項: 実px (角丸/影/余白)・8スロット対応付け・画像欠落時の fallback ❓ (Card 実装着手時) / バッジの実px (`radius.badge` は暫定 sm) 🚧 / 割引率の算出式・端数処理・上限値は上流未決 (`design.md` §8.1)

## PriceTag

- ステータス: Draft
- 用途: 価格表示 (数字 Bold 700 + tabular-nums + 円 + 補助テキスト)
- 構成:
  - 数字: `{font.price.family}` / `{font.price.weight}` (700・tabular-nums) / `{font.price.numberSize}` (1.25rem) / 文字色は tone 別 (下表)
  - 「円」: `{font.body.family}` / weight 600 相当 🚧 (スケール外実測。正規化 ❓)
  - 補助価格・価格条件注記 (税・人数・泊数等)・割引前価格: `{font.price.captionSize}` (0.75rem) / 文字色は tone 別 (下表)
- tone (背景文脈): `default` (明色面) / `inverse` (inverse 面)。**背景文脈は明示的に選択する**。`tone` は variant 語彙 (GOV-0002) とは別軸であり、variant 語彙への追加ではない。実装 API 名 (prop 名) は未確定 ❓ (下表の対応関係が正)

| 要素 | `tone="default"` (明色面) | `tone="inverse"` (inverse 面) |
| --- | --- | --- |
| 主要価格 (数字・「円」) | `{color.text.strong}` (#212121・白背景 ≈16.10:1) | `{color.text.inverse}` (#ffffff・#212121 上 ≈16.10:1) |
| 補助価格・価格条件注記・割引前価格 | `{color.text.mutedStrong}` (#616161・白背景 ≈6.19:1) | `{color.text.inverseMuted}` (#9e9e9e・#212121 上 ≈6.01:1) |
| その他の本文 | 用途に応じた default 面用 semantic (`{color.text.body}` 等) | 用途に応じた inverse 面用 semantic (`{color.text.inverse}` / `{color.text.inverseMuted}`) |

- 対応する面: `default` = `{color.surface.default}` / `subtle` / `muted`、`inverse` = `{color.surface.inverse}`
- Do / Don't:
  - Do: 税・条件の補助テキストを必ず併記できる構造にする
  - Do: 明色面では補助価格・価格条件注記・割引前価格の文字色に `{color.text.mutedStrong}` (#616161・白背景 ≈6.2:1) を使用する
  - Do: inverse 面では tone を `inverse` に切り替え、主要価格 `{color.text.inverse}` / 補助価格・価格条件注記・割引前価格 `{color.text.inverseMuted}` を使用する
  - Don't: 数字と単位を1つのテキストで固定しない (スロット分離)
  - Don't: 購買判断や内容理解に必要な補足条件へ `{color.text.muted}` (#9e9e9e・白背景 ≈2.7:1) を使用しない
  - Don't: inverse 面へ `{color.text.mutedStrong}` を使用しない (#616161 は #212121 上 ≈2.60:1)
  - Don't: 明色面へ `{color.text.inverseMuted}` を使用しない (#9e9e9e は白背景 ≈2.7:1)
  - Don't: primitive を直接参照する / 利用側で任意 HEX を指定する / global token のローカル再束縛を正式仕様として扱う
  - Don't: 背景色を検知して自動反転する仕様にする / コンポーネント内部の固定色だけで複数背景へ対応する
- 関連トークン: `font.price.*` / `color.text.strong` / `color.text.mutedStrong` / `color.text.inverse` / `color.text.inverseMuted` / `color.surface.default` / `color.surface.inverse`
- 未確定事項: 「円」weight 600 の正規化 ❓ / tone の実装 API 名 (prop 名) ❓ / `{color.surface.inverse}` 以外の暗色面での tone 適用可否 ❓ (検証済みは #212121 上のみ)

## ReviewStars

- ステータス: Draft 🚧
- 用途: 星評価表示 (宿泊固有。表示のみ)
- 構成: 星アイコン×5 + 数値スコア。アイコンは **Font Awesome 6 の star** (TVL-0006)
- Do / Don't:
  - Do: 数値スコアを併記 (色・形のみで伝えない = R9)
  - Don't: 他サービスへ流用しない
- 関連トークン: `{icon.reviewSize}` (bound) / `{color.icon.rating}` (bound・各スキームの逆色 #C8912C/#C8B12C = TVL-0011)
- 未確定事項: 星の実寸 (要実査。検討トリガー: ReviewStars 実装着手時)

## Header

- ステータス: Draft
- 用途: 全ページ共通ヘッダー。構成: ロゴ / ナビゲーション / 会員導線。実測: bg 白・高さ約 41px
- 状態: sticky 時は `{elevation.sticky}`
- Do / Don't:
  - Do: bg は `{color.surface.default}`
  - Don't: 新規デザインでヘッダーを複数系統作らない
- 未確定事項: 内部ナビ構成の実査

## Footer

- ステータス: Draft
- 用途: 全ページ共通フッター
- Do / Don't:
  - Do: 新系 (`lp/_footer`) を正とし、新規制作はこれに揃える 🚧 暫定
  - Don't: 旧系フッターを新規ページへ複製しない
- 未確定事項: 旧系の廃止時期

## Breadcrumb

- ステータス: Draft
- 用途: 階層ナビゲーション
- 構成: リンク (`{color.text.link}` = 主色・TVL-0011) + 区切り + 現在地 (`{color.text.muted}`)
- Do: 現在地はリンク化しない
- リンク部分の状態ごとの文字色は `design.md` §2.2 に従う (hover = `{color.text.linkHover}` / active = `{color.text.linkActive}` / visited = `{color.text.link}` を維持 / focus = `{color.focus.ring}` の `outline`)
- 未確定事項: パンくずのリンクへ下線の既定を及ぼすかは未判定 (`design.md` §2.2 が定めた**下線**の既定は文中リンクを対象とし、パンくずは領域とレイアウトでリンクが成立する standalone 側にあたる)

## Modal / Overlay

- ステータス: Draft
- 用途: 重ね合わせ UI
- 実装基盤: **最終的に drawer へ全面統一**。新規は drawer で実装。centered dialog は deprecated (移行期間中は併存)。現在の方針根拠は `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**)。`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認のため、現存する正本・現在の仕様根拠として扱わない
- 移行ロードマップ: **未決**。移行対象・順序・期限・完了条件・具体的なロードマップはいずれも決定されていない。決定する場合は外部実装 Repository の実査が先行する (`governance/owner-decisions.md` §11)
- 状態: open/close 遷移は `{motion.transition.*}` 🚧
- Do / Don't:
  - Do: z 軸は `{elevation.overlay}` / `{elevation.modal}` を使用
  - Don't: 第3のモーダル基盤を導入しない
- 未確定事項: 既存 centered dialog の移行対象・順序・期限・完了条件は**未決**。`TVL-0007` で管理されているとは認定しない (ADR 正本が Repository 内に不在・historical provenance 未確認)。詳細は `governance/owner-decisions.md` §11

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-09 | 0.3.0-draft: 独立DS再構築。GOV-0002 (variant 語彙)・TVL-0006 (FA6)・TVL-0007 (drawer統一)・TVL-0001〜0003 (rem/4px/テキスト2段) を反映 | Claude Design (Builder) |
| 2026-07-28 | Task 009-28R: Modal / Overlay 節の `TVL-0007` への参照・委任表現を補正 (3 箇所)。①実装基盤 = 「drawer に全面統一 (TVL-0007)」を「最終的に drawer へ全面統一」へ改め、現在の方針根拠が `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**) であることと、`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認のため現存する正本・現在の仕様根拠として扱わないことを明記。あわせて「移行期間限定」を「移行期間中は併存」へ改め、現在判断の内容と一致させた。②「移行ロードマップは TVL-0007 参照」という**存在しない委任先にロードマップが存在すると読める表現を削除**し、移行対象・順序・期限・完了条件・具体的ロードマップがいずれも未決であること、決定する場合は外部実装 Repository の実査が先行することへ補正。③未確定事項 = 「既存 centered dialog の移行対象・順序 (TVL-0007 で管理)」を、移行対象・順序・期限・完了条件が未決であり `TVL-0007` で管理されているとは認定しない旨へ補正。**現行仕様そのものは不変** (最終的な drawer への統一・新規は drawer で実装・centered dialog の deprecated・移行期間中の併存・第3の Modal 実装基盤を導入しないはいずれも維持)。判断日 (2026-07-27) と本反映日 (2026-07-28) は別の事象として区別している。本工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-07-28、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。Modal / Overlay 節の 用途・ステータス・状態 (`{motion.transition.*}` 🚧)・Do (`{elevation.overlay}` / `{elevation.modal}`)・Don't (第3のモーダル基盤を導入しない)、他 Component の仕様、token の値・参照・`$status`・`$description`・`$note`、version・正式 Status、Modal の具体的なライブラリ・モジュール・DOM 構造、open／close・focus・scroll lock・backdrop・dismiss 等の具体挙動、rental-car / inbound の成果物は不変。3DS 横断 Q9 の未決状態・`TVL-0007` の historical provenance 未確認・`alignment-blocking-facts-resolution-plan.md` §8L の R-D 分類は変更していない。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-33: 共通事項にテキスト色 4 段 (`{color.text.strong}` / `{color.text.body}` / `{color.text.mutedStrong}` / `{color.text.muted}`) の使用ルールを [事実] として 1 行追加した。判読性を必要とする補助情報 (補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件) は `{color.text.mutedStrong}` (#616161・白背景 ≈6.2:1) を使用し、`{color.text.muted}` (#9e9e9e・白背景 ≈2.7:1) は通常テキストに求められる 4.5:1 に達しないため判読性を要する情報には用いない。適用規格・達成レベルの正式確定・適合判定・適合宣言は本書では行わない。PriceTag の構成行を「補助価格・価格条件注記 (税・人数・泊数等)・割引前価格」へ改め文字色を `{color.text.mutedStrong}` へ変更し、Do 1 行・Don't 1 行・関連トークン行を追加した。**不変**: Button / Input / SearchForm / Card / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、PriceTag の用途・ステータス・数字と「円」の構成・「円」weight 600 の未確定事項、Breadcrumb 現在地の `{color.text.muted}`、トークンの値・参照先・`$status`、primitive の色値、version 表記、UI 構造・Component API・DOM 構造、rental-car / inbound の成果物。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-34: **共通事項に 5 行追加**した。①テキスト 4 段は明色面用であり inverse 面は `{color.text.inverse}` (主要文字) / `{color.text.inverseMuted}` (補助情報) の 2 段を使うこと (`{color.text.inverseMuted}` を明色面へ・`{color.text.mutedStrong}` を inverse 面へ使用しない) ②面と文字色の組み合わせ条件 (campaign accent を面として使用できるのは (a) 24px 以上または (b) 20px 以上かつ bold・ウェイトの境界は bold = 700 以上／通常ウェイト = 700 未満・scheme inverse 面は main `#C8912C` / sub `#C8B12C` を個別に扱う) は `design.md` §2.1 が正であり `{color.text.onAccent}` の存在を理由にコントラスト確認を省略しないこと ③背景文脈は明示的な tone / variant として選択し、背景色検知による自動反転・内部固定色のみでの複数背景対応・primitive 直接参照・任意 HEX 指定・global token のローカル再束縛を採らないこと ④角丸の用途トークン 3 系統 (`{radius.action}` / `{radius.card}` / `{radius.badge}`) と非操作ラベルへ pill を使わないこと・操作可能なバッジは action 系として扱うこと ⑤割引率の表記規則は `design.md` §8.1 が正であること。**Card (ResultCard)** に `Card.slot.badge` の規則を追加した — 角丸 `{radius.badge}` 🚧、面と文字色の文字サイズ・ウェイト分岐 ((a) 24px 以上 (ウェイトを問わない) または (b) 20px 以上かつ bold = `{color.accent.campaign}` 面 + `{color.text.onAccent}`／それ以外 = (i) 20px 未満のすべてと (ii) 20px 以上 24px 未満かつ通常ウェイトを含み、campaign accent を面として使わず既定は `{color.surface.inverse}` 面 + `{color.text.inverse}`)、Do 2 行 (割引率表記は `design.md` §8.1 に従い表示成立条件を満たさない場合はラベル自体を表示しない・色のみで伝えない)、Don't 4 行 ((a) (b) を満たさない文字への白文字・縁取り/影による代替・評価色の販促流用・操作可能なバッジを badge のまま扱うこと)。関連トークン行・未確定事項行も更新した。**PriceTag に tone (背景文脈) を追加**した — `default` (明色面) / `inverse` (inverse 面) の 2 値、要素 3 種 (主要価格・補助価格/価格条件注記/割引前価格・その他の本文) × tone 2 値の対応表、対応する面の対応関係、Do 1 行 (inverse 面での tone 切替)、Don't 4 行 (inverse 面へ `{color.text.mutedStrong}`・明色面へ `{color.text.inverseMuted}`・primitive 直接参照/任意 HEX/ローカル再束縛・背景色検知による自動反転と内部固定色のみでの対応)、関連トークン行、未確定事項 2 件 (tone の実装 API 名・`{color.surface.inverse}` 以外の暗色面での適用可否)。構成行 2 件の文字色指定を tone 別 (下表) 参照へ改め、既存 Do 1 行の冒頭に「明色面では」の限定を補った。`tone` は variant 語彙 (GOV-0002) とは別軸であり variant 語彙への追加ではない。実装 API 名 (prop 名) は未確定として扱う。**不変**: Button / Input / SearchForm / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、Card のスロット責務名・バリアント・既存 Do/Don't、PriceTag の用途・ステータス・数字と「円」の構成・「円」weight 600 の未確定事項・既存 Do 1 行と Don't 2 行、共通事項の既存 6 行、token の値・参照先・`$status`、primitive の色値、version 表記。**作成していないもの**: 新規 Component (badge は既存の `Card.slot.badge` の規則として記載)、画面制作側の JSX / CSS / 生成バンドルの変更、価格算出ロジック。適用規格・達成レベルの正式確定・適合判定・適合宣言は本書では行わない。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。改訂着手の設計承認は取得していない (同 §9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-35: **共通事項に 3 行追加**した。①見出しは文書レベル (h1〜h6) と Component で同一トークン群 `{font.heading.*}` を共用し、割当 (h1 2.5rem / h2 2rem / h3 1.5rem / h4 1.25rem / h5 1.125rem / h6 1rem・ウェイト `{font.heading.weight}` 700・行間 `{font.heading.lineHeight}` 1.3) は `design.md` §3.1 が正であること、Component が既定から外れる値を必要とする場合は当該 Component の項へ明示記載すること (暗黙の上書きを認めない)、明朝 `{font.display.family}` は明示的に選択する書体であり見出しの既定ではないこと。②リンクは色に加え状態ごとの文字色 (hover = `{color.text.linkHover}` / active = `{color.text.linkActive}` / visited = 専用色なしで `{color.text.link}` 維持 / focus = `{color.focus.ring}` outline) を使用し、文中リンクには下線を付し hover で下線を外さないこと、standalone なリンク (カード全体リンク・ナビゲーション項目・パンくず) への下線の既定は未判定で状態ごとの文字色は対象を限定しないこと、リンクの状態表現に `opacity` を用いず共通事項の暫定参照から除外していること。③プレースホルダ文字色は `{color.text.placeholder}` (#616161・≈6.2:1) を使用し `{color.text.muted}` (#9e9e9e・≈2.7:1) を流用しないこと、必須項目・ラベル・エラーメッセージ・入力形式の説明の代替に用いないこと。**共通事項の既存 1 行を改訂**した — 「全 Component の hover は opacity 変化 (≈0.85) を暫定参照とし `🚧 暫定` を付す」に**リンクの hover を対象外とする除外を追記**し (リンクは `design.md` §2.2 の色変更を用い確定値のため `🚧 暫定` を付さない)、あわせて `follow-up #4` の範囲との対応を保った。**Button** の hover 行に、`Button.text` は文字色に `{color.text.link}` を用いるがその hover を `{color.text.linkHover}` と同一視せずボタンの hover は共通事項の暫定参照に従う旨 (hover 以外の状態一式は `follow-up #4` で未取得) を追記し、同行の `follow-up #4` の位置を hover から hover 以外の状態一式へ改めた。**Input** に構成行 (入力値 `{color.text.body}` / プレースホルダ `{color.text.placeholder}`) を追加し、Do 1 行・Don't 1 行を追加、関連トークン行を `color.text.*` から `color.text.body` / `color.text.placeholder` へ具体化した。**Breadcrumb** にリンク部分の状態ごとの文字色の行と未確定事項 1 行 (パンくずのリンクへ下線の既定を及ぼすかは未判定 = standalone 側) を追加した。**不変**: 共通事項の他の既存行、SearchForm / Card / PriceTag / ReviewStars / Header / Footer / Modal の仕様、Button のバリアント・Do / Don't・関連トークン・未確定事項・active / disabled / loading / focus の記述、Input のステータス・用途・バリアント・状態 (error / focus / disabled / success の 🚧)・未確定事項 (`follow-up #2`)、Breadcrumb の構成・Do、`{color.text.link}` / `{color.text.muted}` / `{font.heading.family}` / `{font.heading.h2Size}` の値・参照先・`$status`、primitive の値、version 表記、UI 構造・Component API・DOM 構造、rental-car / inbound の成果物。**行っていないもの**: 状態固定リスト (命名規則§2) への追加、variant 語彙 (GOV-0002) への追加、新規 primitive の追加、reset / base 層の CSS 実装方針の策定、実装ファイルの変更。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
