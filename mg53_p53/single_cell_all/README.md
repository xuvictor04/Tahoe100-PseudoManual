# single_cell_all: TRIM72-detected vs undetected single cells in every well (D1b at full scale)

Step D1b of the MG53 (TRIM72) / p53 workstream, using Tahoe-100M's own data only. Inside every (well, cell line) group,
do cells with detected TRIM72 mRNA carry more or less p53-target mRNA than their neighbours without it, and is that
difference larger in TP53 wild-type lines than in TP53-altered lines?

Tahoe has no MG53 perturbation and measures mRNA only. Every number here is an **association** between TRIM72 mRNA
and p53-target mRNA in single cells, read from target-gene mRNA, never p53 protein. The TP53 genotype is the control:
an MG53 -> p53 effect can only act where p53 works. The primary estimand is therefore the TRIM72 log rate ratio in
TP53-WT lines **minus** that in TP53-altered lines; anything equal in both groups does not go through p53.

## Answer

**No TP53-dependent association between a cell's TRIM72 and its p53 output (the pre-specified primary estimand),
across 803,499 TRIM72-detected cells in 30,803 (well, line) groups.**

- **Size of what is excluded:** a WT-specific *decrease* of more than ~1.2% in p53-target counts per doubling of a
  cell's TRIM72, and an increase of more than ~5.9%. If half of TRIM72's overdispersion is technical, ~1.8% and ~9.3%.
  These bounds depend on an overdispersion model, see the caveats.
- **What does move with TRIM72:** TRIM72-detected cells carry more p53-target mRNA in both TP53 groups, but placebo
  genes do the same (generic). They carry more ATF3 than placebo genes do, equally in WT and altered lines (a shared
  stress state, not p53).
- **Secondary signal, opposite direction:** a few single p53 targets of the DNA-repair arm (XPC, DDB2, ZMAT3) lean
  *higher* in TRIM72-detected WT cells. That is the opposite of an MG53-lowers-p53 effect, and it is not significant
  for the pre-specified score.
- **Grouped by measured p53 function instead of genotype** (not pre-specified): the P53 score lean is larger, +0.082
  log RR in p53-responsive minus unresponsive lines (permutation p 0.010, HK p 0.078), above all 16 placebo
  predictors (empirical p 0.059, the smallest possible with 16). Same direction as the secondary signal: more
  p53-target mRNA in TRIM72-detected cells where p53 works, again the opposite of MG53 lowering p53. It comes from
  the 'other drugs' wells and MDM2 / XPC / DDB2 / ZMAT3, not from DMSO or the TRIM72 raisers, and not from CDKN1A.
- **Ambient negative controls:** a predictor that can only be ambient RNA ('CDKN2A detected' in CDKN2A-deleted lines)
  gives a WT - alt P53 score difference of -0.086 (HK p 0.004, 7 vs 6 lines). With few lines a single contrast can
  look significant from soup alone, so only placebo-calibrated results are read. Soup does not reproduce TRIM72's
  ATF3 or TP53-mRNA association (TRIM72 at the 100th, CDKN2A at the 47th / 60th percentile of the placebos there).

All numbers below are for all wells pooled unless a class is named. Rate ratio (RR) = counts per UMI in
TRIM72-detected vs undetected cells of the same well and line, adjusted for depth and cell cycle. "WT - alt" is the
difference of the log RRs between TP53-WT (17 lines) and TP53-altered (30 lines). CIs and the first p are
Hartung-Knapp (HK: t on lines - 1 df, Welch df for WT - alt; never narrower than DerSimonian-Laird). The earlier
DerSimonian-Laird normal CIs, which are narrower, are kept in the tables as `*_DL`. p_perm = TP53-label permutation
over lines (10,000).

