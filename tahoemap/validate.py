"""validate - does the vector space / nodal map recover known biology, and what in it is new?

Every test runs on the genes in the vector space (embed/included_cols.npy); cos = signed cosine of their unit vectors
(embed/gene_unit.npy), i.e. the correlation of two genes' denoised response profiles over (drug-dose, line) contexts.

  gene sets        the curated control sets of tahoemap/data/control_sets.json (literature programmes, no network),
                   plus MSigDB Hallmark and Reactome sets (reference/gene_sets.parquet) with >= 5 genes in the space.
                   Per set: mean within-set cos; AUROC of the within-set pairs against 20,000 random pairs of genes in
                   the space, on cos and on |cos| (Mann-Whitney: P(set pair > random pair), ties count 1/2; 0.5 = no
                   better than random); an empirical p of that AUROC against random gene sets of the same size
                   (control, Hallmark and synthetic sets); the share of members in the set's most common module of
                   the nodal map; the drug-doses that raise / lower the set most (mean pooled DD_z over members).
  opposite pairs   programmes expected to move in opposite directions (control_sets.json 'opposite_pairs'): mean
                   cross-set cos (expect < 0), share of cross pairs with cos < 0, share of cross pairs in the same
                   module (expect high: the nodal map is built on |cos|), and the distance between the two sets'
                   centroids on the nodal map (x, y) and on the signed map (xs, ys), each divided by that map's spread
                   (sqrt(var x + var y)). Opposite genes should sit far apart in the signed space and together on the
                   nodal map.
  module labels    every module, and each of its arms, against every set: hypergeometric upper tail (universe =
                   genes in the space), Benjamini-Hochberg over all tests. Label = the best set (smallest p among
                   sets of <= 300 genes, else any) with q < 0.05 and >= 3 shared genes, else the module's top genes.
  drug check       AUROC of drug-vector cos (embed/drug_vectors.npy) for drug pairs sharing moa_fine against pairs
                   with different moa_fine (drugs with a known mechanism only: 'unclear' / 'unknown' left out; two
                   salt forms of one compound are never paired).
  novel            (a) relations' novel_candidate pairs (reproduced in both compound halves, fdr <= 0.05, |cos| >= 0.5,
                   no shared gene group / pathway / STRING link, not the same locus, no read-through risk), one row
                   per unordered pair; (b) guilt by association: members of a module arm enriched for a set
                   (q < 0.01; sets of <= 300 genes) that the set does not list, with mean cos >= 0.5 to the arm's
                   listed members.
  synthetic truth  only with truth=<ground_truth.json of tests/make_synthetic_tahoe.py>: the generator's planted gene
                   sets and opposite pairs, with the same metrics.

Outputs in OUT/validation/ (README.md there documents every column):
    report.md, metrics.json, control_sets.csv (every tested set, all sources), opposite_pairs.csv,
    module_enrichment.csv, module_labels.csv, drug_moa.csv, novel_edges.csv, novel_members.csv
"""

import json
import os
import re
import time
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import tlib as T
from .common import folder, log, read_effects_index, stable_seed, stamp_stage, write_csv, write_json

VERSION = 1
N_RANDOM = 20_000           # random gene pairs: the background of every AUROC
N_NULL = 200                # random gene sets per set size for the empirical p of a set's AUROC
NULL_SOURCES = ("control", "hallmark", "synthetic")
NULL_POOL = 4000            # random sets are drawn from this many random genes (their cosines held in memory: 64 MB)
MIN_SET = 5                 # Hallmark / Reactome sets need this many genes in the space (enrichment: every source)
LABEL_Q = 0.05
LABEL_MIN_OVERLAP = 3
LABEL_MAX_SET = 300         # labels prefer specific sets (as relations' PATHWAY_MAX); guilt by association uses only these
GBA_Q = 0.01
GBA_COS = 0.5
GBA_MIN_ANNOT = 3
GBA_PER_GENE = 5            # novel_members.csv keeps each gene's 5 most significant sets
OPP_COS = -0.1              # 'opposite': mean cross-set cos <= this
TOGETHER = 0.5              # 'together on the nodal map': centroid distance <= this many spreads and < half the signed
ENRICH_KEEP_P = 0.05        # module_enrichment.csv keeps tests with overlap >= 2 and p <= this
TOP_DD = 5
UNTRUSTED = ("unreliable plate only", "position not correctable", "wells disagree")
NO_MOA = {"", "nan", "none", "unclear", "unknown"}
CONTROL_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "control_sets.json")
SYNTH_OPPOSITE = [("HDAC_UP", "HDAC_DOWN"), ("COLOC_UP", "COLOC_DOWN"), ("COLOC2_UP", "COLOC2_DOWN")]
SOURCES_ORDER = {"control": 0, "synthetic": 1, "hallmark": 2, "reactome": 3}


# ----------------------------------------------------------------------------- small helpers
def _auroc(pos, neg_sorted):
    """P(pos > neg) + 1/2 P(pos == neg): the Mann-Whitney AUROC, rank-based, numpy only (neg sorted ascending)."""
    pos = np.asarray(pos, dtype=np.float64)
    pos = np.sort(pos[np.isfinite(pos)])                 # sorted needles: searchsorted is several times faster
    if not len(pos) or not len(neg_sorted):
        return np.nan
    lo = np.searchsorted(neg_sorted, pos, side="left")
    hi = np.searchsorted(neg_sorted, pos, side="right")
    return float((lo.sum() + 0.5 * (hi - lo).sum()) / (len(pos) * len(neg_sorted)))


def _bh(p):
    p = np.asarray(p, dtype=np.float64)
    n = p.size
    if not n:
        return p.copy()
    o = np.argsort(p, kind="mergesort")
    r = p[o] * n / np.arange(1, n + 1)
    r = np.minimum.accumulate(r[::-1])[::-1]
    q = np.empty(n)
    q[o] = np.minimum(r, 1.0)
    return q


_TOKENS = {"P53": "p53", "TP53": "TP53", "G2M": "G2/M", "G1S": "G1/S", "MTORC1": "mTORC1", "MTOR": "mTOR",
           "TNFA": "TNF-alpha", "NFKB": "NF-kB", "DN": "down", "WNT": "Wnt", "NOTCH": "Notch", "V1": "v1",
           "V2": "v2", "ER": "ER", "UP": "up", "DOWN": "down"}
_UPPER = {"E2F", "MYC", "KRAS", "IL2", "IL6", "STAT5", "STAT3", "JAK", "PI3K", "AKT", "TGF", "UV", "DNA", "RNA",
          "DREAM", "UPR", "ISR", "ATF4", "NRF2", "MAPK", "AHR", "SREBP1", "HDAC", "RIBI", "COLOC", "COLOC2", "GR"}


def short_name(name, source=""):
    """'HALLMARK_P53_PATHWAY' -> 'p53 pathway', 'DREAM_G2M_DOWN' -> 'DREAM G2/M down'; Reactome names unchanged."""
    s = str(name)
    if source == "reactome" or "_" not in s and " " in s:
        return s
    s = re.sub(r"^HALLMARK_", "", s)
    words = []
    for t in s.split("_"):
        if t in _TOKENS:
            words.append(_TOKENS[t])
        elif t in _UPPER or (re.search(r"\d", t) and len(t) <= 6):
            words.append(t)
        else:
            words.append(t.lower())
    return " ".join(w for w in words if w)


def _f(x, fmt="{:.2f}", na="-"):
    try:
        if x is None or not np.isfinite(float(x)):
            return na
    except (TypeError, ValueError):
        return str(x)
    return fmt.format(float(x))


def _pct(x):
    return _f(x, "{:.1%}" if np.isfinite(x) and 0 < abs(x) < 0.1 else "{:.0%}")


def _cell(v):
    return str(v).replace("|", "/").replace("\n", " ")


def _md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(_cell(v) for v in r) + " |" for r in rows]
    return "\n".join(out)


def _p_fmt(p):
    if p is None or not np.isfinite(p):
        return "-"
    return f"{p:.1e}" if p < 1e-3 else f"{p:.3f}"


# ----------------------------------------------------------------------------- gene names -> cols
def _name_index(eg, ann, included):
    """Upper-cased name -> one gene col. Precedence (as the reference stage): HGNC approved symbol, Tahoe symbol,
    a previous symbol of exactly one gene. A name on several cols -> the first included col (else the first col)."""
    def choose(cs):
        cs = sorted(set(cs))
        inc = [c for c in cs if included[c]]
        return (inc or cs)[0]

    layers = []
    if ann is not None and "hgnc_symbol" in ann:
        hs = ann["hgnc_symbol"].fillna("").astype(str).to_numpy()
        layers.append(([(h, c) for c, h in enumerate(hs) if h], False))
    layers.append(([(s, c) for c, s in enumerate(eg["symbol"].fillna("").astype(str)) if s], False))
    if ann is not None and "prev_symbols" in ann:
        pv = ann["prev_symbols"].fillna("").astype(str).to_numpy()
        layers.append(([(p_.strip(), c) for c, s in enumerate(pv) if s for p_ in s.split("|") if p_.strip()], True))
    lookup = {}
    for pairs, unique_only in layers:
        tmp = {}
        for name, c in pairs:
            tmp.setdefault(name.upper(), []).append(int(c))
        for name, cs in tmp.items():
            if name in lookup or (unique_only and len(set(cs)) > 1):
                continue
            lookup[name] = choose(cs)
    return lookup


