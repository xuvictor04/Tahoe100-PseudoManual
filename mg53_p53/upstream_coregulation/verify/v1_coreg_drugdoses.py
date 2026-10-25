#!/usr/bin/env python3
"""Adversarial check of the drug-dose co-regulation claims (F4, F5, F8, F9, F12 and part of F3) of
upstream_coregulation.py, recomputed independently from the atlas DD_z / DD_lfc (method v3).

    python3 mg53_p53/upstream_coregulation/verify/v1_coreg_drugdoses.py

Reads only /home/user/tahoe_data/atlas/effects (read-only) and two coordinate tables:
  ../external/ensembl_biomart_genes_GRCh38.tsv  (Ensembl 116, as the analysis used)
  ext_download/ensembl110_genes.tsv              (Ensembl 110 / Jul 2023 BioMart archive, closest to Tahoe's annotation:
                                                  it holds all but 17 of Tahoe's 62,710 gene ids; Ensembl 116 misses 1,282)
Writes out/v1_*.csv only.
"""
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import rankdata, fisher_exact, spearmanr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, REPO)
FXD = "/home/user/tahoe_data/atlas/effects"
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(11)


def load_coords(path):
    b = pd.read_csv(path, sep="\t", dtype={"Chromosome/scaffold name": str})
    b = b.iloc[:, :7]
    b.columns = ["ensembl_id", "ens_name", "chrom", "start", "end", "strand", "biotype"]
    prim = [str(i) for i in range(1, 23)] + ["X", "Y"]
    return b[b["chrom"].isin(prim)].drop_duplicates("ensembl_id")


def dog_classes(genes, coords, expr_min=5.0, near=20_000, far=100_000, ratio=8.0):
    """Own implementation of the analysis's rule: sense_exposed = an expressed (atlas pooled CPM >= 5) same-strand gene
    ends <= 20 kb upstream of the gene's start (no overlap with any expressed same-strand gene) and is >= 8x its level;
    unexposed = no expressed same-strand gene within 100 kb upstream or overlapping, no convergent expressed
    opposite-strand gene within 100 kb downstream; antisense_exposed_only; other."""
    gm = pd.read_parquet("/home/user/tahoe_data/metadata/gene_metadata.parquet")
    g = genes.merge(gm[["token_id", "ensembl_id"]], left_on="token", right_on="token_id", how="left")
    g = g.merge(coords, on="ensembl_id", how="left")
    cls = np.full(len(g), "no coordinates", dtype=object)
    up_name = np.full(len(g), "", dtype=object)
    up_dist = np.full(len(g), np.nan)
    has = g["chrom"].notna().to_numpy()
    E = g[has & (g["pooled_cpm"] >= expr_min).to_numpy()]
    idx = {}
    for (c, s), v in E.groupby(["chrom", "strand"]):
        idx[(c, s)] = (v["start"].to_numpy(), v["end"].to_numpy(), v["pooled_cpm"].to_numpy(),
                       v["symbol"].to_numpy(), v["col"].to_numpy())
    for i in np.flatnonzero(has):
        r = g.iloc[i]
        s = int(r.strand)
        st, en, cpm, col = int(r.start), int(r.end), float(r.pooled_cpm), int(r.col)
        same = idx.get((r.chrom, s))
        opp = idx.get((r.chrom, -s))
        overl = False
        ud = np.inf
        ucpm = np.nan
        if same is not None:
            S, En, C, N, Co = same
            overl = bool(((S < en) & (En > st) & (Co != col)).any())
            if s == 1:
                m = En < st
                if m.any():
                    k = np.flatnonzero(m)[np.argmax(En[m])]
                    ud, ucpm, up_name[i] = st - En[k], C[k], N[k]
            else:
                m = S > en
                if m.any():
                    k = np.flatnonzero(m)[np.argmin(S[m])]
                    ud, ucpm, up_name[i] = S[k] - en, C[k], N[k]
        cd = np.inf
        ccpm = np.nan
        if opp is not None:
            S, En, C, N, Co = opp
            if s == 1:
                m = S > en
                if m.any():
                    k = np.flatnonzero(m)[np.argmin(S[m])]
                    cd, ccpm = S[k] - en, C[k]
            else:
                m = En < st
                if m.any():
                    k = np.flatnonzero(m)[np.argmax(En[m])]
                    cd, ccpm = st - En[k], C[k]
        up_dist[i] = ud if np.isfinite(ud) else np.nan
        no_up = (ud > far) and not overl
        if ud <= near and ucpm / cpm >= ratio and not overl:
            cls[i] = "sense_exposed"
        elif no_up and cd <= near and ccpm / cpm >= ratio:
            cls[i] = "antisense_exposed_only"
        elif no_up and cd > far:
            cls[i] = "unexposed"
        else:
            cls[i] = "other"
    return pd.DataFrame({"col": g["col"].to_numpy(), "class": cls, "up_gene": up_name, "up_dist": up_dist})


