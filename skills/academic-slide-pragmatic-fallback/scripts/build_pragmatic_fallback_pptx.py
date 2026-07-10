#!/usr/bin/env python3
"""Build clean, editable academic fallback decks in the bundled sample style.

The deck is built from a blank 16:9 presentation. This intentionally avoids
the sample deck's content-bearing master/layout layers while preserving its
white ground, red-black-gray palette, quiet top navigation, title rule, and
footer/page-number rhythm.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


SLIDE_W, SLIDE_H = Inches(13.333), Inches(7.5)
RED, BLACK, GRAY, LIGHT = RGBColor(160, 15, 30), RGBColor(30, 30, 30), RGBColor(105, 105, 105), RGBColor(247, 247, 247)
FONT = "Microsoft YaHei"
FORBIDDEN_AUDIENCE_TEXT = ("pragmatic fallback", "editable fallback", "route c", "image2", "模板路径", "构建器")


def set_name(shape, name: str) -> None:
    shape.name = name


def set_east_asia_font(run) -> None:
    rpr = run._r.get_or_add_rPr()
    rpr.set("ea", FONT)


def add_rect(slide, name, x, y, w, h, color):
    shape = slide.shapes.add_shape(1, x, y, w, h)
    set_name(shape, name)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_text(slide, name, text, x, y, w, h, size, color=BLACK, bold=False, align=PP_ALIGN.LEFT, wrap=True):
    box = slide.shapes.add_textbox(x, y, w, h)
    set_name(box, name)
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = wrap
    frame.margin_left = frame.margin_right = Pt(0)
    frame.margin_top = frame.margin_bottom = Pt(0)
    frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    paragraph = frame.paragraphs[0]
    paragraph.alignment = align
    run = paragraph.add_run()
    run.text = str(text)
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    set_east_asia_font(run)
    return box


def title_copy(title: str) -> tuple[str, int, float]:
    title = title.strip()
    if len(title) > 54:
        raise ValueError("title exceeds 54 characters; rewrite it before building the slide")
    if len(title) <= 32:
        return title, 30, 0.54
    if "\n" not in title:
        midpoint = len(title) // 2
        split = max(title.rfind("，", 0, midpoint), title.rfind("：", 0, midpoint), title.rfind(" ", 0, midpoint))
        if split < 12:
            split = midpoint
        title = title[: split + 1].rstrip() + "\n" + title[split + 1 :].lstrip()
    return title, 24, 0.84


def validate_copy(item: dict) -> None:
    for value in [item.get("title", ""), item.get("takeaway", "")] + list(item.get("bullets") or []):
        lowered = str(value).lower()
        if any(term in lowered for term in FORBIDDEN_AUDIENCE_TEXT):
            raise ValueError(f"slide {item.get('slide_no')}: internal production text is not audience-facing: {value}")
    bullets = item.get("bullets") or []
    if len(bullets) > 5 or any(len(str(line)) > 58 for line in bullets):
        raise ValueError(f"slide {item.get('slide_no')}: shorten to at most five bullets of 58 characters")


def add_chrome(slide, navigation: list[str], section: str, slide_no: int, footer: str):
    if section not in navigation:
        raise ValueError(f"slide {slide_no}: section must be one of deck.navigation")
    add_rect(slide, "AGENT_NAV_BACKGROUND", 0, 0, SLIDE_W, Inches(0.43), LIGHT)
    slot_w = SLIDE_W / len(navigation)
    for index, label in enumerate(navigation):
        x = slot_w * index
        active = label == section
        if active:
            add_rect(slide, f"AGENT_NAV_ACTIVE_{index}", x, 0, slot_w, Inches(0.43), RED)
        add_text(slide, f"AGENT_NAV_LABEL_{index}", label, x, Inches(0.035), slot_w, Inches(0.29), 11, RGBColor(255, 255, 255) if active else BLACK, active, PP_ALIGN.CENTER, False)
    add_rect(slide, "AGENT_NAV_RULE", Inches(0.55), Inches(0.51), Inches(12.2), Inches(0.015), GRAY)
    if footer:
        add_text(slide, "AGENT_FOOTER", footer, Inches(0.8), Inches(7.06), Inches(8.8), Inches(0.16), 8, GRAY, False, PP_ALIGN.LEFT, False)
    add_text(slide, "AGENT_PAGE_NUMBER", str(slide_no), Inches(12.45), Inches(7.05), Inches(0.3), Inches(0.16), 8, GRAY, False, PP_ALIGN.RIGHT, False)


def add_title(slide, title: str):
    copy, size, height = title_copy(title)
    add_text(slide, "AGENT_TITLE", copy, Inches(0.8), Inches(0.63), Inches(11.8), Inches(height), size, BLACK, True, PP_ALIGN.LEFT, True)
    add_rect(slide, "AGENT_TITLE_RULE", Inches(0.8), Inches(0.63 + height + 0.05), Inches(3.15), Inches(0.018), RED)


def add_bullets(slide, bullets: list[str], x, y, w, h, size=18):
    if not bullets:
        return
    text = "\n".join(f"• {line}" for line in bullets)
    add_text(slide, "AGENT_BODY", text, x, y, w, h, size, BLACK, False, PP_ALIGN.LEFT, True)


def add_figure(slide, figure: dict, x, y, w, h, slide_no: int, index: int):
    path = Path(figure.get("path", ""))
    if not path.is_file():
        raise FileNotFoundError(f"slide {slide_no}: missing prepared figure: {path}")
    required = ("figure_id", "source_page", "source_label")
    if figure.get("source_type") != "figure_crop" or figure.get("crop_verified") is not True or any(not figure.get(key) for key in required):
        raise ValueError(f"slide {slide_no}: figure needs figure_crop, crop_verified=true, figure_id, source_page, and source_label")
    with Image.open(path) as image:
        ratio = image.width / image.height
    frame_ratio = w / h
    if ratio >= frame_ratio:
        actual_w, actual_h = w, int(w / ratio)
        actual_x, actual_y = x, y + int((h - actual_h) / 2)
    else:
        actual_w, actual_h = int(h * ratio), h
        actual_x, actual_y = x + int((w - actual_w) / 2), y
    picture = slide.shapes.add_picture(str(path), actual_x, actual_y, actual_w, actual_h)
    set_name(picture, f"AGENT_FIGURE_{figure['figure_id']}")
    caption = figure.get("caption") or f"来源：{figure['source_label']}（论文第 {figure['source_page']} 页）"
    add_text(slide, f"AGENT_FIGURE_CAPTION_{index}", caption, x, y + h + Inches(0.02), w, Inches(0.18), 9, GRAY, False, PP_ALIGN.CENTER, False)


def layout_cover(slide, item):
    add_text(slide, "AGENT_COVER_TITLE", item["title"], Inches(1.2), Inches(2.2), Inches(10.9), Inches(1.0), 34, BLACK, True, PP_ALIGN.CENTER, True)
    meta = item.get("metadata") or item.get("bullets") or []
    if meta:
        add_text(slide, "AGENT_COVER_META", "\n".join(str(x) for x in meta[:5]), Inches(2.0), Inches(3.45), Inches(9.3), Inches(1.35), 16, GRAY, False, PP_ALIGN.CENTER, True)
    if item.get("takeaway"):
        add_text(slide, "AGENT_TAKEAWAY", item["takeaway"], Inches(1.1), Inches(6.1), Inches(11.1), Inches(0.3), 15, RED, True, PP_ALIGN.CENTER, True)


def layout_text(slide, item):
    add_title(slide, item["title"])
    add_bullets(slide, item.get("bullets") or [], Inches(1.0), Inches(1.65), Inches(11.0), Inches(4.7), 20)


def layout_figure_right(slide, item):
    add_title(slide, item["title"])
    figures = item.get("figures") or []
    if len(figures) != 1:
        raise ValueError("figure_right requires exactly one figure")
    add_bullets(slide, item.get("bullets") or [], Inches(0.95), Inches(1.65), Inches(4.55), Inches(4.55), 18)
    add_figure(slide, figures[0], Inches(6.0), Inches(1.55), Inches(6.1), Inches(4.75), item["slide_no"], 0)


def layout_figure_wide(slide, item):
    add_title(slide, item["title"])
    figures = item.get("figures") or []
    if len(figures) != 1:
        raise ValueError("figure_wide requires exactly one figure")
    add_figure(slide, figures[0], Inches(0.95), Inches(1.55), Inches(11.45), Inches(3.9), item["slide_no"], 0)
    add_bullets(slide, item.get("bullets") or [], Inches(1.0), Inches(5.75), Inches(11.0), Inches(0.72), 17)


def layout_process(slide, item):
    add_title(slide, item["title"])
    steps = item.get("steps") or []
    if not 2 <= len(steps) <= 5:
        raise ValueError("process requires 2–5 short steps")
    width = Inches(10.9 / len(steps))
    for index, step in enumerate(steps):
        x = Inches(1.15) + index * width
        add_rect(slide, f"AGENT_STEP_BOX_{index}", x, Inches(3.0), width - Inches(0.16), Inches(1.0), LIGHT)
        add_text(slide, f"AGENT_STEP_TEXT_{index}", step, x + Inches(0.08), Inches(3.15), width - Inches(0.32), Inches(0.7), 18, BLACK, True, PP_ALIGN.CENTER, True)
        if index < len(steps) - 1:
            add_text(slide, f"AGENT_STEP_ARROW_{index}", "→", x + width - Inches(0.08), Inches(3.21), Inches(0.18), Inches(0.4), 20, RED, True, PP_ALIGN.CENTER, False)
    add_bullets(slide, item.get("bullets") or [], Inches(1.1), Inches(4.65), Inches(10.9), Inches(1.15), 18)


def layout_comparison(slide, item):
    add_title(slide, item["title"])
    columns = item.get("columns") or []
    if len(columns) != 2:
        raise ValueError("comparison requires exactly two columns")
    for index, column in enumerate(columns):
        x = Inches(0.95 + index * 5.85)
        add_text(slide, f"AGENT_COLUMN_HEAD_{index}", column.get("heading", ""), x, Inches(1.65), Inches(5.15), Inches(0.35), 21, RED, True, PP_ALIGN.LEFT, True)
        add_bullets(slide, column.get("bullets") or [], x, Inches(2.15), Inches(5.15), Inches(3.7), 18)


def layout_summary(slide, item):
    add_title(slide, item["title"])
    rows = item.get("summary_rows") or []
    if not 2 <= len(rows) <= 5:
        raise ValueError("summary requires 2–5 summary_rows")
    row_h = Inches(4.65 / len(rows))
    for index, row in enumerate(rows):
        y = Inches(1.55) + index * row_h
        add_rect(slide, f"AGENT_SUMMARY_LINE_{index}", Inches(0.95), y, Inches(11.35), Inches(0.012), RED)
        add_text(slide, f"AGENT_SUMMARY_LABEL_{index}", row.get("label", ""), Inches(1.05), y + Inches(0.12), Inches(2.0), row_h - Inches(0.18), 19, RED, True, PP_ALIGN.LEFT, True)
        add_text(slide, f"AGENT_SUMMARY_VALUE_{index}", row.get("value", ""), Inches(3.2), y + Inches(0.12), Inches(8.65), row_h - Inches(0.18), 18, BLACK, False, PP_ALIGN.LEFT, True)


def layout_closing(slide, item):
    add_text(slide, "AGENT_CLOSING", item.get("closing_text", "感谢聆听 · 欢迎提问"), Inches(1.2), Inches(2.8), Inches(10.9), Inches(0.75), 30, BLACK, True, PP_ALIGN.CENTER, True)
    if item.get("metadata"):
        add_text(slide, "AGENT_CLOSING_META", "\n".join(item["metadata"][:3]), Inches(2.0), Inches(4.1), Inches(9.3), Inches(0.8), 13, GRAY, False, PP_ALIGN.CENTER, True)


def infer_layout(item: dict) -> str:
    if item.get("layout_type"):
        return item["layout_type"]
    if item.get("closing_text"):
        return "closing"
    if item.get("slide_no") == 1:
        return "cover"
    if item.get("steps"):
        return "process"
    if item.get("columns"):
        return "comparison"
    if item.get("summary_rows"):
        return "summary"
    figures = item.get("figures") or []
    if len(figures) == 1:
        with Image.open(figures[0]["path"]) as image:
            return "figure_wide" if image.width / image.height >= 1.15 else "figure_right"
    return "text"


LAYOUTS = {"cover": layout_cover, "text": layout_text, "figure_right": layout_figure_right, "figure_wide": layout_figure_wide, "process": layout_process, "comparison": layout_comparison, "summary": layout_summary, "closing": layout_closing}


def build(plan: dict, output: Path) -> dict:
    deck, slides = plan.get("deck") or {}, plan.get("slides") or []
    navigation = deck.get("navigation") or []
    if not (3 <= len(navigation) <= 7) or not slides:
        raise ValueError("deck needs 3–7 navigation labels and at least one slide")
    prs = Presentation()
    prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H
    footer = deck.get("footer", "")
    used_layouts = []
    for item in slides:
        item = dict(item)
        item["slide_no"] = int(item.get("slide_no", 0))
        if item["slide_no"] < 1 or not item.get("title"):
            raise ValueError("every slide needs slide_no and title")
        validate_copy(item)
        layout = infer_layout(item)
        if layout not in LAYOUTS:
            raise ValueError(f"slide {item['slide_no']}: unsupported layout_type {layout}")
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        add_chrome(slide, navigation, item.get("section") or navigation[0], item["slide_no"], footer)
        LAYOUTS[layout](slide, item)
        if item.get("takeaway") and layout not in ("cover", "closing"):
            add_text(slide, "AGENT_TAKEAWAY", item["takeaway"], Inches(0.95), Inches(6.55), Inches(11.15), Inches(0.3), 16, RED, True, PP_ALIGN.LEFT, True)
        used_layouts.append(layout)
    output.parent.mkdir(parents=True, exist_ok=True)
    prs.save(output)
    return {"status": "passed", "slide_count": len(slides), "output": str(output), "route": "pragmatic_fallback", "layouts": used_layouts}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = build(json.loads(args.plan.read_text(encoding="utf-8")), args.out)
    data = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.write_text(data, encoding="utf-8")
    print(data, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
