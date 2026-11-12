"""validate - does the vector space / nodal map recover known biology, and what in it is new?

Every test runs on the genes in the vector space (embed/included_cols.npy); cos = signed cosine of their unit vectors
(embed/gene_unit.npy), i.e. the correlation of two genes' denoised response profiles over (drug-dose, line) contexts.

  gene sets        the curated control sets of tahoemap/data/control_sets.json (literature programmes, no network),
                   plus MSigDB Hallmark and Reactome sets (reference/gene_sets.parquet) with >= 5 genes in the space.
                   Per set: mean within-set cos; AUROC of the within-set pairs against 20,000 random pairs of genes in
                   the space, on cos and on |cos| (Mann-Whitney: P(set pair > random pair), ties count 1/2; 0.5 = no
                   better than random); an empirical p of that AUROC against random gene sets of the same size
                   (control, Hallmark and synthetic sets); the share of members in the set's most common module of
                   the nodal map; the drug-doses that raise / lower the set most (mean pooled DD_z over members;
                   every drug-dose in its ranked place, one with an artifact flag marked '⚠' with its flags).
  opposite pairs   programmes expected to move in opposite directions (control_sets.json 'opposite_pairs'): mean
                   cross-set cos (expect < 0), share of cross pairs with cos < 0, share of cross pairs in the same
                   module (expect high: the nodal map is built on |cos|), and the distance between the two sets'
                   centroids on the nodal map (x, y) and on the signed map (xs, ys), each divided by that map's spread
                   (sqrt(var x + var y)), and the neighbourhood mixing of the two sets on each map (map_mixing: 1 = as
                   mixed as chance, 0 = no gene of one set among the nearest map neighbours of the other). Opposite
                   genes should share neighbourhoods on the nodal map and none on the signed map. (t-SNE keeps
                   neighbourhoods, not long distances: how far apart two separate islands land varies from machine
                   to machine, so the verdict rests on the mixing, not on the signed-map centroid distance.)
  module labels    every module, and each of its arms, against every set: hypergeometric upper tail (universe =
                   genes in the space), Benjamini-Hochberg over all tests. Version 7 (README 'module_labels.csv'):
                   candidates q < 0.05 and >= 3 shared genes; strong = q < 0.01, >= 5x the chance overlap and >= 3
                   independent shared genes (near-identical copies that can share reads count once), else weak; a
                   curated control set that is not weak wins over Hallmark / Reactome, else the smallest p as before.
                   Label = strong set label, else the drug class that drives the module (its 10 strongest drug-doses,
                   module pooled z >= 3: >= 3 compounds of one class; ChEMBL's classes first, then Tahoe's moa_fine),
                   else 'weak: ...', else a lineage label, else the top genes; alerts for read-sharing copies,
                   lineage-restricted modules and Y-chromosome genes.
  drug check       AUROC of drug-vector cos (embed/drug_vectors.npy) for drug pairs sharing a class against pairs
                   that do not, with two class sources side by side: Tahoe's moa_fine ('unclear' / 'unknown' left
                   out) and the mechanism classes (drug_classes.json labels or ChEMBL mechanism texts); one molecule
                   never paired; plus the agreement of the two annotations, every disagreement listed.
  neighbouring     the tables stage's neighbouring-well rule (tables/info.json neighbour_rule, drugdoses nb_*),
  wells            shown: placements, tiers against the chance rate, every drug-dose with a tier.
  novel            (a) relations' novel_candidate pairs (reproduced in both compound halves, fdr <= 0.05, |cos| >= 0.5,
                   no shared gene group / pathway / STRING link, not the same locus, no read-through risk), one row
                   per unordered pair, with relations' lineage-pair and read-sharing columns; (b) guilt by
                   association: members of a module arm enriched for a set (q < 0.01; sets of <= 300 genes) that the
                   set does not list, with mean cos >= 0.5 to the arm's listed members.
  line-selective   control_sets.json 'line_controls' (KRAS G12C x Adagrasib, BRAF V600E x BRAF inhibitors, NR3C1-high
  responses        lines x glucocorticoids, BT-474 x ERBB2 drugs, TP53 not recorded x TOP1 / TOP2 poisons; cited):
                   AUROC of the group's line selectivity (tables/drug_line_response sel_z; and response strength)
                   with a permutation p.
  synthetic truth  only with truth=<ground_truth.json of tests/make_synthetic_tahoe.py>: the generator's planted gene
                   sets and opposite pairs, with the same metrics; planted line-selective and direction answers.
  direction        the direction stage's controls (direction/controls.json, edges.parquet; when the stage ran): the
                   positive controls recovered (TP53 -> the p53 targets with their ranks, counted or not and why,
                   TP53 -> cells and response strength under DNA-damaging drugs, KRAS G12C -> Adagrasib, KEAP1 ->
                   NRF2 targets), per kind the edges written next to the false or non-specific edges the controls
                   expect (random pseudo-genotype groups; random genes and line sets for the natural knockouts; the
                   level tests with permuted levels), the grade-A arrows' group false shares, the same-locus check,
                   the counts by grade, and with truth the generator's planted direction answers.

Alerts: nothing is left out of a list for a flag ("if there is a reason to doubt, do not remove, rather alert"). An
item with a reason for doubt keeps its ranked place and carries '⚠' with the reason in plain words: a drug-dose with
an artifact flag in the best drug-dose lists, a novel pair or module member with a gene that is in the vector space
only through drug-doses that carry an alert (embed genes.parquet evidence_flagged_only; column alert), a drug with no
trustworthy dose in the drug check. A list cut at N (the report's top 25, the 5 best drug-doses) also keeps the N
strongest items without an alert that the flagged ones would push below the cut (embed.capped).

Outputs in OUT/validation/ (README.md there documents every column):
    report.md, metrics.json, control_sets.csv (every tested set, all sources), opposite_pairs.csv,
    module_enrichment.csv, module_labels.csv, drug_moa.csv, novel_edges.csv, novel_members.csv, line_controls.csv
"""

import json
import os
import re
import time
import warnings

import numpy as np
import pandas as pd

from . import tlib as T
from .common import (ARTIFACT_FLAGS, NB_TOP, TL_DD, fmt_q, folder, has_artifact, log, marked_names,
                     read_effects_index, replace_file, stable_seed, stamp_stage, write_csv, write_json)
from .embed import capped

VERSION = 9                 # 3: flagged items stay in their ranked place, with an alert; 4: the direction section;
#                             5: drug_moa.csv lists every drug of a class (was the first 12); 6: module_enrichment.csv
#                             lists every overlapping gene (was the first 25); report.md marks every cut name ('…');
#                             7: label priority, weak labels, drug-class and lineage labels, module alerts, neighbouring
#                             wells, translation inhibitors, Tahoe and ChEMBL drug check, line-selective controls,
#                             direction controls
#                             8: drug-class labels as plural noun phrases ('raised by glucocorticoid receptor
#                             agonists'); report wording (a gene not measured, an assessment not run, the run's
#                             line count, µM)
#                             9: README and report call the neighbouring-well top-dose tier 'an alert, not an artifact
#                             flag' (as tables and the explorer do); 'translation inhibitor' stays a caveat
N_RANDOM = 20_000           # random gene pairs: the background of every AUROC
N_NULL = 200                # random gene sets per set size for the empirical p of a set's AUROC
NULL_SOURCES = ("control", "hallmark", "synthetic")
NULL_POOL = 4000            # random sets are drawn from this many random genes (their cosines held in memory: 64 MB)
MIN_SET = 5                 # Hallmark / Reactome sets need this many genes in the space (enrichment: every source)
LABEL_Q = 0.05
LABEL_MIN_OVERLAP = 3
LABEL_MAX_SET = 300         # labels prefer specific sets (as relations' PATHWAY_MAX); guilt by association uses
                            # only these
CURATED_FIRST = True        # version 7: a curated control set that is a candidate and not weak wins over Hallmark and
                            # Reactome (before, the smallest p won whatever the source: module 113 of the real run,
                            # the metallothionein genes, was named 'hypoxia')
LABEL_STRONG_Q = 0.01       # a set label is strong when q < this, ...
LABEL_STRONG_FOLD = 5.0     # ... the overlap is >= this many times the chance overlap, and ...
#                             ... >= LABEL_MIN_OVERLAP shared genes remain when each group of near-identical copies
#                             (read-sharing, relations.read_sharing_pairs) counts once; else it is 'weak: ...'
LABEL_GENES = 5             # the genes a label names (a set label: its first shared genes; else 3 + and 2 - top genes)
DRIVER_TOP_DD = 10          # driving drug class: among the module's 10 strongest drug-doses (module pooled z) ...
DRIVER_MIN_Z = 3.0          # ... with a signed module z >= this (flagged drug-doses included) ...
DRIVER_MIN_DRUGS = 3        # ... the class with the most distinct compounds, >= this many (or >= 2 when that is every
                            # compound of the class in the screen)
DRIVER_MAX_SHARE = 0.25     # a class that is the best one in more than this share of the modules is too general to
                            # name a module: it stays in label_drugs and drivers_*, and the label takes the module's
                            # best other class (the real run: the 2 translation inhibitors lead 103 of 235 modules)
READSHARE_MODULE_SHARE = 0.2   # read-sharing alert: >= this share of the members are near-identical copies (or >= 2
                               # of the label's named genes are copies of one another)
LINEAGE_MAX_SHARE = 0.6     # lineage alert: the median member is expressed in < this share of the lines (relations'
                            # lineage rule)
LINEAGE_CORE = 0.5          # lines_core: lines expressing at least this share of the members
ORGAN_P = 0.05              # lineage_organs: organs enriched among lines_core (hypergeometric p <= this)
CHRY_ANY = 3                # Y-chromosome alert: >= 3 members on chrY, or ...
CHRY_MIN = 2                # ... >= 2 and ...
CHRY_SHARE = 0.1            # ... >= 10% of the members
TAG_READSHARE = "⚠ read-sharing copies"
TAG_LINEAGE = "⚠ lineage-restricted"
TAG_CHRY = "⚠ Y-chromosome genes"
TL_WORDS = "translation inhibitor: rise may be mRNA stabilisation"   # a translation inhibitor in a raise list
TL_CANDIDATE = re.compile(r"protein synthesis|ribosom", re.I)        # TL candidates outside the class (not used by
TL_NOT = re.compile(r"bacteri", re.I)                                # the rule): ChEMBL mechanism text
TL_TAHOE = "Protein synthesis inhibitor"                             # ... or this Tahoe moa_fine
NB_TABLE_MAX = 200          # report table of neighbouring-well drug-doses: all of them up to this; above, the strongest
                            # by J with 'k of N' (all in tables/drugdoses.parquet)
LINE_PERM = 2000            # line-selective controls: label shuffles for the permutation p of the AUROC
NOVEL_TOP = 25              # report: top novel pairs shown per list ('k of N'; all in novel_edges.csv)
NOVEL_LINEAGE = ["n_lines_a", "n_lines_b", "lines_shared", "lines_jaccard", "lineage_pair", "lineage_p", "read_sharing",
                 "read_sharing_risk"]    # copied from relations/gene_relations.parquet (relations version 5)
LINEAGE_P_STRONG = 0.01     # a lineage pair with lineage_p >= this is no stronger than 1 in 100 pairs expressed in
                            # equally overlapping lines
GBA_Q = 0.01
GBA_COS = 0.5
GBA_MIN_ANNOT = 3
GBA_PER_GENE = 5            # novel_members.csv keeps each gene's 5 most significant sets
OPP_COS = -0.1              # 'opposite': mean cross-set cos <= this
TOGETHER = 0.5              # 'together on the nodal map': centroid distance <= this many spreads, and the two sets more
                            # mixed there than on the signed map
MIX_K = 5                   # map_mixing: nearest map neighbours per gene
MIX_APART = 0.25            # 'apart on the signed map': mixing <= this (0 = no shared neighbourhood, 1 = chance)
ENRICH_KEEP_P = 0.05        # module_enrichment.csv keeps tests with overlap >= 2 and p <= this
TOP_DD = 5
ALERT = "⚠"
CC_FLAG = "cell-cycle shift"  # the drug-dose flag whose share of a set's change the best drug-dose lists give
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
        # genes in the space only through drug-doses that carry an alert (False: an older embed stage)
        self.flagged_only = self.eg["evidence_flagged_only"].fillna(False).astype(bool).to_numpy() \
            if "evidence_flagged_only" in self.eg else np.zeros(self.gK, dtype=bool)
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


def _set_means(M, X):
    """sets x drug-doses: the mean of X (drug-doses x genes) over each set's members (M: genes x sets), NaN-aware."""
    F = np.isfinite(X).astype(np.float32)
    X = np.nan_to_num(X, nan=0.0)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.asarray(M.T @ X.T) / np.asarray(M.T @ F.T)


def _cc_shares(out, fxd, dd, M, gK, cc):
    """For the drug-doses whose flags include 'cell-cycle shift' (cc, bool per drug-dose): (share, cleared), sets x
    drug-doses (NaN / False elsewhere), by the tables stage's rule (tables.cc_rule) applied to each set's mean change:
    the mean pooled lfc over its members against what the shift predicts for them, the drug-dose's S / G2M module lfc
    times the members' mean cell-cycle slopes (tables/genes.parquet cc_slope_S, cc_slope_G2M). None when the slopes,
    the module values or the rule are missing (then the flag is shown as it is)."""
    gp = os.path.join(out, "tables", "genes.parquet")
    if not cc.any() or not os.path.exists(gp) or not {"S_PHASE_lfc", "G2M_PHASE_lfc"} <= set(dd.columns):
        return None
    import pyarrow.parquet as pq
    if not {"col", "cc_slope_S", "cc_slope_G2M"} <= set(pq.ParquetFile(gp).schema_arrow.names):
        return None
    try:
        from .tables import cc_rule
    except ImportError:
        return None
    tg = pd.read_parquet(gp, columns=["col", "cc_slope_S", "cc_slope_G2M"]).set_index("col").reindex(np.arange(gK))
    rows = np.flatnonzero(cc)
    slopes = tg[["cc_slope_S", "cc_slope_G2M"]].to_numpy(np.float32).T             # 2 x genes
    mS, mG = _set_means(M, slopes).T                                               # per set: mean slopes
    S = pd.to_numeric(dd["S_PHASE_lfc"], errors="coerce").to_numpy(np.float64)[rows]
    G = pd.to_numeric(dd["G2M_PHASE_lfc"], errors="coerce").to_numpy(np.float64)[rows]
    lfc = np.asarray(np.load(os.path.join(fxd, "DD_lfc.npy"), mmap_mode="r")[rows, :gK], dtype=np.float32)
    sh, cl = cc_rule(_set_means(M, lfc), mS[:, None] * S[None, :] + mG[:, None] * G[None, :])
    share = np.full((M.shape[1], len(dd)), np.nan)
    cleared = np.zeros((M.shape[1], len(dd)), dtype=bool)
    share[:, rows], cleared[:, rows] = sh, cl
    return share, cleared


def _flags_of_record(out, dd):
    """The drug-doses' flags of record (tables.dd_flags_of_record: the atlas flags plus 'like a neighbouring well' and
    'translation inhibitor'), else the atlas flags of drugdose.csv (an output made before tables version 5)."""
    try:
        from .tables import dd_flags_of_record
        f = np.asarray(dd_flags_of_record(out), dtype=object)
        if len(f) == len(dd):
            return np.array([str(x) if isinstance(x, str) else "" for x in f], dtype=object)
    except Exception as e:  # noqa: BLE001
        log(f"  flags of record not read ({type(e).__name__}: {e}); using the atlas flags")
    return dd["flags"].fillna("").astype(str).to_numpy(dtype=object) if "flags" in dd else \
        np.full(len(dd), "", dtype=object)


def _best_drugdoses(out, gK, sets):
    """Per set: the TOP_DD drug-doses with the highest / lowest mean pooled DD_z over its members, every drug-dose in
    its ranked place. Flags are the flags of record (tables.dd_flags_of_record). One with an artifact flag
    (common.ARTIFACT_FLAGS, technically untrustworthy ones and 'like a neighbouring well' included) is followed by '⚠'
    and its flags in plain words; for a cell-cycle shift also the share of the set's mean change that the shift would
    explain (_cc_shares), and a shift that is not the explanation by the tables stage's rule is named without '⚠'.
    Named without '⚠': the top-dose alert 'like a neighbouring well (top dose)' (an alert, not an artifact flag),
    and in the raise lists the caveat of a member of the translation-inhibitor class, '(translation inhibitor: rise
    may be mRNA stabilisation)'. When the TOP_DD
    strongest include drug-doses with an alert, the TOP_DD strongest without one are listed too, all in ranked order
    (embed.capped). When a translation inhibitor is among the TOP_DD strongest raisers, the list 'without translation
    inhibitors' (the TOP_DD strongest other drug-doses, same rule and format) is returned too. Returns the lists up
    and down, per set how many entries of each carry an alert, and the raise lists without translation inhibitors
    ('' where none is needed)."""
    from scipy import sparse
    fxd = os.path.join(out, "atlas", "effects")
    dd = read_effects_index(fxd)["drugdose"]
    flags = _flags_of_record(out, dd)
    toks = [[t for t in str(f).split("; ") if t] for f in flags]
    art = [[t for t in tk if t in ARTIFACT_FLAGS] for tk in toks]
    nbtop = np.array([NB_TOP in tk for tk in toks], dtype=bool)
    tl = np.array([TL_DD in tk for tk in toks], dtype=bool)
    cc = np.array([CC_FLAG in a for a in art], dtype=bool)
    lab = (dd["drug"].astype(str) + " " + dd["dose"].astype(str) + " uM").to_numpy()
    rows, cols = [], []
    for j, st in enumerate(sets):
        rows += list(st["cols"])
        cols += [j] * len(st["cols"])
    M = sparse.csr_matrix((np.ones(len(rows), dtype=np.float32), (rows, cols)), shape=(gK, len(sets)))
    Z = np.asarray(np.load(os.path.join(fxd, "DD_z.npy"), mmap_mode="r")[:, :gK], dtype=np.float32)
    mean = _set_means(M, Z)                                                         # sets x drug-doses
    del Z
    ccs = _cc_shares(out, fxd, dd, M, gK, cc)
    other = np.array([any(a != CC_FLAG for a in x) for x in art], dtype=bool)     # an alert whatever the set

    def entry(j, i, alert, up):
        """The text of drug-dose i in set j's list."""
        txt = [a for a in art[i] if a != CC_FLAG]
        if cc[i]:
            sh = ccs[0][j, i] if ccs is not None else np.nan
            txt.append(f"{CC_FLAG}, explains ~{int(round(100 * sh))}% of this change" if np.isfinite(sh) else CC_FLAG)
        notes = ([NB_TOP] if nbtop[i] else []) + ([TL_WORDS] if tl[i] and up else [])
        body = ((f", {ALERT} " if alert else ", ") + ", ".join(txt) if txt else "") + \
            ("".join(f", {n}" for n in notes))
        return f"{lab[i]} ({mean[j, i]:+.1f}{body})"

    up, down, n_alert, up_no_tl = [], [], [], []
    for j in range(len(sets)):
        v = mean[j]
        fin = np.where(np.isfinite(v))[0]
        if not len(fin):
            up.append("")
            down.append("")
            up_no_tl.append("")
            n_alert.append((0, 0))
            continue
        alert = other | (cc & ~ccs[1][j]) if ccs is not None else other | cc
        o = fin[np.argsort(-v[fin], kind="mergesort")]
        res = []
        for order, is_up in ((o, True), (o[::-1], False)):
            shown = capped(order, ~alert, TOP_DD)
            res.append(("; ".join(entry(j, i, alert[i], is_up) for i in shown), int(alert[shown].sum())))
        up.append(res[0][0])
        down.append(res[1][0])
        n_alert.append((res[0][1], res[1][1]))
        if tl[o[:TOP_DD]].any():
            o2 = o[~tl[o]]
            up_no_tl.append("; ".join(entry(j, i, alert[i], True) for i in capped(o2, ~alert, TOP_DD)))
        else:
            up_no_tl.append("")
    return up, down, n_alert, up_no_tl


# ----------------------------------------------------------------------------- opposite pairs
def map_mixing(xy, ia, ib, k=MIX_K):
    """How mixed two gene sets are on a 2-D map (rows ia and ib of xy): for each gene of either set, the share of its
    k nearest map neighbours among the genes of both sets that belong to the other set, divided by that share under
    random labels (other set's size / (n - 1)); the mean over each set, averaged over the two sets. 1 = as mixed as
    chance, 0 = no gene has a neighbour from the other set. NaN when a set has fewer than 2 placed genes."""
    from sklearn.neighbors import NearestNeighbors
    ia, ib = np.asarray(ia, dtype=np.int64), np.asarray(ib, dtype=np.int64)
    P = np.asarray(xy, dtype=np.float64)
    ia, ib = ia[np.isfinite(P[ia]).all(1)], ib[np.isfinite(P[ib]).all(1)]
    na, nb = len(ia), len(ib)
    if na < 2 or nb < 2:
        return float("nan")
    lab = np.r_[np.zeros(na, bool), np.ones(nb, bool)]
    pts = P[np.r_[ia, ib]]
    n = na + nb
    kk = min(k, n - 1)
    _, nbr = NearestNeighbors(n_neighbors=kk + 1).fit(pts).kneighbors(pts)
    nbr = nbr[:, 1:]                                         # without the gene itself
    other = (lab[nbr] != lab[:, None]).mean(axis=1)
    expect = np.where(lab, na, nb) / (n - 1)
    r = other / expect
    return float((r[~lab].mean() + r[lab].mean()) / 2)


