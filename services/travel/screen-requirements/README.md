# Travel Screen Requirements

- Status: In preparation
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Screen Requirements レイヤーの入口・共通管理構造
- Position in Repository: `services/travel/screen-requirements/README.md` — Screen Requirements レイヤー (travel サービス配下)。サービス入口は [../README.md](../README.md)。参照する上流成果物 (Service Design, SD-001〜SD-007) は [../service-design/principles.md](../service-design/principles.md) / [../service-design/information-architecture.md](../service-design/information-architecture.md) / [../service-design/navigation.md](../service-design/navigation.md) / [../service-design/content-principles.md](../service-design/content-principles.md) / [../service-design/cta-principles.md](../service-design/cta-principles.md) / [../service-design/screen-matrix.md](../service-design/screen-matrix.md) / [../service-design/ux-decision-records.md](../service-design/ux-decision-records.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Design System / Implementation) との関係は §10 を参照。

本 README は Screen Requirements レイヤーの入口文書であり、個別の画面要件そのものは定義しない。個別 Screen Requirement を作成する前提となる、共通の管理構造・対応方法・Open Issue 管理を定義する。

## 1. Purpose

- Screen Requirements レイヤーの目的・責務と、個別 Screen Requirement 文書の共通構造を定義する。
- 上流 Service Design 成果物 (SD-001〜SD-007) と Screen Requirement 文書の対応方法、および Screen Matrix の画面候補 (SCR-001〜SCR-014) との追跡可能性を定義する。
- 「対応方法を定義する」ことと「実際の分割・統合・個別要件を決定する」ことを区別する。後者は本文書では確定しない。

## 2. Scope

### Managed

- Screen Requirements レイヤーの目的・責務・管理対象。
- 個別 Screen Requirement 文書の共通構造。
- Screen Matrix 画面候補との対応・分割・統合の管理方法 (対応方法の定義のみ)。
- Screen Requirement ID と Screen Matrix の SCR ID の区別。
- Status の扱い。
- 上流 Service Design 成果物の参照方法。
- 下流 Design System との関係。
- 未定義要求を Open Issue として保持する方法。
- 個別 Screen Requirement を作成する順序の決定基準。

### Not Managed

- 14 画面候補の個別 Screen Requirement 作成。
- 画面候補の追加・削除・名称変更・分割・統合の確定。
- 実装画面数・URL・ルート・サイトマップ・画面遷移。
- UI・レイアウト・ワイヤーフレーム・Component 仕様。
- 入力項目・バリデーション・API・DB・状態遷移。
- 予約・決済・認証・会員・変更・取消等の業務仕様。
- Service Design / Design System / Governance の内容変更。
- Repository 内に存在しない方針名・略称・Decision・正式採番の創作。

## 3. Preconditions

### Facts

- 上流の Service Design 成果物 SD-001〜SD-007 が Draft として存在する ([../service-design/README.md](../service-design/README.md))。
- Screen Matrix ([../service-design/screen-matrix.md](../service-design/screen-matrix.md)) は 14 画面候補 (SCR-001〜SCR-014) を Draft として管理する。
- 個別 Screen Requirement 文書は現時点で未作成である。
- 正式な画面一覧・URL・画面遷移・業務仕様は未定義である。
- Design System は既存資産として存在する ([../design-system/](../design-system/))。

### Decisions

- 本レイヤーの入口・共通管理構造を定義する (個別要件は作成しない)。
- Screen Matrix の画面候補と Screen Requirement 文書を 1 対 1 で前提としない。
- 未定義事項を推測で補完せず Open Issue として保持する ([../service-design/ux-decision-records.md](../service-design/ux-decision-records.md) UXDR-TRAVEL-001 と一致)。

### Hypotheses

- なし。

### Open Issues

- Screen Requirement ID 体系の正式採用。
- 個別文書の作成単位・作成順。
- 各画面候補の分割・統合。
- （詳細は §17 に集約）

## 4. Information Classification

本レイヤーおよび個別 Screen Requirement 文書では、情報を以下に区別する。混同しない。

- **Fact** — 確認済みの事実。
- **Decision** — 採用する設計判断。
- **Hypothesis** — 検証が必要な仮説。
- **Open Issue** — 未決事項。

未定義の業務・機能・画面仕様を Fact または Decision として扱わない。根拠が確認できない場合は Open Issue とする。

## 5. Screen Requirement Unit

