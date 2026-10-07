# 02_Yosser_teacher — the teacher's worksheets, one lesson at a time

**Level:** 101 · for the owner, going over each worksheet after the class

The owner's French teacher, Yosser, gives a worksheet per lesson: a reading text, exercises on it, a grammar point, and a *Corrigé* with the answers. This chapter keeps each worksheet as one table, every line in French, in English, and in the IPA of Le Robert's key, so that a line can be read, understood and pronounced from one row. A program per lesson reads the table back from the page and checks what no eye checks across a hundred and sixty rows: that every symbol is a French phoneme, which nasal vowels and liaisons occur, and how much of the worksheet rests on its grammar point.

| # | Lesson | What it holds |
|---|---|---|
| 1 | [Lesson 1: La maison — français, anglais, IPA](lesson_01_la_maison/README.md) | The rooms and furniture of a house, a reading text about Adam's house, comprehension questions, *vrai ou faux*, fill-ins, *il y a*, the prepositions of place, and the Corrigé |

How to read a lesson's table: French as printed, bold rows for the sections, `________` for a blank; English as a translation; IPA after Le Robert's key, from memory, with ‿ for a compulsory liaison, (t)‿ for the optional one after *est*, and the Corrigé's answer in square brackets where the worksheet leaves a blank. A program under each table reads it back from the page and checks it.

## Anki

One file imports the whole chapter, kept apart from the textbook's: [`anki/yosser_teacher_all.txt`](anki/yosser_teacher_all.txt), with a subdeck per lesson. Each lesson folder has its own two decks under `anki/`: one generated from the lesson's table by `tools/anki_from_tables.py` (every word, question and sentence, French to English and English to French, and the exercises with their answers), and one of challenges written by hand (answer the comprehension questions, correct the false statements, say it, which article). Cards carry the tags `fr-en`, `en-fr`, `exercise` and `challenge`.

## Po polsku, w skrócie

Ten rozdział zbiera karty pracy od nauczycielki francuskiego, lekcja po lekcji. Każda karta jest jedną tabelą: każda linijka po francusku, po angielsku i w transkrypcji fonetycznej według klucza Le Roberta, tak aby z jednego wiersza dało się zdanie przeczytać, zrozumieć i wymówić. Program przy każdej lekcji czyta tabelę ze strony i sprawdza to, czego oko nie sprawdzi w stu sześćdziesięciu wierszach: czy każdy znak jest francuskim fonemem, które samogłoski nosowe i jakie łączenia międzywyrazowe (liaison) występują, i jak duża część karty opiera się na jej punkcie gramatycznym.

## Auf Deutsch: Stichwörter

Jedes Arbeitsblatt der Lehrerin steht hier als eine Tabelle, Zeile für Zeile auf Französisch, Englisch und in Lautschrift, und ein Programm liest die Tabelle zurück und prüft jedes Zeichen.

Arbeitsblatt · Lautschrift · Bindung (liaison) · Nasalvokal · Lösungsschlüssel · Lesetext · Übung
