# MDM2 and MG53, level by level

Regenerate every number here with:

```
python3 mg53_p53/findings/mdm2_mg53_levels.py --results ~/Tahoe-100M/mg53_p53
```

## Why this table exists, and what MDM2 is

MDM2 came out of the per-gene screen marked **"down with MG53"** — one of only eight of the 29 canonical p53
effectors to reach the calibrated threshold, and the only one of the p53 program's top three genes to reach
it at all. That is worth a table of its own, for two reasons.

The first is that MDM2 is not a reading of p53's output. It sits on **both** sides of p53: p53 induces MDM2
transcriptionally, and the MDM2 protein then ubiquitinates p53 and sends it for degradation. So it is a p53
**regulator** whose mRNA happens also to be p53-responsive. If MG53 moved MDM2, the interesting reading would
run toward p53, not away from it — which makes it the one gene in the set where an association could speak to
what regulates p53 rather than to what p53 does.

The second is measurement. MDM2 is the **best-measured gene in the entire analysis**: 185.8 CPM, detected in
all 50 lines, moved up by 96 of the 98 reference compounds. MG53 sits at 5.89 CPM with 12.4% of profiles at
zero. Whatever MDM2 shows or fails to show is not a detection problem on MDM2's side.

| | MG53 (TRIM72) | MDM2 | CDKN1A (contrast gene) |
|---|---|---|---|
| Median level across lines | 5.89 CPM | **185.8 CPM** | 56.4 CPM |
| Lines where detected | 50 of 50, 12.4% of profiles zero | 50 of 50 | 47 of 50 |
| Role | the exposure | p53 regulator (p53 induces it; its protein degrades p53) | p53 effector (arrest) |
| In the data-defined p53 program | not a member | induction arm, **rank 3** of 180 | induction arm, rank 29 |
| Moved up by | — | 96 of 98 compounds | 85 of 98 |
| Fold change under p53 activators, WT lines | — | **1.255x**, the largest of all 195 program genes | 1.117x |
| Baseline, TP53-WT vs TP53-altered lines | 1.08x, p 0.77 | **3.07x, p 3.4e-12** | 1.96x, p 5.8e-4 |
| Fold-change range over the 1,132 exposures | 0.31x to 12.24x | 0.46x to 2.11x | 0.50x to 2.15x |
| Split-half reliability | 0.289 | — | — |

**That last row but one is the positive control for everything below.** The same per-line measurement that
finds MDM2 running 3.07x higher in TP53-wild-type lines than in TP53-altered ones — the p53 → MDM2 feedback
loop, textbook, p = 3.4e-12 — finds nothing at all from MG53 (1.08x, p 0.77). A null from MG53 in this data is
not a measurement failure. It is a null.

## What "level" means here, because two different things are called that

| | What it is | Where it lives |
|---|---|---|
| **LEVEL** | how much mRNA is present | pooled CPM per exposure; each line's untreated baseline; `TRIM72_level` |
| **CHANGE** | how far the gene moved under the drug | corrected log2 fold change: `TRIM72_z`, `r2`, fold change |

They do not behave the same way, so every table below says which one it is binning. There are four
resolutions at which both genes exist in a run's output:

| Unit | n | What varies |
|---|---|---|
| 1. baseline across cell lines | 48 lines | each line's own untreated level of both genes |
| 2. drug-dose, lines pooled | 1,132 exposures | what each exposure does to both genes |
| 3. cell line x drug-dose | 861 cells | 18 MG53-raising exposures x 50 lines |
| 4. the genome-wide screen | 53,084 cells | reported from the run, not recomputed here |

Unit 4 is reported rather than recomputed because per-gene **per-line** values are not in the export — only
MG53 and the program score are resolved per line for all exposures. Unit 3 exists because one step of the
pipeline did export per-line values for five named genes, MDM2 among them, over a selected set of 18
exposures.

## Table 1 — the headline: MG53 change against MDM2 change

Deciles of MG53's fold change over the 1,132 exposures, lines pooled. This is the direct answer to "compare
different levels of MG53 and MDM2".

