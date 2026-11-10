"""relations - gene x gene: which genes move with each gene, which move opposite, and how sure we are.

For every gene in the vector space (embed stage) the 100 partners with the largest |cosine| are kept, with:

  cos            signed cosine of the two genes' unit vectors = correlation of their denoised response profiles
                 across every (drug-dose, cell line) context. + : they go up and down together; - : opposite.
  z_gene         that cosine as a robust z against all of this gene's partners (a gene with a broad response
                 has many moderate cosines; z says how exceptional this partner is for this gene)
  cos_half1/2    the same cosine in the two spaces fitted on two disjoint halves of the compounds
  fdr            sign-concordance false discovery rate. Pairs are selected in one half's space and their sign is
                 checked in the other half, whose noise is independent: under no relation the sign agrees half the
                 time, so FDR(t) = (#disagreeing + 1) / #agreeing pairs with |other-half cos| >= t (both directions
                 pooled, made monotone). A pair's fdr is read at t = min(|cos_half1|, |cos_half2|) (conservative).
  evidence       "both halves"     the same sign in both halves of the compounds: the same sign in the full space and
                                   in both halves, min |half cos| >= 0.2, AND fdr <= 0.10. The halves share the lines
                                   and plates, so this guards against single-compound effects, not against everything;
                                   98% of the top-100 partners pass it on the real data.
                 "one half"        strong (|cos| >= 0.5) in one of the two random halves only (the halves are a
                                   hash split of compound names): the other half does not show it, no error estimate.
                                   Often a response driven by a single compound.
                 "not reproduced"  otherwise
  genomic flags  same chromosome, gap in bp, same strand, locus (<= 50 kb apart), readthrough_risk (same strand,
                 <= 20 kb, the 5' gene >= 8x more expressed: transcription running past the 5' gene is counted as
                 the 3' gene's mRNA, so the pair correlates without any regulation)
  known flags    shared HGNC gene group, shared pathway (Hallmark, or a Reactome pathway of <= 300 genes),
                 STRING combined score (>= 400 kept)
  rank_ba, z_ba  the same pair seen from the partner's side (NaN when a is not among b's 100 strongest partners)
  mutual_rank    max(rank, rank_ba);  specificity = min(|z_gene|, |z_ba|): how exceptional the pair is for both genes.
                 At full scale broad programmes give most strong pairs the same sign in both halves; specificity
                 separates a particular relation from membership of the same large programme (mutually-top pairs are
                 also ~3x more often already known, so specificity tracks real relations).
  novel_candidate  mutual_rank <= 10, specificity >= 4, evidence "both halves", fdr <= 0.05, |cos| >= 0.5, not known,
                 not the same locus, both genes
                 have a registry (HGNC) record and coordinates (for an undescribed or unplaced gene "not known" and
                 "not the same locus" mean nothing), and only when the sources that define "known" loaded (HGNC,
                 Ensembl, STRING, and Hallmark or Reactome); otherwise info.json says which were missing. The lineage
                 and read-sharing alerts below do not change it: they are alerts, shown with the pair.

  Lineage pairs (relations version 5). Genes that only some cell lines express often move together whatever their
  regulation, because their contexts are the responses of the same few lines. On the real data, among genes expressed
  in <= 30 of 50 lines, the share of pairs with |cos| >= 0.5 rises with the overlap of their expressing lines (Jaccard
  J): J < 0.3 0.43%, 0.3-0.5 2.2%, 0.5-0.6 5.8%, 0.6-0.7 10.6%, 0.7-0.8 17.1%, 0.8-0.9 27.1%, >= 0.9 38.3% (random
  pairs of genes expressed in >= 48 lines: 1.6%). The zeros of the lines that do not express a gene do not make the
  cosine (their offset is < 0.001); the shared lines' responses do.
  n_lines_a/b    lines that truly express each gene (tensor/line_measured.npy, the mask behind tables
                 n_lines_expressing; else tables/line_effects.parquet 'expressed')
  lines_shared   lines expressing both;  lines_jaccard  = shared / lines expressing either
  lineage_pair   both genes restricted (expressed in <= LINEAGE_MAX_SHARE x the lines: 30 of 50) and J >= 0.5
  lineage_p      NaN unless lineage_pair: (1 + pairs of restricted genes in the same J bin with |cos| >= this pair's
                 |cos|) / (1 + pairs in the bin), from the exact |cos| and J of every pair of restricted genes in the
                 space (a seeded sample of LINEAGE_NULL_MAX genes when there are more); bins LINEAGE_BINS. A small
                 lineage_p: the pair is stronger than almost all pairs that share their lines as much.
  Every lineage pair carries the alert 'lineage: both genes are expressed in few lines, mostly the same (...)'.

  Read-sharing copies (relations version 5). Reads of near-identical sequences can be counted for either gene, so
  such genes correlate without any regulation. read_sharing_pairs() finds them: (a) Ensembl Compara paralogues
  (reference/paralogues.parquet) with >= READSHARE_PID % protein identity (the larger of the two directions);
  (b) an HGNC pseudogene and its parent: symbol = parent + 'P' + digits (HERC2P2 -> HERC2), or a sibling that differs
  in a last single digit, with a base of >= 5 characters that does not end in a digit (PDXDC2P -> PDXDC1, HSP90AB3P ->
  HSP90AB1), or the HGNC name 'X pseudogene N'; plus two pseudogenes of one parent (HERC2P2 - HERC2P3); (c) an HGNC
  read-through transcript and its parts (KLRC4-KLRK1 contains KLRK1). Columns read_sharing ('' / 'paralogue' /
  'pseudogene' / 'read-through') and read_sharing_risk; each such pair carries an alert that says why.

  alert          '' or '⚠ ' + every reason to doubt the pair, in plain words: not reproduced in both random halves
                 (or strong in one half only), the same locus or a read-through risk, a lineage pair, a read-sharing
                 copy, a gene that is in the vector space only through drug-doses that carry an alert (embed
                 genes.parquet evidence_flagged_only). Every pair stays in the table in its ranked place; the alert only
                 says why to doubt it.

  Counting units (info.json 'units'). rows = (gene, partner) rows: each gene's top 100 partners, so a pair can appear
  twice (once from each side); pairs = distinct unordered gene pairs. Every count is given in both units.

Without the reference stage the genomic and known flags are empty, nothing is called novel and the read-sharing
copies are not assessed.
"""