# ----------------------------------------------------------------------------- gene sets
def _collect_sets(out, eg, ann, included, lookup, truth):
    """[{key, source, set, label, note, n_listed, n_found, cols (included gene cols), names (listed, upper)}]"""
    sets, opposite = [], []
    with open(CONTROL_JSON, encoding="utf-8") as fh:
        cj = json.load(fh)
    for name, d in cj.get("sets", {}).items():
        genes = [str(g) for g in d.get("genes", [])]
        found = sorted({lookup[g.upper()] for g in genes if g.upper() in lookup})
        sets.append({"key": f"control:{name}", "source": "control", "set": name, "label": short_name(name),
                     "note": d.get("note", ""), "n_listed": len(genes), "n_found": len(found),
                     "cols": np.array([c for c in found if included[c]], dtype=np.int64),
                     "names": {g.upper() for g in genes}})
    for p in cj.get("opposite_pairs", []):
        opposite.append({"source": "control", "a": p["a"], "b": p["b"], "note": p.get("note", "")})

    gp = os.path.join(out, "reference", "gene_sets.parquet")
    n_ref = 0
    if os.path.exists(gp):
        gs = pd.read_parquet(gp)
        gs = gs[gs["source"].isin(["hallmark", "reactome"])].dropna(subset=["col"])
        gs = gs.assign(col=gs["col"].astype(np.int64), symbol=gs["symbol"].fillna("").astype(str))
        size = gs["set_size"] if "set_size" in gs else pd.Series(np.nan, index=gs.index)
        gs = gs.assign(set_size=size)
        for (src, name), g in gs.groupby(["source", "set"], sort=True):
            cols = np.unique(g["col"].to_numpy())
            cols = cols[(cols >= 0) & (cols < len(included))]
            inc = cols[included[cols]]
            if len(inc) < MIN_SET:
                continue
            n_ref += 1
            sets.append({"key": f"{src}:{name}", "source": src, "set": str(name), "label": short_name(name, src),
                         "note": "", "n_listed": int(np.nanmax(g["set_size"])) if g["set_size"].notna().any()
                         else len(cols), "n_found": int(len(cols)), "cols": inc.astype(np.int64),
                         "names": set(g["symbol"].str.upper())})
    log(f"  gene sets: {sum(s['source'] == 'control' for s in sets)} control, {n_ref} Hallmark / Reactome "
        f"with >= {MIN_SET} genes in the space" + ("" if os.path.exists(gp) else " (no reference stage)"))

    if truth:
        with open(truth, encoding="utf-8") as fh:
            gt = json.load(fh)
        syn = gt.get("extra_not_in_panel_spec", {}).get("synthetic gene sets", {}) or {}
        for name, genes in syn.items():
            genes = [str(g) for g in genes]
            found = sorted({lookup[g.upper()] for g in genes if g.upper() in lookup})
            sets.append({"key": f"synthetic:{name}", "source": "synthetic", "set": name, "label": short_name(name),
                         "note": "planted by the synthetic generator", "n_listed": len(genes),
                         "n_found": len(found), "cols": np.array([c for c in found if included[c]], dtype=np.int64),
                         "names": {g.upper() for g in genes}})
        for a, b in SYNTH_OPPOSITE:
            if a in syn and b in syn:
                opposite.append({"source": "synthetic", "a": a, "b": b, "note": "planted opposite arms"})
        log(f"  synthetic truth: {len(syn)} planted sets from {truth}")
    return sets, opposite


# ----------------------------------------------------------------------------- per-set metrics
class _Space:
    """The genes in the space, their unit vectors (full and halves), modules, arms and map coordinates."""

    def __init__(self, out, n_random=N_RANDOM):
        ed = os.path.join(out, "embed")
        self.inc = np.load(os.path.join(ed, "included_cols.npy")).astype(np.int64)
        self.eg = pd.read_parquet(os.path.join(ed, "genes.parquet"))
        self.gK = len(self.eg)
        self.sym = self.eg["symbol"].fillna("").astype(str).to_numpy()
        self.pos = np.full(self.gK, -1, dtype=np.int64)
        self.pos[self.inc] = np.arange(len(self.inc))
        self.included = self.pos >= 0
        self.U = np.load(os.path.join(ed, "gene_unit.npy"), mmap_mode="r")[self.inc].astype(np.float32)
        self.U = np.nan_to_num(self.U)
        self.U1 = self.U2 = None
        if os.path.exists(os.path.join(ed, "gene_unit_half1.npy")):
            self.U1 = np.nan_to_num(np.load(os.path.join(ed, "gene_unit_half1.npy"), mmap_mode="r")[self.inc]
                                    .astype(np.float32))
            self.U2 = np.nan_to_num(np.load(os.path.join(ed, "gene_unit_half2.npy"), mmap_mode="r")[self.inc]
                                    .astype(np.float32))
        n = len(self.inc)
        self.n = n
        nodes = pd.read_parquet(os.path.join(out, "graph", "nodes.parquet")).set_index("col")
        nodes = nodes.reindex(self.inc)
        self.module = nodes["module"].fillna(0).astype(np.int64).to_numpy()
        self.arm = nodes["arm"].fillna("").astype(str).to_numpy()
        self.axis_proj = nodes["axis_proj"].fillna(0).to_numpy() if "axis_proj" in nodes else np.zeros(n)
        self.xy = nodes[["x", "y"]].to_numpy(dtype=np.float64)
        self.xys = nodes[["xs", "ys"]].to_numpy(dtype=np.float64)
        self.spread = float(np.sqrt(np.nansum(np.nanvar(self.xy, axis=0))))
        self.spread_s = float(np.sqrt(np.nansum(np.nanvar(self.xys, axis=0))))
        nm = int(self.module.max()) if n else 0
        self.n_modules = nm
        cnt = np.bincount(self.module, minlength=nm + 1).astype(np.float64)
        self.mod_share = cnt / max(n, 1)
        self.p_same_module = float((self.mod_share[1:] ** 2).sum())      # two random genes share a module
        rng = np.random.default_rng(stable_seed("validate", "random pairs"))
        self.bg_cos = np.zeros(0)
        self.bg_abs = np.zeros(0)
        if n >= 2:
            a = rng.integers(0, n, n_random)
            b = (a + rng.integers(1, n, n_random)) % n                     # b != a
            c = np.einsum("ij,ij->i", self.U[a], self.U[b]).astype(np.float64)
            self.bg_cos = np.sort(c)
            self.bg_abs = np.sort(np.abs(c))
        self._null = {}
        self._pool = None

    def null(self, size, n_null):
        """AUROCs (cos, abs cos) of n_null random gene sets of this size. The sets are drawn from one random pool of
        <= NULL_POOL genes whose cosines are computed once (one large product instead of thousands of small ones)."""
        if self._pool is None:
            rng = np.random.default_rng(stable_seed("validate", "null pool"))
            pool = np.sort(rng.choice(self.n, min(self.n, NULL_POOL), replace=False))
            self._pool = (self.U[pool] @ self.U[pool].T).astype(np.float32)
        G = self._pool
        if size not in self._null:
            rng = np.random.default_rng(stable_seed("validate", "null", size))
            iu = np.triu_indices(size, 1)
            a1 = np.empty(n_null)
            a2 = np.empty(n_null)
            for i in range(n_null):
                s = rng.choice(len(G), size, replace=False)
                c = G[np.ix_(s, s)][iu]
                a1[i] = _auroc(c, self.bg_cos)
                a2[i] = _auroc(np.abs(c), self.bg_abs)
            self._null[size] = (a1, a2)
        return self._null[size]


def _mean_pair_cos(V):
    """Mean of v_i . v_j over pairs i < j without the n x n product: (|sum v|^2 - sum |v|^2) / (n (n - 1))."""
    n = len(V)
    if n < 2:
        return np.nan
    V = V.astype(np.float64)
    t = V.sum(axis=0)
    return float((t @ t - (V * V).sum()) / (n * (n - 1)))


