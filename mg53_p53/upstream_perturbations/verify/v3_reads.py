#!/usr/bin/env python3
"""Adversarial verification, part 3: raw-read (pseudocount-free, uncorrected) checks of TRIM72 calls, from the gene
panel's well x line sums (/home/user/tahoe_data/gene_panel/well_line.parquet). Read-only.
  - observed vs expected TRIM72 reads per drug-dose (expected = each line's pooled CPM over the plate's drug wells x
    the line's UMIs in the well), and its Spearman with the corrected log2FC over the significant raisers
  - per-plate split for drug-doses on two plates (mitoxantrone, idarubicin, HHT)
  - lowerers: per-line sign consistency, rank of the pooled ratio within the plate, and whether other low-level panel
    genes fall in the same wells (non-specific)
  - per line: WT vs altered TP53 for the strongest raisers (pseudocount-free per-line ratios), MDM2 as positive control
"""
import os
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from scipy import stats

GP = "/home/user/tahoe_data/gene_panel"
EFF = "/home/user/tahoe_data/atlas/effects"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 80)

GENES = ["TRIM72", "MDM2", "CDKN1A", "PYCARD", "AIM2", "CASP5", "IL1B", "NLRP3", "HSPA6", "ABCB1", "ABCG2", "NAPEPLD"]
wl = pq.read_table(os.path.join(GP, "well_line.parquet"),
                   columns=["sample", "cell_line_id", "n_cells", "total_counts"] + GENES).to_pandas()
wells = pd.read_csv(os.path.join(EFF, "wells.csv"))
dd = pd.read_csv(os.path.join(EFF, "drugdose.csv"))
genes = pd.read_csv(os.path.join(EFF, "genes.csv"))
c = int(genes.loc[genes["symbol"] == "TRIM72", "col"].iloc[0])
dd["lfc"] = np.asarray(np.load(os.path.join(EFF, "DD_lfc.npy"), mmap_mode="r")[:, c], float)
dd["z"] = np.asarray(np.load(os.path.join(EFF, "DD_z.npy"), mmap_mode="r")[:, c], float)
dd["qup"] = np.asarray(np.load(os.path.join(EFF, "DD_qup.npy"), mmap_mode="r")[:, c], float)
dd["sig_up"] = (dd.qup < 0.1) & (dd.lfc >= np.log2(1.2))

wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum()   # duplicates (none expected here) summed
wl = wl.merge(wells[["sample", "plate", "is_dmso", "drugdose_row", "used_in_drugdose", "well"]], on="sample", how="inner")
wl = wl[wl["n_cells"] >= 30]
dw = wl[~wl["is_dmso"].astype(bool)]
for g in GENES:
    agg = dw.groupby(["plate", "cell_line_id"])[[g, "total_counts"]].sum()
    base = (agg[g] / agg["total_counts"]).rename(f"base_{g}")
    wl = wl.join(base, on=["plate", "cell_line_id"])
    wl[f"exp_{g}"] = wl[f"base_{g}"] * wl["total_counts"]

used = wl[wl["used_in_drugdose"].astype(str).str.lower().eq("true") & (wl["drugdose_row"] >= 0)]
pool = used.groupby("drugdose_row").agg(**{f"obs_{g}": (g, "sum") for g in GENES},
                                        **{f"exp_{g}": (f"exp_{g}", "sum") for g in GENES},
                                        umis=("total_counts", "sum"))
for g in GENES:
    pool[f"ratio_{g}"] = pool[f"obs_{g}"] / pool[f"exp_{g}"]
dd = dd.join(pool, how="left")
sig = dd[dd.sig_up].sort_values("z", ascending=False)
rs = stats.spearmanr(sig["lfc"], np.log2(sig["ratio_TRIM72"]))
print(f"significant raisers n={len(sig)}: Spearman corrected log2FC vs log2(obs/exp reads) = {rs.statistic:.3f} (p {rs.pvalue:.2g})")
print(sig[["drug", "conc", "plates", "lfc", "z", "obs_TRIM72", "exp_TRIM72", "ratio_TRIM72"]].assign(fold=lambda d: 2 ** d.lfc).round(3).to_string())
print("raisers with pooled read ratio < 1.5:", sig.loc[sig.ratio_TRIM72 < 1.5, ["drug", "conc", "ratio_TRIM72"]].values.tolist())
rs = stats.spearmanr(dd["lfc"], np.log2(dd["ratio_TRIM72"].clip(lower=1e-3)), nan_policy="omit")
print(f"all drug-doses: Spearman corrected log2FC vs log2 read ratio = {rs.statistic:.3f}")

