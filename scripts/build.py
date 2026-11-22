#!/usr/bin/env python3
"""Build the three static, SEO-addressable language variants of the landing."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://podlinker.com"

COPY = {
    "ca": {
        "title": "Podlinker — Descobreix podcasts a través de la teva gent",
        "description": "Descobreix episodis a través de les persones que segueixes. Desa els que tries i escolta'ls en un podcast a la teva mida.",
        "skip": "Salta al contingut", "navLabel": "Navegació principal", "navHow": "Com funciona", "navHighlights": "Destacats", "navPersonal": "Podcast a mida", "langLabel": "Idioma del web",
        "hero": "El teu pròxim podcast comença amb algú que segueixes.",
        "intro": "Segueix persones. Descobreix els episodis dels podcasts que segueixen. Un feed fet de la teva gent, no d'una llista anònima.",
        "cta": "Descobreix com funciona",
        "diagramHeading": "Així es construeix el teu feed", "youFollow": "Tu segueixes", "people": "persones", "theyFollow": "Elles segueixen", "podcasts": "podcasts", "youDiscover": "Tu descobreixes", "episodes": "episodis",
        "networkLabel": "La teva xarxa", "networkDetail": "Perfils que has triat seguir", "sharedLabel": "La seva col·lecció", "sharedDetail": "Podcasts que comparteixen amb la xarxa", "feedLabel": "Capítols nous", "feedDetail": "Dels podcasts que segueixen",
        "highlightsTitle": "Destacats: les recomanacions de la teva xarxa.",
        "highlightsBody": "A Destacats hi trobes episodis que les persones que segueixes han recomanat expressament. El feed principal, en canvi, mostra els capítols nous dels podcasts que segueixen.",
        "personalTitle": "Els episodis que tries, junts al teu reproductor.",
        "personalBody": "Desa capítols de podcasts diferents. Podlinker els reuneix en un RSS privat que pots afegir al teu reproductor habitual i que s'actualitza quan canvies la selecció.",
        "savedLabel": "Episodis desats", "savedDetail": "Els capítols que tries", "rssLabel": "El teu RSS privat", "rssDetail": "La teva selecció, sempre al dia", "playerLabel": "El teu reproductor", "playerDetail": "Escolta'ls on ja escoltes podcasts",
        "footer": "Descobrir podcasts, de persona a persona.", "brandAria": "Podlinker, inici",
    },
    "es": {
        "title": "Podlinker — Descubre podcasts a través de tu gente",
        "description": "Descubre episodios a través de las personas que sigues. Guarda los que eliges y escúchalos en un podcast a tu medida.",
        "skip": "Ir al contenido", "navLabel": "Navegación principal", "navHow": "Cómo funciona", "navHighlights": "Destacados", "navPersonal": "Podcast a medida", "langLabel": "Idioma de la web",
        "hero": "Tu próximo podcast empieza con alguien a quien sigues.",
        "intro": "Sigue a personas. Descubre los episodios de los podcasts que siguen. Un feed hecho con tu gente, no con una lista anónima.",
        "cta": "Descubre cómo funciona",
        "diagramHeading": "Así se construye tu feed", "youFollow": "Tú sigues a", "people": "personas", "theyFollow": "Ellas siguen", "podcasts": "podcasts", "youDiscover": "Tú descubres", "episodes": "episodios",
        "networkLabel": "Tu red", "networkDetail": "Perfiles que has elegido seguir", "sharedLabel": "Su colección", "sharedDetail": "Podcasts que comparten con la red", "feedLabel": "Capítulos nuevos", "feedDetail": "De los podcasts que siguen",
        "highlightsTitle": "Destacados: las recomendaciones de tu red.",
        "highlightsBody": "En Destacados encuentras episodios que las personas a las que sigues han recomendado expresamente. El feed principal, en cambio, muestra los capítulos nuevos de los podcasts que siguen.",
        "personalTitle": "Los episodios que eliges, juntos en tu reproductor.",
        "personalBody": "Guarda capítulos de distintos podcasts. Podlinker los reúne en un RSS privado que puedes añadir a tu reproductor habitual y que se actualiza cuando cambias la selección.",
        "savedLabel": "Episodios guardados", "savedDetail": "Los capítulos que eliges", "rssLabel": "Tu RSS privado", "rssDetail": "Tu selección, siempre al día", "playerLabel": "Tu reproductor", "playerDetail": "Escúchalos donde ya escuchas podcasts",
        "footer": "Descubrir podcasts, de persona a persona.", "brandAria": "Podlinker, inicio",
    },
    "en": {
        "title": "Podlinker — Discover podcasts through your people",
        "description": "Discover episodes through the people you follow. Save the ones you choose and listen to them in a podcast made for you.",
        "skip": "Skip to content", "navLabel": "Main navigation", "navHow": "How it works", "navHighlights": "Highlights", "navPersonal": "Your own podcast", "langLabel": "Website language",
        "hero": "Your next podcast starts with someone you follow.",
        "intro": "Follow people. Discover episodes from the podcasts they follow. A feed shaped by your people, not an anonymous chart.",
        "cta": "See how it works",
        "diagramHeading": "How your feed takes shape", "youFollow": "You follow", "people": "people", "theyFollow": "They follow", "podcasts": "podcasts", "youDiscover": "You discover", "episodes": "episodes",
        "networkLabel": "Your network", "networkDetail": "Profiles you chose to follow", "sharedLabel": "Their collection", "sharedDetail": "Podcasts they share with the network", "feedLabel": "New episodes", "feedDetail": "From the podcasts they follow",
        "highlightsTitle": "Highlights: what your network recommends.",
        "highlightsBody": "Highlights shows episodes explicitly recommended by people you follow. Your main feed, by contrast, shows new episodes from podcasts they follow.",
        "personalTitle": "The episodes you choose, together in your player.",
        "personalBody": "Save episodes from different podcasts. Podlinker brings them together in a private RSS feed you can add to your usual podcast player. It updates when you change your selection.",
        "savedLabel": "Saved episodes", "savedDetail": "The episodes you choose", "rssLabel": "Your private RSS", "rssDetail": "Your selection, always up to date", "playerLabel": "Your podcast player", "playerDetail": "Listen where you already listen to podcasts",
        "footer": "Discover podcasts, person to person.", "brandAria": "Podlinker, home",
    },
}

LANG_NAMES = {"ca": "Català", "es": "Español", "en": "English"}

for locale, raw in COPY.items():
    c = {key: escape(value, quote=True) for key, value in raw.items()}
    langs = "\n".join(
        f'<a href="../{code}/" lang="{code}" hreflang="{code}" data-lang="{code}" class="{"active" if code == locale else ""}" {"aria-current=\"page\"" if code == locale else ""}>{code.upper()}<span class="sr-only"> — {name}</span></a>'
        for code, name in LANG_NAMES.items()
    )
    alternates = "\n".join(f'<link rel="alternate" hreflang="{code}" href="{BASE}/{code}/">' for code in COPY)
    html = f'''<!doctype html>
<html lang="{locale}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#3047cd">
  <title>{c["title"]}</title>
  <meta name="description" content="{c["description"]}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{c["title"]}">
  <meta property="og:description" content="{c["description"]}">
  <meta property="og:image" content="{BASE}/assets/og-{locale}.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:url" content="{BASE}/{locale}/">
  <link rel="canonical" href="{BASE}/{locale}/">
  {alternates}
  <link rel="alternate" hreflang="x-default" href="{BASE}/">
  <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
  <link rel="preload" href="../assets/barlow-condensed-800.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="../assets/style.css">
  <script defer src="../assets/site.js"></script>
</head>
<body>
  <a class="skip-link" href="#main">{c["skip"]}</a>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="./" aria-label="{c["brandAria"]}"><span class="brand-mark"><img src="../assets/logo.svg" alt="" width="28" height="28"></span><span>podlinker<span class="brand-dot">.</span></span></a>
      <nav class="header-nav" aria-label="{c["navLabel"]}"><a href="#com-funciona">{c["navHow"]}</a><a href="#destacats">{c["navHighlights"]}</a><a href="#podcast-a-mida">{c["navPersonal"]}</a></nav>
      <nav class="language-switch" aria-label="{c["langLabel"]}">{langs}</nav>
    </div>
  </header>
  <main id="main">
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap hero-inner">
        <div class="hero-main">
          <h1 id="hero-title">{c["hero"]}</h1>
          <div class="hero-bottom">
            <p>{c["intro"]}</p>
            <a class="button button-lime" href="#com-funciona">{c["cta"]} <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-5-5 5 5-5 5"/></svg></a>
          </div>
        </div>
      </div>
    </section>
    <section class="mechanism" id="com-funciona" aria-labelledby="diagram-title">
      <div class="wrap">
        <div class="section-heading"><h2 id="diagram-title">{c["diagramHeading"]}</h2><span class="section-rule" aria-hidden="true"></span></div>
        <div class="network-board" aria-label="{c["diagramHeading"]}">
          <div class="board-column people-column"><div class="board-caption">{c["youFollow"]} <strong>{c["people"]}</strong></div><div class="mechanism-stage people-stage"><strong>{c["networkLabel"]}</strong><span>{c["networkDetail"]}</span></div></div>
          <div class="board-arrow" aria-hidden="true"><span></span></div>
          <div class="board-column shows-column"><div class="board-caption">{c["theyFollow"]} <strong>{c["podcasts"]}</strong></div><div class="mechanism-stage shows-stage"><strong>{c["sharedLabel"]}</strong><span>{c["sharedDetail"]}</span></div></div>
          <div class="board-arrow" aria-hidden="true"><span></span></div>
          <div class="board-column episode-column"><div class="board-caption">{c["youDiscover"]} <strong>{c["episodes"]}</strong></div><div class="mechanism-stage episode-stage"><strong>{c["feedLabel"]}</strong><span>{c["feedDetail"]}</span></div></div>
        </div>
      </div>
    </section>
    <section class="highlights" id="destacats" aria-labelledby="highlights-title">
      <div class="wrap highlights-inner">
        <h2 id="highlights-title">{c["highlightsTitle"]}</h2>
        <p>{c["highlightsBody"]}</p>
      </div>
    </section>
    <section class="personal-podcast" id="podcast-a-mida" aria-labelledby="personal-podcast-title">
      <div class="wrap">
        <div class="personal-podcast-inner"><h2 id="personal-podcast-title">{c["personalTitle"]}</h2><p>{c["personalBody"]}</p></div>
        <div class="saved-flow">
          <div class="flow-stage saved-stage"><h3>{c["savedLabel"]}</h3><svg class="saved-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18l-6-4-6 4V3Z"/></svg><p>{c["savedDetail"]}</p></div>
          <div class="flow-arrow" aria-hidden="true"><span></span></div>
          <div class="flow-stage rss-stage"><h3>{c["rssLabel"]}</h3><div class="flow-icon rss-icon" aria-hidden="true"><span></span><span></span><span></span></div><p>{c["rssDetail"]}</p></div>
          <div class="flow-arrow" aria-hidden="true"><span></span></div>
          <div class="flow-stage player-stage"><h3>{c["playerLabel"]}</h3><div class="flow-icon play-icon" aria-hidden="true"><span></span></div><p>{c["playerDetail"]}</p></div>
        </div>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="wrap footer-inner"><div><span class="footer-brand">podlinker<span>.</span></span><p>{c["footer"]}</p></div></div></footer>
</body>
</html>
'''
    (ROOT / locale / "index.html").write_text(html)

(ROOT / "index.html").write_text('''<!doctype html><html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Podlinker</title><script src="assets/redirect.js"></script></head><body><p><a href="ca/">Podlinker · Català</a></p><p><a href="es/">Español</a> · <a href="en/">English</a></p></body></html>''')

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}/{locale}/</loc></url>\n" for locale in COPY)
    + '</urlset>\n'
)
