# Collaborative Intelligence Systems Lab Website

This is the website repo of Collaboative Intelligence Systems Lab (CISL) at the 
University of California, Riverside.

Prerequisites
* bibtexparser

Commands
* Edit assets/publication.bib
```python
python3 ./assets/bib2yml.py --bibtex_fp ./assets/publication.bib
```

```shell
bundle update 
jekyll build
jekyll serve
``` 
publish the _site folder

Copyright CISL@UCR