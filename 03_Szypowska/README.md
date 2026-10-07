# 03_Szypowska — a Polish textbook of French, one page per lesson

**Level:** 101 · for a Polish reader learning French from Szypowska's course

The owner's Polish textbook of French, by Szypowska, teaches in numbered lessons: a reading text or dialogue with the book's own phonetic transcription under every line, a word list with Polish glosses, notes on pronunciation and realia, a grammar section in Polish, and exercises. This chapter keeps the French of each lesson as one table: the French as printed, the English with the Polish below it, and the pronunciation in Le Robert's IPA. The Polish explanations are not transcribed; the French words inside them are. An exercise that asks for a translation into French gets the French and its IPA, with the English and the book's Polish below.

| # | Lesson | What it holds |
|---|---|---|
| 3 | [Lesson 3: Regardons des photos](lecon_03_regardons_des_photos/README.md) | Photos of Suzanne and Pierre, Paris and Warsaw; the word list; the imperative, the definite article, *de* as the genitive, *à* with a city; the exercises with a translation into French |
| 4 | [Lesson 4: Chez les Lefèvre](lecon_04_chez_les_lefevre/README.md) | A visit to the Lefèvres' flat, rue du Bac; the word list; the letter *c*; elision; *du, de la, de l', des*; the exercises with a translation into French |
| 5 | [Lesson 5: Dialogue](lecon_05_dialogue/README.md) | *J'ai un stylo*: *avoir* in the present, affirmative, negative and interrogative; *ne … pas de*; *est-ce que* against inversion; the word list; the exercises with a translation into French |

How to read a lesson's table: French as printed, bold rows for the sections, `________` for a blank; English with the Polish below it, the book's Polish in the word lists and the grammar examples and mine elsewhere; IPA after Le Robert's key, from memory, with ‿ for a compulsory liaison. The answers to the exercises are mine, not the book's: an answer follows the sentence after →, or sits in square brackets inside the IPA where the sentence has a blank. A program under each table reads it back from the page and holds the book's own brackets to it with the key below.

## Anki

One file imports the whole chapter: [`anki/szypowska_all.txt`](anki/szypowska_all.txt), with a subdeck per lesson. Each lesson folder also has its own two decks under `anki/`: one generated from the lesson's table by `tools/anki_from_tables.py` (every word, question and sentence, French to meaning and meaning to French, and the exercises with their answers), and one of challenges written by hand (say it, make it negative, read the book's bracket, which article). Cards carry the tags `fr-en`, `en-fr`, `exercise` and `challenge`, so one direction can be suspended at a stroke.

## The book's notation, and Le Robert's

The book writes its transcriptions in square brackets with a notation made for Polish readers, not in the IPA. It is a one-to-one relettering of the IPA except in two points: the book marks vowel length with a colon, which Le Robert does not mark, and it writes the final *o* of *photo* as the open [ɔ], where Le Robert has /o/. The key, which every lesson's program applies to the book's brackets and checks against the page's IPA:

| The book writes | Le Robert writes | Example |
|---|---|---|
| ż | /ʒ/ | Jean [żã] /ʒɑ̃/ |
| sz | /ʃ/ | la chambre [la szã:br] /la ʃɑ̃bʁ/ |
| ã | /ɑ̃/ | la France [la frã:s] /la fʁɑ̃s/ |
| õ | /ɔ̃/ | on [õ] /ɔ̃/ |
| ɛ̃, œ̃ | /ɛ̃/, /œ̃/, the same | le bain [lə bɛ̃] /lə bɛ̃/, un [œ̃] /œ̃/ |
| ü | /y/ | Suzanne [süzan] /syzan/ |
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
| ə ɛ ɔ e i u a ø j | the same | le palais [lə palɛ] /lə palɛ/ |

The order matters when a machine applies it: *wua* and *üi* are read before *ua*, *ui* and *w*, or the *w* that *ua* produces would turn into a *v*. The programs read the brackets left to right, longest match first, and never re-read what they have written.

How sure: the key is read off the pages in hand, so it is certain for the symbols they use; a later lesson may bring a symbol not yet listed. The Le Robert side is written from memory, as in the [Sounds](../01_Sounds/README.md) chapter, and the two places where the book and Le Robert differ, *photo* and the first vowel of *Eiffel*, are both heard in France.
