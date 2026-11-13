# Podlinker landing

Public pre-launch landing for Podlinker. It explains the people → podcasts → episodes discovery model without implying that a podcast follow is a listen or recommendation. The example people and shows are fictional. Product decisions are canonical in [`podlinker/project`](https://github.com/podlinker/project).

The site is static HTML/CSS/JS in Catalan, Spanish and English. No account data, tracking or signup is collected here. The landing does not link to the staging demo.

## Edit and preview

Edit translations in `scripts/build.py`, then run:

```sh
python3 scripts/build.py
python3 -m http.server 8000
```

Open `http://localhost:8000/`. The root route chooses a previously selected language, then the browser language, then Catalan. Language links persist the choice locally. Each `/ca/`, `/es/` and `/en/` route has its own metadata and canonical URL. To change the visual system, follow `DESIGN.md` and the app's design system.

Social preview images are committed as `assets/og-*.png`; `scripts/og.html?lang=ca|es|en` is their source. Regenerate all three at 1200×630 if the headline changes.

## Publication

The canonical public site is `https://podlinker.com/`, served from the Podlinker test host as a separate static Caddy site. The deployment uses an independent release directory and does not replace `staging.podlinker.com`. `.github/workflows/pages.yml` also publishes the same static entry points, assets, robots file and sitemap to GitHub Pages on a push to `main`; its URL is `https://podlinker.github.io/landing/`. The older Next.js template files remain in the repository for now but are not built or shipped by that workflow.

Edit `BASE` in `scripts/build.py` when moving the canonical domain. The build regenerates the localized pages, `robots.txt` and `sitemap.xml`. The root-language redirect is an external script so the site works under Caddy's `script-src 'self'` policy. Do not set a GitHub Pages `CNAME`; DNS for `podlinker.com` points to the test host.
