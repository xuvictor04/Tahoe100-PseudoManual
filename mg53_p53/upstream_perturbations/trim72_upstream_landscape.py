#!/usr/bin/env python3
"""MG53 (TRIM72) upstream: the perturbation landscape in Tahoe-100M (method-v3 corrected atlas effects).

Which drug-doses raise or lower TRIM72 mRNA, and what do they have in common?
  (a) every drug-dose ranked by TRIM72 z, by fold change and by a within-plate z, with q-values, flags, dose pattern,
      global activity, cell loss and plates; how TRIM72's plate baseline batch (plates 1-3 and 14 high, 4-13 low)
      distorts the fold-change ranking.
  (b) class enrichment (curated pharmacology classes, moa_fine, moa_broad, single targets) among TRIM72 raisers and
      lowerers, at the compound level, by permutation within strata of global activity (strong drugs move
      everything), with BH; unstratified Fisher tests alongside to show what activity matching changes.
  (c) specificity: where TRIM72 ranks among all genes for each raiser; how broad the drug-dose's program is; which
      genes rise together with TRIM72 in raisers beyond activity-matched non-raisers; genome-wide co-regulation
      partners of TRIM72 across drug-doses (raw and with global activity partialled out).
  (d) shared biology: TRIM72 z against the panel's programs (P53_ACTIVITY, ISR, NRF2, UPR, heat shock, IFN, NF-kB,
      cell cycle, proteasome), single genes (ATF3, DDIT3, PMAIP1, CDKN1A, MDM2, TP53, MYC, MCL1, HEXIM1) and two
      a-priori signatures (immediate-early genes, short-lived mRNAs) across drug-doses: rank and partial rank
      correlations, raisers vs activity-matched non-raisers, a multivariable rank model with a compound-cluster
      bootstrap.
  (d2) per cell line (the gene panel's own per-(well, line) corrected effects): is the TRIM72 rise of the raisers
      larger in TP53-wild-type lines (p53 upstream of TRIM72?), with CDKN1A / MDM2 as positive controls.

Everything is read-only on the data folder ($MG53_DATA, else $TAHOE_DATA, else ~/Tahoe-100M); outputs go to
tables/ in $MG53_OUT (default: next to this script):
  a_TRIM72_drugdose_ranking.csv          every drug-dose: fold, z, q, flags, dose pattern, activity, cell loss, plates,
                                         plate baseline, within-plate z / rank, pseudocount-free pooled fold, panel lines
  a_TRIM72_plate_baseline_and_spread.csv per plate: TRIM72 baseline CPM, spread of effects, plate factor
  a_TRIM72_plate_batch_checks.csv        how the baseline batch moves fold changes and ranks
  a_TRIM72_plate6_vs_plate14_pairs.csv   the same 92 drug-doses on a low- (6) and a high-baseline (14) plate
  a_TRIM72_top30_three_rankings.csv      top 30 by z, fold change and within-plate z, with all three ranks
  b_TRIM72_class_enrichment_compound_level.csv / _drugdose_level.csv, b_class_members.csv,
  b_TRIM72_compound_level.csv, b_activity_strata_compounds.csv, b_top_activity_stratum_compounds.csv
  c_TRIM72_specificity_in_raisers.csv, c_genes_coinduced_with_TRIM72_in_raisers.csv,
  c_raisers_and_matched_controls.csv, c_TRIM72_genomewide_partners_across_drugdoses.csv,
  c_muscle_and_myogenic_genes.csv
  d_program_scores_by_drugdose.csv, d_TRIM72_vs_programs_correlations.csv, d_TRIM72_multivariable_rank_model.csv,
  d_program_high_vs_TRIM72_raisers_active_drugdoses.csv, d_top20_drugdoses_per_program_with_TRIM72.csv,
  d_TRIM72_raiser_program_profile.csv
  d2_TRIM72_raisers_TP53_WT_vs_altered.csv, d2_TRIM72_TP53_contrast_across_drugdoses.csv,
  d2_TRIM72_TP53_contrast_by_drugdose.csv, d2_per_line_effects_raisers.csv

    python3 trim72_upstream_landscape.py                 # all parts (~40 s on 4 CPUs, peak ~2 GB)
    python3 trim72_upstream_landscape.py --skip-per-line # without part d2 (~15 s)

All associations; Tahoe has no MG53 perturbation, so nothing here is causal for MG53 -> p53.
"""
import argparse
import json
import os
import shutil
import sys
import tempfile
import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, REPO)
import tahoe_atlas as A                # noqa: E402  (read-only helpers: FX, flags, dose patterns)
import tahoe_mtap_gankyrin as T        # noqa: E402

DATA = os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA") or os.path.expanduser("~/Tahoe-100M")   # the Tahoe-100M folder with atlas/ and gene_panel/
ATLAS = os.path.join(DATA, "atlas")
EFF = os.path.join(ATLAS, "effects")
GP = os.path.join(DATA, "gene_panel")
GR = os.path.join(GP, "results")
OUTDIR = os.environ.get("MG53_OUT") or HERE      # tables/ (and cache/, external/) go here; run_mg53_p53.py sets it
TAB = os.path.join(OUTDIR, "tables")

GENE = "TRIM72"
Q_CUT, LFC_MIN = A.Q_CUT, A.LFC_MIN           # 0.10, log2(1.2): the atlas's significance rule
NOMINAL_DOWN_Z = -2.0                          # TRIM72 decreases are weak: a nominal cut for 'lowerer'
HIGH_BASELINE_CPM = 5.0                        # plates whose median line reads TRIM72 above this = high-baseline
MIN_LINES_RANKED = 25                          # genes expressed in >= half of the 50 lines enter gene ranks
SEED = 20261022

warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 50)
pd.set_option("display.max_colwidth", 80)


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def save(df, name, index=False):
    path = os.path.join(TAB, name)
    df.to_csv(path, index=index, float_format="%.6g")
    log(f"  wrote tables/{name} ({len(df)} rows)")
    return path


def bh(p):
    """Benjamini-Hochberg q-values (NaN kept)."""
    p = np.asarray(p, dtype=float)
    q = np.full(p.shape, np.nan)
    ok = np.isfinite(p)
    if ok.sum() == 0:
        return q
    pv = p[ok]
    o = np.argsort(pv)
    r = pv[o] * len(pv) / np.arange(1, len(pv) + 1)
    r = np.minimum.accumulate(r[::-1])[::-1]
    out = np.empty_like(pv)
    out[o] = np.minimum(r, 1.0)
    q[ok] = out
    return q


def mad(x):
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    return 1.4826 * np.median(np.abs(x - np.median(x))) if x.size else np.nan


def rank_resid(y, covs):
    """Ranks of y with the ranks of covs regressed out (OLS with intercept)."""
    ry = stats.rankdata(y)
    X = np.column_stack([np.ones(len(ry))] + [stats.rankdata(c) for c in covs]) if covs else np.ones((len(ry), 1))
    beta, *_ = np.linalg.lstsq(X, ry, rcond=None)
    return ry - X @ beta


def partial_spearman(x, y, covs):
    """Spearman of x and y with covs partialled out of both ranks; p from t with n - 2 - k df."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    cv = [np.asarray(c, float) for c in covs]
    for c in cv:
        ok &= np.isfinite(c)
    n, k = int(ok.sum()), len(cv)
    if n < k + 5:
        return np.nan, np.nan, n
    rx = rank_resid(x[ok], [c[ok] for c in cv])
    ry = rank_resid(y[ok], [c[ok] for c in cv])
    r = float(np.corrcoef(rx, ry)[0, 1])
    df = n - 2 - k
    t = r * np.sqrt(df / max(1e-12, 1 - r * r))
    p = float(2 * stats.t.sf(abs(t), df))
    return r, p, n


def strat_perm_matrix(values, strata, B, rng):
    """B x n matrix: `values` permuted within each stratum independently per row."""
    values = np.asarray(values, dtype=np.float32)
    out = np.empty((B, len(values)), dtype=np.float32)
    for s in np.unique(strata):
        idx = np.flatnonzero(strata == s)
        perm = np.argsort(rng.random((B, idx.size)), axis=1)
        out[:, idx] = values[idx][perm]
    return out


def quantile_strata(x, k):
    """k equal-count strata of x (ties broken by order)."""
    r = pd.Series(np.asarray(x, float)).rank(method="first").to_numpy()
    return np.minimum((r - 1) * k // len(r), k - 1).astype(int)


# ============================================================================= loading
class Data:
    def __init__(self):
        log("Loading the atlas effects (read-only) ...")
        self.fx = fx = A.FX(ATLAS)
        self.dd = dd = fx.dd.copy()
        dd["conc"] = dd["conc"].astype(float)
        self.genes = fx.genes
        self.c = fx.col_of(GENE)
        self.lfc = np.asarray(fx.DD_lfc, dtype=np.float32)
        self.z = np.asarray(fx.DD_z, dtype=np.float32)
        self.qup = np.asarray(fx.DD_qup, dtype=np.float32)
        self.qdn = np.asarray(fx.DD_qdn, dtype=np.float32)
        g = self.genes
        self.sym = g["symbol"].astype(str).to_numpy()
        self.ranked = np.flatnonzero((g["kind"] == "gene").to_numpy() & (g["n_lines_expressing"] >= MIN_LINES_RANKED))
        lvl = float(g.loc[self.c, "median_line_cpm"])
        self.level_matched = np.flatnonzero((g["kind"] == "gene").to_numpy()
                                            & (g["n_lines_expressing"] >= MIN_LINES_RANKED)
                                            & (g["median_line_cpm"] >= lvl / 4) & (g["median_line_cpm"] <= lvl * 4))
        self.trim72_level = lvl
        dd["compound"] = [T.salt_base(x).lower() for x in dd["drug"]]
        dd["activity"] = np.log1p(dd["n_sig_genes"].astype(float))
        dd["key"] = list(zip(dd["drug"], dd["conc"].round(4)))
        self.col = {s: int(i) for i, s in zip(g["col"], g["symbol"].astype(str)) if s not in ("nan",)}
        log(f"  {len(dd)} drug-doses, {len(g)} columns; TRIM72 = column {self.c} (median line {lvl:.2f} CPM); "
            f"ranked genes (expressed in >= {MIN_LINES_RANKED} lines): {len(self.ranked)}; level-matched "
            f"({lvl / 4:.2f}-{lvl * 4:.1f} CPM): {len(self.level_matched)}")

    def gene_z(self, symbol):
        c = self.col.get(symbol)
        return None if c is None else self.z[:, c].astype(float)


# ============================================================================= part a
def plate_baselines():
    """TRIM72 untreated level per plate: median over lines of the pooled CPM of the plate's drug wells / DMSO wells
    (profiles with >= 30 cells), from the gene panel's well x line sums."""
    import pyarrow.parquet as pq
    wl = pq.read_table(os.path.join(GP, "well_line.parquet"),
                       columns=["sample", "cell_line_id", "n_cells", "total_counts", GENE]).to_pandas()
    sm = pd.read_csv(os.path.join(GP, "sample_map.csv"), usecols=["sample", "plate", "is_dmso"])
    wl = wl.merge(sm, on="sample")
    wl = wl[wl["n_cells"] >= T.MIN_CELLS]
    out = {}
    for lab, sub in (("drug_wells", wl[~wl["is_dmso"].astype(bool)]), ("dmso_wells", wl[wl["is_dmso"].astype(bool)])):
        g = sub.groupby(["plate", "cell_line_id"])[[GENE, "total_counts"]].sum()
        cpm = g[GENE] / g["total_counts"] * 1e6
        out[f"TRIM72_median_line_cpm_{lab}"] = cpm.groupby(level="plate").median()
    # per well, pseudocount-free and uncorrected (a check on the corrected values, which use log2(count + 0.5)):
    # TRIM72 reads observed vs expected from each line's pooled CPM over the plate's drug wells, the well's pooled
    # CPM, and the pseudocount floor (median over lines of 0.5 / UMIs x 1e6: what a line with zero reads reads as)
    dw = wl[~wl["is_dmso"].astype(bool)]
    g = dw.groupby(["plate", "cell_line_id"])[[GENE, "total_counts"]].sum()
    base = (g[GENE] / g["total_counts"] * 1e6).rename("base")
    x = wl.join(base, on=["plate", "cell_line_id"])
    x["exp"] = x["base"] * x["total_counts"] / 1e6
    x["floor"] = 0.5 / x["total_counts"] * 1e6
    per_well = x.groupby("sample").agg(obs_reads=(GENE, "sum"), exp_reads=("exp", "sum"), umis=("total_counts", "sum"),
                                       floor_cpm=("floor", "median"))
    return pd.DataFrame(out), per_well