def _opposite(sp, pa, pb):
    shared = np.intersect1d(pa, pb)
    pa = np.setdiff1d(pa, shared)
    pb = np.setdiff1d(pb, shared)
    r = {"n_a": len(pa), "n_b": len(pb), "n_shared_dropped": len(shared), "mean_cross_cos": np.nan,
         "median_cross_cos": np.nan, "frac_cross_neg": np.nan, "auroc_anti": np.nan, "mean_cross_cos_half1": np.nan,
         "mean_cross_cos_half2": np.nan, "within_cos_a": np.nan, "within_cos_b": np.nan,
         "share_same_module": np.nan, "random_same_module": sp.p_same_module,
         "share_opposite_arms_in_same_module": np.nan, "nodal_centroid_dist": np.nan,
         "signed_centroid_dist": np.nan, "nodal_mixing": np.nan, "signed_mixing": np.nan}
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
    r["nodal_mixing"], r["signed_mixing"] = map_mixing(sp.xy, pa, pb), map_mixing(sp.xys, pa, pb)
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
    mn, ms = r.get("nodal_mixing", np.nan), r.get("signed_mixing", np.nan)
    if np.isfinite(dn) and np.isfinite(ds) and np.isfinite(mn) and np.isfinite(ms):
        s += (f". Neighbourhood mixing (1 = as mixed as chance, 0 = none): {mn:.2f} on the nodal map vs {ms:.2f} on "
              f"the signed map; centroid distance {dn:.2f} vs {ds:.2f} map spreads")
        together = dn <= TOGETHER and mn > ms
        apart = ms <= MIX_APART
        if mc <= OPP_COS and together and apart:
            s += " - together on the nodal map, apart on the signed map, as intended."
        elif mc <= OPP_COS and not together:
            s += " - opposite in the vector space, but the nodal map does not bring them together."
        elif mc <= OPP_COS:
            s += " - together on the nodal map, but the signed map does not keep them apart."
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


def _clip(text, n):
    """A name for a report table: whole when it has n characters or fewer, else its first n - 1 and '…' (the CSV the
    table comes from holds it whole)."""
    t = "" if text is None or (isinstance(text, float) and not np.isfinite(text)) else str(text)
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def _arm_names(top, n_arm, k=5):
    """An arm's first k genes (marked_names: an alerted gene keeps its place), and 'k of N' when the arm has more."""
    names = marked_names(top, k)
    if not names:
        return "-"
    try:
        n = int(n_arm)
    except (TypeError, ValueError):
        n = len(names)
    return ", ".join(names) + (f" … ({len(names)} of {n})" if n > len(names) else "")


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
                     "p": P[a, b], "q": Q[a, b], "genes": ", ".join(sp.sym[sp.inc[ov]]),
                     "_cols": [int(x) for x in sp.inc[ov]], "_n_listed": st.get("n_listed", np.nan)})
    cols = ["module", "arm", "n_unit", "source", "set", "set_label", "n_set", "overlap", "expected", "fold", "p",
            "q", "genes", "_cols", "_n_listed"]
    df = pd.DataFrame(rows, columns=cols)
    if len(df):
        df["_a"] = df["arm"].map({"all": 0, "+": 1, "-": 2})
        df = df.sort_values(["module", "_a", "p"], kind="mergesort").drop(columns="_a").reset_index(drop=True)
    return df


def read_sharing_groups(cols, pairs):
    """Groups of near-identical copies among the gene cols `cols`: the connected groups (>= 2 genes) of the read-sharing
    pairs (relations.read_sharing_pairs: {(lo, hi): ...} or any iterable of col pairs) whose two genes are both in
    cols. Each group is a list of cols; groups are ordered largest first, then by their first col."""
    cs = {int(c) for c in cols}
    parent = {}

    def find(x):
        root = x
        while parent.get(root, root) != root:
            root = parent[root]
        while parent.get(x, x) != root:
            parent[x], x = root, parent[x]
        return root
    for a, b in pairs:
        a, b = int(a), int(b)
        if a in cs and b in cs and a != b:
            ra, rb = find(a), find(b)
            parent.setdefault(ra, ra)
            parent.setdefault(rb, rb)
            if ra != rb:
                parent[max(ra, rb)] = min(ra, rb)
    groups = {}
    for c in parent:
        groups.setdefault(find(c), []).append(c)
    out = [sorted(g) for g in groups.values() if len(g) >= 2]
    return sorted(out, key=lambda g: (-len(g), g[0]))


def independent_overlap(cols, group_of):
    """The shared genes `cols` counted with each group of read-sharing copies once (group_of: col -> group id)."""
    seen, n = set(), 0
    for c in cols:
        g = group_of.get(int(c))
        if g is None:
            n += 1
        elif g not in seen:
            seen.add(g)
            n += 1
    return n


def weak_reasons(q, fold, indep):
    """Why a set label is weak ([] = strong): q >= LABEL_STRONG_Q, fold < LABEL_STRONG_FOLD, or fewer than
    LABEL_MIN_OVERLAP shared genes once each group of read-sharing copies counts once."""
    why = []
    if not (np.isfinite(q) and q < LABEL_STRONG_Q):
        why.append(f"q {fmt_q(q)} is not below {LABEL_STRONG_Q:g}")
    if not (np.isfinite(fold) and fold >= LABEL_STRONG_FOLD):
        why.append(f"{_f(fold, '{:.1f}')}x the chance overlap, under {LABEL_STRONG_FOLD:g}x")
    if indep < LABEL_MIN_OVERLAP:
        why.append(f"{indep} independent shared gene{'' if indep == 1 else 's'} (near-identical copies that can share "
                   f"reads count once), under {LABEL_MIN_OVERLAP}")
    return why


def weak_text(short, overlap, n_set, q):
    """'weak: {short name} ({overlap} of {n_set} genes, q {q:.0e})'."""
    return f"weak: {short} ({int(overlap)} of {int(n_set)} genes, q {fmt_q(q)})"


def label_candidates(enr, group_of):
    """The candidate set labels of every module unit: rows of module_enrichment (with '_cols', the shared gene cols)
    with q < LABEL_Q and overlap >= LABEL_MIN_OVERLAP, plus independent (shared genes, a read-sharing group counted
    once; group_of: {module: {col: group id}}), weak (bool) and weak_why (text)."""
    c = enr[(enr["q"] < LABEL_Q) & (enr["overlap"] >= LABEL_MIN_OVERLAP)].copy()
    if not len(c):
        return c.assign(independent=pd.Series(dtype=np.int64), weak=pd.Series(dtype=bool),
                        weak_why=pd.Series(dtype=object))
    ind, weak, why = [], [], []
    for m, cols, q, fold in zip(c["module"], c["_cols"], c["q"], c["fold"]):
        k = independent_overlap(cols, group_of.get(int(m), {}))
        w = weak_reasons(float(q), float(fold), k)
        ind.append(k)
        weak.append(bool(w))
        why.append("; ".join(w))
    return c.assign(independent=np.array(ind, dtype=np.int64), weak=np.array(weak, dtype=bool), weak_why=why)


def choose_set(c):
    """The set label among candidate rows c (one module, or one arm), or None. CURATED_FIRST: when a curated control
    set is a candidate that is not weak, only control candidates compete. Then (as before) sets of <= LABEL_MAX_SET
    genes in the space when there is one, the smallest p (4 significant digits; Reactome repeats one gene list under
    many names), then curated source first, the smaller set (in the space, then at the source), the larger overlap,
    the set name, the whole module before its arms."""
    if c is None or not len(c):
        return None
    if CURATED_FIRST:
        ctl = c[(c["source"] == "control") & ~c["weak"].astype(bool)]
        if len(ctl):
            c = ctl
    spec = c[c["n_set"] <= LABEL_MAX_SET]
    if len(spec):
        c = spec
    nl = pd.to_numeric(c["_n_listed"], errors="coerce") if "_n_listed" in c else pd.Series(np.nan, index=c.index)
    key = pd.DataFrame({"p": [float(f"{x:.4g}") for x in c["p"]], "s": c["source"].map(SOURCES_ORDER).fillna(9),
                        "n": c["n_set"], "nl": nl.fillna(10 ** 9), "o": -c["overlap"], "set": c["set"].astype(str),
                        "a": c["arm"].map({"all": 0, "+": 1, "-": 2}).fillna(3)}, index=c.index)
    return c.loc[key.sort_values(list(key.columns), kind="mergesort").index[0]]


def drug_class_lists(out, drugs, moa):
    """Per drug-dose, its mechanism classes from two sources (README 'module_labels.csv'): 'ChEMBL' = the class labels
    of tahoemap/data/drug_classes.json the drug belongs to (mechanisms.drug_classes: ChEMBL mechanism rules, WHO ATC
    via ChEMBL and cited code constants), or for a drug in none of them its ChEMBL mechanism texts; 'Tahoe' = Tahoe's
    moa_fine ('', 'unclear', 'unknown' ignored). drugs, moa: per drug-dose. Returns ({'ChEMBL': [[names]], 'Tahoe':
    [[names]]}, the ChEMBL source's name: 'ChEMBL' or 'code constants' when ChEMBL did not load)."""
    from . import mechanisms as MC
    try:
        K = MC.drug_classes(out)
        ann = MC.drug_annotations(out)
    except Exception as e:  # noqa: BLE001  (no drug table at all: no ChEMBL classes)
        log(f"  drug classes not read ({type(e).__name__}: {e})")
        K = pd.DataFrame(columns=["drug", "class", "label"])
        ann = pd.DataFrame(columns=["drug", "chembl_mechanisms", "annotation_status"])
    order = {k: i for i, k in enumerate(MC.class_order())}
    lab = {}
    for d, k, lb in sorted(zip(K["drug"].astype(str), K["class"].astype(str), K["label"].astype(str)),
                           key=lambda t: (t[0], order.get(t[1], 99))):
        lab.setdefault(d, [])
        if lb not in lab[d]:
            lab[d].append(lb)
    mech = {}
    if "chembl_mechanisms" in ann:
        for d, t in zip(ann["drug"].astype(str), ann["chembl_mechanisms"].fillna("").astype(str)):
            mech[d] = list(dict.fromkeys(x.strip() for x in t.split("; ") if x.strip().lower() not in NO_MOA))
    st = ann["annotation_status"].fillna("").astype(str) if "annotation_status" in ann else pd.Series([], dtype=str)
    loaded = bool(len(st)) and not (st == MC.NOT_LOADED).all()
    chem = [lab.get(str(d)) or mech.get(str(d), []) for d in drugs]
    tah = [[] if str(m).strip().lower() in NO_MOA else [str(m).strip()] for m in moa]
    return {"ChEMBL": chem, "Tahoe": tah}, ("ChEMBL" if loaded else "code constants")


def _same_class(chembl_name, tahoe_name):
    """Do a ChEMBL-source class and a Tahoe moa_fine name the same class? Equal words (case ignored), or the Tahoe
    label maps to that class in drug_classes.json 'tahoe_moa_classes' (a comparison table, never a class rule)."""
    if str(chembl_name).casefold() == str(tahoe_name).casefold():
        return True
    from . import mechanisms as MC
    rules = MC.load_rules()
    keys = (rules.get("tahoe_moa_classes") or {}).get(str(tahoe_name), [])
    return any(MC.class_info(k).get("label") == chembl_name for k in keys if isinstance(k, str))


def _best_classes(Z, salt, names, classes, alert, size, exclude, n_top, min_z, min_drugs):
    """One pass of driving_classes: per module and direction the best qualifying class of each source, leaving out
    the (source, class) pairs in exclude."""
    rows, leads = [], {}
    for m in range(Z.shape[0]):
        rec = {}
        for sgn, d in ((1.0, "up"), (-1.0, "down")):
            v = sgn * np.nan_to_num(Z[m], nan=-np.inf)
            top = [int(i) for i in np.argsort(-v, kind="mergesort")[:n_top] if v[i] >= min_z]
            rec[d] = {}
            for src, cl in classes.items():
                per = {}
                for i in top:
                    for c in cl[i]:
                        if (src, c) not in exclude:
                            per.setdefault(c, []).append(i)
                best = None
                for c, idx in sorted(per.items(), key=lambda kv: (-len({salt[i] for i in kv[1]}), kv[0])):
                    comp = {}
                    for i in idx:                                # strongest first: idx follows the ranked order
                        comp.setdefault(salt[i], []).append(i)
                    k = len(comp)
                    if k >= min_drugs or (k >= 2 and k == size[src].get(c, 0)):
                        drugs = [names[ii[0]] + (f" {ALERT}" if alert[ii].all() else "") for ii in comp.values()]
                        best = {"class": c, "drugs": drugs, "k": k, "size": size[src].get(c, 0),
                                "z": float(sgn * Z[m, idx[0]])}
                        break
                rec[d][src] = best
                if best is not None:
                    leads.setdefault((src, best["class"]), set()).add(m + 1)
        rows.append(rec)
    return rows, leads


def driving_classes(Z, salt, names, classes, alert=None, n_top=DRIVER_TOP_DD, min_z=DRIVER_MIN_Z,
                    min_drugs=DRIVER_MIN_DRUGS, max_share=DRIVER_MAX_SHARE):
    """The drug classes that drive each module (MOD-1). Z: modules x drug-doses (graph/module_pooled_z.npy: + arm mean
    pooled z minus - arm mean); salt: the compound of each drug-dose (salt_base); names: its drug name; classes:
    {source: per drug-dose list of class names} (drug_class_lists); alert: per drug-dose bool (an artifact flag).
    Per module and direction (up = +z, down = -z): the n_top strongest drug-doses whose signed z >= min_z, flagged ones
    included; per class the distinct compounds among them; the best class = the most compounds (ties alphabetical)
    that qualifies: >= min_drugs compounds, or >= 2 when that is every compound of the class in the screen.
    A class that is the best one in more than max_share of the modules is too general to name a module (in the real
    run the two translation inhibitors, Homoharringtonine and Harringtonine, a whole class of 2, lead 103 of 235
    modules): a second pass finds each module's best class without the too-general ones, for the label; the
    too-general class is still written (module_drivers).
    Returns (rows, leads, general): rows[m][direction][source] = {'all': best class of the first pass, 'specific':
    best class without the too-general ones}, each {'class', 'drugs' (names, strongest first, ' ⚠' = every counted
    drug-dose of it carries an artifact flag), 'k', 'size', 'z' (the strongest z)} or None; leads[(source, class)] =
    the modules it leads (the first pass for a too-general class, else the second); general = the too-general
    (source, class) pairs."""
    Z = np.asarray(Z, dtype=np.float64)
    Dn = Z.shape[1] if Z.ndim == 2 else 0
    alert = np.zeros(Dn, dtype=bool) if alert is None else np.asarray(alert, dtype=bool)
    size = {}
    for src, cl in classes.items():
        per = {}
        for i in range(Dn):
            for c in cl[i]:
                per.setdefault(c, set()).add(salt[i])
        size[src] = {c: len(v) for c, v in per.items()}
    args = (n_top, min_z, min_drugs)
    rows_all, leads_all = _best_classes(Z, salt, names, classes, alert, size, set(), *args)
    general = {k for k, v in leads_all.items() if len(v) > max_share * max(Z.shape[0], 1)}
    rows_sp, leads_sp = _best_classes(Z, salt, names, classes, alert, size, general, *args) if general else \
        (rows_all, leads_all)
    leads = dict(leads_sp)
    leads.update({k: leads_all[k] for k in general})
    rows = [{d: {src: {"all": ra[d][src], "specific": rs[d][src]} for src in classes} for d in ("up", "down")}
            for ra, rs in zip(rows_all, rows_sp)]
    return rows, leads, general


# the last word of a class name that is a noun naming drugs: the plural of such a name adds 's' to it ('HDAC inhibitor'
# -> 'HDAC inhibitors'); a class of tahoemap/data/drug_classes.json has its own 'plural'; any other name reads 'drugs
# with the mechanism ...' (class_plural)
PLURAL_NOUNS = ("inhibitor", "agonist", "antagonist", "blocker", "activator", "modulator", "poison", "binder",
                "stabiliser", "stabilizer", "destabiliser", "destabilizer", "degrader", "analog", "analogue",
                "antimetabolite", "trapper", "intercalator", "alkylator", "ligand", "opener", "chelator", "disruptor",
                "antibiotic", "steroid", "glucocorticoid", "corticosteroid", "inducer", "uncoupler", "antifolate",
                "taxane", "statin", "retinoid", "ionophore", "drug", "compound")


def class_plural(name):
    """A class name as a plural noun phrase for a sentence ('raised by glucocorticoid receptor agonists'): the
    'plural' of the drug_classes.json class with this label; else the name with its last noun made plural (PLURAL_NOUNS,
    before any bracket: 'Kinase X inhibitor (type II)' -> 'Kinase X inhibitors (type II)'); else 'drugs with the
    mechanism <name>'. The class columns of module_drivers keep the name itself."""
    from . import mechanisms as MC
    name = str(name or "").strip()
    for v in (MC.load_rules().get("classes") or {}).values():
        if isinstance(v, dict) and v.get("label") == name and v.get("plural"):
            return str(v["plural"])
    m = re.match(r"^(.*?)(\s*\([^()]*\))?$", name)
    head, tail = (m.group(1), m.group(2) or "") if m else (name, "")
    words = head.split(" ")
    last = words[-1].lower() if words else ""
    if last in PLURAL_NOUNS:
        return " ".join(words[:-1] + [words[-1] + "s"]) + tail
    if last.endswith("s") and last[:-1] in PLURAL_NOUNS:
        return name
    return f"drugs with the mechanism '{name}'"


def _is_translation(name):
    """Is a class name the label of a drug_classes.json class whose effect is 'translation'?"""
    from . import mechanisms as MC
    return any(isinstance(v, dict) and v.get("effect") == "translation" and v.get("label") == name
               for v in (MC.load_rules().get("classes") or {}).values())


def module_drivers(rec, leads, n_modules, chembl_source="ChEMBL", general=()):
    """One module's driver columns and texts from driving_classes: per direction the classes written (ChEMBL's when it
    qualifies, else Tahoe's; both when both qualify and name different classes; and a too-general class that is the
    best one before it is left out, marked so), with their compounds and sources; the label_drugs text ('raised by
    {class} ({drugs}; class from {source}; this class leads {k} of {M} modules)', the same with 'lowered by', joined by
    ' · '); the class the label names (the first one that is not too general: up first, then down) and how many
    modules it leads."""
    res, parts, first = {}, [], {}
    general = set(general)
    for d, verb in (("up", "raised by"), ("down", "lowered by")):
        rd = rec.get(d) or {}

        def pick(src, key):
            x = (rd.get(src) or {})
            return x.get(key) if isinstance(x, dict) and ("all" in x or "specific" in x) else (x or None)
        ch, ta = pick("ChEMBL", "specific"), pick("Tahoe", "specific")
        srcname = {"ChEMBL": chembl_source, "Tahoe": "Tahoe"}
        written = []
        if ch is not None:
            written.append(("ChEMBL", ch, srcname["ChEMBL"]))
            if ta is not None and not _same_class(ch["class"], ta["class"]):
                written.append(("Tahoe", ta, "Tahoe"))
            elif ta is not None:
                written[0] = ("ChEMBL", ch, f"{chembl_source}; Tahoe agrees ({ta['class']})")
        elif ta is not None:
            written.append(("Tahoe", ta, "Tahoe"))
        for src in ("ChEMBL", "Tahoe"):                  # a too-general class: written after, never the label
            g = pick(src, "all")
            if g is not None and (src, g["class"]) in general and all(w[1]["class"] != g["class"] for w in written):
                written.append((src, g, srcname[src] + "; too general to name a module"))
        res[f"drivers_{d}_class"] = "; ".join(w["class"] for _, w, _ in written)
        res[f"drivers_{d}_drugs"] = "; ".join(", ".join(w["drugs"]) for _, w, _ in written)
        res[f"drivers_{d}_source"] = "; ".join(sn for _, _, sn in written)
        for s_, w, sn in written:
            k = len(leads.get((s_, w["class"]), ()))
            gen = (s_, w["class"]) in general
            tl = "; a rise under a translation inhibitor may be mRNA stabilisation" if d == "up" and \
                _is_translation(w["class"]) else ""
            parts.append(f"{verb} {class_plural(w['class'])} ({', '.join(w['drugs'])}; class from "
                         f"{sn.split('; too general')[0]}"
                         f"{tl}; this class leads {k} of {n_modules} modules"
                         + (", too many to name a module)" if gen else ")"))
            if d not in first and not gen:
                first[d] = (w["class"], k)
    res["label_drugs"] = " · ".join(parts)
    lead = first.get("up") or first.get("down")
    res["drivers_class_modules"] = int(lead[1]) if lead else 0
    res["_drug_label"] = (f"raised by {class_plural(first['up'][0])}" if "up" in first else
                          f"lowered by {class_plural(first['down'][0])}" if "down" in first else "")
    return res


