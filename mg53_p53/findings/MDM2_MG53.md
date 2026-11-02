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

The second is measurement. MDM2 is **well** measured — 185.8 CPM, detected in all 50 lines, moved up by 96 of
the 98 reference compounds — while MG53 sits at 5.89 CPM with 12.4% of profiles at zero. It is not the
best-measured gene in the data (185.8 CPM is 903rd of 16,643 genes by level, and among the 29 canonical
effectors TNFRSF10B is higher at 200.5 CPM); the point is only that nothing MDM2 shows or fails to show here
is a detection problem on MDM2's side.

| | MG53 (TRIM72) | MDM2 | CDKN1A (contrast gene) |
|---|---|---|---|
| Median level across lines | 5.89 CPM | 185.8 CPM (903rd of 16,643) | 56.4 CPM |
| Lines where detected | 50 of 50, 12.4% of profiles zero | 50 of 50 | 47 of 50 |
| Role | the exposure | p53 regulator (p53 induces it; its protein degrades p53) | p53 effector (arrest) |
| In the data-defined p53 program | not a member | induction arm, **rank 3** of 180 | induction arm, rank 29 |
| Moved up by | — | 96 of 98 compounds | 85 of 98 |
| Fold change under p53 activators, WT lines | — | **1.255x**, the largest of all 195 program genes | 1.117x |
| Baseline, TP53-WT vs TP53-altered lines | 1.08x, p 0.77 | **3.07x, p 3.4e-12** | 1.96x, p 5.8e-4 |
| Fold-change range over the 1,132 exposures | 0.31x to 12.24x | 0.46x to 2.11x | 0.50x to 2.15x |
| Split-half reliability | 0.289 to 0.705 by subset | — | — |

**That baseline row is the positive control for everything below**, with one limit stated up front. The
per-line baseline measurement finds MDM2 running 3.07x higher in TP53-wild-type lines than in TP53-altered
ones — the p53 → MDM2 feedback loop, textbook — and finds nothing from MG53. The exact comparisons, since
they are not identical: MDM2 is 17 WT against 33 altered lines, ratio of geometric means 3.07x, Welch
p 3.3e-12 (Mann-Whitney on the medians: 3.14x, p 1.8e-7); MG53 is 17 against 31 lines, 1.08x, Welch p 0.77
(Mann-Whitney median ratio 1.20x, p 0.78).

What that licenses is narrow but real: **MDM2's side of every null below is sound** — a gene whose 3x
biological signal this measurement recovers at p 1e-12 is not failing to show a comparable MG53 effect for
want of detection. What it does **not** license is any claim about MG53's reliability, which is separately
and poorly characterised (0.289 split-half, and the plate and replicate problems documented throughout). A
null here is a null about the *association*, limited by the exposure, not by the outcome.

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
| 3. cell line x drug-dose | **843** cells | 18 MG53-raising exposures x 50 lines |
| 4. the genome-wide screen | 53,084 cells | reported from the run, not recomputed here |
| 5. single cells in one well | up to 47 lines | MG53-detected against MG53-undetected cells |

Unit 3's n is 843, not the 900 rows of the source table: MDM2 is present in 861 of them and MG53's corrected
value in 843, so every MG53 → MDM2 contrast runs on the 843 where both exist (305 wild-type, 538 altered),
and the CDKN1A contrast on 789.

Unit 4 is reported rather than recomputed because per-gene **per-line** values are not in the export — only
MG53 and the program score are resolved per line for all exposures. Unit 3 exists because one step of the
pipeline did export per-line values for five named genes, MDM2 among them, over a selected set of 18
exposures.

## Table 1 — the headline: MG53 change against MDM2 change

Deciles of MG53's fold change over the 1,132 exposures, lines pooled. This is the direct answer to "compare
different levels of MG53 and MDM2".

Both means of MDM2's fold change are given because they are not the same number and the difference reaches
2 percentage points in the top bin. **Geometric** is 2^(mean log2), which is what a log-scale analysis
produces; **arithmetic** is the mean of the ratios.

