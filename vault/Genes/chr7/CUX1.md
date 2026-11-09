---
symbol: "CUX1"
type: "gene"
col: 15074
ensembl_id: "ENSG00000257923"
name: "cut like homeobox 1"
location: "7q22.1"
module: 168
arm: "-"
pooled_cpm: 356.86
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# CUX1

*cut like homeobox 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.27× (z +8.3, q 8e-14, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.288× (z -30.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF12]] (+0.66, fdr 7e-06), [[NFE2L2]] (+0.65, fdr 1e-05), [[ASXL2]] (+0.64, fdr 7e-06); moves opposite to [[PMS2P3-1]] (-0.68, fdr 7e-06), [[SDHAP4]] (-0.67, fdr 1e-05), [[C1orf52]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +8.3 | 8e-14 | 25/48 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +7.1 | 3e-10 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +5.4 | 1e-05 | 27/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.9 | 1e-04 | 25/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +4.2 | 0.003 | 22/47 (HOP62, H4, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.005 | 28/50 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.22×** | +3.9 | 0.007 | 22/50 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.8 | 0.009 | 15/48 (RPMI-7951, PANC-1, …) | two highest doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.011 | 10/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.7 | 0.011 | 5/48 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.031 | 15/47 (SW480, C32, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.031 | 19/48 (RPMI-7951, HEC-1-A, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.031 | 10/49 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.10× | +3.4 | 0.031 | 2/48 (NCI-H2347, CHP-212) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.036 | 25/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.038 | 6/48 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.052 | 21/48 (HOP62, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.054 | 4/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.288×** | -30.2 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.312×** | -28.3 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.366×** | -24.4 | 0e+00 | 48/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.525×** | -15.0 | 0e+00 | 44/47 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.663×** | -10.0 | 2e-21 | 45/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.662×** | -9.3 | 2e-18 | 35/45 (C32, SW48, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.688×** | -9.1 | 1e-17 | 32/49 (SK-MEL-2, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.687×** | -8.7 | 2e-16 | 32/44 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.699×** | -8.7 | 2e-16 | 44/48 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.718×** | -8.0 | 6e-14 | 39/48 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.795×** | -7.9 | 2e-13 | 29/48 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.611×** | -6.2 | 2e-08 | 43/48 (MIA PaCa-2, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -6.0 | 7e-08 | 28/48 (SW48, C-33 A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.635×** | -5.8 | 3e-07 | 43/49 (HT-29, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.645×** | -5.6 | 1e-06 | 29/38 (Panc 03.27, C32, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.798×** | -5.5 | 2e-06 | 33/49 (HOP62, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.661×** | -5.3 | 5e-06 | 29/49 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.845× | -4.1 | 0.001 | 22/48 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.750×** | -3.6 | 0.006 | 26/47 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.762×** | -3.4 | 0.013 | 26/48 (KATO III, A498, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.767×** | -3.4 | 0.015 | 21/48 (A-172, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 821 | 0 | 15 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -20.2) |
| [[HOP62 (line)]] | alt | 367 | 3 (1 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.250× (z -23.0) |
| [[RKO (line)]] | wt | 383 | 3 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -21.7) |
| [[SK-MEL-2 (line)]] | alt | 320 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -21.7) |
| [[A-172 (line)]] | wt | 483 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -22.3) |
| [[J82 (line)]] | alt | 352 | 0 | 10 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.413× (z -21.4) |
| [[NCI-H1792 (line)]] | alt | 406 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -25.1) |
| [[LOX-IMVI (line)]] | wt | 345 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 325 | 1 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.217× (z -29.0) |
| [[NCI-H460 (line)]] | wt | 443 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -27.5) |
| [[SW48 (line)]] | wt | 632 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -22.6) |
| [[SW480 (line)]] | alt | 356 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -30.8) |
| [[CFPAC-1 (line)]] | alt | 200 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.391× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 293 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -19.5) |
| [[HT-29 (line)]] | alt | 373 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.9) | [[Belinostat (drug)]] 5 µM 0.243× (z -25.4) |
| [[LoVo (line)]] | wt | 629 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -28.2) |
| [[NCI-H23 (line)]] | alt | 361 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -21.5) |
| [[SNU-1 (line)]] | wt | 363 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -21.6) |
| [[AsPC-1 (line)]] | alt | 282 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.264× (z -20.6) |
| [[C-33 A (line)]] | alt | 378 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -20.3) |
| [[HCT15 (line)]] | alt | 422 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 211 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -20.0) |
| [[KATO III (line)]] | alt | 503 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -20.2) |
| [[LS 180 (line)]] | wt | 410 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -21.8) |
| [[A-427 (line)]] | wt | 286 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -20.8) |
| [[A498 (line)]] | wt | 458 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -18.4) |
| [[A549 (line)]] | wt | 379 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -15.6) |
| [[BT-474 (line)]] | alt | 314 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -19.4) |
| [[CHP-212 (line)]] | wt | 402 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -12.3) |
| [[COLO 205 (line)]] | alt | 292 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.215× (z -19.2) |
| [[Hs 766T (line)]] | wt | 239 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -17.4) |
| [[NCI-H2030 (line)]] | alt | 388 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 209 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 236 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -17.3) |
| [[PANC-1 (line)]] | alt | 241 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -15.3) |
| [[SW 900 (line)]] | alt | 261 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -15.2) |
| [[AN3 CA (line)]] | alt | 422 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 402 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -21.8) |
| [[SHP-77 (line)]] | alt | 155 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.373× (z -14.4) |
| [[SNU-423 (line)]] | alt | 237 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -20.5) |
| [[SW1417 (line)]] | alt | 429 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -14.0) |
| [[H4 (line)]] | wt | 272 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -10.0) |
| [[HS-578T (line)]] | alt | 334 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 317 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -17.2) |
| [[RPMI-7951 (line)]] | alt | 236 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.413× (z -12.1) |
| [[NCI-H661 (line)]] | alt | 290 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -10.2) |
| [[NCI-H2122 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 209 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF12]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[NFE2L2]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ASXL2]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[BPTF]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ERCC6L2]] | +0.64 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TSC22D1]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[STAG1]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[FAM193A]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.61 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[ZFHX3]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | -0.68 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[SDHAP4]] | -0.67 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[C1orf52]] | -0.65 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[SHQ1]] | -0.65 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.64 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PMS2P3]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SNHG21]] | -0.63 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[DUSP11]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.63 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[MFSD9]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.62 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[POMGNT2]] | -0.62 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **-** arm (projection on the module's main direction -0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.8, -15.8); signed map (14.4, -11.0). **Vector** length 134, 50.4% of its response variance represented; |z| ≥ 3 in 1,738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +13.8 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +12.9 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +9.5 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.8 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.6 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.8 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.2 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.8 | -15.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.4 | -7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.3 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -24.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.4 | -5.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.4 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -5.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -3.1 | -1.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cut like homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,815,904-102,283,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDP, CDP1, CUX, CUT, Clox, CDP/Cut, CDP/Cux, Cux/CDP; previously CUTL1 |
| Gene groups (HGNC) | CUT class homeoboxes and pseudogenes; Golgins |
| Reactome | 9 pathways, smallest: Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [P39880](https://www.uniprot.org/uniprotkb/P39880) (Homeobox protein cut-like 1):

> Transcription factor involved in the control of neuronal differentiation in the brain. Regulates dendrite development and branching, and dendritic spine formation in cortical layers II-III. Also involved in the control of synaptogenesis. In addition, it has probably a broad role in mammalian development as a repressor of developmentally regulated gene expression. May act by preventing binding of positively-activing CCAAT factors to promoters. Component of nf-munr repressor; binds to the matrix …

**Summary**, from NCBI Gene [1523](https://www.ncbi.nlm.nih.gov/gene/1523):

> The protein encoded by this gene is a member of the homeodomain family of DNA binding proteins. It may regulate gene expression, morphogenesis, and differentiation and it may also play a role in the cell cycle progession. Several alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:2557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2557) · Entrez [1523](https://www.ncbi.nlm.nih.gov/gene/1523) · UniProt [P39880](https://www.uniprot.org/uniprotkb/P39880) · Ensembl [ENSG00000257923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257923)

## Data

Gene col 15074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15074); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15074]; `tensor/DDL_lfc|DDL_z.npy` [15074]; `embed/gene_vectors.npy` [15074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15074 or target_col == 15074). Every well: [[CUX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
