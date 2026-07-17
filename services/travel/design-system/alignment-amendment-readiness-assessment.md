# Travel Alignment Amendment Readiness Assessment

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Alignment Assessment のうち、Work Order 5 ([alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md)) で分離した各改訂候補側面について、関連する未解決事項と Repository 内の直接証拠を照合し、実際の Design System 改訂タスクを開始できる状態かを記録した着手可否評価。Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 6「実際の改訂タスクを開始できるかの判断 (改訂着手可否の判断)」の実行。Design System の改定・候補の採用/却下・解決策の設計・優先順位付けは行わない。
- Position in Repository: `services/travel/design-system/alignment-amendment-readiness-assessment.md` — Design System レイヤー (travel サービス配下)。Design System README の Reference Order 上で自身より前に配置される上流成果物は、レイヤー入口 [README.md](README.md)・Alignment 計画 [alignment-plan.md](alignment-plan.md)・Baseline 評価 [baseline-assessment.md](baseline-assessment.md)・Service Design 横断整合性評価 [service-design-alignment-assessment.md](service-design-alignment-assessment.md)・Screen Requirements 個別整合性評価 [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md)・Observation 横断集約 [alignment-observations-aggregation.md](alignment-observations-aggregation.md)・改訂候補と未解決事項の分離 [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md)。Service Design 成果物・Screen Requirements 成果物・既存 Design System 4 成果物との関係は本文 Sources (§5) / Evidence Rules (§7) / Relationship (§15) に記載し、Position の上流成果物へ混在させない。下流成果物 (Assets / Implementation) との関係は Downstream Impact (§12) を参照。

本文書は着手可否評価の記録であり、Design System 仕様・Design Decision・改訂着手の承認一覧の正本ではない。評価は静的であり、Design System を変更しない。判断表現 (§8) は Work Order 6 内の記録用であり、正式 Status・恒久的分類・Decision ID・優先度ではない。ファイル名 `alignment-amendment-readiness-assessment.md` は記述的な暫定識別子であり、正式な分類体系・評価 ID・命名規則を確定しない。Work Order 4・5 の T/C/X ラベルは入力文書内の説明用 Topic 参照であり、正式 ID へ昇格させず、新しい候補 ID を採番しない。SCR ID は Screen Matrix 上の画面候補 ID であり、Screen Requirement 文書 ID・実装画面 ID・URL・route と同一視しない。Fact / Decision / Hypothesis / Open Issue を区別し、新しい Design Decision・UX Decision を追加しない。

## 1. Purpose

- Alignment Plan ([alignment-plan.md](alignment-plan.md)) §10 Recommended Work Order の 6「実際の改訂タスクを開始できるかの判断 (改訂着手可否の判断)」を実行する。
- Work Order 5 で分離した各候補側面 (§13) と、Work Order 5 §14・§16 で関連付けられた未解決事項を入力に、候補ごとに実際の Design System 改訂タスクを開始できる状態かを、Repository 内の直接証拠だけで判断・記録する。
- 候補別判断から総合的な改訂着手可否を導出する。
- これは静的な着手可否評価であり、Design System の改定・候補の採用/却下・解決策の設計・優先順位付けではない (§10・§13)。
- 「未解決事項を調査・解決する作業が可能であること」と「Design System の実際の改訂タスクを開始できること」を区別する。本タスクでは未解決事項を解決する Issue や branch を追加作成しない。

## 2. Readiness Assessment Snapshot

