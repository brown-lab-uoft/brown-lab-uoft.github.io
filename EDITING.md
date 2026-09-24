# Making changes yourself

Most day-to-day updates — swapping a photo, editing a sentence, adding a news item —
don't require a terminal at all.

## Fastest path: edit directly on GitHub.com

1. Browse to the file on github.com.
2. Click the pencil (✎) icon to edit it (or "Add file → Upload files" for photos, inside
   the target folder).
3. Make your change.
4. At the bottom, pick **"Create a new branch and start a pull request"** — not "commit
   directly to `main`".
5. Open the PR, merge it, wait ~1 min for the "Build and Deploy" Action to finish (check
   the Actions tab), then hard-refresh the live site.

Never commit straight to `main`. A branch + PR means a bad edit doesn't go live
immediately, and you can see the diff before it does.

## Photos — where they live

| What | Location |
|---|---|
| Your headshot (About, Team, social previews) | `images/headshot.jpg` |
| Team headshots | `images/team/`, filenames wired up in `_data/team_members.yml` |
| Homepage group photo | `images/group/group-photo-main.jpg` |
| Gallery photos | `images/gallery/`, listed in `_pages/gallery.md` |
| Research page thumbnails | `images/research/`, referenced in `_pages/research.md` |
| Lab logo (navbar, small) | `images/logo.png` |
| Lab logo (large — Contact Us, social share fallback) | `images/logo_large.png` |
| Homepage hero banner | `images/banner/colorful-test-tubes.jpg` |
| Page banners (About/Publications/Team/Repositories/News) | `images/gallery/*` — see "Page banners" below |
| Contact Us photo | `images/contact/jb-contact.jpg` |
| Sponsor/funder logos | `images/`, listed in `_data/funders.yml` |

**Easiest swap**: upload a new photo with the *same filename* to overwrite it — nothing
else to change. If you want a new filename, you'll also need to update the one line
referencing it (the .md or .yml file listed above).

### Page banners

About, Publications, Team, Repositories, and News each show a short photo strip above
their content. It's controlled by one line in that page's front matter (the `---`
block at the top of the file), e.g. in `_pages/about.md`:

```yaml
banner: gallery/peptide-library-synthesis-2.jpg
```

The path is relative to `images/`. To change a page's banner, just edit that line to
point at a different file already in `images/`. To remove a page's banner entirely,
delete the `banner:` line. Research and Gallery don't have one (deliberately — they're
already photo-heavy).

## Text/content — where it lives

| What | File |
|---|---|
| Team roster (names, roles, order) | `_data/team_members.yml` |
| Alumni | `_data/alumni.yml` |
| News items | `_data/news.yml` |
| Grants | `_data/grants.yml` |
| Awards | `_data/awards.yml` |
| Funder/sponsor logos (shown on the homepage) | `_data/funders.yml` |
| Your education (shown on About) | `_data/pi.yml` |
| Your bio paragraph | `_pages/about.md` |
| Homepage "About Us" text, group photo caption, Contact Us address | `_pages/home.md` |
| Research area descriptions | `_pages/research.md` |
| Repositories page (GitHub links) | `_pages/repositories.md` |
| Contact address, your name/email/links, accent color | `_config.yml` |
| Publications | `assets/ref.bib` — **don't hand-edit this**, it's auto-overwritten every Monday from your ORCID. Fix publications at the source (ORCID) instead. |

**Adding a team member** — copy this pattern into `_data/team_members.yml` (order in the
file = order on the page):
```yaml
- name: "Full Name"
  photo: team/filename.jpg
  info: "Role"
```

**Changing the lab's address** — edit the `address:` block in `_config.yml`. It drives
both the printed address and the Google Maps embed on the homepage automatically.

## What's safe to touch yourself vs. what to bring back to me (or another developer)

- **Safe**: anything in `_data/*.yml`, page text in `_pages/*.md`, front-matter fields
  like `banner:`/`description:`/`image:`, swapping images. These are content — low risk,
  easy to review in a PR diff.
- **Bring it back**: anything in `_layouts/`, `_includes/`, or `_sass/`. That's the
  template/CSS machinery. A small mistake there can break the build in ways that aren't
  obvious from the diff.
