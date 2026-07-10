# Final Page Lock

Use this reference once the user accepts a page order, a deck outline, or a version such as a unified/reordered final deck.

## Core Rule

When page order is accepted, lock the final page numbers. Later edits should modify content within the same slide IDs unless the user explicitly asks to reorder the deck again.

## Lock Conditions

Treat the page order as locked when:

- the user says a version is good, acceptable, or can be kept;
- the user says to continue refining the same version;
- `deck_order_map.md` is marked final;
- a final assembled PPT has been produced and accepted.

## Locked-Order Rules

- Do not move slides to new positions during local refinement.
- Do not renumber pages unless the user requests a structure change.
- Do not change navigation page ranges unless the deck structure changes.
- Redrawn images must keep the same `slide_##.png` final filename.
- If a slide is moved to backup, update `deck_order_map.md`, `image_generation_status.md`, speaker notes, and the visible page number together.

## Unlock Conditions

Only unlock order when the user says:

```text
重新调整结构 | 重排顺序 | 改目录 | 改章节 | 主线重新排 | 保留完整版但重排
```

## Lock Record Template

```text
locked_slide_order: true/false
locked_version:
locked_page_count:
reason:
allowed_changes:
forbidden_changes:
```
