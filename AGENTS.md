# Instruccions per a agents — `podlinker/landing`

## Funció i funcionament

Web públic de presentació, separat de l'app i de staging. La versió publicada és **HTML/CSS/JS estàtic** en català, castellà i anglès, generat per `scripts/build.py`; `assets/` conté estils, scripts, logo i imatges socials, i `.github/workflows/pages.yml` publica GitHub Pages des de `main`. Els fitxers Next.js antics continuen al repositori, però no formen part d'aquest desplegament. Llegiu `README.md` abans de canviar el flux de publicació.

Editeu el generador i regenereu les rutes `/ca/`, `/es/`, `/en/`, `robots.txt` i `sitemap.xml` amb `python3 scripts/build.py`; reviseu els HTML generats i els metadades per idioma. Si canvia el titular, actualitzeu també les tres imatges OG. Manteniu la proposta clara: persones → podcasts → episodis; un follow no equival a escolta ni recomanació. La landing explica funcions reals amb diagrames abstractes, sense inventar persones, podcasts, capítols o activitat social. No afegiu un signup, analítica, promeses de llançament o enllaç a staging com si fossin funcionalitats aprovades.

Per disseny, consulteu `DESIGN.md` per aquesta landing i [artwork/BRAND.md](https://github.com/podlinker/artwork/blob/main/BRAND.md) per als actius i criteris transversals. La direcció de marca és vigent des del 2026-11-17, però aquesta aprovació no modifica automàticament els tokens de la landing ni defineix el logotip mestre.

## Mapa de fonts

- [Project](https://github.com/podlinker/project) governa producte, decisions, login i [estat real](https://github.com/podlinker/project/blob/main/STATUS.md); el [tauler](https://github.com/orgs/podlinker/projects/2) ordena la feina. No feu de `PRODUCT.md` local una segona font de veritat.
- [Artwork](https://github.com/podlinker/artwork) és la casa dels logos i la guia de marca vigent; `DESIGN.md` d'aquí és local a la landing.
- [App](https://github.com/podlinker/app) és el producte web; [backend](https://github.com/podlinker/backend) és l'API; [ideas](https://github.com/podlinker/ideas) conté idees no aprovades.
