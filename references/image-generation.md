# Image Generation — Engine Routing

How to actually produce logos and mockups **in this environment**. Choose the first path that is available; each has a fallback. Verified as of skill creation:

- ✅ **Magnific MCP** — authenticated & working. **Primary AI engine.** Raster + SVG generation, logo-as-reference, background removal, relight, upscale (2–16×), variations, video, brand kits, **and a built-in stock photo/vector catalog** (`stock_search`/`stock_download`, Freepik). Tool cheat-sheet below.
- ✅ **Unsplash MCP** — **primary photography source when connected.** Free, high-quality, authentic/editorial photography — exactly the imagery mood in the reference library (Ecovine's aerial fields, lifestyle shots). ⚠️ **Not connected by default** — check with `claude mcp list`; if absent, connect it once (see "Photography sourcing" below) and meanwhile fall back to Magnific `stock_search`.
- ✅ **Figma MCP** — authenticated & working. Best for editable vector logos, design systems, and guideline files.
- ✅ **Canva MCP** — authenticated & working. Brand kits, templates, quick editable collateral.
- ✅ **`Artifact` tool + HTML** — always works. The signature deliverables (brand board, guidelines) render here regardless of any API.
- ⚠️ **`design` skill Gemini scripts** (`~/.claude/skills/design/scripts/logo|cip/generate.py`) — require `GEMINI_API_KEY` **and** the `google-genai` package, **neither present** at skill-creation time. Use only after confirming both exist (see bottom). Don't assume they work.

Always confirm availability at run time with `claude mcp list` (an MCP server may be unauthenticated in a given session, and Unsplash may not be connected at all); fall back down the list.

## Magnific tool cheat-sheet

The verified tool names (prefix `mcp__claude_ai_Magnific__`):

| Need | Tool | Notes |
|---|---|---|
| Logo / illustration (raster) | `images_generate` | TTI, or pass up to 12 `references[]`. `aspectRatio`, `count≤8`. Output is opaque. |
| Logo (true vector) | `images_generate_svg` | Recraft v4 Pro Vector — best for clean geometric marks/wordmarks. |
| Raster → vector | `images_to_svg` | Trace an existing logo to SVG. |
| **Mockup with the real logo on it** | `images_generate` + `references:[{type:"image", identifier:<logo>}]` | Upload the logo first, then reference it so the *actual* mark appears on the product. |
| Transparent cutout | `images_remove_background` | Chain after generate to drop a logo/product onto mockups. |
| Print-res | `images_upscale` | 2×/4×/8×/16×; `precision` for faithful, `creative` for added detail. |
| On-brand auto-gen | `images_generate` + `brandKitId` | Applies a saved brand kit's palette/logo/type automatically. See `brand_kit_list`/`brand_kit_get`. |
| Stock photo/vector | `stock_search` → `stock_download` | Freepik catalog; `content_type`, `license:free`, `orientation`. Photography fallback when Unsplash is absent. |
| Motion reveal | `video_generate` | Chain a still → video for launch clips. |

Reusable assets (a recurring character, product, style LoRA, location) live in the Magnific **library** (`library_list`/`library_show`) and can be passed as typed `references[]` to keep a subject consistent across a set.

### Magnific in practice

- **Model-name trap:** "Nano Banana 2" is `imagen-nano-banana-2-flash`. The id *without* `-flash` is the Pro model. Picking the wrong one silently changes both look and cost.
- **Budget before you fan out.** ~75 credits per 2K image; a 36-frame set is ~2,700. An unlimited plan on the web does **not** apply over MCP — credits are consumed.
- **One recipe for the whole set.** Write a single art-direction sentence and vary only the subject. Venüs Sigorta's 10 frames all ran: *"cinematic editorial, Mediterranean Antalya, 35/50/85mm, shallow DOF, natural low-angle light, deep shadows, muted limestone + charcoal + slate, **exactly one crimson red accent**, documentary realism unposed, no text/logos."* Consistency was high enough to accept the set in one pass. Naming the accent colour **and its count** is what keeps a brand rule visible in generated imagery.
- Always end prompts with **"no text, no watermark"** — generators letter fake words onto signage and packaging otherwise.
- **Output is PNG and heavy.** `sips -s format jpeg -s formatOptions 82 -Z 1600` took one set from 60 MB to 15 MB with no visible loss at deck scale.
- **The connector can be unauthorised in a given session** even when it works elsewhere (Renta's whole package was built with zero AI imagery for this reason). Check first, and have the HTML/CSS + real client photography path ready — it is a legitimate deliverable, not a downgrade.

## Logos

Priority order:

1. **Vector by hand (SVG)** — for geometric monograms, lettermarks, and simple symbolic marks, author the SVG directly. Full control, infinitely scalable, tiny, editable, no dependency. Best default for the clean geometric marks this skill favours. Build on a grid; keep stroke/counter ratios consistent (see `logo-system.md`).
2. **Figma** (`use_figma` / `create_new_file`) — when the user wants an editable working file, a logo *system* with variants, or design-system integration. Load the `/figma-use` skill first (MCP instruction). Produces real vector the user can refine.
3. **Magnific** — `images_generate` for concept exploration and richer/illustrative marks; `images_generate_svg` or `images_to_svg` to get vector out. Good for mascots, emblems, textured or illustrative logos, and fast concept rounds. **Always generate on a clean white/transparent background.**
4. **Gemini `design` script** *(only if key+package confirmed)* — `python3 ~/.claude/skills/design/scripts/logo/generate.py --brand "X" --style <style> --industry <ind>`. Rich style/colour/industry knowledge base via its `search.py`.

### Vector by script — wordmarks that survive a missing font

Never ship a logotype as `<text>`: the client's machine won't have the font, and variable-font axes won't apply even where it does. Convert to outlines at build time.

```python
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer          # pin variable axes
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
```

1. **Pin the axes first.** `instancer.instantiateVariableFont(tt, {"wght": 900, "wdth": 125})` — an expanded/heavy cut of a variable family (e.g. `Archivo[wdth,wght].ttf`) is an *instance*, not a style name. Do this before shaping so harfbuzz measures the real widths.
2. **Shape with harfbuzz** for glyph ids + positions (correct kerning and optical spacing).
3. **Outline with a pen:** `glyphset[name].draw(TransformPen(SVGPathPen(glyphset), t))`, where `t` carries the position harfbuzz returned plus any scale/skew. Emit `<path>` only.
4. **Features for logotypes:** `{"liga": False, "clig": False, "dlig": False, "calt": False, "kern": True}`. Leaving ligatures on silently fuses letter pairs in a wordmark — kerning is the only feature you want.
5. **Ring/arc text** (emblem seals) is the same pipeline with each glyph rotated onto a radius — one `arc_text()` helper covers the top and bottom arcs.

**Python gotcha:** the default `python3` / venv on this machine stalls with fontTools. Use `/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`. Fonts resolve from `~/Library/Fonts/`; a missing file must fail loudly, not fall back to a default face.

**Contour splitting gotcha (TrueType):** a contour whose points are *all* off-curve does not begin with `moveTo` — the pen emits `qCurveTo(..., None)`. Split contours on `closePath`/`endPath`, never on `moveTo`, or every glyph collapses to a single contour and counters fill in.

**When the font has no ligatures or alternates**, character has to come from composition instead: tracking, case, and the choice of face (an *ReverseItalic* backslant is a strong retro lever), plus a simple disc / ring / frame / bar / overlap device. Do not wait for a font to hand you the idea.

Whatever the engine: produce **2–3 distinct concepts** first (different archetypes — e.g. a monogram, a negative-space mark, a wordmark), let the user pick, *then* build the full system around the winner. Reuse the exact chosen logo file across all mockups so the identity stays consistent.

## Mockups & applications

Priority order:

1. **Magnific** — the workhorse here. Upload the finished logo, then `images_generate` with it passed in `references:[{type:"image", identifier:<logo>}]` so the **real mark** appears on the product (not a hallucinated one). Use the prompt seeds in `mockup-catalog.md`. For photographic scenes, drop in a real photo (Unsplash/stock) as a second reference or generate the environment and composite the cutout logo (`images_remove_background`). `images_relight` / `images_expand` / `images_upscale` to finish. Chain image→`video_generate` for motion reveals.
2. **HTML/CSS composition + `Artifact`** — build flat-lays, device frames, signage panels, and social templates directly with brand tokens. Always works, pixel-perfect, editable, on-brand. Great for stationery, social kits, and simple product shots.
3. **Gemini CIP script** *(only if key+package confirmed)* — `python3 ~/.claude/skills/design/scripts/cip/generate.py --brand "X" --logo <logo.png> --industry "<ind>" --set` for a full deliverable set, then `render-html.py` for a presentation.
4. **PSD smart-object libraries** — the user's own mockup library lives at `~/Downloads/logo-brand-design-skill-gelistirme/Mockups/` (Studio Stationery, Dusk, Slash, Monolith, Storefront, Signage, Packaging, City Advertising, Device, Burger). Use as Photoshop/Figma smart-object templates for photoreal, print-grade results when hand-finishing.

## Photography sourcing

Real photography is essential to the reference look — the hero-over-photography reveal (Ecovine's mark over the aerial field), mockup and moodboard backgrounds, the bento board's lifestyle tile, and the guidelines' Imagery / art-direction pages. See `photography.md` for *which* photos to choose and *how* to treat them; this is *where to get them*.

Priority order:

1. **Unsplash MCP** *(preferred, when connected)* — free, high-quality, authentic photography with a clean editorial feel that matches the reference mood. Tool names vary by server build, so discover them at run time with `ToolSearch "unsplash"` (typically a search + a get/download). Workflow: search by art-direction keywords → pick shots that fit the moodboard → download to `<brand>-brand/mockups/photography/`.
   - **Check first:** `claude mcp list | grep -i unsplash`. If it's not listed, it isn't connected.
   - **Connect it once** (needs a free Unsplash *Access Key* from https://unsplash.com/developers). Adding an MCP server is an interactive/config step — do it in an interactive `claude` session, e.g.:
     ```bash
     claude mcp add unsplash --env UNSPLASH_ACCESS_KEY=YOUR_KEY -- npx -y <unsplash-mcp-package>
     ```
     Confirm the exact package/tool names with the user before wiring it in; don't guess a package into a real config.
   - **Attribution:** Unsplash's license is free for commercial use with no permission needed, but crediting the photographer is required by their guidelines — record photographer + link in `brief.md` for any published/client work.
2. **Magnific stock** *(available now, no setup)* — `stock_search` (Freepik catalog: `content_type:"photo"`, `license:"free"`, `orientation`) → `stock_download`. Solid fallback whenever Unsplash isn't connected. Also reaches vectors, PSDs, and icons for collateral.
3. **Generate the scene** — `images_generate` a photographic environment on-brand when no stock shot fits (e.g. a specific storefront or product context), then composite the logo.
4. **User's PSD/library** — `~/Downloads/logo-brand-design-skill-gelistirme/` for reference-grade scenes and smart-object mockups.

Keep the imagery consistent: pick a single art-direction (light & fresh *or* dark & moody — see `photography.md`) and source every photo to it.

## Signature HTML deliverables (always available)

These reproduce the exact reference aesthetic and never depend on an API:
- **Bento brand board** → `assets/brand-board.html` (Kidly/Metriva layout).
- **Guidelines deck** → `assets/brand-guidelines.html` (Radesk structure).

Workflow: copy the template into the brand's output folder, set the `--brand-*` / `--font-*` tokens and swap in real logo/mockup images, then publish with the `Artifact` tool. **Load the `artifact-design` skill before publishing** (harness requirement). Artifacts start private; the user can share.

## Vector conversion & cleanup

- Raster logo → vector: Magnific `images_to_svg`, or Figma trace, or note it for manual vectorising.
- Background removal for placing marks on mockups: Magnific `images_remove_background`.
- Upscale for print: Magnific `images_upscale`.

## Output hygiene

- Save everything under `<brand>-brand/` (see SKILL.md for the folder tree).
- Logos on **white or transparent**; name files by variant (`logo-primary`, `logo-reversed`, `logo-mono`, `submark`, `favicon`).
- Keep one source of truth for colours/type (the CSS token block) and feed the same values into every prompt and template.

## Confirming the Gemini path (optional)

Only if you intend to use the `design` scripts:
```bash
python3 -c "import google.genai" 2>&1        # must NOT error
printenv GEMINI_API_KEY                        # must be non-empty (or present in ~/.claude/.env)
```
If either fails, skip Gemini and use Magnific / Figma / HTML. To enable later: `pip install google-genai` and add `GEMINI_API_KEY=...` to `~/.claude/.env`.
