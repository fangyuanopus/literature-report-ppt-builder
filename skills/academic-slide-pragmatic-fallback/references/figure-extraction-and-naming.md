# Figure Extraction and Naming Rules

Use these rules when extracting, cropping, or naming real paper figures for image2 pages.

## Non-Negotiable Figure Rule

All scientific visuals must come from:

- the main paper PDF;
- the supplementary information / supporting information file;
- user-provided screenshots;
- user-provided PPT pages.

Do not create, redraw, beautify, regenerate, or replace scientific data visuals with AI-generated substitutes.

## Allowed Operations

Allowed:

- crop;
- enlarge or reduce;
- align;
- mask irrelevant margins;
- place figure panels into a slide composition;
- add short labels, thin boxes, arrows, or callouts;
- lightly adjust page placement for readability.

Not allowed:

- changing curves, peaks, spectra, bars, dots, microscopy, structures, tables, labels, legends, or numeric values;
- replotting data unless the user explicitly provides raw data and asks for a separate derived chart;
- removing axes, legends, sample names, units, or scale bars when they are needed for meaning;
- using decorative replacements for scientific figures.

## Naming Convention

Name extracted or cropped figure assets using this pattern:

```text
slide##_Fig##_panel##_source.png
```

Examples:

```text
slide10_Fig2_panelB-C_main.png
slide15_FigS23_panelA_SI.png
slide18_TableS4_full_SI.png
slide12_Fig3_panelD_main_preserve-scale-bar.png
```

Use:

- `main` for main-paper figures;
- `SI` for supplementary figures;
- `user` for user-provided screenshots;
- `panelA`, `panelB-C`, or `full` to show which part is used.

## Cropping Rules

Preserve when scientifically relevant:

- panel labels;
- axes and axis titles;
- legends;
- units;
- sample names;
- scale bars;
- reaction conditions;
- color bars;
- inset labels;
- statistical markers or error bars.

Crop only parts that do not change interpretation, such as large white margins, repeated caption fragments, or unrelated panels not used on the slide.

## Annotation Rules

Use annotations to guide attention, not to decorate.

Allowed annotation types:

- thin red box around a key region;
- short label naming the trend or sample;
- simple arrow pointing to the key signal;
- small note explaining what the viewer should notice.

Do not annotate with slogans, icons, artificial visual effects, or exaggerated claims.

## Manifest Link

Every extracted/cropped asset must correspond to a row in the figure-source manifest:

```text
asset filename | source figure | source file | slide number | claim supported | crop notes
```


## No Decorative Vector or Icon Rule

Do not add externally generated vector icons, decorative diagrams, fake scientific schemes, or AI-generated science illustrations to fill space. The only allowed additions are explanatory overlays on real source figures or simple text-only logic arrows/boxes that do not pretend to be scientific data.

Allowed annotations are attention guides: red boxes, arrows, shaded regions, zoom windows copied from the same source, short labels, and key-number callouts. If a slide needs a mechanism or structure that is not available as a real figure, use a text logic page instead of drawing one.

## Readability and Annotation Links

Before accepting a cropped figure, apply `figure-readability-standard.md`. Before adding callouts, apply `annotation-language.md`. If a cropped figure cannot remain readable, split the figure, enlarge the key panel, or move the full version to backup rather than forcing it into the mainline.