def standardise(X):
    X = X - X.mean(axis=0)
    sd = X.std(axis=0)
    sd[sd == 0] = 1
    return X / sd


_SVD = {}


def remove_pcs(Xs, k):
    if k == 0:
        return Xs
    key = (Xs.shape, float(Xs[:5, :5].sum()))
    if key not in _SVD:
        _SVD.clear()
        _SVD[key] = np.linalg.svd(Xs, full_matrices=False)
    U, S, Vt = _SVD[key]
    return standardise(Xs - (U[:, :k] * S[:k]) @ Vt[:k])


def corr_with(Xs, t):
    y = Xs[:, t]
    return (y @ Xs) / Xs.shape[0]


def main():
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    gi = np.flatnonzero((genes["kind"] == "gene").to_numpy())
    G = genes.iloc[gi].reset_index(drop=True)
    sym = G["symbol"].astype(str).to_numpy()
    t = int(np.flatnonzero(sym == "TRIM72")[0])
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    for c in ("unreliable_plate_only", "position_not_correctable"):
        dd[c] = dd[c].astype(str).str.lower().eq("true")
    keep = ~(dd["unreliable_plate_only"] | dd["position_not_correctable"]).to_numpy()
    ddk = dd[keep].reset_index(drop=True)
    Zall = np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r"))[keep][:, gi].astype(np.float64)
    Lall = np.asarray(np.load(os.path.join(FXD, "DD_lfc.npy"), mmap_mode="r"))[keep][:, gi].astype(np.float64)
    nan_frac = np.isnan(Zall).mean(axis=0)
    print(f"{Zall.shape[0]} drug-doses x {len(gi)} genes; TRIM72 NaN z: {np.isnan(Zall[:, t]).sum()}; "
          f"genes with any NaN z: {(nan_frac > 0).sum()}, median NaN frac among them {np.median(nan_frac[nan_frac > 0]) if (nan_frac > 0).any() else 0:.3f}")
    Z = np.nan_to_num(Zall)
    L = np.nan_to_num(Lall)
    n = Z.shape[0]

    # ---- DoG classes with both annotations
    e116 = load_coords(os.path.join(os.path.dirname(HERE), "external", "ensembl_biomart_genes_GRCh38.tsv"))
    e110 = load_coords(os.path.join(HERE, "ext_download", "ensembl110_genes.tsv"))
    C116 = dog_classes(G, e116).set_index("col").reindex(G["col"])
    C110 = dog_classes(G, e110).set_index("col").reindex(G["col"])
    cls116 = C116["class"].to_numpy()
    cls110 = C110["class"].to_numpy()
    # compare with the analysis's own class table
    theirs = pd.read_csv(os.path.join(os.path.dirname(HERE), "tables", "c_DoG_gene_exposure_classes.csv"),
                         usecols=["col", "class"]).set_index("col").reindex(G["col"])["class"].fillna("no coordinates")
    agree = float((theirs.to_numpy() == cls116).mean())
    print(f"DoG classes: my E116 re-implementation agrees with the analysis's table for {100 * agree:.2f}% of genes")
    print("E116 class counts", pd.Series(cls116).value_counts().to_dict())
    print("E110 class counts", pd.Series(cls110).value_counts().to_dict())
    print("TRIM72 class E116:", cls116[t], C116["up_gene"].iloc[t], C116["up_dist"].iloc[t],
          "| E110:", cls110[t], C110["up_gene"].iloc[t], C110["up_dist"].iloc[t])
    cls_tab = pd.DataFrame({"gene": sym, "class_E116": cls116, "class_E110": cls110,
                            "up_gene_E116": C116["up_gene"].to_numpy(), "up_dist_E116": C116["up_dist"].to_numpy(),
                            "up_gene_E110": C110["up_gene"].to_numpy(), "up_dist_E110": C110["up_dist"].to_numpy(),
                            "class_analysis_table": theirs.to_numpy()})
    cls_tab.to_csv(os.path.join(OUT, "v1_dog_classes_E116_vs_E110.csv"), index=False)
    print("class change E116 -> E110:\n", pd.crosstab(cls_tab["class_E116"], cls_tab["class_E110"]))

    # ---- variants
    ida = ddk["drug"].str.startswith("Idarubicin").to_numpy()
    top10_t = np.argsort(-Z[:, t])[:10]
    rms = np.sqrt((Z ** 2).mean(axis=1))
    top10_g = np.argsort(-rms)[:10]
    pl = ddk["plates"].astype(str)
    p412 = pl.isin([f"plate{i}" for i in range(4, 13)]).to_numpy()
    p13 = pl.isin(["plate1", "plate2", "plate3"]).to_numpy()
    allm = np.ones(n, dtype=bool)
    print("top-10 TRIM72 drug-doses:", "; ".join(f"{ddk.drug[i]} {ddk.conc[i]:g}" for i in top10_t))
    print("top-10 global (RMS z) drug-doses:", "; ".join(f"{ddk.drug[i]} {ddk.conc[i]:g}" for i in top10_g))
    subsets = {"all": allm, "drop_top10_TRIM72": ~np.isin(np.arange(n), top10_t),
               "drop_top10_global_rmsz": ~np.isin(np.arange(n), top10_g), "drop_idarubicin_all_doses": ~ida,
               "plates4to12_single_plate_only": p412, "plates1to3_only": p13}
    R = {}
    for sname, m in subsets.items():
        Xs = standardise(Z[m])
        for k in (0, 1, 3, 10):
            Xk = remove_pcs(Xs, k)
            R[(sname, f"pearson_minus{k}pc")] = corr_with(Xk, t)
            if sname == "all" or k in (0, 3):
                R[(sname, f"spearman_minus{k}pc")] = corr_with(standardise(rankdata(Xk, axis=0)), t)
        if sname == "all":
            R[(sname, "pearson_lfc_raw")] = corr_with(standardise(L[m]), t)
        print("done subset", sname, int(m.sum()))
    ref0 = R[("all", "pearson_minus0pc")]
    ref3 = R[("all", "pearson_minus3pc")]

    def topk(r, k):
        rr = r.copy()
        rr[t] = -np.inf
        return np.argsort(-rr)[:k]

    # level-matched null for the DoG share of the top-100 (E110 and E116), for the 'all' variants
    lvl = G["median_line_cpm"].to_numpy()
    cand = np.flatnonzero((lvl >= lvl[t] / 2) & (lvl <= lvl[t] * 2) & (G["n_lines_expressing"] >= 45).to_numpy() &
                          (np.arange(len(gi)) != t))
    rnd = rng.choice(cand, size=min(300, cand.size), replace=False)
    rows = []
    focus = ["FUS", "ATF3", "PMAIP1", "TFRC", "CXCL8", "ABCB1", "TP53", "BTG2", "AIM2", "FOSB", "FOS", "FNDC7", "PYGM",
             "VWCE", "FGF18", "SEMA4A", "MIR9-1HG", "LDHC", "SELPLG"]
    for (sname, vname), r in R.items():
        rr = r.copy()
        rr[t] = -np.nan
        rank = pd.Series(-np.where(np.arange(len(r)) == t, -np.inf, r)).rank(method="min").to_numpy()
        t20, t50, t100 = topk(r, 20), topk(r, 50), topk(r, 100)
        rec = {"subset": sname, "variant": vname, "n_drugdoses": int(subsets[sname].sum()),
               "top10": ", ".join(sym[t20[:10]]),
               "overlap_top20_with_all_pearson_raw": len(set(t20) & set(topk(ref0, 20))),
               "overlap_top100_with_all_pearson_raw": len(set(t100) & set(topk(ref0, 100))),
               "overlap_top100_with_all_pearson_minus3pc": len(set(t100) & set(topk(ref3, 100))),
               "spearman_r_vector_vs_all_pearson_raw": spearmanr(np.delete(r, t), np.delete(ref0, t))[0],
               "spearman_r_vector_vs_all_pearson_minus3pc": spearmanr(np.delete(r, t), np.delete(ref3, t))[0],
               "top100_pct_sense_exposed_E116": 100 * float((cls116[t100] == "sense_exposed").mean()),
               "top100_pct_sense_exposed_E110": 100 * float((cls110[t100] == "sense_exposed").mean()),
               "n_absr_ge_0.3": int((np.abs(np.delete(r, t)) >= 0.3).sum())}
        for f in focus:
            j = int(np.flatnonzero(sym == f)[0])
            rec[f"r_{f}"] = r[j]
            rec[f"rank_{f}"] = int(rank[j])
        rows.append(rec)
    rob = pd.DataFrame(rows)
    rob.to_csv(os.path.join(OUT, "v1_coreg_robustness.csv"), index=False, float_format="%.4g")
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    print(rob[["subset", "variant", "n_drugdoses", "overlap_top20_with_all_pearson_raw",
               "overlap_top100_with_all_pearson_raw", "overlap_top100_with_all_pearson_minus3pc",
               "spearman_r_vector_vs_all_pearson_minus3pc", "top100_pct_sense_exposed_E116",
               "top100_pct_sense_exposed_E110", "r_FUS", "rank_FUS", "r_ATF3", "r_PMAIP1", "r_TP53"]].to_string())
    print(rob[["subset", "variant", "top10"]].to_string())

    # null: DoG share in the top-100 partners of 300 level-matched genes ('all', Pearson raw / minus 3 PCs / 10 PCs)
    nul = []
    sense110 = cls110 == "sense_exposed"
    sense116 = cls116 == "sense_exposed"
    Xs = standardise(Z)
    for k in (0, 3, 10):
        Xk = remove_pcs(Xs, k)
        r_t = corr_with(Xk, t)
        Rr = (Xk[:, rnd].T @ Xk) / n
        Rr[np.arange(len(rnd)), rnd] = -np.inf
        Rr[:, t] = -np.inf
        tops = np.argsort(-Rr, axis=1)[:, :100]
        f110 = sense110[tops].mean(axis=1) * 100
        f116 = sense116[tops].mean(axis=1) * 100
        tt = topk(r_t, 100)
        o110 = 100 * sense110[tt].mean()
        o116 = 100 * sense116[tt].mean()
        nul.append({"variant": f"pearson_minus{k}pc", "TRIM72_top100_pct_DoG_E116": o116,
                    "matched_median_E116": np.median(f116), "TRIM72_pctile_E116": 100 * np.mean(f116 < o116),
                    "TRIM72_top100_pct_DoG_E110": o110, "matched_median_E110": np.median(f110),
                    "TRIM72_pctile_E110": 100 * np.mean(f110 < o110),
                    "matched_DoG_exposed_E110_median": float(np.median(f110[sense110[rnd]])) if sense110[rnd].any() else np.nan,
                    "TRIM72_pctile_vs_matched_DoG_exposed_E110": float(100 * np.mean(f110[sense110[rnd]] < o110)) if sense110[rnd].any() else np.nan,
                    "n_matched": len(rnd), "n_matched_DoG_exposed_E110": int(sense110[rnd].sum()),
                    "TRIM72_n_absr_ge_0.3": int((np.abs(np.delete(r_t, t)) >= 0.3).sum()),
                    "matched_median_n_absr_ge_0.3": float(np.median((np.abs(np.where(np.isfinite(Rr), Rr, 0)) >= 0.3).sum(axis=1)))})
        # Fisher (F4): low genes (<= 10 CPM) with r >= 0.4 : sense_exposed vs unexposed
        low = lvl <= 10
        for lab, cl in (("E116", cls116), ("E110", cls110)):
            sel = low & np.isin(cl, ["sense_exposed", "unexposed"]) & (np.arange(len(gi)) != t)
            mod = r_t >= 0.4
            a = int((sel & mod & (cl == "sense_exposed")).sum())
            b = int((sel & mod & (cl == "unexposed")).sum())
            c = int((sel & ~mod & (cl == "sense_exposed")).sum())
            d = int((sel & ~mod & (cl == "unexposed")).sum())
            orr, p = fisher_exact([[a, b], [c, d]])
            nul[-1][f"fisher_{lab}_module_exposed"] = f"{a}/{a + b}"
            nul[-1][f"fisher_{lab}_rest_pct_exposed"] = 100 * c / max(c + d, 1)
            nul[-1][f"fisher_{lab}_OR"] = orr
            nul[-1][f"fisher_{lab}_p"] = p
    nul = pd.DataFrame(nul)
    nul.to_csv(os.path.join(OUT, "v1_dog_share_null.csv"), index=False, float_format="%.4g")
    print(nul.T.to_string())

    # ---- F5: TRIM72 vs FUS across drug-doses, and percentile among genes of FUS's level
    f = int(np.flatnonzero(sym == "FUS")[0])
    plvl = G["pooled_cpm"].to_numpy()
    cf = np.flatnonzero((plvl >= plvl[f] / 2) & (plvl <= plvl[f] * 2))
    out5 = []
    for k in (0, 3, 10):
        r = corr_with(remove_pcs(Xs, k), t)
        out5.append({"variant": f"minus{k}pc", "r_TRIM72_FUS": r[f], "n_FUS_level_genes": cf.size,
                     "pctile_among_FUS_level_genes": 100 * float((r[cf] < r[f]).mean())})
    print(pd.DataFrame(out5).to_string())
    pd.DataFrame(out5).to_csv(os.path.join(OUT, "v1_TRIM72_FUS.csv"), index=False, float_format="%.4g")

    # ---- F9: p53 targets mean r vs level-matched random sets
    import tahoe_gene_panel as Pn
    p53 = [int(np.flatnonzero(sym == g)[0]) for g in Pn.P53_ACTIVITY if (sym == g).any()]
    rows9 = []
    for k in (0, 3, 10):
        r = corr_with(remove_pcs(Xs, k), t)
        obs = r[p53].mean()
        pools = []
        for i in p53:
            d_ = np.abs(np.log2(np.maximum(lvl, 1e-6)) - np.log2(lvl[i]))
            c_ = np.flatnonzero((d_ <= 1) & ~np.isin(np.arange(len(lvl)), p53 + [t]))
            pools.append(c_)
        null = np.stack([r[rng.choice(c_, 4000)] for c_ in pools], axis=1).mean(axis=1)
        rows9.append({"variant": f"minus{k}pc", "n_p53_targets": len(p53), "mean_r": obs, "null_mean": null.mean(),
                      "null_sd": null.std(), "z": (obs - null.mean()) / null.std(),
                      "p_two_sided": (1 + (np.abs(null - null.mean()) >= abs(obs - null.mean())).sum()) / (len(null) + 1),
                      "r_TP53": r[sym == "TP53"][0], "r_MDM2": r[sym == "MDM2"][0], "r_CDKN1A": r[sym == "CDKN1A"][0]})
    print(pd.DataFrame(rows9).to_string())
    pd.DataFrame(rows9).to_csv(os.path.join(OUT, "v1_p53_targets.csv"), index=False, float_format="%.4g")

    # ---- F3: idarubicin 5 uM: share of low genes up (q < 0.05 and > 2x), TRIM72 percentile
    Q = np.asarray(np.load(os.path.join(FXD, "DD_qup.npy"), mmap_mode="r"))[:, gi].astype(np.float64)
    Lf = np.asarray(np.load(os.path.join(FXD, "DD_lfc.npy"), mmap_mode="r"))[:, gi].astype(np.float64)
    Zf = np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r"))[:, gi].astype(np.float64)
    rows3 = []
    for drug in ("Idarubicin (hydrochloride)", "Homoharringtonine", "Auranofin", "Dinaciclib"):
        r_ = int(dd.index[(dd["drug"] == drug) & np.isclose(dd["conc"], 5.0)][0])
        up = (Q[r_] < 0.05) & (Lf[r_] > 1)
        low = lvl <= 10
        for lab, cl in (("E116", cls116), ("E110", cls110)):
            se, un = cl == "sense_exposed", cl == "unexposed"
            rows3.append({"drug": drug, "annotation": lab, "pct_low_DoG_up": 100 * up[low & se].mean(),
                          "pct_low_unexposed_up": 100 * up[low & un].mean(),
                          "pct_all_low_up": 100 * up[low].mean(),
                          "TRIM72_z": Zf[r_, t], "TRIM72_lfc": Lf[r_, t],
                          "TRIM72_z_pctile_all_genes": 100 * float((Zf[r_] < Zf[r_, t]).mean()),
                          "TRIM72_z_pctile_DoG_exposed": 100 * float((Zf[r_, se] < Zf[r_, t]).mean()),
                          "TRIM72_z_pctile_low_genes_within2x": 100 * float(
                              (Zf[r_, (lvl >= lvl[t] / 2) & (lvl <= lvl[t] * 2)] < Zf[r_, t]).mean()),
                          "n_DoG_exposed": int(se.sum())})
    print(pd.DataFrame(rows3).to_string())
    pd.DataFrame(rows3).to_csv(os.path.join(OUT, "v1_F3_raisers.csv"), index=False, float_format="%.4g")

    # ---- F12: DoG sense index per drug-dose with E110 classes (expression-stratified, as the analysis defines)
    lowm = lvl <= 10
    lv = np.log2(lvl)
    edges = np.quantile(lv[lowm], np.linspace(0, 1, 6))
    b = np.clip(np.searchsorted(edges, lv, side="right") - 1, 0, 4)
    res12 = {}
    for lab, cl in (("E116", cls116), ("E110", cls110)):
        diffs, w = [], []
        for k in range(5):
            e = lowm & (b == k) & (cl == "sense_exposed")
            u = lowm & (b == k) & (cl == "unexposed")
            diffs.append(np.nanmean(Zf[:, e], axis=1) - np.nanmean(Zf[:, u], axis=1))
            w.append(e.sum())
        idx = np.average(np.column_stack(diffs), axis=1, weights=w)
        res12[lab] = idx
    o12 = dd[["drug", "conc", "plates"]].copy()
    o12["DoG_index_E116"] = res12["E116"]
    o12["DoG_index_E110"] = res12["E110"]
    o12["rank_E116"] = o12["DoG_index_E116"].rank(ascending=False).astype(int)
    o12["rank_E110"] = o12["DoG_index_E110"].rank(ascending=False).astype(int)
    o12["TRIM72_z"] = Zf[:, t]
    kk = ~dd["unreliable_plate_only"].to_numpy()
    print("F12 index vs TRIM72 z Spearman (E116, E110):", spearmanr(o12.loc[kk, "DoG_index_E116"], o12.loc[kk, "TRIM72_z"]),
          spearmanr(o12.loc[kk, "DoG_index_E110"], o12.loc[kk, "TRIM72_z"]))
    print(o12[np.isclose(o12["conc"], 5.0) & o12["drug"].isin(["Idarubicin (hydrochloride)", "Homoharringtonine",
                                                                "Auranofin", "Panobinostat", "Dinaciclib"])].to_string())
    o12.to_csv(os.path.join(OUT, "v1_F12_dog_index.csv"), index=False, float_format="%.4g")


if __name__ == "__main__":
    main()
