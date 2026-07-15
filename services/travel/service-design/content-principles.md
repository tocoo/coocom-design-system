# Travel Content Principles

- Status: Draft
- Scope: 国内宿泊サービス (`travel`, 暫定識別子) の Content 設計原則の初版 Draft
- Position in Repository: `services/travel/service-design/content-principles.md` — Service Design レイヤー (travel サービス配下)。入口は [README.md](README.md)、上位原則は [principles.md](principles.md)、情報構造は [information-architecture.md](information-architecture.md)、Navigation は [navigation.md](navigation.md)、横断共通は [Governance](../../../governance/README.md) を参照。

## 1. Purpose

本文書は、国内宿泊サービスにおける Content 設計原則の Draft 正本を管理する。

- サービス内の情報を、利用者が理解・判断・行動できる形で表現するための共通原則を定義する。
- 後続成果物 (CTA Principles / Screen Matrix / Screen Requirements) および Design System のレビューに、共通の Content 基準を提供する。
- [Information Architecture](information-architecture.md) および [Navigation](navigation.md) の定義を変更せず、Content 表現上の基準として参照する。
- 具体的な文言・コピー・キャンペーン表現・ブランドトーンは確定しない。

## 2. Preconditions

### Facts

- [Service Design Principles](principles.md) は Draft として存在する。
- [Information Architecture](information-architecture.md) は Draft として存在する。
- [Navigation](navigation.md) は Draft として存在する。
- Content Principles は本タスク以前には未作成だった。
- ブランド・コンテンツ・マーケティング戦略は未定義である。

### Decisions

- 10 の Content Principles を初版 Draft の判断基準とする。
- 6 つの Content Category を初版 Draft として扱う。
- 具体的なコピーやブランド表現は定義しない。
- 未定義事項を推測で補完しない。

### Hypothesis

- なし。

### Open Issues

- ブランドボイス。
- 正式な用語集。
- 法務表記。
- 多言語対応。
- 価格・Policy の表示基準。
- 評価・推奨表現の根拠基準。
- Content の運用・承認方法。

## 3. Content Principles

判断基準として、以下の [Service Design Principles](principles.md) を主に参照する: SDP-001〜010。原則から具体的な仕様が自動的に決まるわけではない。本文書内で新しい原則を独断で追加・統合・削除しない。

## CTP-001: Purpose Before Detail

### Decision

情報の目的と利用者が判断すべきことを、詳細より先に理解できるようにする。

### Rationale

利用者が現在の目的と判断要点を把握できないと、詳細に埋もれて判断が困難になる (SDP-001)。

### Application

- 情報の主目的を先に示す。
- 利用者が判断すべき要点を明確にする。
- 詳細情報で主要な意味を埋没させない。

### Does Not Decide

- 表示順の具体仕様 / 文字数 / レイアウト / 見出し文言。

### Related Artifacts

- Screen Matrix / Screen Requirements / Design System

## CTP-002: Plain and Direct Language

### Decision

内部用語や曖昧な表現を避け、利用者が理解できる直接的な表現を使用する。

### Rationale

内部用語や曖昧表現は利用者に推測を強い、誤解を生む (SDP-001 / SDP-004)。

### Application

- 社内用語・業界用語を説明なく使用しない。
- 曖昧な代名詞や対象不明な表現を避ける。
- 必要以上に婉曲・誇張した表現を使用しない。

### Does Not Decide

- 正式な用語集 / ブランドトーン / 敬語レベル / 翻訳方針。

### Related Artifacts

- Navigation / CTA Principles / Screen Requirements

## CTP-003: Conditions Near Decisions

### Decision

価格・条件・制約・例外を、それらが判断へ影響する位置と時点で提示する。

### Rationale

重要条件が判断より後に判明すると、透明性と信頼性を損なう (SDP-003 / SDP-002)。

### Application

- Price、Policy、Availability 等を判断対象の近くで示す。
- 後から重要条件が判明する構造を避ける。
- 重要条件を補足情報だけへ隔離しない。

### Does Not Decide

- 表示項目 / 価格構造 / Policy の正式分類 / 表示位置。

### Related Artifacts

- Information Architecture / Screen Requirements / Design System

## CTP-004: Evidence-backed Claims

### Decision

「おすすめ」「人気」「安い」「残りわずか」等の評価・強調表現には、確認可能な根拠を必要とする。

### Rationale

根拠のない評価・希少性表現は誤認を招く。未確認の前提を事実として扱わない (SDP-003 / SDP-008)。

### Application

- 根拠のない評価・比較・希少性表現を使用しない。
- 根拠、対象、期間、基準が不明な場合は確定表現にしない。
- Hypothesis や推定値を Fact として提示しない。

### Does Not Decide

- ランキングロジック / 評価基準 / データ提供元 / 証拠の保存形式。

