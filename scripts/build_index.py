#!/usr/bin/env python3
"""
Rebuild assets/logo-archive/index.json from the upstream gilbarbara/logos repo.

    python3 build_index.py --clone          # shallow-clone upstream to a temp dir, mine, merge
    python3 build_index.py --repo ~/logos   # mine an existing checkout

Sector labels are NOT derivable from the SVGs — they were assigned by an LLM pass.
This script preserves the sector of every brand already in the index and prints any
NEW brands as `unclassified` so they can be labelled and re-merged. It never silently
drops or invents a label.
"""
import argparse, json, os, re, subprocess, sys, tempfile, colorsys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "..", "assets", "logo-archive", "index.json")
UPSTREAM = "https://github.com/gilbarbara/logos.git"

# 6-digit alternative MUST precede the 3-digit one: alternation is first-match,
# so `{3}|{6}` silently captures "#1ED" out of "#1ED760".
HEX = re.compile(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b')
PAINT = re.compile(r'(?:fill|stop-color|stroke)\s*[:=]\s*"?\s*(#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b)', re.I)
VIEWBOX = re.compile(r'viewBox="([\d.\-\s]+)"')


def norm(h):
    h = h.lower().lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return '#' + h


def hsl(h):
    r, g, b = [int(h.lstrip('#')[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    hh, l, s = colorsys.rgb_to_hls(r, g, b)
    return hh * 360, s * 100, l * 100


def is_neutral(h):
    _, s, l = hsl(h)
    return s < 12 or l > 96 or l < 4


def path_weight(svg, color):
    """Approximate area: summed path-data length of elements painted `color`.

    Not true rendered area — but path complexity correlates well enough to rank a
    brand's dominant hue above its accents, which is all the ordering needs.
    """
    w = 0
    for m in re.finditer(r'<(path|circle|rect|polygon|ellipse|stop)\b([^>]*)>', svg):
        attrs = m.group(2)
        if color in [norm(x) for x in PAINT.findall(attrs)]:
            d = re.search(r'\sd="([^"]*)"', attrs)
            w += len(d.group(1)) if d else 120
    return w


def mine(fp):
    svg = open(fp, encoding='utf-8', errors='replace').read()
    body = re.sub(r'<title>.*?</title>', '', svg, flags=re.S)
    paints = [norm(c) for c in PAINT.findall(body)] or [norm(c) for c in HEX.findall(body)]
    counts = Counter(paints)
    ordered = sorted(counts, key=lambda c: (-path_weight(body, c), -counts[c]))

    vb, aspect = VIEWBOX.search(svg), None
    if vb:
        p = [float(x) for x in vb.group(1).split()]
        if len(p) == 4 and p[3]:
            aspect = round(p[2] / p[3], 3)

    brand = [c for c in ordered if not is_neutral(c)]
    return {
        "colors": brand[:4],
        "neutrals": [c for c in ordered if is_neutral(c)][:2],
        "aspect": aspect,
        "gradient": "linearGradient" in svg or "radialGradient" in svg,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--clone", action="store_true", help="shallow-clone upstream into a temp dir")
    g.add_argument("--repo", help="path to an existing gilbarbara/logos checkout")
    args = ap.parse_args()

    tmp = None
    if args.clone:
        tmp = tempfile.mkdtemp(prefix="logos-")
        repo = os.path.join(tmp, "logos")
        print(f"cloning {UPSTREAM} ...", file=sys.stderr)
        subprocess.run(["git", "clone", "--depth", "1", UPSTREAM, repo], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        repo = os.path.expanduser(args.repo)

    manifest = json.load(open(os.path.join(repo, "logos.json")))
    known = {}
    if os.path.exists(INDEX):
        known = {e["id"]: e.get("sector", "unclassified") for e in json.load(open(INDEX))}

    # Upstream reuses a shortname for genuinely different products (Dojo vs Dojo
    # Toolkit, Panda vs Panda CSS, Tor vs Tor Browser). Left alone these collide
    # into one entry and `show` silently returns whichever landed last. For any
    # colliding shortname, fall back to the primary filename stem, which is unique.
    collisions = {s for s, n in Counter(b["shortname"] for b in manifest).items() if n > 1}

    out, new = [], []
    for b in manifest:
        files, sn = b["files"], b["shortname"]
        icon = next((f for f in files if re.search(r'-icon\.svg$', f)), None)
        full = next((f for f in files if f == sn + ".svg"), None)
        primary = full or icon or files[0]
        fp = os.path.join(repo, "logos", primary)
        if not os.path.exists(fp):
            continue

        bid = sn
        if sn in collisions:
            bid = re.sub(r'(-icon)?\.svg$', '', primary)

        if bid not in known:
            new.append(bid)
        # `has_primary` means only "a file named <shortname>.svg exists" — NOT that it
        # is a wordmark. For the 953 brands with no -icon sibling that file is usually
        # the bare symbol (median aspect 1.00). Only when an -icon sibling ALSO exists
        # is <shortname>.svg reliably a full lockup (median aspect 4.23).
        e = {
            "name": b["name"], "id": bid, "url": b.get("url", ""),
            "sector": known.get(bid, "unclassified"),
            "files": files, "has_icon": bool(icon), "has_primary": bool(full),
            **mine(fp),
        }
        if icon and os.path.exists(os.path.join(repo, "logos", icon)):
            ic = mine(os.path.join(repo, "logos", icon))
            e["icon_aspect"], e["icon_colors"] = ic["aspect"], ic["colors"]
        out.append(e)

    out.sort(key=lambda e: e["id"])
    os.makedirs(os.path.dirname(INDEX), exist_ok=True)
    json.dump(out, open(INDEX, "w"), separators=(",", ":"))

    dropped = set(known) - {e["id"] for e in out}
    print(f"wrote {len(out)} brands -> {INDEX}")
    print(f"  submark+lockup pairs: {sum(1 for e in out if e['has_icon'] and e['has_primary'])}")
    print(f"  achromatic          : {sum(1 for e in out if not e['colors'])}")
    if new:
        print(f"\n  {len(new)} NEW brands need a sector label (currently 'unclassified'):")
        for n in new[:40]:
            print(f"    {n}")
        if len(new) > 40:
            print(f"    ... and {len(new) - 40} more")
    if dropped:
        print(f"\n  {len(dropped)} brands disappeared upstream: {', '.join(sorted(dropped)[:20])}")
    if tmp:
        subprocess.run(["rm", "-rf", tmp])


if __name__ == "__main__":
    main()
