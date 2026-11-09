---
symbol: "BMPR2"
type: "gene"
col: 12830
ensembl_id: "ENSG00000204217"
name: "bone morphogenetic protein receptor type 2"
location: "2q33.1-q33.2"
module: 231
arm: "+"
pooled_cpm: 282.23
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/231"]
generated_by: "tahoemap"
---

# BMPR2

*bone morphogenetic protein receptor type 2* — 2q33.1-q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +14.7, q 0e+00, up in 33 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.671× (z -11.9, q 1e-29, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASEK]] (+0.58, fdr 3e-05), [[NCOA1]] (+0.57, fdr 1e-05), [[RC3H1]] (+0.57, fdr 2e-05); moves opposite to [[TAF1A]] (-0.61, fdr 1e-05), [[NLE1]] (-0.60, fdr 1e-05), [[MIER2]] (-0.58, fdr 3e-05).
> It is in [[Module 231]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +14.7 | 0e+00 | 33/49 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +9.7 | 9e-20 | 36/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.6 | 9e-09 | 28/50 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +6.0 | 4e-07 | 25/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +5.5 | 5e-06 | 10/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +5.4 | 5e-06 | 13/48 (A498, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +5.2 | 1e-05 | 24/48 (SW480, KATO III, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 35/50 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +5.2 | 2e-05 | 14/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.18× | +5.0 | 4e-05 | 21/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.18× | +4.7 | 1e-04 | 22/50 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 31/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +4.6 | 2e-04 | 16/47 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +4.4 | 5e-04 | 8/48 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +4.3 | 7e-04 | 18/47 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.002 | 27/48 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.13× | +3.7 | 0.006 | 9/49 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.6 | 0.011 | 13/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -11.9 | 1e-29 | 33/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -8.6 | 2e-15 | 28/48 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.719×** | -8.5 | 4e-15 | 34/48 (AsPC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.744×** | -8.1 | 5e-14 | 30/45 (C32, Panc 03.27, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.753×** | -8.1 | 6e-14 | 31/47 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -8.1 | 6e-14 | 34/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -7.9 | 3e-13 | 25/48 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.631×** | -7.2 | 6e-11 | 34/47 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.792×** | -6.9 | 2e-10 | 29/49 (C32, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.794×** | -6.9 | 4e-10 | 30/48 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.794×** | -6.8 | 4e-10 | 33/48 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.796×** | -6.5 | 3e-09 | 23/44 (Panc 03.27, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.809×** | -6.3 | 1e-08 | 28/48 (C32, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.811×** | -6.2 | 2e-08 | 26/49 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -6.2 | 3e-08 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.675×** | -6.1 | 3e-08 | 29/49 (HOP62, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -4.8 | 5e-05 | 32/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.750×** | -4.5 | 2e-04 | 26/48 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.750×** | -4.5 | 2e-04 | 30/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.878× | -3.9 | 0.003 | 15/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.917× | -3.7 | 0.006 | 11/49 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.884× | -3.7 | 0.006 | 9/49 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.851× | -3.4 | 0.013 | 19/48 (Hs 766T, LOX-IMVI, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 326 | 2 | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.413× (z -16.6) |
| [[SW1417 (line)]] | alt | 369 | 2 (1 ⚠) | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +14.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.457× (z -14.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.636× (z -9.0) |
| [[C32 (line)]] | wt | 439 | 1 | 9 (8 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.466× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.618× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 284 | 1 | 8 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +19.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -19.8) |
| [[HOP62 (line)]] | alt | 344 | 0 | 8 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.454× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 215 | 6 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +21.5) | [[Homoharringtonine (drug)]] 0.05 µM 0.564× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 330 | 2 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.545× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 483 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -17.6) |
| [[RKO (line)]] | wt | 209 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +17.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -14.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 390 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.471× (z -11.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.529× (z -10.2) |
| [[HT-29 (line)]] | alt | 244 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.500× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[LoVo (line)]] | wt | 199 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +23.8) | — |
| [[LS 180 (line)]] | wt | 189 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +20.6) | — |
| [[A498 (line)]] | wt | 194 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +21.0) | — |
| [[A549 (line)]] | wt | 298 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -14.9) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -12.6) |
| [[KATO III (line)]] | alt | 174 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 266 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.489× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.567× (z -9.6) |
| [[SW480 (line)]] | alt | 238 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +16.6) | — |
| [[COLO 205 (line)]] | alt | 235 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.3) | [[Ixazomib citrate (drug)]] 5 µM 0.413× (z -10.1) |
| [[J82 (line)]] | alt | 321 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -16.4) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.490× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 313 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.481× (z -13.2) |
| [[PANC-1 (line)]] | alt | 282 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +15.7) | — |
| [[SNU-1 (line)]] | wt | 263 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-172 (line)]] | wt | 395 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -20.3) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -16.7) |
| [[AN3 CA (line)]] | alt | 394 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[BT-474 (line)]] | alt | 261 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -14.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HCT15 (line)]] | alt | 178 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.7) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 287 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.617× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Hs 766T (line)]] | wt | 225 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +15.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.588× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 249 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 213 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +13.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.546× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 311 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -14.7) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.525× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 304 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +12.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 249 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -9.6) ⚠ toxic |
| [[SW48 (line)]] | wt | 196 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 344 | 1 | 0 | [[Rapamycin (drug)]] 5 µM 1.58× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 383 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H661 (line)]] | alt | 902 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 368 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -9.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 365 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SNU-423 (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -14.3) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 330 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 501 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 261 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 395 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASEK]] | +0.58 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[NCOA1]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RC3H1]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[VAMP8]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ARID4B]] | +0.55 | +0.39 / +0.63 | both halves | 5e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[LRRC57]] | +0.54 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[PPM1B]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[NCOA2]] | +0.54 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[TMEM50A]] | +0.54 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[KIAA2026]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SUMO2]] | +0.53 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[ARID1B]] | +0.53 | +0.39 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF1A]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[NLE1]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MIER2]] | -0.58 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[POLR3A]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PRMT5]] | -0.55 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[AP4B1]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[RABGGTB]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[FAM222A-AS1]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DNAJA3]] | -0.52 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[B3GNTL1]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ZNF202]] | -0.52 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[BCAN-AS2]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BMPR2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 231]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.4, -44.7); signed map (-9.8, 9.7). **Vector** length 146, 51.1% of its response variance represented; |z| ≥ 3 in 1,666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +12.3 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.3 | +14.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +8.0 | +6.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.4 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.9 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.2 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.5 | -8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.4 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -8.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.6 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein receptor type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1-q33.2 — chr2:202,376,327-202,567,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRK-3, T-ALK, BMPR3, BMPR-II; previously PPH1 |
| Gene groups (HGNC) | Type 2 receptor serine/threonine kinases; BMP receptors |
| Hallmark sets | TGF_BETA_SIGNALING, IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: Signaling by BMP; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13873](https://www.uniprot.org/uniprotkb/Q13873) (Bone morphogenetic protein receptor type-2):

> On ligand binding, forms a receptor complex consisting of two type II and two type I transmembrane serine/threonine kinases. Type II receptors phosphorylate and activate type I receptors which autophosphorylate, then bind and activate SMAD transcriptional regulators. Can also mediate signaling through the activation of the p38MAPK cascade. Binds to BMP7, BMP2 and, less efficiently, BMP4. Binding is weak but enhanced by the presence of type I receptors for BMPs. Mediates induction of …

**Summary**, from NCBI Gene [659](https://www.ncbi.nlm.nih.gov/gene/659):

> This gene encodes a member of the bone morphogenetic protein (BMP) receptor family of transmembrane serine/threonine kinases. The ligands of this receptor are members of the TGF-beta superfamily. BMPs are involved in endochondral bone formation and embryogenesis. These proteins transduce their signals through the formation of heteromeric complexes of two different types of serine (threonine) kinase receptors: type I receptors of about 50-55 kD and type II receptors of about 70-80 kD. Mutations …

**Accessions** — [HGNC:1078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1078) · Entrez [659](https://www.ncbi.nlm.nih.gov/gene/659) · UniProt [Q13873](https://www.uniprot.org/uniprotkb/Q13873) · Ensembl [ENSG00000204217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204217)

## Data

Gene col 12830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12830); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12830]; `tensor/DDL_lfc|DDL_z.npy` [12830]; `embed/gene_vectors.npy` [12830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12830 or target_col == 12830). Every well: [[BMPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
