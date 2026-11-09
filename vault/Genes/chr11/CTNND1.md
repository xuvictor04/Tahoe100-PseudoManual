---
symbol: "CTNND1"
type: "gene"
col: 12618
ensembl_id: "ENSG00000198561"
name: "catenin delta 1"
location: "11q12.1"
module: 59
arm: "+"
pooled_cpm: 389.04
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# CTNND1

*catenin delta 1* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.21× (z +6.6, q 2e-08, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.539× (z -14.0, q 2e-41, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.681× (z -13.3, q 9e-38, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUFT1]] (+0.67, fdr 7e-06), [[CGN]] (+0.61, fdr 3e-05), [[CD2AP]] (+0.60, fdr 1e-05); moves opposite to [[BEND3]] (-0.57, fdr 1e-05), [[TTL]] (-0.55, fdr 1e-05), [[NBPF15]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[ADGRF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +6.6 | 2e-08 | 24/47 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +6.1 | 2e-07 | 27/47 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +6.1 | 2e-07 | 29/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.7 | 2e-06 | 33/47 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +5.0 | 7e-05 | 29/48 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +4.3 | 0.001 | 27/49 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.002 | 20/47 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.2 | 0.002 | 3/49 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.010 | 15/48 (HEC-1-A, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.020 | 23/46 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled); position effect removed |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.025 | 8/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.042 | 5/47 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.059 | 21/49 (HEC-1-A, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.059 | 6/47 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.539×** | -14.0 | 2e-41 | 41/44 (NCI-H1792, H4, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -13.3 | 9e-38 | 36/48 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.616×** | -11.4 | 8e-28 | 37/43 (NCI-H1792, LoVo, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -10.5 | 1e-23 | 39/47 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.666×** | -9.9 | 3e-21 | 39/48 (NCI-H1792, Panc 03.27, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.656×** | -9.9 | 4e-21 | 36/46 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.715×** | -8.2 | 2e-14 | 37/47 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.654×** | -5.4 | 4e-06 | 31/44 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.787×** | -5.1 | 2e-05 | 25/47 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.865× | -5.0 | 3e-05 | 12/47 (A-427, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.809×** | -4.5 | 4e-04 | 24/47 (BT-474, SW1417, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -3.9 | 0.004 | 9/47 (BT-474, Hs 766T, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.736×** | -3.9 | 0.004 | 29/48 (NCI-H1573, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.8 | 0.005 | 21/47 (HepG2/C3A, KATO III, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.862× | -3.5 | 0.019 | 19/47 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.020 | 26/47 (SW1417, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.910× | -3.2 | 0.033 | 4/47 (BT-474, PANC-1, …) | top dose only |  |
| [[Aliskiren (drug)]] 0.5 µM |  | 0.860× | -3.2 | 0.033 | 9/48 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 889 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -19.4) |
| [[LoVo (line)]] | wt | 505 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 377 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -19.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -17.7) |
| [[HT-29 (line)]] | alt | 724 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 194 | 6 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.31× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.542× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 815 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.386× (z -17.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -15.3) |
| [[SW480 (line)]] | alt | 408 | 1 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.54× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.501× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -11.9) |
| [[COLO 205 (line)]] | alt | 697 | 1 | 5 (2 ⚠) | [[Peretinoin (drug)]] 5 µM 2.08× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -15.3) |
| [[A549 (line)]] | wt | 302 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.06× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -18.5) |
| [[AsPC-1 (line)]] | alt | 513 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.451× (z -9.7) |
| [[H4 (line)]] | wt | 361 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.6) |
| [[KATO III (line)]] | alt | 563 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 257 | 3 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.46× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.513× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 517 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.460× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 735 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -12.8) |
| [[SW 900 (line)]] | alt | 415 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 228 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.01× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.486× (z -10.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 698 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -14.8) |
| [[HCT15 (line)]] | alt | 621 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -11.0) |
| [[HS-578T (line)]] | alt | 341 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -10.2) |
| [[J82 (line)]] | alt | 264 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.4) | [[Ixazomib citrate (drug)]] 5 µM 0.588× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 428 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -15.0) |
| [[RKO (line)]] | wt | 232 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.538× (z -8.5) ⚠ toxic |
| [[A498 (line)]] | wt | 246 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 1.94× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.8) |
| [[Hs 766T (line)]] | wt | 495 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 484 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 585 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -16.3) |
| [[PANC-1 (line)]] | alt | 374 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.80× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.507× (z -11.0) ⚠ transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -10.0) |
| [[CHP-212 (line)]] | wt | 304 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -13.3) |
| [[HOP62 (line)]] | alt | 216 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.497× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 241 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.05× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -15.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 239 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 344 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.514× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 295 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.490× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 234 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 152 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -11.9) |
| [[SNU-423 (line)]] | alt | 309 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -9.1) |
| [[SW 1271 (line)]] | alt | 280 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.211× (z -11.0) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 243 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.5) | — |
| [[A-172 (line)]] | wt | 212 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 233 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 301 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 337 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 391 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 373 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUFT1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CGN]] | +0.61 | +0.44 / +0.54 | both halves | 3e-05 | STRING 433 |
| [[CD2AP]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 | pathway: Cell-Cell communication |
| [[LIMA1]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 820 |
| [[RAB30]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[MAP3K13]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[JUP]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 901 |
| [[USP54]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ATP8B1]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CHD2]] | +0.54 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.53 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ELF3]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[TTL]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[NBPF15]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[NBPF20]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZFYVE9]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PRMT3]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[NAE1]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NBPF8]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A15]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SMYD2]] | -0.51 | -0.22 / -0.57 | both halves | 6e-04 |  |
| [[CCT5]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[EEF1AKMT1]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF1]] | B | ADGRF1 activity raises CTNND1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without ADGRF1 | 0.003 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[ELF3]] | B | ELF3 activity strengthens CTNND1's drug response | lines that do not express ELF3 (23) vs lines expressing it (25) | the lines without ELF3 respond 0.76× as strongly (z diff +1.33); strongest at Auranofin 5 µM: 0.73x vs 0.58x (z diff +4.1) | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3; target measured in part of the lines; artifact flags |
| [[FRK]] | B | FRK activity raises CTNND1's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without FRK | 0.005 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[ST14]] | B | ST14 activity raises CTNND1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.00× lower at baseline in the lines without ST14 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[GBP2]] | B | GBP2 activity raises CTNND1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[RBM47]] | B | RBM47 activity raises CTNND1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without RBM47 | 0.013 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[PTPRR]] | B | PTPRR activity raises CTNND1's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without PTPRR | 0.022 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[ELF3]] | B | ELF3 activity raises CTNND1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without ELF3 | 0.030 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[RBM47]] | B | RBM47 activity strengthens CTNND1's drug response | lines that do not express RBM47 (19) vs lines expressing it (29) | the lines without RBM47 respond 0.83× as strongly (z diff +0.90); strongest at Auranofin 5 µM: 0.73x vs 0.60x (z diff +3.6) | 0.033 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3; target measured in part of the lines; artifact flags |
| [[TJP3]] | B | TJP3 activity raises CTNND1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without TJP3 | 0.034 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[JUP]] | B | JUP activity strengthens CTNND1's drug response | lines that do not express JUP (16) vs lines expressing it (32) | the lines without JUP respond 0.82× as strongly (z diff +1.25); strongest at Auranofin 5 µM: 0.75x vs 0.61x (z diff +3.8) | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671; target measured in part of the lines; artifact flags |
| [[VWA1]] | B | VWA1 activity raises CTNND1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without VWA1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (20.0, 1.3); signed map (49.1, 6.7). **Vector** length 124, 43.4% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.2 | +4.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.8 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -10.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -13.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.3 | -5.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.9 | -0.1 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | catenin delta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,753,243-57,819,546 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0384, p120, p120cas, p120ctn; previously CTNND |
| Gene groups (HGNC) | Armadillo repeat containing; p120 catenin family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 23 pathways, smallest: CDH11 homotypic and heterotypic interactions; Regulation of CDH19 Expression and Function; InlA-mediated entry of Listeria monocytogenes into host cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O60716](https://www.uniprot.org/uniprotkb/O60716) (Catenin delta-1):

> Key regulator of cell-cell adhesion that associates with and regulates the cell adhesion properties of both C-, E- and N-cadherins, being critical for their surface stability. Promotes localization and retention of DSG3 at cell-cell junctions, via its interaction with DSG3. Beside cell-cell adhesion, regulates gene transcription through several transcription factors including ZBTB33/Kaiso2 and GLIS2, and the activity of Rho family GTPases and downstream cytoskeletal dynamics. Implicated both in …

**Summary**, from NCBI Gene [1500](https://www.ncbi.nlm.nih.gov/gene/1500):

> This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the neighboring upstream thioredoxin-related transmembrane protein 2 (TMX2) gene. [provided by RefSeq, …

**Accessions** — [HGNC:2515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2515) · Entrez [1500](https://www.ncbi.nlm.nih.gov/gene/1500) · UniProt [O60716](https://www.uniprot.org/uniprotkb/O60716) · Ensembl [ENSG00000198561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198561)

## Data

Gene col 12618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12618); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12618]; `tensor/DDL_lfc|DDL_z.npy` [12618]; `embed/gene_vectors.npy` [12618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12618 or target_col == 12618). Every well: [[CTNND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
