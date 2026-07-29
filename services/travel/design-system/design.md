# 国内宿泊予約 Design System (travel) — design.md

- 種別: DS 成果物 (design.md = 統合文書)
- 状態: Draft (0.3.0-draft)
- 作成日: 2026-07-09
- Source of Truth: https://github.com/tocoo/coocom-design-system/tree/main/services/travel/design-system (R3-10)
- 対象: 顧客向け UI のみ (管理画面は対象外)
- 実装の所在: GitHub `tocoo/tocoo_travel`
- 独立性: 本 DS は国内レンタカー・インバウンドレンタカーと Foundation/Semantic/Component/design.md を共有しない (要求仕様 R1)。命名・運用規約のみ3サービス共通 (`governance/` 参照 = R2)

---

## 1. 概要・ブランド位置づけ

- [事実] サービス: ToCoo! 宿泊予約 (tocoo.jp)。国内宿泊予約の顧客向けサイト
- [決定] 主色=メイン: ロイヤルブルー `#2C50C8` (brand.primary)。サブ: ヴィヴィッドインディゴ `#4845D4` (brand.secondary)。オーナー決定 2026-07-10 (TVL-0010)。旧 主色 紺 `#283593` (navy) から変更
- [事実] 固有要素: 星評価 (ReviewStars)・価格強調タイポ (PriceTag)。レンタカー2サービスには無い
- [観察] コピートーンは実用・価格訴求。CTA 文言例「プラン選択へ」。**詳細の委任先として記載されていた `brand-content.md` は Repository 内に存在しない** (参照切れ = [README.md](README.md) §8・§16)。現時点で確認できるブランド／コンテンツ規則の記載箇所は §8
- [事実] 負債の非持込: Bootstrap 残骸 `--primary:#007bff`・変数二重定義・管理画面系の色 (teal `#1798A5` 等) は本 DS に持ち込まない
- [事実] 非構築: 会員ランク色 (破棄済)

## 2. カラー

正: `semantic.travel.json` (用途) → `primitive.travel.json` (値)。以下は要約。配色は **共有ファウンデーション＋ブランド2スキーム** の二層 (TVL-0010)。全スキーム共通 (共有) は器/ニュートラル (白基調 warm-gray)・テキスト・境界のみ (surface/text/border)。状態色 (success/error)・特集アクセント・評価色 (星)・リンクは **per-scheme** = 各スキームが自スキームの値を保持 (TVL-0011。正式採用時に共通化): `color.scheme.main` = メイン(royal) / `color.scheme.sub` = サブ(indigo)。各スキームは tint(50)/soft(300)/base(500)/hover(600)/pressed(700)/ink(900)/**inverse(逆色)**/error/accent。

