# How this repository was made (New Zealand)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| New Zealand Legislation (legislation.govt.nz), Parliamentary Counsel Office | <https://www.legislation.govt.nz> | 2026-10-29 | no copyright in legislation (Copyright Act 1994 s 27); other site content Crown copyright, CC BY |
| Internet Archive Wayback Machine | <https://web.archive.org/> | 2026-10-29 | Internet Archive terms of use; the legislation itself has no copyright (s 27) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution-act` | Constitution Act 1986 | 4 | 2005-05-17 to 2026-09-04 |
| `bill-of-rights-act` | New Zealand Bill of Rights Act 1990 | 3 | 1994-02-01 to 2022-08-30 |
| `privacy-act` | Privacy Act 2020 | 26 | 2020-12-09 to 2026-05-01 |
| `crimes-act` | Crimes Act 1961 | 58 | 2007-09-03 to 2026-08-08 |

The build made 112 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 98 | one law on its in-force day |
| 10 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 219 laws in the record.
- 181 tags.

## Dates

Each commit is dated at noon (Pacific/Auckland) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each change is dated by the in-force date the Parliamentary Counsel Office history note for the provision states ("Section 25: repealed, on 13 November 2025, by section 51 of the Parliament (Repeals and Amendments) Act 2025"); each version is the official consolidation as at its stated date (Legislation Act 2019, s 78). https://www.legislation.govt.nz

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `fa2dc877c2ffa67d58a7cb3a01598a503008d4556f7edbd177e6789fe8cf476e` (2429761 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

91 versions of 4 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English is built: New Zealand legislation is enacted in English (some Acts also have te reo Maori text, none in these acts).
- Versions are the official consolidations archived by the Internet Archive; consolidations that were not archived are missing, and their changes are dated by the history notes of the next archived one.
- "Compare" notes are kept as printed under each section; the PCO history notes and reprint notes are not law text and are left out of the files (they are used only to date and credit changes).
- Units: the long title, each section and each schedule; Part and cross headings are not separate files.
- A consolidation whose words equal the previous one (an older reprint relabelled by its reprint date) is not a version.
- Where one provision was changed on several dates between two archived consolidations, the first date reads "[The source does not give the text in force on this date.]" and the last date has the new words.
- A history note "editorial change made by the PCO" (Legislation Act 2019, subpart 2 of Part 3) credits the change to pco-editorial, a publisher entry, not to the Legislation Act 2019. The PCO editorial notes, the reprint notes and the site "secondary legislation" buttons inside provisions are not law text and are dropped.
- Orders in Council and other secondary legislation named in history notes are laws of kind decree, keyed sl-<year>-<number> (LI and SR citations likewise); Acts are keyed act-<year>-<number>.
- A capture of a "latest" page that a later capture contradicts by stating an earlier "as at" date is an older rendering of a consolidation the PCO re-issued, and is not used.
- Constitution Act 1986: the page stating "as at 2007-09-03" (archived 20110724) is an older rendering of the consolidation the PCO later re-issued as "as at 2005-05-17" (archived 20250216); only the re-issue is used.
- New Zealand Bill of Rights Act 1990: the page stating "as at 2007-09-03" (archived 20110410) is an older rendering of the consolidation the PCO later re-issued as "as at 1994-02-01" (archived 20130506); only the re-issue is used.
- Privacy Act 2020 came into force on 2020-12-01, except subpart 2 of Part 3 and ss 213-215, in force the day after Royal assent (s 2); the PCO consolidations archived for earlier dates (2020-08-07) and the as-enacted pages show text not yet in force, so the history starts with the first archived consolidation on or after 2020-12-01.
- Pages used for constitution-act: as at 2005-05-17 from https://www.legislation.govt.nz/act/public/1986/0114/latest/whole.html (capture 20250216094023); as at 2025-11-13 from https://www.legislation.govt.nz/act/public/1986/114/en/latest/ (capture 20260714164843); as at 2026-09-04 from https://legislation.govt.nz/act/public/1986/114/en/latest/ (capture 20261005094648)
- Pages used for bill-of-rights-act: as at 1994-02-01 from http://www.legislation.govt.nz/act/public/1990/0109/latest/whole.html (capture 20130506161514); as at 2013-07-01 from https://www.legislation.govt.nz/act/public/1990/0109/latest/whole.html (capture 20220911064208); as at 2022-08-30 from https://legislation.govt.nz/act/public/1990/109/en/latest/ (capture 20261005094754)
- Pages used for privacy-act: as at 2020-12-09 from https://legislation.govt.nz/act/public/2020/0031/latest/whole.html?search=ts_act%40bill%40regulation%40deemedreg_privacy+act+2020_resel_25_a&p=1 (capture 20210227064807); as at 2021-04-01 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20210806181120); as at 2021-10-08 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20211215213819); as at 2021-10-28 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20220211170818); as at 2022-04-12 from https://legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20220517101308); as at 2022-06-17 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html?search=qs_act%40bill%40regulation%40deemedreg_privacy+act+2020_resel_25_h&p=1 (capture 20220707104712); as at 2022-09-01 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20221104232129); as at 2022-11-15 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20221123220427); as at 2022-11-30 from https://legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20230407015612); as at 2023-04-20 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20230626191620); as at 2023-07-01 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20230918193807); as at 2023-12-06 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html?search=sw_096be8ed81e0475e_defendant_25_se&p=1 (capture 20240313072107); as at 2024-06-06 from https://legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20240624234257); as at 2024-07-01 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html (capture 20241108212031); as at 2025-01-26 from https://legislation.govt.nz/act/public/2020/0031/latest/whole.html?search=ts_act%40bill%40regulation%40deemedreg_Privacy+Act+2020_resel_25_a&p=1%2f (capture 20250405053304); as at 2025-03-30 from https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html?search=ta_act_P_ac%40ainf%40anif_an%40bn%40rn_25_a&p=3 (capture 20250502075814); as at 2025-11-27 from https://www.legislation.govt.nz/act/public/2020/31/en/latest/ (capture 20260327145751); as at 2026-05-01 from https://www.legislation.govt.nz/act/public/2020/31/en/latest/ (capture 20260926101200)
- Pages used for crimes-act: as at 2007-09-03 from https://www.legislation.govt.nz/act/public/1961/0043/1.0/whole.html (capture 20240615042147); as at 2008-10-01 from http://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20081021013158); as at 2008-12-25 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20090321093136); as at 2009-12-08 from http://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html?search=ts_act_building+act_resel (capture 20100524054038); as at 2010-06-01 from http://www.legislation.govt.nz:80/act/public/1961/0043/51.0/whole.html (capture 20200105174126); as at 2011-07-01 from http://legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20110724195927); as at 2011-07-13 from http://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20120119031219); as at 2012-02-13 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20120224140207); as at 2012-03-19 from http://legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20120403145405); as at 2012-04-18 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20121024115201); as at 2012-10-01 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20130518094059); as at 2013-07-01 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20130720225602); as at 2013-08-05 from http://legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20130824180047); as at 2013-08-19 from http://legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20140426042855); as at 2014-05-11 from http://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html?search=qs_act_burglary (capture 20141209233532); as at 2014-12-12 from http://legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20150109011817); as at 2014-12-15 from http://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20150427091818); as at 2015-05-07 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20150515014511); as at 2015-07-03 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20151021125734); as at 2015-11-07 from http://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20170308204736); as at 2017-03-01 from http://legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20170730145251); as at 2017-07-14 from http://legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20171002054536); as at 2017-09-28 from http://legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20181107210323); as at 2018-11-13 from http://legislation.govt.nz/act/public/1961/0043/140.0/whole.html (capture 20190214010001); as at 2018-12-03 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20190313205506); as at 2019-03-12 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20190623212239); as at 2019-07-01 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20200327071143); as at 2020-03-24 from http://www.legislation.govt.nz:80/act/public/1961/0043/latest/whole.html (capture 20200625215803); as at 2020-07-01 from http://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20200804045342); as at 2020-08-26 from https://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20210914184022); as at 2021-10-05 from https://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20211119004415); as at 2021-11-06 from https://legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20230411142023); as at 2023-04-13 from https://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20241005224619); as at 2024-10-01 from https://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html (capture 20250303093521); as at 2025-03-14 from https://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html?ref=kannz.com (capture 20250424161720); as at 2025-04-05 from https://www.legislation.govt.nz/act/public/1961/0043/latest/whole.html?search=ts_act_crimes+act (capture 20250515233108); as at 2025-11-27 from https://www.legislation.govt.nz/act/public/1961/43/en/latest/ (capture 20260325103537); as at 2026-05-26 from https://www.legislation.govt.nz/act/public/1961/43/en/latest/ (capture 20260714171221); as at 2026-08-08 from https://www.legislation.govt.nz/act/public/1961/43/en/latest/ (capture 20260926101512)

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Opus 5.5 (claude-opus-5-5) wrote Lexifina's code and chose the sources; it did not write or alter any legal text. The code is deterministic and runs no model; every line of law comes from an archived official page.
