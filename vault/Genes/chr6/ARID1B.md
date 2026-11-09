---
symbol: "ARID1B"
type: "gene"
col: 553
ensembl_id: "ENSG00000049618"
name: "AT-rich interaction domain 1B"
location: "6q25.3"
module: 137
arm: "+"
pooled_cpm: 278.2
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 29
n_dd_up_clean: 9
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# ARID1B

*AT-rich interaction domain 1B* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +7.2, q 2e-10, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.161× (z -39.4, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL17]] (+0.76, fdr 7e-06), [[NCOA2]] (+0.73, fdr 7e-06), [[CREBBP]] (+0.72, fdr 7e-06); moves opposite to [[GIPR]] (-0.64, fdr 1e-05), [[SEC22B]] (-0.62, fdr 1e-05), [[FCHO1]] (-0.61, fdr 6e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.2 | 2e-10 | 34/47 (LS 180, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.9 | 3e-04 | 30/46 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.27×** | +4.7 | 4e-04 | 31/49 (A-427, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.51×** | +4.7 | 4e-04 | 38/49 (A-427, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.003 | 24/47 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.012 | 21/47 (C32, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.7 | 0.014 | 11/47 (AsPC-1, C32, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.014 | 22/47 (C32, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.014 | 23/47 (C32, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.13× | +3.7 | 0.014 | 15/47 (A-427, LS 180, …) | top dose only | low cells (technical?) |
| [[XRK3F2 (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.015 | 33/47 (PANC-1, C-33 A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.017 | 22/47 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.019 | 13/47 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.038 | 19/47 (H4, A-172, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.2 | 0.052 | 19/47 (SK-MEL-2, COLO 205, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.056 | 22/47 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.056 | 9/47 (HOP62, A549, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +3.1 | 0.059 | 0/47 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.161×** | -39.4 | 0e+00 | 47/47 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.171×** | -38.1 | 0e+00 | 47/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.193×** | -35.5 | 0e+00 | 47/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.418×** | -18.8 | 0e+00 | 47/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.590×** | -16.0 | 0e+00 | 47/47 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.514×** | -13.8 | 3e-41 | 40/43 (C-33 A, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.517×** | -13.7 | 2e-40 | 45/46 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.534×** | -12.5 | 5e-34 | 39/44 (AN3 CA, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.569×** | -12.1 | 4e-32 | 44/47 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.580×** | -11.7 | 5e-30 | 48/48 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -10.3 | 3e-23 | 40/47 (C32, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.497×** | -10.1 | 3e-22 | 43/48 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.422×** | -9.7 | 1e-20 | 47/48 (HT-29, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.781×** | -7.5 | 3e-12 | 26/47 (C32, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.717×** | -7.1 | 3e-11 | 38/47 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -6.7 | 1e-09 | 39/47 (LOX-IMVI, SW48, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.656×** | -4.7 | 7e-05 | 41/47 (SW 900, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.779×** | -4.5 | 3e-04 | 31/47 (HT-29, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.822×** | -4.2 | 6e-04 | 25/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.688×** | -4.2 | 6e-04 | 35/47 (LOX-IMVI, HOP62, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 438 | 1 | 16 (8 ⚠) | [[PH-797804 (drug)]] 5 µM 3.15× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -35.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.176× (z -28.6) |
| [[LOX-IMVI (line)]] | wt | 389 | 0 | 15 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0842× (z -39.2) |
| [[NCI-H1573 (line)]] | alt | 255 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -28.8) |
| [[A-427 (line)]] | wt | 433 | 1 (1 ⚠) | 11 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.54× (z +9.4) ⚠ cell-cycle shift, explains ~76% of this change | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -32.6) |
| [[AN3 CA (line)]] | alt | 861 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -21.5) |
| [[HT-29 (line)]] | alt | 276 | 1 | 11 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -28.2) |
| [[NCI-H2030 (line)]] | alt | 443 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -30.8) |
| [[NCI-H460 (line)]] | wt | 199 | 2 (1 ⚠) | 10 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.171× (z -27.6) |
| [[SK-MEL-2 (line)]] | alt | 383 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -27.3) |
| [[HepG2_C3A (line)]] | wt | 388 | 1 (1 ⚠) | 10 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -30.7) |
| [[HOP62 (line)]] | alt | 189 | 1 | 10 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.150× (z -29.4) |
| [[KATO III (line)]] | alt | 284 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -28.8) |
| [[LoVo (line)]] | wt | 246 | 2 (1 ⚠) | 9 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.171× (z -25.8) |
| [[LS 180 (line)]] | wt | 351 | 2 (1 ⚠) | 9 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -31.1) |
| [[Panc 03.27 (line)]] | alt | 233 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -29.2) |
| [[SNU-423 (line)]] | alt | 436 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -29.2) |
| [[SW480 (line)]] | alt | 427 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0872× (z -35.6) |
| [[NCI-H23 (line)]] | alt | 309 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -29.4) |
| [[PANC-1 (line)]] | alt | 403 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -32.5) |
| [[RKO (line)]] | wt | 328 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -28.0) |
| [[SW48 (line)]] | wt | 381 | 0 | 9 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.123× (z -23.6) |
| [[C-33 A (line)]] | alt | 543 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -33.0) |
| [[CHP-212 (line)]] | wt | 404 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -18.9) |
| [[RPMI-7951 (line)]] | alt | 260 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -17.1) |
| [[SW 900 (line)]] | alt | 229 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -25.4) |
| [[SW1417 (line)]] | alt | 334 | 1 | 7 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -30.5) |
| [[A-172 (line)]] | wt | 186 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -22.5) |
| [[AsPC-1 (line)]] | alt | 210 | 1 (1 ⚠) | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -28.7) |
| [[HEC-1-A (line)]] | alt | 286 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -28.3) |
| [[J82 (line)]] | alt | 221 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -24.0) |
| [[NCI-H2347 (line)]] | alt | 144 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -26.4) |
| [[NCI-H661 (line)]] | alt | 427 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -15.3) |
| [[SHP-77 (line)]] | alt | 280 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -24.9) |
| [[SNU-1 (line)]] | wt | 418 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -24.9) |
| [[A498 (line)]] | wt | 128 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -25.3) |
| [[A549 (line)]] | wt | 175 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -19.6) |
| [[Hs 766T (line)]] | wt | 167 | 1 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -22.9) |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -26.1) |
| [[HCT15 (line)]] | alt | 326 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -14.3) |
| [[HS-578T (line)]] | alt | 211 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -26.0) |
| [[hTERT-HPNE (line)]] | wt | 250 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -22.5) |
| [[COLO 205 (line)]] | alt | 162 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -20.3) |
| [[SW 1271 (line)]] | alt | 329 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -10.9) |
| [[BT-474 (line)]] | alt | 214 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 131 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -15.8) |
| [[H4 (line)]] | wt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 173 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL17]] | +0.76 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[NCOA2]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[CREBBP]] | +0.72 | +0.61 / +0.66 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers; STRING 585 |
| [[TCF12]] | +0.72 | +0.63 / +0.65 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[WDFY3]] | +0.72 | +0.57 / +0.65 | both halves | 1e-05 | same gene group |
| [[UBTF]] | +0.71 | +0.66 / +0.59 | both halves | 7e-06 | pathway: Epigenetic regulation of gene expression |
| [[ARID2]] | +0.70 | +0.49 / +0.72 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 997 |
| [[ATAD2B]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TLK2]] | +0.66 | +0.31 / +0.69 | both halves | 2e-04 |  |
| [[TBC1D5]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ARID1A]] | +0.65 | +0.49 / +0.56 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[CRPPA]] | +0.65 | +0.65 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIPR]] | -0.64 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SEC22B]] | -0.62 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FCHO1]] | -0.61 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[CDA]] | -0.59 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[RGS9]] | -0.59 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GP6-AS1]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[KIF21B]] | -0.58 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[KIAA0513]] | -0.57 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[GDPD5]] | -0.57 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RARS1]] | -0.56 | -0.49 / -0.49 | both halves | 2e-05 | pathway: MITF-M-regulated melanocyte development |
| [[KCTD21]] | -0.56 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MAST1]] | -0.56 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC33]] | B | CCDC33 activity lowers ARID1B's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.51× higher at baseline in the lines without CCDC33 | 0.072 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-4.6, 13.8); signed map (27.5, -23.6). **Vector** length 146, 59.1% of its response variance represented; |z| ≥ 3 in 1,624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.4 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.8 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.2 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +8.4 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.4 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -14.1 | -16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -13.1 | -11.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -9.0 | -18.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -12.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.6 | -35.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -6.4 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.5 | -9.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.4 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -10.3 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:156,776,020-157,210,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1235, ELD/OSA1, p250R, BAF250b, DAN15, 6A3-5, SMARCF2 |
| Gene groups (HGNC) | AT-rich interaction domain containing; Armadillo like helical domain containing; BAF complex subunits |
| Reactome | 19 pathways, smallest: Formation of the canonical BAF (cBAF) complex; Formation of neuronal progenitor and neuronal BAF (npBAF and nBAF); SWI/SNF chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFD5](https://www.uniprot.org/uniprotkb/Q8NFD5) (AT-rich interactive domain-containing protein 1B):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF complex) and the neuron-specific chromatin remodeling complex (nBAF complex). …

**Summary**, from NCBI Gene [57492](https://www.ncbi.nlm.nih.gov/gene/57492):

> This locus encodes an AT-rich DNA interacting domain-containing protein. The encoded protein is a component of the SWI/SNF chromatin remodeling complex and may play a role in cell-cycle activation. The protein encoded by this locus is similar to AT-rich interactive domain-containing protein 1A. These two proteins function as alternative, mutually exclusive ARID-subunits of the SWI/SNF complex. The associated complexes play opposing roles. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:18040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18040) · Entrez [57492](https://www.ncbi.nlm.nih.gov/gene/57492) · UniProt [Q8NFD5](https://www.uniprot.org/uniprotkb/Q8NFD5) · Ensembl [ENSG00000049618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049618)

## Data

Gene col 553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 553); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 553]; `tensor/DDL_lfc|DDL_z.npy` [553]; `embed/gene_vectors.npy` [553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 553 or target_col == 553). Every well: [[ARID1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
