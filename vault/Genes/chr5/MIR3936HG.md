---
symbol: "MIR3936HG"
type: "gene"
col: 13881
ensembl_id: "ENSG00000233006"
name: "MIR3936 host gene"
location: "5q31.1"
module: 13
arm: "+"
pooled_cpm: 25.98
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 17
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MIR3936HG

*MIR3936 host gene* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.47× (z +7.4, q 5e-11, up in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~78% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.70× (z +7.3, q 9e-11, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.487× (z -10.0, q 1e-20, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.303× (z -8.6, q 1e-15, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PM20D2]] (+0.57, fdr 3e-05), [[DMTN]] (+0.55, fdr 4e-05), [[ATP1A1-AS1]] (+0.54, fdr 1e-05); moves opposite to [[NAV1]] (-0.55, fdr 1e-05), [[TIMP1]] (-0.54, fdr 1e-05), [[FAM89B]] (-0.52, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[HSD11B2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.47×** | +7.4 | 5e-11 | 31/47 (H4, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +7.3 | 9e-11 | 35/47 (KATO III, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +6.3 | 6e-08 | 26/46 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.55×** | +6.0 | 2e-07 | 26/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.55×** | +6.0 | 2e-07 | 29/47 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.35×** | +5.5 | 4e-06 | 26/47 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 1e-05 | 26/46 (KATO III, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 3e-05 | 15/46 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 3e-05 | 21/47 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.9 | 6e-05 | 20/45 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +4.8 | 7e-05 | 21/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.44×** | +4.7 | 1e-04 | 22/46 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.7 | 1e-04 | 24/47 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.4 | 4e-04 | 23/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.41×** | +4.3 | 5e-04 | 19/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 8e-04 | 19/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 18/47 (HEC-1-A, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.001 | 19/47 (C-33 A, KATO III, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.487×** | -10.0 | 1e-20 | 35/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.510×** | -9.4 | 2e-18 | 35/45 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.303×** | -8.6 | 1e-15 | 32/43 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -8.1 | 1e-13 | 33/47 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.581×** | -7.5 | 5e-12 | 28/46 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.604×** | -7.0 | 2e-10 | 28/46 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.593×** | -7.0 | 2e-10 | 32/46 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -5.0 | 5e-05 | 23/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | **0.729×** | -4.2 | 0.001 | 21/44 (HS-578T, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.588×** | -3.9 | 0.007 | 13/36 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.835× | -3.6 | 0.018 | 21/45 (A549, CFPAC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -3.5 | 0.020 | 18/46 (RKO, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.767×** | -3.5 | 0.021 | 15/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.789×** | -3.3 | 0.037 | 23/45 (A549, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.794×** | -3.2 | 0.048 | 18/46 (NCI-H460, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.854× | -3.1 | 0.061 | 11/47 (MIA PaCa-2, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.808×** | -3.0 | 0.091 | 9/46 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.804×** | -2.9 | 0.100 | 12/47 (MIA PaCa-2, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 36.5 | 4 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.62× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.210× (z -11.3) ⚠ cell-cycle shift, explains ~72% of this change |
| [[LoVo (line)]] | wt | 79.1 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -14.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 41.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 26.4 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -10.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 29.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +8.7) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.173× (z -10.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[H4 (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0904× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.119× (z -8.7) |
| [[HS-578T (line)]] | alt | 12.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.0564× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~68% of this change |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +9.4) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -10.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.241× (z -11.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[Panc 03.27 (line)]] | alt | 41.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.296× (z -10.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[RKO (line)]] | wt | 16.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +9.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.175× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 37.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0537× (z -11.0) |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0853× (z -8.5) |
| [[C32 (line)]] | wt | 14.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 26.3 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0526× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 61.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.121× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 6.57 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -9.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1792 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +16.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PM20D2]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[DMTN]] | +0.55 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[ATP1A1-AS1]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[FAM149A]] | +0.53 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[CIART]] | +0.53 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SLC22A5]] | +0.52 | +0.51 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HSBP1L1]] | +0.51 | +0.56 / +0.27 | both halves | 3e-04 |  |
| [[IQCH-AS1]] | +0.51 | +0.58 / +0.31 | both halves | 2e-04 |  |
| [[HOTAIR]] | +0.51 | +0.37 / +0.33 | both halves | 1e-04 |  |
| [[STEAP2]] | +0.51 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[MTERF2]] | +0.51 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[RAVER2]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[TTC39A]] | +0.50 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAV1]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[TIMP1]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.52 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[TSHZ3]] | -0.52 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SLC25A51]] | -0.51 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[PDLIM7]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[WWTR1]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[LRWD1]] | -0.51 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[PHC2]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ARID3B]] | -0.50 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[RNF168]] | -0.50 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[MEA1]] | -0.49 | -0.49 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD11B2]] | B | HSD11B2 activity raises MIR3936HG's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 2.16× lower at baseline in the lines without HSD11B2 | 0.005 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[TESMIN]] | B | TESMIN activity raises MIR3936HG's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without TESMIN | 0.022 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[HAS2]] | B | HAS2 activity lowers MIR3936HG's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.68× higher at baseline in the lines without HAS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[ITGA11]] | B | ITGA11 activity weakens MIR3936HG's drug response | lines that do not express ITGA11 (33) vs lines expressing it (14) | the lines without ITGA11 respond 1.68× as strongly (z diff -1.31); strongest at Ouabain (Octahydrate) 0.5 µM: 0.52x vs 0.81x (z diff -2.9) | 0.033 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; target measured in part of the lines; artifact flags |
| [[SMPDL3B]] | B | SMPDL3B activity raises MIR3936HG's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without SMPDL3B | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[ITGA11]] | B | ITGA11 activity lowers MIR3936HG's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 1.69× higher at baseline in the lines without ITGA11 | 0.045 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[ICA1]] | B | ICA1 activity raises MIR3936HG's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without ICA1 | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MIR3936HG's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[AP1G2]] | B | AP1G2 activity raises MIR3936HG's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without AP1G2 | 0.070 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[HSD11B2]] | B | HSD11B2 activity strengthens MIR3936HG's drug response | lines that do not express HSD11B2 (15) vs lines expressing it (32) | the lines without HSD11B2 respond 0.72× as strongly (z diff +1.32); strongest at Ouabain (Octahydrate) 5 µM: 0.64x vs 0.42x (z diff +2.8) | 0.076 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC44A3]] | B | SLC44A3 activity raises MIR3936HG's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without SLC44A3 | 0.077 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[LINC01748]] | B | LINC01748 activity raises MIR3936HG's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 1.59× lower at baseline in the lines without LINC01748 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction -0.479). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, 30.9); signed map (39.8, -13.7). **Vector** length 84.3, 19.5% of its response variance represented; |z| ≥ 3 in 1,256 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +5.1 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +7.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.0 | +6.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +4.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -8.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | +0.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MIR3936 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q31.1 — chr5:132,311,285-132,370,170 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC553103, SLC22A5-AS1 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40538) · Entrez [553103](https://www.ncbi.nlm.nih.gov/gene/553103) · Ensembl [ENSG00000233006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233006)

## Data

Gene col 13881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13881); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13881]; `tensor/DDL_lfc|DDL_z.npy` [13881]; `embed/gene_vectors.npy` [13881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13881 or target_col == 13881). Every well: [[MIR3936HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR3936HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