| MG53 decile | n | MG53 fold change (median) | **MDM2 fold change (mean, 95% CI)** | CDKN1A fold change |
|---|---|---|---|---|
| 1 (lowest) | 114 | 0.65x | 1.002 (0.988–1.016) | 0.947 |
| 2 | 113 | 0.79x | 1.008 (0.996–1.021) | 0.988 |
| 3 | 113 | 0.87x | 1.012 (1.001–1.024) | 1.013 |
| 4 | 113 | 0.93x | 1.001 (0.991–1.011) | 0.995 |
| 5 | 113 | 0.98x | 1.013 (0.999–1.026) | 0.999 |
| 6 | 113 | 1.03x | 1.005 (0.993–1.016) | 0.997 |
| 7 | 113 | 1.09x | 1.001 (0.992–1.011) | 1.011 |
| 8 | 113 | 1.16x | 0.984 (0.968–1.002) | 1.016 |
| 9 | 113 | 1.28x | 0.989 (0.977–1.000) | 1.035 |
| 10 (highest) | 114 | 1.56x | 1.017 (0.982–1.052) | 1.080 |

**It is a flat line.** Across a 2.4x span of MG53, MDM2 moves by under 2% in either direction, no bin's
interval excludes 1.00 by any margin, the trend across bins is -0.15 by rank, and the top decile sits
*above* the bottom one. The contrast gene in the last column does what a gene tracking MG53 looks like:
0.947 to 1.080, climbing with the bins.

The overall Spearman is **-0.092** (p 0.002, compound-bootstrap CI -0.156 to -0.022), which reproduces the
run's own figure exactly. But the Pearson correlation on the same pairs is **+0.003**. When the two disagree
that completely, the rank statistic is being set by the bulk and the Pearson by the tail, and neither is
describing a line — it is describing a cloud with a slight tilt in the middle and the opposite tilt at the
end. Adjusting for how much the whole transcriptome moved (`atlas_n_sig_genes`, cell counts, S and G2M phase,
UMI per cell) takes the Spearman to **-0.022**, and the compound-clustered bootstrap p to 0.45.

## Table 2 — MG53 level against MDM2 level, and why the big number here is an artefact

| MG53 decile | n | MG53 level (CPM, median) | MDM2 level (CPM, mean ± SE) | CDKN1A level (CPM) |
|---|---|---|---|---|
| 1 (lowest) | 114 | 0.80 | 328.9 ± 4.4 | 65.3 |
| 2 | 113 | 1.02 | 337.2 ± 5.1 | 63.0 |
| 3 | 113 | 1.31 | 332.0 ± 6.0 | 62.4 |
| 4 | 113 | 1.61 | 311.4 ± 4.6 | 63.5 |
| 5 | 113 | 2.20 | 284.9 ± 5.5 | 67.5 |
| 6 | 113 | 2.85 | 276.9 ± 5.9 | 70.2 |
| 7 | 113 | 3.78 | 271.6 ± 6.5 | 69.0 |
| 8 | 113 | 7.98 | 258.7 ± 6.1 | 69.4 |
| 9 | 113 | 11.84 | 252.1 ± 6.7 | 78.2 |
| 10 (highest) | 114 | 16.40 | 261.8 ± 6.6 | 82.5 |

Read on its own this looks like the strongest result in the whole set: Spearman **-0.614**, p 1e-22, MDM2
falling from 329 to 252 CPM as MG53 rises 20x. **It is a plate batch effect, in full.** MG53 carries a 3.12
log2 plate-batch gap — the largest of all 16,656 genes — and each exposure sits on one or two of 14 plates:

| | Spearman |
|---|---|
| All 1,132 exposures together | **-0.614** |
| Between plates (the 14 plate medians) | **-0.763** |
| Within plate, pooled (plate medians removed) | **+0.074** |
| Mean of the 13 per-plate correlations | **+0.087**, negative on only 2 plates |

MG53's plate medians run from 0.86 to 14.05 CPM — a 16x spread with no drug in it — and MDM2's run the other
way, 343 down to 227. Comparing exposures that sit on the same plate, the relationship is *weakly positive*.
There is no level-to-level relationship between these two genes; there is a plate.

(The one thing this is **not** is library collapse. MG53's CPM is flat against UMI per cell, rho -0.013, so
the plate effect is not simply the denominator moving.)

## Table 3 — each line's own untreated level, across 48 cell lines

