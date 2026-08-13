# Colour Systems

The reference identities all use the same architecture: a **small, opinionated core** plus a **structured support system**. Copy this structure; swap the hues.

## The formula: anchor + accent + neutrals

Every case study resolves to:

- **1 deep anchor** — the brand's gravity. Forest green (Ecovine), navy/midnight (Dentcor, Metriva, Radesk), deep purple (Kidly).
- **1 vivid accent** — the spark, used sparingly for energy and CTAs. Lime (Ecovine, Radesk), electric purple (Metriva), orange (Kidly).
- **Neutrals** — white/off-white + a grayscale ramp for UI, text, and breathing room.

Two to three brand colours max at the core. Restraint is what makes them look premium. Kidly's purple+orange *duo* is the whole personality; Dentcor is essentially navy + white.

## Four-layer palette (the Radesk model)

Structure the full system in four tiers — this is exactly how the Radesk guideline lays out its colour pages:

1. **Primary** (3–4 swatches) — White · Anchor · a mid brand hue · Accent. Give each a **name**, HEX, RGB, and CMYK.
   - *Radesk:* White · Purple · Midnight · Lime.
2. **Secondary** (4–6 brights) — an extended palette for illustration, data, categories, states. *Radesk:* Cyan, Yellow, Orange, Red + light tints of each.
3. **Grayscale ramp** (6–9 steps, named) — from near-white to black for type, borders, surfaces. *Radesk:* Cloud · Smoke · Steel · Space · Graphite · Arsenic · Phantom · Black.
4. **Application tests** — logo-on-each-colour, logo-on-photography, and accessible text/background pairings. Prove the palette works before shipping it.

## Naming swatches

Named colours read as a designed system, not a random picker. Use evocative-but-clear names tied to the brand world:
- Neutrals: Cloud, Smoke, Steel, Space, Graphite, Phantom, Ink, Bone, Paper.
- Brand hues: name to the mood — Midnight, Forest, Leaf, Ember, Electric, Coral, Sun.

## Ratio & usage (the 60/30/10 discipline)

- **~60%** neutral/ground (white or the anchor as a full-bleed background — see Ecovine's green-field and Metriva's near-black tiles).
- **~30%** anchor/secondary structural colour.
- **~10%** vivid accent — reserved for the moments that must pop (CTA, key icon, one word in a headline). Overusing the accent kills it.

Note the reference move: brand-colour **full-bleed backgrounds**. Ecovine packaging sits on a flat green field; Metriva tiles are near-black or purple; Kidly's board is lavender. A saturated ground is a fast, high-impact way to signal the brand.

## Contrast & accessibility

- Body text must clear **WCAG AA** (contrast ≥ 4.5:1); large display text ≥ 3:1. Verify anchor-on-white and white-on-anchor.
- The vivid accent is often *not* text-safe on white (lime, yellow) — restrict it to fills, shapes, and large elements, not small type.
- Always define which text colour rides on each brand background (the "application tests" tier).

## Choosing hues from personality

| Personality | Anchor | Accent | Notes |
|---|---|---|---|
| Natural, wholesome | Forest / olive green | Lime / leaf | Two tones of one hue = calm + fresh (Ecovine) |
| Premium, trustworthy | Navy / midnight | Ice blue / white | Restraint signals expertise (Dentcor) |
| Intelligent, modern | Near-black / indigo | Electric violet | High-tech, confident (Metriva, Radesk) |
| Playful, youthful | Deep purple / grape | Orange / marigold | Complementary duo = fun, energetic (Kidly) |
| Luxury, editorial | Charcoal / black | Muted metallic or single jewel tone | Monochrome + one restrained pop (Dusk mood) |
| Appetite, hospitality | Warm red / terracotta | Cream / mustard | Warm, energetic F&B (burger storefront) |

## Check the anchor against reality before locking it

The table above is a *starting* vector. Before you commit the anchor, test it against 1,401 shipped marks (`references/logo-archive.md`):

```bash
scripts/logo_archive.py palette fintech           # the category convention
scripts/logo_archive.py search --color '#635BFF'  # who already owns this colour
```

Two numbers change how you choose:

- **38.4% of chromatic tech logos are blue-primary.** In tech, blue is not a choice — it's the default, and it's camouflage. Pick it only *because* trust reads louder than distinctiveness for this brief, and say so in the brief.
- **12.6% ship pure black/white** (Vercel, Notion, GitHub). Achromatic is a legitimate, confident position, not a failure to decide. It also sidesteps the collision problem entirely.

`search --color` ranks by perceptual distance (ΔE). **ΔE < 10 against a brand in the same sector is a collision** — a viewer will read them as the same colour. Move, or own the similarity deliberately.

Sector conventions worth knowing before you break them: security skews **red 42%** (against the blue default); fintech **blue 50%**; ai-ml is the most achromatic at **20%**. Caveat: that corpus is 50% devtools — it says nothing about hospitality, food, or local services. For those briefs, ignore it and use the exemplars.

## Deriving the palette from a real-world source

When the brand sits inside a strong existing visual system — a country, a sport, a heritage material — the palette can be *derived* rather than invented, and it buys recognition before a word is read. Pattaya Skydiving's system is the Thai flag's red and navy (Siam Red `#E01A2B`, Freefall Navy `#101A46`) over cloud white.

Two rules keep it from turning into costume:

- **Take the hues, not the artefact.** The flag is the *source*, never an element in the mark. Encode it structurally instead — the ram-air canopy's five cells reading as the flag's five stripes.
- **Legacy colours become UI-only, or they die.** The outgoing accent survived as an interface colour and was banned from the logo. State which layer each colour is allowed in (mark / UI / neither), or the old system leaks back through the website. And convert the site's palette in **one pass after the mark is chosen**, never in parallel with concept exploration.

## Say which surface each colour is allowed on

A palette that works on screen often needs one more neutral in print and social, and the two must not be swapped by accident. Venüs Sigorta's identity layer added a warm neutral, **Kireç `#EFEAE1`**, for stationery and social while the web kept the cooler **Sis `#F5F6F8`** — both are brand neutrals, each scoped to its surface. Write the scope into the swatch table (`web` / `print + social` / `UI only` / `never in the mark`), not into a conversation. The same discipline retires a legacy colour cleanly (see the section above).

**Turn the 10% accent rule into a written brand rule.** "Red never exceeds 10% of any composition" is checkable by a designer who has never met you; "use the accent sparingly" is not. Put the number in the guidelines.

## Delivery

- Provide HEX + RGB + CMYK (and Pantone if print-critical) for every core swatch.
- Ship CSS variables and a swatch sheet. The `brand-board.html` and `brand-guidelines.html` templates already tokenize the palette — set the `--brand-*` variables once and everything updates.
- Include gradients only if the brand calls for it (tech/AI often does — Metriva's phone UI); keep them subtle and derived from the core hues.
