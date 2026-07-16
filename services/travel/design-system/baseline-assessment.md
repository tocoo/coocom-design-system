# Travel Design System Baseline Assessment

- Status: Draft
- Scope: 既存 Design System 4 資産 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) の内部整合性・provenance・placeholder / 実査待ち状況を read-only で評価した結果の記録。上流 Service Design / Screen Requirements との Alignment 評価、既存資産の修正、gap の解決は行わない。
- Position in Repository: `services/travel/design-system/baseline-assessment.md` — Design System レイヤー (travel サービス配下)。前提・評価方法は Governance の実在成果物 ([../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md))、Design System 入口 [README.md](README.md)、評価計画 [alignment-plan.md](alignment-plan.md)。同一 Design System レイヤーの評価対象は `design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md` (§5)。上流 (Service Design [../service-design/README.md](../service-design/README.md) / Screen Requirements [../screen-requirements/README.md](../screen-requirements/README.md)) は評価境界の確認のためにのみ参照し、本評価は上流 Alignment を対象としない。下流成果物 (Assets / Implementation) との関係は §15 を参照。

本文書は `alignment-plan.md` §10 Recommended Work Order の 1、および §11 First Assessment Recommendation の実行結果である。評価結果は記録するが、既存資産の修正・上流 Alignment 判定・gap 解決・Decision を行わない。観察区分は `alignment-plan.md` §8 のものだけを使用し、正式 Status・優先度・severity・Design Decision と混同しない。ファイル名 `baseline-assessment.md` は記述的な暫定名であり、正式な評価体系名・命名規則・Alignment ID を確定しない。

## 1. Purpose

- 既存 Design System 4 資産を read-only で機械的・記述的に検証し、内部整合性・token 参照解決・placeholder / 実査待ち・provenance / 参照切れの状況を実測値で記録する。
- 後続の Alignment Assessment (Work Order 2 以降) が、未検証・placeholder・provenance 未確認の DS 記述を「正しい実現手段」として扱う危険を避けるための土台情報を提供する。
- 「Baseline を確認・記録する」ことと「既存資産を修正する / 上流適合を判定する / gap を解決する」ことを区別する。後者は本文書では行わない (§16)。

## 2. Assessment Snapshot

