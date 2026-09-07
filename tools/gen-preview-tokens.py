#!/usr/bin/env python3
"""DS 見本ページ (preview.<service>.html) の生成ブロックを更新する。

各サービスの `semantic.<service>.json` / `primitive.<service>.json` を正本として、
見本ページ内のマーカーで囲まれた 3 ブロックを生成する。見本ページに値や一覧を手で
書き写さないための生成器であり、値・`$status` の正本は JSON 側にある。

  @generated:tokens   :root の CSS 変数 (semantic 全件 + primitive の各スケール)
  @generated:colors   色見本の一覧 (semantic の色トークン全件)
  @generated:scales   タイポ・余白・角丸・影などスケールの一覧

対応サービスは SERVICES に定義する。サービスごとに色見本の並び (color_groups) と
アイコン見本の色 (icon_color) が異なるため、共通の走査ロジックへ設定として渡す。

使い方:
    python3 tools/gen-preview-tokens.py                     # 全サービスを更新
    python3 tools/gen-preview-tokens.py --service travel    # 1 サービスだけ更新
    python3 tools/gen-preview-tokens.py --check             # 差分があれば終了コード 1
"""

import argparse
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# primitive から CSS 変数へ出す群 (semantic に無いスケールのみ)。全サービス共通
PRIMITIVE_GROUPS = [
    "spacing", "breakpoint", "radius", "shadow", "iconSize",
    "typography.size", "typography.lineHeight", "typography.fontWeight",
    "elevation.z", "size.container", "border.width",
]

# スケール見本の並び: (見出し, パス接頭辞, 見本の描き方)。全サービス共通
SCALE_GROUPS = [
    ("文字サイズ", "typography.size", "text"),
    ("行間", "typography.lineHeight", "plain"),
    ("ウェイト", "typography.fontWeight", "weight"),
    ("余白", "spacing", "bar"),
    ("角丸 (primitive)", "radius", "radius"),
    ("角丸 (用途)", "radius.", "radius-semantic"),
    ("影", "shadow", "shadow"),
    ("アイコンサイズ", "iconSize", "icon"),
    ("ブレークポイント", "breakpoint", "plain"),
    ("コンテナ幅", "size.container", "plain"),
    ("重なり (z)", "elevation.z", "plain"),
    ("モーション", "motion", "plain"),
]

# サービスごとの設定。色見本の並びは各 DS が持つ semantic の群に合わせる
# (travel は color.icon = 評価色を持ち、rental-car は color.mask = マスク面を持つ)
SERVICES = {
    "travel": {
        "dir": ROOT / "services" / "travel" / "design-system",
        "color_groups": [
            ("スキーム — メイン (royal)", "color.scheme.main"),
            ("スキーム — サブ (indigo)", "color.scheme.sub"),
            ("ブランド", "color.brand"),
            ("操作 (Button)", "color.action"),
            ("文字", "color.text"),
            ("面", "color.surface"),
            ("境界", "color.border"),
            ("状態", "color.state"),
            ("特集アクセント", "color.accent"),
            ("ラベル・タグ", "color.label"),
            ("会員種別", "color.membership"),
            ("施設属性タグ", "color.tag"),
            ("フォーカス・アイコン・オーバーレイ", "color.focus"),
            ("", "color.icon"),
            ("", "color.overlay"),
        ],
        # アイコンサイズ見本の色に使う CSS 変数 (評価色)
        "icon_color": "--color-icon-rating",
    },
    "rental-car": {
        "dir": ROOT / "services" / "rental-car" / "design-system",
        "color_groups": [
            ("スキーム — メイン (royal)", "color.scheme.main"),
            ("スキーム — サブ (indigo)", "color.scheme.sub"),
            ("ブランド", "color.brand"),
            ("操作 (Button)", "color.action"),
            ("文字", "color.text"),
            ("面", "color.surface"),
            ("境界", "color.border"),
            ("状態", "color.state"),
            ("特集アクセント", "color.accent"),
            ("ラベル・タグ", "color.label"),
            ("会員種別", "color.membership"),
            ("中立タグ", "color.tag"),
            ("フォーカス・マスク・オーバーレイ", "color.focus"),
            ("", "color.mask"),
            ("", "color.overlay"),
        ],
        # rental-car は評価色 (ReviewStars) を持たないため主色を用いる
        "icon_color": "--color-brand-primary",
    },
}