| Test | Estimate (HK 95% CI) | p (HK) / p_perm | Against 16 placebo predictors | Against 66 placebo outcomes |
|---|---|---|---|---|
| **Primary: P53 score (21 targets), WT - alt** | +0.041 log RR (ratio 1.042, 0.971 to 1.118) | 0.24 / 0.15 | 81.25th percentile, empirical p 0.35 | 85th percentile, p 0.28 |
| P53 score, WT - alt, DMSO / raisers / p53 activators / other drugs | -0.001 / -0.006 / +0.010 / +0.047 | p_perm 0.98 / 0.78 / 0.74 / 0.12 | 62.5th / 56.25th / 68.75th / 81.25th | |
| P53 score, WT - alt, within-well paired | +0.056 | p_perm 0.054 | | |
| Primary 5 targets summed (MDM2, CDKN1A, FDXR, ZMAT3, DDB2), WT - alt | +0.043 (-0.044 to 0.128) | 0.31 / 0.22 | 75th, p 0.41 | 85th, p 0.25 |
| MDM2 / CDKN1A, WT - alt | +0.058 / -0.042 | 0.23 / 0.32; p_perm 0.16 / 0.29 | 87.5th / 25th | |
| **Per doubling of a cell's TRIM72**, P53 score, WT - alt | 1.023 per doubling (0.988 to 1.059); half of alpha technical 1.036 (0.982 to 1.093) | | | |
| P53 score within groups: WT / altered | RR 1.091 (1.019 to 1.169) / 1.048 (1.027 to 1.069) | 0.015 / < 1e-4 | 87.5th / 68.75th percentile (placebo median RR 1.033 / 1.034): generic | |
| ATF3 within groups: WT / altered | RR 1.379 / 1.348 | < 1e-6 / < 1e-10 | 100th / 100th (placebo median 1.08): specific to TRIM72 | 100th |
| ATF3, WT - alt | +0.022 | 0.64 / 0.66 | 75th | |
| PMAIP1 within groups / WT - alt | RR 1.244 / 1.224; +0.016 | p_perm 0.71 | 87.5th (not distinguishable from placebos) | |
| TP53 mRNA within groups / WT - alt | RR 1.211 / 1.141; +0.060 | 0.15 / 0.095 | 100th / 100th | |
| NF-kB (NFKBIA+TNFAIP3+CXCL8), WT - alt | +0.007 | 0.88 / 0.89 | 43.75th | |
| Ferroptosis (SLC7A11+GPX4+CHAC1), WT - alt | -0.026 | 0.52 / 0.51 | 18.75th | |
| SLC7A11 alone (p53-repressed; MG53->p53 predicts + in WT), WT - alt | -0.063 (-0.177 to 0.051) | 0.27 / 0.30 | 18.75th | |
| Apoptosis (BAX+BBC3+PMAIP1), WT - alt | +0.011 | 0.74 / 0.76 | 56.25th | |

**What the test can exclude (per doubling).** TRIM72 counts are overdispersed given depth: pooled alpha 2.8 (WT)
and 3.3 (altered). Under a gamma-Poisson model, detected cells then carry about 4x the true TRIM72 rate of undetected
cells (log2 ratio 2.0 / 2.2). Dividing by that, the P53 score changes by 1.023 per doubling of TRIM72 more in WT than
in altered lines (HK 95% CI 0.988 to 1.059; the earlier DL CI was 0.994 to 1.052). A WT-specific fall of more than
1.2% per doubling is excluded, and so is a rise of more than 5.9%. Changes of 5.0% per doubling would be detected
with 80% power. Alpha includes any technical overdispersion that depth does not explain, which would overstate the
true-rate contrast and make the bounds too tight. If half of alpha is technical (alpha 1.4 / 1.7, log2 ratio
1.3 / 1.5), the CI is 0.982 to 1.093: a fall of more than 1.8% and a rise of more than 9.3% are excluded (80% power
at 7.8%). Per class (CI per doubling):

