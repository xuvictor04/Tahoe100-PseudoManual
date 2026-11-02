---
type: finding
tags: [finding, downstream, p53, mg53, per-gene, effect-size]
status: current
---

# Downstream of MG53

What MG53's level **does to p53 and to p53's output** — the regulatory direction, tested four ways at the
program level, then gene by gene across the whole of [[p53 program P]].

> [!summary] In one line
> In the TP53-wild-type lines the association is flat and bounded: nothing above roughly **0.4–0.6% of p53
> output per doubling of measured MG53** (about **1.3–2%** per doubling of true MG53) survives. The raw
> correlation is positive for every read-out and collapses the moment drug identity is removed, the small
> residual that remains lives in the **TP53-altered** lines rather than the wild-type ones, and signed per
> gene the program splits **35 toward more p53 output against 32 toward less**.

> [!warning] "Downstream" here is regulatory, never positional
> Downstream of MG53 = what its level does to p53 and p53's output. [[TRIM72]] also sits 10.6 kb **3' of**
> [[PYCARD-AS1]] and 17 kb **3' of** [[FUS]] on the same strand, so transcription running past them is
> counted as TRIM72 mRNA. That is [[Readthrough spillover]] — a fact about position and about the
> measurement — and it is never called downstream. It matters here only because it dilutes the exposure:
> see [[Why MG53 is hard to measure here]] and [[The TRIM72 locus]]. Whether p53 regulates MG53 is **out of
> scope** and no number below bears on it.

Two companion notes carry pieces of this and are not restated here: [[The measurement with controls]] for
the same question asked with a knockout-like control arm of ten p53-null lines, and [[MDM2 and MG53]] for
the one gene that got its own write-up.

## The four contrast structures, and where the signal goes

Table A fits the same MG53 → p53 relation in the **17 TP53-wild-type lines** under four nestings. `raw`
uses all variation; `within-line` removes each line's mean; `within-drug-dose` removes each drug-dose's
mean; `two-way` removes both ([[Two-way fixed effects]]). Slopes are log2 of the read-out per doubling of
measured MG53, intervals 95% with cell-line-clustered SEs, 19,232 line × drug-dose rows.

| p53 read-out | basis | raw r | within-line | within-drug-dose | two-way r | two-way slope (95% CI) |
|---|---|---|---|---|---|---|
| data-defined program P (180 genes) | data-defined | +0.091 | +0.093 | +0.009 | +0.013 | +0.0009 (−0.0014, +0.0032) |
| data-defined repression arm (15 genes) | data-defined | +0.015 | +0.017 | −0.002 | +0.000 | +0.0000 (−0.0072, +0.0073) |
| CollecTRI TP53 targets (612 genes) | list-based | +0.194 | +0.197 | +0.068 | +0.074 | **+0.0029 (+0.0006, +0.0051)** |
| curated 21-gene P53_ACTIVITY | list-based | +0.074 | +0.075 | −0.008 | −0.007 | −0.0011 (−0.0050, +0.0029) |
| curated p53 primary targets | list-based | +0.031 | +0.031 | −0.019 | −0.018 | −0.0039 (−0.0092, +0.0014) |
| curated p53 all targets | list-based | +0.047 | +0.048 | −0.021 | −0.020 | −0.0036 (−0.0080, +0.0007) |

[`mg53_p53/findings/tables/tableA_wt_p53_targets.csv`]

**The collapse is caused by the drug, not by the line.** Removing cell-line means changes nothing — program
P goes +0.091 → +0.093, CollecTRI +0.194 → +0.197 — while removing drug-dose means takes program P to
+0.009 and CollecTRI to +0.068. Adding the line effect on top of the drug-dose effect then does almost
nothing more. So the raw positive correlation is **drugs that move MG53 and p53 targets together**: a
compound that stresses the cell raises readthrough into the TRIM72 locus and activates p53 in the same
wells, and any exposure with that property will correlate with any stress-responsive outcome. Only the
two-way column is a statement about MG53.

