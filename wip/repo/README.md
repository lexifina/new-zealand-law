# New Zealand: law history in git

The law of New Zealand as a git history: one file per provision, one commit per Act on the day its change took effect, and the Act that made each change as the commit's author. `git blame` names the Act behind every line; `git log` lists every change to a section; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `nz/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution-act/` | Constitution Act 1986 | 4 | From the official consolidation as at 17 May 2005 to the one as at 4 September 2026 |
| `bill-of-rights-act/` | New Zealand Bill of Rights Act 1990 | 3 | From the consolidation as at 1 February 1994 to the one as at 30 August 2022, still current |

Every version is an **official consolidation** published by the Parliamentary Counsel Office (PCO) on [legislation.govt.nz](https://www.legislation.govt.nz). Under section 78 of the Legislation Act 2019, an electronic consolidation published there is an official version of the legislation, and each page says so in its notes. The per-act `README.md` in each folder lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did s 6 of the Constitution Act say on 1 July 2026? | `python tools/on.py 2026-07-01 constitution-act sec-006` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2026-07-01T23:59:59Z" main -- constitution-act/sec-006.md):constitution-act/sec-006.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2026-07-01T23:59:59Z" main -- constitution-act/sec-006.md; git show "$($r):constitution-act/sec-006.md"` |
| Which Act wrote each line of s 24 of the Bill of Rights? | `git blame bill-of-rights-act/sec-024.md` |
| Every change to s 18 of the Constitution Act, word by word | `git log -p --word-diff constitution-act/sec-018.md` |
| Every Act in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one Act changed | `git show law/act-2026-053` (tags `law/<key>`; the key is the Act's year and number, `act-2026-053` = 2026 No 53) |
| The whole Act on a date | `python tools/on.py 2015-01-01 bill-of-rights-act` |
| The Act on a version's in-force day | `git show constitution-act/2025-11-13` (tags `<act>/<in-force day>`) |

File names: `sec-003a.md` is section 3A, `sch-01.md` is Schedule 1, `long-title.md` is the long title. After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Pacific/Auckland, on the day the change took effect**. The day is in the `In-force:` trailer, which the tools read.
- **The day comes from the PCO's history note** for the provision, for example "Section 25: repealed, on 13 November 2025, by section 51 of the Parliament (Repeals and Amendments) Act 2025 (2025 No 63)". The PCO states the in-force day there, so no default commencement rule is applied.
- **Changes between two archived consolidations** are dated by the history notes of the later one. The Constitution Amendment Act 2026 changed ss 6 and 8 on 10 July 2026. No consolidation as at that day is archived, so that commit's words come from the consolidation as at 4 September 2026, whose notes date those two sections to 10 July.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- **Against today's text.** The newest archived page of each Act (captured 5 October 2026) is the current official consolidation. Replaying every version in this record gives that page exactly, provision by provision: all 38 files of the Constitution Act and all 32 of the Bill of Rights. `tools/verify.py` runs this check from the cache. No archived page states a later date.
- **Every version is a dated official source.** Each version names its source page (an Internet Archive capture of legislation.govt.nz, with the capture time in the address) and the sha256 of the bytes it was read from.
- Every version of every Act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the Act that made the change, with an e-mail address that cannot exist (`act-2026-053@legislation.govt.nz.invalid`), so `git blame` and `git log --author` name it. The committer is always Lexifina.

- **Credits come only from the source.** A provision is credited to the Act its history note names for a day between the two consolidations. A change that no note explains is committed separately by the publisher, labelled "unexplained". There is one: the PCO corrected "or." to "or" in s 22(b) of the Constitution Act between the consolidations as at 17 May 2005 and 13 November 2025.
- **The first commit of each Act** is "oldest version available", credited to the publisher. It is the oldest consolidation archived, not the Act as passed. The Acts that shaped that text, as its history notes name them, are listed in the commit.
- Blame credits whole lines (one subsection or paragraph per line). Use `git log -p --word-diff` to see exactly which words each Act changed.

## What it does not show

- **The Acts as passed, and the years before the oldest archived consolidation.** legislation.govt.nz started in 2008 with consolidations then current. The Constitution Act starts as at 17 May 2005, after the Constitution Amendment Acts of 1987, 1999 and 2005 and the other Acts its notes name. The Bill of Rights starts as at 1 February 1994, after the Human Rights Act 1993.
- **Consolidations nobody archived.** Only pages the Internet Archive captured are used. A change made between two archived consolidations is still dated by the later one's history notes. If a provision changed on two different days in that gap, the text in between is not given: the first day's file reads "[The source does not give the text in force on this date.]".
- **Older renderings.** Pages the PCO later re-issued are not versions. The Constitution page labelled "as at 03 September 2007" (archived 2009 to 2011) is the old reprint layout of the consolidation the PCO now publishes as "as at 17 May 2005", and the same holds for the Bill of Rights.
- **History notes and reprint notes** are not law text and are not in the files; they are used only to date and credit changes. "Compare" notes are kept as printed.
- **Part and cross headings** are not separate files.
- **Court rulings.** A declaration of inconsistency under the Bill of Rights changes no words, so it is not in this record.

## How it is built


No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | API or bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Internet Archive](https://web.archive.org/) | Web archive | the captures it holds | n/a | CDX API | Used: every page read is a pinned capture |
| [Common Crawl](https://commoncrawl.org) | Web archive | n/a | n/a | yes | Checked: holds no legislation.govt.nz pages |
| [NZLII](http://www.nzlii.org) | Legal information institute | no | no | no | Not used: not official, no dated versions |
| [legidiff](https://github.com/tonyandrewmeyer/legidiff) | Volunteer git history built from PCO XML | yes | partly | n/a | Prior art; not read, no text copied |
| [nz-statute-book](https://github.com/jonnonz1/nz-statute-book) | Volunteer git repo, one commit per consolidation | yes | partly | n/a | Prior art; not read, no text copied |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

"Under section 27 of the Copyright Act 1994, there is no copyright in New Zealand legislation, including in legislation published by the PCO on this website" ([legislation.govt.nz/copyright](https://www.legislation.govt.nz/copyright/)). All other content on the site is Crown copyright, licensed under a Creative Commons Attribution licence (CC BY). Source: New Zealand Legislation, Parliamentary Counsel Office, www.legislation.govt.nz. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.
