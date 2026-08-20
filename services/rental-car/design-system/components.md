# Component 仕様 — 国内レンタカー (rental-car)

- 種別: DS 成果物 (Ph-D Component 仕様)
- 状態: Draft (0.3.0-draft)
- 作成日: 2026-07-02 / 更新日: 2026-08-20
- 参照トークン: `semantic.rental-car.json` のみ (primitive 直接参照は禁止)
- 根拠: オーナー判断 2026-08-18「国内宿泊で新たに定義されたものを適用する」。実装実測は `migration-map.md`、ラベル・タグは `labels-tags.rental-car.md` を参照
- 注記: `TVL-NNNN` は ADR 正本が Repository 内に不在であり、本書では現在の仕様根拠として参照しない

## 1. 共通事項

結論: Component が定義するのは自身の構造・状態・トークン参照だけである。ページの配置と余白は Foundation の責務であり、本書では決めない。

- 状態の固定リスト: `hover / active / focus / disabled / loading / error / success`。追加は決定記録が必要
- hover は `opacity` 約 .85 の暫定 `🚧`。focus は `outline` + `color.focus.ring`
- ボタンは pill (`radius.action`)。実装の 4px 固有形状・グラデ・emboss 影は廃止
- accent (特集色) はバッジ専用で塗りボタンにしない。主 CTA の個数制約は本 DS では設けない (§2 Button の未確定事項を参照)
- 価格は PriceTag (数字 700 + tabular-nums + 「円」 + 補助テキスト) を必ず使う
- 最小タップ領域 44px。コントラストは AA が下限
- アイコンは Font Awesome 6。絵文字は製品コピーに使わない
- travel と同型 (7 件・定義体系の採用。**意匠と値は本 DS のファイルで定義し、travel のファイルを参照しない**): Button / Input / PriceTag / Header / Breadcrumb / Footer / Modal
- 本 DS で先行定義 (3 件・travel 側は未着手): Select / FormLabel / Label・Tag
- レンタカー固有 (8 件): SearchForm / ResultCard / SecretPrice / Options / StorePicker / StepIndicator / Filter / Sort・Pagination

## 2. フォーム系

結論: Button と Input は travel と同型の定義を本 DS のファイルで持つ。Select と FormLabel はレンタカーが時刻・車種条件で多用するため本 DS で先行定義する。

### Button

- バリアント: `primary` / `secondary` / `ghost` / `text` の 4 語。`campaign` は廃止 (accent は塗りボタン禁止)
- 意匠 (4 語すべてに束縛を与える。角丸はいずれも `radius.action` = pill・影なし)
  - `primary` = `color.action.primary.bg` (主色) 面 + `color.action.primary.text` (白) + weight 700
  - `secondary` = `color.action.secondary.bg` (白) 面 + `color.action.secondary.text` (`#212121`) + `border.default` の枠
  - `ghost` = 透明地 + `color.text.strong` の枠と文字。低強調のナビ操作
  - `text` = 透明地 + `color.text.link` の文字。面と枠を持たない低強調のテキスト操作
- 状態: hover = `color.action.primary.hoverBg` または opacity .85 `🚧` / focus = `color.focus.ring` の outline / disabled は `🚧` 未定義 (E2 満車表現の前提となるため優先度が高い)
- サイズ: 標準 44px・SP の全幅 CTA は 48px
- Do: 実装は Semantic のみ参照する。CTA の優先度は `primary` / `secondary` / `ghost` / `text` の強弱階層で表現する
- Don't: 角丸 4px・縦グラデ・text-shadow の旧意匠を再現しない
- 関連トークン: `color.action.primary.*` / `color.action.secondary.*` / `color.text.strong` / `color.text.link` / `radius.action` / `color.focus.ring` / `motion.transition.*` `🚧`
- 未確定事項: disabled・loading の意匠。**繰り返し要素 (ResultCard 等) 内の主 CTA の個数制約** — travel は Web部責任者判断 2026-08-03 ([governance/owner-decisions.md](../../../governance/owner-decisions.md) §16) で「1 画面の主 CTA は `primary` 1 つに絞る」を撤回し個数制約を撤廃したが、同記録は適用範囲を travel に限定している。rental-car への適用判断は未取得であり、本書は個数制約を設けない `🚧`

