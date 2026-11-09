---
symbol: "HOOK3"
type: "gene"
col: 9608
ensembl_id: "ENSG00000168172"
name: "hook microtubule tethering protein 3"
location: "8p11.21"
module: 1
arm: "-"
pooled_cpm: 185.11
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# HOOK3

*hook microtubule tethering protein 3* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.18× (z +5.3, q 5e-05, up in 19 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.13× (z +4.2, q 0.007, up in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 1.45×, MIA PaCa-2 1.42×; ⚠ cell-cycle shift, explains ~78% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.599× (z -17.2, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.651× (z -14.4, q 7e-45, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIB1]] (+0.58, fdr 1e-04), [[NUMB]] (+0.53, fdr 3e-05), [[PPP2R3A]] (+0.52, fdr 2e-05); moves opposite to [[MTPAP]] (-0.54, fdr 1e-05), [[TGFBRAP1]] (-0.54, fdr 3e-05), [[METAP1D]] (-0.53, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 1.45×, MIA PaCa-2 1.42×; ⚠ cell-cycle shift, explains ~78% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.18× | +5.3 | 5e-05 | 19/47 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +4.2 | 0.007 | 14/47 (LOX-IMVI, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.042 | 21/49 (RKO, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.03× | +3.3 | 0.16 | 0/50 | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.22 | 11/50 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.19× | +3.0 | 0.22 | 13/48 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 27 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.599×** | -17.2 | 0e+00 | 44/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -15.6 | 0e+00 | 42/47 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -14.4 | 7e-45 | 38/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.658×** | -14.1 | 7e-43 | 42/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.753×** | -13.5 | 3e-39 | 31/48 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -12.2 | 2e-32 | 40/49 (HOP62, HS-578T, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.699×** | -12.0 | 2e-31 | 37/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.683×** | -10.8 | 3e-25 | 33/45 (J82, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.741×** | -10.1 | 5e-22 | 31/49 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.579×** | -9.6 | 5e-20 | 36/48 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.760×** | -9.2 | 2e-18 | 34/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.757×** | -9.0 | 1e-17 | 30/48 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.758×** | -9.0 | 2e-17 | 34/47 (SNU-423, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.783×** | -7.9 | 1e-13 | 28/44 (HOP62, NCI-H1573, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.800×** | -7.5 | 2e-12 | 31/48 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -6.3 | 8e-09 | 25/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.833×** | -5.9 | 1e-07 | 25/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.909× | -4.5 | 2e-04 | 5/48 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.874× | -4.5 | 2e-04 | 16/48 (HS-578T, HOP62, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.5 µM |  | 0.836× | -4.1 | 0.001 | 19/48 (SW480, A-172, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.919× | -4.0 | 0.001 | 8/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.883× | -3.9 | 0.002 | 12/47 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.925× | -3.7 | 0.004 | 9/48 (HOP62, A-172, …) | top dose only |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.925× | -3.7 | 0.004 | 3/49 (A498, NCI-H661, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.009 | 18/49 (RPMI-7951, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.872× | -3.1 | 0.029 | 13/48 (SHP-77, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.897× | -3.1 | 0.029 | 9/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 347 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -15.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.219× (z -13.1) |
| [[J82 (line)]] | alt | 240 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.335× (z -10.9) |
| [[A-172 (line)]] | wt | 297 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -26.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -21.1) |
| [[LOX-IMVI (line)]] | wt | 311 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.297× (z -11.4) |
| [[HS-578T (line)]] | alt | 366 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 233 | 0 | 7 (5 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.264× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -12.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.292× (z -10.4) |
| [[HCT15 (line)]] | alt | 336 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.417× (z -11.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.538× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 263 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.493× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 180 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -12.8) |
| [[H4 (line)]] | wt | 196 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -12.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 232 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -15.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -25.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.277× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 261 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -12.2) |
| [[SNU-423 (line)]] | alt | 169 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.475× (z -11.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -13.9) |
| [[Hs 766T (line)]] | wt | 270 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.496× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 310 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -11.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 139 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.435× (z -14.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.600× (z -9.0) |
| [[LS 180 (line)]] | wt | 170 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 162 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.546× (z -9.2) |
| [[SW1417 (line)]] | alt | 202 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.515× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[SW480 (line)]] | alt | 151 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.566× (z -12.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 185 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.545× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 200 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -13.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 91.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.464× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[RPMI-7951 (line)]] | alt | 249 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.434× (z -11.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.232× (z -11.3) |
| [[SW 900 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.534× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 231 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.120× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 149 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.348× (z -10.9) |
| [[KATO III (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.465× (z -11.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -13.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.589× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H661 (line)]] | alt | 181 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.295× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 179 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.399× (z -8.5) |
| [[SNU-1 (line)]] | wt | 227 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -10.0) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 246 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.0534× (z -14.5) |
| [[SW48 (line)]] | wt | 175 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.441× (z -8.9) |
| [[A498 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 234 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 209 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIB1]] | +0.58 | +0.36 / +0.68 | both halves | 1e-04 | same gene group |
| [[NUMB]] | +0.53 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[PPP2R3A]] | +0.52 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RABGEF1]] | +0.52 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SELENOW]] | +0.52 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[ATP11B]] | +0.50 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[MYO9B]] | +0.50 | +0.62 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CBL]] | +0.50 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[GAN]] | +0.50 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[RAB6A]] | +0.50 | +0.60 / +0.51 | both halves | 1e-05 | STRING 431 |
| [[SLC35F5]] | +0.49 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[HMCES]] | +0.49 | +0.58 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | -0.54 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[METAP1D]] | -0.53 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[STK33]] | -0.53 | -0.63 / -0.49 | both halves | 2e-05 |  |
| [[ZZZ3]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[TMEM177]] | -0.50 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.50 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ZNF485]] | -0.50 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[COG2]] | -0.50 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ZNF239]] | -0.50 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[BMS1P1-1]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[BYSL]] | -0.48 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.4, 3.8); signed map (-16.9, 16.2). **Vector** length 97.8, 28.2% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +6.3 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.4 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.6 | -12.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.6 | -9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.3 | -15.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.1 | -9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | hook microtubule tethering protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,896,946-43,030,535 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HK3 |
| Gene groups (HGNC) | FHF complex; HOOK family; Centriolar satellite proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VS8](https://www.uniprot.org/uniprotkb/Q86VS8) (Protein Hook homolog 3):

> Acts as an adapter protein linking the dynein motor complex to various cargos and converts dynein from a non-processive to a highly processive motor in the presence of dynactin. Facilitates the interaction between dynein and dynactin and activates dynein processivity (the ability to move along a microtubule for a long distance without falling off the track). Predominantly recruits 2 dyneins, which increases both the force and speed of the microtubule motor. Component of the FTS/Hook/FHIP …

**Summary**, from NCBI Gene [84376](https://www.ncbi.nlm.nih.gov/gene/84376):

> Hook proteins are cytosolic coiled-coil proteins that contain conserved N-terminal domains, which attach to microtubules, and more divergent C-terminal domains, which mediate binding to organelles. The Drosophila Hook protein is a component of the endocytic compartment.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:23576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23576) · Entrez [84376](https://www.ncbi.nlm.nih.gov/gene/84376) · UniProt [Q86VS8](https://www.uniprot.org/uniprotkb/Q86VS8) · Ensembl [ENSG00000168172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168172)

## Data

Gene col 9608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9608); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9608]; `tensor/DDL_lfc|DDL_z.npy` [9608]; `embed/gene_vectors.npy` [9608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9608 or target_col == 9608). Every well: [[HOOK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOOK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
