---
symbol: "MTMR12"
type: "gene"
col: 7454
ensembl_id: "ENSG00000150712"
name: "myotubularin related protein 12"
location: "5p13.3"
module: 77
arm: "+"
pooled_cpm: 63.41
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# MTMR12

*myotubularin related protein 12* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.45× (z +9.6, q 5e-19, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.464× (z -18.4, q 0e+00, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.708× (z -12.7, q 1e-34, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF5L]] (+0.74, fdr 9e-06), [[TRIM35]] (+0.67, fdr 3e-05), [[GFOD2]] (+0.66, fdr 1e-05); moves opposite to [[NQO1-DT]] (-0.64, fdr 4e-05), [[TIA1]] (-0.63, fdr 2e-05), [[AKT1S1]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +9.6 | 5e-19 | 40/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +8.7 | 8e-16 | 37/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +7.5 | 1e-11 | 34/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +7.1 | 2e-10 | 0/49 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.7 | 1e-06 | 27/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +5.2 | 2e-05 | 23/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.6 | 4e-04 | 19/49 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.2 | 0.002 | 21/48 (SW 900, SW1417, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.6 | 0.020 | 4/48 (SW48, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.13× | +3.2 | 0.077 | 9/49 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.09× | +3.2 | 0.077 | 11/48 (HEC-1-A, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.079 | 7/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.085 | 10/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +3.0 | 0.098 | 7/48 (Panc 03.27, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.464×** | -18.4 | 0e+00 | 37/44 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.502×** | -17.9 | 0e+00 | 40/49 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -17.0 | 0e+00 | 35/41 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.708×** | -12.7 | 1e-34 | 32/48 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -8.4 | 6e-15 | 29/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.737×** | -7.6 | 3e-12 | 29/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -7.4 | 1e-11 | 31/48 (HT-29, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.873× | -5.0 | 4e-05 | 19/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.840× | -4.5 | 3e-04 | 21/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.838× | -4.4 | 5e-04 | 20/49 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.854× | -4.1 | 0.002 | 22/48 (A-172, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.864× | -3.8 | 0.007 | 20/48 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.4 | 0.027 | 13/48 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.2 | 0.055 | 13/48 (LoVo, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.1 | 0.064 | 13/48 (H4, HOP62, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.886× | -3.0 | 0.078 | 8/48 (AsPC-1, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 64.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -20.0) |
| [[LOX-IMVI (line)]] | wt | 67.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 49.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.480× (z -13.7) |
| [[A498 (line)]] | wt | 60.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.457× (z -9.7) |
| [[A549 (line)]] | wt | 64.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -11.5) |
| [[J82 (line)]] | alt | 85.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 78.4 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.49× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -20.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 80.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -13.4) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.602× (z -9.6) |
| [[HS-578T (line)]] | alt | 74.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 81.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.612× (z -9.4) |
| [[PANC-1 (line)]] | alt | 63.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.659× (z -10.3) |
| [[SW 900 (line)]] | alt | 85.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -12.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 53.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.45× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -16.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -17.7) |
| [[BT-474 (line)]] | alt | 105 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.50× (z +9.7) | [[Lonafarnib (drug)]] 5 µM 0.136× (z -11.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 74.9 | 2 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 2.62× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.05 µM 2.01× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 56.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 75.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.579× (z -8.7) |
| [[HT-29 (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.327× (z -10.0) |
| [[LoVo (line)]] | wt | 60.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0639× (z -35.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -14.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -15.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.5) ⚠ cell-cycle shift, explains ~5% of this change |
| [[H4 (line)]] | wt | 49.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -10.2) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HepG2_C3A (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[KATO III (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.5) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[NCI-H1573 (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -18.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 55.2 | 1 | 0 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 1.72× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -11.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -15.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 85.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.466× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | +0.74 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[TRIM35]] | +0.67 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[GFOD2]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.66 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.66 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CSK]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ESS2]] | +0.65 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[POMGNT2]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.64 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[CCNQ]] | +0.64 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[LCMT1]] | +0.63 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[BRF1]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NQO1-DT]] | -0.64 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[TIA1]] | -0.63 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[AKT1S1]] | -0.63 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[LYRM1]] | -0.62 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TSGA10]] | -0.61 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.60 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[TAF9B]] | -0.59 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | -0.59 | -0.60 / -0.23 | both halves | 5e-04 |  |
| [[TENM3-AS1]] | -0.59 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[DCAF8]] | -0.59 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[CYB5D2]] | -0.58 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[NANOS3]] | -0.58 | -0.53 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MTMR12's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.8, -0.3); signed map (-43.0, -3.4). **Vector** length 102, 24.3% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.1 | +8.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.7 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:32,226,994-32,312,987 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 3-PAP, FLJ20476, KIAA1682, 3PAP; previously PIP3AP |
| Gene groups (HGNC) | Myotubularins |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the early endosome membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0I1](https://www.uniprot.org/uniprotkb/Q9C0I1) (Myotubularin-related protein 12):

> Acts as an adapter for the myotubularin-related phosphatases. Regulates phosphatase MTM1 protein stability and possibly its intracellular location. By stabilizing MTM1 protein levels, required for skeletal muscle maintenance but not for myogenesis (By similarity).

**Summary**, from NCBI Gene [54545](https://www.ncbi.nlm.nih.gov/gene/54545):

> Phosphatidylinositide 3-kinase-derived membrane-anchored phosphatidylinositides, such as phosphatidylinositol 3-phosphate (PtdIns(3)P), regulate diverse cellular processes. The protein encoded by this gene functions as an adaptor subunit in a complex with an active PtdIns(3)P 3-phosphatase. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:18191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18191) · Entrez [54545](https://www.ncbi.nlm.nih.gov/gene/54545) · UniProt [Q9C0I1](https://www.uniprot.org/uniprotkb/Q9C0I1) · Ensembl [ENSG00000150712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150712)

## Data

Gene col 7454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7454); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7454]; `tensor/DDL_lfc|DDL_z.npy` [7454]; `embed/gene_vectors.npy` [7454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7454 or target_col == 7454). Every well: [[MTMR12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
