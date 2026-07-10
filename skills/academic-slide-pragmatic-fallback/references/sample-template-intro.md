# Sample Literature Report Template Intro

Use this file with `sample-template-slot-manifest.json` when Image2 is unavailable and the user has explicitly accepted fallback PPTX output.

## One Sentence

Red-black-gray academic literature-report template with quiet top navigation, conclusion-style titles, figure-led result pages, compact captions, and restrained footer/page-number habits.

## Style Contract

- Canvas: 16:9, wide academic presentation.
- Palette: sample red, black, gray, warm off-white, and white.
- Tone: rigorous journal-club / group-meeting report, not commercial pitch design.
- Typography: preserve inherited font size tiers; do not shrink one title or body slot independently.
- Navigation: keep the template's understated navigation rhythm; do not redraw it as large button tabs.
- Figures: real paper/SI/user figures only; crop margins before insertion.

## Page Roles

| Role | Source Slides | Use For |
| --- | --- | --- |
| cover | 1 | Paper title, Chinese title/subtitle, speaker/date metadata |
| background | 2-4 | Problem setup, prior limitation, paper positioning |
| method | 5-7 | Research strategy, workflow, architecture, method overview |
| result | 8-14 | Main evidence pages with one or more real figures |
| application | 15-17 | Application/performance/generalization evidence |
| summary | 18-19 | Takeaways, limitations, presentation-ready conclusions |
| ending | 20 | Closing only; do not force into content if unnecessary |

## Selection Rules

- Select by role first, then by evidence density.
- Prefer result pages with inherited image slots when a slide needs scientific figures.
- Prefer text-only logic pages only for background, summary, or conceptual transitions.
- Do not use a cover, ending, or section-like page as a dense result page.
- Do not repeat the same source slide in the current builder unless a future true slide-cloning implementation is available.
- If no source slide has a suitable inherited slot, split the slide, choose another role-compatible page, or stop with planning artifacts.

## Text Slot Rules

- Use `slot_id` from `sample-template-slot-manifest.json` whenever possible.
- Keep inherited style and same-level font sizes.
- Rewrite text to fit the slot; do not use ellipsis truncation.
- If a slot is marked replaceable and is not used by current content, delete it explicitly in `fallback_edit_plan.json`.
- Navigation labels and page numbers are template chrome unless the deck order/navigation plan requires a deliberate edit.

## Figure Slot Rules

- Every inserted scientific visual must be listed in `figure_source_manifest.md`.
- Every inserted image should pass through `prepare_fallback_figure.py` or the builder's built-in preparation step.
- Use inherited image slots; do not add new image boxes over template objects unless the edit plan documents the exception.
- If a real figure remains too small or off-center after preparation, choose a larger figure-frame source slide or split the figure across slides.

## Build Route

Preferred fallback route:

```bash
python3 scripts/draft_fallback_edit_plan.py slide_briefs.json fallback_edit_plan.json
python3 scripts/build_fallback_template_pptx.py fallback_edit_plan.json fallback_presentation.pptx --report fallback_build_report.json
```

Review the build report before delivery. Overflow warnings, ellipsis warnings, untouched replaceable slots, or missing prepared figures mean the fallback still needs repair.
