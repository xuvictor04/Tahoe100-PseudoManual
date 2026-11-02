---
type: concept
tags: [concept, method, calibration, nulls, selection]
status: current
---

# Placebo genes and reference families

> [!summary] In one line
> A gene's correlation with MG53 means nothing until you say which genes it is being ranked against — and
> the study's own 4,642-gene downstream export is **97% selected for association with MG53**, so a
> percentile inside it is a rank within a discovery set, not evidence that the gene is unusual.

## Why a bare correlation is not a result

Across 1,086 reliable drug-doses, the **median** gene's raw correlation with MG53 is **+0.124**, with a
5th–95th range of **−0.388 to +0.492**, over all 16,642 tested genes. So "this gene correlates with MG53 at
+0.12" describes the typical gene. And the whole distribution moves with the covariate choice:

| Variant | SD of *r* | Genes at \|r\| ≥ 0.3 | Genes at q < 0.05 | Top-100 overlap with raw |
|---|---|---|---|---|
| raw | 0.272 | 5,881 | 14,021 | — |
| covariates | 0.171 | 1,405 | 11,100 | 59 |
| minus-1PC | 0.218 | 2,894 | 12,920 | 44 |
| minus-3PC | 0.168 | 1,178 | 11,025 | 44 |
| minus-10PC | 0.139 | **660** | 9,726 | **30** |

[`genomewide/s1_landscape_by_variant.csv`, `s1_variant_agreement.csv`, reproduced exactly.] Per-gene MDE80
is |r| 0.090–0.108, and ≈0.17 after BH over 16,642 genes. The reason the partner count collapses from 5,881
to 660 is that the top 10 principal axes of the drug-dose gene matrix carry **62.8%** of MG53's
across-drug-dose variance and the top 20 carry **83.4%** [`upstream_coregulation/tables/a_pc_variance.csv`]
— most of MG53's drug-to-drug movement is generic drug response, not MG53.

So two things are needed before a number is interpretable: the covariate variant, and the **reference
family** the gene is ranked against.

## The trap: the study's own downstream export is a discovery set

> [!danger] `export/downstream/genes.csv` is not a sample of genes
> It holds **4,642** rows. **4,500 of them are there because the genome-wide screen had already called them
> significant against MG53 at q < 0.1.** The remaining 142 are p53-program members selected using the TP53
> wild-type/altered labels. Nothing in it was chosen before the statistic was computed.
> [`MDM2_MG53.md`, "Is MDM2 unusual?"]

That is **96.9%** selected on the exposure under test, and it shows in the family's own shape: its median
Spearman against MG53 is **+0.253 on level and +0.053 on change** rather than 0, and only **36%** of its
genes are negative. A percentile inside it is a rank within a family shifted toward MG53 association by
construction.

[[MDM2]] makes the difference concrete. It is itself one of the 4,500 — its export record reads
*"Tahoe p53 program P; genome_wide screen: common slope q < 0.1"* — so it is being ranked against genes
chosen for the same reason it was:

| Family | Quantity | MDM2 | percentile | family median | family 5th–95th |
|---|---|---|---|---|---|
| **16,642 tested, unselected** | co-regulation *r*, raw | +0.005 | **36th** | +0.124 | −0.388 to +0.492 |
| **16,642 tested, unselected** | the same, 3 PCs removed | +0.034 | **60th** | −0.008 | −0.252 to +0.293 |
| 4,642 discovery set | CHANGE (corrected log2), Spearman | −0.080 | 26th | +0.053 | −0.286 to +0.388 |
| 4,642 discovery set | LEVEL (pooled CPM), Spearman | −0.614 | 9th | +0.253 | −0.681 to +0.823 |
| *16,642*, [[CDKN1A]] | *co-regulation r, raw* | *+0.418* | *89th* | | |
| *4,642*, CDKN1A | *CHANGE, Spearman* | *+0.290* | *88th* | | |

In the unselected family MDM2 sits in the middle twice over — 36th and 60th. In the discovery set it looks
like an outlier at the 9th percentile, and that figure carries the extra warning of
[[Plate batch effects]]: on the LEVEL statistic roughly one gene in eleven is at least that negative, in a
distribution dominated by plate structure. An earlier version of that section used the discovery set and
called it "all genes"; the correction moves MDM2 *closer* to the centre, and is logged in
[[Corrections and retractions]].

