# High-Quality Production Protocol

Use this protocol when the user wants the strongest or best possible literature-report PPT. The goal is to prevent the model from jumping from paper reading directly to slide output.

## Principle

Do not treat PPT generation as one step. Treat it as a staged production pipeline:

```text
close reading -> logic extraction -> evidence mapping -> adaptive navigation -> deck order map -> page briefs -> image2 status tracking -> PPT assembly -> render audit -> quality report
```

If the user explicitly requests maximum quality, deep mode, strongest model, or best possible result, follow this protocol even if it takes more intermediate work.

## Required Production Stages

### Stage 1: Intake and file audit

Confirm or internally identify:

- main paper PDF;
- supplementary information / supporting information file;
- sample deck style reference;
- any user-specific focus or time limit;
- language: Chinese by default for literature reports.

Record any missing or unreadable file before planning slides.

### Stage 2: Rigorous close reading

Use `close-reading-rules.md` as the reading discipline.

For full PPT production, do not reproduce the full paper paragraph by paragraph unless the user asks. Instead, create a faithful extraction of:

- research question;
- field gap;
- author strategy;
- methods;
- evidence chain;
- limitations;
- transferable ideas.

### Stage 2.5: Terminology and domain control

Use `terminology-control.md` to establish a term table before writing slide copy. Use `domain-adaptation.md` to choose the evidence-chain order that fits the paper domain.

### Stage 3: Main-paper + SI crosswalk

Use `main-si-crosswalk.md` to connect every main-paper claim with SI support when available.

Do not ignore SI. Use SI for synthesis details, controls, extended characterization, stability, repeatability, and supporting figures.

### Stage 4: Figure-source manifest

Use `figure-source-manifest.md` and `figure-extraction-and-naming.md`.

Every scientific visual used in the deck must have a source record. If a source cannot be identified, do not use the visual.


### Stage 4.5: Adaptive navigation and deck order map

Use `adaptive-navigation.md` to derive navigation labels from the paper's actual argument. Do not hard-code one universal navigation bar. Then create `deck_order_map.md` using `deck-order-map.md` before page briefs or image2 generation.

The deck order map must define every slide's final page number, section, navigation highlight, page role, source figures, mainline/backup status, and final image filename. This map becomes the source of truth for all later image generation and PPT assembly.

### Stage 5: Page outline

Create a page-by-page outline of at least 20 slides for a full deck unless the user requested fewer. The outline must follow the adaptive navigation and deck order map, while preserving the sample deck visual rhythm. The default fallback rhythm is:

```text
封面 -> 基本信息 -> 研究背景 -> 研究思路 -> 研究结果 -> 总结启发 -> 汇报完毕
```

The results section can expand beyond the default page count when the paper logic requires it.

### Stage 6: Page briefs

Before creating image2, write one page brief per slide using `page-brief-template.md`.

A page brief is the contract between paper reading and slide design. Do not generate a slide image before its brief is clear.

### Stage 7: Image2 generation

Create one 16:9 full-slide image per slide. Each image2 should already contain title, adaptive navigation, figures, annotations, notes, and page number. Use `batch-image-consistency.md` for multi-batch generation and `image-generation-status.md` to record generated, accepted, redrawn, and final-assembled slides.

Use deterministic composition and real source materials. Do not use freeform image generation for scientific data or figures. Follow `real-figure-annotation-rules.md` and `trend-emphasis-rules.md`.

### Stage 8: PPT assembly

Before assembly, use `version-control-and-final-folder.md` and `pre-assembly-checklist.md`. Insert only accepted images from the final approved image2 folder full-slide into the PPT. Do not rebuild the deck as editable PPT elements unless the user requests editable slides.

### Stage 9: Speaker notes, question prep, and backup slides

When maximum quality is requested, prepare speaker notes using `speaker-notes-template.md`. Use `question-prep.md` for likely teacher/advisor questions and safe answers. Use `backup-slides.md` to append or plan backup slides for dense SI evidence, controls, methods, or full source panels.

### Stage 9.5: Output package choice

Use `editable-output-options.md` to decide whether to return only the default stable image2-based PPT or, if requested and feasible, an additional editable PPT.

### Stage 10: Post-assembly audit and final quality report

After assembly, use `post-assembly-render-audit.md` to render or inspect the assembled PPT as a whole and create a montage when feasible. Then use `quality-gates.md` before delivery. If any gate fails, fix it or explicitly report the limitation. Use `failure-recovery.md` to handle missing files, unreadable figures, low-resolution source images, or unsupported claims. Use `final-scoring-rubric.md` to create a concise final score in the quality report.

## Required Internal Artifacts

For maximum-quality runs, create or maintain these artifacts internally, and return them when useful or requested:

```text
paper_logic_tree.md
terminology_table.md
main_si_crosswalk.md
figure_source_manifest.md
adaptive_navigation_plan.md
deck_order_map.md
slide_outline.md
page_briefs.md
image2_generation_plan.md
image_generation_status.md
speaker_notes.md
possible_questions.md
backup_slide_plan.md
pre_assembly_checklist.md
post_assembly_audit.md
final_ppt_render_montage.png
quality_check_report.md
```

These artifacts make the workflow auditable and reduce hidden mistakes.

## Stage 10.5: Iterative refinement and diagnosis

When refining an existing PPT, do not restart the whole pipeline unless needed. Use `deck-diagnosis-mode.md` to diagnose page-level and deck-level issues, use `redraw-priority.md` to decide A/B/C actions, and use `final-page-lock.md` to preserve accepted page order. Use `speaker-notes-to-slide-check.md` as a presentation-readiness test for key pages.

Add these artifacts when refining:

```text
deck_diagnosis_report.md
redraw_priority_plan.md
final_page_lock.md
final_delivery_preview.md
```
