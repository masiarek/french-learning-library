#!/usr/bin/env python3
"""Check every transcription in the source chapters' tables.

    python3 tools/check_ipa.py        # fail if any IPA cell holds a symbol that is not a French phoneme

The lesson pages of 02_Yosser_teacher and 03_Szypowska are tables of French,
English (with Polish below) and IPA, written by hand. This tool reads every
IPA cell on those pages, splits it into symbols of Le Robert's French
inventory, longest match first, and fails on anything else: a stray Latin
letter, an English symbol, a stress or length mark. The inventory is the one
the Sounds chapter holds (01_Sounds/ipa_english_vs_french).
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ("02_Yosser_teacher", "03_Szypowska")


def nfd(s: str) -> str:
    return unicodedata.normalize("NFD", s)


FRENCH = {nfd(s) for s in "p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ w j ɥ i e ɛ a ɑ ɔ o u y ø œ ə ɑ̃ ɛ̃ ɔ̃ œ̃".split()}
LONGEST = max(len(s) for s in FRENCH)
# Punctuation and the editorial marks of the tables, none of them a sound:
# square brackets round an answer that fills a blank, round brackets round an
# optional liaison consonant, dots for a blank left open, list separators.
SKIP = set(" ,.!?:;·()[]…+–—-‿")


def symbols(ipa: str) -> list[str]:
    text = nfd(ipa)
    out, i = [], 0
    while i < len(text):
        if text[i] in SKIP:
            i += 1
            continue
        for n in range(LONGEST, 0, -1):
            if text[i : i + n] in FRENCH:
                out.append(text[i : i + n])
                i += n
                break
        else:
            out.append(text[i])
            i += 1
    return out


def main() -> int:
    bad = 0
    pages = sorted(p for c in CHAPTERS for p in (ROOT / c).glob("*/README.md"))
    for page in pages:
        cells = total = 0
        for line in page.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| ") or line.startswith("| French"):
                continue
            parts = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(parts) != 3:
                continue
            for ipa in re.findall(r"/([^/]+)/", parts[2]):
                cells += 1
                syms = symbols(ipa)
                total += len(syms)
                unknown = sorted({s for s in syms if s not in FRENCH})
                if unknown:
                    bad += 1
                    print(f"{page.relative_to(ROOT)}: /{ipa}/ has {' '.join(unknown)}")
        print(f"{page.relative_to(ROOT)}: {cells} transcriptions, {total} symbols, all French" if not bad else "")
    if bad:
        print(f"\n{bad} transcription(s) hold a symbol that is not a French phoneme.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
