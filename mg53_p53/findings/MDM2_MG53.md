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

The second is measurement. MDM2 is **well** measured — 185.8 CPM, detected in all 50 lines, moved up by 96
of the 98 reference compounds — while MG53 sits at 5.89 CPM with 12.42% of the 62,611 usable profiles from
expressing lines at zero. That figure is reproducible only with its denominator, which earlier versions of
the three places it appears in this document did not carry: over all 63,921 usable profiles it is 13.69%,
and over all 66,449 profiles 16.56%. MDM2 is still not the best-measured gene in the data (185.8 CPM is
903rd of 16,643 genes by level, and among the 29 canonical effectors TNFRSF10B is higher at 200.5 CPM); the
point is only that nothing MDM2 shows or fails to show here is a detection problem on MDM2's side.

| | MG53 (TRIM72) | MDM2 | CDKN1A (contrast gene) |
|---|---|---|---|
| Median level across lines | 5.89 CPM over the **DMSO wells** (3.95 CPM over all wells, which is the scope of the other two cells; 6.13 on reliable plates) | 185.8 CPM (903rd of 16,643) | 56.4 CPM |
| Lines where detected | **49 of 50** (NCI-H661 fails the expression filter); 12.42% of usable profiles from expressing lines are zero | 50 of 50 | 47 of 50 |
| Role | the exposure | p53 regulator (p53 induces it; its protein degrades p53) | p53 effector (arrest) |
| In the data-defined p53 program | not a member | induction arm, **rank 3** of 180 | induction arm, rank 29 |
| Moved up by | — | 96 of 98 compounds | 85 of 98 |
| Fold change under p53 activators, WT lines | — | **1.255x**, the largest of all 195 program genes | 1.117x |
| Baseline, TP53-WT vs TP53-altered lines | 1.08x, p 0.77 | **3.07x, p 3.4e-12** | 1.96x, p 5.8e-4 |
| Fold-change range over the 1,132 exposures | 0.31x to 12.24x | 0.46x to 2.11x | 0.50x to 2.15x |
| Split-half reliability | 0.289 full-data (0.301 in TP53-WT lines, 0.283 in altered); the 0.425-0.705 subset values are not scope-matched and no "true MG53" scale is built from any of them | — | — |

**That baseline row is the positive control for everything below**, with one limit stated up front. The
per-line baseline measurement finds MDM2 running 3.07x higher in TP53-wild-type lines than in TP53-altered
ones — the p53 → MDM2 feedback loop, textbook — and finds nothing from MG53. The exact comparisons, since
they are not identical: MDM2 is 17 WT against 33 altered lines, ratio of geometric means 3.07x, Welch
p 3.4e-12 (Mann-Whitney on the medians: 3.14x, p 1.8e-7); MG53 is 17 against 31 lines, 1.08x, Welch p 0.77
(Mann-Whitney median ratio 1.20x, p 0.78).

What that licenses is narrow but real: **MDM2's side of every null below is sound** — a gene whose 3x
biological signal this measurement recovers at p 1e-12 is not failing to show a comparable MG53 effect for
want of detection. What it does **not** license is any claim about MG53's reliability, which is separately
and poorly characterised: the project's two published anchors — 0.289317 split-half (`fe = ddxg`) and
0.114342 replicate-well (`fe = dd`) — are different specifications and are not interchangeable, the
`key_results.csv` row usually cited for "0.114" in fact reads 0.113639, and the plate and replicate problems
documented throughout sit underneath all three. A null here is a null about the *association*, limited by
the exposure, not by the outcome.

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
| 3. cell line x drug-dose | **843** cells | 18 selected exposures (13 MG53 raisers + 5 p53 reference activators) x 50 lines |
| 4. the genome-wide screen | 53,084 cells | reported from the run, not recomputed here |
| 5. single cells in one well | up to 47 lines; **20,120** line x well groups at full scale | MG53-detected against MG53-undetected cells: two well sets in Table 6, every well class in Table 6b |

Unit 3's n is 843, not the 900 rows of the source table: MDM2 is present in 861 of them and MG53's corrected
value in 843, so every MG53 → MDM2 contrast runs on the 843 where both exist (305 wild-type, 538 altered),
and the CDKN1A contrast on 789.

Unit 4 is reported rather than recomputed because per-gene **per-line** values are not in the export — only
MG53 and the program score are resolved per line for all exposures. Unit 3 exists because two of the
pipeline's own step outputs do carry per-line values for named genes, and they are nested:

| Table | Shape | Used as |
|---|---|---|
| `downstream_p53/tables/a_per_line_effects.csv` | MG53, five p53 genes (MDM2, CDKN1A, BBC3, PMAIP1, TP53) and the program score, over 18 selected exposures x 50 lines — 900 rows | unit 3 above |
| `p53_dependence/tables/per_line_effects_selected.csv` | ten gene labels — MG53, eight p53 genes and the program score — over **87** drug-doses x 50 lines at scope "mean of used wells", 40,583 rows, **4,179 of them MDM2** | the out-of-sample test at the end of Table 4 |

The second contains the first. Seventeen of its 87 drug-doses are 17 of unit 3's 18 (Panobinostat 5 µM is
the one exposure unit 3 has and it does not), and across the 5,507 line x exposure cells the two tables
share over their seven common genes, every value is the same number rounded to six significant figures —
max |diff| 5.0e-06, and exactly 0 once unit 3's value is rounded. So the larger table is a strict superset
of unit 3's quantity, and its other **70 exposures are held out**: never used above, and the test of unit
3's one positive row. An earlier version of this passage said one pipeline step had exported per-line
values for five genes over 18 exposures and stopped there, and the closing section then recommended a
follow-up on the premise that 18 was all the run had.

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
| MG53 z x MDM2 z | **-0.092** | **0.0020** | +0.003 | -0.28 to +0.25 |
| MG53 log2 fold x MDM2 log2 fold (the table above) | -0.080 | 0.0074 | +0.006 | -0.046 to +0.048 |
| after adjusting for transcriptome-wide activity | -0.022 (partial) | 0.45 | +0.062 | -0.15 to +0.29 |

The -0.092 reproduces the run's own figure exactly, and its drug-bootstrap CI (-0.156 to -0.022, also the
run's) excludes zero. But the Pearson on the same pairs is **+0.003**, and this file's own compound bootstrap
of that Pearson spans **-0.204 to +0.213**. When rank and product-moment statistics disagree that completely,
neither is describing a line: it is a cloud with a slight tilt through the middle and the opposite tilt at
the end. Adjusting for how much the whole transcriptome moved (`atlas_n_sig_genes`, cell counts, S and G2M
phase, UMI per cell) takes the partial Spearman to **-0.022** (its own p 0.45) and the compound-bootstrap p
on the slope to 0.46.

