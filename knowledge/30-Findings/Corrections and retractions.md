---
type: finding
tags: [finding, corrections, retractions, provenance, honesty, inference]
status: current
---

# Corrections and retractions

This is the vault's honesty ledger. It lists every number in the committed write-ups under
`mg53_p53/findings/` that the two later analysis documents contradict, with both values side by side.

Nothing here is softened, and nothing is removed from the record. Where a published number was wrong, the
published number stays on the page next to its replacement, because a reader who finds the committed text
elsewhere in the repository needs to be able to recognise it.

> [!warning] Two mechanisms produce almost every row below
> **Inference, not arithmetic.** The pipeline's arithmetic reproduces: pooled fold changes match to
> 1e-4, `DD_lfc` to 5e-6, `DD_z` exactly, and the recomputed arm slopes agree with the committed ones to
> 1e-18. What changed is the standard error, the null, the multiplicity family and the reference class.
> The committed intervals use a CR0 standard error clustered on cell line with a 1.96 multiplier, over 6 to
> 28 clusters; the replacements use a per-arm CR1 factor, a conservative two-way (drug, line) cluster, and
> a *t* on min(drugs, lines) − 1 degrees of freedom. The controlled-measurement document states the
> committed construction was **12–58% too narrow**.
> **The disattenuation divisor.** Every "per doubling of true MG53" figure in the committed text divides a
> same-well slope by a split-half reliability of 0.289. Both new documents reject that: the divisor is
> wrong (it is group-specific, 0.301 and 0.283) and the division is the wrong *kind* of correction, because
> exposure and outcome are counted from the same cells in the same well against the same total-UMI
> denominator. See [[Reliability and disattenuation]].
> **Output that was never opened.** The eight **R** rows at the foot of the table have a third mechanism and
> no arithmetic in it at all. Every headline number of `MDM2_MG53.md` reproduced; what failed was provenance
> — three statements false as written, an exposure set misdescribed, and four pieces of the run's own output
> never read, among them the 70-exposure panel that retires the one row that document nominated for
> follow-up. The conclusions did not move.

**Source tags used in the table.** **M** = the controlled-measurement document, written up in this vault as
[[The measurement with controls]]. **U** = the upstream document, written up as [[Upstream of MG53]], whose
own §8 carries the fuller list including claims that never reached the committed files. **R** = the
five-lens adversarial review of `MDM2_MG53.md`, applied in that document and condensed in
[[MDM2 and MG53]]; its section pointers are to `MDM2_MG53.md` itself. Section pointers are otherwise to the
M and U documents. "Committed" paths are relative to `mg53_p53/findings/`; run-output paths
(`downstream_p53/`, `p53_dependence/`, `single_cell_all/`) are relative to the run tree.

---

## Corrections to the committed write-ups