### Related Artifacts

- Information Architecture / Screen Requirements

## CTP-005: Consistent Terminology

### Decision

同じオブジェクト・状態・操作には、一貫した用語を使用する。

### Rationale

用語の不整合は学習コストと誤解を生み、サービス全体の整合性を損なう (SDP-004 / SDP-009)。

### Application

- IA オブジェクト名と矛盾する用語を独断で作らない。
- 同じ状態や操作に複数名称を混在させない。
- Navigation ラベルと本文の意味を一致させる。

### Does Not Decide

- 正式な日本語・英語名称 / 用語集の管理方法 / 商品名・ブランド名。

### Related Artifacts

- Information Architecture / Navigation / Design System

## CTP-006: Explicit State and Uncertainty

### Decision

確定・未確定・取得中・変更可能性・失敗等の状態を曖昧にしない。

### Rationale

状態が曖昧だと、利用者はシステムの実態を誤解する (SDP-005)。

### Application

- Loading、Success、Error、Unavailable 等の状態を示す。
- 料金・在庫等の変動可能性を必要に応じて示す。
- 未取得・未確認情報を確定情報のように見せない。

### Does Not Decide

- 状態一覧 / 更新頻度 / 状態表示 Component / システム仕様。

### Related Artifacts

- Information Architecture / Screen Requirements / Design System

## CTP-007: Actionable Error and Recovery

### Decision

問題が発生した場合、何が起きたか、利用者が次に何を行えるかを示す。

### Rationale

原因と次の行動が示されないと、利用者は回復できない (SDP-006)。

### Application

- 問題の概要を理解できるようにする。
- 再試行、修正、戻る、問い合わせ等の可能な行動を示す。
- 利用者の責任ではない問題を、利用者の誤りのように表現しない。

### Does Not Decide

- エラーコード / エラー文言 / サポートチャネル / 再試行ロジック。

### Related Artifacts

- Navigation / Screen Requirements / Design System

## CTP-008: Accessible and Scannable Content

### Decision

視覚表現だけに意味を依存せず、見出し・順序・簡潔さにより理解しやすくする。

### Rationale

視覚のみに依存する表現は、環境や支援技術によって意味が失われる (SDP-007)。

### Application

- 見出しと情報順序で構造を理解できるようにする。
- 長い文章を必要以上に連続させない。
- 色、アイコン、位置だけに意味を依存させない。
- 支援技術で意味が失われない表現を考慮する。

### Does Not Decide

- 具体的なアクセシビリティ規格 / タイポグラフィ / 文字数制限 / Component 仕様。

### Related Artifacts

- Screen Requirements / Design System

## CTP-009: Context-preserving References

### Decision

リンク、補足、Policy、Review 等を参照する際、対象と元の文脈を失わせない。

### Rationale

参照によって対象や元の文脈を見失うと、判断が中断する (SDP-009 / SDP-006)。

### Application

- Policy や Review の対象を明確にする。
- 補足情報から元の対象へ戻れる文脈を維持する。
- リンク先や参照対象を予測できるようにする。

### Does Not Decide

- リンク配置 / モーダル・別画面等の UI / URL / 履歴保持方式。

### Related Artifacts

- Navigation / Screen Requirements

## CTP-010: Separate Fact, Decision, and Promotion

### Decision

事実、条件、サービス上の判断、販促表現を混同しない。

### Rationale

事実と販促・推奨が混同されると、利用者は客観情報を見分けられない (SDP-003 / SDP-008)。

### Application

- 施設・料金・条件等の Fact と販促表現を区別する。
- サービス運営上の推奨を客観的事実のように見せない。
- 広告・特集・編集情報がある場合、その性質を曖昧にしない。

### Does Not Decide

- 広告表示ルール / キャンペーン方針 / ブランド表現 / 推奨ロジック。

### Related Artifacts

- Information Architecture / CTA Principles / Screen Requirements

## 4. Content Categories

以下の分類はコンテンツ戦略や画面構成を決定するものではない。Key Principles は §3 の CTP を参照する。

| Content Category | Purpose | Related IA Objects | Key Principles | Status |
| --- | --- | --- | --- | --- |
| Identification | 対象を識別する | Destination / Accommodation / Room / Stay Plan / Booking | CTP-002 / 005 | Draft |
| Decision Support | 比較・評価・選択を支援する | Accommodation / Stay Plan / Price / Availability / Review | CTP-001 / 003 / 004 / 006 | Draft |
| Conditions and Policies | 条件・制約・例外を伝える | Policy / Price / Availability / Booking | CTP-003 / 005 / 006 | Draft |
| Task Guidance | 利用者の操作・判断を支援する | Search Criteria / Booking / User | CTP-001 / 002 / 007 | Draft |
| Status and Feedback | 現在状態・処理結果を伝える | Availability / Price / Booking | CTP-006 / 007 | Draft |
| Editorial and Support | 発見・理解・問題解決を支援する | Content / Destination / Accommodation / User | CTP-004 / 008 / 009 / 010 | Draft |

