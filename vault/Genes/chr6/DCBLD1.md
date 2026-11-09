---
symbol: "DCBLD1"
type: "gene"
col: 8951
ensembl_id: "ENSG00000164465"
name: "discoidin, CUB and LCCL domain containing 1"
location: "6q22.1"
module: 147
arm: "+"
pooled_cpm: 54.46
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# DCBLD1

*discoidin, CUB and LCCL domain containing 1* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.19× (z +4.8, q 8e-04, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 3.84×, A-172 2.00×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 4.65×, A498 3.50×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-172 3.29×, A498 2.98×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.724× (z -8.8, q 1e-15, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT18]] (+0.58, fdr 1e-05), [[MYL12A]] (+0.53, fdr 4e-05), [[PFN1]] (+0.53, fdr 3e-05); moves opposite to [[U2AF1L4]] (-0.50, fdr 6e-05), [[HMBOX1]] (-0.47, fdr 7e-04), [[IQCK]] (-0.46, fdr 4e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAMLD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 3.84×, A-172 2.00×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 4.65×, A498 3.50×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-172 3.29×, A498 2.98×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.8 | 8e-04 | 20/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.020 | 21/48 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -8.8 | 1e-15 | 30/48 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.650×** | -8.2 | 5e-14 | 29/45 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.660×** | -7.4 | 4e-11 | 24/40 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.701×** | -6.8 | 1e-09 | 31/48 (HOP62, PANC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -6.3 | 3e-08 | 23/36 (HCT15, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -6.1 | 1e-07 | 27/48 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -6.0 | 1e-07 | 8/49 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -4.7 | 1e-04 | 24/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.802×** | -4.1 | 0.003 | 19/46 (C-33 A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.695×** | -3.6 | 0.016 | 11/47 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.712×** | -3.4 | 0.035 | 13/34 (A-172, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.840× | -3.2 | 0.066 | 15/47 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.735×** | -3.1 | 0.089 | 19/44 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 5 µM |  | **0.806×** | -3.1 | 0.089 | 7/47 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.794×** | -3.0 | 0.089 | 8/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 153 | 0 | 17 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -17.3) |
| [[HOP62 (line)]] | alt | 180 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -20.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -19.3) |
| [[NCI-H1573 (line)]] | alt | 48.0 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.3) |
| [[A549 (line)]] | wt | 99.5 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 81.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -13.0) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.9) |
| [[A498 (line)]] | wt | 28.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +17.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.9) |
| [[A-172 (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.29× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 66.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 49.4 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 4.65× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -17.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -11.4) ⚠ toxic |
| [[C32 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -10.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 34.8 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0499× (z -10.4) |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0793× (z -10.5) |
| [[SNU-423 (line)]] | alt | 177 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -10.7) |
| [[SW48 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT18]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MYL12A]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[PFN1]] | +0.53 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[HMGA2]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[ACTN1]] | +0.52 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ASAP1]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[DOCK4]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[BCAP29]] | +0.51 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[FMNL2]] | +0.51 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[EIF5A2]] | +0.50 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PALM2AKAP2]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[CD59]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF1L4]] | -0.50 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[HMBOX1]] | -0.47 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[IQCK]] | -0.46 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[FNBP4]] | -0.45 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[WARS1]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RPAP3-DT]] | -0.44 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ZSCAN31]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SEM1]] | -0.44 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[ZNF771]] | -0.43 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[BNIP1]] | -0.43 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[TP53BP1]] | -0.43 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[LUC7L2]] | -0.43 | -0.31 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAMLD1]] | B | MAMLD1 activity raises DCBLD1's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without MAMLD1 | 0.084 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.8, 4.2); signed map (9.3, 41.7). **Vector** length 95.8, 21.3% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[vincristine (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | discoidin, CUB and LCCL domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:117,453,817-117,569,858 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46341, dJ94G16.1 |
| Matched by | ensembl_id |

UniProt [Q8N8Z6](https://www.uniprot.org/uniprotkb/Q8N8Z6) carries no function annotation.

**Summary**, from NCBI Gene [285761](https://www.ncbi.nlm.nih.gov/gene/285761):

> Predicted to enable signaling receptor activity. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21479) · Entrez [285761](https://www.ncbi.nlm.nih.gov/gene/285761) · UniProt [Q8N8Z6](https://www.uniprot.org/uniprotkb/Q8N8Z6) · Ensembl [ENSG00000164465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164465)

## Data

Gene col 8951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8951); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8951]; `tensor/DDL_lfc|DDL_z.npy` [8951]; `embed/gene_vectors.npy` [8951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8951 or target_col == 8951). Every well: [[DCBLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCBLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