| Class | Alpha as estimated | Half of alpha technical |
|---|---|---|
| DMSO | 0.955 to 1.049 | 0.930 to 1.078 |
| TRIM72 raisers | 0.955 to 1.051 | 0.926 to 1.090 |
| p53 activators | 0.972 to 1.040 | 0.958 to 1.062 |
| other drugs | 0.988 to 1.056 | 0.982 to 1.086 |

**Secondary: single p53 targets lean the other way.** The P53 score is dominated by MDM2 and CDKN1A, which do not
move. Among the 24 unique p53 outcomes (P53 score, primary-5 sum, TP53 and the 21 score members), the WT - alt
estimate is positive for 21 (SPATA18 has no estimate: data in one altered line only; CDKN1A and ACER2 are negative),
and for 9 it is above all 16 placebo predictors: BBC3, DDB2, PHLDA3, PLK3, RPS27L, TP53I3, TP53INP1, XPC, ZMAT3. The
empirical p cannot go below 1/17.

| Target | WT - alt (log RR) | p (HK) | p_perm | BH q (on p_perm) | Placebo-calibrated p | With ATF3 as a covariate (`adjusted_ATF3/`) |
|---|---|---|---|---|---|---|
| XPC | +0.154 | 0.0019 | 1e-4 | 0.010 | 0.008 | +0.131, HK p 0.004, p_perm 3e-4, q 0.029 |
| DDB2 | +0.155 | 0.0041 | 0.0014 | 0.074 | 0.016 | +0.121, HK p 0.015, p_perm 0.006 |
| ZMAT3 | +0.115 | 0.013 | 0.0085 | 0.33 | 0.083 | +0.092, HK p 0.033, p_perm 0.032 |

This is more p53-target mRNA in TRIM72-detected cells of WT lines. That is the direction of p53 activation in the
same stressed cells, and the opposite of an MG53-degrades-p53 effect. Adjusting for per-cell ATF3 removes part of the
P53-score lean (+0.041 to +0.019, HK p 0.56, p_perm 0.48) but not the XPC/DDB2 lean. Treat it as a hypothesis: it is
secondary, and those genes are low per cell.

**TP53 functional status as the grouping** (`p53_functional_status_contrasts.csv`; not pre-specified). The gene
panel calls each line's p53 responsive or unresponsive from its measured response to p53 activators. Lines with
fitted groups: 11 responsive (all TP53-WT), 27 unresponsive (26 altered, 1 WT), 9 uncertain and left out (5 WT,
4 altered). The continuous p53 responsiveness of all 47 lines is used as well (meta-regression). Each contrast is
also computed for the 16 placebo predictors.

| Outcome (all wells) | Responsive - unresponsive (log RR, HK 95% CI) | p (HK) / p_perm | Placebo percentile, empirical p | Slope per log2 unit of responsiveness, p_perm |
|---|---|---|---|---|
| P53 score | +0.082 (-0.011 to 0.174) | 0.078 / 0.010 | 100th, 0.059 | +0.089, 0.017 (100th, 0.12) |
| P53 score: DMSO / raisers / p53 activators / other drugs | +0.037 / +0.000 / +0.026 / +0.093 | p_perm 0.26 / 0.98 / 0.36 / 0.006 | 75th / 68.75th / 87.5th / 100th | |
| Primary 5 summed | +0.094 (-0.016 to 0.204) | 0.087 / 0.013 | 100th, 0.059 | +0.096, 0.027 |
| MDM2 / CDKN1A | +0.110 / -0.023 | p_perm 0.012 / 0.58 | 100th / 50th | |
| XPC / DDB2 / ZMAT3 | +0.199 / +0.224 / +0.141 | p_perm 2e-4 / 1e-4 / 0.008 | 100th / 100th / 100th | |
| TP53 mRNA / ATF3 | +0.055 / +0.063 | p_perm 0.20 / 0.30 | 93.75th / 100th (empirical p 0.12 / 0.24) | |

