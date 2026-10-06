# English and French in the IPA: one alphabet, two inventories

**Level:** 101 · for anyone who has opened a French dictionary and seen /ʁ/, /ɑ̃/ or /y/ for the first time

**One line:** The International Phonetic Alphabet (IPA) is one alphabet for every language, so a symbol means the same sound in an English dictionary and in a French one. What differs is which symbols each language needs: of Oxford's 46 English symbols and Le Robert's 36 French ones, only 21 are in both. A French transcription is recognised by its nasal tildes, its /y ø œ/ and its /ʁ/, and by having no stress marks at all; an English one by its stress marks, length marks, schwas and diphthongs.

## Why a learner needs this

A French dictionary gives every word in the IPA, between slashes: *chien* /ʃjɛ̃/, *rue* /ʁy/, *peur* /pœʁ/. Assimil and most course books do the same in their first lessons. The symbols look like a secret code, but they are the same code an English dictionary uses, so anyone who can read /ðə ˈkwɪk ˈbraʊn ˈfɒks/ already knows most of it. What is left to learn is short: the symbols French has that English lacks, which are exactly the sounds an English speaker has to learn to make, and the symbols English has that French lacks, which are exactly the sounds a French speaker struggles with in English.

## The same symbols, the same sounds

The two languages share 21 symbols, and in each of them the symbol means the same thing:

