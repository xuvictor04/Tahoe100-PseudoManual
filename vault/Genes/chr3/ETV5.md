---
symbol: "ETV5"
type: "gene"
col: 14403
ensembl_id: "ENSG00000244405"
name: "ETS variant transcription factor 5"
location: "3q27.2"
module: 174
arm: "+"
pooled_cpm: 82.31
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 39
n_dd_up_clean: 14
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# ETV5

*ETS variant transcription factor 5* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.56× (z +21.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.0966× (z -50.3, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB5]] (+0.72, fdr 7e-06), [[SPRED2]] (+0.70, fdr 7e-06), [[PHC2]] (+0.70, fdr 7e-06); moves opposite to [[TBC1D22B]] (-0.62, fdr 2e-05), [[ANXA4]] (-0.61, fdr 3e-05), [[DECR1]] (-0.60, fdr 9e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ASTL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.56×** | +21.0 | 0e+00 | 47/48 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +20.1 | 0e+00 | 47/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +19.9 | 0e+00 | 45/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +13.2 | 1e-37 | 40/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +9.4 | 8e-19 | 34/48 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +8.2 | 2e-14 | 24/48 (Panc 03.27, COLO 205, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +7.9 | 2e-13 | 29/48 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.40×** | +7.2 | 3e-11 | 31/47 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +7.2 | 4e-11 | 35/49 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.23×** | +6.4 | 7e-09 | 23/48 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.28×** | +5.5 | 3e-06 | 21/48 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.4 | 3e-06 | 26/48 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +5.3 | 4e-06 | 25/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.06×** | +5.2 | 1e-05 | 27/48 (Panc 03.27, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +5.0 | 2e-05 | 17/49 (SNU-1, PANC-1, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.23×** | +4.7 | 1e-04 | 18/47 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 2e-04 | 21/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 4e-04 | 22/48 (SNU-1, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.0966×** | -50.3 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.107×** | -45.5 | 0e+00 | 49/50 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.132×** | -43.7 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.152×** | -42.1 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.223×** | -40.2 | 0e+00 | 48/48 (SW480, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.226×** | -33.0 | 0e+00 | 47/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.253×** | -30.8 | 0e+00 | 47/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.409×** | -27.3 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.278×** | -26.5 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.399×** | -24.0 | 0e+00 | 45/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -16.9 | 0e+00 | 33/43 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.139×** | -14.1 | 3e-43 | 41/46 (A-427, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.177×** | -12.4 | 2e-33 | 43/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.191×** | -11.8 | 1e-30 | 42/50 (SW480, A-427, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.667×** | -11.2 | 1e-27 | 39/49 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.517×** | -10.7 | 3e-25 | 42/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.647×** | -9.7 | 7e-21 | 30/48 (KATO III, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 176 | 3 | 22 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.07× (z +11.3) | [[Cobimetinib (drug)]] 5 µM 0.0363× (z -49.8) |
| [[KATO III (line)]] | alt | 108 | 3 | 19 (5 ⚠) | [[Belinostat (drug)]] 5 µM 2.76× (z +10.0) | [[Ponatinib (drug)]] 0.5 µM 0.0546× (z -28.5) |
| [[PANC-1 (line)]] | alt | 89.3 | 3 | 18 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.16× (z +10.4) | [[Cobimetinib (drug)]] 5 µM 0.0708× (z -34.3) |
| [[NCI-H2347 (line)]] | alt | 112 | 3 | 17 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +10.4) | [[Cobimetinib (drug)]] 5 µM 0.0873× (z -22.2) |
| [[A-427 (line)]] | wt | 151 | 0 | 19 (4 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0427× (z -33.2) |
| [[A498 (line)]] | wt | 55.0 | 4 | 14 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.23× (z +13.1) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.150× (z -20.3) |
| [[MIA PaCa-2 (line)]] | alt | 138 | 0 | 18 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.291× (z -44.3) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0371× (z -33.7) |
| [[Panc 03.27 (line)]] | alt | 44.6 | 5 | 13 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +15.9) | [[Cobimetinib (drug)]] 5 µM 0.0885× (z -18.9) |
| [[SW1417 (line)]] | alt | 89.5 | 5 | 13 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.31× (z +14.8) | [[Cobimetinib (drug)]] 5 µM 0.0790× (z -24.7) |
| [[COLO 205 (line)]] | alt | 39.5 | 7 (3 ⚠) | 10 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +14.3) | [[Cobimetinib (drug)]] 5 µM 0.0483× (z -17.9) |
| [[NCI-H460 (line)]] | wt | 52.1 | 7 (4 ⚠) | 10 | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +13.3) | [[Trametinib (drug)]] 0.5 µM 0.183× (z -22.8) |
| [[CFPAC-1 (line)]] | alt | 49.8 | 4 | 11 | [[Panobinostat (drug)]] 5 µM 3.71× (z +11.4) | [[Cobimetinib (drug)]] 5 µM 0.0883× (z -20.1) |
| [[Hs 766T (line)]] | wt | 41.1 | 3 | 11 | [[Panobinostat (drug)]] 5 µM 3.96× (z +10.9) | [[Trametinib (drug)]] 5 µM 0.0498× (z -19.6) |
| [[HT-29 (line)]] | alt | 58.2 | 3 | 11 | [[Belinostat (drug)]] 5 µM 3.17× (z +9.8) | [[Cobimetinib (drug)]] 5 µM 0.0550× (z -23.6) |
| [[LoVo (line)]] | wt | 64.7 | 4 (1 ⚠) | 10 | [[Belinostat (drug)]] 5 µM 3.67× (z +12.6) | [[Cobimetinib (drug)]] 5 µM 0.0615× (z -25.9) |
| [[NCI-H2030 (line)]] | alt | 81.5 | 2 | 12 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.73× (z +9.0) | [[Cobimetinib (drug)]] 5 µM 0.0876× (z -21.0) |
| [[SHP-77 (line)]] | alt | 54.0 | 0 | 14 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0240× (z -26.0) |
| [[SK-MEL-2 (line)]] | alt | 155 | 3 | 11 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.0) | [[Cobimetinib (drug)]] 5 µM 0.0688× (z -28.2) |
| [[A-172 (line)]] | wt | 66.2 | 3 | 10 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.59× (z +12.9) | [[Cobimetinib (drug)]] 5 µM 0.145× (z -18.8) |
| [[C32 (line)]] | wt | 79.9 | 0 | 13 | — | [[Binimetinib (drug)]] 0.5 µM 0.128× (z -22.1) |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 13 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0517× (z -28.8) |
| [[HOP62 (line)]] | alt | 96.0 | 1 | 12 | [[Belinostat (drug)]] 5 µM 2.47× (z +9.5) | [[Cobimetinib (drug)]] 5 µM 0.0688× (z -26.9) |
| [[HS-578T (line)]] | alt | 126 | 3 | 10 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.56× (z +10.7) | [[Cobimetinib (drug)]] 5 µM 0.143× (z -21.3) |
| [[J82 (line)]] | alt | 75.4 | 3 | 10 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.95× (z +12.3) | [[Cobimetinib (drug)]] 5 µM 0.142× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 61.8 | 4 | 9 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +11.8) | [[Trametinib (drug)]] 5 µM 0.150× (z -16.0) |
| [[SNU-1 (line)]] | wt | 133 | 0 | 13 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0256× (z -30.9) |
| [[A549 (line)]] | wt | 36.6 | 3 | 9 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.73× (z +11.4) | [[Cobimetinib (drug)]] 5 µM 0.100× (z -19.2) |
| [[AsPC-1 (line)]] | alt | 37.0 | 3 | 9 | [[Belinostat (drug)]] 5 µM 4.63× (z +13.3) | [[Cobimetinib (drug)]] 5 µM 0.0808× (z -21.0) |
| [[LOX-IMVI (line)]] | wt | 67.8 | 4 | 8 | [[Panobinostat (drug)]] 5 µM 3.80× (z +13.2) | [[Trametinib (drug)]] 5 µM 0.0782× (z -21.0) |
| [[SNU-423 (line)]] | alt | 49.6 | 4 | 8 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +12.1) | [[Cobimetinib (drug)]] 5 µM 0.0960× (z -21.2) |
| [[H4 (line)]] | wt | 126 | 0 | 11 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0662× (z -24.1) |
| [[HCT15 (line)]] | alt | 87.5 | 0 | 11 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0506× (z -23.3) |
| [[NCI-H23 (line)]] | alt | 51.2 | 0 | 11 | — | [[Trametinib (drug)]] 5 µM 0.0946× (z -20.1) |
| [[SW 900 (line)]] | alt | 102 | 0 | 11 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0722× (z -23.2) |
| [[AN3 CA (line)]] | alt | 106 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.0857× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 36.7 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.42× (z +13.3) | [[Trametinib (drug)]] 5 µM 0.0721× (z -18.6) |
| [[RKO (line)]] | wt | 102 | 1 | 9 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.56× (z +9.5) | [[Cobimetinib (drug)]] 5 µM 0.121× (z -20.5) |
| [[HepG2_C3A (line)]] | wt | 93.3 | 0 | 9 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0846× (z -21.8) |
| [[CHP-212 (line)]] | wt | 61.3 | 0 | 8 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0789× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 51.8 | 3 | 5 | [[Panobinostat (drug)]] 0.5 µM 4.49× (z +10.6) | [[Cobimetinib (drug)]] 5 µM 0.0430× (z -21.3) |
| [[C-33 A (line)]] | alt | 51.0 | 0 | 7 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0527× (z -16.7) |
| [[BT-474 (line)]] | alt | 28.1 | 0 | 6 | — | [[Trametinib (drug)]] 0.5 µM 0.178× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 6 | — | [[Trametinib (drug)]] 5 µM 0.0717× (z -22.5) |
| [[LS 180 (line)]] | wt | 64.8 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.102× (z -12.4) |
| [[SW 1271 (line)]] | alt | 97.0 | 0 | 4 | — | [[Trametinib (drug)]] 0.5 µM 0.0820× (z -12.6) |
| [[SW48 (line)]] | wt | 64.2 | 0 | 3 | — | [[Trametinib (drug)]] 5 µM 0.122× (z -10.8) |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB5]] | +0.72 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[SPRED2]] | +0.70 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[PHC2]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.68 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TOX2]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ETV4]] | +0.67 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[ZFYVE28]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 606 |
| [[SPRY4]] | +0.65 | +0.73 / +0.65 | both halves | 7e-06 | STRING 638 |
| [[EIF4EBP1]] | +0.65 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[RAC2]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[RNF168]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D22B]] | -0.62 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ANXA4]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[DECR1]] | -0.60 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[MR1]] | -0.60 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[AHI1-DT]] | -0.60 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[DUSP16]] | -0.59 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[GBP1]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[TAPBPL]] | -0.58 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[KMO]] | -0.57 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GAS2]] | -0.57 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[DRAM1]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[RAB21]] | -0.56 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASTL]] | B | ASTL activity raises ETV5's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without ASTL | 0.013 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ETV5's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FYN]] | C | FYN activity strengthens ETV5's drug response | lines that do not express FYN (8) vs lines expressing it (42) | the lines without FYN respond 1.08× as strongly (z diff +2.35); strongest at Binimetinib 0.5 µM: 0.35x vs 0.37x (z diff +3.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent; rests on the correction |
| [[STX1A]] | C | STX1A activity weakens ETV5's drug response | lines that do not express STX1A (3) vs lines expressing it (47) | the lines without STX1A respond 1.11× as strongly (z diff -4.41); strongest at Binimetinib 0.5 µM: 0.31x vs 0.37x (z diff -4.9) | 0.083 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent; rests on the correction |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.2, 5.1); signed map (6.6, 48.2). **Vector** length 150, 53.7% of its response variance represented; |z| ≥ 3 in 2,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +9.4 | +21.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.6 | +20.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.4 | +19.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.1 | +13.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.1 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +7.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.4 | +5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.4 | +7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.9 | +4.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -15.1 | -45.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -15.0 | -40.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -14.2 | -50.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -13.5 | -33.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -13.1 | -43.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -12.6 | -42.1 |

## What is on record

|  |  |
|---|---|
| Name | ETS variant transcription factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:186,046,314-186,110,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERM |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P41161](https://www.uniprot.org/uniprotkb/P41161) (ETS translocation variant 5):

> Binds to DNA sequences containing the consensus nucleotide core sequence 5'-GGAA.-3'.

**Summary**, from NCBI Gene [2119](https://www.ncbi.nlm.nih.gov/gene/2119):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in cellular response to oxidative stress; negative regulation of transcription by RNA polymerase II; and positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3494) · Entrez [2119](https://www.ncbi.nlm.nih.gov/gene/2119) · UniProt [P41161](https://www.uniprot.org/uniprotkb/P41161) · Ensembl [ENSG00000244405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244405)

## Data

Gene col 14403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14403); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14403]; `tensor/DDL_lfc|DDL_z.npy` [14403]; `embed/gene_vectors.npy` [14403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14403 or target_col == 14403). Every well: [[ETV5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETV5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
