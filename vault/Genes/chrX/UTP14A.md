---
symbol: "UTP14A"
type: "gene"
col: 8008
ensembl_id: "ENSG00000156697"
name: "UTP14A small subunit processome component"
location: "Xq26.1"
module: 1
arm: "+"
pooled_cpm: 43.96
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# UTP14A

*UTP14A small subunit processome component* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +22.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.832× (z -4.6, q 0.001, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGA]] (+0.81, fdr 7e-06), [[SDAD1]] (+0.80, fdr 7e-06), [[NIFK]] (+0.80, fdr 7e-06); moves opposite to [[LAPTM4A]] (-0.66, fdr 7e-06), [[TMEM59]] (-0.65, fdr 7e-06), [[GNAS]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +22.6 | 0e+00 | 47/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.71×** | +17.8 | 0e+00 | 46/48 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +16.1 | 0e+00 | 48/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.80×** | +12.5 | 1e-33 | 39/47 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.61×** | +12.0 | 4e-31 | 43/48 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +10.7 | 1e-24 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +10.0 | 1e-21 | 46/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +9.3 | 1e-18 | 36/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +8.0 | 9e-14 | 38/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.54×** | +7.7 | 9e-13 | 30/48 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +7.6 | 2e-12 | 32/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +7.4 | 8e-12 | 35/47 (SW480, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.13×** | +7.0 | 8e-11 | 34/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.06×** | +6.7 | 6e-10 | 38/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +6.6 | 2e-09 | 32/47 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.92×** | +6.1 | 4e-08 | 31/46 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +5.5 | 1e-06 | 25/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +4.8 | 3e-05 | 25/47 (MIA PaCa-2, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.67×** | +4.8 | 4e-05 | 23/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.832×** | -4.6 | 0.001 | 22/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.756×** | -4.6 | 0.001 | 22/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.798×** | -4.0 | 0.006 | 22/48 (A498, AN3 CA, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.812×** | -4.0 | 0.006 | 17/48 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.793×** | -4.0 | 0.006 | 17/47 (C-33 A, SW48, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.006 | 19/48 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.794×** | -4.0 | 0.006 | 19/47 (LoVo, C-33 A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.803×** | -3.9 | 0.006 | 21/47 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.798×** | -3.9 | 0.006 | 18/47 (A549, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.833× | -3.7 | 0.013 | 18/48 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.024 | 19/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Minodronic acid (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.11 | 8/48 (SK-MEL-2, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 50.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 3.66× (z +10.7) | [[Adagrasib (drug)]] 0.05 µM 0.657× (z -12.2) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 32.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 47.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 85.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 38.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 23.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 73.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.1) | — |
| [[SW480 (line)]] | alt | 90.1 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.59× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 33.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.96× (z +12.5) | — |
| [[KATO III (line)]] | alt | 45.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0654× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 38.6 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 76.9 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +11.1) | — |
| [[A549 (line)]] | wt | 47.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.3) | — |
| [[COLO 205 (line)]] | alt | 28.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 38.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.5) | — |
| [[J82 (line)]] | alt | 38.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 45.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +10.2) | — |
| [[RKO (line)]] | wt | 52.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 36.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.1) | — |
| [[A-172 (line)]] | wt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +10.8) | — |
| [[A-427 (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0848× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.8) | — |
| [[H4 (line)]] | wt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 34.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0921× (z -10.6) |
| [[HS-578T (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.5) | — |
| [[LoVo (line)]] | wt | 42.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.248× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGA]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[SDAD1]] | +0.80 | +0.82 / +0.80 | both halves | 7e-06 | STRING 834 |
| [[NIFK]] | +0.80 | +0.86 / +0.75 | both halves | 7e-06 | STRING 805 |
| [[MAK16]] | +0.80 | +0.83 / +0.78 | both halves | 7e-06 | STRING 823 |
| [[PAK1IP1]] | +0.79 | +0.81 / +0.77 | both halves | 7e-06 | STRING 535 |
| [[REXO4]] | +0.78 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[BYSL]] | +0.78 | +0.76 / +0.78 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 997 |
| [[MRTO4]] | +0.78 | +0.79 / +0.77 | both halves | 7e-06 | STRING 679 |
| [[LTV1]] | +0.77 | +0.77 / +0.78 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 827 |
| [[DDX31]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 | STRING 631 |
| [[BRIX1]] | +0.77 | +0.81 / +0.69 | both halves | 7e-06 | STRING 651 |
| [[SURF6]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 | STRING 699 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4A]] | -0.66 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.65 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[GNAS]] | -0.63 | -0.63 / -0.71 | both halves | 7e-06 |  |
| [[ITM2B]] | -0.62 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[MPC2]] | -0.61 | -0.57 / -0.58 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises UTP14A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[EFNB2]] | B | EFNB2 activity lowers UTP14A's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.51× higher at baseline in the lines without EFNB2 | 0.018 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[MICE]] | B | MICE activity lowers UTP14A's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without MICE | 0.025 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises UTP14A's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.5, -37.1); signed map (-0.2, -44.5). **Vector** length 101, 28.9% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.60 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +17.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +10.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +6.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.6 | +6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -3.2 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | UTP14A small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:129,906,121-129,929,761 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-16, Utp14; previously SDCCAG16 |
| Gene groups (HGNC) | SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVJ6](https://www.uniprot.org/uniprotkb/Q9BVJ6) (U3 small nucleolar RNA-associated protein 14 homolog A):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Ensures correct nucleolar localization of small ribosomal subunit …

**Summary**, from NCBI Gene [10813](https://www.ncbi.nlm.nih.gov/gene/10813):

> This gene encodes a member of the uridine triphosphate 14 family. As an essential component of a large ribonucleoprotein complex bound to the U3 small nucleolar RNA, the encoded protein is involved in ribosome biogenesis and 18S rRNA synthesis. An autosomal retrotransposed copy of this X-linked gene exists on chromosome 13. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:10665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10665) · Entrez [10813](https://www.ncbi.nlm.nih.gov/gene/10813) · UniProt [Q9BVJ6](https://www.uniprot.org/uniprotkb/Q9BVJ6) · Ensembl [ENSG00000156697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156697)

## Data

Gene col 8008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8008); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8008]; `tensor/DDL_lfc|DDL_z.npy` [8008]; `embed/gene_vectors.npy` [8008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8008 or target_col == 8008). Every well: [[UTP14A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP14A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
