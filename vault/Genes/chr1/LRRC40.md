---
symbol: "LRRC40"
type: "gene"
col: 831
ensembl_id: "ENSG00000066557"
name: "leucine rich repeat containing 40"
location: "1p31.1"
module: 65
arm: "+"
pooled_cpm: 52.06
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# LRRC40

*leucine rich repeat containing 40* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.03× (z +10.0, q 9e-21, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.583× (z -7.6, q 2e-11, down in 35 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.713× (z -4.8, q 3e-04, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.0807×, HCT15 0.0912×, H4 0.141×, C-33 A 0.165×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (H4 0.114×, SHP-77 0.301×, NCI-H1573 0.313×, NCI-H1792 0.313×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.151×, SNU-423 0.297×, NCI-H2030 0.287×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.378×); [[Ixazomib (drug)]] 5 µM in 1 line (H4 0.0827×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG9]] (+0.64, fdr 7e-06), [[MRPL39]] (+0.64, fdr 7e-06), [[SPATA7]] (+0.61, fdr 2e-05); moves opposite to [[LINC02284]] (-0.58, fdr 1e-05), [[TXNRD1]] (-0.53, fdr 4e-05), [[TUT7]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +10.0 | 9e-21 | 41/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +7.4 | 3e-11 | 41/49 (SW480, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.1 | 2e-07 | 33/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +5.4 | 8e-06 | 29/48 (RKO, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 2e-05 | 29/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 1e-04 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.7 | 2e-04 | 26/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +4.6 | 2e-04 | 29/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.010 | 24/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.020 | 22/48 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.039 | 18/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.24× | +3.1 | 0.11 | 21/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.24× | +3.0 | 0.11 | 22/48 (LoVo, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.0807×, HCT15 0.0912×, H4 0.141×, C-33 A 0.165×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (H4 0.114×, SHP-77 0.301×, NCI-H1573 0.313×, NCI-H1792 0.313×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.151×, SNU-423 0.297×, NCI-H2030 0.287×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.378×); [[Ixazomib (drug)]] 5 µM in 1 line (H4 0.0827×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -7.6 | 2e-11 | 35/47 (H4, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -7.1 | 3e-10 | 30/41 (Panc 03.27, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -4.8 | 3e-04 | 32/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.695×** | -4.7 | 3e-04 | 27/44 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.725×** | -4.5 | 7e-04 | 26/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.847× | -3.3 | 0.086 | 15/48 (CHP-212, SW 900, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.1 | 0.15 | 22/48 (RPMI-7951, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +12.8) | — |
| [[SW480 (line)]] | alt | 57.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +15.4) | — |
| [[AsPC-1 (line)]] | alt | 44.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +11.1) | — |
| [[H4 (line)]] | wt | 87.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib (drug)]] 5 µM 0.0827× (z -8.8) |
| [[LoVo (line)]] | wt | 36.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.84× (z +16.2) | — |
| [[LS 180 (line)]] | wt | 48.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 54.7 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 62.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +13.7) | — |
| [[HepG2_C3A (line)]] | wt | 36.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.91× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.378× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 37.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 57.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +10.4) | — |
| [[A-172 (line)]] | wt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -14.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -12.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 74.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0912× (z -16.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 23.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +9.1) | — |
| [[KATO III (line)]] | alt | 27.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.63× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -9.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -20.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 50.7 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0657× (z -9.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 52.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +9.4) | — |
| [[SW48 (line)]] | wt | 54.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.99× (z +8.8) | — |
| [[A498 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG9]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MRPL39]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SPATA7]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[MINDY3]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.60 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[COPS4]] | +0.58 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.57 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[MRS2]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[NUP54]] | +0.57 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[CDADC1]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[AP3S1]] | +0.56 | +0.62 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02284]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TXNRD1]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[TUT7]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[SETX]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PLEKHA6]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[NECAB2]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[EIF4G3]] | -0.50 | -0.65 / -0.37 | both halves | 8e-05 |  |
| [[LINC01033]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[POU2F2]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[DNTTIP2]] | -0.49 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[NFE2L2]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers LRRC40's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without PLEKHA6 | 0.052 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[STARD9]] | B | STARD9 activity raises LRRC40's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without STARD9 | 0.062 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.6, -10.2); signed map (-30.5, -12.9). **Vector** length 87.0, 22.6% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:70,144,805-70,205,579 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20331 |
| Matched by | ensembl_id |

UniProt [Q9H9A6](https://www.uniprot.org/uniprotkb/Q9H9A6) carries no function annotation.

**Summary**, from NCBI Gene [55631](https://www.ncbi.nlm.nih.gov/gene/55631):

> Predicted to be involved in intracellular signal transduction. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26004) · Entrez [55631](https://www.ncbi.nlm.nih.gov/gene/55631) · UniProt [Q9H9A6](https://www.uniprot.org/uniprotkb/Q9H9A6) · Ensembl [ENSG00000066557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066557)

## Data

Gene col 831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 831); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 831]; `tensor/DDL_lfc|DDL_z.npy` [831]; `embed/gene_vectors.npy` [831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 831 or target_col == 831). Every well: [[LRRC40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