Three readings the table forces:

- The **data-defined** read-out is flat at every nesting. Its two-way interval, ±0.002 log2, is the
  tightest in the table.
- The **only interval that excludes zero is positive**, not negative: CollecTRI's +0.0029 (+0.0006,
  +0.0051). If MG53 damped p53 output, this is the row that should have gone the other way.
- For the two curated target sets the **correlation** interval sits below zero (−0.032 to −0.003 and −0.034
  to −0.006) while the **slope** interval spans it. Table A's direction column is decided on the slope, and
  both of those read "none". Neither the CollecTRI positive nor the curated negatives were put through the
  label-permutation and placebo machinery the pipeline applies to its primary test; both rest on
  cell-line-clustered SEs with 17 lines, and neither is reported as a finding
  [`mg53_p53/findings/MG53_p53_TABLES.md`, "Caveats that apply to all three tables"].

## The bound in TP53-wild-type lines

The declared test is list-free: program P against measured TRIM72, with (drug-dose × TP53-group) and line
fixed effects, 17 WT and 30 altered lines, 53,084 rows.

| Quantity | Value | Source |
|---|---|---|
| slope in WT lines | **+0.00040 log2** per doubling (p 0.744) | [`genome_wide/tables/c_program_models.csv`, row 0] |
| slope in altered lines | **+0.00223** (two-way p 0.067) | same |
| WT − altered | **−0.00183 (95% CI −0.00523 to +0.00158)**; two-way p 0.285, TP53-label permutation p 0.304, Holm over 6 covariate sets 1.0 | same |
| smallest detectable difference, 80% power | **0.0059 log2 ≈ 0.4%** per doubling of measured TRIM72; ≈ 9% of the program's residual SD per SD of TRIM72 | same, `mde_diff_80` |
| the same bound per doubling of **true** TRIM72 | **≈ 0.020 log2 ≈ 1.4%** (0.00592 ÷ split-half reliability 0.289) | recomputed; reliability [`two_way/tables/key_results.csv` row 184] |

The WT-only fit of Table A agrees with the joint model's WT arm: +0.0009 (−0.0014, +0.0032) on 19,232 rows
against +0.00040 on 53,084. The WT − altered difference is stable across covariate sets (−0.0015 to
−0.0023) and across fold programs (−0.0016 to −0.0024); the **component** slopes are not, which is why the
difference and not the arm is the declared quantity (with three genome-wide components as covariates
b_WT becomes −0.00248, p 0.031; with drug-dose-only fixed effects the difference flips to +0.00262, p 0.47)
[`c_program_models.csv` rows 1–6, 15–19].

**Why the small p-values in that same row are not the test.** The row also carries p 0.046 with
drug-dose-clustered errors only and p 0.027 from shuffling TRIM72 within drug-doses. Neither allows for
each line keeping its genotype across all 1,132 drug-doses, so neither is declared, and the
[[Placebo genes and reference families]] show why: 100 response-matched and 100 expression-matched genes put
in TRIM72's place give **median WT − altered t of −1.59 and −1.46**, with 88% and 92% of them negative.
TRIM72's −1.08 sits at the **69th and 64th percentile** (empirical p 0.733 and 0.653) — less negative than
the typical placebo. Any gene that tracks drug sensitivity looks faintly "WT-specific" against a response
only WT lines can make, so the analytic p is uncalibrated and the null rests on the label permutation and
the placebos [`c_program_models.csv` row 0; `genome_wide/tables/c_placebos.csv`]. See
[[FDR calibration and the inflated null]] and [[Nulls and calibration]].

The list-based tests agree on the main point and add leans in both directions that the data-defined program
does not share:

| Test | Estimate | Reading |
|---|---|---|
| 21-gene P53_SCORE, all drug-doses | WT − altered **−0.00317 (−0.00849, +0.00216)**, p 0.238, label permutation 0.258; detectable 0.0093 measured, 0.0321 true | null |
| the same 21 genes against 500 random 21-gene modules | t −1.20 against mean +0.20 (SD 0.62), empirical p 0.040 | a small negative lean specific to the list |
| the same 21 genes, camera set test | difference p 0.300 (0.032 if genes are treated as independent) | null once gene correlation is allowed for |
| program P, same set test | mean t −0.03 against −0.11 for other genes, p 0.77 | no lean |
| CollecTRI TP53 regulon activity, within lines | r −0.060 (q 0.005); WT − altered q 0.97 | real but not genotype-dependent |
| mean of 612 CollecTRI TP53 targets | common slope **+0.0030** (p 0.0013); difference −0.00085 (p 0.60) | opposite sign to the row above; not genotype-dependent |

[`two_way/tables/key_results.csv` rows 0, 140; `genome_wide/tables/key_results.csv` rows 26, 30–31;
`summary/T11_upstream_TF_activity.csv`; `genome_wide/tables/c_program_models.csv` row 74]

Taking the two scales together gives the vault's headline range: effects above roughly **0.4–0.6% per
doubling of measured MG53**, about **1.3–2% of true MG53**, are excluded
[`mg53_p53/findings/README.md`, "The short answer"]. The bound on **p53-driven arrest** is the same
quantity: p21's own slope is positive and tiny (below), and the arrest effectors in the curated list behave
like the rest of the program — see [[The p21-DREAM axis]].

## The residual is in the altered lines, not the wild-type ones

Everything that looks like an association sits where p53 cannot act on it.

- The joint model's two arms: WT **+0.00040** (p 0.744) against altered **+0.00223** (p 0.067). The WT arm
  is the flat one.
- Split the altered lines by how much p53 output they retain ([[Per-line p53 function]]; activity = each
  line's mean program-P induction under the p53-activating drug-doses, against a truncating/splice/deletion
  null median of +0.0038 and a wild-type median of +0.1474):

| Split | Group | Lines | two-way r (95% CI) | slope (95% CI) | direction |
|---|---|---|---|---|---|
| data-defined inducibility | WT (functional p53) | 17 | +0.013 (−0.002, +0.027) | +0.0009 (−0.0014, +0.0032) | none |
| | altered, **higher** activity | 18 | +0.024 (+0.010, +0.038) | +0.0010 (−0.0010, +0.0030) | none |
| | altered, **lower** activity (at/below null) | 14 | +0.085 (+0.068, +0.101) | **+0.0043 (+0.0004, +0.0082)** | positive |
| gene-panel functional call (list-based) | responsive | 11 | +0.021 | +0.0014 (−0.0015, +0.0043) | none |
| | unresponsive | 28 | +0.058 | **+0.0026 (+0.0001, +0.0052)** | positive |
| | uncertain | 9 | −0.009 | −0.0006 (−0.0025, +0.0013) | none |

[`mg53_p53/findings/tables/tableC_mutants_by_activity.csv`, per-line values in
`tables/per_line_p53_activity.csv`]

**The gradient runs the wrong way for anything mediated by p53.** The association is largest in the mutants
with the *least* p53 activity, absent in the wild-type lines and in the higher-activity mutants, and
positive in sign. An effect working through p53 cannot be strongest in cells with the least functional p53.
Both of those intervals only just exclude zero, on 14 and 28 lines, and would not be expected to survive
the label-permutation and placebo machinery; they are not reported as findings either. The reading is the
readthrough / stress-amplitude confound, which the control-arm design in
[[The measurement with controls]] tests directly and reaches the same verdict on.

The per-gene screen tells the same story at its extreme. The gene with the most extreme nominal `p_diff` in
the whole program, [[INKA2]] at 1.9e−03, has its difference carried by the **altered** arm (`b_alt` +0.0202,
p 0.0043; `b_WT` −0.0046, p 0.39) — the wrong arm for anything MG53 does to p53's output
[`genome_wide/tables/c_screen_genes.csv.gz`].