| Claim as published (and where) | Corrected value | Corrected by | Why the new number is the right one |
|---|---|---|---|
| p53-null control arm D, p53-activating drug-doses: **+0.225% (CI +0.007 to +0.443)** — an interval that **excludes zero** [`README.md`, "The measurement…"; `tables/mg53_to_p53_effect.csv`, row `p53-activating / D`] | **+0.225% (−0.103, +0.553)** — includes zero. Within-drug-dose shuffle p 0.059, whole-line permutation p 0.055 | M, main table | A more conservative standard error: the per-arm CR1 factor and the two-way (drug, line) cluster on a *t* with min(drugs, lines) − 1 df, in place of a CR0 cell-line SE times 1.96 on 10 clusters |
| Low-activity mutant arm C, p53-activating: **+0.430% (CI +0.048 to +0.814)**, excludes zero [`README.md`; `tables/mg53_to_p53_effect.csv`] | **+0.430% (−0.091, +0.954)**. Shuffle p 0.0005, whole-line permutation p 0.030 | M, main table | Same standard error. Note the finding itself survives on the calibrated null — all drug-doses give whole-line p 0.0010, Holm 0.008 over the pre-specified family of 10, wild cluster bootstrap p 0.038 with an interval excluding zero — so it is the inference that changed, not the result |
| Arm C, all drug-doses: **+0.304% (+0.022, +0.587)**, excludes zero [`tables/mg53_to_p53_effect.csv`, row `all drug-doses / C`; not quoted in the README prose] | **+0.304% (−0.022, +0.632)** | M, main table | Same standard error |
| Arm A (functional p53), all drug-doses — the study's headline: **+0.095% (95% CI −0.11% to +0.30%)** [`README.md`; CSV gives −0.10713, +0.29780] | **+0.095% (−0.161%, +0.352%)**. Two-way p 0.427, whole-line permutation p 0.387, restricted wild cluster bootstrap p 0.394 (CI −0.00243 to +0.00517) | M, headline and main table | Same standard error. The point estimate is unchanged (+0.00137 log2) because the fixed effects are now absorbed exactly rather than by iterated demeaning — the two fits agree to 1e-18, so this is a reproduction of the estimate and a replacement of its interval |
| Knockout-controlled contrast A − D, all drug-doses: **+0.050% (−0.163 to +0.264)** [`README.md`; CSV] | **+0.050% (−0.194, +0.295)**. Two-way p 0.672, whole-line permutation p 0.665, wild cluster bootstrap p 0.666 (CI −0.00300 to +0.00445) | M, "The knockout-controlled contrast A − D" | The contrast is now fitted **jointly**, with (drug-dose × arm) fixed-effect cells and arm-specific slopes, so its covariance is correct under drug clustering. The committed interval came from `hypot` of two separate SEs, which is valid only under cell-line clustering — where the arms share no line and the covariance is exactly zero |
| Arm A, p53-activating: **−0.123%**, quoted with no interval [`README.md`; CSV gives −0.565, +0.321] | **−0.123% (−0.857, +0.616)**, MDE80 +1.034% | M, main table | Same standard error; and an interval belongs on the number, since the committed text leans on the comparison with arm D |
| Contrast A − D, p53-activating: **−0.347% (−0.838, +0.146)** [`tables/mg53_to_p53_effect.csv`] | **−0.347% (−1.014, +0.324)**. Two-way p 0.293, whole-line permutation p 0.392 | M, main table | Joint fit plus the conservative two-way cluster, as above |
| Arm B (TP53-WT, damped), all drug-doses: **−0.091% (−0.197, +0.016)** [`tables/mg53_to_p53_effect.csv`] | **−0.091% (−0.346, +0.165)** | M, main table | Same standard error. This is the largest widening in the table — 6 cell-line clusters, *t*(5) = 2.571 in place of 1.96 |
| "the arm could have detected **0.29%**" — the study's stated power [`README.md`; CSV `mde_pct` 0.28958] | **+0.357%** at 80% power (+0.322% with the normal multiplier), i.e. 3.0% of the +0.1704 log2 (+12.5%) p53 response the same arm shows to a p53-activating drug-dose | M, headline and main table | The few-cluster multiplier *t*(.975, df) + *t*(.80, df) = 3.11 at df 10 replaces the normal 2.8016, applied to the wider two-way SE. The normal multiplier is 5–11% too optimistic at these cluster counts |
| Every other `mde_pct` in the committed CSV: **0.152 / 0.403 / 0.0959 / 0.305** (arms B, C, D, A − D, all drug-doses) and **0.636 / 0.547 / 0.312 / 0.709** (arms A, C, D, A − D, p53-activating) [`tables/mg53_to_p53_effect.csv`] | **0.348 / 0.461 / 0.121 / 0.346** and **1.034 / 0.738 / 0.456 / 0.953** | M, main table | Same multiplier and same standard error, arm by arm |
| The true-MG53 detection limit implied for arm A by dividing the committed MDE by 0.289 | **+1.194%** per doubling of true MG53 using the TP53-wild-type reliability 0.301 (10.0% of the drug-induced p53 response); **+1.155%** for the A − D contrast, disattenuated arm by arm | M, headline and "A − D" | A group-specific divisor, and a disattenuation applied separately to each arm instead of once to the difference |
| Reliability **0.289** used as the single divisor for every "true MG53" conversion [`FINDINGS.md` "Power"; `MG53_p53_TABLES.md` column glossary and per-gene bound; `MDM2_MG53.md` summary table and §on the true scale] | **0.301 in TP53-wild-type lines, 0.283 in TP53-altered lines**. A contrast across genotypes must be disattenuated arm by arm: the single-divisor version of A − D gives +0.174% against the correct **+0.158%**, which is **10% too large** | M, "A − D" and the generator's note (6) | Reliability is group-specific and the quantity being corrected spans both groups, so one divisor is arithmetically wrong for a contrast |
| The same 0.289 used as the attenuation factor **λ** for an MG53-as-exposure slope — the published `mde_diff_80_attenuation_corrected` applies 1/0.288981 = 3.46× [`two_way/tables/d1_two_way_models.csv`; carried into `MG53_p53_TABLES.md`] | **λ = 0.078–0.105 (a 9–12× correction), 0.055 trimmed.** 0.289 is the optimistic floor of that range, so the published correction is **understated by 3.6×** | U, F6 and §6.4 | The split-half splits *cells* within each (well, line) and re-runs the correction on each half, so it measures cell-sampling noise only and books every well-level artefact as signal. Matched on the same 102 replicated drug-doses it reads 0.425164, so the published agreement between the counting-noise share and 1 − 0.289 compared unmatched samples |
| Any figure reported "per doubling of **true** MG53" by dividing a same-well slope by λ — including `FINDINGS.md`'s bound of **"about 1.4% per doubling of true TRIM72"** (recomputed there as 0.00592 / 0.289) and `README.md`'s **"about 1.3–2% of true MG53"** | The division is **not licensed at all**: exposure and outcome are counted from the same cells, in the same well, against the same total-UMI denominator, so the classical correction's independence condition fails by construction. The artefact-free replacement needs no λ — **+0.0074 to +0.0079 program-log2 per doubling of true MG53 [−0.018, +0.026]**, from cov(exposure in well A, outcome in well B) over 102 cross-batch replicate pairs. If one insists on dividing, 0.005925 ÷ λ gives **1.37% at 0.301 and about 4.0–5.3% at λ 0.105–0.080** (recomputed here) | U, F7 and §2.6; M agrees in its caveats | A correlated-error channel that the classical correction cannot handle, demonstrated directly: the cross-well estimate of the association is at or below zero in every arm while the same-well estimate is positive |
| `MG53_p53_TABLES.md`'s per-gene bound: **"+2.0% in the gene per doubling of measured MG53 … and, dividing by MG53's split-half reliability of 0.289, +7.1% per doubling of true MG53"**; common slope "+1.0% measured / +3.7% true" | The measured bounds stand. The true-MG53 restatements become roughly **+21% to +29%** and **+10% to +13%** at λ 0.105–0.080 (recomputed here), and are better read as unquantified, per the row above | U, F6 and §2.6 | Same λ and same independence failure |
| Replicate-well reliability **"0.114 [`two_way/tables/key_results.csv` row 206]"** [`FINDINGS.md` "Power"] | Row 206 reads **0.113639**. `reliability_single_well` 0.114342 is at row 111 of `trim72_reliability.csv` (`fe = dd`), and `reliability_full_spearman_brown` 0.289317 at row 54 (`fe = ddxg`); row 184's `estimate` cell is 0.169124, with 0.289 appearing only in its `detail` string. **Three different specifications, not interchangeable** | U, §2.3 | All verified directly at source. There is also no single exchangeable-replicate reliability to quote: the two wells' residual SDs are 0.519 and 0.825, a 2.5× difference by design, one deep-plate and one shallow-plate well |
| The menu of subset reliabilities "**0.289 … 0.425, 0.586, 0.610 and 0.705** for the active, p53-responsive and other subsets" [`MDM2_MG53.md`; `MG53_p53_TABLES.md` cites `ii_active` 0.610 as halving the de-attenuation] | The high values are **not scope-matched**: 0.585 is variant `ii_p53` (the 50 drug-doses with curated P53_ACTIVITY z ≥ 3) and 0.706 is `ii_trim72` (the 23 MG53-moving ones). Neither is the 142-drug-dose `in_S2_p53_activating` set, so **no scope-matched reliability for the p53-activating scope exists** and every true-MG53 scaling of that scope is unverified | M, "What this can and cannot establish" | A divisor estimated on 23 or 50 drug-doses does not describe a 142-drug-dose scope |
| **"21 drug-doses raise TRIM72"**, with per-drug verdicts of "Replicated" and "Supported" [`FINDINGS.md`, "Drugs that raise it"; `MG53_p53_TABLES.md` Table B] | **2 of 21 survive a replication requirement** — idarubicin 5 µM and homoharringtonine 5 µM, both wells each. **17 cannot be tested at all** because the design gives them one well; mitoxantrone 5 µM passes in 1 of 2 wells with the two wells disagreeing in *sign*; adagrasib 0.05 µM passes in 1 of 14 | U, F1 and §4.2 | A control that was missing: the committed grading never asked whether a call replicates in a second well, and 1,024 of 1,132 drug-doses rest on one used well |
| The count **21** read as evidence that MG53 is specifically drug-responsive | **Uninformative.** The identical calling rule on 2,409 screen genes matched to MG53's expression level gives a median of 17 raisers per gene (mean 18.2, p90 32, max 70), putting MG53's 21 at the **66.7th percentile**; restricting to the 419 level-matched genes with `dog_class = unexposed`, structurally incapable of readthrough spillover, *raises* the median to 20 and moves MG53 to the **53.2nd percentile** | U, F2 | A placebo-gene calibration measured in the same wells. The ledger must carry the counter-caveat: a no-signal null yields **0.12–0.14 calls** (median 0, p95 1, P(≥21) ≤ 0.0005), so the procedure is **not** miscalibrated. The placebo result says MG53 is unremarkable among genes of its level, not that the 21 calls are false positives |
| Dinaciclib 0.05 / 0.5 / 5 µM at **3.8× / 3.7× / 5.6×**, graded "Weak" [`FINDINGS.md`]; "Dinaciclib 5 uM, corrected log2 fold **+2.48**, positive" [`MG53_p53_TABLES.md` Table B] | **Refuted — an artefact of the ratio-scale estimand.** On an added-CPM scale all three doses score ≈0 (`R4_z` 0.674 / −0.304 / 0.000, q up to 0.969), with 71–82% cell loss, a 10.8× depth deficit, 25 of 44 lines carrying zero MG53 reads at 5 µM, and a pseudocount floor of 2.545 CPM (half-count) or 5.090 (one-count) against a plate baseline of 0.883 — so a line with **no reads at all** already scores 62–111% of the reported 2.478 log2 | U, §4.2 and §6.4 | A control that was missing: the absolute scale. A fold change built on a pseudocount in a depleted well can be produced with no added RNA |
| Mitoxantrone 5 µM: "**3.9× on plate 6, 1.07× on plate 14** … Not replicated" [`FINDINGS.md`] | Per-line, per-plate matched pooled counts give **2.93× on plate 6** (615 observed against 210.2 expected, 42 of 48 lines up, sign test p 5.0e-8) and **0.73× on plate 14** (2,814 against 3,848, 13 of 48 up); pooled 0.84×; added CPM +5.3 then −5.4. The correct description is **non-replication with a sign flip** | U, §4.2 | A count-based estimand in place of the ratio-scale atlas fold. The flip is more informative than "not replicated": no fixed positive absolute induction can produce it, so mitoxantrone falsifies the fixed-absolute-induction model in the one testable decision-relevant case |
| Added CPM for the two replicated raisers, plate 6 against plate 14: "**+39.9 vs +46.2 and +46.6 vs +36.8 CPM**" [`FINDINGS.md`, from `upstream_coregulation/tables/c_locus_strand_summary_raiser_wells.csv`] | Recomputed from per-line matched pooled counts: idarubicin **+39.9 / +40.9** (1.02× apart, against a 4.4× gap in fold terms) and homoharringtonine **+46.4 / +30.4** (1.53× apart) | U, §4.2 | The Grade-A call rests on the matched per-line count estimand, which is the one that supports "the same absolute amount of RNA across an 8× baseline gap" |
| Drug classes: "No raising class passes FDR … **smallest q 0.218** over 189 class rows"; TOP2 poisons "4 of 5 (p 0.0118, q 0.218)" [`FINDINGS.md`, "Drug classes"] | The smallest q is 0.2183 **only within the family as the pipeline cut it**. BH recomputed over all 189 rows for that statistic gives **q 0.5575**, and over 189 rows × 4 statistics (756 tests) the smallest q anywhere is **0.3024**. Leave-one-out removes most of the apparent signal: TOP2-poison residual mean z 4.956 → 2.561, anthracycline 7.679 → 4.251 | U, §4.7 | The committed q was corrected within a narrower family than the one actually searched. The conclusion (no raising class at FDR) is unchanged and strengthened |
| "The only class result at FDR is a lowering lean of Tahoe's mixed '**Other TK inhibitor**' class (14 compounds; **q 0.010**)" [`FINDINGS.md`] | **q 0.00999 within the 25 `moa_fine` rows, 0.0756 over all 189 rows, 0.3024 over 756 tests.** It does survive leave-one-out (−0.737). Treat as a hypothesis for a replicated design, not a finding | U, §4.7 | The q depends entirely on the family definition, and the family searched was the larger one |
| "**TRIM72 has a typical number of partners (5,881 at \|r\| ≥ 0.3 vs a matched median of 5,330)**" [`FINDINGS.md`, "What moves with it"] | **Holds raw only.** With covariates MG53 sits at the **29th percentile** (1,405 partners against a matched median of 2,797). The pipeline's own `TRIM72_pctile_n_partners` is 59.67 raw and 29.0 with covariates, reaching the 100th percentile only once principal components are removed (660 against a matched median of 13.5) | U, §5.2 and §6.4 | The statement is true in one covariate choice and false in another, and the choice was never declared. Every claim about "MG53's partners" is a claim about one variant |
| "**51 of the 52 low genes still at r ≥ 0.4 are readthrough-exposed (odds ratio 193, p 5.8e-33)**" [`FINDINGS.md`] | The odds ratio is monotone in the number of PCs removed across five variants of one pre-specified contrast: **raw 2.234** (637-gene module, 34.07% exposed, p 6.3e-15), covariates 41.79, minus-1PC 26.37, minus-3PC 98.2, minus-10PC 192.7. Over *all* low-expressed genes surviving at r ≥ 0.4 the module has **83 members, not 52** (51 exposed, 31 "other", 1 strictly unexposed), and on a graded definition **70 of 83 = 84.3%** are readthrough geometry, with a whole-module **OR 18.3 (p 5.6e-34)** | U, §5.2 and §6.4 | Variant selection inside a pre-specified family — 193 and 98 were reported while 2.2 was omitted — plus an undercounted module. The correction **strengthens the biology and cuts the headline odds ratio tenfold** |
| "That puts TRIM72 at the **99th percentile of 300 level-matched genes** (median 4%) and the **92nd of 39 readthrough-exposed genes** of its level (median 11%)" [`FINDINGS.md`] | Against the 300 expression-matched genes MG53 is at the **96.7–99.0 percentile** across the five variants, which converts to empirical **p 0.013–0.037** (BH over variants q 0.028–0.037 — survives). Against the 39 matched genes that are **themselves** readthrough-exposed it is at the **84.6–94.9 percentile**, which converts to empirical **p 0.075–0.175, never below 0.05 in any variant**, on a design whose attainable floor is 1/40 = 0.025 | U, §5.2 | A percentile is not a p value, and the geometry-matched family is the one that bears on specificity. The honest statement: MG53's readthrough enrichment is **specific relative to expression level and typical relative to readthrough geometry** — which is good evidence that [[Readthrough spillover]] is the right account and direct evidence that MG53 is not special within it |
| "Within lines, **no TF passes the noise ceiling: the maximum \|r\| is 0.080 (E2F4)**"; the TP53 regulon within lines at **r −0.060** [`FINDINGS.md`, "Transcription factors" and the list-based test table] | **Slice-dependent.** The table holds four slices (2 TRIM72 versions × 2 covariate sets) and in **three of them 2–3 labels exceed their slice's ceiling, always including the p53 activated-target set** (−0.0765 to −0.0829 against ceilings 0.070–0.080) — 27–38% larger in magnitude than the −0.060 reported. Maximum positive is +0.0714 (MYBL1), minimum −0.0801 (E2F4) | U, §3.8 and §5.3 | The slice was not declared as a choice. The direction is negative, so this does not make p53 a positive regulator of MG53 — but the reported figure is not the largest the table holds |
| CollecTRI regulon leaders: "**ATF4 r 0.36 (q 9e-26), ATF5 0.36, ELK4 0.35, SRF 0.31, XBP1 0.29, MEF2C 0.21, AP1 0.20**" [`FINDINGS.md`, from `summary/T11_upstream_TF_activity.csv`] | Ranked over all 679 regulons the maximum is **ATF5 0.359** (drug-block CI 0.289–0.430, 25 targets), then ATF4 0.357, **TWIST1 0.354, GCM1 0.353 (6 targets), TWIST2 0.351**; minimum −0.377 (NAB2, 6 targets); median \|r\| 0.106. **473 of 679 reach q < 0.1, so significance is uninformative**; 409 of 679 CIs exclude zero and **64 of the 473 "significant" TFs have a drug-block CI spanning zero**; four of the top eight rest on 5–13 targets | U, §5.3 | The committed list omits regulons that outrank the named ones, and carries no intervals and no target counts — without which an r of 0.35 on 6 targets reads like an r of 0.35 on 25. See [[Transcription factor activity inference]] |
| "Plate 6 and plate 14 agree at **r 0.75** overall, but only **0.28** without the two strong raisers" [`FINDINGS.md`, "Using the exported data" item 7] | **Pearson 0.775 and 0.321** | U, §2.4 and §6.4 | Recomputed directly from the per-well export |
| "Its median TRIM72 log2 fold is below 0 on **every plate** (−0.06 to −0.92)" and "Tahoe's uncentred DESeq2 values sit below 0 on every plate" [`FINDINGS.md`, item 5 and "Drugs that raise it"] | Negative on **13 of 14** plates. **Plate 9 is positive** — and it carries five single-well raisers | U, §2.4 and §6.4 | A missing plate in the original count, and the exception is not incidental: it is a plate the raiser list leans on |
| "Of 62,611 usable profiles from expressing lines, **12.4%** have zero UMIs" [`FINDINGS.md`, item 1]; the bare "**12.4% of profiles zero**" [`MDM2_MG53.md`, three places] | **Correct with its denominator: 12.42%** of usable profiles from expressing lines. Over all 63,921 usable profiles it is **13.69%**, and over all 66,449 profiles **16.56%**. The bare form needs its denominator attached | U, §2.4 and §6.4 | The figure is reproducible only with the denominator it was computed on, and the three denominators differ by a third |
| "**Organ does not predict the level either (p 0.65)**" [`FINDINGS.md`, "Cell-line traits"] | The 13-organ Kruskal-Wallis is **H 9.19, p 0.708**. The reported **H 3.31 / p 0.653** is a 6-group pooled version — the statistic and the degrees of freedom as reported did not go together. Organ's unadjusted R² of 0.186 is a 12-parameter fit whose **adjusted R² is −0.085** | U, §5.4 and §6.3 | A matched statistic and df. The conclusion is unchanged and firmer: lineage explains nothing |
| "the **14** KMT2D-altered lines have **+1.48 log2** more TRIM72 (95% CI **0.84–2.12**; q 0.046 within this outcome, 0.12 over all tests)" [`FINDINGS.md`, "Cell-line traits"] | **15** KMT2D-altered lines, **+1.481 log2 (2.79×)**, SE 0.349, **CI 0.797–2.165**, R² 0.277 on 49 lines, 5,000-draw line-label permutation **p 2e-4**, MDE80 1.118 log2 (2.17×). The committed drop with PYCARD-AS1 in the model is confirmed exactly (+1.527 → +0.390, SE 0.275, CI −0.149 to +0.930), and the residual is now shown to be a **bounded null below its own MDE** (permutation p 0.102, MDE80 0.665–0.669 log2) | U, §5.4 | Rebuilt from the per-line table over the full 49-line set with honest multiplicity over all 5,075 line tests. The effect reduces to the locus, not to chromatin |
| P24's readthrough composition: "20.6% readthrough-geometry vs **2.1% of all program members**" [`FINDINGS.md`, "Programs"] | 20.6% against **4.2% of atlas genes (OR 6.0, p 1.3e-9) and 1.7% of *other* program members (OR 14.7, p 7.6e-16)** | U, §5.5 | The committed denominator includes P24 itself, which is the set being tested |
| "readthrough-geometry genes … against **4.2% of all genes**" [`FINDINGS.md`, twice] | **4.218%.** The pipeline table prints 4.224%, which divides a 703 numerator from one gene universe by the 16,642 of another | U, §5.2 | An arithmetic slip in the source table. The committed rounding is unaffected; recorded so the printed column is not trusted to three figures |
| "**MEF2A / C / D are expressed (298.5 / 21.9 / 86.8 CPM)**", their mRNA relating to TRIM72 at "−0.17, −0.165, −0.03" [`FINDINGS.md`, twice] | **MEF2A / B / C / D at 298.5 / 13.8 / 21.8 / 86.8 CPM**, correlations **−0.175 / −0.037 / −0.165 / −0.026** | U, §5.3 | Recomputed; rounding-level, and the reading is unchanged — the muscle factors are silent, absent, or negatively related |
| Table 4's mean rho over the 18 exposures, **−0.162473**, called "**the pipeline's own estimator**" [`MDM2_MG53.md`, "The per-exposure Spearman"] | That is the **arithmetic** mean. The pipeline averages in **Fisher z** and reads **−0.179022**, 10% further from zero, at p 0.030194 / q 0.181164 on 5,000 draws. Both are now printed side by side, arithmetic still the document's statistic | R, Table 4 | Recomputed both ways from `downstream_p53/tables/a_per_line_effects.csv` over the same 18 exposures and 17 wild-type lines: arithmetic −0.162473, Fisher z −0.179022, the latter matching `a_pooled_over_drugdoses.csv` exactly, and `README_tables.txt` says "Fisher z average" outright. The mislabel ran toward the document's own null conclusion |
| The **per-exposure shuffle** labelled "**This is the null the pipeline reports**", with the line-label shuffle as "the stricter null" whose cost was "exactly the inflation the weaker null was hiding" [`MDM2_MG53.md`, same section] | **All three withdrawn.** `a_pooled_over_drugdoses.csv` carries exactly one p column, `p_line_permutation` — "ONE line-label permutation applied to all drug-doses at once" — and had already returned **p 0.030194** for this cell. The document's 0.036 on 2,000 draws **reproduces** the pipeline rather than correcting it; the per-exposure shuffle's 0.005 is the anti-conservative of the two, and no run table applies it to a mean over exposures | R, Table 4 | The pipeline's own column and README, read directly. Permuting MDM2 inside each exposure destroys the fact that the same 17 lines recur in all 18, which is the structure the claim is about |
| Unit 3's exposures called "**18 MG53-raising exposures**" [`MDM2_MG53.md`, Table 4 and the unit table; carried into [[MDM2 and MG53]]] | **13 of the 18** were selected for raising MG53 (role "TRIM72 raiser", panel call up at z ≥ 4, 2.05× to 12.24×). The other **five are p53 reference activators that missed that cut, and four of them lower MG53** — Topotecan 0.5 µM 0.93×, Mitoxantrone 0.5 µM 0.89×, Selinexor 5 µM 0.81×, Amsacrine 5 µM 0.76×; the fifth, Idarubicin 0.5 µM, raises it 2.15× at z 3.42. Those four are the only exposures of the 18 where MG53 falls | R, Table 4 | `a_selected_drugdoses.csv`, row by row. Not cosmetic: on the 13 raisers alone the wild-type statistic is **−0.223 arithmetic / −0.244 Fisher z, p 0.0035, negative in 10 of 13** against **−0.005 (1 of 5, p 0.98)** on the activators, so the published 18-exposure figure is a diluted union. The five dilute because MG53 moves less across lines in them (median between-line SD 0.86 against 1.26) |
| Table 4's wild-type row nominated for follow-up — "**if anything in this document is followed up, this is the row**" — on the premise that it "needs the two things this run cannot give it — per-line MDM2 values across all 1,132 exposures instead of 18" [`MDM2_MG53.md`, closing section] | **Withdrawn: it fails out of sample.** `p53_dependence/tables/per_line_effects_selected.csv` holds the same per-line quantity over **87** drug-doses (10 gene labels × 50 lines, 40,583 rows), a strict superset of unit 3's 18 agreeing to max \|diff\| 5.0e-06 on all 5,507 shared cells — so **70 exposures were held out and unexamined**. On those 70 the statistic is **−0.0077, negative in 35 of 70, line-label p 0.84**, against **−0.1807 at p 0.029** on the 17 shared. The raiser subset the tilt lived in goes the same way: **−0.032, 5 of 10, p 0.66** against −0.201 at p 0.018 on 14. What stands is the pooled within-exposure slope over all 87, **−0.0307 (95% CI −0.0597 to −0.0059, cell-line bootstrap over 17 clusters, p 0.016, n 1,478) = −2.1% of MDM2 per doubling, interval −4.1% to −0.4%** | R, "The out-of-sample test" | Both estimators recomputed panel by panel from the 87-exposure table with the line-label null and a cell-line bootstrap. The premise was false in the way that mattered — the run had 87, enough to test the row and retire it. "More than 17 wild-type lines" stands: the larger panel buys exposures, not lines, and 24 of its 87 drug-doses were themselves selected with the TP53 labels |
| "nothing detectable … between the MG53-positive and MG53-negative cells of a single well" — a bound-shaped sentence with **no bound**, at the one unit of the five where the document gave none [`MDM2_MG53.md`, "What this adds up to"] | The run publishes one. Per doubling of a cell's MG53: wild-type rate ratio **1.0346 (0.9882–1.0832)**, largest change not excluded **8.3%**, MDE80 **6.7%**; untreated altered wells **0.9784 (0.9587–0.9986)**, largest not excluded **4.1%**, MDE80 2.9%. This resolution is therefore **2.4× coarser** than the exposure-level ±3.4%, in the arm the p53 question needs | R, Table 6b | `single_cell_all/tables/per_doubling_bounds.csv`, alpha-as-estimated scenario, read row by row. The step converts the detected/undetected contrast to a doubling of the implied true MG53 rate under its pooled overdispersion, so it is the same unit as the exposure-level bound and the two are comparable |
| The two-well single-cell comparison called "**the best-controlled comparison in the data**", its untreated altered **−8.5%** read as what this resolution shows [`MDM2_MG53.md`, Table 6] | The identical GLM runs at full scale over **20,120 (cell line × well) groups, 1,289 wells, 47 lines** (9,099 wild-type, 11,021 altered), and **the pooled sign is the other way**: all wells **1.0331 (0.9941–1.0737), p 0.095**; wild-type **1.0711 (0.9763–1.1751), p 0.14**. The step's own primary estimand, wild-type minus altered, is null in all five well classes (all wells 1.0593, permutation **p 0.158**; 0.11 to 0.85 across classes). The untreated negative survives at about half the size over all 28 DMSO wells — **0.9559 (0.9165–0.9971), p 0.037, q 0.093** — and the raiser class reads 0.9489 (0.9150–0.9840), p 0.0056, q 0.020, but both sit at the **15th–27th percentile of that step's 63–66 placebo outcome genes** (empirical p 0.39–0.55) | R, Table 6b | `single_cell_all/tables/trim72_meta_by_tp53_group.csv`, `trim72_WT_minus_altered.csv` and the placebo-outcome null, row by row. Table 6's eight MDM2 cells are two exposures of this same fit, so the plate-6-against-plate-14 disagreement is a two-well reliability statement, not the pooled behaviour of the resolution |
| Unit 3's within-exposure wild-type interval as "**−0.139 to +0.019, compound-bootstrap p 0.13**" [`MDM2_MG53.md`, Table 4, twice] | **−0.142958 to +0.019653, p_boot 0.123**, on a bootstrap clustered on **cell line — 17 clusters**, not on compound. Two separate faults: the generator seeded each bootstrap from `abs(hash((SEED, label, …)))`, which Python salts per process, so **no interval or `p_boot` in `mdm2_mg53_models.csv` could be regenerated** and the prose drifted from the committed table; and "compound" was the wrong word for a cell-line-clustered fit. The seed is a blake2b digest now, and every such bound is a 2,000-draw Monte Carlo quantity whose third digit moves | R, the generator's note | Reproduced the committed interval exactly by re-running the procedure under the stable seed (slope −0.060284, 17 clusters, 2,000 draws → −0.142958, +0.019653, p 0.123), and confirmed the salting: `abs(hash(…))` on the one key returned three different values under PYTHONHASHSEED 1 / 2 / 3 where blake2b returned one. The mislabel ran the other way — clustered on compound the same row reads **−0.127 to −0.009, p 0.018**, an interval excluding zero |

