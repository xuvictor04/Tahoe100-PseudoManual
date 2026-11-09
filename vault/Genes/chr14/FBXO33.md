---
symbol: "FBXO33"
type: "gene"
col: 9110
ensembl_id: "ENSG00000165355"
name: "F-box protein 33"
location: "14q21.1"
module: 1
arm: "-"
pooled_cpm: 56.86
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FBXO33

*F-box protein 33* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.26× (z +19.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.376× (z -15.5, q 0e+00, down in 38 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.530× (z -5.5, q 6e-06, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD37]] (+0.70, fdr 7e-06), [[MOSPD3]] (+0.68, fdr 1e-05), [[INPP5K]] (+0.68, fdr 7e-06); moves opposite to [[DNAJC11]] (-0.76, fdr 7e-06), [[DPH5-DT]] (-0.69, fdr 1e-05), [[ANAPC7]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **3.26×** | +19.6 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.23×** | +19.4 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.71×** | +16.5 | 0e+00 | 48/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +11.6 | 1e-28 | 33/48 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +10.5 | 1e-23 | 47/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +9.6 | 5e-20 | 44/49 (SW48, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +8.7 | 3e-16 | 41/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +7.1 | 1e-10 | 33/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +6.1 | 5e-08 | 27/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +5.3 | 6e-06 | 28/49 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.4 | 6e-04 | 25/49 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +4.1 | 0.002 | 22/48 (NCI-H460, BT-474, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.22×** | +3.3 | 0.050 | 20/47 (NCI-H460, SW480, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.078 | 12/48 (NCI-H2347, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.1 | 0.078 | 12/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.078 | 15/48 (CFPAC-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.078 | 7/48 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.0 | 0.095 | 10/48 (C32, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -15.5 | 0e+00 | 38/41 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.430×** | -14.0 | 7e-42 | 47/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.532×** | -10.4 | 4e-23 | 38/49 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.530×** | -5.5 | 6e-06 | 32/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.539×** | -5.3 | 1e-05 | 35/48 (HCT15, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.552×** | -5.1 | 3e-05 | 30/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.562×** | -5.0 | 5e-05 | 29/48 (NCI-H2347, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.725×** | -4.9 | 7e-05 | 26/44 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.764×** | -4.3 | 0.001 | 24/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.0 | 0.004 | 2/49 (C-33 A, NCI-H2122) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.790×** | -3.7 | 0.010 | 26/47 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.802×** | -3.6 | 0.012 | 21/49 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.802×** | -3.6 | 0.012 | 19/48 (HOP62, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.668×** | -3.5 | 0.021 | 19/48 (SK-MEL-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.672×** | -3.4 | 0.022 | 17/46 (KATO III, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.024 | 18/49 (NCI-H1573, HT-29, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.045 | 14/48 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.769×** | -3.1 | 0.064 | 11/49 (LOX-IMVI, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.832×** | -3.0 | 0.074 | 15/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.836× | -2.9 | 0.084 | 9/49 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.9 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +16.2) | — |
| [[NCI-H2347 (line)]] | alt | 103 | 4 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -18.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 70.0 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.3 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 55.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.6) | — |
| [[RKO (line)]] | wt | 42.9 | 6 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 6.41× (z +14.0) | — |
| [[SK-MEL-2 (line)]] | alt | 53.3 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.5 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.15× (z +15.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.421× (z -9.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 58.7 | 2 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.83× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -19.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 81.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.93× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 90.2 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -16.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 53.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -12.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 43.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 48.6 | 4 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 5.01× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 75.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.34× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 50.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 26.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +16.8) | — |
| [[SNU-423 (line)]] | alt | 55.5 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.06× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 56.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 52.5 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.36× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -10.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 122 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 20.2× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 23.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.41× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 44.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.74× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 48.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 115 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.06× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -15.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 99.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -13.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 76.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -12.6) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 57.3 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.99× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 51.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 34.7 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.79× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -18.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 47.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.09× (z +8.6) | — |
| [[A498 (line)]] | wt | 29.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 63.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.101× (z -11.2) |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0886× (z -13.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 40.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.19× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0650× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 72.2 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0779× (z -10.0) |
| [[AN3 CA (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD37]] | +0.70 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.68 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[INPP5K]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ORC4]] | +0.67 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ARL3]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.66 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RNASE4]] | +0.66 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[MXI1]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ANG]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[FAM117B]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.76 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[DPH5-DT]] | -0.69 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.68 | -0.74 / -0.58 | both halves | 7e-06 |  |
| [[UTP20]] | -0.68 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.67 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.66 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[DHX37]] | -0.66 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[ATXN10]] | -0.65 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.64 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ITPA]] | -0.63 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[MTHFSD]] | -0.63 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises FBXO33's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without NR3C2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[KLHL32]] | B | KLHL32 activity raises FBXO33's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without KLHL32 | 0.036 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[NR4A2]] | B | NR4A2 activity raises FBXO33's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without NR4A2 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LGALS1]] | B | LGALS1 activity lowers FBXO33's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 1.26× higher at baseline in the lines without LGALS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[DLL3]] | B | DLL3 activity lowers FBXO33's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.04× higher at baseline in the lines without DLL3 | 0.084 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[EPHB3]] | B | EPHB3 activity raises FBXO33's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without EPHB3 | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[FBXL20]] | C | FBXL20's natural level strengthens FBXO33's drug response | FBXL20's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.11; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (5.9, -11.9); signed map (-25.0, 15.6). **Vector** length 116, 37.6% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.7 | +19.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.6 | +8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +16.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +19.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.4 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.4 | -14.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.4 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.6 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -6.3 | -3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.1 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:39,397,684-39,432,466 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fbx33 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6M2](https://www.uniprot.org/uniprotkb/Q7Z6M2) (F-box only protein 33):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Probably recognizes and binds to phosphorylated target proteins. Recognizes YBX1 (By similarity).

**Summary**, from NCBI Gene [254170](https://www.ncbi.nlm.nih.gov/gene/254170):

> This locus represents an member of the F-box gene family. The encoded protein contains an F-box motif and a domain that might form a structure similar to a leucine-rich repeat found in placental RNAse inhibitor. This locus may be associated with copy number variation of UGT2B17 (GeneID 7367), which has been associated with susceptibility to osteoporosis.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:19833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19833) · Entrez [254170](https://www.ncbi.nlm.nih.gov/gene/254170) · UniProt [Q7Z6M2](https://www.uniprot.org/uniprotkb/Q7Z6M2) · Ensembl [ENSG00000165355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165355)

## Data

Gene col 9110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9110); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9110]; `tensor/DDL_lfc|DDL_z.npy` [9110]; `embed/gene_vectors.npy` [9110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9110 or target_col == 9110). Every well: [[FBXO33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