> [!warning] Two censuses of this export disagree slightly
> `MDM2_MG53.md` counts **4,500 of 4,642** entering on q < 0.1. §6.1 of the upstream analysis counts
> **4,144 of 4,586 screen genes** (90.4%). Both are recorded here because neither has been reconciled; the
> conclusion is identical either way — an overwhelming majority of the export is selected on MG53.

The underlying selection is itself a calibration problem rather than a finding: 4,500 of 16,642 genes
(27.0%) clear q_common < 0.1 at an observed λ_common of **4.4436**, against 1.0 for a calibrated
statistic — see [[FDR calibration and the inflated null]].

## What an unselected family looks like instead

Three kinds, in increasing strictness:

**1. Selected for nothing.** The 16,642 tested genes. This is the honest default and the one to reach for
first. Its cost: the run supplies only its Pearson *r* on z, so it cannot be split into level and change.

**2. Matched on expression level.** Necessary because almost everything about MG53 is level-dependent. The
families in use: **2,409** level-matched screen genes for the raiser-count test
[`raisers/t19_placebo_gene_calls.csv`]; **300** expression-matched genes for the partner landscape
[`upstream_coregulation/tables/a_null_summary.csv`]; and **100 expression-matched plus 100
response-matched** placebo exposures for the per-gene screen [`genome_wide/tables/c_placebos.csv`].

**3. Matched on geometry as well.** Readthrough exposure is strongly level-dependent — 12.1% of genes at
2–5 CPM are exposed against 0.073% above 50 CPM — so a level-matched family still confounds level with
geometry. The strict families are the **419** level-matched genes with `dog_class = unexposed`
(structurally incapable of [[Readthrough spillover]]) and the **39** matched genes that are *themselves*
readthrough-exposed.

### The family choice changes the verdict, twice

**MG53's raiser list.** Running the identical calling rule on the 2,409 level-matched genes gives a median
of **17** raisers per gene (mean 18.2, p90 32, max 70). MG53's 21 sits at the **66.7th percentile**, and its
best single effect (`DD_z` 15.89) at the 56.5th percentile of those genes' maxima. Restricted to the 419
*unexposed* level-matched genes the median *rises* to **20** and MG53 falls to the **53.2nd percentile**
[`verify_raisers_0`, recomputed]. The length of the raiser list carries no information.

