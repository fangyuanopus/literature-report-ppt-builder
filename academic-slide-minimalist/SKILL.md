---
name: academic-slide-minimalist
description: >
  Use this skill for Chinese academic literature-report PPTs, research slides, journal-club decks, thesis-defense slides, slide page images, or paper-to-PPT workflows based on real paper/SI figures. It enforces an Image2 availability gate: only an Image2-style native 16:9 full-slide image backend may create authoritative final pages. If unavailable or unconfirmed, stop before Image2-only PPTX creation and ask whether the user accepts a clearly labeled fallback PPTX. Fallback PPTX output is allowed only after explicit consent and must follow the bundled assets/sample-literature-report.pptx through a template-inspect, slide-duplicate, inherited-object-edit workflow; never produce an ad hoc freeform code-rendered deck or a hand-redrawn template approximation as fallback.
---

# Academic Slide Minimalist

## Non-Bypassable Execution Gates

These gates override every other workflow section in this skill. Run them before any slide-generation or PPTX-packaging action.

### Gate A: Image2 availability gate

Before creating final slide images, sample redesigned pages, or a PPTX, explicitly determine whether the current environment has an Image2-style native full-slide image-generation backend.

The backend counts as available only if all are true:

- it can generate one complete 16:9 academic slide image per page;
- the full-slide image can include title, navigation, real source figure crops, annotations, labels, notes, and page number inside the image;
- it can preserve scientific source crops faithfully without redrawing, restyling, or semantically changing them;
- its outputs can be saved as accepted final slide images and then mechanically packaged into an image-only PPTX.

If availability is unavailable, unclear, unconfirmed, or blocked by the current environment, do not create or deliver an Image2-only PPTX. First explain the boundary, then ask whether the user accepts a lower-fidelity fallback PPTX route. Until the user explicitly accepts that fallback, deliver only the valid non-image artifacts: paper reading outputs, adaptive navigation, `deck_order_map.md`, `figure_source_manifest.md`, `page_briefs.md`, Image2 prompts, and assembly notes.

Use this boundary statement when Image2 is unavailable:

```text
当前环境未确认可用 Image2-style 全页幻灯片生成后端，因此无法交付严格 Image2-only 高保真 PPTX。请选择：
A. 只交付可用于后续 Image2 生成的页面方案、figure manifest、page briefs、prompts 与 assembly notes；
B. 接受降级版 PPTX：使用现有 `assets/sample-literature-report.pptx` 的模板、版式节奏和红黑灰学术风格生成可编辑 fallback PPTX；它不是 Image2-only 高保真交付，也不能声称通过 Image2 manifest 与 image-only 验证。
```

### Gate B: Image2 manifest gate

Do not package a PPTX unless `image2_manifest.json` exists and records every final slide image. The manifest must include:

```json
{
  "image2_backend_confirmed": true,
  "slides": [
    {
      "slide_no": 1,
      "final_image": "final_images/slide_001.png",
      "generation_route": "image2_full_slide",
      "accepted": true,
      "source_figures": []
    }
  ]
}
```

Every delivered Image2-only slide must have `generation_route: "image2_full_slide"` and `accepted: true`. If the manifest is missing, incomplete, or says any page used another route, do not deliver an Image2-only PPTX.

### Gate C: PPTX validation gate

Before delivering a PPTX, run `scripts/validate_image_only_pptx.py` on the assembled file. If a manifest exists, validate with `--manifest image2_manifest.json`. Delivery is allowed only when the validator passes.

A passing PPTX must have exactly one full-slide image per slide and no editable text boxes, shapes, charts, tables, SmartArt, icons, or extra PowerPoint annotations.

### Gate D: mandatory delivery statement

When delivering a PPTX, include this factual checklist in the final response:

```text
Image2 backend used: yes
Full-slide images generated: yes
PPTX assembly mode: one full-slide image per slide
Editable slide elements: none
Source scientific visuals: real paper/SI/user-provided figures only
Validation completed: yes
```

If any line is not true, do not deliver the Image2-only PPTX.

### Gate E: explicit fallback consent gate

Fallback PPTX creation is allowed only after all of these are true:

- Image2-style full-slide generation is unavailable, unclear, unconfirmed, or blocked;
- the user has been shown the boundary statement above;
- the user explicitly chooses the fallback route or otherwise clearly states that a lower-fidelity PPTX is acceptable;
- the fallback deck uses the bundled `assets/sample-literature-report.pptx` through a template-following workflow: inspect the sample deck, map every output slide to a source slide, duplicate the mapped slides, then edit inherited objects rather than drawing a parallel layout;
- the fallback deck is grounded in the current main paper, SI, or user-provided source figures; do not use mock figures, decorative substitutes, or scientific content copied from the sample deck;
- the fallback deck passes a render-based layout QA pass with no unintended overlaps, no clipped text, and no sparse pages that use only a small fraction of the slide canvas;
- the fallback deck has no unused template placeholders or leftover shapes occupying figure/text space;
- the fallback navigation follows the sample deck's quiet academic style rather than generic oversized button tabs;
- the final response and file names clearly distinguish the fallback deck from the authoritative Image2-only deck.