def part_a(D):
    log("Part a: ranking of every drug-dose and the plate-baseline batch ...")
    fx, dd, c = D.fx, D.dd, D.c
    w = fx.wells.copy()
    w["W2"] = np.asarray(fx.W2[:, c], dtype=float)
    w["Z"] = np.asarray(fx.Z[:, c], dtype=float)
    w["plate_factor_gene"] = fx.gene_scale([c])[:, 0]
    drug_w = fx.drug_w
    # within-plate view: each drug well against the other drug wells of its own plate (robust z and percentile)
    w["wp_z"] = np.nan
    w["wp_pct"] = np.nan
    for p, ii in w[drug_w].groupby("plate").indices.items():
        rows = np.flatnonzero(drug_w)[ii]
        v = w["W2"].to_numpy()[rows]
        w.loc[w.index[rows], "wp_z"] = (v - np.nanmedian(v)) / mad(v)
        w.loc[w.index[rows], "wp_pct"] = pd.Series(v).rank(pct=True).to_numpy()

    pb, well_cpm = plate_baselines()
    for k in ("obs_reads", "exp_reads", "umis", "floor_cpm"):
        w[k] = w["sample"].astype(str).map(well_cpm[k]).to_numpy()
    w["rank_in_plate"] = np.nan
    for p, ii in w[drug_w].groupby("plate").indices.items():
        rows = np.flatnonzero(drug_w)[ii]
        w.loc[w.index[rows], "rank_in_plate"] = pd.Series(-w["W2"].to_numpy()[rows]).rank(method="min").to_numpy()
    n_in_plate = w[drug_w].groupby("plate").size().to_dict()
    pb["baseline_group"] = np.where(pb["TRIM72_median_line_cpm_drug_wells"] >= HIGH_BASELINE_CPM, "high", "low")
    high = set(pb.index[pb["baseline_group"] == "high"])
    log(f"  high-baseline plates (median line >= {HIGH_BASELINE_CPM:g} CPM in drug wells): {sorted(high)}")

    t = dd[["drug", "conc", "compound", "targets", "moa_fine", "moa_broad", "n_wells", "plates", "wells"]].copy()
    t["fold_change"] = 2.0 ** D.lfc[:, c]
    t["log2FC"] = D.lfc[:, c]
    t["z"] = D.z[:, c]
    t["q_up"] = D.qup[:, c]
    t["q_down"] = D.qdn[:, c]
    t["sig_up"] = (t["q_up"] < Q_CUT) & (t["log2FC"] >= LFC_MIN)
    t["sig_down"] = (t["q_down"] < Q_CUT) & (t["log2FC"] <= -LFC_MIN)
    t["nominal_down"] = t["z"] <= NOMINAL_DOWN_Z
    pats_up = [fx.dose_pattern(c, d) for d in t["drug"]]
    t["z_by_dose"] = [p[1] for p in pats_up]
    t["dose_pattern_up"] = [p[0] for p in pats_up]
    t["dose_pattern_down"] = [fx.dose_pattern(c, d, sign=-1)[0] for d in t["drug"]]
    t["flags"] = A.gene_flag_col(fx, c)
    t["position"] = A.position_flag(fx, c)
    t["plate_factor_gene"] = fx.gene_plate_scale(c)
    for k in ("n_genes_up", "n_genes_down", "n_sig_genes", "cells_log2_vs_plate", "cells_log2_best_well",
              "genes_per_cell_log2_vs_plate", "composition_shift_log2", "S_PHASE_z", "G2M_PHASE_z", "replicate_r",
              "unreliable_plate_only"):
        t[k] = dd[k].to_numpy()
    t["activity_decile"] = quantile_strata(dd["activity"], 10) + 1
    # per drug-dose: used wells' within-plate z (Stouffer) and percentile (mean), baseline of their plates
    wpz, wpp, base, grp, used_plates, rk_txt, best_rk, pooled = [], [], [], [], [], [], [], []
    bmap = pb["TRIM72_median_line_cpm_drug_wells"].to_dict()
    for i in range(len(dd)):
        ii = fx.wells_of_dd.get(i, np.array([], int))
        v = w["wp_z"].to_numpy()[ii]
        v = v[np.isfinite(v)]
        wpz.append(v.sum() / np.sqrt(len(v)) if len(v) else np.nan)
        wpp.append(np.nanmean(w["wp_pct"].to_numpy()[ii]) if len(ii) else np.nan)
        pl = list(w["plate"].to_numpy()[ii])
        used_plates.append(",".join(sorted(set(pl), key=lambda s: int(s.replace("plate", "")))))
        rks = w["rank_in_plate"].to_numpy()[ii]
        rk_txt.append("; ".join(f"{p}: {int(r)} of {n_in_plate[p]}" for p, r in zip(pl, rks) if np.isfinite(r)))
        best_rk.append(float(np.nanmin(rks)) if len(ii) and np.isfinite(rks).any() else np.nan)
        ob, ex, um, fl = (w[k].to_numpy()[ii] for k in ("obs_reads", "exp_reads", "umis", "floor_cpm"))
        pooled.append((np.nansum(ob), np.nansum(ex), 1e6 * np.nansum(ob) / np.nansum(um) if len(ii) else np.nan,
                       1e6 * np.nansum(ex) / np.nansum(um) if len(ii) else np.nan, np.nanmax(fl) if len(ii) else np.nan,
                       "; ".join(f"{p}: {o / e:.2f}x" for p, o, e in zip(pl, ob, ex) if e > 0)))
        base.append(float(np.exp(np.mean(np.log([bmap[p] for p in pl])))) if pl else np.nan)
        hs = {p in high for p in pl}
        grp.append("high (plates " + ",".join(sorted({p.replace('plate', '') for p in pl if p in high}, key=int)) + ")"
                   if hs == {True} else "low" if hs == {False} else "mixed (high + low)" if hs else "")
    t["used_plates"] = used_plates
    t["plate_baseline_cpm"] = base
    t["plate_baseline_group"] = ["high" if g.startswith("high") else g for g in grp]
    t["within_plate_z"] = wpz
    t["within_plate_pct"] = wpp
    t["rank_in_plate_by_well"] = rk_txt          # 1 = the largest TRIM72 increase among the plate's drug wells
    t["best_rank_in_plate"] = best_rk
    t["TRIM72_reads_used_wells"] = [p_[0] for p_ in pooled]
    t["TRIM72_reads_expected_from_plate_baseline"] = [p_[1] for p_ in pooled]
    t["pooled_fold_no_pseudocount"] = t["TRIM72_reads_used_wells"] / t["TRIM72_reads_expected_from_plate_baseline"]
    t["pooled_fold_no_pseudocount_by_well"] = [p_[5] for p_ in pooled]
    t["treated_pooled_cpm"] = [p_[2] for p_ in pooled]
    t["same_lines_baseline_pooled_cpm"] = [p_[3] for p_ in pooled]
    t["pseudocount_floor_cpm"] = [p_[4] for p_ in pooled]       # worst used well: median over its lines
    t["pseudocount_floor_above_baseline"] = t["pseudocount_floor_cpm"] > t["plate_baseline_cpm"]
    t["rank_z_up"] = (-t["z"]).rank(method="min")
    t["rank_fold_up"] = (-t["log2FC"]).rank(method="min")
    t["rank_within_plate_up"] = (-t["within_plate_z"]).rank(method="min")
    t["rank_z_down"] = t["z"].rank(method="min")
    t["rank_fold_down"] = t["log2FC"].rank(method="min")
    t["rank_within_plate_down"] = t["within_plate_z"].rank(method="min")
    # the panel's per-line view of the same drug-dose (lines measured / up / down)
    pan = pd.read_csv(os.path.join(GR, f"{GENE}_drug_effects_by_dose.csv"),
                      usecols=["drug", "conc", "call", "n_lines", "n_lines_up", "n_lines_down", "frac_lines_positive",
                               "z_corrected"])
    pan["key"] = list(zip(pan["drug"], pan["conc"].astype(float).round(4)))
    pan = pan.drop(columns=["drug", "conc"]).rename(columns={"call": "panel_call", "n_lines": "panel_n_lines",
                                                             "n_lines_up": "panel_n_lines_up",
                                                             "n_lines_down": "panel_n_lines_down",
                                                             "frac_lines_positive": "panel_frac_lines_positive",
                                                             "z_corrected": "panel_z"})
    t["key"] = dd["key"].to_numpy()
    t = t.merge(pan, on="key", how="left").drop(columns="key")
    t.index = dd.index
    log(f"  atlas z vs panel z for TRIM72: Pearson r = {np.corrcoef(t['z'], t['panel_z'].fillna(0))[0, 1]:.4f} "
        f"(max |diff| {np.nanmax(np.abs(t['z'] - t['panel_z'])):.3g})")
    t = t.sort_values("z", ascending=False)
    save(t, "a_TRIM72_drugdose_ranking.csv")

    # ---- plate table
    d = w[drug_w]
    pt = d.groupby("plate").agg(n_drug_wells=("W2", "size"), median_W2=("W2", "median"), mad_W2=("W2", mad),
                                mad_Z=("Z", mad), plate_factor_gene_median=("plate_factor_gene", "median"),
                                p95_W2=("W2", lambda x: np.nanpercentile(x, 95)), max_W2=("W2", "max"),
                                n_wells_W2_ge_1=("W2", lambda x: int((x >= 1).sum())),
                                n_wells_Z_ge_3=("Z", lambda x: int((x >= 3).sum())))
    pt = pb.join(pt)
    pt["unreliable_plate"] = pt.index.isin(fx.unreliable)
    pt = pt.loc[sorted(pt.index, key=lambda s: int(s.replace("plate", "")))]
    pt.index.name = "plate"
    save(pt.reset_index(), "a_TRIM72_plate_baseline_and_spread.csv")

    # ---- batch checks
    rows = []
    rs = stats.spearmanr(t["z"], t["log2FC"])
    rows.append(("spearman z vs log2FC, all drug-doses", len(t), rs.statistic, rs.pvalue, ""))
    rs = stats.spearmanr(t["z"], t["within_plate_z"], nan_policy="omit")
    rows.append(("spearman z vs within-plate z, all drug-doses", len(t), rs.statistic, rs.pvalue, ""))
    share_all = (t["plate_baseline_group"] == "low").mean()
    rows.append(("share of all drug-doses on low-baseline plates only", len(t), share_all, np.nan, ""))
    for N in (10, 20, 50):
        for lab, col in (("fold change", "log2FC"), ("z", "z"), ("within-plate z", "within_plate_z")):
            top = t.sort_values(col, ascending=False).head(N)
            sh = (top["plate_baseline_group"] == "low").mean()
            p = stats.binomtest(int((top["plate_baseline_group"] == "low").sum()), N, share_all,
                                alternative="greater").pvalue
            rows.append((f"top {N} increases by {lab}: share on low-baseline plates only", N, sh, p,
                         "binomial vs the share among all drug-doses (one-sided, greater)"))
    # is the noise (spread of the plate's drug wells) larger on low-baseline plates? (it would deflate z there)
    pm = w[drug_w & ~w["plate"].isin(fx.unreliable).to_numpy()].groupby("plate")["W2"].agg(mad)
    hi_m, lo_m = pm[pm.index.isin(high)], pm[~pm.index.isin(high)]
    mw = stats.mannwhitneyu(lo_m, hi_m)
    rows.append(("spread (MAD) of TRIM72 log2 effects across drug wells: low- vs high-baseline plates (reliable)",
                 len(pm), float(lo_m.median() - hi_m.median()), mw.pvalue,
                 f"median MAD low {lo_m.median():.3f} (n {len(lo_m)}) vs high {hi_m.median():.3f} (n {len(hi_m)}); "
                 "Mann-Whitney"))
    # significant increases without the pseudocount: reads observed vs expected (uncorrected, pooled over lines)
    s_ = t[t["sig_up"]]
    rs = stats.spearmanr(s_["log2FC"], np.log2(s_["pooled_fold_no_pseudocount"]))
    rows.append(("significant increases: spearman corrected log2FC vs pseudocount-free pooled log2 fold", len(s_),
                 rs.statistic, rs.pvalue,
                 "; ".join(f"{r.drug} {r.conc:g}: corrected {r.fold_change:.2f}x, pooled {r.pooled_fold_no_pseudocount:.2f}x "
                           f"({int(r.TRIM72_reads_used_wells)} reads vs {r.TRIM72_reads_expected_from_plate_baseline:.0f} "
                           f"expected; floor {r.pseudocount_floor_cpm:.2f} vs baseline {r.plate_baseline_cpm:.2f} CPM)"
                           for r in s_.sort_values("z", ascending=False).itertuples())))
    s_ = t[t["sig_up"] & t["pseudocount_floor_above_baseline"]]
    rows.append(("significant increases whose pseudocount floor exceeds the plate baseline (inflated by low UMIs)",
                 len(s_), np.nan, np.nan, "; ".join(f"{r.drug} {r.conc:g}" for r in s_.itertuples())))
    # plate 3 (high baseline, the noisiest TRIM72 plate: z divisor 1.91): fold changes without z
    s3 = t[(t["used_plates"] == "plate3") & (t["fold_change"] >= 2) & (t["z"] < 3)]
    rows.append(("plate-3-only drug-doses with >= 2x but z < 3 (fold ranking promotes them)", len(s3),
                 float(s3["z"].median()) if len(s3) else np.nan, np.nan,
                 "; ".join(f"{r.drug} {r.conc:g} {r.fold_change:.2f}x z {r.z:.2f} rank fold {int(r.rank_fold_up)} "
                           f"rank z {int(r.rank_z_up)}" for r in s3.itertuples())))
    # paired: the same drug-dose on plate 6 (low baseline) and plate 14 (high)
    pairs = []
    W2v, Zv, wpzv = w["W2"].to_numpy(), w["Z"].to_numpy(), w["wp_z"].to_numpy()
    for i in range(len(dd)):
        ii = fx.wells_of_dd.get(i, np.array([], int))
        pl = list(w["plate"].to_numpy()[ii])
        if "plate6" in pl and "plate14" in pl and len(ii) == 2:
            a, b = ii[pl.index("plate6")], ii[pl.index("plate14")]
            pairs.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "W2_plate6": W2v[a],
                          "W2_plate14": W2v[b], "Z_plate6": Zv[a], "Z_plate14": Zv[b],
                          "within_plate_z_plate6": wpzv[a], "within_plate_z_plate14": wpzv[b],
                          "drugdose_z": D.z[i, c], "drugdose_fold": 2 ** D.lfc[i, c]})
    pr = pd.DataFrame(pairs).sort_values("drugdose_z", ascending=False)
    save(pr, "a_TRIM72_plate6_vs_plate14_pairs.csv")
    rs = stats.spearmanr(pr["W2_plate6"], pr["W2_plate14"])
    rows.append(("plate6 vs plate14 (same drug-dose, same position): spearman of log2 effect", len(pr), rs.statistic,
                 rs.pvalue, ""))
    ts = stats.theilslopes(pr["W2_plate6"], pr["W2_plate14"])
    rows.append(("plate6 vs plate14: Theil-Sen slope of log2 effect (plate6 on plate14)", len(pr), ts.slope, np.nan,
                 f"95% CI {ts.low_slope:.2f}-{ts.high_slope:.2f}; > 1 = plate-6 (low baseline) folds larger"))
    ts = stats.theilslopes(pr["Z_plate6"], pr["Z_plate14"])
    rows.append(("plate6 vs plate14: Theil-Sen slope of z (plate6 on plate14)", len(pr), ts.slope, np.nan,
                 f"95% CI {ts.low_slope:.2f}-{ts.high_slope:.2f}"))
    strong = pr[pr["drugdose_z"] >= 3]
    for _, r in strong.iterrows():
        rows.append((f"plate6/plate14 log2 effect ratio: {r['drug']} {r['conc']:g} uM", 2,
                     r["W2_plate6"] / r["W2_plate14"], np.nan,
                     f"plate6 {2 ** r['W2_plate6']:.2f}x (z {r['Z_plate6']:.1f}) vs plate14 {2 ** r['W2_plate14']:.2f}x "
                     f"(z {r['Z_plate14']:.1f})"))
    save(pd.DataFrame(rows, columns=["check", "n", "value", "p", "note"]), "a_TRIM72_plate_batch_checks.csv")

    # compact: the top 30 of each ranking with all three ranks
    keep = set()
    for col in ("rank_z_up", "rank_fold_up", "rank_within_plate_up"):
        keep |= set(t.index[t[col] <= 30])
    top = t.loc[sorted(keep, key=lambda i: t.at[i, "rank_z_up"])]
    cols = ["drug", "conc", "fold_change", "z", "q_up", "within_plate_z", "rank_z_up", "rank_fold_up",
            "rank_within_plate_up", "rank_in_plate_by_well", "plate_baseline_group", "used_plates",
            "plate_baseline_cpm", "pooled_fold_no_pseudocount", "pooled_fold_no_pseudocount_by_well",
            "TRIM72_reads_used_wells", "pseudocount_floor_cpm", "n_sig_genes",
            "cells_log2_vs_plate", "dose_pattern_up", "z_by_dose", "flags", "panel_n_lines_up", "panel_n_lines"]
    save(top[cols], "a_TRIM72_top30_three_rankings.csv")
    return t


