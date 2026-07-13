# ToCoo Design System — 成果物索引

- 種別: DS 成果物の入口 (README)
- 状態: Draft (サービスごとに版数が異なる — 下表「トークン現行版」参照)
- 作成日: 2026-07-02
- 更新日: 2026-07-13 (travel を 0.3.0-draft へ更新)
- 構築主体: Claude Design (Builder 役割)。自己レビューは Architect 役割で実施済。2026-07-02 の独立監査所見 (是正 R-1/R-2・S-3〜S-6) を反映後、travel は設計判断 TVL-0001〜0012 を経て 0.3.0-draft へ更新済。rental-car・inbound は初版 Draft のまま。再監査と最終判断 (オーナー) は未了

---

## 構成 (3独立 DS = ADR-0022)

3サービスは Foundation (Primitive 含む)・Semantic・design.md を共有しない (P1)。命名・運用規約のみ共通 (P2)。

| サービス | フォルダ | トークン現行版 (primitive / semantic) | 成果物 |
| --- | --- | --- | --- |
| 国内宿泊予約 (tvl / travel) | `travel/` | 0.3.0 / 0.3.0-draft | design.md・primitive.travel.json・semantic.travel.json・components.md |
| 国内レンタカー (drc / japan) | `rental-car/` | 0.2.0 / 0.2.1-draft | design.md・primitive.rental-car.json・semantic.rental-car.json・components.md |
| インバウンドレンタカー (irc / inbound) | `inbound/` | 0.2.1 / 0.1.1-draft | design.md・primitive.inbound.json・semantic.inbound.json・components.md (semantic は新規生成) |

読み順 (各サービス): `design.md` → `semantic.*.json` → `primitive.*.json` → `components.md`

## 規約 (3サービス共通 = P2)

- 命名: `01_共通アセット/命名規則.md` (引き渡しパッケージ同梱) に準拠
- 参照: Semantic → primitive は `{color.palette.*}` 形式。Component 実装は Semantic のみ参照 (primitive 直接参照禁止)
- 未確定: `$status=placeholder` + `$note` (Q番号 / follow-up 番号)。文書中は 🚧 暫定 / ❓ 要議論
- 非構築: 会員ランク色 (C-10 破棄)・100選ゾーン・管理画面 UI (P3)

## 未確定事項 (分類C)

オーナー確認待ちの集約は `owner-decisions.md` を参照。travel の未確定事項は `travel/design.md` §未確定事項の一覧を正とする (TVL-0005・success 色は 0.3.0-draft で解決済。shadow/motion/ボタン状態/フォームは実査待ちで継続)。

## 構築ステータス

| フェーズ (構築ロードマップ §3) | travel | rental-car | inbound |
| --- | --- | --- | --- |
| Ph-A 前提確認 | 済 | 済 | 済 |
| Ph-B Foundation | 済 (0.3.0-draft) | 済 (Draft) | 済 (Draft) |
| Ph-C Semantic | 済 (0.3.0-draft) | 済 (Draft) | 済 (Draft・新規生成) |
| Ph-D Component | 済 (0.3.0-draft・未取得は placeholder) | 済 (Draft・同左) | 済 (Draft・同左) |
| Ph-E design.md | 済 (0.3.0-draft) | 済 (Draft) | 済 (Draft) |
| Ph-F 自己検証 | 済 (再実施) | 済 (再実施) | 済 (再実施) |

- travel は上記 2026-07-02 Draft から設計判断 TVL-0001〜0012 を反映し **0.3.0-draft** へ更新済 (rem/4px 化・テキスト2段確定・breakpoint 現代化・タイポグラフィ刷新・ブランド色 navy→ロイヤル/インディゴ・per-scheme 配色・campaign ボタン廃止 ほか)。rental-car・inbound は初版 Draft のまま
- MB-1〜MB-5 の品質判定は自己検証ベース。MB-3 以降の正式判定は独立監査 (Claude Code 側 Architect) の再監査とオーナーレビューに委ねる
- 是正履歴: 独立監査所見 (2026-07-02) の R-1 (primitive 直接参照の解消)・R-2 (travel link を placeholder へ降格)・S-3〜S-6 を反映済。うち **R-2 (travel link) はその後 TVL-0011 で link=各スキームの主色として解決済** (降格は解消)。Ph-F を再実施し components.md の primitive 直接参照ゼロを確認

---

## 変更履歴

| 日付 | 変更内容 | 変更者 |
| --- | --- | --- |
| 2026-07-02 | 初版 (3サービス分の成果物一式・索引・ステータス) | Claude Design |
| 2026-07-02 | 独立監査所見の是正を反映 (R-1/R-2・S-3〜S-6)。直接参照のあった semantic 3ファイルは version bump (travel/rc 0.2.1、inbound 0.1.1)、primitive.inbound 0.2.1 | Claude Design (Builder) |
| 2026-07-13 | travel/ を 0.3.0-draft へ更新 (TVL-0001〜0012・PR分割)。ブランド色刷新・rem/4px化・per-scheme配色・campaign廃止。索引の構成表 (トークン現行版)・構築ステータス・是正履歴 (R-2 解消) を実態に同期 | Claude Code |