> [!note] This does not say the 21 raisers are false positives
> A no-signal null (per-well z ~ N(0, that plate's `mad_Z`), 2,000–5,000 draws, BH within each draw) yields
> **0.12–0.14 calls** (median 0, p95 1, P(≥21) ≤ 0.0005), so the calling procedure is **not
> miscalibrated**. The placebo family says something different and compatible: drugs change gene expression
> pervasively, and MG53 is unremarkable among genes of its level. Keep the two questions apart.

**MG53's readthrough enrichment.** Against the 300 expression-matched genes MG53 sits at the 96.7–99.0
percentile — empirical p **0.013–0.037**, BH over the five variants q 0.028–0.037, which survives. Against
the 39 matched genes that are themselves readthrough-exposed it sits at the 84.6–94.9 percentile —
empirical p **0.075–0.175, never below 0.05 in any variant**, on a design whose attainable floor is
1/40 = 0.025 [`a_null_summary.csv`, rows 0–1]. The honest statement is therefore: **MG53's readthrough
enrichment is specific relative to expression level and typical relative to readthrough geometry.** That
cuts both ways — good evidence that readthrough is the right account, and direct evidence that MG53 is not
special within it. The same source table reports the TRIM72–FUS baseline correlation at the 99.9th
percentile of genes at FUS's level **and at the 56.6th percentile among readthrough pairs**; the analysis
quoted the first half.

### What the placebo families say about inflation

| Statistic | MG53 | Expression-matched placebos | Response-matched placebos |
|---|---|---|---|
| λ_common (1.0 = calibrated) | 4.4436 | median **5.518** (2.437–8.994) | median **4.685** (3.385–6.192) |
| Genes at q_common < 0.1 | 4,500 | 2 to 8,381 (median 5,331) | 897 to 5,344 (median 3,196) |

[`genome_wide/tables/c_calibration.csv`.] MG53 sits **inside** the placebo range on both. The inflation
belongs to line-level structure, not to MG53 — matched placebos show the same or more. This is the single
most useful thing a reference family has done in this project.

The headline genotype contrast gets the same treatment and passes it: placebo-empirical p **0.653 and
0.733** over the 100 expression-matched and 100 response-matched placebo genes
[`genome_wide/tables/c_program_models.csv`, row 0]. *(Corrected: the earlier text said 10 and 10 — the
10-gene sets in `c_calibration.csv` are the λ-inflation panel, a different object.)*

## Five ways a reference family goes wrong, all of them present here

1. **Resolution below the claim.** A family of 10 has a floor of 1/11; its percentiles have resolution 0.1.
   A reported 0.0 or 1.0 from the per-gene screen's 10-placebo panels means "most extreme of ten", not a
   *p* value, and cannot support a claim on its own.
2. **Non-exchangeability.** In the 25-readout per-line placebo panel, ~14 of 25 non-p53 readouts are
   cell-cycle/E2F genes that p53 represses indirectly, so the panel's median is **−0.62 standardised SD**
   and its one-sided empirical *p* is not a calibrated test.
3. **Contamination by the thing under test.** The one placebo that beats MG53 on the per-line statistic
   (+0.450, the "generic stress/ISR module") is **two genes, ATF3 and DDIT3**; ATF3 is a
   [[p53 program P|program-P]] member the analysis's own tables class as `p53_target` (ρ_adj +0.4705), and
   DDIT3 alone scores +0.192. Excluding the contaminated module, **0 of 15–16 clean placebos exceed MG53**,
   so the one-sided placebo *p* is **0.0625** rather than 0.080
   [`verify_p53_regulates_1/v12_perline_placebo.csv`].
4. **Scale dependence.** Two quantities are both called "standardised" and the verdict flips with the
   choice: **3–8 of 25** placebos exceed MG53 per unit of exposure, **0–2** per SD of exposure. One unit of
   `program_P_delta_log2` is 13.4 SDs of that exposure, so the "+18.27 SD" figure is not an attainable
   effect.
5. **A point estimate of a random quantity.** MG53's 21 raisers is itself a noisy count from a design where
   90.5% of drug-doses have one well, and "66.7th percentile" is quoted with no interval on the 21.

A sixth problem is logistical and blocked a result outright: the project **owns** the right family for the
per-line statistic — 100 expression-matched and 100 response-matched genes in `c_placebos.csv` — but not at
the per-line grain, so **no calibrated placebo test of the per-line ρ +0.31 was possible**. That is the
honest statement, in place of quoting an uncalibrated one.

## Checklist for building one

1. **Chosen before the statistic**, or chosen for nothing at all.
2. **Matched on every nuisance the statistic is sensitive to** — here that is expression level *and*
   readthrough geometry, because the two are correlated.
3. **Large enough that 1/(n+1) beats the p value** you intend to claim.
4. **Exchangeable with the target**: no member selected for the behaviour under test, and no member that is
   part of the outcome (the ATF3 case).
5. **Reported with the family's own median and 5th–95th**, not only the target's percentile — a percentile
   without the family's shape hides whether the family is centred on zero.

## Links

- [[FDR calibration and the inflated null]] — λ_common, and why q is not a p here
- [[Cross-fitting and circularity]] — selection on the *outcome* side, the mirror of this note
- [[Nulls and calibration]], [[How the numbers are decided]]
- [[Readthrough spillover]] — the geometry a level-matched family still confounds
- [[Plate batch effects]] — why the LEVEL percentiles in the discovery set are plate structure
- [[MDM2 and MG53]], [[Upstream of MG53]], [[Corrections and retractions]]
- [[Tables — what the study produced]] — where each family's table lives
- [[MDM2]], [[CDKN1A]], [[TRIM72]]

## Sources

- `mg53_p53/findings/MDM2_MG53.md` — "Is MDM2 unusual? Two reference families, and the difference between
  them matters", and `tables/mdm2_mg53_allgene_null.csv` whose `family` column states that the 4,642-gene
  family is a discovery set.
- `/tmp/claude-0/-home-user-Tahoe100-PseudoManual/6ff0eb71-456e-5d8b-af99-308c7803f336/tasks/w2dbqis5h.output`
  — *Upstream of MG53*, finding F2 and §§4.3, 5.1, 5.2, 6.1, 6.3.
- `mg53_p53/findings/MG53_p53_TABLES.md` — "q_common must not be read as a p value".
- `raisers/t19_placebo_gene_calls.csv`; `genomewide/s1_landscape_by_variant.csv`;
  `upstream_coregulation/tables/a_null_summary.csv`, `a_pc_variance.csv`;
  `genome_wide/tables/c_calibration.csv`, `c_placebos.csv`, `c_program_models.csv`.