### Does a line's MG53 level predict its p53 activity?

No, in any group. Spearman rho across lines:

| MG53 level vs | all (49) | altered (32) | WT (17) |
|---|---|---|---|
| data-defined inducibility | −0.125 (p 0.39) | −0.206 (p 0.26) | −0.186 (p 0.47) |
| panel responsiveness | +0.013 (p 0.93) | +0.009 (p 0.96) | −0.025 (p 0.93) |
| basal p53 activity | −0.014 (p 0.93) | +0.007 (p 0.97) | −0.282 (p 0.27) |

[`mg53_p53/findings/MG53_p53_TABLES.md`, Table C; `tables/per_line_p53_activity.csv`]

## Per gene, signed by the direction p53 moves it

A gene's MG53 slope is in **that gene's own units**, and "up with MG53" means more p53 output for a
p53-induced gene and *less* for a p53-repressed one. Only the signed version can be added across genes;
that is the whole point of [[Signing genes by p53 direction]].

| Direction p53 moves the gene | genes | with a verdict | toward MORE p53 output | toward LESS | direction mixed | membership unstable |
|---|---|---|---|---|---|---|
| induced by p53 (arm P) | 180 | 62 | **32** | **30** | 63 | 43 |
| repressed by p53 (arm P-down) | 15 | 5 | **3** | **2** | 2 | 2 |
| **all 195 program genes** | 195 | **67** | **35** | **32** | 65 | 45 |
| *the 29 canonical effectors* | *29* | *8* | *5* | *3* | *11* | *3* |

[`mg53_p53/findings/tables/tableD_signed_tally.csv`; per-gene rows
`tables/tableD_p53_target_genes.csv` (195 rows), `tables/p53_effectors_per_gene.csv` (29 rows)]

**35 against 32.** A coherent change in p53 output would push the two arms in opposite *gene-level*
directions and so land almost entirely on one side of this split. It lands on both sides equally, in the
full program and in the curated effector list alike. The unsigned tally — "34 positive, 33 negative" — hides
that three of those positives are repressed genes moving the p53-output score the other way.

Three further facts make the 67 a background number rather than a result:

- **It *is* the background rate.** 67 of 195 pass the exposure-shuffle `q_xperm_common` < 0.1 (34.4%)
  against 5,746 of 16,642 tested genes genome-wide (34.5%); 53 of 195 pass the analytic `q_common` (27.2%)
  against 27.04%. What differs is sign and size: the 4,447 non-program hits are **71.7% positive** with a
  median |b_common| of **0.0153**, while the program's hits split 24/29 with a median of **0.0037**
  [`c_screen_genes.csv.gz`; recomputed].
- **The two most canonical effectors point opposite ways.** [[CDKN1A]] (p21) **+0.0104** log2 per doubling
  (`q_common` 0.031, xperm 0.0089) = **+0.72% of p21 per doubling of MG53**, and [[MDM2]] **−0.0050**
  (q 0.069, xperm 0.031) = −0.35% — the largest p53-activation fold change in the program moving the other
  way from p21. Eight of the 29 effectors clear the threshold, five positive ([[CDKN1A]], [[PMAIP1]],
  [[AEN]], [[ACER2]], [[BTG2]]) and three negative ([[MDM2]], [[DDB2]], [[TP53I3]]) — 28% against the 27%
  base rate, signs split both ways. MDM2's own interval and plate decomposition are in [[MDM2 and MG53]].
- **The placebo percentiles are extreme in both directions at once.** Positive end CDKN1A 0.9/1.0, PMAIP1
  1.0/1.0, AEN 1.0/1.0, BTG2 1.0/1.0; negative end MDM2 0.1/0.0, DDB2 0.1/0.0, TP53I3 0.0/0.0. Resolution
  is 0.1 because each family holds only 10 placebo exposures, so a 0.0 or 1.0 means "most extreme of ten"
  and supports nothing alone — but the *pattern* across the 29 is the signature of MG53 tracking overall
  transcriptional response amplitude, which makes it a better predictor than a random matched gene for any
  responsive gene, in whichever direction that gene happens to go.

