---
symbol: "PPP2R5E"
type: "gene"
col: 7761
ensembl_id: "ENSG00000154001"
name: "protein phosphatase 2 regulatory subunit B'epsilon"
location: "14q23.2"
module: 186
arm: "+"
pooled_cpm: 221.1
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# PPP2R5E

*protein phosphatase 2 regulatory subunit B'epsilon* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.83× (z +18.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.550× (z -15.2, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H23 0.319×, LoVo 0.395×, NCI-H1573 0.271×, C-33 A 0.352×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.410×, A-427 0.430×, Panc 03.27 0.440×, LS 180 0.419×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LS 180 0.404×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPK2]] (+0.73, fdr 8e-06), [[SEC24B]] (+0.73, fdr 7e-06), [[ZMYM2]] (+0.69, fdr 7e-06); moves opposite to [[HUS1]] (-0.72, fdr 7e-06), [[ZNF674]] (-0.65, fdr 1e-05), [[SRSF6]] (-0.61, fdr 1e-05).
> It is in [[Module 186]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.83×** | +18.6 | 0e+00 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +15.4 | 0e+00 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +14.1 | 4e-43 | 43/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +13.1 | 3e-37 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +10.4 | 3e-23 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +9.4 | 7e-19 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +8.9 | 4e-17 | 41/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +7.8 | 3e-13 | 31/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.8 | 3e-13 | 27/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +7.1 | 6e-11 | 34/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.2 | 3e-08 | 28/50 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +5.6 | 1e-06 | 29/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.1 | 1e-05 | 32/45 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.23×** | +5.0 | 2e-05 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.002 | 27/49 (PANC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.068 | 5/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.073 | 12/48 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H23 0.319×, LoVo 0.395×, NCI-H1573 0.271×, C-33 A 0.352×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.410×, A-427 0.430×, Panc 03.27 0.440×, LS 180 0.419×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LS 180 0.404×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -15.2 | 0e+00 | 39/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.645×** | -11.6 | 1e-28 | 41/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.709×** | -8.4 | 6e-15 | 31/45 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.785×** | -6.2 | 1e-07 | 34/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -5.0 | 6e-05 | 20/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -4.7 | 2e-04 | 12/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.840× | -4.6 | 3e-04 | 21/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -4.4 | 7e-04 | 22/48 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -4.2 | 0.002 | 18/48 (HT-29, HepG2/C3A, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.906× | -3.7 | 0.012 | 10/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.873× | -3.6 | 0.017 | 13/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.870× | -3.6 | 0.018 | 15/49 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.875× | -3.5 | 0.019 | 9/47 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.880× | -3.4 | 0.025 | 7/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.880× | -3.4 | 0.025 | 15/49 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.888× | -3.1 | 0.053 | 12/48 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.892× | -3.0 | 0.068 | 8/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.889× | -3.0 | 0.069 | 13/48 (J82, LS 180, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.895× | -2.9 | 0.080 | 5/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.898× | -2.9 | 0.097 | 7/48 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.887× | -2.9 | 0.097 | 16/48 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 199 | 10 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.38× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.664× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 231 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -12.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 155 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +23.5) | — |
| [[NCI-H1573 (line)]] | alt | 217 | 6 (2 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.63× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -18.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 451 | 7 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -21.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 186 | 8 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.29× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.15× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.515× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 204 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -19.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 404 | 3 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.15× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -12.2) ⚠ cell-cycle shift, explains ~10% of this change |
| [[C32 (line)]] | wt | 240 | 2 | 5 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 5.03× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -12.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 229 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -15.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 300 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.37× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -15.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 167 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.89× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 208 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.9) | — |
| [[KATO III (line)]] | alt | 144 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.08× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 239 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 384 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.04× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 289 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.76× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -13.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 257 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.32× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.456× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 280 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.46× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 196 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.17× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.509× (z -10.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 245 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.70× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.517× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 214 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.07× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 258 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.41× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -14.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 137 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +14.7) | — |
| [[HT-29 (line)]] | alt | 145 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.46× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 234 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 350 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.29× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -14.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 233 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.554× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 313 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 287 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.429× (z -10.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 272 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.06× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 236 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 121 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.19× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 256 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -11.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 173 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.78× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 203 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.35× (z +11.3) | — |
| [[A498 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 168 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 197 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 253 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK2]] | +0.73 | +0.79 / +0.58 | both halves | 8e-06 |  |
| [[SEC24B]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[ZMYM2]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[GAPVD1]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[RELCH]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 | same gene group; STRING 473 |
| [[UBE2G1]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[PDE7A]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[BMPR1A]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[AMBRA1]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[GRB2]] | +0.65 | +0.76 / +0.59 | both halves | 7e-06 | pathway: Co-stimulation by CD28 |
| [[CNOT6L]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 | pathway: Intracellular signaling by second messengers |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUS1]] | -0.72 | -0.70 / -0.65 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[ZNF674]] | -0.65 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[SRSF6]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[TFE3]] | -0.61 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[MYSM1]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[FAM83G]] | -0.60 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.59 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[KDM6B]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ZNF554]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[IER2]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.3, -8.4); signed map (-35.4, -7.0). **Vector** length 114, 41.3% of its response variance represented; |z| ≥ 3 in 1,285 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +7.7 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.8 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | -1.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.5 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.6 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B'epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:63,371,364-63,543,377 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B56E, B56epsilon |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits; Armadillo like helical domain containing |
| Reactome | 52 pathways, smallest: APC truncation mutants have impaired AXIN binding; AXIN missense mutants destabilize the destruction complex; Signaling by AMER1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16537](https://www.uniprot.org/uniprotkb/Q16537) (Serine/threonine-protein phosphatase 2A 56 kDa regulatory subunit epsilon isoform):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment.

**Summary**, from NCBI Gene [5529](https://www.ncbi.nlm.nih.gov/gene/5529):

> The protein encoded by this gene belongs to the phosphatase 2A regulatory subunit B family. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic …

**Accessions** — [HGNC:9313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9313) · Entrez [5529](https://www.ncbi.nlm.nih.gov/gene/5529) · UniProt [Q16537](https://www.uniprot.org/uniprotkb/Q16537) · Ensembl [ENSG00000154001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154001)

## Data

Gene col 7761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7761); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7761]; `tensor/DDL_lfc|DDL_z.npy` [7761]; `embed/gene_vectors.npy` [7761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7761 or target_col == 7761). Every well: [[PPP2R5E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R5E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
