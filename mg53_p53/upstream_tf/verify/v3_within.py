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

named = ["AP1", "NFKB", "ATF4", "ATF5", "XBP1", "HSF1", "SRF", "ELK4", "CREB1", "TP53", "E2F4", "E2F1", "MYC", "MYBL1", "MEF2C", "MEF2A", "MYOD1"]
ok, d, l, dcode, lcode, yt, Q = setup(trim)
print("rows", ok.sum(), "drug-doses", len(np.unique(d)), "lines", len(np.unique(l)))
tab = pd.read_csv(os.path.join(STEP, "tables", "a2_within_line_tf_vs_trim72.csv.gz"))
tf_full = tab[(tab.trim72_version == "TRIM72") & (tab.covset == "full")].set_index("tf")
rows = []
for tf in named:
    k = tfs.index(tf)
    x = TF[:, :, k].astype(float)
    okx = ok & np.isfinite(x)
    if okx.sum() != ok.sum():
        o2, d2, l2, dc2, lc2, yt2, Q2 = setup(trim, extra_ok=np.isfinite(x))
    else:
        o2, d2, l2, dc2, lc2, yt2, Q2 = ok, d, l, dcode, lcode, yt, Q
    xt = xres(x[o2][:, None], dc2, lc2, Q2)[:, 0]
    b = xt @ yt2 / (xt @ xt); e = yt2 - b * xt
    r = xt @ yt2 / np.sqrt((xt @ xt) * (yt2 @ yt2))
    se_d, Gd = cluster_se(xt, e, drug_of[d2]); se_l, Gl = cluster_se(xt, e, l2)
    # WT / altered slopes
    x1 = xres((x[o2] * wt[l2])[:, None], dc2, lc2, Q2)[:, 0]; x2 = xres((x[o2] * ~wt[l2])[:, None], dc2, lc2, Q2)[:, 0]
    X2 = np.column_stack([x1, x2]); bb = np.linalg.lstsq(X2, yt2, rcond=None)[0]; e2 = yt2 - X2 @ bb
    XtXi = np.linalg.inv(X2.T @ X2); S = np.zeros((Gl, 2)); np.add.at(S, l2, X2 * e2[:, None])
    V = Gl / (Gl - 1) * XtXi @ (S.T @ S) @ XtXi
    sed = np.sqrt(V[0, 0] + V[1, 1] - 2 * V[0, 1])
    t_ = tf_full.loc[tf] if tf in tf_full.index else None
    rows.append({"tf": tf, "n": int(o2.sum()), "r_within": r, "b": b, "p_drug": 2 * stats.t.sf(abs(b / se_d), Gd - 1),
                 "r_ci95_drug_lo": r - 1.96 * r / (b / se_d) if b != 0 else np.nan,
                 "r_ci95_drug_hi": r + 1.96 * r / (b / se_d) if b != 0 else np.nan,
                 "b_WT": bb[0], "b_alt": bb[1], "p_diff_line": 2 * stats.t.sf(abs((bb[0] - bb[1]) / sed), Gl - 1),
                 "table_r": t_["r_partial_within"] if t_ is not None else np.nan,
                 "table_b": t_["b"] if t_ is not None else np.nan, "table_q": t_["q_bh_twoway"] if t_ is not None else np.nan,
                 "table_b_WT": t_["b_WT"] if t_ is not None else np.nan, "table_b_alt": t_["b_alt"] if t_ is not None else np.nan})
R = pd.DataFrame(rows)
pd.set_option("display.width", 250)
print(R.round(4).to_string(index=False))
R.to_csv(os.path.join(OUT, "v3_within_named.csv"), index=False)

# calibration: TFs complete on the common rows; drug-row permutation of the residual TRIM72 within line
allfin = np.isfinite(TF).all(axis=2)
okc, dC, lC, dcC, lcC, ytC, QC = setup(trim, extra_ok=allfin)
print("calibration rows (all TFs finite):", okc.sum())
Xall = TF[okc].astype(np.float64)                  # n x T
T = Xall.shape[1]
Xt = np.empty_like(Xall)
for c0 in range(0, T, 100):
    Xt[:, c0:c0 + 100] = xres(Xall[:, c0:c0 + 100], dcC, lcC, QC)
del Xall
Xn = Xt / np.linalg.norm(Xt, axis=0)
yu = ytC / np.linalg.norm(ytC)
r_obs = yu @ Xn
# residual grid
Yg = np.full(okc.shape, np.nan); Yg[okc] = ytC
dd_rows = np.unique(dC)
drug_rows = drug_of[dd_rows]
# permute whole drugs (all their doses move together; to a drug with the same number of kept doses)
rng = np.random.default_rng(11)
grp = pd.Series(dd_rows).groupby(drug_rows).apply(list)
by_n = {}
for dg, rws in grp.items():
    by_n.setdefault(len(rws), []).append(dg)
