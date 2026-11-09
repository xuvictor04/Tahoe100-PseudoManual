---
symbol: "MAP2K3"
type: "gene"
col: 420
ensembl_id: "ENSG00000034152"
name: "mitogen-activated protein kinase kinase 3"
location: "17p11.2"
module: 141
arm: "+"
pooled_cpm: 56.4
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 24
n_dd_up_clean: 17
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# MAP2K3

*mitogen-activated protein kinase kinase 3* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.50× (z +35.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 0.5 µM: 0.650× (z -6.3, q 1e-07, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHB]] (+0.74, fdr 7e-06), [[EPHA2]] (+0.73, fdr 7e-06), [[EHD1]] (+0.69, fdr 7e-06); moves opposite to [[SNX13]] (-0.57, fdr 1e-05), [[SOS1]] (-0.53, fdr 2e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.50×** | +35.5 | 0e+00 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.40×** | +21.8 | 0e+00 | 47/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.15×** | +20.2 | 0e+00 | 46/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.54×** | +18.6 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.17×** | +17.0 | 0e+00 | 47/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **8.62×** | +16.6 | 0e+00 | 46/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.00×** | +16.2 | 0e+00 | 47/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.81×** | +15.2 | 0e+00 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.14×** | +15.2 | 0e+00 | 46/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +12.5 | 4e-34 | 41/46 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.21×** | +11.7 | 6e-30 | 39/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.40×** | +11.6 | 1e-29 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +10.2 | 8e-23 | 43/48 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.08×** | +9.7 | 1e-20 | 42/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +9.4 | 1e-19 | 39/48 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +8.6 | 3e-16 | 39/48 (SK-MEL-2, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +8.2 | 1e-14 | 35/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +6.5 | 2e-09 | 32/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +4.1 | 9e-04 | 23/49 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.010 | 17/48 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.027 | 12/48 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.650×** | -6.3 | 1e-07 | 34/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.676×** | -6.3 | 1e-07 | 35/49 (NCI-H23, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.693×** | -6.0 | 4e-07 | 32/48 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.660×** | -5.9 | 7e-07 | 34/47 (NCI-H23, HCT15, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.674×** | -5.8 | 8e-07 | 33/49 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.665×** | -5.8 | 8e-07 | 30/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.703×** | -5.5 | 2e-06 | 30/49 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.764×** | -5.5 | 2e-06 | 27/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.668×** | -5.5 | 3e-06 | 30/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -5.1 | 2e-05 | 7/49 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.760×** | -4.7 | 2e-04 | 29/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.579×** | -4.2 | 0.001 | 22/45 (SK-MEL-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.756×** | -3.9 | 0.005 | 22/48 (NCI-H23, SK-MEL-2, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.612×** | -3.8 | 0.007 | 22/47 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.711×** | -3.6 | 0.013 | 18/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.018 | 18/47 (HS-578T, SK-MEL-2, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.789×** | -3.5 | 0.018 | 15/47 (A498, SNU-423, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.020 | 18/47 (LoVo, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 75.9 | 7 (2 ⚠) | 13 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +24.4) | [[Adagrasib (drug)]] 0.05 µM 0.540× (z -19.5) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.239× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 43.0 | 19 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +28.8) | — |
| [[NCI-H1573 (line)]] | alt | 60.6 | 13 (6 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +23.9) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.269× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 85.8 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +22.5) | — |
| [[SW480 (line)]] | alt | 55.3 | 10 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.0) | [[Cobimetinib (drug)]] 5 µM 0.391× (z -9.3) |
| [[LoVo (line)]] | wt | 54.5 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +26.3) | — |
| [[PANC-1 (line)]] | alt | 29.6 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +21.8) | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +19.0) | — |
| [[HS-578T (line)]] | alt | 33.8 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +22.1) | — |
| [[SW48 (line)]] | wt | 164 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 33.1 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +20.4) | — |
| [[A-427 (line)]] | wt | 21.4 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 83.0 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +20.4) | — |
| [[SNU-423 (line)]] | alt | 46.5 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +22.8) | — |
| [[A549 (line)]] | wt | 88.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +25.5) | — |
| [[RKO (line)]] | wt | 74.0 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +17.2) | — |
| [[BT-474 (line)]] | alt | 46.4 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +19.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +18.9) | [[Adagrasib (drug)]] 0.05 µM 0.597× (z -13.5) ⚠ position not correctable |
| [[AsPC-1 (line)]] | alt | 65.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +22.9) | — |
| [[HEC-1-A (line)]] | alt | 107 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 56.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +18.9) | — |
| [[C32 (line)]] | wt | 37.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +22.1) | — |
| [[HepG2_C3A (line)]] | wt | 50.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +15.1) | — |
| [[Panc 03.27 (line)]] | alt | 42.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +16.3) | — |
| [[SW 900 (line)]] | alt | 68.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +17.4) | — |
| [[H4 (line)]] | wt | 38.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +15.4) | — |
| [[HCT15 (line)]] | alt | 55.6 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.17× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.70× (z +8.9) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.192× (z -12.0) |
| [[Hs 766T (line)]] | wt | 41.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +17.9) | — |
| [[LS 180 (line)]] | wt | 82.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +16.7) | — |
| [[NCI-H1792 (line)]] | alt | 21.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +16.7) | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 47.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +17.1) | — |
| [[SW1417 (line)]] | alt | 53.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.3) | — |
| [[A498 (line)]] | wt | 74.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +24.0) | — |
| [[CFPAC-1 (line)]] | alt | 48.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +20.4) | — |
| [[SHP-77 (line)]] | alt | 57.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +13.3) | — |
| [[SNU-1 (line)]] | wt | 87.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 37.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 46.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +10.1) | — |
| [[KATO III (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.6) | — |
| [[SW 1271 (line)]] | alt | 86.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHB]] | +0.74 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 | STRING 480 |
| [[EHD1]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PMEPA1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[FOSL1]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[STMN3]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DUSP5]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[VPS37B]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CSRNP1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ITGA3]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[IER2]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX13]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[SOS1]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARC]] | B | ARC activity raises MAP2K3's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.25× lower at baseline in the lines without ARC | 0.064 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[JAG1]] | B | JAG1 activity raises MAP2K3's level | lines that do not express JAG1 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without JAG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |
| [[MAP2K1]] | B | MAP2K1 activity raises MAP2K3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SHB]] | B | SHB activity raises MAP2K3's level | lines that do not express SHB (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without SHB | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.1, 2.3); signed map (5.5, 39.7). **Vector** length 110, 40.0% of its response variance represented; |z| ≥ 3 in 1,719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.4 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.5 | +18.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +6.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.7 | +0.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -8.5 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -8.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -0.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.8 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.2 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.1 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:21,284,672-21,315,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEK3, MKK3, MAPKK3, SAPKK2; previously PRKMK3 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, HEME_METABOLISM, TNFA_SIGNALING_VIA_NFKB, MTORC1_SIGNALING |
| Reactome | 29 pathways, smallest: Uptake and function of anthrax toxins; Uptake and actions of bacterial toxins; activated TAK1 mediates p38 MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P46734](https://www.uniprot.org/uniprotkb/P46734) (Dual specificity mitogen-activated protein kinase kinase 3):

> Dual specificity kinase. Is activated by cytokines and environmental stress in vivo. Catalyzes the concomitant phosphorylation of a threonine and a tyrosine residue in the MAP kinase p38. Part of a signaling cascade that begins with the activation of the adrenergic receptor ADRA1B and leads to the activation of MAPK14.

**Summary**, from NCBI Gene [5606](https://www.ncbi.nlm.nih.gov/gene/5606):

> The protein encoded by this gene is a dual specificity protein kinase that belongs to the MAP kinase kinase family. This kinase is activated by mitogenic and environmental stress, and participates in the MAP kinase-mediated signaling cascade. It phosphorylates and thus activates MAPK14/p38-MAPK. This kinase can be activated by insulin, and is necessary for the expression of glucose transporter. Expression of RAS oncogene is found to result in the accumulation of the active form of this kinase, …

**Accessions** — [HGNC:6843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6843) · Entrez [5606](https://www.ncbi.nlm.nih.gov/gene/5606) · UniProt [P46734](https://www.uniprot.org/uniprotkb/P46734) · Ensembl [ENSG00000034152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000034152)

## Data

Gene col 420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 420); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 420]; `tensor/DDL_lfc|DDL_z.npy` [420]; `embed/gene_vectors.npy` [420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 420 or target_col == 420). Every well: [[MAP2K3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2K3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
