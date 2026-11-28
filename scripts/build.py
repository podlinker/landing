#!/usr/bin/env python3
"""Build the three static, SEO-addressable language variants of the landing."""
from hashlib import sha256
from html import escape
from pathlib import Path
from os import environ

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://podlinker.com"

# A returning browser must not pair new markup with older cached styles or scripts.
ASSET_URLS = {
    name: f"assets/{name}?v={sha256((ROOT / 'assets' / name).read_bytes()).hexdigest()[:16]}"
    for name in ("style.css", "site.js", "redirect.js", "not-found.js")
}

COPY = {
    "ca": {
        "title": "Podlinker — Descobreix podcasts a través de la teva gent",
        "description": "Descobreix episodis a través de les persones que segueixes. Desa els que tries i escolta'ls en un podcast a la teva mida.",
        "skip": "Salta al contingut", "navLabel": "Navegació principal", "navHow": "Descoberta", "navHighlights": "Destacats", "navPersonal": "Podcast a mida", "langLabel": "Idioma del web",
        "hero": "El teu pròxim podcast comença amb algú que segueixes.",
        "intro": "Segueix persones. Descobreix els episodis dels podcasts que segueixen. Un feed fet de la teva gent, no d'una llista anònima.",
        "cta": "Mira com funciona",
        "diagramHeading": "Troba capítols nous. I podcasts que no coneixies.",
        "networkLabel": "Les persones que segueixes", "sharedLabel": "Els podcasts que comparteixen", "feedLabel": "Els episodis que descobreixes",
        "highlightsTitle": "Destacats",
        "highlightsBody": "Quan algú que segueixes recomana un episodi, ho veus al feed. A Destacats pots trobar totes aquestes recomanacions juntes.",
        "personalTitle": "Els episodis que tries, junts al teu reproductor.",
        "personalBody": "Desa episodis de podcasts diferents i activa un enllaç privat (RSS) per escoltar-los al teu reproductor de podcasts compatible. La selecció s’actualitza quan hi afegeixes o en treus un capítol.",
        "savedLabel": "Episodis desats", "savedDetail": "Tria capítols de podcasts diferents.", "rssLabel": "Un enllaç privat", "rssDetail": "Activa el teu feed RSS.", "playerLabel": "El teu reproductor", "playerDetail": "Afegeix-hi l’enllaç per escoltar els desats.",
        "footer": "Podlinker és en fase de pilot tancat.", "brandAria": "Podlinker, inici",
        "discoveryBody": "Al feed hi entren capítols nous dels podcasts que comparteix la teva xarxa. A «Podcasts nous per a tu» hi trobes podcasts de la xarxa que encara no tens a la biblioteca.",
    },
    "es": {
        "title": "Podlinker — Descubre podcasts a través de tu gente",
        "description": "Descubre episodios a través de las personas que sigues. Guarda los que eliges y escúchalos en un podcast a tu medida.",
        "skip": "Ir al contenido", "navLabel": "Navegación principal", "navHow": "Descubrir", "navHighlights": "Destacados", "navPersonal": "Podcast a medida", "langLabel": "Idioma de la web",
        "hero": "Tu próximo podcast empieza con alguien a quien sigues.",
        "intro": "Sigue a personas. Descubre los episodios de los podcasts que siguen. Un feed hecho con tu gente, no con una lista anónima.",
        "cta": "Mira cómo funciona",
        "diagramHeading": "Encuentra episodios nuevos. Y podcasts que no conocías.",
        "networkLabel": "Las personas a las que sigues", "sharedLabel": "Los podcasts que comparten", "feedLabel": "Los episodios que descubres",
        "highlightsTitle": "Destacados",
        "highlightsBody": "Cuando alguien a quien sigues recomienda un episodio, lo ves en el feed. En Destacados puedes encontrar todas esas recomendaciones juntas.",
        "personalTitle": "Los episodios que eliges, juntos en tu reproductor.",
        "personalBody": "Guarda episodios de distintos podcasts y activa un enlace privado (RSS) para escucharlos en un reproductor de podcasts compatible. La selección se actualiza cuando añades o quitas un episodio.",
        "savedLabel": "Episodios guardados", "savedDetail": "Elige episodios de distintos podcasts.", "rssLabel": "Un enlace privado", "rssDetail": "Activa tu feed RSS.", "playerLabel": "Tu reproductor", "playerDetail": "Añade el enlace para escuchar lo que guardaste.",
        "footer": "Podlinker está en fase de piloto cerrado.", "brandAria": "Podlinker, inicio",
        "discoveryBody": "En el feed aparecen episodios nuevos de los podcasts que comparte tu red. En «Podcasts nuevos para ti» encuentras podcasts de tu red que aún no tienes en tu biblioteca.",
    },
    "en": {
        "title": "Podlinker — Discover podcasts through your people",
        "description": "Discover episodes through the people you follow. Save the ones you choose and listen to them in a podcast made for you.",
        "skip": "Skip to content", "navLabel": "Main navigation", "navHow": "Discovery", "navHighlights": "Highlights", "navPersonal": "Your own podcast", "langLabel": "Website language",
        "hero": "Your next podcast starts with someone you follow.",
        "intro": "Follow people. Discover episodes from the podcasts they follow. A feed shaped by your people, not an anonymous chart.",
        "cta": "See how it works",
        "diagramHeading": "Find new episodes. And podcasts you haven’t heard of.",
        "networkLabel": "The people you follow", "sharedLabel": "The podcasts they share", "feedLabel": "The episodes you discover",
        "highlightsTitle": "Highlights",
        "highlightsBody": "When someone you follow recommends an episode, it shows up in your feed. In Highlights you can find all those recommendations together.",
        "personalTitle": "The episodes you choose, together in your player.",
        "personalBody": "Save episodes from different podcasts and turn on a private link (RSS) to listen in a compatible podcast player. Your selection updates as you add or remove episodes.",
        "savedLabel": "Saved episodes", "savedDetail": "Pick episodes from different podcasts.", "rssLabel": "A private link", "rssDetail": "Turn on your RSS feed.", "playerLabel": "Your podcast player", "playerDetail": "Add the link to listen to your saved episodes.",
        "footer": "Podlinker is in a closed pilot.", "brandAria": "Podlinker, home",
        "discoveryBody": "Your feed brings you new episodes from podcasts your network shares. “Podcasts new to you” brings together podcasts from your network that aren’t in your library yet.",
    },
}

