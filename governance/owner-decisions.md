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
