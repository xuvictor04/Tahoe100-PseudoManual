---
symbol: "THRAP3"
type: "gene"
col: 601
ensembl_id: "ENSG00000054118"
name: "thyroid hormone receptor associated protein 3"
location: "1p34.3"
module: 16
arm: "+"
pooled_cpm: 203.31
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# THRAP3

*thyroid hormone receptor associated protein 3* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.45× (z +22.3, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.689× (z -16.5, q 0e+00, down in 41 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.430×, CFPAC-1 0.518×, A498 0.501×, AsPC-1 0.531×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.329×, CFPAC-1 0.485×, MIA PaCa-2 0.494×; ⚠ toxic; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.321×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACIN1]] (+0.61, fdr 7e-06), [[PRPF6]] (+0.60, fdr 3e-05), [[HNRNPD]] (+0.60, fdr 1e-05); moves opposite to [[METTL21A]] (-0.59, fdr 1e-05), [[DGKE]] (-0.57, fdr 3e-05), [[HPRT1]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.45×** | +22.3 | 0e+00 | 48/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.50×** | +17.8 | 0e+00 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.65×** | +17.5 | 0e+00 | 48/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +13.0 | 2e-36 | 42/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.42×** | +12.1 | 1e-31 | 38/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +10.2 | 3e-22 | 38/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +9.4 | 3e-19 | 0/50 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.21×** | +6.6 | 4e-09 | 25/49 (NCI-H23, A-172, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.18× | +5.7 | 7e-07 | 20/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.36×** | +5.6 | 1e-06 | 35/47 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +4.7 | 1e-04 | 25/49 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.13× | +4.3 | 7e-04 | 17/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.14× | +4.3 | 7e-04 | 17/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +4.3 | 7e-04 | 18/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.3 | 8e-04 | 18/38 (A-427, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[BI-3406 (drug)]] 0.05 µM |  | 1.11× | +3.4 | 0.026 | 3/49 (RPMI-7951, COLO 205, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.09× | +3.1 | 0.055 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 601.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.430×, CFPAC-1 0.518×, A498 0.501×, AsPC-1 0.531×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.329×, CFPAC-1 0.485×, MIA PaCa-2 0.494×; ⚠ toxic; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.321×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -16.5 | 0e+00 | 41/49 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.825×** | -8.6 | 2e-15 | 28/48 (LS 180, RKO, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.796×** | -7.6 | 7e-12 | 27/48 (H4, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.821×** | -6.8 | 2e-09 | 26/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -5.8 | 8e-07 | 21/48 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.843× | -5.7 | 1e-06 | 22/47 (RKO, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.850× | -5.6 | 2e-06 | 23/48 (A549, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.848× | -5.4 | 4e-06 | 23/50 (LS 180, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.881× | -4.4 | 8e-04 | 11/48 (J82, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.893× | -3.9 | 0.005 | 12/49 (SW480, CHP-212, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.905× | -3.4 | 0.030 | 1/49 (CHP-212) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.926× | -3.2 | 0.055 | 2/48 (RKO, HEC-1-A) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | 0.839× | -3.2 | 0.067 | 12/48 (HCT15, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 263 | 7 (5 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.05× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -13.9) |
| [[PANC-1 (line)]] | alt | 211 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +18.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.36× (z +16.1) | — |
| [[LS 180 (line)]] | wt | 194 | 5 (3 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.71× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 219 | 6 (3 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.63× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -14.0) |
| [[LoVo (line)]] | wt | 203 | 5 (3 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.78× (z +21.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 176 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.76× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 171 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.49× (z +13.2) | — |
| [[A549 (line)]] | wt | 175 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.91× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -17.5) |
| [[HOP62 (line)]] | alt | 211 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.96× (z +10.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.3) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -10.7) |
| [[HS-578T (line)]] | alt | 233 | 4 (2 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 3.59× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 249 | 4 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +13.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.494× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 208 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.00× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.550× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 195 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.43× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SNU-423 (line)]] | alt | 199 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.38× (z +11.3) | — |
| [[SW48 (line)]] | wt | 219 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.6) ⚠ cell-cycle shift, explains ~24% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.7) |
| [[C32 (line)]] | wt | 143 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.60× (z +10.1) | — |
| [[H4 (line)]] | wt | 221 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.25× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.0) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 191 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.76× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 147 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 3.50× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -11.0) |
| [[RKO (line)]] | wt | 211 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.23× (z +14.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.329× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.2) |
| [[SW480 (line)]] | alt | 223 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.85× (z +18.4) | — |
| [[A498 (line)]] | wt | 251 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -16.7) |
| [[BT-474 (line)]] | alt | 171 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.31× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 209 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.39× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -16.8) |
| [[Hs 766T (line)]] | wt | 252 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.36× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 197 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 3.45× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.8) |
| [[J82 (line)]] | alt | 257 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.73× (z +10.0) | — |
| [[KATO III (line)]] | alt | 178 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.90× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 233 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.17× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -9.3) |
| [[SW1417 (line)]] | alt | 155 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.40× (z +11.4) | — |
| [[A-172 (line)]] | wt | 143 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 245 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.62× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 172 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.7× (z +16.7) | — |
| [[HCT15 (line)]] | alt | 311 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.46× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 189 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.62× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.581× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 186 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.97× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 196 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -14.8) |
| [[C-33 A (line)]] | alt | 260 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.09× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 173 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.52× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 151 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.14× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 188 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.88× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 218 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 181 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACIN1]] | +0.61 | +0.62 / +0.67 | both halves | 7e-06 | STRING 606 |
| [[PRPF6]] | +0.60 | +0.70 / +0.44 | both halves | 3e-05 | STRING 469 |
| [[HNRNPD]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[RNF40]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[KAT5]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[DDX23]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PBRM1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[C2CD5]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ZNF644]] | +0.57 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ZNF180]] | +0.56 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[BMS1]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZMYM4]] | +0.55 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL21A]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[DGKE]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[HPRT1]] | -0.57 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[MOB1B]] | -0.56 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[PAQR3]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MID2]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[FAM89A]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[DHX32]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ISCA1]] | -0.51 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[SLC41A1]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[LHX1-DT]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.9, -1.3); signed map (-11.2, -28.4). **Vector** length 124, 37.8% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.3 | +22.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.2 | +17.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.1 | +17.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.8 | +12.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.0 | +10.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +4.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -16.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -5.6 | -7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.4 | -8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | -5.2 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.9 | -6.8 |
|  | [[Infigratinib (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | +0.0 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:36,224,432-36,305,357 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRAP150, BCLAF2 |
| Gene groups (HGNC) | WTAP complex; Spliceosomal A complex |
| Reactome | 5 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; Adipogenesis; PPARA activates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2W1](https://www.uniprot.org/uniprotkb/Q9Y2W1) (Thyroid hormone receptor-associated protein 3):

> Involved in pre-mRNA splicing. Remains associated with spliced mRNA after splicing which probably involves interactions with the exon junction complex (EJC). Can trigger mRNA decay which seems to be independent of nonsense-mediated decay involving premature stop codons (PTC) recognition. May be involved in nuclear mRNA decay. Involved in regulation of signal-induced alternative splicing. During splicing of PTPRC/CD45 is proposed to sequester phosphorylated SFPQ from PTPRC/CD45 pre-mRNA in …

**Summary**, from NCBI Gene [9967](https://www.ncbi.nlm.nih.gov/gene/9967):

> Enables nuclear thyroid hormone receptor binding activity; phosphoprotein binding activity; and transcription coactivator activity. Involved in positive regulation of circadian rhythm and regulation of gene expression. Acts upstream of or within positive regulation of transcription by RNA polymerase II. Located in exon-exon junction complex and nuclear speck. Part of mediator complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22964) · Entrez [9967](https://www.ncbi.nlm.nih.gov/gene/9967) · UniProt [Q9Y2W1](https://www.uniprot.org/uniprotkb/Q9Y2W1) · Ensembl [ENSG00000054118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054118)

## Data

Gene col 601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 601); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 601]; `tensor/DDL_lfc|DDL_z.npy` [601]; `embed/gene_vectors.npy` [601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 601 or target_col == 601). Every well: [[THRAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THRAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
