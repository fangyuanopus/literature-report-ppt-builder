# Quality Gates for Literature-Report PPT Generation

Use these gates to prevent common failures before delivering a PPT.

## Gate 1: File Intake Gate

Pass only if:

- the main paper has been identified;
- the SI / supplementary file has been identified when provided;
- the sample deck is treated as style reference, not scientific content;
- missing files or unreadable pages are explicitly noted.

Fail response:

```text
当前缺少/无法读取：[file or pages]. 我不能把未读材料当作已读内容。可先基于已读材料生成大纲，或请补充文件。
```

## Gate 2: Close-Reading Gate

Pass only if:

- the paper's research object, problem, strategy, evidence, and conclusion are clear;
- main claims are separated from interpretation and speculation;
- SI evidence has been checked for methods, controls, and supplementary figures;
- technical terms, sample names, units, and conditions are preserved.

## Gate 3: Figure Integrity Gate

Pass only if:

- every scientific visual comes from the main paper, SI, or user-provided screenshots;
- each used figure appears in the manifest;
- axes, legends, scale bars, units, and sample names are preserved when scientifically necessary;
- no figure is redrawn or AI-generated as a scientific substitute;
- cropping does not change the scientific meaning.

## Gate 4: Story and Page Gate

Pass only if:

- the deck follows the sample structure: 基本信息 -> 研究背景 -> 研究思路 -> 研究结果 -> 总结启发;
- the full deck has at least 20 pages unless the user requested fewer;
- each slide has one main claim;
- dense results are split across multiple pages;
- the results section follows an evidence chain rather than random figure order.

## Gate 5: Image2 Layout Gate

Pass only if each page image:

- is 16:9;
- includes navigation, title, figure(s), short notes, and page number when applicable;
- uses red-black-gray academic style;
- keeps one dominant figure or one clear evidence block;
- avoids decorative icons, commercial templates, gradients, glows, and fake diagrams.

## Gate 5.5: Image2 Execution and Manifest Gate

Pass only if:

- Image2-style full-slide generation availability was explicitly confirmed before final page generation;
- `image2_manifest.json` exists before PPTX assembly;
- every final slide image is listed in the manifest;
- every manifest entry has `generation_route: "image2_full_slide"` and `accepted: true`;
- every final image path in the manifest exists;
- no page image was produced by Python, Pillow, Matplotlib, HTML/CSS, SVG/canvas, browser screenshots, editable PowerPoint layouts, templates, or rasterized editable slides.

If this gate fails, do not deliver an Image2-only PPTX. Explain the boundary and ask whether the user accepts a clearly labeled lower-fidelity fallback PPTX based on `assets/sample-literature-report.pptx`. Without explicit fallback consent, deliver only reading outputs, page briefs, Image2 prompts, and assembly notes.

## Gate 6: Final PPT Assembly Gate

Pass only if:

- image2 pages were inserted full-slide into PPT pages;
- `scripts/validate_image_only_pptx.py` passes on the final PPTX, with manifest validation when available;
- the final PPTX has exactly one full-slide picture per slide and zero editable slide objects;
- page order matches the approved/internal outline;
- navigation active section and page numbers are consistent;
- no slide is blank, duplicated by accident, or missing from the page count;
- the final PPTX opens and contains the expected number of slides.

## Gate 6.5: Fallback Template PPTX Gate

Use this gate only when Image2 is unavailable and the user explicitly accepted fallback output.

Pass only if:

