#!/usr/bin/env python3
"""Build the three static, SEO-addressable language variants of the landing."""
from html import escape
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://podlinker.com"

COPY = {
    "ca": {
        "title": "Podlinker — Descobreix podcasts a través de la teva gent",
        "description": "Segueix persones i descobreix els episodis dels podcasts que elles segueixen. Podlinker és una nova manera de trobar la teva propera escolta.",
        "skip": "Salta al contingut", "navHow": "Com funciona", "navBeta": "Avís de la beta", "langLabel": "Idioma del web",
        "hero": "El teu pròxim podcast comença amb algú que segueixes.",
        "intro": "Segueix persones. Descobreix els episodis dels podcasts que segueixen. Un feed fet de la teva gent, no d'una llista anònima.",
        "cta": "Avisa'm quan obri la beta", "building": "Podlinker està en construcció",
        "diagramHeading": "Així es construeix el teu feed", "youFollow": "Tu segueixes", "people": "persones", "theyFollow": "Elles segueixen", "podcasts": "podcasts", "youDiscover": "Tu descobreixes", "episodes": "episodis",
        "person1": "La Mar", "person2": "En Pol", "show1": "Fora de mapa", "show2": "Herbari", "sampleEpisode": "Un nou capítol", "sampleSource": "de Fora de mapa", "sampleLabel": "Exemple fictici",
        "note": "Seguir un podcast no vol dir haver escoltat ni recomanat tots els seus capítols.",
        "footer": "Descobrir podcasts, de persona a persona.", "brandAria": "Podlinker, inici", "footerStatus": "Una nova manera de descobrir podcasts. En construcció.",
        "betaEyebrow": "LLISTA D’INTERÈS", "betaTitle": "Un correu quan estiguem a punt.", "betaBody": "Apunta’t per rebre només l’avís quan obrim la beta de Podlinker. Sense butlletí ni correus entremig.",
        "confirmedTitle": "Ja ets a la llista", "confirmedBody": "Hem confirmat el teu correu. T’avisarem quan obrim la beta. No cal fer res més.", "confirmedBack": "Torna a Podlinker", "confirmedPath": "beta-confirmada",
    },
    "es": {
        "title": "Podlinker — Descubre podcasts a través de tu gente",
        "description": "Sigue a personas y descubre los episodios de los podcasts que siguen. Podlinker es una nueva manera de encontrar tu próxima escucha.",
        "skip": "Ir al contenido", "navHow": "Cómo funciona", "navBeta": "Aviso de la beta", "langLabel": "Idioma de la web",
        "hero": "Tu próximo podcast empieza con alguien a quien sigues.",
        "intro": "Sigue a personas. Descubre los episodios de los podcasts que siguen. Un feed hecho con tu gente, no con una lista anónima.",
        "cta": "Avísame cuando abra la beta", "building": "Podlinker está en construcción",
        "diagramHeading": "Así se construye tu feed", "youFollow": "Tú sigues a", "people": "personas", "theyFollow": "Ellas siguen", "podcasts": "podcasts", "youDiscover": "Tú descubres", "episodes": "episodios",
        "person1": "Mar", "person2": "Pol", "show1": "Fora de mapa", "show2": "Herbari", "sampleEpisode": "Un nuevo episodio", "sampleSource": "de Fora de mapa", "sampleLabel": "Ejemplo ficticio",
        "note": "Seguir un podcast no significa haber escuchado ni recomendado todos sus episodios.",
        "footer": "Descubrir podcasts, de persona a persona.", "brandAria": "Podlinker, inicio", "footerStatus": "Una nueva manera de descubrir podcasts. En construcción.",
        "betaEyebrow": "LISTA DE INTERÉS", "betaTitle": "Un correo cuando estemos listos.", "betaBody": "Apúntate para recibir solo el aviso cuando abramos la beta de Podlinker. Sin boletín ni correos entre medias.",
        "confirmedTitle": "Ya estás en la lista", "confirmedBody": "Hemos confirmado tu correo. Te avisaremos cuando abramos la beta. No tienes que hacer nada más.", "confirmedBack": "Volver a Podlinker", "confirmedPath": "beta-confirmada",
    },
    "en": {
        "title": "Podlinker — Discover podcasts through your people",
        "description": "Follow people and discover episodes from the podcasts they follow. Podlinker is a new way to find your next listen.",
        "skip": "Skip to content", "navHow": "How it works", "navBeta": "Beta notice", "langLabel": "Website language",
        "hero": "Your next podcast starts with someone you follow.",
        "intro": "Follow people. Discover episodes from the podcasts they follow. A feed shaped by your people, not an anonymous chart.",
        "cta": "Let me know when beta opens", "building": "Podlinker is in the making",
        "diagramHeading": "How your feed takes shape", "youFollow": "You follow", "people": "people", "theyFollow": "They follow", "podcasts": "podcasts", "youDiscover": "You discover", "episodes": "episodes",
        "person1": "Mar", "person2": "Pol", "show1": "Fora de mapa", "show2": "Herbari", "sampleEpisode": "A new episode", "sampleSource": "from Fora de mapa", "sampleLabel": "Fictional example",
        "note": "Following a podcast doesn't mean someone has listened to or recommended every episode.",
        "footer": "Discover podcasts, person to person.", "brandAria": "Podlinker, home", "footerStatus": "A new way to discover podcasts. In the making.",
        "betaEyebrow": "INTEREST LIST", "betaTitle": "One email when we’re ready.", "betaBody": "Sign up to get a single notice when the Podlinker beta opens. No newsletter or emails in between.",
        "confirmedTitle": "You're on the list", "confirmedBody": "Your email is confirmed. We'll let you know when beta opens. There's nothing else to do.", "confirmedBack": "Back to Podlinker", "confirmedPath": "beta-confirmed",
    },
}