| MG53 decile | n | MG53 fold change (median) | **MDM2, geometric (95% CI)** | **MDM2, arithmetic (95% CI)** | CDKN1A geometric |
|---|---|---|---|---|---|
| 1 (lowest) | 114 | 0.65x | 1.002 (0.988–1.016) | 1.005 (0.992–1.018) | 0.947 |
| 2 | 113 | 0.79x | 1.008 (0.996–1.021) | 1.010 | 0.988 |
| 3 | 113 | 0.87x | 1.012 (1.001–1.024) | 1.014 (1.002–1.026) | 1.013 |
| 4 | 113 | 0.93x | 1.001 (0.991–1.011) | 1.003 | 0.995 |
| 5 | 113 | 0.98x | 1.013 (0.999–1.026) | 1.016 (1.000–1.031) | 0.999 |
| 6 | 113 | 1.03x | 1.005 (0.993–1.016) | 1.007 | 0.997 |
| 7 | 113 | 1.09x | 1.001 (0.992–1.011) | 1.003 | 1.011 |
| 8 | 113 | 1.16x | 0.984 (0.968–1.002) | 0.988 (0.972–1.005) | 1.016 |
| 9 | 113 | 1.28x | 0.989 (0.977–1.000) | 0.991 (0.979–1.002) | 1.035 |
| 10 (highest) | 114 | 1.56x | 1.017 (0.982–1.052) | **1.035 (0.996–1.074)** | 1.080 |

**It is a flat line, with two hairline exceptions.** Across a 2.4x span of MG53, MDM2's geometric mean stays
within 2% of 1.00 and the trend across bins is -0.15 by rank, with the top decile sitting *above* the
bottom. Two intervals do exclude 1.00 by a hair — bin 3 at 1.001–1.024 (above) and bin 9 at 0.977–0.99996
(below) — and on the arithmetic scale bins 3 and 5 do. The top bin is +3.5% arithmetic rather than +1.7%
geometric, so "within 2%" is a statement about the geometric mean only. None of these is a trend; they are
what ten intervals look like when none of them means anything. The contrast gene in the last column shows
what tracking MG53 looks like: 0.947 to 1.080, climbing with the bins.

Correlations on the same 1,132 exposures, with each statistic's own p:

| Pair | Spearman | its p | Pearson | slope, compound-bootstrap CI |
|---|---|---|---|---|
| MG53 z x MDM2 z | **-0.092** | **0.0020** | +0.003 | -0.29 to +0.26 |
| MG53 log2 fold x MDM2 log2 fold (the table above) | -0.080 | 0.0074 | +0.006 | -0.046 to +0.048 |
| after adjusting for transcriptome-wide activity | -0.019 (partial) | — | +0.062 | -0.13 to +0.29 |

The -0.092 reproduces the run's own figure exactly, and its drug-bootstrap CI (-0.156 to -0.022, also the
run's) excludes zero. But the Pearson on the same pairs is **+0.003**, and this file's own compound bootstrap
of that Pearson spans **-0.209 to +0.213**. When rank and product-moment statistics disagree that completely,
neither is describing a line: it is a cloud with a slight tilt through the middle and the opposite tilt at
the end. Adjusting for how much the whole transcriptome moved (`atlas_n_sig_genes`, cell counts, S and G2M
phase, UMI per cell) takes the partial Spearman to **-0.019** and the bootstrap p on the slope to 0.45.

The bound this unit supports, rather than a bare "nothing": per doubling of measured MG53, MDM2 changes by
between **-3.2% and +3.4%** (95%, compound-clustered).

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

Read on its own this looks like the strongest result in the whole set: Spearman **-0.614**, its own
p **5e-118**, MDM2 falling from 329 to 252 CPM as MG53 rises 20x. **It is a plate batch effect, in full.**
MG53 carries a 3.12 log2 plate-batch gap — the largest of all 16,656 genes — and all but one exposure sits
on one or two of the 14 plates (1,030 on one, 101 on two; Adagrasib at 0.05 µM is on 13):

| | Spearman |
|---|---|
| All 1,132 exposures together | **-0.614** |
| Between plates (the 14 plate medians) | **-0.763** |
| Within plate, pooled (plate medians removed) | **+0.074** |
| Mean of the 13 per-plate correlations | **+0.087**, negative on only 2 plates |

