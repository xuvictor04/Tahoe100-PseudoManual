"""html_map - the interactive gene map: one self-contained HTML file, OUT/map/gene_map.html.

No network, no external script or style: vanilla JavaScript on a <canvas>, with every number the page shows computed
here and embedded as one compact JSON block. Open the file in any current browser (also from a USB stick / offline).

What the page shows
    six tabs (docs/DESIGN-review-and-physics.md, part 1); the search box and the side panel belong to all of them, and
    a gene selected on one tab is selected on every tab:
      Nodal map / Signed vector map   the two t-SNE layouts of the graph stage (below); one canvas, switching tabs
                                      animates every gene from one layout to the other
      Physics: neighbourhood          a live force simulation of the selected gene, its partners and (depth 2) their
                                      partners (springs = the embedded top-partner lists, `rel`)
      Physics: module                 a live force simulation of one module (springs = graph/edges.parquet among its
                                      genes; optional dimmed ring of 1-hop outside genes)
      Physics: all genes              every map gene, started from the nodal-map positions (springs = every edge of
                                      graph/edges.parquet; edges drawn for the selected gene only)
      How to read this                the help text
    The physics engine (vanilla JS, typed arrays, one engine for the three tabs): springs on edges (force ∝ |cos| x
    (distance - rest length) / min(degree of the two genes), as d3-force's link force, so hubs stay stable; rest
    length s0 x (1.6 - |cos|): shorter for stronger edges), 1/d repulsion between every pair through a Barnes-Hut
    quadtree (theta 0.8; genes visited in tree order for cache locality), a weak pull to the centre, velocity damping
    and a cooling alpha (d3-force's integration). The sign switch makes red (cos < 0) edges either springs ("opposite
    genes attract": the nodal view) or pushers ("opposite genes repel": push up to 6 rest lengths, no pull beyond: the
    signed view, the - arm parts from the + arm). Drag (a gene's partners follow), double-click to pin, click to
    select, pan / zoom, pause (space), re-heat, reset, fit; sliders for repulsion, springs and minimum |cos|; an
    evidence filter; colour by module or arm; labels for the selected gene, its partners, pinned genes and (zoomed
    in) everyone. The all-genes tab runs as many steps per frame as fit in a ~13 ms budget (one step every other
    frame when one step takes > 45 ms). window.TAHOE_MAP exposes tab(), sim(), screen(), stats(), benchTick() for
    tests (tests/checks.py drives the page with Playwright when it is installed).
    The maps: the NODAL map (graph x, y: genes that respond to the same drugs sit together whether they go up together
    or in opposite directions; the two arms of a pathway form one island) and the SIGNED vector map (graph xs, ys:
    genes that move in opposite directions are pushed apart). Pan (drag), zoom (wheel / pinch), hover (symbol, module
    and arm, name), colour by module (a fixed palette of 20 colours cycled, unassigned grey) or by arm (+ / -), a module legend
    (labels from validation/module_labels.csv, else the module's top genes; click = highlight), a search box with
    autocomplete (symbol, alias, previous symbol, name), and a side panel for the selected gene: name and function
    (reference stage), module and arm, its top partners (green line = moves with it, red = moves opposite; cos,
    evidence, fdr, locus / readthrough / known / novel flags), its top drug-doses up and down (clean rows of
    tables/drug_effects.parquet: fold, z, lines moving) and the cell lines where it responds most
    (tables/line_effects.parquet). Genes that are not in the vector space (too few responsive contexts, no evidence
    of a response beyond that count, noise RNA) are searchable too: the panel then gives their drug-doses and lines,
    and why they are not on the map, as the embed stage's rule with its counts.
    The URL hash selects a gene (gene_map.html#HMOX1), so other documents can link to a gene.

What the page says is the stages' own rule, never more: the per-line counts and 'strongest' use the per-line |z| cut
the tables stage calibrated (tables/info.json; '-' below it); 'both' halves = same sign with fdr <= 0.10 in two random
halves of the compounds, 'one' = strong in one random half only (not replicated); 'novel?' only when
relations/info.json says novelty could be assessed (else which sources were missing); a module's arms are called
opposite only when graph/modules.parquet says so (arms_opposite), and its drug lists are the pooled module z
(graph/module_pooled_z.npy) with |z| >= 1, flagged drug-doses marked with a dagger.

Inputs (read only): graph/nodes.parquet, graph/modules.parquet, graph/module_pooled_z.npy, graph/edges.parquet,
graph/info.json, relations/gene_relations.parquet, relations/info.json,
tables/{genes,drug_effects,line_effects,drugdoses,lines}.parquet, tables/info.json, embed/genes.parquet,
embed/info.json; optional: reference/annotations.parquet, validation/module_labels.csv. Without graph/edges.parquet
(an older graph stage) the module and all-genes tabs fall back to the top-partner lists.

The embedded JSON (<script id="tm-data" type="application/json">; "<" is written as \\u003c). Entries 0..n-1 are
the genes on the map in graph/nodes.parquet order, entries n..n_all-1 the genes that are not on the map (by col).
Scaled integers: cos x100, fdr x100 (-1 = none), lfc x100 (log2), z x10.
    v, title, made, n, scale       version, title, date, number of map genes, the integer scales
    col, sym                       per entry: gene col (atlas/effects/genes.csv row), label (unique symbol)
    x, y, xs, ys                   per map gene: nodal and signed layout, rounded to 2 decimals
    mod, arm                       per map gene: module (0 = unassigned); arm string, one char each: + - or .
    name, fn, alias                per entry (empty lists without the reference stage): HGNC name, a function
                                   snippet (UniProt function, else NCBI summary), aliases and previous symbols "|"
    cpm, nup, ndn, nlx             per entry: pooled CPM, clean drug-doses raising / lowering it, lines expressing
                                   it (tables/genes)
    why                            per off-map entry: -1 noise-class RNA, -2 included but not laid out, else the
                                   number of responsive contexts (embed needs `min_responsive`)
    rel                            per map gene: flat [partner entry, cos, fdr, flags] x top partners (by rank).
                                   flags = evidence (0 not reproduced, 1 one half, 2 both halves) + 4 locus +
                                   8 readthrough_risk + 16 shared_gene_group + 32 known + 64 novel_candidate +
                                   256 * round(STRING score / 10) + 32768 * (index into pw + 1)
    pw                             shared pathway names (rel flags point here)
    up, dn                         per entry: flat [dd, lfc, z, lines moving] x top drug-doses; in dn lfc and z
                                   are stored NEGATED (positive, saves the signs)
    ln                             per entry: flat [line, n dd up, n dd down, dd, lfc, z] x top lines (measured lines
                                   only; n dd up / down at the calibrated per-line cut; dd, lfc, z = the line's
                                   strongest clean drug-dose, up or down; dd -1 = none at |z| >= line_z)
    dd, lines, organ               labels: drug-dose by dd row ("Drug dose uM"), cell line by line index, organ
    mods                           per module: id, n, np, nm, label, genes (top-gene label), plus, minus, opp
                                   (arms_opposite), cb (mean cos between the sides), up, down (pooled module z
                                   >= 1 / <= -1, ' †' = artifact flag), lines (graph/modules)
    palette, ref, labels_from, min_responsive
    embed                          the embed stage's inclusion rule and counts (embed/info.json)
    line_z, line_z_cal, line_chance  the per-line |z| cut, whether it is calibrated, the expected chance calls per
                                   gene x line
    novel_ok, novel_blocked        relations/info.json novel_assessed, novel_blocked_by
    mod_z                          the module card's |z| floor
    edges                          graph/edges.parquet between two map genes, one row per pair (a < b), sorted:
                                   {"m": rows, "bytes": 2 or 4 (index width), "a", "b": base64 of little-endian
                                   unsigned entry indices, "cos": base64 of int8 round(cos x 100), "ev": base64 of
                                   uint8 evidence of the pair in relations (0 not reproduced, 1 one half, 2 both
                                   halves)}: ~6 bytes per edge before base64 (~1.4 MB at 177,000 edges)
    k_edges                        graph/info.json k_edges (partners per gene in the kNN graph), or null
    lit, lit_v                     only when OUT/review holds literature reviews (tahoemap/review): flat [entry a,
                                   entry b, verdict, citations] x the connection verdicts of gene a's review on gene b
                                   (review/connections.parquet) where a and b are partners in `rel` (one way or the
                                   other); lit_v = the verdict names. The side
                                   panel's partner list shows them as a small "lit:" badge (a's verdict on b, else
                                   b's on a). The stamp records vault.review_fingerprint, so a review run makes the
                                   map out of date.
"""

import base64
import json
import os
import re
import time
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import vault as V
from .common import folder, log, stamp_stage

VERSION = 3                    # 3: tabs, the three physics simulations, graph/edges.parquet embedded
N_PARTNERS = 15
N_DRUGS = 8
N_LINES = 5
N_MOD_DRUGS = 10               # module card: drug-doses per direction, with |pooled module z| >= MOD_Z
MOD_Z = 1.0
LINE_Z_FALLBACK = 4.0          # per-line |z| cut when tables/info.json has none (older tables stage: uncalibrated)
FN_CHARS = 110
MAX_BYTES = 16_000_000         # above this the function snippets are shortened, then the line lists
EVIDENCE = {"not reproduced": 0, "one half": 1, "both halves": 2}
# 20 colours for modules (cycled: module m gets PALETTE[(m - 1) % 20]); the first 8 are a CVD-checked categorical
# set on the light surface, the next 12 darker / other hues. Modules are numbered by size, so the big ones get these.
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948",
           "#104281", "#9a6324", "#00695c", "#7d8f00", "#a3307a", "#18a7c9", "#8b1a1a", "#9c7ce8",
           "#7cb518", "#37474f", "#5e2b97", "#bf8040"]


# ----------------------------------------------------------------------------- reading
def _read(path, columns, filters=None):
    """The listed columns that exist in the file (older runs may lack some), optionally row-filtered."""
    import pyarrow.parquet as pq
    have = set(pq.read_schema(path).names)
    cols = [c for c in columns if c in have]
    if filters:
        filters = [f for f in filters if f[0] in have] or None
    return pd.read_parquet(path, columns=cols, filters=filters)


def _bool(df, c):
    if c not in df:
        return np.zeros(len(df), dtype=bool)
    return df[c].fillna(False).astype(bool).to_numpy()


def _num(df, c, fill=np.nan):
    if c not in df:
        return np.full(len(df), fill, dtype=np.float64)
    return pd.to_numeric(df[c], errors="coerce").to_numpy(dtype=np.float64)


def _scaled(x, scale, fill=0):
    """Round x * scale to int; NaN / inf -> fill."""
    x = np.asarray(x, dtype=np.float64) * scale
    ok = np.isfinite(x)
    return np.where(ok, np.rint(np.where(ok, x, 0.0)), fill).astype(np.int64)


def _str(v):
    if v is None:
        return ""
    if isinstance(v, float) and not np.isfinite(v):
        return ""
    s = str(v).strip()
    return "" if s.lower() in ("nan", "none", "<na>") else s


# ----------------------------------------------------------------------------- per-entry lists
def _first_k(ent, k):
    """ent sorted ascending: mask of the first k rows of every run of equal values."""
    ent = np.asarray(ent)
    if ent.size == 0:
        return np.zeros(0, dtype=bool)
    start = np.searchsorted(ent, ent, "left")
    return (np.arange(ent.size) - start) < k


def _lists(ent, mat, n):
    """Rows sorted by entry (ent ascending, rows in display order) -> one flat int list per entry 0..n-1."""
    if len(ent) == 0:
        return [[] for _ in range(n)]
    m = mat.shape[1]
    flat = np.asarray(mat, dtype=np.int64).ravel().tolist()
    lo = np.searchsorted(ent, np.arange(n), "left").tolist()
    hi = np.searchsorted(ent, np.arange(n), "right").tolist()
    return [flat[a * m:b * m] for a, b in zip(lo, hi)]


_TAG = re.compile(r"^\s*\[[^\]]{1,80}\]:\s*")
_REFS = re.compile(r"\s*\((?:PubMed|ECO|By similarity)[^)]*\)")


def _snippet(s, n):
    """The first sentence(s) of a function text, cut at a word boundary to <= n characters."""
    s = _str(s)
    if not s:
        return ""
    s = _TAG.sub("", s)
    s = _REFS.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= n:
        return s
    end = s.rfind(". ", 0, n)
    if end >= n * 0.5:
        return s[:end + 1]
    cut = s[:n].rsplit(" ", 1)[0].rstrip(",;:(")
    return cut + "…"


# ----------------------------------------------------------------------------- module labels
_LABEL_COLS = ("label", "module_label", "name", "title", "top_set", "best_set", "set", "term", "description")


def _validation_labels(out):
    """{module: label} from validation/module_labels.csv (whatever its label column is called), else {}."""
    p = os.path.join(out, "validation", "module_labels.csv")
    if not os.path.exists(p):
        return {}
    try:
        df = pd.read_csv(p)
    except (OSError, ValueError, pd.errors.ParserError) as e:
        log(f"  module_labels.csv unreadable ({e}); labelling modules by their top genes")
        return {}
    low = {c.lower(): c for c in df.columns}
    mcol = low.get("module") or next((c for c in df.columns if "module" in c.lower()
                                      and pd.api.types.is_numeric_dtype(df[c])), None)
    lcol = next((low[c] for c in _LABEL_COLS if c in low and low[c] != mcol), None)
    if lcol is None:
        lcol = next((c for c in df.columns if c != mcol and df[c].dtype == object), None)
    if mcol is None or lcol is None:
        log("  module_labels.csv has no module / label column; labelling modules by their top genes")
        return {}
    out_ = {}
    for m, lab in zip(pd.to_numeric(df[mcol], errors="coerce"), df[lcol]):
        lab = _str(lab)
        if np.isfinite(m) and lab and int(m) not in out_:
            out_[int(m)] = lab[:90]
    return out_


def _top_genes_label(plus, minus, k_plus=3, k_minus=2):
    p = [g.strip() for g in _str(plus).split(",") if g.strip()][:k_plus]
    m = [g.strip() for g in _str(minus).split(",") if g.strip()][:k_minus]
    s = ", ".join(p)
    if m:
        s += " | − " + ", ".join(m)
    return s


def _info(path):
    """A stage's info.json as a dict ({} when missing or unreadable)."""
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh) or {}
    except (OSError, ValueError):
        return {}


def _module_drugs(z, dlab, dart, sign, k=N_MOD_DRUGS, zmin=MOD_Z):
    """The module card's drug-doses one way: up to k with sign * pooled module z >= zmin, strongest first; ' †' marks
    an artifact flag (tables/drugdoses.parquet); 'none with |z| >= 1' when there is none."""
    v = np.nan_to_num(sign * np.asarray(z, dtype=np.float64), nan=-np.inf)
    o = [i for i in np.argsort(-v, kind="stable")[:k] if v[i] >= zmin]
    if not o:
        return f"none with |z| ≥ {zmin:g}"
    lab = (lambda i: dlab[i] if i < len(dlab) and dlab[i] else f"drug-dose {i}")
    art = (lambda i: i < len(dart) and dart[i])
    return "; ".join(lab(i) + (" †" if art(i) else "") + f" ({float(z[i]):+.1f})" for i in o)


# ----------------------------------------------------------------------------- graph edges (physics tabs)
def _b64(arr):
    return base64.b64encode(np.ascontiguousarray(arr).tobytes()).decode("ascii")


def _edge_block(gd, ent, gK, n, pair_keys, pair_ev):
    """graph/edges.parquet between two map genes as compact base64 arrays (module docstring: `edges`).
    pair_keys / pair_ev: sorted keys lo * n + hi of the relations pairs and their best evidence code."""
    p = os.path.join(gd, "edges.parquet")
    if n == 0 or not os.path.exists(p):
        log("  no graph/edges.parquet: the module and all-genes tabs use the top-partner lists")
        return {"m": 0}
    e = _read(p, ["col_a", "col_b", "cos"])
    if not {"col_a", "col_b", "cos"} <= set(e.columns):
        log("  graph/edges.parquet lacks col_a / col_b / cos: the module and all-genes tabs use the top-partner lists")
        return {"m": 0}
    a = e["col_a"].to_numpy(dtype=np.int64)
    b = e["col_b"].to_numpy(dtype=np.int64)
    c = _num(e, "cos")
    ok = (a >= 0) & (a < gK) & (b >= 0) & (b < gK) & np.isfinite(c)
    ea = np.where(ok, ent[np.clip(a, 0, gK - 1)], -1)
    eb = np.where(ok, ent[np.clip(b, 0, gK - 1)], -1)
    ok &= (ea >= 0) & (ea < n) & (eb >= 0) & (eb < n) & (ea != eb)
    lo, hi, c = np.minimum(ea, eb)[ok], np.maximum(ea, eb)[ok], c[ok]
    key = lo * n + hi
    o = np.lexsort((-np.abs(c), key))                       # one row per pair: the strongest
    key, lo, hi, c = key[o], lo[o], hi[o], c[o]
    first = np.r_[True, key[1:] != key[:-1]] if len(key) else np.zeros(0, dtype=bool)
    key, lo, hi, c = key[first], lo[first], hi[first], c[first]
    ev = np.full(len(key), 2, dtype=np.uint8)                 # a graph edge missing from relations: as replicated
    if len(pair_keys) and len(key):
        pos = np.clip(np.searchsorted(pair_keys, key), 0, len(pair_keys) - 1)
        hit = pair_keys[pos] == key
        ev[hit] = pair_ev[pos[hit]]
    width, dt = (2, "<u2") if n <= 65535 else (4, "<u4")
    q = np.clip(np.rint(c * 100), -100, 100).astype(np.int8)
    log(f"  graph edges: {len(key):,} between map genes ({(ev == 2).sum():,} both halves, {(ev == 1).sum():,} one half)")
    return {"m": int(len(key)), "bytes": width, "a": _b64(lo.astype(dt)), "b": _b64(hi.astype(dt)), "cos": _b64(q),
            "ev": _b64(ev)}


