# Mockup & Application Catalog

The application types the reference library covers, with art-direction notes and ready prompt seeds. Pick a set that fits the brand's channels — a dental clinic needs stationery + signage + uniform; an app needs device + app-icon + web. See `image-generation.md` for *how* to render these here.

## Application taxonomy

**Stationery** — business card (front + back), letterhead / A4, envelope (DL + C5), compliment slip, folder, notecard, stamp/seal, sticker.
**Digital** — app UI screen, app icon (iOS squircle / macOS / browser tab), website header/hero, social profile (avatar + banner) for IG/X/LinkedIn, email signature, social post templates.
**Apparel & merch** — t-shirt, hoodie, cap, tote bag, uniform/apron (Dentcor medical uniform), lanyard, enamel pin, mug, notebook, pen.
**Signage & environment** — storefront fascia, illuminated 3D sign, reception/wall logo, window-glass graphics (burger shop), wayfinding/directional, door vinyl, office glass partition (Dentcor).
**Packaging** — box, bag (retail/shopping), product label/sleeve, pouch, bottle/jar, food packaging & tray wrap (Ecovine produce), tissue/wrap, tape.
**Advertising / OOH** — billboard, bus-stop / city panel, poster, flyer, digital display ad, vehicle livery.
**Print collateral** — brochure, flyer, poster, menu, price list, folder, report cover.

## Signature presentation recipes (match the reference look)

- **Stationery flat-lay** — top-down, brand-colour flat ground, cards + letterhead + envelope softly overlapping, one card flipped to show the reverse, soft directional shadow. (Dentcor / navy.)
- **Packaging repeat-grid** — the product branded and tiled in a neat grid on a brand-colour field, isometric-ish top angle. (Ecovine / green.)
- **Storefront / window** — daylight exterior, real architecture, logo on fascia + window vinyl, believable reflections. (Burger shop.)
- **Device trio** — phone + laptop + tablet showing the app/site, floating on a soft gradient or dark ground. (Metriva / Dusk.)
- **Moody hold** — a person in dark clothing holding a card or box, low-key cinematic light, monochrome props. (Dusk.)
- **Hero over photography** — mark knocked out over a full-bleed on-brand photo. (Ecovine field.)

## Prompt seeds (adapt per brand)

Fill `[BRAND]`, `[LOGO]`, `[COLOR]`, `[SECTOR]`. Keep the logo/colour/type consistent across every prompt so the set coheres. Always request realistic soft shadows, correct perspective, and clean composition.

- **Business-card flat-lay:** "Top-down flat-lay of a premium business card set for [BRAND], a [SECTOR] brand — front and back cards, letterhead and envelope, arranged with slight overlap on a flat [COLOR] background, soft realistic directional shadow, matte paper, minimal, high-end brand mockup, studio light."
- **Storefront sign:** "Modern [SECTOR] storefront in daylight, [BRAND] logo on an illuminated fascia sign and window-glass vinyl, real urban architecture, believable glass reflections, clean minimal branding, photographic."
- **Packaging grid:** "Neat repeating grid of branded [product] packaging for [BRAND] on a flat [COLOR] background, top-down, consistent labels showing the logo and pattern, bright product photography, premium FMCG mockup."
- **App icon + phone:** "iPhone home screen close-up showing the [BRAND] app icon (rounded squircle) among other icons, plus the app's main screen on a second device, soft gradient background, crisp modern UI."
- **Apparel:** "[COLOR] tote bag / t-shirt / cap with the [BRAND] logo, worn/held by a person in matching dark clothing, moody studio light, editorial branding mockup."
- **Moody card hold:** "Cinematic dark studio shot, a person in black clothing holding a [BRAND] business card and a branded box, low-key lighting, monochrome props, premium agency mockup."

## Quality bar (reject and regenerate if any fail)

- Logo is **undistorted**, correct colours, legible, placed where it physically belongs.
- Perspective and shadows are **physically plausible**; no melting text, no warped edges.
- **Real brand copy** on every surface (name, tagline, contact) — never lorem or gibberish where a real value exists.
- One accent moment; the rest restrained. Consistent radius/shadow language across the set.
- Backgrounds are clean and on-brand; no stock-photo clutter fighting the mark.

## Fallback when AI mockups aren't available

If no image generator is reachable, **compose mockups in HTML/CSS** (flat-lay cards, device frames, signage panels) using the brand tokens and deliver as an `Artifact`, or use the **PSD mockup libraries** the user keeps in `~/Downloads/logo-brand-design-skill-gelistirme/Mockups/` (Studio Stationery, Dusk, Slash, Storefront, Signage, Packaging, City Advertising, Device) as smart-object templates in Photoshop/Figma. See `image-generation.md`.
