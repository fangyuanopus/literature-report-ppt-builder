# Image2 Execution Gate

Use this reference before any final slide image or PPTX production attempt.

## Purpose

This gate prevents the skill from silently falling back to code-rendered slides, editable PowerPoint layouts, screenshots, or templates when Image2-style full-slide generation is unavailable. A fallback PPTX may be created only after the user explicitly accepts the lower-fidelity fallback route, and it must use the bundled `assets/sample-literature-report.pptx` through template inspection, source-slide duplication, and inherited-slot replacement.

## Gate A: Backend availability

Before generating pages, answer internally:

```text
Is an Image2-style native full-slide generation backend available right now?
Can it generate complete 16:9 academic slide images?
Can it preserve real source figure crops without redrawing scientific content?
Can the accepted outputs be saved as final slide images?
```

If the answer to any item is no, unknown, or unconfirmed, stop before Image2-only PPTX creation. Explain the boundary and ask whether the user accepts a clearly labeled fallback PPTX.

Allowed output when the gate fails and the user has not accepted fallback:

```text
paper_logic_tree.md
adaptive_navigation_plan.md
deck_order_map.md
figure_source_manifest.md
page_briefs.md
image2_generation_prompts.md
assembly_notes.md
quality_check_report.md
```

Forbidden output when the gate fails and the user has not accepted fallback:

```text
final_presentation.pptx
slide page images created by code
editable PPTX
HTML/CSS/SVG/canvas/browser screenshot slides
rasterized editable slides
```

If the user explicitly accepts fallback output, the assistant may produce a clearly labeled lower-fidelity PPTX based on `assets/sample-literature-report.pptx`, preferably named:

```text
fallback_presentation.pptx
editable_fallback_presentation.pptx
```

Do not call this fallback deck `final_presentation.pptx` unless the user explicitly requests that filename. Do not claim it passed Image2 manifest or image-only validation. Do not create an unrelated freeform deck or a hand-redrawn approximation of the template. Inspect the bundled sample, map every output slide to a source slide, duplicate those slides, and edit inherited text/image/table slots while preserving the sample's 16:9 format, red-black-gray academic tone, navigation rhythm, title hierarchy, and page-number/footer conventions.

## Gate B: Manifest requirement

Before assembly, create `image2_manifest.json`.

Minimum schema:

```json
{
  "image2_backend_confirmed": true,
  "slides": [
    {
      "slide_no": 1,
      "section": "cover",
      "final_image": "final_images/slide_001.png",
      "generation_route": "image2_full_slide",
      "accepted": true,
      "source_figures": []
    }
  ]
}
```

Rules:

- every planned slide must appear in the manifest;
- every slide must have `generation_route: "image2_full_slide"`;
- every slide must have `accepted: true`;
- every `final_image` must exist;
- no PPTX may be assembled from images not listed in the manifest.

## Gate C: Mechanical PPTX validation

After assembly, run:

```bash
python scripts/validate_image_only_pptx.py final_presentation.pptx --manifest image2_manifest.json
```

Delivery is blocked if validation fails.

## Final response requirement

When an Image2-only PPTX is delivered, the assistant must include:

```text
Image2 backend used: yes
Full-slide images generated: yes
PPTX assembly mode: one full-slide image per slide
Editable slide elements: none
Source scientific visuals: real paper/SI/user-provided figures only
Validation completed: yes
```

If any line would be false, do not deliver the Image2-only PPTX. If the user accepted fallback output, include this instead:

```text
Image2 backend used: no
Delivery mode: fallback PPTX accepted by user
Image2-only validation: not applicable
Scientific visuals: real paper/SI/user-provided figures only
Editable or code-rendered elements may exist: yes
Template source: assets/sample-literature-report.pptx
Template-following workflow: inspected, mapped, duplicated, edited inherited objects
```
