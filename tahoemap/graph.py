"""graph - the 2D nodal map of gene relatedness, its modules, and a signed map for comparison.

Two different questions give two different maps:

  nodal map (x, y)    "how closely related are these genes?"  Distance = 1 - |cos|. Genes that respond in OPPOSITE
                      directions to the same perturbations (cos near -1) are as related as genes that respond the
                      same way, so they land next to each other: the two arms of one pathway form one island.
  signed map (xs, ys) "do these genes do the same thing?"  Distance = 1 - cos. Opposite genes land far apart; this
                      is the 2D picture of the vector space (embed stage).

Both are t-SNE layouts of the top-90 neighbour distances (sklearn, precomputed sparse metric, the same PCA-based
start, a fixed seed). Modules are Louvain communities (networkx) of the kNN graph that links each gene to its 15
strongest partners by |cos| >= 0.3 whose relation has the same sign in both halves of the compounds ("both halves",
fdr <= 0.10) or is very strong in one half (|cos| >= 0.5) (weight |cos|, sign kept). Inside a module, each gene's
side of the module's main direction gives its arm; a module has a real "-" arm only when >= 5 genes sit on that side
AND the two sides anti-correlate (mean cosine between them <= -0.2): then the + arm and the - arm move opposite to
each other under the same drugs. Otherwise every member is "+" (a single-armed module). Modules larger than 300 genes or
looser than a mean member |cosine| of 0.3 are split again by Louvain on their own subgraph (up to 4 levels): at full
scale the first pass returns programme-sized communities of 1,000+ loosely related genes. modules.parquet records the
mean cosine within each arm and between the arms. Module scores per (drug-dose, line) = mean z of the + arm minus
mean z of the - arm (the + arm alone in single-armed modules), from tensor DDL_z; pooled scores likewise from atlas
DD_z. A module's responsive lines are those with the largest mean |score| over its 8 strongest drug-doses. Its drug
lists (drugs_up / drugs_down) are the 8 strongest pooled module z, flagged drug-doses included in their ranked
place: a drug-dose with an artifact flag (common.has_artifact on its flags of record, tables.dd_flags_of_record, so
'like a neighbouring well' counts) reads '... (+4.2) (⚠ toxic; transcription drop)' (its flags of record), and any of
the 8 strongest without an alert that falls beyond the first 8 is listed too.

Module covariates (graph version 6). A module whose pooled score rises and falls with a technical measure of the
wells, or with the cell-cycle shift, may be partly that measure. For each module and each covariate of
tables/drugdoses.parquet - UMI per cell, genes per cell, cells per well (cell loss), the composition shift (technical),
the S-phase shift, the G2/M shift (cell cycle) - modules.parquet gives cov_<k>_r (Pearson) and cov_<k>_rho
(Spearman) over the trusted drug-doses (not 'unreliable plate only', 'position not correctable' or 'wells disagree').
covariate_tag lists 'moves with <covariate> across drug-doses (r .., rank r ..)' for each covariate with
min(|r|, |rank r|) >= 0.3 ('' when none); covariate_kinds says 'technical', 'cell cycle' or both. A note, not an
alert: a cell-cycle module is expected to move with the cell-cycle shift. info.json covariate_null_max_r: per
covariate, the 99% quantile over 200 shuffles of the largest |r| over the modules (about 0.12-0.16 on the real
data), so 0.3 is well above chance.

Partner preservation (graph version 6). info.json partner_preservation: for each layout (x,y; xs,ys; xm,ym; xsm,ysm),
the share of the genes' 15 strongest relation partners (both on the map) that are among the gene's 50 nearest genes
on that layout, and chance = 50 / (genes - 1). On the real data 0.358 (nodal), 0.357 (signed), 0.314 (nodal spread)
and 0.310 (signed spread), against 0.0033 by chance: a flat map keeps about a third of each gene's closest partners
nearby, far more than chance but far from all. Read the partner lists (relations), not the distance on the map.

graph/modules.gmt: one gene set per module arm ('module <m> +', 'module <m> -'), members ordered by |projection|.

Spread layouts (xm, ym on the nodal map; xsm, ysm on the signed map). t-SNE keeps each gene's near neighbours but
packs the groups against each other, so on the 2D maps the modules look mushed. The spread layouts keep each group's
own t-SNE arrangement and move the groups apart as blocks:
  groups     nodal map: the modules; signed map: the arms of the modules (a two-armed module is two groups there,
             because its arms sit apart on the signed map)
  anchors    from how far apart the groups are in the full vector space (embed gene vectors, k dimensions): a group's
             direction is its main axis (first right singular vector of its unit gene vectors; nodal) or its mean
             unit vector (signed); distance 1 - |cos| (nodal) or 1 - cos (signed) between the directions; 2D positions
             by classical MDS refined by SMACOF (stress majorisation)
  blocks     each group becomes one compact block: its islands on the t-SNE map (members within SPREAD_LINK x the
             map's median neighbour distance of each other, single linkage) keep their own arrangement and are
             packed together (a lone far-away member is an island of one); the block's disc covers its members
  packing    the anchors are scaled so that neighbouring discs about touch; overlapping discs are pushed apart (gap
             SPREAD_GAP x the median radius), then the whole set is drawn toward its centre in small steps, each
             followed by the collision pass, until the discs cover SPREAD_FILL of their bounding circle (so the empty
             space between far-apart groups goes, while neighbours stay neighbours)
  the rest   a gene without a module moves rigidly with one group: of the groups of its SPREAD_NEAR nearest grouped
             genes on the t-SNE map, the one it is most similar to in the vector space (summed |cos| on the nodal
             map, summed positive cos on the signed map, to those neighbours of that group); it keeps its offset
             from the nearest of them, so it stays where it was relative to them (moves are never averaged across
             groups, whose blocks move in different directions)
Deterministic (no random draws). info.json "spread" records, per map, how mixed the groups are: the share of the 5
nearest grouped genes of every grouped gene that belong to another group, on the t-SNE layout and on the spread one
(mixing_tsne, mixing_spread); and, for the genes without a group, their mean |cos| (nodal) or cos (signed) to their 5
nearest grouped genes on each layout (free_sim_tsne, free_sim_spread: how alike the genes they are drawn next to are).

modules.parquet top_plus / top_minus: the arm's members by |projection| on the module's main direction, cut at 15
with the cap rule (capped: the 15 strongest, and any of the 15 strongest without an alert beyond them); a gene in the
vector space only through drug-doses that carry an alert (embed genes.parquet evidence_flagged_only) is written
'SYMBOL ⚠' in its ranked place.
"""

