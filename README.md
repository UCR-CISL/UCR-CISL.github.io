# Collaborative Intelligence Systems Lab Website

Website of the [Collaborative Intelligence Systems Lab (CISL)](https://cisl.ucr.edu/) at UC Riverside.

## Adding a new member

Edit [`assets/team.bib`](assets/team.bib). Add a `@member` entry using an existing entry as reference.

Key fields:
- `title` — full name
- `note` — department (e.g. `ECE`, `CSE`) and optionally `, co-advised with Dr. X`
- `year` / `month` — start date (used for sorting)
- `addendum` — end date: `pres.` for active members, or a date string like `Summer 2025` for alumni
- `webtype` — controls which section the person appears in: `PI` / `PHD` / `MS` / `BS` / `Visitor`
- `avatar`, `email`, `web`, `github`, `linkedin`, `gscholar` — optional profile fields
- `next` — next position (alumni only)

On push, a GitHub Action runs [`assets/bib2yml_team.py`](assets/bib2yml_team.py) to regenerate `_data/team_auto.yml`. **Do not edit `team_auto.yml` directly.**

## Adding a publication

Edit [`assets/publications.bib`](assets/publications.bib). Use an existing entry as reference.

Special bibtex fields recognized by this site (thumbnail image, project page, GitHub link, etc.) are documented in the existing entries and on the [publications page](https://cisl.ucr.edu/publication/).

On push, a GitHub Action runs [`assets/bib2yml.py`](assets/bib2yml.py) to regenerate `_data/pub_auto.yml`. **Do not edit `pub_auto.yml` directly.**

After adding a publication, add a news entry to `_data/news.yml`.

## Adding a teaching entry

Edit [`assets/teaching.bib`](assets/teaching.bib). On push, a GitHub Action runs [`assets/bib2yml_teaching.py`](assets/bib2yml_teaching.py) to regenerate `_data/teaching_auto.yml`.

## Preview locally

```shell
bundle update
bundle exec jekyll serve
```

## GitHub Actions

| Workflow | Trigger | Effect |
|---|---|---|
| `update_team.yml` | push to `assets/team.bib` | Regenerates `_data/team_auto.yml` |
| `update_pub.yml` | push to `assets/publications.bib` | Regenerates `_data/pub_auto.yml` |
| `update_teaching.yml` | push to `assets/teaching.bib` | Regenerates `_data/teaching_auto.yml` |

Copyright CISL@UCR
