# オーナー確認事項 (分類C) — 一覧

- 種別: DS 成果物付属 (構築ロードマップ §4「オーナー確認ゲート」= 分類Cの確定必要事項を1箇所に集約)
- 状態: Draft
- 作成日: 2026-07-02
- 規約: 確認待ちを理由に構築は止めていない。各項目は placeholder として成果物に構造化済で、確定時に差し替え可能

---

## 1. 値論点 (open-questions Q1-9。暫定運用案で構築済)

| Q | 論点 | 影響 DS | 暫定運用 (成果物に適用済) |
| --- | --- | --- | --- |
| Q1 | 国内レンタカー主色赤の正値 (a #9E2334 / b #9B2030 / c #9F1E30) | rental-car | 暫定 #9E2334 (red.700)。ゾーン実装値 #9B2030 は現状維持。**インバウンドへ自動適用しない**。⚠ S-3: 実装着手ガイド§5-2 の provenance 索引は国内RC brand primary を #9B2030 (red.800) と記載しており、Q1 暫定運用案 (#9E2334) と引き渡しパッケージ内部で記述が割れている (オーナー判断時の混乱防止のため明記) |
| Q2 | テキスト主色 (1段/2段/各維持) | 3DS | 2段 (#424242 + #212121) を暫定共通。国内実測 #1F1F1F の扱い含む |
| Q3 | base unit (8px / 5px / 4px ハイブリッド) | 3DS | 刻み体系先行・4px 系で仮バインド (RC/IB 実装は 5px 系・宿泊は 16px map) |
| Q4 | root 基準・本文サイズ (16px統一 / ブランド別許容 / rem再定義) | 3DS | T-shirt スケール先行・root 未バインド。実測値で仮バインド |
| Q5 | breakpoint 統一値 | 3DS | 宿泊 foundation (600/768/992/1200) を暫定基準 (宿泊のみ自装値のため bound) |
| Q6 | 実装クラス命名方法論 (FLOCSS 等) | 3DS | トークンは憲章命名で先行 (要 ADR。Component 実装着手時) |
| Q8 | アイコン体系 (Material / FA6 / 自社 / lucide) | 3DS | 新規制作分のみ統一・既存維持 |
| Q9 | モーダル実装基盤 | 3DS | 新規は drawer 方向・既存併存 |

(Q7 はクローズ済: 顧客向けのみ = 2026-06-02 判断)

## 2. 本構築で新たに顕在化した確認事項

| # | 事項 | 影響 | 提案 (Claude Design) |
| --- | --- | --- | --- |
| 1 | インバウンド brand primary #9E2334 の公式承認 | inbound 全体 | ゾーン実装値 (本番確証) として bound 済。ブランド正値としての承認のみ要 |
| 2 | インバウンド link 色 blue #064f9e の存置/赤系へ寄せ | inbound リンク UI | 現状値で bind 済 (混載初版 $note の「赤系へ寄せる方向」は未決のまま) |
| 3 | 国内レンタカー link 正値 (現状 未スタイル既定青) | rental-car リンク UI | null placeholder。新 DS での用途トークン再定義が必要 [推奨] |
| 4 | 欧文 Outfit の採否 (付随論点) | inbound 見出し | Roboto 基準・Outfit は display (装飾) で保留 |
| 5 | 宿泊リンク色の使い分け (赤 #d10000 と紺 #283593 が併存) | travel リンク UI | text.link=赤 で bind 済。正規化は要議論 |
| 6 | Button variant 命名 (secondary / ghost / tertiary / text) | 3DS Button | 暫定名 + 要 ADR (命名規則 §10) |
| 7 | 国内本文 15px・IB h2 36px 等のスケール外実測値の正規化 | rental-car / inbound | Q4 と併せて判断 |
| 8 | サービス識別子 rental-car / inbound / travel の採用 | 3DS 全体・フォルダ/ファイル名 | 暫定採用 + 要 ADR (命名規則§6: サービス識別子は実装段階で確定)。確定まで現行識別子で運用 (S-6) |

## 3. 未取得データ (follow-up-research 13件のうち構築に影響したもの)

値の確定ではなく**追加調査**が必要な項目 (調査の実施判断はオーナー/運営):

| follow-up # | 項目 | 成果物での扱い |
| --- | --- | --- |
| #2 | フォーム入力/エラー/必須・検証 | Input 仕様を最小定義 + placeholder |
| #4 | ボタン状態 (hover/active/disabled/focus) | hover opacity 暫定。状態トークン未生成 |
| #5 | 宿泊/国内の success 色 | IB #58b85d を暫定参照 (placeholder) |
| #6 | RC コンテナ幅・画像比率 | 宿泊値を暫定参照 (placeholder) |
| #7 | 国内RC パンくず有無 | Breadcrumb 仕様を保留 |
| #8 | 横断使用件数 (Q1/Q3/Q5 の判断材料) | 件数なしで暫定判断 |
| #10 | 4言語レイアウト/フォント破綻・cn/kr fallback | fallback スロットを placeholder (null) |
| #13 | shadow 実値 | 暫定3段で据置き |
| #1 | Select/Tabs/Toast/Table/Accordion 実体 | Component 未着手として明示 |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Q1-9 暫定運用の適用状況・新規確認事項7件・未取得の扱いを集約) | Claude Design |
| 2026-07-02 | 是正 S-3 (Q1 に provenance 索引との記述齟齬を注記)・S-6 (サービス識別子の要 ADR を確認事項#8 に追加) | Claude Design (Builder) |