import os
import time
import warnings

import numpy as np
import pandas as pd

from .common import folder, has_artifact, log, read_effects_index, replace_file, save_npy, stable_seed, \
    stamp_stage, write_json, write_parquet

VERSION = 6                # 4: spread layouts (xm, ym, xsm, ysm); flagged drug-doses marked in the module drug lists
#                            5: genes without a module move with one group; top_plus / top_minus marked and capped
#                            6: the drug lists read the flags of record (common.has_artifact); module covariates
#                               (cov_<k>_r / _rho, covariate_kinds, covariate_tag); info.json partner_preservation;
#                               graph/modules.gmt
K_EDGES = 15
K_LAYOUT = 90
MIN_MODULE = 5
MIN_EDGE = 0.3
ONE_HALF_EDGE = 0.5      # a "one half" relation joins the graph only when this strong
ARMS_OPPOSITE = -0.2     # mean cosine between the two sides at or below this: two real, opposite arms
MAX_MODULE = 300         # larger modules are split again (Louvain on their own subgraph) ...
LOOSE_COS = 0.3          # ... and so are modules whose members' mean |cosine| is below this
SPLIT_DEPTH = 4
N_MOD_DRUGS = 8          # drugs_up / drugs_down: the strongest pooled module z (plus unflagged ones beyond them)
SPREAD_LINK = 3.0        # a group's islands: members within this x the map's median neighbour distance, linked
SPREAD_GAP = 0.3         # gap between two group discs, x the median disc radius
SPREAD_FILL = 0.4        # groups packed until their discs cover this share of their bounding circle
SPREAD_FILL_ISLANDS = 0.6  # the same for the islands of one group
SPREAD_NEAR = 5          # a gene without a module moves with one group, chosen among this many nearest module genes
ALERT = "⚠"
UNTRUSTED = ("unreliable plate only", "position not correctable", "wells disagree")    # as embed.UNTRUSTED
# module covariates (module docstring): key, tables/drugdoses.parquet column, words, kind
COVARIATES = (("umi_per_cell", "umi_per_cell_log2_vs_plate", "UMI per cell", "technical"),
              ("genes_per_cell", "genes_per_cell_log2_vs_plate", "genes per cell", "technical"),
              ("cells", "cells_log2_vs_plate", "cells per well (cell loss)", "technical"),
              ("composition", "composition_shift_log2", "the composition shift", "technical"),
              ("S_phase", "S_PHASE_lfc", "the S-phase shift", "cell cycle"),
              ("G2M_phase", "G2M_PHASE_lfc", "the G2/M shift", "cell cycle"))
COV_MIN = 0.3            # a module is tagged when min(|r|, |rank r|) >= this for a covariate
COV_PERM = 200           # shuffles of the permutation null (info.json covariate_null_max_r)
COV_NULL_Q = 0.99        # ... its reported quantile of the largest |r| over the modules
COV_TEXT = "moves with {name} across drug-doses (r {r:+.2f}, rank r {rho:+.2f})"
PRESERVE_TOP = 15        # partner preservation: each gene's 15 strongest partners ...
PRESERVE_K = 50          # ... found among its 50 nearest genes on a 2-D layout
LAYOUTS = (("x", "y"), ("xs", "ys"), ("xm", "ym"), ("xsm", "ysm"))

# the words of the columns this stage adds (graph version 6); the explorer and the docs show them
COLUMN_DOCS = {"graph/modules.parquet": {
    **{f"cov_{k}_r": f"Pearson r between the module's pooled score and {w} ({c}) over the trusted drug-doses"
       for k, c, w, _ in COVARIATES},
    **{f"cov_{k}_rho": f"Spearman (rank) r between the module's pooled score and {w} over the trusted drug-doses"
       for k, _, w, _ in COVARIATES},
    "covariate_kinds": "'technical', 'cell cycle' or 'technical and cell cycle': the kinds of covariate in the tag",
    "covariate_tag": f"'moves with <covariate> across drug-doses (r .., rank r ..)' for each covariate with "
                     f"min(|r|, |rank r|) >= {COV_MIN:g}, '; '-joined; a note, not an alert; '' none"}}
FILE_DOCS = {"graph/modules.gmt": "one gene set per module arm ('module <m> +' / 'module <m> -'), members by "
                                  "|projection|"}


def _layout(n, rows, cols, dist, init, seed):
    from scipy.sparse import csr_matrix
    from sklearn.manifold import TSNE
    D = csr_matrix((np.maximum(dist, 1e-6), (rows, cols)), shape=(n, n))
    k = int(D.getnnz(axis=1).min())
    perp = float(max(2.0, min(30.0, (k - 2) / 3.0)))      # t-SNE reads int(3 * perplexity + 1) neighbours
    kw = dict(n_components=2, metric="precomputed", init=init, random_state=seed, perplexity=perp,
              learning_rate="auto")
    try:
        ts = TSNE(max_iter=1000, **kw)
    except TypeError:                                    # scikit-learn < 1.5
        ts = TSNE(n_iter=1000, **kw)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        Y = ts.fit_transform(D)
    return Y.astype(np.float32)


