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
  culture-coral: "#f38b74"
  food-gold: "#e6cd5d"
  technology-sea: "#80c1bd"
typography:
  display:
    fontFamily: "Barlow Condensed, Impact, sans-serif"
    fontSize: "clamp(62px, 7.1vw, 96px)"
    fontWeight: 800
    lineHeight: 0.91
    letterSpacing: "-0.022em"
  headline:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(50px, 5.6vw, 77px)"
    fontWeight: 800
    lineHeight: 0.94
    letterSpacing: "-0.021em"
  title:
    fontFamily: "Barlow Condensed, Impact, sans-serif"
    fontSize: "clamp(39px, 4vw, 55px)"
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: "-0.015em"
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
  avatar: "50%"
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
  person-row:
    backgroundColor: "{colors.cool-paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "7px 11px"
    height: "60px"
  podcast-row-coral:
    backgroundColor: "#f9e4d9"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "7px 12px"
    height: "60px"
  episode-example:
    backgroundColor: "{colors.signal-lime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "14px 17px"
---

# Design System: Podlinker Landing

## Overview

**Creative North Star: "La graella d'escoltes"**

The public landing extends the app's radio-programme-guide identity into a more expressive, editorial introduction. Programme blue carries the header and opening statement; condensed display type gives the proposition its voice. The mechanism board makes the social relationship visible as a sequence of people, podcasts and episodes. This is a flat, ruled composition, not a stack of floating cards.

The page alternates a cool paper ground, a pale blue story field and a dark closing field. A compact microphone mark anchors the brand. Examples in the mechanism board are clearly fictional; its visual treatment must not imply that following a podcast means listening to or recommending every episode.

**Key Characteristics:**

- Oversized condensed headings against plain, high-contrast color fields.
- One ruled, three-stage network diagram instead of decorative podcast imagery.
- Signal lime reserved for the call to action, selected language, status dot and example episode.
- Square buttons and content blocks; only person avatars and the status dot are circular.

## Colors

### Primary

- **Programme blue** (`#3047cd`) establishes the header, hero and footer, and appears in diagram arrows and the episode index. **Programme blue deep** (`#2336a9`) supplies the small episode-index text.
- **Signal lime** (`#e5f468`) identifies the main demo action, selected language, status indicator, selection highlight and fictional episode example. The observed button hover lightens to `#f1faad`.

### Secondary

- **Culture coral** (`#f38b74`), **food gold** (`#e6cd5d`) and **technology sea** (`#80c1bd`) come from the app's topic palette. The landing uses lighter tints of coral and sea for person initials, and coral and gold for example podcast rows.

### Neutral

- **Ink** (`#182334`) carries reading text and the closing field. **Cool paper** (`#f4f6f5`) is the default reading surface.
- **Muted ink** (`#53616c`) is used for diagram captions and explanatory notes. **Rule** (`#cbd4d5`) separates people and the alternate story field.
- White is the text color on blue and ink fields. The first story panel uses a pale blue field (`#e7ebfc`), while the second returns to cool paper.

**The Signal Color Rule.** Lime indicates a specific action, selection or example; it is not a general background accent.

## Typography

Barlow Condensed is self-hosted at weights 700 and 800 for the major headings and example titles. The system sans stack serves paragraphs, controls and metadata. The type pairing matches the product app while allowing larger, more declarative landing-page headings.

- **Display** (800; `clamp(62px, 7.1vw, 96px)`; `0.91` line-height) carries the hero proposition.
- **Headline** (800; `clamp(50px, 5.6vw, 77px)`; `0.94` line-height) carries the paired story statements.
- **Title** (700; `clamp(39px, 4vw, 55px)`; `0.98` line-height) labels the mechanism section.
- **Body** (19px; `1.58` line-height in story panels) explains the proposition in a familiar system sans, with a measure up to `55ch` in the story fields.
- **Label** (14px and 700 in navigation; smaller, heavier labels in the diagram) keeps navigation and example metadata compact.

**The Condensed Voice Rule.** Use Barlow Condensed for prominent propositions and named example titles; keep explanatory reading in the system sans.

## Layout

The shared wrapper has a maximum width of `1280px` and `44px` side gutters on desktop. The hero is a wide blue field with a large heading above a description-and-actions row. Below it, a five-track mechanism board reads as person column → arrow → podcast column → arrow → episode column, enclosed by two strong ink rules. Story panels use paired heading and paragraph columns (`1fr .8fr`); the closing field places its statement opposite the demo action.

At `1050px`, the hero state note returns to normal flow and the hero description and actions stack. At `760px`, the wrapper narrows to `18px` side gutters, the navigation wraps below the brand, the mechanism becomes a vertical sequence, and story and closing fields become one column. A `390px` adjustment tightens header and diagram text. Controls retain at least the observed `44px` navigation/language hit height where applicable.

## Elevation & Depth

There are no resting shadows. Color fields, two-pixel diagram and section rules, one-pixel row separators, and generous vertical spacing establish the hierarchy. Focus uses a `3px` lime outline with a `4px` offset; it is a state cue, not an elevation effect.

**The Flat Programme Rule.** Separate ideas with rules, spacing and purposeful field changes; do not add ambient card shadows to this system.

## Shapes

Buttons, language selections, example podcasts and the episode block have square corners. The square white brand-mark tile contains the existing microphone asset. Only person avatars and the small status signal use a `50%` radius. The board's horizontal-to-vertical arrows are line drawings, not icon tiles.

## Components

### Demo action

The primary call to action is a square lime link (`min-height: 57px`, `padding: 0 19px`) with a trailing inline arrow. It lightens on hover and uses the shared lime focus outline. The same action appears on the blue hero and ink closing field. A secondary underlined text link is used only for the in-page mechanism jump.

### Header and language control

The header has a blue field, compact brand lockup and underlined-on-hover navigation. CA / ES / EN sits in a thin outlined group; the active language is filled lime. On narrow screens, navigation wraps to its own row without hiding the language choices.

### Mechanism board

People are ruled rows with circular initial avatars. Podcasts are flat, softly tinted rows with a small uppercase type label and condensed name. The destination episode is a solid lime block with a blue index marker, a condensed example title and a visible fictional-example label. Arrows express the relationship between the three columns; they rotate with the mobile sequence.

### Story and closing fields

The two story sections alternate pale blue and cool paper while preserving the same two-column text structure. The closing field reverses to ink and repeats the demo action with a clearly bordered fictionality label. None of these fields are raised cards.

## Do's and Don'ts

### Do:

- **Do** keep people, followed podcasts and newly discovered episodes legible as separate stages.
- **Do** preserve the app's programme blue, cool paper, ink, signal lime and Barlow Condensed identity.
- **Do** use flat rules and color fields to organize information, including on mobile.

### Don't:

- **Don't** make a podcast follow look like a listening event or recommendation.
- **Don't** turn fictional examples into implied real catalog art, user testimony or account activity.
- **Don't** replace the square editorial language with rounded floating cards or ambient shadows.
