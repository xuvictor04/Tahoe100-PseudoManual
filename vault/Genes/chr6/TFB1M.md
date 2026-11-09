---
symbol: "TFB1M"
type: "gene"
col: 392
ensembl_id: "ENSG00000029639"
name: "transcription factor B1, mitochondrial"
location: "6q25.3"
module: 134
arm: "+"
pooled_cpm: 47.44
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# TFB1M

*transcription factor B1, mitochondrial* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.77× (z +12.9, q 3e-35, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.353× (z -23.6, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.385× (z -21.6, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS13]] (+0.68, fdr 1e-05), [[HDHD5]] (+0.64, fdr 1e-05), [[MRPL17]] (+0.64, fdr 2e-05); moves opposite to [[SARM1]] (-0.56, fdr 3e-05), [[CAPN3]] (-0.55, fdr 4e-05), [[DAZAP2]] (-0.54, fdr 4e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FAM216A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +12.9 | 3e-35 | 38/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +12.5 | 2e-33 | 39/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +12.4 | 7e-33 | 39/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +10.9 | 2e-25 | 39/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.9 | 6e-10 | 25/47 (RKO, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +6.5 | 1e-08 | 24/47 (A498, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +6.0 | 2e-07 | 27/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 4e-06 | 22/47 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 4e-05 | 22/46 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 2e-04 | 13/47 (CFPAC-1, HS-578T, …) | two highest doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 14/47 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 11/46 (A-427, CFPAC-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.001 | 12/46 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.014 | 11/47 (CFPAC-1, Hs 766T, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.5 | 0.021 | 9/47 (A549, BT-474, …) | two highest doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.049 | 3/47 (SW 900, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.353×** | -23.6 | 0e+00 | 36/44 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -21.6 | 0e+00 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.403×** | -19.8 | 0e+00 | 31/38 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -19.5 | 0e+00 | 39/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.406×** | -18.9 | 0e+00 | 35/42 (C32, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.474×** | -16.9 | 0e+00 | 42/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.518×** | -14.9 | 0e+00 | 37/47 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.401×** | -10.8 | 2e-25 | 33/48 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -10.7 | 7e-25 | 35/46 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -9.9 | 3e-21 | 31/47 (C32, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -7.0 | 2e-10 | 25/47 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.557×** | -6.9 | 2e-10 | 23/47 (MIA PaCa-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -5.7 | 4e-07 | 25/46 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.787×** | -5.4 | 2e-06 | 21/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.653×** | -5.1 | 2e-05 | 20/42 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.830×** | -4.2 | 7e-04 | 19/47 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.795×** | -3.7 | 0.005 | 16/47 (BT-474, HCT15, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.864× | -3.3 | 0.020 | 5/47 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.826×** | -3.1 | 0.041 | 9/47 (H4, C32, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.873× | -3.0 | 0.060 | 8/46 (C32, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.836× | -2.9 | 0.072 | 8/47 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 168 | 0 | 16 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0929× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.193× (z -15.8) |
| [[MIA PaCa-2 (line)]] | alt | 162 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.170× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -14.6) |
| [[PANC-1 (line)]] | alt | 55.4 | 1 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -23.1) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.305× (z -11.3) |
| [[SW480 (line)]] | alt | 69.1 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0296× (z -44.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -19.5) |
| [[J82 (line)]] | alt | 42.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.265× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 58.6 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.185× (z -8.7) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.384× (z -9.5) |
| [[SHP-77 (line)]] | alt | 57.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.222× (z -12.0) |
| [[A-427 (line)]] | wt | 50.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.4) ⚠ cell-cycle shift, explains ~7% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0946× (z -22.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 79.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 49.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.9 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0950× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 82.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -18.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.3 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.76× (z +11.0) | — |
| [[A498 (line)]] | wt | 18.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -11.1) |
| [[C-33 A (line)]] | alt | 42.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -9.1) |
| [[HOP62 (line)]] | alt | 64.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -9.2) |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -11.1) |
| [[CHP-212 (line)]] | wt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0701× (z -14.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -21.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 56.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -11.3) |
| [[LoVo (line)]] | wt | 20.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -13.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 31.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 64.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.89× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.110× (z -9.0) |
| [[SW1417 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -14.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS13]] | +0.68 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[HDHD5]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MRPL17]] | +0.64 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ARL6]] | +0.64 | +0.57 / +0.51 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[CABIN1]] | +0.63 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ATG4C]] | +0.61 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[RIMKLA]] | +0.60 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CHD1L]] | +0.60 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[SERGEF]] | +0.59 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[FAM234B]] | +0.59 | +0.55 / +0.43 | both halves | 4e-05 |  |
| [[C17orf58]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZNF215]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SARM1]] | -0.56 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CAPN3]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DAZAP2]] | -0.54 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[EOLA2-DT]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[COPB2-DT]] | -0.54 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF846]] | -0.53 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[MC1R]] | -0.53 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[LINC02762]] | -0.52 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[PHF8]] | -0.51 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[RUSC1-AS1]] | -0.51 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[IL18BP]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CASTOR3P-1]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM216A]] | B | FAM216A activity raises TFB1M's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.29× lower at baseline in the lines without FAM216A | 0.020 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[FAM216A]] | B | FAM216A activity strengthens TFB1M's drug response | lines that do not express FAM216A (7) vs lines expressing it (40) | the lines without FAM216A respond 0.66× as strongly (z diff +2.14); strongest at Dinaciclib 0.05 µM: 1.08x vs 0.35x (z diff +7.1) | 0.045 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NAV2]] | B | NAV2 activity raises TFB1M's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without NAV2 | 0.054 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[NRN1]] | B | NRN1 activity raises TFB1M's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.22× lower at baseline in the lines without NRN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises TFB1M's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.00× lower at baseline in the lines without KDM2B-DT | 0.066 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[PPP4R4]] | B | PPP4R4 activity raises TFB1M's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without PPP4R4 | 0.073 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[HACE1]] | C | HACE1 activity raises TFB1M's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 3.23× lower at baseline in the lines without HACE1 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.2, -13.4); signed map (-38.9, 20.5). **Vector** length 121, 34.6% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.6 | +12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +10.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +3.3 | +3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +5.0 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | +2.7 | +2.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -19.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -18.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -23.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.9 | -14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -9.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.1 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -2.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor B1, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:155,256,134-155,314,493 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mtTFB, CGI-75 |
| Gene groups (HGNC) | 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 7 pathways, smallest: rRNA modification in the mitochondrion; rRNA processing in the mitochondrion; Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVM0](https://www.uniprot.org/uniprotkb/Q8WVM0) (Dimethyladenosine transferase 1, mitochondrial):

> Mitochondrial methyltransferase which uses S-adenosyl methionine to dimethylate two highly conserved adjacent adenosine residues (A1583 and A1584) within the loop of helix 45 at the 3-prime end of 12S rRNA, thereby regulating the assembly or stability of the small subunit of the mitochondrial ribosome. Also required for basal transcription of mitochondrial DNA, probably via its interaction with POLRMT and TFAM. Stimulates transcription independently of the methyltransferase activity.

**Summary**, from NCBI Gene [51106](https://www.ncbi.nlm.nih.gov/gene/51106):

> The protein encoded by this gene is a dimethyltransferase that methylates the conserved stem loop of mitochondrial 12S rRNA. The encoded protein also is part of the basal mitochondrial transcription complex and is necessary for mitochondrial gene expression. The methylation and transcriptional activities of this protein are independent of one another. Variations in this gene may influence the severity of aminoglycoside-induced deafness (AID).[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:17037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17037) · Entrez [51106](https://www.ncbi.nlm.nih.gov/gene/51106) · UniProt [Q8WVM0](https://www.uniprot.org/uniprotkb/Q8WVM0) · Ensembl [ENSG00000029639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000029639)

## Data

Gene col 392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 392); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 392]; `tensor/DDL_lfc|DDL_z.npy` [392]; `embed/gene_vectors.npy` [392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 392 or target_col == 392). Every well: [[TFB1M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFB1M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