A fallback PPTX must not be named or described as `final_presentation.pptx` unless the user explicitly asks for that filename. Prefer names such as:

```text
fallback_presentation.pptx
editable_fallback_presentation.pptx
```

When delivering a fallback PPTX, include this factual checklist instead of the Image2-only checklist:

```text
Image2 backend used: no
Delivery mode: fallback PPTX accepted by user
Image2-only validation: not applicable
Scientific visuals: real paper/SI/user-provided figures only
Editable or code-rendered elements may exist: yes
Template source: assets/sample-literature-report.pptx
Render/layout QA completed: yes
```

Never imply that the fallback PPTX satisfies Gates B-D. If the user does not accept fallback output, continue with the non-image planning artifacts only.

### Gate F: fallback template gate

When producing a fallback PPTX, use the bundled `assets/sample-literature-report.pptx` as the required template source. Preserve its 16:9 format, red-black-gray academic tone, title hierarchy, navigation rhythm, figure/caption treatment, and page-number/footer habits as much as the fallback tooling allows.

The fallback deck may be editable and may contain PowerPoint text boxes, shapes, and normal picture objects, but it must not be a hand-redrawn imitation of the template. Use a strict template-following workflow:

1. inspect all slides in `assets/sample-literature-report.pptx`;
2. use `references/sample-template-slot-manifest.json` as the bundled template slot reference, or regenerate it with `scripts/extract_template_slot_manifest.py` if the sample PPTX changes;
3. choose a source slide for every output slide;
4. create a `fallback_edit_plan.json` or `template-frame-map.json` that lists each source slide and explicit edit targets;
5. duplicate the mapped source slides into a starter deck;
6. prepare every real source figure with `scripts/prepare_fallback_figure.py` or an equivalent deterministic crop step before insertion, and record `prepared_figure_manifest.json`;
7. edit inherited text, image, table, and placeholder objects in place while preserving their original position, size, typography, crop, and frame treatment;
8. replace sample scientific content only with current paper/SI/user-provided content;
9. render the result and check overlap, clipping, sparse layout, placeholder leftovers, off-center/margin-dominated figures, and inherited-template overflow.

Use `scripts/draft_fallback_edit_plan.py` to create a first-pass `fallback_edit_plan.json` from structured slide briefs when no hand-authored plan exists. Then use `scripts/build_fallback_template_pptx.py` for fallback construction when possible. The builder accepts the edit plan, applies inherited slot edits from `references/sample-template-slot-manifest.json`, prepares source figures, emits `prepared_figure_manifest.json`, and writes a build report with overflow, ellipsis, untouched-slot, and image-preparation warnings. If this builder reports `status: "needs_review"`, fix the plan/content before delivery.

Fallback image placement must be figure-aware, not a rigid slot fill. The draft plan should profile each real paper figure or table by aspect ratio, density, and layout hint. When a wide table, wide plot, or dense multi-panel figure does not fit a single inherited image slot, the edit plan may use `fit_strategy: "adaptive_contain"` and `frame_scope: "all_image_slots"` to merge inherited image slots into one larger figure region. This is allowed only inside the mapped template slide's inherited image area and must not redraw the page from scratch, stretch the scientific image, or crop away scientific content.

For literature-report fallback decks, every content slide should include at least one real paper/SI/user-provided scientific figure, table, or source crop unless it is a true cover, ending, section divider, or explicitly documented logic-only transition. Do not let background, method, result, application, or summary pages become generic text-only slides when relevant real figures or tables are available.

Do not build fallback pages with a fresh freeform layout engine, generic card grid, oversized UI navigation, or new PowerPoint objects over the copied template when an inherited source object should be edited instead. If the tooling cannot identify editable targets or cleanly replace inherited objects, stop with planning artifacts instead of delivering a loosely redrawn deck.

Never copy the sample deck's scientific content into a new paper deck. Treat `assets/sample-literature-report.pptx` as a template/style source only; all scientific figures, claims, captions, and conclusions must come from the current paper, SI, or user-provided material.

Read `references/sample-template-intro.md`, `references/fallback-template-pptx.md`, `references/fallback-template-edit-spec.md`, and `references/sample-template-slot-manifest.json` before creating any fallback PPTX.

The fallback workflow should mirror the useful contract of `gorden-ppt-skill`: use slot IDs or explicit object addresses, preserve template typography and same-level font sizes, respect capacity hints, rewrite overly long text instead of shrinking individual boxes, and keep every output slide traceable to a source template slide.

## Core Mission

Create academic literature-report PPTs that are **clear before they are beautiful**.

The default target is a complete Chinese academic presentation deck that follows the user's sample deck rhythm while adapting to the current paper's argument.

Use the sample PPT as a visual and rhythm reference, not as a fixed set of section names. Derive the actual navigation labels and page order from the paper's domain, evidence chain, and story structure. A simple paper can use a default rhythm such as basic information, background, research idea, results, summary, and closing; a result-heavy paper should split results into meaningful sections such as design strategy, performance validation, structure evidence, mechanism explanation, application validation, or limitations.

