# Podlinker landing

Public pre-launch landing for Podlinker. It explains the people → podcasts → episodes discovery model without implying that a podcast follow is a listen or recommendation. The example people and shows are fictional. Product decisions are canonical in [`podlinker/project`](https://github.com/podlinker/project).

The site is static HTML/CSS/JS in Catalan, Spanish and English. No account data, tracking or signup is collected here. The demo links open the separately hosted, fictional [staging experience](https://staging.podlinker.com/).

## Edit and preview

Edit translations in `scripts/build.py`, then run:

```sh
python3 scripts/build.py
python3 -m http.server 8000
```

Open `http://localhost:8000/`. The root route chooses a previously selected language, then the browser language, then Catalan. Language links persist the choice locally. Each `/ca/`, `/es/` and `/en/` route has its own metadata and canonical URL. To change the visual system, follow `DESIGN.md` and the app's design system.

Social preview images are committed as `assets/og-*.png`; `scripts/og.html?lang=ca|es|en` is their source. Regenerate all three at 1200×630 if the headline changes.

## Publication

`.github/workflows/pages.yml` publishes only the static entry points, assets, robots file and sitemap to GitHub Pages on a push to `main`. The older Next.js template files remain in the repository for now but are not built or shipped by that workflow. The public review URL is `https://podlinker.github.io/landing/`.

Do not set a `CNAME` or change DNS until the GitHub Pages version is approved for `podlinker.com`. When moving domains, update `BASE` in `scripts/build.py`, regenerate the pages, and update `robots.txt` and `sitemap.xml` before configuring the domain.
