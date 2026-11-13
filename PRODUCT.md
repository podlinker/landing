# Podlinker — product context for the landing

Canonical product decisions live in [podlinker/project](https://github.com/podlinker/project), especially `PRODUCT.md`, `DECISIONS.md` and `AUTH.md`. This file is a concise brief for the public landing; when facts differ, the canonical project repository wins.

Podlinker is a social network for discovering podcast episodes through people you follow and the podcasts they follow. The primary feed shows all new episodes of those podcasts, deduplicated when multiple followed people follow the same podcast. Following a podcast never implies listening to or recommending each episode. Explicit recommendations belong to a separate later highlights experience.

People have varied podcast collections. The visitor follows people, sees the podcasts in their orbit, and discovers episodes through that network. The public catalog is provider-independent. Login will use a Podlinker account with email and one-time code. Spotify is out of scope.

The web must support Catalan, Spanish and English. The visitor's language choice persists; browser language is the first-visit default and Catalan is the fallback.

Until the service is ready, this landing explains the proposition and can link to the public staging demo. The staging social data is fictional and its follow/save interactions are browser-local, not real account state. Do not offer a fake signup, imply a release date, invent real user endorsements, or claim an episode was listened to or recommended because someone follows its podcast.

Visual identity for the product app is defined in `podlinker/app/DESIGN.md`: radio-programme-guide editorial character, programme blue `#3047cd`, cool paper `#f4f6f5`, ink `#182334`, signal lime `#e5f468`, Barlow Condensed display, flat ruled composition and compact microphone mark. The landing may be more expressive than the operating app while remaining recognizably part of this system.
