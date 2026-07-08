# Editable Output Options

Use this reference when deciding whether to output an image-based deck, editable deck, fallback deck, or a hybrid package.

## Default

The default output is an image2-based stable PPT:

```text
one complete 16:9 image2 page -> inserted full-slide into PPT
```

This preserves layout stability and matches the user's preferred workflow.

## Optional Editable Versions

Only create editable versions when the user asks, or when Image2 is unavailable and the user explicitly accepts a lower-fidelity fallback PPTX. Fallback editable decks must use the bundled `assets/sample-literature-report.pptx` through a template-following workflow: inspect source slides, duplicate mapped slides, and replace inherited slots.

### Stable presentation deck

- Filename suggestion: `final_presentation.pptx`
- Each slide is a full-slide image.
- Best for presenting and avoiding layout shifts.

### Editable text deck

- Filename suggestion: `editable_presentation.pptx`
- Text boxes, figures, and shapes remain editable where feasible.
- Scientific figures still must be real source images, not redrawn substitutes.
- Use this when the user likely needs to revise wording manually.

### Fallback editable deck

- Filename suggestion: `editable_fallback_presentation.pptx`
- Use only when Image2 is unavailable and the user explicitly accepts fallback output.
- Use the bundled `assets/sample-literature-report.pptx` template by editing inherited text/image/table slots in duplicated source slides; preserve its academic red-black-gray rhythm, title hierarchy, navigation behavior, and page-number/footer conventions.
- Do not make a freeform editable deck that merely imitates the template colors or approximate coordinates.
- Clearly state that this is not the authoritative Image2-only deck and does not pass Image2 manifest validation.

### Hybrid package

- Provide both stable and editable versions if time/tooling allows.
- The stable version is the authoritative presentation version.
- The editable version is a convenience copy and may have slight layout differences.

## Caution

Do not promise an editable deck unless it was actually created. If only the image2-based deck is produced, state that clearly. If a fallback deck is produced, label it as template-based fallback output and do not imply Image2-only validation.
