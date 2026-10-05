# French — Learning Library

<!-- --8<-- [start:hero] -->

A learning library for French, built the same way as its siblings [math-learning-library ↗](https://github.com/masiarek/math-learning-library), [learning-to-learn-library ↗](https://github.com/masiarek/learning-to-learn-library) and [rust-learning-library ↗](https://github.com/masiarek/rust-learning-library): **one idea per page, and every claim that a program can check, checked by a program that actually runs.**

No page here hand-types what a program prints. Each lesson links a real `.py` file; a tool runs it, checks the output against a recorded answer key, and pastes that verified output into the page. CI fails if any of the three drift apart. So when a page says *"English and French share 21 IPA symbols, and 17 of them are consonants"*, that is not an impression; it is the output of a set difference.

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

## Other ways in

- [Topic map](TOPICS.md): every page by subject.
- [Glossary](GLOSSARY.md): the terms, each with the page that explains it.
- [Resources](RESOURCES.md): the dictionaries and books behind the pages.
- [Roadmap](ROADMAP.md): what is written and what is deliberately not written yet.
- [Conventions](CONTRIBUTING.md): the house rules for adding a page.

<!-- --8<-- [end:below-hero] -->
