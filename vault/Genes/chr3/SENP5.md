---
symbol: "SENP5"
type: "gene"
col: 4046
ensembl_id: "ENSG00000119231"
name: "SUMO specific peptidase 5"
location: "3q29"
module: 52
arm: "+"
pooled_cpm: 200.6
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SENP5

*SUMO specific peptidase 5* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +15.9, q 0e+00, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.647× (z -11.1, q 6e-26, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.704× (z -9.0, q 5e-17, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS53]] (+0.75, fdr 7e-06), [[PDCD6]] (+0.75, fdr 7e-06), [[RABGEF1]] (+0.71, fdr 7e-06); moves opposite to [[CFL2]] (-0.68, fdr 7e-06), [[REPIN1]] (-0.66, fdr 7e-06), [[ZSCAN12]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +15.9 | 0e+00 | 42/49 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.71×** | +14.1 | 6e-43 | 46/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.60×** | +12.4 | 6e-33 | 47/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.55×** | +11.7 | 3e-29 | 44/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +9.8 | 1e-20 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +8.7 | 3e-16 | 44/49 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +8.4 | 3e-15 | 38/48 (HCT15, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +8.1 | 5e-14 | 33/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +7.3 | 2e-11 | 33/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +7.3 | 2e-11 | 32/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +7.2 | 2e-11 | 35/50 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.30×** | +6.9 | 2e-10 | 35/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +6.6 | 1e-09 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +6.4 | 9e-09 | 35/48 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +5.7 | 6e-07 | 37/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.6 | 1e-04 | 21/48 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 19/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -11.1 | 6e-26 | 39/44 (NCI-H2347, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.700×** | -9.5 | 7e-19 | 40/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -9.0 | 5e-17 | 37/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -8.8 | 1e-16 | 35/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.749×** | -7.7 | 2e-12 | 36/48 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.751×** | -7.5 | 6e-12 | 38/49 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -5.9 | 4e-07 | 29/48 (AsPC-1, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.782×** | -5.8 | 4e-07 | 24/45 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.810×** | -5.6 | 1e-06 | 27/48 (H4, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.859× | -4.5 | 4e-04 | 15/48 (AsPC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.858× | -4.1 | 0.002 | 19/48 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.854× | -4.0 | 0.003 | 15/47 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.903× | -3.8 | 0.005 | 12/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.868× | -3.8 | 0.007 | 13/48 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.908× | -3.6 | 0.010 | 5/48 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.010 | 22/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.874× | -3.6 | 0.010 | 10/48 (A498, A549, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.817×** | -3.5 | 0.013 | 20/47 (LOX-IMVI, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.880× | -3.4 | 0.018 | 10/49 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.895× | -3.4 | 0.018 | 9/48 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 252 | 10 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +21.4) | — |
| [[NCI-H460 (line)]] | wt | 126 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +18.0) | — |
| [[SW480 (line)]] | alt | 290 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +21.7) | — |
| [[SNU-1 (line)]] | wt | 197 | 4 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -11.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 247 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +17.9) | [[Selinexor (drug)]] 5 µM 0.616× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 240 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.8) | — |
| [[LoVo (line)]] | wt | 203 | 3 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 1.86× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.73× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.515× (z -9.9) |
| [[LS 180 (line)]] | wt | 170 | 4 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.6) | [[Harringtonine (drug)]] 5 µM 0.434× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 183 | 4 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 186 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.61× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.518× (z -11.7) |
| [[PANC-1 (line)]] | alt | 212 | 4 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +12.8) | [[Harringtonine (drug)]] 5 µM 0.513× (z -10.6) |
| [[BT-474 (line)]] | alt | 226 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +15.6) | — |
| [[KATO III (line)]] | alt | 229 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 326 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.514× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 163 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 168 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 227 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.25× (z +16.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 207 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.544× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 222 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.445× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 159 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 272 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.504× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 168 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 194 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.507× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 162 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.556× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 210 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.35× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 148 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.6) | — |
| [[J82 (line)]] | alt | 298 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.521× (z -10.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 195 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +12.4) | — |
| [[A-172 (line)]] | wt | 173 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.516× (z -10.6) |
| [[H4 (line)]] | wt | 227 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.353× (z -12.8) ⚠ transcription drop; cell-cycle shift, explains ~15% of this change |
| [[Hs 766T (line)]] | wt | 150 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.459× (z -10.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 181 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.373× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 280 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 133 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.82× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 185 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 278 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +10.3) | — |
| [[A549 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 165 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS53]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[PDCD6]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[LRRC8A]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[RAB43]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[PMPCA]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[MFN1]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[LIN52]] | +0.66 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[FBH1]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL2]] | -0.68 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[REPIN1]] | -0.66 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[ZSCAN12]] | -0.66 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[CHIC1]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[ZNF780A]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CLK4]] | -0.61 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[C12orf29]] | -0.61 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[TAB2]] | -0.61 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[BTN2A2]] | -0.60 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[KPNA5]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 | STRING 406 |
| [[ZNF772]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SENP5's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.9, -0.1); signed map (-46.9, 0.5). **Vector** length 127, 46.1% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +15.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.0 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.9 | +7.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.7 | +14.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.8 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Pralsetinib (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Naproxen (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -13.5 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -11.5 | -7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -11.4 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -10.3 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.2 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.6 | -5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | SUMO specific peptidase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,867,856-196,934,714 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC27076 |
| Gene groups (HGNC) | SUMO specific peptidases |
| Reactome | 3 pathways, smallest: SUMO is proteolytically processed; Processing and activation of SUMO; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HI0](https://www.uniprot.org/uniprotkb/Q96HI0) (Sentrin-specific protease 5):

> Protease that catalyzes two essential functions in the SUMO pathway: processing of full-length SUMO3 to its mature form and deconjugation of SUMO2 and SUMO3 from targeted proteins. Has weak proteolytic activity against full-length SUMO1 or SUMO1 conjugates. Required for cell division.

**Summary**, from NCBI Gene [205564](https://www.ncbi.nlm.nih.gov/gene/205564):

> The reversible posttranslational modification of proteins by the addition of small ubiquitin-like SUMO proteins (see SUMO1; MIM 601912) is required for numerous biologic processes. SUMO-specific proteases, such as SENP5, are responsible for the initial processing of SUMO precursors to generate a C-terminal diglycine motif required for the conjugation reaction. They also have isopeptidase activity for the removal of SUMO from high molecular mass SUMO conjugates (Di Bacco et al., 2006 [PubMed …

**Accessions** — [HGNC:28407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28407) · Entrez [205564](https://www.ncbi.nlm.nih.gov/gene/205564) · UniProt [Q96HI0](https://www.uniprot.org/uniprotkb/Q96HI0) · Ensembl [ENSG00000119231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119231)

## Data

Gene col 4046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4046); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4046]; `tensor/DDL_lfc|DDL_z.npy` [4046]; `embed/gene_vectors.npy` [4046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4046 or target_col == 4046). Every well: [[SENP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SENP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
