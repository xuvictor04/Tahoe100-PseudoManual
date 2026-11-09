---
symbol: "ELF1"
type: "gene"
col: 4205
ensembl_id: "ENSG00000120690"
name: "E74 like ETS transcription factor 1"
location: "13q14.11"
module: 51
arm: "+"
pooled_cpm: 205.44
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ELF1

*E74 like ETS transcription factor 1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +14.2, q 7e-43, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.431× (z -17.6, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.480× (z -15.4, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.67, fdr 7e-06), [[PATL2]] (+0.66, fdr 1e-05), [[EPC2]] (+0.65, fdr 1e-05); moves opposite to [[PIGF]] (-0.61, fdr 1e-05), [[GNAS-AS1]] (-0.61, fdr 1e-05), [[PMS2P3-1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[IFI16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +14.2 | 7e-43 | 35/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +11.2 | 1e-26 | 37/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.9 | 8e-10 | 31/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 2e-05 | 26/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.52×** | +4.6 | 5e-04 | 37/48 (HCT15, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.005 | 18/48 (HEC-1-A, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.005 | 21/47 (LOX-IMVI, SW480, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.22×** | +4.0 | 0.005 | 24/47 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.007 | 22/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.011 | 28/50 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +3.7 | 0.013 | 21/50 (HEC-1-A, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.015 | 23/48 (NCI-H460, KATO III, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.026 | 19/47 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.431×** | -17.6 | 0e+00 | 45/49 (COLO 205, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -15.4 | 0e+00 | 40/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.473×** | -15.1 | 0e+00 | 39/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.487×** | -15.1 | 0e+00 | 40/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.489×** | -15.0 | 0e+00 | 43/48 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.558×** | -11.1 | 2e-26 | 41/45 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -8.6 | 7e-16 | 33/48 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.673×** | -8.0 | 1e-13 | 39/50 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.766×** | -7.9 | 2e-13 | 29/49 (A498, HepG2/C3A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.717×** | -6.7 | 1e-09 | 29/48 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -6.6 | 2e-09 | 35/48 (HT-29, COLO 205, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.770×** | -5.5 | 2e-06 | 28/48 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.782×** | -4.9 | 3e-05 | 26/47 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.810×** | -4.2 | 9e-04 | 27/47 (A549, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.817×** | -4.2 | 9e-04 | 24/48 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.696×** | -4.0 | 0.003 | 30/49 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.853× | -3.2 | 0.043 | 19/48 (A549, Hs 766T, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.899× | -3.1 | 0.047 | 11/49 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.756×** | -3.1 | 0.056 | 19/48 (SW 900, C32, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.862× | -2.9 | 0.085 | 17/47 (C-33 A, A498, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.906× | -2.9 | 0.085 | 10/48 (SNU-1, SNU-423, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.825×** | -2.9 | 0.095 | 14/48 (HepG2/C3A, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 194 | 9 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 265 | 2 (1 ⚠) | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.458× (z -9.4) |
| [[RKO (line)]] | wt | 284 | 5 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +18.4) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -17.4) |
| [[A-172 (line)]] | wt | 133 | 2 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -10.0) |
| [[A498 (line)]] | wt | 159 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +25.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -16.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.408× (z -14.5) |
| [[HT-29 (line)]] | alt | 435 | 1 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -19.8) |
| [[SNU-423 (line)]] | alt | 175 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.352× (z -12.8) |
| [[SW480 (line)]] | alt | 250 | 3 (1 ⚠) | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.82× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.91× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 270 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.401× (z -11.4) |
| [[SW 900 (line)]] | alt | 231 | 0 | 9 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.334× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 165 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 343 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 186 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.264× (z -15.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.324× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 394 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -10.7) |
| [[LoVo (line)]] | wt | 277 | 6 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.34× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 122 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +20.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 164 | 0 | 7 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.193× (z -17.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 242 | 2 | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.03× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.479× (z -9.9) |
| [[A549 (line)]] | wt | 205 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.363× (z -9.7) |
| [[C32 (line)]] | wt | 209 | 3 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.80× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.320× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.399× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 226 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.499× (z -9.0) |
| [[LS 180 (line)]] | wt | 238 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 1,259 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0719× (z -29.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.280× (z -14.3) |
| [[HS-578T (line)]] | alt | 103 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 126 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.3) | [[Belinostat (drug)]] 0.5 µM 0.431× (z -9.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -8.6) |
| [[SW1417 (line)]] | alt | 280 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.453× (z -11.6) |
| [[SW48 (line)]] | wt | 243 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 200 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 137 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -16.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.311× (z -13.8) |
| [[H4 (line)]] | wt | 110 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 129 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +20.6) | — |
| [[HOP62 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.3) | [[Belinostat (drug)]] 5 µM 0.436× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 97.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0533× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 164 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 311 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 150 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 248 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.67 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PATL2]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[EPC2]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SCAMP1-AS1]] | +0.64 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[IFIT2]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TMEM265]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CEBPD]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TOR1AIP1]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MAD2L1BP]] | +0.62 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[NUTM2E]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[BRAF]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGF]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[GNAS-AS1]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[RPA1]] | -0.58 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[P3H1]] | -0.56 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[COG5]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TTC13]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MMS19]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ATP7B]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PPM1F]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ELAVL1]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TBCD]] | -0.55 | -0.48 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI16]] | B | IFI16 activity strengthens ELF1's drug response | lines that do not express IFI16 (18) vs lines expressing it (32) | the lines without IFI16 respond 0.74× as strongly (z diff +1.59); rises at some drug-doses, falls at others (27% from rises): Panobinostat 5 µM: 0.64x vs 0.46x (z diff +3.1); Panobinostat 0.5 µM: 0.60x vs 0.46x (z diff +3.1); Harringtonine 5 µM: 1.32x vs 1.91x (z diff +2.7) | 0.052 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF; rises at some drug-doses, falls at others; artifact flags |
| [[RSAD2]] | B | RSAD2 activity raises ELF1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without RSAD2 | 0.059 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[KLF5]] | B | KLF5 activity raises ELF1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.52× lower at baseline in the lines without KLF5 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[IFIT3]] | B | IFIT3 activity raises ELF1's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without IFIT3 | 0.062 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[PLEKHA4]] | B | PLEKHA4 activity strengthens ELF1's drug response | lines that do not express PLEKHA4 (7) vs lines expressing it (43) | the lines without PLEKHA4 respond 0.62× as strongly (z diff +2.46); strongest at Panobinostat 5 µM: 0.89x vs 0.48x (z diff +6.7) | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent; artifact flags |
| [[GBP1]] | B | GBP1 activity raises ELF1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.12× lower at baseline in the lines without GBP1 | 0.091 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IFI35]] | C | IFI35 activity raises ELF1's level | lines that do not express IFI35 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without IFI35 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, ISG15, BIRC3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (20.4, -31.2); signed map (9.7, -17.5). **Vector** length 120, 41.3% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.4 | +11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -6.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.6 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.5 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.3 | -15.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -8.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.9 | -1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | E74 like ETS transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:40,931,924-41,061,440 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: RUNX1 regulates transcription of genes involved in interleukin signaling; RUNX1 regulates transcription of genes involved in BCR signaling; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P32519](https://www.uniprot.org/uniprotkb/P32519) (ETS-related transcription factor Elf-1):

> Transcription factor that activates the LYN and BLK promoters. Appears to be required for the T-cell-receptor-mediated trans activation of HIV-2 gene expression. Binds specifically to two purine-rich motifs in the HIV-2 enhancer.

**Summary**, from NCBI Gene [1997](https://www.ncbi.nlm.nih.gov/gene/1997):

> This gene encodes an E26 transformation-specific related transcription factor. The encoded protein is primarily expressed in lymphoid cells and acts as both an enhancer and a repressor to regulate transcription of various genes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:3316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3316) · Entrez [1997](https://www.ncbi.nlm.nih.gov/gene/1997) · UniProt [P32519](https://www.uniprot.org/uniprotkb/P32519) · Ensembl [ENSG00000120690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120690)

## Data

Gene col 4205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4205); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4205]; `tensor/DDL_lfc|DDL_z.npy` [4205]; `embed/gene_vectors.npy` [4205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4205 or target_col == 4205). Every well: [[ELF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
