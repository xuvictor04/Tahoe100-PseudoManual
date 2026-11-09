---
symbol: "PAX8-AS1"
type: "gene"
col: 12106
ensembl_id: "ENSG00000189223"
name: "PAX8 antisense RNA 1"
location: "2q14.1"
module: 26
arm: "+"
pooled_cpm: 51.73
n_lines_expressing: 31
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PAX8-AS1

*PAX8 antisense RNA 1* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.49× (z +7.8, q 2e-12, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.365× (z -19.7, q 0e+00, down in 29 of 29 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.433× (z -8.6, q 8e-16, down in 23 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01033]] (+0.54, fdr 5e-05), [[PSD4]] (+0.54, fdr 3e-05, ⚠ same locus), [[SMUG1]] (+0.54, fdr 8e-05), [[LINC00520]] (+0.54, fdr 8e-05); moves opposite to [[ALDH7A1]] (-0.50, fdr 3e-04), [[STRA6LP]] (-0.49, fdr 7e-05), [[POGLUT2]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FBXW10B]] → it (grade B ⚠); 2 go from it, the strongest it → [[FBXW10B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +7.8 | 2e-12 | 21/29 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +6.2 | 1e-07 | 19/28 (NCI-H460, SW48, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 1e-06 | 20/28 (SW48, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.2 | 3e-05 | 10/29 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.8 | 2e-04 | 16/28 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.011 | 6/29 (NCI-H460, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.014 | 8/27 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.014 | 9/30 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.027 | 9/29 (NCI-H460, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.030 | 10/28 (NCI-H460, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.4 | 0.042 | 13/29 (SW48, SNU-423, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.069 | 1/30 (RPMI-7951) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.069 | 4/30 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.074 | 5/28 (NCI-H460, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.077 | 8/29 (NCI-H460, SW48, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.077 | 12/29 (NCI-H1792, Panc 03.27, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.0 | 0.077 | 5/29 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.077 | 7/28 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.365×** | -19.7 | 0e+00 | 29/29 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.431×** | -16.5 | 0e+00 | 28/29 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.456×** | -15.4 | 0e+00 | 27/29 (SW480, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.520×** | -12.8 | 3e-35 | 26/29 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.538×** | -11.7 | 2e-29 | 23/29 (SW480, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.596×** | -10.1 | 5e-22 | 25/28 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.704×** | -9.7 | 2e-20 | 21/29 (KATO III, SW480, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -8.6 | 8e-16 | 23/29 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -7.9 | 2e-13 | 22/30 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.675×** | -7.7 | 1e-12 | 16/28 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.684×** | -7.4 | 7e-12 | 18/29 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.713×** | -6.6 | 2e-09 | 13/29 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.740×** | -5.9 | 2e-07 | 17/28 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **0.758×** | -5.2 | 8e-06 | 20/28 (HCT15, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.761×** | -5.1 | 1e-05 | 15/28 (SW480, COLO 205, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.638×** | -4.6 | 1e-04 | 12/30 (COLO 205, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.830×** | -3.6 | 0.008 | 6/28 (SNU-1, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.740×** | -3.1 | 0.055 | 4/30 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 212 | 0 | 17 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -26.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.145× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 60.5 | 8 (2 ⚠) | 7 (7 ⚠) | [[Trametinib (drug)]] 5 µM 2.64× (z +10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Binimetinib (drug)]] 5 µM 2.59× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -22.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[COLO 205 (line)]] | alt | 227 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -21.9) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0859× (z -12.3) |
| [[LS 180 (line)]] | wt | 72.8 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -18.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.119× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 97.2 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 57.4 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -14.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[Panc 03.27 (line)]] | alt | 89.1 | 1 | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.43× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[CFPAC-1 (line)]] | alt | 71.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -19.3) ⚠ cell-cycle shift, explains ~58% of this change |
| [[KATO III (line)]] | alt | 71.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -27.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -25.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HT-29 (line)]] | alt | 100 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -22.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SNU-1 (line)]] | wt | 102 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0828× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 110 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.08× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.283× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 92.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.161× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~64% of this change |
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -14.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 57.6 | 3 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.51× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.06× (z +11.5) | — |
| [[A-172 (line)]] | wt | 19.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +12.3) ⚠ cell-cycle shift, explains ~58% of this change | [[Panobinostat (drug)]] 5 µM 0.197× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 23.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0550× (z -15.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 122 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.64× (z +9.9) ⚠ unreliable plate only | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -16.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +15.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[A-427 (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.30 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.38 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.74 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01033]] | +0.54 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[PSD4]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 | ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[SMUG1]] | +0.54 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[LINC00520]] | +0.54 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[LINC01564]] | +0.54 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[PELO-AS1]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 | same gene group |
| [[CCDC90B-AS1]] | +0.53 | +0.33 / +0.60 | both halves | 1e-04 | same gene group |
| [[MYO16-AS1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 | same gene group |
| [[SPATA6L]] | +0.52 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[MGAM]] | +0.52 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[FER1L6]] | +0.52 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[PITX1-AS1]] | +0.52 | +0.33 / +0.49 | both halves | 1e-04 | same gene group |
| [[ACTR3C]] | +0.52 | +0.40 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH7A1]] | -0.50 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[STRA6LP]] | -0.49 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[POGLUT2]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SUGT1P4-STRA6LP-CCDC180]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[FAM102B]] | -0.48 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[CEP57L1]] | -0.48 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[POT1]] | -0.48 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[SPATA6]] | -0.48 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[SUGT1P4-STRA6LP]] | -0.47 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[BTBD3]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[MDM1]] | -0.47 | -0.10 / -0.58 | ⚠ one half (not replicated) | 0.003 |  |
| [[MZT1]] | -0.47 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[MPHOSPH9]] | -0.47 | -0.40 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXW10B]] | B | FBXW10B activity raises PAX8-AS1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 2.61× lower at baseline in the lines without FBXW10B | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[LINC01917]] | B | LINC01917 activity raises PAX8-AS1's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without LINC01917 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PAX8-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[PAX8]] | C | PAX8 activity raises PAX8-AS1's level | lines that do not express PAX8 (34) vs lines expressing it (16) | 3.87× lower at baseline in the lines without PAX8 | 7e-04 | ⚠ within organs, on part of the lines; also absent: FGF19, RGPD2, BMP10; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXW10B]] | B | PAX8-AS1 activity raises FBXW10B's level | lines that do not express PAX8-AS1 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without PAX8-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC68, PAX8, PCSK5; maybe low, not absent |
| [[PAX8]] | C | PAX8-AS1 activity raises PAX8's level | lines that do not express PAX8-AS1 (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without PAX8-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: CCDC68, PAX8, PCSK5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (2.7, 50.0); signed map (51.3, 7.7). **Vector** length 86.1, 21.9% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.8 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +0.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.3 | -16.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.7 | -15.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.7 | -19.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.6 | -6.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | PAX8 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q14.1 — chr2:113,211,421-113,276,581 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49271) · Entrez [654433](https://www.ncbi.nlm.nih.gov/gene/654433) · Ensembl [ENSG00000189223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189223)

## Data

Gene col 12106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12106); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12106]; `tensor/DDL_lfc|DDL_z.npy` [12106]; `embed/gene_vectors.npy` [12106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12106 or target_col == 12106). Every well: [[PAX8-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX8-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