Two cautions that belong with the tally rather than against it. **Direction is often not a fact about the
gene**: `frac_compounds_wt_up` puts **65 of 195** program genes and **11 of the 29** effectors between 0.35
and 0.65 — [[BAX]] at 0.541 among them. And **program membership is unstable without tracking the verdict**:
of the 67 genes with a verdict, 20 were re-selected in 0 or 1 of the 5 cross-fitting folds, and those 20
split 11 toward less output against 9 toward more — the same even split as the stable genes
([[Cross-fitting and circularity]]). The largest slopes in the program, [[GRIN2C]] (+0.0511) and
[[ENSG00000285901]] (+0.0351), sit on genes of 2.1 and 4.7 CPM, where |b_common| is largest genome-wide for
reasons of expression alone (median |b_common| by CPM bin: 0.0140 below 1 CPM, 0.0027 above 64).

### Not one gene differs by TP53 status

**0 of 195 program genes — and 0 of all 16,642 tested genes — reach `q_diff` < 0.1 or `q_label_diff` < 0.1.**
This is the genotype contrast, the one that would have to move for a wild-type-specific MG53 → p53 effect.

- `q_diff` cannot even rank genes: 194 of the 195 sit at its floor of 0.99879, which is a real BH value and
  not a missing one, so "none" means nowhere near significance rather than "untested".
- Genome-wide the statistic is slightly **deflated** (lambda 0.963; 5 genes at p < 0.001 against 16.6
  expected) [`c_screen_genes.csv.gz`; `genome_wide/tables/key_results.csv` row 24].
- **No gene reaches its own detection bound.** A lone discovery at `q_diff` < 0.1 needs p ≤ 0.1/16,642, i.e.
  |t| ≥ 5.11 at the median df of 46; with a median `se_diff` of 0.0048 that is **|diff| ≥ 0.029 log2 = +2.0%
  in the gene per doubling of measured MG53**, or **+7.1% per doubling of true MG53**. The largest |diff| in
  the table is 0.035 and 0 of 195 clear their own 80% threshold (13 exceed the much weaker 1.96 × se). For
  the common slope the same bound is +1.0% measured / +3.7% true.
- For scale: that true-MG53 bound is **1.43× the median program gene's entire wild-type-minus-altered
  genotype effect** (0.070 log2). MG53 would have to move a p53 target by more than TP53 genotype itself
  does for this screen to have seen it [`c_screen_genes.csv.gz`, `se_diff`/`se_common`/`df`;
  `two_way/tables/trim72_reliability.csv`; recomputed]. See [[Reliability and disattenuation]].
- The design is also smaller per gene than the row count suggests: after pruning, the 195 genes contribute
  **11 to 17 wild-type** and 22 to 30 altered lines (median 17 and 30, df median 46), not the panel's 17 and
  33.

## What MG53's residual variation tracks instead

Within drug-doses, 4,500 of 16,642 genes have a common MG53 slope at q < 0.1 (3,213 positive) — but
response-matched placebo exposures give 897–5,344 such genes (median 3,196) and expression-matched placebos
a median of 5,330, with genome-wide inflation lambda 4.44 for MG53 against 4.69 and 5.52 for the placebos.
MG53 sits **inside** the placebo range [`genome_wide/tables/c_calibration.csv`].

