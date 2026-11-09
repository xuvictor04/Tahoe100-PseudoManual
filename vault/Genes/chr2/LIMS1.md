---
symbol: "LIMS1"
type: "gene"
col: 9851
ensembl_id: "ENSG00000169756"
name: "LIM zinc finger domain containing 1"
location: "2q12.3"
module: 178
arm: "+"
pooled_cpm: 282.76
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# LIMS1

*LIM zinc finger domain containing 1* — 2q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +19.8, q 0e+00, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (CFPAC-1 3.35×, NCI-H460 2.28×, Panc 03.27 2.54×, A498 1.94×, …); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H460 2.01×, PANC-1 1.85×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 2.50×, NCI-H460 1.82×; ⚠ cell-cycle shift, explains ~8% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.670× (z -22.5, q 0e+00, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSBP2]] (+0.50, fdr 4e-05), [[YES1]] (+0.49, fdr 7e-05), [[CDK14]] (+0.49, fdr 2e-04); moves opposite to [[ASB7]] (-0.57, fdr 1e-05), [[ZNF224]] (-0.54, fdr 2e-05), [[ZNF174]] (-0.53, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IL11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9851.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (CFPAC-1 3.35×, NCI-H460 2.28×, Panc 03.27 2.54×, A498 1.94×, …); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H460 2.01×, PANC-1 1.85×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 2.50×, NCI-H460 1.82×; ⚠ cell-cycle shift, explains ~8% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +19.8 | 0e+00 | 29/48 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +7.2 | 2e-10 | 24/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +6.9 | 1e-09 | 22/48 (NCI-H460, BT-474, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +6.8 | 1e-09 | 22/49 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +5.9 | 3e-07 | 22/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.6 | 3e-06 | 17/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +5.0 | 5e-05 | 0/50 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.11× | +4.2 | 0.002 | 19/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.11× | +4.2 | 0.002 | 17/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.07× | +4.1 | 0.002 | 2/48 (HepG2/C3A, C-33 A) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.11× | +4.1 | 0.002 | 17/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.6 | 0.015 | 14/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 14/48 (LoVo, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.09× | +3.2 | 0.059 | 9/47 (BT-474, HT-29, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.08× | +3.2 | 0.059 | 6/47 (HT-29, C-33 A, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.08× | +3.1 | 0.078 | 6/48 (NCI-H23, C-33 A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -22.5 | 0e+00 | 39/49 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -16.5 | 0e+00 | 38/49 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -13.7 | 3e-40 | 39/47 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.759×** | -10.9 | 1e-25 | 32/48 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -9.0 | 3e-17 | 20/48 (SW1417, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.653×** | -8.8 | 8e-17 | 33/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.795×** | -8.7 | 2e-16 | 27/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | **0.817×** | -8.0 | 7e-14 | 26/48 (AsPC-1, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.823×** | -7.7 | 8e-13 | 24/48 (HS-578T, H4, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.837× | -6.8 | 8e-10 | 24/50 (C32, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.858× | -6.0 | 8e-08 | 23/48 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.904× | -5.6 | 1e-06 | 10/48 (RPMI-7951, CHP-212, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.882× | -5.0 | 3e-05 | 18/48 (hTERT-HPNE, LOX-IMVI, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.879× | -4.9 | 4e-05 | 15/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.887× | -4.7 | 8e-05 | 16/49 (HOP62, LS 180, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.897× | -4.1 | 0.001 | 11/49 (SW 1088, RPMI-7951, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.922× | -4.0 | 0.002 | 10/48 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.907× | -3.8 | 0.004 | 11/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.908× | -3.8 | 0.004 | 7/48 (RPMI-7951, KATO III, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 0.915× | -3.7 | 0.005 | 4/49 (SK-MEL-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.911× | -3.7 | 0.006 | 11/48 (H4, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.910× | -3.6 | 0.008 | 13/47 (SK-MEL-2, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 1,207 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 777 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -17.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -14.6) |
| [[LS 180 (line)]] | wt | 237 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -15.0) |
| [[C32 (line)]] | wt | 275 | 2 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.411× (z -13.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 174 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +28.0) | — |
| [[BT-474 (line)]] | alt | 150 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 259 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -15.9) |
| [[SW480 (line)]] | alt | 492 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -18.9) |
| [[A498 (line)]] | wt | 312 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +18.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -12.4) |
| [[H4 (line)]] | wt | 487 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 176 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.99× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.536× (z -10.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.346× (z -9.2) |
| [[A549 (line)]] | wt | 254 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 255 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -17.9) |
| [[HOP62 (line)]] | alt | 420 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.1) |
| [[HS-578T (line)]] | alt | 645 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 370 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -15.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.510× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 277 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 315 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -10.3) |
| [[SW 900 (line)]] | alt | 213 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +18.2) | — |
| [[SW1417 (line)]] | alt | 337 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 188 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +30.2) | [[TAK-901 (drug)]] 5 µM 0.383× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 159 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +13.3) | — |
| [[RKO (line)]] | wt | 166 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.493× (z -9.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 265 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.578× (z -9.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 313 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -9.9) |
| [[HT-29 (line)]] | alt | 171 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.8) | [[TAK-901 (drug)]] 5 µM 0.350× (z -9.0) |
| [[J82 (line)]] | alt | 172 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +14.8) | [[TAK-901 (drug)]] 5 µM 0.371× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 135 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 185 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +20.9) | — |
| [[A-172 (line)]] | wt | 360 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.8) |
| [[C-33 A (line)]] | alt | 266 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.358× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 140 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.251× (z -8.9) |
| [[HCT15 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.529× (z -9.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 199 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.284× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 225 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -11.4) |
| [[SNU-423 (line)]] | alt | 262 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.5) | — |
| [[SW 1088 (line)]] | alt | 674 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.3) |
| [[SW48 (line)]] | wt | 184 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -11.6) |
| [[AN3 CA (line)]] | alt | 191 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 347 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 423 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 261 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBP2]] | +0.50 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[YES1]] | +0.49 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[CDK14]] | +0.49 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[IL11]] | +0.48 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[ABR]] | +0.48 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[PTPRN2]] | +0.47 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[SLC4A7]] | +0.46 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[STK10]] | +0.46 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[MYO1C]] | +0.46 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[MACF1]] | +0.45 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[ZBTB46]] | +0.45 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[MIR222HG]] | +0.44 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*70 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ZNF224]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZNF174]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[FASTKD3]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[NIF3L1]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[MRPL44]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[LRIG2]] | -0.51 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[HOXA3]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[FNTB]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ZDHHC7]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ALG9]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[PANK1]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL11]] | B | IL11 activity raises LIMS1's level | lines that do not express IL11 (27) vs lines expressing it (23) | 1.69× lower at baseline in the lines without IL11 | 0.046 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction -0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.0, -17.2); signed map (-2.5, 34.2). **Vector** length 123, 34.6% of its response variance represented; |z| ≥ 3 in 1,408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +19.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +6.3 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.2 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -9.6 | -16.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -9.5 | -8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.3 | -13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -22.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.8 | -7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | LIM zinc finger domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.3 — chr2:108,533,671-108,687,246 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PINCH, PINCH1 |
| Gene groups (HGNC) | LIMS zinc finger family; LIM domain containing; ILK-PINCH-Parvin complex subunits |
| Reactome | 4 pathways, smallest: Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; Cell-extracellular matrix interactions; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P48059](https://www.uniprot.org/uniprotkb/P48059) (LIM and senescent cell antigen-like-containing domain protein 1):

> Within the IPP (ILK-PINCH-PARVIN) complex, binds to F-actin, promoting F-actin bundling, a process required to generate force for actin cytoskeleton reorganization and subsequent dynamic cell adhesion events such as cell spreading and migration.

**Summary**, from NCBI Gene [3987](https://www.ncbi.nlm.nih.gov/gene/3987):

> The protein encoded by this gene is an adaptor protein which contains five LIM domains, or double zinc fingers. The protein is likely involved in integrin signaling through its LIM domain-mediated interaction with integrin-linked kinase, found in focal adhesion plaques. It is also thought to act as a bridge linking integrin-linked kinase to NCK adaptor protein 2, which is involved in growth factor receptor kinase signaling pathways. Its localization to the periphery of spreading cells also …

**Accessions** — [HGNC:6616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6616) · Entrez [3987](https://www.ncbi.nlm.nih.gov/gene/3987) · UniProt [P48059](https://www.uniprot.org/uniprotkb/P48059) · Ensembl [ENSG00000169756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169756)

## Data

Gene col 9851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9851); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9851]; `tensor/DDL_lfc|DDL_z.npy` [9851]; `embed/gene_vectors.npy` [9851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9851 or target_col == 9851). Every well: [[LIMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
