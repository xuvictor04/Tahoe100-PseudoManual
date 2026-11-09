---
symbol: "HIRA"
type: "gene"
col: 1862
ensembl_id: "ENSG00000100084"
name: "histone cell cycle regulator"
location: "22q11.21"
module: 36
arm: "+"
pooled_cpm: 97.49
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# HIRA

*histone cell cycle regulator* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.73× (z +15.4, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.88× (z +8.4, q 3e-15, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.428× (z -23.8, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.736× (z -12.0, q 6e-31, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYW1]] (+0.75, fdr 7e-06), [[FOXK2]] (+0.74, fdr 7e-06), [[TRAPPC10]] (+0.73, fdr 7e-06); moves opposite to [[DZIP3]] (-0.64, fdr 1e-05), [[SDCBP]] (-0.62, fdr 1e-05), [[NDUFA5]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.73×** | +15.4 | 0e+00 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.63×** | +13.6 | 7e-40 | 43/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.53×** | +11.9 | 2e-30 | 42/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +9.3 | 1e-18 | 39/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +8.4 | 3e-15 | 36/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +7.9 | 3e-13 | 32/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +7.8 | 3e-13 | 35/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +7.8 | 3e-13 | 32/48 (H4, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +7.8 | 5e-13 | 33/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +7.5 | 3e-12 | 29/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +7.5 | 3e-12 | 38/48 (NCI-H460, HCT15, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.19× | +7.0 | 1e-10 | 20/49 (NCI-H460, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +6.9 | 2e-10 | 26/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +6.3 | 1e-08 | 30/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **1.23×** | +5.7 | 5e-07 | 27/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.5 | 3e-04 | 19/48 (HOP62, C32, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +4.5 | 3e-04 | 23/48 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.006 | 14/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.009 | 12/49 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.072 | 4/48 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.094 | 6/49 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.428×** | -23.8 | 0e+00 | 45/49 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.416×** | -23.7 | 0e+00 | 42/44 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.736×** | -12.0 | 6e-31 | 41/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.664×** | -10.6 | 3e-24 | 29/45 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.801×** | -8.7 | 3e-16 | 27/48 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -8.7 | 3e-16 | 40/49 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.809×** | -8.4 | 5e-15 | 22/48 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.767×** | -7.2 | 6e-11 | 29/48 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.821×** | -5.5 | 2e-06 | 25/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.816×** | -5.5 | 2e-06 | 23/48 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.830×** | -5.2 | 9e-06 | 22/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.845× | -4.7 | 1e-04 | 16/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.7 | 1e-04 | 19/48 (RPMI-7951, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.848× | -4.6 | 1e-04 | 16/48 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.786×** | -3.8 | 0.004 | 14/48 (LoVo, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.863× | -3.8 | 0.004 | 19/47 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.036 | 14/48 (hTERT-HPNE, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.887× | -3.2 | 0.036 | 6/49 (SW 900, A549, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.897× | -3.1 | 0.062 | 11/48 (C32, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 110 | 7 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -15.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 128 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -18.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 144 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -14.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 109 | 4 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -12.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 152 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.648× (z -8.5) |
| [[A-172 (line)]] | wt | 60.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 70.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -11.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 63.1 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +12.3) | — |
| [[SW1417 (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -14.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -14.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -16.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 55.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 99.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -12.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 97.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -15.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[hTERT-HPNE (line)]] | wt | 91.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 76.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 87.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.02× (z +8.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.153× (z -22.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 82.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.649× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 78.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.13× (z +10.4) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 99.4 | 2 | 1 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 3.66× (z +12.4) | [[Atazanavir (sulfate) (drug)]] 5 µM 0.223× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 158 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -16.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -19.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0690× (z -29.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 85.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 74.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -30.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 59.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.33× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.0520× (z -29.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 86.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.0901× (z -20.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 95.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 87.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 78.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -13.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 95.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.572× (z -8.5) |
| [[SW48 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -14.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 99.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -14.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 83.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 94.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 79.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0984× (z -9.6) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 92.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW1]] | +0.75 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.74 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.70 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[ZMYND19]] | +0.68 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[EMC8]] | +0.68 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[DGCR8]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[LIN52]] | +0.66 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[VKORC1L1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SCLY]] | +0.65 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[NFATC3]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DEXI]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZIP3]] | -0.64 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[SDCBP]] | -0.62 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[FAM200B]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[BROX]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[CLN5]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SEPSECS]] | -0.58 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[CGGBP1]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[NOTCH2NLC]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SF3B1]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.825). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-11.8, -17.3); signed map (-46.4, -21.3). **Vector** length 125, 38.8% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.5 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.2 | +13.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -11.8 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -11.0 | -12.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -10.0 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.9 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.8 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Ixazomib (drug)]] 5 µM |  | -2.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | histone cell cycle regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,330,698-19,447,450 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DGCR1, TUP1; previously TUPLE1 |
| Gene groups (HGNC) | WD repeat domain containing; HIRA histone chaperone complex subunits |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 7 pathways, smallest: Replacement of protamines by nucleosomes in the male pronucleus; Formation of Senescence-Associated Heterochromatin Foci (SAHF); DNA Damage/Telomere Stress Induced Senescence |
| Matched by | ensembl_id |

**Function**, from UniProt [P54198](https://www.uniprot.org/uniprotkb/P54198) (Protein HIRA):

> Cooperates with ASF1A to promote replication-independent chromatin assembly. Required for the periodic repression of histone gene transcription during the cell cycle. Required for the formation of senescence-associated heterochromatin foci (SAHF) and efficient senescence-associated cell cycle exit.

**Summary**, from NCBI Gene [7290](https://www.ncbi.nlm.nih.gov/gene/7290):

> This gene encodes a histone chaperone that preferentially places the variant histone H3.3 in nucleosomes. Orthologs of this gene in yeast, flies, and plants are necessary for the formation of transcriptionally silent heterochomatin. This gene plays an important role in the formation of the senescence-associated heterochromatin foci. These foci likely mediate the irreversible cell cycle changes that occur in senescent cells. It is considered the primary candidate gene in some haploinsufficiency …

**Accessions** — [HGNC:4916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4916) · Entrez [7290](https://www.ncbi.nlm.nih.gov/gene/7290) · UniProt [P54198](https://www.uniprot.org/uniprotkb/P54198) · Ensembl [ENSG00000100084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100084)

## Data

Gene col 1862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1862); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1862]; `tensor/DDL_lfc|DDL_z.npy` [1862]; `embed/gene_vectors.npy` [1862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1862 or target_col == 1862). Every well: [[HIRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
