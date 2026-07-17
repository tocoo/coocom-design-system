# 国内宿泊 (travel)

- サービス名: 国内宿泊
- 暫定サービス識別子: `travel`
- 注記: このディレクトリ名 (`travel`) は**暫定の識別子**である。正式なサービス識別子は未決 (他の表記例として `tvl` 等が確認されている)。確定まで既存識別子で運用する。確定した識別子として扱わないこと。詳細は [governance/owner-decisions.md](../../governance/owner-decisions.md) 確認事項 #8 を参照。

このディレクトリは、国内宿泊サービスの設計資産の入口である。

## レイヤーの責務とリンク

| レイヤー | 責務 | リンク | 状態 |
| --- | --- | --- | --- |
| Service Design | サービスの設計意図・方針 | [service-design/](service-design/README.md) | Draft (SD-001〜SD-007) |
| Screen Requirements | 画面要件 | [screen-requirements/](screen-requirements/README.md) | In preparation (SCR-001〜SCR-005・SCR-013・SCR-014 個別要件は Draft / SCR-006〜SCR-012 は Not started) |
| Design System | 視覚・トークン・コンポーネント定義 | [design-system/](design-system/README.md) | 既存資産 (Draft)・上流との Alignment は Work Order 1〜5 を Draft で実施済み (Work Order 6・改定は未着手) |
| Assets | 設計に付随する資産 | [assets/](assets/README.md) | Not started |

横断の共通規約は [governance/](../../governance/README.md) を参照。

## 推奨参照順序

1. 本 README
2. Service Design → Screen Requirements → Design System → Assets

Design System 内の推奨読み順は [design-system/README.md](design-system/README.md) を正本として参照する。

## 現在存在する成果物

- **Service Design** — SD-001〜SD-007 が Draft として存在する。入口: [service-design/README.md](service-design/README.md)
  - [principles.md](service-design/principles.md) (SD-001) / [information-architecture.md](service-design/information-architecture.md) (SD-002) / [navigation.md](service-design/navigation.md) (SD-003) / [content-principles.md](service-design/content-principles.md) (SD-004) / [cta-principles.md](service-design/cta-principles.md) (SD-005) / [screen-matrix.md](service-design/screen-matrix.md) (SD-006) / [ux-decision-records.md](service-design/ux-decision-records.md) (SD-007)
- **Screen Requirements** — 入口・共通管理構造を定義済 (`In preparation`)。着手可能候補の個別 Screen Requirement が Draft として存在する。入口: [screen-requirements/README.md](screen-requirements/README.md)
  - 入口 README (`In preparation`) / [creation-plan.md](screen-requirements/creation-plan.md) (SCR-001〜SCR-014 の作成単位・着手可否・作成順序の評価, `Draft`)
  - 個別 Screen Requirement (`Draft`): SCR-001 [service-entry.md](screen-requirements/service-entry.md) / SCR-002 [destination-discovery.md](screen-requirements/destination-discovery.md) / SCR-003 [accommodation-search.md](screen-requirements/accommodation-search.md) / SCR-004 [search-results.md](screen-requirements/search-results.md) / SCR-005 [accommodation-detail.md](screen-requirements/accommodation-detail.md) / SCR-013 [help-and-support.md](screen-requirements/help-and-support.md) / SCR-014 [editorial-content.md](screen-requirements/editorial-content.md)
  - 参照順序は [screen-requirements/README.md](screen-requirements/README.md) §13 Reference Order を正本とする (本 README では別の作成順を定義しない)。
- **Design System (既存資産)** — レイヤー入口 README (`Draft`)・Alignment Assessment 計画 (`Draft`)・Baseline Assessment (`Draft`)・Service Design 横断整合性評価 (`Draft`)・Screen Requirements 整合性評価 (`Draft`)・Observation 横断集約 (`Draft`)・改訂候補と未解決事項の分離 (`Draft`) を整備。既存資産のトークン現行版: primitive 0.3.0-draft / semantic 0.3.0-draft (Draft、各 JSON の `$meta.version` 準拠)。Alignment は Work Order 1 (Baseline 確認)・Work Order 2 (Service Design 横断原則との整合性評価)・Work Order 3 (作成済み 7 個別 Screen Requirement ごとの整合性評価)・Work Order 4 (Work Order 2・3 の Observation の横断集約)・Work Order 5 (改訂候補と未解決事項の分離) まで Draft で実施済み。Work Order 5 は改訂候補と未解決事項の分離であり、改定要否決定・改訂内容確定・改訂着手可能・改定完了ではない。実際の改訂タスクを開始できるかの判断 (Work Order 6 = 改訂着手可否の判断) および Design System の改定は未着手。入口: [design-system/README.md](design-system/README.md)
  - [design-system/README.md](design-system/README.md) (レイヤー入口・既存資産の管理構造・上流下流関係, `Draft`)
  - [design-system/alignment-plan.md](design-system/alignment-plan.md) (Alignment Assessment の評価方法・記録構造・推奨順の計画, `Draft`)
  - [design-system/baseline-assessment.md](design-system/baseline-assessment.md) (既存 4 資産の Baseline Assessment: 内部整合性・provenance・placeholder の read-only 確認結果, `Draft`)
  - [design-system/service-design-alignment-assessment.md](design-system/service-design-alignment-assessment.md) (Service Design 横断原則と既存 Design System の整合性評価: Work Order 2 の結果, `Draft`)
  - [design-system/screen-requirements-alignment-assessment.md](design-system/screen-requirements-alignment-assessment.md) (作成済み 7 個別 Screen Requirement ごとの整合性評価: Work Order 3 の結果, `Draft`)
  - [design-system/alignment-observations-aggregation.md](design-system/alignment-observations-aggregation.md) (Work Order 2・3 の Observation の横断集約: Work Order 4 の結果, `Draft`)
  - [design-system/alignment-amendment-candidate-separation.md](design-system/alignment-amendment-candidate-separation.md) (集約 Observation の改訂候補と未解決事項の分離: Work Order 5 の結果, `Draft`)
  - [design-system/design.md](design-system/design.md)
  - [design-system/semantic.travel.json](design-system/semantic.travel.json)
  - [design-system/primitive.travel.json](design-system/primitive.travel.json)
  - [design-system/components.md](design-system/components.md)

Design System の既存資産 (`design.md`・JSON・`components.md`) は本 bootstrap 以前から存在し、内容は変更していない (移行に伴う参照パス修正を除く)。入口 README (`Draft`) は既存資産と上流成果物の関係を管理する基盤であり、既存資産の内容・version・Status を変更しない。上流との Alignment 評価は Work Order 1〜5 (Baseline 確認・Service Design 横断整合性評価・Screen Requirements 個別整合性評価・Observation 横断集約・改訂候補と未解決事項の分離) を Draft で実施済みである。次段の Work Order 6 で改訂着手可否を判断し、実際の Design System の改定はその後の承認された別タスクでのみ扱う (Work Order 6 の判断前に改定を既定路線としない)。

## 現在存在しない成果物

- Screen Requirements 個別文書 (SCR-006〜SCR-012): 未作成 (`Not started`)。レイヤー入口は `In preparation`。
- Assets: 未着手 (`Status: Not started`)

未着手・未定義の領域について、要求・仕様を推測して記載しないこと。
