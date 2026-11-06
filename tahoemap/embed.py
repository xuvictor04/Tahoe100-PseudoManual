"""embed - one vector space for genes, drug-doses, drug-dose x cell-line contexts and cell lines.

Every gene is described by how it moves across perturbations: its per-line z (tensor DDL_z) in every
(drug-dose, cell line) context of an active, trustworthy drug-dose (not 'unreliable plate only', 'position not
correctable' or 'wells disagree'; active = >= min_active significant genes pooled over lines, OR >= min_active genes
at per-line |z| >= 5 in >= 2 lines, so a response confined to a few lines enters too). A gene enters the space only
if it reaches |z| >= 3 in >= min_responsive of these contexts AND has real evidence of a response: a significant
clean pooled drug-dose (the atlas's q < 0.1 and >= 1.2x, BH within the gene), or a per-line |z| >= max(5, the
tables stage's calibrated per-line cut) in >= 2 lines of one trustworthy drug-dose. At full scale almost every
expressed gene reaches a fixed count of |z| >= 3 contexts by chance alone, so the count is not enough. That matrix X (genes x contexts) is factorised,
X ~ U S V', after removing the broad components that make every gene look related (global toxicity / shutdown axes;
the atlas's "programs" rule). Then, in one k-dimensional space:

    gene vector          g = U S          (its direction is the gene's response pattern; cosine between two genes
                                           = correlation of their denoised response profiles)
    context vector       c = V            (one per drug-dose x line)
    drug-dose vector     d = S^-1 U' x    (x = its pooled z profile, standardised like X; also for drug-doses that
                                           were not used to fit the space)
    drug vector          U' x = S d       (of the drug's best trustworthy dose; principal coordinates, for
                                           drug-drug cosine)
    predicted z          g . c  or  g . d (the dot product reproduces the observed activity)
    line vector          s_l[k] = how strongly component k responds in line l relative to the typical line
                                  (slope of the line's context vectors on the drug-doses' mean vectors)
    line baseline vector the line's untreated expression profile projected the same way

Sign matters in this space: two genes that respond in opposite directions to the same perturbations have cosine
near -1 and sit far apart; the nodal map (graph stage) uses |cosine| instead and puts them together.

Reproducibility: compounds (salt forms merged) are dealt into two halves and the space is fitted again on each half;
relations.run compares gene-gene cosines between the halves (independent perturbations).
"""

import os
import time
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import tlib as T
from .common import (folder, log, read_effects_index, save_npy, stable_seed, stamp_stage, write_json,
                     write_parquet)

VERSION = 2
UNTRUSTED = ("unreliable plate only", "position not correctable", "wells disagree")
LINE_ACTIVE_Z = 5.0    # a drug-dose is also active when >= min_active genes reach this per-line |z| in >= 2 lines
Z_CLIP = 8.0
BROAD_R = 0.3          # a broad component: |gene-component r| >= this ...
BROAD_FRAC = 0.05      # ... for >= this share of the genes (and >= BROAD_MIN genes), among the first BROAD_MAXPC
BROAD_MIN = 200
BROAD_MAXPC = 3


def _svd(X, k, seed):
    from sklearn.utils.extmath import randomized_svd
    k = int(max(1, min(k, min(X.shape) - 1)))
    U, S, Vt = randomized_svd(X, n_components=k, n_iter=6, n_oversamples=20, random_state=seed)
    return U.astype(np.float32), S.astype(np.float32), Vt.astype(np.float32)


def _standardise(X):
    """Centre each gene's row and scale it by max(its SD, the median SD): weakly responsive genes are not blown up."""
    mu = X.mean(axis=1, keepdims=True)
    X -= mu
    sd = np.sqrt(np.einsum("ij,ij->i", X, X) / max(X.shape[1], 1))[:, None]
    floor = float(np.median(sd[sd > 0])) if (sd > 0).any() else 1.0
    sc = np.maximum(sd, floor)
    X /= sc
    return mu.ravel(), sc.ravel()


