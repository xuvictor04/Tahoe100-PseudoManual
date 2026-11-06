"""relations - gene x gene: which genes move with each gene, which move opposite, and how sure we are.

For every gene in the vector space (embed stage) the 100 partners with the largest |cosine| are kept, with:

  cos            signed cosine of the two genes' unit vectors = correlation of their denoised response profiles
                 across every (drug-dose, cell line) context. + : they go up and down together; - : opposite.
  z_gene         that cosine as a robust z against all of this gene's partners (a gene with a broad response
                 has many moderate cosines; z says how exceptional this partner is for this gene)
  cos_half1/2    the same cosine in the two spaces fitted on two disjoint halves of the compounds
  evidence       "both halves"     same sign in the full space and in both halves, min |half cos| >= 0.2
                 "one half"        strong (>= 0.5) in one half only: the driving compounds sit in one half
                                   (a relation seen with one drug family; real, but not replicated across drugs)
                 "not reproduced"  otherwise
  fdr            sign-concordance false discovery rate. Pairs are selected in one half's space and their sign is
                 checked in the other half, whose noise is independent: under no relation the sign agrees half the
                 time, so FDR(t) = #disagreeing / #agreeing pairs with |other-half cos| >= t (both directions pooled,
                 made monotone). A pair's fdr is read at t = min(|cos_half1|, |cos_half2|) (conservative).
  genomic flags  same chromosome, gap in bp, same strand, locus (<= 50 kb apart), readthrough_risk (same strand,
                 <= 20 kb, the 5' gene >= 8x more expressed: transcription running past the 5' gene is counted as
                 the 3' gene's mRNA, so the pair correlates without any regulation)
  known flags    shared HGNC gene group, shared pathway (Hallmark, or a Reactome pathway of <= 300 genes),
                 STRING combined score (>= 400 kept)
  novel_candidate  evidence "both halves", fdr <= 0.05, |cos| >= 0.5, not known, not the same locus, and both
                 genes have a registry (HGNC) record (for an undescribed gene "not known" means nothing)

Without the reference stage the genomic and known flags are empty and nothing is called novel.
"""

import os
import time
import warnings

import numpy as np
import pandas as pd

from .common import folder, log, stamp_stage, write_csv, write_json, write_parquet

VERSION = 1
TOP = 100
REPRO_MIN = 0.2
ONE_HALF = 0.5
NOVEL_COS = 0.5
NOVEL_FDR = 0.05
LOCUS_BP = 50_000
READTHROUGH_BP = 20_000
READTHROUGH_RATIO = 8.0
PATHWAY_MAX = 300


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
    raw = np.minimum(1.0, np.where(n_ag > 0, n_dis / np.maximum(n_ag, 1), 1.0))
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
        sg = np.sign(cosv)
        both = (np.sign(h1) == sg) & (np.sign(h2) == sg) & (np.minimum(np.abs(h1), np.abs(h2)) >= REPRO_MIN)
        one = ~both & (np.maximum(np.abs(h1), np.abs(h2)) >= ONE_HALF) & \
            (np.minimum(np.abs(h1), np.abs(h2)) < REPRO_MIN)
        rel["evidence"] = np.where(both, "both halves", np.where(one, "one half", "not reproduced"))
        curve = _fdr_curve(U1, U2, min(top, 50))
        write_csv(curve, os.path.join(rd, "fdr_curve.csv"))
        t = np.where(np.sign(h1) == np.sign(h2), np.minimum(np.abs(h1), np.abs(h2)), 0.0)
        fdr = np.interp(t, curve["t"].to_numpy(), curve["fdr"].to_numpy())
        rel["fdr"] = np.where(np.sign(h1) == np.sign(h2), fdr, 1.0).astype(np.float32)
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
        for c in ("same_chrom", "same_strand", "locus", "readthrough_risk"):
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
    rel["novel_candidate"] = have_ref & both_recorded & rel["reproducible"] & (rel["fdr"] <= NOVEL_FDR) & \
        (rel["abs_cos"] >= NOVEL_COS) & ~rel["known"] & ~rel["locus"]
    write_parquet(rel, os.path.join(rd, "gene_relations.parquet"))
    und = rel[rel["col_a"] < rel["col_b"]]
    info = {"version": VERSION, "genes": int(n), "top": int(kk), "pairs": int(len(rel)),
            "reproducible_pairs": int(und["reproducible"].sum()),
            "one_half_pairs": int((und["evidence"] == "one half").sum()),
            "fdr_le_0.05_pairs": int((und["fdr"] <= 0.05).sum()) if have_halves else None,
            "known_pairs": int(und["known"].sum()), "locus_pairs": int(und["locus"].sum()),
            "readthrough_risk_pairs": int(und["readthrough_risk"].sum()),
            "novel_candidate_pairs": int(und["novel_candidate"].sum()), "reference": bool(have_ref),
            "minutes": round((time.time() - t0) / 60, 2)}
    write_json(info, os.path.join(rd, "info.json"))
    stamp_stage(out, "relations", VERSION, info)
    log(f"Relations done: {info['reproducible_pairs']:,} reproducible pairs (both halves), "
        f"{info['novel_candidate_pairs']:,} novel candidates ({info['minutes']} min)")
    return info
