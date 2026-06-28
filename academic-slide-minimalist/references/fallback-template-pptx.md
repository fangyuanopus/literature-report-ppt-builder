# Fallback Template PPTX Rules

Use this reference only when Image2-style full-slide generation is unavailable and the user explicitly accepts fallback PPTX output.

## Required Source Contract

Do not create a real fallback literature-report PPTX unless the current task has enough source material:

- main paper PDF or full paper content;
- supplementary information / supporting information when the task expects SI support;
- real figures extracted from the paper, SI, or user-provided source images.

If those sources are missing, deliver only the planning artifacts and ask for the missing material. Do not use mock figures, decorative placeholders, invented charts, generated scientific diagrams, or the bundled sample deck's scientific content as substitutes.

## Template Source

Use `assets/sample-literature-report.pptx` as the required template/style/rhythm source.

Preserve as much as feasible:

- 16:9 page size;
- red-black-gray academic palette;
- top navigation rhythm;
- conclusion-style title hierarchy;
- page number and footer habits;
- figure/caption and annotation style;
- clean academic spacing.

Do not copy the sample deck's scientific claims, paper figures, captions, data, or terminology into a new paper deck unless the user explicitly says that sample deck is the current content source.

## Layout Density Rules

Fallback pages must use the slide canvas deliberately. Avoid tiny card-only pages that leave most of the slide empty.

## Template Cleanup Rules

Before adding new content to a fallback slide, remove or intentionally replace all copied sample-slide scientific content and placeholder objects.

Check especially for:

- empty rectangles, cards, or caption boxes left under inserted figures;
- invisible or near-empty text boxes occupying figure space;
- old sample-deck figure captions, labels, notes, and page-specific annotations;
- duplicate navigation bars or old active-section marks;
- background groups that visually frame an empty area without serving the new layout.

Do not leave a shape in the deck merely because it came from the template. Every visible object must either be template chrome (navigation, footer, page number, rule line) or current-deck content.

## Navigation Rules

Fallback navigation must follow the bundled sample deck's academic navigation style, not a generic segmented-button UI.

Rules:

- keep the navigation shallow and quiet, with thin dividers or understated tab styling;
- use one clear active state in sample red;
- keep inactive labels black/gray and visually secondary;
- do not use large filled button blocks across the top unless the sample slide itself uses that exact treatment;
- do not let navigation consume more than about 8-10% of slide height;
- make navigation labels short enough to avoid truncation or collision;
- verify after rendering that navigation does not overlap the title or subtitle.

If the chosen tooling cannot reliably reproduce the sample navigation, use a simpler text-and-rule navigation rather than oversized UI-like tabs.

## Figure Placement Rules

Real figures should be visually dominant and should not be boxed into a tiny placeholder.

For figure-led pages:

- place the figure in a single clean figure region occupying roughly 45-65% of slide area;
- preserve the figure's aspect ratio and readability;
- do not place an empty card, caption box, or other shape underneath the figure unless it contains a useful current-paper caption;
- put captions or source labels close to the figure edge, not in a large empty box below it;
- keep explanatory bullets in a separate text region that does not overlap or visually compete with the figure.

If a figure is too small or dense to read, split the evidence across multiple slides, crop a more focused real region, or move it to backup. Do not shrink a full paper table until it becomes decorative.

For normal content pages:

- use one dominant content area occupying roughly 55-75% of the slide width or height;
- use real figures at a readable size whenever figures are available;
- pair each figure with 2-4 short evidence-led bullets or callouts;
- avoid three small equal cards as the default layout unless the page is explicitly a comparison or summary;
- keep title, subtitle, navigation, and footer outside the main evidence area;
- if a page has too little content, merge it with a neighboring page or turn it into a stronger figure-led page.

For text-only logic pages:

- use a large left-to-right or top-to-bottom logic structure;
- keep no more than 4 main text blocks;
- use strong spacing and hierarchy instead of many small boxes;
- do not leave the center of the slide visually empty.

## Text Fit Rules

Before delivery, check rendered slides for:

- title wrapping that collides with navigation or subtitle;
- bullets clipped inside cards or text boxes;
- text too small to read during presentation;
- overlapping callouts, figures, navigation, or page numbers;
- long unbroken English identifiers overflowing their boxes.

Fix by shortening text first, then widening boxes, changing page type, splitting into multiple pages, or moving detail to speaker notes / backup. Do not simply shrink body text until it becomes unreadable.

## Render QA

Before delivering fallback PPTX:

1. Render all slides to PNG if a renderer is available.
2. Create a contact sheet / montage.
3. Inspect every slide for overlap, clipping, sparse layouts, unreadable figures, and inconsistent navigation.
4. Iterate until the deck is visually acceptable.
5. Record the result in `quality_check_report.md` or `fallback_test_report.json`.

If rendering is unavailable, perform structural checks and state that visual render QA could not be completed. Do not claim render QA passed.

## Delivery Statement

When delivering a fallback PPTX, include:

```text
Image2 backend used: no
Delivery mode: fallback PPTX accepted by user
Template source: assets/sample-literature-report.pptx
Source scientific visuals: real paper/SI/user-provided figures only
Image2-only validation: not applicable
Render/layout QA completed: yes/no
Editable elements may exist: yes
```
