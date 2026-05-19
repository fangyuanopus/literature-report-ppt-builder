---
name: academic-slide-minimalist
description: use this skill when the user wants to create, redesign, critique, or generate academic research ppt slides, literature-report decks, thesis-defense slides, journal-club presentations, ppt page images, slide copy, or full paper-to-ppt workflows. especially use it when the user provides a paper pdf plus supplementary information, asks to follow a sample deck/template, says image2, wants at least 20 pages, needs adaptive navigation, wants a reordered full deck, requires real paper figures only, or wants rigorous close reading before slide generation. first read the paper and si, build logic/evidence maps and a deck-order map, derive paper-specific navigation, create 16:9 slide images, assemble the ppt, and audit page order/style without inventing scientific visuals.
---

# Academic Slide Minimalist

## Core Mission

Create academic literature-report PPTs that are **clear before they are beautiful**.

The default target is a complete Chinese academic presentation deck that follows the user's sample deck rhythm while adapting to the current paper's argument.

Use the sample PPT as a visual and rhythm reference, not as a fixed set of section names. Derive the actual navigation labels and page order from the paper's domain, evidence chain, and story structure. A simple paper can use a default rhythm such as basic information, background, research idea, results, summary, and closing; a result-heavy paper should split results into meaningful sections such as design strategy, performance validation, structure evidence, mechanism explanation, application validation, or limitations.

When the user says to follow their sample PPT, do **not** invent a generic commercial deck and do not hard-code one universal navigation bar. Preserve the sample deck's navigation style, page rhythm, academic tone, and restrained red-black-gray visual language, while adapting section names to the current paper. Use `references/sample-deck-rhythm.md`, `references/adaptive-navigation.md`, and, when needed, the bundled `assets/sample-literature-report.pptx` as style references only.

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

### 6. Generate image2 pages first

For final PPT construction, use the user's preferred image2 workflow:

1. create one complete 16:9 slide image for each page.
2. each image should already include title, navigation, figures, labels, notes, and page number.
3. insert those images into corresponding PPT pages.
4. do not rebuild the deck as many editable PPT text boxes unless the user specifically asks.

The generated PPT should behave like an image-based deck: stable layout, consistent style, low risk of element shifting.

### 7. Assemble the PPT

Place each image2 page full-slide into the PPT in order.

Keep the deck structure and visual rhythm close to the user's sample. Do not switch to a generic commercial template.

### 7.5. Prepare speaker notes, backup slides, and question preparation when quality matters

For maximum-quality tasks, prepare speaker notes using `references/speaker-notes-template.md`. Notes should include the spoken purpose, a 30-60 second Chinese script for important slides, transition sentences, likely questions, and safe answers.

Use `references/question-prep.md` to prepare likely teacher/advisor questions and cautious answers. Use `references/backup-slides.md` to decide whether dense SI evidence, methods, controls, or full source panels should be appended as backup slides.

### 7.6. Choose output editability deliberately

Default to the user's preferred image2-based stable deck. Use `references/editable-output-options.md` only when the user asks for an editable deck or when a dual stable/editable package is clearly useful. Never claim an editable PPT exists unless it was actually produced.

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

If outputting an artifact, return the final PPTX. In maximum-quality mode, also prepare the support deliverables in `references/delivery-package.md` when feasible; never claim a support file exists if it was not actually produced. Use `references/failure-recovery.md` whenever a source, figure, or deliverable cannot be produced cleanly.

### When the user asks for slide advice only

Output:

1. page type
2. one-sentence claim
3. figure placement
4. revised slide copy
5. what to remove

### When the user asks to redesign one page

Output a 16:9 PPT-ready page image if possible. Keep the scientific visuals real and sourced from the user-provided material.

## Required Checklist

Use `references/style-checklist.md` before finalizing any page.

Use `references/paper-to-ppt-workflow.md` for full literature-report decks.

Use `references/sample-deck-rhythm.md` when following the user's sample literature-report PPT style.

Use `references/sample-style-spec.md` to keep visual parameters close to the bundled sample deck.

Use `references/high-quality-production-protocol.md` when the user asks for maximum-quality or strongest-model output.

Use `references/generation-brief-template.md` before building a full deck.

Use `references/page-brief-template.md` before generating each image2 page.

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
