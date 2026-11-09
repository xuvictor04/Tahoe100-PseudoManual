---
symbol: "CYTOR"
type: "gene"
col: 13335
ensembl_id: "ENSG00000222041"
name: "cytoskeleton regulator RNA"
location: "2p11.2"
module: 151
arm: "+"
pooled_cpm: 158.18
n_lines_expressing: 48
n_dd_up: 33
n_dd_down: 41
n_dd_up_clean: 22
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# CYTOR

*cytoskeleton regulator RNA* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.17× (z +14.7, q 0e+00, up in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.41× (z +11.8, q 6e-30, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.622× (z -9.1, q 7e-17, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4435-2HG]] (+0.87, fdr 7e-06), [[ANAPC1P4]] (+0.76, fdr 7e-06), [[BACH1]] (+0.69, fdr 7e-06); moves opposite to [[DRAM2]] (-0.56, fdr 1e-05), [[RCOR3]] (-0.53, fdr 1e-05), [[CASC3]] (-0.53, fdr 1e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00460]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.17×** | +14.7 | 0e+00 | 38/46 (NCI-H23, LS 180, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.41×** | +11.8 | 6e-30 | 42/47 (NCI-H460, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +10.0 | 3e-21 | 40/46 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +9.8 | 1e-20 | 37/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.97×** | +9.1 | 8e-18 | 37/46 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.03×** | +9.1 | 8e-18 | 37/46 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.81×** | +7.9 | 2e-13 | 34/46 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.74×** | +7.4 | 8e-12 | 36/46 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.64×** | +6.6 | 2e-09 | 33/46 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +6.3 | 2e-08 | 35/46 (NCI-H2030, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.7 | 8e-07 | 28/46 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +5.6 | 1e-06 | 32/46 (SHP-77, LS 180, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.54×** | +5.5 | 1e-06 | 28/45 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +5.3 | 6e-06 | 27/47 (SHP-77, LS 180, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +4.9 | 3e-05 | 28/46 (LS 180, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.8 | 7e-05 | 25/46 (SHP-77, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.002 | 30/47 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.014 | 23/47 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.015 | 21/46 (HepG2/C3A, SK-MEL-2, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.021 | 24/47 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.033 | 22/46 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.041 | 23/46 (LS 180, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -9.1 | 7e-17 | 35/47 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.532×** | -9.0 | 9e-17 | 35/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.516×** | -8.9 | 1e-16 | 39/46 (KATO III, HCT15, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.594×** | -8.7 | 7e-16 | 35/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.534×** | -8.1 | 4e-14 | 31/46 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -7.1 | 9e-11 | 31/42 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.577×** | -7.1 | 9e-11 | 31/45 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.594×** | -7.0 | 1e-10 | 34/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.620×** | -7.0 | 2e-10 | 31/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -6.9 | 2e-10 | 31/46 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.594×** | -6.8 | 7e-10 | 32/45 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.654×** | -6.6 | 2e-09 | 32/46 (SW480, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.615×** | -6.1 | 6e-08 | 34/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.661×** | -5.6 | 1e-06 | 25/47 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.756×** | -5.3 | 4e-06 | 25/46 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.476×** | -5.2 | 6e-06 | 29/48 (SHP-77, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.685×** | -5.1 | 1e-05 | 27/46 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -5.1 | 1e-05 | 25/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 263 | 4 (4 ⚠) | 15 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.62× (z +9.7) ⚠ cell-cycle shift, explains ~32% of this change | [[Binimetinib (drug)]] 0.5 µM 0.274× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 259 | 0 | 17 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -18.5) |
| [[HCT15 (line)]] | alt | 86.6 | 4 (3 ⚠) | 10 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.82× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.23× (z +8.8) | [[Trametinib (drug)]] 5 µM 0.199× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 130 | 14 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.66× (z +15.0) | — |
| [[KATO III (line)]] | alt | 113 | 7 (4 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.38× (z +11.1) | [[Ponatinib (drug)]] 5 µM 0.298× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 238 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 214 | 3 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +20.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +10.6) | [[Cobimetinib (drug)]] 5 µM 0.208× (z -12.8) |
| [[SNU-1 (line)]] | wt | 329 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.43× (z +17.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.71× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 554 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -20.0) |
| [[SK-MEL-2 (line)]] | alt | 116 | 5 (3 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 5.27× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.93× (z +9.9) | [[Trametinib (drug)]] 5 µM 0.176× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 112 | 4 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.60× (z +10.0) | [[Trametinib (drug)]] 0.5 µM 0.301× (z -11.1) |
| [[LS 180 (line)]] | wt | 47.9 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +17.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.17× (z +12.6) | — |
| [[RKO (line)]] | wt | 479 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -15.5) |
| [[SHP-77 (line)]] | alt | 80.6 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.34× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -21.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 137 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +10.2) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.284× (z -10.4) |
| [[HOP62 (line)]] | alt | 221 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.49× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -11.8) ⚠ toxic · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.386× (z -8.7) |
| [[HT-29 (line)]] | alt | 56.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +13.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.06× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.51× (z +11.6) | [[Adagrasib (drug)]] 0.05 µM 0.519× (z -15.0) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 87.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +10.6) | — |
| [[A-172 (line)]] | wt | 252 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.41× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.4) |
| [[A498 (line)]] | wt | 221 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -15.5) |
| [[J82 (line)]] | alt | 241 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.50× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.321× (z -10.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.5) |
| [[LoVo (line)]] | wt | 40.5 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.56× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 169 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 60.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +11.2) | — |
| [[SW48 (line)]] | wt | 103 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.00× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.7) |
| [[A549 (line)]] | wt | 164 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 168 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 5.93× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 125 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 83.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 219 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.9) |
| [[HS-578T (line)]] | alt | 87.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.17× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 40.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.38× (z +10.5) | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.119× (z -9.4) |
| [[PANC-1 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 168 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.55× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 206 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.8) |
| [[AN3 CA (line)]] | alt | 181 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 37.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4435-2HG]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[ANAPC1P4]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[BACH1]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[KPNA4]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.64 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ABL2]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[IQCJ-SCHIP1]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MIR222HG]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ASAP1]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SGMS2]] | +0.62 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[CCN1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM2]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CASC3]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[APTR]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 | same gene group |
| [[MKRN1]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SEC61A2]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PCMTD1]] | -0.51 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[CNNM2]] | -0.50 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00460]] | B | LINC00460 activity raises CYTOR's level | lines that do not express LINC00460 (31) vs lines expressing it (19) | 1.73× lower at baseline in the lines without LINC00460 | 0.030 | ⚠ within organs, on part of the lines; also absent: LINC02335, LINC01605, KISS1 |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises CYTOR's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without ITGB1-DT | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[LTBP2]] | B | LTBP2 activity raises CYTOR's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without LTBP2 | 0.037 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[TOP2A]] | B | TOP2A activity raises CYTOR's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC03004]] | B | LINC03004 activity raises CYTOR's level | lines that do not express LINC03004 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without LINC03004 | 0.069 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, OR4F15, ADAM12; maybe low, not absent |
| [[ADAMTS12]] | B | ADAMTS12 activity weakens CYTOR's drug response | lines that do not express ADAMTS12 (31) vs lines expressing it (17) | the lines without ADAMTS12 respond 1.55× as strongly (z diff -1.97); strongest at Harringtonine 5 µM: 2.50x vs 1.30x (z diff -5.0) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; target measured in part of the lines; artifact flags |
| [[ADAMTS12]] | B | ADAMTS12 activity raises CYTOR's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 1.69× lower at baseline in the lines without ADAMTS12 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises CYTOR's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without PDCD1LG2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, 10.1); signed map (11.5, 40.9). **Vector** length 155, 59.5% of its response variance represented; |z| ≥ 3 in 1,935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +9.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.5 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +11.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.3 | +5.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.9 | +3.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.3 | -9.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.1 | -6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.0 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -8.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.9 | -7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.4 | -8.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.3 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | cytoskeleton regulator RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p11.2 — chr2:87,454,781-87,636,740 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MGC4677; previously C2orf59, NCRNA00152, LINC00152 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [112597](https://www.ncbi.nlm.nih.gov/gene/112597):

> This gene produces a long non-coding RNA that is overexpressed in cancer cells and promotes cell proliferation and epithelial-mesenchymal transition. This RNA may bind enhancer of zeste homolog 2 and participate in the transcriptional silencing of tumor suppressor genes. It may act as a sponge for microRNAs. Alternatively spliced variants have been observed. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:28717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28717) · Entrez [112597](https://www.ncbi.nlm.nih.gov/gene/112597) · Ensembl [ENSG00000222041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000222041)

## Data

Gene col 13335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13335); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13335]; `tensor/DDL_lfc|DDL_z.npy` [13335]; `embed/gene_vectors.npy` [13335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13335 or target_col == 13335). Every well: [[CYTOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYTOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
