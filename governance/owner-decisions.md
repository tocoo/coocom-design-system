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
- 規約: 恒久 ID・Decision ID は採番せず説明用の項目名で記録する。既存 §1〜§3 の項目・内容・暫定運用案は不変。本節の記録だけでは Review / Approval Rules 正本は作成されず、共通阻害 Fact も解決されない。GitHub PR がマージされたことを設計承認済みとする記録は追加しない。
- 回答状況: 全 11 項目についてオーナーの明示的回答を **2026-07-17** に取得し、下表「オーナー回答」列へ記録した (ユーザーが明示した内容を直接記録。要約による意味変更・主体の補完はしない)。回答に残る条件・未決は「残る Open Issue」列へ分離する。主体名はユーザーが Repository へ記載可能として明示した名称のみを使用する。

| 項目名 | 確認事項 | オーナー回答 (2026-07-17) | 残る Open Issue |
| --- | --- | --- | --- |
| 適用範囲 | Review / Approval Rules を国内宿泊 (travel) だけに適用するか、Repository 横断規則とするか | Repository 横断規則 (travel / rental-car / inbound 横断) とする | — |
| 候補採否の決定主体 | 改訂候補の採用・却下を誰が決定するか | Web部の責任者 | — |
| 改訂着手の承認主体 | Design System 改訂タスクの開始を誰が承認するか | Web部の責任者 (候補採否の決定主体と同一) | — |
| 責務の分割 | 内容レビュー・Repository 反映・未解決事項解決の責務をどう分けるか | **内容レビュー**: 影響度・高＝Web部責任者・チーフデザイナー／影響度・低＝Web部レビュー担当者。**Repository 反映**: 影響度・高＝Web部責任者・チーフデザイナーの必須レビューをゲートに反映確定／影響度・低＝当該2者のレビュー不要 (Web部レビュー担当者のレビューで反映)。**未解決事項の解決確認**: 未解決事項の性質に応じて分かれ、種別ごとの主体は本表「上流 Open Issue の解決単位」「Governance 正本の担当」「placeholder / 実査待ちの確認主体」で定義 (確認する主体＝各種別で解決を行う主体と同一)。**GitHub 操作**: commit／push／PR 作成＝作業担当者 (改訂作業の実施者)／merge＝レビュー後にレビュアーが実行 (影響度・高＝Web部責任者・チーフデザイナー、影響度・低＝Web部レビュー担当者) | — |
| 上流 Open Issue の解決単位 | Service Design / Screen Requirements の Open Issue について、解決主体をどの単位で定義するか | 単位は一意に固定せず重要度・影響度に応じる。主体は影響度・高＝Web部責任者・チーフデザイナー／影響度・低＝Web部レビュー担当者 | 各案件で全体共通／成果物別／論点別のどの単位を採るかの具体的な振り分けは案件ごと・未定 |
| Governance 正本の担当 | Governance・ADR・provenance・参照切れについて、正本作成または有効性確認を誰が担うか | 影響度・高＝Web部責任者・チーフデザイナー／影響度・低＝Web部レビュー担当者 (命名規則・ADR・provenance 確認・参照切れの正本作成／有効性確認) | — |
| placeholder / 実査待ちの確認主体 | placeholder・実査待ちの調査結果を誰が確認するか | 確認方法はルールに従う。そのルールを決める主体＝Web部責任者 | 個別項目の確認主体はルール制定まで未定 |
| GitHub 操作と設計承認の関係 | GitHub PR の approval または merge を設計承認として扱うか、別の明示的承認記録を必要とするか | merge を設計承認と同一視しない。別途、明示的な設計承認記録を必要とする | — |
| 承認結果の記録先 | 承認結果をどの Repository 成果物へ、どの状態表現で記録するか | 正本は owner-decisions.md にログとして記録 (承認日・承認主体等)。利用者向けに示すべき内容は別途 Wiki に文書として記録 (Wiki は非正本)。状態表現はログ形式 | ログの詳細な項目立ては将来の Review / Approval Rules で規定しうる |
| 再評価の条件 | 阻害 Fact 解消後に Work Order 6 相当の再評価をどの条件で行うか | 一旦 (暫定) 全候補一括。トリガー起点は、まず「承認・反映・解決主体の定義・記録」(全候補共通の阻害) の解消。参照切れ・placeholder / 実査待ちは未解消のままでも再評価へ進める (必須トリガーにしない) | 上流 Open Issue・provenance 未確認を必須トリガーとするかは未確定 |
| Alignment 完了条件の所在 | Alignment 完了条件をこの規則で扱うか、別の Governance 成果物で扱うか | 将来の Review / Approval Rules 正本の中に一節として定義する | 完了条件の内容自体は未定義 (本工程では中身を決めない) |

