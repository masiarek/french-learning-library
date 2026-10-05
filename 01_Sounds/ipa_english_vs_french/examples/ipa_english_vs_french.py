"""English and French in the IPA: one alphabet, two inventories.

The International Phonetic Alphabet is one alphabet for every language, so a
symbol means the same sound in an English dictionary and in a French one. What
differs is which symbols each language needs. This program holds the two
inventories as sets, prints what they share and what each has alone, and then
reads two dictionary-style transcriptions symbol by symbol and says, for each
symbol, which language it belongs to. It also checks the three marks that give
a transcription's language away before any vowel is read: stress, length and
the nasal tilde.

Inventories: British English after the Oxford Learner's Dictionaries key
(Received Pronunciation: 44 phonemes plus the two weak vowels i and u); French after Le Robert's key (the
standard Parisian inventory, with the four nasal vowels and the e muet).
"""

from __future__ import annotations

import unicodedata

# ----------------------------------------------------------------------------
# The two inventories
# ----------------------------------------------------------------------------

ENGLISH_CONSONANTS = set("p b t d k ɡ f v θ ð s z ʃ ʒ h m n ŋ l r w j".split()) | {"tʃ", "dʒ"}
# Oxford's key adds two weak vowels to the 44: the i of "happy" and the u of
# "situation", short and unstressed, written without a length mark.
ENGLISH_VOWELS = (
    set("ɪ e æ ʌ ɒ ʊ ə i u".split())
    | set("iː ɑː ɔː uː ɜː".split())
    | set("eɪ aɪ ɔɪ əʊ aʊ ɪə eə ʊə".split())
)
ENGLISH = ENGLISH_CONSONANTS | ENGLISH_VOWELS

FRENCH_CONSONANTS = set("p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ w j ɥ".split())
FRENCH_VOWELS = set("i e ɛ a ɑ ɔ o u y ø œ ə".split()) | set("ɑ̃ ɛ̃ ɔ̃ œ̃".split())
FRENCH = FRENCH_CONSONANTS | FRENCH_VOWELS

# Marks that are not sounds but tell the two apart at a glance.
STRESS = "ˈ"
LENGTH = "ː"
TILDE = "̃"  # the combining tilde that makes a nasal vowel

# ----------------------------------------------------------------------------
# The two sentences, transcribed as Oxford Learner's and Le Robert would
# ----------------------------------------------------------------------------

ENGLISH_SENTENCE = "The quick brown fox jumps over the lazy dog."
ENGLISH_IPA = "ðə kwɪk braʊn fɒks dʒʌmps ˈəʊvə ðə ˈleɪzi dɒɡ"

FRENCH_SENTENCE = "Le petit chien brun saute par-dessus la vieille clôture."
FRENCH_IPA = "lə pəti ʃjɛ̃ bʁœ̃ sot paʁdəsy la vjɛj klotyʁ"


def symbols(ipa: str, inventory: set[str]) -> list[str]:
    """Split a transcription into the symbols of an inventory.

    Greedy, longest match first, so that a diphthong such as əʊ or an affricate
    such as dʒ is one symbol and not two. A combining tilde stays with its
    vowel because the nasal vowels are in the inventory as two code points.
    Stress marks and spaces are skipped; anything else unknown is kept as a
    one-character symbol so that it shows up as unplaced in the report.
    """
    text = unicodedata.normalize("NFD", ipa)
    longest = max(len(s) for s in inventory)
    out: list[str] = []
    i = 0
    while i < len(text):
        if text[i] in (" ", STRESS):
            i += 1
            continue
        for n in range(longest, 0, -1):
            piece = text[i : i + n]
            if piece in inventory:
                out.append(piece)
                i += n
                break
        else:
            out.append(text[i])
            i += 1
    return out


def show(title: str, items: set[str]) -> None:
    print(f"{title:<28} {len(items):>2}: {' '.join(sorted(items))}")


def main() -> None:
    print("1. The inventories as sets")
    show("English (RP) phonemes", ENGLISH)
    show("French phonemes", FRENCH)
    show("in both", ENGLISH & FRENCH)
    show("English only", ENGLISH - FRENCH)
    show("French only", FRENCH - ENGLISH)
    print()

    print("2. The marks that give the language away")
    for name, ipa in (("English", ENGLISH_IPA), ("French", FRENCH_IPA)):
        nfd = unicodedata.normalize("NFD", ipa)
        print(
            f"   {name:<8} stress marks {nfd.count(STRESS)}  "
            f"length marks {nfd.count(LENGTH)}  nasal tildes {nfd.count(TILDE)}"
        )
    print()

    print("3. Each sentence, symbol by symbol")
    for name, sentence, ipa, own, other in (
        ("English", ENGLISH_SENTENCE, ENGLISH_IPA, ENGLISH, FRENCH),
        ("French", FRENCH_SENTENCE, FRENCH_IPA, FRENCH, ENGLISH),
    ):
        syms = symbols(ipa, own)
        used = set(syms)
        print(f"   {name}: {sentence}")
        print(f"   /{ipa}/")
        print(f"   {len(syms)} symbols, {len(used)} distinct")
        show("     shared with the other", used & other)
        show(f"     {name} only", used - other)
        unplaced = used - own
        print(f"     not in the inventory      {len(unplaced):>2}: {' '.join(sorted(unplaced)) or '-'}")
        print()

    print("4. Checks")
    e_used = set(symbols(ENGLISH_IPA, ENGLISH))
    f_used = set(symbols(FRENCH_IPA, FRENCH))
    print("   every English symbol is an English phoneme:", e_used <= ENGLISH)
    print("   every French symbol is a French phoneme:   ", f_used <= FRENCH)
    print("   the English line has a stress mark:        ", STRESS in ENGLISH_IPA)
    print("   the French line has no stress mark:        ", STRESS not in FRENCH_IPA)
    print("   the French line has a nasal vowel:         ", TILDE in unicodedata.normalize("NFD", FRENCH_IPA))
    print("   the English line has no nasal vowel:       ", TILDE not in unicodedata.normalize("NFD", ENGLISH_IPA))
    print("   the English line has a diphthong:          ", bool(e_used & {"eɪ", "aɪ", "ɔɪ", "əʊ", "aʊ"}))
    print("   the French line has none:                  ", not (f_used & {"eɪ", "aɪ", "ɔɪ", "əʊ", "aʊ"}))


if __name__ == "__main__":
    main()