- **Most consonants:** /p b t d k ɡ f v s z m n l/, and /ʃ ʒ/ as in English *ship, measure* and French *chat, jour*. The glides /w j/ are the same in *we, yes* and *oui, yeux*.
- **Three vowels:** /i/ (*see*, *si*), /u/ (*too*, *tout*) and /e/, which English uses in *bed* and French in *été*. Oxford writes English *bed* as /e/; many other dictionaries write it /ɛ/, the open sound of French *père*, and the English vowel sits between the two.
- **The schwa /ə/**, with a difference in use explained below.

## What French has that English does not

| Symbols | French examples | What an English speaker must learn |
|---|---|---|
| /ɑ̃ ɛ̃ ɔ̃ œ̃/ | *dans, vin, bon, brun* | The four nasal vowels. The tilde means the air goes through the nose. English has no nasal vowel phoneme, so an English transcription never carries a tilde. |
| /y ø œ/ | *tu, peu, peur* | The front rounded vowels: the tongue as for /i e ɛ/, the lips as for /u o ɔ/. This is why *tu* and *tout* are hard to tell apart at first. |
| /ʁ/ | *rue, Paris* | The French r, made at the back of the throat. The English r is /ɹ/, made with the tongue tip, though dictionaries write it /r/ for simplicity. |
| /ɥ/ | *huit, lui* | A glide made with the lips rounded as for /y/. English has nothing like it. |
| /ɲ/ | *agneau, montagne* | The *gn* sound, close to English *canyon* said quickly. |
| /a ɑ o ɔ ɛ/ on their own | *patte, pâte, eau, porte, père* | Pure vowels that English uses only inside diphthongs, if at all. Most speakers today merge /a/ and /ɑ/. |

## What English has that French does not

| Symbols | English examples | What a French speaker must learn |
|---|---|---|
| /θ ð/ | *thin, this* | The two *th* sounds. French has neither, which is why *the* comes out as *ze*. |
| /h/ | *house* | French spells *h* but never pronounces it. |
| /ŋ/ | *sing* | French has it only in borrowed words such as *parking*. |
| /æ ʌ ɒ ɪ ʊ/ | *cat, cup, dog, sit, put* | The lax short vowels. French vowels are all tense, so these fall together with the nearest French vowel: *ship* and *sheep* both become /ʃip/. |
| /iː ɑː ɔː uː ɜː/ | *see, car, saw, too, bird* | Length is distinctive in English and marked with ː. French has no length distinction, so a French transcription has no ː. |
| /eɪ aɪ ɔɪ əʊ aʊ/ | *day, my, boy, go, now* | Diphthongs, one vowel gliding into another. French vowels are pure, so a transcription like /əʊ/ never appears, and *gâteau* is /ɡɑto/, never /ɡætəʊ/. |
| /tʃ dʒ/ | *church, judge* | French has only the fricatives /ʃ ʒ/, so *jump* begins with /ʒ/ in a French mouth. |

## Three marks that give the language away before a vowel is read

**Stress.** English dictionaries put ˈ before the stressed syllable, and getting it wrong changes the word: *ˈrecord* the noun, *reˈcord* the verb. French stress always falls on the last syllable of a phrase and never distinguishes words, so French dictionaries leave the mark out entirely.

**Length.** The ː after a vowel appears in English transcriptions and not in French ones.

**The tilde.** The ̃ over a vowel appears in French transcriptions and never in English ones.

**And the schwa.** Both languages use /ə/, but for different things. In English it is the weak vowel of any unstressed syllable: *the, about, over*. In French it is the *e muet* of *le, petit, dessus*, a rounded sound close to /ø/, which is often dropped altogether in fast speech (*p'tit*).

## Two sentences, symbol by symbol

The program holds the two inventories as sets, after the pronunciation keys of Oxford Learner's Dictionaries and Le Robert, and reads two dictionary-style transcriptions through them:

- English, as Oxford Learner's gives each word: *The quick brown fox jumps over the lazy dog.*
- French, as Le Robert gives each word: *Le petit chien brun saute par-dessus la vieille clôture.*

For each symbol it says whether the other language has it, and it checks the three marks. Every English word was checked against the Oxford Learner's page for it; the French words follow Le Robert's key from memory, and the one uncertain point is *brun*, which Le Robert gives as /bʁœ̃/ while most speakers in France now say /bʁɛ̃/, the two nasal vowels having merged.

<!-- output:ipa_english_vs_french -->
*Verified output of [`ipa_english_vs_french.py`](examples/ipa_english_vs_french.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. The inventories as sets
English (RP) phonemes        46: aɪ aʊ b d dʒ e eə eɪ f h i iː j k l m n p r s t tʃ u uː v w z æ ð ŋ ɑː ɒ ɔɪ ɔː ə əʊ ɜː ɡ ɪ ɪə ʃ ʊ ʊə ʌ ʒ θ
French phonemes              36: a b d e f i j k l m n o p s t u v w y z ø œ œ̃ ɑ ɑ̃ ɔ ɔ̃ ə ɛ ɛ̃ ɡ ɥ ɲ ʁ ʃ ʒ
in both                      21: b d e f i j k l m n p s t u v w z ə ɡ ʃ ʒ
English only                 25: aɪ aʊ dʒ eə eɪ h iː r tʃ uː æ ð ŋ ɑː ɒ ɔɪ ɔː əʊ ɜː ɪ ɪə ʊ ʊə ʌ θ
French only                  15: a o y ø œ œ̃ ɑ ɑ̃ ɔ ɔ̃ ɛ ɛ̃ ɥ ɲ ʁ

2. The marks that give the language away
   English  stress marks 2  length marks 0  nasal tildes 0
   French   stress marks 0  length marks 0  nasal tildes 2

3. Each sentence, symbol by symbol
   English: The quick brown fox jumps over the lazy dog.
   /ðə kwɪk braʊn fɒks dʒʌmps ˈəʊvə ðə ˈleɪzi dɒɡ/
   31 symbols, 24 distinct
     shared with the other   15: b d f i k l m n p s v w z ə ɡ
     English only             9: aʊ dʒ eɪ r ð ɒ əʊ ɪ ʌ
     not in the inventory       0: -

   French: Le petit chien brun saute par-dessus la vieille clôture.
   /lə pəti ʃjɛ̃ bʁœ̃ sot paʁdəsy la vjɛj klotyʁ/
   34 symbols, 19 distinct
     shared with the other   12: b d i j k l p s t v ə ʃ
     French only              7: a o y œ̃ ɛ ɛ̃ ʁ
     not in the inventory       0: -

4. Checks
   every English symbol is an English phoneme: True
   every French symbol is a French phoneme:    True
   the English line has a stress mark:         True
   the French line has no stress mark:         True
   the French line has a nasal vowel:          True
   the English line has no nasal vowel:        True
   the English line has a diphthong:           True
   the French line has none:                   True
```
<!-- /output -->

Three things to read off the output:

1. **The shared symbols are the consonants.** Of the 21 symbols in both inventories, 17 are consonants and glides. Almost all the work of learning the other language's sounds is in the vowels.
2. **French has 15 symbols of its own and English 25**, so French has the smaller inventory, yet the French sentence uses a French-only symbol in nearly every word. The two sets are different in kind, not just in size.
3. **The marks alone identify the language.** Two stress marks and no tilde: English. Two tildes and no stress mark: French. A reader can tell which dictionary a line came from without reading a single vowel.

## A dialogue from Assimil, read in IPA

The owner's course book, Assimil's *French with Ease*, marks liaison with ‿ in its early dialogues. Here is one, *Au magasin*, transcribed line by line. The transcription follows Le Robert's key from memory and is not checked against a dictionary.

| French | IPA |
|---|---|
| S'il vous plaît, madame, est-ce qu'il est cher, ce chapeau ? | /sil vu plɛ madam, ɛs kil ɛ ʃɛʁ, sə ʃapo/ |
| Non, il n'est pas cher. Le prix est très raisonnable. | /nɔ̃, il nɛ pa ʃɛʁ. lə pʁi ɛ tʁɛ ʁɛzɔnabl/ |
| Bon. Et... Où sont les gants ? | /bɔ̃. e... u sɔ̃ le ɡɑ̃/ |
| Les gants sont là-bas. Vous voyez ? | /le ɡɑ̃ sɔ̃ laba. vu vwaje/ |
| Ah, merci... Mais, est-ce qu'ils sont‿en laine ? | /a, mɛʁsi... mɛ, ɛs kil sɔ̃t‿ɑ̃ lɛn/ |
| Non, ils ne sont pas‿en laine, ils sont‿en acrylique. | /nɔ̃, il nə sɔ̃ paz‿ɑ̃ lɛn, il sɔ̃t‿ɑ̃n‿akʁilik/ |
| Bon. Euh... est-ce qu'il est cinq heures ? | /bɔ̃. ø... ɛs kil ɛ sɛ̃k‿œʁ/ |
| Comment ? Ah, je comprends, vous‿attendez votre mari ! | /kɔmɑ̃? a, ʒə kɔ̃pʁɑ̃, vuz‿atɑ̃de vɔtʁ maʁi/ |

What the dialogue adds to the two sentences above:

- **Liaison.** The ‿ marks a consonant that exists only before a vowel: *sont‿en* gives /t/, *pas‿en* and *vous‿attendez* give /z/ (a written *s* becomes /z/ in liaison), *cinq‿heures* gives /k/. The book leaves *en acrylique* unmarked, but *en* before a vowel always liaises, /ɑ̃n‿akʁilik/. Liaison has its own rules, compulsory, optional and forbidden, and is a lesson of its own on the [roadmap](../../ROADMAP.md).
- **All four nasal vowels in a dozen lines:** /ɛ̃/ *magasin, cinq*; /ɔ̃/ *non, bon, sont, comprends*; /ɑ̃/ *gants, en, comment, attendez*; and /œ̃/ nowhere, which is typical of how rare it is.
- **Silent final letters:** *plaît, prix, est, gants, pas, bas, comprends, mari*, and the *-ez* of *attendez*, which is /e/. The *t* of *sont* and the *s* of *vous* come back only in liaison.
- **The e muet** in *ce, le, je, ne* is written /ə/ and often dropped in speech: *je comprends* is heard as /ʃkɔ̃pʁɑ̃/, the /ʒ/ devoicing against the /k/.
- **/ø/ in *euh*** is the hesitation vowel, the same as in *peu*. Its English counterpart *er* is /ɜː/, a sound French does not have.

