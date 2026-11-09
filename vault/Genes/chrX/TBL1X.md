---
symbol: "TBL1X"
type: "gene"
col: 2179
ensembl_id: "ENSG00000101849"
name: "transducin beta like 1 X-linked"
location: "Xp22.31-p22.2"
module: 222
arm: "+"
pooled_cpm: 152.47
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# TBL1X

*transducin beta like 1 X-linked* — Xp22.31-p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.29× (z +5.4, q 3e-05, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.404× (z -19.5, q 0e+00, down in 41 of 44 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.548× (z -18.2, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42BPA]] (+0.56, fdr 1e-05), [[PTPN4]] (+0.54, fdr 3e-05), [[STAU2]] (+0.54, fdr 5e-05); moves opposite to [[ARHGAP1]] (-0.52, fdr 3e-05), [[ZNF17]] (-0.47, fdr 1e-04), [[APLN]] (-0.47, fdr 1e-04).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[VPS13A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +5.4 | 3e-05 | 27/44 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +5.3 | 3e-05 | 26/44 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.1 | 7e-05 | 17/44 (RPMI-7951, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.22×** | +4.2 | 0.004 | 21/43 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.009 | 21/43 (CFPAC-1, SW480, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.13× | +3.7 | 0.021 | 12/44 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.7 | 0.021 | 18/43 (SNU-1, BT-474, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.044 | 10/44 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.17× | +3.3 | 0.049 | 19/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.049 | 11/44 (SNU-1, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.053 | 15/43 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.16× | +3.2 | 0.055 | 17/44 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.056 | 15/44 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.063 | 17/46 (A-427, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.088 | 20/45 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.093 | 17/43 (NCI-H460, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.093 | 8/44 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.093 | 13/44 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.404×** | -19.5 | 0e+00 | 41/44 (LoVo, C-33 A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.422×** | -18.5 | 0e+00 | 39/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -18.2 | 0e+00 | 42/45 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.603×** | -15.4 | 0e+00 | 35/44 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.517×** | -14.2 | 1e-43 | 38/44 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -13.6 | 4e-40 | 39/44 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -13.3 | 3e-38 | 40/43 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.571×** | -12.0 | 2e-31 | 36/44 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.590×** | -10.5 | 6e-24 | 33/42 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -9.6 | 4e-20 | 38/45 (RKO, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.639×** | -9.6 | 4e-20 | 36/45 (CHP-212, C-33 A, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.636×** | -9.3 | 5e-19 | 34/44 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.638×** | -9.3 | 9e-19 | 35/46 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **0.678×** | -8.0 | 4e-14 | 26/41 (C-33 A, AN3 CA, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.728×** | -6.6 | 2e-09 | 25/44 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -5.7 | 3e-07 | 26/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.792×** | -5.0 | 2e-05 | 23/44 (SW1417, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.699×** | -4.0 | 0.002 | 24/44 (LoVo, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -3.8 | 0.003 | 19/44 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.720×** | -3.7 | 0.005 | 20/43 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.831×** | -3.7 | 0.006 | 20/43 (RKO, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 0.890× | -3.5 | 0.010 | 8/44 (SW48, RKO, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.862× | -3.2 | 0.030 | 20/44 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.813×** | -3.2 | 0.030 | 16/44 (LoVo, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.870× | -2.9 | 0.073 | 20/44 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.778×** | -2.8 | 0.079 | 20/44 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 348 | 0 | 18 (13 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -24.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 161 | 0 | 17 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -27.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -21.1) |
| [[MIA PaCa-2 (line)]] | alt | 217 | 0 | 17 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -22.8) |
| [[NCI-H1573 (line)]] | alt | 276 | 0 | 17 (13 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -30.0) |
| [[LS 180 (line)]] | wt | 173 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -18.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 280 | 0 | 13 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0524× (z -36.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -17.3) |
| [[RKO (line)]] | wt | 175 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -23.0) |
| [[A-427 (line)]] | wt | 221 | 0 | 12 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -17.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.456× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 178 | 0 | 12 (8 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.427× (z -11.7) |
| [[SW48 (line)]] | wt | 276 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -16.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -14.2) |
| [[PANC-1 (line)]] | alt | 148 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 128 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -17.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.5) |
| [[C-33 A (line)]] | alt | 433 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.9) |
| [[HT-29 (line)]] | alt | 116 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -18.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -12.3) |
| [[SW1417 (line)]] | alt | 155 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -16.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -14.9) |
| [[A549 (line)]] | wt | 142 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -14.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 228 | 2 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Panobinostat (drug)]] 5 µM 0.460× (z -11.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.313× (z -9.2) |
| [[CHP-212 (line)]] | wt | 241 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0998× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -10.2) |
| [[SNU-423 (line)]] | alt | 221 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -15.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -9.7) |
| [[A-172 (line)]] | wt | 86.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -13.5) |
| [[SNU-1 (line)]] | wt | 216 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -17.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 105 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -12.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.276× (z -9.7) |
| [[AN3 CA (line)]] | alt | 443 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 364 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -15.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.335× (z -12.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[Hs 766T (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -13.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 131 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.477× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -11.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.413× (z -9.5) |
| [[HOP62 (line)]] | alt | 84.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -13.4) |
| [[SW 900 (line)]] | alt | 89.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 311 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 87.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -13.2) |
| [[H4 (line)]] | wt | 144 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -8.9) |
| [[HCT15 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -14.5) |
| [[J82 (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SHP-77 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[A498 (line)]] | wt | 37.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42BPA]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PTPN4]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 | pathway: Transcriptional Regulation by MECP2 |
| [[STAU2]] | +0.54 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[NR6A1]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PARD3]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[GKAP1]] | +0.52 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[SLC7A11]] | +0.52 | +0.47 / +0.54 | both halves | 2e-05 | pathway: Cellular response to chemical stress |
| [[NFIB]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[DOCK3]] | +0.50 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[COBL]] | +0.50 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[LONRF2]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[RAPGEF2]] | +0.48 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP1]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF17]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[APLN]] | -0.47 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[KIAA0319L]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PANK2]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CPT2]] | -0.46 | -0.53 / -0.37 | both halves | 8e-05 | pathway: PPARA activates gene expression; STRING 453 |
| [[C12orf4]] | -0.46 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[KCTD10]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[SENP2]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CCNT1]] | -0.43 | -0.48 / -0.36 | both halves | 1e-04 | pathway: Signaling by Nuclear Receptors |
| [[COG1]] | -0.43 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TMCO1]] | -0.43 | -0.47 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VPS13A]] | C | TBL1X activity raises VPS13A's level | lines that do not express TBL1X (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without TBL1X | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF160, ZNF845, CRPPA; its own permutation p |
| [[LMO4]] | C | TBL1X activity raises LMO4's level | lines that do not express TBL1X (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without TBL1X | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF160, ZNF845, CRPPA; its own permutation p |

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 15.4); signed map (4.4, 11.8). **Vector** length 104, 32.3% of its response variance represented; |z| ≥ 3 in 1,666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +9.5 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.4 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -9.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | transducin beta like 1 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.31-p22.2 — chrX:9,463,320-9,741,037 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EBI; previously TBL1 |
| Gene groups (HGNC) | WD repeat domain containing; NCoR/SMRT transcriptional repression complex subunits |
| Reactome | 55 pathways, smallest: Loss of MECP2 binding ability to the NCoR/SMRT complex; Disorders of Nervous System Development; Loss of function of MECP2 in Rett syndrome |
| Matched by | ensembl_id |

