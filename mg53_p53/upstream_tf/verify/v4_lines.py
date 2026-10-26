"""Verifier v4: 50-line feature analysis. (i) recompute TRIM72 untreated level independently from gene_panel
well_line.parquet (DMSO wells); (ii) null: TRIM72 untreated level vs level-matched random genes' untreated level (same
oe_level procedure on the pass cache's DMSO counts); (iii) KMT2D robustness (leave-one-out, organ, n drivers);
(iv) idarubicin induction vs untreated: shared-baseline artefact check with plate-split untreated level."""
import os, sys, warnings
import numpy as np, pandas as pd
from scipy import stats
warnings.simplefilter("ignore")
DATA = sys.argv[1] if len(sys.argv) > 1 else "/home/user/tahoe_data"
STEP = "/home/user/Tahoe100-PseudoManual/mg53_p53/upstream_tf"
FXD = os.path.join(DATA, "atlas", "effects")
P = np.load(os.path.join(STEP, "cache", "pass_73b0ba7f7c76.npz"))
genes = pd.read_csv(os.path.join(FXD, "genes.csv")); gg = genes[genes.kind == "gene"].reset_index(drop=True)
sym = gg.symbol.astype(str).to_numpy(); gix = {s: i for i, s in enumerate(sym)}
lines = pd.read_csv(os.path.join(FXD, "lines.csv"), dtype=str); lid = lines.iloc[:, 0].tolist()
em = np.load(os.path.join(FXD, "expr_mask.npy"))[:, gg.col.to_numpy()].astype(bool)
plates = [str(p) for p in P["plates"]]
import json
info = json.load(open(os.path.join(FXD, "info.json")))
print("info", info)
unrel = set(info.get("unreliable_plates", []))
rel_pl = [i for i, p in enumerate(plates) if p not in unrel]
print("reliable plates used:", [plates[i] for i in rel_pl])
dmc, dmt, dmn = P["dm_c"], P["dm_t"], P["dm_n"]
MINC = 30

def oe(c, expressed, pl):
    O = np.zeros(c.shape[1]); E = np.zeros(c.shape[1])
    for p in pl:
        ok = dmn[p] >= MINC
        cpm = np.where(ok, 1e6 * c[p] / dmt[p], np.nan)
        med = np.nanmedian(cpm[ok & expressed])
        O += np.where(ok, c[p], 0); E += np.where(ok, dmt[p] / 1e6 * med, 0)
    return np.where(E >= 2, np.log2((O + 0.5) / (E + 0.5)), np.nan)

b1 = pd.read_csv(os.path.join(STEP, "tables", "b1_line_outcomes.csv"), dtype={"cell_line_id": str}).set_index("cell_line_id").reindex(lid)
jt = gix["TRIM72"]
tr = oe(dmc[:, :, jt].astype(float), em[:, jt], rel_pl)
print("own oe TRIM72 vs table: max|diff|", np.nanmax(np.abs(tr - b1.TRIM72_untreated_rel.to_numpy())))

# (i) independent: gene_panel well_line DMSO
wl = pd.read_parquet(os.path.join(DATA, "gene_panel", "well_line.parquet"), columns=["sample", "cell_line_id", "n_cells", "total_counts", "TRIM72"])
sm = pd.read_csv(os.path.join(DATA, "gene_panel", "sample_map.csv"))
print("sample_map cols", list(sm.columns)[:12])
wells = pd.read_csv(os.path.join(FXD, "wells.csv"))
dm_samples = set(wells.loc[wells.is_dmso.astype(bool), "sample"])
plate_of = dict(zip(wells["sample"], wells["plate"]))
w = wl[wl["sample"].isin(dm_samples)].copy(); w["plate"] = w["sample"].map(plate_of)
w = w[~w.plate.isin(unrel)]
g = w.groupby(["plate", "cell_line_id"])[["TRIM72", "total_counts", "n_cells"]].sum().reset_index()
g = g[g.n_cells >= MINC]
g["cpm"] = 1e6 * g.TRIM72 / g.total_counts
# simple independent level: per plate, log2(cpm+0.5/lib) minus plate median, mean over plates
g["l"] = np.log2((g.TRIM72 + 0.5) / g.total_counts * 1e6)
g["lc"] = g.l - g.groupby("plate").l.transform("median")
alt = g.groupby("cell_line_id").lc.mean().reindex(lid)
m = alt.notna() & b1.TRIM72_untreated_rel.notna()
print("independent (gene_panel, mean over plates of plate-centred log CPM) vs table untreated level: Spearman",
      stats.spearmanr(alt[m], b1.TRIM72_untreated_rel[m]).correlation, "n", m.sum())

# (ii) null distribution: level-matched genes' untreated rel vs TRIM72 rel
lvl = gg.median_line_cpm.to_numpy(float); nle = gg.n_lines_expressing.to_numpy(float)
lt = lvl[jt]
for lab, cand in (("level-matched (0.5-2x TRIM72 median line CPM, >=45 lines)", np.flatnonzero((lvl >= lt / 2) & (lvl <= 2 * lt) & (nle >= 45))),
                  ("low genes (1-20 CPM, any lines)", np.flatnonzero((lvl >= 1) & (lvl <= 20)))):
    rng = np.random.default_rng(5)
    pick = rng.choice(cand, size=min(400, len(cand)), replace=False)
    pick = pick[pick != jt]
    rho = []
    for j in pick:
        v = oe(dmc[:, :, j].astype(float), em[:, j], rel_pl)
        mm = np.isfinite(v) & np.isfinite(tr)
        if mm.sum() >= 30:
            rho.append(stats.spearmanr(v[mm], tr[mm]).correlation)
    rho = np.array(rho)
    print(f"{lab}: n genes {len(rho)}, median rho with TRIM72 untreated {np.median(rho):.3f}, 90th pct {np.percentile(rho, 90):.3f}, "
          f"99th {np.percentile(rho, 99):.3f}, max {rho.max():.3f}; share >= 0.57 (FUS) {np.mean(rho >= 0.57):.3f}; >= 0.82 {np.mean(rho >= 0.82):.3f}")
