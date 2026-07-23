# Logo System

A logo is never one file. In every reference case it is a *system*: a primary mark, lockups, a compact submark, construction & clearspace rules, and colour variants. Design the system, not the picture.

## Mark archetypes (choose deliberately)

From the reference library and the canon (Airey, *Logo Design Love*; *Logo Modernism*):

1. **Geometric monogram** — one or two letters built on a grid. *Metriva* "M" (rounded columns), *Radesk* mark. Best for tech, corporate, agencies. Feels engineered, ownable, scales tiny.
2. **Negative-space / dual-meaning mark** — the idea hides in the counter-space. *Ecovine* sprout (wheat + leaves reading as a plant), *Dentcor* "smile/tooth" curve. Best when there's a clever product truth to encode. High craft payoff.
3. **Emblem / badge / seal** — mark + type locked in a bounded shape, often a ring with orbital text. *Ecovine* "Pure · Fresh" circular seals; *Kidly* scalloped "Smart Starts for Curious Kids" badge. Best for heritage, food, community, stamps/patterns. Comes with a built-in secondary mark.
4. **Custom rounded wordmark** — the name itself is the logo, hand-tuned. *Kidly* (bouncy), *Metriva* (soft geometric), *radesk* (clean lowercase). Best when the name is short and memorable.
5. **Abstract symbol** — a non-literal form carrying an attribute (motion, connection, growth). Use when the category is crowded with literal icons and you want to stand apart.
6. **Icon system / sub-brand set** — one construction logic spun into many icons. *Ecovine* vegetable set (tomato, carrot, pepper, beet, chili…) sharing one silhouette style. Powerful for ranges, categories, patterns.

**Default picks by brief:** premium/precise → monogram or negative-space; natural/food → emblem + icon system; playful → custom wordmark + badge; tech → monogram or abstract + wordmark.

## The lockup family (always produce all of these)

| Variant | Use |
|---|---|
| **Primary lockup** | Mark + wordmark, the canonical arrangement (usually mark-left or mark-top) |
| **Horizontal lockup** | Mark left of wordmark — for wide spaces (letterhead, web header, signage) |
| **Vertical / stacked lockup** | Mark above wordmark — for square/tall spaces (app splash, avatar, tote) |
| **Submark / logomark** | The symbol alone — favicon, app icon, stamp, pattern unit |
| **Monogram / lettermark** | 1–2 letters — social avatar, embossing, tiny sizes |
| **Wordmark alone** | Type only — where a symbol would be redundant |

### Proportions that real lockups hit

Measured across the 418 brands in `references/logo-archive.md` that ship a separable submark *and* a full lockup:

- **Submarks are square.** Median icon aspect **1.000**; 52% fall within 0.9–1.1. Not an aesthetic preference — avatars, favicons, and app tiles are square containers, and a non-square submark loses area in every one of them.
- **Horizontal lockups are ~4:1.** Median aspect **4.23** (IQR 3.41–5.17), and ≈4× the width of the brand's own icon. Drift much past ~6:1 and the lockup stops fitting real headers and signage; much under ~3:1 and it reads as a stacked mark, not a horizontal one.
- **Only 29.8% of tech brands ship both forms at all.** A submark is a deliberate investment, justified when the brand needs an avatar/app presence. Say why it exists rather than producing it by reflex.

Design against these, then check: `scripts/logo_archive.py pairs --sector <sector>`.

## Construction grid

Show the mark built on geometry — this is a signature page in the Radesk guideline ("Construction / Logo Mark, Horizontal, Vertical"). Communicates rigor.
- Build monograms/symbols on a **modular grid** or from **circles + a consistent stroke/counter ratio**. Keep stroke widths and corner radii consistent across the family.
- Present the mark with light construction guides (grid lines, circles, key measurements) on a tinted panel.
- Corner radius, stroke weight, and optical spacing are the three things to lock and never break.

## Clearspace & minimum size

- **Clearspace:** define an exclusion zone using a unit derived *from the logo itself* (e.g. `X` = height of the wordmark's cap, or the width of the mark's core stroke). Common rule: keep clear space of `1X` on all sides; `0.5X` for tight contexts.
- **Minimum size:** state a min width for the full lockup (e.g. 24 mm print / 120 px screen) and for the submark (e.g. 16 px favicon). Test legibility of counters and negative space at the smallest size.
- **Responsive logo:** define 2–3 simplification steps — full lockup → mark + short wordmark → submark only — as the space shrinks (like Metriva's app-icon reduction).

## Colour variants (each mark needs all four)

1. **Full colour** — on light background.
2. **Reversed** — on the dark/anchor colour (Dentcor white mark on navy card).
3. **Mono / one-colour** — single ink, for stamping, engraving, fax-grade contexts.
4. **On backgrounds / on photography** — knockout white or brand-tint over imagery, with a legibility scrim if needed (Ecovine mark over the aerial field). Radesk devotes whole pages to "P. Colors / Logo on Backgrounds."

## Do / Don't (misuse page)

Always ship a misuse page in guidelines. Standard forbidden moves: don't stretch/distort, don't rotate, don't recolour outside the palette, don't add shadows/outlines/gradients not in the system, don't place on low-contrast backgrounds, don't rearrange the lockup, don't box it when clearspace is available, don't outline the wordmark.

## Practical output

- **Vector is the deliverable.** For geometric monograms and wordmarks, prefer true vector (SVG) — hand-author simple geometric marks, or use Figma / Magnific `images_generate_svg` / `images_to_svg`. See `image-generation.md`.
- Export the family as: primary (SVG + PNG on transparent), reversed, mono, submark, favicon set. Always generate raster logos on a clean **white or transparent** background so they drop into mockups.
- Keep every variant in one folder: `<brand>-brand/logo/`.