---

## Corrections already recorded in the write-ups

Some of the committed documents caught their own errors and said so on the page. Those are listed here so
the ledger is complete, and because the habit is the point: a corrected number kept next to its replacement
is worth more than a clean page.

**`MDM2_MG53.md` records twenty-one**, under "Corrections this document carries" — see [[MDM2 and MG53]].
These seven predate the review:

1. the 4,642-gene reference family was called **"all genes"** when 4,500 of its members, 97% of it, had been
   selected for association with MG53 and MDM2 is one of them, so percentiles inside it are ranks within the
   discovery set. The unselected 16,642-gene co-regulation family is the one the conclusions rest on. See
   [[Placebo genes and reference families]];
2. MDM2 was called **the best-measured gene in the analysis** when 185.8 CPM is **903rd of 16,643** by level;
3. **three Spearman correlations were quoted with their OLS slope's p value**, one of them overstating
   significance by nine orders of magnitude;
4. the wild-type-versus-altered equality in the genome-wide screen was said to mean a p53-mediated effect
   **"cannot"** behave that way, when the test has about **21% power** (the difference CI is
   [−0.010, +0.009]);
5. the **per-doubling-of-true-MG53 figure was given as a point value using the reliability subset that
   maximises it** — the ledger row above supersedes even the corrected version, since the division itself is
   not licensed;
