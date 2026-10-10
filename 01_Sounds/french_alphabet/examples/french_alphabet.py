#!/usr/bin/env python3
"""The French alphabet: the 26 letter names, read in the IPA.

A letter name is a French word with a pronunciation of its own, and the 26 of
them obey the sound rules of French like any other word. This program holds the
names as Le Robert writes them and checks four things:

1. every symbol in the names is a French phoneme, and the alphabet alone drills
   several of the sounds that English does not have;
2. the e of every name is the closed /e/ when it ends the name and the open /ɛ/
   when a consonant follows it (the loi de position), with no exception;
3. the shape of a consonant's name, vowel after (bé) or vowel before (effe),
   follows the class the letter had in Latin, stop or continuant, and not the
   sound the letter has in French, which is why cé and gé keep a stop's shape
   while sounding /s/ and /ʒ/;
4. every name but one contains a sound its letter spells; the one is h, which
   spells no sound at all.
"""

from __future__ import annotations

import unicodedata


def nfd(s: str) -> str:
    return unicodedata.normalize("NFD", s)


# Le Robert's inventory, as 01_Sounds/ipa_english_vs_french holds it.
CONSONANTS = set("p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ w j ɥ".split())
VOWELS = {nfd(v) for v in "i e ɛ a ɑ ɔ o u y ø œ ə ɑ̃ ɛ̃ ɔ̃ œ̃".split()}
FRENCH = CONSONANTS | VOWELS
LONGEST = max(len(s) for s in FRENCH)

# The 15 symbols French has and Oxford's English key lacks: the first lesson's
# output, "French only".
FRENCH_ONLY = {nfd(s) for s in "a o y ø œ œ̃ ɑ ɑ̃ ɔ ɔ̃ ɛ ɛ̃ ɥ ɲ ʁ".split()}

# The stops of French; every other consonant is a continuant (fricative,
# nasal, liquid or glide), a sound that can be held.
STOPS = set("p b t d k ɡ".split())

# The consonant letters Latin had, by the class of their Latin sound. The
# letters j, v and w were added later, h lost its sound, and x, y and z were
# named otherwise, so the rule is stated for these fourteen.
LATIN_STOPS = set("b c d g k p q t")
LATIN_CONTINUANTS = set("f l m n r s")

# Letter, its name as spelled, the name in Le Robert's IPA, and the sounds the
# letter spells in French words (so that the name can be checked for one).
ALPHABET = [
    ("a", "a", "a", ["a"]),
    ("b", "bé", "be", ["b"]),
    ("c", "cé", "se", ["k", "s"]),
    ("d", "dé", "de", ["d"]),
    ("e", "e", "ə", ["ə", "e", "ɛ"]),
    ("f", "effe", "ɛf", ["f"]),
    ("g", "gé", "ʒe", ["ɡ", "ʒ"]),
    ("h", "ache", "aʃ", []),
    ("i", "i", "i", ["i"]),
    ("j", "ji", "ʒi", ["ʒ"]),
    ("k", "ka", "ka", ["k"]),
    ("l", "elle", "ɛl", ["l"]),
    ("m", "emme", "ɛm", ["m"]),
    ("n", "enne", "ɛn", ["n"]),
    ("o", "o", "o", ["o"]),
    ("p", "pé", "pe", ["p"]),
    ("q", "ku", "ky", ["k"]),
    ("r", "erre", "ɛʁ", ["ʁ"]),
    ("s", "esse", "ɛs", ["s", "z"]),
    ("t", "té", "te", ["t"]),
    ("u", "u", "y", ["y"]),
    ("v", "vé", "ve", ["v"]),
    ("w", "double vé", "dubləve", ["w", "v"]),
    ("x", "ics", "iks", ["ks", "ɡz", "s", "z"]),
    ("y", "i grec", "iɡʁɛk", ["i", "j"]),
    ("z", "zède", "zɛd", ["z"]),
]


def symbols(ipa: str) -> list[str]:
    """Split a transcription into inventory symbols, longest match first.

    Anything that is not in the inventory comes out as a one-character symbol,
    so that it shows up in the check below.
    """
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


def shape(syms: list[str]) -> str:
    """The pattern of a name: a vowel, vowel after the consonant, before it, or other."""
    pattern = "".join("V" if s in VOWELS else "C" for s in syms)
    return {"V": "a vowel", "CV": "vowel after", "VC": "vowel before"}.get(pattern, "other")


def show(label: str, items) -> None:
    items = sorted(items)
    print(f"   {label:<40} {len(items):>2}: {' '.join(items) if items else '-'}")


