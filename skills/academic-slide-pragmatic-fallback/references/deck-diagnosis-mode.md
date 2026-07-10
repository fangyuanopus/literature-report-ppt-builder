# Deck Diagnosis Mode

Use this mode when the user asks how to improve an existing deck or says the deck is messy, ugly, hard to present, out of order, missing navigation, inconsistent in style, or needs another refinement round.

## Core Rule

Do not immediately redraw the whole deck. Diagnose first, then decide what should be kept, locally repaired, redrawn, reordered, or moved to backup.

## Trigger Phrases

Use this mode for requests such as:

- 这版 PPT 还有哪里能优化;
- 页面顺序乱;
- 风格不统一;
- 有些页没有导航栏;
- 哪些页需要重画;
- 继续精修;
- 先做逐页优化清单;
- 帮我诊断这份 PPT.

## Diagnosis Dimensions

Check every page for:

1. story order: whether the page appears at the right point in the evidence chain;
2. navigation: whether navigation labels and active highlight match `deck_order_map.md`;
3. mainline/backup boundary: whether dense support material interrupts the main story;
4. figure integrity: whether all scientific visuals are real source figures;
5. figure readability: whether the audience can read axes, legends, scale bars, and key regions;
6. trend emphasis: whether the important number, peak, comparison, or region is marked;
7. visual consistency: whether the page matches the approved sample-style contract;
8. claim calibration: whether the title overstates the evidence;
9. speaker readiness: whether the page can support a 30-60 second oral explanation.

## Output Template

```text
slide | current role | problem | fix type | redraw priority | recommended action
```

Use fix types:

```text
keep | local repair | redraw image2 | reorder | split | merge | move to backup | remove
```

## Workflow

1. Read the current PPT, image folder, montage, or page screenshots when available.
2. Compare the actual pages with `deck_order_map.md` if it exists.
3. If no order map exists, reconstruct one before recommending edits.
4. Use `redraw-priority.md` to classify pages as A/B/C.
5. Only after diagnosis should image2 pages be redrawn or the PPT reassembled.