6. the **per-line genotype interaction was not reported at all**, although it reads **p 2e-06 with the
   wild-type slope six times the altered one** before each exposure's mean is removed, after which it is
   p 0.36 — and its contrast gene behaves identically, including a sign flip between arms that no p53 route
   predicts;
7. the **unit-3 n was given as 861** where every contrast in it runs on **843**.

The other fourteen came from the review. **Eight are the R rows in the table above.** Two the table already
carried from the other documents — the bare "12.4% of profiles zero" and the 0.289-to-0.705 reliability
menu. The last four are transcription-level and change no reading:

- MG53 given as detected in "**50 of 50**" lines, hardcoded in the generator, where the export says **49**:
  NCI-H661 (CVCL_1577) fails the expression filter and `b_baseline_per_line.csv` agrees at 49 of 50. Now
  read from `export/all_genes/genes.csv` like the other two genes' counts;
- the activity-adjusted partial Spearman given twice as **−0.019** where it is **−0.022299**, recomputed by
  residualising both genes on the five activity covariates over all 1,132 exposures;
- the p quoted beside it as 0.45, which is the **Spearman's own p (0.4535)**; the bootstrap p is **0.46**;
- Table 6's caveat that MG53 is "detected in a minority of cells at about **5 UMIs**" — a pseudobulk
  profile's whole count over a median 1,217 cells. A **detected cell carries 1.12 to 1.18 UMIs**, at a
  detection rate of **1.3%** of an untreated line's cells (0.36% on plate 6, 3.01% on plate 14; 7.5% and
  10.0% under idarubicin), with detected cells **23% to 32%** more deeply sequenced than undetected ones.
  Understating this understated the table's exposure to the depth confound.