| Group | MG53 baseline band | n | MG53 baseline (log2, median) | MDM2 baseline (mean, 95% CI) |
|---|---|---|---|---|
| all lines | lowest quarter | 12 | -1.57 | +0.21 (-0.46, +0.87) |
| all lines | second | 12 | -0.64 | +0.09 (-0.45, +0.63) |
| all lines | third | 12 | +0.53 | +0.62 (+0.09, +1.15) |
| all lines | highest quarter | 12 | +1.36 | +0.41 (-0.12, +0.94) |
| TP53-WT | lowest third | 6 | -1.15 | +1.42 (+0.95, +1.90) |
| TP53-WT | middle third | 5 | +0.35 | +1.18 (+0.77, +1.59) |
| TP53-WT | highest third | 6 | +0.98 | +1.54 (+1.18, +1.91) |
| TP53-altered | lowest third | 11 | -1.33 | -0.34 (-0.72, +0.04) |
| TP53-altered | middle third | 10 | +0.09 | -0.45 (-0.77, -0.12) |
| TP53-altered | highest third | 10 | +1.36 | +0.04 (-0.39, +0.48) |

Nothing, in any group: r = +0.08 over all 48 lines (p 0.57), -0.10 in the 17 wild-type lines, +0.15 in the
31 altered ones. A cell line that carries more MG53 does not carry more or less MDM2.

What the same column *does* show is the 3.07x wild-type / altered split — visible here as every WT band
sitting near +1.2 to +1.5 and every altered band near -0.4 to 0.0, with no overlap between the groups and no
trend inside either one. MDM2's baseline is set by whether the line has working p53. It is not set by MG53.

## Table 4 — within one exposure, across cell lines: the one contrast that shows something

Hold the drug and dose fixed and compare the lines against each other. Among the lines given the same
exposure, do the ones that raise MG53 most show the least MDM2? This is the only contrast in the document
where the answer is not flatly no, so it gets the most careful null.

The unit is 861 line x exposure cells — the 18 MG53-raising exposures for which the pipeline exported
per-line values for MDM2 — and each line is compared only against the other lines on the same exposure.
Binned first, five bins per group:

| Group | MG53 quintile within exposure | n | MG53 change (median) | MDM2 change (mean, 95% CI) |
|---|---|---|---|---|
| all lines | 1 (lowest) | 169 | -1.54 | -0.002 (-0.102, +0.097) |
| all lines | 3 | 169 | +0.03 | -0.004 (-0.097, +0.088) |
| all lines | 5 (highest) | 169 | +1.44 | -0.013 (-0.122, +0.097) |
| TP53-WT | 1 (lowest) | 61 | -1.38 | +0.169 (-0.046, +0.385) |
| TP53-WT | 2 | 61 | -0.32 | +0.390 (+0.193, +0.587) |
| TP53-WT | 3 | 61 | +0.22 | +0.361 (+0.156, +0.566) |
| TP53-WT | 4 | 61 | +0.82 | +0.147 (-0.045, +0.340) |
| TP53-WT | 5 (highest) | 61 | +1.71 | -0.049 (-0.249, +0.150) |
| TP53-altered | 1 (lowest) | 108 | -1.66 | -0.040 (-0.148, +0.068) |
| TP53-altered | 3 | 108 | -0.13 | -0.216 (-0.292, -0.140) |
| TP53-altered | 5 (highest) | 108 | +1.32 | -0.034 (-0.149, +0.080) |

Pooled over all lines it is flat. In the 17 wild-type lines it does decline — +0.39 in the second bin down
to -0.05 in the top — though not from the first bin, and as a single slope that is **-0.060 (95% CI -0.139
to +0.019, compound-bootstrap p 0.13)**: not significant. In the altered lines the pattern is
non-monotonic, most negative in the middle.

The same data by the pipeline's own estimator says something stronger, so both are given.

The statistic is a Spearman per exposure over the lines in that group, averaged over the 18 exposures — the
pipeline's own estimator. Two nulls, and the difference between them is the point:

- **per-exposure shuffle**: MDM2 permuted independently inside each exposure. Holds the exposure set, the
  line count and both marginals fixed — but it also destroys the fact that the *same* 17 or 30 lines appear
  in all 18 exposures. If a line simply tends to run high in MG53 and low in MDM2 as a standing property,
  the real statistic keeps that and this null throws it away, so its p is too small. **This is the null the
  pipeline reports.**
- **line-label shuffle**: one permutation of the cell-line labels, applied to every exposure at once. Each
  line's whole MDM2 profile travels together and is attached to a different line's MG53 profile. Line-level
  structure survives in the null, so what gets tested is the claim actually being made.

