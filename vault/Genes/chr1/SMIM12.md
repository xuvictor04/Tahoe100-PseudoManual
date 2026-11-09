---
symbol: "SMIM12"
type: "gene"
col: 8794
ensembl_id: "ENSG00000163866"
name: "small integral membrane protein 12"
location: "1p34.3"
module: 15
arm: "+"
pooled_cpm: 19.8
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SMIM12

*small integral membrane protein 12* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +19.3, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.646× (z -5.9, q 2e-06, down in 20 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.691× (z -5.4, q 1e-05, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LoVo 0.177×, A-172 0.156×, HOP62 0.193×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.116×, HEC-1-A 0.176×, A-172 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SW480 0.293×, PANC-1 0.253×, BT-474 0.166×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.268×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM186]] (+0.66, fdr 7e-06), [[MYH3]] (+0.65, fdr 1e-05), [[TMEM187]] (+0.63, fdr 1e-05); moves opposite to [[TTC21B]] (-0.63, fdr 1e-05), [[ZDHHC20]] (-0.63, fdr 1e-05), [[PGAP1]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +19.3 | 0e+00 | 45/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +12.3 | 4e-32 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +10.4 | 5e-23 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +9.8 | 1e-20 | 37/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +9.6 | 8e-20 | 30/47 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +8.8 | 1e-16 | 40/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +7.8 | 4e-13 | 33/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.7 | 1e-06 | 23/43 (NCI-H1573, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +4.9 | 6e-05 | 24/47 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.9 | 6e-05 | 22/48 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.9 | 6e-05 | 22/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.8 | 7e-05 | 22/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 20/47 (SW480, A498, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.6 | 2e-04 | 24/47 (NCI-H23, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.001 | 19/48 (HT-29, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.005 | 14/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8794.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LoVo 0.177×, A-172 0.156×, HOP62 0.193×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.116×, HEC-1-A 0.176×, A-172 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SW480 0.293×, PANC-1 0.253×, BT-474 0.166×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.268×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.646×** | -5.9 | 2e-06 | 20/35 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.691×** | -5.4 | 1e-05 | 23/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -5.4 | 1e-05 | 25/47 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.709×** | -5.0 | 8e-05 | 25/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.712×** | -5.0 | 8e-05 | 20/39 (SW480, HEC-1-A, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.644×** | -3.3 | 0.075 | 13/38 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.854× | -3.3 | 0.075 | 11/48 (CHP-212, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.792×** | -3.3 | 0.075 | 17/30 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.656×** | -3.2 | 0.082 | 15/46 (KATO III, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.1 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.21× (z +14.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -12.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 43.2 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -14.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 19.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +13.4) | [[AZD2858 (drug)]] 0.5 µM 0.0524× (z -13.2) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 17.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +14.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -11.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 30.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.8) |
| [[A549 (line)]] | wt | 15.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -9.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 15.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 28.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 23.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 11.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +12.6) | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -9.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.2) | — |
| [[KATO III (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 18.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.2) | — |
| [[RKO (line)]] | wt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +10.8) | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM186]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MYH3]] | +0.65 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[TMEM187]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CKMT2-AS1]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[UBAP1L]] | +0.61 | +0.73 / +0.46 | both halves | 2e-05 |  |
| [[ANKRD17-DT]] | +0.61 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[SMUG1]] | +0.61 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.60 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[LTO1]] | +0.59 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[TLNRD1]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TECPR2]] | +0.57 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[GRK4]] | +0.57 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC21B]] | -0.63 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ZDHHC20]] | -0.63 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[PGAP1]] | -0.61 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[ADD3]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ALDH7A1]] | -0.59 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[HMGN3]] | -0.59 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[SCP2]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[HLTF]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CERS6]] | -0.58 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[MNS1]] | -0.57 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[MAPRE2]] | -0.57 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[NDRG3]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMIM12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises SMIM12's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (11.3, 5.9); signed map (18.9, -6.9). **Vector** length 85.9, 18.5% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +19.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.6 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -3.2 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:34,712,737-34,859,755 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90372; previously C1orf212 |
| Matched by | ensembl_id |

UniProt [Q96EX1](https://www.uniprot.org/uniprotkb/Q96EX1) carries no function annotation.

**Summary**, from NCBI Gene [113444](https://www.ncbi.nlm.nih.gov/gene/113444):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25154) · Entrez [113444](https://www.ncbi.nlm.nih.gov/gene/113444) · UniProt [Q96EX1](https://www.uniprot.org/uniprotkb/Q96EX1) · Ensembl [ENSG00000163866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163866)

## Data

Gene col 8794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8794); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8794]; `tensor/DDL_lfc|DDL_z.npy` [8794]; `embed/gene_vectors.npy` [8794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8794 or target_col == 8794). Every well: [[SMIM12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
