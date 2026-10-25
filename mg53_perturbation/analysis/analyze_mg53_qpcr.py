#!/usr/bin/env python3
"""
analyze_mg53_qpcr.py -- analysis pipeline for the MG53 (TRIM72) perturbation qPCR experiment.

WHAT THIS IS FOR
----------------
The wet-lab experiment perturbs MG53 (TRIM72) -- control / overexpression / knockdown --
in TP53-WT and TP53-null cell lines, under vehicle / a p53 activator / idarubicin (and any
other treatments), and reads mRNA out by qPCR Ct values. This script turns a tidy table of
Ct values into:

  - QC tables (technical-replicate spread, Ct censoring, reference-gene stability,
    perturbation efficacy check),
  - per-sample dCt (relative to the geometric mean of the reference genes),
  - per-condition fold table (2^-ddCt vs the matched control), genes grouped by module,
  - the D1 PRIMARY result: does MG53-OE lower the p53 score in TP53-WT but NOT in TP53-null
    (the MG53 x TP53 interaction), strongest under p53 activation,
  - the D2 SCREEN result: MG53 effects on the other reported pathways, with effects that
    persist in TP53-null flagged as p53-INDEPENDENT,
  - a markdown REPORT.md.

HYPOTHESES SERVED (see mg53_perturbation/assay_panel/panel.csv for the assay design)
  D1 (primary)  raising MG53 lowers p53-target mRNA in TP53-WT, most under p53 activation,
                not in TP53-null (MG53 x TP53 interaction); knockdown the opposite.
  D2 (screen)   MG53 effects on NF-kB, PI3K-AKT/FOXO, cell cycle, ferroptosis, apoptosis
                etc.; an effect also seen in TP53-null is p53-independent.
  (U1-U3 are addressed upstream by the TRIM72 junction/intron/intergenic assays, which this
   script treats as the MG53-perturbation readout + stress markers; the heavy upstream
   discrimination -- readthrough vs own promoter -- is a design question for those assays.)

QUANTITATION MODEL
  Expression is assumed to double per cycle (efficiency = 2): relative quantity = 2^-Ct, so
    dCt   = Ct(target) - mean(Ct(reference genes))            [arithmetic mean of ref Ct
            == geometric mean of reference quantities]
    ddCt  = dCt(sample) - dCt(matched control)
    fold  = 2^-ddCt    and    log2 fold change = -ddCt
  Higher Ct = less RNA, so a POSITIVE dCt effect means expression went DOWN. All reported
  effects are converted to log2 fold change (-ddCt), so POSITIVE = up, NEGATIVE = down.
  An optional per-assay 'efficiency' column (amplification efficiency E in [1,2], where the
  usual E=2) switches dCt to efficiency-corrected units: dCt uses log2(E)*Ct per assay.

STATISTICS
  Within each time point, per gene and per module score, a linear model is fit on dCt:
      dCt ~ mg53 * tp53 * treatment  (+ cell_line as an additive block to soak up
                                       line-to-line baseline differences)
  From the fit we read, by exact linear contrasts:
      - MG53 effect in TP53-WT   (OE vs control, KD vs control),
      - MG53 effect in TP53-null,
      - the MG53 x TP53 interaction (null minus WT)  <- the primary D1 test,
  at each treatment, with 95% CIs and BH-FDR across genes within each module family.
  Engine: statsmodels MixedLM (bio_rep as a random effect) when statsmodels is installed;
  otherwise a numpy OLS fallback (biological samples as rows; tech reps averaged first) with
  t-based CIs. The engine actually used is reported in every table and in REPORT.md.

USAGE
  python3 analyze_mg53_qpcr.py --input ct_values.csv [--config config.json]
                               [--panel ../assay_panel/panel.csv] [--outdir results]
                               [--engine auto|ols|mixedlm]
  Input CSV columns (one row per Ct measurement):
      sample, cell_line, tp53, mg53, treatment, time_h, bio_rep, tech_rep, gene, ct
      optional: mg53_check, efficiency
  tp53 in {WT, null}; mg53 in {control, overexpression, knockdown}; ct may be a number or
  'Undetermined'/'NA'/'' (treated as not detected, never imputed).

Only numpy / pandas / scipy are required (statsmodels is used if present).
"""
import argparse
import json
import math
import os
import sys
import numpy as np
import pandas as pd
from scipy import stats

try:
    import statsmodels.api as sm  # noqa: F401
    HAVE_SM = True
except Exception:
    HAVE_SM = False

# --------------------------------------------------------------------------- defaults
CT_CENSOR = 35.0            # Ct > this (or undetermined) => not reliably detected, censored
TECHREP_SD_FLAG = 0.3       # flag technical-replicate SD above this many cycles
REF_MOVE_FLAG = 0.5         # flag a reference whose dCt SD across conditions exceeds this
GENORM_M_FLAG = 1.0         # flag a reference whose geNorm M exceeds this (heterogeneous: 1.5)

REF_MG53 = "control"
REF_TP53 = "WT"
REF_TREAT = "vehicle"