import os
import time
import warnings

import numpy as np
import pandas as pd

import json
import re

from .common import folder, log, stable_seed, stamp_stage, write_csv, write_json, write_parquet

ALERT = "⚠"

VERSION = 5                 # 4: an alert column (every reason to doubt a pair, in plain words)
#                             5: lineage pairs (n_lines_a/b, lines_shared, lines_jaccard, lineage_pair, lineage_p),
#                                read-sharing copies (read_sharing, read_sharing_risk), their alerts, and info.json
#                                counts in two units (rows and pairs)
TOP = 100
REPRO_MIN = 0.2
REPRO_FDR = 0.10
ONE_HALF = 0.5
NOVEL_COS = 0.5
NOVEL_FDR = 0.05
NOVEL_MUTUAL_RANK = 10      # each gene among the other's 10 strongest partners ...
NOVEL_SPECIFICITY = 4.0     # ... and exceptional for both (|z_gene| >= 4 both ways)
LOCUS_BP = 50_000
READTHROUGH_BP = 20_000
READTHROUGH_RATIO = 8.0
PATHWAY_MAX = 300
# lineage pairs (module docstring)
LINEAGE_MAX_SHARE = 0.6     # a gene is restricted when expressed in <= this x the lines (30 of 50)
LINEAGE_MIN_J = 0.5         # ... and a pair of restricted genes is a lineage pair from this Jaccard of their lines
LINEAGE_BINS = (0.5, 0.6, 0.7, 0.8, 0.9, 1.0001)    # Jaccard bins of the lineage null
LINEAGE_NULL_MAX = 8000     # more restricted genes than this: the null uses a seeded sample of this many
LINEAGE_COS = 0.5           # the share of null pairs reported per bin: |cos| >= this
LINEAGE_TIE = 1e-6          # |cos| values this close count as equal (rounding differs between matrix products)
# read-sharing copies (module docstring)
READSHARE_PID = 95.0        # Compara paralogues with >= this % protein identity (the larger direction)
READSHARE_KINDS = ("paralogue", "pseudogene", "read-through")
READSHARE_TEXT = {
    "paralogue": "near-identical paralogues ({pid:.0f}% protein identity): reads can be counted for either gene",
    "pseudogene": "a pseudogene and its parent gene (or two copies of one parent): reads can be counted for either "
                  "gene",
    "read-through": "{rt} is a read-through transcript that contains {part}: reads can be counted for either gene"}
LINEAGE_TEXT = ("lineage: both genes are expressed in few lines, mostly the same ({na} and {nb} of {L}, {s} shared): "
                "such genes often move together whatever their regulation ({pct}% of such pairs reach |cos| >= "
                "{cos:g} here, and this pair is stronger than {beat}% of them)")
UNITS = ("rows = (gene, partner) rows, each gene's top 100 partners, so a pair can appear twice; pairs = distinct "
         "unordered gene pairs")
SAME_SIGN = "same sign in both halves of the compounds"
SAME_SIGN_NOTE = ("the halves share the lines and plates, so this guards against single-compound effects, not against "
                  "everything; 98% of the top-100 partners pass it")

# the words of the columns this stage adds or rewords (relations version 5); the explorer and the docs show them
COLUMN_DOCS = {"relations/gene_relations.parquet": {
    "evidence": f"'both halves': the {SAME_SIGN} (the same sign in the full space and in both halves, min |half cos| "
                f">= 0.2 and fdr <= 0.10; {SAME_SIGN_NOTE}); 'one half': |cos| >= 0.5 in one half only; otherwise "
                "'not reproduced'",
    "reproducible": "evidence is 'both halves' (the same sign in both halves of the compounds)",
    "n_lines_a": "lines that truly express this gene (tensor/line_measured.npy, as tables n_lines_expressing)",
    "n_lines_b": "lines that truly express the partner",
    "lines_shared": "lines that express both genes",
    "lines_jaccard": "lines_shared / lines that express either gene",
    "lineage_pair": f"both genes are expressed in <= {LINEAGE_MAX_SHARE:g} x the lines (30 of 50) and lines_jaccard "
                    f">= {LINEAGE_MIN_J:g}: such genes often move together whatever their regulation (an alert)",
    "lineage_p": "only for a lineage pair: (1 + pairs of such restricted genes in the same Jaccard bin with |cos| at "
                 "least this pair's) / (1 + pairs in the bin); small = stronger than almost all pairs that share "
                 "their lines as much",
    "read_sharing": "'paralogue' (Compara, >= 95% protein identity), 'pseudogene' (a pseudogene and its parent, or two "
                    "copies of one parent) or 'read-through' (a read-through transcript and a gene it contains): "
                    "reads can be counted for either gene; '' none",
    "read_sharing_risk": "read_sharing is not empty (an alert)"}}



def _top_partners(U, top, block=2048):
    """Top partners by |cos| for every row of U (unit rows), plus each row's robust centre / scale of cos."""
    n = U.shape[0]
    top = min(top, n - 1)
    idx = np.zeros((n, top), dtype=np.int64)
    val = np.zeros((n, top), dtype=np.float32)
    med = np.zeros(n, dtype=np.float32)
    mad = np.zeros(n, dtype=np.float32)
    for r0 in range(0, n, block):
        r1 = min(n, r0 + block)
        C = U[r0:r1] @ U.T
        C[np.arange(r1 - r0), np.arange(r0, r1)] = 0.0
        a = np.abs(C)
        part = np.argpartition(-a, top - 1, axis=1)[:, :top]
        pv = np.take_along_axis(a, part, axis=1)
        order = np.argsort(-pv, axis=1)
        part = np.take_along_axis(part, order, axis=1)
        idx[r0:r1] = part
        val[r0:r1] = np.take_along_axis(C, part, axis=1)
        m = np.median(C, axis=1)
        med[r0:r1] = m
        mad[r0:r1] = 1.4826 * np.median(np.abs(C - m[:, None]), axis=1)
    return idx, val, med, mad


