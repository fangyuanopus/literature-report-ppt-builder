---
name: academic-slide-pragmatic-fallback
description: Create Chinese academic literature-report PPTs from real paper/SI figures. Use for journal-club, thesis-defense, paper-to-PPT, and slide-review tasks, especially when Image2-style full-slide generation is unavailable. Preserve the strict Image2-only route when available; otherwise require explicit consent and choose a clean template-fidelity or a sample-style pragmatic fallback with real figures, source tracking, structural QA, and render QA.
---

# Academic Slides with Safe Fallbacks

Create academic decks that are evidence-led, readable, and honest about their production route.

## Non-negotiable rules

- Use scientific visuals only from the paper, SI, or user-provided sources. Never fabricate, redraw, or semantically alter data figures, microscopy, spectra, molecular structures, mechanisms, tables, or charts.
- Write conclusion-style titles, trace every visual in a figure-source manifest, and calibrate claims to evidence.
- Do not call an editable or code-built deck Image2-only.

## Choose one route

### Route A: Image2-only authoritative deck

Use only when a full-slide Image2 backend is confirmed and can faithfully preserve supplied scientific crops. Keep `image2_manifest.json`, package one approved full-slide image per PPTX slide, and run `scripts/validate_image_only_pptx.py`.

### Route B: template-fidelity fallback

Use only after explicit user consent and a passed hygiene audit. The template owns its navigation, footer, and mapped slots; code edits inherited objects in place and must not add a second navigation layer.

When the user explicitly asks to reproduce the bundled sample template exactly, use Route B's exact-template mode. Preserve the sample's navigation labels and decorative chrome intentionally, map each output page to a distinct source-slide archetype, and replace or remove every source-specific scientific object. Do not describe a code-redrawn Route C deck as an exact reproduction. Read `references/exact-template-fidelity.md` before building.

```text
python scripts/build_fallback_template_pptx.py edit_plan.json exact.pptx --strict --fail-on-warnings
python scripts/audit_fallback_template_pptx.py exact.pptx --build-report exact.build-report.json --check-masters --exact-template --fail-on-review
python scripts/audit_exact_template_fidelity.py exact.pptx --plan edit_plan.json --build-report exact.build-report.json --fail-on-review
```

```text
python scripts/audit_fallback_template_pptx.py template.pptx --check-masters --fail-on-review
```

Reject templates containing old scientific content, figure labels, sample names, or non-removable master/layout objects. For adaptive cross-domain reuse, also reject fixed legacy navigation. The only exception is exact-template mode, where the user has explicitly requested that navigation and it remains semantically appropriate. Read `references/template-hygiene.md` and `references/fallback-template-pptx.md`.

### Route C: pragmatic fallback

Use only after explicit user consent when Image2 is unavailable and no clean, domain-compatible template passes Route B. Start from a blank 16:9 presentation: code owns every visible object. Never import a content-bearing master or layout.

Route C follows the visual grammar of `assets/sample-literature-report.pptx`—white canvas, red-black-gray palette, shallow top navigation, conclusion title, thin rule, and quiet footer/page number—without inheriting the sample's old content. Read `references/first-template-style-contract.md` and `references/pragmatic-fallback.md`.

Every page brief must specify one of: `cover`, `text`, `figure_right`, `figure_wide`, `process`, `comparison`, `summary`, or `closing`.

```text
python scripts/build_pragmatic_fallback_pptx.py pragmatic_edit_plan.json --out editable_fallback_presentation.pptx
python scripts/validate_pragmatic_fallback_pptx.py editable_fallback_presentation.pptx --plan pragmatic_edit_plan.json --fail-on-review
```

Every displayed scientific figure requires `source_type: figure_crop`, `crop_verified: true`, figure ID, source page, and source label. A full paper-page scan is not a figure crop.

## Page ownership and fit contract

- Choose exactly one owner per slide: inherited template objects in Route B, or generated objects in Route C. Never combine the two.
- The builder treats every code-owned text box as a fixed template slot: it blocks copy that exceeds the slot's CJK-aware line capacity, as well as titles over 54 characters and overlong bullet lists. Shorten or restructure copy before building; never shrink one page's font or truncate with ellipses.
- Select the layout from the evidence: use wide figures for plots/tables, right-side figures for portrait images, process flow for 2–5 steps, comparison for two alternatives, and summary rows for 2–5 conclusions/parameters.
- Do not expose internal route names, template notes, model names, fallback labels, or build instructions in audience-facing slides.

## Required production flow

1. Confirm paper/SI source availability and explicit fallback consent.
2. Create `paper_analysis.json` following `references/paper-analysis-contract.md`, then run `scripts/validate_paper_analysis.py --fail-on-review`. This is the source of truth for the logic tree, figure boundaries, evidence chains, adaptive navigation, and slide claims.
3. Derive the terminology table, figure-source manifest, `deck_order_map.md`, and page briefs from the validated analysis. Do not introduce a slide claim, source figure, or navigation section that is absent from the analysis without updating and revalidating it.
4. Choose Route A, B, or C and prepare page briefs with source crops and page types.
5. Build only through that route; do not silently substitute a different route.
6. Run structural QA, render every slide with PowerPoint/LibreOffice where available, inspect individual pages and a montage, and fix all overflow, overlap, legacy residue, unreadable figures, and inconsistent chrome.

For exact-template mode, also compare the montage with the source-template montage. Passing structural QA alone is insufficient: the inherited navigation, title treatment, margins, footer band, image framing, and whitespace rhythm must remain visibly unchanged.

## Route C delivery statement

```text
Image2 backend used: no
Delivery mode: pragmatic editable fallback accepted by user
Visual style: sample-deck-derived white/red/black academic grammar
Scientific visuals: real paper/SI/user-provided figure crops only
Structural QA completed: yes
Render/layout QA completed: yes/no
Editable elements may exist: yes
```
