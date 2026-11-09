---
symbol: "NVL"
type: "gene"
col: 6794
ensembl_id: "ENSG00000143748"
name: "nuclear VCP like"
location: "1q42.11"
module: 12
arm: "+"
pooled_cpm: 70.69
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NVL

*nuclear VCP like* — 1q42.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.41× (z +10.6, q 3e-23, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.38× (z +9.0, q 4e-17, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.636× (z -13.9, q 3e-41, down in 33 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.646× (z -13.4, q 1e-38, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX57]] (+0.70, fdr 7e-06), [[MPHOSPH10]] (+0.65, fdr 1e-05), [[DRG1]] (+0.63, fdr 1e-05); moves opposite to [[CD164]] (-0.55, fdr 2e-05), [[EIF4EBP2]] (-0.51, fdr 1e-04), [[MARCKSL1]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +10.6 | 3e-23 | 37/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +9.6 | 2e-19 | 33/48 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +9.0 | 4e-17 | 27/48 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +8.7 | 5e-16 | 27/49 (LoVo, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +8.4 | 4e-15 | 29/48 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +7.2 | 8e-11 | 26/48 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +6.3 | 2e-08 | 25/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +6.3 | 2e-08 | 24/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +5.7 | 9e-07 | 21/48 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.20×** | +5.6 | 1e-06 | 21/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.1 | 1e-05 | 21/48 (SW480, RKO, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.17× | +4.9 | 5e-05 | 18/48 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.12× | +4.8 | 9e-05 | 9/48 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.002 | 13/49 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.9 | 0.003 | 8/48 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.6 | 0.012 | 17/48 (KATO III, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.024 | 4/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.11× | +3.3 | 0.026 | 6/48 (LoVo, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.11× | +3.2 | 0.032 | 7/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.042 | 10/49 (KATO III, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.047 | 11/48 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.069 | 3/49 (LoVo, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.11× | +2.9 | 0.070 | 6/49 (NCI-H23, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -13.9 | 3e-41 | 33/48 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.646×** | -13.4 | 1e-38 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -11.8 | 5e-30 | 25/43 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.708×** | -9.2 | 7e-18 | 28/45 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.744×** | -9.1 | 1e-17 | 34/49 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -8.4 | 3e-15 | 29/47 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.761×** | -8.4 | 3e-15 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.764×** | -8.3 | 8e-15 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.771×** | -8.0 | 8e-14 | 27/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.863× | -4.1 | 0.002 | 16/48 (Hs 766T, SW480, …) | two highest doses |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.876× | -3.9 | 0.004 | 13/47 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | 0.888× | -3.7 | 0.011 | 16/48 (BT-474, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.889× | -3.6 | 0.011 | 9/47 (SNU-423, hTERT-HPNE, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.922× | -3.6 | 0.015 | 8/48 (NCI-H23, SW480, …) | two highest doses |  |
| [[OTS514 (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.016 | 14/46 (AsPC-1, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.025 | 4/48 (HS-578T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.927× | -3.3 | 0.027 | 7/48 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.896× | -3.3 | 0.031 | 4/48 (SW 1088, MIA PaCa-2, …) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.046 | 10/47 (HCT15, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.907× | -2.9 | 0.084 | 12/47 (SW 900, HCT15, …) | top dose only |  |
| [[Futibatinib (drug)]] 5 µM |  | 0.839× | -2.8 | 0.099 | 7/46 (HCT15, AN3 CA, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 179 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -30.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 10 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -18.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.405× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 95.1 | 1 (1 ⚠) | 8 (5 ⚠) | [[Belinostat (drug)]] 5 µM 1.66× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.235× (z -25.5) |
| [[A-172 (line)]] | wt | 83.4 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -15.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 80.5 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.289× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -13.1) |
| [[J82 (line)]] | alt | 125 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -12.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 54.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -18.8) |
| [[SW480 (line)]] | alt | 63.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.381× (z -15.5) |
| [[LoVo (line)]] | wt | 55.6 | 2 (2 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.02× (z +9.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -11.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 66.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -15.9) |
| [[SW1417 (line)]] | alt | 65.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.492× (z -8.5) |
| [[KATO III (line)]] | alt | 43.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.26× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.49× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.308× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 83.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.435× (z -10.6) |
| [[AN3 CA (line)]] | alt | 73.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 62.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -12.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 72.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.508× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.536× (z -9.0) |
| [[LS 180 (line)]] | wt | 55.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.429× (z -9.1) |
| [[RKO (line)]] | wt | 57.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 63.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -15.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 46.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 50.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H596 (line)]] | alt | 61.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.557× (z -10.4) |
| [[SNU-423 (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -11.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX57]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.65 | +0.66 / +0.57 | both halves | 1e-05 | STRING 621 |
| [[DRG1]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[MRPS11]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CINP]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 | same gene group |
| [[THAP7]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[AARSD1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RTCB]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MRPS26]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD164]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[EIF4EBP2]] | -0.51 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[MARCKSL1]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[PANK3]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 | same gene group |
| [[M6PR]] | -0.48 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[MMGT1]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CHRAC1]] | -0.48 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[SLC6A8]] | -0.47 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[PEAK1]] | -0.47 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[LINC02035]] | -0.47 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[GNG12]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.2, -8.2); signed map (-14.3, -12.4). **Vector** length 107, 26.5% of its response variance represented; |z| ≥ 3 in 1,188 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.4 | +8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.0 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.7 | -9.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.6 | -8.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Erlotinib (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear VCP like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.11 — chr1:224,227,334-224,330,189 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NVL2 |
| Gene groups (HGNC) | AAA ATPases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15381](https://www.uniprot.org/uniprotkb/O15381) (Nuclear valosin-containing protein-like):

> Participates in the assembly of the telomerase holoenzyme and effecting of telomerase activity via its interaction with TERT. Involved in both early and late stages of the pre-rRNA processing pathways. Spatiotemporally regulates 60S ribosomal subunit biogenesis in the nucleolus. Catalyzes the release of specific assembly factors, such as WDR74, from pre-60S ribosomal particles through the ATPase activity.

**Summary**, from NCBI Gene [4931](https://www.ncbi.nlm.nih.gov/gene/4931):

> This gene encodes a member of the AAA (ATPases associated with diverse cellular activities) superfamily. Multiple transcript variants encoding different isoforms have been found for this gene. Two encoded proteins, described as major and minor isoforms, have been localized to distinct regions of the nucleus. The largest encoded protein (major isoform) has been localized to the nucleolus and shown to participate in ribosome biosynthesis (PMID: 15469983, 16782053), while the minor isoform has …

**Accessions** — [HGNC:8070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8070) · Entrez [4931](https://www.ncbi.nlm.nih.gov/gene/4931) · UniProt [O15381](https://www.uniprot.org/uniprotkb/O15381) · Ensembl [ENSG00000143748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143748)

## Data

Gene col 6794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6794); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6794]; `tensor/DDL_lfc|DDL_z.npy` [6794]; `embed/gene_vectors.npy` [6794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6794 or target_col == 6794). Every well: [[NVL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NVL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