def _pair_cos(Ua, Ub):
    return np.einsum("ij,ij->i", Ua, Ub)


def _fdr_curve(U1, U2, top):
    """Select pairs in one half, score them in the other (independent noise); both directions pooled."""
    s_all, agree_all = [], []
    for A_, B_ in ((U1, U2), (U2, U1)):
        idx, val, _, _ = _top_partners(A_, top)
        a = np.repeat(np.arange(A_.shape[0]), idx.shape[1])
        b = idx.ravel()
        hb = _pair_cos(B_[a], B_[b])
        s_all.append(np.abs(hb))
        agree_all.append(np.sign(hb) == np.sign(val.ravel()))
    s = np.concatenate(s_all)
    agree = np.concatenate(agree_all)
    grid = np.round(np.arange(0.0, 1.0001, 0.01), 2)
    n_ag = np.array([(agree & (s >= t)).sum() for t in grid], dtype=float)
    n_dis = np.array([(~agree & (s >= t)).sum() for t in grid], dtype=float)
    raw = np.minimum(1.0, np.where(n_ag > 0, (n_dis + 1) / np.maximum(n_ag, 1), 1.0))   # +1: target-decoy
    # a pair passing threshold t is also called at every lower threshold: its q is the smallest FDR over t' <= t
    fdr = np.minimum.accumulate(raw)
    return pd.DataFrame({"t": grid, "pairs_agree": n_ag.astype(int), "pairs_disagree": n_dis.astype(int),
                         "fdr": fdr})


def _load_reference(out, gK):
    rd = os.path.join(out, "reference")
    ann = sets = string = None
    p = os.path.join(rd, "annotations.parquet")
    if os.path.exists(p):
        ann = pd.read_parquet(p).set_index("col").reindex(np.arange(gK))
    p = os.path.join(rd, "gene_sets.parquet")
    if os.path.exists(p):
        sets = pd.read_parquet(p)
    p = os.path.join(rd, "string_pairs.parquet")
    if os.path.exists(p):
        string = pd.read_parquet(p)
    return ann, sets, string


def _set_index(sets, gK):
    """Per gene: frozenset of HGNC groups, and of pathways (Hallmark, Reactome <= PATHWAY_MAX genes)."""
    groups = [frozenset()] * gK
    paths = [frozenset()] * gK
    names = {}
    if sets is None or not len(sets):
        return groups, paths, names
    s = sets.dropna(subset=["col"]).copy()
    s["col"] = s["col"].astype(int)
    size = s.groupby(["source", "set"])["col"].transform("size")
    s["key"] = s["source"].astype(str) + ":" + s["set"].astype(str)
    names = dict(zip(s["key"], s["set"].astype(str)))
    g = s[s["source"] == "hgnc_group"].groupby("col")["key"].apply(frozenset)
    pth = s[(s["source"] == "hallmark") | ((s["source"] == "reactome") & (size <= PATHWAY_MAX))] \
        .groupby("col")["key"].apply(frozenset)
    groups = [g.get(c, frozenset()) for c in range(gK)]
    paths = [pth.get(c, frozenset()) for c in range(gK)]
    return groups, paths, names


NOVEL_SOURCES = (("hgnc",), ("ensembl",), ("string_links",), ("string_info",), ("hallmark", "reactome"))


def _source_status(out):
    """{source key: status} of reference/sources.json ({} when it cannot be read)."""
    try:
        with open(os.path.join(out, "reference", "sources.json"), encoding="utf-8") as fh:
            return {k: (v or {}).get("status", "") for k, v in json.load(fh).get("sources", {}).items()}
    except (OSError, ValueError):
        return {}


def _missing_sources(out):
    """The sources that define 'known' and 'same locus' and did not load (empty list: novelty can be assessed)."""
    if not os.path.exists(os.path.join(out, "reference", "sources.json")):
        return ["reference/sources.json"]
    st = _source_status(out)
    ok = {k for k, v in st.items() if v in ("cached", "downloaded")}
    return [" or ".join(alts) for alts in NOVEL_SOURCES if not any(a in ok for a in alts)]


# ----------------------------------------------------------------------------- lineage pairs
def expressed_mask(out, gK):
    """(genes x lines bool, source text): the lines that truly express each gene - tensor/line_measured.npy (lines x
    genes, the mask behind tables n_lines_expressing), else tables/line_effects.parquet 'expressed'; (None, reason)
    when neither exists."""
    p = os.path.join(out, "tensor", "line_measured.npy")
    if os.path.exists(p):
        m = np.load(p, mmap_mode="r")
        if m.ndim == 2 and m.shape[1] >= gK:
            return np.ascontiguousarray(np.asarray(m[:, :gK], dtype=bool).T), "tensor/line_measured.npy"
    p = os.path.join(out, "tables", "line_effects.parquet")
    if os.path.exists(p):
        import pyarrow.parquet as pq
        if {"col", "line", "expressed"} <= set(pq.ParquetFile(p).schema_arrow.names):
            le = pd.read_parquet(p, columns=["col", "line", "expressed"])
            c = pd.to_numeric(le["col"], errors="coerce").fillna(-1).to_numpy(np.int64)
            ln = pd.to_numeric(le["line"], errors="coerce").fillna(-1).to_numpy(np.int64)
            L = int(ln.max()) + 1 if len(ln) else 0
            E = np.zeros((gK, max(L, 0)), dtype=bool)
            ok = (c >= 0) & (c < gK) & (ln >= 0)
            E[c[ok], ln[ok]] = le["expressed"].fillna(False).astype(bool).to_numpy()[ok]
            return E, "tables/line_effects.parquet expressed"
    return None, "not assessed (no tensor/line_measured.npy and no tables/line_effects.parquet)"


def lineage_columns(ca, cb, E, block=200_000):
    """Per row (gene cols ca, cb; E genes x lines bool): n_lines_a, n_lines_b, lines_shared (int16) and lines_jaccard
    (float64: shared / lines expressing either; 0 when neither expresses any line)."""
    n = E.sum(axis=1).astype(np.int64)
    sh = np.zeros(len(ca), dtype=np.int64)
    for r0 in range(0, len(ca), block):
        sh[r0:r0 + block] = (E[ca[r0:r0 + block]] & E[cb[r0:r0 + block]]).sum(axis=1)
    un = n[ca] + n[cb] - sh
    J = np.where(un > 0, sh / np.maximum(un, 1), 0.0)
    return n[ca].astype(np.int16), n[cb].astype(np.int16), sh.astype(np.int16), J.astype(np.float64)