# ----------------------------------------------------------------------------- the data block
def build_data(out, partners=N_PARTNERS, drugs=N_DRUGS, lines=N_LINES, fn_chars=FN_CHARS):
    """Everything the page shows, as one dict of lists (see the module docstring for the layout)."""
    gd, td, ed = (os.path.join(out, d) for d in ("graph", "tables", "embed"))
    for p in (os.path.join(gd, "nodes.parquet"), os.path.join(td, "genes.parquet"),
              os.path.join(out, "relations", "gene_relations.parquet")):
        if not os.path.exists(p):
            raise SystemExit(f"map: {p} is missing; run the earlier stages first")

    # ---- entries: map genes (graph order), then every other gene col
    nodes = pd.read_parquet(os.path.join(gd, "nodes.parquet"), columns=["col", "module", "arm", "x", "y", "xs", "ys"])
    tg = _read(os.path.join(td, "genes.parquet"), ["col", "symbol", "label", "pooled_cpm", "noise_rna",
                                                    "n_dd_up_clean", "n_dd_down_clean", "n_lines_expressing"]
               ).sort_values("col")
    gK = int(max(tg["col"].max(), nodes["col"].max())) + 1
    on = nodes["col"].to_numpy(dtype=np.int64)
    is_on = np.zeros(gK, dtype=bool)
    is_on[on] = True
    off = np.array([c for c in tg["col"].to_numpy(dtype=np.int64) if not is_on[c]], dtype=np.int64)
    order = np.concatenate([on, off])
    n, na = len(on), len(order)
    ent = np.full(gK, -1, dtype=np.int64)
    ent[order] = np.arange(na)
    log(f"Map: {n:,} genes on the map, {len(off):,} more searchable")

    lab = np.array([""] * gK, dtype=object)
    lab[tg["col"].to_numpy()] = tg["label"].fillna(tg["symbol"]).astype(str).to_numpy() if "label" in tg else \
        tg["symbol"].astype(str).to_numpy()
    sym = [s or f"col{c}" for s, c in zip(lab[order].tolist(), order.tolist())]

    def per_col(values, fill):
        arr = np.full(gK, fill, dtype=np.float64)
        arr[tg["col"].to_numpy()] = values
        return arr[order]

    cpm = per_col(_num(tg, "pooled_cpm"), np.nan)
    cpm = [round(v, 1) if v < 10 else int(round(v)) for v in np.nan_to_num(cpm, nan=0.0).tolist()]
    nup = per_col(_num(tg, "n_dd_up_clean", 0), 0).astype(np.int64).tolist()
    ndn = per_col(_num(tg, "n_dd_down_clean", 0), 0).astype(np.int64).tolist()
    nlx = per_col(np.nan_to_num(_num(tg, "n_lines_expressing", -1), nan=-1), -1).astype(np.int64).tolist()

    # ---- the stages' own rules and cuts (embed: inclusion; tables: calibrated per-line cut; relations: novelty)
    einfo = _info(os.path.join(ed, "info.json"))
    min_resp = einfo.get("min_responsive")
    embed_rule = {k: einfo.get(k) for k in ("min_responsive", "min_active", "contexts", "drugdoses_active",
                                            "drugdoses_total", "lines", "line_z_responsive", "n_genes_excluded_chance",
                                            "null_rate")}
    tinfo = _info(os.path.join(td, "info.json"))
    line_z_cal = tinfo.get("line_z_threshold") is not None
    line_z = float(tinfo["line_z_threshold"]) if line_z_cal else LINE_Z_FALLBACK
    line_chance = tinfo.get("line_z_expected_chance")
    rinfo = _info(os.path.join(out, "relations", "info.json"))
    if "novel_assessed" in rinfo:
        novel_ok, novel_blocked = bool(rinfo["novel_assessed"]), [str(x) for x in rinfo.get("novel_blocked_by") or []]
    else:                                         # older relations stage: novelty needed the reference stage
        novel_ok = os.path.exists(os.path.join(out, "reference", "annotations.parquet"))
        novel_blocked = [] if novel_ok else ["the reference stage"]
    why = [-2] * len(off)
    if os.path.exists(os.path.join(ed, "genes.parquet")) and len(off):
        eg = _read(os.path.join(ed, "genes.parquet"), ["col", "included", "n_responsive_contexts", "noise_rna"])
        nr = np.full(gK, -2, dtype=np.int64)
        resp = np.nan_to_num(_num(eg, "n_responsive_contexts", 0), nan=0).astype(np.int64)
        v = np.where(_bool(eg, "noise_rna"), -1, np.where(_bool(eg, "included"), -2, resp))
        nr[eg["col"].to_numpy(dtype=np.int64)] = v
        why = nr[off].tolist()

    # ---- reference annotations (optional)
    name, fn, alias = [], [], []
    ap = os.path.join(out, "reference", "annotations.parquet")
    have_ref = os.path.exists(ap)
    if have_ref:
        an = _read(ap, ["col", "symbol", "hgnc_symbol", "name", "protein_name", "function", "ncbi_summary",
                        "aliases", "prev_symbols"])
        acol = an["col"].to_numpy(dtype=np.int64)
        keep = (acol >= 0) & (acol < gK)
        an, acol = an[keep], acol[keep]
        nm = np.array([""] * gK, dtype=object)
        fx = np.array([""] * gK, dtype=object)
        al = np.array([""] * gK, dtype=object)
        cols = {c: (an[c].tolist() if c in an else [None] * len(an)) for c in
                ("symbol", "hgnc_symbol", "name", "protein_name", "function", "ncbi_summary", "aliases",
                 "prev_symbols")}
        for i, c in enumerate(acol.tolist()):
            nm[c] = _str(cols["name"][i]) or _str(cols["protein_name"][i])
            fx[c] = _snippet(cols["function"][i], fn_chars) or _snippet(cols["ncbi_summary"][i], fn_chars)
            own = _str(cols["symbol"][i]).upper()
            names = []
            hs = _str(cols["hgnc_symbol"][i])
            if hs and hs.upper() != own:
                names.append(hs)
            for f in ("aliases", "prev_symbols"):
                names += [t.strip() for t in re.split(r"[|,;]", _str(cols[f][i])) if t.strip()]
            seen, keep_ = {own}, []
            for t in names:
                if t.upper() not in seen:
                    seen.add(t.upper())
                    keep_.append(t)
            al[c] = "|".join(keep_)
        name, fn, alias = nm[order].tolist(), fx[order].tolist(), al[order].tolist()
        log(f"  reference: {sum(1 for s in name if s):,} names, {sum(1 for s in fn if s):,} function snippets")
    else:
        log("  no reference annotations: names, functions and aliases are left out")

    # ---- relations: top partners per map gene (by the relations rank)
    rel = _read(os.path.join(out, "relations", "gene_relations.parquet"),
                ["col_a", "col_b", "rank", "cos", "abs_cos", "evidence", "fdr", "locus", "readthrough_risk",
                 "shared_gene_group", "shared_pathway", "string_score", "known", "novel_candidate"])
    a = rel["col_a"].to_numpy(dtype=np.int64)
    b = rel["col_b"].to_numpy(dtype=np.int64)
    ok = (a >= 0) & (a < gK) & (b >= 0) & (b < gK)
    ea = np.where(ok, ent[np.clip(a, 0, gK - 1)], -1)
    eb = np.where(ok, ent[np.clip(b, 0, gK - 1)], -1)
    ok &= (ea >= 0) & (ea < n) & (eb >= 0) & (eb < n)
    rel = rel[ok].reset_index(drop=True)
    ea, eb = ea[ok], eb[ok]
    # every pair's best evidence (before the top-k cut): the graph edges below carry it
    ev_all = rel["evidence"].map(EVIDENCE).fillna(0).astype(np.int64).to_numpy() if "evidence" in rel else \
        np.zeros(len(rel), dtype=np.int64)
    pev = pd.Series(ev_all).groupby(np.minimum(ea, eb) * n + np.maximum(ea, eb)).max()
    pair_keys, pair_ev = pev.index.to_numpy(dtype=np.int64), pev.to_numpy().astype(np.uint8)
    del ev_all, pev
    rank = _num(rel, "rank") if "rank" in rel else -np.abs(_num(rel, "cos"))
    o = np.lexsort((np.nan_to_num(rank, nan=1e9), ea))
    rel, ea, eb = rel.iloc[o].reset_index(drop=True), ea[o], eb[o]
    k = _first_k(ea, partners)
    rel, ea, eb = rel[k].reset_index(drop=True), ea[k], eb[k]
    ev = rel["evidence"].map(EVIDENCE).fillna(0).astype(np.int64).to_numpy() if "evidence" in rel else \
        np.zeros(len(rel), dtype=np.int64)
    pw_names = rel["shared_pathway"].map(_str) if "shared_pathway" in rel else pd.Series([""] * len(rel))
    codes, pw = pd.factorize(pw_names.where(pw_names != "", None))
    sscore = np.clip(_scaled(_num(rel, "string_score"), 0.1, 0), 0, 127)
    flags = (ev + 4 * _bool(rel, "locus") + 8 * _bool(rel, "readthrough_risk") + 16 * _bool(rel, "shared_gene_group")
             + 32 * _bool(rel, "known") + 64 * _bool(rel, "novel_candidate") + 256 * sscore
             + 32768 * (codes.astype(np.int64) + 1))
    rmat = np.column_stack([eb, _scaled(_num(rel, "cos"), 100), _scaled(_num(rel, "fdr"), 100, -1), flags])
    rel_lists = _lists(ea, rmat, n)
    shown_pairs = np.unique(np.minimum(ea, eb) * n + np.maximum(ea, eb))   # the side panel's partner pairs
    log(f"  relations: {len(rel):,} partner rows for {int((np.diff(np.r_[-1, ea]) != 0).sum()):,} genes, "
        f"{len(pw):,} shared pathways")
    del rel
    edges = _edge_block(gd, ent, gK, n, pair_keys, pair_ev)
    del pair_keys, pair_ev
    k_edges = _info(os.path.join(gd, "info.json")).get("k_edges")

    # ---- drug-doses up / down (clean rows of the fold-change table)
    de = _read(os.path.join(td, "drug_effects.parquet"),
               ["col", "dd", "lfc", "z", "clean", "n_lines_up", "n_lines_down"],
               filters=[("clean", "==", True)])
    if "clean" in de:
        de = de[de["clean"].fillna(False).astype(bool)]
    dc = de["col"].to_numpy(dtype=np.int64)
    de_ent = np.where((dc >= 0) & (dc < gK), ent[np.clip(dc, 0, gK - 1)], -1)
    z = _num(de, "z")
    up_lists, dn_lists = [], []
    for sign, nl_col, store in ((1, "n_lines_up", up_lists), (-1, "n_lines_down", dn_lists)):
        m = (de_ent >= 0) & np.isfinite(z) & (sign * z > 0)
        e, zz = de_ent[m], sign * z[m]
        o = np.lexsort((-zz, e))
        idx = np.flatnonzero(m)[o]
        e = e[o]
        kk = _first_k(e, drugs)
        idx, e = idx[kk], e[kk]
        sub = de.iloc[idx]
        mat = np.column_stack([_num(sub, "dd").astype(np.int64), _scaled(sign * _num(sub, "lfc"), 100),
                               _scaled(sign * _num(sub, "z"), 10), _scaled(_num(sub, nl_col), 1)])
        store.extend(_lists(e, mat, na))
    log(f"  drug-doses: {len(de):,} clean rows -> top {drugs} up / down per gene")
    del de

    # ---- cell lines where the gene responds most
    le = _read(os.path.join(td, "line_effects.parquet"),
               ["col", "line", "expressed", "response_sd", "n_dd_up", "n_dd_down", "best_up_dd", "best_up_lfc",
                "best_up_z", "best_down_dd", "best_down_lfc", "best_down_z"])
    if "expressed" in le:
        le = le[le["expressed"].fillna(False).astype(bool)]
    lc = le["col"].to_numpy(dtype=np.int64)
    le_ent = np.where((lc >= 0) & (lc < gK), ent[np.clip(lc, 0, gK - 1)], -1)
    nu = np.nan_to_num(_num(le, "n_dd_up", 0), nan=0)
    nd = np.nan_to_num(_num(le, "n_dd_down", 0), nan=0)
    sd = np.nan_to_num(_num(le, "response_sd"), nan=-1)
    score = nu + nd
    m = le_ent >= 0
    o = np.lexsort((-sd[m], -score[m], le_ent[m]))
    idx = np.flatnonzero(m)[o]
    e = le_ent[idx]
    # lines with responding drug-doses (up to `lines`); a gene with none in any line keeps its 2 most variable lines
    has_any = np.zeros(na, dtype=bool)
    has_any[e[score[idx] > 0]] = True
    keep = _first_k(e, lines) & ((score[idx] > 0) | (~has_any[e] & _first_k(e, 2)))
    idx, e = idx[keep], e[keep]
    bu, bd = _num(le, "best_up_z")[idx], _num(le, "best_down_z")[idx]
    use_up = np.nan_to_num(bu, nan=-np.inf) >= -np.nan_to_num(bd, nan=np.inf)
    bdd = np.where(use_up, _num(le, "best_up_dd")[idx], _num(le, "best_down_dd")[idx])
    blfc = np.where(use_up, _num(le, "best_up_lfc")[idx], _num(le, "best_down_lfc")[idx])
    bz = np.where(use_up, bu, bd)
    bdd = np.where(np.isfinite(bdd) & np.isfinite(bz) & (np.abs(np.nan_to_num(bz)) >= line_z), bdd, -1)
    lmat = np.column_stack([_num(le, "line")[idx].astype(np.int64), nu[idx].astype(np.int64),
                            nd[idx].astype(np.int64), bdd.astype(np.int64),
                            _scaled(blfc, 100), _scaled(bz, 10)])
    ln_lists = _lists(e, lmat, na)
    log(f"  cell lines: {len(le):,} gene x line rows -> up to {lines} lines per gene")
    del le

    # ---- labels: drug-doses, lines, modules
    dlab, dart = [], []
    dp = os.path.join(td, "drugdoses.parquet")
    if os.path.exists(dp):
        dd = _read(dp, ["dd", "drug", "dose", "flags"])
        ddi = dd["dd"].to_numpy(dtype=np.int64) if "dd" in dd else np.arange(len(dd))
        dlab = [""] * (int(ddi.max()) + 1 if len(ddi) else 0)
        dart = [False] * len(dlab)
        fl = dd["flags"].map(_str) if "flags" in dd else pd.Series([""] * len(dd))
        for i, d_, s_, f_ in zip(ddi.tolist(), dd["drug"].map(_str), dd["dose"].map(_str), fl):
            dlab[i] = f"{d_} {s_} uM".strip()
            dart[i] = A.has_artifact(f_)
    llab, organ = [], []
    lp = os.path.join(td, "lines.parquet")
    if os.path.exists(lp):
        li = _read(lp, ["line", "cell_name", "cell_line_id", "Organ"])
        lii = li["line"].to_numpy(dtype=np.int64) if "line" in li else np.arange(len(li))
        size = int(lii.max()) + 1 if len(lii) else 0
        llab, organ = [""] * size, [""] * size
        cn = li["cell_name"].map(_str) if "cell_name" in li else pd.Series([""] * len(li))
        cid = li["cell_line_id"].map(_str) if "cell_line_id" in li else pd.Series([""] * len(li))
        org = li["Organ"].map(_str) if "Organ" in li else pd.Series([""] * len(li))
        for i, c_, d_, o_ in zip(lii.tolist(), cn, cid, org):
            llab[i], organ[i] = c_ or d_ or f"line {i}", o_

    vlab = _validation_labels(out)
    mods = []
    mp = os.path.join(gd, "modules.parquet")
    if os.path.exists(mp):
        md = pd.read_parquet(mp).sort_values("module").reset_index(drop=True)
        zp = os.path.join(gd, "module_pooled_z.npy")
        MZ = np.load(zp) if os.path.exists(zp) else None
        if MZ is not None and MZ.shape[0] != len(md):
            log(f"  module_pooled_z.npy has {MZ.shape[0]} rows for {len(md)} modules: drug lists from modules.parquet")
            MZ = None
        for k, r in enumerate(md.to_dict("records")):
            mid = int(r["module"])
            fallback = _top_genes_label(r.get("top_plus"), r.get("top_minus"))
            opp = bool(r["arms_opposite"]) if r.get("arms_opposite") is not None else int(r.get("n_minus", 0)) > 0
            cb = r.get("mean_cos_between_arms")
            cb = round(float(cb), 2) if cb is not None and np.isfinite(float(cb)) else None
            if MZ is not None:
                up, down = _module_drugs(MZ[k], dlab, dart, 1), _module_drugs(MZ[k], dlab, dart, -1)
            else:                                 # older graph stage: its unfiltered lists
                up, down = _str(r.get("drugs_up")), _str(r.get("drugs_down"))
            mods.append({"id": mid, "n": int(r.get("n_genes", 0)), "np": int(r.get("n_plus", 0)),
                         "nm": int(r.get("n_minus", 0)), "label": vlab.get(mid) or fallback,
                         "genes": fallback, "plus": _str(r.get("top_plus")), "minus": _str(r.get("top_minus")),
                         "opp": opp, "cb": cb, "up": up, "down": down, "lines": _str(r.get("responsive_lines"))})
    labels_from = "validation" if vlab else "graph"

    def xy(c):
        v = nodes[c].to_numpy(dtype=np.float64)
        return np.round(np.nan_to_num(v, nan=0.0, posinf=0.0, neginf=0.0), 2).tolist()

    arm = "".join(a if a in ("+", "-") else "." for a in nodes["arm"].fillna("").astype(str).tolist())
    lit = _literature(out, tg, ent, gK, n, shown_pairs)
    return {
        "v": VERSION, "title": "Tahoe-100M gene map", "made": time.strftime("%Y-%m-%d"),
        "n": n, "scale": {"cos": 100, "fdr": 100, "lfc": 100, "z": 10},
        "col": order.tolist(), "sym": sym,
        "x": xy("x"), "y": xy("y"), "xs": xy("xs"), "ys": xy("ys"),
        "mod": nodes["module"].fillna(0).astype(np.int64).tolist(), "arm": arm,
        "name": name, "fn": fn, "alias": alias,
        "cpm": cpm, "nup": nup, "ndn": ndn, "nlx": nlx, "why": why,
        "rel": rel_lists, "pw": [str(p) for p in pw],
        "up": up_lists, "dn": dn_lists, "ln": ln_lists,
        "dd": dlab, "lines": llab, "organ": organ, "mods": mods,
        "palette": PALETTE, "ref": bool(have_ref), "labels_from": labels_from, "min_responsive": min_resp,
        "embed": embed_rule, "line_z": round(line_z, 2), "line_z_cal": line_z_cal,
        "line_chance": round(float(line_chance), 3) if line_chance is not None else None,
        "novel_ok": novel_ok, "novel_blocked": novel_blocked, "mod_z": MOD_Z,
        "edges": edges, "k_edges": int(k_edges) if isinstance(k_edges, (int, float)) else None,
        **lit,
    }


def _literature(out, tg, ent, gK, n, shown_pairs):
    """The gene-gene connection verdicts of the literature reviews (OUT/review) on the side panel's partner pairs
    (shown_pairs: sorted min(a, b) * n + max(a, b) of the embedded top-partner lists), as the {"lit": [...],
    "lit_v": [...]} entries of the page data; {} without reviews (the page is then as before)."""
    if V.review_fingerprint(out) is None:
        return {}
    by = {}
    labels = tg["label"] if "label" in tg else tg["symbol"]
    for c, s_, lab in zip(tg["col"].to_numpy(dtype=np.int64), tg["symbol"].map(_str), labels.map(_str)):
        for k in (lab, s_):
            if k:
                by.setdefault(k.upper(), int(c))
    names = list(V.VERDICTS)
    flat = []
    for r in V.review_connections(out, gene_col=lambda x: by.get(str(x).upper())):
        eid, pk = _str(r.get("entity_id")), _str(r.get("partner_kind")) or "gene"
        pc = r.get("partner_col")
        if not eid.startswith("gene:") or pk != "gene" or not eid[5:].isdigit() or pc is None or pd.isna(pc):
            continue
        a, b = int(eid[5:]), int(pc)
        if not (0 <= a < gK and 0 <= b < gK) or ent[a] < 0 or ent[a] >= n or ent[b] < 0 or ent[b] >= n:
            continue
        key = min(ent[a], ent[b]) * n + max(ent[a], ent[b])
        i = np.searchsorted(shown_pairs, key)
        if i >= len(shown_pairs) or shown_pairs[i] != key:
            continue                                       # not a pair the side panel lists
        v = _str(r.get("verdict"))
        if not v:
            continue
        if v not in names:
            names.append(v)
        flat += [int(ent[a]), int(ent[b]), names.index(v), int(len([x for x in _str(r.get("citations")).split(";")
                                                                      if x.strip()]))]
    log(f"  literature: {len(flat) // 4:,} connection verdicts on the side panel's partner pairs "
        "(review/connections.parquet)")
    return {"lit": flat, "lit_v": names}


def _encode(data):
    """Compact JSON that is safe inside a <script> element."""
    s = json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return s.replace("<", "\\u003c")


def _shrink(data, fn_chars, lines):
    """Shorter function snippets and line lists (only when the page would be too large)."""
    data["fn"] = [s if len(s) <= fn_chars else _snippet(s, fn_chars) for s in data["fn"]]
    if lines is not None:
        data["ln"] = [v[:6 * lines] for v in data["ln"]]
    return data


def render(data):
    payload = _encode(data)
    title = data.get("title", "gene map").replace("<", "").replace("&", "and")
    return _TEMPLATE.replace("__TITLE__", title).replace("__DATA__", payload)


def run(out, partners=N_PARTNERS, drugs=N_DRUGS, lines=N_LINES, fn_chars=FN_CHARS, max_bytes=MAX_BYTES):
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    md = folder(out, "map")
    with np.errstate(invalid="ignore", divide="ignore"):
        data = build_data(out, partners=partners, drugs=drugs, lines=lines, fn_chars=fn_chars)
    page = render(data)
    size = len(page.encode("utf-8"))
    for fc, nl in ((80, None), (60, 3), (40, 2)):          # keep the page loadable on a laptop
        if size <= max_bytes:
            break
        log(f"  page is {size / 1e6:.1f} MB: shortening function snippets to {fc} characters"
            + (f" and line lists to {nl}" if nl else ""))
        page = render(_shrink(data, fc, nl))
        size = len(page.encode("utf-8"))
    path = os.path.join(md, "gene_map.html")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(page)
    os.replace(tmp, path)
    n_rel = sum(1 for r in data["rel"] if r)
    info = {"version": VERSION, "file": path, "bytes": size, "mb": round(size / 1e6, 2),
            "genes_on_map": data["n"], "genes_searchable": len(data["sym"]), "genes_with_partners": n_rel,
            "graph_edges": data["edges"].get("m", 0), "graph_edges_bytes": sum(len(data["edges"].get(k, ""))
                                                                              for k in ("a", "b", "cos", "ev")),
            "modules": len(data["mods"]), "module_labels_from": data["labels_from"], "reference": data["ref"],
            "partners": partners, "drugs": drugs, "lines": lines,
            "literature_verdicts": len(data.get("lit") or []) // 4, "review": V.review_fingerprint(out),
            "minutes": round((time.time() - t0) / 60, 2)}
    stamp_stage(out, "map", VERSION, info)
    log(f"Map done: {path} ({info['mb']} MB, {data['n']:,} genes on the map, {info['minutes']} min)")
    return info


