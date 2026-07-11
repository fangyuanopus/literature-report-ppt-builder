# First Template Style Contract

Apply this contract to every pragmatic fallback page. It captures the visual grammar of `assets/sample-literature-report.pptx` without importing its polluted masters.

## Persistent chrome

- 16:9 white canvas; no dark sidebars, gradients, or oversized cards.
- Content pages use one shallow, bordered top navigation row with 3–7 Chinese labels. The active section is deep academic red; inactive labels are black/gray on white.
- Use a large conclusion-style title in the sample deck's deep academic red, aligned close to the left page edge.
- Small gray publication footer and page number. Footer content is bibliographic only.
- Cover and closing pages omit navigation, footer, and page number; both use the sample deck's full-width deep-red bottom band.

## Layout grammar

- Use a centered cover and closing page.
- Let a real figure dominate an evidence page. Use a wide region for horizontal plots/tables and a right region for portrait figures.
- When a nominally wide figure is not actually panoramic, place it in a large left evidence panel and move interpretation into a narrow right panel rather than letterboxing the figure in an overly wide frame.
- Use a horizontal process row only for 2–5 logical steps; use comparison only for true alternatives.
- Use readable summary rows rather than small card grids or raw figure-number labels.

## Safety

- Every visible object belongs on the slide layer and has an `AGENT_` ownership prefix.
- No title, body, caption, footer, navigation, or page number may overlap another visible object or exceed the canvas.
- Use prepared scientific figure crops only. Split dense multi-panel evidence across slides when it cannot be read at presentation scale.
- Use Microsoft YaHei and set the East Asian font attribute for generated Chinese text.
