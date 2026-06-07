#!/usr/bin/env python3
"""Validate that a PPTX is an image-only container for Image2 full-slide pages.

Checks:
- every slide contains exactly one picture
- that picture fills the slide canvas
- no editable text boxes, shapes, charts, tables, SmartArt, or extra graphic frames
- optional image2_manifest.json confirms Image2 full-slide route for every slide

Usage:
    python scripts/validate_image_only_pptx.py final.pptx
    python scripts/validate_image_only_pptx.py final.pptx --manifest image2_manifest.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
}

TOLERANCE_EMU = 1000


def _parse_xml(zf: zipfile.ZipFile, name: str) -> ET.Element:
    return ET.fromstring(zf.read(name))


def _slide_sort_key(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 10**9


def _presentation_size(zf: zipfile.ZipFile) -> tuple[int, int]:
    root = _parse_xml(zf, "ppt/presentation.xml")
    sld_sz = root.find("p:sldSz", NS)
    if sld_sz is None:
        raise ValueError("ppt/presentation.xml has no slide size")
    return int(sld_sz.attrib["cx"]), int(sld_sz.attrib["cy"])


def _is_full_slide(pic: ET.Element, slide_cx: int, slide_cy: int) -> bool:
    xfrm = pic.find("p:spPr/a:xfrm", NS)
    if xfrm is None:
        return False
    off = xfrm.find("a:off", NS)
    ext = xfrm.find("a:ext", NS)
    if off is None or ext is None:
        return False
    x = int(off.attrib.get("x", "0"))
    y = int(off.attrib.get("y", "0"))
    cx = int(ext.attrib.get("cx", "0"))
    cy = int(ext.attrib.get("cy", "0"))
    return (
        abs(x) <= TOLERANCE_EMU
        and abs(y) <= TOLERANCE_EMU
        and abs(cx - slide_cx) <= TOLERANCE_EMU
        and abs(cy - slide_cy) <= TOLERANCE_EMU
    )


def _validate_manifest(manifest_path: Path, slide_count: int) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"manifest cannot be read as JSON: {exc}"]

    if data.get("image2_backend_confirmed") is not True:
        errors.append("manifest image2_backend_confirmed must be true")

    slides = data.get("slides")
    if not isinstance(slides, list):
        errors.append("manifest slides must be a list")
        return errors

    if len(slides) != slide_count:
        errors.append(f"manifest slide count {len(slides)} != PPTX slide count {slide_count}")

    seen = set()
    for index, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            errors.append(f"manifest slide {index} is not an object")
            continue
        slide_no = slide.get("slide_no", index)
        if slide_no in seen:
            errors.append(f"manifest duplicate slide_no {slide_no}")
        seen.add(slide_no)
        if slide.get("generation_route") != "image2_full_slide":
            errors.append(f"slide {slide_no}: generation_route is not image2_full_slide")
        if slide.get("accepted") is not True:
            errors.append(f"slide {slide_no}: accepted must be true")
        final_image = slide.get("final_image")
        if not final_image:
            errors.append(f"slide {slide_no}: final_image is missing")
        else:
            final_path = (manifest_path.parent / str(final_image)).resolve()
            if not final_path.exists():
                errors.append(f"slide {slide_no}: final_image does not exist: {final_image}")
    return errors


def validate_pptx(pptx_path: Path, manifest_path: Path | None = None) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not pptx_path.exists():
        return False, [f"PPTX does not exist: {pptx_path}"]

    try:
        with zipfile.ZipFile(pptx_path) as zf:
            slide_cx, slide_cy = _presentation_size(zf)
            slide_names = sorted(
                [name for name in zf.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", name)],
                key=_slide_sort_key,
            )
            if not slide_names:
                errors.append("PPTX contains no slides")

            for slide_index, slide_name in enumerate(slide_names, start=1):
                root = _parse_xml(zf, slide_name)
                pics = root.findall(".//p:pic", NS)
                shapes = root.findall(".//p:sp", NS)
                graphic_frames = root.findall(".//p:graphicFrame", NS)
                group_shapes = root.findall(".//p:grpSp", NS)
                connectors = root.findall(".//p:cxnSp", NS)
                charts = root.findall(".//c:chart", NS)
                tables = root.findall(".//a:tbl", NS)

                if len(pics) != 1:
                    errors.append(f"slide {slide_index}: expected exactly 1 picture, found {len(pics)}")
                elif not _is_full_slide(pics[0], slide_cx, slide_cy):
                    errors.append(f"slide {slide_index}: picture does not fill the full slide canvas")

                if shapes:
                    errors.append(f"slide {slide_index}: contains {len(shapes)} editable shape(s)/text box(es)")
                if graphic_frames:
                    errors.append(f"slide {slide_index}: contains {len(graphic_frames)} editable graphic frame(s)")
                if group_shapes:
                    errors.append(f"slide {slide_index}: contains {len(group_shapes)} group shape(s)")
                if connectors:
                    errors.append(f"slide {slide_index}: contains {len(connectors)} connector shape(s)")
                if charts:
                    errors.append(f"slide {slide_index}: contains chart object(s)")
                if tables:
                    errors.append(f"slide {slide_index}: contains table object(s)")

            if manifest_path is not None:
                errors.extend(_validate_manifest(manifest_path, len(slide_names)))
    except zipfile.BadZipFile:
        return False, ["file is not a valid PPTX/ZIP archive"]
    except Exception as exc:  # noqa: BLE001
        return False, [f"validation failed unexpectedly: {exc}"]

    return not errors, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an Image2 image-only PPTX.")
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--manifest", type=Path, default=None)
    args = parser.parse_args()

    ok, errors = validate_pptx(args.pptx, args.manifest)
    if ok:
        print("PASS: PPTX is image-only and satisfies the Image2 container checks.")
        return 0

    print("FAIL: PPTX did not pass image-only/Image2 validation.")
    for err in errors:
        print(f"- {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
