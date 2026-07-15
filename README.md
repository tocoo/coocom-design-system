# coocom Service Design Repository

- 種別: リポジトリ全体の入口 (README)
- 状態: 初期構造 (bootstrap) — Service Design 策定を開始するための最小基盤
- 対象リポジトリ: `tocoo/coocom-design-system`

このリポジトリは、Service Design から Design System までを一元管理するための設計リポジトリである。従来は Design System 中心の構成だったが、Task 001〜004 の設計成果物に基づき、Service Design を含む論理レイヤー構造へ移行した。

## 1. 目的

- サービスの設計意図から Design System までを、責務ごとに分離して一元管理する。
- 後続の Service Design 策定を開始できる、責務が判別可能な基盤を提供する。

## 2. Single Source of Truth

- このリポジトリ本体が、設計の Single Source of Truth (正本) である。
- Governance・Service Design・Screen Requirements・Design System・Assets・設計判断・決定記録・正式仕様・未決事項は、すべてリポジトリ本体で管理する。

## 3. リポジトリ本体と GitHub Wiki の責務

- **リポジトリ本体 (正本)**: 設計判断・正式仕様・ADR・Design System の正本を置く。設計判断はリポジトリ本体を優先する。
- **GitHub Wiki (非正本)**: リポジトリの読み方・利用ガイド・初学者向け説明・運用説明などを置く想定の補助領域。設計判断・正式仕様・ADR・Design System の正本を Wiki に置かない。
- 本 README には、存在が確認できない Wiki ページへのリンクは記載しない。

## 4. 論理レイヤー

リポジトリは 5 つの論理レイヤーを持つ。

1. **Governance** — 全サービスを横断する共通領域 (`governance/`)
2. **Service Design** — サービス単位 (`services/<service>/service-design/`)
3. **Screen Requirements** — サービス単位 (`services/<service>/screen-requirements/`)
4. **Design System** — サービス単位 (`services/<service>/design-system/`)
5. **Assets** — サービス単位 (`services/<service>/assets/`)

Governance は横断共通、それ以外は原則サービス単位で管理する。

## 5. サービス一覧

現在の対象サービスは 3 つ。ディレクトリ名は**暫定のサービス識別子**であり、正式な識別子は未決である (`governance/owner-decisions.md` 確認事項 #8 を参照)。

| サービス | ディレクトリ | 入口 |
| --- | --- | --- |
| 国内宿泊 | `services/travel/` | [services/travel/README.md](services/travel/README.md) |
| 国内レンタカー | `services/rental-car/` | [services/rental-car/README.md](services/rental-car/README.md) |
| インバウンドレンタカー | `services/inbound/` | [services/inbound/README.md](services/inbound/README.md) |

## 6. 推奨参照順序

1. 本 README (全体像)
2. [governance/](governance/README.md) (横断の位置づけと不足成果物)
3. 各サービス README → 各サービス配下の Service Design → Screen Requirements → Design System → Assets

上位レイヤー (なぜ・何を) から下位レイヤー (どう見せる・素材) へ向かう順を推奨とする。これは参照の目安であり、確定した運用フローではない。

## 7. リンク

- Governance: [governance/README.md](governance/README.md) / [governance/owner-decisions.md](governance/owner-decisions.md)
- 国内宿泊: [services/travel/README.md](services/travel/README.md)
- 国内レンタカー: [services/rental-car/README.md](services/rental-car/README.md)
- インバウンドレンタカー: [services/inbound/README.md](services/inbound/README.md)

## 8. 現在の構築状態

- 各サービスの **Design System は既存資産** として存在する (下表)。
- **Service Design / Screen Requirements の着手状況はサービス別に異なる** (下表)。国内宿泊 (travel) は Service Design が Draft (SD-001〜SD-007)、Screen Requirements が入口設計中 (In preparation)。国内レンタカー・インバウンドレンタカーは未着手。**Assets は全サービス未着手** (`Status: Not started`)。
- Governance は最小限の入口 (README・owner-decisions.md) のみ。正本となる原則・命名規則・ADR・レビュー規則・用語定義は未整備 (`governance/README.md` を参照)。

| サービス | Service Design | Screen Requirements | Design System | Assets |
| --- | --- | --- | --- | --- |
| 国内宿泊 (travel) | Draft (SD-001〜SD-007) | In preparation | 既存資産 (Draft, 0.3.0-draft 系) | Not started |
| 国内レンタカー (rental-car) | Not started | Not started | 既存資産 (Draft) | Not started |
| インバウンドレンタカー (inbound) | Not started | Not started | 既存資産 (Draft) | Not started |

各サービスの Design System の版数・成果物・状態の詳細は、当該サービスの README を参照。

## 9. 事実・決定・仮説・未決事項の区別

- 本リポジトリでは、事実・確定した決定・仮説 (暫定運用)・未決事項を混同しないこと。
- 未決事項は未決として明示する。暫定的な扱い (例: サービス識別子) を確定と表現しない。

## 10. 対象外

- 実装コードは本リポジトリの管理対象外とする。
- Design System の内容改善・トークン値の変更・命名変更は本 bootstrap の対象外。

---

## 付録: 移行前の Design System 索引の継承情報

本リポジトリは移行前、Design System の成果物索引 README だった。その有効情報は以下へ継承した。

- 各サービスの Design System 版数・成果物・構築ステータスは、各サービス README (`services/<service>/README.md`) の Design System セクションへ移動した。
- 3 サービス共通の規約 (命名・参照形式・未確定表記など) は Governance の対象であり、正本は未整備 (`governance/README.md` に不足として明記)。

### 変更履歴 (移行前 DS 索引 README より継承。Design System 資産の履歴)

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (3サービス分の成果物一式・索引・ステータス) | Claude Design |
| 2026-07-02 | 独立監査所見の是正を反映 (R-1/R-2・S-3〜S-6)。直接参照のあった semantic 3ファイルは version bump (travel/rc 0.2.1、inbound 0.1.1)、primitive.inbound 0.2.1 | Claude Design (Builder) |
| 2026-07-13 | travel/ を 0.3.0-draft へ更新 (TVL-0001〜0012・PR分割)。ブランド色刷新・rem/4px化・per-scheme配色・campaign廃止 | Claude Code |
| 2026-07-14 | リポジトリを Service Design Repository の初期構造へ移行 (Task 005 bootstrap)。Design System 資産を `services/<service>/design-system/` へ移動 | Claude Code |
