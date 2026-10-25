#!/usr/bin/env python3
"""F5 check: do readthrough-exposed genes track their upstream same-strand gene (across drug-doses and untreated
across lines), with Ensembl 110 classes (Tahoe's annotation era) as well as Ensembl 116, against level-matched random
partners on another chromosome? Needs out/v1_dog_classes_E116_vs_E110.csv and out/v2_cache (v1, v2 first).

    python3 mg53_p53/upstream_coregulation/verify/v5_dog_pairs.py
"""
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from v1_coreg_drugdoses import standardise, FXD, OUT, load_coords  # noqa: E402
from v3_baseline_locus import zr_masked  # noqa: E402

rng = np.random.default_rng(9)


def main():
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    gi = np.flatnonzero((genes["kind"] == "gene").to_numpy())
    G = genes.iloc[gi].reset_index(drop=True)
    sym = G["symbol"].astype(str).to_numpy()
    tokens = G["token"].astype(int).to_numpy()
    plvl = G["pooled_cpm"].to_numpy()
    v1 = pd.read_csv(os.path.join(OUT, "v1_dog_classes_E116_vs_E110.csv"))
    e110 = load_coords(os.path.join(HERE, "ext_download", "ensembl110_genes.tsv"))
    gm = pd.read_parquet("/home/user/tahoe_data/metadata/gene_metadata.parquet")
    chrom = G.merge(gm[["token_id", "ensembl_id"]], left_on="token", right_on="token_id", how="left").merge(
        e110[["ensembl_id", "chrom"]], on="ensembl_id", how="left")["chrom"].astype(str).to_numpy()
    pos = {s: i for i, s in enumerate(sym)}
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    for c in ("unreliable_plate_only", "position_not_correctable"):
        dd[c] = dd[c].astype(str).str.lower().eq("true")
    keep = ~(dd["unreliable_plate_only"] | dd["position_not_correctable"]).to_numpy()
    Z = np.nan_to_num(np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r"))[keep][:, gi].astype(np.float64))
    Xs = standardise(Z)
    U, S, Vt = np.linalg.svd(Xs, full_matrices=False)
    X3 = standardise(Xs - (U[:, :3] * S[:3]) @ Vt[:3])
    # untreated: within-plate z-ranks over lines of log CPM (quiet wells, reliable plates), atlas genes
    q = np.load(os.path.join(OUT, "v2_cache", "plate_line_quiet.npz"))
    info = json.load(open(os.path.join(FXD, "info.json")))
    use = [i for i, p in enumerate(q["plates"]) if p not in info["unreliable_plates"]]
    cnt = q["counts"][use][:, :, tokens].astype(np.float64)
    tot = q["total"][use]
    okl = tot > 0
    nl = okl.sum(axis=1).astype(float)
    ZB = zr_masked(np.log2((cnt + 0.5) / np.where(okl, tot, 1.0)[:, :, None] * 1e6), okl)     # P x L x genes
    del cnt
    rows = []
    for lab in ("E116", "E110"):
        cl = v1[f"class_{lab}"].to_numpy()
        up = v1[f"up_gene_{lab}"].fillna("").to_numpy()
        gp = np.array([i for i in range(len(sym)) if cl[i] == "sense_exposed" and up[i] in pos])
        upi = np.array([pos[up[i]] for i in gp])
        rpart = np.zeros((len(gp), 20), dtype=int)
        lp = np.log2(np.maximum(plvl, 1e-6))
        for k, (g_, u_) in enumerate(zip(gp, upi)):
            w_ = 1.0
            c_ = np.flatnonzero((np.abs(lp - lp[u_]) <= w_) & (chrom != chrom[g_]))
            while c_.size < 20:
                w_ += 0.5
                c_ = np.flatnonzero((np.abs(lp - lp[u_]) <= w_) & (chrom != chrom[g_]))
            rpart[k] = rng.choice(c_, 20, replace=False)
        for nm, X in (("drugdoses_raw", Xs), ("drugdoses_minus3pc", X3)):
            n = X.shape[0]
            obs = (X[:, gp] * X[:, upi]).sum(axis=0) / n
            rnd = np.stack([(X[:, gp] * X[:, rpart[:, j]]).sum(axis=0) / n for j in range(20)], axis=1)
            d = obs - np.median(rnd, axis=1)
            rows.append({"annotation": lab, "data": nm, "n_pairs": len(gp), "median_r_pair": np.median(obs),
                         "median_r_random": np.median(rnd), "pct_pairs_above_random": 100 * (d > 0).mean(),
                         "wilcoxon_p": wilcoxon(d).pvalue})
        bo = np.median(np.einsum("plg,plg->pg", ZB[:, :, gp], ZB[:, :, upi]) / nl[:, None], axis=0)
        br = np.stack([np.median(np.einsum("plg,plg->pg", ZB[:, :, gp], ZB[:, :, rpart[:, j]]) / nl[:, None], axis=0)
                       for j in range(20)], axis=1)
        d = bo - np.median(br, axis=1)
        rows.append({"annotation": lab, "data": "untreated_lines_within_plate", "n_pairs": len(gp),
                     "median_r_pair": np.median(bo), "median_r_random": np.median(br),
                     "pct_pairs_above_random": 100 * (d > 0).mean(), "wilcoxon_p": wilcoxon(d).pvalue})
    t, f = pos["TRIM72"], pos["FUS"]
    rt = {"drugdoses_raw": (Xs[:, t] @ Xs[:, f]) / Xs.shape[0], "drugdoses_minus3pc": (X3[:, t] @ X3[:, f]) / X3.shape[0],
          "untreated_lines_within_plate": float(np.median((ZB[:, :, t] * ZB[:, :, f]).sum(axis=1) / nl))}
    for k, v in rt.items():
        rows.append({"annotation": "-", "data": k, "n_pairs": 1, "median_r_pair": v, "note": "TRIM72-FUS"})
    R = pd.DataFrame(rows)
    pd.set_option("display.width", 250)
    print(R.to_string())
    R.to_csv(os.path.join(OUT, "v5_dog_pairs.csv"), index=False, float_format="%.4g")


if __name__ == "__main__":
    main()