The genotype contrast dilutes this: 6 of the 17 WT lines are not called responsive (5 uncertain, 1 unresponsive).
The direction is the same as the single-target lean above (TRIM72-detected cells carry more p53-target mRNA where
p53 works), so it does not support MG53 lowering p53 output. It is absent in the DMSO, TRIM72-raiser and
p53-activator wells, comes from the 1,201 'other drugs' wells, and is carried by p53 targets that are low per cell. With per-cell ATF3 as a
covariate (`adjusted_ATF3/`) the P53 score difference falls to +0.055 (HK p 0.17, p_perm 0.053; still above all
placebos), while XPC (+0.170) and DDB2 (+0.184) stay (p_perm 2e-4 / 1e-4).

**Ambient negative controls** (`ambient_negative_controls.csv`, `ambient_control_lines.csv`). In 13 CDKN2A-deleted
lines (7 WT, 6 altered) CDKN2A reads are 5-17% of the ambient expectation (soup = the other lines of the same
wells), and in 6 MTAP-null lines MTAP reads are 7-16% of it, so every such read is ambient RNA. 'Gene detected' for
these genes is then a predictor that can only reflect soup capture (0.97% / 3.5% of cells; TRIM72 1.2% in the same
lines). Same model, same groups, fitted only in those lines, read against the placebo predictors in the same lines.

| Predictor, lines | P53 score: WT / altered / WT - alt (HK p) | TRIM72, same lines: WT - alt (HK p) | Placebos there: median, range of WT - alt | ATF3, all lines: soup / TRIM72 (percentile) |
|---|---|---|---|---|
| CDKN2A detected, 7 WT + 6 altered CDKN2A-deleted lines | -0.054 / +0.032 / -0.086 (0.004) | -0.024 (0.62) | -0.034, -0.175 to +0.062 | +0.039 (47th) / +0.298 (100th) |
| MTAP detected, 2 WT + 4 altered MTAP-null lines | -0.035 / +0.049 / -0.084 (0.029) | -0.069 (0.55) | +0.036, -0.261 to +0.222 | +0.039 (47th) / +0.274 (93rd) |

Pure ambient capture lands inside the placebo range (20th and 40th percentile for the WT - alt P53 score), but with
6-13 lines it can reach a nominal HK p of 0.004. TRIM72's own WT - alt in these lines is near zero. Its ATF3 and TP53
associations are far above what soup gives, so they are not ambient artefacts.

**Sensitivity** (`sensitivity_subsets.csv`; not pre-specified, each read against the placebo predictors in the same
wells):

| Subset | P53 score, WT - alt | p (HK) / p_perm | Placebo percentile, empirical p |
|---|---|---|---|
| Plate 13 left out | +0.040 | 0.25 / 0.16 | 81.25th, 0.35 |
| High-TRIM72 plates (1-3, 14) | +0.045 | 0.22 / 0.13 | 87.5th, 0.24 |
| Low-TRIM72 plates (4-13) | +0.025 | 0.53 / 0.45 | 75th, 0.53 |
| D1's idarubicin 5 uM wells | +0.038 | 0.13 / 0.22 | 81.25th, 0.29 |
| Raisers that activate p53 (12 drug-doses, 15 wells) | -0.058 | 0.007 / 0.012 | 18.75th, 0.29 |
| Raisers that do not activate p53 (9 drug-doses, 24 wells) | +0.044 | 0.27 / 0.18 | 81.25th, 0.59 |
| Cap 0: all fitted groups + 374 sampled cap-dropped groups with all their cells | +0.040 | 0.25 / 0.15 | 81.25th, 0.35 |
| Cap 0: the sampled cap-dropped groups alone (359 groups fitted for the P53 score) | -0.060 | 0.48 / 0.37 | 25th, 0.29 |
| Cap 0 for every sampled at-risk group (replacing its cap-2,000 fit) | +0.039 | 0.25 / 0.16 | 81.25th, 0.35 |
| Sampled at-risk groups fitted at both caps: cap 0 / cap 2,000 | +0.097 / +0.128 | 0.11 / 0.034; 0.056 / 0.010 | 100th / 100th, 0.059 / 0.059 |

