#!/usr/bin/env python3
"""
logo_archive — search 1,402 real production brand logos (gilbarbara/logos) for
benchmarking, palette calibration, and mockup assets.

    ./logo_archive.py search stripe              # by name
    ./logo_archive.py search --sector fintech    # by sector
    ./logo_archive.py search --color '#635BFF'   # nearest brand colour (Lab ΔE)
    ./logo_archive.py search --sector ai-ml --color '#000000' --limit 30
    ./logo_archive.py show stripe                # full record + file list
    ./logo_archive.py palette fintech            # what the sector actually ships
    ./logo_archive.py pairs --sector devtools    # brands with a separable submark + lockup
    ./logo_archive.py fetch stripe               # download SVG(s) -> cache, print paths
    ./logo_archive.py fetch stripe --icon --out ./mockups/

Colours are mined from the SVG paint attributes and ordered by approximate area,
so `colors[0]` is the dominant brand hue. Brands with an empty `colors` list are
genuinely achromatic (Notion, Vercel) — that's signal, not missing data.

TRADEMARK: every logo here is its owner's property. Use for study, benchmarking,
and as third-party marks in mockups (integration rows, tech-stack slides). NEVER
feed one to an image generator as the basis for a client's mark.
"""
import argparse, json, os, sys, colorsys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "..", "assets", "logo-archive", "index.json")
CACHE = os.path.join(HERE, "..", "assets", "logo-archive", "cache")
CDN = "https://cdn.svglogos.dev/logos/{}"


# ---------- colour maths ----------