# ============================================================================= part b
CURATED = {
    "anthracycline (TOP2 poison)": ["Idarubicin (hydrochloride)", "Epirubicin (hydrochloride)",
                                    "Doxorubicin (hydrochloride)"],
    "TOP2 poison (anthracyclines, mitoxantrone, amsacrine)": ["Idarubicin (hydrochloride)",
                                                              "Epirubicin (hydrochloride)",
                                                              "Doxorubicin (hydrochloride)",
                                                              "Mitoxantrone (dihydrochloride)", "Amsacrine"],
    "TOP1 inhibitor": ["Topotecan (hydrochloride)", "Irinotecan", "Irinotecan (hydrochloride)"],
    "alkylating / platinum": ["Bendamustine", "Busulfan", "Oxaliplatin", "Altretamine"],
    "antimetabolite / nucleoside analogue": ["5-Fluorouracil", "Cytarabine", "Cytarabine (hydrochloride)",
                                             "Gemcitabine", "Clofarabine", "Hydroxyurea", "Methotrexate",
                                             "Pemetrexed", "Raltitrexed", "Trifluridine", "Trimetrexate",
                                             "Idoxuridine"],
    "DNMT inhibitor (azanucleoside)": ["5-Azacytidine", "Decitabine"],
    "DDR kinase / PARP inhibitor": ["AZD1390", "Elimusertib hydrochloride", "AZD-7648", "Rucaparib (phosphate)",
                                    "olaparib"],
    "DNA-damaging cytotoxic (TOP1/TOP2/alkylating/antimetabolite)": None,     # union, filled below
    "ribosome-binding translation inhibitor (harringtonines)": ["Homoharringtonine", "Harringtonine"],
    "translation initiation (eIF4 / MNK) inhibitor": ["4EGI-1", "Tomivosertib", "SBI-0640756", "ETC-206"],
    "transcriptional CDK (CDK9-active) inhibitor": ["Dinaciclib", "AT7519"],
    "CDK4/6 inhibitor": ["palbociclib", "Ribociclib", "Abemaciclib"],
    "HDAC inhibitor (pan / class I)": ["Panobinostat", "Belinostat", "Tucidinostat"],
    "proteasome inhibitor": ["Bortezomib", "Ixazomib", "Ixazomib citrate"],
    "microtubule agent": ["Docetaxel", "Docetaxel (Trihydrate)", "Paclitaxel", "Vinblastine (sulfate)",
                          "vincristine", "Mebendazole", "Tubulin inhibitor 6"],
    "mitotic kinase (Aurora / PLK) inhibitor": ["TAK-901", "Volasertib"],
    "cardiac glycoside (Na/K-ATPase)": ["Ouabain (Octahydrate)", "Digitoxin"],
    "thiol-reactive / redox (TXNRD, arsenical, fumarate, quinone)": ["Auranofin", "Darinaparsin",
                                                                     "Dimethyl fumarate", "Menadione"],
    "MEK inhibitor": ["Binimetinib", "Cobimetinib", "TAK-733", "Trametinib", "Trametinib (DMSO_TF solvate)"],
    "RAF inhibitor": ["Dabrafenib", "Encorafenib", "Vemurafenib"],
    "ERK inhibitor": ["MK-8353", "Temuterkib"],
    "RAF/MEK/ERK inhibitor (any)": None,                                       # union
    "KRAS / SOS1 inhibitor": ["Adagrasib", "BI-3406", "RMC-6236"],
    "FGFR inhibitor": ["Erdafitinib", "Futibatinib", "Infigratinib", "Pemigatinib"],
    "BCR-ABL / multi-RTK inhibitor (ponatinib-like)": ["Ponatinib", "Radotinib", "Flumatinib (mesylate)",
                                                       "Asciminib", "c-Kit-IN-1"],
    "VEGFR/PDGFR/MET/RET multi-kinase inhibitor": ["Cabozantinib (S-malate)", "Sunitinib", "Regorafenib",
                                                   "Sulfatinib", "Vandetanib", "Pexidartinib (hydrochloride)",
                                                   "Pralsetinib", "Crizotinib (hydrochloride)", "crizotinib",
                                                   "Capmatinib"],
    "EGFR/ERBB inhibitor": ["Afatinib", "Almonertinib (hydrochloride)", "Almonertinib (mesylate)", "Erlotinib",
                            "Gefitinib", "Lapatinib ditosylate", "Neratinib", "Neratinib (maleate)",
                            "Osimertinib (mesylate)", "Simotinib", "Tucatinib"],
    "receptor tyrosine kinase inhibitor (any of the above RTK classes)": None,  # union
    "PI3K / AKT / mTOR inhibitor": ["Alpelisib", "BAY1125976", "Bimiralisib", "Capivasertib", "GSK1059615",
                                    "Ipatasertib", "AZD-8055", "Everolimus", "Rapamycin", "Sapanisertib",
                                    "Temsirolimus", "Torkinib", "LY-2584702 (tosylate salt)"],
    "JAK inhibitor": ["Fedratinib (hydrochloride hydrate)", "Filgotinib", "Tofacitinib", "Tofacitinib (citrate)"],
    "p38 / JNK / other MAPK-family inhibitor": ["PH-797804", "Ralimetinib dimesylate", "Bentamapimod", "NG25",
                                                "PF-06260933", "OTS514", "ERK5-IN-2", "LJI308"],
    "glucocorticoid": ["Betamethasone dipropionate", "Budesonide", "Dexamethasone", "Methylprednisolone succinate",
                       "Triamcinolone"],
    "statin": ["Pitavastatin (Calcium)", "Pravastatin (sodium)"],
    "GSK3 inhibitor": ["9-ING-41", "AZD2858", "CP21R7", "LY2090314"],
    "retinoid / rexinoid": ["Bexarotene", "Peretinoin", "Retinoic acid", "Tazarotene"],
    "cyclooxygenase inhibitor (NSAID)": ["Aspirin", "Celecoxib", "Meloxicam", "Naproxen", "Nimesulide", "Oxaprozin",
                                         "Piroxicam", "Sodium Salicylate", "Tolmetin", "Valdecoxib",
                                         "Salicylic acid"],
}
CURATED["protein kinase inhibitor (any curated kinase class)"] = None             # union, filled below
CURATED["DNA-damaging cytotoxic (TOP1/TOP2/alkylating/antimetabolite)"] = sorted(set(
    CURATED["TOP2 poison (anthracyclines, mitoxantrone, amsacrine)"] + CURATED["TOP1 inhibitor"]
    + CURATED["alkylating / platinum"] + CURATED["antimetabolite / nucleoside analogue"]))
