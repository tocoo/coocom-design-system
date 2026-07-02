# Component 仕様 — 国内宿泊予約 (travel)

- 種別: DS 成果物 (Ph-D Component 仕様)
- 状態: Draft
- 作成日: 2026-07-02
- 参照トークン: `semantic.travel.json` のみ (primitive 直接参照は禁止 = 命名規則§1)
- 根拠: 56-IDマトリクス (宿泊列)・layerB-observations §1/§2・実装着手ガイド §3/§4・固有制約サマリ TR-i1〜i3

---

## 共通事項

- [事実] 状態の固定リスト: `hover / active / focus / disabled / loading / error / success` (命名規則§2)。追加は ADR 必須
- [事実] ボタン状態 (hover/active/disabled/focus) は宿泊で未取得 (BT-03 / follow-up #4)。全 Component の hover は「opacity 変化」を暫定参照とし `🚧 暫定` を付す
- [事実] フォーカスは `outline` ベースで `{color.focus.ring}` を使用 (命名規則§8)。コントラストは A-02 未監査 (AA 目標)
- [推奨] Variant 暫定名のうち `secondary` (白CTA)・`ghost` 系は命名規則§10 の確定待ち。`要 ADR` を明記した
- [事実] 未着手 Component: Select / Tabs / Toast / Table / Accordion — 実体データ皆無 (follow-up #1)。分類保留・本仕様に含めない

---

## Button

- ステータス: Draft
- 用途: 画面内の操作起点。予約導線の主 CTA・補助操作
- バリアント:
  - `Button.primary` — bg `{color.action.primary.bg}` (紺) / 文字 `{color.action.primary.text}` / 角丸 `{radius.action}` (pill)
  - `Button.secondary` 🚧 暫定名 (要 ADR: tertiary/text/ghost の採否 = 命名規則§10) — 白CTA。bg `{color.action.secondary.bg}` / 文字 `{color.action.secondary.text}` / pill。layerB §1 実測 (bg白・#212121・999px)
  - `Button.campaign` ❓ 要議論 — 特集用 `{color.accent.campaign}`。採否は Phase 5 相当のブランドルール整理で判断
- 状態:
  - hover: `{color.action.primary.hoverBg}` 🚧 暫定 (navy 暗色未抽出 → opacity 変化を暫定参照 = follow-up #4)
  - active / disabled / focus / loading: 🚧 未取得 (BT-03)。focus は `{color.focus.ring}` outline を暫定適用
- Do / Don't:
  - Do: 1画面の主 CTA は `primary` 1つに絞る
  - Do: 実装は Semantic のみ参照する
  - Don't: 特集色 `{color.accent.campaign}` を通常導線の CTA に使わない (主色と分離 = 付随論点)
  - Don't: `--primary:#007bff` (Bootstrap 残骸 D-5) を参照しない
- 関連トークン: `color.action.*` / `radius.action` / `color.focus.ring` / `motion.transition.*`
- 現状差分メモ: `.c-btn` + 修飾子体系あり (BT-01/02 構造🟢)。形状は pill (R-01 🟡)
- 未確定事項: 状態一式 (follow-up #4)・サイズ段階 sm/md/lg の実測なし (暫定 md のみ定義)・secondary 命名 (要 ADR)

## Input

- ステータス: Draft 🚧
- 用途: フォームの単一入力 (テキスト/日付/数値)
- バリアント: `Input.default` のみ (実体不足のため最小定義 = 原則6)
- 状態:
  - error: 文字/枠 `{color.state.error}` 🚧 暫定 (宿泊のエラー表現実体は未取得 = F-02 / follow-up #2)
  - focus: `{color.focus.ring}` outline 🚧 暫定
  - disabled / success: 🚧 未取得
- Do / Don't:
  - Do: エラーはテキストメッセージ併記 (色のみで伝えない = A-02 AA 目標)
  - Don't: 未取得の必須表現 (アスタリスク等) を推測で固定しない (F-03)
- 関連トークン: `color.border.*` / `color.state.error` / `color.text.*` / `color.focus.ring`
- 現状差分メモ: 宿泊は Foundation 系のフォーム基盤 (F-02)
- 未確定事項: 入力/エラー/必須・検証の実体一式 (follow-up #2。追加観察には検索実行・送信操作が必要)

## SearchForm

- ステータス: Draft
- 用途: 宿泊検索の起点フォーム (`_search_form.ejs` 11KB = F-01 構造🟢)
- バリアント: `SearchForm.default` (TOP/一覧共用)
- 構成: Input 群 + 主 CTA (`Button.primary`)。フィールド構成の確定は実装実査が必要 🚧
- 状態: バリデーションは Input の error 状態に委譲 (F-02/F-03 未取得)
- Do / Don't:
  - Do: 検索実行 CTA は `Button.primary` を使用
  - Don't: フォーム構造を新規に再発明しない (既存 `_search_form.ejs` の構造を正とする = P4 段階導入)
- 関連トークン: Button / Input の参照に準ずる
- 現状差分メモ: 単一 ejs に集約済 (レンタカーの多経路 13KB+9KB と異なり構造は明快)
- 未確定事項: フィールド構成・レイアウト実測 (要実査)

## Card (ResultCard)

- ステータス: Draft
- 用途: 検索結果の宿泊施設カード (`.result-card` 8スロット = K-01 構造🟢)
- スロット (責務名 = 命名規則§2。8スロットへの対応付けは実査で確定 🚧):
  `Card.slot.media` / `Card.slot.title` / `Card.slot.meta` / `Card.slot.rating` / `Card.slot.price` / `Card.slot.badge` / `Card.slot.description` / `Card.slot.actions`
- バリアント: `Card.search` (検索結果) / `Card.plan` ❓ (プラン用の実体は要実査)
- 状態: hover 🚧 未取得
- Do / Don't:
  - Do: 評価は `Card.slot.rating` に ReviewStars を配置 (TR-i1。宿泊固有)
  - Do: 価格は `Card.slot.price` に PriceTag を配置 (TR-i2)
  - Do: バッジ (free-badge/プライム = K-04) は `Card.slot.badge` に集約
  - Don't: スロットを位置名 (top-left 等) で命名しない
- 関連トークン: `radius.card` 🚧 / `color.surface.default` / `color.border.subtle` / shadow (placeholder)
- 現状差分メモ: 見せ方はビジュアル重視 (K-02 🟡 DS内許容差)。画像なし表現は未定義 (D-1/D-6)
- 未確定事項: 実 px (角丸/影/余白) 未取得 (layerB §5)・8スロットと実装の対応付け・画像欠落時の fallback (D-6)

## PriceTag

- ステータス: Draft
- 用途: 価格表示 (TR-i2: 数字 900 ウェイト + 円 (Noto) + 補助テキスト)
- 構成:
  - 数字: `{font.price.family}` / `{font.price.weight}` (900) / `{font.price.numberSize}` (実測 20px) / `{color.text.strong}`
  - 「円」: `{font.body.family}` (Noto) / weight 600 相当 🚧 (実測: Noto Sans JP 600)
  - 補助価格: `{font.price.captionSize}` (実測 12px) / `{color.text.muted}` (実測 #616161)
- Do / Don't:
  - Do: 税・条件の補助テキストを必ず併記できる構造にする (価格表記フォーマットは DS 内で統一 = 判断基準§3 🟢)
  - Don't: 数字と単位を1つのテキストで固定しない (スロット分離)
- 関連トークン: `font.price.*` / `color.text.strong` / `color.text.muted`
- 現状差分メモ: layerB §2 実測パターンに一致 (K-03 構造🟢)
- 未確定事項: 「円」の weight 600 は primitive スケール外 (medium=500/bold=700)。正規化は Q4 と併せ要議論 ❓

## ReviewStars

- ステータス: Draft 🚧
- 用途: 星評価表示 (review-unit = K-05/TR-i1。宿泊固有・レンタカー2サービスには無い)
- 構成: 星アイコン×5 + 数値スコア (表示のみ。入力用途は実体なし)
- 状態: なし (静的表示)
- Do / Don't:
  - Do: 数値スコアを併記 (色・形のみで伝えない = A-02)
  - Don't: 他サービスへ流用しない (機能有無による差 = 🟡)
- 関連トークン: `{icon.reviewSize}`(星のサイズ・🚧 Q8 依存)/ `{color.icon.rating}`(星の色・🚧 未抽出・null placeholder)
- 現状差分メモ: 実装は review-unit (K-05)
- 未確定事項: 星の色・実寸は未抽出 ❓ (要実査。アイコン体系 Q8 に依存。検討トリガー: ReviewStars 実装着手時)

## Header

- ステータス: Draft
- 用途: 全ページ共通ヘッダー (`_header.ejs` = N-01 構造🟢)
- 構成: ロゴ / ナビゲーション / 会員導線。実測: bg 白・高さ約 41px (layerB §1)
- 状態: sticky 時は `{elevation.sticky}` を使用
- Do / Don't:
  - Do: bg は `{color.surface.default}`
  - Don't: 新規デザインでヘッダーを複数系統作らない (D-4 の再生産防止)
- 関連トークン: `color.surface.default` / `color.text.*` / `color.brand.primary`
- 現状差分メモ: 構造🟢 (N-01)。D-4 寄りの肥大あり
- 未確定事項: 内部ナビ構成の実査

## Footer

- ステータス: Draft
- 用途: 全ページ共通フッター
- Do / Don't:
  - Do: 新系 (`lp/_footer`) を正とし、新規制作はこれに揃える 🚧 暫定
  - Don't: 旧系フッターを新規ページへ複製しない (D-4)
- 関連トークン: `color.surface.*` / `color.text.*`
- 現状差分メモ: 新旧2系が並存 (N-02 🟢/D-4)
- 未確定事項: 旧系の廃止時期 (段階導入 P4 に従う)

## Breadcrumb

- ステータス: Draft
- 用途: 階層ナビゲーション (pankuzu = N-04 🟢)
- 構成: リンク (`{color.text.link}`) + 区切り + 現在地 (`{color.text.muted}`)
- Do / Don't:
  - Do: 現在地はリンク化しない
- 関連トークン: `color.text.link` / `color.text.muted`
- 未確定事項: なし (構造は既存実装を正とする)

## Modal / Overlay

- ステータス: Draft 🚧
- 用途: 重ね合わせ UI (drawer + `_modal_prime` = M-02)
- 実装基盤: ❓ 要議論 (Q9)。暫定運用 =「新規は drawer 方向・既存併存」。検討トリガー: Overlay/Modal 系 Component 着手時
- 状態: open/close 遷移は `{motion.transition.*}` 🚧 (follow-up #3)
- Do / Don't:
  - Do: z 軸は `{elevation.overlay}` / `{elevation.modal}` を使用
  - Don't: 新規に第3のモーダル基盤を導入しない (Q9 決着まで)
- 関連トークン: `elevation.*` / `color.surface.default` / `motion.transition.*`
- 未確定事項: 実装基盤の統一 (Q9・オーナー判断)

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Button/Input/SearchForm/Card/PriceTag/ReviewStars/Header/Footer/Breadcrumb/Modal。未取得は placeholder 明示) | Claude Design (Builder) |
| 2026-07-02 | 是正 R-1: primitive 直接参照を Semantic へ書換え (Modal/Header の `elevation.z.*`→`{elevation.*}`、ReviewStars の `iconSize.sm`→`{icon.reviewSize}` + 星色 `{color.icon.rating}`)。S-5: ReviewStars 星色を null placeholder で構造化・検討トリガー付与 | Claude Design (Builder) |
