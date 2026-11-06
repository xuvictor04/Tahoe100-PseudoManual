"""graph - the 2D nodal map of gene relatedness, its modules, and a signed map for comparison.

Two different questions give two different maps:

  nodal map (x, y)    "how closely related are these genes?"  Distance = 1 - |cos|. Genes that respond in OPPOSITE
                      directions to the same perturbations (cos near -1) are as related as genes that respond the
                      same way, so they land next to each other: the two arms of one pathway form one island.
  signed map (xs, ys) "do these genes do the same thing?"  Distance = 1 - cos. Opposite genes land far apart; this
                      is the 2D picture of the vector space (embed stage).

Both are t-SNE layouts of the top-90 neighbour distances (sklearn, precomputed sparse metric, the same PCA-based
start, a fixed seed). Modules are Louvain communities (networkx) of the kNN graph that links each gene to its 15
strongest partners by |cos| >= 0.3 whose relation is replicated ("both halves", i.e. fdr <= 0.10) or very strong in
one half of the compounds (|cos| >= 0.5) (weight |cos|, sign kept). Inside a module, each gene's side of the
module's main direction gives its arm; a module has a real "-" arm only when >= 5 genes sit on that side AND the two
sides anti-correlate (mean cosine between them <= -0.2): then the + arm and the - arm move opposite to each other
under the same drugs. Otherwise every member is "+" (a single-armed module). modules.parquet records the mean cosine
within each arm and between the arms. Module scores per (drug-dose, line) = mean z of the + arm minus mean z of the
- arm (the + arm alone in single-armed modules), from tensor DDL_z; pooled scores likewise from atlas DD_z. A
module's responsive lines are those with the largest mean |score| over its 8 strongest drug-doses.
"""

import os
import time
import warnings

import numpy as np
import pandas as pd

from .common import folder, log, read_effects_index, save_npy, stable_seed, stamp_stage, write_json, \
    write_parquet

VERSION = 2
K_EDGES = 15
K_LAYOUT = 90
MIN_MODULE = 5
MIN_EDGE = 0.3
ONE_HALF_EDGE = 0.5      # a "one half" relation joins the graph only when this strong
ARMS_OPPOSITE = -0.2     # mean cosine between the two sides at or below this: two real, opposite arms


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
    n = len(inc)
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
    comms = nx.community.louvain_communities(G, weight="weight", resolution=resolution,
                                             seed=stable_seed("louvain") % (2 ** 31))
    comms = sorted([sorted(c) for c in comms if len(c) >= MIN_MODULE], key=lambda c: (-len(c), c[0]))
    module = np.zeros(n, dtype=np.int64)
    for m, c in enumerate(comms, 1):
        module[c] = m
    arm = np.array([""] * n, dtype=object)
    axis_proj = np.zeros(n, dtype=np.float32)
    arm_stats = {}

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
        between = mean_cos(cp, cm, False)
        opposite = len(cm) >= MIN_MODULE and np.isfinite(between) and between <= ARMS_OPPOSITE
        arm[c] = np.where(p >= 0, "+", "-") if opposite else "+"
        axis_proj[c] = p
        arm_stats[m] = {"mean_cos_within_plus": mean_cos(cp, cp, True), "mean_cos_within_minus": mean_cos(cm, cm, True),
                        "mean_cos_between_arms": between, "arms_opposite": bool(opposite)}
    log(f"  {len(comms)} modules of >= {MIN_MODULE} genes (Louvain on {len(edges):,} edges); "
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

    deg = np.bincount(np.concatenate([edges["i"], edges["j"]]), minlength=n)
    nodes = pd.DataFrame({"col": inc, "symbol": sym[inc], "module": module, "arm": arm, "axis_proj": axis_proj,
                          "x": xy[:, 0], "y": xy[:, 1], "xs": xys[:, 0], "ys": xys[:, 1], "degree": deg})
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
                     "top_plus": ", ".join(sym[inc[plus[:15]]]), "top_minus": ", ".join(sym[inc[minus[:15]]]),
                     "x": float(xy[c, 0].mean()), "y": float(xy[c, 1].mean()),
                     "xs": float(xys[c, 0].mean()), "ys": float(xys[c, 1].mean()),
                     "drugs_up": "; ".join(f"{dlabel[i]} ({pooled[m - 1, i]:+.1f})" for i in o[:8]),
                     "drugs_down": "; ".join(f"{dlabel[i]} ({pooled[m - 1, i]:+.1f})" for i in o[::-1][:8]),
                     "responsive_lines": ", ".join(cell[ol[:8]]), **arm_stats[m]})
    write_parquet(pd.DataFrame(rows), os.path.join(gd, "modules.parquet"))
    save_npy(os.path.join(gd, "module_scores.npy"), scores.astype(np.float16))
    save_npy(os.path.join(gd, "module_pooled_z.npy"), pooled)
    info = {"version": VERSION, "genes": int(n), "modules": nm, "unassigned": int((module == 0).sum()),
            "edges": int(len(edges)), "k_edges": k_edges, "k_layout": K_LAYOUT, "resolution": resolution,
            "minutes": round((time.time() - t0) / 60, 2)}
    write_json(info, os.path.join(gd, "info.json"))
    stamp_stage(out, "graph", VERSION, info)
    log(f"Graph done: {nm} modules, {len(edges):,} edges ({info['minutes']} min)")
    return info
