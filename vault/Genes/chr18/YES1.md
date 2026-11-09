---
symbol: "YES1"
type: "gene"
col: 10683
ensembl_id: "ENSG00000176105"
name: "YES proto-oncogene 1, Src family tyrosine kinase"
location: "18p11.32"
module: 54
arm: "-"
pooled_cpm: 190.31
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# YES1

*YES proto-oncogene 1, Src family tyrosine kinase* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +30.4, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.823× (z -5.8, q 2e-06, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H23 0.412×, A-427 0.572×, RKO 0.566×, LOX-IMVI 0.473×); [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.717×, MIA PaCa-2 0.781×, HOP62 0.837×; ⚠ position not correctable); [[Panobinostat (drug)]] 0.5 µM in 3 lines (A-427 0.542×, NCI-H23 0.482×, RKO 0.573×; ⚠ cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 5 µM in 1 line (NCI-H23 0.649×).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTRF1L]] (+0.56, fdr 1e-05), [[PHF10]] (+0.54, fdr 6e-05), [[KPNA4]] (+0.51, fdr 3e-05); moves opposite to [[POP7]] (-0.57, fdr 2e-04), [[TAB1]] (-0.55, fdr 3e-05), [[DDX55]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC4A7]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +30.4 | 0e+00 | 43/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +16.8 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +13.5 | 3e-39 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +13.2 | 8e-38 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +13.2 | 1e-37 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +12.5 | 4e-34 | 38/49 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +11.6 | 2e-29 | 38/45 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +11.3 | 7e-28 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +11.1 | 6e-27 | 33/44 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +9.8 | 5e-21 | 35/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +9.2 | 2e-18 | 37/49 (SW48, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +8.9 | 2e-17 | 35/47 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +8.5 | 5e-16 | 35/48 (C32, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +7.7 | 4e-13 | 31/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +7.1 | 4e-11 | 20/49 (LoVo, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +5.6 | 8e-07 | 25/48 (HT-29, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +4.5 | 2e-04 | 18/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.001 | 20/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.027 | 10/49 (PANC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.10× | +2.8 | 0.097 | 5/48 (PANC-1, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H23 0.412×, A-427 0.572×, RKO 0.566×, LOX-IMVI 0.473×); [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.717×, MIA PaCa-2 0.781×, HOP62 0.837×; ⚠ position not correctable); [[Panobinostat (drug)]] 0.5 µM in 3 lines (A-427 0.542×, NCI-H23 0.482×, RKO 0.573×; ⚠ cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 5 µM in 1 line (NCI-H23 0.649×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.823×** | -5.8 | 2e-06 | 25/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.823×** | -5.8 | 2e-06 | 22/48 (NCI-H23, RKO, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -5.5 | 8e-06 | 2/50 (NCI-H23, MIA PaCa-2) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -5.2 | 3e-05 | 23/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 0.839× | -5.0 | 6e-05 | 21/47 (HT-29, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.851× | -4.8 | 2e-04 | 19/48 (LOX-IMVI, NCI-H23, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.901× | -4.4 | 0.001 | 8/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.903× | -4.3 | 0.001 | 10/48 (NCI-H23, C32, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.871× | -4.1 | 0.002 | 19/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.908× | -3.9 | 0.005 | 7/49 (C32, HOP62, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.837× | -3.8 | 0.008 | 17/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.887× | -3.6 | 0.016 | 12/47 (C32, LOX-IMVI, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.887× | -3.6 | 0.016 | 11/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.902× | -3.5 | 0.021 | 8/48 (NCI-H23, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.901× | -3.4 | 0.025 | 10/49 (NCI-H23, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.897× | -3.2 | 0.042 | 10/48 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.075 | 12/48 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.929× | -3.0 | 0.078 | 6/48 (NCI-H23, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 135 | 14 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +27.7) | — |
| [[SW480 (line)]] | alt | 179 | 11 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +18.5) | — |
| [[LoVo (line)]] | wt | 139 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 199 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +28.9) | — |
| [[LS 180 (line)]] | wt | 162 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 244 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +16.5) | — |
| [[HT-29 (line)]] | alt | 196 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +21.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.580× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[KATO III (line)]] | alt | 117 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 331 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.412× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 233 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 390 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +21.5) | — |
| [[SW48 (line)]] | wt | 153 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.6) | — |
| [[A549 (line)]] | wt | 150 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.9) | — |
| [[AsPC-1 (line)]] | alt | 165 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +21.0) | — |
| [[HEC-1-A (line)]] | alt | 152 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +18.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 290 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +16.7) | — |
| [[NCI-H1573 (line)]] | alt | 200 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +28.1) | — |
| [[NCI-H2347 (line)]] | alt | 202 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +16.9) | — |
| [[A-427 (line)]] | wt | 370 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.79× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.542× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.572× (z -11.6) |
| [[A498 (line)]] | wt | 147 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.9) | — |
| [[C32 (line)]] | wt | 149 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 59.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 104 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.5) | — |
| [[SW 900 (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.4) | — |
| [[SW1417 (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +21.7) | — |
| [[A-172 (line)]] | wt | 205 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 200 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.13× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 403 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.487× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 222 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +20.5) | [[Lonafarnib (drug)]] 5 µM 0.231× (z -12.9) ⚠ toxic |
| [[RKO (line)]] | wt | 268 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.566× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 205 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +22.3) | — |
| [[SNU-423 (line)]] | alt | 138 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.8) | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +19.3) | — |
| [[H4 (line)]] | wt | 202 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 180 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 148 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.7) | — |
| [[J82 (line)]] | alt | 236 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 237 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.7) | — |
| [[SHP-77 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.04× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 268 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 202 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 621 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRF1L]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PHF10]] | +0.54 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[KPNA4]] | +0.51 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ZNF655]] | +0.51 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[HDGFL3]] | +0.51 | +0.26 / +0.50 | both halves | 4e-04 |  |
| [[SEPTIN11]] | +0.50 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[BLOC1S6]] | +0.50 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[CMTM6]] | +0.49 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[WSB2]] | +0.49 | +0.26 / +0.50 | both halves | 3e-04 |  |
| [[LIMS1]] | +0.49 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[CTNNA1]] | +0.49 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[PRKAR1A]] | +0.49 | +0.27 / +0.56 | both halves | 3e-04 | pathway: Anti-inflammatory response favouring Leishmania parasite infection |