def _within_abs_cos(U, c, block=2048):
    """Mean off-diagonal |cos| among the members: relatedness as the nodal map sees it (two opposite arms of one
    module are tightly related although their signed cosine is negative)."""
    n = len(c)
    if n < 2:
        return float("nan")
    M = U[c]
    tot = 0.0
    for r0 in range(0, n, block):
        tot += float(np.abs(M[r0:r0 + block] @ M.T).sum())
    return (tot - n) / (n * (n - 1))


def _refine(G, U, comms, seed):
    """Louvain on a whole-genome kNN graph returns a few programme-sized communities of 1,000+ genes whose members
    are only loosely alike. Split, by Louvain on the module's own subgraph, every module larger than MAX_MODULE
    genes or looser than LOOSE_COS (mean |cosine| among members, so opposite arms count as related), up to
    SPLIT_DEPTH times; members left in pieces
    smaller than MIN_MODULE become unassigned (module 0)."""
    import networkx as nx
    out, n_split = [], 0
    stack = [(c, 0) for c in comms]
    while stack:
        c, depth = stack.pop()
        loose = len(c) > MAX_MODULE or (len(c) > 2 * MIN_MODULE and _within_abs_cos(U, c) < LOOSE_COS)
        if not loose or depth >= SPLIT_DEPTH:
            out.append(c)
            continue
        parts = nx.community.louvain_communities(G.subgraph(c), weight="weight", resolution=1.0, seed=seed + depth)
        parts = [sorted(p) for p in parts]
        if len(parts) <= 1:
            out.append(c)
            continue
        n_split += 1
        stack.extend((p, depth + 1) for p in parts)
    return out, n_split


def _knn(U, k, signed, block=2048):
    n = U.shape[0]
    k = min(k, n - 1)
    rows, cols, dist = [], [], []
    for r0 in range(0, n, block):
        r1 = min(n, r0 + block)
        C = U[r0:r1] @ U.T
        C[np.arange(r1 - r0), np.arange(r0, r1)] = -np.inf if signed else 0.0
        S = C if signed else np.abs(C)
        part = np.argpartition(-S, k - 1, axis=1)[:, :k]
        sv = np.take_along_axis(S, part, axis=1)
        rows.append(np.repeat(np.arange(r0, r1), k))
        cols.append(part.ravel())
        dist.append((1.0 - sv).ravel())
    return np.concatenate(rows), np.concatenate(cols), np.concatenate(dist).astype(np.float64)


def capped(order, alert, k):
    """The first k of `order` (indices, strongest first), plus any of the first k without an alert that fall beyond
    them, in their ranked order: flagged items keep their place, and they never push an unflagged one out of view."""
    order = list(order)
    keep = set(order[:k]) | set([i for i in order if not alert[i]][:k])
    return [i for i in order if i in keep]


def _mds2(Dm, iters=300):
    """2D points whose distances fit the dissimilarities Dm: classical MDS, refined by SMACOF (stress majorisation:
    the Guttman transform, unweighted). Deterministic: the eigenvector signs are fixed (largest entry positive)."""
    from scipy.linalg import eigh
    n = len(Dm)
    if n == 1:
        return np.zeros((1, 2))
    if n == 2:
        return np.array([[0.0, 0.0], [float(Dm[0, 1]), 0.0]])
    J = np.eye(n) - 1.0 / n
    B = -0.5 * J @ (Dm ** 2) @ J
    w, V = eigh(B, subset_by_index=[n - 2, n - 1])
    X = V[:, ::-1] * np.sqrt(np.maximum(w[::-1], 0.0))
    for c in range(2):
        if X[np.argmax(np.abs(X[:, c])), c] < 0:
            X[:, c] = -X[:, c]
    t = np.arange(n, dtype=np.float64)                    # coincident points: a tiny fixed offset parts them
    X = X + 1e-6 * max(float(Dm.max()), 1e-9) * np.column_stack([np.cos(t), np.sin(t)])
    for _ in range(iters):
        d = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
        with np.errstate(divide="ignore", invalid="ignore"):
            Bm = np.where(d > 1e-12, -Dm / d, 0.0)
        np.fill_diagonal(Bm, 0.0)
        np.fill_diagonal(Bm, -Bm.sum(axis=1))
        Xn = Bm @ X / n
        done = np.abs(Xn - X).max() <= 1e-7 * max(float(np.abs(Xn).max()), 1e-12)
        X = Xn
        if done:
            break
    return X


def _collide(P, R, gap, iters=3000):
    """Push discs (centres P, radii R) apart until no two overlap (closer than R_a + R_b + gap); the larger disc of a
    pair moves less (shares by the other's area). Deterministic."""
    from scipy.spatial import cKDTree
    P = np.array(P, dtype=np.float64)
    w = R.astype(np.float64) ** 2
    reach = 2.0 * float(R.max()) + gap
    tol = 1e-3 * max(gap, 1e-12)
    for _ in range(iters):
        pr = cKDTree(P).query_pairs(reach, output_type="ndarray")
        if not len(pr):
            break
        a, b = pr[:, 0], pr[:, 1]
        dv = P[b] - P[a]
        d = np.hypot(dv[:, 0], dv[:, 1])
        ov = R[a] + R[b] + gap - d
        m = ov > tol
        if not m.any():
            break
        a, b, dv, d, ov = a[m], b[m], dv[m], d[m], ov[m]
        z = d < 1e-12
        if z.any():                                       # the same point: a fixed direction per pair
            ang = (a[z] * 7 + b[z] * 3).astype(np.float64)
            dv[z] = np.column_stack([np.cos(ang), np.sin(ang)])
            d[z] = 1.0
        u = dv / d[:, None]
        fa = w[b] / (w[a] + w[b])
        mv = np.zeros_like(P)
        np.add.at(mv, a, -u * (ov * fa)[:, None])
        np.add.at(mv, b, u * (ov * (1.0 - fa))[:, None])
        P += 0.5 * mv
    return P


