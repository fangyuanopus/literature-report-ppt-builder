# Sample Deck Rhythm Reference

Use this reference when the user asks to follow the uploaded literature-report sample deck. The bundled `assets/sample-literature-report.pptx` is a style and structure reference, not a scientific source.

## Core Deck Rhythm

The sample deck is a Chinese literature-report presentation. Its logic is:

```text
封面 -> 基本信息 -> 研究背景 -> 研究思路 -> 研究结果 -> 总结启发 -> 汇报完毕
```

Preserve this rhythm by default as a presentation cadence. Do not replace it with a generic business deck, poster deck, dashboard deck, or freeform academic template. However, do not treat these labels as mandatory fixed navigation text for every paper; adapt navigation labels to the current paper when more precise sections are needed.

## Navigation Language

Use a top navigation row on normal content slides. The sample-style fallback is:

```text
基本信息 | 研究背景 | 研究思路 | 研究结果 | 总结启发 | Backup
```

But this is only a fallback. For each paper, derive the actual navigation with `adaptive-navigation.md`. A catalysis paper may need `设计策略 | 性能验证 | 结构证据 | 机理解释`; an algorithm paper may need `方法框架 | 实验结果 | 消融分析 | 泛化验证`.

Rules:

- Active section uses deep academic red or the sample deck active style.
- Inactive sections stay light gray / black / muted.
- Keep the navigation visually quiet; it should orient the audience, not dominate the page.
- Use the same navigation labels and order throughout the whole deck.
- Backup slides use a distinct Backup state.
- Keep page numbers near the bottom, consistent with the sample deck.

## Typical Page Roles

### Cover Page

Use the cover page to show:

- English paper title;
- Chinese translated title;
- presentation date and presenter;
- 3-5 key metrics, objects, or keywords if the paper provides them;
- journal / citation block when useful.

### Basic Information Pages

Use these pages to establish:

- paper title, authors, DOI, journal, year;
- research object;
- one-paragraph Chinese research summary;
- core contribution split into several concrete points.

### Research Background Pages

Use these pages to explain:

- why the field cares about the problem;
- what existing methods/materials can do;
- what remains unresolved;
- why the paper's target problem matters.

Prefer background figures from the paper/SI when available. If no real figure exists, use text-only logic pages rather than generated visuals.

### Research Idea Pages

Use these pages to explain:

- author's design strategy;
- route from problem to material/method;
- key hypothesis;
- experimental or computational route.

Only use real schemes/figures from the paper/SI. Simple text arrows are allowed for logic, but do not create fake scientific mechanisms.

### Research Result Pages

This is usually the longest section. Split results into separate evidence pages:

- synthesis or sample formation;
- phase/structure confirmation;
- morphology or direct observation;
- composition/active-site evidence;
- porosity or other basic property;
- stability/reliability;
- performance;
- comparison;
- mechanism discussion;
- recycling or application extension.

Use figure IDs in captions or notes so the source remains traceable.

### Summary and Inspiration Pages

End with:

- 2-4 concrete paper conclusions;
- what evidence supports the conclusions;
- methodological inspiration;
- limitations or unresolved questions;
- what can be learned for future research.

## Visual Style

Default style:

- white or very light gray background;
- restrained red-black-gray palette;
- large, conclusion-style title;
- dominant real figure;
- 2-3 short explanation points;
- figure ID labels such as `Fig. 2B-C` or `Fig. S12`;
- minimal red annotations: thin boxes, arrows, or short callouts;
- no decorative icons, glows, gradients, 3D, or technology backgrounds.

## Text Style

Write like a graduate student doing a group-meeting report:

- concrete, not slogan-like;
- evidence-led;
- cautious when evidence is indirect;
- Chinese explanation should be clear and oral-report friendly;
- retain accepted technical terms such as STEM, PXRD, XPS, BET, DFT, TOF, TON when useful.

## Non-Source Rule

The sample PPT teaches structure and style only. It must never be treated as a source for the new paper's scientific figures, data, conclusions, or terminology unless the user explicitly says it is content material for the current task.