上表の記録は、Ordered Creation Steps ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) §12) の手順 1「確認事項への明示的回答」に対応する。回答の記録は、Review / Approval Rules 正本の作成・承認・適用、および Work Order 6 の再評価・共通阻害 Fact の全面解消を意味しない。

---

## 5. 設計承認ログ (Design Approval Log)

- 種別: 設計承認の記録 (正本)。上記 §1〜§4 (値論点・構築で顕在化した確認事項・未取得データ・Review / Approval Rules 作成前のオーナー確認事項) とは独立した設計承認の記録であり、混同しない。
- 規約: 本ログは設計承認の直接証拠である。GitHub PR の approval・merge を設計承認と同一視しない。恒久 Decision ID・正式 Status 体系は採番・新設しない (承認内容を追跡するための記録項目である)。

| 項目 | 内容 |
| --- | --- |
| 承認対象 | Governance Review and Approval Rules ([review-approval-rules.md](review-approval-rules.md)) |
| 承認内容 | Review / Approval Rules を Repository 横断規則として承認。責務区別・影響度別のレビュー／反映／GitHub 操作経路・設計承認と GitHub 操作の分離・承認ログ正本 (本ファイル)・規則ライフサイクル・再評価条件を承認。影響度の判定主体を Web部責任者の都度判断として定義。§19 Alignment 完了条件の 6 観点を承認。 |
| 承認日 | 2026-07-17 |
| 承認主体 | Web部責任者 |
| 適用範囲 | Repository 横断 (travel / rental-car / inbound を含む Repository 全体) |
| 根拠成果物 | [review-approval-rules.md](review-approval-rules.md) |
| 根拠 PR | 本承認記録 PR (Task 009-4): [#67](https://github.com/tocoo/coocom-design-system/pull/67) |
| 適用開始条件 | 本承認記録 PR (Task 009-4) が main へマージされた時点。承認・PR ブランチ上では未適用。 |
| 条件付き承認の条件 | 下記「承認後も残る Open Issue」を承認後に持ち越すことを前提とする条件付き承認 (承認前の追加解決は要求しない)。 |
| 承認後も残る Open Issue | ① 影響度・高／低の明文判定基準は現時点では設けられない (判定主体は Web部責任者の都度判断として定義済み)。② 上流 Open Issue の具体的解決単位は案件ごと・未定。③ placeholder／実査待ちの個別確認主体は Web部責任者が確認方法を定めるまで未定。④ Work Order 6 再評価で上流 Open Issue・provenance 未確認を必須トリガーとするかは未確定。⑤ 命名規則・ADR・用語定義・Repository principles の正本は未整備。 |

本承認は Review / Approval Rules の承認であり、Travel Work Order 6 の評価結果を自動的に変更しない。本承認および本 PR のマージは、改訂候補の採否・Design System 改定要否・改訂着手・Work Order 6 再評価・Design System 改定を意味しない。影響度・高／低の判定結果は Wiki (非正本) に記録する ([review-approval-rules.md](review-approval-rules.md) §8)。

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Q1-9 暫定運用の適用状況・新規確認事項7件・未取得の扱いを集約) | Claude Design |
| 2026-07-02 | 是正 S-3 (Q1 に provenance 索引との記述齟齬を注記)・S-6 (サービス識別子の要 ADR を確認事項#8 に追加) | Claude Design (Builder) |
| 2026-07-17 | §4 (Review / Approval Rules 作成前に必要な確認事項) を独立節として追加。Travel Work Order 6 の共通阻害 Fact への対応整理 ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) 連動)。既存 §1〜§3 の項目・内容・暫定運用案は不変。回答・主体割当は未記入 | Claude Code |
| 2026-07-17 | §4 の全 11 項目へオーナーの明示的回答 (2026-07-17 取得) を記録。表を「確認事項／オーナー回答/残る Open Issue」の列構成へ変更。残る未定・条件付きは Open Issue 列へ分離。既存 §1〜§3 は不変。正式 Status 体系は新設せず、規則正本の作成・承認・適用や Work Order 6 再評価は行っていない | Claude Code |
| 2026-07-17 | Task 009-4: §5 設計承認ログを §1〜§4 と分離して追加。オーナー (Web部責任者) が Governance Review and Approval Rules を Repository 横断規則として明示的に承認 (2026-07-17)。適用開始は本承認記録 PR の main マージ後とし、承認後も残る Open Issue を条件として明記。恒久 Decision ID・正式 Status 体系は新設せず。既存 §1〜§4 は不変。Work Order 6 の再評価・Design System 改定は行っていない | Claude Code |