LANG_NAMES = {"ca": "Català", "es": "Español", "en": "English"}


def language_links(prefix):
    return "\n        ".join(
        f'<a href="{prefix}{code}/" lang="{code}" hreflang="{code}">{name}</a>'
        for code, name in LANG_NAMES.items()
    )


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
  <meta name="theme-color" content="#2544bd">
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
  <link rel="stylesheet" href="../{ASSET_URLS["style.css"]}">
  <script defer src="../{ASSET_URLS["site.js"]}"></script>
</head>
<body>
  <a class="skip-link" href="#main">{c["skip"]}</a>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="./" aria-label="{c["brandAria"]}"><span class="brand-mark"><img src="../assets/logo.svg" alt="" width="28" height="28"></span><span>podlinker<span class="brand-dot">.</span></span></a>
      <nav class="language-switch" aria-label="{c["langLabel"]}">{langs}</nav>
      <nav class="header-nav" aria-label="{c["navLabel"]}"><a href="#com-funciona">{c["navHow"]}</a><a href="#destacats">{c["navHighlights"]}</a><a href="#podcast-a-mida">{c["navPersonal"]}</a></nav>
    </div>
  </header>
  <main id="main" tabindex="-1">
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap hero-inner">
        <div class="hero-main">
          <h1 id="hero-title">{c["hero"]}</h1>
          <p>{c["intro"]}</p>
          <a class="button" href="#com-funciona">{c["cta"]} <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-5-5 5 5-5 5"/></svg></a>
        </div>
        <ol class="signal-board" role="list">
          <li><span class="signal-icon signal-people" aria-hidden="true"><i></i><i></i><i></i></span><strong>{c["networkLabel"]}</strong></li>
          <li><span class="signal-icon signal-shows" aria-hidden="true"><i></i><i></i><i></i></span><strong>{c["sharedLabel"]}</strong></li>
          <li><span class="signal-icon signal-episodes" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span><strong>{c["feedLabel"]}</strong></li>
        </ol>
      </div>
    </section>
    <section class="discovery" id="com-funciona" tabindex="-1" aria-labelledby="diagram-title">
      <div class="wrap discovery-grid">
        <div class="discovery-main">
          <h2 id="diagram-title">{c["diagramHeading"]}</h2>
          <p>{c["discoveryBody"]}</p>
        </div>
        <section class="highlights" id="destacats" tabindex="-1" aria-labelledby="highlights-title">
          <div class="highlight-mark" aria-hidden="true"></div>
          <h2 id="highlights-title">{c["highlightsTitle"]}</h2>
          <p>{c["highlightsBody"]}</p>
        </section>
      </div>
    </section>
    <section class="personal-podcast" id="podcast-a-mida" tabindex="-1" aria-labelledby="personal-podcast-title">
      <div class="wrap">
        <div class="personal-podcast-inner">
          <h2 id="personal-podcast-title">{c["personalTitle"]}</h2>
          <p>{c["personalBody"]}</p>
        </div>
        <ol class="saved-flow" role="list">
          <li class="flow-stage">
            <svg class="saved-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18l-6-4-6 4V3Z"/></svg>
            <h3>{c["savedLabel"]}</h3>
            <p>{c["savedDetail"]}</p>
          </li>
          <li class="flow-stage">
            <div class="flow-icon rss-icon" aria-hidden="true"><span></span><span></span><span></span></div>
            <h3>{c["rssLabel"]}</h3>
            <p>{c["rssDetail"]}</p>
          </li>
          <li class="flow-stage">
            <div class="flow-icon play-icon" aria-hidden="true"><span></span></div>
            <h3>{c["playerLabel"]}</h3>
            <p>{c["playerDetail"]}</p>
          </li>
        </ol>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="wrap footer-inner"><span class="footer-brand">podlinker<span class="brand-dot">.</span></span><p>{c["footer"]}</p></div></footer>