**Function**, from UniProt [O60907](https://www.uniprot.org/uniprotkb/O60907) (F-box-like/WD repeat-containing protein TBL1X):

> F-box-like protein involved in the recruitment of the ubiquitin/19S proteasome complex to nuclear receptor-regulated transcription units. Plays an essential role in transcription activation mediated by nuclear receptors. Probably acts as integral component of corepressor complexes that mediates the recruitment of the 19S proteasome complex, leading to the subsequent proteasomal degradation of transcription repressor complexes, thereby allowing cofactor exchange.

**Summary**, from NCBI Gene [6907](https://www.ncbi.nlm.nih.gov/gene/6907):

> The protein encoded by this gene has sequence similarity with members of the WD40 repeat-containing protein family. The WD40 group is a large family of proteins, which appear to have a regulatory function. It is believed that the WD40 repeats mediate protein-protein interactions and members of the family are involved in signal transduction, RNA processing, gene regulation, vesicular trafficking, cytoskeletal assembly and may play a role in the control of cytotypic differentiation. This encoded …

**Accessions** — [HGNC:11585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11585) · Entrez [6907](https://www.ncbi.nlm.nih.gov/gene/6907) · UniProt [O60907](https://www.uniprot.org/uniprotkb/O60907) · Ensembl [ENSG00000101849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101849)

## Data

Gene col 2179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2179); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2179]; `tensor/DDL_lfc|DDL_z.npy` [2179]; `embed/gene_vectors.npy` [2179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2179 or target_col == 2179). Every well: [[TBL1X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBL1X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