B = 200
null_r = np.zeros((B, T))
for b in range(B):
    mp = {}
    for nd_, drugs in by_n.items():
        sh = rng.permutation(drugs)
        for a_, b_ in zip(drugs, sh):
            for r1, r2 in zip(grp[a_], grp[b_]):
                mp[r1] = r2
    src = np.array([mp[x] for x in dC])
    yp = Yg[src, lC]
    m = np.isfinite(yp)
    ypz = np.where(m, yp, 0.0)
    null_r[b] = (ypz / np.linalg.norm(ypz)) @ Xn
sd = null_r.std(axis=0)
z = r_obs / sd
p_perm = 2 * stats.norm.sf(np.abs(z))
o = np.argsort(p_perm); qq = np.minimum.accumulate((p_perm[o] * T / np.arange(1, T + 1))[::-1])[::-1]
q = np.empty(T); q[o] = np.minimum(qq, 1)
ctrl = np.array([t.startswith("TP53 ") for t in tfs])
tab_r = tf_full["r_partial_within"].reindex(tfs).to_numpy()
tab_p = tf_full["p_twoway"].reindex(tfs).to_numpy()
print("r own (common rows) vs table r across TFs: corr", np.corrcoef(r_obs[~ctrl], tab_r[~ctrl])[0, 1])
print("analytic SE of r ~1/sqrt(n)", 1 / np.sqrt(okc.sum()), "; drug-row permutation null SD median", np.median(sd))
# implied SD in the table: r / z where z from p_twoway
z_tab = stats.t.isf(tab_p / 2, 46)
print("table implied SD of r (|r|/z) median", np.nanmedian(np.abs(tab_r) / z_tab))
pv = p_perm[~ctrl]
qv = q[~ctrl]
print("TFs q<0.1 by drug-row permutation:", int((qv < 0.1).sum()), "pos", int(((qv < 0.1) & (r_obs[~ctrl] > 0)).sum()),
      "neg", int(((qv < 0.1) & (r_obs[~ctrl] < 0)).sum()), "of", int((~ctrl).sum()))
print("table TFs q<0.1:", int((tf_full.q_bh_twoway < 0.1).sum()))
# null false-positive rate: how many TFs pass q<0.1 in permuted data using the permutation SD
fp = []
for b in range(min(B, 50)):
    zb = null_r[b] / sd; pb = 2 * stats.norm.sf(np.abs(zb))[~ctrl]
    ob = np.argsort(pb); qb = np.minimum.accumulate((pb[ob] * len(pb) / np.arange(1, len(pb) + 1))[::-1])[::-1]
    fp.append(int((qb < 0.1).sum()))
print("permuted-data TFs at q<0.1 (50 perms): mean", np.mean(fp), "max", np.max(fp))
pd.DataFrame({"tf": tfs, "r_own": r_obs, "null_sd_drugperm": sd, "p_perm": p_perm, "q_perm": q, "table_r": tab_r,
              "table_p": tab_p}).to_csv(os.path.join(OUT, "v3_within_all_calibration.csv"), index=False, float_format="%.4g")

# TP53 positive control within lines: MDM2 r2 / CDKN1A r2 on TP53 (MDM2, CDKN1A out)
for yname in ("MDM2", "CDKN1A"):
    Yv = Ysel[:, :, sel.index(yname)]
    for tfn in ("TP53 (MDM2, CDKN1A out)", "TP53 activated targets (MDM2, CDKN1A out)"):
        k = tfs.index(tfn); x = TF[:, :, k].astype(float)
        o2, d2, l2, dc2, lc2, yt2, Q2 = setup(Yv, extra_ok=np.isfinite(x))
        x1 = xres((x[o2] * wt[l2])[:, None], dc2, lc2, Q2)[:, 0]; x2 = xres((x[o2] * ~wt[l2])[:, None], dc2, lc2, Q2)[:, 0]
        X2 = np.column_stack([x1, x2]); bb = np.linalg.lstsq(X2, yt2, rcond=None)[0]; e2 = yt2 - X2 @ bb
        G = l2.max() + 1; XtXi = np.linalg.inv(X2.T @ X2); S = np.zeros((G, 2)); np.add.at(S, l2, X2 * e2[:, None])
        V = G / (G - 1) * XtXi @ (S.T @ S) @ XtXi
        sed = np.sqrt(V[0, 0] + V[1, 1] - 2 * V[0, 1])
        # also: per-line slopes, how many WT lines have slope > every altered line median
        print(f"PC within: {yname} r2 ~ {tfn}: n {o2.sum()}, b_WT {bb[0]:.3f} (se {np.sqrt(V[0,0]):.3f}), b_alt {bb[1]:.3f} "
              f"(se {np.sqrt(V[1,1]):.3f}), diff p {2*stats.t.sf(abs((bb[0]-bb[1])/sed), G-1):.2g}")