def _set_metrics(sp, st, n_null):
    p = sp.pos[st["cols"]]
    n = len(p)
    r = {"n_in_space": n, "mean_cos": np.nan, "median_cos": np.nan, "frac_pos": np.nan, "auroc_cos": np.nan,
         "auroc_abs": np.nan, "p_random_sets_cos": np.nan, "p_random_sets_abs": np.nan, "mean_cos_half1": np.nan,
         "mean_cos_half2": np.nan, "top_module": 0, "top_module_share": np.nan, "top_module_genome_share": np.nan,
         "top_module_arm_share": np.nan}
    if n < 2:
        return r
    iu = np.triu_indices(n, 1)
    c = (sp.U[p] @ sp.U[p].T)[iu].astype(np.float64)
    r.update(mean_cos=float(c.mean()), median_cos=float(np.median(c)), frac_pos=float((c > 0).mean()),
             auroc_cos=_auroc(c, sp.bg_cos), auroc_abs=_auroc(np.abs(c), sp.bg_abs))
    if sp.U1 is not None:
        r["mean_cos_half1"] = _mean_pair_cos(sp.U1[p])
        r["mean_cos_half2"] = _mean_pair_cos(sp.U2[p])
    if st["source"] in NULL_SOURCES and n_null and n <= min(sp.n, NULL_POOL) // 2:
        a1, a2 = sp.null(n, n_null)
        r["p_random_sets_cos"] = float((1 + (a1 >= r["auroc_cos"]).sum()) / (1 + len(a1)))
        r["p_random_sets_abs"] = float((1 + (a2 >= r["auroc_abs"]).sum()) / (1 + len(a2)))
    m = sp.module[p]
    if (m > 0).any():
        cnt = np.bincount(m[m > 0])
        top = int(cnt.argmax())
        r.update(top_module=top, top_module_share=float(cnt[top] / n),
                 top_module_genome_share=float(sp.mod_share[top]))
        a = sp.arm[p][m == top]
        r["top_module_arm_share"] = float(max((a == "+").sum(), (a == "-").sum()) / len(a))
    return r


def _best_drugdoses(out, gK, sets):
    """Per set: the TOP_DD drug-doses with the highest / lowest mean pooled DD_z over its members (drug-doses that are
    technically untrustworthy are left out; '†' marks other artifact flags, e.g. toxic)."""
    from scipy import sparse
    fxd = os.path.join(out, "atlas", "effects")
    dd = read_effects_index(fxd)["drugdose"]
    flags = dd["flags"].fillna("").astype(str).to_numpy()
    ok = np.array([not any(u in set(f.split("; ")) for u in UNTRUSTED) for f in flags])
    art = np.array([A.has_artifact(f) for f in flags])
    lab = (dd["drug"].astype(str) + " " + dd["dose"].astype(str) + " uM").to_numpy()
    Z = np.asarray(np.load(os.path.join(fxd, "DD_z.npy"), mmap_mode="r")[:, :gK], dtype=np.float32)
    F = np.isfinite(Z).astype(np.float32)
    Z = np.nan_to_num(Z, nan=0.0)
    rows, cols = [], []
    for j, st in enumerate(sets):
        rows += list(st["cols"])
        cols += [j] * len(st["cols"])
    M = sparse.csr_matrix((np.ones(len(rows), dtype=np.float32), (rows, cols)), shape=(gK, len(sets)))
    with np.errstate(invalid="ignore", divide="ignore"):
        mean = np.asarray(M.T @ Z.T) / np.asarray(M.T @ F.T)           # sets x drug-doses
    mean[:, ~ok] = np.nan
    up, down = [], []
    for j in range(len(sets)):
        v = mean[j]
        fin = np.where(np.isfinite(v))[0]
        if not len(fin):
            up.append("")
            down.append("")
            continue
        o = fin[np.argsort(-v[fin], kind="mergesort")]
        up.append("; ".join(f"{lab[i]}{'†' if art[i] else ''} ({v[i]:+.1f})" for i in o[:TOP_DD]))
        down.append("; ".join(f"{lab[i]}{'†' if art[i] else ''} ({v[i]:+.1f})" for i in o[::-1][:TOP_DD]))
    return up, down


# ----------------------------------------------------------------------------- opposite pairs
def _opposite(sp, pa, pb):
    shared = np.intersect1d(pa, pb)
    pa = np.setdiff1d(pa, shared)
    pb = np.setdiff1d(pb, shared)
    r = {"n_a": len(pa), "n_b": len(pb), "n_shared_dropped": len(shared), "mean_cross_cos": np.nan,
         "median_cross_cos": np.nan, "frac_cross_neg": np.nan, "auroc_anti": np.nan, "mean_cross_cos_half1": np.nan,
         "mean_cross_cos_half2": np.nan, "within_cos_a": np.nan, "within_cos_b": np.nan,
         "share_same_module": np.nan, "random_same_module": sp.p_same_module,
         "share_opposite_arms_in_same_module": np.nan, "nodal_centroid_dist": np.nan,
         "signed_centroid_dist": np.nan}
    if not len(pa) or not len(pb):
        return r
    C = (sp.U[pa] @ sp.U[pb].T).astype(np.float64)
    c = C.ravel()
    r.update(mean_cross_cos=float(c.mean()), median_cross_cos=float(np.median(c)),
             frac_cross_neg=float((c < 0).mean()), auroc_anti=_auroc(-c, -sp.bg_cos[::-1]))
    if sp.U1 is not None:
        r["mean_cross_cos_half1"] = float(sp.U1[pa].astype(np.float64).sum(0) @ sp.U1[pb].astype(np.float64).sum(0)
                                          / (len(pa) * len(pb)))
        r["mean_cross_cos_half2"] = float(sp.U2[pa].astype(np.float64).sum(0) @ sp.U2[pb].astype(np.float64).sum(0)
                                          / (len(pa) * len(pb)))
    r["within_cos_a"], r["within_cos_b"] = _mean_pair_cos(sp.U[pa]), _mean_pair_cos(sp.U[pb])
    ma, mb = sp.module[pa], sp.module[pb]
    same = (ma[:, None] == mb[None, :]) & (ma[:, None] > 0)
    r["share_same_module"] = float(same.mean())
    if same.any():
        opp = sp.arm[pa][:, None] != sp.arm[pb][None, :]
        r["share_opposite_arms_in_same_module"] = float(opp[same].mean())
    if sp.spread > 0:
        r["nodal_centroid_dist"] = float(np.linalg.norm(sp.xy[pa].mean(0) - sp.xy[pb].mean(0)) / sp.spread)
    if sp.spread_s > 0:
        r["signed_centroid_dist"] = float(np.linalg.norm(sp.xys[pa].mean(0) - sp.xys[pb].mean(0)) / sp.spread_s)
    return r


def _reading(r):
    a, b = r["a"], r["b"]
    if not np.isfinite(r["mean_cross_cos"]):
        return f"{a} / {b}: not testable here ({r['n_a']} and {r['n_b']} genes in the vector space)."
    mc, fn = r["mean_cross_cos"], r["frac_cross_neg"]
    if mc <= -0.1:
        s = f"{a} / {b}: the two sets move in opposite directions (mean cross-set cosine {mc:+.2f}; {fn:.0%} of " \
            f"the cross pairs are negative)"
    elif mc <= OPP_COS / 3:
        s = f"{a} / {b}: only weakly opposite (mean cross-set cosine {mc:+.2f}; {fn:.0%} of cross pairs negative)"
    else:
        s = f"{a} / {b}: NOT opposite in this data (mean cross-set cosine {mc:+.2f}; {fn:.0%} of cross pairs " \
            f"negative)"
    s += f". {_pct(r['share_same_module'])} of the cross pairs share a module of the nodal map (two random " \
         f"genes: {_pct(r['random_same_module'])})"
    if np.isfinite(r["share_opposite_arms_in_same_module"]):
        s += f", and {_pct(r['share_opposite_arms_in_same_module'])} of those sit on opposite arms"
    dn, ds = r["nodal_centroid_dist"], r["signed_centroid_dist"]
    if np.isfinite(dn) and np.isfinite(ds):
        s += f". Centroid distance: {dn:.2f} map spreads on the nodal map vs {ds:.2f} on the signed map"
        together = dn <= TOGETHER and dn < 0.5 * ds
        if mc <= OPP_COS and together:
            s += " - together on the nodal map, apart in the signed vector space, as intended."
        elif mc <= OPP_COS:
            s += " - opposite in the vector space, but the nodal map does not bring them together."
        else:
            s += " - with no opposite relation in the data, the map test does not apply."
    else:
        s += "."
    return s


