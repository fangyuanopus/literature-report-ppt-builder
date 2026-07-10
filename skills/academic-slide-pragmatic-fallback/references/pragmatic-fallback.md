# Pragmatic Fallback Route

Use only after explicit user acceptance of an editable fallback. Start from a blank 16:9 deck and never import a content-bearing template master/layout. Follow `first-template-style-contract.md` for every page.

## Plan schema

```json
{
  "deck": {"navigation": ["研究背景", "研究设计", "结果验证", "结论展望"], "footer": "论文题目 · 期刊年份"},
  "slides": [{
    "slide_no": 1,
    "section": "结果验证",
    "layout_type": "figure_wide",
    "title": "结论型标题",
    "bullets": ["证据点一", "证据点二"],
    "figures": [{"figure_id": "fig_06", "path": "prepared/fig_06.png", "source_type": "figure_crop", "crop_verified": true, "source_page": 3, "source_label": "Fig. 6", "caption": "固液比对游离油得率的影响"}]
  }]
}
```

The figure must be a prepared crop, not a full paper-page scan. Use `source_label` only beside that displayed crop; do not put an orphaned `Fig. N` on a summary page.

## Page types

- `cover`: centered title and bibliographic metadata; no dense bullets.
- `text`: background, limitation, or interpretation page with 2–5 concise bullets.
- `figure_right`: portrait micrograph, scheme, or tall figure on the right; 2–5 evidence bullets on the left.
- `figure_wide`: horizontal plot/table as the dominant content; 2–4 concise interpretation bullets below.
- `process`: a 2–5 step chain, not a dense pseudo-flowchart.
- `comparison`: two genuine alternatives only.
- `summary`: 2–5 parameter or conclusion rows.
- `closing`: minimal thank-you page with bibliographic metadata only.

## Hard checks

- Use 3–7 short navigation labels and one active label only.
- Rewrite titles longer than 54 characters; never allow title overflow.
- Use at most five body bullets, each no longer than 58 characters.
- Use Microsoft YaHei for Chinese visible text. Do not expose route names, fallback/template/model terms, or build notes.
- Run the pragmatic validator, then render and inspect every slide. Fix all overflow, overlap, unreadable figures, sparse page types, and inconsistent chrome before delivery.