- **D1's idarubicin wells:** RR 1.020 (WT) and 0.982 (altered), against D1's 1.0195 and 0.9832.
- **Raisers that activate p53:** RR WT 0.958 vs altered 1.015, the hypothesis direction. But placebo predictors give
  a median of -0.019 in the same wells, which puts TRIM72 at the 18.75th percentile (empirical p 0.29). MDM2 there:
  -0.071, p_perm 0.083, 12.5th percentile. Not specific to TRIM72.
- **Raisers that do not activate p53** (the subset left out of the earlier write-up; 16 of its 24 wells are
  adagrasib 0.05 uM, the others auranofin, dinaciclib 0.5 and 5 uM, panobinostat, cyclosporin A, filgotinib, TAK-901
  and calcium lactate): P53 score +0.044, the opposite sign, p_perm 0.18. MDM2 there +0.125,
  p_perm 0.041, above all placebos but empirical p 0.18. Together with the row above, the raisers do not show one
  consistent WT-specific direction.
- **Cap 0** (the 2,000-cell cap drops 1,914 qualifying groups that keep < 5 TRIM72-detected cells; a random 20% of the
  6,088 groups at risk of that, 1,194 groups and 4.3M cells, were also fitted with all their cells, and 374 of them
  are cap-dropped groups): putting the dropped groups back does not move the primary estimate (+0.041 to +0.040).
  The at-risk groups (large groups with few TRIM72-detected cells) lean more positive at either cap, the same lean as
  above, and the cap itself changes little (+0.128 subsampled, +0.097 with all cells).

**Limits.**
- mRNA only; associations only.
- Most TRIM72-detected cells have 1 UMI, and part of TRIM72's reads may be readthrough from FUS.
- Between-line heterogeneity is large (I2 0.98-0.99 for the P53 score), so inference is at the line level: HK
  t-intervals over 17 / 30 lines and the line-label permutation. Normal p-values over groups would be far too small.
- Few lines per contrast: an ambient-only predictor reaches HK p 0.004 in 13 lines, so the placebo calibration, not
  a single p, decides what is specific to TRIM72.
- The per-cell panel has no PI3K-AKT, cell-cycle (CCND1, KIF11) or RAC1 read-outs.

## Design

