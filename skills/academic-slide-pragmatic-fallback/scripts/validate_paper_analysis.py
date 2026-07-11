#!/usr/bin/env python3
"""Validate the evidence contract between paper reading and slide planning."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


LOGIC_FIELDS = (
    "research_object",
    "background",
    "unresolved_problem",
    "author_strategy",
    "methods",
    "key_conclusion",
    "limitations_and_inspiration",
)
EVIDENCE_STRENGTHS = {
    "direct",
    "indirect",
    "supplementary",
    "proposed",
    "preliminary",
}
SLIDE_ROLES_WITHOUT_EVIDENCE = {"cover", "paper_information", "closing", "section_divider"}


def required_text(data: dict[str, Any], field: str, issues: list[str], context: str) -> str:
    value = str(data.get(field, "")).strip()
    if not value:
        issues.append(f"{context}: missing {field}")
    return value


def unique_ids(items: list[dict[str, Any]], field: str, issues: list[str], context: str) -> set[str]:
    values: list[str] = []
    for index, item in enumerate(items, 1):
        value = required_text(item, field, issues, f"{context}[{index}]")
        if value:
            values.append(value)
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        issues.append(f"{context}: duplicate {field}: {duplicates}")
    return set(values)


def validate(data: dict[str, Any]) -> dict[str, Any]:
    issues: list[str] = []
    if data.get("$schema") != "academic-paper-analysis/v1":
        issues.append("$schema must be academic-paper-analysis/v1")

    paper = data.get("paper") or {}
    required_text(paper, "title", issues, "paper")
    required_text(paper, "domain", issues, "paper")
    source_files = list(paper.get("source_files") or [])
    source_ids = unique_ids(source_files, "source_id", issues, "paper.source_files")
    for index, source in enumerate(source_files, 1):
        required_text(source, "role", issues, f"paper.source_files[{index}]")
    if not source_files:
        issues.append("paper: source_files must include the main paper")
    elif not any(str(source.get("role", "")).strip() == "main" for source in source_files):
        issues.append("paper.source_files: one source must have role=main")

    logic_tree = data.get("logic_tree") or {}
    for field in LOGIC_FIELDS:
        required_text(logic_tree, field, issues, "logic_tree")

    figures = list(data.get("figures") or [])
    figure_ids = unique_ids(figures, "figure_id", issues, "figures")
    for index, figure in enumerate(figures, 1):
        context = f"figures[{index}]"
        source_id = required_text(figure, "source_id", issues, context)
        if source_id and source_id not in source_ids:
            issues.append(f"{context}: source_id {source_id!r} is not in paper.source_files")
        required_text(figure, "source_label", issues, context)
        if not isinstance(figure.get("source_page"), int) or figure["source_page"] < 1:
            issues.append(f"{context}: source_page must be a positive integer")
        required_text(figure, "direct_observation", issues, context)
        required_text(figure, "does_not_prove", issues, context)
        strength = required_text(figure, "evidence_strength", issues, context)
        if strength and strength not in EVIDENCE_STRENGTHS:
            issues.append(f"{context}: invalid evidence_strength {strength!r}")
    if not figures:
        issues.append("figures: at least one real paper/SI figure record is required")

    evidence_chains = list(data.get("evidence_chains") or [])
    evidence_ids = unique_ids(evidence_chains, "evidence_id", issues, "evidence_chains")
    for index, evidence in enumerate(evidence_chains, 1):
        context = f"evidence_chains[{index}]"
        for field in ("question", "interpretation", "slide_claim", "caution"):
            required_text(evidence, field, issues, context)
        referenced_figures = list(evidence.get("figure_ids") or [])
        if not referenced_figures:
            issues.append(f"{context}: figure_ids must not be empty")
        for figure_id in referenced_figures:
            if figure_id not in figure_ids:
                issues.append(f"{context}: unknown figure_id {figure_id!r}")
        strength = required_text(evidence, "evidence_strength", issues, context)
        if strength and strength not in EVIDENCE_STRENGTHS:
            issues.append(f"{context}: invalid evidence_strength {strength!r}")
    if not evidence_chains:
        issues.append("evidence_chains: at least one chain is required")

    navigation = list(data.get("navigation") or [])
    navigation_labels = unique_ids(navigation, "label", issues, "navigation")
    if not 3 <= len(navigation) <= 8:
        issues.append("navigation: use 3–8 labels")
    for index, item in enumerate(navigation, 1):
        required_text(item, "purpose", issues, f"navigation[{index}]")

    slides = list(data.get("slides") or [])
    slide_ids = unique_ids(slides, "slide_id", issues, "slides")
    if not slides:
        issues.append("slides: at least one slide is required")
    for index, slide in enumerate(slides, 1):
        context = f"slides[{index}]"
        if slide.get("slide_no") != index:
            issues.append(f"{context}: slide_no must be sequential and equal to {index}")
        required_text(slide, "page_role", issues, context)
        required_text(slide, "mainline_or_backup", issues, context)
        required_text(slide, "title", issues, context)
        section = required_text(slide, "section", issues, context)
        if section and section not in navigation_labels:
            issues.append(f"{context}: section {section!r} is not in navigation")
        evidence_refs = list(slide.get("evidence_ids") or [])
        figure_refs = list(slide.get("figure_ids") or [])
        if str(slide.get("page_role")) not in SLIDE_ROLES_WITHOUT_EVIDENCE and not evidence_refs:
            issues.append(f"{context}: content slide requires evidence_ids")
        for evidence_id in evidence_refs:
            if evidence_id not in evidence_ids:
                issues.append(f"{context}: unknown evidence_id {evidence_id!r}")
        for figure_id in figure_refs:
            if figure_id not in figure_ids:
                issues.append(f"{context}: unknown figure_id {figure_id!r}")
        if evidence_refs and not figure_refs:
            issues.append(f"{context}: evidence-led slide requires figure_ids")
    if len(slide_ids) != len(slides):
        issues.append("slides: each slide needs a unique slide_id")

    return {
        "$schema": "academic-paper-analysis-validation/v1",
        "status": "failed" if issues else "passed",
        "issues": issues,
        "counts": {
            "source_files": len(source_files),
            "figures": len(figures),
            "evidence_chains": len(evidence_chains),
            "navigation": len(navigation),
            "slides": len(slides),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("analysis", type=Path, help="paper_analysis.json")
    parser.add_argument("--out", type=Path, help="validation report JSON")
    parser.add_argument("--fail-on-review", action="store_true")
    args = parser.parse_args()
    result = validate(json.loads(args.analysis.read_text(encoding="utf-8")))
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 2 if args.fail_on_review and result["status"] != "passed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
