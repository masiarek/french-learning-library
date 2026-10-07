#!/usr/bin/env python3
"""Make each lesson's Anki decks from the table on its page, one per direction.

    python3 tools/anki_from_tables.py 03_Szypowska            # write <lesson>/anki/<lesson>_fr_pl.txt and _pl_fr.txt
    python3 tools/anki_from_tables.py 03_Szypowska --check    # write nothing; fail if any deck is stale (CI)

A lesson page here is one table: French | English, with the Polish below it |
IPA. Every row with a transcription gives one card in each direction. In the
chapter of the Polish textbook the directions are FR-PL (the French with its
IPA on the front, the Polish and the English on the back) and PL-FR (the book's Polish
on the front, the French with its IPA and the English on the back); in the
teacher's chapter, which has no Polish, FR-EN and EN-FR. An exercise row
gives one card, in the French-front deck: a sentence with a blank, or the
book's sentence with the instruction of its section, on the front, and the
answer on the back. Heading rows, in bold, name the sections; the page's H1
names the subdeck. The decks are generated so that they cannot drift from
the page; the challenges beside them, <lesson>/anki/<lesson>_challenges.txt,
are written by hand and left alone.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLANK = "________"

# chapter folder -> (name in the deck, French-front direction, to-French direction, has Polish)
CHAPTERS = {
    "02_Yosser_teacher": ("Yosser", "FR-EN", "EN-FR", False),
    "03_Szypowska": ("Szypowska", "FR-PL", "PL-FR", True),
}


def clean(cell: str) -> str:
    """A table cell as card text: no Markdown emphasis, straight quotes made typographic."""
    s = cell.replace("**", "").replace("*", "").strip()
    s = re.sub(r'"([^"]*)"', "“\\1”", s).replace('"', "”")
    return re.sub(r"\s+", " ", s)


def parse_page(text: str):
    """The H1, and every table row as (french, meaning, ipa, section)."""
    title = next(l[2:].strip() for l in text.splitlines() if l.startswith("# "))
    rows, section = [], ""
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0] == "French" or all(set(c) <= set("-: ") for c in cells):
            continue
        if cells[0].startswith("**"):
            section = re.sub(r"^\d+\.\s*", "", clean(cells[0]))
            continue
        rows.append((clean(cells[0]), clean(cells[1]), clean(cells[2]), section))
    return title, rows


def dedupe(cards):
    """A word the page repeats gives one card; a front that recurs with a
    different back is numbered so that Anki keeps both."""
    backs: dict[str, list[str]] = {}
    out = []
    for front, back, tag in cards:
        had = backs.setdefault(front, [])
        if back in had:
            continue
        had.append(back)
        n = len(had)
        out.append((front if n == 1 else f"{front} ({n})", back, tag))
    return out


def cards(rows, polish: bool):
    """Two lists: the French-front cards (with the exercises) and the to-French cards."""
    fr, to_fr = [], []
    base = ""
    for french, meaning, ipa, section in rows:
        if not ipa:
            continue
        english, pl = (meaning.split("<br>", 1) + [""])[:2] if "<br>" in meaning else (meaning, "")
        if french.startswith("→"):
            answer = french.lstrip("→ ").strip()
            front = f"{base} → {section}"
            if section.lower().startswith("answer"):
                words = re.sub(r"[.,!?]", "", answer).split()
                front += f" ({' '.join(words[:2])})"
            fr.append((front, f"{answer}<br>{ipa}<br>{meaning}", "exercise"))
            continue
        base = french
        if BLANK in french:
            fr.append((f"{french}<br>({section})", f"{ipa}<br>{meaning}", "exercise"))
            continue
        # French-front cards show the IPA under the French, so the card is read
        # and pronounced before it is turned; the meaning is the answer.
        if polish and pl:
            fr.append((f"{french}<br>{ipa}", f"{pl}<br>{english}", "fr-pl"))
            to_fr.append((pl, f"{french}<br>{ipa}<br>{english}", "pl-fr"))
        else:
            fr.append((f"{french}<br>{ipa}", english, "fr-en"))
            to_fr.append((english, f"{french}<br>{ipa}", "en-fr"))
    return dedupe(fr), dedupe(to_fr)


def deck_text(name: str, direction: str, title: str, lesson_tag: str, items) -> str:
    lines = [
        "#separator:tab",
        "#html:true",
        "#notetype:Basic",
        f"#deck:French::{name} ({direction})::{title}",
        f"#tags:french {name.lower()} {lesson_tag} {direction.lower()}",
        "#columns:Front\tBack\tTags",
        "#tags column:3",
    ]
    for front, back, tag in items:
        lines.append("\t".join([front, back, tag]))
    return "\n".join(lines) + "\n"


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if len(args) != 1 or args[0] not in CHAPTERS:
        sys.exit(__doc__ + "\nKnown chapters: " + ", ".join(CHAPTERS))
    chapter = ROOT / args[0]
    name, d_fr, d_to, polish = CHAPTERS[args[0]]
    lessons = sorted(p.parent for p in chapter.glob("*/README.md"))
    if not lessons:
        sys.exit(f"{chapter}: no lessons found")
    stale = []
    for lesson in lessons:
        title, rows = parse_page((lesson / "README.md").read_text(encoding="utf-8"))
        parts = lesson.name.split("_")
        lesson_tag = parts[0] + parts[1]
        fr, to_fr = cards(rows, polish)
        for direction, items in ((d_fr, fr), (d_to, to_fr)):
            text = deck_text(name, direction, title, lesson_tag, items)
            out = lesson / "anki" / f"{lesson.name}_{direction.lower().replace('-', '_')}.txt"
            if check:
                if not out.exists() or out.read_text(encoding="utf-8") != text:
                    stale.append(str(out.relative_to(ROOT)))
                else:
                    print(f"{out.relative_to(ROOT)}: up to date, {len(items)} cards.")
                continue
            out.parent.mkdir(exist_ok=True)
            out.write_text(text, encoding="utf-8")
            print(f"wrote {out.relative_to(ROOT)}: {len(items)} cards.")
    if stale:
        sys.exit("stale: " + ", ".join(stale) + f" — run python3 tools/anki_from_tables.py {args[0]}")


if __name__ == "__main__":
    main()