The same document also keeps, deliberately, the two results that would have been read as findings without
their controls: the **−0.614** correlation between MDM2 and MG53 CPM, which is a plate batch effect in full
(between plate medians −0.763, within plate **+0.074** — see [[Plate batch effects]]), and the per-line
genotype interaction at item 6.

**`MG53_p53_TABLES.md` records two:**

- **the fold-change baseline.** "An earlier version of this section said `fold_WT_broad` was diluted by
  averaging over drug-doses that mostly do not activate p53. That was wrong: the average is taken over the
  142 **p53-activating** drug-doses specifically." It reads low for two other reasons — its baseline is the
  same line's median over that plate's **drug wells**, not vehicle, and it is a compound-equal mean over 98
  compounds, so one strong activator is averaged with 97 weaker ones and the median program gene reads only
  1.06×;
- **the placebo resolution.** The `placebo_pct_common_*` and `placebo_pct_diff_*` columns have a
  **resolution of 0.1, because each family holds only 10 placebo exposures in the per-gene screen**. A 0.0
  or 1.0 there means "most extreme of ten", not a p value, and cannot support a claim on its own. This does
  **not** conflict with `FINDINGS.md`'s 100 expression-matched and 100 response-matched placebos: the
  10-gene sets are the λ-inflation panel in `genome_wide/tables/c_calibration.csv`, while the program-level
  test in `c_program_models.csv` draws on the 200 exposures in `c_placebos.csv`. The upstream document
  confirms the 100-and-100 figure for the program-level test field by field.