# ----------------------------------------------------------------------------- module enrichment
def _enrichment(sp, sets):
    """Every module ('all') and arm ('+', '-') vs every set with >= MIN_SET genes in the space."""
    from scipy import sparse
    from scipy.stats import hypergeom
    units = []
    for m in range(1, sp.n_modules + 1):
        mem = np.where(sp.module == m)[0]
        if not len(mem):
            continue
        units.append((m, "all", mem))
        for a in ("+", "-"):
            ar = mem[sp.arm[mem] == a]
            if len(ar) >= 2:
                units.append((m, a, ar))
    tsets = [j for j, st in enumerate(sets) if len(st["cols"]) >= MIN_SET and st["source"] != "synthetic"]
    if not units or not tsets:
        return units, tsets, np.zeros((len(units), len(tsets))), np.ones((len(units), len(tsets))), \
            np.ones((len(units), len(tsets)))
    r_, c_ = [], []
    for i, (_, _, mem) in enumerate(units):
        r_ += [i] * len(mem)
        c_ += list(mem)
    Au = sparse.csr_matrix((np.ones(len(r_), dtype=np.int32), (r_, c_)), shape=(len(units), sp.n))
    r_, c_ = [], []
    for j, sj in enumerate(tsets):
        p = sp.pos[sets[sj]["cols"]]
        r_ += list(p)
        c_ += [j] * len(p)
    Bs = sparse.csc_matrix((np.ones(len(r_), dtype=np.int32), (r_, c_)), shape=(sp.n, len(tsets)))
    O = np.asarray((Au @ Bs).todense()).astype(np.int64)
    nu = np.array([len(u[2]) for u in units], dtype=np.int64)
    ns = np.array([len(sets[j]["cols"]) for j in tsets], dtype=np.int64)
    P = np.ones(O.shape)
    i, j = np.nonzero(O >= 1)
    P[i, j] = hypergeom.sf(O[i, j] - 1, sp.n, ns[j], nu[i])
    Q = _bh(P.ravel()).reshape(P.shape)
    return units, tsets, O, P, Q


def _enrichment_table(sp, sets, units, tsets, O, P, Q):
    ns = np.array([len(sets[j]["cols"]) for j in tsets], dtype=np.int64)
    i, j = np.nonzero((O >= 2) & ((P <= ENRICH_KEEP_P) | (Q < LABEL_Q)))
    rows = []
    for a, b in zip(i, j):
        m, arm, mem = units[a]
        st = sets[tsets[b]]
        ov = np.intersect1d(mem, sp.pos[st["cols"]])
        ov = ov[np.argsort(-np.abs(sp.axis_proj[ov]), kind="mergesort")]
        exp = len(mem) * ns[b] / sp.n
        rows.append({"module": m, "arm": arm, "n_unit": len(mem), "source": st["source"], "set": st["set"],
                     "set_label": st["label"], "n_set": int(ns[b]), "overlap": int(O[a, b]),
                     "expected": round(exp, 3), "fold": round(O[a, b] / exp, 3) if exp > 0 else np.nan,
                     "p": P[a, b], "q": Q[a, b], "genes": ", ".join(sp.sym[sp.inc[ov[:25]]])})
    cols = ["module", "arm", "n_unit", "source", "set", "set_label", "n_set", "overlap", "expected", "fold", "p",
            "q", "genes"]
    df = pd.DataFrame(rows, columns=cols)
    if len(df):
        df["_a"] = df["arm"].map({"all": 0, "+": 1, "-": 2})
        df = df.sort_values(["module", "_a", "p"], kind="mergesort").drop(columns="_a").reset_index(drop=True)
    return df


def _labels(sp, sets, units, tsets, O, P, Q, out):
    mp = os.path.join(out, "graph", "modules.parquet")
    mods = pd.read_parquet(mp).set_index("module") if os.path.exists(mp) else pd.DataFrame()
    ns = np.array([len(sets[j]["cols"]) for j in tsets], dtype=np.int64)

    src = np.array([SOURCES_ORDER.get(sets[j]["source"], 9) for j in tsets])

    def best(rows_i):
        """(unit index, set index into tsets) of the best q < LABEL_Q test among units rows_i, or None. Equal p
        (Reactome repeats one gene list under many names) -> curated source first, then the smaller set (in the
        space, then at the source)."""
        cand = [(float(f"{P[i, j]:.4g}"), src[j], ns[j], sets[tsets[j]]["n_listed"], -O[i, j], sets[tsets[j]]["set"],
                 i, j) for i in rows_i
                for j in np.where((Q[i] < LABEL_Q) & (O[i] >= LABEL_MIN_OVERLAP))[0]]
        if not cand:
            return None
        spec = [c for c in cand if c[2] <= LABEL_MAX_SET]
        c = min(spec or cand)
        return c[6], c[7]

    by_mod = {}
    for i, (m, arm, _) in enumerate(units):
        by_mod.setdefault(m, {})[arm] = i
    rows = []
    for m in range(1, sp.n_modules + 1):
        mem = np.where(sp.module == m)[0]
        if not len(mem):
            continue
        u = by_mod.get(m, {})
        rec = {"module": m, "n_genes": len(mem), "n_plus": int((sp.arm[mem] == "+").sum()),
               "n_minus": int((sp.arm[mem] == "-").sum())}
        b = best(list(u.values()))
        if m in mods.index:
            tp = [g for g in str(mods.at[m, "top_plus"]).split(", ") if g]
            tm = [g for g in str(mods.at[m, "top_minus"]).split(", ") if g]
        else:
            order = mem[np.argsort(-np.abs(sp.axis_proj[mem]), kind="mergesort")]
            tp = [sp.sym[sp.inc[k]] for k in order if sp.arm[k] == "+"]
            tm = [sp.sym[sp.inc[k]] for k in order if sp.arm[k] == "-"]
        top_genes = ", ".join(tp[:3] + tm[:2])
        if b is not None:
            i, j = b
            st = sets[tsets[j]]
            rec.update(label=st["label"], label_source=st["source"], label_set=st["set"], label_arm=units[i][1],
                       label_overlap=int(O[i, j]), label_n_set=int(ns[j]), label_p=P[i, j], label_q=Q[i, j])
        else:
            rec.update(label="genes: " + top_genes, label_source="top genes", label_set="", label_arm="",
                       label_overlap=0, label_n_set=0, label_p=np.nan, label_q=np.nan)
        for arm, nm in (("+", "plus"), ("-", "minus")):
            bb = best([u[arm]]) if arm in u else None
            if bb is not None:
                st = sets[tsets[bb[1]]]
                rec[f"{nm}_label"], rec[f"{nm}_set"], rec[f"{nm}_q"] = st["label"], st["set"], Q[bb]
            else:
                rec[f"{nm}_label"], rec[f"{nm}_set"], rec[f"{nm}_q"] = "", "", np.nan
        rec["top_plus"] = ", ".join(tp[:8])
        rec["top_minus"] = ", ".join(tm[:8])
        rows.append(rec)
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- novel candidates
def _novel_edges(out, sp, ann_name):
    p = os.path.join(out, "relations", "gene_relations.parquet")
    cols = ["col_a", "col_b", "cos", "abs_cos", "cos_half1", "cos_half2", "evidence", "fdr", "novel_candidate",
            "locus", "readthrough_risk", "same_chrom", "distance_bp"]
    empty = pd.DataFrame(columns=["col_a", "symbol_a", "name_a", "module_a", "arm_a", "col_b", "symbol_b", "name_b",
                                  "module_b", "arm_b", "same_module", "cos", "cos_half1", "cos_half2", "evidence",
                                  "fdr", "same_chrom", "distance_bp"])
    if not os.path.exists(p):
        return empty
    import pyarrow.parquet as pq
    have = set(pq.ParquetFile(p).schema_arrow.names)
    rel = pd.read_parquet(p, columns=[c for c in cols if c in have])
    if "novel_candidate" not in rel:
        return empty
    keep = rel["novel_candidate"].fillna(False).astype(bool)
    for c in ("locus", "readthrough_risk"):
        if c in rel:
            keep &= ~rel[c].fillna(False).astype(bool)
    r = rel[keep].copy()
    if not len(r):
        return empty
    lo = np.minimum(r["col_a"], r["col_b"]).to_numpy()
    hi = np.maximum(r["col_a"], r["col_b"]).to_numpy()
    r["col_a"], r["col_b"] = lo, hi
    r = r.sort_values("abs_cos", ascending=False, kind="mergesort").drop_duplicates(["col_a", "col_b"])
    a, b = r["col_a"].to_numpy(), r["col_b"].to_numpy()
    pa, pb = sp.pos[a], sp.pos[b]
    ma = np.where(pa >= 0, sp.module[np.maximum(pa, 0)], 0)
    mb = np.where(pb >= 0, sp.module[np.maximum(pb, 0)], 0)
    res = pd.DataFrame({"col_a": a, "symbol_a": sp.sym[a], "name_a": ann_name[a], "module_a": ma,
                        "arm_a": np.where(pa >= 0, sp.arm[np.maximum(pa, 0)], ""),
                        "col_b": b, "symbol_b": sp.sym[b], "name_b": ann_name[b], "module_b": mb,
                        "arm_b": np.where(pb >= 0, sp.arm[np.maximum(pb, 0)], ""),
                        "same_module": (ma == mb) & (ma > 0), "cos": r["cos"].to_numpy(),
                        "cos_half1": r["cos_half1"].to_numpy(), "cos_half2": r["cos_half2"].to_numpy(),
                        "evidence": r["evidence"].to_numpy(), "fdr": r["fdr"].to_numpy(),
                        "same_chrom": r["same_chrom"].to_numpy() if "same_chrom" in r else False,
                        "distance_bp": r["distance_bp"].to_numpy() if "distance_bp" in r else np.nan})
    return res.reset_index(drop=True)