MG53's plate medians run from 0.86 to 14.05 CPM — a 16x spread with no drug in it — and MDM2's run the other
way, 343 down to 227. Comparing exposures that sit on the same plate, the relationship is *weakly positive*.
There is no level-to-level relationship between these two genes; there is a plate.

Two conventions were checked because the decomposition depends on one. Assigning each exposure to the first
plate named leaves plate 6 holding a single exposure, so its "median" is one number. Dropping plate 6
entirely gives a between-plate Spearman of **-0.791**; counting every plate an exposure actually appears on
gives **-0.793** between plates and **+0.031** within. The sign of the conclusion is unchanged either way;
the magnitude of the within-plate figure is convention-dependent (+0.074 against +0.031) and small in both.

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

With 48 lines that is a weak bound and should be read as one: the 95% interval on r runs **-0.21 to +0.36**,
so this unit excludes only correlations above about 0.36 in size. It is the least informative of the five
units here, and it is included because it is the only one where neither gene has been touched by a drug.

What the same column *does* show is the 3.07x wild-type / altered split — visible here as every WT band
sitting near +1.2 to +1.5 and every altered band near -0.4 to 0.0, with no overlap between the groups and no
trend inside either one. MDM2's baseline is set by whether the line has working p53. It is not set by MG53.

## Table 4 — within one exposure, across cell lines: the one contrast that shows something

Hold the drug and dose fixed and compare the lines against each other. Among the lines given the same
exposure, do the ones that raise MG53 most show the least MDM2? This is the only contrast in the document
where the answer is not flatly no, so it gets the most careful null.

The unit is 843 line x exposure cells — the 18 MG53-raising exposures for which the pipeline exported
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

One caution on reading the column: it is MDM2 minus that exposure's mean *over all 50 lines*, so the
wild-type bands sit uniformly positive and the altered bands uniformly negative because of the 3.07x
baseline gap, not because of MG53. Compare bands within a genotype, never across.

### The same data without the exposure control, and why it is not reported as a result

Binning the per-line values **raw** — not removing each exposure's mean — gives by far the largest per-line
numbers in the run, and they look like a clean dose-response:

| Group | MG53 quintile (raw) | n | MG53 change (median) | MDM2 change (mean) | across-bin trend | top − bottom |
|---|---|---|---|---|---|---|
| TP53-WT | 1 → 5 | 61 each | -0.42 → +4.23 | **+0.971 → +0.009** | **-0.9** | **-0.96 log2 = 0.51x** |
| TP53-altered | 1 → 5 | ~108 each | -0.59 → +3.90 | +0.242 → +0.044 | -1.0 | -0.20 log2 |
| all lines | 1 → 5 | ~169 each | -0.57 → +3.95 | +0.459 → +0.031 | -0.9 | -0.43 log2 |

A monotone decline halving MDM2's induction across the wild-type range. It is not reported as a result
because the comparison is between **different exposures**: the drugs that raise MG53 most (translation
inhibitors, CDK inhibitors) are not the drugs that induce MDM2 most, and wild-type lines have far more MDM2
induction to lose. Removing each exposure's mean — comparing a line only against lines given the same drug
at the same dose — is what the binned table above does, and it collapses to flat.

### Does the slope differ by TP53 status? Yes raw, no within exposure

This is the test that decides whether this unit supports a p53 route. Model: MDM2 = a + b₁·MG53 + b₂·WT +
b₃·(MG53 × WT), cluster-robust on cell line, 49 lines.

| Outcome | Fit | n | b, altered | b, wild-type | **interaction (WT extra)** | t | **p** |
|---|---|---|---|---|---|---|---|
| MDM2 | raw | 843 | -0.036 | -0.214 | **-0.178 ± 0.038** | -4.71 | **2.4e-06** |
| MDM2 | **within exposure** | 843 | -0.016 | -0.060 | **-0.045 ± 0.049** | -0.92 | **0.36** |
| *CDKN1A* | *raw* | 789 | *+0.141* | *-0.071* | *-0.212 ± 0.044* | *-4.88* | *1.1e-06* |
| *CDKN1A* | *within exposure* | 789 | *+0.096* | *+0.100* | *+0.004 ± 0.066* | *+0.06* | *0.95* |

