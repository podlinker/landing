---
name: Podlinker Landing
description: A public introduction to podcast discovery through the people you follow
colors:
  programme-blue: "#3047cd"
  programme-blue-deep: "#2336a9"
  ink: "#182334"
  cool-paper: "#f4f6f5"
  signal-lime: "#e5f468"
  muted-ink: "#53616c"
  rule: "#cbd4d5"
  people-field: "#f9e4d9"
  podcast-field: "#f5edc8"
  player-field: "#e6eaff"
typography:
  display:
    fontFamily: "Barlow Condensed, Impact, sans-serif"
    fontSize: "clamp(62px, 7.1vw, 96px)"
    fontWeight: 800
    lineHeight: 0.91
    letterSpacing: "-0.022em"
  title:
    fontFamily: "Barlow Condensed, Impact, sans-serif"
    fontSize: "clamp(39px, 4vw, 55px)"
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: "-0.015em"
  feature:
    fontFamily: "Barlow Condensed, Impact, sans-serif"
    fontSize: "clamp(52px, 6.1vw, 82px)"
    fontWeight: 800
    lineHeight: 0.94
    letterSpacing: "-0.022em"
  body:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.58
  label:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "14px"
    fontWeight: 700
rounded:
  square: "0px"
spacing:
  compact: "8px"
  regular: "12px"
  wide: "24px"
components:
  button-lime:
    backgroundColor: "{colors.signal-lime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "0 19px"
    height: "57px"
  button-lime-hover:
    backgroundColor: "#f1faad"
    textColor: "{colors.ink}"
  language-choice-active:
    backgroundColor: "{colors.signal-lime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    height: "44px"
  text-link:
    textColor: "#ffffff"
    height: "44px"
  header-nav-link:
    textColor: "#ffffff"
    height: "44px"
  mechanism-stage:
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "17px 19px"
    minHeight: "137px"
  episode-stage:
    backgroundColor: "{colors.signal-lime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "14px 17px"
---

# Design System: Podlinker Landing

