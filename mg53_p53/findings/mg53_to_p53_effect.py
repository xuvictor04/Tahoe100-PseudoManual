#!/usr/bin/env python3
"""Measure the change in p53 activity per change in MG53, with a p53-knockout-like control arm.

The question: for a doubling of MG53 (TRIM72) mRNA, how much does p53 activity change, and is that change
specific to cells that have working p53?

Design. Lines are split into arms by how much p53 activity they actually retain, so that the arms with no
p53 serve as a negative control. Tahoe has no engineered p53 knockout, but it has the next best thing: 10
lines whose only TP53 allele is truncated, splice-disrupted or deleted outright (KATO III is a whole-gene
deletion). Those cannot mount a p53 response, so any MG53 -> p53-activity slope measured in them is being
produced by something other than p53, and it is the right thing to subtract.

    A  functional p53      the lines the genotype-blind panel calls responsive (all are TP53 wild-type)
    B  WT, not responsive  TP53 wild-type by sequence but functionally damped
    B2 mutant, some activity
    C  low-activity mutant retains <= 15% of the wild-type-minus-null gap  (pseudo-control)
    D  p53-null CONTROL    truncating / splice / whole-gene deletion, core null reference  (knockout-like)

Model, per arm, matching the pipeline's fixed-effect structure: both cell-line and drug-dose means are
removed from the outcome and the exposure, then one slope is fitted. So the estimate uses only residual
co-variation: for a given line under a given drug, does p53 activity deviate from expectation in the same
direction MG53 does?

    outcome   P_r2_mean   the data-defined p53 program score for that line x drug-dose (log2)
    exposure  r2_mean     MG53's corrected log2 fold change for the same cell

The headline is reported both as log2 of the program per doubling of MG53 and as a percentage change in p53
activity, with the knockout-controlled contrast A - D.

Inference, and what changed from the first pass of this script. The arithmetic reproduces: the slopes this
file now prints agree with the ones it printed before to 1e-18, and `first_pass_b_minus_this` in the output
carries that difference per row. What changed is everything around the slope.

    1.  The fixed effects are absorbed exactly -- drug-dose cells inside each arm, plus an orthonormal basis
        of the cell-demeaned line dummies -- instead of by 60 rounds of iterated demeaning. `two_way_slope`
        below is kept as the first-pass reference implementation and is refitted per row as a check.
    2.  The standard error. The first pass used a CR0 cell-line SE and a 1.96 multiplier; with 6 to 21 lines
        per arm that is too small twice over, and it came out 12-58% too narrow. Every SE now carries the
        pipeline's CR1 factor computed FROM THAT ARM (1.05 to 1.20, not one pooled factor); the quoted
        interval is the conservative two-way (drug, line) cluster; and the critical value is a t on
        min(drugs, lines) - 1 degrees of freedom. Three intervals that excluded zero under the first pass --
        the low-activity mutants at both scopes, and the control arm under p53-activating drug-doses -- cross
        zero under this one.
    3.  The contrast A - D comes from a JOINT stacked fit with (drug-dose x arm) fixed-effect cells and
        arm-specific slopes, so its covariance is right under drug clustering. The first pass took `hypot` of
        two separate SEs, which is valid only under cell-line clustering, where the arms share no line and
        the covariance is exactly zero.
    4.  Two nulls instead of none, because the pipeline's own calibration says an analytic p is not evidence
        here [genome_wide/tables/c_calibration.csv: the analytic common-slope statistic is inflated ~4.4x and
        matched placebo exposures behave the same or worse]. The within-drug-dose exposure shuffle is
        reported but is ANTI-CONSERVATIVE for a line-level exposure, because permuting raw MG53 inside a
        drug-dose destroys the line-level structure the line fixed effect would otherwise absorb; its SD
        comes out 0.2 to 0.9 times the clustered SE. The null to read is the whole-line permutation, which
        reassigns each line's entire MG53 trajectory to another line of the same arm: it keeps the
        within-line dependence and reproduces the clustered SE. Both nulls' means are emitted, so a displaced
        null is visible rather than silent.
    5.  MDE uses the few-cluster multiplier t(.975, df) + t(.80, df) (3.11 at df 10, 2.95 at df 20) rather
        than the normal 2.8016, which is 5-11% too optimistic at these cluster counts. Both are emitted.
    6.  Disattenuation is group-specific -- 0.301 in TP53-wild-type lines, 0.283 in TP53-altered ones
        [two_way/tables/trim72_reliability.csv, i_all x ddxg x full] -- so the contrast is disattenuated arm
        by arm instead of by one pooled 0.289 divisor, which for a contrast spanning both genotypes is
        arithmetically wrong. Read `pct_true` as an upper bound on precision and NOT as a corrected estimate:
        90% of the (drug-dose, line) exposures rest on a single well whose program score is built from the
        same cells against the same total-UMI denominator with the same corrections subtracted, so exposure
        and outcome errors are not independent and the classical 1/reliability correction is not licensed in
        either direction.
    7.  Holm and BH over the pre-specified family -- program P, the four fittable arms and the contrast, both
        scopes, 10 tests -- so the one nominally small p is never reported unadjusted.

The outcome list grows itself: any overlay score `load()` finds is fitted as a secondary outcome, which is
how the non-p53 read-outs that carry MG53's real covariation get into the table. A continuous version is
fitted too: one pooled slope whose dependence on retained p53 activity is a coefficient rather than an arm.

NOT computable from a run's output alone: per-arm placebo-gene pseudo-controls (a matched gene put in MG53's
place within each arm) need per-line values for arbitrary genes, which only `export/all_genes` on the full
data provides. The pipeline's own `c_placebos.csv` has 200 placebo exposures at the wild-type / altered split
only, and is printed for context.

Usage:
    python3 mg53_to_p53_effect.py --results ~/Tahoe-100M/mg53_p53
"""
import argparse
import os

