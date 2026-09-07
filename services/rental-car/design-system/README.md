# Rental-car Design System

- Status: Draft (0.3.0-draft)
- 作成日: 2026-09-07
- Scope: 国内レンタカーサービス (`rental-car`・暫定識別子) の Design System レイヤーの入口。本レイヤーが持つ成果物の一覧・読み順・責務の境界・Open Issue を管理する。
- Position in Repository: `services/rental-car/design-system/README.md` — Design System レイヤー (rental-car サービス配下)。サービス入口は [../README.md](../README.md)。横断の共通規約は [../../../governance/README.md](../../../governance/README.md)・判断の記録は [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md)。

本 README は入口文書であり、**個別のトークン・Component・ブランド値・判断そのものは定義・変更しない**。値と規則の正本は §2 の各成果物にある。

---

## 1. Purpose

- 本レイヤーが持つ成果物を実在ファイル名で一覧化し、読み順と各成果物の責務を示す。
- 「何がどこに書いてあるか」を一意にし、同じ事柄が複数の文書で別々に定義される状態を防ぐ。
- 本レイヤーが**決めないこと**の境界 (上流・下流・他 DS との関係) を明示する。
- 未確認・不足・矛盾・未検証の事項を Open Issue として保持する。

## 2. 成果物の一覧