def module_lineage(cols, nexp, E, organ, chrom, sym, L):
    """A module's line-identity readings (MOD-3): median_lines_expressing (median over the members of the lines
    expressing them, tables/genes.parquet n_lines_expressing), lines_core (lines expressing at least LINEAGE_CORE of
    the members), the organs enriched among those lines (hypergeometric upper tail <= ORGAN_P, best first: 'Bowel 8 of
    9'), the members on the Y chromosome; plus the alert texts and the lineage label."""
    from scipy.stats import hypergeom
    cols = np.asarray(cols, dtype=np.int64)
    r = {"median_lines_expressing": np.nan, "lines_core": -1, "lineage_organs": "", "chrY_genes": "",
         "_lineage": False, "_organ_text": "", "_alerts": [], "_tags": [], "_lineage_label": ""}
    if not len(cols):
        return r
    ne = nexp[cols] if nexp is not None else np.full(len(cols), np.nan)
    med = float(np.nanmedian(ne)) if np.isfinite(ne).any() else np.nan
    r["median_lines_expressing"] = med
    core = np.zeros(0, dtype=np.int64)
    if E is not None:
        core = np.flatnonzero(E[cols].mean(axis=0) >= LINEAGE_CORE)
        r["lines_core"] = int(len(core))
    org = []
    if organ is not None and len(core) and len(core) < L:
        o_all = pd.Series(organ).fillna("").astype(str).to_numpy()
        for o in sorted({x for x in o_all if x}):
            b = int((o_all == o).sum())
            k = int((o_all[core] == o).sum())
            if k:
                p = float(hypergeom.sf(k - 1, L, b, len(core)))
                if p <= ORGAN_P:
                    org.append((p, -k, o, k, b))
        org.sort()
    r["lineage_organs"] = ", ".join(f"{o} {k} of {b}" for _p, _k, o, k, b in org)
    r["_organ_text"] = " and ".join(f"{k} of the {b} {o} lines" for _p, _k, o, k, b in org)
    if np.isfinite(med) and med < LINEAGE_MAX_SHARE * L:
        r["_lineage"] = True
        txt = (f"{ALERT} lineage-restricted: its median gene is expressed in {med:g} of {L} lines (genes expressed in "
               f"the same lines often move together whatever their regulation); most members are expressed in "
               f"{max(r['lines_core'], 0)} lines")
        if r["_organ_text"]:
            txt += f", including {r['_organ_text']}"
        r["_alerts"].append(txt)
        r["_tags"].append(TAG_LINEAGE)
        r["_lineage_label"] = (f"lineage: expressed mainly in {max(r['lines_core'], 0)} lines"
                               + (f" (including {r['_organ_text']})" if r["_organ_text"] else ""))
    if chrom is not None:
        y = [c for c in cols if str(chrom[c]) in ("Y", "chrY")]
        r["chrY_genes"] = ", ".join(sorted(sym[c] for c in y))
        if len(y) >= CHRY_ANY or (len(y) >= CHRY_MIN and len(y) >= CHRY_SHARE * len(cols)):
            r["_alerts"].append(f"{ALERT} {len(y)} genes on the Y chromosome ({r['chrY_genes']}): they are expressed "
                                "only in lines from male donors, so the module partly marks line identity")
            r["_tags"].append(TAG_CHRY)
    return r


def module_readshare(cols, pairs, sym):
    """A module's groups of near-identical copies among its members (read_sharing_groups): read_sharing_genes ('A, B,
    C | D, E'), read_sharing_n (members in a group), and the groups themselves (for readshare_alert)."""
    groups = read_sharing_groups(cols, pairs)
    return {"read_sharing_genes": " | ".join(", ".join(sym[c] for c in g) for g in groups),
            "read_sharing_n": int(sum(len(g) for g in groups)), "n_genes": int(len(cols)), "_groups": groups,
            "_group_of": {c: i for i, g in enumerate(groups) for c in g}}


def readshare_alert(rs, named):
    """(alerts, tags) of the read-sharing reading (MOD-2): an alert when >= 2 of the genes the label names (named:
    cols; the module's 5 strongest genes, and a set label's first 5 shared genes) are near-identical copies (in a
    group), or >= READSHARE_MODULE_SHARE of the members are in groups."""
    groups = rs.get("_groups") or []
    if not groups:
        return [], []
    named = {int(c) for c in named}
    in_groups = len(named & {c for g in groups for c in g})
    n_in, n = rs["read_sharing_n"], max(rs.get("n_genes", 0), 1)
    if in_groups >= 2 or n_in >= READSHARE_MODULE_SHARE * n:
        return ([f"{ALERT} {n_in} of its {n} genes are near-identical copies that can share sequencing reads "
                 f"({rs['read_sharing_genes']}): part of their co-movement may be read counting, not regulation"],
                [TAG_READSHARE])
    return [], []


def label_rows(mods, cands, drivers, lineage, readshare, n_modules):
    """module_labels.csv rows. mods: one dict per module (module, n_genes, n_plus, n_minus, top_plus, top_minus,
    top_genes ('genes: ...' names), covariate_tag); cands: label_candidates rows; drivers: {module: module_drivers};
    lineage: {module: module_lineage}; readshare: {module: module_readshare}. The label is the first of: a strong set
    label, the driving drug class ('raised by {class}'; 'lowered by {class}' when only the fall qualifies), a weak set
    label ('weak: ...'), the lineage label, 'genes: ...'. Each component keeps its own columns."""
    by_mod = {m: g for m, g in cands.groupby("module")} if len(cands) else {}
    rows = []
    for md in mods:
        m = int(md["module"])
        c = by_mod.get(m)
        b = choose_set(c)
        rec = dict(md)
        named_top = list(rec.pop("_named_top", []) or [])
        rec.pop("top_genes", None)
        if b is not None:
            short = str(b["set_label"])
            weak = bool(b["weak"])
            rec.update(set_label=weak_text(short, b["overlap"], b["n_set"], b["q"]) if weak else short,
                       label_set=b["set"], label_arm=b["arm"], label_overlap=int(b["overlap"]),
                       label_independent_overlap=int(b["independent"]), label_n_set=int(b["n_set"]),
                       label_fold=float(b["fold"]), label_p=float(b["p"]), label_q=float(b["q"]), label_weak=weak,
                       label_weak_why=str(b["weak_why"]), _set_source=str(b["source"]))
        else:
            rec.update(set_label="", label_set="", label_arm="", label_overlap=0, label_independent_overlap=0,
                       label_n_set=0, label_fold=np.nan, label_p=np.nan, label_q=np.nan, label_weak=False,
                       label_weak_why="", _set_source="")
        for arm, nm in (("+", "plus"), ("-", "minus")):
            bb = choose_set(c[c["arm"] == arm]) if c is not None else None
            if bb is not None:
                rec[f"{nm}_label"] = weak_text(bb["set_label"], bb["overlap"], bb["n_set"], bb["q"]) if bb["weak"] \
                    else str(bb["set_label"])
                rec[f"{nm}_set"], rec[f"{nm}_q"] = str(bb["set"]), float(bb["q"])
            else:
                rec[f"{nm}_label"], rec[f"{nm}_set"], rec[f"{nm}_q"] = "", "", np.nan
        dv = drivers.get(m) or {}
        for k in ("drivers_up_class", "drivers_up_drugs", "drivers_up_source", "drivers_down_class",
                  "drivers_down_drugs", "drivers_down_source", "label_drugs"):
            rec[k] = dv.get(k, "")
        rec["drivers_class_modules"] = int(dv.get("drivers_class_modules", 0))
        ln = lineage.get(m) or module_lineage([], None, None, None, None, None, 1)
        rs = readshare.get(m) or {"read_sharing_genes": "", "read_sharing_n": 0, "n_genes": md.get("n_genes", 0)}
        rec.update(median_lines_expressing=ln["median_lines_expressing"], lines_core=ln["lines_core"],
                   lineage_organs=ln["lineage_organs"], chrY_genes=ln["chrY_genes"],
                   lineage_label=ln["_lineage_label"], read_sharing_genes=rs["read_sharing_genes"],
                   read_sharing_n=int(rs["read_sharing_n"]))
        if b is not None and not rec["label_weak"]:
            label, source = rec["set_label"], rec["_set_source"]
        elif dv.get("_drug_label"):
            label, source = dv["_drug_label"], "drug class"
        elif b is not None:
            label, source = rec["set_label"], rec["_set_source"]
        elif ln["_lineage"]:
            label, source = ln["_lineage_label"], "lineage"
        else:
            label, source = "genes: " + md.get("top_genes", ""), "top genes"
        # the read-sharing alert looks at the genes the label names: the module's 5 strongest genes (the 'genes:'
        # label and the map name them), and a set label's first 5 shared genes
        named = named_top + (list(b["_cols"])[:LABEL_GENES] if b is not None and source == rec["_set_source"]
                             else [])
        ra, rt = readshare_alert(rs, named)
        alerts = ra + ln["_alerts"]
        tags = rt + ln["_tags"]
        rec.update(label=label, label_source=source, label_alert="; ".join(alerts),
                   label_display=label + ("".join(f" {t}" for t in tags)))
        rec.pop("_set_source", None)
        rows.append(rec)
    cols = ["module", "n_genes", "n_plus", "n_minus", "label", "label_source", "label_display", "label_alert",
            "label_weak", "label_weak_why", "set_label", "label_set", "label_arm", "label_overlap",
            "label_independent_overlap", "label_n_set", "label_fold", "label_p", "label_q", "plus_label", "plus_set",
            "plus_q", "minus_label", "minus_set", "minus_q", "label_drugs", "drivers_up_class", "drivers_up_drugs",
            "drivers_up_source", "drivers_down_class", "drivers_down_drugs", "drivers_down_source",
            "drivers_class_modules", "lineage_label", "median_lines_expressing", "lines_core", "lineage_organs",
            "chrY_genes", "read_sharing_genes", "read_sharing_n", "covariate_tag", "top_plus", "top_minus"]
    df = pd.DataFrame(rows)
    for c in cols:
        if c not in df:
            df[c] = ""
    return df[cols]


def _strongest(sp, cols, k):
    """The k genes of cols (genome cols) with the largest |axis projection| on the nodal map, both arms together."""
    cols = np.asarray(cols, dtype=np.int64)
    pr = np.abs(sp.axis_proj[sp.pos[cols]])
    return [int(c) for c in cols[np.argsort(-pr, kind="mergesort")[:k]]]


def _module_members(sp):
    """{module: (gene cols of its members, + arm cols by |axis projection|, - arm cols likewise)} of the space."""
    res = {}
    for m in range(1, sp.n_modules + 1):
        mem = np.where(sp.module == m)[0]
        if not len(mem):
            continue
        order = mem[np.argsort(-np.abs(sp.axis_proj[mem]), kind="mergesort")]
        res[m] = (sp.inc[mem], sp.inc[order[sp.arm[order] == "+"]], sp.inc[order[sp.arm[order] == "-"]])
    return res


def label_inputs(out, gK):
    """What the labels read besides the enrichment: read-sharing pairs (relations.read_sharing_pairs; {} when the
    reference stage or HGNC / Compara did not load) and their source; per gene the lines expressing it (tables
    genes.parquet n_lines_expressing, else the expressed mask) and the expressed mask (relations.expressed_mask); the
    lines' organs (tables/lines.parquet Organ, in line order); per gene its chromosome (reference annotations chrom);
    the module pooled z (graph/module_pooled_z.npy) with the drug-doses' compounds, names, classes and artifact
    alerts."""
    from .common import has_artifact
    from .relations import expressed_mask, read_sharing_pairs, read_sharing_source
    res = {"pairs": {}, "pairs_source": "not assessed", "nexp": None, "E": None, "E_source": "", "organ": None,
           "L": 0, "chrom": None, "Z": None}
    try:
        res["pairs"] = read_sharing_pairs(out)
        res["pairs_source"] = read_sharing_source(out)
    except Exception as e:  # noqa: BLE001  (an older relations module or a broken reference table: no groups)
        res["pairs_source"] = f"not assessed ({type(e).__name__}: {e})"
    E, src = expressed_mask(out, gK)
    res["E"], res["E_source"] = E, src
    gp = os.path.join(out, "tables", "genes.parquet")
    if os.path.exists(gp):
        import pyarrow.parquet as pq
        if {"col", "n_lines_expressing"} <= set(pq.ParquetFile(gp).schema_arrow.names):
            g = pd.read_parquet(gp, columns=["col", "n_lines_expressing"]).set_index("col").reindex(np.arange(gK))
            res["nexp"] = pd.to_numeric(g["n_lines_expressing"], errors="coerce").to_numpy(np.float64)
    if res["nexp"] is None and E is not None:
        res["nexp"] = E.sum(axis=1).astype(np.float64)
    lp = os.path.join(out, "tables", "lines.parquet")
    if os.path.exists(lp):
        li = pd.read_parquet(lp).sort_values("line")
        res["L"] = int(len(li))
        if "Organ" in li:
            res["organ"] = li["Organ"].fillna("").astype(str).to_numpy()
    if E is not None:
        res["L"] = int(E.shape[1]) if not res["L"] else res["L"]
        if res["organ"] is not None and len(res["organ"]) != E.shape[1]:
            res["organ"] = None
    ap = os.path.join(out, "reference", "annotations.parquet")
    if os.path.exists(ap):
        import pyarrow.parquet as pq
        if {"col", "chrom"} <= set(pq.ParquetFile(ap).schema_arrow.names):
            a = pd.read_parquet(ap, columns=["col", "chrom"]).set_index("col").reindex(np.arange(gK))
            res["chrom"] = a["chrom"].fillna("").astype(str).to_numpy()
    zp = os.path.join(out, "graph", "module_pooled_z.npy")
    dp = os.path.join(out, "tables", "drugdoses.parquet")
    if os.path.exists(zp):
        res["Z"] = np.load(zp)
        if os.path.exists(dp):
            dd = pd.read_parquet(dp)
        else:
            dd = read_effects_index(os.path.join(out, "atlas", "effects"))["drugdose"]
        dd = dd.reset_index(drop=True)
        res["dd_drug"] = dd["drug"].astype(str).to_numpy()
        res["dd_salt"] = dd["salt_base"].astype(str).to_numpy() if "salt_base" in dd else \
            np.array([T.salt_base(x) for x in res["dd_drug"]])
        moa = dd["moa_fine"].fillna("").astype(str).to_numpy() if "moa_fine" in dd else np.array([""] * len(dd))
        res["classes"], res["chembl_source"] = drug_class_lists(out, res["dd_drug"], moa)
        try:
            from .tables import dd_flags_of_record
            fl = dd_flags_of_record(out)
        except Exception:  # noqa: BLE001
            fl = dd["flags"].fillna("").astype(str).to_numpy() if "flags" in dd else np.array([""] * len(dd))
        res["dd_alert"] = np.array([has_artifact(f) for f in fl], dtype=bool)
        if res["Z"].shape[1] != len(dd):
            log(f"  module_pooled_z has {res['Z'].shape[1]} drug-doses, the drug-dose table {len(dd)}: no drug classes")
            res["Z"] = None
    return res


def _labels(sp, enr, out, inputs=None):
    """module_labels.csv (README): the label of every module by the version 7 rules (label_rows) with every component
    in its own column. enr: module_enrichment with '_cols' (shared gene cols) and '_n_listed'."""
    inp = inputs if inputs is not None else label_inputs(out, sp.gK)
    mp = os.path.join(out, "graph", "modules.parquet")
    gm = pd.read_parquet(mp).set_index("module") if os.path.exists(mp) else pd.DataFrame()
    members = _module_members(sp)
    mods, lineage, readshare, group_of = [], {}, {}, {}
    drv_rows, leads, general = ([], {}, set()) if inp.get("Z") is None else driving_classes(
        inp["Z"], inp["dd_salt"], inp["dd_drug"], inp["classes"], inp["dd_alert"])
    drivers = {}
    nm = len(members)
    for m, (cols, plus, minus) in members.items():
        if m in gm.index:
            tp, tm = marked_names(gm.at[m, "top_plus"]), marked_names(gm.at[m, "top_minus"])
        else:
            tp = [sp.sym[c] + (f" {ALERT}" if sp.flagged_only[c] else "") for c in plus]
            tm = [sp.sym[c] + (f" {ALERT}" if sp.flagged_only[c] else "") for c in minus]
        md = {"module": m, "n_genes": len(cols), "n_plus": len(plus), "n_minus": len(minus),
              "top_genes": ", ".join(marked_names(", ".join(tp), 3) + marked_names(", ".join(tm), 2)),
              "_named_top": _strongest(sp, cols, LABEL_GENES),
              "covariate_tag": str(gm.at[m, "covariate_tag"]) if m in gm.index and "covariate_tag" in gm
              and isinstance(gm.at[m, "covariate_tag"], str) else "",
              "top_plus": ", ".join(marked_names(", ".join(tp), 8)),
              "top_minus": ", ".join(marked_names(", ".join(tm), 8))}
        mods.append(md)
        readshare[m] = module_readshare(cols, inp["pairs"], sp.sym)
        group_of[m] = readshare[m]["_group_of"]
        lineage[m] = module_lineage(cols, inp["nexp"], inp["E"], inp["organ"], inp["chrom"], sp.sym, inp["L"])
        if drv_rows and m - 1 < len(drv_rows):
            drivers[m] = module_drivers(drv_rows[m - 1], leads, nm, inp.get("chembl_source", "ChEMBL"), general)
    cands = label_candidates(enr, group_of)
    return label_rows(mods, cands, drivers, lineage, readshare, nm), {
        "read_sharing_source": inp["pairs_source"], "expressed_from": inp["E_source"], "lines": inp["L"],
        "chembl_source": inp.get("chembl_source", ""), "drug_classes": inp.get("Z") is not None,
        "leads": {f"{s}: {c}": len(v) for (s, c), v in sorted(leads.items(), key=lambda kv: (-len(kv[1]), kv[0]))},
        "too_general": sorted(f"{s}: {c}" for s, c in general)}


# ----------------------------------------------------------------------------- novel candidates
def _novel_edges(out, sp, ann_name):
    p = os.path.join(out, "relations", "gene_relations.parquet")
    cols = ["col_a", "col_b", "cos", "abs_cos", "cos_half1", "cos_half2", "evidence", "fdr", "novel_candidate",
            "locus", "readthrough_risk", "same_chrom", "distance_bp", "alert"] + NOVEL_LINEAGE
    empty = pd.DataFrame(columns=["col_a", "symbol_a", "name_a", "module_a", "arm_a", "col_b", "symbol_b", "name_b",
                                  "module_b", "arm_b", "same_module", "cos", "cos_half1", "cos_half2", "evidence",
                                  "fdr", "same_chrom", "distance_bp"] + NOVEL_LINEAGE + ["alert"])
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
    # relations version 5: the lineage pair and read-sharing columns (an older relations stage: not assessed)
    for c in NOVEL_LINEAGE:
        if c in r:
            res[c] = r[c].to_numpy()
        else:
            res[c] = {"lineage_pair": False, "read_sharing_risk": False, "read_sharing": ""}.get(c, np.nan)
    # the pair's alert (relations 'alert'; an older relations stage: from embed's evidence_flagged_only)
    if "alert" in r:
        res["alert"] = r["alert"].fillna("").astype(str).to_numpy()
    else:
        res["alert"] = [_gene_alert(sp, [x, y]) for x, y in zip(a, b)]
    return res.reset_index(drop=True)


def _gene_alert(sp, cols):
    """'' or '⚠ ' + the genes of cols that are in the vector space only through drug-doses that carry an alert."""
    fo = [sp.sym[c] for c in cols if sp.flagged_only[c]]
    return f"{ALERT} " + "; ".join(f"{g} is in the vector space only through drug-doses that carry an alert"
                                   for g in fo) if fo else ""


