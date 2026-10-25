#!/usr/bin/env python3
"""F1 cell-cycle confounding: idarubicin 5 uM arrests cells (S_PHASE z 8). Do per-line TRIM72 induction and p53-score
induction both follow the line's cell-cycle shift, and does partialling it out change the TRIM72 vs P53_SCORE
association? Per-line S / G2M / PROTEASOME effects from atlas DD_r2_modules.npy; per-line TRIM72_r2 / P53_SCORE from
the analysis's a_per_line_effects (re-derived independently in v1: Pearson 0.9999 / 0.98). Also Fisher-z 95% CIs for
the main rho values (what size of association the n=17 WT test can exclude).

    python3 verify/v1c_cellcycle.py -> verify/out/v1c_*.csv
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")
rng = np.random.default_rng(17)
IDA = "Idarubicin (hydrochloride)"
E = os.path.join(DATA, "atlas", "effects")
dd = pd.read_csv(os.path.join(E, "drugdose.csv"))
lid = pd.read_csv(os.path.join(E, "lines.csv")).cell_line_id.astype(str).tolist()
mod = np.load(os.path.join(E, "DD_r2_modules.npy"), mmap_mode="r")
pl = pd.read_csv(os.path.join(ROOT, "tables", "a_per_line_effects.csv"))


def partial(x, y, Z, nperm=4000):
    ok = np.isfinite(x) & np.isfinite(y)
    if Z is not None:
        ok &= np.isfinite(Z).all(1)
    n = int(ok.sum())
    rx, ry = stats.rankdata(x[ok]), stats.rankdata(y[ok])
    if Z is not None:
        X = np.column_stack([np.ones(n)] + [stats.rankdata(Z[ok, j]) for j in range(Z.shape[1])])
        rx = rx - X @ np.linalg.lstsq(X, rx, rcond=None)[0]
        ry = ry - X @ np.linalg.lstsq(X, ry, rcond=None)[0]
    r = float(np.corrcoef(rx, ry)[0, 1])
    null = np.array([np.corrcoef(rx[rng.permutation(n)], ry)[0, 1] for _ in range(nperm)])
    p = float((1 + (np.abs(null) >= abs(r) - 1e-12).sum()) / (nperm + 1))
    k = 0 if Z is None else Z.shape[1]
    se = 1 / np.sqrt(max(n - 3 - k, 1))
    lo, hi = np.tanh(np.arctanh(r) - 1.96 * se), np.tanh(np.arctanh(r) + 1.96 * se)
    return n, r, p, lo, hi


rows = []
for drug, conc in ((IDA, 5.0), (IDA, 0.5), ("Doxorubicin (hydrochloride)", 5.0), ("Epirubicin (hydrochloride)", 5.0),
                   ("Topotecan (hydrochloride)", 5.0), ("Mitoxantrone (dihydrochloride)", 5.0)):
    ri = int(dd.index[(dd.drug == drug) & np.isclose(dd.conc, conc)][0])
    Mo = pd.DataFrame(np.asarray(mod[ri]), index=lid, columns=["S", "G2M", "PROT"])
    g0 = pl[(pl.drug == drug) & np.isclose(pl.conc, conc)].set_index("cell_line_id").join(Mo)
    for grp in ("WT", "altered"):
        g = g0[g0.tp53_group == grp]
        x = g.TRIM72_r2.to_numpy()
        for out in ("P53_SCORE", "MDM2", "CDKN1A"):
            y = g[out].to_numpy()
            for adj, cols in (("none", None), ("S+G2M", ["S", "G2M"]), ("beta+A", ["atlas_beta", "atlas_A"]),
                              ("beta+A+S+G2M", ["atlas_beta", "atlas_A", "S", "G2M"]),
                              ("TRIM72 base+S+G2M", ["TRIM72_base", "S", "G2M"])):
                Z = None if cols is None else g[cols].to_numpy(float)
                n, r, p, lo, hi = partial(x, y, Z)
                rows.append(dict(drug=drug, conc=conc, group=grp, outcome=out, adjust=adj, n=n, rho=r, p_perm=p,
                                 fisher_ci_lo=lo, fisher_ci_hi=hi))
        # how much do the two readouts follow the cell-cycle shift?
        for v in ("TRIM72_r2", "P53_SCORE"):
            for cc in ("S", "G2M"):
                ok = g[v].notna() & g[cc].notna()
                rows.append(dict(drug=drug, conc=conc, group=grp, outcome=f"{v} vs {cc} shift", adjust="-",
                                 n=int(ok.sum()), rho=stats.spearmanr(g.loc[ok, v], g.loc[ok, cc])[0],
                                 p_perm=stats.spearmanr(g.loc[ok, v], g.loc[ok, cc])[1]))
R = pd.DataFrame(rows)
R.to_csv(os.path.join(OUT, "v1c_cellcycle_partial.csv"), index=False)
pd.set_option("display.width", 220)
pd.set_option("display.max_rows", 400)
print(R[(R.drug == IDA) & (R.conc == 5)].round(3).to_string())
print(R[(R.outcome == "P53_SCORE") & (R.group == "WT")].round(3).to_string())
