---
type: finding
tags: [finding, upstream, mg53, readthrough, perturbation, bounded-null]
status: current
---

# Upstream of MG53

What raises and lowers MG53 ([[TRIM72]]) mRNA in [[Tahoe-100M]]. "Upstream" here is **regulatory**: what
changes MG53's level. What MG53's level then does to p53 is [[Downstream of MG53]].

The answer, in one line: **the best-supported determinant of MG53's level in this dataset is transcription
running into its locus from its 5′ neighbours — [[Readthrough spillover]] — and not any transcription factor.**
Of the 21 drug-doses the committed pipeline calls raisers, two survive a replication requirement. The p53
pathway is not supported as a positive upstream regulator of MG53, with a bound of about 0.43× [[CDKN1A]]'s
induction on the same statistic.

Every claim below is tagged **PRE-SPECIFIED** or **EXPLORATORY** exactly as the source analysis tags it.
Numbers come from the upstream analysis document (`WORK/`, the subfolders `raisers/`, `p53_regulates/`,
`genomewide/`, `variance/` and the independent `verify_*` recomputations) unless another path is given.
Where that document corrected a published number, both values appear — see §8, *Claims dropped, withdrawn
or corrected*, which is the most useful section of this note, and the vault's ledger,
[[Corrections and retractions]].

---

## 1. Drugs that raise MG53, and by how much

The committed calling rule — BH `q_up` < 0.10 for MG53 across 1,132 drug-doses, plus |lfc| ≥ log2 1.2, with
a per-well Z boundary of 2.9258 — returns exactly **21 raisers and 1 lowerer**. The recomputation reproduces
the pipeline's arithmetic wherever the two overlap (pooled pseudocount-free log2 fold change matches at
r = 1.000000, max |diff| 0.0001; `DD_z` is exactly the Stouffer combination of per-well Z, max |diff| 0.0)
[`raisers/t1_inventory_all_drugdoses.csv`; `verify_raisers_0`]. **The disagreements below are about
inference, not arithmetic.**

Largest committed effects, as corrected log2 fold change
[`mg53_p53/findings/tables/tableB_upstream_mg53.csv`; `export/upstream/TRIM72_per_drugdose.csv`]:

| Drug-dose | Corrected log2 fold | Fold | `DD_z` | Plates |
|---|---|---|---|---|
| Idarubicin 5 µM | **+3.61** | 12.2× | 15.89 | 6, 14 |
| Homoharringtonine 5 µM | **+3.36** | 10.3× | 14.77 | 6, 14 |
| Auranofin 5 µM | +2.71 | 6.6× | 8.43 | 12 |
| Homoharringtonine 0.5 µM | +2.55 | 5.9× | 7.93 | 5 |
| Dinaciclib 5 µM | +2.48 | 5.6× | 7.40 | 9 |
| Epirubicin 5 µM | +2.18 | 4.5× | 6.49 | 9 |

### The graded inventory — PRE-SPECIFIED

| Grade | Drug-doses | Why |
|---|---|---|
| **A — replicated, artefact-clean, mechanism attributed** | idarubicin 5 µM; homoharringtonine 5 µM | both wells pass the call rule; the *added* CPM is nearly identical across an 8× baseline gap (idarubicin +39.9 / +40.9 CPM, 1.02× apart, against 4.4× apart in fold terms; homoharringtonine +46.4 / +30.4, 1.53×); 0 lines with zero TRIM72 reads for idarubicin and 48 of 48 lines above their own-plate DMSO expectation (sign test p 3.6e-15), homoharringtonine 47 of 48 (p 1.7e-13); both unchanged under a ≥ 5-UMI-in-both-arms restriction; neither shows a survivorship gradient |
| **B — non-replicated, with a sign flip** | mitoxantrone 5 µM | plate 6 rises **2.93×** (615 observed against 210.2 expected, 42 of 48 lines up, sign test p 5.0e-8); plate 14 **falls to 0.73×** (2,814 against 3,848, 13 of 48 up); pooled 0.84×; added CPM +5.3 then −5.4 |
| **C — artefact of the ratio-scale estimand** | dinaciclib 5 / 0.5 / 0.05 µM | 71–82% cell loss, 10.8× depth deficit, 25 of 44 lines with zero MG53 reads at 5 µM; the pseudocount floor alone is 2.545 CPM (half-count) or 5.090 (one-count) against a plate baseline of 0.883, so a line with **no reads at all** already scores 62–111% of the reported 2.478 log2. On an added-CPM scale all three doses score ≈ 0 (`R4_z` 0.674 / −0.304 / 0.000, q up to 0.969) |
| **D — untestable (single well)** | the remaining 15 of 21 — auranofin 5, panobinostat 5, doxorubicin 5, epirubicin 5, topotecan 5, harringtonine 5, ouabain 5, filgotinib 5, TAK-901 0.05, cyclosporin A 0.05 µM and the sub-maximal idarubicin and homoharringtonine doses [full list: `upstream_perturbations/tables/a_TRIM72_drugdose_ranking.csv`] | one well each; no replication is possible at any effect size |

Mitoxantrone is **not** "refuted on every count-based estimand" — that statement is withdrawn. The pooled
0.84× averages two wells whose effects have opposite signs, each individually well supported at the line
level. The correct reading is non-replication with a sign flip, which is *more* informative: no fixed
positive absolute induction can produce a sign flip, so mitoxantrone falsifies the fixed-absolute-induction
model in the one decision-relevant case where that model was testable [`verify_raisers_0/v11_mitox.py`].
(The older committed write-up gives mitoxantrone's per-plate folds as 3.9× and 1.07× from a different table;
the matched pooled-count recomputation gives 2.93× and 0.73×.)

### Compound-level extension — PRE-SPECIFIED

With the **compound** as the unit of inference (Stouffer over its three doses) and a design-preserving
within-plate label permutation (5,000 draws), exactly **three compounds** reach q_perm < 0.10 —
homoharringtonine, idarubicin and dinaciclib — all at the permutation floor p 0.0002, and one of the three
is the dinaciclib artefact. The compound family is **379** distinct compounds, not 359 (the smaller figure
merges salt forms), and **12** reach q_normal < 0.10, not 11: the four with no drug-dose among the committed
21 are gefitinib (0.064), naproxen (0.073), S-adenosyl-L-methionine (0.038) and **crizotinib** (0.096), the
last omitted from the original enumeration. None survives the permutation null (q_perm 0.55–0.73). MDE: a
three-dose compound needs a mean per-dose 0.641 log2 (1.56×) at 80% power to clear z 2.86. Dose-monotone
raisers are 12 of 334 against a null mean of 10.2 (permutation p 0.327, shuffle unit = dose label within
compound; 80% power needs 19) — a **bounded null**.

---

## 2. Only two of the 21 survive replication — and why the rest cannot be tested

**F1, PRE-SPECIFIED.** Idarubicin 5 µM and homoharringtonine 5 µM pass the call rule in *both* their wells.
Of the other 19 [`raisers/t7_replication_survival.csv`; design census confirmed in `verify_raisers_0`]:

- **mitoxantrone 5 µM** had two wells and failed, with the wells disagreeing in **sign**;
- **adagrasib 0.05 µM** passes in 1 of its 14 wells;
- **seventeen cannot be tested at all, because the design gives them one well.**

This is enumeration over the design, not a test. The reason the 17 are untestable is structural, and three
facts fix it:

1. **90.5% of all drug-doses have a single well.** There is no second measurement to disagree with.
2. **A single well cannot reach FDR 0.10 at any effect size under the natural exchangeability unit
   (EXPLORATORY).** An exact within-plate rank p has a floor of 1/94 = 0.01064, and BH over 1,132
   drug-doses needs p ≤ 8.8e-5 for the top rank, so the smallest attainable q for a single well is **12.0**.
   Every single-well call therefore rests on the normal-theory assumption for Z. The stronger claim that
   "no reanalysis can remove it" is overstated: pooling the within-plate null across all 14 plates (1,252
   drug wells, exchangeable within plate after centring) reaches a resolution near 1/1,252 = 8.0e-4, within
   an order of magnitude of what BH needs. **The floor is a property of the chosen null, not of the design.**
