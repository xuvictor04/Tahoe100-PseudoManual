"""Verifier v3: recompute per-group TRIM72 (and placebo-predictor) log rate ratios from the RAW per-cell files with own
code, for a random subset of fitted (well, line) groups, and stress-test them:
  rep        same cells as the step (replicates its per-file Bernoulli subsample), same model  -> compare with cache
  all        all cells of the group (no 2,000-cell cap), same model                             -> cap effect
  nocc       all cells, no cell-cycle covariates                                                 -> cell-cycle confounding
  flex       all cells, + log n_genes + quintile dummies of log total UMI                       -> depth / complexity
  trim95     all cells below the group's 95th percentile of total UMI (doublet proxy)           -> doublets
  dose       all cells, TRIM72 = 1 UMI and >= 2 UMI as separate indicators                      -> dose / ambient
Plus every NCI-H661 cell (TRIM72 not expressed: its TRIM72 reads are ambient / readthrough) with a well-fixed-effect
Poisson model: what does 'TRIM72 detected' do in a line whose TRIM72 is soup?
Own Newton solver (not the step's batched IRLS). Writes only under verify/out."""
import glob, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor
import numpy as np, pandas as pd, pyarrow.parquet as pq

D, data, outdir = sys.argv[1:4]
N_SEL = int(sys.argv[4]) if len(sys.argv) > 4 else 400
N_DROP = 100
SEED = 20261026
SCRIPT_SEED = 20261025
t0 = time.time()
info = json.load(open(f"{D}/cache/run_info.json"))
OUTS = info["params"]["outcomes"]
PLAC = info["params"]["placebo"]
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
OUTDEF = {"P53_SCORE": P53, "MDM2": ["MDM2"], "CDKN1A": ["CDKN1A"], "XPC": ["XPC"], "DDB2": ["DDB2"],
          "ATF3": ["ATF3"], "TP53": ["TP53"], "PMAIP1": ["PMAIP1"]}
genes = list(dict.fromkeys(["TRIM72"] + PLAC + sum(OUTDEF.values(), [])))
cols = ["sample", "cell_line_id", "total_counts", "n_genes", "S_PHASE", "G2M_PHASE"] + genes

g = pd.read_csv(f"{D}/tables/groups.csv.gz")
g["gid"] = np.arange(len(g))
G = pd.read_parquet(f"{D}/cache/group_stats.parquet")
assert (g.loc[G["gid"], "n_cells_used"].to_numpy() == G["n_used"].to_numpy()).all()
rng = np.random.default_rng(SEED)
fitted = g.index[g["fitted"].fillna(False).astype(bool)].to_numpy()
sel = np.sort(rng.choice(fitted, N_SEL, replace=False))
dropped = g.index[g["skip_reason"].eq("too few detected cells after sampling")].to_numpy()
seld = np.sort(rng.choice(dropped, N_DROP, replace=False))
h661 = g[(g["cell_name"] == "NCI-H661") & ~g["skip_reason"].eq("failed well")]
key_sel = {(s, c): i for s, c, i in zip(g["sample"], g["cell_line_id"], g["gid"]) if i in set(sel) | set(seld)}
h661_id = h661["cell_line_id"].iloc[0]
h661_samples = set(h661["sample"])
kp = g["sampling_prob"].to_numpy()

