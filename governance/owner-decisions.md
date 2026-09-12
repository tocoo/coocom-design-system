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
| Q5 | breakpoint 統一値 | 3DS | **決定 (2026-07-24, Web部責任者, Task 009-18-BP1): 3DS 共通 breakpoint = `640 / 768 / 1024 / 1280` (Travel `TVL-0004` の現行 bound 値を 3DS 共通値として再認定)。** 旧 `600 / 768 / 992 / 1200` は Travel 移行前の値であり現行 Travel foundation ではない (現行 Travel bound token は `640/768/1024/1280`)。RC / IB は本共通値へ統一 (breakpoint 値を変更・`$status` は placeholder 維持 = 各ゾーン実装 2段(959/960)・6段(320/520/692/800/960/961) との移行整理は follow-up #8 待ち)。`TVL-0004` の ADR 正本作成・provenance 解消は未了 (009-19 provenance トラックへ残す)。代表 viewport (画面設計・HTML 確認用) は breakpoint と別概念で各 `design.md` に記録 |
| Q6 | 実装クラス命名方法論 (FLOCSS 等) | 3DS | トークンは憲章命名で先行 (要 ADR。Component 実装着手時) |
| Q8 | アイコン体系 (Material / FA6 / 自社 / lucide) | 3DS | 新規制作分のみ統一・既存維持。**3DS 横断で統一する体系は未決** (rental-car / inbound を含む。本行の 4 候補は未決のまま維持)。一方、**国内宿泊 (travel) についてのみ 2026-07-27 に Web部責任者の現在判断を取得済み** (標準 = Font Awesome 6 / 新規制作は原則 FA6 統一 / 既存 Material は改修時に置換 / ReviewStars は FA6 `star` 維持 / `icon.reviewSize` の `$value = {iconSize.sm}`・`$status = bound` を維持)。適用範囲は travel 限定で rental-car / inbound / 3DS 横断共通体系へは自動適用しない (詳細は §10)。`TVL-0006` の ADR 正本・historical provenance は未確認 (009-19 provenance トラックへ残す) |
| Q9 | モーダル実装基盤 | 3DS | 新規は drawer 方向・既存併存。**rental-car / inbound を含む 3DS 横断で統一する Modal 実装基盤は未決** (本行の暫定運用は未決のまま維持)。一方、**国内宿泊 (travel) についてのみ 2026-07-27 に Web部責任者の現在判断を取得済み** (最終到達方針 = drawer へ統一／移行中状態 = 新規は原則 drawer・既存 centered dialog は当面併存／移行対象・順序・期限・完了条件・ロードマップは未決)。適用範囲は travel 限定で rental-car / inbound / 3DS 横断の共通 Modal 実装基盤へは自動適用しない (詳細は §11)。`TVL-0007` の ADR 正本・historical provenance は未確認 (009-19 provenance トラックへ残す) |

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

## 6. 適用開始の事実記録 (Activation Record)

- 種別: 適用開始条件成立の事実記録。上記 §5 設計承認ログとは分離した Fact の記録であり、新たな設計承認・承認種別・正式 Status 体系ではない。§1〜§5 の内容は本節で変更しない。
- 規約: GitHub の approval・merge を設計承認と同一視しない。本節は §5 で既に承認された規則について、承認時に定めた適用開始条件が満たされた Fact のみを記録する。恒久 Decision ID・正式 Status 体系は採番・新設しない。

| 項目 | 内容 |
| --- | --- |
| 対象規則 | Governance Review and Approval Rules ([review-approval-rules.md](review-approval-rules.md)) |
| 明示的承認 | §5 設計承認ログに記録済み（承認主体: Web部責任者、明示的承認日: 2026-07-17） |
| 適用開始条件 | 本承認記録 PR (Task 009-4) の main マージ（§5 の「適用開始条件」と同一） |
| 根拠 PR | [#67](https://github.com/tocoo/coocom-design-system/pull/67) |
| 条件成立を示す merge commit | `d095ded2998e0180ae6836747e8fbbd95a7a2ef1` |
| 現在状態 | 適用開始済み（適用中） |

本節は、§5 で承認された適用開始条件が PR #67 の main マージによって満たされた Fact の記録である。PR #67 の merge は既に承認された適用開始条件を満たした操作であって、それ自体を設計承認として扱わない（設計承認は §5）。本適用開始は、改訂候補の採否・Design System 改定要否・改訂着手・Travel Work Order 6 の再評価・Design System 改定を意味しない（Work Order 6 は未再評価）。

---

## 7. Travel上流Open Issue解決単位の案件別判断記録

- 種別: **Review / Approval Rules §12・§21② に基づく案件別のプロセス判断**の記録。上記 §1〜§6 (値論点・構築で顕在化した確認事項・未取得データ・Review / Approval Rules 作成前のオーナー確認事項・設計承認ログ・適用開始の事実記録) とは独立した記録であり、混同しない。**本記録は設計承認ではない**。§5 の Design Approval Log へ追加せず、既存の Review / Approval Rules の承認内容も変更しない。
- 規約: 恒久 Decision ID・新しい正式 Status・Phase・Gate は採番・新設しない。取得した回答は原文の意味を変えずに記録する。本記録は上流 Open Issue の内容を解決するものではなく、後続解決タスクを**どの単位で起票・追跡するか**だけを記録する。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | Task 009-7 ([../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md)) で整理された国内宿泊 (travel) サービスの上流 Service Design / Screen Requirements Open Issue 群 (Navigation 分類・Global Navigation・History and Recovery／状態モデルの業務定義／IA Object の業務モデル／入力・検索仕様／表示項目・料金・評価仕様／主要行動・CTA／可逆・回復フロー・サポート範囲／タイポグラフィ具体規格の扱い／アクセシビリティ適用規格の扱い) |
| 判断日 | 2026-07-21 |
| 判断主体 | Web部責任者 |
| 取得した回答 (原文の意味を変えず記録) | **「論点別」**。上記の上流 Open Issue 群を論点 (テーマ) ごとの単位で後続解決タスクとして起票・追跡する。 |
| 適用範囲 | 国内宿泊 (travel) サービスの今回の Alignment 阻害 Fact 解決経路。他サービス (rental-car / inbound) へは適用しない。 |
| 根拠 | Task 009-7 成果物 ([../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8 Q1・§9)、Review / Approval Rules ([review-approval-rules.md](review-approval-rules.md)) §12・§21②、本 Task (Task 009-8) の Issue #74 および本 Task の PR |
| 回答により確定した事項 | 後続の上流 Open Issue 解決タスクの起票・追跡単位を**論点別 (9 論点)** とすること。展開は [../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8A に記録。 |
| 回答後も未決の事項 | 各上流 Open Issue の内容そのもの／どの論点 (単位) から着手するか／ビジネス上の優先順位／各後続タスクの影響度 (Q5)／placeholder・実査待ちの確認方法 (Q2) と個別確認主体 (Q3)／provenance 未確認の扱い／再評価トリガー (Q4)／候補採否・改定要否・継続保留・改訂着手。いずれも本記録では決定・補完しない。 |

**Does Not Decide / Does Not Authorize**: 本記録は上流 Open Issue の内容を解決・close せず、Design System の改定要否・候補採否・継続保留・改訂着手・設計承認を決定・承認しない。Task 009-6 の全 12 候補「現時点では開始できない」を変更しない。Q2〜Q5 への回答を補完しない。個別確認主体・担当者・期限・工数を推測しない。GitHub の approval・merge を設計承認と同一視しない。本記録の起票単位に関する Wiki 記載があっても、本判断の正本は本 §7 である (Wiki は非正本)。

---

## 8. Travel上流Open Issue初回着手論点の案件別判断記録

- 種別: **Review / Approval Rules §8・§12 および Task 009-8 の解決計画に基づく案件別のプロセス判断**の記録。上記 §1〜§7 とは独立した記録であり、混同しない。**本記録は設計承認ではない**。§5 の Design Approval Log へ追加せず、§7「解決単位＝論点別」の回答も上書きしない。既存の Review / Approval Rules の承認内容も変更しない。
- 規約: 恒久 Decision ID・新しい正式 Status・Phase・Gate は採番・新設しない。取得した回答は原文の意味を変えずに記録する。本記録は上流 Open Issue の内容を解決するものではなく、最初に扱う論点を特定し後続解決タスクを起票可能な状態にするための判断だけを記録する。最初に扱う論点の選択は、その論点の内容に対する承認ではない。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | Task 009-8 の解決計画 ([../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md)) §8A.2 で論点別に整理された 9 論点 (T1〜T9) |
| 判断日 | 2026-07-21 |
| 判断主体 | Web部責任者 |
| 提示した 9 論点 | T1 Navigation 分類・Global Navigation・History and Recovery／T2 状態モデルの業務定義／T3 IA Object の業務モデル／T4 入力・検索仕様／T5 表示項目・料金・評価仕様／T6 主要行動・CTA／T7 可逆・回復フロー・サポート範囲／T8 タイポグラフィ具体規格の扱い／T9 アクセシビリティ適用規格の扱い (各論点の対象上流成果物・対応 Design System 候補側面・完了条件・決定/承認しない事項は同計画 §8A.2 のとおり中立に提示) |
| 取得した回答 (原文の意味を変えず記録) | **「どれからでも構わない」** |
| 最初に扱う論点 | 特定の 1 件に限定されず、T1〜T9 の**いずれからでも着手してよい**というオーナー判断。単一論点の指定・順序付き・並行着手の明示・条件付き・現時点で選ばない、のいずれとも異なり、初回着手論点の優先順位・限定をオーナーからは付与しないという回答である。 |
| 適用範囲 | 国内宿泊 (travel) サービスの今回の Alignment 阻害 Fact 解決経路。他サービス (rental-car / inbound) へは適用しない。 |
| 根拠 | Task 009-8 成果物 ([../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8A)、[owner-decisions.md](owner-decisions.md) §7、Review / Approval Rules ([review-approval-rules.md](review-approval-rules.md)) §8・§12、本 Task (Task 009-9) の Issue #76 および本 Task の PR |
| 回答により確定した事項 | 最初に解決対象として扱う上流 Open Issue の論点を、オーナーは特定の 1 件に限定せず、T1〜T9 のいずれからでも着手してよいとしたこと (初回着手論点の優先順位・限定は付与されない)。 |
| 回答後も未決の事項 | 実際にどの論点から着手するかの具体選択／着手する論点の具体的な解決内容／上流成果物へ記録する判断内容／残る論点の着手順序／各後続タスクの影響度 (Q5)／Q2 placeholder・実査待ちの確認方法／Q3 個別確認主体／Q4 再評価トリガー／provenance・参照切れの扱い／候補採否・改定要否・継続保留・改訂着手。いずれも本記録では決定・補完しない。 |

**Does Not Decide / Does Not Authorize**: 本記録は上流 Open Issue の内容を解決・close せず、選択されなかった論点を却下・不要・継続保留とせず、Design System の改定要否・候補採否・改訂着手・設計承認を決定・承認しない。最初に扱う論点の選択 (本件では「どれからでも構わない」) を、当該論点の内容に対する承認として扱わない。Task 009-6 の全 12 候補「現時点では開始できない」を変更しない。§7「解決単位＝論点別」を上書きしない。Q2〜Q5 への回答を補完しない。個別確認主体・担当者・期限・工数を推測しない。GitHub の approval・merge を設計承認と同一視しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §8 である (Wiki は非正本)。

---

## 9. Review / Approval Rules 改定の承認記録 (§8 編集的訂正 carve-out)

- 種別: **Review / Approval Rules ([review-approval-rules.md](review-approval-rules.md)) の改定 (§17 手順6「規則の変更」) に対する Web部責任者の承認記録**。上記 §1〜§8 とは独立した記録であり、混同しない。本記録は §5 設計承認ログで承認された規則本体への**改定**の承認であり、§5 の記録自体は変更しない (§5 は初回承認の記録として保持)。本記録は Design System の候補採否・改定要否・改訂着手といった**設計承認ではない**。
- 規約: 恒久 Decision ID・新しい正式 Status・Phase・Gate は採番・新設しない。取得した判断は原文の意味を変えずに記録する。GitHub の approval・merge を承認と同一視しない (§5・§6 と同じ)。

| 項目 | 内容 |
| --- | --- |
| 承認対象 | Review / Approval Rules §8 への改定: 編集的訂正の類型を影響度・低とする明文の carve-out の追加 |
| 承認内容 | 非文・誤字脱字・明白な文法／表記の誤りの訂正で、記述の意味・主張・意図を変えない字句修正を、影響度・低として扱う明文の例外を §8 に設ける。設計内容・設計判断・token・Component・version・プロセス判断に影響する変更、文の追加・削除や記述内容／整合の実質的変更、意味が変わりうる変更、該当するか迷う・境界的な場合は本例外の対象外とし、通常どおり Web部責任者が都度判定する (迷う場合は安全側で高)。Web部責任者は個別に高へ引き上げ可能。本例外はルール制定段階を含め規則適用中は有効。 |
| 承認日 | 2026-07-21 |
| 承認主体 | Web部責任者 |
| 本改定自体の影響度 | 高 (本件として明示取得、2026-07-21)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 既定の Web部責任者＋チーフデザイナー。 |
| 適用範囲 | Review / Approval Rules は Repository 横断規則 (§4) であり、本 carve-out も規則の適用範囲に従う。ただし本 carve-out は編集的訂正の類型に限定され、他の変更類型・一般的な高／低の内容基準・特定サービスの個別判断へ一般化しない。 |
| 根拠成果物 | [review-approval-rules.md](review-approval-rules.md) §8・§5 Out of Scope・§17・§21・§23 |
| 根拠 PR | 本改定 PR (Task 009-4-F1) |
| 契機 | PR [#81](https://github.com/tocoo/coocom-design-system/pull/81) (Task 009-10-F1) の非文訂正レベルの補正に対し、暫定運用「ルール制定段階はすべて高」により責任者＋チーフデザイナーの必須レビューを要したことが過剰であるとの Web部責任者の指摘。 |
| 位置づけ | §5 で承認された規則本体への改定 (§17 手順6) の承認であり、§5 初回承認・§6 適用開始・§7・§8 の各記録は変更しない。Design System の候補採否・改定要否・改訂着手・設計承認ではない。 |
| 残る Open Issue | 一般的な高／低の明文判定基準は引き続き未整備 ([review-approval-rules.md](review-approval-rules.md) §8・§21)。本 carve-out は編集的訂正の類型に限定した部分的明文化であり、一般基準を確定しない。 |

本承認は Review / Approval Rules §8 への編集的訂正 carve-out の追加の承認である。本承認および本 PR のマージは、改訂候補の採否・Design System 改定要否・改訂着手・Work Order 6 再評価・Design System 改定を意味しない。影響度・高／低の判定結果は Wiki (非正本) に記録する ([review-approval-rules.md](review-approval-rules.md) §8)。

---

## 10. Travel アイコン体系 (Font Awesome 6) の現在判断記録

- 種別: 国内宿泊 (travel) のアイコン体系について Web部責任者が示した **2026-07-27 時点の現在判断**の記録。上記 §1〜§9 とは独立した記録であり、混同しない。本記録は §1 Q8 の 3DS 横断論点を解決せず、`TVL-0006` の historical provenance も解決しない。§5 設計承認ログ・§6 適用開始記録・§7〜§9 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。取得した判断は原文の意味を変えずに記録する。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・description・note・Component 仕様を変更しない。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | 国内宿泊 (travel) のアイコン体系。Task 009-27 で調査した `TVL-0006` (Font Awesome 6) 関連の現行記録 (対象: [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §6、[../services/travel/design-system/components.md](../services/travel/design-system/components.md) ReviewStars、[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) `icon.reviewSize`) |
| 判断日 | 2026-07-27 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-07-27 時点)。過去判断の復元・追認・認定ではない |
| 取得した判断 ⓐ アイコン体系 | 国内宿泊の新規制作における標準アイコン体系は **Font Awesome 6** とする |
| 取得した判断 ⓑ 新規制作への適用 | 国内宿泊の新規制作では、原則として FA6 へ統一する。ただし package・style・weight・ライセンス・CDN／npm／kit 等の導入方式は本記録の判断に**含めない** |
| 取得した判断 ⓒ 既存 Material の扱い | 既存 Material アイコンは、対象ページまたは Component に**実際の改修が発生した際に** FA6 へ置換する。「改修時」とは、対象ページまたは Component に実際の改修が発生した機会を指す。次は意味しない: アイコン置換のみを目的とする一括改修／全対象箇所の洗い出し／置換順序・期限・完了条件の決定／未改修箇所での既存 Material 使用禁止 |
| 取得した判断 ⓓ ReviewStars | travel の ReviewStars では、FA6 の `star` を使用する現行方針を維持する。ただし solid／regular 等の style・weight・package・実装方式・実寸は本記録では決定しない |
| 取得した判断 ⓔ サイズ token | `icon.reviewSize` の現行 token 定義 (`$value = {iconSize.sm}`、現在の解決値 `16px`、`$status = bound`) を維持する。これは**論理 token の参照関係を維持する判断**であり、次は意味しない: `icon.reviewSize` が literal な `16px` を直接保持していること／ReviewStars の現行実装から `16px` を実測確認したこと／`components.md` ReviewStars の「星の実寸 (要実査)」が解消したこと |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・将来追加されるその他のサービス・3DS 横断の共通アイコン体系へは**自動適用しない** |
| §1 Q8 との関係 | §1 Q8 (アイコン体系 = Material / FA6 / 自社 / lucide) の **3DS 横断論点は未決のまま維持**する。travel = 2026-07-27 の現在判断を取得済み / rental-car・inbound を含む 3DS 横断統一 = 未決、という状態に分離する。Q8 を削除せず、「FA6 で解決済み」への単純な置き換えもしない |
| historical provenance | 次はいずれも **未確認のまま**: `TVL-0006` 導入前の判断成立経路／過去の判断主体・判断日／ADR 正本／historical provenance／2026-07-09・2026-07-13 時点で Owner 確認が行われたか。**commit 作成者・作成日、PR 作成者・merge 日を過去の判断主体・判断日として扱わない**。本記録の判断日 (2026-07-27)・判断主体 (Web部責任者) は現在判断のものであり、過去判断の認定ではない |
| 本記録工程の影響度 | **未取得**。本記録工程について影響度を明示的に判定・記録した直接証拠は Repository 内に存在しない。影響度の判定主体は Web部責任者の都度判断 ([review-approval-rules.md](review-approval-rules.md) §8)。必要レビュー主体は影響度判定前は未確定 (同 §10。高 = Web部責任者＋チーフデザイナー／低 = Web部レビュー担当者)。高／低の一般的な明文判定基準は未整備であり、推測・補完しない (同 §8・§21)。[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L.1 の影響度・低 は R-D 整理工程 (Task 009-19) についての記録であり、同節が「過去 Task の影響度や前工程からの自己導出ではない」、同 §8L.6 が「着手する工程の影響度 (Q5) を別途取得すること (本 Task の影響度ではない)」と定めているため、本記録工程へ適用しない。影響度が明示 (判定・記録) されていない変更を、レビュー済み・反映可能として扱わない (同規則 §8) |
| 根拠 | Task 009-27 の調査結果 (`TVL-0006` の全出現箇所・導入前後の差分・Owner 確認経路・§1 Q8 との併存状態)、[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L (R-D provenance トラック)、[review-approval-rules.md](review-approval-rules.md) §10・§13、Task 009-27R の Issue [#104](https://github.com/tocoo/coocom-design-system/issues/104) および本記録の PR |
| 判断により確定した事項 | travel について ⓐ〜ⓔ を 2026-07-27 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | 3DS 横断のアイコン体系統一 (§1 Q8)／FA6 の package・style・weight・ライセンス・導入方式／既存 Material の対象箇所・置換順序・期限・完了条件／ReviewStars の星の実寸 (要実査)／`TVL-0006` の ADR 正本・historical provenance。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は `TVL-0006` の過去判断・ADR 正本を発見・復元せず、2026-07-09・2026-07-13 の判断主体・判断日を認定せず、`TVL-0006` の historical provenance を解決しない。3DS 横断での FA6 統一を決定せず、rental-car・inbound の §1 Q8 を解決しない。FA6 の package・style・weight・ライセンス・導入方式を決定せず、既存 Material の一括置換・置換対象・順序・期限・完了条件を決定しない。ReviewStars の実寸を確定せず、`iconSize.sm` の `16px` を `TVL-0006` で新規決定したものとは扱わない。`color.icon.rating`・`TVL-0011` に関する記録を再判断しない。travel の token・値・`$status`・description・note・Component 仕様・ReviewStars のアイコン仕様を変更しない。新たな ADR が恒久的に不要であるとは確定しない。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §10 である (Wiki は非正本)。

---

## 11. Travel Modal 実装基盤 (drawer) の現在判断記録

- 種別: 国内宿泊 (travel) の Modal 実装基盤について Web部責任者が示した **2026-07-27 時点の現在判断**の記録。上記 §1〜§10 とは独立した記録であり、混同しない。本記録は §1 Q9 の 3DS 横断論点を解決せず、`TVL-0007` の historical provenance も解決しない。§5 設計承認ログ・§6 適用開始記録・§7〜§10 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。取得した判断は原文の意味を変えずに記録する。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・description・note・Component の実装要件を変更しない。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | 国内宿泊 (travel) の Modal 実装基盤。Task 009-28 で調査した `TVL-0007` (drawer 全面統一・centered dialog deprecated) 関連の現行記録 (対象: [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §7、[../services/travel/design-system/components.md](../services/travel/design-system/components.md) Modal / Overlay) |
| 判断日 | 2026-07-27 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-07-27 時点)。過去判断の復元・追認・認定ではない |
| 取得した判断 ⓐ 最終到達方針 | travel の Modal 実装基盤は、最終的に **drawer へ統一**する現行方針を維持する。これは最終到達方針であり、既存 centered dialog の即時廃止・一括置換を意味しない |
| 取得した判断 ⓑ 新規制作 | 新規 Modal は**原則 drawer で実装**し、**第3の Modal 実装基盤は導入しない**。具体的なライブラリ・モジュール・実装方式・DOM 構造は本記録では決定しない |
| 取得した判断 ⓒ 既存 centered dialog | deprecated として扱うが、**移行期間中の併存を認める**。対象ページまたは Component に**実際の改修が発生した際に** drawer への置換要否を確認する。次は意味しない: 置換のみを目的とする一括改修／全対象箇所の洗い出し／全既存の即時廃止／未改修箇所での使用禁止／移行順序・期限・完了条件の決定 |
| 取得した判断 ⓓ 「centered dialog」の対象 | travel に既存する**非 drawer 型 Modal を指す概念上の呼称**として扱う。実装上のどのモジュール・クラス・識別子に対応するかは Repository 内で確認できていない。**`M-02`・`_modal_prime` 等の具体的な実装実体との対応を本記録から認定しない** |
| 取得した判断 ⓔ 移行計画 | 移行対象・順序・期限・完了条件・具体的な移行ロードマップは**現時点では決定しない**。決定する場合は**外部実装 Repository の実査を先に行い**、現行実装・対象件数・例外・SP／PC 別挙動・アクセシビリティ要件を確認する必要がある (実査は別工程) |
| 取得した判断 ⓕ token・挙動 | `elevation.overlay`・`elevation.modal` およびその `$status = bound`、`motion.transition.*` の `$status = placeholder`、follow-up #3／`TVL-0008` との関係を**維持し変更しない**。open／close 遷移・focus・scroll lock・backdrop・dismiss 等の具体挙動は本記録では決定しない |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・将来追加されるその他のサービス・3DS 横断の共通 Modal 実装基盤へは**自動適用しない** |
| §1 Q9 との関係 | §1 Q9 (モーダル実装基盤) の **3DS 横断論点は未決のまま維持**する。travel = 2026-07-27 の現在判断を取得済み／rental-car・inbound を含む 3DS 横断統一 = 未決、という状態に分離する。Q9 を削除せず、「drawer で解決済み」への単純な置き換えもしない。**Q9 を `TVL-0007` の過去の選定・承認記録として扱わない**。本記録後も次の4つを分離して維持する: ①travel の最終到達方針 = drawer へ統一 ②travel の移行中状態 = 新規は原則 drawer・既存 centered dialog は当面併存 ③3DS 横断 Q9 = 未決 ④`TVL-0007` の historical provenance = 未確認 |
| historical provenance | 次はいずれも **未確認のまま**: `TVL-0007` 導入前の判断成立経路／過去の判断主体・判断日／ADR・Decision 正本／historical provenance／過去に Owner 確認が行われたか／導入時点に存在した移行ロードマップ／過去に決定された移行対象・順序・期限・完了条件。**commit 作成者・作成日、PR 作成者・merge 日を過去の判断主体・判断日として扱わない**。本記録の判断日 (2026-07-27)・判断主体 (Web部責任者) は現在判断のものであり、過去判断の認定ではない。また判断日 (2026-07-27) と Repository への反映日 (2026-07-28) は別の事象である |
| 本記録工程の影響度 | **高** (判定者 = Web部責任者、判定日 = 2026-07-28、**本件について明示取得**)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定である **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11)。判定理由 (Web部責任者): Governance 正本へ現在判断を新設する／3DS 横断論点である §1 Q9 へ注記する／Design System 成果物 `design.md`・`components.md` の規範的な表現を補正する／不在の `TVL-0007` へ委任している参照を解消する／仕様そのものは変更しないが、仕様の根拠・確定範囲・未決状態の読み取りに影響する。過去 Task の影響度や前工程からの自己導出ではない (高／低の一般的な明文判定基準は未整備であり推測・補完しない。同 §8・§21)。同 §8 の編集的訂正 carve-out は、文の追加・記述内容の実質的変更を含むため本工程に適用しない |
| 根拠 | Task 009-28 の調査結果 (`TVL-0007` の全出現箇所・全 149 commit の走査による定義見出しの不在・導入前後の差分・§1 Q9 との併存状態・rental-car / inbound との記述差)、[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L (R-D provenance トラック)、[review-approval-rules.md](review-approval-rules.md) §10・§13、Task 009-28R の Issue [#106](https://github.com/tocoo/coocom-design-system/issues/106) および本記録の PR |
| 判断により確定した事項 | travel について ⓐ〜ⓕ を 2026-07-27 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | 3DS 横断の Modal 実装基盤統一 (§1 Q9)／具体的なライブラリ・モジュール・実装方式・DOM 構造／既存 centered dialog の対象箇所・移行順序・期限・完了条件・移行ロードマップ／「centered dialog」と実装実体の対応／`motion.transition.*` の実値 (follow-up #3・`TVL-0008`)／`TVL-0007` の ADR 正本・historical provenance。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は `TVL-0007` の過去判断・ADR 正本を発見・復元せず、過去の判断主体・判断日を認定せず、`TVL-0007` の historical provenance を解決しない。3DS 横断での drawer 統一を決定せず、rental-car・inbound の §1 Q9 を解決しない。既存 centered dialog の廃止判断・即時廃止・一括置換を行わず、移行対象・順序・期限・完了条件を決定せず、移行ロードマップを制定しない。「centered dialog」と `M-02`・`_modal_prime` 等の実装実体との対応を認定しない。新たな Modal 実装基盤を選定せず、Modal の具体的なライブラリ・モジュール・DOM 構造・open／close・focus・scroll lock・backdrop・dismiss 等の挙動を決定しない。travel の token・値・`$status`・description・note・Component の実装要件・version・正式 Status を変更しない。[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L の R-D 分類を変更しない。新たな ADR が恒久的に不要であるとは確定しない。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §11 である (Wiki は非正本)。

---

## 12. Travel 配布物 (バンドル・スナップショット) の生成・管理責務と版の対応付けの現在判断記録

- 種別: 国内宿泊 (travel) の Design System 配布物 (バンドル・スナップショット) の生成・管理責務と、配布スナップショットが SOT のどの版に対応するかの対応付けについて Web部責任者が示した **2026-08-03 時点の現在判断**の記録。上記 §1〜§11 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§11 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。取得した判断は原文の意味を変えずに記録する。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$description`・`$note`・`$meta.version` を変更しない。**判断日 (2026-08-03) と本 Repository 反映日 (2026-08-03) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の Design System 配布物 (バンドル・スナップショット) の生成・管理責務の所在、および配布スナップショットが SOT のどの版に対応するかの対応付け方法。契機は依頼元 (ウルトラトクー市 一覧ページ 画面設計・2026-08-03 起票) の依頼 A「バインド DS スナップショットの同期」(Task 009-37・Issue [#115](https://github.com/tocoo/coocom-design-system/issues/115)) |
| 判断日 | 2026-08-03 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-03 時点)。過去の生成手順・生成主体の復元・追認ではない |
| 取得した判断 ⓐ 生成・管理責務の所在 | 配布物 (バンドル・スナップショット) の生成・管理責務 — SOT の `semantic.travel.json` / `primitive.travel.json` からバンドルを生成し配布スナップショットを更新する責務 — は **実装リポジトリ側 (`tocoo/tocoo_travel`)** に置く。具体的な生成器・生成手順・更新契機の運用手順そのものは本記録では確定しない (実装リポジトリ側の作業) |
| 取得した判断 ⓑ 版の対応付け方法 | 配布スナップショットは SOT の **`semantic.travel.json` (および `primitive.travel.json`) の `$meta.version`** に対応付ける。ただし `$meta.version` の付与規則 (version bump の条件) 自体は本 Repository 内で未決の Open Issue であり ([../services/travel/design-system/README.md](../services/travel/design-system/README.md) §13・§16)、本記録はその付与規則を確定しない |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定である **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11)。判定理由 (Web部責任者): Governance 正本 (owner-decisions.md) へ現在判断を新設する。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は文の追加を含むため本工程に適用しない |
| 根拠 | 依頼元の依頼 A (2026-08-03)、Task 009-37 の Issue [#115](https://github.com/tocoo/coocom-design-system/issues/115)、`semantic.travel.json` / `primitive.travel.json` / [baseline-assessment.md](../services/travel/design-system/baseline-assessment.md) の実測、[review-approval-rules.md](review-approval-rules.md) §14、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (生成・管理責務 = 実装リポジトリ側 `tocoo/tocoo_travel`) と ⓑ (版の対応付け = `$meta.version` 基準) を 2026-08-03 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | `$meta.version` の付与規則 (version bump の条件・README §13/§16)／具体的な生成器・生成手順・更新契機の運用手順／配布スナップショット `fe4b9e52` と commit / version の対応／バンドル再生成の実施そのもの。いずれも本記録では決定・補完しない |

### 配布スナップショットと SOT の乖離 (本記録時点の Fact・`main` `cbc19c6`)

- SOT の `semantic.travel.json` の leaf token (`$value` を持つ行) は **77 件**、`primitive.travel.json` は **97 件** (実測)。[baseline-assessment.md](../services/travel/design-system/baseline-assessment.md) が 2026-07-16 時点で記録した「semantic 63 件・primitive 97 件」に対し、**semantic のみ +14 件**、primitive は増減なし。依頼元が観測したスナップショット (semantic 63 トークン構成) はこの 2026-07-16 時点の構成と一致する。
- 未収録の semantic **14 件**の確定リスト (トークン名・`$value`・`$status`・追加 Task。`semantic.travel.json` の実測と一致)。

| # | トークン | `$value` | `$status` | 追加 Task |
| --- | --- | --- | --- | --- |
| 1 | `color.text.mutedStrong` | `{color.palette.gray.700}` | bound | Task 009-33 |
| 2 | `color.text.onAccent` | `{color.palette.white}` | bound | Task 009-34 |
| 3 | `color.text.inverseMuted` | `{color.palette.gray.600}` | bound | Task 009-34 |
| 4 | `radius.badge` | `{radius.sm}` | **placeholder** | Task 009-34 |
| 5 | `font.heading.weight` | `{typography.fontWeight.bold}` | bound | Task 009-35 |
| 6 | `font.heading.lineHeight` | `{typography.lineHeight.tight}` | bound | Task 009-35 |
| 7 | `font.heading.h1Size` | `{typography.size.4xl}` | bound | Task 009-35 |
| 8 | `font.heading.h3Size` | `{typography.size.2xl}` | bound | Task 009-35 |
| 9 | `font.heading.h4Size` | `{typography.size.xl}` | bound | Task 009-35 |
| 10 | `font.heading.h5Size` | `{typography.size.lg}` | bound | Task 009-35 |
| 11 | `font.heading.h6Size` | `{typography.size.md}` | bound | Task 009-35 |
| 12 | `color.text.linkHover` | `{color.scheme.main.hover}` | bound | Task 009-35 |
| 13 | `color.text.linkActive` | `{color.scheme.main.pressed}` | bound | Task 009-35 |
| 14 | `color.text.placeholder` | `{color.palette.gray.700}` | bound | Task 009-35 |

- 依頼書が挙げた 4 件 (`color.text.mutedStrong` / `color.text.onAccent` / `color.text.linkHover` / `radius.badge`) は上記 14 件の部分集合である。依頼書の表に無い 10 件も同じく未収録である。
- 配布スナップショット ID `fe4b9e52` は本 Repository の Git object として解決できない (`git cat-file -t fe4b9e52` = `Not a valid object name`)。スナップショットがどの commit / version に対応するかを本 Repository 内で確認する方法は現時点で存在しない。この点が ⓑ の版の対応付け方法を決める背景である。
- `radius.badge` は `$status: placeholder` である (14 件中唯一)。[design.md](../services/travel/design-system/design.md) §9 (Agent Prompt Guide) 手順 3 は placeholder トークンについて「`$note` を確認し、生成物にも『🚧 暫定』を伝播させる」と定める。配布に含める場合この規則が及ぶ (`radius.badge` の `placeholder` → `bound` 昇格は本記録では行わない)。

**Does Not Decide / Does Not Authorize**: 本記録はバンドルの再生成そのものを実施せず、生成器・生成手順・更新契機の運用手順を確定しない。成果物側の暫定 materialize の削除を行わない。token の値・参照先・`$status`・`$meta.version`・正式 Status を変更しない。`radius.badge` の `placeholder` → `bound` 昇格を行わない。`$meta.version` の付与規則 (version bump の条件) を確定しない。配布スナップショット `fe4b9e52` と commit / version の対応を認定しない。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §12 である (Wiki は非正本)。

---

## 13. Travel バッジ面色・文字色の現在判断記録

- 種別: 国内宿泊 (travel) の小サイズバッジの面色 (依頼 B) と、逆色を面として使う場合の文字色 (依頼 C) について Web部責任者が示した **2026-08-03 時点の現在判断**の記録。上記 §1〜§12 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§12 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。取得した判断は原文の意味を変えずに記録する。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$description`・`$meta.version` を変更しない (面用途は既存 `color.scheme.*.inverse` を参照)。**判断日 (2026-08-03) と本 Repository 反映日 (2026-08-03) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の `Card.slot.badge` (割引率ラベル・状態バッジ等) の面色と文字色。依頼元 (ウルトラトクー市 一覧ページ 画面設計・2026-08-03 起票) の依頼 B「小サイズのバッジに使える面色と文字色」および依頼 C「逆色 `#C8912C` を面として使う場合の文字色」(Task 009-38・Issue [#116](https://github.com/tocoo/coocom-design-system/issues/116))。対象記述 = [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §2.1・[../services/travel/design-system/components.md](../services/travel/design-system/components.md) `Card.slot.badge` |
| 判断日 | 2026-08-03 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-03 時点) |
| 取得した判断 ⓐ 依頼 B (小サイズバッジの面色) | 選択肢 **b2** = accent 淡色 primitive を新設し「淡色面 + 濃色文字」を semantic に追加する方向を採る。ただし accent 淡色段 (50/100 相当・現行 palette に不在) の**実色値は本記録では未取得**であり、新規 primitive・semantic の実追加は実色値取得後の別作業とする。取得後に「淡色面 + `color.text.strong` の 4.5:1 以上」を検証して確定する。取得までは現行の代替規則が有効で、12px のバッジは既定 (neutral dark 面 `color.surface.inverse` + `color.text.inverse`) を用い campaign accent を面として使用しない |
| 取得した判断 ⓑ 依頼 C (逆色面の文字色) | 選択肢 **c1** = `color.scheme.*.inverse` の面用途を割引ラベル背景へ拡張し、文字色を `color.text.strong` に固定する。コントラスト = main `#C8912C` 上 5.78:1・sub `#C8B12C` 上 7.50:1 (design.md §2.1 の表と一致)。白文字は使用しない (main 2.78:1・sub 2.15:1 で通常・大きなテキストのいずれも未達)。逆色の値は評価色 (`color.icon.rating` = 文字/アイコン色) と割引ラベル背景 (面 + `color.text.strong`) の 2 用途に用いるが用途は分離し、`color.icon.rating` トークンを面へ流用しない。面用途に専用 semantic 用途トークンは追加せず `color.scheme.*.inverse` を面として参照する (新規トークンなし) |
| 取得した判断 ⓒ 依頼元が根拠とする 2026-07-31 の Owner 決定の扱い | 依頼元は「Owner 決定 (2026-07-31) により accent を採用」「Owner 例外承認」を根拠として挙げるが、`2026-07-30` / `2026-07-31` / `2026-08-` を含む記述は**本記録着手時点 (`main` `cbc19c6`) の本 Repository 全体で 0 件**であり、当該 Owner 決定は本 Repository 内に記録が無かった (本記録の追加後は本記録自身が `2026-08-` を含むため、計測時点を `cbc19c6` に固定する)。この事実を提示したうえで、Web部責任者は本記録 (2026-08-03 の現在判断 = ⓐ b2・ⓑ c1) をもって accent を面/点として用いる方向を**現在判断として記録**することを判断した。**過去 (2026-07-31) の判断主体・判断日は認定せず、本記録は現在判断として扱う** (§10/§11 と同じ区別)。commit 作成者・作成日・PR 作成者・merge 日を過去の判断主体・判断日として扱わない |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定である **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11)。判定理由 (Web部責任者): design.md §2.1 の規範規則 (`color.scheme.*.inverse` の面用途の未定義→定義・文字色の固定) を変更し、Governance 正本へ現在判断を新設する。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は文の追加・規範規則の変更を含むため本工程に適用しない |
| 根拠 | 依頼元の依頼 B / C (2026-08-03)、Task 009-38 の Issue [#116](https://github.com/tocoo/coocom-design-system/issues/116)、design.md §2.1 の検証済みコントラスト比 (main 5.78:1・sub 7.50:1)、`semantic.travel.json` の実測、[review-approval-rules.md](review-approval-rules.md) §10、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (依頼 B = b2・実色値取得待ち) ⓑ (依頼 C = c1・面用途を割引ラベル背景へ拡張・`color.text.strong` 固定) を 2026-08-03 時点の現在判断として記録し、ⓒ 2026-07-31 の Owner 決定が本 Repository 内に記録が無かった事実を提示したうえで本記録を現在判断として扱うこと |
| 判断後も未決・未確認の事項 | b2 の accent 淡色段の実色値・新規 primitive/semantic の実追加／2026-07-31 の historical provenance (過去の判断主体・判断日・ADR 正本)／`Card.slot.badge` の実 px (`radius.badge` の実査待ち)。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は accent 淡色段の実色値を確定せず、新規 primitive・semantic を追加しない (b2 の実追加は実色値取得後の別作業)。2026-07-31 の過去判断・ADR 正本を発見・復元せず、過去の判断主体・判断日を認定しない。既存 token の値・参照先・`$status`・`$meta.version`・正式 Status を変更しない (面用途は既存 `color.scheme.*.inverse` を参照)。`radius.badge` の `placeholder` → `bound` 昇格を行わない。適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (コントラスト比は概算の記録)。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §13 である (Wiki は非正本)。

---

## 14. Travel placeholder / 実査待ちの確認方法・個別確認主体の現在判断記録

- 種別: 国内宿泊 (travel) の placeholder / 実査待ちトークンの**確認方法**と**個別項目の確認主体**について Web部責任者が示した **2026-08-03 時点の現在判断**の記録。[review-approval-rules.md](review-approval-rules.md) §14 は「確認方法を決める主体 = Web部責任者／個別項目の確認主体 = 確認ルールが制定されるまで未定」と定め、Web部責任者が確認方法および個別項目の確認主体を明示しその記録が Repository 内に存在するまで placeholder・実査待ちの項目を解決済みとして扱わないとしている (同 §14・§21)。本記録はその明示・記録に対応する。上記 §1〜§13 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§13 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。承認済み・適用中の規則 [review-approval-rules.md](review-approval-rules.md) 本体は改定せず、規則が Web部責任者に委ねた決定の記録を本ファイルに置く。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$note`・`$meta.version` を変更しない。**判断日 (2026-08-03) と本 Repository 反映日 (2026-08-03) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の placeholder / 実査待ちトークンの確認方法と個別確認主体。契機は依頼元 (ウルトラトクー市 一覧ページ 画面設計・2026-08-03 起票) の依頼 F「placeholder の解決」(Task 009-41・Issue [#119](https://github.com/tocoo/coocom-design-system/issues/119))。[review-approval-rules.md](review-approval-rules.md) §14 が求める「確認方法」と「個別項目の確認主体」 |
| 判断日 | 2026-08-03 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-03 時点) |
| 取得した判断 ⓐ 確認方法 | placeholder / 実査待ちトークンの実値は、**依頼元 (画面設計) が提出する値を受領して確定する**。実装実測ではなく設計側の提出値を正とする |
| 取得した判断 ⓑ 個別確認主体 | **作業担当者 (改訂作業の実施者) が提出値を SOT の placeholder と照合し、Web部責任者が確認する**。[review-approval-rules.md](review-approval-rules.md) §14 が「確認ルールが制定されるまで未定」としていた個別項目の確認主体を本記録で定義する |
| 記録先 | 本 owner-decisions.md §14。承認済み・適用中の規則 [review-approval-rules.md](review-approval-rules.md) §14 本体は改定しない (規則が Web部責任者に委ねた決定の記録を本ファイルに置く) |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **低** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定である **Web部レビュー担当者**。判定理由 (Web部責任者): placeholder の列挙・追跡先の整理と確認方法/主体の記録であり、token の値・`$status`・`$meta.version` の変更を伴わない。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21) |
| 根拠 | 依頼元の依頼 F (2026-08-03)、Task 009-41 の Issue [#119](https://github.com/tocoo/coocom-design-system/issues/119)、`semantic.travel.json` / `primitive.travel.json` の実測 (placeholder 11 件)、[review-approval-rules.md](review-approval-rules.md) §14・§21、[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L (R-D トラック)、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (確認方法 = 依頼元提出値の受領) ⓑ (個別確認主体 = 作業担当者照合 + Web部責任者確認) を 2026-08-03 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | 実査 (提出値の受領) そのもの／placeholder の bound 昇格・暫定値の確定／follow-up #3 が §3 に追跡行を持たない不足の解消 (R-D §8L の別論点)／follow-up 番号体系の正本整備。いずれも本記録では決定・補完しない |

### placeholder 11 件の確定リスト (本記録時点・`main` `cbc19c6`)

`$status: placeholder` の実測は semantic 4 件・primitive 7 件・計 **11 件**。追跡先を **follow-up #13 / follow-up #3 / follow-up 番号なし** の 3 区分で分離する (一括で同一区分として扱わない)。

| ファイル | トークン | `$value` | 追跡先区分 |
| --- | --- | --- | --- |
| semantic | `radius.card` | `{radius.md}` | follow-up 番号なし (TVL-0008・design.md §5 の実査待ち区分) |
| semantic | `radius.badge` | `{radius.sm}` | follow-up 番号なし (実確定は `radius.card` と同じ実査待ち区分) |
| semantic | `motion.transition.duration` | `{motion.duration.base}` | follow-up #3 |
| semantic | `motion.transition.easing` | `{motion.easing.standard}` | follow-up #3 |
| primitive | `shadow.sm` | `0 1px 2px rgba(0,0,0,0.05)` | follow-up #13 |
| primitive | `shadow.md` | `0 2px 8px rgba(0,0,0,0.10)` | follow-up #13 |
| primitive | `shadow.lg` | `0 8px 24px rgba(0,0,0,0.15)` | follow-up #13 |
| primitive | `motion.duration.fast` | `150ms` | follow-up #3 |
| primitive | `motion.duration.base` | `300ms` | follow-up #3 |
| primitive | `motion.duration.slow` | `500ms` | follow-up #3 |
| primitive | `motion.easing.standard` | `ease` | follow-up #3 |

- 追跡先の状態は follow-up 番号ごとに異なる: **follow-up #13** (shadow 実値) は本 §3 に追跡行を持つ (`| #13 | shadow 実値 | 暫定3段で据置き |`)。**follow-up #3** (motion 実値) は §3 に記載が無く、この不足は [../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L (Task 009-19・R-D トラック) が既に記録している。**radius.card / radius.badge** は follow-up 番号を持たず TVL-0008 および design.md §5 の実査待ち区分である。本記録は follow-up #3 の §3 追跡行の不足を新たに解消せず、R-D トラック (§8L) の既存記録との対応関係のみ整理する。
- 依頼書は「計 10 件」としていたが、これは `radius.badge` (Task 009-34 で追加) が反映される前の件数であり、本記録時点の実測は **11 件**である。
- 本 §14 の確認方法・確認主体は placeholder 全般 (11 件) へ及ぶ。実査 (提出値の受領) は未実施であり、11 件はいずれも placeholder を維持する (bound 昇格・暫定値の確定は行わない)。

**Does Not Decide / Does Not Authorize**: 本記録は実査 (提出値の受領) そのものを実施せず、placeholder の `bound` 昇格・暫定値 (`radius.card` = md 8px・`shadow.*` 3 段・`motion.*`) の確定を行わない。follow-up #3 が §3 に追跡行を持たない不足を本記録で解消せず (R-D §8L の別論点)、follow-up 番号体系の正本整備も行わない。承認済み・適用中の規則 [review-approval-rules.md](review-approval-rules.md) 本体を改定しない。token の値・参照先・`$status`・`$note`・`$meta.version`・正式 Status を変更しない。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §14 である (Wiki は非正本)。

---

## 15. Travel 依頼 D 新規 Component 定義工程への着手可否の現在判断記録

- 種別: 国内宿泊 (travel) の依頼 D で受理した新規 Component (Pagination / Badge 単体 / Stepper / Empty state) の**定義工程への着手可否**について Web部責任者が示した **2026-08-03 時点の現在判断**の記録。上記 §1〜§14 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§14 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断と同一視しない。本記録は Component 仕様・variant 語彙・状態固定リスト・token を新設・変更しない。**判断日 (2026-08-03) と本 Repository 反映日 (2026-08-03) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | 依頼元 (ウルトラトクー市 一覧ページ 画面設計・2026-08-03 起票) の依頼 D で受理した新規 Component (Pagination / Badge 単体 / Stepper / Empty state) の定義工程への着手可否 (Task 009-39・Issue [#117](https://github.com/tocoo/coocom-design-system/issues/117)。受理・分類は Task 009-39 で実施し、仕様定義は別 Task)。依頼 D-6 (ボトムシート / ポップオーバー) は #114 (Task 009-36) の範囲であり本記録の対象外 |
| 判断日 | 2026-08-03 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-03 時点) |
| 取得した判断 | 依頼 D の新規 Component の**定義工程への着手を可とする**。ただし着手可は改訂着手の可否 ([review-approval-rules.md](review-approval-rules.md) §9 = Web部の責任者) のみであり、Component 仕様・variant 語彙 (GOV-0002)・状態固定リスト (命名規則§2)・token の新設ではない。仕様定義は実体データ・実装実査を伴う別 Task で扱う |
| 12 候補との関係 | 依頼 D の新規 Component は、Work Order 6 ([../services/travel/design-system/alignment-amendment-readiness-assessment.md](../services/travel/design-system/alignment-amendment-readiness-assessment.md)) が扱う 12 候補 (既存の alignment 候補側面) とは別である。Work Order 6 の総合判断「全 12 候補は現時点では開始できない」は本記録により変更しない |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **低** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定である **Web部レビュー担当者**。判定理由 (Web部責任者): 新規 Component の受理・分類と着手可否の記録であり、Component 仕様・token・variant 語彙・状態固定リストの新設を伴わない。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21) |
| 根拠 | 依頼元の依頼 D (2026-08-03)、Task 009-39 の Issue [#117](https://github.com/tocoo/coocom-design-system/issues/117)、[../services/travel/design-system/components.md](../services/travel/design-system/components.md) 共通事項 / [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §7 の未着手 Component 一覧、[review-approval-rules.md](review-approval-rules.md) §9・§10、本記録の PR |
| 判断により確定した事項 | 依頼 D の新規 Component の定義工程への着手を可としたこと (改訂着手の可否のみ) |
| 判断後も未決・未確認の事項 | 各新規 Component の仕様・variant・状態・実体データ・実装実査・着手順序・優先度。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は新規 Component の仕様・variant 語彙・状態固定リスト・token を新設・変更しない。着手順序・優先度を決定しない (依頼元の優先順位 §7 を DS 側の着手順序として自動採用しない)。Work Order 6 の 12 候補「現時点では開始できない」を変更しない。既存 token の値・`$status`・`$meta.version` を変更しない。Design System の候補採否・改定要否・(12 候補の) 改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §15 である (Wiki は非正本)。

---

## 16. Travel 依頼 E 規定不足 (省略規則・表記規則の管理正本・繰り返し内 CTA) の現在判断記録

- 種別: 国内宿泊 (travel) の依頼 E「規定の不足」のうち Owner 判断を要した 3 件 (E-3 施設名の省略規則・E-4 コンテンツ表記規則の管理正本・E-5 繰り返し要素内の CTA) について Web部責任者が示した **2026-08-03 時点の現在判断**の記録。上記 §1〜§15 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§15 の各記録は変更しない。E-1 (画像面の scrim) と E-2 (会員限定マスク) は Owner 判断を要さず design.md 未確定事項の一覧へ新規起票した (本記録の対象外)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。**判断日 (2026-08-03) と本 Repository 反映日 (2026-08-03) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | 依頼元 (ウルトラトクー市 一覧ページ 画面設計・2026-08-03 起票) の依頼 E「規定の不足」のうち Owner 判断を要した 3 件 (Task 009-40・Issue [#118](https://github.com/tocoo/coocom-design-system/issues/118)): E-3 施設名の省略規則／E-4 コンテンツ表記規則の管理正本／E-5 繰り返し要素内の CTA |
| 判断日 | 2026-08-03 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-03 時点) |
| 取得した判断 ⓐ E-3 (施設名の省略規則) | 施設名の省略規則 (行数制限・truncation / ellipsis / line-clamp 等) は [../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8J (Task 009-17) が **UI・Implementation 下流課題**へ分類済みであり、この**分類を維持する** (DS 層で省略規則を定めない)。依頼と既存分類の抵触について DS 側で分類を変更しない |
| 取得した判断 ⓑ E-4 (コンテンツ表記規則の管理正本) | 割引率等のコンテンツ表記規則 (価格の単位表記の文言規則を含む) の管理正本は、**独立した文書 (`brand-content.md` 等) を新設する方向を確定する**。実際の文書作成・中身・文書体系上の位置づけ・管理責務・既存正本との関係は別 Task であり、推測で新規正本を作成しない (README.md §16 の Open Issue)。価格の単位表記 (依頼 E-4 の (iii)) は §8.1 の対象外であり design.md 未確定事項へ新規起票した |
| 取得した判断 ⓒ E-5 (繰り返し要素内の CTA) | [../services/travel/design-system/components.md](../services/travel/design-system/components.md) Button の Do「1 画面の主 CTA は `primary` 1 つに絞る」を**撤回**し、**主 CTA の個数制約を撤廃する**。CTA の優先度は `primary` / `secondary` / `ghost` / `text` の強弱階層で表現し、繰り返し要素 (検索結果カード等) 内で各項目が `primary` を持つことを妨げない。これは Component の規範規則の変更である |
| 依頼元の 2026-07-3x Owner 例外承認の扱い | 依頼元は E-5 について「Owner 例外承認」を根拠として挙げるが、`2026-07-30` / `2026-07-31` / `2026-08-` を含む記述は**本記録着手時点 (`main` `cbc19c6`) の本 Repository 全体で 0 件**であり、当該例外承認は本 Repository 内に記録が無かった (本記録の追加後は本記録自身が `2026-08-` を含むため、計測時点を `cbc19c6` に固定する)。本記録は過去の例外承認を認定せず、E-5 を現在判断 (Do の撤回・個数制約の撤廃) として扱う |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定である **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11)。判定理由 (Web部責任者): E-5 は components.md Button の規範規則 (Do) を撤回・変更し、Governance 正本へ現在判断を新設する。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は規範規則の変更を含むため本工程に適用しない |
| 根拠 | 依頼元の依頼 E (2026-08-03)、Task 009-40 の Issue [#118](https://github.com/tocoo/coocom-design-system/issues/118)、[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8J (E-3)、design.md §8.1・`../service-design/content-principles.md` §10 (E-4)、components.md Button (E-5)、[review-approval-rules.md](review-approval-rules.md) §10、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (E-3 = §8J 分類維持・DS 層で定めない) ⓑ (E-4 = 独立文書新設の方向・作成は別 Task) ⓒ (E-5 = Button Do の撤回・主 CTA 個数制約の撤廃) を 2026-08-03 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | E-1 (画像面の scrim)・E-2 (会員限定マスク) の構成／E-4 の独立文書の作成・中身・管理責務／E-3 の下流課題 (UI・Implementation) 側での実際の省略規則／2026-07-3x の historical provenance。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は §8J の UI・Implementation 下流課題分類を変更しない (E-3)。`brand-content.md` を新規作成せず、コンテンツ表記規則の中身・管理責務を確定しない (E-4)。E-1 (画像面の scrim)・E-2 (会員限定マスク) の構成を確定しない (未確定事項として起票のみ)。2026-07-3x の過去の例外承認を認定しない。依頼元の暫定実装 (`color-mix` による scrim・独自文言・鍵アイコン等) を DS の規則として追認しない。既存 token の値・`$status`・`$meta.version` を変更しない。variant 語彙 (GOV-0002)・状態固定リストを新設しない。Design System の候補採否・改定要否・(12 候補の) 改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §16 である (Wiki は非正本)。

---

## 17. Travel Modal 表示形態 (form) における popover の位置づけの現在判断記録

- 種別: 国内宿泊 (travel) の Modal に表示形態 (form) 軸 (drawer / sheet / popover) を定義するにあたり、`popover` が §11 判断ⓑ の「第3の Modal 実装基盤」に当たるかについて Web部責任者が示した **2026-08-03 時点の現在判断**の記録。上記 §1〜§16 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§16 の各記録は変更しない。本記録は §11 (Modal 実装基盤 = drawer) を上書きせず、その判断ⓑ の解釈を明確化する。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。**判断日 (2026-08-03) と本 Repository 反映日 (2026-08-03) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の Modal の表示形態 (form) 軸 (drawer / sheet / popover) における `popover` の位置づけ。契機は依頼元 (ウルトラトクー市 一覧ページ 画面設計・2026-07-29 受領) の DS 変更依頼「ボトムシートとアンカー付きポップオーバーの定義追加」(依頼 D-6・Task 009-36・Issue [#114](https://github.com/tocoo/coocom-design-system/issues/114))。[review-approval-rules.md](review-approval-rules.md) は参照せず、§11 判断ⓑ「第3の Modal 実装基盤は導入しない」との関係を判断対象とする |
| 判断日 | 2026-08-03 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-03 時点) |
| 取得した判断 | `popover` は §11 判断ⓑ の「第3の Modal 実装基盤」に**当たらない**。`popover` は overlay の z 軸・backdrop・dismiss を `drawer` / `sheet` と共有する**同一基盤上の表示形態**である。配置方式 (基準要素への相対配置) が `drawer` / `sheet` と異なることは、実装基盤の相違としない。したがって form 軸に `drawer` (既定) / `sheet` / `popover` の 3 値を定義してよい (実装基盤は drawer 単一を維持し第3の実装基盤を導入しない = §11 ⓑ を維持) |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定である **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11)。判定理由 (Web部責任者): Governance 正本へ現在判断を新設し、design.md §7.1・components.md Modal の規範記述を拡張し新規 semantic / primitive トークン (radius.overlay・color.overlay.backdrop・color.palette.blackAlpha.45) を追加する (Task 009-36)。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は規範記述の拡張・トークン追加を含むため本工程に適用しない |
| 根拠 | 依頼元の依頼 D-6 (2026-07-29 受領・2026-08-03 依頼群として再整理)、Task 009-36 の Issue [#114](https://github.com/tocoo/coocom-design-system/issues/114)、本 §11 (Modal 実装基盤 = drawer・判断ⓑ)、[../services/travel/design-system/design.md](../services/travel/design-system/design.md) §7.1、[review-approval-rules.md](review-approval-rules.md) §10、本記録の PR |
| 判断により確定した事項 | `popover` が §11 ⓑ の「第3の Modal 実装基盤」に当たらず、form 軸に `drawer` / `sheet` / `popover` の 3 値を定義してよいこと (実装基盤は drawer 単一を維持) |
| 判断後も未決・未確認の事項 | 「実装基盤」の一般的定義 (Repository 内に未整備)／`popover` / `sheet` の a11y・`sheet` 最大高・`popover` 幅段階・実装 API 名 (prop 名)／`TVL-0007` の historical provenance。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は §11 (Modal 実装基盤 = drawer・判断ⓐ〜ⓕ) を上書き・変更しない。「実装基盤」の一般的定義を確定しない。`popover` / `sheet` の a11y (role / aria-modal / フォーカストラップ / スクロールロック等)・実装方式・DOM 構造・`sheet` 最大高・`popover` 幅段階・実装 API 名を決定しない。既存 token の値・`$status` を変更しない (`radius.overlay` / `color.overlay.backdrop` / `color.palette.blackAlpha.45` は placeholder で追加)。`TVL-0007` の historical provenance を解決しない。Design System の候補採否・改定要否・(12 候補の) 改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §17 である (Wiki は非正本)。

---

## 18. Travel セクション間余白の規定不足 (36px 段 spacing.9・位置用途トークン・44px 段・暫定 primitive 直参照) の受理と分類の現在判断記録

- 種別: 国内宿泊 (travel) のスペーシング系の規定不足について Web部責任者が示した **2026-08-04 時点の現在判断**の記録。契機は依頼元 (ToCoo! 国内宿泊トップページ 画面設計・2026-08-04 起票・DS-REQUEST「セクション間余白の規定と 36px 段」) の依頼 (Task 009-42・Issue [#127](https://github.com/tocoo/coocom-design-system/issues/127))。上記 §1〜§17 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§17 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$description`・`$meta.version` を変更しない (`spacing.9`・位置用途 semantic トークンの実追加は本記録では行わない)。**判断日 (2026-08-04) と本 Repository 反映日 (2026-08-04) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel のセクション間・ブロック間の余白と 36px 相当段。依頼元 (2026-08-04 起票) の DS-REQUEST「セクション間余白の規定と 36px 段」(Task 009-42・Issue [#127](https://github.com/tocoo/coocom-design-system/issues/127))。対象記述 = [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §4・[../services/travel/design-system/primitive.travel.json](../services/travel/design-system/primitive.travel.json) の `spacing` スケール・[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) (位置用途トークン不在) |
| 判断日 | 2026-08-04 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-04 時点) |
| 取得した判断 ⓐ 36px 段 (spacing.9) | primitive `spacing` スケールに `9` = `2.25rem` (36px) を**追加する方向を確定**する。36 = 4×9 で 4px 系 (TVL-0002) と整合し、位置は既存 `8` (32px = 2rem) と `10` (40px = 2.5rem) の間、`$status` の初期値は **bound** (4px 系で値が確定するため placeholder ではない)。ただし実追加 (primitive の編集) は本記録では行わず、改訂着手の設計承認 ([review-approval-rules.md](review-approval-rules.md) §9・§20) を経た別 Task とする。既存段の値・参照・`$status` は変更しない |
| 取得した判断 ⓑ 位置の用途 semantic トークン | 「セクション間」の余白のみ用途 semantic トークンとして定義する方向を確定する。「セクション内ブロック間」「面色セクションの内側 padding」の 2 区分は用途トークン化せず据置く。命名規則の正本 (`governance/naming-rules.md`) は Repository 内に存在せず参照切れ ([../services/travel/design-system/README.md](../services/travel/design-system/README.md) §16 の Open Issue) であるため、用途トークンの命名は当該正本の整備に依存する事実を併せて記録する。実追加 (semantic の編集) は本記録では行わず別 Task とする |
| 取得した判断 ⓒ 44px 段 (タップ領域) | 44px 段は `spacing` へ**追加しない (現状維持)**。既存の 48px (`spacing.12`) 代替運用は依頼元の観測であり、DS の規則として追認しない。44px の要否は既知の未確定事項 (design.md §7.1・[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8K = target size を UI・Implementation 下流課題に分類済み) に残す |
| 取得した判断 ⓓ 暫定 primitive 直参照 | 用途トークン (ⓑ) が定義されるまでの primitive 直参照の扱いは、用途トークンの定義 (別 Task) により解消する方向とする。それまでは用途トークン不在の未解消事項として残し、依頼元の暫定実装 (`--spacing-9` の暫定追加・`var(--spacing-9)` への一斉化) を DS の規則として追認しない |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定である **Web部レビュー担当者**。判定理由 (Web部責任者): 本記録工程は現在判断の記録と design.md 未確定事項の一覧の更新のみで、token の値・参照先・`$status`・`$meta.version`・規範規則 (§4) を変更しない (`spacing.9`・位置用途トークンの実追加は別 Task)。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は文の追加を含むため本工程に適用しない |
| 根拠 | 依頼元の DS-REQUEST「セクション間余白の規定と 36px 段」(2026-08-04)、Task 009-42 の Issue [#127](https://github.com/tocoo/coocom-design-system/issues/127)、`primitive.travel.json` の `spacing` 実測 (`0/1/2/3/4/5/6/8/10/12/16`・`9` 不在)、`semantic.travel.json` の位置用途トークン 0 件 (全文検索)、design.md §4・§7.1・未確定事項の一覧、[review-approval-rules.md](review-approval-rules.md) §8・§9・§10・§20、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (`spacing.9` = 2.25rem を 8 と 10 の間へ bound で追加する方向・実追加は別 Task) ⓑ (「セクション間」のみ用途 semantic トークン化する方向・他 2 区分据置・命名は `naming-rules.md` 整備に依存) ⓒ (44px 段は追加しない・現状維持) ⓓ (直参照は用途トークン定義で解消する方向) を 2026-08-04 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | `spacing.9`・位置用途 semantic トークンの実追加 (別 Task・§9・§20 設計承認先行)／用途トークンの命名 (`naming-rules.md` 参照切れ)／「セクション内ブロック間」「面色セクション内側 padding」の 2 区分の要否／44px の下流課題 (UI・Implementation) 側での扱い。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は `spacing.9`・位置用途 semantic トークンを実追加しない (実追加は改訂着手の設計承認を経た別 Task)。44px 段を追加しない。`governance/naming-rules.md` を新規作成しない (参照切れの正本を推測で作成しない)。既存 spacing 段の値・参照・`$status`・`$meta.version` を変更しない。依頼元の暫定実装 (`--spacing-9` の暫定追加・`var(--spacing-9)` 一斉化) を DS の規則として追認しない。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §18 である (Wiki は非正本)。

---

## 19. Travel 会員限定ラベルの用途区別・会員種別語の表記管轄・`color.text.onAccent` の状態の受理と分類の現在判断記録

- 種別: 国内宿泊 (travel) の会員限定ラベルの表現区別・会員種別語の表記管轄・`color.text.onAccent` の状態について Web部責任者が示した **2026-08-04 時点の現在判断**の記録。契機は依頼元 (ToCoo! 国内宿泊トップページ 画面設計・2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」依頼A + 判断点7) の依頼 (Task 009-43・Issue [#128](https://github.com/tocoo/coocom-design-system/issues/128))。上記 §1〜§18 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§18 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$description`・`$meta.version` を変更しない (会員限定ラベルの用途トークン・区別規則の実定義は行わず、`color.text.onAccent` は既に `bound`)。**判断日 (2026-08-04) と本 Repository 反映日 (2026-08-04) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の会員限定 (有料会員限定) ラベルの表現区別 (カテゴリラベルとの区別)・会員種別語 (無料 / 有料会員) の表記管轄・`color.text.onAccent` の状態。依頼元 (2026-08-04 起票) の依頼A + 判断点7 (Task 009-43・Issue [#128](https://github.com/tocoo/coocom-design-system/issues/128))。対象記述 = [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §2.1・§8 系・[../services/travel/design-system/components.md](../services/travel/design-system/components.md) `Card.slot.badge`・[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) `color.text.onAccent` |
| 判断日 | 2026-08-04 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-04 時点) |
| 取得した判断 ⓐ 会員限定ラベルの区別 | 会員限定 (有料会員限定) ラベルをカテゴリラベルと**区別する**方向を確定する。区別の手段 = 面色を用途で使い分ける — **基本 = neutral 面 / 特集紐づき = accent 面 / 例外 = inverse 面**。ただし**既存トークンの範囲で成立する組み合わせに限定**し、新しい色値・新しい面色用途を先に既成事実化しない (面色・文字色の成立条件は design.md §2.1 の検証表が正。§2.1 の (a)(b) サイズ・ウェイト条件により小サイズ (例 12px) では accent 面が成立しない場合があり、その場合は本 §13 の既定 = neutral dark 面に従う。小サイズの accent 面/白文字の適否は Task 009-44 (#129) が扱う)。写真の上に置く場合の扱いは E-1 (画像を面とする場合の scrim・Task 009-40 起票・design.md 未確定事項の一覧) と関連する (Task 009-46 (#131) は未選択値への `color.text.muted` 使用の別論点であり scrim ではない)。用途トークン・区別規則の実定義は改訂着手の設計承認 ([review-approval-rules.md](review-approval-rules.md) §9・§20) を経た別 Task とする |
| 取得した判断 ⓑ 会員種別語の表記管轄 | 会員種別語 (無料 / 有料会員) の表記は DS の token 管轄ではなく**コンテンツ表記規則の管轄**である。その管理正本については、参照切れの `brand-content.md` を [../services/travel/design-system/README.md](../services/travel/design-system/README.md) §16 (travel DS README の Open Issues) が未決として保持し、独立文書を新設する方向は本ファイル (owner-decisions.md) §16 (依頼 E-4) に記録されている。管理正本の所在 (design.md §8 系への集約か独立文書の新設か) は Task 009-45 (#130) が扱う論点であり、本記録では会員種別語の具体的な表記規則も管理正本の所在も確定しない (推測で表記規則を作らない・`brand-content.md` は未作成) |
| 取得した判断 ⓒ `color.text.onAccent` の状態 | `semantic.travel.json` に `color.text.onAccent` = `{color.palette.white}`・`$status: bound` として**既に定義済み** (Task 009-34 で追加)。DS 側の追加・変更は不要である。依頼元のポイント DS 側の同期漏れ (暫定追加) の解消は依頼元 Repository 側の対応であり、本 Repository では token を変更しない |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定である **Web部レビュー担当者**。判定理由 (Web部責任者): 本記録工程は現在判断の記録と design.md 未確定事項の一覧・components.md `Card.slot.badge` の未確定事項の更新のみで、`Card.slot.badge` の規範規則・token の値・`$status`・`$meta.version` を変更しない (会員限定ラベルの用途トークン・区別規則の実定義は別 Task・`color.text.onAccent` は既 `bound`)。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は文の追加を含むため本工程に適用しない |
| 根拠 | 依頼元の依頼A + 判断点7 (2026-08-04)、Task 009-43 の Issue [#128](https://github.com/tocoo/coocom-design-system/issues/128)、[../services/travel/design-system/components.md](../services/travel/design-system/components.md) `Card.slot.badge`、design.md §2.1、`semantic.travel.json` の `color.text.onAccent` = `{color.palette.white}`・`bound` (実測)、README.md §16、本 §13 (バッジ面色)・§16 (依頼 E-4)、[review-approval-rules.md](review-approval-rules.md) §8・§9・§10・§20、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (会員限定ラベルをカテゴリラベルと区別・手段 = 面色使い分け 基本 neutral / 特集 accent / 例外 inverse・既存トークンの範囲に限定・実定義は別 Task) ⓑ (会員種別語の表記はコンテンツ表記規則の管轄・管理正本の所在は §16 論点 / Task 009-45 に従い本記録で具体表記を確定しない) ⓒ (`color.text.onAccent` は既 `bound`・DS 側の追加不要) を 2026-08-04 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | 会員限定ラベルの用途トークン・区別規則の実定義 (別 Task・§9・§20 設計承認先行)／各面色の具体トークンと文字色の成立条件 (design.md §2.1・Task 009-44)／写真上への配置 (E-1 = 画像面の scrim・Task 009-40 起票)／会員種別語の管理正本の所在の確定 (§16 / Task 009-45) と具体表記。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は会員限定ラベルの用途トークン・区別規則を実定義しない (実定義は改訂着手の設計承認を経た別 Task)。新しい色値・新しい面色用途を追加しない。`brand-content.md` を新規作成せず、会員種別語の表記規則を確定しない。`color.text.onAccent` の値・参照先・`$status`・`$meta.version` を変更しない (既に `bound`)。依頼元の実装 (2 ラベルを同一バッジとし区別を付けない運用) を DS の規則として追認しない。会員限定で情報をマスクする表現 (E-2・Task 009-40 起票済) の構成を確定しない (本件はラベル・バッジの表現区別で別論点)。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §19 である (Wiki は非正本)。

---

## 20. Travel バッジ/ラベルの面色規則不適合 (割引率 #C8912C/白・小サイズ accent/白) の受理と分類の現在判断記録

- 種別: 国内宿泊 (travel) の Card.slot.badge の白文字非準拠運用について Web部責任者が示した **2026-08-04 時点の現在判断**の記録。契機は依頼元 (ToCoo! 国内宿泊トップページ 画面設計・2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」依頼B + 判断点2/4) の依頼 (Task 009-44・Issue [#129](https://github.com/tocoo/coocom-design-system/issues/129))。上記 §1〜§19 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§19 の各記録は変更しない (本 §13 のバッジ面色記録の記述も編集しない)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$description`・`$meta.version` を変更せず、§2.1・components.md `Card.slot.badge` の面色・コントラスト規則 (白文字禁止・(i)(ii) 代替・逆色面 `color.text.strong` 固定) も**実緩和しない** (例外の実規則化は別 Task)。**判断日 (2026-08-04) と本 Repository 反映日 (2026-08-04) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の `Card.slot.badge` の白文字非準拠運用 — (i) 割引率ラベル `#C8912C` 面 / 白文字 14px、(ii) 12px 小サイズラベル (会員限定・カテゴリ) campaign accent 面 / 白文字。依頼元 (2026-08-04 起票) の依頼B + 判断点2/4 (Task 009-44・Issue [#129](https://github.com/tocoo/coocom-design-system/issues/129))。対象記述 = [../services/travel/design-system/components.md](../services/travel/design-system/components.md) `Card.slot.badge`・[../services/travel/design-system/design.md](../services/travel/design-system/design.md) §2.1 検証表・本 §13 (§8.1 は同じ割引率ラベルの**表記規則**であり面色は扱わないため対象外) |
| 判断日 | 2026-08-04 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-04 時点) |
| 取得した判断 ⓐ 白文字非準拠運用の受理 | 実装側に (i)(ii) の白文字非準拠運用が存在し、いずれも現行規則 (`Card.slot.badge` の「逆色面は `color.text.strong` 固定・白文字を使用しない」「(i) 20px 未満のすべて / (ii) 20px 以上 24px 未満かつ通常ウェイト には campaign accent を面として使用しない」・design.md §2.1) に**不適合**である事実を DS 側で認識・記録する。コントラスト比は `#C8912C`×白 2.78:1・`#C8B12C`×白 2.15:1・campaign accent `#E4572E`×白 3.68:1 でいずれも通常テキスト 4.5:1 に達しない |
| 取得した判断 ⓑ 例外許容の方向 | これらの白文字非準拠を**例外として許容する方向**を確定する。例外の限定条件 = **用途 = 非操作の点的ラベル** (バッジ・割引率ラベル・カテゴリラベル等の非操作ラベル) かつ **面 = campaign accent または scheme 逆色 (`#C8912C` / `#C8B12C`)** に限定する。**サイズ・ウェイトは不問** (小サイズ・通常ウェイトを含む)。**AA 未達であることを明示する** (上記コントラスト比・通常テキスト 4.5:1 に達しない)。本例外は本 §13 (2026-08-03) の「逆色面は `color.text.strong` 固定・白文字を使用しない」および §2.1・components.md の白文字禁止・(i)(ii) 代替に対する例外であり、**その実際の規則化 (§2.1・components.md `Card.slot.badge` への例外条項の追加) は改訂着手の設計承認 ([review-approval-rules.md](review-approval-rules.md) §9・§20) を経た別 Task とする**。それまで現行規則 (白文字禁止・(i)(ii) 代替・逆色面 `color.text.strong` 固定) は維持し、実装側の非準拠運用は DS 規則としては未是正のまま扱う (依頼元の実装を実規則化の前に既成事実化しない) |
| 取得した判断 ⓒ 白文字が成立する面 | 既存 palette の範囲で通常テキスト 4.5:1 を満たす白文字面は `color.surface.inverse` (#212121・16.10:1) の**1 面のみ** (§2.1 検証表)。campaign accent (3.68:1)・scheme 逆色 (2.78:1 / 2.15:1) はいずれも未達であり、他面で白文字は成立しない。ⓑ の例外許容は AA 未達を明示のうえで許容する方向であって、成立 (適合) の主張ではない |
| 取得した判断 ⓓ b2 (accent 淡色段) の扱い | 本 §13 の b2 (小サイズバッジ向けに accent 淡色面 = 淡色面 + 濃色文字 を新設する方向・実色値未取得) を**維持し保留する**。取得までの 12px ラベルの暫定は §13 の既定 (neutral dark 面 `color.surface.inverse` + `color.text.inverse`) を維持する。b2 (淡色面の追加) と ⓑ (白文字非準拠の例外許容) は同一問題への別経路として併存し、b2 は実色値取得まで保留する |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定である **Web部レビュー担当者**。判定理由 (Web部責任者): 本記録工程は現在判断の記録と design.md 未確定事項の一覧・components.md `Card.slot.badge` 未確定事項の更新のみで、§2.1・components.md の面色・コントラスト規則 (白文字禁止・(i)(ii) 代替・逆色面 `color.text.strong` 固定) を実緩和せず、token の値・`$status`・`$meta.version` を変更しない (例外の実規則化・b2 の実追加は別 Task)。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は文の追加を含むため本工程に適用しない |
| 根拠 | 依頼元の依頼B + 判断点2/4 (2026-08-04)、Task 009-44 の Issue [#129](https://github.com/tocoo/coocom-design-system/issues/129)、[../services/travel/design-system/components.md](../services/travel/design-system/components.md) `Card.slot.badge`、design.md §2.1 検証表 (main 5.78:1 / sub 7.50:1・白文字 2.78:1 / 2.15:1・accent 3.68:1・surface.inverse 16.10:1)、本 §13 (バッジ面色・c1・b2)、[review-approval-rules.md](review-approval-rules.md) §8・§9・§10・§20、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (白文字非準拠 (i)(ii) の存在と現行規則不適合を認識・記録) ⓑ (例外許容の方向・限定条件 = 非操作の点的ラベル + campaign accent/逆色面・サイズ/ウェイト不問・AA 未達明示・実規則化は別 Task・現行規則は維持) ⓒ (白文字成立面は `surface.inverse` の 1 面のみ) ⓓ (b2 保留・12px 暫定は §13 の既定を維持) を 2026-08-04 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | 例外条項の実規則化 (§2.1・components.md・別 Task・§9・§20 設計承認先行)／b2 の accent 淡色段の実色値・淡色面の実追加 (§13)／実装側の是正 / 非是正の範囲・時期 (実装 Repository 側の判断)／例外許容 (ⓑ) と b2 (ⓓ) のいずれを最終的な解決とするか。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は §2.1・components.md `Card.slot.badge` の面色・コントラスト規則 (白文字禁止・(i)(ii) 代替・逆色面 `color.text.strong` 固定) を実緩和・変更しない (例外の実規則化は改訂着手の設計承認を経た別 Task)。本 §13 の記述を編集しない (本 §20 は 2026-08-04 の現在判断として例外許容の方向を記録するのみ)。新規 primitive・面色用途トークンを追加せず、b2 の accent 淡色段の実色値を発明しない。依頼元の実装 (`#C8912C` 面 / 白文字・12px accent 面 / 白文字) を DS の例外規則として (実規則化の前に) 追認しない。実装側の是正の範囲・時期を決定しない。適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (コントラスト比は概算の記録・ⓑ は AA 未達を明示する)。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §20 である (Wiki は非正本)。

---

## 21. Travel 割引率の表記規則 (§8.1) の改訂・コンテンツ表記規則の管理正本 (§16 の新設方向の撤回) の受理と分類の現在判断記録

- 種別: 国内宿泊 (travel) の割引率の表記規則 (§8.1) の改訂とコンテンツ表記規則の管理正本について Web部責任者が示した **2026-08-04 時点の現在判断**の記録。契機は依頼元 (ToCoo! 国内宿泊トップページ 画面設計・2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」判断点5 + DS-REQUEST「割引率の表記規則 (§8.1)」) の依頼 (Task 009-45・Issue [#130](https://github.com/tocoo/coocom-design-system/issues/130))。上記 §1〜§20 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§20 の各記録は変更しない (本 §16 の記述も編集しない — 本 §21 は 2026-08-04 の現在判断として §16 の E-4 方向を撤回する方向を記録するのみ)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$meta.version` を変更せず、**§8.1 本体・§16 本体・[../services/travel/design-system/README.md](../services/travel/design-system/README.md) §16 の記述も実編集しない** (実改訂は改訂着手の設計承認を経た別 Task)。**判断日 (2026-08-04) と本 Repository 反映日 (2026-08-04) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の割引率の表記規則 (design.md §8.1) の基本形・マイナス付与規則・「最大」条件・改訂場所・記号、およびコンテンツ表記規則の管理正本 (本 §16・E-4)。依頼元 (2026-08-04 起票) の判断点5 + DS-REQUEST「割引率の表記規則 (§8.1)」(Task 009-45・Issue [#130](https://github.com/tocoo/coocom-design-system/issues/130))。対象記述 = [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §8.1・§8・本 §16・[../services/travel/design-system/README.md](../services/travel/design-system/README.md) §16 |
| 判断日 | 2026-08-04 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-04 時点) |
| 取得した判断 ⓐ 基本形の変更・マイナス付与規則の撤回 | §8.1 の割引率表記の基本形を `-NN%` → **`NN%OFF`** へ変更し、マイナス付与規則 (§8.1「符号」節 L297-298「割引率であることを視覚的に示すため、数値の前に半角マイナス `-` を付す」) を**撤回する方向**を確定する。§8.1「表示形式」L291 (基本形 `-NN%`)・L292 (原則使用しない表記に `NN%OFF` が含まれる点)・「符号」節の [決定] を改める設計変更として記録する。§8.1 L293 の上書き機構 (「Owner 決定またはブランドガイドラインに存在する場合はそれを優先し根拠を記録する」) に沿い、本 §21 (本 Repository 内で確認できる Owner 決定) が改訂の根拠となる。**§8.1 本体の実改訂は改訂着手の設計承認 ([review-approval-rules.md](review-approval-rules.md) §9・§20) を経た別 Task**であり、それまで §8.1 の基本形は `-NN%` のまま維持する |
| 取得した判断 ⓑ 「最大NN%OFF」の使用条件 | 現行 §8.1 L324 は「最大」等の条件付き表現の使用条件を ❓ 未確定としている。**使用条件を定める方向**を確定する = 対象範囲 (対象プラン等) における最大値であり、かつ文脈で「最大」と判別可能な場合にのみ使用する (CTP-004 Evidence-backed Claims)。ただし割引率の**算出式・端数処理・表示可能な上限値・`100%` 以上のデータの扱い**は上流未決 (§8.1 L307/L322-323・`../service-design/content-principles.md` §10) であり据置く (DS では任意の数値を決定しない) |
| 取得した判断 ⓒ 改訂場所・§16 の新設方向の撤回 | 改訂は現行 **§8.1 で恒久的に行う方向** (新設文書の作成を待たない) とする。あわせて、本 §16 (2026-08-03・E-4) の「コンテンツ表記規則の管理正本として独立文書 (`brand-content.md` 等) を新設する方向」を**撤回**し、割引率等のコンテンツ表記規則は **design.md §8 系に集約する方向**を確定する。[../services/travel/design-system/README.md](../services/travel/design-system/README.md) §8/§16 の `brand-content.md` の Open Issue も「新設しない」で決着する方向とする。**§16 の記述の実編集・README の実更新・§8.1 の実改訂はいずれも改訂着手の設計承認 (§9・§20) を経た別 Task**であり、現時点では §16・README・§8.1 の本体は未改訂 (§8.1 L338 は現在も新設方向を記す) |
| 取得した判断 ⓓ 記号 | 全角 `％`・`▲NN%` の禁止を維持する (§8.1 L292)。パーセント記号は半角 `%` を用いる (§8.1 L291 の基本形「半角マイナス + 半角数字 + 半角パーセント」および L292 が全角 `20％引き` を原則使用しないとする点と同方向・依頼書 [m0333] とも同方向) |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **高** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定である **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11)。判定理由 (Web部責任者): 本記録工程は現在判断の記録と design.md 未確定事項の一覧の更新のみで §8.1・§16・README の本体は実改訂しないが、記録する現在判断が承認済み §8.1 (割引率表記規則) の基本形変更・マイナス付与規則の撤回、および承認済み本 §16 (コンテンツ表記規則の管理正本の方向) の撤回を方向づける設計変更に及ぶため、本記録工程を高とする。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は規範方向の変更・文の追加を含むため本工程に適用しない |
| 根拠 | 依頼元の判断点5 + DS-REQUEST「割引率の表記規則 (§8.1)」(2026-08-04)、Task 009-45 の Issue [#130](https://github.com/tocoo/coocom-design-system/issues/130)、design.md §8.1 (L287-338 の現行 [決定]・L293 の上書き機構)・§8 (管理正本)、本 §16 (E-4)、[../services/travel/design-system/README.md](../services/travel/design-system/README.md) §16、`../service-design/content-principles.md` §10 (上流未決)、[review-approval-rules.md](review-approval-rules.md) §8・§9・§10・§20、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (基本形 `-NN%` → `NN%OFF`・マイナス付与規則の撤回の方向・実改訂は別 Task) ⓑ (「最大NN%OFF」の使用条件を定める方向 = 対象範囲の最大値かつ文脈で判別可・算出/上限は据置) ⓒ (改訂場所 = §8.1 恒久・§16 の `brand-content.md` 新設方向を撤回し design.md §8 系集約の方向・README も新設しない方向・実編集は別 Task) ⓓ (全角 `％`・`▲` の禁止維持・半角 `%`) を 2026-08-04 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | §8.1・§16・README の実改訂 (別 Task・§9・§20 設計承認先行)／割引率の算出式・端数処理・上限値・`100%` 以上・割引率と値引額の使い分け (上流未決・content-principles.md §10)／design.md §8 系集約後の文書構成・管理責務。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は §8.1・§16・README の記述を実編集しない (実改訂は改訂着手の設計承認を経た別 Task)。依頼元 Owner 決定 [m0XXX] を本 Repository の承認正本として扱わず、依頼元の実装 (「35%OFF」等) を DS の規則として (実改訂の前に) 追認しない。`brand-content.md` を新規作成しない (§16 の新設方向は本記録で撤回する方向であり作成もしない)。割引率の算出式・端数処理・上限値・`100%` 以上の扱いを決定しない (上流未決)。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §21 である (Wiki は非正本)。

---

## 22. Travel 未選択値 (プレースホルダ相当) への color.text.muted 使用の受理と分類の現在判断記録

- 種別: 国内宿泊 (travel) の検索モジュールの未選択値への `color.text.muted` 使用について Web部責任者が示した **2026-08-04 時点の現在判断**の記録。契機は依頼元 (ToCoo! 国内宿泊トップページ 画面設計・2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」§4.5 + 判断点6) の依頼 (Task 009-46・Issue [#131](https://github.com/tocoo/coocom-design-system/issues/131))。上記 §1〜§21 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§21 の各記録は変更しない (§2.3 の記述も編集しない)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は Design System の token・値・`$status`・`$description`・`$meta.version` を変更せず、§2.3 の `color.text.muted` 流用禁止規則も**実緩和しない** (例外の実規則化は別 Task・`color.text.placeholder` / `color.text.muted` は既に `bound`)。**判断日 (2026-08-04) と本 Repository 反映日 (2026-08-04) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | travel の検索モジュールの未選択値 (「都道府県を選択」「日付を選択」等) の文字色。§2.3 の placeholder 対象と `color.text.muted` の流用禁止。依頼元 (2026-08-04 起票) の §4.5 + 判断点6 (Task 009-46・Issue [#131](https://github.com/tocoo/coocom-design-system/issues/131))。対象記述 = [../services/travel/design-system/design.md](../services/travel/design-system/design.md) §2.3・[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) `color.text.placeholder` / `color.text.muted` |
| 判断日 | 2026-08-04 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-04 時点) |
| 取得した判断 ⓐ select の未選択値のみ muted 例外許容 | **select の未選択値 (選択前の `option` に相当する表示) に限り** `color.text.muted` (#9e9e9e・白背景 ≈2.7:1) の使用を**例外として許容する方向**を確定する。`color.text.muted` は通常テキストに求められる 4.5:1 に達しない (**AA 未達を明示する**)。本例外は §2.3 の「`color.text.muted` をプレースホルダへ流用しない」(L157) および §2.3 が選択前 `option` を `color.text.placeholder` 対象とする点 (L156) に対する例外であり、**その実際の規則化 (§2.3 への例外条項の追加) は改訂着手の設計承認 ([review-approval-rules.md](review-approval-rules.md) §9・§20) を経た別 Task**とする。それまで §2.3 (muted 流用禁止・選択前 `option` → placeholder) は維持し、実装側の未選択値への muted 使用は DS 規則としては未是正のまま扱う (依頼元の実装を実規則化の前に既成事実化しない) |
| 取得した判断 ⓑ 通常 input/textarea placeholder は維持 | select の未選択値以外の `input` / `textarea` の `::placeholder` は現行どおり `color.text.placeholder` (gray.700・#616161・白背景 ≈6.2:1) を維持する。例外 (ⓐ) は **select の未選択値に限定**し、通常のプレースホルダへは及ぼさない |
| 取得した判断 ⓒ 未選択値が §2.3 の placeholder 対象に含まれる事実 | `color.text.placeholder` の `$description` は「対象 = `input` / `textarea` の `::placeholder`、選択前の `option` に相当する表示」と定めており、未選択値はこの対象に含まれる (既定義)。本例外 (ⓐ) は、この既定義の対象のうち select の未選択値のみを `color.text.muted` へ切り替える方向であり、`color.text.placeholder` トークンの `$value` (`{color.palette.gray.700}`)・`$status` (`bound`) は変更しない |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 本記録工程の影響度 | **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定である **Web部レビュー担当者**。判定理由 (Web部責任者): 本記録工程は現在判断の記録と design.md 未確定事項の一覧の更新のみで、§2.3 の `color.text.muted` 流用禁止規則を実緩和せず、token (`color.text.placeholder` / `color.text.muted`) の値・`$status`・`$meta.version` を変更しない (例外の実規則化は別 Task)。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は文の追加を含むため本工程に適用しない |
| 根拠 | 依頼元の §4.5 + 判断点6 (2026-08-04)、Task 009-46 の Issue [#131](https://github.com/tocoo/coocom-design-system/issues/131)、design.md §2.3 (L156-157)、`semantic.travel.json` の `color.text.placeholder` (`{color.palette.gray.700}`・`bound`) / `color.text.muted` (`{color.palette.gray.600}`・`bound`) (実測)、本 §14 (placeholder 実査待ちの確認方法・別論点)、[review-approval-rules.md](review-approval-rules.md) §8・§9・§10・§20、本記録の PR |
| 判断により確定した事項 | travel について ⓐ (select の未選択値のみ `color.text.muted` 例外許容の方向・AA 未達明示・実規則化は別 Task・§2.3 は維持) ⓑ (通常 input/textarea の placeholder は `color.text.placeholder` gray.700 を維持) ⓒ (未選択値は §2.3 の placeholder 対象に含まれる既定義・placeholder トークンは不変) を 2026-08-04 時点の現在判断として記録したこと |
| 判断後も未決・未確認の事項 | §2.3 への例外条項の実規則化 (別 Task・§9・§20 設計承認先行)／実装側の是正 / 非是正の範囲・時期 (実装 Repository 側の判断)／select コンポーネント自体の仕様 (未着手・components.md)。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は §2.3 の記述を実編集せず、`color.text.muted` 流用禁止規則を実緩和しない (例外の実規則化は改訂着手の設計承認を経た別 Task)。`color.text.placeholder` / `color.text.muted` の値・参照先・`$status`・`$meta.version` を変更しない (両者 `bound`)。依頼元の実装 (未選択値に #9e9e9e) を DS の例外規則として (実規則化の前に) 追認しない。ラベル (「都道府県」「地域」等 12px) を gray.700 に変更したという依頼元の実装 (Owner 決定 [m0258] の付随内容) を DS の規則として扱わない。実装側の是正の範囲・時期を決定しない。適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (ⓐ は AA 未達を明示する)。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。rental-car / inbound の成果物へ適用しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §22 である (Wiki は非正本)。

---

## 23. デザインシステム適用範囲の例外 (広告・非 UI クリエイティブ・画像等) を Governance 横断ルールとして新設することの受理と分類の現在判断記録

- 種別: デザインシステムの適用範囲について、**広告・非 UI クリエイティブ・画像等 (Webサイト内の機能 UI 要素ではない、自己完結した視覚アセット)** に対しトークン (フォント / カラー / スペーシング) 指定外の値の使用を例外的に許容する**恒久的な適用範囲の例外原則を Governance 横断ルールとして新設すること**について、Web部責任者が示した **2026-08-05 時点の現在判断 (起票時の方向性)** の記録。契機は依頼者 (Web部責任者) の直接依頼 (2026-08-05・Task 009-47・Issue [#138](https://github.com/tocoo/coocom-design-system/issues/138))。上記 §1〜§22 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§22 の各記録は変更しない。**本記録は受理と分類の工程であり、Governance 原則正本 (新規ファイル) の実本文は作成・確定しない (改訂着手 = 原則正本の新設の設計承認 [review-approval-rules.md](review-approval-rules.md) §9・§20 と影響度判定 §8 を先行させる)**。本件は Task 009-42〜46 (travel 限定・#127-131) とは別系統の Governance 横断論点である。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。**現在判断と過去の provenance を区別する**。GitHub の approval・merge を判断と同一視しない。本記録は 3 サービス (travel / rental-car / inbound) の Design System の token・値・`$status`・`$description`・`$meta.version`・version を変更せず、各 `design.md` の冒頭スコープ行・§8・[README.md](README.md)・承認済み [review-approval-rules.md](review-approval-rules.md) 本体を実編集しない。**判断日 (2026-08-05) と本 Repository 反映日 (2026-08-05) は同日だが別の事象として区別する**。

| 項目 | 内容 |
| --- | --- |
| 判断対象 | Governance 横断ルールとして「デザインシステム適用範囲の例外 (広告・非 UI クリエイティブ・画像等)」を新設することの受理と分類 (3 サービス共通の適用範囲原則)。依頼者 (Web部責任者) の直接依頼 (2026-08-05・Task 009-47・Issue [#138](https://github.com/tocoo/coocom-design-system/issues/138))。対象記述 (欠落の確認先) = 3 サービス `design.md` 冒頭スコープ行 ([../services/travel/design-system/design.md](../services/travel/design-system/design.md) L7 / [../services/rental-car/design-system/design.md](../services/rental-car/design-system/design.md) L6 / [../services/inbound/design-system/design.md](../services/inbound/design-system/design.md) L6)・各 §8 (travel L276 / rental-car L78 / inbound L88)・[README.md](README.md) (L35-40 principles 正本未整備) |
| 判断日 | 2026-08-05 |
| 判断主体 | Web部責任者 |
| 判断の種別 | **現在判断** (2026-08-05 時点・起票時の方向性) |
| 取得した判断 ⓐ Governance 横断ルールとして新設する方向 | 本例外原則を特定サービスの `design.md` ではなく **Governance 横断ルール (3 サービス共通の適用範囲原則) として新設する方向**を確定する。DS はサービス単位で独立し Foundation/Semantic/Component/design.md を共有しない (要求仕様 R1・travel design.md L9) が、命名・運用規約は 3 サービス共通で `governance/` に置く (R2・同 L9)。適用範囲の例外はこの共通運用規約の系に属するため Governance 横断とする。**新規 Governance ファイルの実本文の作成・確定は改訂着手の設計承認 ([review-approval-rules.md](review-approval-rules.md) §9・§20) を経た別 Task**であり、それまで原則正本は新設しない ([README.md](README.md) L37「本 bootstrap では新規作成しない」とする principles 正本領域への初の追加のため設計承認をゲートとする) |
| 取得した判断 ⓑ スタイル (トークン) のみ例外・A11y 最低ライン (R9) は維持 | 許容する逸脱は **フォント (書体・ウェイト)・カラー・スペーシングのトークン指定外の値の使用に限る**。**WCAG 2.2 AA の最低ライン (要求仕様 R9・travel design.md L53) は免除しない**。非 UI クリエイティブ内で情報を伝える重要テキストのコントラスト等は本例外の対象外とし、引き続き最低ラインを満たす |
| 分類した骨子 (定義案・4 項目) | 起票時の 2 方向性 (ⓐ・ⓑ) を前提に、新設する例外原則の骨子を次の 4 項目として分類する (定義案・確定は設計承認時)。**① 対象**: 広告・非 UI クリエイティブ・画像等 = Webサイト内の機能 UI 要素ではない自己完結した視覚アセット (想定例: 写真・イラスト・広告 / キャンペーンバナー・販促ビジュアル・ロゴ / ワードマーク)。**② 許容する逸脱**: フォント・カラー・スペーシングのトークン指定外の値の使用。**③ 維持する制約 (免除しない)**: WCAG 2.2 AA の最低ライン (R9)。**④ 適用境界**: ライブ UI (HTML/CSS でレンダリングされる文字・ボタン・入力・ナビゲーション・カード・バッジ等の機能要素) は従来どおりトークンに従う。境界の細部 (ヒーロー領域の見出しがライブテキストか画像内テキストか・ロゴ内タイポの扱い) は設計承認時に確定する |
| 分類した置き場所・相互参照・既存記述との整合 | 想定構成 = 新規 Governance ファイル (適用範囲の例外原則) を正本とし、3 サービス `design.md` の冒頭スコープ行から参照する。既存の部分記述との整合を次のとおり整理する。① 冒頭スコープ (顧客向け UI のみ・管理画面除外) は**管理画面 vs 顧客向け**の線引きであり、顧客向けサイト内の**非 UI クリエイティブ vs UI 要素**の線引きではない (別軸)。② rental-car §8 L83 / inbound §8 L94 の「広告 / SNS / メールは資産提供待ち — 本版スコープ外」は*資産提供待ちのため本版限定の範囲外*という趣旨であって、**恒久的な例外原則ではない** (本例外は恒久原則として別に位置づく)。③ travel §8 に同種記述はない。**ファイル名・配置・原則正本体系への収め方・各 design.md 冒頭スコープ行 / §8 からの実際の相互参照追記・rental-car / inbound §8 記述との最終的な書き分けは設計承認時に確定する (本 Task では実追記・書き換えを行わない)** |
| 欠落の確認結果 (Fact・`origin/main` `8de04c9` 時点) | 「非 UI クリエイティブは DS トークン指定外使用を例外的に許容する」という**恒久的な適用範囲の例外原則は、3 サービスの Design System にも Governance にも明文化されていない (欠落)**。直接証拠: 3 サービス冒頭スコープ行は管理画面除外のみ (travel L7 / rental-car L6 / inbound L6)・各 §8 に恒久例外原則なし (rental-car L83 / inbound L94 は資産提供待ち本版スコープ外・travel §8 に該当記述なし)・[README.md](README.md) は principles 正本を未整備とし本 bootstrap では新規作成しないとする (L35-40)。既存の部分記述は本例外を代替しない |
| 適用範囲 | **Governance 横断 (3 サービス共通の適用範囲原則)**。travel / rental-car / inbound の 3 サービスに及ぶ横断ルールとして新設する方向 (起票時の方向性ⓐ)。ただし原則正本の実本文・各 design.md への相互参照追記は改訂着手の設計承認を経た別 Task |
| 本記録工程の影響度 | **高** (判定者 = Web部責任者、判定日 = 2026-08-05、本件について明示取得)。→ 必要レビュー主体 = [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定である **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11)。判定理由 (Web部責任者): 本記録工程は現在判断の記録のみで新規 Governance ファイルの実本文・各 design.md・review-approval-rules.md・token を実改訂しないが、記録する現在判断が **Governance 横断の原則正本の初の新設** ([README.md](README.md) が「新規作成しない」とする principles 正本領域への初の追加) を方向づける設計変更に及ぶため、本記録工程を高とする。高／低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21)。同 §8 の編集的訂正 carve-out は規範方向の追加・文の追加を含むため本工程に適用しない |
| 根拠 | 依頼者 (Web部責任者) の直接依頼 (2026-08-05)、Task 009-47 の Issue [#138](https://github.com/tocoo/coocom-design-system/issues/138)、3 サービス `design.md` 冒頭スコープ行 (travel L7 / rental-car L6 / inbound L6)・§8 (travel L276 / rental-car L78・L83 / inbound L88・L94)・travel design.md L9 (R1 / R2)・L53 (R9 = WCAG 2.2 AA)、[README.md](README.md) L35-40 (principles 正本未整備・bootstrap では新規作成しない)、[review-approval-rules.md](review-approval-rules.md) §8・§9・§10・§20、本記録の PR |
| 判断により確定した事項 | ⓐ (Governance 横断ルールとして新設する方向・実本文は別 Task) ⓑ (フォント / カラー / スペーシングのトークン指定外使用のみ例外・A11y 最低ライン R9 は維持) を 2026-08-05 時点の現在判断 (起票時の方向性) として記録し、新設する例外原則の骨子 4 項目 (対象・許容する逸脱・維持する制約 = R9 維持・適用境界) を定義案として分類し、置き場所・相互参照方法と既存部分記述との整合を分類したこと |
| 判断後も未決・未確認の事項 | 新規 Governance ファイルの実本文の作成・確定 (別 Task・§9・§20 設計承認先行)／ファイル名・配置・原則正本体系への収め方／3 サービス design.md 冒頭スコープ行・§8 からの相互参照の実追記／適用境界の細部 (ライブテキスト vs 画像内テキスト・ロゴ内タイポ)／rental-car・inbound §8「本版スコープ外 (資産提供待ち)」記述との最終的な書き分け。いずれも本記録では決定・補完しない |

**Does Not Decide / Does Not Authorize**: 本記録は新規 Governance ファイル (適用範囲の例外原則の正本) を作成・確定しない (実本文の作成は改訂着手の設計承認 §9・§20 を経た別 Task)。承認済み [review-approval-rules.md](review-approval-rules.md) 本体を改定しない。3 サービス `design.md` の冒頭スコープ行・§8・token・値・参照先・`$status`・`$description`・`$meta.version`・version を変更しない。rental-car / inbound §8 の「本版スコープ外 (資産提供待ち)」記述を書き換えない。適用境界の細部 (ライブテキスト vs 画像内テキスト・ロゴ内タイポ) を最終確定しない。A11y の適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (ⓑ は WCAG 2.2 AA = R9 を最低ラインとして維持する方向を記録するのみ)。Design System の候補採否・改定要否・改訂着手・設計承認を決定・承認しない。GitHub の approval・merge を判断と同一視しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §23 である (Wiki は非正本)。

---

## 24. Travel ラベル・タグ定義 (A〜H) の実装 (設計承認・影響度・現在判断) の記録

- 種別: 国内宿泊 (travel) のラベル・タグ定義シート (画面設計 Owner 決定 2026-08-07・一部 2026-08-10) を DS 正本 (SOT) へ実装することについて Web部責任者が示した現在判断・改訂着手の設計承認・影響度判定の記録。契機は依頼元 (ToCoo! 国内宿泊 画面設計「ラベル・タグ定義シート」・「DS 依頼書: ラベル・タグ定義 (travel)」2026-08-07 起票 / 2026-08-10 改訂) の依頼 (Task 009-48〜009-56・Issue [#140](https://github.com/tocoo/coocom-design-system/issues/140)〜[#148](https://github.com/tocoo/coocom-design-system/issues/148))。上記 §1〜§23 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§23 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。現在判断と過去の provenance を区別する。GitHub の approval・merge を判断・設計承認と同一視しない。依頼元 (画面設計) の決定は依頼元が観測・記録した事実として扱い、本記録 (Web部責任者の現在判断) をもって本 Repository の承認正本とする。仮色 (実色値未取得) は placeholder として bind し発明しない。**判断日 (2026-08-10) と本 Repository 反映日 (2026-08-10) は同日だが別の事象として区別する**。

### 24-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | ラベル・タグ定義シート (A〜H) の DS 正本 (SOT) への実装 = `design.md` (§2.1 白文字例外・検証表・§8.1 表記・F 予約条件・H 適用範囲)・`components.md` (`Card.slot.badge` の分岐・器・各ラベル)・`primitive.travel.json` / `semantic.travel.json` (accent 2 段・用途色・器・`radius.badge`) の改訂/新設 |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-08-10 |
| 承認主体 | Web部責任者 |
| 根拠 | 各件の方向は既に確定済み (いずれも本記録: A 白文字例外 = §20 / A 表記 = §21 / b2 = §13。承認種別欄の「§9・§20」= [review-approval-rules.md](review-approval-rules.md) の節であり本記録 §20 とは別)、または画面設計 Owner 決定 (2026-08-07 / 08-10) で確定。依頼書は「既存の方向確定の実行・用途の追記・規則の明文化であり新しい色値もトークンも増やさない」とする (例外は accent 2 段で、うち淡色段 1 値のみ Owner 選定で確定・残 3 値は 🚧 仮色) |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |

### 24-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **高** (判定者 = Web部責任者・判定日 2026-08-10・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定 = **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11) |
| 判定理由 (Web部責任者) | 本実装は承認済み §2.1・§8.1・`components.md` `Card.slot.badge` の規範規則を実改訂し (白文字例外の追加・表記の基本形変更・符号節撤回)、`design.md` に節 (F 予約条件・H 適用範囲) を新設し、primitive / semantic に新規トークンを追加する。設計内容・設計判断・token 値/定義に及ぶため §8 の編集的訂正 carve-out (字句のみ) の対象外。Task 009-45 (§21・表記) も高判定だった。高/低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21) |

### 24-3. 取得した現在判断 (カテゴリ別)

| カテゴリ | 取得した判断 (2026-08-10 時点の現在判断) |
| --- | --- |
| 器 (共通) | 全ラベルの共通器 = 高さ sm 20px / md 24px・左右余白 sm 8px / md 12px・行高 1 (上下中央・上下余白は指定しない)・角丸 `radius.badge` (4px)・面のあるラベル 700 / 中立タグ (D) 400。semantic に top-level `label.*` として追加 (既存 spacing / typography.size / fontWeight / radius への割当・新しい数値なし) |
| A 割引率 | 逆色面 `#C8912C` + 白文字 (≈2.78:1・AA 未達) を**非操作の点的ラベルに限る例外**として実規則化 (§2.1・`Card.slot.badge`)。表記の基本形を `-NN%` → `NN%OFF` へ変更し、**数字を 1 段大きく表示** (§8.1・符号節 = マイナス付与規則を撤回・全角 `％`/`▲` 禁止維持・半角 `%`)。用途色 `color.label.discount`。実 px = 器・`radius.badge` = 4px |
| B 会員 | 有料 (プライム) = accent 淡色面 `#F9CDBC` + 濃色文字 `#8A2E11` (🚧 仮色)。無料 = 主色 tint `#E8EDFB` + ink `#14224A`。`color.membership.paid` / `free`。primitive に accent 淡色段 (`orange.100` bound) / 濃色段 (`orange.800` 🚧) と `coral` 2 段 (🚧) を追加。「会員ランク色は構築しない (破棄済)」は階級表現に限る形で**差し戻し** (会員種別 2 値は別) |
| C 特集 | **仮決定** (accent の帰属が B / C で未定) のため本バッチでは実装しない (据え置き・依頼書 §10)。用途色 `color.label.category` は追加しない |
| D 施設属性 | 中立面 `surface.muted` `#F5F5F5` + 文字 `text.body`・400。色を持たせず器 1 つに統合。区分 (D1 施設種別 / D2 館内設備 / D3 利用条件) は順序で読ませる (D4 格付けは廃止)。`color.tag.neutral` |
| E 在庫・状態 | E1 残室僅少 = `state.error` の文字を価格の直上に (面なし・白背景 ≈4.8:1・写真上に出さない)。`color.label.stock`。`state.error` の用途に「利用者に不利な事実の明示」を含める (F 規則 7 と共通・上流 CTP-010)。E2 販売終了 (非活性 CTA) は**方向のみ** (CTA に集約) で値は未確定 = 据え置き (依頼書 §10) |
| F 予約条件 | 決済手段・返金可否・ポイント付与の表示規則 7 点を `design.md` に新設 (面なしテキスト行・文字色 4 役 = 得 `scheme.main.base` 暫定 / 損 `state.error` / 中立 `text.mutedStrong` / 操作 `text.link`・アイコン固定・並び固定・文言併記)。**色値もトークンも新設しない** (既存色の割当規則のみ)。メリット色は G-1 (現行 base) で暫定・リンクとの見分けは未解決 (依頼書 §10) |
| G 写真枚数 | pill (`surface.inverse` + 白文字・`radius.action`) で既存トークンで成立するため **DS への token 追加なし** (依頼書 §10)。`components.md` に規則として明記 |
| H 適用範囲 | クリエイティブへの DS 適用を **2 段** (適用 = トークンのみ / 適用外 = ガイドライン) に分け `design.md` に新設。カラーは厳守・品質下限 (AA・44px・代替テキスト・色だけで伝えない) は維持・**グラデーションは審査対象**。審査基準の策定と審査主体の設置は運用体制として DS 側に委ねられた新規論点 (Task 009-55) であり、基準・主体の実策定は本バッチに含めない |
| 実査値 (§9) | accent 濃色段 (`orange.800` `#8A2E11`) は 🚧 仮色・実色値は実査待ち。サブスキーム `coral` 2 段 (`#f8cbc2` / `#8a2c18`) も 🚧 仮色。accent 淡色段 (`orange.100` `#F9CDBC`) は Owner 選定で bound。`radius.badge` は 4px で placeholder → bound 昇格 (§14 の確認方法・確認主体を満たす・値は変わらない) |

### 24-4. §23 (Governance 横断) との関係・未決事項

- H (クリエイティブ適用範囲) は §23 (Task 009-47・非 UI クリエイティブのトークン指定外使用の例外を Governance 横断ルールとして新設する方向) と同軸だが、本 §24 は travel `design.md` §8 系への明文化 (travel 限定) を実装する。§23 の「カラーもトークン指定外を許容」(ⓑ) と本シートの「カラーは厳守」の差分、および原則正本の置き場所 (Governance 横断 vs travel design.md) は §23 の設計承認プロセス・Task 009-55 (Issue [#147](https://github.com/tocoo/coocom-design-system/issues/147)) で扱う (本 §24 では travel §8 への明文化に留める)。
- **判断後も未決・未確認の事項**: accent 濃色段・coral 2 段の実色値 (実査待ち・§9・§14)／C 特集の用途色 (accent 帰属未定・据え置き)／E2 販売終了の値 (方向のみ)／F メリット色 (G-1 暫定・リンクとの見分け)／H グラデーション審査基準・審査主体の実策定 (Task 009-55)／§23 との原則正本の置き場所・カラー差分。いずれも本記録では決定・補完しない。

**Does Not Decide / Does Not Authorize**: 本記録は accent 濃色段・`coral` 2 段の実色値を発明・確定しない (🚧 仮色 placeholder)。C 特集の用途色・E2 販売終了の値を確定しない (据え置き)。F のメリット色 (得 = `scheme.main.base`) を暫定から確定へ昇格せず、リンクとの見分けを解決しない。H のグラデーション審査基準・審査主体を策定・指名しない。承認済み [review-approval-rules.md](review-approval-rules.md) 本体を改定しない。rental-car / inbound の成果物へ適用しない。適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (コントラスト比は概算・依頼元/シート値の記録。白文字例外・在庫 error は AA 未達を明示する)。GitHub の approval・merge を設計承認・判断と同一視しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §24 である (Wiki は非正本)。

---

## 25. 国内レンタカー (rental-car) DS 0.3.0-draft — 国内宿泊 (travel) Foundation 定義体系の採用 (設計承認・影響度・現在判断) の記録

- 種別: 国内レンタカー (rental-car) の Design System へ国内宿泊 (travel) 0.3.0-draft の Foundation 定義体系を採用することについて Web部責任者が示した現在判断・改訂着手の設計承認・影響度判定の記録。契機は Claude Design のハンドオフバンドル「国内レンタカーのデザインシステム構築」(`design_handoff_rental-car-ds/`・2026-08-19 作成) による反映依頼。上記 §1〜§24 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§24 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。現在判断と過去の provenance を区別する。GitHub の approval・merge を判断・設計承認と同一視しない。`TVL-NNNN` は ADR 正本が Repository 内に不在であるため、本記録および rental-car の新規文書で現在の仕様根拠として参照しない。仮色 (実色値未取得) は placeholder として bind し発明しない。**Foundation 採用の方向の判断日 (2026-08-18)・ハンドオフバンドルの作成日 (2026-08-19)・本 Repository への反映日 (2026-08-20) は別の事象として区別する**。

### 25-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | rental-car DS 0.3.0-draft への改訂 = `primitive.rental-car.json` / `semantic.rental-car.json` の全置換・`components.md` の全置換・`design.md` の Foundation 記述 (カラー・タイポ・スペーシング・角丸・BP・アイコン・オーバーレイ) の改訂・`labels-tags.rental-car.md` と `migration-map.md` の新設・`services/rental-car/README.md` の版表記と読み順の更新 |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 方向の判断日 | 2026-08-18 (Web部責任者「国内宿泊で新たに定義されたものを適用する」) |
| 改訂着手の承認日 | 2026-08-20 |
| 承認主体 | Web部責任者 |
| 根拠 | 適用の方向は 2026-08-18 の判断で確定済。travel 0.3.0-draft の Foundation は本 Repository の `services/travel/design-system/{primitive,semantic}.travel.json` に実在し (`color.scheme.main` / `sub`・`#2c50c8` / `#4845d4`)、採用対象の定義体系が確認できる。rental-car 側は 0.2.x 系のまま主色 3 候補が未確定 (Q1) であり、本改訂はその未確定を解消する |
| 適用範囲 | **国内レンタカー (rental-car) に限定**。inbound・3DS 横断へは自動適用しない |

### 25-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **高** (判定者 = Web部責任者・判定日 2026-08-20・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定 = **Web部責任者 および チーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11) |
| 判定理由 (Web部責任者) | 本改訂は Foundation を全面置換し、主色が赤系 3 候補からロイヤル `#2C50C8` へ変わる。primitive / semantic の token 値・`components.md` の Component 定義・version に及び、`design.md` に節を新設するため、§8 の編集的訂正 carve-out (意味を変えない字句の修正) の対象外である。§24-2 (travel ラベル・タグ実装) も高判定だった。高/低の一般的な明文判定基準は未整備であり推測・補完しない (同 §8・§21) |

### 25-3. 取得した現在判断 (カテゴリ別)

| カテゴリ | 取得した判断 (2026-08-18 の方向・2026-08-20 時点の現在判断) |
| --- | --- |
| 配色の構造 | 共有ファウンデーション (白・グレー・テキスト・境界) + ブランド 2 スキームの二層。既定 = main (ロイヤル `#2C50C8`)・sub (インディゴ `#4845D4`) は第 2 候補。**いずれを正式採用するかは未決** |
| 役割色 | per-scheme とする。success = 主色 / link = 主色 / error・特集アクセント・評価色はスキーム別。いずれかのスキームが正式採用された時点で共通化する |
| 独立性 | 3 独立 DS の原則 (P1/ADR-0022) は**維持する**。採用するのは travel の**定義体系**であり、値は rental-car のファイルに独立して持つ。travel のファイルを参照・共有しない |
| 廃止値 | 赤 3 候補 (`#9E2334` / `#9B2030` / `#9F1E30`)・紺 `#283593`・link `#0050a0` と hover `#06f`・CTA 緑 `#43A047`・`$tocooBlue` `#2B4B65`・マスクのグレー板 `#7F7F7F`・`.cat-label` の分類色 (`#060` / `#C90`) と尾 `#8C4801`・5px 刻みユーティリティ・本文 15px / lh 1.4・Bootstrap 残骸 `#007BFF`。実装の事実値としてのみ `migration-map.md` の左列に残し、DS の正値としない |
| 旧 Q 論点の解消 | Q1 (主色赤の正値 3 候補)・Q2 (テキスト主色)・Q3 (base unit = 5px 系)・Q4 (root 基準・本文 15px)・Q8 (アイコン体系) は本判断により**解消**する。Q5 (breakpoint) は 2026-07-24 決定済で `$status` を bound へ昇格する |
| ボタン形状 | **pill** (`radius.action`) とする。旧 R-01 (角丸 4px を国内レンタカー固有の意匠として維持する) は**廃止**する。縦グラデ・emboss 影・text-shadow も廃止 |
| 書体 | 明朝 (Noto Serif JP) + ゴシック (LINE Seed JP・フォールバック Noto Sans JP) の 2 書体。本文 1rem / lh 1.8 |
| ラベル・タグ | travel の定義シート (A〜H) を継承し、レンタカーの用途へ割り当てる。器は sm (20px) / md (24px) の 2 段。**要追加トークン 5 件** (`label.*` の器・`membership.paid`/`free`・`accent.campaignTint`/`campaignInk`・`label.stock`・`tag.neutral`) は未追加であり `🚧` を伝播させる。C 特集の用途色・E2 販売終了の値は travel と同じく**据え置き** |
| オーバーレイ | drawer を既定形態とする記述は**本書 (rental-car `design.md` / `components.md`) の提案**である。3 DS 横断の Modal 実装基盤 (本記録 §1 Q9) は未決のまま。BottomSheet / Popover は**未承認の拡張候補**として本文から分離して書く |
| 実査待ち (§14) | accent 濃色段の実色 (仮色 `#8A2E11`)・ResultCard の実 px・料金列の実ラベル・モーション実値・シャドウ実値・ロゴ素材は未取得であり `🚧` のまま置く。記憶からの再構築は行わない |

### 25-4. §24 との関係・未決事項

- §24-1 は適用範囲を「**国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない」とし、同記録の Does Not Authorize も「rental-car / inbound の成果物へ適用しない」と述べている。本 §25 は、その**自動適用ではなく**、rental-car について別途取得した判断として記録するものである。§24 の判断内容・適用範囲は変更しない。
- ラベル・タグ定義は travel の定義シート (A〜H) を**継承**するが、用途の割当・D4 の廃止・B-2 の既定非表示は rental-car 固有の判断である。
- **判断後も未決・未確認の事項**: スキームの正式採用 (main / sub)／accent 濃色段の実色値 (実査待ち・§14)／accent の帰属 (B 有料会員 / C 特集)／A 割引率の逆色面 + 白文字 (2.78:1・AA 未達) を許容する例外条項の明文化／E2 満車・受付終了の値 (方向のみ)／F メリット色とリンクの見分け／ResultCard の実 px・料金列の実ラベル／モーション・シャドウの実値／ロゴ素材・写真選定基準／サービス識別子 `rental-car` の正式化 (確認事項 #8)／Filter の件数算出仕様／3 DS 横断の Modal 実装基盤 (§1 Q9)。いずれも本記録では決定・補完しない。

**Does Not Decide / Does Not Authorize**: 本記録は main / sub いずれのスキームを正式採用するかを決定しない。accent 濃色段の実色値・ResultCard の実 px・料金列の実ラベル・モーション・シャドウの実値を発明・確定しない (`🚧` placeholder)。C 特集の用途色・E2 販売終了の値を確定しない (据え置き)。A 割引率の白文字例外を rental-car の規則として明文化・完了させない (例外条項の明文化は未了)。drawer を 3 DS 横断の Modal 実装基盤として確定せず、BottomSheet / Popover を承認しない。サービス識別子 `rental-car` を正式識別子として確定しない (確認事項 #8)。承認済み [review-approval-rules.md](review-approval-rules.md) 本体を改定しない。§24 の適用範囲・判断内容を変更しない。travel / inbound の成果物へ適用しない。適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない (コントラスト比は概算・ハンドオフ元の記録)。GitHub の approval・merge を設計承認・判断と同一視しない。本記録に関する Wiki 記載があっても、本判断の正本は本 §25 である (Wiki は非正本)。

---

## 26. Travel 文書レベル見出しの書体選択 (要素ではなく役割で選ぶ) の明文化 — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: 国内宿泊 (travel) `services/travel/design-system/design.md` §3.1 について、文書レベルの見出しの書体を要素 (`h1`〜`h6`) ではなく役割で選ぶことを明文化する改訂に対し、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機は [Issue #163](https://github.com/tocoo/coocom-design-system/issues/163) (実装側 `tocoo/tocoo_travel` の Issue `6980` で顕在化した論点の起票)。上記 §1〜§25 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§25 の各記録は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。

### 26-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | `services/travel/design-system/design.md` §3.1 への [決定] 2 行・[事実] 1 行の追加 (①本節が定めるのは既定値であり要素と書体の対応を固定しないこと・書体の選択は役割で決まり要素名では決まらないこと・役割が §3 の Display・Hero・特集・詳細施設名にあたる場合は `h1` であっても `font.display.family` を明示的に選択してよいこと、②明示的な選択の結果サイズ・太さ・行間が既定から外れる場合は当該画面仕様または当該 Component 仕様へ明示記載すること、③個々の見出しの該当判断は同書では行わないこと)、および §3 の表の Display 行への参照追記・未確定事項の一覧への 1 行追加 |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-04 |
| 承認主体 | Web部責任者 |
| 根拠 | 現行 §3.1 は明朝を「明示的に選択する書体」と述べており本改訂は明朝の使用可否を変更しない。要素と書体の対応を固定しない旨が明文化されていないため、実装側で `h1` への明朝適用の可否判断が画面ごとに発生している ([Issue #163](https://github.com/tocoo/coocom-design-system/issues/163) 背景)。既定と禁止の区別を明文化することで、規則の内容を変えずに一意に読めるようにする |
| 適用範囲 | **国内宿泊 (travel) の `design.md` に限定**。rental-car・inbound・3DS 横断へは自動適用しない |
| 是正後の承認対象 (2026-09-05) | 上記の承認対象は 2026-09-04 時点のものであり、PR [#164](https://github.com/tocoo/coocom-design-system/pull/164) のコードレビュー (2 回) を経て次のとおり変わった。**§3.1 は [決定] 4 行・[事実] 1 行**となり、当初の②「サイズ・太さ・行間が既定から外れる場合は当該**画面仕様**または当該 Component 仕様へ明示記載」は**撤回**して「原則として認めない。認めるのは利用目的とデザイン上の必然性が明確に示され**承認 (承認主体 = Web部責任者) を得た場合**に限る」へ置き換え、あわせて「**サイズ・太さ・行間の既定は書体の選択と独立**」を追加した。Component が既定から外れる値を必要とする場合の扱いは、§3.1 が既に定める [決定] (当該 Component 仕様へ明示記載) に一本化した。**§3 の表**は Display 行への参照追記に加え、h1〜h6 行への注記 (「既定。役割による書体の選択は §3.1」)、Display 行への「特集」の補い、Display 行への太さの優先関係の注記を行った。本欄は 26-3 の現在判断 (2026-09-05) を承認対象の記述へ反映したものであり、**承認種別・承認日 (2026-09-04)・承認主体・適用範囲は変更しない** |

### 26-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **低** (判定者 = Web部責任者・判定日 2026-09-04・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定 = **Web部レビュー担当者**。同 §11 により、そのレビューが反映確定の前提となる |
| 判定の位置づけ | 本判定は本件に限る都度判断であり、§8 の編集的訂正 carve-out の適用でも、一般的な高／低の内容基準の確定でもない |

### 26-3. 取得した現在判断 (2026-09-04・2026-09-05)

| 論点 | 取得した判断 |
| --- | --- |
| 改訂着手 | **承認する**。Issue #163 のスコープ 1〜3 に限定して §3.1 へ [決定] を追加する |
| 既定値そのもの | **変更しない**。`h1` = `4xl` 2.5rem / 太さ 700 / 行間 1.3・既定書体 = ゴシック (`font.heading.family`) は既定として維持する |
| 明朝を明示的に選択した場合のウェイト | **§3.1 には書かない** (書体の選択規則のみを明文化する)。§3 の表の「Noto Serif JP (明朝) 500–600」の記述は不変であり、実装側のウェイト供給の差異は実装 Repository `tocoo/tocoo_travel` 側で追跡する |
| 明示的に選択した書体と既定値の関係 (2026-09-05) | **サイズ・太さ・行間の既定は書体の選択と独立**とする。明朝を明示的に選択しても `h1` の太さ 700 を含む §3.1 の既定がそのまま適用され、§3 の表の「500–600」は書体の**用途に関する記述**であって太さの既定を置き換えない。`h1` の太さ 700 の定義自体は変更しない。**但し書き**: 同一のウェイト値でも書体により見えの太さが異なる側面があることを認識のうえで、当面は本扱いとする。取得の契機 = PR #164 のコードレビュー指摘 (§3.1 の 700 と §3 の 500–600 のいずれが規範かが本書内で読み取れない) |
| 既定から外れる値の可否 (2026-09-05) | **原則として認めない**。サイズ・太さ・行間は §3.1 の既定に従う。認めるのは、**利用目的とデザイン上の必然性が明確に示され、承認を得た場合**に限る (**承認主体 = Web部責任者**)。`design.md` §8.3 の**適用外 (クリエイティブ)** にあたるものや LP はその**例**であり、**許容される場面をこれらに限定しない** (閉じた列挙にしない)。§8.3 の適用外にあたる場合は、あわせて同節の扱い (必然性・制約・目的の提示／カラー厳守／品質下限／事前の宣言) に従う。**Component** が既定から外れる値を必要とする場合は、§3.1 が既に定める「当該 Component 仕様へ明示記載」に一本化し、別途の承認は要求しない (Component 仕様は Design System の成果物であり、記載の時点で本 Repository の改訂手続 = 影響度判定・内容レビューを通るため)。「当該**画面仕様**に明示的に記載する」という当初文言は、例外の基準を示さないまま記載先を上流成果物に求めるものであったため撤回した。取得の契機 = PR [#164](https://github.com/tocoo/coocom-design-system/pull/164) のコードレビュー (1 回目 = 記載先の「画面仕様」が [../services/travel/screen-requirements/README.md](../services/travel/screen-requirements/README.md) §15 のとおり多くが未定義で記載主体も未定／2 回目 = 承認主体が本書内に存在せず、(a)(b) の閉じた列挙が §8.3 の適用外の列挙 (LP を含まない) と矛盾する) |

### 26-4. 本記録が決定しないこと

- 個々の画面の見出しが Display・Hero・特集・詳細施設名にあたるか否かの該当判断 (画面別の情報構造は Screen Requirements 側の課題)。
- 新しいサイズ値・ウェイト値・行間値 (primitive) の追加、`font.heading.*` / `font.display.*` の `$value`・参照先・`$status` の変更。
- §3 の「Noto Serif JP (明朝) 500–600」の記述変更、および明朝のウェイト供給 (実装側) の解決。
- 実装 Repository (`tocoo/tocoo_travel`) 側の適用作業、および文書レベルの見出し既定 (§3.1) を実装へ反映する範囲・順序・期限。
- rental-car・inbound の成果物への適用。

---

## 27. Travel C カテゴリ・特集ラベルの用途色と accent の帰属 (B 有料会員 / C 特集) の確定 — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: 国内宿泊 (travel) の `Card.slot.badge` C カテゴリ・特集ラベルについて、§24 で据え置いた用途色と、その前提であった **accent の帰属 (B 有料会員 / C 特集)** を確定することに対し、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機は [Issue #162](https://github.com/tocoo/coocom-design-system/issues/162) (実装側 `tocoo/tocoo_travel` の Issue `6953` で顕在化した、用途色未確定に起因する実装 3 分岐の起票)。上記 §1〜§26 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§26 の各記録は変更しない。**§13 (b2)・§19 (会員限定ラベルの用途区別)・§20 (白文字例外の方向)・§24 (ラベル・タグ定義 A〜H の実装) の本体は改定せず**、本 §27 を現在判断として扱う (§10 / §11 と同じ区別)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。

### 27-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | ①[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) への用途色 `color.label.category` (`surface` / `text` / `icon` / `border` の 4 件) の追加、②[../services/travel/design-system/components.md](../services/travel/design-system/components.md) `Card.slot.badge` の「ラベル種別と用途色」C 行の据え置き記述の置換と白文字例外条項の適用範囲の縮小、③[../services/travel/design-system/design.md](../services/travel/design-system/design.md) §2 用途要約表への 1 行追加・§2.1 検証表への 1 行追加・§2.1「非操作の点的ラベルに限る白文字の例外」の適用範囲の縮小と同節の見出しの「A 割引率ラベルに限る白文字の例外」への改称・未確定事項の一覧の更新 (C 用途色を解決へ・派生する未定義事項 1 行の追加) |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-05 |
| 承認主体 | Web部責任者 |
| 根拠 | §24 (2026-08-10) は C 特集の用途色を「accent の帰属が B / C で未定」を理由に据え置いた。その結果、実装側 (`tocoo/tocoo_travel`) で C 相当のラベルが 3 通りに分岐している ([Issue #162](https://github.com/tocoo/coocom-design-system/issues/162) 背景 — 宿泊トップ `.hero-label--category` = 白面 + 濃文字 + accent アイコン (仮決定トークン経由) / 施設詳細 `.hd-clabel` = 同配色だがトークンを介さない個別指定 / サイト共通 `.gl-label--campaign` = accent 濃色面 + 白文字)。帰属を確定し用途色を DS 側に置くことで、実装側はこの 3 通りを 1 つに寄せられる |
| 適用範囲 | **国内宿泊 (travel) の `design.md` / `components.md` / `semantic.travel.json` に限定**。rental-car・inbound・3DS 横断へは自動適用しない (rental-car の C1 / C2 は [../services/rental-car/design-system/labels-tags.rental-car.md](../services/rental-car/design-system/labels-tags.rental-car.md) のとおり据え置きのまま) |

### 27-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **高** (判定者 = Web部責任者・判定日 2026-09-05・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定 = **Web部責任者およびチーフデザイナー**。同 §11 により、そのレビューが反映確定の前提となる |
| 判定の位置づけ | 本判定は本件に限る都度判断であり、§8 の編集的訂正 carve-out の適用でも、一般的な高／低の内容基準の確定でもない。用途色トークンの新設と面色規則の帰属確定を伴い、実装 3 箇所の配色を 1 つへ寄せる指示になるため、§24 (影響度 = 高) と同水準とした |

### 27-3. 取得した現在判断 (2026-09-05)

| 論点 | 取得した判断 |
| --- | --- |
| ⓐ accent の帰属 (B 有料会員 / C 特集) | **面と点で役割分離する**。accent を**面**として持つのは **B 会員種別** (`color.membership.paid` = accent 淡色段 `campaignTint` / `campaignInk`) のみとし、**C カテゴリ・特集**は accent を**アイコン (点)** として持つ。C の面は白 (`color.surface.default`) とし accent で塗らない。§19 (2026-08-04) が記した「基本 = neutral 面 / 特集紐づき = accent 面 / 例外 = inverse 面」のうち「特集紐づき = accent 面」は、**面ではなく点 (アイコン) で紐づく**形へ本記録で確定する (§19 本体は改定しない)。§24 で実装済みの `color.membership.paid` の値・参照先・`$status` は**変更しない** |
| ⓑ C の用途色 `color.label.category` の semantic 定義 | **定義する**。`color.label.category.surface` = `{color.surface.default}` (#FFFFFF)・`.text` = `{color.text.strong}` (#212121)・`.icon` = `{color.accent.campaign}` (#E4572E) の 3 件を `semantic.travel.json` に追加する。いずれも**既存 semantic への参照**であり、新しい色値・新しい primitive は追加しない。実装側がトークンを介さず個別指定している箇所 (`.hd-clabel`) が仮決定の変更に追従しない問題を、単一の参照名を与えることで解消する |
| ⓒ 12px (`label.fontSize.sm`) ラベルでの成立解 | **白面 × `color.text.strong` = ≈16.10:1 で成立する** (本 Repository で実測)。サイズ・ウェイトの条件を伴わないため、C については (i) (ii) の代替 2 択 (① neutral dark 面 `color.surface.inverse` / ② accent 淡色面 `campaignTint` + `campaignInk`) を要しない。② は accent 濃色段が 🚧 仮色で 4.5:1 未検証だが、C はこれに依存しない。accent アイコン (#E4572E) は白面上 ≈3.68:1 で、**非テキスト UI 要素の 3:1 は満たすが通常テキスト 4.5:1 には達しない**ため、アイコンに限り用いて文字色・面色には用いない |
| ⓓ サイト共通 `.gl-label--campaign` (accent 濃色面 + 白文字 12px) の扱いと白文字例外との整合 | **C の用途色へ寄せ、白文字例外の対象外と明記する**。実装 3 分岐すべてを `color.label.category` へ統一し、C に campaign accent 面 + 白文字を用いない。あわせて `design.md` §2.1「非操作の点的ラベルに限る白文字の例外」(本 Task で「A 割引率ラベルに限る白文字の例外」へ改称) の**適用範囲を縮小**する — 用途を **A 割引率ラベル (`color.label.discount`) に限り**、面を **scheme 逆色 (`color.scheme.*.inverse`) に限る** (campaign accent 面 + 白文字を例外から外す)。**取得の契機** = 縮小前の §2.1 は用途例に「カテゴリラベル」を、面に campaign accent を含め「サイズ・ウェイトは不問」としており、`components.md` `Card.slot.badge` の「(i) (ii) では campaign accent 面を使用しない・代替は 2 択」と読みが割れていた (本 Repository の実測。二通りの読みが成立し、`.gl-label--campaign` が規則違反か否かの判定が分かれる状態だった)。本縮小により campaign accent 面の (i) (ii) 白文字禁止は例外なく維持される。方向を記録した §20 本体は改定せず、本 §27 を現在判断とする |
| ⓕ 白系の面の上に置く C ラベルの分離手段 (2026-09-05 追加取得・Task 009-60R) | **枠線を引く**。**白系の面 (`color.surface.default` `#FFFFFF` / `color.surface.subtle` `#F9F9F9`) の上に置く場合にのみ**、`color.label.category.border` = `{color.border.default}` (`#CCCCCC`) の枠線を `border.width.thin` (1px) で引く。**写真の上・有色面の上では枠線を引かず**面のみで分離する (影・スクリムは用いない = ラベル・タグ定義シートと整合)。**取得の契機** = C の面を白と確定した結果、白いカード面・`surface.subtle` の上では面のみで境界が生じない (白 × 白 = 1.00:1・白 × `surface.subtle` = 1.05:1・本 Repository で実測)。**値の選定** = 既存 border 3 段の白面上コントラストは `subtle` `#e0e0e0` 1.32:1 / `default` `#cccccc` 1.61:1 / `strong` `#bcbcbc` 1.90:1 で、**非テキスト UI 要素の 3:1 に達する既存の border トークンは存在しない** (同実測)。DS 既定の境界線である `color.border.default` を採り、**3:1 未達を明示する** (適合宣言は行わない)。枠線は分離の補助であり、ラベルの識別は文字 (≈16.10:1) が担う。新しい色値・新しい primitive は追加しない |
| ⓔ C のウェイト | `components.md` `Card.slot.badge` の既存規則「面のあるラベルは `label.weight.emphasis` (700)」に従い **700** とする (C は白面という面を持つため)。`label.weight.emphasis` の `$description` が置いていた「C 特集は accent 帰属確定後に面を持つ場合」という条件付き記述を、確定後の記述へ是正する。新しいウェイト値は追加しない |

### 27-4. 本記録が決定しないこと

- accent 濃色段 (`orange.800` `#8A2E11`) ・サブスキーム `coral` 2 段の実色値 (🚧 仮色・実査待ち・§14・§24)。b2 (accent 淡色面 + 濃色文字) の 4.5:1 成立検証は実色値確定後のままとし、`color.membership.paid` / `color.accent.campaignTint` / `campaignInk` の `$status` (placeholder) を昇格しない。
- **C ラベルのアイコンのサイズ**。本記録はアイコンの色 (`color.label.category.icon`) を確定するが、サイズを定めない。アイコン体系のサイズスケール `iconSize.sm〜xl` の最小段は 16px で、ラベルの器 sm (高さ `label.height.sm` 20px・文字 `label.fontSize.sm` 12px) に当てる値は `design.md`・`components.md` のいずれにも無い ([../services/travel/design-system/preview.travel.html](../services/travel/design-system/preview.travel.html) の見本は継承の 12px で描いておりスケール外の例示である)。`design.md` 未確定事項の一覧へ 1 行として記録する。
- 画像・グラデーションを面とする場合の scrim の要否 (依頼 E-1)。ⓕ は**単色の白系の面**の上での分離手段を定めるのみで、写真・グラデーション上の扱いは従前どおり別論点とする。
- E2 販売終了の値・F メリット色とリンクの見分け・H グラデーション審査基準/審査主体 (§24-4 の未決事項)。
- スキームの正式採用 (main / sub)、副色 (sub) 文脈での C の用途色の個別定義 (`color.label.category` は DS 既定ビルド = メインの値を参照する既存の per-scheme 方針に従う)。
- 実装 Repository (`tocoo/tocoo_travel`) 側の適用作業・是正の範囲と時期 (Issue `6953` を含む)。本記録は DS 側の用途色を確定するのみで、実装側の改修計画を決定しない。
- rental-car・inbound の成果物への適用 (rental-car の C1 / C2 は据え置きのまま。適用する場合は §25 と同様に別途取得した判断として記録する)。
- 適用規格・達成レベルの正式確定・適合判定・適合宣言 (コントラスト比は概算の記録)。

## 28. Travel ブレークポイントごとの文書レベル見出しのサイズ段 (既定の適用幅・狭い幅での段下げ・4 の倍数規則) の確定 — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: 国内宿泊 (travel) の `design.md` §3.1 が定める文書レベル見出しの既定について、**どの viewport 幅に対する値か**と**狭い幅でサイズ段を下げることの可否と規則**を確定することに対し、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機は [Issue #168](https://github.com/tocoo/coocom-design-system/issues/168)。上記 §1〜§27 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§27 の各記録は変更しない。**§12 (配布スナップショットと SOT の乖離・本記録時点の Fact) の表の 10 行目 `font.heading.h5Size` = `{typography.size.lg}` は、`main` `cbc19c6` 時点の記録として遡及変更しない**。§26 (文書レベル見出しの書体選択) の本体も改定せず、本 §28 を現在判断として扱う (§10 / §11 と同じ区別)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。

### 28-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | ①[../services/travel/design-system/design.md](../services/travel/design-system/design.md) §3.1 の割当表への幅 2 列の追加・`h5` の参照先変更・[決定] 群の追加、②同 §3 の表の見出し行と §4 のブレークポイント行への注記、③同 未確定事項の一覧の更新 (本論点の解決行の追加・`h6` 行の `h5` への拡大・2 行の新規追加)、④[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) の `font.heading.h5Size` の `$value` 変更と `$meta.notes` の同期、⑤[../services/travel/design-system/components.md](../services/travel/design-system/components.md) 共通事項の見出し割当記述の同期、⑥[../services/travel/design-system/preview.travel.html](../services/travel/design-system/preview.travel.html) の見出し表を幅追従へ変更 (本ページ初の `@media`) |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-07 |
| 承認主体 | Web部責任者 |
| 根拠 | §3.1 の既定 (`h1` 2.5rem 〜 `h6` 1rem) は viewport 幅の限定が付かない単一値として定義され、§4 の breakpoint・代表 viewport と関係づける記述が正本に無かった。このため狭い幅でサイズ段を下げる実装が §3.1 の「既定から外れる」(原則不許可・要承認) にあたるのか下流の裁量なのかが正本から一意に決まらず、実装側 (`tocoo/tocoo_travel` `origin/dev-ds` `e664e5802`・2026-09-04) では既に 8 ファイルが media query 内で `font-size` を宣言し、境界も段の刻みも画面ごとに割れたまま積み上がっていた (本 Repository で実測) |
| 適用範囲 | **国内宿泊 (travel) の `design.md` / `components.md` / `semantic.travel.json` / `preview.travel.html` に限定**。rental-car・inbound・3DS 横断へは自動適用しない |

### 28-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **高** (判定者 = Web部責任者・判定日 2026-09-07・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定 = **Web部責任者およびチーフデザイナー**。同 §11 により、そのレビューが反映確定の前提となる |
| 判定の位置づけ | 本判定は本件に限る都度判断であり、§8 の編集的訂正 carve-out の適用でも、一般的な高／低の内容基準の確定でもない。既に bound 済みの semantic トークン (`font.heading.h5Size`) の参照先を変更し、実装側の既存宣言の適合／非適合を左右するため、§26 (見出しの書体選択・影響度 = 高) と同水準とした |

### 28-3. 取得した現在判断 (2026-09-07)

| 論点 | 取得した判断 |
| --- | --- |
| ⓐ 規則の形 | **一意の段下げ表を DS が定める**。どの幅でどの段を用いるかを DS が一意に決め、画面ごとに境界・段数を選ぶ裁量を与えない。範囲制約のみを定めて画面に委ねる形は採らない (起票の契機である「共通規則が無い」状態が実質的に残るため) |
| ⓑ §3.1 の既定が適用される幅と段下げ表 | **既定は `breakpoint.lg` (1024px) 以上に適用される値**とし、1024px 未満は次の段を用いる — `h1` `3xl` 2rem / `h2` `2xl` 1.5rem / `h3` `xl` 1.25rem / `h4`・`h5`・`h6` `md` 1rem。**段を移す境界は 1024px の 1 つのみ**とし、`breakpoint.sm` (640px) / `md` (768px) / `xl` (1280px) では変えない。**根拠** = §4 の代表 viewport `390 / 768 / 1280 / 1440px` を 1024px がちょうど 2 対 2 に分ける (狭 = 390・768 / 広 = 1280・1440)。実装側の確定 6 例のうち Hero 施設名 2 例 (`ultra_plan_s.scss` `.up-hotelname` / `ultra_market_s.scss` `.um-hero__name`) が本表と完全一致し、境界を 768px に置く 4 例は一致しない (本 Repository で実測。実装側の是正は本記録の範囲外) |
| ⓒ 段下げと §3.1 の例外条項との関係 | **本表の範囲内での段下げは「既定から外れる」に該当しない**。したがって画面ごとの都度の承認を要しない。承認 (承認主体 = Web部責任者) を要するのは本表の外に出る場合に限る — 境界を `breakpoint.lg` 以外に置く／本表と異なる段を用いる／§3 のスケールに無い値を用いる／幅が広がるとサイズが小さくなる。§26-3 が記録した「既定から外れる値は原則として認めない」は本表を含む既定に対して引き続き有効であり、本記録はその適用対象を幅の軸へ拡張したものである (§26 本体は改定しない) |
| ⓓ `h5` の参照先 (`lg` 18px の扱い) | **`font.heading.h5Size` の参照先を `{typography.size.lg}` (1.125rem・18px) から `{typography.size.md}` (1rem・16px) へ変更する**。**根拠** = 文書レベルの見出しには実寸が 4 の倍数である段のみを用いる規則を新設したことによる。`typography.size` 9 段のうち 4 の倍数でないのは `sm` (14px) と `lg` (18px) の 2 段のみで、`spacing` 全 11 段・`iconSize` 全 4 段・`breakpoint` 全 4 段・`radius` の実寸 3 段 (`full` 9999px は pill の番兵値) はいずれも 4 の倍数である (本 Repository で実測)。`lg` は、`h1` を `4xl` (40px) に置いた結果 16px 以上かつ 4 の倍数の段が 16 / 20 / 24 / 32 / 40 の 5 つしか使えず 6 レベルに 1 つ足りなかったために用いられていた段であり、変更前に同段を参照する semantic トークンは `font.heading.h5Size` の 1 件のみであった (同実測)。**帰結を明示する** — `h5` と `h6` がいずれの幅でも同値 (1rem) となり見出しのサイズ段は実質 5 段になる。1024px 未満では `h4` も 1rem となり本文 (`font.body.size` 1rem) とも同値になるため、狭い幅で寸法によって区別できる見出しは `h1` / `h2` / `h3` の 3 段である。**代替案として検討し採らなかったもの** = `h1` に `display-lg` (48px) を用いる 6 段構成 (48 / 40 / 32 / 24 / 20 / 16)。4px 系のまま 6 レベルすべてが識別可能になるが、`display-lg` は §3 が Display・Hero・特集・詳細施設名に割り当てている段で用途が重なり、実装反映時の実寸変化も最大 (24px → 48px) になるため |
| ⓔ 4 の倍数規則の適用範囲 (`sm` 14px の扱い) | **見出しの段からのみ排除し、`sm` (14px) は現状維持とする**。同段は `label.fontSize.md` / `label.numberSize.sm` として §8.1 の「数字は `%OFF` より §3 のスケールで 1 段上」の規則および `label.*` の器トークンに組み込まれ bound 確定済み (Task 009-48) であり、実装でも 143 箇所で参照されている (本 Repository で実測)。**TVL-0002 (4px 系) の適用範囲を `typography` 全体へ拡げない** — 同 ADR の記述 (`design.md` §4) は引き続きスペーシングを対象とする。本規則は「文書レベルの見出しに用いる段」のみを制限する |
| ⓕ [alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8J との優先関係 | **見出しのサイズ段については §3.1 が上位**とし、同 §8J (Task 009-17・2026-07-23) が「可変/レスポンシブタイポグラフィ・PC/SP 別 font size・モバイル具体値」を UI・Implementation 下流課題へ分類したことによる下流の裁量は、§3.1 の表の内側でのみ成立する (表が幅ごとの値を一意に定めるため、下流が段を選ぶ余地は残らない)。**§8J の分類そのものは変更しない** — Task 009-17 時点の記録として保持し、見出しのサイズ段以外 (行数制限・行長・改行/禁則・truncation/ellipsis/line-clamp・overflow・Component 内テキスト制約・文字数) には引き続き同節の分類が有効である |
| ⓖ 見本ページでの確認手段 | **`preview.travel.html` の見出し表を幅追従にする**。`@media (min-width: 1024px)` で見本欄の `font-size` を切り替え (本ページで初の `@media`。従来は 0 件で幅を変えても文字サイズが変化しなかった)、「既定」「狭い幅」の 2 列と現在どちらを表示しているかの表示を設ける。規則の記述は置かず正本 (`design.md` §3.1) を参照する既存方針を維持する |

### 28-4. 本記録が決定しないこと

- **幅ごとの値を持つ semantic トークンの新設**。狭い幅の段は `design.md` §3.1 の表で既存 primitive 段 (`3xl` / `2xl` / `xl` / `md`) への割当として示すにとどめ、`font.heading.*` に breakpoint 軸を持ち込まない。新しい primitive (サイズ・行間・ウェイト) も追加しない。`typography.size.lg` の primitive 自体は削除せず値・`$status` とも不変。
- **§3・§3.1 の他の既定値**。`h1` `4xl` 2.5rem / `h2` `3xl` 2rem / `h3` `2xl` 1.5rem / `h4` `xl` 1.25rem / `h6` `md` 1rem・太さ 700・行間 1.3・書体の選択規則 (§26) は変更しない。`display-lg` (48px) の用途区分も変更しない。
- **§4 の breakpoint 値・代表 viewport 値**。`640 / 768 / 1024 / 1280px` (TVL-0004・3DS 共通値として再認定済み) と `390 / 768 / 1280 / 1440px` は不変。本記録は既存の `breakpoint.lg` を見出しの境界として選定するのみ。
- **`h5` / `h6` と本文 (いずれも 1rem) の区別根拠、および `h5` と `h6` の相互の区別根拠**。本文のウェイトが正本上不在でウェイトによる区別が成立しないことは従前どおりで、`design.md` 未確定事項の一覧に対象を `h5` へ拡大して起票する。
- **見出し以外の `typography` 用途へ 4 の倍数規則を及ぼすか**。ⓔ のとおり見出しに限定し、`sm` (14px) を含む全体の整合は未判定として `design.md` 未確定事項の一覧へ起票する。
- **実装 Repository (`tocoo/tocoo_travel`) 側の適用作業・既存の非適合箇所の是正**。境界を 768px に置く 4 例 (`.up-hsec` / `.up-h3` / `.up-h4` / `.hd-overview__name`) と、§3 のスケールに無い値を用いる 1 例 (`spa/top_spa.scss` L313 の `calc(--typography-size-2xl + --spacing-1)` = 28px) の是正の範囲・順序・期限は実装 Repository 側の課題。`design.md` 未確定事項の一覧へ起票する。
- **§3.1 の既定を実装へ反映する範囲・順序・期限**。既存の未確定事項として保持する。
- **画面別の見出し階層・semantic role の割当** (どの画面のどのコンテンツを `h1` / `h2` とするか)。§3.1 冒頭のとおり Screen Requirements 側の課題であり、§8J.4 の分類も変更しない。
- **適用規格・達成レベルの正式確定・適合判定・適合宣言**。
- **rental-car・inbound の成果物への適用**。適用する場合は §25 と同様に別途取得した判断として記録する。

---

## 29. 国内レンタカー (rental-car) DS — 国内宿泊 (travel) 最新版 (Task 009-58〜009-62) の適用 — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: 国内レンタカー (rental-car) の Design System へ、国内宿泊 (travel) の最新版 (Task 009-58〜009-62 時点) の定義体系を適用することに対し、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機は [Issue #170](https://github.com/tocoo/coocom-design-system/issues/170)。上記 §1〜§28 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§28 の各記録は変更しない。
- **本記録は §25〜§28 からの自動適用ではない。** §26 / §27 / §28 はいずれも適用範囲を「国内宿泊 (travel) に限定。rental-car・inbound・3DS 横断へは自動適用しない」と明記しており、§25 も「§24 の自動適用ではなく rental-car について別途取得した判断」として記録されている。本 §29 も同じ形で、**rental-car について別途取得した判断**として記録する。§24・§26・§27・§28 の判断内容・適用範囲は変更しない。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。`TVL-NNNN` は ADR 正本が Repository 内に不在であるため、本記録および rental-car の文書で現在の仕様根拠として参照しない。仮色 (実色値未取得) は placeholder として bind し発明しない。

### 29-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | ①[../services/rental-car/design-system/semantic.rental-car.json](../services/rental-car/design-system/semantic.rental-car.json) の部分更新 (**39 件追加・`radius.input` 1 件削除・`font.heading.h3Size` の参照先変更**)、②[../services/rental-car/design-system/primitive.rental-car.json](../services/rental-car/design-system/primitive.rental-car.json) の部分更新 (accent の淡色段・濃色段 **4 件追加**)、③[../services/rental-car/design-system/design.md](../services/rental-car/design-system/design.md) の部分更新 (§2.4 面と文字色・§2.5 リンク・§2.6 未入力状態の文字色・§3.1 文書レベルの見出しスケール・§7.1 Modal の表示形態・§8.1 割引率の表記規則・§8.2 予約条件の表示規則・§8.3 クリエイティブへの適用範囲の **8 節を新設**／§2.2 用途表・§2.3 品質下限・§3 タイポグラフィ・§5 角丸・§6 オーバーレイ・§7 コアコンポーネント・§9 Agent Prompt Guide・未確定事項の一覧の是正)、④[../services/rental-car/design-system/components.md](../services/rental-car/design-system/components.md) の部分更新 (§1 共通事項・Button・Input・Select・SearchForm・Label / Tag・PriceTag・Modal。**§6「拡張候補 (未承認)」を本文へ統合して廃止**し §7・§8 を繰り上げ)、⑤[../services/rental-car/design-system/labels-tags.rental-car.md](../services/rental-car/design-system/labels-tags.rental-car.md) の部分更新 (器とカテゴリのトークン参照化・**C1 の記述是正**・§4 要追加トークン表の消し込み)、⑥[../services/rental-car/design-system/preview.rental-car.html](../services/rental-car/design-system/preview.rental-car.html) の**新設** (DS 見本ページ・非正本)、⑦[../services/rental-car/design-system/README.md](../services/rental-car/design-system/README.md) の**新設** (design-system レイヤー入口文書)、⑧[../services/rental-car/README.md](../services/rental-car/README.md) の部分更新 (読み順・現在存在する成果物)、⑨`tools/gen-preview-tokens.py` の部分更新 (複数サービス対応)、⑩[../services/travel/design-system/design.md](../services/travel/design-system/design.md) の部分更新 (§2.1 代替規則 1 の記述是正 1 行と変更履歴 2 行のみ。**travel のトークンの値・参照先・`$status`・検証表の各行・[決定]・適用範囲は変更しない**) |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-07 |
| 承認主体 | Web部責任者 |
| 根拠 | rental-car が採用済みなのは **2026-08-20 時点の travel Foundation 定義体系** (§25) であり、それ以降 travel に入った確定 (§26 見出しの書体選択・§27 C カテゴリ・特集の用途色と accent の帰属・§28 幅ごとの見出しのサイズ段、および Task 009-48〜009-56 のラベル・タグ実装) が未反映である。実測した差分は semantic トークン **42 件** (travel 側のみ)・primitive **6 件** (同)・文書の節 **8 節**で、**値の食い違いは 0 件**であった。また rental-car 側には、travel 側の確定を待つ形で `🚧` を置いたままの記述 (A 割引率の例外条項が未明文化・accent の帰属が未確定・要追加トークン 6 件・主 CTA 個数制約の適用判断が未取得・BottomSheet / Popover が未承認候補) が複数あり、本適用によりこれらを解消できる |
| 適用範囲 | **国内レンタカー (rental-car) に限定**。travel・inbound・3DS 横断へは自動適用しない。**ただし承認対象⑩は travel `design.md` の記述是正**であり、travel の値・[決定]・適用範囲を変更しないことを条件に本 PR の範囲へ含める (2026-09-07・Web部責任者判断・明示取得) |

### 29-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **高** (判定者 = Web部責任者・判定日 2026-09-07・本件について明示取得)。**承認対象⑩ (travel `design.md` の記述是正) も同じく高** (判定者 = Web部責任者・判定日 2026-09-07・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定 = **Web部責任者およびチーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11) |
| 判定の位置づけ | 本判定は本件に限る都度判断であり、§8 の編集的訂正 carve-out (意味を変えない字句の修正) の適用でも、一般的な高／低の内容基準の確定でもない。semantic **39 件の追加・1 件の削除**・既に bound 済みのトークン (`font.heading.h3Size`) の**参照先変更**を伴い、`design.md` に **8 節を新設**するため carve-out の対象外である。前例として、より小さい範囲であった §25 (rental-car Foundation 定義体系の採用) も高判定であり、travel 側の §27 (用途色 4 件の追加)・§28 (semantic 1 件の参照先変更) も高判定であった |

### 29-3. 取得した現在判断 (2026-09-07)

本 Issue の起票時に取得した 7 件の判断。いずれも rental-car の既存記述・既存トークンと両立しない論点、または travel 限定と明記された判断の適用可否である。

| # | 論点 | 取得した判断 |
| --- | --- | --- |
| D-2 | `font.heading.h3Size` を `lg` (1.125rem・18px) のまま維持するか `2xl` (1.5rem・24px) へ揃えるか | **24px へ揃える**。travel と同じ段構成 (h1 40 / h2 32 / h3 24 / h4 20 / h5 16 / h6 16px) とする。**帰結**: `font.display.mdSize` (18px・車種クラス名) と `h3Size` が同値でなくなるため、旧 §3 の「同一要素へ 2 系統を割り当てない」という同値衝突は解消する |
| D-4 | 文書レベル見出しに**実寸が 4 の倍数の段のみ**を用いる規則を採るか | **採用する**。**対象は文書レベルの見出しのみ**とし、`font.display.mdSize` (`lg` 18px・車種クラス名) は**対象外**であることを明記する。`sm` (14px) も `label.fontSize.md` / `label.numberSize.sm` として bound 確定済みのため対象外。4px 系 (§4) の適用範囲を `typography` 全体へ拡げない |
| F-5 | 入力要素の角丸を `radius.input` (4px) のまま維持するか `radius.action` (pill) へ統一するか | **pill へ統一する** (`radius.input` を廃止・削除)。同一フォーム内でボタン (pill) と入力欄 (4px) が異なる形状を持つ状態を解消する。角丸の用途トークンは 5 系統から **4 系統** (action / card / badge / overlay) へ |
| F-1 | Modal の表示形態 (form = drawer / sheet / popover) を正式仕様にするか、「未承認の拡張候補」のまま据え置くか | **正式仕様にする**。`components.md` §6「拡張候補 (未承認)」の BottomSheet / Popover を form 軸の `sheet` / `popover` として本文へ統合し、同節を廃止する。**実装基盤は drawer 単一を維持し第 3 の Modal 実装基盤を導入しない** (`popover` は overlay の z 軸・backdrop・dismiss を共有する同一基盤上の表示形態であり第 3 の実装基盤に当たらない)。切替は `breakpoint.lg` (1024px) 未満 = `sheet` / 以上 = `popover`。backdrop は 3 形態共通 |
| F-4 | 主 CTA の個数制約の撤廃 (travel = §16) を適用するか | **適用する**。rental-car でも**主 CTA の個数制約を設けない**ことを確定する。CTA の優先度は `primary` / `secondary` / `ghost` / `text` の強弱階層で表現し、繰り返し要素 (ResultCard 等) 内で各項目が `primary` を持つことを妨げない。`components.md` Button の「適用判断は未取得 `🚧`」を解消する |
| C-5 | select の未選択値 (プレースホルダ相当) への `color.text.muted` の扱い (travel = §22) を適用するか | **適用し、かつ適用範囲を UI の種別で限定しない**。**未入力状態の案内文字** — `input` / `textarea` の `::placeholder`、Select の未選択値 (選択前の `option` に相当する表示)、その他の入力フィールドの未入力表示 — の**すべて**に `color.text.muted` (`#9E9E9E`・白背景 2.68:1) を用いる。**AA 未達であることを明示する**。適合宣言は行わない。**色の許容であって、未入力であることを色だけで伝えてよいという意味ではない** (未入力の識別は文言が担う)。本判断により**プレースホルダ専用の用途トークン `color.text.placeholder` は定義しない** (当初案の semantic 追加から取り下げ)。判読性を要する補助情報は `color.text.mutedStrong` (`#616161`・6.19:1) を用いる。**適用範囲 = rental-car に限定**し、travel (§22) ・inbound へは及ぼさない (3 独立 DS の原則 P1/ADR-0022)。<br>**適用範囲の変更経緯 (事実)**: 本判断の当初取得時 (2026-09-07) は travel §22 と同じ「Select の未選択値のみ」であった。同日、PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) のコードレビューが `design.md` §2.6 内の規則の矛盾を検出したことを契機に、**Web部責任者が「未入力時の状態を特定の UI に限定しない。`color.text.muted` に統一」と判断** (2026-09-07・明示取得) し、適用範囲を上記へ変更した |
| H-1 / H-2 | DS 見本ページ (`preview.rental-car.html`) と design-system レイヤー入口 README を本 Issue に含めるか | **含める**。見本ページは**非正本**とし規則の文章を持たせない。値・色見本・スケールの 3 ブロックは生成器から出力し、見本ページへ値を手で書き写さない。あわせて `tools/gen-preview-tokens.py` を**複数サービス対応**にする (従来は `DS = services/travel/design-system` を固定) |

**本 PR ([#171](https://github.com/tocoo/coocom-design-system/pull/171)) のコードレビューを契機に追加取得した判断 (2026-09-07)**

| # | 論点 | 取得した判断 |
| --- | --- | --- |
| F-6 | Modal の `sheet` の最大高・`popover` の幅段階を未確定のまま残すか、DS の規則として確定するか | **確定する**。`sheet` の最大高は **`90vh`**、`popover` の幅は **`240〜320px`** とする。いずれも `components.md` に既にあった値をそのまま規則へ格上げしたものであり、**新しい値を発明していない**。`90vh` は `drawer` の SP 上限と同値であり、「選んで即閉じる」用途に対する**上限**として置く (常用の高さではない)。**適用範囲 = rental-car に限定**し、travel・inbound へは及ぼさない (3 独立 DS の原則 P1/ADR-0022)。継承元の travel は同 2 項目を「依頼元の画面固有実装値 (85% / 420px / 680px) であり本 Repository で実査していない」として**未確定のまま維持**する (travel `design.md` §7.1・本 §17 の Does Not Decide)。<br>**取得経緯 (事実)**: 本判断は §29-3 の 7 件と異なり Issue [#170](https://github.com/tocoo/coocom-design-system/issues/170) 起票時には取得していない。本 PR のコードレビューが「正本 `design.md` §7.1 は未確定としているのに `components.md` は `🚧` なしの確定値として記載している」食い違いを検出したことを契機に、**Web部責任者が 2026-09-07 に明示取得**したものである |
| F-7 | C カテゴリ・特集ラベル (C1 企画名 / C2 販売条件) を写真の上に置いてよいか | **置いてよい**。**写真の上に置けるのは A 割引率と C カテゴリ・特集の 2 カテゴリ**とする。C は写真の上・有色面の上では**枠線を引かず面のみで分離**する (影・スクリムは用いない = [../services/rental-car/design-system/design.md](../services/rental-car/design-system/design.md) §2.4 の [決定])。他のカテゴリ (B 会員種別 / D 中立タグ / E 在庫・販売状態 / F 予約条件 / G 写真枚数 / H) は写真の上に置かない。**適用範囲 = rental-car に限定**し、travel・inbound へは及ぼさない (3 独立 DS の原則 P1/ADR-0022)。<br>**取得経緯 (事実)**: 本判断も F-6 と同じく Issue [#170](https://github.com/tocoo/coocom-design-system/issues/170) 起票時には取得していない。本 PR のコードレビューが、本 PR で新設した `design.md` §2.4 の [決定] (「写真の上・有色面の上では枠線を引かず面のみで分離する」= C を写真の上に置く前提) と、[../services/rental-car/design-system/labels-tags.rental-car.md](../services/rental-car/design-system/labels-tags.rental-car.md) A 節の「写真の上に置けるのは A だけ」との食い違いを検出したことを契機に、**Web部責任者が 2026-09-07 に明示取得**したものである。なお当該食い違いは本 PR 以前から `labels-tags.rental-car.md` 内に存在した (`origin/main` の同ファイルで A 節・C1 節の双方を実測)。**本判断により `labels-tags.rental-car.md` A 節の当該記述を是正する**。ラベル・タグ定義シート原本との照合は本 Repository では行っていない (**未検証**) |

あわせて、travel 側で既に確定していた次の内容を rental-car の規則として明文化する (上記 7 件の判断の適用に付随するもので、いずれも travel 側の確定内容を**縮小後の形で**持ち込む)。

| 項目 | 内容 |
| --- | --- |
| A 割引率ラベルに限る白文字の例外 | 用途を **A 割引率ラベル (`color.label.discount`) に限り**、面を **scheme 逆色 (`color.scheme.*.inverse`) に限る**。campaign accent 面 + 白文字は例外に含めない。サイズ・ウェイトは不問。**AA 未達 (main 2.78:1 / sub 2.15:1) を明示**し適合宣言は行わない。§25 の Does Not Authorize が「例外条項の明文化は未了」としていた状態はこれで解消する |
| accent の帰属 | accent を**面**として持つのは **B 会員種別** (`color.membership.paid` = accent 淡色段) のみとし、**C カテゴリ・特集は accent をアイコン (点)** (`color.label.category.icon`) として持つ。C の面は白 (`color.surface.default`) とし accent で塗らない。`labels-tags.rental-car.md` C1 と `design.md` 未確定事項の `🚧` 2 箇所を解消する |
| C を白系の面の上に置く場合の分離手段 | **白系の面 (`color.surface.default` / `color.surface.subtle`) の上に置く場合にのみ** `color.label.category.border` (= `color.border.default` `#CCCCCC`) の枠線を `border.width.thin` (1px) で引く。写真の上・有色面の上では引かない。枠線は白面上 **1.61:1**・`surface.subtle` 上 **1.53:1** で**非テキスト UI 要素の 3:1 に達しない**ことを明示する (本 Repository で実測)。分離の補助であり、識別は文字 (16.10:1) が担う。適合宣言は行わない |
| `labels-tags.rental-car.md` C1 の記述の是正 | 旧記述「用途色トークン (`label.category` 相当) は追加しない。**国内宿泊 (travel) でも C 特集は据え置き**であり」は、travel が Task 009-60 (2026-09-05・§27) で `color.label.category` を確定しているため**現在の事実に反していた**。当該記述を削除し、用途色を定義した記述へ置き換える |
| 表記規則 3 節 | §8.1 割引率の表記規則 (基本形 `NN%OFF`・数字は `%OFF` より 1 段上・半角/整数/先頭ゼロなし・端数処理は未確定・表示しない条件 4 件・表示成立条件)・§8.2 予約条件の表示規則 (面なしのテキスト行・文字色 4 役・アイコン固定 5 種・並び固定・文言併記・得/損の 2 問判定)・§8.3 クリエイティブへの DS 適用範囲の詳細 (グラデーションを審査対象とする・どちらの段かを先に宣言し宣言がなければ適用とみなす・書体/文字サイズ/ウェイト/器の形/傾きは必然性を示せば外せる) |

### 29-4. 追加・変更するトークン

| 種別 | 内容 |
| --- | --- |
| semantic 追加 | **39 件** — (A 面と文字色) `color.text.inverseMuted` / `onAccent`、(B リンク) `color.text.linkHover` / `linkActive`、(D 文書レベル見出し) `font.heading.lineHeight` / `h4Size` / `h5Size` / `h6Size`、(E ラベル・タグ) 器 `label.*` 12 件・`color.label.discount.surface` / `text`・`color.label.category.surface` / `text` / `icon` / `border`・`color.label.stock`・`color.membership.paid.surface` / `text`・`color.membership.free.surface` / `text`・`color.tag.neutral.surface` / `text`・`color.accent.campaignTint` / `campaignInk`・`color.scheme.{main,sub}.accentTint` / `accentInk` |
| semantic 参照先の変更 | **1 件** — `font.heading.h3Size`: `{typography.size.lg}` (18px) → `{typography.size.2xl}` (24px) |
| semantic 削除 | **1 件** — `radius.input` (判断 F-5 による) |
| primitive 追加 | **4 件** — `color.palette.orange.100` (`#F9CDBC`・bound) / `orange.800` (`#8A2E11`・🚧 仮色) / `coral.100` (`#F8CBC2`・🚧 仮色) / `coral.800` (`#8A2C18`・🚧 仮色) |

- **placeholder の扱い (§14)**: accent の濃色段 (`orange.800` / `coral.800`) とサブスキームの淡色段 (`coral.100`) は継承元である travel 側でも `placeholder` (仮色) であり、`🚧` を伝播させる。**実色を発明しない**。淡色段 `orange.100` (`#F9CDBC`) のみ bound とする。B-1 の淡色面 + 濃色文字 (5.84:1) は概算であり、成立検証は実色値確定後に本 Repository で行う。
- **値は rental-car のファイルに独立して持つ** (3 独立 DS の原則 = P1/ADR-0022)。travel のファイルを参照・共有しない。採用するのは travel の**定義体系**である。

### 29-5. 適用しない / 維持する

**travel 固有のため適用しない**

- `color.icon.rating` / `icon.reviewSize` — ReviewStars (星評価) は宿泊固有であり rental-car に対象の Component がない。したがって travel `design.md` §2.1 の「評価色と販促面色の用途境界」も本 DS では成立しない。
- primitive `color.palette.red.500` `#D10000` / `orange.500` `#EF4123` — travel の旧リンク色・特集面色の実測値であり rental-car の実装事実値ではない。
- travel `design.md` L382 の「割引率等のコンテンツ表記規則を管理する正本は独立した文書 (`brand-content.md` 等) を新設する方向を確定する」という [決定] 行 — travel 自身が Task 009-45 (2026-08-04・§21) で §16 の新設方向を**撤回**し §8 系へ集約する方向を確定しているため、撤回済みの方向を本 DS へ持ち込まない。

**rental-car 独自要素として維持する**

- `color.mask.secret` (SecretPrice のマスク面 = B-2 無料会員の面色)・`font.display.mdSize` (車種クラス名 18px 明朝)・`icon.size` (既定 20px)。
- 本 DS で先行定義した Component 3 件 (Select / FormLabel / Label・Tag。travel 側は未着手) とレンタカー固有 Component 8 件 (SearchForm / ResultCard / SecretPrice / Options / StorePicker / StepIndicator / Filter / Sort・Pagination)。
- ラベル体系の割当差 — D4 格付けの廃止 / B-2 の既定非表示 / C1・C2 の 2 区分 (企画名・販売条件) / D1〜D3 (車種クラス・装備・利用条件) / E1 は「在庫僅少」/ G は車両写真の枚数。
- 画像なし表現 (No Image fallback = `surface.muted` 面 + `text.mutedStrong` の文字・比率 4:3)。**travel は §6 で「未定義」であり rental-car が先行している**。
- [../services/rental-car/design-system/migration-map.md](../services/rental-car/design-system/migration-map.md) (実装 japan ゾーンの旧値 12 項目との対照表。travel に対応物がない)。
- `design.md` §2 の既存小節 (§2.1 スキーム / §2.2 用途 / §2.3 品質下限) を保持し、新設分を **§2.4〜§2.6** とする。**travel と節番号が 1 対 1 に対応しないのは §2 のみ**で、§3.1・§7.1・§8.1〜§8.3 は同じ番号である。

### 29-6. 本記録が決定しないこと

- **スキームの正式採用 (main / sub)**。`color.state.success` / `color.text.link` / `linkHover` / `linkActive` / `color.state.error` / `color.accent.campaign` / `campaignTint` / `campaignInk` / `color.label.discount.surface` / `color.membership.free.*` / `color.mask.secret` は現在 `main` を参照して固定されており、スキームの切替に自動追随しない。
- **accent 濃色段 (`orange.800`) およびサブスキーム coral の 2 段の実色値**。🚧 仮色のまま維持し `$status` を昇格しない。b2 (accent 淡色面 + 濃色文字) の 4.5:1 成立検証は実色値確定後とする。
- **E2 満車・受付終了の意匠値** (Button の disabled 定義が先)。**F 予約条件の「得」の文字色とリンクの見分け** (同値 `#2C50C8` のため押せないのにリンクに見える論点)。
- **C カテゴリ・特集ラベルのアイコンのサイズ** (`iconSize` の最小段は 16px で、器 sm = 高さ 20px・文字 12px に当てる値が正本に無い。継承元の travel 側でも未定義)。
- **ResultCard の実 px・料金列の実ラベル・モーション/シャドウの実値・ロゴ素材・写真選定基準・backdrop の実値**。いずれも実査待ちであり発明しない。
- **サービス識別子 `rental-car` の正式化** (確認事項 `#8`)。**Filter の件数算出仕様**。
- **3 DS 横断の Modal 実装基盤** (§1 Q9)。判断 F-1 は rental-car の**表示形態**を定めるものであり、横断の実装基盤を確定しない。
- **画像・グラデーションを面とする場合の文字色と scrim の要否**。§2.4 の検証表は**単色面のみ**を対象とする。
- **Modal の form の a11y** (`role` / `aria-modal` / フォーカストラップ / 復帰先・背面スクロールロック)・実装 API 名 (prop 名)。(**`sheet` の最大高と `popover` の幅段階は判断 F-6 で確定した**ため本項から外れる。)**最小タップ領域 44px の spacing トークンは追加しない** (`spacing` に 44px の段が無く、44px は WCAG 2.2 の 2.5.5 Enhanced 相当で §2.3 の AA 最低ラインから導けない)。品質下限としての 44px 自体は §2.3 で維持する。
- **クリエイティブのグラデーション審査基準・審査主体の設置**。§23 (Governance 横断) との原則正本の置き場所、および §23ⓑ「カラーもトークン指定外を許容」と本 DS §8.3「カラーは厳守」の差分の解消も本記録では行わない。
- **画面別の見出し階層・semantic role の割当** (どの画面のどのコンテンツを `h1` / `h2` とするか)。本 DS の Screen Requirements レイヤーは未着手である。
- **見出し以外の `typography` 用途へ 4 の倍数規則を及ぼすか**。判断 D-4 のとおり文書レベルの見出しに限定する。
- **実装 Repository (`tocoo/tocoo_rental_car`) 側の適用作業**・既存の非適合箇所の是正・反映の範囲/順序/期限。実装の見出し実測値は本 Repository で実査していない。
- **恒久 Decision ID・ADR・正式 Status・Phase・Gate の採番・作成・新設**。**`$meta.version` の bump** (付与規則そのものが未決)。
- **適用規格・達成レベルの正式確定・適合判定・適合宣言**。本記録および rental-car の文書に記載したコントラスト比は本 Repository での実測値の記録であり、適合宣言ではない。
- **travel・inbound の成果物への適用**。§24・§26・§27・§28 の判断内容・適用範囲は変更しない。

## 30. Travel `design.md` §2.1 検証表の欠落の回収と Breadcrumb 現在地の文字色の確定 — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: 国内宿泊 (travel) `design.md` §2.1「面 (背景) と文字色の組み合わせ規則」の検証表が、同書・`components.md` が通常の用法として規定する組み合わせを欠いていた件の回収、および Breadcrumb 現在地の文字色の確定について、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機は [Issue #172](https://github.com/tocoo/coocom-design-system/issues/172)。上記 §1〜§29 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§29 の各記録は変更しない。
- **本記録は §29 からの自動適用ではない。** §29 は適用範囲を「国内レンタカー (rental-car) に限定。travel・inbound・3DS 横断へは自動適用しない」と明記しており、同 §29-3 判断 C-5 (未入力状態の案内文字を `color.text.muted` に統一) も rental-car 限定である。本 §30 は **travel について別途取得した判断**であり、rental-car・inbound へは及ばない (3 独立 DS の原則 = P1/ADR-0022)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。新しい色値 (primitive) を発明しない。

### 30-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | ①[../services/travel/design-system/design.md](../services/travel/design-system/design.md) の部分更新 (§2.1 検証表への **21 行追加** (14 行 → **35 行**)・既存 1 行の概算 `≈11.1:1` の実測値 `11.11:1` への是正・既存 5 行への「**主色**」の明示 (実測値は不変)・列見出し「概算」→「コントラスト比」の是正と概算/実測の区別の明記・`color.text.muted` を表に載せない旨の [決定] 1 行の追加・未確定事項の一覧 1 行の ✅ 解決化)、②[../services/travel/design-system/components.md](../services/travel/design-system/components.md) の部分更新 (`Breadcrumb` の現在地の文字色を `color.text.muted` から `color.text.mutedStrong` へ変更・Don't 1 行の追加)、③[../services/travel/design-system/preview.travel.html](../services/travel/design-system/preview.travel.html) の部分更新 (Breadcrumb の見本と caption を②へ追随。**非正本**) |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-07 |
| 承認主体 | Web部責任者 |
| 根拠 | `design.md` §2.1 の検証表は「**表に無い組み合わせを検証済みとして扱わない**」と網羅性を宣言しながら、同書・`components.md` が実測値つきで通常の用法として規定する組み合わせを欠いていた (改訂前 **14 行**)。継承先の国内レンタカー (rental-car) では同じ欠落が Task 009-63R2 / 009-63R3 で是正済み (18 行 → 25 行) であり、継承元の travel 側に残っていたものを回収する。あわせて、`components.md` `Breadcrumb` の現在地が `color.text.muted` (`#9E9E9E`・白面 **2.68:1**) を用いており、`design.md` §2 の [事実]「`color.text.muted` は判読性を要する情報には用いない」と食い違っていた |
| 適用範囲 | **国内宿泊 (travel) に限定**。rental-car・inbound・3DS 横断へは自動適用しない |

### 30-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **高** (判定者 = Web部責任者・判定日 2026-09-07・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定 = **Web部責任者およびチーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11) |
| 判定の位置づけ | 本判定は本件に限る都度判断であり、§8 の編集的訂正 carve-out (意味を変えない字句の修正) の適用でも、一般的な高／低の内容基準の確定でもない。正本の規範表への**行の追加**と、Component 仕様の**文字色の変更**を伴うため carve-out の対象外である。前例として、より小さい範囲であった §27 (用途色 4 件の追加)・§28 (semantic 1 件の参照先変更) も高判定であった |

### 30-3. 取得した現在判断 (2026-09-07)

| # | 論点 | 取得した判断 |
| --- | --- | --- |
| G-1 | 白面 × `color.text.muted` (`#9E9E9E`・**2.68:1**・AA 未達) を §2.1 の検証表へどう載せるか。同組み合わせは `components.md` `Breadcrumb` の現在地で使用中であり、travel の未確定事項の一覧に「Breadcrumb 現在地への `color.text.muted` 適用の可否」が ❓ 未判定として残っていた | **表へ載せず、Breadcrumb 現在地の文字色を `color.text.mutedStrong` (`#616161`・白面 6.19:1) へ変更する**。理由は、travel `design.md` §2 の [事実] が既に「`color.text.muted` (白背景 2.68:1) は通常テキストに求められる 4.5:1 に達しないため、判読性を要する情報には用いない」と定めており、現在地は判読性を要する情報であるため。本判断により AA 未達の組み合わせを DS の規則として記録するのではなく**解消する**。**新しい色値は追加しない** (`color.text.mutedStrong` は既存 bound トークン)。`color.text.muted` トークンは文字色の濃度段として定義を維持し、値・参照先・`$status` を変更しない。<br>**適用範囲 = travel に限定**。rental-car (§29-3 判断 C-5 = 未入力状態の案内文字を `color.text.muted` に統一・AA 未達明示) とは扱いが異なるが、これは 3 独立 DS の原則 (P1/ADR-0022) による差であり、いずれか一方へ揃えない |
| G-2 | 本件の影響度 (§8) | **高** (§30-2) |

### 30-4. 追加・変更するトークン

**なし。** semantic・primitive のいずれにも追加・削除・値の変更・参照先の変更・`$status` の変更を行わない。§2.1 の検証表へ追加する 10 行はいずれも**既存の bound 済みトークンの値から機械的に決まるコントラスト比の記録**であり、新しい色値・新しい規則を追加するものではない。

### 30-5. 検証表へ追加する組み合わせ (実測値)

いずれも本 Repository で WCAG 2.x 標準式により実測した値である。`color.text.link` / `linkHover` / `linkActive` は per-scheme (主色 = royal / 副色 = indigo) で値が異なるため、`design.md` の「**2 スキームは値が異なるため、値やコントラスト比を伴う記述でワイルドカード表記を用いて 1 行に束ねない**」に従い主色・副色で行を分ける (各 2 行 = 計 6 行)。

| # | 面 (背景) | 文字 | 実測 | 通常テキスト (4.5:1) | 規定箇所 |
| --- | --- | --- | ---: | --- | --- |
| 1 | `color.action.primary.bg` `#2C50C8` | `color.action.primary.text` `#FFFFFF` | **6.80:1** | 達成 | `components.md` Button `primary` |
| 2 | `color.surface.default` `#FFFFFF` | `color.text.body` `#424242` | **10.05:1** | 達成 | 本文の既定・`components.md` Input 入力値 |
| 3 | `color.surface.default` `#FFFFFF` | `color.text.mutedStrong` `#616161` | **6.19:1** | 達成 | `design.md` §2 の [事実]・`components.md` PriceTag / Breadcrumb 現在地 (本記録 G-1) |
| 4 | `color.surface.default` `#FFFFFF` | `color.text.placeholder` `#616161` | **6.19:1** | 達成 | `design.md` §2.3 |
| 5 | `color.surface.default` `#FFFFFF` | `color.text.link` 主色 `#2C50C8` / 副色 `#4845D4` | **6.80:1** / **6.82:1** | 達成 | `design.md` §2.2 |
| 6 | `color.surface.default` `#FFFFFF` | `color.text.linkHover` 主色 `#2340A6` / 副色 `#3936B0` | **8.92:1** / **9.02:1** | 達成 | `design.md` §2.2 |
| 7 | `color.surface.default` `#FFFFFF` | `color.text.linkActive` 主色 `#1B3488` / 副色 `#2C2A8C` | **11.09:1** / **11.56:1** | 達成 | `design.md` §2.2 |

- **行数 (事実)**: 改訂前 **14 行** → 改訂後 **35 行** (追加 **21 行**)。内訳は [Issue #172](https://github.com/tocoo/coocom-design-system/issues/172) の 1〜7 = **10 行**と、PR [#173](https://github.com/tocoo/coocom-design-system/pull/173) のコードレビュー (2026-09-07) を契機に追加した **11 行** (下記) である。[Issue #172](https://github.com/tocoo/coocom-design-system/issues/172) の推奨欄は「14 行 → 22 行」と記していたが、同 Issue が列挙する 1〜4 が各 1 行・5〜7 が各 2 行で計 **10 行**であるため、正しい改訂後の行数は **24 行**である (Issue の計算誤り)。追加する組み合わせの内容は Issue の 1〜7 と同一であり、増減はない。
- 3 と 4 は同じ primitive (`gray.700` `#616161`) を参照するため実測値が一致するが、`design.md` §2 の [事実]「用途別名が同じ primitive を参照する場合でも、一方の値の変更が他方へ自動的に及ぶ設計にはしない」に従い**別トークンとして行を分ける**。
- 1 の `color.action.primary.bg` は `{color.brand.primary}` → `{color.scheme.main.base}` を参照し **`#2C50C8` に固定**される (semantic を解決して確認)。スキーム切替に追随しないため主色・副色の 2 値は生じず 1 行である。

**PR [#173](https://github.com/tocoo/coocom-design-system/pull/173) のコードレビュー (2026-09-07) を契機に追加した 11 行**

同レビューが「同じ理由で表に無い組み合わせが残っている」「per-scheme の判定基準が表内で割れている」ことを検出したため、承認対象①の範囲を拡大した (Web部責任者判断 2026-09-07)。**新しい色値・新しい規則は追加していない。**

| # | 面 (背景) | 文字 | 実測 | 通常テキスト (4.5:1) | 規定箇所 |
| --- | --- | --- | ---: | --- | --- |
| 8 | `color.surface.muted` `#F5F5F5` | `color.tag.neutral.text` `#424242` | **9.22:1** | 達成 | D 施設属性タグ (`color.tag.neutral`) |
| 9 | `color.surface.default` `#FFFFFF` | `color.state.error` 主色 `#D23A3A` / 副色 `#D2405F` | **4.77:1** / **4.53:1** | 達成 | E1 残室僅少 (`color.label.stock`)。per-scheme のため 2 行 |
| 10 | `color.scheme.main.tint` `#E8EDFB` | `color.scheme.main.ink` `#14224A` | **13.21:1** | 達成 | B 無料会員ラベル (`color.membership.free`) |
| 11 | `color.action.secondary.bg` `#FFFFFF` | `color.action.secondary.text` `#212121` | **16.10:1** | 達成 | `components.md` Button `secondary` |
| 12 | `color.surface.inverse` `#212121` | `color.text.mutedStrong` `#616161` | **2.60:1** | **未達 (禁止)** | `components.md` §1 の [事実] |
| 13 | `color.accent.campaign` 副色 `#E0553C` | `color.text.onAccent` `#FFFFFF` | **3.79:1** | 未達 (条件付き) | §2.1 (主色行の副色対応) |
| 14 | `color.accent.campaign` 副色 `#E0553C` | `color.text.strong` `#212121` | **4.24:1** | 未達 (規則としては使用しない) | 同上 |
| 15 | `color.surface.default` / `subtle` / `muted` | `color.accent.campaign` 副色 `#E0553C` (文字色として) | **3.79:1** / **3.60:1** / **3.48:1** | 未達 (条件付き) | 同上。面ごとに 3 行 |

- 8〜12 は同レビューが名指しした 5 組である。9 の `color.state.error` は §2 の用途表が per-scheme (主色 `#D23A3A` / 副色 `#D2405F`) と定義しているため 2 行に分ける。10 の `color.membership.free` と 11 の `color.action.secondary` は同表が per-scheme トークンとして定義していないため各 1 行である。
- 13〜15 は、`color.accent.campaign` が §2 の用途表で per-scheme (主色 `#E4572E` / 副色 `#E0553C`) と定義されているにもかかわらず、改訂前の表が**主色の値のみ**を記録していたことへの対応である。既存 5 行には「**主色**」である旨を明示した (**実測値は変更していない**)。
- **副色スキームの `color.accent.campaignTint` `#F8CBC2` / `campaignInk` `#8A2C18` は 🚧 仮色**であるため、これに対応する行は追加しない。実色値確定後に本 Repository で検証する (主色側の `campaignTint` の扱いと同じ)。
- **per-scheme の判定基準 (事実)**: あるトークンを主色・副色の 2 行に分けるか 1 行にするかは、`semantic.travel.json` の解決チェーンではなく **§2 の用途表が per-scheme トークンとして定義しているか否か**による。`color.action.primary.bg` と `color.text.link` は JSON 上いずれも `{color.scheme.main.base}` へ解決するが、前者は副色が別トークン (`color.brand.secondary`) であり per-scheme ではなく、後者は同表に「副色=sub.base」と注記された per-scheme トークンである。

### 30-6. 本記録が決定しないこと

- **`color.text.muted` の適用可能範囲そのものの明文化** (装飾的・非必須の弱表現に限るか)。travel の未確定事項の一覧に ❓ 未判定として残す。本記録が確定するのは Breadcrumb 現在地への適用可否のみである。
- **select の未選択値 (プレースホルダ相当) への `color.text.muted` 使用** (§22 で方向確定・§2.3 への例外条項の実規則化は別 Task)。本記録は §22 の判断内容・適用範囲を変更しない。
- **画像・グラデーションを面とする場合の文字色と scrim の要否**。§2.1 の検証表は**単色面のみ**を対象とする (依頼 E-1)。
- **`color.text.muted` トークンの削除・非推奨化**。文字色の濃度段としての定義を維持する。
- **rental-car・inbound の成果物への適用**。§29-3 判断 C-5 (rental-car の未入力状態の案内文字 = `color.text.muted` に統一) の判断内容・適用範囲は変更しない。
- **上流 NVP-001 (現在地の可視性) の解決**。本記録は DS 側の文字色を定めるにとどまり、上流の要件そのものを確定しない。
- **適用規格・達成レベルの正式確定・適合判定・適合宣言**。本記録および travel の文書に記載したコントラスト比は本 Repository での実測値の記録であり、適合宣言ではない。
- **恒久 Decision ID・ADR・正式 Status・Phase・Gate の採番・作成・新設**。**`$meta.version` の bump**。
- **実装 Repository (`tocoo/tocoo_travel`) 側の適用作業**。実装の Breadcrumb の現在地の文字色は本 Repository で実査していない (**未検証**)。


## 31. Travel 文書レベル見出しの太さ 100 (thin) の導入と `typography.fontWeight` スケールの配信段への整合 (travel / rental-car) — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: 国内宿泊 (travel) の文書レベルの見出しに **LINE Seed JP Thin (100)** を選べるようにする件、および同件の検証中に判明した **`typography.fontWeight` のスケールに書体が配信しない段が含まれていた**件について、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機は [Issue #174](https://github.com/tocoo/coocom-design-system/issues/174)。上記 §1〜§30 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§30 の各記録は変更しない。
- **本記録は §28 (ブレークポイントごとの見出しサイズ段) の続きではない。** §28 が確定したのは**サイズ段と適用幅**であり、本記録が確定するのは**太さ**である。§28 の判断内容・適用範囲は変更しない。
- **適用範囲は国内宿泊 (travel) と国内レンタカー (rental-car) の 2 サービス**であり、範囲はスケールの整合 (後述 H-5) の部分に限り 2 サービスへ及ぶ。**見出しの太さ 100 を選べる規則 (H-1〜H-4) は travel に限る。** inbound へは及ばない (後述 H-6・3 独立 DS の原則 = P1/ADR-0022)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。

### 31-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | ①[../services/travel/design-system/primitive.travel.json](../services/travel/design-system/primitive.travel.json) の `typography.fontWeight` の**追加 2 件** (`thin` 100・`extraBold` 800) と**削除 2 件** (`medium` 500・`black` 900)、②[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) への `font.heading.weightThin` の追加 (既定 `font.heading.weight` は不変)、③[../services/travel/design-system/design.md](../services/travel/design-system/design.md) の部分更新 (§2.1 用語の定義「ウェイトの境界」の是正・§3 の表と箇条・§3.1 の表への列追加と [決定] の追加/改訂・未確定事項の一覧 2 行追加)、④[../services/rental-car/design-system/primitive.rental-car.json](../services/rental-car/design-system/primitive.rental-car.json) の同じスケール整合 (追加 2 件・削除 2 件)、⑤[../services/rental-car/design-system/design.md](../services/rental-car/design-system/design.md) の部分更新 (§2.1 用語の定義の是正・§3 の箇条と [事実]・§3.1 の [決定] 改訂)、⑥両サービスの `preview.*.html` の部分更新 (Google Fonts 読み込み・生成ブロックの再生成・注記。**非正本**) |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-11 |
| 承認主体 | Web部責任者 |
| 根拠 | ①見出しのウェイトを変更したいという要望に対し、正本は文書レベルの見出しを **700 固定**と定め、100 に相当する primitive を持たなかった ([Issue #174](https://github.com/tocoo/coocom-design-system/issues/174))。②同件の検証で、`typography.fontWeight` が定義する `medium` (500) と `black` (900) に、書体 (LINE Seed JP) の**対応する字面が存在しない**ことが判明した (本 Repository での実測)。正本が存在しない字面を値として定義し続けることは、実装が指定しても得られない見た目を DS が約束している状態にあたる |
| 適用範囲 | H-1〜H-4 (太さ 100 の選択規則) = **travel に限定**。H-5 (スケールの配信段への整合) = **travel および rental-car**。inbound へは及ばない (H-6) |

### 31-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **高** (判定者 = Web部責任者・判定日 2026-09-11・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・高の既定 = **Web部責任者およびチーフデザイナー**。いずれか一方のレビューのみで内容レビュー完了・反映確定として扱わない (同 §10・§11) |
| 判定の位置づけ | 本判定は本件に限る都度判断であり、§8 の編集的訂正 carve-out (意味を変えない字句の修正) の適用でも、一般的な高／低の内容基準の確定でもない。**primitive の削除 2 件**・**追加 2 件**・承認済みの [決定] の改訂・2 サービスにまたがる変更を伴うため carve-out の対象外である |

### 31-3. 取得した現在判断 (2026-09-11)

| # | 論点 | 取得した判断 |
| --- | --- | --- |
| H-1 | 太さ 100 を見出しの**既定そのもの**にするか、既定は 700 のまま**選べる選択肢**として足すか | **既定は 700 のまま、明示的な選択肢として足す**。`font.heading.weight` (700) は置き換えず、選択しない限り 700 が適用される。選択のための semantic を別に設ける (`font.heading.weightThin`)。**根拠となった実測** = 実寸 16px の見出しに 100 を当てると本文 (400) より細くなり、見出しが本文より弱く見える (本 Repository で描画して確認)。既定にすると `h4`〜`h6` を含む全段が巻き添えになる |
| H-2 | 100 を使ってよい見出しの**範囲** (文書レベル `h1`〜`h6` 全体か、Display・Hero・特集・詳細施設名のような役割に限るか) | **要素名 (`h1`〜`h6`) では制限しない。** 制限は実寸で行う (H-4)。`design.md` §3.1 が既に「書体は要素名ではなく役割で選ぶ」と定めており、太さも要素名では決めない |
| H-3 | `design.md` §3.1 の [決定]「**新しいサイズ値・行間値・ウェイト値 (primitive) は追加しない**」の扱い (改訂するか、本件を例外として記録するか) | **決定文を改訂する。** サイズ値・行間値を追加しない方針は変更せず、ウェイト値についてのみ本 Task の追加・削除を記録する形へ改める。例外として別記すると、正本の [決定] と実物が食い違ったまま残るため |
| H-4 | 100 は細いため小さい見出しでの可読性が課題になりうる。**サイズの下限**を設けるか | **実寸 24px (1.5rem) 以上の見出しに限る。** 24px 未満では 100 を用いず既定の 700 を用いる。判定の対象はその幅で実際に適用される実寸であり、**同一の見出しが幅によって可否を変える** (`h3` は 1024px 以上で 24px = 可・1024px 未満で 20px = 不可)。本条件を満たす選択は §3.1 の「既定から外れる」に該当せず、**画面ごとの都度の承認を要しない**。<br>**根拠となった実測** = 40px / 32px / 24px では 100 が 700 と別の表情として成立する一方、20px で目に見えて弱くなり、16px では本文 400 より細くなる。下限 24px は §2.1 の**条件 (a)** (`24px` 以上・ウェイトを問わない) とも一致する |
| H-5 | `typography.fontWeight` が定義する段のうち、書体が**配信していない段**の扱い | **配信されている段は追加し、配信されていない段は記述を削除する。** 本判断により `medium` (500) と `black` (900) を削除し、`thin` (100) と `extraBold` (800) を追加する。<br>**実測 (本 Repository)** = Google Fonts が LINE Seed JP について配信するウェイトは **100 / 400 / 700 / 800 の 4 段のみ**である (`wght@100` / `@400` / `@700` / `@800` は `@font-face` が日本語 124 スライスぶん返り、`@200` / `@300` / `@500` / `@600` / `@900` は CSS ではなく `400: Font family not found` の HTML が返る)。削除する 2 段を `$value` で参照する semantic トークンは travel・rental-car・inbound のいずれにも**存在しなかった**。<br>**判断取得時に想定していた 300 は存在しない** — 取得時点では 300 も配信段と見込んでいたが、その見込みは配信されていないウェイトを要求した際に返るエラーページの内容を配信 CSS と誤って読み取った測定誤りによるものであり、`@font-face` の実数で測り直した結果 300 は配信されていないことが確定した。本判断の内容 (配信されていれば追加・されていなければ削除) は変わらず、追加対象が `thin` 100 と `extraBold` 800 の 2 件に確定した |
| H-6 | H-5 を適用する**サービスの範囲** | **travel と rental-car の 2 サービス**とする。両サービスは `typography.fontFamily` の先頭がいずれも LINE Seed JP であり、配信段が同一である (実測)。**inbound は保留** — 同 DS の書体規定 (`Murecho` / `Noto Sans JP` / `Roboto` / `Outfit`) 自体が暫定であり、配信段も travel / rental-car と異なるため、書体規定の確定後に別途判断する |
| H-7 | 本件の影響度 (§8) | **高** (§31-2) |

### 31-4. 追加・変更するトークン

**primitive (travel / rental-car の両方)**

| トークン | 変更 | 値 | `$status` | 参照する semantic |
| --- | --- | ---: | --- | --- |
| `typography.fontWeight.thin` | **追加** | 100 | bound | travel = `font.heading.weightThin`。rental-car = **無し** (用途は正本上未定義) |
| `typography.fontWeight.regular` | 不変 | 400 | bound | `label.weight.neutral` |
| `typography.fontWeight.medium` | **削除** | (500) | — | 削除前から **0 件** |
| `typography.fontWeight.bold` | 不変 | 700 | bound | `font.heading.weight` / `font.price.weight` / `label.weight.emphasis` |
| `typography.fontWeight.extraBold` | **追加** | 800 | bound | **無し** (両サービスとも用途は正本上未定義) |
| `typography.fontWeight.black` | **削除** | (900) | — | 削除前から **0 件** |

**semantic (travel のみ)**

| トークン | 変更 | `$value` | `$status` |
| --- | --- | --- | --- |
| `font.heading.weightThin` | **追加** | `{typography.fontWeight.thin}` | bound |
| `font.heading.weight` | **不変** | `{typography.fontWeight.bold}` (700) | bound |

- **新しい色値は追加していない。** 本記録が扱うのはウェイトのみである。
- **`$meta.version` は primitive / semantic とも据置き** (bump の条件は各 README の Open Issue として未決)。

### 31-5. 本記録が決定しないこと

- **`extraBold` (800) の用途。** 値として持つのみで、参照する semantic は両サービスとも設けない。どの用途に割り当てるかは別途判断する。
- **rental-car の見出しへ太さ 100 を導入するか否か。** 同サービスの `font.heading.weight` (700) は不変であり、travel `design.md` §3.1 の選択規則は同サービスへ自動適用しない (P1/ADR-0022)。
- **inbound の `typography.fontWeight` の扱い** (H-6 のとおり保留)。同 DS の書体規定の確定後に別途判断する。
- **本文 (`font.body`) のウェイト。** 正本上いまも未定義であり、本記録では扱わない。
- **明朝 (`font.display.family` = Noto Serif JP) を選んだ見出しの太さ。** 同書体は 100 を配信していないため (配信段は 200〜900・`wght@100` は `400: Font family not found`・本 Repository で実測)、明朝 × 100 は選べない。これは実測された制約の記録であり、明朝側の太さの規定を新たに定めるものではない。
- **画像・グラデーションを面とする場合の 100 の見えかた。** §2.1 が同面を対象外・未定義としている範囲に属する (travel の未確定事項の一覧へ起票)。
- **適用規格・達成レベルの正式確定・適合判定・適合宣言。** 太さは §2.1 のコントラスト比を変えない (比はウェイトでは変わらない)。本記録は適合宣言を行わない。
- **恒久 Decision ID・ADR・正式 Status・Phase・Gate の採番・作成・新設。**
- **実装 Repository (`tocoo/tocoo_travel`) 側の適用作業** (Google Fonts 読み込みの更新・トークンスナップショットの同期・実際の見出しへの適用)。実装側の状態は本 Repository で実査していない (**未検証**)。


## 32. リポジトリ入口 README ほか 3 文書の記述の最新化 — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: リポジトリ入口 [../README.md](../README.md)・Governance 入口 [README.md](README.md)・国内宿泊入口 [../services/travel/README.md](../services/travel/README.md)・インバウンドレンタカー入口 [../services/inbound/README.md](../services/inbound/README.md) の**記述を `main` の現状へ最新化する**改訂に対し、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機は [Issue #176](https://github.com/tocoo/coocom-design-system/issues/176)。
- **本記録は Design System の内容を変更しない。** トークン値・`$status`・`$meta.version`・規則・Component 仕様のいずれも対象外であり、扱うのは入口文書の記述のみである。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。

### 32-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | 4 つの入口文書の記述の最新化。①[../README.md](../README.md) — 冒頭「状態」・§4 (`tools/` の位置づけ)・§7 (補助スクリプトへのリンク)・§8 (構築状態・サービス表・DS 見本ページ)・§10 (対象外の現在の扱い)。②[README.md](README.md) — `owner-decisions.md` の説明を §31 まで、規則の説明へ適用開始後の改定 1 件を反映。③[../services/travel/README.md](../services/travel/README.md) — 見本ページの追記とレイヤー表・成果物説明の是正。④[../services/inbound/README.md](../services/inbound/README.md) — primitive 版数 `0.2.1` → `0.2.2-draft` の是正と、bootstrap 後の変更 1 件の明記 |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-11 |
| 承認主体 | Web部責任者 |
| 根拠 | 入口文書が **既に完了した作業を未着手と記述している**状態にあった。とくに [../README.md](../README.md) §8 の「Design System 改定は未着手」は、2026-07-24 (Task 009-18-BP1) 以降 travel / rental-car で継続している改定と矛盾する。[../services/inbound/README.md](../services/inbound/README.md) の `primitive 0.2.1` は JSON の `$meta.version` (`0.2.2-draft`) と一致しない事実の誤りである。入口文書は参照順序上の起点であり (§6)、誤った現況記述は下位レイヤーの読み違えへ伝播する |
| 適用範囲 | **上記 4 文書の記述に限定**。各サービスの Design System 成果物・Screen Requirements・Service Design の内容へは及ばない |

### 32-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **低** (判定者 = Web部責任者・判定日 2026-09-11・本件について明示取得) |
| 必要レビュー主体 | [review-approval-rules.md](review-approval-rules.md) §10 の影響度・低の既定 = **Web部レビュー担当者**。反映確定の前提は同 §11 に従う |
| 判定の位置づけ | 本判定は本件に限る都度判断である。**§8 の編集的訂正 carve-out (意味を変えない字句の修正) を根拠とする自動的な「低」ではない** — 本件は記述の意味 (現況の記述内容) を変えるため carve-out の対象外であり、本件について明示的に取得した判定である |

### 32-3. 取得した現在判断 (2026-09-11)

| # | 論点 | 取得した判断 |
| --- | --- | --- |
| I-1 | 最新化の反映経路 | **ブランチを作成し PR として反映する**。`main` はルールセット保護下にあり直接 push しない |
| I-2 | 最新化の対象範囲 ([../README.md](../README.md) のみか、実測で判明した他の入口文書も含めるか) | **4 文書すべてを 1 つの作業単位として扱う**。①[../README.md](../README.md)、②[../services/inbound/README.md](../services/inbound/README.md) の版数是正、③[../services/travel/README.md](../services/travel/README.md) への見本ページ・改定継続の反映、④[README.md](README.md) の `owner-decisions.md` 説明の §31 までの拡張 |
| I-3 | 本件の影響度 (§8) | **低** (§32-2) |

### 32-4. 記述上の扱いの統一 (本記録に基づき 4 文書で揃える点)

- **「12 候補の改訂」と「案件ごとの改定」を別経路として書き分ける。** Work Order 6 の総合判断 (全 12 候補「現時点では開始できない」・Task 009-6 / 2026-07-21 が記録上の最新) は維持する一方、案件ごとの改訂着手承認 ([review-approval-rules.md](review-approval-rules.md) §9・§20) に基づく Design System の改定は継続中である。**従前の「Design System 改定は未着手」という書き方は、前者を指しながら後者まで否定する形になっていたため用いない。**
- **`tools/` は 5 論理レイヤーのいずれにも属さない補助スクリプト置き場であり、正本ではない**ことを入口で明記する。
- **DS 見本ページ (`preview.<service>.html`) は非正本**であり、値・`$status` の正本は各サービスの JSON と `design.md` にあることを、travel・rental-car の双方で同じ扱いとして書く。

### 32-5. 本記録が決定しないこと

- **Work Order 6 の総合判断の変更・再評価の実施。** 全 12 候補「現時点では開始できない」・Alignment 未完了 (§19 観点 4・5 未充足) は本記録により変更しない。
- **Design System のトークン値・`$status`・`$meta.version`・規則・Component 仕様の変更。** 本件は記述の最新化に限る。
- **不足成果物の新規作成。** Repository principles・命名規則・ADR・用語定義の正本は引き続き未整備であり、本記録は空ファイルや推測による規約を作成しない。
- **承認済みの [review-approval-rules.md](review-approval-rules.md) 本体の改定。**
- **サービス識別子の確定。** `travel` / `rental-car` / `inbound` は暫定のままである (確認事項 #8)。
- **入口文書以外の陳腐化の点検範囲の確定。** 本件で点検したのは 4 つの入口文書であり、下位レイヤーの各成果物の記述が現況と一致するかは本記録では判定しない。
- **恒久 Decision ID・ADR・正式 Status・Phase・Gate の採番・作成・新設。**


## 33. Travel 文書レベル見出しの太さの明示的な選択肢への regular (400) の追加 — Task 009-65 の thin (100) 限定の是正 — 改訂着手の設計承認・影響度・現在判断の記録

- 種別: 国内宿泊 (travel) の文書レベルの見出しの太さについて、Task 009-65 (§31) が既定 700 に対する明示的な選択肢を **thin (100) のみ**と規定していた点を誤りと判断し、**regular (400) を同じ条件の選択肢として追加する**件について、Web部責任者が示した改訂着手の設計承認・影響度判定・現在判断の記録。契機 = 実装リポジトリ `tocoo/tocoo_travel` のお問い合わせ (`#7032`) のレビューで、FAQ (`#7031`) の見出し (`.faq__title` 32/40px・`.question` 20/24px) の 400 指定が現行 SOT のもとで逸脱と判定されたこと ([Issue #178](https://github.com/tocoo/coocom-design-system/issues/178))。上記 §1〜§32 とは独立した記録であり、混同しない。§5 設計承認ログ・§6 適用開始記録・§7〜§32 の各記録は変更しない。
- **本記録は §31 の判断内容を遡って変更するものではない。** §31 の H-1〜H-7 (thin の導入・スケールの配信段への整合) はそのまま有効であり、本記録が是正するのは「明示的な選択肢が thin のみである」という規定の範囲である。
- **適用範囲は国内宿泊 (travel) に限る。** rental-car / inbound へは及ばない (thin と同じ扱い・3 独立 DS の原則 = P1/ADR-0022)。
- 規約: 恒久 Decision ID・ADR・新しい正式 Status・Phase・Gate は採番・作成・新設しない。GitHub の approval・merge を判断・設計承認と同一視しない。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定しない。

### 33-1. 改訂着手の設計承認 (§9・§20)

| 項目 | 内容 |
| --- | --- |
| 承認対象 | ①[../services/travel/design-system/semantic.travel.json](../services/travel/design-system/semantic.travel.json) への `font.heading.weightRegular` (= 既存 primitive `typography.fontWeight.regular` 400 への参照) の追加 (既定 `font.heading.weight` 700 は不変)、②[../services/travel/design-system/design.md](../services/travel/design-system/design.md) の部分更新 (§3 の箇条・§3.1 の表の列名と [決定] の追加/改訂・[根拠] [事実] の追加/改訂)、③[../services/travel/design-system/primitive.travel.json](../services/travel/design-system/primitive.travel.json) の `regular` の `$description` への見出し用途の追記 (値・`$status` は不変)、④[../services/travel/design-system/preview.travel.html](../services/travel/design-system/preview.travel.html) の部分更新 (**非正本**) |
| 承認種別 | **改訂着手承認** ([review-approval-rules.md](review-approval-rules.md) §9・§20)。候補採否とは別の判断 |
| 承認日 | 2026-09-12 |
| 承認主体 | Web部責任者 |
| 根拠 | Task 009-65 の規定のもとでは、見出しへの 400 の使用が既定からの逸脱と判定される。Web部責任者は、明示的な選択肢が thin のみとなっていることを**規定側の誤り**と判断した (2026-09-12。実装側 FAQ の 400 を逸脱と扱わない) |
| 適用範囲 | travel に限定。rental-car / inbound へは及ばない |

### 33-2. 影響度 (§8)

| 項目 | 内容 |
| --- | --- |
| 影響度 | **未取得** (判定主体 = Web部責任者の都度判断 = [review-approval-rules.md](review-approval-rules.md) §8。取得後に本表を更新する) |
| 参考 | 同種の先行判断 = §31 (thin の導入) は**高**。ただし本件は primitive の追加・削除を伴わず (既存 `regular` への参照追加のみ)、対象も travel 1 サービスに限る点で §31 と異なる |

### 33-3. 取得した現在判断 (2026-09-12)

| # | 論点 | 取得した判断 |
| --- | --- | --- |
| J-1 | regular (400) を見出しの選択肢として認めるか | **認める。** Task 009-65 が明示的な選択肢を thin (100) のみとした規定は誤りであり是正する。既定は `font.heading.weight` (700) のまま変更しない。選択のための semantic を別に設ける (`font.heading.weightRegular`) |
| J-2 | 400 を選べる**条件** | **thin と同一 = その幅で実際に適用される実寸が 24px (1.5rem) 以上の見出しに限る。** 要素名 (`h1`〜`h6`) では制限しない。可否の条件体系を両ウェイトで 1 本化する (100 の下限のような描画実測に基づくものではない) |
| J-3 | 進め方 | **既存フロー = Issue 起票 → 本記録への判断記録 → origin/main からの新ブランチで PR** |

### 33-4. 追加・変更するトークン

**semantic (travel のみ)**

| トークン | 変更 | `$value` | `$status` |
| --- | --- | --- | --- |
| `font.heading.weightRegular` | **追加** | `{typography.fontWeight.regular}` (400) | bound |
| `font.heading.weight` | **不変** | `{typography.fontWeight.bold}` (700) | bound |
| `font.heading.weightThin` | **不変** | `{typography.fontWeight.thin}` (100) | bound |

- **primitive は追加・削除・値の変更のいずれも行わない** (`typography.fontWeight.regular` 400 は既存。`$description` への見出し用途の追記のみ)。
- **新しい色値は追加していない。** 本記録が扱うのはウェイトのみである。
- **`$meta.version` は primitive / semantic とも据置き** (bump の条件は各 README の Open Issue として未決)。

### 33-5. 本記録が決定しないこと

- **実装 Repository (`tocoo/tocoo_travel`) 側の適用作業** (FAQ・お問い合わせ等の見出しへの適用・トークンスナップショットの同期)。実装側 FAQ の 400 が本規定の条件 (実寸 24px 以上) を満たすか否かの個別判定も行わない (FAQ `.question` の 1024px 未満の実寸は 20px であり、本規定のもとでは 700 を用いる対象になる — この適合判定は実装側タスクの範囲)。
- **rental-car / inbound の見出しへの 400 の導入。** travel `design.md` §3.1 の選択規則は他サービスへ自動適用しない (P1/ADR-0022)。
- **thin (100) の条件・規定の変更。** §31 の判断はそのまま有効である。
- **本文 (`font.body`) のウェイト。** 正本上いまも未定義であり、本記録では扱わない。
- **`extraBold` (800) の用途。** 選択肢には加えない。
- **適用規格・達成レベルの正式確定・適合判定・適合宣言。**
- **恒久 Decision ID・ADR・正式 Status・Phase・Gate の採番・作成・新設。**


---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (Q1-9 暫定運用の適用状況・新規確認事項7件・未取得の扱いを集約) | Claude Design |
| 2026-07-02 | 是正 S-3 (Q1 に provenance 索引との記述齟齬を注記)・S-6 (サービス識別子の要 ADR を確認事項#8 に追加) | Claude Design (Builder) |
| 2026-07-17 | §4 (Review / Approval Rules 作成前に必要な確認事項) を独立節として追加。Travel Work Order 6 の共通阻害 Fact への対応整理 ([review-approval-rules-creation-plan.md](review-approval-rules-creation-plan.md) 連動)。既存 §1〜§3 の項目・内容・暫定運用案は不変。回答・主体割当は未記入 | Claude Code |
| 2026-07-17 | §4 の全 11 項目へオーナーの明示的回答 (2026-07-17 取得) を記録。表を「確認事項／オーナー回答/残る Open Issue」の列構成へ変更。残る未定・条件付きは Open Issue 列へ分離。既存 §1〜§3 は不変。正式 Status 体系は新設せず、規則正本の作成・承認・適用や Work Order 6 再評価は行っていない | Claude Code |
| 2026-07-17 | Task 009-4: §5 設計承認ログを §1〜§4 と分離して追加。オーナー (Web部責任者) が Governance Review and Approval Rules を Repository 横断規則として明示的に承認 (2026-07-17)。適用開始は本承認記録 PR の main マージ後とし、承認後も残る Open Issue を条件として明記。恒久 Decision ID・正式 Status 体系は新設せず。既存 §1〜§4 は不変。Work Order 6 の再評価・Design System 改定は行っていない | Claude Code |
| 2026-07-17 | Task 009-5: §6 適用開始の事実記録 (Activation Record) を §5 と分離して追加。PR #67 (Task 009-4 承認記録) の main マージ（merge commit d095ded2998e0180ae6836747e8fbbd95a7a2ef1）により、承認時に定めた適用開始条件が成立した Fact を記録（現在状態＝適用中）。merge を設計承認と同一視せず、設計承認は §5 のまま不変。既存 §1〜§5 は不変。恒久 Decision ID・正式 Status 体系・新承認種別は新設せず。Work Order 6 の再評価・Design System 改定は行っていない | Claude Code |
| 2026-07-21 | Task 009-8: §7 Travel上流Open Issue解決単位の案件別判断記録を §1〜§6 と分離して追加。Web部責任者の判断「論点別」(2026-07-21) を Review / Approval Rules §12・§21② に基づくプロセス判断として記録 (設計承認ではない・§5 Design Approval Log へは追加しない)。既存 §1〜§6・設計承認ログ・適用開始記録・規則承認内容は不変。恒久 Decision ID・正式 Status 体系・Phase・Gate は新設せず。上流 Open Issue の内容解決・候補採否・改定要否・改訂着手・設計承認は行っていない。Q2〜Q5 は未回答のまま保持 | Claude Code |
| 2026-07-21 | Task 009-4-F1: §9 Review / Approval Rules 改定の承認記録 (§8 編集的訂正 carve-out) を §1〜§8 と分離して追加。Web部責任者が、非文・誤字脱字・明白な文法／表記誤りの訂正で意味を変えないものを影響度・低とする [review-approval-rules.md](review-approval-rules.md) §8 の明文 carve-out を承認 (2026-07-21、本改定自体の影響度=高)。§17 手順6「規則の変更」の初回実施。§5 初回承認・§6 適用開始・§7・§8 は不変。一般的な高／低の内容基準は引き続き Open Issue (本 carve-out は部分的明文化)。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない。恒久 Decision ID・正式 Status 体系・Phase・Gate は新設せず | Claude Code |
| 2026-07-21 | Task 009-9: §8 Travel上流Open Issue初回着手論点の案件別判断記録を §1〜§7 と分離して追加。Web部責任者の判断「どれからでも構わない」(2026-07-21、最初に扱う論点を特定の 1 件に限定せず T1〜T9 のいずれからでも着手してよい) を Review / Approval Rules §8・§12 に基づくプロセス判断として記録 (設計承認ではない・§5 へは追加しない・§7 の「解決単位＝論点別」は上書きしない)。選択されなかった論点を却下・不要・継続保留とせず、最初に扱う論点の選択を内容承認として扱わない。既存 §1〜§7 は不変。恒久 Decision ID・正式 Status 体系・Phase・Gate は新設せず。上流 Open Issue の内容解決・候補採否・改定要否・改訂着手・設計承認は行っていない。Q2〜Q5 は未回答のまま保持 | Claude Code |
| 2026-07-24 | Task 009-18-BP1: §1 値論点表の Q5 (breakpoint 統一値) 行を是正。旧 Travel 値 `600/768/992/1200` を現行 Travel foundation として記録していた誤記を、Q5 決定 (2026-07-24, Web部責任者) の 3DS 共通 breakpoint = `640/768/1024/1280` (Travel `TVL-0004` の現行 bound 値を再認定・旧値は移行前) へ更新。RC/IB は本共通値へ統一 (breakpoint 値変更・`$status` placeholder 維持)、`TVL-0004` の ADR 正本・provenance 解消は 009-19 へ残す旨を明記。§1 の他 Q・§2〜§9・設計承認ログ (§5) は不変。恒久 Decision ID・正式 Status 体系は新設せず。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-07-27 | Task 009-27R: §10 Travel アイコン体系 (Font Awesome 6) の現在判断記録を §1〜§9 と分離して追加。Web部責任者の 2026-07-27 時点の現在判断 (ⓐ標準 = FA6／ⓑ新規制作は原則 FA6 統一・導入方式は含めない／ⓒ既存 Material は改修時に置換・一括改修や順序/期限/完了条件は含めない／ⓓReviewStars は FA6 `star` 維持・style/weight/package/実装方式/実寸は決めない／ⓔ`icon.reviewSize` の `$value = {iconSize.sm}`・`$status = bound` を維持・実測確認ではない) を **travel 限定**の適用範囲で記録。あわせて §1 値論点表の Q8 (アイコン体系) 行に、3DS 横断統一は未決のまま維持しつつ travel のみ現在判断を取得済みである旨と §10 への参照を追記 (Q8 の削除・「FA6 で解決済み」への置換はしない)。`TVL-0006` の ADR 正本・過去の判断主体・判断日・historical provenance は未確認のまま (009-19 provenance トラックに残る)。§1 の他 Q・§2〜§9・設計承認ログ (§5) は不変。恒久 Decision ID・ADR・正式 Status 体系は採番・作成・新設せず。travel の token・値・`$status`・description・note・Component 仕様、rental-car / inbound の成果物は変更していない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-07-27 | Task 009-27R の記述是正: PR [#105](https://github.com/tocoo/coocom-design-system/pull/105) コードレビュー (issuecomment-5087572255) の指摘に対応し、§10「本記録工程の影響度」行を是正。影響度・高 の取得根拠として記載していた `Task 009-20` は Repository・GitHub Issue のいずれにも存在せず検証できないため、影響度・高 の断定を撤回し **未取得** (本記録工程について影響度を明示的に判定・記録した直接証拠は Repository 内に存在しない) へ変更。あわせて、判定主体 = Web部責任者の都度判断 ([review-approval-rules.md](review-approval-rules.md) §8)、必要レビュー主体 = 影響度判定前は未確定 (同 §10。高 = Web部責任者＋チーフデザイナー／低 = Web部レビュー担当者)、高／低の一般的な明文判定基準は未整備で推測・補完しない (同 §8・§21)、[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L.1 の影響度・低 は R-D 整理工程 (Task 009-19) についての記録であり同 §8L.1・§8L.6 により本記録工程へ適用しない、影響度が明示 (判定・記録) されていない変更をレビュー済み・反映可能として扱わない (同規則 §8) を明記。**是正対象は §10 の当該 1 行のみ**。§10 の他行 (現在判断 ⓐ〜ⓔ・適用範囲 = travel 限定・§1 Q8 との関係・historical provenance 未確認・根拠・Does Not Decide)・§1 Q8 行・§2〜§9・設計承認ログ (§5) は不変。travel の token・値・`$status`・description・note・Component 仕様、rental-car / inbound の成果物は変更していない。恒久 Decision ID・ADR・正式 Status 体系は採番・作成・新設せず。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-07-28 | Task 009-28R: §11 Travel Modal 実装基盤 (drawer) の現在判断記録を §1〜§10 と分離して追加。Web部責任者の **2026-07-27 時点**の現在判断 (ⓐ最終到達方針 = drawer へ統一を維持・即時廃止／一括置換ではない／ⓑ新規は原則 drawer・第3の実装基盤を導入しない・ライブラリ／モジュール／実装方式／DOM 構造は決めない／ⓒ既存 centered dialog は deprecated だが移行期間中の併存を認め改修時に置換要否を確認・一括改修／洗い出し／即時廃止／使用禁止／順序・期限・完了条件は含めない／ⓓ「centered dialog」は非 drawer 型 Modal を指す概念上の呼称であり `M-02`・`_modal_prime` 等の実装実体との対応を認定しない／ⓔ移行対象・順序・期限・完了条件・ロードマップは未決で決定には外部実装 Repository の実査が先行／ⓕ`elevation.overlay`・`elevation.modal` の `bound`・`motion.transition.*` の `placeholder`・follow-up #3／`TVL-0008` との関係および具体挙動は不変) を **travel 限定**の適用範囲で記録。あわせて §1 値論点表の Q9 (モーダル実装基盤) 行に、3DS 横断統一は未決のまま維持しつつ travel のみ現在判断を取得済みである旨と §11 への参照を追記 (Q9 の削除・「drawer で解決済み」への置換はしない)。**判断日 (2026-07-27) と本 Repository 反映日 (2026-07-28) は別の事象として区別**している。本記録工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-07-28、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。`TVL-0007` の ADR 正本・過去の判断主体・判断日・historical provenance・過去の移行ロードマップは未確認のまま (009-19 provenance トラックに残る)。§1 の他 Q・§2〜§10・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。travel の token・値・`$status`・description・note・Component の実装要件・version、rental-car / inbound の成果物、[../services/travel/design-system/alignment-blocking-facts-resolution-plan.md](../services/travel/design-system/alignment-blocking-facts-resolution-plan.md) §8L の R-D 分類は変更していない。同一 Task で `design.md` §7・`components.md` Modal / Overlay の `TVL-0007` 参照・委任表現を補正しているが、Modal の現行仕様そのものは変更していない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-37: §12 Travel 配布物 (バンドル・スナップショット) の生成・管理責務と版の対応付けの現在判断記録を §1〜§11 と分離して追加。依頼元 (ウルトラトクー市 一覧ページ 画面設計・2026-08-03 起票) の依頼 A「バインド DS スナップショットの同期」に対応し、Web部責任者の **2026-08-03 時点**の現在判断 (ⓐ生成・管理責務 = 実装リポジトリ側 `tocoo/tocoo_travel`・生成器/生成手順/更新契機の運用手順は含めない／ⓑ版の対応付け = SOT の `$meta.version` 基準・`$meta.version` の付与規則自体は README §13/§16 の未決 Open Issue で確定しない) を **travel 限定**の適用範囲で記録。あわせて SOT と配布スナップショットの乖離 14 件の確定リスト (semantic のみ +14・primitive 増減なし・`semantic.travel.json` 実測と一致・うち `radius.badge` のみ placeholder)、依頼書の 4 件は 14 件の部分集合であること、配布スナップショット ID `fe4b9e52` が本 Repository の Git object として解決できないこと (`git cat-file -t` = Not a valid object name)、placeholder を配布に含める場合 design.md §9 手順 3 の「🚧 暫定」伝播が及ぶことを Fact として記録。**判断日 (2026-08-03) と本 Repository 反映日 (2026-08-03) は同日だが別の事象として区別**。本記録工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。§1〜§11・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。バンドルの再生成・成果物側の暫定 materialize 削除は本 Repository では行わない (実装リポジトリ側)。travel の token・値・`$status`・`$note`・`$meta.version`・version、rental-car / inbound の成果物は変更していない。`radius.badge` の placeholder → bound 昇格は行っていない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-38: §13 Travel バッジ面色・文字色の現在判断記録を §1〜§12 と分離して追加。依頼元 (2026-08-03 起票) の依頼 B / C に対応し、Web部責任者の 2026-08-03 現在判断 (ⓐ依頼 B = b2 accent 淡色面の新設方向・実色値は未取得で新規 primitive/semantic の実追加は取得後の別作業／ⓑ依頼 C = c1 `color.scheme.*.inverse` の面用途を割引ラベル背景へ拡張・文字色 `color.text.strong` 固定 (main 5.78:1 / sub 7.50:1)・白文字不可・評価色 `color.icon.rating` トークンを面へ流用しない・面用途に専用 semantic 用途トークンは追加せず既存トークンを面として参照／ⓒ依頼元が根拠とする 2026-07-31 の Owner 決定は本 Repository 全体で 0 件・記録が無かった事実を提示のうえ本記録を現在判断として扱い過去の判断主体・判断日は認定しない) を **travel 限定**で記録。判断日 (2026-08-03) と反映日 (2026-08-03) は同日だが別事象として区別。本記録工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。同一 Task で design.md §2.1 の規範規則 (面用途の未定義→定義・文字色固定) と components.md `Card.slot.badge`・`semantic.travel.json` の `$note` を補正しているが、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の色値、rental-car / inbound の成果物は不変。新規 primitive・新規 semantic 用途トークンは追加していない。`radius.badge` の placeholder → bound 昇格は行っていない。§1〜§12・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-38R の記述是正: PR [#121](https://github.com/tocoo/coocom-design-system/pull/121) コードレビュー (issuecomment-5164668167) の指摘に対応し、§13 ⓒ の grep 根拠を是正。「`2026-07-30` / `2026-07-31` / `2026-08-` を含む記述は本 Repository 全体で 0 件」という無スコープ・現在形の断定は、本記録 (2026-08-03 付) の追加後は本記録自身が `2026-08-` を含み自己参照で偽となるため、計測時点を **本記録着手時点 (`main` `cbc19c6`)** に固定した (§12 と同じスコープ付け)。核心の `2026-07-30` / `2026-07-31` は `cbc19c6` 時点で 0 件であり、「当該 Owner 決定は本 Repository 内に記録が無かった」という結論・現在判断 ⓐ b2・ⓑ c1 は不変。**是正対象は §13 ⓒ の当該 1 行のみ**。§13 の他行・§1〜§12・§14・設計承認ログ (§5)・適用開始記録 (§6) は不変。token・値・`$status`・`$note`・`$meta.version`・version、rental-car / inbound の成果物は変更していない。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-41: §14 Travel placeholder / 実査待ちの確認方法・個別確認主体の現在判断記録を §1〜§13 と分離して追加。依頼元 (2026-08-03 起票) の依頼 F「placeholder の解決」に対応し、Web部責任者の 2026-08-03 現在判断 (ⓐ確認方法 = 依頼元 (画面設計) の提出値を受領して確定・実装実測ではない／ⓑ個別確認主体 = 作業担当者が提出値を SOT の placeholder と照合し Web部責任者が確認) を **travel 限定**で記録。review-approval-rules.md §14 が「未定」としていた個別確認主体を定義し、記録先は承認済み規則 review-approval-rules.md §14 本体ではなく本ファイル (規則が Web部責任者に委ねた決定の記録)。あわせて placeholder **11 件** (semantic 4・primitive 7) の確定リストと追跡先 3 区分 (follow-up #13 / #3 / follow-up 番号なし) を記録し、follow-up #3 が §3 に追跡行を持たない不足は R-D トラック (§8L) の既存記録との対応関係のみ整理 (新規解決しない)、依頼書の「10 件」は `radius.badge` 反映前の件数で実測 11 件である旨を記録。判断日と反映日は同日だが別事象として区別。本記録工程の影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。実査 (提出値の受領) は未実施・placeholder は 11 件とも維持・bound 昇格や暫定値の確定は行わない。§1〜§13・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。travel の token・値・`$status`・`$note`・`$meta.version`・version、rental-car / inbound の成果物は変更していない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-39: §15 Travel 依頼 D 新規 Component 定義工程への着手可否の現在判断記録を §1〜§14 と分離して追加。依頼元 (2026-08-03 起票) の依頼 D「Component の不足」に対応し、Web部責任者の 2026-08-03 現在判断 (依頼 D の新規 Component = Pagination / Badge 単体 / Stepper / Empty state の定義工程への着手を可とする。着手可は改訂着手の可否 = review-approval-rules.md §9 のみで Component 仕様・variant 語彙・状態固定リスト・token の新設ではなく仕様定義は別 Task) を **travel 限定**で記録。依頼 D の新規 Component は Work Order 6 の 12 候補とは別であり同 Work Order 6 の「全 12 候補は現時点では開始できない」は不変・依頼 D-6 は #114 の範囲で本記録の対象外である旨を併記。判断日と反映日は同日だが別事象。本記録工程の影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。§1〜§14・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。Component 仕様・variant 語彙・状態固定リスト・token・rental-car / inbound の成果物は変更していない。Design System の候補採否・改定要否・(12 候補の) 改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-40: §16 Travel 依頼 E 規定不足 (省略規則・表記規則の管理正本・繰り返し内 CTA) の現在判断記録を §1〜§15 と分離して追加。依頼元 (2026-08-03 起票) の依頼 E「規定の不足」のうち Owner 判断を要した 3 件について Web部責任者の 2026-08-03 現在判断 (ⓐE-3 施設名の省略規則 = alignment-blocking-facts-resolution-plan.md §8J の UI・Implementation 下流課題分類を維持・DS 層で定めない／ⓑE-4 コンテンツ表記規則の管理正本 = 独立文書 (brand-content.md 等) を新設する方向を確定・作成/中身/管理責務は別 Task／ⓒE-5 繰り返し内 CTA = components.md Button の Do「1 画面の主 CTA は primary 1 つに絞る」を撤回し主 CTA の個数制約を撤廃・強弱階層で優先度を表現) を **travel 限定**で記録。依頼元の 2026-07-3x Owner 例外承認は本 Repository 全体で 0 件・記録が無かった事実を提示のうえ E-5 を現在判断として扱う。E-1 (画像面の scrim)・E-2 (会員限定マスク) は Owner 判断を要さず design.md 未確定事項へ新規起票 (本記録の対象外)。判断日と反映日は同日だが別事象。本記録工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。同一 Task で components.md Button の Do を撤回・変更し design.md §8.1・§2.1・未確定事項を補正しているが、既存 token の値・`$status`・`$meta.version`・version、variant 語彙 (GOV-0002)・状態固定リスト、rental-car / inbound の成果物は不変。§1〜§15・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。brand-content.md の新規作成・§8J 分類の変更は行っていない。Design System の候補採否・改定要否・(12 候補の) 改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-40R の記述是正: PR [#124](https://github.com/tocoo/coocom-design-system/pull/124) コードレビュー (issuecomment-5164668979) の指摘に対応し、§16「依頼元の 2026-07-3x Owner 例外承認の扱い」行の grep 根拠を是正。§13 と同型の自己参照問題 (「`2026-08-` を含む記述は本 Repository 全体で 0 件」が本記録自身の 2026-08-03 付追加後は偽) を、計測時点を **本記録着手時点 (`main` `cbc19c6`)** に固定して是正 (§12 と同じスコープ付け)。核心の `2026-07-30` / `2026-07-31` は `cbc19c6` 時点で 0 件であり、「当該例外承認は本 Repository 内に記録が無かった」という結論・E-5 の現在判断 (Do の撤回・個数制約の撤廃) は不変。§13 ⓒ の同型是正は PR #121 (Task 009-38R) 側で行い本 PR では触れていない (スタック上流の rebase で伝播)。**是正対象は §16 の当該 1 行のみ**。§16 の他行・§1〜§15・設計承認ログ (§5)・適用開始記録 (§6) は不変。token・値・`$status`・`$meta.version`・version は変更していない。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。Design System の候補採否・改定要否・(12 候補の) 改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-03 | Task 009-36: §17 Travel Modal 表示形態 (form) における popover の位置づけの現在判断記録を §1〜§16 と分離して追加。依頼元の依頼 D-6「ボトムシート / アンカー付きポップオーバーの定義追加」に対応し、Web部責任者の 2026-08-03 現在判断 (popover は §11 判断ⓑ の「第3の Modal 実装基盤」に当たらない = overlay の z 軸・backdrop・dismiss を drawer / sheet と共有する同一基盤上の表示形態であり配置方式の相違を実装基盤の相違としない。したがって form 軸に drawer / sheet / popover の 3 値を定義してよく実装基盤は drawer 単一を維持) を **travel 限定**で記録。§11 (Modal 実装基盤 = drawer) は上書きせず判断ⓑ の解釈を明確化。判断日と反映日は同日だが別事象。本記録工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-03、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。同一 Task で design.md §7.1・§5・§2 表・未確定事項と components.md Modal / Overlay・共通事項 (角丸 4 系統) を拡張し、semantic に radius.overlay (radius.lg 参照・placeholder)・color.overlay.backdrop (新規 primitive 参照・placeholder)、primitive に color.palette.blackAlpha.45 (rgba(0,0,0,0.45)・placeholder・実装バンドル観測値を暫定参照) を追加しているが、既存 token の値・$status・$meta.version・version、shadow.* / motion.transition.* の placeholder、rental-car / inbound の成果物は不変。§1〜§16・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。§11 の判断ⓐ〜ⓕ・TVL-0007 の historical provenance・a11y / sheet 最大高 / popover 幅 / 実装 API 名は決定・補完していない。Design System の候補採否・改定要否・(12 候補の) 改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-04 | Task 009-42: §18 Travel セクション間余白の規定不足 (36px 段 spacing.9・位置用途トークン・44px 段・暫定 primitive 直参照) の受理と分類の現在判断記録を §1〜§17 と分離して追加。依頼元 (ToCoo! 国内宿泊トップページ 画面設計・2026-08-04 起票・DS-REQUEST「セクション間余白の規定と 36px 段」) に対応し、Web部責任者の 2026-08-04 現在判断 (ⓐ`spacing.9` = 2.25rem (36px) を 4px 系と整合させ 8 と 10 の間へ `$status = bound` で追加する方向を確定・実追加は別 Task／ⓑ「セクション間」のみ位置用途 semantic トークン化する方向を確定・「セクション内ブロック間」「面色セクション内側 padding」の 2 区分は据置・命名は参照切れの `governance/naming-rules.md` 整備に依存／ⓒ44px 段は追加しない・現状維持・48px 代替運用は追認しない／ⓓ暫定 primitive 直参照は用途トークン定義で解消する方向) を **travel 限定**で記録 (受理と分類の工程)。判断日と反映日は同日だが別事象として区別。本記録工程の影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。同一 PR で design.md 未確定事項の一覧を更新しているが、`spacing.9`・位置用途 semantic トークンの実追加・§4 本体の改訂は行わず (改訂着手の設計承認 §9・§20 を経た別 Task)、既存 token の値・参照先・`$status`・`$meta.version`・version、primitive の spacing スケール、rental-car / inbound の成果物は不変。§1〜§17・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。`governance/naming-rules.md` の新規作成は行っていない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-04 | Task 009-43: §19 Travel 会員限定ラベルの用途区別・会員種別語の表記管轄・`color.text.onAccent` の状態の受理と分類の現在判断記録を §1〜§18 と分離して追加。依頼元 (2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」依頼A + 判断点7) に対応し、Web部責任者の 2026-08-04 現在判断 (ⓐ会員限定 (有料会員限定) ラベルをカテゴリラベルと区別する方向を確定・手段 = 面色使い分け (基本 neutral / 特集 accent / 例外 inverse)・既存トークンの範囲に限定し新色値/新面色用途を先に既成事実化しない・面色成立は §2.1 と Task 009-44 に重なる・用途トークン/区別規則の実定義は別 Task／ⓑ会員種別語 (無料 / 有料会員) の表記はコンテンツ表記規則の管轄で、管理正本の所在 (design.md §8 系集約か独立文書新設か) は Task 009-45 (#130) が扱う論点・本記録で具体表記も管理正本の所在も確定しない／ⓒ`color.text.onAccent` は既に `bound` (Task 009-34) で DS 側の追加不要) を **travel 限定**で記録 (受理と分類の工程)。判断日と反映日は同日だが別事象として区別。本記録工程の影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。同一 PR で design.md 未確定事項の一覧と components.md `Card.slot.badge` の未確定事項を更新しているが、`Card.slot.badge` の規範規則・会員限定ラベルの用途トークン・区別規則の実定義は行わず、`color.text.onAccent` を含む既存 token の値・参照先・`$status`・`$meta.version`・version、rental-car / inbound の成果物は不変。§1〜§18・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。`brand-content.md` の新規作成は行っていない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-04 | Task 009-44: §20 Travel バッジ/ラベルの面色規則不適合 (割引率 #C8912C/白・小サイズ accent/白) の受理と分類の現在判断記録を §1〜§19 と分離して追加。依頼元 (2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」依頼B + 判断点2/4) に対応し、Web部責任者の 2026-08-04 現在判断 (ⓐ実装側の白文字非準拠 (i) 割引率 `#C8912C` 面/白 14px・(ii) 12px campaign accent 面/白 が現行規則 (`Card.slot.badge`・§2.1) に不適合である事実を認識・記録 = `#C8912C`×白 2.78:1・`#C8B12C`×白 2.15:1・accent×白 3.68:1／ⓑ非操作の点的ラベル + campaign accent/scheme 逆色面 に限り白文字を例外として許容する方向を確定・サイズ/ウェイト不問・AA 未達明示・§13/§2.1 の白文字禁止に対する例外で実規則化は別 Task・現行規則は維持／ⓒ白文字成立面は `surface.inverse` (16.10:1) の 1 面のみ／ⓓ§13 の b2 (accent 淡色面) は保留・12px 暫定は §13 の既定 neutral dark 面を維持) を **travel 限定**で記録 (受理と分類の工程)。判断日と反映日は同日だが別事象として区別。本記録工程の影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。同一 PR で design.md 未確定事項の一覧と components.md `Card.slot.badge` の未確定事項を更新しているが、§2.1・components.md の面色・コントラスト規則 (白文字禁止・(i)(ii) 代替・逆色面 `color.text.strong` 固定) を実緩和せず・§13 の記述も編集せず、token の値・参照先・`$status`・`$meta.version`・version・primitive の色値、rental-car / inbound の成果物は不変。§1〜§19・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。新規 primitive・面色用途トークンの追加・b2 実色値の発明は行っていない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-04 | Task 009-45: §21 Travel 割引率の表記規則 (§8.1) の改訂・コンテンツ表記規則の管理正本 (§16 の新設方向の撤回) の受理と分類の現在判断記録を §1〜§20 と分離して追加。依頼元 (2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」判断点5 + DS-REQUEST「割引率の表記規則 (§8.1)」) に対応し、Web部責任者の 2026-08-04 現在判断 (ⓐ§8.1 の基本形を `-NN%` → `NN%OFF` へ変更・マイナス付与規則を撤回する方向・§8.1 L293 の上書き機構に沿い §21 が根拠・実改訂は別 Task／ⓑ「最大NN%OFF」の使用条件を定める方向 = 対象範囲の最大値かつ文脈で判別可・CTP-004・算出/上限は上流未決で据置／ⓒ改訂場所 = §8.1 恒久・§16 の `brand-content.md` 新設方向を撤回し design.md §8 系集約の方向・README も新設しない方向・§16/README/§8.1 本体の実編集は別 Task／ⓓ全角 `％`・`▲` の禁止維持・半角 `%`) を **travel 限定**で記録 (受理と分類の工程)。判断日と反映日は同日だが別事象として区別。本記録工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。同一 PR で design.md 未確定事項の一覧と components.md Card の未確定事項を更新しているが、§8.1 本体 (L287-338)・§16 本体・README の記述は実編集せず、token の値・参照先・`$status`・`$meta.version`・version、rental-car / inbound の成果物は不変。§1〜§20・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。`brand-content.md` の新規作成・割引率の算出式/端数処理/上限値の決定は行っていない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-04 | Task 009-46: §22 Travel 未選択値 (プレースホルダ相当) への color.text.muted 使用の受理と分類の現在判断記録を §1〜§21 と分離して追加。依頼元 (2026-08-04 起票・DS-REQUEST「会員限定ラベルと割引率ラベルの面色」§4.5 + 判断点6) に対応し、Web部責任者の 2026-08-04 現在判断 (ⓐselect の未選択値 (選択前 `option` 相当) に限り `color.text.muted` (#9e9e9e・≈2.7:1) を例外許容する方向・AA 未達明示・§2.3 の muted 流用禁止 (L157)・選択前 `option` → placeholder (L156) への例外で実規則化は別 Task・§2.3 は維持／ⓑ通常 input/textarea の placeholder は `color.text.placeholder` (gray.700・≈6.2:1) を維持／ⓒ未選択値は §2.3 の placeholder 対象に含まれる既定義・placeholder トークンは不変) を **travel 限定**で記録 (受理と分類の工程)。判断日と反映日は同日だが別事象として区別。本記録工程の影響度 = **低** (判定者 = Web部責任者、判定日 = 2026-08-04、本件について明示取得。必要レビュー主体 = Web部レビュー担当者)。同一 PR で design.md 未確定事項の一覧を更新しているが、§2.3 本体 (L154-163) を実編集せず muted 流用禁止規則を実緩和せず、token (`color.text.placeholder` / `muted`) の値・参照先・`$status`・`$meta.version`・version、rental-car / inbound の成果物は不変。§1〜§21・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。依頼元の未選択値 muted 使用・ラベル gray.700 変更を DS 規則として追認していない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-05 | Task 009-47: §23 デザインシステム適用範囲の例外 (広告・非 UI クリエイティブ・画像等) を Governance 横断ルールとして新設することの受理と分類の現在判断記録を §1〜§22 と分離して追加。依頼者 (Web部責任者) の直接依頼 (2026-08-05・Issue [#138](https://github.com/tocoo/coocom-design-system/issues/138)) に対応し、Web部責任者の 2026-08-05 現在判断 (起票時の方向性: ⓐGovernance 横断ルール (3 サービス共通) として新設する方向・実本文は改訂着手の設計承認を経た別 Task／ⓑフォント / カラー / スペーシングのトークン指定外使用のみ例外・WCAG 2.2 AA 最低ライン (R9) は維持) を **Governance 横断 (3 サービス共通)** の適用範囲で記録 (受理と分類の工程)。あわせて新設する例外原則の骨子 4 項目 (対象・許容する逸脱・維持する制約 = R9 維持・適用境界) を定義案として分類し、恒久的な例外原則が 3 サービス design.md 冒頭スコープ行 (travel L7 / rental-car L6 / inbound L6)・§8 (rental-car L83 / inbound L94 は資産提供待ち本版スコープ外・travel §8 に該当なし)・governance/README.md (L35-40 principles 正本未整備) のいずれにも明文化されていない (欠落) 事実を直接証拠で記録。判断日と反映日は同日だが別事象として区別。本記録工程の影響度 = **高** (判定者 = Web部責任者、判定日 = 2026-08-05、本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。新規 Governance ファイルの実本文・各 design.md 冒頭スコープ行・§8・承認済み review-approval-rules.md 本体は実編集せず (原則正本の実本文は §9・§20 設計承認を経た別 Task)、3 サービスの token・値・参照先・`$status`・`$description`・`$meta.version`・version は不変。§1〜§22・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。新規 Governance ファイルの新規作成・rental-car / inbound §8 の書き換えは行っていない。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-05 | Task 009-47R の記述是正: PR [#139](https://github.com/tocoo/coocom-design-system/pull/139) コードレビュー補足 (issuecomment-5186543849) の指摘②に対応し、§23 Does Not 節 (L577) の「承認済み review-approval-rules.md 本体を改定しない」に付していた出典注記 `(CLAUDE.md §11)` を削除。理由 = CLAUDE.md は git 未追跡 (`.git/info/exclude` によるローカル限定除外) で GitHub・新規 clone に存在せずレビュー環境から典拠を辿れないこと、および同一制約を述べる §14 (L319・L358) と §23 自身の規約 bullet (L558) が CLAUDE.md を引用しない引用規律と不整合であること。制約の内容 (承認済み規則本体を改定しない) は不変で、制約のみを記述する形へ揃えた。**是正対象は §23 Does Not 節の当該 1 箇所のみ**。§23 の現在判断 ⓐ・ⓑ・骨子 4 項目・影響度 = 高・欠落の確認結果・他行、および §1〜§22・設計承認ログ (§5)・適用開始記録 (§6) は不変。3 サービスの token・値・参照先・`$status`・`$description`・`$meta.version`・version、各 design.md・[README.md](README.md)・承認済み [review-approval-rules.md](review-approval-rules.md) 本体は変更していない。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。Design System の候補採否・改定要否・改訂着手・設計承認は行っていない | Claude Code |
| 2026-08-10 | Task 009-48〜009-56 (ラベル・タグ定義 A〜H の実装): §24 を追加。ラベル・タグ定義シート (画面設計 Owner 決定 2026-08-07/08-10) の SOT 実装について改訂着手の設計承認 (§9・§20)・影響度=高 (§8)・カテゴリ別の現在判断を記録。primitive/semantic のトークン追加 (accent 2 段・用途色・器・radius.badge=bound) は別 PR、design.md/components.md の実改訂も別 PR。C 特集・E2・F メリット色は据え置き。既存 §1〜§23 は不変 | Claude Code |
| 2026-08-10 | Task 009-48〜009-56 の記述是正 (PR #149 独立エージェント再レビュー issuecomment-5238944112 の指摘に対応): §24-1 根拠欄の自ファイル参照「A 白文字例外 = §20」を「いずれも本記録: … = §20」へ明示し、同小節の承認種別欄が指す [review-approval-rules.md](review-approval-rules.md) §20 との近接による取り違えを解消した。§24 の判断内容 (承認対象・承認種別・影響度・カテゴリ別判断)・§1〜§23・他記述は不変。新規 ADR・Decision ID・正式 Status は採番・新設していない | Claude Code |
| 2026-08-20 | 国内レンタカー DS 0.3.0-draft: §25 を追加。travel 0.3.0-draft の Foundation 定義体系を rental-car へ採用することについて、方向の判断 (2026-08-18)・改訂着手の設計承認 (§9・§20, 2026-08-20)・影響度=高 (§8, 2026-08-20 明示取得)・カテゴリ別の現在判断を記録。§24 は travel 限定・rental-car へ自動適用しないと明記しているため、本 §25 は自動適用ではなく rental-car について別途取得した判断として記録した。3 独立 DS の原則は維持し値は rental-car のファイルに独立して持つ。スキームの正式採用・accent 濃色段の実色・C 特集・E2 は据え置き。既存 §1〜§24 は不変 | Claude Code |
| 2026-09-04 | Task 009-59: §26 Travel 文書レベル見出しの書体選択 (要素ではなく役割で選ぶ) の明文化について、改訂着手の設計承認 (§9・§20, 2026-09-04)・影響度=低 (§8, 2026-09-04 明示取得・必要レビュー主体 = Web部レビュー担当者)・取得した現在判断 3 件 (改訂着手の承認／既定値そのものは不変／明朝を明示選択した場合のウェイトは §3.1 に書かない) を §1〜§25 と分離して追加。契機は [Issue #163](https://github.com/tocoo/coocom-design-system/issues/163)。§5 設計承認ログ・§6 適用開始記録・§7〜§25 の各記録および承認済み [review-approval-rules.md](review-approval-rules.md) 本体は不変。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-05 | Task 009-59R: §26-3 に現在判断 1 件を追加 (2026-09-05・Web部責任者)。サイズ・太さ・行間の既定は**書体の選択と独立**とし、明朝を明示選択しても `h1` の太さ 700 を含む §3.1 の既定が適用される。§3 の「500–600」は書体の用途記述であり太さの既定を置き換えない。見えの太さが書体により異なる点は但し書きとして併記。取得の契機は PR #164 のコードレビュー指摘。§26-1 承認対象・§26-2 影響度 (低)・§26-4 決定しないこと・§1〜§25 の各記録および承認済み [review-approval-rules.md](review-approval-rules.md) 本体は不変。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-05 | Task 009-59R: §26-3 に現在判断 1 件を追加 (2026-09-05・Web部責任者)。文書レベルの見出しで**既定 (サイズ・太さ・行間) から外れる値は原則として認めない**とし、例外を (a) `design.md` §8.3 の適用外 (クリエイティブ)、(b) 利用目的・必然性が明確に示され承認を得たもの の 2 つに限定。承認の主体・手続は §8.3 の宣言運用によるものとし §3.1 では定めない。取得の契機は PR #164 のコードレビュー指摘。§26-1 承認対象・§26-2 影響度 (低)・§26-4 決定しないこと・§1〜§25 の各記録および承認済み [review-approval-rules.md](review-approval-rules.md) 本体・`design.md` §8.3 の本文は不変。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-05 | Task 009-59R2: Task 009-59R の記述是正 (PR [#164](https://github.com/tocoo/coocom-design-system/pull/164) の 2 回目のコードレビュー指摘に対応)。**§26-1 に「是正後の承認対象 (2026-09-05)」の 1 行を追加** — 承認対象の記述が 2026-09-04 時点のままで、撤回済みの②「画面仕様または Component 仕様へ明示記載」を含み、実装後の §3.1 ([決定] 4 行) および §3 の表の 2 行の改訂を覆っていなかったため、是正後の承認対象を明記した。**§26-3「既定から外れる値の可否」行を書き換え** — ①**承認主体 = Web部責任者**を明記 (従前は「承認の主体・手続は §8.3 の宣言運用による」としていたが、§8.3 の運用は自己宣言であって承認行為ではなく、審査主体の設置は同節の [事実] のとおり未了であるため、承認を求める相手が正本上存在しない状態だった)。②例外を **(a)(b) の閉じた列挙から、単一の基準 (利用目的とデザイン上の必然性の提示＋承認) ＋例示へ改めた** (従前の「(a) §8.3 の適用外、(b) LP 等に限る」は、§8.3 の適用外の列挙が LP を含まないため「§8.3 に従う」と両立しなかった。Web部責任者判断 2026-09-05 =「2 つに限らない」)。③**Component の逸脱**は §3.1 が既に定める「当該 Component 仕様へ明示記載」に一本化し別途の承認を要求しないことを明記 (Web部責任者判断 2026-09-05)。**不変**: §26-1 の承認種別・承認日 (2026-09-04)・承認主体・根拠・適用範囲、§26-2 の影響度 (低・判定日 2026-09-04)、§26-3 の他 4 行、§26-4、§1〜§25 の全記録、設計承認ログ (§5)、適用開始記録 (§6)。**作成・追加していないもの**: 承認手続 (申請様式・記録先・期限) の定義、`design.md` §8.3 の本文変更、§8.3 の適用外の列挙への LP の追加、審査基準・審査主体の設置 (Task 009-55 の範囲)、新規 primitive・token。承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定していない。影響度は Task 009-59 と同じく**低** (判定者 = Web部責任者・判定日 2026-09-04)。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-05 | Task 009-60: §27 「Travel C カテゴリ・特集ラベルの用途色と accent の帰属 (B 有料会員 / C 特集) の確定」を §1〜§26 と分離して追加 ([Issue #162](https://github.com/tocoo/coocom-design-system/issues/162))。Web部責任者の 2026-09-05 現在判断 (ⓐ accent は**面 = B 会員種別 / 点 (アイコン) = C カテゴリ・特集**で役割分離し C の面は白とする／ⓑ 用途色 `color.label.category` (`surface` / `text` / `icon` の 3 件・既存 semantic への参照のみ・新色値なし) を `semantic.travel.json` に定義する／ⓒ 12px は白面 × `color.text.strong` ≈16.10:1 で成立し C は (i) (ii) の代替 2 択に依存しない・accent はアイコン (非テキスト 3:1) に限る／ⓓ 実装 3 分岐を C の用途色へ寄せ、`design.md` §2.1 の白文字例外の適用範囲を **A 割引率ラベル + scheme 逆色面**へ縮小して `components.md` の (i) (ii) 代替 2 択との読みの割れを解消する／ⓔ C のウェイトは既存規則どおり 700) を **travel 限定**で記録。改訂着手の設計承認 (§9・§20) 取得済み (承認主体 = Web部責任者・承認日 2026-09-05)。影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-05・本件について明示取得。必要レビュー主体 = Web部責任者およびチーフデザイナー)。同一 PR で `design.md` (§2 要約表 1 行追加・§2.1 検証表 1 行追加・白文字例外の縮小・未確定事項の一覧の更新と 1 行追加)・`components.md` (`Card.slot.badge` の C 行・白文字例外・関連トークン・未確定事項)・`semantic.travel.json` (`color.label.category` 3 件の追加と 3 箇所の記述是正) を改訂している。**不変**: §1〜§26 の各記録 (§13 b2・§19 面色使い分け・§20 白文字例外の方向・§24 ラベル・タグ定義の実装を含む)・設計承認ログ (§5)・適用開始記録 (§6)、`color.membership.paid` / `color.accent.campaignTint` / `campaignInk` の値・参照先・`$status` (placeholder)、accent 濃色段・coral 2 段の 🚧 仮色、primitive の色値、`$meta.version`、rental-car / inbound の成果物。**決定していないもの**: accent 濃色段/coral の実色値・b2 の 4.5:1 検証・白面 C ラベルの白系面上での分離手段 (境界線の要否)・E2 / F / H の未決事項・スキームの正式採用・実装 Repository 側の適用作業。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。承認済み [review-approval-rules.md](review-approval-rules.md) 本体は改定していない | Claude Code |
| 2026-09-05 | Task 009-60R: §27 に**現在判断 ⓕ を追加** (PR [#165](https://github.com/tocoo/coocom-design-system/pull/165) のコードレビュー指摘に対応)。ⓓ が「実装 3 分岐すべてを `color.label.category` へ統一」と指示する一方、C の面を白と確定した結果、白いカード面・`surface.subtle` の上では面のみで境界が生じない (白 × 白 = 1.00:1・白 × `surface.subtle` = 1.05:1・本 Repository で実測) にもかかわらず、§27-4 は分離手段を「本記録が決定しないこと」に置いたままだった。**ⓕ = 白系の面 (`color.surface.default` / `color.surface.subtle`) の上に置く場合にのみ `color.label.category.border` (= `color.border.default` `#CCCCCC`) の枠線を `border.width.thin` (1px) で引く**。写真の上・有色面の上では引かない。値の選定根拠として既存 border 3 段の白面上コントラスト (`subtle` 1.32:1 / `default` 1.61:1 / `strong` 1.90:1) を実測し、**非テキスト UI 要素の 3:1 に達する既存の border トークンが存在しない**ことと、3:1 未達を明示して適合宣言を行わないことを記録した。あわせて §27-1 の承認対象を `color.label.category` の **4 件** (`surface` / `text` / `icon` / `border`) へ更新し、§27-4 から分離手段の項を外して**アイコンのサイズ**の項を加えた (`iconSize.sm〜xl` の最小段 16px に対し器 sm は高さ 20px・文字 12px で、当てる値が正本に無い)。**不変**: §1〜§26 の各記録・§27-1 の承認種別/承認日/承認主体/適用範囲・§27-2 の影響度 (高) と必要レビュー主体・§27-3 の ⓐ〜ⓔ・設計承認ログ (§5)・適用開始記録 (§6)、`color.membership.paid` / `campaignTint` / `campaignInk` の `$status` (placeholder)、primitive の色値、rental-car / inbound の成果物。**決定していないもの**: C ラベルのアイコンのサイズ・accent 濃色段/coral の実色値・b2 の 4.5:1 検証・写真/グラデーション上の scrim (依頼 E-1)・E2 / F / H の未決事項・スキームの正式採用・実装 Repository 側の適用作業。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設せず。承認済み [review-approval-rules.md](review-approval-rules.md) 本体は改定していない | Claude Code |
| 2026-09-07 | Task 009-62: §28 「Travel ブレークポイントごとの文書レベル見出しのサイズ段 (既定の適用幅・狭い幅での段下げ・4 の倍数規則) の確定」を §1〜§27 と分離して追加 ([Issue #168](https://github.com/tocoo/coocom-design-system/issues/168)・Web部責任者判断 2026-09-07)。改訂着手の設計承認 (§9・§20)・影響度 = **高** (判定者 = Web部責任者・判定日 2026-09-07・明示取得)・現在判断 7 件 (ⓐ 一意の段下げ表を DS が定める／ⓑ 既定は `breakpoint.lg` 1024px 以上に適用し 1024px 未満は h1 `3xl` / h2 `2xl` / h3 `xl` / h4〜h6 `md`・境界は 1024px の 1 つのみ／ⓒ 表の範囲内の段下げは §3.1 の「既定から外れる」に該当せず都度承認不要／ⓓ `font.heading.h5Size` の参照先を `{typography.size.lg}` から `{typography.size.md}` へ変更・見出しには実寸が 4 の倍数の段のみを用いる／ⓔ `sm` 14px は対象外で TVL-0002 の適用範囲を `typography` 全体へ拡げない／ⓕ `alignment-blocking-facts-resolution-plan.md` §8J との優先関係 = 見出しのサイズ段は §3.1 が上位・§8J の分類自体は不変／ⓖ 見本ページを幅追従にする) と Does Not Decide を記録した。**§12 の表 10 行目 (`font.heading.h5Size` = `{typography.size.lg}`) は `main` `cbc19c6` 時点の Fact として遡及変更していない。§26 本体・§27 本体・§5 設計承認ログ・§6 適用開始記録・承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定していない。** | Claude Code |
| 2026-09-07 | Task 009-63: §29 「国内レンタカー (rental-car) DS — 国内宿泊 (travel) 最新版 (Task 009-58〜009-62) の適用」を §1〜§28 と分離して追加 ([Issue #170](https://github.com/tocoo/coocom-design-system/issues/170))。改訂着手の設計承認 (§9・§20, 2026-09-07)・影響度 = **高** (§8, 2026-09-07 明示取得・必要レビュー主体 = Web部責任者およびチーフデザイナー)・取得した現在判断 7 件 (D-2 `font.heading.h3Size` を 24px へ揃える／D-4 文書レベル見出しに実寸 4 の倍数の段のみを用いる (`font.display.mdSize` 18px は対象外)／F-5 入力要素の角丸を `radius.action` (pill) へ統一し `radius.input` を廃止／F-1 Modal の表示形態 (form = drawer / sheet / popover) を正式仕様にし旧「拡張候補 (未承認)」を廃止／F-4 主 CTA の個数制約を設けない／C-5 Select の未選択値のみ `color.text.muted` を例外許容 (AA 未達明示)／H-1・H-2 DS 見本ページと design-system 入口 README を新設し生成器を複数サービス対応にする) と、これに付随して明文化する 5 項目 (A 割引率ラベルに限る白文字の例外・accent の帰属 (面 = B / 点 = C)・白系の面上での C の枠線・`labels-tags.rental-car.md` C1 の記述是正・表記規則 3 節)、トークンの追加/変更 (semantic **40 件追加・1 件削除・1 件の参照先変更**、primitive **4 件追加**。うち 3 段は 🚧 仮色)、適用しない / 維持する分、Does Not Decide を記録した。**本記録は §25〜§28 からの自動適用ではなく、rental-car について別途取得した判断である** (§26 / §27 / §28 はいずれも適用範囲を travel に限定と明記しており、§25 も §24 の自動適用ではない形で記録されている)。**§24・§25・§26・§27・§28 の判断内容・適用範囲・§5 設計承認ログ・§6 適用開始記録・承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定していない。** travel / inbound の成果物・token・値・`$status`・`$meta.version` は変更していない。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設していない | Claude Code |
| 2026-09-07 | Task 009-63R: §29 の記述是正 (PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) コードレビュー [issuecomment-5565532746](https://github.com/tocoo/coocom-design-system/pull/171#issuecomment-5565532746) の指摘に対応)。①§29-1 承認対象③・§29-2 判定の位置づけの「7 節を新設」を実測値の **8 節**へ是正した (§2.4 / §2.5 / §2.6 / §3.1 / §7.1 / §8.1 / §8.2 / §8.3。同 §29-1 根拠欄は既に「8 節」と記載しており同一節内で矛盾していた)。②**§29-3 判断 C-5 の適用範囲を変更**した — Web部責任者の 2026-09-07 判断 (明示取得)「未入力時の状態を特定の UI に限定しない。`color.text.muted` に統一」により、`input` / `textarea` の `::placeholder`・Select の未選択値・その他の入力フィールドの未入力表示のすべてを `color.text.muted` (2.68:1・**AA 未達明示**) とし、プレースホルダ専用トークン `color.text.placeholder` の追加を取り下げた。これに伴い §29-1 承認対象①・§29-2・§29-4 の semantic 追加件数を **40 件 → 39 件**へ、§29-1 承認対象③の節名を「§2.6 プレースホルダ」から「§2.6 未入力状態の文字色」へ是正した。**適用範囲は rental-car に限定**し、travel の §22 (2026-08-04 判断・Select の未選択値のみ) および inbound の成果物は不変。③本記録は Design System の適用規格・達成レベルの正式確定・適合判定・適合宣言を行わない。§1〜§28・設計承認ログ (§5)・適用開始記録 (§6) は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設していない | Claude Code |
| 2026-09-07 | Task 009-63R2: §29 に**判断 F-6 を追加取得**して記録した — Modal の `sheet` の最大高を **`90vh`**、`popover` の幅を **`240〜320px`** として**確定する** (Web部責任者判断 2026-09-07・明示取得・影響度 = **高**・必要レビュー主体 = Web部責任者およびチーフデザイナー)。契機は PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) のコードレビューが検出した、正本 [../services/rental-car/design-system/design.md](../services/rental-car/design-system/design.md) §7.1 の「未確定として残す」と `components.md` の `🚧` なしの確定値記載との食い違いである。**確定した値は `components.md` に既にあったものと同一**で新しい値は発明していない。これに伴い §29-6 の「決定しないこと」から当該 2 項目を外した。**適用範囲は rental-car に限定**し、travel (§17 の Does Not Decide・travel `design.md` §7.1 の未確定) ・inbound は不変 (本行の「travel は不変」は F-6 の対象である §7.1 についての記述である。同じ Task 009-63R2 で travel `design.md` §2.1 代替規則 1 の記述是正を行っており、その承認対象・影響度は Task 009-63R3 で §29-1 承認対象⑩・§29-2 へ記録した)。§29-3 の既存 7 件 (D-2 / D-4 / F-5 / F-1 / F-4 / C-5 / H-1・H-2)・§29-1・§29-2・§29-4・§29-5・§1〜§28・設計承認ログ (§5)・適用開始記録 (§6)・承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は不変。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設していない | Claude Code |
| 2026-09-07 | Task 009-63R3: §29 の記述是正と**判断 F-7 の追加取得** (PR [#171](https://github.com/tocoo/coocom-design-system/pull/171) コードレビュー 3 回目 [issuecomment-5567573901](https://github.com/tocoo/coocom-design-system/pull/171#issuecomment-5567573901) の指摘に対応)。①**§29-3 に判断 F-7 を追加**した — C カテゴリ・特集ラベル (C1 / C2) を**写真の上に置いてよい**とし、写真の上に置けるのは **A 割引率と C の 2 カテゴリ**とする (Web部責任者判断 2026-09-07・明示取得)。契機は、本 PR で新設した rental-car `design.md` §2.4 の [決定] と `labels-tags.rental-car.md` A 節「写真の上に置けるのは A だけ」との食い違いである。**適用範囲は rental-car に限定**。②**§29-1 の承認対象に⑩ travel `design.md` の部分更新を追加**し、§29-1 適用範囲と §29-2 影響度に同⑩の扱い (影響度 = **高**・判定者 = Web部責任者・判定日 2026-09-07・明示取得) を記録した — 本 PR は travel `design.md` §2.1 代替規則 1 の記述是正を含むにもかかわらず、承認対象・影響度の記録が本書に無かった。③**2026-09-07 Task 009-63R2 の行の「travel は不変」に注記**を補い、当該記述が F-6 の対象である travel §7.1 についてのものであることと、§2.1 の記述是正が承認対象⑩に記録されていることを明記した。**不変**: §29-3 の既存 8 件 (D-2 / D-4 / F-5 / F-1 / F-4 / C-5 / H-1・H-2 / F-6) の判断内容、§29-4・§29-5・§29-6、§1〜§28 の判断内容・適用範囲、設計承認ログ (§5)、適用開始記録 (§6)、承認済みの [review-approval-rules.md](review-approval-rules.md) 本体。恒久 Decision ID・ADR・正式 Status・Phase・Gate は採番・作成・新設していない | Claude Code |
| 2026-09-07 | Task 009-64: §30 「Travel `design.md` §2.1 検証表の欠落の回収と Breadcrumb 現在地の文字色の確定」を §1〜§29 と分離して追加 ([Issue #172](https://github.com/tocoo/coocom-design-system/issues/172))。改訂着手の設計承認 (§9・§20、2026-09-07・Web部責任者)・**影響度 = 高** (判定者 = Web部責任者・判定日 2026-09-07・明示取得・必要レビュー主体 = Web部責任者およびチーフデザイナー)・取得した現在判断 **2 件** (G-1 = 白面 × `color.text.muted` 2.68:1 を検証表へ載せず **Breadcrumb 現在地の文字色を `color.text.mutedStrong` `#616161` 6.19:1 へ変更**して AA 未達を解消する／G-2 = 影響度)・検証表へ追加する **10 行**の実測値・本記録が決定しないこと **8 項目**を記録した。**適用範囲 = travel に限定**し rental-car・inbound へは及ぼさない (3 独立 DS の原則 P1/ADR-0022)。とくに §29-3 判断 C-5 (rental-car の未入力状態の案内文字を `color.text.muted` に統一・AA 未達明示) とは扱いが異なるが、**同判断の内容・適用範囲は変更しない**。**トークンの追加・削除・値の変更・参照先の変更・`$status` の変更は 0 件**。**不変**: §1〜§29 の各記録、[review-approval-rules.md](review-approval-rules.md) 本体。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-07 | Task 009-64R: §30 の記述是正と**承認対象①の範囲拡大** (PR [#173](https://github.com/tocoo/coocom-design-system/pull/173) のコードレビュー 2026-09-07 の指摘 6 件に対応)。①**§30-1 承認対象①の行数を「10 行追加」から「21 行追加」(14 行 → 35 行) へ拡大**し、既存 1 行の概算 `≈11.1:1` の実測値 `11.11:1` への是正と既存 5 行への「主色」の明示を承認対象へ加えた (Web部責任者判断 2026-09-07)。②**§30-5 に「PR #173 のコードレビューを契機に追加した 11 行」の表を追加**した — 同レビューが名指しした 5 組 (`color.tag.neutral` 9.22:1・`color.label.stock` 主色 4.77:1 / 副色 4.53:1・`color.membership.free` 13.21:1・Button `secondary` 16.10:1・`surface.inverse` × `mutedStrong` 2.60:1 = **禁止**) と、per-scheme の判定基準を表全体へ一貫させるための**副色スキームの campaign accent 5 組** (3.79:1 / 4.24:1 / 3.79:1 / 3.60:1 / 3.48:1)。副色の `campaignTint` / `campaignInk` は 🚧 仮色のため追加しない。③**per-scheme の判定基準を [事実] として明記**した — 主色・副色で行を分けるか否かは `semantic.travel.json` の解決チェーンではなく **§2 の用途表が per-scheme トークンとして定義しているか否か**による (`color.action.primary.bg` と `color.text.link` は JSON 上いずれも `{color.scheme.main.base}` へ解決するが前者は per-scheme ではない)。**トークンの追加・削除・値の変更・参照先の変更・`$status` の変更は引き続き 0 件**。**不変**: §30-2 影響度 (**高**)・§30-3 判断 G-1 / G-2 の内容・§30-4 (トークン変更なし)・§30-6 決定しないこと、§1〜§29 の各記録、[review-approval-rules.md](review-approval-rules.md) 本体。新規 ADR・Decision ID・正式 Status・Phase・Gate は作成・採番・新設していない | Claude Code |
| 2026-09-11 | Task 009-65: §31 「Travel 文書レベル見出しの太さ 100 (thin) の導入と `typography.fontWeight` スケールの配信段への整合 (travel / rental-car)」を §1〜§30 と分離して追加 ([Issue #174](https://github.com/tocoo/coocom-design-system/issues/174))。改訂着手の設計承認 (§9・§20、2026-09-11・Web部責任者)、影響度 = **高** (§8、2026-09-11・明示取得)、現在判断 7 件 (H-1 既定は 700 のまま 100 を明示的な選択肢として足す／H-2 選べる要素を `h1`〜`h6` の要素名では制限しない／H-3 §3.1 の [決定]「新しいウェイト値は追加しない」を改訂する／H-4 選べるのは実寸 24px 以上の見出しに限る／H-5 書体が配信していないウェイトは記述を削除し、配信されているウェイトは追加する／H-6 H-5 の適用は travel と rental-car の 2 サービス・inbound は書体規定が暫定のため保留／H-7 影響度 = 高) を記録した。§31-4 に追加・変更するトークン (primitive = `thin` 100 と `extraBold` 800 を追加・`medium` 500 と `black` 900 を削除／semantic = travel のみ `font.heading.weightThin` を追加・既定 `font.heading.weight` 700 は不変) を、§31-5 に本記録が決定しないこと 9 件を記載した。**§5 設計承認ログ・§6 適用開始記録・§7〜§30 の各記録は変更していない。** 承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定していない | Claude Code |
| 2026-09-11 | Task 009-66: §32 「リポジトリ入口 README ほか 3 文書の記述の最新化」を §1〜§31 と分離して追加 ([Issue #176](https://github.com/tocoo/coocom-design-system/issues/176))。Web部責任者の**改訂着手の設計承認 (2026-09-11)**・**影響度 = 低 (本件について明示取得)**・現在判断 I-1〜I-3 (反映経路 = PR・対象範囲 = 入口 4 文書・影響度) を記録。あわせて 4 文書で揃える記述上の扱い (§32-4) — **「12 候補の改訂 (未着手)」と「案件ごとの改訂着手承認に基づく改定 (継続中)」の書き分け**・`tools/` が 5 レイヤー外の非正本であること・DS 見本ページが非正本であること — を記録。**Design System のトークン値・`$status`・`$meta.version`・規則・Component 仕様は変更していない。**Work Order 6 の総合判断 (全 12 候補「現時点では開始できない」)・[review-approval-rules.md](review-approval-rules.md) 本体・既存 §1〜§31 は不変 | Claude Code |
| 2026-09-12 | Task 009-67: §33 「Travel 文書レベル見出しの太さの明示的な選択肢への regular (400) の追加 — Task 009-65 の thin (100) 限定の是正」を §1〜§32 と分離して追加 ([Issue #178](https://github.com/tocoo/coocom-design-system/issues/178))。改訂着手の設計承認 (§9・§20、2026-09-12・Web部責任者)、影響度 = **未取得** (§8・取得後に §33-2 を更新)、現在判断 3 件 (J-1 regular 400 を既定 700 に対する明示的な選択肢として認める・§31 の thin 限定は誤りとして是正／J-2 条件は thin と同一 = 実寸 24px 以上・要素名では制限しない／J-3 進め方 = 既存フロー) を記録した。§33-4 に追加・変更するトークン (semantic = travel のみ `font.heading.weightRegular` を追加。primitive は追加・削除・値の変更なし・`regular` の `$description` 追記のみ。既定 `font.heading.weight` 700・`weightThin` 100 は不変) を、§33-5 に本記録が決定しないこと 7 件を記載した。**§5 設計承認ログ・§6 適用開始記録・§7〜§32 の各記録は変更していない。** 承認済みの [review-approval-rules.md](review-approval-rules.md) 本体は改定していない | Claude Code |