def _novel_members(sp, sets, units, tsets, Q, ann_name, n_ref_sets):
    cols = ["col", "symbol", "name", "module", "arm", "source", "set", "set_label", "set_q", "n_annotated_in_arm",
            "n_arm", "mean_cos", "max_cos", "mean_cos_half1", "mean_cos_half2", "n_reference_sets", "alert"]
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
                "n_reference_sets": n_ref_sets[g], "alert": [_gene_alert(sp, [x]) for x in g]}))
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
def _class_check(Un, labels, mol, names, flagged, untr, active):
    """The drug check for one class source. labels: per drug a set of class names (empty = no class: left out);
    mol: the molecule of each drug (two drugs of one molecule are never paired); Un: unit drug vectors (zero = no
    vector: left out). Returns ({'all', 'active'}: overall AUROC of same-class pairs vs other pairs, ...), [per class
    rows with >= 2 drugs])."""
    has = np.array([bool(x) for x in labels]) & (np.linalg.norm(Un, axis=1) > 0)
    res = {}
    for tag, sel in (("all", has), ("active", has & active)):
        idx = np.where(sel)[0]
        cl = {c for i in idx for c in labels[i]}
        r = {"drugs": int(len(idx)), "classes": int(len(cl)), "pos_pairs": 0, "neg_pairs": 0, "auroc": np.nan,
             "mean_cos_same": np.nan, "mean_cos_other": np.nan, "drugs_no_trustworthy_dose": int(untr[idx].sum()),
             "drugs_flagged_dose": int(flagged[idx].sum())}
        if len(idx) >= 3:
            C = Un[idx] @ Un[idx].T
            iu = np.triu_indices(len(idx), 1)
            same = np.array([[bool(labels[a] & labels[b]) for b in idx] for a in idx])[iu]
            keep = (mol[idx][:, None] != mol[idx][None, :])[iu]
            c = C[iu]
            pos, neg = c[keep & same], c[keep & ~same]
            r.update(pos_pairs=int(len(pos)), neg_pairs=int(len(neg)), auroc=_auroc(pos, np.sort(neg)),
                     mean_cos_same=float(pos.mean()) if len(pos) else np.nan,
                     mean_cos_other=float(neg.mean()) if len(neg) else np.nan)
        res[tag] = r
    idx = np.where(has)[0]
    rows = []
    if len(idx) >= 3:
        C = Un[idx] @ Un[idx].T
        lab = [labels[i] for i in idx]
        for cl in sorted({c for x in lab for c in x}):
            w = np.array([k for k, x in enumerate(lab) if cl in x], dtype=np.int64)
            o = np.array([k for k, x in enumerate(lab) if cl not in x], dtype=np.int64)
            if len(w) < 2:
                continue
            iu = np.triu_indices(len(w), 1)
            ks = (mol[idx[w]][:, None] != mol[idx[w]][None, :])[iu]
            within = C[np.ix_(w, w)][iu][ks]
            between = C[np.ix_(w, o)].ravel() if len(o) else np.zeros(0)
            rows.append({"class": cl, "n_drugs": int(len(w)), "drugs": ", ".join(names[idx[w]]),
                         "n_drugs_flagged_dose": int(flagged[idx[w]].sum()),
                         "n_drugs_no_trustworthy_dose": int(untr[idx[w]].sum()),
                         "n_pairs": int(len(within)), "mean_cos_within": float(within.mean()) if len(within)
                         else np.nan, "mean_cos_to_other_classes": float(between.mean()) if len(between) else np.nan,
                         "auroc_within_vs_other": _auroc(within, np.sort(between))})
    return res, rows


def _drug_check(out):
    """Do drugs of one mechanism class get similar drug vectors (embed/drug_vectors.npy)? Two class sources side by
    side: Tahoe's moa_fine (as before; 'unclear' / 'unknown' left out) and the mechanism classes (drug_class_lists
    'ChEMBL': the class labels of tahoemap/data/drug_classes.json, or a drug's ChEMBL mechanism texts). Two drugs of
    one molecule (the same ChEMBL id, else the same name without its salt) are never paired. Returns (results
    {'tahoe': {'all', 'active'}, 'chembl': {...}, 'chembl_source', 'min_active'}, drug_moa table: one row per class
    with >= 2 drugs, Tahoe's first, then the mechanism classes)."""
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
    drug = dr["drug"].astype(str).to_numpy()
    moa = dr["moa_fine"].fillna("").astype(str).str.strip().to_numpy() if "moa_fine" in dr \
        else np.array([""] * len(dr))
    tahoe = [set() if m.lower() in NO_MOA else {m} for m in moa]
    cls, csrc = drug_class_lists(out, drug, moa)
    chembl = [set(x) for x in cls["ChEMBL"]]
    salt = np.array([T.salt_base(d) for d in drug])
    cid = {}
    try:
        from . import mechanisms as MC
        a = MC.drug_annotations(out)
        cid = dict(zip(a["drug"].astype(str), a["chembl_id"].fillna("").astype(str)))
    except Exception:  # noqa: BLE001
        pass
    mol = np.array([cid.get(d) or s for d, s in zip(drug, salt)], dtype=object)
    nsig = pd.to_numeric(dr.get("n_sig_genes", pd.Series(0, index=dr.index)), errors="coerce").fillna(0).to_numpy()
    # a drug whose vector is of a dose with an artifact flag (embed drugs.parquet alert), e.g. one with no trustworthy
    # dose (trusted = False), is tested like the others and marked
    untr = ~dr["trusted"].fillna(True).astype(bool).to_numpy() if "trusted" in dr else np.zeros(len(dr), dtype=bool)
    flagged = (dr["alert"].fillna("").astype(str) != "").to_numpy() | untr if "alert" in dr else untr
    names = np.array([d + (f" {ALERT}" if u else "") for d, u in zip(drug, flagged)], dtype=object)
    active = nsig >= min_active
    rt, tt = _class_check(Un, tahoe, mol, names, flagged, untr, active)
    rc, tc = _class_check(Un, chembl, mol, names, flagged, untr, active)
    for r in (rt, rc):
        for v in r.values():
            v["min_active"] = min_active
    rows = [dict(class_source="Tahoe", moa_fine=x["class"], **x) for x in tt]
    rows += [dict(class_source=csrc, moa_fine="", **x) for x in tc]
    tab = pd.DataFrame(rows)
    if len(tab):
        tab["_s"] = (tab["class_source"] != "Tahoe").astype(int)
        tab = tab.sort_values(["_s", "auroc_within_vs_other", "n_drugs"], ascending=[True, False, False],
                              kind="mergesort").drop(columns="_s").reset_index(drop=True)
        first = ["class_source", "class", "moa_fine"]
        tab = tab[first + [c for c in tab.columns if c not in first]]
    return {"all": rt["all"], "active": rt["active"], "tahoe": rt, "chembl": rc, "chembl_source": csrc,
            "min_active": min_active}, tab


def _annotation_agreement(out):
    """(counts per annotation_status token, rows of every drug with an annotation_alert: drug, Tahoe (moa_fine;
    targets), ChEMBL (mechanisms), alert) from the drug annotations (mechanisms.drug_annotations)."""
    try:
        from . import mechanisms as MC
        a = MC.drug_annotations(out)
    except Exception as e:  # noqa: BLE001
        log(f"  drug annotations not read ({type(e).__name__}: {e})")
        return {}, []
    st = a["annotation_status"].fillna("").astype(str) if "annotation_status" in a else pd.Series([], dtype=str)
    counts = {k: int(v) for k, v in st.str.split("; ").explode().value_counts().items() if k}
    rows = []
    if "annotation_alert" in a:
        for _, r in a[a["annotation_alert"].fillna("").astype(str) != ""].iterrows():
            tah = "; ".join(x for x in (str(r.get("tahoe_moa_fine") or ""),
                                        ("targets " + str(r.get("tahoe_targets"))) if str(r.get("tahoe_targets") or "")
                                        else "") if x)
            rows.append([r["drug"], tah or "-", str(r.get("chembl_mechanisms") or "") or "-",
                         str(r["annotation_alert"])])
    return counts, rows


# ----------------------------------------------------------------------------- neighbouring wells (section 4)
NB_INTRO = ("Wells that touch on a plate (side by side, above or below, or at a corner) can share signal: liquid "
            "carried from one well to the next, or a local problem on part of a plate. Pairs of drug-doses of "
            "different "
            "compounds on the same plate are compared: a pair resembles when at least half of one's significant genes "
            "move the same way (|z| >= 3) in the other, and it moves at least 30% of the other's 30 strongest genes.")
NB_CAVEAT = "A same-row resemblance below significance (e.g. plate7 row C) is not tested here."


def _explorer_link(site, dd_):
    """A Markdown link to a drug-dose's explorer page (links.dd); without a site URL the run folder's own explorer."""
    from . import links
    url = links.dd(site or "../explorer/web/index.html", int(dd_))
    return f"[explorer]({url})"


def _split_where(where):
    """'plate3 G8 next to H8; plate4 A4 next to B4' -> ('plate3 G8; plate4 A4', 'plate3 H8; plate4 B4')."""
    own, other = [], []
    for part in [x.strip() for x in str(where or "").split("; ") if x.strip()]:
        if " next to " in part:
            a, b = part.split(" next to ", 1)
            plate = a.split(" ", 1)[0]
            own.append(a)
            other.append(", ".join(f"{plate} {w.strip()}" for w in b.split(",") if w.strip()))
        else:
            own.append(part)
    return "; ".join(own), "; ".join(other)


def _neighbour_section(out, site=None):
    """Section 4 of report.md and metrics.json 'neighbouring_wells': the tables stage's neighbouring-well rule (tables
    info.json 'neighbour_rule' and drugdoses.parquet nb_*; the tables stage computes every number, this section only
    shows them)."""
    L = ["## 4. Neighbouring wells", "", NB_INTRO, ""]
    ip = os.path.join(out, "tables", "info.json")
    info = {}
    if os.path.exists(ip):
        with open(ip, encoding="utf-8") as fh:
            info = json.load(fh).get("neighbour_rule") or {}
    dp = os.path.join(out, "tables", "drugdoses.parquet")
    dd = pd.read_parquet(dp) if os.path.exists(dp) else pd.DataFrame()
    if not info or "nb_tier" not in dd:
        L += ["The tables stage of this output has no neighbouring-well rule (it was made before tables version 5): "
              "`tahoe run --from tables` adds it.", ""]
        return L, None
    rows = []
    for o in info.get("orientation") or []:
        rows.append([o.get("orientation"), f"{int(o.get('judged') or 0):,}", f"{int(o.get('resembling') or 0):,}",
                     _pct(o["share"]) if o.get("share") is not None else "-",
                     f"{o['x_far_share']:.2f}x" if o.get("x_far_share") is not None else "-"])
    L += ["**Resembling pairs by placement** (a pair counted once, at its closest placement):", "",
          _md_table(["placement", "pairs judged", "resembling", "share", "x the share at 3+ wells apart"], rows), ""]
    pp, ex, dn = info.get("pairs_passing") or {}, info.get("expected_passes") or {}, info.get("drugdoses") or {}
    rows = [[t, pp.get(t, 0), _f(ex.get(t), "{:.1f}"), dn.get(t, 0)] for t in pp]
    L += [f"**Touching pairs that pass the rule, by tier** ({int(info.get('pairs_judged') or 0):,} touching pairs "
          f"judged; {int(info.get('far_pairs_judged') or 0):,} pairs 3 or more wells apart give the chance rate). "
          "'artifact': the drug's higher doses do not show the shared genes (flagged 'like a neighbouring well' on "
          "the genes the neighbour moves the same way); 'top dose': the drug's top dose, so the data cannot tell a "
          "carried-over signal from a real effect (an alert, not an artifact flag); 'same mechanism': the two "
          "compounds share "
          "an annotated mechanism (a note); 'dose response': the drug's lower doses already move its strongest "
          "shared genes the same way, so its own effect grows with the dose (a note).", "",
          _md_table(["tier", "adjacent pairs passing",
                     "expected from pairs 3+ apart (at most: those include real copies that resemble their class "
                     "elsewhere)", "drug-doses"], rows), ""]
    t = dd[dd["nb_tier"].fillna("").astype(str) != ""].copy()
    n = len(t)
    if n:
        rank = {x: i for i, x in enumerate(("artifact", "top dose", "same mechanism", "dose response"))}
        t["_r"] = t["nb_tier"].map(rank).fillna(9)
        t["_j"] = pd.to_numeric(t["nb_share"], errors="coerce").fillna(0)
        shown = t.sort_values(["_j"], ascending=False, kind="mergesort").head(NB_TABLE_MAX) if n > NB_TABLE_MAX \
            else t
        shown = shown.sort_values(["_r", "_j"], ascending=[True, False], kind="mergesort")
        um = "µM"
        rows = []
        for _, r in shown.iterrows():
            own, other = _split_where(r.get("nb_where"))
            rows.append([f"{r['drug']} {r['dose']} {um}", own or "-",
                         f"{r.get('nb_partner') or '-'} ({other or '-'})", int(r.get("nb_n_sig") or 0),
                         int(r.get("nb_shared") or 0), _f(r.get("nb_share")), _f(r.get("nb_top_share")),
                         _pct(float(r["nb_other_doses_share"])) if pd.notna(r.get("nb_other_doses_share")) else "-",
                         _pct(float(r["nb_partner_own_share"])) if pd.notna(r.get("nb_partner_own_share")) else "-",
                         r["nb_tier"], int(r.get("nb_genes") or 0), _explorer_link(site, r["dd"])])
        head = (f"**Every drug-dose with a tier** ({n}; tables/drugdoses.parquet nb_* has the full alert text, "
                "nb_alert). J = the share of its significant genes the partner moves the same way; T = the share of "
                "the partner's 30 strongest genes it moves the same way; 'its other doses' / 'partner's other doses' "
                "= the largest share of the shared genes that the drug's (the partner's) other doses move the same "
                "way; 'genes flagged' = genes that carry the flag or the alert.")
        if n > NB_TABLE_MAX:
            head += f" {NB_TABLE_MAX} of {n} shown (the strongest by J); all in tables/drugdoses.parquet (nb_tier)."
        L += [head, "",
              _md_table(["drug-dose", "plate, well", "partner (drug-dose, well)", "significant genes", "shared", "J",
                         "T", "its other doses", "partner's other doses", "tier", "genes flagged", "explorer link"],
                        rows), ""]
    else:
        L += ["No drug-dose passes the rule in this run.", ""]
    L += [NB_CAVEAT, ""]
    met = {"pairs_judged": info.get("pairs_judged"), "pairs_passing": pp, "expected_passes": ex, "drugdoses": dn,
           "table_rows": int(min(n, NB_TABLE_MAX)), "drugdoses_with_tier": int(n)}
    return L, met


# ----------------------------------------------------------------------------- line-selective responses (section 8)
def auroc_perm(x, grp, n_perm=LINE_PERM, seed=0):
    """(AUROC of x in the group (grp True) vs the others, permutation p): P(group value > other value), ties 1/2;
    p = (1 + shuffles with an AUROC >= the real one) / (1 + n_perm), the group labels shuffled over the same values
    (a stable seed). NaN, NaN when either side is empty."""
    x = np.asarray(x, dtype=np.float64)
    grp = np.asarray(grp, dtype=bool)
    if not grp.any() or grp.all():
        return np.nan, np.nan
    a = _auroc(x[grp], np.sort(x[~grp]))
    rng = np.random.default_rng(seed)
    k = int(grp.sum())
    # rank form of the AUROC: (sum of the group's ranks - k (k + 1) / 2) / (k (n - k)), ties averaged
    r = pd.Series(x).rank(method="average").to_numpy()
    n = len(x)
    hits = 0
    for _ in range(int(n_perm)):
        idx = rng.choice(n, k, replace=False)
        if (r[idx].sum() - k * (k + 1) / 2) / (k * (n - k)) >= a - 1e-12:
            hits += 1
    return float(a), float((1 + hits) / (1 + n_perm))


def _control_lines(rule, lines, out):
    """(bool per line of the group, the rule in words) for one line_controls 'lines' entry."""
    L = len(lines)
    kind = rule.get("rule")
    if kind == "driver_change":
        pat = str(rule.get("pattern", ""))
        dc = lines["driver_changes"].fillna("").astype(str) if "driver_changes" in lines else pd.Series([""] * L)
        g = np.array([pat in [x.strip() for x in t.split(";")] for t in dc], dtype=bool)
        return g, f"lines whose recorded driver changes include {pat}"
    if kind == "line_names":
        names = {str(x) for x in rule.get("names", [])}
        return lines["cell_name"].astype(str).isin(names).to_numpy(), "the line" + (
            "s " if len(names) > 1 else " ") + ", ".join(sorted(names))
    if kind == "tp53":
        st = str(rule.get("status", ""))
        t = lines["tp53_status"].fillna("").astype(str) if "tp53_status" in lines else pd.Series([""] * L)
        same = {st} | ({"wild type"} if st == "not recorded" else set())     # tables before version 5 wrote 'wild type'
        return t.isin(same).to_numpy(), f"lines whose TP53 status reads '{st}'"
    if kind == "baseline_high":
        gene, fold = str(rule.get("gene", "")), float(rule.get("fold_of_median", 1.5))
        p = os.path.join(out, "tables", "line_effects.parquet")
        if not os.path.exists(p):
            return np.zeros(L, dtype=bool), f"{gene} baseline not available (no tables/line_effects.parquet)"
        le = pd.read_parquet(p, columns=["symbol", "line", "baseline_cpm"], filters=[("symbol", "==", gene)])
        b = le.groupby("line")["baseline_cpm"].max().reindex(lines["line"].to_numpy()).to_numpy(np.float64)
        med = float(np.nanmedian(b)) if np.isfinite(b).any() else np.nan
        g = np.isfinite(b) & (b >= fold * med) if np.isfinite(med) else np.zeros(L, dtype=bool)
        if not np.isfinite(med):                     # the gene is not in this run's tables (not measured)
            return g, (f"lines whose {gene} baseline is at least {fold:g}x its median over the lines ({gene} is not "
                       "measured in this run, so no line qualifies)")
        return g, f"lines whose {gene} baseline is at least {fold:g}x its median over the lines ({med:.0f} CPM)"
    return np.zeros(L, dtype=bool), f"unknown line rule {kind!r}"


def _control_drugs(rule, out, drugs_tab):
    """([(drug name, why)] in the screen, the rule in words) for one line_controls 'drugs' entry. drugs_tab:
    tables/drugs.parquet (drug, salt_base, targets, chembl_targets)."""
    from . import mechanisms as MC
    names = drugs_tab["drug"].astype(str).tolist()
    if "names" in rule:
        want = {MC.molecule_key(x) for x in rule["names"]}
        hit = [(d, "named in the control") for d in names if MC.molecule_key(d) in want]
        return hit, ", ".join(rule["names"])
    if "class" in rule:
        cls = rule["class"] if isinstance(rule["class"], list) else [rule["class"]]
        hit = {}
        K = MC.drug_classes(out)
        for c in cls:
            for d, src in zip(K.loc[K["class"] == c, "drug"].astype(str), K.loc[K["class"] == c, "source"].astype(str)):
                if d in names:
                    hit.setdefault(d, f"{MC.class_info(c).get('label', c)} ({src})")
        return sorted(hit.items()), " / ".join(MC.class_info(c).get("label", c) for c in cls) + \
            " (tahoemap/data/drug_classes.json)"
    if "targets_any" in rule:
        want = {str(x).upper() for x in rule["targets_any"]}
        hit = []
        mech = MC.drug_mechanisms(out)
        ch = {}
        for d, g in zip(mech["drug"].astype(str), mech["target_genes"].fillna("").astype(str)):
            ch.setdefault(d, set()).update(x.strip().upper() for x in g.split(",") if x.strip())
        for _, r in drugs_tab.iterrows():
            d = str(r["drug"])
            tah = {x.strip().upper() for x in re.split(r"[,;]", str(r.get("targets") or "")) if x.strip()}
            why = []
            if tah & want:
                why.append("Tahoe target " + ", ".join(sorted(tah & want)))
            if ch.get(d, set()) & want:
                why.append("ChEMBL target " + ", ".join(sorted(ch[d] & want)))
            if why:
                hit.append((d, "; ".join(why)))
        return hit, "drugs whose Tahoe or ChEMBL targets include " + ", ".join(sorted(want))
    return [], "unknown drug rule"


