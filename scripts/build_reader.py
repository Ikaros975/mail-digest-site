#!/usr/bin/env python3
"""Build dark-tech mobile reader HTML from markdown (mail + video).

## sections become top-level block-cards.
### subsections under a ## become nested sub-cards inside that parent card.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / ".venv" / "lib").glob("python*/site-packages") if (ROOT / ".venv").exists() else []:
    sys.path.insert(0, str(p))
for p in Path("/workspace/digest-site/.venv/lib").glob("python*/site-packages"):
    sys.path.insert(0, str(p))

import markdown

RAILS = ["cyan", "blue", "purple", "orange", "green", "gold", "red"]

TEMPLATE_LINKS = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{title}</title>
  <link rel="stylesheet" href="{css_prefix}assets/tokens.css" />
  <link rel="stylesheet" href="{css_prefix}assets/digest-reader.css" />
</head>
<body>
  <div class="reader-wrap">
    <header class="reader-hero reveal">
      <div class="reader-kicker">{kicker}</div>
      <h1>{title}</h1>
      <div class="reader-meta">{meta}</div>
    </header>
    <main>
{body}
    </main>
    <footer class="reader-footer reveal">邮件推送 · 暗色科技阅读页</footer>
  </div>
  <script>
  (function () {{
    var nodes = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) {{
      nodes.forEach(function (n) {{ n.classList.add('in'); }});
      return;
    }}
    var io = new IntersectionObserver(function (entries) {{
      entries.forEach(function (e) {{
        if (e.isIntersecting) {{
          e.target.classList.add('in');
          e.target.classList.remove('out');
        }} else if (e.boundingClientRect.top < 0) {{
          e.target.classList.add('out');
          e.target.classList.remove('in');
        }} else {{
          e.target.classList.remove('in');
        }}
      }});
    }}, {{ threshold: 0.12, rootMargin: '0px 0px -8% 0px' }}});
    nodes.forEach(function (n) {{ io.observe(n); }});
  }})();
  </script>
</body>
</html>
"""

TEMPLATE_INLINE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{title}</title>
  <style>
{style}
  </style>
</head>
<body>
  <div class="reader-wrap">
    <header class="reader-hero reveal">
      <div class="reader-kicker">{kicker}</div>
      <h1>{title}</h1>
      <div class="reader-meta">{meta}</div>
    </header>
    <main>
{body}
    </main>
    <footer class="reader-footer reveal">邮件推送 · 暗色科技阅读页</footer>
  </div>
  <script>
  (function () {{
    var nodes = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) {{
      nodes.forEach(function (n) {{ n.classList.add('in'); }});
      return;
    }}
    var io = new IntersectionObserver(function (entries) {{
      entries.forEach(function (e) {{
        if (e.isIntersecting) {{
          e.target.classList.add('in');
          e.target.classList.remove('out');
        }} else if (e.boundingClientRect.top < 0) {{
          e.target.classList.add('out');
          e.target.classList.remove('in');
        }} else {{
          e.target.classList.remove('in');
        }}
      }});
    }}, {{ threshold: 0.12, rootMargin: '0px 0px -8% 0px' }}});
    nodes.forEach(function (n) {{ io.observe(n); }});
  }})();
  </script>
</body>
</html>
"""


def strip_frontmatter(md: str) -> str:
    md = md.replace("\r\n", "\n")
    if md.startswith("---\n"):
        end = md.find("\n---\n", 4)
        if end != -1:
            return md[end + 5 :].lstrip("\n")
    return md


def md_html(body_md: str) -> str:
    return markdown.markdown(
        body_md,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html5",
    )


def split_h3(body: str) -> tuple[str, list[tuple[str, str]]]:
    """Split a ## body into lead markdown + list of (### heading, body)."""
    parts = re.split(r"(?m)^###\s+(.+)$", body)
    lead = parts[0].strip()
    subs: list[tuple[str, str]] = []
    i = 1
    while i + 1 < len(parts):
        subs.append((parts[i].strip(), parts[i + 1].strip()))
        i += 2
    return lead, subs


