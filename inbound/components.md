# Component 仕様 — インバウンドレンタカー (inbound)

- 種別: DS 成果物 (Ph-D Component 仕様)
- 状態: Draft
- 作成日: 2026-07-02
- 参照トークン: `semantic.inbound.json` のみ (primitive 直接参照は禁止 = 命名規則§1)
- 根拠: 56-IDマトリクス (インバウンド列)・layerB-observations §3/§4・inventory-inbound.md・固有制約サマリ IB-i1〜i5・実装着手ガイド §2/§3

---

## 共通事項 (i18n 構造制約 = 本 DS の中核)

- [事実] IB-i1: 4言語 (en/cn/kr/th)。全 Component は言語切替後も成立すること
- [事実] IB-i4: 文言長は言語で大きく変動する。**固定幅のテキストボックス・固定行数の切り詰めを前提にしない** (折返し・可変高を既定とする)
- [事実] IB-i5: コンテンツは locale 単位で格納。Component はテキストを直接持たず locale 供給を受ける
- [事実] フォントは `font.locale.*` の fallback 体系で解決 (IB-i2/D-10)。ページ・言語ごとのフォント継ぎ足しを再生産しない。許可リスト外 (Quicksand/Salesforce Sans 等) は新規採用しない
- [事実] 状態の固定リスト: `hover / active / focus / disabled / loading / error / success` (命名規則§2)
- [事実] hover は opacity 変化のみ確認 (BT-03)。hover 以外の状態は 🚧 未取得 (follow-up #4)
- [事実] 未着手 Component: Select / Tabs / Toast / Table / Accordion (follow-up #1)

---

## Button

- ステータス: Draft
- 用途: 操作起点。予約導線 CTA
- バリアント:
  - `Button.primary` — bg `{color.action.primary.bg}` (赤) / 文字 `{color.action.primary.text}` / 角丸 `{radius.actionCompact}` 🚧 (%btn-red 実装 3px)
  - `Button.ghost` 🚧 暫定名 (要 ADR = 命名規則§10) — Book Now 型。透明 bg / 文字 `{color.action.ghost.text}` / pill `{radius.action}` / weight bold / padding 実測 8px 24px (layerB §3)
- 状態: hover = opacity 変化 🚧 暫定 (BT-03)。active/disabled/focus/loading 🚧 未取得 (follow-up #4)
- Do / Don't:
  - Do: CTA 文言は動詞先頭・英語短文 ("Book Now" / "View details" = 🟢 候補)
  - Do: 文言長可変 (IB-i4) — 幅固定にせず min-width + padding で組む
  - Don't: pill と 3px 角丸を同一階層で混用しない (使い分け基準の明文化まで ❓。検討トリガー: Button 実装着手時)
- 関連トークン: `color.action.*` / `radius.action` / `radius.actionCompact` / `color.focus.ring` / `motion.transition.*`
- 現状差分メモ: 階層体系なし (BT-02: @extend のみ)。構造🟢/色🔵/形🟡
- 未確定事項: 状態一式 (follow-up #4)・pill/3px の使い分け (検討トリガー: Button 実装着手時)・ghost 命名 (要 ADR)

## Input

- ステータス: Draft 🚧
- 用途: フォームの単一入力
- バリアント: `Input.default`
- 状態:
  - error: 背景 `{color.form.errorBg}` (#ffd6de) + テキスト `{color.state.error}` 🚧 (#f00 は要精査)
  - focus: 背景 `{color.form.focusBg}` (#f3c8d0。実装名 `forcus` 誤記を正規化 = D-3) + `{color.focus.ring}` outline 🚧
  - disabled / success: success は `{color.state.success}` (実装 confirm #f6f6f6 は要精査 ❓)
- Do / Don't:
  - Do: エラーはテキスト併記 (A-02)。4言語分の文言長を想定した可変レイアウト (IB-i4)
  - Don't: `forcus` 等の誤記命名を新規コードへ持ち込まない
- 関連トークン: `color.form.*` / `color.state.*` / `color.border.*` / `color.focus.ring`
- 現状差分メモ: 状態色の実装値あり (F-02) だが必須/検証は未取得 (F-03)
- 未確定事項: 必須表現・検証仕様 (follow-up #2)

## SearchForm

- ステータス: Draft
- 用途: レンタカー検索 (search_module = F-01 構造🟢)
- 構成: pickup 地点・日時の条件入力群 + CTA。クエリ未指定では結果非表示 (layerB §4)
- Do / Don't:
  - Do: 4言語のラベル長差を吸収するレイアウト (IB-i4)
  - Don't: 言語別にフォーム構造を分岐しない (locale はコンテンツ層で解決 = IB-i5)
- 関連トークン: Button / Input の参照に準ずる
- 現状差分メモ: bookingform.scss 9KB + search_module.scss 13KB
- 未確定事項: フィールド構成の実査・検索結果カードの実測 (検索実行が必要 = layerB §5)

## Card (ResultCard / PlanCard)

- ステータス: Draft
- 用途: 検索結果カード (rental_box = K-01) / プランカード (地域×6 = inventory §5)
- スロット (責務名。実装との対応付けは実査で確定 🚧):
  `Card.slot.media` / `Card.slot.title` / `Card.slot.meta` / `Card.slot.price` / `Card.slot.badge` / `Card.slot.description` / `Card.slot.actions`
- バリアント: `Card.search` (高密度テキスト = K-02 🟡) / `Card.plan` (ヒーロー画像+地域名+キャッチ+説明+CTA+最低価格)
- Do / Don't:
  - Do: 価格は `Card.slot.price` に PriceTag (JPY~ 形式) を配置
  - Do: 在庫バッジ ("X cars left" = K-04) は `Card.slot.badge` に集約
  - Do: 画像欠落 (noimage 多発 = D-1) を前提に media スロットの fallback を設計 ❓ (D-6。検討トリガー: Card 実装着手時)
  - Don't: 多言語で改行崩れする固定高レイアウトにしない (IB-i4)
- 関連トークン: `radius.card` 🚧 / `color.surface.default` / `color.border.subtle`
- 現状差分メモ: noimage.jpg 多発 (D-1/D-6 重大負債)。実 px 未取得 (検索実行が必要)
- 未確定事項: 実 px・noimage 実挙動 (layerB §4/§5)・スロット対応付け

## PriceTag (通貨/法表記スロット = IB-i3)

- ステータス: Draft
- 用途: 価格表示。`{金額} JPY~ (tax included)` で統一 (CP-03 表記揺れなし = 🟢)
- 構成 (スロット分離。固定文字列にしない = 構造化インプット仕様§6):
  - `PriceTag.slot.amount` — 数字。`{font.price.family}` / `{font.price.weight}` (Roboto 700・実測 14px)
  - `PriceTag.slot.currency` — 通貨表記 ("JPY~")。将来の通貨追加に備えスロット化
  - `PriceTag.slot.legal` — 法表記 ("tax included")。locale 別文言を供給 (IB-i5)
- Do / Don't:
  - Do: 法表記スロットを省略可能にしない (法令要件 = 判断基準§3 価格表記🟢)
  - Don't: "JPY~ (tax included)" を1つの固定文字列で実装しない
- 関連トークン: `font.price.*` / `color.text.strong` / `color.text.muted`
- 現状差分メモ: layerB §3 実測と表記統一を確認済
- 未確定事項: 金額フォントサイズの段階 (カード内/詳細頁の実測不足 🚧)

## LanguageSwitcher

- ステータス: Draft (inbound 固有 = N-03)
- 用途: en/cn/kr/th の言語切替 (IB-i1。国内・宿泊には無い)
- 構成: 現在言語表示 + 4言語の選択リスト。選択肢は各言語の自称表記 (English/中文/한국어/ไทย) 🚧 表記実査
- 状態: 現在言語は選択不可表示。focus `{color.focus.ring}`
- Do / Don't:
  - Do: 切替先 locale のフォント fallback (`font.locale.*`) を適用
  - Do: `aria-label="{動詞}{対象}"` 形式 (命名規則§8。例 "Switch language")
  - Don't: 国旗アイコンのみで言語を表現しない (言語≠国。テキスト併記)
- 関連トークン: `font.locale.*` / `color.text.link` / `color.border.default`
- 現状差分メモ: 実装あり (N-03)。UI 実測は未取得 🚧
- 未確定事項: 配置 (Header 内想定)・表記・多言語 URL 規約 (`/{lang}/...` = 命名規則§5) との連動

## Header

- ステータス: Draft
- 用途: 全ページ共通ヘッダー (layouts = N-01 構造🟢)
- 構成: ロゴ / ナビ / LanguageSwitcher (inbound 固有)
- Do / Don't:
  - Do: LanguageSwitcher を Header に常設 (4言語導線 = IB-i1)
  - Don't: header.scss 22KB 級の肥大を新規で再生産しない (D-4)
- 関連トークン: `color.surface.default` / `color.brand.primary` / `color.text.*`
- 未確定事項: 内部構成の実査

## Footer

- ステータス: Draft
- 用途: 全ページ共通フッター (lp/_footer = N-02 🟢)
- Do / Don't:
  - Do: locale 別の法的表記・リンク群を供給できる構造 (IB-i5)
- 関連トークン: `color.surface.*` / `color.text.*`
- 未確定事項: 構成実査

## Breadcrumb

- ステータス: Draft
- 用途: 階層ナビゲーション (N-04: IB はあり = 🟢)
- 構成: リンク (`{color.text.link}`) + 区切り + 現在地 (`{color.text.muted}`)
- Do / Don't:
  - Do: locale 別ラベル供給 (IB-i5)。現在地はリンク化しない
- 関連トークン: `color.text.link` / `color.text.muted`
- 未確定事項: なし (構造は既存実装を正とする)

## Modal / Overlay

- ステータス: Draft 🚧
- 用途: 重ね合わせ UI (M-02: 現行は remodal)
- 実装基盤: ❓ Q9。暫定運用 =「新規は drawer 方向・既存併存」
- Do / Don't:
  - Do: z 軸は `{elevation.overlay}` / `{elevation.modal}`。遷移は `{motion.transition.*}` (300ms/ease = 実測)
  - Don't: 新規に別基盤を追加しない (Q9 決着まで)
- 関連トークン: `elevation.*` / `motion.transition.*`
- 未確定事項: 実装基盤の統一 (Q9)

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Button/Input/SearchForm/Card/PriceTag/LanguageSwitcher/Header/Footer/Breadcrumb/Modal。i18n 構造制約を共通事項に明記) | Claude Design (Builder) |
| 2026-07-02 | 是正 R-1: Modal の `elevation.z.*`→`{elevation.*}` (Semantic 参照へ)。S-5: Button の pill/3px 使い分けに検討トリガー付与 | Claude Design (Builder) |
