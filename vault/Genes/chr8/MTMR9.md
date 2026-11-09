---
symbol: "MTMR9"
type: "gene"
col: 2478
ensembl_id: "ENSG00000104643"
name: "myotubularin related protein 9"
location: "8p23.1"
module: 129
arm: "+"
pooled_cpm: 39.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# MTMR9

*myotubularin related protein 9* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.38× (z +11.3, q 4e-27, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.476× (z -18.3, q 0e+00, down in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.713× (z -11.8, q 7e-30, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRI1]] (+0.59, fdr 3e-05), [[TUBB6]] (+0.59, fdr 1e-05), [[NSUN5]] (+0.59, fdr 4e-05); moves opposite to [[CSDE1]] (-0.56, fdr 5e-05), [[EPHX1]] (-0.56, fdr 1e-05), [[PCBP2]] (-0.55, fdr 3e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +11.3 | 4e-27 | 30/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +11.3 | 4e-27 | 41/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.8 | 1e-12 | 27/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +6.4 | 3e-08 | 24/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +5.0 | 6e-05 | 18/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +4.3 | 0.001 | 17/48 (NCI-H2347, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.003 | 13/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +3.9 | 0.007 | 12/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.009 | 18/48 (PANC-1, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.009 | 10/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | 1.17× | +3.8 | 0.009 | 16/47 (LoVo, LS 180, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.015 | 14/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.024 | 11/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.030 | 6/48 (H4, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.038 | 16/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.067 | 9/47 (A-172, NCI-H2347, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.13× | +2.9 | 0.094 | 14/45 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.476×** | -18.3 | 0e+00 | 37/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -15.0 | 0e+00 | 34/41 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -11.8 | 7e-30 | 31/48 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.609×** | -11.3 | 1e-27 | 29/45 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -5.9 | 5e-07 | 24/48 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~10% of this change | **0.801×** | -5.5 | 4e-06 | 23/46 (CHP-212, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -5.1 | 3e-05 | 24/47 (Panc 03.27, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.823×** | -4.8 | 1e-04 | 21/48 (SK-MEL-2, AN3 CA, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | 0.846× | -4.0 | 0.005 | 18/47 (BT-474, COLO 205, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.956× | -3.6 | 0.016 | 1/49 (HOP62) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.034 | 13/48 (COLO 205, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.908× | -3.4 | 0.034 | 9/48 (hTERT-HPNE, SW 1088, …) | top dose only |  |
| [[Alpelisib (drug)]] 0.05 µM |  | 0.869× | -3.3 | 0.044 | 6/48 (SHP-77, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 88.3 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0766× (z -16.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 59.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.9) |
| [[PANC-1 (line)]] | alt | 28.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -14.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 37.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -17.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 68.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 49.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -21.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 28.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 54.0 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.30× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -11.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 75.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -15.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 59.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.9) |
| [[CHP-212 (line)]] | wt | 49.3 | 0 | 2 (2 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0675× (z -12.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[J82 (line)]] | alt | 27.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -11.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 28.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -9.1) |
| [[RKO (line)]] | wt | 57.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.7) |
| [[SHP-77 (line)]] | alt | 91.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 60.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -11.7) |
| [[SW48 (line)]] | wt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.594× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[C-33 A (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -16.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0842× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[H4 (line)]] | wt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.207× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 37.9 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.272× (z -8.7) |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.5) |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -19.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0617× (z -8.9) |
| [[AN3 CA (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRI1]] | +0.59 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TUBB6]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[PGBD1]] | +0.59 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ZNF699]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ZNF81]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[USP4]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PUS3]] | +0.57 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[MTRES1]] | +0.57 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[FSD1L]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[EIF6]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[NT5C]] | +0.57 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[EPHX1]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PCBP2]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[BCO2]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[VAMP1]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CNOT1]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[PAPOLA]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ITM2B]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMEM123]] | -0.52 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[MAP7D2]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[GNAS]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RORA-AS1]] | -0.51 | -0.39 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MTMR9's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.9, -2.5); signed map (-12.0, -21.2). **Vector** length 91.7, 19.8% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | +6.7 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +4.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.0 | +1.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -18.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:11,284,816-11,328,146 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434K171, LIP-STYX; previously C8orf9, MTMR8 |
| Gene groups (HGNC) | Myotubularins |
| Reactome | 7 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of IP2, IP, and Ins in the cytosol; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QG7](https://www.uniprot.org/uniprotkb/Q96QG7) (Myotubularin-related protein 9):

> Acts as an adapter for myotubularin-related phosphatases. Increases lipid phosphatase MTMR6 catalytic activity, specifically towards phosphatidylinositol 3,5-bisphosphate and MTMR6 binding affinity for phosphorylated phosphatidylinositols. Positively regulates lipid phosphatase MTMR7 catalytic activity (By similarity). Increases MTMR8 catalytic activity towards phosphatidylinositol 3-phosphate. The formation of the MTMR6-MTMR9 complex, stabilizes both MTMR6 and MTMR9 protein levels. Stabilizes …

**Summary**, from NCBI Gene [66036](https://www.ncbi.nlm.nih.gov/gene/66036):

> This gene encodes a myotubularin-related protein that is atypical to most other members of the myotubularin-related protein family because it has no dual-specificity phosphatase domain. The encoded protein contains a double-helical motif similar to the SET interaction domain, which is thought to have a role in the control of cell proliferation. In mouse, a protein similar to the encoded protein binds with MTMR7, and together they dephosphorylate phosphatidylinositol 3-phosphate and inositol …

**Accessions** — [HGNC:14596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14596) · Entrez [66036](https://www.ncbi.nlm.nih.gov/gene/66036) · UniProt [Q96QG7](https://www.uniprot.org/uniprotkb/Q96QG7) · Ensembl [ENSG00000104643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104643)

## Data

Gene col 2478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2478); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2478]; `tensor/DDL_lfc|DDL_z.npy` [2478]; `embed/gene_vectors.npy` [2478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2478 or target_col == 2478). Every well: [[MTMR9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
