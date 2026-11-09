#!/usr/bin/env python3
"""test_surfaces.py - the surfaces that point into the explorer: the links (tahoemap/links.py), the map (html_map
VERSION 7), the vault (VERSION 5) and the look-ups (query.py). Design section 11.1, item 9.

    python tests/test_surfaces.py [--out OUT] [--data DATA]

check(out, data=None) runs every check on a finished output and returns [(name, ok, detail)], ok True, False or
'warn' (tests/checks.py calls it; design I5). It reads OUT and writes only into a temporary folder. Run alone, it
prints one line per check and exits 1 when any failed; --out defaults to run_tests.py's synthetic output
(/tmp/tahoemap_test/out_seed0).

What is checked:
  links      labels with spaces, parentheses and '/' ('Idarubicin (hydrochloride)', 'HepG2/C3A') stay one path
             segment and decode back exactly; git remotes in https, ssh and local-proxy form give the owner and the
             repository; '', 'none' and 'off' mean no site; every builder returns None without a site
  map        the stamp has no 'shortened' entry and html_map no shortening code (_shrink, _shrink_steps, MAX_BYTES);
             the page holds "explorer_base":"<site url>" exactly once (the explorer stage's regex finds it once);
             every function snippet is the registry text or a cut that ends in '…'; each line row carries BOTH the
             strongest drug-dose up and down (tables/line_effects), and when one carries an alert, the strongest
             without one that way; every direction row of direction_view that touches a gene of the page is on the
             page with its edge line (decoded here: = direction_view.edge_line, notes included), and every row a
             gene's capped list shows carries its reading; in a headless browser (Playwright; else 'warn') every
             preview list says 'k of N shown · all N in the explorer' with the true k and N and a link into the
             explorer, also on a page without a site URL (links to ../explorer/web/index.html)
  vault      .tahoemap-paths.json lists every gene, plates, drug, line, module and plate note (and only existing
             ones); every gene, drug, line and module note starts with 'Explorer: ... · Map: ...'; every
             '(k of N shown; all N in the explorer: ...)' has k <= N and points into the explorer; a gene's drug
             and partner lists say their true N; registry texts cut at 500 characters end in '…' with a link; without
             a site URL the notes name the local explorer
  look-ups   `gene X --top 0` and --top all print every row (no '... more'); a capped list prints 'all N: <url>';
             query.parse_top; whether cli.py takes '--top all' (warn until it does)
"""

import argparse
import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

DEFAULT_OUT = os.path.join(tempfile.gettempdir(), "tahoemap_test", "out_seed0")
KOFN = re.compile(r"\((\d[\d,]*) of (\d[\d,]*)(?: [^()]*?)? shown; all (\d[\d,]*) in the explorer: ([^)]*?)\)")
MAP_KOFN = re.compile(r"(\d[\d,]*) of (\d[\d,]*) (.+?) shown · all (\d[\d,]*) in the explorer")
EXPLORER_RE = r'"explorer_base"\s*:\s*(?:"(?:[^"\\]|\\.)*"|null)'     # the explorer stage's (tahoemap/explorer.py)


def _int(s):
    return int(str(s).replace(",", ""))


def map_data(out):
    """(page text, embedded JSON) of OUT/map/gene_map.html."""
    txt = open(os.path.join(out, "map", "gene_map.html"), encoding="utf-8").read()
    m = re.search(r'<script id="tm-data" type="application/json">(.*?)</script>', txt, re.S)
    return txt, json.loads(m.group(1))


