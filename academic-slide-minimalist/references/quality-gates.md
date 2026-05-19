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

## Gate 6: Final PPT Assembly Gate

Pass only if:

- image2 pages were inserted full-slide into PPT pages;
- page order matches the approved/internal outline;
- navigation active section and page numbers are consistent;
- no slide is blank, duplicated by accident, or missing from the page count;
- the final PPTX opens and contains the expected number of slides.

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

- final PPTX;
- image2 pages, if produced;
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
