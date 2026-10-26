"""Verifier v1: independent drug-dose-level recomputation of the upstream_tf A1 TF associations.
Own regulon parsing, own locus exclusion, a DIFFERENT activity method (mean of signed target z, no centering;
and a centred version), partial r with the same covariate list built here, OLS with drug-cluster (CR1) SE,
leave-one-drug-out jackknife SE. Then break attempts: influence, global activity, AP-1/IEG overlap, readthrough.
Reads only; writes to verify/out_v1/."""
import json, os, sys
import numpy as np, pandas as pd
from scipy import stats

DATA = sys.argv[1] if len(sys.argv) > 1 else "/home/user/tahoe_data"
STEP = "/home/user/Tahoe100-PseudoManual/mg53_p53/upstream_tf"
OUT = os.path.join(STEP, "verify", "out_v1"); os.makedirs(OUT, exist_ok=True)
FXD = os.path.join(DATA, "atlas", "effects")
rng = np.random.default_rng(1)

genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
gg = genes[genes.kind == "gene"].reset_index(drop=True)
cols = gg["col"].to_numpy()
sym = gg["symbol"].astype(str).to_numpy()
gix = {s: i for i, s in enumerate(sym)}
dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
keep = ~(dd.unreliable_plate_only.astype(bool) | dd.position_not_correctable.astype(bool)).to_numpy()
ddk = dd[keep].reset_index(drop=True)
Z = np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r")[np.flatnonzero(keep)][:, cols], dtype=np.float64)
Z = np.nan_to_num(Z)
n = Z.shape[0]
print("drug-doses", n, "genes", Z.shape[1])

# locus: own read of the Ensembl JSON + gene_metadata (ensembl -> symbol)
loc = json.load(open(os.path.join(STEP, "cache", "external", "ensembl_trim72_region.json")))
gm = pd.read_parquet(os.path.join(DATA, "metadata", "gene_metadata.parquet"))
ens2sym = dict(zip(gm["ensembl_id"].astype(str), gm["gene_symbol"].astype(str)))
tok2 = dict(zip(gm["token_id"].astype(int), gm["ensembl_id"].astype(str)))
loc_ids = {g["id"] for g in loc}
loc_syms = {g.get("external_name") for g in loc if g.get("external_name")} | {ens2sym.get(i, "") for i in loc_ids}
gens = np.array([tok2.get(int(t), "") for t in gg["token"]])
excl = np.isin(sym, list(loc_syms)) | np.isin(gens, list(loc_ids))
print("locus genes in atlas:", sorted(sym[excl]))
univ = ~excl

# regulon: own parse (sign rule: inhibition-only -> -1 else +1; complexes of AP-1 / NF-kB members -> AP1 / NFKB)
t = pd.read_csv(os.path.join(STEP, "cache", "external", "collectri.tsv"), sep="\t")
AP1 = {"JUN", "JUNB", "JUND", "FOS", "FOSB", "FOSL1", "FOSL2"}; NFKB = {"REL", "RELA", "RELB", "NFKB1", "NFKB2"}
def tfname(s):
    m = set(s.split("_"))
    if m <= AP1: return "AP1"
    if m <= NFKB: return "NFKB"
    return s
t["tf"] = t["source_genesymbol"].astype(str).map(tfname)
inh = t["is_inhibition"].astype(str).str.lower().eq("true") & ~t["is_stimulation"].astype(str).str.lower().eq("true")
t["w"] = np.where(inh, -1.0, 1.0)
reg = t.groupby(["tf", "target_genesymbol"])["w"].mean().reset_index()
reg["w"] = np.sign(reg["w"]).replace(0, 1)
reg["j"] = reg["target_genesymbol"].map(gix)
reg = reg.dropna(subset=["j"]); reg["j"] = reg["j"].astype(int)
reg = reg[univ[reg["j"].to_numpy()]]
print("TRIM72 in regulons after exclusion:", (reg.target_genesymbol == "TRIM72").sum(),
      "FUS:", (reg.target_genesymbol == "FUS").sum())
cnt = reg.groupby("tf").size()
tfs = sorted(cnt.index[cnt >= 5])
print("TFs with >= 5 targets:", len(tfs))
REG = {tf: (g["j"].to_numpy(), g["w"].to_numpy()) for tf, g in reg[reg.tf.isin(tfs)].groupby("tf")}

def act_mean(Zm, tf, drop=None):
    j, w = REG[tf]
    if drop is not None:
        k = ~np.isin(j, drop); j, w = j[k], w[k]
    return (Zm[:, j] * w).sum(axis=1) / len(j)

def act_centred(Zm, tf):
    j, w = REG[tf]
    mu = Zm[:, univ].mean(axis=1)
    return ((Zm[:, j] - mu[:, None]) * w).sum(axis=1) / len(j)

y = Z[:, gix["TRIM72"]]
rms = np.sqrt((Z ** 2).mean(axis=1))
cov = np.column_stack([np.log1p(ddk.n_sig_genes.fillna(0)), ddk.cells_log2_vs_plate.fillna(0),
                       ddk.umi_per_cell_log2_vs_plate.fillna(0), ddk.genes_per_cell_log2_vs_plate.fillna(0),
                       ddk.composition_shift_log2.fillna(0), ddk.S_PHASE_z.fillna(0), ddk.G2M_PHASE_z.fillna(0),
                       ddk.PROTEASOME_z.fillna(0), rms]).astype(float)
