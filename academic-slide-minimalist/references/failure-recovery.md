# Failure Recovery Rules

Use this reference when the paper-to-PPT workflow encounters missing, unreadable, low-quality, or contradictory material.

## Core Rule

Never solve a missing-source problem by inventing content. If the paper, SI, figure, table, method, or panel is unavailable or unreadable, state the limitation, use only available evidence, or change the slide into a logic/text page.

## Common Failure Modes and Required Responses

### 1. Main paper cannot be read

Do not create a full literature-report PPT from memory, title, abstract snippets, or external guesses.

Allowed response:

```text
主文 PDF 无法完整读取，因此不能生成完整文献汇报。可以先基于可读页面生成临时大纲，但最终 PPT 需要重新读取完整论文。
```

### 2. SI / supplementary information is missing

If the user normally expects SI-based PPTs, state that SI support is absent. Continue only if the user accepts a main-paper-only run.

In the PPT, avoid claims that usually require SI support, such as synthesis reproducibility, extended stability, extra controls, or detailed experimental conditions, unless they are in the main paper.

### 3. SI is scanned or figure text is unreadable

Use page screenshots and visual inspection where possible. Do not rely on OCR unless unavoidable. If a panel label, axis, unit, or sample name cannot be read, mark it as uncertain and avoid using that panel as a main proof slide.

### 4. Figure resolution is too low

Do not enlarge until it becomes misleading or unreadable. Prefer:

- use the full PDF page screenshot at higher resolution;
- crop a smaller region;
- use the figure as supplementary support rather than main evidence;
- create a text explanation page with figure source noted as low-resolution.

### 5. Too many figures are available

Do not include every figure. Rank figures by evidence value:

1. figures that prove the main object exists;
2. figures that prove the key property or mechanism;
3. figures that prove performance/application;
4. controls and SI validation;
5. minor characterization or repeated trends.

Move lower-priority but useful SI figures to backup slides.

### 6. Figure and claim do not match

If a figure does not directly support the slide claim, change either the claim or the figure. Never use a visually attractive figure as decoration for an unrelated claim.

### 7. Required figure is unavailable

Use one of these fallbacks:

- text/logic page with no figure;
- use a different real figure that supports a narrower claim;
- mark the slide as needing user-provided source material;
- move the point to speaker notes rather than presenting it as visual evidence.

### 8. The paper cannot support 20 meaningful pages

Still do not inflate content with invented diagrams. Prefer:

- split background and method logic more carefully;
- include SI validation and backup slides;
- create a stronger discussion/inspiration section;
- if still insufficient, report that the source material supports fewer substantive slides.

### 9. Contradictory or ambiguous evidence

Do not resolve contradictions silently. Mark them as limitations or discussion points:

```text
该结果与 Fig. Sx 的趋势不完全一致，因此本页只能表述为“支持……趋势”，不能写成“完全证明……”。
```

### 10. Time or tool limitation

Prioritize scientific correctness over visual polish. If there is not enough time/tooling for all support files, produce the final PPTX and the figure-source manifest first, then report which optional files were not produced.

## Recovery Report

When a failure or limitation affects final quality, include it in `quality_check_report.md`:

```text
issue | affected slide(s) | impact | recovery action | remaining risk
```
