---
name: brand-identity
description: >-
  Design a complete logo and brand identity, the way a senior brand designer would.
  Use this whenever the user asks to "prepare brand identity" / "prepare brand design" /
  "create a brand" / "design a logo and branding" for a named brand (e.g. "prepare brand
  identity for Acme"), or in Turkish "marka kimliği hazırla" / "marka tasarımı hazırla" /
  "logo tasarla". Delivers strategy, a logo system (marks, lockups, construction, clearspace,
  variants), colour system, typography, a bento brand board, realistic mockups, and a full
  brand-guidelines deck — in the clean, modern, editorial style of the reference library
  (emblem/negative-space/geometric-monogram logos; anchor+accent palettes; Radesk-style
  guidelines; Kidly/Metriva bento boards). Not for editing an existing brand's single asset —
  use the `design` or `banner-design` skills for one-off graphics.
metadata:
  author: OD Creative
  version: "1.1.0"
---

# Brand Identity

Act as a senior logo & brand-identity designer. When the user says **"prepare brand identity / brand design for [X]"**, run the pipeline below and produce a coherent, professional identity system — not a single logo. The aesthetic target is the curated reference library: **clean, modern, editorial, restrained**; opinionated anchor+accent colour; geometric/negative-space/emblem marks; and the two signature deliverables — a **bento brand board** and a **Radesk-style guidelines deck**.

**Primary visual calibration → `references/reference-library.md` + `references/exemplars/`.** Before designing, open 4–6 exemplar images matching the brief's sector to lock the look. The house style, distilled from a ~1,200-image archive: **bold two-colour (duotone) system + an idea-driven mark (friendly mascot *or* clean negative-space/geometric device) + everything shown on a colour-matched mockup.** Cream (`#FEFAE0`-family), not white, is the recurring neutral.

**Reality check → `references/logo-archive.md`.** 1,402 *shipped* marks (searchable via `scripts/logo_archive.py`) answer what a category actually looks like, so the anchor colour and lockup proportions are chosen against evidence, not vibes. The exemplars set the craft bar; the archive stops you accidentally designing the category average — or colliding with a real brand. **Tech/B2B briefs only** (it's 50% devtools) and **never** a source for a client's mark: those logos are their owners' trademarks. See the hard rule in that file.

## Operating principles

- **Strategy before pixels.** A positioning decision precedes every visual one. State assumptions instead of stalling.
- **Design a system, not a picture.** Marks come as families (lockups, submark, variants, clearspace, construction).
- **Be decisive.** Default to the **Standard** scope and make strong choices; offer the user picks at the two real forks (logo concept, colour direction), not at every step.
- **Restraint reads as premium.** 2–3 brand colours, one accent moment per composition, generous space, consistent radius/shadow language.
- **Everything ties to tokens.** One colour/type token block feeds the board, the guidelines, and every generation prompt, so the whole system coheres.
- **Real copy, never lorem** on any mock surface where a real value (name, tagline, contact) exists.

## Workflow

Run these in order. Load the linked reference file when you reach each step (don't preload everything).

1. **Brief, strategy & moodboard** → `references/brand-strategy.md`, `references/reference-library.md`, `references/photography.md`
   Capture or infer: name, sector, offer, audience, 3–5 personality adjectives, positioning, competitors, scope, language. If key facts are missing and the user is available, ask **one** focused round (≤4 questions) via `AskUserQuestion`; otherwise infer and **state the assumptions**. Write the positioning statement, personality→design vector, and 3–5 tagline options. **Open 4–6 `references/exemplars/` images matching the sector** to calibrate the style. Pick **one photographic art-direction** (light&fresh / dark&moody / clinical / playful / warm) and pull a 6–9 image **moodboard** (Unsplash → Magnific stock fallback) to lock the *feeling* before any asset is made.

2. **Visual direction** → `references/logo-system.md`, `references/color-systems.md`, `references/reference-library.md`, `references/typography.md`, `references/logo-archive.md`
   Choose mark archetype(s), a colour system (anchor + accent + neutrals, four-layer palette), and type roles. For the archive look, start from a proven **duotone recipe** (`reference-library.md` §3) and a heavy geometric sans (Gilroy/Montserrat/Outfit). **For tech/B2B briefs, before locking the anchor:** `logo_archive.py palette <sector>` for the convention, then `logo_archive.py search --color <candidate>` — ΔE < 10 against a same-sector brand is a collision, so move or own it deliberately. Record the reasoning in the brief. Lock the **design tokens** (HEX/RGB + font families) now.

3. **Logo concepts** → `references/image-generation.md`, `references/reference-library.md`, `references/presentation-formats.md`
   Produce **2–3 distinct concepts** (different archetypes — e.g. monogram vs. negative-space vs. wordmark). For this style, the core fork is **one character/mascot concept vs. one geometric/negative-space concept** (`reference-library.md` §2). Prefer hand-authored **SVG** for geometric marks; else Figma / Magnific. Always on white/transparent. Past a handful of files, **emit the family from a generator** (`_kaynak/gen_logo.py`) and outline logotypes with uharfbuzz + fontTools rather than shipping `<text>` — `logo-system.md` § "Build the family from a script". Present as a **concept-direction deck** with a named direction per page and a stated recommendation (`presentation-formats.md` §9), then stop: nothing downstream starts before the user picks.

4. **Logo system** → `references/logo-system.md`
   Build out the winner: primary + horizontal + vertical lockups, submark, monogram, construction grid, clearspace (in `X` units), min sizes, and colour variants (full / reversed / mono / on-image). Real shipped proportions to design against (`logo-archive.md`): **submarks are square** (median 1.000), **horizontal lockups ≈4:1** (median 4.23) and ≈4× their own icon's width.

5. **Brand system**
   Finalise the four-layer colour palette (named swatches + HEX/RGB/CMYK), the type scale + in-use specimen, and — for Full scope — an icon/pattern system and imagery art-direction.

6. **Bento brand board** → `assets/brand-board.html`, `references/presentation-formats.md`
   The signature quick deliverable (Kidly/Metriva format). Copy the template, set tokens, drop in the real submark + a mockup. Deliver as an **Artifact** (load `artifact-design` first) or a screenshot.

7. **Applications & mockups** → `references/mockup-catalog.md`, `references/image-generation.md`, `references/photography.md`
   Generate the scope-appropriate set (stationery flat-lay, devices, signage/storefront, packaging, apparel). Magnific with the real logo passed as a `references[]` image; or HTML/CSS compositions; reuse the exact chosen logo everywhere. Ground environmental/lifestyle shots in moodboard photography (Unsplash/stock), graded to the one art-direction. Produce the **hero-over-photography** reveal here too. Need real third-party marks (integrations row, tech-stack slide, "works with" strip)? `logo_archive.py fetch <id>` — as themselves only, never as input to a generator.

8. **Guidelines deck** → `assets/brand-guidelines.html`, `references/guidelines-structure.md`
   The full system doc (Radesk structure): cover → intro/mission/vision → logo (construction, clearspace, variants, misuse) → colour → typography → applications. Deliver as an **Artifact** and/or print-to-PDF.

9. **Package & hand off**
   Save everything to the brand folder (below), then summarise what was produced, the token values, and suggested next steps.

## Scope tiers

- **Essentials** — logo system + colour + type + brand board.
- **Standard** (default) — Essentials + stationery + 3–5 mockups + guidelines deck.
- **Full identity** — Standard + icon/pattern system + packaging + signage/environment + social kit + 30–40-screen guidelines.

## Environment / engines (verified at skill creation)

Route generation per `references/image-generation.md` (Magnific tool cheat-sheet there) and photography per `references/photography.md`. Short version:
- ✅ **Magnific** MCP — the **primary AI engine**: images, true-vector SVG, logo-as-reference mockups, background removal, relight, upscale, brand kits, **and a built-in stock photo catalog** (`stock_search`/`stock_download`). Plus **Figma** (editable vectors/systems), **Canva**, and the **`Artifact`** tool + **HTML** — all work here.
- 📷 **Photography:** prefer **Unsplash MCP** (authentic, free, matches the reference mood). **Not connected by default** — check `claude mcp list`; connect once with an Unsplash Access Key (see `image-generation.md`). Until then, fall back to **Magnific `stock_search`**, which works now.
- ✅ The two HTML deliverables render regardless of any API — the reliable backbone.
- ⚠️ The `design` skill's **Gemini** logo/CIP scripts need `GEMINI_API_KEY` + `google-genai`, **neither present** by default. Confirm before relying on them; otherwise use Magnific/Figma/HTML.
- 📁 **Style-calibration archives the user maintains** — browse for calibration, don't hard-depend on the paths:
  - `~/Downloads/logodesign_man/` — ~1,200 finished LOGODESIGN.MAN identity posts (the source of `references/reference-library.md` and `references/exemplars/`). The **primary** house-style reference; a 16-image captioned subset ships inside the skill so it works even if this path is gone.
  - `~/Downloads/logo-brand-design-skill-gelistirme/` — Behance case studies, UI8 brand-guideline templates, mockup PSDs, reference books.

## Output folder

Save deliverables under a per-brand folder so the user gets a clean package:

```
<brand>-brand/
├─ brief.md                 # strategy, positioning, personality, taglines, tokens
├─ logo/                    # primary, horizontal, vertical, submark, mono, reversed, favicon (SVG + PNG)
├─ brand-board.html         # bento board
├─ brand-guidelines.html    # guidelines deck
├─ mockups/                 # generated application renders
└─ tokens.css               # colour + type variables (single source of truth)
```

Default location: `./<brand>-brand/` in the working directory (or `~/Desktop/<brand>-brand/` if no project context). Confirm the location with the user if ambiguous. Note: the user's memory records brand-specific destinations for some clients (e.g. Integro → `~/Desktop/integro/`) — honour those when the brand matches.

## Complementary skills

- `design` — logo/CIP Gemini generators, icon sets, slides (use its generators when the Gemini path is enabled).
- `banner-design` / `ui-ux-pro-max` — social banners, web UI, premium font library.
- `brand` — brand *voice*, tone, messaging frameworks (pairs with this skill's *visual* system).
- Figma/Canva/Magnific MCP — editable files and AI assets.