Fitted raw, MDM2's wild-type slope is **six times** the altered one at p 2×10⁻⁶ — exactly what p53
dependence would look like, and the strongest genotype signal anywhere in this document. Fitted within
exposure, it is gone (p 0.36).

The contrast gene settles which reading is right. CDKN1A's raw interaction is just as significant
(p 1×10⁻⁶) and in the *same* direction, with its slope **changing sign between arms** (+0.141 altered,
-0.071 wild-type) — and fitted within exposure its two arms land on top of each other, +0.096 and +0.100,
interaction p 0.95. No p53-mediated mechanism predicts a p53 effector's MG53 slope flipping sign in the
lines that have p53. Both raw interactions are tracking which exposures the lines sat in.

So this unit does not support a p53 route. But it is the one place where an uncontrolled reading would have
produced a strong positive result, and the difference between p 2×10⁻⁶ and p 0.36 is a single fixed effect.

So this unit does not support a p53 route. But it is the one place where an uncontrolled reading would have
produced a strong positive result, and the difference between p 2×10⁻⁶ and p 0.36 is a single fixed effect.

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
two thirds — leaves MDM2 between 0.95 and 1.08. Not twelve independent chances, though: three of the rows
are one compound at different doses (Trametinib, twice as the DMSO solvate), so there are **ten distinct
compounds**, and eight of the twelve are kinase inhibitors (MEK, BCR-ABL, MET, FGFR, HER2). One mechanism
class dominates the bottom of the MG53 range, which is a fact about the library rather than about MG53.

The ranking also has a seam worth knowing: this block is ordered by MG53's **z** while the column displayed
is **fold change**, so the two disagree about which exposures are extreme — ranked by fold change instead,
PF-06260933 at 5 µM (3.29x, MDM2 1.155) enters the raised block and Mitoxantrone leaves it. The CSV now
carries both orderings.

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
1.016, p 0.82, at the 34th percentile.

Two honest limits on reading that as p53-independence. The **arms are not statistically distinguishable**:
the wild-type-minus-altered difference is +0.105 ± 0.077, **p 0.17**, with 30 lines against 17 — the same
power asymmetry as the screen. And the two plate-level replicates behind the altered figure are 0.914
(p 0.031) and **0.961 (p 0.52)**, so one of the two carries it; while in the wild-type arm DMSO plate 14's
per-line median points the same way (-0.210) as the altered arm. The pattern is suggestive of a route that
does not need p53, not a demonstration of one.

A caveat that belongs with this table specifically: MG53 is detected in a minority of cells at about 5 UMIs,
so "MG53-detected" partly means "more deeply sequenced cell". The UMI offset, the UMI covariate and the
depth-stratified version are what stand against that, and the adjusted and unadjusted per-line medians do
differ (for DMSO plate 14 WT, -0.210 adjusted against -0.122 unadjusted), so the adjustment is doing work.

### The contrast gene in the same cells, and what the two of them together rule out

| Well set | TP53 | lines | **CDKN1A rate ratio** | p | percentile among controls | depth-matched | p |
|---|---|---|---|---|---|---|---|
| DMSO, plates 6+14 | WT | 17 | 1.114 | 0.068 | 69th (85) | 1.078 | 0.25 |
| DMSO, plates 6+14 | altered | 27 | **1.208** | **4e-5** | 77th (84) | 1.155 | **0.003** |
| Idarubicin 5 µM, both wells | WT | 14 | 1.019 | 0.68 | 59th (80) | 0.961 | 0.54 |
| Idarubicin 5 µM, both wells | altered | 26 | 1.005 | 0.92 | 50th (80) | 1.003 | 0.86 |

In untreated cells, the MG53-positive cells carry **more CDKN1A and less MDM2** than their neighbours in the
same well: +20.8% and -8.5% in the altered lines, both outside the control-gene distribution, both holding
when depth is matched. The same sign split appears at the drug-dose unit (CDKN1A rho +0.29, MDM2 -0.08) and
in the genome-wide screen (+0.0104 against -0.0050). Three independent resolutions agreeing on the split
means it is a real feature of the data rather than noise.

