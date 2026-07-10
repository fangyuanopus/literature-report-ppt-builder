# Rigorous Paper Close Reading Rules

Use this reference when the user asks for paragraph-by-paragraph paper reading, translation, and commentary, or when preparing a literature-report PPT from a main paper and supplementary information.

## Core Principle

Read with strict lexical fidelity. Do not replace careful reading with a summary. Preserve technical terms, claim boundaries, evidence relationships, equations, symbols, figure labels, sample names, units, and experimental conditions.

## Interactive Close Reading Mode

Use this mode only when the user explicitly asks to read the paper step by step, paragraph by paragraph, or to use the close-reading prompt directly.

Process exactly one original paragraph at a time. If the paragraph is long, subdivide it into logical argument units, but do not remove, merge, rewrite, or alter any original wording. Across all units, the full original paragraph must appear completely.

For each logical unit, output three layers in this fixed order:

1. **Full original English text**
   - Reproduce the supplied English text verbatim.
   - Do not omit, paraphrase, compress, or alter words.
   - Reproduce equations, symbols, tables, and pseudocode exactly as supplied.

2. **Line-by-line or sentence-by-sentence Chinese translation**
   - Translate into natural, academically standard Mainland Chinese.
   - Keep the meaning faithful and the style mature.
   - Avoid machine-translation tone.

3. **Deep analytical commentary**
   Cover the points that matter for the passage:
   - function in the paper's overall argument;
   - logical structure;
   - implicit assumptions;
   - methodological mechanics;
   - potential weaknesses;
   - theoretical implications;
   - transferable ideas;
   - common misunderstandings;
   - links to nearby sections, figures, and SI evidence.

After finishing one complete original paragraph, stop and wait. Proceed only after the user explicitly says “继续”, “可以了”, “下一段”, or equivalent. Never advance automatically in interactive close-reading mode.

## Initial Overview for a New Paper

At the beginning of a new paper, provide a concise structural overview before paragraph-level reading:

```text
research question | main contribution | argument roadmap | key terminology | likely figure/evidence structure
```

Do not let this overview replace detailed reading.

## PPT Production Mode

When the final task is to generate a literature-report PPT, do not stop after each paragraph. Use close reading internally to build a faithful argument map, then convert the result into slides.

For PPT production, produce or internally maintain:

```text
paragraph/section -> claim -> evidence -> figure/table -> SI support -> slide claim -> slide page
```

Do not reproduce the full paper verbatim in the PPT deliverable. Use the close reading to prevent information loss, mistranslation, unsupported claims, and figure-message mismatch.

## Main Paper + SI Reading Order

Default order when both files are provided:

1. Title, abstract, and graphical/TOC figure if present.
2. Introduction: field problem, gap, and motivation.
3. Results section: claims, figures, methods embedded in results, and evidence chain.
4. Discussion/conclusion: final contribution, limitations, and future implications.
5. SI overview: experimental methods, synthesis details, extra characterization, controls, repeated tests, raw/expanded data, and extra figures.
6. Cross-link main text claims to SI support.

## Figure and Evidence Reading

For every figure that may enter the PPT, record:

```text
figure id | main/SI | panel(s) | what the figure directly shows | what it does not prove | related paragraph | possible slide claim
```

Do not overstate evidence. Distinguish:

- directly observed evidence;
- indirectly supported evidence;
- proposed mechanism;
- comparison result;
- supplementary control;
- preliminary application test.

## Fidelity Warnings

Avoid these errors:

- summarizing a paragraph before understanding each sentence;
- translating technical terms inconsistently;
- treating SI figures as decorative rather than evidentiary;
- using a figure because it looks good rather than because it supports a claim;
- turning proposed mechanisms into proven mechanisms;
- making slide titles stronger than the paper's evidence permits;
- skipping equations, conditions, concentrations, temperatures, sample names, controls, or units.

## External Sources

For user-provided paper/SI reading, rely on the supplied material. Do not browse externally unless the user explicitly asks for external verification, citation lookup, or missing metadata.