# Built-in default panel (used only when panel.csv is absent). Gene names are normalised
# (text before " (" dropped). Mirrors mg53_perturbation/assay_panel/panel.csv.
BUILTIN_MODULES = {
    "MG53_total":          ["TRIM72_total"],
    "MG53_endogenous":     ["TRIM72_endogenous", "TRIM72_intron"],
    "p53_primary":         ["MDM2", "CDKN1A", "FDXR", "ZMAT3", "DDB2", "TP53I3"],
    "p53_secondary":       ["BBC3", "RRM2B", "SESN1", "GDF15"],
    "locus_readthrough":   ["FUS", "FUS-TRIM72 intergenic", "PYCARD-AS1", "PYCARD", "ITGAM"],
    "stress_markers":      ["ATF3", "FOS", "PMAIP1", "HEXIM1", "DDIT3"],
    "screen_NFkB":         ["NFKBIA", "TNFAIP3", "CXCL8"],
    "screen_PI3K_AKT_FAK": ["TXNIP", "IRS1", "PTK2"],
    "screen_cell_cycle":   ["CCND1", "KIF11"],
    "screen_RAC1":         ["RAC1"],
    "screen_ferroptosis":  ["SLC7A11", "GPX4", "CHAC1"],
    "screen_apoptosis":    ["BAX", "MCL1"],
}
BUILTIN_REFERENCES = ["GAPDH", "ACTB", "PPIA"]
# p53 score: positive p53 transcriptional targets that rise on p53 activation (SLC7A11 is
# p53-REPRESSED so it is NOT part of the up-score; it is read on its own in the screen).
P53_SCORE_MEMBERS = ["MDM2", "CDKN1A", "FDXR", "ZMAT3", "DDB2", "TP53I3",
                     "BBC3", "RRM2B", "SESN1", "GDF15"]
P53_MODULE_FAMILIES = ["p53_primary", "p53_secondary"]
SCREEN_MODULE_FAMILIES = ["screen_NFkB", "screen_PI3K_AKT_FAK", "screen_cell_cycle",
                          "screen_RAC1", "screen_ferroptosis", "screen_apoptosis"]
BIO_KEYS = ["cell_line", "tp53", "mg53", "treatment", "time_h", "bio_rep"]


# --------------------------------------------------------------------------- helpers
def normalize_gene(g):
    """'CDKN1A (p21)' -> 'CDKN1A'; 'TRIM72_total (exon2-exon3 junction)' -> 'TRIM72_total'."""
    return str(g).split(" (")[0].strip()


def parse_ct(val):
    """Parse a Ct cell. Returns float, or np.nan for undetermined/blank/non-numeric."""
    if val is None:
        return np.nan
    s = str(val).strip()
    if s == "" or s.lower() in ("undetermined", "undet", "na", "n/a", "nan", "none"):
        return np.nan
    try:
        return float(s)
    except ValueError:
        return np.nan


def bh_fdr(pvals):
    """Benjamini-Hochberg FDR. Accepts NaNs (passed through as NaN)."""
    p = np.asarray(pvals, dtype=float)
    out = np.full(p.shape, np.nan)
    ok = np.isfinite(p)
    if ok.sum() == 0:
        return out
    idx = np.where(ok)[0]
    pv = p[idx]
    order = np.argsort(pv)
    ranked = pv[order]
    n = len(pv)
    adj = ranked * n / (np.arange(n) + 1)
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    adj = np.clip(adj, 0, 1)
    res = np.empty(n)
    res[order] = adj
    out[idx] = res
    return out


# --------------------------------------------------------------------------- config
def load_config(args):
    """Build the analysis config: reference genes, gene modules, score members, control
    levels, and which treatments count as p53 activators for the D1 headline."""
    cfg = {
        "references": None,
        "modules": None,
        "p53_score_members": list(P53_SCORE_MEMBERS),
        "p53_module_families": list(P53_MODULE_FAMILIES),
        "screen_module_families": list(SCREEN_MODULE_FAMILIES),
        "ref_mg53": REF_MG53, "ref_tp53": REF_TP53, "ref_treat": REF_TREAT,
        "d1_activator_treatments": None,   # resolved from data if None
        "ct_censor": CT_CENSOR,
        "techrep_sd_flag": TECHREP_SD_FLAG,
        "ref_move_flag": REF_MOVE_FLAG,
        "genorm_m_flag": GENORM_M_FLAG,
    }
    # user config file overrides
    if args.config and os.path.isfile(args.config):
        with open(args.config) as fh:
            user = json.load(fh)
        cfg.update(user)

    # modules / references default from panel.csv, else built-in
    if cfg["modules"] is None or cfg["references"] is None:
        panel_mods, panel_refs = modules_from_panel(args.panel)
        if cfg["modules"] is None:
            cfg["modules"] = panel_mods if panel_mods else {m: list(v) for m, v in BUILTIN_MODULES.items()}
        if cfg["references"] is None:
            cfg["references"] = panel_refs if panel_refs else list(BUILTIN_REFERENCES)

    # normalise names
    cfg["references"] = [normalize_gene(g) for g in cfg["references"]]
    cfg["modules"] = {m: [normalize_gene(g) for g in gs] for m, gs in cfg["modules"].items()}
    cfg["p53_score_members"] = [normalize_gene(g) for g in cfg["p53_score_members"]]
    return cfg


def modules_from_panel(panel_path):
    """Read module membership + reference genes from assay_panel/panel.csv if present."""
    candidates = [panel_path,
                  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                               "assay_panel", "panel.csv")]
    for p in candidates:
        if p and os.path.isfile(p):
            df = pd.read_csv(p)
            gcol = "gene/assay" if "gene/assay" in df.columns else df.columns[0]
            df["g"] = df[gcol].map(normalize_gene)
            mods, refs = {}, []
            for mod, sub in df.groupby("module"):
                genes = list(dict.fromkeys(sub["g"].tolist()))
                if mod == "reference":
                    refs = genes
                else:
                    mods[mod] = genes
            return mods, refs
    return None, None


