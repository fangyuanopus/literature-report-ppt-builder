# Editable Output Options

Use this reference when deciding whether to output an image-based deck, editable deck, or both.

## Default

The default output is an image2-based stable PPT:

```text
one complete 16:9 image2 page -> inserted full-slide into PPT
```

This preserves layout stability and matches the user's preferred workflow.

## Optional Editable Versions

Only create editable versions when the user asks or when it is clearly useful.

### Stable presentation deck

- Filename suggestion: `final_presentation.pptx`
- Each slide is a full-slide image.
- Best for presenting and avoiding layout shifts.

### Editable text deck

- Filename suggestion: `editable_presentation.pptx`
- Text boxes, figures, and shapes remain editable where feasible.
- Scientific figures still must be real source images, not redrawn substitutes.
- Use this when the user likely needs to revise wording manually.

### Hybrid package

- Provide both stable and editable versions if time/tooling allows.
- The stable version is the authoritative presentation version.
- The editable version is a convenience copy and may have slight layout differences.

## Caution

Do not promise an editable deck unless it was actually created. If only the image2-based deck is produced, state that clearly.