## 5. Relationship with IA Objects

以下は [Information Architecture](information-architecture.md) の 12 オブジェクトに対する Content 上の考慮事項である。IA オブジェクトの追加・変更は行わない。

| IA Object | Content Consideration | Status |
| --- | --- | --- |
| Destination | 地理・目的地の単位と関係を誤解なく示す | Draft |
| Search Criteria | 選択中の条件と変更可能性を明確にする | Draft |
| Accommodation | 施設を識別・比較できる情報を一貫して示す | Draft |
| Room | Accommodation・定員・設備等との関係を明確にする | Draft |
| Stay Plan | 提供内容・適用条件・対象 Room との関係を明確にする | Draft |
| Availability | 対象条件、確認時点、変動可能性を示す | Draft |
| Price | 対象、単位、内訳、条件、合計の関係を明確にする | Draft |
| Policy | 適用対象、条件、例外、影響を明確にする | Draft |
| Review | 評価対象、提供元、基準、不確実性を明確にする | Draft |
| Booking | 予約対象、条件、状態、変更の影響を明確にする | Draft |
| User | 会員モデルを推測せず、必要な役割を明確にする | Draft |
| Content | 編集・案内・サポート・販促の性質を混同しない | Draft |

## 6. Relationship with Navigation

- Navigation ラベルは移動先を合理的に予測できる表現を必要とする。
- Local / Contextual Navigation では、現在の対象との関係を Content で説明できるようにする。
- Task Navigation では、現在の段階と次に可能な行動を理解できる表現を必要とする。
- History and Recovery Navigation では、戻り先・修正対象・失われない情報を理解できるようにする。
- Utility Navigation では、主要タスクと補助情報を混同しない。
- 具体的な Navigation ラベルは本タスクで決定しない。

## 7. Status and Uncertainty Model

これはシステム状態一覧や業務状態遷移を定義するものではない。

| Information State | Content Requirement | Status |
| --- | --- | --- |
| Confirmed | 確定情報として対象・条件を明確に示す | Draft |
| Provisional | 暫定・変更可能であることを示す | Draft |
| Loading / Updating | 処理中または更新中であることを示す | Draft |
| Unavailable | 利用不能な対象・条件・理由を可能な範囲で示す | Draft |
| Error | 問題の概要と次の行動を示す | Draft |
| Unknown / Not confirmed | 不明・未確認であることを確定情報と区別する | Draft |

## 8. Boundary

### Content Principles に含む

- 情報表現の原則
- 情報の明確性・一貫性・透明性
- 条件・状態・不確実性の表現
- IA・Navigation との関係
- 後続成果物の判断基準

### Content Principles に含まない

- 具体的な文言 / CTA ラベル / ブランドボイス / キャンペーンコピー / SEO / 翻訳 / 法務文言 / UI Component / レイアウト / 画面別仕様 / コンテンツ制作・承認フロー

## 9. Relationship with Other Artifacts

- **Service Design Principles** — Content 判断の上位基準。
- **Information Architecture** — Content が表現する情報オブジェクトと概念関係を提供する。
- **Navigation** — 移動先、現在地、関係性を Content で理解できるようにする。
- **CTA Principles** — 利用者へ求める行動の表現・優先順位を定義する。Content Principles では具体的な CTA ラベルを決定しない。
- **Screen Matrix** — 各画面で扱う Content Category、IA オブジェクト、状態を整理する。
- **Screen Requirements** — 画面単位の具体的な Content 要件を定義する。
- **Design System** — Content の構造・状態・アクセシビリティを UI として実現する設計語彙を提供する。

## 10. Open Issues

以下は未決である。解決策は推測して記載しない。

- 10 原則の正式承認。
- CTP ID の正式採用。
- Content Category の正式承認。
- 正式な用語集・表記規則。
- ブランドボイス・トーン。
- 多言語・翻訳方針。
- 価格・税・手数料等の表示基準。
- Policy の表示基準。
- Review・評価・ランキングの表現基準。
- 「おすすめ」「人気」「お得」「残りわずか」等の根拠基準。
- エラー・状態表現の具体基準。
- 法務・規約・広告表現との整合性。
- コンテンツ制作・レビュー・承認フロー。
- 既存 Design System 内の文言・状態表現との整合性。
- CTA Principles 策定時の境界確認。
- Screen Matrix 策定時に不足分類が判明する可能性。

## 11. Change Log

| Date | Change | Status |
|---|---|---|
| 2026-07-15 | Initial draft of Travel Content Principles | Draft |
