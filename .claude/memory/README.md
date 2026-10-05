# The second brain

Notes that every Claude session in this repository reads at the start and updates before it ends, so that what one session learns, the next one already knows. `CLAUDE.md` imports the short, always-needed files; the rest are read when the task touches them.

| File | Holds | Loaded |
|---|---|---|
| [owner.md](owner.md) | how the owner works and what they want from a session | always |
| [lessons_learned.md](lessons_learned.md) | mistakes and dead ends, so they are not repeated | always |
| [inbox.md](inbox.md) | ideas and follow-ups not done yet | always |
| [decisions.md](decisions.md) | dated log of decisions and preferences, with the reason | when a choice comes up |
| [sources.md](sources.md) | the books and notes behind the library, and where they are | when working from a source |

## Rules for writing here

- **This repository is public.** Write nothing private: no email addresses, no personal details beyond how the owner likes to work, no file contents from their drives, no secrets.
- **Durable facts only.** A preference, a decision, a pitfall, an open idea. Not a transcript, not a summary of the session.
- **One line per fact where possible**, dated `YYYY-MM-DD` in `decisions.md`.
- **Newest wins.** When a new fact contradicts an old one, change or delete the old one; don't keep both.
- **Keep the always-loaded files short** (about 40 lines each), because every session pays for them. Move what is rarely needed to `decisions.md` or `sources.md`.
- **Done items leave the inbox.** When an inbox idea is done, delete it, and log the result in `decisions.md` if it settled something.
