---
symbol: "CCNT1"
type: "gene"
col: 4964
ensembl_id: "ENSG00000129315"
name: "cyclin T1"
location: "12q13.11-q13.12"
module: 7
arm: "+"
pooled_cpm: 66.74
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CCNT1

*cyclin T1* — 12q13.11-q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.09× (z +20.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.555× (z -13.3, q 1e-37, down in 33 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.787× (z -5.4, q 1e-05, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNIP1]] (+0.64, fdr 1e-05), [[PRPF4]] (+0.62, fdr 1e-05), [[ZKSCAN5]] (+0.61, fdr 1e-05); moves opposite to [[ENAH]] (-0.58, fdr 1e-05), [[KIF13A]] (-0.58, fdr 1e-05), [[LRRFIP2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.09×** | +20.0 | 0e+00 | 48/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.96×** | +16.9 | 0e+00 | 44/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +14.8 | 0e+00 | 38/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +14.1 | 6e-43 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +12.8 | 1e-35 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +12.7 | 4e-35 | 38/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +11.0 | 3e-26 | 40/48 (SW480, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +10.8 | 4e-25 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +9.3 | 6e-19 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +7.8 | 3e-13 | 27/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.5 | 4e-09 | 21/37 (LOX-IMVI, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.4 | 7e-09 | 31/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.31×** | +6.4 | 7e-09 | 27/48 (SW480, LS 180, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.29×** | +5.7 | 4e-07 | 23/47 (HT-29, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +4.7 | 1e-04 | 21/48 (NCI-H460, C32, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.008 | 17/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.044 | 10/49 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4964.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -13.3 | 1e-37 | 33/43 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.617×** | -11.4 | 2e-27 | 37/49 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.787×** | -5.4 | 1e-05 | 25/47 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.829×** | -5.2 | 3e-05 | 19/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.868× | -4.8 | 2e-04 | 15/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.825×** | -4.4 | 0.001 | 19/48 (NCI-H2030, A549, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.847× | -3.9 | 0.007 | 15/47 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.853× | -3.8 | 0.010 | 17/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.855× | -3.7 | 0.013 | 15/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.810×** | -3.5 | 0.020 | 14/48 (NCI-H23, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.884× | -3.5 | 0.020 | 11/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.863× | -3.5 | 0.020 | 16/49 (A498, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.899× | -3.5 | 0.020 | 12/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.859× | -3.5 | 0.021 | 18/47 (A549, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.878× | -3.4 | 0.021 | 13/50 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.858× | -3.4 | 0.021 | 13/48 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.866× | -3.4 | 0.021 | 17/48 (CHP-212, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.904× | -3.4 | 0.021 | 8/48 (A498, SHP-77, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.865× | -3.3 | 0.027 | 17/48 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.4 | 12 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 65.5 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -14.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 87.2 | 8 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +15.8) | — |
| [[SW480 (line)]] | alt | 87.7 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.555× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 85.5 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.44× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -17.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 49.0 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 46.2 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.69× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -13.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 58.0 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.74× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 63.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 67.3 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.03× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 126 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.09× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -13.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.8) | — |
| [[KATO III (line)]] | alt | 57.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.05× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.0613× (z -28.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 48.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.45× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.19× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 163 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 94.6 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0932× (z -14.1) |
| [[Hs 766T (line)]] | wt | 43.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 47.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.1) | — |
| [[J82 (line)]] | alt | 60.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 37.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 64.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.67× (z +12.2) | — |
| [[RKO (line)]] | wt | 79.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.14× (z +9.6) | — |
| [[SW48 (line)]] | wt | 64.8 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 4.07× (z +9.9) | [[Capmatinib (drug)]] 5 µM 0.0989× (z -9.0) |
| [[C-33 A (line)]] | alt | 68.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.57× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.6) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[COLO 205 (line)]] | alt | 55.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.8× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 59.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.204× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[HS-578T (line)]] | alt | 45.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 85.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 57.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -19.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 71.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNIP1]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PRPF4]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ZKSCAN5]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[YRDC]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ZNF384]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[TRIM39]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[DIABLO]] | +0.59 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZNF597]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MAP3K7]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[HCG18]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ISG20L2]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[GPANK1]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENAH]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[KIF13A]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[LRRFIP2]] | -0.57 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[MAP4]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TNPO1]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[KRAS]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 | pathway: ESR-mediated signaling |
| [[TRIM37]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[AFDN]] | -0.51 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[MAP4K5]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ARHGAP17]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[RNF130]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[NCKAP1]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-34.8, -6.4); signed map (-5.2, -11.4). **Vector** length 85.5, 22.0% of its response variance represented; |z| ≥ 3 in 1,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.9 | +7.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +20.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | +4.0 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +16.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin T1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11-q13.12 — chr12:48,688,458-48,716,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CCNT, CYCT1; previously HIVE1 |
| Gene groups (HGNC) | Cyclins; P-TEFb complex subunits |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 31 pathways, smallest: Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery; HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [O60563](https://www.uniprot.org/uniprotkb/O60563) (Cyclin-T1):

> Regulatory subunit of the cyclin-dependent kinase pair (CDK9/cyclin-T1) complex, also called positive transcription elongation factor B (P-TEFb), which facilitates the transition from abortive to productive elongation by phosphorylating the CTD (C-terminal domain) of the large subunit of RNA polymerase II (RNA Pol II). Required to activate the protein kinase activity of CDK9: acts by mediating formation of liquid-liquid phase separation (LLPS) that enhances binding of P-TEFb to the CTD of RNA …

**Summary**, from NCBI Gene [904](https://www.ncbi.nlm.nih.gov/gene/904):

> This gene encodes a member of the highly conserved cyclin C subfamily. The encoded protein tightly associates with cyclin-dependent kinase 9, and is a major subunit of positive transcription elongation factor b (p-TEFb). In humans, there are multiple forms of positive transcription elongation factor b, which may include one of several different cyclins along with cyclin-dependent kinase 9. The complex containing the encoded cyclin and cyclin-dependent kinase 9 acts as a cofactor of human …

**Accessions** — [HGNC:1599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1599) · Entrez [904](https://www.ncbi.nlm.nih.gov/gene/904) · UniProt [O60563](https://www.uniprot.org/uniprotkb/O60563) · Ensembl [ENSG00000129315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129315)

## Data

Gene col 4964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4964); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4964]; `tensor/DDL_lfc|DDL_z.npy` [4964]; `embed/gene_vectors.npy` [4964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4964 or target_col == 4964). Every well: [[CCNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
