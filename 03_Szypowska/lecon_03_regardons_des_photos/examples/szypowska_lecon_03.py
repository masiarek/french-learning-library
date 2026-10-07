"""Lesson 3 of Szypowska's textbook, read back by a program.

The page holds the French of the lesson as one table: French, English with
Polish below, IPA after Le Robert. The book gives its own transcription in
square brackets under every line of the reading and beside every word of
the list, in a notation made for Polish readers. This program types those
brackets in, reletters them with the key on the chapter page, and holds the
result to the page's IPA, item by item; it also checks that every symbol on
the page is a French phoneme. Where the two part, the output says which
symbol the book has and which Le Robert has.

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
    ('Madame Renoir, Marie et Jean regardent les photos et les cartes.', 'madam rənua:r mari e żã rəgard le fɔtɔ e le kart'),
    ('Voici la photo de Suzanne, l’amie de Marie.', 'wuasi la fɔtɔ də süzan lami də mari'),
    ('Et voilà la photo de Pierre, le camarade de Jean.', 'e wuala la fɔtɔ də pjɛ:r lə kamarad də żã'),
    ('Voici Paris, la capitale de la France. Regarde la Tour Eiffel !', 'wuasi pari la kapital də la frã:s rəgard la tu:r efɛl'),
    ('Et voilà Varsovie, la capitale de la Pologne. Regardez le Palais de la Culture et de la Science !', 'e wuala warsɔwi la kapital də la pɔlɔń rəgarde lə palɛ də la kültü:r e də la sjã:s'),
    ('A Varsovie on parle polonais.', 'a warsɔwi õ parl pɔlɔnɛ'),
    ('A Paris on parle français.', 'a pari õ parl frãsɛ'),
    ('trois', 'trua'),
    ('troisième', 'truazjɛm'),
    ('Suzanne', 'süzan'),
    ('l’amie (ż)', 'lami'),
    ('voilà', 'wuala'),
    ('Pierre', 'pjɛr'),
    ('le camarade', 'lə kamarad'),
    ('Paris', 'pari'),
    ('la capitale', 'la kapital'),
    ('la France', 'la frã:s'),
    ('regarde !', 'rəgard'),
    ('Varsovie', 'warsɔwi'),
    ('la Pologne', 'la pɔlɔń'),
    ('la tour', 'la tu:r'),
    ('le palais', 'lə palɛ'),
    ('la culture', 'la kültü:r'),
    ('la science', 'la sjã:s'),
    ('aussi', 'osi'),
    ('à Varsovie', 'a warsɔwi'),
    ('à Paris', 'a pari'),
    ('nous aimons', 'nuzɛmõ'),
    ('la Tour Eiffel', 'la turefɛl'),
]

# Where the book and Le Robert are expected to part: (book, Le Robert).
EXPECTED = {("ɔ", "o"), ("e", "ɛ")}
EXPECTED_LABEL = "the final o of photo and the first vowel of Eiffel"


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