## How to practise

1. **Read the IPA before the spelling** when you meet a new French word. French spelling hides the sound (*eau, au, o, ô* are all /o/); the transcription shows it.
2. **Learn the fifteen French-only symbols as sounds to make**, not as letters to recognise. Each one is a mouth position English never uses.
3. **When a word sounds wrong, look for the mark.** A missing nasal, a diphthong where a pure vowel belongs, or a stress on the wrong syllable are the three most common English accents in French, and each one is visible in the transcription.
4. **Check the key of the dictionary you use.** Oxford writes *bed* as /e/, others as /ɛ/; some French dictionaries no longer list /œ̃/ or /ɑ/. The sounds are the same; the house styles differ.

## Po polsku, w skrócie

Międzynarodowy alfabet fonetyczny (IPA) jest jeden dla wszystkich języków, więc ten sam znak oznacza ten sam dźwięk w słowniku angielskim i francuskim. Różnica polega na tym, których znaków dany język potrzebuje. Z 46 znaków angielskich u Oxforda i 36 francuskich u Le Roberta tylko 21 jest wspólnych, i są to prawie same spółgłoski.

Francuski ma to, czego angielski nie ma: cztery samogłoski nosowe /ɑ̃ ɛ̃ ɔ̃ œ̃/ z tyldą (Polak zna takie dźwięki z „ą" i „ę"), samogłoski /y ø œ/ wymawiane z zaokrąglonymi ustami jak przy „u", ale z językiem jak przy „i" (polskie „u" w słowie „tu" to nie to samo), gardłowe /ʁ/ zamiast polskiego „r" i spółgłoskę /ɲ/, czyli polskie „ń". Angielski ma to, czego francuski nie ma: /θ ð/ jak w *thin, this*, /h/, krótkie luźne samogłoski /æ ʌ ɒ ɪ ʊ/, długie samogłoski z dwukropkiem i dyftongi /eɪ aɪ əʊ aʊ/.