When the user says to follow their sample PPT, do **not** invent a generic commercial deck and do not hard-code one universal navigation bar. Preserve the sample deck's navigation style, page rhythm, academic tone, and restrained red-black-gray visual language, while adapting section names to the current paper. Use `references/sample-deck-rhythm.md`, `references/adaptive-navigation.md`, and, when needed, the bundled `assets/sample-literature-report.pptx` as style references only.

## Image2-Only Route Lock

This skill is an Image2-style full-slide academic deck workflow, not a code-rendered slide engine and not an editable PowerPoint layout workflow.

For any final slide page image, redesigned page, sample page, full-deck page, or delivered PPTX:

1. Image2-style native full-slide generation is the only allowed visual generation route.
2. Each slide must be generated as one complete 16:9 full-slide image.
3. The generated image itself must already contain the title, navigation, real source figure crops, annotations, labels, notes, and page number.
4. A final PPTX, when delivered, is only a mechanical container for those accepted full-slide images.
5. Each PPT slide must contain exactly one full-slide image and no editable slide objects.

Hard stop for the authoritative Image2-only route: if Image2-style full-slide generation or an equivalent native full-slide image-generation backend is unavailable, stop before Image2-only PPTX assembly and ask whether the user accepts a fallback PPTX. Do not create a substitute deck unless the user explicitly accepts the fallback route. If accepted, the substitute must be template-based using `assets/sample-literature-report.pptx`.

Forbidden routes for the authoritative Image2-only deck include:

- Python, Pillow, Matplotlib, or any code-drawn full-slide page;
- HTML, CSS, React, or browser-rendered slide pages;
- SVG or canvas slide rendering;
- browser screenshots of coded layouts;
- native PowerPoint layouts built from editable text boxes, shapes, charts, tables, SmartArt, icons, or card grids;
- editable PPT pages rasterized afterward and presented as Image2 output;
- generic commercial PPT templates;
- decorative AI scientific diagrams replacing real paper figures.

Allowed code usage is mechanical only:

- extract or crop real figures from paper, SI, user screenshots, or user PPT pages;
- rename, organize, and version source assets;
- create contact sheets, montages, or render audits for QA;
- compress or validate images;
- package accepted full-slide images into an image-only PPTX;
- check slide count, aspect ratio, ordering, filenames, and whether editable elements exist.

Code must never be used to design or render the authoritative Image2-only final slide page. If the user explicitly accepts a fallback PPTX, code or editable PowerPoint construction may be used only to inspect the bundled template, duplicate selected template slides, and replace inherited template slots for that clearly labeled fallback deck, while still preserving real scientific figures and honest delivery labeling. Code must not hand-redraw a slide from approximate template coordinates.

## Non-Negotiable Scientific Rule

Use only **real figures from the paper, supplementary information, user-provided screenshots, or user-provided PPT pages** as scientific visuals.

Never invent, regenerate, redraw, or replace scientific content, including:

- molecular structures
- crystal structures
- microscopy images
- spectra
- XRD / NMR / IR / Raman / TG / DSC data
- adsorption curves
- reaction schemes
- mechanisms
- tables
- catalytic or performance charts
- any experimental data figure

Allowed operations are deterministic only:

- crop
- enlarge / reduce
- align
- mask margins
- add simple labels
- add thin boxes / arrows / lines
- add short callouts
- place the real figure into a 16:9 slide image

If a needed figure is not available, do not fabricate it. Use a text/logic page, ask for the source, or say the figure is missing.

## Real Figure Fidelity Lock

Image2-style generation may compose the academic slide page, but it must not invent, redraw, stylize, reinterpret, or semantically alter scientific visuals.

All scientific visuals must come from exact source crops extracted from:

- the main paper PDF;
- supplementary information / supporting information;
- user-provided screenshots;
- user-provided PPT pages;
- other explicit user-provided source images.

The image-generation prompt must instruct the backend to preserve source figure crops as faithful embedded evidence, not reinterpret them as decorative diagrams.

Never use Image2 or any other image model to fabricate, approximate, or restyle:

- molecular structures;
- crystal structures;
- microscopy images;
- spectra;
- XRD / NMR / IR / Raman / TG / DSC data;
- adsorption curves;
- reaction schemes;
- mechanisms;
- tables;
- catalytic or performance charts;
- any experimental data figure.

If the image-generation backend cannot preserve real figure crops reliably enough for academic use, stop after preparing the figure-source manifest, slide outline, page briefs, Image2 prompts, and assembly notes. Do not replace real figures with simulated charts, redrawn mechanisms, decorative scientific icons, or code-generated substitutes.

## Default Full-Deck Rule

When the user asks for a literature-report PPT from a paper:

- default to **at least 20 pages** unless the user specifies fewer pages.
- page count has no hard upper limit.
- prioritize explaining the paper clearly over compressing content.
- split dense results into multiple pages rather than crowding one slide.
- use one page for one claim whenever possible.

A 20+ page deck is acceptable if the paper has enough logic, figures, and results to support it.


## Global Deck Control Rules

