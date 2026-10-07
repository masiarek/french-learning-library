# 02_Yosser_teacher — the teacher's worksheets, one lesson at a time

**Level:** 101 · for the owner, going over each worksheet after the class

The owner's French teacher, Yosser, gives a worksheet per lesson: a reading text, exercises on it, a grammar point, and a *Corrigé* with the answers. This chapter keeps each worksheet as one table, every line in French, in English, and in the IPA of Le Robert's key, so that a line can be read, understood and pronounced from one row.

| # | Lesson | What it holds |
|---|---|---|
| 1 | [Lesson 1: La maison — français, anglais, IPA](lesson_01_la_maison/README.md) | The rooms and furniture of a house, a reading text about Adam's house, comprehension questions, *vrai ou faux*, fill-ins, *il y a*, the prepositions of place, and the Corrigé |

How to read a lesson's table: French as printed, bold rows for the sections, `________` for a blank; English as a translation; IPA after Le Robert's key, from memory, with ‿ for a compulsory liaison, (t)‿ for the optional one after *est*, and the Corrigé's answer in square brackets where the worksheet leaves a blank. Each lesson ends with an **AI section**, mine and not the teacher's: notes on particular words, each word of the lesson in two or three set phrases, the lesson's words in new sentences, a few new words, and new exercises with their answers, in the same table.

## Anki

Two sets, kept apart from the textbook's, each one file with a subdeck per lesson:

| Set | File | On the front | On the back |
|---|---|---|---|
| Yosser (FR-EN) | [`anki/yosser_fr_en.txt`](anki/yosser_fr_en.txt) | the French | the English and the IPA; also the exercises, with their answers |
| Yosser (EN-FR) | [`anki/yosser_en_fr.txt`](anki/yosser_en_fr.txt) | the English | the French and the IPA; also the challenges written by hand, under their own subdeck |

Each lesson folder holds its own decks under `anki/`: the two generated from the lesson's table by `tools/anki_from_tables.py`, and the challenges. Cards carry the tags `fr-en`, `en-fr`, `exercise` and `challenge`.
