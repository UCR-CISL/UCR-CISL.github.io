import os
import argparse
import bibtexparser
from bibtexparser.middlewares import SeparateCoAuthors, SplitNameParts
import yaml
from tqdm import tqdm

paper_dir = 'papers'
output_dir = './_data/pub_auto.yml'
venues_file = './_data/venues.yml'

def load_venues():
    if os.path.exists(venues_file):
        with open(venues_file, 'r') as f:
            mapping = yaml.safe_load(f)
            return mapping if mapping else {}
    print(f"Warning: venues file not found at {venues_file}, using empty mapping")
    return {}

booktitle_series_map = load_venues()

def add_new_articles(bibdbs):

    print("Adding {} articles".format(len(bibdbs)))

    yml = open(output_dir, 'w')
    output_lines = []
    bibdbs = sorted(bibdbs, key=lambda pub: pub['year'], reverse=True)
    for i in range(len(bibdbs)):
        bibdb = bibdbs[i]
        # print(bibdb)
        conf = ""
        if 'series' in bibdb:
            conf = bibdb['series']
        elif 'booktitle' in bibdb:
            conf = bibdb['booktitle']
        elif 'journal' in bibdb:
            conf = bibdb['journal']
        elif 'archiveprefix' in bibdb:
            conf = bibdb['archiveprefix']

        # print(conf)

        for conf_name in booktitle_series_map:
            if conf.lower() == conf_name.lower():
                conf = booktitle_series_map[conf_name]

        # conf = conf.split(' ')[0]
        # conf = conf.split('\'')[0].strip()

        bibdb['conf'] = conf

        # print(bibdb['author'])
        if 'author' in bibdb:
            names = bibdb['author']
            author_field = ", ".join(
                " ".join(name.first) + " " + " ".join(name.von + name.last)
                for name in names
            )
            bibdb['author'] = author_field
        # print(bibdb['author'])
        # output = yaml.dump(bibdb, default_flow_style=False)
        # print(output)
        # output_lines.append("-\n")
        # output_lines.append(output)

    f = open(output_dir, "w")
    # f.writelines(output_lines)
    yaml.dump(bibdbs, f, default_flow_style=False)
    f.close()




_PARSE_MIDDLEWARE = [SeparateCoAuthors(), SplitNameParts()]

def add_new_articles_from_tex_file(tex_fp):
    library = bibtexparser.parse_file(tex_fp, append_middleware=_PARSE_MIDDLEWARE)
    add_new_articles([dict(entry.items()) for entry in library.entries])

def add_new_articles_from_tex_string(tex_string):
    library = bibtexparser.parse_string(tex_string, append_middleware=_PARSE_MIDDLEWARE)
    add_new_articles([dict(entry.items()) for entry in library.entries])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bibtex_fp', default="tmp.bib", help='text from bibtex file')
    parser.add_argument('--bibtex', default=None, help='text from bibtex file')
    parser.add_argument('--bibname', default=None, help='bib name, default is none to reuse name from bibtxt')
    arguments = parser.parse_args()

    bibdb = None
    if arguments.bibtex is not None:
        add_new_articles_from_tex_string(arguments.bibtex)
    elif arguments.bibtex_fp is not None:
        add_new_articles_from_tex_file(arguments.bibtex_fp)
    else:
        print("Invalid bibtex text or bib file!")
        print("Entering dummy text file for texting")
        bibtex = "@inproceedings{sener2018active," \
                 "title={Active Learning for Convolutional Neural Networks: A Core-Set Approach}," \
                 "author={Ozan Sener and Silvio Savarese}," \
                 "booktitle={International Conference on Learning Representations}," \
                 "year={2018}," \
                 "url={https://openreview.net/forum?id=H1aIuk-RW},}"
        library = bibtexparser.parse_string(bibtex, append_middleware=_PARSE_MIDDLEWARE)
        add_new_articles([dict(entry.items()) for entry in library.entries])