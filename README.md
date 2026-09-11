# coocom Service Design Repository

- 種別: リポジトリ全体の入口 (README)
- 状態: 運用中 — 初期構造 (bootstrap, Task 005・2026-07-14) は構築済み。現在は Governance の Review / Approval Rules (承認済み・適用中) の下で、Design System の改定と国内宿泊 (travel) の上流成果物の整備を進めている
- 対象リポジトリ: `tocoo/coocom-design-system`
- 本 README が記述する現状の基準: `main` (2026-09-11 時点)

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

リポジトリ直下の `tools/` は上記 5 レイヤーのいずれにも属さない補助スクリプト置き場であり、**正本ではない**。現在の内容は DS 見本ページの生成器 `tools/gen-preview-tokens.py` のみである (§8 参照)。

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

- Governance: [governance/README.md](governance/README.md) / [governance/owner-decisions.md](governance/owner-decisions.md) / [governance/review-approval-rules-creation-plan.md](governance/review-approval-rules-creation-plan.md) (Draft) / [governance/review-approval-rules.md](governance/review-approval-rules.md) (承認済み・適用中)
- 国内宿泊: [services/travel/README.md](services/travel/README.md)
- 国内レンタカー: [services/rental-car/README.md](services/rental-car/README.md)
- インバウンドレンタカー: [services/inbound/README.md](services/inbound/README.md)
- 補助スクリプト (非正本): [tools/gen-preview-tokens.py](tools/gen-preview-tokens.py) — DS 見本ページ `preview.<service>.html` の生成ブロックを、各サービスの JSON を正本として更新する

## 8. 現在の構築状態

以下は `main` (2026-09-11 時点) の内容に基づく。

- 各サービスの **Design System は既存資産**として存在する (下表)。**国内宿泊 (travel) と国内レンタカー (rental-car) は改定が継続している**。改定は案件ごとに、Review / Approval Rules (`governance/review-approval-rules.md`) の経路 — 同規則 §8 影響度判定・§9／§20 改訂着手承認・§10 内容レビュー・§11 反映確定 — で扱い、取得した判断は `governance/owner-decisions.md` §10 以降の案件別節へ記録する。インバウンドレンタカー (inbound) は移行後に breakpoint 記録の整合 (primitive `0.2.2-draft`) を行ったのみで、内容の改定は未着手。
- **Service Design / Screen Requirements の着手状況はサービス別に異なる** (下表)。国内宿泊 (travel) は Service Design が Draft (SD-001〜SD-007)、Screen Requirements は入口 README と Creation Plan が存在し、着手可能候補 (SCR-001〜SCR-005・SCR-013・SCR-014) の個別要件が Draft・SCR-006〜SCR-012 は Not started (レイヤー全体は In preparation)。国内レンタカー・インバウンドレンタカーは未着手。**Assets は全サービス未着手** (`Status: Not started`)。
- Governance には入口 README・owner-decisions.md・Review / Approval Rules Creation Plan (Draft)・Review / Approval Rules 正本 (`governance/review-approval-rules.md`) が存在する。Review / Approval Rules は **Task 009-4 (2026-07-17) でオーナー (Web部責任者) が Repository 横断規則として明示的に承認し、適用開始条件（承認記録 PR の main マージ）は PR #67 のマージ（merge commit d095ded）で成立したため現在は適用中**である (Status = 承認済み・適用中。承認の正本ログは owner-decisions.md §5、適用開始の事実記録は §6)。適用開始後に 1 件の改定があり、**同規則 §8 へ編集的訂正 carve-out (編集的訂正の類型を影響度・低とする明文の例外) を追加する改定が 2026-07-21 に承認され、規則本体へ反映済み**である (承認記録は owner-decisions.md §9)。`governance/owner-decisions.md` は現在 §1〜§32 を持ち、**§10 以降は案件別の現在判断・改訂着手の設計承認・影響度判定の記録**である (承認済みの `review-approval-rules.md` 本体は、この案件別記録によっては改定しない)。**原則・命名規則・ADR・用語定義の正本は依然として未整備** (`governance/README.md` を参照)。
- **上流 (Service Design / Screen Requirements) と travel Design System の Alignment は未完了である。** Work Order 1〜6 は Draft で実施済みで、Work Order 6 (改訂着手可否の判断) の総合判断は Task 009-6 (2026-07-21) の再評価が記録上の最新であり、**全 12 候補「現時点では開始できない」を維持**している。Task 009-7 (2026-07-24) で候補固有の阻害 Fact の解決計画を Draft として作成した。**この 12 候補の改訂着手と、上記の案件ごとの Design System 改定は別経路である** — 案件別の記録は Work Order 6 の総合判断を変更していない (例: owner-decisions.md §15)。

| サービス | Service Design | Screen Requirements | Design System | Assets |
| --- | --- | --- | --- | --- |
| 国内宿泊 (travel) | Draft (SD-001〜SD-007) | In preparation (入口・Creation Plan あり; SCR-001〜SCR-005・SCR-013・SCR-014 個別要件 Draft, SCR-006〜SCR-012 Not started) | Draft (0.3.0-draft 系)・改定継続中 (記録上の最新は Task 009-65 / 2026-09-11) | Not started |
| 国内レンタカー (rental-car) | Not started | Not started | Draft (0.3.0-draft 系)・travel の定義体系を採用 (Task 009-57 / 009-63。判断は owner-decisions.md §25・§29) | Not started |
| インバウンドレンタカー (inbound) | Not started | Not started | Draft (primitive 0.2.2-draft / semantic 0.1.1-draft)・内容の改定は未着手 | Not started |

各サービスの Design System の版数・成果物・状態の詳細は、当該サービスの README を参照。

**DS 見本ページ**: 国内宿泊 (`services/travel/design-system/preview.travel.html`) と国内レンタカー (`services/rental-car/design-system/preview.rental-car.html`) には、正本のトークンを実際に描画した見本ページがある。見本ページは**非正本**であり、値・`$status` の正本は各サービスの `semantic.<service>.json` / `primitive.<service>.json` と `design.md` にある。見本ページ内の生成ブロックは `tools/gen-preview-tokens.py` で更新する (`--check` で差分の有無を検査できる)。

## 9. 事実・決定・仮説・未決事項の区別

- 本リポジトリでは、事実・確定した決定・仮説 (暫定運用)・未決事項を混同しないこと。
- 未決事項は未決として明示する。暫定的な扱い (例: サービス識別子) を確定と表現しない。

## 10. 対象外

- 実装コードは本リポジトリの管理対象外とする。
- Design System の内容改善・トークン値の変更・命名変更は、初期構造の構築 (bootstrap, Task 005) の対象外だった。現在はこれらを bootstrap とは別に、Review / Approval Rules (`governance/review-approval-rules.md`) の経路に従う個別 Task として扱う (§8 参照)。

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
