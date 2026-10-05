# Lessons learned

Pitfalls met in earlier sessions. Check here before repeating an approach.

- **Dictionary sites are blocked in cloud sessions** (Oxford Learner's, Larousse, Le Robert, Wikipedia) by the environment's network policy. A session on the owner's iMac through `claude remote-control` can read them, with `curl` from the shell when the web-fetch tool is refused. From the cloud, write from memory and say so.
- **Nasal vowels are two code points** (vowel plus combining tilde U+0303). Normalise to NFD before counting or splitting a transcription, and match longest symbol first so that /ɑ̃/, /dʒ/ and /əʊ/ stay whole.
- **Oxford's key has 46 symbols, not 44**: it adds the weak /i/ of *happy* and /u/ of *situation*. A 44-phoneme inventory marks the last vowel of *lazy* as unknown.
- **The site builds from `master`** here, as in the math library; the learning-to-learn library uses `main`. Check before copying a workflow across.
