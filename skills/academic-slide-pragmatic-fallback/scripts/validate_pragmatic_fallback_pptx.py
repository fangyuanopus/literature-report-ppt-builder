#!/usr/bin/env python3
"""Structural QA for the clean pragmatic fallback route."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE


def all_shapes(shapes):
    for shape in shapes:
        yield shape
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from all_shapes(shape.shapes)


def intersects(a, b) -> bool:
    return not (a.left + a.width <= b.left or b.left + b.width <= a.left or a.top + a.height <= b.top or b.top + b.height <= a.top)


def check_overlap(shapes):
    content = [s for s in shapes if any(s.name.startswith(prefix) for prefix in ("AGENT_BODY", "AGENT_FIGURE_", "AGENT_TAKEAWAY", "AGENT_COLUMN_", "AGENT_STEP_TEXT", "AGENT_SUMMARY_LABEL", "AGENT_SUMMARY_VALUE")) and "CAPTION" not in s.name]
    return [f"{a.name} overlaps {b.name}" for index, a in enumerate(content) for b in content[index + 1 :] if intersects(a, b)]


def validate(pptx: Path, plan: dict) -> dict:
    prs, expected = Presentation(pptx), plan.get("slides") or []
    issues, pages = [], []
    if len(prs.slides) != len(expected):
        issues.append(f"slide count mismatch: deck={len(prs.slides)} plan={len(expected)}")
    nav_count = len((plan.get("deck") or {}).get("navigation") or [])
    for index, slide in enumerate(prs.slides, 1):
        shapes = list(all_shapes(slide.shapes))
        names = [shape.name for shape in shapes]
        texts = [shape.text.strip() for shape in shapes if getattr(shape, "has_text_frame", False) and shape.text.strip()]
        figures = [name for name in names if name.startswith("AGENT_FIGURE_") and "CAPTION" not in name]
        expected_figures = (expected[index - 1].get("figures") or []) if index <= len(expected) else []
        if len([name for name in names if name.startswith("AGENT_NAV_LABEL_")]) != nav_count:
            issues.append(f"slide {index}: duplicated or incomplete navigation")
        if len(figures) != len(expected_figures):
            issues.append(f"slide {index}: figures deck={len(figures)} plan={len(expected_figures)}")
        unowned = [name for name in names if not name.startswith("AGENT_")]
        if unowned:
            issues.append(f"slide {index}: unowned shapes: {', '.join(unowned[:4])}")
        for shape in shapes:
            if shape.left < 0 or shape.top < 0 or shape.left + shape.width > prs.slide_width or shape.top + shape.height > prs.slide_height:
                issues.append(f"slide {index}: outside canvas: {shape.name}")
        for text in texts:
            if re.search(r"\b(?:fig\.?\s*\d+|route\s*[abc]|image2|fallback)\b", text, re.I) and not figures:
                issues.append(f"slide {index}: unsupported visible internal/figure reference: {text[:80]}")
        for overlap in check_overlap(shapes):
            issues.append(f"slide {index}: {overlap}")
        pages.append({"slide_no": index, "shape_count": len(shapes), "figure_count": len(figures)})
    return {"$schema": "academic-pragmatic-fallback-audit/v2", "pptx": str(pptx), "status": "failed" if issues else "passed", "issues": issues, "slides": pages}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--fail-on-review", action="store_true")
    args = parser.parse_args()
    result = validate(args.pptx, json.loads(args.plan.read_text(encoding="utf-8")))
    data = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(data, encoding="utf-8")
    else:
        print(data, end="")
    return 0 if result["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
