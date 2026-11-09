---
symbol: "MFSD6"
type: "gene"
col: 7551
ensembl_id: "ENSG00000151690"
name: "major facilitator superfamily domain containing 6"
location: "2q32.2"
module: 55
arm: "+"
pooled_cpm: 42.7
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 28
direction_downstream: 0
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# MFSD6

*major facilitator superfamily domain containing 6* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.49× (z +8.1, q 4e-13, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.439× (z -23.5, q 0e+00, down in 36 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.577× (z -11.1, q 1e-26, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICA1]] (+0.55, fdr 1e-05), [[TMEM30B]] (+0.54, fdr 4e-05), [[PERP]] (+0.54, fdr 4e-05); moves opposite to [[SYDE1]] (-0.54, fdr 3e-05), [[SSH1]] (-0.48, fdr 5e-05), [[ATP8B3]] (-0.47, fdr 4e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[C1orf116]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 4e-13 | 29/46 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.8 | 2e-12 | 24/41 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.1 | 3e-10 | 18/34 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.25×** | +6.4 | 2e-08 | 23/46 (LS 180, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.7 | 1e-06 | 20/46 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.29×** | +5.3 | 1e-05 | 21/46 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +4.7 | 2e-04 | 18/36 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +4.5 | 6e-04 | 15/46 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.004 | 13/46 (NCI-H460, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +3.8 | 0.008 | 17/46 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.015 | 8/46 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.015 | 15/45 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.018 | 16/44 (SK-MEL-2, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.022 | 15/45 (NCI-H460, LS 180, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.027 | 7/46 (NCI-H1573, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.045 | 8/46 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.065 | 6/46 (C-33 A, hTERT-HPNE, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.083 | 5/46 (BT-474, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.439×** | -23.5 | 0e+00 | 36/45 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.412×** | -17.9 | 0e+00 | 36/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.432×** | -16.9 | 0e+00 | 37/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.460×** | -15.6 | 0e+00 | 32/45 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.469×** | -15.3 | 0e+00 | 36/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.548×** | -12.1 | 6e-32 | 36/46 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.577×** | -11.1 | 1e-26 | 31/46 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -10.3 | 5e-23 | 32/47 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.617×** | -9.7 | 2e-20 | 34/46 (LS 180, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -9.6 | 4e-20 | 29/45 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.434×** | -8.8 | 6e-17 | 30/44 (RKO, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.656×** | -8.5 | 1e-15 | 29/46 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.659×** | -8.4 | 2e-15 | 28/45 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -7.9 | 1e-13 | 27/46 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.679×** | -7.5 | 3e-12 | 24/45 (NCI-H1792, NCI-H460, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -6.6 | 1e-09 | 25/46 (HT-29, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.726×** | -4.6 | 1e-04 | 20/46 (KATO III, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.659×** | -4.4 | 3e-04 | 17/45 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.676×** | -4.1 | 9e-04 | 15/45 (LoVo, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.688×** | -3.9 | 0.002 | 17/44 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.823×** | -3.9 | 0.002 | 20/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.706×** | -3.7 | 0.005 | 16/45 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.707×** | -3.6 | 0.005 | 15/45 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.777×** | -3.6 | 0.006 | 10/46 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 99.3 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -27.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.296× (z -14.0) |
| [[LoVo (line)]] | wt | 73.7 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -30.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.179× (z -10.7) |
| [[Hs 766T (line)]] | wt | 61.7 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.124× (z -9.4) |
| [[KATO III (line)]] | alt | 89.7 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -22.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.168× (z -10.7) |
| [[SW480 (line)]] | alt | 73.7 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -27.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.491× (z -10.5) |
| [[SW48 (line)]] | wt | 75.6 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -8.8) |
| [[HT-29 (line)]] | alt | 98.3 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.217× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 39.4 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -21.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 60.0 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0951× (z -18.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 56.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 29.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 57.3 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.131× (z -12.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.209× (z -9.3) |
| [[A549 (line)]] | wt | 50.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -18.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 62.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 37.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.348× (z -9.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.365× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 70.9 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -14.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 91.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 56.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.99× (z +9.7) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.113× (z -10.8) |
| [[A498 (line)]] | wt | 23.5 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.75× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 14.9 | 0 | 3 (1 ⚠) | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0592× (z -12.0) |
| [[HCT15 (line)]] | alt | 56.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 34.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 27.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0615× (z -19.2) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[NCI-H1573 (line)]] | alt | 38.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 58.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 28.7 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0322× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICA1]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TMEM30B]] | +0.54 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[PERP]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[LPGAT1]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SLC44A5]] | +0.54 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[POF1B]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[HTR1D]] | +0.52 | +0.42 / +0.44 | both halves | 4e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[TNFSF15]] | +0.52 | +0.53 / +0.37 | both halves | 9e-05 |  |
| [[C4BPB]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[EPS8L3]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CLIC5]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SYK]] | +0.51 | +0.51 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYDE1]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[SSH1]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ATP8B3]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[NR2F2-AS1]] | -0.47 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[GYS1]] | -0.47 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[MLXIP]] | -0.46 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[NUMBL]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[LINC02985]] | -0.43 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[XYLT2]] | -0.43 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[ZNF404]] | -0.43 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[NAV1]] | -0.42 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[GLIS3]] | -0.42 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 28, C 0. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf116]] | B | C1orf116 activity raises MFSD6's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TOX3]] | B | TOX3 activity raises MFSD6's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without TOX3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[PCDH1]] | B | PCDH1 activity raises MFSD6's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.88× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[LMO7]] | B | LMO7 activity raises MFSD6's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without LMO7 | 0.010 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[COL17A1]] | B | COL17A1 activity raises MFSD6's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without COL17A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[LGR6]] | B | LGR6 activity raises MFSD6's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.37× lower at baseline in the lines without LGR6 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises MFSD6's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.34× lower at baseline in the lines without TMPRSS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SLC22A3]] | B | SLC22A3 activity raises MFSD6's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without SLC22A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[ICA1]] | B | ICA1 activity raises MFSD6's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without ICA1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[LPAR5]] | B | LPAR5 activity raises MFSD6's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without LPAR5 | 0.025 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[SYK]] | B | SYK activity raises MFSD6's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without SYK | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[TSPAN8]] | B | TSPAN8 activity raises MFSD6's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without TSPAN8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.4, 46.6); signed map (53.6, 5.9). **Vector** length 97.1, 25.5% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +7.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +3.5 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.4 | -17.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.2 | -16.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.0 | -15.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | major facilitator superfamily domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:190,408,355-190,509,205 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC73A1, FLJ20160 |
| Gene groups (HGNC) | Solute carrier family 73 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZSS7](https://www.uniprot.org/uniprotkb/Q6ZSS7) (Major facilitator superfamily domain-containing protein 6):

> (Microbial infection) Acts as a receptor for respiratory enterovirus D68. Mechanistically, binds to viral particles and is required for viral cell entry while initial attachment to cells is mainly mediated by interactions with sialic acid.

**Summary**, from NCBI Gene [54842](https://www.ncbi.nlm.nih.gov/gene/54842):

> Predicted to enable MHC class I protein binding activity and MHC class I receptor activity. Predicted to be involved in antigen processing and presentation of exogenous peptide antigen via MHC class I. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24711) · Entrez [54842](https://www.ncbi.nlm.nih.gov/gene/54842) · UniProt [Q6ZSS7](https://www.uniprot.org/uniprotkb/Q6ZSS7) · Ensembl [ENSG00000151690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151690)

## Data

Gene col 7551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7551); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7551]; `tensor/DDL_lfc|DDL_z.npy` [7551]; `embed/gene_vectors.npy` [7551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7551 or target_col == 7551). Every well: [[MFSD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
