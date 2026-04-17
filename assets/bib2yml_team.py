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

        # --- department + coadvisor (current student display) ----------------
        explicit_dept = entry.get('department', '').strip()
        note = entry.get('note', '').strip()

        if explicit_dept:
            # PI entry only
            person['department'] = explicit_dept
        else:
            # Parse dept and coadvisor from note (used by avatar_entry for current students)
            dept, parsed_coadvisor = _parse_note(note)
            if dept:
                person['department'] = dept
            coadvisor = parsed_coadvisor
            if coadvisor:
                person['coadvisor'] = coadvisor

        # --- note (alumni display) -------------------------------------------
        # Pass note through as-is so alumni_entry.html can display it directly.
        if note:
            person['note'] = note

        # --- direct pass-through fields ---------------------------------------
        for field in ['avatar', 'email', 'web', 'github', 'linkedin',
                      'gscholar', 'twitter', 'facebook', 'next']:
            val = entry.get(field, '').strip()
            if val:
                person[field] = val

        # --- current vs. past -------------------------------------------------
        # Inferred from addendum: "pres." means active, anything else means past.
        # PI has no addendum so is always treated as current.
        addendum = entry.get('addendum', '').strip()
        current = (addendum == 'pres.' or webtype == 'PI')
        person['current'] = current

        # --- year (past members only) -----------------------------------------
        # addendum holds the end date string (e.g. "Summer 2025"); parse the
        # 4-digit year from it.  webyear overrides when an explicit value is set.
        if not current:
            webyear = entry.get('webyear', '').strip()
            if webyear:
                person['year'] = int(webyear)
            else:
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