This file records the **current landing implementation**, not the corporate identity. Shared assets and approved cross-product color, typography and tone rules live in [`podlinker/artwork/BRAND.md`](https://github.com/podlinker/artwork/blob/main/BRAND.md). Some landing tokens below predate that approval; they document deployed behavior, not an alternative official palette. Align them when editing the landing. The master-logo specifications remain open.

## Overview

**Creative North Star: "La graella d'escoltes"**

The public landing extends the app's current radio-programme-guide visual language into a more expressive, editorial introduction. Programme blue carries the header and opening statement; condensed display type gives the proposition its voice. The mechanism board makes the social relationship visible as a sequence of people, podcasts and episodes. This is a flat, ruled composition, not a stack of floating cards.

The page moves from the programme-blue opening to the cool-paper mechanism board, then a ruled Highlights band for explicit recommendations, a white editorial statement and flat three-stage diagram for the private saved-episode RSS feed, and the programme-blue footer. A compact microphone mark anchors the brand. The diagrams use abstract stages rather than fabricated people, titles or social actions; the feed diagram must not imply that following a podcast means listening to or recommending every episode.

**Key Characteristics:**

- Oversized condensed headings against plain, high-contrast color fields.
- One ruled, three-stage network diagram instead of decorative podcast imagery.
- Signal lime reserved for the in-page call to action, selected language and the episode/RSS stages.
- Square buttons and content blocks; the player symbol is circular.

## Colors

### Primary

- **Programme blue** (`#3047cd`) establishes the header, hero and footer, and appears in diagram arrows. **Programme blue deep** (`#2336a9`) supplies diagram symbols.
- **Signal lime** (`#e5f468`) identifies the in-page action, selected language and episode/RSS stages. The button hover lightens to `#f1faad`.

### Secondary

- Pale coral and gold fields distinguish the first two stages of the abstract network diagram; pale lavender distinguishes the player's destination. They are not a rule for real podcast covers.

### Neutral

- **Ink** (`#182334`) carries reading text. **Cool paper** (`#f4f6f5`) is the default reading surface.
- **Muted ink** (`#53616c`) is used for diagram captions and explanatory notes. **Rule** (`#cbd4d5`) separates ruled content.
- White is the text color on blue and ink fields.

**The Signal Color Rule.** Lime indicates a specific action, selection or outcome; it is not a general background accent.

## Typography

Barlow Condensed is self-hosted at weights 700 and 800 for the major headings and diagram statements. The system sans stack serves paragraphs, controls and metadata. The type pairing matches the product app while allowing larger, more declarative landing-page headings.

- **Display** (800; `clamp(62px, 7.1vw, 96px)`; `0.91` line-height) carries the hero proposition.
- **Title** (700; `clamp(39px, 4vw, 55px)`; `0.98` line-height) labels the mechanism section.
- **Feature** (800; `clamp(52px, 6.1vw, 82px)`; `0.94` line-height) carries the personal-podcast statement in the white band.
- **Body** uses a familiar system sans for the hero introduction and section explanations.
- **Label** (14px and 700 in navigation; smaller, heavier labels in the diagram) keeps navigation and stage metadata compact.

**The Condensed Voice Rule.** Use Barlow Condensed for prominent propositions and stage statements; keep explanatory reading in the system sans.

## Layout

The shared wrapper has a maximum width of `1280px` and `44px` side gutters on desktop. The hero is a wide blue field with a large heading above a description-and-action row. Below it, a five-track mechanism board reads as people followed → arrow → their shared podcasts → arrow → new episodes, enclosed by two strong ink rules. The Highlights band pairs a direct headline with a plain-language contrast between explicit recommendations and the automatic feed; it has no decorative card. The white personal-podcast band pairs editorial copy with a three-stage diagram: saved episodes → private RSS → usual podcast player. The final stage is explanatory, not a fake player UI. The footer follows it directly.

At `1050px`, the hero description and action stack. At `760px`, the wrapper narrows to `18px` side gutters, the navigation wraps below the brand, and all diagrams become vertical sequences. The Highlights and personal-feed bands stack heading above their diagrams. A `390px` adjustment tightens header and diagram text. Controls retain at least the observed `44px` navigation/language hit height where applicable.

## Elevation & Depth

There are no resting shadows. Color fields, two-pixel diagram and section rules, one-pixel row separators, and generous vertical spacing establish the hierarchy. Focus uses a `3px` lime outline with a `4px` offset; it is a state cue, not an elevation effect.

**The Flat Programme Rule.** Separate ideas with rules, spacing and purposeful field changes; do not add ambient card shadows to this system.

## Shapes

Buttons, language selections and diagram blocks have square corners. The square white brand-mark tile contains the existing microphone asset. The player's play symbol is circular. The board's horizontal-to-vertical arrows are line drawings, not icon tiles.

## Components

### In-page action

The primary call to action is a square lime link to the mechanism section (`min-height: 57px`, `padding: 0 19px`) with a trailing inline arrow. It lightens on hover and uses the shared lime focus outline.

### Header and language control

The header stays visible at the top while scrolling, with enough scroll offset that in-page section links do not hide content beneath it. It has a blue field, compact brand lockup and underlined-on-hover navigation. CA / ES / EN sits in a thin outlined group; the active language is filled lime. On narrow screens, navigation wraps to its own row without hiding the language choices.

### Mechanism board

Three flat stages describe the actual relationship: the listener's chosen network, the podcasts those people share, and the new episodes that reach the listener's feed. No account names, show titles or episode titles are invented. Arrows express the relationship between columns and rotate with the mobile sequence.

### Highlights and saved episodes

The Highlights band directly explains that it contains episodes explicitly recommended by followed people, unlike the main feed of new episodes from podcasts they follow. It does not invent a recommendation by any person. Saved episodes form a separate, private selection; their diagram leads to one private RSS channel and then the listener's existing podcast player. Flat color fields and arrows make the outcome scannable without pretending Podlinker plays audio itself.

## Do's and Don'ts

### Do:

- **Do** keep people, followed podcasts and newly discovered episodes legible as separate stages.
- **Do** align new landing work with the approved brand palette and headline typography; keep existing deployed colors documented honestly until the landing itself is revised.
- **Do** use flat rules and color fields to organize information, including on mobile.

### Don't:

- **Don't** make a podcast follow look like a listening event or recommendation.
- **Don't** fabricate account activity or use real public-profile data as a promotional endorsement without a separate decision.
- **Don't** replace the square editorial language with rounded floating cards or ambient shadows.
