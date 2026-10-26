"""Verifier v2: try to break the top drug-dose-level TF associations with TRIM72 (table's ULM t from
a1_tf_activity_by_drugdose.csv.gz, plus own ULM recomputed for regulon edits)."""
import json, os, sys
import numpy as np, pandas as pd
from scipy import stats

DATA = sys.argv[1] if len(sys.argv) > 1 else "/home/user/tahoe_data"
STEP = "/home/user/Tahoe100-PseudoManual/mg53_p53/upstream_tf"
OUT = os.path.join(STEP, "verify", "out_v2"); os.makedirs(OUT, exist_ok=True)
FXD = os.path.join(DATA, "atlas", "effects")
genes = pd.read_csv(os.path.join(FXD, "genes.csv")); gg = genes[genes.kind == "gene"].reset_index(drop=True)
sym = gg.symbol.astype(str).to_numpy(); gix = {s: i for i, s in enumerate(sym)}
dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
keep = ~(dd.unreliable_plate_only.astype(bool) | dd.position_not_correctable.astype(bool)).to_numpy()
ddk = dd[keep].reset_index(drop=True)
Z = np.nan_to_num(np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r")[np.flatnonzero(keep)][:, gg.col.to_numpy()], dtype=np.float64))
y = Z[:, gix["TRIM72"]]
ACT = pd.read_csv(os.path.join(STEP, "tables", "a1_tf_activity_by_drugdose.csv.gz"))
assert (ACT.drug.to_numpy() == ddk.drug.to_numpy()).all() and np.allclose(ACT.conc, ddk.conc)
rms = np.sqrt((Z ** 2).mean(axis=1))
cov = np.column_stack([np.log1p(ddk.n_sig_genes.fillna(0)), ddk.cells_log2_vs_plate.fillna(0),
                       ddk.umi_per_cell_log2_vs_plate.fillna(0), ddk.genes_per_cell_log2_vs_plate.fillna(0),
                       ddk.composition_shift_log2.fillna(0), ddk.S_PHASE_z.fillna(0), ddk.G2M_PHASE_z.fillna(0),
                       ddk.PROTEASOME_z.fillna(0), rms]).astype(float)
drug = ddk.drug.to_numpy()

def resid(v, C):
    X = np.column_stack([np.ones(len(v))] + [c for c in C if c is not None])
    b, *_ = np.linalg.lstsq(X, v, rcond=None)
    return v - X @ b

def pr(x, yv, C, m=None):
    if m is not None:
        x, yv, C = x[m], yv[m], [c[m] for c in C]
    a, b = resid(x, C), resid(yv, C)
    return float(a @ b / np.sqrt((a @ a) * (b @ b)))

# own ULM (decoupler-style) for regulon edits
loc = json.load(open(os.path.join(STEP, "cache", "external", "ensembl_trim72_region.json")))
locsyms = {g.get("external_name") for g in loc if g.get("external_name")}
reg = pd.read_csv(os.path.join(STEP, "tables", "a0_regulons_used.csv.gz"))
reg = reg[(reg.source == "CollecTRI") & reg.target_in_atlas & ~reg.target_in_trim72_locus]
excl = np.isin(sym, list(locsyms | {"ENSG00000255439", "ENSG00000260911"}))
univ = ~excl
Zu = np.where(univ[None, :], Z, np.nan)

def ulm_t(tf, drop=()):
    r = reg[(reg.tf == tf) & ~reg.target.isin(drop)]
    w = np.zeros(len(sym)); w[r.target.map(gix).to_numpy()] = r.weight.to_numpy()
    w = w[univ]; X = Z[:, univ]
    wc = w - w.mean(); Xc = X - X.mean(axis=1, keepdims=True)
    b = Xc @ wc / (wc @ wc)
    rss = ((Xc - b[:, None] * wc[None, :]) ** 2).sum(axis=1)
    return b / np.sqrt(rss / (X.shape[1] - 2) / (wc @ wc)), len(r)

named = ["ATF5", "ATF4", "XBP1", "SRF", "ELK4", "AP1", "NFKB", "HSF1", "CREB1", "TP53"]
out = []
def rec(test, tf, r, n=None, note=""):
    out.append({"test": test, "tf": tf, "r": r, "n": n, "note": note})

# 0) reproduce the table r with the table's activity and own covariate build
tab = pd.read_csv(os.path.join(STEP, "tables", "a1_dd_tf_vs_trim72.csv.gz"))
tc = tab[(tab.source == "CollecTRI_t") & (tab.trim72_version == "TRIM72") & (tab.variant == "covariates")].set_index("tf")
for tf in named:
    x = ACT[tf].to_numpy()
    rec("covariates (own code, table activity)", tf, pr(x, y, [cov]), len(y), f"table {tc.loc[tf, 'r']:.4f}")
    t_own, nt = ulm_t(tf)
    rec("covariates (own ULM t)", tf, pr(t_own, y, [cov]), len(y), f"targets {nt}; max|t_own - t_table| {np.max(np.abs(t_own - x)):.2g}")

# 1) influence: drop the top k% drug-doses by |TRIM72 z|, by |activity|, by the product contribution
for tf in named:
    x = ACT[tf].to_numpy()
    a, b = resid(x, [cov]), resid(y, [cov])
    contrib = (a / a.std()) * (b / b.std())
    for frac in (0.01, 0.05, 0.10):
        k = int(round(frac * len(y)))
        m = np.ones(len(y), bool); m[np.argsort(-np.abs(y))[:k]] = False
        rec(f"drop top {frac:.0%} |TRIM72 z|", tf, pr(x, y, [cov], m), int(m.sum()))
        m = np.ones(len(y), bool); m[np.argsort(-contrib)[:k]] = False
        rec(f"drop top {frac:.0%} drug-doses by contribution to r", tf, pr(x, y, [cov], m), int(m.sum()))
    # Spearman partial
    rx, ry = stats.rankdata(x), stats.rankdata(y)
    rec("Spearman partial (ranks, covariates ranked)", tf, pr(rx, ry, [np.column_stack([stats.rankdata(c) for c in cov.T])]), len(y))
    # leave-one-drug-out min / max
    ud = np.unique(drug)
    lo = []
    for d in ud:
        m = drug != d
        lo.append(pr(x, y, [cov], m))
    lo = np.array(lo)
    j = int(np.argmin(lo))
    rec("leave-one-drug-out: min r", tf, float(lo.min()), None, f"drop {ud[j]}")
    # jackknife SE (drug)
    G = len(ud); se = np.sqrt((G - 1) / G * ((lo - lo.mean()) ** 2).sum())
    rec("leave-one-drug-out jackknife SE of r", tf, float(se), G)
    # drop the 20 drugs most influential for this TF (greedy by single-drug drop)
    worst = ud[np.argsort(lo)[:20]]
    m = ~np.isin(drug, worst)
    rec("drop the 20 drugs whose single removal lowers r most", tf, pr(x, y, [cov], m), int(m.sum()))
    # global activity: low-activity drug-doses only
    for qq in (0.5, 0.75):
        m = rms <= np.quantile(rms, qq)
        rec(f"only drug-doses with RMS z <= {int(qq*100)}th pct", tf, pr(x, y, [cov], m), int(m.sum()))

# 2) mediation by the AP-1 / IEG / ATF3 module: partial ATF3 z, PMAIP1 z, an IEG score, AP1 activity
IEG = ["FOS", "FOSB", "JUN", "JUNB", "EGR1", "EGR2", "EGR3", "IER2", "IER3", "IER5", "ATF3", "DUSP1", "NR4A1",
       "KLF6", "KLF4", "PPP1R15A", "GADD45B", "MYC", "ZFP36", "CYR61", "CCN1", "CTGF", "CCN2", "SERTAD1", "BTG2"]
ieg = [g for g in IEG if g in gix]
ieg_score = Z[:, [gix[g] for g in ieg]].mean(axis=1)
med = {"ATF3 z": Z[:, gix["ATF3"]], "PMAIP1 z": Z[:, gix["PMAIP1"]], "IEG score (mean z of %d IEGs)" % len(ieg): ieg_score,
       "AP1 activity": ACT["AP1"].to_numpy(), "DDIT3 z": Z[:, gix["DDIT3"]]}
med["all of the above"] = np.column_stack(list(med.values()))
for tf in named:
    x = ACT[tf].to_numpy()
    for nm, v in med.items():
        if tf == "AP1" and "AP1" in nm:
            continue
        rec(f"covariates + partial {nm}", tf, pr(x, y, [cov, v.reshape(len(y), -1)]), len(y))
rec("TRIM72 vs IEG score (covariates)", "-", pr(ieg_score, y, [cov]), len(y), ",".join(ieg))
rec("TRIM72 vs ATF3 z (covariates)", "-", pr(Z[:, gix["ATF3"]], y, [cov]), len(y))

# 3) regulon overlap: drop AP-1 targets and IEGs from each regulon
ap1_t = set(reg.loc[reg.tf == "AP1", "target"])
nfkb_t = set(reg.loc[reg.tf == "NFKB", "target"])
for tf in [t for t in named if t not in ("AP1", "NFKB")]:
    tg = set(reg.loc[reg.tf == tf, "target"])
    ov = tg & (ap1_t | set(ieg))
    t2, nt = ulm_t(tf, drop=ov)
    rec("regulon minus AP-1 targets and IEGs (own ULM t)", tf, pr(t2, y, [cov]), len(y),
        f"{len(ov)} of {len(tg)} targets dropped; {nt} left")
    ov2 = tg & (ap1_t | nfkb_t | set(ieg))
    t3, nt3 = ulm_t(tf, drop=ov2)
    rec("regulon minus AP-1, NF-kB targets and IEGs (own ULM t)", tf, pr(t3, y, [cov]), len(y),
        f"{len(ov2)} of {len(tg)} dropped; {nt3} left")
    t4, _ = ulm_t(tf, drop=ov2)
    rec("... and partial the IEG score + AP1 + NFKB activity", tf, pr(t4, y, [cov, ieg_score[:, None], ACT[["AP1", "NFKB"]].to_numpy()]), len(y))

# 4) readthrough: FUS z partialled (both sides) and FUS-high drug-doses dropped
fus = Z[:, gix["FUS"]]
for tf in named:
    x = ACT[tf].to_numpy()
    rec("covariates + FUS z partialled", tf, pr(x, y, [cov, fus[:, None]]), len(y))
rec("TRIM72 vs FUS z (covariates)", "-", pr(fus, y, [cov]), len(y))

# 5) PCs: own PCA, partial 1..20
Zs = Z[:, univ]; Zs = (Zs - Zs.mean(0)) / np.where(Zs.std(0) > 0, Zs.std(0), 1)
U, S, _ = np.linalg.svd(Zs, full_matrices=False)
for k in (1, 3, 10, 20, 50):
    for tf in named:
        rec(f"minus top {k} PCs (no covariates)", tf, pr(ACT[tf].to_numpy(), y, [U[:, :k]]), len(y))

D = pd.DataFrame(out)
D.to_csv(os.path.join(OUT, "v2_break_dd.csv"), index=False, float_format="%.4g")
P = D[D.tf.isin(named)].pivot_table(index="test", columns="tf", values="r", aggfunc="first")[named]
pd.set_option("display.width", 250)
print(P.round(3).to_string())
print(D[D.tf == "-"].to_string(index=False))
print(D[D.test.str.startswith("leave-one-drug-out: min")][["tf", "r", "note"]].to_string(index=False))
print(D[D.test.str.startswith("regulon minus AP-1 targets")][["tf", "note"]].to_string(index=False))
print(D[D.test.str.startswith("covariates (own ULM")][["tf", "r", "note"]].to_string(index=False))
