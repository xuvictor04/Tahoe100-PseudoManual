---
symbol: "RNPC3"
type: "gene"
col: 11756
ensembl_id: "ENSG00000185946"
name: "RNA binding region (RNP1, RRM) containing 3"
location: "1p21.1"
module: 89
arm: "+"
pooled_cpm: 30.08
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# RNPC3

*RNA binding region (RNP1, RRM) containing 3* — 1p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.41× (z +10.4, q 2e-22, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.24× (z +6.5, q 1e-08, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.711× (z -7.0, q 2e-09, down in 21 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.628× (z -5.2, q 5e-05, down in 21 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS13B-DT]] (+0.70, fdr 7e-06), [[RWDD3]] (+0.68, fdr 7e-06), [[PNISR]] (+0.65, fdr 7e-06); moves opposite to [[EGR3]] (-0.58, fdr 3e-05), [[SLC9A3R1]] (-0.58, fdr 1e-04), [[MYLK2]] (-0.57, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAFIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +10.4 | 2e-22 | 37/48 (HS-578T, A498, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +10.0 | 5e-21 | 36/46 (SW1417, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.5 | 1e-08 | 22/47 (BT-474, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +6.5 | 2e-08 | 24/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.8 | 7e-07 | 24/48 (SW48, C32, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.7 | 1e-06 | 22/48 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +5.0 | 4e-05 | 17/48 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.26×** | +4.6 | 3e-04 | 17/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.4 | 7e-04 | 14/48 (A-172, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.23×** | +4.4 | 7e-04 | 16/48 (LoVo, SHP-77, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 14/47 (A549, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.7 | 0.008 | 9/48 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.008 | 7/48 (hTERT-HPNE, H4, …) | rises with dose | position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.008 | 14/49 (BT-474, J82, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.013 | 17/47 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.014 | 9/47 (NCI-H23, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.016 | 6/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.026 | 9/48 (HT-29, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.034 | 5/47 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.711×** | -7.0 | 2e-09 | 21/37 (SK-MEL-2, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -5.2 | 5e-05 | 21/49 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -5.1 | 5e-05 | 22/46 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -4.4 | 0.002 | 17/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.694×** | -4.1 | 0.005 | 15/48 (NCI-H460, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.827×** | -4.0 | 0.005 | 20/46 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.832×** | -3.9 | 0.008 | 17/48 (NCI-H1573, SK-MEL-2, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.882× | -3.8 | 0.011 | 4/49 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.894× | -3.4 | 0.046 | 18/47 (SNU-423, CFPAC-1, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.855× | -3.3 | 0.046 | 18/45 (NCI-H1573, SK-MEL-2, …) | rises with dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.742×** | -3.3 | 0.046 | 14/47 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.867× | -3.0 | 0.10 | 10/47 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.05 µM |  | 0.867× | -3.0 | 0.10 | 8/47 (HepG2/C3A, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 28.5 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.20× (z +9.5) ⚠ cell-cycle shift, explains ~30% of this change | [[PH-797804 (drug)]] 5 µM 0.0912× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 62.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.402× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~55% of this change |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 1 | — | [[CP21R7 (drug)]] 0.05 µM 0.0521× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 50.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.475× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13B-DT]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[RWDD3]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PNISR]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 | STRING 495 |
| [[ZNF493]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.63 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[TM2D1]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[YBEY]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[NAA38]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 | STRING 506 |
| [[ELMOD3]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 | same gene group |
| [[TAF11]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[FBXO9]] | +0.59 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[ZBTB8OS]] | +0.59 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR3]] | -0.58 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[SLC9A3R1]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[MYLK2]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SPATA32]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[EGR1]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[EGR2]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ACTN1]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[LRRC59]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[C13orf46]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PSMG1]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SHB]] | -0.53 | -0.58 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFIP]] | B | MAFIP activity raises RNPC3's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without MAFIP | 0.010 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.0, 21.3); signed map (-0.9, -2.6). **Vector** length 87.4, 17.4% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.7 | +10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +10.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +3.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding region (RNP1, RRM) containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.1 — chr1:103,525,691-103,555,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1839, FLJ20008, RBM40, SNRNP65 |
| Gene groups (HGNC) | RNA binding motif containing; U11/U12 di-snRNP |
| Reactome | 4 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LT9](https://www.uniprot.org/uniprotkb/Q96LT9) (RNA-binding region-containing protein 3):

> Participates in pre-mRNA U12-dependent splicing, performed by the minor spliceosome which removes U12-type introns. U12-type introns comprises less than 1% of all non-coding sequences. Binds to the 3'-stem-loop of m(7)G-capped U12 snRNA.

**Summary**, from NCBI Gene [55599](https://www.ncbi.nlm.nih.gov/gene/55599):

> Two types of spliceosomes catalyze splicing of pre-mRNAs. The major U2-type spliceosome is found in all eukaryotes and removes U2-type introns, which represent more than 99% of pre-mRNA introns. The minor U12-type spliceosome is found in some eukaryotes and removes U12-type introns, which are rare and have distinct splice consensus signals. The U12-type spliceosome consists of several small nuclear RNAs and associated proteins. This gene encodes a 65K protein that is a component of the U12-type …

**Accessions** — [HGNC:18666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18666) · Entrez [55599](https://www.ncbi.nlm.nih.gov/gene/55599) · UniProt [Q96LT9](https://www.uniprot.org/uniprotkb/Q96LT9) · Ensembl [ENSG00000185946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185946)

## Data

Gene col 11756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11756); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11756]; `tensor/DDL_lfc|DDL_z.npy` [11756]; `embed/gene_vectors.npy` [11756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11756 or target_col == 11756). Every well: [[RNPC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNPC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
