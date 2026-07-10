#!/usr/bin/env python3
"""Draft a fallback_edit_plan.json from structured slide briefs.

This is the planning half of the Gorden-style fallback route. It does not build
the deck; it selects source template slides and maps brief content onto
inherited slots from sample-template-slot-manifest.json. The generated plan is a
draft: review it, shorten text if needed, then pass it to
build_fallback_template_pptx.py.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image


DEFAULT_MANIFEST = Path("academic-slide-minimalist/references/sample-template-slot-manifest.json")

ROLE_FALLBACKS = {
    "cover": ["cover"],
    "background": ["background", "method", "summary"],
    "method": ["method", "background", "result"],
    "result": ["result", "application", "method"],
    "application": ["application", "result", "summary"],
    "summary": ["summary", "ending", "background"],
    "ending": ["ending", "summary"],
    "backup": ["result", "application", "summary"],
}

FIGURE_ROLE_FALLBACKS = {
    "background": ["method", "result", "application", "background", "summary"],
    "summary": ["result", "application", "method", "summary", "background"],
    "ending": ["result", "application", "summary", "ending"],
}

# These source pages contain strong sample-paper visual content that is hard to
# neutralize by slot replacement alone. Keep them available as a last resort,
# but strongly prefer cleaner evidence pages for automatic fallback decks.
AUTO_AVOID_SOURCE_SLIDES = {3}


def load_manifest(path: Path) -> dict[str, Any]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["_pages_by_slide"] = {int(page["source_slide"]): page for page in manifest.get("pages", [])}
    return manifest


def normalize_briefs(data: dict[str, Any]) -> list[dict[str, Any]]:
    slides = data.get("slides") or data.get("slide_briefs") or []
    if not slides:
        raise ValueError("slide brief file must contain slides or slide_briefs")
    normalized = []
    for index, slide in enumerate(slides, 1):
        normalized.append(
            {
                **slide,
                "output_slide": int(slide.get("output_slide", slide.get("slide_no", index))),
                "role": slide.get("role") or slide.get("section_role") or "result",
            }
        )
    return normalized


def text_capacity(slot: dict[str, Any]) -> int:
    return int(slot.get("capacity", {}).get("max_chars") or 0)


def visual_width(text: str) -> float:
    width = 0.0
    for char in text:
        if "\u4e00" <= char <= "\u9fff" or "\u3000" <= char <= "\u303f" or "\uff00" <= char <= "\uffef":
            width += 1.0
        elif char == " ":
            width += 0.35
        elif char.isascii():
            width += 0.5
        else:
            width += 0.8
    return width


def compact_cover_subtitle(text: str, slot: dict[str, Any]) -> str:
    capacity = slot.get("capacity", {})
    max_width = float(capacity.get("chars_per_line") or capacity.get("max_chars") or 0)
    if float(capacity.get("font_size_pt") or 0) >= 48:
        max_width *= 0.78
    if not max_width or visual_width(text) <= max_width:
        return text
    candidates = []
    cleaned = text.replace("汇报", "").replace("报告", "").strip(" ：:-")
    candidates.append(cleaned)
    chinese_only = "".join(char for char in cleaned if "\u4e00" <= char <= "\u9fff")
    if chinese_only:
        candidates.append(chinese_only)
    for marker in ["机制", "方法", "模型", "框架", "算法", "系统"]:
        pos = chinese_only.find(marker)
        if pos > 0:
            candidates.append(chinese_only[: pos + len(marker)])
    for candidate in candidates:
        if candidate and visual_width(candidate) <= max_width:
            return candidate
    kept = ""
    for char in chinese_only or cleaned:
        if visual_width(kept + char) > max_width:
            break
        kept += char
    return kept or text


def slot_top(slot: dict[str, Any]) -> int:
    return int(slot.get("frame", {}).get("emu", {}).get("top") or 0)


def slot_area(slot: dict[str, Any]) -> int:
    frame = slot.get("frame", {}).get("emu", {})
    return int(frame.get("width") or 0) * int(frame.get("height") or 0)


def text_slots(page: dict[str, Any], *, editable_only: bool = True) -> list[dict[str, Any]]:
    slots = page.get("text_slots", [])
    if editable_only:
        slots = [slot for slot in slots if slot.get("editable")]
    return slots


def image_slots(page: dict[str, Any]) -> list[dict[str, Any]]:
    return [slot for slot in page.get("image_slots", []) if slot.get("editable", True)]


def find_title_slot(page: dict[str, Any], role: str) -> dict[str, Any] | None:
    slots = text_slots(page)
    if role == "cover":
        candidates = [slot for slot in slots if "cover title" in slot.get("role", "")]
    else:
        candidates = [slot for slot in slots if "slide title" in slot.get("role", "") or "title" in slot.get("role", "")]
    if not candidates:
        candidates = slots
    if not candidates:
        return None
    return sorted(candidates, key=lambda slot: (-text_capacity(slot), slot_top(slot)))[0]


def find_subtitle_slots(page: dict[str, Any], title_slot_id: str | None) -> list[dict[str, Any]]:
    slots = [slot for slot in text_slots(page) if slot["slot_id"] != title_slot_id]
    return sorted(slots, key=lambda slot: (-text_capacity(slot), slot_top(slot)))


def find_text_slot_by_current(page: dict[str, Any], pattern: str) -> dict[str, Any] | None:
    for slot in text_slots(page):
        if pattern in slot.get("current_text", ""):
            return slot
    return None


def find_caption_slots(page: dict[str, Any]) -> list[dict[str, Any]]:
    slots = [slot for slot in text_slots(page) if "caption" in slot.get("role", "") or "figure label" in slot.get("role", "")]
    return sorted(slots, key=lambda slot: (slot_top(slot), slot.get("frame", {}).get("emu", {}).get("left") or 0))


def find_body_slots(page: dict[str, Any], used_slot_ids: set[str]) -> list[dict[str, Any]]:
    slots = [
        slot
        for slot in text_slots(page)
        if slot["slot_id"] not in used_slot_ids
        and "navigation" not in slot.get("role", "")
        and "page number" not in slot.get("role", "")
        and "caption" not in slot.get("role", "")
        and "figure label" not in slot.get("role", "")
    ]
    return sorted(slots, key=lambda slot: (-text_capacity(slot), -slot_area(slot)))


def figure_count(brief: dict[str, Any]) -> int:
    return len(brief.get("figures") or [])


def candidate_roles_for(brief: dict[str, Any]) -> list[str]:
    role = brief["role"]
    if figure_count(brief):
        figure_roles = FIGURE_ROLE_FALLBACKS.get(role)
        if figure_roles:
            return figure_roles
    return ROLE_FALLBACKS.get(role, [role, "result", "summary"])


def figure_aspects(brief: dict[str, Any]) -> list[float]:
    aspects = []
    for figure in brief.get("figures") or []:
        image = figure.get("image") or figure.get("path") or figure.get("source")
        if not image:
            continue
        try:
            with Image.open(image) as im:
                aspects.append(im.width / im.height)
        except Exception:
            continue
    return aspects


def figure_profile(figure: dict[str, Any]) -> dict[str, Any]:
    image = figure.get("image") or figure.get("path") or figure.get("source")
    profile: dict[str, Any] = {
        "kind": figure.get("kind") or "unknown",
        "aspect": None,
        "layout_hint": "unknown",
        "dense": False,
    }
    if not image:
        return profile
    name = Path(str(image)).name.lower()
    try:
        with Image.open(image) as im:
            aspect = im.width / im.height
            profile["aspect"] = round(aspect, 4)
            profile["size"] = [im.width, im.height]
    except Exception:
        aspect = None
    if "table" in name or figure.get("kind") == "table":
        profile["kind"] = "table"
        profile["dense"] = True
    elif "fig" in name:
        profile["kind"] = "figure"
    if aspect is not None:
        if aspect >= 1.8:
            profile["layout_hint"] = "wide"
        elif aspect <= 0.8:
            profile["layout_hint"] = "portrait"
        elif 0.8 < aspect < 1.25:
            profile["layout_hint"] = "square"
        else:
            profile["layout_hint"] = "landscape"
    if profile["kind"] == "table" and profile["layout_hint"] in {"wide", "landscape"}:
        profile["preferred_frame"] = "wide-dominant"
    elif profile["layout_hint"] == "portrait":
        profile["preferred_frame"] = "tall"
    else:
        profile["preferred_frame"] = "balanced"
    return profile


def slot_aspect(slot: dict[str, Any]) -> float:
    frame = slot.get("frame", {}).get("emu", {})
    width = float(frame.get("width") or 1)
    height = float(frame.get("height") or 1)
    return width / height


def aspect_occupancy(image_aspect: float, frame_aspect: float) -> float:
    return min(image_aspect / frame_aspect, frame_aspect / image_aspect)


def figure_fit_score(page: dict[str, Any], brief: dict[str, Any]) -> int:
    aspects = figure_aspects(brief)
    if not aspects:
        return 0
    slots = sorted(image_slots(page), key=lambda slot: -slot_area(slot))
    if not slots:
        return -80 * len(aspects)
    occupancies = [
        aspect_occupancy(image_aspect, slot_aspect(slot))
        for image_aspect, slot in zip(aspects, slots)
    ]
    missing = max(0, len(aspects) - len(slots))
    return int(sum(occupancies) / max(1, len(occupancies)) * 80) - missing * 80


def page_score(page: dict[str, Any], brief: dict[str, Any], used_sources: set[int]) -> tuple[int, int, int, int]:
    source_slide = int(page["source_slide"])
    if source_slide in used_sources:
        return (-9999, 0, 0, 0)
    figures_needed = figure_count(brief)
    images = image_slots(page)
    role_score = 40 if page.get("role") == brief["role"] else 0
    figure_score = 0
    if figures_needed:
        figure_score = 80 - abs(len(images) - figures_needed) * 18
        if len(images) < figures_needed:
            figure_score -= 40 * (figures_needed - len(images))
        if len(images) > figures_needed:
            figure_score -= 8 * (len(images) - figures_needed)
    elif images:
        # Text-only briefs should not pick image-heavy pages just because the
        # role matches; that creates many delete edits and sparse layouts.
        figure_score -= 28 * len(images)
    if figures_needed and source_slide in AUTO_AVOID_SOURCE_SLIDES:
        figure_score -= 120
    if figures_needed and brief["role"] in {"summary", "ending"} and page.get("role") == "background":
        figure_score -= 60
    figure_score += figure_fit_score(page, brief)
    density_score = len(text_slots(page)) + min(len(images), 3) * 3
    return (role_score + figure_score + density_score, len(images), len(text_slots(page)), -source_slide)


def choose_source_page(manifest: dict[str, Any], brief: dict[str, Any], used_sources: set[int]) -> dict[str, Any]:
    pages_by_slide = manifest["_pages_by_slide"]
    candidate_roles = candidate_roles_for(brief)
    candidates = [
        page
        for page in pages_by_slide.values()
        if page.get("role") in candidate_roles and int(page["source_slide"]) not in used_sources
    ]
    if not candidates:
        candidates = [page for page in pages_by_slide.values() if int(page["source_slide"]) not in used_sources]
    if not candidates:
        raise ValueError("no unused source slides available; repeated source slides require a clone-capable builder")
    return sorted(candidates, key=lambda page: page_score(page, brief, used_sources), reverse=True)[0]


def normalize_body(brief: dict[str, Any]) -> list[str]:
    body = brief.get("body") or brief.get("bullets") or brief.get("notes") or []
    if isinstance(body, str):
        return [body]
    return [str(item) for item in body if str(item).strip()]


def make_text_edit(slot: dict[str, Any], text: str) -> dict[str, Any]:
    return {
        "slot_id": slot["slot_id"],
        "new_text": text,
    }


def make_plan_for_slide(page: dict[str, Any], brief: dict[str, Any]) -> dict[str, Any]:
    used_slot_ids: set[str] = set()
    edits: list[dict[str, Any]] = []
    slots_by_id = {
        slot["slot_id"]: slot
        for slot in page.get("text_slots", []) + page.get("image_slots", []) + page.get("object_slots", [])
    }

    title = brief.get("title") or brief.get("core_claim") or brief.get("claim")
    title_slot = find_title_slot(page, brief["role"])
    if title and title_slot:
        edits.append(make_text_edit(title_slot, str(title)))
        used_slot_ids.add(title_slot["slot_id"])

    if brief["role"] == "cover":
        subtitle = brief.get("subtitle") or brief.get("paper_title_cn")
        if subtitle:
            subtitle_candidates = [
                slot
                for slot in find_subtitle_slots(page, title_slot["slot_id"] if title_slot else None)
                if "\u6c47\u62a5" not in slot.get("current_text", "")
            ]
            if subtitle_candidates:
                slot = subtitle_candidates[0]
                edits.append(make_text_edit(slot, compact_cover_subtitle(str(subtitle), slot)))
                used_slot_ids.add(slot["slot_id"])
        speaker = brief.get("speaker")
        speaker_slot = find_text_slot_by_current(page, "\u6c47\u62a5\u4eba")
        if speaker and speaker_slot:
            edits.append(make_text_edit(speaker_slot, str(speaker)))
            used_slot_ids.add(speaker_slot["slot_id"])
        date = brief.get("date")
        date_slot = find_text_slot_by_current(page, "\u6c47\u62a5\u65e5\u671f")
        if date and date_slot:
            edits.append(make_text_edit(date_slot, str(date)))
            used_slot_ids.add(date_slot["slot_id"])
        meta = brief.get("meta") or []
        if isinstance(meta, str):
            meta = [meta]
        remaining_slots = [
            slot
            for slot in find_subtitle_slots(page, title_slot["slot_id"] if title_slot else None)
            if slot["slot_id"] not in used_slot_ids
        ]
        for slot, text in zip(remaining_slots, meta):
            edits.append(make_text_edit(slot, str(text)))
            used_slot_ids.add(slot["slot_id"])
    else:
        body_items = normalize_body(brief)
        body_slots = find_body_slots(page, used_slot_ids)
        if body_items and body_slots:
            if len(body_items) == 1:
                edits.append(make_text_edit(body_slots[0], body_items[0]))
                used_slot_ids.add(body_slots[0]["slot_id"])
            else:
                # Prefer one large inherited body slot for bullet-style content,
                # because splitting across tiny decorative labels often harms the template.
                edits.append(make_text_edit(body_slots[0], "\n".join(body_items)))
                used_slot_ids.add(body_slots[0]["slot_id"])

    figures = brief.get("figures") or []
    sorted_image_slots = sorted(image_slots(page), key=lambda slot: -slot_area(slot))
    for slot, figure in zip(sorted_image_slots, figures):
        image = figure.get("image") or figure.get("path") or figure.get("source")
        if image:
            profile = figure_profile(figure)
            edit = {
                "slot_id": slot["slot_id"],
                "new_image": str(image),
                "figure_profile": profile,
                "fit_strategy": "adaptive_contain",
            }
            if profile.get("dense") and profile.get("layout_hint") in {"wide", "landscape"}:
                edit["min_frame_occupancy"] = 0.4
            # When a single wide/dense figure lands on a multi-image template
            # page, use the inherited image region as one combined figure area
            # rather than leaving the real paper figure trapped in one small slot.
            if len(figures) == 1 and len(sorted_image_slots) > 1:
                edit["frame_scope"] = "all_image_slots"
            edits.append(edit)
            used_slot_ids.add(slot["slot_id"])

    captions = [figure.get("caption") or figure.get("label") for figure in figures if figure.get("caption") or figure.get("label")]
    for slot, caption in zip(find_caption_slots(page), captions):
        edits.append(make_text_edit(slot, str(caption)))
        used_slot_ids.add(slot["slot_id"])

    used_shape_paths = [
        (slots_by_id.get(slot_id, {}).get("address") or {}).get("shape_path", [])
        for slot_id in used_slot_ids
    ]
    for slot_id in page.get("delete_or_replace_objects", []):
        if slot_id not in used_slot_ids:
            object_slot = slots_by_id.get(slot_id, {})
            object_shape_id = (object_slot.get("address") or {}).get("shape_id")
            if object_shape_id is not None and any(object_shape_id in path for path in used_shape_paths):
                continue
            edits.append({"slot_id": slot_id, "action": "delete"})

    return {
        "output_slide": brief["output_slide"],
        "source_slide": page["source_slide"],
        "role": brief["role"],
        "reuse_mode": "template-prune",
        "brief_title": brief.get("title") or brief.get("core_claim") or "",
        "edits": edits,
    }


def draft_plan(briefs: list[dict[str, Any]], manifest: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    used_sources: set[int] = set()
    slide_map = []
    report_items = []
    for brief in briefs:
        page = choose_source_page(manifest, brief, used_sources)
        used_sources.add(int(page["source_slide"]))
        mapped = make_plan_for_slide(page, brief)
        slide_map.append(mapped)
        figures_needed = figure_count(brief)
        images_available = len(image_slots(page))
        aspects = figure_aspects(brief)
        chosen_slots = sorted(image_slots(page), key=lambda slot: -slot_area(slot))
        predicted_occupancy = [
            round(aspect_occupancy(image_aspect, slot_aspect(slot)), 4)
            for image_aspect, slot in zip(aspects, chosen_slots)
        ]
        figure_profiles = [figure_profile(figure) for figure in brief.get("figures") or []]
        delete_count = sum(1 for edit in mapped["edits"] if edit.get("action") == "delete")
        text_edit_count = sum(1 for edit in mapped["edits"] if "new_text" in edit)
        image_edit_count = sum(1 for edit in mapped["edits"] if "new_image" in edit)
        warnings = []
        if images_available < figures_needed:
            warnings.append(f"figure slots insufficient: need {figures_needed}, have {images_available}")
        if figures_needed and images_available > figures_needed + 2:
            warnings.append(f"source slide has many extra image slots: need {figures_needed}, have {images_available}")
        if predicted_occupancy and min(predicted_occupancy) < 0.45:
            warnings.append(f"low predicted image occupancy: {predicted_occupancy}")
        if delete_count > 8:
            warnings.append(f"many inherited objects will be deleted: {delete_count}")
        if not text_edit_count:
            warnings.append("no text edit mapped")
        report_items.append(
            {
                "output_slide": brief["output_slide"],
                "role": brief["role"],
                "brief_title": brief.get("title") or brief.get("core_claim") or "",
                "source_slide": page["source_slide"],
                "source_role": page.get("role"),
                "layout_type": page.get("layout_type"),
                "use_for": page.get("use_for"),
                "selection_guidance": page.get("selection_guidance"),
                "figures_needed": figures_needed,
                "image_slots_available": images_available,
                "predicted_image_occupancy": predicted_occupancy,
                "figure_profiles": figure_profiles,
                "text_edits": text_edit_count,
                "image_edits": image_edit_count,
                "delete_edits": delete_count,
                "warnings": warnings,
            }
        )
    plan = {
        "$schema": "academic-fallback-edit-plan/v1",
        "template_pptx": manifest.get("template_pptx"),
        "manifest": "references/sample-template-slot-manifest.json",
        "generation_route": "drafted-from-slide-briefs",
        "selected_slides": [item["source_slide"] for item in slide_map],
        "slide_map": slide_map,
    }
    report_warnings = sum(len(item["warnings"]) for item in report_items)
    report = {
        "$schema": "academic-fallback-plan-report/v1",
        "status": "needs_review" if report_warnings else "passed",
        "warning_count": report_warnings,
        "slides": report_items,
    }
    return plan, report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("briefs", type=Path, help="slide_briefs.json")
    parser.add_argument("out", type=Path, help="fallback_edit_plan.json")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--report", type=Path, help="optional fallback_plan_report.json")
    parser.add_argument("--fail-on-warnings", action="store_true", help="return non-zero when plan report needs review")
    args = parser.parse_args()

    brief_data = json.loads(args.briefs.read_text(encoding="utf-8"))
    manifest = load_manifest(args.manifest)
    plan, report = draft_plan(normalize_briefs(brief_data), manifest)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(args.out)
    if args.report:
        print(args.report)
    if args.fail_on_warnings and report["status"] != "passed":
        raise SystemExit(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