The partners are not p53 genes. Of the 100 largest |b_common| in the screen, **none is a program member**,
all 100 slopes are positive (0.062 to 0.143), median expression is 2.77 CPM against the program's 54.19,
and **61 of 100 carry readthrough spillover geometry** against 4.218% genome-wide — still a **6.4×**
enrichment among genes at or below the list's own 75th-percentile expression, so not an expression artefact
[`mg53_p53/findings/tables/tableD_top_mg53_partners.csv`; `c_screen_genes.csv.gz`, `dog_class`; recomputed].
The top of that list is [[ENSG00000283573]] (+0.1431), [[FNDC7]] (+0.1408) and [[SEMA4A]] (+0.1325). In the
other direction, only **2 of 195** program genes carry that geometry at all ([[MIR3659HG]] and [[RRM2B]]),
so the program is not itself a readthrough list. Each line's MG53 therefore tracks that line's general
readthrough tendency and its overall response amplitude — see [[Readthrough spillover]] and
[[Upstream of MG53]].

Also null at program level: 49 of 50 atlas programs track MG53 across drug-doses (drug co-response), 25 do
within lines (21 positive), and **none differs by genotype** (smallest q 0.99)
[`genome_wide/tables/d_program_vs_exposure.csv`].

## Single cells

Single-cell tests use the 116-gene panel and a detected / not-detected exposure — MG53 is detected in only
**1.7–3.0%** of cells — so they answer a coarser question, and they agree.

- WT − altered log rate ratio **+0.041 (CI −0.030 to +0.111), p 0.24** [`single_cell_all/tables/key_results.csv`
  row 4].
- MG53-detected cells carry **9.1% more** p53-score mRNA in WT lines (rate ratio 1.091, p 0.015) and 4.8%
  more in altered lines, plus more [[ATF3]] (1.38× and 1.35×) — co-induction in the same stressed cells, not
  suppression [`summary/T10_single_cell_all_wells.csv`].
- Split by p53 *function* rather than genotype (post hoc): **+0.081** (functional-label permutation p 0.010),
  MDM2 +0.110, i.e. *more* p53-target mRNA in the responsive lines — the opposite of suppression
  [`single_cell_all/tables/p53_functional_status_contrasts.csv` rows 12–19].

## Subsets of active drug-doses: the negative numbers, and why they are not robust

The only place a negative WT-specific slope appears is in subsets restricted to drug-doses where MG53 moves
or p53 is driven. They do not hold up:

| Subset | Estimate | What breaks it |
|---|---|---|
| 22 drug-doses with \|DD_z\| ≥ 3 (chosen on the exposure, not the outcome) | **−0.0336 (−0.0605, −0.0067)**, p 0.0175, label permutation 0.010 | Holm over the 4 subsets gives 0.040 / 0.070 [`c_program_models.csv` rows 7–9] |
| two_way's 62 active drug-doses | **−0.0300**, p 0.015 | Holm over variants 0.121 / 0.144; with line effects estimated from all drug-doses the slope falls to −0.0178 (p 0.22) [`two_way/tables/key_results.csv` rows 43, 126–128] |
| a plain re-fit of the same 22 | −0.0155 | carried by a **positive altered** slope (+0.0137), not a negative WT slope (−0.0018) [recomputed from `export/TRIM72/TRIM72_per_drugdose_line.csv`, `export/downstream/program_scores_per_drugdose_line.csv`] |

And the 22 **mix two opposite 24 h p53 states**: 14 have a higher p53 program in WT (the DNA-damage drugs —
idarubicin 0.5 µM +0.66 log2, doxorubicin 5 µM +0.49, idarubicin 5 µM +0.37) and 8 have a lower one
(transcription or translation inhibitors under which short-lived p53-target mRNAs fall — auranofin 5 µM
−0.29, dinaciclib 5 µM −0.28, panobinostat 5 µM −0.26) [`genome_wide/tables/b_drugdose_p53_activation.csv`,
`program_P_delta_log2`]. Pooling the two kinds can produce a negative slope by itself, and placebo genes give
negative differences in these subsets too. Whether these are small real effects below the 1–2% bound or the
product of that pooling is listed among the open questions.

## Corrections recorded

