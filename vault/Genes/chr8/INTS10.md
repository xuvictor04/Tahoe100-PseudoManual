---
symbol: "INTS10"
type: "gene"
col: 2475
ensembl_id: "ENSG00000104613"
name: "integrator complex subunit 10"
location: "8p21.3"
module: 40
arm: "+"
pooled_cpm: 60.95
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# INTS10

*integrator complex subunit 10* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.79× (z +13.3, q 8e-38, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.237× (z -49.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCB1]] (+0.63, fdr 1e-05), [[ANKRD39]] (+0.60, fdr 1e-05), [[NFATC3]] (+0.60, fdr 8e-06); moves opposite to [[FNBP1P1]] (-0.63, fdr 1e-05), [[PNRC2]] (-0.62, fdr 1e-05), [[PPP1R1C]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +13.3 | 8e-38 | 40/48 (LOX-IMVI, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +10.0 | 4e-21 | 35/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +9.1 | 2e-17 | 35/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **1.28×** | +5.7 | 2e-06 | 23/46 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.0 | 7e-05 | 20/45 (SNU-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.007 | 14/49 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.8 | 0.013 | 13/48 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.7 | 0.014 | 19/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.12 | 13/48 (NCI-H2347, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.14 | 12/49 (NCI-H23, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.237×** | -49.2 | 0e+00 | 48/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.339×** | -25.2 | 0e+00 | 46/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.418×** | -21.1 | 0e+00 | 43/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.542×** | -14.8 | 0e+00 | 39/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -14.7 | 0e+00 | 41/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -13.1 | 3e-37 | 40/49 (LOX-IMVI, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -12.3 | 7e-33 | 34/48 (A498, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -12.2 | 2e-32 | 35/48 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.610×** | -11.9 | 5e-31 | 36/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.675×** | -8.8 | 1e-16 | 25/45 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.783×** | -8.3 | 4e-15 | 25/48 (HS-578T, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.705×** | -7.8 | 3e-13 | 31/47 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -7.5 | 3e-12 | 26/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.784×** | -5.9 | 2e-07 | 22/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.792×** | -5.6 | 7e-07 | 23/48 (A498, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.663×** | -5.2 | 7e-06 | 24/48 (HS-578T, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.812×** | -5.0 | 2e-05 | 22/48 (A-172, SW480, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -4.0 | 0.002 | 20/48 (HS-578T, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 107 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -30.8) |
| [[A-172 (line)]] | wt | 52.5 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -28.5) |
| [[A498 (line)]] | wt | 114 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -37.3) |
| [[hTERT-HPNE (line)]] | wt | 90.7 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -26.1) |
| [[NCI-H460 (line)]] | wt | 62.3 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -42.3) |
| [[NCI-H1573 (line)]] | alt | 53.2 | 2 | 6 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -27.5) |
| [[LOX-IMVI (line)]] | wt | 42.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -29.0) |
| [[H4 (line)]] | wt | 87.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -26.6) |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -31.8) |
| [[SNU-1 (line)]] | wt | 69.1 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0965× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 38.2 | 1 | 4 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -21.2) |
| [[C32 (line)]] | wt | 48.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -24.8) |
| [[HOP62 (line)]] | alt | 40.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -26.3) |
| [[KATO III (line)]] | alt | 79.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.345× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 82.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -33.7) |
| [[RKO (line)]] | wt | 72.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.0) |
| [[SW 900 (line)]] | alt | 57.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.0) |
| [[A549 (line)]] | wt | 68.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 71.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -37.4) |
| [[NCI-H2347 (line)]] | alt | 44.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -26.2) |
| [[PANC-1 (line)]] | alt | 37.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -22.2) |
| [[RPMI-7951 (line)]] | alt | 58.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -28.1) |
| [[SK-MEL-2 (line)]] | alt | 43.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -17.0) |
| [[SW480 (line)]] | alt | 95.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -20.5) |
| [[A-427 (line)]] | wt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -13.2) |
| [[C-33 A (line)]] | alt | 66.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.4) |
| [[HCT15 (line)]] | alt | 87.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -15.9) |
| [[Hs 766T (line)]] | wt | 65.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -20.1) |
| [[J82 (line)]] | alt | 21.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.3) |
| [[LoVo (line)]] | wt | 51.3 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -21.1) |
| [[LS 180 (line)]] | wt | 69.6 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.561× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 56.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.2) |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -17.7) |
| [[SW 1088 (line)]] | alt | 76.0 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0527× (z -10.2) |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.6) |
| [[SW48 (line)]] | wt | 91.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.2) |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -13.9) |
| [[CHP-212 (line)]] | wt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.2) |
| [[COLO 205 (line)]] | alt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 59.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.5) |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.3) |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.2) |
| [[AN3 CA (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCB1]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[NFATC3]] | +0.60 | +0.63 / +0.57 | both halves | 8e-06 |  |
| [[DUXAP10]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[NBAS]] | +0.59 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[OXNAD1]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[RNF216]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PRKRA]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ORC3]] | +0.58 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[IQSEC2]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNBP1P1]] | -0.63 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.62 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[PPP1R1C]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PDCL3P4]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[TRIM8]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CHMP4B]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[NOP14-AS1]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[LINC02340]] | -0.58 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[MMRN2]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[LPXN]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SKIL]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers INTS10's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AMIGO2]] | B | AMIGO2 activity lowers INTS10's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without AMIGO2 | 0.095 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.4, -21.8); signed map (-52.6, -1.6). **Vector** length 131, 39.7% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.7 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.8 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.6 | +9.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.9 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.6 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.4 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.8 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -49.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -25.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -21.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.7 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:19,817,391-19,852,083 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10569, INT10; previously C8orf35 |
| Gene groups (HGNC) | Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVR2](https://www.uniprot.org/uniprotkb/Q9NVR2) (Integrator complex subunit 10):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [55174](https://www.ncbi.nlm.nih.gov/gene/55174):

> INTS10 is a subunit of the Integrator complex, which associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690) (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25548) · Entrez [55174](https://www.ncbi.nlm.nih.gov/gene/55174) · UniProt [Q9NVR2](https://www.uniprot.org/uniprotkb/Q9NVR2) · Ensembl [ENSG00000104613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104613)

## Data

Gene col 2475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2475); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2475]; `tensor/DDL_lfc|DDL_z.npy` [2475]; `embed/gene_vectors.npy` [2475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2475 or target_col == 2475). Every well: [[INTS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