| Group | Contrast | mean rho over 18 exposures | negative in | p, per-exposure shuffle | **p, line-label shuffle** |
|---|---|---|---|---|---|
| all lines | MG53 change → MDM2 | -0.017 | 11 of 18 | 0.64 | 0.71 |
| **TP53-WT (17)** | **MG53 change → MDM2** | **-0.162** | **11 of 18** | **0.005** | **0.036** |
| TP53-altered (30) | MG53 change → MDM2 | -0.047 | 12 of 18 | 0.29 | 0.45 |
| TP53-WT | MG53 *level* → MDM2 | -0.033 | 9 of 18 | 0.55 | 0.69 |
| all lines | *CDKN1A* → MG53 change | +0.135 | 4 of 18 | <0.001 | 0.008 |
| TP53-WT | *CDKN1A* → MG53 change | +0.163 | 2 of 18 | 0.006 | 0.059 |
| TP53-altered | *CDKN1A* → MG53 change | +0.122 | 6 of 18 | 0.012 | 0.086 |

**The stricter null costs the result most of its significance but does not kill it**: p 0.005 becomes 0.036,
and the null's spread widens by 34% (SD 0.058 to 0.078) — which is exactly the inflation the weaker null was
hiding.

Then the accounting, which is where it ends. Nine contrasts were tested; at p = 0.036 and rank 2 this is
**q ≈ 0.16** by Benjamini-Hochberg, so it does not clear 0.1. It sits in the smallest arm available,
**17 lines**. Its magnitude is estimator-dependent: the same data as a pooled within-exposure residual slope
gives -0.060 with a compound-bootstrap p of 0.13. The per-exposure correlations run from **-0.65 to +0.31**,
so the mean of -0.162 is an average over exposures that disagree about the sign. And the contrast does not
reproduce in the TP53-altered arm, while the genome-wide screen — with 47 lines and all 1,132 exposures
rather than 18 — puts the wild-type-minus-altered difference at -0.0006, p 0.89.

So: a hint, in the one place it could show up, that does not survive its own accounting. Worth recording,
not worth believing yet. If anything in this document is followed up, this is the row to follow up.

## Table 5 — the twelve biggest raisers and the twelve biggest lowerers, named

Binning hides what the extremes do, and the extremes are where a real effect would be easiest to see. These
are the exposures themselves.

| End | Drug | µM | MG53 fold | **MDM2 fold** | CDKN1A fold | p53 activity z |
|---|---|---|---|---|---|---|
| raised | Idarubicin | 5 | 12.24x | 1.06 | 1.08 | 18.1 |
| raised | Homoharringtonine | 5 | 10.26x | 1.38 | 1.92 | 20.6 |
| raised | Auranofin | 5 | 6.56x | **0.66** | 2.15 | **-7.8** |
| raised | Homoharringtonine | 0.5 | 5.87x | 1.77 | 1.90 | 17.4 |
| raised | Dinaciclib | 5 | 5.57x | **0.66** | 1.07 | 0.6 |
| raised | Epirubicin | 5 | 4.52x | 0.91 | 1.05 | 8.1 |
| raised | Dinaciclib | 0.5 | 3.70x | 0.81 | 1.14 | 1.6 |
| raised | Dinaciclib | 0.05 | 3.82x | 1.15 | 1.11 | 7.0 |
| raised | Harringtonine | 5 | 3.60x | 1.27 | 1.44 | 6.2 |
| raised | Doxorubicin | 5 | 2.99x | 0.92 | 1.00 | 10.0 |
| raised | Panobinostat | 5 | 2.70x | **0.48** | 0.73 | 1.1 |
| raised | Mitoxantrone | 5 | 2.05x | 1.20 | 1.37 | 11.3 |
| lowered | NG25 | 5 | 0.31x | 1.08 | 0.50 | -1.5 |
| lowered | Ponatinib | 5 | 0.39x | 1.01 | 0.69 | 3.9 |
| lowered | Trametinib (solvate) | 0.05 | 0.48x | 1.06 | 0.90 | 1.1 |
| lowered | Cabozantinib | 5 | 0.50x | 0.98 | 0.83 | 0.6 |
| lowered | HI-TOPK-032 | 0.05 | 0.52x | 1.01 | 0.94 | -0.6 |
| lowered | Balsalazide | 0.05 | 0.54x | 1.08 | 1.01 | 0.0 |
| lowered | Infigratinib | 0.05 | 0.54x | 0.95 | 1.05 | 0.2 |
| lowered | Trametinib (solvate) | 5 | 0.55x | 1.02 | 1.00 | 1.6 |
| lowered | Anethole trithione | 5 | 0.61x | 1.03 | 0.97 | -0.1 |
| lowered | Trametinib | 0.05 | 0.64x | 0.99 | 0.90 | 0.8 |
| lowered | Radotinib | 5 | 0.65x | 0.98 | 0.81 | 1.3 |
| lowered | Neratinib | 5 | 0.65x | 0.99 | 0.93 | -0.3 |

