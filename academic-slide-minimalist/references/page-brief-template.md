# Page Brief Template

Use one page brief for every slide before creating image2. The page brief is mandatory for high-quality full-deck generation.

## Purpose

A page brief prevents slide generation from becoming a figure collage. It forces every slide to have one claim, one evidence role, and one layout decision.

## Template

```text
slide number:
final page number:
section:
navigation labels:
navigation highlight:
mainline or backup:
page type:
layout pattern:
core claim:
why this slide exists:
source figure(s):
source location:
evidence strength:
figure role:
what to crop or preserve:
key trend:
key number(s):
what to annotate:
annotation language:
figure readability check:
Chinese slide title:
Chinese slide copy:
speaker-note purpose:
risk / caution:
question risk level:
speaker-note reverse check:
layout plan:
image2 filename:
status:
```

## Field Rules

### slide number

Use the final PPT order.

### section

Use the paper-specific navigation and section labels derived with `adaptive-navigation.md`. The default labels such as 基本信息, 研究背景, 研究思路, 研究结果, 总结启发, and Backup are only a fallback. For result-heavy papers, use more precise labels such as 性能验证, 结构证据, 机理解释, 应用验证, or domain-appropriate alternatives.

### navigation labels / navigation highlight

Copy the full navigation bar and active highlight from `deck_order_map.md`. Every normal slide in the same deck should use the same navigation labels in the same order.

### mainline or backup

Use `mainline`, `closing`, or `backup`. Use `mainline-backup-boundary.md` to decide.

### page type

Use one of:

```text
evidence slide | comparison slide | logic/route slide | background gap slide | method slide | summary/inspiration slide | closing slide
```

### core claim

Write one sentence that the audience should remember. It should be a conclusion-style claim, not a topic label.

Weak:

```text
热稳定性
```

Better:

```text
高温处理后样品仍保持主要晶体特征与介孔吸附行为
```

### source figure(s)

List exact figure IDs, including main paper or SI status.

Examples:

```text
Fig. 2B-E, main paper
Fig. S23, SI
```

If there is no figure, write `none - logic/text page`.

### evidence strength

Use labels from `evidence-strength.md`.

### what to crop or preserve

State what must not be removed: axes, legends, scale bars, units, sample names, panel labels, or conditions.

### Chinese slide copy

Keep it short. Default: 2-3 bullet points or 1 short explanatory paragraph.

### risk / caution

Flag overclaim risks such as:

- evidence is indirect;
- mechanism is proposed, not proven;
- comparison is limited to selected conditions;
- SI support is necessary;
- no direct image exists.

## Completion Rule

Do not generate image2 for a page until its brief has a clear core claim, figure source, evidence role, and layout plan.

## Optional Maximum-Quality Fields

Add these fields when creating `page_briefs.md` for a maximum-quality run:

```text
terminology to preserve:
trend emphasis:
likely audience question:
safe answer:
backup slide link:
editable-output note:
```

### terminology to preserve

List any exact sample names, units, figure labels, or technical terms that must remain consistent.

### likely audience question / safe answer

Use `question-prep.md` for important evidence slides, weak-claim slides, and limitation slides.

### backup slide link

If a slide simplifies a dense SI figure or method, note the backup slide that preserves the full support.


## Additional Refinement Fields

For deck refinement, add:

```text
redraw priority: A / B / C
locked page number:
local repair action:
keep / redraw reason:
```

Use `redraw-priority.md` and `final-page-lock.md`.