- Screen Requirement 文書の単位は、Screen Matrix の画面候補 (SCR) を出発点とするが、SCR と 1 対 1 に固定しない。
- 1 つの Screen Requirement 文書は、利用者タスクと情報責務を基準に、1 つ以上の画面候補に対応し得る。
- 作成単位 (どの範囲を 1 文書とするか) は未決であり、Open Issue として保持する。
- 正式な画面構成・業務要求が不足している場合、作成単位を確定しない。

## 6. Common Document Structure

将来作成する個別 Screen Requirement 文書は、最低限以下の構造を持つ。各節の**責務のみ**を定義し、本文書では具体的な要件を記入しない。未定義の要件は空想で埋めず Open Issue として扱う。

- **Title** — 文書の対象を示す表題。
- **Status** — 個別文書の状態 (初期は `Draft`)。
- **Scope** — 対象範囲。
- **Position in Repository** — Repository 上の位置と上流・下流の参照。
- **Purpose** — 文書の目的。
- **Related Screen Matrix Candidates** — 対応する Screen Matrix の SCR ID (1 つ以上)。
- **Preconditions** — Facts / Decisions / Hypotheses / Open Issues。
- **User Tasks** — 対象の利用者タスク (Screen Matrix の Primary User Tasks を上流参照)。
- **Information Responsibilities** — 扱う情報オブジェクト (Information Architecture を上流参照)。
- **Functional Requirements** — 機能要件。**業務仕様が未定義の場合は記入せず Open Issue とする。**
- **Content Requirements** — 情報表現の要件 (Content Principles を上流参照)。
- **Navigation Requirements** — 現在地・移動・文脈保持の要件 (Navigation を上流参照)。
- **CTA Requirements** — 行動・確約・状態の要件 (CTA Principles を上流参照)。
- **State and Feedback Requirements** — 状態・処理結果・エラーの要件。
- **Accessibility Requirements** — アクセシビリティ要件 (視覚のみに依存しない等)。
- **Constraints** — 制約。
- **Does Not Decide** — この文書だけでは確定しない事項。
- **Upstream References** — 参照した上流成果物 (SD-001〜SD-007)。
- **Downstream Impact** — Design System・実装への影響 (下流)。
- **Open Issues** — 未解決事項。
- **Acceptance Criteria** — 受入基準。確定主体が未定義の場合は Open Issue とする。
- **Change Log** — 変更履歴。

`Functional Requirements` 等に必要な業務仕様が未定義の場合、推測で補完せず Open Issue として明示する。

## 7. ID and Status Model

### ID

- `SCR-001`〜`SCR-014` は [Screen Matrix](../service-design/screen-matrix.md) 上の**画面候補 ID** であり、Screen Requirement 文書 ID と自動的に同一視しない。
- 新しい Screen Requirement ID 体系の正式採用は本文書では確定しない。
- 管理上 ID 例が必要な場合も、正式採番ではなく placeholder であることを明示する (例として用いる `SR-xxx` 等は暫定であり確定した採番ではない)。
- ID 体系そのものが未決であるため Open Issue として保持する (§17)。
- SCR ID を URL・route・実装画面 ID として使用しない。

### Status

- 本レイヤー入口 README の Status は `In preparation`。
- 個別 Screen Requirement は未作成のため `Not started`。
- 将来作成する個別成果物の初期 Status は `Draft`。
- Screen Matrix の画面候補 Status と Screen Requirement 文書 Status を混同しない。

## 8. Relationship with Screen Matrix

Screen Matrix ([../service-design/screen-matrix.md](../service-design/screen-matrix.md)) の画面候補と Screen Requirement 文書は **1 対 1 を前提としない**。具体的な分割・統合対象は本文書では確定しない。

### One Candidate to Multiple Requirements

- 1 つの画面候補が複数の Screen Requirement 文書へ分割される場合がある。
- 各 Screen Requirement は、対応する同一の SCR ID を参照できる。
- 分割の理由・根拠・未決事項を記録する。

### Multiple Candidates to One Requirement

- 複数の画面候補が 1 つの Screen Requirement 文書へ統合される場合がある。
- 統合する場合、関連するすべての SCR ID を列挙する。
- 統合の理由・根拠・未決事項を記録する。

### Traceability Rules

- 分割・統合後も、元の画面候補との追跡可能性を失わせない。
- 各 Screen Requirement は `Related Screen Matrix Candidates` に対応 SCR ID を明示する。
- 正式な画面構成や業務要求が不足している場合、分割・統合を確定せず Open Issue とする。
- SCR ID を URL・route・実装画面 ID として使用しない。

## 9. Relationship with Upstream Artifacts

