# Delivery Package

Use this reference for maximum-quality full literature-report PPT tasks.

## Standard Delivery

Return at least:

```text
final_presentation.pptx
```

If Image2-style generation is unavailable, do not treat `final_presentation.pptx` as available. First ask whether the user accepts a lower-fidelity fallback PPTX. Without explicit consent, return the planning artifacts instead. With explicit consent, create a template-following fallback using `assets/sample-literature-report.pptx`: inspect the template, select and duplicate source slides, and replace inherited slots. Use a clearly labeled filename such as `fallback_presentation.pptx` or `editable_fallback_presentation.pptx`.

## Maximum-Quality Delivery

When the user asks for the best possible result, strongest model, full workflow, or traceable output, prepare these deliverables when feasible:

```text
final_presentation.pptx
image2_pages.zip
image2_manifest.json
figure_source_manifest.md
paper_logic_tree.md
terminology_table.md
main_si_crosswalk.md
slide_outline.md
page_briefs.md
speaker_notes.md
possible_questions.md
backup_slide_plan.md or backup_slides.pptx
quality_check_report.md
editable_presentation.pptx (only if requested/produced)
```

## Deliverable Definitions

### final_presentation.pptx

The assembled PPT, with each accepted Image2 page inserted full-slide. Deliver this only after `image2_manifest.json` exists and `scripts/validate_image_only_pptx.py` passes.

### fallback_presentation.pptx / editable_fallback_presentation.pptx

A lower-fidelity PPTX produced only after the user explicitly accepts fallback output when Image2 is unavailable. It must follow the bundled `assets/sample-literature-report.pptx` by duplicating or pruning mapped source slides and replacing inherited text/image/table slots rather than using an unrelated freeform layout or a hand-redrawn approximation. Use `scripts/build_fallback_template_pptx.py` when possible and deliver its `fallback_build_report.json` alongside the deck. It may contain editable elements, but scientific figures must still come from real paper/SI/user-provided sources. Do not claim that a fallback deck passed Image2 manifest or image-only validation. Deliver it only after the slot/edit plan, figure manifest, render/layout QA, overflow checks, and placeholder cleanup are complete.

### image2_pages.zip

All generated 16:9 page images in final slide order.

### image2_manifest.json

A machine-checkable record that Image2-style full-slide generation was confirmed and that every delivered slide image used `generation_route: "image2_full_slide"` and `accepted: true`.

### figure_source_manifest.md

A traceable list of every scientific visual, its source, its slide, and the claim it supports.

### paper_logic_tree.md

The paper's argument structure: background, problem, strategy, evidence, application, conclusion, limitation, inspiration.

### main_si_crosswalk.md

A mapping from main-paper claims to SI figures, tables, methods, and controls.

### slide_outline.md

The final page order with section, title, figure source, and page purpose.

### page_briefs.md

One page brief per slide, prepared before image2 generation.

### speaker_notes.md

30-60 second Chinese oral notes for important slides, plus transition sentences and likely questions.

### quality_check_report.md

A final checklist report using `quality-gates.md`, including any unresolved limitations.

## If Time or Tooling Is Limited

Prioritize deliverables in this order:

```text
1. final_presentation.pptx, only if Image2 and validation gates passed
2. fallback_presentation.pptx, only if Image2 is unavailable, the user explicitly accepts fallback output, and the bundled sample template is used through template inspection, source-slide duplication, and inherited-slot replacement
3. image2_manifest.json, required when Image2-only PPTX is delivered
4. figure_source_manifest.md
5. page_briefs.md
6. fallback_build_report.json, required when `scripts/build_fallback_template_pptx.py` is used
7. quality_check_report.md, required for fallback PPTX and should include slot/edit-plan status, render/layout QA status, overflow status, and placeholder cleanup status
8. speaker_notes.md
9. possible_questions.md
10. image2_pages.zip
11. editable_presentation.pptx, only if requested
```

Do not claim a deliverable was produced if it was not produced.


### terminology_table.md

A consistent English-Chinese terminology table for sample names, methods, units, and cautious claim verbs.

### possible_questions.md

Likely teacher/advisor questions and safe answers grounded in the main paper and SI.

### backup_slide_plan.md / backup_slides.pptx

Backup slide plan or actual backup slides for methods, controls, full figure panels, and dense SI evidence.

### editable_presentation.pptx

Optional editable deck. Produce only when requested or feasible. The image2-based stable deck remains the authoritative presentation version.

When Image2 is unavailable, editable output is allowed only as user-approved fallback output, must use the bundled sample template through the fallback template edit spec, and must be labeled accordingly.

## Delivery Honesty

Always state exactly which deliverables were produced. Do not list support files as complete if they were only planned.


### adaptive_navigation_plan.md

The paper-specific navigation labels, page ranges, and rationale. This prevents hard-coded navigation labels from being used across unrelated papers.

### deck_order_map.md

The final page-order source of truth: page number, section, navigation highlight, mainline/backup status, source figures, final image filename, and status.

### image_generation_status.md

A table tracking whether each image2 page is planned, generated, accepted, redrawn, replaced, or final-assembled.

### pre_assembly_checklist.md

A check that all accepted images exist in the final folder and match the deck order map before PPT assembly.

### post_assembly_audit.md / final_ppt_render_montage.png

A whole-deck audit after PPT assembly. The montage helps verify page order, navigation continuity, page numbers, and visual consistency.

### deck_diagnosis_report.md

A page-by-page diagnosis of current problems, fix type, redraw priority, and recommended action for an existing deck.

### redraw_priority_plan.md

A plan classifying slides as A: must redraw, B: local repair, or C: keep.

### final_page_lock.md

A record of whether page order is locked, which version is locked, and which changes are allowed.

### final_delivery_preview.md

A concise final overview for the user: page count, mainline/backup count, navigation labels, core evidence chain, audit status, produced support files, and manual checks.

### post_assembly_audit.md / final_ppt_render_montage.png

A whole-deck audit after PPT assembly. The montage helps verify page order, navigation continuity, page numbers, and visual consistency.
