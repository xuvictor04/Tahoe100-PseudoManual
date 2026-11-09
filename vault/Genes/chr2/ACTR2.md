---
symbol: "ACTR2"
type: "gene"
col: 6117
ensembl_id: "ENSG00000138071"
name: "actin related protein 2"
location: "2p14"
module: 24
arm: "-"
pooled_cpm: 299.28
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ACTR2

*actin related protein 2* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +25.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 3.60×, A549 3.84×, PANC-1 3.15×, SNU-423 4.52×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 3.55×, A549 3.80×, PANC-1 3.25×, SNU-423 4.73×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.769× (z -6.7, q 1e-08, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAP29]] (+0.63, fdr 7e-06), [[BZW1]] (+0.62, fdr 1e-05), [[DR1]] (+0.61, fdr 1e-05); moves opposite to [[EPB41L4A-AS1]] (-0.69, fdr 7e-06), [[PCGF1]] (-0.63, fdr 2e-05, ⚠ PCGF1 in the vector space only through flagged drug-doses), [[NSUN5P1-1]] (-0.61, fdr 1e-05), [[SNHG7]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIK3CB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6117.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 3.60×, A549 3.84×, PANC-1 3.15×, SNU-423 4.52×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 3.55×, A549 3.80×, PANC-1 3.25×, SNU-423 4.73×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +25.8 | 0e+00 | 49/49 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +24.9 | 0e+00 | 44/44 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +17.1 | 0e+00 | 43/45 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +6.9 | 1e-09 | 31/48 (KATO III, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.27×** | +6.0 | 2e-07 | 31/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.24×** | +5.5 | 3e-06 | 27/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.23×** | +5.0 | 4e-05 | 27/50 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.21×** | +4.9 | 9e-05 | 24/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.9 | 0.006 | 17/47 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.15× | +3.7 | 0.015 | 11/48 (SNU-423, C32, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.15× | +3.3 | 0.042 | 11/48 (CFPAC-1, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | 1.14× | +3.2 | 0.056 | 15/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 5 µM |  | 1.09× | +3.2 | 0.066 | 0/48 | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.14× | +3.1 | 0.071 | 14/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.769×** | -6.7 | 1e-08 | 33/48 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -5.3 | 3e-05 | 23/48 (J82, NCI-H2347, …) | top dose only | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.838× | -4.3 | 0.003 | 22/49 (A-427, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -4.1 | 0.005 | 20/48 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.861× | -3.8 | 0.017 | 18/48 (LOX-IMVI, J82, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.7 | 0.023 | 19/48 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.060 | 22/49 (C-33 A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.912× | -3.3 | 0.062 | 1/49 (HOP62) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.863× | -3.3 | 0.062 | 14/50 (NCI-H23, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.880× | -3.2 | 0.069 | 17/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.098 | 18/48 (COLO 205, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.886× | -3.1 | 0.098 | 8/47 (SW 1271, LS 180, …) | top dose only | position effect removed |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.846× | -3.0 | 0.099 | 17/48 (A-172, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.797×** | -3.0 | 0.099 | 17/50 (NCI-H23, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.888× | -3.0 | 0.099 | 9/48 (KATO III, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.798×** | -3.0 | 0.099 | 21/48 (RKO, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 506 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +18.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.531× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 332 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +19.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 299 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +17.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 380 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.85× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.492× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 209 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +15.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.250× (z -11.5) |
| [[SNU-423 (line)]] | alt | 187 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +21.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 357 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +18.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 493 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 262 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +19.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 315 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +13.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.534× (z -9.3) |
| [[J82 (line)]] | alt | 259 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.62× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 191 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.51× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 399 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +22.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 349 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +25.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 336 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +25.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 237 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +11.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 255 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +15.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 224 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +18.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 221 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +17.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 260 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +18.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 237 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +15.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 275 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +14.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 309 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +14.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 248 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +20.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 287 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +14.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 371 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +20.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 392 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +15.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 259 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +20.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 316 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +17.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 214 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +14.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 268 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +17.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 275 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 318 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +20.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 191 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 258 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 232 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +18.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 296 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 495 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +13.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 313 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +18.9) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.230× (z -13.0) |
| [[SHP-77 (line)]] | alt | 207 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 207 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +13.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 270 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +12.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 355 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP29]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[BZW1]] | +0.62 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[DR1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ARPC5]] | +0.59 | +0.57 / +0.62 | both halves | 8e-06 | same gene group; pathway: Clathrin-mediated endocytosis; STRING 999 |
| [[AKIRIN1]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CMTM6]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LAMC1]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CHRAC1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RO60]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SCYL2]] | +0.56 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | -0.69 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | -0.63 | -0.46 / -0.61 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P1-1]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.61 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[SNHG15]] | -0.61 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SNHG12]] | -0.58 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[NELFA]] | -0.57 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[NOP53]] | -0.57 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ZFAS1]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[RAB24]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[EGFL8]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[SNHG1]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ENKD1]] | -0.55 | -0.40 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CB]] | B | PIK3CB activity raises ACTR2's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.5, -14.5); signed map (-6.3, 38.1). **Vector** length 126, 42.7% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.8 | +5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.3 | +6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.4 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.6 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.3 | +1.7 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.9 | +2.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.7 | +2.0 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -6.5 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.9 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.9 | -3.2 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | -4.1 | -0.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -4.0 | -0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -4.0 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.0 | -1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:65,227,788-65,271,253 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARP2 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits; Actin related proteins |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 20 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P61160](https://www.uniprot.org/uniprotkb/P61160) (Actin-related protein 2):

> ATP-binding component of the Arp2/3 complex, a multiprotein complex that mediates actin polymerization upon stimulation by nucleation-promoting factor (NPF). The Arp2/3 complex mediates the formation of branched actin networks in the cytoplasm, providing the force for cell motility. Seems to contact the pointed end of the daughter actin filament. In podocytes, required for the formation of lamellipodia downstream of AVIL and PLCE1 regulation. In addition to its role in the cytoplasmic …

**Summary**, from NCBI Gene [10097](https://www.ncbi.nlm.nih.gov/gene/10097):

> The specific function of this gene has not yet been determined; however, the protein it encodes is known to be a major constituent of the ARP2/3 complex. This complex is located at the cell surface and is essential to cell shape and motility through lamellipodial actin assembly and protrusion. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:169) · Entrez [10097](https://www.ncbi.nlm.nih.gov/gene/10097) · UniProt [P61160](https://www.uniprot.org/uniprotkb/P61160) · Ensembl [ENSG00000138071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138071)

## Data

Gene col 6117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6117); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6117]; `tensor/DDL_lfc|DDL_z.npy` [6117]; `embed/gene_vectors.npy` [6117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6117 or target_col == 6117). Every well: [[ACTR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
