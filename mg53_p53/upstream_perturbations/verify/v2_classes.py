#!/usr/bin/env python3
"""Adversarial verification, part 2: compound-level class enrichment of TRIM72 raisers / lowerers, own code.
Re-derives the compound table from the atlas (not from the analysis CSVs), re-runs the activity-stratified tests for
anthracyclines, TOP2 poisons, harringtonines and moa_fine 'Other TK inhibitor', then stress-tests them:
  - plate layout (plates 1-3 high TRIM72 baseline + plate-3 z divisor 1.91 vs plates 4-12) as an extra stratum
  - alternative activity strata (5 / 20 strata; activity at 5 uM only)
  - salt forms merged more aggressively ('ixazomib citrate' -> ixazomib, 'larotrectinib sulfate' -> larotrectinib)
  - leave-one-compound-out
Read-only on /home/user/tahoe_data."""
import os
import re
import numpy as np
import pandas as pd
from scipy import stats

EFF = "/home/user/tahoe_data/atlas/effects"
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 120)
rng = np.random.default_rng(7)
B = 20000

genes = pd.read_csv(os.path.join(EFF, "genes.csv"))
dd = pd.read_csv(os.path.join(EFF, "drugdose.csv"))
c = int(genes.loc[genes["symbol"] == "TRIM72", "col"].iloc[0])
dd["lfc"] = np.asarray(np.load(os.path.join(EFF, "DD_lfc.npy"), mmap_mode="r")[:, c], float)
dd["z"] = np.asarray(np.load(os.path.join(EFF, "DD_z.npy"), mmap_mode="r")[:, c], float)
dd["qup"] = np.asarray(np.load(os.path.join(EFF, "DD_qup.npy"), mmap_mode="r")[:, c], float)
dd["sig_up"] = (dd.qup < 0.1) & (dd.lfc >= np.log2(1.2))
dd["nom_dn"] = dd.z <= -2


def base_paren(s):
    return re.sub(r"\s*\((?:[^()]|\([^()]*\))*\)\s*$", "", str(s)).strip().lower()


SALTS = r"\s+(citrate|sulfate|mesylate|maleate|hydrochloride|dihydrochloride|tosylate|phosphate|sodium|calcium|hcl)$"


def base_aggr(s):
    b = base_paren(s)
    b = re.sub(SALTS, "", b)
    return b


def layout(plates):
    ps = {int(p.replace("plate", "")) for p in str(plates).split(",")}
    if ps & {1, 2, 3}:
        return "L1-3"
    if ps & {4, 5, 6, 14}:
        return "L4-6"
    if ps & {7, 8, 9}:
        return "L7-9"
    if ps & {10, 11, 12}:
        return "L10-12"
    return "L13"


dd["layout"] = [layout(p) for p in dd["plates"]]
dd["activity"] = np.log1p(dd["n_sig_genes"].astype(float))


def compound_table(namefun):
    x = dd.copy()
    x["compound"] = [namefun(d) for d in x["drug"]]
    pdz = x.groupby(["compound", "conc"])["z"].agg(lambda s: s.sum() / np.sqrt(len(s))).reset_index()
    g = pdz.groupby("compound")["z"]
    comp = pd.DataFrame({"z_max": g.max(), "z_min": g.min()})
    gx = x.groupby("compound")
    comp["raiser"] = gx["sig_up"].any()
    comp["lower_nom"] = gx["nom_dn"].any()
    comp["activity"] = gx["activity"].max()
    comp["act5"] = x[x.conc == 5].groupby("compound")["activity"].max()
    comp["layouts"] = gx["layout"].agg(lambda s: ",".join(sorted(set(s))))
    comp["layout1"] = gx["layout"].agg(lambda s: sorted(set(s))[0])   # first (L1-3 sorts first)
    comp["has_L13"] = comp["layouts"].str.contains("L1-3")
    comp["moa_fine"] = gx["moa_fine"].agg(lambda s: ";".join(sorted({str(v) for v in s})))
    return comp