def _novel_members(sp, sets, units, tsets, Q, ann_name, n_ref_sets):
    cols = ["col", "symbol", "name", "module", "arm", "source", "set", "set_label", "set_q", "n_annotated_in_arm",
            "n_arm", "mean_cos", "max_cos", "mean_cos_half1", "mean_cos_half2", "n_reference_sets"]
    parts = []
    for i, (m, arm, mem) in enumerate(units):
        if arm == "all":
            continue
        for j in np.where(Q[i] < GBA_Q)[0]:
            st = sets[tsets[j]]
            if len(st["cols"]) > LABEL_MAX_SET:
                continue
            sp_set = sp.pos[st["cols"]]
            annot = np.intersect1d(mem, sp_set)
            if len(annot) < GBA_MIN_ANNOT:
                continue
            cand = np.setdiff1d(mem, sp_set)
            cand = np.array([k for k in cand if sp.sym[sp.inc[k]].upper() not in st["names"]], dtype=np.int64)
            if not len(cand):
                continue
            C = sp.U[cand] @ sp.U[annot].T
            mc = C.mean(axis=1)
            ok = mc >= GBA_COS
            if not ok.any():
                continue
            k = cand[ok]
            g = sp.inc[k]
            nan = np.full(len(k), np.nan)
            parts.append(pd.DataFrame({
                "col": g, "symbol": sp.sym[g], "name": ann_name[g], "module": m, "arm": arm, "source": st["source"],
                "set": st["set"], "set_label": st["label"], "set_q": float(Q[i, j]),
                "n_annotated_in_arm": len(annot), "n_arm": len(mem), "mean_cos": mc[ok], "max_cos": C.max(axis=1)[ok],
                "mean_cos_half1": (sp.U1[k] @ sp.U1[annot].T).mean(axis=1) if sp.U1 is not None else nan,
                "mean_cos_half2": (sp.U2[k] @ sp.U2[annot].T).mean(axis=1) if sp.U2 is not None else nan,
                "n_reference_sets": n_ref_sets[g]}))
    if not parts:
        return pd.DataFrame(columns=cols)
    df = pd.concat(parts, ignore_index=True)[cols]
    # each gene's GBA_PER_GENE most significant sets; genes ranked by the mean cos for their most significant set
    df = df.sort_values(["col", "set_q", "mean_cos"], ascending=[True, True, False], kind="mergesort")
    df = df.groupby("col", sort=False).head(GBA_PER_GENE)
    best = df.groupby("col", sort=False)["mean_cos"].first()
    df["_r"] = df["col"].map(best)
    df = df.sort_values(["_r", "col", "set_q"], ascending=[False, True, True], kind="mergesort")
    return df.drop(columns="_r").reset_index(drop=True)


# ----------------------------------------------------------------------------- drug check
def _drug_check(out):
    ed = os.path.join(out, "embed")
    p = os.path.join(ed, "drug_vectors.npy")
    if not (os.path.exists(p) and os.path.exists(os.path.join(ed, "drugs.parquet"))):
        return {}, pd.DataFrame()
    V = np.nan_to_num(np.load(p).astype(np.float64))
    dr = pd.read_parquet(os.path.join(ed, "drugs.parquet"))
    min_active = 10
    ip = os.path.join(ed, "info.json")
    if os.path.exists(ip):
        with open(ip, encoding="utf-8") as fh:
            min_active = int(json.load(fh).get("min_active", 10))
    norm = np.linalg.norm(V, axis=1)
    Un = V / np.maximum(norm, 1e-12)[:, None]
    moa = dr["moa_fine"].fillna("").astype(str).str.strip().to_numpy() if "moa_fine" in dr \
        else np.array([""] * len(dr))
    valid = ~pd.Series(moa).str.lower().isin(NO_MOA).to_numpy() & (norm > 0)
    salt = np.array([T.salt_base(d) for d in dr["drug"].astype(str)])
    nsig = pd.to_numeric(dr.get("n_sig_genes", pd.Series(0, index=dr.index)), errors="coerce").fillna(0).to_numpy()
    res = {}
    for tag, sel in (("all", valid), ("active", valid & (nsig >= min_active))):
        idx = np.where(sel)[0]
        r = {"drugs": int(len(idx)), "moa_classes": int(len(set(moa[idx]))), "pos_pairs": 0, "neg_pairs": 0,
             "auroc": np.nan, "mean_cos_same_moa": np.nan, "mean_cos_other": np.nan}
        if len(idx) >= 3:
            C = Un[idx] @ Un[idx].T
            iu = np.triu_indices(len(idx), 1)
            same = (moa[idx][:, None] == moa[idx][None, :])[iu]
            keep = (salt[idx][:, None] != salt[idx][None, :])[iu]
            c = C[iu]
            pos, neg = c[keep & same], c[keep & ~same]
            r.update(pos_pairs=int(len(pos)), neg_pairs=int(len(neg)), auroc=_auroc(pos, np.sort(neg)),
                     mean_cos_same_moa=float(pos.mean()) if len(pos) else np.nan,
                     mean_cos_other=float(neg.mean()) if len(neg) else np.nan)
        r["min_active"] = min_active
        res[tag] = r
    # per class (all drugs with a known mechanism)
    idx = np.where(valid)[0]
    rows = []
    if len(idx) >= 3:
        C = Un[idx] @ Un[idx].T
        mi, si = moa[idx], salt[idx]
        for cl in sorted(set(mi)):
            w = np.where(mi == cl)[0]
            o = np.where(mi != cl)[0]
            if len(w) < 2:
                continue
            sub = C[np.ix_(w, w)]
            iu = np.triu_indices(len(w), 1)
            ks = (si[w][:, None] != si[w][None, :])[iu]
            within = sub[iu][ks]
            between = C[np.ix_(w, o)].ravel()
            rows.append({"moa_fine": cl, "n_drugs": len(w), "drugs": ", ".join(dr["drug"].astype(str).to_numpy()
                                                                               [idx[w]][:12]),
                         "n_pairs": int(len(within)), "mean_cos_within": float(within.mean()) if len(within)
                         else np.nan, "mean_cos_to_other_classes": float(between.mean()) if len(between) else np.nan,
                         "auroc_within_vs_other": _auroc(within, np.sort(between))})
    tab = pd.DataFrame(rows)
    if len(tab):
        tab = tab.sort_values(["auroc_within_vs_other", "n_drugs"], ascending=[False, False],
                              kind="mergesort").reset_index(drop=True)
    return res, tab


# ----------------------------------------------------------------------------- report
def _set_rows(df, n=None, n_null=N_NULL):
    rows = []
    for _, r in (df if n is None else df.head(n)).iterrows():
        tm = f"{int(r['top_module'])} ({_pct(r['top_module_share'])}; all genes {_pct(r['top_module_genome_share'])})" \
            if r["top_module"] > 0 else "-"
        p = r["p_random_sets_cos"]
        ps = f"<= {p:.3f}" if np.isfinite(p) and p <= 1.0 / (1 + n_null) + 1e-12 else _p_fmt(p)
        rows.append([r["set"], f"{r['n_in_space']}/{r['n_listed']}", _f(r["mean_cos"]), _f(r["auroc_cos"]),
                     _f(r["auroc_abs"]), ps, tm, r["best_dd_up"] or "-"])
    return rows


SET_HEAD = ["set", "genes in space / listed", "mean cos", "AUROC cos", "AUROC abs(cos)", "p (random sets)",
            "top module (share; all genes)", "drug-doses raising it most (mean z)"]


def _opp_table(op):
    rows = []
    for _, r in op.iterrows():
        rows.append([f"{r['a']} / {r['b']}", f"{r['n_a']} / {r['n_b']}", _f(r["mean_cross_cos"], "{:+.2f}"),
                     _pct(r["frac_cross_neg"]), _f(r["auroc_anti"]),
                     f"{_pct(r['share_same_module'])} (random {_pct(r['random_same_module'])})",
                     _pct(r["share_opposite_arms_in_same_module"]), _f(r["nodal_centroid_dist"]),
                     _f(r["signed_centroid_dist"])])
    return _md_table(["pair", "genes a / b", "mean cross cos", "cross pairs < 0", "AUROC anti",
                      "cross pairs in same module", "of those, opposite arms", "nodal map distance",
                      "signed map distance"], rows)


