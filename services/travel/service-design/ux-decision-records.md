# Travel UX Decision Records

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の UX 設計判断を記録する UX Decision Records の初版 Draft
- Position in Repository: `services/travel/service-design/ux-decision-records.md` — Service Design レイヤー (travel サービス配下、SD-007)。入口は [README.md](README.md)。参照する上流成果物 (SD-001〜SD-006) は [principles.md](principles.md) / [information-architecture.md](information-architecture.md) / [navigation.md](navigation.md) / [content-principles.md](content-principles.md) / [cta-principles.md](cta-principles.md) / [screen-matrix.md](screen-matrix.md)。横断共通は [Governance](../../../governance/README.md)。下流成果物 (Screen Requirements / Design System / Implementation) との関係は §10 を参照。

## 1. Purpose

本文書は、国内宿泊サービスにおける UX 設計判断とその根拠・影響・状態を継続的に記録する Draft 正本である。

- UX 判断を、後から根拠を追跡でき、下流成果物へ一貫して伝達できる形で残す。
- 本タスクは個別の UX 判断を大量に確定するものではなく、記録の運用ルールと初期 Record を定義する。
- 上流成果物 (SD-001〜SD-006) の定義は変更しない。

## 2. Preconditions

### Facts

- SD-001〜SD-006 が Draft として存在する ([principles.md](principles.md) / [information-architecture.md](information-architecture.md) / [navigation.md](navigation.md) / [content-principles.md](content-principles.md) / [cta-principles.md](cta-principles.md) / [screen-matrix.md](screen-matrix.md))。
- UX Decision Records は本タスク以前には未作成だった。
- Screen Requirements は未作成である。
- 正式な承認者・承認フローは未定義である。

### Decisions

- UX Decision Records を SD-007 として管理する。
- 6 つの Status を使用する。
- 3 件の初期 Record を登録する。
- 過去 Record を削除せず履歴として保持する。
- 未定義事項を推測で補完しない。

### Hypothesis

- なし。

### Open Issues

- Decision Owner。
- 承認フロー。
- Record 追加条件。
- ID の正式採用。
- GitHub Issue・PR との連携。
- 下流成果物への反映確認方法。

## 3. What to Record

以下に該当する UX 判断を記録対象とする。

- 複数成果物へ影響する判断
- 後から理由を追跡する必要がある判断
- 複数案の比較を経た判断
- 利用者体験上の重要なトレードオフ
- Screen Requirements または Design System へ制約を与える判断
- 将来見直す可能性がある判断
- 上流成果物間の適用解釈を確定する判断

## 4. What Not to Record

以下は原則として記録しない。

- 軽微な文言修正
- 単純な誤字修正
- 文書内整合性だけの修正
- 既存原則をそのまま適用しただけの判断
- 技術実装だけに閉じた判断
- Issue や PR の作業履歴
- 未検討の案
- 根拠のない仮説
- すでに上流成果物で明確に決定済みの内容の重複記録

文書内整合性修正を UX Decision として登録しない。

## 5. Record Structure

各 Record を以下の構造で記述する。

```text
## UXDR-TRAVEL-XXX: Decision Title

### Status
Proposed / Accepted / Deferred / Superseded / Rejected / Deprecated

### Date
YYYY-MM-DD

### Decision Owner
未確定の場合は `Open Issue` とする。

### Context
判断が必要になった背景。

### Decision
採用または提案する判断。

### Rationale
判断理由。

### Alternatives Considered
検討した代替案。存在しない場合は、その理由を記載する。

### Consequences
利用者体験、運用、設計への影響。

### Related Upstream Artifacts
判断根拠となる SD-001〜SD-006。

### Downstream Impact
Screen Requirements、Design System、実装等への影響。

### Evidence Classification
Fact / Decision / Hypothesis / Open Issue。

### Open Issues
未解決事項。

### Supersedes
置き換える Record。なければ `None`。

### Superseded By
置き換えられた Record。なければ `None`。
```