It also argues against the p53 route rather than for it. CDKN1A and MDM2 are both p53-induced; under p53
they move **together**. Finding them moving apart — and doing so most clearly in the lines where p53 is
disabled — points at whatever distinguishes an MG53-positive cell from its neighbours (cell-cycle position,
stress state, arrest) rather than at p53 arbitrating between them.

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
running into the TRIM72 locus. A doubling of measured MG53 buys **-0.35%** of MDM2, with a 95% interval of
-0.61% to -0.08% (line-clustered) or -0.51% to -0.18% (drug-clustered). MDM2's own range across exposures is
0.46x to 2.11x. This slope is not a player in that range.

The "per doubling of **true** MG53" column needs a range, not a number. Dividing by a reliability assumes
classical measurement error, and the run reports split-half reliability for MG53 under several subsets:
0.289 for the primary specification, but 0.425, 0.586, 0.610 and 0.705 for the active, p53-responsive and
MG53-moving subsets. The sibling `MG53_p53_TABLES.md` already flags that the 0.610 variant "would halve the
de-attenuation", and it does:

| reliability used | per doubling of true MG53 | 95% interval |
|---|---|---|
| 0.289 (primary, i_all) | **-1.19%** | -2.11% to -0.26% |
| 0.425 (active, plates 3/13 excluded) | -0.81% | — |
| 0.610 (active exposures) | **-0.57%** | -1.01% to -0.12% |
| 0.705 (MG53-moving exposures) | -0.49% | — |

So the true-MG53 effect is somewhere around **-0.5% to -1.2%** per doubling. The earlier version of this
table gave -1.19% alone, which is the subset that maximises the correction. (The correction itself is right:
0.289 is already the Spearman-Brown full-data reliability — raw split-half 0.169, 2r/(1+r) = 0.289 — not a
half-reliability, so dividing once is correct and in the right direction.)

**The point estimates are the same size in both genotype arms, but this test cannot carry much weight.**
b_WT = -0.0054, b_altered = -0.0048, difference -0.0006. The honest version is the interval, not the p: the
**95% CI on the difference runs -0.0100 to +0.0087**, which spans a difference twice the size of the whole
common slope in either direction, and b_WT's own CI is **-0.0140 to +0.0032**, including zero and including
2.9x b_altered. Against a difference the size of a fully p53-mediated effect (-0.0054) this test has about
**21% power**; against -0.010, 58%. So p 0.89 here is mostly an absence of power.