import numpy as np
import pandas as pd

ARMS = ["A. functional p53 (responsive)", "B. WT, not fully responsive", "B2. mutant, some activity",
        "C. low-activity mutant (pseudo-control)", "D. p53-null CONTROL (trunc/splice/del)"]

# the secondary outcomes, in the order they are reported; each is fitted only if load() found its column
OVERLAYS = [("curated 21-gene p53 panel", "OVERLAY_P53_ACTIVITY21_r2_mean"),
            ("stress / ISR markers (non-p53)", "OVERLAY_GM_stress_markers_r2_mean"),
            ("locus readthrough, FUS (non-p53)", "OVERLAY_GM_locus_readthrough_r2_mean"),
            ("housekeeping reference (non-p53)", "OVERLAY_GM_reference_r2_mean")]


def two_way_slope(s, x, y, cluster="cell_line_id", unit="drug_dose_row"):
    """One slope after removing both cluster and unit means from x and y, with a cluster-robust SE.

    The first pass's implementation, kept as a reference: `run()` refits it per row and reports the
    difference from the exactly-absorbed slope as `first_pass_b_minus_this`. Its CR0 SE and 1.96 multiplier
    are what the quoted intervals no longer use.
    """
    s = s.dropna(subset=[x, y]).copy()
    if s[cluster].nunique() < 3:
        return None
    s["_x"], s["_y"] = s[x].astype(float), s[y].astype(float)
    for _ in range(60):                                   # alternating projections; converges well before 60
        for c in ("_x", "_y"):
            s[c] -= s.groupby(cluster)[c].transform("mean")
            s[c] -= s.groupby(unit)[c].transform("mean")
    a, b = s["_x"].to_numpy(), s["_y"].to_numpy()
    sxx = float(np.sum(a * a))
    if sxx <= 0:
        return None
    beta = float(np.sum(a * b) / sxx)
    s["_r"] = b - beta * a
    num = sum(float(np.sum(g["_x"].to_numpy() * g["_r"].to_numpy())) ** 2 for _, g in s.groupby(cluster))
    se = float(np.sqrt(num) / sxx)
    return dict(b=beta, se=se, lo=beta - 1.96 * se, hi=beta + 1.96 * se,
                n_rows=len(s), n_lines=int(s[cluster].nunique()),
                pct=100 * (2 ** beta - 1), pct_lo=100 * (2 ** (beta - 1.96 * se) - 1),
                pct_hi=100 * (2 ** (beta + 1.96 * se) - 1),
                # smallest slope this arm could detect at 80% power, as a percentage
                mde_pct=100 * (2 ** (2.802 * se) - 1))