For any full-deck or multi-batch image2 task, control the deck as a single presentation project, not as independent pages.

1. Derive paper-specific navigation before page design. Do not hard-code `基本信息 | 研究背景 | 研究思路 | 研究结果 | 总结启发 | Backup`; use it only as a fallback. Follow `references/adaptive-navigation.md`.
2. Create or maintain `deck_order_map.md` before image2 generation. Page order, section, navigation highlight, slide title, source figures, and mainline/backup status must come from this map. Follow `references/deck-order-map.md`.
3. Separate mainline and backup pages deliberately. Dense methods, full tables, full fitting parameters, and likely Q&A belong in backup unless they are central to the main story. Follow `references/mainline-backup-boundary.md`.
4. In multi-batch image generation, use one style contract for every batch: same aspect ratio, navigation, title scale, page-number placement, red-black-gray palette, annotation style, and figure treatment. Follow `references/batch-image-consistency.md`.
5. Use real scientific figures only. Do not add decorative vector icons or invented diagrams. Only annotate real figures with boxes, arrows, shaded regions, zoom windows, labels, and key-number callouts. Follow `references/real-figure-annotation-rules.md` and `references/trend-emphasis-rules.md`.
6. Track generation status for every slide. Do not guess which pages are complete; keep `image_generation_status.md`. Follow `references/image-generation-status.md`.
7. Assemble the PPT only from the final approved image folder. Follow `references/version-control-and-final-folder.md`, `references/pre-assembly-checklist.md`, and `references/post-assembly-render-audit.md`.
8. Authoritative final slide pages must be Image2-style full-slide images only. Code may support extraction, cropping, file naming, contact sheets, QA, compression, and image-only PPTX packaging, but code must not design or render the Image2-only final slide pages. If no Image2-style full-slide generation route is available, ask whether the user accepts a clearly labeled fallback PPTX before producing any substitute. If accepted, build the fallback from `assets/sample-literature-report.pptx`, not from a freeform code layout. Follow `references/fallback-template-pptx.md` for source-grounding, density, and layout QA rules, and follow `references/fallback-template-edit-spec.md` for the slot manifest, slide mapping, inherited-object replacement, and capacity checks.


## Iterative Refinement and Diagnosis Mode

When the user asks to continue optimizing an existing deck, diagnose before redrawing. Use `references/deck-diagnosis-mode.md` to identify page-order, navigation, style, figure-readability, claim, and speaker-readiness problems. Then use `references/redraw-priority.md` to classify slides as A: must redraw, B: local repair, or C: keep. Do not regenerate the whole deck unless the diagnosis shows global failure or the user explicitly requests a full rebuild.

If the user has accepted a version or says the version is good, treat the final page order as locked. Use `references/final-page-lock.md`; later edits should preserve slide IDs, filenames, page numbers, and navigation ranges unless the user explicitly asks to reorder the structure.

Use `references/sample-layout-grammar.md` to choose a repeatable layout type before designing each page. Use `references/figure-readability-standard.md` and `references/annotation-language.md` before accepting figure pages. Use `references/speaker-notes-to-slide-check.md` and `references/question-risk-level.md` to make sure important pages are speakable and defensible.

## Maximum-Quality Mode

When the user asks to use the strongest model, maximum quality, best possible result, or says they will provide a main paper plus SI for a complete literature-report PPT, use `references/high-quality-production-protocol.md`.

