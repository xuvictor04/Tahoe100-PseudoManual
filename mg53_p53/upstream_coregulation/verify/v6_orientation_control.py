#!/usr/bin/env python3
"""Adversarial controls not run by the analysis (needs v1 and v2 first):

 (1) Orientation control for the readthrough reading of F4/F5. Neighbouring genes co-vary for many reasons (shared
     chromatin domain, bidirectional promoters). If the coupling of a low gene to a much stronger neighbour is due to
     readthrough, it should be strongest when the low gene lies DOWNSTREAM of the strong gene on the same strand
     (tandem_down) and weak when the low gene lies UPSTREAM of it on the same strand (tandem_up), or on the other
     strand (convergent / divergent), at the same gap. Pairs: atlas genes, strong gene >= 5 CPM and >= 8x the low
     gene, gap <= 20 kb, no overlap. Ensembl 110 coordinates (Tahoe's annotation era).
     Statistic: r of corrected z across drug-doses (raw, 3 PCs removed) and untreated within-plate Spearman over lines
     (median over 13 reliable plates).
 (2) Composition of TRIM72's top-100 partners (3 PCs removed) by the same orientation classes.
 (3) TP53 mRNA vs TRIM72 across variants, with level-matched percentiles (F9).
 (4) Untreated TRIM72 vs TP53 status / basal p53 activity, recomputed from the v2 sums (F9).

    python3 mg53_p53/upstream_coregulation/verify/v6_orientation_control.py
"""
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu, spearmanr, fisher_exact, kruskal

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from v1_coreg_drugdoses import standardise, FXD, OUT, load_coords  # noqa: E402
from v3_baseline_locus import zr_masked  # noqa: E402

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)
rng = np.random.default_rng(21)


def pairs_table(G, coords, expr_min=5.0, ratio=8.0, near=20_000):
    gm = pd.read_parquet("/home/user/tahoe_data/metadata/gene_metadata.parquet")
    g = G.merge(gm[["token_id", "ensembl_id"]], left_on="token", right_on="token_id", how="left").merge(
        coords, on="ensembl_id", how="left")
    g["i"] = np.arange(len(g))
    g = g[g["chrom"].notna()]
    rows = []
    for c, h in g.groupby("chrom"):
        h = h.sort_values("start")
        st, en, sd = h["start"].to_numpy(int), h["end"].to_numpy(int), h["strand"].to_numpy(int)
        lv, ii = h["pooled_cpm"].to_numpy(float), h["i"].to_numpy(int)
        for a in range(len(h)):                     # a = low gene
            for b in range(max(0, a - 60), min(len(h), a + 61)):   # b = strong gene (neighbours in start order)
                if a == b or lv[b] < expr_min or lv[b] < ratio * lv[a]:
                    continue
                if st[b] < en[a] and en[b] > st[a]:
                    continue                        # overlapping
                if en[b] < st[a]:
                    gap, b_left = st[a] - en[b], True
                else:
                    gap, b_left = st[b] - en[a], False
                if gap > near:
                    continue
                same = sd[a] == sd[b]
                if same:
                    # strong gene upstream of the low gene in the direction of transcription -> tandem_down
                    down = (sd[b] == 1 and b_left) or (sd[b] == -1 and not b_left)
                    conf = "tandem_down (readthrough geometry)" if down else "tandem_up"
                else:
                    # strong gene's 3' end points at the low gene -> convergent
                    conv = (sd[b] == 1 and b_left) or (sd[b] == -1 and not b_left)
                    conf = "convergent" if conv else "divergent"
                rows.append((ii[a], ii[b], conf, gap))
    return pd.DataFrame(rows, columns=["low", "strong", "config", "gap"])


