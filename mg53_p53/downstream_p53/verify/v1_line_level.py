#!/usr/bin/env python3
"""Adversarial check of F1/F3 (idarubicin 5 uM, per-line TRIM72 induction vs p53-target induction).

Independent of downstream_p53.py's cache: per (well, line) counts come straight from gene_panel/well_line.parquet,
the baseline is the line's median log2 CPM over the same plate's drug wells (or its DMSO wells), optional composition
shift from atlas/effects/composition_shift.parquet. Atlas DD_beta / DD_A read directly. The analysis's own cache is
also read once to reproduce its exact numbers.

    python3 verify/v1_line_level.py           -> verify/out/v1_*.csv
Nothing is written outside verify/out.
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
IDA = "Idarubicin (hydrochloride)"
IDA_WELLS = {"plate6": "smp_2010", "plate14": "smp_2778"}
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
GENES = ["TRIM72", "TP53", "PMAIP1", "ATF3"] + P53
MIN_CELLS = 30
rng = np.random.default_rng(7)


def spearman_partial(x, y, Z=None):
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    if Z is not None:
        Z = np.asarray(Z, float).reshape(len(x), -1)
        ok &= np.isfinite(Z).all(1)
    n = ok.sum()
    rx, ry = stats.rankdata(x[ok]), stats.rankdata(y[ok])
    k = 0
    if Z is not None:
        Zr = np.column_stack([np.ones(n)] + [stats.rankdata(Z[ok, j]) for j in range(Z.shape[1])])
        rx = rx - Zr @ np.linalg.lstsq(Zr, rx, rcond=None)[0]
        ry = ry - Zr @ np.linalg.lstsq(Zr, ry, rcond=None)[0]
        k = Z.shape[1]
    r = np.corrcoef(rx, ry)[0, 1]
    # permutation p of the residual correlation
    perm = np.array([np.corrcoef(rx[rng.permutation(n)], ry)[0, 1] for _ in range(4000)])
    pp = (1 + (np.abs(perm) >= abs(r) - 1e-12).sum()) / 4001
    return int(n), float(r), float(pp), k


def boot_ci(x, y, Z=None, B=2000):
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    if Z is not None:
        Z = np.asarray(Z, float).reshape(len(x), -1)
        ok &= np.isfinite(Z).all(1)
    idx = np.where(ok)[0]
    out = []
    for _ in range(B):
        ii = rng.choice(idx, len(idx), replace=True)
        if len(np.unique(ii)) < 6:
            continue
        rx, ry = stats.rankdata(x[ii]), stats.rankdata(y[ii])
        if Z is not None:
            Zr = np.column_stack([np.ones(len(ii))] + [stats.rankdata(Z[ii, j]) for j in range(Z.shape[1])])
            rx = rx - Zr @ np.linalg.lstsq(Zr, rx, rcond=None)[0]
            ry = ry - Zr @ np.linalg.lstsq(Zr, ry, rcond=None)[0]
        with np.errstate(invalid="ignore"):
            out.append(np.corrcoef(rx, ry)[0, 1])
    out = np.array(out)
    out = out[np.isfinite(out)]
    return float(np.quantile(out, 0.025)), float(np.quantile(out, 0.975))


# ---------------------------------------------------------------- 0. reproduce from the analysis's own table
pl = pd.read_csv(os.path.join(os.path.dirname(HERE), "tables", "a_per_line_effects.csv"))
pl = pl[(pl.drug == IDA) & np.isclose(pl.conc, 5)].set_index("cell_line_id")
rows = []
for grp in ("WT", "altered"):
    g = pl[pl.tp53_group == grp]
    for adj, Z in (("none", None), ("beta+A", g[["atlas_beta", "atlas_A"]].to_numpy())):
        n, r, pp, _ = spearman_partial(g.TRIM72_r2, g.P53_SCORE, Z)
        rows.append(dict(source="analysis table a_per_line_effects", group=grp, adjust=adj, n=n, rho=r, p_perm=pp))
rep = pd.DataFrame(rows)

# ---------------------------------------------------------------- 1. independent per-line effects from raw counts
sm = pd.read_csv(os.path.join(DATA, "gene_panel", "sample_map.csv"), dtype={"sample": str})
wl = pd.read_parquet(os.path.join(DATA, "gene_panel", "well_line.parquet"),
                     columns=["sample", "cell_line_id", "n_cells", "total_counts"] + GENES)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum()     # duplicates at file boundaries
wl = wl.merge(sm[["sample", "plate", "drug", "conc", "is_dmso"]], on="sample")
wl = wl[wl.plate.isin(["plate6", "plate14"])]
# well-level cell totals: drop failed wells (< 10% of the plate's median well)
wc = wl.groupby("sample").n_cells.sum()
pm = wl.groupby("sample").plate.first()
bad = wc[wc < 0.1 * wc.groupby(pm).transform("median")].index
wl = wl[~wl["sample"].isin(bad)]
comp = pd.read_parquet(os.path.join(DATA, "atlas", "effects", "composition_shift.parquet"))
wl = wl.merge(comp, on=["sample", "cell_line_id"], how="left")
for g in GENES:
    wl["y_" + g] = np.log2((wl[g] + 0.5) / wl.total_counts * 1e6)
ok = wl.n_cells >= MIN_CELLS
lines = pd.read_csv(os.path.join(DATA, "atlas", "effects", "lines.csv"))
lid = lines.cell_line_id.astype(str).tolist()
genes_at = pd.read_csv(os.path.join(DATA, "atlas", "effects", "genes.csv"))
expr = np.load(os.path.join(DATA, "atlas", "effects", "expr_mask.npy"), mmap_mode="r")
ga = genes_at[genes_at.kind == "gene"].drop_duplicates("symbol")
col_of = dict(zip(ga.symbol, ga.col))
EXPR = pd.DataFrame({g: np.asarray(expr[:, col_of[g]]).astype(bool) for g in GENES}, index=lid)
base = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "baseline_by_cell_line.csv")).set_index("cell_line_id")
tp = base["tp53_group"].reindex(lid)
name = lines.set_index("cell_line_id")["cell_name"]

eff = {}
for bmode in ("drug-well median", "DMSO wells"):
    for cmode in ("composition shift", "no composition shift"):
        per_plate = []
        for plate, w in IDA_WELLS.items():
            P_ = wl[(wl.plate == plate) & ok]
            if bmode == "drug-well median":
                B = P_[~P_.is_dmso & (P_["sample"] != w)]
                bl = B.groupby("cell_line_id")[["y_" + g for g in GENES]].median()
                if cmode == "composition shift":
                    Bc = B.copy()
                    for g in GENES:
                        Bc["y_" + g] = Bc["y_" + g] - Bc.shift_log2.fillna(0)
                    bl = Bc.groupby("cell_line_id")[["y_" + g for g in GENES]].median()
            else:
                B = wl[(wl.plate == plate) & wl.is_dmso]
                Bs = B.groupby("cell_line_id")[GENES + ["total_counts"]].sum()
                bl = pd.DataFrame({"y_" + g: np.log2((Bs[g] + 0.5) / Bs.total_counts * 1e6) for g in GENES})
            T = P_[P_["sample"] == w].set_index("cell_line_id")
            r = pd.DataFrame({g: T["y_" + g] - bl["y_" + g].reindex(T.index) for g in GENES})
            if cmode == "composition shift":
                r = r.sub(T.shift_log2.fillna(0), axis=0)
            r["plate"] = plate
            per_plate.append(r)
        R = pd.concat(per_plate).reset_index().groupby("cell_line_id")[GENES].mean().reindex(lid)
        for g in GENES:
            R.loc[~EXPR[g], g] = np.nan
        R["P53_SCORE"] = R[P53].mean(axis=1)
        eff[(bmode, cmode)] = R
        R.assign(cell_line=name.reindex(lid).values, tp53=tp.values).to_csv(
            os.path.join(OUT, f"v1_effects_{bmode.split()[0]}_{cmode.split()[0]}.csv"))

# atlas covariates
dd = pd.read_csv(os.path.join(DATA, "atlas", "effects", "drugdose.csv"))
ri = int(dd.index[(dd.drug == IDA) & np.isclose(dd.conc, 5)][0])
beta = pd.Series(np.asarray(np.load(os.path.join(DATA, "atlas", "effects", "DD_beta.npy"), mmap_mode="r")[ri]), index=lid)
Aab = pd.Series(np.asarray(np.load(os.path.join(DATA, "atlas", "effects", "DD_A.npy"), mmap_mode="r")[ri]), index=lid)
# p53 responsiveness from reference activators that do NOT raise TRIM72 (TRIM72 z <= 0): selinexor 5, amsacrine 5,
# topotecan 0.5, mitoxantrone 0.5 -- the 'expected' p53 response of a line to a p53 stimulus without a TRIM72 rise
# per-line effects are not in DD_lfc (pooled); use the analysis table a_per_line_effects (method v3 per-line r2)
ape = pd.read_csv(os.path.join(os.path.dirname(HERE), "tables", "a_per_line_effects.csv"))
refs = [("Selinexor", 5.0), ("Amsacrine", 5.0), ("Topotecan (hydrochloride)", 0.5), ("Mitoxantrone (dihydrochloride)", 0.5)]
resp = pd.concat([ape[(ape.drug == d) & np.isclose(ape.conc, c)].set_index("cell_line_id")["P53_SCORE"] for d, c in refs],
                 axis=1).mean(axis=1).reindex(lid)
tbase = np.log2(pd.read_csv(os.path.join(os.path.dirname(HERE), "cache", "lines.csv")).set_index("cell_line_id")
                ["cpm_dmso_TRIM72"].reindex(lid) + 0.1)

rows = []
for (bmode, cmode), R in eff.items():
    for grp in ("WT", "altered"):
        gm = (tp == grp).to_numpy()
        for drop in ("none", "drop A-427 (0 reads, 1 well)"):
            m = gm.copy()
            if drop != "none":
                m &= (name.reindex(lid) != "A-427").to_numpy()
            covs = {"none": None, "DD_beta+DD_A": np.column_stack([beta, Aab]),
                    "DD_beta+DD_A+TRIM72 base": np.column_stack([beta, Aab, tbase]),
                    "p53 resp (non-raisers)": resp.to_numpy()[:, None],
                    "p53 resp+DD_beta+DD_A": np.column_stack([resp, beta, Aab])}
            for out in ("P53_SCORE", "MDM2", "CDKN1A", "TP53"):
                for adj, Z in covs.items():
                    x, y = R["TRIM72"].to_numpy()[m], R[out].to_numpy()[m]
                    Zm = None if Z is None else Z[m]
                    n, r, pp, k = spearman_partial(x, y, Zm)
                    lo, hi = boot_ci(x, y, Zm, 1000) if out == "P53_SCORE" else (np.nan, np.nan)
                    rows.append(dict(source="independent", baseline=bmode, composition=cmode, group=grp, lines=drop,
                                     outcome=out, adjust=adj, n=n, rho=r, p_perm=pp, boot_lo=lo, boot_hi=hi))
res = pd.DataFrame(rows)
res.to_csv(os.path.join(OUT, "v1_idarubicin_line_correlations.csv"), index=False)
rep.to_csv(os.path.join(OUT, "v1_reproduce_analysis.csv"), index=False)

# agreement of my per-line effects with the analysis's method-v3 per-line r2
R = eff[("drug-well median", "composition shift")]
agree = []
for g, col in (("TRIM72", "TRIM72_r2"), ("P53_SCORE", "P53_SCORE"), ("MDM2", "MDM2"), ("CDKN1A", "CDKN1A")):
    a = pl[col].reindex(lid)
    ok2 = a.notna() & R[g].notna()
    agree.append(dict(feature=g, n=int(ok2.sum()), pearson=float(np.corrcoef(a[ok2], R[g][ok2])[0, 1]),
                      spearman=float(stats.spearmanr(a[ok2], R[g][ok2])[0]),
                      median_abs_diff=float((a[ok2] - R[g][ok2]).abs().median())))
pd.DataFrame(agree).to_csv(os.path.join(OUT, "v1_agreement_with_analysis.csv"), index=False)

# leave-one-line-out influence (main independent version, WT, unadjusted and DD_beta+DD_A)
inf = []
gm = (tp == "WT").to_numpy()
for adj, Z in (("none", None), ("DD_beta+DD_A", np.column_stack([beta, Aab]))):
    idx = np.where(gm & R["TRIM72"].notna().to_numpy() & R["P53_SCORE"].notna().to_numpy())[0]
    for j in idx:
        m = np.zeros(len(lid), bool)
        m[idx] = True
        m[j] = False
        n, r, pp, _ = spearman_partial(R["TRIM72"].to_numpy()[m], R["P53_SCORE"].to_numpy()[m], None if Z is None else Z[m])
        inf.append(dict(adjust=adj, left_out=name[lid[j]], n=n, rho=r))
pd.DataFrame(inf).to_csv(os.path.join(OUT, "v1_leave_one_out_WT.csv"), index=False)

# TRIM72 induction vs baseline and treated level (is 'induction' just the inverse of the untreated level?)
lev = []
for grp in ("WT", "altered", None):
    m = (tp == grp).to_numpy() if grp else np.ones(len(lid), bool)
    x = R["TRIM72"].to_numpy()[m]
    lev.append(dict(group=grp or "all", n=int(np.isfinite(x).sum()),
                    rho_induction_vs_untreated=stats.spearmanr(x, tbase.to_numpy()[m], nan_policy="omit")[0],
                    rho_induction_vs_treated_level=stats.spearmanr(x, pl["TRIM72_level"].reindex(lid).to_numpy()[m],
                                                                   nan_policy="omit")[0]))
pd.DataFrame(lev).to_csv(os.path.join(OUT, "v1_trim72_induction_vs_level.csv"), index=False)

# P53_SCORE separates WT from altered under idarubicin 5 uM? (is the outcome a p53 readout here?)
a, b = R.loc[tp == "WT", "P53_SCORE"].dropna(), R.loc[tp == "altered", "P53_SCORE"].dropna()
u = stats.mannwhitneyu(a, b)
pd.DataFrame([dict(median_WT=a.median(), median_altered=b.median(), n_WT=len(a), n_alt=len(b),
                   AUC=u.statistic / len(a) / len(b), p=u.pvalue)]).to_csv(os.path.join(OUT, "v1_p53score_WT_vs_alt.csv"),
                                                                        index=False)
pd.set_option("display.width", 220)
print(rep.to_string())
print(pd.DataFrame(agree).to_string())
print(res[(res.outcome == "P53_SCORE")].round(3).to_string())
print(pd.DataFrame(lev).round(3).to_string())
print(pd.read_csv(os.path.join(OUT, "v1_p53score_WT_vs_alt.csv")).round(4).to_string())
li = pd.DataFrame(inf)
print(li.groupby("adjust").rho.describe().round(3))
print(li.sort_values("rho").round(3).to_string())