def lineage_null(U, cols, E, max_share=LINEAGE_MAX_SHARE, bins=LINEAGE_BINS, null_max=LINEAGE_NULL_MAX,
                 cos=LINEAGE_COS, block=1024):
    """The lineage null: every pair of restricted genes (cols: the genes of U's rows; restricted = expressed in <=
    max_share x the lines) with its exact |cos| (U rows, unit vectors) and Jaccard of expressing lines. More than
    null_max restricted genes: a seeded sample of null_max of them. Returns a dict: restricted (bool per row of U),
    L, max_lines, genes (restricted genes), null_genes, sampled, pairs, sorted (one sorted |cos| array per bin),
    share (per bin: share of its pairs with |cos| >= cos), below (pairs with J below bins[0] and their share)."""
    L = E.shape[1]
    nl = E[cols].sum(axis=1)
    max_lines = int(np.floor(max_share * L + 1e-9))
    restricted = nl <= max_lines
    ri = np.flatnonzero(restricted)
    sampled = ri.size > null_max
    if sampled:
        rng = np.random.default_rng(stable_seed("lineage null", int(ri.size), int(null_max)))
        ri = np.sort(rng.choice(ri, size=null_max, replace=False))
    R = np.asarray(U[ri], dtype=np.float32)
    Er = E[cols[ri]].astype(np.float32)
    nr = Er.sum(axis=1).astype(np.int64)
    edges = np.asarray(bins, dtype=np.float64)
    nb = len(edges) - 1
    parts = [[] for _ in range(nb)]
    below_n = below_hit = 0
    for r0 in range(0, ri.size, block):
        r1 = min(ri.size, r0 + block)
        C = np.abs(R[r0:r1] @ R.T)
        I_ = np.rint(Er[r0:r1] @ Er.T).astype(np.int64)
        Un = nr[r0:r1, None] + nr[None, :] - I_
        Jm = np.where(Un > 0, I_ / np.maximum(Un, 1), 0.0)
        upper = np.arange(ri.size)[None, :] > np.arange(r0, r1)[:, None]     # each pair once (i < j)
        jj, cc = Jm[upper], C[upper]
        k = np.digitize(jj, edges) - 1
        lo = k < 0
        below_n += int(lo.sum())
        below_hit += int((cc[lo] >= cos).sum())
        for t in range(nb):
            sel = k == t
            if sel.any():
                parts[t].append(cc[sel])
    srt = [np.sort(np.concatenate(p_)) if p_ else np.zeros(0, dtype=np.float32) for p_ in parts]
    share = [float((x >= cos).mean()) if x.size else float("nan") for x in srt]
    return {"restricted": restricted, "L": int(L), "max_lines": max_lines, "genes": int(restricted.sum()),
            "null_genes": int(ri.size), "sampled": bool(sampled), "pairs": int(sum(x.size for x in srt) + below_n),
            "bins": [float(x) for x in edges], "sorted": srt, "share": share, "below": (below_n, below_hit)}


def lineage_p_values(abs_cos, J, null, tie=LINEAGE_TIE):
    """(lineage_p, share of the pair's bin) per pair: (1 + null pairs in the same J bin with |cos| >= this |cos|) /
    (1 + pairs in the bin); NaN for a J outside the bins. Values within `tie` of each other count as equal."""
    abs_cos = np.asarray(abs_cos, dtype=np.float64)
    k = np.digitize(np.asarray(J, dtype=np.float64), np.asarray(null["bins"])) - 1
    p = np.full(abs_cos.size, np.nan)
    sh = np.full(abs_cos.size, np.nan)
    for t, arr in enumerate(null["sorted"]):
        sel = np.flatnonzero(k == t)
        if not sel.size:
            continue
        ge = arr.size - np.searchsorted(arr, abs_cos[sel] - tie, side="left")
        p[sel] = (1.0 + ge) / (1.0 + arr.size)
        sh[sel] = null["share"][t]
    return p, sh


def _floor(x, nd):
    f = 10.0 ** nd
    return np.floor(x * f + 1e-9) / f


def lineage_reason(na, nb, L, shared, share, p, cos=LINEAGE_COS):
    """The alert reason of one lineage pair (one clause; module docstring)."""
    beat = 100.0 * (1.0 - p)
    beat_t = f"{_floor(beat, 2):.2f}" if beat > 99 else f"{_floor(beat, 0):.0f}"
    return LINEAGE_TEXT.format(na=int(na), nb=int(nb), L=int(L), s=int(shared), pct=f"{100.0 * share:.1f}",
                               cos=cos, beat=beat_t)


# ----------------------------------------------------------------------------- read-sharing copies
_PSEUDO_STEM = re.compile(r"^(.+?)P[0-9]*$")
_ONE_DIGIT = re.compile(r"^(.{5,}?)([0-9])$")
_PSEUDO_NAME = re.compile(r"^(\S+) pseudogene\b", re.I)


def _read_ann(out, ann):
    if ann is None:
        p = os.path.join(out, "reference", "annotations.parquet")
        if not os.path.exists(p):
            return None
        ann = pd.read_parquet(p)
    ann = ann.copy()
    if "col" not in ann:
        ann["col"] = np.arange(len(ann))
    return ann


