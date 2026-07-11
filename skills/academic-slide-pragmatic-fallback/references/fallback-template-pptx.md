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

## Required Template-Following Workflow

Fallback PPTX output must follow the existing template deck instead of approximating it with a new code layout.

Required steps:

1. Inspect every slide in `assets/sample-literature-report.pptx`; do not infer the template from one screenshot or one representative slide.
2. Use `references/sample-template-slot-manifest.json` as the source slot manifest, or regenerate it with `scripts/extract_template_slot_manifest.py` if `assets/sample-literature-report.pptx` changes. The manifest records source-slide roles, inherited text/image/table slots, object addresses, capacity hints, figure frames, navigation/footer chrome, and sample scientific objects that must be replaced or deleted.
3. Select a source slide for every output slide based on the needed page role and evidence density.
4. Create a `fallback_edit_plan.json`, `template-frame-map.json`, or equivalent mapping that records each output slide, source slide, reuse mode, and edit targets.
5. For any slide whose scientific content changes, define explicit edit targets for inherited title, body, figure, caption, table, annotation, footer, and placeholder objects. Do not label a content-bearing slide as preserve-only.
6. Copy the template and prune/reorder it to the mapped source slides before editing. The checked-in builder currently requires distinct source slides; choose an equivalent unused archetype instead of pretending to clone a slide part.
7. Prepare real source figures by trimming PDF/screenshot margins before insertion. Use `scripts/prepare_fallback_figure.py` or an equivalent deterministic crop step, and record the result in `prepared_figure_manifest.json`.
8. Edit inherited objects in place. Replace inherited sample figures with prepared real current-paper/SI/user figures, and rewrite inherited sample text with current-paper claims. For figures or tables whose aspect ratio does not fit a single inherited slot, adapt within the inherited image region instead of forcing a cramped slot fill.
9. Add new objects only when the mapped source slide lacks an inherited object for the required role, and record the reason and bounded placement.
10. Render the final fallback deck and inspect every slide.

Use `scripts/build_fallback_template_pptx.py` for step 6-8 when the deck can be represented as source-slide selection plus inherited slot edits. Follow `fallback-template-edit-spec.md` for the required slot manifest, edit plan, text replacement, image replacement, build report, and QA contract.

Forbidden fallback routes:

- rebuilding a visually similar deck from scratch;
- using a generic card/grid layout engine and only copying the colors;
- drawing a new navigation bar when the copied source slide already has navigation chrome;
- adding new text boxes over old sample text instead of replacing or deleting the inherited object;
- leaving inherited scientific content hidden behind new objects;
- rasterizing a code-drawn editable deck and describing it as template-based.

If the tooling cannot inspect, duplicate, or edit inherited template objects reliably, stop and deliver planning artifacts only.

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

Cleanup also applies inside the PPTX package. Remove unused slide relationships, replaced image relationships, inherited notes/notes masters, stale section IDs, unused masters/layouts, old core/app/custom document properties, and old slide-count/title metadata. A clean render is not proof that the package is clean.

Also inspect inherited PowerPoint placeholders that may not be obvious in rendered PNGs. Empty title, footer, date, slide-number, picture, and content placeholders must be filled, deleted, or explicitly documented as intentional template chrome. Do not pass cleanup by overlaying new objects on top of empty placeholders.

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
- trim irrelevant PDF/screenshot background margins before placement so the visible scientific content is centered in the inherited frame;
- adapt the placement to the real figure's shape: wide tables need wide regions, portrait diagrams need taller regions, and multi-panel figures may need to be split rather than squeezed;
- when a mapped template slide has multiple inherited image slots but the current slide needs one wide/dense figure, merge those inherited image slots into a single larger figure region if doing so better preserves the paper figure;
- do not place an empty card, caption box, or other shape underneath the figure unless it contains a useful current-paper caption;
- put captions or source labels close to the figure edge, not in a large empty box below it;
- keep explanatory bullets in a separate text region that does not overlap or visually compete with the figure.

If a figure is too small, visually off-center, margin-dominated, or dense to read after preparation, split the evidence across multiple slides, crop a more focused real region, choose a different source slide with a better image slot, or move it to backup. Do not shrink a full paper table until it becomes decorative.

For code-built fallback decks, classify dense tables in the edit plan. The builder's readability gate evaluates the actual inserted size at a 1280x720 review canvas, independently of frame occupancy, so a wide but shallow table cannot pass merely because it fills its small slot.

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
2. Create a contact sheet / montage. On macOS, `scripts/render_pptx_quicklook_contact_sheet.py fallback.pptx --out-dir fallback_render_qa --clean` is the preferred fallback when LibreOffice rendering is unavailable.
3. Inspect every slide for overlap, clipping, sparse layouts, unreadable figures, and inconsistent navigation.
4. Iterate until the deck is visually acceptable.
5. Record the result in `quality_check_report.md` or `fallback_test_report.json`.

Run an overflow/canvas-boundary check when available. If a copied source slide already contains an inherited object that slightly overflows, do not ignore it: either choose a cleaner source slide, fix/delete the inherited object, or document it as inherited template overflow in the QA report. New fallback content must not introduce additional overflow.

If rendering is unavailable, perform structural checks and state that visual render QA could not be completed. Do not claim render QA passed.

## Delivery Statement

When delivering a fallback PPTX, include:

```text
Image2 backend used: no
Delivery mode: fallback PPTX accepted by user
Template source: assets/sample-literature-report.pptx
Template-following workflow: inspected, mapped, duplicated, edited inherited objects
Source scientific visuals: real paper/SI/user-provided figures only
Image2-only validation: not applicable
Render/layout QA completed: yes/no
Editable elements may exist: yes
```
