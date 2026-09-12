#!/usr/bin/env python3
"""Build dark-tech mobile reader HTML from markdown (mail + video)."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / ".venv" / "lib").glob("python*/site-packages") if (ROOT / ".venv").exists() else []:
    sys.path.insert(0, str(p))
# also try digest-site venv
for p in Path("/workspace/digest-site/.venv/lib").glob("python*/site-packages"):
    sys.path.insert(0, str(p))

import markdown

RAILS = ["cyan", "blue", "purple", "orange", "green", "gold", "red"]

TEMPLATE = """<!DOCTYPE html>
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
    }}, {{ threshold: 0.12, rootMargin: '0px 0px -8% 0px' }});
    nodes.forEach(function (n) {{ io.observe(n); }});
  }})();
  </script>
</body>
</html>
"""


def md_to_sections(md: str) -> tuple[str, list[tuple[str, str]]]:
    """Return (title, [(heading, html_inner), ...])."""
    md = md.replace("\r\n", "\n").strip()
    title = "阅读"
    m = re.search(r"^#{1,2}\s+(.+)$", md, re.M)
    if m:
        title = m.group(1).strip()
        md = md[m.end() :].lstrip("\n")

    # split on ### or ## headings
    parts = re.split(r"(?m)^(#{2,3})\s+(.+)$", md)
    # parts[0] = lead (懒人包 etc)
    sections: list[tuple[str, str]] = []
    lead = parts[0].strip()
    if lead:
        sections.append(("概览", lead))
    i = 1
    while i + 2 < len(parts):
        _hashes, heading, body = parts[i], parts[i + 1], parts[i + 2]
        sections.append((heading.strip(), body.strip()))
        i += 3
    return title, sections


def render_section(heading: str, body_md: str, rail: str) -> str:
    inner = markdown.markdown(
        body_md,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html5",
    )
    # avoid duplicate h2 if body starts with heading already consumed
    return (
        f'      <section class="block-card rail-{rail} reveal">\n'
        f'        <div class="label">{rail}</div>\n'
        f"        <h2>{heading}</h2>\n"
        f"        {inner}\n"
        f"      </section>\n"
    )


def build(md_path: Path, out: Path, kicker: str, meta: str, css_prefix: str) -> None:
    title, sections = md_to_sections(md_path.read_text(encoding="utf-8"))
    body = []
    for idx, (h, b) in enumerate(sections):
        rail = RAILS[idx % len(RAILS)]
        body.append(render_section(h, b, rail))
    html = TEMPLATE.format(
        title=title,
        kicker=kicker,
        meta=meta,
        body="".join(body),
        css_prefix=css_prefix,
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"built={out}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    ap.add_argument("--kicker", default="DIGEST · FULL TEXT")
    ap.add_argument("--meta", default="")
    ap.add_argument("--css-prefix", default="")  # '' for docs/*.html; '../' for docs/videos/YYYY/MM/
    args = ap.parse_args()
    build(args.input, args.output, args.kicker, args.meta, args.css_prefix)


if __name__ == "__main__":
    main()
