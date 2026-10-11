"""Build-time fixes that would otherwise cost a pinned plugin dependency.

Three jobs, all about finding your way around:

1. **Clean chapter labels.** MkDocs derives a section label from the folder name
   on disk, so `01_Sounds/` reads as "01 Sounds". The numeric prefix exists
   to set reading order in a file listing; it should not be visible in the nav.
   Only *prefixed* folders are relabelled — a lesson folder takes its label from
   its page's own H1, which is already written the way it should read.

2. **Order the sections.** `NAV_ORDER` states the intended reading order per
   folder, keyed by folder path, listing children by their on-disk name. At the
   top level the chapters are the exception: they sort by name, A to Z, wherever
   the `CHAPTERS` marker sits, because the owner looks a subject up by name. The
   numbers still give the suggested reading order, which Start Here spells out.
   Inside a chapter the lessons keep their reading order, because each chapter
   is one argument and its steps depend on the ones before.

3. **Keep the topic map complete.** `TOPICS.md` groups every lesson by subject.
   A lesson missing from it is logged as a warning, and `mkdocs build --strict`
   (what CI runs) fails on a warning, so a new lesson cannot ship without a
   place on the map. A chapter listed in `INDEXED_CHAPTERS` is a dictionary
   rather than an argument (one page per word, dozens of them): there the
   chapter's own `README.md` is the index, a page linked from it has its place,
   and `TOPICS.md` keeps one line for the chapter.

Why order here rather than by renaming files: a filename is a permanent URL.
Renumbering `03_` to `04_` to insert a lesson would move every page after it and
break any link anyone saved. Ordering is presentation, so it belongs in the
presentation layer. Unlisted pages keep their alphabetical slot at the bottom, so
adding a page needs no edit here.

One structural note that is easy to get wrong: the top-level object MkDocs hands
`on_nav` is a `Navigation`, whose children live on `.items`. Only `Section` has
`.children`. A hook that reaches for `.children` at the top level silently does
nothing at all — the build still succeeds, and the sidebar is simply never
touched.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

PREFIX = re.compile(r"^(\d+)[_-]")

# Where the numbered chapters go in the top-level order: all of them, A to Z by
# the name shown in the sidebar, so a new chapter needs no edit here.
CHAPTERS = "*chapters*"

# A lesson page: <numbered chapter>/<lesson>/README.md. Start Here is not one.
LESSON = re.compile(r"^(?!00_)\d+_[^/]+/[^/]+/README\.md$")
TOPIC_MAP = "TOPICS.md"
LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")

# Chapters whose own README.md indexes their pages, one line per word, so that
# TOPICS.md need not repeat the list: a page of such a chapter has its place
# when the chapter page links it.
INDEXED_CHAPTERS = {"05_1000_words", "06_Expressions"}

log = logging.getLogger("mkdocs.hooks.topic_map")

# Chapters whose sidebar label is not the title-cased folder name: a source
# chapter is named after the person or book it comes from, with a word of
# explanation in brackets, which a folder name cannot carry.
CHAPTER_LABELS = {
    "02_Yosser_teacher": "Yosser (teacher)",
    "03_Szypowska": "Szypowska (Polish material)",
    "05_1000_words": "1000 words",
}

# Words the naive title-caser gets wrong.
FIXUPS = {
    "Vs": "vs",
    "And": "and",
    "Or": "or",
    "The": "the",
    "To": "to",
    "A": "a",
    "In": "in",
    "Of": "of",
}

# Reading order per folder path. Children named by on-disk name; anything not
# listed sorts alphabetically after the listed ones.
NAV_ORDER: dict[str, list[str]] = {
    "": [
        "index.md",
        "00_Start_Here",
        "TOPICS.md",
        CHAPTERS,
        "GLOSSARY.md",
        "RESOURCES.md",
        "ROADMAP.md",
    ],
    # The sounds of French, written down: the alphabet the dictionaries use,
    # and what in it is French and what is not.
    "01_Sounds": [
        "README.md",
        "ipa_english_vs_french",
        "four_inventories",
        "french_alphabet",
        "homophones",
    ],
    # The owner's teacher's worksheets, one lesson each, in the order given.
    "02_Yosser_teacher": [
        "README.md",
        "lesson_01_la_maison",
        "lesson_01_lecture_ma_maison",
        "lesson_02_etre_avoir",
        "lesson_03_ou_est",
        "lesson_04_salutations",
    ],
    # Szypowska's Polish textbook of French, one page per lesson of the book,
    # in the book's order.
    "03_Szypowska": [
        "README.md",
        "lecon_03_regardons_des_photos",
        "lecon_04_chez_les_lefevre",
        "lecon_05_dialogue",
        "lecon_06_en_visite",
    ],
    # The pronunciation videos, one page each, in the order the owner sent them.
    "04_Pronunciation": [
        "README.md",
        "sons_an_on",
        "son_e_ouvert",
        "resources",
    ],
    # The thousand words of the owner's vocabulary app, one page per word. Only
    # the chapter page is listed: the word pages sort A to Z after it, as a
    # dictionary does, and the chapter page numbers them in order of arrival.
    "05_1000_words": [
        "README.md",
    ],
    # Whole phrases, one page each, indexed by the chapter page like the words.
    "06_Expressions": [
        "README.md",
    ],
}


def _label(name: str) -> str:
    """Folder name on disk -> sidebar label."""
    if name in CHAPTER_LABELS:
        return CHAPTER_LABELS[name]
    words = PREFIX.sub("", name).replace("_", " ").replace("-", " ").split()
    out = [FIXUPS.get(w.capitalize(), w.capitalize()) for w in words]
    if out:
        out[0] = out[0][0].upper() + out[0][1:]
    return " ".join(out)


def _is_section(item) -> bool:
    return getattr(item, "children", None) is not None


def _first_src(item) -> str:
    """Source path of `item`, or of the first page anywhere beneath it."""
    page_file = getattr(item, "file", None)
    if page_file is not None:
        return page_file.src_uri
    for child in getattr(item, "children", None) or []:
        found = _first_src(child)
        if found:
            return found
    return ""


def _on_disk_name(item, depth: int) -> str:
    """The name NAV_ORDER lists this child by: a filename, or a folder segment."""
    src = _first_src(item)
    if not src:
        return (getattr(item, "title", "") or "").lower()
    parts = src.split("/")
    if not _is_section(item):
        return parts[-1]
    return parts[depth] if depth < len(parts) - 1 else parts[-1]


def _order_key(path: str, name: str) -> tuple[int, str]:
    listed = NAV_ORDER.get(path, [])
    if name in listed:
        return (listed.index(name), "")
    if CHAPTERS in listed and PREFIX.match(name):
        return (listed.index(CHAPTERS), _label(name).lower())
    return (len(listed), name.lower())


def _readme_h1(section) -> str:
    """The H1 of a section's own README.md, read from disk ("" if it has none)."""
    for child in section.children:
        page_file = getattr(child, "file", None)
        if page_file is None or page_file.src_uri.rsplit("/", 1)[-1] != "README.md":
            continue
        with open(page_file.abs_src_path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("# "):
                    return line[2:].strip()
    return ""


def _visit(items: list, path: str, depth: int) -> None:
    for child in items:
        if not _is_section(child):
            continue
        name = _on_disk_name(child, depth)
        # A numbered chapter folder is relabelled from its name. A lesson folder
        # takes its page's H1, which is authored prose. Left alone, MkDocs titles
        # a section from its folder name, and that only looks right while the two
        # happen to agree: `fat_cantor_set` came out "Fat cantor set", losing the
        # capital on a proper noun and the article in the H1. Title-casing the
        # folder name instead would fight the page just as badly
        # ("Significant Figures").
        if PREFIX.match(name):
            child.title = _label(name)
        else:
            child.title = _readme_h1(child) or child.title

    items.sort(key=lambda c: _order_key(path, _on_disk_name(c, depth)))

    for child in items:
        if not _is_section(child):
            continue
        name = _on_disk_name(child, depth)
        _visit(child.children, f"{path}/{name}".lstrip("/"), depth + 1)


def on_nav(nav, config, files):
    """Relabel numbered chapters and apply NAV_ORDER, depth-first."""
    _visit(nav.items, "", 0)
    return nav


def on_files(files, config):
    """Warn about every lesson that TOPICS.md does not link to."""
    docs = Path(config["docs_dir"])
    topic_map = docs / TOPIC_MAP
    if not topic_map.exists():
        log.warning("%s is missing: it should list every lesson by subject", TOPIC_MAP)
        return files
    linked = {
        (topic_map.parent / target).resolve()
        for target in LINK.findall(topic_map.read_text(encoding="utf-8"))
    }
    for chapter in INDEXED_CHAPTERS:
        index = docs / chapter / "README.md"
        if index.exists():
            linked |= {
                (index.parent / target).resolve()
                for target in LINK.findall(index.read_text(encoding="utf-8"))
            }
    for page in files.documentation_pages():
        if LESSON.match(page.src_uri) and (docs / page.src_uri).resolve() not in linked:
            where = TOPIC_MAP
            if page.src_uri.split("/")[0] in INDEXED_CHAPTERS:
                where = f"{page.src_uri.split('/')[0]}/README.md or {TOPIC_MAP}"
            log.warning("%s has no place in %s; add it to the index", page.src_uri, where)
    return files