Screen Requirements の上流成果物は、README の Reference Order 上で先行する Service Design 成果物 (SD-001〜SD-007) とする。各成果物の定義を Screen Requirements 側で変更・再定義しない。

- **SD-001 [Service Design Principles](../service-design/principles.md)** — 要件判断の上位基準。
- **SD-002 [Information Architecture](../service-design/information-architecture.md)** — 扱う情報オブジェクトと概念関係。
- **SD-003 [Navigation](../service-design/navigation.md)** — 現在地・移動・文脈保持・回復の基準。
- **SD-004 [Content Principles](../service-design/content-principles.md)** — 情報表現・状態・不確実性の基準。
- **SD-005 [CTA Principles](../service-design/cta-principles.md)** — 行動・確約・状態・優先順位の基準。
- **SD-006 [Screen Matrix](../service-design/screen-matrix.md)** — 対象となる画面候補と責務。
- **SD-007 [UX Decision Records](../service-design/ux-decision-records.md)** — Accepted な UX 判断の制約。

## 10. Relationship with Downstream Artifacts

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Design System** ([../design-system/](../design-system/)) — Screen Requirements の下流に位置する。既存 Design System を参照して現状を確認できるが、既存 Design System の記述を上流要求へ昇格させない。関係は下流関係として扱う。
- **Implementation** — Repository の管理対象外。Screen Requirement だけで実装仕様を確定しない。

## 11. Open Issue Handling

- 未定義の事業要求・業務仕様・画面仕様は、推測で補完せず Open Issue として保持する。
- 各 Screen Requirement 文書の `Open Issues` 節、および本 README の §17 に集約する。
- Open Issue が解決されるまで、それに依存する要件・分割・統合・作成順を確定しない。
- 既存文書にない回答を推測して付与しない。

## 12. Creation Order

14 画面候補の作成順を現時点では確定しない。順序決定時に確認する基準のみを定義する。

- 上流成果物の定義充足度。
- 未定義の事業要求・業務仕様への依存度。
- 他候補との依存関係。
- 分割・統合の未決度。
- 利用者タスク上の位置。
- 下流設計へ与える影響。
- Open Issue の数と重大性。

現時点で確実に順序を決められないため、作成順そのものを Open Issue とする。`SCR-001` から機械的に作成するとは決めない。

## 13. Reference Order

Screen Requirements レイヤーの推奨参照順序は以下とする。未作成の成果物にはリンクを作成しない。

1. 本 README (レイヤー入口・共通管理構造)
2. [creation-plan.md](creation-plan.md) (SCR-001〜SCR-014 の作成単位・着手可否・作成順序の評価, Draft)
3. [service-entry.md](service-entry.md) (SCR-001 Service Entry の個別 Screen Requirement, Draft)
4. [help-and-support.md](help-and-support.md) (SCR-013 Help and Support の個別 Screen Requirement, Draft)
5. [editorial-content.md](editorial-content.md) (SCR-014 Editorial Content の個別 Screen Requirement, Draft)
6. [accommodation-search.md](accommodation-search.md) (SCR-003 Accommodation Search の個別 Screen Requirement, Draft)
7. [search-results.md](search-results.md) (SCR-004 Search Results の個別 Screen Requirement, Draft)
8. その他の個別 Screen Requirement 文書 (SCR-002, SCR-005〜SCR-012) — 未作成 (`Not started`)

個別 Screen Requirement (上記 3・4・5・6・7) の並びは参照上の配置であり、正式な個別要件の作成順を意味しない。作成順の評価と未決事項は [creation-plan.md](creation-plan.md) §10・§15 を参照する。

上流 Service Design 成果物 (SD-001〜SD-007) は本 README の Position ヘッダーおよび §9 を参照する。

## 14. Planned Artifacts

- SCR-001 Service Entry ([service-entry.md](service-entry.md))、SCR-003 Accommodation Search ([accommodation-search.md](accommodation-search.md))、SCR-004 Search Results ([search-results.md](search-results.md))、SCR-013 Help and Support ([help-and-support.md](help-and-support.md))、SCR-014 Editorial Content ([editorial-content.md](editorial-content.md)) の個別 Screen Requirement が Draft として存在する。その他の画面候補 (SCR-002, SCR-005〜SCR-012) の個別 Screen Requirement は未作成 (`Not started`)。
- 作成単位・件数・ファイル命名規則・作成順はいずれも未決 (Open Issue)。したがって残りの個別 Screen Requirement の Planned Artifact 一覧は現時点では確定しない。
- 対象となり得る画面候補は Screen Matrix の SCR-001〜SCR-014 だが、Screen Requirement 文書として 1 対 1 に確定したものではない。