</body>
</html>
'''
    (ROOT / locale / "index.html").write_text(html)

(ROOT / "index.html").write_text(f'''<!doctype html>
<html lang="ca">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>Podlinker</title>
  <script src="{ASSET_URLS["redirect.js"]}"></script>
  <link rel="stylesheet" href="{ASSET_URLS["style.css"]}">
</head>
<body class="landing-language">
  <header class="site-header">
    <div class="wrap header-inner">
      <h1 class="brand"><span class="brand-mark"><img src="assets/logo.svg" alt="" width="28" height="28"></span><span>podlinker<span class="brand-dot">.</span></span></h1>
    </div>
  </header>
  <main class="wrap">
    <nav class="locale-links" aria-label="Català / Español / English">
        {language_links("")}
    </nav>
  </main>
</body>
</html>
''')

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}/{locale}/</loc></url>\n" for locale in COPY)
    + '</urlset>\n'
)

# The error document can be served from any nested URL.
error_prefix = environ.get("LANDING_404_PREFIX", "")
(ROOT / "404.html").write_text(f'''<!doctype html>
<html lang="ca">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>404 · Pàgina no trobada · Podlinker</title>
  <link rel="icon" href="{error_prefix}/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{error_prefix}/{ASSET_URLS["style.css"]}">
  <script defer src="{error_prefix}/{ASSET_URLS["not-found.js"]}"></script>
</head>
<body>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{error_prefix}/"><span class="brand-mark"><img src="{error_prefix}/assets/logo.svg" alt="" width="28" height="28"></span><span>podlinker<span class="brand-dot">.</span></span></a>
    </div>
  </header>
  <main class="wrap landing-not-found">
    <div class="error-recovery">
      <h1 class="error-fallback" data-error-fallback>
        <span lang="ca">Pàgina no trobada</span>
        <span lang="es">Página no encontrada</span>
        <span lang="en">Page not found</span>
      </h1>
      <section lang="ca" data-error-language hidden><h1>No hem trobat aquesta pàgina</h1><p>L’enllaç pot haver canviat. Pots tornar a la portada de Podlinker.</p><a class="button" href="{error_prefix}/ca/">Torna a la portada</a></section>
      <section lang="es" data-error-language hidden><h1>No encontramos esta página</h1><p>Puede que el enlace haya cambiado. Puedes volver a la portada de Podlinker.</p><a class="button" href="{error_prefix}/es/">Volver al inicio</a></section>
      <section lang="en" data-error-language hidden><h1>This page couldn’t be found</h1><p>The link may have changed. You can return to the Podlinker homepage.</p><a class="button" href="{error_prefix}/en/">Back to the homepage</a></section>
      <nav class="locale-links" aria-label="Català / Español / English">
        {language_links(f"{error_prefix}/")}
      </nav>
    </div>
    <div class="error-frequency" aria-hidden="true"><span>404</span></div>
  </main>
</body>
</html>
''')
