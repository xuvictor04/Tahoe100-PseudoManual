---
symbol: "SMYD3"
type: "gene"
col: 11675
ensembl_id: "ENSG00000185420"
name: "SET and MYND domain containing 3"
location: "1q44"
module: 23
arm: "-"
pooled_cpm: 548.38
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 33
n_dd_up_clean: 6
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SMYD3

*SET and MYND domain containing 3* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.32× (z +14.9, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.190× (z -41.4, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (59 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 42 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C20orf27]] (+0.72, fdr 1e-05), [[NAA10]] (+0.71, fdr 3e-05, ⚠ NAA10 in the vector space only through flagged drug-doses), [[STUB1]] (+0.69, fdr 2e-04), [[KIAA1328]] (+0.68, fdr 7e-05); moves opposite to [[PBLD]] (-0.70, fdr 2e-04), [[MR1]] (-0.68, fdr 3e-04), [[PPP1R12A-AS2]] (-0.66, fdr 0.003, ⚠ one half only (not replicated)), [[ATXN1L]] (-0.66, fdr 6e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +14.9 | 0e+00 | 47/47 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +13.1 | 5e-37 | 46/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +11.0 | 1e-25 | 45/47 (AsPC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +7.2 | 9e-11 | 37/47 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.7 | 1e-06 | 28/47 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +5.3 | 9e-06 | 41/48 (SK-MEL-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.190×** | -41.4 | 0e+00 | 47/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.332×** | -27.5 | 0e+00 | 48/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.244×** | -23.9 | 0e+00 | 46/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.319×** | -20.1 | 0e+00 | 46/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.323×** | -19.9 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.335×** | -19.2 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.328×** | -18.9 | 0e+00 | 46/46 (HT-29, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.504×** | -12.1 | 1e-31 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -11.6 | 2e-29 | 41/43 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.520×** | -11.5 | 9e-29 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.502×** | -11.2 | 2e-27 | 43/44 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.323×** | -10.4 | 1e-23 | 47/48 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.467×** | -10.3 | 5e-23 | 46/48 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.556×** | -9.9 | 1e-21 | 40/46 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -9.3 | 5e-19 | 40/47 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.542×** | -8.2 | 7e-15 | 47/47 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -7.5 | 2e-12 | 33/47 (SW480, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -7.3 | 8e-12 | 35/49 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -7.3 | 9e-12 | 35/47 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.9 | 1e-10 | 31/47 (SNU-1, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -6.8 | 3e-10 | 38/47 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 550 | 2 | 20 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -28.0) |
| [[SNU-1 (line)]] | wt | 788 | 1 | 21 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -29.7) |
| [[SW480 (line)]] | alt | 475 | 3 | 19 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +13.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -29.2) |
| [[HOP62 (line)]] | alt | 636 | 2 | 19 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -45.3) |
| [[LoVo (line)]] | wt | 489 | 3 | 18 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -39.7) |
| [[LOX-IMVI (line)]] | wt | 554 | 3 | 18 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -23.9) |
| [[RKO (line)]] | wt | 729 | 4 | 17 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -36.8) |
| [[BT-474 (line)]] | alt | 999 | 4 | 16 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -19.5) |
| [[A-172 (line)]] | wt | 540 | 4 | 15 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -40.5) |
| [[HT-29 (line)]] | alt | 360 | 5 | 14 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +16.4) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -31.7) |
| [[SW 900 (line)]] | alt | 611 | 4 | 15 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -37.1) |
| [[PANC-1 (line)]] | alt | 510 | 3 | 15 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -48.4) |
| [[hTERT-HPNE (line)]] | wt | 481 | 4 | 13 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.01× (z +19.1) | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -29.4) |
| [[J82 (line)]] | alt | 536 | 3 | 14 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -21.6) |
| [[SNU-423 (line)]] | alt | 727 | 1 | 16 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -32.8) |
| [[HCT15 (line)]] | alt | 742 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -36.5) |
| [[HEC-1-A (line)]] | alt | 817 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -30.6) |
| [[SW1417 (line)]] | alt | 392 | 3 | 13 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -33.3) |
| [[H4 (line)]] | wt | 459 | 3 | 12 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -33.2) |
| [[NCI-H1792 (line)]] | alt | 329 | 3 | 12 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -32.5) |
| [[NCI-H23 (line)]] | alt | 536 | 1 | 14 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.73× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -46.8) |
| [[NCI-H460 (line)]] | wt | 1,046 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.7) |
| [[C-33 A (line)]] | alt | 1,086 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -18.8) |
| [[C32 (line)]] | wt | 558 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -33.2) |
| [[HepG2_C3A (line)]] | wt | 368 | 4 | 10 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.66× (z +16.0) | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -30.5) |
| [[LS 180 (line)]] | wt | 736 | 2 | 12 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -18.6) |
| [[Panc 03.27 (line)]] | alt | 572 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -31.3) |
| [[Hs 766T (line)]] | wt | 511 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -31.7) |
| [[HS-578T (line)]] | alt | 613 | 1 | 11 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -23.8) |
| [[NCI-H2347 (line)]] | alt | 296 | 5 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.52× (z +17.2) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -20.1) |
| [[SW 1271 (line)]] | alt | 1,256 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -26.1) |
| [[SW48 (line)]] | wt | 731 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -29.9) |
| [[A-427 (line)]] | wt | 547 | 1 | 10 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.85× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -32.7) |
| [[CHP-212 (line)]] | wt | 684 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -27.0) |
| [[CFPAC-1 (line)]] | alt | 522 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -31.4) |
| [[RPMI-7951 (line)]] | alt | 435 | 2 | 8 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -22.8) |
| [[SHP-77 (line)]] | alt | 987 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -19.9) |
| [[SK-MEL-2 (line)]] | alt | 484 | 5 (1 ⚠) | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -14.1) |
| [[A549 (line)]] | wt | 485 | 3 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -36.2) |
| [[AN3 CA (line)]] | alt | 585 | 0 | 9 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0881× (z -23.9) |
| [[AsPC-1 (line)]] | alt | 169 | 4 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.54× (z +21.3) | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -17.4) |
| [[NCI-H2030 (line)]] | alt | 345 | 1 | 8 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -32.1) |
| [[A498 (line)]] | wt | 363 | 2 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -33.0) |
| [[COLO 205 (line)]] | alt | 333 | 2 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -22.1) |
| [[NCI-H1573 (line)]] | alt | 408 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -23.0) |
| [[SW 1088 (line)]] | alt | 549 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -18.0) |
| [[NCI-H661 (line)]] | alt | 602 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -12.1) |
| [[KATO III (line)]] | alt | 43.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 525 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 574 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C20orf27]] | +0.72 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NAA10]] ⚠ | +0.71 | +0.49 / +0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[STUB1]] | +0.69 | +0.31 / +0.39 | both halves | 2e-04 |  |
| [[KIAA1328]] | +0.68 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[ANTKMT]] | +0.66 | +0.37 / +0.41 | both halves | 9e-05 | same gene group |
| [[PAFAH1B3]] | +0.66 | +0.52 / +0.26 | both halves | 4e-04 |  |
| [[EDA]] | +0.65 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[GARNL3]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RALGAPA2]] | +0.63 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[LRBA]] | +0.63 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[NHP2]] | +0.62 | +0.49 / +0.26 | both halves | 4e-04 |  |
| [[SBF2]] | +0.62 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[WASF3]] | +0.62 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 40 of them with an alert (⚠; 40 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | -0.70 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[MR1]] | -0.68 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[PPP1R12A-AS2]] | -0.66 | -0.60 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[ATXN1L]] | -0.66 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[EFCAB5]] | -0.65 | -0.58 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[BTN2A1]] | -0.65 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[NEK8]] | -0.64 | -0.57 / -0.23 | both halves | 5e-04 |  |
| [[ATE1OSP]] | -0.64 | -0.57 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[AP4S1]] | -0.64 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[SEC24B-AS1]] | -0.63 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[CHD1-DT]] | -0.63 | -0.56 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[CFLAR]] | -0.63 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ZBED5]] | -0.63 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[DDX59]] | -0.63 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[USP34-DT]] | -0.62 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[C3orf38]] | -0.62 | -0.55 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMYD3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SMYD3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SMYD3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity raises SMYD3's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADARB1]] | C | ADARB1 activity raises SMYD3's level | lines that do not express ADARB1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without ADARB1 | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC16A1-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-0.8, 14.2); signed map (-31.5, 3.4). **Vector** length 111, 49.5% of its response variance represented; |z| ≥ 3 in 1,983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +11.2 | +14.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.7 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +10.7 | +11.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.3 | +7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | -1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.7 | -27.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.6 | -18.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -9.1 | -8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -6.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.7 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | SET and MYND domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:245,749,342-246,507,312 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KMT3E; previously ZNFN3A1, ZMYND1 |
| Gene groups (HGNC) | Zinc fingers MYND-type; SET domain containing; Non-histone lysine methyltransferases |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7B4](https://www.uniprot.org/uniprotkb/Q9H7B4) (Histone-lysine N-methyltransferase SMYD3):

> Histone methyltransferase. Specifically methylates 'Lys-4' of histone H3, inducing di- and tri-methylation, but not monomethylation. Also methylates 'Lys-5' of histone H4. Plays an important role in transcriptional activation as a member of an RNA polymerase complex. Binds DNA containing 5'-CCCTCC-3' or 5'-GAGGGG-3' sequences.

**Summary**, from NCBI Gene [64754](https://www.ncbi.nlm.nih.gov/gene/64754):

> This gene encodes a histone methyltransferase which functions in RNA polymerase II complexes by an interaction with a specific RNA helicase. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:15513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15513) · Entrez [64754](https://www.ncbi.nlm.nih.gov/gene/64754) · UniProt [Q9H7B4](https://www.uniprot.org/uniprotkb/Q9H7B4) · Ensembl [ENSG00000185420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185420)

## Data

Gene col 11675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11675); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11675]; `tensor/DDL_lfc|DDL_z.npy` [11675]; `embed/gene_vectors.npy` [11675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11675 or target_col == 11675). Every well: [[SMYD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMYD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
