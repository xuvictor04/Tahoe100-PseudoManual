#!/usr/bin/env python3
"""F8 check: are the AP-1 / stress TFs that track TRIM72 (3 PCs removed) robust within each plate group, and what
do the muscle sets do across drug-doses? Level-matched set tests recomputed from the atlas DD_z.

    python3 mg53_p53/upstream_coregulation/verify/v4_f8_tf_sets.py
"""
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from v1_coreg_drugdoses import standardise, FXD, OUT  # noqa: E402

SETS = {"AP1_IEG": ["FOS", "FOSB", "JUN", "JUNB", "EGR1", "EGR2", "EGR3", "ATF3", "IER2", "NR4A1"],
        "MUSCLE_TF": ["MYOD1", "MYOG", "MYF5", "MYF6", "MEF2A", "MEF2B", "MEF2C", "MEF2D", "SRF", "MYOCD"],
        "MUSCLE_STRUCTURAL": ["ACTA1", "CKM", "MYH3", "DES", "TNNT1", "TNNT2", "CAV3", "RYR1", "ATP2A1", "DYSF", "MYL11",
                              "MSTN"],
        "F8_listed_TFs": ["FOSB", "FOS", "POU2F2", "NFATC1", "GTF2B", "AHRR", "ATF3", "CSRNP2", "EGR3", "IRF1"]}
rng = np.random.default_rng(3)


def main():
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    gi = np.flatnonzero((genes["kind"] == "gene").to_numpy())
    G = genes.iloc[gi].reset_index(drop=True)
    sym = G["symbol"].astype(str).to_numpy()
    lvl = G["median_line_cpm"].to_numpy()
    t = int(np.flatnonzero(sym == "TRIM72")[0])
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    for c in ("unreliable_plate_only", "position_not_correctable"):
        dd[c] = dd[c].astype(str).str.lower().eq("true")
    keep = ~(dd["unreliable_plate_only"] | dd["position_not_correctable"]).to_numpy()
    ddk = dd[keep].reset_index(drop=True)
    Z = np.nan_to_num(np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r"))[keep][:, gi].astype(np.float64))
    pl = ddk["plates"].astype(str)
    subsets = {"all": np.ones(len(ddk), dtype=bool),
               "plates4to12_single_plate_only": pl.isin([f"plate{i}" for i in range(4, 13)]).to_numpy(),
               "plates1to3_only": pl.isin(["plate1", "plate2", "plate3"]).to_numpy()}
    rows, gene_rows = [], []
    for sname, m in subsets.items():
        Xs = standardise(Z[m])
        U, S, Vt = np.linalg.svd(Xs, full_matrices=False)
        for k in (0, 3, 10):
            Xk = standardise(Xs - (U[:, :k] * S[:k]) @ Vt[:k]) if k else Xs
            r = (Xk[:, t] @ Xk) / Xk.shape[0]
            for nm, members in SETS.items():
                idx = [int(np.flatnonzero(sym == g)[0]) for g in members if (sym == g).any()]
                pools = []
                for i in idx:
                    d_ = np.abs(np.log2(np.maximum(lvl, 1e-6)) - np.log2(lvl[i]))
                    pools.append(np.flatnonzero((d_ <= 1) & ~np.isin(np.arange(len(lvl)), idx + [t])))
                null = np.stack([r[rng.choice(p_, 4000)] for p_ in pools], axis=1).mean(axis=1)
                obs = r[idx].mean()
                rows.append({"subset": sname, "n_drugdoses": int(m.sum()), "pcs_removed": k, "set": nm,
                             "n_genes": len(idx), "mean_r": obs, "null_mean": null.mean(),
                             "z": (obs - null.mean()) / null.std(),
                             "p_two_sided": (1 + (np.abs(null - null.mean()) >= abs(obs - null.mean())).sum()) / 4001,
                             "genes": ", ".join(f"{sym[i]} {r[i]:+.2f}" for i in idx)})
            for g in [g_ for g_ in SETS["F8_listed_TFs"] + ["PYGM", "ACTA1", "ATP2A1"] if (sym == g_).any()]:
                j = int(np.flatnonzero(sym == g)[0])
                gene_rows.append({"subset": sname, "pcs_removed": k, "gene": g, "r": r[j]})
    R = pd.DataFrame(rows)
    R.to_csv(os.path.join(OUT, "v4_set_tests_by_plate_group.csv"), index=False, float_format="%.4g")
    pd.set_option("display.width", 250)
    pd.set_option("display.max_colwidth", 140)
    print(R.drop(columns=["genes"]).to_string())
    print(R[R["set"].isin(["MUSCLE_STRUCTURAL"])][["subset", "pcs_removed", "genes"]].to_string())
    GR = pd.DataFrame(gene_rows).pivot_table(index="gene", columns=["subset", "pcs_removed"], values="r")
    GR.to_csv(os.path.join(OUT, "v4_listed_TFs_r_by_plate_group.csv"), float_format="%.3f")
    print(GR.round(2).to_string())


if __name__ == "__main__":
    main()
