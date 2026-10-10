#!/usr/bin/env python3
"""Homophones: lit, lie, lis, and the letters French writes but does not say.

Le lit (the bed), il lit (he reads), la lie (the dregs of the wine) and il lie
(he ties) come from four different roots, are spelled five ways, and are all
said /li/. What keeps them apart on the page is a final -t, -s, -e, -es or
-ent, and those are exactly the letters French does not pronounce. This
program holds the forms with their transcriptions and checks four things:

1. grouped by sound, the forms of the four roots give one group of seven
   forms and five spellings under /li/, and the near misses (lis the lily,
   ils lisent, lier, lu) fall outside it because a letter of theirs is said;
2. every spelling in the /li/ group is "li" plus one of the silent endings of
   the French verb and the French plural, and nothing else;
3. in the present tense of lier four of the six written forms sound alike,
   in lire three, in parler four, in finir three, in être and avoir two: the
   written ending carries the person and the sound does not, which is why
   the subject pronoun cannot be left out as it can in Latin or Polish;
4. the word before a /li/ settles some readings and not others: the article
   picks the noun (le lit, la lie), but il, je and tu each leave two verbs
   open, and only ils tells lire from lier, because ils lisent says its s.

A last section lists more sets of the same kind, read from the open ipa-dict
word list, and checks that every transcription on the page uses only Le
Robert's symbols.
"""

from __future__ import annotations

import unicodedata
from collections import defaultdict


def nfd(s: str) -> str:
    return unicodedata.normalize("NFD", s)


# Le Robert's inventory, as 01_Sounds/ipa_english_vs_french holds it.
FRENCH = {nfd(s) for s in "p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ w j ɥ i e ɛ a ɑ ɔ o u y ø œ ə ɑ̃ ɛ̃ ɔ̃ œ̃".split()}
LONGEST = max(len(s) for s in FRENCH)

# The endings French writes and does not say: the person endings of the verb
# (-e, -es, -ent; -s, -s, -t) and the plural -s of the noun.
SILENT_ENDINGS = {"", "e", "es", "ent", "s", "t"}

# The forms of the four roots that meet at /li/, and the near misses around
# them. Each row: spelling, IPA, what it is, the root, and the words that can
# stand before it (an article for a noun, a subject pronoun for a verb form).
FORMS = [
    ("lit", "li", "bed", "le lit, the bed", "lectus", ["le", "un"]),
    ("lit", "li", "lire", "il lit, he reads (lire)", "legere", ["il"]),
    ("lis", "li", "lire", "je lis, tu lis, I read, you read (lire)", "legere", ["je", "tu"]),
    ("lie", "li", "dregs", "la lie, the dregs", "lia (Gaulish)", ["la", "une"]),
    ("lie", "li", "lier", "je lie, il lie, I tie, he ties (lier)", "ligare", ["je", "il"]),
    ("lies", "li", "lier", "tu lies, you tie (lier)", "ligare", ["tu"]),
    ("lient", "li", "lier", "ils lient, they tie (lier)", "ligare", ["ils"]),
    ("lisent", "liz", "lire", "ils lisent, they read (lire)", "legere", ["ils"]),
    ("lis", "lis", "lily", "le lis, the lily (also lys)", "lilium", ["le", "un"]),
    ("lier", "lje", "to tie", "to tie, the infinitive", "ligare", []),
    ("lié", "lje", "tied", "tied, the participle", "ligare", []),
    ("lu", "ly", "read", "read, the participle (lire)", "legere", []),
]

# The present tense of six verbs, je tu il nous vous ils, spelling and IPA.
PARADIGMS = {
    "lire": [("lis", "li"), ("lis", "li"), ("lit", "li"), ("lisons", "lizɔ̃"), ("lisez", "lize"), ("lisent", "liz")],
    "lier": [("lie", "li"), ("lies", "li"), ("lie", "li"), ("lions", "ljɔ̃"), ("liez", "lje"), ("lient", "li")],
    "parler": [("parle", "paʁl"), ("parles", "paʁl"), ("parle", "paʁl"), ("parlons", "paʁlɔ̃"), ("parlez", "paʁle"), ("parlent", "paʁl")],
    "finir": [("finis", "fini"), ("finis", "fini"), ("finit", "fini"), ("finissons", "finisɔ̃"), ("finissez", "finise"), ("finissent", "finis")],
    "être": [("suis", "sɥi"), ("es", "ɛ"), ("est", "ɛ"), ("sommes", "sɔm"), ("êtes", "ɛt"), ("sont", "sɔ̃")],
    "avoir": [("ai", "e"), ("as", "a"), ("a", "a"), ("avons", "avɔ̃"), ("avez", "ave"), ("ont", "ɔ̃")],
}
PERSONS = ["je", "tu", "il", "nous", "vous", "ils"]