- `assets/sample-literature-report.pptx` was used through a template-following workflow, not as a loose visual inspiration;
- all source template slides were inspected before choosing layouts;
- `template_slot_manifest.json` or an equivalent slot manifest records inherited source-slide roles, text/image/table slots, object addresses, capacity hints, figure frames, and template chrome;
- `fallback_edit_plan.json` or an equivalent edit plan records selected slides, slide mapping, replacement text, replacement figures, keep/delete decisions, and exceptions;
- `scripts/draft_fallback_edit_plan.py` was used to create the first-pass plan from slide briefs when no hand-authored edit plan existed, or the QA report explains the manual planning route;
- `fallback_plan_report.json` or an equivalent plan report records source-slide selection, figure-slot fit, mapped edits, deletion count, and planning warnings;
- every inserted figure/table has a figure profile or equivalent record of aspect ratio/layout hint, and source-slide selection considers that profile rather than only the number of image slots;
- every non-cover/non-ending content slide uses at least one real paper/SI/user-provided figure, table, or source crop when suitable source visuals are available, or the QA report explains why the slide is intentionally logic-only;
- `scripts/build_fallback_template_pptx.py` was used when the deck can be expressed as source-slide selection plus inherited slot edits, or the QA report explains why it could not be used;
- `fallback_build_report.json` or an equivalent build report records text edits, image edits, prepared figures, overflow warnings, ellipsis warnings, image-frame warnings, and untouched replaceable slots;
- the build report status is `passed`, or every `needs_review` warning has been fixed or explicitly documented as an unresolved limitation;
- `fallback_structural_audit.json` or an equivalent structural audit exists when visual render QA is unavailable;
- a rendered contact sheet exists for fallback PPTX visual QA when the local platform can render PPTX pages; on macOS, use `scripts/render_pptx_quicklook_contact_sheet.py`;
- every output slide is mapped to a source slide in `template-frame-map.json` or an equivalent map;
- content-bearing slides define explicit inherited-object edit targets; they are not marked preserve-only;
- mapped source slides were duplicated into a starter deck before editing;
- inherited text, image, table, caption, footer, navigation, and placeholder objects were edited, replaced, or deleted intentionally while preserving their source position, size, typography, crop, and frame treatment rather than covered by new overlays;
- new objects are documented exceptions, not the main layout mechanism;
- the deck is grounded in the current paper, SI, or user-provided real source figures;
- no mock figure, invented scientific chart, decorative scientific diagram, or sample-deck scientific content is used as evidence;
- `figure_source_manifest.md` lists every figure used in the fallback deck;
- `prepared_figure_manifest.json` or an equivalent manifest lists every inserted source figure after deterministic margin trimming/preparation;
- every inserted paper/SI/user figure uses the prepared crop rather than the raw PDF/screenshot crop when the raw asset has excess margins;
- rendered QA confirms the actual scientific content inside each image frame is visually centered/readable, not pushed off-center by retained page margins or screenshot borders;
- wide tables, portrait diagrams, and dense multi-panel figures are placed in regions that match their shape, using documented adaptive placement within inherited image regions when necessary;
- normal content pages use the main canvas deliberately and are not sparse card-only layouts;
- template cleanup removed old sample scientific content, empty placeholders, and unused shapes that occupy figure or text space;
- cleanup did not delete a grouped object that contains a reused real-paper figure, caption, or body text slot;
- navigation follows the sample deck's quiet academic style and is not rendered as oversized generic UI buttons;
- figure-led pages have a dominant readable figure region with no empty card or leftover shape sitting below the figure;
- rendered QA or equivalent visual inspection found no unintended text overlap, clipping, unreadable figures, or navigation/page-number collisions;
- overflow/canvas-boundary checks pass, or any inherited source-template overflow is fixed, remapped to a cleaner source slide, or explicitly documented as inherited template overflow without new content overflow;
- the final response clearly states that Image2-only validation is not applicable.

If this gate fails, do not deliver the fallback PPTX as a formal literature-report deck. Fix the layout/source problem or deliver planning artifacts only.

## Gate 7: Claim Calibration Gate

Check slide language:

- use “表明/说明/支持” for normal evidence;
- use “直接观察到” only for direct imaging/observation;
- use “初步表明/可能与……有关” for limited or indirect evidence;
- do not say “证明机理” when the paper only proposes a mechanism;
- do not say “工业化可用” unless the paper proves industrial deployment;
- do not say “最优” unless the comparison directly supports it.

## Gate 8: Page Brief Gate

Pass only if:

- every slide has a page brief before image2 generation;
- every page brief has one core claim;
- every scientific visual has a source figure and asset filename when extracted;
- evidence strength is labeled;
- risk/caution notes prevent overclaiming.

## Gate 9: Speaker Notes Gate

For maximum-quality tasks, pass only if:

