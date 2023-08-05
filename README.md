# Collaborative Intelligence Systems Lab Website

This is the website repo of [Collaboative Intelligence Systems Lab (CISL)](https://cisl.ucr.edu/) at the 
University of California, Riverside.

## New member
Please add an entry to [/_data/team.yml](https://github.com/UCR-CISL/UCR-CISL.github.io/blob/main/_data/team.yml). Use existing member entry as references.

## New publication
Please add a bibtex entry to [/assets/pubication.bib](https://github.com/UCR-CISL/UCR-CISL.github.io/blob/main/assets/publications.bib). Use existing bibtex entry as references. 

*Note: there are a few special items added to bibtex entry that only this website recognizes, such as for thumbnail images, project website, github links, etc. Please see the [publication page](https://cisl.ucr.edu/publication/) and their corresponding bibtex entry for examples.*

Run compilation script to update [/_data/pub.yml](https://github.com/UCR-CISL/UCR-CISL.github.io/blob/main/_data/pub.yml). (Run ```pip install bibtexparser``` if not already)
```python
python3 ./assets/bib2yml.py --bibtex_fp ./assets/publication.bib
```
*Note: Do not edit pub.yml directly as the compilation script will overwrite it.*

Lastly, add a recent news entry to the [home page](https://github.com/UCR-CISL/UCR-CISL.github.io/blob/main/index.md) to share the good news!

## Preview website
```shell
bundle update 
bundle exec jekyll serve
```
## Publish website
Commit and push changes to this repo. That's all!

Copyright CISL@UCR