def read_sharing_pairs(out, ann=None):
    """{(lo, hi): (kind, text)} for every pair of Tahoe genes (gene cols, lo < hi) whose reads can be counted for
    either gene (module docstring, 'Read-sharing copies'): kind 'paralogue' (reference/paralogues.parquet,
    max(identity, homology_identity) >= READSHARE_PID), 'pseudogene' (reference/annotations.parquet locus_type
    'pseudogene' and its parent, or two pseudogenes of one parent) or 'read-through' (locus_type 'readthrough' and
    its '-' parts); text = the alert reason. A pair matched by more than one rule keeps the first, in that order. ann:
    the annotations table (default: read from out); missing files or columns: those rules find nothing."""
    res = {}
    ann = _read_ann(out, ann)
    p = os.path.join(out, "reference", "paralogues.parquet")
    if os.path.exists(p):
        par = pd.read_parquet(p)
        if {"col_a", "col_b", "identity", "homology_identity"} <= set(par.columns):
            pid = np.fmax(pd.to_numeric(par["identity"], errors="coerce").to_numpy(np.float64),
                          pd.to_numeric(par["homology_identity"], errors="coerce").to_numpy(np.float64))
            ok = np.flatnonzero(pid >= READSHARE_PID)
            ca = par["col_a"].to_numpy(np.int64)[ok]
            cb = par["col_b"].to_numpy(np.int64)[ok]
            for x, y, v in sorted(zip(ca, cb, pid[ok]), key=lambda t: (min(t[0], t[1]), max(t[0], t[1]), -t[2])):
                if x != y:
                    k = (int(min(x, y)), int(max(x, y)))
                    if k not in res:
                        res[k] = ("paralogue", READSHARE_TEXT["paralogue"].format(pid=float(v)))
    if ann is None:
        return res
    col = pd.to_numeric(ann["col"], errors="coerce").fillna(-1).to_numpy(np.int64)

    def txt(c):
        return ann[c].fillna("").astype(str).to_numpy() if c in ann else np.array([""] * len(ann), dtype=object)
    sym, hs, lt, name = txt("symbol"), txt("hgnc_symbol"), txt("locus_type"), txt("name")
    c2s = {int(c): s_ for c, s_ in zip(col, sym)}
    s2c = {}
    for arr in (sym, hs):                                 # Tahoe's symbol first, then HGNC's
        for c, s_ in zip(col, arr):
            if s_ and c >= 0:
                s2c.setdefault(s_.upper(), int(c))
    parents = {}
    for i in np.flatnonzero(lt == "pseudogene"):
        c, P = int(col[i]), set()
        if c < 0:
            continue
        for s_ in dict.fromkeys(x.upper() for x in (sym[i], hs[i]) if x):
            m = _PSEUDO_STEM.match(s_)
            if not m:
                continue
            stem = m.group(1)
            if s2c.get(stem, c) != c:                     # symbol = parent + 'P' + digits
                P.add(s2c[stem])
                continue
            m2 = _ONE_DIGIT.match(stem)                   # a sibling differing in a last single digit
            if m2 and not m2.group(1)[-1].isdigit():
                for d in "0123456789":
                    sib = m2.group(1) + d
                    if d != m2.group(2) and s2c.get(sib, c) != c:
                        P.add(s2c[sib])
        m3 = _PSEUDO_NAME.match(name[i])                  # HGNC name 'X pseudogene N'
        if m3 and s2c.get(m3.group(1).upper(), c) != c:
            P.add(s2c[m3.group(1).upper()])
        if P:
            parents[c] = P
    pseudo = set()
    bypar = {}
    for c, P in parents.items():
        for q in P:
            pseudo.add((min(c, q), max(c, q)))
            bypar.setdefault(q, []).append(c)
    for q, cs in bypar.items():                           # two pseudogenes of one parent
        cs = sorted(set(cs))
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                pseudo.add((cs[i], cs[j]))
    for k in sorted(pseudo):
        res.setdefault(k, ("pseudogene", READSHARE_TEXT["pseudogene"]))
    for i in np.flatnonzero(lt == "readthrough"):
        c = int(col[i])
        if c < 0 or "-" not in sym[i]:
            continue
        for part in sym[i].split("-"):
            q = s2c.get(part.upper())
            if q is not None and q != c:
                k = (min(c, q), max(c, q))
                res.setdefault(k, ("read-through", READSHARE_TEXT["read-through"].format(rt=sym[i],
                                                                                      part=c2s.get(q) or part)))
    return res


def read_sharing_source(out):
    """What read_sharing_pairs could use: 'Compara 112 + HGNC', 'HGNC only (paralogues not loaded)', 'Compara 112
    only (HGNC not loaded)', 'not assessed (HGNC and the Compara paralogues not loaded)' or 'not assessed (reference
    stage not run)'."""
    if not os.path.exists(os.path.join(out, "reference", "annotations.parquet")):
        return "not assessed (reference stage not run)"
    st = _source_status(out)
    hgnc = st.get("hgnc", "") in ("cached", "downloaded")
    par = os.path.exists(os.path.join(out, "reference", "paralogues.parquet"))
    rel_ = "112"
    try:
        from .reference import COMPARA
        m = re.search(r"release-(\d+)", COMPARA["url"])
        rel_ = m.group(1) if m else rel_
    except Exception:  # noqa: BLE001
        pass
    if par and hgnc:
        return f"Compara {rel_} + HGNC"
    if hgnc:
        return "HGNC only (paralogues not loaded)"
    if par:
        return f"Compara {rel_} only (HGNC not loaded)"
    return "not assessed (HGNC and the Compara paralogues not loaded)"


def read_sharing_columns(ca, cb, pairs):
    """Per row: read_sharing kind ('' when none) and the alert reason text ('' when none)."""
    kind = np.full(len(ca), "", dtype=object)
    text = np.full(len(ca), "", dtype=object)
    if not pairs:
        return kind, text
    keys = pd.DataFrame([(a, b, k_, t) for (a, b), (k_, t) in pairs.items()], columns=["lo", "hi", "kind", "text"])
    m = pd.DataFrame({"lo": np.minimum(ca, cb), "hi": np.maximum(ca, cb)}).merge(keys, on=["lo", "hi"], how="left")
    kind = m["kind"].fillna("").to_numpy(dtype=object)
    text = m["text"].fillna("").to_numpy(dtype=object)
    return kind, text


