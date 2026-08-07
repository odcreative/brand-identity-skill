# Presentation Formats

*How* the work is shown is half the craft. The reference library uses a recurring set of presentation formats. Match the format to the moment. The two signature deliverables — the **bento brand board** and the **guidelines deck** — have ready HTML templates in `assets/`.

## 1. Bento brand board  ★ signature quick-win

The single most-used format in the library (*Kidly*, *Metriva*). A grid of **rounded tiles in mixed sizes** on a **tinted brand background**, packing the whole identity onto one shareable canvas: primary logo tile, colour tiles, a mockup or two, the submark/badge, a tagline, an app icon, a photographic lifestyle tile.

Rules that make it read right:
- **Rounded corners** (16–28px), consistent gap (12–20px), tinted ground (a soft brand tint or near-black).
- **Mixed tile sizes** — one hero logo tile ~2×2, supporting tiles 1×1 / 2×1. Asymmetry with balance.
- Alternate **fills**: some tiles are brand-colour with reversed logo, some are white, one or two are photographic/mockup.
- One tile is the **wordmark large**; one is the **submark/app icon**; one carries the **tagline**.
- → Use `assets/brand-board.html`. Deliver via the `Artifact` tool (shareable page) after loading `artifact-design`.

## 2. Guidelines deck  ★ signature full deliverable

The structured, numbered, multi-screen document (*Radesk*, 36 screens). Cover → index → introduction/vision → logo (construction, clearspace, variants) → colour (primary/secondary/grayscale/on-bg) → typography → icon/app → imagery → applications. Full section spec in `guidelines-structure.md`.
- → Use `assets/brand-guidelines.html`. Landscape 16:9 sections, one idea per screen, numbered `1.0 / 2.0 …`. Deliver as an `Artifact` and/or print to PDF.

## 3. Hero logo over photography

The mark, knocked out in white (or brand tint), centred over a full-bleed, on-brand photograph — *Ecovine*'s sprout over the aerial green field. Used as an opener, section divider, or social hero. Add a small ©/™ for polish. Needs a legibility scrim if the photo is busy. High emotional impact, low information.

## 4. Stationery flat-lay

Top-down arrangement of business card (front + back), letterhead, envelope, comp slip — on a **flat brand-colour ground** (*Dentcor* on navy). Soft realistic shadows, slight overlap, one card angled to show the reverse. The classic "the brand is real" shot. See `mockup-catalog.md`.

## 5. Packaging / product repeat-grid

The product, branded, **tiled in a repeating grid** on a brand-colour background (*Ecovine* produce trays on green). Shows range and pattern at once; great for FMCG, food, cosmetics. Pair with the icon-system pattern on labels/sleeves.

## 6. Real-environment mockups

The brand in the world: storefront + window graphics (*burger* window-glass), 3D signage, wayfinding, billboards / city advertising, vehicle livery. Grounds the identity at human scale and sells it to stakeholders. Prefer daylight, real architecture, believable placement.

## 7. Moody / editorial scenes

Dark, cinematic, single-subject shots — a person in dark clothing holding a card/box, low-key light, monochrome props (*Dusk* mockups). Signals premium/fashion/agency. Use for hero and cover imagery when the brand is upscale or design-led.

## 8. Icon & app presentation

App icon on a device home screen, in the browser tab, as macOS/iOS icons, and social avatars (Radesk's "Applications / Icon" pages). Show the submark surviving at real UI sizes and inside platform masks (squircle, circle).

## 9. Concept-direction deck  ★ the decision moment

When step 3 hands over 2–3 concepts, the deliverable is a **deck**, not a folder of SVGs. Working structure, one section per screen:

**cover → brief recap → one full page per direction → decision page.**

Each direction page carries the mark large, its lockup family small, the typeface it's built from, and one sentence on the idea. Name the directions (`01 SPEAR`, `02 SEAL`, `03 CANOPY`) — clients discuss names, not file paths.

The decision page states **your recommendation**, with a primary and a secondary pick and the reason. A designer who presents three equal options makes the client do the design work. Nothing downstream (palette rollout, applications, guidelines) starts until this page is answered.

---

## Capturing an HTML deck headlessly

The decks are HTML, so client-ready images come from Chrome headless. Rules learned the hard way:

- **Fix the page height:** `.page { height: 100vh }`. Left as `min-height`, grid rows overflow into the next section.
- **Don't grow `--window-size` to fit a long page.** `100vh` scales with the window, so a taller window changes the layout you're trying to capture. Keep `1440x900` and isolate one section per shot by injecting `section.page:not(:nth-of-type(N)) { display: none }`.
- **`#fragment` navigation does not work headless** — the capture lands on page 1 regardless. Same fix: isolate by CSS, not by anchor.
- **Iframes taller than ~8000px don't rasterise.** For long-page captures, use an anchored iframe with a ~2500px window and repeat down the page.
- **CDP `captureBeyondViewport` inflates `vh`-based layouts.** Prefer section isolation over full-page capture whenever the design uses viewport units.
- Serve with `python3 -m http.server --directory <dir>` — never `cd` first, the harness resets the shell's cwd between calls.

---

## Choosing per request

| The user wants… | Lead with |
|---|---|
| A fast, shareable overview | Bento brand board (1) |
| A client-ready system doc | Guidelines deck (2) |
| An emotional reveal / social hero | Hero over photography (3) |
| "Make it feel real" | Stationery flat-lay (4) + real-environment (6) |
| Retail / product brand | Packaging repeat-grid (5) |
| Premium / fashion / agency | Moody editorial (7) |
| A digital product | Icon & app presentation (8) |
| A pick between logo concepts | Concept-direction deck (9) |

Default **Standard** delivery = brand board (1) + stationery (4) + 2–3 mockups (4/6) + guidelines deck (2).

## Craft constants across all formats

- Generous negative space; let the mark breathe.
- Consistent corner radius and shadow language throughout a set.
- Real, soft, directional shadows on mockups — never harsh drop shadows.
- One accent moment per composition; everything else neutral.
- Brand-colour full-bleed grounds for impact; white grounds for clarity.
- Every text string on a mockup is real brand copy (name, tagline, contact) — never lorem where a real value exists.