# ----------------------------------------------------------------------------- the page
_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<title>__TITLE__</title>
<style>
:root{--surface:#fcfcfb;--page:#f9f9f7;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;
--ring:rgba(11,11,11,.12);--with:#0ca30c;--opp:#d03b3b;--accent:#2a78d6;--hl:#eef3fb}
*{box-sizing:border-box}
html,body{margin:0;height:100%;font:13px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--page)}
body{display:flex;flex-direction:column;overflow:hidden}
header{display:flex;align-items:flex-end;gap:4px 16px;padding:0 12px;border-bottom:1px solid var(--grid);background:var(--surface);flex-wrap:wrap}
header h1{font-size:15px;margin:0 2px 11px 0;font-weight:600;white-space:nowrap}
#tabs{display:flex;flex-wrap:wrap}
#tabs button{border:0;border-bottom:2px solid transparent;background:transparent;padding:12px 9px 9px;font:inherit;cursor:pointer;color:var(--ink2);white-space:nowrap}
#tabs button:hover{color:var(--ink);background:var(--hl)}
#tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--ink);font-weight:600}
#tabs .ph{color:var(--muted);font-weight:400}
.grp{display:flex;align-items:center;gap:6px;color:var(--ink2);white-space:nowrap}
.seg{display:inline-flex;border:1px solid var(--axis);border-radius:6px;overflow:hidden;flex:none}
.seg button{border:0;background:transparent;padding:5px 10px;font:inherit;cursor:pointer;color:var(--ink2);white-space:nowrap}
.seg button+button{border-left:1px solid var(--axis)}
.seg button[aria-pressed="true"]{background:var(--ink);color:#fff}
.btn{border:1px solid var(--axis);background:transparent;border-radius:6px;padding:5px 10px;font:inherit;cursor:pointer;color:var(--ink2);white-space:nowrap}
.btn:hover,.seg button:hover{background:var(--hl);color:var(--ink)}
.seg button[aria-pressed="true"]:hover{background:var(--ink);color:#fff}
#sw{position:relative;margin:7px 0 7px auto}
#q{width:230px;padding:5px 8px;border:1px solid var(--axis);border-radius:6px;font:inherit;background:#fff}
#q:focus{outline:2px solid var(--accent);outline-offset:-1px}
#ac{position:absolute;top:calc(100% + 3px);right:0;z-index:30;background:#fff;border:1px solid var(--axis);border-radius:6px;box-shadow:0 6px 18px rgba(0,0,0,.12);max-height:360px;overflow:auto;display:none;min-width:340px}
#ac div{padding:5px 9px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#ac div.on,#ac div:hover{background:var(--hl)}
#ac b{font-weight:600}
#ac .m{color:var(--muted)}
main{flex:1;display:flex;min-height:0}
#stage{flex:1;display:flex;flex-direction:column;min-width:0}
.pane{flex:1;display:none;flex-direction:column;min-height:0}
.pane.on{display:flex}
.bar{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;padding:6px 10px;border-bottom:1px solid var(--grid);background:var(--surface);color:var(--ink2)}
.bars{border-bottom:1px solid var(--grid);background:var(--surface)}
.bars .bar{border-bottom:0}
.bars .bar+.bar{padding-top:0}
.bar .seg button{padding:3px 9px}
.bar .btn{padding:3px 9px}
.bar select,.bar input[type=number]{font:inherit;padding:2px 4px;border:1px solid var(--axis);border-radius:5px;background:#fff;color:var(--ink)}
.rng{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.rng input{width:84px;accent-color:#52514e;margin:0}
.rng output{display:inline-block;min-width:26px;color:var(--ink);font-variant-numeric:tabular-nums}
.wrap{flex:1;position:relative;min-height:0;background:var(--surface);overflow:hidden}
.wrap canvas{position:absolute;inset:0;width:100%;height:100%;display:block;cursor:grab;touch-action:none}
.wrap canvas.drag{cursor:grabbing}
.wrap canvas.onnode{cursor:pointer}
.tip{position:absolute;pointer-events:none;background:#fff;border:1px solid var(--ring);border-radius:6px;padding:5px 8px;box-shadow:0 2px 10px rgba(0,0,0,.14);display:none;max-width:340px;z-index:5}
.tip b{font-size:13px}
.tip .m{color:var(--ink2)}
.status{position:absolute;right:10px;bottom:5px;max-width:calc(100% - 20px);color:var(--ink2);font-size:12px;pointer-events:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;background:rgba(252,252,251,.88);border-radius:4px;padding:1px 6px}
.status:empty{display:none}
.info{position:absolute;left:10px;top:10px;max-width:min(470px,calc(100% - 20px));background:rgba(252,252,251,.94);border:1px solid var(--ring);border-radius:8px;padding:6px 9px;z-index:4;color:var(--ink2);pointer-events:none}
.info.none{display:none}
.info b{color:var(--ink)}
.info .ky{margin-top:3px;font-size:12px;color:var(--muted)}
.info .ky span.it{white-space:nowrap;margin-right:9px}
.info .ictl{pointer-events:auto;display:flex;flex-wrap:wrap;align-items:center;gap:5px 8px;margin:0 0 6px;padding:0 0 6px;border-bottom:1px solid var(--grid)}
.info .ictl select{font:inherit;padding:2px 4px;border:1px solid var(--axis);border-radius:5px;background:#fff;color:var(--ink);max-width:290px}
.info .ictl .btn{padding:2px 8px}
.info .ictl label{display:flex;align-items:center;gap:4px;white-space:nowrap}
.msg{position:absolute;inset:0;display:none;align-items:center;justify-content:center;text-align:center;padding:40px 15%;color:var(--ink2);font-size:14px;pointer-events:none}
.msg.on{display:flex}
.key{display:inline-block;width:16px;height:0;border-top:3px solid;vertical-align:middle;margin:0 3px 0 0}
.keyd{display:inline-block;width:16px;height:0;border-top:2px dashed;vertical-align:middle;margin:0 3px 0 0}
#legend{position:absolute;left:10px;top:10px;max-height:calc(100% - 46px);width:270px;display:flex;flex-direction:column;background:rgba(252,252,251,.95);border:1px solid var(--ring);border-radius:8px;z-index:4}
#legend .hd{display:flex;align-items:center;justify-content:space-between;padding:6px 8px;border-bottom:1px solid var(--grid);font-weight:600}
#legend .hd button{border:0;background:transparent;cursor:pointer;color:var(--ink2);font:inherit;padding:0 4px}
#lgbody{overflow:auto;padding:4px 0}
#legend.closed #lgbody,#legend.closed #armkey{display:none}
#armkey{padding:6px 8px;border-bottom:1px solid var(--grid);display:none;color:var(--ink2)}
.li{display:flex;align-items:center;gap:7px;padding:2px 8px;cursor:pointer;white-space:nowrap}
.li:hover{background:var(--hl)}
.li.on{background:#dde8f8}
.li .t{overflow:hidden;text-overflow:ellipsis;flex:1;color:var(--ink)}
.li .n{color:var(--muted);font-variant-numeric:tabular-nums}
.sw{display:inline-block;width:10px;height:10px;border-radius:50%;flex:none}
aside{width:440px;flex:none;border-left:1px solid var(--grid);overflow:auto;background:var(--surface);padding:12px 16px 30px}
aside h2{font-size:20px;margin:0 0 2px}
aside h3{font-size:13px;margin:16px 0 5px;color:var(--ink);font-weight:600;border-bottom:1px solid var(--grid);padding-bottom:3px}
aside .nm{color:var(--ink2);font-size:14px}
aside .fn{color:var(--ink2);margin:6px 0}
.note{color:var(--muted);font-size:12px}
aside p{margin:6px 0}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}
th{text-align:left;font-weight:600;color:var(--ink2);font-size:12px;border-bottom:1px solid var(--grid);padding:3px 4px}
td{padding:2px 4px;border-bottom:1px solid #f0efea;vertical-align:top}
td.r,th.r{text-align:right}
tr.ck{cursor:pointer}
tr.ck:hover td{background:var(--hl)}
.k{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:4px;vertical-align:baseline}
.bd{display:inline-block;font-size:11px;line-height:15px;padding:0 5px;border-radius:9px;border:1px solid var(--axis);color:var(--ink2);margin:1px 2px 1px 0;white-space:nowrap}
table.pt td:first-child{white-space:nowrap}
.bd.nov{border-color:#6250d6;color:#4a3aa7}
.bd.loc{border-color:#eda100;color:#7a5200}
.bd.rt{border-color:#d03b3b;color:#a02020}
.bd.lit{border-color:#2a78d6;color:#104281;background:#eef4fb}
.bd.lit.lit-contradicted{border-color:#d03b3b;color:#a02020;background:#fbeeee}
a,.lk{color:var(--accent);cursor:pointer;text-decoration:none}
a:hover,.lk:hover{text-decoration:underline}
.mcard{background:#f4f6f9;border:1px solid var(--grid);border-radius:8px;padding:8px 10px;margin:0 0 10px}
.mcard .row{margin:3px 0}
.mcard .lbl{color:var(--muted);font-size:12px}
.helpwrap{flex:1;overflow:auto;padding:14px 28px 40px;background:var(--surface)}
.howto{max-width:880px}
.howto h3{font-size:15px;margin:14px 0 4px}
.howto h4{margin:12px 0 3px;font-size:13px}
.howto p,.howto li{color:var(--ink2);margin:3px 0}
.howto ul{padding-left:18px;margin:4px 0}
@media (max-width:1280px){#tabs button{padding:12px 6px 9px}#q{width:165px}#ac{min-width:300px}header{gap:4px 10px}}
</style>
</head>
<body>
<header>
  <h1>Tahoe-100M gene map</h1>
  <nav id="tabs" role="tablist" aria-label="Displays">
    <button role="tab" data-tab="nodal" aria-selected="true" title="t-SNE of 1 - |cos|: genes that respond to the same drugs sit together, also when they move in opposite directions">Nodal map</button>
    <button role="tab" data-tab="signed" aria-selected="false" title="t-SNE of 1 - cos: genes that move in opposite directions are pushed apart">Signed vector map</button>
    <button role="tab" data-tab="nbr" aria-selected="false" title="A live force simulation of the selected gene, its partners and their partners"><span class="ph">Physics:</span> neighbourhood</button>
    <button role="tab" data-tab="mod" aria-selected="false" title="A live force simulation of one module: its genes and the graph edges among them"><span class="ph">Physics:</span> module</button>
    <button role="tab" data-tab="all" aria-selected="false" title="A live force simulation of every gene on the map, started from the nodal-map positions"><span class="ph">Physics:</span> all genes</button>
    <button role="tab" data-tab="help" aria-selected="false">How to read this</button>
  </nav>
  <div class="grp" id="sw"><input id="q" type="search" placeholder="Search a gene (symbol, alias, name)" autocomplete="off" spellcheck="false" aria-label="Search a gene"><div id="ac" role="listbox"></div></div>
</header>
<main>
  <section id="stage">
    <div class="pane on" id="pane-map" role="tabpanel">
      <div class="bar">
        <div class="grp">Colour <span class="seg"><button id="c0" aria-pressed="true">Module</button><button id="c1" aria-pressed="false">Arm (+ / &minus;)</button></span></div>
        <button class="btn" id="fitb" title="Show every gene">Reset view</button>
        <span class="note" id="mapnote"></span>
      </div>
      <div class="wrap" id="mapwrap">
        <canvas id="cv"></canvas>
        <div id="legend"><div class="hd"><span id="lgtitle">Modules</span><button id="lgx" title="Collapse / expand">&#8722;</button></div><div id="armkey"></div><div id="lgbody"></div></div>
        <div id="tip" class="tip"></div>
        <div id="status" class="status"></div>
      </div>
    </div>
    <div class="pane" id="pane-nbr" role="tabpanel"></div>
    <div class="pane" id="pane-mod" role="tabpanel"></div>
    <div class="pane" id="pane-all" role="tabpanel"></div>
    <div class="pane" id="pane-help" role="tabpanel"><div class="helpwrap"><div id="helptext" class="howto"></div></div></div>
  </section>
  <aside id="panel"></aside>
</main>
<noscript><p style="padding:20px">This map needs JavaScript.</p></noscript>
<script id="tm-data" type="application/json">__DATA__</script>
<script>
"use strict";
(function () {
const D = JSON.parse(document.getElementById("tm-data").textContent);
const N = D.n, NA = D.sym.length, PAL = D.palette, GREY = "#bdbcb6";
const ARMC = {"+": "#eb6834", "-": "#2a78d6"};
const WITH = "#0ca30c", OPP = "#d03b3b", SURF = "#fcfcfb", INK = "#0b0b0b", INK2 = "#52514e";
const WITH_T = "#05600a", OPP_T = "#8f1d1d";
const EVS = ["none", "one", "both"];
const FF = "system-ui,-apple-system,sans-serif";
const $ = id => document.getElementById(id);
const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
const has = a => a && a.length > 0;
const MODS = new Map(D.mods.map(m => [m.id, m]));
const modColour = m => m > 0 ? PAL[(m - 1) % PAL.length] : GREY;
const isMap = t => t === "nodal" || t === "signed";

// ---------------------------------------------------------------- shared by every tab: the selection and the highlighted module
let sel = -1, hlMod = -1, P = [], pset = new Set(), focus = "gene", active = "nodal", mapSelPending = false, selGen = 0;
const PHYS = {};                                   // the three physics tabs, by key
function partnersOf(i) {
  const a = (i >= 0 && i < N) ? (D.rel[i] || []) : [], out = [];
  for (let t = 0; t + 3 < a.length; t += 4) {
    const f = a[t + 3];
    out.push({j: a[t], cos: a[t + 1] / 100, fdr: a[t + 2] < 0 ? null : a[t + 2] / 100, ev: f & 3,
      locus: !!(f & 4), rt: !!(f & 8), group: !!(f & 16), known: !!(f & 32), novel: !!(f & 64),
      string: (Math.floor(f / 256) % 128) * 10, pw: Math.floor(f / 32768) - 1});
  }
  return out;
}

// ---------------------------------------------------------------- one frame loop, for the visible tab only
let pendingFrame = false;
function req() { if (!pendingFrame) { pendingFrame = true; requestAnimationFrame(loop); } }
function loop(now) {
  pendingFrame = false;
  let more = false;
  if (isMap(active)) more = mapFrame(now);
  else if (PHYS[active]) more = PHYS[active].frame(now);
  if (more) req();
}

// ---------------------------------------------------------------- drawing helpers
// Points are written straight into one pixel buffer (a single putImageData per frame): no canvas call per point,
// so 16k+ points stay fast also where the canvas is not GPU-accelerated. Lines, rings and labels go on top.
const LITTLE = new Uint8Array(new Uint32Array([1]).buffer)[0] === 1;
const pack = (r, g, b) => LITTLE ? (((255 << 24) | (b << 16) | (g << 8) | r) >>> 0) : (((r << 24) | (g << 16) | (b << 8) | 255) >>> 0);
const rgbOf = hex => { const v = parseInt(hex.slice(1), 16); return [(v >> 16) & 255, (v >> 8) & 255, v & 255]; };
const SURF_RGB = rgbOf(SURF), SURF_PACKED = pack(SURF_RGB[0], SURF_RGB[1], SURF_RGB[2]);
function PointLayer(cv, ctx) {
  let img = null, buf8 = null, buf32 = null, mask = null;
  function getMask(R, Wd) {
    if (mask && mask.R === R && mask.Wd === Wd) return mask;
    const e = Math.ceil(R + 0.5), m = {R: R, Wd: Wd, e: e, full: [], fdx: [], fdy: [], part: [], cov: [], pdx: [], pdy: []};
    for (let dy = -e; dy <= e; dy++) for (let dx = -e; dx <= e; dx++) {
      const c = Math.max(0, Math.min(1, R + 0.5 - Math.hypot(dx, dy)));
      if (c >= 0.98) { m.full.push(dy * Wd + dx); m.fdx.push(dx); m.fdy.push(dy); }
      else if (c > 0.04) { m.part.push(dy * Wd + dx); m.cov.push(c); m.pdx.push(dx); m.pdy.push(dy); }
    }
    for (const key of ["full", "fdx", "fdy", "part", "pdx", "pdy"]) m[key] = Int32Array.from(m[key]);
    m.cov = Float32Array.from(m.cov);
    return (mask = m);
  }
  // XA, YA: world coordinates; screen = (XA * k + tx, ys * YA * k + ty) in CSS pixels; groups: [{c, a, idx}]
  return function (XA, YA, ys, groups, kk, txx, tyy, dpr, R) {
    const Wd = cv.width, Hd = cv.height;
    if (!img || img.width !== Wd || img.height !== Hd) { img = ctx.createImageData(Wd, Hd); buf8 = img.data; buf32 = new Uint32Array(buf8.buffer); }
    buf32.fill(SURF_PACKED);
    if (groups) {
      const k = kk * dpr, ky = ys * k, tx = txx * dpr, ty = tyy * dpr, M = getMask(R * dpr, Wd), e = M.e;
      const full = M.full, part = M.part, cov = M.cov, fdx = M.fdx, fdy = M.fdy, pdx = M.pdx, pdy = M.pdy;
      const nf = full.length, np = part.length;
      for (const g of groups) {
        const a = g.a * 0.92, rgb = rgbOf(g.c);
        const cr = rgb[0] * a + SURF_RGB[0] * (1 - a), cg = rgb[1] * a + SURF_RGB[1] * (1 - a), cb = rgb[2] * a + SURF_RGB[2] * (1 - a);
        const solid = pack(Math.round(cr), Math.round(cg), Math.round(cb)), idx = g.idx;
        for (let j = 0; j < idx.length; j++) {
          const i = idx[j], X = Math.round(XA[i] * k + tx), Y = Math.round(YA[i] * ky + ty);
          if (X < -e || Y < -e || X >= Wd + e || Y >= Hd + e) continue;
          if (X >= e && Y >= e && X < Wd - e && Y < Hd - e) {
            const base = Y * Wd + X;
            for (let t = 0; t < nf; t++) buf32[base + full[t]] = solid;
            for (let t = 0; t < np; t++) {
              const o = (base + part[t]) << 2, c = cov[t];
              buf8[o] += (cr - buf8[o]) * c; buf8[o + 1] += (cg - buf8[o + 1]) * c; buf8[o + 2] += (cb - buf8[o + 2]) * c;
            }
          } else {                                            // near the edge: clip pixel by pixel
            for (let t = 0; t < nf; t++) {
              const x = X + fdx[t], y = Y + fdy[t];
              if (x >= 0 && y >= 0 && x < Wd && y < Hd) buf32[y * Wd + x] = solid;
            }
            for (let t = 0; t < np; t++) {
              const x = X + pdx[t], y = Y + pdy[t];
              if (x < 0 || y < 0 || x >= Wd || y >= Hd) continue;
              const o = (y * Wd + x) << 2, c = cov[t];
              buf8[o] += (cr - buf8[o]) * c; buf8[o + 1] += (cg - buf8[o + 1]) * c; buf8[o + 2] += (cb - buf8[o + 2]) * c;
            }
          }
        }
      }
    }
    ctx.putImageData(img, 0, 0);
  };
}
function halo(ctx, text, x, y, font, colour) {
  ctx.font = font; ctx.lineJoin = "round"; ctx.lineWidth = 3.5; ctx.strokeStyle = "rgba(252,252,251,.92)";
  ctx.strokeText(text, x, y); ctx.fillStyle = colour || INK; ctx.fillText(text, x, y);
}
// labels that would overlap one already drawn are skipped
function Labeler(ctx) {
  const placed = [];
  return function (text, x, y, font, colour, hgt) {
    ctx.font = font;
    const w = ctx.measureText(text).width, b = [x - 1, y - hgt / 2, x + w + 1, y + hgt / 2];
    for (const q of placed) if (b[0] < q[2] && b[2] > q[0] && b[1] < q[3] && b[3] > q[1]) return false;
    placed.push(b); halo(ctx, text, x, y, font, colour);
    return true;
  };
}
function quant(sorted, q) { return sorted[Math.min(sorted.length - 1, Math.max(0, Math.round(q * (sorted.length - 1))))]; }

// ================================================================ tabs 1-2: the two t-SNE maps (one canvas, two layouts)
function norm(xa, ya) {
  const n = xa.length, X = new Float32Array(n), Y = new Float32Array(n);
  if (!n) return {x: X, y: Y};
  const sx = Float64Array.from(xa).sort(), sy = Float64Array.from(ya).sort();
  const x0 = quant(sx, .005), x1 = quant(sx, .995), y0 = quant(sy, .005), y1 = quant(sy, .995);
  const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, s = Math.max(x1 - x0, y1 - y0, 1e-9) / 2;
  for (let i = 0; i < n; i++) { X[i] = (xa[i] - cx) / s; Y[i] = (ya[i] - cy) / s; }
  return {x: X, y: Y};
}
const LAY = [norm(D.x, D.y), norm(D.xs, D.ys)];
const PX = new Float32Array(N), PY = new Float32Array(N);
PX.set(LAY[0].x); PY.set(LAY[0].y);
let layout = 0, anim = null;
const cv = $("cv"), ctx = cv.getContext("2d"), wrap = $("mapwrap"), tip = $("tip"), mapLayer = PointLayer(cv, ctx);

// view (screen = world * k + t; y up)
let W = 1, H = 1, DPR = 1, K0 = 1, mapSized = false;
const V = {k: 1, tx: 0, ty: 0}, T = {k: 1, tx: 0, ty: 0};
const legendW = () => $("legend").classList.contains("closed") ? 0 : 290;
function fitTarget() {
  const lw = W > 700 ? legendW() : 0, w = W - lw;
  K0 = Math.max(10, Math.min(w, H) / 2 * 0.9);
  return {k: K0, tx: lw + w / 2, ty: H / 2};
}
function fit(now) { Object.assign(T, fitTarget()); if (now) Object.assign(V, T); req(); }
function resize() {
  const r = wrap.getBoundingClientRect();
  if (r.width < 2 || r.height < 2) return;                 // the map tab is hidden
  DPR = window.devicePixelRatio || 1;
  W = r.width; H = r.height;
  cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
  if (!mapSized) {
    mapSized = true; fit(true);
    if (sel >= 0 && sel < N) { centreOn(sel, layout); Object.assign(V, T); mapSelPending = false; }
  } else { const f = fitTarget(); K0 = f.k; }
  req();
}
const sx = i => PX[i] * V.k + V.tx, sy = i => -PY[i] * V.k + V.ty;

let colourMode = 0, hover = -1, groups = null;
function colourOf(i) {
  if (colourMode === 1) return ARMC[D.arm[i]] || GREY;
  return modColour(D.mod[i]);
}
function regroup() {
  const g = new Map();
  const selOn = sel >= 0 && sel < N;
  for (let i = 0; i < N; i++) {
    let a = 1;
    if (hlMod >= 0 && D.mod[i] !== hlMod) a = 0.13;
    if (selOn && i !== sel && !pset.has(i)) a = Math.min(a, 0.4);
    const c = colourOf(i), key = a + c;
    let e = g.get(key);
    if (!e) { e = {c: c, a: a, idx: []}; g.set(key, e); }
    e.idx.push(i);
  }
  groups = [...g.values()].sort((p, q) => (p.a - q.a) || ((q.c === GREY) - (p.c === GREY)));
  for (const e of groups) e.idx = Int32Array.from(e.idx);
  req();
}
const pointR = () => Math.min(5, Math.round(4 * 2 * Math.pow(V.k / K0, 0.3)) / 4);
function ease(t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
function mapFrame(now) {
  if (!mapSized) resize();
  let more = false;
  if (anim) {
    const t = Math.min(1, (now - anim.t0) / anim.dur), e = ease(t), A = LAY[anim.from], B = LAY[anim.to];
    for (let i = 0; i < N; i++) { PX[i] = A.x[i] + (B.x[i] - A.x[i]) * e; PY[i] = A.y[i] + (B.y[i] - A.y[i]) * e; }
    if (t >= 1) anim = null; else more = true;
  }
  for (const key of ["k", "tx", "ty"]) {
    const d = T[key] - V[key];
    if (Math.abs(d) > (key === "k" ? V.k * 1e-3 : 0.3)) { V[key] += d * 0.28; more = true; } else V[key] = T[key];
  }
  mapDraw();
  return more;
}
function mapDraw() {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  mapLayer(PX, PY, -1, groups, V.k, V.tx, V.ty, DPR, pointR());
  const r = pointR();
  ctx.globalAlpha = 1;
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  drawModuleLabels();
  if (sel >= 0 && sel < N) drawSelection(r);
  if (hover >= 0 && hover !== sel) {
    ctx.beginPath(); ctx.arc(sx(hover), sy(hover), r + 3, 0, 2 * Math.PI);
    ctx.lineWidth = 1.5; ctx.strokeStyle = INK; ctx.stroke();
  }
}
const nModLabels = 40;
function drawModuleLabels() {
  if (!D.mods.length) return;
  const sum = new Map();
  for (let i = 0; i < N; i++) {
    const m = D.mod[i];
    if (m <= 0) continue;
    let s = sum.get(m);
    if (!s) { s = [0, 0, 0]; sum.set(m, s); }
    s[0] += PX[i]; s[1] += PY[i]; s[2]++;
  }
  ctx.textAlign = "center"; ctx.textBaseline = "middle";
  const zoomed = V.k / K0 > 2.2, selOn = sel >= 0 && sel < N;
  for (const m of D.mods) {
    const s = sum.get(m.id);
    if (!s) continue;
    if (hlMod >= 0 && m.id !== hlMod) continue;
    if (hlMod < 0 && !zoomed && m.id > nModLabels) continue;
    const X = s[0] / s[2] * V.k + V.tx, Y = -s[1] / s[2] * V.k + V.ty;
    if (X < 0 || Y < 0 || X > W || Y > H) continue;
    // the full label only for the highlighted module; otherwise the module number (muted while a gene is selected)
    let text = hlMod === m.id ? "M" + m.id + " " + m.label : "M" + m.id;
    if (text.length > 60) text = text.slice(0, 58) + "…";
    halo(ctx, text, X, Y, "600 11px " + FF, selOn && hlMod !== m.id ? "#898781" : "#2b2b2a");
  }
}
function drawSelection(r) {
  const x0 = sx(sel), y0 = sy(sel);
  for (const p of P) {
    const a = Math.abs(p.cos);
    ctx.strokeStyle = p.cos > 0 ? WITH : OPP; ctx.globalAlpha = 0.35 + 0.6 * a; ctx.lineWidth = 0.8 + 2.4 * a;
    ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(sx(p.j), sy(p.j)); ctx.stroke();
  }
  ctx.globalAlpha = 1;
  for (const p of P) {
    ctx.beginPath(); ctx.arc(sx(p.j), sy(p.j), r + 1.5, 0, 2 * Math.PI);
    ctx.fillStyle = colourOf(p.j); ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = p.cos > 0 ? WITH : OPP; ctx.stroke();
  }
  ctx.beginPath(); ctx.arc(x0, y0, r + 4, 0, 2 * Math.PI);
  ctx.fillStyle = colourOf(sel); ctx.fill(); ctx.lineWidth = 2.5; ctx.strokeStyle = INK; ctx.stroke();
  // labels: the selected gene first, then partners by |cos|, skipping any that would overlap one already drawn
  ctx.textAlign = "left"; ctx.textBaseline = "middle";
  const label = Labeler(ctx);
  label(D.sym[sel], x0 + r + 7, y0, "700 13px " + FF, INK, 15);
  for (const p of P) label(D.sym[p.j], sx(p.j) + r + 4, sy(p.j), "11px " + FF, p.cos > 0 ? WITH_T : OPP_T, 12);
}

// hit testing, pointer, wheel
function nearest(mx, my) {
  const r = Math.max(6, pointR() + 3), r2 = r * r;
  let best = -1, bd = r2;
  const k = V.k, tx = V.tx, ty = V.ty, dim = hlMod >= 0;
  for (let i = 0; i < N; i++) {
    const dx = PX[i] * k + tx - mx, dy = -PY[i] * k + ty - my, d = dx * dx + dy * dy;
    if (d < bd || (d === bd && dim && D.mod[i] === hlMod)) { bd = d; best = i; }
  }
  return best;
}
const ptrs = new Map();
let dragged = false, pinch = null, downAt = null;
function local(e, el) { const r = el.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
cv.addEventListener("pointerdown", e => {
  cv.setPointerCapture(e.pointerId);
  ptrs.set(e.pointerId, local(e, cv));
  dragged = false; downAt = local(e, cv);
  if (ptrs.size === 2) { const [a, b] = [...ptrs.values()]; pinch = {d: Math.hypot(a[0] - b[0], a[1] - b[1]), k: T.k}; }
  cv.classList.add("drag");
});
cv.addEventListener("pointermove", e => {
  const p = local(e, cv);
  if (ptrs.has(e.pointerId)) {
    const q = ptrs.get(e.pointerId);
    ptrs.set(e.pointerId, p);
    if (ptrs.size === 2 && pinch) {
      const [a, b] = [...ptrs.values()], d = Math.hypot(a[0] - b[0], a[1] - b[1]), mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
      zoomAt(mx, my, (pinch.k * d / Math.max(pinch.d, 1)) / T.k, true);
      dragged = true;
      return;
    }
    const dx = p[0] - q[0], dy = p[1] - q[1];
    if (Math.abs(p[0] - downAt[0]) + Math.abs(p[1] - downAt[1]) > 3) dragged = true;
    V.tx += dx; V.ty += dy; T.tx += dx; T.ty += dy;
    hideTip(); req();
    return;
  }
  const h = nearest(p[0], p[1]);
  if (h !== hover) { hover = h; req(); }
  if (h >= 0) showTip(h, p[0], p[1]); else hideTip();
});
function endPtr(e) {
  ptrs.delete(e.pointerId);
  if (ptrs.size < 2) pinch = null;
  if (ptrs.size === 0) cv.classList.remove("drag");
}
cv.addEventListener("pointerup", e => {
  const p = local(e, cv), wasDrag = dragged;
  endPtr(e);
  if (!wasDrag && e.button === 0) { const h = nearest(p[0], p[1]); if (h >= 0) select(h, false, "map"); else if (sel >= 0) select(-1, false, "map"); }
});
cv.addEventListener("pointercancel", endPtr);
cv.addEventListener("pointerleave", () => { if (hover >= 0) { hover = -1; req(); } hideTip(); });
function zoomAt(mx, my, f, immediate) {
  const k = Math.min(K0 * 400, Math.max(K0 * 0.3, T.k * f)), g = k / T.k;
  T.tx = mx - (mx - T.tx) * g; T.ty = my - (my - T.ty) * g; T.k = k;
  if (immediate) Object.assign(V, T);
  req();
}
cv.addEventListener("wheel", e => {
  e.preventDefault();
  const [mx, my] = local(e, cv), dy = e.deltaMode === 1 ? e.deltaY * 33 : e.deltaY;
  zoomAt(mx, my, Math.exp(-dy * 0.0016), false);
  hideTip();
}, {passive: false});
cv.addEventListener("dblclick", e => { const [mx, my] = local(e, cv); zoomAt(mx, my, 2, false); });

function tipHtml(i) {
  const m = D.mod[i], arm = D.arm[i], mod = MODS.get(m);
  let h = "<b>" + esc(D.sym[i]) + "</b>";
  if (has(D.name) && D.name[i]) h += " <span class='m'>" + esc(D.name[i]) + "</span>";
  h += "<br><span class='k' style='background:" + modColour(m) + "'></span>" +
       (m > 0 ? "Module " + m + (arm !== "." && mod && mod.opp ? ", arm " + (arm === "-" ? "&minus;" : "+") : "") + (mod ? " <span class='m'>" + esc(mod.label) + "</span>" : "") : "<span class='m'>no module</span>");
  return h;
}
function placeTip(el, html, mx, my, Wd, Hd) {
  el.innerHTML = html; el.style.display = "block";
  const tw = el.offsetWidth, th = el.offsetHeight;
  let x = mx + 14, y = my + 14;
  if (x + tw > Wd - 4) x = mx - tw - 12;
  if (y + th > Hd - 4) y = my - th - 12;
  el.style.left = Math.max(2, x) + "px"; el.style.top = Math.max(2, y) + "px";
}
function showTip(i, mx, my) { placeTip(tip, tipHtml(i), mx, my, W, H); }
function hideTip() { tip.style.display = "none"; }

// views, colours, legend
function setLayout(l) {
  if (l === layout && !anim) return;
  anim = {from: layout, to: l, t0: performance.now(), dur: 750};
  // start from the current (possibly mid-animation) positions
  LAY[2] = {x: Float32Array.from(PX), y: Float32Array.from(PY)}; anim.from = 2;
  layout = l;
  if (sel >= 0 && sel < N) { centreOn(sel, l); mapSelPending = false; }   // follow the selected gene to the new layout
  status(); req();
}
function setColour(c) {
  colourMode = c;
  $("c0").setAttribute("aria-pressed", c === 0); $("c1").setAttribute("aria-pressed", c === 1);
  $("armkey").style.display = c === 1 ? "block" : "none";
  regroup();
}
function buildLegend() {
  const body = $("lgbody"), counts = new Map();
  let nArm = {"+": 0, "-": 0, ".": 0};
  for (let i = 0; i < N; i++) { counts.set(D.mod[i], (counts.get(D.mod[i]) || 0) + 1); nArm[D.arm[i]] = (nArm[D.arm[i]] || 0) + 1; }
  $("armkey").innerHTML =
    "<div><span class='sw' style='background:" + ARMC["+"] + "'></span> + arm (" + nArm["+"].toLocaleString() + ")" +
    " &nbsp; <span class='sw' style='background:" + ARMC["-"] + "'></span> &minus; arm (" + nArm["-"].toLocaleString() + ")" +
    (nArm["."] ? " &nbsp; <span class='sw' style='background:" + GREY + "'></span> none" : "") + "</div>" +
    "<div class='note' style='margin-top:3px'>A module has a &minus; arm only where its two sides move in opposite directions under the same drugs (mean cos between them &le; &minus;0.2); otherwise all its genes are +.</div>";
  let h = "";
  for (const m of D.mods) {
    h += "<div class='li' data-m='" + m.id + "' title='" + esc("M" + m.id + ": " + m.label + " (" + m.n + " genes)") + "'>" +
      "<span class='sw' style='background:" + modColour(m.id) + "'></span><span class='t'><b>M" + m.id + "</b> " + esc(m.label) +
      "</span><span class='n'>" + (counts.get(m.id) || m.n) + "</span></div>";
  }
  if (counts.get(0)) h += "<div class='li' data-m='0'><span class='sw' style='background:" + GREY + "'></span><span class='t'>no module</span><span class='n'>" + counts.get(0) + "</span></div>";
  if (!h) h = "<div class='note' style='padding:4px 8px'>No modules.</div>";
  body.innerHTML = h;
  $("lgtitle").innerHTML = "Modules (" + D.mods.length + ")" + (D.labels_from === "validation" ? "" : " <span class='note' style='font-weight:400'>labels: top genes</span>");
  body.addEventListener("click", e => {
    const li = e.target.closest(".li");
    if (li) highlight(+li.dataset.m === hlMod ? -1 : +li.dataset.m);
  });
}
function highlight(m) {
  hlMod = m; focus = "module";
  for (const li of document.querySelectorAll("#lgbody .li")) li.classList.toggle("on", +li.dataset.m === m);
  if (m >= 0) { const li = document.querySelector("#lgbody .li[data-m='" + m + "']"); if (li) li.scrollIntoView({block: "nearest"}); }
  regroup(); renderPanel(); status();
  for (const k in PHYS) PHYS[k].onHighlight(m);
}
function centreOn(i, l) {
  // zoom so that the gene and its partners fill the free part of the canvas, centred on the gene
  const lw = W > 700 ? legendW() : 0, w = W - lw, X = LAY[l].x, Y = LAY[l].y;
  let far = 0;
  for (const p of P) far = Math.max(far, Math.abs(X[p.j] - X[i]), Math.abs(Y[p.j] - Y[i]));
  const k = far > 0 ? Math.min(K0 * 40, Math.max(K0 * 1.2, 0.42 * Math.min(w, H) / far)) : Math.max(T.k, K0 * 4);
  T.k = k; T.tx = lw + w / 2 - X[i] * k; T.ty = H / 2 + Y[i] * k;
}

// ================================================================ tabs 3-5: one force simulation, three views of it
function mulberry(seed) {
  let a = seed >>> 0;
  return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}
// graph/edges.parquet (the kNN graph that defines the modules): index pairs, cos x100, evidence; decoded on first use
let EG = null;
function b64bytes(s) { const t = atob(s || ""), u = new Uint8Array(t.length); for (let i = 0; i < t.length; i++) u[i] = t.charCodeAt(i); return u; }
function graphEdges() {
  if (EG) return EG;
  const e = D.edges || {}, w = e.bytes || 2;
  let m = e.m || 0;
  const A = new Int32Array(m), B = new Int32Array(m), C = new Float32Array(m), EV = new Uint8Array(m);
  if (m) {
    const ua = b64bytes(e.a), ub = b64bytes(e.b), uc = b64bytes(e.cos), ue = b64bytes(e.ev);
    let k2 = 0;
    for (let k = 0; k < m; k++) {
      let a = 0, b = 0;
      for (let t = w - 1; t >= 0; t--) { a = a * 256 + ua[k * w + t]; b = b * 256 + ub[k * w + t]; }
      if (a >= N || b >= N || a === b) continue;
      const c = uc[k];
      A[k2] = a; B[k2] = b; C[k2] = (c > 127 ? c - 256 : c) / 100; EV[k2] = ue.length > k ? ue[k] : 2; k2++;
    }
    m = k2;
  }
  const off = new Int32Array(N + 1);
  for (let k = 0; k < m; k++) { off[A[k] + 1]++; off[B[k] + 1]++; }
  for (let i = 0; i < N; i++) off[i + 1] += off[i];
  const adj = new Int32Array(2 * m), fill = off.slice(0, N);
  for (let k = 0; k < m; k++) { adj[fill[A[k]]++] = k; adj[fill[B[k]]++] = k; }
  return (EG = {m: m, A: A, B: B, C: C, EV: EV, off: off, adj: adj});
}

// The engine. Velocity Verlet with friction, as d3-force: every force adds to the velocities, scaled by alpha; alpha
// cools toward alphaTarget (0 unless a gene is dragged); positions move by the damped velocities.
//   springs     every edge: (d - L) / d * spr * |cos| / min(degree) (shared by the two ends by degree), rest length
//               L = s0 * (1.6 - |cos|): stronger relations are shorter springs. With oppRepel, an edge with cos < 0
//               only pushes: rest length s0 * pushLen, and no pull beyond it.
//   repulsion   every pair: -rep / d (2D Coulomb), Barnes-Hut quadtree with theta 0.8 (a cell of width w at distance
//               d counts as one body when w / d < theta)
//   centre      -centre * position: a weak pull that keeps the layout together
function makeSim() {
  const S = {n: 0, m: 0, alpha: 0, alphaMin: 0.002, alphaTarget: 0, alphaDecay: 1 - Math.pow(0.002, 1 / 300),
    vDecay: 0.4, rep: 30, spr: 1, centre: 0.03, theta2: 0.64, oppRepel: false, s0: 30, pushLen: 6, dmin2: 4, ticks: 0};
  let cap = 0, cnt = 0, qx0, qy0, qw, qcx, qcy, qm, qkid, qpt, qint, nxt;
  const stack = new Int32Array(4 * 64 + 8), MAXD = 52;
  let seed = 7;
  const jiggle = () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return (seed / 0x7fffffff - 0.5) * 1e-3; };
  function grow(c) {                                     // only while the tree is built: centres of mass come after
    const o = cnt;
    const nx0 = new Float64Array(c), ny0 = new Float64Array(c), nw = new Float64Array(c), ncx = new Float64Array(c), ncy = new Float64Array(c);
    const nm = new Float64Array(c), nkid = new Int32Array(4 * c), npt = new Int32Array(c), nint = new Uint8Array(c);
    if (qx0) { nx0.set(qx0.subarray(0, o)); ny0.set(qy0.subarray(0, o)); nw.set(qw.subarray(0, o)); nkid.set(qkid.subarray(0, 4 * o)); npt.set(qpt.subarray(0, o)); nint.set(qint.subarray(0, o)); }
    qx0 = nx0; qy0 = ny0; qw = nw; qcx = ncx; qcy = ncy; qm = nm; qkid = nkid; qpt = npt; qint = nint; cap = c;
  }
  function cell(x0, y0, w) {
    if (cnt >= cap) grow(Math.max(64, cap * 2));
    const c = cnt++;
    qx0[c] = x0; qy0[c] = y0; qw[c] = w; qkid[4 * c] = qkid[4 * c + 1] = qkid[4 * c + 2] = qkid[4 * c + 3] = -1;
    qpt[c] = -1; qint[c] = 0;
    return c;
  }
  function insert(i) {
    const x = S.x, y = S.y, px = x[i], py = y[i];
    let c = 0, depth = 0;
    for (;;) {
      if (qint[c]) {
        const h = qw[c] / 2, q = (px >= qx0[c] + h ? 1 : 0) + (py >= qy0[c] + h ? 2 : 0);
        let k = qkid[4 * c + q];
        if (k < 0) { k = cell(qx0[c] + (q & 1) * h, qy0[c] + (q >> 1) * h, h); qkid[4 * c + q] = k; qpt[k] = i; nxt[i] = -1; return; }
        c = k; depth++;
        continue;
      }
      const j = qpt[c];
      if (j < 0) { qpt[c] = i; nxt[i] = -1; return; }
      if (depth >= MAXD || (x[j] === px && y[j] === py)) { nxt[i] = j; qpt[c] = i; return; }
      // split the leaf: its point (and any coincident ones chained to it) moves down one level
      qint[c] = 1; qpt[c] = -1;
      const h = qw[c] / 2, q = (x[j] >= qx0[c] + h ? 1 : 0) + (y[j] >= qy0[c] + h ? 2 : 0);
      const k = cell(qx0[c] + (q & 1) * h, qy0[c] + (q >> 1) * h, h);
      qkid[4 * c + q] = k; qpt[k] = j;
    }
  }
  function buildTree() {
    const n = S.n, x = S.x, y = S.y;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (let i = 0; i < n; i++) { const a = x[i], b = y[i]; if (a < x0) x0 = a; if (a > x1) x1 = a; if (b < y0) y0 = b; if (b > y1) y1 = b; }
    let w = Math.max(x1 - x0, y1 - y0);
    if (!(w > 0)) w = 1;
    w = w * 1.0001 + 1e-6;
    cnt = 0; cell(x0, y0, w);
    for (let i = 0; i < n; i++) insert(i);
    // centres of mass, children before parents (a child always has a higher index than its parent)
    for (let c = cnt - 1; c >= 0; c--) {
      let m = 0, sx = 0, sy = 0;
      if (qint[c]) {
        for (let q = 0; q < 4; q++) { const k = qkid[4 * c + q]; if (k >= 0 && qm[k] > 0) { m += qm[k]; sx += qcx[k] * qm[k]; sy += qcy[k] * qm[k]; } }
      } else for (let j = qpt[c]; j >= 0; j = nxt[j]) { m++; sx += x[j]; sy += y[j]; }
      qm[c] = m; qcx[c] = m ? sx / m : 0; qcy[c] = m ? sy / m : 0;
    }
  }
  let ordBuf = null;
  function treeOrder() {                                 // the genes leaf by leaf, depth first: neighbours in space are neighbours in memory
    if (!ordBuf || ordBuf.length !== S.n) ordBuf = new Int32Array(S.n);
    let k = 0, sp = 0;
    stack[sp++] = 0;
    while (sp > 0) {
      const c = stack[--sp];
      if (!qint[c]) { for (let j = qpt[c]; j >= 0; j = nxt[j]) ordBuf[k++] = j; continue; }
      for (let q = 3; q >= 0; q--) { const kk = qkid[4 * c + q]; if (kk >= 0) stack[sp++] = kk; }
    }
    return ordBuf;
  }
  function repulse(alpha) {
    buildTree();
    const n = S.n, x = S.x, y = S.y, vx = S.vx, vy = S.vy, str = -S.rep * alpha, th2 = S.theta2, dmin2 = S.dmin2;
    const QM = qm, QI = qint, QP = qpt, QK = qkid, QX = qcx, QY = qcy, QW = qw, NX = nxt, st = stack;
    const ord = treeOrder();
    for (let oi = 0; oi < n; oi++) {
      const i = ord[oi], xi = x[i], yi = y[i];
      let ax = 0, ay = 0, sp = 0;
      st[sp++] = 0;
      while (sp > 0) {
        const c = st[--sp], m = QM[c];
        if (!m) continue;
        if (!QI[c]) {                                    // a leaf: every gene in it, one by one
          for (let j = QP[c]; j >= 0; j = NX[j]) {
            if (j === i) continue;
            let dx = x[j] - xi, dy = y[j] - yi, l = dx * dx + dy * dy;
            if (l === 0) { dx = jiggle(); dy = jiggle(); l = dx * dx + dy * dy; }
            if (l < dmin2) l = Math.sqrt(dmin2 * l);
            ax += dx * str / l; ay += dy * str / l;
          }
          continue;
        }
        const dx = QX[c] - xi, dy = QY[c] - yi, w = QW[c];
        let l = dx * dx + dy * dy;
        if (w * w < th2 * l) {                           // far enough: the whole cell as one body at its centre of mass
          if (l < dmin2) l = Math.sqrt(dmin2 * l);
          const f = str * m / l;
          ax += dx * f; ay += dy * f;
          continue;
        }
        const b = 4 * c;
        for (let q = 0; q < 4; q++) { const k = QK[b + q]; if (k >= 0) st[sp++] = k; }
      }
      vx[i] += ax; vy[i] += ay;
    }
  }
  S.load = function (n, px, py, ea, eb, ec) {
    S.n = n; S.x = Float32Array.from(px); S.y = Float32Array.from(py);
    S.vx = new Float32Array(n); S.vy = new Float32Array(n); S.fx = new Float32Array(n); S.fy = new Float32Array(n);
    S.fixed = new Uint8Array(n);                         // 1 pinned by the user, 2 being dragged, 4 the centre gene (pinned at the start)
    const m = ea.length;
    S.m = m; S.ea = Int32Array.from(ea); S.eb = Int32Array.from(eb); S.ec = Float32Array.from(ec);
    const deg = new Float32Array(n);
    for (let k = 0; k < m; k++) { deg[S.ea[k]]++; deg[S.eb[k]]++; }
    S.deg = deg;
    S.estr = new Float32Array(m); S.ebias = new Float32Array(m); S.elen = new Float32Array(m);
    for (let k = 0; k < m; k++) {
      const a = S.ea[k], b = S.eb[k], w = Math.abs(S.ec[k]);
      S.estr[k] = w / Math.max(1, Math.min(deg[a], deg[b]));
      S.ebias[k] = deg[a] / (deg[a] + deg[b]);
      S.elen[k] = S.s0 * (1.6 - w);
    }
    // incident edges per node (CSR)
    const off = new Int32Array(n + 1);
    for (let k = 0; k < m; k++) { off[S.ea[k] + 1]++; off[S.eb[k] + 1]++; }
    for (let i = 0; i < n; i++) off[i + 1] += off[i];
    const adj = new Int32Array(2 * m), fill = off.slice(0, n);
    for (let k = 0; k < m; k++) { adj[fill[S.ea[k]]++] = k; adj[fill[S.eb[k]]++] = k; }
    S.off = off; S.adj = adj;
    nxt = new Int32Array(Math.max(1, n));
    if (cap < 2 * n + 16) { cnt = 0; grow(2 * n + 16); }
  };
  S.tick = function () {
    const n = S.n;
    if (!n) return;
    S.alpha += (S.alphaTarget - S.alpha) * S.alphaDecay;
    const alpha = S.alpha, x = S.x, y = S.y, vx = S.vx, vy = S.vy;
    // springs
    const ea = S.ea, eb = S.eb, ec = S.ec, estr = S.estr, ebias = S.ebias, elen = S.elen, ks = S.spr * alpha;
    const rep = S.oppRepel, push = S.s0 * S.pushLen;
    if (ks > 0) for (let k = 0, m = S.m; k < m; k++) {
      const a = ea[k], b = eb[k];
      let dx = x[b] + vx[b] - x[a] - vx[a], dy = y[b] + vy[b] - y[a] - vy[a], l = Math.sqrt(dx * dx + dy * dy);
      if (l < 1e-9) { dx = jiggle(); dy = jiggle(); l = Math.sqrt(dx * dx + dy * dy); }
      let L = elen[k];
      if (rep && ec[k] < 0) { if (l >= push) continue; L = push; }
      const f = (l - L) / l * ks * estr[k], bb = ebias[k];
      dx *= f; dy *= f;
      vx[b] -= dx * bb; vy[b] -= dy * bb;
      vx[a] += dx * (1 - bb); vy[a] += dy * (1 - bb);
    }
    // repulsion between every pair, and the pull to the centre
    if (S.rep > 0 && n > 1) repulse(alpha);
    const c = S.centre * alpha;
    for (let i = 0; i < n; i++) { vx[i] -= x[i] * c; vy[i] -= y[i] * c; }
    // move
    const keep = 1 - S.vDecay, fixed = S.fixed, fx = S.fx, fy = S.fy;
    for (let i = 0; i < n; i++) {
      if (fixed[i]) { x[i] = fx[i]; y[i] = fy[i]; vx[i] = 0; vy[i] = 0; continue; }
      let a = vx[i] * keep, b = vy[i] * keep;
      if (!(a === a && b === b)) { a = 0; b = 0; }
      vx[i] = a; vy[i] = b; x[i] += a; y[i] += b;
    }
    S.ticks++;
  };
  S.heat = a => { S.alpha = Math.max(S.alpha, a); };
  S.moving = () => S.n > 0 && (S.alpha >= S.alphaMin || S.alphaTarget > 0);
  return S;
}

// springs among a set of genes (loc: entry -> index in the set, -1 outside), as three arrays
function relSprings(ids, loc, minCos, evMin) {               // each gene's top partners (relations, as in the side panel)
  const ea = [], eb = [], ec = [], seen = new Set(), n = ids.length;
  for (let u = 0; u < n; u++) {
    const a = D.rel[ids[u]] || [];
    for (let t = 0; t + 3 < a.length; t += 4) {
      const v = loc[a[t]];
      if (v < 0 || v === u) continue;
      const c = a[t + 1] / 100;
      if (Math.abs(c) < minCos || (a[t + 3] & 3) < evMin) continue;
      const lo = Math.min(u, v), hi = Math.max(u, v), key = lo * n + hi;
      if (seen.has(key)) continue;
      seen.add(key); ea.push(lo); eb.push(hi); ec.push(c);
    }
  }
  return {ea: ea, eb: eb, ec: ec, src: "rel"};
}
function graphSprings(ids, loc, minCos, evMin) {             // the kNN graph (graph/edges.parquet)
  const G = graphEdges();
  if (!G.m) return relSprings(ids, loc, minCos, evMin);
  const ea = [], eb = [], ec = [];
  for (let u = 0; u < ids.length; u++) {
    const i = ids[u];
    for (let p = G.off[i]; p < G.off[i + 1]; p++) {
      const k = G.adj[p];
      if (G.A[k] !== i) continue;                              // each edge once, from its first gene
      const v = loc[G.B[k]];
      if (v < 0 || Math.abs(G.C[k]) < minCos || G.EV[k] < evMin) continue;
      ea.push(u); eb.push(v); ec.push(G.C[k]);
    }
  }
  return {ea: ea, eb: eb, ec: ec, src: "graph"};
}

function physBar(kind) {
  const seg = (k, labels, on, titles) => "<span class='seg'>" + labels.map((l, t) => "<button data-k='" + k + t + "' aria-pressed='" + (t === on) + "'" +
    (titles ? " title='" + titles[t] + "'" : "") + ">" + l + "</button>").join("") + "</span>";
  const rng = (k, label, min, max, step, val, title) => "<label class='rng' title='" + title + "'>" + label + " <input type='range' data-k='" + k +
    "' min='" + min + "' max='" + max + "' step='" + step + "' value='" + val + "'><output data-k='" + k + "o'></output></label>";
  let h = "<div class='bars'><div class='bar'>";
  h += "<div class='grp'>Opposite genes " + seg("opp", ["attract", "repel"], 0, [
    "Red (opposite) relations are springs like green ones: both arms of a pathway form one cluster (the nodal view)",
    "Red (opposite) relations push their two genes apart: the minus arm separates from the plus arm (the signed view)"]) + "</div>";
  h += "<div class='grp'>Colour " + seg("col", ["Module", "Arm"], kind === "mod" ? 1 : 0) + "</div>";
  h += "<span class='seg'><button data-k='pause' aria-pressed='false' title='Pause / resume the simulation (space)'>Pause</button>" +
    "<button data-k='heat' title='Re-heat: let the layout move again'>Re-heat</button>" +
    "<button data-k='reset' title='Start the layout again and unpin every gene'>Reset</button>" +
    "<button data-k='fit' title='Fit the view to all genes'>Fit</button></span>";
  if (kind === "nbr") h += "<div class='grp' title='1: the selected gene and its partners; 2: also their partners'>Depth " + seg("dep", ["1", "2"], 1) + "</div>" +
    "<label class='grp' title='At most this many genes (the strongest partners first)'>Max genes <input type='number' data-k='max' min='10' max='3000' step='10' value='300' style='width:68px'></label>";
  h += "</div><div class='bar'>";
  h += rng("rep", "Repulsion", 0, 150, 5, 30, "Strength of the push between every pair of genes") +
    rng("spr", "Springs", 0, 300, 10, 100, "Strength of the springs, in % of the default") +
    rng("min", "Min |cos|", 0, 95, 5, 30, "Relations weaker than this are not springs");
  h += "<label class='grp' title='both halves: same sign with fdr &lt;= 0.10 in two random halves of the compounds; one half: strong in one random half only (not replicated)'>Evidence <select data-k='ev'>" +
    "<option value='1'>both or one half</option><option value='2'>both halves only</option></select></label>";
  return h + "</div></div>";
}
// the module tab's picker sits on the canvas, above the module's label and arms
const MOD_CTL = "<div class='ictl'><label>Module <select data-k='msel'></select></label>" +
  "<button class='btn' data-k='mselg' title='Show the module of the selected gene'>Selected gene's module</button>" +
  "<label title='Also show, dimmed, the genes outside the module that its genes link to'><input type='checkbox' data-k='ring'> outside genes (1 hop)</label></div>";

function PhysPane(kind) {
  const pane = $("pane-" + kind);
  pane.innerHTML = physBar(kind) + "<div class='wrap'><canvas></canvas><div class='info none'>" + (kind === "mod" ? MOD_CTL : "") +
    "<div class='itxt'></div></div><div class='msg'></div><div class='tip'></div><div class='status'></div></div>";
  const q = k => pane.querySelector("[data-k='" + k + "']");
  const wrapEl = pane.querySelector(".wrap"), cvs = pane.querySelector("canvas"), g2 = cvs.getContext("2d");
  const tipEl = pane.querySelector(".tip"), infoEl = pane.querySelector(".info"), itxt = pane.querySelector(".itxt");
  const msgEl = pane.querySelector(".msg"), statusEl = pane.querySelector(".status");
  const S = makeSim(), layer = kind === "all" ? PointLayer(cvs, g2) : null;
  const st = {colour: kind === "mod" ? 1 : 0, paused: false, dirty: true, fresh: true, autoFit: true, follow: false,
    depth: 2, maxN: 300, minCos: 0.3, ev: 1, module: -1, ring: false,
    ids: new Int32Array(0), dim: new Uint8Array(0), level: new Uint8Array(0), byDeg: new Int32Array(0), centre: -1,
    msg: "", info: "", hover: -1, drag: -1, groups: null, groupsDirty: true, avgTick: 0, tpf: 0, drawMs: 0, frames: [],
    skip: 0, centreSel: false, lastStatus: 0, src: ""};
  const loc = new Int32Array(NA).fill(-1), nloc = new Int32Array(NA).fill(-1);
  let W = 1, H = 1, DPR = 1, fitK = 1, sized = false, clickTimer = 0, dragged = false, downAt = null, pinch = null, lastFit = null;
  const V = {k: 1, tx: 0, ty: 0}, T = {k: 1, tx: 0, ty: 0}, ptrs = new Map();
  const visible = () => active === kind;
  const nodeColour = i => st.colour === 1 ? (ARMC[D.arm[i]] || GREY) : modColour(D.mod[i]);

  // ---------------------------------------------------------------- what to simulate
  function buildNbr() {
    if (sel < 0) return {msg: "Select a gene (search above, or click one on another tab) to see it with its partners and their partners."};
    if (sel >= N) return {msg: "<b>" + esc(D.sym[sel]) + "</b> is not on the map (not in the vector space), so it has no partners to simulate. Its drug-doses and cell lines are in the side panel."};
    const ids = [sel], parent = [-1], level = [0], score = [1];
    nloc[sel] = 0;
    const ok = p => Math.abs(p.cos) >= st.minCos && p.ev >= st.ev;
    for (const p of partnersOf(sel)) {
      if (ids.length >= st.maxN) break;
      if (!ok(p) || nloc[p.j] >= 0) continue;
      nloc[p.j] = ids.length; ids.push(p.j); parent.push(0); level.push(1); score.push(Math.abs(p.cos));
    }
    const n1 = ids.length;
    if (st.depth >= 2) {
      const cand = [];
      for (let u = 1; u < n1; u++) for (const p of partnersOf(ids[u])) if (ok(p) && nloc[p.j] < 0) cand.push([p.j, u, Math.abs(p.cos) * score[u]]);
      cand.sort((a, b) => b[2] - a[2]);
      for (const c of cand) {
        if (ids.length >= st.maxN) break;
        if (nloc[c[0]] >= 0) continue;
        nloc[c[0]] = ids.length; ids.push(c[0]); parent.push(c[1]); level.push(2); score.push(c[2]);
      }
    }
    const sp = relSprings(ids, nloc, st.minCos, st.ev), n2 = ids.length - n1;
    const info = "<b>" + esc(D.sym[sel]) + "</b> with " + (n1 - 1) + " partner" + (n1 === 2 ? "" : "s") +
      (st.depth >= 2 ? " and " + n2 + " of their partners" : "") + " &middot; " + sp.ea.length + " springs (top partners, |cos| &ge; " + st.minCos.toFixed(2) + ")";
    return {ids: ids, parent: parent, level: level, centre: 0, springs: sp, info: info};
  }
  function buildMod() {
    if (!D.mods.length || !N) return {msg: "This run has no modules."};
    if (!MODS.has(st.module)) st.module = (sel >= 0 && sel < N && D.mod[sel] > 0) ? D.mod[sel] : (hlMod > 0 ? hlMod : D.mods[0].id);
    const m = st.module, ids = [], parent = [], dim = [];
    syncPicker();
    for (let i = 0; i < N; i++) if (D.mod[i] === m) { nloc[i] = ids.length; ids.push(i); parent.push(-1); dim.push(0); }
    const nIn = ids.length;
    if (st.ring && nIn) {
      const G = graphEdges(), cand = [];
      for (let u = 0; u < nIn; u++) {
        const i = ids[u];
        if (G.m) {
          for (let p = G.off[i]; p < G.off[i + 1]; p++) {
            const k = G.adj[p], j = G.A[k] === i ? G.B[k] : G.A[k];
            if (D.mod[j] !== m && Math.abs(G.C[k]) >= st.minCos && G.EV[k] >= st.ev) cand.push([j, u, Math.abs(G.C[k])]);
          }
        } else for (const p of partnersOf(i)) if (p.j < N && D.mod[p.j] !== m && Math.abs(p.cos) >= st.minCos && p.ev >= st.ev) cand.push([p.j, u, Math.abs(p.cos)]);
      }
      cand.sort((a, b) => b[2] - a[2]);
      const cap = Math.max(30, 2 * nIn);
      for (const c of cand) {
        if (ids.length - nIn >= cap) break;
        if (nloc[c[0]] >= 0) continue;
        nloc[c[0]] = ids.length; ids.push(c[0]); parent.push(c[1]); dim.push(1);
      }
    }
    const sp = graphSprings(ids, nloc, st.minCos, st.ev);
    if (ids.length > nIn) {                                    // outside genes hang on the module only
      const ea = [], eb = [], ec = [];
      for (let k = 0; k < sp.ea.length; k++) if (sp.ea[k] < nIn || sp.eb[k] < nIn) { ea.push(sp.ea[k]); eb.push(sp.eb[k]); ec.push(sp.ec[k]); }
      sp.ea = ea; sp.eb = eb; sp.ec = ec;
    }
    const md = MODS.get(m);
    let info = "<b>M" + m + "</b> " + esc(md ? md.label : "") + "<br>";
    if (md) info += md.opp ? md.np + " genes in the <b style='color:" + ARMC["+"] + "'>+ arm</b>, " + md.nm + " in the <b style='color:" + ARMC["-"] + "'>&minus; arm</b>: the arms move opposite" +
      (md.cb != null ? " (mean cos between them " + (md.cb > 0 ? "+" : "") + md.cb.toFixed(2) + ")" : "") : md.n + " genes, single-armed";
    info += " &middot; " + sp.ea.length + " springs" + (ids.length > nIn ? " &middot; " + (ids.length - nIn) + " outside genes (dimmed)" : "");
    return {ids: ids, parent: parent, dim: dim, centre: -1, springs: sp, info: info};
  }
  function buildAll() {
    if (!N) return {msg: "No genes on the map."};
    const ids = new Int32Array(N);
    for (let i = 0; i < N; i++) { ids[i] = i; nloc[i] = i; }
    const sp = graphSprings(ids, nloc, st.minCos, st.ev);
    return {ids: ids, parent: null, centre: -1, springs: sp,
      info: "All <b>" + N.toLocaleString() + "</b> genes on the map &middot; " + sp.ea.length.toLocaleString() + " springs (" +
        (sp.src === "graph" ? "the kNN graph that defines the modules" : "each gene's top partners") + "); edges are drawn for the selected gene only"};
  }
  // start positions for genes that were not in the simulation before
  function place(g, px, py, keep) {
    const n = g.ids.length, rnd = mulberry(1234 + n), s0 = S.s0;
    const done = Uint8Array.from(keep);
    if (kind !== "nbr") {
      // nodal-map coordinates (y up there, down here), scaled to about the simulation's equilibrium size
      const L = LAY[0];
      let cx = 0, cy = 0, c = 0, r2 = 0;
      for (let u = 0; u < n; u++) if (!(g.dim && g.dim[u])) { cx += L.x[g.ids[u]]; cy += L.y[g.ids[u]]; c++; }
      if (c) { cx /= c; cy /= c; }
      for (let u = 0; u < n; u++) if (!(g.dim && g.dim[u])) { const dx = L.x[g.ids[u]] - cx, dy = L.y[g.ids[u]] - cy; r2 += dx * dx + dy * dy; }
      const rms = Math.sqrt(r2 / Math.max(1, c)) || 1, sc = 0.5 * Math.sqrt(Math.max(S.rep, 10) * Math.max(c, 2) / S.centre) / rms;
      for (let u = 0; u < n; u++) if (!done[u] && !(g.dim && g.dim[u])) {
        px[u] = (L.x[g.ids[u]] - cx) * sc + jit(rnd); py[u] = -(L.y[g.ids[u]] - cy) * sc + jit(rnd); done[u] = 1;
      }
    }
    // the rest around the gene they were reached from (which comes first); level-1 partners on a circle
    let n1 = 0;
    if (g.level) for (let u = 0; u < n; u++) if (g.level[u] === 1) n1++;
    let t1 = 0;
    for (let u = 0; u < n; u++) {
      if (done[u]) continue;
      const p = g.parent ? g.parent[u] : -1, bx = p >= 0 ? px[p] : 0, by = p >= 0 ? py[p] : 0;
      if (p < 0) { px[u] = bx; py[u] = by; done[u] = 1; continue; }
      let a, r;
      if (g.level && g.level[u] === 1) { a = 2 * Math.PI * (t1++ + 0.5 * rnd()) / Math.max(1, n1); r = s0 * 2.2; }
      else { a = 2 * Math.PI * rnd(); r = s0 * (0.8 + 0.6 * rnd()); }
      px[u] = bx + r * Math.cos(a); py[u] = by + r * Math.sin(a); done[u] = 1;
    }
  }
  const jit = rnd => (rnd() - 0.5) * 0.5;
  function rebuild(fresh) {
    st.dirty = false;
    const g = kind === "nbr" ? buildNbr() : kind === "mod" ? buildMod() : buildAll();
    const oldIds = st.ids, oldN = oldIds.length, ox = S.x, oy = S.y, ofx = S.fx, ofy = S.fy, ofix = S.fixed;
    if (!g.ids) {
      for (let u = 0; u < oldN; u++) loc[oldIds[u]] = -1;
      st.ids = new Int32Array(0); st.dim = new Uint8Array(0); st.level = new Uint8Array(0); st.byDeg = new Int32Array(0);
      S.load(0, [], [], [], [], []); S.alpha = 0;
      st.msg = g.msg || ""; st.info = ""; st.centre = -1;
      showText(); req();
      return;
    }
    const ids = Int32Array.from(g.ids), n = ids.length;
    const px = new Float32Array(n), py = new Float32Array(n), keep = new Uint8Array(n), old = new Int32Array(n).fill(-1);
    let kept = 0;
    if (!fresh) for (let u = 0; u < n; u++) { const o = loc[ids[u]]; if (o >= 0) { old[u] = o; px[u] = ox[o]; py[u] = oy[o]; keep[u] = 1; kept++; } }
    for (let u = 0; u < oldN; u++) loc[oldIds[u]] = -1;
    for (let u = 0; u < n; u++) { loc[ids[u]] = u; nloc[ids[u]] = -1; }
    place(g, px, py, keep);
    S.load(n, px, py, g.springs.ea, g.springs.eb, g.springs.ec);
    for (let u = 0; u < n; u++) if (old[u] >= 0 && (ofix[old[u]] & 1)) { S.fixed[u] = 1; S.fx[u] = ofx[old[u]]; S.fy[u] = ofy[old[u]]; }
    if (g.centre >= 0) { const c = g.centre; S.fixed[c] |= 4; S.fx[c] = S.x[c]; S.fy[c] = S.y[c]; }
    st.ids = ids; st.dim = g.dim ? Uint8Array.from(g.dim) : new Uint8Array(n); st.level = g.level ? Uint8Array.from(g.level) : new Uint8Array(n);
    st.centre = g.centre; st.info = g.info || ""; st.msg = ""; st.src = g.springs.src;
    const order = Array.from({length: n}, (_, u) => u);
    order.sort((a, b) => (st.dim[a] - st.dim[b]) || (S.deg[b] - S.deg[a]));
    st.byDeg = Int32Array.from(order);
    const most = kept >= 0.6 * n;
    S.alpha = most ? 0.5 : (kind === "all" ? 0.3 : 1);
    if (fresh || !most) {
      st.follow = false;
      st.autoFit = !(kind === "all" && sel >= 0 && sel < N);
      if (kind === "all") st.centreSel = sel >= 0 && sel < N;
    }
    st.groupsDirty = true;
    showText(); req();
  }
  function showText() {
    msgEl.innerHTML = st.msg ? "<div>" + st.msg + "</div>" : ""; msgEl.classList.toggle("on", !!st.msg);
    let key = "";
    if (S.n) {
      const it = s => "<span class='it'>" + s + "</span> ";
      key = "<div class='ky'>" + it("<span class='key' style='border-color:" + WITH + "'></span>moves with") +
        it(S.oppRepel ? "<span class='keyd' style='border-color:" + OPP + "'></span>moves opposite: pushes apart" : "<span class='key' style='border-color:" + OPP + "'></span>moves opposite: pulls together") +
        it("thickness = |cos|") + (st.colour === 1 ? it("<span class='sw' style='background:" + ARMC["+"] + "'></span> + arm") +
        it("<span class='sw' style='background:" + ARMC["-"] + "'></span> &minus; arm") : "") + "</div>";
    }
    itxt.innerHTML = st.info ? st.info + key : "";
    infoEl.classList.toggle("none", !st.info && kind !== "mod");
    st.infoH = infoEl.classList.contains("none") ? 0 : infoEl.offsetHeight;
  }

  // ---------------------------------------------------------------- view
  function computeFit() {
    const n = S.n, x = S.x, y = S.y, top = (st.infoH ? st.infoH + 10 : 0) + 22, bot = 26, side = 24;
    if (!n) return {k: 1, tx: W / 2, ty: H / 2};
    let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    if (n > 3000) {                                            // robust bounds from a sample
      const step = Math.ceil(n / 3000), xs = [], ys = [];
      for (let u = 0; u < n; u += step) { xs.push(x[u]); ys.push(y[u]); }
      xs.sort((a, b) => a - b); ys.sort((a, b) => a - b);
      x0 = quant(xs, .01); x1 = quant(xs, .99); y0 = quant(ys, .01); y1 = quant(ys, .99);
    } else for (let u = 0; u < n; u++) { const a = x[u], b = y[u]; if (a < x0) x0 = a; if (a > x1) x1 = a; if (b < y0) y0 = b; if (b > y1) y1 = b; }
    const w = Math.max(x1 - x0, S.s0 * 3), h = Math.max(y1 - y0, S.s0 * 3);
    const k = Math.max(0.002, Math.min(3, (W - 2 * side) / w, (H - top - bot) / h));
    fitK = k;
    return (lastFit = {k: k, tx: W / 2 - (x0 + x1) / 2 * k, ty: top + (H - top - bot) / 2 - (y0 + y1) / 2 * k});
  }
  function resize() {
    const r = wrapEl.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    DPR = window.devicePixelRatio || 1;
    const w0 = W, h0 = H;
    W = r.width; H = r.height;
    cvs.width = Math.round(W * DPR); cvs.height = Math.round(H * DPR);
    if (!sized) { sized = true; Object.assign(T, computeFit()); Object.assign(V, T); }
    else if (!st.autoFit && !st.follow) { const dx = (W - w0) / 2, dy = (H - h0) / 2; V.tx += dx; V.ty += dy; T.tx += dx; T.ty += dy; }
    if (visible()) req();
  }
  new ResizeObserver(resize).observe(wrapEl);
  const SX = u => S.x[u] * V.k + V.tx, SY = u => S.y[u] * V.k + V.ty;
  // node radius: grows a little when zoomed in; smaller when there are many genes
  const nodeR = () => kind === "all" ? Math.max(1.6, Math.min(5, 2.2 * Math.pow(V.k / fitK, 0.4))) :
    Math.max(2.2, Math.min(9, 5 * Math.min(1, Math.sqrt(300 / Math.max(1, S.n))) * Math.pow(V.k / fitK, 0.3)));
  function centreSel() {
    st.centreSel = false;
    const u = sel >= 0 ? loc[sel] : -1;
    if (u < 0 || !sized) return;
    let far = 0;
    for (let p = S.off[u]; p < S.off[u + 1]; p++) {
      const k = S.adj[p], v = S.ea[k] === u ? S.eb[k] : S.ea[k];
      far = Math.max(far, Math.abs(S.x[v] - S.x[u]), Math.abs(S.y[v] - S.y[u]));
    }
    const f = computeFit(), k = far > 0 ? Math.min(f.k * 60, Math.max(f.k * 2, 0.4 * Math.min(W, H) / far)) : f.k * 6;
    T.k = k; T.tx = W / 2 - S.x[u] * k; T.ty = H / 2 - S.y[u] * k;
    st.autoFit = false; st.follow = true;
  }

  // ---------------------------------------------------------------- frame: simulation steps within a time budget, then draw
  const BUDGET = 13, MAXT = 12;
  function frame(now) {
    if (!sized) resize();
    const run = S.moving() && !st.paused;
    if (run) {
      st.frames.push(now);
      while (st.frames.length > 2 && st.frames[0] < now - 1000) st.frames.shift();
      // several steps per frame when fast; one step every other frame when one step takes longer than ~3 frames
      if (st.avgTick < 45 || (st.skip ^= 1)) {
        const t0 = performance.now();
        let k = 0;
        do { S.tick(); k++; } while (k < MAXT && performance.now() - t0 + st.avgTick < BUDGET);
        const dt = (performance.now() - t0) / k;
        st.avgTick = st.avgTick ? 0.8 * st.avgTick + 0.2 * dt : dt; st.tpf = k;
      }
    } else st.frames.length = 0;
    const f = computeFit();
    if (st.autoFit) Object.assign(T, f);
    let moving = false;
    for (const key of ["k", "tx", "ty"]) {
      const d = T[key] - V[key];
      if (Math.abs(d) > (key === "k" ? V.k * 1e-3 : 0.3)) { V[key] += d * 0.25; moving = true; } else V[key] = T[key];
    }
    if (st.follow && sel >= 0 && loc[sel] >= 0) {               // keep the selected gene where it is on the screen ...
      const u = loc[sel];
      let far = 0;                                               // ... and zoom out when its partners drift out of view
      for (let p = S.off[u]; p < S.off[u + 1]; p++) {
        const k = S.adj[p], v = S.ea[k] === u ? S.eb[k] : S.ea[k];
        far = Math.max(far, Math.abs(S.x[v] - S.x[u]), Math.abs(S.y[v] - S.y[u]));
      }
      if (far > 0) T.k = Math.max(f.k, Math.min(T.k, 0.45 * Math.min(W, H) / far));
      T.tx = W / 2 - S.x[u] * T.k; T.ty = H / 2 - S.y[u] * T.k;
      if (!moving) { V.tx = T.tx; V.ty = T.ty; }
    }
    if (st.groupsDirty && kind === "all") makeGroups();
    const t1 = performance.now();
    draw();
    st.drawMs = performance.now() - t1;
    if (!run || now - st.lastStatus > 300) status();
    return run || moving;
  }
  function makeGroups() {
    st.groupsDirty = false;
    const g = new Map(), n = S.n, u0 = sel >= 0 ? loc[sel] : -1, near = new Set();
    if (u0 >= 0) for (let p = S.off[u0]; p < S.off[u0 + 1]; p++) { const k = S.adj[p]; near.add(S.ea[k] === u0 ? S.eb[k] : S.ea[k]); }
    for (let u = 0; u < n; u++) {
      const i = st.ids[u];
      let a = 1;
      if (hlMod >= 0 && D.mod[i] !== hlMod) a = 0.13;
      if (u0 >= 0 && u !== u0 && !near.has(u)) a = Math.min(a, 0.45);
      const c = nodeColour(i), key = a + c;
      let e = g.get(key);
      if (!e) { e = {c: c, a: a, idx: []}; g.set(key, e); }
      e.idx.push(u);
    }
    st.groups = [...g.values()].sort((p, q) => (p.a - q.a) || ((q.c === GREY) - (p.c === GREY)));
    for (const e of st.groups) e.idx = Int32Array.from(e.idx);
  }
  function selNeighbours() {                                    // [node, cos] of the selected gene's springs, strongest first
    const u = sel >= 0 ? loc[sel] : -1, out = [];
    if (u < 0) return out;
    for (let p = S.off[u]; p < S.off[u + 1]; p++) { const k = S.adj[p]; out.push([S.ea[k] === u ? S.eb[k] : S.ea[k], S.ec[k]]); }
    return out.sort((a, b) => Math.abs(b[1]) - Math.abs(a[1]));
  }
  function draw() {
    const n = S.n;
    g2.setTransform(1, 0, 0, 1, 0, 0);
    if (layer) layer(S.x || [], S.y || [], 1, n ? st.groups : null, V.k, V.tx, V.ty, DPR, nodeR());
    else { g2.fillStyle = SURF; g2.fillRect(0, 0, cvs.width, cvs.height); }
    g2.setTransform(DPR, 0, 0, DPR, 0, 0);
    if (!n) return;
    const r = nodeR(), nb = selNeighbours();
    if (kind !== "all") { drawEdges(); drawNodes(r); }
    else drawSelected(r, nb);
    if (kind === "mod") drawArmLabels(r);
    drawLabels(r, nb);
    if (st.hover >= 0 && st.hover < n) {
      g2.beginPath(); g2.arc(SX(st.hover), SY(st.hover), r + 3, 0, 2 * Math.PI);
      g2.lineWidth = 1.5; g2.strokeStyle = INK; g2.stroke();
    }
  }
  function drawEdges() {
    const m = S.m, ea = S.ea, eb = S.eb, ec = S.ec, dim = st.dim, paths = [];
    const dens = Math.max(0.08, Math.min(1, Math.sqrt(160 / Math.max(1, m))));   // many edges: each one lighter
    for (let b = 0; b < 16; b++) paths.push(null);
    for (let e = 0; e < m; e++) {
      const a = ea[e], b = eb[e], c = ec[e], wb = Math.min(3, Math.floor(Math.abs(c) * 4));
      const bk = ((dim[a] || dim[b]) ? 8 : 0) + (c < 0 ? 4 : 0) + wb;
      const p = paths[bk] || (paths[bk] = new Path2D());
      p.moveTo(SX(a), SY(a)); p.lineTo(SX(b), SY(b));
    }
    g2.lineCap = "round";
    for (let bk = 0; bk < 16; bk++) {
      if (!paths[bk]) continue;
      const dimmed = bk >= 8, neg = (bk & 4) !== 0, w = ((bk & 3) + 0.5) / 4, push = neg && S.oppRepel;
      g2.strokeStyle = neg ? OPP : WITH;
      g2.lineWidth = push ? 0.3 + 1.8 * w : 0.35 + 3 * w;    // thickness proportional to |cos|; pushers thinner
      g2.globalAlpha = dimmed ? 0.14 : dens * (push ? 0.1 + 0.25 * w : 0.3 + 0.5 * w);
      g2.setLineDash(push ? [5, 4] : []);
      g2.stroke(paths[bk]);
    }
    g2.setLineDash([]); g2.globalAlpha = 1;
  }
  function drawNodes(r0) {
    const n = S.n, ids = st.ids, dim = st.dim, fixed = S.fixed;
    for (let pass = 0; pass < 2; pass++) for (let u = 0; u < n; u++) {
      if ((dim[u] ? 0 : 1) !== pass) continue;
      const i = ids[u], X = SX(u), Y = SY(u);
      if (X < -20 || Y < -20 || X > W + 20 || Y > H + 20) continue;
      const r = i === sel ? r0 + 3 : (pset.has(i) && kind === "nbr") ? r0 + 1 : r0;
      g2.beginPath(); g2.arc(X, Y, r, 0, 2 * Math.PI);
      g2.globalAlpha = dim[u] ? 0.5 : 1;
      g2.fillStyle = dim[u] ? GREY : nodeColour(i); g2.fill();
      if (n < 800) { g2.lineWidth = 1; g2.strokeStyle = SURF; g2.stroke(); }
      g2.globalAlpha = 1;
      if (fixed[u] & 5) { g2.beginPath(); g2.arc(X, Y, r + (i === sel ? 4.5 : 2.2), 0, 2 * Math.PI); g2.lineWidth = 1.6; g2.strokeStyle = INK2; g2.stroke(); }
      if (i === sel) { g2.beginPath(); g2.arc(X, Y, r + 1, 0, 2 * Math.PI); g2.lineWidth = 2.5; g2.strokeStyle = INK; g2.stroke(); }
    }
  }
  function drawSelected(r, nb) {                                // all-genes tab: edges only for the selected gene
    const u0 = sel >= 0 ? loc[sel] : -1;
    if (u0 < 0) return;
    const X0 = SX(u0), Y0 = SY(u0);
    for (const [v, c] of nb) {
      const a = Math.abs(c);
      g2.strokeStyle = c > 0 ? WITH : OPP; g2.globalAlpha = 0.35 + 0.55 * a; g2.lineWidth = 0.6 + 2.6 * a;
      g2.setLineDash(c < 0 && S.oppRepel ? [5, 4] : []);
      g2.beginPath(); g2.moveTo(X0, Y0); g2.lineTo(SX(v), SY(v)); g2.stroke();
    }
    g2.setLineDash([]); g2.globalAlpha = 1;
    for (const [v, c] of nb) {
      g2.beginPath(); g2.arc(SX(v), SY(v), r + 1.5, 0, 2 * Math.PI);
      g2.fillStyle = nodeColour(st.ids[v]); g2.fill(); g2.lineWidth = 2; g2.strokeStyle = c > 0 ? WITH : OPP; g2.stroke();
    }
    for (let u = 0; u < S.n; u++) if (S.fixed[u] & 5) { g2.beginPath(); g2.arc(SX(u), SY(u), r + 2.2, 0, 2 * Math.PI); g2.lineWidth = 1.6; g2.strokeStyle = INK2; g2.stroke(); }
    g2.beginPath(); g2.arc(X0, Y0, r + 4, 0, 2 * Math.PI);
    g2.fillStyle = nodeColour(sel); g2.fill(); g2.lineWidth = 2.5; g2.strokeStyle = INK; g2.stroke();
  }
  function armSplit() {                                       // per arm: [sum x, sum y, n, sum x^2 + y^2, top screen y]
    const s = {"+": [0, 0, 0, 0, Infinity], "-": [0, 0, 0, 0, Infinity]};
    for (let u = 0; u < S.n; u++) {
      if (st.dim[u]) continue;
      const v = s[D.arm[st.ids[u]]];
      if (!v) continue;
      const x = S.x[u], y = S.y[u], Y = SY(u);
      v[0] += x; v[1] += y; v[2]++; v[3] += x * x + y * y; if (Y < v[4]) v[4] = Y;
    }
    return s;
  }
  function drawArmLabels(r) {
    // "+ arm" / "- arm" over each arm, once the two arms have parted (centroids further apart than the arms are wide)
    const md = MODS.get(st.module);
    if (!md || !md.opp) return;
    const s = armSplit(), p = s["+"], m = s["-"];
    if (p[2] < 2 || m[2] < 2) return;
    const c = v => [v[0] / v[2], v[1] / v[2]], sd = v => { const q = c(v); return Math.sqrt(Math.max(0, v[3] / v[2] - q[0] * q[0] - q[1] * q[1])); };
    const cp = c(p), cm = c(m);
    if (Math.hypot(cp[0] - cm[0], cp[1] - cm[1]) < 1.3 * (sd(p) + sd(m)) / 2) return;
    g2.textAlign = "center"; g2.textBaseline = "middle";
    halo(g2, "+ arm (" + p[2] + ")", cp[0] * V.k + V.tx, Math.max(14, p[4] - r - 14), "700 13px " + FF, ARMC["+"]);
    halo(g2, "− arm (" + m[2] + ")", cm[0] * V.k + V.tx, Math.max(14, m[4] - r - 14), "700 13px " + FF, ARMC["-"]);
  }
  function drawLabels(r, nb) {
    const n = S.n, label = Labeler(g2), seen = new Uint8Array(n), ids = st.ids;
    g2.textAlign = "left"; g2.textBaseline = "middle";
    const zoom = V.k / fitK, everyone = kind === "all" ? zoom > 5 : (n <= 150 || zoom > 1.8);
    let placed = 0;
    const put = (u, font, colour, hgt) => {
      if (seen[u] || placed > 450) return;
      seen[u] = 1;
      const X = SX(u), Y = SY(u);
      if (X < -40 || Y < -10 || X > W || Y > H + 10) return;
      if (label(D.sym[ids[u]], X + r + 4, Y, font, colour, hgt)) placed++;
    };
    const u0 = sel >= 0 ? loc[sel] : -1;
    if (u0 >= 0) put(u0, "700 13px " + FF, INK, 15);
    for (const [v, c] of nb) put(v, "600 11px " + FF, c > 0 ? WITH_T : OPP_T, 12);
    if (st.hover >= 0 && st.hover < n) put(st.hover, "600 11px " + FF, INK, 12);
    for (let u = 0; u < n; u++) if (S.fixed[u] & 5) put(u, "600 11px " + FF, INK2, 12);
    if (everyone) for (const u of st.byDeg) { if (placed > 450) break; put(u, "11px " + FF, st.dim[u] ? "#a3a29b" : INK2, 12); }
  }

  // ---------------------------------------------------------------- status line and tooltip
  function fps() { const f = st.frames; return f.length > 2 ? (f.length - 1) * 1000 / (f[f.length - 1] - f[0]) : 0; }
  function status() {
    st.lastStatus = performance.now();
    if (!S.n) { statusEl.textContent = ""; return; }
    const s = [S.n.toLocaleString() + " genes", S.m.toLocaleString() + " springs",
      st.paused ? "paused" : S.moving() ? "moving (alpha " + S.alpha.toFixed(2) + ")" : "settled"];
    const f = fps();
    if (f && !st.paused && S.moving()) s.push(Math.round(f) + " frames/s, " + st.tpf + " step" + (st.tpf === 1 ? "" : "s") + " per frame");
    s.push("drag a gene = move it, double-click = pin, click = select, wheel = zoom");
    statusEl.textContent = s.join("  ·  ");
  }
  function springCos(a, b) {
    if (a < 0 || b < 0) return null;
    for (let p = S.off[a]; p < S.off[a + 1]; p++) { const k = S.adj[p]; if ((S.ea[k] === a ? S.eb[k] : S.ea[k]) === b) return S.ec[k]; }
    return null;
  }
  function showTipP(u, mx, my) {
    const i = st.ids[u];
    let h = tipHtml(i);
    if (sel >= 0 && i !== sel) {
      const c = springCos(loc[sel], u);
      if (c != null) h += "<br>" + (c > 0 ? "moves with " : "moves opposite to ") + esc(D.sym[sel]) + " (cos " + (c > 0 ? "+" : "") + c.toFixed(2) + ")";
    }
    if (st.dim[u]) h += "<br><span class='m'>outside the module</span>";
    h += "<br><span class='m'>" + ((S.fixed[u] & 5) ? "pinned: double-click to unpin" : "drag to move, double-click to pin") + "</span>";
    placeTip(tipEl, h, mx, my, W, H);
  }
  const hideTipP = () => { tipEl.style.display = "none"; };

  // ---------------------------------------------------------------- pointer: drag a gene, pan, zoom, click, double-click
  function hit(mx, my) {
    const n = S.n, r = Math.max(7, nodeR() + 3);
    let best = -1, bd = r * r;
    for (let u = 0; u < n; u++) {
      const dx = SX(u) - mx, dy = SY(u) - my, d = dx * dx + dy * dy;
      if (d < bd) { bd = d; best = u; }
    }
    return best;
  }
  const world = p => [(p[0] - V.tx) / V.k, (p[1] - V.ty) / V.k];
  function zoomAtP(mx, my, f, immediate) {
    const k = Math.min(fitK * 400, Math.max(fitK * 0.2, T.k * f)), g = k / T.k;
    T.tx = mx - (mx - T.tx) * g; T.ty = my - (my - T.ty) * g; T.k = k;
    if (immediate) Object.assign(V, T);
    st.autoFit = false; st.follow = false;
    req();
  }
  cvs.addEventListener("pointerdown", e => {
    cvs.setPointerCapture(e.pointerId);
    const p = local(e, cvs);
    ptrs.set(e.pointerId, p);
    downAt = p; dragged = false;
    if (ptrs.size === 2) {
      const [a, b] = [...ptrs.values()];
      pinch = {d: Math.hypot(a[0] - b[0], a[1] - b[1]), k: T.k};
      if (st.drag >= 0) { S.fixed[st.drag] &= ~2; S.alphaTarget = 0; st.drag = -1; }
      return;
    }
    const u = e.button === 0 ? hit(p[0], p[1]) : -1;
    if (u >= 0) { st.drag = u; S.fx[u] = S.x[u]; S.fy[u] = S.y[u]; S.fixed[u] |= 2; }
    cvs.classList.add("drag");
  });
  cvs.addEventListener("pointermove", e => {
    const p = local(e, cvs);
    if (ptrs.has(e.pointerId)) {
      const q0 = ptrs.get(e.pointerId);
      ptrs.set(e.pointerId, p);
      if (ptrs.size === 2 && pinch) {
        const [a, b] = [...ptrs.values()], d = Math.hypot(a[0] - b[0], a[1] - b[1]);
        zoomAtP((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, (pinch.k * d / Math.max(pinch.d, 1)) / T.k, true);
        dragged = true;
        return;
      }
      if (Math.abs(p[0] - downAt[0]) + Math.abs(p[1] - downAt[1]) > 3) dragged = true;
      if (st.drag >= 0) {
        if (!dragged) return;
        const u = st.drag, w = world(p);
        S.fx[u] = w[0]; S.fy[u] = w[1];
        if (st.paused) { S.x[u] = w[0]; S.y[u] = w[1]; }
        else { S.alphaTarget = 0.3; S.heat(0.15); }
        st.autoFit = false;
        hideTipP(); req();
        return;
      }
      const dx = p[0] - q0[0], dy = p[1] - q0[1];
      V.tx += dx; V.ty += dy; T.tx += dx; T.ty += dy;
      st.autoFit = false; st.follow = false;
      hideTipP(); req();
      return;
    }
    const u = hit(p[0], p[1]);
    if (u !== st.hover) { st.hover = u; cvs.classList.toggle("onnode", u >= 0); req(); }
    if (u >= 0) showTipP(u, p[0], p[1]); else hideTipP();
  });
  function endP(e) {
    ptrs.delete(e.pointerId);
    if (ptrs.size < 2) pinch = null;
    if (ptrs.size === 0) cvs.classList.remove("drag");
  }
  cvs.addEventListener("pointerup", e => {
    const wasDrag = dragged, u = st.drag;
    endP(e);
    if (u >= 0) { S.fixed[u] &= ~2; S.alphaTarget = 0; st.drag = -1; req(); }
    if (!wasDrag && e.button === 0 && u >= 0) {
      const i = st.ids[u];
      clearTimeout(clickTimer);
      const g0 = selGen;                                         // wait: a double-click pins instead; any other
      if (i !== sel) clickTimer = setTimeout(() => { if (selGen === g0) select(i, false, kind); }, 240);   // selection meanwhile wins
    }
  });
  cvs.addEventListener("pointercancel", e => { endP(e); if (st.drag >= 0) { S.fixed[st.drag] &= ~2; S.alphaTarget = 0; st.drag = -1; } });
  cvs.addEventListener("pointerleave", () => { if (st.hover >= 0) { st.hover = -1; req(); } hideTipP(); });
  cvs.addEventListener("dblclick", e => {
    clearTimeout(clickTimer);
    const p = local(e, cvs), u = hit(p[0], p[1]);
    if (u < 0) { zoomAtP(p[0], p[1], 2, false); return; }
    if (S.fixed[u] & 5) S.fixed[u] &= ~5;
    else { S.fixed[u] |= 1; S.fx[u] = S.x[u]; S.fy[u] = S.y[u]; }
    S.heat(0.1); setPaused(false); req();
    if (st.hover === u) showTipP(u, p[0], p[1]);
  });
  cvs.addEventListener("wheel", e => {
    e.preventDefault();
    const [mx, my] = local(e, cvs), dy = e.deltaMode === 1 ? e.deltaY * 33 : e.deltaY;
    zoomAtP(mx, my, Math.exp(-dy * 0.0016), false);
    hideTipP();
  }, {passive: false});

  // ---------------------------------------------------------------- controls
  function segSet(k, on, nb) { for (let t = 0; t < nb; t++) { const b = q(k + t); if (b) b.setAttribute("aria-pressed", t === on); } }
  function setPaused(p) {
    st.paused = p;
    const b = q("pause");
    b.textContent = p ? "Resume" : "Pause"; b.setAttribute("aria-pressed", p);
    status(); req();
  }
  function setOpp(rep) {
    S.oppRepel = rep; segSet("opp", rep ? 1 : 0, 2);
    S.heat(kind === "all" ? 0.5 : 0.8); setPaused(false); showText(); req();
  }
  function setModule(m) {
    if (!MODS.has(m)) return;
    if (m !== st.module) { st.module = m; st.dirty = true; }
    syncPicker();
    if (m !== hlMod) highlight(m);                             // the side panel shows the module card
    if (st.dirty && visible()) rebuild(false);
  }
  function syncPicker() {
    const s = q("msel");
    if (!s) return;
    if (!s.options.length) s.innerHTML = D.mods.map(m => "<option value='" + m.id + "'>" + esc("M" + m.id + " · " + (m.label.length > 48 ? m.label.slice(0, 46) + "…" : m.label) + " (" + m.n + ")") + "</option>").join("");
    s.value = String(st.module);
  }
  pane.addEventListener("click", e => {
    const b = e.target.closest("button[data-k]");
    if (!b) return;
    const k = b.dataset.k;
    if (k === "opp0" || k === "opp1") setOpp(k === "opp1");
    else if (k === "col0" || k === "col1") { st.colour = k === "col1" ? 1 : 0; segSet("col", st.colour, 2); st.groupsDirty = true; showText(); req(); }
    else if (k === "pause") setPaused(!st.paused);
    else if (k === "heat") { S.heat(kind === "all" ? 0.5 : 0.8); setPaused(false); }
    else if (k === "reset") { rebuild(true); st.autoFit = true; st.follow = false; setPaused(false); }
    else if (k === "fit") { st.autoFit = true; st.follow = false; req(); }
    else if (k === "dep0" || k === "dep1") { st.depth = k === "dep1" ? 2 : 1; segSet("dep", st.depth - 1, 2); rebuild(false); }
    else if (k === "mselg") { if (sel >= 0 && sel < N && D.mod[sel] > 0) setModule(D.mod[sel]); }
  });
  const out = (k, v) => { const o = q(k + "o"); if (o) o.textContent = v; };
  const sliders = () => {
    S.rep = +q("rep").value; S.spr = +q("spr").value / 100; st.minCos = +q("min").value / 100;
    out("rep", S.rep); out("spr", S.spr.toFixed(1) + "×"); out("min", st.minCos.toFixed(2));
  };
  sliders();
  q("rep").addEventListener("input", () => { sliders(); S.heat(0.3); setPaused(false); });
  q("spr").addEventListener("input", () => { sliders(); S.heat(0.3); setPaused(false); });
  q("min").addEventListener("input", sliders);
  q("min").addEventListener("change", () => { sliders(); rebuild(false); });
  q("ev").addEventListener("change", () => { st.ev = +q("ev").value; rebuild(false); });
  if (q("max")) q("max").addEventListener("change", () => { st.maxN = Math.max(10, Math.min(3000, +q("max").value || 300)); q("max").value = st.maxN; rebuild(false); });
  if (q("msel")) q("msel").addEventListener("change", () => setModule(+q("msel").value));
  if (q("ring")) q("ring").addEventListener("change", () => { st.ring = q("ring").checked; rebuild(false); });

  // ---------------------------------------------------------------- the rest of the page talks to the tab through these
  return {
    frame: frame,
    show: () => {
      resize();
      const first = !S.n && !st.msg;
      if (st.dirty || first) rebuild(st.fresh);
      st.fresh = false;
      if (first) { Object.assign(T, computeFit()); Object.assign(V, T); }
      if (kind === "all" && st.centreSel) { centreSel(); Object.assign(V, T); }
      showText(); status(); req();
    },
    onSelect: origin => {
      if (kind === "nbr") st.dirty = true;
      else if (kind === "mod") {
        if (origin !== "mod" && sel >= 0 && sel < N && D.mod[sel] > 0 && D.mod[sel] !== st.module) { st.module = D.mod[sel]; st.dirty = true; syncPicker(); }
      } else if (origin !== "all") st.centreSel = sel >= 0 && sel < N;
      st.groupsDirty = true;
      if (visible()) { if (st.dirty) rebuild(false); if (st.centreSel) centreSel(); req(); }
    },
    onHighlight: m => {
      if (kind === "mod" && m > 0 && m !== st.module && MODS.has(m)) { st.module = m; st.dirty = true; syncPicker(); }
      st.groupsDirty = true;
      if (visible()) { if (st.dirty) rebuild(false); req(); }
    },
    togglePause: () => setPaused(!st.paused),
    state: () => ({kind: kind, n: S.n, m: S.m, ids: Array.from(st.ids), x: Array.from(S.x || []), y: Array.from(S.y || []),
      fixed: Array.from(S.fixed || []), alpha: S.alpha, moving: S.moving(), paused: st.paused, opposite: S.oppRepel ? "repel" : "attract",
      module: st.module, depth: st.depth, msg: st.msg, springs: st.src, ticks: S.ticks}),
    screen: i => { const u = i >= 0 && i < NA ? loc[i] : -1; return u < 0 ? null : {x: SX(u), y: SY(u), w: W, h: H}; },
    stats: () => ({fps: fps(), tickMs: st.avgTick, drawMs: st.drawMs, ticksPerFrame: st.tpf, alpha: S.alpha, n: S.n, m: S.m}),
    benchTick: k => { const a = S.alpha; S.alpha = Math.max(a, 0.5); const t0 = performance.now(); for (let r = 0; r < k; r++) S.tick(); const ms = (performance.now() - t0) / k; return ms; },
  };
}

// ================================================================ selection (shared by every tab) and the side panel
function select(i, centre, origin) {
  sel = i; focus = "gene"; selGen++;
  P = partnersOf(i); pset = new Set(P.map(p => p.j));
  qi.value = i >= 0 ? D.sym[i] : "";
  if (i >= 0 && i < N) {
    if (isMap(active)) { if (centre) centreOn(i, layout); mapSelPending = false; }
    else mapSelPending = true;                     // centre the map on it when the map tab is shown again
  }
  try { history.replaceState(null, "", i >= 0 ? "#" + encodeURIComponent(D.sym[i]) : location.pathname + location.search); } catch (err) { /* file:// in some browsers */ }
  regroup(); renderPanel(); status();
  for (const k in PHYS) PHYS[k].onSelect(origin || "");
}
const ddLabel = d => (d >= 0 && D.dd[d]) ? D.dd[d] : (d >= 0 ? "drug-dose " + d : "");
const foldOf = l100 => Math.pow(2, l100 / 100);
const fdrTxt = f => f == null ? "" : (f < 0.01 ? "&lt;0.01" : f.toFixed(2));
function moduleCard(m) {
  const md = MODS.get(m);
  if (!md) return "";
  const cb = md.cb == null ? "" : "mean cos between the two sides " + (md.cb > 0 ? "+" : "") + md.cb.toFixed(2);
  const arms = md.opp ? md.np + " in the + arm, " + md.nm + " in the &minus; arm; the arms move opposite (" + cb + ")" :
    "single-armed: " + (cb ? "the two sides of its main direction are not two opposite arms (" + cb + "; a &minus; arm needs &ge; 5 genes on its side and &le; &minus;0.2)" : "all genes on one side of its main direction");
  return "<div class='mcard'><div><span class='sw' style='background:" + modColour(m) + "'></span> <b>Module " + m + "</b> " +
    "<span class='note'>" + md.n + " genes: " + arms + "</span>" +
    " <span class='lk' data-hl='-1' style='float:right'>clear</span></div>" +
    "<div class='row'><b>" + esc(md.label) + "</b> <span class='lk' data-mtab='" + m + "'>simulate</span></div>" +
    (md.plus ? "<div class='row'><span class='lbl'>" + (md.opp ? "+ arm" : "genes") + ":</span> " + esc(md.plus) + "</div>" : "") +
    (md.minus ? "<div class='row'><span class='lbl'>&minus; arm:</span> " + esc(md.minus) + "</div>" : "") +
    (md.up ? "<div class='row'><span class='lbl'>Drug-doses that raise it (" + (md.opp ? "+ arm up, &minus; arm down; mean pooled z of the + arm minus the &minus; arm" : "mean pooled z of its genes") + "; |z| &ge; " + D.mod_z + "; &dagger; = artifact flag):</span> " + esc(md.up) + "</div>" : "") +
    (md.down ? "<div class='row'><span class='lbl'>... that lower it:</span> " + esc(md.down) + "</div>" : "") +
    (md.lines ? "<div class='row'><span class='lbl' title='largest mean |module score| over its 8 strongest drug-doses'>Most responsive cell lines:</span> " + esc(md.lines) + "</div>" : "") +
    "</div>";
}
function drugTable(a, dir) {
  if (!has(a)) return "<p class='note'>No clean drug-dose " + (dir > 0 ? "raises" : "lowers") + " it pooled over the cell lines (median; |z| &ge; 3 or q &lt; 0.1). A response in fewer than about half of the lines does not reach the pooled data: see the cell lines below.</p>";
  let h = "<table><tr><th>Drug-dose</th><th class='r' title='fold change pooled over the cell lines (median)'>fold</th><th class='r'>z</th><th class='r' title='cell lines that move the same way (per-line z &ge; 2 and &ge; 1.2x)'>lines</th></tr>";
  for (let t = 0; t + 3 < a.length; t += 4)
    h += "<tr><td>" + esc(ddLabel(a[t])) + "</td><td class='r'>" + foldOf(dir * a[t + 1]).toFixed(2) + "&times;</td><td class='r'>" +
      (dir * a[t + 2] / 10).toFixed(1) + "</td><td class='r'>" + a[t + 3] + "</td></tr>";
  return h + "</table>";
}
function lineTable(a) {
  if (!has(a)) return "<p class='note'>Not measured in any line (not expressed, or only ambient RNA), or no per-line data.</p>";
  let h = "<table><tr><th>Cell line</th><th class='r' title='clean drug-doses raising it in this line (per-line z &ge; " + D.line_z + ", &ge; 1.5x)'>&uarr;</th><th class='r' title='... lowering it'>&darr;</th><th>strongest drug-dose here</th></tr>";
  for (let t = 0; t + 5 < a.length; t += 6) {
    const l = a[t], org = D.organ[l] ? " <span class='note'>" + esc(D.organ[l]) + "</span>" : "";
    const best = a[t + 3] >= 0 ? esc(ddLabel(a[t + 3])) + " <span class='note'>" + foldOf(a[t + 4]).toFixed(2) + "&times;, z " + (a[t + 5] / 10).toFixed(1) + "</span>" : "&ndash;";
    h += "<tr><td>" + esc(D.lines[l] || ("line " + l)) + org + "</td><td class='r'>" + a[t + 1] + "</td><td class='r'>" + a[t + 2] +
      "</td><td>" + best + "</td></tr>";
  }
  return h + "</table><p class='note'>&uarr; / &darr; = clean drug-doses moving it &ge; 1.5&times; at per-line |z| &ge; " + D.line_z +
    (D.line_z_cal ? " (calibrated on this run" + (D.line_chance != null ? ": about " + D.line_chance + " chance calls per gene and line" : "") + ")" : " (not calibrated in this run: a per-line z of 4-5 can arise by chance)") +
    "; the strongest of them is shown, &ndash; = none.</p>";
}
const LIT = new Map();                             // literature verdicts (OUT/review): a * NA + b -> [verdict, citations]
if (D.lit) for (let t = 0; t + 3 < D.lit.length; t += 4) LIT.set(D.lit[t] * NA + D.lit[t + 1], [D.lit[t + 2], D.lit[t + 3]]);
function litBadge(i, j) {
  let v = LIT.get(i * NA + j), from = "";
  if (!v) { v = LIT.get(j * NA + i); if (v) from = " (in " + D.sym[j] + "'s review)"; }
  if (!v) return "";
  const name = D.lit_v[v[0]] || "?";
  return "<span class='bd lit lit-" + esc(name) + "' title='AI-agent literature review" + esc(from) + ": " + esc(name) + ", " + v[1] +
    " citation" + (v[1] === 1 ? "" : "s") + " (review/connections.parquet; the vault note has the review and its links)'>lit: " + esc(name) + "</span>";
}
function partnerTable() {
  if (!P.length) return "<p class='note'>No partners recorded.</p>";
  let h = "<table class='pt'><tr><th>Gene</th><th class='r' title='signed cosine: +1 = same direction, -1 = opposite'>cos</th><th title='both = same sign with fdr &le; 0.10 in two random halves of the compounds; one = strong in one random half only (not replicated, no error estimate); none = neither'>halves</th><th class='r' title='estimated share of false relations among pairs at least this strong in both halves'>fdr</th><th>flags</th></tr>";
  let nLit = 0;
  for (const p of P) {
    let f = LIT.size ? litBadge(sel, p.j) : "";
    if (f) nLit++;
    if (p.novel && D.novel_ok) f += "<span class='bd nov' title='both halves, fdr <= 0.05, |cos| >= 0.5, not in any reference set, not the same locus'>novel?</span>";
    if (p.locus) f += "<span class='bd loc' title='within 50 kb of each other'>same locus</span>";
    if (p.rt) f += "<span class='bd rt' title='same strand, <= 20 kb, the 5-prime gene much more expressed: read-through can make them correlate'>read-through risk</span>";
    if (p.known) {
      if (p.string) f += "<span class='bd' title='known: STRING combined score " + p.string + "'>STRING " + p.string + "</span>";
      if (p.pw >= 0 && D.pw[p.pw]) f += "<span class='bd' title='known: shared pathway " + esc(D.pw[p.pw]) + "'>pathway</span>";
      if (p.group) f += "<span class='bd' title='known: same HGNC gene group'>family</span>";
      if (!p.string && p.pw < 0 && !p.group) f += "<span class='bd'>known</span>";
    }
    h += "<tr class='ck' data-g='" + p.j + "'><td><span class='k' style='background:" + (p.cos > 0 ? WITH : OPP) + "'></span>" + esc(D.sym[p.j]) +
      "</td><td class='r'>" + (p.cos > 0 ? "+" : "") + p.cos.toFixed(2) + "</td><td>" + EVS[p.ev] + "</td><td class='r'>" + fdrTxt(p.fdr) + "</td><td>" + f + "</td></tr>";
  }
  h += "</table>";
  if (nLit) h += "<p class='note'><span class='bd lit'>lit:</span> = the verdict of an AI-agent literature review on the pair (established, indirect, plausible, unexpected, contradicted); not checked by a person. The review itself is in the gene's vault note.</p>";
  if (!D.novel_ok) h += "<p class='note'>Novelty not assessed: " + esc((D.novel_blocked || []).join(", ") || "reference sources") + " missing, so no pair is called novel.</p>";
  return h;
}
function whyOut(w) {
  // the embed stage's inclusion rule, with its counts (embed/info.json)
  const E = D.embed || {}, need = E.min_responsive || D.min_responsive || 5;
  let h = "it reaches per-line |z| &ge; 3 in " + w + " of the " + (E.drugdoses_active != null ?
    E.drugdoses_active + " active, trustworthy drug-doses &times; " + (E.lines != null ? E.lines : D.lines.length) + " lines the space is built from (drug-doses with &ge; " + (E.min_active || 10) + " significant genes, pooled or in single lines, and no untrusted flag)" :
    "(drug-dose, cell line) contexts the space is built from");
  if (w < need) return h + "; the space needs " + need + ".";
  h += "; that count is not enough on its own: the space also needs a significant clean pooled drug-dose (q &lt; 0.1, &ge; 1.2&times;)" +
    (E.line_z_responsive != null ? " or a per-line |z| &ge; " + (+E.line_z_responsive).toFixed(1) + " in &ge; 2 lines of one drug-dose" : "") + ", and it has neither";
  if (E.null_rate != null) h += " (chance rate of |z| &ge; 3 per context " + (+E.null_rate).toPrecision(2) + ")";
  if (E.n_genes_excluded_chance != null) h += "; " + E.n_genes_excluded_chance.toLocaleString() + " genes of this run reach the count without either";
  return h + ".";
}
function geneCard(i) {
  let h = "<h2>" + esc(D.sym[i]) + "</h2>";
  if (has(D.name) && D.name[i]) h += "<div class='nm'>" + esc(D.name[i]) + "</div>";
  if (has(D.fn) && D.fn[i]) h += "<p class='fn'>" + esc(D.fn[i]) + "</p>";
  if (has(D.alias) && D.alias[i]) h += "<p class='note'>Also: " + esc(D.alias[i].split("|").join(", ")) + "</p>";
  if (i < N) {
    const m = D.mod[i], arm = D.arm[i], md = MODS.get(m);
    h += "<p><span class='k' style='background:" + modColour(m) + "'></span>" + (m > 0 ? "<span class='lk' data-hl='" + m + "'>Module " + m + "</span>" +
      (md && !md.opp ? ", single-armed" : arm !== "." ? ", " + (arm === "-" ? "&minus;" : "+") + " arm" : "") + (md ? " &middot; " + esc(md.label) : "") : "No module") + "</p>";
  } else {
    const w = D.why[i - N];
    h += "<p class='note'><b>Not on the map:</b> " + (w === -1 ? "a noise-class RNA (left out of the vector space by design)." :
      w === -2 ? "in the vector space but not laid out." : whyOut(w)) + "</p>";
  }
  const c = D.cpm[i];
  const nl = D.nlx[i];
  h += "<p class='note'>Level " + (c == null ? "?" : c.toLocaleString()) + " CPM (pooled)" + (nl >= 0 ? ", expressed in " + nl + " of " + D.lines.length + " cell lines" : "") +
    ". Raised by " + D.nup[i] + " and lowered by " + D.ndn[i] + " clean drug-doses (q &lt; 0.1, &ge; 1.2x).</p>";
  if (i < N) {
    h += "<h3>Moves with (<span style='color:" + WITH + "'>green</span>) or opposite to (<span style='color:" + OPP + "'>red</span>) &mdash; top " + P.length + "</h3>" + partnerTable();
  }
  h += "<h3>Drug-doses that raise it</h3>" + drugTable(D.up[i], 1);
  h += "<h3>Drug-doses that lower it</h3>" + drugTable(D.dn[i], -1);
  h += "<h3>Cell lines where it responds most</h3>" + lineTable(D.ln[i]);
  h += "<p class='note' style='margin-top:12px'>Fold = vs the same cell line's typical treated well on the plate (not DMSO), pooled over the cell lines (median); only drug-doses without technical-artifact flags. <span class='lk' data-help='1'>How to read this</span></p>";
  return h;
}
function renderPanel() {
  const g = sel >= 0 ? geneCard(sel) : "", m = hlMod >= 0 ? moduleCard(hlMod) : "";
  let h = (focus === "module" || !g) ? m + g : g + (m ? "<h3>Highlighted module</h3>" + m : "");
  if (!h) h = "<p class='note'>Click a gene on the map or search for one. <span class='lk' data-help='1'>How to read this</span></p>" + HOWTO_MAPS;
  $("panel").innerHTML = h;
  $("panel").scrollTop = 0;
}
$("panel").addEventListener("click", e => {
  const g = e.target.closest("[data-g]"), m = e.target.closest("[data-hl]"), hp = e.target.closest("[data-help]"), mt = e.target.closest("[data-mtab]");
  if (g) select(+g.dataset.g, true, "panel");
  else if (mt) { if (+mt.dataset.mtab !== hlMod) highlight(+mt.dataset.mtab); showTab("mod"); }
  else if (m) highlight(+m.dataset.hl === hlMod ? -1 : +m.dataset.hl);
  else if (hp) showTab("help");
});

// ---------------------------------------------------------------- search
const SYM_L = D.sym.map(s => s.toLowerCase());
const ALI = [];
if (has(D.alias)) D.alias.forEach((s, i) => { if (s) for (const a of s.split("|")) if (a) ALI.push([a.toLowerCase(), a, i]); });
function search(q) {
  q = q.trim().toLowerCase();
  if (!q) return [];
  const out = [], seen = new Set(), MAX = 14;
  const add = (i, via) => { if (!seen.has(i) && out.length < MAX) { seen.add(i); out.push({i: i, via: via}); } };
  const bylen = (a, b) => (D.sym[a].length - D.sym[b].length) || (a >= N) - (b >= N) || (D.sym[a] < D.sym[b] ? -1 : 1);
  for (let i = 0; i < NA; i++) if (SYM_L[i] === q) add(i);
  for (const [l, a, i] of ALI) if (l === q) add(i, a);
  let pre = [];
  for (let i = 0; i < NA; i++) if (SYM_L[i].startsWith(q)) pre.push(i);
  pre.sort(bylen).forEach(i => add(i));
  for (const [l, a, i] of ALI) { if (out.length >= MAX) break; if (l.startsWith(q)) add(i, a); }
  for (let i = 0; i < NA && out.length < MAX; i++) if (SYM_L[i].includes(q)) add(i);
  if (q.length >= 3 && has(D.name)) for (let i = 0; i < NA && out.length < MAX; i++) if (D.name[i] && D.name[i].toLowerCase().includes(q)) add(i, "name");
  return out;
}
let acItems = [], acOn = 0;
const qi = $("q"), ac = $("ac");
function acRender() {
  if (!acItems.length) { ac.style.display = "none"; return; }
  ac.innerHTML = acItems.map((r, k) => "<div data-k='" + k + "' class='" + (k === acOn ? "on" : "") + "'>" +
    (r.via && r.via !== "name" ? "<span class='m'>" + esc(r.via) + " &rarr; </span>" : "") + "<b>" + esc(D.sym[r.i]) + "</b>" +
    (has(D.name) && D.name[r.i] ? " <span class='m'>" + esc(D.name[r.i]) + "</span>" : "") +
    (r.i >= N ? " <span class='m'>(not on the map)</span>" : "") + "</div>").join("");
  ac.style.display = "block";
}
qi.addEventListener("input", () => { acItems = search(qi.value); acOn = 0; acRender(); });
qi.addEventListener("keydown", e => {
  if (e.key === "ArrowDown" || e.key === "ArrowUp") {
    if (acItems.length) { acOn = (acOn + (e.key === "ArrowDown" ? 1 : acItems.length - 1)) % acItems.length; acRender(); }
    e.preventDefault();
  } else if (e.key === "Enter") {
    if (!acItems.length) acItems = search(qi.value);
    if (acItems.length) pick(acItems[acOn] ? acOn : 0);
    e.preventDefault();
  } else if (e.key === "Escape") { acItems = []; acRender(); qi.blur(); }
});
ac.addEventListener("mousedown", e => { const d = e.target.closest("[data-k]"); if (d) { pick(+d.dataset.k); e.preventDefault(); } });
qi.addEventListener("blur", () => setTimeout(() => { ac.style.display = "none"; }, 150));
qi.addEventListener("focus", () => qi.select());              // typing replaces the selected gene's symbol
function pick(k) {
  const r = acItems[k];
  if (!r) return;
  qi.value = D.sym[r.i]; acItems = []; acRender();
  select(r.i, true, "search");
}

// ---------------------------------------------------------------- help
const HOWTO_MAPS = "<div class='howto'><h3>How to read this</h3>" +
  "<p>Each dot is a gene. Its place comes from how it responds to about 1,100 drug-doses (379 drugs &times; 3 doses, 24 h) in each of 50 cancer cell lines (Tahoe-100M): two genes that rise and fall under the same treatments in the same lines are related.</p>" +
  "<h4>Nodal map</h4><p>Genes that respond to the <b>same</b> drugs sit together, <b>whether they move in the same direction or in opposite directions</b>. A pathway whose activated genes go up while the genes it represses go down forms one island. That island is a <b>module</b>. When its two sides move opposite (mean cos between them &le; &minus;0.2, &ge; 5 genes on each side) they are the module's <b>+ arm</b> and <b>&minus; arm</b> (colour by arm to see them); otherwise the module is single-armed and all its genes are +.</p>" +
  "<h4>Signed vector map</h4><p>The same genes, but now genes that move in <b>opposite</b> directions are pushed <b>apart</b>: only genes that go up and down together stay close. An island of the nodal map that splits in two here has two opposite arms. Switching between the two map tabs animates each gene from one place to the other.</p>" +
  "<h4>Distances</h4><p>Both maps keep each gene's near neighbours faithfully; the distance between two far-apart islands means little.</p>" +
  "<h4>A selected gene</h4><ul><li><b style='color:" + WITH + "'>Green lines</b>: genes that move <b>with</b> it; <b style='color:" + OPP + "'>red lines</b>: genes that move <b>opposite</b> to it.</li>" +
  "<li><b>cos</b>: similarity of the two genes' responses across every drug-dose &times; cell line, from +1 (always together) to &minus;1 (always opposite).</li>" +
  "<li><b>halves</b>: the compounds were split at random into two halves (a hash of the compound name) and the space fitted on each; <i>both</i> = the same sign in both halves with fdr &le; 0.10; <i>one</i> = strong in one of the two random halves only: not replicated, no error estimate; <i>none</i> = neither. <b>fdr</b>: the estimated share of false relations among pairs at least this strong in both halves.</li>" +
  "<li><b>same locus</b> / <b>read-through risk</b>: neighbouring genes can correlate for genomic reasons. <b>known</b>: shared pathway, gene family or STRING interaction; <b>novel?</b>: a strong relation seen in both halves (fdr &le; 0.05) and not found in those references; shown only when the references needed to rule out known links loaded.</li>" +
  "<li><b>Drug-doses</b>: fold change and z of the gene, pooled over the cell lines (median: a response in fewer than about half of the lines does not show here), against the same line's typical treated well on the plate (not DMSO); only drug-doses free of technical artifacts. <b>lines</b> = number of cell lines moving the same way.</li>" +
  "<li><b>Cell lines</b>: where the gene responds most: how many clean drug-doses raise (&uarr;) or lower (&darr;) it at least 1.5&times; in that line at the per-line |z| cut calibrated on this run, and the strongest one. Lines that do not express the gene, or read only ambient RNA for it, are not measured.</li></ul>" +
  "<h4>Using the map</h4><p>Drag to pan, scroll or pinch to zoom, double-click to zoom in, click a gene to select it (Esc clears), click a module in the legend to highlight it. Search finds symbols, aliases, previous symbols and names; genes that are not on the map (too few responses) still open their drug and cell-line tables. A link ending in <code>#SYMBOL</code> opens that gene. The selected gene is the same on every tab.</p></div>";
const KTXT = D.k_edges ? "each gene's " + D.k_edges + " strongest replicated partners" : "each gene's strongest replicated partners";
const HOWTO_PHYS = "<div class='howto'><h3>The tabs</h3><ul>" +
  "<li><b>Nodal map</b>: the t-SNE layout of 1 &minus; |cos|: opposite genes together.</li>" +
  "<li><b>Signed vector map</b>: the t-SNE layout of 1 &minus; cos: opposite genes apart.</li>" +
  "<li><b>Physics: neighbourhood</b>: a live force simulation of the selected gene, its partners and (depth 2) their partners.</li>" +
  "<li><b>Physics: module</b>: a live force simulation of one module, all its genes and the edges among them.</li>" +
  "<li><b>Physics: all genes</b>: a live force simulation of every gene on the map, started from the nodal-map positions.</li></ul>" +
  "<p>The side panel and the search box belong to every tab: a gene selected on one tab is selected on all of them.</p>" +
  "<h4>What moves the genes in the physics tabs</h4><p>One simulation engine runs all three. Every relation is a <b>spring</b>: it pulls in proportion to |cos| &times; (distance &minus; rest length), and a stronger relation has a shorter rest length. <b>Every pair of genes repels</b> (like charges: force &prop; 1/distance; computed with a Barnes-Hut quadtree, &theta; = 0.8, so 15,000 genes stay interactive). A weak pull holds everything near the centre, and friction slows the genes. The motion cools down (alpha) until the layout settles; any change re-heats it.</p>" +
  "<p>A force layout is a picture of the graph, not a measurement: which genes hold together means a lot, where two groups end up relative to each other means little, and a Reset may land the groups in other places.</p>" +
  "<h4>The sign switch</h4><p><b>Opposite genes attract</b> (the default): red relations (genes that move opposite) are springs like green ones, so a gene and the genes that move opposite to it gather into one cluster: the nodal view, where both arms of a pathway form one island. <b>Opposite genes repel</b>: red relations push their two genes apart (drawn dashed; they push up to six rest lengths and do not pull beyond), so a module's &minus; arm separates from its + arm: the signed view. Flipping the switch re-heats the simulation so you can watch the arms part.</p>" +
  "<h4>Colours</h4><ul><li>Edges: <b style='color:" + WITH + "'>green</b> = the two genes move together, <b style='color:" + OPP + "'>red</b> = they move opposite; thickness &prop; |cos|.</li>" +
  "<li>Genes: by module (the legend's colours) or by arm (<b style='color:" + ARMC["+"] + "'>+ arm</b>, <b style='color:" + ARMC["-"] + "'>&minus; arm</b>, grey = no module). A dark ring = the selected gene; a grey ring = a pinned gene; grey dots in the module tab = genes outside the module.</li></ul>" +
  "<h4>Neighbourhood</h4><p>The selected gene (pinned at the start), its partners (depth 1) and their partners (depth 2), strongest first, at most <i>Max genes</i> (default 300). The springs are the genes' top partners from the relations table (the lists in the side panel) that pass <i>Min |cos|</i> and <i>Evidence</i>. Click another gene to move the neighbourhood to it; the genes already there keep their places.</p>" +
  "<h4>Module</h4><p>One module: pick it from the list, use <i>Selected gene's module</i>, click <i>simulate</i> on a module card in the side panel, or click a module in the map legend. Its springs are the edges of the kNN graph that defines the modules (" + KTXT + ", |cos| &ge; 0.3), among the module's genes. Coloured by arm by default; <i>outside genes (1 hop)</i> adds, dimmed, the genes outside the module that its genes link to.</p>" +
  "<h4>All genes</h4><p>Every gene on the map, starting from its place on the nodal map, with every kNN-graph edge as a spring. Edges are drawn for the selected gene only (while the layout moves, 177,000 lines would hide everything). Each frame runs as many simulation steps as fit in about 13 ms, so the page stays responsive at any size; the status line shows frames per second.</p>" +
  "<h4>Controls</h4><ul><li><b>Drag a gene</b> to move it: its partners follow. <b>Double-click</b> a gene to pin or unpin it. <b>Click</b> a gene to select it. Drag the background to pan; wheel or pinch to zoom.</li>" +
  "<li><b>Pause / Resume</b> (space bar), <b>Re-heat</b> (let it move again), <b>Reset</b> (start the layout again and unpin everything), <b>Fit</b> (show every gene).</li>" +
  "<li><b>Repulsion</b> and <b>Springs</b>: the strengths of the two forces. <b>Min |cos|</b>: weaker relations are not springs. <b>Evidence</b>: only relations replicated in both random halves of the compounds, or also those strong in one half.</li>" +
  "<li>Labels: the selected gene, its springs' partners and pinned genes; everyone when zoomed in (labels that would overlap are left out).</li></ul></div>";
$("helptext").innerHTML = HOWTO_PHYS + HOWTO_MAPS;

// ---------------------------------------------------------------- tabs, status, keys, start
const TABS = ["nodal", "signed", "nbr", "mod", "all", "help"];
const PANE = {nodal: "map", signed: "map", nbr: "nbr", mod: "mod", all: "all", help: "help"};
function showTab(t) {
  if (!TABS.includes(t)) return;
  active = t;
  for (const b of document.querySelectorAll("#tabs [data-tab]")) b.setAttribute("aria-selected", b.dataset.tab === t);
  for (const p of ["map", "nbr", "mod", "all", "help"]) $("pane-" + p).classList.toggle("on", PANE[t] === p);
  hideTip();
  if (isMap(t)) {
    resize();
    const l = t === "nodal" ? 0 : 1;
    if (l !== layout || anim) setLayout(l);
    else if (mapSelPending && sel >= 0 && sel < N) { centreOn(sel, layout); mapSelPending = false; }
    status();
  } else if (PHYS[t]) PHYS[t].show();
  req();
}
for (const b of document.querySelectorAll("#tabs [data-tab]")) b.addEventListener("click", () => showTab(b.dataset.tab));
function status() {
  const nm = D.mods.length, s = [(N).toLocaleString() + " genes on the map", (NA - N).toLocaleString() + " more searchable",
    nm + " modules", layout === 0 ? "nodal map" : "signed vector map"];
  if (hlMod >= 0) s.push("module " + hlMod + " highlighted");
  s.push("drag = pan, wheel = zoom, click = select, Esc = clear");
  $("status").textContent = s.join("  ·  ");
  $("mapnote").textContent = layout === 0 ? "distance = 1 − |cos|: genes that move opposite sit together" : "distance = 1 − cos: genes that move opposite sit apart";
}
$("c0").addEventListener("click", () => setColour(0));
$("c1").addEventListener("click", () => setColour(1));
$("fitb").addEventListener("click", () => fit(false));
$("lgx").addEventListener("click", () => { const l = $("legend"); l.classList.toggle("closed"); $("lgx").innerHTML = l.classList.contains("closed") ? "+" : "&#8722;"; });
document.addEventListener("keydown", e => {
  if (e.target === qi) return;
  const tag = e.target && e.target.tagName;
  if (e.key === "Escape") { if (sel >= 0) select(-1, false, "key"); else if (hlMod >= 0) highlight(-1); }
  else if (e.key === "/") { qi.focus(); e.preventDefault(); }
  else if (e.key === " " && PHYS[active] && !/^(INPUT|SELECT|BUTTON|TEXTAREA)$/.test(tag)) { PHYS[active].togglePause(); e.preventDefault(); }
});
new ResizeObserver(resize).observe(wrap);
window.addEventListener("hashchange", fromHash);
function fromHash() {
  const h = decodeURIComponent((location.hash || "").slice(1)).trim().toLowerCase();
  if (!h) return;
  let i = SYM_L.indexOf(h);
  if (i < 0) { const r = search(h); if (r.length && (SYM_L[r[0].i] === h || (r[0].via && r[0].via.toLowerCase() === h))) i = r[0].i; }
  if (i >= 0 && i !== sel) select(i, true, "hash");
}
for (const k of ["nbr", "mod", "all"]) PHYS[k] = PhysPane(k);
buildLegend(); resize(); setColour(0); renderPanel(); status(); fromHash();
window.TAHOE_MAP = {select: i => select(i, true, "api"), search: search, data: D, tab: showTab,
  bench: n => { const t0 = performance.now(); for (let r = 0; r < n; r++) mapDraw(); return (performance.now() - t0) / n; },
  state: () => ({layout: layout, sel: sel, hlMod: hlMod, colourMode: colourMode, k: V.k / K0, tab: active}),
  sim: key => PHYS[key] ? PHYS[key].state() : null,
  screen: (key, i) => PHYS[key] ? PHYS[key].screen(i) : null,
  stats: key => PHYS[key] ? PHYS[key].stats() : null,
  benchTick: (key, n) => PHYS[key] ? PHYS[key].benchTick(n) : null};
})();
</script>
</body>
</html>
"""