`UXDR-TRAVEL` は管理用の暫定識別子であり、正式な恒久採番として確定したものではない。Hypothesis だけを根拠とする場合は Status を `Proposed` または `Deferred` とし、`Accepted` にしない。

## 6. Status Model

個別 Record の Status と、文書全体の Status (`Draft`) を混同しない。

| Status | Meaning |
| --- | --- |
| Proposed | 判断案として記録され、未採用 |
| Accepted | 現時点の正式な設計判断として採用 |
| Deferred | 情報不足や依存関係により判断を保留 |
| Superseded | 後続の Decision により置き換えられた |
| Rejected | 検討したが採用しなかった |
| Deprecated | 現在は使用しないが履歴として保持 |

## 7. Decision Lifecycle

1. 判断が必要な論点を特定する。
2. 関連する Fact、Decision、Hypothesis、Open Issue を整理する。
3. 必要に応じて複数案を比較する。
4. Proposed として Record を作成する。
5. 権限を持つ Decision Owner が判断する。
6. Accepted、Deferred、Rejected 等へ更新する。
7. 下流成果物へ影響を反映する。
8. 後続判断で置き換える場合は Superseded 関係を双方向に記録する。
9. 過去 Record を削除せず履歴として保持する。

承認者・承認フローは本タスクで確定しない。

## 8. Decision Records

## UXDR-TRAVEL-001: Preserve Unknowns Instead of Inventing Requirements

### Status

Accepted

### Date

2026-07-15

### Decision Owner

Open Issue

### Context

国内宿泊サービスの上位事業要求・業務仕様・画面要件の多くが未定義のまま Service Design を進めている。未定義事項の扱いを設計判断として明文化する必要がある。

### Decision

上位事業要求・業務仕様・画面要件が未定義の場合、推測で補完せず、Open Issue として維持する。

### Rationale

- Repository 全体の unknown-first 方針と一致する。
- 誤った前提が下流設計へ伝播することを防ぐ。
- 後から判断根拠を追跡可能にする。

### Alternatives Considered

- 未定義事項を暫定的な仮定で補完して設計を確定する案。既存の [principles.md](principles.md) (SDP-008 Evidence over Assumption / SDP-010 Incremental Definition) が未確認前提を事実として扱わない方針を示しているため、不採用。

### Consequences

- 下流成果物へ誤った前提が伝播しない。
- 未決事項が残り、確定には追加情報が必要となる。
- 判断根拠を追跡可能に保つ。

### Related Upstream Artifacts

- Service Design Principles
- Information Architecture
- Navigation
- Content Principles
- CTA Principles
- Screen Matrix

### Downstream Impact

- Screen Requirements / Design System は、未定義事項に依存する要件・仕様を確定せず、Open Issue を引き継ぐ。

### Evidence Classification

Decision

### Open Issues

- 本 Record の Decision Owner は未確定。

### Supersedes

None

### Superseded By

None

## UXDR-TRAVEL-002: Separate Conceptual Screen Candidates from Implemented Screens

### Status

Accepted

### Date

2026-07-15

### Decision Owner

Open Issue

### Context

[screen-matrix.md](screen-matrix.md) が 14 の画面候補を定義したが、正式な画面構成・URL・業務要件は未定義である。画面候補と実装画面の関係を明確にする必要がある。

### Decision

Screen Matrix の画面候補を、実装上の 1 画面・URL・ルートと同一視しない。

### Rationale

- Screen Matrix は責務と利用者タスクを管理する。
- 画面候補は分割・統合される可能性がある。
- 正式な画面構成と業務要件が未定義である。

### Alternatives Considered

- 画面候補を実装画面と 1 対 1 で固定する案。[screen-matrix.md](screen-matrix.md) の Screen Candidate Principles および Relationship with Screen Requirements が分割・統合の可能性を明記しているため、不採用。

### Consequences

- 画面候補は Screen Requirements 策定時に分割・統合され得る。
- 実装は画面候補を直接のルート定義として扱わない。