# ----------------------------------------------------------------------------- links
def links_checks():
    from tahoemap import links as LK
    bad = []
    site = "https://owner.github.io/repo/"
    for label in ("Idarubicin (hydrochloride)", "HepG2/C3A", "SYM (ENSG00000123)", "a b#c?d%e", "TRIM72"):
        for u in (LK.drug(site, label), LK.line(site, label), LK.gene(site, label, "drugs"), LK.module(site, label),
                  LK.group(site, label), LK.search(site, label)):
            seg = u.split("#/", 1)[1].split("/")[1]
            if urllib.parse.unquote(seg) != label or any(ch in seg for ch in " ()/#?"):
                bad.append((label, u))
    want = {"https://owner.github.io/repo/#/drug/Idarubicin%20%28hydrochloride%29": LK.drug(site, "Idarubicin "
                                                                                          "(hydrochloride)"),
            "https://owner.github.io/repo/#/line/HepG2%2FC3A": LK.line(site, "HepG2/C3A"),
            "https://owner.github.io/repo/#/gene/TRIM72/line/HepG2%2FC3A": LK.gene(site, "TRIM72",
                                                                                 sub=("line", "HepG2/C3A")),
            "https://owner.github.io/repo/#/pair/A%20B/C": LK.pair(site, "A B", "C"),
            "https://owner.github.io/repo/map/gene_map.html#TRIM72": LK.map_gene(site, "TRIM72"),
            "https://owner.github.io/repo/#/dd/12/lines": LK.dd(site, 12, "lines")}
    bad += [(w, g) for w, g in want.items() if w != g]
    remotes = {"https://github.com/xuvictor04/Tahoe100-PseudoManual": ("xuvictor04", "Tahoe100-PseudoManual"),
               "https://github.com/o/r.git": ("o", "r"), "git@github.com:o/r.git": ("o", "r"),
               "ssh://git@github.com/o/r.git": ("o", "r"), "ssh://git@github.com:22/o/r": ("o", "r"),
               "http://local_proxy@127.0.0.1:43173/git/o/r": ("o", "r"), "https://gitlab.com/o/r.git": None,
               "": None}
    bad += [(u, LK.parse_remote(u), w) for u, w in remotes.items() if LK.parse_remote(u) != w]
    if LK.site_url("") is not None or LK.site_url("none") is not None or LK.site_url("https://x.io/r") != \
            "https://x.io/r/":
        bad.append("site_url normalising")
    if any(f(None, "x") is not None for f in (LK.drug, LK.line, LK.module, LK.map_gene, LK.search)) or \
            LK.gene(None, "x") is not None:
        bad.append("a builder without a site does not return None")
    for kw in ({"tab": "nope"}, {"tab": "drugs", "sub": ("line", "A")}, {"sub": ("nope", "A")}):
        try:
            LK.gene(site, "X", **kw)
            bad.append(f"links.gene accepted {kw}")
        except ValueError:
            pass
    return not bad, f"{len(want)} addresses, {len(remotes)} remotes; problems: {bad[:4]}"


# ----------------------------------------------------------------------------- map
def map_stamp_checks(out):
    from tahoemap import html_map as HM
    st = json.load(open(os.path.join(out, "stages", "map.json"), encoding="utf-8"))
    info = st.get("info") or {}
    src = open(HM.__file__, encoding="utf-8").read()
    gone = [x for x in ("_shrink", "_shrink_steps", "MAX_BYTES") if hasattr(HM, x)] + \
        [x for x in ("def _shrink", "MAX_BYTES") if x in src]
    ok = st.get("version") == HM.VERSION == 7 and "shortened" not in info and not gone
    return ok, (f"map stamp version {st.get('version')} (code {HM.VERSION}), 'shortened' in stamp: "
                f"{'shortened' in info}, shortening symbols left: {gone}; {info.get('mb')} MB")


def map_base_checks(out):
    txt, D = map_data(out)
    st = json.load(open(os.path.join(out, "stages", "map.json"), encoding="utf-8")).get("info") or {}
    n_key = txt.count('"explorer_base":')
    site = st.get("site_url", "")
    _new, n_sub = re.subn(EXPLORER_RE, '"explorer_base":"../"', txt)
    ok = n_key == 1 and n_sub == 1 and D.get("explorer_base") == site and f'"explorer_base":"{site}"' in txt
    return ok, (f"explorer_base {D.get('explorer_base')!r} ({n_key} key, the explorer's regex finds {n_sub}); site "
                f"{site!r}")


