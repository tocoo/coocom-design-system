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
- [事実] 指で操作する要素 (ボタン・チップ・プルダウン・オーバーレイ内の選択肢行・タブ等) の**最小の高さは `{size.tapTarget}` (48px)** とする。44px を用いない。正は `design.md` §4.2 (Task 009-68)
- [事実] **選択・適用・現在地といった状態を色だけで伝えない。** 形 (チェック印・点・下線・アイコン)・太さ・面のいずれかを併せ持つ。hover に用いる表現 (面 `{color.surface.subtle}`) を選択中の表現へ流用しない — 同じ表現を割り当てると両者が区別できなくなる (Task 009-69)
- [事実] テキスト色は `{color.text.strong}` / `{color.text.body}` / `{color.text.mutedStrong}` / `{color.text.muted}` の4段。判読性を必要とする補助情報 (補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件) は `{color.text.mutedStrong}` (#616161・白背景 ≈6.2:1) を使用する。`{color.text.muted}` (#9e9e9e・白背景 ≈2.7:1) は通常テキストに求められる 4.5:1 に達しないため、判読性を要する情報には用いない。適用規格・達成レベルの正式確定・適合判定・適合宣言は本書では行わない (design.md §2)
- [事実] 上記4段は**明色面 (`{color.surface.default}` / `subtle` / `muted`) 用**である。inverse 面 (`{color.surface.inverse}` #212121) 上のテキストは `{color.text.inverse}` (主要文字・≈16.10:1) と `{color.text.inverseMuted}` (補助情報・≈6.01:1) の2段を使用する。`{color.text.inverseMuted}` (#9e9e9e) を明色面へ使用しない (白背景 ≈2.7:1)。`{color.text.mutedStrong}` を inverse 面へ使用しない (#616161 は #212121 上 ≈2.60:1)
- [事実] 面 (背景) として色を使う場合の許可される文字色・文字サイズ条件は面ごとに異なる。組み合わせ一覧・campaign accent を面として使用できる条件 ((a) `24px` 以上 (ウェイトを問わない) または (b) `20px` 以上かつ bold)・(a) (b) を満たさない場合 ((i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト) の代替規則・ウェイトの境界 (bold = `700` 以上／通常ウェイト = `700` 未満)・scheme inverse 面 (main `#C8912C` / sub `#C8B12C`) の文字色は `design.md` §2.1 が正。**`{color.text.onAccent}` の存在を理由にコントラスト確認を省略しない**
- [事実] 背景文脈は**明示的な tone / variant として選択できる**ようにする。背景色を検知して自動反転する仕様・コンポーネント内部の固定色だけで複数背景へ対応する仕様は採らない。禁止: primitive の直接参照 / 利用側による任意 HEX 指定 / global token のローカル再束縛を正式仕様とすること
- [事実] 角丸の用途トークンは `{radius.action}` (pill・操作要素)・`{radius.card}` (カード外形)・`{radius.badge}` (非操作のバッジ/ラベル)・`{radius.overlay}` (オーバーレイ = Modal の form = sheet の上端2隅等・`design.md` §7.1)・`{radius.select}` (プルダウン = 8px・`design.md` §5) の**5系統**。非操作の割引率ラベル・状態バッジへ `{radius.action}` を使用しない (操作要素との誤認防止)。**操作可能なバッジは badge ではなく action 系 Component として扱う**
- [事実] 割引率のコンテンツ表記規則 (`NN%OFF`・数字強調・桁・端数処理の未確定・上限/異常値・表示成立条件) は `design.md` §8.1 が正。Component 仕様では表記規則そのものを再定義しない
- [事実] 見出しは**文書レベル (h1〜h6) と Component の見出しで同一トークン群 `{font.heading.*}` を共用する**。割当 (**`breakpoint.lg` 1024px 以上の既定** = h1 2.5rem / h2 2rem / h3 1.5rem / h4 1.25rem / h5 1rem / h6 1rem、**1024px 未満** = h1 2rem / h2 1.5rem / h3 1.25rem / h4〜h6 1rem・ウェイト `{font.heading.weight}` 700・行間 `{font.heading.lineHeight}` 1.3) は `design.md` §3.1 が正。段を移す境界は 1024px の 1 つのみで、この表の範囲内での段下げは §3.1 の「既定から外れる」に該当しない (都度の承認を要しない)。文書レベルの見出しには実寸が 4 の倍数である段のみを用いる (`typography.size` の `sm` 14px・`lg` 18px は見出しに用いない。`sm` は下記 `label.*` の器トークンで用いる段であり本規則の対象外)。Component が文書レベルの既定から外れる値を必要とする場合は**当該 Component の項へ明示的に記載する** (暗黙の上書きを認めない)。明朝 `{font.display.family}` は Display/Hero/特集/詳細施設名で明示的に選択する書体であり見出しの既定ではない
- [事実] リンクは色 `{color.text.link}` (= 主色・TVL-0011) に加え、状態ごとの文字色 (hover = `{color.text.linkHover}` / active = `{color.text.linkActive}` / visited = 専用色を設けず `{color.text.link}` を維持 / focus = `{color.focus.ring}` の `outline`) を使用する。**文中リンクには下線を付し、hover で下線を外さない**。standalone なリンク (カード全体リンク・ナビゲーション項目・パンくず) への下線の既定は未判定であり、状態ごとの文字色は対象を限定せず適用される。**リンクの状態表現に `opacity` を用いない** — 上記の「全 Component の hover は opacity 変化 (≈0.85) を暫定参照」からリンクを除外している。正は `design.md` §2.2
- [事実] **未入力状態の案内文字** (`input` / `textarea` の `::placeholder`・Select の未選択値・その他の入力フィールドの未入力表示) の文字色は `{color.text.muted}` (#9E9E9E・白背景 **2.68:1**・**AA 未達を明示**) に統一する。**UI の種別で限定しない**。未入力であることを色だけで伝えず文言が担う。案内文字を必須項目・ラベル・エラーメッセージ・入力形式の説明の代替として用いない。正は `design.md` §2.3 (Task 009-71)
- [事実] variant 語彙は `primary / secondary / ghost / campaign / text` の5語で確定 (GOV-0002)。語彙外の新設は ADR 必須。**travel の Button 実装は4語 (primary/secondary/ghost/text)**— campaign (accent 塗りボタン) は廃止 (TVL-0012)、accent はバッジ/割引ラベルの「点」専用 (Card badge)
- [事実] 未着手 Component: Toast / Table / Accordion / Pagination / Badge (単体) / Stepper / Empty state。本仕様に含めない。**Select は Task 009-68・Tabs は Task 009-69 で定義済みへ移した**。Task 009-69 / 009-70 ではあわせて、実装に存在しながら未着手一覧に載っていなかった 10 件 (Checkbox / Radio・OptionRow・NavigationRow・Chip・OverlayTrigger・DateRangeCalendar・AvailabilityCalendar・RangeSlider・Skeleton・StickyBar) を新規に定義した。**Pagination / Badge (単体) / Stepper / Empty state は依頼元 (2026-08-03・依頼 D) の指摘で受理した** (Task 009-39・受理と分類のみ。仕様定義は別 Task)。Tabs / Select は従来から未着手として記載済み。各 Component の実体データ・実装実査の有無は Component ごとに異なる (`Pagination` / `Stepper` / `Empty state` は全文検索 0 件・従来の未着手一覧にも不在だった / Badge は `Card.slot.badge` としてスロット規則が定義済みだが Card 外で使う単体 Component は未定義)
- [事実] **Badge (単体) Component の切り出し境界** (Task 009-39): 既に定義済みの `Card.slot.badge` (角丸 `{radius.badge}`・面と文字色の (a)(b) 分岐・割引ラベルの面色・Do / Don't = `design.md` §2.1 が正) と、単体 Component として追加で必要になる範囲 (Card 外での配置・サイズ段階・操作可能な場合の扱い) を分離する。**操作可能なバッジは badge ではなく action 系 Component として扱う**既存の境界 (共通事項) は再定義しない
- [事実] 依頼 D の新規 Component (Pagination / Badge (単体) / Stepper / Empty state) の**定義工程への着手は Web部責任者判断 2026-08-03 で可** (正本 = `governance/owner-decisions.md` §15)。ただし着手可は改訂着手の可否 (`governance/review-approval-rules.md` §9) であり、Component 仕様・variant 語彙 (GOV-0002)・状態固定リスト (命名規則§2) の新設ではない。依頼 D の新規 Component は Work Order 6 の 12 候補 (alignment 候補) とは別であり、同 Work Order 6 の「12 候補は現時点では開始できない」は不変

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
  - Do: CTA の優先度は `primary` / `secondary` / `ghost` / `text` の強弱階層で表現する。**主 CTA の個数制約は設けない** (Web部責任者判断 2026-08-03・依頼 E-5。従来の「1 画面の主 CTA は `primary` 1 つに絞る」を撤回。正本 = `governance/owner-decisions.md` §16)。繰り返し要素 (検索結果カード等) 内で各項目が `primary` を持つことを妨げない
  - Do: 実装は Semantic のみ参照する
  - Don't: accent (`{color.accent.campaign}`) をボタン塗りに使わない (バッジ/割引ラベル等の「点」専用・TVL-0012)
  - Don't: `--primary:#007bff` (Bootstrap 残骸) を参照しない
- 関連トークン: `color.action.*` / `radius.action` / `color.focus.ring` / `motion.transition.*`
- 未確定事項: 状態一式 (follow-up #4)・サイズ段階 sm/md/lg の実測なし (暫定 md のみ)

## Input

- ステータス: Draft 🚧
- 用途: フォームの単一入力 (テキスト/日付/数値)
- バリアント: `Input.default` のみ (実体不足のため最小定義)
- 構成: 入力値の文字色 `{color.text.body}` / 未入力時の案内文字の色 `{color.text.muted}` (#9E9E9E・白背景 2.68:1・**AA 未達を明示**。`design.md` §2.3 が正)
- 状態: error = 文字/枠 `{color.state.error}` 🚧 暫定 / focus = `{color.focus.ring}` outline 🚧 / disabled・success 🚧 未取得
- Do / Don't:
  - Do: エラーはテキストメッセージ併記 (色のみで伝えない = WCAG 2.2 AA / R9)
  - Do: プレースホルダは入力の補助にとどめ、必須項目・ラベル・エラーメッセージ・入力形式の説明の代替にしない
  - Don't: 未取得の必須表現 (アスタリスク等) を推測で固定しない
  - Don't: 未入力の案内文字へ `{color.text.mutedStrong}` (#616161) を使わない — 入力済みテキスト (#424242) との濃度差が小さく、未入力か入力済みかが読み取りにくくなる (`design.md` §2.3 の [根拠])
- 関連トークン: `color.border.*` / `color.state.error` / `color.text.body` / `color.text.muted` / `color.focus.ring`
- 未確定事項: 入力/エラー/必須・検証の実体一式 (follow-up #2)

## Select

- ステータス: Draft
- 用途: **1 階層で選択肢が短い**一覧から 1 つ選ぶ入力 (子どもの年齢等)
- バリアント: `Select.default` のみ
- 構成:
  - 器 — 最小の高さ `{size.tapTarget}` (48px) / 枠線 `{border.width.thin}` × `{color.border.default}` / 面 `{color.surface.default}` / 角丸 `{radius.select}` (8px)
  - 余白 — 左右 `{select.paddingInline}` (12px)。右側は下記シェブロンの領域を加算する
  - 文字 — 書体 `{font.body.family}` / サイズ `{font.body.size}` (1rem・16px) / 選択済みの文字色 `{color.text.body}`
  - 未選択値 — `{color.text.muted}` (`#9E9E9E`・白背景 **2.68:1**・**AA 未達を明示**。`design.md` §2.3 が正。`input` / `textarea` の未入力と同一の扱いであり UI の種別で色を変えない)
  - シェブロン — ブラウザ標準の矢印を止め (`appearance: none`)、`{select.chevronSize}` の Font Awesome 6 グリフを右端に置く (`design.md` §6 のアイコン体系)
- 状態: focus = `{color.focus.ring}` outline / error = 枠 `{color.state.error}` 🚧 暫定 (Input に合わせる) / disabled・success 🚧 未取得
- **Modal の表示形態 (form) との使い分け**:
  - 本 Component を用いる — 選択肢が 1 階層で短く、選んだ値をその場に表示するだけで完結する場合
  - `Modal` の `sheet` / `drawer` / `popover` (§7.1) を用いる — 選択肢に階層がある (地方 → 都道府県)・件数が多く絞り込みや検索を要する・選んだ後に他の入力と組み合わせる場合
  - 件数のしきい値は定めない (未確定事項)
- Do / Don't:
  - Do: 角丸は `{radius.select}` (8px) を用いる。これは「入力要素は `{radius.action}` (pill)」(`design.md` §5) に対する **Select 限定の例外**である
  - Do: 未選択であることは選択肢の文言 (「選択してください」等) で伝える。色だけで伝えない
  - Do: 実装は Semantic のみ参照する
  - Don't: シェブロンを SVG 画像・データ URI で描かない (色の解決値が焼き込まれ、スキーム切替に追随しない)
  - Don't: 本 Component を pill (`{radius.action}`) にしない (ボタン・チップ型操作要素と見分けがつかなくなる)
  - Don't: 未選択であることを色だけで伝えない。文言 (「選択してください」等) を必ず併記する (`design.md` §2.3)
- 関連トークン: `{radius.select}` / `{size.tapTarget}` / `{select.paddingInline}` / `{select.chevronSize}` / `{color.border.default}` / `{border.width.thin}` / `{color.surface.default}` / `{color.text.body}` / `{color.text.muted}` / `{color.focus.ring}` / `{color.state.error}` 🚧 / `{font.body.family}` / `{font.body.size}`
- [事実] 実装 (`tocoo/tocoo_travel` `origin/dev-ds` `142afb120`・2026-09-15) は 2 箇所に分かれ、角丸 (8px / 4px)・文字サイズ (14px / 16px)・シェブロン (自前 SVG / ブラウザ標準) が食い違っていた (`search_s_global.scss` L532・`ultra_market_s.scss` L1091。本 Repository で実測)。本節はこの割れを上記の値へ統一する。**実装側の是正の範囲・順序・期限は実装 Repository 側の課題**である
- [事実] 実装にはプルダウンを UI に用いず、値の運搬にのみ `<select>` を残してチップで選ばせている箇所がある (`inquiry_s.scss` L32・L401)。上記の使い分けに照らすとこれは Select ではなく選択用チップの範囲であり、本節の対象外とする (選択用チップの定義は後続 Task)
- 未確定事項: サイズ段階 (sm/md/lg) は実体がなく定義しない / 複数選択・検索付きの選択は対象外 (実体皆無) / Modal の表示形態へ切り替える件数のしきい値 / error・disabled・success の実体一式 (follow-up #2)

## Checkbox / Radio

- ステータス: Draft
- 用途: 絞り込み条件・同意など、複数選択 (Checkbox) / 単一選択 (Radio) の入力
- バリアント: なし (`Checkbox` と `Radio` は同じ器を共有し、形状と選択時の表現のみ異なる)
- 構成:
  - ネイティブの `input` を**視覚的にのみ隠し** (フォーカスは受け取れる状態を保つ)、箱と印を自前で描く
  - 箱 — 一辺 `{control.size}` (16px) / 面 `{color.surface.default}` / 未選択の枠 `{control.borderWidth}` (2px) × `{color.border.strong}`
  - 角丸 — Checkbox = `{control.radius}` (4px) / Radio = 円
  - 選択時 — Checkbox = 面 `{color.brand.primary}` + 枠 `{color.brand.primary}` + `{color.text.inverse}` のチェック印 (`{control.glyphSize}` の FA6 グリフ) / Radio = 面は `{color.surface.default}` のまま中心に直径 `{control.dotSize}` (8px) の `{color.brand.primary}` の点
  - ラベル — 文字 `{color.text.body}` / 箱との間隔 `{control.gap}` (12px)
- 状態: focus = `{color.focus.ring}` の outline (`{control.borderWidth}`・オフセット 4px) / disabled・error 🚧 未取得
- Do / Don't:
  - Do: `input` は `opacity: 0` 等で**視覚的にのみ隠す**。`display: none` / `visibility: hidden` を用いない (キーボードで操作できなくなる)
  - Do: 箱とラベルは同一の `label` 要素に収め、ラベル文字を押しても切り替わるようにする
  - Do: 選択状態を**色だけで伝えない** — Checkbox はチェック印、Radio は中心の点という形の差を併せ持つ
  - Don't: チェック印を SVG 画像・データ URI で描かない (アイコンは FA6 に統一 = `design.md` §6。色の解決値が焼き込まれスキーム切替に追随しない)
  - Don't: `{radius.badge}` を流用しない (同トークンは非操作のバッジ/ラベル専用で入力要素を対象外と定めている)
- 関連トークン: `{control.size}` / `{control.radius}` / `{control.borderWidth}` / `{control.glyphSize}` / `{control.dotSize}` / `{control.gap}` / `{color.surface.default}` / `{color.border.strong}` / `{color.brand.primary}` / `{color.text.inverse}` / `{color.text.body}` / `{color.focus.ring}`
- [事実] 実装 (`tocoo/tocoo_travel` `origin/dev-ds`) は DS 準拠のファイルの中で 3 箇所に分かれ、絞り込みパネル (`filter_s_global.scss` L58-127) のみが上記の作り、お問い合わせ (`inquiry_s.scss` L707) とソリューション (`solution_s.scss` L510) はネイティブ部品を 24px で置くだけで**選択時の色もフォーカス枠も持たない** (本 Repository で実測)。本節は前者へ統一する (Web部責任者判断 2026-09-15・正本 = `governance/owner-decisions.md` §34 K-6)。実装側の是正の範囲・順序・期限は実装 Repository 側の課題である
- 未確定事項: disabled・error・不定 (indeterminate) 状態の実体 / サイズ段階 (実体皆無)

## OptionRow

- ステータス: Draft
- 用途: オーバーレイ (Modal の `sheet` / `drawer` / `popover`) の中に並ぶ、**選択肢から 1 つ選ぶ**行 (並び替えの選択等)
- バリアント: なし
- 構成:
  - 器 — 最小の高さ `{size.tapTarget}` (48px) / 上下 `{row.paddingBlock}` (12px)・左右 `{row.paddingInline}` (16px) / 面と枠は持たない (`transparent`)
  - 文字 — `{row.fontSize}` (14px) / `{color.text.strong}` / 行内の間隔 `{row.gap}` (12px)
  - 選択中 — 文字を `{font.heading.weight}` (700) にし、色を `{color.text.link}` にしたうえで、**行末にチェックのアイコン** (FA6) を置く
  - 区切り — 行を隙間なく並べる場合は `{border.width.thin}` × `{color.border.subtle}` の下線を用いる
- 状態: hover = 面 `{color.surface.subtle}` / focus = `{color.focus.ring}` outline / disabled 🚧 未取得
- Do / Don't:
  - Do: 選択中であることを**色だけで伝えない** — 太さ・チェックアイコンを併せ持つ
  - Do: 選択したら確定し、オーバーレイを閉じる
  - Don't: 選択中の表現に面 (背景) を用いない — 面は hover に割り当てており、同じ面を使うと hover と選択中が見分けられなくなる
  - Don't: 階層をたどる行 (`NavigationRow`) と混在させない
- 関連トークン: `{size.tapTarget}` / `{row.paddingBlock}` / `{row.paddingInline}` / `{row.gap}` / `{row.fontSize}` / `{color.text.strong}` / `{color.text.link}` / `{font.heading.weight}` / `{color.surface.subtle}` / `{color.border.subtle}` / `{border.width.thin}` / `{color.focus.ring}`
- [事実] 実装は 2 箇所 (`search_result_s.scss` L616-638 の並び替え・`chokuzen_s.scss` L1213-1237) にあり、**値は 1 つも違わない複写**である (本 Repository で実測)。左右余白のみ目的地の行 (12px) と食い違っていたため 16px へ統一した
- 未確定事項: 複数選択を伴う行の扱い (実体皆無) / disabled の実体

## NavigationRow

- ステータス: Draft
- 用途: オーバーレイの中に並ぶ、**次の階層へ進む**行 (目的地 = 地方 → 都道府県 → エリア等)
- バリアント: なし
- 構成:
  - 器・文字 — `OptionRow` と同じ器 (`{size.tapTarget}` / `{row.paddingBlock}` / `{row.paddingInline}` / `{row.gap}` / `{row.fontSize}` / `{color.text.strong}`) を用いる
  - 行末 — 次の階層があることを示す右向きシェブロン (FA6)。必要に応じてその手前に件数を `{row.countFontSize}` (12px) / `{color.text.body}` で置く
  - 現在たどっている経路 — 面 `{color.surface.subtle}` に加えて文字を `{font.heading.weight}` (700) にする
- 状態: hover = 面 `{color.surface.subtle}` / focus = `{color.focus.ring}` outline
- Do / Don't:
  - Do: 現在の経路は**面と太さの両方**で示す。面だけでは hover と同じ見た目になり区別できない (Web部責任者判断 2026-09-15・`governance/owner-decisions.md` §35)
  - Do: 押した結果が「選択の確定」ではなく「次の階層の表示」であることを、行末のシェブロンで示す
  - Don't: 選択の確定に用いない (確定は `OptionRow` の役割)
  - Don't: シェブロンに `{color.text.muted}` を用いない — 白面上 2.68:1 で非テキスト UI 要素に求められる 3:1 に達しない
- 関連トークン: `OptionRow` と同じ器トークン一式 / `{row.countFontSize}` / `{color.surface.subtle}` / `{font.heading.weight}` / `{color.text.body}` / `{color.text.mutedStrong}`
- [事実] 実装 (`search_s_global.scss` L336-364) は `:hover` と `.is-active` の双方へ `color.surface.subtle` を指定しており、**マウスを乗せている行と現在たどっている行が画面上で区別できない**状態にあった (本 Repository で実測)。本節は現在の経路に太さを加えることでこれを解消する。**新しい色は追加していない**
- [事実] 同実装のシェブロンは `color.text.muted` (`#9E9E9E`・白面 2.68:1) を用いている (`search_s_global.scss` L364)。本節は `{color.text.mutedStrong}` (`#616161`・白面 6.19:1) を正とする。実装側の是正は実装 Repository 側の課題である
- 未確定事項: 階層の深さの上限 / 戻る操作の表現 (ヘッダー側の責務との切り分け)

## Chip

- ステータス: Draft
- 用途: pill 形状の小さな操作要素。**選択させる** (種別の選択等) / **適用中の絞り込みを示し押すと解除する** の 2 用途
- **用途軸 (use)**: `select` (選択用) / `applied` (適用中の絞り込み) の 2 値。**variant 語彙 (GOV-0002) とは別軸**であり語彙への追加ではない (`PriceTag` の `tone`・`Modal` の `form` と同じ扱い)
- 構成 (共通): 最小の高さ `{size.tapTarget}` (48px) / 角丸 `{chip.radius}` (pill) / 左右 `{chip.paddingInline}` (16px) / 文言とアイコンの間隔 `{chip.gap}` (8px)
- 構成 (use ごと):

| | `use = select` | `use = applied` |
|---|---|---|
| 面 | `{color.surface.default}` | `{color.scheme.main.tint}` |
| 枠 | `{chip.borderWidth}` (1px) × `{color.border.default}` | なし |
| 文字 | `{chip.fontSize.select}` (14px) / `{color.text.body}` | `{chip.fontSize.applied}` (12px) / `{color.text.strong}` |
| 上下余白 | `{chip.paddingBlock.select}` (8px) | `{chip.paddingBlock.applied}` (4px) |
| 選択中 | 枠 `{color.brand.primary}` + 面 `{color.scheme.main.tint}` + `{font.heading.weight}` (700) + `{color.text.strong}` | — (適用中であること自体が面で示される) |
| 押したとき | 選択が切り替わる | その絞り込みが解除される (行末に解除のアイコン) |

- 状態: focus = `{color.focus.ring}` outline / hover 🚧 暫定 (共通事項の opacity 変化) / disabled 🚧 未取得
- Do / Don't:
  - Do: `use` は明示的に選択する。文脈から自動で切り替えない
  - Do: `use = select` の選択中は、枠・面・太さの 3 つで示す (色だけで伝えない)
  - Do: `use = applied` には解除のアイコンを置き、押すと何が起きるかを形で示す
  - Don't: 非操作のラベル・バッジに用いない — それらは `Card.slot.badge` / `{radius.badge}` の範囲であり、pill 形状は操作要素のシグネチャである
  - Don't: `use = applied` に枠線を足さない (面で足りており、解除操作の並びが過密になる)
- 関連トークン: `{size.tapTarget}` / `{chip.radius}` / `{chip.paddingInline}` / `{chip.gap}` / `{chip.borderWidth}` / `{chip.paddingBlock.*}` / `{chip.fontSize.*}` / `{color.surface.default}` / `{color.scheme.main.tint}` / `{color.border.default}` / `{color.brand.primary}` / `{color.text.body}` / `{color.text.strong}` / `{color.text.mutedStrong}` / `{font.heading.weight}` / `{color.focus.ring}`
- [事実] 実装は `use = select` が 1 箇所 (`inquiry_s.scss` L426-444)、`use = applied` が 2 箇所 (`search_result_s.scss` L296-312・`chokuzen_s.scss` L373-390) にあり、後者 2 つは**値が 1 つも違わない複写**である (本 Repository で実測)。`use = applied` の最小の高さは実装では 44px であり、`design.md` §4.2 (48px) に合わせて変更する
- 未確定事項: hover の実体 (follow-up #4) / disabled / 1 行に収まらない場合の折り返しと省略

## Tabs

- ステータス: Draft
- 用途: 同じ場所に複数の内容を切り替えて表示する (検索モジュールの検索種別等)
- バリアント: なし
- 構成:
  - タブ — 最小の高さ `{size.tapTarget}` (48px) / 上下 `{tab.paddingBlock}` (12px)・左右 `{tab.paddingInline}` (8px) / 面と枠は持たない
  - 文字 — `{tab.fontSize}` (14px) / `{font.heading.weight}` (700)
  - 非選択 — `{color.text.mutedStrong}` / 下線なし
  - 選択中 — `{color.text.link}` + 下 `{tab.indicatorWidth}` (2px) × `{color.brand.primary}` の線
- 状態: focus = `{color.focus.ring}` outline / hover 🚧 暫定 / disabled 🚧 未取得
- Do / Don't:
  - Do: 選択中は**色と下線の両方**で示す (色だけで伝えない)
  - Do: 切り替えても同じ場所に表示する。別画面へ遷移する導線には用いない (それはナビゲーション項目の役割)
  - Don't: タブの本数を横スクロール前提で増やさない (実体が無く、省略・スクロールの規則を定めていない)
- 関連トークン: `{size.tapTarget}` / `{tab.paddingBlock}` / `{tab.paddingInline}` / `{tab.fontSize}` / `{tab.indicatorWidth}` / `{font.heading.weight}` / `{color.text.mutedStrong}` / `{color.text.link}` / `{color.brand.primary}` / `{color.focus.ring}`
- [事実] 実装は 1 箇所 (`search_s_global.scss` L52-69) のみで割れていない (本 Repository で実測)。非選択の文字色は同実装が `color.text.muted-strong` を用いており本節と一致する
- 未確定事項: a11y (`role="tablist"` / `aria-selected` / 矢印キー操作) は `alignment-blocking-facts-resolution-plan.md` §8K の下流課題 / 本数が多い場合の省略・スクロール / タブ内容 (pane) の切替の遷移

## OverlayTrigger

- ステータス: Draft
- 用途: 絞り込み・並び替え・検索条件のオーバーレイを開く起点。**現在の値を表示したまま押せる**ボタン
- バリアント: なし (`Button` の 4 語とは別の Component。枠線を持ち、アイコン + ラベル + 現在値 + 件数バッジを抱える形が異なる)
- 構成:
  - 器 — 最小の高さ `{size.tapTarget}` (48px) / 角丸 `{trigger.radius}` (pill) / 上下 `{trigger.paddingBlock}` (8px)・左右 `{trigger.paddingInline}` (16px) / 面 `{color.surface.default}` / 枠 `{trigger.borderWidth}` (1px) × `{color.border.default}`
  - 中身 — アイコン (`{color.text.mutedStrong}`) + ラベル (`{color.text.mutedStrong}`) + 現在値 (`{trigger.fontSize}` 14px / `{font.heading.weight}` 700 / `{color.text.strong}`)。間隔は `{trigger.gap}` (8px)
  - 件数バッジ — 適用中の絞り込みの件数を示す。最小幅 `{trigger.badgeMinWidth}` (20px) / 面 `{color.brand.primary}` / 文字 `{color.text.inverse}`
  - 現在値が長い場合は末尾を省略する (`text-overflow`)。狭い幅では表示幅に上限を置く
- 状態: focus = `{color.focus.ring}` outline / hover 🚧 暫定 / disabled 🚧 未取得
- Do / Don't:
  - Do: 押すと開くことを、開いた先 (`Modal` の `sheet` / `drawer` / `popover`) と対応づける
  - Do: 現在の値をボタン上に出す。何が適用されているかをボタンを押さずに読めるようにする
  - Don't: `Button` の variant (`primary` / `secondary` / `ghost` / `text`) で代用しない — それらは現在値・件数バッジを抱える形を持たない
  - Don't: 件数を色だけで示さない (数字を表示する)
- 関連トークン: `{size.tapTarget}` / `{trigger.radius}` / `{trigger.paddingBlock}` / `{trigger.paddingInline}` / `{trigger.gap}` / `{trigger.borderWidth}` / `{trigger.fontSize}` / `{trigger.badgeMinWidth}` / `{color.surface.default}` / `{color.border.default}` / `{color.text.strong}` / `{color.text.mutedStrong}` / `{color.brand.primary}` / `{color.text.inverse}` / `{font.heading.weight}` / `{color.focus.ring}`
- [事実] 実装は 2 箇所 (`search_result_s.scss` L212-227・`chokuzen_s.scss` L304-323) にあり、**値は 1 つも違わない複写**である (本 Repository で実測)。最小の高さは実装では 44px (`calc(spacing.4 * 2.75)`) であり、`design.md` §4.2 (48px) に合わせて変更する。追従帯の中の条件ボタン (`search_result_s.scss` L783) と絞り込み解除リンク (同 L314) も同じ 44px を用いており、同様に 48px とする
- 未確定事項: hover の実体 (follow-up #4) / disabled / 起点が 3 つ以上並ぶ場合の優先順位

## DateRangeCalendar

- ステータス: Draft
- 用途: 宿泊日など**日付の範囲 (開始日〜終了日)** を選ぶカレンダー
- バリアント: なし
- 構成:
  - 器 — 内側余白 `{calendar.padding}` (16px)。1024px 未満は 1 か月、1024px 以上は 2 か月を `{calendar.monthGap}` (24px) の間隔で並べる
  - 月送り — 一辺 `{calendar.navSize}` (48px) の円形ボタン (枠 `{calendar.navBorderWidth}` × `{color.border.default}` / 文字色 `{color.text.link}`)。表示中の期間は `{font.heading.family}` / `{font.body.size}` / `{font.heading.weight}`
  - 曜日見出し — 高さ `{calendar.weekdayHeight}` (32px) / `{calendar.weekdayFontSize}` (12px) / `{color.text.mutedStrong}`。日曜は `{color.state.error}`、土曜は `{color.text.link}`
  - 日付セル — 最小の高さ `{size.tapTarget}` (48px) / `{calendar.dateFontSize}` (14px) / `{color.text.strong}` / 数字は等幅 (`tabular-nums`)
  - 範囲の表現 — 両端 = 面 `{color.brand.primary}` + `{color.text.inverse}` + `{font.heading.weight}` + 角丸 `{calendar.selectedRadius}` (16px) / 期間中 = 面 `{color.surface.subtle}`
- 状態: 選択不可 (過去日) 🚧 暫定 — `{color.text.mutedStrong}` + 不透明度 0.45。**DS に選択不可の文字色トークンが無い**ため暫定表現である (未確定事項) / focus = `{color.focus.ring}` outline
- Do / Don't:
  - Do: 曜日の色分け (日曜・土曜) は補助にとどめる。曜日は列の位置でも判別できる
  - Do: 範囲の両端と期間中を**面の濃さで区別**し、両端は太さも併せ持つ
  - Don't: 選択不可を不透明度だけで表現したまま確定しない (未確定事項として追跡する)
  - Don't: 空室・料金を載せない — それは `AvailabilityCalendar` の役割
- 関連トークン: `{calendar.padding}` / `{calendar.navSize}` / `{calendar.navBorderWidth}` / `{calendar.monthGap}` / `{calendar.weekdayHeight}` / `{calendar.weekdayFontSize}` / `{calendar.dateFontSize}` / `{calendar.selectedRadius}` / `{size.tapTarget}` / `{color.brand.primary}` / `{color.text.inverse}` / `{color.surface.subtle}` / `{color.text.strong}` / `{color.text.mutedStrong}` / `{color.text.link}` / `{color.state.error}` / `{font.heading.family}` / `{font.heading.weight}` / `{color.focus.ring}`
- [事実] 実装は 1 箇所 (`search_s_global.scss` L382-461) のみで割れていない (本 Repository で実測)。同実装のコメントは「DS に disabled 用 text トークン無し。muted+opacity で暫定表現」と記しており、本節はこれを未確定事項として引き継ぐ
- 未確定事項: **選択不可 (過去日・満室) の文字色トークン** — 不透明度 0.45 を掛けた実効コントラストは本 Repository で検証しておらず、AA 適合を主張しない / 月送りの上限・下限 / 1 泊も選べない期間の表現

## AvailabilityCalendar

- ステータス: Draft
- 用途: 日付ごとの**空室状況と料金**を一覧するカレンダー (プラン空室カレンダー)
- バリアント: なし
- 構成:
  - セル — 最小の高さ **96px** / 角丸 `{availability.cellRadius}` (8px) / 上下 `{availability.cellPaddingBlock}` (8px)・左右は 640px 以上で `{availability.cellPaddingInline}` (4px)、640px 未満は実装が 2px を用いる (段が無く未確定事項) / 枠線は用いず**面で状態を分ける**
  - 面 — 空室あり・残りわずか = `{color.scheme.main.tint}` / 問い合わせ = `{color.surface.muted}` / 空室なし = `{color.surface.subtle}`
  - 選択中の日 — 面は変えず、内側に `{availability.selectedBorderWidth}` (2px) × `{color.brand.primary}` の枠を重ねる
  - 文字 — 日付は `{font.price.family}`、料金・在庫は 10px (`{typography.size.xs}` から 2px 小さい派生値)。残りわずかは `{color.label.stock}`、問い合わせは `{color.text.mutedStrong}`、空室なしは `{color.text.placeholder}`
- 状態: 空室なしは押せない (`cursor: default`) / focus = `{color.focus.ring}` outline 🚧
- Do / Don't:
  - Do: 空室状況は**面と文言の両方**で示す。面の色だけで在庫状態を伝えない
  - Do: 選択中の日は枠で示す。面を変えると在庫状態の表示と衝突する
  - Don't: 日付の範囲選択に用いない — それは `DateRangeCalendar` の役割
- 関連トークン: `{availability.cellRadius}` / `{availability.cellPaddingBlock}` / `{availability.cellPaddingInline}` / `{availability.selectedBorderWidth}` / `{color.scheme.main.tint}` / `{color.surface.muted}` / `{color.surface.subtle}` / `{color.brand.primary}` / `{font.price.family}` / `{color.label.stock}` / `{color.text.mutedStrong}` / `{color.text.placeholder}`
- [事実] 実装は 1 箇所 (`ultra_plan_calendar_s.scss` L100-183) のみで割れていない (本 Repository で実測)
- [事実] セルの最小の高さ 96px は実装では `calc(spacing.16 + spacing.8)` (64px + 32px) で組まれている。`spacing` に 96px の段が無いため**単一のトークンでは表せない**。本節は実装値をそのまま正とし、**新しい段は追加しない** (トークン化の要否は未確定事項)
- [事実] 料金・在庫の 10px は `calc(typography.size.xs - 0.125rem)` で組まれており、`typography.size` の 9 段に存在しない値である。**本書はこれを正としない** — 段の新設の要否を未確定事項として起票する
- 未確定事項: セル高 96px のトークン化 / **料金・在庫の 10px** (スケール外の値・段の新設の要否) / 横スクロール時の月またぎ / focus の実体

## RangeSlider

- ステータス: Draft
- 用途: 価格など**数値の範囲**を 2 つのつまみで絞り込む
- バリアント: なし
- 構成:
  - 軌道 — 高さ `{rangeSlider.trackHeight}` (4px) / 角丸 `{rangeSlider.trackRadius}` (pill) / 面 `{color.surface.muted}`
  - 選択範囲 — 面 `{color.brand.primary}`
  - つまみ — 直径 `{rangeSlider.thumbSize}` (16px) / 円 / 面 `{color.surface.default}` / 内側に `{rangeSlider.thumbBorderWidth}` (2px) × `{color.brand.primary}` の枠 + `{shadow.md}` 🚧
  - 当たり判定 — つまみを掴める領域の高さ `{rangeSlider.hitHeight}` (24px)
  - 現在値 — 軌道の下に下限・上限を両端揃えで表示する
- 状態: focus = `{color.focus.ring}` outline / disabled 🚧 未取得
- Do / Don't:
  - Do: 現在の下限・上限を**数値で併記**する。つまみの位置だけで値を伝えない
  - Do: ネイティブの `input[type="range"]` を土台に用い、キーボードで操作できる状態を保つ
  - Don't: `{size.tapTarget}` (48px) を軌道上のつまみへ適用しない — 独立した操作要素の最小の高さであり、つまみは当たり判定 24px で扱う
- 関連トークン: `{rangeSlider.trackHeight}` / `{rangeSlider.trackRadius}` / `{rangeSlider.thumbSize}` / `{rangeSlider.thumbBorderWidth}` / `{rangeSlider.hitHeight}` / `{color.surface.muted}` / `{color.surface.default}` / `{color.brand.primary}` / `{shadow.md}` 🚧 / `{color.focus.ring}`
- [事実] 実装は 1 箇所 (`search_result_s.scss` L645-700) のみで割れていない (本 Repository で実測)
- 未確定事項: 影 `{shadow.md}` は placeholder (follow-up #13) / 下限と上限が交差したときの挙動 / 刻み幅 / disabled

## Skeleton

- ステータス: Draft
- 用途: 読み込み中に、**これから出る内容の場所**を面で示す骨組み
- バリアント: なし
- 構成:
  - 器 — 置き換える対象と同じ外形を用いる。カードを置き換える場合は角丸 `{radius.card}` 🚧
  - 面 — `{color.surface.muted}`
  - 線 — 角丸 `{skeleton.radius}` (4px)。高さは `{skeleton.lineHeight.sm}` (16px・本文相当) / `.md` (24px・見出し相当) / `.lg` (32px・価格相当) / `.xl` (40px・ボタン相当) の 4 段
  - 余白 — 内側 `{skeleton.padding}` (16px) / 線どうしの間隔 `{skeleton.gap}` (12px)
- 状態: なし (読み込み完了で実内容に置き換わる)
- Do / Don't:
  - Do: 置き換える対象と**同じ外形・同じ配置**にする。差があると読み込み完了時に内容が飛ぶ
  - Do: 読み込み中であることを支援技術へ伝える手段 (`aria-busy` 等) を併せて用いる
  - Don't: 点滅・明滅で読み込み中を表現しない (`prefers-reduced-motion` への配慮が別途必要になる)
  - Don't: 実際には出ない要素の骨組みを置かない
- 関連トークン: `{skeleton.radius}` / `{skeleton.padding}` / `{skeleton.gap}` / `{skeleton.lineHeight.sm}` / `.md` / `.lg` / `.xl` / `{color.surface.muted}` / `{radius.card}` 🚧
- [事実] 実装は 1 箇所 (`ultra_market_s.scss` L806-860) のみで割れていない (本 Repository で実測)。ただし同実装はカード外形に `radius.lg` (16px) を用いており、**カード外形の用途トークン `{radius.card}` (暫定 md = 8px) と食い違う**。本節は `{radius.card}` を正とする — 骨組みは置き換える対象と同じ外形であるべきであり、対象であるカードの角丸は `{radius.card}` が定めるためである。**`{radius.card}` 自体が `placeholder` (実px 未取得) である点は本 Task で解消しない**
- 未確定事項: `{radius.card}` の実px (follow-up・`design.md` §5) / 骨組みを出す件数・最小表示時間 / 読み込み中の支援技術への伝え方

## StickyBar

- ステータス: Draft
- 用途: 一覧をスクロールした際に画面上端へ貼り付き、**現在の検索条件と主要な操作**を出し続ける帯
- バリアント: なし
- 構成:
  - 器 — 上下 `{stickyBar.paddingBlock}` (4px) / 左右 `{stickyBar.paddingInline}` (16px) / 要素の間隔 `{stickyBar.gap}` (12px) / 面 `{color.surface.default}` / `{shadow.sm}` 🚧
  - z 軸 — `{elevation.sticky}`
  - 上端の位置 — サイト共通の固定告知の下に置く (実測値を実装が渡す)
  - 中身 — 条件ボタン (最小の高さ `{size.tapTarget}` / 角丸 `{trigger.radius}` / 面 `{color.surface.subtle}`) に、主となる条件を `{stickyBar.mainFontSize}` (14px) / `{font.heading.weight}` / `{color.text.strong}` で、補助を `{stickyBar.subFontSize}` (12px) / `{color.text.mutedStrong}` で 2 行に積む。結果ヘッダーが画面外へ出たら絞り込みと並び替えの起点もこの帯へ合流させる
- 状態: 表示 / 非表示 (スクロール位置による)。focus = `{color.focus.ring}` outline
- Do / Don't:
  - Do: 画面の占有を 1 本に抑える。帯を複数積まない
  - Do: 帯の中の操作要素も `{size.tapTarget}` (48px) を満たす
  - Don't: 帯に入れる情報を増やして高さを可変にしない (内容が跳ねる)
- 関連トークン: `{stickyBar.paddingBlock}` / `{stickyBar.paddingInline}` / `{stickyBar.gap}` / `{stickyBar.mainFontSize}` / `{stickyBar.subFontSize}` / `{elevation.sticky}` / `{color.surface.default}` / `{color.surface.subtle}` / `{shadow.sm}` 🚧 / `{size.tapTarget}` / `{trigger.radius}` / `{color.text.strong}` / `{color.text.mutedStrong}` / `{font.heading.weight}` / `{color.focus.ring}`
- [事実] 実装は 2 箇所 (`search_result_s.scss` L761-826・`chokuzen_s.scss` L1245 以降) にあり、**値は 1 つも違わない複写**である (本 Repository で実測)
- 未確定事項: 影 `{shadow.sm}` は placeholder (follow-up #13) / 出現・退出の遷移 (`{motion.transition.*}` 🚧) / 固定告知との重なりの規則

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
  - 角丸: `{label.radius}` (= `{radius.badge}` = 4px・確定 bound・Owner 2026-08-07)。`{radius.action}` (pill) を使用しない — 操作要素との誤認防止
  - 器 (寸法・共通・2 サイズ。ラベル・タグ定義シート 器・器トークン `label.*` が正):
    - 高さ `{label.height.sm}` (20px) / `{label.height.md}` (24px)、左右余白 `{label.paddingInline.sm}` (8px) / `{label.paddingInline.md}` (12px)、行高 `{label.lineHeight}` (1・上下中央・上下余白は指定しない)
    - 文字サイズ `{label.fontSize.sm}` (12px) / `{label.fontSize.md}` (14px)。ウェイトは面のあるラベル `{label.weight.emphasis}` (700) / 中立タグ (D) `{label.weight.neutral}` (400)
    - **A 割引率の数字強調**: 数字は `{label.numberSize.sm}` (14px) / `{label.numberSize.md}` (16px) = `%OFF` (文字サイズ) より 1 段上 (`design.md` §8.1「数字の強調」が正)
  - ラベル種別と用途色 (面色の成立条件は上記分岐・`design.md` §2.1 / §8.2 / §8.3 が正):
    - **A 割引率** = `{color.label.discount}` (逆色面 #C8912C + 白文字・A 割引率ラベルに限る白文字の例外)
    - **B 会員種別** = `{color.membership.paid}` (有料・accent 淡色面 + 濃色文字・🚧 仮色) / `{color.membership.free}` (無料・主色 tint + ink・既定では非表示 = 誘導の印)
    - **D 施設属性** = `{color.tag.neutral}` (中立面 #F5F5F5 + `{color.text.body}`・400・色を持たせず区分は順序で読ませる)
    - **E1 残室僅少** = `{color.label.stock}` (= `{color.state.error}` の文字・面なし・価格直上・白背景のみ・写真上に出さない)
    - **C カテゴリ・特集** = `{color.label.category}` (企画名・タイムセール等、商品の所属を示す非操作ラベル)。面 `{color.label.category.surface}` (白 #FFFFFF) + 文字 `{color.label.category.text}` (#212121・≈16.10:1) + アイコン `{color.label.category.icon}` (campaign accent #E4572E)。**accent は面ではなくアイコン (点) として持つ** — accent を面として持つのは B 会員種別 (`{color.membership.paid}` = accent 淡色段) のみとする用途分離による (Task 009-60・Web部責任者判断 2026-09-05・`governance/owner-decisions.md` §27)。面を accent で塗らない。器は sm (12px)・ウェイトは `{label.weight.emphasis}` (700)。**白面は下記 (a) (b) の分岐に依存せず成立する**ため、12px でも (i) (ii) の代替 2 択を要しない。**白系の面 (`{color.surface.default}` `#FFFFFF` / `{color.surface.subtle}` `#F9F9F9`) の上に置く場合は、枠線 `{color.label.category.border}` (= `{color.border.default}` `#CCCCCC`) を `{border.width.thin}` (1px) で引く** — 面のみでは境界が生じないため (白 × 白 1.00:1・白 × `surface.subtle` 1.05:1)。写真の上・有色面の上では**枠線を引かず**面のみで分離する (影・スクリムは用いない)。枠線は白面上 ≈1.61:1 で**非テキスト UI 要素の 3:1 に達しない**ことを明示する (分離の補助であり識別は文字 ≈16.10:1 が担う。`design.md` §2.1 が正・Task 009-60R・`governance/owner-decisions.md` §27-3 ⓕ)。**アイコンの字形とサイズは未規定** (下記 未確定事項)
    - **F 予約条件** は面を持たないテキスト行 (バッジの器に乗せない・`design.md` §8.2)。**G 写真枚数** は pill (`{color.surface.inverse}` + 白文字・`{radius.action}`) で本 badge の器の対象外 (既存トークンで成立・追加なし)
  - 面と文字色は文字サイズ・ウェイトで分岐する (境界の定義は `design.md` §2.1 が正)
    - **(a) `24px` 以上 (ウェイトを問わない)、または (b) `20px` 以上かつ bold (`700` 以上)**: 面 `{color.accent.campaign}` (#E4572E) + 文字 `{color.text.onAccent}` (≈3.68:1・大きなテキスト基準 3:1 のみ達成)
    - **上記以外** (= (i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト (`700` 未満)): 面 `{color.accent.campaign}` を使用しない。代替は **2 択**とする (Task 009-49・`design.md` §2.1 が正):
      - ① **[既定] neutral dark 面** — 面 `{color.surface.inverse}` (#212121) + 文字 `{color.text.inverse}` (≈16.10:1)。既存トークンの範囲で通常テキスト 4.5:1 を満たす面
      - ② **accent 淡色面 (b2)** — 面 `{color.accent.campaignTint}` (#F9CDBC) + 文字 `{color.accent.campaignInk}` (#8A2E11・濃色文字)。小サイズ (12px) ラベル向け。**accent 濃色段が 🚧 仮色のため、淡色面 + 濃色文字の 4.5:1 成立は実色値確定後に検証**する (それまでは ① を用いる)
      - accent を**文字色**として明色面に置く方法はこの場合の代替にならない (明色面上 3.38〜3.68:1・淡色面上 ≈2.5:1 で通常テキスト 4.5:1 未達。`design.md` §2.1 が正)
  - 割引ラベルの面色 (c1・Web部責任者判断 2026-08-03。`design.md` §2.1 が正):
    - **scheme 逆色面**: 面 `{color.scheme.main.inverse}` (#C8912C・副色文脈は `{color.scheme.sub.inverse}` #C8B12C) + 文字 `{color.text.strong}` に固定する (main 5.78:1 / sub 7.50:1) を原則とする。評価色 `{color.icon.rating}` トークンを面へ流用しない (逆色の値は評価と割引ラベルの 2 用途で共有するが用途は分離する)
    - **[例外] 非操作の点的ラベルに限る白文字** (Task 009-48・A 割引率ラベル = `{color.label.discount}`): 逆色面 (`{color.scheme.*.inverse}`) + 白文字 (`{color.text.inverse}`) を、**A 割引率ラベルに限り例外として許容する** (逆色面 2.78:1 / 2.15:1 = **AA 未達を明示**・サイズ/ウェイト不問)。白文字が通常テキスト 4.5:1 を満たす面は `{color.surface.inverse}` の 1 面のみ。**campaign accent 面 + 白文字は本例外に含めない** — 下記 (i) (ii) の白文字禁止と代替 2 択は例外なく維持する。A 割引率ラベル以外の非操作ラベル (B 会員種別・C カテゴリ・特集・D 施設属性・E 在庫/販売状態) と操作可能なバッジ (action 系) はいずれも対象外。原則 (白文字禁止) は維持し例外を A 割引率 + 逆色面に限る (Task 009-60 で当初の「非操作の点的ラベル + campaign accent/逆色面」から縮小・`design.md` §2.1「A 割引率ラベルに限る白文字の例外」が正)
    - **小サイズ (例 12px) の accent 淡色面 (b2)** (Task 009-49): accent 淡色面 (面 `{color.accent.campaignTint}` #F9CDBC + 濃色文字 `{color.accent.campaignInk}` #8A2E11) を semantic に**追加済み** ((i)(ii) 代替の 2 択目)。ただし accent **濃色段が 🚧 仮色**のため、淡色面 + 濃色文字の 4.5:1 成立は実色値確定後に検証する。それまで 12px は既定 (① neutral dark 面) を用いる (正本 = `governance/owner-decisions.md` §13・§24・`design.md` §2.1)
  - Do: 割引率の表記は `design.md` §8.1 に従う (`NN%OFF`・数字は `%OFF` より 1 段上のサイズ段で強調)。表示成立条件を満たさない場合はラベル自体を表示しない
  - Do: 状態・カテゴリを色のみで伝えずテキストを併記する (R9)
  - Don't: campaign accent 面上に (a) (b) を満たさない白文字 ((i) `20px` 未満のすべて／(ii) `20px` 以上 `24px` 未満かつ通常ウェイト) を置く
  - Don't: 縁取り・影でコントラスト不足を解決したものとして扱う
  - Don't: 評価色 (`{color.icon.rating}` = スキーム逆色) を割引ラベル・販促面へ流用する (用途境界は `design.md` §2.1)
  - Don't: バッジを操作可能にする場合に badge のまま扱う — action 系 Component として扱い `{radius.action}` を使用する
- 関連トークン: `radius.card` 🚧 / `radius.badge` (bound 4px) / `label.*` (器 = height / paddingInline / lineHeight / fontSize / numberSize / weight / radius) / `color.label.discount` / `color.label.category` / `color.label.stock` / `color.membership.paid` 🚧 / `color.membership.free` / `color.tag.neutral` / `color.accent.campaignTint` 🚧 / `color.accent.campaignInk` 🚧 / `color.surface.default` / `color.surface.subtle` / `color.surface.inverse` / `color.border.subtle` / `color.border.default` / `border.width.thin` / `color.accent.campaign` / `color.text.onAccent` / `color.text.inverse` / `color.scheme.main.inverse` / `color.scheme.sub.inverse` / `color.text.strong` / shadow 🚧
- 未確定事項: 実px (角丸/影/余白)・8スロット対応付け・画像欠落時の fallback ❓ (Card 実装着手時) / バッジの角丸 (`radius.badge` = 4px・**bound 確定** ✅・Task 009-56)・器の実px (高さ/余白/文字/数字サイズは `label.*` で確定・Task 009-48。accent 濃色段/coral は 🚧 仮色) / 割引率の算出式・端数処理・上限値は上流未決 (`design.md` §8.1) / **1 施設に複数の料金選択肢を並べる横並び構成 (食事条件別の選択肢リスト等) が 8 スロット構造 (単一の `Card.slot.price` を前提) で表現できるか** ❓ (依頼元 2026-08-03・依頼 D-8。Task 009-39 で受理。既存の実px・8スロット対応付けの実査待ちとは別論点) / 会員種別 (無料/有料) の用途色 = **実定義済み** ✅ (`{color.membership.paid}` 🚧 仮色 / `{color.membership.free}`・Task 009-52・`governance/owner-decisions.md` §24)。会員限定ラベルとカテゴリラベルの区別は面色使い分け (§19) に沿い、C カテゴリ・特集の用途色 = **実定義済み** ✅ (`{color.label.category}` = 白面 + `{color.text.strong}` + accent アイコン・accent の帰属は「面 = B 会員種別 / 点 (アイコン) = C 特集」で確定・Task 009-60・`governance/owner-decisions.md` §27)。**白系の面の上に置く場合の分離手段** = **確定** ✅ (`{color.label.category.border}` = `{color.border.default}` `#CCCCCC` の 1px 枠線・白系の面の上に置く場合のみ・Task 009-60R・`governance/owner-decisions.md` §27-3 ⓕ)。**残る未定義事項** ❓: C ラベルの**アイコンの字形とサイズ** (**字形**は `design.md` §6 がアイコン体系を Font Awesome 6 と定めるのみで、個々のラベルへの割当規則が本書・`design.md` のいずれにも無い。**サイズ**は `iconSize.sm〜xl` の最小段が 16px で、器 sm = 高さ 20px・文字 12px に当てる値が本書・`design.md` のいずれにも無い。`design.md` 未確定事項の一覧) / バッジ/ラベルの白文字非準拠 = **実規則化済み** ✅ (**A 割引率ラベル + scheme 逆色面 に限る**白文字例外・サイズ/ウェイト不問・AA 未達明示・Task 009-48・`design.md` §2.1「A 割引率ラベルに限る白文字の例外」・`governance/owner-decisions.md` §24)。**2026-09-05 に適用範囲を縮小** — Task 009-60 で C カテゴリ・特集ラベルを白面へ確定したことに伴い、当初の「非操作の点的ラベル + campaign accent/scheme 逆色面」から用途を **A 割引率ラベルに**、面を **scheme 逆色に**限る形へ改め、campaign accent 面 + 白文字を例外から外した (`governance/owner-decisions.md` §27) / 割引率の表記の基本形 = **実改訂済み** ✅ (§8.1 で `-NN%` → `NN%OFF`・数字強調・Task 009-51・`governance/owner-decisions.md` §24)。本 Card の §8.1 参照 (Do・共通事項の割引率表記行) を `NN%OFF` へ整合済み

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
- 構成: リンク (`{color.text.link}` = 主色・TVL-0011) + 区切り + 現在地 (`{color.text.mutedStrong}` #616161・白背景 6.19:1)
- Do: 現在地はリンク化しない
- Don't: 現在地へ `{color.text.muted}` (#9e9e9e・白背景 2.68:1) を使わない (通常テキストの 4.5:1 に達しない。正は `design.md` §2.1 の検証表・§2 の [事実])
- リンク部分の状態ごとの文字色は `design.md` §2.2 に従う (hover = `{color.text.linkHover}` / active = `{color.text.linkActive}` / visited = `{color.text.link}` を維持 / focus = `{color.focus.ring}` の `outline`)
- 未確定事項: パンくずのリンクへ下線の既定を及ぼすかは未判定 (`design.md` §2.2 が定めた**下線**の既定は文中リンクを対象とし、パンくずは領域とレイアウトでリンクが成立する standalone 側にあたる)

## Modal / Overlay

- ステータス: Draft
- 用途: 重ね合わせ UI
- 実装基盤: **最終的に drawer へ全面統一**。新規は drawer で実装。centered dialog は deprecated (移行期間中は併存)。現在の方針根拠は `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**)。`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認のため、現存する正本・現在の仕様根拠として扱わない
- 表示形態 (form): `drawer` (既定) / `sheet` / `popover` の 3 値 (`design.md` §7.1 が正)。実装基盤は drawer 単一を維持し **第3の Modal 実装基盤を導入しない** (`popover` は overlay の z 軸・backdrop・dismiss を共有する同一基盤上の表示形態であり第3の実装基盤に当たらない = `governance/owner-decisions.md` §17)。form は variant 語彙 (GOV-0002) とは**別軸** (PriceTag の `tone` と同じ扱い)。配置 = `sheet` は画面下端貼付き・全幅・上端2隅角丸 (`{radius.overlay}`) / `popover` は基準要素を起点に下方余地なしなら上反転・基準要素が必要 / `drawer` は既存記述を変更しない。切替 = `{breakpoint.lg}` (1024px) 未満は `sheet`・以上は `popover` (drawer は既定で切替の対象外)。backdrop (`{color.overlay.backdrop}` 🚧) は 3 形態すべてで使用。実装 API 名 (prop 名) は未確定 ❓
- 移行ロードマップ: **未決**。移行対象・順序・期限・完了条件・具体的なロードマップはいずれも決定されていない。決定する場合は外部実装 Repository の実査が先行する (`governance/owner-decisions.md` §11)
- 状態: open/close 遷移は `{motion.transition.*}` 🚧
- Do / Don't:
  - Do: z 軸は `{elevation.overlay}` / `{elevation.modal}` を使用
  - Do: 表示形態 (form) は明示的に選択する。背景・文脈を検知して自動で形態を切り替えない
  - Don't: 第3のモーダル基盤を導入しない
- 関連トークン: `{elevation.overlay}` / `{elevation.modal}` / `{radius.overlay}` 🚧 / `{color.overlay.backdrop}` 🚧 / `{motion.transition.*}` 🚧 / `{shadow.*}` 🚧
- 未確定事項: 既存 centered dialog の移行対象・順序・期限・完了条件は**未決**。`TVL-0007` で管理されているとは認定しない (ADR 正本が Repository 内に不在・historical provenance 未確認)。詳細は `governance/owner-decisions.md` §11 / form = sheet の最大高・popover の幅段階 (依頼元固有値・未実査)・form の a11y (role / aria-modal / フォーカストラップ / スクロールロック等 = §8K 下流課題)はいずれも未確定 (**最小タップ領域は Task 009-68 で 48px = `{size.tapTarget}` に確定した** = `design.md` §4.2。44px 段の spacing トークンは引き続き追加しない)

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-09 | 0.3.0-draft: 独立DS再構築。GOV-0002 (variant 語彙)・TVL-0006 (FA6)・TVL-0007 (drawer統一)・TVL-0001〜0003 (rem/4px/テキスト2段) を反映 | Claude Design (Builder) |
| 2026-07-28 | Task 009-28R: Modal / Overlay 節の `TVL-0007` への参照・委任表現を補正 (3 箇所)。①実装基盤 = 「drawer に全面統一 (TVL-0007)」を「最終的に drawer へ全面統一」へ改め、現在の方針根拠が `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**) であることと、`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認のため現存する正本・現在の仕様根拠として扱わないことを明記。あわせて「移行期間限定」を「移行期間中は併存」へ改め、現在判断の内容と一致させた。②「移行ロードマップは TVL-0007 参照」という**存在しない委任先にロードマップが存在すると読める表現を削除**し、移行対象・順序・期限・完了条件・具体的ロードマップがいずれも未決であること、決定する場合は外部実装 Repository の実査が先行することへ補正。③未確定事項 = 「既存 centered dialog の移行対象・順序 (TVL-0007 で管理)」を、移行対象・順序・期限・完了条件が未決であり `TVL-0007` で管理されているとは認定しない旨へ補正。**現行仕様そのものは不変** (最終的な drawer への統一・新規は drawer で実装・centered dialog の deprecated・移行期間中の併存・第3の Modal 実装基盤を導入しないはいずれも維持)。判断日 (2026-07-27) と本反映日 (2026-07-28) は別の事象として区別している。本工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-07-28、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。Modal / Overlay 節の 用途・ステータス・状態 (`{motion.transition.*}` 🚧)・Do (`{elevation.overlay}` / `{elevation.modal}`)・Don't (第3のモーダル基盤を導入しない)、他 Component の仕様、token の値・参照・`$status`・`$description`・`$note`、version・正式 Status、Modal の具体的なライブラリ・モジュール・DOM 構造、open／close・focus・scroll lock・backdrop・dismiss 等の具体挙動、rental-car / inbound の成果物は不変。3DS 横断 Q9 の未決状態・`TVL-0007` の historical provenance 未確認・`alignment-blocking-facts-resolution-plan.md` §8L の R-D 分類は変更していない。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-33: 共通事項にテキスト色 4 段 (`{color.text.strong}` / `{color.text.body}` / `{color.text.mutedStrong}` / `{color.text.muted}`) の使用ルールを [事実] として 1 行追加した。判読性を必要とする補助情報 (補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件) は `{color.text.mutedStrong}` (#616161・白背景 ≈6.2:1) を使用し、`{color.text.muted}` (#9e9e9e・白背景 ≈2.7:1) は通常テキストに求められる 4.5:1 に達しないため判読性を要する情報には用いない。適用規格・達成レベルの正式確定・適合判定・適合宣言は本書では行わない。PriceTag の構成行を「補助価格・価格条件注記 (税・人数・泊数等)・割引前価格」へ改め文字色を `{color.text.mutedStrong}` へ変更し、Do 1 行・Don't 1 行・関連トークン行を追加した。**不変**: Button / Input / SearchForm / Card / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、PriceTag の用途・ステータス・数字と「円」の構成・「円」weight 600 の未確定事項、Breadcrumb 現在地の `{color.text.muted}`、トークンの値・参照先・`$status`、primitive の色値、version 表記、UI 構造・Component API・DOM 構造、rental-car / inbound の成果物。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-34: **共通事項に 5 行追加**した。①テキスト 4 段は明色面用であり inverse 面は `{color.text.inverse}` (主要文字) / `{color.text.inverseMuted}` (補助情報) の 2 段を使うこと (`{color.text.inverseMuted}` を明色面へ・`{color.text.mutedStrong}` を inverse 面へ使用しない) ②面と文字色の組み合わせ条件 (campaign accent を面として使用できるのは (a) 24px 以上または (b) 20px 以上かつ bold・ウェイトの境界は bold = 700 以上／通常ウェイト = 700 未満・scheme inverse 面は main `#C8912C` / sub `#C8B12C` を個別に扱う) は `design.md` §2.1 が正であり `{color.text.onAccent}` の存在を理由にコントラスト確認を省略しないこと ③背景文脈は明示的な tone / variant として選択し、背景色検知による自動反転・内部固定色のみでの複数背景対応・primitive 直接参照・任意 HEX 指定・global token のローカル再束縛を採らないこと ④角丸の用途トークン 3 系統 (`{radius.action}` / `{radius.card}` / `{radius.badge}`) と非操作ラベルへ pill を使わないこと・操作可能なバッジは action 系として扱うこと ⑤割引率の表記規則は `design.md` §8.1 が正であること。**Card (ResultCard)** に `Card.slot.badge` の規則を追加した — 角丸 `{radius.badge}` 🚧、面と文字色の文字サイズ・ウェイト分岐 ((a) 24px 以上 (ウェイトを問わない) または (b) 20px 以上かつ bold = `{color.accent.campaign}` 面 + `{color.text.onAccent}`／それ以外 = (i) 20px 未満のすべてと (ii) 20px 以上 24px 未満かつ通常ウェイトを含み、campaign accent を面として使わず既定は `{color.surface.inverse}` 面 + `{color.text.inverse}`)、Do 2 行 (割引率表記は `design.md` §8.1 に従い表示成立条件を満たさない場合はラベル自体を表示しない・色のみで伝えない)、Don't 4 行 ((a) (b) を満たさない文字への白文字・縁取り/影による代替・評価色の販促流用・操作可能なバッジを badge のまま扱うこと)。関連トークン行・未確定事項行も更新した。**PriceTag に tone (背景文脈) を追加**した — `default` (明色面) / `inverse` (inverse 面) の 2 値、要素 3 種 (主要価格・補助価格/価格条件注記/割引前価格・その他の本文) × tone 2 値の対応表、対応する面の対応関係、Do 1 行 (inverse 面での tone 切替)、Don't 4 行 (inverse 面へ `{color.text.mutedStrong}`・明色面へ `{color.text.inverseMuted}`・primitive 直接参照/任意 HEX/ローカル再束縛・背景色検知による自動反転と内部固定色のみでの対応)、関連トークン行、未確定事項 2 件 (tone の実装 API 名・`{color.surface.inverse}` 以外の暗色面での適用可否)。構成行 2 件の文字色指定を tone 別 (下表) 参照へ改め、既存 Do 1 行の冒頭に「明色面では」の限定を補った。`tone` は variant 語彙 (GOV-0002) とは別軸であり variant 語彙への追加ではない。実装 API 名 (prop 名) は未確定として扱う。**不変**: Button / Input / SearchForm / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、Card のスロット責務名・バリアント・既存 Do/Don't、PriceTag の用途・ステータス・数字と「円」の構成・「円」weight 600 の未確定事項・既存 Do 1 行と Don't 2 行、共通事項の既存 6 行、token の値・参照先・`$status`、primitive の色値、version 表記。**作成していないもの**: 新規 Component (badge は既存の `Card.slot.badge` の規則として記載)、画面制作側の JSX / CSS / 生成バンドルの変更、価格算出ロジック。適用規格・達成レベルの正式確定・適合判定・適合宣言は本書では行わない。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。改訂着手の設計承認は取得していない (同 §9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-35: **共通事項に 3 行追加**した。①見出しは文書レベル (h1〜h6) と Component で同一トークン群 `{font.heading.*}` を共用し、割当 (h1 2.5rem / h2 2rem / h3 1.5rem / h4 1.25rem / h5 1.125rem / h6 1rem・ウェイト `{font.heading.weight}` 700・行間 `{font.heading.lineHeight}` 1.3) は `design.md` §3.1 が正であること、Component が既定から外れる値を必要とする場合は当該 Component の項へ明示記載すること (暗黙の上書きを認めない)、明朝 `{font.display.family}` は明示的に選択する書体であり見出しの既定ではないこと。②リンクは色に加え状態ごとの文字色 (hover = `{color.text.linkHover}` / active = `{color.text.linkActive}` / visited = 専用色なしで `{color.text.link}` 維持 / focus = `{color.focus.ring}` outline) を使用し、文中リンクには下線を付し hover で下線を外さないこと、standalone なリンク (カード全体リンク・ナビゲーション項目・パンくず) への下線の既定は未判定で状態ごとの文字色は対象を限定しないこと、リンクの状態表現に `opacity` を用いず共通事項の暫定参照から除外していること。③プレースホルダ文字色は `{color.text.placeholder}` (#616161・≈6.2:1) を使用し `{color.text.muted}` (#9e9e9e・≈2.7:1) を流用しないこと、必須項目・ラベル・エラーメッセージ・入力形式の説明の代替に用いないこと。**共通事項の既存 1 行を改訂**した — 「全 Component の hover は opacity 変化 (≈0.85) を暫定参照とし `🚧 暫定` を付す」に**リンクの hover を対象外とする除外を追記**し (リンクは `design.md` §2.2 の色変更を用い確定値のため `🚧 暫定` を付さない)、あわせて `follow-up #4` の範囲との対応を保った。**Button** の hover 行に、`Button.text` は文字色に `{color.text.link}` を用いるがその hover を `{color.text.linkHover}` と同一視せずボタンの hover は共通事項の暫定参照に従う旨 (hover 以外の状態一式は `follow-up #4` で未取得) を追記し、同行の `follow-up #4` の位置を hover から hover 以外の状態一式へ改めた。**Input** に構成行 (入力値 `{color.text.body}` / プレースホルダ `{color.text.placeholder}`) を追加し、Do 1 行・Don't 1 行を追加、関連トークン行を `color.text.*` から `color.text.body` / `color.text.placeholder` へ具体化した。**Breadcrumb** にリンク部分の状態ごとの文字色の行と未確定事項 1 行 (パンくずのリンクへ下線の既定を及ぼすかは未判定 = standalone 側) を追加した。**不変**: 共通事項の他の既存行、SearchForm / Card / PriceTag / ReviewStars / Header / Footer / Modal の仕様、Button のバリアント・Do / Don't・関連トークン・未確定事項・active / disabled / loading / focus の記述、Input のステータス・用途・バリアント・状態 (error / focus / disabled / success の 🚧)・未確定事項 (`follow-up #2`)、Breadcrumb の構成・Do、`{color.text.link}` / `{color.text.muted}` / `{font.heading.family}` / `{font.heading.h2Size}` の値・参照先・`$status`、primitive の値、version 表記、UI 構造・Component API・DOM 構造、rental-car / inbound の成果物。**行っていないもの**: 状態固定リスト (命名規則§2) への追加、variant 語彙 (GOV-0002) への追加、新規 primitive の追加、reset / base 層の CSS 実装方針の策定、実装ファイルの変更。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-38: `Card.slot.badge` に割引ラベルの面色 (c1・Web部責任者判断 2026-08-03) を追記。**scheme 逆色面**は 面 `{color.scheme.main.inverse}` (#C8912C・副色文脈は `{color.scheme.sub.inverse}` #C8B12C) + 文字 `{color.text.strong}` に固定 (main 5.78:1 / sub 7.50:1・白文字 2.78:1 / 2.15:1 は使用しない・評価色 `{color.icon.rating}` トークンを面へ流用しない)。**小サイズ (例 12px) の accent 淡色面 (b2)** は Web部責任者が新設方向を選択済みだが accent 淡色段の実色値が未取得のため未追加で、取得までは 12px は既定 (neutral dark 面) を用いる旨を追記 (正本 = `governance/owner-decisions.md` §13・`design.md` §2.1)。関連トークン行に `{color.scheme.main.inverse}` / `{color.scheme.sub.inverse}` / `{color.text.strong}` を追加。**不変**: Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、共通事項、`Card.slot.badge` の既存の角丸・(a)(b) 分岐・既定の neutral dark 面・Do / Don't、token の値・参照先・`$status`・version、primitive の色値、rental-car / inbound の成果物。**追加していないもの**: 新規 primitive・新規 semantic 用途トークン・単体 Component。引用したコントラスト比は `design.md` §2.1 の表と一致 (main 5.78:1 / sub 7.50:1)。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-39: 依頼元 (2026-08-03) の依頼 D「Component の不足」に対応 (受理と分類のみ)。共通事項の未着手 Component 一覧に Pagination / Badge (単体) / Stepper / Empty state を追加 (依頼 D で受理・Tabs / Select は従来から記載済み・各 Component の実体データ/実装実査の有無は個別)。共通事項に **Badge (単体) Component の切り出し境界** (定義済みの `Card.slot.badge` と単体 Component の追加範囲 = Card 外配置・サイズ段階・操作可能時 = action 系 を分離・既存の境界は再定義しない) と、依頼 D の新規 Component の**定義工程への着手が Web部責任者判断 2026-08-03 で可** (改訂着手の可否のみ・正本 = owner-decisions.md §15・Work Order 6 の 12 候補とは別) である旨を [事実] として追加。**Card (ResultCard) の未確定事項に D-8** (1 施設に複数の料金選択肢を並べる横並び構成が 8 スロット構造で表現できるか・既存の実px/8スロット対応付けとは別論点) を 1 件追加。**不変**: Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、Card のスロット責務名・バリアント・既存 Do/Don't・既存の未確定事項、共通事項の他の既存行、token の値・参照先・`$status`・version、primitive の色値、rental-car / inbound の成果物。**新設していないもの**: Component 仕様・variant 語彙 (GOV-0002)・状態固定リスト (命名規則§2)・新規 primitive/semantic トークン。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-40: 依頼元 (2026-08-03) の依頼 E-5「繰り返し要素内の CTA」に対応 (Web部責任者判断)。**Button の Do「1 画面の主 CTA は `primary` 1 つに絞る」を撤回**し、CTA の優先度は `primary` / `secondary` / `ghost` / `text` の強弱階層で表現すること・**主 CTA の個数制約は設けない**こと・繰り返し要素 (検索結果カード等) 内で各項目が `primary` を持つことを妨げないこと (正本 = `governance/owner-decisions.md` §16) へ改めた。**不変**: Button の他の Do / Don't・バリアント・状態・関連トークン・未確定事項、Input / SearchForm / Card / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、共通事項、token の値・参照先・`$status`・version、primitive の色値、rental-car / inbound の成果物。**新設していないもの**: variant 語彙 (GOV-0002)・状態固定リスト・新規 primitive/semantic トークン。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-03 | Task 009-36: 依頼元の依頼 D-6 に対応し Modal / Overlay 節に表示形態 (form) を追加。form = drawer (既定) / sheet / popover の 3 値 (`design.md` §7.1 が正)・実装基盤は drawer 単一を維持し第3の Modal 実装基盤を導入しない (popover は同一基盤上の表示形態で第3基盤に当たらない = governance/owner-decisions.md §17)・form は variant 語彙とは別軸・配置 (sheet = 下端貼付き全幅・上端2隅 `{radius.overlay}` / popover = 基準要素起点で下方余地なしなら上反転・基準要素が必要 / drawer 不変)・切替 (`{breakpoint.lg}` 1024px 未満 = sheet / 以上 = popover)・backdrop `{color.overlay.backdrop}` を 3 形態共通・実装 API 名は未確定 を追記。Do に「form は明示的に選択する (自動切替しない)」を追加。関連トークン行 (`{elevation.overlay}` / `{elevation.modal}` / `{radius.overlay}` / `{color.overlay.backdrop}` / `{motion.transition.*}` / `{shadow.*}`) と未確定事項 (sheet 最大高・popover 幅段階・form の a11y = §8K 下流課題・最小タップ領域 44px は追加せず) を追記。**共通事項**の角丸を 3→4 系統へ (`{radius.overlay}` 追加)。**不変**: Modal の既存記述 (drawer 統一・centered dialog deprecated・移行未決・第3基盤を導入しない Don't)、他 Component の仕様、共通事項の他の行、token の値・参照先・`$status`・version、rental-car / inbound の成果物。**新設していないもの**: variant 語彙 (GOV-0002)・状態固定リスト・Modal の具体的ライブラリ / DOM 構造 / open・close / focus / scroll lock / dismiss 等の挙動。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-43: 依頼元 (2026-08-04・依頼A + 判断点7) に対応 (受理と分類)。**Card の未確定事項に 1 件追加**した — 会員限定 (有料会員限定) ラベルをカテゴリラベルと区別するか (🚧 区別する方向・手段 = 面色使い分け 基本 neutral / 特集 accent / 例外 inverse・既存トークンの範囲に限定・実定義は別 Task・正本 = `governance/owner-decisions.md` §19・面色成立は `design.md` §2.1 と Task 009-44 に重なる)。**不変**: `Card.slot.badge` の規範規則 (角丸・(a)(b) 分岐・面色・Do / Don't)、Card のスロット責務名・バリアント・既存 Do/Don't・既存の未確定事項、Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、共通事項、token の値・参照先・`$status`・version (`color.text.onAccent` は既 `bound`)、primitive の色値、rental-car / inbound の成果物。**新設・変更していないもの**: 会員限定ラベルの用途トークン・区別規則の実定義・新色値/新面色用途・variant 語彙 (GOV-0002)・状態固定リスト。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-44: 依頼元 (2026-08-04・依頼B + 判断点2/4) に対応 (受理と分類)。**Card の未確定事項に 1 件追加**した — バッジ/ラベルの白文字非準拠 (割引率 `#C8912C` 面/白・小サイズ campaign accent 面/白) の扱い (🚧 現行の面色規則に不適合・非操作の点的ラベル + campaign accent/scheme 逆色面 に限り白文字を例外許容する方向・AA 未達明示・実規則化は別 Task・現行規則は維持・正本 = `governance/owner-decisions.md` §20)。**不変**: `Card.slot.badge` の規範規則 (角丸・(a)(b) 分岐・**逆色面 `{color.text.strong}` 固定・白文字を使用しない**・(i)(ii) に campaign accent を面として使わない・Do / Don't)、Card の他のスロット責務名・バリアント・既存 Do/Don't・既存の未確定事項、Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、共通事項、token の値・参照先・`$status`・version、primitive の色値、rental-car / inbound の成果物。**新設・変更していないもの**: 面色・コントラスト規則の実緩和・例外条項の実追加・新色値/新面色用途・variant 語彙 (GOV-0002)・状態固定リスト。影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-04 | Task 009-45: 依頼元 (2026-08-04・判断点5 + DS-REQUEST「割引率の表記規則 (§8.1)」) に対応 (受理と分類)。**Card の未確定事項に 1 件追加**した — 割引率の表記の基本形が §8.1 で `-NN%` → `NN%OFF` へ変更される方向 (🚧 Task 009-45・Web部責任者判断 2026-08-04・§8.1 本体の実改訂は別 Task・正本 = `governance/owner-decisions.md` §21)。本 Card の §8.1 参照 (`Card.slot.badge` Do・共通事項の割引率表記) は §8.1 実改訂時に整合予定・現時点では未改訂。**不変**: `Card.slot.badge` の Do「割引率の表記は `design.md` §8.1 に従う (`-NN%`)」・共通事項の割引率表記行 (`-NN%`)・その他の規範規則、Card の他のスロット責務名・バリアント・既存 Do/Don't・既存の未確定事項、Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、共通事項の他の行、token の値・参照先・`$status`・version、primitive の色値、rental-car / inbound の成果物。**変更していないもの**: §8.1 の実改訂・割引率表記の `-NN%` 参照 (実改訂は別 Task)・variant 語彙 (GOV-0002)・状態固定リスト。影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-08-10 | Task 009-48/009-49/009-51/009-52/009-56 (ラベル・タグ定義シート A〜G の実装。009-56 = radius.badge の bound 反映・器の実px): **`Card.slot.badge` の (i)(ii) 代替を 2 択化** (① 既定 neutral dark 面 / ② accent 淡色面 `{color.accent.campaignTint}` + 濃色文字 `{color.accent.campaignInk}` = b2・🚧 仮色は実色値確定後に検証)。**逆色面に「非操作の点的ラベルに限る白文字の例外」**を追加 (逆色面/campaign accent 面 + 白文字・AA 未達明示・サイズ/ウェイト不問・`{color.label.discount}`)。**器 (寸法・2 サイズ)** を追加 (`{label.height/paddingInline/lineHeight/fontSize/numberSize/weight/radius}`・高さ sm20/md24・左右 8/12・文字 12/14・数字は 1 段上 14/16)。**ラベル種別と用途色**を追加 (A `label.discount` / B `membership.paid`🚧`/free` / D `tag.neutral` / E1 `label.stock` / C 据え置き / F 面なし行 / G pill 対象外)。角丸を `{radius.badge}` bound (4px) へ・§8.1 参照を `NN%OFF`・数字強調へ整合。共通事項の割引率表記行も `NN%OFF` へ。未確定事項の白文字非準拠/§8.1/会員種別/radius.badge を実装済み・bound へ更新。正本 = `governance/owner-decisions.md` §24。**不変**: Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、Card のスロット責務名・バリアント・(a)(b) 分岐の境界、既存 Do/Don't、rental-car / inbound の成果物。トークンの実体追加は別 PR (semantic/primitive)。影響度 = **高** (判定者 = Web部責任者・判定日 2026-08-10・§24)。改訂着手の設計承認取得済み (§9・§20・§24)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-05 | Task 009-60: **`Card.slot.badge` の C カテゴリ・特集の用途色を確定**した ([Issue #162](https://github.com/tocoo/coocom-design-system/issues/162)・正本 = `governance/owner-decisions.md` §27・Web部責任者判断 2026-09-05)。**ラベル種別と用途色の C 行**を「仮決定 (accent の帰属未定) のため据え置き」から実定義へ置換 — **C カテゴリ・特集** = `{color.label.category}` (面 `{color.label.category.surface}` 白 #FFFFFF + 文字 `{color.label.category.text}` #212121 = ≈16.10:1 + アイコン `{color.label.category.icon}` campaign accent #E4572E)。**accent は面ではなくアイコン (点) として持つ** — accent を面として持つのは B 会員種別 (`{color.membership.paid}` = accent 淡色段) のみとする用途分離により、accent の帰属を確定した。器は sm (12px)・ウェイトは既存規則どおり `{label.weight.emphasis}` (700)・白面は (a) (b) 分岐に依存せず成立するため 12px でも (i) (ii) の代替 2 択を要しない旨を明記。**白文字例外条項の適用範囲を縮小** — 「逆色面または campaign accent 面 + 白文字を**非操作の点的ラベルに限り**許容」から「逆色面 + 白文字を **A 割引率ラベルに限り**許容」へ改め、campaign accent 面 + 白文字を例外から外し、(i) (ii) の白文字禁止と代替 2 択を例外なく維持することを明記した (A 以外の非操作ラベル = B / C / D / E と操作可能なバッジはいずれも対象外)。**関連トークン行**に `color.label.category` を追加。**未確定事項**の「C カテゴリの用途色は accent 帰属未定のため据え置き」を **実定義済み** ✅ へ更新し、派生する未定義事項 ❓ 1 件 (白面の C ラベルを白系の面の上に置く場合の分離手段 = 境界線の要否) を明記した。**不変**: `Card.slot.badge` の角丸 (`{label.radius}` = `{radius.badge}` 4px)・器 (`label.*` の高さ/余白/文字/数字サイズ/ウェイト)・A / B / D / E1 / F / G の用途色・(a) (b) 分岐の境界・(i) (ii) 代替 2 択 (① neutral dark 面 / ② accent 淡色面 b2)・割引ラベルの逆色面 `{color.text.strong}` 固定・b2 の 🚧 仮色の扱い・Do / Don't の各行、Card の他のスロット責務名・バリアント・既存 Do/Don't、Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、共通事項、token の値・参照先・`$status`・version、primitive の色値、rental-car / inbound の成果物。**新設・変更していないもの**: 新規 Component・variant 語彙 (GOV-0002)・状態固定リスト・新しい色値 (`color.label.category` の 3 件はいずれも既存 semantic への参照)・白面 C ラベルの境界線の規定・placeholder の bound 昇格。改訂着手の設計承認取得済み (§9・§20・`governance/owner-decisions.md` §27-1)。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-05・本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-05 | Task 009-60R (PR [#165](https://github.com/tocoo/coocom-design-system/pull/165) のコードレビュー指摘に対応): **未確定事項の「バッジ/ラベルの白文字非準拠」行を縮小後の範囲へ是正** — 同行は「非操作の点的ラベル + campaign accent/scheme 逆色面 に限る白文字例外」と Task 009-60 の縮小前のまま残っており、同じファイルの `Card.slot.badge` 例外条項 (「campaign accent 面 + 白文字は本例外に含めない」) と**矛盾していた**。用途 = **A 割引率ラベル**・面 = **scheme 逆色面**へ是正し、2026-09-05 の縮小の経緯を追記した (`design.md` §2.1 の同条項は「**A 割引率ラベルに限る白文字の例外**」へ改称・本書の引用 2 箇所を新見出し名へ更新)。**C 行に枠線の規則を追加** — 白系の面 (`{color.surface.default}` / `{color.surface.subtle}`) の上に置く場合にのみ `{color.label.category.border}` (= `{color.border.default}` `#CCCCCC`) を `{border.width.thin}` (1px) で引き、写真の上・有色面の上では引かない (Web部責任者判断 2026-09-05・正本 = `governance/owner-decisions.md` §27-3 ⓕ)。枠線は白面上 ≈1.61:1 で**非テキスト UI 要素の 3:1 に達しない**ことを明示する。未確定事項の「分離手段」を ❓ → ✅ **確定**へ更新し、**アイコンのサイズが未規定**であることを ❓ として残した (`iconSize.sm〜xl` の最小段 16px に対し器 sm は高さ 20px・文字 12px)。関連トークンに `color.label.category.border` / `color.border.default` / `color.surface.subtle` / `border.width.thin` を追加。**不変**: Button / Input / SearchForm / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、Card のスロット責務名・バリアント・(a) (b) 分岐の境界・(i) (ii) 代替 2 択、白文字例外の適用範囲そのもの、`color.label.category` の `surface` / `text` / `icon` の値と参照先、共通事項、version。**新設・変更していないもの**: 新規 Component・variant 語彙 (GOV-0002)・新しい色値 (`border` は既存 semantic への参照)・アイコンサイズの値・placeholder の bound 昇格。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-05。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-05 | Task 009-61 ([Issue #166](https://github.com/tocoo/coocom-design-system/issues/166)): `Card.slot.badge` の **C カテゴリ・特集のアイコンの未規定範囲に「字形」を加える是正**。「**アイコンのサイズは未規定**」および未確定事項の「残る未定義事項」の記述はいずれも対象を**サイズのみ**としていたが、字形 (どのアイコンを用いるか) も本書・`design.md` のいずれにも定めがない (`design.md` §6 はアイコン体系を Font Awesome 6 と定めるのみで、個々のラベルへの割当規則を持たない)。両箇所を「**字形とサイズ**」へ広げ、字形とサイズそれぞれについて未定義である根拠を分けて記した。正本の一覧は `design.md` 未確定事項の一覧 (同日 Task 009-61 で同旨の是正)。**不変**: C の用途色 (`{color.label.category}` の面・文字・アイコン・枠線)・accent の帰属 (面 = B 会員種別 / 点 = C 特集)・枠線の規則 (白系の面の上に置く場合のみ 1px)・器とウェイト (sm 12px・`{label.weight.emphasis}` 700)・A 割引率ラベルの白文字例外の範囲・他の未確定事項の各項。**作成・追加していないもの**: 字形の割当規則そのもの・アイコンサイズのトークン | Claude Code |
| 2026-09-07 | Task 009-62: **共通事項の見出し割当の記述を更新**した ([Issue #168](https://github.com/tocoo/coocom-design-system/issues/168)・正本 = `design.md` §3.1・`governance/owner-decisions.md` §28・Web部責任者判断 2026-09-07)。`{font.heading.*}` の割当を幅ごとの 2 組 (**`breakpoint.lg` 1024px 以上の既定** = h1 2.5rem / h2 2rem / h3 1.5rem / h4 1.25rem / **h5 1rem** / h6 1rem、**1024px 未満** = h1 2rem / h2 1.5rem / h3 1.25rem / h4〜h6 1rem) として記載し、段を移す境界が 1024px の 1 つのみであること、この表の範囲内での段下げは §3.1 の「既定から外れる」に該当せず都度の承認を要しないこと、文書レベルの見出しには実寸が 4 の倍数である段のみを用いること (`sm` 14px は `label.*` の器トークンで用いる段のため本規則の対象外) を追記した。`{font.heading.h5Size}` の参照先が `{typography.size.lg}` (18px) から `{typography.size.md}` (1rem) へ変わったことによる記述の同期である。**不変**: 共通事項の他の行、Button / SearchForm / Input / Card / PriceTag / ReviewStars / Breadcrumb / Header / Footer / Modal の仕様、`Card.slot.badge` のラベル種別と用途色・器トークン `label.*` (`fontSize` / `numberSize` / `height` / `paddingInline` / `lineHeight` / `weight` / `radius`) の値と参照先、`{font.heading}` の他のトークン、version 表記、rental-car / inbound の成果物。**行っていないもの**: Component 仕様への幅ごとの値の追加、新規 primitive・semantic トークンの追加、実装ファイルの変更。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-07・本件について明示取得) | Claude Code |
| 2026-09-07 | Task 009-64: **`Breadcrumb` の現在地の文字色を変更**した ([Issue #172](https://github.com/tocoo/coocom-design-system/issues/172)・Web部責任者判断 2026-09-07・明示取得・正本 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §30 判断 G-1)。構成行の現在地を `{color.text.muted}` (#9e9e9e・白背景 **2.68:1**) から **`{color.text.mutedStrong}`** (#616161・白背景 **6.19:1**) へ改め、現在地へ `{color.text.muted}` を使わない Don't を 1 行追加した。従前の記述は `design.md` §2 の [事実]「`color.text.muted` は通常テキストに求められる 4.5:1 に達しないため判読性を要する情報には用いない」と食い違っており、同 §2.1 の検証表にも当該組み合わせの行が無いまま (表は「表に無い組み合わせを検証済みとして扱わない」と宣言) 使用されていた。**新しい色値・新しいトークンは追加していない** (`{color.text.mutedStrong}` は既存 bound トークン)。あわせて非正本の [preview.travel.html](preview.travel.html) の Breadcrumb 見本 (`.crumb__current`) と caption を本変更へ追随させた。**不変**: `Breadcrumb` の用途・ステータス・Do (現在地はリンク化しない)・リンク部分の状態ごとの文字色・未確定事項 (下線の既定は未判定)、他 Component の仕様、共通事項、`{color.text.muted}` / `{color.text.mutedStrong}` の値・参照先・`$status` (トークンの追加・削除・変更は **0 件**)、Input / PriceTag の `{color.text.muted}` に関する既存 Don't、rental-car / inbound の成果物。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-07・本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-15 | Task 009-68: **`Select` 節を新設**し、共通事項へ最小タップ領域と角丸 5 系統を反映した ([Issue #180](https://github.com/tocoo/coocom-design-system/issues/180)・Web部責任者判断 2026-09-15・正本 = `governance/owner-decisions.md` §34・`design.md` §4.1 / §4.2 / §5 / §2.3)。①**`Select` 節を追加**した — 器 (高さ `{size.tapTarget}` 48px / 枠線 `{border.width.thin}` × `{color.border.default}` / 面 `{color.surface.default}` / 角丸 `{radius.select}` 8px)、余白 (`{select.paddingInline}` 12px + シェブロン領域)、文字 (`{font.body.family}` / `{font.body.size}` 16px / 選択済み `{color.text.body}` / 未選択 `{color.text.muted}` = AA 未達を明示)、シェブロン (`{select.chevronSize}`・FA6 グリフ・**SVG 画像/データ URI で描かない**)、状態 (focus = `{color.focus.ring}`・error 🚧 暫定・disabled / success 🚧 未取得)、**Modal の表示形態 (§7.1) との使い分け** (1 階層で短い一覧 = Select / 階層あり・件数が多い・他の入力と組み合わせる = sheet / drawer / popover。件数のしきい値は定めない)、Do / Don't、未確定事項。②**共通事項**に、指で操作する要素の最小の高さを `{size.tapTarget}` (48px) とする行を追加し、角丸の用途トークンを **4 系統 → 5 系統** (`{radius.select}` 追加) へ更新し、未着手 Component 一覧から **Select を外した** (8 件へ)。③Modal の未確定事項の「最小タップ領域 44px の spacing トークン (追加せず)」に、Task 009-68 で 48px に確定した旨を追記した (44px 段は引き続き追加しない)。**不変**: Button / Input / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様 (Modal は未確定事項の当該 1 行のみ追記)、`Card.slot.badge` のラベル種別・用途色・器トークン `label.*` の値と参照先、共通事項の他の行、variant 語彙 (GOV-0002)・状態固定リスト (命名規則§2)、token の値・参照先・`$status`・version、rental-car / inbound の成果物。**行っていないもの**: `Input` の角丸・仕様の変更、Select のサイズ段階 (sm/md/lg) の定義、複数選択・検索付き選択の定義、他の未着手 Component の定義、実装ファイルの変更。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-15・本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-15 | Task 009-69: **「選ぶための部品」5 節 (6 Component) を新設**した ([Issue #182](https://github.com/tocoo/coocom-design-system/issues/182)・Web部責任者判断 2026-09-15・正本 = `governance/owner-decisions.md` §35)。①**`Checkbox / Radio`** — ネイティブ `input` を視覚的にのみ隠し (`display: none` は用いない)、箱 (`{control.size}` 16px・`{control.borderWidth}` 2px × `{color.border.strong}`) と印を自前で描く。Checkbox は `{control.radius}` (4px) + `{color.brand.primary}` 面 + `{color.text.inverse}` のチェック印 (`{control.glyphSize}`)、Radio は円 + 中心に `{control.dotSize}` (8px) の点。②**`OptionRow`** (単一選択の行) — 器 `{size.tapTarget}` / `{row.paddingBlock}` / `{row.paddingInline}` / `{row.gap}` / `{row.fontSize}`、選択中は太字 + `{color.text.link}` + チェックアイコンで示し**面は用いない** (面は hover 用)。③**`NavigationRow`** (階層をたどる行) — `OptionRow` と同じ器を共有し、行末にシェブロンと件数を持つ。現在の経路は面 `{color.surface.subtle}` + **太字**で示す (実装は hover と同じ面のみで区別できなかった)。シェブロンは `{color.text.mutedStrong}` を正とする (実装の `color.text.muted` は白面 2.68:1 で非テキスト UI 要素の 3:1 未達)。④**`Chip`** — **用途軸 `use` = `select` / `applied` の 2 値**を定義 (variant 語彙 GOV-0002 への追加ではない・`PriceTag` の `tone` と同じ別軸)。面・枠・文字サイズ・上下余白が `use` ごとに分かれ、`select` の選択中は枠 `{color.brand.primary}` + 面 `{color.scheme.main.tint}` + 太字で示す。⑤**`Tabs`** — 選択中は `{color.text.link}` + 下線 `{tab.indicatorWidth}` (2px) × `{color.brand.primary}` の**両方**で示す。⑥**共通事項**に「状態を色だけで伝えない・hover の表現 (面 `{color.surface.subtle}`) を選択中へ流用しない」を追加し、**未着手 Component 一覧から Tabs を外した** (7 件へ)。**不変**: Button / Input / Select / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、`Card.slot.badge` のラベル種別・用途色・器トークン `label.*`、共通事項の他の行、variant 語彙 (GOV-0002)・状態固定リスト (命名規則§2)、token の値・参照先・`$status`・version、rental-car / inbound の成果物。**行っていないもの**: a11y の実装方式の決定 (§8K の下流課題)、disabled / error / hover の実体の確定 (follow-up #2 / #4)、他の未着手 Component の定義、実装ファイルの変更。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-15・本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-15 | Task 009-70: **「一覧まわりの部品」6 節を新設**した ([Issue #184](https://github.com/tocoo/coocom-design-system/issues/184)・Web部責任者判断 2026-09-15・正本 = `governance/owner-decisions.md` §36)。①**`OverlayTrigger`** — 絞り込み・並び替え・条件のオーバーレイを開く起点。枠線 + アイコン + ラベル + 現在値 + 件数バッジを抱える形であり `Button` の 4 語では代用できないため別 Component とした (§36 M-2)。最小の高さは実装の 44px から `{size.tapTarget}` (48px) へ揃える。②**`DateRangeCalendar`** — 日付の範囲選択。両端は面 `{color.brand.primary}` + `{color.text.inverse}` + 太字 + `{calendar.selectedRadius}`、期間中は面 `{color.surface.subtle}`。**選択不可 (過去日) は実装が `color.text.mutedStrong` + 不透明度 0.45 の暫定表現であり、DS に選択不可の文字色トークンが無い**ため未確定事項として起票した (AA 適合を主張しない)。③**`AvailabilityCalendar`** — 空室状況と料金の一覧。面で在庫状態を分け、選択中の日は内側の枠で示す (面を変えると在庫状態の表示と衝突するため)。**セル高 96px は `spacing` に段が無く単一トークンで表せない**、**料金・在庫の 10px は `typography.size` の 9 段に存在しない派生値**であり、いずれも未確定事項として起票した (本書は 10px を正としない)。④**`RangeSlider`** — 軌道 4px・つまみ 16px・当たり判定 24px。`{size.tapTarget}` は独立した操作要素の最小の高さであり軌道上のつまみには適用しない旨を明記した。⑤**`Skeleton`** — 線の高さを 4 段 (16 / 24 / 32 / 40px) で定義。**カード外形は `{radius.card}` を正とする** — 実装は `radius.lg` (16px) を用いており用途トークンと食い違っていた (§36 M-3。`radius.card` の placeholder は解消しない)。⑥**`StickyBar`** — 上端に貼り付く帯。z 軸 `{elevation.sticky}`、帯の中の操作要素も `{size.tapTarget}` を満たす。⑦**共通事項**の未着手 Component 一覧の記述を更新した (Task 009-69 / 009-70 で新規定義した 10 件を明記。未着手は 7 件で不変)。**不変**: Button / Input / Select / Checkbox / Radio / OptionRow / NavigationRow / Chip / Tabs / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、`Card.slot.badge` のラベル種別・用途色・器トークン `label.*`、`select.*` / `control.*` / `row.*` / `chip.*` / `tab.*` / `size.tapTarget`、共通事項の他の行、variant 語彙 (GOV-0002)・状態固定リスト (命名規則§2)、token の値・参照先・`$status`・version、rental-car / inbound の成果物。**行っていないもの**: 選択不可の文字色トークンの新設、`spacing` / `typography.size` の段の追加、`radius.card` / `shadow.*` / `motion.*` の placeholder の解消、実装ファイルの変更。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-15・本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-15 | Task 009-71: **未入力状態の文字色の統一を反映**した ([Issue #186](https://github.com/tocoo/coocom-design-system/issues/186)・正本 = `design.md` §2.3・`governance/owner-decisions.md` §37)。①**共通事項**の「入力欄のプレースホルダ文字色は `{color.text.placeholder}`」の行を、**未入力状態の案内文字 (`::placeholder`・Select の未選択値・その他の未入力表示) はすべて `{color.text.muted}` (`#9E9E9E`・2.68:1・AA 未達を明示)・UI の種別で限定しない**へ書き換えた。②**`Input`** の構成とその関連トークンを `{color.text.placeholder}` から `{color.text.muted}` へ変更し、Don't を「未入力の案内文字へ `{color.text.mutedStrong}` を使わない (入力済み `#424242` との濃度差が小さく判別しにくくなる)」へ差し替えた。③**`Select`** の未選択値の記述に「`input` / `textarea` の未入力と同一の扱いであり UI の種別で色を変えない」を明記し、Don't を「未選択であることを色だけで伝えない」へ差し替えた。**不変**: Button / Select (未選択値以外) / Checkbox / Radio / OptionRow / NavigationRow / Chip / Tabs / OverlayTrigger / DateRangeCalendar / AvailabilityCalendar / RangeSlider / Skeleton / StickyBar / SearchForm / Card / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal の仕様、共通事項の他の行、器トークン群 (`label.*` / `select.*` / `control.*` / `row.*` / `chip.*` / `tab.*` / `trigger.*` / `calendar.*` / `availability.*` / `rangeSlider.*` / `skeleton.*` / `stickyBar.*`)、token の値・参照先・`$status`・version、rental-car / inbound の成果物。**行っていないもの**: `AvailabilityCalendar` の空室なしの日付が参照する `{color.text.placeholder}` の変更 (選択不可の用途であり未判定の論点として残す)、実装ファイルの変更。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-15・本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー) | Claude Code |
