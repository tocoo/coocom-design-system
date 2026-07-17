# Travel Alignment Amendment Candidate Separation

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Alignment Assessment のうち、Work Order 4 ([alignment-observations-aggregation.md](alignment-observations-aggregation.md)) で集約された Observation を、Work Order 1 の証拠制約を保持しながら「改訂を検討し得る候補」と「未解決に依存し確定できない事項」へ分離した記録。Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 5「改訂候補と未解決事項の分離」の実行。改訂の具体内容・解決策・優先順位・Design System の改定要否・改訂着手可否は決定しない。
- Position in Repository: `services/travel/design-system/alignment-amendment-candidate-separation.md` — Design System レイヤー (travel サービス配下)。Design System README の Reference Order 上で自身より前に配置される上流成果物は、レイヤー入口 [README.md](README.md)・Alignment 計画 [alignment-plan.md](alignment-plan.md)・Baseline 評価 [baseline-assessment.md](baseline-assessment.md)・Service Design 横断整合性評価 [service-design-alignment-assessment.md](service-design-alignment-assessment.md)・Screen Requirements 個別整合性評価 [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md)・Observation 横断集約 [alignment-observations-aggregation.md](alignment-observations-aggregation.md)。Service Design 成果物・Screen Requirements 成果物・既存 Design System 4 成果物との関係は本文 Sources (§8) / Method (§9) / Separation Traceability Index (§12) / 各分離節 (§13〜§15) に記載し、Position の上流成果物へ混在させない。下流成果物 (Assets / Implementation) との関係は Downstream Impact (§21) を参照。

本文書は分離記録であり、Design System 仕様・Design Decision・改訂候補の採用一覧の正本ではない。分離は Work Order 4 が集約済みの Observation を「改訂を検討し得る候補」と「未解決に依存し確定できない事項」へ整理するものであり、新しい Observation・分類・Decision を追加しない。評価上の観察区分 (Alignment Plan §8) を Repository 成果物の正式 Status・優先度・severity と混同しない。ファイル名 `alignment-amendment-candidate-separation.md` は記述的な暫定識別子であり、正式な分類体系・候補 ID・Issue ID・命名規則を確定しない。Work Order 4 の T/C/X ラベルは入力文書内の説明用 Topic であり正式 ID ではない。本文書もこれらを正式 ID へ昇格させず、新しい候補 ID・未解決事項 ID・優先度 ID を採番しない。SCR ID は Screen Matrix 上の画面候補 ID であり、Screen Requirement 文書 ID・実装画面 ID・URL・route と同一視しない。Fact / Decision / Hypothesis / Open Issue を区別し、新しい Design Decision・UX Decision を追加しない。

## 1. Purpose

- Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 5「改訂候補と未解決事項の分離」を実行する。
- Work Order 4 で集約された Observation を、(1) 改訂を検討し得る候補、(2) 上流・業務仕様・provenance 等の未解決に依存し確定できない事項、(3) いずれにも変換すべきでない分離対象外の Observation、へ整理する。
- 元 Observation・出典・provenance・placeholder・実査待ち・参照切れ・Open Issue・Does Not Decide を失わず、Separation Traceability Index (§12) で追跡可能にする。
- 「候補と未解決事項へ分離する」ことと「改訂内容を決める / 解決策を提案する / 優先順位を付ける / Design System の改定要否を判断する / 改訂着手可否を判断する」ことを区別する。後者は本文書では行わない (§20・§23)。
- 分離結果は Work Order 6「実際の改訂タスクを開始できるかの判断 (改訂着手可否の判断)」の入力とする。

## 2. Status

- 本文書の Status は `Draft` である。
- 入力の集約文書・評価文書・計画文書はいずれも Draft である。分離が入力文書の Status を昇格させることはない。
- Work Order 5 を Draft として実施済みと記載する条件は §20 Work Order 5 Completion Boundary に定義する。

## 3. Position

- 本文書は Design System レイヤー (travel サービス配下) の 6 番目の Alignment 記録である。
- Design System README の Reference Order 上で自身より前にある上流成果物として本文書が参照できるのは、[README.md](README.md)・[alignment-plan.md](alignment-plan.md)・[baseline-assessment.md](baseline-assessment.md)・[service-design-alignment-assessment.md](service-design-alignment-assessment.md)・[screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md)・[alignment-observations-aggregation.md](alignment-observations-aggregation.md) のみ。
- Service Design 成果物 (SD-001〜SD-007)・Screen Requirements 成果物 (作成済み 7 個別 Screen Requirement)・既存 Design System 4 成果物 (`design.md` / `semantic.travel.json` / `primitive.travel.json` / `components.md`) との関係は、上流 Position へ混在させず、本文 Sources (§8)・Method (§9)・Separation Traceability Index (§12)・各分離節 (§13〜§15) に記載する。
- Assets と Implementation は下流成果物であり Downstream Impact (§21) に分離する。

## 4. Purpose Boundary（分離と再評価・改訂の区別）

- 本文書は Work Order 4 が集約済みの Observation を分離する。既存 Design System 4 成果物・Service Design・Screen Requirements・Governance を再評価しない。Work Order 4 の集約 Topic とその元出典を追跡し、分離に必要な範囲で入力評価文書を確認する。
- 分離は Observation の観察区分・provenance・placeholder・実査待ち・参照切れ・Open Issue・Does Not Decide を変更・解決・昇格させない。
- 「改訂を検討し得る候補」への記載は、改訂すべきという Decision・改定要否の決定・新規 Component/token の必要性確定・改訂内容の確定・改訂着手可能・優先順位の確定・承認済みのいずれも意味しない (§13 冒頭に再掲)。

## 5. Separation Snapshot

