---
symbol: "ABAT"
type: "gene"
col: 11361
ensembl_id: "ENSG00000183044"
name: "4-aminobutyrate aminotransferase"
location: "16p13.2"
module: 2
arm: "+"
pooled_cpm: 22.57
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ABAT

*4-aminobutyrate aminotransferase* — 16p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.81× (z +31.3, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.603× (z -9.0, q 1e-16, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD4B]] (+0.63, fdr 3e-05), [[CYB5R1]] (+0.61, fdr 3e-05), [[MKNK1]] (+0.60, fdr 2e-05); moves opposite to [[KLHL11]] (-0.60, fdr 3e-05), [[THAP12]] (-0.59, fdr 3e-05), [[PANK1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SLC51A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.81×** | +31.3 | 0e+00 | 45/46 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.51×** | +30.4 | 0e+00 | 44/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.41×** | +26.4 | 0e+00 | 45/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +17.6 | 0e+00 | 30/45 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.53×** | +16.5 | 0e+00 | 29/45 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.31×** | +13.0 | 1e-36 | 37/46 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +11.2 | 2e-27 | 32/46 (J82, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.90×** | +10.8 | 2e-25 | 28/46 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +9.6 | 6e-20 | 24/46 (HOP62, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +8.1 | 4e-14 | 27/46 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +8.0 | 7e-14 | 27/45 (SW1417, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.33×** | +7.9 | 2e-13 | 21/35 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +6.8 | 4e-10 | 27/46 (J82, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 3e-08 | 23/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.56×** | +5.6 | 7e-07 | 20/46 (SW480, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 19/46 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.603×** | -9.0 | 1e-16 | 28/46 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -8.4 | 1e-14 | 22/42 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.630×** | -8.2 | 3e-14 | 25/46 (RPMI-7951, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.635×** | -8.1 | 8e-14 | 24/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -8.0 | 1e-13 | 28/46 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -7.5 | 9e-12 | 24/46 (COLO 205, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.675×** | -7.0 | 2e-10 | 23/45 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.714×** | -6.0 | 1e-07 | 22/46 (A549, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.713×** | -5.6 | 2e-06 | 19/44 (NCI-H2030, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.729×** | -5.4 | 4e-06 | 19/44 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -5.2 | 8e-06 | 15/45 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.814×** | -3.5 | 0.025 | 11/46 (SK-MEL-2, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.814×** | -3.4 | 0.029 | 14/34 (HepG2/C3A, LoVo, …) | inconsistent across doses | composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | **0.831×** | -3.3 | 0.038 | 6/45 (NCI-H2030, Hs 766T, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.039 | 11/45 (J82, HEC-1-A, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.042 | 12/44 (LoVo, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.835× | -3.1 | 0.063 | 9/46 (NCI-H460, AN3 CA, …) | top dose only | plate-row cell shift |
| [[Docetaxel (drug)]] 5 µM |  | 0.887× | -3.0 | 0.065 | 10/46 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.851× | -2.9 | 0.092 | 5/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.851× | -2.9 | 0.092 | 8/45 (H4, A549, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -2.9 | 0.092 | 8/46 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.6 | 9 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +18.5) | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 15.6 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +22.4) | — |
| [[HepG2_C3A (line)]] | wt | 303 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.456× (z -9.5) |
| [[LoVo (line)]] | wt | 17.7 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.74× (z +14.7) | [[Digitoxin (drug)]] 5 µM 0.119× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 26.2 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 9.50× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 24.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +19.0) | — |
| [[HT-29 (line)]] | alt | 14.1 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.42× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 23.6 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.15× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.63× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[PANC-1 (line)]] | alt | 6.81 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 19.1× (z +17.0) | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +12.9) | — |
| [[A-172 (line)]] | wt | 29.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +16.0) | — |
| [[A-427 (line)]] | wt | 14.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.29× (z +11.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 17.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.28× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.30× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -10.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 8.23 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 23.6× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 20.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.81× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 3 | — | [[Malotilate (drug)]] 0.5 µM 0.0900× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 24.4× (z +16.4) | — |
| [[COLO 205 (line)]] | alt | 31.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.49× (z +13.1) | — |
| [[HCT15 (line)]] | alt | 32.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 28.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.01× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 7.46 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 12.2× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +12.5) | — |
| [[RKO (line)]] | wt | 26.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.03× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.42× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 12.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.75× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 8.11 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.14× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.84 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.69× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 8.33 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 54.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 11.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.13× (z +9.0) | — |
| [[A549 (line)]] | wt | 17.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +17.7) | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[H4 (line)]] | wt | 22.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.31× (z +8.9) | — |
| [[C32 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD4B]] | +0.63 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CYB5R1]] | +0.61 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[MKNK1]] | +0.60 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[NEAT1]] | +0.59 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[CLIP2]] | +0.59 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[DNAJB1]] | +0.58 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[TPST1]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TVP23C-CDRT4]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[GIPR]] | +0.55 | +0.26 / +0.52 | both halves | 4e-04 |  |
| [[PSMD3]] | +0.55 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[SLC8B1]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[SORBS1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL11]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[THAP12]] | -0.59 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PANK1]] | -0.58 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RAB11FIP2]] | -0.57 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MBNL3]] | -0.56 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[PTPN18]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[DR1]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ANGEL2]] | -0.56 | -0.24 / -0.56 | both halves | 4e-04 |  |
| [[ACTL6A]] | -0.55 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PRIMPOL]] | -0.55 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[C5orf15]] | -0.54 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[UBTF]] | -0.54 | -0.21 / -0.52 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC51A]] | C | ABAT's natural level weakens SLC51A's drug response | ABAT's natural level across 41 lines (lineage-adjusted; a glimpse) | r -0.70, reverse +0.18; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.189). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.5, 11.0); signed map (-21.5, 22.9). **Vector** length 85.2, 18.2% of its response variance represented; |z| ≥ 3 in 1,284 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +16.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +17.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +11.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.4 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.1 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | 4-aminobutyrate aminotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:8,674,596-8,784,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GABAT, GABA-T |
| Gene groups (HGNC) | Transaminases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY, P53_PATHWAY |
| Reactome | 4 pathways, smallest: GABA synthesis, release, reuptake and degradation; Neurotransmitter release cycle; Transmission across Chemical Synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [P80404](https://www.uniprot.org/uniprotkb/P80404) (4-aminobutyrate aminotransferase, mitochondrial):

> Catalyzes the conversion of gamma-aminobutyrate and L-beta-aminoisobutyrate to succinate semialdehyde and methylmalonate semialdehyde, respectively. Can also convert delta-aminovalerate and beta-alanine (By similarity).

**Summary**, from NCBI Gene [18](https://www.ncbi.nlm.nih.gov/gene/18):

> 4-aminobutyrate aminotransferase (ABAT) is responsible for catabolism of gamma-aminobutyric acid (GABA), an important, mostly inhibitory neurotransmitter in the central nervous system, into succinic semialdehyde. The active enzyme is a homodimer of 50-kD subunits complexed to pyridoxal-5-phosphate. The protein sequence is over 95% similar to the pig protein. GABA is estimated to be present in nearly one-third of human synapses. ABAT in liver and brain is controlled by 2 codominant alleles with …

**Accessions** — [HGNC:23](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23) · Entrez [18](https://www.ncbi.nlm.nih.gov/gene/18) · UniProt [P80404](https://www.uniprot.org/uniprotkb/P80404) · Ensembl [ENSG00000183044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183044)

## Data

Gene col 11361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11361); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11361]; `tensor/DDL_lfc|DDL_z.npy` [11361]; `embed/gene_vectors.npy` [11361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11361 or target_col == 11361). Every well: [[ABAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
