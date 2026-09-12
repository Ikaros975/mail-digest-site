# digest-site

邮件推送全文归档：Markdown 存档 + 阅读用 HTML。

## 本地生成

```bash
/workspace/digest-site/.venv/bin/python /workspace/digest-site/scripts/build_html.py \
  content/某期.md --eyebrow "鸭哥 AI 手记 · 全文" --slug 2026-09-12
```

产物在 `public/`（`index.html` + 各期 `.html`）。

## 发布

推到 GitHub 后开启 Pages（源：`public/` 或 `docs/`），微信推送里放 HTML 链接。