def main():
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    gi = np.flatnonzero((genes["kind"] == "gene").to_numpy())
    G = genes.iloc[gi].reset_index(drop=True)
    sym = G["symbol"].astype(str).to_numpy()
    pos = {s: i for i, s in enumerate(sym)}
    t = pos["TRIM72"]
    lvl = G["pooled_cpm"].to_numpy(float)
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    for c in ("unreliable_plate_only", "position_not_correctable"):
        dd[c] = dd[c].astype(str).str.lower().eq("true")
    keep = ~(dd["unreliable_plate_only"] | dd["position_not_correctable"]).to_numpy()
    Z = np.nan_to_num(np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r"))[keep][:, gi].astype(np.float64))
    n = Z.shape[0]
    Xs = standardise(Z)
    U, S, Vt = np.linalg.svd(Xs, full_matrices=False)
    X = {"raw": Xs, "minus3pc": standardise(Xs - (U[:, :3] * S[:3]) @ Vt[:3]),
         "minus10pc": standardise(Xs - (U[:, :10] * S[:10]) @ Vt[:10])}
    del U, Vt
    q = np.load(os.path.join(OUT, "v2_cache", "plate_line_quiet.npz"))
    info = json.load(open(os.path.join(FXD, "info.json")))
    use = [i for i, p in enumerate(q["plates"]) if p not in info["unreliable_plates"]]
    tok = G["token"].astype(int).to_numpy()
    cnt = q["counts"][use][:, :, tok].astype(np.float64)
    tot = q["total"][use]
    okl = tot > 0
    nl = okl.sum(axis=1).astype(float)
    ZB = zr_masked(np.log2((cnt + 0.5) / np.where(okl, tot, 1.0)[:, :, None] * 1e6), okl)
    del cnt

    # ---------------- (1) orientation control
    e110 = load_coords(os.path.join(HERE, "ext_download", "ensembl110_genes.tsv"))
    PT = pairs_table(G, e110)
    a_, b_ = PT["low"].to_numpy(), PT["strong"].to_numpy()
    for k, Xk in X.items():
        PT[f"r_{k}"] = (Xk[:, a_] * Xk[:, b_]).sum(axis=0) / n
    PT["rho_untreated"] = np.median(np.einsum("plg,plg->pg", ZB[:, :, a_], ZB[:, :, b_]) / nl[:, None], axis=0)
    PT["low_gene"], PT["strong_gene"] = sym[a_], sym[b_]
    PT["gap_bin"] = pd.cut(PT["gap"], [-1, 5000, 10000, 20000], labels=["0-5kb", "5-10kb", "10-20kb"])
    PT.to_csv(os.path.join(OUT, "v6_neighbour_pairs.csv"), index=False, float_format="%.4g")
    rows = []
    ref = "tandem_down (readthrough geometry)"
    for stat in ("r_raw", "r_minus3pc", "r_minus10pc", "rho_untreated"):
        for conf, h in PT.groupby("config"):
            rec = {"statistic": stat, "config": conf, "n_pairs": len(h), "median": h[stat].median(),
                   "mean": h[stat].mean()}
            for gb, hh in h.groupby("gap_bin", observed=True):
                rec[f"median_{gb}"] = hh[stat].median()
            if conf != ref:
                rr = PT.loc[PT["config"] == ref, stat]
                rec["MWU_p_vs_tandem_down"] = mannwhitneyu(rr, h[stat]).pvalue
            rows.append(rec)
    OC = pd.DataFrame(rows)
    OC.to_csv(os.path.join(OUT, "v6_orientation_control.csv"), index=False, float_format="%.4g")
    print("(1) neighbour pairs (low gene vs >= 8x stronger neighbour <= 20 kb), by orientation:")
    print(OC.round(4).to_string())
    print(PT[(PT["low_gene"] == "TRIM72")].to_string())

    # ---------------- (2) TRIM72's top-100 partners by orientation class
    cls = {}
    for conf in PT["config"].unique():
        cls[conf] = set(PT.loc[PT["config"] == conf, "low"])
    rows = []
    for k, Xk in X.items():
        r = (Xk[:, t] @ Xk) / n
        r[t] = -np.inf
        top = np.argsort(-r)[:100]
        rec = {"variant": k}
        for conf, s in cls.items():
            in_top = np.isin(top, list(s)).sum()
            rec[f"top100_n_{conf}"] = int(in_top)
            rec[f"all_pct_{conf}"] = 100 * len(s) / len(sym)
        # level-matched comparison: genes within 2x of TRIM72's level
        rows.append(rec)
    CT = pd.DataFrame(rows)
    CT.to_csv(os.path.join(OUT, "v6_top100_by_orientation.csv"), index=False, float_format="%.4g")
    print("(2) TRIM72 top-100 partners by orientation class of the gene (a gene can be in several):")
    print(CT.T.to_string())

    # ---------------- (3) TP53 mRNA vs TRIM72, level-matched percentile, per variant
    lp = np.log2(np.maximum(G["median_line_cpm"].to_numpy(float), 1e-6))
    rows = []
    for k, Xk in X.items():
        r = (Xk[:, t] @ Xk) / n
        for gname in ("TP53", "MDM2", "CDKN1A", "FUS", "FNDC7", "PYGM", "ATF3", "FOSB"):
            j = pos[gname]
            m = (np.abs(lp - lp[j]) <= 1) & (np.arange(len(sym)) != t)
            rows.append({"variant": k, "gene": gname, "r": r[j], "pct_level_within2x": 100 * (r[m] < r[j]).mean(),
                         "pct_all_genes": 100 * (r < r[j]).mean(), "n_level_genes": int(m.sum())})
    TP = pd.DataFrame(rows)
    TP.to_csv(os.path.join(OUT, "v6_TP53_and_key_partners_r.csv"), index=False, float_format="%.4g")
    print("(3)")
    print(TP.round(3).to_string())

    # ---------------- (4) untreated TRIM72 vs TP53 status and basal p53 activity
    zt = np.where(okl, ZB[:, :, t], np.nan)
    lines = list(q["lines"])
    tline = pd.Series(np.nanmedian(zt, axis=0), index=lines, name="TRIM72_within_plate_z_median")
    cpm = np.log2((q["counts"][use][:, :, int(G["token"].iloc[t])] + 0.5) / np.where(okl, tot, 1.0) * 1e6)
    cpm = np.where(okl, cpm, np.nan)
    cpm_c = cpm - np.nanmean(cpm, axis=1, keepdims=True)
    tl2 = pd.Series(np.nanmedian(cpm_c, axis=0), index=lines, name="TRIM72_log2cpm_vs_plate_mean")
    fs = pd.read_csv("/home/user/tahoe_data/gene_panel/results/p53_functional_status.csv").set_index("cell_line_id")
    bl = pd.read_csv("/home/user/tahoe_data/gene_panel/results/baseline_by_cell_line.csv").set_index("cell_line_id")
    D = pd.concat([tline, tl2], axis=1).join(fs[["organ", "basal_p53_activity_log2", "p53_responsiveness_log2"]])
    D = D.join(bl[["tp53_group"]] if "tp53_group" in bl else None)
    rows = []
    wt = D["tp53_group"].astype(str).str.upper().str.startswith("WT")
    for col in ("TRIM72_within_plate_z_median", "TRIM72_log2cpm_vs_plate_mean"):
        p = mannwhitneyu(D.loc[wt, col], D.loc[~wt, col]).pvalue
        rows.append({"test": f"{col}: TP53 WT vs altered (Mann-Whitney)", "n1": int(wt.sum()), "n2": int((~wt).sum()),
                     "estimate": D.loc[wt, col].median() - D.loc[~wt, col].median(), "p": p})
        for v in ("basal_p53_activity_log2", "p53_responsiveness_log2"):
            m = D[v].notna()
            rr, pp = spearmanr(D.loc[m, col], D.loc[m, v])
            rows.append({"test": f"{col} vs {v} (Spearman)", "n1": int(m.sum()), "estimate": rr, "p": pp})
        org = D["organ"].fillna("other")
        vc = org.value_counts()
        org = org.where(org.map(vc) >= 3, "other")
        H, pk = kruskal(*[D.loc[org == o, col] for o in org.unique()])
        rows.append({"test": f"{col} by organ (Kruskal-Wallis)", "n1": len(D), "estimate": H, "p": pk})
    F9 = pd.DataFrame(rows)
    F9.to_csv(os.path.join(OUT, "v6_F9_untreated_p53.csv"), index=False, float_format="%.4g")
    print("(4)")
    print(F9.to_string())


if __name__ == "__main__":
    main()
