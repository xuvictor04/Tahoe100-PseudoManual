---
symbol: "ZBTB41"
type: "gene"
col: 10874
ensembl_id: "ENSG00000177888"
name: "zinc finger and BTB domain containing 41"
location: "1q31.3"
module: 41
arm: "+"
pooled_cpm: 84.25
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ZBTB41

*zinc finger and BTB domain containing 41* — 1q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.37× (z +6.9, q 1e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.588× (z -11.5, q 6e-28, down in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.484× (z -7.3, q 1e-10, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL2BP]] (+0.63, fdr 7e-06), [[USO1]] (+0.61, fdr 1e-05), [[EBLN3P]] (+0.60, fdr 1e-05); moves opposite to [[FOXK2]] (-0.52, fdr 1e-05), [[NDUFS6]] (-0.50, fdr 3e-05), [[NBL1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.9 | 1e-09 | 33/48 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.9 | 1e-09 | 32/48 (NCI-H1573, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.9 | 1e-09 | 31/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.23×** | +6.4 | 2e-08 | 26/48 (A-172, A-427, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.1 | 4e-05 | 23/49 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.027 | 20/48 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.027 | 11/48 (NCI-H1573, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.17× | +3.5 | 0.033 | 14/50 (SK-MEL-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.037 | 9/48 (SK-MEL-2, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.051 | 17/44 (SW48, SHP-77, …) | top dose only | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.11 | 10/49 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.15× | +3.0 | 0.12 | 13/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -11.5 | 6e-28 | 43/48 (SHP-77, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -7.3 | 1e-10 | 36/49 (A-172, SW 900, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -6.9 | 1e-09 | 33/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.737×** | -6.6 | 6e-09 | 32/48 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.657×** | -6.5 | 9e-09 | 39/48 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.748×** | -6.3 | 3e-08 | 33/48 (RPMI-7951, H4, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -5.8 | 6e-07 | 31/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.778×** | -5.4 | 4e-06 | 27/48 (Hs 766T, hTERT-HPNE, …) | two highest doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.644×** | -4.4 | 7e-04 | 25/48 (A-172, hTERT-HPNE, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.758×** | -4.3 | 0.001 | 27/48 (MIA PaCa-2, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.774×** | -4.0 | 0.004 | 23/48 (CHP-212, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.833×** | -3.9 | 0.004 | 21/48 (NCI-H2030, A-172, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.775×** | -3.9 | 0.004 | 22/49 (HCT15, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.835× | -3.9 | 0.004 | 20/48 (CHP-212, SHP-77, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.006 | 22/49 (HT-29, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.844× | -3.7 | 0.008 | 21/48 (KATO III, A549, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.795×** | -3.5 | 0.012 | 19/48 (SW 900, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.802×** | -3.4 | 0.019 | 17/48 (A498, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 87.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.307× (z -9.4) |
| [[Hs 766T (line)]] | wt | 113 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -11.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 79.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +11.0) | — |
| [[A-172 (line)]] | wt | 129 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 79.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 196 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~5% of this change |
| [[MIA PaCa-2 (line)]] | alt | 104 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.401× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~5% of this change |
| [[NCI-H1792 (line)]] | alt | 83.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.411× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 72.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.401× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 66.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.210× (z -15.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.373× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.401× (z -10.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0852× (z -11.6) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 76.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.363× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.510× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[NCI-H661 (line)]] | alt | 73.0 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.138× (z -9.0) |
| [[RKO (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 64.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.382× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 73.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.398× (z -10.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 61.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL2BP]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[USO1]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[EBLN3P]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[FAM220A]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[BROX]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[BLOC1S5]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ARCN1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TDP2]] | +0.58 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[RAB14]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[RIMOC1]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[DYNC1LI2]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[RAB33B]] | +0.56 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXK2]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NDUFS6]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[NBL1]] | -0.49 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TIMM23B]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[UCK2]] | -0.49 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CSNK1G2]] | -0.47 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[DUS1L]] | -0.47 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ZNF787]] | -0.45 | -0.45 / -0.45 | both halves | 3e-05 | same gene group |
| [[CELF1]] | -0.45 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[HDAC7]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ALYREF]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SAPCD1]] | -0.45 | -0.38 / -0.50 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.414). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.2, -16.4); signed map (-19.2, -13.5). **Vector** length 116, 31.8% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.3 | +6.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.5 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.4 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +2.1 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -6.7 | -6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -11.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.4 | -3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.2 | -3.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.8 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.3 — chr1:197,153,682-197,201,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FRBZ1, FLJ36199, DKFZp686C06120, ZNF924 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SVQ8](https://www.uniprot.org/uniprotkb/Q5SVQ8) (Zinc finger and BTB domain-containing protein 41):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [360023](https://www.ncbi.nlm.nih.gov/gene/360023):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24819) · Entrez [360023](https://www.ncbi.nlm.nih.gov/gene/360023) · UniProt [Q5SVQ8](https://www.uniprot.org/uniprotkb/Q5SVQ8) · Ensembl [ENSG00000177888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177888)

## Data

Gene col 10874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10874); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10874]; `tensor/DDL_lfc|DDL_z.npy` [10874]; `embed/gene_vectors.npy` [10874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10874 or target_col == 10874). Every well: [[ZBTB41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
