---
symbol: "MGLL"
type: "gene"
col: 1080
ensembl_id: "ENSG00000074416"
name: "monoglyceride lipase"
location: "3q21.3"
module: 116
arm: "+"
pooled_cpm: 76.63
n_lines_expressing: 36
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 21
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# MGLL

*monoglyceride lipase* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +16.3, q 0e+00, up in 18 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.510× (z -15.7, q 0e+00, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGM5P2-1]] (+0.62, fdr 1e-05), [[DUSP5-DT]] (+0.58, fdr 1e-05), [[SAMD4A]] (+0.58, fdr 3e-05); moves opposite to [[PGAP1]] (-0.57, fdr 1e-05), [[SPATA6]] (-0.53, fdr 3e-05), [[BCL9]] (-0.52, fdr 3e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RDUR]] → it (grade B ⚠); 21 go from it, the strongest it → [[BCL9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +16.3 | 0e+00 | 18/35 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +13.7 | 2e-40 | 20/35 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.44×** | +12.0 | 1e-30 | 25/35 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +11.6 | 5e-29 | 24/34 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.60×** | +11.0 | 5e-26 | 29/34 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +10.6 | 3e-24 | 16/27 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.55×** | +10.2 | 2e-22 | 25/34 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.56×** | +10.0 | 7e-22 | 29/33 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.53×** | +9.9 | 2e-21 | 25/33 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +7.7 | 9e-13 | 25/33 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.57×** | +7.5 | 3e-12 | 24/34 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.72×** | +6.6 | 2e-09 | 22/32 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +6.2 | 3e-08 | 16/30 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.6 | 1e-06 | 17/34 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.4 | 2e-06 | 13/34 (HOP62, BT-474, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.48×** | +4.8 | 5e-05 | 19/34 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +4.2 | 9e-04 | 10/34 (SNU-423, KATO III, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.9 | 0.003 | 8/34 (BT-474, A498, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.033 | 7/34 (NCI-H2347, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.055 | 4/34 (A549, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.510×** | -15.7 | 0e+00 | 30/34 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.540×** | -14.4 | 2e-44 | 28/34 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.609×** | -11.6 | 7e-29 | 26/34 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -9.4 | 5e-19 | 22/34 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -8.5 | 1e-15 | 24/34 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.699×** | -8.1 | 7e-14 | 20/33 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.715×** | -7.8 | 4e-13 | 24/35 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.707×** | -7.8 | 5e-13 | 19/34 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -7.6 | 2e-12 | 20/34 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -7.0 | 1e-10 | 20/34 (CFPAC-1, A498, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.621×** | -5.8 | 3e-07 | 20/34 (CFPAC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.781×** | -5.8 | 4e-07 | 21/34 (RKO, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.786×** | -5.4 | 3e-06 | 17/33 (J82, LOX-IMVI, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.703×** | -4.3 | 7e-04 | 12/34 (CFPAC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.709×** | -4.2 | 1e-03 | 16/34 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.828×** | -4.1 | 0.002 | 14/34 (SK-MEL-2, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.866× | -4.0 | 0.002 | 11/34 (SK-MEL-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.851× | -3.8 | 0.005 | 13/35 (J82, SK-MEL-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 257 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -26.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.156× (z -25.8) |
| [[HS-578T (line)]] | alt | 120 | 5 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +17.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -11.3) |
| [[COLO 205 (line)]] | alt | 66.0 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 3.83× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 208 | 1 (1 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -24.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -17.6) |
| [[J82 (line)]] | alt | 136 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.413× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.291× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 131 | 4 (2 ⚠) | 4 (1 ⚠) | [[Peretinoin (drug)]] 5 µM 2.99× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -15.2) |
| [[A498 (line)]] | wt | 180 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 167 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.18× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -14.3) |
| [[A549 (line)]] | wt | 114 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -22.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.228× (z -16.9) |
| [[hTERT-HPNE (line)]] | wt | 112 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +9.5) ⚠ cell-cycle shift, explains ~24% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 23.9 | 5 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.17× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -13.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.273× (z -12.4) |
| [[BT-474 (line)]] | alt | 114 | 2 (1 ⚠) | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.97× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.387× (z -8.6) |
| [[HOP62 (line)]] | alt | 44.3 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.6) | [[Ixazomib citrate (drug)]] 5 µM 0.368× (z -8.9) |
| [[HT-29 (line)]] | alt | 165 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.207× (z -12.5) |
| [[SW480 (line)]] | alt | 20.8 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +13.2) | — |
| [[A-172 (line)]] | wt | 76.4 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -8.6) |
| [[KATO III (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -10.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.302× (z -10.0) |
| [[LS 180 (line)]] | wt | 68.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -23.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.509× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 37.0 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.330× (z -11.1) |
| [[RKO (line)]] | wt | 45.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.305× (z -8.7) |
| [[SNU-423 (line)]] | alt | 72.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -12.1) |
| [[Hs 766T (line)]] | wt | 83.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.88× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 39.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 74.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.87× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 8.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.67 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGM5P2-1]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[DUSP5-DT]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SAMD4A]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[MAMLD1]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF28]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[GRK4]] | +0.57 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[CAPN2]] | +0.56 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[ETS1]] | +0.56 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[RGS20]] | +0.56 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[RPSAP52]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ITGB1-DT]] | +0.55 | +0.49 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAP1]] | -0.57 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SPATA6]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[BCL9]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[DYNC2LI1]] | -0.51 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TBC1D32]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[FAM229B]] | -0.50 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PEX2]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CRYZL1]] | -0.49 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[PRMT9]] | -0.49 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[ETFB]] | -0.48 | -0.33 / -0.47 | both halves | 1e-04 | pathway: HALLMARK_ADIPOGENESIS |
| [[KCTD6]] | -0.48 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[MRPL22]] | -0.47 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDUR]] | B | RDUR activity raises MGLL's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without RDUR | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[MAP2K1]] | B | MAP2K1 activity raises MGLL's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[ARHGEF28]] | B | ARHGEF28 activity raises MGLL's level | lines that do not express ARHGEF28 (6) vs lines expressing it (44) | 3.35× lower at baseline in the lines without ARHGEF28 | 0.076 | ⚠ within organs, on part of the lines; also absent: SHB, RABGEF1P3, TBILA; maybe low, not absent |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL9]] | B | MGLL activity lowers BCL9's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.80× higher at baseline in the lines without MGLL | 0.015 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[BBS5]] | B | MGLL activity lowers BBS5's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.24× higher at baseline in the lines without MGLL | 0.015 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[ZNF713]] | B | MGLL activity lowers ZNF713's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.84× higher at baseline in the lines without MGLL | 0.021 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[BCAR3]] | B | MGLL activity raises BCAR3's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.93× lower at baseline in the lines without MGLL | 0.022 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[LINC00707]] | B | MGLL activity raises LINC00707's level | lines that do not express MGLL (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without MGLL | 0.025 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[TET1]] | B | MGLL activity lowers TET1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 3.98× higher at baseline in the lines without MGLL | 0.033 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[ETS1]] | B | MGLL activity raises ETS1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.47× lower at baseline in the lines without MGLL | 0.038 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[TBILA]] | B | MGLL activity raises TBILA's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without MGLL | 0.040 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[CCDC9B]] | B | MGLL activity raises CCDC9B's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without MGLL | 0.041 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[PGAP1]] | B | MGLL activity lowers PGAP1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.00× higher at baseline in the lines without MGLL | 0.044 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[LINC00393]] | B | MGLL activity raises LINC00393's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without MGLL | 0.044 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[SPATA6]] | B | MGLL activity lowers SPATA6's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.93× higher at baseline in the lines without MGLL | 0.046 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.3, 11.2); signed map (13.0, 42.3). **Vector** length 117, 31.3% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +11.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.2 | +11.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.8 | +10.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.7 | +10.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -7.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -7.8 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -4.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | monoglyceride lipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:127,689,062-128,052,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HU-K5, MGL, MAGL |
| Gene groups (HGNC) | Lipases; 2-arachidonoylglycerol hydrolases |
| Hallmark sets | FATTY_ACID_METABOLISM, UV_RESPONSE_DN, ADIPOGENESIS |
| Reactome | 18 pathways, smallest: Acyl chain remodeling of DAG and TAG; Arachidonate production from DAG; Triglyceride catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99685](https://www.uniprot.org/uniprotkb/Q99685) (Monoglyceride lipase):

> Converts monoacylglycerides to free fatty acids and glycerol. Hydrolyzes the endocannabinoid 2-arachidonoylglycerol, and thereby contributes to the regulation of endocannabinoid signaling, nociperception and perception of pain. Regulates the levels of fatty acids that serve as signaling molecules and promote cancer cell migration, invasion and tumor growth.

**Summary**, from NCBI Gene [11343](https://www.ncbi.nlm.nih.gov/gene/11343):

> This gene encodes a serine hydrolase of the AB hydrolase superfamily that catalyzes the conversion of monoacylglycerides to free fatty acids and glycerol. The encoded protein plays a critical role in several physiological processes including pain and nociperception through hydrolysis of the endocannabinoid 2-arachidonoylglycerol. Expression of this gene may play a role in cancer tumorigenesis and metastasis. Alternatively spliced transcript variants encoding multiple isoforms have been observed …

**Accessions** — [HGNC:17038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17038) · Entrez [11343](https://www.ncbi.nlm.nih.gov/gene/11343) · UniProt [Q99685](https://www.uniprot.org/uniprotkb/Q99685) · Ensembl [ENSG00000074416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074416)

## Data

Gene col 1080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1080); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1080]; `tensor/DDL_lfc|DDL_z.npy` [1080]; `embed/gene_vectors.npy` [1080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1080 or target_col == 1080). Every well: [[MGLL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGLL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
