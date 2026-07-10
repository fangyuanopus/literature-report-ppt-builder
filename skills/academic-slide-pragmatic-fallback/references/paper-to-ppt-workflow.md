# Paper-to-PPT Workflow

Use this reference for full literature-report PPT generation.

For maximum-quality runs, also follow `high-quality-production-protocol.md`. The strongest workflow is staged: close reading, logic tree, main-SI crosswalk, figure manifest, slide outline, page briefs, image2 generation, PPT assembly, speaker notes, and final quality report.

## 1. Intake

Inputs may include:

- paper PDF
- supplementary information PDF
- paper figures/screenshots
- user sample PPT
- user notes or desired focus

Treat the sample PPT as a structure and style reference, not as a scientific source unless the user says so. If the bundled sample exists, consult `sample-deck-rhythm.md` before planning pages.

## 1.1 Required Reading Discipline

Before planning slides, apply the close-reading rules in `close-reading-rules.md`. For a full PPT task, do not output the whole close reading unless requested. Instead, use it to create a faithful logic tree and evidence map.

When both main paper and SI are uploaded, never rely on the main paper alone. The SI must be scanned for:

- experimental details and synthesis conditions
- control experiments
- additional characterization
- stability or recycling tests
- expanded performance comparisons
- raw/extended figures and tables
- figure panels that support slide-level claims

## 1.2 Terminology and Domain Setup

Before writing slide titles or copy, use `terminology-control.md` to create a terminology table. Use `domain-adaptation.md` to choose the right evidence-chain order for the paper type.

If a file, figure, or SI page is missing or unreadable, use `failure-recovery.md` before proceeding.

## 1.3 Adaptive Navigation and Deck Order

Before writing slide outlines, derive paper-specific navigation using `adaptive-navigation.md`. The sample deck's top navigation style should be copied visually, but the section labels should come from the current paper's structure.

Then create `deck_order_map.md` using `deck-order-map.md`. This map is the source of truth for final page numbers, section labels, navigation highlights, mainline/backup status, source figures, and final image filenames.

For result-heavy papers, split a generic `研究结果` section into more useful labels such as `性能验证`, `结构证据`, `机理解释`, `应用验证`, or domain-appropriate alternatives.

## 2. Paper Logic Tree

Extract the following from the main paper first, then enrich it with SI evidence:

```text
1. research object
2. research background
3. unresolved problem
4. author's hypothesis or design idea
5. experimental / computational route
6. key evidence chain
7. performance or application result
8. conclusion
9. limitations and inspiration
```

For Chinese literature reports, write the logic in clear academic presentation language, not in dense paper language.

## 3. Evidence Chain

For each result, identify:

```text
question -> figure evidence -> interpretation -> page claim
```

Example:

```text
question: is the target pore structure real?
figure evidence: Fig. 2B-E, STEM + structural model
interpretation: model and direct imaging show aligned pore channels
page claim: 结构模型与 STEM 共同证实 36R 直通孔道
```

## 4. Page Count Strategy

Default full deck: at least 20 pages.

Do not force one result category into one page. Split when needed:

- synthesis route
- phase confirmation
- microscopic morphology
- structure refinement
- porosity / pore size
- stability
- composition / active sites
- performance
- comparison
- mechanism or discussion
- recycling / robustness

## 5. Default Page Allocation

```text
1 cover
2 paper information
3 core contribution overview
4 background: field need
5 background: existing limitation
6 background: core contradiction
7 research idea: overall route
8 research idea: key design
9 method/synthesis overview
10 result: sample/phase formation
11 result: structure evidence 1
12 result: structure evidence 2
13 result: morphology/direct observation
14 result: property/porosity/basic characterization
15 result: stability/reliability
16 result: active site/composition evidence
17 result: performance result 1
18 result: performance comparison
19 result: mechanism/advantage explanation
20 result: recycling/application extension
21 paper summary
22 inspiration and limitations
23 closing page
```

Add or remove pages only if the paper logic requires it, but do not go below 20 for a full deck unless requested.

## 6. Page Briefs and Image2 Production

Before image2 production, prepare one page brief per slide using `page-brief-template.md`. A slide should not be generated until its core claim, source figure, evidence strength, crop plan, and layout plan are clear.

Each page should be exported as a complete 16:9 image.

Each image includes:

- adaptive top navigation from `deck_order_map.md`
- title
- real figure(s)
- annotations
- short notes
- page number

Use `figure-extraction-and-naming.md` when extracting or cropping assets. Then insert each image into a blank PPT page as the full-slide background/content.

## 7. Pre-Generation Brief and Outline

Use `generation-brief-template.md` to prepare the logic tree, evidence chain, manifest preview, page outline, and risk notes before image2 production.

## 7.1 Pre-Generation Outline

Before generating image2 pages, prepare a page-by-page outline:

```text
slide number | navigation section | navigation highlight | mainline/backup | conclusion-style title | main paper figure(s) | SI figure(s) | page purpose
```

For at least 20-page decks, make sure background, research idea, results, summary, and inspiration are all represented. Do not compress the results section if more pages are needed to explain the evidence chain clearly.

## 8. Speaker Notes, Backup Slides, and Question Prep

For maximum-quality runs, prepare Chinese speaker notes using `speaker-notes-template.md`. At minimum, include notes for all background transition pages, research idea pages, key evidence pages, performance pages, summary pages, and likely-question pages.

Use `question-prep.md` to prepare likely teacher/advisor questions and safe answers. Use `backup-slides.md` to decide which dense SI materials should become backup slides instead of crowding the main story.

## 8.5 Output Format Options

Default to stable image2-based PPT. Use `editable-output-options.md` only if the user requests editable slides or dual output.

## 8.8 Image Status, Final Folder, and Assembly Control

Use `image-generation-status.md` after each image2 batch. Use `version-control-and-final-folder.md` to copy only accepted pages into `image2_pages_unified_final/` with final sequential names. Use `pre-assembly-checklist.md` before creating the PPT.

## 8.9 Post-Assembly Audit

After creating the PPT, use `post-assembly-render-audit.md` to check the complete deck order, navigation, page numbers, and style consistency. Create a montage when feasible and fix global issues before delivery.

## 9. Quality Gates

Before delivery, apply `quality-gates.md`. If any gate fails, either fix the issue or explicitly report the limitation instead of silently proceeding. Use `final-scoring-rubric.md` to score the final deck in maximum-quality mode.

## 10. Delivery

Return the final PPTX. In maximum-quality mode, use `delivery-package.md` to prepare support deliverables when feasible. If the user asks, also return the image2 PNG files or a ZIP of them.

## 8.10 Existing Deck Refinement

If the task is to improve a current deck rather than create one from scratch, use `deck-diagnosis-mode.md` first. Then apply `redraw-priority.md`, `final-page-lock.md`, `sample-layout-grammar.md`, `figure-readability-standard.md`, `annotation-language.md`, and `speaker-notes-to-slide-check.md`. Keep accepted page order locked unless the user explicitly asks for a structural reorder.
