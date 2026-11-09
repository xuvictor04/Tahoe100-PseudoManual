---
symbol: "HSF1"
type: "gene"
col: 11629
ensembl_id: "ENSG00000185122"
name: "heat shock transcription factor 1"
location: "8q24.3"
module: 36
arm: "+"
pooled_cpm: 48.62
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# HSF1

*heat shock transcription factor 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.54× (z +10.6, q 2e-23, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.571× (z -19.4, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THOC5]] (+0.75, fdr 7e-06), [[STK25]] (+0.67, fdr 7e-06), [[HERC2P3]] (+0.67, fdr 1e-05); moves opposite to [[SGO1-AS1]] (-0.65, fdr 1e-05), [[ZC3H6]] (-0.63, fdr 1e-05), [[TRMT1L]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +10.6 | 2e-23 | 41/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +9.8 | 2e-20 | 4/49 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +9.3 | 2e-18 | 38/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +8.4 | 9e-15 | 34/48 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +7.3 | 3e-11 | 32/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +7.2 | 5e-11 | 33/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.9 | 3e-10 | 26/46 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.8 | 7e-10 | 27/42 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +5.4 | 4e-06 | 25/45 (SHP-77, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.5 | 3e-04 | 12/48 (NCI-H460, NCI-H2347, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 1e-03 | 16/48 (CFPAC-1, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.9 | 0.005 | 15/43 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +3.4 | 0.034 | 8/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.041 | 8/48 (SW480, SW 900, …) | two highest doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.054 | 4/48 (RKO, BT-474, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.069 | 7/47 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.571×** | -19.4 | 0e+00 | 41/47 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -10.3 | 1e-22 | 36/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.754×** | -9.8 | 2e-20 | 35/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -8.7 | 6e-16 | 31/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -7.6 | 4e-12 | 32/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.790×** | -5.6 | 3e-06 | 22/47 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.815×** | -5.0 | 4e-05 | 21/48 (A498, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.815×** | -4.8 | 1e-04 | 22/48 (A-427, RKO, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.828×** | -4.5 | 5e-04 | 16/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.838× | -4.3 | 8e-04 | 15/48 (HS-578T, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.882× | -4.3 | 0.001 | 8/48 (CHP-212, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.842× | -4.2 | 0.001 | 14/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.836× | -4.1 | 0.002 | 17/46 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.898× | -3.7 | 0.007 | 16/48 (AsPC-1, A-427, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.887× | -3.7 | 0.007 | 8/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.889× | -3.5 | 0.015 | 13/48 (HepG2/C3A, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.869× | -3.4 | 0.019 | 10/48 (A498, C-33 A, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.910× | -3.3 | 0.031 | 7/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.913× | -3.2 | 0.047 | 9/48 (CHP-212, NCI-H1573, …) | top dose only | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.874× | -3.1 | 0.051 | 9/48 (NCI-H661, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 73.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -15.4) |
| [[BT-474 (line)]] | alt | 75.2 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.8) |
| [[A-427 (line)]] | wt | 56.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -10.5) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 63.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -12.5) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.385× (z -9.9) |
| [[A549 (line)]] | wt | 60.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -12.1) |
| [[HOP62 (line)]] | alt | 55.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 51.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 65.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -10.9) |
| [[SHP-77 (line)]] | alt | 54.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.40× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 30.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.1) |
| [[A-172 (line)]] | wt | 36.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.8) |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0706× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 75.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.3) |
| [[HS-578T (line)]] | alt | 72.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -11.1) |
| [[J82 (line)]] | alt | 63.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 58.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.52× (z +10.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 60.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -8.6) |
| [[PANC-1 (line)]] | alt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -10.7) |
| [[RKO (line)]] | wt | 93.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -8.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SK-MEL-2 (line)]] | alt | 47.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -22.8) |
| [[SNU-1 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.7) |
| [[C32 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC5]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[STK25]] | +0.67 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[HERC2P3]] | +0.67 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.66 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[POMT2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ERI3]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[HERC2P2]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PEX26]] | +0.64 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[WDR5]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1-AS1]] | -0.65 | -0.77 / -0.54 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.63 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.61 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD26]] | -0.59 | -0.71 / -0.50 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.58 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[DZIP3]] | -0.57 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[ATP23]] | -0.57 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[REL]] | -0.56 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HHLA3]] | -0.55 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.55 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers HSF1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HSF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LHFPL6]] | B | LHFPL6 activity lowers HSF1's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.17× higher at baseline in the lines without LHFPL6 | 0.0998 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.9, -30.6); signed map (-16.0, -51.4). **Vector** length 105, 25.1% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.2 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +8.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.0 | -19.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | heat shock transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,291,591-144,314,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSTF1 |
| Gene groups (HGNC) | Heat shock transcription factor family |
| Reactome | 12 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); Attenuation phase; HSF1 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00613](https://www.uniprot.org/uniprotkb/Q00613) (Heat shock factor protein 1):

> Functions as a stress-inducible and DNA-binding transcription factor that plays a central role in the transcriptional activation of the heat shock response (HSR), leading to the expression of a large class of molecular chaperones, heat shock proteins (HSPs), that protect cells from cellular insult damage. In unstressed cells, is present in a HSP90-containing multichaperone complex that maintains it in a non-DNA-binding inactivated monomeric form. Upon exposure to heat and other stress stimuli, …

**Summary**, from NCBI Gene [3297](https://www.ncbi.nlm.nih.gov/gene/3297):

> The product of this gene is a transcription factor that is rapidly induced after temperature stress and binds heat shock promoter elements (HSE). This protein plays a role in the regulation of lifespan. Expression of this gene is repressed by phosphorylation, which promotes binding by heat shock protein 90. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:5224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5224) · Entrez [3297](https://www.ncbi.nlm.nih.gov/gene/3297) · UniProt [Q00613](https://www.uniprot.org/uniprotkb/Q00613) · Ensembl [ENSG00000185122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185122)

## Data

Gene col 11629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11629); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11629]; `tensor/DDL_lfc|DDL_z.npy` [11629]; `embed/gene_vectors.npy` [11629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11629 or target_col == 11629). Every well: [[HSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