# ----------------------------------------------------------------------------- alerts and counts
def pair_alerts(rel, flagged_only, sym, have_halves=True, extra=None):
    """The alert of every pair (module docstring, 'alert'): '' or '⚠ ' + its reasons, '; '-joined. flagged_only:
    bool per gene col (embed evidence_flagged_only); sym: symbol per gene col; extra: per row, '' or further reasons
    ('; '-joined: the lineage and read-sharing reasons), placed before the flagged-only reasons."""
    n = len(rel)
    ev = rel["evidence"].astype(str).to_numpy() if "evidence" in rel else np.full(n, "")
    ca, cb = rel["col_a"].to_numpy(np.int64), rel["col_b"].to_numpy(np.int64)

    def col(c):
        return rel[c].fillna(False).astype(bool).to_numpy() if c in rel else np.zeros(n, dtype=bool)
    rt, lc = col("readthrough_risk"), col("locus")
    reasons = [(ev == "one half", "strong in one random half of the compounds only (not replicated)"),
               (ev == "not reproduced", "not reproduced in both random halves of the compounds" if have_halves else
                "reproducibility not tested (no half spaces)"),
               (rt, "read-through risk (neighbours on one strand, the 5' gene far more expressed)"),
               (lc & ~rt, f"same locus (<= {LOCUS_BP // 1000} kb apart: neighbours can correlate without regulation)")]
    code = np.zeros(n, dtype=np.int64)                     # one bit per reason: few distinct texts to build
    for b, (mask, _) in enumerate(reasons):
        code |= mask.astype(np.int64) << b
    text = {c: "; ".join(t for b, (_, t) in enumerate(reasons) if c >> b & 1) for c in np.unique(code)}
    out = pd.Series(code).map(text).to_numpy(dtype=object)
    if extra is not None:
        for i in np.flatnonzero(np.asarray([bool(x) for x in extra])):
            out[i] = f"{out[i]}; {extra[i]}" if out[i] else extra[i]
    for c in (ca, cb):                                     # a gene in the space only through flagged drug-doses
        for i in np.flatnonzero(flagged_only[c]):
            t = f"{sym[c[i]]} is in the vector space only through drug-doses that carry an alert"
            out[i] = f"{out[i]}; {t}" if out[i] else t
    return np.array([f"{ALERT} {t}" if t else "" for t in out], dtype=object)


COUNTS = (("both_halves", lambda r: r["evidence"].astype(str) == "both halves"),
          ("one_half", lambda r: r["evidence"].astype(str) == "one half"),
          ("not_reproduced", lambda r: r["evidence"].astype(str) == "not reproduced"),
          ("fdr_le_0.05", lambda r: pd.to_numeric(r["fdr"], errors="coerce") <= 0.05),
          ("known", lambda r: r["known"].fillna(False).astype(bool)),
          ("locus", lambda r: r["locus"].fillna(False).astype(bool)),
          ("readthrough_risk", lambda r: r["readthrough_risk"].fillna(False).astype(bool)),
          ("with_alert", lambda r: r["alert"].fillna("").astype(str) != ""),
          ("novel_candidate", lambda r: r["novel_candidate"].fillna(False).astype(bool)),
          ("lineage", lambda r: r["lineage_pair"].fillna(False).astype(bool)),
          ("read_sharing", lambda r: r["read_sharing_risk"].fillna(False).astype(bool)))
COUNT_COLUMNS = {"both_halves": "evidence", "one_half": "evidence", "not_reproduced": "evidence", "fdr_le_0.05": "fdr",
                 "known": "known", "locus": "locus", "readthrough_risk": "readthrough_risk", "with_alert": "alert",
                 "novel_candidate": "novel_candidate", "lineage": "lineage_pair", "read_sharing": "read_sharing_risk"}


def count_info(rel):
    """info.json's counts in both units (module docstring, 'Counting units'): units, rows_total, pairs_total, and
    rows_<k> / pairs_<k> for every k of COUNTS (None when the table lacks the column), share_rows_both_halves."""
    ca = rel["col_a"].to_numpy(np.int64)
    cb = rel["col_b"].to_numpy(np.int64)
    key = np.minimum(ca, cb) * (int(max(ca.max(initial=0), cb.max(initial=0))) + 1) + np.maximum(ca, cb)
    res = {"units": UNITS, "rows_total": int(len(rel)), "pairs_total": int(np.unique(key).size)}
    for k, fn in COUNTS:
        if COUNT_COLUMNS[k] not in rel:
            res[f"rows_{k}"] = res[f"pairs_{k}"] = None
            continue
        m = np.asarray(fn(rel), dtype=bool)
        res[f"rows_{k}"] = int(m.sum())
        res[f"pairs_{k}"] = int(np.unique(key[m]).size)
    rb = res.get("rows_both_halves")
    res["share_rows_both_halves"] = round(rb / max(len(rel), 1), 4) if rb is not None else None
    return res