In maximum-quality mode, do not jump from paper reading directly to PPT generation. Produce or internally maintain these staged artifacts:

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
image2_manifest.json
speaker_notes.md
quality_check_report.md
deck_diagnosis_report.md
redraw_priority_plan.md
final_delivery_preview.md
final_page_montage.png
```

The default deliverable remains the final PPTX, but when feasible also return traceable support files described in `references/delivery-package.md`.

## Reading Modes

Use two related but different reading modes.

### Mode A: Interactive close reading

Use this mode when the user explicitly asks to read, translate, or analyze the paper paragraph by paragraph. Follow `references/close-reading-rules.md` strictly. Process only one original paragraph at a time, preserve the supplied English text verbatim, translate sentence-by-sentence into academically natural Mainland Chinese, then provide deep commentary. Stop after each original paragraph and wait for the user to say “继续”, “可以了”, or “下一段”.

### Mode B: PPT production reading

Use this mode when the user asks for a full literature-report PPT. Apply the same rigor internally, but do not pause after every paragraph and do not reproduce the whole paper verbatim in the final answer. Instead, transform close reading into:

- a paper logic tree;
- a main-paper + SI evidence chain;
- a figure-source manifest;
- a page-by-page PPT outline;
- slide claims and Chinese presentation copy.

For PPT generation, close reading is a source-grounding method, not a requirement to display the entire original paper text.

## Mandatory Workflow for Paper-to-PPT Tasks

Follow this sequence. Do not jump directly into slide design.

### 0. Confirm the input contract

For the user's normal workflow, expect:

- one main paper PDF;
- one corresponding supplementary information / supporting information file;
- the sample deck style, either uploaded in the conversation or bundled as `assets/sample-literature-report.pptx`.

If the main paper or SI is missing, state the limitation. Do not pretend missing material has been read.

### 1. Read the main paper and supplementary information rigorously

When the user provides both a paper PDF and supplementary information, treat them as one evidence system. Read the main paper for the argument and the SI for experimental details, controls, extra characterization, validation, and source figures.

Use close-reading discipline from `references/close-reading-rules.md`: preserve terminology, avoid paraphrase drift, track claims at sentence level when needed, and never replace close reading with vague summary.

Then extract the paper's logic before making slides:

```text
research background -> unresolved problem -> author strategy -> key methods -> key evidence -> performance/application -> conclusion -> inspiration
```

For each major result, identify:

- what question it answers
- which figure proves it
- what conclusion the audience should remember
- whether the evidence is direct, indirect, supplementary, or preliminary
- whether supporting details or figures come from the main paper or SI

### 1.5. Establish terminology and domain logic

Before writing slide copy, create or internally maintain a terminology table using `references/terminology-control.md`. Keep technical terms, sample names, abbreviations, units, and cautious claim verbs consistent across slides and speaker notes.

Identify the paper's domain pattern using `references/domain-adaptation.md` so the result section follows the right evidence chain instead of a generic figure order.

### 2. Build a figure-source manifest

Before slide generation, create or maintain an internal manifest:

```text
figure id | source page/section | content | used slide | evidence role | claim supported
```

Use this manifest to prevent fake figures, unsupported claims, and figure-message mismatch. Use `references/figure-source-manifest.md` for the full manifest fields and extraction notes, `references/figure-extraction-and-naming.md` for asset naming/cropping rules, and `references/evidence-strength.md` to calibrate how strongly each claim may be worded.

### 3. Map the paper into an adaptive sample-style deck

Use the user's sample PPT as the visual rhythm and navigation style reference, not as a fixed outline. Consult `references/sample-deck-rhythm.md`, then derive paper-specific navigation with `references/adaptive-navigation.md` and write the final page order with `references/deck-order-map.md`.

Rules:

- the navigation labels must match the current paper's argument structure;
- use 5-8 short Chinese navigation labels when possible;
- default labels such as 基本信息 / 研究背景 / 研究思路 / 研究结果 / 总结启发 are only a fallback;
- split long result sections into more informative labels such as 性能验证, 结构证据, 机理解释, 应用验证, or 局限讨论 when this helps the audience follow the logic;
- every page must map to one `section` and one `navigation_highlight` in `deck_order_map.md`;
- backup pages must have a distinct backup state and should not interrupt the mainline story.

Each section can contain multiple pages. The result and evidence sections are usually the longest.

### 4. Decide the page claim before layout

Every slide should have one core claim. Titles should be conclusion-style rather than topic-style.

Weak:

- 热稳定性
- 催化性能
- 结构表征

Better:

- 高温处理后样品仍保持特征衍射峰与介孔吸附特征
- Al/Ti 引入使该骨架从结构材料转向催化平台
- 结构模型与 STEM 共同证实 36R 直通孔道

### 5. Prepare the generation brief and page briefs

Before generating image2 pages, prepare the overall generation brief using `references/generation-brief-template.md` and then prepare one page brief per slide using `references/page-brief-template.md`.

Every page brief must specify:

- the slide's section and page type;
- its one-sentence core claim;
- exact source figure(s) or `none - logic/text page`;
- evidence strength;
- what to crop or preserve;
- Chinese slide title and copy;
- layout plan;
- risk/caution note.

If the user asked to review the outline first, pause after the brief. If the user asked for direct generation, maintain the brief internally and continue.

### 6. Generate Image2-style full-slide pages, or request fallback consent

For authoritative final PPT construction, Image2-style native full-slide generation is the only permitted slide-design route.

Required process:

1. Generate one complete 16:9 slide image for each page through Image2-style full-slide generation.
2. Each generated page image must already include the slide title, adaptive navigation, real source figure crops, annotations, labels, notes, and page number.
3. Record every accepted page in `image2_manifest.json` with `generation_route: "image2_full_slide"` and `accepted: true`.
4. Insert each accepted full-slide image into the corresponding PPT page as one full-slide image.
5. The resulting PPTX must behave like an image-based deck: stable layout, no editable slide text, no shifting objects, and no dependency on PowerPoint layout rendering.

The PPTX is only a packaging container. It is not the design surface.

Allowed code usage is strictly mechanical:

- extract or crop real paper / SI / user-provided figures;
- rename and organize source assets;
- create contact sheets or rendered montages for QA;
- compress images;
- package accepted PNG/JPG slide images into an image-only PPTX;
- validate page count, aspect ratio, filenames, ordering, and editable-object absence.

Forbidden routes for the authoritative Image2-only deck:

- HTML/CSS/React slide rendering;
- SVG/canvas slide rendering;
- Python/Pillow/Matplotlib slide drawing;
- browser screenshots of coded layouts;
- native PowerPoint layout construction with editable text boxes, shapes, charts, tables, SmartArt, icons, or card grids;
- rasterizing an editable PPT after designing it as normal slides;
- generic commercial templates;
- decorative AI diagrams that replace real scientific figures.

Hard stop for Image2-only delivery: if Image2-style full-slide generation or an equivalent native full-slide image-generation backend is unavailable, stop before Image2-only PPTX assembly and ask whether the user accepts a lower-fidelity fallback PPTX. Do not generate a substitute academic deck unless the user explicitly accepts that fallback route. If accepted, the fallback must adapt `assets/sample-literature-report.pptx` as the template/style source.

### 7. Assemble the Image2-only PPT

Assemble the PPT only after accepted Image2-style full-slide images exist.

Rules:

- Place exactly one final full-slide image on each PPT slide.
- The image must fill the full 16:9 slide canvas.
- Do not add editable PowerPoint text, shapes, charts, tables, icons, SmartArt, or extra annotations on top of the image.
- Do not use PowerPoint as the visual design tool.
- Do not use code-rendered pages as substitutes for Image2-style generated pages in the authoritative Image2-only deck.
- PPT packaging is a mechanical container step only.

Before packaging, confirm `image2_manifest.json` exists and every slide is accepted from the Image2 full-slide route. After packaging, run `scripts/validate_image_only_pptx.py` and block delivery if validation fails.

The final PPT must be image-only. If editable elements are present, the deck fails this skill's output contract.

### 7.5. Prepare speaker notes, backup slides, and question preparation when quality matters

For maximum-quality tasks, prepare speaker notes using `references/speaker-notes-template.md`. Notes should include the spoken purpose, a 30-60 second Chinese script for important slides, transition sentences, likely questions, and safe answers.

Use `references/question-prep.md` to prepare likely teacher/advisor questions and cautious answers. Use `references/backup-slides.md` to decide whether dense SI evidence, methods, controls, or full source panels should be appended as backup slides.

### 7.6. Output editability boundary

This skill's default and authoritative deliverable is an image-only PPTX assembled from Image2-style full-slide images.

Do not create an editable PPTX as a fallback when Image2-style generation is unavailable unless the user explicitly accepts a lower-fidelity fallback route after seeing the Image2 boundary.

If the user explicitly asks for editable slides, explain the boundary:

- this skill is optimized for stable Image2-style academic slide images;
- editable PPT construction is a different, lower-fidelity workflow;
- editable reconstruction may lose the visual quality, stability, and figure-fidelity guarantees of this skill;
- the current skill may provide page briefs, figure placement plans, and Image2 prompts;
- if the user still wants a PPTX without Image2, the assistant may produce a clearly labeled template-based fallback deck only after explicit consent.

Never claim an editable PPT exists unless it was actually produced through a separate editable-slide workflow. Do not use editable slides as an intermediate step and then rasterize them as if they were Image2 output. Any editable fallback deck must remain labeled as fallback output and must follow the bundled sample template.

### 8. Final check

Before delivering, apply `references/quality-gates.md` and verify:

- every scientific visual is from the paper/SI/user source.
- verify each slide has one main claim.
- verify at least 20 pages for full literature-report decks unless user requested fewer.
- verify no page is crowded with too many equal-weight figures.
- verify navigation, page numbers, and section labels are consistent and match `deck_order_map.md`.
- verify the final PPT is assembled from the approved final image2 folder only.
- verify a rendered montage or equivalent page audit has checked order, navigation, and style continuity.
- verify result claims do not exceed the paper's evidence.
- verify every final PPT slide contains exactly one full-slide image.
- verify slidesWithEditableText = 0.
- verify there are no editable PowerPoint text boxes, shapes, charts, tables, icons, SmartArt, or extra annotations.
- verify no final page was created through Python/Pillow/Matplotlib, HTML/CSS/React, SVG/canvas, browser screenshots, or native editable PowerPoint construction.
- verify code was used only for extraction, cropping, file organization, QA, compression, validation, or image-only PPTX packaging.
- verify Image2-style full-slide generation was used for every final slide image.
- verify `image2_manifest.json` exists and every slide has `generation_route: "image2_full_slide"` and `accepted: true`.
- verify `scripts/validate_image_only_pptx.py` passed on the final PPTX, with manifest validation when available.
- verify the final response includes the mandatory delivery statement.
- if Image2-style generation was unavailable, verify no Image2-only PPTX was delivered; only outlines, page briefs, prompts, assembly notes, or a user-approved fallback PPTX may be delivered.

## Deck Structure Template

Use this as a fallback for a normal paper presentation, not as a fixed universal structure. Adapt section labels and page order using `adaptive-navigation.md` and `deck-order-map.md`. Keep at least 20 pages for full decks unless the user requests fewer.

```text
1. 封面：论文题目、中文题目、作者、期刊、DOI、汇报人/日期
2. 基本信息：研究对象、核心指标、摘要式贡献
3. 基本信息：论文核心贡献拆解
4. 研究背景：领域需求/应用场景
5. 研究背景：已有方法或材料的不足
6. 研究背景：本文要解决的核心矛盾
7. 研究思路：作者的总体设计路线
8. 研究思路：关键材料/方法/假设
9. 研究结果：合成/制备/样品获得
10. 研究结果：结构或组成证据 1
11. 研究结果：结构或组成证据 2
12. 研究结果：形貌/微观/直接观察证据
13. 研究结果：孔道/界面/性能基础表征
14. 研究结果：稳定性或可靠性验证
15. 研究结果：功能位点/机理证据
16. 研究结果：核心性能测试
17. 研究结果：对比性能或优势来源
18. 研究结果：循环/拓展/应用验证
19. 论文总结：本文贡献三点
20. 论文启发：方法、局限、可借鉴点
21. 汇报完毕：致谢页
```

If the paper is complex, split pages 9-18 into more detailed evidence pages.

## Slide Style Rules

Default visual language:

- white or very light gray background
- red-black-gray academic palette
- deep academic red for active section, keywords, and minimal figure annotation
- large conclusion title
- dominant real figure
- short text, usually 2-3 points
- high whitespace
- simple thin lines
- no decorative icons unless they already exist in the source material

Avoid:

- commercial poster style
- dense dashboard/card grids
- excessive shadows
- gradients / glow / 3D effects
- AI-style decorative technology backgrounds
- invented schematic art
- over-designed infographics

## Page Anatomy

For most content slides:

```text
[top navigation derived from the paper-specific navigation plan]
[one-line conclusion title]

