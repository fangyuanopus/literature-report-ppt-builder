#!/usr/bin/env python3
"""Prepare real paper figures for fallback template slots.

Paper-extracted figures often include large white margins from PDF crops. If
those margins are inserted into an inherited template image frame, the actual
scientific figure appears off-center or too small. This helper trims background
margins while preserving the real figure pixels.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageOps, ImageStat


def corner_background(image: Image.Image, sample: int = 12) -> tuple[int, int, int]:
    rgb = image.convert("RGB")
    w, h = rgb.size
    boxes = [
        (0, 0, min(sample, w), min(sample, h)),
        (max(0, w - sample), 0, w, min(sample, h)),
        (0, max(0, h - sample), min(sample, w), h),
        (max(0, w - sample), max(0, h - sample), w, h),
    ]
    values = []
    for box in boxes:
        stat = ImageStat.Stat(rgb.crop(box))
        values.append(tuple(int(v) for v in stat.median))
    return tuple(sorted(channel)[len(channel) // 2] for channel in zip(*values))


def trim_background(
    image: Image.Image,
    threshold: int = 246,
    padding: int = 10,
    tolerance: int = 18,
) -> tuple[Image.Image, dict[str, Any]]:
    rgba = image.convert("RGBA")
    rgb = rgba.convert("RGB")
    bg = corner_background(rgb)
    # Treat both near-white and corner-background-color pixels as background.
    diff = ImageChops.difference(rgb, Image.new("RGB", rgb.size, bg))
    diff_gray = ImageOps.grayscale(diff)
    bg_mask = diff_gray.point(lambda px: 0 if px <= tolerance else 255, mode="L")
    white_gray = ImageOps.grayscale(rgb)
    white_mask = white_gray.point(lambda px: 0 if px >= threshold else 255, mode="L")
    mask = ImageChops.lighter(bg_mask, white_mask)
    alpha = rgba.getchannel("A")
    alpha_mask = alpha.point(lambda px: 0 if px <= 8 else 255, mode="L")
    mask = ImageChops.multiply(mask, alpha_mask)
    bbox = mask.getbbox()
    if not bbox:
        return rgba, {
            "bbox": [0, 0, rgba.width, rgba.height],
            "removed": {"left": 0, "top": 0, "right": 0, "bottom": 0},
            "changed": False,
        }
    left, top, right, bottom = bbox
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(rgba.width, right + padding)
    bottom = min(rgba.height, bottom + padding)
    meta = {
        "bbox": [left, top, right, bottom],
        "removed": {
            "left": left,
            "top": top,
            "right": rgba.width - right,
            "bottom": rgba.height - bottom,
        },
        "changed": (left, top, right, bottom) != (0, 0, rgba.width, rgba.height),
    }
    return rgba.crop((left, top, right, bottom)), meta


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--threshold", type=int, default=246)
    parser.add_argument("--padding", type=int, default=10)
    parser.add_argument("--tolerance", type=int, default=18)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    for src in args.inputs:
        with Image.open(src) as image:
            original_size = image.size
            trimmed, meta = trim_background(
                image,
                threshold=args.threshold,
                padding=args.padding,
                tolerance=args.tolerance,
            )
        out = args.out_dir / f"{src.stem}_trimmed.png"
        trimmed.save(out)
        entries.append(
            {
                "source": str(src),
                "prepared": str(out),
                "operation": "trim_background",
                "original_size": list(original_size),
                "prepared_size": list(trimmed.size),
                "bbox": meta["bbox"],
                "bbox_removed": meta["removed"],
                "changed": meta["changed"],
                "scientific_content_changed": False,
            }
        )
        print(out)
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(
            json.dumps(
                {
                    "$schema": "academic-fallback-prepared-figures/v1",
                    "figures": entries,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
