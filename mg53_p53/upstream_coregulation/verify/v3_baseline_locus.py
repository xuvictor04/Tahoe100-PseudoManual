#!/usr/bin/env python3
"""Adversarial check of the baseline (F6, F7, F10) and locus / readthrough claims (F1, F2) from the independent
pseudobulk sums of v2_pseudobulk_pass.py (run that first).

    python3 mg53_p53/upstream_coregulation/verify/v3_baseline_locus.py

Writes out/v3_*.csv. Reads only out/v2_cache, out/v1_dog_classes_E116_vs_E110.csv, ext_download/*, and the atlas
genes.csv / lines.csv / gene_metadata (read-only).
"""
import json
import os

import numpy as np
import pandas as pd
from scipy.stats import rankdata, spearmanr, mannwhitneyu

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
C2 = os.path.join(OUT, "v2_cache")
FXD = "/home/user/tahoe_data/atlas/effects"
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)
rng = np.random.default_rng(5)


def zr(M, axis):
    R = rankdata(M, axis=axis)
    R = R - R.mean(axis=axis, keepdims=True)
    sd = R.std(axis=axis, keepdims=True)
    sd[sd == 0] = np.nan
    return R / sd


def main():
    gm = pd.read_parquet("/home/user/tahoe_data/metadata/gene_metadata.parquet")
    sym = pd.Series(gm["gene_symbol"].values, index=gm["token_id"].values)
    tok = {s: int(t) for s, t in zip(gm["gene_symbol"], gm["token_id"])}
    T = tok["TRIM72"]
    q = np.load(os.path.join(C2, "plate_line_quiet.npz"))
    plates = list(q["plates"])
    info = json.load(open(os.path.join(FXD, "info.json")))
    use = [i for i, p in enumerate(plates) if p not in info["unreliable_plates"]]
    pn = [plates[i] for i in use]
    # atlas genes -> DoG classes (v1)
    ag = pd.read_csv(os.path.join(FXD, "genes.csv"))
    ag = ag[ag["kind"] == "gene"].reset_index(drop=True)
    v1 = pd.read_csv(os.path.join(OUT, "v1_dog_classes_E116_vs_E110.csv"))
    assert (v1["gene"].astype(str).to_numpy() == ag["symbol"].astype(str).to_numpy()).all()
    c110 = dict(zip(ag["token"].astype(int), v1["class_E110"]))
    c116 = dict(zip(ag["token"].astype(int), v1["class_E116"]))

    rows_b = []
    for defn in ("quiet", "all", "dmso"):
        z = q if defn == "quiet" else np.load(os.path.join(C2, f"plate_line_sums_{defn}.npz"))
        counts = z["counts"][use].astype(np.float64)       # P x L x G
        tot = z["total"][use]
        okp = (tot > 0).all(axis=1)
        counts, tot = counts[okp], tot[okp]
        P, L, G = counts.shape
        csum = counts.sum(axis=(0, 1))
        named = np.zeros(G, dtype=bool)
        named[gm["token_id"].astype(int).to_numpy()] = True
        toks = np.flatnonzero((csum >= 200) & named)
        toks = toks[toks != T]
        pooled = 1e6 * csum / tot.sum()
        lt = np.log2((counts[:, :, toks] + 0.5) / tot[:, :, None] * 1e6)
        yt = np.log2((counts[:, :, T] + 0.5) / tot * 1e6)
        ZG = np.nan_to_num(zr(lt, 1))
        ZT = zr(yt, 1)
        rho = np.median(np.einsum("pl,plg->pg", ZT, ZG) / L, axis=0)
        # naive version: Spearman over all (plate, line) points, no within-plate ranking (what a pooled analysis does)
        ZGn = np.nan_to_num(zr(lt.reshape(P * L, -1), 0))
        ZTn = zr(yt.reshape(-1), 0)
        rho_naive = (ZTn @ ZGn) / (P * L)
        res = pd.DataFrame({"token": toks, "gene": sym.reindex(toks).values, "pooled_cpm": pooled[toks],
                            "rho_within_plate_median": rho, "rho_naive_pooled_plates": rho_naive})
        lb = np.log2(res["pooled_cpm"].to_numpy())
        o = np.argsort(lb)
        pct = np.empty(len(res))
        for i in range(len(res)):
            lo, hi = np.searchsorted(lb[o], [lb[i] - 1, lb[i] + 1])
            pct[i] = 100 * float((rho[o[lo:hi]] < rho[i]).mean())
        res["pct_vs_level_within2x"] = pct
        res["rank_within_plate"] = res["rho_within_plate_median"].rank(ascending=False).astype(int)
        res["rank_naive"] = res["rho_naive_pooled_plates"].rank(ascending=False).astype(int)
        # plate gap of every gene (plates 1-3,14 vs 4-12), from this definition
        hi_ = np.array([p in ("plate1", "plate2", "plate3", "plate14") for p in np.array(pn)[okp]])
        cpm = counts / tot[:, :, None] * 1e6
        lc = np.log2(np.median(cpm, axis=1) + 0.1)
        gap = lc[hi_].mean(axis=0) - lc[~hi_].mean(axis=0)
        res["plate_gap"] = gap[toks]
        if defn == "quiet":
            # line-level background of near-silent reads: per plate, mean within-plate z of log CPM over genes at
            # 0.05-0.5 CPM pooled (random 2000); partial rho of TRIM72 with each gene given that background
            silent = np.flatnonzero((pooled[toks] >= 0.05) & (pooled[toks] <= 0.5))
            silent = rng.choice(silent, size=min(2000, silent.size), replace=False)
            bg = ZG[:, :, silent].mean(axis=2)                     # P x L
            bgz = zr(bg, 1)
            r_tb = np.einsum("pl,pl->p", ZT, bgz) / L                # P
            r_gb = np.einsum("pl,plg->pg", bgz, ZG) / L              # P x g
            r_tg = np.einsum("pl,plg->pg", ZT, ZG) / L
            part = (r_tg - r_tb[:, None] * r_gb) / np.sqrt((1 - r_tb[:, None] ** 2) * (1 - r_gb ** 2))
            res["rho_partial_given_silent_background"] = np.median(part, axis=0)
            res["rank_partial"] = res["rho_partial_given_silent_background"].rank(ascending=False).astype(int)
            print(f"TRIM72 vs near-silent-gene background (median over plates): rho {np.median(r_tb):.3f}")
            print("plate-level TRIM72 rho with background:", np.round(r_tb, 2))
            gaps = pd.DataFrame({"token": np.arange(G), "gene": sym.reindex(np.arange(G)).values, "pooled_cpm": pooled,
                                 "plate_gap": gap})
            gaps = gaps[(gaps["pooled_cpm"] >= 2) & gaps["gene"].notna()].copy()
            gaps["gap_rank"] = gaps["plate_gap"].rank(ascending=False).astype(int)
            gaps["class_E110"] = gaps["token"].map(c110).fillna("not in atlas")
            gaps["class_E116"] = gaps["token"].map(c116).fillna("not in atlas")
            gaps.sort_values("gap_rank").to_csv(os.path.join(OUT, "v3_plate_gap_genomewide.csv"), index=False,
                                                float_format="%.4g")
            res_quiet = res
        key = ["PYCARD-AS1", "FUS", "ITGAM", "ITGAX", "PYCARD", "FNDC7", "SRF", "ACTA1", "TP53"]
        for kname in key:
            r_ = res[res["gene"] == kname]
            if len(r_):
                rec = {"definition": defn, "n_plates": int(okp.sum()), "gene": kname, "n_genes": len(res)}
                rec.update(r_.iloc[0][["pooled_cpm", "rho_within_plate_median", "rank_within_plate",
                                       "pct_vs_level_within2x", "rho_naive_pooled_plates", "rank_naive",
                                       "plate_gap"]].to_dict())
                if "rho_partial_given_silent_background" in r_:
                    rec["rho_partial_given_silent_background"] = r_.iloc[0]["rho_partial_given_silent_background"]
                    rec["rank_partial"] = r_.iloc[0]["rank_partial"]
                rows_b.append(rec)
        top_w = res.nsmallest(20, "rank_within_plate")["gene"].tolist()
        top_n = res.nsmallest(20, "rank_naive")["gene"].tolist()
        print(f"[{defn}] {len(res)} genes; top within-plate: {', '.join(map(str, top_w[:12]))}")
        print(f"[{defn}] top naive pooled: {', '.join(map(str, top_n[:12]))}")
        print(f"[{defn}] Spearman across genes of naive rho vs plate gap: "
              f"{spearmanr(res['rho_naive_pooled_plates'], res['plate_gap'])[0]:.3f}; within-plate rho vs plate gap: "
              f"{spearmanr(res['rho_within_plate_median'], res['plate_gap'])[0]:.3f}; "
              f"median |gap| of naive top-100 {res.nsmallest(100, 'rank_naive')['plate_gap'].median():.2f} vs "
              f"within-plate top-100 {res.nsmallest(100, 'rank_within_plate')['plate_gap'].median():.2f} vs all "
              f"{res['plate_gap'].median():.2f}")
        del counts, lt, ZG
    B = pd.DataFrame(rows_b)
    B.to_csv(os.path.join(OUT, "v3_baseline_key_genes.csv"), index=False, float_format="%.4g")
    print(B.to_string())
    res_quiet.sort_values("rank_within_plate").to_csv(os.path.join(OUT, "v3_baseline_genomewide_quiet.csv"),
                                                      index=False, float_format="%.4g")
    print("top 15 partial (given near-silent background):",
          ", ".join(res_quiet.nsmallest(15, "rank_partial")["gene"].astype(str)))

    # ---- plate gap (F7): TRIM72 rank, DoG share among top-100, level-stratified DoG vs unexposed
    gp = pd.read_csv(os.path.join(OUT, "v3_plate_gap_genomewide.csv"))
    tr = gp[gp["gene"] == "TRIM72"].iloc[0]
    print(f"F7: TRIM72 gap {tr['plate_gap']:.2f}, rank {int(tr['gap_rank'])} of {len(gp)} genes >= 2 CPM")
    out7 = []
    for lab in ("E110", "E116"):
        c = gp[f"class_{lab}"]
        top = gp.nsmallest(100, "gap_rank")
        rec = {"annotation": lab, "TRIM72_gap": tr["plate_gap"], "TRIM72_rank": int(tr["gap_rank"]),
               "n_genes": len(gp), "top100_pct_sense_exposed": 100 * float((top[f"class_{lab}"] == "sense_exposed").mean()),
               "all_pct_sense_exposed": 100 * float((c == "sense_exposed").mean())}
        low = (gp["pooled_cpm"] <= 20)
        sub = gp[low & c.isin(["sense_exposed", "unexposed"])].copy()
        sub["bin"] = pd.qcut(np.log2(sub["pooled_cpm"]), 5, labels=False)
        diffs, ws = [], []
        for b_, h in sub.groupby("bin"):
            e = h.loc[h[f"class_{lab}"] == "sense_exposed", "plate_gap"]
            u = h.loc[h[f"class_{lab}"] == "unexposed", "plate_gap"]
            diffs.append(e.median() - u.median())
            ws.append(len(e))
        obs = np.average(diffs, weights=ws)
        # stratified permutation of the class labels within level bins
        null = []
        lab_arr = (sub[f"class_{lab}"] == "sense_exposed").to_numpy()
        gv = sub["plate_gap"].to_numpy()
        bins = sub["bin"].to_numpy()
        for _ in range(1000):
            perm = lab_arr.copy()
            for b_ in np.unique(bins):
                m = bins == b_
                perm[m] = rng.permutation(perm[m])
            d_ = [np.median(gv[(bins == b_) & perm]) - np.median(gv[(bins == b_) & ~perm]) for b_ in np.unique(bins)]
            null.append(np.average(d_, weights=ws))
        null = np.array(null)
        rec.update({"level_stratified_median_gap_diff_DoG_minus_unexposed": obs,
                    "perm_p": (1 + (np.abs(null) >= abs(obs)).sum()) / 1001,
                    "n_DoG_2to20": int(lab_arr.sum()), "n_unexposed_2to20": int((~lab_arr).sum()),
                    "raw_medians": f"{sub.loc[lab_arr, 'plate_gap'].median():.3f} vs {sub.loc[~lab_arr, 'plate_gap'].median():.3f}"})
        out7.append(rec)
    print(pd.DataFrame(out7).T.to_string())
    pd.DataFrame(out7).to_csv(os.path.join(OUT, "v3_F7_plate_gap.csv"), index=False, float_format="%.4g")

    # ---- locus in the idarubicin / HHT 5 uM wells (F1, F2)
    w = np.load(os.path.join(C2, "wells_p6_p14.npz"))
    med, tc, tt, tcell = w["median_cpm"], w["target_counts"], w["target_total"], w["target_cells"]
    targets = list(w["targets"])
    lab_of = {"smp_2010": ("Idarubicin 5 (plate6)", 0), "smp_2778": ("Idarubicin 5 (plate14)", 1),
              "smp_2047": ("Homoharringtonine 5 (plate6)", 0), "smp_2815": ("Homoharringtonine 5 (plate14)", 1)}
    # locus genes from Ensembl 110 within +-250 kb of TRIM72
    e110 = pd.read_csv(os.path.join(HERE, "ext_download", "ensembl110_genes.tsv"), sep="\t",
                       dtype={"Chromosome/scaffold name": str})
    e110.columns = ["ensembl_id", "name", "chrom", "start", "end", "strand", "biotype"]
    loc = e110[(e110["chrom"] == "16") & (e110["end"] > 31214119 - 250_000) & (e110["start"] < 31231537 + 250_000)]
    loc = loc.merge(gm, on="ensembl_id", how="inner").sort_values("start")
    fus_end_110 = int(loc.loc[loc["gene_symbol"] == "FUS", "end"].iloc[0])
    print("Ensembl 110 locus:", loc[loc["gene_symbol"].isin(["FUS", "PYCARD-AS1", "PYCARD", "TRIM72", "PYDC1",
                                                              "ITGAM", "ITGAX", "ITGAD"])][
        ["gene_symbol", "start", "end", "strand"]].to_string())
    locrows, gainrows = [], []
    gain_tabs = {}
    for s in targets:
        lab, a = lab_of[s]
        j = targets.index(s)
        ok = (tcell[j] >= 30) & np.isfinite(med[a]).all(axis=1) & (tt[j] > 0)
        O = tc[j][ok].sum(axis=0).astype(np.float64)
        E = (tt[j][ok][:, None] * med[a][ok] / 1e6).sum(axis=0)
        lvl = 1e6 * E / tt[j][ok].sum()
        good = (E >= 5) & sym.reindex(np.arange(len(O))).notna().to_numpy()
        lr = np.log2((O + 0.5) / (E + 0.5))
        lg = np.log2(np.maximum(lvl, 1e-6))
        gi_ = np.flatnonzero(good)
        o_ = gi_[np.argsort(lg[gi_])]
        pct = np.full(len(O), np.nan)
        for i in gi_:
            lo, hi = np.searchsorted(lg[o_], [lg[i] - 1, lg[i] + 1])
            pct[i] = 100 * float((lr[o_[lo:hi]] < lr[i]).mean())
        added = 1e6 * (O - E) / tt[j][ok].sum()
        for _, r in loc.iterrows():
            t_ = int(r["token_id"])
            locrows.append({"well": lab, "gene": r["gene_symbol"], "start": r["start"], "end": r["end"],
                            "strand": r["strand"], "downstream_of_FUS_end_E110": r["start"] > fus_end_110,
                            "observed": O[t_], "expected": E[t_], "log2_OE": lr[t_],
                            "pct_vs_level_within2x": pct[t_], "added_cpm": added[t_], "baseline_cpm": lvl[t_],
                            "n_lines": int(ok.sum()), "well_median_log2OE_E_ge_5": float(np.median(lr[good]))})
        # per-line gain correlation with TRIM72 (genome-wide; genes with E >= 5)
        cpm_w = tc[j][ok] / tt[j][ok][:, None] * 1e6
        base = med[a][ok]
        gain = cpm_w[:, gi_] - base[:, gi_]
        tpos = int(np.flatnonzero(gi_ == T)[0])
        Rg = zr(gain, 0)
        rho_g = (Rg[:, tpos] @ np.nan_to_num(Rg)) / Rg.shape[0]
        Rb = zr(base[:, gi_], 0)
        rho_b = (Rb[:, tpos] @ np.nan_to_num(Rb)) / Rb.shape[0]        # baseline (plate median) co-variation
        # partial: gain_T vs gain_g given base_T and base_g (Spearman ranks)
        x1, x2, x3 = Rg[:, tpos], Rb[:, tpos], None
        n_ = Rg.shape[0]
        r12 = rho_g                                            # r(gT, gg)
        r13 = float(x1 @ x2) / n_                              # r(gT, bT)
        r14 = (x1 @ np.nan_to_num(Rb)) / n_                    # r(gT, bg)
        r23 = (Rb[:, tpos] @ np.nan_to_num(Rg)) / n_           # r(bT, gg)
        r24 = rho_b                                            # r(bT, bg)
        r34 = (np.nan_to_num(Rg) * np.nan_to_num(Rb)).sum(axis=0) / n_   # r(gg, bg)
        Cm = np.zeros((len(gi_), 4, 4))
        Cm[:, 0, 0] = Cm[:, 1, 1] = Cm[:, 2, 2] = Cm[:, 3, 3] = 1
        Cm[:, 0, 1] = Cm[:, 1, 0] = r12
        Cm[:, 0, 2] = Cm[:, 2, 0] = r13
        Cm[:, 0, 3] = Cm[:, 3, 0] = r14
        Cm[:, 1, 2] = Cm[:, 2, 1] = r23
        Cm[:, 1, 3] = Cm[:, 3, 1] = r34
        Cm[:, 2, 3] = Cm[:, 3, 2] = r24
        fin = np.isfinite(Cm).all(axis=(1, 2))
        part = np.full(len(gi_), np.nan)
        Pm = np.linalg.pinv(Cm[fin])
        part[fin] = -Pm[:, 0, 1] / np.sqrt(Pm[:, 0, 0] * Pm[:, 1, 1])
        # log-ratio version (per line log2 fold change, pseudo 0.5 CPM)
        lfc = np.log2((cpm_w[:, gi_] + 0.5) / (base[:, gi_] + 0.5))
        Rl = zr(lfc, 0)
        rho_l = (Rl[:, tpos] @ np.nan_to_num(Rl)) / n_
        gt = pd.DataFrame({"token": gi_, "gene": sym.reindex(gi_).values, "baseline_cpm": lvl[gi_],
                           "rho_gain": rho_g, "rho_baseline_same_lines": rho_b, "rho_gain_partial_baselines": part,
                           "rho_log2fc": rho_l})
        gt = gt[gt["token"] != T]
        for c_ in ("rho_gain", "rho_gain_partial_baselines", "rho_log2fc", "rho_baseline_same_lines"):
            gt[f"rank_{c_}"] = gt[c_].rank(ascending=False, method="min")
        lb = np.log2(np.maximum(gt["baseline_cpm"].to_numpy(), 1e-6))
        oo = np.argsort(lb)
        for c_ in ("rho_gain", "rho_gain_partial_baselines", "rho_log2fc"):
            v = gt[c_].to_numpy()
            pc = np.empty(len(gt))
            for i in range(len(gt)):
                lo, hi = np.searchsorted(lb[oo], [lb[i] - 1, lb[i] + 1])
                vv = v[oo[lo:hi]]
                pc[i] = 100 * float((vv[np.isfinite(vv)] < v[i]).mean())
            gt[f"pct_level_{c_}"] = pc
        gain_tabs[lab] = gt
        cc = spearmanr(gt["rho_gain"], gt["rho_baseline_same_lines"], nan_policy="omit")[0]
        print(f"{lab}: {int(ok.sum())} lines; across genes Spearman(rho_gain, rho_baseline) = {cc:.3f}")
        for g_ in ("PYCARD-AS1", "ITGAM", "FUS", "PYCARD", "ITGAD", "ITGAX"):
            r_ = gt[gt["gene"] == g_]
            if len(r_):
                rr = r_.iloc[0]
                gainrows.append({"well": lab, "gene": g_, "n_lines": int(ok.sum()), "n_genes": len(gt),
                                 **{c_: rr[c_] for c_ in gt.columns if c_.startswith(("rho", "rank", "pct"))}})
        # TRIM72 gain vs FUS level per line
        f_ = tok["FUS"]
        gT = cpm_w[:, T] - base[:, T]
        gainrows.append({"well": lab, "gene": "TRIM72 gain vs FUS CPM in well (Spearman)", "n_lines": int(ok.sum()),
                         "rho_gain": spearmanr(gT, cpm_w[:, f_])[0]})
        gainrows.append({"well": lab, "gene": "TRIM72 gain vs FUS baseline CPM (Spearman)", "n_lines": int(ok.sum()),
                         "rho_gain": spearmanr(gT, base[:, f_])[0]})
        gainrows.append({"well": lab, "gene": "TRIM72 gain vs PYCARD-AS1 gain (Pearson, CPM)", "n_lines": int(ok.sum()),
                         "rho_gain": np.corrcoef(gT, cpm_w[:, tok["PYCARD-AS1"]] - base[:, tok["PYCARD-AS1"]])[0, 1]})
    LT = pd.DataFrame(locrows)
    LT.to_csv(os.path.join(OUT, "v3_locus_OE_in_wells.csv"), index=False, float_format="%.4g")
    show = LT[(LT["expected"] >= 5) | LT["gene"].isin(["PYDC1"])]
    print(show[["well", "gene", "strand", "downstream_of_FUS_end_E110", "observed", "expected", "log2_OE",
                "pct_vs_level_within2x", "added_cpm", "baseline_cpm"]].to_string())
    # strand summary using level-matched percentiles (E >= 5)
    srow = []
    for lab, h in LT[LT["expected"] >= 5].groupby("well"):
        dn = h["downstream_of_FUS_end_E110"] & (h["gene"] != "TRIM72")
        srow.append({"well": lab,
                     "plus_downstream_genes": ", ".join(h.loc[dn & (h["strand"] == 1), "gene"]),
                     "plus_downstream_median_pct": h.loc[dn & (h["strand"] == 1), "pct_vs_level_within2x"].median(),
                     "minus_downstream_genes": ", ".join(h.loc[dn & (h["strand"] == -1), "gene"]),
                     "minus_downstream_median_pct": h.loc[dn & (h["strand"] == -1), "pct_vs_level_within2x"].median(),
                     "upstream_lt_2cpm_genes": ", ".join(h.loc[~dn & (h["baseline_cpm"] < 2) & (h["gene"] != "TRIM72"), "gene"]),
                     "upstream_lt_2cpm_median_pct": h.loc[~dn & (h["baseline_cpm"] < 2) & (h["gene"] != "TRIM72"),
                                                          "pct_vs_level_within2x"].median(),
                     "upstream_all_median_pct": h.loc[~dn & (h["gene"] != "TRIM72"), "pct_vs_level_within2x"].median(),
                     "TRIM72_pct": h.loc[h["gene"] == "TRIM72", "pct_vs_level_within2x"].iloc[0]})
    S = pd.DataFrame(srow)
    S.to_csv(os.path.join(OUT, "v3_locus_strand_levelmatched.csv"), index=False, float_format="%.4g")
    print(S.to_string())
    GR = pd.DataFrame(gainrows)
    GR.to_csv(os.path.join(OUT, "v3_gain_corr_key_genes.csv"), index=False, float_format="%.4g")
    print(GR.to_string())
    for lab, gt in gain_tabs.items():
        print(lab, "top by rho_gain:", ", ".join(gt.nsmallest(10, "rank_rho_gain")["gene"].astype(str)))
        print(lab, "top by partial:", ", ".join(gt.nsmallest(10, "rank_rho_gain_partial_baselines")["gene"].astype(str)))
        print(lab, "top by log2fc:", ", ".join(gt.nsmallest(10, "rank_rho_log2fc")["gene"].astype(str)))
        gt.to_csv(os.path.join(OUT, f"v3_gain_corr_{lab.replace(' ', '_').replace('(', '').replace(')', '')}.csv.gz"),
                  index=False, float_format="%.4g")


if __name__ == "__main__":
    main()