Two things come straight off this table.

**Driving MG53 down does nothing to MDM2.** Every one of the twelve biggest lowerers — MG53 cut by a third to
two thirds — leaves MDM2 between 0.95 and 1.08. Twelve independent chances for a negative relationship to
show itself as MDM2 rising, and it never does.

**Among the raisers, MDM2 follows p53 activity, not MG53.** MDM2 goes *up* where p53 output is high
(homoharringtonine, z 17–21, MDM2 1.38x and 1.77x; mitoxantrone z 11.3, 1.20x; harringtonine z 6.2, 1.27x)
and *down* where it is not (auranofin, z **-7.8**, MDM2 0.66x; panobinostat z 1.1, 0.48x; dinaciclib at 5 µM,
z 0.6, 0.66x). MG53 is raised 2.0x to 12.2x throughout, in no particular relation to either. The gene is
doing exactly what a p53-regulated transcript should do, and MG53 is not the thing it is tracking.

## Table 6 — single cells: MDM2 in the cells that have MG53 against the cells that do not

This is the best-controlled comparison in the data, and the most literal reading of "different levels of
MG53": inside **one cell line, one well**, split the cells by whether MG53 was detected in them and ask how
much MDM2 each group has. Cell line, drug, dose, plate and well are all held fixed by construction. The run
fits a quasi-Poisson GLM per line (offset log UMIs; covariates log UMIs, S-phase and G2M fractions, well
indicator), pools lines by random effects, and — crucially — puts **every non-p53 panel gene through the same
fit**, giving 78 to 85 control genes to place MDM2 against.

Percentile is MDM2's rank among that well set's control genes, with the number of controls in brackets.

| Well set | TP53 | lines | **MDM2 rate ratio** | p | percentile among controls | depth-matched ratio | p |
|---|---|---|---|---|---|---|---|
| DMSO, plates 6+14 | WT | 17 | 1.016 | 0.82 | 34th (85) | 1.063 | 0.67 |
| DMSO, plates 6+14 | altered | 30 | **0.915** | **0.005** | **3.6th (84)** | 0.881 | 0.047 |
| DMSO, plate 14 | WT | 17 | 0.944 | 0.49 | 10th (80) | 0.878 | 0.19 |
| DMSO, plate 6 | WT | 16 | 1.207 | 0.17 | 71st (83) | 0.974 | 0.78 |
| Idarubicin 5 µM, both wells | WT | 16 | 1.043 | 0.18 | 65th (80) | 1.059 | 0.49 |
| Idarubicin 5 µM, both wells | altered | 30 | 1.003 | 0.93 | 50th (80) | 0.949 | 0.10 |
| **Idarubicin 5 µM, plate 14** | WT | 14 | **1.150** | **3e-6** | **84th (79)** | 1.191 | 0.025 |
| **Idarubicin 5 µM, plate 6** | WT | 15 | **0.941** | 0.20 | 15th (78) | 0.961 | 0.30 |

**Read the last two rows together.** They are the *same drug at the same dose in the same wild-type lines*,
run on two plates. Plate 14 says MDM2 is **15% higher** in MG53-positive cells, at p = 3x10⁻⁶ and the 84th
percentile of its control genes. Plate 6 says **6% lower**. Pooling them gives +4.3%, p 0.18, the 65th
percentile — nothing. One of those two plates would, on its own, have been a publishable-looking result in
either direction.

That is the clearest statement available of what MG53 measurements in this data are worth at this
resolution, and it is why nothing in this document rests on a single well set.

