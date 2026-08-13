# Typography

The reference identities share a typographic personality: **modern, geometric or grotesque sans-serifs, a wide weight range, generous spacing on labels, and confident large type in use.** Type does most of the heavy lifting once the logo is set.

## Type roles

Define a small, deliberate set:

- **Display / headline** — the voice. Big, characterful (Manrope-class geometric grotesque; rounded soft-sans for playful brands).
- **Body / text** — quiet and legible at small sizes. Often the same family at a lighter weight, or a neutral companion.
- **Mono / label / eyebrow** — for kickers, tags, spec numbers, UI labels. Wide-tracked uppercase reads as "designed" (the `Construction.` / `Clearspace.` labels in Radesk).

Two families is plenty; one super-family used across weights is often better (Radesk uses **Manrope** ExtraLight → ExtraBold for everything). One family, many weights = cohesion.

## Default recommendations (safe, high-quality, widely available)

Pick to match personality. All are free/near-ubiquitous unless noted:

| Personality | Display | Body | Notes |
|---|---|---|---|
| Modern tech / SaaS | **Manrope**, Space Grotesk, Geist | Inter, Manrope | Geometric grotesque; the Radesk look |
| Premium / corporate | **Neue-grotesque** (Helvetica Now, Inter, Söhne\*) | Inter | Tight, neutral, expensive |
| Natural / humanist | **Hanken Grotesk**, Figtree, DM Sans | Source Sans | Warm, rounded terminals |
| Playful / youthful | **Baloo 2**, Fredoka, Quicksand | Nunito | Rounded, bouncy (Kidly energy) |
| Editorial / luxury | **Fraunces**, Canela\*, Playfair Display | Inter, Lora | High-contrast serif display + clean sans body |
| Wordmark craft | Custom-drawn from a geometric base | — | Hand-tune the name itself |

\* Premium/self-hosted fonts (Söhne, Canela, Gilroy, Satoshi, Clash…) are available via `ui-ux-pro-max`'s font library — use them when licensing is fine and the brand warrants it. Otherwise default to the Google-hosted picks above so deliverables render everywhere.

## A second, technical face — scoped hard

Some brands need a face for machine-ish strings: policy numbers, dates, reference codes, versal labels. Venüs Sigorta pairs **Manrope** (300/500/800) with **IBM Plex Mono**, and the rule shipped with it is what makes it work: **mono is for data strings only — never headings, never body.** An unscoped second family becomes a second voice within a week.

Related discipline from the same system: **hierarchy comes from weight, not colour.** Once colour carries hierarchy, the accent stops being an accent.

## Licensed display faces: name the swap at concept time

If a concept is built on a licensed font (Gilroy, Söhne, Canela, Clash…), say so *on the direction page* and name the free substitute it would move to if that direction wins (Gilroy → Poppins/Outfit). Discovering the licence question after the client has chosen turns a decision into a re-draw.

## Type scale

Use a modular scale (ratio ~1.25 minor-third for UI, ~1.333 perfect-fourth for editorial). Example (16px base, 1.25):

`12 · 14 · 16 · 20 · 25 · 31 · 39 · 49 · 61 · 76`

Define named steps and their role:
- **Display XL / L** — hero statements ("Built for Smarter Systems.").
- **H1–H3** — section and card headings.
- **Body L / M / S** — running text.
- **Label / Caption** — eyebrows, tags, legal.

## Spacing & setting rules

- **Tracking:** tighten large display (−1% to −3%); widen small uppercase labels (+6% to +12%). This one move accounts for much of the "premium" feel.
- **Leading:** ~1.1–1.2 for display, ~1.4–1.6 for body.
- **Measure:** 45–75 characters per line for body.
- **Alignment:** left-aligned by default; centre only for badges/short statements.
- **Case:** Sentence case for reading; UPPERCASE (tracked) for labels/eyebrows; the wordmark sets its own rule.
- **Weight contrast:** pair a light/regular body against a semibold/bold display — the Radesk specimen shows the full ramp (ExtraLight → ExtraBold) precisely to demonstrate this range.

## Specimen page (for guidelines)

Show: the family name, all weights (with a big `Aa` and the alphabet), the type scale with px/pt values, and an **in-use** block — a real headline + paragraph set in the brand, exactly as Radesk's "Primary Typography" and "In-use Typography" pages do. Prove the type works in context, not just as a chart.

## Delivery

- Name families + weights, provide fallbacks and `@font-face` / CSS `font-family` stacks.
- Note licensing and download links (Google Fonts URL, or vendor).
- The HTML templates expose `--font-display` and `--font-body` variables — set them once.