def _line_controls(out, truth=None):
    """Section 8 of report.md and metrics.json 'line_controls': for each line_controls entry of control_sets.json
    (and, with the synthetic truth, the planted line-selective answers), per drug-dose of its drugs the AUROC of the
    line selectivity (tables/drug_line_response.parquet sel_z) of the group's measured lines against the other
    measured lines, with a permutation p (LINE_PERM shuffles of the group labels, stable seed)."""
    rp = os.path.join(out, "tables", "drug_line_response.parquet")
    L = ["## 8. Line-selective responses: known positive controls", ""]
    if not os.path.exists(rp):
        L += ["tables/drug_line_response.parquet is missing (an output made before tables version 5): "
              "`tahoe run --from tables` adds it.", ""]
        return L, None
    import pyarrow.parquet as pq
    have = set(pq.ParquetFile(rp).schema_arrow.names)
    r = pd.read_parquet(rp, columns=[c for c in ("dd", "drug", "dose", "conc", "line", "cell_name", "measured",
                                                 "sel_z", "selective", "response_strength") if c in have])
    if "response_strength" not in r:
        r["response_strength"] = np.nan
    lines = pd.read_parquet(os.path.join(out, "tables", "lines.parquet")).sort_values("line").reset_index(drop=True)
    drugs_tab = pd.read_parquet(os.path.join(out, "tables", "drugs.parquet"))
    ddp = os.path.join(out, "tables", "drugdoses.parquet")
    ddf = pd.read_parquet(ddp, columns=["dd", "flags"]).set_index("dd")["flags"].fillna("").astype(str) \
        if os.path.exists(ddp) else pd.Series(dtype=str)
    cell = lines["cell_name"].astype(str).to_numpy()
    with open(CONTROL_JSON, encoding="utf-8") as fh:
        ctl = json.load(fh).get("line_controls", [])
    entries = []
    for c in ctl:
        grp, gtext = _control_lines(c.get("lines", {}), lines, out)
        dr, dtext = _control_drugs(c.get("drugs", {}), out, drugs_tab)
        entries.append({"name": c["name"], "group": grp, "group_text": gtext, "drugs": dr, "drug_text": dtext,
                        "source": c.get("source", ""), "note": c.get("note", ""), "doses": None})
    gt = truth
    if isinstance(gt, str) and gt:
        with open(gt, encoding="utf-8") as fh:
            gt = json.load(fh)
    if isinstance(gt, dict):
        ks = (gt.get("direction") or {}).get("kras_g12_selectivity") or {}
        if ks:
            entries.append({"name": "planted (synthetic): KRAS codon-12 lines x Trametinib",
                            "group": np.isin(cell, ks.get("lines", [])), "group_text": "the planted lines",
                            "drugs": [(ks.get("drug"), "planted")], "drug_text": str(ks.get("drug")),
                            "source": "ground_truth.json direction.kras_g12_selectivity",
                            "note": ks.get("expected", ""),
                            "doses": [float(x) for x in ks["doses"]] if ks.get("doses") else None})
        wt = (gt.get("groups") or {}).get("tp53_wt") or []
        if wt:
            pick = [d for d in drugs_tab["drug"].astype(str) if d.split(" (")[0] in ("Doxorubicin", "Topotecan")]
            entries.append({"name": "planted (synthetic): tp53_wt lines x Doxorubicin / Topotecan 5 µM",
                            "group": np.isin(cell, wt), "group_text": "the generator's tp53_wt lines",
                            "drugs": [(d, "planted p53 response") for d in pick], "drug_text": ", ".join(pick),
                            "source": "ground_truth.json groups.tp53_wt", "note": "", "doses": [5.0]})
    rows, met = [], []
    for e in entries:
        grp = e["group"]
        if not e["drugs"]:
            rows.append([e["name"], "No drug of this control in the screen", f"0 of {int(grp.sum())}", "-", "-", "-",
                         "-", "-", "-", "-"])
            met.append({"control": e["name"], "dd": None, "drug": "", "dose": "", "group_lines_measured": 0,
                        "group_lines": int(grp.sum()), "auroc": None, "p": None, "auroc_response_strength": None,
                        "p_response_strength": None, "group_lines_with_response_strength": 0, "top_lines": "",
                        "selective_lines": "", "flags": "", "note": "no drug of this control in the screen"})
            continue
        for d, _why in e["drugs"]:
            sub = r[r["drug"].astype(str) == str(d)]
            for (dd_, dose, conc), x in sub.groupby(["dd", "dose", "conc"], sort=True):
                if e["doses"] is not None and float(conc) not in e["doses"]:
                    continue
                x = x.set_index("line").reindex(lines["line"].to_numpy())
                meas = x["measured"].fillna(False).astype(bool).to_numpy() & np.isfinite(x["sel_z"].to_numpy(float))
                z = x["sel_z"].to_numpy(np.float64)
                g = grp & meas
                auc, p = auroc_perm(z[meas], grp[meas], LINE_PERM, stable_seed("validate", "line control", e["name"],
                                                                                int(dd_)))
                b = x["response_strength"].to_numpy(np.float64)
                hb = np.isfinite(b)
                auc_b, p_b = auroc_perm(b[hb], grp[hb], LINE_PERM, stable_seed("validate", "line control beta",
                                                                               e["name"], int(dd_)))
                o = np.argsort(-np.nan_to_num(z, nan=-np.inf), kind="mergesort")[:5]
                top = ", ".join(f"{cell[i]}{'*' if grp[i] else ''} {z[i]:.1f}" for i in o if meas[i])
                sel = x["selective"].fillna(False).astype(bool).to_numpy() & meas
                sl = ", ".join(f"{cell[i]}{'*' if grp[i] else ''}" for i in np.flatnonzero(sel)) or "none"
                fl = ddf.get(int(dd_), "")
                ftxt = ((f"{ALERT} " if has_artifact(fl) else "") + fl) if fl else ""
                rows.append([e["name"], f"{d} {dose} µM", f"{int(g.sum())} of {int(grp.sum())}", _f(auc),
                             _p_fmt(p), f"{_f(auc_b)} ({int((grp & hb).sum())} of {int(grp.sum())} lines)"
                             if np.isfinite(auc_b) else "-", _p_fmt(p_b), top or "-", sl, ftxt or "-"])
                met.append({"control": e["name"], "dd": int(dd_), "drug": str(d), "dose": str(dose),
                            "group_lines_measured": int(g.sum()), "group_lines": int(grp.sum()),
                            "auroc": None if not np.isfinite(auc) else round(auc, 4),
                            "p": None if not np.isfinite(p) else p,
                            "auroc_response_strength": None if not np.isfinite(auc_b) else round(auc_b, 4),
                            "p_response_strength": None if not np.isfinite(p_b) else p_b,
                            "group_lines_with_response_strength": int((grp & hb).sum()),
                            "top_lines": top, "selective_lines": sl,
                            "flags": fl, "note": ""})
    L += ["Lines with a recorded change (or a measured trait) that the literature says make them respond more "
          "strongly to a drug. For each drug-dose: the AUROC of the line selectivity (sel_z, "
          "tables/drug_line_response.parquet: how far a line's response strength stands above the drug-dose's other "
          "lines) of the group's measured lines against the other measured lines (1 = every group line above every "
          f"other line, 0.5 = no difference), and its permutation p ({LINE_PERM:,} shuffles of the group labels). "
          "'*' = a line of the group. 'selective lines' = lines with sel_z >= 3 and at least 20 genes beyond the "
          "per-line cut (the tables stage's rule). The same AUROC on the lines' response strength (the atlas's "
          "DD_beta: how strongly a line shows the drug-dose's pooled signature; lines of the growth analysis only) "
          "is given next to it: sel_z counts genes beyond each line's cut and says little where lines move few genes "
          "past it. A control that fails is shown like the others.", "",
          _md_table(["control", "drug-dose", "group lines measured", "AUROC (sel_z)", "p",
                     "AUROC (response strength)", "p", "5 lines with the highest sel_z", "selective lines", "flags"],
                    rows), "",
          "How each control picks its lines and drugs, and its source:", ""]
    for e in entries:
        why = "; ".join(f"{d} ({w})" for d, w in e["drugs"]) or "none in the screen"
        ng = int(e["group"].sum())
        L.append(f"- {e['name']}: {e['group_text']} ({ng} line{'' if ng == 1 else 's'}: "
                 f"{', '.join(cell[e['group']]) or 'none'}); drugs: {e['drug_text']} - in the screen: {why}. "
                 + (f"{e['note'][0].upper()}{e['note'][1:]}. " if e["note"] else "") + f"Source: {e['source']}.")
    L.append("")
    return L, met


# ----------------------------------------------------------------------------- report
def _tl_candidates(out):
    """Drugs that might block translation but are not in the translation-inhibitor class (drug_classes.json): Tahoe
    moa_fine 'Protein synthesis inhibitor', or a ChEMBL mechanism matching TL_CANDIDATE and not TL_NOT; with their
    ChEMBL mechanism and the not_members reason. Candidates, not used by the rule."""
    try:
        from . import mechanisms as MC
        a = MC.drug_annotations(out)
        rules = MC.load_rules()
        members = set()
        for k, v in (rules.get("classes") or {}).items():
            if isinstance(v, dict) and v.get("effect") == "translation":
                members |= set(MC.members(out, k))
        nm = {}
        for k, v in (rules.get("not_members") or {}).items():
            if isinstance(v, dict):
                nm.update({kk: vv for kk, vv in v.items() if not kk.startswith("_")})
    except Exception:  # noqa: BLE001
        return []
    res = []
    for _, r in a.iterrows():
        d = str(r["drug"])
        if d in members:
            continue
        mech = str(r.get("chembl_mechanisms") or "")
        tah = str(r.get("tahoe_moa_fine") or "")
        if tah == TL_TAHOE or (TL_CANDIDATE.search(mech) and not TL_NOT.search(mech)):
            why = nm.get(MC.molecule_key(d), "")
            res.append(f"{d} (Tahoe: {tah or '-'}; ChEMBL: {mech or 'no mechanism'}"
                       + (f"; not a member: {why}" if why else "") + ")")
    return res


def _um(text):
    """A control_sets.csv drug-dose list for the report: 'drug dose uM (...)' written 'drug dose µM (...)', the unit
    the rest of the report uses (the csv keeps 'uM': other stages read its items by that text)."""
    return re.sub(r" uM \(", " µM (", str(text or ""))


def _set_rows(df, n=None, n_null=N_NULL):
    rows = []
    for _, r in (df if n is None else df.head(n)).iterrows():
        tm = f"{int(r['top_module'])} ({_pct(r['top_module_share'])}; all genes {_pct(r['top_module_genome_share'])})" \
            if r["top_module"] > 0 else "-"
        p = r["p_random_sets_cos"]
        ps = f"<= {p:.3f}" if np.isfinite(p) and p <= 1.0 / (1 + n_null) + 1e-12 else _p_fmt(p)
        up = _um(r["best_dd_up"]) or "-"
        nt = r.get("best_dd_up_without_tl") if "best_dd_up_without_tl" in r else ""
        if isinstance(nt, str) and nt:
            up += f"<br>without translation inhibitors: {_um(nt)}"
        rows.append([r["set"], f"{r['n_in_space']}/{r['n_listed']}", _f(r["mean_cos"]), _f(r["auroc_cos"]),
                     _f(r["auroc_abs"]), ps, tm, up])
    return rows


SET_HEAD = ["set", "genes in space / listed", "mean cos", "AUROC cos", "AUROC abs(cos)", "p (random sets)",
            "top module (share; all genes)", "drug-doses raising it most (mean z)"]


def _tl_counts(d):
    """(sets with a translation inhibitor among the TOP_DD strongest raisers, of them at rank 1)."""
    k = r1 = 0
    for txt, nt in zip(d["best_dd_up"].fillna("").astype(str), d.get("best_dd_up_without_tl",
                                                                      pd.Series([""] * len(d))).fillna("").astype(str)):
        if nt:
            k += 1
            if txt.split("; ")[0].find(TL_WORDS) >= 0:
                r1 += 1
    return k, r1


def _opp_table(op):
    rows = []
    for _, r in op.iterrows():
        rows.append([f"{r['a']} / {r['b']}", f"{r['n_a']} / {r['n_b']}", _f(r["mean_cross_cos"], "{:+.2f}"),
                     _pct(r["frac_cross_neg"]), _f(r["auroc_anti"]),
                     f"{_pct(r['share_same_module'])} (random {_pct(r['random_same_module'])})",
                     _pct(r["share_opposite_arms_in_same_module"]),
                     f"{_f(r['nodal_centroid_dist'])} / {_f(r.get('nodal_mixing', np.nan))}",
                     f"{_f(r['signed_centroid_dist'])} / {_f(r.get('signed_mixing', np.nan))}"])
    return _md_table(["pair", "genes a / b", "mean cross cos", "cross pairs < 0", "AUROC anti",
                      "cross pairs in same module", "of those, opposite arms", "nodal map: distance / mixing",
                      "signed map: distance / mixing"], rows)


def _also_clean(alert, n):
    """The note that a top-n list also holds the n strongest items without an alert (when they fall below the cut)."""
    alert = np.asarray(alert, dtype=bool)
    extra = len(capped(np.arange(alert.size), ~alert, n)) - min(n, alert.size)
    return f", and {extra} more without an alert that the {n} strongest pushed below the cut" if extra else ""


SET_SOURCES = ("control", "hallmark", "reactome")


def _arm_tag(r):
    """' (+)' after a set label's source when the set labels one arm ('' for other labels)."""
    arm = r.get("label_arm")
    return f" ({arm})" if r.get("label_source") in SET_SOURCES and isinstance(arm, str) and arm else ""
RULE_CHANGE = ("Rule changed in validate version 7: a curated control set now wins over Hallmark and Reactome when it "
               "shares 3 or more genes and is not weak. Before, the smallest p won whatever the source, which named "
               "the metallothionein module (113) hypoxia.")


def label_counts(labels):
    """Counts of the label sources: strong set (control / hallmark / reactome, not weak), drug class, weak set,
    lineage, top genes; and the modules with each alert tag."""
    if not len(labels):
        return {}
    src = labels["label_source"].fillna("").astype(str)
    weak = labels["label_weak"].fillna(False).astype(bool)
    is_set = src.isin(SET_SOURCES)
    disp = labels["label_display"].fillna("").astype(str)
    return {"strong_set": int((is_set & ~weak).sum()),
            "strong_set_by_source": {k: int(((src == k) & ~weak).sum()) for k in SET_SOURCES},
            "drug_class": int((src == "drug class").sum()), "weak_set": int((is_set & weak).sum()),
            "lineage": int((src == "lineage").sum()), "top_genes": int((src == "top genes").sum()),
            "with_alert": int((labels["label_alert"].fillna("").astype(str) != "").sum()),
            "read_sharing_alert": int(disp.str.contains(TAG_READSHARE, regex=False).sum()),
            "lineage_alert": int(disp.str.contains(TAG_LINEAGE, regex=False).sum()),
            "chrY_alert": int(disp.str.contains(TAG_CHRY, regex=False).sum()),
            "with_driving_class": int((labels["label_drugs"].fillna("").astype(str) != "").sum())}


def _nw(n, one, many=None):
    """'1 lineage label' / '3 lineage labels' (many: the plural when it is not one + 's')."""
    return f"{n} {one if n == 1 else (many or one + 's')}"


def _modules_section(sp, labels, label_info):
    """Section 5: the modules, their labels by the version 7 rules, and every alerted module."""
    lc = label_counts(labels)
    L = ["## 5. Modules and their labels", "",
         f"Each module and each of its arms was tested against every set (hypergeometric, universe = the {sp.n:,} "
         f"genes in the space, Benjamini-Hochberg over all tests; module_enrichment.csv). A set is a candidate label "
         f"with q < {LABEL_Q} and >= {LABEL_MIN_OVERLAP} shared genes; it is strong with q < {LABEL_STRONG_Q:g}, at "
         f"least {LABEL_STRONG_FOLD:g}x the chance overlap and >= {LABEL_MIN_OVERLAP} shared genes once each group of "
         "near-identical copies (genes that can share sequencing reads) counts once; else it is weak. A curated "
         "control set that is a candidate and not weak is chosen first; else the most significant set (of <= "
         f"{LABEL_MAX_SET} genes when there is one). The label is the first of: a strong set label; the drug class "
         f"that drives the module (among its {DRIVER_TOP_DD} strongest drug-doses with a module z of at least "
         f"{DRIVER_MIN_Z:g}, the class with the most distinct compounds, at least {DRIVER_MIN_DRUGS}, or 2 when that "
         "is every compound of the class in the screen; ChEMBL's classes first, then Tahoe's moa_fine); a weak set "
         "label ('weak: ...'); a lineage label (a module whose median gene is expressed in under "
         f"{LINEAGE_MAX_SHARE:.0%} of the lines); the module's top genes. Every part keeps its own column in "
         "module_labels.csv (the set label even when another label is chosen, label_drugs, lineage_label, "
         "top_plus / top_minus), and label_display adds the alert tags.", "", RULE_CHANGE, ""]
    if lc:
        bs = lc["strong_set_by_source"]
        L += [f"Labels of the {len(labels)} modules: {_nw(lc['strong_set'], 'strong set label')} (control "
              f"{bs['control']}, Hallmark {bs['hallmark']}, Reactome {bs['reactome']}), "
              f"{_nw(lc['drug_class'], 'drug class', 'drug classes')}, {_nw(lc['weak_set'], 'weak set label')}, "
              f"{_nw(lc['lineage'], 'lineage label')}, {lc['top_genes']} by their top genes. "
              f"{_nw(lc['with_driving_class'], 'module has', 'modules have')} a driving drug class (label_drugs), "
              "whatever their "
              f"label. Drug classes from: {label_info.get('chembl_source') or 'not available'} and Tahoe's moa_fine. "
              f"Alerts: {lc['read_sharing_alert']} modules with near-identical copies ("
              + _read_sharing_words(label_info.get("read_sharing_source")) + f"), {lc['lineage_alert']} "
              "lineage-restricted (expressed "
              f"lines from {label_info.get('expressed_from') or 'not available'}), {lc['chrY_alert']} with "
              "Y-chromosome genes.", ""]
        leads = label_info.get("leads") or {}
        if leads:
            top = list(leads.items())
            L += [f"Drug classes that drive the most modules ({min(10, len(top))} of {len(top)}; all in "
                  "module_labels.csv drivers_*): " + "; ".join(f"{k} {v}" for k, v in top[:10]) + ".", ""]
        L += [f"The 20 largest ({min(20, len(labels))} of {len(labels)} modules; all {len(labels)} in "
              "module_labels.csv; 'k of N' after an arm's names: k of its N genes named, all of them in "
              "graph/nodes.parquet; 'covariate' = the graph stage's note when the module's score moves with a "
              "technical measure or the cell cycle, a note, not an alert):", ""]
        rows = [[r["module"], r["n_genes"], f"{r['n_plus']}/{r['n_minus']}", r["label_display"],
                 r["label_source"] + _arm_tag(r),
                 _p_fmt(r["label_q"]) if r["label_source"] in SET_SOURCES else "-",
                 r["covariate_tag"] if isinstance(r["covariate_tag"], str) and r["covariate_tag"] else "-",
                 _arm_names(r["top_plus"], r.get("n_plus")), _arm_names(r["top_minus"], r.get("n_minus"))]
                for _, r in labels.sort_values("n_genes", ascending=False, kind="mergesort").head(20).iterrows()]
        L += [_md_table(["module", "genes", "+/-", "label", "from (arm)", "q", "covariate", "top + arm",
                         "top - arm"], rows), ""]
        al = labels[labels["label_alert"].fillna("").astype(str) != ""]
        L += [f"**Every module with an alert** ({len(al)}):", ""]
        if len(al):
            rows = [[r["module"], r["n_genes"], r["label_display"], _f(r["median_lines_expressing"], "{:g}"),
                     r["lineage_organs"] if isinstance(r["lineage_organs"], str) and r["lineage_organs"] else "-",
                     r["label_alert"]] for _, r in al.iterrows()]
            L += [_md_table(["module", "genes", "label", "median lines expressing", "organs", "alerts"], rows), ""]
        else:
            L += ["None.", ""]
    return L, lc


def _novel_section(sp, edges, n_sets, rinfo):
    """Section 6: novel gene relations, the lineage pairs and read-sharing copies apart."""
    L = ["## 6. Novel gene relations", ""]
    if rinfo.get("novel_blocked_by"):
        L += [f"**Novelty was not assessed**: these reference sources did not load: "
              f"{', '.join(rinfo['novel_blocked_by'])}. Without them a known link or a shared locus cannot be ruled "
              "out, so no pair is called novel. Run `tahoe run --from reference` with network access.", ""]
    N = len(edges)
    lin = edges["lineage_pair"].fillna(False).astype(bool).to_numpy() if "lineage_pair" in edges and N else \
        np.zeros(N, dtype=bool)
    lp = pd.to_numeric(edges["lineage_p"], errors="coerce").to_numpy() if "lineage_p" in edges and N else \
        np.full(N, np.nan)
    rs = edges["read_sharing"].fillna("").astype(str).to_numpy() != "" if "read_sharing" in edges and N else \
        np.zeros(N, dtype=bool)
    k, k01, r = int(lin.sum()), int((lin & (lp >= LINEAGE_P_STRONG)).sum()), int(rs.sum())
    e_alert = edges["alert"].fillna("").astype(str).to_numpy() != "" if "alert" in edges else np.zeros(N, dtype=bool)
    L += ["Pairs (one row per pair) reproduced in both halves of the compounds (the same sign in both halves, fdr <= "
          "0.05, |cos| >= 0.5) with no shared HGNC gene group, no shared Hallmark / Reactome pathway and no STRING "
          "link, and not the same locus or a read-through pair. The halves share the lines and plates, so this "
          "guards against single-compound effects, not against everything.", "",
          f"{N:,} novel pairs; {k:,} of them ({ALERT}) are lineage pairs (both genes expressed in few lines, mostly "
          f"the same ones; {k01:,} of them no stronger than 99% of such pairs); {r:,} are read-sharing copies "
          f"({ALERT}); {N - k:,} are not lineage pairs. {int(e_alert.sum()):,} pairs carry an alert of any kind "
          "(novel_edges.csv alert).", ""]

    def table(sel, title):
        idx = np.flatnonzero(sel)
        if not len(idx):
            return [f"{title}: none.", ""]
        sub = edges.iloc[idx]
        alert = e_alert[idx]
        shown = capped(np.arange(len(sub)), ~alert, NOVEL_TOP)
        fo = sp.flagged_only
        rows = []
        for _, r_ in sub.iloc[shown].iterrows():
            lt = (f"{int(r_['n_lines_a'])} / {int(r_['n_lines_b'])} lines, J {_f(r_['lines_jaccard'])}"
                  + (f", lineage p {_p_fmt(r_['lineage_p'])}" if r_.get("lineage_pair") else "")) \
                if "n_lines_a" in r_ and pd.notna(r_.get("n_lines_a")) else "-"
            rows.append([f"{r_['symbol_a']}{' ' + ALERT if fo[r_['col_a']] else ''} ({r_['module_a']}{r_['arm_a']})",
                         f"{r_['symbol_b']}{' ' + ALERT if fo[r_['col_b']] else ''} ({r_['module_b']}{r_['arm_b']})",
                         _f(r_["cos"], "{:+.2f}"),
                         f"{_f(r_['cos_half1'], '{:+.2f}')} / {_f(r_['cos_half2'], '{:+.2f}')}",
                         _p_fmt(r_["fdr"]), lt, (_clip(r_["name_a"], 40) or "-") + " / " + (_clip(r_["name_b"], 40)
                                                                                           or "-"),
                         _clip(r_["alert"], 160) if isinstance(r_["alert"], str) and r_["alert"] else "-"])
        return [f"{title} ({min(NOVEL_TOP, len(sub))} of {len(sub):,} by |cos|{_also_clean(alert, NOVEL_TOP)}; all in "
                "novel_edges.csv):", "",
                _md_table(["gene a (module arm)", "gene b (module arm)", "cos", "cos half1 / half2", "fdr",
                           "lines expressing a / b", "names", "alert"], rows), ""]
    if N:
        L += table(~lin, "Top pairs without a lineage alert")
        L += table(lin, f"Top lineage pairs {ALERT}")
    elif not n_sets.get("reference"):
        L += ["Nothing can be called novel without the reference stage.", ""]
    return L, {"edges_lineage": k, "edges_lineage_p_ge_0.01": k01, "edges_read_sharing": r}