`FINDINGS.md` carries a sibling ledger one level down — "Repository text that the verified numbers correct",
nine rows correcting `SUMMARY.md` and the individual step READMEs, including the cap-0 sample numbers, the
structurally untestable AP1 row, the `signalling_category` kinase overlay, the non-converged medians in
`d_single_cell_meta_all_outcomes.csv`, and the "> 1.2% excluded" bound. Those corrections stand.

---

## Flagged, but not settled

Honesty requires separating "corrected" from "contradicted but unresolved". These are the second kind.

**Intervals built the same way as the three that reversed, but never refitted.**
`MG53_p53_TABLES.md` Tables A and C quote 95% intervals with cell-line-clustered standard errors over 9 to
28 clusters — the construction that proved 12–58% too narrow everywhere it was recomputed. Table C's
"Responsive, 11 lines" row, **+0.0014 (−0.0015, +0.0043)**, *is* the same fit as
`tables/mg53_to_p53_effect.csv` arm A and so inherits its correction exactly. Its two **positive** verdicts
do not: altered lines at or below null, 14 lines, **+0.0043 (+0.0004, +0.0082)**, and panel-unresponsive,
28 lines, **+0.0026 (+0.0001, +0.0052)**. So does Table A's single interval excluding zero — CollecTRI TP53
targets, 17 lines, **+0.0029 (+0.0006, +0.0051)** — on which the committed line "the only interval that
excludes zero is **positive**" depends. None was recomputed. Treat all three verdicts as **unresolved**, not
as corrected; the direction of the committed reading (an association largest where p53 is least functional,
and positive) is what [[Downstream of MG53]] and [[The measurement with controls]] both independently
support.