# per plate split for multi-plate raisers
print("\n-- per-well (pseudocount-free, per-line pooled) for 2-plate drug-doses among raisers and selected others")
for drug, conc in [("Idarubicin (hydrochloride)", 5.0), ("Homoharringtonine", 5.0), ("Mitoxantrone (dihydrochloride)", 5.0),
                   ("Amsacrine", 5.0), ("Selinexor", 5.0), ("Docetaxel", 5.0), ("Tucidinostat", 5.0)]:
    i = dd.index[(dd.drug == drug) & (dd.conc == conc)][0]
    s = used[used.drugdose_row == i].groupby(["sample", "plate", "well"]).agg(obs=("TRIM72", "sum"), exp=("exp_TRIM72", "sum"))
    s["ratio"] = s.obs / s.exp
    print(drug, conc, f"(z {dd.at[i, 'z']:.2f}, corrected {2 ** dd.at[i, 'lfc']:.2f}x):",
          "; ".join(f"{p} {w}: {o:.0f}/{e:.0f} = {r:.2f}x" for (smp, p, w), o, e, r in zip(s.index, s.obs, s.exp, s.ratio)))

# trametinib wells
print("\n-- trametinib, all wells")
for drug in ("Trametinib", "Trametinib (DMSO_TF solvate)", "Binimetinib", "Cobimetinib", "TAK-733"):
    for i in dd.index[dd.drug == drug]:
        s = used[used.drugdose_row == i].groupby(["plate", "well"]).agg(obs=("TRIM72", "sum"), exp=("exp_TRIM72", "sum"))
        print(f"  {drug} {dd.at[i, 'conc']}: z {dd.at[i, 'z']:.2f} corrected {2 ** dd.at[i, 'lfc']:.2f}x | " +
              "; ".join(f"{p} {w}: {o:.0f}/{e:.0f}={o / e:.2f}x" for (p, w), o, e in zip(s.index, s.obs, s.exp)))

# lowerers: per-line consistency and plate rank
print("\n-- lowerers (z <= -3 or named in the claim)")
used_w = used.copy()
used_w["lr"] = np.log2((used_w["TRIM72"] + 0.5) / (used_w["exp_TRIM72"] + 0.5))
names = [("Ponatinib", 5.0), ("Cabozantinib (S-malate)", 5.0), ("NG25", 5.0), ("Radotinib", 5.0), ("Neratinib (maleate)", 5.0),
         ("Tirabrutinib", 5.0), ("Infigratinib", 5.0), ("Pralsetinib", 5.0)]
names += [(r.drug, r.conc) for r in dd[dd.z <= -3].itertuples()]
seen = set()
for drug, conc in names:
    if (drug, conc) in seen:
        continue
    seen.add((drug, conc))
    hit = dd.index[(dd.drug == drug) & (dd.conc == conc)]
    if len(hit) == 0:
        print("  not found", drug, conc); continue
    i = hit[0]
    s = used_w[used_w.drugdose_row == i]
    # per line pooled over the drug-dose's wells
    pl = s.groupby("cell_line_id")[["TRIM72", "exp_TRIM72"]].sum()
    pl = pl[pl.exp_TRIM72 >= 1]
    n_dn = int((pl.TRIM72 < pl.exp_TRIM72).sum()); n = len(pl)
    sgn = stats.binomtest(n_dn, n, 0.5).pvalue if n else np.nan
    plates = sorted(set(s.plate))
    # rank of pooled ratio among all drug-doses on the same single plate
    same = dd[dd.plates == ",".join(plates)] if len(plates) == 1 else dd[dd.plates == dd.at[i, "plates"]]
    rk = int((same["ratio_TRIM72"] < dd.at[i, "ratio_TRIM72"]).sum()) + 1
    other = {g: dd.at[i, f"ratio_{g}"] for g in ("PYCARD", "AIM2", "CASP5", "IL1B", "HSPA6", "NAPEPLD", "ABCG2")}
    print(f"  {drug} {conc} ({dd.at[i, 'plates']}): z {dd.at[i, 'z']:.2f}, corrected {2 ** dd.at[i, 'lfc']:.2f}x, reads {dd.at[i, 'obs_TRIM72']:.0f}"
          f"/{dd.at[i, 'exp_TRIM72']:.0f} = {dd.at[i, 'ratio_TRIM72']:.2f}x; lines below expected {n_dn}/{n} (sign p {sgn:.2g}); "
          f"rank {rk} of {len(same)} lowest on its plate(s) | other low panel genes ratio: " +
          ", ".join(f"{g} {v:.2f}" for g, v in other.items()))