- key slides have 30-60 second Chinese speaker notes;
- transition sentences explain how the story moves forward;
- likely questions and safe answers are prepared for major evidence and limitation slides;
- notes do not exaggerate beyond the paper.

## Gate 10: Delivery Package Gate

For maximum-quality tasks, pass only if the final response clearly states which deliverables were produced:

- final PPTX, only if Image2 and validation gates passed;
- image2 pages, if produced;
- image2_manifest.json, if a PPTX was delivered;
- figure manifest;
- page briefs;
- speaker notes;
- quality report.

Do not mention a deliverable as complete unless it actually exists.


## Gate 11: Terminology Consistency Gate

Pass only if:

- key technical terms have consistent Chinese translations;
- sample names, abbreviations, chemical formulas, and units are preserved;
- claim verbs match evidence strength;
- slide copy and speaker notes use the same terminology.

## Gate 12: Failure Recovery Gate

Pass only if:

- missing or unreadable files/pages/figures are reported rather than hidden;
- unsupported claims are removed or weakened;
- low-resolution or ambiguous figures are not used as decisive evidence;
- any unresolved limitation appears in the quality report.

## Gate 13: Backup and Question-Prep Gate

For maximum-quality tasks, pass only if:

- useful SI evidence that would clutter the main deck is moved to backup slides or a backup plan;
- likely teacher/advisor questions are prepared for key claims, weak evidence, and limitations;
- safe answers cite the paper/SI evidence and do not invent experiments.

## Gate 14: Editable Output Honesty Gate

Pass only if:

- the final response clearly distinguishes stable image2-based PPT from optional editable PPT;
- an editable deck is mentioned only if it was actually produced;
- the stable deck remains the authoritative presentation version unless the user requests otherwise.

## Gate 15: Final Scoring Gate

For maximum-quality tasks, include a final score using `final-scoring-rubric.md` in the quality report. Do not give a high score if figure sources are not traceable, SI was ignored, or major claims are overworded.


## Gate 16: Adaptive Navigation Gate

Pass only if:

- navigation labels are derived from the current paper or explicitly accepted as the fallback;
- all slides use the same navigation labels in the same order;
- the active navigation highlight matches each slide's role;
- result-heavy papers split generic `研究结果` into clearer labels when useful;
- backup slides use a distinct Backup state.

## Gate 17: Deck Order Map Gate

Pass only if:

- `deck_order_map.md` exists for full decks;
- final page numbers, image filenames, source figures, and mainline/backup status are recorded;
- PPT assembly follows this map, not generation order.

## Gate 18: Batch Image Consistency Gate

Pass only if:

- every image batch uses the same style contract;
- every page has consistent title, navigation, footer, page number, and annotation style;
- `image_generation_status.md` identifies generated, accepted, redrawn, and final-assembled slides.

## Gate 19: Pre/Post Assembly Audit Gate

Pass only if:

- pre-assembly checks confirm all accepted images exist in the final image folder;
- the final PPT is assembled only from the approved final image folder;
- a rendered montage or equivalent whole-deck audit checks page order, navigation, page numbers, and style continuity.

## Gate 20: Diagnosis and Redraw Priority Gate

Pass only if refinement tasks first diagnose the current deck and classify pages using A/B/C redraw priority before major regeneration. Do not redraw C pages unless the user asks.

## Gate 21: Figure Readability Gate

Pass only if key figures are readable in presentation mode: axes, legends, scale bars, labels, critical numbers, and diagnostic regions remain visible. Dense tables and multi-panel figures are split or moved to backup when needed.

## Gate 22: Final Page Lock Gate

Pass only if accepted deck order remains locked during local refinement. Any reorder must be explicitly requested and recorded in `deck_order_map.md`.

## Gate 23: Speaker-Readiness Gate

Pass only if key slides can support a 30-60 second speaker note with purpose, figure interpretation, transition, risk wording, and backup reference where needed.

## Gate 24: Final Delivery Preview Gate

Pass only if the final response can accurately summarize page count, mainline/backup split, navigation labels, core evidence chain, audit status, produced support files, and remaining manual checks.