**The readthrough index and idarubicin.** `FINDINGS.md` reports that on the effect-size index
`DoG_sense_index_log2`, **9 of the 21 raisers** are global readthrough inducers and idarubicin 5 µM raises
TRIM72 12× while the index stays flat (**+0.002, rank 534**). The upstream document reports **8 of 21 in the
top tail and 7 in the bottom tail, with idarubicin 5 µM in the bottom tail at rank 1,104 of 1,132**, and
marks the claim **unverified in detail** because the index was not rebuilt. The two readings draw on
different columns and neither has been reconciled; the upstream document's own first next step (P1) is the
analysis that would settle it. What both agree on is that idarubicin's effect is locus-local — its own
neighbourhood rises sharply, with FUS gaining 189.5 CPM in its plate-6 well.

**Internal inconsistencies between committed files, which neither new document resolves.**

- Untreated MG53 across lines: **1.0–24.65 CPM, median 6.13** [`FINDINGS.md`] against **0.93–23.6 CPM,
  median 5.9** [`MG53_p53_TABLES.md`] and **5.89 CPM** [`MDM2_MG53.md`]. The upstream document gives the
  spread as **21.4× by pooled DMSO CPM, or 24.4–25.9× from recomputed line effects**, which is consistent
  with all three but adjudicates none.
- MDM2's wild-type-versus-altered baseline Welch p: **3.3e-12** [`README.md` and `MDM2_MG53.md` body]
  against **3.4e-12** [`MDM2_MG53.md` summary table].

**Two claims the upstream document flags as at risk whose text is not in these four files**, so there is
nothing here to correct: "MDM2 +1.0967 (z 8.79) at idarubicin 5 µM", **mis-cited** — the value lives in
`p53_dependence/tables/wt_vs_altered_selected_long.csv` (p_perm 1e-4, fdr 1.7e-4), not the table cited; and
the idarubicin 5 µM TRIM72 wild-type-minus-altered difference, which takes **four values** across the
project's own tables (−0.6175, −0.1401, −0.0191, +0.3373; all non-significant, but quoting one of four
without reconciling them is not publishable).

**Three results that run the other way, which the committed write-ups do not carry at all.** Omissions, not
errors — but a ledger that only lists overstatements is not honest either.

- **MUSCLE_STRUCTURAL** (MYH3, TNNT1, TNNT2, RYR1, ATP2A1, DYSF) is the **only one of 44 gene sets to
  survive BH over the whole gene-set family**, in two variants: mean r **+0.318** (z 3.50, p 0.0015,
  q_BH 0.0073) with covariates, **+0.229** (z 3.28, p 5.0e-4, q 0.0031) with 3 PCs removed, against
  level-matched random sets. Removing ATP2A1, the 16p11.2 member, leaves 0.307 and 0.207, and the null is
  level-matched by construction, so neither ground offered for dismissing it holds. For a project about a
  muscle gene this is the most under-weighted result in the material.
