"""Lesson 4 of Szypowska's textbook, read back by a program.

The page holds the French of the lesson as one table: French, English with
Polish below, IPA after Le Robert. The book gives its own transcription in
square brackets under every line of the reading and beside every word of
the list. This program types those brackets in, reletters them with the key
on the chapter page, and holds the result to the page's IPA, item by item;
it also checks that every symbol on the page is a French phoneme. Lesson 4
is where the book's notation shows its last symbols, sz for the ch of
chambre and üi for the ui of cuisine.

The French inventory is the one of the Sounds chapter's first lesson
(01_Sounds/ipa_english_vs_french), and the key is the chapter page's table;
both are copied here because every example in this library runs on its own.
"""

from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "README.md"


def nfd(s: str) -> str:
    return unicodedata.normalize("NFD", s)


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


FRENCH_CONSONANTS = set("p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ w j ɥ".split())
FRENCH_VOWELS = set("i e ɛ a ɑ ɔ o u y ø œ ə".split()) | set("ɑ̃ ɛ̃ ɔ̃ œ̃".split())
FRENCH = {nfd(s) for s in FRENCH_CONSONANTS | FRENCH_VOWELS}
NASALS = [nfd(s) for s in ("ɑ̃", "ɛ̃", "ɔ̃", "œ̃")]

STRESS, LENGTH, LIAISON = "ˈ", "ː", "‿"
# Punctuation and the editorial marks of the table, none of them a sound.
SKIP = set(" ,.!?:;·()[]…+–—-")

# The book's notation -> Le Robert's IPA: the key on the chapter page. It is
# applied left to right, longest match first, and never re-reads what it has
# written: "wua" is read before "ua" and "w", or the w that "ua" produces
# would turn into a v.
KEY = {
    nfd(k): nfd(v)
    for k, v in {
        "wua": "vwa", "üi": "ɥi", "ui": "wi", "ua": "wa", "sz": "ʃ", "ż": "ʒ",
        "ã": "ɑ̃", "õ": "ɔ̃", "ü": "y", "ń": "ɲ", "w": "v", "r": "ʁ", "g": "ɡ",
        ":": "",
    }.items()
}

# The book's own transcriptions, typed from its brackets, keyed by the French
# exactly as the table on the page has it.
BOOK = [
    ('Monsieur et Madame Lefèvre habitent un appartement rue du Bac.', 'məsjø e madam ləfɛ:wr abitœ̃napartəmã rü dü bak'),
    ('Nous entrons.', 'nuzãtrõ'),
    ('Nous visitons l’appartement de la famille Lefèvre.', 'nu wizitõ lapartəmã də la famij ləfɛ:wr'),
    ('Voici le cabinet de travail de Monsieur Lefèvre.', 'wuasi lə kabinɛ də trawaj də məsjø ləfɛ:wr'),
    ('Voilà la salle à manger avec le divan de la fille, et ici, la chambre des parents avec le lit du garçon.', 'wuala la sal a mãże awɛk lə diwã də la fij e isi la szã:br de parã awɛk lə li dü garsõ'),
    ('Madame Lefèvre montre aussi la cuisine et la salle de bain.', 'madam ləfɛ:wr mõ:tr osi la küizin e la sal də bɛ̃'),
    ('Ensuite nous sortons.', 'ãsüit nu sɔrtõ'),
    ('quatre', 'katr'),
    ('habiter', 'abite'),
    ('habitent', 'abit'),
    ('un appartement', 'œ̃napartəmã'),
    ('la rue', 'la rü'),
    ('le bac', 'lə bak'),
    ('entrer', 'ãtre'),
    ('nous entrons', 'nuzãtrõ'),
    ('visiter', 'wizite'),
    ('nous visitons', 'nuwizitõ'),
    ('la famille', 'la famij'),
    ('de la famille', 'də la famij'),
    ('le cabinet', 'lə kabinɛ'),
    ('le travail', 'lə trawaj'),
    ('le cabinet de travail', 'lə kabinɛ də trawaj'),
    ('la salle', 'la sal'),
    ('manger', 'mãże'),
    ('la salle à manger', 'la salamãże'),
    ('avec', 'awɛk'),
    ('le divan', 'lə diwã'),
    ('la fille', 'la fij'),
    ('ici', 'isi'),
    ('la chambre', 'la szã:br'),
    ('les parents', 'leparã'),
    ('des parents', 'deparã'),
    ('le lit', 'lə li'),
    ('le garçon', 'lə garsõ'),
    ('du garçon', 'dü garsõ'),
    ('montrer', 'mõtre'),
    ('montre', 'mõ:tr'),
    ('le bain', 'lə bɛ̃'),
    ('la cuisine', 'la küizin'),
    ('la salle de bain', 'la sal də bɛ̃'),
    ('ensuite', 'ãsüit'),
    ('nous sortons', 'nusɔrtõ'),
    ('ici, voici', 'isi wuasi'),
    ('cabinet, cuisine', 'kabinɛ küizin'),
    ('Bac, avec', 'bak awɛk'),
    ('la rue du Bac', 'la rüdübak'),
]

