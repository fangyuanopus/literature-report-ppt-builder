# Full-Deck Reorder Mode

Use this mode when the user says the deck order is messy, pages lack sequence, navigation is inconsistent, categories are unclear, or they want to keep the full version but reorder and unify it.

## Trigger Phrases

Use this mode for requests such as:

- 页面先后顺序很乱;
- 没有先后顺序;
- 没有导航栏;
- 没有分类;
- 保留完整版但重排统一;
- 按逻辑重新组装;
- 风格要统一;
- 不要继续随机生成单页.

## Workflow

1. Inventory existing pages and image files.
2. Identify each page's actual role: basic information, background, strategy, performance, structure, mechanism, summary, closing, backup, etc.
3. Derive or revise adaptive navigation labels for the current paper.
4. Rebuild `deck_order_map.md` with final page numbers.
5. Decide which old pages can be reused and which need redraw.
6. Normalize or regenerate only pages that fail navigation, style, or order requirements.
7. Copy accepted pages into `image2_pages_unified_final/` with sequential names.
8. Run `pre-assembly-checklist.md`.
9. Assemble the image2-based PPTX.
10. Run `post-assembly-render-audit.md` and produce a montage.

## Reuse Rule

Do not redraw every page automatically. Reuse pages that are scientifically correct and style-compatible after adding/normalizing navigation and page numbers. Redraw pages that are disordered, visually incompatible, scientifically risky, missing navigation, or too hard to explain.

## User Communication

When discussing this mode, explain that the goal is global deck coherence: order, categories, navigation, page numbers, mainline/backup boundary, and final assembly consistency.
