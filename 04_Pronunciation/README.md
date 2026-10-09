# 04_Pronunciation — the sounds of French, one video at a time

**Level:** 101 · for the owner, repeating after a video

The owner follows the pronunciation Shorts of Anne Le Grand's channel Parlez-vous FRENCH: each one drills a sound or a pair of sounds with a short list of words on the screen, the letters that make the sound in red, and asks the viewer to repeat them several times in a row. This chapter keeps each video as one page: the sound, the spelling rules behind it in a few bullets, the video's own words at the top of the table, and a drill written here for the same sound, every line in French, in English, and in the IPA of Le Robert's key. The [Sounds](../01_Sounds/README.md) chapter reads the alphabet; this one practises it.

| # | Lesson | What it holds |
|---|---|---|
| 1 | [Les sons ɑ̃ et ɔ̃](sons_an_on/README.md) | The two nasal vowels of *blanc* and *blond*: the spellings *an, am, en, em* and *on, om*, minimal pairs, words with each sound and with both, where the nasal goes away, and the video's title and description |
| 2 | [Le son ɛ](son_e_ouvert/README.md) | The open *e* of *est, mais, lève, être, appelle*: /e/ against /ɛ/, *e* before a consonant that is said, *è, ê, ai, ei*, the endings *-et, -êt* |

How to read a lesson's table: French as printed, bold rows for the sections, `________` for a blank; English as a translation; IPA after Le Robert's key, from memory, with ‿ for a compulsory liaison, a · between the two words of a minimal pair, and the answer to an exercise in square brackets where the sentence has a blank. The video writes a sound in square brackets, and its symbol for the open nasal, [ã], is Le Robert's /ɑ̃/; the pages use the dictionary's symbols throughout. Each lesson ends with an **AI section**, mine and not the video's: notes on particular words, the video's words in two or three set phrases, the sound in new sentences, new words that carry it, and new exercises with their answers, in the same table.

Where the video's words come from: a screenshot of the screen, sent by the owner. YouTube is blocked from the cloud, and the captions of a Short are automatic and could not be fetched from the iMac either, so the only readable source of the list is the screen. A video whose screenshot has not arrived yet has the drill alone, and says so.

## Anki

Two sets, kept apart from the teacher's and the textbook's, each one file with a subdeck per lesson:

| Set | File | On the front | On the back |
|---|---|---|---|
| Pronunciation (FR-EN) | [`anki/pronunciation_fr_en.txt`](anki/pronunciation_fr_en.txt) | the French, with the IPA under it | the English; also the exercises, with their answers |
| Pronunciation (EN-FR) | [`anki/pronunciation_en_fr.txt`](anki/pronunciation_en_fr.txt) | the English | the French and the IPA; also the challenges written by hand, under their own subdeck |

Each lesson folder holds its own decks under `anki/`: the two generated from the lesson's table by `tools/anki_from_tables.py`, the challenges, and two import files, `<lesson>_import_pronunciation_fr_en.txt` and `<lesson>_import_pronunciation_en_fr.txt`, which hold that lesson alone (the challenges under the second) for importing a new lesson without touching the rest. Cards carry the tags `fr-en`, `en-fr`, `exercise` and `challenge`.

## The series

The Shorts come from one playlist of the channel ([playlist PLuT0u2X0m8iW8m67rsGqUD6U7LzDKcnw6 ↗](https://www.youtube.com/playlist?list=PLuT0u2X0m8iW8m67rsGqUD6U7LzDKcnw6)). The channel's site, parlez-vous-french.com, has a page of rules for most of the spellings the videos drill (*on* and *om*, *en* and *em*, the liaison), and a page's bullets name it where they follow it; the site is blocked from the cloud, so those rules were read from search summaries.