LANG_NAMES = {"ca": "Català", "es": "Español", "en": "English"}

for locale, raw in COPY.items():
    c = {key: escape(value, quote=True) for key, value in raw.items()}
    embed_path = ROOT / "embeds" / f"{locale}.html"
    if not embed_path.exists() and os.getenv("PODLINKER_PREVIEW_WAITLIST") != "1":
        raise RuntimeError(f"Missing reviewed Mailjet embed: {embed_path}")
    form_embed = embed_path.read_text() if embed_path.exists() else "<!-- Mailjet form embed pending -->"
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
      <nav class="header-nav" aria-label="{c["navHow"]}"><a href="#com-funciona">{c["navHow"]}</a><a href="#beta">{c["navBeta"]}</a></nav>
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
            <a class="button button-lime" href="#beta">{c["cta"]} <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-5-5 5 5-5 5"/></svg></a>
          </div>
        </div>
        <p class="hero-state"><span class="state-signal" aria-hidden="true"></span>{c["building"]}</p>
      </div>
    </section>
    <section class="mechanism" id="com-funciona" aria-labelledby="diagram-title">
      <div class="wrap">
        <div class="section-heading"><h2 id="diagram-title">{c["diagramHeading"]}</h2><span class="section-rule" aria-hidden="true"></span></div>
        <div class="network-board" aria-label="{c["diagramHeading"]}">
          <div class="board-column people-column"><div class="board-caption">{c["youFollow"]} <strong>{c["people"]}</strong></div><div class="people-list"><div class="person"><span class="avatar avatar-coral" aria-hidden="true">M</span><span>{c["person1"]}</span></div><div class="person"><span class="avatar avatar-sea" aria-hidden="true">P</span><span>{c["person2"]}</span></div></div></div>
          <div class="board-arrow" aria-hidden="true"><span></span></div>
          <div class="board-column shows-column"><div class="board-caption">{c["theyFollow"]} <strong>{c["podcasts"]}</strong></div><div class="show-list"><div class="show show-coral"><span class="show-type">PODCAST</span><strong>{c["show1"]}</strong></div><div class="show show-gold"><span class="show-type">PODCAST</span><strong>{c["show2"]}</strong></div></div></div>
          <div class="board-arrow" aria-hidden="true"><span></span></div>
          <div class="board-column episode-column"><div class="board-caption">{c["youDiscover"]} <strong>{c["episodes"]}</strong></div><div class="episode-example"><div class="episode-index"><span>FEED</span></div><strong>{c["sampleEpisode"]}</strong><span>{c["sampleSource"]}</span><small>{c["sampleLabel"]}</small></div></div>
        </div>
        <p class="board-note">{c["note"]}</p>
      </div>
    </section>
    <section class="waitlist" id="beta" aria-labelledby="beta-title">
      <div class="wrap waitlist-grid">
        <div class="waitlist-copy"><p class="waitlist-eyebrow">{c["betaEyebrow"]}</p><h2 id="beta-title">{c["betaTitle"]}</h2><p>{c["betaBody"]}</p></div>
        <div class="waitlist-form">{form_embed}</div>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="wrap footer-inner"><div><span class="footer-brand">podlinker<span>.</span></span><p>{c["footer"]}</p></div><small>{c["footerStatus"]}</small></div></footer>
</body>
</html>
'''
    (ROOT / locale / "index.html").write_text(html)

    confirmed = f'''<!doctype html>
<html lang="{locale}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#3047cd">
  <title>{c["confirmedTitle"]} — Podlinker</title>
  <link rel="icon" type="image/svg+xml" href="../../assets/favicon.svg">
  <link rel="stylesheet" href="../../assets/style.css">
</head>
<body class="confirmation-page">
  <main class="confirmation-main">
    <div class="wrap confirmation-content">
      <a class="brand" href="../" aria-label="{c["brandAria"]}"><span class="brand-mark"><img src="../../assets/logo.svg" alt="" width="28" height="28"></span><span>podlinker<span class="brand-dot">.</span></span></a>
      <h1>{c["confirmedTitle"]}</h1>
      <p>{c["confirmedBody"]}</p>
      <a class="button button-lime" href="../">{c["confirmedBack"]} <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-5-5 5 5-5 5"/></svg></a>
    </div>
  </main>
</body>
</html>
'''
    confirmed_dir = ROOT / locale / raw["confirmedPath"]
    confirmed_dir.mkdir(parents=True, exist_ok=True)
    (confirmed_dir / "index.html").write_text(confirmed)

(ROOT / "index.html").write_text('''<!doctype html><html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Podlinker</title><script src="assets/redirect.js"></script></head><body><p><a href="ca/">Podlinker · Català</a></p><p><a href="es/">Español</a> · <a href="en/">English</a></p></body></html>''')

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}/{locale}/</loc></url>\n" for locale in COPY)
    + '</urlset>\n'
)
