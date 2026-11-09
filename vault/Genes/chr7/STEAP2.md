---
symbol: "STEAP2"
type: "gene"
col: 8052
ensembl_id: "ENSG00000157214"
name: "STEAP2 metalloreductase"
location: "7q21.13"
module: 8
arm: "+"
pooled_cpm: 22.92
n_lines_expressing: 39
n_dd_up: 25
n_dd_down: 28
n_dd_up_clean: 18
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# STEAP2

*STEAP2 metalloreductase* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.63× (z +11.6, q 3e-28, up in 28 of 36 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.49× (z +6.9, q 9e-10, up in 21 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.339× (z -25.8, q 0e+00, down in 34 of 36 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.368× (z -17.2, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPD52L1]] (+0.64, fdr 7e-06), [[RAVER2]] (+0.63, fdr 1e-05), [[STEAP1]] (+0.57, fdr 1e-05, ⚠ same locus), [[SLC18B1]] (+0.57, fdr 5e-05); moves opposite to [[CYTH2]] (-0.61, fdr 1e-05), [[ZNF324]] (-0.55, fdr 4e-05), [[MAPK8IP3]] (-0.51, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DENND2D]] → it (grade B ⚠); 6 go from it, the strongest it → [[TMEM38B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.63×** | +11.6 | 3e-28 | 28/36 (LoVo, RKO, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +10.8 | 2e-24 | 28/37 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.6 | 7e-12 | 15/25 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +6.9 | 9e-10 | 21/37 (AsPC-1, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.03×** | +6.4 | 2e-08 | 17/35 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.98×** | +6.1 | 9e-08 | 18/35 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.94×** | +6.0 | 2e-07 | 20/34 (AsPC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.9 | 3e-07 | 15/37 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 5e-07 | 15/36 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +5.2 | 1e-05 | 16/36 (Panc 03.27, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.8 | 7e-05 | 18/35 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.31×** | +4.7 | 1e-04 | 13/36 (COLO 205, RKO, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.32×** | +4.7 | 1e-04 | 12/36 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.7 | 1e-04 | 15/35 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.6 | 1e-04 | 12/32 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +4.5 | 3e-04 | 13/35 (A549, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.002 | 10/37 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.008 | 12/35 (AsPC-1, SW480, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.012 | 10/37 (AsPC-1, KATO III, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.023 | 9/36 (AsPC-1, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.339×** | -25.8 | 0e+00 | 34/36 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.368×** | -17.2 | 0e+00 | 34/37 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.382×** | -16.5 | 0e+00 | 31/34 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.384×** | -15.8 | 0e+00 | 28/37 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -15.2 | 0e+00 | 30/37 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -13.8 | 4e-41 | 32/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.498×** | -12.0 | 3e-31 | 31/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.507×** | -11.7 | 1e-29 | 27/37 (SW48, SW480, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.542×** | -10.5 | 3e-24 | 27/36 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.568×** | -9.7 | 1e-20 | 23/36 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.392×** | -8.4 | 2e-15 | 22/36 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -7.4 | 6e-12 | 21/37 (SW480, HT-29, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -6.9 | 2e-10 | 20/35 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -6.6 | 2e-09 | 19/36 (COLO 205, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.706×** | -6.0 | 8e-08 | 19/37 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.790×** | -5.6 | 6e-07 | 21/36 (COLO 205, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.543×** | -5.5 | 1e-06 | 15/34 (HT-29, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -5.0 | 2e-05 | 15/36 (SW480, COLO 205, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.582×** | -4.9 | 3e-05 | 12/34 (HT-29, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.715×** | -4.1 | 1e-03 | 13/37 (SW480, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 35.0 | 0 | 12 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.102× (z -22.2) |
| [[COLO 205 (line)]] | alt | 114 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -23.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -18.7) |
| [[SW480 (line)]] | alt | 43.2 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0900× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -22.8) |
| [[NCI-H1573 (line)]] | alt | 54.9 | 1 (1 ⚠) | 8 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.69× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -29.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -11.3) |
| [[HT-29 (line)]] | alt | 32.4 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -14.7) |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -23.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.282× (z -10.2) |
| [[RKO (line)]] | wt | 34.1 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0898× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.2) |
| [[SW1417 (line)]] | alt | 103 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -16.7) |
| [[SW48 (line)]] | wt | 73.4 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -16.7) |
| [[A549 (line)]] | wt | 22.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.47× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.262× (z -9.1) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -9.3) |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0402× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 51.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.314× (z -9.6) |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0655× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -12.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 23.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.61× (z +8.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 67.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -10.0) |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 9.64 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -13.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L1]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[RAVER2]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[STEAP1]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 | same gene group; STRING 979; ⚠ same locus (2.8 kb, same strand: neighbours can correlate without regulation) |
| [[SLC18B1]] | +0.57 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[HDDC2]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ENPP4]] | +0.56 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[RAB11FIP2]] | +0.55 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[STEAP2-AS1]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXB9]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ZFAND1]] | +0.53 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CISD2]] | +0.52 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[KCTD14]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[PAQR3]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH2]] | -0.61 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[ZNF324]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MAPK8IP3]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ZER1]] | -0.51 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[DNAAF9]] | -0.50 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[MOB2]] | -0.49 | -0.15 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[PLIN3]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[TOM1L2]] | -0.47 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[MYO9B]] | -0.47 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[MIDN]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[TUBB6]] | -0.46 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[RAB35]] | -0.46 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[OTUD5]] | -0.46 | -0.31 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND2D]] | B | DENND2D activity raises STEAP2's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without DENND2D | 0.052 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[SORL1]] | B | SORL1 activity raises STEAP2's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.59× lower at baseline in the lines without SORL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[RNF43]] | B | RNF43 activity raises STEAP2's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without RNF43 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[SAMD12]] | B | SAMD12 activity raises STEAP2's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without SAMD12 | 0.093 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[MAP2K1]] | B | MAP2K1 activity lowers STEAP2's level | compounds that target MAP2K1: 3 of 4 raise it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[STEAP2-AS1]] | C | STEAP2-AS1 activity raises STEAP2's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 5.99× lower at baseline in the lines without STEAP2-AS1 | 9e-05 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent; co-absent with the target |
| [[STEAP1]] | C | STEAP1 activity raises STEAP2's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 4.69× lower at baseline in the lines without STEAP1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM38B]] | B | STEAP2 activity lowers TMEM38B's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 1.37× higher at baseline in the lines without STEAP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT |
| [[TMEM64]] | B | STEAP2 activity lowers TMEM64's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 1.51× higher at baseline in the lines without STEAP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT |
| [[SORL1]] | B | STEAP2 activity raises SORL1's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 4.04× lower at baseline in the lines without STEAP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT |
| [[HDDC2]] | B | STEAP2 activity lowers HDDC2's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 1.18× higher at baseline in the lines without STEAP2 | 0.090 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT |
| [[STEAP1]] | C | STEAP2 activity raises STEAP1's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without STEAP2 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT; co-absent with the target |
| [[STEAP2-AS1]] | C | STEAP2 activity raises STEAP2-AS1's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 2.67× lower at baseline in the lines without STEAP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.452). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.9, 13.0); signed map (14.8, -45.4). **Vector** length 93.2, 21.8% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +7.8 | +11.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +10.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.9 | +5.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -11.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -15.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -13.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -6.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | STEAP2 metalloreductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.13 — chr7:90,167,590-90,238,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IPCA-1, STAMP1, STMP; previously PCANAP1 |
| Gene groups (HGNC) | STEAP family; Flavoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFT2](https://www.uniprot.org/uniprotkb/Q8NFT2) (Metalloreductase STEAP2):

> Integral membrane protein that functions as a NADPH-dependent ferric-chelate reductase, using NADPH from one side of the membrane to reduce a Fe(3+) chelate that is bound on the other side of the membrane (By similarity). Mediates sequential transmembrane electron transfer from NADPH to FAD and onto heme, and finally to the Fe(3+) chelate (By similarity). Can also reduce Cu(2+) to Cu(1+) (By similarity).

**Summary**, from NCBI Gene [261729](https://www.ncbi.nlm.nih.gov/gene/261729):

> This gene is a member of the STEAP family and encodes a multi-pass membrane protein that localizes to the Golgi complex, the plasma membrane, and the vesicular tubular structures in the cytosol. A highly similar protein in mouse has both ferrireductase and cupric reductase activity, and stimulates the cellular uptake of both iron and copper in vitro. Increased transcriptional expression of the human gene is associated with prostate cancer progression. Alternate transcriptional splice variants, …

**Accessions** — [HGNC:17885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17885) · Entrez [261729](https://www.ncbi.nlm.nih.gov/gene/261729) · UniProt [Q8NFT2](https://www.uniprot.org/uniprotkb/Q8NFT2) · Ensembl [ENSG00000157214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157214)

## Data

Gene col 8052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8052); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8052]; `tensor/DDL_lfc|DDL_z.npy` [8052]; `embed/gene_vectors.npy` [8052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8052 or target_col == 8052). Every well: [[STEAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