The one row that is consistent across its own replicates is the untreated **TP53-altered** lines: MDM2 runs
8.5% lower in MG53-positive cells (p 0.005, 3.6th percentile of 84 controls, and 0.881 with p 0.047 when the
comparison is restricted to cells of matched sequencing depth). The wild-type arm of the same comparison is
1.016, p 0.82, at the 34th percentile; the wild-type-minus-altered difference is +0.105 ± 0.077, p 0.17. So
once again the only thing that replicates sits in the lines where p53 cannot act on MDM2 at all.

A caveat that belongs with this table specifically: MG53 is detected in a minority of cells at about 5 UMIs,
so "MG53-detected" partly means "more deeply sequenced cell". The UMI offset, the UMI covariate and the
depth-stratified version are what stand against that, and the adjusted and unadjusted per-line medians do
differ (for DMSO plate 14 WT, -0.210 adjusted against -0.122 unadjusted), so the adjustment is doing work.

## Table 7 — the genome-wide screen's own slope on MDM2

This is the one estimate with per-line resolution across all exposures: cell-line and drug-dose fixed
effects, 53,084 line x exposure cells, 47 lines. Reported from `c_screen_genes`, not recomputed.

| Arm / covariate set | slope (log2 MDM2 per doubling of MG53) | change in MDM2, measured MG53 | change in MDM2, true MG53 | p |
|---|---|---|---|---|
| gw (primary) | -0.00500 | **-0.35%** | -1.19% | 0.016 |
| gw_all | -0.00501 | -0.35% | -1.19% | 0.015 |
| gw_pc | -0.00600 | -0.41% | -1.43% | 0.002 |
| curated_cycle | -0.00478 | -0.33% | -1.14% | 0.022 |
| no covariates | -0.00500 | -0.35% | -1.19% | 0.018 |
| gw_rt (readthrough-corrected) | -0.00501 | -0.35% | -1.19% | 0.006 |
| **TP53-WT lines only (17)** | -0.00539 | -0.37% | -1.28% | **0.21** |
| **TP53-altered lines only (30)** | -0.00476 | -0.33% | -1.13% | **0.016** |
| WT minus altered | -0.00063 | -0.04% | -0.15% | 0.89 |

Three readings, in order of importance.

**The sign is robust and the size is tiny.** Every covariate set lands between -0.0048 and -0.0060,
including the readthrough-corrected one — so this is not spillover from the FUS / PYCARD-AS1 transcription
running into the TRIM72 locus. But a doubling of measured MG53 buys **-0.35%** of MDM2; dividing by MG53's
0.289 split-half reliability to express it per doubling of *true* MG53 gives **-1.19%**. MDM2's own range
across exposures is 0.46x to 2.11x. This slope is not a player in that range.

**The slope is the same size in lines that cannot induce MDM2 from p53.** b_WT = -0.0054, b_altered =
-0.0048, difference -0.0006 (p 0.89). In the 30 TP53-altered lines p53 cannot drive MDM2's transcription at
all — that is exactly the 3.07x baseline gap in Table 0 — and yet the slope there is as large as in the
wild-type lines, and is the arm carrying the significance (p 0.016 against 0.21). **A p53-mediated effect
cannot behave like that.** Whatever this slope is, it is not running through p53.

**It would not survive on its own.** Its t is -2.51. To clear q < 0.1 as the only significant gene among the
16,643 tested, it would need |slope| >= 0.0102 — twice what it has. It clears BH at q 0.069 (0.031 by the
exposure-shuffle null) only because a large mass of genes clears with it, and the run's own calibration finds
that mass **4.44x inflated**. This was the basis of the "down with MG53" verdict in the per-gene table, and
it should be read as a verdict about a gene set, not a certificate about MDM2.

### Why MDM2 cleared the threshold when 21 of the 29 effectors did not

Not because its effect is large. Of the eight effectors with a verdict, MDM2's slope is the **smallest**:

| Gene | \|slope\| | SE | median CPM | verdict |
|---|---|---|---|---|
| **MDM2** | **0.0050** | **0.00199** | **185.8** | down |
| DDB2 | 0.0075 | 0.00314 | 54.3 | down |
| PMAIP1 | 0.0081 | 0.00324 | 69.4 | up |
| AEN | 0.0090 | 0.00373 | 17.0 | up |
| TP53I3 | 0.0100 | 0.00423 | 5.5 | down |
| CDKN1A | 0.0104 | 0.00351 | 56.4 | up |
| ACER2 | 0.0136 | 0.00595 | 13.7 | up |
| BTG2 | 0.0153 | 0.00678 | 8.5 | up |

