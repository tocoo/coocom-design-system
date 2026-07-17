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

## 4. Review / Approval Rules 作成前に必要な確認事項 (Governance)

- 種別: Governance レビュー・承認規則の正本作成前に必要なオーナー確認事項。上記 §1〜§3 (値論点・構築で顕在化した確認事項・未取得データ) とは独立した論点であり、混同しない。
- 背景: Travel の Work Order 6 (改訂着手可否評価, [../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)) が、全 12 候補側面を「現時点では開始できない」と判断し、全候補共通の阻害 Fact として「実際の改訂タスクの承認・反映・解決主体が Repository 内で未定義」を記録した。整理は [review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) (Draft) を参照。
- 規約: 恒久 ID・Decision ID は採番せず説明用の項目名で記録する。回答・推奨案は未記入 (推測しない)。本節の追加だけでは Review / Approval Rules 正本は作成されず、共通阻害 Fact も解決されない。

| 項目名 | 確認事項 (未回答) |
| --- | --- |
| 適用範囲 | Review / Approval Rules を国内宿泊 (travel) だけに適用するか、Repository 横断規則とするか |
| 候補採否の決定主体 | 改訂候補の採用・却下を誰が決定するか |
| 改訂着手の承認主体 | Design System 改訂タスクの開始を誰が承認するか |
| 責務の分割 | 内容レビュー・Repository 反映・未解決事項解決の責務をどう分けるか |
| 上流 Open Issue の解決単位 | Service Design / Screen Requirements の Open Issue について、解決主体をどの単位で定義するか |
| Governance 正本の担当 | Governance・ADR・provenance・参照切れについて、正本作成または有効性確認を誰が担うか |
| placeholder / 実査待ちの確認主体 | placeholder・実査待ちの調査結果を誰が確認するか |
| GitHub 操作と設計承認の関係 | GitHub PR の approval または merge を設計承認として扱うか、別の明示的承認記録を必要とするか |
| 承認結果の記録先 | 承認結果をどの Repository 成果物へ、どの状態表現で記録するか |
| 再評価の条件 | 阻害 Fact 解消後に Work Order 6 相当の再評価をどの条件で行うか |
| Alignment 完了条件の所在 | Alignment 完了条件をこの規則で扱うか、別の Governance 成果物で扱うか |

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Q1-9 暫定運用の適用状況・新規確認事項7件・未取得の扱いを集約) | Claude Design |
| 2026-07-02 | 是正 S-3 (Q1 に provenance 索引との記述齟齬を注記)・S-6 (サービス識別子の要 ADR を確認事項#8 に追加) | Claude Design (Builder) |
| 2026-07-17 | §4 (Review / Approval Rules 作成前に必要な確認事項) を独立節として追加。Travel Work Order 6 の共通阻害 Fact への対応整理 ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) 連動)。既存 §1〜§3 の項目・内容・暫定運用案は不変。回答・主体割当は未記入 | Claude Code |
