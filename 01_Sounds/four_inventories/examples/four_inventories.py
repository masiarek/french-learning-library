"""Four phoneme inventories in the IPA: English, French, German, Polish.

The same alphabet, four different drawers of it. The program holds the four
inventories as sets and asks the questions a learner asks: how much do any two
languages share, what is in all four, what does each have alone, and, for a
speaker of English, German or Polish, which French sounds are new. It ends with
the three marks that tell the transcriptions apart before a vowel is read:
stress, length and the nasal tilde.

Sources, all dictionary keys: English after Oxford Learner's Dictionaries
(Received Pronunciation plus the weak i and u); French after Le Robert; German
after the Duden Aussprachewörterbuch; Polish after the Handbook of the IPA's
illustration (Jassem 2003), with the two nasal vowels of ą and ę counted as
phonemes, which not every description does. Symbol choices follow those keys:
Oxford writes the English r as /r/, Jassem the Polish sz and ż as /ʂ ʐ/.
"""

from __future__ import annotations

import unicodedata

C = lambda s: set(s.split())  # noqa: E731  (a short name keeps the tables readable)

ENGLISH = (
    C("p b t d k ɡ f v θ ð s z ʃ ʒ h m n ŋ l r w j tʃ dʒ")
    | C("ɪ e æ ʌ ɒ ʊ ə i u iː ɑː ɔː uː ɜː")
    | C("eɪ aɪ ɔɪ əʊ aʊ ɪə eə ʊə")
)
FRENCH = C("p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ w j ɥ") | C("i e ɛ a ɑ ɔ o u y ø œ ə ɑ̃ ɛ̃ ɔ̃ œ̃")
GERMAN = (
    C("p b t d k ɡ f v s z ʃ ʒ ç x h m n ŋ l ʁ j pf ts tʃ")
    | C("iː ɪ eː ɛ ɛː aː a oː ɔ uː ʊ øː œ yː ʏ ə ɐ")
    | C("aɪ aʊ ɔʏ")
)
POLISH = (
    C("p b t d k ɡ f v s z ʂ ʐ ɕ ʑ x m n ɲ l r w j ts dz tʂ dʐ tɕ dʑ")
    | C("i ɨ ɛ a ɔ u ɛ̃ ɔ̃")
)

LANGS = {"English": ENGLISH, "French": FRENCH, "German": GERMAN, "Polish": POLISH}

# Which marks each language's dictionary transcriptions carry.
MARKS = {
    "English": {"stress": True, "length": True, "tilde": False},
    "French": {"stress": False, "length": False, "tilde": True},
    "German": {"stress": True, "length": True, "tilde": False},
    "Polish": {"stress": False, "length": False, "tilde": True},
}

TILDE = "̃"


def fmt(items: set[str]) -> str:
    return " ".join(sorted(items)) or "-"


def main() -> None:
    names = list(LANGS)

    print("1. Sizes")
    for name, inv in LANGS.items():
        vowels = {s for s in inv if any(ch in "iɪeɛæaɑɒɔoʊuyʏøœəɐʌɜɨ" for ch in s)}
        print(f"   {name:<8} {len(inv):>2} phonemes: {len(inv) - len(vowels):>2} consonants, {len(vowels):>2} vowels")
    print()

    print("2. Shared symbols, pair by pair")
    print("   " + " " * 8 + "".join(f"{n:>9}" for n in names))
    for a in names:
        row = "".join(f"{len(LANGS[a] & LANGS[b]):>9}" for b in names)
        print(f"   {a:<8}{row}")
    print()

    core = set.intersection(*LANGS.values())
    print(f"3. In all four ({len(core)}): {fmt(core)}")
    print()

    print("4. What each language has that none of the other three has")
    for name, inv in LANGS.items():
        others = set.union(*(v for k, v in LANGS.items() if k != name))
        only = inv - others
        print(f"   {name:<8} {len(only):>2}: {fmt(only)}")
    print()

    print("5. What French asks of each speaker (French minus their inventory)")
    for name in ("English", "German", "Polish"):
        new = FRENCH - LANGS[name]
        print(f"   from {name:<8} {len(new):>2} new: {fmt(new)}")
    # German writes its tense vowels long, so e i o u look new only on paper.
    german_short = {s.rstrip("ː") for s in GERMAN}
    new = FRENCH - german_short
    print(f"   from German, length marks ignored: {len(new):>2} new: {fmt(new)}")
    # Polish writes sz and ż as ʂ ʐ; a French ʃ ʒ is close enough to start with.
    polish_near = POLISH | {"ʃ", "ʒ"}
    new = FRENCH - polish_near
    print(f"   from Polish, with ʂ ʐ standing in for ʃ ʒ: {len(new):>2} new: {fmt(new)}")
    print()

    print("6. The marks in a dictionary transcription")
    print("   " + " " * 8 + "   stress   length    tilde")
    for name, m in MARKS.items():
        print(f"   {name:<8}" + "".join(f"{'yes' if m[k] else 'no':>9}" for k in ("stress", "length", "tilde")))
    print()

    print("7. Checks")
    has_tilde = {n: any(TILDE in unicodedata.normalize("NFD", s) for s in inv) for n, inv in LANGS.items()}
    has_length = {n: any("ː" in s for s in inv) for n, inv in LANGS.items()}
    print("   tilde appears in the inventory exactly where the table says:  ", all(has_tilde[n] == MARKS[n]["tilde"] for n in names))
    print("   length mark appears exactly where the table says:            ", all(has_length[n] == MARKS[n]["length"] for n in names))
    print("   Polish and French share both nasal vowels ɛ̃ ɔ̃:               ", {"ɛ̃", "ɔ̃"} <= POLISH & FRENCH)
    print("   German and French share the front rounded vowels ø œ y:       ", {"ø", "œ", "y"} <= {s.rstrip("ː") for s in GERMAN} & FRENCH)
    print("   German and French share the uvular r ʁ:                       ", "ʁ" in GERMAN & FRENCH)
    print("   Polish and French share ɲ and w:                              ", {"ɲ", "w"} <= POLISH & FRENCH)
    print("   English alone has θ ð:                                        ", {"θ", "ð"} <= ENGLISH - FRENCH - GERMAN - POLISH)


if __name__ == "__main__":
    main()