def _remove_broad(X, seed, n_genes, tag):
    """Remove (in place) broad components among the first BROAD_MAXPC; return the record of every tested one."""
    U, S, Vt = _svd(X, min(10, min(X.shape) - 1), seed)
    norms = np.sqrt(np.einsum("ij,ij->i", X, X))
    norms[norms == 0] = 1.0
    rows, removed = [], []
    need = max(BROAD_MIN, BROAD_FRAC * n_genes)
    tot = float(np.einsum("ij,ij->i", X, X).sum())
    for j in range(len(S)):
        r = U[:, j] * S[j] / norms
        n_follow = int((np.abs(r) >= BROAD_R).sum())
        broad = j < BROAD_MAXPC and n_follow >= need
        rows.append({"fit": tag, "component": j + 1, "variance_pct": 100.0 * float(S[j] ** 2) / max(tot, 1e-12),
                     "genes_following": n_follow, "removed": broad})
        if broad:
            removed.append(j)
    for j in removed:                                     # X -= u s v' in row blocks (no big temporary)
        u, s, v = U[:, j], S[j], Vt[j]
        for r0 in range(0, X.shape[0], 4096):
            X[r0:r0 + 4096] -= np.outer(u[r0:r0 + 4096] * s, v).astype(np.float32)
    return rows, removed, (U, S, Vt)


def _fit(X, k, seed, n_genes, tag):
    rows, removed, first = _remove_broad(X, seed, n_genes, tag)
    remaining = float(np.einsum("ij,ij->i", X, X).astype(np.float64).sum())
    U, S, Vt = _svd(X, k, seed + 1)
    return U, S, Vt, rows, removed, remaining


