# 02_Yosser_teacher — the teacher's worksheets, one lesson at a time

**Level:** 101 · for the owner, going over each worksheet after the class

The owner's French teacher, Yosser, gives a worksheet per lesson: a reading text, exercises on it, a grammar point, and a *Corrigé* with the answers. This chapter keeps each worksheet as one table, every line in French, in English, and in the IPA of Le Robert's key, so that a line can be read, understood and pronounced from one row.

| # | Lesson | What it holds |
|---|---|---|
| 1 | [Lesson 1: La maison — français, anglais, IPA](lesson_01_la_maison/README.md) | The rooms and furniture of a house, a reading text about Adam's house, comprehension questions, *vrai ou faux*, fill-ins, *il y a*, the prepositions of place, and the Corrigé |
| 2 | [Lesson 1, the reading: Ma maison — each sentence with its IPA](lesson_01_lecture_ma_maison/README.md) | The same text, questions and true-or-false statements, each sentence standing alone with its transcription under it, for reading aloud on a phone; no table and no decks of its own, the lesson page has them; and sections 7 to 10, the grammar of il y a and its six sentences, the prepositions of place and the model description of a house, the same way |
| 3 | [Lesson 2: Être et avoir — français, anglais, IPA](lesson_02_etre_avoir/README.md) | The present of *être* and *avoir* with the worksheet's examples, *à retenir*, two exercises with the answers (the sheet's *Je ________ un livre* corrected to *J'ai*); and in the AI section, *ils sont* against *ils ont*, *avoir* for age, hunger and cold, *ne … pas de*, inversion with *-t-*, and questions about yourself. The owner records the lesson as audio drills on a Mac, [recipe in Resources](../RESOURCES.md#audio-of-a-lesson-on-a-mac) |
| 4 | [Lesson 3: Où est … ? Asking about location — français, anglais, IPA](lesson_03_ou_est/README.md) | An A1 grammar card the owner sent with the teacher's lessons, on 2026-10-11, from an app or course not named on the screen: *où est, où sont, où se trouve*, *qu'est-ce que*, *quel, quelle, quels, quelles*, its examples and three structure tables; in the AI section, the answers (*à droite, en face de, près d'ici*), *quel* to fill in, questions to make from answers, and a dialogue in the street |

How to read a lesson's table: French as printed, bold rows for the sections, `________` for a blank; English as a translation; IPA after Le Robert's key, from memory, with ‿ for a compulsory liaison, (t)‿ for the optional one after *est*, and the Corrigé's answer in square brackets where the worksheet leaves a blank. Each lesson ends with an **AI section**, mine and not the teacher's: notes on particular words, each word of the lesson in two or three set phrases, the lesson's words in new sentences, a few new words, and new exercises with their answers, in the same table.

## Anki

Two sets, kept apart from the textbook's, each one file with a subdeck per lesson:

| Set | File | On the front | On the back |
|---|---|---|---|
| Yosser (FR-EN) | [`anki/yosser_fr_en.txt`](anki/yosser_fr_en.txt) | the French, with the IPA under it | the English; also the exercises, with their answers |
| Yosser (EN-FR) | [`anki/yosser_en_fr.txt`](anki/yosser_en_fr.txt) | the English | the French and the IPA; also the challenges written by hand, under their own subdeck |

Each lesson folder holds its own decks under `anki/`: the two generated from the lesson's table by `tools/anki_from_tables.py`, the challenges, and two import files, `<lesson>_import_yosser_fr_en.txt` and `<lesson>_import_yosser_en_fr.txt`, which hold that lesson alone (the challenges under the second) for importing a new lesson without touching the rest. Cards carry the tags `fr-en`, `en-fr`, `exercise` and `challenge`.