def _rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"bad hex: {h}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _lab(h):
    """sRGB -> CIE L*a*b* (D65). Used for perceptual nearest-colour search."""
    r, g, b = [c / 255 for c in _rgb(h)]
    r, g, b = [((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92 for c in (r, g, b)]
    x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047
    y = (r * 0.2126 + g * 0.7152 + b * 0.0722) / 1.00000
    z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else (7.787 * t) + (16 / 116)
    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e(h1, h2):
    """CIE76 ΔE. Rough but monotonic enough to rank 'closest brand colour'."""
    a, b = _lab(h1), _lab(h2)
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def hue_name(h):
    r, g, b = [c / 255 for c in _rgb(h)]
    hh, l, s = colorsys.rgb_to_hls(r, g, b)
    deg, s, l = hh * 360, s * 100, l * 100
    if s < 12:
        return "neutral" if 4 < l < 96 else ("white" if l >= 96 else "black")
    for lo, hi, nm in [(0, 15, "red"), (15, 45, "orange"), (45, 70, "yellow"),
                       (70, 165, "green"), (165, 195, "teal"), (195, 250, "blue"),
                       (250, 290, "purple"), (290, 335, "magenta"), (335, 361, "red")]:
        if lo <= deg < hi:
            return nm
    return "other"


# ---------- data ----------

def load():
    if not os.path.exists(INDEX):
        sys.exit(f"index not found: {INDEX}\nRun scripts/build_index.py to regenerate it.")
    return json.load(open(INDEX))


def fmt(e, score=None):
    c = " ".join(e["colors"][:3]) or "(achromatic)"
    tag = []
    if e["has_icon"] and e["has_primary"]:
        tag.append("lockup+icon")
    elif e["has_icon"]:
        tag.append("icon")
    if e.get("gradient"):
        tag.append("gradient")
    s = f"  ΔE{score:5.1f}" if score is not None else ""
    return f"{e['id']:28} {e['sector']:22} {c:26} {','.join(tag):12}{s}"


# ---------- commands ----------

def cmd_search(a):
    d = load()
    if a.query:
        q = a.query.lower()
        d = [e for e in d if q in e["id"].lower() or q in e["name"].lower()]
    if a.sector:
        d = [e for e in d if e["sector"] == a.sector]
    if a.hue:
        d = [e for e in d if e["colors"] and hue_name(e["colors"][0]) == a.hue]
    if a.pairs_only:
        d = [e for e in d if e["has_icon"] and e["has_primary"]]

    scores = {}
    if a.color:
        scored = []
        for e in d:
            if not e["colors"]:
                continue
            best = min(delta_e(a.color, c) for c in e["colors"])
            scores[e["id"]] = best
            scored.append(e)
        d = sorted(scored, key=lambda e: scores[e["id"]])

    if not d:
        print("no matches")
        return
    for e in d[:a.limit]:
        print(fmt(e, scores.get(e["id"])))
    if len(d) > a.limit:
        print(f"... {len(d) - a.limit} more (--limit to widen)")


def cmd_show(a):
    d = {e["id"]: e for e in load()}
    e = d.get(a.id)
    if not e:
        near = [k for k in d if a.id.lower() in k][:8]
        sys.exit(f"unknown id: {a.id}" + (f"\ndid you mean: {', '.join(near)}" if near else ""))
    print(f"{e['name']}  ({e['id']})")
    print(f"  sector    {e['sector']}")
    print(f"  site      {e['url']}")
    print(f"  colours   {', '.join(f'{c} [{hue_name(c)}]' for c in e['colors']) or '(achromatic)'}")
    print(f"  neutrals  {', '.join(e['neutrals']) or '-'}")
    print(f"  aspect    {e['aspect']} (w/h){'  icon ' + str(e['icon_aspect']) if e.get('icon_aspect') else ''}")
    print(f"  gradient  {e['gradient']}")
    print(f"  files     {', '.join(e['files'])}")


MIN_N = 15  # below this, percentages are noise dressed up as evidence


def cmd_palette(a):
    d = [e for e in load() if e["sector"] == a.sector]
    if not d:
        sys.exit(f"no brands in sector: {a.sector}")
    from collections import Counter
    hues = Counter(hue_name(e["colors"][0]) for e in d if e["colors"])
    achrom = sum(1 for e in d if not e["colors"])
    multi = sum(1 for e in d if len(e["colors"]) >= 2)
    grad = sum(1 for e in d if e["gradient"])

    print(f"sector: {a.sector}   n={len(d)}")
    if len(d) < MIN_N:
        print(f"\n  !! n={len(d)} is too small to generalise from. This archive is a\n"
              f"     developer-tool collection; thin sectors are not a market sample.\n"
              f"     Read the brands below as individual examples, not as a trend.\n")
    print(f"\ndominant hue of the primary brand colour:")
    for h, n in hues.most_common():
        print(f"  {h:10} {n:4}  {100*n/len(d):5.1f}%  {'█' * round(40*n/len(d))}")
    print(f"\n  achromatic (black/white only)  {achrom:4}  {100*achrom/len(d):5.1f}%")
    print(f"  2+ brand colours               {multi:4}  {100*multi/len(d):5.1f}%")
    print(f"  uses a gradient                {grad:4}  {100*grad/len(d):5.1f}%")
    print(f"\nrepresentative marks:")
    for e in [x for x in d if x["colors"]][:12]:
        print(f"  {e['id']:24} {' '.join(e['colors'][:3])}")


def cmd_pairs(a):
    d = [e for e in load() if e["has_icon"] and e["has_primary"]]
    if a.sector:
        d = [e for e in d if e["sector"] == a.sector]
    print(f"{len(d)} brands ship a separable submark alongside a full lockup")
    print("(median lockup aspect 4.23, median icon aspect 1.000 -- see logo-archive.md)\n")
    for e in d[:a.limit]:
        ia = e.get("icon_aspect")
        print(f"  {e['id']:24} icon {str(ia):6} lockup {str(e['aspect']):6} "
              f"ratio {round(e['aspect']/ia, 2) if ia and e['aspect'] else '-'}")


def cmd_fetch(a):
    d = {e["id"]: e for e in load()}
    e = d.get(a.id)
    if not e:
        sys.exit(f"unknown id: {a.id}")
    files = e["files"]
    if a.icon:
        files = [f for f in files if "-icon" in f] or files
    out = a.out or CACHE
    os.makedirs(out, exist_ok=True)
    for f in files:
        dest = os.path.join(out, f)
        if os.path.exists(dest) and not a.force:
            print(f"cached  {dest}")
            continue
        try:
            with urllib.request.urlopen(CDN.format(f), timeout=20) as r:
                open(dest, "wb").write(r.read())
            print(f"fetched {dest}")
        except urllib.error.URLError as ex:
            print(f"FAILED  {f}: {ex}", file=sys.stderr)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="search by name / sector / colour")
    s.add_argument("query", nargs="?", default=None)
    s.add_argument("--sector")
    s.add_argument("--color", help="hex; ranks by perceptual distance")
    s.add_argument("--hue", help="red|orange|yellow|green|teal|blue|purple|magenta")
    s.add_argument("--pairs-only", action="store_true", help="only brands with a separable icon + lockup")
    s.add_argument("--limit", type=int, default=20)
    s.set_defaults(f=cmd_search)

    s = sub.add_parser("show", help="full record for one brand")
    s.add_argument("id")
    s.set_defaults(f=cmd_show)

    s = sub.add_parser("palette", help="colour statistics for a sector")
    s.add_argument("sector")
    s.set_defaults(f=cmd_palette)

    s = sub.add_parser("pairs", help="brands with a separable submark + full lockup")
    s.add_argument("--sector")
    s.add_argument("--limit", type=int, default=40)
    s.set_defaults(f=cmd_pairs)

    s = sub.add_parser("fetch", help="download SVG(s) from the CDN")
    s.add_argument("id")
    s.add_argument("--icon", action="store_true", help="icon variant only")
    s.add_argument("--out", help="destination dir (default: skill cache)")
    s.add_argument("--force", action="store_true")
    s.set_defaults(f=cmd_fetch)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
