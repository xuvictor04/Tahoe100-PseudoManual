---
type: finding
tags: [finding, mdm2, mg53, p53, plate-effects, reference-families, corrections]
status: current
---

# MDM2 and MG53

[[MDM2]] came out of the per-gene screen marked **"down with MG53"** — one of only eight of the 29 canonical
p53 effectors to clear the calibrated threshold, and the only one of [[p53 program P]]'s top three genes to
clear it at all. Condensed from `mg53_p53/findings/MDM2_MG53.md`, which carries every number here.

> [!summary] In one line
> Across five resolutions the association is **bounded and small, not demonstrably zero**: −3.2% to +3.4% per
> doubling of measured MG53 at the exposure level, −0.61% to −0.08% in the genome-wide screen, nothing
> detectable between untreated lines or between the MG53-positive and MG53-negative cells of one well.
> **Nothing about it looks p53-mediated.** The two largest-looking numbers — a −0.614 level correlation and a
> p 2.4e-06 genotype interaction — are a plate effect and an exposure confound.

## Why MDM2 is not just another effector

MDM2 sits on **both** sides of p53 ([[The p53 pathway]]): p53 induces it transcriptionally, and the MDM2
protein ubiquitinates p53 and sends it for degradation. It is a p53 **regulator** whose mRNA happens also to
be p53-responsive, so if MG53 moved MDM2 the reading would run *toward* p53 rather than away from it — the
one gene in the set where an association could speak to what regulates p53 instead of to what p53 does.
[[CDKN1A]], the contrast gene used throughout, is a readout of output only.

> [!tip] The positive control, and what it licenses
> MDM2 is well enough measured that nothing it fails to show is a detection problem on its side: 185.8 CPM
> (903rd of 16,643 by level — **not** the best-measured gene, see the corrections), detected in all 50 lines,
> moved up by 96 of 98 reference compounds, against [[MG53 (TRIM72)]]'s 5.89 CPM with 12.4% of profiles at
> zero ([[Why MG53 is hard to measure here]]). Per-line baselines then put MDM2 **3.07× higher in
> TP53-wild-type than TP53-altered lines** (17 vs 33 lines, geometric means, Welch p 3.3e-12; Mann-Whitney on
> medians 3.14×, p 1.8e-7) — the p53 → MDM2 feedback loop recovered from this very table — against MG53's
> **1.08×, p 0.77**. So MDM2's side of every null below is sound. It licenses **nothing** about MG53's
> reliability, separately poor at split-half 0.289–0.705 by subset: a null here is a null about the
> *association*, limited by the exposure, not the outcome.
> [`mg53_p53/findings/tables/mdm2_mg53_context.csv`]

## Five resolutions, and the two things called "level"

