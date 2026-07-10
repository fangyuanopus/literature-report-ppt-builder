# Image Generation Status

Use this reference to track page-image completion in full-deck and multi-batch image2 workflows.

## Purpose

The user may ask which slide images are missing, accepted, or need redraw. Do not guess. Maintain a status table.

## Required Table

```text
slide | final title | section | source figures | image2 filename | generated | nav correct | style consistent | page number correct | source integrity | status | notes
```

## Status Values

Use one of:

```text
planned | generated | needs_redraw | accepted | replaced | final_assembled
```

## Update Rules

- After each image batch, update the table.
- When a slide is redrawn, mark the old version `replaced` and the new version `accepted` only after checking it.
- Before PPT assembly, all mainline and backup slides must be `accepted`.
- After assembly, mark included pages as `final_assembled`.

## Answering User Status Questions

When the user asks `还有哪些图片没生成`, answer from this table:

```text
未生成:
- slide xx ...
需要重绘:
- slide xx ...
已接受:
- slide xx ...
```

Do not say all images are complete unless the table supports it.
