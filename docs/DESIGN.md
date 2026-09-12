# Digest site design

## Nested sections
- Top-level `##` → primary `.block-card`
- Nested `###` under that `##` → `.block-card.sub-card` inside a `.sub-stack` (e.g. 三大职业 → ①②③)
- Prefer `build_reader.py --inline` for Pages HTML so CSS cannot 404