## Genes that move opposite

*51 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP7]] | -0.57 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[TAB1]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[DDX55]] | -0.55 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[NUP160]] | -0.55 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[HEATR6]] | -0.52 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[GTF3C2]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[LRIG2]] | -0.52 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[PHAF1]] | -0.51 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[RBM14]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 | pathway: RUNX2 regulates bone development |
| [[MRPS34]] | -0.50 | -0.24 / -0.55 | both halves | 5e-04 |  |
| [[MRPL44]] | -0.49 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[CHCHD1]] | -0.49 | -0.30 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A7]] | C | SLC4A7 activity raises YES1's level | lines that do not express SLC4A7 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without SLC4A7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, CSPG5, NR4A3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.5, -16.4); signed map (13.4, -12.2). **Vector** length 103, 31.9% of its response variance represented; |z| ≥ 3 in 1,391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +30.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.1 | +1.6 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | -0.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | -6.1 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +4.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.4 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | YES proto-oncogene 1, Src family tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:721,588-812,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Yes, c-yes, HsT441 |
| Gene groups (HGNC) | SH2 domain containing; Src family tyrosine kinases; SH3 domain containing |
| Reactome | 39 pathways, smallest: FCGR activation; PECAM1 interactions; Regulation of KIT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P07947](https://www.uniprot.org/uniprotkb/P07947) (Tyrosine-protein kinase Yes):

> Non-receptor protein tyrosine kinase that is involved in the regulation of cell growth and survival, apoptosis, cell-cell adhesion, cytoskeleton remodeling, and differentiation. Stimulation by receptor tyrosine kinases (RTKs) including EGFR, PDGFR, CSF1R and FGFR leads to recruitment of YES1 to the phosphorylated receptor, and activation and phosphorylation of downstream substrates. Upon EGFR activation, promotes the phosphorylation of PARD3 to favor epithelial tight junction assembly. …

**Summary**, from NCBI Gene [7525](https://www.ncbi.nlm.nih.gov/gene/7525):

> This gene is the cellular homolog of the Yamaguchi sarcoma virus oncogene. The encoded protein has tyrosine kinase activity and belongs to the src family of proteins. This gene lies in close proximity to thymidylate synthase gene on chromosome 18, and a corresponding pseudogene has been found on chromosome 22. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12841) · Entrez [7525](https://www.ncbi.nlm.nih.gov/gene/7525) · UniProt [P07947](https://www.uniprot.org/uniprotkb/P07947) · Ensembl [ENSG00000176105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176105)

## Data

Gene col 10683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10683); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10683]; `tensor/DDL_lfc|DDL_z.npy` [10683]; `embed/gene_vectors.npy` [10683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10683 or target_col == 10683). Every well: [[YES1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YES1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