def map_snippet_checks(out):
    from tahoemap import html_map as HM
    bad = []
    t = "Binds DNA. " * 5 + "Plays a role in the regulation of transcription of many genes, notably of the p53 pathway."
    for n in (20, 40, 110):
        s = HM._snippet(t, n)
        if len(s) > n or not s.endswith("…"):
            bad.append((n, s))
    if HM._snippet("short text", 110) != "short text":
        bad.append("an uncut text changed")
    _txt, D = map_data(out)
    ap = os.path.join(out, "reference", "annotations.parquet")
    n_fn = n_cut = 0
    if os.path.exists(ap) and any(D.get("fn") or []):
        an = pd.read_parquet(ap, columns=[c for c in ("col", "function", "ncbi_summary")
                                          if c in pd.read_parquet(ap).columns])
        by = {int(c): (f, s) for c, f, s in zip(an["col"], an.get("function", [None] * len(an)),
                                                 an.get("ncbi_summary", [None] * len(an)))}
        for e, fn in enumerate(D["fn"]):
            if not fn:
                continue
            n_fn += 1
            f, s = by.get(int(D["col"][e]), (None, None))
            want = HM._snippet(f, HM.FN_CHARS) or HM._snippet(s, HM.FN_CHARS)
            n_cut += fn.endswith("…")
            if fn != want or len(fn) > HM.FN_CHARS:
                bad.append((D["sym"][e], fn[:40]))
    return not bad, (f"_snippet cuts end in '…' within n; {n_fn} snippets on the page ({n_cut} cut, each ending in "
                     f"'…'); problems: {bad[:3]}")


def map_line_checks(out):
    """Each line row of the side panel: the strongest drug-dose up AND down (the *_all columns when the tables stage
    has them), each dd -1 below the per-line cut, and when one carries an alert the strongest without one that way
    (the clean best_* columns) when it reaches the cut."""
    _txt, D = map_data(out)
    W = int(D.get("lnw") or 0)
    if W != 19:
        return False, f"lnw {W}: the page has no up and down blocks"
    cols = ["col", "line"] + [f"best_{d}_{c}{x}" for d in ("up", "down") for c in ("dd", "z", "clean")
                              for x in ("", "_all")]
    le = pd.read_parquet(os.path.join(out, "tables", "line_effects.parquet"))
    le = le[[c for c in cols if c in le.columns]]
    all_ = "best_up_dd_all" in le
    x = "_all" if all_ else ""
    by = {(int(c), int(l_)): r for c, l_, r in zip(le["col"], le["line"], le.to_dict("records"))}
    fl, lz = D["fl"], float(D["line_z"])
    bad, n_rows, n_both, n_clean = [], 0, 0, 0
    for e, a in enumerate(D["ln"]):
        for t in range(0, len(a) - W + 1, W):
            n_rows += 1
            r = by[(int(D["col"][e]), int(a[t]))]
            both = 0
            for o, d, s in ((5, "up", 1), (12, "down", -1)):
                dd, z = r.get(f"best_{d}_dd{x}"), r.get(f"best_{d}_z{x}")
                want = int(dd) if np.isfinite(dd) and np.isfinite(z) and abs(z) >= lz else -1
                both += want >= 0
                if a[t + o] != want or (want >= 0 and abs(a[t + o + 2] / 10 - z) > 0.051):
                    bad.append((D["sym"][e], int(a[t]), d, a[t + o], want))
                    continue
                alert = want >= 0 and a[t + o + 3] > 0 and fl[a[t + o + 3] - 1][1] == 1
                cdd, cz = r.get(f"best_{d}_dd"), r.get(f"best_{d}_z")
                cw = int(cdd) if (all_ and alert and np.isfinite(cdd) and np.isfinite(cz) and abs(cz) >= lz
                                  and int(cdd) != want) else -1
                n_clean += cw >= 0
                if a[t + o + 4] != cw:
                    bad.append((D["sym"][e], int(a[t]), d, "clean", a[t + o + 4], cw))
            n_both += both == 2
    return (not bad and n_rows > 0,
            f"{n_rows:,} line rows; {n_both:,} name a drug-dose both ways (the old page dropped one of them); "
            f"{n_clean:,} also name the strongest without an alert; mismatches {bad[:3]}")


def _fill(t, s, tg):
    return t.replace("\x02", tg).replace("\x01", s)


