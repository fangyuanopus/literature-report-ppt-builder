# Exact Template Fidelity Mode

Use this mode only when the user explicitly asks for an exact reproduction of `assets/sample-literature-report.pptx`. It is a Route B workflow: edit inherited template objects in place instead of redrawing the visual system with code.

## Archetype selection

Choose a distinct source slide for each output page. Prefer these sample archetypes:

- slide 1: cover;
- slides 10–12 or 15: two-figure evidence;
- slide 14: dominant wide figure;
- slide 16: figure-left and text-right evidence;
- slide 18: summary;
- slide 20: closing.

Do not duplicate one source slide to create multiple output pages. Duplicate slide-part names can make downstream rendering and editing unreliable.

## Required build contract

1. Copy the original sample presentation and prune it to the selected source slides.
2. Use `references/sample-template-slot-manifest.json` to address inherited objects.
3. Replace text and images in place with `scripts/build_fallback_template_pptx.py`.
4. List every inherited scientific object in `delete_or_replace_objects`; retain only generic chrome.
5. Use real paper, SI, or user-provided figure crops. Never redraw scientific data.
6. Use one `new_paragraphs` entry per inherited paragraph when body copy contains multiple points. Use `style: base` and `style: emphasis` to reuse the template's original black and red runs instead of flattening the text into one style.
7. Run the builder with `--strict --fail-on-warnings`.
8. Run `scripts/audit_fallback_template_pptx.py --check-masters --exact-template --fail-on-review` on the result.
9. Run `scripts/audit_exact_template_fidelity.py --plan ... --build-report ... --fail-on-review` to compare slide size, source layout/master, preserved chrome, edited text geometry, inherited run styles, and image-frame containment.
10. Render every page, compare its montage with the source-template montage, and inspect any page whose figure or text appears undersized.

The source template owns navigation, title styling, margins, footer bands, line weights, and whitespace. New parallel objects are not allowed. If the requested content cannot fit an inherited archetype without moving or shrinking its chrome, choose another source archetype or shorten the copy.

## Completion criteria

- build report status is `passed` with zero warnings;
- structural audit status is `passed`;
- exact-template fidelity audit status is `passed`;
- the output PPTX contains no duplicate ZIP part names;
- no inherited notes, custom properties, stale sections, unused slide masters/layouts, or incorrect slide counts remain in the package;
- no old paper text, figure, caption, annotation, or source label remains;
- multi-point body copy occupies distinct inherited paragraphs and preserves any requested red emphasis runs;
- every scientific visual is legible at slideshow scale;
- the final montage preserves the original template's visual rhythm.
