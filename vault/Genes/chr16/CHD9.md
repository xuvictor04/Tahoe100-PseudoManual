---
symbol: "CHD9"
type: "gene"
col: 10803
ensembl_id: "ENSG00000177200"
name: "chromodomain helicase DNA binding protein 9"
location: "16q12.2"
module: 12
arm: "+"
pooled_cpm: 271.23
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CHD9

*chromodomain helicase DNA binding protein 9* — 16q12.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (RKO 2.18×, A-427 2.01×, HepG2/C3A 2.19×, C-33 A 1.82×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (RKO 2.29×, C-33 A 1.90×, SW480 1.63×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (RKO 2.11×, C-33 A 2.14×, LOX-IMVI 1.68×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.456× (z -23.3, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.698× (z -15.0, q 0e+00, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS18B]] (+0.69, fdr 7e-06), [[CEP350]] (+0.62, fdr 1e-05), [[SEC62]] (+0.62, fdr 1e-05); moves opposite to [[BCAP31]] (-0.54, fdr 2e-05), [[AKT1]] (-0.54, fdr 1e-05), [[POMGNT1]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10803.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (RKO 2.18×, A-427 2.01×, HepG2/C3A 2.19×, C-33 A 1.82×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (RKO 2.29×, C-33 A 1.90×, SW480 1.63×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (RKO 2.11×, C-33 A 2.14×, LOX-IMVI 1.68×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +5.1 | 2e-04 | 21/48 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.8 | 5e-04 | 23/48 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +4.2 | 0.005 | 7/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.7 | 0.028 | 19/48 (RKO, C-33 A, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.028 | 10/48 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.13× | +3.6 | 0.033 | 9/48 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.12× | +3.5 | 0.035 | 9/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.051 | 11/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.10 | 15/48 (C-33 A, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.11 | 15/47 (RKO, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.11× | +3.1 | 0.11 | 4/49 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.11× | +3.0 | 0.12 | 5/48 (NCI-H2347, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.456×** | -23.3 | 0e+00 | 47/49 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -21.1 | 0e+00 | 39/44 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.544×** | -16.7 | 0e+00 | 42/45 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -15.0 | 0e+00 | 37/49 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -12.8 | 3e-35 | 43/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.670×** | -11.2 | 4e-27 | 40/48 (HT-29, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -10.7 | 1e-24 | 43/48 (J82, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -10.3 | 3e-23 | 42/48 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.729×** | -9.3 | 6e-19 | 32/48 (HEC-1-A, NCI-H460, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.742×** | -8.8 | 7e-17 | 41/48 (HOP62, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -8.5 | 8e-16 | 32/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.775×** | -7.6 | 2e-12 | 31/48 (HEC-1-A, RKO, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.776×** | -7.2 | 2e-11 | 28/50 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.788×** | -7.1 | 7e-11 | 30/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.793×** | -6.9 | 3e-10 | 27/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.874× | -5.6 | 6e-07 | 14/49 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.681×** | -5.5 | 8e-07 | 25/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.854× | -4.6 | 8e-05 | 16/48 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.867× | -4.2 | 5e-04 | 17/47 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.820×** | -4.2 | 6e-04 | 23/49 (MIA PaCa-2, NCI-H2122, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.877× | -3.7 | 0.004 | 14/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.875× | -3.6 | 0.005 | 11/47 (CHP-212, Panc 03.27, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.845× | -3.5 | 0.007 | 18/48 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.894× | -3.1 | 0.031 | 8/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.906× | -2.9 | 0.061 | 10/48 (COLO 205, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 388 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -21.6) |
| [[J82 (line)]] | alt | 226 | 0 | 11 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.417× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 337 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.479× (z -12.3) |
| [[SNU-423 (line)]] | alt | 234 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 309 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -27.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 385 | 4 (4 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +20.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -21.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 379 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.659× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 380 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -13.5) |
| [[BT-474 (line)]] | alt | 171 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -11.1) |
| [[HT-29 (line)]] | alt | 321 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.458× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.472× (z -11.6) |
| [[PANC-1 (line)]] | alt | 180 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.489× (z -15.3) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.338× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 218 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -12.6) |
| [[HS-578T (line)]] | alt | 310 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -18.1) |
| [[SW1417 (line)]] | alt | 202 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.523× (z -9.7) |
| [[A-172 (line)]] | wt | 382 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -14.2) |
| [[A498 (line)]] | wt | 403 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -11.5) |
| [[C-33 A (line)]] | alt | 326 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -18.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 375 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -11.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 596 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 271 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.428× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.564× (z -8.5) |
| [[LS 180 (line)]] | wt | 263 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.530× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 281 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -16.1) |
| [[SW480 (line)]] | alt | 282 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.63× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -10.9) |
| [[KATO III (line)]] | alt | 265 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.505× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~16% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -10.6) |
| [[LoVo (line)]] | wt | 248 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.591× (z -8.9) |
| [[A-427 (line)]] | wt | 212 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +18.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -21.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 316 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -14.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 417 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -23.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 278 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -18.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 217 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.68× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.497× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 166 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.437× (z -12.7) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 277 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -16.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.508× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[COLO 205 (line)]] | alt | 303 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -13.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 305 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.492× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 281 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 165 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0927× (z -17.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 385 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.541× (z -9.0) |
| [[Hs 766T (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 215 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.646× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.2) |
| [[SHP-77 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -13.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -13.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.536× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 209 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 457 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 175 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18B]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CEP350]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SEC62]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PPIG]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[BDP1]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 | STRING 525 |
| [[KIAA1586]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[COIL]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CLK4]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PEX12]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CEBPZ]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CRCP]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[AKT1]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[POMGNT1]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[AHSA1]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TESK1]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ZNF731P]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[HSPA8]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TPST2]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[LINC03009]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SMG1P3]] | -0.49 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[INTS1]] | -0.48 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[ANKRD30BL]] | -0.48 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.1, 1.8); signed map (4.1, -16.5). **Vector** length 111, 38.0% of its response variance represented; |z| ≥ 3 in 1,522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.5 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.9 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | -0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -15.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -10.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.0 | -11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -16.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -8.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:53,054,991-53,329,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12178, KIAA0308, BC022889 |
| Gene groups (HGNC) | SNF2 related family |
| Reactome | 24 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression; CHD6, CHD7, CHD8, CHD9 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3L8U1](https://www.uniprot.org/uniprotkb/Q3L8U1) (ATP-dependent chromatin remodeler CHD9):

> Probable ATP-dependent chromatin-remodeling factor. Acts as a transcriptional coactivator for PPARA and possibly other nuclear receptors. Has DNA-dependent ATPase activity and binds to A/T-rich DNA. Associates with A/T-rich regulatory regions in promoters of genes that participate in the differentiation of progenitors during osteogenesis (By similarity).

**Summary**, from NCBI Gene [80205](https://www.ncbi.nlm.nih.gov/gene/80205):

> Predicted to enable ATP binding activity; ATP hydrolysis activity; and DNA binding activity. Predicted to be involved in DNA-templated transcription. Predicted to act upstream of or within chromatin organization. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25701) · Entrez [80205](https://www.ncbi.nlm.nih.gov/gene/80205) · UniProt [Q3L8U1](https://www.uniprot.org/uniprotkb/Q3L8U1) · Ensembl [ENSG00000177200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177200)

## Data

Gene col 10803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10803); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10803]; `tensor/DDL_lfc|DDL_z.npy` [10803]; `embed/gene_vectors.npy` [10803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10803 or target_col == 10803). Every well: [[CHD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
