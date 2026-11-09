---
symbol: "ANP32A"
type: "gene"
col: 6393
ensembl_id: "ENSG00000140350"
name: "acidic nuclear phosphoprotein 32 family member A"
location: "15q23"
module: 29
arm: "+"
pooled_cpm: 119.2
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ANP32A

*acidic nuclear phosphoprotein 32 family member A* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +17.5, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.503× (z -18.3, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF362]] (+0.66, fdr 1e-05), [[LDB1]] (+0.65, fdr 1e-05), [[TOP2B]] (+0.62, fdr 1e-05); moves opposite to [[LRRC8E]] (-0.62, fdr 1e-05), [[POLM]] (-0.57, fdr 4e-05), [[TBRG1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +17.5 | 0e+00 | 49/49 (LoVo, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.04×** | +13.4 | 2e-38 | 45/49 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.73×** | +9.9 | 6e-21 | 35/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.1 | 6e-14 | 44/50 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.53×** | +7.4 | 2e-11 | 32/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.42×** | +6.6 | 4e-09 | 39/48 (Hs 766T, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.3 | 3e-08 | 36/48 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.7 | 6e-07 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +5.4 | 4e-06 | 30/49 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.1 | 2e-05 | 25/48 (Hs 766T, SW1417, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.32×** | +5.0 | 3e-05 | 32/47 (LoVo, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.9 | 4e-05 | 27/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 32/48 (H4, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.025 | 23/47 (NCI-H1792, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.031 | 19/48 (A498, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.503×** | -18.3 | 0e+00 | 37/48 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -13.1 | 6e-37 | 46/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.499×** | -13.1 | 6e-37 | 47/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -12.2 | 4e-32 | 38/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.625×** | -8.9 | 1e-16 | 43/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.720×** | -5.8 | 5e-07 | 35/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.572×** | -5.5 | 3e-06 | 40/49 (C-33 A, AN3 CA, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.3 | 1e-05 | 25/48 (NCI-H2347, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.769×** | -4.9 | 5e-05 | 30/48 (C32, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.772×** | -4.9 | 7e-05 | 28/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.784×** | -4.6 | 2e-04 | 32/49 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.780×** | -4.5 | 3e-04 | 29/48 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.813×** | -3.7 | 0.008 | 25/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **0.825×** | -3.5 | 0.021 | 23/47 (SNU-1, C32, …) | two highest doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.042 | 19/48 (CHP-212, J82, …) | inconsistent across doses | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.045 | 18/49 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.887× | -3.2 | 0.048 | 7/48 (NCI-H23, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.057 | 19/47 (SNU-423, NCI-H1792, …) | rises with dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 113 | 5 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -21.2) |
| [[PANC-1 (line)]] | alt | 174 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -16.5) |
| [[SW480 (line)]] | alt | 121 | 4 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 96.8 | 3 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -17.8) |
| [[A-172 (line)]] | wt | 66.4 | 3 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -19.6) |
| [[C32 (line)]] | wt | 143 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -19.0) |
| [[HOP62 (line)]] | alt | 110 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 129 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -21.4) |
| [[A498 (line)]] | wt | 74.6 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -11.8) |
| [[A549 (line)]] | wt | 118 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 173 | 3 (1 ⚠) | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -10.5) |
| [[HT-29 (line)]] | alt | 159 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 125 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 167 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 105 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -15.9) |
| [[KATO III (line)]] | alt | 117 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.450× (z -9.7) |
| [[LS 180 (line)]] | wt | 110 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 120 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 149 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -12.3) |
| [[SW48 (line)]] | wt | 154 | 2 | 2 | [[TAK-901 (drug)]] 0.05 µM 3.51× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.4) |
| [[C-33 A (line)]] | alt | 219 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.334× (z -13.6) |
| [[COLO 205 (line)]] | alt | 118 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.5) |
| [[HS-578T (line)]] | alt | 60.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.1) |
| [[J82 (line)]] | alt | 122 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -16.5) |
| [[NCI-H2030 (line)]] | alt | 179 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.4) |
| [[Panc 03.27 (line)]] | alt | 92.9 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 117 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.5) |
| [[A-427 (line)]] | wt | 100 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 136 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.0) |
| [[HCT15 (line)]] | alt | 139 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 63.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -16.8) |
| [[LoVo (line)]] | wt | 87.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +15.9) | — |
| [[SNU-423 (line)]] | alt | 67.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.8) |
| [[AN3 CA (line)]] | alt | 188 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 70.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 97.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.0) | — |
| [[H4 (line)]] | wt | 105 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.7) | — |
| [[RKO (line)]] | wt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 137 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Glasdegib (drug)]] 0.05 µM 0.0653× (z -9.1) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 129 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +14.7) | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[LDB1]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TOP2B]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[CDK2AP1]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[AK4]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[USF1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CUL2]] | +0.59 | +0.64 / +0.53 | both halves | 1e-05 | same gene group |
| [[KDM1A]] | +0.59 | +0.70 / +0.57 | both halves | 9e-06 | same gene group |
| [[UBP1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GTF2I]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[UBR5]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[HOXB7]] | +0.57 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8E]] | -0.62 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[POLM]] | -0.57 | -0.43 / -0.54 | both halves | 4e-05 | same gene group |
| [[TBRG1]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PLEKHM1]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SDHAF2]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ZDHHC18]] | -0.53 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ZNF674]] | -0.53 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[SRRD]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PILRB]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MAP1S]] | -0.52 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[LCAT]] | -0.52 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ABAT]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANP32A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TRIM7]] | B | TRIM7 activity lowers ANP32A's level | lines that do not express TRIM7 (9) vs lines expressing it (41) | 1.11× higher at baseline in the lines without TRIM7 | 0.073 | ⚠ within organs, on part of the lines; also absent: IRAK2, A4GALT, PAPSS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-16.6, -21.5); signed map (-10.6, -35.0). **Vector** length 134, 47.7% of its response variance represented; |z| ≥ 3 in 1,195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.0 | +17.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.2 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.0 | -18.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.3 | -12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | -6.3 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.9 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.5 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | acidic nuclear phosphoprotein 32 family member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:68,778,535-68,820,897 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LANP, PP32, I1PP2A, PHAPI, MAPM, mapmodulin; previously C15orf1 |
| Gene groups (HGNC) | ANP32 acidic nuclear phosphoproteins; INHAT complex; SET complex; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: HuR (ELAVL1) binds and stabilizes mRNA; Regulation of mRNA stability by proteins that bind AU-rich elements; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P39687](https://www.uniprot.org/uniprotkb/P39687) (Acidic leucine-rich nuclear phosphoprotein 32 family member A):

> Multifunctional protein that is involved in the regulation of many processes including tumor suppression, apoptosis, cell cycle progression or transcription. Promotes apoptosis by favouring the activation of caspase-9/CASP9 and allowing apoptosome formation. In addition, plays a role in the modulation of histone acetylation and transcription as part of the INHAT (inhibitor of histone acetyltransferases) complex. Inhibits the histone-acetyltransferase activity of EP300/CREBBP (CREB-binding …

**Summary**, from NCBI Gene [8125](https://www.ncbi.nlm.nih.gov/gene/8125):

> Enables RNA binding activity. Involved in nucleocytoplasmic transport. Located in several cellular components, including endoplasmic reticulum; nucleoplasm; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13233) · Entrez [8125](https://www.ncbi.nlm.nih.gov/gene/8125) · UniProt [P39687](https://www.uniprot.org/uniprotkb/P39687) · Ensembl [ENSG00000140350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140350)

## Data

Gene col 6393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6393); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6393]; `tensor/DDL_lfc|DDL_z.npy` [6393]; `embed/gene_vectors.npy` [6393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6393 or target_col == 6393). Every well: [[ANP32A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANP32A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