The bound this unit supports, rather than a bare "nothing": per doubling of measured MG53, MDM2 changes by
between **-3.1% and +3.4%** (95%, compound-clustered).

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

## Table 4 — within one exposure, across cell lines: the contrast that showed something, and the test that retires it

Hold the drug and dose fixed and compare the lines against each other. Among the lines given the same
exposure, do the ones that raise MG53 most show the least MDM2? On these 18 exposures this is the only
contrast in the document where the answer is not flatly no, so it gets the most careful null — and then, at
the end of the section, a test on the 70 exposures of the run's larger per-line panel that it was not
selected on, which it fails.

The unit is 843 line x exposure cells — the 18 selected exposures for which the pipeline exported per-line
values for MDM2 — and each line is compared only against the other lines on the same exposure. The 18 are
not one panel. Thirteen were selected for raising MG53: `a_selected_drugdoses.csv` role beginning "TRIM72
raiser", panel call up at z ≥ 4, fold change 2.05x to 12.24x, and 5 of those 13 are p53 reference
activators as well. The other **five are p53 reference activators that missed that cut, and four of them
lower MG53** — Topotecan 0.5 µM 0.93x, Mitoxantrone 0.5 µM 0.89x, Selinexor 5 µM 0.81x, Amsacrine 5 µM
0.76x — the fifth, Idarubicin 0.5 µM, raising it 2.15x at z 3.42, just under the cut. Those four are the
only exposures in the 18 where MG53 goes down at all. (Earlier versions called all 18 "MG53-raising
exposures", here and in the unit table near the top; four of them lower it.) The split moves the
correlation below by a quarter (-0.223 across the 13 against -0.162 across all 18), so it is carried
through there. Binned first, five bins per group:

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
to -0.05 in the top — though not from the first bin, and as a single slope that is **-0.060 (95% CI -0.143
to +0.020, cell-line bootstrap p 0.12)**: not significant. In the altered lines the pattern is
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
b₃·(MG53 × WT), cluster-robust on cell line — 49 lines for MDM2, 46 for the CDKN1A rows, which lose three
lines to non-detection.

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

### The per-exposure Spearman, and its two permutation nulls

The statistic is a Spearman per exposure over the lines in that group, averaged over the 18. Two averages,
because they are different numbers: the **arithmetic** mean of the 18 rhos is **-0.162473** in the
wild-type MDM2 row, and the **Fisher-z** mean is **-0.179022**. The Fisher-z one is the pipeline's
estimator (`a_pooled_over_drugdoses.csv`; README_tables.txt: "mean rho over a set of drug-doses (Fisher z
average)"), and recomputing it here from `a_per_line_effects.csv` returns the pipeline's own `mean_rho` to
six decimals in all 18 of the exposure-set x group x contrast cells the two tables share. Fisher z
stretches the large correlations, so the two means part company whenever the per-exposure rhos spread, and
which one ends up further from zero depends on which tail is the longer: in this row it is the negative
one, reaching -0.65, so the Fisher-z mean sits 10% further out, while in the all-lines row it sits 1%
closer in. The arithmetic mean stays this document's statistic and both are in the table below. (An earlier
version called -0.162473 "the pipeline's own estimator". It is not; the pipeline averages in Fisher z and
reads -0.179022.)

Two nulls, and the difference between them is the point:

- **per-exposure shuffle**: MDM2 permuted independently inside each exposure. Holds the exposure set, the
  line count and both marginals fixed — but it also destroys the fact that the *same* 17 or 30 lines appear
  in all 18 exposures. If a line simply tends to run high in MG53 and low in MDM2 as a standing property,
  the real statistic keeps that and this null throws it away, so its p is too small. It is the
  anti-conservative of the two, and no table in the run applies it to a mean over exposures: the pipeline
  permutes residuals inside a *single* exposure (`a_line_correlations.csv`, `p_perm`), never across a set.
- **line-label shuffle**: one permutation of the cell-line labels, applied to every exposure at once. Each
  line's whole MDM2 profile travels together and is attached to a different line's MG53 profile. Line-level
  structure survives in the null, so what gets tested is the claim actually being made. **This is the null
  the pipeline reports**: `a_pooled_over_drugdoses.csv` carries exactly one p column,
  `p_line_permutation`, defined in README_tables.txt as "ONE line-label permutation applied to all
  drug-doses at once (they share lines and wells)", on 5,000 draws.

| Group | Contrast | mean rho over the 18, arithmetic | the same, Fisher z | negative in | p, per-exposure shuffle | **p, line-label shuffle** |
|---|---|---|---|---|---|---|
| all lines | MG53 change → MDM2 | -0.017 | -0.017 | 11 of 18 | 0.64 | 0.71 |
| **TP53-WT (17)** | **MG53 change → MDM2** | **-0.162** | **-0.179** | **11 of 18** | **0.005** | **0.036** |
| TP53-altered (30) | MG53 change → MDM2 | -0.047 | -0.048 | 12 of 18 | 0.29 | 0.45 |
| TP53-WT | MG53 *level* → MDM2 | -0.033 | -0.038 | 9 of 18 | 0.55 | 0.69 |
| all lines | *CDKN1A* → MG53 change | +0.135 | +0.140 | 4 of 18 | <0.001 | 0.008 |
| TP53-WT | *CDKN1A* → MG53 change | +0.163 | +0.172 | 2 of 18 | 0.006 | 0.059 |
| TP53-altered | *CDKN1A* → MG53 change | +0.122 | +0.131 | 6 of 18 | 0.012 | 0.086 |

**Both nulls are computed here, and the line-label one is the pipeline's.** On the wild-type MDM2 row the
per-exposure shuffle gives p 0.005 and the line-label shuffle p 0.036, with a null spread 34% wider
(SD 0.058 against 0.078) — the line-level structure the per-exposure shuffle discards. The pipeline had
already run the line-label null on the same statistic and got **p 0.030194** on 5,000 draws against 0.036
here on 2,000, with q 0.181164 by Benjamini-Hochberg inside its own 12-test family (two predictors x six
outcomes, not the nine contrasts accounted for below). Both of its figures are carried row by row into
`tables/mdm2_mg53_per_exposure_rho.csv` in `pipeline_` columns, so the two can be compared without leaving
the file. The 0.036 above therefore *reproduces* the pipeline rather than correcting it, and the
per-exposure shuffle's 0.005 is the anti-conservative one of the two. (An earlier version of this passage
called the line-label null "the stricter null", said it "costs the result most of its significance", and
called the gap "exactly the inflation the weaker null was hiding" — written as though this document had
imposed a null the pipeline had not. All three readings are withdrawn: for a mean over exposures the
line-label null is the only one the pipeline runs, and it reports the same answer.)

