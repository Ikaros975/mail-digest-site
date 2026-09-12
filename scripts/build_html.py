#!/usr/bin/env python3
"""Build readable HTML pages from markdown digests."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".venv" / "lib" / "python3.13" / "site-packages"))
# also try any venv site-packages
for p in (ROOT / ".venv" / "lib").glob("python*/site-packages"):
    sys.path.insert(0, str(p))

import markdown  # noqa: E402

TEMPLATE = (ROOT / "templates" / "article.html").read_text(encoding="utf-8")


def md_to_html_body(md: str) -> str:
    return markdown.markdown(
        md,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html5",
    )


def extract_title(md: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"^##\s+(.+)$", md, re.M)
    if m:
        return m.group(1).strip()
    return fallback


def slugify(s: str) -> str:
    s = re.sub(r"[\[\]#：:]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff._-]+", "", s)
    return s[:80] or "digest"


def build_one(md_path: Path, out_dir: Path, eyebrow: str, slug: str | None) -> Path:
    md = md_path.read_text(encoding="utf-8")
    title = extract_title(md, md_path.stem)
    body = md_to_html_body(md)
    # drop duplicate h1 if template shows title separately — keep in body for now
    html = (
        TEMPLATE.replace("{{title}}", title)
        .replace("{{eyebrow}}", eyebrow)
        .replace("{{body}}", body)
    )
    name = slug or slugify(title)
    dest = out_dir / f"{name}.html"
    dest.write_text(html, encoding="utf-8")
    return dest


def write_index(pages: list[tuple[str, str]], out_dir: Path) -> None:
    items = "\n".join(
        f'      <li><a href="{href}">{title}</a></li>' for title, href in pages
    )
    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>阅读归档</title>
<style>
body{{margin:0;font-family:system-ui,sans-serif;background:#f7f5f0;color:#1c1917}}
.wrap{{max-width:720px;margin:40px auto;padding:0 18px}}
.card{{background:#fff;border:1px solid #e7e5e4;border-radius:18px;padding:28px}}
h1{{font-size:1.4rem;margin:0 0 16px}}
li{{margin:10px 0;line-height:1.5}}
a{{color:#0e7490}}
</style></head><body><div class="wrap"><div class="card">
<h1>阅读归档</h1>
<ul>
{items}
</ul>
</div></div></body></html>
"""
    (out_dir / "index.html").write_text(html, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=ROOT / "public")
    ap.add_argument("--eyebrow", default="邮件推送 · 全文阅读")
    ap.add_argument("--slug", default=None)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    pages: list[tuple[str, str]] = []
    for i, path in enumerate(args.inputs):
        slug = args.slug if len(args.inputs) == 1 else None
        if slug is None:
            # prefer date from path like yage-20260912
            m = re.search(r"(20\d{6})", str(path))
            slug = m.group(1) if m else None
        dest = build_one(path, args.out, args.eyebrow, slug)
        title = extract_title(path.read_text(encoding="utf-8"), dest.stem)
        pages.append((title, dest.name))
        print(f"built={dest}")
    write_index(pages, args.out)
    print(f"index={args.out / 'index.html'}")


if __name__ == "__main__":
    main()