CURATED["RAF/MEK/ERK inhibitor (any)"] = sorted(set(CURATED["MEK inhibitor"] + CURATED["RAF inhibitor"]
                                                    + CURATED["ERK inhibitor"]))
CURATED["receptor tyrosine kinase inhibitor (any of the above RTK classes)"] = sorted(set(
    CURATED["FGFR inhibitor"] + CURATED["BCR-ABL / multi-RTK inhibitor (ponatinib-like)"]
    + CURATED["VEGFR/PDGFR/MET/RET multi-kinase inhibitor"] + CURATED["EGFR/ERBB inhibitor"]))
CURATED["protein kinase inhibitor (any curated kinase class)"] = sorted(set(
    CURATED["receptor tyrosine kinase inhibitor (any of the above RTK classes)"] + CURATED["RAF/MEK/ERK inhibitor (any)"]
    + CURATED["PI3K / AKT / mTOR inhibitor"] + CURATED["JAK inhibitor"] + CURATED["p38 / JNK / other MAPK-family inhibitor"]
    + CURATED["GSK3 inhibitor"] + CURATED["CDK4/6 inhibitor"] + CURATED["transcriptional CDK (CDK9-active) inhibitor"]
    + CURATED["mitotic kinase (Aurora / PLK) inhibitor"] + ["AZD1390", "Elimusertib hydrochloride", "AZD-7648"]))


def compound_table(D, t):
    """One row per compound (salt forms merged): z at each dose (Stouffer over forms), its max and min over doses,
    any significant increase / nominal decrease, activity (max log1p n_sig_genes over its drug-doses)."""
    dd = D.dd
    x = pd.DataFrame({"compound": dd["compound"].to_numpy(), "drug": dd["drug"].to_numpy(),
                      "conc": dd["conc"].round(4).to_numpy(), "z": t.sort_index()["z"].to_numpy(),
                      "sig_up": t.sort_index()["sig_up"].to_numpy(), "nominal_down": t.sort_index()["nominal_down"].to_numpy(),
                      "sig_down": t.sort_index()["sig_down"].to_numpy(), "activity": dd["activity"].to_numpy(),
                      "n_sig_genes": dd["n_sig_genes"].to_numpy(), "moa_fine": dd["moa_fine"].to_numpy(),
                      "moa_broad": dd["moa_broad"].to_numpy(), "targets": dd["targets"].to_numpy()})
    per_dose = x.groupby(["compound", "conc"])["z"].agg(lambda s: s.sum() / np.sqrt(len(s))).reset_index()
    g = per_dose.groupby("compound")["z"]
    comp = pd.DataFrame({"z_max": g.max(), "z_min": g.min(), "n_doses": g.size()})
    gx = x.groupby("compound")
    comp["drugs"] = gx["drug"].agg(lambda s: "; ".join(sorted(set(s))))
    comp["raiser"] = gx["sig_up"].any()
    comp["lowerer_nominal"] = gx["nominal_down"].any()
    comp["sig_down"] = gx["sig_down"].any()
    comp["activity"] = gx["activity"].max()
    comp["max_n_sig_genes"] = gx["n_sig_genes"].max()
    comp["moa_fine"] = gx["moa_fine"].agg(lambda s: "; ".join(sorted({v for v in s if v and v != "nan"})))
    comp["moa_broad"] = gx["moa_broad"].agg(lambda s: "; ".join(sorted({v for v in s if v and v != "nan"})))
    comp["targets"] = gx["targets"].agg(lambda s: ", ".join(sorted({u.strip() for v in s for u in
                                                                    str(v).replace(";", ",").split(",")
                                                                    if u.strip() and u.strip() != "nan"})))
    comp["best_up"] = x.loc[x.groupby("compound")["z"].idxmax()].set_index("compound").apply(
        lambda r: f"{r['drug']} {r['conc']:g} uM (z {r['z']:.2f})", axis=1)
    comp["best_down"] = x.loc[x.groupby("compound")["z"].idxmin()].set_index("compound").apply(
        lambda r: f"{r['drug']} {r['conc']:g} uM (z {r['z']:.2f})", axis=1)
    return comp


def class_systems(D, comp):
    """{system: {class: set(compounds)}} at the compound level."""
    base = {d: T.salt_base(d).lower() for d in D.dd["drug"].unique()}
    known = set(D.dd["drug"])
    systems = {"curated": {}, "moa_fine": {}, "moa_broad": {}, "target": {}}
    for k, drugs in CURATED.items():
        miss = [d for d in drugs if d not in known]
        if miss:
            sys.exit(f"curated class {k}: drug names not in the data: {miss}")
        systems["curated"][k] = {base[d] for d in drugs}
    for cp, r in comp.iterrows():
        for v in [s for s in r["moa_fine"].split("; ") if s and s != "unclear"]:
            systems["moa_fine"].setdefault(v, set()).add(cp)
        for v in [s for s in r["moa_broad"].split("; ") if s]:
            systems["moa_broad"].setdefault(v, set()).add(cp)
        for v in [s for s in r["targets"].split(", ") if s]:
            systems["target"].setdefault(v, set()).add(cp)
    return {s: {k: v for k, v in cl.items() if len(v) >= 2} for s, cl in systems.items()}


