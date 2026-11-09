---
symbol: "TAOK1"
type: "gene"
col: 8355
ensembl_id: "ENSG00000160551"
name: "TAO kinase 1"
location: "17q11.2"
module: 194
arm: "+"
pooled_cpm: 312.05
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# TAOK1

*TAO kinase 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.59× (z +5.4, q 5e-05, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.403× (z -21.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPSF2]] (+0.61, fdr 7e-05), [[NSD1]] (+0.58, fdr 3e-05), [[CEP350]] (+0.58, fdr 1e-05); moves opposite to [[SHF]] (-0.57, fdr 2e-05), [[FAM118A]] (-0.55, fdr 1e-04), [[FCHO1]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 194]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +5.4 | 5e-05 | 32/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +5.1 | 1e-04 | 27/48 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +5.0 | 1e-04 | 28/48 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.16× | +4.9 | 1e-04 | 21/48 (PANC-1, KATO III, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.7 | 3e-04 | 27/48 (A498, RKO, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.18× | +4.0 | 0.007 | 21/48 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.049 | 15/48 (AsPC-1, C-33 A, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.052 | 29/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.3 | 0.052 | 14/48 (CFPAC-1, A498, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.052 | 8/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.057 | 13/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.057 | 1/48 (HCT15) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.075 | 16/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -21.5 | 0e+00 | 48/48 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.441×** | -19.4 | 0e+00 | 47/48 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.456×** | -18.6 | 0e+00 | 47/48 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -13.6 | 7e-40 | 39/44 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.578×** | -12.5 | 8e-34 | 46/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -11.1 | 8e-27 | 42/45 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.630×** | -10.9 | 5e-26 | 42/49 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.649×** | -10.2 | 9e-23 | 46/48 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -9.3 | 1e-18 | 37/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -7.6 | 1e-12 | 35/48 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.729×** | -7.5 | 4e-12 | 43/48 (HT-29, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -5.3 | 5e-06 | 33/49 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.636×** | -5.2 | 1e-05 | 22/38 (HS-578T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.809×** | -5.0 | 2e-05 | 31/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.813×** | -4.7 | 9e-05 | 25/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.002 | 33/49 (HepG2/C3A, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.765×** | -3.7 | 0.008 | 36/48 (HT-29, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.859× | -3.6 | 0.009 | 13/48 (BT-474, HepG2/C3A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.025 | 27/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.787×** | -3.3 | 0.027 | 26/48 (J82, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.912× | -3.1 | 0.049 | 5/48 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.884× | -2.9 | 0.077 | 6/47 (C-33 A, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 428 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.377× (z -19.9) |
| [[LOX-IMVI (line)]] | wt | 456 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -20.2) |
| [[HOP62 (line)]] | alt | 381 | 1 | 9 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.70× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -18.6) |
| [[PANC-1 (line)]] | alt | 371 | 3 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +16.4) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.57× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -15.1) |
| [[J82 (line)]] | alt | 344 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -15.9) |
| [[SK-MEL-2 (line)]] | alt | 273 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -14.7) |
| [[A549 (line)]] | wt | 439 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -20.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.364× (z -16.7) |
| [[C32 (line)]] | wt | 300 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -15.8) |
| [[HS-578T (line)]] | alt | 289 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 354 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.412× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 231 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.4) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.366× (z -14.8) |
| [[HT-29 (line)]] | alt | 245 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.9) ⚠ cell-cycle shift, explains ~12% of this change | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 417 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.297× (z -18.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 321 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.278× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 326 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.349× (z -17.2) |
| [[A-427 (line)]] | wt | 328 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.570× (z -9.6) |
| [[A498 (line)]] | wt | 296 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.518× (z -12.1) |
| [[BT-474 (line)]] | alt | 313 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -17.1) |
| [[LS 180 (line)]] | wt | 235 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 405 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.452× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 239 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -16.1) |
| [[hTERT-HPNE (line)]] | wt | 287 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.403× (z -13.0) |
| [[KATO III (line)]] | alt | 249 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.4) ⚠ cell-cycle shift, explains ~12% of this change | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -10.9) |
| [[LoVo (line)]] | wt | 228 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.421× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 284 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 378 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -19.7) |
| [[SW 900 (line)]] | alt | 253 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.367× (z -15.1) |
| [[SW1417 (line)]] | alt | 265 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -16.0) |
| [[SW480 (line)]] | alt | 248 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 3.40× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -17.6) |
| [[A-172 (line)]] | wt | 512 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.455× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 212 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.506× (z -10.1) |
| [[COLO 205 (line)]] | alt | 238 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.54× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -11.3) |
| [[HCT15 (line)]] | alt | 336 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.528× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 174 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.462× (z -11.5) |
| [[RKO (line)]] | wt | 326 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.421× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 255 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.444× (z -11.6) |
| [[SNU-1 (line)]] | wt | 322 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.503× (z -9.9) |
| [[C-33 A (line)]] | alt | 393 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -8.5) |
| [[Hs 766T (line)]] | wt | 216 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -12.9) |
| [[SHP-77 (line)]] | alt | 195 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.522× (z -9.6) |
| [[SNU-423 (line)]] | alt | 333 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.441× (z -12.1) |
| [[SW48 (line)]] | wt | 278 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -13.1) |
| [[CHP-212 (line)]] | wt | 298 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -11.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.385× (z -9.0) |
| [[H4 (line)]] | wt | 267 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -11.2) |
| [[AN3 CA (line)]] | alt | 302 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.415× (z -8.9) |
| [[NCI-H2122 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 423 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | +0.61 | +0.38 / +0.67 | both halves | 7e-05 | pathway: Dengue Virus-Host Interactions; STRING 436 |
| [[NSD1]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CEP350]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DARS1]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[LZIC]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[KRCC1]] | +0.57 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[TRIP11]] | +0.55 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[MCTS1]] | +0.55 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[CLOCK]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TRMT1L]] | +0.55 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CREBBP]] | +0.55 | +0.33 / +0.62 | both halves | 1e-04 |  |
| [[UBE3B]] | +0.55 | +0.36 / +0.52 | both halves | 9e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHF]] | -0.57 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[FAM118A]] | -0.55 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[FCHO1]] | -0.52 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[SHQ1]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PNKD]] | -0.50 | -0.34 / -0.47 | both halves | 1e-04 | same gene group |
| [[FCHSD1]] | -0.50 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[LPCAT4]] | -0.50 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[TMEM243]] | -0.50 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[SLC45A4]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[OSBPL7]] | -0.50 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[MCOLN2]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[RASAL1]] | -0.50 | -0.26 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-24.4, 7.5); signed map (12.1, -25.0). **Vector** length 117, 46.6% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.6 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.4 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.7 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +5.7 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.5 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.1 | -12.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.8 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -11.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.2 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -7.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | TAO kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,390,363-29,551,903 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1361, MARKK, PSK2, MAP3K16, FLJ14314, TAO1, hTAOK1, hKFC-B |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; MicroRNA protein coding host genes; TAO kinase family |
| Reactome | 21 pathways, smallest: Dengue virus modulates apoptosis; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L7X3](https://www.uniprot.org/uniprotkb/Q7L7X3) (Serine/threonine-protein kinase TAO1):

> Serine/threonine-protein kinase involved in various processes such as p38/MAPK14 stress-activated MAPK cascade, DNA damage response and regulation of cytoskeleton stability. Phosphorylates MAP2K3, MAP2K6 and MARK2. Acts as an activator of the p38/MAPK14 stress-activated MAPK cascade by mediating phosphorylation and subsequent activation of the upstream MAP2K3 and MAP2K6 kinases. Involved in G protein-coupled receptor signaling to p38/MAPK14. In response to DNA damage, involved in the G2/M …

**Summary**, from NCBI Gene [57551](https://www.ncbi.nlm.nih.gov/gene/57551):

> Enables alpha-tubulin binding activity; beta-tubulin binding activity; and kinase activity. Involved in several processes, including mitotic G2 DNA damage checkpoint signaling; negative regulation of microtubule depolymerization; and positive regulation of MAPK cascade. Located in cytosol; microtubule cytoskeleton; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29259) · Entrez [57551](https://www.ncbi.nlm.nih.gov/gene/57551) · UniProt [Q7L7X3](https://www.uniprot.org/uniprotkb/Q7L7X3) · Ensembl [ENSG00000160551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160551)

## Data

Gene col 8355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8355); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8355]; `tensor/DDL_lfc|DDL_z.npy` [8355]; `embed/gene_vectors.npy` [8355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8355 or target_col == 8355). Every well: [[TAOK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAOK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
