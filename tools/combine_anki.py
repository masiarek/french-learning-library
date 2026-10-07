#!/usr/bin/env python3
"""Combine a chapter's Anki decks into one file that imports in one go.

    python3 tools/combine_anki.py 03_Szypowska       # write 03_Szypowska/anki/szypowska_all.txt
    python3 tools/combine_anki.py 03_Szypowska --check    # write nothing, fail if it is stale

Each lesson keeps its decks in <lesson>/anki/: the one generated from its
table by tools/anki_from_tables.py and the hand-written challenges. The combined file adds a deck column, so Anki still files every card
under its lesson's subdeck, and it merges each deck's file-level tags into
the card's own tag, so a card keeps both when imported from either file.
"""

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


def build(chapter: Path) -> str:
    sources = sorted(p for p in chapter.glob("*/anki/*.txt"))
    if not sources:
        sys.exit(f"{chapter}: no lesson decks found")
    parent = parse(sources[0])[0].rsplit("::", 1)[0]
    lines = [
        "#separator:tab",
        "#html:true",
        "#notetype:Basic",
        "#columns:Front\tBack\tTags\tDeck",
        "#tags column:3",
        "#deck column:4",
    ]
    for path in sources:
        deck, file_tags, cards = parse(path)
        for front, back, tag in cards:
            tags = " ".join(dict.fromkeys(file_tags + tag.split()))
            lines.append("\t".join([front, back, tags, deck]))
    return "\n".join(lines) + "\n", parent, len(sources)


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    chapter = ROOT / args[0]
    text, parent, n = build(chapter)
    name = chapter.name.split("_", 1)[1].lower() if "_" in chapter.name else chapter.name.lower()
    out = chapter / "anki" / f"{name}_all.txt"
    cards = sum(1 for l in text.splitlines() if not l.startswith("#"))
    if check:
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            sys.exit(f"{out.relative_to(ROOT)} is stale: run python3 tools/combine_anki.py {args[0]}")
        print(f"{out.relative_to(ROOT)}: up to date, {cards} cards from {n} decks.")
        return
    out.parent.mkdir(exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}: {cards} cards from {n} decks, subdecks under {parent}.")


if __name__ == "__main__":
    main()
