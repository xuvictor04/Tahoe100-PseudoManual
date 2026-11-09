---
symbol: "ANKRD27"
type: "gene"
col: 2557
ensembl_id: "ENSG00000105186"
name: "ankyrin repeat domain 27"
location: "19q13.11"
module: 77
arm: "+"
pooled_cpm: 59.24
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# ANKRD27

*ankyrin repeat domain 27* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.00× (z +16.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.459× (z -25.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.81, fdr 7e-06), [[TMEM120B]] (+0.80, fdr 7e-06), [[SH3PXD2B]] (+0.75, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.74, fdr 1e-05), [[BAZ2B]] (-0.74, fdr 1e-05), [[PATL2]] (-0.74, fdr 9e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +16.7 | 0e+00 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +16.0 | 0e+00 | 44/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +15.7 | 0e+00 | 44/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +8.2 | 4e-14 | 38/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +7.3 | 4e-11 | 36/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +7.1 | 9e-11 | 31/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.3 | 2e-08 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +4.8 | 9e-05 | 14/48 (NCI-H1792, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +4.1 | 0.002 | 14/47 (RPMI-7951, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 18/48 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.16× | +3.5 | 0.025 | 12/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.16× | +3.4 | 0.032 | 15/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.14× | +3.2 | 0.065 | 16/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2557.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.459×** | -25.6 | 0e+00 | 42/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.431×** | -19.3 | 0e+00 | 45/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.489×** | -17.1 | 0e+00 | 40/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.617×** | -10.7 | 2e-24 | 31/45 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.640×** | -10.7 | 2e-24 | 35/48 (HOP62, LOX-IMVI, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -8.8 | 1e-16 | 33/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -8.8 | 1e-16 | 33/48 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -8.7 | 3e-16 | 28/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -7.9 | 2e-13 | 29/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.722×** | -7.8 | 5e-13 | 31/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.715×** | -7.7 | 8e-13 | 29/41 (HEC-1-A, Panc 03.27, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -7.5 | 4e-12 | 32/49 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -7.3 | 1e-11 | 29/48 (A549, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.753×** | -6.8 | 6e-10 | 28/49 (A-427, A549, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.808×** | -5.1 | 1e-05 | 24/48 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -4.8 | 7e-05 | 21/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -4.1 | 0.001 | 17/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.846× | -3.7 | 0.006 | 15/47 (C32, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 0.906× | -3.3 | 0.028 | 9/48 (A549, HOP62, …) | top dose only | position effect removed |
| [[Olanzapine (drug)]] 5 µM |  | 0.906× | -3.2 | 0.035 | 4/48 (MIA PaCa-2, J82, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.914× | -2.9 | 0.078 | 4/48 (A-172, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 86.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -17.7) |
| [[HOP62 (line)]] | alt | 86.6 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -27.8) |
| [[A549 (line)]] | wt | 117 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -21.5) |
| [[HS-578T (line)]] | alt | 99.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 29.4 | 2 | 5 | [[Belinostat (drug)]] 5 µM 2.48× (z +9.5) | [[Harringtonine (drug)]] 0.5 µM 0.206× (z -16.5) |
| [[A498 (line)]] | wt | 64.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 70.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -30.4) |
| [[NCI-H2030 (line)]] | alt | 33.9 | 3 | 3 | [[Belinostat (drug)]] 5 µM 2.88× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -15.4) |
| [[PANC-1 (line)]] | alt | 80.3 | 2 | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.80× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -27.8) |
| [[SW480 (line)]] | alt | 55.3 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +12.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.479× (z -10.3) |
| [[LS 180 (line)]] | wt | 45.7 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 2.77× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 85.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -26.2) |
| [[NCI-H2347 (line)]] | alt | 41.4 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.15× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.9) |
| [[SW 900 (line)]] | alt | 48.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.4) |
| [[LoVo (line)]] | wt | 50.6 | 3 | 1 | [[Belinostat (drug)]] 5 µM 2.86× (z +13.3) | [[Harringtonine (drug)]] 5 µM 0.479× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 62.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -24.6) |
| [[RKO (line)]] | wt | 61.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.6) |
| [[BT-474 (line)]] | alt | 61.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.504× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 50.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -10.9) |
| [[J82 (line)]] | alt | 81.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 60.5 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 57.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.8) |
| [[SW1417 (line)]] | alt | 44.5 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.39× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.0) |
| [[SW48 (line)]] | wt | 60.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 50.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0978× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.546× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.5) |
| [[COLO 205 (line)]] | alt | 44.4 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.14× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 39.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.4) |
| [[SHP-77 (line)]] | alt | 48.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 47.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -11.5) |
| [[C-33 A (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.206× (z -9.8) ⚠ toxic |
| [[C32 (line)]] | wt | 39.0 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.102× (z -9.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 51.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.5) |
| [[HT-29 (line)]] | alt | 67.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -10.7) |
| [[KATO III (line)]] | alt | 45.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 27.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.309× (z -9.5) |
| [[NCI-H661 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.144× (z -10.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 64.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.1) |
| [[AN3 CA (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.81 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.80 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[SH3PXD2B]] | +0.75 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ATP7B]] | +0.75 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MGST3]] | +0.74 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[BICD2]] | +0.74 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[MAST3]] | +0.74 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[CAMKK1]] | +0.73 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[PCMT1]] | +0.73 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[LCMT1]] | +0.73 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[LPCAT4]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.73 | +0.61 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.74 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.74 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[PATL2]] | -0.74 | -0.74 / -0.36 | both halves | 9e-05 |  |
| [[TIA1]] | -0.74 | -0.77 / -0.55 | both halves | 1e-05 |  |
| [[DECR1]] | -0.74 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[LPXN]] | -0.73 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[PBLD]] | -0.73 | -0.72 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ZBED5]] | -0.72 | -0.70 / -0.37 | both halves | 7e-05 |  |
| [[RFX3-DT]] | -0.71 | -0.71 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ERCC6L2-AS1]] | -0.71 | -0.72 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[PPP3CB-AS1]] | -0.71 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[WARS2-AS1]] | -0.70 | -0.69 / -0.24 | both halves | 4e-04 |  |
| [[PNRC2]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[LEKR1]] | -0.70 | -0.74 / -0.36 | both halves | 9e-05 |  |
| [[LINC01004]] | -0.70 | -0.64 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ANKRD27's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00869-1]] | B | LINC00869-1 activity lowers ANKRD27's level | lines that do not express LINC00869-1 (7) vs lines expressing it (43) | 1.40× higher at baseline in the lines without LINC00869-1 | 0.031 | ⚠ within organs, on part of the lines; also absent: OSBPL10, STPG2, EIF4E3; maybe low, not absent |
| [[STARD9]] | B | STARD9 activity raises ANKRD27's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without STARD9 | 0.039 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises ANKRD27's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without SLC29A4 | 0.046 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[ASAP3]] | B | ASAP3 activity raises ANKRD27's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ASAP3 | 0.046 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ANKRD27's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ANKRD27's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM111A]] | C | FAM111A activity strengthens ANKRD27's drug response | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A respond 0.51× as strongly (z diff +1.75); strongest at Ouabain (Octahydrate) 5 µM: 1.16x vs 0.63x (z diff +5.6) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.860). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (0.3, 0.4); signed map (-40.8, -4.3). **Vector** length 130, 38.9% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +10.9 | +15.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.5 | +16.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +10.2 | +16.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.5 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.3 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.3 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.7 | -25.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.5 | -19.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -17.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.6 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,597,006-32,676,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00040, DKFZp434L0718, VARP |
| Gene groups (HGNC) | Ankyrin repeat domain containing; VPS9 domain containing; Small nucleolar RNA protein coding host genes |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NW4](https://www.uniprot.org/uniprotkb/Q96NW4) (Ankyrin repeat domain-containing protein 27):

> May be a guanine exchange factor (GEF) for Rab21, Rab32 and Rab38 and regulate endosome dynamics. May regulate the participation of VAMP7 in membrane fusion events; in vitro inhibits VAMP7-mediated SNARE complex formation by trapping VAMP7 in a closed, fusogenically inactive conformation. Involved in peripheral melanosomal distribution of TYRP1 in melanocytes; the function, which probably is implicating vesicle-trafficking, includes cooperation with Rab32, Rab38 and VAMP7 (By similarity). …

**Summary**, from NCBI Gene [84079](https://www.ncbi.nlm.nih.gov/gene/84079):

> Enables guanyl-nucleotide exchange factor activity and small GTPase binding activity. Involved in endocytic recycling and negative regulation of SNARE complex assembly. Acts upstream of or within early endosome to late endosome transport. Located in endosome; lysosome; and plasma membrane. Implicated in eosinophilic esophagitis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25310) · Entrez [84079](https://www.ncbi.nlm.nih.gov/gene/84079) · UniProt [Q96NW4](https://www.uniprot.org/uniprotkb/Q96NW4) · Ensembl [ENSG00000105186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105186)

## Data

Gene col 2557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2557); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2557]; `tensor/DDL_lfc|DDL_z.npy` [2557]; `embed/gene_vectors.npy` [2557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2557 or target_col == 2557). Every well: [[ANKRD27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
