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

- **Size of what is excluded:** a WT-specific *decrease* of more than ~0.6% in p53-target counts per doubling of a
  cell's TRIM72, and an increase of more than ~5%. This bound depends on an overdispersion model, see the caveats.
- **What does move with TRIM72:** TRIM72-detected cells carry more p53-target mRNA in both TP53 groups, but placebo
  genes do the same (generic). They carry more ATF3 than placebo genes do, equally in WT and altered lines (a shared
  stress state, not p53).
- **Secondary signal, opposite direction:** a few single p53 targets of the DNA-repair arm (XPC, DDB2, ZMAT3) lean
  *higher* in TRIM72-detected WT cells. That is the opposite of an MG53-lowers-p53 effect, and it is not significant
  for the pre-specified score.

All numbers below are for all wells pooled unless a class is named. Rate ratio (RR) = counts per UMI in
TRIM72-detected vs undetected cells of the same well and line, adjusted for depth and cell cycle. "WT - alt" is the
difference of the log RRs between TP53-WT (17 lines) and TP53-altered (30 lines).

| Test | Estimate (95% CI) | p (line-label permutation) | Against 16 placebo predictors | Against 66 placebo outcomes |
|---|---|---|---|---|
| **Primary: P53 score (21 targets), WT - alt** | +0.041 log RR (ratio 1.042, 0.983 to 1.104) | 0.15 | 81st percentile, empirical p 0.35 | 85th percentile, p 0.28 |
| P53 score, WT - alt, DMSO / raisers / p53 activators / other drugs | -0.001 / -0.006 / +0.010 / +0.047 | 0.98 / 0.78 / 0.74 / 0.12 | 63rd / 50th / 81st / 81st | |
| P53 score, WT - alt, within-well paired | +0.056 | 0.054 | | |
| Primary 5 targets summed (MDM2, CDKN1A, FDXR, ZMAT3, DDB2), WT - alt | +0.043 (-0.028 to 0.113) | 0.22 | 75th, p 0.41 | 85th, p 0.25 |
| MDM2 / CDKN1A, WT - alt | +0.058 / -0.042 | 0.16 / 0.29 | 88th / 25th | |
| **Per doubling of a cell's TRIM72**, P53 score, WT - alt | 1.023 per doubling (0.994 to 1.052) | | | |
| P53 score within groups: WT / altered | RR 1.091 / 1.048 | (normal p 0.002 / < 1e-4) | 88th / 69th percentile (placebo median RR 1.033 / 1.034): generic | |
| ATF3 within groups: WT / altered | RR 1.379 / 1.348 | | 100th / 100th (placebo median 1.08): specific to TRIM72 | 100th |
| ATF3, WT - alt | +0.022 | 0.66 | | |
| PMAIP1 within groups / WT - alt | RR 1.244 / 1.224; +0.016 | 0.71 | 88th (not distinguishable from placebos) | |
| TP53 mRNA within groups / WT - alt | RR 1.211 / 1.141; +0.060 | 0.095 | 100th / 100th | |
| NF-kB (NFKBIA+TNFAIP3+CXCL8), WT - alt | +0.007 | 0.89 | 44th | |
| Ferroptosis (SLC7A11+GPX4+CHAC1), WT - alt | -0.026 | 0.51 | 19th | |
| SLC7A11 alone (p53-repressed; MG53->p53 predicts + in WT), WT - alt | -0.063 (-0.163 to 0.037) | 0.30 | 19th | |
| Apoptosis (BAX+BBC3+PMAIP1), WT - alt | +0.011 | 0.76 | 56th | |

**What the test can exclude (per doubling).** TRIM72 counts are overdispersed given depth: pooled alpha 2.8 (WT)
and 3.3 (altered). Under a gamma-Poisson model, detected cells then carry about 4x the true TRIM72 rate of undetected
cells (log2 ratio 2.0 / 2.2). Dividing by that, the P53 score changes by 1.023 per doubling of TRIM72 more in WT than
in altered lines (95% CI 0.994 to 1.052). A WT-specific fall of more than 0.6% per doubling is excluded, and so is a
rise of more than 5.2%. Changes of 4.1% per doubling would be detected with 80% power. Per class (CI per doubling):

| Class | CI per doubling |
|---|---|
| DMSO | 0.962 to 1.041 |
| TRIM72 raisers | 0.959 to 1.047 |
| p53 activators | 0.975 to 1.037 |
| other drugs | 0.994 to 1.050 |

Alpha includes any technical overdispersion that depth does not explain. That would overstate the true-rate contrast
and make these bounds too tight.

