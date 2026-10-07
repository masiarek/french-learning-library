#!/usr/bin/env python3
"""Combine a chapter's Anki decks into one file per direction.

    python3 tools/combine_anki.py 03_Szypowska            # write 03_Szypowska/anki/szypowska_fr_pl.txt and szypowska_pl_fr.txt
    python3 tools/combine_anki.py 03_Szypowska --check    # write nothing, fail if either is stale

Each lesson keeps its decks in <lesson>/anki/: the two generated from its
table by tools/anki_from_tables.py, one per direction, and the hand-written
challenges. Every deck names its set in its #deck header, "French::Szypowska
(PL-FR)::…", and this tool gathers the decks of a set into one file, named
after the set, so that a set imports in one go and files its cards under a
subdeck per lesson. Each deck's file-level tags are merged into its cards'
own tag, so a card keeps both when imported from either file. The two
chapters never share a file: the owner asked for that.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse(path: Path):
    deck, tags, cards = None, "", []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#deck:"):
            deck = line[len("#deck:"):]
        elif line.startswith("#tags:"):
            tags = line[len("#tags:"):]
        elif line.startswith("#") or not line.strip():
            continue
        else:
            front, back, tag = line.split("\t")
            cards.append((front, back, tag))
    if deck is None:
        sys.exit(f"{path}: no #deck: header")
    return deck, tags.split(), cards


def build(chapter: Path) -> dict[str, str]:
    """Set name -> the combined file's text."""
    sources = sorted(p for p in chapter.glob("*/anki/*.txt"))
    if not sources:
        sys.exit(f"{chapter}: no lesson decks found")
    sets: dict[str, list[str]] = {}
    for path in sources:
        deck, file_tags, cards = parse(path)
        set_name = deck.split("::")[1]
        lines = sets.setdefault(set_name, [])
        for front, back, tag in cards:
            tags = " ".join(dict.fromkeys(file_tags + tag.split()))
            lines.append("\t".join([front, back, tags, deck]))
    header = [
        "#separator:tab",
        "#html:true",
        "#notetype:Basic",
        "#columns:Front\tBack\tTags\tDeck",
        "#tags column:3",
        "#deck column:4",
    ]
    return {name: "\n".join(header + lines) + "\n" for name, lines in sets.items()}


def slug(set_name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", set_name.lower()).strip("_")


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    chapter = ROOT / args[0]
    stale = []
    for set_name, text in sorted(build(chapter).items()):
        out = chapter / "anki" / f"{slug(set_name)}.txt"
        cards = sum(1 for l in text.splitlines() if not l.startswith("#"))
        if check:
            if not out.exists() or out.read_text(encoding="utf-8") != text:
                stale.append(str(out.relative_to(ROOT)))
            else:
                print(f"{out.relative_to(ROOT)}: up to date, {cards} cards.")
            continue
        out.parent.mkdir(exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}: {cards} cards, the set {set_name}.")
    if stale:
        sys.exit("stale: " + ", ".join(stale) + f" — run python3 tools/combine_anki.py {args[0]}")


if __name__ == "__main__":
    main()
