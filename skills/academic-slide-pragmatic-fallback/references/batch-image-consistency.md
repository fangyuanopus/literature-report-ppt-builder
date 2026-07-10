# Batch Image Consistency

Use this reference whenever image2 pages are generated in multiple batches.

## Core Rule

A full deck must look like one deck, not a collection of unrelated generated pages. Every batch must inherit the same visual contract.

## Required Style Contract

Before generating the first batch, define:

```text
aspect ratio: 16:9
canvas size:
background:
primary red:
text colors:
title position:
title size range:
navigation labels:
navigation position:
navigation highlight style:
footer / page number position:
figure annotation style:
bullet style:
backup styling:
```

Store this in `image2_generation_plan.md` or a style contract section.

## Batch Rules

For every batch:

- use the same navigation labels and order;
- use the same active-section highlight logic;
- use the same page-number position;
- use the same title scale and margin;
- use the same red-black-gray palette;
- use real source figures only;
- avoid decorative icons, synthetic illustrations, commercial poster layouts, and unrelated vector art;
- keep annotation types consistent: thin red boxes, arrows, shaded regions, zoom windows, short labels, and key-number callouts.

## Batch Acceptance Check

After each batch, update `image_generation_status.md`:

```text
slide | generated | style consistent | nav correct | page number correct | source figures real | accepted / redraw
```

If a batch drifts in style, do not continue producing more pages in that style. Redraw or normalize it before assembly.