DIR_KIND_WORDS = {"genotype_response": "recorded mutation -> a gene's drug response",
                  "genotype_baseline": "recorded mutation -> a gene's baseline level",
                  "genotype_sensitivity": "recorded mutation -> cells under a drug-dose",
                  "genotype_selectivity": "recorded mutation -> the lines' response strength to a drug-dose",
                  "null_response": "not expressed (natural knockout) -> a partner's drug response",
                  "null_baseline": "not expressed (natural knockout) -> a partner's baseline level",
                  "null_sensitivity": "not expressed (natural knockout) -> cells under a drug-dose",
                  "null_selectivity": "not expressed (natural knockout) -> the lines' response strength to a drug-dose",
                  "drug_target": "compounds that target a gene -> a gene's level",
                  "level": "natural level -> a partner's drug response",
                  "level_sensitivity": "natural level -> cells under a drug-dose"}
DIR_GRADES = ("A: passes every check listed in direction/README.md; B: read its alerts; C: a glimpse, a lead to check, "
              "not a finding")


def _kind_words(DV, kind):
    """The plain words of a direction kind: DIR_KIND_WORDS, else direction_view's KIND_SHORT / KIND_WORDS (a kind
    added after this version), else the kind's name."""
    return DIR_KIND_WORDS.get(kind) or getattr(DV, "KIND_SHORT", {}).get(kind) or \
        getattr(DV, "KIND_WORDS", {}).get(kind) or kind


def _share_text(x):
    """A false or non-specific share as the direction stage prints it: 'under 1%' below 0.005, else whole percent."""
    try:
        x = float(x)
    except (TypeError, ValueError):
        return "-"
    if not np.isfinite(x):
        return "-"
    return "under 1%" if x < 0.005 else f"{x:.0%}"


def _planted_direction(name, p, e, ctl):
    """One line (and metrics) for a planted direction answer of the synthetic truth that has no kind / source (the
    generator's newer plants): what the direction output shows for it."""
    exp = str(p.get("expected", ""))
    m = {"planted": None, "found": None}
    pos = (ctl.get("positive") or {}) if isinstance(ctl, dict) else {}
    if name == "top2_poisons":
        genes = set(p.get("genes") or [])
        sel = e[(e["kind"] == "drug_target") & (e["target"].isin(genes))] if len(e) else e
        mc = sel["mechanism_class"].fillna("").astype(str) if "mechanism_class" in sel else pd.Series([], dtype=str)
        trap = sel[mc.str.contains("TOP2", case=False)] if len(sel) else sel
        signs = sorted({int(x) for x in trap["sign"]}) if len(trap) else []
        grades = trap["grade"].value_counts().to_dict() if len(trap) else {}
        m.update(planted=len(genes), found=int(trap["target"].nunique()) if len(trap) else 0, signs=signs)
        txt = (f"{m['found']} of the {len(genes)} planted genes come back as TOP2-poison drug-target arrows "
               f"(signs {signs or '-'}; grades {grades or '-'}): a trapped enzyme's sign is not inferred")
    elif name == "promiscuous_gr_gene":
        g = str(p.get("gene"))
        sel = e[(e["kind"] == "drug_target") & (e["target"] == g)] if len(e) else e
        rows = [f"{r['source']} (q {fmt_q(r['q'], '{:.2g}')}, grade {r['grade']}, sign {int(r['sign']):+d})"
                for _, r in sel.sort_values("q").head(10).iterrows()] if len(sel) else []
        m.update(planted=1, found=int(len(sel)))
        txt = (f"{len(sel)} drug-target arrow{'' if len(sel) == 1 else 's'} into {g}"
               + (": " + "; ".join(rows) if rows else "")
               + (f" ({len(sel) - 10} more in direction/edges.parquet)" if len(sel) > 10 else ""))
    elif name in ("kras_g12_selectivity", "one_dose_selective"):
        d = str(p.get("drug"))
        sel = e[e["kind"].astype(str).str.endswith("selectivity") & e["target"].astype(str).str.contains(
            re.escape(d), regex=True)] if len(e) else e
        rows = [f"{r['source']} → {r['target']} (q {fmt_q(r['q'], '{:.2g}')}, grade {r['grade']}, "
                f"sign {int(r['sign']):+d})" for _, r in sel.head(10).iterrows()] if len(sel) else []
        m.update(planted=1, found=int(len(sel)))
        txt = (f"{len(sel)} selectivity arrow{'' if len(sel) == 1 else 's'} into the response to {d}"
               + (": " + "; ".join(rows) if rows else ""))
    elif name == "programme":
        genes = set(p.get("genes") or [])
        sel = e[e["source"].isin(genes) & e["kind"].astype(str).str.startswith("null")] if len(e) else e
        prog = sel[pd.to_numeric(sel["programme_sets"], errors="coerce").fillna(-1) > 0] \
            if "programme_sets" in sel and len(sel) else sel.iloc[0:0]
        grades = sel["grade"].value_counts().to_dict() if len(sel) else {}
        m.update(planted=len(genes), found=int(sel["source"].nunique()) if len(sel) else 0)
        txt = (f"{len(sel)} natural-knockout arrows from {m['found']} of the {len(genes)} programme genes "
               f"(grades {grades or '-'}; {len(prog)} of them read as an expression programme, other line sets "
               "overlapping)")
    elif name == "p53_fall_target":
        g = str(p.get("gene"))
        per = []
        for k, v in pos.items():
            per += [x for x in (v.get("per_gene") or []) if x.get("gene") == g]
        x = per[0] if per else {}
        m.update(planted=1, found=int(bool(x.get("counted"))))
        txt = (f"{g} in the p53 control: " + ("counted as recovered" if x.get("counted") else
                                               f"not counted ({x.get('why_not') or 'not tested'})") if x
               else f"{g} is not among the p53 control's genes")
    else:
        txt = "no automatic check for this plant"
    return f"- {name}: {txt}." + (f" Planted: {exp}" if exp else ""), m


def _direction_section(out, truth=None):
    """Section 10 of report.md and metrics.json 'direction': the direction stage's positive controls with ranks (the
    p53 control's counted and not-counted targets with why), per kind the edges written against the false or
    non-specific edges its controls expect (random pseudo-genotype groups, random genes and random line sets for the
    natural knockouts, permuted levels), the grade-A arrows' group false shares, counts by grade, the same-locus
    check, and (truth) the planted direction answers. Every newer key is read with .get, so an older direction output
    still renders. When the stage has not run (an older output): one sentence that says so, and None."""
    from . import direction_view as DV
    head = "## 10. Direction: which gene probably acts on which"
    dv = DV.load(out, cache=False)
    if dv is None:
        return [head, "",
                "The direction stage has not run on this output: `tahoe run` adds it, then rebuilds this report, the "
                "vault and the map.", ""], None
    e, ctl, inf = dv.edges, dv.controls or {}, dv.info or {}
    grades = {g: int((e["grade"] == g).sum()) for g in DV.GRADES} if len(e) else {g: 0 for g in DV.GRADES}
    n_alert = int(e["has_alert"].sum()) if len(e) and "has_alert" in e else 0
    kinds = list(getattr(DV, "KINDS", ()))
    if not kinds and len(e):
        kinds = sorted(set(e["kind"].astype(str)))
    L = [head, "",
         "From the direction stage (direction/; its README.md documents the columns and lists every check; "
         "docs/direction.md explains the method): arrows SOURCE → TARGET from recorded mutations, natural knockouts "
         "(lines that do not express a gene), compounds annotated to act on a gene, and genes' natural levels across "
         f"the lines, each with a p, a Benjamini-Hochberg q, a grade and its alerts. {DV.CAVEAT}", "",
         f"{len(e):,} edges ({len(dv.rows):,} rows once edges that are one test for several sources are merged) "
         f"in {len(kinds)} kinds: grade A {grades['A']:,}, B {grades['B']:,}, C {grades['C']:,}; {n_alert:,} with an "
         f"alert ({ALERT}). Grades: {DIR_GRADES}.", ""]
    met = {"edges": int(len(e)), "rows": int(len(dv.rows)), "by_grade": grades, "with_alert": n_alert,
           "positive": {}, "expected_false_edges": {}, "synthetic": {}, "kinds": {}}
    # ---- positive controls
    pos = ctl.get("positive") or {}
    if pos:
        L += ["**Positive controls** (known biology that has to come back):", ""]
    for k, v in pos.items():
        marks = dv.control_alerts(k, v) if hasattr(dv, "control_alerts") else {}

        def mk(nm, marks=marks):
            return f" {ALERT}" if marks.get(str(nm)) else ""
        if "per_gene" in v:
            per = sorted(v["per_gene"], key=lambda x: (x.get("rank") or 10 ** 9))
            has_counted = any("counted" in x for x in per)
            if has_counted:
                rec = [x for x in per if x.get("counted")]
                miss = [x for x in per if not x.get("counted")]
            else:
                rec = [x for x in per if x.get("edge") and x.get("sign") == 1]
                miss = [x for x in per if not (x.get("edge") and x.get("sign") == 1)]
            shown = ", ".join(f"{x['gene']} (rank {x.get('rank')}, {x.get('grade')}{mk(x['gene'])})" for x in rec) \
                or "none"
            why = [f"{x['gene']} (rank {x.get('rank')}: {x.get('why_not') or 'not an edge with the right sign'})"
                   for x in miss]
            L.append(f"- {k}: {v.get('recovered_right_sign')} of the {v.get('targets_present')} p53 target genes "
                     f"present counted as recovered ({v.get('wrong_sign', 0)} with the wrong sign); median rank "
                     f"{_f(v.get('median_rank'), '{:.0f}')} of {v.get('genes_ranked', 0):,} genes. "
                     + (f"Expected: {v['expected']}. " if v.get("expected") else "")
                     + f"Counted (rank among all genes, grade; {ALERT} = the arrow carries an alert): {shown}. "
                     f"Not counted ({len(miss)}, each with why): {'; '.join(why) or 'none'}.")
            for x in v.get("edge_not_counted") or []:
                L.append(f"  - an edge that is not counted: {x.get('gene')} ({x.get('why_not')})")
            met["positive"][k] = {"present": v.get("targets_present"),
                                  "recovered_right_sign": v.get("recovered_right_sign"),
                                  "wrong_sign": v.get("wrong_sign"), "median_rank": v.get("median_rank"),
                                  "ranks_recovered": [x.get("rank") for x in rec],
                                  "not_counted": {x["gene"]: x.get("why_not", "") for x in miss}}
        elif v.get("assessable") is False:
            L.append(f"- {k}: not assessable ({v.get('why', '')})")
            met["positive"][k] = {"assessable": False, "why": v.get("why", "")}
        elif "drugdoses_tested" in v:
            dds = v.get("drugdoses") or []
            whys = v.get("drugdoses_why") or []
            items = [str(x) + mk(x) + (f" [{whys[i]}]" if i < len(whys) and whys[i] else "")
                     for i, x in enumerate(dds)]
            right = v.get("right_sign", v.get("right_sign_doses"))
            L.append(f"- {k}: {v.get('edges')} edges among {v.get('drugdoses_tested')} drug-doses tested, {right} with "
                     f"the expected sign ({v.get('expected', '')})"
                     + (f", {v.get('wrong_sign')} with the other sign" if v.get("wrong_sign") else "")
                     + (": " + "; ".join(items) if items else ""))
            met["positive"][k] = {"edges": v.get("edges"), "right_sign": right,
                                  "drugdoses_tested": v.get("drugdoses_tested")}
        else:
            L.append(f"- {k}: {v.get('recovered_right_sign', 0)} of {v.get('targets_present', 0)} recovered with the "
                     f"right sign ({v.get('wrong_sign', 0)} with the wrong sign): "
                     + (", ".join(str(x) + mk(x) for x in v.get("genes") or []) or "none"))
            met["positive"][k] = {"recovered_right_sign": v.get("recovered_right_sign"),
                                  "wrong_sign": v.get("wrong_sign")}
    if pos:
        L.append("")
    # ---- per kind: real edges vs the expected false (or non-specific) edges
    exp = ctl.get("expected_false_edges") or {}
    nullc = ctl.get("null_controls") or {}
    rows = []
    wide = ((e["q"] < 0.10) & (e["q_group"].isna() | (e["q_group"] < 0.10))) if len(e) else pd.Series(dtype=bool)

    def gr(sel):
        return "/".join(str(int((sel["grade"] == g).sum())) for g in DV.GRADES)
    label = {}                                     # metrics key -> its plain-words row label
    for kind in kinds:
        sel = e[e["kind"] == kind] if len(e) else e
        words = _kind_words(DV, kind)
        met["kinds"][kind] = {"edges": int(len(sel)), "by_grade": {g: int((sel["grade"] == g).sum())
                                                                   for g in DV.GRADES} if len(sel) else {}}
        if kind.startswith(("genotype", "level")):
            parts = [(kind, "over the whole table", sel[wide[sel.index]] if len(sel) else sel)]
            if kind.startswith("genotype") or kind == "level_sensitivity":
                key = f"{kind}_within_group_only" if kind.startswith("genotype") else f"{kind}_within_drugdose_only"
                what = "within its group only" if kind.startswith("genotype") else "within its drug-dose only"
                parts.append((key, what, sel[~wide[sel.index]] if len(sel) else sel))
            ctl_w = "random pseudo-genotype groups" if kind.startswith("genotype") else \
                "the same tests with every level permuted"
            for key, what, sub in parts:
                x = exp.get(key) or {}
                rows.append([f"{words} ({what})", len(sub), gr(sub), DV.expected_text(x), ctl_w])
                label[key] = f"{words} ({what})"
                met["expected_false_edges"][key] = {"edges": int(len(sub)), "expected_false": x.get("expected_false"),
                                                    "expected_false_upper": x.get("expected_false_upper")}
        elif kind in ("null_baseline", "null_response") and (exp.get(kind) or {}).get("expected_nonspecific") \
                is not None:
            x = exp[kind]
            rows.append([words, len(sel), gr(sel), f"{_f(x.get('expected_nonspecific'))} non-specific",
                         "random genes that are not partners, tested the same way: the arrows that would appear for "
                         "any gene"])
            met["expected_false_edges"][kind] = {"edges": int(len(sel)),
                                                 "expected_nonspecific": x.get("expected_nonspecific")}
        elif kind in ("null_sensitivity", "null_selectivity") and (exp.get(kind) or {}).get("expected_false") \
                is not None:
            x = exp[kind]
            rows.append([words, len(sel), gr(sel), DV.expected_text(x), "random line sets of the real sets' sizes"])
            label[kind] = words
            met["expected_false_edges"][kind] = {"edges": int(len(sel)), "expected_false": x.get("expected_false"),
                                                 "expected_false_upper": x.get("expected_false_upper")}
        else:
            rows.append([words, len(sel), gr(sel), "-", "no random control (each edge's alerts say what to doubt)"])
    L += ["**Edges per kind against the controls.** 'Expected false' = the edges a table without any real effect "
          "would hold: random pseudo-genotype groups (line sets drawn at random, tested exactly like the recorded "
          "groups, counted at the real table's cut), random line sets for the natural knockouts' cells and response "
          "strength, and, for the level kinds, the same tests with every gene's level permuted over its lines. "
          "'Non-specific' (natural knockouts' level and response) = the arrows that random genes which are not "
          "partners would give as often: differences between these lines that are not specific to the partners.", "",
          _md_table(["evidence", "edges", "A / B / C", "expected false or non-specific", "control"], rows), "",
          DV.CONTROLS_CAVEAT, ""]
    for k, v in exp.items():
        if isinstance(v, dict) and v.get("how") and k in ("null_baseline", "null_response", "null_sensitivity",
                                                          "null_selectivity"):
            L.append(f"- {_kind_words(DV, k)}: {v['how']}.")
    rates = nullc.get("rates") or {}
    if rates:
        bins = nullc.get("bins") or []
        for k, r in rates.items():
            L.append(f"- random-gene rate per test, {_kind_words(DV, k)}, by how many other line sets overlap the "
                     "lines lacking the gene: " + ", ".join(f"{b} {x:.2%}" if isinstance(x, (int, float)) else
                                                            f"{b} -" for b, x in zip(bins, r)) + ".")
    for k, v in (nullc.get("line_sets") or {}).items():
        L.append(f"- {_kind_words(DV, k)}: {v.get('pseudo_sets')} random line sets gave {v.get('arrows')} arrows "
                 f"({_f(v.get('rate_per_set'), '{:.3f}')} per set, up to {_f(v.get('upper_per_set'), '{:.3f}')}); "
                 f"x the {v.get('real_sets_tested')} real sets tested = {_f(v.get('expected_false'))} expected false "
                 f"(up to {_f(v.get('expected_false_upper'))}).")
    if rates or nullc.get("line_sets") or any(k.startswith("null") for k in exp):
        L.append("")
    warn = [f"{label.get(k, k)} ({v.get('edges')} edge{'' if v.get('edges') == 1 else 's'}, "
            f"{v.get('expected_false')} expected false)"
            for k, v in met["expected_false_edges"].items()
            if v.get("expected_false") is not None and v.get("edges") and v["expected_false"] >= 0.5 * v["edges"]]
    if warn:
        L += [f"{ALERT} The controls expect at least half of these edges to be false: " + "; ".join(warn)
              + ". Read them as leads.", ""]
    # ---- grade-A arrows: each group's expected false share (genotype kinds)
    if len(e) and "false_share" in e:
        fa = e[(e["grade"] == "A") & e["kind"].astype(str).str.startswith("genotype")]
        fs = pd.to_numeric(fa["false_share"], errors="coerce")
        hi = pd.to_numeric(e["false_share"], errors="coerce") >= 0.2
        lines_ = []
        for kind, g in fa.groupby("kind"):
            f = pd.to_numeric(g["false_share"], errors="coerce")
            lines_.append(f"{_kind_words(DV, kind)}: {len(g)} grade-A arrows, their groups' expected false share "
                          f"median {_share_text(f.median())}, at most {_share_text(f.max())}")
        L += ["**Grade-A arrows and their group's false share.** Each genotype arrow carries the share of its group's "
              "arrows that random groups of the same size would give (false_share; 20% or more is an alert and "
              "blocks grade A). " + ("; ".join(lines_) + "." if lines_ else "No grade-A genotype arrow.")
              + f" Over all genotype arrows, {int(hi.sum())} sit in a group at 20% or more.", ""]
        met["grade_a_false_share"] = {"arrows": int(len(fa)), "median": None if fs.dropna().empty else
                                      float(fs.median()), "max": None if fs.dropna().empty else float(fs.max()),
                                      "arrows_at_or_above_20pct": int(hi.sum())}
    neg = (ctl.get("negative") or {}).get("summary") or {}
    if neg:
        L += [f"Random pseudo-groups ({(inf.get('groups_tested') or {}).get('pseudo_controls', '?')} groups): edges "
              "per group over the whole table, pseudo vs real: " + "; ".join(
                  f"{k} {v.get('pseudo_edges_mean_per_group')} vs {v.get('real_edges_mean_per_group')}"
                  for k, v in neg.items()) + ".", ""]
    tw = inf.get("tests_written_by_kind") or {}
    if tw:
        L += ["Distinct tests written per kind (one test can give arrows for several sources): "
              + ", ".join(f"{_kind_words(DV, k)} {v:,}" for k, v in tw.items()) + ".", ""]
    sl = inf.get("same_locus_check") or {}
    if sl:
        L += [("Same locus (source and target within "
               f"{int(sl.get('max_bp') or 0) / 1e6:g} Mb, deleted or gained together): "
               + (f"{sl.get('edges_same_locus', 0)} of the {sl.get('edges_checked', 0)} arrows checked; "
                  f"{sl.get('text') or ''} (genes without coordinates cannot be checked)." if sl.get("ran") else
                  f"not checked ({sl.get('text') or 'no gene coordinates'}).")), ""]
        met["same_locus"] = {k: sl.get(k) for k in ("ran", "genes", "genes_with_coordinates", "edges_checked",
                                                    "edges_same_locus")}
    # ---- the synthetic truth's planted direction answers (truth: ground_truth.json's path, or its content)
    if isinstance(truth, str) and truth:
        try:
            with open(truth, encoding="utf-8") as fh:
                truth = json.load(fh)
        except (OSError, ValueError):
            truth = None
    planted = (truth if isinstance(truth, dict) else {}).get("direction") or {}
    if planted:
        L += ["**Synthetic ground truth** (ground_truth.json 'direction'; the generator's planted answers):", ""]
        for name, p in planted.items():
            if not (p.get("kind") and p.get("source")):
                line, m = _planted_direction(name, p, e, ctl)
                L.append(line)
                met["synthetic"][name] = m
                continue
            tg = set(p.get("targets") or p.get("partners") or [])
            sel = e[(e["kind"] == p.get("kind")) & (e["source"] == p.get("source"))] if len(e) else e
            hit = sel[sel["target"].isin(tg)] if len(sel) else sel
            right = hit[hit["sign"] == p.get("sign", 1)] if len(hit) else hit
            clear = int(right["direction_clear"].fillna(False).astype(bool).sum()) if len(right) and \
                p.get("kind") == "level" else None
            L.append(f"- {name}: {p.get('source')} → {len(right)} of the {len(tg)} planted targets as "
                     f"{p.get('kind')} edges with the right sign ({len(hit) - len(right)} with the other sign)"
                     + (f", {clear} with the direction clear (the reverse clearly weaker, allowing for the arrow "
                        "having been selected because it is strong)" if clear is not None else "")
                     + (f"; grades {right['grade'].value_counts().to_dict()}" if len(right) else ""))
            met["synthetic"][name] = {"planted": len(tg), "recovered_right_sign": int(len(right)),
                                      "other_sign": int(len(hit) - len(right)), "direction_clear": clear}
        L.append("")
    return L, met