**Secondary: single p53 targets lean the other way.** The P53 score is dominated by MDM2 and CDKN1A, which do not
move. Among the 29 p53 outcomes, the WT - alt estimate is positive for 25, and for 9 it is above all 16 placebo
predictors: BBC3, DDB2, PHLDA3, PLK3, RPS27L, TP53I3, TP53INP1, XPC, ZMAT3. The empirical p cannot go below 1/17.

| Target | WT - alt (log RR) | p_perm | BH q | Placebo-calibrated p | With ATF3 as a covariate (`adjusted_ATF3/`) |
|---|---|---|---|---|---|
| XPC | +0.154 | 1e-4 | 0.010 | 0.006 | +0.131, p_perm 3e-4, q 0.029 |
| DDB2 | +0.155 | 0.0014 | 0.074 | 0.013 | +0.121, p_perm 0.006 |
| ZMAT3 | +0.115 | 0.0085 | 0.33 | 0.083 | +0.092, p_perm 0.032 |

This is more p53-target mRNA in TRIM72-detected cells of WT lines. That is the direction of p53 activation in the
same stressed cells, and the opposite of an MG53-degrades-p53 effect. Adjusting for per-cell ATF3 removes part of the
P53-score lean (+0.041 to +0.019, p_perm 0.48) but not the XPC/DDB2 lean. Treat it as a hypothesis: it is
secondary, and those genes are low per cell.

**Sensitivity** (`sensitivity_subsets.csv`; not pre-specified, each read against the placebo predictors in the same
wells):

| Subset | P53 score, WT - alt | p_perm |
|---|---|---|
| Plate 13 left out | +0.040 | 0.16 |
| High-TRIM72 plates (1-3, 14) | +0.045 | 0.13 |
| Low-TRIM72 plates (4-13) | +0.025 | 0.45 |
| D1's idarubicin 5 uM wells | +0.038 | 0.22 |
| Raisers that activate p53 (12 drug-doses, 15 wells) | -0.058 | 0.012 |

- **D1's idarubicin wells:** RR 1.020 (WT) and 0.982 (altered), against D1's 1.0195 and 0.9832.
- **Raisers that activate p53:** RR WT 0.958 vs altered 1.015, the hypothesis direction. But placebo predictors give
  a median of -0.019 in the same wells, which puts TRIM72 at the 19th percentile (empirical p 0.29). MDM2 there:
  -0.071, p_perm 0.083, 12th percentile. Not specific to TRIM72.

**Limits.**
- mRNA only; associations only.
- Most TRIM72-detected cells have 1 UMI, and part of TRIM72's reads may be readthrough from FUS.
- Between-line heterogeneity is large (I2 ~0.98 for the P53 score), so inference is at the line level and needs the
  permutation p-values; normal p-values over groups would be far too small.
- The per-cell panel has no PI3K-AKT, cell-cycle (CCND1, KIF11) or RAC1 read-outs.

## Design

