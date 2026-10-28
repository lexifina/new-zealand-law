"""Checks corpus.json against the official text, per act, and writes verification.json.

1. The newest archived `latest` page of the act (the current official consolidation when it was captured) must state
   the same "as at" date as the act's last version (or the last version comes from that page, dated by a PCO note
   after its "as at" day and no later than its capture), and no archived page may state a later date.
2. The act replayed version by version from corpus.json must equal that newest page, unit by unit, exactly (after
   the same typesetting normalisation parse.py applies).
3. Every version must come from a cached source whose sha256 matches.

    python -X utf8 verify.py [corpus.json]
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import parse

HERE = Path(__file__).resolve().parent


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'corpus.json'
    corpus = json.loads(path.read_text(encoding='utf-8'))
    caps = json.loads((HERE / 'captures.json').read_text(encoding='utf-8'))
    out = {}
    for a in corpus['acts']:
        state, before = {}, {}
        for v in a['versions']:
            before = dict(state)
            raw = parse.cache_path(v['source_url']).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == v['sha256'], v['source_url']
            if 'units' in v:
                state = dict(v['units'])
            for k, u in (v.get('changes') or {}).items():
                if u is None:
                    state.pop(k, None)
                else:
                    state[k] = u
        last = a['versions'][-1]['from']
        rows = [c for c in caps[a['slug']] if c.get('as_at')]
        newest = max((c for c in rows if c['kind'].endswith('latest')), key=lambda c: c['timestamp'])
        latest_date = max(c['as_at'] for c in rows)
        parsed = parse.parse_page(parse.cache_path(
            f'https://web.archive.org/web/{newest["timestamp"]}id_/{newest["url"]}').read_bytes(),
            parse.lt_notes_for(a['slug']))
        page = parsed['units']
        # a repealed Act: its last version removes every provision on the day the newest page says the whole Act was
        # repealed; that page prints the last words in force, so it is compared with the version before the repeal
        repealed = None
        if not state and len(a['versions']) > 1:
            raw = parse.cache_path(f'https://web.archive.org/web/{newest["timestamp"]}id_/{newest["url"]}').read_bytes()
            note = parse.whole_repeal(raw, a['title'])
            evs = parse.note_events(note, (None, a['title'])) if note else []
            lv = a['versions'][-1]
            if (len(evs) == 1 and evs[0][0] == last and set(lv.get('changes') or {}) == set(before)
                    and all(c == [evs[0][1]] for c in lv['credits'].values()) and set(lv['credits']) == set(before)):
                repealed, state = note, before
        diff = sorted(k for k in set(page) | set(state)
                      if (page.get(k) or {}).get('text') != (state.get(k) or {}).get('text'))
        # a repealed Act whose repeal-day page also prints its last provisions as "[Repealed]" that day by the same law
        # (Judicature Act 1908 s 87): parse.py removes them in the repeal version itself, so they differ from the
        # version before only by that stub, with a note giving exactly that day and law
        same_day = []
        if repealed:
            law = a['versions'][-1]['credits'] and next(iter(a['versions'][-1]['credits'].values()))
            for k in diff:
                evs_k = [e for n in parsed['notes'].get(k, []) for e in parse.note_events(n, (None, a['title']))]
                if (k in page and k in state and page[k]['text'].endswith('\n[Repealed]\n')
                        and page[k]['text'].split('\n', 1)[0] == state[k]['text'].split('\n', 1)[0]
                        and any(e[0] == last and [e[1]] == law for e in evs_k)):
                    same_day.append(k)
            diff = [k for k in diff if k not in same_day]
        # a reused section number (s 63 and s 63-2): parse.py keeps each provision under its earlier key, so within
        # such a group the same provisions may sit under swapped keys; the group must hold the same texts
        for ks in parsed.get('dups', {}).values():
            if sorted(page[k]['text'] for k in ks) == sorted((state.get(k) or {}).get('text', '') for k in ks):
                diff = [k for k in diff if k not in ks]
        # the newest page may already show a PCO change its note dates after the page's own "as at" day: parse.py then
        # ends the act with a version on that day, from that page, no later than the day it was captured
        cap_day = f'{newest["timestamp"][:4]}-{newest["timestamp"][4:6]}-{newest["timestamp"][6:8]}'
        src = f'https://web.archive.org/web/{newest["timestamp"]}id_/{newest["url"]}'
        last_ok = last == newest['as_at'] or (newest['as_at'] < last <= cap_day
                                              and a['versions'][-1]['source_url'] == src)
        ok = last_ok and newest['as_at'] == latest_date and not diff
        out[a['slug']] = {'last_version': last, 'newest_capture': newest['timestamp'], 'newest_url': newest['url'],
                          'newest_states': newest['as_at'], 'units': len(state), 'unit_mismatches': diff, 'ok': ok}
        if repealed:
            out[a['slug']]['repealed'] = repealed
        if same_day:
            out[a['slug']]['repealed_on_the_day'] = same_day
        print(a['slug'], 'OK' if ok else 'FAIL', out[a['slug']])
    dest = HERE / ('verification.json' if path.name == 'corpus.json' else f'verification-{path.stem}.json')
    dest.write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
