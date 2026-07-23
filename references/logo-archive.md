# Logo Archive — 1,402 real production marks

The exemplar library (`reference-library.md`) is **aspirational** work: award-style identity posts, art-directed, never shipped at scale. This archive is the opposite and the complement — **1,402 logos that real companies actually ship**, mined from [gilbarbara/logos](https://github.com/gilbarbara/logos). Use the exemplars to set the *craft bar*; use this archive to answer *"what does this category actually look like, and how do I avoid looking like it?"*

Index: `assets/logo-archive/index.json` (~390 KB). Tool: `scripts/logo_archive.py`. SVGs are **not** vendored — 25 MB would bloat the skill — they stream from `cdn.svglogos.dev` on demand and cache locally.

## ⛔ The one hard rule

**Every mark here is its owner's trademark.** There are exactly two legitimate uses:

1. **Study & benchmarking** — read them, measure them, learn the category's conventions.
2. **Third-party marks in a mockup** — an integrations row, a tech-stack slide, a "works with" strip, a partner wall. Real logos, used as themselves.

**Never** feed one to an image generator as a style reference, base, or `references[]` image for a client's mark. Never trace, recolour, or "adjust" one into a deliverable. If a generated concept resembles one of these, kill the concept. A brand identity that borrows a real company's mark is not a deliverable — it is a legal problem handed to the client.

## What's in the index

Per brand: `id`, `name`, `url`, `sector`, `files`, `colors[]`, `neutrals[]`, `aspect`, `icon_aspect`, `gradient`, `has_icon`, `has_primary`.

Two fields need care:

- **`colors[]`** is mined from SVG paint attributes and ordered by approximate area, so `colors[0]` is the dominant hue. An **empty list means genuinely achromatic** (Notion, Vercel, GitHub) — that is a finding, not missing data.
- **`has_primary`** means only *"a file named `<id>.svg` exists"* — **not** that it's a wordmark. For the 953 brands with no `-icon` sibling, that file is usually the bare symbol (median aspect 1.00). Only when an `-icon` sibling **also** exists is `<id>.svg` reliably a full lockup (median aspect 4.23). Trust "lockup" only for the 418 pairs.

## Commands

```bash
scripts/logo_archive.py search --sector fintech          # who's in the category
scripts/logo_archive.py search --color '#635BFF'         # nearest real brand colour (Lab ΔE)
scripts/logo_archive.py search --sector ai-ml --hue blue # crowding check
scripts/logo_archive.py palette security                 # what the sector actually ships
scripts/logo_archive.py pairs --sector devtools          # submark ↔ lockup geometry
scripts/logo_archive.py show stripe                      # one brand, full record
scripts/logo_archive.py fetch stripe --out ./mockups/    # SVG for a mockup (see hard rule)
```

`search --color` ranks by CIE76 ΔE against every mined colour. **ΔE < 10 means a viewer would read your colour and theirs as the same brand colour.** Run it on your proposed anchor before locking it — in a crowded category, that's a collision, not an inspiration.

## What the corpus actually says

Measured across all 1,402 (regenerate with `build_index.py`):

| Fact | Value | So what |
|---|---|---|
| Blue is the primary hue | **38.4%** of chromatic marks | The tech default. Choosing blue is choosing camouflage. |
| Exactly one brand colour | **38.2%** | Restraint is the norm, not a bold move. |
| 3+ brand colours | 27.5% | Usually a multi-product suite (Slack, Figma), not a startup. |
| Pure black/white | **12.6%** | A real, confident strategy (Vercel, Notion) — not a cop-out. |
| Gradient | 19.8% | Fine in AI/dev; still a minority. |
| Separable submark + lockup | **29.8%** (418) | Most tech brands ship *only* one form. |

**Sector hue skews** (`palette <sector>` for the full picture):

| Sector | n | Dominant hue | Achromatic |
|---|---|---|---|
| fintech | 28 | blue **50%**, orange 21% | 10.7% |
| security | 36 | **red 42%**, blue 25% | 11.1% |
| data | 132 | blue 39%, red 14%, purple 11% | 7.6% |
| ai-ml | 30 | blue 33%, red/orange 13% | **20.0%** |
| devtools | 705 | blue 31%, red 15%, orange 12% | 12.5% |

Security skewing **red** against the overall blue default is the kind of category convention worth either honouring (fit in) or breaking (stand out) — deliberately, with the number in hand.

**Submark geometry** (the 418 true pairs): median icon aspect **1.000** — 52% sit within 0.9–1.1. Submarks are square because avatars, favicons, and app icons are square. Median lockup aspect **4.23** (IQR 3.41–5.17), i.e. a horizontal lockup ≈ **4× as wide as tall**, and ≈ **4× the width of its own icon**. These are good default targets for step 4 of the workflow; deviating far from them usually means the lockup won't drop into real containers.

## ⚠️ The corpus is skewed — do not launder it as market data

**706 of 1,402 brands are devtools** (50%). This is a *"collection for developers/DevOps/geeks"*, not a sample of business. It follows that:

- **Thin sectors are anecdotes.** health n=1, travel-mobility n=4, enterprise-hr n=4. `palette` prints a warning below n=15 and it means it — a 100% bar over one brand is noise. Never cite these to a client.
- **Absent categories are absent.** No hospitality, agriculture, legal, construction, local services. For an Ecovine or a Kidly brief this archive has **nothing** to say. Use `reference-library.md` and the exemplars.
- **It skews B2B software.** "Blue is 38%" is true *of tech*. Don't state it as a fact about brands in general.

Sector labels came from an LLM classification pass, not upstream metadata — they're good but not authoritative. `build_index.py` preserves them across rebuilds and flags new brands as `unclassified` rather than guessing.

## Where this plugs into the workflow

- **Step 1 (strategy)** — `search --sector <x>` for a real competitive set: who's there, what they look like. Better than inventing competitors.
- **Step 2 (visual direction)** — run `palette <sector>` **before** picking the anchor, and `search --color <candidate>` **after**. The first tells you the convention; the second tells you if you've collided with it. Record both in the brief as justification.
- **Step 4 (logo system)** — `pairs --sector <x>` for real submark/lockup proportions to design against.
- **Step 7 (mockups)** — `fetch` real third-party marks for integration rows and tech-stack surfaces. Re-read the hard rule first.

## Regenerating

```bash
scripts/build_index.py --clone            # shallow-clone upstream, re-mine, merge
scripts/build_index.py --repo ~/logos     # use an existing checkout
```

Existing sector labels survive; new upstream brands appear as `unclassified` and want a labelling pass. Upstream reuses a few shortnames for different products (Dojo/Dojo Toolkit, Panda/Panda CSS, Tor/Tor Browser) — the script derives unique ids from the filename for those, so don't be surprised by `pandacss` or `tor-browser`.
