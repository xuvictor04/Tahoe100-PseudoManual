---
symbol: "ACTB"
type: "gene"
col: 1126
ensembl_id: "ENSG00000075624"
name: "actin beta"
location: "7p22.1"
module: 111
arm: "+"
pooled_cpm: 625.24
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# ACTB

*actin beta* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.23× (z +18.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.55× (z +4.3, q 0.002, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.623× (z -6.9, q 3e-09, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNA]] (+0.71, fdr 7e-06), [[TPM4]] (+0.67, fdr 7e-06), [[CORO1C]] (+0.62, fdr 7e-06); moves opposite to [[YBEY]] (-0.63, fdr 1e-05), [[LRSAM1]] (-0.62, fdr 1e-05), [[HSCB]] (-0.62, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.23×** | +18.8 | 0e+00 | 49/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.40×** | +16.7 | 0e+00 | 44/44 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.62×** | +12.2 | 4e-32 | 45/45 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.55×** | +4.3 | 0.002 | 38/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.52×** | +4.3 | 0.002 | 39/47 (SW 900, NCI-H460, …) | two highest doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.002 | 42/48 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.75×** | +4.1 | 0.003 | 41/48 (SW 900, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.005 | 35/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.009 | 37/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.43×** | +3.7 | 0.014 | 35/48 (NCI-H460, SW 900, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.42×** | +3.5 | 0.028 | 29/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.24×** | +3.1 | 0.089 | 30/49 (SK-MEL-2, SNU-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.78×** | +3.1 | 0.089 | 33/46 (SW 900, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -6.9 | 3e-09 | 35/49 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.743×** | -4.3 | 0.004 | 28/48 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.624×** | -4.0 | 0.013 | 33/48 (HepG2/C3A, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.684×** | -3.9 | 0.014 | 40/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Trimetrexate (drug)]] 5 µM |  | **0.771×** | -3.8 | 0.018 | 41/49 (SNU-1, C32, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.500×** | -3.7 | 0.019 | 35/45 (A-427, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.704×** | -3.5 | 0.041 | 36/47 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.714×** | -3.3 | 0.053 | 39/48 (RKO, A-427, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.540×** | -3.3 | 0.053 | 34/49 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.725×** | -3.3 | 0.053 | 28/48 (LoVo, HT-29, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.681×** | -3.2 | 0.062 | 40/49 (LS 180, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 290 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.7× (z +23.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.2) | — |
| [[A-172 (line)]] | wt | 664 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.71× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 467 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.23× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[A549 (line)]] | wt | 573 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.92× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 448 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.0× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +12.0) | — |
| [[A-427 (line)]] | wt | 691 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +14.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -18.3) |
| [[C-33 A (line)]] | alt | 348 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.77× (z +16.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.8) |
| [[C32 (line)]] | wt | 423 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.38× (z +17.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 638 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +14.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.7) |
| [[KATO III (line)]] | alt | 794 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +13.0) ⚠ toxic; transcription drop | [[Cabozantinib (S-malate) (drug)]] 5 µM 0.316× (z -9.4) |
| [[LoVo (line)]] | wt | 548 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.2) |
| [[LS 180 (line)]] | wt | 636 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 973 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +17.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 889 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +13.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 471 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +17.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -8.8) |
| [[SW48 (line)]] | wt | 547 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +14.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.1) |
| [[SW480 (line)]] | alt | 576 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +16.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.4) |
| [[A498 (line)]] | wt | 748 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +18.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 515 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.82× (z +14.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 638 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +11.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 310 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.37× (z +13.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 611 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.63× (z +16.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 412 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.05× (z +12.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 1,079 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +11.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 453 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -14.5) |
| [[HOP62 (line)]] | alt | 324 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +17.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 585 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.38× (z +15.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 587 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.37× (z +18.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 397 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +15.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 677 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +17.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 564 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +15.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 696 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 1,553 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 534 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +17.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 648 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.82× (z +16.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 562 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +15.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 426 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +15.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 318 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +16.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 482 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +15.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 576 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +15.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.1) |
| [[SNU-1 (line)]] | wt | 876 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 999 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +9.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 649 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 246 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +14.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 406 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 428 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 467 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 939 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 635 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNA]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 750 |
| [[TPM4]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 | STRING 496 |
| [[CORO1C]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | STRING 698 |
| [[WDR1]] | +0.62 | +0.68 / +0.60 | both halves | 7e-06 | STRING 709 |
| [[MYH9]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 991 |
| [[KRT8]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 | STRING 670 |
| [[ACTR3]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 | pathway: Clathrin-mediated endocytosis; STRING 957 |
| [[ANXA2]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 | STRING 767 |
| [[FKBP1A]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 | pathway: Oncogenic MAPK signaling |
| [[VMA21]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ACTG1]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 999 |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YBEY]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[LRSAM1]] | -0.62 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[HSCB]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[COG7]] | -0.62 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[WHAMM]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 | STRING 911 |
| [[SNHG32]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MPHOSPH8]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[ZMYM5]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ZNF766]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[FNBP4]] | -0.57 | -0.60 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.3, 25.3); signed map (-7.8, 35.1). **Vector** length 131, 52.7% of its response variance represented; |z| ≥ 3 in 1,388 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Platelet activation, signaling and aggregation* (reactome, mean cos +0.53 to 11); *RHO GTPases activate PAKs* (reactome, mean cos +0.56 to 4); *G-protein beta:gamma signalling* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +5.6 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.8 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | -6.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.9 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.9 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | actin beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,526,409-5,563,902 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Actins; BAF complex subunits; PBAF complex subunits; GBAF complex subunits |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 106 pathways, smallest: Insulin-like Growth Factor-2 mRNA Binding Proteins (IGF2BPs/IMPs/VICKZs) bind RNA; Folding of actin by CCT/TriC; Formation of annular gap junctions |
| Matched by | ensembl_id |

**Function**, from UniProt [P60709](https://www.uniprot.org/uniprotkb/P60709) (Actin, cytoplasmic 1):

> Actin is a highly conserved protein that polymerizes to produce filaments that form cross-linked networks in the cytoplasm of cells. Actin exists in both monomeric (G-actin) and polymeric (F-actin) forms, both forms playing key functions, such as cell motility and contraction. In addition to their role in the cytoplasmic cytoskeleton, G- and F-actin also localize in the nucleus, and regulate gene transcription and motility and repair of damaged DNA. Plays a role in the assembly of the …

**Summary**, from NCBI Gene [60](https://www.ncbi.nlm.nih.gov/gene/60):

> This gene encodes one of six different actin proteins. Actins are highly conserved proteins that are involved in cell motility, structure, integrity, and intercellular signaling. The encoded protein is a major constituent of the contractile apparatus and one of the two nonmuscle cytoskeletal actins that are ubiquitously expressed. Mutations in this gene cause Baraitser-Winter syndrome 1, which is characterized by intellectual disability with a distinctive facial appearance in human patients. …

**Accessions** — [HGNC:132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:132) · Entrez [60](https://www.ncbi.nlm.nih.gov/gene/60) · UniProt [P60709](https://www.uniprot.org/uniprotkb/P60709) · Ensembl [ENSG00000075624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075624)

## Data

Gene col 1126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1126); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1126]; `tensor/DDL_lfc|DDL_z.npy` [1126]; `embed/gene_vectors.npy` [1126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1126 or target_col == 1126). Every well: [[ACTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