- **The "> 1.2% excluded" bound was the wrong scale.** `SUMMARY.md` under "Does more TRIM72 go with less p53
  output?" says a fall of more than 1.2% per doubling is excluded. That bound comes from **single cells**
  with a detected / not-detected exposure. The pseudobulk bounds apply to **measured** MG53, and for true
  MG53 they widen about 3.5× (two_way 0.0093 → 0.0321 log2). Quote 0.4–0.6% measured / 1.3–2% true
  [`two_way/tables/key_results.csv` row 0].
- **[[FDXR]] was the one negative lean in the earlier list-based work, and it is not credible per gene.**
  List-based: −0.0215 (CI −0.0376 to −0.0055; p 0.0098; label permutation 0.0075; q_label 0.067)
  [`two_way/tables/key_results.csv` row 34]. Per gene in the screen: `diff` −0.0213 (se 0.0083, nominal
  p_diff 0.0135) but `q_diff` and `q_label_diff` both 0.999; the common slope is flat (+0.0025, q 0.75); the
  effect halves to −0.0101 and the nominal p collapses to 0.111 when three response principal components are
  added; its placebo percentiles are 0.1 and 0.0, i.e. 9 and 10 of 10 matched placebos give a *lower* t; and
  |diff| is **2.3× below FDXR's own 80%-power bound of 0.0495**. One gene of 195 at nominal p 0.013 is what
  the second-smallest of 195 tests gives. As a p53 target FDXR is impeccable (1.237× in WT lines,
  `wt_minus_alt_log2` +0.314, kept by all 5 folds and all 98 leave-one-compound-out programs); as an MG53
  result it is not.
- **Three intervals in the control-arm measurement no longer exclude zero** under conservative inference.
  Those belong to [[The measurement with controls]] and are listed there; see also
  [[Corrections and retractions]].

## What this cannot say

- **Association, not perturbation.** [[Tahoe-100M]] contains no MG53 perturbation and no protein data, so no
  slope here separates MG53 changing a p53 target from the two moving together, and the direction of
  causation is not identified. MG53 acts largely post-translationally; the exposure is a transcript count.
- **No line carries an MG53 alteration.** All 50 are wild-type for TRIM72 and differ only in level (0.93 to
  23.6 CPM, median 5.9), so nothing contrasts functional with non-functional MG53.
- **The exposure is partly not MG53.** Part of the measured signal is [[Readthrough spillover]] rather than
  MG53's own transcript, which dilutes the exposure in every table above; median 5 UMIs per profile and a
  split-half reliability of 0.289 do the rest.
- **The effective sample is 11 to 17 lines, not 50 and not 53,000 rows.** 33 of 50 lines carry a TP53 driver
  mutation, only 11 of 50 are functionally responsive, and the altered lines retain roughly 5% of the
  wild-type response (median responsiveness 0.948 against 0.256, 3.7×, Mann-Whitney p 3.1e−07 on the
  genotype-blind ranking). Two-thirds of the panel contributes a floor of near-zero p53 output that cannot
  move in either direction [`mg53_p53/findings/tables/p53_nullification.csv`] — see
  [[p53 nullification in cancer cell lines]] and [[Per-line p53 function]].
- **24 h only.** Nothing here speaks to effects before 24 h, to p53 protein, or to anything below the bound.
  Program P's mean averages short-lived targets ([[MDM2]], [[CDKN1A]]) with longer-lived ones ([[FDXR]],
  [[DDB2]]) [[p53 program P]].
- **Arrest and death are not directly measured.** The per-line composition shift does not track surviving
  cell counts (r −0.01) and the atlas corrects composition out by design, so "no p53-driven arrest" is a
  statement about arrest-gene mRNA, not about cell counts.
- **Program P's own weak spots** apply to the read-out: its TP53 specificity is partly circular, in 23 of 44
  selected drug-doses a non-TP53 grouping (mostly organ) explains the WT-vs-altered divergence better, and
  the repression arm fell back to a top-25 list in 4 of 5 folds. See [[Program P derivation]] and
  [[Plate batch effects]] for what else the design absorbs.

