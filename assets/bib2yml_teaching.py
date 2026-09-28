"""
bib2yml_teaching.py

Converts teaching.bib -> _data/teaching_auto.yml
Entries are sorted reverse-chronologically (year desc, month desc).
No author/conference processing — all fields are passed through as-is.
"""

import argparse
import bibtexparser
import yaml

OUTPUT_DIR = './_data/teaching_auto.yml'

MONTH_ORDER = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12,
}


def convert(bibtex_fp):
    library = bibtexparser.parse_file(bibtex_fp)
    entries = [dict(entry.items()) for entry in library.entries]

    # Sort reverse-chronologically: year desc, then month desc
    def sort_key(e):
        year = int(e.get('year', 0))
        month = MONTH_ORDER.get(e.get('month', '0'), 0)
        return (year, month)

    entries = sorted(entries, key=sort_key, reverse=True)

    # Drop internal bibtexparser keys and fields not useful for the website
    drop_keys = {'ENTRYTYPE', 'ID'}
    cleaned = []
    for e in entries:
        entry = {k: v for k, v in e.items() if k not in drop_keys}
        cleaned.append(entry)

    with open(OUTPUT_DIR, 'w') as f:
        yaml.dump(cleaned, f, default_flow_style=False, allow_unicode=True)

    print(f"Written {len(cleaned)} entries to {OUTPUT_DIR}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bibtex_fp', default='assets/teaching.bib',
                        help='path to teaching.bib')
    args = parser.parse_args()
    convert(args.bibtex_fp)