# --------------------------------------------------------------------------- load + QC
def load_input(path):
    df = pd.read_csv(path)
    required = ["sample", "cell_line", "tp53", "mg53", "treatment",
                "time_h", "bio_rep", "tech_rep", "gene", "ct"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        sys.exit(f"Input CSV is missing required columns: {missing}")
    df["gene"] = df["gene"].map(normalize_gene)
    df["ct_raw"] = df["ct"]
    df["ct_num"] = df["ct"].map(parse_ct)
    df["time_h"] = pd.to_numeric(df["time_h"], errors="coerce")
    for c in ("tp53", "mg53", "treatment", "cell_line"):
        df[c] = df[c].astype(str)
    if "efficiency" not in df.columns:
        df["efficiency"] = 2.0
    df["efficiency"] = pd.to_numeric(df["efficiency"], errors="coerce").fillna(2.0)
    if "mg53_check" not in df.columns:
        df["mg53_check"] = ""
    return df


def censor_cts(df, cfg):
    """Mark undetermined / Ct>censor as not detected. Returns df with 'detected' flag and
    'ct_used' (NaN where censored). Never imputes."""
    df = df.copy()
    undetermined = ~np.isfinite(df["ct_num"])
    over = df["ct_num"] > cfg["ct_censor"]
    df["censor_reason"] = np.where(undetermined, "undetermined",
                            np.where(over, f"Ct>{cfg['ct_censor']:g}", ""))
    df["detected"] = ~(undetermined | over)
    df["ct_used"] = np.where(df["detected"], df["ct_num"], np.nan)
    return df


def qc_censoring_table(df):
    """Per gene x condition: how many measurements were censored (reported, never imputed)."""
    g = (df.assign(n=1, cens=(~df["detected"]).astype(int))
           .groupby(["gene", "tp53", "mg53", "treatment", "time_h"], as_index=False)
           .agg(n_measurements=("n", "sum"),
                n_censored=("cens", "sum")))
    g["frac_censored"] = (g["n_censored"] / g["n_measurements"]).round(3)
    g["why"] = "undetermined or Ct>censor; censored (dropped from quantitation), never imputed"
    return g.sort_values(["frac_censored"], ascending=False)


def qc_techrep_table(df, cfg):
    """Technical-replicate spread per (biological sample, gene). Flag SD > threshold."""
    rows = []
    keys = BIO_KEYS + ["gene"]
    for key, sub in df.groupby(keys):
        cts = sub.loc[sub["detected"], "ct_used"].values
        n_det = len(cts)
        n_total = len(sub)
        sd = float(np.std(cts, ddof=1)) if n_det >= 2 else np.nan
        rng = float(np.max(cts) - np.min(cts)) if n_det >= 1 else np.nan
        rows.append(dict(zip(keys, key)) | dict(
            n_techrep=n_total, n_detected=n_det,
            ct_mean=float(np.mean(cts)) if n_det else np.nan,
            ct_sd=sd, ct_range=rng,
            flag_sd_gt_thresh=bool(np.isfinite(sd) and sd > cfg["techrep_sd_flag"]),
            partial_detection=bool(0 < n_det < n_total)))
    out = pd.DataFrame(rows)
    out["why"] = (f"technical replicate SD across detected Ct; flag if SD > "
                  f"{cfg['techrep_sd_flag']} cycles or only some reps detected")
    return out.sort_values("ct_sd", ascending=False, na_position="last")


def collapse_techreps(df):
    """Average detected Ct over technical replicates -> one Ct per (bio sample, gene)."""
    keys = BIO_KEYS + ["gene"]
    agg = (df[df["detected"]]
           .groupby(keys, as_index=False)
           .agg(ct=("ct_used", "mean"),
                efficiency=("efficiency", "mean"),
                n_techrep_detected=("ct_used", "size")))
    # samples where the gene was never detected: keep a censored row (ct = NaN)
    allcombos = df[keys].drop_duplicates()
    merged = allcombos.merge(agg, on=keys, how="left")
    merged["detected"] = np.isfinite(merged["ct"])
    # carry mg53_check / sample label
    meta = (df.groupby(BIO_KEYS, as_index=False)
              .agg(sample=("sample", "first"), mg53_check=("mg53_check", "first")))
    merged = merged.merge(meta, on=BIO_KEYS, how="left")
    return merged


# --------------------------------------------------------------------------- dCt / ddCt
def compute_dct(sample_ct, cfg):
    """dCt per (biological sample, target gene) vs geometric mean of reference quantities.

    In Ct space the geometric mean of reference *quantities* is the arithmetic mean of the
    reference Ct values (dividing each by log2(efficiency) when efficiency != 2)."""
    refs = set(cfg["references"])
    # per-sample reference mean (efficiency-weighted Ct)
    df = sample_ct.copy()
    df["ct_eff"] = df["ct"] * np.log2(df["efficiency"].clip(lower=1.0001))  # log2 quantity units
    ref_rows = df[df["gene"].isin(refs) & df["detected"]]
    refmean = (ref_rows.groupby(BIO_KEYS, as_index=False)
                       .agg(ref_ct_eff=("ct_eff", "mean"),
                            n_ref_detected=("gene", "nunique")))
    df = df.merge(refmean, on=BIO_KEYS, how="left")
    df["dct"] = df["ct_eff"] - df["ref_ct_eff"]        # pseudo-dCt (log2 quantity units)
    df["is_reference"] = df["gene"].isin(refs)
    df["dct_note"] = np.where(df["detected"] & np.isfinite(df["ref_ct_eff"]),
                              "dCt = Ct(target)-mean(Ct(ref)); efficiency-adjusted",
                              "pseudo-dCt not available (target or all references censored)")
    return df, refmean


def compute_ddct(dct_df, cfg):
    """ddCt vs matched control (same cell_line, treatment, time, bio_rep). If no bio_rep
    match, fall back to the mean control dCt for that cell_line/treatment/time."""
    df = dct_df.copy()
    ctrl = df[df["mg53"] == cfg["ref_mg53"]]
    # paired control (exact bio_rep)
    paired = (ctrl.groupby(["cell_line", "treatment", "time_h", "bio_rep", "gene"], as_index=False)
                   .agg(ctrl_dct_paired=("dct", "mean")))
    # pooled control (mean over bio_reps)
    pooled = (ctrl.groupby(["cell_line", "treatment", "time_h", "gene"], as_index=False)
                   .agg(ctrl_dct_pooled=("dct", "mean")))
    df = df.merge(paired, on=["cell_line", "treatment", "time_h", "bio_rep", "gene"], how="left")
    df = df.merge(pooled, on=["cell_line", "treatment", "time_h", "gene"], how="left")
    df["ctrl_dct"] = df["ctrl_dct_paired"].where(np.isfinite(df["ctrl_dct_paired"]),
                                                 df["ctrl_dct_pooled"])
    df["pairing"] = np.where(np.isfinite(df["ctrl_dct_paired"]), "paired_bio_rep",
                      np.where(np.isfinite(df["ctrl_dct_pooled"]), "pooled_control", "no_control"))
    df["ddct"] = df["dct"] - df["ctrl_dct"]
    df["log2fc"] = -df["ddct"]
    df["fold"] = np.power(2.0, df["log2fc"])
    return df


# --------------------------------------------------------------------------- reference QC
def qc_reference_stability(dct_df, sample_ct, cfg):
    """Two reference-stability reads:
       (1) geNorm M: for each reference, mean over the other references of SD of the
           pairwise log2 ratio across samples (= SD of Ct_i - Ct_j).
       (2) SD of each reference's dCt (vs the mean of the OTHER references) across conditions.
       Flag a reference that moves."""
    refs = [r for r in cfg["references"] if r in set(sample_ct["gene"])]
    out = []
    # wide table of reference Ct per sample
    wide = (sample_ct[sample_ct["gene"].isin(refs) & sample_ct["detected"]]
            .pivot_table(index=BIO_KEYS, columns="gene", values="ct", aggfunc="mean"))
    for ri in refs:
        if ri not in wide.columns:
            continue
        # geNorm M
        ms = []
        for rj in refs:
            if rj == ri or rj not in wide.columns:
                continue
            ratio = (wide[ri] - wide[rj]).dropna()
            if len(ratio) >= 2:
                ms.append(float(np.std(ratio, ddof=1)))
        genorm_m = float(np.mean(ms)) if ms else np.nan
        # reference dCt vs mean of other refs, per condition
        others = [c for c in wide.columns if c != ri]
        if others:
            ref_dct = wide[ri] - wide[others].mean(axis=1)
            tmp = ref_dct.reset_index().rename(columns={0: "refdct"})
            tmp.columns = list(ref_dct.index.names) + ["refdct"]
            cond = tmp.groupby(["tp53", "mg53", "treatment", "time_h"])["refdct"].mean()
            sd_across_cond = float(np.std(cond.values, ddof=1)) if len(cond) >= 2 else np.nan
            worst = (cond - cond.mean()).abs()
            worst_cond = worst.idxmax() if len(worst) else None
            worst_shift = float((cond - cond.mean()).reindex([worst_cond]).iloc[0]) if worst_cond is not None else np.nan
        else:
            sd_across_cond, worst_cond, worst_shift = np.nan, None, np.nan
        flag = bool((np.isfinite(genorm_m) and genorm_m > cfg["genorm_m_flag"]) or
                    (np.isfinite(sd_across_cond) and sd_across_cond > cfg["ref_move_flag"]))
        out.append({
            "reference": ri, "geNorm_M": round(genorm_m, 3) if np.isfinite(genorm_m) else np.nan,
            "dCt_SD_across_conditions": round(sd_across_cond, 3) if np.isfinite(sd_across_cond) else np.nan,
            "worst_condition": str(worst_cond) if worst_cond is not None else "",
            "worst_shift_cycles": round(worst_shift, 3) if np.isfinite(worst_shift) else np.nan,
            "flag_unstable": flag,
            "why": (f"geNorm M (flag >{cfg['genorm_m_flag']}) and SD of this reference's dCt "
                    f"across conditions (flag >{cfg['ref_move_flag']} cycles); a flagged "
                    f"reference moves and should be dropped / replaced"),
        })
    res = pd.DataFrame(out).sort_values("dCt_SD_across_conditions", ascending=False, na_position="last")
    return res


def qc_perturbation_check(ddct_df, cfg):
    """Did the MG53 perturbation work? Compare the MG53 readout assays (modules starting
    with 'MG53') in OE / KD vs control per cell line / treatment / time."""
    mg_genes = []
    for m, gs in cfg["modules"].items():
        if m.startswith("MG53"):
            mg_genes += gs
    mg_genes = set(mg_genes)
    sub = ddct_df[ddct_df["gene"].isin(mg_genes) & (ddct_df["mg53"] != cfg["ref_mg53"])]
    if sub.empty:
        return pd.DataFrame(columns=["gene", "cell_line", "mg53", "treatment", "time_h",
                                     "median_log2fc", "expected_dir", "consistent", "why"])
    rows = []
    for key, s in sub.groupby(["gene", "cell_line", "mg53", "treatment", "time_h"]):
        med = float(np.nanmedian(s["log2fc"].values))
        exp = "up" if key[2] == "overexpression" else "down"
        consistent = (med > 0.3) if exp == "up" else (med < -0.3)
        rows.append({"gene": key[0], "cell_line": key[1], "mg53": key[2],
                     "treatment": key[3], "time_h": key[4],
                     "median_log2fc": round(med, 3), "expected_dir": exp,
                     "consistent": bool(consistent),
                     "why": "MG53 readout should rise with OE and fall with KD; |log2fc|>0.3 = consistent"})
    return pd.DataFrame(rows).sort_values(["gene", "cell_line", "mg53"])


# --------------------------------------------------------------------------- design + model
def build_design(sub, factors, refs):
    """Return (X, specs, names). Dummy (reference-cell) coding for the given factors with
    main effects + all 2-/3-way interactions among factors that have >=2 levels. cell_line,
    if present in `factors`, is added additively (main effects only, no interactions)."""
    inter_factors = [f for f in factors if f != "cell_line"]
    cols = [np.ones(len(sub))]
    specs = [{}]
    names = ["Intercept"]
    # main-effect dummies for interaction factors
    maindum = {}
    for f in inter_factors:
        levels = [lv for lv in sorted(sub[f].astype(str).unique()) if lv != refs[f]]
        maindum[f] = {}
        for lv in levels:
            d = (sub[f].astype(str) == lv).astype(float).values
            maindum[f][lv] = d
            cols.append(d); specs.append({f: lv}); names.append(f"{f}[{lv}]")
    # interactions (2- and 3-way) among interaction factors
    present = [f for f in inter_factors if maindum.get(f)]
    from itertools import combinations, product
    for k in (2, 3):
        for combo in combinations(present, k):
            lvl_lists = [list(maindum[f].keys()) for f in combo]
            for lv_tuple in product(*lvl_lists):
                d = np.ones(len(sub))
                spec = {}
                for f, lv in zip(combo, lv_tuple):
                    d = d * maindum[f][lv]
                    spec[f] = lv
                if d.sum() == 0:
                    continue
                cols.append(d); specs.append(spec)
                names.append(":".join(f"{f}[{lv}]" for f, lv in spec.items()))
    # additive cell_line block (nuisance; not in contrasts)
    if "cell_line" in factors:
        levels = [lv for lv in sorted(sub["cell_line"].astype(str).unique())]
        if len(levels) >= 2:
            for lv in levels[1:]:
                d = (sub["cell_line"].astype(str) == lv).astype(float).values
                cols.append(d); specs.append({"cell_line": lv}); names.append(f"cell_line[{lv}]")
    X = np.column_stack(cols)
    return X, specs, names


def fit_model(X, y, groups=None, engine="ols"):
    """Fit the linear model. Returns (beta, cov, dof, used_engine, ok). OLS via numpy with
    t-based inference; MixedLM via statsmodels (bio_rep random effect) when requested and
    available, with z-based inference (dof -> inf)."""
    n, p = X.shape
    if engine == "mixedlm" and HAVE_SM and groups is not None:
        try:
            md = sm.MixedLM(y, X, groups=np.asarray(groups))
            res = md.fit(method="lbfgs", reml=True, disp=False)
            beta = np.asarray(res.fe_params, dtype=float)
            cov = np.asarray(res.cov_params(), dtype=float)[:p, :p]
            return beta, cov, np.inf, "mixedlm", True
        except Exception:
            pass  # fall through to OLS
    # numpy OLS
    XtX = X.T @ X
    XtX_inv = np.linalg.pinv(XtX)
    beta = XtX_inv @ X.T @ y
    resid = y - X @ beta
    rank = int(np.linalg.matrix_rank(X))
    dof = n - rank
    if dof <= 0:
        return beta, np.full((p, p), np.nan), dof, "ols", False
    sigma2 = float(resid @ resid) / dof
    cov = sigma2 * XtX_inv
    return beta, cov, dof, "ols", True


def contrast_vector(specs, mg53_level, group, treat, refs, interaction=False):
    """Build a contrast vector over the design columns.
       - effect of mg53=mg53_level vs control, at tp53=group and treatment=treat; or
       - interaction = effect(null) - effect(WT) at treatment=treat (interaction=True).
    """
    c = np.zeros(len(specs))
    for j, s in enumerate(specs):
        if s.get("mg53") != mg53_level:
            continue
        if "cell_line" in s:
            continue
        # treatment condition
        if treat == refs["treatment"]:
            if "treatment" in s:
                continue
        else:
            if "treatment" in s and s["treatment"] != treat:
                continue
        if interaction:
            # must involve tp53=null (the non-ref tp53 level)
            if s.get("tp53") != group:
                continue
        else:
            if group == refs["tp53"]:
                if "tp53" in s:
                    continue
            else:
                if "tp53" in s and s["tp53"] != group:
                    continue
        c[j] = 1.0
    return c


def eval_contrast(c, beta, cov, dof):
    est = float(c @ beta)
    var = float(c @ cov @ c)
    if not np.isfinite(var) or var < 0:
        return est, np.nan, np.nan, np.nan, np.nan
    se = math.sqrt(var)
    if se == 0:
        return est, 0.0, est, est, np.nan
    tstat = est / se
    if np.isfinite(dof):
        p = 2 * stats.t.sf(abs(tstat), dof)
        crit = stats.t.ppf(0.975, dof)
    else:
        p = 2 * stats.norm.sf(abs(tstat))
        crit = stats.norm.ppf(0.975)
    return est, se, est - crit * se, est + crit * se, p


# --------------------------------------------------------------------------- contrasts
def build_response_frames(ddct_df, cfg):
    """One frame per response: every panel gene (dct per sample), plus module scores
    (mean member dCt per sample), plus the p53 score. Returns list of dicts."""
    responses = []
    # per-gene
    genes_in_panel = {g for gs in cfg["modules"].values() for g in gs} | set(cfg["references"])
    gene_to_module = {}
    for m, gs in cfg["modules"].items():
        for g in gs:
            gene_to_module.setdefault(g, m)
    for g, sub in ddct_df.groupby("gene"):
        fam = gene_to_module.get(g, "reference" if g in set(cfg["references"]) else "other")
        d = sub[["cell_line", "tp53", "mg53", "treatment", "time_h", "bio_rep", "dct"]].copy()
        responses.append({"name": g, "kind": "gene", "family": fam, "data": d})
    # module scores (mean member dCt per sample)
    score_defs = {m: gs for m, gs in cfg["modules"].items()}
    score_defs["p53_score"] = cfg["p53_score_members"]
    for sname, members in score_defs.items():
        mem = ddct_df[ddct_df["gene"].isin(members)]
        if mem.empty:
            continue
        d = (mem.groupby(["cell_line", "tp53", "mg53", "treatment", "time_h", "bio_rep"],
                         as_index=False).agg(dct=("dct", "mean")))
        responses.append({"name": sname, "kind": "module_score", "family": sname, "data": d})
    return responses


def compute_contrasts(ddct_df, cfg, engine_req):
    rows = []
    responses = build_response_frames(ddct_df, cfg)
    mg_levels = [lv for lv in ddct_df["mg53"].unique() if lv != cfg["ref_mg53"]]
    for resp in responses:
        d_all = resp["data"].dropna(subset=["dct"])
        for time_h, d in d_all.groupby("time_h"):
            if len(d) < 4 or d["mg53"].nunique() < 2:
                continue
            factors = [f for f in ["mg53", "tp53", "treatment"] if d[f].nunique() >= 2]
            if "mg53" not in factors:
                continue
            refs = {"mg53": cfg["ref_mg53"], "tp53": cfg["ref_tp53"], "treatment": cfg["ref_treat"]}
            # ensure reference levels exist; else pick a present level
            for f in factors:
                if refs[f] not in set(d[f].astype(str)):
                    refs[f] = sorted(d[f].astype(str).unique())[0]
            fac_with_line = factors + (["cell_line"] if d["cell_line"].nunique() >= 2 else [])
            X, specs, names = build_design(d, fac_with_line, refs)
            y = d["dct"].values.astype(float)
            # map bio_rep to a group id for mixed model
            groups = (d["cell_line"].astype(str) + "|" + d["bio_rep"].astype(str)).values
            beta, cov, dof, used_engine, ok = fit_model(
                X, y, groups=groups, engine=("mixedlm" if engine_req in ("auto", "mixedlm") and HAVE_SM else "ols"))
            if not ok:
                continue
            treats = sorted(d["treatment"].astype(str).unique())
            tp53_levels = set(d["tp53"].astype(str).unique())
            has_wt = refs["tp53"] in tp53_levels
            null_level = next((lv for lv in tp53_levels if lv != refs["tp53"]), None)
            for m in mg_levels:
                if m not in set(d["mg53"].astype(str)):
                    continue
                for t in treats:
                    # effect in WT
                    if has_wt:
                        c = contrast_vector(specs, m, refs["tp53"], t, refs)
                        if c.sum() > 0:
                            est, se, lo, hi, p = eval_contrast(c, beta, cov, dof)
                            rows.append(_row(resp, time_h, m, t, "MG53_in_WT", est, se, lo, hi, p, used_engine, len(d)))
                    # effect in null
                    if null_level is not None:
                        c = contrast_vector(specs, m, null_level, t, refs)
                        if c.sum() > 0:
                            est, se, lo, hi, p = eval_contrast(c, beta, cov, dof)
                            rows.append(_row(resp, time_h, m, t, "MG53_in_null", est, se, lo, hi, p, used_engine, len(d)))
                    # interaction null - WT
                    if has_wt and null_level is not None:
                        c = contrast_vector(specs, m, null_level, t, refs, interaction=True)
                        if c.sum() > 0:
                            est, se, lo, hi, p = eval_contrast(c, beta, cov, dof)
                            rows.append(_row(resp, time_h, m, t, "MG53_x_TP53_interaction", est, se, lo, hi, p, used_engine, len(d)))
    res = pd.DataFrame(rows)
    if res.empty:
        return res
    # BH-FDR across genes within each (family, time, treatment, contrast, mg53) group;
    # applied to per-gene rows only.
    res["fdr"] = np.nan
    gene_mask = res["kind"] == "gene"
    for key, idx in res[gene_mask].groupby(["family", "time_h", "treatment", "contrast", "mg53"]).groups.items():
        res.loc[idx, "fdr"] = bh_fdr(res.loc[idx, "p"].values)
    return res


def _row(resp, time_h, m, t, contrast, est, se, lo, hi, p, engine, n):
    # est is on dCt (positive = expression DOWN). Report as log2 fold change (-est).
    return {
        "response": resp["name"], "kind": resp["kind"], "family": resp["family"],
        "time_h": time_h, "mg53": m, "treatment": t, "contrast": contrast,
        "log2fc": round(-est, 4),
        "ci_low": round(-hi, 4) if np.isfinite(hi) else np.nan,
        "ci_high": round(-lo, 4) if np.isfinite(lo) else np.nan,
        "se": round(se, 4) if np.isfinite(se) else np.nan,
        "p": p, "n_samples": int(n), "engine": engine,
        "dct_effect_pos_is_down": round(est, 4),
    }


# --------------------------------------------------------------------------- output tables
def per_condition_fold(ddct_df, cfg):
    """Rows = genes grouped by module; columns = conditions (OE/KD x tp53 x treatment x time).
    Value = fold (2^-median ddCt across samples)."""
    sub = ddct_df[ddct_df["mg53"] != cfg["ref_mg53"]].copy()
    if sub.empty:
        return pd.DataFrame()
    sub["condition"] = (sub["mg53"] + "|" + sub["tp53"] + "|" + sub["treatment"]
                        + "|" + sub["time_h"].astype(str) + "h")
    med = (sub.groupby(["gene", "condition"], as_index=False)
              .agg(median_ddct=("ddct", "median")))
    med["fold"] = np.power(2.0, -med["median_ddct"])
    wide = med.pivot_table(index="gene", columns="condition", values="fold")
    # attach module
    gene_to_module = {}
    for m, gs in cfg["modules"].items():
        for g in gs:
            gene_to_module.setdefault(g, m)
    wide.insert(0, "module", [gene_to_module.get(g, "other") for g in wide.index])
    order = {m: i for i, m in enumerate(cfg["modules"].keys())}
    wide = wide.assign(_o=[order.get(m, 999) for m in wide["module"]]).sort_values(["_o", "module"]).drop(columns="_o")
    return wide.round(3).reset_index()


def d1_primary_table(contrasts, cfg):
    """D1: p53 modules/score, MG53 x TP53 and the per-genotype effects. Primary flag on the
    p53_score MG53 effect in WT and the interaction, under a p53 activator."""
    if contrasts.empty:
        return contrasts
    fams = set(cfg["p53_module_families"]) | {"p53_score"}
    d = contrasts[contrasts["family"].isin(fams)].copy()
    acts = cfg.get("d1_activator_treatments")
    d["is_activator_treatment"] = d["treatment"].isin(acts) if acts else False
    d["is_primary"] = (
        (d["response"] == "p53_score")
        & d["is_activator_treatment"]
        & (d["mg53"] == "overexpression")
        & (d["contrast"].isin(["MG53_in_WT", "MG53_x_TP53_interaction"]))
    )
    d["why"] = np.where(
        d["contrast"] == "MG53_x_TP53_interaction",
        "D1 interaction: MG53 effect in null minus WT (0 => p53-dependent lowering is WT-specific)",
        "MG53 effect on p53 output (log2fc<0 = p53 targets down, consistent with MG53 lowering p53)")
    return d.sort_values(["is_primary", "response", "time_h", "treatment", "contrast"],
                         ascending=[False, True, True, True, True])


def screen_table(contrasts, cfg):
    """D2 screen: MG53 effect per screen gene/module, with a p53-independence call (effect
    present in TP53-null)."""
    if contrasts.empty:
        return contrasts
    fams = set(cfg["screen_module_families"])
    d = contrasts[contrasts["family"].isin(fams) & (contrasts["mg53"] == "overexpression")].copy()
    # p53-independence: significant MG53 effect in null
    d["p53_independent_signal"] = (d["contrast"] == "MG53_in_null") & (d["p"] < 0.05) & (d["log2fc"].abs() > 0.3)
    d["why"] = np.where(
        d["contrast"] == "MG53_in_null",
        "MG53 effect in TP53-null: a real effect here is p53-INDEPENDENT",
        np.where(d["contrast"] == "MG53_in_WT",
                 "MG53 effect in TP53-WT (may mix p53-dependent and -independent)",
                 "MG53 x TP53 interaction (nonzero => partly p53-dependent)"))
    return d.sort_values(["family", "response", "time_h", "treatment", "contrast"])


# --------------------------------------------------------------------------- report
def write_report(outdir, cfg, df, contrasts, d1, screen, qc_ref, qc_tech, qc_cens, qc_pert, used_engine):
    lines = []
    A = lines.append
    A("# MG53 (TRIM72) perturbation qPCR -- analysis report\n")
    A(f"- Rows in input (measurements): **{len(df)}**")
    A(f"- Biological samples: **{df[BIO_KEYS].drop_duplicates().shape[0]}**  "
      f"(cell lines {df['cell_line'].nunique()}, treatments {df['treatment'].nunique()}, "
      f"time points {sorted(df['time_h'].dropna().unique().tolist())})")
    A(f"- Genes assayed: **{df['gene'].nunique()}**; reference genes used: "
      f"**{', '.join([r for r in cfg['references'] if r in set(df['gene'])])}**")
    A(f"- Quantitation: 2^-ddCt (efficiency=2 unless a per-assay `efficiency` column is given); "
      f"dCt vs the geometric mean of the reference quantities (= mean reference Ct).")
    A(f"- Statistics engine: **{used_engine}** "
      f"({'statsmodels MixedLM, bio_rep random effect' if used_engine=='mixedlm' else 'numpy OLS fallback, t-based CIs; tech reps averaged, biological samples as rows'}).")
    A(f"- statsmodels installed: **{HAVE_SM}**.\n")

    # QC
    A("## QC\n")
    n_cens = int((~df["detected"]).sum())
    A(f"- Censored measurements (undetermined or Ct>{cfg['ct_censor']:g}): **{n_cens}** "
      f"of {len(df)} ({100*n_cens/max(len(df),1):.1f}%). Censored, never imputed. See `qc_censoring.csv`.")
    n_tech_flag = int(qc_tech["flag_sd_gt_thresh"].sum()) if not qc_tech.empty else 0
    A(f"- Technical-replicate SD > {cfg['techrep_sd_flag']} cycles: **{n_tech_flag}** (sample x gene). See `qc_techreps.csv`.")
    if not qc_ref.empty:
        movers = qc_ref[qc_ref["flag_unstable"]]["reference"].tolist()
        A(f"- Reference-gene stability (geNorm M, dCt SD across conditions): flagged unstable: "
          f"**{', '.join(movers) if movers else 'none'}**. See `qc_reference_stability.csv`.")
    if not qc_pert.empty:
        frac_ok = 100 * qc_pert["consistent"].mean()
        A(f"- Perturbation check (MG53 readout moves with OE/KD): **{frac_ok:.0f}%** of OE/KD conditions consistent. See `qc_perturbation_check.csv`.")
    A("")

    # D1
    A("## D1 (primary): does MG53-OE lower the p53 score in WT but not null?\n")
    prim = d1[d1.get("is_primary", False) == True] if not d1.empty else d1
    if d1.empty:
        A("_No D1 contrasts could be computed (check that TP53-WT, overexpression and an activator are present)._\n")
    elif prim.empty:
        A("_No p53 activator treatment was identified; D1 effects are tabulated for all treatments in `d1_primary.csv`._\n")
    else:
        A("| response | time_h | treatment | contrast | log2fc | 95% CI | p | FDR |")
        A("|---|---|---|---|---|---|---|---|")
        for _, r in prim.iterrows():
            ci = f"{r['ci_low']:.2f} to {r['ci_high']:.2f}" if np.isfinite(r['ci_low']) else "NA"
            fdr = f"{r['fdr']:.3g}" if np.isfinite(r.get('fdr', np.nan)) else "-"
            A(f"| {r['response']} | {r['time_h']:g} | {r['treatment']} | {r['contrast']} | "
              f"{r['log2fc']:+.2f} | {ci} | {r['p']:.2g} | {fdr} |")
        A("\nInterpretation: a **negative** `MG53_in_WT` log2fc = p53 targets fall with MG53 "
          "overexpression in TP53-WT (supports D1). An interaction near 0 that is driven by a "
          "WT-only effect = the lowering is p53-genotype-specific. Full table: `d1_primary.csv`.\n")

    # Screen
    A("## D2 (screen): other MG53 pathways; p53-independence\n")
    if screen.empty:
        A("_No screen contrasts computed._\n")
    else:
        indep = screen[screen["p53_independent_signal"] == True]
        A(f"- Screen genes with a **p53-independent** MG53-OE signal (significant in TP53-null): "
          f"**{', '.join(sorted(indep['response'].unique())) if not indep.empty else 'none at this power'}**.")
        A("- Full per-gene/per-treatment screen with genotype split and FDR: `screen.csv`.\n")

    A("## Output files\n")
    for fn, desc in [
        ("per_sample_dct.csv", "per biological sample x gene: Ct, dCt (pseudo-dCt explicit), ddCt vs matched control, fold, log2fc, pairing, censor status"),
        ("per_condition_fold.csv", "genes (grouped by module) x conditions; value = fold (2^-median ddCt)"),
        ("d1_primary.csv", "D1 result: p53 modules/score, MG53 effect in WT, in null, and the MG53 x TP53 interaction, by treatment and time, with 95% CI and BH-FDR"),
        ("screen.csv", "D2 screen: MG53-OE effect per screen gene/module with genotype split and p53-independence call"),
        ("contrasts_all.csv", "every contrast computed (all genes, modules, treatments, times)"),
        ("qc_censoring.csv", "censored measurements per gene x condition"),
        ("qc_techreps.csv", "technical-replicate spread per sample x gene"),
        ("qc_reference_stability.csv", "reference-gene stability (geNorm M + dCt SD across conditions)"),
        ("qc_perturbation_check.csv", "did MG53 OE/KD move the MG53 readout assays"),
    ]:
        A(f"- `{fn}` -- {desc}")
    with open(os.path.join(outdir, "REPORT.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")


# --------------------------------------------------------------------------- orchestration
def resolve_activators(df, cfg):
    if cfg.get("d1_activator_treatments"):
        return cfg
    treats = [t for t in df["treatment"].astype(str).unique()]
    keys = ("activator", "nutlin", "nutlin-3a", "rg7388", "idasanutlin", "apr-246")
    acts = [t for t in treats if any(k in t.lower() for k in keys)]
    cfg["d1_activator_treatments"] = acts
    return cfg


def run(args):
    cfg = load_config(args)
    df = load_input(args.input)
    df = censor_cts(df, cfg)
    cfg = resolve_activators(df, cfg)

    os.makedirs(args.outdir, exist_ok=True)

    # QC
    qc_cens = qc_censoring_table(df)
    qc_tech = qc_techrep_table(df, cfg)

    sample_ct = collapse_techreps(df)
    dct_df, _ = compute_dct(sample_ct, cfg)
    ddct_df = compute_ddct(dct_df, cfg)

    qc_ref = qc_reference_stability(dct_df, sample_ct, cfg)
    qc_pert = qc_perturbation_check(ddct_df, cfg)

    engine_req = args.engine
    contrasts = compute_contrasts(ddct_df, cfg, engine_req)
    used_engine = (contrasts["engine"].mode().iloc[0] if not contrasts.empty else
                   ("mixedlm" if engine_req in ("auto", "mixedlm") and HAVE_SM else "ols"))

    d1 = d1_primary_table(contrasts, cfg)
    screen = screen_table(contrasts, cfg)
    cond_fold = per_condition_fold(ddct_df, cfg)

    # write per-sample dCt (targets only; references kept for transparency)
    cols = (BIO_KEYS + ["sample", "gene", "is_reference", "ct", "n_ref_detected",
                        "dct", "dct_note", "ctrl_dct", "pairing", "ddct", "log2fc", "fold",
                        "detected"])
    per_sample = ddct_df.reindex(columns=[c for c in cols if c in ddct_df.columns]).copy()
    per_sample = per_sample.rename(columns={"dct": "pseudo_dct"})
    per_sample.round(4).to_csv(os.path.join(args.outdir, "per_sample_dct.csv"), index=False)

    cond_fold.to_csv(os.path.join(args.outdir, "per_condition_fold.csv"), index=False)
    (d1 if not d1.empty else pd.DataFrame()).to_csv(os.path.join(args.outdir, "d1_primary.csv"), index=False)
    (screen if not screen.empty else pd.DataFrame()).to_csv(os.path.join(args.outdir, "screen.csv"), index=False)
    (contrasts if not contrasts.empty else pd.DataFrame()).to_csv(os.path.join(args.outdir, "contrasts_all.csv"), index=False)
    qc_cens.to_csv(os.path.join(args.outdir, "qc_censoring.csv"), index=False)
    qc_tech.to_csv(os.path.join(args.outdir, "qc_techreps.csv"), index=False)
    qc_ref.to_csv(os.path.join(args.outdir, "qc_reference_stability.csv"), index=False)
    qc_pert.to_csv(os.path.join(args.outdir, "qc_perturbation_check.csv"), index=False)

    write_report(args.outdir, cfg, df, contrasts, d1, screen, qc_ref, qc_tech, qc_cens, qc_pert, used_engine)
    print(f"[analyze_mg53_qpcr] wrote outputs to {args.outdir} (engine={used_engine}, statsmodels={HAVE_SM})")
    return cfg, df, contrasts, d1, screen, qc_ref, qc_tech, qc_cens, qc_pert


def main():
    ap = argparse.ArgumentParser(description="Analyse MG53 (TRIM72) perturbation qPCR Ct data.")
    ap.add_argument("--input", required=True, help="tidy CSV of Ct values")
    ap.add_argument("--config", default=None, help="optional JSON config (references, modules, ...)")
    ap.add_argument("--panel", default=None, help="assay_panel/panel.csv (default: auto-locate)")
    ap.add_argument("--outdir", default="results", help="output directory")
    ap.add_argument("--engine", default="auto", choices=["auto", "ols", "mixedlm"],
                    help="auto: mixedlm if statsmodels present else ols")
    args = ap.parse_args()
    run(args)


if __name__ == "__main__":
    main()