def md_to_h2_sections(md: str) -> tuple[str, list[tuple[str, str]]]:
    md = strip_frontmatter(md).strip()
    title = "阅读"
    m = re.search(r"^#\s+(.+)$", md, re.M)
    if m:
        title = m.group(1).strip()
        md = md[m.end() :].lstrip("\n")

    parts = re.split(r"(?m)^##\s+(.+)$", md)
    sections: list[tuple[str, str]] = []
    lead = parts[0].strip()
    if lead:
        sections.append(("概览", lead))
    i = 1
    while i + 1 < len(parts):
        sections.append((parts[i].strip(), parts[i + 1].strip()))
        i += 2
    return title, sections


def render_sub(heading: str, body_md: str, rail: str) -> str:
    inner = md_html(body_md)
    return (
        f'        <div class="block-card sub-card rail-{rail}">\n'
        f'          <div class="label">{rail}</div>\n'
        f"          <h3>{heading}</h3>\n"
        f"          {inner}\n"
        f"        </div>\n"
    )


def render_section(heading: str, body_md: str, rail: str, rail_idx: int) -> str:
    lead, subs = split_h3(body_md)
    lead_html = md_html(lead) if lead else ""
    sub_html = ""
    if subs:
        chunks = []
        for j, (sh, sb) in enumerate(subs):
            # child rails continue the palette after parent
            child_rail = RAILS[(rail_idx + 1 + j) % len(RAILS)]
            chunks.append(render_sub(sh, sb, child_rail))
        sub_html = '        <div class="sub-stack">\n' + "".join(chunks) + "        </div>\n"
    return (
        f'      <section class="block-card rail-{rail} reveal">\n'
        f'        <div class="label">{rail}</div>\n'
        f"        <h2>{heading}</h2>\n"
        f"        {lead_html}\n"
        f"{sub_html}"
        f"      </section>\n"
    )


def load_inline_style() -> str:
    tokens = (ROOT / "docs/assets/tokens.css").read_text(encoding="utf-8")
    css = (ROOT / "docs/assets/digest-reader.css").read_text(encoding="utf-8")
    css = re.sub(r"@import\s+url\(['\"]?[^'\")]+['\"]?\);\s*", "", css)
    return tokens + "\n\n" + css


def build(
    md_path: Path,
    out: Path,
    kicker: str,
    meta: str,
    css_prefix: str,
    inline: bool = False,
) -> None:
    title, sections = md_to_h2_sections(md_path.read_text(encoding="utf-8"))
    body = []
    for idx, (h, b) in enumerate(sections):
        rail = RAILS[idx % len(RAILS)]
        body.append(render_section(h, b, rail, idx))
    body_html = "".join(body)
    if inline:
        html = TEMPLATE_INLINE
        html = html.replace("{title}", title)
        html = html.replace("{kicker}", kicker)
        html = html.replace("{meta}", meta)
        html = html.replace("{body}", body_html)
        html = html.replace("{style}", load_inline_style())
    else:
        html = TEMPLATE_LINKS.format(
            title=title,
            kicker=kicker,
            meta=meta,
            body=body_html,
            css_prefix=css_prefix,
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"built={out} nested_subs={sum(1 for _, b in sections if re.search(r'(?m)^### ', b))}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    ap.add_argument("--kicker", default="DIGEST · FULL TEXT")
    ap.add_argument("--meta", default="")
    ap.add_argument("--css-prefix", default="")
    ap.add_argument("--inline", action="store_true", help="Embed tokens+css in <style> (Pages-safe)")
    args = ap.parse_args()
    build(args.input, args.output, args.kicker, args.meta, args.css_prefix, inline=args.inline)


if __name__ == "__main__":
    main()