| 用途 (Semantic) | 参照 | 値 | 状態 |
| --- | --- | --- | --- |
| `color.scheme.main.*` (メイン=royal) | royal.50/300/500/600/700/900 + amber.500 + red.400 + orange.400 | tint #E8EDFB / soft #8E9EE6 / base #2C50C8 / hover #2340A6 / pressed #1B3488 / ink #14224A / **inverse #C8912C (アンバー・逆色)** / error #D23A3A / accent #E4572E | bound (TVL-0010/0011) |
| `color.scheme.sub.*` (サブ=indigo) | indigo.50/300/500/600/700/900 + gold.500 + rose.500 + coral.500 | tint #EDECFB / soft #928EE4 / base #4845D4 / hover #3936B0 / pressed #2C2A8C / ink #191840 / **inverse #C8B12C (ゴールド・逆色)** / error #D2405F / accent #E0553C | bound (TVL-0010/0011) |
| `color.brand.primary` (メイン) | scheme.main.base | `#2C50C8` | bound (白背景 ≈6.8:1) |
| `color.brand.primaryHover` | scheme.main.hover | `#2340A6` | bound |
| `color.brand.secondary` (サブ) | scheme.sub.base | `#4845D4` | bound (白背景 ≈6.8:1) |
| `color.brand.secondaryHover` | scheme.sub.hover | `#3936B0` | bound |
| `color.text.strong` / `body` | gray.900 / 800 | `#212121` / `#424242` | **bound (TVL-0003)** |
| `color.text.mutedStrong` | gray.700 | `#616161` | bound (白背景 ≈6.2:1) |
| `color.text.muted` | gray.600 | `#9e9e9e` | bound (白背景 ≈2.7:1) |
| `color.text.inverse` (inverse 面の主要文字) | white | `#ffffff` | bound (inverse 面 #212121 上 ≈16.10:1) |
| `color.text.inverseMuted` (inverse 面の補助情報) | gray.600 | `#9e9e9e` | bound (inverse 面 #212121 上 ≈6.01:1・明色面には使用しない) |
| `color.text.onAccent` (campaign accent 面の文字) | white | `#ffffff` | bound (accent 面 #E4572E 上 ≈3.68:1・**大きなテキスト相当のみ**) |
| `color.text.link` | scheme.main.base (副色=sub.base) | `#2C50C8` / `#4845D4` | bound (TVL-0011・リンク=主色。TVL-0005 解決) |
| `color.surface.default/subtle/muted` | white / gray.50 / 100 | `#fff` / `#f9f9f9` / `#f5f5f5` | bound |
| `color.border.subtle/default/strong` | gray.300/400/500 | `#e0e0e0` / `#ccc` / `#bcbcbc` | bound |
| `color.state.success` | scheme.main.base (副色=sub.base) | `#2C50C8` / `#4845D4` | bound (TVL-0011・成功=各パレット主色。専用緑廃止) |
| `color.state.error` | scheme.main.error (副色=sub.error) | `#D23A3A` / `#D2405F` | bound (TVL-0011・per-scheme・正式採用時共通化) |
| `color.accent.campaign` | scheme.main.accent (副色=sub.accent) | `#E4572E` / `#E0553C` | bound (TVL-0011・per-scheme・正式採用時共通化) |
| `color.focus.ring` | brand.primary | `#2C50C8` | bound (白背景 ≈6.8:1) |
| `color.icon.rating` | scheme.main.inverse (副色=sub.inverse) | `#C8912C` / `#C8B12C` | bound (TVL-0011・評価色=各パレット逆色) |

- [事実] 品質基準: WCAG 2.2 AA を最低ラインとし DS には違反値を入れない (要求仕様 R9)。本文 #424242 ≈9.7:1・主色 royal #2C50C8 ≈6.8:1・副色 indigo #4845D4 ≈6.8:1 いずれも AA 適合 (AAA 7:1 は未達)
- [事実] テキスト色は 4 段構成 (`strong` #212121 / `body` #424242 / `mutedStrong` #616161 / `muted` #9e9e9e)。判読性を必要とする補助情報 — 補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件 — は `color.text.mutedStrong` (白背景 ≈6.2:1) を使用する。`color.text.muted` (白背景 ≈2.7:1) は通常テキストに求められる 4.5:1 に達しないため、判読性を要する情報には用いない。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (適用規格・達成レベルは未確定)

### 2.1 面 (背景) と文字色の組み合わせ規則

色を**面 (背景)** として使う場合、許可される文字色と文字サイズ・ウェイトの条件は面ごとに異なる。以下は本書で検証した組み合わせであり、ここに無い組み合わせを検証済みとして扱わない。

| 面 (背景) | 文字 | 概算 | 通常テキスト (4.5:1) | 大きなテキスト (3:1) | 扱い |
| --- | --- | ---: | --- | --- | --- |
| `color.accent.campaign` `#E4572E` | `color.text.onAccent` `#FFFFFF` | 3.68:1 | 未達 | 達成 | **条件付きで許可** (大きなテキスト相当のみ) |
| `color.accent.campaign` `#E4572E` | `color.text.strong` `#212121` | 4.37:1 | 未達 | 達成 | 条件付き (通常テキストは不可) |
| `color.surface.inverse` `#212121` | `color.text.inverse` `#FFFFFF` | 16.10:1 | 達成 | 達成 | 許可 |
| `color.surface.inverse` `#212121` | `color.text.inverseMuted` `#9E9E9E` | 6.01:1 | 達成 | 達成 | 許可 (補助情報) |
| `color.scheme.*.inverse` `#C8912C` | `#FFFFFF` | 2.78:1 | 未達 | 未達 | **禁止** |
| `color.scheme.*.inverse` `#C8912C` | `color.text.strong` `#212121` | 5.78:1 | 達成 | 達成 | 許可 |
| `color.surface.default` `#FFFFFF` | `color.accent.campaign` `#E4572E` (文字色として) | 3.68:1 | 未達 | 達成 | 条件付き (大きなテキスト相当のみ) |

#### campaign accent 面上の文字

- [事実] `color.accent.campaign` (`#E4572E`) 上では、白文字 3.68:1・濃色文字 `#212121` 4.37:1 のいずれも通常テキストの 4.5:1 に達しない。**既存色の範囲では、campaign accent 面上で任意サイズの通常テキストを成立させる文字色は存在しない**
- [決定] campaign accent 面上の文字色は `color.text.onAccent` を使用し、**WCAG 2.2 上の大きなテキストに該当する場合に限定する**。最低条件は `24px` 以上の通常ウェイト、または約 `18.7px` 以上の bold 相当
- [決定] 実運用上の誤差・フォント差を避けるため、**DS の推奨最低値は `20px / bold 以上`** とする。ただし 20px 未満でもウェイトを上げれば自動的に適合するという定義にはしない
- [決定] `color.text.onAccent` の存在は「白であれば常にアクセシブル」を意味しない。背景色と文字サイズ・ウェイトの確認を省略しない

#### 20px 未満 (小サイズ) の代替規則

20px 未満の割引率ラベル・通常テキストには `color.accent.campaign` を**面として使用しない**。次のいずれかを用いる。

1. **[既定] neutral dark 面へ切り替える** — 背景 `color.surface.inverse` (`#212121`) + 文字 `color.text.inverse` (16.10:1)。既存トークンのみで AA を満たすため、小サイズの割引率ラベルの既定とする
2. accent を**文字色**として白または淡色面 (`color.surface.default` / `subtle` / `muted`) に置く — ただし白面上 3.68:1 のため、この場合も大きなテキスト相当に限る
3. accent を面ではなく**境界色・アイコン・点的装飾**に限定する (非テキスト UI 要素の 3:1 は満たす)

- [事実] 上記はいずれも既存 palette の組み合わせで成立するため、代替背景色の primitive を新設していない
- [決定] 禁止: campaign accent 面上に 12px〜16px 程度の白文字を置く / `onAccent` の存在だけを理由にコントラスト確認を省略する / AA 未達を「ブランド表現」で自動的に許容する / 文字へ縁取り・影を付けることでコントラスト不足を解決したものとして扱う

#### scheme inverse 色を面として使用する場合

- [事実] `color.scheme.main.inverse` (`#C8912C`) 上の白文字は 2.78:1 であり、通常テキスト 4.5:1 だけでなく大きなテキスト 3:1 も満たさない
- [決定] 本色を面として使用する場合の文字色は `color.text.strong` (`#212121`・5.78:1) を原則とする。白文字は正式な通常利用として許可しない
- [事実] semantic alias (`color.text.onSchemeInverse` 等) は追加していない。現在 `color.scheme.*.inverse` の確認できる用途は評価色 (`color.icon.rating` = 文字/アイコン色) のみで、**面としての正式用途が正本上未定義**であるため、組み合わせ規則のみを本書に記載した (既存 semantic 設計の粒度に合わせ、面用途を先に既成事実化しない)
- [Owner判断事項] 既存の Owner 指示で `#C8912C` 面上の白文字が指定されている場合、**現行指示とアクセシビリティ基準は矛盾する**。DS 側で Owner 指示を自動的に上書きしない。AA 適合案は濃色文字であり、白文字を維持するには背景色の変更が必要となる。最終判断は Owner 事項。「Owner 指示」を理由に AA 適合済みとして扱わない
- [事実] 副色スキームの `#C8B12C` 上のコントラスト比は本書では未検証

#### 評価色と販促面色の用途境界

- [事実] `{color.scheme.main.inverse}` / `{color.scheme.sub.inverse}` を `$value` で参照する semantic トークンは `color.icon.rating` (ReviewStars 星の色) の 1 件のみである (`semantic.travel.json` 全文検索で確認)。`color.brand.*` / `color.state.*` / `color.accent.campaign` はいずれも scheme の `base` / `error` / `accent` を参照し、`inverse` は参照していない。`color.scheme.sub.inverse` を参照する semantic トークンは存在しない (副色文脈での適用は per-scheme の記述として保持されている)
- [決定] 評価色 (`color.icon.rating`)・割引/販促色 (`color.accent.campaign`)・ブランド補色 (`color.scheme.*.inverse`)・状態色 (`color.state.*`) を同一用途へ統合しない (上流 `../service-design/content-principles.md` CTP-010「事実・条件・サービス上の判断・販促表現を混同しない」と整合)
- [決定] 評価用途は既存定義を維持する。`color.icon.rating` を割引ラベル・販促面・状態色へ流用しない
- [Owner判断事項] **`color.scheme.*.inverse` を割引ラベル背景へ使用できるかは未定義**。根拠となる正本・Owner 決定が Repository 内に存在しないため、DS では用途追加を確定しない。推奨案は campaign accent との役割を明確に分離すること (割引/販促 = `color.accent.campaign`、評価 = scheme 逆色)

## 3. タイポグラフィ

root 16px・**rem 基準** (TVL-0001)。2 書体構成 = 明朝 (表現) + ゴシック (機能)。タイポグラフィ設計方針 (共有 dc) 2026-07-10 の決定を反映。

| 用途 | 値 | 状態 |
| --- | --- | --- |
| 本文・UI | LINE Seed JP / 1rem / lh 1.8 | **bound (Q1)** |
| 見出し (一覧・カード) | LINE Seed JP 700 / h2 2rem | **bound (Q2)** |
| Display・Hero・詳細施設名 | Noto Serif JP (明朝) 500–600 | **bound (Q8)** |
| 欧文 | LINE Seed JP に統合 (旧 Roboto 廃止) | bound |
| 数字 (価格) | LINE Seed JP 700・tabular-nums (旧 Barlow 900 廃止) | **bound (Q3)** |

- サイズスケール: xs 0.75 / sm 0.875 / md 1 / lg 1.125 / xl 1.25 / 2xl 1.5 / 3xl 2 / 4xl 2.5 / display-lg 3rem (48px・Q4)
- 行間: tight 1.3 / normal 1.5 / relaxed 1.8 (本文)
- [注意] 実装移行時に px→rem の書き換えが発生する (TVL-0001 Consequences)
- [観察] 特集頁の見出しフォント不一致・壊れた font stack は新規制作で再生産しない

## 4. スペーシング・グリッド・ブレークポイント

- スペーシング: **4px (0.25rem) 系で確定** (TVL-0002)。spacing.0〜16 全段 bound
- コンテナ幅: `975 / 1195 / 1425px` (宿泊実装値・bound)
- ブレークポイント: **`640 / 768 / 1024 / 1280px`** (TVL-0004。現代標準へ更新 — 旧実装値 600/992/1200 からの変更。移行方針は TVL-0004 参照)。**本値は 3DS 共通 breakpoint として再認定** (owner-decisions.md Q5 決定・2026-07-24・Task 009-18-BP1)。ADR 正本・provenance は未確認 (009-19 provenance トラックへ残す)
- 代表 viewport (画面設計・Claude Design・HTML 確認用の表示幅): **`390 / 768 / 1280 / 1440px`** (3DS 横断・Web部責任者判断 2026-07-24・Task 009-18-BP1)。**これは表示確認用の代表幅であり responsive breakpoint token ではない** (breakpoint は上記・`breakpoint.*` token が正)

## 5. 角丸・シャドウ

- 角丸: `radius.sm 4 / md 8 / lg 16 / full 9999px` (bound)。用途トークンは 3 系統
  - `radius.action` = full (pill) — ボタン・CTA・入力要素・チップ型操作要素。宿泊のサービスシグネチャ
  - `radius.card` = 暫定 md (8px) — カード外形。🚧 実px未取得
  - `radius.badge` = 暫定 sm (4px) — **非操作**のバッジ・ラベル (割引率ラベル・状態バッジ・カテゴリラベル・短い補助ラベル)。🚧 実px未取得
- [決定] 割引率ラベル・状態バッジへ `radius.action` (pill) を使用しない。pill 形状はボタン・操作要素のシグネチャであり、非操作のラベルに用いると操作要素と誤認される。**バッジが操作可能な場合は badge ではなく action 系 Component として扱う** (その場合の角丸は `radius.action`)
- [事実] `radius.badge` の参照先 sm (4px) は既存 primitive radius scale からの暫定選定であり、新しい数値は追加していない。選定根拠は ①`radius.action` (pill) との形状差別化 ②`radius.card` (暫定 md) との階層差 ③小サイズラベルでの形状安定。実確定は `radius.card` と同じ実査待ち区分
- シャドウ: 実値未抽出 🚧 (follow-up #13。暫定3段で据置き = TVL-0008)

## 6. アイコン・画像

- アイコン体系: **Font Awesome 6 で確定** (TVL-0006)。新規制作は FA6 に統一、既存 Material 混在箇所は改修時に置換。サイズスケールは `iconSize.sm〜xl` (bound)
- 画像比率: object-fit 制御あり
- 画像なし・在庫ゼロ時の表現: 未定義 ❓ 検討トリガー: Card 実装着手時

## 7. コアコンポーネント

正: `components.md`。定義済: Button / Input / SearchForm / Card (ResultCard) / PriceTag / ReviewStars / Header / Footer / Breadcrumb / Modal。

- 実装は Semantic のみ参照 (primitive 直接参照禁止)
- 状態リストは固定 (hover/active/focus/disabled/loading/error/success)。宿泊のボタン状態は未取得 🚧
- Button variant 語彙は GOV-0002 (cross-service 5語)。**travel の Button 実装は4語 (primary/secondary/ghost/text)**。campaign(accent 塗りボタン)は廃止し accent はバッジ/割引ラベルの点専用 (TVL-0012)
- PriceTag は背景文脈を**明示的に選択する軸 (tone)** を持ち、`default` (明色面) と `inverse` (inverse 面) の 2 値を定義する。inverse 面では主要価格 `color.text.inverse`・補助価格/価格条件注記/割引前価格 `color.text.inverseMuted` を使用する (対応関係の正は `components.md`)。背景色を検知して自動反転する仕様・コンポーネント内部の固定色だけで複数背景へ対応する仕様は採らない。**tone は variant 語彙 (GOV-0002) とは別軸であり、variant 語彙への追加ではない**。実装 API 名 (prop 名) は未確定 ❓
- モーダルは **最終的に drawer へ全面統一**。centered dialog は deprecated・段階移行 (移行期間中は併存)。現在の方針根拠は `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**)。3DS 横断の Modal 実装基盤 (同 §1 Q9) は**未決**。`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認のため、現在の仕様根拠として参照しない (R-D provenance トラック)
- 未着手: Select / Tabs / Toast / Table / Accordion (実体皆無)

## 8. ブランド・クリエイティブガイド

- [事実] **ライティング・価格表記の正本として参照されていた `brand-content.md` は Repository 内に存在しない** (参照切れ。[README.md](README.md) §8・§16 が「`brand-content.md` の参照と実在状況 (存在しない)」を未決 Open Issue として保持)。**存在しない参照を確認済みの正本として扱わない**。本節が現時点で確認できるブランド／コンテンツ規則の記載箇所であり、`brand-content.md` の新規作成は行っていない (作成の要否は §8.1 末尾の Owner判断事項)
- [事実] 上流のコンテンツ規則正本 [../service-design/content-principles.md](../service-design/content-principles.md) は Draft として存在するが、§10 Open Issues で「正式な用語集・表記規則」「価格・税・手数料等の表示基準」をいずれも**未決**として保持し、§8 Boundary で具体的な文言・キャンペーンコピーを対象外としている。[../service-design/information-architecture.md](../service-design/information-architecture.md) IA-OBJ-007 Price も「正式な料金構造や表示単位は確定しない」と明記する
- [観察] 価格中心・実用トーン。数字を大きく強調する価格タイポがブランド表現の中核
- [事実] 特集は `#EF4123` を面で多用。通常導線と特集を色で分離する現状構造を維持
- [事実] 写真選定基準は未明文化 ❓ 検討トリガー: ブランドルール整理時
- [事実] ロゴファイルは未提供。プレーンな "ToCoo!" ワードマーク (見出しフォント + brand primary) で代用中。実ロゴ提供時に差し替え

### 8.1 割引率の表記規則

**本節は「表示 (表記) 規則」のみを定義し、割引率の算出方法・端数処理・上限値といった事業・価格仕様は定義しない。** 算出規則と表示規則を混同しない。

#### 表示形式

- [決定] 基本形は `-NN%` (半角マイナス + 半角数字 + 半角パーセント)。例: `-5%` / `-20%` / `-35%`
- [決定] 原則として使用しない表記: `20%OFF` / `20％引き` (全角パーセント) / `▲20%` / `最大20%OFF` (条件付き表現の既定使用)。同一の意味へ複数表記を混在させない (CTP-005 Consistent Terminology)
- [事実] 上記と異なる明示的な規則が Owner 決定またはブランドガイドラインに存在する場合はそれを優先し根拠を記録する。**現時点で Repository 内に該当する Owner 決定は確認できない** ([../../../governance/owner-decisions.md](../../../governance/owner-decisions.md) に割引率表記の決定記録なし)

#### 符号

- [決定] 割引率であることを視覚的に示すため、数値の前に半角マイナス `-` を付す
- [決定] これは**表示規則として付与する記号**であり、計算上の負数をそのまま出力するものではない

#### 桁

- [決定] 半角数字を使用する / 原則として整数表示 / 不要な先頭ゼロを付けない (`-05%` は不可) / 小数点以下を表示しない

#### 端数処理 (未確定)

- 🚧 **表示上の暫定案**: 小数点以下切り捨て
- ❓ **未確定事項**: 正式な算出式と端数処理
- **決定主体**: 価格・商品仕様の Owner
- [決定] DS は事業上の価格算出方法を新規決定しない。上記の暫定案を DS の正式規則として扱わない

#### 上限および異常値

割引ラベルを**表示しない**条件 (DS の表示規則として定義):

- [決定] 算出結果が `0%` 以下の場合
- [決定] 算出不能の場合
- [決定] 元価格が存在しない場合
- [決定] 販売価格が元価格以下でない場合 (=値引きが成立しない場合)

DS では確定しない事項 (Owner判断事項):

- ❓ `100%` 以上となるデータの扱い
- ❓ 表示可能な上限値
- ❓ 「最大」「〜」等の条件付き表現を使用する条件
- [決定] 上限値・異常値処理が上流仕様に無い状態で、DS が任意の数値を決定しない

#### 表示内容の真実性 (表示成立条件)

- [決定] 割引率は、比較対象となる価格・対象条件・税条件・人数・日程等が**一致する場合にのみ**表示できる
- [決定] DS は価格計算ロジックを定義しない。上記は表示が成立するために必要な前提の記載である
- [決定] 根拠・対象・期間・基準が不明な場合は確定表現にしない (CTP-004 Evidence-backed Claims)
- [決定] 割引率は販促表現であり、施設・料金・条件等の Fact と区別できる表現とする (CTP-010)

#### 割引率と値引額

- ❓ **未確定事項**: 割引率 (`-NN%`) と値引額 (金額) の使い分け基準。値引額を表示する場合の通貨記号・桁区切り等の表記も未決 (上流の価格表記基準そのものが未決 = `content-principles.md` §10)
- [Owner判断事項] 使い分け基準の決定主体は価格・商品仕様の Owner および ブランド Owner
- [Owner判断事項] 割引率等のコンテンツ表記規則を管理する正本を本節 (design.md §8) に置き続けるか、独立した文書 (`brand-content.md` 等) を新設するかは未決。新設する場合の文書体系上の位置づけ・管理責務・既存正本との関係は Owner 判断を要する。**本タスクでは推測で新規正本を作成していない**

## 9. Agent Prompt Guide

AI に本 DS で UI を生成させる際の読み順と規則:

1. `semantic.travel.json` を読み、色・フォントは Semantic トークン名で指定する (HEX 直書き・primitive 直接参照は禁止)
2. `components.md` の該当 Component の固定フォーマット (用途/バリアント/状態/Do・Don't) に従う
3. `$status=placeholder` のトークンは `$note` を確認し、生成物にも「🚧 暫定」を伝播させる
4. 宿泊固有要素: 評価は ReviewStars、価格は PriceTag (数字900+円+補助) を必ず使う
5. 禁止: `--primary:#007bff`・会員ランク色・**他サービスのトークン値の流用 (R1-6)**
6. 迷ったら: `governance/naming-rules.md` → 本書 §1〜8

## 未確定事項の一覧

| 論点 | 内容 | 状態 |
| --- | --- | --- |
| TVL-0005 | リンク色 (赤 #d10000 / 紺 #283593) | ✅ 解決 (TVL-0011・リンク=各スキーム主色) |
| follow-up #4 | ボタンの hover 以外の状態 (active/focus/disabled/loading) 一式 | 🚧 実査待ち (TVL-0008)。※ brand primaryHover は TVL-0010 で解決 (royal.600) |
| follow-up #13 | shadow 実値 | 🚧 実査待ち |
| follow-up #3 | motion 実値 | 🚧 実査待ち |
| follow-up #5 | success 色 | ✅ 解決 (TVL-0011・成功=各パレット主色) |
| follow-up #2 | フォーム入力/エラー/必須・検証 | 🚧 実査待ち |
| — | カード実px・8スロット対応付け・画像欠落 fallback | 🚧 実査待ち / ❓ Card 着手時 |
| Q6 | 実装クラス命名方法論 (FLOCSS 等) | ❓ 検討トリガー: Component 実装着手時 |
| — | Breadcrumb 現在地への `color.text.muted` (白背景 ≈2.7:1) 適用の可否 | ❓ 未判定。価格・補助情報の用途に該当せず、上流 NVP-001 (現在地の可視性) と全ページ共通 Component の影響範囲を伴うため本書では判定しない |
| — | `color.text.muted` の適用可能範囲 (装飾的・非必須の弱表現に限るか) の明文化 | ❓ 未判定。判読性を要する補助情報が `mutedStrong` を使用することのみ確定 |
| — | 割引率の正式な算出式・端数処理 | ❓ 未確定。決定主体 = 価格・商品仕様の Owner。DS の表示上の暫定案は「小数点以下切り捨て」(§8.1・正式規則ではない) |
| — | 割引率の表示可能な上限値・`100%` 以上のデータの扱い・「最大」等の条件付き表現を使用する条件 | ❓ 未確定。DS では任意の数値を決定しない (§8.1) |
| — | 割引率 (`-NN%`) と値引額 (金額) の使い分け基準・値引額の表記 | ❓ 未確定。上流の価格表記基準そのものが未決 (`../service-design/content-principles.md` §10) |
| — | 割引率等のコンテンツ表記規則の管理正本 (§8 に置き続けるか独立文書を新設するか) | ❓ Owner判断事項。参照切れの `brand-content.md` は推測で新規作成していない (README.md §16) |
| — | `color.scheme.*.inverse` を面 (背景) として使用する正式用途 (割引ラベル背景等) | ❓ 未定義。Owner判断事項。面として使う場合の文字色規則のみ §2.1 に定義 |
| — | `#C8912C` 面上に白文字を指定する既存 Owner 指示が存在する場合の解消 | ❓ Owner判断事項。白文字は 2.78:1 で通常・大きなテキストいずれも未達 (§2.1)。DS 側で Owner 指示を上書きしない |
| — | campaign accent 面上の通常テキスト (20px 未満) を成立させる濃色背景の追加要否 | ❓ 未判定。既存 palette の組み合わせで代替が成立するため primitive を新設していない (§2.1) |
| — | `radius.badge` の実px | 🚧 実査待ち。暫定 sm (4px)。`radius.card` と同じ区分 (§5) |
| — | PriceTag の tone (背景文脈) の実装 API 名 (prop 名) | ❓ 未確定。DS は default / inverse の 2 値と色の対応関係のみ定義 (`components.md`) |
| — | `color.text.inverseMuted` を inverse 以外の暗色面へ適用する場合の可否 | ❓ 未判定。検証済みは inverse surface `#212121` 上 (≈6.01:1) のみ |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-09 | 0.3.0-draft: 独立DS再構築 (要求仕様 R1〜R10)。TVL-0001〜0008 反映 (rem化・4px系・テキスト2段・BP現代標準・FA6・drawer統一・リンク色保留・実査待ちplaceholder維持) | Claude Design (Builder) |
| 2026-07-24 | Task 009-18-BP1: §4 に記述追加。ブレークポイント `640/768/1024/1280px` (TVL-0004) を 3DS 共通 breakpoint として再認定した旨を注記 (owner-decisions.md Q5 決定・2026-07-24。Travel token 値は不変)。代表 viewport (画面設計・HTML 確認用) `390/768/1280/1440px` を breakpoint とは別概念として §4 に追加 (3DS 横断・正本=各 design.md)。ADR 正本・provenance 未確認は 009-19 へ残す旨を明記。token・値・status・version は不変 | Claude Code |
| 2026-07-28 | Task 009-28R: §7 のモーダル記述について、`TVL-0007` を現在の仕様根拠として参照する表現を補正。現在の方針根拠は `governance/owner-decisions.md` §11 (2026-07-27, Web部責任者の現在判断・**travel 限定**) であること、3DS 横断の Modal 実装基盤 (同 §1 Q9) は**未決**であること、`TVL-0007` は ADR 正本が Repository 内に不在で historical provenance 未確認であるため現在の仕様根拠として参照しないことを明記した。**現行仕様そのものは不変** (drawer への全面統一・centered dialog の deprecated・段階移行はいずれも維持)。判断日 (2026-07-27) と本反映日 (2026-07-28) は別の事象として区別している。本工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-07-28、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。§7 の他記述・§1〜§6・§8〜§9・未確定事項の一覧・token・値・`$status`・version・Component の実装要件・rental-car / inbound の成果物は不変。`TVL-0007` の historical provenance 未確認と `alignment-blocking-facts-resolution-plan.md` §8L の R-D 分類は変更していない。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-28 | Task 009-28R の記述是正: PR [#107](https://github.com/tocoo/coocom-design-system/pull/107) コードレビュー (issuecomment-5098867540) の指摘に対応し、§7 のモーダル記述の冒頭を是正。**「モーダルは drawer に全面統一」という、統一が完了済みと読める記述を撤回**し、「モーダルは最終的に drawer へ全面統一」へ変更した。同 PR 内で `components.md` の実装基盤行を「最終的に drawer へ全面統一」へ補正した一方、本ファイルは補正前の表現のままとしていたため、**本 PR によって 2 文書間に表現の分岐が生じていた**。あわせて「段階移行」に「(移行期間中は併存)」を補い、`governance/owner-decisions.md` §11 の判断ⓐ (最終到達方針であり既存 centered dialog の即時廃止・一括置換を意味しない)・判断ⓒ (deprecated だが移行期間中の併存を認める) と読み取りを一致させた。**是正対象は §7 の当該 1 行のみ**。方針そのものは不変 (最終的に drawer へ統一する現行方針・centered dialog の deprecated・段階移行はいずれも維持) であり、即時廃止・一括置換・移行対象・順序・期限・完了条件を決定していない。§7 の他記述・§1〜§6・§8〜§9・未確定事項の一覧・token・値・`$status`・version・Component の実装要件・rental-car / inbound の成果物は不変 | Claude Code |
| 2026-07-29 | Task 009-33: §2 の表に semantic トークン `color.text.mutedStrong` (gray.700 `#616161`・bound・白背景 ≈6.2:1) の行を追加し、`color.text.muted` の行に白背景コントラスト値 (≈2.7:1) を補記した。§2 にテキスト色の 4 段構成 (`strong` `#212121` / `body` `#424242` / `mutedStrong` `#616161` / `muted` `#9e9e9e`) と、判読性を必要とする補助情報 (補助価格・税/人数/泊数等の価格条件注記・割引前価格・購買判断や内容理解に必要な補足条件) が `color.text.mutedStrong` を使用すること、`color.text.muted` は通常テキストに求められる 4.5:1 に達しないため判読性を要する情報には用いないことを [事実] として 1 行追加した。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない。未確定事項の一覧に 2 行追加した (Breadcrumb 現在地への `color.text.muted` 適用の可否・`color.text.muted` の適用可能範囲の明文化。いずれも本書では判定しない)。**不変**: §1・§3〜§9、§2 表の他の行、`color.text.muted` の参照先 gray.600 と値 `#9e9e9e` と `bound`、`color.text.body`、primitive の色値、他の token・`$status`、version 表記、Component の実装要件、rental-car / inbound の成果物。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-07-29 | Task 009-34: **§2 の表**に `color.text.inverse` / `color.text.inverseMuted` / `color.text.onAccent` の 3 行を追加した。**§2.1「面 (背景) と文字色の組み合わせ規則」を新設**し、検証した 7 組み合わせの表 (背景・文字・概算・通常テキスト 4.5:1 判定・大きなテキスト 3:1 判定・扱い)、campaign accent 面上の文字は `color.text.onAccent` を使用し大きなテキスト相当 (24px 通常ウェイト以上または約18.7px bold 以上) に限定すること、DS の推奨最低値を 20px / bold 以上とし 20px 未満でウェイトを上げても自動適合とはしないこと、20px 未満の代替規則 3 案 (既定 = `color.surface.inverse` 面 + `color.text.inverse` / accent を文字色として淡色面に置く場合も大きなテキスト相当のみ / accent を境界色・アイコン・点的装飾に限定)、禁止事項 4 件 (12〜16px の白文字・`onAccent` を理由としたコントラスト確認の省略・AA 未達のブランド表現としての自動許容・縁取り/影による代替)、`color.scheme.*.inverse` を面として使う場合は `color.text.strong` を原則とし白文字を正式な通常利用として許可しないこと、評価色・割引/販促色・ブランド補色・状態色を同一用途へ統合しない用途境界を記載した。**§5** に `radius.badge` (暫定 sm 4px) と非操作ラベルへ pill を使わない規則を追記した。**§7** に PriceTag の tone (default / inverse) を追記した。**§8** の「正: `brand-content.md`」を撤回し、同ファイルが Repository 内に存在しないこと・存在しない参照を正本として扱わないこと・現時点で確認できる記載箇所が §8 であることへ改めた。§1 の同ファイルへの委任表現も同様に改めた。**§8.1「割引率の表記規則」を新設**し、表示形式 (`-NN%`・原則使用しない表記)・符号 (表示規則として付与する記号)・桁 (半角/整数/先頭ゼロなし/小数非表示)・端数処理 (表示上の暫定案 = 小数点以下切り捨て／未確定事項 = 正式な算出式と端数処理／決定主体 = 価格・商品仕様の Owner を区別して記録し暫定案を正式規則として扱わない)・表示しない条件 4 件 (0% 以下・算出不能・元価格なし・販売価格が元価格以下でない)・DS で確定しない事項 3 件 (100% 以上の扱い・上限値・条件付き表現の使用条件)・表示成立条件 (比較対象価格・対象条件・税条件・人数・日程等の一致。DS は価格計算ロジックを定義しない)・割引率と値引額の使い分けが未決であることを記載した。**未確定事項の一覧に 11 行追加**した。**不変**: §3・§4・§6・§9、§2 表の他の行、§2 の既存 2 行 ([事実] 品質基準・テキスト 4 段)、既存 token の値・参照先・`$status`、primitive の色値、version 表記、Component の実装要件、rental-car / inbound の成果物。**作成していないもの**: `brand-content.md` (新設の要否・管理正本の所在は §8.1 に Owner判断事項として記載)、価格算出ロジック、事業上の割引率算出式、新規 primitive、`color.text.onSchemeInverse` 相当の alias。本書は適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (§2.1 のコントラスト比は概算の記録)。影響度は**未取得** (判定主体 = Web部責任者の都度判断 = [../../../governance/review-approval-rules.md](../../../governance/review-approval-rules.md) §8)。改訂着手の設計承認は取得していない (同 §9・§20)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