def _mixing(xy, t_of, k=5):
    """Share of the k nearest grouped genes (on this layout) of every grouped gene that belong to another group."""
    from scipy.spatial import cKDTree
    g = t_of >= 0
    if g.sum() <= k or len(np.unique(t_of[g])) < 2:
        return 0.0
    _, j = cKDTree(xy[g]).query(xy[g], k=k + 1)
    return float((t_of[g][j[:, 1:]] != t_of[g][:, None]).mean())


def _pack(P, R, gap, fill):
    """Discs (centres P, radii R) packed: overlaps pushed apart (_collide), then the whole set drawn toward its
    area-weighted centre in small steps, each followed by a collision pass, until the discs cover `fill` of their
    bounding circle or stop getting closer. Neighbours stay neighbours; empty space between far-apart discs goes."""
    P = _collide(P, R, gap)
    w = R.astype(np.float64) ** 2
    area = float(np.pi * w.sum())

    def bound(Q):
        c = (Q * w[:, None]).sum(axis=0) / w.sum()
        return c, float((np.hypot(Q[:, 0] - c[0], Q[:, 1] - c[1]) + R).max())
    for _ in range(400):
        c, b = bound(P)
        if area >= fill * np.pi * b * b:
            break
        Q = _collide(c + (P - c) * 0.95, R, gap, iters=80)
        if bound(Q)[1] > 0.995 * b:
            break
        P = Q
    return _collide(P, R, gap)


def _block(p, spacing):
    """A group's members as one compact block: its islands on the t-SNE map (members within SPREAD_LINK x the map's
    typical neighbour spacing of each other, single linkage) keep their own arrangement and are packed together
    (_pack). Returns the members' offsets from the block's centre and the block's radius."""
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components
    from scipy.spatial import cKDTree
    m = len(p)
    pr = cKDTree(p).query_pairs(SPREAD_LINK * spacing, output_type="ndarray") if m > 1 else np.zeros((0, 2), int)
    nc, lab = connected_components(coo_matrix((np.ones(len(pr)), (pr[:, 0], pr[:, 1])), shape=(m, m)),
                                   directed=False)
    cen = np.array([p[lab == t].mean(axis=0) for t in range(nc)])
    if nc > 1:
        rad = np.array([max(float(np.hypot(*(p[lab == t] - cen[t]).T).max()), 0.5 * spacing) for t in range(nc)])
        size = np.bincount(lab, minlength=nc).astype(np.float64)
        c0 = (cen * size[:, None]).sum(axis=0) / size.sum()
        P = _pack(cen - c0, rad, 0.5 * spacing, SPREAD_FILL_ISLANDS)
        off = p - cen[lab] + P[lab]
    else:
        off = p - cen[0]
    off = off - np.median(off, axis=0)
    return off, float(np.hypot(off[:, 0], off[:, 1]).max()) + 0.5 * spacing


def _free_sim(xy, unit, vecs, signed, k=5):
    """Mean |cos| (signed: cos) of every gene without a group to its k nearest grouped genes on this layout; None
    without vectors or without such genes."""
    from scipy.spatial import cKDTree
    g, f = unit >= 0, unit < 0
    if vecs is None or not f.any() or g.sum() < k:
        return None
    _, j = cKDTree(xy[g]).query(xy[f], k=k)
    c = np.einsum("fk,fjk->fj", vecs[f], vecs[g][j.reshape(int(f.sum()), -1)])
    return round(float((c if signed else np.abs(c)).mean()), 4)


def spread_layout(xy, unit, dirs, signed, vecs=None):
    """The spread layout of one map (module docstring, 'Spread layouts'). xy: the t-SNE layout (genes x 2); unit:
    group per gene, 0..G-1, -1 = no group; dirs: G x k unit directions of the groups in the vector space; signed:
    distance 1 - cos (else 1 - |cos|); vecs: the genes' unit vectors (genes x k), which choose the group a gene
    without a group moves with (None: the group of its nearest grouped gene). Returns (genes x 2 float32, stats)."""
    from scipy.spatial import cKDTree
    xy = np.asarray(xy, dtype=np.float64)
    out = xy.copy()
    G = len(dirs)
    grouped = unit >= 0
    if G < 2 or not grouped.any():
        return out.astype(np.float32), {"groups": int(G), "mixing_tsne": 0.0, "mixing_spread": 0.0}
    spacing = float(np.median(cKDTree(xy).query(xy, k=2)[0][:, 1])) if len(xy) > 1 else 1.0
    spacing = spacing if spacing > 0 else 1e-3
    R, off = np.full(G, 0.5 * spacing), np.zeros_like(xy)
    for t in range(G):
        m = np.flatnonzero(unit == t)
        if len(m):
            off[m], R[t] = _block(xy[m], spacing)
    C = np.clip(dirs @ dirs.T, -1.0, 1.0)
    Dm = (1.0 - C) if signed else (1.0 - np.abs(C))
    Dm = np.clip((Dm + Dm.T) / 2.0, 0.0, 2.0)
    np.fill_diagonal(Dm, 0.0)
    Aa = _mds2(Dm)
    gap = SPREAD_GAP * float(np.median(R))
    dA = np.sqrt(((Aa[:, None, :] - Aa[None, :, :]) ** 2).sum(-1))
    np.fill_diagonal(dA, np.inf)
    nn = np.argmin(dA, axis=1)
    dnn = dA[np.arange(G), nn]
    ok = np.isfinite(dnn) & (dnn > 1e-9)
    s = float(np.median((R + R[nn] + gap)[ok] / dnn[ok])) if ok.any() else 1.0
    P = _pack(Aa * s, R, gap, SPREAD_FILL)
    out[grouped] = P[unit[grouped]] + off[grouped]
    free = ~grouped
    if free.any():                                        # a gene without a group moves rigidly with one group
        gi, fi = np.flatnonzero(grouped), np.flatnonzero(free)
        kk = int(min(SPREAD_NEAR, gi.size))
        _, j = cKDTree(xy[gi]).query(xy[fi], k=kk)
        j = j.reshape(fi.size, -1)                         # nearest first
        anchor = j[:, 0]
        if vecs is not None and kk > 1:
            sim = np.einsum("fk,fjk->fj", vecs[fi], vecs[gi][j])
            sim = np.clip(sim, 0.0, None) if signed else np.abs(sim)
            tj = unit[gi][j]                                # the neighbours' groups
            score = (sim[:, :, None] * (tj[:, :, None] == tj[:, None, :])).sum(axis=1)   # summed sim of its group
            best = tj[np.arange(fi.size), np.argmax(score, axis=1)]
            anchor = j[np.arange(fi.size), np.argmax(tj == best[:, None], axis=1)]       # nearest of that group
        out[fi] = xy[fi] + (out[gi][anchor] - xy[gi][anchor])
    return out.astype(np.float32), {"groups": int(G), "mixing_tsne": round(_mixing(xy, unit), 4),
                                    "mixing_spread": round(_mixing(out, unit), 4),
                                    "free_genes": int(free.sum()), "free_sim_tsne": _free_sim(xy, unit, vecs, signed),
                                    "free_sim_spread": _free_sim(out, unit, vecs, signed)}


