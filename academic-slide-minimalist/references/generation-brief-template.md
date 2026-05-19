# Generation Brief Template

Use this before building a full literature-report PPT whenever feasible. The brief can be shown to the user for approval, or maintained internally if the user asked for direct generation.

## Required Brief Sections

### 1. File Intake

```text
main paper: [filename]
SI / supplementary information: [filename]
sample deck/style reference: [filename or bundled sample]
output: Chinese literature-report PPT, image2-first, at least 20 pages
```

If either the main paper or SI is missing, state what is missing. Do not pretend the missing file was read.

### 2. Paper Logic Tree

```text
research background -> unresolved problem -> author strategy -> methods/evidence -> performance/application -> conclusion -> inspiration
```

Use short Chinese phrases, not long paragraphs.

### 3. Evidence Chain

```text
question | main-paper evidence | SI support | interpretation | caution level
```

Caution levels:

- direct evidence;
- indirect support;
- supplementary support;
- proposed explanation;
- preliminary performance result.

### 4. Figure-Source Manifest Preview

```text
slide | figure id | source file | panel(s) | evidence role | supported slide claim
```

Every scientific image planned for the deck must appear here.

### 4.5 Adaptive Navigation Plan

```text
paper domain:
main story axis:
navigation labels:
label | page range | purpose | active highlight rule
backup state:
why these labels fit this paper:
```

Do not use a fixed navigation label set unless it genuinely fits the paper.

### 4.6 Deck Order Map Preview

```text
final page | section | navigation highlight | mainline/backup | conclusion title | source figure(s) | image2 filename | status
```

This preview should later become `deck_order_map.md`.

### 5. Page-by-Page Outline

```text
slide number | navigation section | navigation highlight | mainline/backup | conclusion-style title | main figure(s) | SI figure(s) | page purpose
```

The outline must contain at least 20 pages unless the user asked for fewer.

### 6. Risk Notes

Record any issue that may affect correctness:

- missing SI;
- figure too low-resolution;
- figure panel label unclear;
- claim depends on indirect evidence;
- mechanism is proposed rather than proven;
- no real figure exists for a desired logic page.

## When to Pause

If the user explicitly asks to review the outline first, pause after the brief.

If the user asks for direct generation, continue after creating the brief internally, but preserve the same checks.

## Required Page-Brief Hand-Off

After the generation brief, create `page_briefs.md` using `page-brief-template.md`. The generation brief defines the deck-level logic; page briefs define each slide.

Minimum hand-off fields for each slide. Include adaptive navigation and final-page identity:

```text
slide number | section | navigation highlight | mainline/backup | conclusion-style title | source figure(s) | evidence strength | layout plan | risk/caution
```

Do not move to image2 generation until each planned slide has a page brief.

### 7. Terminology Table Preview

```text
English term | Chinese term | use rule | caution
```

Include recurring sample names, methods, units, and claim verbs. Use `terminology-control.md`.

### 8. Domain Evidence Chain

```text
paper domain:
chosen result chain:
reason:
```

Use `domain-adaptation.md` to avoid forcing all papers into the same result order.

### 9. Backup and Question Plan

```text
backup slide candidates:
likely question themes:
slides needing cautious answers:
```

Use `backup-slides.md` and `question-prep.md` in maximum-quality mode.

### 10. Failure Recovery Notes

```text
issue | affected source/slide | recovery action | remaining risk
```

Use `failure-recovery.md` whenever source material is incomplete or ambiguous.

### 11. Layout Grammar and Readability Plan

```text
slide | layout pattern | figure readability risk | annotation language | speaker-note check | question risk level
```

Use `sample-layout-grammar.md`, `figure-readability-standard.md`, `annotation-language.md`, `speaker-notes-to-slide-check.md`, and `question-risk-level.md`.

### 12. Refinement Diagnosis Plan

When improving an existing deck, include:

```text
slide | current problem | redraw priority | repair action | locked page number | final filename
```
