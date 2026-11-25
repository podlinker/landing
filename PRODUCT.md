# Podlinker — product context for the landing

<!-- impeccable:product-schema 1 -->

Canonical product decisions live in [podlinker/project](https://github.com/podlinker/project), especially `PRODUCT.md`, `DECISIONS.md` and `AUTH.md`. This file is a concise brief for the public landing; when facts differ, the canonical project repository wins.

## Platform

web

## Users

Podcast listeners looking for something to hear next through people they choose to follow.

## Product Purpose

The landing introduces Podlinker and explains how following people leads to discovering episodes from the podcasts they follow.

## Positioning

Podlinker is a social network for discovering podcast episodes through people you follow and the podcasts they follow. The primary feed shows all new episodes of those podcasts, deduplicated when multiple followed people follow the same podcast. Following a podcast never implies listening to or recommending each episode. Explicit recommendations are attributed actions in the main feed and are also shown together in Highlights, which follows the profile's existing visibility. The closed pilot also offers a focused discovery view of podcasts shared by a listener’s network that are not already in their library.

## Operating Context

The web must support Catalan, Spanish and English. The visitor's language choice persists; browser language is the first-visit default and Catalan is the fallback.

This public landing is separate from the closed staging pilot and does not link to the staging demo.

## Capabilities and Constraints

People have varied podcast collections. The visitor follows people, sees the podcasts in their orbit, and discovers episodes through that network. The public catalog is provider-independent. The closed pilot uses Podlinker accounts with email and one-time codes. Spotify is out of scope.

Separately from the social feed, a person can save episodes from different podcasts and opt in to a personal RSS feed of those saved episodes for their usual podcast player. Adding or removing a saved episode updates that feed. This is available only in the closed staging pilot, not a public launch; see the canonical [feature status](https://github.com/podlinker/project/blob/main/FEATURES.md).

## Brand Commitments

Shared assets and the approved corporate identity guide live in [`podlinker/artwork/BRAND.md`](https://github.com/podlinker/artwork/blob/main/BRAND.md). The `DESIGN.md` files in app and landing describe their current interfaces, not a separate brand palette or typography. The landing may be more expressive than the operating app while remaining recognizably part of the same product.

## Evidence on Hand

The linked feature status records which capabilities are available in the closed pilot. The landing's diagrams describe real product behavior; they are abstract, not screenshots or invented account content.

## Product Principles

- Distinguish podcast follows, explicit recommendations and a listener's private saved-episode feed.
- Explain the real product without fabricated social activity, endorsements, a fake signup or a release date.
- Keep Catalan, Spanish and English available, and do not add an "in construction" status badge.
