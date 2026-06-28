# Pre-Assembly Checklist

Use this checklist immediately before creating the PPTX from image2 pages.

## Required Checks

Pass only if:

- `deck_order_map.md` exists and has final page numbers for every slide;
- `adaptive_navigation_plan.md` exists or navigation labels are recorded in the order map;
- every slide has a page brief;
- every scientific figure appears in `figure_source_manifest.md`;
- every planned slide has an accepted image in `image2_pages_unified_final/`;
- `image2_manifest.json` exists and lists every final image;
- every manifest entry has `generation_route: "image2_full_slide"` and `accepted: true`;
- filenames are sequential and match final page numbers;
- each image is 16:9;
- each normal slide has the correct navigation bar and active highlight;
- backup slides have the backup navigation state;
- no decorative vector icons or invented scientific visuals are present;
- old draft images are not in the final folder.

## Fail Actions

If any check fails, do not assemble the Image2-only final PPT yet. Fix the affected image, page brief, order map, or manifest first. If Image2 availability is not confirmed, stop before Image2-only PPTX creation and ask whether the user accepts a clearly labeled fallback PPTX based on `assets/sample-literature-report.pptx`. Without explicit fallback consent, deliver only page briefs, prompts, and assembly notes.

## Minimal Report

Record:

```text
check item | pass/fail | affected slides | action taken
```
