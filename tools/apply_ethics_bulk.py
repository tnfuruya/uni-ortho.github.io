# -*- coding: utf-8 -*-
"""Bulk HTML updates for JOS homepage ethics alignment. Run from repo root."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_SNIPPET = (
    "札幌市西区、琴似にある矯正歯科クリニックです。最新設備を利用して成長期のお子様、成人矯正、顎変形症の治療、顎関節症の咬合治療などを行っております。"
)
NEW_SNIPPET = (
    "札幌市西区、琴似にある矯正歯科クリニックです。各種画像診断装置を利用して、成長期のお子様から成人の矯正、顎変形症の治療、顎関節症の咬合治療などに対応しております。"
)

ALT_OLD1 = 'alt="バナー｜見えない治療"'
ALT_NEW1 = 'alt="バナー｜舌側（リンガル）矯正について"'
ALT_OLD2 = 'alt="バナー｜見せて魅せる治療"'
ALT_NEW2 = 'alt="バナー｜ワイヤー矯正（装置の見え方）について"'

TWO_LEVEL_PREFIXES = (
    "infomation/ontona_etc/",
    "treatment/end/",
    "treatment/start/",
    "treatment/surgery/",
)


def strip_testimonial_banner_block(text: str) -> str:
    """Remove <p>...</sideBn07...感想...</p> blocks (one line each)."""
    lines = text.splitlines(keepends=True)
    out = []
    for line in lines:
        if "sideBn07.jpg" in line and "感想" in line:
            continue
        out.append(line)
    return "".join(out)


def fix_contact_two_level(rel: str, text: str) -> str:
    if not rel.replace("\\", "/").startswith(TWO_LEVEL_PREFIXES):
        return text
    return text.replace('href="../contact/index.html"', 'href="../../contact/index.html"')


def fix_contact_page(text: str) -> str:
    """contact/index.html self-links."""
    return text.replace('href="../contact/index.html"', 'href="./index.html"')


def process_file(path: Path) -> bool:
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    raw = path.read_text(encoding="utf-8")
    orig = raw

    if OLD_SNIPPET in raw:
        raw = raw.replace(OLD_SNIPPET, NEW_SNIPPET)
    raw = raw.replace("顎口腔機能診断医療機関", "顎口腔機能診断施設")
    raw = raw.replace(ALT_OLD1, ALT_NEW1)
    raw = raw.replace(ALT_OLD2, ALT_NEW2)
    raw = strip_testimonial_banner_block(raw)

    if rel == "contact/index.html":
        raw = fix_contact_page(raw)
    else:
        raw = fix_contact_two_level(rel, raw)

    if raw != orig:
        path.write_text(raw, encoding="utf-8")
        return True
    return False


def main():
    changed = []
    for p in sorted(ROOT.rglob("*.html")):
        if "tools" in p.parts:
            continue
        if process_file(p):
            changed.append(p.relative_to(ROOT))
    print(f"Updated {len(changed)} files")
    for c in changed:
        print(" ", c)


if __name__ == "__main__":
    main()