**The split this document did not report, which is where the result actually lives.** The same statistic and
the same two nulls, run on the 13 raisers and the 5 reference activators separately:

| Exposure set | Group | n | mean rho, arithmetic | the same, Fisher z | negative in | p, per-exposure shuffle | **p, line-label shuffle** | the pipeline's own p / q |
|---|---|---|---|---|---|---|---|---|
| **13 MG53 raisers** | **TP53-WT** | 13 | **-0.223** | **-0.244** | **10 of 13** | 0.0005 | **0.0035** | 0.0040 / 0.024 |
| 5 p53 reference activators | TP53-WT | 5 | -0.005 | -0.005 | 1 of 5 | 0.97 | 0.977 | 0.977 / 0.977 |
| all 18, the row above | TP53-WT | 18 | -0.162 | -0.179 | 11 of 18 | 0.005 | 0.036 | 0.030 / 0.181 |
| 13 MG53 raisers | TP53-altered | 13 | -0.046 | -0.047 | 9 of 13 | 0.38 | 0.539 | 0.538 / 0.538 |

The whole wild-type tilt is in the raisers. Putting back the five exposures that were never selected for
MG53 pulls the correlation from -0.223 to -0.162 and its p from 0.0035 to 0.036, so the headline row is the
diluted union — which is all this document reported until now. The dilution is in what those five exposures
are: a Spearman over 17 lines needs the exposure to have moved MG53 by different amounts in different
lines, and the median between-line SD of MG53's change is **0.86 across the five against 1.26 across the
13** (median fold change 0.89x against 3.82x), so there is less there to rank the lines on.

This localises the result rather than rescuing it, but it does move the accounting. The 13 still run from
-0.65 to +0.31 with three of them positive, the same 13 in the altered arm are flat at -0.046 (p 0.54), and
it is still the same 17 lines. In the nine-contrast accounting below, though, the raiser row is one more
contrast and not a substitute for the union: counted in among the nine its q is **0.035 at most** — that is
its value at rank 1, and Benjamini-Hochberg can only move it down — and against all 27 contrasts this file
now computes (three exposure sets x three groups x three contrasts, nested, so that is the conservative end)
it is the smallest p of the 27, at **q 0.095**. Both clear 0.1, which the 18-exposure row does not, which
leaves this subset as the one cell of unit 3 that clears its own accounting — so the 87-exposure test below
is run on the raiser subset too, not only on whole panels. And the pipeline's own q 0.024 here is not a
third opinion: like its 0.181 above, it is BH inside a 12-test family of its own.

Then the accounting, which is where it ends. Nine contrasts were tested; at p = 0.036 and rank 2 this is
**q ≈ 0.16** by Benjamini-Hochberg, so it does not clear 0.1. It sits in the smallest arm available,
**17 lines**. Its magnitude is estimator-dependent: the same data as a pooled within-exposure residual slope
gives -0.060 with a cell-line bootstrap p of 0.12. The per-exposure correlations run from **-0.65 to +0.31**,
so the mean of -0.162 is an average over exposures that disagree about the sign. And the contrast does not
reproduce in the TP53-altered arm, while the genome-wide screen — with 47 lines and all 1,132 exposures
rather than 18 — puts the wild-type-minus-altered difference at -0.0006, p 0.89.

### The out-of-sample test, on 70 exposures this statistic has never seen

The 18 exposures above are not all the per-line MDM2 the run holds.
`p53_dependence/tables/per_line_effects_selected.csv` carries the same quantity over **87** drug-doses on
the same 50 lines — the same number to six significant figures on all 5,507 cells the two tables share
across their seven common genes, 813 of those cells MDM2's — and 17 of the 87 are the exposures used above.
That leaves **70 exposures this statistic was not selected on**, so the test this row was nominated for was
runnable in the run's own output all along. Both of unit 3's estimators, recomputed on each panel, with the
line-label null and a cell-line bootstrap:

| Panel | exposures | mean rho, TP53-WT | negative in | p, line-label shuffle | pooled within-exposure slope (95% CI) | p | n |
|---|---|---|---|---|---|---|---|
| in sample (the 17 shared with the 18) | 17 | **-0.181** | 11 of 17 | **0.029** | -0.072 (-0.144 to -0.004) | 0.040 | 288 |
| **held out** | **70** | **-0.008** | **35 of 70** | **0.841** | -0.014 (-0.043 to +0.013) | 0.378 | 1,190 |
| whole panel | 87 | -0.041 | 46 of 87 | 0.265 | **-0.031 (-0.060 to -0.006)** | **0.016** | 1,478 |
| in sample, MG53-raiser role | 14 | -0.201 | 9 of 14 | 0.018 | -0.077 (-0.147 to -0.011) | 0.023 | 237 |
| **held out, MG53-raiser role** | **10** | **-0.032** | **5 of 10** | **0.66** | -0.001 (-0.039 to +0.040) | 0.99 | 170 |

**The published statistic does not replicate.** On the 70 held-out exposures the mean of the per-exposure
Spearmans is **-0.008**, negative in exactly half of them — **35 of 70** — with a line-label p of **0.84**.
On the 17 shared exposures the same code on the same table gives **-0.181 at p 0.029**. Two parts of one
table, the same 17 wild-type lines, the same estimator, and they disagree about whether there is anything
there. (The in-sample -0.181 is slightly larger than the -0.162 above because the one exposure unit 3 has
and this table does not is Panobinostat 5 µM, whose own rho is **+0.147**; dropping it moves the mean of the
remaining 17 from -0.162 to -0.181.)

**Nor does the subset the tilt lived in.** The 13 raisers above are unit 3's own label, panel call up at
z ≥ 4. This panel carries a raiser role of its own on **24** of its 87 drug-doses — a different 24 from the
screen hits below, and a looser cut: of the 17 shared it marks **14**, adding Idarubicin 0.5 µM, Topotecan
0.5 µM and Mitoxantrone 0.5 µM (the last two lower MG53) and dropping Harringtonine 5 µM. That is the
nearest thing to unit 3's raiser set the larger panel has, and **10** more drug-doses carry the role among
the held-out 70. On the 14 in sample it reads as unit 3's raiser row does: mean rho **-0.201**, negative in
9 of 14, line-label p **0.018**, pooled slope **-0.077 (-0.147 to -0.011, p 0.023, n 237)**. On the 10 it
had never seen it is **-0.032**, negative in **5 of 10**, p **0.66**, slope **-0.001 (-0.039 to +0.040,
p 0.99, n 170)** — zero to three decimals. The localisation holds inside the selected panel and vanishes
outside it, exactly as the union does: the one cell of unit 3 that cleared its own accounting does not
replicate either.

