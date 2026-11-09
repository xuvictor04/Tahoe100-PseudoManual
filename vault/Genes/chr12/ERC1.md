---
symbol: "ERC1"
type: "gene"
col: 1356
ensembl_id: "ENSG00000082805"
name: "ELKS/RAB6-interacting/CAST family member 1"
location: "12p13.33"
module: 211
arm: "+"
pooled_cpm: 379.22
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# ERC1

*ELKS/RAB6-interacting/CAST family member 1* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.29× (z +7.2, q 4e-10, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.500× (z -19.8, q 0e+00, down in 41 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.686× (z -15.8, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC6B]] (+0.78, fdr 7e-06), [[RABGAP1L]] (+0.65, fdr 1e-05), [[ADK]] (+0.64, fdr 1e-05); moves opposite to [[KBTBD2]] (-0.55, fdr 3e-05), [[TUT1]] (-0.48, fdr 6e-05), [[IFNGR2]] (-0.48, fdr 4e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1356.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +7.2 | 4e-10 | 31/46 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +6.4 | 5e-08 | 26/47 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.28×** | +5.9 | 5e-07 | 28/47 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +5.0 | 7e-05 | 25/46 (H4, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +5.0 | 8e-05 | 21/47 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.7 | 2e-04 | 19/47 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +4.5 | 6e-04 | 16/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.14× | +3.4 | 0.041 | 13/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.064 | 20/49 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.077 | 14/47 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.26× | +3.1 | 0.10 | 20/47 (MIA PaCa-2, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 1.25× | +3.0 | 0.11 | 16/47 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.11 | 8/47 (NCI-H460, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.500×** | -19.8 | 0e+00 | 41/43 (NCI-H23, HCT15, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -19.3 | 0e+00 | 46/46 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.503×** | -18.9 | 0e+00 | 41/44 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.509×** | -17.9 | 0e+00 | 45/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -15.8 | 0e+00 | 36/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -9.9 | 4e-21 | 43/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.506×** | -9.2 | 3e-18 | 38/48 (NCI-H23, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.737×** | -9.0 | 1e-17 | 37/47 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.756×** | -8.0 | 9e-14 | 32/47 (SW48, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.789×** | -6.3 | 2e-08 | 25/47 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.663×** | -5.5 | 1e-06 | 33/47 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.876× | -5.5 | 1e-06 | 21/47 (SW48, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | 0.840× | -5.2 | 9e-06 | 21/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.857× | -4.6 | 2e-04 | 21/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.859× | -4.2 | 0.001 | 15/46 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.917× | -3.6 | 0.009 | 4/47 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.891× | -3.4 | 0.017 | 12/47 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.853× | -3.4 | 0.022 | 16/46 (J82, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.895× | -3.3 | 0.026 | 19/47 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.927× | -3.2 | 0.035 | 3/48 (NCI-H2122, SW 1271, …) | rises with dose |  |
| [[Irinotecan (drug)]] 5 µM |  | **0.794×** | -3.1 | 0.043 | 19/49 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.043 | 16/48 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 401 | 10 (2 ⚠) | 4 (4 ⚠) | [[Trametinib (drug)]] 0.5 µM 1.81× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -19.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 352 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 521 | 2 (1 ⚠) | 8 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.72× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.389× (z -20.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 770 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.378× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 250 | 2 (1 ⚠) | 7 (6 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.02× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -13.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -9.4) |
| [[PANC-1 (line)]] | alt | 336 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -19.8) |
| [[LOX-IMVI (line)]] | wt | 618 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 248 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 986 | 1 | 7 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.62× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -42.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.321× (z -11.5) |
| [[SW480 (line)]] | alt | 452 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.624× (z -10.4) |
| [[RKO (line)]] | wt | 677 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.143× (z -33.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -13.3) |
| [[SNU-423 (line)]] | alt | 279 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -16.5) |
| [[C-33 A (line)]] | alt | 575 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -13.6) |
| [[HCT15 (line)]] | alt | 542 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -33.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -13.1) |
| [[HOP62 (line)]] | alt | 533 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -19.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 365 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -18.3) |
| [[LS 180 (line)]] | wt | 252 | 1 (1 ⚠) | 5 (4 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.4) ⚠ cell-cycle shift, explains ~54% of this change | [[PH-797804 (drug)]] 5 µM 0.177× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 392 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -15.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 215 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -17.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1,109 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -28.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 351 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.449× (z -12.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.547× (z -8.5) |
| [[H4 (line)]] | wt | 427 | 1 | 4 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.80× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -15.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 288 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.445× (z -12.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 273 | 2 (2 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.67× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -13.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 237 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -17.2) |
| [[A549 (line)]] | wt | 365 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -21.0) |
| [[KATO III (line)]] | alt | 286 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -14.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 486 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -15.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 397 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.521× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.589× (z -9.4) |
| [[Hs 766T (line)]] | wt | 238 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -15.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 228 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 346 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.485× (z -10.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 316 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.514× (z -9.7) ⚠ toxic |
| [[SW 900 (line)]] | alt | 333 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -13.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 379 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -11.1) |
| [[CHP-212 (line)]] | wt | 314 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -12.4) |
| [[NCI-H661 (line)]] | alt | 391 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.5) |
| [[SNU-1 (line)]] | wt | 396 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.453× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 510 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.305× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 224 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 270 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.540× (z -11.2) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 238 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.87× (z +9.7) ⚠ unreliable plate only | — |
| [[BT-474 (line)]] | alt | 239 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.545× (z -9.6) |
| [[COLO 205 (line)]] | alt | 228 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.532× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 44.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 300 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC6B]] | +0.78 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[RABGAP1L]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ADK]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[SUPT3H]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[CCSER2]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MAP4]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[VTI1A]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[DYM]] | +0.59 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[KIF1B]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SMG6]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ANO10]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[FER]] | +0.55 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD2]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TUT1]] | -0.48 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[IFNGR2]] | -0.48 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[COQ6]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SP3]] | -0.48 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[AGAP13P]] | -0.47 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[RBM22]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[COG4]] | -0.45 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[NIPBL-DT]] | -0.45 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[CHAMP1]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[CYP4V2]] | -0.45 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[ZNF17]] | -0.44 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ERC1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDS5A]] | C | PDS5A's natural level strengthens ERC1's drug response | PDS5A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.38; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[UBE2K]] | C | UBE2K's natural level strengthens ERC1's drug response | UBE2K's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.29; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.1, -34.2); signed map (-17.8, 3.1). **Vector** length 119, 41.3% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +9.8 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | +8.6 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +5.0 |
|  | [[EX229 (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.1 | +0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.1 | -19.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.1 | -9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -18.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -15.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ELKS/RAB6-interacting/CAST family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:990,509-1,495,933 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ELKS, KIAA1081, CAST2, MGC12974; previously RAB6IP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUD2](https://www.uniprot.org/uniprotkb/Q8IUD2) (ELKS/Rab6-interacting/CAST family member 1):

> Regulatory subunit of the IKK complex. Probably recruits IkappaBalpha/NFKBIA to the complex. May be involved in the organization of the cytomatrix at the nerve terminals active zone (CAZ) which regulates neurotransmitter release. May be involved in vesicle trafficking at the CAZ. May be involved in Rab-6 regulated endosomes to Golgi transport.

**Summary**, from NCBI Gene [23085](https://www.ncbi.nlm.nih.gov/gene/23085):

> The protein encoded by this gene is a member of a family of RIM-binding proteins. RIMs are active zone proteins that regulate neurotransmitter release. This gene has been found fused to the receptor-type tyrosine kinase gene RET by gene rearrangement due to the translocation t(10;12)(q11;p13) in thyroid papillary carcinoma. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:17072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17072) · Entrez [23085](https://www.ncbi.nlm.nih.gov/gene/23085) · UniProt [Q8IUD2](https://www.uniprot.org/uniprotkb/Q8IUD2) · Ensembl [ENSG00000082805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082805)

## Data

Gene col 1356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1356); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1356]; `tensor/DDL_lfc|DDL_z.npy` [1356]; `embed/gene_vectors.npy` [1356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1356 or target_col == 1356). Every well: [[ERC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