| Element | Choice |
|---|---|
| Cells | All 3,388 files of `gene_panel/cells/*.parquet` (95,624,334 cells), streamed file by file, only the needed columns |
| Groups | (well, line) with >= 50 cells, >= 5 TRIM72-detected (>= 1 UMI) and >= 5 undetected cells, line expresses TRIM72 (atlas `expr_mask`), TP53 group known, not a failed well; after the subsample TRIM72 must still have >= 5 detected cells |
| Subsample | Uniform Bernoulli subsample to at most `--max-cells-per-group` cells (default 2,000, seeded per file). Uniform, not by TRIM72 status, so the placebo-predictor fits stay valid. Keeps 47.1M of the 60.0M cells in the 32,717 qualifying groups (809,067 of their 931,222 TRIM72-detected cells, 87%); 1,914 groups then fall below 5 TRIM72-detected cells, leaving 30,803 groups, 43.3M cells and 803,499 detected cells |
| Cap-0 sample | Groups with a binomial probability > 1e-6 of falling below 5 TRIM72-detected (or undetected) cells under the cap are 'at risk' (6,088); a seeded random 20% of them (`--cap0-frac`, 1,194 groups, 4.28M cells) is also fitted with all its cells in the same pass. Every cap-dropped group is in the at-risk set, so the sampled ones (374) are a simple random sample of the 1,914 dropped groups |
| Model per group | Quasi-Poisson GLM (IRLS; dispersion = Pearson chi2/df, floored at 1): counts ~ TRIM72 detected + log total UMI + log S-phase fraction + log G2M fraction, offset log total UMI. Same model as `downstream_p53.py` (d); the batched fit agrees with that scalar code to < 1e-7 |
| Outcomes | P53_SCORE (21 P53_ACTIVITY members summed), P53_PRIMARY5 (MDM2+CDKN1A+FDXR+ZMAT3+DDB2), the five primary targets, TP53, the other 16 members; screen modules of `mg53_p53/gene_modules.csv` (formerly `mg53_perturbation/assay_panel/panel.csv`) present in the per-cell panel (NF-kB, ferroptosis, apoptosis, ATF3, PMAIP1, DDIT3); 66 non-p53 panel genes (placebo outcomes) |
| Placebo predictors | 'gene X detected' for the 16 non-p53-linked, non-screen panel genes whose detection rate in the qualifying groups is within 1/3x-3x of TRIM72's (1.55%): ABCG2, NLRP3, AIM2, GSDMD, OSGIN1, SDF2L1, IL1B, AKR1B10, NAPEPLD, ABCB1, CDKN2B, AKR1C2, PSPH, HMOX1, GSDME, IRF7; same model, same groups, outcomes = all p53 and screen read-outs |
| Ambient negative controls | 'CDKN2A detected' in the CDKN2A-deleted lines and 'MTAP detected' in the MTAP-null lines (gene panel `p53_functional_status.csv` flags) whose reads of the gene are < 0.3x the ambient expectation (`--ambient-max-ratio`): 13 of 15 CDKN2A-deleted lines (HS-578T and NCI-H2122 express it) and 6 of 6 MTAP-null lines. Same model and groups, fitted only in those lines |
| Pooling | Two-stage DerSimonian-Laird random effects: over the wells of each (line, well class), then over lines within a TP53 group (17 WT / 30 altered lines with data). Lines are the units, because the same lines repeat in every well. Stage-2 SEs are Hartung-Knapp (variance factor floored at 1, t on lines - 1 df); the DL normal SEs are kept as `*_DL` |
| WT minus altered | Difference of the two line-level means, HK SE and Welch-Satterthwaite df. p_perm reshuffles the TP53 labels of the lines (10,000 permutations). A within-well paired version (WT groups minus altered groups of the same well, then over wells) has its own line-label permutation p |
| TP53 functional status | The gene panel's functional call (responsive vs unresponsive; uncertain left out) in place of the genotype, same estimator and label permutation; and the slope of the line estimates on the continuous p53 responsiveness (random-effects meta-regression, HK SE on k - 2 df, 2,000 permutations). TRIM72 and every placebo predictor |
| Well classes | DMSO (28 wells); TRIM72 raisers (gene panel call 'up', 21 drug-doses, 39 wells); p53 activators (P53_ACTIVITY z >= 3, FDR < 0.10, not raisers; 53 wells); other drugs (1,201 wells); all wells (1,321) |
| Per doubling | Negative-binomial overdispersion of TRIM72 counts given depth (moment estimator, pooled per class x TP53 group). Under a gamma-Poisson model it gives the true TRIM72 rate in detected vs undetected cells; the log rate ratio and its HK CI are divided by the log2 of that ratio. Also with alpha halved (half of the overdispersion technical) |
| Sensitivity | Plate 13 left out; high-TRIM72 plates (1-3, 14) vs low (4-13); raisers with vs without p53 activation; D1's two idarubicin 5 uM wells; the cap-0 rows; all with the placebo-predictor null. Separately, the whole analysis with per-cell ATF3 as an extra covariate (`adjusted_ATF3/`) |

Modules of `gene_modules.csv` that the per-cell panel lacks (PI3K-AKT/FAK: TXNIP, IRS1, PTK2; cell cycle: CCND1, KIF11;
RAC1, MCL1, FOS, HEXIM1, GDF15) cannot be tested in single cells here.