The pooled within-exposure slope is the estimator to carry forward, because the mean of rhos gives every
exposure the same weight however little MG53 moves across the lines in it, while a slope weights each
exposure by the MG53 spread it actually has — and the two panels differ there: the median within-exposure SD
of MG53 across the wild-type lines is **1.23 log2 on the 17** (selected for raising MG53) against **0.90 on
the 70**, where only 10 of the 70 carry an MG53-raiser role at all and the other 60 entered as p53
activators or screen hits. Over all 87 exposures the slope is **-0.031 log2 MDM2 per log2 MG53 (95% CI
-0.060 to -0.006, cell-line bootstrap over 17 clusters, p 0.016, n 1,478)** — **-2.1% of MDM2 per doubling
of MG53, interval -4.1% to -0.4%** — against **-0.072 (-0.144 to -0.004, p 0.040, n 288)** on the 17, and
**-0.014 (-0.043 to +0.013, p 0.378, n 1,190)** on the 70 held out alone. So the tilt as a slope is 43% of
what the 17 exposures said, undetectable on held-out exposures by itself, and inside the bound Table 1
already put on this pair (-3.1% to +3.4% per doubling). It is also wild-type-only on this panel, as it was
on the 18: the altered arm reads **-0.005 (-0.027 to +0.015, p 0.637, n 2,616)** over the same 87 exposures,
and all 49 lines pooled read **-0.004 (-0.023 to +0.016, p 0.650, n 4,094)**. **The 87-exposure slope is
this document's estimate of the within-exposure tilt**; the 17- and 18-exposure figures above are what a
selected panel gave.

One convention note, because -0.072 and the -0.060 above are the same estimator fitted two ways. The slopes
in this subsection remove each exposure's mean **inside the arm being fitted**, which is the exposure fixed
effect the contrast asks for; the -0.060 above removes each exposure's mean over all 50 lines and then takes
the wild-type rows, which leaves a per-exposure offset inside the arm. On unit 3's own 18 exposures the
arm-demeaned fit reads **-0.067 (-0.137 to +0.001, bootstrap p 0.053, cluster-robust p 0.067)** rather than
-0.060, so somewhat more than half the gap between -0.060 and -0.072 is the convention and the rest is
Panobinostat 5 µM leaving. The 17- and 18-exposure fits differ by that one exposure and land either side of
0.05 — bootstrap 0.040 and cluster-robust 0.050 on the 17, 0.053 and 0.067 on the 18 — so nothing should be
read from which of them clears it. What settles the row is the 70. That 18-exposure row sits in
`tables/mdm2_mg53_out_of_sample.csv` beside the other five for exactly this comparison.

Two limits the larger panel does not relieve, and one scope note.

- **It is not label-free.** Twenty-four of the 87 drug-doses are in the panel *because* they were TRIM72
  wild-type-versus-altered screen hits — selected using the TP53 labels — and all 24 sit in the held-out 70
  (33 of the 70, and 36 of the 87, carry that flag). The held-out set is out of sample for the MG53 → MDM2
  contrast. It is not label-free about TP53.
- **It is still 17 wild-type lines.** The same 50 cell lines, the same 17 with wild-type TP53, 1,478
  wild-type line x exposure cells instead of 305. The panel buys exposures, not lines, so the smallest-arm
  problem behind this row is untouched.
- **Scope.** The `p53_dependence` step asks whether p53 regulates MG53, which is not one of this project's
  two questions, and none of that step's conclusions are used here or anywhere in this document. What is
  used is its per-line table, as raw per-line gene values — the same quantity unit 3 is built from, over
  more exposures.

So: a hint, in the one place it could show up, that does not survive its own accounting and does not survive
its own out-of-sample test. **The row this document used to nominate for follow-up is withdrawn.** An
earlier version of this section ended "if anything in this document is followed up, this is the row to
follow up", and the closing section recommended it on the premise that the run could not supply per-line
MDM2 for more than 18 exposures. The premise was false — 87 — and on the 70 the row had not seen, it is a
coin flip.

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

This is the most literal reading of "different levels of MG53", and the design that holds the most fixed:
inside **one cell line, one well**, split the cells by whether MG53 was detected in them and ask how much
MDM2 each group has. Cell line, drug, dose, plate and well are all held fixed by construction. The run fits
a quasi-Poisson GLM per line (offset log UMIs; covariates log UMIs, S-phase and G2M fractions, well
indicator), pools lines by random effects, and — crucially — puts **every non-p53 panel gene through the
same fit**, giving 78 to 85 control genes to place MDM2 against. The table below is six wells of two
exposures, though — DMSO H11 and H12 on plates 6 and 14, idarubicin C12 on each — while the same GLM runs
over every well class in the data, 20,120 line x well groups over 1,289 wells, which this table does not
use and Table 6b below does. An earlier version called this the best-controlled comparison in the data; the
control is the design's, and Table 6b has the same design over all of those wells.

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
resolution, and it is why no conclusion in this document rests on a single well set. It is a two-well
reliability statement, not the pooled behaviour of this resolution, which runs the other way: Table 6b.

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

A caveat that belongs with this table specifically, and it is larger than earlier versions said. MG53 is
detected in **1.3%** of an untreated line's cells here (0.4% on plate 6, 3.0% on plate 14; 7.5% and 10.0%
in the two idarubicin wells — medians over the 49 lines), and a detected cell carries about **one** UMI of
it: 1.12 to 1.18 per detected cell across the six well sets. The "about 5 UMIs" of earlier versions was a
pseudobulk profile's whole count over a median of 1,217 cells, not a cell's, which understated how close to
the detection floor this contrast runs. Detected cells are also **23% to 32%** more deeply sequenced than
the undetected cells of the same well set (2,014 against 1,631 median UMIs on idarubicin plate 14), so
"MG53-detected" partly means "more deeply sequenced cell". The UMI offset, the UMI covariate and the
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
same well: +20.8% and -8.5% in the altered lines, both holding when depth is matched. Only the MDM2 leg is
outside its control-gene distribution, at the **3.6th percentile of 84** controls; CDKN1A, at the **77th**,
is inside it, and 19 of those 84 unrelated genes move up more than CDKN1A does. (An earlier version called
both legs outside it, against the 77th percentile printed in the table above and the generator's own
`control_percentile_verdict`, which has read "inside" for that row all along.) The controls themselves tilt
up in MG53-positive cells — their median rate ratio is **1.068** here, not 1.00 — so read against that
median the split is **+13.1% and -14.4%**: a relative statement, not an absolute one. The same sign split
appears at the drug-dose unit (CDKN1A rho +0.29, MDM2 -0.08) and in the genome-wide screen (+0.0104 against
-0.0050), and it survives at full scale in untreated wells (next section). Two of the three resolutions
carry it at full strength; in these two well sets only the MDM2 leg clears its own control family, and at
full scale neither leg does — MDM2 sits at the 27th percentile of its 63 placebo outcomes in the same
untreated altered cell and CDKN1A at the 83rd.