What can be said is weaker and still useful: the significance in this model sits in the **altered** arm
(p 0.016 against 0.21 in wild-type), the arm where p53 drives MDM2 least — and the altered lines' MDM2
induction is damped, not abolished (the baseline gap is 3.07x, finite, and these lines retain roughly 5% of
the wild-type p53 response). This is **consistent with** a route that does not run through p53, and it is
corroborated by the two tests above that do have power — the within-exposure per-line interaction (p 0.36,
with the contrast gene's arms landing on top of each other) and the p53-activation split, where the tilt
lives in the exposures that do *not* activate p53. On its own, though, the WT-versus-altered comparison in
this screen does not exclude a p53-mediated effect, and an earlier version of this document claimed it did.

**It would not survive on its own — on one of the two standard errors the run supplies.** Its t is -2.51
against the line-clustered SE of 0.00199. To clear q < 0.1 as the only significant gene among the 16,642
tested it would need |slope| >= 0.0102, **2.0x** what it has. But the run also supplies a **drug-clustered**
SE of 0.00122, and on that one t is **-4.09, p 1.7e-04**, and the bar is 0.0063 — only **1.25x** its slope.
The earlier version of this section quoted only the first, which is the one that makes MDM2 look weaker.

Either way the BH verdict is a statement about a gene set: it clears q 0.069 (0.031 by the exposure-shuffle
null) because a large mass of genes clears with it, and the run's own calibration finds that mass **4.44x
inflated** on the test-statistic scale. Deflating MDM2's own t by √4.44 gives t = -1.19, p ≈ 0.24. That is
the most pessimistic reading available and it is worth stating, because it means the "down with MG53" verdict
in the per-gene table should be read as a ranking, not as a certificate about this gene.

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

## Is MDM2 unusual? Two reference families, and the difference between them matters

The only way MDM2's own correlation means anything is to ask where it falls among other genes measured the
same way. There are two candidate families here and **they are not equivalent — an earlier version of this
section used the wrong one and called it "all genes"**:

- **The 16,642 tested genes.** Selected for nothing. This is the honest reference family. The run supplies
  its own co-regulation correlation of every tested gene against MG53 across drug-doses, raw and with three
  principal components removed.
- **The 4,642 exported downstream genes.** *Not* a sample of genes. **4,500 of them are in that export
  because the genome-wide screen had already called them significant against MG53 at q < 0.1** — and MDM2 is
  itself one of the 4,500 (its export record reads "Tahoe p53 program P; genome_wide screen: common slope
  q < 0.1"). The remaining 142 are p53-program members selected with the TP53 labels. A percentile here is a
  rank **inside the discovery set**, in a family shifted toward MG53 association by construction — which is
  why its median Spearman is +0.25 on level and +0.05 on change rather than 0, and why only 36% of its genes
  are negative.

| Family | Quantity | MDM2 | percentile | family median | family 5th–95th |
|---|---|---|---|---|---|
| **16,642 tested, unselected** | co-regulation r across exposures, raw | +0.005 | **36th** | +0.124 | -0.388 to +0.492 |
| **16,642 tested, unselected** | the same, 3 PCs removed | +0.034 | **60th** | -0.008 | -0.252 to +0.293 |
| 4,642 discovery set | CHANGE (corrected log2), Spearman | -0.080 | 26th | +0.053 | -0.286 to +0.388 |
| 4,642 discovery set | LEVEL (pooled CPM), Spearman | -0.614 | 9th | +0.253 | -0.681 to +0.823 |
| *16,642, CDKN1A* | *co-regulation r, raw* | *+0.418* | *89th* | | |
| *4,642, CDKN1A* | *CHANGE, Spearman* | *+0.290* | *88th* | | |

**In the unselected family MDM2 sits at the 36th and 60th percentiles — the middle, twice over.** That is
the claim to rely on, and it is the one the correction strengthens rather than weakens: the proper family
puts MDM2 closer to the centre than the discovery set did. The contrast gene sits at the 89th in the same
family, which is what a gene that genuinely tracks MG53 looks like.

Inside the discovery set the two recomputed statistics give the 26th and 9th percentiles. Those should be
read for what they are — ranks among genes already selected for MG53 association — and the LEVEL one carries
the extra warning of Table 2: roughly one gene in eleven is at least that negative, in a distribution
dominated by plate structure.

The cost of the honest family is that it is the run's Pearson r on z rather than a statistic recomputed here,
so it cannot be split into level and change. Computing a true unselected distribution for either would need
per-exposure values for all 16,642 genes, which the export does not carry.

## Joint distribution

Counts in each MG53 x MDM2 quintile cell, 1,132 exposures, against the 45.3 expected per cell if the two were
independent (chi-square p = 0.042, and knife-edge: an equal-size quintile split that allocates the 2 leftover rows differently gives p 0.055):

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
| 843 line x exposure | within exposure, TP53-WT | mean rho -0.162, p 0.036, **q ~0.16** | a hint, unconfirmed |
| 843 line x exposure | within exposure, TP53-altered | -0.047, p 0.45 | nothing |
| single cells | untreated, TP53-WT | rate ratio 1.016, 34th percentile of 85 controls | nothing |
| single cells | untreated, TP53-altered | 0.915, p 0.005, 3.6th percentile | replicates, wrong arm for p53 |
| single cells | idarubicin, TP53-WT | **+15% on plate 14, -6% on plate 6** | irreproducible |
| 53,084 cells | screen, common slope | -0.35% per doubling, same in all 6 covariate sets | smallest of the eight; under the lone-discovery bar |
| 53,084 cells | screen, WT vs altered | -0.0054 vs -0.0048, difference CI [-0.010, +0.009] | ~21% power; uninformative |
| 843 line x exposure | genotype interaction, **raw** | WT extra -0.178 ± 0.038, **p 2e-06** | exposure-confounded |
| 843 line x exposure | genotype interaction, **within exposure** | WT extra -0.045 ± 0.049, p 0.36 | no genotype effect |

**The relationship between MG53 and MDM2 is bounded and small, not demonstrably zero**, and the bound is
what the data give: per doubling of measured MG53, MDM2 moves between **-3.2% and +3.4%** at the exposure
level, between **-0.61% and -0.08%** in the genome-wide screen, and by nothing detectable across untreated
cell lines (where the bound is weak, |r| < 0.36) or between the MG53-positive and MG53-negative cells of a
single well. The screen's "down with MG53" verdict is a ranking, and the smallest effect among the eight
genes that cleared, carried by MDM2's precision rather than its size; in the unselected 16,642-gene family
MDM2 sits at the 36th percentile.

**Nothing about it looks p53-mediated**, which is what the question was — though that now rests on the
tests with power rather than on the WT/altered comparison in the screen. The per-line genotype interaction
vanishes once exposures are held fixed (p 0.36), and the contrast gene's two arms land on top of each other
there while its raw interaction is as significant as MDM2's. Partialling out p53 output makes the exposure-
level correlation *more* negative, not less. The tilt lives in the exposures that do **not** activate p53
(Spearman -0.119, p 9e-05) and is absent in the 50 that do (+0.048, **p 0.74**). CDKN1A and MDM2 move in
*opposite* directions with MG53 at three independent resolutions, which no p53 route predicts for two genes
p53 induces together. The one single-cell result that replicates sits in the p53-altered arm — although the
arms there are not statistically distinguishable either (difference +0.105 ± 0.077, p 0.17).

**What the data are good for, and what they are not.** MDM2's side of the measurement is sound: the 3.07x
wild-type/altered baseline split at p 3.3e-12 is the p53-MDM2 feedback loop recovered from this very table,
so a comparable MG53 effect would not be missed for want of detection in the outcome. The limit is on the
MG53 side: 5.89 CPM, 12.4% zeros, split-half reliability 0.289 to 0.705 depending on subset, the largest
plate gap of 16,656 genes, and two wells of the same exposure disagreeing by 21 percentage points at
single-cell resolution. Tahoe also has no MG53 perturbation, no protein measurement, and one time point. An
absence here constrains the association; it cannot rule out a protein-level or post-transcriptional link,
which is where TRIM72's known biology mostly lives.

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
| `tables/mdm2_mg53_genotype_interaction.csv` | the per-line MG53 x TP53-status interaction for both genes, fitted raw and within exposure |
| `tables/mdm2_mg53_allgene_null.csv` | MDM2's percentile in each reference family, with a `family` column stating that the 4,642-gene one is a discovery set |
| `tables/mdm2_mg53_allgene_null_cpm_pooled.csv`, `..._r2_median_lines_mean.csv` | the full per-gene distributions those percentiles come from, 4,642 genes each |
| `tables/mdm2_mg53_extremes.csv` | the named exposures at both ends of MG53 |
| `tables/mdm2_mg53_crosstab.csv` | the joint quintile counts with expected counts and the chi-square |
| `tables/mdm2_mg53_context.csv` | what each gene is: level, detection, program membership, response range |

**What is circular, and it is two things, not one.** MDM2's program membership, its rank, and its
p53-activation fold change were all selected using the TP53 genotype labels, so they cannot be used to argue
about p53-specificity — they are descriptive only. Separately, the **4,642-gene reference family is itself a
selected set**: 4,500 of its members are there because the screen called them significant against MG53, and
MDM2 is one of them, so percentiles within it are ranks inside the discovery set. The 16,642-gene
co-regulation family is unselected and is the one the conclusions rest on. Nothing in the MG53 screen
columns used the TP53 labels.

**Corrections this document carries**, recorded rather than quietly fixed, because an earlier version of
each was wrong: the reference family was called "all genes" when 97% of it was selected against MG53; MDM2
was called the best-measured gene in the analysis when it is 903rd of 16,643 by level; three Spearman
correlations were quoted with their OLS slope's p value, one of them overstating significance by nine orders
of magnitude; the WT-versus-altered equality in the screen was said to mean a p53-mediated effect "cannot"
behave that way, when the test has about 21% power; the per-doubling-of-true-MG53 figure was given as a
point value using the reliability subset that maximises it; the per-line genotype interaction, which is
significant at p 2e-06 before exposures are held fixed, was not reported at all; and the unit-3 n was given
as 861 where every contrast in it runs on 843.