| Artifact | Responsibility | Status |
| --- | --- | --- |
| [creation-plan.md](creation-plan.md) | SCR-001〜SCR-014 の作成単位・着手可否・作成順序の評価 | Draft |
| [service-entry.md](service-entry.md) | SCR-001 Service Entry の個別 Screen Requirement | Draft |
| [accommodation-search.md](accommodation-search.md) | SCR-003 Accommodation Search の個別 Screen Requirement | Draft |
| [search-results.md](search-results.md) | SCR-004 Search Results の個別 Screen Requirement | Draft |
| [help-and-support.md](help-and-support.md) | SCR-013 Help and Support の個別 Screen Requirement | Draft |
| [editorial-content.md](editorial-content.md) | SCR-014 Editorial Content の個別 Screen Requirement | Draft |
| 個別 Screen Requirement 文書 (SCR-002, SCR-005〜SCR-012) | 各画面候補の要件 | Not started (未作成) |

## 15. Current Status

- 本レイヤー入口 README が `In preparation` として存在する。
- SCR-001〜SCR-014 の作成順序評価 ([creation-plan.md](creation-plan.md)) が `Draft` として存在する。
- SCR-001 Service Entry の個別 Screen Requirement ([service-entry.md](service-entry.md)) が `Draft` として存在する。
- SCR-003 Accommodation Search の個別 Screen Requirement ([accommodation-search.md](accommodation-search.md)) が `Draft` として存在する。
- SCR-004 Search Results の個別 Screen Requirement ([search-results.md](search-results.md)) が `Draft` として存在する。
- SCR-013 Help and Support の個別 Screen Requirement ([help-and-support.md](help-and-support.md)) が `Draft` として存在する。
- SCR-014 Editorial Content の個別 Screen Requirement ([editorial-content.md](editorial-content.md)) が `Draft` として存在する。
- その他の画面候補 (SCR-002, SCR-004〜SCR-012) の個別 Screen Requirement は未作成 (`Not started`)。
- 上流 Service Design 成果物 SD-001〜SD-007 が Draft として存在する。
- 下流 Design System は既存資産として存在する。
- 上位の事業・業務・画面仕様の多くは未定義であり、Open Issue として保持する。

## 16. Quality Criteria

今後作成する個別 Screen Requirement 文書には、以下を適用する。

- 単独で読んでも理解できる。
- 責務が明確で、他文書との重複がない。
- Fact / Decision / Hypothesis / Open Issue が区別されている。
- 対応する SCR ID への追跡可能性がある。
- 上流成果物 (SD-001〜SD-007) の定義を再定義せず参照する。
- 未定義事項を推測で補完せず Open Issue として扱う。
- アクセシビリティを後工程限定にしない。
- 下流 (Design System・実装) への影響を Downstream Impact として分離する。

## 17. Open Issues

以下は未決である。解決策は推測して記載しない。作成順序評価に関する未決事項は [creation-plan.md](creation-plan.md) §15 に整理する (本 README の未決事項を削除・確定しない)。

- Screen Requirement ID 体系の正式採用。
- 個別文書のファイル命名規則。
- 14 画面候補の正式承認。
- 各候補の分割・統合。
- Screen Requirement 文書の作成単位。
- 個別要件の作成順。
- Acceptance Criteria の確定主体。
- Review・承認フロー。
- 業務要求・機能要求の提供元。
- URL・ルート・サイトマップとの対応。
- Design System への反映確認方法。
- Screen Matrix の進捗更新方法。
- Requirement 変更時の上流・下流影響確認方法。

## 18. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Define Screen Requirements foundation (entry README and common management structure) | In preparation |
| 2026-07-15 | Add Reference Order and creation-plan.md (Draft) to Planned Artifacts and Current Status | In preparation |
| 2026-07-15 | Add service-entry.md (SCR-001, Draft) to Reference Order, Planned Artifacts, and Current Status | In preparation |
| 2026-07-15 | Add help-and-support.md (SCR-013, Draft) to Reference Order, Planned Artifacts, and Current Status | In preparation |
| 2026-07-16 | Add editorial-content.md (SCR-014, Draft) to Reference Order, Planned Artifacts, and Current Status | In preparation |
| 2026-07-16 | Add accommodation-search.md (SCR-003, Draft) to Reference Order, Planned Artifacts, and Current Status | In preparation |
| 2026-07-16 | Add search-results.md (SCR-004, Draft) to Reference Order, Planned Artifacts, and Current Status | In preparation |
