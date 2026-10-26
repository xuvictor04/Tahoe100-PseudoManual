"""Verifier: is TRIM72 in NCI-H661 (atlas: not expressed) ambient? Per well, H661 TRIM72 CPM vs the well's TRIM72 'soup'
(all other lines pooled), binned; same for each fitted line, to estimate how much of each line's TRIM72 is soup-like."""
import sys, numpy as np, pandas as pd
data = sys.argv[1]
wl = pd.read_parquet(f"{data}/gene_panel/well_line.parquet", columns=["sample", "cell_line_id", "n_cells", "total_counts", "TRIM72", "det_TRIM72"])
wl["sample"] = wl["sample"].astype(str); wl["cell_line_id"] = wl["cell_line_id"].astype(str)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum()
li = pd.read_csv(f"{data}/atlas/effects/lines.csv"); li["cell_line_id"] = li["cell_line_id"].astype(str)
base = pd.read_csv(f"{data}/gene_panel/results/baseline_by_cell_line.csv"); base["cell_line_id"] = base["cell_line_id"].astype(str)
wl = wl.merge(li[["cell_line_id", "cell_name"]], on="cell_line_id").merge(base[["cell_line_id", "tp53_group"]], on="cell_line_id", how="left")
sm = pd.read_csv(f"{data}/gene_panel/sample_map.csv"); sm["sample"] = sm["sample"].astype(str)
fail = set(pd.read_csv(f"{data}/atlas/effects/failed_wells.csv")["sample"].astype(str))
wl = wl[~wl["sample"].isin(fail)]
tot = wl.groupby("sample")[["total_counts", "TRIM72"]].sum()
H = wl[wl["cell_name"] == "NCI-H661"].set_index("sample")
soup = (tot["TRIM72"] - H["TRIM72"].reindex(tot.index).fillna(0)) / (tot["total_counts"] - H["total_counts"].reindex(tot.index).fillna(0)) * 1e6
H = H.join(soup.rename("soup_cpm"))
H["bin"] = pd.qcut(H["soup_cpm"], 5, labels=False, duplicates="drop")
b = H.groupby("bin").agg(wells=("n_cells", "size"), soup_cpm=("soup_cpm", "median"), cells=("n_cells", "sum"), umi=("total_counts", "sum"), trim72=("TRIM72", "sum"), det=("det_TRIM72", "sum"))
b["H661_cpm"] = b["trim72"] / b["umi"] * 1e6
b["H661_det_pct"] = 100 * b["det"] / b["cells"]
b["H661_over_soup"] = b["H661_cpm"] / b["soup_cpm"]
print("NCI-H661 TRIM72 by quintile of the well's TRIM72 soup (other lines pooled):")
print(b.round(4).to_string())
# Poisson regression of H661 counts on log soup (offset log umi): slope 1 = proportional to soup (ambient)
from scipy import optimize
x = np.log(H["soup_cpm"].clip(lower=1e-3).to_numpy()); y = H["TRIM72"].to_numpy(); off = np.log(H["total_counts"].to_numpy() / 1e6)
def nll(p):
    eta = p[0] + p[1] * (x - x.mean()) + off
    return -(y * eta - np.exp(eta)).sum()
r = optimize.minimize(nll, [0, 0.5], method="BFGS")
print("H661 Poisson slope on log soup CPM (1 = proportional to soup):", r.x[1].round(3), "+-", np.sqrt(np.diag(r.hess_inv))[1].round(3))
# overall ambient fraction estimate rho = H661 TRIM72 / (soup cpm * H661 umi)
rho = H["TRIM72"].sum() / (H["soup_cpm"] * H["total_counts"] / 1e6).sum()
print(f"H661: TRIM72 UMIs {H['TRIM72'].sum():.0f}, expected if soup-proportional with rho=1: {(H['soup_cpm']*H['total_counts']/1e6).sum():.0f}; rho = {rho:.3f}")
# per line: own CPM vs expected soup-only CPM (rho x soup of the same wells) -> soup fraction
rows = []
for (cn, tp), h in wl[wl["cell_name"] != "NCI-H661"].groupby(["cell_name", "tp53_group"]):
    h = h.set_index("sample")
    s_ = ((tot["TRIM72"] - h["TRIM72"]) / (tot["total_counts"] - h["total_counts"]) * 1e6).reindex(h.index)
    exp_soup = rho * (s_ * h["total_counts"] / 1e6).sum()
    rows.append(dict(cell_name=cn, tp53_group=tp, umi=h["total_counts"].sum(), trim72=h["TRIM72"].sum(), cpm=h["TRIM72"].sum() / h["total_counts"].sum() * 1e6,
                     expected_soup_umis=exp_soup, soup_fraction_est=exp_soup / h["TRIM72"].sum()))
R = pd.DataFrame(rows).sort_values("soup_fraction_est", ascending=False)
print(R.round(3).to_string(index=False))
R.to_csv(sys.argv[2], index=False)
print("lines with estimated soup fraction >= 0.5:", R.groupby("tp53_group").apply(lambda d: int((d.soup_fraction_est >= 0.5).sum())).to_dict(),
      "of", R.groupby("tp53_group").size().to_dict())