def load(res, state_dir):
    """The per-(drug-dose, line) panel: MG53's fold change, the p53 program score, the arm, the overlays.

    `drug` is carried because the second cluster dimension is the drug, which is the pipeline's choice; it
    comes from the same source table. The overlay scores are one extra merge and supply the secondary
    outcomes -- a run without that export simply fits the pre-specified outcome alone.
    """
    tx = pd.read_csv(os.path.join(res, "export/TRIM72/TRIM72_per_drugdose_line.csv"))
    pr = pd.read_csv(os.path.join(res, "export/downstream/program_scores_per_drugdose_line.csv"))
    act = pd.read_csv(os.path.join(res, "genome_wide/tables/b_drugdose_p53_activation.csv"))
    st = pd.read_csv(os.path.join(state_dir, "per_line_p53_state.csv"))
    nr = pd.read_csv(os.path.join(state_dir, "null_reference_lines.csv"))
    core = set(nr.loc[nr["role"].astype(str).str.startswith("null reference (core)"), "cell_line_id"])
    d = tx[["drug_dose_row", "drug", "cell_line_id", "cell_name", "tp53_group", "n_wells_r2", "r2_mean"]].merge(
        pr[["drug_dose_row", "cell_line_id", "P_r2_mean"]], on=["drug_dose_row", "cell_line_id"])
    ov = os.path.join(res, "export/downstream/overlay/scores_per_drugdose_line.csv")
    if os.path.exists(ov):
        o = pd.read_csv(ov)
        keep = [c for _, c in OVERLAYS if c in o.columns]
        if keep:
            d = d.merge(o[["drug_dose_row", "cell_line_id"] + keep], on=["drug_dose_row", "cell_line_id"],
                        how="left")
    d = d.merge(act[["drugdose_row", "in_S2_p53_activating"]], left_on="drug_dose_row",
                right_on="drugdose_row", how="left")
    d = d.merge(st[["cell_line_id", "functional_call", "ind_P_mean_frac_of_WT_gap"]],
                on="cell_line_id", how="left")
    d = d[(d["n_wells_r2"] >= 1) & d["r2_mean"].notna() & d["P_r2_mean"].notna()].copy()
    d["arm"] = np.where(d["functional_call"] == "responsive", ARMS[0],
                np.where(d["cell_line_id"].isin(core), ARMS[4],
                np.where(d["tp53_group"] == "WT", ARMS[1],
                np.where(d["ind_P_mean_frac_of_WT_gap"] <= 0.15, ARMS[3], ARMS[2]))))
    return d


