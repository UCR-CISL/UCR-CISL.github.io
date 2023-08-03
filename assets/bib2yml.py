import os
import argparse
import bibtexparser
import yaml
from tqdm import tqdm

paper_dir = 'papers'
output_dir = './_data/pub.yml'

booktitle_series_map = {
    "International Conference on Learning Representations": "ICLR",
    "IEEE Transactions on Robotics": "TOR",
    "Conference on Robot Learning": "CoRL",
    "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition": "CVPR",
    "Proceedings of the IEEE conference on Computer Vision and Pattern Recognition": "CVPR",
    "Proceedings of the European Conference on Computer Vision (ECCV) Workshops": "ECCV",
    "European conference on computer vision": "ECCV",
    "Robotics: Science and Systems": "RSS",
    "Advances in Neural Information Processing Systems": "NIPS",
    "Proceedings of the IEEE International Conference on Computer Vision": "ICCV",
    "Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.": "IMWUT",
    "IEEE Communications Magazine": "CommMag",
    "IEEE Transactions on Vehicular Technology": "TVT",
    "The Journal of Defense Modeling and Simulation": "JDMS",
}

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
        conf = conf.split('\'')[0].strip()

        bibdb['conf'] = conf

        # print(bibdb['author'])
        bibdb = bibtexparser.customization.author(bibdb)
        # print(bibdb['author'])
        author_field = ""
        prev_author_field = bibdb['author']
        for j in range(len(prev_author_field)-1):
            author = prev_author_field[j]
            author_field += author.split(', ')[1] + " "  + author.split(',')[0] + ", "
        author_field += prev_author_field[-1].split(', ')[1] + " " + prev_author_field[-1].split(',')[0]
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




def add_new_articles_from_tex_file(tex_fp):
    bibfile = open(tex_fp)
    bibdb = bibtexparser.load(bibfile)
    add_new_articles(bibdb.entries)
    bibfile.close()

def add_new_articles_from_tex_string(tex_string):
    bibdb = bibtexparser.loads(tex_string)
    add_new_articles(bibdb.entries)

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
        bibdb = bibtexparser.loads(bibtex)
        add_new_articles(bibdb.entries)