def part_b(D, t, B):
    log(f"Part b: class enrichment (compound level, {B} stratified permutations) ...")
    rng = np.random.default_rng(SEED)
    comp = compound_table(D, t)
    comp["activity_stratum"] = quantile_strata(comp["activity"], 10) + 1
    st = comp["activity_stratum"].to_numpy()
    comp["z_max_resid"] = comp["z_max"] - comp.groupby("activity_stratum")["z_max"].transform("median")
    comp["z_min_resid"] = comp["z_min"] - comp.groupby("activity_stratum")["z_min"].transform("median")
    systems = class_systems(D, comp)
    names = comp.index.to_numpy()
    pos = {n: i for i, n in enumerate(names)}
    # strata summary
    ss = comp.groupby("activity_stratum").agg(n_compounds=("z_max", "size"),
                                              min_n_sig_genes=("max_n_sig_genes", "min"),
                                              max_n_sig_genes=("max_n_sig_genes", "max"),
                                              n_raisers=("raiser", "sum"), n_lowerers_nominal=("lowerer_nominal", "sum"),
                                              median_z_max=("z_max", "median"), median_z_min=("z_min", "median"))
    save(ss.reset_index(), "b_activity_strata_compounds.csv")

    perm = {
        "raiser": strat_perm_matrix(comp["raiser"].astype(float).to_numpy(), st, B, rng),
        "lowerer_nominal": strat_perm_matrix(comp["lowerer_nominal"].astype(float).to_numpy(), st, B, rng),
        "z_max": strat_perm_matrix(comp["z_max"].to_numpy(), st, B, rng),
        "z_min": strat_perm_matrix(comp["z_min"].to_numpy(), st, B, rng),
    }
    obsv = {k: comp[k].astype(float).to_numpy() for k in perm}
    rows, members_rows = [], []
    for sysname, classes in systems.items():
        keys = sorted(classes)
        M = np.zeros((len(keys), len(names)), dtype=np.float32)
        for j, k in enumerate(keys):
            for cp in classes[k]:
                M[j, pos[cp]] = 1
        size = M.sum(axis=1)
        nullsum = {k: perm[k] @ M.T for k in perm}            # B x classes
        for j, k in enumerate(keys):
            mem = M[j].astype(bool)
            o = {kk: float(obsv[kk][mem].sum()) for kk in perm}
            r = {"system": sysname, "class": k, "n_compounds": int(size[j]),
                 "compounds": "; ".join(sorted(names[mem])),
                 "n_in_top_activity_stratum": int((st[mem] == st.max()).sum()),
                 "median_max_n_sig_genes": float(np.median(comp["max_n_sig_genes"].to_numpy()[mem]))}
            for lab, kk, side in (("raisers", "raiser", 1), ("lowerers_nominal", "lowerer_nominal", 1)):
                nul = nullsum[kk][:, j]
                r[f"n_{lab}"] = int(o[kk])
                r[f"{lab}_names"] = "; ".join(sorted(names[mem & (obsv[kk] > 0)]))
                r[f"expected_{lab}_activity_matched"] = float(nul.mean())
                r[f"obs_over_exp_{lab}"] = o[kk] / nul.mean() if nul.mean() > 0 else np.nan
                r[f"p_{lab}_stratified"] = (1 + int((nul >= o[kk] - 1e-9).sum())) / (B + 1)
                a = int(o[kk])
                b_ = int(size[j]) - a
                cc = int(obsv[kk].sum()) - a
                d_ = len(names) - int(size[j]) - cc
                orr, pf = stats.fisher_exact([[a, b_], [cc, d_]], alternative="greater")
                r[f"fisher_OR_{lab}_unstratified"] = orr
                r[f"fisher_p_{lab}_unstratified"] = pf
            nul = nullsum["z_max"][:, j] / size[j]
            r["mean_z_max"] = o["z_max"] / size[j]
            r["mean_z_max_resid"] = float(comp["z_max_resid"].to_numpy()[mem].mean())
            r["p_mean_z_max_up_stratified"] = (1 + int((nul >= r["mean_z_max"] - 1e-9).sum())) / (B + 1)
            nul = nullsum["z_min"][:, j] / size[j]
            r["mean_z_min"] = o["z_min"] / size[j]
            r["mean_z_min_resid"] = float(comp["z_min_resid"].to_numpy()[mem].mean())
            r["p_mean_z_min_down_stratified"] = (1 + int((nul <= r["mean_z_min"] + 1e-9).sum())) / (B + 1)
            # leave-one-compound-out: does the class's raise signal hinge on one compound?
            if size[j] >= 3:
                loo = []
                for cp in names[mem]:
                    m2 = mem.copy()
                    m2[pos[cp]] = False
                    loo.append(comp["z_max_resid"].to_numpy()[m2].mean())
                r["mean_z_max_resid_min_leave_one_out"] = float(np.min(loo))
                loo = []
                for cp in names[mem]:
                    m2 = mem.copy()
                    m2[pos[cp]] = False
                    loo.append(comp["z_min_resid"].to_numpy()[m2].mean())
                r["mean_z_min_resid_max_leave_one_out"] = float(np.max(loo))
            rows.append(r)
            for cp in names[mem]:
                members_rows.append({"system": sysname, "class": k, "compound": cp, "drugs": comp.at[cp, "drugs"],
                                     "z_max": comp.at[cp, "z_max"], "z_min": comp.at[cp, "z_min"],
                                     "raiser": comp.at[cp, "raiser"], "lowerer_nominal": comp.at[cp, "lowerer_nominal"],
                                     "max_n_sig_genes": comp.at[cp, "max_n_sig_genes"],
                                     "activity_stratum": comp.at[cp, "activity_stratum"],
                                     "best_up": comp.at[cp, "best_up"], "best_down": comp.at[cp, "best_down"]})
    res = pd.DataFrame(rows)
    for pcol in ("p_raisers_stratified", "p_lowerers_nominal_stratified", "p_mean_z_max_up_stratified",
                 "p_mean_z_min_down_stratified", "fisher_p_raisers_unstratified", "fisher_p_lowerers_nominal_unstratified"):
        res[pcol.replace("p_", "q_", 1) if pcol.startswith("p_") else pcol.replace("_p_", "_q_")] = \
            res.groupby("system")[pcol].transform(lambda s: pd.Series(bh(s.to_numpy()), index=s.index))
    res = res.sort_values(["system", "p_mean_z_max_up_stratified"])
    save(res, "b_TRIM72_class_enrichment_compound_level.csv")
    save(pd.DataFrame(members_rows), "b_class_members.csv")
    cur_of = {}
    for k, cps in systems["curated"].items():
        for cp in cps:
            cur_of.setdefault(cp, []).append(k)
    comp["curated_classes"] = [" | ".join(sorted(cur_of.get(cp, []))) for cp in comp.index]
    comp_out = comp.reset_index().sort_values("z_max", ascending=False)
    save(comp_out, "b_TRIM72_compound_level.csv")
    top = comp_out[comp_out["activity_stratum"] == comp_out["activity_stratum"].max()]
    save(top[["compound", "drugs", "raiser", "z_max", "z_min", "best_up", "max_n_sig_genes", "moa_fine", "targets",
              "curated_classes"]], "b_top_activity_stratum_compounds.csv")

    # secondary: drug-dose level (20 activity strata), curated + moa_fine, raiser / nominal lowerer counts
    rng = np.random.default_rng(SEED + 1)
    x = t.sort_index()
    stdd = quantile_strata(D.dd["activity"], 20)
    pr_up = strat_perm_matrix(x["sig_up"].astype(float).to_numpy(), stdd, B, rng)
    pr_dn = strat_perm_matrix(x["nominal_down"].astype(float).to_numpy(), stdd, B, rng)
    pr_z = strat_perm_matrix(x["z"].to_numpy(), stdd, B, rng)
    comp_of = D.dd["compound"].to_numpy()
    rows = []
    for sysname in ("curated", "moa_fine"):
        for k, cps in sorted(systems[sysname].items()):
            mem = np.isin(comp_of, list(cps))
            n = int(mem.sum())
            r = {"system": sysname, "class": k, "n_drug_doses": n}
            for lab, arr, pm in (("raisers", x["sig_up"].to_numpy(), pr_up),
                                 ("lowerers_nominal", x["nominal_down"].to_numpy(), pr_dn)):
                o = int(arr[mem].sum())
                nul = pm[:, mem].sum(axis=1)
                r[f"n_{lab}"] = o
                r[f"expected_{lab}"] = float(nul.mean())
                r[f"p_{lab}_stratified"] = (1 + int((nul >= o - 1e-9).sum())) / (B + 1)
            o = float(x["z"].to_numpy()[mem].mean())
            nul = pr_z[:, mem].mean(axis=1)
            r["mean_z"] = o
            r["p_mean_z_up"] = (1 + int((nul >= o - 1e-9).sum())) / (B + 1)
            r["p_mean_z_down"] = (1 + int((nul <= o + 1e-9).sum())) / (B + 1)
            rows.append(r)
    r2 = pd.DataFrame(rows)
    for pcol in ("p_raisers_stratified", "p_lowerers_nominal_stratified", "p_mean_z_up", "p_mean_z_down"):
        r2[pcol.replace("p_", "q_", 1)] = r2.groupby("system")[pcol].transform(
            lambda s: pd.Series(bh(s.to_numpy()), index=s.index))
    save(r2.sort_values(["system", "p_mean_z_up"]), "b_TRIM72_class_enrichment_drugdose_level.csv")
    return comp, res


