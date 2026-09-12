# 共用视觉

- 风格：`dark-tech-style`（暗色科技）+ `frontend-design` 原则（用户口中的 fonted-design 按此落地）
- CSS：`tokens.css` + `digest-reader.css`
- 规则：每板块一张色卡（`.block-card.rail-*`），一节一色；滚动 `.reveal` 淡入；手机优先 max-width 720
- 构建：`scripts/build_reader.py`
- 视频页 CSS 相对路径用 `../../../assets/`（从 `docs/videos/YYYY/MM/`）
