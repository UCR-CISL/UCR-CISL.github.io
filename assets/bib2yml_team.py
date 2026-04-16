"""
bib2yml_team.py

Converts team.bib -> _data/team_auto.yml for the Jekyll website.
Only @member entries that carry a 'webtype' field are included.

Department + co-advisor resolution (in priority order):
  1. Explicit 'department' field  → use as-is (visitor / PI entries).
  2. No 'department' field        → parse from 'note':
       note format: "DEPT"  or  "DEPT, co-advised with Dr. X"
       • everything before ", co-advised with" becomes department
       • "Dr. X" becomes coadvisor (unless an explicit 'coadvisor' field is set)
"""

import argparse
import re
import bibtexparser
from bibtexparser.bparser import BibTexParser
import yaml

OUTPUT_PATH = './_data/team_auto.yml'

bibparser = BibTexParser()
bibparser.ignore_nonstandard_types = False

_COADVISOR_RE = re.compile(r',\s*co-advised with (.+)$', re.IGNORECASE)
_YEAR_IN_ADDENDUM = re.compile(r'\b(\d{4})\b')


def _parse_note(note):
    """Return (dept, coadvisor) extracted from a note string."""
    note = note.strip()
    m = _COADVISOR_RE.search(note)
    if m:
        return note[:m.start()].strip(), m.group(1).strip()
    return note, None


def convert(bibtex_fp):
    with open(bibtex_fp) as f:
        db = bibtexparser.load(f, parser=bibparser)

    people = []
    for entry in db.entries:
        webtype = entry.get('webtype', '').strip()
        if not webtype:
            continue  # not a website entry

        person = {
            'name': entry['title'].strip(),
            'type': webtype,
        }

        # --- department + coadvisor -------------------------------------------
        explicit_dept = entry.get('department', '').strip()
        explicit_coadvisor = entry.get('coadvisor', '').strip()

        if explicit_dept:
            # Visitor / PI entries carry an explicit department field
            person['department'] = explicit_dept
            if explicit_coadvisor:
                person['coadvisor'] = explicit_coadvisor
        else:
            # PhD / MS / UG entries: parse from note
            note = entry.get('note', '').strip()
            dept, parsed_coadvisor = _parse_note(note)
            if dept:
                person['department'] = dept
            coadvisor = explicit_coadvisor or parsed_coadvisor
            if coadvisor:
                person['coadvisor'] = coadvisor

        # --- direct pass-through fields ---------------------------------------
        for field in ['avatar', 'email', 'web', 'github', 'linkedin',
                      'gscholar', 'twitter', 'facebook', 'next']:
            val = entry.get(field, '').strip()
            if val:
                person[field] = val

        # --- role (alumni / past visitors) ------------------------------------
        webrole = entry.get('webrole', '').strip()
        if webrole:
            person['role'] = webrole

        # --- year (alumni / past visitors only) -------------------------------
        # addendum holds the end date string (e.g. "Summer 2025"); parse the
        # 4-digit year from it.  webyear overrides when an explicit value is set.
        if webtype in ('Alumni', 'PastVisitor'):
            webyear = entry.get('webyear', '').strip()
            if webyear:
                person['year'] = int(webyear)
            else:
                addendum = entry.get('addendum', '').strip()
                m = _YEAR_IN_ADDENDUM.search(addendum)
                if m:
                    person['year'] = int(m.group(1))

        people.append(person)

    with open(OUTPUT_PATH, 'w') as f:
        yaml.dump(people, f, default_flow_style=False, allow_unicode=True)

    print(f"Written {len(people)} entries to {OUTPUT_PATH}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert team.bib to _data/team_auto.yml')
    parser.add_argument('--bibtex_fp', default='assets/team.bib',
                        help='path to team.bib')
    args = parser.parse_args()
    convert(args.bibtex_fp)
