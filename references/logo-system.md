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

Measured across the 419 brands in `references/logo-archive.md` that ship a separable submark *and* a full lockup:

- **Submarks are square.** Median icon aspect **1.000**; 52% fall within 0.9–1.1. Not an aesthetic preference — avatars, favicons, and app tiles are square containers, and a non-square submark loses area in every one of them.
- **Horizontal lockups are ~4:1.** Median aspect **4.23** (IQR 3.41–5.17), and ≈4× the width of the brand's own icon. Drift much past ~6:1 and the lockup stops fitting real headers and signage; much under ~3:1 and it reads as a stacked mark, not a horizontal one.
- **Only 29.8% of tech brands ship both forms at all.** A submark is a deliberate investment, justified when the brand needs an avatar/app presence. Say why it exists rather than producing it by reflex.

Design against these, then check: `scripts/logo_archive.py pairs --sector <sector>`.

## When the client already has a mark

Most identity work is not a blank page — a logo exists and the job is to build a *system* around it. Two moves do most of the work:

- **Measure the mark, then derive everything from one curve.** Venüs Sigorta's logo is a roof; its arc's measured centreline (`M 501 907 Q 1079 233 1657 907`, apex `1079,570`) became the single generator for three graphic devices — concentric roof layers, a tiled roof-tile grid, and a vertical "cover lines" field whose top contour follows the arc. A graphic language derived from a measured curve of the mark cannot drift from it; one invented alongside it always does.
- **Group the existing paths, don't redraw them.** Load the client SVG's path data and group indices into named parts (Venüs: roof `[1,2]`, "venüs" `[0,3,4,5,6,8,9]`, "SİGORTA" `[7,10..16]`; Renta: `0,1` = letters, `2,3` = red tail, `4,5,6` = tent). The generator then assembles lockups from parts. Redrawing "close enough" is the fastest way to ship a mark that fails the client's own eye test.
- **Derive the lockups they never had.** Both brands arrived with one horizontal file. The horizontal lock, the stacked lock, and a square **badge** (emblem + one letter, as a tile) were new — and the badge is what makes the avatar, the favicon, and the email-signature PNG possible.
- **Cutting colours is a legitimate system decision.** Renta's mark went 3 colours → 2 (red wordmark + ink tent) because the thin `#E3E3E2`/`#868686` grey rules disappeared at small size and in print. Keep the outgoing version as `<name>-miras.svg` in the archive and say in the guidelines which one supersedes it.

State min size in **both units** — Renta: full lock 120 px / 26 mm, emblem 32 px / 10 mm — and derive the clearspace `X` from the mark (half the letter height there).

## Multi-line logotypes

A stacked, text-only logotype (no symbol) lives or dies on the optical alignment of its lines. From the İstanbul Sanal Ofis round, where all three directions were type-only:

- **Justify with the `wdth` axis, never by scaling.** Setting three lines to equal width by stretching or squashing the glyphs is visible immediately. A variable family with a width axis (Archivo `wdth`) gives real, drawn widths at every step.
- **Open the narrow line; do not squeeze the wide one.** Tightening the wide line runs into the negative-tracking limit and then silently overflows the viewBox instead of failing. Widening the narrow line has headroom.
- **Lay out to the real ink bbox, not cap height.** Turkish `İ` carries a dot above the cap line. Anchored to cap height, it either escapes the viewBox or collides with the line above.
- **A dotted accent is an ownable device.** The two `İ` dots in the accent colour gave that direction its whole identity — no symbol required.

## Emblem shapes that read as something else

Every abstract emblem is checked against what it accidentally resembles. Two real rejections from one set:

- **Three flat parallel rules read as a hamburger menu.** Curving them into waves fixed it.
- **A ring cut from a filled circle reads as the Target logo.** Squaring the container fixed it.

Squint at the emblem at favicon size and name the first thing you see. If it is a UI affordance or another brand, the shape is wrong regardless of the concept behind it.

**Balance the forms across a set.** When several marks ship together (a 4-brand concept set), give them deliberately different geometry — one organic, one square, one circular, one linear — so the set reads as a range instead of four attempts at the same idea.

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

## Build the family from a script, not by hand

Past roughly six files, a lockup family stops being hand-authorable: 3 concepts × (submark, horizontal, vertical, reversed, mono) is 15–27 SVGs that all have to stay in sync. Author a **generator** — one Python file that emits the whole family — and treat the SVGs as build output.

- **The script is the source of truth.** Edits go to the generator and everything regenerates. Never patch an emitted SVG; the next run silently reverts it. Keep it at `<brand>-brand/_kaynak/gen_logo.py` and say so in the handoff, or the next session hand-edits the output.
- **Outline the wordmark, don't reference the font.** `<text>` renders wrong wherever the font isn't installed — which is every client machine. Shape with **uharfbuzz**, outline with **fontTools**, emit `<path>`. Full recipe in `image-generation.md` § "Vector by script".
- **Parametrise the skeleton, not the shape.** R5's logotype family came from `glyph_R` / `glyph_5` builders taking width, weight, and counter as arguments — "wide monolith" and "condensed near-square" are two calls, not two drawings.
- **Normalise every variant through one fit function.** A shared `fit(groups, box, margin)` that scales each assembled mark into a common box is what makes submark, horizontal, and vertical read as one family instead of three sizes.
- Reversed and mono variants then come free: same geometry, one ink parameter.

## Letterform constraints that bite

Field notes from hand-built geometric marks. Each of these cost a rebuild:

- **Stencil bridges need a `<mask>`, not `evenodd`.** A cutting rectangle that extends past the letter leaves its outer part as a single winding pass, so `fill-rule="evenodd"` paints it **solid** instead of clearing it.
- **A geometric `R`'s leg cannot spring straight off the bowl.** Keep `legTopX = (bowl_outer − bowl_arc) − leg_width` greater than the stem width, or the leg grows *into* the stem. In heavy and condensed cuts this is the first constraint that binds — solve it before detailing the rest of the letter.
- **Near-square beats wide for avatars.** A condensed logotype whose ratio approaches 1:1 works as favicon and avatar with no emblem at all — which can retire an entire symbol concept. Test the wordmark inside the square container *before* designing a submark for it (see the square-submark median above).
- **Non-square marks break `<img>` containers.** Under `object-fit: contain`, any container whose aspect doesn't match the mark's pushes construction frames and rules outside the box. Set the container's aspect from the SVG's own `viewBox`.
- **Dark grounds need the reversed file, not CSS.** An ink-filled SVG embedded via `<img>` can't be recoloured by the page, so a dark presentation band swallows it whole. Ship `-ters` / `-reversed` files and swap the `src`.

## Practical output

- **Vector is the deliverable.** For geometric monograms and wordmarks, prefer true vector (SVG) — hand-author simple geometric marks, script the family (above), or use Figma / Magnific `images_generate_svg` / `images_to_svg`. See `image-generation.md`.
- Export the family as: primary (SVG + PNG on transparent), reversed, mono, submark, favicon set. Always generate raster logos on a clean **white or transparent** background so they drop into mockups.
- Keep every variant in one folder: `<brand>-brand/logo/`.
