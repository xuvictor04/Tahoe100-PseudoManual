"""html_map - the interactive gene map: one self-contained HTML file, OUT/map/gene_map.html.

No network, no external script or style: vanilla JavaScript on a <canvas>, with every number the page shows computed
here and embedded as one compact JSON block. Open the file in any current browser (also from a USB stick / offline).

What the page shows
    two views of the same genes (buttons): the NODAL map (graph x, y: genes that respond to the same drugs sit
    together whether they go up together or in opposite directions; the two arms of a pathway form one island) and
    the SIGNED vector map (graph xs, ys: genes that move in opposite directions are pushed apart). Switching animates
    every gene from one layout to the other. Pan (drag), zoom (wheel / pinch), hover (symbol, module and arm, name),
    colour by module (a fixed palette of 20 colours cycled, unassigned grey) or by arm (+ / -), a module legend
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

Inputs (read only): graph/nodes.parquet, graph/modules.parquet, graph/module_pooled_z.npy,
relations/gene_relations.parquet, relations/info.json, tables/{genes,drug_effects,line_effects,drugdoses,lines}.parquet,
tables/info.json, embed/genes.parquet, embed/info.json; optional: reference/annotations.parquet,
validation/module_labels.csv.

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
"""

import json
import os
import re
import time
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from .common import folder, log, stamp_stage