Najszybciej poznać język po znakach, które nie są dźwiękami: angielska transkrypcja ma akcent ˈ przed sylabą akcentowaną i dwukropek długości; francuska nie ma akcentu wcale, bo akcent pada zawsze na ostatnią sylabę frazy, ma za to tyldy. Program trzyma oba zestawy znaków jako zbiory, wypisuje część wspólną i różnice, a potem czyta dwa zdania znak po znaku i sprawdza, że angielskie ma akcenty i dyftongi, a francuskie tyldy i ani jednego akcentu.

## Auf Deutsch: Stichwörter

Das IPA ist ein Alphabet für alle Sprachen; Englisch und Französisch teilen nur 21 Zeichen, fast nur Konsonanten, und eine französische Transkription erkennt man an Nasalvokalen, /y ø œ/, /ʁ/ und am fehlenden Betonungszeichen.

Lautschrift · Phoneminventar · Nasalvokal · gerundeter Vorderzungenvokal · Zäpfchen-R · Betonungszeichen · Längenzeichen · Diphthong · Schwa · Schnittmenge

## See also

- [Sounds](../README.md) — the chapter this lesson opens
- [Glossary](../../GLOSSARY.md) — the terms, each with the page that explains it
- [Sets ↗](https://masiarek.github.io/math-learning-library/04_Sets/) — the math library's chapter on the sets the program uses: intersection, difference, subset
- Oxford Learner's Dictionaries, pronunciation key, and the entries for *the, quick, brown, fox, jump, over, lazy, dog*, each read for this page
- Le Robert, *Dictionnaire de la langue française*, pronunciation key, from memory
- International Phonetic Association, *Handbook of the IPA* (Cambridge, 1999), the French and the English illustrations, from memory