# ----------------------------------------------------------------------------- module covariates
def _pearson(a, b):
    """Pearson r over the entries where both are finite (NaN with < 3 such entries or no spread)."""
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 3:
        return float("nan")
    x, y = a[ok] - a[ok].mean(), b[ok] - b[ok].mean()
    d = np.sqrt((x @ x) * (y @ y))
    return float(x @ y / d) if d > 0 else float("nan")


def _spearman(a, b):
    from scipy.stats import rankdata
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 3:
        return float("nan")
    return _pearson(rankdata(a[ok]), rankdata(b[ok]))


def module_covariates(pooled, cov, trusted, seed=None, n_perm=COV_PERM):
    """Per module: Pearson r and Spearman rho of its pooled score (pooled: modules x drug-doses) with each covariate
    of COVARIATES (cov: {key: values per drug-dose}) over the trusted drug-doses; covariate_kinds and covariate_tag
    (COV_TEXT for each covariate with min(|r|, |rho|) >= COV_MIN, '; '-joined; '' when none). Also the permutation
    null: per covariate, the COV_NULL_Q quantile over n_perm shuffles of the covariate (among the trusted drug-doses
    with a value) of the largest |r| over the modules. Returns (DataFrame, {key: null max |r|})."""
    pooled = np.asarray(pooled, dtype=np.float64)
    nm = pooled.shape[0]
    tr = np.asarray(trusted, dtype=bool)
    cols, null = {}, {}
    rng = np.random.default_rng(stable_seed("module covariates") if seed is None else seed)
    tags = [[] for _ in range(nm)]
    kinds = [[] for _ in range(nm)]
    for key, _col, name, kind in COVARIATES:
        x = np.asarray(cov.get(key, np.full(pooled.shape[1], np.nan)), dtype=np.float64)
        sel = tr & np.isfinite(x)
        r = np.array([_pearson(pooled[m, sel], x[sel]) for m in range(nm)])
        rho = np.array([_spearman(pooled[m, sel], x[sel]) for m in range(nm)])
        cols[f"cov_{key}_r"] = r.astype(np.float32)
        cols[f"cov_{key}_rho"] = rho.astype(np.float32)
        hit = np.minimum(np.abs(np.nan_to_num(r)), np.abs(np.nan_to_num(rho))) >= COV_MIN
        for m in np.flatnonzero(hit):
            tags[m].append(COV_TEXT.format(name=name, r=r[m], rho=rho[m]))
            if kind not in kinds[m]:
                kinds[m].append(kind)
        if sel.sum() >= 3 and nm and n_perm:              # the null: shuffle the covariate, keep the modules
            Z = pooled[:, sel]
            Z = Z - np.nanmean(Z, axis=1, keepdims=True)
            Z = np.nan_to_num(Z)
            zn = np.sqrt((Z ** 2).sum(axis=1))
            xs = x[sel] - x[sel].mean()
            xn = float(np.sqrt(xs @ xs))
            mx = []
            for _ in range(n_perm):
                xp = rng.permutation(xs)
                with np.errstate(invalid="ignore", divide="ignore"):
                    rr = (Z @ xp) / np.maximum(zn * xn, 1e-12)
                mx.append(float(np.abs(rr).max()))
            null[key] = round(float(np.quantile(mx, COV_NULL_Q)), 4)
        else:
            null[key] = None
    order = {"technical": 0, "cell cycle": 1}
    df = pd.DataFrame(cols)
    df["covariate_kinds"] = [" and ".join(sorted(k_, key=order.get)) for k_ in kinds]
    df["covariate_tag"] = ["; ".join(t) for t in tags]
    return df, null