def _read_sharing_words(src):
    """The read-sharing clause of the report's label summary from relations.read_sharing_source: 'read sharing;
    pairs from Compara 112 + HGNC', or 'read sharing not assessed: HGNC and the Compara paralogues did not load'."""
    src = str(src or "?")
    if src.startswith("not assessed"):
        why = src[len("not assessed"):].strip().strip("()")
        why = why.replace(" not loaded", " did not load")
        return "read sharing not assessed" + (f": {why}" if why else "")
    return f"read sharing; pairs from {src}"


def _n_lines(out, label_info=None):
    """The cell lines of this run: label_info 'lines' (module labels), else the rows of tables/lines.parquet; None
    when neither is there."""
    n = (label_info or {}).get("lines")
    if n:
        return int(n)
    p = os.path.join(out, "tables", "lines.parquet") if out else ""
    try:
        return int(len(pd.read_parquet(p, columns=["line"]))) if p and os.path.exists(p) else None
    except Exception:  # noqa: BLE001
        return None


def _report(path, ctx):
    sp, cs, op, labels, edges, members, drug, drug_tab, n_sets, n_null = (
        ctx["sp"], ctx["cs"], ctx["op"], ctx["labels"], ctx["edges"], ctx["members"], ctx["drug"], ctx["drug_tab"],
        ctx["n_sets"], ctx["n_null"])
    L = ["# Validation report", "",
         f"Written by `tahoemap validate` (tahoemap/validate.py, version {VERSION}) on "
         f"{time.strftime('%Y-%m-%d %H:%M')}. "
         f"{sp.n:,} genes are in the vector space ({sp.U.shape[1]} dimensions); the nodal map has "
         f"{sp.n_modules} modules. `cos` is the signed cosine of two genes' unit vectors: the correlation of their "
         f"denoised responses over every (drug-dose, cell line) context (+1 = always move together, -1 = always "
         f"opposite). AUROC = probability that a pair of genes from the set has a higher cosine than a random pair "
         f"of genes in the space (0.5 = no better than random, 1 = every set pair beats every random pair). "
         f"'p (random sets)' = share of {n_null} random gene sets of the same size that score at least as high.", "",
         "Sections: 1 known programmes, 2 opposite programmes, 3 drug check, 4 neighbouring wells, 5 modules and "
         "labels, 6 novel gene relations, 7 novel module members, 8 line-selective responses, 9 synthetic ground "
         "truth (synthetic data only), 10 direction; then caveats and files.", ""]

    ctl = cs[cs["source"] == "control"].sort_values("auroc_cos", ascending=False, na_position="last")
    tested = ctl[ctl["n_in_space"] >= 2]
    k_tl, r1_tl = _tl_counts(ctl)
    L += ["## 1. Do known programmes hang together in the vector space?", "",
          f"Curated control sets (tahoemap/data/control_sets.json; literature, not Tahoe), ranked by AUROC on cos. "
          f"{len(tested)} of {len(ctl)} sets have >= 2 genes in the space; "
          f"{int((tested['auroc_cos'] >= 0.6).sum())} reach AUROC >= 0.6 and "
          f"{int((tested['p_random_sets_cos'] <= 0.05).sum())} have p <= 0.05 against random sets. "
          f"'top module' = the module holding most of the set's genes, its share of the set, and its share of all "
          f"genes (the chance level). Every drug-dose keeps its ranked place; {ALERT} and its flags in plain words "
          f"mark one with an artifact flag (technically untrustworthy ones and 'like a neighbouring well' included; "
          f"the flags of record of the tables stage), and when the {TOP_DD} strongest "
          f"hold such drug-doses, the {TOP_DD} strongest without an alert follow in their ranked place too. For a "
          f"cell-cycle shift the share of the set's mean change that the shift would explain is given (the tables "
          f"stage's rule; a shift that does not explain the change is named without {ALERT}). A drug-dose of the "
          f"translation-inhibitor class reads '({TL_WORDS})': blocking translation stabilises short-lived mRNAs, so "
          "a rise there may not be more transcription; when one is among a set's "
          f"{TOP_DD} strongest raisers, the cell adds the {TOP_DD} strongest raisers without translation inhibitors. "
          f"{k_tl} of the {len(ctl)} curated sets have a translation inhibitor among their {TOP_DD} strongest "
          f"raisers ({r1_tl} at rank 1).", "",
          _md_table(SET_HEAD, _set_rows(ctl, n_null=n_null)), ""]
    for src, title in (("hallmark", "MSigDB Hallmark"), ("reactome", "Reactome")):
        d = cs[cs["source"] == src]
        if not len(d):
            continue
        k_, r1_ = _tl_counts(d)
        L += [f"**{title}** ({len(d)} sets with >= {MIN_SET} genes in the space): median AUROC on cos "
              f"{_f(d['auroc_cos'].median())}, {int((d['auroc_cos'] >= 0.6).sum())} sets "
              f"({_pct((d['auroc_cos'] >= 0.6).mean())}) "
              f"at >= 0.6" + (f", {int((d['p_random_sets_cos'] <= 0.05).sum())} with p <= 0.05 against random sets"
                              if d["p_random_sets_cos"].notna().any() else "")
              + f"; {k_} with a translation inhibitor among their {TOP_DD} strongest raisers ({r1_} at rank 1; "
              "control_sets.csv best_dd_up_without_tl gives their lists without them).", ""]
        if src == "hallmark":
            L += [_md_table(SET_HEAD, _set_rows(d.sort_values("auroc_cos", ascending=False), 12, n_null)), ""]
    if not n_sets.get("reference"):
        L += ["No Hallmark / Reactome sets: the reference stage did not run (or found no sets).", ""]
    cand = ctx.get("tl_candidates") or []
    L += ["Translation inhibitors here are the members of the class in tahoemap/data/drug_classes.json "
          "(tables/README.md 'Drug classes used by rules'). Drugs that might also block translation but are not in "
          "the class (Tahoe moa_fine 'Protein synthesis inhibitor', or a ChEMBL mechanism naming protein synthesis or "
          "the ribosome, bacterial ones left out) - candidates, not used by the rule: "
          + ("; ".join(cand) if cand else "none in this screen") + ".", ""]

    L += ["## 2. Opposite programmes: apart in the vector space, together on the nodal map", "",
          "Pairs of programmes expected to move in opposite directions under the same drugs. In the signed vector "
          "space they should be anti-aligned (mean cross-set cosine < 0, most cross pairs negative); the nodal map "
          "is built on |cos|, so it should put them in the same module (on opposite arms) and close together, while "
          "the signed map keeps them apart. Map distances are centroid distances divided by the map's spread "
          "(sqrt(var x + var y)); mixing = how often a gene's 5 nearest map neighbours (among both sets) come from "
          "the other set, relative to chance (1 = as mixed as chance, 0 = never). t-SNE keeps neighbourhoods, not "
          "long distances, so 'apart on the signed map' is read from the mixing (at most 0.25); how far apart two "
          "separate islands land varies from machine to machine. 'AUROC anti' = P(cross pair cos < random pair cos).",
          ""]
    ctl_op = op[op["source"] == "control"] if len(op) else op
    if len(ctl_op):
        L += [_opp_table(ctl_op), ""]
        L += ["- " + _reading(r) for _, r in ctl_op.iterrows()]
        L += [""]

    L += ["## 3. Drug check: do drugs with the same mechanism get similar vectors?", ""]
    if drug:
        csrc = drug.get("chembl_source", "ChEMBL")
        rows = []
        for tag in ("all", "active"):
            t, c = drug["tahoe"][tag], drug["chembl"][tag]
            lab = "all drugs with a class" if tag == "all" else \
                f"active drugs only (best dose >= {drug.get('min_active', 10)} significant genes)"
            rows.append([lab, f"{t['drugs']} / {c['drugs']}", f"{t['classes']} / {c['classes']}",
                         f"{t['pos_pairs']:,} / {c['pos_pairs']:,}",
                         f"{_f(t['mean_cos_same'], '{:+.2f}')} vs {_f(t['mean_cos_other'], '{:+.2f}')} / "
                         f"{_f(c['mean_cos_same'], '{:+.2f}')} vs {_f(c['mean_cos_other'], '{:+.2f}')}",
                         f"{_f(t['auroc'], '{:.3f}')} / {_f(c['auroc'], '{:.3f}')}"])
        n_untr = drug["tahoe"]["all"].get("drugs_no_trustworthy_dose", 0)
        n_fl = drug["tahoe"]["all"].get("drugs_flagged_dose", 0)
        L += ["Cosine of drug vectors (each drug's best trustworthy dose) for pairs of drugs that share a class vs "
              "pairs that do not, with two class sources side by side: Tahoe's moa_fine ('unclear' / 'unknown' left "
              f"out) and the mechanism classes ({csrc}: the class labels of tahoemap/data/drug_classes.json - ChEMBL "
              "mechanism rules, WHO ATC via ChEMBL and cited code constants - or, for a drug in none of them, its "
              "ChEMBL mechanism texts). Two drugs of one molecule (the same ChEMBL id, else the same name without its "
              "salt) are never paired."
              + (f" {n_fl} of the drugs with a Tahoe class get the vector of a dose with an artifact flag (marked "
                 f"{ALERT} in drug_moa.csv; embed/drugs.parquet alert says which)" if n_fl else "")
              + (f", {n_untr} of them because they have no trustworthy dose (every dose flagged unreliable plate "
                 f"only, position not correctable or wells disagree)" if n_untr else "")
              + ("; they are tested like the others." if n_fl else ""), "",
              _md_table(["drugs", f"drugs (Tahoe / {csrc})", "classes", "same-class pairs",
                         "mean cos same vs other", "AUROC"], rows), ""]
        if len(drug_tab):
            tt = drug_tab[drug_tab["class_source"] == "Tahoe"]
            tc = drug_tab[drug_tab["class_source"] != "Tahoe"]
            used, rows = set(), []
            for _, r in tt.iterrows():
                m = [i for i, c in zip(tc.index, tc["class"]) if i not in used and _same_class(c, r["class"])]
                used.update(m)
                rc = tc.loc[m[0]] if m else None
                rows.append([r["class"], r["drugs"], _f(r["auroc_within_vs_other"]),
                             rc["class"] if rc is not None else "-", rc["drugs"] if rc is not None else "-",
                             _f(rc["auroc_within_vs_other"]) if rc is not None else "-"])
            for i, r in tc.iterrows():
                if i not in used:
                    rows.append(["-", "-", "-", r["class"], r["drugs"], _f(r["auroc_within_vs_other"])])
            L += [f"Every class with >= 2 drugs, one row per class, the two sources side by side where they name the "
                  f"same class ({len(tt)} Tahoe classes, {len(tc)} {csrc} classes; drug_moa.csv has their pair "
                  "counts and mean cosines):", "",
                  _md_table(["Tahoe class", "drugs", "AUROC", f"{csrc} class", "drugs", "AUROC"], rows), ""]
        counts, arows = ctx.get("annotation") or ({}, [])
        if counts or arows:
            L += ["**Annotation agreement** (tables/drugs.parquet annotation_status; a drug can carry several "
                  "statuses): " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))
                  + f". Every drug whose two annotations disagree ({len(arows)}; Tahoe's annotation is never "
                  "overwritten):", ""]
            if arows:
                L += [_md_table(["drug", "Tahoe", "ChEMBL", "alert"], arows), ""]
    else:
        L += ["No drug vectors (embed stage files missing).", ""]

    L += ctx.get("nb_lines") or []
    ml, _lc = _modules_section(sp, labels, ctx.get("label_info") or {})
    L += ml
    rinfo = ctx.get("rinfo") or {}
    nl, _nm = _novel_section(sp, edges, n_sets, rinfo)
    L += nl

    top = members.drop_duplicates("col") if len(members) else members
    m_alert = top["alert"].fillna("").astype(str).to_numpy() != "" if "alert" in top else \
        np.zeros(len(top), dtype=bool)
    L += ["## 7. Novel module members (guilt by association)", "",
          f"Genes on a module arm enriched for a set (q < {GBA_Q}; sets of <= {LABEL_MAX_SET} genes in the space, "
          f">= {GBA_MIN_ANNOT} of them on the arm) that the set does not list, with mean cosine >= {GBA_COS} to the "
          f"arm's listed members: {len(top):,} genes "
          f"({len(members):,} gene-set rows in novel_members.csv, <= {GBA_PER_GENE} most significant sets per gene)"
          + (f"; {int(m_alert.sum()):,} of these genes carry an alert ({ALERT}: in the vector space only through "
             f"drug-doses that carry an alert)" if m_alert.any() else "")
          + f". Top 25 genes{_also_clean(m_alert, 25)}, each with the arm's most significant set that does not list "
          f"it ('sets already listing the gene' = Hallmark / Reactome sets naming it at all; 0 = no pathway "
          f"annotation):", ""]
    if len(members):
        top = top.iloc[capped(np.arange(len(top)), ~m_alert, 25)]
        rows = [[r["symbol"] + (f" {ALERT}" if r.get("alert") else ""), (_clip(r["name"], 45) or "-"),
                 f"{r['module']}{r['arm']}", _clip(r["set_label"], 60),
                 f"{r['n_annotated_in_arm']}/{r['n_arm']}", _f(r["mean_cos"]),
                 f"{_f(r['mean_cos_half1'])} / {_f(r['mean_cos_half2'])}", r["n_reference_sets"]]
                for _, r in top.iterrows()]
        L += [_md_table(["gene", "name", "module arm", "set", "listed members in arm", "mean cos to them",
                         "half1 / half2", "sets already listing the gene"], rows), ""]

    L += ctx.get("line_lines") or []

    syn = cs[cs["source"] == "synthetic"]
    if len(syn):
        L += ["## 9. Synthetic ground truth", "",
              "The synthetic generator's planted gene sets (ground_truth.json 'synthetic gene sets'), with the same "
              "metrics. (On the synthetic data most curated control sets are real gene names that the generator does "
              "not move together, so sections 1-2 there are not a test of the method; this section is.)", "",
              _md_table(SET_HEAD, _set_rows(syn.sort_values("auroc_cos", ascending=False), n_null=n_null)), ""]
        so = op[op["source"] == "synthetic"] if len(op) else op
        if len(so):
            L += [_opp_table(so), ""] + ["- " + _reading(r) for _, r in so.iterrows()] + [""]

    L += ctx.get("direction_lines") or []
    dm = ctx.get("dmso") or {}
    L += ["## Caveats", "",
          "- Correlation is not mechanism: two genes with a high cosine respond alike to these drugs in these "
          "lines; that may be co-regulation, a shared upstream stress, or a shared cell-state change.",
          "- One time point (24 h): early and late responses are not separated; direct and indirect targets look the "
          "same.",
          f"- Cancer cell lines only ({_n_lines(ctx.get('out'), ctx.get('label_info')) or 'all'} lines in this run): "
          "relations driven by mutated pathways or lost checkpoints (e.g. TP53) "
          "may not hold in normal cells, and tissue-specific programmes are under-represented.",
          "- Relations strong in only one of the two random halves of the compounds ('one half' in relations; the "
          "halves are a hash split of compound names) do not have the same sign in both halves and carry no error "
          "estimate; they are never called novel here. The halves share the lines and plates, so the same sign in "
          "both halves guards against single-compound effects, not against everything; 98% of the top-100 partners "
          "pass it.",
          "- Neighbouring genes (same locus, <= 50 kb) and read-through pairs (the 5' gene's transcription running "
          "into the 3' gene) correlate without regulation: they are excluded from 'novel'. Genes expressed in the "
          "same few lines (lineage pairs) and near-identical copies that can share sequencing reads are kept, with "
          "an alert.",
          "- 'Not known' means no shared HGNC gene group, Hallmark / Reactome pathway or STRING link (score >= 400) "
          "in the cached reference files; the literature may still describe the relation.",
          "- Gene-set AUROCs are against random gene pairs of the space; sets of genes that respond rarely in "
          "Tahoe-100M (few genes in the space) are weak tests, whatever their biology.",
          f"- Nothing is left out of a list for a flag: an item with a reason for doubt keeps its ranked place and "
          f"carries {ALERT} with the reason. Genes in the vector space only through drug-doses that "
          f"carry an alert ({int((sp.flagged_only & sp.included).sum()):,} genes; embed/genes.parquet "
          f"evidence_flagged_only) are part of every test. Only the fit of the vector space leaves out the "
          f"technically untrustworthy drug-doses (unreliable plate only, position not correctable, wells disagree; "
          f"embed/info.json lists them)."]
    if dm.get("plates"):
        L.append("- DMSO sign check (tables/info.json dmso_sign_changes: drug_effects rows whose change against the "
                 "typical drug well and against the plate's DMSO wells point opposite ways, by at least 1.2x): "
                 + "; ".join(f"{p} {v.get('sign_changes', 0):,} of {v.get('rows', 0):,} rows"
                             + (f" ({v.get('no_dmso_value'):,} without a DMSO value)" if v.get("no_dmso_value") else "")
                             for p, v in dm["plates"].items()) + ".")
    L.append("")
    L += ["## Files", "",
          "control_sets.csv (every tested set), opposite_pairs.csv, module_enrichment.csv, module_labels.csv, "
          "drug_moa.csv, novel_edges.csv, novel_members.csv, line_controls.csv, metrics.json; README.md documents the "
          "columns.", ""]
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    replace_file(tmp, path)


