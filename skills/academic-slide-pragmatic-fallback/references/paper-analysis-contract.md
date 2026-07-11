# Paper Analysis Contract

Use this contract before creating `deck_order_map.md`, page briefs, Image2 prompts, or a fallback edit plan. It makes the paper-understanding stage inspectable instead of relying on an unrecorded summary.

## Required artifact

Create `paper_analysis.json` and validate it before generation:

```bash
python scripts/validate_paper_analysis.py paper_analysis.json \
  --out paper_analysis_validation.json \
  --fail-on-review
```

The contract has five linked layers:

```text
paper + SI sources
  -> logic_tree
  -> figures
  -> evidence_chains
  -> navigation + slides
```

The slide plan may only cite figure IDs and evidence IDs declared earlier in the file. A page title is therefore traceable to a question, a real source figure, its direct observation, and an evidence-strength boundary.

## Schema outline

```json
{
  "$schema": "academic-paper-analysis/v1",
  "paper": {
    "title": "...",
    "domain": "algorithm / materials / biology / ...",
    "source_files": [{"source_id": "main", "role": "main", "path": "paper.pdf"}]
  },
  "logic_tree": {
    "research_object": "...",
    "background": "...",
    "unresolved_problem": "...",
    "author_strategy": "...",
    "methods": "...",
    "key_conclusion": "...",
    "limitations_and_inspiration": "..."
  },
  "figures": [{
    "figure_id": "fig_1",
    "source_id": "main",
    "source_page": 3,
    "source_label": "Figure 1",
    "direct_observation": "图中直接可见的事实",
    "does_not_prove": "不能由该图单独推出的结论",
    "evidence_strength": "direct"
  }],
  "evidence_chains": [{
    "evidence_id": "ev_architecture",
    "question": "作者如何替代循环主干？",
    "figure_ids": ["fig_1"],
    "interpretation": "...",
    "slide_claim": "...",
    "evidence_strength": "direct",
    "caution": "..."
  }],
  "navigation": [{"label": "方法框架", "purpose": "解释作者策略"}],
  "slides": [{
    "slide_no": 1,
    "slide_id": "s01",
    "section": "方法框架",
    "page_role": "design_strategy",
    "mainline_or_backup": "mainline",
    "title": "...",
    "evidence_ids": ["ev_architecture"],
    "figure_ids": ["fig_1"]
  }]
}
```

## Rules

- Record main paper and SI separately. A figure must identify its `source_id`, PDF page, and printed figure/table label.
- `direct_observation` describes only what the figure or table visibly establishes; `does_not_prove` blocks title overstatement.
- Every evidence chain has one question, one or more figure IDs, an interpretation, a slide claim, and a caution boundary.
- Every non-cover, non-closing, non-divider slide must cite an evidence chain. Evidence-led slides must also cite the real figure IDs used on the page.
- Navigation labels are deck-level and immutable after the analysis passes. Each slide section must reference one of them.
- Use `direct`, `indirect`, `supplementary`, `proposed`, or `preliminary` as evidence strength. Do not present `proposed` or `preliminary` evidence as proven fact.

## Handoff

After validation:

1. derive `deck_order_map.md` from `navigation` and `slides`;
2. derive page briefs from each slide's claim, figures, evidence strength, and caution;
3. crop only figures declared in `figures` and preserve their source metadata in the figure-source manifest;
4. build the PPT through Route A, B, or C, without changing the evidence chain silently.