- Separation target: 作業開始時点の `main`。
- Separation snapshot (main commit SHA): `8fdfd1b5d3524768f4f9b8679cfedd2d51ecb1c3` (PR #53 merge)。
- 分離日: 2026-07-17。
- 本作業は Repository 内文書の静的な分離記録であり、実装検証ではない。既存 Design System 4 成果物は再評価せず、入力評価文書の直接証拠を追跡する。作業中に main の更新はなく、異なる snapshot を混在させていない。
- Work Order 4 の T-01〜T-07 / C-01〜C-10 / X-01〜X-07 ラベルは入力文書 (alignment-observations-aggregation.md) 内の説明用 Topic であり、正式 ID ではない。

### 入力文書 (blob SHA @ `8fdfd1b`)

| 入力 | ファイル | 役割 | blob SHA |
| --- | --- | --- | --- |
| 主入力 (Work Order 4) | [alignment-observations-aggregation.md](alignment-observations-aggregation.md) | 集約 Observation (分離対象) | `89ef99de6da00b226bb12445d7dfe253e49a2e84` |
| 方法・境界 | [alignment-plan.md](alignment-plan.md) | 評価方法・分類・順序 (§5〜§10) | `0296b435e6394da840031bb50dd8aaed471a261d` |
| 証拠制約 (Work Order 1) | [baseline-assessment.md](baseline-assessment.md) | token/placeholder/provenance/参照切れ | `89ea9d17257cf2e5b162dc702944b21033ef71e2` |
| 追跡確認 (Work Order 2) | [service-design-alignment-assessment.md](service-design-alignment-assessment.md) | SD 横断責務の元 Observation | `528b3cccc0bb0c91ec3a1a8a233f8ff28152475b` |
| 追跡確認 (Work Order 3) | [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) | 7 SCR の元 Observation | `521d3b54d9cba455c2b07db4edfb059865447a28` |

### 分離が追跡する既存 Design System 4 成果物 (再評価しない)

- [design.md](design.md) / [semantic.travel.json](semantic.travel.json) / [primitive.travel.json](primitive.travel.json) / [components.md](components.md)。いずれも Draft・version `0.3.0-draft`。本文書はこれらを再評価せず、入力評価文書が記録した直接証拠を追跡する。

## 6. Scope

- Work Order 4 の集約 Observation (T-01〜T-07・C-01〜C-10・X-01〜X-07、§16 Source-specific Variations、§17 provenance/placeholder/実査待ち/参照切れの影響、§18 Conflict and Over-coverage、§19 Unresolved Dependencies) を分離対象とする。
- 分離単位は Topic 全体の機械的な一括分類ではなく、Topic に含まれる「設計責務と Observation の組み合わせ (側面)」とする (§9・§11)。
- 1 つの Topic に「DS 側の定義不足として記録できる側面」と「上流 Open Issue・provenance・placeholder・実査待ち等に依存する側面」の両方が含まれる場合、Topic 全体をどちらか一方へ丸めず、側面を分けて別々に記録する。
- 同じ T/C/X Topic を複数の分離レコードから参照できる。新しい恒久 ID は採番しない。

## 7. Out of Scope

- 改訂候補の採用・却下、改訂内容・解決策の提案。
- Design System の改定要否判断、改訂着手可否の判断 (Work Order 6)。
- gap の原因責任の決定、優先順位・重要度・severity・対応順・工数・担当者・期限・Milestone の決定。
- 候補ごとの `ready` / `blocked` / `approved` 等の状態付与、新規 Issue への分解。
- 実際の Design System 変更、新規 Component/token/pattern/文書の提案。
- 承認主体の推測。
- 既存 Design System 4 成果物・Service Design・Screen Requirements・Governance の再評価・修正。
- SCR-006〜SCR-012 の評価・要求定義。
- 数値スコア・適合率・カバレッジ率・件数ランキング・pass/fail・severity・優先順位の導入。

## 8. Sources

Position の上流成果物 (README / alignment-plan / baseline-assessment / service-design-alignment-assessment / screen-requirements-alignment-assessment / alignment-observations-aggregation) と区別し、本分離が対象・参照とする成果物を示す。

- **主入力 (分離対象)**: [alignment-observations-aggregation.md](alignment-observations-aggregation.md) (Work Order 4)。集約 Topic T-01〜T-07・C-01〜C-10・X-01〜X-07 と §16〜§19。
- **方法・境界**: [alignment-plan.md](alignment-plan.md) (§5 Assessment Unit / §6 Evidence Rules / §8 Observation Classification / §9 Assessment Dimensions / §10 Recommended Work Order)。
- **証拠制約・追跡確認**: [baseline-assessment.md](baseline-assessment.md) (Work Order 1)・[service-design-alignment-assessment.md](service-design-alignment-assessment.md) (Work Order 2)・[screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) (Work Order 3)。集約 Topic の元出典を追跡し、分離に必要な範囲で確認する。
- **入力評価文書を通じて追跡される成果物 (再評価しない)**: Service Design SD-001〜SD-007 ([../service-design/README.md](../service-design/README.md))・作成済み 7 個別 Screen Requirement ([../screen-requirements/README.md](../screen-requirements/README.md))・既存 Design System 4 成果物。

## 9. Method

1. Work Order 4 の各集約 Topic (T/C/X) と §16〜§19 を、設計責務と Observation の側面単位で確認する。
2. 各側面について、DS 側で対応する定義がない/部分的/責務の関係が明文化されていないことを直接確認できるか、または上流 Open Issue・provenance・placeholder・実査待ち・参照切れに依存して確定できないかを判別する。
3. 「改訂を検討し得る候補」節 (§13)・「未解決に依存し確定できない事項」節 (§14)・「分離対象外として保持する Observation」節 (§15) へ振り分ける。1 つの設計責務に候補側面と未解決側面が併存する場合は側面を分け、両者を §16 で相互リンクする。
4. 各レコードは、Source Topic (既存 T/C/X)・Source Assessment・Source Section・Related SD ID・Related SCR・Original Observation Classification・provenance・placeholder/実査待ち・参照切れ・Open Issue・Does Not Decide を保持する。
5. Separation Traceability Index (§12) で、T-01〜T-07・C-01〜C-10・X-01〜X-07・§16〜§19 の引き継ぎ先を追跡する。
6. Work Order 6 の判断 (改訂着手可否) に踏み込まず、未解決事項は依存関係として記録する。

分離は単なる文章の連結やコピーではなく、候補側面・未解決側面・分離対象外の関係が理解できる形にする。元 Observation を削除せず、Separation Traceability (§12) で保持する。入力評価文書と矛盾する可能性を確認した場合は本文書内で不一致として記録し、元文書を修正しない。

## 10. Evidence Rules

Alignment Plan §6 と入力文書 (Work Order 2〜4 の Evidence Rules) を継承する。

- 分離の証拠は、Work Order 4 が集約した Observation と、その元出典 (Work Order 2/3 の実在記述、Work Order 1 の証拠制約) に限定する。入力文書が記録していない対応・不足・矛盾を本分離で新たに作らない。
- 既存 Design System 4 成果物の記述は、入力評価文書が引用した範囲で追跡する。本分離が独自に成果物を再走査して新しい直接証拠を追加しない。
- ファイル名・Component 名の推測、一般慣行、実装仕様の推測、不在文書の内容、正本のない ADR の想定、Decision ID の存在のみを根拠とする再認定、Downstream Impact の Component 例、Component 存在のみを根拠とする利用要求、未着手 Component の必要性化、Open Issue / Does Not Decide を確定要件へ変換した内容は、候補の根拠として扱わない。
- provenance 未確認の記述・参照切れ文書の想定内容を、候補の適合根拠・実現手段として使用しない。

## 11. Separation Rules

### 11.1 3 節の定義

- **改訂を検討し得る候補 (§13)**: Repository 内の直接証拠だけで、(a) 上流の設計責務が改訂の具体内容を推測しなくても識別でき、(b) DS 側で対応する定義がない/部分的/責務の関係が明文化されていないことを直接確認でき、(c) 未定義の事業要求・業務仕様・画面仕様を補完せず検討対象の責務を記述でき、(d) Component/token/pattern/文書の具体的な追加・変更案を決定しなくても成立し、(e) provenance 未確認の記述を適合根拠に使用していない、側面。候補の表現は設計責務レベルに留め、具体的な修正案 (特定 Component の追加・特定 token 値への変更) を書かない。
- **未解決に依存し確定できない事項 (§14)**: 未定義の事業要求/業務仕様/画面仕様、Service Design または Screen Requirement の Open Issue、SCR-006〜SCR-012 等の対象外領域、provenance 未確認、ADR 正本不在、`brand-content.md`/`governance/naming-rules.md` の参照切れ、placeholder、実査待ち、follow-up の未完了/追跡先不明、外部 Repository/実装/URL の未検証、承認主体/解決主体/反映主体の未定義、のいずれかに依存する側面。解決内容・値・仕様・担当者・期限を推測しない。
- **分離対象外として保持する Observation (§15)**: 対応を直接確認でき別の未解決制約を伴わない Observation、Work Order 4 で矛盾/過剰が確認されていないという対象 snapshot 限定の Fact、Work Order 5 の処理対象でない評価対象外 Observation、元評価の境界や Does Not Decide を保持するための Observation。新しい Observation 分類や正式 Status ではなく、改訂候補でも未解決事項でもない元 Observation を失わないための置き場所。

### 11.2 判定規則 (厳守)

- `対応する定義を確認できない` だけを理由に、自動的に改訂候補へ分類しない。
- `一部のみ確認できる` だけを理由に、自動的に改訂候補へ分類しない。
- Component が存在しないことだけを理由に、新規 Component 候補としない。
- 未着手 Component が存在することだけを理由に、その Component を改訂候補としない。
- Screen Requirement の Downstream Impact に Component 例があることを採用根拠にしない。
- placeholder または実査待ちは、値や実態の確認前に改訂候補へ変換しない。
- provenance 未確認の Decision ID を、改訂候補の根拠に使用しない。
- 参照切れ文書の想定内容を、改訂候補の根拠に使用しない。
- 上流 Open Issue に依存する具体仕様を、DS 側の不足として断定しない。
- IA Object を Component・表示項目・データモデルと同一視しない。Content Category を Component・掲載枠と同一視しない。
- Navigation Types と Navigation component を自動対応させない。Navigation State Model・CTA State Model・Component state を同一視しない。Navigation と CTA を別の設計責務として扱う。
- `Error / Interrupted` を 1 つの複合状態名として扱う。SCR 間で異なる Navigation States を共通化しない。SCR-014 に `Error / Interrupted` を追加しない。

### 11.3 候補と未解決事項が併存する場合

- 改訂候補節には、未解決事項へ依存せず直接確認できる責務の側面 (対応の明文化余地) だけを記載する。
- 未解決事項節には、確定を妨げる上流・provenance・placeholder・実査待ち等を記載する。
- 両者を §16 Candidate–Unresolved Dependency Relationships で相互リンクする。
- 未解決事項があるため候補が実行可能かどうかは判断しない。`conditional candidate` 等の新しい正式分類を作らない。候補を `blocked` / `ready` 等の実行状態へ分類しない。

### 11.4 Observation 分類

元 Observation には Alignment Plan §8 の 10 分類だけを使用する: 対応を直接確認できる / 一部のみ確認できる / 対応する定義を確認できない / 過剰 / 矛盾 / placeholder / 実査待ち / provenance 未確認 / 参照切れ / 評価対象外。「改訂を検討し得る候補」「未解決に依存し確定できない事項」「分離対象外として保持する Observation」は Work Order 5 の整理上の節であり、11 番目以降の Observation 分類ではない。数値スコア・適合率・カバレッジ率・件数ランキング・pass/fail・severity は導入しない。

## 12. Separation Traceability Index

Work Order 4 の全 Topic と §16〜§19 が分離後にどこへ引き継がれたかを確認する索引。網羅性確認のための索引であり、数値カバレッジ・得点・適合率を算出しない。「候補」「未解決」「対象外」は §13/§14/§15 の該当レコード (説明用見出し) を指す。既存 T/C/X ラベルを正式 ID へ昇格させず、新しい候補 ID・未解決事項 ID・優先度 ID を作成しない。

| 入力 Topic / 節 | 関連する設計責務 | 改訂候補 (§13) | 未解決事項 (§14) | 対象外保持 (§15) | 元 Observation 分類 |
| --- | --- | --- | --- | --- | --- |
| T-01 | focus 可視化・アクセシビリティ基盤 | あり (規格・達成レベルの対応明文化余地) | あり (規格・達成レベルの確定主体・コントラスト自認) | 方針記述部分 (WCAG 2.2 AA 最低ラインの記述は対応を直接確認できる) | 一部のみ確認できる (SDP-007 は対応を直接確認できる併記) |
| T-02 | 状態の色表現 | あり (状態モデルとの対応明文化余地) | あり (状態業務定義・follow-up #4・Input error placeholder・naming-rules 参照切れ) | success/error token の存在は対応を直接確認できる部分 | 一部のみ確認できる, placeholder |
| T-03 | タイポグラフィスケール | あり (具体規格・文字数制限の対応明文化余地) | あり (具体仕様の確定主体・CTP-008 Does Not Decide) | スケール記述は対応を直接確認できる部分 | 対応を直接確認できる / 一部のみ確認できる |
| T-04 | accent/campaign 色による Fact/Promotion 分離基盤 | なし (対応を直接確認できる。判定規則により provenance 未確認を候補根拠にしない) | あり (TVL-0011/0012 provenance 未確認) | 対応を直接確認できる部分 (accent 点専用 token) | 対応を直接確認できる, provenance 未確認 |
| T-05 | 価格・評価表現 token | あり (表現責務と token の対応明文化余地) | あり (料金構造・Review 提供元の業務モデル・「円」weight 実査待ち) | — | 一部のみ確認できる, 実査待ち |
| T-06 | radius/shadow/motion placeholder | なし (placeholder は値確認前に候補化しない) | あり (placeholder token 計 10 の解決) | — | placeholder |
| T-07 | token 参照内部整合性・DS 独立性 | なし | なし | あり (対応を直接確認できる・別の未解決制約なし) | 対応を直接確認できる |
| C-01 | Button と CTA 明確性・主要行動 | あり (情報確認と選択の区別・主要行動と Button の対応明文化余地) | あり (主要 CTA は上流未定義・GOV-0002 provenance・follow-up #4) | CTA-002「主 CTA primary 1 つ」は対応を直接確認できる部分 | 対応を直接確認できる / 一部のみ確認できる, provenance 未確認 |
| C-02 | SearchForm/Input と検索・入力責務 | あり (入力の状態表現・回復責務と Input の対応明文化余地) | あり (入力項目・バリデーション・条件保持は上流 Open Issue・Input follow-up #2・GOV-0002) | 検索開始 CTA (Button.primary) は対応を直接確認できる部分 | 一部のみ確認できる, 実査待ち |
| C-03 | Card と Accommodation 表現 | あり (Accommodation 表現責務と Card の対応明文化余地) | あり (表示項目・順・比較基準は上流 Open Issue・Card 実 px/8 スロット実査待ち・radius.card/shadow placeholder) | — | 一部のみ確認できる, 実査待ち, placeholder |
| C-04 | PriceTag と価格・条件表現 | あり (条件提示責務と PriceTag の対応明文化余地) | あり (価格構造・表示位置は上流 Does Not Decide・「円」weight 実査待ち) | 条件併記構造は対応を直接確認できる部分 | 一部のみ確認できる |
| C-05 | ReviewStars と評価表現 | あり (評価表現責務と ReviewStars の対応明文化余地) | あり (Review 提供元・評価対象・信頼性は上流 Open Issue・星実寸実査待ち) | 数値併記は対応を直接確認できる部分 (X-04) | 一部のみ確認できる, 実査待ち |
| C-06 | Header/Breadcrumb/Footer と Navigation component | あり (NAV 分類と Navigation component の対応明文化余地) | あり (Global Nav 対象領域・History and Recovery 保持方式は上流 NAV/SCR Open Issue) | component の実在は対応を直接確認できる部分 | 一部のみ確認できる / 対応する定義を確認できない |
| C-07 | Modal/Overlay と可逆操作・回復 | あり (可逆/不可逆区別責務と DS 側規則の対応明文化余地) | あり (保存期間・Undo・エラー処理は上流 Does Not Decide・TVL-0007 provenance・Input follow-up #2) | Modal/Overlay の実在は対応を直接確認できる部分 | 一部のみ確認できる / 対応する定義を確認できない |
| C-08 | Recovery Action 用 component/規則の不在 | あり (Recovery Action 責務と DS 側の対応明文化余地) | あり (問い合わせ手段・処理フロー・サポート範囲は上流 Open Issue・follow-up #4) | — | 対応する定義を確認できない / 一部のみ確認できる |
| C-09 | 支援・FAQ・Policy 表現 component の不在 (未着手) | 限定的にあり (支援領域の表現責務と DS 対応の明文化余地。未着手 Component を候補としない) | あり (サポート範囲・FAQ 構成は上流 Open Issue・brand-content 参照切れ・未着手 component) | 未着手 (成果物不在) の事実保持 | 対応する定義を確認できない |
| C-10 | 専用表現語彙の不在 (IA Object) | あり (IA Object 表現責務と DS 表現語彙の対応明文化余地) | あり (IA Object 業務モデルは IA §11 Open Issue・SCR-005/006 境界・User は対象外領域) | User (認証・会員・履歴) は評価対象外として保持 | 対応する定義を確認できない |
| X-01 | Navigation と CTA の責務分離 | あり (責務分離を述べる DS 本文規則の対応明文化余地) | あり (GOV-0002 provenance) | component 単位の別扱いは対応を直接確認できる部分 | 一部のみ確認できる / 対応する定義を確認できない |
| X-02 | Fact/Decision/Promotion 分離 | なし (対応を直接確認できる。judge 規則により provenance/参照切れを候補根拠にしない) | あり (TVL provenance・brand-content 参照切れ・広告表示ルールは上流 Does Not Decide) | 対応を直接確認できる部分 (最も広く共有) | 対応を直接確認できる, provenance 未確認 |
| X-03 | 状態・不確実性モデルと DS 状態表現 | あり (状態モデルと DS 状態表現の対応明文化余地) | あり (状態の業務定義は上流 Open Issue・follow-up #4・motion placeholder・空結果/在庫切れ挙動) | success/error 表現は対応を直接確認できる部分 | 対応する定義を確認できない / 一部のみ確認できる, placeholder |
| X-04 | Accessibility 非依存原則 | あり (適用規格・達成レベルの対応明文化余地) | あり (規格・達成レベル確定主体・画像 fallback 実査待ち) | 非視覚依存の方針記述は対応を直接確認できる部分 | 対応を直接確認できる / 一部のみ確認できる |
| X-05 | 未確定事項の保持 (placeholder 伝播) | なし (DS 運用は対応を直接確認できる) | あり (placeholder/実査待ちの解決主体・TVL-0008/0010 provenance) | 保持運用は対応を直接確認できる部分 (UXDR-TRAVEL-001) | 対応を直接確認できる |
| X-06 | IA Object と表現語彙の非 1 対 1 | あり (IA Object/Content Category と DS 表現の対応整理の明文化余地) | あり (IA Object 業務仕様は IA §11 Open Issue) | 非 1 対 1 原則の保持 (UXDR-TRAVEL-002) は対応を直接確認できる部分 | 一部のみ確認できる / 対応する定義を確認できない |
| X-07 | 文言表現の正本不在 | なし (参照切れ文書の想定内容を候補根拠にしない) | あり (brand-content.md/naming-rules.md/ADR 正本不在) | — | 参照切れ |
| §16 Source-specific Variations | Topic 内のスコープ固有差異 | 各候補レコードの Source-specific Variation 欄・§19 に保持 | 各未解決事項レコードに保持 | — | 元 Topic の分類を継承 |
| §17 provenance/placeholder/実査待ち/参照切れ | 証拠制約 | — | あり (§14・§17 Boundary に集約) | — | provenance 未確認/placeholder/実査待ち/参照切れ |
| §18 Conflict and Over-coverage | 矛盾・過剰の不在 | なし | なし | あり (対象 snapshot 限定の Fact として §15・§18 Boundary に保持) | 矛盾/過剰は入力評価になし |
| §19 Unresolved Dependencies | 依存関係 | — | あり (§14 の未解決事項レコードの主基盤) | — | 元 Topic の分類を継承 |

## 13. 改訂を検討し得る候補

本節への記載は、Design System を改定すべきという Decision・改定要否の決定・新規 Component や token の必要性確定・改訂内容の確定・改訂着手可能・優先順位の確定・承認済みのいずれも意味しない。各レコードの `Candidate Aspect` は具体的な修正案ではなく、改訂を検討し得る設計責務の範囲である。見出しは説明用であり、恒久 ID ではない。

### 候補: NAV 分類と DS Navigation component の対応の明文化

- **Source Topic**: C-06 (関連 X-01)。
- **Assessment Dimension**: Component / pattern (Navigation 整理軸)。
- **Design Responsibility**: NAV-001〜006 (Navigation Types) を UI として表現する責務と、DS 側 Navigation component の対応関係。
- **Source Assessment**: WO2 §8.3、WO3 §12〜§18 の Navigation 節、WO4 C-06。
- **Source Section**: WO4 C-06 / WO2 §8.3 / WO3 各 SCR §8。
- **Related Service Design ID**: NVP-001・NAV-001〜006。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: 一部のみ確認できる / 対応する定義を確認できない (併記)。
- **DS-side Observed Condition**: Header・Breadcrumb・Footer は実在するが、DS 側に NAV-001〜006 分類との対応記述がない。
- **Direct Evidence**: components.md Header/Breadcrumb/Footer、WO4 C-06「DS 側に NAV-ID との対応記述はない」。
- **Candidate Aspect**: 上流で定義された Navigation Types の責務と、DS 側 Navigation component の対応関係を明文化する余地。特定 component の追加や特定 NAV への割当は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: NAV-001〜006 は上流 SD-003 に実在し、DS 側に対応記述がないことは components.md で直接確認できる。対応の明文化余地の指摘に、業務仕様や具体 UI の補完を要しない。
- **Related Unresolved Dependency**: Global Navigation 対象領域・History and Recovery 保持方式の上流未定義 (§14「Navigation 分類の上流未定義」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation のナビゲーション実装 (Repository 管理対象外)。
- **Open Issue**: NAV 分類対応の記述をどこが定義するか未定。
- **Does Not Decide**: Navigation component と NAV-ID の対応確定・特定 component の追加は本分離で決めない。Navigation Types と component を自動対応させない。

### 候補: Navigation と CTA の責務分離を述べる DS 本文規則の明文化

- **Source Topic**: X-01 (関連 C-06・C-01)。
- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: Navigation 要素と CTA 要素を別 Pattern・別評価軸で扱う責務 (UXDR-TRAVEL-003) を DS 側に明文化する関係。
- **Source Assessment**: WO2 §8.6、WO4 X-01。
- **Source Section**: WO4 X-01 / WO2 §8.6。
- **Related Service Design ID**: UXDR-TRAVEL-003・NAV-001〜006・CTA-002。
- **Related SCR**: SCR-001〜SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: 一部のみ確認できる / 対応する定義を確認できない (併記)。
- **DS-side Observed Condition**: components.md は Button (CTA) と Header/Breadcrumb (Navigation) を別 component として定義するが、責務分離を述べる本文規則が確認できない。
- **Direct Evidence**: WO4 X-01「責務分離を述べる DS 側の本文規則は不在」、cta-principles.md §8「具体的な UI 分類は Design System 側で定義する」に対応する DS 側規則は未記述。
- **Candidate Aspect**: UXDR-TRAVEL-003 が求める Navigation/CTA の責務分離を DS 側で明文化する余地。component の分割状態は既にあるため、規則記述の対応関係に限る。
- **Why This Aspect Can Be Stated Without Assumption**: UXDR-TRAVEL-003 は Accepted な上流 Decision として実在し、DS 側に責務分離の本文規則がないことは直接確認できる。
- **Related Unresolved Dependency**: Button variant 語彙の GOV-0002 provenance 未確認 (§14「Decision ID の provenance」)。
- **Provenance**: GOV-0002 は provenance 未確認 (候補の適合根拠には使用しない)。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation の Navigation/CTA 実装 (Repository 管理対象外)。
- **Open Issue**: 責務分離規則の記述主体。
- **Does Not Decide**: 責務分離規則の内容・追加は本分離で決めない。Navigation と CTA を混同しない。

### 候補: 上流状態モデルと DS 状態表現の対応の明文化

- **Source Topic**: X-03 (関連 T-02・C-08)。
- **Assessment Dimension**: Cross-cutting (State and Feedback 整理軸)。
- **Design Responsibility**: Navigation State Model・CTA State Model・Status and Uncertainty Model を UI として表現する責務と DS 状態表現の対応関係。
- **Source Assessment**: WO2 §8.3/§8.4/§8.5、WO3 各 SCR §10、WO4 X-03/T-02。
- **Source Section**: WO4 X-03・T-02 / WO2 §8.3〜§8.5 / WO3 各 SCR §10。
- **Related Service Design ID**: Navigation State Model・CTA State Model・Status and Uncertainty Model・CTP-006・CTA-007・SDP-005。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: 対応する定義を確認できない / 一部のみ確認できる, placeholder (併記)。
- **DS-side Observed Condition**: DS 側は success/error 中心の状態色・状態固定リストを持つが、状態モデルの各状態 (Pending Confirmation・Navigation State 各状態等) との対応定義が確認できない。
- **Direct Evidence**: semantic `color.state.success`/`error`・components.md 状態固定リスト、WO4 X-03「Pending Confirmation・Navigation State 各状態に対応する DS 定義は確認できない」。
- **Candidate Aspect**: 上流の各状態モデルと DS 状態表現の対応関係を明文化する余地。状態の具体一覧の確定や特定 token/component の追加は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: 状態モデルは上流 SD-003/SD-004/SD-005 に実在し、DS 側に対応定義がない/一部のみであることは直接確認できる。Navigation State Model・CTA State Model・Component state を同一視しない範囲で記述する。
- **Related Unresolved Dependency**: 状態の業務定義 (上流 Open Issue)・ボタン状態 follow-up #4・motion placeholder・空結果/在庫切れ挙動の未定義 (§14「状態モデルの業務定義未定義」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: ボタン状態 follow-up #4・motion placeholder は未解決事項側 (§14)。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation の状態遷移表示 (Repository 管理対象外)。
- **Open Issue**: 状態モデル対応の記述主体。
- **Does Not Decide**: 状態の具体一覧・業務定義・UI 表現・token 値は本分離で決めない。SCR 間で異なる Navigation States を共通化せず、SCR-014 に `Error / Interrupted` を追加しない。

### 候補: Recovery Action 責務と DS 側の対応の明文化

- **Source Topic**: C-08 (関連 X-03)。
- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 中断・エラーからの回復行動 (Recovery Action, CTA-TYPE-004) を UI として表現する責務と DS 側の対応関係。
- **Source Assessment**: WO3 §17 (SCR-013)、WO2 §8.5 (CTA-007)、WO4 C-08。
- **Source Section**: WO4 C-08 / WO3 §17 / WO2 §8.5。
- **Related Service Design ID**: CTA-TYPE-004・CTA-007。
- **Related SCR**: SCR-013。
- **Original Observation Classification**: 対応する定義を確認できない / 一部のみ確認できる (併記)。
- **DS-side Observed Condition**: error/loading 状態は状態固定リストにあるが、Recovery Action 用の component/規則が確認できない。
- **Direct Evidence**: WO4 C-08「Recovery Action (CTA-TYPE-004) に対応する DS 側の component/規則は確認できない」。
- **Candidate Aspect**: 上流で定義された Recovery Action の責務と DS 側の対応関係を明文化する余地。特定 component の追加は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: CTA-TYPE-004 は上流 SD-005 に実在し、DS 側に Recovery Action 用の規則がないことは直接確認できる。
- **Related Unresolved Dependency**: 問い合わせ手段・処理フロー・サポート対象範囲の上流未定義・ボタン状態 follow-up #4 (§14「可逆/回復の上流未定義」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: ボタン状態 follow-up #4 は未解決事項側。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation の回復動線 (Repository 管理対象外)。
- **Open Issue**: Recovery Action 責務の記述主体。
- **Does Not Decide**: Recovery Action の component/規則・特定 component の追加は本分離で決めない。未着手 component を必要 component へ変換しない。

### 候補: IA Object・Content Category の表現責務と DS 表現語彙の対応の明文化

- **Source Topic**: C-10 (関連 X-06)。
- **Assessment Dimension**: Component / pattern・Cross-cutting (IA Object 整理軸)。
- **Design Responsibility**: 宿泊領域の IA Object (Destination/Room/Stay Plan/Availability/Policy/Booking/Content 等) と Content Category を UI として表現する責務と DS 表現語彙の対応関係。
- **Source Assessment**: WO2 §8.2/§8.4、WO3 各 SCR §5/§7、WO4 C-10/X-06。
- **Source Section**: WO4 C-10・X-06 / WO2 §8.2・§8.4 / WO3 各 SCR §5・§7。
- **Related Service Design ID**: IA-OBJ-001・IA-OBJ-004・IA-OBJ-005・IA-OBJ-006・IA-OBJ-008・IA-OBJ-010・IA-OBJ-012・Content Categories (6)。
- **Related SCR**: SCR-001・SCR-002・SCR-004・SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: 対応する定義を確認できない (一部の IA Object は一部のみ確認できる)。
- **DS-side Observed Condition**: SearchForm/Card/PriceTag/ReviewStars が対応する IA Object は一部のみで、他 IA Object・Content Category の専用表現語彙が確認できない。
- **Direct Evidence**: WO4 C-10「専用表現語彙は対応する定義を確認できない」、IA §10「Design System は各情報オブジェクトや状態を UI として表現する設計語彙を提供する」。
- **Candidate Aspect**: 上流 IA Object・Content Category の表現責務と DS 表現語彙の対応関係を整理・明文化する余地。IA Object を Component/表示項目/データモデルと同一視せず、Content Category を Component/掲載枠と同一視しない範囲に留める。
- **Why This Aspect Can Be Stated Without Assumption**: IA-OBJ 群・Content Categories は上流 SD-002/SD-004 に実在し、DS 側に専用表現語彙がないことは直接確認できる。責務の対応整理の指摘に業務仕様の補完を要しない。
- **Related Unresolved Dependency**: IA Object の内容・関係・業務仕様 (IA §11 Open Issue)・SCR-005/SCR-006 境界・User (認証・会員・履歴) の対象外性 (§14「IA Object の業務モデル未定義」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: Content 文言は brand-content.md 参照切れ (§14「文言・命名の正本不在」)。
- **Downstream Impact**: Implementation の各領域表現 (Repository 管理対象外)。
- **Open Issue**: IA Object・Content Category 対応整理の記述主体。
- **Does Not Decide**: 専用 component の要否・IA Object と Component の同一視は本分離で決めない。

### 候補: 可逆/不可逆区別責務と DS 側規則の対応の明文化

- **Source Topic**: C-07。
- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 可逆操作・回復可能性 (SDP-006)・不可逆前の可逆 (CTA-006) を UI として区別する責務と DS 側規則の対応関係。
- **Source Assessment**: WO2 §8.1 (SDP-006)・§8.5 (CTA-006)、WO4 C-07。
- **Source Section**: WO4 C-07 / WO2 §8.1・§8.5。
- **Related Service Design ID**: SDP-006・CTA-006。
- **Related SCR**: — (WO2 横断責務として記録。SCR-003 の Error 回復は C-02/入力側)。
- **Original Observation Classification**: 一部のみ確認できる / 対応する定義を確認できない (併記)。
- **DS-side Observed Condition**: Modal/Overlay は実在するが、可逆/不可逆を区別する DS 側の明示規則が確認できない。
- **Direct Evidence**: components.md Modal/Overlay、WO4 C-07「可逆/不可逆を区別する DS 側の明示規則は確認できない」。
- **Candidate Aspect**: CTA-006 が求める可逆/不可逆の区別責務と DS 側規則の対応関係を明文化する余地。保存期間・Undo の仕様確定は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: SDP-006・CTA-006 は上流に実在し、DS 側に区別規則がないことは直接確認できる。
- **Related Unresolved Dependency**: 保存期間・Undo・エラー処理仕様は上流 Does Not Decide・TVL-0007 provenance・Input follow-up #2 (§14「可逆/回復の上流未定義」)。
- **Provenance**: drawer 統一 TVL-0007 は provenance 未確認 (候補根拠に使用しない)。
- **Placeholder / Inspection Pending**: Input 状態 follow-up #2 は未解決事項側。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation の回復フロー (Repository 管理対象外)。
- **Open Issue**: 可逆/不可逆区別規則の記述主体。
- **Does Not Decide**: 可逆/不可逆規則・エラー処理仕様は本分離で決めない。

### 候補: アクセシビリティ適用規格・達成レベルと focus/非依存表現の対応の明文化

- **Source Topic**: T-01・X-04。
- **Assessment Dimension**: Foundation / token・Cross-cutting (Accessibility 整理軸)。
- **Design Responsibility**: 操作要素の focus 可視化・色/アイコン/位置/画像だけに依存させない責務 (SDP-007/NVP-008/CTA-009/CTP-008) と、適用規格・達成レベルの対応関係。
- **Source Assessment**: WO2 §8.1/§8.3/§8.4/§8.5、WO3 各 SCR §11、WO4 T-01/X-04。
- **Source Section**: WO4 T-01・X-04 / WO2 §8.1・§8.3〜§8.5 / WO3 各 SCR §11。
- **Related Service Design ID**: SDP-007・NVP-008・CTA-009・CTP-008。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-013・SCR-014。
- **Original Observation Classification**: 対応を直接確認できる (方針記述) / 一部のみ確認できる (具体規格未定義) の併記。
- **DS-side Observed Condition**: `color.focus.ring`・「色/アイコン/位置だけに意味を依存させない」・「WCAG 2.2 AA を最低ライン」の方針記述はあるが、適用規格・達成レベルが未定義。
- **Direct Evidence**: design.md §2「WCAG 2.2 AA を最低ライン」・semantic `color.focus.ring`・components.md 非視覚依存記述、WO4 T-01/X-04「適用規格・達成レベルは未定義」。
- **Candidate Aspect**: アクセシビリティの適用規格・達成レベルと DS の focus/非依存表現の対応関係を明文化する余地。具体的な達成基準値の確定は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: SDP-007/NVP-008/CTA-009/CTP-008 は上流に実在し、方針記述はあるが適用規格・達成レベルが未定義であることは直接確認できる。
- **Related Unresolved Dependency**: 適用規格・達成レベルの確定主体・画像 fallback 実査待ち・コントラスト未達可能性の DS 自認 (§14「アクセシビリティ規格の未定義」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 画像欠落 fallback (SCR-014) は未解決事項側。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation のアクセシビリティ実装 (Repository 管理対象外)。
- **Open Issue**: 適用規格・達成レベルの記述主体。
- **Does Not Decide**: 適用規格・達成レベル・実装方式・画像仕様は本分離で決めない。

### 候補: 情報確認と選択の区別・CTA 主要行動責務と DS Button 定義の対応の明文化

- **Source Topic**: C-01。
- **Assessment Dimension**: Component / pattern (CTA 整理軸)。
- **Design Responsibility**: 行動の明確性・情報確認と選択の区別 (CTA-001/CTA-004)・主要行動の優先関係を UI として表現する責務と DS Button 定義の対応関係。
- **Source Assessment**: WO2 §8.5、WO3 §15/§16、WO4 C-01。
- **Source Section**: WO4 C-01 / WO2 §8.5 / WO3 §15 (SCR-004)・§16 (SCR-005)。
- **Related Service Design ID**: CTA-001・CTA-004 (CTA-002 は対応を直接確認できる部分)。
- **Related SCR**: SCR-004・SCR-005。
- **Original Observation Classification**: 一部のみ確認できる (CTA-002 は対応を直接確認できる併記), provenance 未確認。
- **DS-side Observed Condition**: Button variant で主/補助の区別は表現し得るが、情報確認と選択の区別・比較/選択の優先関係の責務対応が一部のみ。
- **Direct Evidence**: components.md Button variant primary/secondary/ghost/text、WO4 C-01「CTA-004 を Button variant で一部のみ表現」。
- **Candidate Aspect**: 情報確認と選択の区別・主要行動の優先関係の責務と DS Button 定義の対応関係を明文化する余地。特定 variant の追加や主要 CTA の確定は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: CTA-001/CTA-004 は上流に実在し、DS 側の対応が一部のみであることは直接確認できる。
- **Related Unresolved Dependency**: 各 SCR で主要行動が未定義 (上流 Open Issue)・GOV-0002 provenance・ボタン状態 follow-up #4 (§14「Decision ID の provenance」「状態モデルの業務定義未定義」)。
- **Provenance**: Button variant GOV-0002 provenance 未確認 (候補根拠に使用しない)。
- **Placeholder / Inspection Pending**: ボタン状態 follow-up #4 は未解決事項側。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: 各 SCR §15 Downstream Impact の Button 例を採用決定と解釈しない (Repository 管理対象外)。
- **Open Issue**: 主要 CTA の確定は上流依存。
- **Does Not Decide**: 主要 CTA の確定・variant の追加改廃は本分離で決めない。

### 候補: 入力の状態表現・回復責務と DS Input 定義の対応の明文化

- **Source Topic**: C-02。
- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 検索条件の入力・状態表現・回復 (IA-OBJ-002/SDP-006/CTP-007) を UI として表現する責務と DS Input/SearchForm 定義の対応関係。
- **Source Assessment**: WO2 §8.2/§8.1、WO3 §12/§14、WO4 C-02。
- **Source Section**: WO4 C-02 / WO2 §8.2・§8.1 / WO3 §12 (SCR-001)・§14 (SCR-003)。
- **Related Service Design ID**: IA-OBJ-002・SDP-006・CTP-007・CTA-001/005。
- **Related SCR**: SCR-001・SCR-003。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち (検索開始 CTA は対応を直接確認できる併記)。
- **DS-side Observed Condition**: SearchForm/Input は存在し検索開始 CTA は対応を直接確認できるが、入力の状態表現・回復の責務対応が一部のみ (Input 状態一式は実査待ち)。
- **Direct Evidence**: components.md SearchForm「Input 群 + 主 CTA」・Input error text 併記、WO4 C-02「Input 状態一式は follow-up #2 実査待ち」。
- **Candidate Aspect**: 入力の状態表現・回復の責務と DS Input 定義の対応関係を明文化する余地。入力項目・バリデーションの確定や特定 Input 状態の追加は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: IA-OBJ-002/SDP-006/CTP-007 は上流に実在し、DS 側の対応が一部のみであることは直接確認できる。
- **Related Unresolved Dependency**: 入力項目・必須条件・バリデーション・条件保持方式は上流 Open Issue・Input follow-up #2 実査待ち・GOV-0002 provenance (§14「入力・検索仕様の上流未定義」)。
- **Provenance**: Button variant GOV-0002 provenance 未確認 (候補根拠に使用しない)。
- **Placeholder / Inspection Pending**: Input 状態一式 follow-up #2 は未解決事項側。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation の検索/入力実装 (Repository 管理対象外)。
- **Open Issue**: 入力項目・バリデーションは上流依存。
- **Does Not Decide**: 入力項目・必須条件・バリデーション・履歴保持の確定は本分離で決めない。

### 候補: 表示責務 (候補/価格/評価) と DS component (Card/PriceTag/ReviewStars) の対応の明文化

- **Source Topic**: C-03・C-04・C-05 (関連 T-05)。
- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 宿泊施設候補・価格と条件・評価を UI として表現する責務 (IA-OBJ-003/007/009・CTA-005・SDP-003) と DS component の対応関係。
- **Source Assessment**: WO2 §8.2/§8.1/§8.5、WO3 §15/§16、WO4 C-03/C-04/C-05/T-05。
- **Source Section**: WO4 C-03・C-04・C-05・T-05 / WO2 §8.2・§8.1・§8.5 / WO3 §15 (SCR-004)・§16 (SCR-005)。
- **Related Service Design ID**: IA-OBJ-003・IA-OBJ-007・IA-OBJ-009・CTA-005・SDP-003・CTP-003。
- **Related SCR**: SCR-002・SCR-004・SCR-005・SCR-014。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち, placeholder (併記)。
- **DS-side Observed Condition**: Card (8 スロット)・PriceTag (条件併記構造)・ReviewStars (数値併記) は存在するが、表示項目・表示順・比較基準等の責務対応が一部のみ (実 px・8 スロット・星実寸・「円」weight は実査待ち、radius.card/shadow は placeholder)。
- **Direct Evidence**: components.md Card/PriceTag/ReviewStars、WO4 C-03/C-04/C-05「一部のみ確認できる・実査待ち」。
- **Candidate Aspect**: 候補提示・価格条件提示・評価表現の責務と DS component の対応関係を明文化する余地。表示項目・表示順・実測値の確定や特定 slot/token の変更は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: IA-OBJ-003/007/009・CTA-005・SDP-003 は上流に実在し、DS 側の対応が一部のみであることは直接確認できる。Downstream Impact の Card/PriceTag/ReviewStars 例を採用根拠にしない。
- **Related Unresolved Dependency**: 表示項目・表示順・比較成立基準・料金構造・Review 提供元は上流 Open Issue、Card 実 px/8 スロット・星実寸・「円」weight 実査待ち、radius.card/shadow placeholder (§14「表示仕様の上流未定義」「placeholder/実査待ちの未取得」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: radius.card/shadow placeholder・実 px/8 スロット/星実寸/「円」weight 実査待ちは未解決事項側。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation の一覧/詳細/価格/評価表示 (Repository 管理対象外)。
- **Open Issue**: 表示仕様は上流依存。
- **Does Not Decide**: 一覧/詳細 UI・表示項目・token 値・Card の採用決定は本分離で決めない。IA Object を Component と同一視しない。

### 候補: タイポグラフィ具体規格と CTP-008 責務の対応の明文化

- **Source Topic**: T-03。
- **Assessment Dimension**: Foundation / token。
- **Design Responsibility**: 可読性・スキャン容易性 (CTP-008) を支えるタイポグラフィスケールと具体規格の対応関係。
- **Source Assessment**: WO2 §8.4、WO4 T-03。
- **Source Section**: WO4 T-03 / WO2 §8.4。
- **Related Service Design ID**: CTP-008。
- **Related SCR**: — (WO2 横断責務)。
- **Original Observation Classification**: 対応を直接確認できる / 一部のみ確認できる (併記)。
- **DS-side Observed Condition**: design.md §3 タイポグラフィスケール (rem 基準)・primitive `typography.size.*` は存在するが、文字数制限・具体規格が未定義。
- **Direct Evidence**: design.md §3・primitive `typography.size.*`、WO4 T-03「文字数制限・具体規格は未定義」。
- **Candidate Aspect**: タイポグラフィの具体規格・文字数制限と CTP-008 責務の対応関係を明文化する余地。具体値の確定は含まない。
- **Why This Aspect Can Be Stated Without Assumption**: CTP-008 は上流に実在し、DS 側にスケール記述はあるが具体規格が未定義であることは直接確認できる。
- **Related Unresolved Dependency**: タイポグラフィ具体仕様の確定主体・CTP-008 Does Not Decide (§14「表示仕様の上流未定義」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Downstream Impact**: Implementation のタイポグラフィ適用 (Repository 管理対象外)。
- **Open Issue**: タイポグラフィ具体仕様は上流 Does Not Decide 依存。
- **Does Not Decide**: タイポグラフィ仕様・token 値は本分離で決めない。

### 候補: 支援領域の表現責務と DS 対応の明文化 (限定的)

- **Source Topic**: C-09。
- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 支援 (FAQ/問い合わせ/Support)・Policy 本文 (CTP-003/006/010) を UI として表現する責務と DS 対応の関係。
- **Source Assessment**: WO3 §17 (SCR-013)、WO4 C-09。
- **Source Section**: WO4 C-09 / WO3 §17。
- **Related Service Design ID**: CTP-003・CTP-006・CTP-010 (Editorial and Support / Conditions and Policies)。
- **Related SCR**: SCR-013。
- **Original Observation Classification**: 対応する定義を確認できない (Accordion 等は未着手と明記)。
- **DS-side Observed Condition**: 支援領域の表現語彙に対応する DS component が確認できない (Accordion 等は未着手)。
- **Direct Evidence**: WO4 C-09「支援領域の表現語彙に対応する DS component は確認できない」、components.md 未着手一覧に Accordion。
- **Candidate Aspect**: 支援領域の表現責務と DS 対応の明文化余地。未着手 component (Accordion 等) を必要 component・改訂候補へ変換せず、サポート対象範囲が上流で定義された後に責務対応を検討できるという範囲に限定する。
- **Why This Aspect Can Be Stated Without Assumption**: CTP-003/006/010 の支援・Policy 表現責務は上流に実在し、DS 側に対応 component がないことは直接確認できる。ただし本候補は上流 Open Issue (サポート範囲) に強く依存するため、§16 で未解決事項と相互リンクする。
- **Related Unresolved Dependency**: サポート対象範囲・FAQ 構成・問い合わせ手段は上流 Open Issue・brand-content.md 参照切れ・未着手 component (§14「可逆/回復の上流未定義」「文言・命名の正本不在」)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし (未着手 = 成果物不在)。
- **Broken Reference**: 文言正本 brand-content.md 不在は未解決事項側。
- **Downstream Impact**: Implementation の支援 UI (Repository 管理対象外)。
- **Open Issue**: サポート対象範囲・FAQ 構成は上流依存。
- **Does Not Decide**: Accordion/フォーム/チャット/モーダル等の採用・追加は本分離で決めない。未着手 component を改訂候補へ変換しない。

## 14. 未解決に依存し確定できない事項

各レコードは、未定義の事業要求/業務仕様/画面仕様・上流 Open Issue・provenance 未確認・参照切れ・placeholder・実査待ち・follow-up・外部未検証・承認/解決/反映主体の未定義に依存する側面を記録する。解決内容・値・仕様・担当者・期限を推測しない。見出しは説明用であり、恒久 ID ではない。

### 未解決: 上流状態モデルの業務定義

- **Source Topic**: X-03・T-02・C-08。
- **Assessment Dimension**: Cross-cutting・Foundation / token。
- **Design Responsibility**: Navigation State Model・CTA State Model・Status and Uncertainty Model の各状態の業務定義。
- **Source Assessment**: WO2 §8.3〜§8.5、WO3 各 SCR §10、WO4 X-03/T-02/C-08/§19。
- **Source Section**: WO4 §19「状態モデルの対応整理」/ X-03・T-02。
- **Related Service Design ID**: Navigation State Model・CTA State Model・Status and Uncertainty Model・CTP-006・CTA-007。
- **Related SCR**: SCR-001〜SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: 対応する定義を確認できない / 一部のみ確認できる, placeholder。
- **Unresolved Fact**: 状態の業務定義 (Pending Confirmation の意味・空結果/在庫切れ挙動・予約状態) が上流で確定していない。DS 側は success/error 中心。
- **Missing Source or Dependency**: 上流の状態業務定義 (Screen Requirement / Service Design の Open Issue)・ボタン状態 follow-up #4・motion placeholder。
- **What Cannot Be Decided**: 状態の具体一覧・状態表示 Component・token 値。候補側の「対応明文化余地」を実行に移せるかは判断しない。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: ボタン状態 follow-up #4・motion placeholder。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 「上流状態モデルと DS 状態表現の対応の明文化」(§13・§16)。
- **Downstream Impact**: Implementation の状態遷移 (Repository 管理対象外)。
- **Open Issue**: 状態業務定義の解決主体。
- **Does Not Decide**: 状態の業務定義・UI 表現を推測しない。SCR 間で状態を正規化せず、SCR-014 に `Error / Interrupted` を追加しない。

### 未解決: Navigation 分類・Global Nav・History and Recovery の上流未定義

- **Source Topic**: C-06・X-01。
- **Assessment Dimension**: Component / pattern・Cross-cutting。
- **Design Responsibility**: Global Navigation 対象領域・History and Recovery (NAV-005) の保持方式。
- **Source Assessment**: WO2 §8.3、WO3 §12〜§18、WO4 C-06/§19。
- **Source Section**: WO4 §19「Navigation 分類の対応整理」/ C-06。
- **Related Service Design ID**: NAV-001〜006 (特に NAV-005 History and Recovery)。
- **Related SCR**: SCR-001・SCR-003・SCR-004・SCR-005・SCR-013。
- **Original Observation Classification**: 一部のみ確認できる / 対応する定義を確認できない。
- **Unresolved Fact**: Global Navigation 対象領域・History and Recovery 保持方式が上流 NAV/SCR Open Issue として未確定。
- **Missing Source or Dependency**: 上流 navigation.md §10 Open Issue・各 SCR §16 Open Issue。
- **What Cannot Be Decided**: NAV 分類対応の実現手段・保持方式。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 「NAV 分類と DS Navigation component の対応の明文化」(§13・§16)。
- **Downstream Impact**: Implementation のナビゲーション (Repository 管理対象外)。
- **Open Issue**: Global Nav 対象領域・History and Recovery の解決主体。
- **Does Not Decide**: Navigation Types と component を自動対応させない。保持方式を推測しない。

### 未解決: IA Object の業務モデル

- **Source Topic**: C-10・X-06。
- **Assessment Dimension**: Component / pattern・Cross-cutting。
- **Design Responsibility**: IA Object (Destination/Room/Stay Plan/Availability/Policy/Booking/Content) の内容・関係・業務仕様。
- **Source Assessment**: WO2 §8.2、WO3 §13〜§18、WO4 C-10/X-06/§19。
- **Source Section**: WO4 §19「IA Object の業務モデル」/ C-10・X-06。
- **Related Service Design ID**: IA-OBJ-001・IA-OBJ-004〜008・IA-OBJ-010・IA-OBJ-012。
- **Related SCR**: SCR-002・SCR-004・SCR-005。
- **Original Observation Classification**: 対応する定義を確認できない。
- **Unresolved Fact**: IA Object の内容・関係・業務仕様が IA §11 Open Issue として未確定。SCR-005/SCR-006 境界も未定義。
- **Missing Source or Dependency**: 上流 information-architecture.md §11 Open Issue・SCR-006〜012 (対象外)。
- **What Cannot Be Decided**: 専用表現語彙の要否・業務モデル。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: Content 文言は brand-content.md 参照切れ (別レコード)。
- **Related Candidate Aspect**: 「IA Object・Content Category の表現責務と DS 表現語彙の対応の明文化」(§13・§16)。
- **Downstream Impact**: Implementation の各領域表現 (Repository 管理対象外)。
- **Open Issue**: IA Object 業務モデルの解決主体。
- **Does Not Decide**: IA Object を Component/表示項目/データモデルと同一視しない。業務モデルを推測しない。

### 未解決: 入力・検索仕様の上流未定義

- **Source Topic**: C-02。
- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 検索条件の入力項目・必須条件・バリデーション・条件保持方式。
- **Source Assessment**: WO3 §14 (SCR-003)、WO4 C-02/§19。
- **Source Section**: WO4 §19「入力・検索仕様」/ C-02。
- **Related Service Design ID**: IA-OBJ-002。
- **Related SCR**: SCR-003。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち。
- **Unresolved Fact**: 入力項目・必須条件・バリデーション・条件保持方式が上流 Open Issue として未確定。
- **Missing Source or Dependency**: SCR-003 §16 Open Issue・Input 状態 follow-up #2。
- **What Cannot Be Decided**: Input の具体対応・状態一式。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: Button variant GOV-0002 provenance 未確認 (別レコード)。
- **Placeholder / Inspection Pending**: Input 状態一式 follow-up #2 実査待ち。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 「入力の状態表現・回復責務と DS Input 定義の対応の明文化」(§13・§16)。
- **Downstream Impact**: Implementation の検索/入力 (Repository 管理対象外)。
- **Open Issue**: 入力仕様の解決主体。
- **Does Not Decide**: 入力項目・バリデーションを推測しない。

### 未解決: 表示仕様 (表示項目/順/比較基準/料金構造/Review 提供元) の上流未定義

- **Source Topic**: C-03・C-04・C-05・T-05・T-03。
- **Assessment Dimension**: Component / pattern・Foundation / token。
- **Design Responsibility**: 候補一覧・詳細の表示項目・表示順・比較成立基準、料金構造・表示単位、Review 提供元・評価対象、タイポグラフィ具体仕様。
- **Source Assessment**: WO2 §8.2/§8.4、WO3 §15/§16、WO4 C-03/C-04/C-05/T-05/T-03/§19。
- **Source Section**: WO4 §19「表示仕様」/ C-03・C-04・C-05・T-05・T-03。
- **Related Service Design ID**: IA-OBJ-003・IA-OBJ-007・IA-OBJ-009・CTA-005・CTP-008。
- **Related SCR**: SCR-004・SCR-005。
- **Original Observation Classification**: 一部のみ確認できる, 実査待ち。
- **Unresolved Fact**: 表示項目・表示順・比較成立基準・料金構造・Review 提供元・タイポグラフィ具体仕様が上流 Open Issue / Does Not Decide として未確定。
- **Missing Source or Dependency**: SCR-004/SCR-005 §16 Open Issue・IA §11・CTP-008 Does Not Decide。
- **What Cannot Be Decided**: 表示 UI・表示項目・具体規格。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: Card 実 px・8 スロット・星実寸・「円」weight 実査待ち。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 「表示責務と DS component の対応の明文化」「タイポグラフィ具体規格と CTP-008 責務の対応の明文化」(§13・§16)。
- **Downstream Impact**: Implementation の表示 (Repository 管理対象外)。
- **Open Issue**: 表示仕様の解決主体。
- **Does Not Decide**: 表示項目・表示順・情報密度を推測しない。

### 未解決: 可逆/不可逆・回復フローの上流未定義

- **Source Topic**: C-07・C-08。
- **Assessment Dimension**: Component / pattern。
- **Design Responsibility**: 保存期間・Undo・エラー処理、問い合わせ手段・処理フロー。
- **Source Assessment**: WO2 §8.1/§8.5、WO3 §14/§17、WO4 C-07/C-08/§19。
- **Source Section**: WO4 §19「可逆/不可逆・回復」/ C-07・C-08。
- **Related Service Design ID**: SDP-006・CTA-006・CTA-TYPE-004・CTA-007。
- **Related SCR**: SCR-013 (Recovery)・SCR-003 (Error 回復)。
- **Original Observation Classification**: 一部のみ確認できる / 対応する定義を確認できない。
- **Unresolved Fact**: 保存期間・Undo・エラー処理・問い合わせ手段・処理フロー・サポート範囲が上流 Does Not Decide / Open Issue として未確定。
- **Missing Source or Dependency**: 上流 Does Not Decide (SDP-006)・SCR-013 §16 Open Issue・ボタン状態 follow-up #4・Input follow-up #2。
- **What Cannot Be Decided**: 可逆/不可逆規則・Recovery Action の実現手段。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: drawer 統一 TVL-0007 provenance 未確認 (別レコード)。
- **Placeholder / Inspection Pending**: ボタン状態 follow-up #4・Input follow-up #2。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 「可逆/不可逆区別責務と DS 側規則の対応の明文化」「Recovery Action 責務と DS 側の対応の明文化」(§13・§16)。
- **Downstream Impact**: Implementation の回復フロー (Repository 管理対象外)。
- **Open Issue**: 回復フロー・サポート範囲の解決主体。
- **Does Not Decide**: エラー処理仕様・問い合わせ手段を推測しない。

### 未解決: 文言・命名の正本不在 (参照切れ)

- **Source Topic**: X-07・T-02・C-09・C-10。
- **Assessment Dimension**: Cross-cutting・Foundation / token。
- **Design Responsibility**: 文言・コピー表現 (CTP-002/005)・用途ベース命名規則 (SDP-004/NVP-005)。
- **Source Assessment**: WO2 §8.4/§8.1/§11、WO3 §13/§17/§18、WO4 X-07/T-02/§17.3。
- **Source Section**: WO4 §17.3 参照切れ / X-07・T-02。
- **Related Service Design ID**: CTP-002・CTP-005・SDP-004・NVP-005。
- **Related SCR**: SCR-002・SCR-013・SCR-014。
- **Original Observation Classification**: 参照切れ。
- **Unresolved Fact**: 文言・コピーの正本 `brand-content.md`、命名規則正本 `governance/naming-rules.md`、ADR 正本が Repository 内に不在。
- **Missing Source or Dependency**: `brand-content.md`・`governance/naming-rules.md`・ADR 正本。
- **What Cannot Be Decided**: 文言表現・命名規則の DS 対応。参照切れ文書の想定内容は推測しない。
- **Repository-defined Resolution Source or Owner**: Governance README は naming-rules 未作成と明記するが解決主体は Repository 内で確認できない (未定義)。
- **Provenance**: 該当なし (存在自体が不在)。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: `brand-content.md` 不在・`governance/naming-rules.md` 不在。
- **Related Candidate Aspect**: なし (参照切れは候補根拠にしない。判定規則)。関連: X-07 は候補側面なし。
- **Downstream Impact**: Implementation の文言/命名適用 (Repository 管理対象外)。
- **Open Issue**: 正本不足の解決主体。
- **Does Not Decide**: 参照切れ文書の内容・作成は本分離で決めない。

### 未解決: Decision ID の provenance 未確認 (GOV-0002・TVL 群)

- **Source Topic**: T-04・X-02・C-01・C-02・C-07・X-01・X-05。
- **Assessment Dimension**: Foundation / token・Component / pattern・Cross-cutting。
- **Design Responsibility**: Button variant 語彙 (GOV-0002)・accent 点専用 (TVL-0011/0012)・drawer 統一 (TVL-0007)・placeholder 維持 (TVL-0008) を裏付ける Decision の provenance。
- **Source Assessment**: WO1 §12、WO2 §11、WO3 §11、WO4 §17.1。
- **Source Section**: WO4 §17.1 provenance 未確認。
- **Related Service Design ID**: GOV-0002・TVL-0001〜TVL-0012 (TVL-0009 は 4 資産に未出現)。
- **Related SCR**: SCR-001〜SCR-005・SCR-013・SCR-014 (該当 Decision を参照する範囲)。
- **Original Observation Classification**: provenance 未確認。
- **Unresolved Fact**: GOV-0002・TVL 群の ADR 正本が Repository 内に不在。一致して見えても上流適合の確定にならない。
- **Missing Source or Dependency**: ADR 正本・owner-decisions.md は確認事項一覧であり ADR ではない。
- **What Cannot Be Decided**: Decision ID の有効性・provenance を根拠とした改訂候補化。provenance 未確認を適合確認済みへ昇格しない。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: GOV-0002・TVL 群 (本レコードの主対象)。
- **Placeholder / Inspection Pending**: TVL-0008 は placeholder 維持に関与 (別レコード)。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 候補の適合根拠には使用しない。関連候補 (NAV/CTA 責務分離・Button 対応等) の provenance 制約として相互リンク (§16)。
- **Downstream Impact**: Implementation (Repository 管理対象外)。
- **Open Issue**: provenance の解決主体。
- **Does Not Decide**: provenance 未確認事項の正当性・Decision ID の再認定は本分離で決めない。

### 未解決: placeholder / 実査待ちの未取得

- **Source Topic**: T-06・T-05・T-02・C-01・C-02・C-03・C-04・C-05・C-08・X-03・X-04・X-05。
- **Assessment Dimension**: Foundation / token・Component / pattern・Cross-cutting。
- **Design Responsibility**: radius/shadow/motion・ボタン状態・Input 状態・Card 実 px/8 スロット・星実寸・「円」weight・画像 fallback の実測/確定。
- **Source Assessment**: WO1 §11、WO2 §11、WO3 §11、WO4 §17.2/T-06/X-05。
- **Source Section**: WO4 §17.2 placeholder / 実査待ち。
- **Related Service Design ID**: SDP-005 (State Visibility)・UXDR-TRAVEL-001 (保持)。
- **Related SCR**: SCR-003・SCR-004・SCR-005・SCR-013・SCR-014。
- **Original Observation Classification**: placeholder・実査待ち。
- **Unresolved Fact**: placeholder token 計 10 (radius.card/motion/shadow)・ボタン状態 (follow-up #4)・Input 状態 (follow-up #2)・Card 実 px/8 スロット・星実寸・「円」weight・画像 fallback (❓) が未取得。DS は未確定を placeholder/実査待ちとして保持 (UXDR-TRAVEL-001 対応)。
- **Missing Source or Dependency**: follow-up #2/#4 の完了・実測。
- **What Cannot Be Decided**: 値・実態確認前に改訂候補へ変換しない。placeholder/実査待ちを「対応済み」へ統合しない。
- **Repository-defined Resolution Source or Owner**: follow-up 番号の追跡先・解決主体は Repository 内で確認できない (未定義)。
- **Provenance**: `radius.card` は TVL 由来 follow-up (別レコード)。
- **Placeholder / Inspection Pending**: 本レコードの主対象 (計 10 placeholder + 実査待ち群)。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 表示責務・状態表現・アクセシビリティの各候補と相互リンク (§16)。値の確定は候補の前提ではなく未解決として保持。
- **Downstream Impact**: Implementation (Repository 管理対象外)。
- **Open Issue**: placeholder/実査待ちの解決主体。
- **Does Not Decide**: placeholder の解消方法・実測値を推測しない。

### 未解決: アクセシビリティ適用規格・達成レベルの未定義

- **Source Topic**: T-01・X-04。
- **Assessment Dimension**: Foundation / token・Cross-cutting。
- **Design Responsibility**: アクセシビリティの適用規格・達成レベル・画像 fallback。
- **Source Assessment**: WO2 §8.1、WO3 各 SCR §11、WO4 T-01/X-04。
- **Source Section**: WO4 T-01・X-04。
- **Related Service Design ID**: SDP-007・NVP-008・CTA-009・CTP-008。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-013・SCR-014。
- **Original Observation Classification**: 一部のみ確認できる (方針記述は対応を直接確認できる)。
- **Unresolved Fact**: WCAG 2.2 AA を最低ラインとする方針記述はあるが、適用規格・達成レベルが未定義。一部コントラスト未達可能性を DS が `$note` で自認。画像欠落 fallback は実査待ち。
- **Missing Source or Dependency**: 適用規格・達成レベルの上流/Governance 定義・画像 fallback 実査。
- **What Cannot Be Decided**: 具体的な達成基準値・実装方式。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 画像欠落 fallback (SCR-014)。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 「アクセシビリティ適用規格・達成レベルと focus/非依存表現の対応の明文化」(§13・§16)。
- **Downstream Impact**: Implementation のアクセシビリティ (Repository 管理対象外)。
- **Open Issue**: 適用規格・達成レベルの解決主体。
- **Does Not Decide**: 達成基準値・実装方式・画像仕様を推測しない。

### 未解決: 承認・反映・解決主体の未定義

- **Source Topic**: 全 Topic 横断 (WO4 §19「承認・反映主体」・§22)。
- **Assessment Dimension**: Cross-cutting。
- **Design Responsibility**: Alignment 評価・集約・分離結果の承認・反映主体、および各未解決事項の解決主体。
- **Source Assessment**: WO1〜WO4 の Open Issues、WO4 §19/§22。
- **Source Section**: WO4 §19「承認・反映主体」/ §22。
- **Related Service Design ID**: — (プロセス上の未定義)。
- **Related SCR**: — 。
- **Original Observation Classification**: 評価対象外 (プロセス未定義であり DS 側 Observation ではない)。
- **Unresolved Fact**: 本分離結果の承認・反映主体、各未解決事項の解決主体、Work Order 6 への引き継ぎ方法が未定義。
- **Missing Source or Dependency**: Governance の承認・レビュー主体の正本 (未整備)。
- **What Cannot Be Decided**: 承認主体・解決主体・反映主体。推測しない。
- **Repository-defined Resolution Source or Owner**: Repository 内で確認できない (未定義)。
- **Provenance**: 該当なし。
- **Placeholder / Inspection Pending**: 該当なし。
- **Broken Reference**: 該当なし。
- **Related Candidate Aspect**: 全候補の実行可否は本分離で判断しない (Work Order 6)。
- **Downstream Impact**: — 。
- **Open Issue**: 承認・反映・解決主体の定義。
- **Does Not Decide**: 承認主体を推測しない。

## 15. 分離対象外として保持する Observation

本節は新しい Observation 分類や正式 Status ではなく、改訂候補でも未解決事項でもない元 Observation を失わないための記録上の置き場所である。

- **T-07 token 参照内部整合性・DS 独立性**: semantic→primitive 参照 63/63 解決・独立 DS (R1) は「対応を直接確認できる」で、別の未解決制約を伴わない。改訂候補にも未解決事項にもしない。
- **X-02 / T-04 Fact/Decision/Promotion 分離 (対応確認部分)**: accent 点専用・根拠なき人気/ランキング/緊急性の非確定は複数 SCR/SD で「対応を直接確認できる」。この対応確認部分は改訂候補にしない (provenance と参照切れは §14 の別レコードへ分離)。
- **X-05 未確定事項の保持運用**: DS が未取得を placeholder/実査待ちとして保持し推測補完しない運用は UXDR-TRAVEL-001 に「対応を直接確認できる」。運用自体は改訂候補にしない (個々の placeholder 解決は §14 へ)。
- **各 Topic の対応を直接確認できる部分**: CTA-002「主 CTA primary 1 つ」(C-01)・検索開始 CTA Button.primary (C-02)・PriceTag 条件併記構造 (C-04)・ReviewStars 数値併記 (C-05)・非視覚依存の方針記述 (X-04)・タイポグラフィスケール記述 (T-03)・component の実在 (C-06/C-07)。これらの対応確認部分は改訂候補にせず、候補側面は別途 §13 に責務レベルで記載した。
- **§18 矛盾・過剰の不在 (対象 snapshot 限定の Fact)**: 入力評価 (WO2/WO3) の範囲で直接的矛盾・過剰は確認されていない。これは対象 snapshot・入力評価の範囲に限定した Fact であり、改訂候補にも未解決事項にもしない。再評価により新しい矛盾・過剰を創作しない (§18)。
- **評価対象外 Observation**: SCR-006〜SCR-012 依存事項・User (認証・会員・履歴保存, 上流制約で取り込まない)・Assets・Implementation は Work Order 5 の処理対象でない評価対象外として保持する。
- **元評価の境界・Does Not Decide**: 各 Topic の Does Not Decide (状態の業務定義・token 値・component 採用等を決めない)・Downstream Impact の Component 例を採用決定としない境界を保持する。

## 16. Candidate–Unresolved Dependency Relationships

候補側面と未解決側面が併存する設計責務について、両者を相互リンクする。未解決事項があるため候補が実行可能かどうかは判断しない (Work Order 6)。`conditional candidate` 等の新しい正式分類を作らず、候補を `blocked`/`ready` 等の実行状態へ分類しない。

| 設計責務 (Source Topic) | 改訂候補側面 (§13) | 依存する未解決事項 (§14) |
| --- | --- | --- |
| NAV 分類対応 (C-06・X-01) | NAV 分類と Navigation component の対応明文化・NAV/CTA 責務分離の本文規則明文化 | Navigation 分類・Global Nav・History and Recovery の上流未定義／GOV-0002 provenance |
| 状態モデル対応 (X-03・T-02・C-08) | 上流状態モデルと DS 状態表現の対応明文化・Recovery Action 責務の対応明文化 | 上流状態モデルの業務定義／可逆・回復の上流未定義／placeholder・実査待ち (follow-up #4・motion) |
| IA Object 表現 (C-10・X-06) | IA Object・Content Category の表現責務と DS 表現語彙の対応明文化 | IA Object の業務モデル／文言・命名の正本不在 |
| 入力・検索 (C-02) | 入力の状態表現・回復責務と DS Input 定義の対応明文化 | 入力・検索仕様の上流未定義／placeholder・実査待ち (Input follow-up #2)／GOV-0002 provenance |
| 表示 (C-03・C-04・C-05・T-05・T-03) | 表示責務と DS component の対応明文化・タイポグラフィ具体規格の対応明文化 | 表示仕様の上流未定義／placeholder・実査待ち (Card 実 px・星実寸・「円」weight・radius.card/shadow) |
| 可逆/回復 (C-07・C-08) | 可逆/不可逆区別責務と DS 側規則の対応明文化・Recovery Action 責務の対応明文化 | 可逆/不可逆・回復フローの上流未定義／TVL-0007 provenance／placeholder・実査待ち |
| アクセシビリティ (T-01・X-04) | 適用規格・達成レベルと focus/非依存表現の対応明文化 | アクセシビリティ適用規格・達成レベルの未定義／画像 fallback 実査待ち |
| CTA 主要行動 (C-01) | 情報確認と選択の区別・主要行動と Button の対応明文化 | 主要 CTA の上流未定義／GOV-0002 provenance／ボタン状態 follow-up #4 |
| 支援領域 (C-09) | 支援領域の表現責務と DS 対応の明文化 (限定的) | 可逆/回復の上流未定義 (サポート範囲・FAQ 構成)／文言・命名の正本不在／未着手 component |
| Navigation/CTA 責務分離 (X-01) | 責務分離を述べる DS 本文規則の明文化 | Decision ID の provenance (GOV-0002) |

## 17. Provenance, Placeholder, Inspection-pending, and Broken Reference Boundary

Work Order 4 §17 の証拠制約を分離後も保持する。これらは値・実態・正本の確認前に改訂候補へ変換しない (§11.2)。

- **provenance 未確認** (GOV-0002・TVL 群・外部 URL): §14「Decision ID の provenance 未確認」レコードへ分離。候補の適合根拠に使用しない。
- **placeholder / 実査待ち** (計 10 placeholder token・follow-up #2/#4・Card 実 px・星実寸・「円」weight・画像 fallback): §14「placeholder / 実査待ちの未取得」レコードへ分離。値確認前に「対応済み」へ統合しない。
- **参照切れ** (`brand-content.md`・`governance/naming-rules.md`・ADR 正本不在): §14「文言・命名の正本不在」レコードへ分離。想定内容を候補根拠にしない。
- 上記の分離は、gap の原因責任・解決策・優先順位・改訂着手可否を決めない (Work Order 6)。

## 18. Conflict and Over-coverage Boundary

- **矛盾 (矛盾)**: 入力評価文書 (Work Order 2・Work Order 3) および Work Order 4 集約の範囲では、上流と DS 記述の直接的矛盾は確認されていない。本分離はこの対象 snapshot・入力評価の範囲に限定して「直接的矛盾は確認されていない」と記載し、再評価により新しい矛盾を創作しない。矛盾が入力評価にないため、矛盾を根拠とする改訂候補を作らない。
- **過剰 (過剰)**: 入力評価文書・Work Order 4 に「過剰」と明示された Observation は確認されない。本分離で新たに「過剰」と判定せず、削除候補を作らない。
- 上記は §15 の分離対象外 (対象 snapshot 限定の Fact) として保持する。

## 19. Source-specific Variations

Work Order 4 §16 のスコープ固有差異を分離後も保持し、無理に共通候補へ昇格させない。

- **状態色 (T-02)**: SCR-003 の Input disabled/success 未取得 (follow-up #2)・error 暫定 placeholder、SCR-004 の motion placeholder。単一の状態対応へ統一せず、各々を §14「placeholder/実査待ち」「状態モデルの業務定義」へ分離。
- **accent・Fact/Promotion (T-04・X-02)**: TVL Decision ID が SCR-001/SCR-005 は TVL-0012、SCR-002/SCR-014 は TVL-0011/0012。片方へ正規化せず §14「Decision ID の provenance」へ分離。
- **Button (C-01)**: SCR-005 の CTA-004・SCR-004 の比較/選択の優先関係は SCR 固有。CTA-002 (主 CTA 1 つ) と統合しない。候補は責務レベルで記述。
- **SearchForm/Input (C-02)**: SCR-001 の入口探索起点と SCR-003 の検索実行はスコープが異なる。候補・未解決とも SCR 別に保持。
- **Card (C-03)**: SCR-004 検索結果・SCR-005 詳細用途・SCR-002/SCR-014 Supporting の用途差を保持。
- **Navigation component (C-06)**: SCR ごとに宣言する Navigation Types が異なる (SCR-001 NAV-001/004/006 等)。共通一覧へ正規化しない。候補は「対応明文化余地」として責務レベルで記述。
- **Recovery/支援 (C-08・C-09)**: SCR-013 固有。他 SCR へ拡張しない。
- **専用表現語彙 (C-10)**: SCR-005 の Room/Stay Plan/Policy 業務モデル・SCR-003 の User (対象外) は IA Object ごとに事情が異なる。
- **状態モデル (X-03)**: SCR ごとの Navigation States が異なり、SCR-004 は `Error / Interrupted` を含み SCR-014 は含まない。SCR-014 に `Error / Interrupted` を追加せず正規化しない。`Error / Interrupted` は 1 つの複合状態名。
- **Accessibility (X-04)**: SCR-014 の画像欠落 fallback (実査待ち) は SCR-014 固有。

## 20. Work Order 5 Completion Boundary

- Work Order 4 の T-01〜T-07・C-01〜C-10・X-01〜X-07 を Separation Traceability Index (§12) で追跡し、各 Topic を改訂候補側面 (§13)・未解決事項側面 (§14)・分離対象外 (§15) へ引き継いだ。Source-specific Variations (§19)・provenance/placeholder/実査待ち/参照切れ (§17)・Conflict/Over-coverage (§18)・Unresolved Dependencies (§14) を保持した。候補と未解決事項が併存する Topic は側面単位で分け、§16 で相互リンクした。よって Work Order 5 を Draft として実施済みとする。
- 本文書は次を実施していない: 改訂候補の採用・却下・改訂内容/解決策の提案・優先順位/重要度/severity/対応順の決定・工数/担当者/期限の設定・候補への `ready`/`blocked`/`approved` 状態付与・新規 Issue への分解・実際の Design System 変更。Work Order 6 (改訂着手可否の判断)・Design System の改定要否判断・承認主体の推測も行っていない。
- 「Work Order 5 実施済み」は、Alignment 全体の完了・Design System 適合・改定要否決定・改定可能・改訂着手可能・承認済みを意味しない。

## 21. Downstream Impact

- **Assets** ([../assets/README.md](../assets/README.md)) — `Not started`。本分離の対象外。
- **Implementation** — Repository 管理対象外。本分離は静的な分離記録であり実装検証ではない。DS から実装画面・URL・route を導出しない。各 Screen Requirement の Downstream Impact に列挙された Component 例を採用決定と解釈しない。

## 22. Open Issues

以下は未決である。解決策は推測して記載しない。

- 本分離結果の承認・反映主体、および Work Order 6「改訂着手可否の判断」への引き継ぎ方法。
- §14 に整理した未解決事項 (状態モデル業務定義・Navigation 分類・IA 業務モデル・入力/表示仕様・可逆/回復・文言/命名正本・provenance・placeholder/実査待ち・アクセシビリティ規格・承認主体) の解決主体。
- 改訂を検討し得る候補のうち、上流 Open Issue や provenance に依存するものが確定できる条件 (Work Order 6 で判断)。
- 正式な候補 ID・未解決事項 ID・分類体系・ファイル名の確定 (本ファイル名 `alignment-amendment-candidate-separation.md` は暫定)。

## 23. Does Not Decide

- 改訂候補の採用・却下、Design System の改定要否。
- 改訂内容・解決策・実装方法、gap の原因責任。
- 優先順位・重要度・severity・対応順、工数・担当者・期限。
- token 値/名/階層/正式な命名規則・placeholder の解消方法。
- Component の追加/削除/統合/分割・Component API/variant/state/実装仕様。
- Service Design または Screen Requirement の修正・SCR-006〜SCR-012 の要求。
- UI 構造・表示項目・表示順・情報密度・API/DB/URL/route・実装 Repository との適合。
- 参照切れ文書の内容・provenance 未確認事項の正当性・正式な候補 ID/未解決事項 ID/分類体系/ファイル名・UX Decision の追加。
- 改訂着手可否 (Work Order 6)・Alignment 完了条件・承認主体。
- 「対応を直接確認できる」を要件充足・承認完了へ、「対応する定義を確認できない」「一部のみ確認できる」を機械的に改訂候補へ、placeholder/実査待ち/provenance 未確認/参照切れを解決済み・改訂候補へ変換しない。

## 24. Relationship to Subsequent Work

- 本分離 (Work Order 5) は、Alignment Plan §10 の次段である Work Order 6「実際の改訂タスクを開始できるかの判断 (改訂着手可否の判断)」の入力となる。
- Work Order 6 は本 PR のマージ前には開始しない。
- Work Order 6 は、改訂候補と未解決事項・その依存関係 (§16) を入力に、Open Issue の解決状況と承認主体の有無から改訂の着手可否を判断する段である。本分離はその判断を含まない。
- 本分離は Design System の修正・新しい Decision・UX Decision を含まない。Design System の改定は Work Order 6 の判断後の承認された別タスクでのみ扱う。

## 25. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-17 | Initial separation (Work Order 5): Work Order 4 で集約された Observation (T-01〜T-07・C-01〜C-10・X-01〜X-07・§16〜§19) を、改訂を検討し得る候補・未解決に依存し確定できない事項・分離対象外として保持する Observation へ、設計責務の側面単位で分離。候補と未解決事項が併存する Topic は側面を分け相互リンク。元 Observation 分類・provenance・placeholder・実査待ち・参照切れを Separation Traceability Index で追跡。改訂内容・解決策・優先順位・改定要否・改訂着手可否は未決定 | Draft |
