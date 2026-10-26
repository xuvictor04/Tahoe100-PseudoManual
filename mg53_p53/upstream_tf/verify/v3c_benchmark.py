"""Verifier v3: within-line (two-way FE) TF vs TRIM72 with own code (alternating projections, FWL), own drug-cluster
and line-cluster SE; calibration by drug-row permutation of the residual TRIM72; TP53 positive control within lines;
WT-minus-altered slopes; disattenuation by the two_way TRIM72 reliability. Reads the step's pass cache (read-only)."""
import os, sys
import numpy as np, pandas as pd
from scipy import stats

DATA = sys.argv[1] if len(sys.argv) > 1 else "/home/user/tahoe_data"
STEP = "/home/user/Tahoe100-PseudoManual/mg53_p53/upstream_tf"
OUT = os.path.join(STEP, "verify", "out_v3"); os.makedirs(OUT, exist_ok=True)
FXD = os.path.join(DATA, "atlas", "effects")
P = np.load(os.path.join(STEP, "cache", "pass_73b0ba7f7c76.npz"))
tfs = [str(s) for s in P["tfs"]]; sel = [str(s) for s in P["sel"]]
wells = pd.read_csv(os.path.join(FXD, "wells.csv"))
dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
lines = pd.read_csv(os.path.join(FXD, "lines.csv"), dtype=str)
lid = lines.iloc[:, 0].astype(str).tolist()
keep = ~(dd.unreliable_plate_only.astype(bool) | dd.position_not_correctable.astype(bool)).to_numpy()
ND, L = len(dd), len(lid)
used = wells.used_in_drugdose.astype(bool).to_numpy() & (wells.drugdose_row.to_numpy() >= 0)
selw = P["selw"].astype(np.float64)

def ddmean(V):
    out = np.full((ND,) + V.shape[1:], np.nan)
    for d in range(ND):
        ii = np.flatnonzero(used & (wells.drugdose_row.to_numpy() == d))
        if len(ii):
            with np.errstate(all="ignore"):
                import warnings; warnings.simplefilter("ignore")
                out[d] = np.nanmean(V[ii], axis=0)
    return out
Ysel = ddmean(selw)
trim = Ysel[:, :, sel.index("TRIM72")]
bg = ddmean(P["bgw"].astype(np.float64))
TF = P["tf_dd"]                                  # dd x lines x T (float32)
bl = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "baseline_by_cell_line.csv"), dtype={"cell_line_id": str}).set_index("cell_line_id")
wt = (bl["tp53_group"].reindex(lid) == "WT").to_numpy()
print("WT lines", wt.sum(), "altered", (~wt).sum())
beta = np.load(os.path.join(FXD, "DD_beta.npy")).astype(float); beta[np.isnan(beta).all(axis=1)] = 0
Aab = np.load(os.path.join(FXD, "DD_A.npy")).astype(float)
mods = np.load(os.path.join(FXD, "DD_r2_modules.npy")).astype(float)
covs = [beta, Aab, mods[:, :, 0], mods[:, :, 1], bg]
drug_of = pd.factorize(dd.drug)[0]

def fe_resid(V, d, l, n_iter=200, tol=1e-10):
    """alternating projections off dd and line means (V: n x k)"""
    from scipy import sparse
    V = V.copy()
    n = len(d)
    Dm = sparse.csr_matrix((np.ones(n), (d, np.arange(n))), shape=(d.max() + 1, n))
    Lm = sparse.csr_matrix((np.ones(n), (l, np.arange(n))), shape=(l.max() + 1, n))
    cd = np.asarray(Dm.sum(1)).ravel(); cl = np.asarray(Lm.sum(1)).ravel()
    for it in range(n_iter):
        V -= ((Dm @ V) / cd[:, None])[d]
        delta = ((Lm @ V) / cl[:, None])[l]; V -= delta
        if np.abs(delta).max() < tol:
            break
    return V

def prune(ok):
    for _ in range(20):
        bad = (ok.sum(1) < 2)[:, None] | (ok.sum(0) < 2)[None, :]
        if not (ok & bad).any(): break
        ok &= ~bad
    return ok

def setup(Y, use_cov=True, extra_ok=None):
    ok = np.isfinite(Y) & keep[:, None]
    if use_cov:
        for c in covs: ok &= np.isfinite(c)
    if extra_ok is not None: ok &= extra_ok
    ok = prune(ok)
    d, l = np.nonzero(ok)
    d = pd.factorize(d)[0] if False else d
    dcode = pd.factorize(d)[0]; lcode = pd.factorize(l)[0]
    yt = fe_resid(Y[ok][:, None], dcode, lcode)[:, 0]
    Q = None
    if use_cov:
        C = np.column_stack([c[ok] for c in covs])
        C = np.column_stack([C * wt[l][:, None], C * (~wt[l])[:, None]])
        Ct = fe_resid(C, dcode, lcode)
        Q, s, _ = np.linalg.svd(Ct, full_matrices=False); Q = Q[:, s > s[0] * 1e-9]
        yt = yt - Q @ (Q.T @ yt)
    return ok, d, l, dcode, lcode, yt, Q

def xres(X, dcode, lcode, Q):
    Xt = fe_resid(X, dcode, lcode)
    if Q is not None: Xt = Xt - Q @ (Q.T @ Xt)
    return Xt

def cluster_se(xt, e, g):
    G = g.max() + 1
    s = np.bincount(g, weights=xt * e, minlength=G)
    return np.sqrt(G / (G - 1) * (s ** 2).sum()) / (xt @ xt), G


ok, d, l, dcode, lcode, yt, Q = setup(trim)
print("rows", ok.sum())
for g in ["FUS","ATF3","PMAIP1","FOS","JUN","EGR1","DDIT3","MDM2","CDKN1A","TP53"]:
    x = Ysel[:, :, sel.index(g)]
    o2, d2, l2, dc2, lc2, yt2, Q2 = setup(trim, extra_ok=np.isfinite(x))
    xt = xres(x[o2][:, None], dc2, lc2, Q2)[:, 0]
    b = xt @ yt2 / (xt @ xt); e = yt2 - b * xt
    r = xt @ yt2 / np.sqrt((xt @ xt) * (yt2 @ yt2))
    se_d, Gd = cluster_se(xt, e, drug_of[d2]); se_l, Gl = cluster_se(xt, e, l2)
    print(f"within-line r TRIM72 r2 vs {g} r2: {r:.4f} (n {o2.sum()}), t_drug {b/se_d:.1f}, t_line {b/se_l:.1f}")
for tf in ["AP1","ATF4","ELK4","E2F4"]:
    k = tfs.index(tf); x = TF[:, :, k].astype(float)
    for g in ["ATF3","FOS","EGR1","DDIT3"]:
        Yg_ = Ysel[:, :, sel.index(g)]
        o2, d2, l2, dc2, lc2, yt2, Q2 = setup(Yg_, extra_ok=np.isfinite(x))
        xt = xres(x[o2][:, None], dc2, lc2, Q2)[:, 0]
        r = xt @ yt2 / np.sqrt((xt @ xt) * (yt2 @ yt2))
        print(f"  within-line r {g} r2 vs {tf} activity: {r:.3f}")