[large real paper figure / carefully cropped figure group]
[direct annotations: short labels, thin boxes, arrows]

[2-3 short notes, only if needed]
[page number]
```

Prefer figure-first layouts:

1. one large real figure + short takeaway
2. large real figure + 2-3 notes
3. two real figures stacked only when one is source and the other is evidence
4. top source strip + bottom evidence figure
5. three columns only for true comparisons
6. process row only for true methodology / logic route pages

## Slide Type Patterns

### Pattern A: Evidence Slide

Use when the slide proves a result from a paper figure.

```text
[结论型标题]

[大图：论文关键图，带框/箭头/标签]

结论：……
证据：……
```

### Pattern B: Comparison Slide

Use when the slide compares materials, samples, conditions, or performance.

```text
[标题直接说出谁更优/差异在哪里]

[主图：对比图或表格裁剪]
[标注：关键样品、关键数值、关键趋势]

这张图说明：……
```

### Pattern C: Logic / Route Slide

Use when explaining the research route or mechanism, but only with real source visuals or simple PPT text flow.

```text
[路线标题]

问题 -> 设计 -> 验证 -> 应用

每一步只写一个关键词和一句解释。
```

### Pattern D: Background Gap Slide

Use when explaining why the paper is needed.

```text
[核心矛盾标题]