# distribution of pooled read ratio on plate 12 (ponatinib's plate)
p12 = dd[dd.plates == "plate12"]["ratio_TRIM72"]
print(f"\nplate12 drug-doses: n {len(p12)}, pooled read ratio median {p12.median():.2f}, 5th pct {p12.quantile(.05):.2f}, min {p12.min():.2f}")

# per-line TP53 WT vs altered, pseudocount-free per line
print("\n-- per line, WT vs altered TP53 (annotation), pseudocount-free per-line log2((obs+0.5)/(exp+0.5)) pooled over used wells")
bl = pd.read_csv(os.path.join(GP, "results", "baseline_by_cell_line.csv"), usecols=["cell_line_id", "tp53_group"])
grp = bl.set_index("cell_line_id")["tp53_group"]
rows = []
for i in dd.index[dd.sig_up | (dd.z >= 3)]:
    s = used[used.drugdose_row == i]
    rr = {"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "z": dd.at[i, "z"]}
    for g in ("TRIM72", "MDM2", "CDKN1A"):
        pl = s.groupby("cell_line_id")[[g, f"exp_{g}"]].sum()
        pl = pl[pl[f"exp_{g}"] >= 2]          # line must have >= 2 expected reads
        lr = np.log2((pl[g] + 0.5) / (pl[f"exp_{g}"] + 0.5))
        gg = lr.index.map(grp)
        wt, al = lr[gg == "WT"], lr[gg == "altered"]
        p = stats.mannwhitneyu(wt, al).pvalue if len(wt) >= 3 and len(al) >= 3 else np.nan
        rr[f"{g}_n_wt"] = len(wt); rr[f"{g}_n_alt"] = len(al)
        rr[f"{g}_wt_med"] = wt.median(); rr[f"{g}_alt_med"] = al.median(); rr[f"{g}_diff"] = wt.median() - al.median(); rr[f"{g}_p"] = p
        if g == "TRIM72":
            rr["TRIM72_frac_alt_up_1.2x"] = float((al >= np.log2(1.2)).mean()) if len(al) else np.nan
    rows.append(rr)
tp = pd.DataFrame(rows).sort_values("z", ascending=False)
print(tp[["drug", "conc", "z", "TRIM72_n_wt", "TRIM72_n_alt", "TRIM72_wt_med", "TRIM72_alt_med", "TRIM72_diff", "TRIM72_p",
          "TRIM72_frac_alt_up_1.2x", "MDM2_diff", "MDM2_p", "CDKN1A_diff"]].round(3).to_string())
d = tp["TRIM72_diff"].dropna()
print(f"raisers (z>=3 or sig): n {len(d)}, median WT-minus-altered {d.median():.3f}, positive {int((d > 0).sum())}/{len(d)}, "
      f"Wilcoxon p {stats.wilcoxon(d).pvalue:.2g}")
# one value per compound (best dose) to avoid counting doses of one drug several times
tp["compound"] = tp["drug"].str.split(" \\(").str[0].str.lower()
d1 = tp.sort_values("z", ascending=False).drop_duplicates("compound")["TRIM72_diff"].dropna()
print(f"  one per compound: n {len(d1)}, median {d1.median():.3f}, positive {int((d1 > 0).sum())}/{len(d1)}, Wilcoxon p {stats.wilcoxon(d1).pvalue:.2g}")
tp.to_csv(os.path.join(OUT, "v3_tp53_per_line_contrast.csv"), index=False)
# basal: TRIM72 CPM of DMSO wells by TP53 group
dm = wl[wl["is_dmso"].astype(bool)].groupby("cell_line_id")[["TRIM72", "total_counts"]].sum()
cpm = dm.TRIM72 / dm.total_counts * 1e6
g = cpm.index.map(grp)
print(f"basal TRIM72 CPM (DMSO): WT median {cpm[g == 'WT'].median():.2f} (n {(g == 'WT').sum()}) vs altered {cpm[g == 'altered'].median():.2f} "
      f"(n {(g == 'altered').sum()}), MW p {stats.mannwhitneyu(cpm[g == 'WT'], cpm[g == 'altered']).pvalue:.2f}")
dd.drop(columns=[c_ for c_ in dd.columns if c_.startswith(("obs_", "exp_")) and not c_.endswith("TRIM72")]).to_csv(
    os.path.join(OUT, "v3_drugdose_read_ratios.csv"), index=False)
