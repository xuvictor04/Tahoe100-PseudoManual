---
symbol: "HYCC2"
type: "gene"
col: 7912
ensembl_id: "ENSG00000155744"
name: "hyccin PI4KA lipid kinase complex subunit 2"
location: "2q33.1"
module: 48
arm: "+"
pooled_cpm: 102.74
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 13
n_dd_up_clean: 21
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# HYCC2

*hyccin PI4KA lipid kinase complex subunit 2* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.93× (z +18.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.472× (z -12.9, q 2e-35, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Apalutamide (drug)]] 0.5 µM: 0.792× (z -4.0, q 0.008, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D12]] (+0.60, fdr 7e-06), [[ZNHIT1]] (+0.60, fdr 2e-05), [[MINDY2]] (+0.60, fdr 1e-05); moves opposite to [[ATXN7L2]] (-0.69, fdr 7e-06), [[SRSF6]] (-0.60, fdr 1e-05), [[SFPQ]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.93×** | +18.5 | 0e+00 | 47/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.84×** | +18.0 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +17.4 | 0e+00 | 42/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.38×** | +15.0 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.35×** | +14.8 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +14.7 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.29×** | +13.1 | 2e-37 | 48/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +10.8 | 1e-25 | 35/49 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +10.3 | 4e-23 | 40/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +9.6 | 3e-20 | 44/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +9.2 | 3e-18 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.75×** | +9.1 | 4e-18 | 44/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +8.7 | 1e-16 | 40/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +8.6 | 4e-16 | 42/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +8.2 | 9e-15 | 45/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +8.0 | 5e-14 | 36/48 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.472×** | -12.9 | 2e-35 | 39/49 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -12.3 | 3e-32 | 38/43 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.573×** | -8.9 | 1e-16 | 33/45 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.792×** | -4.0 | 0.008 | 24/48 (NCI-H460, SW48, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.803×** | -3.8 | 0.018 | 23/47 (J82, HS-578T, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.809×** | -3.6 | 0.026 | 24/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.6 | 0.028 | 10/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.816×** | -3.5 | 0.032 | 20/48 (SW 1088, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.820×** | -3.4 | 0.039 | 20/48 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.822×** | -3.4 | 0.042 | 23/48 (A498, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.048 | 15/48 (A498, NCI-H460, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.826×** | -3.3 | 0.048 | 20/48 (NCI-H1792, CHP-212, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.059 | 16/48 (A498, J82, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.065 | 13/48 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.840× | -3.0 | 0.100 | 11/49 (A498, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.8 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +19.3) | — |
| [[J82 (line)]] | alt | 115 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 83.3 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 63.7 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 74.6 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 67.9 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 79.6 | 7 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 129 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 54.7 | 8 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.66× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 122 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 75.6 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -18.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 149 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 67.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +18.2) | — |
| [[KATO III (line)]] | alt | 46.4 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 99.2 | 5 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.04× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -13.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 94.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +19.0) | — |
| [[A549 (line)]] | wt | 72.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +17.3) | — |
| [[COLO 205 (line)]] | alt | 60.7 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.16× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 70.2 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 47.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.3) | — |
| [[A-427 (line)]] | wt | 40.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -13.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 99.8 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.66× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 51.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.9) | — |
| [[SW48 (line)]] | wt | 48.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.98× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 205 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -16.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 339 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -16.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 40.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 100 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 113 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 145 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.09× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 111 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -11.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 76.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 124 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 82.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 177 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 93.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 98.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 106 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.60× (z +9.9) | [[Docetaxel (drug)]] 0.05 µM 0.362× (z -9.5) ⚠ transcription drop |
| [[C32 (line)]] | wt | 82.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -16.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 73.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D12]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ZNHIT1]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MINDY2]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PLAG1]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SMAP2]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.57 | +0.28 / +0.54 | both halves | 3e-04 |  |
| [[GMCL1]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[OST4]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[RELCH]] | +0.55 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[ACOT8]] | +0.55 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[FGFR1OP2]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CNOT8]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L2]] | -0.69 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[SRSF6]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TRMO]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.59 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[PUF60]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[FKTN]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[CLPB]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[EPC2]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[UTP20]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[COA7]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DUS3L]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.2, -20.9); signed map (-33.6, 11.8). **Vector** length 82.0, 26.7% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +18.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +6.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.6 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | -0.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | +17.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | hyccin PI4KA lipid kinase complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,973,718-201,071,671 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39518; previously FAM126B |
| Gene groups (HGNC) | PI4KA lipid kinase complex |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXS8](https://www.uniprot.org/uniprotkb/Q8IXS8) (Hyccin 2):

> Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane.

**Summary**, from NCBI Gene [285172](https://www.ncbi.nlm.nih.gov/gene/285172):

> Predicted to be involved in phosphatidylinositol phosphate biosynthetic process and protein localization to plasma membrane. Located in cell junction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28593) · Entrez [285172](https://www.ncbi.nlm.nih.gov/gene/285172) · UniProt [Q8IXS8](https://www.uniprot.org/uniprotkb/Q8IXS8) · Ensembl [ENSG00000155744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155744)

## Data

Gene col 7912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7912); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7912]; `tensor/DDL_lfc|DDL_z.npy` [7912]; `embed/gene_vectors.npy` [7912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7912 or target_col == 7912). Every well: [[HYCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
