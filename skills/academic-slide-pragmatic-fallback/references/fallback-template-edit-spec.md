# Fallback Template Edit Spec

Use this reference together with `fallback-template-pptx.md` when Image2 is unavailable and the user explicitly accepts fallback PPTX output.

This workflow borrows the useful part of template-editing skills such as `gorden-ppt-skill`: do not make code guess a fresh layout. First turn the template PPTX into a structured edit contract, then select slides and replace inherited slots.

## Core Principle

The fallback implementation should behave like template editing, not slide design.

Allowed:

- select source slides from `assets/sample-literature-report.pptx`;
- duplicate selected source slides into a starter deck;
- replace inherited text runs while preserving their font, size, color, paragraph spacing, and position;
- replace inherited image frames with real paper/SI/user-provided figures while preserving frame geometry and crop intent;
- delete inherited sample scientific content only when the edit plan says so;
- add a new object only when no inherited slot can serve the required role, with a bounded placement and reason.

Forbidden:

- rebuild the page from scratch with approximate coordinates;
- use the template only as a color/style reference;
- add a new title, navigation bar, text box, image frame, or caption over copied template objects instead of editing the inherited object;
- silently shrink fonts, resize boxes, or move template furniture to fit long text;
- leave sample-deck scientific text or figures hidden behind new objects.

## Required Intermediate Files

A real fallback deck must create or internally maintain these files:

```text
template_audit.md
template_slot_manifest.json
fallback_plan_report.json
fallback_edit_plan.json
prepared_figure_manifest.json
figure_source_manifest.md
fallback_build_report.json
quality_check_report.md or fallback_test_report.json
```

If any of these cannot be produced, do not claim the fallback passed template-following QA.

For the bundled sample deck, start from `sample-template-slot-manifest.json`. If `assets/sample-literature-report.pptx` changes, regenerate that manifest with:

```bash
python3 scripts/extract_template_slot_manifest.py
```

Use the dedicated builder whenever possible:

```bash
python3 scripts/draft_fallback_edit_plan.py \
  slide_briefs.json \
  fallback_edit_plan.json \
  --report fallback_plan_report.json

python3 scripts/build_fallback_template_pptx.py \
  fallback_edit_plan.json \
  fallback_presentation.pptx \
  --report fallback_build_report.json \
  --strict \
  --fail-on-warnings

python3 scripts/audit_fallback_template_pptx.py \
  fallback_presentation.pptx \
  --build-report fallback_build_report.json \
  --out fallback_structural_audit.json \
  --fail-on-review

python3 scripts/render_pptx_quicklook_contact_sheet.py \
  fallback_presentation.pptx \
  --out-dir fallback_render_qa \
  --clean
```

The draft script chooses role-compatible source slides and maps structured slide briefs onto inherited title, body, caption, and image slots. For figure slides, it also considers real image aspect ratios and reports predicted image occupancy so margin-heavy or badly matched frames can be avoided before building. It must avoid source pages whose sample scientific visuals are too strong to neutralize cleanly, unless the plan explicitly documents why no cleaner result/application page is available. Review `fallback_plan_report.json` before building, especially when it reports extra image slots, low predicted occupancy, many deletion edits, or a surprising source slide.

The builder is intentionally limited. It edits inherited slots from the manifest, prepares real source figures, prunes/reorders selected template slides, and writes a report. It should not be bypassed with a freeform code layout when a requested slide can be expressed as source-slide selection plus slot edits.

For exact-template output, add `--check-masters --exact-template` to the structural audit and run `audit_exact_template_fidelity.py` with the edit plan and build report. The exact audit verifies that the used master/layout shape trees, preserved chrome, text-box geometry, structured paragraph runs, and inherited image bounds did not drift.

If the build report says `status: "needs_review"`, do not deliver the fallback as finished. Shorten text, choose a better source slide, split the slide, tighten the real crop, or explicitly delete/replace remaining template objects, then rebuild.

On macOS, use `render_pptx_quicklook_contact_sheet.py` when LibreOffice rendering is unavailable or unstable. It creates per-slide QuickLook thumbnails plus `contact_sheet.png`; inspect this image before delivery.

If rendering is unavailable, run `audit_fallback_template_pptx.py` as a structural fallback QA. This does not replace visual QA, but it catches slide-count mismatches, surfaced warnings, and obvious sample scientific residue.

## Template Audit

Inspect every slide in `assets/sample-literature-report.pptx`, using rendered PNGs plus PPTX structure inspection.

For each source slide, record:

- slide number;
- page role: cover, section divider, background, method, result, comparison, summary, ending, or backup;
- navigation state and section label;
- reusable layout type: title-only, figure-left/text-right, figure-top/bullets-bottom, dense evidence, text-only logic, closing, etc.;
- main figure frame(s), table frame(s), caption slots, body text slots, title slots, footer/page-number slots;
- objects that are template chrome and must be kept;
- sample scientific objects that must be replaced or deleted;
- known hazards such as inherited overflow, grouped objects, empty placeholders, or non-editable flattened images.

Grouped template objects require special care. If a group contains any slot that will be reused for real paper text, captions, or figures, do not delete the whole group as a cleanup action. Delete only unused children or choose a cleaner source slide.

Do not choose output slides before this audit exists.

## Slot Manifest

Create `template_slot_manifest.json` in a structure like this. For the bundled sample deck, `references/sample-template-slot-manifest.json` is the checked-in baseline.

```json
{
  "$schema": "academic-fallback-template-slots/v1",
  "template_pptx": "assets/sample-literature-report.pptx",
  "slide_count": 20,
  "slide_size": { "width": 1280, "height": 720, "aspect": "16:9" },
  "theme": {
    "palette": ["#a20f18", "#1d1d1f", "#5f6268", "#f4f2ef"],
    "style": "red-black-gray academic"
  },
  "pages": [
    {
      "source_slide": 6,
      "role": "method",
      "layout_type": "figure-left-text-right",
      "use_for": "method overview with one dominant real figure",
      "slots": [
        {
          "slot_id": "s6_title",
          "kind": "text",
          "role": "slide title",
          "address": { "shape_id": 12, "paragraph": 0, "run": 0 },
          "current_text": "验证性质",
          "editable": true,
          "preserve_style": true,
          "capacity": { "max_chars": 28, "max_lines": 1 }
        },
        {
          "slot_id": "s6_main_figure",
          "kind": "image",
          "role": "dominant figure",
          "address": { "shape_id": 18 },
          "editable": true,
          "preserve_frame": true,
          "expected_source": "sample scientific figure; replace"
        }
      ],
      "keep_objects": ["navigation", "footer", "page number", "rule lines"],
      "delete_or_replace_objects": ["sample scientific claim text", "sample figure caption"]
    }
  ]
}
```

The exact address format may use the available tooling's IDs, but it must be stable enough for the current run and precise enough to target inherited objects.

## Fallback Edit Plan

Create `fallback_edit_plan.json` before editing the PPTX:

```json
{
  "$schema": "academic-fallback-edit-plan/v1",
  "document_properties": {
    "title": "Attention Is All You Need",
    "subject": "学术文献汇报",
    "creator": "",
    "last_modified_by": "",
    "company": ""
  },
  "selected_slides": [1, 3, 6, 10, 20],
  "slide_map": [
    {
      "output_slide": 1,
      "source_slide": 1,
      "role": "cover",
      "reuse_mode": "duplicate-slide",
      "edits": [
        { "slot_id": "s1_title", "new_text": "Attention Is All You Need" },
        { "slot_id": "s1_subtitle", "new_text": "Transformer: 用注意力替代递归的序列建模路线" },
        { "slot_id": "s1_main_figure", "new_image": "real_figures/fig1_transformer_architecture.png" }
      ]
    }
  ]
}
```

Rules:

- every output slide must map to one source slide;
- every content-bearing output slide must list explicit text/image/table edit targets;
- each text edit should use `slot_id` and `new_text`, or a precise `address` only when no slot ID exists;
- each image edit should use an inherited image `slot_id` and `new_image`;
- deletion of inherited sample objects should be explicit with `{"slot_id": "...", "action": "delete"}`;
- every editable slot in the selected source slide must be kept, replaced, or deleted intentionally;
- `preserve-only` is allowed only for true separator/ending/chrome slides with no changed scientific content;
- long text must be rewritten shorter, moved to notes, split across slides, or mapped to a roomier source slide. Do not solve fit by changing only one slot's font size.

For a multi-point inherited body box, use structured paragraphs instead of embedding every line in one text run:

```json
{
  "slot_id": "s16_text_7",
  "new_paragraphs": [
    {
      "runs": [
        {"text": "1. 基础证据，", "style": "base"},
        {"text": "关键结论。", "style": "emphasis"}
      ]
    },
    "2. 第二条完整结论。"
  ]
}
```

`base` and `emphasis` reuse the matching inherited run formatting. Do not set a new color or font directly. The new paragraph count must not exceed the inherited paragraph count.

