---
symbol: "TNNT1"
type: "gene"
col: 2541
ensembl_id: "ENSG00000105048"
name: "troponin T1, slow skeletal type"
location: "19q13.42"
module: 208
arm: "+"
pooled_cpm: 38.34
n_lines_expressing: 41
n_dd_up: 4
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# TNNT1

*troponin T1, slow skeletal type* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.72× (z +6.1, q 5e-07, up in 28 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 4.08×, HEC-1-A 3.49×, PANC-1 2.74×, NCI-H1573 4.15×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.17×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -19.3, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID3B]] (+0.72, fdr 7e-06), [[RTN2]] (+0.71, fdr 7e-06), [[GNAI2]] (+0.68, fdr 4e-05); moves opposite to [[SNX5]] (-0.65, fdr 1e-05), [[MBNL3]] (-0.59, fdr 1e-04), [[PHACTR2]] (-0.57, fdr 3e-04).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF404]] → it (grade B ⚠); 4 go from it, the strongest it → [[DNAAF9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2541.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 4.08×, HEC-1-A 3.49×, PANC-1 2.74×, NCI-H1573 4.15×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.17×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.1 | 5e-07 | 28/35 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +5.2 | 6e-05 | 20/28 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.42×** | +3.9 | 0.017 | 24/38 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +3.5 | 0.079 | 15/39 (HT-29, HCT15, …) | all doses, flat |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.20 | 16/39 (A498, PANC-1, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.69× | +3.1 | 0.20 | 11/39 (A-427, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.21 | 12/38 (RPMI-7951, NCI-H460, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.294×** | -19.3 | 0e+00 | 37/39 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.271×** | -14.6 | 1e-45 | 38/38 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.360×** | -11.0 | 1e-25 | 35/39 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.399×** | -10.3 | 2e-22 | 36/39 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -9.6 | 1e-19 | 32/38 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -9.4 | 7e-19 | 33/39 (SW 900, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.487×** | -8.0 | 9e-14 | 35/39 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.533×** | -7.0 | 2e-10 | 29/38 (H4, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.521×** | -7.0 | 2e-10 | 27/39 (A549, C32, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -6.4 | 1e-08 | 26/38 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.575×** | -6.2 | 4e-08 | 31/39 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.617×** | -5.4 | 3e-06 | 26/39 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.626×** | -5.2 | 8e-06 | 24/39 (A-172, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -5.0 | 3e-05 | 19/37 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.648×** | -4.8 | 5e-05 | 24/39 (A-172, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.651×** | -4.8 | 6e-05 | 22/39 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.667×** | -4.5 | 2e-04 | 28/39 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -3.7 | 0.006 | 17/39 (A-172, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.715×** | -3.5 | 0.011 | 22/38 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -3.5 | 0.013 | 20/39 (SW 900, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.725×** | -3.3 | 0.023 | 17/39 (LoVo, SW 1088, …) | inconsistent across doses |  |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.1 | 0.041 | 14/39 (NCI-H460, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 170 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -15.7) |
| [[HOP62 (line)]] | alt | 42.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -22.6) |
| [[HS-578T (line)]] | alt | 75.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0499× (z -27.6) |
| [[H4 (line)]] | wt | 112 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -16.6) |
| [[SW 900 (line)]] | alt | 33.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.3) |
| [[A549 (line)]] | wt | 65.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 35.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -20.9) |
| [[LoVo (line)]] | wt | 30.8 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -13.0) |
| [[A-427 (line)]] | wt | 82.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -20.5) |
| [[HEC-1-A (line)]] | alt | 51.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 27.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 57.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.4) |
| [[PANC-1 (line)]] | alt | 60.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 46.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.9) |
| [[C32 (line)]] | wt | 35.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.8) |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.6) |
| [[J82 (line)]] | alt | 54.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -20.5) |
| [[LOX-IMVI (line)]] | wt | 46.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0369× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 45.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 53.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.4) |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.7) |
| [[SW480 (line)]] | alt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -14.8) |
| [[A498 (line)]] | wt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.72× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0723× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -18.9) |
| [[SW 1088 (line)]] | alt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -8.8) |
| [[AN3 CA (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3B]] | +0.72 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[RTN2]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[GNAI2]] | +0.68 | +0.72 / +0.42 | both halves | 4e-05 |  |
| [[GIPR]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PDZD7]] | +0.65 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[RRAS]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SYP]] | +0.64 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[SLC27A1]] | +0.64 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[MAST1]] | +0.64 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[FAM89B]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.64 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[KLC3]] | +0.62 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX5]] | -0.65 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.59 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[PHACTR2]] | -0.57 | -0.65 / -0.29 | both halves | 3e-04 |  |
| [[FUBP1]] | -0.57 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[HNF4G]] | -0.56 | -0.48 / -0.26 | both halves | 3e-04 |  |
| [[CPSF2]] | -0.56 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[FIGN]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RNASEH2B]] | -0.54 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MCCC2]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SH2D4A]] | -0.53 | -0.48 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF404]] | B | ZNF404 activity raises TNNT1's level | lines that do not express ZNF404 (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without ZNF404 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1 |
| [[FBXO27]] | B | FBXO27 activity raises TNNT1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without FBXO27 | 0.092 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[PDZD4]] | B | PDZD4 activity raises TNNT1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.40× lower at baseline in the lines without PDZD4 | 0.098 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAAF9]] | B | TNNT1 activity raises DNAAF9's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without TNNT1 | 0.066 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |
| [[DNAAF3]] | B | TNNT1 activity raises DNAAF3's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without TNNT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |
| [[TNNI3]] | B | TNNT1 activity raises TNNI3's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without TNNT1 | 0.081 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |
| [[MBNL3]] | B | TNNT1 activity lowers MBNL3's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 2.70× higher at baseline in the lines without TNNT1 | 0.093 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.5, 0.3); signed map (-24.4, 23.6). **Vector** length 87.1, 26.0% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.9 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.6 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.1 | -5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -14.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | troponin T1, slow skeletal type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,132,698-55,149,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ANM, STNT, TNT, TNTS, FLJ98147, MGC104241, NEM5 |
| Gene groups (HGNC) | Troponin complex subunits |
| Hallmark sets | MYOGENESIS |
| Reactome | 2 pathways, smallest: Striated Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P13805](https://www.uniprot.org/uniprotkb/P13805) (Troponin T, slow skeletal muscle):

> Troponin T is the tropomyosin-binding subunit of troponin, the thin filament regulatory complex which confers calcium-sensitivity to striated muscle actomyosin ATPase activity.

**Summary**, from NCBI Gene [7138](https://www.ncbi.nlm.nih.gov/gene/7138):

> This gene encodes a protein that is a subunit of troponin, which is a regulatory complex located on the thin filament of the sarcomere. This complex regulates striated muscle contraction in response to fluctuations in intracellular calcium concentration. This complex is composed of three subunits: troponin C, which binds calcium, troponin T, which binds tropomyosin, and troponin I, which is an inhibitory subunit. This protein is the slow skeletal troponin T subunit. Mutations in this gene cause …

**Accessions** — [HGNC:11948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11948) · Entrez [7138](https://www.ncbi.nlm.nih.gov/gene/7138) · UniProt [P13805](https://www.uniprot.org/uniprotkb/P13805) · Ensembl [ENSG00000105048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105048)

## Data

Gene col 2541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2541); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2541]; `tensor/DDL_lfc|DDL_z.npy` [2541]; `embed/gene_vectors.npy` [2541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2541 or target_col == 2541). Every well: [[TNNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
