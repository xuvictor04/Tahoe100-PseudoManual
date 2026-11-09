---
symbol: "UBL3"
type: "gene"
col: 4318
ensembl_id: "ENSG00000122042"
name: "ubiquitin like 3"
location: "13q12.3"
module: 232
arm: "+"
pooled_cpm: 91.05
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/232"]
generated_by: "tahoemap"
---

# UBL3

*ubiquitin like 3* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.27× (z +17.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.768× (z -5.7, q 6e-06, down in 30 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.688× (z -4.2, q 0.003, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF103]] (+0.57, fdr 1e-05), [[RMND5A]] (+0.53, fdr 9e-05), [[GABARAPL1]] (+0.52, fdr 3e-05); moves opposite to [[NDC1]] (-0.57, fdr 3e-05), [[PRMT7]] (-0.54, fdr 3e-05), [[MTERF3]] (-0.52, fdr 3e-05).
> It is in [[Module 232]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NT5M]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SMARCA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.27×** | +17.7 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +17.3 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +12.5 | 2e-33 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +11.5 | 3e-28 | 40/49 (MIA PaCa-2, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +10.6 | 2e-24 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +9.7 | 2e-20 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.3 | 1e-14 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 2e-10 | 30/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +7.0 | 2e-10 | 31/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +5.1 | 2e-05 | 26/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +5.1 | 2e-05 | 25/48 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.8 | 8e-05 | 25/48 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 7e-04 | 22/48 (NCI-H1573, hTERT-HPNE, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.0 | 0.002 | 13/49 (SHP-77, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.9 | 0.003 | 24/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.093 | 10/48 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.768×** | -5.7 | 6e-06 | 30/48 (A-172, J82, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.787×** | -5.2 | 7e-05 | 24/48 (HT-29, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.810×** | -4.6 | 1e-03 | 27/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.688×** | -4.2 | 0.003 | 22/48 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.822×** | -4.1 | 0.005 | 24/48 (NCI-H23, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.698×** | -4.1 | 0.005 | 24/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.834× | -3.9 | 0.006 | 22/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.882× | -3.9 | 0.008 | 17/49 (NCI-H1792, HepG2/C3A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.715×** | -3.8 | 0.010 | 18/48 (J82, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.717×** | -3.8 | 0.010 | 20/48 (RKO, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.897× | -3.3 | 0.041 | 5/48 (SW 900, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.852× | -3.3 | 0.041 | 18/42 (Panc 03.27, SHP-77, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.043 | 18/48 (BT-474, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.749×** | -3.3 | 0.043 | 12/49 (KATO III, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.859× | -3.2 | 0.059 | 18/48 (A-172, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.8 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +21.4) | — |
| [[NCI-H1573 (line)]] | alt | 87.3 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.93× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.89× (z +12.2) | — |
| [[SW480 (line)]] | alt | 92.7 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +14.2) | — |
| [[COLO 205 (line)]] | alt | 344 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.36× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 53.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +19.9) | — |
| [[HepG2_C3A (line)]] | wt | 131 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[hTERT-HPNE (line)]] | wt | 118 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 122 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 36.2× (z +16.5) | — |
| [[RKO (line)]] | wt | 106 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 87.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +19.4) | — |
| [[AsPC-1 (line)]] | alt | 76.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 58.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 268 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 85.5 | 2 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.10× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 113 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A549 (line)]] | wt | 59.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 93.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 0.5 µM 0.232× (z -8.9) |
| [[C32 (line)]] | wt | 133 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.05× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 71.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.1) | — |
| [[KATO III (line)]] | alt | 164 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.417× (z -9.7) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H2030 (line)]] | alt | 51.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 49.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 163 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 67.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.7) | — |
| [[A-427 (line)]] | wt | 41.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.70× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +15.1) | — |
| [[H4 (line)]] | wt | 67.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 86.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 87.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.4) | — |
| [[LoVo (line)]] | wt | 84.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 87.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H2347 (line)]] | alt | 90.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 86.6 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0858× (z -8.7) |
| [[SW 900 (line)]] | alt | 127 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +8.5) | — |
| [[A-172 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF103]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[RMND5A]] | +0.53 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[GABARAPL1]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[C11orf58]] | +0.51 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[SATB1]] | +0.51 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[FAM120AOS]] | +0.50 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[CHMP1B]] | +0.50 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[CUTALP]] | +0.50 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[RNF103-CHMP3]] | +0.50 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[CPEB4]] | +0.50 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[JMJD1C]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[LITAF]] | +0.48 | +0.45 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDC1]] | -0.57 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PRMT7]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[MTERF3]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SNRNP40]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[GEMIN5]] | -0.50 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[NSUN2]] | -0.49 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[TRAIP]] | -0.49 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[HDHD5]] | -0.49 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[CABIN1]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[EIF3B]] | -0.48 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[NT5M]] | -0.48 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[PIGU]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity lowers UBL3's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.68× higher at baseline in the lines without NT5M | 0.056 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA2]] | C | UBL3's natural level strengthens SMARCA2's drug response | UBL3's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.69, reverse -0.15; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 232]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.4, -16.3); signed map (13.3, -2.1). **Vector** length 88.5, 22.7% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.8 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.5 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.4 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +1.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -4.0 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -3.6 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:29,764,371-29,850,617 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCG-1, DKFZP434K151, FLJ32018; previously PNSC1 |
| Matched by | ensembl_id |

UniProt [O95164](https://www.uniprot.org/uniprotkb/O95164) carries no function annotation.

**Summary**, from NCBI Gene [5412](https://www.ncbi.nlm.nih.gov/gene/5412):

> Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12504) · Entrez [5412](https://www.ncbi.nlm.nih.gov/gene/5412) · UniProt [O95164](https://www.uniprot.org/uniprotkb/O95164) · Ensembl [ENSG00000122042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122042)

## Data

Gene col 4318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4318); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4318]; `tensor/DDL_lfc|DDL_z.npy` [4318]; `embed/gene_vectors.npy` [4318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4318 or target_col == 4318). Every well: [[UBL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
