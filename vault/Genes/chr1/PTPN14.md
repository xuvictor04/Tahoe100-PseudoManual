---
symbol: "PTPN14"
type: "gene"
col: 7591
ensembl_id: "ENSG00000152104"
name: "protein tyrosine phosphatase non-receptor type 14"
location: "1q32.3-q41"
module: 120
arm: "+"
pooled_cpm: 326.71
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# PTPN14

*protein tyrosine phosphatase non-receptor type 14* — 1q32.3-q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.79× (z +6.9, q 3e-09, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 2.56×, A549 2.29×, NCI-H23 1.98×, A-427 1.92×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 5 lines (A549 5.81×, HT-29 4.59×, MIA PaCa-2 4.45×, A-427 3.66×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SNU-1 2.49×, HT-29 2.08×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (SW48 5.22×, Panc 03.27 3.30×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 2.31×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.364× (z -22.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEAD1]] (+0.58, fdr 2e-05), [[CCN2]] (+0.54, fdr 1e-05), [[ARHGAP18]] (+0.51, fdr 2e-05); moves opposite to [[RBCK1]] (-0.53, fdr 3e-05), [[ENTHD1]] (-0.47, fdr 2e-05), [[HDHD3]] (-0.46, fdr 6e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[CAV1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7591.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 2.56×, A549 2.29×, NCI-H23 1.98×, A-427 1.92×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 5 lines (A549 5.81×, HT-29 4.59×, MIA PaCa-2 4.45×, A-427 3.66×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SNU-1 2.49×, HT-29 2.08×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (SW48 5.22×, Panc 03.27 3.30×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 2.31×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +6.9 | 3e-09 | 34/48 (A549, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +4.4 | 0.003 | 28/47 (SW48, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.015 | 23/47 (SNU-1, HT-29, …) | rises with dose | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.7 | 0.027 | 19/47 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.16 | 19/47 (BT-474, HT-29, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.30× | +3.1 | 0.16 | 19/46 (COLO 205, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.0 | 0.17 | 20/47 (HT-29, SNU-1, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.10× | +3.0 | 0.17 | 8/48 (NCI-H1792, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.364×** | -22.9 | 0e+00 | 47/47 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.382×** | -21.8 | 0e+00 | 47/47 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.471×** | -17.1 | 0e+00 | 46/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -16.9 | 0e+00 | 36/48 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.553×** | -12.9 | 3e-36 | 41/46 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -7.5 | 5e-12 | 32/47 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.752×** | -6.5 | 7e-09 | 30/47 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -6.5 | 7e-09 | 32/47 (C32, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.756×** | -6.3 | 1e-08 | 29/48 (CFPAC-1, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.739×** | -6.3 | 1e-08 | 29/44 (CFPAC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.752×** | -6.1 | 5e-08 | 29/47 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.756×** | -6.1 | 6e-08 | 29/47 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.767×** | -6.0 | 9e-08 | 30/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -5.8 | 3e-07 | 23/47 (C32, J82, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -5.6 | 1e-06 | 22/47 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.796×** | -5.2 | 8e-06 | 26/47 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.694×** | -4.3 | 4e-04 | 29/47 (CFPAC-1, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.833×** | -4.0 | 0.002 | 22/46 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.794×** | -3.7 | 0.005 | 23/47 (SW 900, NCI-H1792, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.855× | -3.5 | 0.009 | 19/47 (HOP62, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 469 | 0 | 30 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -24.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -21.0) |
| [[J82 (line)]] | alt | 495 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -21.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 764 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -25.2) |
| [[HOP62 (line)]] | alt | 633 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -21.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -21.0) |
| [[HS-578T (line)]] | alt | 304 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 406 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -20.8) |
| [[Panc 03.27 (line)]] | alt | 470 | 1 | 9 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.30× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.203× (z -22.5) |
| [[SW480 (line)]] | alt | 457 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -20.9) |
| [[HT-29 (line)]] | alt | 209 | 4 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.59× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.332× (z -16.4) |
| [[SNU-423 (line)]] | alt | 362 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 375 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 549 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -16.5) |
| [[SW 900 (line)]] | alt | 409 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -18.1) |
| [[KATO III (line)]] | alt | 240 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 364 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 287 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -19.4) |
| [[A498 (line)]] | wt | 346 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -14.5) |
| [[A549 (line)]] | wt | 128 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.81× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.504× (z -9.8) |
| [[BT-474 (line)]] | alt | 122 | 2 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.47× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -11.8) |
| [[Hs 766T (line)]] | wt | 397 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -20.1) |
| [[PANC-1 (line)]] | alt | 516 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -13.6) |
| [[SW48 (line)]] | wt | 219 | 2 | 3 | [[PH-797804 (drug)]] 5 µM 5.22× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.342× (z -11.9) |
| [[A-427 (line)]] | wt | 205 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.66× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.452× (z -10.9) |
| [[COLO 205 (line)]] | alt | 139 | 2 (2 ⚠) | 2 | [[Selinexor (drug)]] 5 µM 2.29× (z +13.3) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -11.4) |
| [[H4 (line)]] | wt | 308 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.378× (z -8.7) |
| [[LoVo (line)]] | wt | 145 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -18.9) |
| [[MIA PaCa-2 (line)]] | alt | 198 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.45× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.438× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 246 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.370× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 338 | 1 (1 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 1.71× (z +9.4) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 5 µM 0.359× (z -12.6) |
| [[SW1417 (line)]] | alt | 202 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -15.7) |
| [[A-172 (line)]] | wt | 451 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.436× (z -12.6) |
| [[C-33 A (line)]] | alt | 295 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -11.6) |
| [[LS 180 (line)]] | wt | 127 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 194 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 171 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.483× (z -11.3) |
| [[RKO (line)]] | wt | 235 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.441× (z -12.0) |
| [[SNU-1 (line)]] | wt | 386 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.428× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.492× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 232 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 219 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.474× (z -9.2) |
| [[SW 1088 (line)]] | alt | 547 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -8.9) |
| [[SW 1271 (line)]] | alt | 240 | 0 | 2 (1 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.223× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -9.4) |
| [[AN3 CA (line)]] | alt | 233 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEAD1]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 | STRING 445 |
| [[CCN2]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ARHGAP18]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[DOCK2]] | +0.50 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[TGFBR2]] | +0.50 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[DDAH1]] | +0.50 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[CAV1]] | +0.48 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[FN1]] | +0.48 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[CTNNAL1]] | +0.48 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[MIR100HG]] | +0.48 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[MIR4435-2HG]] | +0.45 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[ANTXR1]] | +0.45 | +0.38 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBCK1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ENTHD1]] | -0.47 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HDHD3]] | -0.46 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[KCP]] | -0.45 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[NT5C2]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[SHFL]] | -0.45 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[CSTB]] | -0.44 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[CPAMD8]] | -0.44 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[FUT2]] | -0.43 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[SLC25A29]] | -0.43 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[TTC39B]] | -0.42 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[CD5L]] | -0.42 | -0.29 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV1]] | B | CAV1 activity raises PTPN14's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without CAV1 | 0.001 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[AXL]] | B | AXL activity raises PTPN14's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without AXL | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[CCN1]] | B | CCN1 activity raises PTPN14's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.98× lower at baseline in the lines without CCN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[PRSS23]] | B | PRSS23 activity raises PTPN14's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without PRSS23 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[MSRB3]] | B | MSRB3 activity raises PTPN14's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without MSRB3 | 0.029 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[CEACAM5]] | B | CEACAM5 activity lowers PTPN14's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 1.98× higher at baseline in the lines without CEACAM5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[COL13A1]] | B | COL13A1 activity raises PTPN14's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.77× lower at baseline in the lines without COL13A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[TGFBI]] | B | TGFBI activity raises PTPN14's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without TGFBI | 0.049 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[LINC02742]] | B | LINC02742 activity raises PTPN14's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 1.70× lower at baseline in the lines without LINC02742 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227 |
| [[ETV1]] | B | ETV1 activity strengthens PTPN14's drug response | lines that do not express ETV1 (11) vs lines expressing it (37) | the lines without ETV1 respond 0.76× as strongly (z diff +1.82); strongest at Ixazomib citrate 5 µM: 0.88x vs 0.65x (z diff +4.0) | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136; target measured in part of the lines; artifact flags |
| [[STX11]] | B | STX11 activity raises PTPN14's level | lines that do not express STX11 (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without STX11 | 0.055 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |
| [[COL4A2]] | B | COL4A2 activity raises PTPN14's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 1.56× lower at baseline in the lines without COL4A2 | 0.077 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.2, 13.4); signed map (15.0, 39.8). **Vector** length 112, 37.3% of its response variance represented; |z| ≥ 3 in 1,680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.5 | +2.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.5 | -7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.9 | -12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.2 | -6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.8 | -6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -5.7 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.8 | -3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.2 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3-q41 — chr1:214,348,700-214,552,449 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEZ, PTPD2 |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type; FERM domain containing |
| Hallmark sets | P53_PATHWAY |
| Reactome | 4 pathways, smallest: Interleukin-37 signaling; Interleukin-1 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15678](https://www.uniprot.org/uniprotkb/Q15678) (Tyrosine-protein phosphatase non-receptor type 14):

> Protein tyrosine phosphatase which may play a role in the regulation of lymphangiogenesis, cell-cell adhesion, cell-matrix adhesion, cell migration, cell growth and also regulates TGF-beta gene expression, thereby modulating epithelial-mesenchymal transition. Mediates beta-catenin dephosphorylation at adhesion junctions. Acts as a negative regulator of the oncogenic property of YAP, a downstream target of the hippo pathway, in a cell density-dependent manner. May function as a tumor suppressor.

**Summary**, from NCBI Gene [5784](https://www.ncbi.nlm.nih.gov/gene/5784):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains an N-terminal noncatalytic domain similar to that of band 4.1 superfamily cytoskeleton-associated proteins, which suggested the membrane or cytoskeleton localization of this protein. It appears to regulate …

**Accessions** — [HGNC:9647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9647) · Entrez [5784](https://www.ncbi.nlm.nih.gov/gene/5784) · UniProt [Q15678](https://www.uniprot.org/uniprotkb/Q15678) · Ensembl [ENSG00000152104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152104)

## Data

Gene col 7591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7591); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7591]; `tensor/DDL_lfc|DDL_z.npy` [7591]; `embed/gene_vectors.npy` [7591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7591 or target_col == 7591). Every well: [[PTPN14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