## Running it

```bash
python3 mg53_p53/single_cell_all/single_cell_all.py --data ~/Tahoe-100M          # tables in ./tables, cache in ./cache
MG53_OUT=/some/folder python3 mg53_p53/single_cell_all/single_cell_all.py      # tables in /some/folder/tables
MG53_OUT=$PWD/mg53_p53/single_cell_all/adjusted_ATF3 \
    python3 mg53_p53/single_cell_all/single_cell_all.py --adjust ATF3          # the ATF3-adjusted sensitivity run
```

- Options: `--max-cells-per-group` (0 = all cells), `--cap0-frac 0.2`, `--ambient-max-ratio 0.3`, `--workers 3`
  (fitting processes), `--readers 2` (parquet threads), `--perm 10000`, `--perm-paired 1000`, `--limit-files N`
  (quick test), `--recompute` (ignore the cache), `--modules` (default `mg53_p53/gene_modules.csv`; the script stops
  with a clear message if it is missing).
- The per-group fits are cached in `cache/fits.parquet`. A rerun with the same parameters (including the resolved
  data folder and its total cell count) rebuilds every table from the cache in ~1-2 min.
- Reads only `gene_panel/` (cells, `well_line.parquet`, `sample_map.csv`, `results/`) and `atlas/effects/`. Writes nothing
  under the data folder; it refuses to.
- Python: numpy, pandas, scipy, plus pyarrow to read parquet (clear error if missing). psutil, if installed, is used
  for memory reporting only; otherwise `resource` (absent on Windows).

**Run here** (4 CPUs, 15 GB; another agent's `two_way` run was active at the same time; default settings, from
scratch, cache and tables deleted first):

| Run | Wall time | Peak memory | Read from disk |
|---|---|---|---|
| Full run (stream + fit + tables), cold page cache (container just restarted) | 782 s (13.0 min): 697 s stream and fit, ~55 s meta-analysis and tables | 3.54 GB PSS for the whole process tree (main process 2.93 GB RSS, each of 3 workers <= 0.55 GB RSS) | 2.06 GB |
| `--adjust ATF3`, right after | 795 s (726 s stream and fit) | 3.72 GB PSS (main 3.16 GB RSS) | 1.64 GB (the parallel run had pushed most cell files out of the page cache) |
| Table rebuild from the cache | 50 s | 2.3 GB | ~0 |

Both full runs read most of the cell files from disk, so they are effectively cold. The stream is CPU-bound in the
fitting workers, not I/O-bound: ~2 GB of parquet is a small part of the ~700 s. The main run's tables were
byte-identical to an earlier run of the same code under a different machine load (fits sorted before caching,
per-group fits sorted by sample, line and outcome), and so was the rebuild from the cache. The .csv.gz tables are
written without a gzip timestamp, so a rerun gives byte-identical files.

- Coverage (`checks.csv`): every file was read (95,624,334 cells), every qualifying group's cell count matched
  `well_line.parquet`, no plate was fitted before all its cells were read, and no cell arrived after its plate was
  fitted (both 0).
- Memory is bounded by holding at most two plates' cells for fitting (largest: plate 2, 5.94M cells at the default
  cap including its cap-0 groups' cells). `--cap0-frac 0` drops the 4.3M cap-0 cells; `--max-cells-per-group 1000`
  lowered the peak to ~1.5-2 GB in a run before the cap-0 sample existed, with 59% instead of 87% of
  TRIM72-detected cells.

## Files

`single_cell_all.py` (the step), `run_log.txt` (log of the run in this folder), `tables/` (see
`tables/README_tables.txt`), `cache/` (per-group fits), `adjusted_ATF3/` (the same tables with per-cell ATF3 as an
extra covariate), `verify/` (the verifier's scripts and outputs; `verify/before/` = the tables before the fixes,
identical to commit 48669fd).