files = sorted(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet")))
print(f"{len(files)} files; {len(sel)} random fitted groups, {len(seld)} dropped-after-subsample groups, "
      f"{len(h661)} H661 groups", flush=True)


def read(fi):
    tb = pq.read_table(files[fi], columns=cols, read_dictionary=["sample", "cell_line_id"])
    u = np.random.default_rng([SCRIPT_SEED, fi]).random(tb.num_rows)           # the step's per-file draw
    sa = tb.column("sample").combine_chunks(); la = tb.column("cell_line_id").combine_chunks()
    sd, ld = [str(v) for v in sa.dictionary.to_pylist()], [str(v) for v in la.dictionary.to_pylist()]
    si, li = sa.indices.to_numpy(zero_copy_only=False), la.indices.to_numpy(zero_copy_only=False)
    code = si.astype(np.int64) * len(ld) + li
    uc, inv = np.unique(code, return_inverse=True)
    gmap = np.array([key_sel.get((sd[k // len(ld)], ld[k % len(ld)]), -1) for k in uc], np.int64)
    hmap = np.array([(ld[k % len(ld)] == h661_id) and (sd[k // len(ld)] in h661_samples) for k in uc], bool)
    gid, is_h = gmap[inv], hmap[inv]
    m = (gid >= 0) | is_h
    if not m.any():
        return None
    t = tb.filter(m).to_pandas()
    gid, is_h, u = gid[m], is_h[m], u[m]
    m = np.ones(len(t), bool)
    m = (gid >= 0) | is_h
    if not m.any():
        return None
    x = t.loc[m].copy()
    x["gid"] = gid[m]
    x["kept"] = np.where(gid[m] >= 0, u[m] < kp[np.maximum(gid[m], 0)], False)
    x["is_h661"] = is_h[m]
    for c_ in genes + ["S_PHASE", "G2M_PHASE"]:
        x[c_] = x[c_].astype(np.float32)
    return x


parts = []
with ThreadPoolExecutor(2) as ex:
    for i, x in enumerate(ex.map(read, range(len(files)))):
        if x is not None:
            parts.append(x)
        if i % 500 == 0:
            print(f"  read {i} files, {time.time() - t0:.0f} s", flush=True)
C = pd.concat(parts, ignore_index=True)
del parts
C["sample"] = C["sample"].astype(str); C["cell_line_id"] = C["cell_line_id"].astype(str)
print(f"cells kept: {len(C):,} ({C['is_h661'].sum():,} H661); {time.time() - t0:.0f} s", flush=True)
C.to_parquet(f"{outdir}/v3_cells.parquet", index=False)

# --------------------------------------------------------------------------- own Poisson / quasi-Poisson Newton
def qp_fit(y, X, off, j=1):
    n, p = X.shape
    b = np.zeros(p)
    b[0] = np.log(max(y.sum(), 0.5) / np.exp(off).sum())
    dev_old = np.inf
    for it in range(60):
        eta = X @ b + off
        mu = np.exp(np.clip(eta, -40, 40))
        grad = X.T @ (y - mu)
        H = (X.T * mu) @ X
        step = np.linalg.solve(H, grad)
        lam = 1.0
        while True:                                     # step halving on the Poisson log-likelihood
            bn = b + lam * step
            mun = np.exp(np.clip(X @ bn + off, -40, 40))
            dev = (mun - y * np.log(mun)).sum()
            if dev <= dev_old + 1e-9 or lam < 1e-4:
                break
            lam /= 2
        b, dev_old = bn, dev
        if np.max(np.abs(lam * step)) < 1e-10:
            break
    mu = np.exp(np.clip(X @ b + off, -40, 40))
    H = (X.T * mu) @ X
    phi = max(1.0, float(((y - mu) ** 2 / mu).sum() / max(1, n - p)))
    V = np.linalg.inv(H) * phi
    return b[j], np.sqrt(V[j, j]), b, V


def design(x, pred, variant):
    T = x["total_counts"].to_numpy(float)
    lt = np.log(T)
    cols_ = [np.ones(len(T))]
    if variant == "dose":
        cols_ += [(pred == 1).astype(float), (pred >= 2).astype(float)]
    else:
        cols_ += [(pred > 0).astype(float)]
    cols_.append(lt)
    if variant != "nocc":
        cols_ += [np.log((x["S_PHASE"].to_numpy(float) + 0.5) / T), np.log((x["G2M_PHASE"].to_numpy(float) + 0.5) / T)]
    if variant == "flex":
        cols_.append(np.log(x["n_genes"].to_numpy(float)))
        qs = np.quantile(lt, [0.2, 0.4, 0.6, 0.8])
        for q_ in qs:
            cols_.append((lt > q_).astype(float))
    return np.column_stack(cols_), lt


def yof(x, o):
    return x[OUTDEF[o]].to_numpy(float).sum(1)


rows = []
ogroups = {k: v for k, v in C[C["gid"] >= 0].groupby("gid")}
TR_OUT = list(OUTDEF)
PL_OUT = ["P53_SCORE", "ATF3"]
for n_, gid in enumerate(list(sel) + list(seld)):
    x_all = ogroups.get(gid)
    if x_all is None:
        continue
    for variant in ("rep", "all", "nocc", "flex", "trim95", "dose"):
        if variant == "rep":
            x = x_all[x_all["kept"]]
        elif variant == "trim95":
            x = x_all[x_all["total_counts"] <= np.quantile(x_all["total_counts"], 0.95)]
        else:
            x = x_all
        if gid in set(seld) and variant != "all":
            continue
        preds = ["TRIM72"] + (PLAC if variant in ("rep", "all", "nocc", "flex") else [])
        for pn in preds:
            pv = x[pn].to_numpy()
            nd = int((pv > 0).sum())
            if nd < 5 or len(pv) - nd < 5:
                continue
            X, lt = design(x, pv, variant)
            for o in (TR_OUT if pn == "TRIM72" else PL_OUT):
                y = yof(x, o)
                if y.sum() < 20:
                    continue
                try:
                    b, s, bb, V = qp_fit(y, X, lt)
                except np.linalg.LinAlgError:
                    continue
                r = dict(gid=gid, variant=variant, pred=pn, outcome=o, beta=b, se=s, n=len(y), n_det=nd,
                         y_det=float(y[pv > 0].sum()), y_tot=float(y.sum()))
                if variant == "dose":
                    r.update(beta2=bb[2], se2=np.sqrt(V[2, 2]), n_det2=int((pv >= 2).sum()))
                rows.append(r)
    if n_ % 50 == 0:
        print(f"  fitted {n_} groups, {time.time() - t0:.0f} s", flush=True)
R = pd.DataFrame(rows)
R.to_csv(f"{outdir}/v3_group_fits.csv.gz", index=False)

# --------------------------------------------------------------------------- NCI-H661: well fixed-effect Poisson
def fe_poisson(y, X, strata):
    """Poisson with one intercept per stratum (profiled out); quasi-Poisson SE. X without intercept."""
    us, si = np.unique(strata, return_inverse=True)
    ns = len(us)
    keep = np.bincount(si, y, ns)[si] > 0                           # strata with no counts carry no information
    y, X, si = y[keep], X[keep], np.unique(si[keep], return_inverse=True)[1]
    ns = si.max() + 1
    b = np.zeros(X.shape[1])
    for it in range(50):
        e = np.exp(X @ b)
        a = np.log(np.bincount(si, y, ns) / np.bincount(si, e, ns))
        mu = e * np.exp(a[si])
        grad = X.T @ (y - mu)
        smu = np.bincount(si, mu, ns)
        mx = np.column_stack([np.bincount(si, mu * X[:, k], ns) for k in range(X.shape[1])])
        H = (X.T * mu) @ X - (mx.T / smu) @ mx
        step = np.linalg.solve(H, grad)
        b = b + step
        if np.max(np.abs(step)) < 1e-10:
            break
    e = np.exp(X @ b); a = np.log(np.bincount(si, y, ns) / np.bincount(si, e, ns)); mu = e * np.exp(a[si])
    smu = np.bincount(si, mu, ns)
    mx = np.column_stack([np.bincount(si, mu * X[:, k], ns) for k in range(X.shape[1])])
    H = (X.T * mu) @ X - (mx.T / smu) @ mx
    phi = max(1.0, float(((y - mu) ** 2 / mu).sum() / max(1, len(y) - ns - X.shape[1])))
    V = np.linalg.inv(H) * phi
    return b, V


hrows = []
Hc = C[C["is_h661"]]
for label, x in (("NCI-H661 (TRIM72 not expressed)", Hc), ("random fitted groups, WT", C[(C["gid"].isin(sel))]
                 .merge(g[["gid", "tp53_group"]], on="gid").query("tp53_group == 'WT'")),
                 ("random fitted groups, altered", C[(C["gid"].isin(sel))].merge(g[["gid", "tp53_group"]], on="gid")
                  .query("tp53_group == 'altered'"))):
    T = x["total_counts"].to_numpy(float); lt = np.log(T)
    strata = (x["sample"] + "|" + x["cell_line_id"]).to_numpy()
    st_, si_ = np.unique(strata, return_inverse=True)
    def cen(v):
        return v - (np.bincount(si_, v) / np.bincount(si_))[si_]
    covs = [cen(lt), cen(np.log((x["S_PHASE"].to_numpy(float) + 0.5) / T)), cen(np.log((x["G2M_PHASE"].to_numpy(float) + 0.5) / T))]
    for pn in ["TRIM72"] + PLAC:
        pv = x[pn].to_numpy()
        nd = int((pv > 0).sum())
        if nd < 30:
            continue
        X = np.column_stack([(pv > 0).astype(float)] + covs)
        for o in TR_OUT:
            y = yof(x, o)
            if y.sum() < 50:
                continue
            b, V = fe_poisson(y, X, strata)
            hrows.append(dict(cells=label, pred=pn, outcome=o, n_cells=len(y), n_det=nd,
                              pct_det=100 * nd / len(y), pct_det_1umi=100 * np.mean(pv[pv > 0] == 1),
                              log_rr=b[0], se=np.sqrt(V[0, 0]), rr=np.exp(b[0])))
HR = pd.DataFrame(hrows)
HR.to_csv(f"{outdir}/v3_h661_fe.csv", index=False)
print(f"done fits {time.time() - t0:.0f} s; rows {len(R)}, H661 rows {len(HR)}", flush=True)
