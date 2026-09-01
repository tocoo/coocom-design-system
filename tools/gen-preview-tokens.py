#!/usr/bin/env python3
"""DS 見本ページ (preview.travel.html) の生成ブロックを更新する。

`semantic.travel.json` / `primitive.travel.json` を正本として、見本ページ内の
マーカーで囲まれた 3 ブロックを生成する。見本ページに値や一覧を手で書き写さない
ための生成器であり、値・`$status` の正本は JSON 側にある。

  @generated:tokens   :root の CSS 変数 (semantic 全件 + primitive の各スケール)
  @generated:colors   色見本の一覧 (semantic の色トークン全件)
  @generated:scales   タイポ・余白・角丸・影などスケールの一覧

使い方:
    python3 tools/gen-preview-tokens.py            # 見本ページを更新
    python3 tools/gen-preview-tokens.py --check    # 差分があれば終了コード 1
"""

import argparse
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DS = ROOT / "services" / "travel" / "design-system"
SEMANTIC = DS / "semantic.travel.json"
PRIMITIVE = DS / "primitive.travel.json"
TARGET = DS / "preview.travel.html"

# primitive から CSS 変数へ出す群 (semantic に無いスケールのみ)
PRIMITIVE_GROUPS = [
    "spacing", "breakpoint", "radius", "shadow", "iconSize",
    "typography.size", "typography.lineHeight", "typography.fontWeight",
    "elevation.z", "size.container", "border.width",
]

# 色見本の並び (semantic の色トークンをこの順で束ねる)
COLOR_GROUPS = [
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
]

# スケール見本の並び: (見出し, パス接頭辞, 見本の描き方)
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

BLOCKS = {
    "tokens": ("  /* === generated:tokens (tools/gen-preview-tokens.py) — 手で編集しない === */",
               "  /* === /generated:tokens === */"),
    "colors": ("<!-- === generated:colors (tools/gen-preview-tokens.py) — 手で編集しない === -->",
               "<!-- === /generated:colors === -->"),
    "scales": ("<!-- === generated:scales (tools/gen-preview-tokens.py) — 手で編集しない === -->",
               "<!-- === /generated:scales === -->"),
}


def load():
    return (json.loads(SEMANTIC.read_text(encoding="utf-8")),
            json.loads(PRIMITIVE.read_text(encoding="utf-8")))


SEM, PRIM = load()


def node(root, path):
    cur = root
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def resolve(value, depth=0):
    if depth > 8 or not isinstance(value, str):
        return value
    ref = re.fullmatch(r"\{(.+)\}", value.strip())
    if not ref:
        return value
    for root in (SEM, PRIM):
        target = node(root, ref.group(1))
        if target and "$value" in target:
            return resolve(target["$value"], depth + 1)
    raise SystemExit(f"参照を解決できない: {value}")


def flatten(obj, prefix=""):
    """($value を持つ葉のパス, 実値, $status, $description) を列挙する。"""
    out = []
    if isinstance(obj, dict):
        if "$value" in obj:
            out.append((prefix, resolve(obj["$value"]), obj.get("$status", ""),
                        obj.get("$description", "")))
        else:
            for key, val in obj.items():
                if not key.startswith("$"):
                    out.append(None) if False else None
                    out.extend(flatten(val, f"{prefix}.{key}" if prefix else key))
    return out


def css_name(path):
    return "--" + re.sub(r"(?<!^)(?=[A-Z])", "-", path.replace(".", "-")).lower()


def flag(status):
    return ' <span class="flag">🚧</span>' if status == "placeholder" else ""


# --- ブロック 1: CSS 変数 -------------------------------------------------

def build_tokens():
    rows = flatten(SEM)
    for group in PRIMITIVE_GROUPS:
        sub = node(PRIM, group)
        if sub is None:
            raise SystemExit(f"primitive に不在: {group}")
        rows += flatten(sub, group)
    width = max(len(css_name(p)) for p, *_ in rows)
    lines = [BLOCKS["tokens"][0], "  :root {"]
    for path, value, status, _ in rows:
        mark = " 🚧 placeholder" if status == "placeholder" else ""
        lines.append(f"    {css_name(path):<{width}}: {value}; /* {path}{mark} */")
    lines.append("  }")
    lines.append(BLOCKS["tokens"][1])
    return "\n".join(lines)


# --- ブロック 2: 色見本 ---------------------------------------------------

def build_colors():
    lines = [BLOCKS["colors"][0]]
    for title, prefix in COLOR_GROUPS:
        rows = [r for r in flatten(node(SEM, prefix), prefix)]
        if not rows:
            raise SystemExit(f"色トークンが空: {prefix}")
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


# --- ブロック 3: スケール見本 --------------------------------------------

def sample(kind, path, value):
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
        return f'<i class="fa-solid fa-star" style="font-size: {var}; color: var(--color-icon-rating)"></i>'
    return ""


def build_scales():
    lines = [BLOCKS["scales"][0]]
    for title, prefix, kind in SCALE_GROUPS:
        if kind == "radius-semantic":
            rows = [r for r in flatten(node(SEM, "radius"), "radius")]
        else:
            root = SEM if prefix.startswith(("motion",)) else PRIM
            sub = node(root, prefix.rstrip("."))
            if sub is None:
                raise SystemExit(f"不在: {prefix}")
            rows = flatten(sub, prefix.rstrip("."))
        lines.append(f'  <h3>{html.escape(title)}</h3>')
        lines.append('  <div class="tablewrap"><table class="scale">')
        lines.append("    <tbody>")
        for path, value, status, _ in rows:
            lines.append(
                f"      <tr><td><code>{path}</code></td>"
                f'<td class="scale__val">{html.escape(str(value))}{flag(status)}</td>'
                f'<td class="scale__sample">{sample(kind, path, value)}</td></tr>'
            )
        lines.append("    </tbody>")
        lines.append("  </table></div>")
    lines.append(BLOCKS["scales"][1])
    return "\n".join(lines)


def apply_blocks(text):
    for name, builder in (("tokens", build_tokens), ("colors", build_colors),
                          ("scales", build_scales)):
        begin, end = BLOCKS[name]
        start, stop = text.find(begin), text.find(end)
        if start < 0 or stop < 0:
            raise SystemExit(f"マーカーが見つからない: {name}")
        text = text[:start] + builder() + text[stop + len(end):]
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    original = TARGET.read_text(encoding="utf-8")
    updated = apply_blocks(original)

    if args.check:
        if updated != original:
            print("生成ブロックが JSON と一致しない。再生成が必要", file=sys.stderr)
            return 1
        print("一致")
        return 0

    if updated != original:
        TARGET.write_text(updated, encoding="utf-8")
        print(f"更新: {TARGET.relative_to(ROOT)}")
    else:
        print("変更なし")
    return 0


if __name__ == "__main__":
    sys.exit(main())
