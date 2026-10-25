#!/usr/bin/env python3
"""Part 6: (a) are the analysis's FDR<0.10 WT-higher TRIM72 screen hits enriched among strong p53 activators (F4)?
(b) epirubicin 5 uM: WT vs missense vs truncating/splice/deletion with the simple DMSO-ratio values (F3).
Usage: python3 verify_part6.py"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
ANA = os.path.join(os.path.dirname(HERE), "tables")
OUT = os.path.join(HERE, "tables")
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)
RNG = np.random.default_rng(5)

sc = pd.read_csv(f"{ANA}/screen_all_drugdoses_wt_minus_altered.csv")
act = (sc.P53_ACTIVITY_all_lines_z >= 5) | (sc.P53_SCORE_wt_minus_altered_z >= 5)
raiser = (sc.TRIM72_all_lines_z_corrected >= 3) & (sc.TRIM72_all_lines_fold_change >= 1.2) & (sc.TRIM72_all_lines_fdr_up < 0.10)
hit_wt = (sc.TRIM72_fdr < 0.10) & (sc.TRIM72_wt_minus_altered_z > 0)
hit_alt = (sc.TRIM72_fdr < 0.10) & (sc.TRIM72_wt_minus_altered_z < 0)
print("strong activators:", int(act.sum()), " raisers:", int(raiser.sum()))
print("\n=== (a) TRIM72 FDR<0.10 hits ===")
print(sc.loc[hit_wt | hit_alt, ["drug", "conc", "TRIM72_wt_minus_altered_z", "TRIM72_fdr", "TRIM72_all_lines_fold_change",
                                "P53_ACTIVITY_all_lines_z", "P53_SCORE_wt_minus_altered_z"]].assign(
    strong_activator=act[hit_wt | hit_alt]).sort_values("TRIM72_wt_minus_altered_z").round(3).to_string(index=False))
rows = []
for lab, h in [("WT-higher hits", hit_wt), ("altered-higher hits", hit_alt)]:
    tab = [[int((h & act).sum()), int((~h & act).sum())], [int((h & ~act).sum()), int((~h & ~act).sum())]]
    orr, p = stats.fisher_exact(tab)
    tab2 = [[int((h & act & raiser).sum()), int((~h & act & raiser).sum())],
            [int((h & ~act & raiser).sum()), int((~h & ~act & raiser).sum())]]
    orr2, p2 = stats.fisher_exact(tab2)
    rows.append(dict(hits=lab, activators_hit=tab[0][0], activators_n=int(act.sum()), others_hit=tab[1][0],
                     others_n=int((~act).sum()), fisher_or=orr, p=p, among_raisers_act_hit=tab2[0][0],
                     among_raisers_act_n=int((act & raiser).sum()), among_raisers_other_hit=tab2[1][0],
                     among_raisers_other_n=int((~act & raiser).sum()), p_among_raisers=p2))
R = pd.DataFrame(rows)
print(R.round(4).to_string(index=False))
R.to_csv(f"{OUT}/f4_wt_higher_hits_vs_activators.csv", index=False)

# ---------------------------------------------------------------- (b) epirubicin by TP53 class
pl = pd.read_csv(f"{OUT}/per_line_dmso_ratio.csv")
lt = pd.read_csv(f"{ANA}/lines_tp53_status.csv").set_index("cell_line_id")
rows = []
for drug, conc, scope in [("Epirubicin (hydrochloride)", 5.0, "plate9"), ("Doxorubicin (hydrochloride)", 5.0, "plate9"),
                          ("Idarubicin (hydrochloride)", 5.0, "mean")]:
    for g in ["TRIM72", "P53_SCORE"]:
        x = pl[(pl.drug == drug) & np.isclose(pl.conc, conc) & (pl.scope == scope) & (pl.gene == g)].dropna(subset=["log2_vs_dmso"])
        cls = x.cell_line_id.map(lt.tp53_class).fillna("?")
        v = x.log2_vs_dmso.to_numpy()
        wt = (x.tp53_group == "WT").to_numpy()
        mis = cls.str.contains("missense only").to_numpy()
        tru = (~wt) & ~mis
        r = dict(drug=drug, conc=conc, scope=scope, gene=g, n_wt=int(wt.sum()), n_missense=int(mis.sum()), n_trunc_other=int(tru.sum()),
                 fc_wt=2 ** np.median(v[wt]), fc_missense=2 ** np.median(v[mis]), fc_trunc_other=2 ** np.median(v[tru]))
        for nm, m in [("missense", mis), ("trunc_other", tru)]:
            r[f"p_wt_vs_{nm}"] = stats.mannwhitneyu(v[wt], v[m]).pvalue
        rows.append(r)
E = pd.DataFrame(rows)
print("\n=== (b) WT vs missense-only vs other altered (truncating/splice/deletion/mixed), DMSO-ratio values ===")
print(lt.tp53_class.value_counts().to_string())
print(E.round(3).to_string(index=False))
E.to_csv(f"{OUT}/f3_by_tp53_class_dmso_ratio.csv", index=False)
