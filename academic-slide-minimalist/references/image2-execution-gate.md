# Image2 Execution Gate

Use this reference before any final slide image or PPTX production attempt.

## Purpose

This gate prevents the skill from silently falling back to code-rendered slides, editable PowerPoint layouts, screenshots, or templates when Image2-style full-slide generation is unavailable.

## Gate A: Backend availability

Before generating pages, answer internally:

```text
Is an Image2-style native full-slide generation backend available right now?
Can it generate complete 16:9 academic slide images?
Can it preserve real source figure crops without redrawing scientific content?
Can the accepted outputs be saved as final slide images?
```

If the answer to any item is no, unknown, or unconfirmed, stop before PPTX creation.

Allowed output when the gate fails:

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

Forbidden output when the gate fails:

```text
final_presentation.pptx
slide page images created by code
editable PPTX
HTML/CSS/SVG/canvas/browser screenshot slides
rasterized editable slides
```

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

When a PPTX is delivered, the assistant must include:

```text
Image2 backend used: yes
Full-slide images generated: yes
PPTX assembly mode: one full-slide image per slide
Editable slide elements: none
Source scientific visuals: real paper/SI/user-provided figures only
Validation completed: yes
```

If any line would be false, do not deliver the PPTX.