- 対象 Repository: `tocoo/coocom-design-system`
- 対象 branch: `main`
- 評価対象 commit SHA: `0d446152ef6226cef67aec4edad486e0a2812cde` (PR #45 merge。レビュー対応 `017a102a29a9c91510bf4a356a794b47181d098d` を含む)
- 評価日: 2026-07-16
- 評価対象 4 ファイルと blob SHA (評価 commit 上):

| ファイル | blob SHA | 自己申告 Status | 自己申告 version |
| --- | --- | --- | --- |
| [design.md](design.md) | `cb9edc16ec1329e33ea0b64fb9789f060ba8bfe9` | Draft | 0.3.0-draft |
| [semantic.travel.json](semantic.travel.json) | `812c9741343d5f642c9e369fb8d11a398389f474` | Draft (`$meta.status`) | 0.3.0-draft (`$meta.version`) |
| [primitive.travel.json](primitive.travel.json) | `7dc8f7889a33627370d5b280d486c37b8403ba8b` | Draft (`$meta.status`) | 0.3.0-draft (`$meta.version`) |
| [components.md](components.md) | `8fa20b88b773c8f302c22728cf46a95549ab458d` | Draft | 0.3.0-draft |

- 評価中の main 更新有無: 評価開始時の最新 commit (`0d446152`) で実施し、評価中に main の更新はなかった。異なる commit の内容は混在させていない。

## 3. Scope

### Assessed

- 上記 4 ファイルの実在・Markdown / JSON 構造・自己申告 Status / version・ファイル間の Status / version 整合。
- `design.md` の要約と JSON / `components.md` の記述の一致 (Repository 内部整合性)。
- Semantic token の Primitive / Semantic への `$value` 参照の全数解決。
- `design.md` / `components.md` が参照する Semantic token path の実在。
- placeholder・実査待ち・follow-up 番号・参照切れ・provenance 未確認・ファイル間矛盾の全数抽出。
- 上流に根拠がないことが確認できる既存 DS 側の主張の「過剰または provenance 未確認の可能性」としての記録。

### Not Assessed / Not Decided

- 上流 Service Design / 個別 Screen Requirement との Alignment 評価。
- token 値の良否・Component の必要性・採用/廃止・placeholder の解決値・follow-up の解決内容・Decision ID の有効性・ADR / 命名規則 / `brand-content.md` の内容・gap の解決策・修正優先度・version bump・実装方法・UI / 画面 / URL / route・SCR-006〜SCR-012 の DS 要件。
- 外部 Repository / 実装コード / Assets の調査。

## 4. Method and Evidence

- 評価は `alignment-plan.md` §6 Evidence Rules に従い、評価対象 4 ファイルと Governance / DS README / Alignment Plan の実在記述のみを証拠とする。
- JSON 2 ファイルは Python (`json.loads`) で実際に parse し、重複キー検出には `object_pairs_hook` を用いた。token tree を走査して leaf token (`$value` を持つ node) を全数列挙し、`$value` の参照 (`{...}` 形式) を Semantic / Primitive の実在 path へ解決し、`$status` / `$note` を集計した。
- `design.md` / `components.md` の token 参照は、`{...}` 形式 (components.md) およびバッククォート内 path 表記 (design.md) を機械抽出し、Semantic token tree の実在 path へ照合した。
- Markdown マーカー (`🚧` / `❓` / 暫定 / 未取得 / 実査待ち / follow-up) と provenance 参照は正規表現で全数集計した。
- 検証スクリプトは Repository 外 (作業ディレクトリ) で実行し、Repository へ追加・commit していない。
- 集計値はすべて上記の機械集計による実測値である。JSON parser は重複キーを保持しないため `object_pairs_hook` で別途検出しており、この制約下で「重複キーなし」と記録する。検出手段のない事項を「問題なし」と断定していない。

## 5. Artifact Inventory

評価対象 4 ファイルはすべて評価 commit 上に実在する (§2 に blob SHA)。各ファイルの自己申告メタ情報:

- [design.md](design.md) — 種別: 統合文書。状態: Draft (0.3.0-draft)。作成日: 2026-07-09。
- [semantic.travel.json](semantic.travel.json) — `$meta.layer` = semantic / `$meta.service` = travel / `$meta.status` = Draft / `$meta.version` = 0.3.0-draft / `$meta.created` = 2026-07-09。leaf token 63 件。
- [primitive.travel.json](primitive.travel.json) — `$meta.layer` = primitive / `$meta.service` = travel / `$meta.status` = Draft / `$meta.version` = 0.3.0-draft / `$meta.created` = 2026-07-09。leaf token 97 件。
- [components.md](components.md) — 種別: Component 仕様。状態: Draft (0.3.0-draft)。作成日: 2026-07-09。定義済 Component 見出し 10 件。

いずれも自己申告であり、本評価は内容の正しさ・承認・上流整合を判定しない。

## 6. Metadata and Version Consistency

| 項目 | design.md | semantic.travel.json | primitive.travel.json | components.md | 観察 |
| --- | --- | --- | --- | --- | --- |
| Status | Draft | Draft (`$meta`) | Draft (`$meta`) | Draft | 一致 |
| version | 0.3.0-draft | 0.3.0-draft | 0.3.0-draft | 0.3.0-draft | 一致 |
| 作成日 | 2026-07-09 | 2026-07-09 | 2026-07-09 | 2026-07-09 | 一致 |
| 対象サービス | travel (tocoo/tocoo_travel) | travel | travel | travel (R3-4) | 一致 |
| 対象範囲 | 顧客向け UI のみ | — | — | — | design.md のみ明記 |
| Source of Truth | GitHub URL (.../design-system tree) | GitHub URL (.../semantic.travel.json blob) | GitHub URL (.../primitive.travel.json blob) | GitHub URL (.../components.md blob) | 4 ファイルとも当 Repository の自己参照 URL。接続先内容は本タスクで未検証 (§12) |

4 資産の Status・version・作成日・対象サービスは相互に一致する (対応を直接確認できる)。Source of Truth の GitHub URL は記載を確認できるが、接続先の内容検証は行っていない (provenance: 外部参照)。

## 7. JSON Structural Validation

Python (`json.loads`) による実測:

- **parse**: `semantic.travel.json`・`primitive.travel.json` ともに JSON として parse 可能。
- **`$meta`**: 両ファイルに存在。`status` (Draft) / `version` (0.3.0-draft) / `layer` / `service` / `created` を確認。
- **token node 構造**: leaf token は `$value` を持つ object。semantic 63 件・primitive 97 件。
- **`$value` 参照形式**: semantic の全 leaf token (63/63) が `{path}` 形式の参照。primitive の leaf token は参照を持たず (0 件)、すべてリテラル値。
- **`$status`**: semantic = bound 60 / placeholder 3。primitive = bound 90 / placeholder 7。
- **`$note`**: placeholder token にはすべて `$note` が付随 (follow-up 番号・TVL-0008 等)。
- **重複キー**: `object_pairs_hook` による検出で **0 件**。標準 parser は重複を保持しないため別手段で検出しており、この制約下で「重複なし」と記録する。
- **空値・不正な型・参照不能値**: 走査範囲で検出されず。
- **Primitive 内参照**: 0 件 (primitive はリテラルのみ)。
- **Semantic → Primitive / Semantic 参照**: §8 に記載 (全数解決)。
- **循環参照**: 検出されず (semantic → semantic の連鎖は最終的に primitive のリテラルへ終端し、primitive は参照を持たない)。
- **未解決参照**: 0 件 (§8)。

## 8. Token Reference Validation

### Semantic → (Primitive / Semantic)

- 検証対象総数 (semantic の参照 token): **63**
- 解決できた参照: **63** (Primitive へ 51 / Semantic 自身へ 12)
- 未解決: **0**
- 参照先が placeholder-status の参照: **2** — `motion.transition.duration` → `motion.duration.base`、`motion.transition.easing` → `motion.easing.standard`
- 集計方法: Python で semantic leaf token の `$value` を全数抽出し、`{path}` を semantic → primitive の順に実在照合。

### Design → Semantic

- `design.md` はバッククォート内で token path を表記する (`{...}` 構文は不使用。`{...}` 抽出結果は 0 件)。
- バッククォート内の Semantic token path 候補 21 件のうち、Semantic leaf へ解決 **19 件** (例: `color.brand.primary` / `color.text.strong` / `color.state.success` / `radius.action` 等)、Semantic group へ解決 `color.scheme.main` / `color.scheme.sub` (`color.scheme.main.*` / `color.scheme.sub.*` を含む)。
- 残りは `radius.sm 4 / md 8 / lg 16 / full 9999px`・`iconSize.sm〜xl` の散文的な値説明で、これらは Primitive の radius / iconSize token を値付きで記述したものであり、参照切れではない (Primitive に実在)。
- 未解決の Semantic token 参照: **0**。

### Components → Semantic

- `components.md` の `{...}` token 参照: 総数 **28** (unique 23)。
- Semantic leaf へ解決: **22**、Semantic group (wildcard) へ解決: **1** (`{motion.transition.*}`)、Primitive への直接参照: **0**、未解決: **0**。
- `components.md` は Semantic のみを参照し Primitive を直接参照していない (「primitive 直接参照禁止」の記述と内部整合)。ただし `{motion.transition.*}` が指す Semantic の `motion.transition.duration` / `easing` は placeholder であり、参照先の未確定が伝播する (実査待ち)。

## 9. Cross-Artifact Consistency

### Metadata

§6 のとおり Status / version / 作成日 / 対象サービスは一致 (対応を直接確認できる)。

### Foundation

- **color**: `design.md` §2 の表示値 (brand.primary #2C50C8 等) は semantic → primitive の解決値と一致 (例: `color.brand.primary` → `scheme.main.base` → `palette.royal.500` = #2c50c8)。
- **Typography**: `design.md` §3 (LINE Seed JP / Noto Serif JP / rem スケール / 価格 700) は semantic `font.*` / primitive `typography.*` と一致。
- **spacing**: `design.md` §4 (4px = 0.25rem 系) は primitive `spacing.*` と一致。
- **breakpoint**: `design.md` §4 (640/768/1024/1280, TVL-0004) は primitive `breakpoint.*` と一致。
- **radius**: `design.md` §5 (sm4/md8/lg16/full9999, action=full=pill) は primitive `radius.*`・semantic `radius.action` と一致。`radius.card` は placeholder (暫定 md) で一致。
- **shadow / elevation**: `design.md` §5「shadow 実値未抽出 🚧 (follow-up #13, TVL-0008)」は primitive `shadow.*` placeholder と一致。elevation は bound で一致。
- **motion**: `design.md`・JSON ともに motion を placeholder (follow-up #3) として扱い一致。
- **icon**: FA6 (TVL-0006)・`iconSize.*` bound で一致。
- **focus / state**: `color.focus.ring` = brand.primary、`state.success` = 主色 / `state.error` = per-scheme で design.md と semantic が一致。

### Component

- `design.md` §7 の定義済 Component 一覧 (Button / Input / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal = 10) は `components.md` の実在見出し 10 件と一致。
- 未着手 Component (Select / Tabs / Toast / Table / Accordion = 5) は両文書で一致して「未着手・実体皆無・仕様に含めない」と記述。
- Button variant: 両文書とも「GOV-0002 が 5 語 (primary/secondary/ghost/campaign/text) を定義するが travel 実装は 4 語 (campaign 廃止, TVL-0012)」と一致。
- Component state: 固定リスト (hover/active/focus/disabled/loading/error/success) を両文書で共有。ボタン状態は未取得 (follow-up #4) と一致。
- Modal / drawer: drawer 全面統一 (TVL-0007)・centered dialog deprecated で一致。
- Card / PriceTag / ReviewStars / Header / Footer / Breadcrumb: `design.md` の記述と `components.md` の定義が対応。

## 10. Component Reference Validation

`components.md` の定義済 10 Component (すべて Status: Draft)。参照 token はすべて Semantic に実在 (§8)。

| Component | 参照 token (Semantic, 実在) | 主な未確定事項 | 観察 |
| --- | --- | --- | --- |
| Button | `color.action.*` / `radius.action` / `color.focus.ring` / `motion.transition.*` | 状態一式 (follow-up #4)・サイズ段階の実測なし | 参照解決・状態は実査待ち |
| Input | `color.border.*` / `color.state.error` / `color.text.*` / `color.focus.ring` | 入力/エラー/必須・検証 (follow-up #2) | 🚧 実査待ち |
| SearchForm | (Button.primary 経由) | フィールド構成・レイアウト実測 | 実査待ち |
| Card (ResultCard) | `radius.card` (placeholder) / `color.surface.default` / `color.border.subtle` / shadow (placeholder) | 実 px・8 スロット対応付け・画像欠落 fallback | placeholder / ❓ 実査待ち |
| PriceTag | `font.price.*` / `color.text.strong` / `color.text.muted` | 「円」weight 600 の正規化 | ❓ |
| ReviewStars | `icon.reviewSize` / `color.icon.rating` | 星の実寸 | 実査待ち |
| Header | `color.surface.default` / `elevation.sticky` | 内部ナビ構成 | 実査待ち |
| Footer | — | 旧系の廃止時期 | 🚧 暫定 |
| Breadcrumb | `color.text.link` / `color.text.muted` | — | — |
| Modal / Overlay | `elevation.overlay` / `elevation.modal` / `motion.transition.*` (placeholder) | centered dialog の移行対象・順序 | motion placeholder 伝播 |

未着手 Component (Select / Tabs / Toast / Table / Accordion): 既存記述どおり「未着手・実体皆無・仕様に含めない」として記録する。必要性の断定・新規作成の提案・Screen Requirement からの必要性評価は行わない (後続タスクへ分離)。既存 Component の存在を利用要求・承認済み仕様として扱わない。

## 11. Placeholder and Inspection-Pending Inventory

### JSON `$status: placeholder` (計 10 件)

| ファイル | token path | 現在の値 | 関連 note / ID | 観察区分 |
| --- | --- | --- | --- | --- |
| semantic | `radius.card` | `{radius.md}` | カード実 px 未取得・暫定 md (TVL-0008) | placeholder |
| semantic | `motion.transition.duration` | `{motion.duration.base}` | follow-up #3 (TVL-0008) | placeholder / 実査待ち |
| semantic | `motion.transition.easing` | `{motion.easing.standard}` | follow-up #3 | placeholder / 実査待ち |
| primitive | `shadow.sm` / `shadow.md` / `shadow.lg` | 暫定 3 段 | follow-up #13 (TVL-0008) | placeholder / 実査待ち |
| primitive | `motion.duration.fast` / `base` / `slow` | 150/300/500ms (暫定) | follow-up #3 | placeholder / 実査待ち |
| primitive | `motion.easing.standard` | `ease` (暫定) | follow-up #3 | placeholder / 実査待ち |

### Markdown マーカー (実測件数)

| マーカー | design.md | components.md |
| --- | --- | --- |
| 🚧 | 9 | 15 |
| ❓ | 4 | 4 |
| 暫定 | 3 | 7 |
| 未取得 | 2 | 4 |
| 実査待ち | 6 | 0 |
| follow-up | 6 | 4 |

これらのマーカーは JSON の placeholder token・未着手 Component・実測未取得事項に対応しており、記述と意味は整合している (`🚧`・`❓` の存在のみを欠陥と断定しない)。`design.md` の「未確定事項の一覧」表は TVL-0005 / follow-up #5 を「✅ 解決」、follow-up #4 / #13 / #3 / #2 等を「🚧 実査待ち」と自己記録している。

### 未着手 Component

Select / Tabs / Toast / Table / Accordion (§10)。

## 12. Provenance and Broken Reference Inventory

| 参照 | 出現箇所 | Repository 内実在 | 扱い |
| --- | --- | --- | --- |
| `brand-content.md` | design.md §1・§8 (「正: brand-content.md」) | **不在** (MISSING) | 参照先が存在しない (参照切れ) |
| `governance/naming-rules.md` | design.md §9・components.md §1/§2/§7/§8 | **不在** (MISSING)。Governance README も「未作成」と明記 | 参照先が存在しない (参照切れ) |
| GOV-0002 | design.md §7・components.md 共通事項/Button | Governance に ADR 正本なし | provenance 未確認 (記述はあるが正本性を確認できない) |
| TVL-0001〜TVL-0012 | design.md・components.md・JSON 全体 (実際に参照されるのは 0001〜0008・0010〜0012。**TVL-0009 は 4 資産のどこにも出現しない**) | ADR 正本なし | provenance 未確認 |
| follow-up #2 / #4 / #5 / #13 | design.md・components.md・JSON | owner-decisions.md §3 に「未取得データ」として記載あり (解決値ではない) | Repository 内に追跡記述はあるが未取得・未解決 |
| follow-up #3 | design.md §未確定一覧・JSON motion note | owner-decisions.md §3 の follow-up 一覧に **記載なし** | provenance 未確認 (追跡先を Repository 内で確認できない) |
| Source of Truth GitHub URL | 4 資産の header | 当 Repository への自己参照 URL | 外部参照。接続先内容は本タスクで未検証 |
| 実装 Repository `tocoo/tocoo_travel` | design.md §実装の所在・primitive `$meta` | — | 外部参照。本タスクでは検証対象外 |
| Markdown 相対リンク `](...)` | design.md / components.md 内 | — | 4 資産に相対リンク構文は存在しない (ファイル名参照はバッククォート散文)。リンク切れ対象なし |

Decision ID (GOV-0002・TVL-xxxx) が複数ファイルで一致していても、ADR 正本が Repository 内に存在しないため provenance 確認済みとはしない。Source of Truth URL・実装 Repository は「文書に記載がある」という Fact のみを記録し、接続先内容の検証は行っていない。

## 13. Observations

観察区分は `alignment-plan.md` §8 のもののみを使用する。severity・優先度・数値スコアは付与しない。

| # | 対象ファイル | 節 / token path / Component | 直接証拠 | 比較対象 | 観察区分 | provenance | placeholder/実査待ち | 矛盾/不足 | Open Issue / Does Not Decide |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | semantic / primitive | token 参照全体 | semantic 参照 63/63 解決・未解決 0・循環なし | Semantic ↔ Primitive | 対応を直接確認できる (DS 内部) | 確認済み (Repository 内) | 2 参照が placeholder 先 | なし | — |
| 2 | primitive / semantic | shadow.* / motion.* / radius.card | `$status: placeholder` 計 10 件 | JSON `$note` / design.md | placeholder / 実査待ち | — | 該当 | なし (記述と整合) | placeholder 解決値は決定しない |
| 3 | design.md / components.md | Component 一覧・未着手一覧 | 定義済 10・未着手 5 が両文書で一致 | design.md §7 ↔ components.md | 対応を直接確認できる (DS 内部) | — | 一部 Component は実査待ち | なし | Component 必要性は判定しない |
| 4 | design.md | §8 / §9 (brand-content.md) | 「正: brand-content.md」だが不在 | Repository | 参照切れ | 参照先なし | — | 参照先不足 | 代替作成しない |
| 5 | design.md / components.md | naming-rules 参照 | `governance/naming-rules.md` 不在 | Governance README | 参照切れ | 参照先なし | — | 命名規則正本の不足 | 命名規則を作らない |
| 6 | 4 資産 | GOV-0002 / TVL-xxxx | Decision ID 参照ありだが ADR 正本なし | Governance README | provenance 未確認 | 未確認 | — | ADR 正本の不足 | Decision ID を再認定しない |
| 7 | 4 資産 | TVL-0009 | TVL-0009 が 4 資産のどこにも出現しない | TVL 連番 | 過剰/欠落の可能性 (観察のみ) | 未確認 | — | 連番の欠落 (意味は不明) | 欠落の解釈をしない |
| 8 | design.md / motion | follow-up #3 | DS は follow-up #3 を参照するが owner-decisions §3 に記載なし | owner-decisions.md §3 | provenance 未確認 | 未確認 | 実査待ち | 追跡先の不足 | 追跡先を推測しない |
| 9 | components.md | `{motion.transition.*}` | 参照先 semantic motion が placeholder | semantic | 一部のみ確認できる | 確認済み (参照解決) | 参照先が placeholder | なし | 解決値を決定しない |
| 10 | 4 資産 | Source of Truth URL / tocoo/tocoo_travel | GitHub URL・実装 Repository の記載あり | 外部 | 評価対象外 (外部参照) | 記載のみ・内容未検証 | — | — | 外部内容を検証しない |
| 11 | 4 資産 | metadata (Status/version/created) | 4 資産で一致 | 相互 | 対応を直接確認できる (DS 内部) | 確認済み | — | なし | — |

## 14. Constraints and Does Not Decide

- 評価対象 4 ファイルを一切変更していない (read-only)。
- 観察区分 (§13) は `alignment-plan.md` §8 のものだけを使用し、正式 Status・優先度・severity・Design Decision ではない。
- 「矛盾」「過剰」「対応する定義を確認できない」を、修正・削除・追加の Decision へ変換していない。
- placeholder / follow-up の解決値・Decision ID の有効性・ADR / 命名規則 / `brand-content.md` の内容・token 値の良否・Component の必要性・version bump・gap 解決策・修正優先度・実装方法・UI / 画面 / URL / route・SCR-006〜SCR-012 の DS 要件を決定しない。
- 上流 Service Design / 個別 Screen Requirement との Alignment は評価していない (Baseline の「対応を直接確認できる」は DS 内部の記述間対応に限定)。

## 15. Downstream Impact

- **Assets** ([../assets/README.md](../assets/README.md)) — `Not started`。本 Baseline の対象外。
- **Implementation** — Repository 管理対象外。実装 Repository (`tocoo/tocoo_travel`) の記載を確認したが、実装状態は確認していない。Baseline から実装画面・URL・route を導出しない。

## 16. Open Issues

以下は未決である。解決策は推測して記載しない。

- Baseline 結果の承認・解決・反映方法、および評価・承認主体。
- placeholder / 実査待ち token (計 10 件) の解決主体・値。
- follow-up #2 / #3 / #4 / #5 / #13 の解決内容と追跡先 (特に #3 は owner-decisions.md §3 に記載なし)。
- `brand-content.md`・`governance/naming-rules.md` の不足の解決主体。
- GOV-0002・TVL-0001〜TVL-0012 の ADR 正本の作成・有効性。
- TVL-0009 が 4 資産で参照されないことの意味 (欠番か未記録か)。
- Source of Truth URL・実装 Repository の接続先内容の検証方法。
- 上流 Service Design / 個別 Screen Requirement との Alignment (Work Order 2 以降)。
- Baseline 結果を後続 Alignment Assessment へ引き継ぐ方法。

## 17. Acceptance Criteria

- 文書 Status が Draft である。
- 評価対象 commit・4 ファイル・blob SHA・評価日が記録されている (§2)。
- 既存 4 資産を変更していない (read-only)。
- JSON 2 ファイルを実際に parse し、token 参照を全数検証している (§7・§8)。集計値は実測値である。
- placeholder / 実査待ち・provenance / 参照切れを全数抽出している (§11・§12)。
- 観察区分は `alignment-plan.md` §8 のものだけを使用し、数値スコア・適合率・合否点・severity を導入していない。
- 評価結果を修正・追加・削除 Decision へ変換していない。上流 Alignment を実施していない。SCR-006〜SCR-012 を評価していない。
- 不在文書・正本のない ADR を存在するものとして扱っていない。Decision ID を再認定していない。外部 Repository の内容を確認済みと主張していない。
- 受入基準の最終確定主体は Open Issue として保持する (§16)。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-16 | Initial baseline assessment of existing Design System 4 artifacts (commit 0d446152): metadata/JSON structure/token reference/cross-artifact consistency/component reference/placeholder/provenance を read-only で実測記録。既存資産の修正・上流 Alignment・gap 解決は未実施 | Draft |
