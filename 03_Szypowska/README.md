# 03_Szypowska — a Polish textbook of French, one page per lesson

**Level:** 101 · for a Polish reader learning French from Szypowska's course

The owner's Polish textbook of French, by Szypowska, teaches in numbered lessons: a reading text or dialogue with the book's own phonetic transcription under every line, a word list with Polish glosses, notes on pronunciation and realia, a grammar section in Polish, and exercises. This chapter keeps the French of each lesson as one table: the French as printed, the English, and the pronunciation in Le Robert's IPA. The book's Polish, its glosses and its explanations, is not on these pages: the owner had it removed on 2026-10-10; the French words inside the explanations are kept. An exercise that asks for a translation into French gets the French and its IPA, with the English.

| # | Lesson | What it holds |
|---|---|---|
| 3 | [Lesson 3: Regardons des photos](lecon_03_regardons_des_photos/README.md) | Photos of Suzanne and Pierre, Paris and Warsaw; the word list; the imperative, the definite article, *de* as the genitive, *à* with a city; the exercises with a translation into French |
| 4 | [Lesson 4: Chez les Lefèvre](lecon_04_chez_les_lefevre/README.md) | A visit to the Lefèvres' flat, rue du Bac; the word list; the letter *c*; elision; *du, de la, de l', des*; the exercises with a translation into French |
| 5 | [Lesson 5: Dialogue](lecon_05_dialogue/README.md) | *J'ai un stylo*: *avoir* in the present, affirmative, negative and interrogative; *ne … pas de*; *est-ce que* against inversion; the word list; the exercises with a translation into French |
| 6 | [Lesson 6: En visite](lecon_06_en_visite/README.md) | A Sunday visit to the Bertins in Chaville: the numbers six to twelve; *au, à la, à l', aux*, the dative; adjectives agree; plurals in *-eaux*, *messieurs, mesdames*; the article for a kind in general; inversion after direct speech; the exercises with a translation into French |

How to read a lesson's table: French as printed, bold rows for the sections, `________` for a blank; English; IPA after Le Robert's key, from memory, with ‿ for a compulsory liaison. The answers to the exercises are mine, not the book's: an answer follows the sentence after →, or sits in square brackets inside the IPA where the sentence has a blank. Each lesson ends with an **AI section**, mine and not the book's: notes on particular words and expressions, each word of the lesson in two or three set phrases, the lesson's words in new sentences, a few new words, and new exercises with their answers, in the same table.

## Anki

Two sets, each one file with a subdeck per lesson:

| Set | File | On the front | On the back |
|---|---|---|---|
| Szypowska (FR-EN) | [`anki/szypowska_fr_en.txt`](anki/szypowska_fr_en.txt) | the French, with the IPA under it | the English; also the exercises, with their answers |
| Szypowska (EN-FR) | [`anki/szypowska_en_fr.txt`](anki/szypowska_en_fr.txt) | the English | the French and the IPA; also the challenges written by hand, under their own subdeck |

Each lesson folder holds its own decks under `anki/`: the two generated from the lesson's table by `tools/anki_from_tables.py`, the challenges, and two import files, `<lesson>_import_szypowska_fr_en.txt` and `<lesson>_import_szypowska_en_fr.txt`, which hold that lesson alone (the challenges under the second) for importing a new lesson without touching the rest. Cards carry the tags `fr-en`, `en-fr`, `exercise` and `challenge`. Until 2026-10-10 the two sets were Szypowska (FR-PL) and (PL-FR), with the book's Polish on the cards; a deck imported under those names stays in Anki until it is deleted there, and these files import under the new names.

## The book's notation, and Le Robert's

The book writes its transcriptions in square brackets with a notation made for Polish readers, not in the IPA. It is a one-to-one relettering of the IPA except in two points: the book marks vowel length with a colon, which Le Robert does not mark, and it writes the final *o* of *photo* as the open [ɔ], where Le Robert has /o/. The key:

| The book writes | Le Robert writes | Example |
|---|---|---|
| ż | /ʒ/ | Jean [żã] /ʒɑ̃/ |
| sz | /ʃ/ | la chambre [la szã:br] /la ʃɑ̃bʁ/ |
| ã | /ɑ̃/ | la France [la frã:s] /la fʁɑ̃s/ |
| õ | /ɔ̃/ | on [õ] /ɔ̃/ |
| ɛ̃, œ̃ | /ɛ̃/, /œ̃/, the same | le bain [lə bɛ̃] /lə bɛ̃/, un [œ̃] /œ̃/ |
| ü | /y/ | Suzanne [süzan] /syzan/ |
| ö | /œ/ | neuf [nöf] /nœf/, la sœur [lasö:r] /la sœʁ/ |
| üi | /ɥi/ | la cuisine [la küizin] /la kɥizin/ |
| ui | /wi/ | oui [ui] /wi/ |
| ua | /wa/ | trois [trua] /tʁwa/ |
| wua | /vwa/ | voilà [wuala] /vwala/ |
| w | /v/ | Varsovie [warsɔwi] /vaʁsɔvi/ |
| ń | /ɲ/ | la Pologne [la pɔlɔń] /la pɔlɔɲ/ |
| r | /ʁ/ | regarde [rəgard] /ʁəɡaʁd/ |
| g | /ɡ/ | le garçon [lə garsõ] /lə ɡaʁsɔ̃/ |
| a: ɛ: u: ü: ã: (a colon for length) | no length mark | la tour [la tu:r] /la tuʁ/ |
| final -o as ɔ | /o/ | la photo [la fɔtɔ] /la fɔto/ |
| ə ɛ ɔ e i u a ø j | the same | le palais [lə palɛ] /lə palɛ/, les messieurs [lemesjø] /le mesjø/ |

How sure: the key is read off the pages in hand, so it is certain for the symbols they use; a later lesson may bring a symbol not yet listed. The Le Robert side is written from memory, as in the [Sounds](../01_Sounds/README.md) chapter. The brackets of lessons 3 to 5 were relettered with this key and compared with the pages' IPA when the pages were written: they agree except for *photo*, the first vowel of *Eiffel*, the *o* of *interrogative*, and one [że] the book prints for *je* in lesson 5 where its own word list has [żənepa].