MDM2's slope is a third of BTG2's. What it has instead is the **second-tightest standard error of all 29
effectors** (0.00199; only CCNG1's 0.00176 is smaller), because at 185.8 CPM it is measured better than
anything else in the panel. MDM2 is in this table because it is precise, not because it moved.

## Is MDM2 unusual? The all-gene placebo

The only way MDM2's own correlation means anything is to ask where it falls among all genes measured the same
way. Each of 4,642 genes was correlated against MG53 across the same 1,132 exposures:

| Quantity | MDM2 | percentile among genes | all-gene median | all-gene 5th–95th | verdict |
|---|---|---|---|---|---|
| CHANGE (corrected log2), Spearman | -0.080 | **26th** | +0.053 | -0.286 to +0.388 | unremarkable |
| LEVEL (pooled CPM), Spearman | -0.614 | **9th** | +0.253 | -0.681 to +0.823 | unremarkable |
| the run's own co-regulation r, raw | +0.005 | **36th** | +0.124 | -0.388 to +0.492 | unremarkable |
| the run's own co-regulation r, 3 PCs removed | +0.034 | **60th** | -0.008 | -0.252 to +0.293 | unremarkable |
| *CDKN1A, same, CHANGE* | +0.290 | *88th* | | | *in the tail* |
| *CDKN1A, same, co-regulation raw* | +0.418 | *89th* | | | *in the tail* |

**MDM2 is an ordinary gene with respect to MG53 at every one of these.** Not at the 1st percentile, not at
the 99th — the 26th, the 9th, the 36th, the 60th. Even the -0.614 CPM correlation of Table 2 is only the 9th
percentile: roughly one gene in eleven is at least that negative, which is what a distribution dominated by
plate structure looks like. The contrast gene sits at the 88th and 89th, which is what a gene that genuinely
tracks MG53 looks like in the same frame.

## Joint distribution

Counts in each MG53 x MDM2 quintile cell, 1,132 exposures, against the 45.3 expected per cell if the two were
independent (chi-square p = 0.042):

| MG53 quintile | MDM2 q1 | q2 | q3 | q4 | q5 |
|---|---|---|---|---|---|
| 1 (lowest MG53) | 37 | 42 | 41 | 53 | 54 |
| 2 | 40 | 41 | 55 | 41 | 49 |
| 3 | 40 | 46 | 44 | 53 | 43 |
| 4 | 51 | 52 | 48 | 45 | 30 |
| 5 (highest MG53) | 59 | 45 | 38 | 34 | **51** |

A faint anti-diagonal tilt — the lowest MG53 cells lean to high MDM2, the fourth row leans low — but the
corner that should be emptiest if MDM2 fell with MG53 holds 51 against 45 expected. The p of 0.042 is on 16
degrees of freedom and is carried as much by that non-monotonicity as by any trend.

## What this adds up to

Every contrast in the document, with what it came to:

| Resolution | Contrast | Result | Verdict |
|---|---|---|---|
| 48 lines, untreated | MG53 baseline vs MDM2 baseline | r +0.08, p 0.57 (WT -0.10, altered +0.15) | nothing |
| 1,132 exposures | MG53 change deciles vs MDM2 | every bin within 2% of 1.00, no trend | nothing |
| 1,132 exposures | MG53 change vs MDM2 change | rho -0.092, Pearson +0.003, -0.022 after activity | 26th percentile of genes |
| 1,132 exposures | MG53 CPM vs MDM2 CPM | -0.614 overall, **+0.074 within plate** | plate artefact |
| the 12 biggest lowerers | MDM2 | 0.95 to 1.08, every one | nothing |
| the 12 biggest raisers | MDM2 | 0.48 to 1.77, following p53 activity | not following MG53 |
| 861 line x exposure | within exposure, TP53-WT | mean rho -0.162, p 0.036, **q ~0.16** | a hint, unconfirmed |
| 861 line x exposure | within exposure, TP53-altered | -0.047, p 0.45 | nothing |
| single cells | untreated, TP53-WT | rate ratio 1.016, 34th percentile of 85 controls | nothing |
| single cells | untreated, TP53-altered | 0.915, p 0.005, 3.6th percentile | replicates, wrong arm for p53 |
| single cells | idarubicin, TP53-WT | **+15% on plate 14, -6% on plate 6** | irreproducible |
| 53,084 cells | screen, common slope | -0.35% per doubling, same in all 6 covariate sets | smallest of the eight; under the lone-discovery bar |
| 53,084 cells | screen, WT vs altered | -0.0054 vs -0.0048, difference p 0.89 | not p53-mediated |

**There is no relationship between the level of MG53 and the level of MDM2 in this data.** Not across cell
lines untreated, not across exposures, not between absolute amounts, and not in the cells of a single well.
The screen's "down with MG53" verdict is real as a statement about where MDM2 falls in a genome-wide ranking
and is the smallest effect among the genes that cleared, carried by MDM2's precision rather than its size;
set against the all-gene distribution it is the 26th percentile.

**And nothing about it looks p53-mediated**, which is what the question was. The screen's slope is the same
size in 30 lines whose p53 cannot touch MDM2 as in 17 where it can. Partialling out p53 output makes the
drug-dose correlation *more* negative, not less. The negative tilt lives in the exposures that do **not**
activate p53 (rho -0.119, p 1e-13) and is absent in the 50 that do (+0.048, p 0.37). The one single-cell
result that replicates sits in the p53-altered arm. If MG53 were acting on p53 through MDM2, none of that
would look like this.

**What the data are good for, and what they are not.** MDM2 is measured well enough to recover its own
biology at high confidence — the 3.07x wild-type/altered baseline split, p 3.4e-12, is the p53-MDM2 feedback
loop sitting right there in the table. The limit is on the MG53 side: 5.89 CPM, 12.4% zeros, split-half
reliability 0.289, the largest plate gap of 16,656 genes, and two wells of the same exposure disagreeing by
21 percentage points at single-cell resolution. Tahoe also has no MG53 perturbation, no protein measurement,
and one time point. An absence here constrains the association; it cannot rule out a protein-level or
post-transcriptional link, which is where TRIM72's known biology mostly lives.

**The one thing worth following up** is the Table 4 row: within an exposure, among TP53-wild-type lines, the
lines that raise MG53 most showing the least MDM2 (mean rho -0.162, p 0.036 under the cell-line-label
shuffle, q ~0.16 over the nine contrasts tested). It needs the two things this run cannot give it — per-line
MDM2 values across all 1,132 exposures instead of 18, which an `export/all_genes` per-line addition would
provide, and more than 17 wild-type lines.

## The files

| File | Contents |
|---|---|
| `tables/mdm2_mg53_bins.csv` | every binned table above, long form: unit, group, which variable was binned, bin bounds, n, mean / median / SD / SE / CI of the outcome in each bin, and the across-bin trend |
| `tables/mdm2_mg53_models.csv` | one row per contrast: slope, SE, t, p, Pearson, Spearman, and the compound-clustered bootstrap interval and p |
| `tables/mdm2_mg53_cpm_by_plate.csv` | the LEVEL comparison split by plate: per-plate medians of both genes, the within-plate correlation on each plate, and the between / within decomposition |
| `tables/mdm2_mg53_single_cell.csv` | the single-cell rate ratios with their control-gene percentiles and the depth-matched version |
| `tables/mdm2_mg53_per_exposure_rho.csv` | the within-exposure across-lines correlations, with both permutation nulls |
| `tables/mdm2_mg53_screen.csv` | the genome-wide screen's slope on MDM2 in every covariate set and arm, with the lone-discovery threshold |
| `tables/mdm2_mg53_allgene_null.csv` | MDM2's percentile among all genes correlated against MG53 the same way |
| `tables/mdm2_mg53_allgene_null_cpm_pooled.csv`, `..._r2_median_lines_mean.csv` | the full per-gene distributions those percentiles come from, 4,642 genes each |
| `tables/mdm2_mg53_extremes.csv` | the named exposures at both ends of MG53 |
| `tables/mdm2_mg53_crosstab.csv` | the joint quintile counts with expected counts and the chi-square |
| `tables/mdm2_mg53_context.csv` | what each gene is: level, detection, program membership, response range |

Which columns are circular: MDM2's program membership, its rank, and its p53-activation fold change were all
selected using the TP53 genotype labels, so they cannot be used to argue about p53-specificity — they are
descriptive only. Nothing in the MG53 columns used those labels.
