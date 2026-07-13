# ToCoo Design System — 成果物索引

- 種別: DS 成果物の入口 (README)
- 状態: Draft
- 作成日: 2026-07-02
- 構築主体: Claude Design (Builder 役割)。自己レビューは Architect 役割で実施済。独立監査 (Claude Code 側 Architect) の初回所見を反映済 (是正 R-1/R-2・S-3〜S-6 = 2026-07-02)。再監査と最終判断 (オーナー) は未了

---

## 構成 (3独立 DS = ADR-0022)

3サービスは Foundation (Primitive 含む)・Semantic・design.md を共有しない (P1)。命名・運用規約のみ共通 (P2)。

| サービス | フォルダ | 成果物 |
| --- | --- | --- |
| 国内宿泊予約 (tvl / travel) | `travel/` | design.md・primitive.travel.json・semantic.travel.json・components.md |
| 国内レンタカー (drc / japan) | `rental-car/` | design.md・primitive.rental-car.json・semantic.rental-car.json・components.md |
| インバウンドレンタカー (irc / inbound) | `inbound/` | design.md・primitive.inbound.json・semantic.inbound.json・components.md (semantic は新規生成) |

読み順 (各サービス): `design.md` → `semantic.*.json` → `primitive.*.json` → `components.md`

## 規約 (3サービス共通 = P2)

- 命名: `01_共通アセット/命名規則.md` (引き渡しパッケージ同梱) に準拠
- 参照: Semantic → primitive は `{color.palette.*}` 形式。Component 実装は Semantic のみ参照 (primitive 直接参照禁止)
- 未確定: `$status=placeholder` + `$note` (Q番号 / follow-up 番号)。文書中は 🚧 暫定 / ❓ 要議論
- 非構築: 会員ランク色 (C-10 破棄)・100選ゾーン・管理画面 UI (P3)

## 未確定事項 (分類C)

オーナー確認待ちの集約は `owner-decisions.md` を参照。

## 構築ステータス

| フェーズ (構築ロードマップ §3) | travel | rental-car | inbound |
| --- | --- | --- | --- |
| Ph-A 前提確認 | 済 | 済 | 済 |
| Ph-B Foundation | 済 (Draft) | 済 (Draft) | 済 (Draft) |
| Ph-C Semantic | 済 (Draft) | 済 (Draft) | 済 (Draft・新規生成) |
| Ph-D Component | 済 (Draft・未取得は placeholder) | 同左 | 同左 |
| Ph-E design.md | 済 (Draft) | 済 (Draft) | 済 (Draft) |
| Ph-F 自己検証 | 済 (再実施) | 済 (再実施) | 済 (再実施) |

- MB-1〜MB-5 の品質判定は自己検証ベース。MB-3 以降の正式判定は独立監査 (Claude Code 側 Architect) の再監査とオーナーレビューに委ねる
- 是正履歴: 独立監査所見 (2026-07-02) の R-1 (primitive 直接参照の解消)・R-2 (travel link 降格)・S-3〜S-6 を反映済。Ph-F を再実施し components.md の primitive 直接参照ゼロを確認

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (3サービス分の成果物一式・索引・ステータス) | Claude Design |
| 2026-07-02 | 独立監査所見の是正を反映 (R-1/R-2・S-3〜S-6)。直接参照のあった semantic 3ファイルは version bump (travel/rc 0.2.1、inbound 0.1.1)、primitive.inbound 0.2.1 | Claude Design (Builder) |
| 2026-07-13 | travel/ を 0.3.0-draft へ更新 (TVL-0001〜0012・PR分割)。ブランド色刷新・rem/4px化・per-scheme配色・campaign廃止 | Claude Code |