- **MG53 raisers are enriched among p53-activating drug-doses in the tail.** At DD_z ≥ 2 the enrichment
  survives amplitude stratification: 17 of 142 against 26 of 944, **OR 4.80, p 7.9e-6**, with permutation of
  the activating label within deciles of `n_sig_genes` giving p 0.0031. At DD_z ≥ 3 it does **not** survive
  (7 against 5.19 expected, p 0.225; Mantel-Haenszel OR falls from 4.40 crude to 1.74). The honest reading:
  MG53 tracks total p53 activation only in the extreme tail, and there mostly through response amplitude.
  See [[Upstream of MG53]].
- **FOSB** is the one candidate regulator the negative conclusion does not cover: rank **63 of 16,642**
  (r 0.582 with covariates, q 9.7e-66, 99.3rd percentile of level-matched genes) and rank 43 at minus-10PC,
  at 51.8 CPM, in the stable core of all five variants, **with no readthrough source 5′ of it**.
  `FINDINGS.md` reports the rank but draws no conclusion from it, so "nothing that behaves like a
  transcriptional regulator survives" remains an assertion rather than a finding until FOSB's rank is
  compared against the most drug-responsive genes generally.

---

## What survived unchanged

Read the list above against this one, or it will mislead. The study's conclusion is not among the
corrections: in TP53-wild-type lines, more MG53 mRNA shows **no detectable association** with p53 target
output or p53-driven arrest, with effects above roughly 0.4–0.6% per doubling of measured MG53 excluded —
and what raises MG53 most in this dataset is transcription running into its locus from its neighbours, not
a transcription factor. See [[What this study found]].

Specifically verified field by field, and unchanged:

- the programme-level genotype contrast — b_WT **+0.000400**, b_alt **+0.002227**, difference
  **−0.001828 [−0.005232, +0.001577]**, two-way p 0.2855, TP53-label permutation **p 0.3038**, MDE80
  **0.005925** — described by the upstream document as the soundest inference in the area, the one whose
  null matches its estimand. The observed difference is 31% of its MDE and has the **wrong sign**;
- the model's size: **53,084 rows, 17 wild-type and 30 altered lines, 47 lines in all**;
- the placebo families and their empirical p values: **100 expression-matched and 100 response-matched**
  genes, t_diff at the 64.0th percentile / p 0.6535 (expression) and 69.0th / 0.7327 (response), reproducing
  the pipeline's own columns to six decimals;
- the calibration that governs every line-level statistic: observed λ_common **4.4436** for MG53 against
  expression-matched placebo medians of **5.518** and response-matched **4.685** — the inflation belongs to
  line-level structure, not to MG53. See [[FDR calibration and the inflated null]];
- the plate-batch gap: **3.124 log2**, rank **1 of 16,656** genes;
- the locus: PYCARD-AS1 against untreated MG53 at ρ **0.820 [0.690–0.899]**, q 9.0e-5 over 5,075 line tests,
  R² **0.679**, with FUS adding 0.007. See [[The TRIM72 locus]];
- program **P24** as MG53's closest program partner: r **0.768** across drug-doses (q 6.21e-86), 0.208 clear
  of the runner-up, **+0.0297 log2 per doubling** within lines, with no TP53-group difference;
- exactly **1 of 1,132** drug-doses reaching the committed lowering rule — ponatinib 5 µM;
- the sense-index Spearman of **0.451**, and the top-100-by-t readthrough share of **55%**.

---

## Links

- [[The measurement with controls]] — the controlled measurement, with its own section listing the three
  intervals that no longer exclude zero
- [[Upstream of MG53]] — §8, *Claims dropped, withdrawn or corrected*, the fuller list on the upstream side
- [[MDM2 and MG53]] — the twenty-one self-recorded corrections and the two documented near-misses
- [[Reliability and disattenuation]] — why the 0.289 divisor is both the wrong value and the wrong kind of
  correction
- [[How the numbers are decided]] — the standards these corrections are measured against
- [[Nulls and calibration]], [[FDR calibration and the inflated null]] — why an analytic p is not evidence
  here
- [[Placebo genes and reference families]] — selected against unselected reference sets
- [[Downstream of MG53]], [[What this study found]] — the conclusions, which the corrections do not move
- [[Tables — what the study produced]] — where each committed number lives

## Sources

1. **New, authoritative.** The controlled-measurement document, *"The measurement: p53 activity change per
   MG53 change, with controls"* — headline, design, main table, the A − D contrast, the mechanism section,
   the placebo pseudo-controls and the caveats, with numbers recomputed in `WORK/final_drug/`, `WORK/out/`.
2. **New, authoritative.** The upstream document, *"Upstream of MG53: regulation, perturbations, and what
   this dataset can support"* — F1–F11, §§2–6, with the independent `verify_*` recomputations and §6.4,
   *Which published claims are at risk*.
3. **New, authoritative.** The five-lens adversarial review of `mg53_p53/findings/MDM2_MG53.md` — the **R**
   rows, every number of which was recomputed here from the run tree (`downstream_p53/`, `p53_dependence/`,
   `single_cell_all/`) rather than taken from the review, and all of which are now carried in that
   document's own corrections passage and in its tables `mdm2_mg53_out_of_sample.csv`,
   `mdm2_mg53_single_cell_all.csv` and `mdm2_mg53_per_exposure_rho.csv`.
4. **Committed, older, and corrected here.** `mg53_p53/findings/FINDINGS.md`,
   `mg53_p53/findings/README.md`, `mg53_p53/findings/MG53_p53_TABLES.md`,
   `mg53_p53/findings/MDM2_MG53.md`.
5. **Committed tables cited row by row above.** `mg53_p53/findings/tables/mg53_to_p53_effect.csv` (10 rows,
   the arm slopes and their intervals and MDEs), `tableA_wt_p53_targets.csv`,
   `tableC_mutants_by_activity.csv`, `tableB_upstream_mg53.csv`, and in the run output
   `two_way/tables/trim72_reliability.csv`, `two_way/tables/key_results.csv`,
   `two_way/tables/d1_two_way_models.csv`, `genome_wide/tables/c_program_models.csv`,
   `genome_wide/tables/c_placebos.csv`, `genome_wide/tables/c_calibration.csv`.
