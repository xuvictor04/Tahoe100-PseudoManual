---
symbol: "FRYL"
type: "gene"
col: 1123
ensembl_id: "ENSG00000075539"
name: "FRY like transcription coactivator"
location: "4p11"
module: 1
arm: "-"
pooled_cpm: 241.2
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FRYL

*FRY like transcription coactivator* — 4p11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +11.8, q 3e-29, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.422× (z -19.3, q 0e+00, down in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.789× (z -5.7, q 9e-07, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.273×, SW480 0.354×, LoVo 0.326×, AsPC-1 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0485×, C-33 A 0.0470×, AsPC-1 0.190×, NCI-H23 0.262×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H460 0.316×, NCI-H1792 0.286×, Panc 03.27 0.277×, SW480 0.352×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.514×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HCT15 0.620×); [[Simotinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0922×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF2]] (+0.59, fdr 1e-05), [[WWC2]] (+0.56, fdr 1e-05), [[TEAD1]] (+0.53, fdr 2e-05); moves opposite to [[RRN3P1]] (-0.56, fdr 2e-05), [[TIGD1]] (-0.49, fdr 3e-05), [[SHLD1]] (-0.48, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +11.8 | 3e-29 | 34/48 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +11.4 | 9e-28 | 45/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +9.3 | 2e-18 | 44/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +8.6 | 1e-15 | 38/48 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +7.9 | 2e-13 | 40/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +6.5 | 8e-09 | 38/48 (SW 900, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +6.2 | 3e-08 | 28/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.8 | 4e-07 | 34/48 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 1e-06 | 32/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.3 | 7e-06 | 25/50 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.7 | 1e-04 | 27/48 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 21/47 (SW 900, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +3.9 | 0.004 | 19/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.047 | 10/47 (C32, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.063 | 17/48 (A-427, RKO, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.065 | 23/49 (C-33 A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.1 | 0.068 | 7/48 (A498, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.273×, SW480 0.354×, LoVo 0.326×, AsPC-1 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0485×, C-33 A 0.0470×, AsPC-1 0.190×, NCI-H23 0.262×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H460 0.316×, NCI-H1792 0.286×, Panc 03.27 0.277×, SW480 0.352×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.514×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HCT15 0.620×); [[Simotinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0922×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.422×** | -19.3 | 0e+00 | 44/45 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.500×** | -16.7 | 0e+00 | 48/49 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -16.2 | 0e+00 | 43/44 (SK-MEL-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -11.9 | 2e-30 | 46/47 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.788×** | -5.8 | 9e-07 | 33/48 (SW 900, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.789×** | -5.7 | 9e-07 | 32/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.700×** | -4.0 | 0.006 | 21/38 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.899× | -3.6 | 0.025 | 18/49 (NCI-H1792, A549, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.879× | -3.1 | 0.12 | 8/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.881× | -3.1 | 0.13 | 10/48 (SW48, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 253 | 4 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.514× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 211 | 5 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -19.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 281 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -18.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 225 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +23.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.468× (z -10.3) ⚠ toxic |
| [[A498 (line)]] | wt | 202 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -13.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 359 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -16.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 248 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -19.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 248 | 3 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 295 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -17.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 199 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +25.7) | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -13.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 227 | 2 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -13.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 300 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -21.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 311 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -23.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 219 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 260 | 1 | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -15.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 280 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -19.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 185 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -13.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 242 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -16.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 165 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -12.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 241 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -16.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 352 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 270 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -21.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 196 | 1 | 3 (3 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -20.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 238 | 1 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -15.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 279 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0470× (z -41.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 330 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 316 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.620× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 245 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -16.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 198 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 372 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.472× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 279 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.378× (z -12.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0485× (z -43.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -15.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 282 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -8.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 152 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 179 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.543× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 197 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 212 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.0) | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 2 | — | [[Simotinib (drug)]] 0.05 µM 0.0922× (z -8.8) |
| [[A549 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 241 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -17.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 297 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF2]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[WWC2]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TEAD1]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[FER]] | +0.53 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SRGAP2]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PRKCA]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ITSN1]] | +0.49 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MAGI3]] | +0.49 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[LARGE1]] | +0.49 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[RASA1]] | +0.49 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[ATXN1]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ZSWIM6]] | +0.47 | +0.43 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRN3P1]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TIGD1]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SHLD1]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZNF70]] | -0.48 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[C3orf33]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[PARL]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[PYROXD1]] | -0.46 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[RBM4B]] | -0.46 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[GSTM2]] | -0.46 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[PMS2P3]] | -0.46 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[TIPIN]] | -0.45 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[PGAP3]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.210). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.0, 14.9); signed map (-15.0, 30.2). **Vector** length 104, 36.4% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.3 | +11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +8.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.1 | +6.5 |
|  | [[Thymol (drug)]] 5 µM |  | +2.8 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Busulfan (drug)]] 5 µM |  | +2.5 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.3 | -11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -19.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.6 | -5.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.2 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | FRY like transcription coactivator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p11 — chr4:48,497,357-48,780,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686E205, AF4p12, MOR2; previously KIAA0826 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O94915](https://www.uniprot.org/uniprotkb/O94915) (Protein furry homolog-like):

> Plays a key role in maintaining the integrity of polarized cell extensions during morphogenesis, regulates the actin cytoskeleton and plays a key role in patterning sensory neuron dendritic fields by promoting avoidance between homologous dendrites as well as by limiting dendritic branching (By similarity). May function as a transcriptional activator.

**Summary**, from NCBI Gene [285527](https://www.ncbi.nlm.nih.gov/gene/285527):

> Predicted to be involved in cell morphogenesis and neuron projection development. Predicted to be active in cell cortex and site of polarized growth. Implicated in Pan-Chung-Bellen syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29127) · Entrez [285527](https://www.ncbi.nlm.nih.gov/gene/285527) · UniProt [O94915](https://www.uniprot.org/uniprotkb/O94915) · Ensembl [ENSG00000075539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075539)

## Data

Gene col 1123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1123); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1123]; `tensor/DDL_lfc|DDL_z.npy` [1123]; `embed/gene_vectors.npy` [1123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1123 or target_col == 1123). Every well: [[FRYL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRYL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
