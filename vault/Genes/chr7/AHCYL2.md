---
symbol: "AHCYL2"
type: "gene"
col: 8165
ensembl_id: "ENSG00000158467"
name: "adenosylhomocysteinase like 2"
location: "7q32.1"
module: 18
arm: "+"
pooled_cpm: 120.8
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# AHCYL2

*adenosylhomocysteinase like 2* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +11.9, q 4e-30, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.565× (z -12.6, q 2e-33, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.365× (z -11.6, q 1e-28, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAQ]] (+0.61, fdr 1e-05), [[ERC1]] (+0.55, fdr 1e-05), [[KANK1]] (+0.54, fdr 4e-05); moves opposite to [[ZNF17]] (-0.55, fdr 2e-05), [[ZBED8]] (-0.54, fdr 4e-05), [[ILK]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CRACD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +11.9 | 4e-30 | 31/49 (HT-29, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +10.1 | 2e-21 | 39/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.58×** | +9.5 | 3e-19 | 42/48 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +8.2 | 4e-14 | 36/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +8.0 | 2e-13 | 33/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.42×** | +7.8 | 8e-13 | 36/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.4 | 9e-12 | 31/48 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +7.3 | 3e-11 | 31/48 (HS-578T, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +7.2 | 3e-11 | 36/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.75×** | +6.4 | 8e-09 | 32/45 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +6.3 | 2e-08 | 32/48 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 4e-07 | 29/48 (HOP62, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.27×** | +5.3 | 4e-06 | 28/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.26×** | +5.0 | 2e-05 | 26/48 (KATO III, COLO 205, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 34/49 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.005 | 20/49 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.7 | 0.006 | 17/47 (C32, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.007 | 22/49 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.018 | 16/48 (C-33 A, HOP62, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.038 | 12/50 (C32, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.565×** | -12.6 | 2e-33 | 40/49 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -11.6 | 1e-28 | 40/49 (HS-578T, SW 900, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -10.4 | 7e-23 | 33/44 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -10.0 | 2e-21 | 31/45 (KATO III, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -7.3 | 3e-11 | 34/48 (LOX-IMVI, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **0.723×** | -7.1 | 8e-11 | 31/48 (NCI-H661, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.740×** | -6.4 | 1e-08 | 27/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.695×** | -4.2 | 0.002 | 19/38 (BT-474, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.881× | -4.0 | 0.005 | 14/49 (C32, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | 0.843× | -3.8 | 0.010 | 21/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.848× | -3.6 | 0.015 | 21/48 (C32, A498, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.813×** | -3.3 | 0.052 | 19/48 (C-33 A, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | 0.769× | -3.0 | 0.11 | 16/46 (PANC-1, C32, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 90.7 | 6 (2 ⚠) | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.329× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -14.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 43.5 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 106 | 3 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -11.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 103 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.4) | [[TAK-901 (drug)]] 5 µM 0.137× (z -12.7) |
| [[SW1417 (line)]] | alt | 194 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -18.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 231 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0590× (z -36.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 79.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +11.3) | — |
| [[LoVo (line)]] | wt | 305 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[MIA PaCa-2 (line)]] | alt | 126 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 130 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.212× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 161 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -30.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 145 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 263 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -13.4) |
| [[SW480 (line)]] | alt | 100 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.496× (z -10.1) |
| [[A-427 (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.217× (z -10.3) |
| [[A498 (line)]] | wt | 87.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.32× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | [[Harringtonine (drug)]] 5 µM 0.226× (z -15.4) ⚠ cell-cycle shift, explains ~87% of this change |
| [[A549 (line)]] | wt | 88.9 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -10.7) ⚠ cell-cycle shift, explains ~87% of this change |
| [[KATO III (line)]] | alt | 158 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -16.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 260 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 94.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 89.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.178× (z -10.7) |
| [[SNU-423 (line)]] | alt | 100 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.261× (z -8.8) |
| [[SW 900 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.151× (z -11.0) |
| [[A-172 (line)]] | wt | 62.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.42× (z +9.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[BT-474 (line)]] | alt | 92.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.128× (z -10.2) ⚠ toxic |
| [[C32 (line)]] | wt | 475 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.367× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 76.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.291× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 55.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 246 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.442× (z -8.5) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -12.8) ⚠ transcription drop; cell-cycle shift, explains ~63% of this change |
| [[Panc 03.27 (line)]] | alt | 116 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 62.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.9) | — |
| [[SW 1088 (line)]] | alt | 92.7 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0852× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 134 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAQ]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ERC1]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[KANK1]] | +0.54 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[RAB5IF]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[FAM135A]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[FTX]] | +0.53 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[CMTM8]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PSMB5]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[PSMB4]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[HSPE1]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[CAMKMT]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PPM1L]] | +0.51 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF17]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZBED8]] | -0.54 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[ILK]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[BIRC2]] | -0.49 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TMEM30A-DT]] | -0.49 | -0.26 / -0.30 | both halves | 3e-04 |  |
| [[POLI]] | -0.46 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[ACTR1B]] | -0.46 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[AXL]] | -0.46 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SARDH]] | -0.46 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[RARA]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LINC00702]] | -0.45 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TADA3]] | -0.45 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACD]] | B | CRACD activity raises AHCYL2's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without CRACD | 0.052 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers AHCYL2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.281). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.9, -9.3); signed map (7.8, -1.7). **Vector** length 105, 31.0% of its response variance represented; |z| ≥ 3 in 1,397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +9.6 | +7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +9.4 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.9 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +4.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +5.1 | +6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +0.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.2 | -10.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.4 | -11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.7 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.2 | -12.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | adenosylhomocysteinase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:129,225,030-129,430,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0828, long-IRBIT, IRBIT2, ADOHCYASE3 |
| Reactome | 4 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HN2](https://www.uniprot.org/uniprotkb/Q96HN2) (S-adenosylhomocysteine hydrolase-like protein 2):

> Regulatory protein that interacts with and modulates the activity of membrane ion transporters, including the sodium-bicarbonate cotransporter SLC4A4, through phosphorylation-dependent binding. Functions as a homolog of AHCYL1 to regulate bicarbonate transport and intracellular pH homeostasis via direct interactions rather than enzymatic activity (By similarity). On the contrary of its homolog AHCYL1, does not regulate ITPR1 sensitivity to inositol 1,4,5-trisphosphate.

**Summary**, from NCBI Gene [23382](https://www.ncbi.nlm.nih.gov/gene/23382):

> The protein encoded by this gene acts as a homotetramer and may be involved in the conversion of S-adenosyl-L-homocysteine to L-homocysteine and adenosine. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:22204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22204) · Entrez [23382](https://www.ncbi.nlm.nih.gov/gene/23382) · UniProt [Q96HN2](https://www.uniprot.org/uniprotkb/Q96HN2) · Ensembl [ENSG00000158467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158467)

## Data

Gene col 8165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8165); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8165]; `tensor/DDL_lfc|DDL_z.npy` [8165]; `embed/gene_vectors.npy` [8165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8165 or target_col == 8165). Every well: [[AHCYL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHCYL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