| ファイル | 種別 | 責務 | Status |
| --- | --- | --- | --- |
| [design.md](design.md) | 正本 | Foundation の統合文書。カラー (面と文字色の組み合わせ規則・リンク・未入力状態の文字色を含む)・タイポグラフィ (文書レベルの見出しスケール)・スペーシング/BP・角丸/シャドウ/モーション・アイコン/画像/オーバーレイ・コアコンポーネントの概観と Modal の表示形態・ブランド/クリエイティブガイド (表記規則 3 節)・Agent Prompt Guide・未確定事項の一覧 | Draft (0.3.0-draft) |
| [semantic.rental-car.json](semantic.rental-car.json) | 正本 | 用途 (Semantic) トークン。実装が参照するのはこの層のみ | Draft (0.3.0-draft) |
| [primitive.rental-car.json](primitive.rental-car.json) | 正本 | 値 (Primitive) トークン。実装からの直接参照は禁止 | Draft (0.3.0-draft) |
| [components.md](components.md) | 正本 | Component 仕様 (共通事項・フォーム系・検索系・検索結果系・オーバーレイ・レスポンシブ) | Draft (0.3.0-draft) |
| [labels-tags.rental-car.md](labels-tags.rental-car.md) | 正本 | ラベル・タグ定義 (器の統一・カテゴリ A〜H・Do / Don't・追加したトークン) | Draft |
| [migration-map.md](migration-map.md) | 記録 | 実装 (japan ゾーン) の旧値と DS 正値の対照表 (12 項目)。**左列は実装の事実値であり DS の正値ではない** | 記録 |
| [preview.rental-car.html](preview.rental-car.html) | **非正本** | DS 見本ページ。正本のトークンを実際に描画したもの。**規則の文章を持たない** | 非正本 |

- **値が食い違った場合は JSON を正とする** ([design.md](design.md) §2 冒頭)。`design.md` の表は要約である。
- `preview.rental-car.html` の CSS 変数・色見本・スケールの 3 ブロックは `tools/gen-preview-tokens.py` が JSON から生成する。JSON を改訂したら `python3 tools/gen-preview-tokens.py --service rental-car` を実行する (一致確認は `--check`)。**見本ページへ値を手で書き写さない**。

## 3. 読み順

1. 本 README
2. [design.md](design.md) — Foundation の規則
3. [semantic.rental-car.json](semantic.rental-car.json) → [primitive.rental-car.json](primitive.rental-car.json) — 値
4. [components.md](components.md) — Component 仕様
5. [labels-tags.rental-car.md](labels-tags.rental-car.md) — ラベル・タグ (A〜H)
6. [migration-map.md](migration-map.md) — 実装の旧値との対応 (必要なときのみ)

見た目を確認するときは [preview.rental-car.html](preview.rental-car.html) を開く。AI に UI を生成させるときの読み順は [design.md](design.md) §9 Agent Prompt Guide が正。

## 4. どこに何が書いてあるか

| 探しているもの | 正本 |
| --- | --- |
| 色・書体・寸法の値と `$status` | `semantic.rental-car.json` → `primitive.rental-car.json` |
| スキーム (main / sub) と用途トークンの対応 / 品質下限 | `design.md` §2.1・§2.2 / §2.3 |
| 面と文字色の組み合わせ規則・白文字の例外・accent の帰属 | `design.md` §2.4 |
| リンクの装飾と状態 / 未入力状態の文字色 | `design.md` §2.5 / §2.6 |
| タイポグラフィ・文書レベルの見出しスケール (h1〜h6) | `design.md` §3・§3.1 |
| 余白・グリッド・ブレークポイント / 角丸・シャドウ・モーション / アイコン・画像・オーバーレイ | `design.md` §4 / §5 / §6 |
| Modal の表示形態 (form = drawer / sheet / popover) | `design.md` §7.1 |
| 割引率の表記 / 予約条件 / クリエイティブへの適用範囲 | `design.md` §8.1 / §8.2 / §8.3 |
| Component の構造・状態・スロット・Do / Don't | `components.md` |
| ラベル・タグ (A〜H) の器と用途色 | `labels-tags.rental-car.md` |
| 実装の旧値 (廃止値) との対応 | `migration-map.md` |
| 誰がいつ何を決めたか | `governance/owner-decisions.md` (Foundation 定義体系の採用 = §25 / travel 最新版の適用 = §29) |

**節番号の注意**: `design.md` の §2 は既存の §2.1 スキーム / §2.2 用途 / §2.3 品質下限を保持したまま、国内宿泊 (travel) `design.md` §2.1〜§2.3 に対応する 3 節を **§2.4〜§2.6** として新設している。travel と節番号が 1 対 1 に対応しないのは §2 のみで、§3.1・§7.1・§8.1〜§8.3 は同じ番号である。

## 5. 責務の境界

### 本レイヤーが管理する

- Foundation (色・書体・余白・角丸・影・モーション・アイコン・BP) の用途と値。
- Component の構造・状態・トークン参照・Do / Don't。
- ラベル・タグの器とカテゴリごとの用途色。
- 表記規則のうち **DS の表示規則にあたる部分** (割引率の表記形式・予約条件の色と並び・クリエイティブへの適用範囲)。
- 未確認・不足・矛盾・未検証の事項の保持 (`design.md` 未確定事項の一覧)。

### 本レイヤーが管理しない

- **ページの配置と余白**・画面構成・URL・route — Component が定義するのは自身の構造・状態・トークン参照だけである ([components.md](components.md) §1)。
- **画面別の見出し階層・semantic role の割当** (どの画面のどのコンテンツを `h1` / `h2` とするか) — Screen Requirements 側の課題。本レイヤーは `h1`〜`h6` の各要素に当てる**既定値**のみを定める ([design.md](design.md) §3.1)。
- **事業・価格仕様** — 割引率の算出方法・端数処理・上限値は定義しない ([design.md](design.md) §8.1)。
- **a11y の実装方式** — `role` / `aria-modal` / フォーカストラップ / 復帰先・背面スクロールロックは DS 層で決定しない ([design.md](design.md) §7.1)。
- **実装 Repository (`tocoo/tocoo_rental_car`) 側の適用作業**・反映の範囲・順序・期限。
- **恒久 Decision ID・ADR・正式 Status 体系・Phase・Gate の採番・新設** — Repository 内に正本体系が未整備であり、推測で採番しない。`TVL-NNNN` は ADR 正本が Repository 内に不在であるため、本レイヤーの文書で現在の仕様根拠として参照しない。
- **適用規格・達成レベルの正式確定・適合判定・適合宣言** — コントラスト比は本 Repository での実測値の記録であり、適合宣言ではない。

## 6. 3 独立 DS の原則

本 DS は国内宿泊 (travel)・インバウンドレンタカー (inbound) と Foundation / Semantic / Component / `design.md` の**ファイルと値を共有しない** (P1/ADR-0022)。

- 0.3.0-draft で採用しているのは travel の**定義体系** (スキーム二層・per-scheme の役割色・2 書体・4px 系・面と文字色の規則・見出しスケール・ラベルの用途色等) であり、**値は本 DS のファイルに独立して持つ**。
- travel のファイルを参照・共有しない。`preview.rental-car.html` が読むのも本ディレクトリの JSON だけである。
- travel 側の判断記録は**適用範囲を travel に限定**しているため、rental-car への適用は**別途取得した判断**として `governance/owner-decisions.md` に記録する (Foundation 定義体系の採用 = §25 / travel 最新版 (Task 009-58〜009-62) の適用 = §29)。
- レンタカー固有の要素 (`color.mask.secret`・`font.display.mdSize` = 車種クラス名・`icon.size`・No Image fallback・固有 Component 8 件・ラベル体系の割当差) は本 DS 独自に維持する。

## 7. Status / version の扱い

- `$status` は `bound` (確定扱い) と `placeholder` (未確定) の 2 値。`placeholder` のトークンは `$note` に理由と追跡先を持つ。
- **`$status = placeholder` のトークンを参照する生成物には `🚧 暫定` を伝播させる** ([design.md](design.md) §9 手順 3)。
- **仮色 (実色値未取得) は placeholder として bind し、実色を発明しない。** 確認方法と個別確認主体は [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §14 (依頼元提出値の受領・作業担当者照合 + Web部責任者確認)。
- `$meta.version` の付与規則そのものは Repository 内で未決である。本レイヤーは版を推測で上げない。

## 8. 上流・下流との関係

- **上流** — Service Design / Screen Requirements はいずれも `Not started` である ([../README.md](../README.md))。上流に無い業務仕様・画面仕様を Design System から逆算しない。不足は不足として保持する。
- **下流** — Assets は `Not started`。実装は `tocoo/tocoo_rental_car` の `japan` ゾーン。実装は **Semantic のみ参照**する (primitive の直接参照は禁止)。
- **横断** — 命名・運用規約は [../../../governance/](../../../governance/README.md) が管轄する。ただし `naming-rules.md` 等の正本は未整備であり、参照切れを解決済みとして扱わない。

## 9. Open Issues

本 README の時点で未解決の事項。**個別の技術的な未確定は [design.md](design.md) の「未確定事項の一覧」が正本**であり、ここではレイヤー運営上の Open Issue のみを挙げる。

- **サービス識別子 `rental-car` は暫定**である。正式識別子 (`drc` / `japan` 等) は未決 ([../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) 確認事項 `#8`)。ディレクトリ名を確定した識別子として扱わない。
- **スキームの正式採用 (main / sub) が未決**である。`color.state.success` / `color.text.link` / `linkHover` / `linkActive` / `color.state.error` / `color.accent.campaign` ほかは現在 `main` を参照して固定されており、スキームの切替に自動追随しない。
- **上流 (Service Design / Screen Requirements) が未着手**であるため、画面別の情報構造に依存する事項 (見出し階層の割当・画面ごとの Component 選択) は本レイヤーで確定できない。
- **`$meta.version` の付与規則**が Repository 内で未決である。
- **Governance 横断ルール §23** (非 UI クリエイティブへの適用範囲の例外) の「カラーもトークン指定外を許容」と、本レイヤー [design.md](design.md) §8.3 の「カラーは厳守」に**差分があり未調整**である。原則正本の置き場所を含め §23 の設計承認プロセスで扱う。
- **クリエイティブのグラデーション審査基準・審査主体**が未策定である ([design.md](design.md) §8.3)。

## 10. 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-09-07 | 初版。Design System レイヤーの入口文書として新設 (Task 009-63・[Issue #170](https://github.com/tocoo/coocom-design-system/issues/170)・記録 = [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) §29)。成果物の一覧・読み順・正本の所在・責務の境界・3 独立 DS の原則・Status / version の扱い・上流/下流との関係・Open Issue を定義した。**個別のトークン・Component・ブランド値・判断は定義・変更していない** | Claude Code |
| 2026-09-07 | Task 009-63R の記述是正: PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) コードレビュー ([issuecomment-5565532746](https://github.com/tocoo/coocom-design-system/pull/171#issuecomment-5565532746)) の指摘に対応。§2.6 の改題 (「プレースホルダの文字色」→「未入力状態の文字色」) に伴い、成果物の一覧と正本の所在表の該当記述を追随させた。**個別のトークン・Component・ブランド値・判断は定義・変更していない** | Claude Code |