It also argues against the p53 route rather than for it. CDKN1A and MDM2 are both p53-induced; under p53
they move **together**. Finding them moving apart — and doing so most clearly in the lines where p53 is
disabled — points at whatever distinguishes an MG53-positive cell from its neighbours (cell-cycle position,
stress state, arrest) rather than at p53 arbitrating between them.

### Table 6b — the same GLM at full scale, where the sign goes the other way

The run puts Table 6's GLM over every well class, not two well sets: **20,120 (cell line x well) groups**
carrying a usable MDM2 comparison — 9,099 of them in wild-type lines, 11,021 in altered — over **1,289
wells and 47 lines**, with Hartung-Knapp stage-2 intervals, 16 placebo predictor genes matched on detection
rate, 62 to 66 placebo outcome genes, ambient-contamination controls, and the per-doubling bound Table 6
does not publish. Not quite the same fit: the group is one well rather than a line's two or four, lines are
pooled in two stages rather than one, and each group is capped at 2,000 cells. The run checks the two
against each other on the exposure they share — under idarubicin 5 µM the wild-type P53_SCORE ratio is
**1.0198** here against **1.0195** in Table 6, and the altered one 0.9817 against 0.9832. Table 6's eight
MDM2 cells are two exposures of this, the two with a two-plate replicate; the table below is every class.
Earlier versions of this document did not open the full-scale step at all.