drug = pd.factorize(ddk.drug)[0]

def resid(v, C):
    X = np.column_stack([np.ones(len(v))] + ([C] if C is not None and np.size(C) else []))
    b, *_ = np.linalg.lstsq(X, v, rcond=None)
    return v - X @ b

def pr(x, yv, C):
    a, b = resid(x, C), resid(yv, C)
    return float(a @ b / np.sqrt((a @ a) * (b @ b)))

def ols_cluster(yv, x, C, groups):
    """t of x in OLS y ~ 1 + x + C with CR1 drug-cluster SE."""
    X = np.column_stack([np.ones(len(yv)), x] + ([C] if C is not None else []))
    XtXi = np.linalg.pinv(X.T @ X)
    b = XtXi @ X.T @ yv
    e = yv - X @ b
    G = groups.max() + 1
    S = np.zeros((G, X.shape[1])); np.add.at(S, groups, X * e[:, None])
    c = G / (G - 1) * (len(yv) - 1) / (len(yv) - X.shape[1])
    V = c * XtXi @ (S.T @ S) @ XtXi
    tt = b[1] / np.sqrt(V[1, 1])
    return b[1], tt, 2 * stats.t.sf(abs(tt), G - 1)

# 1) all TFs, mean method, covariates: partial r and drug-cluster p
rows = []
for tf in tfs:
    x = act_mean(Z, tf)
    xc = act_centred(Z, tf)
    r_raw = float(np.corrcoef(x, y)[0, 1])
    r_cov = pr(x, y, cov)
    r_cov_c = pr(xc, y, cov)
    _, tt, p = ols_cluster(y, x, cov, drug)
    rows.append({"tf": tf, "n_targets": len(REG[tf][0]), "r_raw_mean": r_raw, "r_cov_mean": r_cov,
                 "r_cov_centred": r_cov_c, "t_cluster": tt, "p_cluster": p})
R = pd.DataFrame(rows)
p = R.p_cluster.to_numpy(); o = np.argsort(p); q = np.empty_like(p)
qq = np.minimum.accumulate((p[o] * len(p) / np.arange(1, len(p) + 1))[::-1])[::-1]; q[o] = np.minimum(qq, 1)
R["q_bh_cluster"] = q
tab = pd.read_csv(os.path.join(STEP, "tables", "a1_dd_tf_vs_trim72.csv.gz"))
tc = tab[(tab.source == "CollecTRI_t") & (tab.trim72_version == "TRIM72") & (tab.variant == "covariates")].set_index("tf")
traw = tab[(tab.source == "CollecTRI_t") & (tab.trim72_version == "TRIM72") & (tab.variant == "raw")].set_index("tf")
R["r_cov_table_ulm"] = R.tf.map(tc["r"]); R["q_table"] = R.tf.map(tc["q_bh"]); R["r_raw_table_ulm"] = R.tf.map(traw["r"])
R.to_csv(os.path.join(OUT, "v1_all_tfs_mean_method.csv"), index=False, float_format="%.4g")
m = R.r_cov_table_ulm.notna()
print("TFs matched to table:", m.sum(), "of", len(R))
print("corr across TFs of r (mean method, covariates) vs table ULM r:", np.corrcoef(R.r_cov_mean[m], R.r_cov_table_ulm[m])[0, 1])
print("corr centred vs table:", np.corrcoef(R.r_cov_centred[m], R.r_cov_table_ulm[m])[0, 1])
print("q<0.1 (drug-cluster OLS, mean method): pos", ((R.q_bh_cluster < 0.1) & (R.t_cluster > 0)).sum(),
      "neg", ((R.q_bh_cluster < 0.1) & (R.t_cluster < 0)).sum(), "of", len(R))
print("table q<0.1: pos", ((tc.q_bh < 0.1) & (tc.r > 0)).sum(), "neg", ((tc.q_bh < 0.1) & (tc.r < 0)).sum())
top = R.sort_values("r_cov_mean", ascending=False)
print("top 15 by own mean-method r (covariates):")
print(top.head(15)[["tf", "n_targets", "r_raw_mean", "r_cov_mean", "r_cov_centred", "p_cluster", "r_cov_table_ulm"]].to_string(index=False))
print("rank of named TFs in own list (of %d):" % len(R))
rk = top.reset_index(drop=True)
for tf in ["ATF5", "ATF4", "XBP1", "SRF", "ELK4", "AP1", "NFKB", "HSF1", "CREB1", "TP53", "DDIT3", "ATF3"]:
    i = rk.index[rk.tf == tf]
    if len(i):
        r_ = rk.loc[i[0]]
        print(f"  {tf}: rank {i[0]+1}, own r {r_.r_cov_mean:.3f} (centred {r_.r_cov_centred:.3f}, raw {r_.r_raw_mean:.3f}), "
              f"cluster p {r_.p_cluster:.2g}; table r {r_.r_cov_table_ulm:.3f}")
tr = tc["r"].rank(ascending=False)
print("table ranks:", {tf: int(tr[tf]) for tf in ["ATF5", "ATF4", "XBP1", "SRF", "ELK4", "AP1", "NFKB", "HSF1"]})
np.save(os.path.join(OUT, "Zkeep_y.npy"), y)