def decode_dir(dr):
    """The `dir` block's rows, decoded as the page does (dirRow / dirLine)."""
    W, r, out = dr["w"], dr["r"], []
    for k in range(len(r) // W):
        b = k * W
        kgs, ss = r[b], dr["ss"][r[b + 1]]
        kind, gi = kgs & 15, (kgs >> 4) & 3
        cells = bool(dr["sens"][kind])
        S, tgt = dr["nm"][ss[0]], dr["nm"][r[b + 2]]
        T = tgt[12:] if cells and tgt.startswith("cells under ") else tgt

        def tx(i):
            return _fill(dr["tx"][i], S, T) if i >= 0 else ""
        line = (f"{S} → {tgt}  [{dr['grades'][gi]}]  {tx(r[b + 4])} ({dr['kshort'][kind]}; {tx(r[b + 6])})"
                + (f"  {tx(r[b + 7])}" if tx(r[b + 7]) else "") + (f"  · notes: {tx(r[b + 9])}" if tx(r[b + 9])
                                                                     else ""))
        src = [(dr["nm"][ss[t]], ss[t + 1]) for t in range(1, len(ss) - 1, 2)]
        out.append({"line": line, "full": bool(kgs & 512), "reading": tx(r[b + 8]), "alert": bool(kgs & 256),
                    "n_notes": kgs >> 10, "cells": cells, "te": r[b + 3], "src": src})
    return out


def map_direction_checks(out):
    """Every direction_view display row that touches a gene of the page is on the page, in ORDER, with its edge line
    (direction_view.edge_line, notes included); the rows each gene's capped lists show (the cap rule at N_DIR) carry
    their reading; the totals of every list are those of direction_view."""
    from tahoemap import direction_view as DV
    from tahoemap import html_map as HM
    dv = DV.load(out, cache=False)
    _txt, D = map_data(out)
    dr = D.get("dir") or {}
    if dv is None:
        return (not dr.get("ok")), "no direction stage: the page says so" if not dr.get("ok") else "rows without stage"
    ent = {int(c): i for i, c in enumerate(D["col"])}
    want = [r for r in dv.rows.itertuples(index=False) if any(int(c) in ent for c in r.source_cols)
            or (str(r.target_type) != "cells" and int(r.target_col) in ent)]
    rows = decode_dir(dr)
    bad = []
    if len(rows) != len(want):
        bad.append(f"{len(rows)} rows on the page, {len(want)} touch a page gene")
    for k, (g, w) in enumerate(zip(rows, want)):
        if g["line"] != DV.edge_line(w) or g["n_notes"] != len(DV.note_reasons(w)) or g["alert"] != bool(w.has_alert):
            bad.append(("row", k, g["line"][:60], DV.edge_line(w)[:60]))
    # the rows each capped list shows: full (with their reading)
    n_lists = n_short = 0
    pos = {id(w): k for k, w in enumerate(want)}
    for e, c in enumerate(D["col"]):
        for f in (dv.upstream, dv.downstream, dv.cells):
            df = f(int(c))
            if not len(df):
                continue
            n_lists += 1
            shown, _n, _a = DV.cap(df, HM.N_DIR)
            for o_ in shown["order"]:
                k = next((i for i, w in enumerate(want) if int(w.order) == int(o_)), None)
                if k is None or not rows[k]["full"] or (str(want[k].reading or "") and not rows[k]["reading"]):
                    n_short += 1
    del pos
    ok = not bad and not n_short and dr.get("n_rows") == len(want)
    return ok, (f"{len(rows):,} rows on the page = direction_view's {len(want):,} that touch a page gene (edge lines "
                f"equal, notes included); {n_lists} gene lists, every row their cap shows has its reading "
                f"({dr.get('full')} rows with it; {n_short} without); problems {bad[:3]}")


def _browser():
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        return None


def map_panel_checks(out, work):
    """In a headless browser: every preview list of the side panel says 'k of N shown · all N in the explorer' with
    the page's own k (rows shown) and the true N (relations, drug_effects, line_effects, direction_view), and links
    to the gene's explorer page; the same with explorer_base '' (links to ../explorer/web/index.html)."""
    sp = _browser()
    if sp is None:
        return "warn", "Playwright not installed: browser check skipped"
    import pathlib
    from tahoemap import direction_view as DV
    from tahoemap import html_map as HM
    txt, D = map_data(out)
    n = D["n"]
    dv = DV.load(out, cache=False)
    de = pd.read_parquet(os.path.join(out, "tables", "drug_effects.parquet"), columns=["col", "z"])
    up_n = de[de["z"] > 0].groupby("col").size()
    dn_n = de[de["z"] < 0].groupby("col").size()
    le = pd.read_parquet(os.path.join(out, "tables", "line_effects.parquet"), columns=["col", "expressed"])
    meas = le[le["expressed"].astype(bool)].groupby("col").size()
    rel = pd.read_parquet(os.path.join(out, "relations", "gene_relations.parquet"), columns=["col_a"])
    rel_n = rel.groupby("col_a").size()
    # genes: the most direction rows, the most drug-doses up, a gene off the map, one with few rows
    cand = sorted(range(len(D["sym"])), key=lambda i: -(len(dv.downstream(int(D["col"][i]))) if dv else 0))[:2]
    cand += sorted(range(len(D["sym"])), key=lambda i: -int(up_n.get(int(D["col"][i]), 0)))[:2]
    cand += [n] if len(D["sym"]) > n else []
    cand += [D["sym"].index(s) for s in ("CDKN1A", "HMOX1", "TP53") if s in D["sym"]]
    cand = list(dict.fromkeys(cand))
    nolink = os.path.join(work, "_test_no_site.html")
    d2 = dict(D)
    d2["explorer_base"] = ""
    with open(nolink, "w", encoding="utf-8") as fh:
        fh.write(HM.render(d2))
    bad, res, errs = [], {}, []
    try:
        with sp() as p:
            b = p.chromium.launch()
            try:
                for page_path, base in ((os.path.join(out, "map", "gene_map.html"), D.get("explorer_base", "")),
                                        (nolink, "")):
                    pg = b.new_page(viewport={"width": 1300, "height": 800})
                    pg.on("pageerror", lambda e_: errs.append(str(e_)))
                    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                    pg.goto(pathlib.Path(page_path).resolve().as_uri())
                    pg.wait_for_function("() => !!window.TAHOE_MAP")
                    xb = (base if base.endswith(".html") else base + "index.html") if base else \
                        "../explorer/web/index.html"
                    n_labels = 0
                    for i in cand:
                        pg.evaluate(f"TAHOE_MAP.select({i})")
                        panel = pg.evaluate("TAHOE_MAP.panel()")
                        hrefs = pg.evaluate("Array.from(document.querySelectorAll('#panel a.xl')).map(a => "
                                            "a.getAttribute('href'))")
                        c = int(D["col"][i])
                        labels = {m.group(3): (_int(m.group(1)), _int(m.group(2)), _int(m.group(4)))
                                  for m in MAP_KOFN.finditer(panel)}
                        n_labels += len(MAP_KOFN.findall(panel))
                        exp = {"drug-doses raising it": (len(D["up"][i]) // 5, int(up_n.get(c, 0))),
                               "drug-doses lowering it": (len(D["dn"][i]) // 5, int(dn_n.get(c, 0))),
                               "measured lines": (len(D["ln"][i]) // D["lnw"], int(meas.get(c, 0)))}
                        if i < n:
                            exp["partners"] = (len(D["rel"][i]) // 4, int(rel_n.get(c, 0)))
                        for what, (k_, n_) in exp.items():
                            if (not D["up" if "raising" in what else "dn"][i] and "drug-doses" in what):
                                continue                          # no list: the panel says none raise / lower it
                            got = labels.get(what)
                            if got is None or got != (k_, n_, n_):
                                bad.append((D["sym"][i], what, got, (k_, n_)))
                        if dv is not None:
                            for w, f in (("up", dv.upstream), ("dn", dv.downstream), ("ce", dv.cells)):
                                df = f(c)
                                if not len(df):
                                    continue
                                k_ = len(DV.cap(df, HM.N_DIR)[0])
                                hits = [(_int(m.group(1)), _int(m.group(2))) for m in MAP_KOFN.finditer(panel)
                                        if m.group(3) == "rows"]
                                if (k_, len(df)) not in hits:
                                    bad.append((D["sym"][i], w, hits, (k_, len(df))))
                        want_href = xb + "#/gene/" + urllib.parse.quote(D["sym"][i], safe="")
                        if not hrefs or not all(h.startswith(want_href) for h in hrefs if "#/gene/" in h):
                            bad.append((D["sym"][i], "links", hrefs[:2], want_href))
                        if not base and "this output's explorer folder" not in panel:
                            bad.append((D["sym"][i], "no local hint"))
                    res["no site" if not base else "site"] = n_labels
                    pg.close()
            finally:
                b.close()
    except Exception as e:  # noqa: BLE001
        if "Executable doesn't exist" in str(e) or "playwright install" in str(e):
            return "warn", "Playwright's Chromium is not installed: browser check skipped"
        raise
    finally:
        if os.path.exists(nolink):
            os.remove(nolink)
    return (not bad and not errs and all(v > 0 for v in res.values()),
            f"{len(cand)} genes; 'k of N' labels per page: {res}; mismatches {bad[:3]}; script errors {errs[:2]}")


# ----------------------------------------------------------------------------- vault
def vault_paths_checks(out):
    vt = os.path.join(out, "vault")
    p = os.path.join(vt, ".tahoemap-paths.json")
    if not os.path.exists(p):
        return False, "no vault/.tahoemap-paths.json"
    d = json.load(open(p, encoding="utf-8"))
    listed = {k: set(v.values()) for k, v in d.items() if isinstance(v, dict)}
    have = {"gene": set(), "plates": set(), "drug": set(), "line": set(), "module": set(), "plate": set()}
    for root, _d, files in os.walk(vt):
        rel = os.path.relpath(root, vt).replace(os.sep, "/")
        for f in files:
            if not f.endswith(".md"):
                continue
            path = f"{rel}/{f}"
            if rel.startswith("Genes/"):
                have["plates" if f.endswith(" — plates.md") else "gene"].add(path)
            elif rel == "Drugs":
                have["drug"].add(path)
            elif rel == "Cell lines":
                have["line"].add(path)
            elif rel == "Modules":
                have["module"].add(path)
            elif rel == "Plates":
                have["plate"].add(path)
    bad = [(k, len(have[k] ^ listed.get(k, set())), sorted(have[k] ^ listed.get(k, set()))[:2]) for k in have
           if have[k] != listed.get(k, set())]
    g = pd.read_parquet(os.path.join(out, "tables", "genes.parquet"), columns=["col"])
    keys_ok = set(d.get("gene", {})) == {str(int(c)) for c in g["col"]}
    return (not bad and keys_ok, f"{ {k: len(v) for k, v in listed.items()} } note paths listed; every gene col a "
                                 f"key: {keys_ok}; differences from the files: {bad[:3]}")


def _notes(out, folder):
    vt = os.path.join(out, "vault", folder)
    for root, _d, files in os.walk(vt):
        for f in files:
            if f.endswith(".md") and not f.endswith(" — plates.md"):
                yield os.path.join(root, f)


def vault_link_checks(out):
    """'Explorer: ... · Map: ...' under the title of every gene, drug, line and module note; every '(k of N shown;
    all N in the explorer: ...)' has k <= N and an address into the explorer; a gene's drug lists and partner lists
    say their true N; a cut registry text ends in '…' with a link."""
    st = json.load(open(os.path.join(out, "stages", "vault.json"), encoding="utf-8")).get("info") or {}
    site = st.get("site_url", "")
    base = site if site else "explorer/web/index.html"
    bad, n_notes, n_kofn = [], 0, 0
    for folder in ("Genes", "Drugs", "Cell lines", "Modules"):
        for p in _notes(out, folder):
            t = open(p, encoding="utf-8").read()
            n_notes += 1
            head = t.split("\n# ", 1)[1].split("\n")
            top = next((x for x in head[1:] if x.strip()), "")
            if not (top.startswith("Explorer: ") and " · Map: " in top and base in top):
                bad.append((os.path.basename(p), top[:60]))
            for m in KOFN.finditer(t):
                n_kofn += 1
                k, n1, n2, url = _int(m.group(1)), _int(m.group(2)), _int(m.group(3)), m.group(4)
                if not (k <= n1 == n2 and base in url):
                    bad.append((os.path.basename(p), m.group(0)[:80]))
    # a gene's drug lists and partner lists: N = the rows of the tables
    de = pd.read_parquet(os.path.join(out, "tables", "drug_effects.parquet"), columns=["col", "z"])
    paths = json.load(open(os.path.join(out, "vault", ".tahoemap-paths.json"), encoding="utf-8"))["gene"]
    n_up = de[de["z"] > 0].groupby("col").size()
    checked = 0
    for c in n_up.sort_values(ascending=False).index[:20]:
        t = open(os.path.join(out, "vault", paths[str(int(c))]), encoding="utf-8").read()
        sec = t.split("## Drugs that raise it", 1)[1].split("\n## ", 1)[0]
        m = KOFN.search(sec)
        checked += 1
        if not m or _int(m.group(2)) != int(n_up[c]):
            bad.append((int(c), "drugs up", m.group(0) if m else None, int(n_up[c])))
    rel = pd.read_parquet(os.path.join(out, "relations", "gene_relations.parquet"), columns=["col_a", "cos"])
    for c, grp in list(rel.groupby("col_a"))[:20]:
        t = open(os.path.join(out, "vault", paths[str(int(c))]), encoding="utf-8").read()
        sec = t.split("## Genes that move with it", 1)[1].split("\n## ", 1)[0]
        m = KOFN.search(sec)
        n_pos = int((grp["cos"] > 0).sum())
        checked += 1
        if n_pos and (not m or _int(m.group(2)) != n_pos):
            bad.append((int(c), "partners", m.group(0) if m else None, n_pos))
    # registry texts: a cut ends in ' …' and links to the full text
    n_cut = 0
    for p in _notes(out, "Genes"):
        t = open(p, encoding="utf-8").read()
        for blk in re.findall(r"\n> (.+?) \(cut at 500 characters; the full text: ([^)]*)\)", t):
            n_cut += 1
            if not blk[0].endswith(" …") or "#/gene/" not in blk[1]:
                bad.append((os.path.basename(p), "cut text"))
    return (not bad and n_kofn > 0,
            f"{n_notes:,} notes with the top line; {n_kofn:,} 'k of N shown' lists; {checked} gene lists' N checked; "
            f"{n_cut} cut registry texts with a link; problems {bad[:3]}")


def vault_nosite_checks(out):
    """Without a site URL the notes name the run folder's explorer (and the map file), never an empty link."""
    from tahoemap import vault as V
    v = V.Vault(out, site_url="")
    tl = v.top_line(v.xu(V.LK.gene, "TRIM72"), "TRIM72")
    k = v.kofn(3, 10, v.xu(V.LK.drug, "Idarubicin (hydrochloride)"))
    cut = v.clip_full("word " * 200, 0)
    whole = v.clip_full("a short text", 0)
    ok = (v.site is None and "explorer/web/index.html#/gene/TRIM72" in tl and "map/gene_map.html#TRIM72" in tl
          and "(3 of 10 shown; all 10 in the explorer: `explorer/web/index.html#/drug/Idarubicin%20%28hydrochloride"
              "%29`" in k and " … (cut at 500 characters; the full text: " in cut and "/annotation`" in cut
          and whole == "a short text")
    return ok, f"top line: {tl}; list: {k}; a cut registry text ends: ...{cut[-120:]}"


# ----------------------------------------------------------------------------- look-ups
def _run_lookup(out, data, *args):
    cmd = [sys.executable, "-m", "tahoemap", *args, "--out", out] + (["--data", data] if data else [])
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, encoding="utf-8",
                       env=dict(os.environ, PYTHONIOENCODING="utf-8", COLUMNS="120"))
    return r.returncode, r.stdout, r.stderr


def _section(txt, head):
    return txt.split("\n" + head, 1)[1].split("\n\n", 1)[0] if ("\n" + head) in txt else ""


def query_checks(out, data=None):
    """`gene X --top 0` and --top all (query.main) print every row of every list: RAISED BY lists every drug_effects
    row with z > 0, MOVES WITH every partner on that side; no '... more'. The default prints 'all N: <url>' under a
    capped list. query.parse_top. cli.py and '--top all' (warn until cli.py takes it: type=query.parse_top)."""
    from tahoemap import query as Q
    de = pd.read_parquet(os.path.join(out, "tables", "drug_effects.parquet"), columns=["col", "z"])
    g = pd.read_parquet(os.path.join(out, "tables", "genes.parquet"), columns=["col", "label"])
    rel = pd.read_parquet(os.path.join(out, "relations", "gene_relations.parquet"), columns=["col_a", "cos"])
    n_up = de[de["z"] > 0].groupby("col").size()
    n_rel = rel[rel["cos"] > 0].groupby("col_a").size()
    score = (n_up.reindex(g["col"]).fillna(0) + n_rel.reindex(g["col"]).fillna(0) / 10).to_numpy()
    c = int(g["col"].iloc[int(np.argmax(score))])
    lab = str(g.set_index("col").at[c, "label"])
    bad = []
    code, txt, err = _run_lookup(out, data, "gene", lab, "--top", "0")
    a = argparse.Namespace(command="gene", names=[lab], top="all", out=out, data=data)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        Q.main(a)
    txt_all = buf.getvalue()
    for name, t in (("--top 0", txt), ("--top all", txt_all)):
        up = _section(t, "RAISED BY")
        n_rows = len(re.findall(r"^ +\d+ {2}", up, re.M))
        mw = _section(t, "MOVES WITH")
        n_mw = len([x for x in mw.splitlines()[3:] if re.match(r"^  \S", x) and not x.startswith("  ...")
                    and " of its top " not in x and "novelty" not in x])
        more = [x for x in t.splitlines() if re.match(r"^\s*\.\.\. \d[\d,]* more", x)]
        if code != 0 or more or n_rows != int(n_up.get(c, 0)):
            bad.append((name, code, n_rows, int(n_up.get(c, 0)), more[:2]))
        if int(n_rel.get(c, 0)) and n_mw < int(n_rel.get(c, 0)):
            bad.append((name, "partners", n_mw, int(n_rel.get(c, 0))))
    code_d, txt_d, _e = _run_lookup(out, data, "gene", lab)
    alls = re.findall(r"all (\d[\d,]*):\s+(\S+)", txt_d)
    if code_d != 0 or not alls or not all("#/gene/" in u for _n, u in alls):
        bad.append(("default", code_d, alls[:2]))
    pt = [Q.parse_top(x) for x in ("all", "0", "7", None)]
    if pt != [0, 0, 7, None]:
        bad.append(("parse_top", pt))
    code_a, _t, err_a = _run_lookup(out, data, "gene", lab, "--top", "all")
    cli = "takes --top all" if code_a == 0 else "rejects --top all (cli.py: --top needs type=query.parse_top)"
    ok = not bad
    if ok and code_a != 0:
        return "warn", (f"gene {lab}: --top 0 and query.main(top='all') print all {int(n_up.get(c, 0))} drug-doses "
                        f"up and every partner; default lists say 'all N: <url>' ({len(alls)}); cli.py {cli}")
    return ok, (f"gene {lab}: --top 0 / all print every row ({int(n_up.get(c, 0))} drug-doses up, "
                f"{int(n_rel.get(c, 0))} partners with it); default 'all N: <url>' lines {len(alls)}; cli.py {cli}; "
                f"problems {bad[:3]}")


# ----------------------------------------------------------------------------- driver
def check(out, data=None):
    """Every check of this file on a finished output: [(name, ok, detail)], ok True, False or 'warn'."""
    work = tempfile.mkdtemp(prefix="tahoe_surfaces_")
    tests = [("links: quoting of labels, git remotes, no site", links_checks),
             ("map: no shortening (stamp, code)", lambda: map_stamp_checks(out)),
             ("map: the explorer_base key", lambda: map_base_checks(out)),
             ("map: function snippets end in '…' when cut", lambda: map_snippet_checks(out)),
             ("map: line rows carry the strongest drug-dose up AND down", lambda: map_line_checks(out)),
             ("map: every direction row with its edge line; capped rows with their reading",
              lambda: map_direction_checks(out)),
             ("map: 'k of N shown · all N in the explorer' on every preview list (browser)",
              lambda: map_panel_checks(out, work)),
             ("vault: .tahoemap-paths.json lists every note", lambda: vault_paths_checks(out)),
             ("vault: explorer links and counts", lambda: vault_link_checks(out)),
             ("vault: without a site URL the notes name the local explorer", lambda: vault_nosite_checks(out)),
             ("look-ups: --top all prints every row; capped lists print 'all N: <url>'",
              lambda: query_checks(out, data))]
    res = []
    try:
        for name, fn in tests:
            try:
                ok, detail = fn()
            except Exception as ex:  # noqa: BLE001
                ok, detail = False, f"{type(ex).__name__}: {ex}"
            res.append((name, ok, str(detail)))
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--out", default=DEFAULT_OUT, help="a finished output (default: run_tests.py's out_seed0)")
    ap.add_argument("--data", default=None, help="its data folder (default: data_seed0 next to it, when there)")
    a = ap.parse_args()
    data = a.data or os.path.join(os.path.dirname(os.path.abspath(a.out)), "data_seed0")
    data = data if os.path.isdir(data) else None
    if not os.path.exists(os.path.join(a.out, "map", "gene_map.html")):
        print(f"{a.out} has no finished output with a map (run tests/run_tests.py first)")
        sys.exit(2)
    res = check(a.out, data)
    for name, ok, detail in res:
        print(f"{'PASS' if ok is True else 'WARN' if ok == 'warn' else 'FAIL'}  {name}: {detail}", flush=True)
    n_fail = sum(1 for _n, ok, _d in res if ok is not True and ok != "warn")
    print(f"\n{len(res) - n_fail} passed (warnings included), {n_fail} failed")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