def _report(path, ctx):
    sp, cs, op, labels, edges, members, drug, drug_tab, n_sets, n_null = (
        ctx["sp"], ctx["cs"], ctx["op"], ctx["labels"], ctx["edges"], ctx["members"], ctx["drug"], ctx["drug_tab"],
        ctx["n_sets"], ctx["n_null"])
    L = ["# Validation report", "",
         f"Written by `tahoemap validate` (tahoemap/validate.py) on {time.strftime('%Y-%m-%d %H:%M')}. "
         f"{sp.n:,} genes are in the vector space ({sp.U.shape[1]} dimensions); the nodal map has "
         f"{sp.n_modules} modules. `cos` is the signed cosine of two genes' unit vectors: the correlation of their "
         f"denoised responses over every (drug-dose, cell line) context (+1 = always move together, -1 = always "
         f"opposite). AUROC = probability that a pair of genes from the set has a higher cosine than a random pair "
         f"of genes in the space (0.5 = no better than random, 1 = every set pair beats every random pair). "
         f"'p (random sets)' = share of {n_null} random gene sets of the same size that score at least as high.", ""]

    ctl = cs[cs["source"] == "control"].sort_values("auroc_cos", ascending=False, na_position="last")
    tested = ctl[ctl["n_in_space"] >= 2]
    L += ["## 1. Do known programmes hang together in the vector space?", "",
          f"Curated control sets (tahoemap/data/control_sets.json; literature, not Tahoe), ranked by AUROC on cos. "
          f"{len(tested)} of {len(ctl)} sets have >= 2 genes in the space; "
          f"{int((tested['auroc_cos'] >= 0.6).sum())} reach AUROC >= 0.6 and "
          f"{int((tested['p_random_sets_cos'] <= 0.05).sum())} have p <= 0.05 against random sets. "
          f"'top module' = the module holding most of the set's genes, its share of the set, and its share of all "
          f"genes (the chance level). Drug-doses marked † carry an artifact flag (e.g. toxic).", "",
          _md_table(SET_HEAD, _set_rows(ctl, n_null=n_null)), ""]
    for src, title in (("hallmark", "MSigDB Hallmark"), ("reactome", "Reactome")):
        d = cs[cs["source"] == src]
        if not len(d):
            continue
        L += [f"**{title}** ({len(d)} sets with >= {MIN_SET} genes in the space): median AUROC on cos "
              f"{_f(d['auroc_cos'].median())}, {int((d['auroc_cos'] >= 0.6).sum())} sets ({_pct((d['auroc_cos'] >= 0.6).mean())}) "
              f"at >= 0.6" + (f", {int((d['p_random_sets_cos'] <= 0.05).sum())} with p <= 0.05 against random sets"
                              if d["p_random_sets_cos"].notna().any() else "") + ".", ""]
        if src == "hallmark":
            L += [_md_table(SET_HEAD, _set_rows(d.sort_values("auroc_cos", ascending=False), 12, n_null)), ""]
    if not n_sets.get("reference"):
        L += ["No Hallmark / Reactome sets: the reference stage did not run (or found no sets).", ""]

    L += ["## 2. Opposite programmes: apart in the vector space, together on the nodal map", "",
          "Pairs of programmes expected to move in opposite directions under the same drugs. In the signed vector "
          "space they should be anti-aligned (mean cross-set cosine < 0, most cross pairs negative); the nodal map "
          "is built on |cos|, so it should put them in the same module (on opposite arms) and close together, while "
          "the signed map keeps them apart. Map distances are centroid distances divided by the map's spread "
          "(sqrt(var x + var y)); 'AUROC anti' = P(cross pair cos < random pair cos).", ""]
    ctl_op = op[op["source"] == "control"] if len(op) else op
    if len(ctl_op):
        L += [_opp_table(ctl_op), ""]
        L += ["- " + _reading(r) for _, r in ctl_op.iterrows()]
        L += [""]

    L += ["## 3. Drug check: do drugs with the same mechanism get similar vectors?", ""]
    if drug:
        rows = []
        for tag, d in drug.items():
            lab = "all drugs with a known moa_fine" if tag == "all" else \
                f"active drugs only (best dose >= {d.get('min_active', 10)} significant genes)"
            rows.append([lab, d["drugs"], d["moa_classes"], d["pos_pairs"], d["neg_pairs"],
                         _f(d["mean_cos_same_moa"], "{:+.2f}"), _f(d["mean_cos_other"], "{:+.2f}"), _f(d["auroc"])])
        L += ["Cosine of drug vectors (each drug's best dose) for pairs sharing moa_fine vs pairs with different "
              "moa_fine ('unclear' / 'unknown' left out; salt forms of one compound never paired).", "",
              _md_table(["drugs", "n", "classes", "same-moa pairs", "other pairs", "mean cos same", "mean cos other",
                         "AUROC"], rows), ""]
        if len(drug_tab):
            t = drug_tab.head(12)
            L += ["Mechanism classes with >= 2 drugs (best first; full table in drug_moa.csv):", "",
                  _md_table(["moa_fine", "drugs", "mean cos within", "mean cos to others", "AUROC"],
                            [[r["moa_fine"], r["drugs"], _f(r["mean_cos_within"], "{:+.2f}"),
                              _f(r["mean_cos_to_other_classes"], "{:+.2f}"), _f(r["auroc_within_vs_other"])]
                             for _, r in t.iterrows()]), ""]
    else:
        L += ["No drug vectors (embed stage files missing).", ""]

    nlab = int((labels["label_source"] != "top genes").sum()) if len(labels) else 0
    L += ["## 4. Modules and their labels", "",
          f"Each module and each of its arms was tested against every set (hypergeometric, universe = the {sp.n:,} "
          f"genes in the space, Benjamini-Hochberg over all tests; module_enrichment.csv). {nlab} of {len(labels)} "
          f"modules carry a set label (q < {LABEL_Q}, >= {LABEL_MIN_OVERLAP} genes shared; the most significant "
          f"set of <= {LABEL_MAX_SET} genes when there is one); the others are named by their top genes. "
          f"The 20 largest:", ""]
    if len(labels):
        rows = [[r["module"], r["n_genes"], f"{r['n_plus']}/{r['n_minus']}", r["label"],
                 f"{r['label_source']}{(' (' + r['label_arm'] + ')') if r['label_arm'] else ''}",
                 _p_fmt(r["label_q"]), ", ".join(r["top_plus"].split(", ")[:5]) or "-",
                 ", ".join(r["top_minus"].split(", ")[:5]) or "-"]
                for _, r in labels.sort_values("n_genes", ascending=False).head(20).iterrows()]
        L += [_md_table(["module", "genes", "+/-", "label", "from (arm)", "q", "top + arm", "top - arm"], rows), ""]

    L += ["## 5. Novel gene relations", "",
          f"{len(edges):,} pairs (one row per pair) are reproduced in both halves of the compounds (fdr <= 0.05, "
          f"|cos| >= 0.5) and have no shared HGNC gene group, no shared Hallmark / Reactome pathway and no STRING "
          f"link, and are not the same locus or a read-through pair. Top 25 by |cos| (novel_edges.csv has all):", ""]
    if len(edges):
        rows = [[f"{r['symbol_a']} ({r['module_a']}{r['arm_a']})", f"{r['symbol_b']} ({r['module_b']}{r['arm_b']})",
                 _f(r["cos"], "{:+.2f}"), f"{_f(r['cos_half1'], '{:+.2f}')} / {_f(r['cos_half2'], '{:+.2f}')}",
                 _p_fmt(r["fdr"]), (str(r["name_a"])[:40] or "-") + " / " + (str(r["name_b"])[:40] or "-")]
                for _, r in edges.head(25).iterrows()]
        L += [_md_table(["gene a (module arm)", "gene b (module arm)", "cos", "cos half1 / half2", "fdr",
                         "names"], rows), ""]
    elif not n_sets.get("reference"):
        L += ["Nothing can be called novel without the reference stage.", ""]

    L += ["## 6. Novel module members (guilt by association)", "",
          f"Genes on a module arm enriched for a set (q < {GBA_Q}; sets of <= {LABEL_MAX_SET} genes in the space, "
          f">= {GBA_MIN_ANNOT} of them on the arm) that the set does not list, with mean cosine >= {GBA_COS} to the "
          f"arm's listed members: {members['col'].nunique() if len(members) else 0:,} genes "
          f"({len(members):,} gene-set rows in novel_members.csv, <= {GBA_PER_GENE} most significant sets per gene). "
          f"Top 25 genes, each with the arm's most significant set that does not list it ('sets already listing the "
          f"gene' = Hallmark / Reactome sets naming it at all; 0 = no pathway annotation):", ""]
    if len(members):
        top = members.drop_duplicates("col").head(25)
        rows = [[r["symbol"], (str(r["name"])[:45] or "-"), f"{r['module']}{r['arm']}", r["set_label"][:60],
                 f"{r['n_annotated_in_arm']}/{r['n_arm']}", _f(r["mean_cos"]),
                 f"{_f(r['mean_cos_half1'])} / {_f(r['mean_cos_half2'])}", r["n_reference_sets"]]
                for _, r in top.iterrows()]
        L += [_md_table(["gene", "name", "module arm", "set", "listed members in arm", "mean cos to them",
                         "half1 / half2", "sets already listing the gene"], rows), ""]

    syn = cs[cs["source"] == "synthetic"]
    if len(syn):
        L += ["## 7. Synthetic ground truth", "",
              "The synthetic generator's planted gene sets (ground_truth.json 'synthetic gene sets'), with the same "
              "metrics. (On the synthetic data most curated control sets are real gene names that the generator does "
              "not move together, so sections 1-2 there are not a test of the method; this section is.)", "",
              _md_table(SET_HEAD, _set_rows(syn.sort_values("auroc_cos", ascending=False), n_null=n_null)), ""]
        so = op[op["source"] == "synthetic"] if len(op) else op
        if len(so):
            L += [_opp_table(so), ""] + ["- " + _reading(r) for _, r in so.iterrows()] + [""]

    L += ["## Caveats", "",
          "- Correlation is not mechanism: two genes with a high cosine respond alike to these drugs in these "
          "lines; that may be co-regulation, a shared upstream stress, or a shared cell-state change.",
          "- One time point (24 h): early and late responses are not separated; direct and indirect targets look the "
          "same.",
          "- Cancer cell lines only (50 lines): relations driven by mutated pathways or lost checkpoints (e.g. TP53) "
          "may not hold in normal cells, and tissue-specific programmes are under-represented.",
          "- Relations seen with one drug family only ('one half' in relations) are real in that family but not "
          "replicated across compounds; they are never called novel here.",
          "- Neighbouring genes (same locus, <= 50 kb) and read-through pairs (the 5' gene's transcription running "
          "into the 3' gene) correlate without regulation: they are excluded from 'novel'.",
          "- 'Not known' means no shared HGNC gene group, Hallmark / Reactome pathway or STRING link (score >= 400) "
          "in the cached reference files; the literature may still describe the relation.",
          "- Gene-set AUROCs are against random gene pairs of the space; sets of genes that respond rarely in "
          "Tahoe-100M (few genes in the space) are weak tests, whatever their biology.", ""]
    L += ["## Files", "",
          "control_sets.csv (every tested set), opposite_pairs.csv, module_enrichment.csv, module_labels.csv, "
          "drug_moa.csv, novel_edges.csv, novel_members.csv, metrics.json; README.md documents the columns.", ""]
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    os.replace(tmp, path)


