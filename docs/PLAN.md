# Recommendation Memo — Track A vs. Track B

Date: 2026-09-22. Companion to [AUDIT.md](AUDIT.md) — read that first; this memo assumes its findings.

**Where to look to compare the tracks yourself**, before reading my recommendation:
- Track B's actual theme, live: **https://alshedivat.github.io/al-folio/** — this is the real demo, maintained by the
  theme author, not a screenshot.
- Track B's source: **https://github.com/alshedivat/al-folio**
- Track A's source: **https://github.com/sbryngelson/academic-website-template** — the template your current site is
  already built from, so your own site *is* the closest thing to a Track A "after" preview.

Everything below about al-folio's content model, gem dependencies, and deployment behavior is verified against that
repository's actual `Gemfile`, `package.json`, and README as of today — not recalled from general knowledge.

---

## Track A: Stay on Bryngelson, fix what's broken

This fixes every finding from the audit at the config/template level. Nothing here requires a new framework.

| # | Change | Files touched | Effort |
|---|---|---|---|
| 1 | Fix sitemap: remove `sitemap: false` from all 8 real content pages (keep it on 404, talks, teaching, software — see #7) | 8 files in `_pages/` | 10 min |
| 2 | Fix Person schema: `site.name` → `site.pi_name` in the JSON-LD block | `_includes/head.html` | 5 min |
| 3 | Delete stray demo content: 3 PDFs in `papers/`, 2 posts in `_posts/`, backing CSV in `_data/` | `papers/*.pdf`, `_posts/*.md`, `_data/great_mathematicians_and_physicists.csv` | 10 min |
| 4 | Install `jekyll-seo-tag`; replace hand-rolled `<head>` meta/OG/Twitter block with the plugin, keep your existing JSON-LD (the plugin doesn't cover Person/Organization) | `Gemfile`, `_config.yml`, `_includes/head.html` | 45 min |
| 5 | Add a `description` front-matter convention so each page gets its own meta description instead of the sitewide default | Every file in `_pages/`, `_includes/head.html` (or handled by #4's plugin via front matter) | 1–1.5 hr (writing 8 real descriptions + wiring) |
| 6 | Add `Organization` as a real top-level JSON-LD entity: University of Toronto + Leslie Dan Faculty of Pharmacy + Acceleration Consortium, each with `url`; reference it from `Person.affiliation` instead of the current bare stub | `_includes/head.html`, new fields in `_config.yml` | 45 min |
| 7 | Resolve the orphaned pages instead of leaving them live: either delete `teaching.md`/`software.md`/`talks.md` outright, or fill them with real content and add them to `nav_pages`. (Given your CV/talks aren't a current priority, I'd default to **delete** unless you tell me otherwise — dead template pages are worse than no page.) | `_pages/teaching.md`, `_pages/software.md`, `_pages/talks.md` | 15 min (delete) or 1–2 hr (populate) |
| 8 | Commission/build a real 1200×630 OG image, wire it as the default `og:image`/`twitter:image` with per-page override support | `_includes/head.html`, new asset | 15 min wiring + your time on the asset itself |
| 9 | `_config.yml`: add `lang: en-CA`, add an `author` block for `jekyll-seo-tag`, rewrite `description` with real target keywords (peptide drug discovery, AS-MS, self-driving labs, AMR, University of Toronto) | `_config.yml` | 20 min |
| 10 | Add `ScholarlyArticle` JSON-LD per publication — jekyll-scholar exposes entry fields to the `bibtemplate.html` layout, so this is a template addition, not a new plugin | `_layouts/bibtemplate.html` | 1–1.5 hr (BibTeX field mapping needs care) |
| 11 | Write `SEO.md` documenting the front-matter conventions (title/description/image) for future-you and students | new file | 30 min |

**Track A total: ~6–9 focused hours**, spread across the chunks above. Every item is independently committable and
buildable — you can stop after any row and be strictly better off than before.

### Design, same track (from the audit's "what's flattening it" list)
These aren't SEO but you asked for them under Track A too:

- **Team photos**: replace `rock.jpg` placeholders with real photos (or, if photos aren't available yet, a
  consistent neutral placeholder — silhouette or initials avatar — anything but the same literal rock five times). No
  code change, just asset replacement in `_data/team_members.yml`. **Your time, not mine** — I don't have photos of
  your students.
- **Homepage hero**: the `.banner-frame` component already exists, styled, in `_sass/layouts/_home.scss` and is
  unused. Adding one banner image (a lab photo, an instrument shot, an abstract peptide-structure render) to
  `home.md` uses a component you're already paying the CSS cost for. 15 min wiring once you have an image.
- **Type scale tokenization**: add `--font-size-*` custom properties to `_sass/base/_variables.scss` (16/18/24/32/48
  as you specified, or closer to your actual h1–h4 values to avoid a visual jump) and reference them from
  `_typography.scss` instead of hardcoded rem literals. Purely a maintainability improvement — nothing here fixes a
  visible bug, since the current single-file hardcoding isn't scattered. 30 min.
- **Leftover hardcoded colors**: replace `#fff` with `var(--bg-card)` (or a new `--on-accent` token) in
  `_buttons.scss`/`_chips.scss`; either theme the Stanford-red `.btn-arxiv`/`.btn-paper` to your teal accent or leave
  it — arXiv's own brand color is arguably correct to keep as-is for an arXiv-specific button, your call. 20 min.
- **Unused leftover assets** (`images/team/*.svg`, six unused `images/research/*.svg`): delete. 5 min.

Design total: **~1.5 hours of my time + however long it takes you to source photos/a hero image**, which is the
actual bottleneck, not code.

---

## Track B: Migrate to al-folio

### What carries over cleanly
- **Publications**: al-folio also uses `jekyll-scholar` against a BibTeX file. Your `assets/ref.bib` moves to
  `_bibliography/papers.bib` with no reformatting of the entries themselves — this is the one piece of content that's
  genuinely portable as-is.
- **Team/people data**: al-folio also reads `_data/` YAML for team info, similar shape to what you have now.

### What gets reformatted (real, mechanical work)
- **News**: your `_data/news.yml` (one array, one entry per item) becomes al-folio's `_news/` **collection** — one
  Markdown file per news item, each with its own front matter. Every existing entry needs to be split out into its
  own file. Same story for anything you'd want on al-folio's "projects" or "teaching" pages (`_projects/`,
  `_teachings/`) — collections, not YAML arrays.
- **CV**: al-folio's CV support goes through a dedicated plugin (`al_folio_cv`) expecting RenderCV or JSONResume
  format — a structured data format you don't currently have any content for, since you don't have a CV page at all
  today. Net-new work, not a migration.
- **All custom design**: the parchment/teal palette, Source Serif + DM Sans pairing, the tokenized spacing scale, the
  dark-mode implementation, the search overlay — none of it exists in al-folio. Al-folio has its own design system
  (its own Sass, its own dark-mode toggle, its own layout conventions). Getting your current look back inside al-folio
  means re-implementing the same design work Track A simply keeps, but now fighting a foreign theme's structure
  instead of your own.

### Real risks, verified against al-folio's actual repo
- **Gemfile weight and fragility**: al-folio's `Gemfile` currently declares **19 gems** against your current **9**.
  Several carry native, non-Ruby dependencies: `mini_racer` embeds a V8 JavaScript engine in the Ruby process,
  `jekyll-imagemagick` shells out to an installed ImageMagick binary, `jekyll-jupyter-notebook` expects a working
  Python/Jupyter install to render notebooks. None of these are things your lab site needs (you have no Jupyter
  notebooks, no need for server-side image processing beyond what you do manually today), but they're part of the
  base template and are exactly the kind of dependency that breaks in CI. This isn't hypothetical — searching
  al-folio's own GitHub issues turns up a recurring pattern: *"the github-pages gem can't satisfy your Gemfile's
  dependencies,"* *"deployment failure — no file matched to requirements.txt,"* and similar, specifically because of
  this heavier dependency surface.
- **This is a rebuild, not an upgrade**: al-folio's own README recommends starting via "Use this template" — a fresh
  repository — specifically so your changes don't tangle with upstream. There's no supported incremental-migration
  path from an unrelated Jekyll theme; you'd stand up a new site and port content in, not transform this repo in
  place.
- **URL/permalink drift**: your current permalinks (`/research/`, `/team/`, `/publications/`) are hand-set in front
  matter and can be preserved in al-folio too (it's still Jekyll), but al-folio's own conventions (e.g., `/news/`,
  `/repositories/`, `/teaching/` as auto-generated collection pages) differ enough that a careless migration breaks
  external links and anything Google has indexed so far — extra care required, not a blocker, but a real task.
- **Deploy pipeline**: not actually a new problem for you — your `deploy.yml` already runs a custom
  `bundle exec jekyll build` via GitHub Actions rather than the legacy native-Pages Jekyll processor, so al-folio's
  heavier Gemfile wouldn't hit the "Pages can't satisfy dependencies" failure mode specifically. It would, however,
  make your Actions build slower and more prone to breaking on gem/native-dependency upgrades over time.

### Effort estimate
Standing up a faithful al-folio site with your content, your permalinks preserved, and your current visual identity
rebuilt inside it: **20–40+ hours**, and that's before ongoing maintenance overhead from the heavier dependency
surface. This is not a "small number of focused sessions" scope — it's a project.

---

## Recommendation: Track A. Not close.

Three reasons, in order of weight:

1. **Every blocking and important finding in the audit is a config/template fix, independent of which theme you're
   on.** The sitemap bug, the wrong-entity Person schema, the duplicate meta description — none of these are
   symptoms of "wrong theme." They're bugs in your current `head.html` and front matter. Migrating to al-folio doesn't
   fix a single one of them for free; you'd still need to do the equivalent work, just inside an unfamiliar codebase.

2. **Your current design is not the liability you think it is.** The audit found a genuinely bespoke, tokenized,
   dark-mode-complete design system already in place. Al-folio would replace it with *its* design system — you'd be
   discarding working, already-customized CSS to adopt someone else's, then spending real hours pulling your palette
   and typography back into it. That's strictly more work than fixing the four or five things that are actually
   dragging the current design down (rock photos, no hero image, unmigrated demo pages).

3. **Al-folio's dependency surface buys you features you don't need at a fragility cost you don't want.** Jupyter
   notebook rendering, a Bayesian related-posts classifier, distill.pub-style posts — none of this is relevant to a
   two-person-plus-PI lab site whose job is to state clearly who you are and what the lab does. What you'd actually
   be buying is more Gemfile surface area to break in CI, which is precisely the "flag it if it complicates the
   build" scenario you told me to watch for.

Track B would make sense if you specifically wanted al-folio's `/repositories/` GitHub-stats cards, its
Jupyter/distill-post support for a technical blog, or you found the current visual system actually ugly rather than
under-filled-in. None of those apply here based on what you've told me and what the audit found.

**Go with Track A.** Ping me and I'll open a branch (`seo-audit-fixes`) and start on the table above — I'd suggest
committing roughly in the order listed, since 1–3 are the highest-leverage and lowest-risk, and 7 (deleting the
orphan pages) needs your one-line answer first: delete `teaching.md`/`software.md`/`talks.md`, or do you actually want
real Teaching/Software/Talks pages eventually?
