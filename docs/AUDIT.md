# SEO & Design Audit — Brown Lab Website

Date: 2026-09-22
Scope: `brown-lab-uoft.github.io`, audited via static analysis of the repo, a local `bundle exec jekyll build`
(ground truth for what actually ships — not just what the templates intend), and one live fetch of the homepage.

**Method note on the visual section**: I don't have real browser rendering/screenshot capability here. The live-fetch
tool converts the page to Markdown, which drops CSS layout, so anything below about visual design is inferred from
reading the Sass/HTML source and the built output, not from looking at pixels. Where the fetch tool reported "no
sidebar" or "no search," that's an artifact of Markdown extraction stripping those elements — both exist in the code
(`_includes/sidebar.html`, the search overlay in `_includes/header.html`) and I've verified them by reading source. I
did not treat the fetch's negative claims as evidence.

Severity key: **blocking** (actively hurts you today, fix first) · **important** (real cost, not urgent) · **polish**
(worth doing, low stakes).

---

## Technical SEO

### 1. [blocking] The sitemap advertises zero pages of your actual site
`jekyll-sitemap` is installed and wired correctly. The problem is upstream: **all 12 files in `_pages/` have
`sitemap: false` in front matter** — Home, About, Research, Publications, Team, News, Media, everything. I confirmed
this isn't theoretical by running `bundle exec jekyll build` and reading the generated `sitemap.xml`. It contains
exactly five URLs:

```
/lecture/notes/1961/11/28/space-time.html          (leftover template demo post)
/fun/2024/05/31/great-mathematicians-and-physicists.html   (leftover template demo post)
/papers/example_proceeding.pdf                      (leftover template demo file)
/papers/feynman06.pdf                               (leftover template demo file)
/papers/feynman39.pdf                               (leftover template demo file)
```

Every real page on the site — the ones that would actually answer "Brown Lab Toronto peptide" — is invisible to the
sitemap. Google can still crawl via internal links/nav without a sitemap, but you're giving it nothing and handing it
five pieces of Feynman-themed demo content instead. This is the single highest-leverage fix available.

### 2. [blocking] The Person schema names the wrong entity
`_includes/head.html` line 71 sets the JSON-LD `Person.name` to `{{ site.name }}`, which resolves to **"Brown Lab at
UofT"** — not your name. Verified in the built output on `/about/`:

```json
"author": {
  "@type": "Person",
  "name": "Brown Lab at UofT",
  "jobTitle": "Assistant Professor",
  ...
}
```

This tells every crawler — Google, and any LLM that parses structured data — that a person named "Brown Lab at UofT"
holds your job title. It should be `site.pi_name` ("Joseph S. Brown"). This is the schema most directly relevant to
your stated goal (being found and correctly identified by AI assistants), and it's currently wrong on every page.

### 3. [important] Meta description is identical on every page
Verified across the full built site: every single page emits the exact same
`<meta name="description" content="Academic webpage of Dr. Joseph S. Brown, Brown Lab, University of Toronto">`. This
is textbook duplicate-meta-description — the first thing Search Console flags — and it's also generic: no mention of
peptides, AMR, self-driving labs, or AS-MS, i.e. none of the terms someone would actually search. The description is
your ad copy in search results; right now every page has the same weak ad copy.