def run(out, dims=64, min_active=10, min_responsive=5, chunk=512, halves=True):
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    ed = folder(out, "embed")
    fxd = os.path.join(out, "atlas", "effects")
    ix = read_effects_index(fxd)
    genes, dd, lines = ix["genes"], ix["drugdose"], ix["lines"]
    gK = int((genes["kind"] == "gene").sum())
    Dn, L = len(dd), len(lines)
    DDL_z = np.load(os.path.join(out, "tensor", "DDL_z.npy"), mmap_mode="r")
    flags = dd["flags"].fillna("").astype(str)
    trusted = ~flags.apply(lambda f: any(u in f for u in UNTRUSTED)).to_numpy()
    pooled_active = trusted & (dd["n_sig_genes"].to_numpy() >= min_active)
    noise = genes["symbol"].astype(str).str.match(A.NOISE_RNA_RE).to_numpy()[:gK]

    # pass 1 over every drug-dose: per gene x drug-dose, how many lines reach |z| >= 3 and |z| >= line_z; per
    # drug-dose x line, how many genes reach |z| >= LINE_ACTIVE_Z (a response confined to a few lines)
    line_z = LINE_ACTIVE_Z
    tinfo = os.path.join(out, "tables", "info.json")
    if os.path.exists(tinfo):                             # the calibrated per-line cut of the tables stage
        import json
        with open(tinfo, encoding="utf-8") as fh:
            line_z = max(line_z, float(json.load(fh).get("line_z_threshold", line_z) or line_z))
    hit = np.zeros((gK, Dn), dtype=np.int16)
    strong = np.zeros((gK, Dn), dtype=np.int16)
    line_hits = np.zeros((Dn, L), dtype=np.int64)
    for g0 in range(0, gK, chunk):
        Z = np.abs(np.nan_to_num(np.asarray(DDL_z[g0:g0 + chunk], dtype=np.float32)))   # chunk x Dn x L
        hit[g0:g0 + chunk] = (Z >= 3).sum(axis=2)
        strong[g0:g0 + chunk] = (Z >= line_z).sum(axis=2)
        line_hits += (Z >= LINE_ACTIVE_Z).sum(axis=0)
    line_active = trusted & ((line_hits >= min_active).sum(axis=1) >= 2)
    active = pooled_active | line_active
    dsel = np.flatnonzero(active)
    if dsel.size < 5:                                     # tiny runs: fall back to every trusted drug-dose
        dsel = np.flatnonzero(trusted)
    log(f"Embed: {dsel.size:,} active trustworthy drug-doses (of {Dn:,}; {int((line_active & ~pooled_active).sum())} "
        f"of them active only in single lines) x {L} lines as contexts")

    # a gene enters the space only if it really responds: a fixed count of |z| >= 3 contexts is reached by chance by
    # almost every expressed gene at full scale, so it also needs a significant clean pooled drug-dose (the atlas's
    # BH within the gene), or a strong per-line response (|z| >= line_z) in >= 2 lines of one trustworthy drug-dose
    n_resp = hit[:, dsel].sum(axis=1).astype(np.int64)
    qup = np.load(os.path.join(fxd, "DD_qup.npy"), mmap_mode="r")
    qdn = np.load(os.path.join(fxd, "DD_qdn.npy"), mmap_mode="r")
    lfc = np.load(os.path.join(fxd, "DD_lfc.npy"), mmap_mode="r")
    clean = ~flags.apply(A.has_artifact).to_numpy()
    sig = np.zeros(gK, dtype=bool)
    for g0 in range(0, gK, 4096):
        g1 = min(gK, g0 + 4096)
        u = (np.asarray(qup[:, g0:g1]) < A.Q_CUT) & (np.asarray(lfc[:, g0:g1]) >= A.LFC_MIN)
        d_ = (np.asarray(qdn[:, g0:g1]) < A.Q_CUT) & (np.asarray(lfc[:, g0:g1]) <= -A.LFC_MIN)
        sig[g0:g1] = ((u | d_) & clean[:, None]).any(axis=0)
    line_resp = ((strong >= 2) & trusted[None, :]).any(axis=1)
    evidence_ok = sig | line_resp
    by_chance = (n_resp >= min_responsive) & ~evidence_ok
    gsel = np.flatnonzero((n_resp >= min_responsive) & evidence_ok & ~noise)
    del hit, strong
    ctx_fin = np.zeros(dsel.size * L, dtype=np.int64)
    for g0 in range(0, gK, chunk):
        Z = np.asarray(DDL_z[g0:g0 + chunk][:, dsel, :], dtype=np.float32).reshape(-1, dsel.size * L)
        ctx_fin += np.isfinite(Z).sum(axis=0)
    cmask = ctx_fin >= max(10, 0.2 * gK)
    cidx = np.flatnonzero(cmask)
    log(f"  {gsel.size:,} responsive genes of {gK:,} (|z| >= 3 in >= {min_responsive} contexts, and a significant "
        f"clean pooled drug-dose ({int((sig & ~noise).sum()):,} genes) or per-line |z| >= {line_z:g} in >= 2 lines of "
        f"one drug-dose ({int((line_resp & ~noise).sum()):,})); {int(by_chance.sum()):,} reached the count without "
        f"either; {cidx.size:,} contexts with data")
    if gsel.size < 10 or cidx.size < 10:
        raise SystemExit("embed: too few responsive genes or contexts to build a vector space")

    X = np.empty((gsel.size, cidx.size), dtype=np.float32)
    for i0 in range(0, gsel.size, chunk):
        gg = gsel[i0:i0 + chunk]
        Z = np.asarray(DDL_z[gg][:, dsel, :], dtype=np.float32).reshape(len(gg), dsel.size * L)[:, cidx]
        np.clip(Z, -Z_CLIP, Z_CLIP, out=Z)
        X[i0:i0 + len(gg)] = np.nan_to_num(Z, nan=0.0)
    ctx_dd = np.repeat(dsel, L)[cidx]
    ctx_line = np.tile(np.arange(L), dsel.size)[cidx]

    # halves by compound (salt forms together)
    base = dd["drug"].astype(str).map(T.salt_base).to_numpy()
    half_of_dd = np.array([stable_seed("half", b) % 2 for b in base])
    Xh = None
    if halves:
        Xh = [X[:, half_of_dd[ctx_dd] == h].copy() for h in (0, 1)]

    mu, sc = _standardise(X)
    seed = stable_seed("embed", gsel.size, cidx.size)
    U, S, Vt, broad_rows, removed, remaining = _fit(X, dims, seed, gsel.size, "all")
    k = len(S)
    captured = 100.0 * float((S.astype(np.float64) ** 2).sum()) / max(remaining, 1e-12)
    log(f"  broad components removed: {', '.join(str(j + 1) for j in removed) or 'none'}; space: {k} dimensions "
        f"holding {captured:.1f}% of the remaining variance")
    gvec = U * S[None, :]                                  # gene vectors (principal coordinates)
    gnorm = np.sqrt((gvec ** 2).sum(axis=1))
    rownorm = np.sqrt(np.einsum("ij,ij->i", X, X))
    represented = np.where(rownorm > 0, (gnorm / np.maximum(rownorm, 1e-12)) ** 2, np.nan)
    del X

    def full(rows_vals, width):
        arr = np.full((gK, width), np.nan, dtype=np.float32)
        arr[gsel] = rows_vals
        return arr

    unit = gvec / np.maximum(gnorm[:, None], 1e-12)
    save_npy(os.path.join(ed, "gene_vectors.npy"), full(gvec, k))
    save_npy(os.path.join(ed, "gene_unit.npy"), full(unit, k))
    save_npy(os.path.join(ed, "singular_values.npy"), S)
    save_npy(os.path.join(ed, "context_vectors.npy"), Vt.T.copy())

    # half spaces
    if halves:
        for h in (0, 1):
            Xh_ = Xh[h]
            _standardise(Xh_)
            Uh, Sh, _Vh, rows_h, rem_h, _ = _fit(Xh_, dims, seed + 10 + h, gsel.size, f"half{h + 1}")
            broad_rows += rows_h
            gh = Uh * Sh[None, :]
            gh /= np.maximum(np.sqrt((gh ** 2).sum(axis=1))[:, None], 1e-12)
            save_npy(os.path.join(ed, f"gene_unit_half{h + 1}.npy"), full(gh, len(Sh)))
            log(f"  half {h + 1}: {Xh_.shape[1]:,} contexts, broad removed: "
                f"{', '.join(str(j + 1) for j in rem_h) or 'none'}")
        del Xh

    # projections: every drug-dose (pooled z) and every line's baseline
    DD_z = np.load(os.path.join(fxd, "DD_z.npy"), mmap_mode="r")
    P = (U / S[None, :]).astype(np.float32)               # x (standardised, over gsel) -> S^-1 U' x
    xd = np.clip(np.nan_to_num(np.asarray(DD_z[:, gsel], dtype=np.float32), nan=0.0), -Z_CLIP, Z_CLIP)
    xd = (xd - mu[None, :]) / sc[None, :]
    dvec = xd @ P                                          # Dn x k
    save_npy(os.path.join(ed, "drugdose_vectors.npy"), dvec.astype(np.float32))

    line_cpm = np.load(os.path.join(fxd, "line_cpm.npy"))[:, gsel]
    yb = np.log2(line_cpm + 1.0)
    yb = yb - np.median(yb, axis=0, keepdims=True)
    lb = (yb / sc[None, :]) @ P
    save_npy(os.path.join(ed, "line_baseline_vectors.npy"), lb.astype(np.float32))

    # line response sensitivity: slope of each line's context vectors on the drug-dose's mean over lines
    V = Vt.T                                               # contexts x k
    dpos = {d: i for i, d in enumerate(dsel)}
    D_mean = np.zeros((dsel.size, k), dtype=np.float64)
    cnt = np.zeros(dsel.size)
    for j in range(V.shape[0]):
        i = dpos[ctx_dd[j]]
        D_mean[i] += V[j]
        cnt[i] += 1
    D_mean /= np.maximum(cnt, 1)[:, None]
    sens = np.full((L, k), np.nan, dtype=np.float32)
    for l in range(L):
        jj = np.flatnonzero(ctx_line == l)
        if jj.size < 5:
            continue
        ref = D_mean[[dpos[d] for d in ctx_dd[jj]]]
        den = (ref ** 2).sum(axis=0)
        sens[l] = np.where(den > 0, (V[jj] * ref).sum(axis=0) / np.maximum(den, 1e-12), np.nan)
    save_npy(os.path.join(ed, "line_response_vectors.npy"), sens)

    # tables
    sym = genes["symbol"].astype(str).to_numpy()
    lab = genes["label"].astype(str).to_numpy()
    inc = np.zeros(gK, dtype=bool)
    inc[gsel] = True
    gtab = pd.DataFrame({"col": np.arange(gK), "symbol": sym[:gK], "label": lab[:gK], "included": inc,
                         "n_responsive_contexts": n_resp, "vector_norm": np.nan, "represented_fraction": np.nan,
                         "noise_rna": noise})
    gtab.loc[gsel, "vector_norm"] = gnorm
    gtab.loc[gsel, "represented_fraction"] = represented
    write_parquet(gtab, os.path.join(ed, "genes.parquet"))
    cell = lines["cell_name"].fillna(lines["cell_line_id"]).astype(str).to_numpy()
    ctab = pd.DataFrame({"j": np.arange(cidx.size), "dd": ctx_dd, "line": ctx_line,
                         "drug": dd["drug"].to_numpy()[ctx_dd], "dose": dd["dose"].to_numpy()[ctx_dd],
                         "cell_line_id": lines["cell_line_id"].to_numpy()[ctx_line], "cell_name": cell[ctx_line],
                         "half": half_of_dd[ctx_dd] + 1})
    write_parquet(ctab, os.path.join(ed, "contexts.parquet"))
    ddt = dd[["drug", "dose", "conc", "n_sig_genes", "flags"]].copy()
    ddt.insert(0, "dd", np.arange(Dn))
    ddt["active_context"] = np.isin(np.arange(Dn), dsel)
    ddt["half"] = half_of_dd + 1
    ddt["vector_norm"] = np.sqrt((dvec.astype(np.float64) ** 2).sum(axis=1))
    write_parquet(ddt, os.path.join(ed, "drugdoses.parquet"))

    # one vector per drug: its best dose (most significant genes; tie -> higher dose)
    # one vector per drug: its best trustworthy dose (most significant genes; tie -> higher dose), in principal
    # coordinates (U'x = S d), which weight the components by their size: these are for drug-drug cosine
    dd2 = dd.assign(dd=np.arange(Dn), conc_num=pd.to_numeric(dd["conc"], errors="coerce").fillna(0),
                    trusted=trusted, untrusted=~trusted)
    best = dd2.sort_values(["drug", "untrusted", "n_sig_genes", "conc_num"], ascending=[True, True, False, False]) \
        .drop_duplicates("drug").sort_values("drug")
    save_npy(os.path.join(ed, "drug_vectors.npy"), (dvec[best["dd"].to_numpy()] * S[None, :]).astype(np.float32))
    cols_ = [c for c in ("drug", "dose", "dd", "n_sig_genes", "trusted", "moa_fine", "targets") if c in best.columns]
    write_parquet(best[cols_].reset_index(drop=True), os.path.join(ed, "drugs.parquet"))

    # components: what each axis is
    comp = []
    var_tot = float((S.astype(np.float64) ** 2).sum())
    dlabel = (dd["drug"].astype(str) + " " + dd["dose"].astype(str)).to_numpy()
    for j in range(k):
        o = np.argsort(U[:, j])
        od = np.argsort(dvec[:, j])
        oline = np.argsort(-np.nan_to_num(sens[:, j], nan=-np.inf))
        comp.append({"component": j + 1, "variance_pct_of_space": 100.0 * float(S[j]) ** 2 / max(var_tot, 1e-12),
                     "top_pos_genes": ", ".join(sym[gsel[o[::-1][:15]]]),
                     "top_neg_genes": ", ".join(sym[gsel[o[:15]]]),
                     "top_pos_drugdoses": "; ".join(dlabel[od[::-1][:10]]),
                     "top_neg_drugdoses": "; ".join(dlabel[od[:10]]),
                     "most_sensitive_lines": ", ".join(cell[oline[:8]])})
    write_parquet(pd.DataFrame(comp), os.path.join(ed, "components.parquet"))
    pd.DataFrame(broad_rows).to_csv(os.path.join(ed, "broad_components.csv"), index=False)
    info = {"version": VERSION, "dims": k, "genes_included": int(gsel.size), "genes_total": gK,
            "contexts": int(cidx.size), "drugdoses_active": int(dsel.size), "drugdoses_total": Dn, "lines": L,
            "min_active": min_active, "min_responsive": min_responsive, "z_clip": Z_CLIP,
            "drugdoses_active_pooled": int(pooled_active.sum()), "drugdoses_active_lines_only":
                int((line_active & ~pooled_active).sum()), "line_active_z": LINE_ACTIVE_Z,
            "line_z_responsive": line_z, "n_genes_significant_pooled": int((sig & ~noise).sum()),
            "n_genes_line_responsive": int((line_resp & ~noise).sum()),
            "n_genes_excluded_chance": int(by_chance.sum()),
            "broad_removed": [int(j) + 1 for j in removed], "halves": bool(halves),
            "variance_captured_pct": round(captured, 2),
            "singular_values": [float(s) for s in S], "minutes": round((time.time() - t0) / 60, 2),
            "model": "X ~ U S V'; gene g = U S; context c = V; drug-dose d = S^-1 U' x; predicted z = g . c or "
                     "g . d (in standardised units); drug_vectors = U' x of the best trustworthy dose (cosine)"}
    write_json(info, os.path.join(ed, "info.json"))
    save_npy(os.path.join(ed, "gene_row_mean.npy"), mu.astype(np.float32))
    save_npy(os.path.join(ed, "gene_row_scale.npy"), sc.astype(np.float32))
    save_npy(os.path.join(ed, "included_cols.npy"), gsel.astype(np.int64))
    stamp_stage(out, "embed", VERSION, info)
    log(f"Embed done: {gsel.size:,} genes in {k} dimensions from {cidx.size:,} contexts ({info['minutes']} min)")
    return info