# Where the book and Le Robert are expected to part: (book, Le Robert).
EXPECTED = set()
EXPECTED_LABEL = "those expected, which here are none"


def table_rows(text: str) -> list[list[str]]:
    """Every body row of every Markdown table on the page, as its cells."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):
            continue
        if cells[0] == "French":
            continue
        rows.append(cells)
    return rows


def symbols(ipa: str) -> list[str]:
    """Split a transcription into inventory symbols, longest match first; an
    unknown character is kept on its own so that it shows up in the report."""
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


def convert(book: str) -> str:
    """The book's notation relettered into Le Robert's, by the key."""
    text = nfd(book)
    longest = max(len(k) for k in KEY)
    out: list[str] = []
    i = 0
    while i < len(text):
        for n in range(longest, 0, -1):
            piece = text[i : i + n]
            if piece in KEY:
                out.append(KEY[piece])
                i += n
                break
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def flat(ipa: str) -> str:
    """A transcription with everything that is not a sound removed, to compare."""
    return "".join(c for c in nfd(ipa) if c not in SKIP and c != LIAISON)


def first_difference(a: str, b: str) -> tuple[str, str]:
    """The first symbol at which two flat transcriptions part."""
    sa, sb = symbols(a), symbols(b)
    for x, y in zip(sa, sb):
        if x != y:
            return nfc(x), nfc(y)
    return (nfc(sa[len(sb)]) if len(sa) > len(sb) else "-", nfc(sb[len(sa)]) if len(sb) > len(sa) else "-")


def french_key(cell: str) -> str:
    return re.sub(r"^\*\*|\*\*$", "", cell).removeprefix("— ").strip()


def main() -> None:
    text = PAGE.read_text(encoding="utf-8")
    rows = [r for r in table_rows(text) if len(r) == 3]
    with_ipa = [(r[0], re.findall(r"/([^/]+)/", r[2])) for r in rows]
    with_ipa = [(f, ts) for f, ts in with_ipa if ts]
    every = [t for _, ts in with_ipa for t in ts]
    first_ipa: dict[str, str] = {}
    for f, ts in with_ipa:
        first_ipa.setdefault(french_key(f), ts[0])

    print("1. The table, read back from the page")
    print(f"   rows: {len(rows)}, with a transcription: {len(with_ipa)}")
    used: Counter[str] = Counter()
    for t in every:
        used.update(symbols(t))
    unknown = sorted(s for s in used if s not in FRENCH)
    print(f"   symbols: {sum(used.values())} in all, {len(used)} distinct")
    print(f"   not in Le Robert's French inventory: {' '.join(unknown) or '-'}")
    nas = "   ".join(f"{nfc(n)} {used[n]}" for n in NASALS)
    print(f"   nasal vowels: {nas}")
    joined: Counter[str] = Counter()
    for t in every:
        for m in re.finditer(r"\(?([a-zɡʁ])\)?‿", t):
            joined[m.group(1)] += 1
    print("   liaisons marked: " + (", ".join(f"{c}‿ {n}" for c, n in sorted(joined.items())) or "none"))
    print()

    print("2. The book's brackets, relettered by the key and held to the page's IPA")
    ok = 0
    missing: list[str] = []
    differences: list[tuple[str, str, str, str]] = []
    for french, book in BOOK:
        page = first_ipa.get(french)
        converted = convert(book)
        if page is None:
            missing.append(french)
        elif flat(converted) == flat(page):
            ok += 1
        else:
            differences.append((french, book, converted, page))
    print(f"   brackets typed from the book: {len(BOOK)}")
    print(f"   agree with the page exactly:  {ok}")
    print(f"   differ:                       {len(differences)}")
    print(f"   not found on the page:        {len(missing)}{(': ' + '; '.join(missing)) if missing else ''}")
    pairs: Counter[tuple[str, str]] = Counter()
    for french, book, converted, page in differences:
        b, r = first_difference(converted, page)
        pairs[(b, r)] += 1
        print(f"   - {french}")
        print(f"       book [{book}] -> /{nfc(converted)}/, page /{nfc(page)}/: book {b}, Le Robert {r}")
    print()

    print("3. Checks")
    print("   every symbol on the page is a French phoneme:     ", not unknown)
    print("   no stress mark and no length mark on the page:    ", all(STRESS not in t and LENGTH not in t for t in every))
    print("   every bracket of the book was found on the page:  ", not missing)
    print(f"   the differences are only {EXPECTED_LABEL}: ", set(pairs) <= EXPECTED)


if __name__ == "__main__":
    main()
