"""Lesson 1 of the teacher's worksheets, read back by a program.

The page holds the whole worksheet *La maison* as one table: French, English,
IPA. This program reads that table from the page itself and checks what no
eye checks across a hundred and sixty rows: that every symbol in the IPA
column is a phoneme of French in Le Robert's key, that no stress mark or
length mark crept in from an English habit, which nasal vowels occur and how
often, which consonants the liaison marks join, and how much of the worksheet
is built on its grammar point, *il y a*.

The French inventory is the one of the Sounds chapter's first lesson
(01_Sounds/ipa_english_vs_french), copied here because every example in this
library runs on its own.
"""

from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "README.md"


def nfd(s: str) -> str:
    return unicodedata.normalize("NFD", s)


FRENCH_CONSONANTS = set("p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ w j ɥ".split())
FRENCH_VOWELS = set("i e ɛ a ɑ ɔ o u y ø œ ə".split()) | set("ɑ̃ ɛ̃ ɔ̃ œ̃".split())
FRENCH = {nfd(s) for s in FRENCH_CONSONANTS | FRENCH_VOWELS}
NASALS = [nfd(s) for s in ("ɑ̃", "ɛ̃", "ɔ̃", "œ̃")]
ROUNDED = ["y", "ø", "œ"]
OTHERS = ["ʁ", "ɥ", "ɲ"]

STRESS, LENGTH, LIAISON = "ˈ", "ː", "‿"
# Punctuation and the editorial marks of the table, none of them a sound:
# square brackets round an answer that fills a blank, round brackets round an
# optional liaison consonant, dots for a blank left open, the separators and
# the plus signs of the list rows.
SKIP = set(" ,.!?:;·()[]…+–—-")


def table_rows(text: str) -> list[list[str]]:
    """Every body row of every Markdown table on the page, as its cells."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):  # the |---|---| line
            continue
        if cells[0] == "French":  # the header row
            continue
        rows.append(cells)
    return rows


def symbols(ipa: str) -> list[str]:
    """Split a transcription into inventory symbols, longest match first.

    An unknown character is kept on its own, so that it shows up in the report
    instead of vanishing.
    """
    text = nfd(ipa)
    longest = max(len(s) for s in FRENCH)
    out: list[str] = []
    i = 0
    while i < len(text):
        if text[i] in SKIP or text[i] == LIAISON:
            i += 1
            continue
        for n in range(longest, 0, -1):
            piece = text[i : i + n]
            if piece in FRENCH:
                out.append(piece)
                i += n
                break
        else:
            out.append(text[i])
            i += 1
    return out


def main() -> None:
    text = PAGE.read_text(encoding="utf-8")
    rows = [r for r in table_rows(text) if len(r) == 3]
    with_ipa = [(r[0], re.findall(r"/([^/]+)/", r[2])) for r in rows]
    with_ipa = [(f, ts) for f, ts in with_ipa if ts]
    every = [t for _, ts in with_ipa for t in ts]

    print("1. The table, read back from the page")
    print(f"   rows: {len(rows)}, with a transcription: {len(with_ipa)}")
    used: Counter[str] = Counter()
    for t in every:
        used.update(symbols(t))
    unknown = sorted(s for s in used if s not in FRENCH)
    print(f"   symbols: {sum(used.values())} in all, {len(used)} distinct")
    print(f"   not in Le Robert's French inventory: {' '.join(unknown) or '-'}")
    print()

    print("2. The sounds French has and English does not, as they occur here")
    for label, group in (("nasal vowels", NASALS), ("front rounded vowels", ROUNDED), ("ʁ, ɥ, ɲ", OTHERS)):
        parts = [f"{unicodedata.normalize('NFC', s)} {used[nfd(s)]}" for s in group]
        print(f"   {label:<22} {'   '.join(parts)}")
    print()

    print("3. Liaisons marked with ‿, by the consonant they add")
    joined: Counter[str] = Counter()
    for t in every:
        for m in re.finditer(r"\(?([a-zɡʁ])\)?‿", t):
            joined[m.group(1)] += 1
    for c, n in sorted(joined.items()):
        print(f"   {c}‿  {n}")
    optional = sum(t.count("(t)‿") for t in every)
    print(f"   of which optional, written (t)‿: {optional}")
    print()

    print("4. The worksheet's grammar point")
    body = [f for f, _ in with_ipa if not f.startswith("**")]
    ilya = [f for f in body if "il y a" in f.lower()]
    print(f"   rows that are not headings: {len(body)}; among them with 'il y a': {len(ilya)}")
    print()

    print("5. Checks")
    print("   every symbol is a French phoneme:           ", not unknown)
    print("   no stress mark and no length mark:          ", all(STRESS not in t and LENGTH not in t for t in every))
    print("   all four nasal vowels occur:                ", all(used[n] > 0 for n in NASALS))
    print("   /œ̃/ occurs (the Assimil dialogue had none):  ", used[NASALS[3]] > 0)
    print("   the liaisons add only z, n, t and ʁ:        ", set(joined) <= {"z", "n", "t", "ʁ"})


if __name__ == "__main__":
    main()