README = """# validation/ - does the vector space recover known biology, and what in it is new?

Written by `tahoemap validate` (tahoemap/validate.py). `cos` = signed cosine of two genes' unit vectors
(embed/gene_unit.npy). Every number is over the genes in the vector space (embed/included_cols.npy). Gene cols are the
row order of atlas/effects/genes.csv; symbols can repeat, so join on col. Read report.md first.

## control_sets.csv - one row per tested gene set
| column | meaning |
|---|---|
| `source` | control (tahoemap/data/control_sets.json), hallmark, reactome (reference/gene_sets.parquet, >= 5 genes in the space), synthetic (only with truth=) |
| `set`, `label`, `note` | set name, short name, curator's note |
| `n_listed`, `n_found`, `n_in_space` | genes listed by the source, found among Tahoe genes, in the vector space (all metrics use these) |
| `mean_cos`, `median_cos`, `frac_pos` | over within-set pairs |
| `auroc_cos`, `auroc_abs` | AUROC of within-set pairs vs 20,000 random pairs of genes in the space, on cos / on abs(cos) (P(set pair > random pair), ties 1/2) |
| `p_random_sets_cos`, `p_random_sets_abs` | share of 200 random gene sets of the same size with an AUROC at least as high ((1 + count) / 201; control, Hallmark, synthetic only) |
| `mean_cos_half1`, `mean_cos_half2` | mean within-set cos in the spaces fitted on each half of the compounds |
| `top_module`, `top_module_share` | the module (nodal map) holding most of the set's genes, and the share of the set's genes in it |
| `top_module_genome_share` | that module's share of all genes in the space (chance level of top_module_share) |
| `top_module_arm_share` | share of the set's genes in that module on its majority arm |
| `best_dd_up`, `best_dd_down` | the 5 drug-doses with the highest / lowest mean pooled z (DD_z) over the set's genes ('drug dose uM (mean z)'; drug-doses flagged unreliable plate only / position not correctable / wells disagree are left out; † = another artifact flag, e.g. toxic) |

## opposite_pairs.csv - programmes expected to move in opposite directions
| column | meaning |
|---|---|
| `source`, `a`, `b`, `note` | the pair (control_sets.json 'opposite_pairs'; synthetic: planted arms) |
| `n_a`, `n_b`, `n_shared_dropped` | genes in the space per set (genes in both sets are dropped) |
| `mean_cross_cos`, `median_cross_cos` | over all cross pairs (a gene of a, a gene of b); expect < 0 |
| `frac_cross_neg` | share of cross pairs with cos < 0 |
| `auroc_anti` | P(cross pair cos < random pair cos) |
| `mean_cross_cos_half1`, `mean_cross_cos_half2` | the same in the two half spaces |
| `within_cos_a`, `within_cos_b` | mean within-set cos of each set |
| `share_same_module` | share of cross pairs in the same module of the nodal map (module 0 = unassigned never counts) |
| `random_same_module` | the same for two random genes (sum of squared module shares) |
| `share_opposite_arms_in_same_module` | among cross pairs in one module, the share on opposite arms |
| `nodal_centroid_dist`, `signed_centroid_dist` | distance between the two sets' centroids on the nodal map (x, y) / signed map (xs, ys), divided by the map's spread sqrt(var x + var y) |
| `reading` | the plain-language reading |

## module_enrichment.csv - modules and arms vs gene sets
Every module ('all'), its + arm and its - arm were tested against every set with >= 5 genes in the space
(hypergeometric upper tail, universe = genes in the space, Benjamini-Hochberg over all tests); rows with overlap >= 2
and p <= 0.05 (or q < 0.05) are kept.
| column | meaning |
|---|---|
| `module`, `arm`, `n_unit` | the module, the unit tested (all / + / -) and its genes |
| `source`, `set`, `set_label`, `n_set` | the set and its genes in the space |
| `overlap`, `expected`, `fold` | genes in both; expected by chance; overlap / expected |
| `p`, `q` | hypergeometric p, BH q over all tests |
| `genes` | overlapping genes (strongest on the module axis first, <= 25) |

## module_labels.csv - one row per module
| column | meaning |
|---|---|
| `module`, `n_genes`, `n_plus`, `n_minus` | the module and its arms |
| `label` | best set with q < 0.05 and >= 3 genes shared (smallest p among sets of <= 300 genes in the space, else any), short name; else 'genes: ...' (top genes of the + arm, then the - arm) |
| `label_source`, `label_set`, `label_arm` | where it came from (control / hallmark / reactome / top genes), the set, the unit (all / + / -) |
| `label_overlap`, `label_n_set`, `label_p`, `label_q` | its test |
| `plus_label`, `plus_set`, `plus_q`, `minus_label`, `minus_set`, `minus_q` | the best set of each arm alone |
| `top_plus`, `top_minus` | top genes of each arm (graph/modules.parquet) |

## drug_moa.csv - mechanism classes (moa_fine) with >= 2 drugs
| column | meaning |
|---|---|
| `moa_fine`, `n_drugs`, `drugs` | the class |
| `n_pairs`, `mean_cos_within` | drug pairs within the class (salt forms of one compound not paired), their mean drug-vector cos |
| `mean_cos_to_other_classes` | mean cos of class members to drugs of other known classes |
| `auroc_within_vs_other` | AUROC of within-class pairs vs (member, other-class drug) pairs |

## novel_edges.csv - candidate new gene-gene relations (relations novel_candidate, one row per pair)
| column | meaning |
|---|---|
| `col_a`, `symbol_a`, `name_a`, `module_a`, `arm_a` | gene a (col_a < col_b), its HGNC name, module and arm |
| `col_b`, `symbol_b`, `name_b`, `module_b`, `arm_b` | gene b |
| `same_module` | both in the same module |
| `cos`, `cos_half1`, `cos_half2`, `evidence`, `fdr` | from relations (full space, the two compound halves, sign-concordance FDR) |
| `same_chrom`, `distance_bp` | genomic position (locus and read-through pairs are excluded) |

## novel_members.csv - guilt by association
A module arm enriched (q < 0.01) for a set of <= 300 genes in the space with >= 3 of them on the arm; a gene of the arm
that the set does not list (by col or by symbol) is kept when its mean cos to the listed members is >= 0.5. Each
gene keeps its 5 most significant sets; genes are ranked by the mean cos for their most significant set.
| column | meaning |
|---|---|
| `col`, `symbol`, `name` | the candidate gene |
| `module`, `arm` | its module arm, which is enriched (q < 0.01) for the set |
| `source`, `set`, `set_label`, `set_q` | the set, and the arm's enrichment q |
| `n_annotated_in_arm`, `n_arm` | the set's genes on the arm; genes on the arm |
| `mean_cos`, `max_cos` | the candidate's cos to the arm's listed members (mean >= 0.5 kept) |
| `mean_cos_half1`, `mean_cos_half2` | the mean in the two half spaces |
| `n_reference_sets` | Hallmark / Reactome sets that already list the gene (0 = no pathway annotation at all) |

## metrics.json
The headline numbers of report.md.
"""


