#!/usr/bin/env python3
"""Part 4: small count checks of quoted numbers (lines up, pooled reads) from the analysis's per-line table and raw
panel counts. Usage: python3 verify_part4.py"""
import os
import numpy as np
import pandas as pd

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
TAB = os.path.join(os.path.dirname(HERE), "tables")
pl = pd.read_csv(f"{TAB}/per_line_effects_selected.csv")
rows = []
for drug, conc in [("Idarubicin (hydrochloride)", 5.0), ("Selinexor", 5.0), ("Epirubicin (hydrochloride)", 5.0)]:
    x = pl[(pl.drug == drug) & np.isclose(pl.conc, conc) & (pl.scope == "mean of used wells") & (pl.gene == "TRIM72")]
    up = (x.z_line > 2) & (x.fold_change > 1.2)
    for g in ["WT", "altered"]:
        m = x.tp53_group == g
        rows.append(dict(drug=drug, conc=conc, group=g, n=int(m.sum()), n_up=int((up & m).sum()),
                         lines_not_up=", ".join(x.loc[m & ~up, "cell_name"])))
print(pd.DataFrame(rows).to_string(index=False))

smap = pd.read_csv(f"{DATA}/gene_panel/sample_map.csv")
wl = pd.read_parquet(f"{DATA}/gene_panel/well_line.parquet", columns=["sample", "cell_line_id", "n_cells", "total_counts", "TRIM72"])
base = pd.read_csv(f"{DATA}/gene_panel/results/baseline_by_cell_line.csv").set_index("cell_line_id")
wl["grp"] = wl.cell_line_id.map(base.tp53_group)
for s in ["smp_2010", "smp_2778"]:
    w = wl[(wl["sample"] == s) & (wl.n_cells >= 30) & (wl.cell_line_id != "CVCL_1577")]
    g = w.groupby("grp")[["TRIM72", "total_counts"]].sum()
    g["cpm"] = 1e6 * g.TRIM72 / g.total_counts
    print(s, g.round(2).to_dict())