- Assessment target: 作業開始時点の `main`。
- Assessment snapshot (main commit SHA): `eb0b89128a4edba8182927516fe4423006d4acf8` (PR #55 merge)。
- 評価日: 2026-07-17。
- 本評価は Repository 内文書の静的な着手可否評価であり、実装検証・Design System の改定ではない。評価中に main の更新はなく、異なる snapshot を混在させていない。

### 入力文書 (blob SHA @ `eb0b891`)

| 入力 | ファイル | 役割 | blob SHA |
| --- | --- | --- | --- |
| 正本入力 (Work Order 5) | [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md) | 候補側面 (§13)・未解決事項 (§14)・相互リンク (§16) | `bbe0faf8e3b3d6d2318bf41fbf19a3002e8de188` |
| 集約 (Work Order 4) | [alignment-observations-aggregation.md](alignment-observations-aggregation.md) | 集約 Topic・Unresolved Dependencies | `89ef99de6da00b226bb12445d7dfe253e49a2e84` |
| 方法・境界 | [alignment-plan.md](alignment-plan.md) | 評価方法・分類・順序・§10 Work Order | `40e29ce48fc14c3d79570a8cf897af53dfa88e39` |
| 証拠制約 (Work Order 1) | [baseline-assessment.md](baseline-assessment.md) | token/placeholder/provenance/参照切れ | `89ea9d17257cf2e5b162dc702944b21033ef71e2` |
| 追跡確認 (Work Order 2) | [service-design-alignment-assessment.md](service-design-alignment-assessment.md) | SD 横断責務の元 Observation | `528b3cccc0bb0c91ec3a1a8a233f8ff28152475b` |
| 追跡確認 (Work Order 3) | [screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) | 7 SCR の元 Observation | `521d3b54d9cba455c2b07db4edfb059865447a28` |

### 既存 Design System 4 成果物 (再評価・変更しない)

- [design.md](design.md) / [semantic.travel.json](semantic.travel.json) / [primitive.travel.json](primitive.travel.json) / [components.md](components.md)。いずれも Draft・version `0.3.0-draft`。本評価はこれらを変更しない。

## 3. Scope

- Work Order 5 §13 に記録された全 12 候補側面と §16 の相互リンクを正本入力とし、漏れなく着手可否を評価する。
- 各候補について、関連する未解決事項 (Work Order 5 §14) と Repository 内の直接証拠を照合する。
- 総合的な改訂着手可否を候補別判断から導出する。

## 4. Out of Scope

- Design System の改定・候補の採用/却下・改定要否の判断・解決策の設計・優先順位付け。
- 具体的な改訂内容・変更対象 Component/token/値/UI・工数/担当者/期限。
- Work Order 5 §15「分離対象外として保持した Observation」の改訂候補化。
- 未解決事項を解決する Issue/branch の作成、未解決事項自体の解決。
- SCR-006〜SCR-012 の評価・要求定義。
- 数値スコア・適合率・件数ランキング・pass/fail・severity・優先順位の導入。
- Assets・Implementation の仕様、API/DB/URL/route/画面遷移。

## 5. Sources

Position の上流成果物 (README / alignment-plan / baseline-assessment / service-design-alignment-assessment / screen-requirements-alignment-assessment / alignment-observations-aggregation / alignment-amendment-candidate-separation) と区別し、本評価が参照する成果物を示す。

- **正本入力**: [alignment-amendment-candidate-separation.md](alignment-amendment-candidate-separation.md) (Work Order 5) の §13 候補・§14 未解決事項・§16 相互リンク。
- **方法・境界**: [alignment-plan.md](alignment-plan.md) (§6 Evidence Rules / §8 Observation Classification / §10 Recommended Work Order)。
- **証拠制約・追跡確認**: [baseline-assessment.md](baseline-assessment.md) (Work Order 1)・[service-design-alignment-assessment.md](service-design-alignment-assessment.md) (Work Order 2)・[screen-requirements-alignment-assessment.md](screen-requirements-alignment-assessment.md) (Work Order 3)・[alignment-observations-aggregation.md](alignment-observations-aggregation.md) (Work Order 4)。
- **承認・解決主体の確認対象**: [../../../governance/README.md](../../../governance/README.md) / [../../../governance/owner-decisions.md](../../../governance/owner-decisions.md)。承認・レビュー主体・ADR 正本の整備状況を確認する (定義有無の Fact 確認に限る)。
- **入力評価文書を通じて追跡される成果物 (再評価しない)**: Service Design SD-001〜SD-007・作成済み 7 個別 Screen Requirement・既存 Design System 4 成果物。

## 6. Method

- Work Order 5 §13 の各候補側面を起点に、§16 の相互リンクで関連付けられた未解決事項 (§14) と、Repository 内の直接証拠 (上流責務の実在・provenance/正本参照の状況・placeholder/実査待ちの状況・承認/解決主体の定義状況) を照合する。
- 候補ごとに §7 の記録項目を作成し、§8 の判断表現・判断規則で着手可否を記録する。
- 候補別判断から総合判断 (§10) を導出する。結論を作業開始前に固定しない。
- 判断には Repository 内で直接確認できる Fact だけを使用する。未確認の事業要求・業務仕様・画面仕様・担当者・期限・承認者を推測しない。
- Navigation と CTA を別責務として扱う。Navigation State Model・CTA State Model・Status and Uncertainty Model・Component state を同一視しない。`Error / Interrupted` を 1 つの複合状態名として扱い、SCR 間の状態差を正規化しない。IA Object を Component/表示項目/データモデルと、Content Category を Component/掲載枠と同一視しない。

## 7. Evidence Rules

Alignment Plan §6 と Work Order 5 の Evidence Rules を継承する。

- 判断の証拠は、Work Order 5 が記録した候補側面・未解決事項と、その元出典 (Work Order 1〜4 の実在記述)、および Governance の承認・解決主体の定義状況に限定する。入力文書が記録していない対応・不足を本評価で新たに作らない。
- 既存 Design System 4 成果物は再評価せず、入力評価文書が引用した範囲で追跡する。
- provenance 未確認の記述・参照切れ文書の想定内容・上流 Open Issue に依存する具体仕様を、着手可否の肯定的根拠に使用しない。
- Repository 内で承認・反映・解決主体が定義されていない場合、ユーザーや Claude Code を主体と推測せず、確認できない Fact として記録する。
- 候補が存在することを、採用済み・改定必要・着手可能・承認済みと解釈しない。

## 8. Judgment Expressions and Rules

### 8.1 判断表現 (Work Order 6 内の記録用)

以下は本 Work Order 内だけの記録用表現であり、正式 Status・恒久的分類・Decision ID・優先度ではない。

- `開始できる`
- `現時点では開始できない`
- `Repository 内の証拠だけでは判断できない`

### 8.2 判断規則

- 必要な上流責務・関連 Open Issue・provenance・正本参照・placeholder/実査待ち・承認/解決主体などが Repository 内の直接証拠で満たされている場合だけ `開始できる`。
- 明示的な未解決依存または必要条件の欠落が確認できる場合は `現時点では開始できない`。
- Repository 内の証拠不足により、条件が満たされたか欠落しているか自体を判定できない場合は `Repository 内の証拠だけでは判断できない`。

### 8.3 承認・解決主体に関する共通 Fact

- Governance README ([../../../governance/README.md](../../../governance/README.md)) は、命名規則・ADR・レビュー規則の正本が未整備であることを明記する。[owner-decisions.md](../../../governance/owner-decisions.md) は「オーナー確認事項」の一覧であり、改訂着手の承認主体・反映主体・解決主体を定義する正本ではない。
- したがって、Repository 内に「実際の Design System 改訂タスクの承認・反映・解決主体」を定義した成果物は確認できない。これは全候補に共通する必要条件 (承認・解決主体) の欠落として確認できる Fact であり、ユーザーや Claude Code を主体と推測しない。

## 9. Candidate-by-candidate Readiness Assessment

Work Order 5 §13 の全 12 候補側面を評価する。各レコードの `Current Judgment` は §8 の判断表現、`Source Topic` は Work Order 4・5 内の説明用 Topic 参照 (正式 ID ではない)。

### 9.1 NAV 分類と DS Navigation component の対応の明文化

- **Candidate Aspect**: 上流 Navigation Types (NAV-001〜006) の責務と DS 側 Navigation component の対応関係の明文化余地。
- **Source Topic**: C-06 (関連 X-01)。
- **Design Responsibility**: Navigation Types を UI として表現する責務と Navigation component の対応。
- **Related Service Design ID**: NVP-001・NAV-001〜006。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-004・SCR-005・SCR-013・SCR-014。
- **Related Unresolved Dependency**: 「Navigation 分類・Global Nav・History and Recovery の上流未定義」(WO5 §14・§16)。
- **Upstream Definition Evidence**: NAV-001〜006 は SD-003 navigation.md に実在。ただし Global Navigation 対象領域・History and Recovery (NAV-005) 保持方式は navigation.md §10 / 各 SCR §16 Open Issue。
- **Provenance / Canonical Source Condition**: 該当する provenance 阻害はなし (NAV 分類自体は正本に実在)。
- **Placeholder / Inspection Pending Condition**: 該当なし。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応関係の明文化余地であり、特定 component の追加・NAV への割当ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: Global Nav 対象領域・History and Recovery 保持方式が上流 Open Issue として未確定であることを navigation.md §10 で直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 上流 NAV Open Issue の未解決・承認/解決主体の未定義。
- **What Cannot Start**: NAV 分類対応を明文化する実際の Design System 改訂タスク。
- **Does Not Authorize**: NAV 分類対応の明文化・component 追加を承認しない。
- **Does Not Decide**: Navigation Types と component の対応内容・改定要否は決めない。Navigation と CTA を混同しない。
- **Downstream Impact**: Implementation のナビゲーション (Repository 管理対象外)。

### 9.2 Navigation と CTA の責務分離を述べる DS 本文規則の明文化

- **Candidate Aspect**: UXDR-TRAVEL-003 が求める Navigation/CTA 責務分離を DS 本文規則として明文化する余地。
- **Source Topic**: X-01 (関連 C-06・C-01)。
- **Design Responsibility**: Navigation 要素と CTA 要素を別 Pattern・別評価軸で扱う責務の DS 側明文化。
- **Related Service Design ID**: UXDR-TRAVEL-003・NAV-001〜006・CTA-002。
- **Related SCR**: SCR-001〜SCR-005・SCR-013・SCR-014。
- **Related Unresolved Dependency**: 「Decision ID の provenance 未確認 (GOV-0002)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: UXDR-TRAVEL-003 は SD-007 に Accepted な UX Decision として実在。DS 側に責務分離の本文規則が不在であることも確認できる。
- **Provenance / Canonical Source Condition**: Button variant 語彙 GOV-0002 は ADR 正本なし → provenance 未確認。
- **Placeholder / Inspection Pending Condition**: 該当なし。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 責務分離規則の明文化余地であり、規則内容の確定ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 上流責務 (UXDR-TRAVEL-003) は実在するが、承認・反映・解決主体が未定義 (§8.3) であり、実際の DS 改訂タスクを開始する必要条件 (承認主体) を欠く。GOV-0002 provenance 未確認も肯定的根拠に使用しない。
- **Missing Evidence or Blocking Fact**: 承認/解決主体の未定義・GOV-0002 provenance 未確認。
- **What Cannot Start**: 責務分離規則を DS へ記述する実際の改訂タスク。
- **Does Not Authorize**: 責務分離規則の追加を承認しない。
- **Does Not Decide**: 責務分離規則の内容・改定要否は決めない。
- **Downstream Impact**: Implementation の Navigation/CTA 実装 (Repository 管理対象外)。

### 9.3 上流状態モデルと DS 状態表現の対応の明文化

- **Candidate Aspect**: Navigation State Model・CTA State Model・Status and Uncertainty Model と DS 状態表現の対応関係の明文化余地。
- **Source Topic**: X-03 (関連 T-02・C-08)。
- **Design Responsibility**: 各状態モデルを UI として表現する責務と DS 状態表現の対応。
- **Related Service Design ID**: Navigation State Model・CTA State Model・Status and Uncertainty Model・CTP-006・CTA-007・SDP-005。
- **Related SCR**: SCR-001〜SCR-005・SCR-013・SCR-014。
- **Related Unresolved Dependency**: 「上流状態モデルの業務定義」「placeholder/実査待ち (follow-up #4・motion)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: 状態モデルは SD-003/SD-004/SD-005 に実在。ただし各状態 (Pending Confirmation・空結果/在庫切れ挙動・予約状態) の業務定義は上流 Open Issue。
- **Provenance / Canonical Source Condition**: 該当なし。
- **Placeholder / Inspection Pending Condition**: ボタン状態 follow-up #4・motion placeholder が未取得。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応関係の明文化余地であり、状態一覧の確定・token/component の追加ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 状態の業務定義が上流 Open Issue、ボタン状態が follow-up #4 実査待ち・motion が placeholder であることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 上流状態業務定義の未解決・placeholder/実査待ち・承認/解決主体の未定義。
- **What Cannot Start**: 状態モデル対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: 状態の具体一覧・状態表示 component の追加を承認しない。
- **Does Not Decide**: 状態の業務定義・UI 表現・token 値は決めない。Navigation State Model・CTA State Model・Component state を同一視しない。SCR-014 に `Error / Interrupted` を追加しない。
- **Downstream Impact**: Implementation の状態遷移表示 (Repository 管理対象外)。

### 9.4 Recovery Action 責務と DS 側の対応の明文化

- **Candidate Aspect**: 中断・エラーからの回復行動 (CTA-TYPE-004) の責務と DS 側の対応関係の明文化余地。
- **Source Topic**: C-08 (関連 X-03)。
- **Design Responsibility**: Recovery Action を UI として表現する責務と DS 側の対応。
- **Related Service Design ID**: CTA-TYPE-004・CTA-007。
- **Related SCR**: SCR-013。
- **Related Unresolved Dependency**: 「可逆/不可逆・回復フローの上流未定義 (問い合わせ手段・処理フロー・サポート範囲)」「placeholder/実査待ち (follow-up #4)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: CTA-TYPE-004 は SD-005 に実在。ただし問い合わせ手段・処理フロー・サポート対象範囲は SCR-013 §16 Open Issue。
- **Provenance / Canonical Source Condition**: 該当なし。
- **Placeholder / Inspection Pending Condition**: ボタン状態 follow-up #4 が未取得。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応関係の明文化余地であり、Recovery Action 用 component の追加ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 問い合わせ手段・処理フロー・サポート範囲が上流 Open Issue、ボタン状態が follow-up #4 実査待ちであることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 上流回復フロー Open Issue の未解決・実査待ち・承認/解決主体の未定義。
- **What Cannot Start**: Recovery Action 対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: Recovery Action 用 component/規則の追加を承認しない。
- **Does Not Decide**: Recovery Action の component/規則を決めない。未着手 component を必要 component へ変換しない。
- **Downstream Impact**: Implementation の回復動線 (Repository 管理対象外)。

### 9.5 IA Object・Content Category の表現責務と DS 表現語彙の対応の明文化

- **Candidate Aspect**: 宿泊領域の IA Object と Content Category を UI として表現する責務と DS 表現語彙の対応関係の明文化余地。
- **Source Topic**: C-10 (関連 X-06)。
- **Design Responsibility**: IA Object・Content Category の表現責務と DS 表現語彙の対応。
- **Related Service Design ID**: IA-OBJ-001・IA-OBJ-004・IA-OBJ-005・IA-OBJ-006・IA-OBJ-008・IA-OBJ-010・IA-OBJ-012・Content Categories (6)。
- **Related SCR**: SCR-001・SCR-002・SCR-004・SCR-005・SCR-013・SCR-014。
- **Related Unresolved Dependency**: 「IA Object の業務モデル (IA §11 Open Issue・SCR-005/006 境界)」「文言・命名の正本不在」(WO5 §14・§16)。
- **Upstream Definition Evidence**: IA-OBJ 群・Content Categories は SD-002/SD-004 に実在。ただし内容・関係・業務仕様は information-architecture.md §11 Open Issue。
- **Provenance / Canonical Source Condition**: Content 文言の正本 `brand-content.md` は参照切れ。
- **Placeholder / Inspection Pending Condition**: 該当なし。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 表現責務の対応整理の明文化余地であり、専用 component の追加ではない。IA Object を Component/表示項目/データモデルと同一視しない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: IA Object の業務モデルが IA §11 Open Issue、`brand-content.md` が参照切れであることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: IA §11 Open Issue の未解決・参照切れ・承認/解決主体の未定義。
- **What Cannot Start**: IA Object・Content Category 対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: 専用表現語彙・component の追加を承認しない。
- **Does Not Decide**: 専用 component の要否・業務モデルは決めない。IA Object を Component、Content Category を掲載枠と同一視しない。
- **Downstream Impact**: Implementation の各領域表現 (Repository 管理対象外)。

### 9.6 可逆/不可逆区別責務と DS 側規則の対応の明文化

- **Candidate Aspect**: 可逆操作・回復可能性 (SDP-006)・不可逆前の可逆 (CTA-006) を UI として区別する責務と DS 側規則の対応関係の明文化余地。
- **Source Topic**: C-07。
- **Design Responsibility**: 可逆/不可逆の区別責務と DS 側規則の対応。
- **Related Service Design ID**: SDP-006・CTA-006。
- **Related SCR**: — (WO2 横断責務)。
- **Related Unresolved Dependency**: 「可逆/不可逆・回復フローの上流未定義 (保存期間・Undo・エラー処理)」「Decision ID の provenance (TVL-0007)」「placeholder/実査待ち (Input follow-up #2)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: SDP-006・CTA-006 は SD-001/SD-005 に実在。ただし保存期間・Undo・エラー処理仕様は上流 Does Not Decide。
- **Provenance / Canonical Source Condition**: drawer 統一 TVL-0007 は provenance 未確認。
- **Placeholder / Inspection Pending Condition**: Input 状態一式 follow-up #2 実査待ち。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 区別規則の対応の明文化余地であり、保存期間・Undo の仕様確定ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 保存期間・Undo・エラー処理が上流 Does Not Decide、Input 状態が follow-up #2 実査待ち、TVL-0007 が provenance 未確認であることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 上流 Does Not Decide・実査待ち・provenance 未確認・承認/解決主体の未定義。
- **What Cannot Start**: 可逆/不可逆区別規則を明文化する実際の改訂タスク。
- **Does Not Authorize**: 可逆/不可逆規則の追加を承認しない。
- **Does Not Decide**: 可逆/不可逆規則・エラー処理仕様は決めない。
- **Downstream Impact**: Implementation の回復フロー (Repository 管理対象外)。

### 9.7 アクセシビリティ適用規格・達成レベルと focus/非依存表現の対応の明文化

- **Candidate Aspect**: アクセシビリティの適用規格・達成レベルと DS の focus/非依存表現の対応関係の明文化余地。
- **Source Topic**: T-01・X-04。
- **Design Responsibility**: アクセシビリティ責務 (SDP-007/NVP-008/CTA-009/CTP-008) と適用規格・達成レベルの対応。
- **Related Service Design ID**: SDP-007・NVP-008・CTA-009・CTP-008。
- **Related SCR**: SCR-001・SCR-002・SCR-003・SCR-013・SCR-014。
- **Related Unresolved Dependency**: 「アクセシビリティ適用規格・達成レベルの未定義」「画像 fallback 実査待ち」(WO5 §14・§16)。
- **Upstream Definition Evidence**: SDP-007/NVP-008/CTA-009/CTP-008 は上流に実在。design.md §2 は「WCAG 2.2 AA を最低ライン」と記述するが、適用規格・達成レベルは未定義。
- **Provenance / Canonical Source Condition**: 該当なし。
- **Placeholder / Inspection Pending Condition**: 画像欠落 fallback (SCR-014) は実査待ち。一部コントラスト未達可能性を JSON `$note` が自認。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 適用規格・達成レベルの対応の明文化余地であり、達成基準値の確定ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 適用規格・達成レベルの確定主体が未定義、画像 fallback が実査待ちであることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 適用規格・達成レベルの確定主体未定義・実査待ち・承認/解決主体の未定義。
- **What Cannot Start**: アクセシビリティ規格対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: 達成基準値・実装方式の確定を承認しない。
- **Does Not Decide**: 適用規格・達成レベル・実装方式・画像仕様は決めない。
- **Downstream Impact**: Implementation のアクセシビリティ実装 (Repository 管理対象外)。

### 9.8 情報確認と選択の区別・CTA 主要行動責務と DS Button 定義の対応の明文化

- **Candidate Aspect**: 情報確認と選択の区別 (CTA-004)・主要行動の優先関係 (CTA-001) の責務と DS Button 定義の対応関係の明文化余地。
- **Source Topic**: C-01。
- **Design Responsibility**: 情報確認と選択の区別・主要行動の責務と Button 定義の対応。
- **Related Service Design ID**: CTA-001・CTA-004。
- **Related SCR**: SCR-004・SCR-005。
- **Related Unresolved Dependency**: 「主要 CTA の上流未定義」「Decision ID の provenance (GOV-0002)」「placeholder/実査待ち (ボタン状態 follow-up #4)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: CTA-001/CTA-004 は SD-005 に実在。ただし各 SCR で主要行動が未定義 (上流 Open Issue)。
- **Provenance / Canonical Source Condition**: Button variant 語彙 GOV-0002 は provenance 未確認。
- **Placeholder / Inspection Pending Condition**: ボタン状態 follow-up #4 実査待ち。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応関係の明文化余地であり、主要 CTA の確定・variant 追加ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 各 SCR で主要行動が未定義 (上流 Open Issue)、ボタン状態が follow-up #4 実査待ち、GOV-0002 が provenance 未確認であることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 主要行動の上流未定義・実査待ち・provenance 未確認・承認/解決主体の未定義。
- **What Cannot Start**: CTA 主要行動対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: 主要 CTA の確定・variant 追加を承認しない。
- **Does Not Decide**: 主要 CTA・variant の改廃は決めない。Navigation と CTA を混同しない。
- **Downstream Impact**: 各 SCR Downstream Impact の Button 例を採用決定と解釈しない (Repository 管理対象外)。

### 9.9 入力の状態表現・回復責務と DS Input 定義の対応の明文化

- **Candidate Aspect**: 検索条件の入力・状態表現・回復 (IA-OBJ-002/SDP-006/CTP-007) の責務と DS Input/SearchForm 定義の対応関係の明文化余地。
- **Source Topic**: C-02。
- **Design Responsibility**: 入力の状態表現・回復責務と Input 定義の対応。
- **Related Service Design ID**: IA-OBJ-002・SDP-006・CTP-007・CTA-001/005。
- **Related SCR**: SCR-001・SCR-003。
- **Related Unresolved Dependency**: 「入力・検索仕様の上流未定義」「placeholder/実査待ち (Input follow-up #2)」「Decision ID の provenance (GOV-0002)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: IA-OBJ-002・SDP-006・CTP-007 は上流に実在。ただし入力項目・必須条件・バリデーション・条件保持方式は SCR-003 §16 Open Issue。
- **Provenance / Canonical Source Condition**: Button variant GOV-0002 は provenance 未確認。
- **Placeholder / Inspection Pending Condition**: Input 状態一式 follow-up #2 実査待ち・error は暫定 placeholder。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応関係の明文化余地であり、入力項目・バリデーションの確定ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 入力項目・バリデーション・条件保持が上流 Open Issue、Input 状態が follow-up #2 実査待ちであることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 入力仕様の上流未定義・実査待ち・provenance 未確認・承認/解決主体の未定義。
- **What Cannot Start**: 入力状態表現対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: 入力項目・バリデーション・Input 状態の追加を承認しない。
- **Does Not Decide**: 入力項目・必須条件・バリデーション・履歴保持は決めない。
- **Downstream Impact**: Implementation の検索/入力実装 (Repository 管理対象外)。

### 9.10 表示責務 (候補/価格/評価) と DS component (Card/PriceTag/ReviewStars) の対応の明文化

- **Candidate Aspect**: 宿泊施設候補・価格と条件・評価を UI として表現する責務と DS component の対応関係の明文化余地。
- **Source Topic**: C-03・C-04・C-05 (関連 T-05)。
- **Design Responsibility**: 候補提示・価格条件提示・評価表現の責務と DS component の対応。
- **Related Service Design ID**: IA-OBJ-003・IA-OBJ-007・IA-OBJ-009・CTA-005・SDP-003・CTP-003。
- **Related SCR**: SCR-002・SCR-004・SCR-005・SCR-014。
- **Related Unresolved Dependency**: 「表示仕様の上流未定義 (表示項目/順/比較基準/料金構造/Review 提供元)」「placeholder/実査待ち (Card 実 px・8 スロット・星実寸・「円」weight・radius.card/shadow)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: IA-OBJ-003/007/009・CTA-005・SDP-003 は上流に実在。ただし表示項目・表示順・比較成立基準・料金構造・Review 提供元は SCR-004/SCR-005 §16・IA §11 Open Issue。
- **Provenance / Canonical Source Condition**: 該当なし。
- **Placeholder / Inspection Pending Condition**: Card 実 px・8 スロット対応付け・星実寸・「円」weight が実査待ち、radius.card/shadow が placeholder。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応関係の明文化余地であり、表示項目・実測値の確定・slot/token の変更ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: 表示仕様が上流 Open Issue、Card 実 px/8 スロット・星実寸・「円」weight が実査待ち、radius.card/shadow が placeholder であることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 表示仕様の上流未定義・実査待ち・placeholder・承認/解決主体の未定義。
- **What Cannot Start**: 表示責務対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: 表示項目・token 値・Card 採用の確定を承認しない。
- **Does Not Decide**: 一覧/詳細 UI・表示項目・token 値は決めない。IA Object を Component と同一視しない。Downstream Impact の例を採用決定と解釈しない。
- **Downstream Impact**: Implementation の表示 (Repository 管理対象外)。

### 9.11 タイポグラフィ具体規格と CTP-008 責務の対応の明文化

- **Candidate Aspect**: タイポグラフィの具体規格・文字数制限と CTP-008 責務の対応関係の明文化余地。
- **Source Topic**: T-03。
- **Design Responsibility**: 可読性・スキャン容易性 (CTP-008) を支えるタイポグラフィスケールと具体規格の対応。
- **Related Service Design ID**: CTP-008。
- **Related SCR**: — (WO2 横断責務)。
- **Related Unresolved Dependency**: 「表示仕様の上流未定義 (タイポグラフィ具体仕様の確定主体・CTP-008 Does Not Decide)」(WO5 §14・§16)。
- **Upstream Definition Evidence**: CTP-008 は SD-004 に実在。design.md §3 タイポグラフィスケール・primitive `typography.size.*` は存在するが、文字数制限・具体規格は CTP-008 Does Not Decide。
- **Provenance / Canonical Source Condition**: 該当なし。
- **Placeholder / Inspection Pending Condition**: 該当なし。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応関係の明文化余地であり、具体値の確定ではない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: タイポグラフィ具体仕様が CTP-008 Does Not Decide として上流で決めない範囲であり、確定主体が未定義であることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 上流 Does Not Decide・確定主体未定義・承認/解決主体の未定義。
- **What Cannot Start**: タイポグラフィ具体規格対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: タイポグラフィ仕様・token 値の確定を承認しない。
- **Does Not Decide**: タイポグラフィ仕様・token 値は決めない。
- **Downstream Impact**: Implementation のタイポグラフィ適用 (Repository 管理対象外)。

### 9.12 支援領域の表現責務と DS 対応の明文化 (限定的)

- **Candidate Aspect**: 支援 (FAQ/問い合わせ/Support)・Policy 本文 (CTP-003/006/010) を UI として表現する責務と DS 対応の関係の明文化余地。
- **Source Topic**: C-09。
- **Design Responsibility**: 支援領域の表現責務と DS 対応。
- **Related Service Design ID**: CTP-003・CTP-006・CTP-010。
- **Related SCR**: SCR-013。
- **Related Unresolved Dependency**: 「可逆/回復の上流未定義 (サポート範囲・FAQ 構成)」「文言・命名の正本不在 (brand-content 参照切れ)」「未着手 component」(WO5 §14・§16)。
- **Upstream Definition Evidence**: CTP-003/006/010 の支援・Policy 表現責務は SD-004 に実在。ただしサポート対象範囲・FAQ 構成・問い合わせ手段は SCR-013 §16 Open Issue。
- **Provenance / Canonical Source Condition**: 文言正本 `brand-content.md` は参照切れ。
- **Placeholder / Inspection Pending Condition**: 該当なし (Accordion 等は未着手 = 成果物不在)。
- **Approval / Resolution Owner Evidence**: 承認・反映・解決主体は Repository 内で確認できない (§8.3)。
- **Scope Boundary**: 対応の明文化余地であり、未着手 component (Accordion 等) を必要 component・改訂候補へ変換しない。
- **Current Judgment**: `現時点では開始できない`。
- **Direct Basis**: サポート範囲・FAQ 構成が上流 Open Issue、`brand-content.md` が参照切れであることを直接確認でき、かつ承認・解決主体が未定義 (§8.3)。
- **Missing Evidence or Blocking Fact**: 上流 Open Issue の未解決・参照切れ・承認/解決主体の未定義。
- **What Cannot Start**: 支援領域対応を明文化する実際の改訂タスク。
- **Does Not Authorize**: Accordion/フォーム/チャット/モーダル等の追加を承認しない。
- **Does Not Decide**: 支援 component の採用・追加は決めない。未着手 component を改訂候補へ変換しない。
- **Downstream Impact**: Implementation の支援 UI (Repository 管理対象外)。

## 10. Overall Readiness Judgment

- **候補別判断の集計 (Fact)**: 上記 12 候補側面すべての Current Judgment は `現時点では開始できない` である。`開始できる` と判断された候補、`Repository 内の証拠だけでは判断できない` と判断された候補はない。これは件数の多寡による評価ではなく、各候補の Direct Basis に記録した個別の直接証拠に基づく。
- **総合判断 (Fact に基づく導出)**: 実際の Design System 改訂タスクは、現時点では開始できない。
- **共通の阻害 Fact**: 全候補に共通して、実際の改訂タスクの承認・反映・解決主体が Repository 内で定義されていない (§8.3。Governance README が命名規則・ADR・レビュー規則の正本未整備を明記し、owner-decisions.md は確認事項一覧であって承認主体の正本ではない)。この必要条件の欠落は、ユーザーや Claude Code を主体と推測せず、確認できない Fact として記録する。
- **候補固有の阻害 Fact**: 加えて各候補は、上流 Open Issue の未解決・provenance 未確認・placeholder/実査待ち・参照切れのいずれかを、Related Unresolved Dependency として明示的に伴う (§9 各 Direct Basis)。
- **限定的に開始可能な範囲**: 本 snapshot・入力の範囲では、承認/解決主体の未定義がすべての候補に共通して確認できるため、実際の Design System 改訂タスクを限定的にでも開始できる候補は確認できない。
- 本判断は結論を作業開始前に固定したものではなく、候補別の直接証拠から導出した。数値スコア・適合率・件数ランキング・pass/fail・severity・優先順位は使用しない。`Alignment approved`・`Alignment complete`・`Design System aligned` 等、Repository 内で定義・承認されていない完了表現は使用しない。
- `開始できる` と判断された候補は存在しないが、仮に将来存在しても、本 PR のマージとユーザーの明示的承認、別タスクなしに Design System の改定を開始してはならない。

## 11. Blocking Facts and Missing Evidence

- **承認・反映・解決主体の未定義 (全候補共通)**: Repository 内に実際の改訂タスクの承認・反映・解決主体を定義した成果物が確認できない (§8.3)。
- **上流 Open Issue の未解決**: Navigation 分類 (Global Nav・History and Recovery)・状態モデル業務定義・IA Object 業務モデル・入力/表示仕様・可逆/回復フロー・支援範囲が Service Design / Screen Requirement の Open Issue として未確定 (WO5 §14)。
- **provenance 未確認**: GOV-0002・TVL 群 (TVL-0007/0011/0012 等) の ADR 正本なし (WO5 §14)。着手可否の肯定的根拠に使用しない。
- **参照切れ**: `brand-content.md`・`governance/naming-rules.md`・ADR 正本が Repository 内に不在 (WO5 §14)。想定内容を根拠にしない。
- **placeholder / 実査待ち**: placeholder token 計 10・ボタン状態 follow-up #4・Input 状態 follow-up #2・Card 実 px/8 スロット・星実寸・「円」weight・画像 fallback が未取得 (WO5 §14)。値・実態の確認前に着手可否を肯定しない。

## 12. Downstream Impact

- **Assets** ([../assets/README.md](../assets/README.md)) — `Not started`。本評価の対象外。
- **Implementation** — Repository 管理対象外。本評価は静的な着手可否評価であり、実装検証・Design System の改定ではない。DS から実装画面・URL・route を導出しない。各 Screen Requirement の Downstream Impact に列挙された Component 例を採用決定と解釈しない。

## 13. Does Not Authorize / Does Not Decide

- 本文書は Design System の改定・候補の採用/却下・改定要否・改訂内容・解決策・優先順位/重要度/severity/対応順・工数/担当者/期限・変更対象 Component/token/値/UI を決定・承認しない。
- 新しい Design Decision・UX Decision・正式 ID・分類体系を追加しない。SCR-006〜SCR-012 の要求・API/DB/URL/route/画面遷移・Assets/Implementation 仕様を決めない。
- `現時点では開始できない` は、候補が不要・却下・無効という意味ではなく、本 snapshot での着手可否記録である。`開始できる` は、採用済み・改定必要・承認済みを意味しない。
- 未解決事項を調査・解決する作業が可能かどうかと、実際の Design System 改訂タスクを開始できるかを区別する。本タスクでは未解決事項を解決する Issue や branch を追加作成しない。
- 承認・反映・解決主体を推測しない (未定義の Fact として記録)。

## 14. Open Issues

以下は未決である。解決策は推測して記載しない。

- 実際の Design System 改訂タスクの承認・反映・解決主体の定義 (§8.3・§11)。
- §11 に列挙した上流 Open Issue・provenance 未確認・参照切れ・placeholder/実査待ちの解決主体。
- 各候補の未解決事項が解決された場合の着手可否の再評価方法 (再評価は本文書では行わない)。
- 正式な評価 ID・分類体系・ファイル名の確定 (本ファイル名 `alignment-amendment-readiness-assessment.md` は暫定)。

## 15. Relationship to Subsequent Work and Artifacts

- 本評価 (Work Order 6) は、Alignment Plan §10 Recommended Work Order の最終段である。Work Order 6 の完了は「着手可否評価を Draft として記録したこと」であり、改定開始・Alignment 承認・Alignment 完了ではない。
- Service Design (SD-001〜SD-007)・Screen Requirements (作成済み 7 個別 Screen Requirement)・既存 Design System 4 成果物は、入力評価文書を通じて追跡した対象であり、本評価はこれらを変更しない。
- 実際の Design System の改定・未解決事項の解決は、本 PR のマージとユーザーの明示的承認を経た、別タスクでのみ扱う。本文書はそれらの着手を承認しない。

## 16. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-17 | Initial readiness assessment (Work Order 6): Work Order 5 §13 の全 12 候補側面について、§14 未解決事項・§16 相互リンクと Repository 内の直接証拠を照合し着手可否を記録。全候補の Current Judgment は「現時点では開始できない」(共通阻害 = 承認・反映・解決主体の未定義、加えて各候補固有の上流 Open Issue・provenance 未確認・placeholder/実査待ち・参照切れ)。総合判断として実際の Design System 改訂タスクは現時点では開始できない。候補の採用/却下・改定要否・優先順位・改訂内容は未決定。Design System 本体は未変更 | Draft |
