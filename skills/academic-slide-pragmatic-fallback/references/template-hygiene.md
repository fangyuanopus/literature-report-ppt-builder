# Template Hygiene Gate

Use this gate before Route B. A template is a style asset only when its master and layout layers do not leak a prior paper into a new deck.

## Reject conditions

Reject the template for adaptive cross-domain use when a master or layout contains any of the following:

- prior-paper sample names, author names, methods, conclusions, or figure/table numbers;
- scientific images, charts, tables, captions, annotations, or source-specific callouts;
- legacy navigation labels that cannot be edited in place without adding parallel objects;
- opaque blocks, placeholder frames, or decorative groups that cover a new evidence region.

Exact-template mode has one narrow exception: fixed navigation and generic decorative chrome may remain when the user explicitly asks to reproduce that template and the labels still fit the new deck. This exception never applies to prior-paper methods, figures, captions, claims, names, or source-specific annotations.

For the bundled sample, run the final audit with `--exact-template`. That flag allowlists only the five fixed navigation labels; it does not relax checks for scientific content, unused masters/layouts, notes, document properties, or orphan package parts.

Generic PowerPoint placeholder prompts, a date field, a slide-number field, and style-only rules are allowed only when they render harmlessly or can be replaced in place.

## Audit

Run:

```text
python scripts/audit_fallback_template_pptx.py TEMPLATE.pptx --check-masters --out template_hygiene_report.json --fail-on-review
```

Read the report before selecting a template. If it reports `failed` or `needs_review`, use Route C unless you can clean the master/layout in PowerPoint and re-audit it.

## Route B ownership

Map every output slide to a source slide. Every visible inherited object must be one of:

1. retained generic chrome;
2. replaced in place with current-paper content; or
3. explicitly removed.

Do not add a new navigation bar over template navigation. Do not hide a legacy figure label behind a new image. Render a sample slide from every selected layout before building the full deck.

In exact-template mode, compare the final montage with the original template montage and require complete slot coverage. A slide passes only when every inherited scientific object is replaced or removed and the original chrome has not shifted.