已有研究/材料 A：优势 + 不足
已有研究/材料 B：优势 + 不足
本文切入点：……
```

### Pattern E: Summary / Inspiration Slide

Use at the end.

```text
论文总结
1. 本文做出了什么新对象/新方法
2. 用哪些证据证明它成立
3. 它带来了什么功能或启发

论文启发
1. 方法启发
2. 表征启发
3. 局限与后续问题
```

## Scientific Copy Rules

Write like a graduate student explaining a journal-club slide.

Prefer:

- “共同证实” for two independent lines of evidence.
- “直接观察到” only for microscopy/direct imaging.
- “表明 / 说明 / 支持” for normal evidence.
- “初步表明” for limited tests.
- “优势在于……” for performance interpretation.
- “不是……而是……” to clarify logic.

Avoid overstating:

- do not say “工业化可用” unless the paper proves industrial deployment.
- do not say “完全稳定” if only limited stability tests are shown.
- do not claim “机理明确” if the paper only proposes a mechanism.
- do not call a result “最优” unless the figure directly supports that comparison.
- do not translate every English term mechanically; keep accepted terms like STEM, PXRD, XPS, BET when useful.

## Failure Behavior When Image2 Is Unavailable

When the user asks for final slide images or a complete PPTX, but Image2-style full-slide generation is unavailable, do not silently attempt a substitute production route.

First explain the Image2 boundary and ask whether the user accepts a lower-fidelity fallback PPTX. If the user does not explicitly accept fallback output, deliver the highest-value non-image outputs that are still valid under this skill:

1. paper logic tree;
2. main-paper + SI crosswalk;
3. figure-source manifest;
4. adaptive navigation plan;
5. deck_order_map;
6. page-by-page outline;
7. page briefs;
8. Image2 prompts;
9. image-only assembly notes;
10. QA checklist.

Use a clear boundary statement: the current environment does not provide an Image2-style full-slide generation route, so this skill cannot create the authoritative Image2-only PPTX. Ask the user to choose between non-image planning artifacts and a clearly labeled fallback PPTX based on `assets/sample-literature-report.pptx`. If the current paper/SI or user-provided real figures are missing, say that a real fallback PPTX cannot be produced yet and ask for the missing source material.

If the user accepts the fallback route, create only a clearly labeled, source-grounded, template-based fallback PPTX. Do not claim it is Image2-only, do not claim Image2 validation passed, and do not list `image2_manifest.json` unless it actually exists for a real Image2 workflow. Do not apologize repeatedly.

## Output Behavior

### When the user asks for a full PPT from a paper

Provide, or internally create before generation:

1. paper logic tree
2. main-paper + SI crosswalk
3. figure-source manifest
4. adaptive navigation plan and deck_order_map.md
5. page-by-page outline with at least 20 pages
6. one page brief per slide
7. image2 generation plan and image_generation_status.md
8. speaker notes when quality mode is requested
9. final PPT assembled from the approved final image2 folder
10. rendered montage / post-assembly audit
11. quality check report
12. deck diagnosis report when refining an existing deck
13. final delivery preview before the final response

If outputting the authoritative Image2-only artifact, return the final PPTX only after Gates A-D pass. If Image2 is unavailable, follow Gate E before creating any fallback PPTX. In maximum-quality mode, also prepare the support deliverables in `references/delivery-package.md` when feasible; never claim a support file exists if it was not actually produced. Use `references/failure-recovery.md` whenever a source, figure, or deliverable cannot be produced cleanly.

### When the user asks for slide advice only

Output:

1. page type
2. one-sentence claim
3. figure placement
4. revised slide copy
5. what to remove

### When the user asks to redesign one page

Output one Image2-style 16:9 full-slide page image if Image2-style generation is available. Keep the scientific visuals real and sourced from the user-provided material.

If Image2-style generation is not available, ask whether the user accepts a fallback redesign. Without explicit fallback consent, output only:

1. diagnosis of the current page;
2. revised one-sentence claim;
3. real figure placement plan;
4. corrected Chinese slide copy;
5. Image2 prompt for the redesigned page.

Do not create the authoritative redesigned page with Python, HTML, CSS, React, SVG, canvas, browser screenshots, Matplotlib, Pillow, or editable PowerPoint objects. If the user explicitly accepts a fallback redesign, label it as fallback output.

## Required Checklist

Use `references/style-checklist.md` before finalizing any page.

Use `references/paper-to-ppt-workflow.md` for full literature-report decks.

Use `references/sample-deck-rhythm.md` when following the user's sample literature-report PPT style.

Use `references/sample-style-spec.md` to keep visual parameters close to the bundled sample deck.

Use `references/high-quality-production-protocol.md` when the user asks for maximum-quality or strongest-model output.

Use `references/generation-brief-template.md` before building a full deck.

Use `references/page-brief-template.md` before generating each image2 page.

Use `references/image2-execution-gate.md` before any final image or PPTX production attempt.

Run `scripts/validate_image_only_pptx.py` before delivering any PPTX.

Use `references/fallback-template-pptx.md` before creating any non-Image2 fallback PPTX.

Use `references/fallback-template-edit-spec.md` before editing, replacing, or adding any object in a non-Image2 fallback PPTX.

Use `references/main-si-crosswalk.md` to connect main-paper claims with SI support.

Use `references/close-reading-rules.md` when the task requires rigorous paper reading or when building a PPT from a main paper plus SI.

Use `references/terminology-control.md` to keep technical terms, sample names, units, and claim verbs consistent.

Use `references/domain-adaptation.md` to adapt the result evidence chain to the paper type.

Use `references/failure-recovery.md` when files, figures, SI pages, or evidence are missing, unreadable, contradictory, or insufficient.

Use `references/backup-slides.md` when dense SI evidence should be moved to backup pages instead of cluttering the main story.

Use `references/question-prep.md` to prepare likely teacher/advisor questions and safe answers.

Use `references/editable-output-options.md` when the user asks for editable PPT output or both stable and editable versions.

Use `references/final-scoring-rubric.md` to score final quality in maximum-quality mode.

Use `references/figure-source-manifest.md` when tracking real figure use.

Use `references/figure-extraction-and-naming.md` when extracting, cropping, or naming paper figure assets.

Use `references/evidence-strength.md` to calibrate claim wording.

Use `references/speaker-notes-template.md` when creating oral presentation notes.

Use `references/delivery-package.md` for maximum-quality final deliverables.



Use `references/adaptive-navigation.md` to derive paper-specific navigation labels instead of hard-coding sample-section names.

Use `references/deck-order-map.md` to lock final page order, navigation highlight, page title, source figures, and mainline/backup status before image2 generation.

Use `references/mainline-backup-boundary.md` to separate main story pages from backup evidence pages.

Use `references/batch-image-consistency.md` to keep multi-batch image2 pages visually consistent.

Use `references/real-figure-annotation-rules.md` before annotating or generating any scientific figure page.

Use `references/trend-emphasis-rules.md` to extract key trends, numbers, and speaking cues from each figure before layout.

Use `references/image-generation-status.md` to track which slide images are generated, accepted, redrawn, and included in the final deck.

Use `references/version-control-and-final-folder.md` to prevent old generated pages from entering the final PPT.

Use `references/pre-assembly-checklist.md` before assembling the PPTX.

Use `references/post-assembly-render-audit.md` after assembling the PPTX.

Use `references/full-deck-reorder-mode.md` when the user asks to keep the full page count but fix order, categories, navigation, or style consistency.

Use `references/quality-gates.md` before final delivery.