| Element | Choice |
|---|---|
| Cells | All 3,388 files of `gene_panel/cells/*.parquet` (95,624,334 cells), streamed file by file, only the needed columns |
| Groups | (well, line) with >= 50 cells, >= 5 TRIM72-detected (>= 1 UMI) and >= 5 undetected cells, line expresses TRIM72 (atlas `expr_mask`), TP53 group known, not a failed well; after the subsample TRIM72 must still have >= 5 detected cells |
| Subsample | Uniform Bernoulli subsample to at most `--max-cells-per-group` cells (default 2,000, seeded per file). Uniform, not by TRIM72 status, so the placebo-predictor fits stay valid. Keeps 47.1M of the 60.0M cells in the 32,717 qualifying groups (809,067 of their 931,222 TRIM72-detected cells, 87%); 1,914 groups then fall below 5 TRIM72-detected cells, leaving 30,803 groups, 43.3M cells and 803,499 detected cells |
| Model per group | Quasi-Poisson GLM (IRLS; dispersion = Pearson chi2/df, floored at 1): counts ~ TRIM72 detected + log total UMI + log S-phase fraction + log G2M fraction, offset log total UMI. Same model as `downstream_p53.py` (d); the batched fit agrees with that scalar code to < 1e-7 |
| Outcomes | P53_SCORE (21 P53_ACTIVITY members summed), P53_PRIMARY5 (MDM2+CDKN1A+FDXR+ZMAT3+DDB2), the five primary targets, TP53, the other 16 members; screen modules of `mg53_perturbation/assay_panel/panel.csv` present in the per-cell panel (NF-kB, ferroptosis, apoptosis, ATF3, PMAIP1, DDIT3); 66 non-p53 panel genes (placebo outcomes) |
| Placebo predictors | 'gene X detected' for the 16 non-p53-linked, non-screen panel genes whose detection rate in the qualifying groups is within 1/3x-3x of TRIM72's (1.55%): ABCG2, NLRP3, AIM2, GSDMD, OSGIN1, SDF2L1, IL1B, AKR1B10, NAPEPLD, ABCB1, CDKN2B, AKR1C2, PSPH, HMOX1, GSDME, IRF7; same model, same groups, outcomes = all p53 and screen read-outs |
| Pooling | Two-stage DerSimonian-Laird random effects: over the wells of each (line, well class), then over lines within a TP53 group (17 WT / 30 altered lines with data). Lines are the units, because the same lines repeat in every well |
| WT minus altered | Difference of the two line-level means. p_perm reshuffles the TP53 labels of the lines (10,000 permutations). A within-well paired version (WT groups minus altered groups of the same well, then over wells) has its own line-label permutation p |
| Well classes | DMSO (28 wells); TRIM72 raisers (gene panel call 'up', 21 drug-doses, 39 wells); p53 activators (P53_ACTIVITY z >= 3, FDR < 0.10, not raisers; 53 wells); other drugs (1,201 wells); all wells (1,321) |
| Per doubling | Negative-binomial overdispersion of TRIM72 counts given depth (moment estimator, pooled per class x TP53 group). Under a gamma-Poisson model it gives the true TRIM72 rate in detected vs undetected cells; the log rate ratio and its CI are divided by the log2 of that ratio |
| Sensitivity | Plate 13 left out; high-TRIM72 plates (1-3, 14) vs low (4-13); raisers with vs without p53 activation; D1's two idarubicin 5 uM wells; all with the placebo-predictor null. Separately, the whole analysis with per-cell ATF3 as an extra covariate (`adjusted_ATF3/`) |

Modules of `panel.csv` that the per-cell panel lacks (PI3K-AKT/FAK: TXNIP, IRS1, PTK2; cell cycle: CCND1, KIF11; RAC1,
MCL1, FOS, HEXIM1, GDF15) cannot be tested in single cells here.

## Running it

```bash
python3 mg53_p53/single_cell_all/single_cell_all.py --data ~/Tahoe-100M          # tables in ./tables, cache in ./cache
MG53_OUT=/some/folder python3 mg53_p53/single_cell_all/single_cell_all.py      # tables in /some/folder/tables
MG53_OUT=$PWD/mg53_p53/single_cell_all/adjusted_ATF3 \
    python3 mg53_p53/single_cell_all/single_cell_all.py --adjust ATF3          # the ATF3-adjusted sensitivity run
```

- Options: `--max-cells-per-group` (0 = all cells), `--workers 3` (fitting processes), `--readers 2` (parquet threads),
  `--perm 10000`, `--perm-paired 1000`, `--limit-files N` (quick test), `--recompute` (ignore the cache).
- The per-group fits are cached in `cache/fits.parquet`; a rerun with the same parameters rebuilds every table from the
  cache in ~1 min.
- Reads only `gene_panel/` (cells, `well_line.parquet`, `sample_map.csv`, `results/`) and `atlas/effects/`. Writes nothing
  under the data folder; it refuses to.
- Python: numpy, pandas, scipy, plus pyarrow to read parquet. statsmodels is not needed.

**Run here** (4 CPUs, 15 GB, another agent running at the same time; default settings):

| Run | Wall time | Peak memory |
|---|---|---|
| Full run (stream + fit) | 982 s (16.4 min), of which 930 s stream and fit | 3.43 GB PSS for the whole process tree (main process 2.99 GB RSS, each of 3 workers <= 0.66 GB RSS) |
| `--adjust ATF3` | 989 s | 3.37 GB PSS |
| Table rebuild from the cache | ~50 s | 2.3 GB |

- Coverage: every file was read (95,624,334 cells), and every qualifying group's cell count matched `well_line.parquet`.
- Memory is bounded by holding at most two plates' subsampled cells (largest plate 5.66M cells at the default cap).
  `--max-cells-per-group 1000` lowers the peak to ~1.5-2 GB and the run time to ~10 min, with 59% instead of 87% of
  TRIM72-detected cells.

## Files

`single_cell_all.py` (the step), `run_log.txt` (log of the run in this folder), `tables/` (see
`tables/README_tables.txt`), `cache/` (per-group fits), `adjusted_ATF3/` (the same tables with per-cell ATF3 as an
extra covariate).
