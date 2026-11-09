---
symbol: "ANAPC5"
type: "gene"
col: 1564
ensembl_id: "ENSG00000089053"
name: "anaphase promoting complex subunit 5"
location: "12q24.31"
module: 57
arm: "+"
pooled_cpm: 108.88
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ANAPC5

*anaphase promoting complex subunit 5* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +22.3, q 0e+00, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.65× (z +11.1, q 1e-26, up in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HEC-1-A 7.23×, LoVo 8.48×, J82 6.46×, SHP-77 6.44×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 6 lines (SW480 2.30×, LoVo 2.75×, HEC-1-A 2.03×, NCI-H1573 2.40×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (KATO III 6.88×, LoVo 6.77×, HEC-1-A 4.60×, J82 3.94×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 2.06×, LoVo 2.19×, HEC-1-A 1.85×, A-427 2.09×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.644× (z -13.7, q 3e-40, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP1]] (+0.73, fdr 7e-06), [[GK5]] (+0.69, fdr 7e-06), [[NUDT21]] (+0.68, fdr 1e-05); moves opposite to [[CCDC90B-AS1]] (-0.65, fdr 1e-05), [[MAD2L1BP]] (-0.65, fdr 1e-05), [[ADNP2]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1564.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (HEC-1-A 7.23×, LoVo 8.48×, J82 6.46×, SHP-77 6.44×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 6 lines (SW480 2.30×, LoVo 2.75×, HEC-1-A 2.03×, NCI-H1573 2.40×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (KATO III 6.88×, LoVo 6.77×, HEC-1-A 4.60×, J82 3.94×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 2.06×, LoVo 2.19×, HEC-1-A 1.85×, A-427 2.09×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +22.3 | 0e+00 | 41/44 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +21.3 | 0e+00 | 45/49 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +12.1 | 2e-31 | 37/45 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +11.1 | 1e-26 | 40/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +8.8 | 2e-16 | 42/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +6.3 | 4e-08 | 32/48 (SW480, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.31×** | +5.9 | 4e-07 | 35/47 (CFPAC-1, J82, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.7 | 0.017 | 18/49 (SW 900, RKO, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.16× | +3.4 | 0.046 | 11/49 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +3.1 | 0.096 | 5/49 (SW1417, RKO, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.1 | 0.11 | 5/48 (C32, CHP-212, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.10× | +3.0 | 0.11 | 9/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -13.7 | 3e-40 | 38/49 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.667×** | -12.7 | 3e-34 | 36/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -11.2 | 5e-27 | 41/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -10.3 | 1e-22 | 43/48 (SW480, SW 1271, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -9.3 | 1e-18 | 37/48 (HS-578T, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -8.6 | 8e-16 | 34/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -8.5 | 1e-15 | 31/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -7.2 | 5e-11 | 34/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.723×** | -7.2 | 5e-11 | 37/48 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.724×** | -7.1 | 6e-11 | 31/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.757×** | -6.1 | 4e-08 | 30/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.5 | 3e-04 | 24/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.838× | -3.9 | 0.005 | 19/48 (LoVo, A-172, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.724×** | -3.7 | 0.008 | 22/48 (NCI-H2347, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.6 | 0.010 | 21/48 (C32, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.021 | 22/49 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.856× | -3.4 | 0.022 | 17/48 (A-172, C32, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.897× | -3.4 | 0.023 | 9/48 (AsPC-1, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 113 | 2 (2 ⚠) | 10 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.19× (z +11.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -17.9) |
| [[C32 (line)]] | wt | 135 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.92× (z +12.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 107 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.51× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -16.8) |
| [[LoVo (line)]] | wt | 145 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 8.48× (z +25.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.75× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -13.1) |
| [[SW480 (line)]] | alt | 140 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.30× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -12.6) |
| [[A-172 (line)]] | wt | 79.9 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.6) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.285× (z -15.2) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 98.2 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.23× (z +26.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.03× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 126 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -15.4) |
| [[HS-578T (line)]] | alt | 128 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -17.8) |
| [[KATO III (line)]] | alt | 84.2 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +23.5) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.463× (z -9.4) |
| [[SW1417 (line)]] | alt | 141 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +14.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -11.8) |
| [[A498 (line)]] | wt | 177 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -22.8) |
| [[HOP62 (line)]] | alt | 74.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.02× (z +15.7) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.459× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 87.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 84.6 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.26× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 62.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +17.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 122 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.3) |
| [[SHP-77 (line)]] | alt | 187 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.44× (z +22.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -8.6) |
| [[SNU-1 (line)]] | wt | 110 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -9.5) |
| [[A-427 (line)]] | wt | 84.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -14.8) |
| [[BT-474 (line)]] | alt | 79.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 62.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +15.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -9.4) |
| [[J82 (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.46× (z +25.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 75.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 69.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 94.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +19.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 87.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.75× (z +16.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +12.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 97.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +13.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +16.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 67.2 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 111 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.3) |
| [[RKO (line)]] | wt | 87.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.7) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.391× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -13.2) |
| [[A549 (line)]] | wt | 93.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.50× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 86.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -9.2) |
| [[COLO 205 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 122 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 80.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.326× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.539× (z -8.7) |
| [[SW 1271 (line)]] | alt | 128 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.151× (z -9.6) |
| [[SW48 (line)]] | wt | 176 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.407× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | +0.73 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[GK5]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NUDT21]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[POT1]] | +0.68 | +0.69 / +0.52 | both halves | 1e-05 | pathway: Cellular Senescence |
| [[ANAPC4]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 | same gene group; pathway: APC-Cdc20 mediated degradation of Nek2A; STRING 999 |
| [[MRPS31P5-1]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.67 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[RPA1]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[METTL17]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PRMT7]] | +0.65 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[MSTO2P]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | -0.65 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MAD2L1BP]] | -0.65 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ADNP2]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[LINC02516]] | -0.63 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[RNF103-CHMP3]] | -0.62 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TSC22D1]] | -0.62 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TRIM69]] | -0.62 | -0.56 / -0.51 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TAF7]] | -0.61 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[RBBP6]] | -0.61 | -0.53 / -0.50 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MZF1-AS1]] | -0.61 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[FBXL19-AS1]] | -0.61 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[FAM131B-AS2]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ANAPC5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.3, -13.8); signed map (-38.1, -14.8). **Vector** length 143, 46.9% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +11.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.8 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.7 | +8.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | -0.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.1 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.6 | -13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.7 | -10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.1 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,308,245-121,399,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APC5 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJX4](https://www.uniprot.org/uniprotkb/Q9UJX4) (Anaphase-promoting complex subunit 5):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [51433](https://www.ncbi.nlm.nih.gov/gene/51433):

> This gene encodes a tetratricopeptide repeat-containing component of the anaphase promoting complex/cyclosome (APC/C), a large E3 ubiquitin ligase that controls cell cycle progression by targeting a number of cell cycle regulators such as B-type cyclins for 26S proteasome-mediated degradation through ubiquitination. The encoded protein is required for the proper ubiquitination function of APC/C and for the interaction of APC/C with transcription coactivators. It also interacts with polyA …

**Accessions** — [HGNC:15713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15713) · Entrez [51433](https://www.ncbi.nlm.nih.gov/gene/51433) · UniProt [Q9UJX4](https://www.uniprot.org/uniprotkb/Q9UJX4) · Ensembl [ENSG00000089053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089053)

## Data

Gene col 1564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1564); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1564]; `tensor/DDL_lfc|DDL_z.npy` [1564]; `embed/gene_vectors.npy` [1564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1564 or target_col == 1564). Every well: [[ANAPC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
