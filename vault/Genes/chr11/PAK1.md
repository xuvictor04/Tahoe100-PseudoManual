---
symbol: "PAK1"
type: "gene"
col: 7358
ensembl_id: "ENSG00000149269"
name: "p21 (RAC1) activated kinase 1"
location: "11q13.5-q14.1"
module: 61
arm: "+"
pooled_cpm: 99.33
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PAK1

*p21 (RAC1) activated kinase 1* — 11q13.5-q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +12.5, q 3e-33, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 3.49×, A-172 2.17×, NCI-H460 2.59×, A-427 1.90×, …); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 2.31×, A-427 2.03×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (COLO 205 5.83×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 1.71×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.561× (z -17.2, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOGA3]] (+0.52, fdr 2e-05), [[CCDC136]] (+0.52, fdr 7e-05), [[DOCK3]] (+0.52, fdr 4e-05); moves opposite to [[PDCD6]] (-0.44, fdr 1e-04), [[BCKDHA]] (-0.44, fdr 4e-04), [[IFT140]] (-0.44, fdr 2e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EBF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7358.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 3.49×, A-172 2.17×, NCI-H460 2.59×, A-427 1.90×, …); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 2.31×, A-427 2.03×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (COLO 205 5.83×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 1.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +12.5 | 3e-33 | 28/47 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +6.4 | 4e-08 | 24/48 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +4.8 | 3e-04 | 18/47 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +4.4 | 0.001 | 13/47 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +4.3 | 0.002 | 12/47 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.2 | 0.002 | 13/47 (LoVo, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.2 | 0.002 | 19/47 (NCI-H1573, A-427, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.14× | +3.9 | 0.007 | 13/47 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.014 | 11/46 (SW480, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.13× | +3.5 | 0.027 | 15/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.4 | 0.031 | 3/47 (SW 900, HCT15, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.12× | +3.2 | 0.056 | 15/46 (NCI-H23, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.11× | +3.2 | 0.056 | 13/47 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +3.2 | 0.064 | 9/48 (CFPAC-1, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.561×** | -17.2 | 0e+00 | 35/47 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -16.6 | 0e+00 | 36/47 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.714×** | -10.0 | 3e-21 | 30/47 (SW480, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.793×** | -9.8 | 2e-20 | 33/48 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.717×** | -9.5 | 3e-19 | 27/43 (LS 180, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.710×** | -9.4 | 5e-19 | 29/44 (C32, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.739×** | -9.0 | 2e-17 | 31/48 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.756×** | -8.0 | 9e-14 | 28/47 (SW480, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.765×** | -7.7 | 1e-12 | 24/46 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.783×** | -7.0 | 2e-10 | 27/49 (Panc 03.27, LS 180, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | **0.817×** | -6.0 | 9e-08 | 24/47 (NCI-H2347, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.895× | -4.7 | 1e-04 | 9/47 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.742×** | -4.6 | 1e-04 | 17/36 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.861× | -4.3 | 8e-04 | 9/48 (NCI-H2347, KATO III, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.777×** | -3.9 | 0.003 | 20/47 (NCI-H23, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.882× | -3.7 | 0.007 | 16/47 (LoVo, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.894× | -3.3 | 0.027 | 11/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.900× | -3.1 | 0.052 | 12/47 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.904× | -3.0 | 0.076 | 13/47 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.827×** | -3.0 | 0.082 | 7/48 (NCI-H23, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.466× (z -11.2) |
| [[COLO 205 (line)]] | alt | 155 | 4 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.246× (z -15.2) |
| [[LoVo (line)]] | wt | 153 | 3 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -13.6) |
| [[LS 180 (line)]] | wt | 181 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.355× (z -15.0) |
| [[A-427 (line)]] | wt | 164 | 3 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.395× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 6 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.154× (z -12.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 134 | 2 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.31× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.477× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 88.1 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.359× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.408× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 103 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0831× (z -31.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.348× (z -13.3) |
| [[SW480 (line)]] | alt | 106 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -20.5) |
| [[A-172 (line)]] | wt | 119 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +17.2) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SW1417 (line)]] | alt | 84.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -16.6) |
| [[C32 (line)]] | wt | 118 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.572× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.562× (z -10.0) |
| [[SHP-77 (line)]] | alt | 82.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.382× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 145 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -16.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[Hs 766T (line)]] | wt | 87.7 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.223× (z -10.4) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.533× (z -8.6) |
| [[HS-578T (line)]] | alt | 82.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.430× (z -9.8) |
| [[HT-29 (line)]] | alt | 183 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.535× (z -9.6) |
| [[J82 (line)]] | alt | 112 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.537× (z -9.9) |
| [[KATO III (line)]] | alt | 230 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 60.4 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.467× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.474× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 37.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.5) | — |
| [[RKO (line)]] | wt | 146 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.508× (z -9.4) |
| [[SW 900 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 100 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.4) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A498 (line)]] | wt | 76.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 78.9 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.71× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 71.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -8.9) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HepG2_C3A (line)]] | wt | 68.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 75.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.52× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 70.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.492× (z -8.5) |
| [[SNU-423 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.2) | — |
| [[A549 (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOGA3]] | +0.52 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CCDC136]] | +0.52 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[DOCK3]] | +0.52 | +0.40 / +0.44 | both halves | 4e-05 | pathway: RAC1 GTPase cycle |
| [[KIAA0408]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[MARK1]] | +0.52 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[MAP4K5]] | +0.51 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[ELAPOR2]] | +0.50 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[DENND1B]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[MYO6]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 | pathway: RHOU GTPase cycle; STRING 928 |
| [[BACH2]] | +0.49 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[FAM171B]] | +0.49 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[LGALSL]] | +0.48 | +0.38 / +0.43 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[BCKDHA]] | -0.44 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[IFT140]] | -0.44 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[NDUFV1]] | -0.40 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[PMPCA]] | -0.40 | -0.34 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | EBF4 activity lowers PAK1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.56× higher at baseline in the lines without EBF4 | 0.062 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[LINC00857]] | B | LINC00857 activity raises PAK1's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without LINC00857 | 0.064 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |
| [[NDRG4]] | B | NDRG4 activity lowers PAK1's level | lines that do not express NDRG4 (10) vs lines expressing it (40) | 1.58× higher at baseline in the lines without NDRG4 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, SMARCA1, ZNF606; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PAK1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, 34.8); signed map (29.5, 25.0). **Vector** length 86.6, 18.3% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +7.7 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.8 | -9.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +12.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | p21 (RAC1) activated kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5-q14.1 — chr11:77,322,017-77,474,635 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | p21 (RAC1) activated kinase family |
| Hallmark sets | APOPTOSIS |
| Reactome | 52 pathways, smallest: CD28 dependent Vav1 pathway; Activation of RAC1; G beta:gamma signalling through CDC42 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13153](https://www.uniprot.org/uniprotkb/Q13153) (Serine/threonine-protein kinase PAK 1):

> Protein kinase involved in intracellular signaling pathways downstream of integrins and receptor-type kinases that plays an important role in cytoskeleton dynamics, in cell adhesion, migration, proliferation, apoptosis, mitosis, and in vesicle-mediated transport processes. Can directly phosphorylate BAD and protects cells against apoptosis (By similarity). Activated by interaction with CDC42 and RAC1. Functions as a GTPase effector that links the Rho-related GTPases CDC42 and RAC1 to the JNK …

**Summary**, from NCBI Gene [5058](https://www.ncbi.nlm.nih.gov/gene/5058):

> This gene encodes a family member of serine/threonine p21-activating kinases, known as PAK proteins. These proteins are critical effectors that link RhoGTPases to cytoskeleton reorganization and nuclear signaling, and they serve as targets for the small GTP binding proteins Cdc42 and Rac. This specific family member regulates cell motility and morphology. Mutations in this gene have been associated with macrocephaly, seizures, and speech delay. Overexpression of this gene is also reported in …

**Accessions** — [HGNC:8590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8590) · Entrez [5058](https://www.ncbi.nlm.nih.gov/gene/5058) · UniProt [Q13153](https://www.uniprot.org/uniprotkb/Q13153) · Ensembl [ENSG00000149269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149269)

## Data

Gene col 7358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7358); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7358]; `tensor/DDL_lfc|DDL_z.npy` [7358]; `embed/gene_vectors.npy` [7358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7358 or target_col == 7358). Every well: [[PAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