### Related Upstream Artifacts

- Information Architecture
- Navigation
- Content Principles
- CTA Principles
- Screen Matrix

### Downstream Impact

- Screen Requirements は画面候補を要件単位へ具体化する際、1 対 1 を前提としない。
- Design System は画面候補単位の固定 UI を前提としない。

### Evidence Classification

Decision

### Open Issues

- 画面候補の分割・統合の正式判断は未決。

### Supersedes

None

### Superseded By

None

## UXDR-TRAVEL-003: Keep Navigation and CTA as Separate Design Responsibilities

### Status

Accepted

### Date

2026-07-15

### Decision Owner

Open Issue

### Context

[navigation.md](navigation.md) と [cta-principles.md](cta-principles.md) は重なり得るが、移動と行動という異なる責務を持つ。両者の関係を明確にする必要がある。

### Decision

Navigation と CTA を、重なり得るが異なる設計責務として管理する。

- Navigation: 情報・領域・文脈間の移動。
- CTA: タスクや状態を前進・変更させる特定行動。

### Rationale

- すべてのリンクを CTA として強調することを防ぐ。
- 移動と確約を混同しない。
- Screen Requirements と Design System で異なる評価軸を持てる。

### Alternatives Considered

- すべての主要リンクを CTA として統一的に扱う案。[cta-principles.md](cta-principles.md) の Boundary between CTA and Navigation が両者を区別しているため、不採用。

### Consequences

- Screen Requirements / Design System は Navigation と CTA を別評価軸で扱う。
- 移動と確約を混同しない。

### Related Upstream Artifacts

- Navigation
- Content Principles
- CTA Principles
- Screen Matrix

### Downstream Impact

- Design System は Navigation 要素と CTA 要素 (Button / Link 等) を別 Pattern・評価軸で扱う。
- Screen Requirements は画面ごとに両者を区別して要件化する。

### Evidence Classification

Decision

### Open Issues

- Navigation Action を主要 CTA として扱う具体基準は未決 ([cta-principles.md](cta-principles.md) の Open Issues)。

### Supersedes

None

### Superseded By

None

## 9. Relationship with Upstream Artifacts

UX Decision Records 側で上流成果物の定義を変更しない。

- **Service Design Principles** — UX 判断の上位基準を提供する。
- **Information Architecture** — 判断対象となる情報オブジェクトと概念関係を提供する。
- **Navigation** — 移動・文脈保持・回復に関する判断基準を提供する。
- **Content Principles** — 情報表現・状態・不確実性に関する判断基準を提供する。
- **CTA Principles** — 行動・確約・状態・優先順位に関する判断基準を提供する。
- **Screen Matrix** — UX 判断が影響する画面候補と責務を特定する。

## 10. Relationship with Downstream Artifacts

下流成果物を Position ヘッダーの「上流成果物」に含めない。

- **Screen Requirements** — Accepted な UX Decision を、画面単位の要件・制約・受入基準へ反映する。
- **Design System** — Accepted な UX Decision を、Component、Pattern、State、Content 構造の設計判断へ反映する。
- **Implementation** — 必要に応じて実装上の制約として参照するが、UX Decision Record だけで実装仕様を確定しない。

## 11. Open Issues

以下は未決である。解決策は推測して記載しない。

- UXDR ID の正式採用。
- Status Model の正式承認。
- Decision Owner の定義。
- Proposed から Accepted への承認権限。
- Review・承認フロー。
- Record 作成の必須条件。
- GitHub Issue / PR / commit との関連付け。
- Superseded 管理方法。
- Screen Requirements への反映確認方法。
- Design System への反映確認方法。
- Decision 変更時の影響範囲確認方法。
- 他サービスとの共通 Decision Record の配置。
- Governance Decision との境界。
- 技術 ADR との境界。
- Record 数増加時の分割方法。
- UXDR-TRAVEL-001〜003 の Decision Owner。
- 初期 Record の正式承認。

## 12. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Initial draft of Travel UX Decision Records | Draft |