def run(out, top=TOP):
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    rd = folder(out, "relations")
    ed = os.path.join(out, "embed")
    U_all = np.load(os.path.join(ed, "gene_unit.npy"))
    inc = np.load(os.path.join(ed, "included_cols.npy"))
    eg = pd.read_parquet(os.path.join(ed, "genes.parquet"))
    gK = len(eg)
    sym = eg["symbol"].astype(str).to_numpy()
    U = U_all[inc].astype(np.float32)
    have_halves = os.path.exists(os.path.join(ed, "gene_unit_half1.npy"))
    if have_halves:
        U1 = np.load(os.path.join(ed, "gene_unit_half1.npy"))[inc].astype(np.float32)
        U2 = np.load(os.path.join(ed, "gene_unit_half2.npy"))[inc].astype(np.float32)
    log(f"Relations: {len(inc):,} genes, top {top} partners each")
    idx, val, med, mad = _top_partners(U, top)
    n, kk = idx.shape
    a = np.repeat(np.arange(n), kk)
    b = idx.ravel()
    cosv = val.ravel()
    rel = pd.DataFrame({"col_a": inc[a], "symbol_a": sym[inc[a]], "col_b": inc[b], "symbol_b": sym[inc[b]],
                        "rank": np.tile(np.arange(1, kk + 1), n), "cos": cosv, "abs_cos": np.abs(cosv)})
    rel["z_gene"] = (cosv - med[a]) / np.maximum(mad[a], 1e-6)
    if have_halves:
        h1 = _pair_cos(U1[a], U1[b])
        h2 = _pair_cos(U2[a], U2[b])
        rel["cos_half1"], rel["cos_half2"] = h1, h2
        curve = _fdr_curve(U1, U2, min(top, 50))
        write_csv(curve, os.path.join(rd, "fdr_curve.csv"))
        agree = np.sign(h1) == np.sign(h2)
        t = np.where(agree, np.minimum(np.abs(h1), np.abs(h2)), 0.0)
        fdr = np.where(agree, np.interp(t, curve["t"].to_numpy(), curve["fdr"].to_numpy()), 1.0)
        rel["fdr"] = fdr.astype(np.float32)
        sg = np.sign(cosv)
        both = (np.sign(h1) == sg) & (np.sign(h2) == sg) & (np.minimum(np.abs(h1), np.abs(h2)) >= REPRO_MIN) & \
            (fdr <= REPRO_FDR)
        one = ~both & (np.maximum(np.abs(h1), np.abs(h2)) >= ONE_HALF) & \
            (np.minimum(np.abs(h1), np.abs(h2)) < REPRO_MIN)
        rel["evidence"] = np.where(both, "both halves", np.where(one, "one half", "not reproduced"))
    else:
        rel["cos_half1"] = rel["cos_half2"] = np.nan
        rel["evidence"] = "not reproduced"
        rel["fdr"] = np.nan
    rel["reproducible"] = rel["evidence"] == "both halves"

    ann, sets, string = _load_reference(out, gK)
    ca, cb = rel["col_a"].to_numpy(), rel["col_b"].to_numpy()
    if ann is not None and "chrom" in ann:
        chrom = ann["chrom"].astype(str).to_numpy()
        st = pd.to_numeric(ann["start"], errors="coerce").to_numpy()
        en = pd.to_numeric(ann["end"], errors="coerce").to_numpy()
        strand = ann["strand"].astype(str).to_numpy()
        same = (chrom[ca] == chrom[cb]) & (chrom[ca] != "nan") & (chrom[ca] != "None") & np.isfinite(st[ca]) \
            & np.isfinite(st[cb])
        gap = np.maximum(0, np.maximum(st[ca], st[cb]) - np.minimum(en[ca], en[cb]))
        rel["coords_known"] = np.isfinite(st[ca]) & np.isfinite(st[cb])
        rel["same_chrom"] = same
        rel["distance_bp"] = np.where(same, gap, np.nan)
        rel["same_strand"] = same & (strand[ca] == strand[cb])
        rel["locus"] = same & (gap <= LOCUS_BP)
        cpm = pd.read_parquet(os.path.join(out, "tables", "genes.parquet"))["pooled_cpm"].to_numpy() \
            if os.path.exists(os.path.join(out, "tables", "genes.parquet")) else \
            pd.read_csv(os.path.join(out, "atlas", "effects", "genes.csv"))["pooled_cpm"].to_numpy()[:gK]
        # the 5' gene on the shared strand: + strand -> smaller start; - strand -> larger end
        plus = strand[ca] == "+"
        a_is_5p = np.where(plus, st[ca] < st[cb], en[ca] > en[cb])
        up, dn = np.where(a_is_5p, ca, cb), np.where(a_is_5p, cb, ca)
        rel["readthrough_risk"] = rel["same_strand"].to_numpy() & (gap <= READTHROUGH_BP) & \
            (cpm[up] >= READTHROUGH_RATIO * np.maximum(cpm[dn], 1e-9))
    else:
        for c in ("coords_known", "same_chrom", "same_strand", "locus", "readthrough_risk"):
            rel[c] = False
        rel["distance_bp"] = np.nan
    groups, paths, names = _set_index(sets, gK)
    shared_g = np.array([bool(groups[x] & groups[y]) for x, y in zip(ca, cb)])
    shared_p = []
    for x, y in zip(ca, cb):
        s = paths[x] & paths[y]
        shared_p.append(names.get(min(s), "") if s else "")
    rel["shared_gene_group"] = shared_g
    rel["shared_pathway"] = shared_p
    if string is not None and len(string):
        lo, hi = np.minimum(ca, cb), np.maximum(ca, cb)
        key = pd.Series(string["score"].to_numpy(),
                        index=pd.MultiIndex.from_arrays([string["col_a"].astype(int), string["col_b"].astype(int)]))
        key = key[~key.index.duplicated()]
        rel["string_score"] = key.reindex(pd.MultiIndex.from_arrays([lo, hi])).to_numpy()
    else:
        rel["string_score"] = np.nan
    have_ref = ann is not None
    rel["known"] = rel["shared_gene_group"] | (rel["shared_pathway"] != "") | rel["string_score"].notna()
    # "not known" only means something for two genes the registries actually describe
    if have_ref and "matched_by" in ann:
        rec = (ann["matched_by"].fillna("none").astype(str) != "none").to_numpy()
        both_recorded = rec[ca] & rec[cb]
    else:
        both_recorded = np.zeros(len(rel), dtype=bool)
    rel["both_annotated"] = both_recorded
    # specificity: is each gene among the other's strongest partners, and exceptional for it? At full scale broad
    # programmes give hundreds of thousands of pairs the same sign in both halves; a candidate must also be specific.
    rev = pd.DataFrame({"col_a": rel["col_b"].to_numpy(), "col_b": rel["col_a"].to_numpy(),
                        "rank_ba": rel["rank"].to_numpy(), "z_ba": rel["z_gene"].to_numpy()})
    rel = rel.merge(rev, on=["col_a", "col_b"], how="left")
    rel["mutual_rank"] = np.maximum(rel["rank"], rel["rank_ba"].fillna(np.inf))
    rel["specificity"] = np.minimum(rel["z_gene"].abs(), rel["z_ba"].abs().fillna(0.0))
    ca, cb = rel["col_a"].to_numpy(), rel["col_b"].to_numpy()
    both_recorded = rel["both_annotated"].to_numpy()
    blocked = _missing_sources(out) if have_ref else ["reference stage not run"]
    rel["novel_candidate"] = (not blocked) & both_recorded & rel["coords_known"] & rel["reproducible"] & \
        (rel["fdr"] <= NOVEL_FDR) & (rel["abs_cos"] >= NOVEL_COS) & ~rel["known"] & ~rel["locus"] & \
        (rel["mutual_rank"] <= NOVEL_MUTUAL_RANK) & (rel["specificity"] >= NOVEL_SPECIFICITY)
    if blocked:
        log(f"  novel candidates not assessed: missing {', '.join(blocked)} (run 'tahoe run --from reference' "
            "with network access)")
    fo = eg["evidence_flagged_only"].fillna(False).astype(bool).to_numpy() if "evidence_flagged_only" in eg \
        else np.zeros(gK, dtype=bool)

    # lineage pairs: both genes expressed in few lines, mostly the same (module docstring)
    E, e_src = expressed_mask(out, gK)
    lin_info = {"source": e_src, "max_share": LINEAGE_MAX_SHARE, "min_jaccard": LINEAGE_MIN_J,
                "bins": list(LINEAGE_BINS), "cos": LINEAGE_COS}
    lin_text = np.full(len(rel), "", dtype=object)
    if E is not None:
        na, nb_, sh, J = lineage_columns(ca, cb, E)
        null = lineage_null(U, inc, E)
        restricted = np.zeros(gK, dtype=bool)
        restricted[inc[null["restricted"]]] = True
        lp = restricted[ca] & restricted[cb] & (J >= LINEAGE_MIN_J)
        p_, share_ = lineage_p_values(rel["abs_cos"].to_numpy(), J, null)
        p_ = np.where(lp, p_, np.nan)
        for i in np.flatnonzero(lp):
            lin_text[i] = lineage_reason(na[i], nb_[i], null["L"], sh[i], share_[i], p_[i])
        rel["n_lines_a"], rel["n_lines_b"], rel["lines_shared"] = na, nb_, sh
        rel["lines_jaccard"] = J.astype(np.float32)
        rel["lineage_pair"] = lp
        rel["lineage_p"] = p_.astype(np.float32)
        bn, bh = null["below"]
        lin_info.update({"lines": null["L"], "max_lines": null["max_lines"], "restricted_genes": null["genes"],
                         "null_genes": null["null_genes"], "null_sampled": null["sampled"],
                         "null_pairs": null["pairs"],
                         "share_ge_0.5": {f"{lo:g}-{min(hi, 1.0):g}": (round(v, 4) if np.isfinite(v) else None)
                                          for lo, hi, v in zip(LINEAGE_BINS[:-1], LINEAGE_BINS[1:], null["share"])},
                         "pairs_per_bin": [int(x.size) for x in null["sorted"]],
                         "share_ge_0.5_below_min_jaccard": round(bh / bn, 4) if bn else None})
        log(f"  lineage pairs: {int(lp.sum()):,} rows of genes expressed in <= {null['max_lines']} of {null['L']} "
            f"lines with Jaccard >= {LINEAGE_MIN_J:g} ({null['genes']:,} restricted genes; null of "
            f"{null['pairs']:,} pairs)")
    else:
        rel["n_lines_a"] = rel["n_lines_b"] = rel["lines_shared"] = np.int16(-1)
        rel["lines_jaccard"] = np.float32(np.nan)
        rel["lineage_pair"] = False
        rel["lineage_p"] = np.float32(np.nan)
        log(f"  lineage pairs {e_src}")

    # read-sharing copies (module docstring)
    rs_src = read_sharing_source(out)
    rs = read_sharing_pairs(out) if not rs_src.startswith("not assessed") else {}
    rs_kind, rs_text = read_sharing_columns(ca, cb, rs)
    rel["read_sharing"] = rs_kind
    rel["read_sharing_risk"] = rs_kind != ""
    extra = np.array(["; ".join(t for t in (x, y) if t) for x, y in zip(lin_text, rs_text)], dtype=object)
    before = pair_alerts(rel, fo, sym, have_halves)
    rel["alert"] = pair_alerts(rel, fo, sym, have_halves, extra=extra)
    write_parquet(rel, os.path.join(rd, "gene_relations.parquet"))

    counts = count_info(rel)
    fo_rows = fo[ca] | fo[cb]
    key = np.minimum(ca, cb) * (gK + 1) + np.maximum(ca, cb)
    nov = rel["novel_candidate"].to_numpy(bool)
    lpm = rel["lineage_pair"].to_numpy(bool)
    rsm = rel["read_sharing_risk"].to_numpy(bool)
    lpv = rel["lineage_p"].to_numpy(np.float64)
    lin_info.update({"rows": counts["rows_lineage"], "pairs": counts["pairs_lineage"],
                     "novel_candidate_pairs": int(np.unique(key[nov & lpm]).size),
                     "novel_candidate_pairs_lineage_p_ge_0.01": int(np.unique(key[nov & lpm & (lpv >= 0.01)]).size)})
    kinds = {k: sum(1 for v in rs.values() if v[0] == k) for k in READSHARE_KINDS}
    rs_info = {"source": rs_src, "pid": READSHARE_PID, "pairs_among_genes": int(len(rs)), "by_kind": kinds,
               "rows": counts["rows_read_sharing"], "pairs": counts["pairs_read_sharing"],
               "rows_without_another_alert": int((rsm & (before == "")).sum()),
               "novel_candidate_pairs": int(np.unique(key[nov & rsm]).size)}
    info = {"version": VERSION, "genes": int(n), "top": int(kk), **counts,
            "rows_flagged_only_gene": int(fo_rows.sum()), "pairs_flagged_only_gene": int(np.unique(key[fo_rows]).size),
            "evidence_both_halves": f"{SAME_SIGN} ({SAME_SIGN_NOTE})",
            "lineage": lin_info, "read_sharing_source": rs_src, "read_sharing": rs_info,
            "reference": bool(have_ref), "novel_assessed": not blocked, "novel_blocked_by": blocked,
            "repro_fdr": REPRO_FDR, "minutes": round((time.time() - t0) / 60, 2)}
    write_json(info, os.path.join(rd, "info.json"))
    stamp_stage(out, "relations", VERSION, info)
    log(f"  read-sharing copies {rs_src}" if rs_src.startswith("not assessed") else
        f"  read-sharing copies ({rs_src}): {len(rs):,} pairs among the genes, {counts['pairs_read_sharing']:,} of "
        "them among the partners")
    log(f"Relations done: {counts['pairs_both_halves']:,} pairs with the {SAME_SIGN} "
        f"({counts['share_rows_both_halves']:.1%} of partner rows), {counts['pairs_novel_candidate']:,} novel "
        f"candidate pairs ({info['minutes']} min)")
    return info
