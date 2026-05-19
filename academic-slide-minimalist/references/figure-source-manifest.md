# Figure Source Manifest

Use this manifest internally before and during full PPT generation.

## Required Fields

```text
figure id | source: main paper or SI | page/location | panel(s) | content | slide number | slide claim | evidence role | notes
```

## Evidence Role Labels

Use one of these labels:

- background context
- research design
- direct structural evidence
- indirect structural evidence
- morphology evidence
- composition evidence
- porosity evidence
- stability evidence
- active-site evidence
- performance evidence
- comparison evidence
- mechanism discussion
- supplementary support

## Rules

- Every scientific figure in the deck must appear in the manifest.
- Mark whether the figure comes from the main paper or supplementary information.
- Link each figure to the paragraph, result, or method detail that justifies its use when possible.
- Do not use a figure if its role is unclear.
- Do not crop out axes, legends, scale bars, or labels if doing so changes the scientific meaning.
- Preserve scale bars for microscopy images whenever possible.
- Preserve sample names and units for charts whenever possible.
- If a figure contains too many panels, choose the panels that support the slide claim and mention the full figure ID in notes when needed.


## Asset Naming Link

When a figure is extracted or cropped, name the asset according to `figure-extraction-and-naming.md`. The asset filename must appear in the manifest so that each image2 page can be traced back to the original paper or SI.

## Evidence Strength Link

Use `evidence-strength.md` to label whether a visual is direct evidence, indirect evidence, supplementary support, preliminary evidence, proposed mechanism support, or application validation. This label should guide the slide title wording.

## Example

```text
Fig. 4A-B | main paper | result section | Ar adsorption and NLDFT pore distribution | slide 14 | 吸附与孔径分布共同证明本征介孔 | porosity evidence | preserve axes and 2.6 nm label
Fig. S23 | SI | thermal stability | PXRD after calcination | slide 15 | 高温处理后骨架仍保持主要特征峰 | stability evidence | annotate retained peaks
```


## Extraction Notes

For each figure, also track how it was extracted or used:

- full figure;
- selected panels only;
- cropped region;
- screenshot from PDF page;
- direct embedded image extraction;
- user-provided screenshot.

If selected panels are used, state the panel letters explicitly. Do not crop out labels that are needed to understand the result.

## Missing or Low-Quality Figures

If a necessary figure is missing, unreadable, or too low-resolution:

1. Do not recreate it with AI.
2. Use a text-only logic page if the point can still be explained honestly.
3. Or ask for a clearer source image / PDF page.
4. Mark the figure status in the manifest.