| Well class, MDM2 | contrast | lines | groups | **rate ratio (95% CI)** | p | q in the step's p53/screen family (41-42 outcomes) |
|---|---|---|---|---|---|---|
| all wells | **WT minus altered** (the step's own primary estimand) | 47 | 20,120 | 1.059 (0.961–1.167) | 0.23, permutation **0.16** | 0.78 |
| all wells | all lines | 47 | 20,120 | **1.033 (0.994–1.074)** | 0.095 | 0.19 |
| all wells | TP53-WT | 17 | 9,099 | 1.071 (0.976–1.175) | 0.14 | 0.25 |
| DMSO, all 28 untreated wells | TP53-altered | 29 | 288 | **0.956 (0.917–0.997)** | 0.037 | 0.093 |
| TRIM72 raisers | all lines | 46 | 828 | **0.949 (0.915–0.984)** | 0.0056 | 0.020 |
| TRIM72 raisers | TP53-altered | 29 | 460 | 0.946 (0.903–0.990) | 0.019 | 0.055 |
| p53 activators | all lines | 45 | 852 | 0.997 (0.950–1.046) | 0.90 | 0.94 |
| other drugs | all lines | 47 | 17,913 | 1.043 (1.002–1.086) | 0.042 | 0.10 |

**The primary estimand is null everywhere.** Wild-type minus altered — the only contrast that can speak to
p53, since an MG53 → p53 effect can act only where p53 works — is a ratio of rate ratios of 1.01 to 1.07
across the five well classes, with TP53-label permutation p 0.11 to 0.85. That is the same answer Table 6's
+0.105 ± 0.077 (p 0.17) gives, now on 45 to 47 lines per class instead of 17 against 30 in four wells.

**The pooled ratio is positive, where Table 6's one replicating row is negative.** Over all wells MDM2
reads **+3.3%** in MG53-detected cells (p 0.095) and **+7.1%** in the wild-type lines (p 0.14) — the
opposite sign to the -8.5% of Table 6's untreated altered row and to plate 6's -5.9%, and the same sign as
plate 14's +15%. So the two-plate disagreement above is the small version of a sign that is not stable
across well classes either. Pooled over every well, neither direction is a result: the strongest of the
four all-wells cells is that +3.3% at p 0.095.

**Two class-specific negatives exist, and their two control families disagree about them.** In the TRIM72
raisers the pooled ratio is **0.949 (0.915–0.984, p 0.0056, q 0.020)** and in the untreated wells of the
altered lines **0.956 (0.917–0.997, p 0.037, q 0.093)** — the untreated negative of Table 6 at about half
the size, over all 28 DMSO wells rather than the 4 behind that row (which are among the 28). Against the
placebo **outcome** genes put through the identical fit — 66 of them in the raiser class, 63 in the
untreated one — MDM2 is unremarkable in both cells: the 15th percentile in the raiser class (empirical
p 0.39) and the 27th in untreated altered wells (p 0.55), while 17 of the step's 42 p53 and screen outcomes
clear q < 0.1 in the raiser cell and 13 of its 41 in the untreated one. Against the 16 placebo **predictor**
genes matched on detection rate it reads the other way: MDM2's negative is at the 6th percentile of that
family in the raiser class and is the most extreme of all 17 predictors in untreated altered wells
(empirical p 0.059, which is the floor 1/17 with 16 placebos). Two control families, opposite verdicts, one
underpowered cell each: that is the whole of it.

**The bound, which Table 6 never states.** Per doubling of a cell's MG53 — the step converts the detected /
undetected contrast to a doubling of the implied true MG53 rate under its pooled overdispersion, so this is
the same unit as the exposure-level bound — the wild-type interval is a rate ratio of **1.035 (0.988 to
1.083)**, and the largest change it cannot exclude is **8.3%**; in the untreated altered wells it is 0.978
(0.959 to 0.999), largest change not excluded **4.1%**. The exposure-level bound excludes anything past
3.4%, so this resolution is **2.4 times coarser** in the arm the p53 question needs: **6.7%**
per doubling is the smallest wild-type effect this fit would catch four times in five, and anything smaller
it misses more often than that (the untreated altered arm's 80%-power threshold is 2.9%).

**The contrast gene at the same scale.** CDKN1A reads **1.164 (1.122–1.208, p 2e-10)** over all wells and
**1.117 (1.058–1.180, p 4e-4)** in the untreated altered wells, so the opposite-sign split of the section
above survives in untreated cells over every DMSO well rather than four. Pooled over every class both genes
read *up* — CDKN1A far more — which makes the split a property of untreated cells rather than of this
resolution. CDKN1A is the sparser transcript and is fitted in fewer groups than MDM2 throughout — 8,811
over 1,107 wells and 42 lines, against MDM2's 20,120 over 1,289 wells and 47 lines — so the two genes'
full-scale cells are not over quite the same material.

## Table 7 — the genome-wide screen's own slope on MDM2

This is the one estimate with per-line resolution across all exposures: cell-line and drug-dose fixed
effects, 53,084 line x exposure cells, 47 lines. Reported from `c_screen_genes`, not recomputed.

| Arm / covariate set | slope (log2 MDM2 per doubling of MG53) | change in MDM2, measured MG53 | p |
|---|---|---|---|
| gw (primary) | -0.00500 | **-0.35%** | 0.016 |
| gw_all | -0.00501 | -0.35% | 0.015 |
| gw_pc | -0.00600 | -0.41% | 0.002 |
| curated_cycle | -0.00478 | -0.33% | 0.022 |
| no covariates | -0.00500 | -0.35% | 0.018 |
| gw_rt (readthrough-corrected) | -0.00501 | -0.35% | 0.006 |
| **TP53-WT lines only (17)** | -0.00539 | -0.37% | **0.21** |
| **TP53-altered lines only (30)** | -0.00476 | -0.33% | **0.016** |
| WT minus altered | -0.00063 | -0.04% | 0.89 |

An earlier version of this table carried a fourth column, "change in MDM2, true MG53", reading -1.19% on the
primary row and -1.13% to -1.43% across the others. That column is removed, not widened; the reason is given
under the first of the three readings below.

Three readings, in order of importance.

**The sign is robust and the size is tiny.** Every covariate set lands between -0.0048 and -0.0060,
including the readthrough-corrected one — so this is not spillover from the FUS / PYCARD-AS1 transcription
running into the TRIM72 locus. A doubling of measured MG53 buys **-0.35%** of MDM2, with a 95% interval of
-0.61% to -0.08% (line-clustered) or -0.51% to -0.18% (drug-clustered). MDM2's own range across exposures is
0.46x to 2.11x. This slope is not a player in that range.

There is no "per doubling of true MG53" figure here at all. An earlier version of this section gave one
as a range rather than a point, dividing the slope by each of the split-half reliabilities the run reports —
0.289 for the primary specification, then 0.425, 0.586, 0.610 and 0.705 for the active, p53-responsive and
MG53-moving subsets — and concluding that the true effect was "somewhere around -0.5% to -1.2%" per doubling.
The range was an improvement on the single -1.19% it replaced, and it is still wrong, for two reasons that
widening cannot fix.

The division is not licensed. MG53 and MDM2 are counted from the same cells, in the same well, against
the same total-UMI denominator, so the classical correction's requirement that exposure error be independent
of outcome error fails by construction: dividing scales the shared same-well artefact up along with any
signal. That channel has been demonstrated rather than assumed — a cross-well version of this kind of
association, exposure read in one well and outcome in its cross-batch replicate, sits at or below zero in
every arm while the same-well version is positive. (The earlier parenthetical that "the correction itself is
right" because 0.289 is already the Spearman-Brown full-data reliability — raw split-half 0.169,
2r/(1+r) = 0.289 — answered the wrong objection. Dividing once rather than twice is the correct arithmetic
for a correction of the wrong kind.)

And none of the high values is scope-matched. This table is fitted over all 1,132 exposures, while the
menu's 0.586 and 0.705 are variants `ii_p53` (0.585 under the `ddxg` fixed effects, 0.586 under `dd`: the 50
drug-doses with curated P53_ACTIVITY z >= 3) and `ii_trim72` (0.706 and 0.705: the 23 MG53-moving ones). A
divisor estimated on 23 or 50 drug-doses does not describe a 1,132-drug-dose fit — and neither variant is
the 142-drug-dose p53-activating set either, so **no scope-matched reliability for the p53-activating scope
exists** and every true-MG53 scaling of that scope anywhere in this project is unverified. The 0.289 anchor
is meanwhile the optimistic floor of the factor's range, because the split-half splits *cells* within each
(well, line) and so books every well-level artefact as signal; matched on the 102 replicated drug-doses the
same statistic reads 0.425, and the cross-batch replicate pairs support 0.078 to 0.105. The earlier -0.5% to
-1.2% was therefore not a range around a quantity; it was one unidentified number divided by another.

So **-0.35% per doubling of measured MG53** is what this table supports, and the measured scale is the only
one used below.

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
| 843 line x exposure | within exposure, TP53-WT | mean rho -0.162, p 0.036, **q ~0.16** — and **-0.008, p 0.84** on the 70 held-out exposures | does not replicate out of sample |
| 1,478 line x exposure | within exposure, TP53-WT, 87-exposure panel | pooled slope **-0.031 (-0.060 to -0.006)**, p 0.016; -0.014 (-0.043 to +0.013) on the 70 held out | the estimate that stands: -2.1% per doubling |
| 843 line x exposure | within exposure, TP53-altered | -0.047, p 0.45 | nothing |
| single cells | untreated, TP53-WT | rate ratio 1.016, 34th percentile of 85 controls | nothing |
| single cells | untreated, TP53-altered | 0.915, p 0.005, 3.6th percentile | replicates, wrong arm for p53 |
| single cells | idarubicin, TP53-WT | **+15% on plate 14, -6% on plate 6** | irreproducible |
| 20,120 line x well groups | all wells, every class pooled | **1.033 (0.994–1.074)**, p 0.095; WT 1.071 (0.976–1.175) | positive, opposite sign to the untreated row above; null |
| 20,120 line x well groups | all wells, WT minus altered (that step's primary estimand) | 1.059 (0.961–1.167), permutation p 0.16; null in all five well classes | no p53 contrast at this resolution |
| 828 line x well groups | TRIM72 raisers, all lines | **0.949 (0.915–0.984)**, p 0.0056, q 0.020 | 15th percentile of 66 placebo outcomes; context, not a result |
| 53,084 cells | screen, common slope | -0.35% per doubling, same in all 6 covariate sets | smallest of the eight; under the lone-discovery bar |
| 53,084 cells | screen, WT vs altered | -0.0054 vs -0.0048, difference CI [-0.010, +0.009] | ~21% power; uninformative |
| 843 line x exposure | genotype interaction, **raw** | WT extra -0.178 ± 0.038, **p 2e-06** | exposure-confounded |
| 843 line x exposure | genotype interaction, **within exposure** | WT extra -0.045 ± 0.049, p 0.36 | no genotype effect |

**The relationship between MG53 and MDM2 is bounded and small, not demonstrably zero**, and the bound is
what the data give: per doubling of measured MG53, MDM2 moves between **-3.1% and +3.4%** at the exposure
level, between **-0.61% and -0.08%** in the genome-wide screen, between **-4.1% and -0.4%** within an
exposure across the 17 wild-type lines on the 87-exposure per-line panel, and by nothing detectable across
untreated cell lines (where the bound is weak, |r| < 0.36) or between the MG53-positive and MG53-negative
cells of a single well — where "nothing detectable" means **nothing larger than about 8%**, the full-scale
single-cell fit putting the wild-type per-doubling ratio at 1.035 (0.988–1.083) and the untreated altered
one at 0.978 (0.959–0.999). That is the loosest per-doubling bound here — in the wild-type arm 2.4 times
weaker than the exposure-level one — and earlier versions of this sentence gave no bound at all for that
unit. The screen's "down with MG53" verdict is a ranking, and the smallest effect among the eight
genes that cleared, carried by MDM2's precision rather than its size; in the unselected 16,642-gene family
MDM2 sits at the 36th percentile.

**Nothing about it looks p53-mediated**, which is what the question was — though that now rests on the
tests with power rather than on the WT/altered comparison in the screen. The per-line genotype interaction
vanishes once exposures are held fixed (p 0.36), and the contrast gene's two arms land on top of each other
there while its raw interaction is as significant as MDM2's. Partialling out p53 output makes the exposure-
level correlation *more* negative, not less. The tilt lives in the exposures that do **not** activate p53
(Spearman -0.119, p 9e-05) and is absent in the 50 that do (+0.048, **p 0.74**). CDKN1A and MDM2 move in
*opposite* directions with MG53 at three independent resolutions — the single-cell one in untreated cells,
where pooling every well class puts both genes up — which no p53 route predicts for two genes p53 induces
together. The one single-cell result that replicates sits in the p53-altered arm, and it holds at full
scale — 0.956 (0.917–0.997) over all 28 untreated wells rather than four — although the arms there are not
statistically distinguishable either (difference +0.105 ± 0.077, p 0.17).

**What the data are good for, and what they are not.** MDM2's side of the measurement is sound: the 3.07x
wild-type/altered baseline split at p 3.4e-12 is the p53-MDM2 feedback loop recovered from this very table,
so a comparable MG53 effect would not be missed for want of detection in the outcome. The limit is on the
MG53 side: 5.89 CPM, 12.42% zeros among usable profiles from expressing lines, a split-half reliability of
0.289 whose subset values are not scope-matched and which cannot be divided out at all, the largest
plate gap of 16,656 genes, and two wells of the same exposure disagreeing by 21 percentage points at
single-cell resolution. Tahoe also has no MG53 perturbation, no protein measurement, and one time point. An
absence here constrains the association; it cannot rule out a protein-level or post-transcriptional link,
which is where TRIM72's known biology mostly lives.

**The one row this document used to nominate for follow-up is withdrawn.** It was the Table 4 row: within an
exposure, among TP53-wild-type lines, the lines that raise MG53 most showing the least MDM2 (mean rho
-0.162, p 0.036 under the cell-line-label shuffle, q ~0.16 over the nine contrasts tested). The run carries
per-line MDM2 for **87** drug-doses, not 18 — 70 of them never used above — and on those 70 the statistic is
**-0.008, negative in 35 of 70, line-label p 0.84**, against **-0.181, p 0.029** on the 17 shared exposures
of the same table. The subset that tilt actually lived in goes the same way: the 87-exposure panel labels 24
of its own drug-doses with an MG53-raiser role, and on the 10 of those never used above the statistic is
**-0.032, negative in 5 of 10, line-label p 0.66**, against -0.201 at p 0.018 on the 14 in sample. What
survives is the pooled within-exposure slope over all 87, **-0.031 (95% CI -0.060 to -0.006, p 0.016, n
1,478) = -2.1% of MDM2 per doubling of MG53**, against -0.072 on the 17 and -0.014 (-0.043 to +0.013) on the
70 alone: a number the size of the bounds above, not a lead. An earlier version of this paragraph said the
row needed "the two things this run cannot give it — per-line MDM2 values across all 1,132 exposures instead
of 18 ... and more than 17 wild-type lines". The first was false in the way that mattered: the run has 87,
which was enough to test the row and retire it. The second stands — the 87-exposure panel is the same 50
lines, 17 of them wild-type — and that panel is not label-free either, 24 of its drug-doses having been
selected as TRIM72 wild-type-versus-altered screen hits. **Nothing in this document is now nominated for
follow-up.** What would move it is in the paragraph above: more wild-type lines, an MG53 perturbation, a
protein measurement. Not more exposures.

## The files

| File | Contents |
|---|---|
| `tables/mdm2_mg53_bins.csv` | every binned table above, long form: unit, group, which variable was binned, bin bounds, n, mean / median / SD / SE / CI of the outcome in each bin, and the across-bin trend |
| `tables/mdm2_mg53_models.csv` | one row per contrast: slope, SE, t, p, Pearson, Spearman, and the cluster bootstrap's interval and p. The cluster is per unit - compound at the drug-dose unit, cell line at the per-line one - and `n_clusters` records which |
| `tables/mdm2_mg53_cpm_by_plate.csv` | the LEVEL comparison split by plate: per-plate medians of both genes, the within-plate correlation on each plate, and the between / within decomposition |
| `tables/mdm2_mg53_single_cell.csv` | the single-cell rate ratios with their control-gene percentiles and the depth-matched version, each also expressed relative to the control genes' own median (1.05 to 1.13 in the untreated well sets, 0.99 to 1.04 under idarubicin, not 1.00), and the well set's MG53 detection rate, UMIs per detected cell and detected-against-undetected depth gap |
| `tables/mdm2_mg53_single_cell_all.csv` | the same fit at full scale, from `single_cell_all`: every well class x TP53 contrast for both genes, with lines, groups and wells behind each cell, the step's own BH q within its p53/screen family (41 or 42 outcomes per cell, and how many of them clear q < 0.1 there), both placebo families (62 to 66 outcome genes, 16 detection-matched predictor genes), and the per-doubling bound with its 80%-power threshold |
| `tables/mdm2_mg53_per_exposure_rho.csv` | the within-exposure across-lines correlations: three exposure sets (all 18, the 13 raisers, the 5 reference activators) x three groups x three contrasts, each with the arithmetic and the Fisher-z mean, both permutation nulls, and the pipeline's own row for the same cell in `pipeline_` columns |
| `tables/mdm2_mg53_out_of_sample.csv` | the same within-exposure contrast on the 87-drug-dose per-line panel, as six panels x three arms: all 87, the 17 unit 3 uses, the 70 held out, the 24 the panel labels with an MG53-raiser role of its own split the same way (14 in sample, 10 held out, because unit 3's whole wild-type tilt sits in its raisers), and unit 3's own 18 refitted under this table's convention. Per row: the mean of the per-exposure Spearmans with its line-label null and null SD, the per-exposure rho range, the median within-exposure SD of MG53, the pooled within-exposure slope with its cell-line bootstrap interval and both p values, how many drug-doses of each panel carry a screen-hit role or flag and how many an MG53-raiser role, and the cell-by-cell agreement with unit 3's own table |
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
point value using the reliability subset that maximises it, then as a -0.5% to -1.2% range, when the
division is not licensed at all under same-well errors and none of the subset divisors is scope-matched, so
Table 7's true-MG53 column is now removed rather than widened; the per-line genotype interaction, which is
significant at p 2e-06 before exposures are held fixed, was not reported at all; the unit-3 n was given as
861 where every contrast in it runs on 843; "12.4% of profiles zero" was quoted bare in three places, where
it is 12.42% of the 62,611 usable profiles from expressing lines and 13.69% or 16.56% on the two wider
denominators; the split-half reliability was given as "0.289 to 0.705 by subset", a menu whose upper end
describes 23- and 50-drug-dose variants rather than any scope used here; Table 4's arithmetic mean of
-0.162473 was called "the pipeline's own estimator" when the pipeline averages the same 18 correlations in
Fisher z and reads -0.179022, now reported beside it; the per-exposure shuffle was called "the null the
pipeline reports" and the line-label shuffle "the stricter null", whose cost was "exactly the inflation the
weaker null was hiding", when the line-label null is the only one the pipeline runs on a mean over exposures
and it had already returned p 0.030194 for that cell, so this document's 0.036 reproduces the pipeline
instead of correcting it; unit 3's exposures were called "18 MG53-raising exposures" when 13 were selected
as raisers and the other five are p53 reference activators, four of which lower MG53; that split was not
reported at all, where the whole wild-type tilt sits in the 13 raisers (Fisher-z mean -0.244, against -0.005
on the five activators) — and that subset does not replicate either, reading -0.032 at line-label p 0.66 on
the 10 held-out drug-doses of the 87-exposure panel that carry a raiser role; the provenance passage said
one pipeline step had exported per-line values for five genes over 18 exposures, where a second step's
`p53_dependence/tables/per_line_effects_selected.csv` carries the same quantity for ten gene labels over 87
drug-doses — the same number to six significant figures on all 5,507 shared cells — so both tables and their
shapes are now named; and the closing section recommended following up Table 4's wild-type row on the
premise that this run could not supply per-line MDM2 beyond 18 exposures, when 70 of those 87 exposures were
held out and unexamined, and on them the row reads **-0.008, negative in 35 of 70, line-label p 0.84**
against -0.181 at p 0.029 in sample — so the nomination is withdrawn, and the pooled within-exposure slope
over all 87 exposures (**-0.031, 95% CI -0.060 to -0.006**) replaces the 18-exposure -0.060 as this
document's estimate of that tilt; the single-cell CDKN1A and MDM2 split was called "both outside the
control-gene distribution" when only MDM2 is (3.6th percentile of 84 controls), CDKN1A sitting at the 77th
with 19 controls above it, a verdict the generator's own `control_percentile_verdict` column had already
stored as "inside" and the table two rows above had already printed — so the control genes' own median rate
ratio (1.068 untreated) and both genes' ratios relative to it (+13.1% and -14.4%) are now carried in
`mdm2_mg53_single_cell.csv` and quoted; MG53 was given as detected in "50 of 50" lines, hardcoded in the
generator, where the export says **49** (NCI-H661 fails the expression filter, and `b_baseline_per_line.csv`
agrees at 49 of 50), which is now read from `export/all_genes/genes.csv` like the other two genes' counts;
the activity-adjusted partial Spearman was given twice as -0.019 where this file's own `models.csv` says
**-0.022299**, recomputed here from `c_drugdose_table.csv` by residualising both genes on the five activity
covariates, and the bootstrap p quoted beside it as 0.45 is **0.46** in the committed table (0.4535 is the
Spearman's own p, which is what that 0.45 appears to have been); the single-cell section used the well sets
of two exposures, called them "the best-controlled comparison in the data", and never opened the run's
`single_cell_all` step — the same GLM over **20,120 line x well groups, 1,289 wells, 47 lines**, fitted per
well rather than per line and pooled in two stages — where the pooled MDM2 ratio is **+3.3% (p 0.095)**
rather than negative, that step's own primary estimand (wild-type minus altered) is null in all five well
classes, and the per-doubling bound it publishes (**1.035, 0.988-1.083**, wild-type) is the bound this
document previously left blank at the one unit where it wrote "nothing detectable" without a number; the
caveat on that table said MG53 is "detected in a minority of cells at about 5 UMIs", reading a pseudobulk
profile's whole count over a median 1,217 cells as a per-cell figure, where a detected cell carries **1.12
to 1.18** UMIs and the detection rate is **1.3%** of an untreated line's cells (0.4% / 3.0% on plates 6 /
14, 7.5% / 10.0% under idarubicin), with detected cells **23% to 32%** more deeply sequenced — all three
quantities now computed per well set in `mdm2_mg53_single_cell.csv`, because understating them understates
this table's exposure to the depth confound; and unit 3's within-exposure wild-type interval was quoted as
"-0.139 to +0.019, compound-bootstrap p 0.13" where the committed table now reads **-0.143 to +0.020 at
p 0.12**, and the
bootstrap it comes from clusters on **cell line** — 17 of them, the wild-type arm — not on compound, which
is the unit-2 cluster. The two slips have different causes: the bootstrap seed was salted by Python's
per-process `hash()`, so the generator could not reproduce its own committed intervals and the prose drifted
from the table, while "compound" was simply the wrong word for a fit clustered on cell line. The seed is a
stable digest now and prose and table agree exactly, but every bootstrap bound and `p_boot` in this file is
a 2,000-draw Monte Carlo quantity (`n_boot_draws` in `models.csv`) whose third digit moves while the
cluster-robust p beside it does not, which is why no sentence above reads a result from which side of zero a
bootstrap bound falls on.