# ----------------------------------------------------------------------------- run
def run(out, truth=None, n_random=N_RANDOM, n_null=N_NULL):
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    vd = folder(out, "validation")
    sp = _Space(out, int(n_random))
    log(f"Validate: {sp.n:,} genes in the space, {sp.n_modules} modules")
    ann = None
    ap = os.path.join(out, "reference", "annotations.parquet")
    if os.path.exists(ap):
        ann = pd.read_parquet(ap).set_index("col").reindex(np.arange(sp.gK))
    ann_name = ann["name"].fillna("").astype(str).to_numpy() if ann is not None and "name" in ann \
        else np.array([""] * sp.gK, dtype=object)
    lookup = _name_index(sp.eg, ann, sp.included)
    sets, opposite = _collect_sets(out, sp.eg, ann, sp.included, lookup, truth)
    n_sets = {"control": sum(s["source"] == "control" for s in sets),
              "reference": sum(s["source"] in ("hallmark", "reactome") for s in sets),
              "synthetic": sum(s["source"] == "synthetic" for s in sets)}

    # ---- per-set metrics
    recs = []
    for st in sets:
        r = {"source": st["source"], "set": st["set"], "label": st["label"], "note": st["note"],
             "n_listed": st["n_listed"], "n_found": st["n_found"]}
        r.update(_set_metrics(sp, st, n_null))
        recs.append(r)
    up, down = _best_drugdoses(out, sp.gK, sets)
    cs = pd.DataFrame(recs)
    cs["best_dd_up"], cs["best_dd_down"] = up, down
    cs["_s"] = cs["source"].map(SOURCES_ORDER).fillna(9)
    cs = cs.sort_values(["_s", "auroc_cos"], ascending=[True, False], na_position="last", kind="mergesort") \
        .drop(columns="_s").reset_index(drop=True)
    write_csv(cs, os.path.join(vd, "control_sets.csv"))
    log(f"  {len(cs)} sets scored ({(time.time() - t0) / 60:.1f} min)")

    # ---- opposite pairs
    key = {(s["source"], s["set"]): s for s in sets}
    orecs = []
    for o in opposite:
        sa, sb = key.get((o["source"], o["a"])), key.get((o["source"], o["b"]))
        if sa is None or sb is None:
            continue
        r = {"source": o["source"], "a": o["a"], "b": o["b"], "note": o["note"]}
        r.update(_opposite(sp, sp.pos[sa["cols"]], sp.pos[sb["cols"]]))
        r["reading"] = _reading(r)
        orecs.append(r)
    op = pd.DataFrame(orecs)
    write_csv(op, os.path.join(vd, "opposite_pairs.csv"))
    for _, r in op.iterrows():
        log(f"  opposite {r['a']}/{r['b']}: cross cos {_f(r['mean_cross_cos'], '{:+.2f}')}, same module "
            f"{_pct(r['share_same_module'])}, nodal map {_f(r['nodal_centroid_dist'])} vs signed "
            f"{_f(r['signed_centroid_dist'])} spreads")

    # ---- module enrichment, labels
    units, tsets, O, P, Q = _enrichment(sp, sets)
    enr = _enrichment_table(sp, sets, units, tsets, O, P, Q)
    write_csv(enr, os.path.join(vd, "module_enrichment.csv"))
    labels = _labels(sp, sets, units, tsets, O, P, Q, out)
    write_csv(labels, os.path.join(vd, "module_labels.csv"))
    log(f"  enrichment: {O.size:,} tests, {int((Q < LABEL_Q).sum()):,} at q < {LABEL_Q}; "
        f"{int((labels['label_source'] != 'top genes').sum()) if len(labels) else 0} of {len(labels)} modules "
        f"labelled")

    # ---- drug check
    drug, drug_tab = _drug_check(out)
    write_csv(drug_tab, os.path.join(vd, "drug_moa.csv"))
    if drug:
        log(f"  drug check: AUROC same moa_fine {_f(drug['all']['auroc'])} ({drug['all']['pos_pairs']} pairs); "
            f"active drugs {_f(drug['active']['auroc'])}")

    # ---- novel candidates
    n_ref_sets = np.zeros(sp.gK, dtype=np.int64)
    for s in sets:
        if s["source"] in ("hallmark", "reactome"):
            n_ref_sets[s["cols"]] += 1
    edges = _novel_edges(out, sp, ann_name)
    write_csv(edges, os.path.join(vd, "novel_edges.csv"))
    members = _novel_members(sp, sets, units, tsets, Q, ann_name, n_ref_sets)
    write_csv(members, os.path.join(vd, "novel_members.csv"))
    log(f"  novel: {len(edges):,} edges, {members['col'].nunique() if len(members) else 0:,} module members")

    # ---- metrics, report
    def summ(src):
        d = cs[(cs["source"] == src) & (cs["n_in_space"] >= 2)]
        return {"n_sets": int(len(d)), "median_auroc_cos": float(d["auroc_cos"].median()) if len(d) else None,
                "median_auroc_abs": float(d["auroc_abs"].median()) if len(d) else None,
                "n_auroc_cos_ge_0.6": int((d["auroc_cos"] >= 0.6).sum()),
                "n_p_random_le_0.05": int((d["p_random_sets_cos"] <= 0.05).sum())}

    def per_set(src):
        d = cs[cs["source"] == src]
        return {r["set"]: {k: r[k] for k in ("n_in_space", "mean_cos", "auroc_cos", "auroc_abs", "p_random_sets_cos",
                                             "top_module", "top_module_share")} for _, r in d.iterrows()}

    def opp(src):
        d = op[op["source"] == src] if len(op) else op
        return [{k: r[k] for k in ("a", "b", "n_a", "n_b", "mean_cross_cos", "frac_cross_neg", "share_same_module",
                                   "random_same_module", "share_opposite_arms_in_same_module",
                                   "nodal_centroid_dist", "signed_centroid_dist")} for _, r in d.iterrows()]

    metrics = {"version": VERSION, "genes_in_space": int(sp.n), "dims": int(sp.U.shape[1]),
               "modules": int(sp.n_modules), "random_pairs": int(len(sp.bg_cos)),
               "random_pair_cos_sd": float(np.std(sp.bg_cos)) if len(sp.bg_cos) else None,
               "control_sets": dict(summ("control"), per_set=per_set("control")),
               "hallmark": summ("hallmark"), "reactome": summ("reactome"),
               "opposite_pairs": opp("control"), "drug_check": drug,
               "module_labels": {"modules": int(len(labels)),
                                 "labelled": int((labels["label_source"] != "top genes").sum()) if len(labels) else 0,
                                 "enrichment_tests": int(O.size), "tests_q_lt_0.05": int((Q < LABEL_Q).sum())},
               "novel": {"edges": int(len(edges)),
                         "genes_with_novel_edge": int(len(set(edges["col_a"]) | set(edges["col_b"])))
                         if len(edges) else 0,
                         "member_rows": int(len(members)),
                         "member_genes": int(members["col"].nunique()) if len(members) else 0},
               "reference": bool(n_sets["reference"])}
    if n_sets["synthetic"]:
        metrics["synthetic"] = dict(summ("synthetic"), per_set=per_set("synthetic"), opposite_pairs=opp("synthetic"))
    write_json(metrics, os.path.join(vd, "metrics.json"))
    _report(os.path.join(vd, "report.md"), {"sp": sp, "cs": cs, "op": op, "labels": labels, "edges": edges,
                                             "members": members, "drug": drug, "drug_tab": drug_tab,
                                             "n_sets": n_sets, "n_null": n_null})
    tmp = os.path.join(vd, "README.md.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(README)
    os.replace(tmp, os.path.join(vd, "README.md"))

    info = {"version": VERSION, "genes": int(sp.n), "sets": n_sets, "modules": int(sp.n_modules),
            "modules_labelled": metrics["module_labels"]["labelled"],
            "control_median_auroc_cos": metrics["control_sets"]["median_auroc_cos"],
            "drug_moa_auroc": drug.get("all", {}).get("auroc") if drug else None,
            "novel_edges": int(len(edges)), "novel_member_genes": metrics["novel"]["member_genes"],
            "truth": bool(truth), "minutes": round((time.time() - t0) / 60, 2)}
    stamp_stage(out, "validate", VERSION, info)
    log(f"Validate done: report in {os.path.join(vd, 'report.md')} ({info['minutes']} min)")
    return info
