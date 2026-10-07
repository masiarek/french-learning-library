# Conventions

House rules for writing a page here. Readers browsing lessons do not need this file; it is for whoever is about to add one.

## The shape of a lesson

```
01_Sounds/
  ipa_english_vs_french/
    README.md                            the lesson
    examples/
      ipa_english_vs_french.py           the program
      ipa_english_vs_french.out          its recorded output
```

One idea per folder. The folder name is the idea, in `lower_snake_case`, and it becomes a permanent URL, so name it for what it teaches, not for where it sits in the reading order.

## Program output is generated

A page never hand-types what a program prints. It marks the spot:

```
<!-- output:ipa_english_vs_french -->
<!-- /output -->
```

and `python3 tools/run_examples.py` fills it from a real run, checked against the recorded `.out` file. A new example has no answer key yet: run `python3 tools/run_examples.py --only <stem> --update` once, then the plain check. Stems are unique across the repository.

## Examples use only the standard library

Any reader with `python3` must be able to run any page. No `pip install`, ever. Output must be the same on every run: no clock, no randomness without a fixed seed, no network.

## Claims a program cannot check

How a sound is made, what a dictionary gives, whether a form is current: name the source (which dictionary, which book, which page) and say how sure the claim is. A verdict written from memory says so.

## The source chapters have no programs

`02_Yosser_teacher` and `03_Szypowska` are the owner's own courses, kept as tables. A lesson there is a page with the lesson's rules in a few bullets, one table, and an AI section at the end (notes on words and expressions, each word of the lesson in set phrases, the lesson's words in new sentences, new words, new exercises with answers, in the same table format), plus two Anki decks; no program, no output block. `tools/check_ipa.py` checks every transcription in those tables against Le Robert's inventory in CI.

## No summary sections

The sibling libraries end every page with a Polish summary and German keywords. This library does not: the owner had both removed from every page on 2026-10-07. A lesson page ends with its program's output and **See also**. Polish appears only where it is content, below the English in a lesson table.

## Links and navigation

- A link to a folder points at its `README.md`. A link to a sibling library is external and marked ↗.
- Every lesson has a place in [TOPICS.md](TOPICS.md); `mkdocs build --strict` fails if one is missing.
- Reading order inside a chapter lives in `NAV_ORDER` in `mkdocs_hooks.py`. Chapters themselves sort A to Z in the sidebar; never list them there.
- Every term the page introduces goes in [GLOSSARY.md](GLOSSARY.md) with a link back.

## Before every commit

```bash
python3 tools/run_examples.py --check
uv run --group docs mkdocs build --strict
```

Both are what CI runs.