### Input

- バリアント: `default`。状態: `error` = `color.state.error` / `focus` = `color.focus.ring` / `disabled` `🚧`
- 意匠: 面 `surface.default` + 境界 `border.default` + `radius.input` (4px)。高さ 44px
- Do: エラーはテキストを併記する (色だけで伝えない)
- 関連トークン: `color.border.*` / `color.state.error` / `color.text.*` / `radius.input`
- 未確定事項: 必須表現・検証仕様の実体 (follow-up #2)

### Select

- 位置づけ: travel 側は未着手。レンタカーの時刻・車種条件の多用により本 DS で先行定義する
- 意匠: Input と同一の面・境界・角丸・高さ。右端に `fa-chevron-down` を 16px・`text.mutedStrong` で置き、`appearance: none` で OS 既定の矢印を消す
- 状態: Input に準ずる。open 状態の意匠は OS 依存とし DS では定義しない
- Don't: 選択肢が 2〜3 個で短い場合に Select を使わない (チップまたはラジオにする)
- 関連トークン: Input と同一 + `icon.size`

### FormLabel

- 用途: 入力に紐づく見出し。ラベル・タグ (A〜H) とは別物であり混用しない
- 構成: ラベル文字 (14px・weight 500・`text.body`) + 必須 / 任意の印 + 補足テキスト (12px・`text.mutedStrong`)
- 意匠: 必須 = `state.error` の文字表記 / 任意 = `text.mutedStrong` の文字表記。面を持たない
- Do: 必須の印は色だけでなく文言で示す
- 関連トークン: `color.text.*` / `color.state.error`

### Label / Tag

- 定義本体は `labels-tags.rental-car.md`。本書では重複させない
- 要点のみ: 器は sm (20px / 左右 8px / 12px) と md (24px / 左右 12px / 14px) の 2 段。面ありは 700・中立タグは 400。押せるものだけ pill
- 未確定事項: 要追加トークン 6 件 (同ファイル §4)

## 3. 検索系

結論: 実装は検索経路が 3 系統に分岐しているが、新規制作は単一構造の SearchForm に集約する。

### SearchForm

- 構成: 経路タブ (エリア / 空港 / キーワード) + 出発エリア + 出発日時 + 返却日時 + 車種クラス + 主 CTA
- レイアウト: PC は `minmax(200px, 1fr)` の自動折返しグリッド、CTA は右下。SP は 1 列縦積み、CTA は幅 100% / 高さ 48px
- 意匠: タブは pill のチップ (選択 = 主色塗り / 非選択 = 白面 + `border.default`)
- Do: 出発と返却の対を隣接配置する。日程未定の検索はチェックボックスで CTA の手前に置く
- Don't: 実装の多経路 (13KB + 9KB の分岐) を新規ページへ複製しない
- 関連トークン: Button / Input / Select の参照に準ずる
- 未確定事項: フィールドの必須・任意の別、日時の入力方式 (Popover か native か)

### StepIndicator

- 用途: 検索 → 選択 → 入力 → 確定の進行表示
- 意匠: pill の 4 段。現在地 = 主色塗り + 白文字 / 完了 = `scheme.main.tint` 面 + 主色文字 / 未到達 = 白面 + `border.default` + `text.mutedStrong`。区切りは `fa-chevron-right`
- レスポンシブ: SP は現在ステップのみラベルを出し、他は番号のみ
- 関連トークン: `color.brand.primary` / `color.scheme.main.tint` / `color.text.mutedStrong` / `radius.action`

### StorePicker

- 用途: レンタカー会社・店舗の選択
- 構成: ラジオ (18px) + 店舗名 (14px・700) + アクセスと営業時間 (12px・`text.mutedStrong`) + 距離 (右寄せ)
- 意匠: 行はカード (`surface.default` + `border.subtle` + `radius.card`)。hover で境界を主色へ。行全体を 44px 以上のタップ領域にする
- Do: 送迎有無と空港からの距離を必ず併記する
- 未確定事項: 各社ロゴ素材が未提供 `🚧` (記憶からの再構築は禁止)

## 4. 検索結果系

結論: 宿泊の Card (8 スロット・画像主役) は使わない。レンタカーはスペックと料金内訳が主役であり、固有の ResultCard を持つ。

### ResultCard

- スロット (責務名で呼ぶ): `media` / `title` / `spec` / `options` / `fare` / `price` / `badge` / `actions`
- 構成: 店舗ヘッダー行 (店舗名 + アクセス + バッジ) / 本体 3 列 (画像 200px・スペック `dl`・補足リスト) / 料金行 (5 列 + 価格と CTA の列)
- 意匠: `surface.default` + `border.subtle` + `radius.card` (暫定 md `🚧`)。料金行は `surface.subtle` 面 + 列間 `border.subtle`。スペックの `dl` は点線の下罫
- 画像欠落時は No Image fallback (`surface.muted` 面 + `text.mutedStrong` の文字。比率 4:3)
- 車種クラス名は明朝 (`font.display.family` + `font.display.mdSize` = 18px)。ゴシックの `font.heading.h3Size` はカード見出し用であり車種クラス名には用いない
- Do: スロットは責務名で命名する。料金の内訳は文字で組む
- Don't: 料金列の見出しを画像化しない。写真を opacity で落として売り切れを示さない
- 関連トークン: `radius.card` `🚧` / `color.surface.*` / `color.border.subtle` / `font.display.family`
- 未確定事項: 料金列の実ラベルと実 px (行高・列幅・角丸・影) は実装実査で確定 `🚧`

### SecretPrice

- 用途: 会員限定価格 (卸価格) のマスクと解放
- 状態: `locked` = `mask.secret` (`scheme.main.tint` `#E8EDFB` = B-2 無料会員の面色) 面 + 鍵アイコン + 「ログインすると卸価格が表示されます」+ text ボタン / `open` = PriceTag を表示
- Do: マスクでも面の高さを保ち、解放時にレイアウトが飛ばないようにする
- Don't: グレー板 (#7f7f7f) を敷く旧実装を踏襲しない
- 関連トークン: `color.mask.secret` / `color.text.link`
- 参照: B-2 会員種別の色を当てる 2 箱のうち「価格のマスク表示」に該当 (`labels-tags.rental-car.md` §2)

### Filter

- 配置: PC は結果左の 280px サイドバーに常時表示。SP は追従バーの「絞り込み」から drawer で全画面
- 構成: 見出し + 「すべて解除」+ 条件グループ (チェックボックス + 件数) + 価格スライダー + 適用中チップ
- 意匠: チップは pill の `scheme.main.tint` 面 + `text.strong` + 解除の `fa-xmark`。行は 44px 以上
- Do: 各条件に件数を併記し、0 件の条件は非活性にする。適用中の条件はチップで見せ 1 タップで解除できるようにする
- Don't: 選択のたびに全画面リロードしない。SP で常時展開しない
- 未確定事項: 実装に facet 型の絞り込みは未確認。件数の算出仕様は要件定義待ち `🚧`

### Sort / Pagination

- 方式: トリガー (pill・44px) + 並び替えパネル。国内宿泊の検索結果と同一方式に統一する
- トリガーの構成: 「並び替え」(400・`text.mutedStrong`) + 現在値 (700) + `fa-arrow-down-wide-short`
- パネル: アンカー直下 8px・幅 280px・影は `🚧` 未定義 (semantic に shadow 系トークンがなく実値も未抽出 = [design.md](design.md) §5)・行 48px・選択行は `scheme.main.tint` 面 + 主色のチェック・選択したら閉じる
- SP: 追従バーに絞り込み (件数バッジ) と並び替え (現在値を省略表示) を並置し、押すと Modal の既定形態 (下からの全幅 drawer) で選択する。BottomSheet 候補 (§6) が承認された場合はそちらへ寄せる `🚧`
- Pagination: 40px の pill。現在地は主色塗り + `aria-current`
- Don't: 常時展開の帯 (下線タブ) やチップ列にしない。件数と並び替えを検索条件と同じ面にまとめない
- 移行: 実装の `.sort` 帯は廃止 (`migration-map.md` 参照)

### PriceTag

- 構成: 数字 (`font.price` 700 + tabular-nums) + 「円」 + 補助テキストの 3 スロット
- サイズ: 既定 20px / `lg` は 1 段上。補助テキストは 12px・`text.mutedStrong` (白背景 6.19:1。`text.muted` は 2.68:1 で AA 未達のため用いない)
- Do: 税・条件 (税込 / 3 日間 / 1 日あたり) を必ず補助スロットに併記する
- 関連トークン: `font.price.*` / `color.text.strong` / `color.text.mutedStrong`

## 5. オプション・ナビゲーション・オーバーレイ

結論: Header / Breadcrumb / Footer / Modal は travel と同型の定義を採るが、意匠と値は本 DS のファイルに独立して持つ。オーバーレイの追加種別 (BottomSheet / Popover) は未承認の拡張候補として §6 に分離する。

### Options

- 用途: チャイルドシート・ETC カード・乗り捨て・免責補償などの付帯選択
- 構成: チェックボックス (18px) + アイコン (20px) + 名称 (14px・700) + 注記 (12px・`text.mutedStrong`) + 価格 (右寄せ・tabular-nums)
- Do: 現地払いと事前決済の区別を注記スロットに明記する
- 意匠: 行はカード。hover で境界を主色へ

### Header / Breadcrumb / Footer

- Header: `surface.default` 面 + `border.subtle` の下罫。ロゴ + 横並びナビ + ログイン。SP はロゴ + ハンバーガー (44px) で、ナビは右からの drawer
- Breadcrumb: 区切りは `text.muted`、リンクは主色、末尾は現在地でリンクにしない
- Footer: `surface.subtle` 面 + 境界線。PC は auto-fit の 3〜4 列、SP は 1 列
- Don't: 紺 (#283593) のベタ塗りフッター・旧系フッターを新規に複製しない
- 未確定事項: ToCoo! ロゴ素材が未提供 `🚧`。ワードマーク (見出しフォント + 主色) で代用する

### Modal

- 形態: drawer (PC は右から 420px / SP は全幅・高さ 90vh まで)。backdrop は `color.overlay.backdrop` (`🚧` 暫定値 rgba(0,0,0,0.45))
- 状態: Esc・backdrop・閉じるボタンで閉じる。フォーカスは内部にトラップし、閉じたら起点に戻す
- z 軸: `elevation.overlay` (1200) / `elevation.modal` (1300)
- Don't: remodal / LightBox など別のモーダル基盤を新規に追加しない。ブラー・グラス表現を使わない
- 未確定事項: 3 DS 横断の Modal 実装基盤は未決 (`governance/owner-decisions.md` §1 Q9)。travel の drawer 統一は travel 限定の現在判断であり、rental-car への適用は本書の提案である `🚧`

## 6. 拡張候補 (未承認)

結論: 以下 2 種は国内レンタカー固有の拡張候補である。オーナー判断の取得までは既定仕様として扱わない。

### BottomSheet (候補)

- 用途: SP の並び替え・絞り込み・時刻や日付の選択など「選んで即閉じる」操作
- 意匠: 全幅・上端 2 隅は `radius.overlay` (16px `🚧`)・ハンドル (40x4px)・行 48px・高さは内容なり (最大 90vh)
- 閉じ方: backdrop タップ・下スワイプ・選択で自動クローズ
- Don't: PC で使わない

### Popover (候補)

- 用途: PC の時刻選択・補足説明・小さな選択肢
- 意匠: アンカー直下 8px・幅 240〜320px・影は `🚧` 未定義 ([design.md](design.md) §5)・backdrop なし
- 閉じ方: 外側クリック・Esc・選択で自動クローズ
- Don't: backdrop を敷かない。SP では同じ内容を BottomSheet で開く

同時に開くオーバーレイは 1 つに限る (drawer・BottomSheet・Popover 共通)。

## 7. レスポンシブ

結論: ブレークポイントは 640 / 768 / 1024 / 1280。実装は 2 段 (959 / 960) しか持たないため、置換時は下表の振る舞いに寄せる。

| Component | 768px 未満 (モバイル) | 1024px 以上 (デスクトップ) |
| --- | --- | --- |
| SearchForm | フィールドを 1 列に縦積み。タブは 3 分割の等幅 pill。CTA は幅 100% / 高さ 48px | 2〜4 列グリッド (minmax 200px)。CTA は右下 |
| ResultCard | 画像 120px + 情報の 2 列。料金は 2x2 グリッド。価格と CTA を最下段に固定 | 画像 / スペック / 補足の 3 列 + 料金 6 列行 |
| Filter | 固定バーの「絞り込み」から drawer で全画面。適用中チップは結果上部に横スクロール | 結果左の 280px サイドバーに常時表示 |
| Sort / Pagination | 追従バーに絞り込み (件数バッジ) と並び替え (現在値を省略表示) を並置。押すと下からの全幅 drawer (BottomSheet 候補は §6 = 未承認) | 結果ヘッダー右にトリガー (pill 44px)。押すとアンカー直下にパネル。ページ送りは結果下部 |
| Header | ロゴ + ハンバーガー (44px)。ナビは右からの drawer | ロゴ + 横並びナビ + ログイン |
| Footer | リンク列を 1 列に縦積み | auto-fit の 3〜4 列 |
| StepIndicator | 現在ステップのみラベル表示、他は番号のみ (折返し可) | 全ステップをラベル付きで横並び |
| Modal | 全幅 drawer (下または右から)。高さは 90vh まで | 右から 420px の drawer |
| Options / StorePicker | 行を縦積み。チェックとラジオは 18px、行全体を 44px 以上のタップ領域に | 同一構造 (アイコン列あり) |

表示確認の代表 viewport は 390 / 768 / 1280 / 1440px であり、ブレークポイントとは別概念である。

## 8. 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Button / Input / SearchForm / Card / PriceTag / Header / Footer / Breadcrumb / Modal) | Claude Design (Builder) |
| 2026-07-02 | 是正 R-1: Modal の `elevation.z.*` を `{elevation.*}` へ、Button Do 項を `{radius.action}` へ統一。S-5: PriceTag 数字書体の実査に検討トリガー付与 | Claude Design (Builder) |
| 2026-08-19 | 0.3.0-draft: オーナー判断 2026-08-18 により Foundation の定義体系を更新 (pill ボタン・主色・2 書体・4px 系)。Select / FormLabel / Label・Tag / SecretPrice / Options / StorePicker / StepIndicator / Filter / Sort・Pagination を追加。ラベル・タグ定義を別ファイル化。BottomSheet / Popover を未承認の拡張候補として分離。レスポンシブ表を追加 | Claude Design |
| 2026-08-20 | 本 Repository へ反映 (0.3.0-draft)。ハンドオフバンドル `design_handoff_rental-car-ds/02_specs/components.rental-car.md` を `components.md` へ全置換。根拠はオーナー判断 2026-08-18 (記録 = [governance/owner-decisions.md](../../../governance/owner-decisions.md) §25) | Claude Code |
| 2026-08-20 | Task 009-57R の記述是正: PR [#156](https://github.com/tocoo/coocom-design-system/pull/156) コードレビュー ([issuecomment-5353729542](https://github.com/tocoo/coocom-design-system/pull/156#issuecomment-5353729542)) の指摘に対応。①共通事項と Button Do から「1 画面の主 CTA は primary 1 つ」を除去し、個数制約を未取得事項として Button の未確定事項へ移した (travel は §16 で撤回済みだが適用範囲は travel 限定)。②`ghost` / `text` の意匠を既存トークンの範囲で定義した (4 語の宣言に対し `primary` しか束縛がなかった)。③判読性を要する 8 箇所の文字色を `text.muted` (2.68:1) から `text.mutedStrong` (6.19:1) へ変更した。④車種クラス名の書体を `font.display.mdSize` に固定した (ゴシック `h3Size` との二重割当を解消)。⑤SecretPrice のマスク面を B-2 の `scheme.main.tint` に揃えた。⑥`shadow.md` の primitive 直接参照を「未定義 `🚧`」へ改めた。⑦Modal の backdrop を `color.overlay.backdrop`、BottomSheet の上端角丸を `radius.overlay` へ置換した (生値の解消)。⑧Sort / Pagination の SP 仕様とレスポンシブ表から未承認候補 BottomSheet への依存を外した。⑨「travel の実体をそのまま使う」を「travel と同型・意匠と値は本 DS で定義」へ改め、内訳を 7 / 3 / 8 件に統一した。**不変**: Component の構造・スロット責務名・状態の固定リスト・レスポンシブのブレークポイント | Claude Code |