BLOCKS = {
    "tokens": ("  /* === generated:tokens (tools/gen-preview-tokens.py) — 手で編集しない === */",
               "  /* === /generated:tokens === */"),
    "colors": ("<!-- === generated:colors (tools/gen-preview-tokens.py) — 手で編集しない === -->",
               "<!-- === /generated:colors === -->"),
    "scales": ("<!-- === generated:scales (tools/gen-preview-tokens.py) — 手で編集しない === -->",
               "<!-- === /generated:scales === -->"),
}


class Service:
    """1 サービスぶんの正本 (semantic / primitive) と見本ページの組。"""

    def __init__(self, name, config):
        self.name = name
        self.dir = config["dir"]
        self.color_groups = config["color_groups"]
        self.icon_color = config["icon_color"]
        self.semantic_path = self.dir / f"semantic.{name}.json"
        self.primitive_path = self.dir / f"primitive.{name}.json"
        self.target = self.dir / f"preview.{name}.html"
        for path in (self.semantic_path, self.primitive_path, self.target):
            if not path.exists():
                raise SystemExit(f"{self.name}: ファイルが無い: {path.relative_to(ROOT)}")
        self.sem = json.loads(self.semantic_path.read_text(encoding="utf-8"))
        self.prim = json.loads(self.primitive_path.read_text(encoding="utf-8"))

    # --- 走査のたすけ ---------------------------------------------------

    @staticmethod
    def node(root, path):
        cur = root
        for key in path.split("."):
            if not isinstance(cur, dict) or key not in cur:
                return None
            cur = cur[key]
        return cur

    def resolve(self, value, depth=0):
        if depth > 8 or not isinstance(value, str):
            return value
        ref = re.fullmatch(r"\{(.+)\}", value.strip())
        if not ref:
            return value
        for root in (self.sem, self.prim):
            target = self.node(root, ref.group(1))
            if target and "$value" in target:
                return self.resolve(target["$value"], depth + 1)
        raise SystemExit(f"{self.name}: 参照を解決できない: {value}")

    def flatten(self, obj, prefix=""):
        """($value を持つ葉のパス, 実値, $status, $description) を列挙する。"""
        out = []
        if isinstance(obj, dict):
            if "$value" in obj:
                out.append((prefix, self.resolve(obj["$value"]), obj.get("$status", ""),
                            obj.get("$description", "")))
            else:
                for key, val in obj.items():
                    if not key.startswith("$"):
                        out.extend(self.flatten(val, f"{prefix}.{key}" if prefix else key))
        return out

    # --- ブロック 1: CSS 変数 -------------------------------------------

    def build_tokens(self):
        rows = self.flatten(self.sem)
        for group in PRIMITIVE_GROUPS:
            sub = self.node(self.prim, group)
            if sub is None:
                raise SystemExit(f"{self.name}: primitive に不在: {group}")
            rows += self.flatten(sub, group)
        width = max(len(css_name(p)) for p, *_ in rows)
        lines = [BLOCKS["tokens"][0], "  :root {"]
        for path, value, status, _ in rows:
            mark = " 🚧 placeholder" if status == "placeholder" else ""
            lines.append(f"    {css_name(path):<{width}}: {value}; /* {path}{mark} */")
        lines.append("  }")
        lines.append(BLOCKS["tokens"][1])
        return "\n".join(lines)

    # --- ブロック 2: 色見本 ---------------------------------------------

    def build_colors(self):
        lines = [BLOCKS["colors"][0]]
        for title, prefix in self.color_groups:
            rows = self.flatten(self.node(self.sem, prefix), prefix)
            if not rows:
                raise SystemExit(f"{self.name}: 色トークンが空: {prefix}")
            if title:
                lines.append(f'  <h3>{html.escape(title)}</h3>')
            lines.append('  <div class="sw-grid">')
            for path, value, status, _ in rows:
                lines.append(
                    '    <div class="sw">'
                    f'<span class="sw__chip" style="background: var({css_name(path)})"></span>'
                    f'<code>{path}</code>'
                    f'<span class="sw__val">{value}{flag(status)}</span>'
                    "</div>"
                )
            lines.append("  </div>")
        lines.append(BLOCKS["colors"][1])
        return "\n".join(lines)

    # --- ブロック 3: スケール見本 ---------------------------------------

    def sample(self, kind, path):
        var = f"var({css_name(path)})"
        if kind == "text":
            return f'<span style="font-size: {var}">見本 Aa 12,800円</span>'
        if kind == "weight":
            return f'<span style="font-weight: {var}">見本 Aa 12,800円</span>'
        if kind == "bar":
            return f'<span class="bar" style="width: {var}"></span>'
        if kind in ("radius", "radius-semantic"):
            return f'<span class="shape" style="border-radius: {var}"></span>'
        if kind == "shadow":
            return f'<span class="shape shape--plain" style="box-shadow: {var}"></span>'
        if kind == "icon":
            return (f'<i class="fa-solid fa-star" style="font-size: {var}; '
                    f'color: var({self.icon_color})"></i>')
        return ""

    def build_scales(self):
        lines = [BLOCKS["scales"][0]]
        for title, prefix, kind in SCALE_GROUPS:
            if kind == "radius-semantic":
                rows = self.flatten(self.node(self.sem, "radius"), "radius")
            else:
                root = self.sem if prefix.startswith(("motion",)) else self.prim
                sub = self.node(root, prefix.rstrip("."))
                if sub is None:
                    raise SystemExit(f"{self.name}: 不在: {prefix}")
                rows = self.flatten(sub, prefix.rstrip("."))
            lines.append(f'  <h3>{html.escape(title)}</h3>')
            lines.append('  <div class="tablewrap"><table class="scale">')
            lines.append("    <tbody>")
            for path, value, status, _ in rows:
                lines.append(
                    f"      <tr><td><code>{path}</code></td>"
                    f'<td class="scale__val">{html.escape(str(value))}{flag(status)}</td>'
                    f'<td class="scale__sample">{self.sample(kind, path)}</td></tr>'
                )
            lines.append("    </tbody>")
            lines.append("  </table></div>")
        lines.append(BLOCKS["scales"][1])
        return "\n".join(lines)

    # --- 反映 -----------------------------------------------------------

    def apply_blocks(self, text):
        for name, builder in (("tokens", self.build_tokens), ("colors", self.build_colors),
                              ("scales", self.build_scales)):
            begin, end = BLOCKS[name]
            start, stop = text.find(begin), text.find(end)
            if start < 0 or stop < 0:
                raise SystemExit(f"{self.name}: マーカーが見つからない: {name}")
            text = text[:start] + builder() + text[stop + len(end):]
        return text


def css_name(path):
    return "--" + re.sub(r"(?<!^)(?=[A-Z])", "-", path.replace(".", "-")).lower()


def flag(status):
    return ' <span class="flag">🚧</span>' if status == "placeholder" else ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--service", choices=sorted(SERVICES), action="append",
                        help="対象サービス (既定: 全サービス。複数指定可)")
    args = parser.parse_args()

    names = args.service or sorted(SERVICES)
    stale = []
    for name in names:
        service = Service(name, SERVICES[name])
        original = service.target.read_text(encoding="utf-8")
        updated = service.apply_blocks(original)
        rel = service.target.relative_to(ROOT)

        if args.check:
            if updated != original:
                print(f"{name}: 生成ブロックが JSON と一致しない。再生成が必要 ({rel})",
                      file=sys.stderr)
                stale.append(name)
            else:
                print(f"{name}: 一致")
            continue

        if updated != original:
            service.target.write_text(updated, encoding="utf-8")
            print(f"{name}: 更新 {rel}")
        else:
            print(f"{name}: 変更なし")

    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