# ----------------------------------------------------------------------------- partner preservation
def partner_preservation(nodes, rel, top=PRESERVE_TOP, k=PRESERVE_K):
    """For each layout of LAYOUTS: the share of the genes' top-`top` relation partners (rank <= top; both genes on
    the map) that are among the gene's k nearest genes on that 2-D layout, over all such (gene, partner) rows; chance
    = k / (genes - 1). How faithfully a flat map keeps the vector space's near neighbours."""
    from scipy.spatial import cKDTree
    cols = nodes["col"].to_numpy(np.int64)
    pos = pd.Series(np.arange(len(cols)), index=cols)
    r = rel[rel["rank"] <= top]
    r = r[r["col_a"].isin(pos.index) & r["col_b"].isin(pos.index)]
    a = pos.reindex(r["col_a"]).to_numpy(np.int64)
    b = pos.reindex(r["col_b"]).to_numpy(np.int64)
    n = len(cols)
    kk = int(min(k, n - 1))
    res = {"top": int(top), "k": kk, "genes": int(n), "rows": int(len(a)),
           "chance": round(kk / max(n - 1, 1), 4), "layouts": {}}
    for xc, yc in LAYOUTS:
        if xc not in nodes or yc not in nodes or not len(a) or kk < 1:
            continue
        P = nodes[[xc, yc]].to_numpy(np.float64)
        _, nn = cKDTree(P).query(P, k=kk + 1)
        nn = nn[:, 1:]                                    # the gene itself first (distinct positions)
        key_nn = np.sort((np.arange(n)[:, None] * n + nn).ravel())
        hit = np.isin(a * n + b, key_nn, assume_unique=False)
        res["layouts"][f"{xc},{yc}"] = round(float(hit.mean()), 4)
    return res


def write_gmt(path, rows):
    """graph/modules.gmt: one gene set per module arm ('module <m> +' / 'module <m> -'), its member symbols; rows:
    (name, description, symbols)."""
    text = "".join("\t".join([nm, desc] + list(g)) + "\n" for nm, desc, g in rows if len(g))
    tmp = path + ".part"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    replace_file(tmp, path)


