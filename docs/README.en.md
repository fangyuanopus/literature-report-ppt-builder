# academic-slide-minimalist

Read the paper and supplementary information first, then build a Chinese academic presentation that explains the evidence chain clearly.

English | [中文](../README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)](../academic-slide-minimalist/SKILL.md)
[![PPTX](https://img.shields.io/badge/output-PPTX-orange)](../academic-slide-minimalist/assets/sample-literature-report.pptx)
[![Language](https://img.shields.io/badge/deck_language-Chinese-red)](README.en.md)

`academic-slide-minimalist` is a Claude Code / Codex skill for rigorous academic literature-report decks. It is designed for Chinese paper presentations, journal clubs, course reports, thesis-defense rehearsals, and image-first PPT workflows.

The core principle is simple: **clarity before beauty, real evidence before visual tricks**.

---

## Demo

The pages below are exported from `academic-slide-minimalist/assets/sample-literature-report.pptx`. They show the intended deck style: real paper figures, conclusion-style titles, restrained red/black/gray academic design, consistent navigation, and traceable evidence.

### Evidence-chain page

![Evidence chain demo](images/demo-evidence-chain.png)

This page type combines characterization evidence and catalytic results into one causal chain. The goal is not to pile up figures, but to make each figure answer a specific question.

### Comparison-summary page

![Comparison summary demo](images/demo-comparison-summary.png)

This page type extracts two or three conclusions from multiple controls. The side panel turns visual trends into speaker-ready claims, and the bottom bar locks the key takeaway.

### Parameter-window page

![Parameter window demo](images/demo-parameter-window.png)

This page type explains why more is not always better. It works well for dose, ratio, temperature, time, loading, and other experimental variables.

### Mechanism-evidence page

![FTIR mechanism demo](images/demo-ftir-mechanism.png)

This page type presents direct mechanistic evidence. It keeps the real spectrum, highlights key regions, and turns experimental observations into a cautious mechanism claim.

---

## What Problem It Solves

Many AI PPT tools can make slides look polished, but academic presentations usually fail for different reasons:

- The model summarizes figures without understanding the paper's argument.
- Fake or redrawn scientific visuals appear in place of real paper figures.
- Slide titles describe topics instead of conclusions.
- Dense results are hidden inside one generic "Results" section.
- Separately generated pages have inconsistent navigation, numbering, typography, and annotation style.
- The final deck lacks backup slides, Q&A preparation, and a traceable figure-source record.

`academic-slide-minimalist` reverses that order: it first controls paper logic, source figures, and evidence strength, then designs the slide pages.

---

## Core Capabilities

### 1. Full paper-to-PPT workflow

The skill starts from a main paper plus supplementary information and follows a staged workflow:

```text
close reading
-> paper logic tree
-> terminology table
-> main/SI evidence crosswalk
-> figure source manifest
-> adaptive navigation
-> deck order map
-> page briefs
-> image2 page generation
-> PPTX assembly
-> render audit / Q&A prep
```

This is not a shallow summary. It converts the paper's argument into a speakable, defensible, traceable slide sequence.

### 2. Real scientific figures only

Scientific visuals must come from the main paper, supplementary information, user-provided screenshots, raw figures, or user-provided PPT pages.

The skill forbids generating or redrawing experimental data, including molecular structures, crystal structures, spectra, microscopy images, XRD/NMR/IR/Raman/TG/DSC, adsorption curves, mechanisms, and performance charts. Allowed operations are deterministic only: crop, scale, align, mask margins, add boxes, arrows, labels, and short callouts.

### 3. Adaptive navigation

The sample rhythm may look like:

```text
Cover -> Basic Information -> Background -> Research Idea -> Results -> Summary -> Closing
```

But the actual deck should derive navigation from the current paper. A catalysis or materials paper may use:

```text
Basic Info | Background | Design Strategy | Performance | Structure Evidence | Mechanism | Summary | Backup
```

Algorithm, biology, computational, and review papers can use different navigation grammars.

### 4. Image-first stable delivery

The default output is image-first: each slide is generated as a complete 16:9 page image, then inserted into PPTX. This reduces layout drift, font substitution, misplaced elements, and cross-device rendering problems.

Editable output is treated as a separate mode and is used only when explicitly requested.

### 5. Quality gates and Q&A preparation

The references cover deck order, figure-source manifests, image readability, terminology control, evidence strength, backup slides, advisor questions, final preview, and render audit.

---

## Who It Is For

- Students and researchers preparing Chinese literature-report presentations.
- Users who need a 20+ page journal-club or group-meeting deck from one paper.
- Users with a sample deck who want a new paper rebuilt in the same academic rhythm.
- Academic scenarios where real paper figures and traceability matter.
- Users who want to diagnose an existing deck before redrawing or reordering it.

It is not intended for generic business decks, flashy concept pages, fake experimental data, redrawn paper figures, or synthetic visuals that merely look scientific.

---

## Installation

### Option 1: Ask your AI assistant to install it

Send this to Codex / Claude Code:

```text
Install this Codex skill:
https://github.com/fangyuanopus/literature-report-ppt-builder

Install it into my local skills directory and tell me how to invoke it after restart.
```

### Option 2: Manual install for Codex

```powershell
git clone https://github.com/fangyuanopus/literature-report-ppt-builder.git
cd literature-report-ppt-builder
Copy-Item -Recurse .\academic-slide-minimalist "$env:USERPROFILE\.codex\skills\academic-slide-minimalist"
```

Restart Codex so the skill metadata can be discovered.

### Option 3: Manual install for Claude Code

```bash
git clone https://github.com/fangyuanopus/literature-report-ppt-builder.git
cd literature-report-ppt-builder
mkdir -p ~/.claude/skills
cp -R academic-slide-minimalist ~/.claude/skills/academic-slide-minimalist
```

---

## Usage Examples

### Build a complete literature-report deck

```text
Use academic-slide-minimalist to turn this main paper and SI into a Chinese literature-report PPT.
Use at least 20 slides. Use only real figures from the paper and SI. First build the paper logic and deck order, then generate the PPT.
```

### Follow a sample deck rhythm

```text
Follow the page rhythm and restrained red/black/gray academic style of my sample PPT.
Do not hard-code the navigation. Split it based on the paper's evidence chain.
```

### Diagnose an existing PPT

```text
First diagnose this literature-report PPT.
Check the mainline, page order, navigation, figure readability, conclusion-style titles, and Q&A risks.
Classify pages into must-redraw, local-repair, and keep.
```

### Close-read a paper paragraph by paragraph

```text
Use the close-reading mode of academic-slide-minimalist.
Translate and explain this paper paragraph by paragraph. Process only one original paragraph at a time and wait for me to say "continue".
```

---

## Outputs

Depending on the task, the skill may generate or maintain:

```text
paper_logic_tree.md
terminology_table.md
main_si_crosswalk.md
figure_source_manifest.md
adaptive_navigation_plan.md
deck_order_map.md
slide_outline.md
page_briefs.md
image2_generation_plan.md
image_generation_status.md
speaker_notes.md
quality_check_report.md
deck_diagnosis_report.md
redraw_priority_plan.md
final_delivery_preview.md
final_presentation.pptx
```

The default final deliverable is a stable image-first PPTX. For complex tasks, keep `figure_source_manifest.md` and `deck_order_map.md` so every figure and claim can be traced back before the presentation.

---

## Repository Structure

```text
academic-slide-minimalist/
  SKILL.md
  agents/
    openai.yaml
  assets/
    sample-literature-report.pptx
  references/
    close-reading-rules.md
    paper-to-ppt-workflow.md
    adaptive-navigation.md
    deck-order-map.md
    figure-source-manifest.md
    quality-gates.md
    ...
docs/
  README.en.md
  images/
    demo-evidence-chain.png
    demo-comparison-summary.png
    demo-parameter-window.png
    demo-ftir-mechanism.png
```

`SKILL.md` is the entry point. `references/` uses progressive disclosure: each stage loads only the rules it needs.

`assets/sample-literature-report.pptx` is a style and rhythm reference, not a scientific source for new papers.

---

## Built-in Reference Modules

| Module | Purpose |
| --- | --- |
| `close-reading-rules.md` | Paragraph-level reading, translation, terminology control, and commentary |
| `paper-to-ppt-workflow.md` | Main paper-to-PPT production process |
| `adaptive-navigation.md` | Domain-specific navigation design |
| `deck-order-map.md` | Page order, section, title, source figures, and backup state |
| `figure-source-manifest.md` | Source tracking for every figure and claim |
| `page-brief-template.md` | Page brief before generation |
| `quality-gates.md` | Final quality checks |
| `question-prep.md` | Advisor/teacher Q&A preparation |
| `backup-slides.md` | Backup slide planning |

---

## Difference from Generic AI PPT Skills

| Dimension | Generic AI PPT generation | academic-slide-minimalist |
| --- | --- | --- |
| Priority | Visual polish first | Paper logic and evidence first |
| Figure source | May create concept visuals | Real paper/SI/user figures only |
| Page organization | Often follows figure order | Organized by problem, strategy, evidence, mechanism, and takeaway |
| Navigation | Fixed template | Derived from the paper domain |
| Output stability | Editable but layout may drift | Image-first stable pages by default |
| Defense prep | Usually absent | Speaker notes, backup, and Q&A risks |

---

## Validation

If you have the Codex `skill-creator` system skill locally:

```powershell
$env:PYTHONUTF8 = "1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\academic-slide-minimalist
```

Expected output:

```text
Skill is valid!
```

---

## Acknowledgements

The README presentation style is inspired by strong open-source skill projects, especially [JuneYaooo/gpt-image2-ppt-skills](https://github.com/JuneYaooo/gpt-image2-ppt-skills) and its clear use of demos, installation steps, and usage examples.

Thanks to LINUX DO and other Chinese AI developer communities for sharing practical Claude Code / Codex / image2 / PPT workflows.

---

## Open-source Notes

This repository provides the skill workflow, prompt rules, references, and sample rhythm. Users are responsible for checking permission to use papers, SI files, screenshots, and sample PPT materials in their own classroom, group meeting, or public presentation context.

This project does not support fabricating experimental data, fake paper figures, or misleading scientific conclusions.

---

## License

MIT License. See [LICENSE](../LICENSE).
