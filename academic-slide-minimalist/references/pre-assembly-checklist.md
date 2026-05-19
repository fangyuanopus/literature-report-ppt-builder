# Pre-Assembly Checklist

Use this checklist immediately before creating the PPTX from image2 pages.

## Required Checks

Pass only if:

- `deck_order_map.md` exists and has final page numbers for every slide;
- `adaptive_navigation_plan.md` exists or navigation labels are recorded in the order map;
- every slide has a page brief;
- every scientific figure appears in `figure_source_manifest.md`;
- every planned slide has an accepted image in `image2_pages_unified_final/`;
- filenames are sequential and match final page numbers;
- each image is 16:9;
- each normal slide has the correct navigation bar and active highlight;
- backup slides have the backup navigation state;
- no decorative vector icons or invented scientific visuals are present;
- old draft images are not in the final folder.

## Fail Actions

If any check fails, do not assemble the final PPT yet. Fix the affected image, page brief, or order map first.

## Minimal Report

Record:

```text
check item | pass/fail | affected slides | action taken
```
