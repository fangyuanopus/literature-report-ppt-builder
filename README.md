# Literature Report PPT Builder Skill

Open-source Codex skill for creating rigorous academic literature-report presentation decks from papers, supplementary information, and real source figures.

The bundled skill is `academic-slide-minimalist`. It is designed for Chinese academic paper presentations, journal-club decks, thesis-defense style reports, and image-first PPT workflows where layout stability and scientific traceability matter.

## What It Does

- Reads a main paper and supplementary information as one evidence system.
- Builds paper logic maps, figure-source manifests, adaptive navigation, and page-level briefs before slide generation.
- Creates image-first 16:9 PPT pages using real figures from the paper, SI, or user-provided materials.
- Preserves a restrained academic visual style based on the included sample deck rhythm.
- Audits page order, figure readability, terminology consistency, and speaker readiness.

## Non-Negotiable Rule

Scientific visuals must come from real source material only. The skill explicitly forbids inventing, regenerating, or redrawing experimental figures, structures, spectra, mechanisms, charts, tables, or other scientific data.

Allowed visual operations are limited to deterministic edits such as cropping, scaling, alignment, masking margins, callouts, boxes, arrows, labels, and full-slide placement.

## Repository Structure

```text
academic-slide-minimalist/
  SKILL.md
  agents/openai.yaml
  assets/sample-literature-report.pptx
  references/
```

`SKILL.md` contains the core workflow. The `references/` files provide progressive-disclosure guidance for specific production stages, including close reading, adaptive navigation, deck ordering, page briefs, image consistency, quality gates, and final delivery.

The sample PPTX is a style and rhythm reference only. It is not a scientific source and should not be reused as evidence for a new paper.

## Install

Copy the skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\academic-slide-minimalist "$env:USERPROFILE\.codex\skills\academic-slide-minimalist"
```

Then start a new Codex session so the skill metadata can be discovered.

## Example Prompts

```text
Use the academic-slide-minimalist skill to turn this paper and SI into a 20+ page Chinese literature-report PPT.
```

```text
按照这份样例 PPT 的节奏，帮我重构这篇论文的文献汇报，要求只使用论文真实图片。
```

```text
先诊断我这个已有文献汇报 PPT 的问题，再给出需要重画的页面清单。
```

## Validation

Validate the skill with the Codex skill validation script when available:

```powershell
$env:PYTHONUTF8 = "1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\academic-slide-minimalist
```

## License

MIT License. See `LICENSE`.