VERSION = 2
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
    log(f"  relations: {len(rel):,} partner rows for {int((np.diff(np.r_[-1, ea]) != 0).sum()):,} genes, "
        f"{len(pw):,} shared pathways")
    del rel

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
    }


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
            "modules": len(data["mods"]), "module_labels_from": data["labels_from"], "reference": data["ref"],
            "partners": partners, "drugs": drugs, "lines": lines, "minutes": round((time.time() - t0) / 60, 2)}
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
header{display:flex;align-items:center;gap:10px 14px;padding:7px 12px;border-bottom:1px solid var(--grid);background:var(--surface);flex-wrap:wrap}
header h1{font-size:15px;margin:0 6px 0 0;font-weight:600;white-space:nowrap}
.grp{display:flex;align-items:center;gap:6px;color:var(--ink2)}
.seg{display:inline-flex;border:1px solid var(--axis);border-radius:6px;overflow:hidden}
.seg button{border:0;background:transparent;padding:5px 10px;font:inherit;cursor:pointer;color:var(--ink2)}
.seg button+button{border-left:1px solid var(--axis)}
.seg button[aria-pressed="true"]{background:var(--ink);color:#fff}
.btn{border:1px solid var(--axis);background:transparent;border-radius:6px;padding:5px 10px;font:inherit;cursor:pointer;color:var(--ink2)}
.btn:hover,.seg button:hover{background:var(--hl);color:var(--ink)}
.seg button[aria-pressed="true"]:hover{background:var(--ink);color:#fff}
#sw{position:relative}
#q{width:230px;padding:5px 8px;border:1px solid var(--axis);border-radius:6px;font:inherit;background:#fff}
#q:focus{outline:2px solid var(--accent);outline-offset:-1px}
#ac{position:absolute;top:calc(100% + 3px);left:0;z-index:30;background:#fff;border:1px solid var(--axis);border-radius:6px;box-shadow:0 6px 18px rgba(0,0,0,.12);max-height:360px;overflow:auto;display:none;min-width:340px}
#ac div{padding:5px 9px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#ac div.on,#ac div:hover{background:var(--hl)}
#ac b{font-weight:600}
#ac .m{color:var(--muted)}
main{flex:1;display:flex;min-height:0}
#mapwrap{flex:1;position:relative;min-width:0;background:var(--surface)}
#cv{position:absolute;inset:0;width:100%;height:100%;display:block;cursor:grab;touch-action:none}
#cv.drag{cursor:grabbing}
#tip{position:absolute;pointer-events:none;background:#fff;border:1px solid var(--ring);border-radius:6px;padding:5px 8px;box-shadow:0 2px 10px rgba(0,0,0,.14);display:none;max-width:340px;z-index:5}
#tip b{font-size:13px}
#tip .m{color:var(--ink2)}
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
#status{position:absolute;left:10px;right:10px;bottom:6px;color:var(--muted);font-size:12px;pointer-events:none;text-align:right;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
aside{width:440px;flex:none;border-left:1px solid var(--grid);overflow:auto;background:var(--surface);padding:12px 16px 30px}
aside h2{font-size:20px;margin:0 0 2px}
aside h3{font-size:13px;margin:16px 0 5px;color:var(--ink);font-weight:600;border-bottom:1px solid var(--grid);padding-bottom:3px}
aside .nm{color:var(--ink2);font-size:14px}
aside .fn{color:var(--ink2);margin:6px 0}
aside .note{color:var(--muted);font-size:12px}
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
a,.lk{color:var(--accent);cursor:pointer;text-decoration:none}
a:hover,.lk:hover{text-decoration:underline}
.mcard{background:#f4f6f9;border:1px solid var(--grid);border-radius:8px;padding:8px 10px;margin:0 0 10px}
.mcard .row{margin:3px 0}
.mcard .lbl{color:var(--muted);font-size:12px}
#help{position:fixed;inset:0;background:rgba(0,0,0,.28);display:none;z-index:50;align-items:center;justify-content:center}
#help.open{display:flex}
#help .box{background:var(--surface);max-width:680px;max-height:85vh;overflow:auto;border-radius:10px;padding:18px 22px;box-shadow:0 10px 40px rgba(0,0,0,.25)}
.howto h4{margin:12px 0 3px;font-size:13px}
.howto p,.howto li{color:var(--ink2);margin:3px 0}
.howto ul{padding-left:18px;margin:4px 0}
</style>
</head>
<body>
<header>
  <h1>Tahoe-100M gene map</h1>
  <div class="grp">View <span class="seg" id="vseg"><button id="v0" aria-pressed="true" title="Distance = 1 - |cos|: genes that respond to the same drugs sit together, also when they move in opposite directions">Nodal map</button><button id="v1" aria-pressed="false" title="Distance = 1 - cos: genes that move in opposite directions are pushed apart">Signed vector map</button></span></div>
  <div class="grp">Colour <span class="seg"><button id="c0" aria-pressed="true">Module</button><button id="c1" aria-pressed="false">Arm (+ / &minus;)</button></span></div>
  <div class="grp" id="sw"><input id="q" type="search" placeholder="Search a gene (symbol, alias, name)" autocomplete="off" spellcheck="false" aria-label="Search a gene"><div id="ac" role="listbox"></div></div>
  <button class="btn" id="fitb" title="Show every gene">Reset view</button>
  <button class="btn" id="helpb">How to read this</button>
</header>
<main>
  <div id="mapwrap">
    <canvas id="cv"></canvas>
    <div id="legend"><div class="hd"><span id="lgtitle">Modules</span><button id="lgx" title="Collapse / expand">&#8722;</button></div><div id="armkey"></div><div id="lgbody"></div></div>
    <div id="tip"></div>
    <div id="status"></div>
  </div>
  <aside id="panel"></aside>
</main>
<div id="help"><div class="box"><div id="helptext"></div><p style="text-align:right;margin:14px 0 0"><button class="btn" id="helpx">Close</button></p></div></div>
<noscript><p style="padding:20px">This map needs JavaScript.</p></noscript>
<script id="tm-data" type="application/json">__DATA__</script>
<script>
"use strict";
(function () {
const D = JSON.parse(document.getElementById("tm-data").textContent);
const N = D.n, NA = D.sym.length, PAL = D.palette, GREY = "#bdbcb6";
const ARMC = {"+": "#eb6834", "-": "#2a78d6"};
const WITH = "#0ca30c", OPP = "#d03b3b", SURF = "#fcfcfb", INK = "#0b0b0b";
const EVS = ["none", "one", "both"];
const $ = id => document.getElementById(id);
const cv = $("cv"), ctx = cv.getContext("2d"), wrap = $("mapwrap"), tip = $("tip");
const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
const fmt = (v, d) => (v == null || !isFinite(v)) ? "" : v.toFixed(d);
const has = a => a && a.length > 0;
const MODS = new Map(D.mods.map(m => [m.id, m]));
const modColour = m => m > 0 ? PAL[(m - 1) % PAL.length] : GREY;

// ---------------------------------------------------------------- layouts, normalised to one box
function quant(sorted, q) { return sorted[Math.min(sorted.length - 1, Math.max(0, Math.round(q * (sorted.length - 1))))]; }
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

// ---------------------------------------------------------------- view (screen = world * k + t; y up)
let W = 1, H = 1, DPR = 1, K0 = 1;
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
  DPR = window.devicePixelRatio || 1;
  const first = W === 1 && H === 1;
  W = Math.max(1, r.width); H = Math.max(1, r.height);
  cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
  if (first) fit(true); else { const f = fitTarget(); K0 = f.k; }
  req();
}
const sx = i => PX[i] * V.k + V.tx, sy = i => -PY[i] * V.k + V.ty;

// ---------------------------------------------------------------- state
let colourMode = 0, hlMod = -1, sel = -1, hover = -1, groups = null, P = [], pset = new Set(), focus = "gene";
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
function colourOf(i) {
  if (colourMode === 1) return ARMC[D.arm[i]] || GREY;
  return modColour(D.mod[i]);
}
function rebuild() {
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

// ---------------------------------------------------------------- drawing
// Points are written straight into one pixel buffer (a single putImageData per frame): no canvas call per point,
// so 16k+ points stay fast also where the canvas is not GPU-accelerated. Lines, rings and labels go on top.
const LITTLE = new Uint8Array(new Uint32Array([1]).buffer)[0] === 1;
const pack = (r, g, b) => LITTLE ? (((255 << 24) | (b << 16) | (g << 8) | r) >>> 0) : (((r << 24) | (g << 16) | (b << 8) | 255) >>> 0);
const rgbOf = hex => { const v = parseInt(hex.slice(1), 16); return [(v >> 16) & 255, (v >> 8) & 255, v & 255]; };
const SURF_RGB = rgbOf(SURF), SURF_PACKED = pack(SURF_RGB[0], SURF_RGB[1], SURF_RGB[2]);
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
function drawPoints() {
  const Wd = cv.width, Hd = cv.height;
  if (!img || img.width !== Wd || img.height !== Hd) { img = ctx.createImageData(Wd, Hd); buf8 = img.data; buf32 = new Uint32Array(buf8.buffer); }
  buf32.fill(SURF_PACKED);
  if (groups) {
    const k = V.k * DPR, tx = V.tx * DPR, ty = V.ty * DPR, M = getMask(pointR() * DPR, Wd), e = M.e;
    const full = M.full, part = M.part, cov = M.cov, fdx = M.fdx, fdy = M.fdy, pdx = M.pdx, pdy = M.pdy;
    const nf = full.length, np = part.length;
    for (const g of groups) {
      const a = g.a * 0.92, rgb = rgbOf(g.c);
      const cr = rgb[0] * a + SURF_RGB[0] * (1 - a), cg = rgb[1] * a + SURF_RGB[1] * (1 - a), cb = rgb[2] * a + SURF_RGB[2] * (1 - a);
      const solid = pack(Math.round(cr), Math.round(cg), Math.round(cb)), idx = g.idx;
      for (let j = 0; j < idx.length; j++) {
        const i = idx[j], X = Math.round(PX[i] * k + tx), Y = Math.round(-PY[i] * k + ty);
        if (X < -e || Y < -e || X >= Wd + e || Y >= Hd + e) continue;
        if (X >= e && Y >= e && X < Wd - e && Y < Hd - e) {
          const base = Y * Wd + X;
          for (let t = 0; t < nf; t++) buf32[base + full[t]] = solid;
          for (let t = 0; t < np; t++) {
            const o = (base + part[t]) << 2, c = cov[t];
            buf8[o] += (cr - buf8[o]) * c; buf8[o + 1] += (cg - buf8[o + 1]) * c; buf8[o + 2] += (cb - buf8[o + 2]) * c;
          }
        } else {                                              // near the edge: clip pixel by pixel
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
}
const pointR = () => Math.min(5, Math.round(4 * 2 * Math.pow(V.k / K0, 0.3)) / 4);
let pending = false;
function req() { if (!pending) { pending = true; requestAnimationFrame(frame); } }
function ease(t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
function frame(now) {
  pending = false;
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
  draw();
  if (more) req();
}
function draw() {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  drawPoints();
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
function halo(text, x, y, font, colour) {
  ctx.font = font; ctx.lineJoin = "round"; ctx.lineWidth = 3.5; ctx.strokeStyle = "rgba(252,252,251,.92)";
  ctx.strokeText(text, x, y); ctx.fillStyle = colour || INK; ctx.fillText(text, x, y);
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
    if (text.length > 60) text = text.slice(0, 58) + "\u2026";
    halo(text, X, Y, "600 11px system-ui,-apple-system,sans-serif", selOn && hlMod !== m.id ? "#898781" : "#2b2b2a");
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
  const placed = [], F1 = "700 13px system-ui,-apple-system,sans-serif", F2 = "11px system-ui,-apple-system,sans-serif";
  const label = (text, x, y, font, colour, hgt) => {
    ctx.font = font;
    const w = ctx.measureText(text).width, b = [x - 1, y - hgt / 2, x + w + 1, y + hgt / 2];
    for (const q of placed) if (b[0] < q[2] && b[2] > q[0] && b[1] < q[3] && b[3] > q[1]) return;
    placed.push(b); halo(text, x, y, font, colour);
  };
  label(D.sym[sel], x0 + r + 7, y0, F1, INK, 15);
  for (const p of P) label(D.sym[p.j], sx(p.j) + r + 4, sy(p.j), F2, p.cos > 0 ? "#05600a" : "#8f1d1d", 12);
}

// ---------------------------------------------------------------- hit testing, pointer, wheel
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
function local(e) { const r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
cv.addEventListener("pointerdown", e => {
  cv.setPointerCapture(e.pointerId);
  ptrs.set(e.pointerId, local(e));
  dragged = false; downAt = local(e);
  if (ptrs.size === 2) { const [a, b] = [...ptrs.values()]; pinch = {d: Math.hypot(a[0] - b[0], a[1] - b[1]), k: T.k}; }
  cv.classList.add("drag");
});
cv.addEventListener("pointermove", e => {
  const p = local(e);
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
  const p = local(e), wasDrag = dragged;
  endPtr(e);
  if (!wasDrag && e.button === 0) { const h = nearest(p[0], p[1]); if (h >= 0) select(h, false); else if (sel >= 0) select(-1); }
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
  const [mx, my] = local(e), dy = e.deltaMode === 1 ? e.deltaY * 33 : e.deltaY;
  zoomAt(mx, my, Math.exp(-dy * 0.0016), false);
  hideTip();
}, {passive: false});
cv.addEventListener("dblclick", e => { const [mx, my] = local(e); zoomAt(mx, my, 2, false); });

function showTip(i, mx, my) {
  const m = D.mod[i], arm = D.arm[i], mod = MODS.get(m);
  let h = "<b>" + esc(D.sym[i]) + "</b>";
  if (has(D.name) && D.name[i]) h += " <span class='m'>" + esc(D.name[i]) + "</span>";
  h += "<br><span class='k' style='background:" + modColour(m) + "'></span>" +
       (m > 0 ? "Module " + m + (arm !== "." && mod && mod.opp ? ", arm " + (arm === "-" ? "&minus;" : "+") : "") + (mod ? " <span class='m'>" + esc(mod.label) + "</span>" : "") : "<span class='m'>no module</span>");
  tip.innerHTML = h; tip.style.display = "block";
  const tw = tip.offsetWidth, th = tip.offsetHeight;
  let x = mx + 14, y = my + 14;
  if (x + tw > W - 4) x = mx - tw - 12;
  if (y + th > H - 4) y = my - th - 12;
  tip.style.left = Math.max(2, x) + "px"; tip.style.top = Math.max(2, y) + "px";
}
function hideTip() { tip.style.display = "none"; }

// ---------------------------------------------------------------- views, colours, legend
function setLayout(l) {
  if (l === layout && !anim) return;
  anim = {from: layout, to: l, t0: performance.now(), dur: 750};
  // start from the current (possibly mid-animation) positions
  LAY[2] = {x: Float32Array.from(PX), y: Float32Array.from(PY)}; anim.from = 2;
  layout = l;
  $("v0").setAttribute("aria-pressed", l === 0); $("v1").setAttribute("aria-pressed", l === 1);
  if (sel >= 0 && sel < N) centreOn(sel, l);     // follow the selected gene and its partners to the new layout
  status(); req();
}
function setColour(c) {
  colourMode = c;
  $("c0").setAttribute("aria-pressed", c === 0); $("c1").setAttribute("aria-pressed", c === 1);
  const ak = $("armkey");
  ak.style.display = c === 1 ? "block" : "none";
  rebuild();
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
  rebuild(); renderPanel(); status();
}

// ---------------------------------------------------------------- selection and the side panel
function centreOn(i, l) {
  // zoom so that the gene and its partners fill the free part of the canvas, centred on the gene
  const lw = W > 700 ? legendW() : 0, w = W - lw, X = LAY[l].x, Y = LAY[l].y;
  let far = 0;
  for (const p of P) far = Math.max(far, Math.abs(X[p.j] - X[i]), Math.abs(Y[p.j] - Y[i]));
  const k = far > 0 ? Math.min(K0 * 40, Math.max(K0 * 1.2, 0.42 * Math.min(w, H) / far)) : Math.max(T.k, K0 * 4);
  T.k = k; T.tx = lw + w / 2 - X[i] * k; T.ty = H / 2 + Y[i] * k;
}
function select(i, centre) {
  sel = i; focus = "gene";
  P = partnersOf(i); pset = new Set(P.map(p => p.j));
  if (i >= 0) qi.value = D.sym[i];
  if (i >= 0 && i < N && centre) centreOn(i, layout);
  if (i < 0) qi.value = "";
  try { history.replaceState(null, "", i >= 0 ? "#" + encodeURIComponent(D.sym[i]) : location.pathname + location.search); } catch (err) { /* file:// in some browsers */ }
  rebuild(); renderPanel(); status();
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
    "<div class='row'><b>" + esc(md.label) + "</b></div>" +
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
function partnerTable() {
  if (!P.length) return "<p class='note'>No partners recorded.</p>";
  let h = "<table class='pt'><tr><th>Gene</th><th class='r' title='signed cosine: +1 = same direction, -1 = opposite'>cos</th><th title='both = same sign with fdr &le; 0.10 in two random halves of the compounds; one = strong in one random half only (not replicated, no error estimate); none = neither'>halves</th><th class='r' title='estimated share of false relations among pairs at least this strong in both halves'>fdr</th><th>flags</th></tr>";
  for (const p of P) {
    let f = "";
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
  if (!h) h = "<p class='note'>Click a gene on the map or search for one.</p>" + HOWTO;
  $("panel").innerHTML = h;
  $("panel").scrollTop = 0;
}
$("panel").addEventListener("click", e => {
  const g = e.target.closest("[data-g]"), m = e.target.closest("[data-hl]"), hp = e.target.closest("[data-help]");
  if (g) select(+g.dataset.g, true);
  else if (m) highlight(+m.dataset.hl === hlMod ? -1 : +m.dataset.hl);
  else if (hp) $("help").classList.add("open");
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
  select(r.i, true);
}

// ---------------------------------------------------------------- help, status, keys, start
const HOWTO = "<div class='howto'><h3>How to read this</h3>" +
  "<p>Each dot is a gene. Its place comes from how it responds to about 1,100 drug-doses (379 drugs &times; 3 doses, 24 h) in each of 50 cancer cell lines (Tahoe-100M): two genes that rise and fall under the same treatments in the same lines are related.</p>" +
  "<h4>Nodal map</h4><p>Genes that respond to the <b>same</b> drugs sit together, <b>whether they move in the same direction or in opposite directions</b>. A pathway whose activated genes go up while the genes it represses go down forms one island. That island is a <b>module</b>. When its two sides move opposite (mean cos between them &le; &minus;0.2, &ge; 5 genes on each side) they are the module's <b>+ arm</b> and <b>&minus; arm</b> (colour by arm to see them); otherwise the module is single-armed and all its genes are +.</p>" +
  "<h4>Signed vector map</h4><p>The same genes, but now genes that move in <b>opposite</b> directions are pushed <b>apart</b>: only genes that go up and down together stay close. An island of the nodal map that splits in two here has two opposite arms. Switching between the maps animates each gene from one place to the other.</p>" +
  "<h4>Distances</h4><p>Both maps keep each gene's near neighbours faithfully; the distance between two far-apart islands means little.</p>" +
  "<h4>A selected gene</h4><ul><li><b style='color:" + WITH + "'>Green lines</b>: genes that move <b>with</b> it; <b style='color:" + OPP + "'>red lines</b>: genes that move <b>opposite</b> to it.</li>" +
  "<li><b>cos</b>: similarity of the two genes' responses across every drug-dose &times; cell line, from +1 (always together) to &minus;1 (always opposite).</li>" +
  "<li><b>halves</b>: the compounds were split at random into two halves (a hash of the compound name) and the space fitted on each; <i>both</i> = the same sign in both halves with fdr &le; 0.10; <i>one</i> = strong in one of the two random halves only: not replicated, no error estimate; <i>none</i> = neither. <b>fdr</b>: the estimated share of false relations among pairs at least this strong in both halves.</li>" +
  "<li><b>same locus</b> / <b>read-through risk</b>: neighbouring genes can correlate for genomic reasons. <b>known</b>: shared pathway, gene family or STRING interaction; <b>novel?</b>: a strong relation seen in both halves (fdr &le; 0.05) and not found in those references; shown only when the references needed to rule out known links loaded.</li>" +
  "<li><b>Drug-doses</b>: fold change and z of the gene, pooled over the cell lines (median: a response in fewer than about half of the lines does not show here), against the same line's typical treated well on the plate (not DMSO); only drug-doses free of technical artifacts. <b>lines</b> = number of cell lines moving the same way.</li>" +
  "<li><b>Cell lines</b>: where the gene responds most: how many clean drug-doses raise (&uarr;) or lower (&darr;) it at least 1.5&times; in that line at the per-line |z| cut calibrated on this run, and the strongest one. Lines that do not express the gene, or read only ambient RNA for it, are not measured.</li></ul>" +
  "<h4>Using the map</h4><p>Drag to pan, scroll or pinch to zoom, double-click to zoom in, click a gene to select it (Esc clears), click a module in the legend to highlight it. Search finds symbols, aliases, previous symbols and names; genes that are not on the map (too few responses) still open their drug and cell-line tables. A link ending in <code>#SYMBOL</code> opens that gene.</p></div>";
$("helptext").innerHTML = HOWTO;
$("helpb").addEventListener("click", () => $("help").classList.add("open"));
$("helpx").addEventListener("click", () => $("help").classList.remove("open"));
$("help").addEventListener("click", e => { if (e.target === $("help")) $("help").classList.remove("open"); });
function status() {
  const nm = D.mods.length, s = [(N).toLocaleString() + " genes on the map", (NA - N).toLocaleString() + " more searchable",
    nm + " modules", layout === 0 ? "nodal map" : "signed vector map"];
  if (hlMod >= 0) s.push("module " + hlMod + " highlighted");
  s.push("drag = pan, wheel = zoom, click = select, Esc = clear");
  $("status").textContent = s.join("  ·  ");
}
$("v0").addEventListener("click", () => setLayout(0));
$("v1").addEventListener("click", () => setLayout(1));
$("c0").addEventListener("click", () => setColour(0));
$("c1").addEventListener("click", () => setColour(1));
$("fitb").addEventListener("click", () => fit(false));
$("lgx").addEventListener("click", () => { const l = $("legend"); l.classList.toggle("closed"); $("lgx").innerHTML = l.classList.contains("closed") ? "+" : "&#8722;"; });
document.addEventListener("keydown", e => {
  if (e.target === qi) return;
  if (e.key === "Escape") { if ($("help").classList.contains("open")) $("help").classList.remove("open"); else if (sel >= 0) select(-1); else if (hlMod >= 0) highlight(-1); }
  else if (e.key === "/") { qi.focus(); e.preventDefault(); }
});
new ResizeObserver(resize).observe(wrap);
window.addEventListener("hashchange", fromHash);
function fromHash() {
  const h = decodeURIComponent((location.hash || "").slice(1)).trim().toLowerCase();
  if (!h) return;
  let i = SYM_L.indexOf(h);
  if (i < 0) { const r = search(h); if (r.length && (SYM_L[r[0].i] === h || (r[0].via && r[0].via.toLowerCase() === h))) i = r[0].i; }
  if (i >= 0 && i !== sel) select(i, true);
}
buildLegend(); resize(); setColour(0); renderPanel(); status(); fromHash();
window.TAHOE_MAP = {select: i => select(i, true), search: search, data: D,
  bench: n => { const t0 = performance.now(); for (let r = 0; r < n; r++) draw(); return (performance.now() - t0) / n; }, state: () => ({layout: layout, sel: sel, hlMod: hlMod, colourMode: colourMode, k: V.k / K0})};
})();
</script>
</body>
</html>
"""