def strata(x, k):
    r = pd.Series(np.asarray(x, float)).rank(method="first").to_numpy()
    return np.minimum((r - 1) * k // len(r), k - 1).astype(int)


def perm_test(vals, members, st, B, stat="sum", side="greater"):
    """Within-stratum permutation of vals; statistic = sum (or mean) over members."""
    vals = np.asarray(vals, float)
    obs = vals[members].sum()
    null = np.zeros(B)
    for s in np.unique(st):
        idx = np.flatnonzero(st == s)
        k = int(members[idx].sum())
        if k == 0:
            continue
        v = vals[idx]
        # draw k without replacement B times
        draws = np.argsort(rng.random((B, idx.size)), axis=1)[:, :k]
        null += v[draws].sum(axis=1)
    if side == "greater":
        p = (1 + (null >= obs - 1e-9).sum()) / (B + 1)
    else:
        p = (1 + (null <= obs + 1e-9).sum()) / (B + 1)
    return obs, null.mean(), p


CLS = {
    "anthracyclines": ["idarubicin", "epirubicin", "doxorubicin"],
    "TOP2 poisons": ["idarubicin", "epirubicin", "doxorubicin", "mitoxantrone", "amsacrine"],
    "harringtonines": ["homoharringtonine", "harringtonine"],
}

for label, namefun in (("paren-only salt merge (as analysis)", base_paren), ("aggressive salt merge", base_aggr)):
    comp = compound_table(namefun)
    n = len(comp)
    comp["st10"] = strata(comp["activity"], 10)
    print(f"\n===== {label}: {n} compounds; raisers {int(comp.raiser.sum())}")
    top = comp[comp.st10 == 9]
    print(f"top activity decile: {len(top)} compounds, min max_n_sig_genes {np.expm1(top.activity.min()):.0f}; "
          f"raisers in it {int(top.raiser.sum())} of {int(comp.raiser.sum())}")
    print("raiser compounds:", comp[comp.raiser].assign(st=lambda d: d.st10 + 1)[["st", "layouts", "z_max"]].sort_values("z_max", ascending=False).to_string())
    print("\nraiser rate by layout (all compounds):")
    print(comp.groupby("layout1").agg(n=("raiser", "size"), raisers=("raiser", "sum"), top_decile=("st10", lambda s: int((s == 9).sum())),
                                      raisers_top=("raiser", lambda s: int(s[comp.loc[s.index, "st10"] == 9].sum())),
                                      lower_nom=("lower_nom", "sum"), med_zmin=("z_min", "median"), med_zmax=("z_max", "median")))
    # schemes of stratification
    lay = comp["layout1"].astype("category").cat.codes.to_numpy()
    hi = comp["has_L13"].to_numpy().astype(int)
    schemes = {
        "act10": comp["st10"].to_numpy(),
        "act5": strata(comp["activity"], 5),
        "act20": strata(comp["activity"], 20),
        "act10 x L1-3 flag": comp["st10"].to_numpy() * 2 + hi,
        "act5 x layout": strata(comp["activity"], 5) * 10 + lay,
        "act10(5uM activity) ": strata(comp["act5"].fillna(0), 10),
    }
    names = comp.index.to_numpy()
    for cl, mem_names in CLS.items():
        mem = np.isin(names, mem_names)
        print(f"\n -- {cl}: members found {list(names[mem])}; raisers {int(comp.raiser[mem].sum())}/{mem.sum()}")
        for sname, st in schemes.items():
            o, e, p = perm_test(comp["raiser"].astype(float), mem, st, B)
            zr = comp["z_max"].to_numpy()
            resid = zr - pd.Series(zr).groupby(st).transform("median").to_numpy()
            o2, e2, p2 = perm_test(zr, mem, st, B)
            print(f"    {sname:22s} raisers {o:.0f} vs exp {e:.2f} p {p:.4f} | sum z_max {o2:.1f} vs {e2:.1f} p {p2:.4f} | "
                  f"mean z_max resid {resid[mem].mean():+.2f}")
        a = int(comp.raiser[mem].sum())
        tab = [[a, mem.sum() - a], [int(comp.raiser.sum()) - a, n - mem.sum() - int(comp.raiser.sum()) + a]]
        print(f"    unstratified Fisher p {stats.fisher_exact(tab, alternative='greater')[1]:.2e}")
        # hypergeometric exact within top decile (all anthracyclines are in it?)
        print("    members' strata (act10, 1-based):", (comp.loc[mem, "st10"] + 1).tolist(),
              " layouts:", comp.loc[mem, "layouts"].tolist())

    # Other TK inhibitor (moa_fine): lowering
    mem = comp["moa_fine"].str.contains("Other TK inhibitor").to_numpy()
    print(f"\n -- moa_fine 'Other TK inhibitor': {mem.sum()} compounds: {list(names[mem])}")
    print(comp.loc[mem, ["z_min", "z_max", "lower_nom", "layouts", "activity"]].assign(n_sig=lambda d: np.expm1(d.activity).round()).to_string())
    zmin = comp["z_min"].to_numpy()
    for sname, st in schemes.items():
        o, e, p = perm_test(zmin, mem, st, B, side="less")
        resid = zmin - pd.Series(zmin).groupby(st).transform("median").to_numpy()
        o2, e2, p2 = perm_test(comp["lower_nom"].astype(float), mem, st, B)
        print(f"    {sname:22s} mean z_min {o / mem.sum():+.2f} vs null {e / mem.sum():+.2f} p {p:.4f}  resid {resid[mem].mean():+.2f} | "
              f"nominal lowerers {o2:.0f} vs {e2:.2f} p {p2:.4f}")
    # leave one out and drop ferulic acid / duplicated larotrectinib
    for drop in (["ferulic acid"], ["larotrectinib sulfate"], ["ferulic acid", "larotrectinib sulfate"]):
        m2 = mem & ~np.isin(names, drop)
        o, e, p = perm_test(zmin, m2, schemes["act10"], B, side="less")
        print(f"    drop {drop}: n {m2.sum()} mean z_min {o / m2.sum():+.2f} vs {e / m2.sum():+.2f} p {p:.4f}")
    # compare to all kinase-inhibitor-like moa_fine classes: how many classes reach this p by chance? (count classes)
    # z_min depends on number of doses: compounds with more drug-doses have lower min by construction
    x = dd.copy(); x["compound"] = [namefun(d) for d in x["drug"]]
    nd = x.groupby("compound").size()
    comp["n_dd"] = nd
    print("    n drug-doses per compound: class mean", comp.loc[mem, "n_dd"].mean().round(2), " all", comp["n_dd"].mean().round(2))
    print("    spearman z_min vs n drug-doses (all compounds):", round(stats.spearmanr(comp.z_min, comp.n_dd).statistic, 3))