3. **One well's fold change is imprecise (PRE-SPECIFIED, F4).** Over 89 non-raiser cross-batch pairs the two
   independent wells agree at Spearman **+0.358** (drug-dose-label permutation, 5,000 draws, p 0.0004), with
   95% limits of agreement −0.779 to +0.824 log2 and an implied per-well SD of 0.289 log2 — so one well's
   95% error is **1.48×**. (The widely quoted 1.74× is the *repeatability coefficient*, which bounds the gap
   between two wells, not one well's error. Corrected in `verify_raisers_0`.) See
   [[Reliability and disattenuation]].

**What a single-well call is worth, PRE-SPECIFIED but inconclusive.** Of 5 drug-doses a single plate-6 well
would have called, 2 replicate — 40% replication (Wilson 11.8–76.9%), implied false-positive rate 60%
(23.1–88.2%); the three failures are mitoxantrone 5, vilanterol 5 and fluvoxamine 5 µM. Counting adagrasib
correctly, the plate-14 arm is 2 of 3 and the pooled rate is **4 of 8 = 50%** (Wilson 21.5–78.5%), with sign
concordance 5 of 6 rather than the reported 7 of 7. On the absolute scale 4 of 11 replicate (36.4%, FPR
63.6% [35.4–84.8]). With 5–8 discoveries the interval spans 57–65 percentage points; bounding the FPR to
±10 points would need ≈ 95 replicated discoveries, about 20× the current replicated design. **The MDE on the
estimate is the binding constraint, which is why this is graded inconclusive rather than "60% of single-well
calls are false."**

> [!note] The raiser list also *misses* real raisers, for a plate reason
> The committed ranking is already essentially a within-plate ranking (Spearman(`DD_z`, within-plate z)
> = 0.9846 [`upstream_perturbations/tables/a_TRIM72_plate_batch_checks.csv`, row 2]). But the 1.2× effect
> floor equals 0.26–0.28 added CPM on a low-baseline plate (median drug-well baseline 1.39 CPM) and **2.37
> added CPM on a high-baseline plate** (11.87 CPM) — 8.5× stricter. Consistently, drug-doses whose used
> wells lie only on plates 1–3 are 250 of 1,132 (22.1%) but carry **1 of 21 raisers against 4.64 expected**
> (Fisher one-sided OR 0.17, p 0.0356; 5,000-draw raiser-label permutation p 0.0368). See
> [[Plate batch effects]].

---

## 3. The length of the raiser list carries no information

**F2, EXPLORATORY — and it should be the pre-specified primary of any confirmatory run.** Running the
*identical* calling rule on 2,409 screen genes matched to MG53's expression level gives a median of **17
raisers per gene** (mean 18.2, p90 32, max 70). MG53's 21 sits at the **66.7th percentile**, and its best
single effect (`DD_z` 15.89) at the 56.5th percentile of those genes' maxima
[`raisers/t19_placebo_gene_calls.csv`, reproduced exactly from a full pass over
`export/upstream/genes_per_drugdose.csv.gz`].

The obvious objection fails. Restricting the comparator to the 419 level-matched genes with
`dog_class = unexposed` — genes structurally incapable of [[Readthrough spillover]] — *raises* the median to
**20** and moves MG53 to the **53.2nd percentile** [`verify_raisers_0`, recomputed]. See
[[Placebo genes and reference families]].

**What this does and does not say — two nulls, read correctly (PRE-SPECIFIED).**

| Null | Expected calls | Reading |
|---|---|---|
| Within-plate label shuffle | 22.2 against 21 observed, P(null ≥ 21) = 0.96 | the shuffle retains the real extreme wells, so **the count 21 carries no information** |
| No-signal null (per-well z ~ N(0, that plate's `mad_Z`), 2,000–5,000 draws, same design, BH within each draw) | **0.12–0.14** calls (median 0, p95 1, P(≥ 21) ≤ 0.0005) | the **procedure is not miscalibrated**; per-plate z-scale variation (`mad_Z` 0.528 on plate 2 to 1.350 on plate 4) contributes ≈ 0.1 expected calls, not 21 |

So the placebo median of 17 does **not** say the 21 are false positives. It says drugs change gene
expression pervasively and that MG53 is unremarkable among genes of its level. The two results answer
different questions, and both belong in any statement about the list. See
[[FDR calibration and the inflated null]].

Two caveats the source carries: the placebo calibration is a **point estimate of a random quantity** (21 is
itself a noisy count from a design that is 90.5% single-well, and "66.7th percentile" is quoted with no
interval on the 21); and the screen-gene universe is itself **selected on MG53** — 4,144 of 4,586 screen
genes entered because their line-level common slope against MG53 reached q < 0.1 — which biases MG53 toward
looking *less* exceptional than it is. The level-matched subset reduces but does not remove this
([[Cross-fitting and circularity]]).

---

## 4. Drugs that lower MG53

Lowering is **largely unverified** in the source; the design facts below are confirmed.

Exactly **1 of 1,132** drug-doses reaches the committed lowering rule: **ponatinib 5 µM** (`DD_qdn` 0.015,
corrected log2 −1.34, 0.39×, z −4.21) — a single plate-12 well
[`mg53_p53/findings/tables/tableB_upstream_mg53.csv`]. Other committed falls: trametinib 0.05 µM −1.05,
cabozantinib 5 µM −1.00, anethole trithione 5 µM −0.72 log2.

Of **41** nominal falls (z ≤ −2), only **trametinib 0.05 µM and radotinib 5 µM** are replicated (two wells
each; pooled counts fall 0.535 and 0.851 log2). **NG25 5 µM and pralsetinib 5 µM** fall hardest but are
single plate-3 wells where the whole transcriptome falls.

The mechanism signature of the lowerers is the mirror image of the raisers', and it is not p53:

| Across the 41 nominal falls | Falls | Rest | Test |
|---|---|---|---|
| Genome-wide readthrough index | **−1.249** | +0.022 | Mann-Whitney p 3.05e-15 |
| Locus-readthrough overlay | **−0.0747** | +0.0022 | p 1.27e-10 |
| Derived p53 program `PROG_P24` | −0.0116 | −0.0164 | p 0.502, **MDE80 0.013 in program score** |

That is evidence *against* drug-induced p53 activity mediating the falls. Simplest reading: **less
readthrough spillover into TRIM72, not less MG53 transcription.**

### Drug classes — PRE-SPECIFIED, bounded null

With the compound as the unit and activity matching, **no drug class raises MG53 at FDR 0.10.** The smallest
q over the 189 class rows is 0.2183 (TOP2 poisons: 5 compounds, 4 raisers against 1.403 expected, O/E 2.85;
DNA-damaging cytotoxics, 22 compounds, p 0.0103). Recomputing BH over all 189 rows for that statistic gives
q 0.5575, and over 189 rows × 4 statistics (756 tests) the smallest q anywhere is 0.3024 — all reproduced
exactly. Leave-one-out removes most of the apparent signal (TOP2 poisons residual mean z 4.956 → 2.561;
anthracyclines 7.679 → 4.251). MDE: with 5 compounds in a class and a background compound-level raiser rate
of 21/1,132, 80% power at FDR 0.10 over 189 classes needs **O/E ≥ 4.5**; observed 2.85.

> [!warning] Do not quote the unstratified TOP2 result
> The unstratified Fisher test reaches q 4.8e-4 for TOP2 poisons, but it is not activity-matched, and TOP2
> poisons are among the most transcriptionally active compounds in the screen. That q is confounded.

The one class-level signal that approaches FDR control is **lowering, by tyrosine-kinase inhibitors**, and
whether it survives depends entirely on the family definition. Tahoe's mixed "Other TK inhibitor" class
(14 compounds; nominal lowerers infigratinib, larotrectinib, pralsetinib, radotinib, tirabrutinib) has mean
z_min −1.566, residual −0.871, p 0.0004 → q 0.00999 within the 25 `moa_fine` rows, 0.0756 over all 189 rows,
0.3024 over 756 tests. It survives leave-one-out (−0.737). Treat it as a **hypothesis for a replicated
design**, not a finding.

---

## 5. Readthrough spillover: the leading account, strand-resolved but not quantified

[[TRIM72]] sits **10.6 kb 3′ of PYCARD-AS1** and **17.05 kb 3′ of [[FUS]]** on the same strand, and FUS runs
at 252 CPM against TRIM72's 5.33 [`upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv`, row 0:
`pooled_cpm` 5.33, `DoG_class` sense_exposed, `up_same_strand_expressed_gene` FUS]. Transcription that fails
to terminate at FUS or PYCARD-AS1 is counted as TRIM72 mRNA. That is [[Readthrough spillover]], and it is a
statement about position, never about regulation. Mechanism detail lives in [[The TRIM72 locus]]; this
section carries only what the upstream analysis established.

### The strand-specific evidence — PRE-SPECIFIED

**F3.** In the 15 raiser wells, two co-positional genes move in **opposite** directions
[`verify_raisers_0`, recomputed from `upstream_coregulation/tables/c_locus_obs_over_exp_raiser_wells.csv`]:

- **the plus-strand genes on the readthrough path 5′ → 3′ of TRIM72 rise**: median excess **+0.856 log2**,
  14 of 15 wells, Wilcoxon one-sided **p 9e-5** (shuffle unit = well);
- **[[PYCARD]], co-positional with PYCARD-AS1 to the base pair but on the minus strand, falls**: median
  **−0.495**, 14 of 15 wells negative, **p 0.00131**. Spearman between the two series is −0.629.

MDE for the paired strand contrast is 1.109 log2 with 15 wells. Two co-positional genes moving in opposite
directions is the cleanest available demonstration that the quantification is **strand-aware**, and it is
stronger evidence for the mechanism than the single median contrast it replaces (§8). It carries two costs:
PYCARD's fall is a second, unexplained phenomenon at the locus, and ≈ 32% of the original contrast came from
the control falling rather than the path rising, so that contrast **overstated the plus-strand rise by
≈ 1.5×**.

One honest counter-example is in the data. **PYDC1**, a minus-strand gene lying *inside* the TRIM72 gene
body (31,215,962–31,217,162 within 31,214,017–31,231,537), **rises** in 10 of 15 raiser wells (median
+0.707, p 0.042) and is strongest where TRIM72 is strongest. With a median expected count of 1.10 it is not
decisive, but it does not fit a simple strand-specific spillover account.

### The flux model over-predicts — EXPLORATORY

A one-parameter flux model calibrated on the plate-batch contrast (**κ = 5.36–8.00 CPM to TRIM72 per CPM to
PYCARD-AS1**, from three independent calibrations) **over-predicts the observed rise by 59% at the median**,
with per-well attributable fractions running from **−140% to +742%** [`raisers/t15_readthrough_attribution.csv`;
`verify_raisers_0`]. So the account is **order-of-magnitude consistent and not quantitatively accounted
for**. Declaring 11 of 14 wells "fully accounted for" because the attributable ratio exceeds 100% turns
systematic over-prediction into a success criterion, and that framing is withdrawn (§8). Note also that the
free-fit κ is fitted on the same 15 raiser wells whose attribution it supports, so its R² 0.924 restates the
premise; only the two plate-based κ are external, and they assume the unexplained plate gap is pure
readthrough.

### It is locus-local, not a genome-wide termination defect — unverified in detail

The readthrough index was not rebuilt, so this is **unverified**, but the pattern is clear: **8 of 21
raisers sit in the top tail of the genome-wide sense readthrough index and 7 sit in the bottom tail**, with
idarubicin 5 µM among the latter at **rank 1,104 of 1,132**, while its own locus neighbourhood rises sharply
and FUS gains 189.5 CPM in its plate-6 well [`upstream_coregulation/tables/c_DoG_index_by_drugdose.csv`;
`c_locus_strand_summary_raiser_wells.csv`, row 1]. **The effect is locus-local.**

### Across drug-doses and across lines — PRE-SPECIFIED

| Quantity | Value | Null / interval |
|---|---|---|
| Sense readthrough index vs MG53 across drug-doses | Pearson **+0.322**, Spearman **+0.458** (pipeline's own 0.451) | drug-block permutation z 9.3–9.6, p 2.5e-4–5.0e-4, MDE80 \|r\| 0.095–0.097 |
| Named index estimand (sense minus antisense, unit weights) | r +0.497, **R² 0.246** | drug-cluster bootstrap 95% CI **[0.119, 0.486]**; 0.206 dropping the 5 most extreme drug-doses |
| Strand contrast, incremental R² over technical covariates + plate | **+0.307** | far above drug mechanism of action (0.002 broad, 0.083 fine) or plate (0.007–0.021) |
| Readthrough-exposed share of MG53's top-100 raw partners | **47%** against 4.218% of all 16,642 genes | level-matched 5,000-draw resample still expects only **5.5–8.4%** (SD 2.2–2.7), z 14.3–17.4, p 2.0e-4 at the permutation floor, MDE80 11.8–16.0% |

**The crucial qualification.** MG53's readthrough enrichment is **specific relative to expression level and
typical relative to readthrough geometry.** Against 300 expression-matched genes MG53 sits at the 96.7–99.0
percentile (empirical p 0.013–0.037, BH over five variants q 0.028–0.037 — survives). Against the **39
matched genes that are themselves readthrough-exposed** it sits at the 84.6–94.9 percentile, which converts
to empirical **p 0.075–0.175, never below 0.05 in any variant**, on a design whose attainable floor is
1/40 = 0.025 [`upstream_coregulation/tables/a_null_summary.csv`, rows 0–1]. The same source table puts the
TRIM72–FUS baseline correlation at the 99.9th percentile of genes at FUS's level **and at the 56.6th
percentile among readthrough pairs**; the analysis quoted only the first half. This cuts both ways: it is
good evidence that readthrough is the right account, and direct evidence that MG53 is not special within it.

Note also that **plate batch is confounded with the readthrough signal by construction**: MG53's untreated
plate gap of 3.124 log2 (8.7×) is the largest of 16,656 genes, and readthrough-exposed genes as a class
share a 0.264 log2 larger gap (p 1.6e-66). Any genome-wide readthrough statistic partly re-measures the
thing that creates MG53's batch structure. See [[Plate batch effects]] and
[[Why MG53 is hard to measure here]].

---

## 6. Transcription factors: a bounded null, and the muscle programme is silent or absent

**F9, PRE-SPECIFIED.** Nothing that behaves like a transcriptional regulator of MG53 survives removal of the
generic drug-response axes. Begin with how much room is left: the **top 10 principal axes of the drug-dose
gene matrix carry 62.8% of MG53's across-drug-dose variance, the top 20 carry 83.4%**
[`upstream_coregulation/tables/a_pc_variance.csv`, exact orthogonal decomposition]. PC1 alone — a
library-quality/stress axis (r −0.645 with RMS z, +0.495 with cell loss) — carries 26.7%; PC8 is the
anthracycline axis. That is the quantitative reason any partner list collapses when the axes are removed.

### Regulon activities — list-based, PRE-SPECIFIED

Of **679 CollecTRI regulons, 473 reach q < 0.1** across drug-doses (348 positive, 125 negative), so
**significance is uninformative and only the margins matter.** Maximum r is **0.359** ([[ATF5]], drug-block
CI 0.289–0.430, 25 targets), then [[ATF4]] 0.357, [[TWIST1]] 0.354, GCM1 0.353 (6 targets), TWIST2 0.351;
the minimum is [[NAB2]] −0.377 (6 targets); median |r| 0.106. **409 of 679 CIs exclude zero, and 64 of the
473 "significant" TFs have a drug-block CI spanning zero.** Four of the top eight rest on 5–13 targets.
MDE80 |r| ≈ 0.112 for a single TF (median drug-block/jackknife SE 0.040; the iid Fisher SE of 0.031 is too
small), ≈ 0.15 after BH. See [[Transcription factor activity inference]].

The overlap control removes most of it. Over the top 50 TFs, dropping AP-1/IEG/[[ATF3]] targets from each
regulon costs a median **0.123** (37 of 50 testable; ATF5 falls 0.359 → 0.003 on 10 remaining targets),
partialling ATF3/[[PMAIP1]]/DDIT3/IEG/AP1 costs **0.108**, and both together cost **0.177**, leaving median
r **0.092 — below the single-test MDE** — with 22 of 37 at q < 0.1 and the same sign. Surviving leaders:
[[ZNF91]] 0.322, TWIST1 0.212, [[APEX1]] 0.174, [[SRF]] 0.168. ZNF91 should not be read as a survivor: its
r *rises* from 0.290 to 0.437 when overlap targets are removed, on 11 remaining targets, which is small-n
instability.

### Within lines — PRE-SPECIFIED, bounded null

187 of 681 labels reach q < 0.1 but **every |r| ≤ 0.080**; the maximum is +0.0714 (MYBL1) and the minimum
−0.0801 (E2F4, a cell-cycle readout). MG53's own measurement-noise ceiling, measured in the identical model
from single co-responding genes, is FOS 0.0801, EGR1 0.0668, [[FUS]] 0.0663, JUN 0.0631, ATF3 0.0621. Median
MDE80 is **0.026–0.027 in partial-r units** (IQR 0.023–0.032), so the study can detect |r| ≥ 0.027: **this
is a bounded null, not missing power.** The drug-dose leaders are flat within lines (ATF4 −0.008, ATF5
−0.007, AP1 ≈ 0). See [[Two-way fixed effects]] and [[The screen model]].

### List-free, with the TF census used only as a label — EXPLORATORY, and cleaner

Ranking all 16,642 genes by correlation with MG53 and labelling TFs afterwards: the best TF mRNA is **FOSB
at rank 63 of 16,642** (r 0.582 with covariates, q 9.7e-66, 99.3rd percentile of level-matched genes); at
minus-10PC FOSB is 0.498 (rank 43), ATF3 0.467 (67), FOS 0.404 (151). **Only 1–3 of 1,217 TFs reach the top
100 against 7.31 expected** (2/2/3/1/2 across the five variants). Median r of TF mRNAs is 0.019 against
0.046 for non-TFs, and TFs are **under-represented** among MG53's partners (Mann-Whitney AUC 0.454,
p 6.3e-8; 0.418, p 2.1e-21). The CollecTRI leaders rank poorly as their own mRNA: ATF5 1,131st, ATF4
4,150th, SRF 3,542nd, TWIST1 5,062nd, [[TP53]] 1,422nd, [[MEF2D]] 11,021st.

> [!important] FOSB is the one candidate the negative conclusion does not cover
> FOSB is rank 63 with covariates and rank 43 with 10 PCs removed, runs at 51.8 CPM, sits in the stable core
> of all five variants, and has **no readthrough source 5′ of it**. It is neither a PC artefact nor
> geometry. "Nothing that behaves like a transcriptional regulator survives" is therefore an **assertion,
> not a finding**, until FOSB's rank is compared against the most drug-responsive genes generally — a cheap
> test that was named and not run.

### The muscle factors that drive TRIM72 in its native tissue are silent or absent here

| Factor | Level in DMSO pseudobulk | Correlation of its own mRNA with MG53 | Reading |
|---|---|---|---|
| [[MYOD1]], [[MYF5]], [[MYF6]] | **0.000 CPM** | — | **no MDE exists; the quantity is unmeasurable, not merely undetected** |
| [[MYOG]] | 0.018 CPM | — | as above |
| [[MEF2A]] | 298.5 CPM | **−0.175** | expressed, wrong sign |
| [[MEF2B]] | 13.8 CPM | −0.037 | expressed, null |
| [[MEF2C]] | 21.8 CPM | **−0.165** | expressed, wrong sign |
| [[MEF2D]] | 86.8 CPM | −0.026 | expressed, null |

The curated MUSCLE_TF set has mean r **−0.046** (p 0.457, MDE80 set |r| 0.197) and −0.055 at minus-10PC, and
baseline MEF2 activity against untreated MG53 across lines is ρ **−0.104 to −0.273** (all q ≥ 0.30, MDE80
|ρ| 0.412). Dropping [[SRF]] takes the set to −0.101, so the near-zero is if anything **generous** to a
muscle-enhancer account. SRF's regulon reaches 0.308 but its own mRNA only 0.172 (rank 3,542), falling to
0.168 after both corrections.

Two list artefacts to know about, because they produce fake muscle signal: CollecTRI lists **TRIM72 itself
as a MYOD1 target**, which is why TRIM72 and every gene within 200 kb had to be removed from all regulons;
and the MYOD1 *regulon* nominally "tracks" MG53 at r 0.086 (q 0.015) even though MYOD1 is at 0 CPM
[`upstream_tf/tables/a4_muscle_promoter_tfs.csv`].

> [!tip] The under-weighted positive: MUSCLE_STRUCTURAL
> **F11, EXPLORATORY.** MUSCLE_STRUCTURAL (MYH3, TNNT1, TNNT2, RYR1, ATP2A1, DYSF) is the **only one of 44
> gene sets to survive BH over the whole gene-set family**, in two variants: mean r **+0.318** (z 3.50,
> p 0.0015, q_BH 0.0073) with covariates, and **+0.229** (z 3.28, p 5.0e-4, q 0.0031) with 3 PCs removed,
> against level-matched random sets [`verify_genomewide_0/v5_gene_set_tests_with_q.csv`]. Both grounds
> offered for dismissing it fail: removing ATP2A1 (the 16p11.2 member) leaves 0.307 and 0.207, and the null
> is level-matched by construction. For a project about a muscle gene this is the most under-weighted result
> in the material, and it deserves its own pre-specified test rather than a parenthesis.

---

## 7. Is the p53 pathway itself upstream of MG53?

The source treats this explicitly, and the answer is a **bounded null, not "no regulation"**. Fuller
treatment of the pathway is in [[The p53 pathway]] and [[p53 program P]]; the arms and the per-line measure
are in [[Per-line p53 function]] and [[p53 nullification in cancer cell lines]]; the reverse direction is
[[Downstream of MG53]].

### The pre-specified primary should be struck

**PRE-SPECIFIED, since invalidated.** The registered estimand was the difference in the slope of MG53 log2
induction on p53-pathway activation between the **11 p53-functional** lines and the **10 core p53-null**
lines, inferred from a cell-line label shuffle (≥ 2,000 draws, shuffle unit = cell line). It returned
**+0.800 log2 per unit of program activation = +4.22% per SD of exposure** [CI +0.43% to +8.17%], line-shuffle
p 0.027–0.033, exposure-shuffle p 0.0001, **MDE80 1.032 log2 = 5.4% per SD** — i.e. **the point estimate was
already below its own MDE** [`p53_regulates/t1_primary_interaction.csv`]. Two defects dissolve it:

- **Triple circularity.** `program_P_delta_log2` (the exposure) is defined as the mean WT-minus-altered
  difference over program-P genes, `in_S2_p53_activating` is a permutation FDR computed against **TP53-label
  permutations**, and the **arms themselves** come from `functional_call`, a threshold on induction of
  program P. The positive controls — [[CDKN1A]], [[MDM2]], DDB2, ZMAT3, FDXR, BBC3, BAX, [[ATF3]] — are all
  members of program P. Recovering one's own labelling criterion is not a demonstration of power. See
  [[Cross-fitting and circularity]] and [[Program P derivation]].
- **p53 function is perfectly collinear with TP53 genotype.** All 11 functional lines are TP53-WT and all 10
  null-core lines are TP53-altered. The panel contains no p53-null TP53-WT line and no p53-functional
  TP53-mutant line, so **no arm pair in this dataset separates p53 function from TP53 genotype.** This is a
  property of the panel, not a correctable analysis choice.

Under a **genotype-preserving** shuffle (functional arm drawn only from the 17 TP53-WT lines, null arm only
from the 32–33 altered, K = 5,000) MG53 gives **p 0.339** — but so does CDKN1A (**p 0.350**), which is why
the two independent recomputations read that null oppositely: one holds it invalid because a random
WT-vs-altered split is *itself* a p53-genotype contrast and absorbs real signal; the other holds that this
*is* the finding, since a random WT-vs-altered arm pair already reproduces 85–91% of each positive control's
slope. **Both readings support the same operational conclusion: the pre-specified primary was never a
defensible positive and the p 0.026–0.033 should be struck.** The published figure belongs to TP53 genotype,
not to p53 function.

### The non-circular replacements — all EXPLORATORY, all moving toward the null

**F8.** The knockout-controlled estimand is extra MG53 induction in the 11 functional over the 10 null-core
lines per SD of p53-pathway activation [`p53_regulates/t14_noncircular_exposures.csv`;
`t15_mg53_summary_by_exposure.csv`]:

| Exposure | MG53, per SD | 95% CI | p (line shuffle) | MDE80 | CDKN1A, same statistic |
|---|---|---|---|---|---|
| Leave-arms-out WT-minus-altered differential (6 WT minus **22** altered lines in neither arm) | **+2.88%** | −0.16% to +6.02% | 0.059–0.061 | 4.34–4.38% | **+14.07%** (MDM2 +15.05%) |
| All-line panel P53_ACTIVITY level | +2.37% | −2.48 to +7.47 | 0.33–0.36 | 7.12–7.19% | +7.71% (p 0.0044) |
| P53_SCORE level over the 28 lines in neither arm | +1.54% | −2.85 to +6.14 | 0.49–0.51 | 6.50–6.53% | +4.66% (p 0.019) |

Standardised, MG53's interaction is **7.9–12.3% of CDKN1A's**. Nothing in the pre-specified family of five
survives BH (minimum q **0.069**; **0.0575** on the verifier's own p-vector)
[`p53_regulates/t16_multiplicity_prespecified.csv`], and the three smallest p-values in that family are the
three now known to be circular or selection-driven. A multivariable test is more informative than either
shuffle: adding a *generic* WT-minus-altered differential drops the p53 differential from +0.798 (p 0.030)
to +0.529 (p 0.206), and to +0.323 (p 0.477) with four generic differentials, while the generic **stress**
differential alone is +1.328 (p 0.0006) [`verify_p53_regulates_1/v3_multivariable.csv`].

### Everything mechanistic points the wrong way or nowhere

- **Specificity across drug-doses, PRE-SPECIFIED.** Over 1,086 kept drug-doses, a drug-dose's p53-programme
  activation and its MG53 induction correlate at Spearman **+0.0230 (p 0.4488)**, Pearson +0.0892
  (p 0.0033), MDE80 |ρ| 0.085 — so under 0.8% of variance either way cannot be excluded.
- **Dose dissociates the two within single drugs, PRE-SPECIFIED.** Idarubicin's programme activation is
  maximal at 0.5 µM (0.655) where MG53 rises 2.15×, and lower at 5 µM (0.367) where MG53 rises **12.24×**.
  Homoharringtonine activates p53 at 0.05 µM (+0.384) and 0.5 µM (+0.272) and not at 5 µM (−0.009), while
  its MG53 folds run 0.98× / 5.87× / 10.26× — within-drug Spearman **−1.0**. Across 352 three-dose drugs,
  the dose that maximises p53 activation is the dose that maximises MG53 **0.332 of the time against a
  chance rate of 0.333** (binomial p ≈ 1.0; mean within-drug Spearman −0.021, Wilcoxon p 0.510).
- **Named discordances** (checked against the whole distribution for cherry-picking — none found; the three
  most negative programme deltas in the screen are all large MG53 raisers): selinexor 5 µM activates p53
  (+0.3145, q 1.56e-4) with MG53 at **0.81×**; auranofin 5 µM has the most negative programme delta in the
  kept screen (**−0.2852**) with MG53 at **6.56×**; dinaciclib 5 µM −0.2776 / 5.57×; panobinostat 5 µM
  −0.2645 / 2.70×.
- **No p53 site at the locus.** TRIM72 is bound in **2 of 393** public TP53 ChIP-seq experiments (both
  SW-480), rank 14,170.5 of 16,173, against CDKN1A's 261/393 at rank 1, and is absent from all three Fischer
  2017 lists [`mg53_p53/literature/chipatlas_tp53_binding_check.csv`;
  `fischer2017_p53_census_check.csv`, run_date 2026-10-22]. **This excludes a *strong* canonical site, not
  any site**: ATF3, a Fischer high-confidence target, is bound in only 30/393 — the same count as GAPDH.
- **Across lines, PRE-SPECIFIED.** Untreated MG53 against basal p53 activity is ρ **+0.003 (p 0.982)**, and
  TP53-WT minus altered is +0.279 log2 (p 0.918); all 7 TP53-group line tests sit at q_BH 0.378–0.976, with
  MDE80 |ρ| 0.412 and 0.841 SD for the mean difference.

### Two residual positives that run the other way, both EXPLORATORY

- **F10 — tail enrichment.** MG53 raisers *are* enriched among p53-activating drug-doses in the tail, and at
  `DD_z` ≥ 2 the enrichment survives amplitude stratification: 17 of 142 against 26 of 944, **OR 4.80,
  p 7.9e-6**, with permutation of the activating label within deciles of `n_sig_genes` giving p 0.0031. At
  `DD_z` ≥ 3 it does **not** survive (7 against 5.19 expected, p 0.225; Mantel-Haenszel OR falls from 4.40
  crude to 1.74) [`verify_p53_regulates_1/v7_tail.py`]. The screen's own unstratified Fisher test is OR 46.5,
  p 2.1e-11 (10 of 36 strong activators up against 9 of 1,096). Honest reading: **MG53 tracks total p53
  activation only in the extreme tail, and there mostly through response amplitude.**
- **The TP53 regulon correction, which runs against the null.** The TP53 CollecTRI regulon's rank is **227
  of 679** by covariate-adjusted r, not 540, and its correlation with MG53 **rises** as the shared stress
  axes are removed: 0.1162 raw → 0.1213 covariates (q 4.5e-4) → 0.1332 minus-3PC → **0.1976 minus-10PC
  (q 2.7e-9, rank 115 of 679)** [`upstream_tf/tables/a1a2_tf_summary.csv`; corrected in
  `verify_genomewide_0/v6_tp53_rank_definitions.csv`]. At 0.1976 it clears the single-test MDE80 of 0.112,
  so **this is not a bounded null**, and the stated mechanism ("the raw association is the shared
  anthracycline/stress axis") is contradicted for the regulon by the project's own table. The fair framing:
  468 of 679 regulons reach q < 0.1 at minus-10PC and the maximum there is ATF4 at 0.417, so TP53 at rank
  115 is **mid-pack — not special, but not absent.** With the mediators partialled, TP53's regulon r goes
  +0.121 → −0.019 (overlap removed) → **−0.183 (q 4.4e-7, sign reversed)**.

### Verdict

**Bounded null for p53-specific regulation of MG53**, with one unresolved per-line association (ρ +0.31
fully adjusted, below its own MDE of 0.42, and confined to the drug-doses selected because MG53 rose in
them — see [[Per-line p53 function]]) and the tail positive above. The claim this licenses is
**"MG53 is not a canonical p53 target and its p53-specific induction is at most about 0.43× CDKN1A's"** —
not "no regulation." Nothing short of direct p53 manipulation (nutlin-3a, or an isogenic TP53-knockout pair,
read at several timepoints) identifies direction. See [[The measurement with controls]] and
[[Nulls and calibration]].

---

## 8. Claims dropped, withdrawn or corrected

These were published or asserted and did not survive independent recomputation. The list is part of the
result, not an appendix to it. The ledger note is [[Corrections and retractions]].

### Withdrawn outright

| Claim | What replaced it |
|---|---|
| "21 drug-doses raise MG53" as a standing result | **At risk.** 2 of 21 replicate; 17 are untestable; the count 21 sits at the 66.7th percentile of level-matched genes |
| **Dinaciclib** as a supported raiser | **Refuted.** Moved to artefact, on the floor argument *and* the added-CPM result (`R4_z` ≈ 0 at all three doses) |
| **Mitoxantrone** as a replicated raiser | **Refuted as stated.** Non-replication with a sign flip (2.93× plate 6, 0.73× plate 14), which also falsifies the fixed-absolute-induction model |
| Mitoxantrone "refuted on every count-based estimand" | Withdrawn; each well is individually well supported at the line level, with opposite signs |
| "Quantitatively accounted for by readthrough spillover" | Withdrawn. A one-parameter model that **over-predicts by 59% at the median** cannot support it; per-well attributable fractions run −140% to +742% |
| The strand control as **one** contrast (median +1.032, 13 of 15 wells, Wilcoxon p 0.00214, sign test p 0.00369) | Withdrawn. Those four numbers come from **three different control-gene sets**, and p spans 0.00015–0.01508 across control definitions. Two control members are inadmissible on the test's own logic: ENSG00000260304 begins at 31,182,511, inside the FUS gene body, and PYDC1 has a median expected count of 1.10, failing the pipeline's own ≥ 5 filter in 14 of 15 wells. Replaced by the two separate numbers in §5 |
| The **R4 "plate-advantage-free" ranking**'s entering and leaving lists | Withdrawn. The estimand is under-specified (it does not say whether the per-well statistic is a cross-line median or a pooled sum) and does not reproduce: 41 calls at q < 0.10 rather than 65, Spearman(`R4_z`, `DD_z`) 0.666 rather than 0.716, top-21 overlap 14 rather than 15, and it does **not** contain all 21 committed raisers. The headline new candidate (lonafarnib 5 µM) does not enter at all. What survives is the *direction*: an absolute-scale ranking is well calibrated (no-signal null 0.11 calls) and is the right scale given the baseline gap |
| "A single well's fold change can be wrong by 1.74×" | **1.48×.** The 1.74× is the repeatability coefficient, which bounds the gap between two wells |
| The **correlation-ceiling** argument (that MG53's observed partner correlations exceed what its reliability permits) | Withdrawn. `r_obs ≤ √(λ_x λ_z)` holds only when the two measurements' errors are independent, which is the condition this material argues against — and for readthrough partners it fails more deeply, because transcription past FUS is *literally counted* as TRIM72 mRNA, so those measurements share **signal**, not merely error. The input was also wrong (drug-dose-grain reliability 0.280, ceiling 0.529, not 0.250/0.500) |
| "p53 regulon r 0.121, rank 540 of 679, collapses under PC removal" | **Refuted.** Rank 227; r *rises* to 0.198 at minus-10PC (rank 115, q 2.7e-9). No rank definition of fourteen tried yields 540 |
| Specificity's "adjusted Spearman +0.0825 (p 0.0065)" | **Dropped as a number.** Both verifiers reproduced it as a Spearman of *linear* residuals; a rank-consistent partial Spearman gives **+0.022 to +0.030 (p 0.35–0.36)**. The conclusion ("under 1% of variance either way") is unaffected |
| "Median within-drug Spearman −0.50" between p53 activation and MG53 | Dropped as a headline: with three doses a Spearman takes only five values, so the median is an artefact of the discrete support. The replacement statement is stronger (§7) |
| The pre-specified p53 primary at p 0.026–0.033 | **Struck** (§7) |
| The AP1 and ATF3 rows of the regulon overlap-control table | **Structurally invalid, never to be read as results.** AP1's activity and ATF3's z *are* the partialled mediators, so those two TFs are regressed on themselves (AP1 0.196 → −0.016 with 402 targets unchanged; ATF3 0.171 → −0.053, both with 0 targets left) |
| The unstratified TOP2-poison Fisher q 4.8e-4 | **Must not be quoted** — not activity-matched, and TOP2 poisons are among the most transcriptionally active compounds in the screen |

### Corrected numbers

| Published | Corrected |
|---|---|
| "51 of 52 low genes at r ≥ 0.4 are readthrough-exposed, OR **193**" | Variant selection inside a pre-specified family: the OR is monotone in the number of PCs removed — **raw 2.234** (637-gene module, 34.07% exposed, p 6.3e-15), covariates 41.79, minus-1PC 26.37, minus-3PC 98.2, minus-10PC 192.7. Over *all* low-expressed genes at r ≥ 0.4 the module has **83** members, not 52, and on a graded definition **70 of 83 = 84.3%** are readthrough geometry, whole-module **OR 18.3** (p 5.6e-34). The correction **strengthens the biology and reduces the headline odds ratio tenfold** |
| Readthrough index variance share **0.291** (r 0.540) | The *named* estimand (sense minus antisense, unit weights) gives r +0.497 and **R² 0.246**. The 0.291 pair is the multiple-R² of a *freely fitted* two-predictor OLS (weights +1.728, −3.388) compared against a null SD calibrated for a single correlation. Drug-cluster bootstrap CI **[0.119, 0.486]**; 0.206 dropping 5 drug-doses. The index also contains TRIM72 itself and its strongest partners (self-weight ≈ 0.2%), so it is a **coherence statistic, not an identified driver** |
| "TRIM72 has a typical number of partners (5,881 against a matched median 5,330)" | Holds **raw only**. With covariates MG53 is at the **29th percentile** (1,405 against 2,797); `TRIM72_pctile_n_partners` is 59.67 raw and 29.0 with covariates, reaching the 100th percentile only once PCs are removed (660 against a matched median 13.5) |
| "The stable core is low-expressed readthrough genes" | Wrong for about a fifth of it. Of the 54 core genes, **32 are strictly readthrough-exposed, 42 have a more highly expressed same-strand neighbour within 20 kb, and 12 have no plausible spillover source**; 14 are above 10 CPM and 4 above 50 CPM. The named leader **LRRC23 is 64.2 CPM with its nearest same-strand neighbour 2.8× *less* expressed** — readthrough cannot raise it. FOSB (51.8 CPM) is also in the core |
| "Exactly 1 of 681 labels exceeds the within-line noise ceiling" | **Slice-dependent.** The table holds four slices (2 TRIM72 versions × 2 covariate sets) and in three of them 2–3 labels exceed their slice's ceiling, **always including the p53 activated-target set** (−0.0765 to −0.0829 against ceilings 0.070–0.080). The direction is negative, so this does not make p53 a positive activator, but the figure is 27–38% larger than the −0.060 reported, and the slice was not declared as a choice |
| "1–3 of 1,217 TFs in the top 100, 2 in all four variants" | 2/2/3/1/2 across the **five** variants |
| "7 of the 12 strongest p53-programme activators do not raise MG53" | **6** (folds 0.848–0.984×); 8 of 12 are not significant raisers, with folds 0.848–1.495× |
| "Plate 6 vs plate 14 pair agreement r 0.75 / 0.28" | **0.775 and 0.321** (Pearson) |
| "All 14 plates negative in Tahoe's own DESeq2" | **13 of 14.** Plate 9 is positive, and it carries five single-well raisers |
| Untreated MG53 spread across lines "46×" | **21.4×** by pooled DMSO CPM, or 24.4–25.9× from recomputed line effects. The 46× came from a median-of-per-plate-log2-CPM estimator whose low end is set by the count floor on the shallow plates |
| Organ explains R² 0.186 of untreated MG53 | A **12-parameter** R² listed beside one-parameter ones; **adjusted R² is −0.085**, and lineage is null (Kruskal-Wallis H 9.19 over 13 organs, p 0.708). The reported H 3.31 / p 0.653 is a 6-group pooled version — the statistic and the df did not go together |
| Leave-arms-out exposure composition "6 WT minus 28 altered" | 6 WT minus **22** altered |
| `mde_diff_80_attenuation_corrected` with λ = 0.288981 (3.46×) [`two_way/tables/d1_two_way_models.csv`] | **Understated by 3.6×** on the λ this work supports (0.080) — and the correction is the wrong kind under correlated errors. See [[Reliability and disattenuation]] |
| "12.4% of profiles zero" | Correct **with its denominator**: 12.42% of usable profiles from expressing lines; 13.69% of all usable; 16.56% of all 66,449 |

### Unstable rather than wrong

Several permutation p-values do not survive a second implementation of the same stated test — raiser cell
loss 0.20 against 0.41, composition shift 0.0018 against 0.0064 — so **the null means and MDEs, which do
reproduce, are what should be quoted**, not the p-values. Likewise the floor-share figures are
convention-dependent (half-count gives 62%, one-count 111%), and an independent reconstruction of "floor
above plate baseline" returns dinaciclib ×3 **plus doxorubicin 5 µM** rather than dinaciclib ×3 plus
topotecan.

### A wording conflict worth knowing

`mg53_p53/findings/tables/tableB_upstream_mg53.csv` labels locus neighbours "upstream (5')" and "downstream
(3')". That is the **positional** sense, which this vault reserves for regulation — see the convention in
[[Readthrough spillover]] and [[How the numbers are decided]]. Read those column values as "5′ of TRIM72"
and "3′ of TRIM72"; nothing about the numbers changes.

---

## 9. Artefacts that travel with the raiser list

**PRE-SPECIFIED, bounded null.** Against activity-matched permutation (raiser label permuted within deciles
of log1p(`n_sig_genes`), 5,000 draws), the 21 raisers are **not more cytotoxic** than transcriptionally
comparable drugs: cell loss −0.4475 against −0.0102, difference −0.437, but the matched null centres at
−0.301 to −0.305, giving p 0.20–0.41 with MDE80 0.452–0.456 log2. The only indicator that separates them is
a small excess composition shift (−0.0933, p 0.0018–0.0064, MDE80 0.058). Floor-driven index p 0.086,
zero-line fraction p 0.47, depth deficit p 0.15. Twelve of 21 carry no artefact flag; six carry two or more
[`raisers/t18_artefact_permutation_tests.csv`, `t17_artefact_flags.csv`].

**One artefact the screen missed, and it runs through most of the list (EXPLORATORY).** Within raiser wells,
lines that lost more cells show **larger** MG53 gains: median Spearman(per-line cell loss, per-line MG53
gain) = **−0.251**, negative in 16 of 21 raisers, sign test p 0.0266, Wilcoxon one-sided p 0.0016,
MDE 0.147. Eight are individually significant: doxorubicin 5 µM (−0.518, p 2e-4), mitoxantrone 5 (−0.516,
p 2e-4), topotecan 5 (−0.429), homoharringtonine 0.5 (−0.404), panobinostat 5 (−0.380), harringtonine 5
(−0.358), dinaciclib 0.05 (−0.357), epirubicin 5 (−0.321) [`verify_raisers_0/v10_surv.py`]. Per-line cell
loss and per-line sequencing depth are themselves confounded, so this cannot separate true survivorship
from a per-line floor/depth effect — but either way it is a **line-level, depth-dependent inflation running
through the raiser list**, invisible to a screen that used drug-dose-level cell loss.

**It also strengthens the two survivors:** idarubicin 5 µM (ρ +0.076, p 0.61) and homoharringtonine 5 µM
(−0.251, p 0.089) are **the two raisers with no survivorship gradient.**

---

## 10. Cell-line background reduces to the locus

**PRE-SPECIFIED, with honest multiplicity over all 5,075 line tests** (7 outcomes × {679 baseline TF
activities, 37 drivers, 6 lineage, 2 locus, 1 TP53 group}; 10,000 label permutations per feature, shuffle
unit = cell line). Only **3 tests reach q < 0.05 and 5 reach q < 0.1**:

| Test | ρ | 95% CI | q_BH over 5,075 | Organ-adjusted |
|---|---|---|---|---|
| **PYCARD-AS1 untreated level vs untreated MG53** | **+0.820** | 0.690–0.899 | **9.0e-5** | +0.811 |
| NFKBIB baseline activity vs idarubicin induction | +0.619 | — | 0.0356 | +0.545 |
| PYCARD-AS1 vs idarubicin induction | −0.625 | — | 0.0356 | −0.616 |
| TP73 baseline activity vs idarubicin induction | +0.593 | — | 0.0670 | +0.560 |
| [[FUS]] untreated level vs untreated MG53 | +0.570 | — | 0.0789 | +0.570 |

MDE80 |ρ| runs 0.412–0.661 across the family (43–49 lines), so ≈ 0.63 is the practical threshold after BH.
The two trait hits for idarubicin inducibility are CollecTRI **regulon activities** — list-defined, not
gene-level measurements.

**Variance of a line's untreated MG53** (range −2.49 to +2.10 log2, SD 1.28, 48–49 lines):

| Predictor | R² alone | R² added over PYCARD-AS1 |
|---|---|---|
| **PYCARD-AS1** | **0.679** (adjusted 0.672, β 1.171 ± 0.119) | — |
| FUS | 0.313 | **+0.007** (β 0.445 ± 0.457, p 0.336) |
| KMT2D alteration | 0.277 | +0.017 |
| Number of altered drivers | 0.131 | — |
| Organ (12 dummies) | 0.186 unadjusted, **adjusted −0.085** | — |
| TP53 group | 0.005 | — |

**KMT2D confirms exactly as committed, and is a locus effect, not a chromatin-regulator effect.**
KMT2D-altered lines (15) carry **+1.481 log2 (2.79×)** more untreated MG53 (SE 0.349, CI 0.797–2.165,
R² 0.277, 49 lines; 5,000-draw line-label permutation p 2e-4, MDE80 1.118 log2 = 2.17×). On the 48 lines
with PYCARD-AS1 the coefficient falls from +1.527 to **+0.390** (SE 0.275, CI −0.149 to +0.930) with
PYCARD-AS1 in the model (β +1.063 ± 0.139), permutation **p 0.102 with MDE80 0.665–0.669 log2** — a
**bounded null below its own MDE**. KMT2D-altered lines also carry +1.068 log2 more PYCARD-AS1 (p 1.1e-4)
and +0.170 more FUS (p 0.039), and 13.9 against 5.8 altered drivers; the driver count explains none of the
KMT2D effect (1.481 → 1.496).

> [!warning] The confound that cannot be removed: 16p11.2 copy number
> Tahoe has no copy-number data. A line carrying extra copies of 16p11.2 would raise TRIM72, FUS and
> PYCARD-AS1 together and produce **exactly** the observed pattern (ρ 0.820, 0.570, R² 0.679). Segmental
> amplification and [[Readthrough spillover]] are **indistinguishable here**, which also makes the KMT2D
> association unresolvable. Obtaining segment-level CN over chr16:31.18–31.43 Mb from DepMap/CCLE is the
> highest-value item in the project that requires data from outside this run.

---

## 11. Program P24, MG53's closest program partner

**PRE-SPECIFIED.** P24 is MG53's closest program partner by a clear margin: r **0.768** across 1,086
drug-doses (drug-block null SD 0.0387, z 19.84, p 1.24e-87, q 6.21e-86), **0.208 clear** of the runner-up
P29 (0.559), with 46 of the 50 atlas programs reaching q < 0.05 — so **the margin is the information**.
Within lines it gives **+0.0297 log2 per doubling (+2.08%)**, p_common_twoway 1.34e-10, q 6.68e-9, with no
TP53-group difference (p_diff_twoway 0.650, label-permutation 0.713)
[`genome_wide/tables/d_program_vs_exposure.csv`].

It is neither a clean pathway nor a pure readthrough class. 102 genes, **20.6% readthrough-exposed against
4.2% of atlas genes (OR 6.0, p 1.3e-9) and 1.7% of other program members (OR 14.7, p 7.6e-16)**; 43.1% with
a neighbour ≤ 20 kb; median 8.80 CPM; median member r 0.409, above all 2,000 level-range-matched random gene
sets. But its **58 members with no 3′ neighbour within 20 kb still reach median r 0.374**, it spans 77
cytobands over 88 annotated members, it carries **no gene-set annotation at all** (0 of 102) and only 4 TFs.
Its drug profile is the readthrough profile: idarubicin 5 µM 4.02× (z 69.4), homoharringtonine 5 µM 2.28×,
doxorubicin 2.27×, epirubicin 2.08×, auranofin 1.94×, mitoxantrone 1.58×, panobinostat 1.54× up; belumosudil
0.87×, radotinib 0.90×, pralsetinib 0.81×, NG25 0.74× down — **it rises under MG53's raisers and falls under
MG53's lowerers.**

The gap between r 0.77 across drug-doses and +2.1% per doubling within a drug-dose is partly a shared drug
driver and partly attenuation by MG53's measurement error; with replicate-well reliability 0.114 the
within-line slope is a **floor** (naive disattenuation would give ≈ 0.26 log2 per doubling, so the true value
lies somewhere in 0.030–0.26), and the two components **cannot be separated with these data**
([[Reliability and disattenuation]]).

---

## 12. Evidence grades, all candidates on one page

| Kind | Candidate | Best effect size | Null / interval | Grade |
|---|---|---|---|---|
| **Genomic neighbourhood / readthrough spillover** | PYCARD-AS1 level (10.6 kb 5′, same strand) | **R² 0.679** of a line's untreated MG53; ρ 0.820 [0.690, 0.899] | 10,000 line permutations, q 9.0e-5 over 5,075 tests | **Strong** — the only class with replicated, variance-accounting evidence |
| | Sense readthrough index across drug-doses | R² 0.246 (named estimand); +0.307 incremental over technical + plate | drug-block permutation, z 9.3–15, MDE80 \|r\| 0.095 | **Moderate** — large, but partly a coherence statistic and Pearson-fragile |
| | [[FUS]] level | ρ 0.570, but **+0.007** R² over PYCARD-AS1 (p 0.336) | MDE for an R² increment ≈ 0.06 | **Weak** (bounded null given the locus) |
| | Each partner's own 5′ neighbourhood (within-line screen) | 61% of top-100 partners readthrough-exposed, OR 38.8 | Fisher p 2.05e-58 | **Strong** for the partner set, not for MG53 specifically |
| **Generic drug-induced stress** | Top 10 PCs of the drug-dose gene matrix | **62.8%** of MG53's across-drug-dose variance (top 20: 83.4%) | exact orthogonal decomposition | **Strong but not MG53-directed** |
| | Overall response amplitude | +1.683 SD on the arm-contrast test, above MG53's +0.998 | per-readout line shuffle, K = 2,000 | **Moderate** — the surviving generic comparator |
| **Transcriptional regulation** | Any CollecTRI regulon, within lines | all \|r\| ≤ 0.080 against a 0.080 noise ceiling | MDE80 0.026–0.027 partial-r | **Bounded null** |
| | FOSB mRNA | r 0.582 (rank 63 of 16,642); 0.498 at minus-10PC (rank 43) | drug-block permutation q 9.7e-66; 99.3rd percentile of level-matched | **Open — the one unexcluded candidate** |
| | p53 pathway | regulon r 0.121 → 0.198 at minus-10PC (rank 115 of 679); target set 0.103 (MDE80 0.100) → −0.013 at minus-3PC; within lines −0.060 to −0.083; across lines ρ 0.003 (MDE80 0.412) | drug-block; 2,000 level-matched sets; two-way cluster; 2,000 line permutations | **Not supported as a positive regulator; mid-pack, not absent** (§7) |
| | MyoD family | 0.000–0.018 CPM | — | **Unmeasurable** |
| | MEF2A/C/D, MUSCLE_TF | set mean −0.046 (p 0.457, MDE80 0.197); own mRNAs negative | 2,000 level-matched sets | **Bounded null, wrong sign** |
| | MUSCLE_STRUCTURAL | +0.318 (q_BH 0.0073 over 44 sets); +0.229 at minus-3PC (q 0.0031) | level-matched sets, 2,000 draws | **Open — the only gene set surviving family-wide BH** |
| **Cell-line background** | KMT2D alteration | +1.481 log2 (2.79×) alone → **+0.390** with PYCARD-AS1 (MDE80 0.665) | 5,000 label permutations, p 2e-4 → 0.102 | **Reduces to the locus** |
| | Organ / lineage | unadjusted R² 0.186, **adjusted −0.085**; H 9.19, p 0.708 | 2,000 permutations | **Null** |
| | [[TP53]] status | R² 0.005; +0.279 log2 (p 0.918) | 2,000 line permutations, MDE80 0.841 SD | **Bounded null** |
| | Driver count | R² 0.131 | — | **Weak, not separable from KMT2D** |
| **Measurement structure, not biology** | Plate batch | 3.124 log2 untreated gap, rank 1 of 16,656 | 5 matched empirical nulls, p 6.0e-5 to 0.0036, Holm 0.0007–0.025 | **Artefact, confounded with the biology by construction** |

---

## 13. What would settle it

Three items, in order of value per unit of effort:

1. **Correlate MG53's induction against the readthrough sense indices already on disk**
   (`export/upstream/TRIM72_per_drugdose.csv` — `DD_z`, `DoG_sense_index_z`, `DoG_antisense_index_z`,
   `rank_sense_index`). MG53's raisers are precisely the transcriptional and translational shutdown drugs,
   and shutdown is the canonical cause of readthrough — yet 7 of 21 raisers sit in the *bottom* tail of the
   genome-wide index. Pre-specify: Spearman over the 1,086 kept drug-doses, plus the rank of the 18
   `DD_z` ≥ 3 raisers on that index, with a drug-block permutation. **One script, minutes**, and the single
   most decision-relevant analysis absent from the current material.
2. **16p11.2 copy number for the 50 lines** (DepMap/CCLE), added as a covariate to the three line-level
   outcomes. Resolves the central ambiguity of the project: whether ρ 0.820 and the KMT2D association are
   readthrough or segmental amplification.
3. **Re-run the 19 single-well raisers on two plates each — one high-baseline, one low-baseline — and read
   the result as added CPM.** Two wells on a low-baseline plate detect 0.80–0.98 added CPM at 80% power,
   well inside the 1.0–7.1 added CPM these drug-doses report. Include 6–8 same-plate duplicate wells, the
   only contrasts that separate within-plate well noise from plate chemistry. 38–46 wells of new data.

A 3′-end, nascent or strand-and-position-resolved assay across FUS–PYCARD-AS1–TRIM72, on two or three MG53-
raising drugs, is the highest-value experiment for the project as a whole: readthrough puts the extra reads
in the TRIM72 introns and 5′ region continuous with PYCARD-AS1, promoter firing does not. Direct p53
manipulation settles §7. Neither is answerable from 3′-biased gene-level counts.

---

## Links

- **Concepts:** [[Readthrough spillover]], [[The TRIM72 locus]], [[MG53 (TRIM72)]], [[Tahoe-100M]],
  [[Why MG53 is hard to measure here]], [[The p53 pathway]], [[p53 program P]],
  [[Transcription factor activity inference]], [[Plate batch effects]], [[Reliability and disattenuation]],
  [[Placebo genes and reference families]], [[FDR calibration and the inflated null]],
  [[Cross-fitting and circularity]], [[Two-way fixed effects]]
- **Findings:** [[What this study found]], [[Downstream of MG53]], [[MDM2 and MG53]],
  [[Per-line p53 function]], [[p53 nullification in cancer cell lines]], [[Corrections and retractions]]
- **Methods:** [[The screen model]], [[Nulls and calibration]], [[Program P derivation]],
  [[The measurement with controls]], [[How the numbers are decided]]
- **Indexes:** [[Home]], [[Genes — Map of Content]], [[Tables — what the study produced]]

## Sources

1. **Authoritative, most recent:** the upstream analysis document *"Upstream of MG53: regulation,
   perturbations, and what this dataset can support"* — findings F1–F11, with `WORK/` subfolders
   `raisers/`, `p53_regulates/`, `genomewide/`, `variance/` and the independent `verify_*` recomputations.
   Every tag (PRE-SPECIFIED / EXPLORATORY / unverified) and every correction in §8 comes from it.
2. **Committed write-ups, older:** `mg53_p53/findings/FINDINGS.md`,
   `mg53_p53/findings/MG53_p53_TABLES.md` (Table B).
3. **Committed table:** `mg53_p53/findings/tables/tableB_upstream_mg53.csv` (38 rows: readthrough
   neighbours, drugs up and down, regulon activities, across-line levels, data-driven programs). Note the
   positional-wording caveat in §8.
4. **Run output referenced throughout:** `upstream_perturbations/tables/`, `upstream_coregulation/tables/`,
   `upstream_tf/tables/`, `genome_wide/tables/`, `two_way/tables/`, `export/upstream/`.
