# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Academic lab website for the Brown Lab at the University of Toronto, built with Jekyll on the
[sbryngelson/academic-website-template](https://github.com/sbryngelson/academic-website-template) (a fork of al-folio
style templates). Deployed to GitHub Pages at brown-lab-uoft.github.io.

## Commands

```bash
bundle install              # install Ruby/Jekyll deps (first time / after Gemfile changes)
bundle exec jekyll serve    # local dev server with live reload, http://localhost:4000
bundle exec jekyll build    # production build -> _site/

npm install                 # install JS deps (only needed if editing assets/js)
npm run build:js            # bundle+minify assets/js/site.js -> assets/js/site.min.js (esbuild)

python scripts/fetch_orcid.py   # regenerate assets/ref.bib from ORCID/CrossRef (needs `requests`)
```

There is no test suite or linter configured. Verify changes by running `bundle exec jekyll build`
(fails loudly on Liquid/YAML errors) and `bundle exec jekyll serve` to visually check pages.

## Architecture

**Content lives in data files, not templates.** Most pages (`_pages/about.md`, `_pages/team.md`, etc.)
are thin Liquid templates that loop over YAML in `_data/` — editing lab content almost always means
editing a `_data/*.yml` file, not the page template:

- `_config.yml` — PI identity (name/title/photo/links/email), site-wide settings, nav pages, and the
  `jekyll-scholar` config (bibliography source/formatting).
- `_data/pi.yml` — PI education list (long form on About, short form in sidebar).
- `_data/team_members.yml` — current students/postdocs shown on the Team page.
- `_data/alumni.yml`, `_data/people.yml` — past members / mentees, grouped by category.
- `_data/grants.yml`, `_data/awards.yml`, `_data/funders.yml` — About page sections.
- `_data/news.yml` — news items shown on the News/home pages.
- `assets/ref.bib` — publications in BibTeX, rendered by jekyll-scholar. **Auto-updated weekly** by
  `.github/workflows/update-publications.yml` via `scripts/fetch_orcid.py`, which pulls works from the
  ORCID API and BibTeX from CrossRef. Manual edits to `ref.bib` can be overwritten by that workflow.

**Layouts** (`_layouts/`) define page chrome: `default.html` is the base, `page.html`/`gridlay.html`/
`textlay.html`/`piclay.html` are content layouts a page's front matter selects via `layout:`,
`publications.html` renders the bibliography, `bibtemplate.html` formats individual citations
(citation style is `citesty.csl`).

**Includes** (`_includes/`) hold shared fragments: `header.html`/`sidebar.html`/`footer.html` for
navigation/chrome, `csv_to_table.html` for rendering CSV data tables, `mathjax.html`/`analytics.html`
for opt-in features toggled from `_config.yml`.

**Styling**: SCSS in `_sass/` (Bootstrap 5 + custom components/layouts/utilities), compiled by Jekyll's
built-in Sass support from `assets/main.scss`. `accent_color` and `dark_mode` in `_config.yml` drive
theme variables — prefer changing those over hand-editing colors in SCSS.

**JS**: `assets/js/site.js` is the source; `npm run build:js` produces the minified
`assets/js/site.min.js` that pages actually load. Edit the former, rebuild, don't hand-edit the `.min.js`.

## Deployment

`.github/workflows/deploy.yml` builds with Jekyll and deploys to GitHub Pages on every push to `main`
(no separate staging environment — pushes to `main` go live). `.github/workflows/update-publications.yml`
runs weekly (and on manual dispatch) to refresh `assets/ref.bib` from ORCID and commits directly to `main`
with `[skip ci]`... except that commit still triggers `deploy.yml` since that workflow has no path filter.
