# Deck Order Map

Use this file to lock the final PPT order before image2 generation and PPT assembly.

## Core Rule

Never assemble a PPT by the order in which images were generated. Always assemble by the final `deck_order_map.md`.

## Required Fields

```text
final_page_number:
slide_id:
section:
navigation_labels:
navigation_highlight:
mainline_or_backup:
page_role:
conclusion_title:
source_figures:
source_files:
evidence_strength:
image2_filename:
status:
notes:
```

## Field Rules

### final_page_number

Use the actual slide number in the final PPT. This number must match the image filename and the visible page number whenever possible.

### section / navigation_highlight

Use the paper-specific navigation labels from `adaptive-navigation.md`. Do not use a fixed universal label set.

### mainline_or_backup

Use one of:

```text
mainline | closing | backup
```

### page_role

Examples:

```text
cover | paper information | background gap | design strategy | performance evidence | structure evidence | mechanism evidence | summary | inspiration | closing | backup method | backup table | backup q&a
```

### image2_filename

Use deterministic final names:

```text
slide_01.png
slide_02.png
...
slide_36.png
```

Intermediate generated images may have other names, but final assembly must use the standardized names.

## Completion Rules

Before generating image2 pages, every planned slide must appear in the map.

Before PPT assembly:

- every `image2_filename` must exist in the final approved image folder;
- no duplicate final page numbers;
- no missing page numbers;
- navigation labels must be identical across rows;
- backup pages must be after the main closing or clearly separated.

## Reorder Mode

When the user says the deck order is messy, pages lack classification, or navigation is inconsistent, rebuild `deck_order_map.md` first. Do not keep editing individual pages randomly.