def run(out, k_edges=K_EDGES, resolution=1.0):
    import networkx as nx
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    gd = folder(out, "graph")
    ed = os.path.join(out, "embed")
    inc = np.load(os.path.join(ed, "included_cols.npy"))
    U = np.load(os.path.join(ed, "gene_unit.npy"))[inc].astype(np.float32)
    eg = pd.read_parquet(os.path.join(ed, "genes.parquet"))
    sym = eg["symbol"].astype(str).to_numpy()
    fo_all = eg["evidence_flagged_only"].fillna(False).astype(bool).to_numpy() if "evidence_flagged_only" in eg \
        else np.zeros(len(eg), dtype=bool)
    n = len(inc)
    fo = fo_all[inc]                                      # per map gene: in the space only through flagged drug-doses
    glab = np.array([s_ + (f" {ALERT}" if f_ else "") for s_, f_ in zip(sym[inc], fo)], dtype=object)
    pos = {c: i for i, c in enumerate(inc)}
    rel = pd.read_parquet(os.path.join(out, "relations", "gene_relations.parquet"),
                          columns=["col_a", "col_b", "rank", "cos", "abs_cos", "evidence"])
    log(f"Graph: {n:,} genes")

    # kNN graph for communities: each gene's strongest partners that are not 'not reproduced'
    e = rel[(rel["abs_cos"] >= MIN_EDGE) & ((rel["evidence"] == "both halves") |
                                            ((rel["evidence"] == "one half") & (rel["abs_cos"] >= ONE_HALF_EDGE)))]
    e = e.sort_values(["col_a", "abs_cos"], ascending=[True, False]).groupby("col_a").head(k_edges)
    a = e["col_a"].map(pos).to_numpy()
    b = e["col_b"].map(pos).to_numpy()
    lo, hi = np.minimum(a, b), np.maximum(a, b)
    edges = pd.DataFrame({"i": lo, "j": hi, "cos": e["cos"].to_numpy()}).drop_duplicates(["i", "j"])
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_weighted_edges_from(zip(edges["i"], edges["j"], np.abs(edges["cos"])))
    seed_l = stable_seed("louvain") % (2 ** 31)
    comms = nx.community.louvain_communities(G, weight="weight", resolution=resolution, seed=seed_l)
    comms, n_split = _refine(G, U, [sorted(c) for c in comms], seed_l)
    comms = sorted([c for c in comms if len(c) >= MIN_MODULE], key=lambda c: (-len(c), c[0]))
    module = np.zeros(n, dtype=np.int64)
    for m, c in enumerate(comms, 1):
        module[c] = m
    arm = np.array([""] * n, dtype=object)
    axis_proj = np.zeros(n, dtype=np.float32)
    arm_stats = {}
    mod_axis = np.zeros((len(comms), U.shape[1]), dtype=np.float64)   # each module's main direction

    def mean_cos(A, B, same):
        if len(A) < 2 if same else (len(A) == 0 or len(B) == 0):
            return float("nan")
        C = U[A] @ U[B].T
        if same:
            C = C[~np.eye(len(A), dtype=bool)]
        return float(C.mean())

    for m, c in enumerate(comms, 1):
        M = U[c]
        _, _, vt = np.linalg.svd(M, full_matrices=False)
        p = M @ vt[0]
        if (p > 0).sum() < (p < 0).sum():                 # the larger side is "+"
            p = -p
        cp = [i for i, v in zip(c, p) if v >= 0]
        cm = [i for i, v in zip(c, p) if v < 0]
        mod_axis[m - 1] = vt[0]
        between = mean_cos(cp, cm, False)
        opposite = len(cm) >= MIN_MODULE and np.isfinite(between) and between <= ARMS_OPPOSITE
        arm[c] = np.where(p >= 0, "+", "-") if opposite else "+"
        axis_proj[c] = p
        arm_stats[m] = {"mean_cos_within_plus": mean_cos(cp, cp, True), "mean_cos_within_minus": mean_cos(cm, cm, True),
                        "mean_cos_between_arms": between, "arms_opposite": bool(opposite)}
    log(f"  {len(comms)} modules of >= {MIN_MODULE} genes (Louvain on {len(edges):,} edges, {n_split} large or loose "
        f"modules split again); "
        f"{int((module == 0).sum()):,} genes unassigned")

    # layouts
    init = np.linalg.svd(U - U.mean(axis=0), full_matrices=False)[0][:, :2]
    init = (init / np.maximum(init.std(axis=0), 1e-9) * 1e-4).astype(np.float32)
    seed = stable_seed("tsne") % (2 ** 31)
    r, c_, d = _knn(U, K_LAYOUT, signed=False)
    xy = _layout(n, r, c_, d, init, seed)
    log(f"  nodal map laid out ({(time.time() - t0) / 60:.1f} min)")
    r, c_, d = _knn(U, K_LAYOUT, signed=True)
    xys = _layout(n, r, c_, d, init, seed)
    log(f"  signed map laid out ({(time.time() - t0) / 60:.1f} min)")

    # spread layouts: the groups moved apart as blocks (module docstring)
    unit_n = np.where(module > 0, module - 1, -1)
    U64 = U.astype(np.float64)
    xym, st_n = spread_layout(xy, unit_n, mod_axis, signed=False, vecs=U64)
    key = np.where(module > 0, 2 * module + (arm == "-"), -1)
    keys = np.unique(key[key >= 0])
    unit_s = np.where(key >= 0, np.searchsorted(keys, key), -1)
    sdir = np.zeros((len(keys), U.shape[1]), dtype=np.float64)
    for t in range(len(keys)):
        v = U[unit_s == t].astype(np.float64).mean(axis=0)
        sdir[t] = v / max(float(np.linalg.norm(v)), 1e-12)
    xysm, st_s = spread_layout(xys, unit_s, sdir, signed=True, vecs=U64)
    spread_info = {"nodal": st_n, "signed": st_s}
    log(f"  spread layouts: {st_n['groups']} modules on the nodal map (a module gene's 5 nearest module genes in "
        f"another module: {st_n['mixing_tsne']:.1%} on the t-SNE layout, {st_n['mixing_spread']:.1%} spread), "
        f"{st_s['groups']} module arms on the signed map ({st_s['mixing_tsne']:.1%} -> {st_s['mixing_spread']:.1%})")
    if st_n.get("free_sim_tsne") is not None and st_s.get("free_sim_tsne") is not None:
        log(f"  genes without a module, mean |cos| to their 5 nearest module genes: {st_n['free_sim_tsne']:.3f} on the "
            f"t-SNE layout, {st_n['free_sim_spread']:.3f} spread (signed map, mean cos: {st_s['free_sim_tsne']:.3f} -> "
            f"{st_s['free_sim_spread']:.3f})")

    deg = np.bincount(np.concatenate([edges["i"], edges["j"]]), minlength=n)
    nodes = pd.DataFrame({"col": inc, "symbol": sym[inc], "module": module, "arm": arm, "axis_proj": axis_proj,
                          "x": xy[:, 0], "y": xy[:, 1], "xs": xys[:, 0], "ys": xys[:, 1], "degree": deg,
                          "xm": xym[:, 0], "ym": xym[:, 1], "xsm": xysm[:, 0], "ysm": xysm[:, 1]})
    write_parquet(nodes, os.path.join(gd, "nodes.parquet"))
    write_parquet(pd.DataFrame({"col_a": inc[edges["i"].to_numpy()], "col_b": inc[edges["j"].to_numpy()],
                                "cos": edges["cos"].to_numpy(), "sign": np.sign(edges["cos"].to_numpy())}),
                  os.path.join(gd, "edges.parquet"))

    # module scores per (drug-dose, line), and the module table
    fxd = os.path.join(out, "atlas", "effects")
    ix = read_effects_index(fxd)
    dd, lines = ix["drugdose"], ix["lines"]
    DDL_z = np.load(os.path.join(out, "tensor", "DDL_z.npy"), mmap_mode="r")
    DD_z = np.load(os.path.join(fxd, "DD_z.npy"), mmap_mode="r")
    Dn, L = len(dd), len(lines)
    nm = len(comms)
    scores = np.zeros((nm, Dn, L), dtype=np.float32)
    pooled = np.zeros((nm, Dn), dtype=np.float32)
    dlabel = (dd["drug"].astype(str) + " " + dd["dose"].astype(str) + " uM").to_numpy()
    from .tables import dd_flags_of_record                # the flags of record (+ neighbouring-well, translation)
    dflags = np.asarray(dd_flags_of_record(out), dtype=object) if "flags" in dd else np.array([""] * Dn, dtype=object)
    dalert = np.array([has_artifact(f) for f in dflags], dtype=bool)

    def dlist(m, order):
        return "; ".join(f"{dlabel[i]} ({pooled[m - 1, i]:+.1f})" + (f" (⚠ {dflags[i]})" if dalert[i] else "")
                         for i in capped(order, dalert, N_MOD_DRUGS))
    cell = lines["cell_name"].fillna(lines["cell_line_id"]).astype(str).to_numpy()
    rows = []
    for m, c in enumerate(comms, 1):
        cols = inc[c]
        is_plus = arm[c] == "+"
        order = np.argsort(cols)
        Zm = np.asarray(DDL_z[cols[order]], dtype=np.float32)          # members x drug-doses x lines
        plus_o = is_plus[order]
        with np.errstate(invalid="ignore"), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sc = np.nanmean(Zm[plus_o], axis=0)
            pz = np.nanmean(np.asarray(DD_z[:, cols[is_plus]], dtype=np.float32), axis=1)
            if (~plus_o).any():                                        # + arm minus - arm
                sc = sc - np.nanmean(Zm[~plus_o], axis=0)
                pz = pz - np.nanmean(np.asarray(DD_z[:, cols[~is_plus]], dtype=np.float32), axis=1)
        scores[m - 1] = sc
        pooled[m - 1] = pz
        o = np.argsort(-np.nan_to_num(pooled[m - 1], nan=0.0))
        strongest = np.argsort(-np.abs(np.nan_to_num(pooled[m - 1], nan=0.0)))[:8]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            spread = np.nanmean(np.abs(scores[m - 1][strongest]), axis=0)
        ol = np.argsort(-np.nan_to_num(spread, nan=-1.0))
        plus = [cc for cc, a_ in zip(c, arm[c]) if a_ == "+"]
        minus = [cc for cc, a_ in zip(c, arm[c]) if a_ == "-"]
        plus = sorted(plus, key=lambda i: -abs(axis_proj[i]))
        minus = sorted(minus, key=lambda i: -abs(axis_proj[i]))
        rows.append({"module": m, "n_genes": len(c), "n_plus": len(plus), "n_minus": len(minus),
                     "top_plus": ", ".join(glab[capped(plus, fo, 15)]),
                     "top_minus": ", ".join(glab[capped(minus, fo, 15)]),
                     "x": float(xy[c, 0].mean()), "y": float(xy[c, 1].mean()),
                     "xs": float(xys[c, 0].mean()), "ys": float(xys[c, 1].mean()),
                     "drugs_up": dlist(m, o), "drugs_down": dlist(m, o[::-1]),
                     "responsive_lines": ", ".join(cell[ol[:8]]), **arm_stats[m]})
    mods = pd.DataFrame(rows)
    # technical and cell-cycle covariates of each module's pooled score (module docstring)
    tp = os.path.join(out, "tables", "drugdoses.parquet")
    cov, trusted, cov_src = {}, np.array([not any(u in f for u in UNTRUSTED) for f in dflags], dtype=bool), ""
    if os.path.exists(tp):
        tdd = pd.read_parquet(tp)
        if len(tdd) == Dn:
            cov = {k: pd.to_numeric(tdd[c], errors="coerce").to_numpy(np.float64) if c in tdd else
                   np.full(Dn, np.nan) for k, c, _, _ in COVARIATES}
            cov_src = "tables/drugdoses.parquet"
    if not cov:
        cov = {k: pd.to_numeric(dd[c], errors="coerce").to_numpy(np.float64) if c in dd else np.full(Dn, np.nan)
               for k, c, _, _ in COVARIATES}
        cov_src = "atlas/effects/drugdose.csv"
    cdf, cov_null = module_covariates(pooled, cov, trusted)
    for c in cdf.columns:
        mods[c] = cdf[c].to_numpy() if nm else []
    write_parquet(mods, os.path.join(gd, "modules.parquet"))
    save_npy(os.path.join(gd, "module_scores.npy"), scores.astype(np.float16))
    save_npy(os.path.join(gd, "module_pooled_z.npy"), pooled)
    gmt = []
    for m, c in enumerate(comms, 1):
        for a_, word in (("+", "+"), ("-", "-")):
            mem = sorted((cc for cc in c if arm[cc] == a_), key=lambda i: -abs(axis_proj[i]))
            if mem:
                gmt.append((f"module {m} {word}", f"graph module {m}, {word} arm: {len(mem)} genes (by |projection|)",
                            [str(x) for x in sym[inc[mem]]]))
    write_gmt(os.path.join(gd, "modules.gmt"), gmt)
    preserve = partner_preservation(nodes, rel)
    n_tag = int((cdf["covariate_tag"] != "").sum()) if nm else 0
    cov_counts = {k: int((np.minimum(cdf[f"cov_{k}_r"].abs().fillna(0), cdf[f"cov_{k}_rho"].abs().fillna(0))
                          >= COV_MIN).sum()) if nm else 0 for k, *_ in COVARIATES}
    log(f"  module covariates: {n_tag} of {nm} modules move with a technical or cell-cycle covariate "
        f"(min(|r|, |rank r|) >= {COV_MIN:g}: " + ", ".join(f"{k} {v}" for k, v in cov_counts.items()) + ")")
    log("  partner preservation (a gene's 15 strongest partners among its 50 nearest on the map): " +
        ", ".join(f"{k} {v:.3f}" for k, v in preserve["layouts"].items()) + f" (chance {preserve['chance']:.4f})")
    info = {"version": VERSION, "genes": int(n), "modules": nm, "unassigned": int((module == 0).sum()),
            "modules_split": int(n_split), "max_module": MAX_MODULE, "loose_cos": LOOSE_COS,
            "edges": int(len(edges)), "k_edges": k_edges, "k_layout": K_LAYOUT, "resolution": resolution,
            "min_edge": MIN_EDGE, "one_half_edge": ONE_HALF_EDGE, "min_module": MIN_MODULE,
            "arms_opposite_cos": ARMS_OPPOSITE, "split_depth": SPLIT_DEPTH, "spread": spread_info,
            "covariates": {"source": cov_src, "columns": {k: c for k, c, _, _ in COVARIATES},
                           "words": {k: w for k, _, w, _ in COVARIATES}, "kinds": {k: t for k, _, _, t in COVARIATES},
                           "trusted_drugdoses": int(trusted.sum()), "min_abs_r": COV_MIN,
                           "rule": f"tagged when min(|r|, |rank r|) >= {COV_MIN:g} between the module's pooled score "
                                   "and the covariate over the trusted drug-doses (not " +
                                   ", ".join(f"'{u}'" for u in UNTRUSTED) + "); a note, not an alert",
                           "modules_tagged": n_tag, "modules_per_covariate": cov_counts},
            "covariate_null_max_r": cov_null,
            "covariate_null_rule": f"{COV_NULL_Q:.0%} quantile, over {COV_PERM} shuffles of the covariate among the "
                                   "trusted drug-doses, of the largest |r| over the modules",
            "partner_preservation": preserve, "gmt": {"file": "modules.gmt", "sets": len(gmt)},
            "minutes": round((time.time() - t0) / 60, 2)}
    write_json(info, os.path.join(gd, "info.json"))
    stamp_stage(out, "graph", VERSION, info)
    log(f"Graph done: {nm} modules, {len(edges):,} edges ({info['minutes']} min)")
    return info
