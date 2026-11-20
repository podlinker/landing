# Podlinker — product context for the landing

Canonical product decisions live in [podlinker/project](https://github.com/podlinker/project), especially `PRODUCT.md`, `DECISIONS.md` and `AUTH.md`. This file is a concise brief for the public landing; when facts differ, the canonical project repository wins.

Podlinker is a social network for discovering podcast episodes through people you follow and the podcasts they follow. The primary feed shows all new episodes of those podcasts, deduplicated when multiple followed people follow the same podcast. Following a podcast never implies listening to or recommending each episode. Explicit recommendations belong to a separate later highlights experience.

People have varied podcast collections. The visitor follows people, sees the podcasts in their orbit, and discovers episodes through that network. The public catalog is provider-independent. Login will use a Podlinker account with email and one-time code. Spotify is out of scope.

Separately from the social feed, a person can save episodes from different podcasts and opt in to a personal RSS feed of those saved episodes for their usual podcast player. Adding or removing a saved episode updates that feed. This is available only in the closed staging pilot, not a public launch; see the canonical [feature status](https://github.com/podlinker/project/blob/main/FEATURES.md).

The web must support Catalan, Spanish and English. The visitor's language choice persists; browser language is the first-visit default and Catalan is the fallback.

Until the service is ready, this landing explains the proposition without linking to the staging demo. The diagram uses fictional examples to explain the model, not real account activity. Do not offer a fake signup, imply a release date, invent real user endorsements, or claim an episode was listened to or recommended because someone follows its podcast.

Shared assets and the approved corporate identity guide live in [`podlinker/artwork/BRAND.md`](https://github.com/podlinker/artwork/blob/main/BRAND.md). The `DESIGN.md` files in app and landing describe their current interfaces, not a separate brand palette or typography. The landing may be more expressive than the operating app while remaining recognizably part of the same product.