# More sets of the same kind: one sound, several spellings. The transcriptions
# are those of the open ipa-dict word list (fr_FR), which agree with Le
# Robert's key for every word here.
SETS = [
    ("vɛʁ", ["ver", "vers", "vert", "verre", "vair"]),
    ("sɛ̃", ["sain", "saint", "sein", "ceint", "seing"]),
    ("sɑ̃", ["cent", "sang", "sans", "sent", "s'en"]),
    ("pɛʁ", ["père", "pair", "paire", "perd", "pers"]),
    ("ʃɛʁ", ["cher", "chère", "chair", "chaire"]),
    ("vwa", ["voie", "voix", "vois", "voit"]),
    ("vɛ̃", ["vin", "vingt", "vain", "vint"]),
    ("mɛ", ["mais", "mai", "met", "mets"]),
    ("tɑ̃", ["tant", "temps", "tend", "taon"]),
    ("so", ["sot", "seau", "sceau", "saut"]),
    ("kɑ̃", ["quand", "quant", "camp", "qu'en"]),
    ("o", ["au", "aux", "eau", "eaux", "haut"]),
    ("ami", ["ami", "amie", "amis", "amies"]),
    ("ly", ["lu", "lue", "lus", "lues", "lut"]),
    ("fwa", ["foi", "foie", "fois"]),
    ("pɛ̃", ["pain", "pin", "peint"]),
    ("pø", ["peu", "peut", "peux"]),
    ("kɔ̃t", ["conte", "compte", "comte"]),
    ("mɛʁ", ["mère", "mer", "maire"]),
    ("ku", ["cou", "coup", "coût"]),
]


def symbols(ipa: str) -> list[str]:
    """Split a transcription into inventory symbols, longest match first; a
    character outside the inventory comes out on its own, so the check sees it."""
    text = nfd(ipa)
    out: list[str] = []
    i = 0
    while i < len(text):
        for n in range(LONGEST, 0, -1):
            if text[i : i + n] in FRENCH:
                out.append(text[i : i + n])
                i += n
                break
        else:
            out.append(text[i])
            i += 1
    return out


def unknown(ipa: str) -> set[str]:
    return {s for s in symbols(ipa) if s not in FRENCH}


def plural(n: int, noun: str) -> str:
    return f"{n} {noun}" if n == 1 else f"{n} {noun}s"


def who(person: str, spelling: str) -> str:
    """The pronoun and the form as written: je lis, but j'ai."""
    if person == "je" and spelling[0] in "aeiouéê":
        return f"j'{spelling}"
    return f"{person} {spelling}"


