"""Lesson 5 of Szypowska's textbook, read back by a program.

The page holds the French of the lesson as one table: French, English with
Polish below, IPA after Le Robert. The book gives its own transcription in
square brackets under every line of the dialogue and beside every word of
the list and the grammar tables. This program types those brackets in,
reletters them with the key on the chapter page, and holds the result to the
page's IPA, item by item; it also checks that every symbol on the page is a
French phoneme. Two brackets part from the page: the dialogue prints [że]
for the je of je n'ai pas, where /ʒə/ is expected and where the word list
itself has [żənepa]; and interrogative has [o] where Le Robert has /ɔ/.

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
    ('J’ai un stylo. Est-ce que j’ai un stylo ?', 'że œ̃ stilo ɛskə że œ̃ stilo'),
    ('Oui, vous avez un stylo.', 'ui wuzawe œ̃ stilo'),
    ('Avez-vous un carnet ?', 'awewu œ̃ karnɛ'),
    ('Oui, j’ai un carnet.', 'ui że œ̃ karnɛ'),
    ('Pierre, as-tu un canif ?', 'pjɛ:r atü œ̃ kanif'),
    ('Non, je n’ai pas de canif.', 'nõ że ne pa də kanif'),
    ('Pierre et Annette, avez-vous des crayons ?', 'pjɛ:r e anɛt awewu de krɛjõ'),
    ('Oui, nous avons des crayons, mais nous n’avons pas de cahiers.', 'ui nuzawõ de krɛjõ mɛ nu nawõ pa də kaje'),
    ('Est-ce que Pierre a une plume ?', 'ɛskə pjɛ:r a ün plüm'),
    ('A-t-il une plume ?', 'atil ün plüm'),
    ('Oui, il a une plume.', 'ui il a ün plüm'),
    ('Est-ce qu’Annette a un cahier ?', 'ɛskanɛt a œ̃ kaje'),
    ('A-t-elle un cahier ?', 'atɛl œ̃ kaje'),
    ('Oui, elle a un cahier.', 'ui ɛl a œ̃ kaje'),
    ('Est-ce que Pierre et Annette ont des crayons ?', 'ɛskə pjɛ:r e anɛt õ de krɛjõ'),
    ('Ont-ils des crayons ?', 'õtil de krɛjõ'),
    ('Oui, ils ont des crayons.', 'ui ilzõ de krɛjõ'),
    ('Est-ce qu’ils ont des cahiers ?', 'ɛskilzõ de kaje'),
    ('Non, ils n’ont pas de cahiers.', 'nõ il nõ pa də kaje'),
    ('cinq', 'sɛ̃k'),
    ('cinquième', 'sɛ̃kjɛm'),
    ('j’ai', 'że'),
    ('un stylo', 'œ̃ stilo'),
    ('vous avez', 'wuzawe'),
    ('avez-vous ?', 'awewu'),
    ('un carnet', 'œ̃ karnɛ'),
    ('as-tu ?', 'atü'),
    ('un canif', 'œ̃ kanif'),
    ('je n’ai pas', 'żənepa'),
    ('Annette', 'anɛt'),
    ('un crayon', 'œ̃ krɛjõ'),
    ('nous avons', 'nuzawõ'),
    ('mais', 'mɛ'),
    ('nous n’avons pas', 'nunawõpa'),
    ('il a', 'il a'),
    ('une plume', 'ünplüm'),
    ('un cahier', 'œ̃ kaje'),
    ('(ils, elles) ont', 'ilzõ ɛlzõ'),
    ('je n’ai pas de canif', 'żə ne pa dəkanif'),
    ('nous n’avons pas de cahiers', 'nu nawõ pa də kaje'),
    ('l’encre (ż)', 'lãkr'),
    ('un encrier', 'œ̃nãkrije'),
    ('une gomme', 'ün gɔm'),
    ('un papier buvard', 'œ̃ papje büwa:r'),
    ('une règle', 'ün rɛgl'),
    ('un stylo à bille', 'œ̃ stilo a bij'),
    ('ont-ils', 'õtil'),
    ('cahier', 'kaje'),
    ('avoir', 'awua:r'),
    ('Forme affirmative', 'fɔrm afirmati:w'),
    ('tu as', 'tü a'),
    ('elle a', 'ɛl a'),
    ('on a', 'õ na'),
    ('ils ont', 'ilzõ'),
    ('elles ont', 'ɛlzõ'),
    ('Forme négative', 'fɔrm negati:w'),
    ('tu n’as pas', 'tünapa'),
    ('il n’a pas', 'ilnapa'),
    ('elle n’a pas', 'ɛlnapa'),
    ('on n’a pas', 'õnapa'),
    ('vous n’avez pas', 'wunawepa'),
    ('ils n’ont pas', 'ilnõpa'),
    ('elles n’ont pas', 'ɛlnõpa'),
    ('Forme interrogative', 'fɔrmɛ̃terogati:w'),
    ('est-ce que j’ai ?', 'ɛskəże'),
    ('a-t-il ?', 'atil'),
    ('a-t-elle ?', 'atɛl'),
    ('a-t-on ?', 'atõ'),
]

# Where the book and Le Robert are expected to part: (book, Le Robert).
EXPECTED = {("e", "ə"), ("o", "ɔ")}
EXPECTED_LABEL = "the e the book prints for je in one line, and the o of interrogative"


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