# FUS / PYCARD-AS1 as in the table
print("table FUS rho / PYCARD-AS1 rho:", stats.spearmanr(b1["FUS_untreated_rel"], b1.TRIM72_untreated_rel, nan_policy="omit").correlation,
      stats.spearmanr(b1["PYCARD-AS1_untreated_rel"], b1.TRIM72_untreated_rel, nan_policy="omit").correlation)
# neighbours other than FUS in the locus
for s in ["KAT8", "BCKDK", "STX4", "VKORC1", "PRSS8", "ZNF646", "ZNF668"]:
    if s in gix:
        v = oe(dmc[:, :, gix[s]].astype(float), em[:, gix[s]], rel_pl)
        mm = np.isfinite(v) & np.isfinite(tr)
        print(f"  locus gene {s}: rho with TRIM72 untreated {stats.spearmanr(v[mm], tr[mm]).correlation:.3f} (n {mm.sum()})")

# (iii) KMT2D
md = pd.read_parquet(os.path.join(DATA, "metadata", "cell_line_metadata.parquet"))
md = md[md.Cell_ID_Cellosaur.isin(lid)]
k = set(md.loc[md.Driver_Gene_Symbol == "KMT2D", "Cell_ID_Cellosaur"])
ndrv = md.groupby("Cell_ID_Cellosaur").Driver_Gene_Symbol.nunique().reindex(lid).fillna(0)
y = b1.TRIM72_untreated_rel
km = pd.Series([l in k for l in lid], index=lid).astype(float)
t = pd.DataFrame({"y": y, "kmt2d": km, "ndrv": ndrv, "organ": b1.organ, "name": b1.cell_line}).dropna(subset=["y"])
print("KMT2D-mutant lines:", t[t.kmt2d == 1][["name", "organ", "ndrv", "y"]].sort_values("y").to_string())
print("ndrv distribution: KMT2D mut median", t[t.kmt2d == 1].ndrv.median(), "others", t[t.kmt2d == 0].ndrv.median())
# partial: rank y on kmt2d controlling for ndrv rank
ry = stats.rankdata(t.y); X = np.column_stack([np.ones(len(t)), stats.rankdata(t.ndrv)])
ryr = ry - X @ np.linalg.lstsq(X, ry, rcond=None)[0]; kr = t.kmt2d.to_numpy() - X @ np.linalg.lstsq(X, t.kmt2d.to_numpy(), rcond=None)[0]
print("KMT2D rho partial on n drivers:", np.corrcoef(ryr, kr)[0, 1])
# drop high-driver-count lines (top quartile)
mm = t.ndrv <= t.ndrv.quantile(0.75)
print("KMT2D rho in lines with ndrv <= 75th pct:", stats.spearmanr(t.y[mm], t.kmt2d[mm]).correlation, "n", mm.sum(), "mut", int(t.kmt2d[mm].sum()))
# leave-one-out
loo = [stats.spearmanr(t.y.drop(i), t.kmt2d.drop(i)).correlation for i in t.index]
print("KMT2D leave-one-line-out rho range", np.min(loo), np.max(loo))
# other drivers with high counts: test random 'pseudo-driver' sets of 14 lines drawn with prob ~ ndrv
rng = np.random.default_rng(9)
w_ = (t.ndrv / t.ndrv.sum()).to_numpy()
pr = []
for b in range(5000):
    s = rng.choice(len(t), 14, replace=False, p=w_)
    v = np.zeros(len(t)); v[s] = 1
    pr.append(stats.spearmanr(t.y, v).correlation)
pr = np.array(pr)
print("pseudo-driver sets of 14 lines sampled in proportion to n drivers: mean rho", pr.mean(), "P(rho >= KMT2D's)",
      np.mean(pr >= stats.spearmanr(t.y, t.kmt2d).correlation))
# (iv) idarubicin induction vs untreated using plate-split untreated level (avoid sharing plate 6 / 14 baselines)
idx = b1["TRIM72_r2_idarubicin_5"]
pl_wo = [i for i in rel_pl if plates[i] not in ("plate6", "plate14")]
tr_wo = oe(dmc[:, :, jt].astype(float), em[:, jt], pl_wo)
mm = np.isfinite(tr_wo) & idx.notna().to_numpy()
print("idarubicin r2 vs untreated (all reliable plates):", stats.spearmanr(idx, y, nan_policy="omit").correlation,
      "; vs untreated from plates other than 6 and 14:", stats.spearmanr(idx[mm], tr_wo[mm]).correlation)
w6 = b1["TRIM72_r2_idarubicin_5_well_plate6"]; w14 = b1["TRIM72_r2_idarubicin_5_well_plate14"]
mm = w6.notna() & w14.notna() & y.notna()
print("cross-well: plate6 well r2 vs plate14 well r2", stats.spearmanr(w6[mm], w14[mm]).correlation,
      "; residuals after untreated adj:",
      stats.spearmanr(w6[mm] - np.polyval(np.polyfit(y[mm], w6[mm], 1), y[mm]), w14[mm] - np.polyval(np.polyfit(y[mm], w14[mm], 1), y[mm])).correlation)
