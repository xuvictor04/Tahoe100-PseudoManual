"""Verifier: ambient coefficient from genes that are homozygously deleted (CDKN2A in cdkn2a_deleted lines, MTAP in
mtap_null lines): a deleted gene's reads in that line can only be soup / cross-contamination. rho = line CPM / soup CPM
(soup = other lines of the same wells pooled). Compare with NCI-H661 TRIM72 (rho ~0.21)."""
import sys, numpy as np, pandas as pd
data = sys.argv[1]
wl = pd.read_parquet(f"{data}/gene_panel/well_line.parquet", columns=["sample", "cell_line_id", "n_cells", "total_counts", "TRIM72", "CDKN2A", "MTAP", "det_TRIM72", "det_CDKN2A", "det_MTAP"])
wl["sample"] = wl["sample"].astype(str); wl["cell_line_id"] = wl["cell_line_id"].astype(str)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum()
fail = set(pd.read_csv(f"{data}/atlas/effects/failed_wells.csv")["sample"].astype(str))
wl = wl[~wl["sample"].isin(fail)]
st = pd.read_csv(f"{data}/gene_panel/results/p53_functional_status.csv"); st["cell_line_id"] = st["cell_line_id"].astype(str)
tot = wl.groupby("sample")[["total_counts", "TRIM72", "CDKN2A", "MTAP"]].sum()
rows = []
for gene, flag in (("CDKN2A", "cdkn2a_deleted"), ("MTAP", "mtap_null"), ("TRIM72", None)):
    ids = st.loc[st[flag].astype(bool), "cell_line_id"] if flag else st.loc[st["cell_name"] == "NCI-H661", "cell_line_id"]
    for cid in ids:
        h = wl[wl["cell_line_id"] == cid].set_index("sample")
        if h.empty:
            continue
        soup = ((tot[gene] - h[gene]) / (tot["total_counts"] - h["total_counts"]) * 1e6).reindex(h.index)
        exp1 = (soup * h["total_counts"] / 1e6).sum()
        rows.append(dict(gene=gene, line=st.set_index("cell_line_id").loc[cid, "cell_name"], umi_per_cell=h["total_counts"].sum() / h["n_cells"].sum(),
                         line_cpm=h[gene].sum() / h["total_counts"].sum() * 1e6, soup_cpm=exp1 / h["total_counts"].sum() * 1e6,
                         det_pct=100 * h[f"det_{gene}"].sum() / h["n_cells"].sum(), rho=h[gene].sum() / exp1))
R = pd.DataFrame(rows)
pd.set_option("display.width", 200)
print(R.round(4).to_string(index=False))
print(R.groupby("gene")["rho"].describe().round(3))
R.to_csv(sys.argv[2], index=False)
