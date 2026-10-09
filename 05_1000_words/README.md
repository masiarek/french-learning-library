# 05_1000_words — a thousand words, one page each

**Level:** 101 · for the owner, one word at a time

The owner learns vocabulary with an app that holds a thousand common French words and shows one entry at a time: the headword, its definitions with the part of speech, the irregular forms where there are any, and one example sentence, each with a voice but without a transcription. This chapter keeps each word as one page: the app’s entry as a table with the IPA of Le Robert’s key added to every line, and under it an AI section with the grammar the word needs (its conjugation, its forms, where it parts from English), the word in set phrases, my own example sentences, and exercises with the answers, every line in French, in English and in IPA. The owner asked for separate pages so that a word can carry a longer explanation.

The table numbers the words in the order they arrived, so the last number is the count so far. The sidebar lists the pages A to Z, as a dictionary does.

| # | Word | English | The grammar on the page |
|---|---|---|---|
| 1 | [devoir](devoir/README.md) /dəvwaʁ/ | must, to have to; to owe | two stems, *dû* against *du*, *devrais* as *should*, *must* of probability, the noun *le devoir* |
| 2 | [tout](tout/README.md) /tu/ | all, every; the whole | *tout, toute, tous, toutes*; *tous* as /tu/ and /tus/; the adverb that agrees by sound; *tout à fait, tout de suite* |
| 3 | [dormir](dormir/README.md) /dɔʁmiʁ/ | to sleep | the *partir* pattern of *-ir* verbs, a singular that drops a consonant, the question by inversion, *s’endormir* |
| 4 | [aller](aller/README.md) /ale/ | to go; to be (feeling) | three stems, the near future, *être* as its auxiliary, *comment allez-vous*, *vas-y* |
| 5 | [sur](sur/README.md) /syʁ/ | on, upon, on top of | where English says *in* or *at*, *about*, *out of*; *sur, sûr* and *sous*; the vowel /y/ |
| 6 | [venir](venir/README.md) /vəniʁ/ | to come | two stems and the denasalised *viennent*, the recent past *venir de*, origin with *de*, the family *tenir, devenir, revenir* |
| 7 | [être](etre/README.md) /ɛtʁ/ | to be; a being | three stems, *fus* of the books, *soyez*, *été*, the auxiliary of movement and reflexive verbs, *avoir* where English says *to be* |

How to read a page: a few bullets on the word first, then the app’s entry as a table, French as the app prints it, English as the app gives it with the part of speech in brackets, IPA after Le Robert’s key, from memory. Bold rows name the sections, `________` is a blank, ‿ a compulsory liaison and (t)‿ or (z)‿ an optional one, a · separates the two words of a minimal pair, and the answer to an exercise stands in square brackets in the IPA where the sentence has a blank. Everything under the **AI section** heading is mine and not the app’s: the grammar in bullets and a conjugation table, the set phrases, my examples, and the exercises, in the same three columns. Every French word on a page carries its IPA, the bullets included.

Where the entries come from: a screenshot of the app, sent by the owner one word at a time, sometimes several in a sitting. The app’s name was not given; its entries read like a frequency list of the thousand most common words, which is the owner’s name for it too. A word that is already on a page is not added again; a new sense or form the app shows for it extends the page.

## Anki

Two sets, kept apart from the teacher’s, the textbook’s and the videos’, each one file with a subdeck per word:

| Set | File | On the front | On the back |
|---|---|---|---|
| 1000 words (FR-EN) | [`anki/1000_words_fr_en.txt`](anki/1000_words_fr_en.txt) | the French, with the IPA under it | the English; also the exercises, with their answers |
| 1000 words (EN-FR) | [`anki/1000_words_en_fr.txt`](anki/1000_words_en_fr.txt) | the English | the French and the IPA; also the challenges written by hand, under their own subdeck |

Each word folder holds its own decks under `anki/`: the two generated from the page’s tables by `tools/anki_from_tables.py`, the challenges, and two import files, `<word>_import_1000_words_fr_en.txt` and `<word>_import_1000_words_en_fr.txt`, which hold that word alone (the challenges under the second) for importing a new word without touching the rest. Cards carry the tags `fr-en`, `en-fr`, `exercise` and `challenge`.
