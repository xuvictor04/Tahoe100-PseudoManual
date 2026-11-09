---
symbol: "WIPF2"
type: "gene"
col: 10117
ensembl_id: "ENSG00000171475"
name: "WAS/WASL interacting protein family member 2"
location: "17q21.2"
module: 3
arm: "+"
pooled_cpm: 186.06
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# WIPF2

*WAS/WASL interacting protein family member 2* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +12.4, q 2e-32, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.447× (z -20.6, q 0e+00, down in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.666× (z -11.2, q 7e-27, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 0.221×, SK-MEL-2 0.183×, CFPAC-1 0.227×, A-427 0.281×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 6 lines (HOP62 0.443×, SNU-423 0.526×, A-172 0.538×, LOX-IMVI 0.524×, …); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (CFPAC-1 0.231×, NCI-H2347 0.278×, A-427 0.254×, HOP62 0.313×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.286×); [[Bimiralisib (drug)]] 5 µM in 1 line (NCI-H596 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2D]] (+0.76, fdr 7e-06), [[LAGE3]] (+0.70, fdr 1e-05), [[RNF114]] (+0.69, fdr 1e-05); moves opposite to [[TMX3]] (-0.73, fdr 7e-06), [[NAA50]] (-0.66, fdr 1e-05), [[ILF3]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +12.4 | 2e-32 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +9.4 | 1e-18 | 37/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +8.5 | 3e-15 | 35/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +8.4 | 8e-15 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +6.8 | 9e-10 | 31/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +5.0 | 6e-05 | 28/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.13× | +4.8 | 1e-04 | 21/48 (PANC-1, A498, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +4.5 | 5e-04 | 17/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.1 | 0.002 | 19/48 (SW480, RKO, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +4.0 | 0.003 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.015 | 18/48 (J82, SW480, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.017 | 7/49 (NCI-H2030, HOP62, …) | rises with dose | plate-row cell shift |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.09× | +3.5 | 0.020 | 0/48 | top dose only |  |
| [[Bergenin (drug)]] 5 µM |  | 1.08× | +3.2 | 0.057 | 0/49 | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +3.2 | 0.060 | 7/49 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.11× | +3.0 | 0.091 | 13/48 (A498, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10117.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 0.221×, SK-MEL-2 0.183×, CFPAC-1 0.227×, A-427 0.281×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 6 lines (HOP62 0.443×, SNU-423 0.526×, A-172 0.538×, LOX-IMVI 0.524×, …); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (CFPAC-1 0.231×, NCI-H2347 0.278×, A-427 0.254×, HOP62 0.313×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.286×); [[Bimiralisib (drug)]] 5 µM in 1 line (NCI-H596 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.447×** | -20.6 | 0e+00 | 44/45 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -20.2 | 0e+00 | 42/44 (Panc 03.27, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.455×** | -16.3 | 0e+00 | 46/49 (CFPAC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.666×** | -11.2 | 7e-27 | 35/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.868× | -5.5 | 5e-06 | 22/49 (CFPAC-1, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.835× | -4.8 | 2e-04 | 22/48 (SNU-423, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.839× | -4.6 | 3e-04 | 22/50 (C32, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | 0.847× | -4.4 | 8e-04 | 18/47 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.856× | -4.3 | 0.001 | 22/48 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.898× | -4.2 | 0.002 | 9/48 (HOP62, A-172, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.759×** | -4.0 | 0.004 | 21/38 (Panc 03.27, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.879× | -3.5 | 0.018 | 5/48 (SW 1088, Panc 03.27, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.876× | -3.4 | 0.026 | 15/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.886× | -3.3 | 0.038 | 10/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.891× | -3.2 | 0.060 | 6/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 227 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.507× (z -9.1) |
| [[PANC-1 (line)]] | alt | 195 | 6 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +17.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.435× (z -14.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 176 | 0 | 8 (7 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.538× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 212 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.524× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 237 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -20.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 160 | 5 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.31× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -17.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 176 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.526× (z -10.4) |
| [[HOP62 (line)]] | alt | 175 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 314 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.96× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -17.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 150 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.506× (z -11.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 459 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -23.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 242 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.57× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.487× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 179 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -16.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 152 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.186× (z -12.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 131 | 3 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.84× (z +9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 183 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.579× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 179 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -16.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 215 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -24.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 187 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.1) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.183× (z -23.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 177 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -20.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 204 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -15.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 220 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -13.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 217 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -19.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 114 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.423× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 201 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -19.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 177 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.6) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.526× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.22× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.02× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 207 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 191 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -15.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 151 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -17.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 148 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -14.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 148 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.96× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.286× (z -9.2) |
| [[SW48 (line)]] | wt | 162 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.60× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -13.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.01× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.49× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 155 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | +0.76 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[LAGE3]] | +0.70 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[RNF114]] | +0.69 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[CNNM4]] | +0.67 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.66 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MCRIP1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.66 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[DENND6B]] | +0.65 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[SEC22A]] | +0.65 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[RPL36AL]] ⚠ | +0.65 | +0.52 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[AFMID]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX3]] | -0.73 | -0.59 / -0.77 | both halves | 7e-06 |  |
| [[NAA50]] | -0.66 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[ILF3]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[DARS2]] | -0.64 | -0.58 / -0.57 | both halves | 8e-06 |  |
| [[MACROH2A1]] | -0.64 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[CCT5]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[IDE]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[IPO5]] | -0.61 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[CCT6A]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.60 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[LARP4]] | -0.60 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-24.0, -30.7); signed map (-27.9, 12.5). **Vector** length 124, 40.2% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.4 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.1 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.5 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | -1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.8 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -20.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | WAS/WASL interacting protein family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,219,304-40,284,136 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WICH, WIRE |
| Reactome | 16 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF74](https://www.uniprot.org/uniprotkb/Q8TF74) (WAS/WASL-interacting protein family member 2):

> Plays an active role in the formation of cell surface protrusions downstream of activated PDGFB receptors. Plays an important role in actin-microspike formation through cooperation with WASL. May cooperate with WASP and WASL to induce mobilization and reorganization of the actin filament system.

**Summary**, from NCBI Gene [147179](https://www.ncbi.nlm.nih.gov/gene/147179):

> This gene encodes a WASP interacting protein (WIP)-related protein. It has been shown that this protein has a role in the WASP-mediated organization of the actin cytoskeleton and that this protein is a potential link between the activated platelet-derived growth factor receptor and the actin polymerization machinery. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30923) · Entrez [147179](https://www.ncbi.nlm.nih.gov/gene/147179) · UniProt [Q8TF74](https://www.uniprot.org/uniprotkb/Q8TF74) · Ensembl [ENSG00000171475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171475)

## Data

Gene col 10117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10117); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10117]; `tensor/DDL_lfc|DDL_z.npy` [10117]; `embed/gene_vectors.npy` [10117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10117 or target_col == 10117). Every well: [[WIPF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WIPF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
