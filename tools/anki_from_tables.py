#!/usr/bin/env python3
"""Make each lesson's Anki deck from the table on its page.

    python3 tools/anki_from_tables.py 03_Szypowska            # write <lesson>/anki/<lesson>.txt for every lesson
    python3 tools/anki_from_tables.py 03_Szypowska --check    # write nothing; fail if any deck is stale (CI)

A lesson page here is one table: French | English, with the Polish below it |
IPA. Every row with a transcription gives two cards, the French on the front
and the meaning with the IPA on the back, then the meaning on the front and
the French with the IPA on the back. An exercise row gives one card instead:
a sentence with a blank, or the book's sentence with the instruction of its
section, on the front, and the answer on the back. Heading rows, in bold,
name the sections; the page's H1 names the deck. The deck is generated so
that it cannot drift from the page; the challenges beside it,
<lesson>/anki/<lesson>_challenges.txt, are written by hand and left alone.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLANK = "________"


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


def cards(rows) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    base = ""
    for french, meaning, ipa, section in rows:
        if not ipa:
            continue
        if french.startswith("→"):
            answer = french.lstrip("→ ").strip()
            front = f"{base} → {section}"
            if section.lower().startswith("answer"):
                words = re.sub(r"[.,!?]", "", answer).split()
                front += f" ({' '.join(words[:2])})"
            out.append((front, f"{answer}<br>{ipa}<br>{meaning}", "exercise"))
            continue
        base = french
        if BLANK in french:
            out.append((f"{french}<br>({section})", f"{ipa}<br>{meaning}", "exercise"))
            continue
        out.append((french, f"{meaning}<br>{ipa}", "fr-en"))
        out.append((meaning, f"{french}<br>{ipa}", "en-fr"))
    # A word the page repeats (in the word list, then in the notes, then in a
    # grammar table) gives one card, not three; a front that recurs with a
    # different back is numbered so that Anki keeps both.
    backs: dict[str, list[str]] = {}
    unique = []
    for front, back, tag in out:
        had = backs.setdefault(front, [])
        if back in had:
            continue
        had.append(back)
        n = len(had)
        unique.append((front if n == 1 else f"{front} ({n})", back, tag))
    return unique


def deck_text(chapter: Path, lesson: Path) -> str:
    title, rows = parse_page((lesson / "README.md").read_text(encoding="utf-8"))
    chapter_name = chapter.name.split("_", 1)[1].split("_")[0]
    lines = [
        "#separator:tab",
        "#html:true",
        "#notetype:Basic",
        f"#deck:French::{chapter_name}::{title}",
        f"#tags:french {chapter_name.lower()} {lesson.name.split('_')[0]}{lesson.name.split('_')[1]}",
        "#columns:Front\tBack\tTags",
        "#tags column:3",
    ]
    for front, back, tag in cards(rows):
        lines.append("\t".join([front, back, tag]))
    return "\n".join(lines) + "\n"


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    chapter = ROOT / args[0]
    lessons = sorted(p.parent for p in chapter.glob("*/README.md"))
    if not lessons:
        sys.exit(f"{chapter}: no lessons found")
    stale = []
    for lesson in lessons:
        text = deck_text(chapter, lesson)
        out = lesson / "anki" / f"{lesson.name}.txt"
        n = sum(1 for l in text.splitlines() if not l.startswith("#"))
        if check:
            if not out.exists() or out.read_text(encoding="utf-8") != text:
                stale.append(str(out.relative_to(ROOT)))
            else:
                print(f"{out.relative_to(ROOT)}: up to date, {n} cards.")
            continue
        out.parent.mkdir(exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}: {n} cards.")
    if stale:
        sys.exit("stale: " + ", ".join(stale) + f" — run python3 tools/anki_from_tables.py {args[0]}")


if __name__ == "__main__":
    main()