**LEVEL** is how much mRNA is present (pooled CPM per exposure, or a line's untreated baseline); **CHANGE** is
how far the gene moved under the drug (corrected log2 fold change). They do not behave alike, so every
contrast states which it bins.

| # | Unit | n | What varies |
|---|---|---|---|
| 1 | untreated baseline across lines | 48 lines | each line's own level of both |
| 2 | drug-dose, lines pooled | 1,132 exposures | what each exposure does |
| 3 | cell line × drug-dose | **843** cells | 18 MG53-raising exposures × 50 lines |
| 4 | the genome-wide screen | 53,084 cells | reported from the run, not recomputed |
| 5 | single cells in one well | up to 47 lines | MG53-detected vs undetected cells |

Unit 3 runs on 843, not the source table's 900 rows: MDM2 is present in 861 and MG53's corrected value in
843, so every contrast uses the 843 where both exist (305 wild-type, 538 altered). It exists only because one
pipeline step exported per-line values for five named genes over 18 exposures — which is also why unit 4 is
reported rather than recomputed.

## The headline: MG53 change against MDM2 change (unit 2)

Deciles of MG53's fold change over the 1,132 exposures, lines pooled; geometric mean is 2^(mean log2).

| MG53 decile | n | MG53 fold (median) | MDM2 geometric (95% CI) | CDKN1A geometric |
|---|---|---|---|---|
| 1 (lowest) | 114 | 0.65× | 1.002 (0.988–1.016) | 0.947 |
| 2 | 113 | 0.79× | 1.008 (0.996–1.021) | 0.988 |
| 3 | 113 | 0.87× | 1.012 (1.001–1.024) | 1.013 |
| 4 | 113 | 0.93× | 1.001 (0.991–1.011) | 0.995 |
| 5 | 113 | 0.98× | 1.013 (0.999–1.026) | 0.999 |
| 6 | 113 | 1.03× | 1.005 (0.993–1.016) | 0.997 |
| 7 | 113 | 1.09× | 1.001 (0.992–1.011) | 1.011 |
| 8 | 113 | 1.16× | 0.984 (0.968–1.002) | 1.016 |
| 9 | 113 | 1.28× | 0.989 (0.977–1.000) | 1.035 |
| 10 (highest) | 114 | 1.56× | 1.017 (0.982–1.052) | 1.080 |

[`mg53_p53/findings/tables/mdm2_mg53_bins.csv`]

**A flat line with two hairline exceptions.** Across a 2.4× span of MG53 the geometric mean stays within 2% of
1.00, the across-bin rank trend is −0.15, and the top decile sits *above* the bottom. Bins 3 and 9
(0.977–0.99996) exclude 1.00 by a hair; the top bin reads +3.5% arithmetic against +1.7% geometric, so "within
2%" is about the geometric mean only. These are what ten intervals look like when none means anything. The
contrast column, 0.947 → 1.080 climbing with the bins, is what tracking MG53 looks like.

The two correlations disagree, which is itself the finding: Spearman **−0.092** (p 0.0020, drug-bootstrap CI
−0.156 to −0.022, reproducing the run exactly) against Pearson **+0.003** on the same pairs, compound
bootstrap **−0.209 to +0.213**. Adjusting for transcriptome-wide activity gives partial Spearman **−0.019**,
p 0.45. Bound: **−3.2% to +3.4%** per doubling of measured MG53.
[`mg53_p53/findings/tables/mdm2_mg53_models.csv`]

## The −0.614 is a plate, in full (unit 2, LEVEL)

Binned on LEVEL instead, MDM2 falls 328.9 ± 4.4 → 252.1 ± 6.7 CPM as MG53's median rises 0.80 → 16.40 CPM:
Spearman **−0.614, p 5e-118**, read naively the strongest result in the study. It is a
[[Plate batch effects|plate batch effect]], and the decomposition says so outright:

| | Spearman |
|---|---|
| all 1,132 exposures together | **−0.614** |
| between plates (the 14 plate medians) | **−0.763** |
| within plate, pooled (plate medians removed) | **+0.074** |
| mean of the 13 per-plate correlations | **+0.087**, negative on only 2 plates |

[`mg53_p53/findings/tables/mdm2_mg53_cpm_by_plate.csv`]

MG53 carries a 3.12 log2 plate gap, the largest of all 16,656 genes, and all but one exposure sits on one or
two of the 14 plates (1,030 on one, 101 on two). Its plate medians run 0.86 → 14.05 CPM, a 16× spread with no
drug in it; MDM2's run the other way, 343 → 227. **Within a plate the relationship is weakly positive.**
Convention moves the magnitude, not the sign: dropping plate 6, which holds a single exposure, gives −0.791
between, and counting every plate an exposure appears on gives −0.793 between and **+0.031** within. Not
library collapse either — MG53's CPM is flat against UMI per cell, rho −0.013. Untreated baselines (unit 1)
agree with no drug involved: r **+0.08**, p 0.57, 95% interval **−0.21 to +0.36**, a weak bound excluding only
correlations above about 0.36.

## Same drug, same dose, two plates, opposite answers (unit 5)

Inside **one cell line, one well**, split cells by whether MG53 was detected and ask how much MDM2 each group
carries — a quasi-Poisson GLM per line (offset log UMIs; covariates log UMIs, S and G2M fractions, well
indicator), pooled by random effects, with **every non-p53 panel gene put through the same fit** to supply
78–85 control genes for the percentile ([[Placebo genes and reference families]]).

| Well set | TP53 | lines | MDM2 rate ratio | p | percentile among controls |
|---|---|---|---|---|---|
| **Idarubicin 5 µM, plate 14** | WT | 14 | **1.150** | **3e-6** | **84th (79)** |
| **Idarubicin 5 µM, plate 6** | WT | 15 | **0.941** | 0.20 | 15th (78) |
| Idarubicin 5 µM, both wells | WT | 16 | 1.043 | 0.18 | 65th (80) |
| DMSO, plates 6+14 | altered | 30 | **0.915** | **0.005** | **3.6th (84)** |
| DMSO, plates 6+14 | WT | 17 | 1.016 | 0.82 | 34th (85) |

[`mg53_p53/findings/tables/mdm2_mg53_single_cell.csv`]

**Read the first two rows together.** Same drug, same dose, same wild-type lines, two plates: plate 14 says
MDM2 is **15% higher** in MG53-positive cells at p 3e-6 and the 84th percentile of its controls; plate 6 says
**6% lower**. Pooled, +4.3%, p 0.18 — nothing. Either plate alone would have looked publishable, in opposite
directions, which is why nothing here rests on one well set. The one row consistent across its replicates is
untreated **TP53-altered** lines, 8.5% lower — the wrong arm for a p53 route, and the arms are not
distinguishable (WT − altered +0.105 ± 0.077, p 0.17). In those same cells CDKN1A moves the *other* way
(+20.8%, p 4e-5), and that split recurs at the drug-dose unit (+0.29 vs −0.08) and in the screen (+0.0104 vs
−0.0050): two genes p53 induces together moving apart at three resolutions argues against a p53 route.

## The genotype interaction: p 2.4e-06 raw, p 0.36 within exposure (unit 3)

MDM2 = a + b₁·MG53 + b₂·WT + b₃·(MG53 × WT), cluster-robust on cell line, 49 lines.

| Outcome | Fit | n | b, altered | b, wild-type | interaction (WT extra) | p |
|---|---|---|---|---|---|---|
| MDM2 | raw | 843 | −0.036 | −0.214 | **−0.178 ± 0.038** | **2.4e-06** |
| MDM2 | **within exposure** | 843 | −0.016 | −0.060 | **−0.045 ± 0.049** | **0.36** |
| *CDKN1A* | *raw* | 789 | *+0.141* | *−0.071* | *−0.212 ± 0.044* | *1.1e-06* |
| *CDKN1A* | *within exposure* | 789 | *+0.096* | *+0.100* | *+0.004 ± 0.066* | *0.95* |

[`mg53_p53/findings/tables/mdm2_mg53_genotype_interaction.csv`]

Fitted raw, MDM2's wild-type slope is **six times** the altered one — exactly what p53 dependence would look
like, and the strongest genotype signal in the source. **The contrast gene settles which reading is right.**
CDKN1A's raw interaction is just as significant and in the *same* direction, with its slope **changing sign
between arms**; fitted within exposure its two arms land on top of each other, +0.096 and +0.100, p 0.95. No
p53-mediated mechanism predicts a p53 effector's MG53 slope flipping sign in the lines that *have* p53. Both
raw interactions track which exposures the lines sat in — the drugs that raise MG53 most are not the drugs
that induce MDM2 most, and wild-type lines have more induction to lose. **The difference between p 2.4e-06 and
p 0.36 is a single fixed effect** ([[Two-way fixed effects]]).

One hint in this unit survives without clearing its accounting: among the 17 wild-type lines, mean rho
**−0.162** over the 18 exposures, p 0.005 under the pipeline's per-exposure shuffle but **p 0.036** under a
cell-line-label shuffle that keeps line-level structure in the null ([[Nulls and calibration]]) — rank 2 of
nine contrasts, **q ≈ 0.16**, per-exposure rhos from −0.65 to +0.31. Worth recording, not worth believing.

## The screen slope (unit 4)

Cell-line and drug-dose fixed effects, 53,084 cells, 47 lines ([[The screen model]]). All six covariate sets
land between **−0.0048 and −0.0060** log2 MDM2 per doubling of MG53, the readthrough-corrected one included,
so this is not [[Readthrough spillover]]: **−0.35%** per doubling (95% −0.61% to −0.08% line-clustered), or
**−0.5% to −1.2%** disattenuated depending on the split-half figure used
([[Reliability and disattenuation]]), against MDM2's own 0.46×–2.11× range. Its slope is the **smallest** of
the eight effectors with a verdict (0.0050 against BTG2's 0.0153) with the second-tightest SE of all 29
(0.00199): MDM2 is in that table because it is precise, not because it moved. The clearing mass of genes is
also **4.44× inflated** on the test-statistic scale, which deflates its t to −1.19, p ≈ 0.24
([[FDR calibration and the inflated null]]). [`mg53_p53/findings/tables/mdm2_mg53_screen.csv`]

## The reference family, which was wrong and is now right

The **16,642 tested genes** are selected for nothing. The **4,642 genes in the downstream export** are *not* a
sample: **4,500 are in the export because the screen had already called them significant against MG53 at
q < 0.1**, MDM2 among them, the other 142 being program members selected with the TP53 labels — hence that
family's median Spearman of +0.25 on LEVEL rather than 0, and only 36% of its genes negative.

| Family | Quantity | MDM2 | percentile | family median |
|---|---|---|---|---|
| **16,642 tested, unselected** | co-regulation r, raw | +0.005 | **36th** | +0.124 |
| **16,642 tested, unselected** | the same, 3 PCs removed | +0.034 | **60th** | −0.008 |
| 4,642 discovery set | CHANGE, Spearman | −0.080 | 26th | +0.053 |
| 4,642 discovery set | LEVEL, Spearman | −0.614 | 9th | +0.253 |
| *16,642, CDKN1A* | *co-regulation r, raw* | *+0.418* | *89th* | |

[`mg53_p53/findings/tables/mdm2_mg53_allgene_null.csv`]

**In the unselected family MDM2 sits at the 36th and 60th percentiles — the middle, twice over**, and the
correction strengthens the conclusion rather than weakening it; the contrast gene sits at the 89th. The
discovery-set ranks are ranks *inside* the selection ([[Cross-fitting and circularity]]), and the
9th-percentile LEVEL figure inherits the plate warning above.

## Corrections this note carries

Seven, recorded rather than quietly fixed, and listed in [[Corrections and retractions]]:

1. The reference family was called **"all genes"** when **97% of it was selected against MG53**.
2. MDM2 was called the **best-measured gene** here; it is **903rd of 16,643** by level.
3. Three Spearman correlations were quoted with their **OLS slope's p value**, one overstating significance by
   **nine orders of magnitude**.
4. The screen's WT-vs-altered equality was said to mean a p53-mediated effect **"cannot"** behave that way;
   the difference is −0.0006, CI −0.0100 to +0.0087, about **21% power** — p 0.89 is absence of power.
5. The per-doubling-of-**true**-MG53 figure was a point value, **−1.19%**, from the reliability subset that
   maximises it; the range is **−0.5% to −1.2%**.
6. The per-line **genotype interaction**, p 2.4e-06 raw, was **not reported at all**.
7. The unit-3 n was given as **861** where every contrast in it runs on **843**.

## What it adds up to

Bounded, small, and not p53-mediated — resting on the tests with power, not the screen's genotype comparison.
Partialling out p53 output makes the exposure-level correlation *more* negative, and the tilt lives in the
exposures that do **not** activate p53 (Spearman −0.119, p 9e-05), absent in the 50 that do (+0.048,
**p 0.74**). Consistent with [[Downstream of MG53]] and [[The measurement with controls]]. The limit is on the
MG53 side throughout, and [[Tahoe-100M]] has no MG53 perturbation, no protein measurement and one time point:
an absence here constrains the *association* and cannot rule out the protein-level link where TRIM72's known
biology mostly lives. Twelve tables back this note; see [[Tables — what the study produced]].