## Links

- **Findings:** [[What this study found]], [[The measurement with controls]], [[MDM2 and MG53]],
  [[Upstream of MG53]], [[Why MG53 is hard to measure here]], [[p53 nullification in cancer cell lines]],
  [[Corrections and retractions]]
- **Concepts:** [[p53 program P]], [[The p53 pathway]], [[The p21-DREAM axis]], [[MG53 (TRIM72)]],
  [[Readthrough spillover]], [[The TRIM72 locus]], [[Signing genes by p53 direction]], [[Tahoe-100M]]
- **Methods:** [[Two-way fixed effects]], [[Reliability and disattenuation]],
  [[Placebo genes and reference families]], [[FDR calibration and the inflated null]],
  [[Cross-fitting and circularity]], [[Nulls and calibration]], [[Program P derivation]],
  [[Per-line p53 function]], [[The screen model]], [[How the numbers are decided]]
- **Indexes:** [[Home]], [[Genes — Map of Content]], [[Tables — what the study produced]]

## Sources

Paths beginning `mg53_p53/findings/` are in the repository; all other paths are relative to a completed
run's results folder (`~/Tahoe-100M/mg53_p53` by default). "recomputed" marks a number derived from the
table named rather than printed in it.

- **Table A, the four contrast structures:** `mg53_p53/findings/tables/tableA_wt_p53_targets.csv`
  (6 read-outs × `r_raw` / `r_within_line` / `r_within_drugdose` / `r_twoway` / `slope_twoway` with
  `slope_lo`/`slope_hi`, 19,232 rows, 17 lines)
- **Table C, mutants by retained p53 activity:**
  `mg53_p53/findings/tables/tableC_mutants_by_activity.csv`, with
  `tables/per_line_p53_activity.csv` and `tables/p53_nullification.csv`
- **Signed per-gene tally:** `mg53_p53/findings/tables/tableD_signed_tally.csv`,
  `tables/p53_effectors_signed_tally.csv`; per-gene rows `tables/tableD_p53_target_genes.csv` (195 genes,
  67 columns) and `tables/p53_effectors_per_gene.csv` (29 canonical effectors); contrast list
  `tables/tableD_top_mg53_partners.csv`
- **Prose and caveats:** `mg53_p53/findings/MG53_p53_TABLES.md` (Tables A and C, the p53-nullification
  section, the full-program and signed-tally sections), `mg53_p53/findings/FINDINGS.md`
  ("Downstream: what goes with more TRIM72", "Reading the 24 h snapshot"),
  `mg53_p53/findings/README.md` ("The short answer", "Per-gene tables")
- **Primary list-free test, placebos and calibration:** `genome_wide/tables/c_program_models.csv` (row 0 and
  rows 1–9, 15–19, 74), `c_placebos.csv`, `c_calibration.csv`, `c_screen_genes.csv.gz`,
  `key_results.csv`, `b_drugdose_p53_activation.csv`, `d_program_vs_exposure.csv`
- **List-based tests and reliability:** `two_way/tables/key_results.csv` (rows 0, 34, 43, 126–128, 140, 184),
  `two_way/tables/trim72_reliability.csv`
- **Single cells:** `single_cell_all/tables/key_results.csv`,
  `single_cell_all/tables/p53_functional_status_contrasts.csv`, `summary/T10_single_cell_all_wells.csv`,
  `summary/T11_upstream_TF_activity.csv`
- **Per-line exposure and program scores:** `export/TRIM72/TRIM72_per_drugdose_line.csv`,
  `export/downstream/program_scores_per_drugdose_line.csv`, `export/downstream/program_flags.csv`
- **Regenerate every findings-table number:** `python3 mg53_p53/findings/make_tables.py --results
  ~/Tahoe-100M/mg53_p53`
