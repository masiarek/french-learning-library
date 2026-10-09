# French — Learning Library

<!-- --8<-- [start:hero] -->

A learning library for French, built the same way as its siblings [math-learning-library ↗](https://github.com/masiarek/math-learning-library), [learning-to-learn-library ↗](https://github.com/masiarek/learning-to-learn-library) and [rust-learning-library ↗](https://github.com/masiarek/rust-learning-library): **one idea per page, and every claim that a program can check, checked by a program that actually runs.**

No page here hand-types what a program prints. A lesson of the Sounds chapter links a real `.py` file; a tool runs it, checks the output against a recorded answer key, and pastes that verified output into the page. CI fails if any of the three drift apart. The three source chapters, the teacher's worksheets, the Polish textbook and the pronunciation videos, are tables for the owner's own learning and carry no program; CI checks every transcription in them against Le Robert's inventory instead. So when a page says *"English and French share 21 IPA symbols, and 17 of them are consonants"*, that is not an impression; it is the output of a set difference.

Much of a language cannot be checked by a program: how a vowel sounds, whether a phrase is idiomatic. Those claims name their source, a dictionary or a grammar, and say how sure they are.

The examples are **stdlib-only, on purpose**. If you have `python3`, you can run every page in this repo.

📖 **Read it as a site:** <https://masiarek.github.io/french-learning-library/>

<!-- --8<-- [end:hero] -->

<!-- --8<-- [start:below-hero] -->

## Start here

[**01_Sounds/**](01_Sounds/README.md) — *What does the French in the dictionary sound like?*

| Lesson | What it teaches |
|---|---|
| [English and French in the IPA](01_Sounds/ipa_english_vs_french/README.md) | One alphabet, two inventories: 21 shared symbols, 15 French-only (nasal vowels, /y ø œ/, /ʁ/), 25 English-only (/θ ð h/, lax vowels, length, diphthongs), and the marks that identify the language before a vowel is read |
| [Four inventories](01_Sounds/four_inventories/README.md) | English, French, German and Polish side by side: 14 symbols in all four, all consonants; French has 8 new sounds for a German speaker, 11 for a Polish one, 15 for an English one |

[**02_Yosser_teacher/**](02_Yosser_teacher/README.md) — *The teacher's worksheets, one lesson at a time*

| Lesson | What it teaches |
|---|---|
| [Lesson 1: La maison](02_Yosser_teacher/lesson_01_la_maison/README.md) | The whole worksheet as one table of French, English and IPA, 161 rows: the rooms and furniture, Adam's house, *il y a*, the prepositions of place, the Corrigé |

[**03_Szypowska/**](03_Szypowska/README.md) — *A Polish textbook of French, one page per lesson*

| Lesson | What it teaches |
|---|---|
| [Lesson 3: Regardons des photos](03_Szypowska/lecon_03_regardons_des_photos/README.md) | The reading, the word list, the grammar (imperative, definite article, *de*, *à*) and the exercises as one table of French, English with Polish, and IPA |
| [Lesson 4: Chez les Lefèvre](03_Szypowska/lecon_04_chez_les_lefevre/README.md) | A flat on the rue du Bac, the letter *c*, elision, *du, de la, de l', des*, the exercises with a translation into French |
| [Lesson 5: Dialogue](03_Szypowska/lecon_05_dialogue/README.md) | *Avoir* in the present and in the negative, *ne … pas de*, *est-ce que* against inversion, school things |
| [Lesson 6: En visite](03_Szypowska/lecon_06_en_visite/README.md) | A Sunday visit: the numbers six to twelve, *au, à la, à l', aux*, adjectives that agree, plurals in *-eaux*, *messieurs* and *mesdames*, inversion after direct speech |

[**04_Pronunciation/**](04_Pronunciation/README.md) — *The pronunciation videos, one page each*

| Lesson | What it teaches |
|---|---|
| [Les sons ɑ̃ et ɔ̃](04_Pronunciation/sons_an_on/README.md) | The nasal vowels of *blanc* and *blond*: the spellings behind them, minimal pairs, both sounds in one word, and where the nasal goes away, in French, English and IPA |
| [Le son ɛ](04_Pronunciation/son_e_ouvert/README.md) | The open *e* of *est, mais, lève, être, appelle*: /e/ against /ɛ/, *e* before a consonant that is said, *è, ê, ai, ei*, and the endings *-et, -êt* |
| [The best resources: audio and IPA together](04_Pronunciation/resources/README.md) | Where a native voice and the IPA come together: dictionaries, minimal-pair decks, articulation videos, course books, feedback, AI assistants, each with a verdict and how sure it is |

## Other ways in

- [Topic map](TOPICS.md): every page by subject.
- [Glossary](GLOSSARY.md): the terms, each with the page that explains it.
- [Resources](RESOURCES.md): the dictionaries and books behind the pages.
- [Roadmap](ROADMAP.md): what is written and what is deliberately not written yet.
- [Conventions](CONTRIBUTING.md): the house rules for adding a page.

<!-- --8<-- [end:below-hero] -->