When `new_text` contains line breaks, each line maps to one inherited paragraph. If a later inherited paragraph is empty, the builder reuses the first available inherited run style instead of falling back to PowerPoint defaults.

## Text Replacement Rules

Preserve the inherited run formatting:

- keep font family, size, bold/weight, color, paragraph alignment, line spacing, and text-box geometry;
- replace only the targeted run or paragraph;
- do not blanket-clear every text-bearing shape;
- do not leave default placeholder text, lorem ipsum, or sample science;
- do not end visible copy with ellipsis as a truncation workaround.

Capacity checks are advisory but mandatory to perform. If text is likely too long:

1. rewrite more concisely;
2. reduce the number of bullets;
3. select a source slide with a larger text slot;
4. split the content into another slide.

Do not silently shrink one title or body slot, because it breaks same-level typography.

## Figure Replacement Rules

For inherited image slots:

- prepare each source figure before insertion with `scripts/prepare_fallback_figure.py` or an equivalent deterministic crop step;
- write a preparation manifest, for example `python3 scripts/prepare_fallback_figure.py real_figures/*.png --out-dir prepared_figures --manifest prepared_figure_manifest.json`;
- trim PDF/screenshot whitespace or flat background margins so the real scientific content, not the surrounding paper margin, is centered in the inherited template frame;
- preserve the inherited frame position, size, and mask unless there is a recorded reason to change it;
- profile each real source figure/table by aspect ratio, density, and layout hint before placement;
- mark dense tables with `figure_profile: {"kind": "table", "dense": true}`. At the default 1280x720 review size, the builder warns when the inserted table is narrower than 560 px or shorter than 170 px; use `min_display_width_px` / `min_display_height_px` only when a reviewed source justifies a different threshold;
- for wide tables, wide plots, or dense figures that would look cramped in one inherited slot, use a recorded adaptive placement such as `fit_strategy: "adaptive_contain"` with `frame_scope: "all_image_slots"` to combine inherited image slots into one larger figure region;
- use only real source figures listed in `figure_source_manifest.md`;
- preserve scientific meaning when cropping;
- do not replace a figure slot with a generated diagram or decorative placeholder;
- if a real paper figure is too dense for the inherited frame, choose a source slide with a larger figure frame, split the figure across slides, or move the dense figure to backup.

If the template slide lacks a suitable image slot, prefer another source slide. Adaptive placement may adjust within inherited image regions, but it must not redraw the whole slide or invent a new layout. Add a new image object only as a documented exception.

Record every prepared figure in `prepared_figure_manifest.json`:

```json
{
  "$schema": "academic-fallback-prepared-figures/v1",
  "figures": [
    {
      "source": "real_figures/fig2_attention_mechanisms.png",
      "prepared": "prepared_figures/fig2_attention_mechanisms_trimmed.png",
      "operation": "trim_background",
      "bbox_removed": {"left": 24, "top": 18, "right": 21, "bottom": 30},
      "scientific_content_changed": false
    }
  ]
}
```

After insertion, inspect the rendered slide. If the actual scientific content still appears visibly off-center, too small, or dominated by leftover margins, do not accept the slide. Fix by preparing a tighter crop, selecting a different source slide with a better frame, or splitting the figure across slides.

## QA Requirements

Before delivery:

1. Render the source template contact sheet.
2. Render the starter deck contact sheet after slide selection/duplication.
3. Render the final fallback deck contact sheet after edits.
4. Run text overflow or canvas-boundary checks when available.
5. Compare final pages against their mapped source slides for title/nav/footer/figure-frame alignment.
6. Inspect the PPTX structure for empty placeholders and hidden sample content when tooling allows.
7. If render QA cannot run, perform structural QA with `scripts/audit_fallback_template_pptx.py` and state that visual render QA is still unavailable.

The QA report must state:

- whether template inspection was completed;
- whether a slot manifest and edit plan existed;
- whether every output slide mapped to a source slide;
- whether all inserted figures were prepared/cropped before placement;
- whether all figures came from real sources;
- whether any inherited overflow or placeholder issue remains;
- whether any image frame occupancy warnings remain;
- whether render QA passed.

## When to Stop

Stop and deliver planning artifacts instead of a PPTX if:

- the template cannot be inspected;
- inherited object addresses cannot be identified;
- real scientific figures are missing;
- the edit plan would require mostly new freeform objects;
- copied sample science cannot be reliably removed;
- rendered QA shows unresolved overlap, clipping, sparse pages, or wrong navigation placement.