README = """# validation/ - does the vector space recover known biology, and what in it is new?

Written by `tahoemap validate` (tahoemap/validate.py, version 7). `cos` = signed cosine of two genes' unit vectors
(embed/gene_unit.npy). Every number is over the genes in the vector space (embed/included_cols.npy). Gene cols are the
row order of atlas/effects/genes.csv; symbols can repeat, so join on col. Read report.md first. Nothing is left out of
a list for a flag: an item with a reason for doubt keeps its ranked place and carries ⚠ with the reason in plain words.

report.md sections: 1 known programmes (curated, Hallmark, Reactome sets), 2 opposite programmes, 3 drug check (Tahoe
and ChEMBL classes side by side; annotation agreement), 4 neighbouring wells, 5 modules and labels, 6 novel gene
relations, 7 novel module members, 8 line-selective responses (known positive controls), 9 synthetic ground truth
(synthetic data only), 10 direction; then caveats and files.

Flags are the flags of record of the tables stage (tables.dd_flags_of_record: the atlas flags plus 'like a
neighbouring well' and 'translation inhibitor'); an artifact flag is one of common.ARTIFACT_FLAGS. The
neighbouring-well top-dose tier, 'like a neighbouring well (top dose)', is an alert, not an artifact flag (as the
tables stage and the explorer call it): named in words, without ⚠, and it never changes clean. 'translation
inhibitor' is a caveat: named, never an alert.

## control_sets.csv - one row per tested gene set
| column | meaning |
|---|---|
| `source` | control (tahoemap/data/control_sets.json), hallmark, reactome (reference/gene_sets.parquet, >= 5 genes \
in the space), synthetic (only with truth=) |
| `set`, `label`, `note` | set name, short name, curator's note |
| `n_listed`, `n_found`, `n_in_space` | genes listed by the source, found among Tahoe genes, in the vector space (all \
metrics use these) |
| `mean_cos`, `median_cos`, `frac_pos` | over within-set pairs |
| `auroc_cos`, `auroc_abs` | AUROC of within-set pairs vs 20,000 random pairs of genes in the space, on cos / on \
abs(cos) (P(set pair > random pair), ties 1/2) |
| `p_random_sets_cos`, `p_random_sets_abs` | share of 200 random gene sets of the same size with an AUROC at least as \
high ((1 + count) / 201; control, Hallmark, synthetic only) |
| `mean_cos_half1`, `mean_cos_half2` | mean within-set cos in the spaces fitted on each half of the compounds |
| `top_module`, `top_module_share` | the module (nodal map) holding most of the set's genes, and the share of the \
set's genes in it |
| `top_module_genome_share` | that module's share of all genes in the space (chance level of top_module_share) |
| `top_module_arm_share` | share of the set's genes in that module on its majority arm |
| `best_dd_up`, `best_dd_down` | the 5 drug-doses with the highest / lowest mean pooled z (DD_z) over the set's \
genes, every drug-dose in its ranked place ('drug dose uM (mean z)'). One with an artifact flag (unreliable plate \
only, position not correctable, wells disagree, toxic, like a neighbouring well, ...) reads 'drug dose uM (mean z, ⚠ \
its flags)'; for a cell-cycle shift with the share of the set's mean change the shift would explain ('cell-cycle \
shift, explains ~N% of this change': the tables stage's rule on the members' mean lfc and mean cell-cycle slopes; a \
shift that does not explain the change is named without ⚠). Named without ⚠ too: the top-dose alert 'like a \
neighbouring well (top dose)' (an alert, not an artifact flag), and the caveat of a member of the \
translation-inhibitor class in best_dd_up, '(..., translation inhibitor: rise may be mRNA stabilisation)': blocking \
translation stabilises short-lived mRNAs, so a rise there may not be more transcription. When the 5 strongest \
hold drug-doses with an alert, the 5 strongest without one follow in their ranked place too |
| `best_dd_up_n_alert`, `best_dd_down_n_alert` | how many drug-doses of each list carry an alert |
| `best_dd_up_without_tl` | when a translation inhibitor is among the 5 strongest raisers: the 5 strongest raisers \
that are not (same rule and format); '' otherwise. The report prints it as a second line of the cell: 'without \
translation inhibitors: ...' |

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
| `nodal_centroid_dist`, `signed_centroid_dist` | distance between the two sets' centroids on the nodal map (x, y) / \
signed map (xs, ys), divided by the map's spread sqrt(var x + var y) |
| `nodal_mixing`, `signed_mixing` | how mixed the two sets are on the nodal / signed map: for each gene, the share \
of its nearest map neighbours (among the genes of both sets) that belong to the other set, divided by that share \
under random labels, averaged; 1 = as mixed as chance, 0 = no gene has a neighbour from the other set |
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
| `genes` | every overlapping gene (`overlap` of them), strongest on the module axis first |

## module_labels.csv - one row per module
How a module is labelled (version 7). Candidates: the sets with q < 0.05 and >= 3 shared genes in the module or one of
its arms (module_enrichment.csv). A candidate is strong when q < 0.01, its overlap is at least 5 times the chance
overlap (fold) and at least 3 shared genes remain when each group of near-identical copies counts once (genes that can
share sequencing reads: relations.read_sharing_pairs, Compara paralogues at >= 95% identity, HGNC pseudogenes and
their parents, read-through transcripts and their parts); else it is weak. The set label: when a curated control set
is a candidate and not weak, the control candidates alone compete; then, as before, sets of <= 300 genes in the space
when there is one, the smallest p (4 significant digits), curated source first, the smaller set, the larger overlap.
Rule changed in validate version 7: a curated control set now wins over Hallmark and Reactome when it shares 3 or more
genes and is not weak. Before, the smallest p won whatever the source, which named the metallothionein module (113)
hypoxia.

The label is the first of: (1) a strong set label; (2) the driving drug class: among the module's 10 strongest
drug-doses whose module pooled z (graph/module_pooled_z.npy: + arm mean pooled z minus - arm mean; up = +z, down =
-z) is >= 3, flagged ones included, the class with the most distinct compounds (ties alphabetical), when it has >= 3
compounds, or >= 2 when that is every compound of the class in the screen; 'raised by {classes}', or 'lowered by
{classes}' when only the fall qualifies ({classes} = the class as a plural noun phrase, class_plural: the class's
'plural' in drug_classes.json, e.g. 'glucocorticoid receptor agonists', 'drugs that act on DNA directly'; else the
name's last noun made plural; else "drugs with the mechanism '<name>'"; version 7 wrote the singular label, which read
'lowered by acts on DNA directly'). Two class sources: 'ChEMBL' = the class labels of
tahoemap/data/drug_classes.json the drug belongs to (tahoemap/mechanisms.py: ChEMBL mechanism rules, WHO ATC via
ChEMBL and cited code constants), or for a drug in none of them its ChEMBL mechanism texts ('code constants' when
ChEMBL did not load); 'Tahoe' = Tahoe's moa_fine ('', 'unclear', 'unknown' ignored). ChEMBL's class is used when it
qualifies, else Tahoe's; both are written when both qualify and name different classes; (3) a weak set label
('weak: {short name} ({overlap} of {n_set} genes, q {q})'); (4) a lineage label ('lineage: expressed mainly in {k}
lines (including a of the b {organ} lines)') when the module is lineage-restricted; (5) 'genes: ...' (top genes of
the + arm, then the - arm). Every part keeps its own column.

Alerts (label_alert, '; '-joined, each starting with ⚠; the tags in label_display):
- read-sharing copies: >= 2 of the genes the label names (a set label's first 5 shared genes, else the 3 + and 2 -
  top genes) are in one group of near-identical copies, or >= 20% of the members are in such groups: '⚠ {k} of its
  {n} genes are near-identical copies that can share sequencing reads ({names}): part of their co-movement may be
  read counting, not regulation'; tag '⚠ read-sharing copies'.
- lineage-restricted: the median member is expressed in < 60% of the lines (relations' lineage rule): '⚠
  lineage-restricted: its median gene is expressed in {m} of {L} lines (genes expressed in the same lines often move
  together whatever their regulation); most members are expressed in {k} lines[, including a of the b {organ} lines]';
  tag '⚠ lineage-restricted'.
- Y-chromosome genes: >= 3 members on chrY, or >= 2 that are >= 10% of the members: '⚠ {k} genes on the Y chromosome
  ({names}): they are expressed only in lines from male donors, so the module partly marks line identity'; tag '⚠
  Y-chromosome genes'.

| column | meaning |
|---|---|
| `module`, `n_genes`, `n_plus`, `n_minus` | the module and its arms |
| `label` | the label by the rule above |
| `label_source` | control, hallmark, reactome (a set label, strong or weak: see label_weak), drug class, lineage, \
top genes |
| `label_display` | label + the alert tags ('⚠ read-sharing copies', '⚠ lineage-restricted', '⚠ Y-chromosome \
genes') |
| `label_alert` | every alert of the module in plain words ('; '-joined; each starts with ⚠); '' = none |
| `label_weak`, `label_weak_why` | the module's set label is weak, and why (q, fold, independent shared genes) |
| `set_label` | the module's set label, whether or not it is the label ('weak: ...' when weak; '' = no candidate) |
| `label_set`, `label_arm`, `label_overlap`, `label_independent_overlap`, `label_n_set`, `label_fold`, `label_p`, \
`label_q` | that set's test: the set, the unit (all / + / -), shared genes, shared genes with each group of copies \
counted once, the set's genes in the space, overlap / chance overlap, p, q (they describe the set label even when the \
label is a drug class or a lineage) |
| `plus_label`, `plus_set`, `plus_q`, `minus_label`, `minus_set`, `minus_q` | the set label of each arm alone (same \
rule) |
| `label_drugs` | the driving classes in words: 'raised by {classes} ({drugs}; class from {source}; this class leads \
{k} of {M} modules)' ({classes}: the class as a plural noun phrase), the same with 'lowered by', joined by ' · ' \
('' = none qualifies) |
| `drivers_up_class`, `drivers_up_drugs`, `drivers_up_source` | the class that raises the module, its compounds \
among the 10 strongest drug-doses (strongest first; '⚠' = every counted drug-dose of it carries an artifact flag) \
and \
its source (ChEMBL / Tahoe; 'ChEMBL; Tahoe agrees (...)' when Tahoe's moa_fine names the same class; two entries \
'; '-joined when both sources qualify with different classes) |
| `drivers_down_class`, `drivers_down_drugs`, `drivers_down_source` | the same for the class that lowers it |
| `drivers_class_modules` | how many modules the class the label names leads (in either direction) |
| `lineage_label` | the lineage label ('' = the module is not lineage-restricted) |
| `median_lines_expressing` | the median over the members of the lines expressing them (tables/genes.parquet \
n_lines_expressing) |
| `lines_core` | lines that express at least half of the members (tensor/line_measured.npy, else tables/line_effects \
expressed) |
| `lineage_organs` | organs whose lines are enriched among lines_core (hypergeometric p <= 0.05, best first): 'Bowel 8 \
of 9' = 8 of the 9 Bowel lines |
| `chrY_genes` | members on the Y chromosome (reference/annotations.parquet chrom) |
| `read_sharing_genes`, `read_sharing_n` | the groups of near-identical copies among the members ('A, B, C | D, E'), \
and how many members are in one |
| `covariate_tag` | the graph stage's note when the module's score moves with a technical measure or the cell cycle \
(graph/modules.parquet; a note, not an alert) |
| `top_plus`, `top_minus` | top genes of each arm (graph/modules.parquet; cut at 8 with the cap rule; a gene in the \
vector space only through drug-doses that carry an alert reads 'SYMBOL ⚠') |

## drug_moa.csv - mechanism classes with >= 2 drugs, from two sources
Rows of Tahoe's classes first (class_source 'Tahoe', moa_fine filled), then the mechanism classes ('ChEMBL', or 'code
constants' when ChEMBL did not load; moa_fine ''): the class labels of tahoemap/data/drug_classes.json, or a drug's
ChEMBL mechanism texts when it is in none of them. Two drugs of one molecule (the same ChEMBL id, else the same name
without its salt) are never paired.
| column | meaning |
|---|---|
| `class_source`, `class` | where the class comes from (Tahoe / ChEMBL) and its name |
| `moa_fine` | Tahoe's moa_fine (Tahoe rows; '' for the mechanism-class rows) |
| `n_drugs`, `drugs` | every drug of the class (⚠ = the drug's vector is of a dose with an artifact flag, \
embed/drugs.parquet alert; it is tested like the others) |
| `n_drugs_flagged_dose`, `n_drugs_no_trustworthy_dose` | the class's drugs marked ⚠; those of them with no \
trustworthy dose (every dose flagged unreliable plate only, position not correctable or wells disagree) |
| `n_pairs`, `mean_cos_within` | drug pairs within the class (one molecule never paired), their mean drug-vector cos |
| `mean_cos_to_other_classes` | mean cos of class members to drugs with a class of the same source that is not \
this one |
| `auroc_within_vs_other` | AUROC of within-class pairs vs (member, other drug) pairs |

## novel_edges.csv - candidate new gene-gene relations (relations novel_candidate, one row per pair)
| column | meaning |
|---|---|
| `col_a`, `symbol_a`, `name_a`, `module_a`, `arm_a` | gene a (col_a < col_b), its HGNC name, module and arm |
| `col_b`, `symbol_b`, `name_b`, `module_b`, `arm_b` | gene b |
| `same_module` | both in the same module |
| `cos`, `cos_half1`, `cos_half2`, `evidence`, `fdr` | from relations (full space, the two compound halves, \
sign-concordance FDR) |
| `same_chrom`, `distance_bp` | genomic position (locus and read-through pairs are excluded) |
| `n_lines_a`, `n_lines_b`, `lines_shared`, `lines_jaccard` | lines expressing each gene, both, and the Jaccard of \
the two line sets (relations version 5) |
| `lineage_pair`, `lineage_p` | both genes expressed in few lines (<= 60% of them) and mostly the same ones (Jaccard \
>= 0.5): a lineage pair (⚠); lineage_p = the share of pairs expressed in equally overlapping lines that are at \
least as strongly related (lineage_p >= 0.01: no stronger than 99% of such pairs); NaN unless a lineage pair |
| `read_sharing`, `read_sharing_risk` | the two genes are near-identical copies that can share sequencing reads \
('paralogue', 'pseudogene', 'read-through'; '' = no) (⚠) |
| `alert` | '' or '⚠ ' + the reasons to doubt the pair in plain words (relations' alert: a gene that is in the \
vector \
space only through drug-doses that carry an alert, a lineage pair, near-identical copies); such pairs are listed \
like the others |

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
| `alert` | '' or '⚠ ' + why to doubt the gene's place: it is in the vector space only through drug-doses that carry \
an alert (embed/genes.parquet evidence_flagged_only); such genes are listed like the others |

## line_controls.csv - line-selective responses: known positive controls (report section 8)
Each entry of control_sets.json 'line_controls' picks a group of lines (a recorded driver change, a high baseline of a
gene, named lines, the TP53 status) and drugs (named, a class of drug_classes.json, or a target in Tahoe's or ChEMBL's
annotation), with a cited source; with truth= (synthetic) the planted line-selective answers are added. One row per
drug-dose of a control's drugs (a control with no drug in the screen keeps one row that says so).
| column | meaning |
|---|---|
| `control`, `dd`, `drug`, `dose` | the control and the drug-dose (dd = atlas/effects/drugdose.csv row) |
| `group_lines_measured`, `group_lines` | the group's lines measured at this drug-dose; the group's lines |
| `auroc`, `p` | AUROC of the line selectivity (tables/drug_line_response.parquet sel_z) of the group's measured lines \
vs the other measured lines (1 = every group line above every other; 0.5 = no difference); permutation p (2,000 \
shuffles of the group labels, stable seed) |
| `auroc_response_strength`, `p_response_strength`, `group_lines_with_response_strength` | the same on the lines' \
response strength (drug_line_response response_strength, the atlas's DD_beta; lines of the growth analysis only) |
| `top_lines` | the 5 lines with the highest sel_z ('*' = a line of the group) |
| `selective_lines` | lines with sel_z >= 3 and >= 20 genes beyond the per-line cut ('*' = of the group) |
| `flags` | the drug-dose's flags of record |
| `note` | 'no drug of this control in the screen' for such a control |

## metrics.json
The headline numbers of report.md: control_sets, hallmark, reactome, opposite_pairs, drug_check (all / active =
Tahoe's; tahoe, chembl, chembl_source), module_labels (modules, labelled = set labels, strong_set and its sources,
drug_class, weak_set, lineage, top_genes, with_alert, read_sharing_alert, lineage_alert, chrY_alert,
with_driving_class, class_leads, read_sharing_source, chembl_source), neighbouring_wells (pairs judged, passing,
expected, drug-doses per tier, table rows), line_controls (the rows of line_controls.csv), annotations (status counts,
alerts), novel (edges, edges_lineage, edges_lineage_p_ge_0.01, edges_read_sharing, members), direction (edges, grades,
positive controls with the not-counted p53 targets and why, expected false or non-specific edges per kind, grade-A
false shares, same locus, kinds, planted answers).
"""


# ----------------------------------------------------------------------------- run
def run(out, truth=None, n_random=N_RANDOM, n_null=N_NULL, site_url=None):
    """The validation stage. site_url: the explorer's address the report links to (links.site_url: None = the
    GitHub Pages address of this code's repository; '' / 'none' = no site: links point into the run folder's own
    explorer, explorer/web/index.html)."""
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
    up, down, n_alert, up_no_tl = _best_drugdoses(out, sp.gK, sets)
    cs = pd.DataFrame(recs)
    cs["best_dd_up"], cs["best_dd_down"] = up, down
    cs["best_dd_up_n_alert"] = [a for a, _ in n_alert]
    cs["best_dd_down_n_alert"] = [b for _, b in n_alert]
    cs["best_dd_up_without_tl"] = up_no_tl
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
    write_csv(enr.drop(columns=["_cols", "_n_listed"]), os.path.join(vd, "module_enrichment.csv"))
    labels, label_info = _labels(sp, enr, out)
    write_csv(labels, os.path.join(vd, "module_labels.csv"))
    lc = label_counts(labels)
    log(f"  enrichment: {O.size:,} tests, {int((Q < LABEL_Q).sum()):,} at q < {LABEL_Q}; labels of {len(labels)} "
        f"modules: " + (f"{lc['strong_set']} strong set, {lc['drug_class']} drug class, {lc['weak_set']} weak set, "
                        f"{lc['lineage']} lineage, {lc['top_genes']} top genes; {lc['with_alert']} with an alert"
                        if lc else "none"))

    # ---- drug check
    drug, drug_tab = _drug_check(out)
    write_csv(drug_tab, os.path.join(vd, "drug_moa.csv"))
    if drug:
        log(f"  drug check: AUROC same class, Tahoe {_f(drug['tahoe']['all']['auroc'])} "
            f"({drug['tahoe']['all']['drugs']} drugs), {drug['chembl_source']} {_f(drug['chembl']['all']['auroc'])} "
            f"({drug['chembl']['all']['drugs']} drugs)")

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

    # ---- neighbouring wells, line-selective controls, annotations
    from . import links
    site = links.site_url(site_url)
    nb_lines, nb_met = _neighbour_section(out, site)
    line_lines, line_met = _line_controls(out, truth)
    write_csv(pd.DataFrame(line_met or [], columns=["control", "dd", "drug", "dose", "group_lines_measured",
                                                    "group_lines", "auroc", "p", "auroc_response_strength",
                                                    "p_response_strength", "group_lines_with_response_strength",
                                                    "top_lines", "selective_lines", "flags", "note"]),
              os.path.join(vd, "line_controls.csv"))
    annotation = _annotation_agreement(out)
    rinfo, tinfo = {}, {}
    for d, k in (("relations", "rinfo"), ("tables", "tinfo")):
        try:
            with open(os.path.join(out, d, "info.json"), encoding="utf-8") as fh:
                (rinfo if k == "rinfo" else tinfo).update(json.load(fh))
        except (OSError, ValueError):
            pass

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
               "module_labels": dict({"modules": int(len(labels)),
                                      "labelled": int(labels["label_source"].isin(SET_SOURCES).sum())
                                      if len(labels) else 0,
                                      "enrichment_tests": int(O.size), "tests_q_lt_0.05": int((Q < LABEL_Q).sum()),
                                      "read_sharing_source": label_info.get("read_sharing_source"),
                                      "chembl_source": label_info.get("chembl_source"),
                                      "class_leads": label_info.get("leads")}, **lc),
               "neighbouring_wells": nb_met, "line_controls": line_met,
               "annotations": {"status": annotation[0], "alerts": len(annotation[1])},
               "novel": {"edges": int(len(edges)),
                         "genes_with_novel_edge": int(len(set(edges["col_a"]) | set(edges["col_b"])))
                         if len(edges) else 0,
                         "member_rows": int(len(members)),
                         "member_genes": int(members["col"].nunique()) if len(members) else 0,
                         "edges_with_alert": int((edges["alert"].fillna("") != "").sum()) if len(edges) else 0,
                         "member_genes_with_alert": int(members.loc[members["alert"].fillna("") != "", "col"]
                                                        .nunique()) if len(members) else 0,
                         "edges_lineage": int(edges["lineage_pair"].fillna(False).astype(bool).sum())
                         if len(edges) and "lineage_pair" in edges else 0,
                         "edges_lineage_p_ge_0.01": int((edges["lineage_pair"].fillna(False).astype(bool)
                                                         & (pd.to_numeric(edges["lineage_p"], errors="coerce")
                                                            >= LINEAGE_P_STRONG)).sum())
                         if len(edges) and "lineage_p" in edges else 0,
                         "edges_read_sharing": int((edges["read_sharing"].fillna("").astype(str) != "").sum())
                         if len(edges) and "read_sharing" in edges else 0},
               "genes_in_space_flagged_only": int((sp.flagged_only & sp.included).sum()),
               "reference": bool(n_sets["reference"])}
    if n_sets["synthetic"]:
        metrics["synthetic"] = dict(summ("synthetic"), per_set=per_set("synthetic"), opposite_pairs=opp("synthetic"))
    dir_lines, dir_metrics = _direction_section(out, truth)
    metrics["direction"] = dir_metrics
    write_json(metrics, os.path.join(vd, "metrics.json"))
    _report(os.path.join(vd, "report.md"), {"sp": sp, "cs": cs, "op": op, "labels": labels, "edges": edges,
                                             "members": members, "drug": drug, "drug_tab": drug_tab,
                                             "n_sets": n_sets, "n_null": n_null, "direction_lines": dir_lines,
                                             "nb_lines": nb_lines, "line_lines": line_lines,
                                             "label_info": label_info, "annotation": annotation, "rinfo": rinfo,
                                             "tl_candidates": _tl_candidates(out),
                                             "dmso": tinfo.get("dmso_sign_changes") or {}, "out": out})
    tmp = os.path.join(vd, "README.md.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(README)
    replace_file(tmp, os.path.join(vd, "README.md"))

    info = {"version": VERSION, "genes": int(sp.n), "sets": n_sets, "modules": int(sp.n_modules),
            "modules_labelled": metrics["module_labels"]["labelled"],
            "label_sources": {k: lc.get(k) for k in ("strong_set", "drug_class", "weak_set", "lineage", "top_genes")},
            "modules_with_alert": lc.get("with_alert"),
            "control_median_auroc_cos": metrics["control_sets"]["median_auroc_cos"],
            "drug_moa_auroc": drug.get("all", {}).get("auroc") if drug else None,
            "novel_edges": int(len(edges)), "novel_member_genes": metrics["novel"]["member_genes"],
            "novel_edges_with_alert": metrics["novel"]["edges_with_alert"],
            "novel_member_genes_with_alert": metrics["novel"]["member_genes_with_alert"],
            "genes_in_space_flagged_only": metrics["genes_in_space_flagged_only"],
            "truth": bool(truth), "minutes": round((time.time() - t0) / 60, 2)}
    stamp_stage(out, "validate", VERSION, info)
    log(f"Validate done: report in {os.path.join(vd, 'report.md')} ({info['minutes']} min)")
    return info
