# Component 仕様 — 国内レンタカー (rental-car)

- 種別: DS 成果物 (Ph-D Component 仕様)
- 状態: Draft
- 作成日: 2026-07-02
- 参照トークン: `semantic.rental-car.json` のみ (primitive 直接参照は禁止 = 命名規則§1)
- 根拠: 56-IDマトリクス (国内レンタカー列)・layerB-observations §3-2・inventory-rental-car.md・実装着手ガイド §3/§4

---

## 共通事項

- [事実] 状態の固定リスト: `hover / active / focus / disabled / loading / error / success` (命名規則§2)。追加は ADR 必須
- [事実] ボタン状態は未取得 (BT-03 / follow-up #4)。hover は「opacity 変化」(IB 実装) を暫定参照 🚧
- [事実] フォーム入力/エラー/必須・検証は未取得 (F-02/F-03 / follow-up #2)
- [事実] フォーカスは `outline` + `{color.focus.ring}` (命名規則§8)。ただし ring 色は Q1 連動 🚧
- [事実] 未着手 Component: Select / Tabs / Toast / Table / Accordion (follow-up #1・実体皆無)

---

## Button

- ステータス: Draft
- 用途: 操作起点。検索・予約導線の主 CTA
- バリアント:
  - `Button.primary` — bg `{color.action.primary.bg}` (赤 🚧 Q1) / 文字 `{color.action.primary.text}` (白) / 角丸 `{radius.action}` (4px) / weight bold。実測: 検索ボタン bg #9B2030・18px・700 (layerB §3-2)
  - `Button.secondary` ❓ — 実体なし。階層体系そのものが国内に無い (BT-02: なし)。第一版では定義せず、必要時に ADR (命名規則§10)
  - `Button.campaign` ❓ 要議論 — `{color.accent.campaign}`。採否はブランドルール整理で判断
- 状態: hover/active/disabled/focus/loading すべて 🚧 未取得 (BT-03)。hover は opacity 暫定・focus は `{color.focus.ring}` outline 暫定
- Do / Don't:
  - Do: 国内の角丸は `{radius.action}` (4px)。pill (IB/宿泊の形状) を流用しない (R-01 🟡 = ゾーンで異なる形状は許容差)
  - Do: 実装は Semantic のみ参照
  - Don't: Q1 未決のまま HEX 直書きしない (確定時に一括差し替え可能に保つ)
- 関連トークン: `color.action.primary.*` / `radius.action` / `color.focus.ring` / `motion.transition.*`
- 現状差分メモ: 階層体系なし (BT-02)。構造🟢/色🔵/形🟡 (BT-01)
- 未確定事項: Q1 (主色正値)・状態一式 (follow-up #4)・サイズ段階の実測なし

## Input

- ステータス: Draft 🚧
- 用途: フォームの単一入力
- バリアント: `Input.default` のみ (実体不足のため最小定義 = 原則6)
- 状態: error `{color.state.error}` 🚧 (follow-up #2 暫定) / focus `{color.focus.ring}` 🚧 / disabled・success 未取得
- Do / Don't:
  - Do: エラーはテキスト併記 (A-02 AA 目標)
  - Don't: 必須表現・検証仕様を推測で固定しない (F-03 未取得)
- 関連トークン: `color.border.*` / `color.state.error` / `color.text.*` / `color.focus.ring`
- 現状差分メモ: 入力/エラー/必須は未取得 (F-02/F-03)。IB 既知値 (error #ffd6de 等) を暫定参照可 (follow-up #2) — ただし値の流用でなく「暫定参照」であることを実装コメントに明示
- 未確定事項: 実体一式 (follow-up #2)

## SearchForm

- ステータス: Draft
- 用途: レンタカー検索の起点フォーム (F-01: 13KB+9KB の多経路 = D-4 寄)
- バリアント: `SearchForm.default`
- 構成: 出発/返却の条件入力群 + 主 CTA (`Button.primary`)。フィールド構成の確定は実装実査が必要 🚧
- Do / Don't:
  - Do: 新規制作では検索経路を単一構造へ集約する方向で設計 (D-4 の再生産防止。既存置換は段階導入 P4)
  - Don't: 多経路実装をそのまま新規ページへ複製しない
- 関連トークン: Button / Input の参照に準ずる
- 現状差分メモ: 構造🟢だが実装は多経路で肥大 (D-4 寄)
- 未確定事項: フィールド構成・レイアウト実測 (要実査)

## Card (ResultCard)

- ステータス: Draft
- 用途: 検索結果の車両/プランカード (K-01: dl/dt/dd 6カラム構造)
- スロット (責務名。現行 dl/dt/dd 6カラムとの対応付けは実査で確定 🚧):
  `Card.slot.media` / `Card.slot.title` / `Card.slot.spec` / `Card.slot.price` / `Card.slot.badge` / `Card.slot.actions`
- バリアント: `Card.search` (検索結果)
- 状態: hover 🚧 未取得
- Do / Don't:
  - Do: スペック情報 (`Card.slot.spec`) を中心に置く (K-02: 国内はスペック寄りの情報密度 = 🟡 DS内許容差)
  - Don't: スロットを位置名で命名しない
- 関連トークン: `radius.card` 🚧 / `color.surface.default` / `color.border.subtle`
- 現状差分メモ: 画像なし表現 noimage (I-02 負債 D-1/D-6)
- 未確定事項: 実 px (角丸/影/余白) 未取得・画像欠落時 fallback (D-6)・画像比率 (follow-up #6)

## PriceTag

- ステータス: Draft 🚧
- 用途: 価格表示 (CP-03: 円+数字強調。構造🟢)
- 構成: 数字 (`{font.price.family}` 🚧 + weight bold 暫定) + 「円」 + 補助テキストのスロット構造 (3サービス共通の構造原則・値は本DS独自)
- Do / Don't:
  - Do: 税・条件の補助テキストを併記できる構造にする (価格表記は DS 内で統一 = 判断基準§3 🟢)
- 関連トークン: `font.price.family` / `color.text.strong` / `color.text.muted`
- 現状差分メモ: 国内の価格タイポ実測は未取得 (K-03 国内=—)
- 未確定事項: 数字書体・サイズ・weight の実測 (要実査 ❓。検討トリガー: PriceTag 実装着手時)

## Header

- ステータス: Draft
- 用途: 全ページ共通ヘッダー (N-01: 22KB = 構造🟢/D-4 寄)
- Do / Don't:
  - Do: bg `{color.surface.default}`・ブランド表示に `{color.brand.primary}` 🚧 Q1
  - Don't: 22KB の既存実装構造をそのまま新規に持ち込まない (D-4)
- 関連トークン: `color.surface.default` / `color.brand.primary` / `color.text.*`
- 未確定事項: 内部ナビ構成の実査

## Footer

- ステータス: Draft
- 用途: 全ページ共通フッター (N-02: 新旧2系 = D-4)
- Do / Don't:
  - Do: 新系を正とし、新規制作はこれに揃える 🚧 暫定
  - Don't: 旧系を新規ページへ複製しない
- 関連トークン: `color.surface.*` / `color.text.*`
- 未確定事項: 旧系の廃止時期 (段階導入 P4)

## Breadcrumb

- ステータス: Draft ❓
- 用途: 階層ナビゲーション
- [事実] 国内RC のパンくず有無は未確認 (N-04 要確認 / follow-up #7)
- 暫定運用: 保留。有無の確認後に仕様化 (検討トリガー: Nav 系 Component 着手時)
- 関連トークン: `color.text.link` 🚧 (link 自体が placeholder) / `color.text.muted`
- 未確定事項: 存在の有無 (follow-up #7)・link 色 (分類C)

## Modal / Overlay

- ステータス: Draft 🚧
- 用途: 重ね合わせ UI (M-02: 現行は LightBox)
- 実装基盤: ❓ Q9。暫定運用 =「新規は drawer 方向・既存併存」。検討トリガー: Overlay/Modal 着手時
- Do / Don't:
  - Do: z 軸は `{elevation.overlay}` / `{elevation.modal}`
  - Don't: 新規に別のモーダル基盤を追加しない (Q9 決着まで)
- 関連トークン: `elevation.*` / `motion.transition.*` 🚧
- 未確定事項: 実装基盤の統一 (Q9)

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Button/Input/SearchForm/Card/PriceTag/Header/Footer/Breadcrumb/Modal。未取得は placeholder 明示) | Claude Design (Builder) |
| 2026-07-02 | 是正 R-1: Modal の `elevation.z.*`→`{elevation.*}`、Button Do 項の `{radius.sm}`→`{radius.action}` (同仕様内既存の Semantic へ統一)。S-5: PriceTag 数字書体実査に検討トリガー付与 | Claude Design (Builder) |
