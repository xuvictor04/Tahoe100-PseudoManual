---
symbol: "EPHA4"
type: "gene"
col: 3759
ensembl_id: "ENSG00000116106"
name: "EPH receptor A4"
location: "2q36.1"
module: 235
arm: "+"
pooled_cpm: 59.12
n_lines_expressing: 31
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/235"]
generated_by: "tahoemap"
---

# EPHA4

*EPH receptor A4* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.8× (z +49.1, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.674× (z -5.3, q 6e-05, down in 19 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.798× (z -4.6, q 1e-03, down in 16 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINE2]] (+0.63, fdr 1e-05), [[CTSC]] (+0.58, fdr 1e-05), [[PCDH10]] (+0.58, fdr 1e-05); moves opposite to [[PSMD9]] (-0.55, fdr 1e-05), [[E4F1]] (-0.47, fdr 4e-05), [[ACTR10]] (-0.47, fdr 4e-05).
> It is in [[Module 235]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[DUSP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.8×** | +49.1 | 0e+00 | 29/29 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **7.69×** | +28.6 | 0e+00 | 27/31 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.16×** | +27.6 | 0e+00 | 26/29 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +24.4 | 0e+00 | 18/29 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.98×** | +14.1 | 5e-43 | 21/29 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.58×** | +13.8 | 2e-41 | 17/29 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +12.7 | 4e-35 | 23/29 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.21×** | +11.6 | 5e-29 | 20/29 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.87×** | +9.1 | 4e-18 | 17/29 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +8.0 | 9e-14 | 17/29 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +6.9 | 3e-10 | 17/29 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.2 | 3e-08 | 14/29 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +6.1 | 5e-08 | 16/29 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.1 | 5e-08 | 20/29 (MIA PaCa-2, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.47×** | +5.4 | 3e-06 | 14/28 (CFPAC-1, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 1e-04 | 14/29 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +4.3 | 5e-04 | 11/30 (NCI-H2347, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +4.3 | 5e-04 | 17/29 (COLO 205, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.008 | 7/29 (BT-474, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.674×** | -5.3 | 6e-05 | 19/27 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -4.6 | 1e-03 | 16/30 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.715×** | -4.5 | 0.001 | 10/29 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.747×** | -4.3 | 0.003 | 15/29 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.819×** | -3.9 | 0.011 | 9/29 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.796×** | -3.7 | 0.020 | 12/29 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.765×** | -3.6 | 0.025 | 11/31 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.792×** | -3.4 | 0.046 | 14/29 (SW480, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.824×** | -3.3 | 0.059 | 8/29 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.845× | -3.3 | 0.059 | 9/30 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Menadione (drug)]] 5 µM |  | 0.807× | -3.0 | 0.13 | 8/28 (SW 900, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 119 | 3 | 13 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.1) | [[Binimetinib (drug)]] 0.5 µM 0.283× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 22.2 | 10 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.2× (z +29.5) | — |
| [[SW1417 (line)]] | alt | 25.9 | 10 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.9× (z +22.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 387 | 5 (1 ⚠) | 3 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.86× (z +19.9) ⚠ position not correctable · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 43.2 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +26.1) | — |
| [[A498 (line)]] | wt | 18.0 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +27.7) | — |
| [[HOP62 (line)]] | alt | 22.4 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.3× (z +31.2) | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.1 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 44.4× (z +28.7) | — |
| [[HS-578T (line)]] | alt | 56.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +19.7) | — |
| [[J82 (line)]] | alt | 50.3 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +22.3) | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +19.6) | — |
| [[SK-MEL-2 (line)]] | alt | 63.1 | 3 | 2 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +16.9) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.251× (z -8.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[BT-474 (line)]] | alt | 57.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.68× (z +18.8) | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +24.3) | — |
| [[LS 180 (line)]] | wt | 118 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 16.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.9× (z +22.2) | — |
| [[SNU-423 (line)]] | alt | 40.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +20.6) | — |
| [[SW 900 (line)]] | alt | 81.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.0610× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 33.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 71.5 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 135 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 300 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 65.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.4× (z +20.8) | — |
| [[LoVo (line)]] | wt | 54.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +20.1) | — |
| [[A-427 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.28 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.89 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINE2]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[CTSC]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PCDH10]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PCDH17]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CEMIP2]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[LINC00534]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[RGS2]] | +0.52 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DIO3OS]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[EXTL2]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CDH11]] | +0.50 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[LINC02320]] | +0.49 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[PTGER4]] | +0.48 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD9]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[E4F1]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ACTR10]] | -0.47 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[COMMD2]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[RWDD1]] | -0.45 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[MBD2]] | -0.44 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SVIL-AS1-1]] | -0.44 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[SH3GLB1]] | -0.43 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[DPH7]] | -0.43 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[HERC2P2]] | -0.43 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[PARP2]] | -0.42 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[FXR2]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EPHA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02320]] | B | LINC02320 activity raises EPHA4's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 2.23× lower at baseline in the lines without LINC02320 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[MAP2K2]] | B | MAP2K2 activity raises EPHA4's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP4]] | B | EPHA4 activity raises DUSP4's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without EPHA4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |
| [[EFNB2]] | B | EPHA4 activity raises EFNB2's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without EPHA4 | 0.014 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |
| [[SOX9]] | B | EPHA4 activity raises SOX9's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without EPHA4 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |
| [[LPAR6]] | B | EPHA4 activity strengthens LPAR6's drug response | lines that do not express EPHA4 (19) vs lines expressing it (29) | the lines without EPHA4 respond 0.41× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 1.11x vs 3.60x (z diff +5.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10; target measured in part of the lines; artifact flags |
| [[NEFM]] | B | EPHA4 activity raises NEFM's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without EPHA4 | 0.089 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |
| [[SOX11]] | C | EPHA4 activity raises SOX11's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without EPHA4 | 0.082 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10; co-absent with the target |

## Where it sits

- **Module**: [[Module 235]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.6, 30.6); signed map (38.0, 30.8). **Vector** length 105, 28.8% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +28.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +49.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +27.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +14.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.5 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -4.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.2 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:221,418,027-221,574,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hek8; previously TYRO1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 8 pathways, smallest: EPHA-mediated growth cone collapse; Somitogenesis; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P54764](https://www.uniprot.org/uniprotkb/P54764) (Ephrin type-A receptor 4):

> Receptor tyrosine kinase which binds membrane-bound ephrin family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Highly promiscuous, it has the unique property among Eph receptors to bind and to be physiologically activated by both GPI-anchored …

**Summary**, from NCBI Gene [2043](https://www.ncbi.nlm.nih.gov/gene/2043):

> This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and their …

**Accessions** — [HGNC:3388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3388) · Entrez [2043](https://www.ncbi.nlm.nih.gov/gene/2043) · UniProt [P54764](https://www.uniprot.org/uniprotkb/P54764) · Ensembl [ENSG00000116106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116106)

## Data

Gene col 3759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3759); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3759]; `tensor/DDL_lfc|DDL_z.npy` [3759]; `embed/gene_vectors.npy` [3759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3759 or target_col == 3759). Every well: [[EPHA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