### 4. [important] `jekyll-seo-tag` isn't installed; `<head>` hand-rolls everything
Not in `Gemfile` or `Gemfile.lock`. What's there instead is a manually written block in `head.html` covering title,
description, OG, Twitter Card, canonical, and JSON-LD. It mostly works (see canonical, below — that part's fine) but
it's a maintenance burden and it's missing things the plugin gives for free: `og:type` differentiation for articles
vs. pages, breadcrumb JSON-LD, and less copy-paste risk as pages are added.

### 5. [important] Social preview image is a portrait headshot, not an OG-sized asset
`og:image` / `twitter:image` both resolve to `images/headshot.jpg` sitewide — same image regardless of what's shared.
It's a headshot, not a 1200×630 designed card, so link previews on Slack/Twitter/LinkedIn will crop it unpredictably.
No per-page override exists.

### 6. [important] No Organization entity in structured data; two real affiliations are structurally invisible
The only "organization" in JSON-LD is a bare `{"@type": "Organization", "name": "University of Toronto"}` nested
inside `Person.affiliation` — no URL, no logo, no `sameAs`. **Leslie Dan Faculty of Pharmacy** and **Acceleration
Consortium** — both real, both important to how you want to be found — appear nowhere in structured data, despite
appearing correctly in prose on the homepage bio and in `_data/grants.yml`. An AI assistant extracting your
affiliation from structured data today would get "University of Toronto" and nothing more specific.

### 7. [important] Publications have no structured data
`/publications/` renders via jekyll-scholar's `{% bibliography %}` tag — a plain HTML list, no `ScholarlyArticle` /
`CreativeWork` JSON-LD per entry. Your papers aren't machine-readable as scholarly works to anything parsing the page.

### 8. [important] Stray demo content is live, public, and is literally what your sitemap currently promotes
`/papers/feynman06.pdf`, `/papers/feynman39.pdf`, `/papers/example_proceeding.pdf` are template leftovers still
sitting in the repo and served in production (see finding #1 — these are 3 of the 5 URLs your sitemap advertises).
Two demo blog posts (`_posts/1961-11-28-space-time.md`, `_posts/2024-05-31-great-mathematicians-and-physicists.md`,
plus their backing `_data/great_mathematicians_and_physicists.csv`) are the other 2.

### 9. [important] `/teaching/` and `/software/` are live with unmigrated template content
Both pages are excluded from `nav_pages` in `_config.yml` and from the sitemap, but `sitemap: false` doesn't stop
Jekyll from building and serving them — anyone with the URL (or a stray inbound link, or a search engine that finds
them some other way) sees Feynman's "Physics 1, 2, 3" course list and a "Path Integral Monte Carlo" software entry
attributed to "R. P. Feynman." `/talks/` is similarly live but structurally empty: it queries
`{% bibliography --query @incollection[keywords ^= invited] %}`, and `ref.bib` has zero entries with an `invited`
keyword, so the page renders two empty headers and nothing else.

### 10. [polish] Homepage `<title>` is "Home - Brown Lab at UofT"
Verified in build output. It's unique (not a duplicate-title problem) but it's the single most valuable title tag on
the domain and it's spent on the word "Home" instead of a value proposition with searchable terms.

### 11. [polish] `_config.yml` has no `lang` or `author` field
`<html lang="en">` is hardcoded in `_layouts/default.html` rather than driven by config (functionally fine, just not
configurable — `en` vs `en-CA` is a marginal signal either way). `author` is moot while `jekyll-seo-tag` is absent;
becomes relevant if you adopt it.

### What's actually fine — no action needed
- **Canonical URLs**: correctly implemented, unique per page, verified in build output (`/`, `/about/`, `/team/` all
  resolve correctly).
- **`robots.txt`**: present, correctly permissive (`Allow: /`), correctly points at `sitemap.xml`. The file itself has
  no problem — what it points to does (#1).
- **Titles are unique per page** (aside from #10's weak copy on Home) — not the "everything says Home" failure mode
  you were worried about.
- **RSS feed** (`feed.xml`) exists and works, hand-rolled rather than via `jekyll-feed`, pulling from both
  `site.posts` and `_data/news.yml`.
- `_config.yml`: `url` is set correctly (`https://brown-lab-uoft.github.io`), `baseurl` is correctly empty for a
  user/org GitHub Pages site.

---

## Visual / design

- **Typography**: DM Sans (body) + Source Serif 4 (headings) + JetBrains Mono (code), loaded from Google Fonts —
  a deliberate serif/sans editorial pairing, not a Bootstrap default stack. Already customized.
- **Color palette**: a warm "parchment" light theme (`#f8f6f1` background, `#2c2a25` text) with a teal accent
  (`#1a7a6d`), plus a full dark-mode palette with genuinely different (not just inverted) warm dark tones. Not
  Bootstrap defaults, not generic.
- **Tokenization**: better than you're assuming. `_sass/base/_variables.scss` already defines CSS custom properties
  for color (with a `[data-bs-theme="dark"]` override block), a spacing scale (`--space-1` through `--space-16`, ≈
  4px–64px), border-radius, shadow, and transition tokens. What's *not* tokenized: the type scale — h1–h4 sizes are
  hardcoded rem literals in `_typography.scss`. That file is a single source of truth (not scattered across the
  codebase), but the sizes aren't swappable via a variable the way color and spacing are.
- **Remaining hardcoded colors**: `#fff` appears ~8 times in `_buttons.scss`/`_chips.scss` where `var(--bg-card)` or a
  new `--on-accent` token would fit the existing system; a Stanford-cardinal red (`#b31b1b` / `#8c1515`) is hardcoded
  for `.btn-arxiv`/`.btn-paper` — inherited from the upstream template, unrelated to your teal brand, never reskinned;
  green/amber (`#16a34a` / `#d97706`) are hardcoded for callout components.
- **Responsive breakpoints**: implemented with intention, not absent — 768px (home grid + hero), 767px (navbar
  collapse), 640px (footer, team grid), each in the component that needs it.
- **Dark mode**: fully implemented — navbar toggle, `localStorage` persistence, `prefers-color-scheme` fallback, and
  a pre-paint inline script in `head.html` that prevents a flash of the wrong theme on load. This is more complete
  than most academic lab sites bother with.
- **Homepage hero**: text-only — an `<h2>` + subhead + six topic "chips" linking to `/research/`. A fully-styled
  `.banner-frame` component exists in `_sass/layouts/_home.scss` (rounded frame, caption bar, hover zoom) but nothing
  in `home.md` uses it — the capability is built and unused.
- **Team page photos**: every current team member's photo is the same placeholder file, `images/rock.jpg`. This is
  the single most visible unpolished thing on the site — five different people, one rock.
- **Unused leftover template assets**: `images/team/*.svg` (illustrated avatars for Feynman collaborators — Hibbs,
  Zweig, Hellwarth, Curtright, Frazer) and six `images/research/*.svg` topics (partons, QED, quantum computing,
  superfluidity, weak interactions, nanotechnology) that no current page references. Clutter, not a functional bug.
- **Search**: a working site-search overlay (icon in navbar, keyboard-accessible, ESC to close) already exists in
  `_includes/header.html` plus supporting JS — a feature most academic sites in this space don't have.

**Net assessment**: the "reads as a default academic site" feeling is not a CSS/architecture problem — the design
system is already bespoke (custom fonts, a real palette, dark mode, partial tokenization, working search). What's
actually flattening it: a text-only hero with no imagery, placeholder rock photos on the one page a prospective
student is most likely to scrutinize, generic research-topic SVG icons, and unmigrated template pages that would
look bad to anyone who found them. This is a content/asset problem wearing a "needs a redesign" costume.

---

## Discoverability

- Pages exist for everything you listed as necessary: research focus (`/research/`), publications
  (`/publications/`, BibTeX via jekyll-scholar), team (`/team/`), news (`/news/`, file is `allnews.md` but permalink
  is `/news/`). No dedicated `/contact/` page, but email and social links are on the PI card on both About and Team
  — I don't think a separate contact page is missing functionality, just a missing URL pattern.
- No CV is linked (`links.cv` is blank in `_config.yml`) — that's presumably intentional/pending, not a bug in the
  template; your call whether to add one.
- RSS feed exists and works, low-value for this audience but zero-cost to keep.
- **No Google Analytics configured** (`analytics.google_id` is blank). You currently have no visibility into whether
  anyone finds this site, from any source, at all — you're diagnosing a discoverability problem with no instrument
  attached to measure it.
- Google Search Console indexing status: **cannot be checked from here** — requires your Google account. See manual
  steps below.

### Manual steps only you can take (noted, not actionable by me)
1. **Google Search Console**: verify domain ownership and check current indexing status — I can't see whether Google
   has indexed any pages today, or what it thinks the site's URLs are. Do this before Phase 3 changes so we have a
   "before" baseline, and again after, to confirm the sitemap fix (#1) actually gets crawled.
2. **Set `analytics.google_id`** in `_config.yml` once you've created a GA4 property, if you want traffic data going
   forward — currently blank, analytics code path already exists and just needs the ID.
3. **Custom domain**: no `CNAME` file exists — the site is on the default `brown-lab-uoft.github.io` subdomain. Not a
   problem for SEO per se, but worth a conscious decision rather than a default.
4. **OG image commissioning**: noted for Phase 3 — a real 1200×630 social-share asset needs actual design/photo
   input from you, not something I should just generate.

---

## Summary — what's actually broken vs. what's fine

| Area | Status |
|---|---|
| Sitemap | **Broken** — advertises 0 real pages, 5 demo artifacts |
| Person/Organization schema | **Broken** — wrong entity name, missing affiliations |
| Meta descriptions | **Broken** — identical everywhere, generic |
| Canonical URLs | Fine |
| robots.txt | Fine |
| Page titles | Mostly fine (one weak one, no duplicates) |
| RSS | Fine, low-value |
| Design system (fonts/color/tokens/dark mode) | Fine, already bespoke |
| Responsive layout | Fine |
| Team page photos | **Broken** — placeholder rock.jpg for real people |
| Hero section | Present but flat — text-only, unused banner component |
| Leftover template content | **Broken** — Feynman demo pages/PDFs live in production |
| Analytics / measurement | **Missing entirely** |

Ready for Phase 2. Let me know when you've read this and I'll draft the Track A vs. Track B recommendation memo.