# ============================================================================= part c
def part_c(D, t):
    log("Part c: specificity of TRIM72 within each raiser, co-induced genes, genome-wide partners ...")
    c = D.c
    rk, lm = D.ranked, D.level_matched
    sel = t[(t["sig_up"]) | (t["z"] >= 3)].index.to_numpy()          # t index = drug-dose row
    rows = []
    for i in sel:
        z = D.z[i, rk].astype(float)
        l = D.lfc[i, rk].astype(float)
        q = D.qup[i, rk].astype(float)
        zt, lt = float(D.z[i, c]), float(D.lfc[i, c])
        ok = np.isfinite(z)
        n = int(ok.sum())
        up2 = (q < Q_CUT) & (l >= 1.0)
        zl, ll = D.z[i, lm].astype(float), D.lfc[i, lm].astype(float)
        sd = mad(z)
        o = np.argsort(-np.nan_to_num(z, nan=-99))[:10]
        rows.append({
            "drug": D.dd.at[i, "drug"], "conc": D.dd.at[i, "conc"], "fold_change": 2 ** lt, "z": zt,
            "q_up": float(D.qup[i, c]), "sig_up": bool(t.at[i, "sig_up"]),
            "plate_baseline_group": t.at[i, "plate_baseline_group"],
            "rank_by_z_among_genes": int((z[ok] > zt).sum()) + 1, "rank_by_fold_among_genes": int((l[ok] > lt).sum()) + 1,
            "n_ranked_genes": n, "percentile_by_z": 100.0 * (z[ok] < zt).mean(),
            "percentile_by_fold": 100.0 * (l[ok] < lt).mean(),
            "rank_by_fold_among_level_matched": int((ll[np.isfinite(ll)] > lt).sum()) + 1,
            "rank_by_z_among_level_matched": int((zl[np.isfinite(zl)] > zt).sum()) + 1,
            "n_level_matched_genes": int(np.isfinite(ll).sum()),
            "n_genes_up_2x_q0.1": int(up2.sum()), "pct_genes_up_2x": 100.0 * up2.sum() / n,
            "n_genes_up_atlas": int(D.dd.at[i, "n_genes_up"]), "n_genes_down_atlas": int(D.dd.at[i, "n_genes_down"]),
            "n_sig_genes": int(D.dd.at[i, "n_sig_genes"]),
            "robust_sd_of_gene_z": sd, "TRIM72_z_over_gene_z_sd": zt / sd if sd > 0 else np.nan,
            "top10_genes_by_z": ", ".join(f"{D.sym[rk[k]]} {2 ** l[k]:.1f}x" for k in o),
            "flags": t.at[i, "flags"]})
    sp = pd.DataFrame(rows).sort_values("z", ascending=False)
    sp["reading"] = [("TRIM72 near the top of a narrow response" if r.percentile_by_z >= 99 and r["n_genes_up_2x_q0.1"] < 200
                      else "TRIM72 within a broad program (>= 500 genes >= 2x up)" if r["n_genes_up_2x_q0.1"] >= 500
                      else "TRIM72 in the top 1% of a moderate response" if r.percentile_by_z >= 99
                      else "TRIM72 not among the strongest responders")
                     for _, r in sp.iterrows()]
    save(sp, "c_TRIM72_specificity_in_raisers.csv")

    # ---- genes co-induced with TRIM72 in raisers beyond activity-matched non-raisers
    raisers = t[t["sig_up"]].copy()
    raisers["compound"] = D.dd.loc[raisers.index, "compound"]
    best = raisers.sort_values("z", ascending=False).drop_duplicates("compound").index.to_numpy()
    rcomp = set(D.dd.loc[best, "compound"])
    cand = t[(~t["sig_up"]) & (t["z"] < 2) & (~D.dd.loc[t.index, "compound"].isin(rcomp))].index.to_numpy()
    act = D.dd["activity"].to_numpy()
    ctrl = []
    for i in best:
        o = cand[np.argsort(np.abs(act[cand] - act[i]))[:5]]
        ctrl.extend(o.tolist())
    ctrl = np.array(sorted(set(ctrl)))
    log(f"  raiser drug-doses (best per compound): {len(best)}; activity-matched controls: {len(ctrl)}")
    rk = D.ranked
    up = (D.qup[:, rk] < Q_CUT) & (D.lfc[:, rk] >= LFC_MIN)
    a = up[best].sum(axis=0)
    b = up[ctrl].sum(axis=0)
    nb, nc = len(best), len(ctrl)
    p = np.array([stats.fisher_exact([[a[k], nb - a[k]], [b[k], nc - b[k]]], alternative="greater")[1]
                  if a[k] >= 3 else 1.0 for k in range(len(rk))])
    zr = np.nanmean(D.z[best][:, rk], axis=0)
    zc = np.nanmean(D.z[ctrl][:, rk], axis=0)
    co = pd.DataFrame({"gene": D.sym[rk], "n_raisers_up": a, "frac_raisers_up": a / nb, "n_controls_up": b,
                       "frac_controls_up": b / nc, "diff_frac": a / nb - b / nc, "mean_z_raisers": zr,
                       "mean_z_controls": zc, "fisher_p_one_sided": p})
    co["fisher_q"] = bh(co["fisher_p_one_sided"].to_numpy())
    co = co.sort_values(["fisher_p_one_sided", "diff_frac"], ascending=[True, False])
    save(co.head(300), "c_genes_coinduced_with_TRIM72_in_raisers.csv")
    pd.DataFrame({"role": ["raiser"] * nb + ["control"] * nc,
                  "drug": list(D.dd.loc[best, "drug"]) + list(D.dd.loc[ctrl, "drug"]),
                  "conc": list(D.dd.loc[best, "conc"]) + list(D.dd.loc[ctrl, "conc"]),
                  "TRIM72_z": list(D.z[best, D.c]) + list(D.z[ctrl, D.c]),
                  "n_sig_genes": list(D.dd.loc[best, "n_sig_genes"]) + list(D.dd.loc[ctrl, "n_sig_genes"])}) \
        .pipe(save, "c_raisers_and_matched_controls.csv")

    # ---- genome-wide partners across all drug-doses: raw Spearman and with activity + cell loss partialled out
    Z = np.nan_to_num(D.z[:, rk].astype(np.float64))
    y = np.nan_to_num(D.z[:, D.c].astype(np.float64))
    R = stats.rankdata(Z, axis=0)
    ry = stats.rankdata(y)
    n = len(y)

    def corr_cols(M, v):
        Mc = M - M.mean(axis=0)
        vc = v - v.mean()
        return (Mc.T @ vc) / (np.sqrt((Mc ** 2).sum(axis=0)) * np.sqrt((vc ** 2).sum()) + 1e-12)
    raw = corr_cols(R, ry)
    cov = np.column_stack([np.ones(n), stats.rankdata(D.dd["activity"]),
                           stats.rankdata(D.dd["cells_log2_vs_plate"].fillna(0))])
    P_ = cov @ np.linalg.pinv(cov)
    Rres = R - P_ @ R
    yres = ry - P_ @ ry
    part = corr_cols(Rres, yres)
    del R, Rres, Z
    df = n - 4
    tt = part * np.sqrt(df / np.maximum(1e-12, 1 - part ** 2))
    pp = 2 * stats.t.sf(np.abs(tt), df)
    gp = pd.DataFrame({"gene": D.sym[rk], "spearman_raw": raw, "spearman_partial_activity_cellloss": part,
                       "p_partial": pp})
    gp["median_line_cpm"] = D.genes["median_line_cpm"].to_numpy()[rk]
    gp = gp[gp["gene"] != GENE]
    gp["q_partial"] = bh(gp["p_partial"].to_numpy())
    gp = gp.sort_values("spearman_partial_activity_cellloss", ascending=False)
    gp["rank_partial"] = np.arange(1, len(gp) + 1)
    well = gp[gp["median_line_cpm"] >= 10]
    out = pd.concat([gp.head(100).assign(direction="positive", gene_set="all ranked genes"),
                     gp.tail(30).iloc[::-1].assign(direction="negative", gene_set="all ranked genes"),
                     well.head(50).assign(direction="positive", gene_set="genes >= 10 CPM (median line)"),
                     well.tail(20).iloc[::-1].assign(direction="negative", gene_set="genes >= 10 CPM (median line)")])
    save(out, "c_TRIM72_genomewide_partners_across_drugdoses.csv")
    lv_top = gp.head(100)["median_line_cpm"].median()
    log(f"  top-100 positive partners: median line {lv_top:.1f} CPM (all ranked genes {gp['median_line_cpm'].median():.1f})")
    # muscle / myogenic genes: the known upstream of TRIM72 in muscle (MyoD family, MEF2) and muscle partners
    rows = []
    ida5 = int(D.dd.index[(D.dd["drug"] == "Idarubicin (hydrochloride)") & (D.dd["conc"] == 5.0)][0])
    hht5 = int(D.dd.index[(D.dd["drug"] == "Homoharringtonine") & (D.dd["conc"] == 5.0)][0])
    gpi = gp.set_index("gene")
    for sname in MUSCLE:
        cc = D.col.get(sname)
        pf = os.path.join(GR, f"{sname}_drug_effects_by_dose.csv")
        if cc is None and os.path.exists(pf):        # a gene-panel gene below the atlas floor: the panel's own z
            pz = pd.read_csv(pf, usecols=["drug", "conc", "z_corrected", "fold_change"])
            pz["key"] = list(zip(pz["drug"], pz["conc"].astype(float).round(4)))
            zz = D.dd["key"].map(pz.set_index("key")["z_corrected"]).to_numpy(dtype=float)
            ff = D.dd["key"].map(pz.set_index("key")["fold_change"]).to_numpy(dtype=float)
            ok = np.isfinite(zz)
            rows.append({"gene": sname, "in_atlas": False,
                         "spearman_with_TRIM72_z": float(stats.spearmanr(D.z[ok, D.c], zz[ok]).statistic),
                         "idarubicin_5uM_fold": ff[ida5], "idarubicin_5uM_z": zz[ida5],
                         "homoharringtonine_5uM_fold": ff[hht5], "homoharringtonine_5uM_z": zz[hht5],
                         "note": "below the atlas's 2-CPM pooled floor; values from the gene panel's corrected table"})
            continue
        if cc is None:
            rows.append({"gene": sname, "in_atlas": False, "note": "below the atlas's 2-CPM pooled floor: not testable"})
            continue
        rows.append({"gene": sname, "in_atlas": True, "median_line_cpm": float(D.genes.at[cc, "median_line_cpm"]),
                     "n_lines_expressing": int(D.genes.at[cc, "n_lines_expressing"]),
                     "spearman_with_TRIM72_z": float(stats.spearmanr(D.z[:, D.c], np.nan_to_num(D.z[:, cc])).statistic),
                     "partial_spearman": float(gpi["spearman_partial_activity_cellloss"].get(sname, np.nan)),
                     "rank_partial_of_all_genes": float(gpi["rank_partial"].get(sname, np.nan)),
                     "idarubicin_5uM_fold": 2 ** float(D.lfc[ida5, cc]), "idarubicin_5uM_z": float(D.z[ida5, cc]),
                     "homoharringtonine_5uM_fold": 2 ** float(D.lfc[hht5, cc]),
                     "homoharringtonine_5uM_z": float(D.z[hht5, cc]), "note": ""})
    save(pd.DataFrame(rows), "c_muscle_and_myogenic_genes.csv")
    return sp, co, best, ctrl


MUSCLE = ["MYOD1", "MYOG", "MYF5", "MYF6", "MEF2A", "MEF2C", "MEF2D", "DES", "CKM", "ACTA1", "CAV3", "CHRNA1",
          "TRIM63", "MSTN", "MYH3", "PYGM", "DYSF", "TTN", "NEB", "TNNT1", "FBXO32", "PPARGC1A", "CDKN1C", "ID2",
          "PYCARD", "ITGAM"]          # PYCARD / ITGAM: TRIM72's neighbours on 16p11.2 (a local-chromatin control)


# ============================================================================= part d
IEG = ["FOS", "FOSB", "JUN", "JUNB", "EGR1", "EGR2", "EGR3", "IER2", "IER3", "IER5", "DUSP1", "KLF6", "ZFP36",
       "NR4A1"]                       # immediate-early genes (superinduced when translation stops)
SHORT_LIVED = ["MYC", "MCL1", "HEXIM1"]   # short-lived mRNAs that fall within hours of CDK9 / transcription block
SINGLE = ["ATF3", "DDIT3", "PMAIP1", "CDKN1A", "MDM2", "TP53", "MYC", "MCL1", "HEXIM1", "JUN", "FOS", "EGR1",
          "GADD45A", "BTG2", "SESN2", "PPM1D"]
PANEL_SCORES = ["P53_ACTIVITY", "ISR", "NRF2", "UPR", "HEAT_SHOCK", "IFN", "NFKB", "FERRO_MARKERS", "INFLAMMASOME",
                "PROTEASOME", "S_PHASE", "G2M_PHASE"]


def program_table(D, t):
    dd = D.dd
    pr = pd.DataFrame({"drug": dd["drug"], "conc": dd["conc"], "TRIM72_z": D.z[:, D.c], "TRIM72_log2FC": D.lfc[:, D.c],
                       "TRIM72_sig_up": t.sort_index()["sig_up"].to_numpy(),
                       "activity_log1p_n_sig_genes": dd["activity"], "n_sig_genes": dd["n_sig_genes"],
                       "cells_log2_vs_plate": dd["cells_log2_vs_plate"],
                       "composition_shift_log2": dd["composition_shift_log2"],
                       "compound": dd["compound"]})
    ps = pd.read_csv(os.path.join(GR, "pathway_scores_by_dose.csv"), usecols=["score", "drug", "conc", "z"])
    ps["key"] = list(zip(ps["drug"], ps["conc"].astype(float).round(4)))
    wide = ps.pivot_table(index="key", columns="score", values="z")
    for s in PANEL_SCORES:
        pr[f"{s}_z"] = dd["key"].map(wide[s]).to_numpy() if s in wide else np.nan
    cx = pd.read_csv(os.path.join(GR, "drug_context_by_dose.csv"),
                     usecols=["drug", "conc", "cells_log2_vs_plate_z", "genes_per_cell_log2_vs_plate_z",
                              "umi_per_cell_log2_vs_plate_z"])
    cx["key"] = list(zip(cx["drug"], cx["conc"].astype(float).round(4)))
    cx = cx.set_index("key")
    for k in ("cells_log2_vs_plate_z", "genes_per_cell_log2_vs_plate_z", "umi_per_cell_log2_vs_plate_z"):
        pr[k] = dd["key"].map(cx[k]).to_numpy()
    for g in SINGLE:
        v = D.gene_z(g)
        if v is not None:
            pr[f"{g}_z"] = v
    for lab, mem in (("IEG_SCORE", IEG), ("SHORT_LIVED_mRNA_SCORE", SHORT_LIVED)):
        cols = [D.col[g] for g in mem if g in D.col]
        pr[f"{lab}_z"] = np.nanmean(D.z[:, cols], axis=1)
        log(f"  {lab}: {len(cols)} of {len(mem)} members found")
    # a generic level-dependent shift: genes at TRIM72's level vs genes >= 32 CPM (does every low gene rise?)
    lvl = D.genes["median_line_cpm"].to_numpy()
    gene = (D.genes["kind"] == "gene").to_numpy()
    low = np.setdiff1d(D.level_matched, [D.c])
    high = np.flatnonzero(gene & (lvl >= 32))
    pr["LOW_LEVEL_GENE_UPLIFT_log2"] = np.nanmean(D.lfc[:, low], axis=1) - np.nanmean(D.lfc[:, high], axis=1)
    return pr


