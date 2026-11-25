---
name: Podlinker Landing
description: An editorial public introduction to discovery through the people you follow
colors:
  programme-blue: "#2544bd"
  ink: "#1c2829"
  paper: "#f8f9f6"
  white: "#ffffff"
  rule: "#b5bdb8"
  blue-light: "#e8edfb"
typography:
  display:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(59px, 7.1vw, 96px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "-0.023em"
  feature:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(43px, 5.6vw, 76px)"
    fontWeight: 800
    lineHeight: 0.94
  body:
    fontFamily: "system-ui, sans-serif"
    fontSize: "18px"
    lineHeight: 1.58
  label:
    fontFamily: "system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 700
rounded:
  square: "0px"
components:
  button-primary:
    backgroundColor: "{colors.white}"
    textColor: "{colors.programme-blue}"
    rounded: "{rounded.square}"
    height: "50px"
  language-current:
    backgroundColor: "{colors.white}"
    textColor: "{colors.programme-blue}"
    height: "44px"
  signal-board:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
  highlights:
    backgroundColor: "{colors.blue-light}"
    textColor: "{colors.ink}"
---

# Design System: Podlinker Landing

The shared palette, type pairing and microphone asset are from [the approved Podlinker brand guide](https://github.com/podlinker/artwork/blob/main/BRAND.md). The current lockup is not a master logo.

## Overview

**Creative North Star: "La graella d'escoltes"**

A blue opening pairs an editorial headline with a listening guide: three ruled rows show how people, podcasts and episodes connect. The programme imagery is abstract: no invented activity, cover art or account data. Below it a short discovery story and a focused Highlights block distinguish what arrives automatically from what a person recommends.

**Key Characteristics:**

- Condensed type and high-contrast fields.
- A ruled, three-stage listening guide next to the opening statement.
- A compact sequence from saved episodes to the listener's own player.

## Colors

Blue is the opening, navigation and footer. Ink on paper or white carries longer reading. The pale blue tonal extension marks the discovery outcome and the Highlights view. Rules are neutral; categories and content do not get branded color assignments.

## Typography

Barlow Condensed 800 is used for display, section and diagram titles. The system sans is used for explanations and navigation. Section body copy is set at 18px with a loose line height.

## Layout

The hero and section introductions use two columns on wide screens and one below 800px. The desktop promo board sits beside the headline; the same sequence follows the primary action on phones. The three-stage personal feed switches to a vertical list below 520px. The header stays visible and anchors account for its measured height.

## Elevation & Depth

No shadows. Use surface contrast and thin rules to group content. Keep a visible focus outline on both the blue and paper fields.

## Shapes

Use square surfaces. Circular elements belong to the diagram glyphs, never to wrapper cards. Use the existing black microphone mark unchanged in a white tile.

## Components

- **Listening guide:** ordered people → podcasts → episodes rows with a short text label and an abstract glyph. The third row is tinted to distinguish the outcome.
- **Highlights:** a separate pale-blue section within discovery; the same attributed recommendation can also appear in the main feed.
- **Saved episodes:** a single ruled sequence with an explicit opt-in step, followed by the listener's compatible player. No player controls are simulated.

## Do's and Don'ts

### Do:

- **Do** keep discovery, explicit recommendations and the private selection distinct.
- **Do** describe availability plainly without adding a false signup or an app demo.

### Don't:

- **Don't** imply that following a podcast means listening or recommending.
- **Don't** use false activity, sample account names or simulated product controls.
