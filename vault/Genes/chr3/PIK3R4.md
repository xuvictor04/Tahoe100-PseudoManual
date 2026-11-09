---
symbol: "PIK3R4"
type: "gene"
col: 12209
ensembl_id: "ENSG00000196455"
name: "phosphoinositide-3-kinase regulatory subunit 4"
location: "3q22.1"
module: 36
arm: "+"
pooled_cpm: 49.36
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PIK3R4

*phosphoinositide-3-kinase regulatory subunit 4* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.77× (z +20.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.616× (z -9.9, q 2e-20, down in 31 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.766× (z -3.8, q 0.014, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.0756×, NCI-H23 0.165×, HT-29 0.130×, NCI-H1792 0.173×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.321×, RKO 0.193×, NCI-H2030 0.263×, LOX-IMVI 0.264×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.234×, RKO 0.227×, C32 0.219×; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (H4 0.114×); [[Futibatinib (drug)]] 5 µM in 1 line (Hs 766T 0.0900×); [[Malotilate (drug)]] 0.05 µM in 1 line (AN3 CA 0.152×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AREL1]] (+0.66, fdr 7e-06), [[PARGP1]] (+0.64, fdr 7e-06), [[ATP5PF]] (+0.63, fdr 4e-05); moves opposite to [[JUN]] (-0.58, fdr 1e-05), [[TFE3]] (-0.55, fdr 2e-05), [[JUND]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +20.9 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +20.0 | 0e+00 | 48/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.33×** | +17.2 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +16.6 | 0e+00 | 42/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.94×** | +14.7 | 0e+00 | 44/49 (LoVo, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.99×** | +11.7 | 1e-29 | 40/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +9.5 | 3e-19 | 31/48 (SW1417, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.49×** | +7.8 | 5e-13 | 32/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +7.6 | 2e-12 | 34/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +6.9 | 3e-10 | 33/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +6.9 | 4e-10 | 29/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +6.2 | 4e-08 | 27/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +5.2 | 7e-06 | 27/48 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +5.1 | 1e-05 | 28/48 (RKO, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.7 | 8e-05 | 24/47 (H4, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.003 | 17/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12209.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.0756×, NCI-H23 0.165×, HT-29 0.130×, NCI-H1792 0.173×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.321×, RKO 0.193×, NCI-H2030 0.263×, LOX-IMVI 0.264×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.234×, RKO 0.227×, C32 0.219×; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (H4 0.114×); [[Futibatinib (drug)]] 5 µM in 1 line (Hs 766T 0.0900×); [[Malotilate (drug)]] 0.05 µM in 1 line (AN3 CA 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.616×** | -9.9 | 2e-20 | 31/48 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -9.3 | 5e-18 | 25/43 (Panc 03.27, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -8.4 | 7e-15 | 29/45 (NCI-H2030, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.758×** | -5.7 | 2e-06 | 26/47 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.2 | 0.004 | 1/49 (AN3 CA) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.014 | 20/48 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.834× | -3.7 | 0.016 | 21/48 (NCI-H2347, HEC-1-A, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.15 | 7/48 (PANC-1, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.901× | -3.0 | 0.15 | 14/48 (HEC-1-A, CFPAC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 53.6 | 8 (2 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -15.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 63.8 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -10.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 70.5 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 67.5 | 4 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.89× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -11.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 44.8 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 36.3 | 5 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +11.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 49.5 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 8.75× (z +10.9) | — |
| [[RKO (line)]] | wt | 50.8 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.68× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 56.8 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.98× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 40.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.47× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -12.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 42.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.1 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 78.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -19.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 50.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 75.5 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 35.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.9) | — |
| [[A498 (line)]] | wt | 44.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +12.8) | — |
| [[C32 (line)]] | wt | 41.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -12.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 32.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +13.9) | — |
| [[H4 (line)]] | wt | 38.4 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.94× (z +9.2) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.114× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 35.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +13.6) | — |
| [[SW1417 (line)]] | alt | 74.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 99.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 28.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Malotilate (drug)]] 0.05 µM 0.152× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 26.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 48.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 41.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.57× (z +8.9) | [[4EGI-1 (drug)]] 5 µM 0.0965× (z -8.5) |
| [[Hs 766T (line)]] | wt | 30.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.19× (z +8.8) | [[Futibatinib (drug)]] 5 µM 0.0900× (z -9.7) |
| [[HT-29 (line)]] | alt | 54.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 36.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 68.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0756× (z -24.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 39.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 35.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AREL1]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PARGP1]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ATP5PF]] | +0.63 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[PGS1]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 | pathway: Phospholipid metabolism |
| [[TRAPPC10]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CUL2]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[HIRA]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[SNHG30]] | +0.60 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[TTI1]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 | same gene group |
| [[NDOR1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SLC38A9]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 | pathway: Autophagy |
| [[SNRNP40]] | +0.59 | +0.65 / +0.57 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUN]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 | pathway: Toll Like Receptor 9 (TLR9) Cascade |
| [[TFE3]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[JUND]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NOTCH2NLC]] | -0.52 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[AFF4]] | -0.51 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[PLEKHO2]] | -0.51 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[RNF223]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZNF286B]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[IQCN]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NOTCH2NLB]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[MAP3K2-DT]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RPLP0P2]] | -0.50 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIK3R4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-10.6, -16.9); signed map (-44.9, -22.7). **Vector** length 87.7, 21.8% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +14.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.6 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +16.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +9.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +7.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -10.2 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.8 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphoinositide-3-kinase regulatory subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:130,678,934-130,746,829 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VPS15, p150 |
| Gene groups (HGNC) | WD repeat domain containing; Armadillo like helical domain containing; PIK3C3 complex subunits; Pseudokinases |
| Reactome | 38 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99570](https://www.uniprot.org/uniprotkb/Q99570) (Phosphoinositide 3-kinase regulatory subunit 4):

> Regulatory subunit of the PI3K complex that mediates formation of phosphatidylinositol 3-phosphate; different complex forms are believed to play a role in multiple membrane trafficking pathways: PI3KC3-C1 is involved in initiation of autophagosomes and PI3KC3-C2 in maturation of autophagosomes and endocytosis. Involved in regulation of degradative endocytic trafficking and cytokinesis, probably in the context of PI3KC3-C2.

**Summary**, from NCBI Gene [30849](https://www.ncbi.nlm.nih.gov/gene/30849):

> Predicted to enable protein serine/threonine kinase activity. Involved in several processes, including autophagosome maturation; early endosome to late endosome transport; and phosphatidylinositol 3-kinase/protein kinase B signal transduction. Located in late endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8982) · Entrez [30849](https://www.ncbi.nlm.nih.gov/gene/30849) · UniProt [Q99570](https://www.uniprot.org/uniprotkb/Q99570) · Ensembl [ENSG00000196455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196455)

## Data

Gene col 12209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12209); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12209]; `tensor/DDL_lfc|DDL_z.npy` [12209]; `embed/gene_vectors.npy` [12209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12209 or target_col == 12209). Every well: [[PIK3R4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3R4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