def part_d(D, t, best, ctrl, B):
    log("Part d: TRIM72 vs stress / p53 / cell-cycle programs across drug-doses ...")
    pr = program_table(D, t)
    save(pr, "d_program_scores_by_drugdose.csv")
    progs = [c for c in pr.columns if (c.endswith("_z") and c != "TRIM72_z") or c == "LOW_LEVEL_GENE_UPLIFT_log2"]
    act, cells = pr["activity_log1p_n_sig_genes"].to_numpy(), pr["cells_log2_vs_plate"].to_numpy()
    active = pr["n_sig_genes"].to_numpy() >= 500
    rows = []
    bi = np.asarray(best)
    ci = np.asarray(ctrl)
    for p in progs:
        x = pr[p].to_numpy(dtype=float)
        y = pr["TRIM72_z"].to_numpy(dtype=float)
        ok = np.isfinite(x) & np.isfinite(y)
        rs = stats.spearmanr(x[ok], y[ok])
        r1, p1, n1 = partial_spearman(x, y, [act])
        r2, p2, n2 = partial_spearman(x, y, [act, cells])
        oka = ok & active
        rsa = stats.spearmanr(x[oka], y[oka])
        r3, p3, n3 = partial_spearman(x[active], y[active], [act[active]])
        xb, xc = x[bi], x[ci]
        xb, xc = xb[np.isfinite(xb)], xc[np.isfinite(xc)]
        if len(xb) >= 3 and len(xc) >= 3:
            mw = stats.mannwhitneyu(xb, xc, alternative="two-sided")
            auc, pmw = mw.statistic / (len(xb) * len(xc)), mw.pvalue
        else:
            auc, pmw = np.nan, np.nan
        rows.append({"program": p[:-2] if p.endswith("_z") else p, "n": int(ok.sum()), "spearman_all": rs.statistic,
                     "p_all": rs.pvalue, "partial_spearman_activity": r1, "p_partial_activity": p1,
                     "partial_spearman_activity_cellloss": r2, "p_partial_activity_cellloss": p2,
                     "n_active_drugdoses": int(oka.sum()), "spearman_active_only": rsa.statistic,
                     "p_active_only": rsa.pvalue, "partial_spearman_active_only_activity": r3, "p_partial_active_only": p3,
                     "median_in_raisers": float(np.median(xb)) if len(xb) else np.nan,
                     "median_in_matched_controls": float(np.median(xc)) if len(xc) else np.nan,
                     "auc_raisers_vs_matched_controls": auc, "p_mannwhitney_raisers_vs_controls": pmw,
                     "n_raisers": len(xb), "n_controls": len(xc)})
    res = pd.DataFrame(rows)
    for pc in ("p_all", "p_partial_activity", "p_partial_activity_cellloss", "p_active_only", "p_partial_active_only",
               "p_mannwhitney_raisers_vs_controls"):
        res[pc.replace("p_", "q_", 1)] = bh(res[pc].to_numpy())
    res = res.sort_values("partial_spearman_activity_cellloss", ascending=False)
    save(res, "d_TRIM72_vs_programs_correlations.csv")

    # ---- sufficiency / necessity among active drug-doses: program high (z >= 4) x TRIM72 raiser
    rows = []
    actv = pr[pr["n_sig_genes"] >= 500]
    rai = actv["TRIM72_sig_up"].to_numpy(bool)
    for p in [c for c in progs if c.endswith("_z") and not c.startswith(("cells_", "genes_", "umi_"))]:
        for sign, lab in ((1, "up"), (-1, "down")):
            x = actv[p].to_numpy(dtype=float) * sign
            hi = x >= 4
            a_, b_ = int((hi & rai).sum()), int((hi & ~rai).sum())
            c_, d_ = int((~hi & rai).sum()), int((~hi & ~rai).sum())
            orr, pf = stats.fisher_exact([[a_, b_], [c_, d_]])
            rows.append({"program": p[:-2], "direction": lab, "n_active_drugdoses": len(actv),
                         "n_program_high": a_ + b_, "n_program_high_and_TRIM72_raiser": a_,
                         "frac_program_high_raising_TRIM72": a_ / (a_ + b_) if a_ + b_ else np.nan,
                         "n_TRIM72_raisers": int(rai.sum()), "frac_raisers_with_program_high": a_ / max(1, rai.sum()),
                         "frac_nonraisers_with_program_high": b_ / max(1, (~rai).sum()), "odds_ratio": orr,
                         "fisher_p": pf,
                         "raisers_with_program_high": "; ".join(f"{r.drug} {r.conc:g}" for r in
                                                               actv[hi & rai].itertuples())})
    sn = pd.DataFrame(rows)
    sn["fisher_q"] = bh(sn["fisher_p"].to_numpy())
    save(sn.sort_values("fisher_p"), "d_program_high_vs_TRIM72_raisers_active_drugdoses.csv")
    # ---- the strongest drug-doses of each program: do they raise TRIM72?
    rows = []
    for p in ("P53_ACTIVITY_z", "HEAT_SHOCK_z", "ATF3_z", "ISR_z", "NFKB_z", "IEG_SCORE_z", "UPR_z", "NRF2_z",
              "S_PHASE_z", "HEXIM1_z"):
        top = pr.sort_values(p, ascending=False).head(20)
        for rnk, (i, r) in enumerate(top.iterrows(), 1):
            rows.append({"program": p[:-2], "rank": rnk, "drug": r["drug"], "conc": r["conc"], "program_z": r[p],
                         "TRIM72_z": r["TRIM72_z"], "TRIM72_fold": 2 ** r["TRIM72_log2FC"],
                         "TRIM72_sig_up": r["TRIM72_sig_up"], "TRIM72_rank_z_up": int(t.at[i, "rank_z_up"]),
                         "n_sig_genes": r["n_sig_genes"]})
    tp = pd.DataFrame(rows)
    save(tp, "d_top20_drugdoses_per_program_with_TRIM72.csv")
    log("  of the 20 strongest drug-doses per program, TRIM72 raisers: " + ", ".join(
        f"{k} {int(v)}" for k, v in tp.groupby("program")["TRIM72_sig_up"].sum().items()))

    # ---- multivariable rank model with a compound-cluster bootstrap
    feats = ["P53_ACTIVITY_z", "ISR_z", "NRF2_z", "UPR_z", "HEAT_SHOCK_z", "NFKB_z", "IFN_z", "S_PHASE_z",
             "G2M_PHASE_z", "ATF3_z", "IEG_SCORE_z", "SHORT_LIVED_mRNA_SCORE_z", "TP53_z",
             "activity_log1p_n_sig_genes", "cells_log2_vs_plate", "genes_per_cell_log2_vs_plate_z"]
    m = pr[["TRIM72_z", "compound"] + feats].dropna()
    Xr = np.column_stack([stats.zscore(stats.rankdata(m[f])) for f in feats])
    yr = stats.zscore(stats.rankdata(m["TRIM72_z"]))
    X1 = np.column_stack([np.ones(len(yr)), Xr])
    beta = np.linalg.lstsq(X1, yr, rcond=None)[0][1:]
    r2 = 1 - ((yr - X1 @ np.linalg.lstsq(X1, yr, rcond=None)[0]) ** 2).sum() / (yr ** 2).sum()
    rng = np.random.default_rng(SEED + 2)
    comps = m["compound"].to_numpy()
    uc = np.unique(comps)
    idx_of = {u: np.flatnonzero(comps == u) for u in uc}
    nb = max(200, B // 10)
    bs = np.empty((nb, len(feats)))
    for b in range(nb):
        pick = rng.choice(uc, size=len(uc), replace=True)
        ii = np.concatenate([idx_of[u] for u in pick])
        bs[b] = np.linalg.lstsq(X1[ii], yr[ii], rcond=None)[0][1:]
    mv = pd.DataFrame({"feature": feats, "std_beta_on_ranks": beta, "ci95_low": np.percentile(bs, 2.5, axis=0),
                       "ci95_high": np.percentile(bs, 97.5, axis=0), "frac_boot_gt0": (bs > 0).mean(axis=0)})
    mv["boot_p_two_sided"] = 2 * np.minimum(mv["frac_boot_gt0"], 1 - mv["frac_boot_gt0"]).clip(lower=1 / nb)
    mv["boot_q"] = bh(mv["boot_p_two_sided"].to_numpy())
    mv["n_drugdoses"] = len(m)
    mv["n_compounds"] = len(uc)
    mv["model_R2"] = r2
    mv["n_bootstrap"] = nb
    save(mv.sort_values("std_beta_on_ranks", ascending=False), "d_TRIM72_multivariable_rank_model.csv")

    # ---- per-raiser profile
    keep = ["drug", "conc", "TRIM72_z", "TRIM72_log2FC", "n_sig_genes", "cells_log2_vs_plate",
            "P53_ACTIVITY_z", "CDKN1A_z", "MDM2_z", "TP53_z", "ATF3_z", "DDIT3_z", "PMAIP1_z", "ISR_z", "NRF2_z", "UPR_z",
            "HEAT_SHOCK_z", "NFKB_z", "IFN_z", "S_PHASE_z", "G2M_PHASE_z", "IEG_SCORE_z", "SHORT_LIVED_mRNA_SCORE_z",
            "genes_per_cell_log2_vs_plate_z"]
    rp = pr.loc[t[t["sig_up"] | (t["z"] >= 3)].index, keep].copy()
    rp["flags"] = t.loc[rp.index, "flags"]
    rp["moa_fine"] = D.dd.loc[rp.index, "moa_fine"]

    def reading(r):
        s = []
        if r["P53_ACTIVITY_z"] >= 3:
            s.append("p53 targets up")
        if r["ISR_z"] >= 3 or r["ATF3_z"] >= 3:
            s.append("ISR/ATF3 up")
        if r["SHORT_LIVED_mRNA_SCORE_z"] <= -3:
            s.append("short-lived mRNAs down (transcription block)")
        if r["IEG_SCORE_z"] >= 3:
            s.append("immediate-early genes up")
        if r["NFKB_z"] >= 3:
            s.append("NF-kB up")
        if r["NRF2_z"] >= 3:
            s.append("NRF2 up")
        if r["HEAT_SHOCK_z"] >= 3:
            s.append("heat shock up")
        if abs(r["S_PHASE_z"]) >= 4 or abs(r["G2M_PHASE_z"]) >= 4:
            s.append("cell-cycle shift")
        return "; ".join(s) or "none of the programs at |z| >= 3"
    rp["programs_at_z3"] = rp.apply(reading, axis=1)
    save(rp.sort_values("TRIM72_z", ascending=False), "d_TRIM72_raiser_program_profile.csv")
    return pr, res, mv


# ============================================================================= part d2: per line, TP53 status
def panel_setup(tmp):
    """The gene panel's in-memory setup (as trim72_idarubicin/corrected/trim72_ida_per_line.py), without P.main:
    side tables go to a temporary folder, and the file index is read from its cache without ever rewriting it."""
    import tahoe_gene_panel as P
    cache = os.path.join(GP, "file_index.json")

    def discover_readonly(data_dir, out_dir, refresh=False):
        with open(cache, encoding="utf-8") as fh:
            return json.load(fh)
    T.discover = discover_readonly
    args = argparse.Namespace(command="analyze", data=DATA, out=GP, workers=0, batch_size=20000, limit_files=0,
                              layout=None, min_cells=T.MIN_CELLS, reindex=False, genes="", mtap_null=None,
                              tp53_wt=None, tp53_altered=None, prior="none", unreliable_plates=None, atlas=None,
                              angles="", model="sonnet", budget=5.0, max_turns=80, parallel=1,
                              permission_mode="dontAsk", web=False, sandbox=False, redo=False, skip_overview=False,
                              dry_run=False, extra_genes="", pcs=None)
    S = P.Run(args)
    S.R = tmp
    P.load(S)
    if os.path.abspath(S.R) != os.path.abspath(tmp):
        sys.exit("panel results folder changed unexpectedly")
    P.step_baseline(S)
    P.step_expression(S)
    P.step_prepare(S)
    S.ctx = T.well_context(S.wl, S.sm, S.cols, S.M)
    return P, S


def part_d2(D, t):
    log("Part d2: per-line TRIM72 effects by TP53 status (gene panel machinery, in memory) ...")
    tmp = tempfile.mkdtemp(prefix="panel_tmp_", dir=OUTDIR)
    try:
        P, S = panel_setup(tmp)
        base = pd.read_csv(os.path.join(GR, "baseline_by_cell_line.csv"), usecols=["cell_line_id", "tp53_group"])
        grp = base.set_index("cell_line_id")["tp53_group"]
        fun = pd.read_csv(os.path.join(GR, "p53_functional_status.csv"),
                          usecols=["cell_line_id", "cell_name", "functional_call"]).set_index("cell_line_id")
        per = {}
        for g in (GENE, "CDKN1A", "MDM2"):
            excl = P.gene_exclusions(S, g)
            res, W, d, cal = T.expression_effects(S.wl, S.sm, g, excl, S.ctx, S.drugs, method=S.M)
            Wd = W.loc[~W["is_dmso"]].copy()
            Wd["dose"] = T.dose_key(Wd)
            used = set(Wd.index[T.used_wells(Wd)])
            x = d[d["sample"].isin(used)].copy()
            x["drug"] = x["sample"].map(W["drug"])
            x["conc"] = x["sample"].map(W["conc"]).astype(float).round(4)
            pl = x.groupby(["drug", "conc", "cell_line_id"])["r2"].mean()
            per[g] = pl
            log(f"  {g}: {len(excl)} lines excluded (not expressed); {pl.index.droplevel(2).nunique()} drug-doses")
        del S
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    def contrast(pl, keys):
        rows = {}
        for k in keys:
            try:
                v = pl.loc[k]
            except KeyError:
                continue
            g = v.index.map(grp)
            wt, al = v[g == "WT"].dropna(), v[g == "altered"].dropna()
            if len(wt) >= 3 and len(al) >= 3:
                mw = stats.mannwhitneyu(wt, al, alternative="two-sided")
                rows[k] = {"n_wt": len(wt), "n_altered": len(al), "median_log2_wt": wt.median(),
                           "median_log2_altered": al.median(), "diff_wt_minus_altered": wt.median() - al.median(),
                           "auc_wt_gt_altered": mw.statistic / (len(wt) * len(al)), "p_mannwhitney": mw.pvalue,
                           "frac_altered_lines_up_1.2x": float((al >= LFC_MIN).mean()),
                           "frac_wt_lines_up_1.2x": float((wt >= LFC_MIN).mean())}
        out_ = pd.DataFrame(list(rows.values()))
        out_.index = pd.MultiIndex.from_tuples(list(rows.keys()), names=["drug", "conc"])
        return out_

    keys_all = sorted(set(per[GENE].index.droplevel(2)))
    sel = t[t["sig_up"] | (t["z"] >= 3)]
    sel_keys = [(r.drug, round(float(r.conc), 4)) for r in sel.itertuples()]
    out = []
    for g in (GENE, "CDKN1A", "MDM2"):
        cdf = contrast(per[g], sel_keys)
        cdf.columns = [f"{g}_{c}" for c in cdf.columns]
        out.append(cdf)
    rt = pd.concat(out, axis=1).reset_index()
    rt["TRIM72_z_all_lines"] = [float(t.loc[(t["drug"] == a) & (t["conc"].round(4) == b), "z"].iloc[0])
                                for a, b in zip(rt["drug"], rt["conc"])]
    # general responsiveness: the atlas's per-line response strength to each drug-dose's consensus (DD_beta, 1 =
    # typical line); a WT-altered gap in beta would make any gene look WT-leaning
    beta = np.asarray(D.fx.DD_beta, dtype=float)
    lid = D.fx.lines["cell_line_id"].astype(str).to_numpy()
    lg = np.array([grp.get(x, "") for x in lid])
    row_of = {k: i for i, k in enumerate(D.dd["key"])}
    bw, bp = [], []
    for a_, b_ in zip(rt["drug"], rt["conc"]):
        i = row_of.get((a_, round(float(b_), 4)))
        v = beta[i] if i is not None else np.full(len(lid), np.nan)
        w_, al_ = v[(lg == "WT") & np.isfinite(v)], v[(lg == "altered") & np.isfinite(v)]
        ok = len(w_) >= 3 and len(al_) >= 3
        bw.append(np.median(w_) - np.median(al_) if ok else np.nan)
        bp.append(stats.mannwhitneyu(w_, al_).pvalue if ok else np.nan)
    rt["consensus_beta_wt_minus_altered"] = bw
    rt["consensus_beta_p_mannwhitney"] = bp
    rt[f"{GENE}_q_mannwhitney"] = bh(rt[f"{GENE}_p_mannwhitney"].to_numpy())
    rt["CDKN1A_q_mannwhitney"] = bh(rt["CDKN1A_p_mannwhitney"].to_numpy())
    save(rt.sort_values("TRIM72_z_all_lines", ascending=False), "d2_TRIM72_raisers_TP53_WT_vs_altered.csv")

    # across all drug-doses: TRIM72's WT-minus-altered contrast vs CDKN1A's, and among p53-activating drug-doses
    ct = contrast(per[GENE], keys_all)[["diff_wt_minus_altered", "p_mannwhitney"]].rename(
        columns={"diff_wt_minus_altered": "TRIM72_diff", "p_mannwhitney": "TRIM72_p"})
    cc = contrast(per["CDKN1A"], keys_all)[["diff_wt_minus_altered"]].rename(
        columns={"diff_wt_minus_altered": "CDKN1A_diff"})
    pw = pd.read_csv(os.path.join(GR, "p53_wt_vs_altered.csv"),
                     usecols=["drug", "conc", "extra_log2_p53_induction_in_WT", "z_wt_more", "all_lines_P53_ACTIVITY_z"])
    pwd = {(a, round(float(b), 4)): r for a, b, r in zip(pw["drug"], pw["conc"], pw.itertuples())}
    j = ct.join(cc, how="inner")
    keys = list(j.index)
    j["p53_targets_extra_in_WT"] = [pwd[k].extra_log2_p53_induction_in_WT if k in pwd else np.nan for k in keys]
    j["p53_wt_more_z"] = [pwd[k].z_wt_more if k in pwd else np.nan for k in keys]
    j["P53_ACTIVITY_z"] = [pwd[k].all_lines_P53_ACTIVITY_z if k in pwd else np.nan for k in keys]
    j["TRIM72_z"] = [float(D.z[row_of[k], D.c]) if k in row_of else np.nan for k in keys]
    bdiff = []
    for k in keys:
        i = row_of.get(k)
        v = beta[i] if i is not None else np.full(len(lid), np.nan)
        w_, al_ = v[(lg == "WT") & np.isfinite(v)], v[(lg == "altered") & np.isfinite(v)]
        bdiff.append(np.median(w_) - np.median(al_) if len(w_) >= 3 and len(al_) >= 3 else np.nan)
    j["consensus_beta_wt_minus_altered"] = bdiff
    rows = []
    for lab, m in (("all drug-doses", np.ones(len(j), bool)),
                   ("P53_ACTIVITY z >= 3 (p53-activating)", (j["P53_ACTIVITY_z"] >= 3).to_numpy()),
                   ("p53 WT-selective induction z >= 3", (j["p53_wt_more_z"] >= 3).to_numpy()),
                   ("TRIM72 raisers (z >= 3)", (j["TRIM72_z"] >= 3).to_numpy())):
        s = j[m].dropna(subset=["TRIM72_diff", "CDKN1A_diff"])
        if len(s) >= 5:
            r1 = stats.spearmanr(s["TRIM72_diff"], s["CDKN1A_diff"])
            r2 = stats.spearmanr(s["TRIM72_diff"], s["p53_targets_extra_in_WT"], nan_policy="omit")
            wsr = stats.wilcoxon(s["TRIM72_diff"]) if len(s) >= 6 else None
            sb = s.dropna(subset=["consensus_beta_wt_minus_altered"])
            r3 = stats.spearmanr(sb["TRIM72_diff"], sb["consensus_beta_wt_minus_altered"]) if len(sb) >= 5 else None
            rows.append({"subset": lab, "n_drugdoses": len(s), "median_TRIM72_wt_minus_altered": s["TRIM72_diff"].median(),
                         "median_CDKN1A_wt_minus_altered": s["CDKN1A_diff"].median(),
                         "wilcoxon_p_TRIM72_diff_ne_0": wsr.pvalue if wsr is not None else np.nan,
                         "spearman_TRIM72_diff_vs_CDKN1A_diff": r1.statistic, "p1": r1.pvalue,
                         "spearman_TRIM72_diff_vs_p53_targets_extra_in_WT": r2.statistic, "p2": r2.pvalue,
                         "n_with_beta": len(sb),
                         "median_consensus_beta_wt_minus_altered": sb["consensus_beta_wt_minus_altered"].median()
                         if len(sb) else np.nan,
                         "spearman_TRIM72_diff_vs_beta_diff": r3.statistic if r3 is not None else np.nan,
                         "p3": r3.pvalue if r3 is not None else np.nan})
    save(pd.DataFrame(rows), "d2_TRIM72_TP53_contrast_across_drugdoses.csv")
    jj = j.reset_index()
    save(jj[["drug", "conc", "TRIM72_z", "TRIM72_diff", "TRIM72_p", "CDKN1A_diff", "consensus_beta_wt_minus_altered",
                                   "p53_targets_extra_in_WT", "p53_wt_more_z", "P53_ACTIVITY_z"]]
         .sort_values("TRIM72_z", ascending=False), "d2_TRIM72_TP53_contrast_by_drugdose.csv")
    # per line for the strongest raisers (for plots / checks)
    lines = []
    for k in sel_keys:
        for g in (GENE, "CDKN1A"):
            try:
                v = per[g].loc[k]
            except KeyError:
                continue
            for cl, val in v.items():
                lines.append({"drug": k[0], "conc": k[1], "gene": g, "cell_line_id": cl,
                              "cell_line": fun["cell_name"].get(cl, cl), "tp53_group": grp.get(cl, ""),
                              "p53_functional_call": fun["functional_call"].get(cl, ""), "log2FC_corrected": val})
    save(pd.DataFrame(lines), "d2_per_line_effects_raisers.csv")
    return rt


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perms", type=int, default=20000, help="permutations for the class tests (default 20000)")
    ap.add_argument("--skip-per-line", action="store_true", help="skip part d2 (gene panel setup, ~1-2 min, ~3 GB)")
    a = ap.parse_args()
    os.makedirs(TAB, exist_ok=True)
    t0 = time.time()
    D = Data()
    t = part_a(D)
    t = t.sort_index()
    part_b(D, t, a.perms)
    sp, co, best, ctrl = part_c(D, t)
    part_d(D, t, best, ctrl, a.perms)
    if not a.skip_per_line:
        part_d2(D, t)
    log(f"done in {time.time() - t0:.0f} s; tables in {TAB}")


if __name__ == "__main__":
    main()