def main() -> None:
    checks: dict[str, bool] = {}

    # ------------------------------------------------------------------ 1
    print("1. The forms of the four roots, grouped by sound")
    by_sound: dict[str, list] = defaultdict(list)
    for spelling, ipa, _, what, root, _ in FORMS:
        by_sound[ipa].append((spelling, what, root))
    for ipa in sorted(by_sound, key=lambda s: (-len(by_sound[s]), s)):
        rows = by_sound[ipa]
        spellings = sorted({r[0] for r in rows}, key=lambda s: (len(s), s))
        roots = sorted({r[2] for r in rows})
        print(f"   /{ipa}/  {plural(len(rows), 'form')}, {plural(len(spellings), 'spelling')}, {plural(len(roots), 'root')}")
        for spelling, what, root in rows:
            print(f"      {spelling:<7} {what:<45} {root}")
    li = by_sound["li"]
    li_spellings = sorted({r[0] for r in li}, key=lambda s: (len(s), s))
    li_roots = sorted({r[2] for r in li})
    print(f"   under /li/: {len(li)} forms, {len(li_spellings)} spellings ({', '.join(li_spellings)}), {len(li_roots)} roots")
    checks["seven forms, five spellings, four roots say /li/"] = (len(li), len(li_spellings), len(li_roots)) == (7, 5, 4)

    # ------------------------------------------------------------------ 2
    print()
    print("2. What the spellings of /li/ add to the sound: a silent ending, and nothing else")
    all_silent = True
    for spelling in li_spellings:
        ending = spelling[2:]
        ok = spelling.startswith("li") and ending in SILENT_ENDINGS
        all_silent &= ok
        shown = f"-{ending}" if ending else "nothing"
        print(f"   {spelling:<7} li + {shown:<8} {'silent' if ok else 'SAID'}")
    print("   the near misses, out of the group because a letter of theirs is said:")
    for spelling, ipa, _, what, _, _ in FORMS:
        if ipa != "li":
            print(f"   {spelling:<7} /{ipa}/".ljust(20) + f"{what}")
    checks["every /li/ spelling is li plus a silent ending"] = all_silent
    sounds_of_lis = sorted({ipa for spelling, ipa, *_ in FORMS if spelling == "lis"})
    print(f"   one spelling, two sounds: lis is /{sounds_of_lis[0]}/ (I read) and /{sounds_of_lis[1]}/ (the lily)")
    checks["lis is /li/ as a verb and /lis/ as the lily"] = sounds_of_lis == ["li", "lis"]

    # ------------------------------------------------------------------ 3
    print()
    print("3. The present tense: six written forms, how many sounds?")
    alike: dict[str, int] = {}
    for verb, forms in PARADIGMS.items():
        sounds: dict[str, list[str]] = defaultdict(list)
        for person, (spelling, ipa) in zip(PERSONS, forms):
            sounds[ipa].append(who(person, spelling))
        biggest = max(sounds.values(), key=len)
        alike[verb] = len(biggest)
        groups = "; ".join(f"/{ipa}/ {', '.join(who)}" for ipa, who in sounds.items())
        print(f"   {verb:<7} {len(forms)} spellings, {len(sounds)} sounds: {groups}")
        print(f"   {'':<7} the commonest sound covers {len(biggest)} of the 6 persons")
    checks["lier 4, lire 3, parler 4, finir 3, être 2, avoir 2 forms alike"] = (
        [alike[v] for v in ("lier", "lire", "parler", "finir", "être", "avoir")] == [4, 3, 4, 3, 2, 2]
    )

    # ------------------------------------------------------------------ 4
    print()
    print("4. What the word before a /li/ settles")
    two_open = []
    for before in ["le", "la", "je", "tu", "il", "ils"]:
        here = [(s, ipa, gloss) for s, ipa, gloss, _, _, b in FORMS if before in b]
        li_here = [h for h in here if h[1] == "li"]
        verdict = "one reading" if len(li_here) == 1 else f"{len(li_here)} readings of /li/"
        if len(li_here) > 1:
            two_open.append(before)
        shown = "; ".join(f"{who(before, s)} /{ipa}/ {gloss}" for s, ipa, gloss in here)
        print(f"   {before:<4} + /li/ : {verdict:<20} {shown}")
    print(f"   left open by the sound: {', '.join(two_open)}; settled: the rest")
    checks["the article settles the noun, il je tu stay open"] = two_open == ["je", "tu", "il"]
    ils = {s: ipa for s, ipa, _, _, _, b in FORMS if "ils" in b}
    checks["ils lisent and ils lient differ in sound"] = ils["lisent"] != ils["lient"]

    # ------------------------------------------------------------------ 5
    print()
    print("5. More sets of the same kind, from ipa-dict")
    total = 0
    for ipa, spellings in SETS:
        total += len(spellings)
        print(f"   /{ipa}/".ljust(10) + f"{len(spellings)} spellings: {', '.join(spellings)}")
    print(f"   {len(SETS)} sounds, {total} spellings")

    # ------------------------------------------------------------------ 6
    print()
    print("6. Checks")
    bad: set[str] = set()
    for _, ipa, *_ in FORMS:
        bad |= unknown(ipa)
    for forms in PARADIGMS.values():
        for _, ipa in forms:
            bad |= unknown(ipa)
    for ipa, _ in SETS:
        bad |= unknown(ipa)
    checks["every transcription uses Le Robert's symbols"] = not bad
    for label, ok in checks.items():
        print(f"   {label + ':':<58} {ok}")


if __name__ == "__main__":
    main()
