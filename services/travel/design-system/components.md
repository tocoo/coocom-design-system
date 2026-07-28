# Component 仕様 — 国内宿泊予約 (travel)

- 種別: DS 成果物 (Component 仕様。R3-4)
- 状態: Draft (0.3.0-draft)
- 作成日: 2026-07-09
- Source of Truth: https://github.com/tocoo/coocom-design-system/blob/main/services/travel/design-system/components.md
- 参照トークン: `semantic.travel.json` のみ (primitive 直接参照は禁止 = 命名規則§1)

---

## 共通事項

- [事実] 状態の固定リスト: `hover / active / focus / disabled / loading / error / success` (命名規則§2)。追加は ADR 必須
- [事実] ボタン状態 (hover/active/disabled/focus) は宿泊で未取得 (follow-up #4 / TVL-0008)。全 Component の hover は「opacity 変化 (≈0.85)」を暫定参照とし `🚧 暫定` を付す
- [事実] フォーカスは `outline` ベースで `{color.focus.ring}` を使用 (命名規則§8)
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
  - hover: 🚧 暫定 opacity 変化 (navy 暗色未抽出 = follow-up #4)
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
- 状態: error = 文字/枠 `{color.state.error}` 🚧 暫定 / focus = `{color.focus.ring}` outline 🚧 / disabled・success 🚧 未取得
- Do / Don't:
  - Do: エラーはテキストメッセージ併記 (色のみで伝えない = WCAG 2.2 AA / R9)
  - Don't: 未取得の必須表現 (アスタリスク等) を推測で固定しない
- 関連トークン: `color.border.*` / `color.state.error` / `color.text.*` / `color.focus.ring`
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
- 関連トークン: `radius.card` 🚧 / `color.surface.default` / `color.border.subtle` / shadow 🚧
- 未確定事項: 実px (角丸/影/余白)・8スロット対応付け・画像欠落時の fallback ❓ (Card 実装着手時)

## PriceTag

- ステータス: Draft
- 用途: 価格表示 (数字 Bold 700 + tabular-nums + 円 + 補助テキスト)
- 構成:
  - 数字: `{font.price.family}` / `{font.price.weight}` (700・tabular-nums) / `{font.price.numberSize}` (1.25rem) / `{color.text.strong}`
  - 「円」: `{font.body.family}` / weight 600 相当 🚧 (スケール外実測。正規化 ❓)
  - 補助価格: `{font.price.captionSize}` (0.75rem) / `{color.text.muted}`
- Do / Don't:
  - Do: 税・条件の補助テキストを必ず併記できる構造にする
  - Don't: 数字と単位を1つのテキストで固定しない (スロット分離)
- 未確定事項: 「円」weight 600 の正規化 ❓

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
