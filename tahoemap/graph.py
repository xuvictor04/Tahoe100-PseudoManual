"""graph - the 2D nodal map of gene relatedness, its modules, and a signed map for comparison.

Two different questions give two different maps:

  nodal map (x, y)    "how closely related are these genes?"  Distance = 1 - |cos|. Genes that respond in OPPOSITE
                      directions to the same perturbations (cos near -1) are as related as genes that respond the
                      same way, so they land next to each other: the two arms of one pathway form one island.
  signed map (xs, ys) "do these genes do the same thing?"  Distance = 1 - cos. Opposite genes land far apart; this
                      is the 2D picture of the vector space (embed stage).

Both are t-SNE layouts of the top-90 neighbour distances (sklearn, precomputed sparse metric, the same PCA-based
start, a fixed seed). Modules are Louvain communities (networkx) of the kNN graph that links each gene to its 15
strongest partners by |cos| that are not marked "not reproduced" (weight |cos|, sign kept). Inside a module, each
gene's arm (+ or -) is the sign of its projection on the module's main direction: the + arm and the - arm move
opposite to each other under the same drugs. Module scores per (drug-dose, line) = mean z of the + arm minus mean z
of the - arm, from tensor DDL_z.
"""

import os
import time
import warnings

import numpy as np
import pandas as pd

from .common import folder, log, read_effects_index, save_npy, stable_seed, stamp_stage, write_json, \
    write_parquet

VERSION = 1
K_EDGES = 15
K_LAYOUT = 90
MIN_MODULE = 5
MIN_EDGE = 0.25


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
    e = rel[(rel["evidence"] != "not reproduced") & (rel["abs_cos"] >= MIN_EDGE)]
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
    for m, c in enumerate(comms, 1):
        M = U[c]
        _, _, vt = np.linalg.svd(M, full_matrices=False)
        p = M @ vt[0]
        if (p > 0).sum() < (p < 0).sum():                 # the larger arm is "+"
            p = -p
        arm[c] = np.where(p >= 0, "+", "-")
        axis_proj[c] = p
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
        sgn = np.where(arm[c] == "+", 1.0, -1.0).astype(np.float32)
        Zm = np.asarray(DDL_z[np.sort(cols)], dtype=np.float32)
        order = np.argsort(cols)
        sg = sgn[order]
        with np.errstate(invalid="ignore"):
            num = np.nansum(Zm * sg[:, None, None], axis=0)
            den = np.isfinite(Zm).sum(axis=0)
        scores[m - 1] = np.where(den > 0, num / np.maximum(den, 1), np.nan)
        pz = np.asarray(DD_z[:, cols], dtype=np.float32) * sgn[None, :]
        pooled[m - 1] = np.nanmean(pz, axis=1)
        o = np.argsort(-np.nan_to_num(pooled[m - 1], nan=0.0))
        spread = np.nanmedian(np.abs(scores[m - 1]), axis=0)
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
                     "responsive_lines": ", ".join(cell[ol[:8]])})
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
