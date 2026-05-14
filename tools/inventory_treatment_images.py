# -*- coding: utf-8 -*-
"""
治療例（treatment）HTML が参照するローカル画像を一覧化します。

使い方:
  python tools/inventory_treatment_images.py
  python tools/inventory_treatment_images.py --cases-only
  python tools/inventory_treatment_images.py --cases-only --photos-only
  python tools/inventory_treatment_images.py --csv tools/treatment_image_refs.csv

--cases-only … src が ./common/img/ で始まる参照（各セクション配下の素材）。
--photos-only … 拡張子が .jpg / .jpeg / .png / .webp のみ（見出しGIFを除外）。
ファイル名を変えずに上書き差し替えすれば HTML の修正は不要です。
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TREATMENT = ROOT / "treatment"
# <img ... src="...">
SRC_RE = re.compile(
    r"<img\b[^>]*\bsrc\s*=\s*([\"'])([^\"']+)\1",
    re.IGNORECASE | re.DOTALL,
)


def norm_key(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(p).replace("\\", "/")


def main() -> None:
    ap = argparse.ArgumentParser(description="List image refs from treatment/*.html")
    ap.add_argument(
        "--cases-only",
        action="store_true",
        help="Only ./common/img/... (case photos under each treatment subfolder)",
    )
    ap.add_argument(
        "--photos-only",
        action="store_true",
        help="Only raster images (.jpg .jpeg .png .webp); excludes GIF headers",
    )
    ap.add_argument("--csv", type=Path, help="Write CSV (paths relative to repo root)")
    args = ap.parse_args()
    if args.photos_only and not args.cases_only:
        ap.error("--photos-only は --cases-only と併用してください（症例フォルダ内の写真のみ対象）。")

    # canonical_rel -> { "refs": [(html_rel, src)], "exists": bool }
    bucket: dict[str, dict] = {}

    for html in sorted(TREATMENT.rglob("*.html")):
        if "index_err" in html.name:
            continue
        text = html.read_text(encoding="utf-8", errors="replace")
        for m in SRC_RE.finditer(text):
            src = m.group(2).strip()
            if not src or src.startswith(("http://", "https://", "//", "mailto:")):
                continue
            if args.cases_only and not src.startswith("./common/img/"):
                continue
            if args.photos_only:
                low = src.lower()
                if not low.endswith((".jpg", ".jpeg", ".png", ".webp")):
                    continue
            resolved = (html.parent / src).resolve()
            try:
                rel = resolved.relative_to(ROOT)
            except ValueError:
                rel_key = f"(outside repo) {src}"
            else:
                rel_key = str(rel).replace("\\", "/")

            if rel_key not in bucket:
                bucket[rel_key] = {"refs": [], "path": resolved if not rel_key.startswith("(") else None}
            bucket[rel_key]["refs"].append((norm_key(html), src))

    rows: list[tuple[str, int, str, str]] = []
    for rel_key in sorted(bucket.keys()):
        refs = bucket[rel_key]["refs"]
        n = len(refs)
        pages = sorted({r[0] for r in refs})
        path = bucket[rel_key]["path"]
        exists = path.is_file() if path else False
        sample_src = refs[0][1]
        rows.append((rel_key, n, "yes" if exists else "NO", sample_src))
        print(f"{rel_key}\n  refs={n} exists={exists} sample={sample_src}\n  pages: {', '.join(pages[:5])}" + (" ..." if len(pages) > 5 else ""))

    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["asset_path", "ref_count", "file_exists", "example_src_in_html"])
            for rel_key, n, ex, sample in rows:
                w.writerow([rel_key, n, ex, sample])
        print(f"\nWrote {args.csv}")


if __name__ == "__main__":
    main()
