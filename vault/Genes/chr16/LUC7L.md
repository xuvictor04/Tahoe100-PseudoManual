---
symbol: "LUC7L"
type: "gene"
col: 146
ensembl_id: "ENSG00000007392"
name: "LUC7 like"
location: "16p13.3"
module: 131
arm: "+"
pooled_cpm: 96.32
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# LUC7L

*LUC7 like* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.89× (z +11.4, q 3e-27, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.459× (z -13.9, q 3e-41, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.773× (z -6.5, q 1e-08, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD18]] (+0.64, fdr 1e-05), [[POLR2J4]] (+0.63, fdr 1e-05), [[MAP2K7]] (+0.61, fdr 2e-05); moves opposite to [[DR1]] (-0.61, fdr 2e-05), [[TWF1]] (-0.54, fdr 3e-05), [[NRAS]] (-0.53, fdr 7e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Rucaparib (phosphate) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +11.4 | 3e-27 | 45/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +11.0 | 1e-25 | 44/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +10.0 | 2e-21 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +9.9 | 7e-21 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.8 | 1e-09 | 45/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +6.7 | 2e-09 | 37/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.43×** | +6.3 | 2e-08 | 36/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +6.0 | 2e-07 | 39/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +5.7 | 9e-07 | 36/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.8 | 1e-04 | 23/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 1e-04 | 32/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.7 | 1e-04 | 29/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 5e-04 | 35/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tomivosertib (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.006 | 25/48 (SW480, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.014 | 21/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.014 | 23/49 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -13.9 | 3e-41 | 46/49 (H4, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -13.1 | 7e-37 | 39/44 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -9.0 | 5e-17 | 40/45 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.773×** | -6.5 | 1e-08 | 38/48 (CHP-212, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -5.7 | 2e-06 | 35/48 (A549, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.747×** | -5.2 | 2e-05 | 35/48 (SW 900, BT-474, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.821×** | -5.0 | 5e-05 | 29/48 (SK-MEL-2, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.828×** | -4.8 | 1e-04 | 25/49 (CHP-212, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -4.2 | 0.001 | 26/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.793×** | -4.1 | 0.002 | 32/48 (J82, Panc 03.27, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **0.814×** | -3.7 | 0.012 | 24/48 (KATO III, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.025 | 23/48 (SNU-423, KATO III, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.830×** | -3.3 | 0.038 | 22/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.833×** | -3.3 | 0.043 | 18/47 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.834× | -3.2 | 0.043 | 17/47 (SNU-423, J82, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.835× | -3.2 | 0.043 | 18/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.073 | 17/47 (NCI-H23, C-33 A, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 89.2 | 6 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.41× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 152 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -15.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 115 | 4 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.41× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.30× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -16.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 138 | 4 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.47× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.37× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -19.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 84.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.25× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.20× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 80.4 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -15.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 105 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -11.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 96.1 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 115 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +10.8) | — |
| [[A549 (line)]] | wt | 101 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -25.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 139 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0555× (z -28.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 83.7 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 61.8 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -14.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.562× (z -9.4) |
| [[A-427 (line)]] | wt | 73.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -12.7) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.417× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 74.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 116 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 93.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 85.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.29× (z +8.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 50.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.28× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 84.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 87.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -14.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -16.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 93.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -12.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 84.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0437× (z -24.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -14.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 90.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 67.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -14.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 82.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.103× (z -9.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 127 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD18]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[POLR2J4]] | +0.63 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[MAP2K7]] | +0.61 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[LSM7]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 | STRING 565 |
| [[ACAD10]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[RBM6]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 | STRING 451 |
| [[DNLZ]] | +0.58 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[PI4KAP1-1]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[DDT]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FAM193A]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SNHG25]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RAB11FIP3]] | +0.54 | +0.38 / +0.56 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DR1]] | -0.61 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TWF1]] | -0.54 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[NRAS]] | -0.53 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[EIF4G2]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ALG10B]] | -0.52 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[GMFB]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[YWHAZ]] | -0.51 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SF3B4]] | -0.51 | -0.48 / -0.38 | both halves | 6e-05 | STRING 650 |
| [[PRELID3B]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[BBS10]] | -0.50 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[ZBED8]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SCRN1]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Rucaparib (phosphate) (drug)]] 0.5 µM | C | LUC7L's natural level lowers the cells' numbers under Rucaparib (phosphate) 0.5 µM (makes them more sensitive) | LUC7L's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.294 over the table, 0.0997 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.7, -14.9); signed map (-17.8, 0.0). **Vector** length 82.0, 23.5% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.4 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.5 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | +5.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +6.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -1.2 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.0 | -0.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | LUC7 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:188,969-229,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LUC7B1, hLuc7B1, Luc7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ29](https://www.uniprot.org/uniprotkb/Q9NQ29) (Putative RNA-binding protein Luc7-like 1):

> May bind to RNA via its Arg/Ser-rich domain.

**Summary**, from NCBI Gene [55692](https://www.ncbi.nlm.nih.gov/gene/55692):

> The LUC7L gene may represent a mammalian heterochromatic gene, encoding a putative RNA-binding protein similar to the yeast Luc7p subunit of the U1 snRNP splicing complex that is normally required for 5-prime splice site selection (Tufarelli et al., 2001 [PubMed 11170747]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:6723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6723) · Entrez [55692](https://www.ncbi.nlm.nih.gov/gene/55692) · UniProt [Q9NQ29](https://www.uniprot.org/uniprotkb/Q9NQ29) · Ensembl [ENSG00000007392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007392)

## Data

Gene col 146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 146); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 146]; `tensor/DDL_lfc|DDL_z.npy` [146]; `embed/gene_vectors.npy` [146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 146 or target_col == 146). Every well: [[LUC7L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LUC7L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