def run(d, out, n_shuf=2000, n_line=1000, seed=20261102):
    """Per-arm MG53 -> p53-activity slopes with the p53-null arm as the knockout-like control.

    What this fixes in the first pass. (1) The fixed effects are absorbed exactly (drug-dose cells inside each
    arm, plus cell line) instead of by iterated demeaning: the slopes come out identical to 1e-18, so this is a
    reproduction, not a change. (2) The inference. The first pass used a CR0 cell-line SE and 1.96; with 6 to 21
    lines per arm that is too small twice over, so every SE now carries the pipeline's CR1 factor computed FROM
    THAT ARM (1.05 to 1.20, not one pooled factor), the quoted interval is the conservative two-way (drug, line)
    cluster, and the critical value is a t on (min(drugs, lines) - 1) degrees of freedom. The one arm whose
    first-pass interval excluded zero at both scopes (the low-activity mutants) and the control arm's
    p53-activating slope then cross zero. (3) The contrast comes from a JOINT stacked fit with (drug-dose x arm)
    cells, so its covariance is right under drug clustering and it gets a two-way interval of its own; the first
    pass's hypot of two SEs is only valid under line clustering, where the arms share no cell line. (4) Two nulls
    instead of none, because the pipeline's calibration says an analytic p is not evidence on its own
    [genome_wide/tables/c_calibration.csv: the analytic common-slope statistic is inflated ~4.4x and matched
    placebo exposures behave the same or worse]. The within-drug-dose exposure shuffle is reported but is
    ANTI-CONSERVATIVE for a line-level exposure - permuting raw MG53 inside a drug-dose destroys the line-level
    structure the line fixed effect would otherwise absorb, and its SD comes out 0.2 to 0.9 times the clustered
    SE. The null to read is the whole-line permutation, which reassigns each line's entire MG53 trajectory to
    another line of the same arm: it preserves within-line dependence, and its SD reproduces the clustered SE
    (0.86 to 0.94 of it in the arms with a near-complete panel). Both nulls' means are reported, so a displaced
    null is visible rather than silent. (5) MDE uses the few-cluster multiplier t(.975, df) + t(.80, df) (3.11 at
    df 10, 2.95 at df 20), not the normal 2.8016, which is 5-11% too optimistic here; both are emitted.
    (6) Disattenuation is group-specific: MG53's full-data reliability is 0.301 in TP53-WT lines and 0.283 in
    TP53-altered ones [two_way/tables/trim72_reliability.csv, i_all x ddxg x full], so the contrast is
    disattenuated arm by arm rather than by one 0.289 divisor. Read pct_true as an upper bound on precision, not
    as a corrected estimate: 90% of the (drug-dose, line) exposures rest on a single well whose program score is
    built from the same cells with the same composition and position corrections subtracted, so exposure and
    outcome errors are not independent and the classical correction is not licensed in either direction.
    (7) Holm and BH over the pre-specified family, so the one nominally small p is reported adjusted. The
    outcome list grows itself: any of the overlay scores present in d (one more merge in load()) is fitted as a
    secondary outcome, which is how the non-p53 read-outs that carry MG53's real covariation get into the table.

    Columns. b is log2 of the outcome per doubling of MEASURED MG53; (lo, hi) is the two-way cluster interval and
    the one to quote, (lo_line, hi_line) the same fit clustered on cell line alone - the dimension the first
    pass used, but not its interval, which took this SE divided by the arm's CR1 factor and times 1.96; pct is
    the percentage change in p53 activity, pct_true the same per doubling of TRUE MG53; mde_pct is the smallest
    change this arm could have detected at 80% power, mde_pct_z the same with the normal multiplier; p_shuffle
    and p_line are the two nulls, sd_shuffle_over_se and sd_line_over_se their SDs as a fraction of the quoted
    SE (a value well below 1 marks an anti-conservative null); cluster2 names the second cluster dimension, which
    is the drug when load() carries a 'drug' column (one more column from the same source table) and otherwise
    the drug-dose, which is coarser than nothing but not the pipeline's choice.
    """
    T975 = (float("nan"), 12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179,
            2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056,
            2.052, 2.048, 2.045, 2.042)
    T80 = (float("nan"), 1.376, 1.061, 0.978, 0.941, 0.920, 0.906, 0.896, 0.889, 0.883, 0.879, 0.876, 0.873,
           0.870, 0.868, 0.866, 0.865, 0.863, 0.862, 0.861, 0.860, 0.859, 0.858, 0.858, 0.857, 0.856, 0.856,
           0.855, 0.855, 0.854, 0.854)
    REL = {"WT": 0.300737, "altered": 0.282534}            # [trim72_reliability.csv, i_all x ddxg x full]
    WT_ARMS = (ARMS[0], ARMS[1])                           # arms A and B are TP53 wild-type by sequence

    def tq(tab, df):
        """Quantile of t on df degrees of freedom, from the table above (normal limit past 30)."""
        return float(tab[df]) if 1 <= df < len(tab) else (1.96 if tab is T975 else 0.8416)

    def pct(v):
        """A log2 slope as a percentage change in p53 activity per doubling of MEASURED MG53."""
        return 100 * (2 ** v - 1)

    def pct_true(v, rel):
        """The same per doubling of TRUE MG53, dividing by that arm's exposure reliability."""
        return 100 * (2 ** (v / rel) - 1)

    def perm_p(obs, null):
        """Two-sided empirical p: (1 + #|null| >= |observed|) / (draws + 1)."""
        null = np.asarray(null, float)
        null = null[np.isfinite(null)]
        if not np.isfinite(obs) or not len(null):
            return np.nan
        return float((1 + (np.abs(null) >= abs(obs) - 1e-12).sum()) / (len(null) + 1))

    def nstat(v, f):
        """f over the finite values of v, or nan when there are none - a null that was not run stays silent."""
        v = np.asarray(v, float)
        v = v[np.isfinite(v)]
        return float(f(v)) if len(v) else np.nan

    def cellsum(V, a):
        """Per-fixed-effect-cell column sums of V, in cell order (reduceat on the rows sorted by cell)."""
        return np.add.reduceat(V[a["ordr"]], a["edges"], axis=0)

    def absorb(cell, line):
        """Exact (cell + line) absorption: the cell index and counts, the row order and edges the sums use, and
        an orthonormal basis of the cell-demeaned line dummies. Fit and nulls are projections on these, so
        nothing is iterated and nothing is approximate."""
        ci = pd.factorize(np.asarray(cell))[0]
        cnt = np.bincount(ci).astype(float)
        ordr = np.argsort(ci, kind="stable")
        edges = np.concatenate([[0], np.cumsum(cnt[:-1]).astype(int)])
        li = pd.factorize(np.asarray(line))[0]
        L = np.zeros((len(ci), int(li.max()) + 1))
        L[np.arange(len(ci)), li] = 1.0
        a = dict(ci=ci, cnt=cnt, ordr=ordr, edges=edges, li=li, n_cells=len(cnt), Q=None)
        Ld = L - cellsum(L, a)[ci] / cnt[ci, None]
        u, sv, _ = np.linalg.svd(Ld, full_matrices=False)
        a["Q"] = u[:, sv > sv[0] * 1e-9] if len(sv) and sv[0] > 0 else np.zeros((len(ci), 0))
        return a

    def resid(V, a):
        """V with both fixed effects removed (cell means, then the line basis)."""
        V2 = V if V.ndim == 2 else V[:, None]
        Vd = V2 - cellsum(V2, a)[a["ci"]] / a["cnt"][a["ci"], None]
        R = Vd - a["Q"] @ (a["Q"].T @ Vd)
        return R if V.ndim == 2 else R[:, 0]

    def fit(a):
        """OLS on the residualised arrays, with CR1 covariances clustered on cell line, on the second dimension,
        and on their intersection. p counts the absorbed fixed effects, so the factor is the pipeline's
        (two_way.cluster_vcov) and it is computed from THIS block, not from a pooled fit."""
        bread = np.linalg.inv(a["xt"].T @ a["xt"])
        b = bread @ (a["xt"].T @ a["ytil"])
        e = a["ytil"] - a["xt"] @ b
        p = a["xt"].shape[1] + a["n_cells"] + int(a["li"].max())
        V = {}
        nl = int(a["li"].max()) + 1
        for nm, g in (("line", a["li"]), ("two", a["di"]), ("inter", a["di"] * nl + a["li"])):
            gi = pd.factorize(g)[0]
            G = int(gi.max()) + 1
            S = np.zeros((G, a["xt"].shape[1]))
            np.add.at(S, gi, a["xt"] * e[:, None])
            c = G / max(G - 1, 1) * (a["n"] - 1) / max(a["n"] - p, 1)
            V[nm] = c * bread @ (S.T @ S) @ bread
            V["G_" + nm] = G
        return b, V

    def se_two(V, R):
        """The conservative two-way SE for the combination R: sqrt(max(V_2 + V_l - V_inter, V_2, V_l))."""
        v2, vl, vi = (float(R @ V[k] @ R) for k in ("two", "line", "inter"))
        return float(np.sqrt(max(v2 + vl - vi, v2, vl, 0.0)))

    def block(s, y, w=None):
        """One fitting block: the absorption, the residualised outcome and regressors, the two cluster indices,
        and the raw (line x cell) exposure panel the whole-line permutation needs."""
        cell = s["_cell"].to_numpy()
        a = absorb(cell, s["cell_line_id"].to_numpy())
        W = np.ones((len(s), 1)) if w is None else np.asarray(w, float)
        a.update(n=len(s), W=W, di=pd.factorize(s[clus2].to_numpy())[0],
                 ytil=resid(s[y].to_numpy(float), a),
                 xt=resid(s["r2_mean"].to_numpy(float)[:, None] * W, a),
                 sd_x=float(np.std(resid(s["r2_mean"].to_numpy(float), a))),
                 sd_y=float(np.std(resid(s[y].to_numpy(float), a))))
        piv = s.pivot_table(index="cell_line_id", columns="_cell", values="r2_mean", aggfunc="first")
        a.update(M=piv.to_numpy(float), cell=cell, line=s["cell_line_id"].to_numpy(), yraw=s[y].to_numpy(float),
                 ri=s["cell_line_id"].map({v: i for i, v in enumerate(piv.index)}).to_numpy(),
                 cj=s["_cell"].map({v: i for i, v in enumerate(piv.columns)}).to_numpy())
        return a

    def shuffle_null(blocks, x, key, n, sd):
        """MG53 shuffled across cell lines INSIDE each drug-dose, the same shuffle for every arm so the contrast
        has a null too. Anti-conservative for a line-level slope (it breaks the within-line structure); reported
        for comparability with the pipeline's calibration, not as the primary inference.
        No projection per draw: x~'y~ = v'ytil and x~'x~ = sum v^2 - sum_cell cellsum^2 / n_cell - |Q'v|^2."""
        rng = np.random.default_rng(sd)
        k = np.unique(np.asarray(key), return_inverse=True)[1].astype(float)[:, None]
        order = np.argsort(k[:, 0], kind="stable")
        outn = np.empty((n, sum(b["W"].shape[1] for b in blocks)))
        for c0 in range(0, n, 100):
            nb = min(100, n - c0)
            sh = np.argsort(k + rng.random((len(x), nb)), axis=0)       # a fresh order inside each drug-dose
            XP = np.empty((len(x), nb))
            XP[order] = x[sh]
            col = 0
            for a in blocks:
                J = a["W"].shape[1]
                V = [XP[a["rows"]] * a["W"][:, j:j + 1] for j in range(J)]
                S = [cellsum(v, a) for v in V]
                P = [a["Q"].T @ v for v in V]
                G = np.empty((nb, J, J))
                for j in range(J):
                    for m in range(j, J):
                        G[:, j, m] = G[:, m, j] = ((V[j] * V[m]).sum(0) - (S[j] * S[m] / a["cnt"][:, None]).sum(0)
                                                   - (P[j] * P[m]).sum(0))
                C = np.stack([a["ytil"] @ v for v in V], axis=1)
                outn[c0:c0 + nb, col:col + J] = np.linalg.solve(G, C[:, :, None])[:, :, 0]
                col += J
        return outn

    def line_null(a, n, sd):
        """Each cell line's WHOLE MG53 trajectory reassigned to another line of the same arm. This is the
        design-based null for a line-level exposure under a line fixed effect: it keeps the within-line
        dependence that makes the clustered SE large, and its SD comes out close to that SE. The panel is
        unbalanced, so the fixed effects are re-absorbed per draw on the rows the donor line actually has."""
        rng = np.random.default_rng(sd)
        nl = a["M"].shape[0]
        b = np.full(n, np.nan)
        for t in range(n):
            while True:
                pm = rng.permutation(nl)
                if (pm != np.arange(nl)).any():
                    break
            xv = a["M"][pm[a["ri"]], a["cj"]]
            ok = np.isfinite(xv)
            aa = a if ok.all() else absorb(a["cell"][ok], a["line"][ok])
            xt = resid(xv[ok], aa)
            yt = a["ytil"] if ok.all() else resid(a["yraw"][ok], aa)
            sxx = float(xt @ xt)
            if sxx > 0:
                b[t] = float(xt @ yt) / sxx
        return b

    def report(est, V, R, a, rel, nulls, extra):
        """One output row: the slope, the cell-line-clustered and the conservative two-way interval (the latter
        on a t with (min clusters - 1) df and the one to quote), the percentage change per doubling of measured
        and of true MG53, the two nulls, and the MDE with the few-cluster and the normal multiplier."""
        seL, se2 = float(np.sqrt(float(R @ V["line"] @ R))), se_two(V, R)
        Gl, G2 = V["G_line"], min(V["G_line"], V["G_two"])
        df, dfl = max(G2 - 1, 1), max(Gl - 1, 1)
        tc, mult = tq(T975, df), tq(T975, df) + tq(T80, df)
        lo, hi = est - tc * se2, est + tc * se2
        sdn = {k: nstat(v, np.std) for k, v in nulls.items()}
        return dict(extra, b=est, se_line=seL, se_twoway=se2, n_lines=int(Gl), n_clusters2=int(V["G_two"]),
                    cluster2=clus2, df=df, t_mult=tc, lo=float(lo), hi=float(hi),
                    lo_line=float(est - tq(T975, dfl) * seL), hi_line=float(est + tq(T975, dfl) * seL),
                    t=est / se2 if se2 > 0 else np.nan, n_rows=a["n"], n_cells=a["n_cells"],
                    sd_x_resid=a["sd_x"], sd_y_resid=a["sd_y"],
                    partial_r=est * a["sd_x"] / a["sd_y"] if a["sd_y"] > 0 else np.nan,
                    pct=pct(est), pct_lo=pct(lo), pct_hi=pct(hi), reliability=rel,
                    pct_true=pct_true(est, rel), pct_true_lo=pct_true(lo, rel), pct_true_hi=pct_true(hi, rel),
                    mde=mult * se2, mde_pct=pct(mult * se2), mde_pct_true=pct_true(mult * se2, rel),
                    mde_mult=mult, mde_pct_z=pct(2.8016 * se2),
                    p_shuffle=perm_p(est, nulls["shuffle"]), p_line=perm_p(est, nulls["line"]),
                    mean_shuffle=nstat(nulls["shuffle"], np.mean), mean_line=nstat(nulls["line"], np.mean),
                    sd_shuffle_over_se=sdn["shuffle"] / se2 if se2 > 0 else np.nan,
                    sd_line_over_se=sdn["line"] / se2 if se2 > 0 else np.nan, n_shuf=n_shuf, n_line=n_line)

    # the second cluster dimension: the drug when load() carries it, else the drug-dose (coarser than nothing,
    # but the pipeline clusters on the drug - one more column from export/TRIM72/TRIM72_per_drugdose_line.csv)
    clus2 = "drug" if "drug" in d.columns else "drug_dose_row"
    outcomes = [(n, c) for n, c in ([("data-defined p53 program P", "P_r2_mean")] + OVERLAYS)
                if c in d.columns]
    rows = []
    scopes = (("all drug-doses", d), ("p53-activating drug-doses", d[d["in_S2_p53_activating"] == True]))  # noqa
    for scope, sub0 in scopes:
        for onm, ocol in outcomes:
            sub = sub0.dropna(subset=["r2_mean", ocol]).reset_index(drop=True)
            sub["_cell"] = sub["drug_dose_row"]
            x, key = sub["r2_mean"].to_numpy(float), sub["drug_dose_row"].to_numpy()
            blocks, keys = [], []
            for arm in ARMS:
                m = np.flatnonzero((sub["arm"] == arm).to_numpy())
                if len(m) < 100 or sub.loc[m, "cell_line_id"].nunique() < 3:
                    continue
                a = block(sub.iloc[m], ocol)
                a["rows"] = m
                blocks.append(a)
                keys.append(arm)
            shuf = shuffle_null(blocks, x, key, n_shuf, seed)
            # the whole-line null re-absorbs the fixed effects per draw, so it is run for the pre-specified
            # outcome only; a secondary outcome carries its interval and the (anti-conservative) shuffle
            lnul = {arm: (line_null(a, n_line, seed + 7 + j) if ocol == "P_r2_mean" else np.array([np.nan]))
                    for j, (arm, a) in enumerate(zip(keys, blocks))}
            one = np.ones(1)
            for j, (arm, a) in enumerate(zip(keys, blocks)):
                b, V = fit(a)
                rel = REL["WT"] if arm in WT_ARMS else REL["altered"]
                chk = two_way_slope(sub[sub["arm"] == arm], "r2_mean", ocol)    # the first pass, as a check
                rows.append(report(float(b[0]), V, one, a, rel,
                                   dict(shuffle=shuf[:, j], line=lnul[arm]),
                                   dict(scope=scope, outcome=onm, arm=arm, prespecified=ocol == "P_r2_mean",
                                        first_pass_b_minus_this=(chk["b"] - float(b[0])) if chk else np.nan)))
            if ARMS[0] in keys and ARMS[4] in keys:        # the knockout-controlled contrast, jointly fitted
                iA, iD = keys.index(ARMS[0]), keys.index(ARMS[4])
                m = np.concatenate([blocks[iA]["rows"], blocks[iD]["rows"]])
                s = sub.iloc[m].copy()
                s["_cell"] = s["drug_dose_row"].astype(str) + "|" + s["arm"]   # cells are drug-dose x arm
                W = np.column_stack([(s["arm"] == ARMS[0]).to_numpy(float),
                                     (s["arm"] == ARMS[4]).to_numpy(float)])
                aj = block(s, ocol, W)
                b, V = fit(aj)
                R = np.array([1.0, -1.0])
                est = float(R @ b)
                # the arms share no cell line, so under line clustering their covariance is zero; the joint fit
                # is what makes the drug-clustered covariance right, which hypot of two SEs cannot be
                nulls = dict(shuffle=shuf[:, iA] - shuf[:, iD], line=lnul[ARMS[0]] - lnul[ARMS[4]])
                r = report(est, V, R, aj, REL["WT"], nulls,
                           dict(scope=scope, outcome=onm, arm="CONTRAST: functional minus p53-null",
                                prespecified=ocol == "P_r2_mean", first_pass_b_minus_this=np.nan))
                # group-specific disattenuation: one 0.289 divisor is wrong for a contrast across genotypes
                r.update(reliability=np.nan, b_true=float(b[0]) / REL["WT"] - float(b[1]) / REL["altered"],
                         pct_true=pct(float(b[0]) / REL["WT"] - float(b[1]) / REL["altered"]),
                         pct_true_lo=np.nan, pct_true_hi=np.nan,
                         mde_pct_true=pct(r["mde"] / REL["WT"]))
                rows.append(r)
        # the continuous version: one pooled fit whose MG53 slope may depend on how much p53 activity the line
        # retains. The drug-dose cell is crossed with the TP53 group, because with a pooled drug-dose fixed
        # effect the moderator also picks up each drug-dose's WT-selective p53 response - a design artifact the
        # shuffle null exposes by centring on the coefficient itself rather than on zero.
        f = "ind_P_mean_frac_of_WT_gap"
        ms = sub0.dropna(subset=["r2_mean", "P_r2_mean", f]).reset_index(drop=True)
        ms["_cell"] = ms["drug_dose_row"].astype(str) + "|" + ms["tp53_group"].astype(str)
        mu = ms.groupby("cell_line_id")[f].first().mean()
        am = block(ms, "P_r2_mean", np.column_stack([np.ones(len(ms)), ms[f].to_numpy(float) - mu]))
        am["rows"] = np.arange(len(ms))
        sh = shuffle_null([am], ms["r2_mean"].to_numpy(float), ms["drug_dose_row"].to_numpy(), n_shuf, seed)
        b, V = fit(am)
        for j, nm in enumerate((f"slope at the mean retained p53 activity ({mu:.2f} of the WT gap)",
                                "slope change per unit of retained p53 activity")):
            e = np.zeros(2)
            e[j] = 1.0
            rows.append(report(float(b[j]), V, e, am, REL["altered"],
                               dict(shuffle=sh[:, j], line=np.array([np.nan])),
                               dict(scope=f"continuous: {scope}", outcome="data-defined p53 program P", arm=nm,
                                    prespecified=False, first_pass_b_minus_this=np.nan)))
    t = pd.DataFrame(rows)
    # Holm and BH over the pre-specified family (program P, the four arms and the contrast, both scopes), so the
    # one nominally small p is never reported unadjusted. No analytic p is emitted: the interval carries that
    # inference, and a t tail needs more than numpy.
    fam = t.index[t["prespecified"].astype(bool)]
    for col in ("p_shuffle", "p_line"):
        q = t.loc[fam, col].to_numpy(float)
        o = np.argsort(np.where(np.isfinite(q), q, 2.0))
        n = int(np.isfinite(q).sum())
        holm, bh = np.full(len(q), np.nan), np.full(len(q), np.nan)
        hi_run, lo_run = 0.0, 1.0
        for i, k in enumerate(o[:n]):
            hi_run = max(hi_run, (n - i) * q[k])
            holm[k] = min(hi_run, 1.0)
        for i in range(n - 1, -1, -1):
            lo_run = min(lo_run, n / (i + 1) * q[o[i]])
            bh[o[i]] = lo_run
        t.loc[fam, "holm_" + col] = holm
        t.loc[fam, "bh_" + col] = bh
    t.to_csv(os.path.join(out, "mg53_to_p53_effect.csv"), index=False)
    return t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--results", default=os.environ.get("MG53_RESULTS") or os.path.expanduser("~/Tahoe-100M/mg53_p53"))
    ap.add_argument("--out", default=os.path.join(here, "tables"))
    ap.add_argument("--state-dir", default=os.path.join(here, "tables"),
                    help="where per_line_p53_state.csv and null_reference_lines.csv live")
    a = ap.parse_args()
    res, out = (os.path.abspath(os.path.expanduser(p)) for p in (a.results, a.out))
    os.makedirs(out, exist_ok=True)
    t = run(load(res, os.path.abspath(os.path.expanduser(a.state_dir))), out)
    pre = t[t["prespecified"].astype(bool)]
    for scope, s in pre.groupby("scope", sort=False):
        print(f"\n===== {scope}   (outcome: data-defined p53 program P)")
        print(f"{'arm':42s} {'lines':>5} {'df':>3} {'slope (log2 P / doubling MG53)':>32} "
              f"{'change in p53 activity':>26} {'line p':>7} {'MDE80':>8}")
        for _, r in s.iterrows():
            print(f"{r['arm']:42s} {int(r['n_lines']):5d} {int(r['df']):3d}   "
                  f"{r['b']:+.5f} ({r['lo']:+.5f},{r['hi']:+.5f})"
                  f"   {r['pct']:+.3f}% ({r['pct_lo']:+.3f},{r['pct_hi']:+.3f})"
                  f"  {r['p_line']:7.4f}  {r['mde_pct']:+.3f}%")
    sec = t[~t["prespecified"].astype(bool) & ~t["scope"].astype(str).str.startswith("continuous")]
    if len(sec):
        print("\n===== secondary and control outcomes (same model, same exposure)")
        print(f"{'arm':42s} {'outcome':34s} {'slope':>10} {'95% CI':>22} {'part. r':>8} {'shuf p':>7}")
        for _, r in sec.iterrows():
            print(f"{r['arm']:42s} {str(r['outcome'])[:34]:34s} {r['b']:+10.5f} "
                  f"({r['lo']:+.5f},{r['hi']:+.5f})  {r['partial_r']:+8.3f} {r['p_shuffle']:7.4f}")
    print("\nMDE80 = the smallest change this arm could have detected at 80% power, with the few-cluster")
    print("multiplier t(.975,df) + t(.80,df); 'line p' is the whole-line exposure permutation, which is the")
    print("calibrated null. The quoted interval is the conservative two-way (drug, line) CR1 cluster on a t")
    print("with min(drugs, lines) - 1 df; the within-drug-dose shuffle p in the CSV is anti-conservative here.")
    print("Arm D cannot mount a p53 response, so any slope there is not p53-mediated and is the control.")
    print(f"\nwrote {os.path.join(out, 'mg53_to_p53_effect.csv')}")


if __name__ == "__main__":
    main()