def main() -> None:
    checks: dict[str, bool] = {}

    # ------------------------------------------------------------------ 1
    print("1. The 26 names, symbol by symbol")
    used: set[str] = set()
    unknown: set[str] = set()
    for letter, name, ipa, _ in ALPHABET:
        syms = symbols(ipa)
        used |= set(syms)
        unknown |= {s for s in syms if s not in FRENCH}
        plural = "symbol" if len(syms) == 1 else "symbols"
        print(f"   {letter}  {name:<10} /{ipa}/".ljust(32) + f"{len(syms)} {plural}, {shape(syms)}")
    print()
    show("distinct symbols in the names", used)
    show("not in Le Robert's inventory", unknown)
    show("French-only sounds the alphabet drills", used & FRENCH_ONLY)
    show("French-only sounds it leaves out", FRENCH_ONLY - used)
    checks["every symbol is a French phoneme"] = not unknown
    checks["the alphabet drills /a o y ɛ ʁ/"] = used & FRENCH_ONLY == {"a", "o", "y", "ɛ", "ʁ"}

    # ------------------------------------------------------------------ 2
    print()
    print("2. The e of a name: closed /e/ when it ends the name, open /ɛ/ before a consonant")
    seen = obeyed = 0
    exceptions = []
    for letter, name, ipa, _ in ALPHABET:
        syms = symbols(ipa)
        for i, s in enumerate(syms):
            if s not in ("e", "ɛ"):
                continue
            seen += 1
            ends_the_name = i == len(syms) - 1
            expected = "e" if ends_the_name else "ɛ"
            where = "ends the name" if ends_the_name else f"before /{syms[i + 1]}/"
            ok = s == expected
            obeyed += ok
            if not ok:
                exceptions.append(name)
            print(f"   {name:<10} /{ipa}/".ljust(26) + f"/{s}/ {where:<14} {'as the rule says' if ok else 'EXCEPTION'}")
    print(f"   {seen} e's in the names, {obeyed} as the rule says, {len(exceptions)} exceptions")
    checks["every e obeys the rule"] = seen == 16 and not exceptions

    # ------------------------------------------------------------------ 3
    print()
    print("3. The shape of a consonant's name: by its Latin class, and by its French sound")
    latin_ok = latin_total = 0
    by_sound_mismatch = []
    for letter, name, ipa, _ in ALPHABET:
        syms = symbols(ipa)
        sh = shape(syms)
        if sh not in ("vowel after", "vowel before"):
            continue
        consonant = syms[0] if sh == "vowel after" else syms[-1]
        sound_class = "stop" if consonant in STOPS else "continuant"
        sound_fits = (sound_class == "stop") == (sh == "vowel after")
        if not sound_fits:
            by_sound_mismatch.append(letter)
        latin = "stop" if letter in LATIN_STOPS else "continuant" if letter in LATIN_CONTINUANTS else "-"
        latin_fits = ""
        if latin != "-":
            latin_total += 1
            fits = (latin == "stop") == (sh == "vowel after")
            latin_ok += fits
            latin_fits = "fits" if fits else "BREAKS"
        print(
            f"   {letter}  {name:<10} {sh:<13} /{consonant}/ {sound_class:<10} {'fits' if sound_fits else 'does not fit':<12}"
            f" Latin {latin:<10} {latin_fits}"
        )
    print(f"   by the Latin class:  {latin_ok} of {latin_total} Latin consonant letters fit the rule")
    print(f"   by the French sound: {len(by_sound_mismatch)} do not: {' '.join(by_sound_mismatch)}")
    checks["Latin class predicts every shape"] = latin_ok == latin_total == 14
    checks["French sound fails on c g j v"] = by_sound_mismatch == ["c", "g", "j", "v"]

    # ------------------------------------------------------------------ 4
    print()
    print("4. Does the name contain a sound the letter spells?")
    without = []
    for letter, name, ipa, sounds in ALPHABET:
        joined = "".join(symbols(ipa))
        found = [s for s in sounds if nfd(s) in joined]
        if not found:
            without.append(letter)
        print(f"   {letter}  {name:<10} /{ipa}/".ljust(32) + (f"yes: /{found[0]}/" if found else "no: the letter spells no sound"))
    print(f"   names without their letter's sound: {len(without)} ({' '.join(without)})")
    checks["only h lacks its own sound"] = without == ["h"]

    # ------------------------------------------------------------------ 5
    print()
    print("5. Checks")
    for label, ok in checks.items():
        print(f"   {label + ':':<40} {ok}")


if __name__ == "__main__":
    main()
