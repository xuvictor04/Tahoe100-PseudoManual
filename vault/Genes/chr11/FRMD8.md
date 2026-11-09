---
symbol: "FRMD8"
type: "gene"
col: 4732
ensembl_id: "ENSG00000126391"
name: "FERM domain containing 8"
location: "11q13.1"
module: 160
arm: "+"
pooled_cpm: 39.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# FRMD8

*FERM domain containing 8* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.91× (z +8.7, q 1e-15, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.418× (z -16.6, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM89B]] (+0.66, fdr 1e-05), [[TMEM184B]] (+0.65, fdr 7e-06), [[MYO9B]] (+0.64, fdr 1e-05); moves opposite to [[ZXDA]] (-0.65, fdr 2e-05), [[ATP5PB]] (-0.61, fdr 1e-05), [[DIS3L]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABHD17C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +8.7 | 1e-15 | 39/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +7.5 | 1e-11 | 38/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.58×** | +6.2 | 1e-07 | 34/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.8 | 9e-07 | 30/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +5.6 | 2e-06 | 29/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.2 | 2e-05 | 24/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.67×** | +4.9 | 1e-04 | 28/47 (NCI-H1573, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 0.002 | 23/46 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.004 | 20/47 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.008 | 21/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.020 | 19/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.025 | 20/48 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.035 | 21/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.28×** | +3.3 | 0.038 | 17/47 (SW480, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.090 | 10/46 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.090 | 12/48 (SW1417, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.418×** | -16.6 | 0e+00 | 42/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.434×** | -10.8 | 1e-24 | 41/47 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.450×** | -10.6 | 5e-24 | 41/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.223×** | -8.8 | 2e-16 | 38/49 (Hs 766T, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.303×** | -7.0 | 3e-10 | 40/46 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -6.4 | 1e-08 | 32/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.636×** | -6.1 | 9e-08 | 34/48 (SW48, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.757×** | -5.3 | 8e-06 | 29/48 (HT-29, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -4.8 | 1e-04 | 22/34 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.728×** | -4.3 | 0.001 | 26/48 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.722×** | -4.1 | 0.002 | 25/48 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.749×** | -3.7 | 0.008 | 21/47 (RPMI-7951, HepG2/C3A, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -3.7 | 0.010 | 21/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.010 | 18/48 (NCI-H460, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.6 | 0.010 | 23/48 (HT-29, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.758×** | -3.6 | 0.011 | 21/47 (NCI-H661, NCI-H460, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.759×** | -3.5 | 0.015 | 20/48 (HT-29, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.3 | 2 | 3 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.41× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 82.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -15.1) |
| [[HS-578T (line)]] | alt | 30.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.4) |
| [[LoVo (line)]] | wt | 69.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -18.6) |
| [[SNU-1 (line)]] | wt | 89.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0960× (z -21.1) |
| [[A-172 (line)]] | wt | 41.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.3) |
| [[HT-29 (line)]] | alt | 59.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 50.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -10.3) |
| [[SW 900 (line)]] | alt | 65.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.2) |
| [[SW48 (line)]] | wt | 129 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -14.4) |
| [[SW480 (line)]] | alt | 25.9 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.38× (z +11.0) | — |
| [[A549 (line)]] | wt | 37.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.3) |
| [[C32 (line)]] | wt | 57.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.5) |
| [[Hs 766T (line)]] | wt | 129 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.0) |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 1 | 1 | [[Belinostat (drug)]] 5 µM 3.71× (z +9.4) | [[TAK-901 (drug)]] 5 µM 0.0544× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 56.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0852× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0390× (z -18.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 40.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.6) |
| [[H4 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -9.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0906× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.8) |
| [[PANC-1 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -12.5) |
| [[RKO (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -9.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.3) |
| [[SW1417 (line)]] | alt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.8) |
| [[A-427 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89B]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 | STRING 546 |
| [[TMEM184B]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CDC34]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PLIN3]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CSNK1E]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CYTH1]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CSNK1G2]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CIB1]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.65 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ATP5PB]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[CC2D2A]] | -0.61 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[USP24]] | -0.60 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[CFL2]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[CILK1]] | -0.58 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[FAM204A]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MRPL30]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[NNT]] | -0.58 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[FUBP1]] | -0.57 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MBTPS2]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | ABHD17C activity raises FRMD8's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.42× lower at baseline in the lines without ABHD17C | 0.082 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (4.7, 1.7); signed map (-13.2, 38.6). **Vector** length 127, 37.7% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.0 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +3.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.1 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -16.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.5 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.5 | -5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.5 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.9 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,386,621-65,413,525 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90369, FKSG44, iTAP |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZ67](https://www.uniprot.org/uniprotkb/Q9BZ67) (FERM domain-containing protein 8):

> Promotes the cell surface stability of iRhom1/RHBDF1 and iRhom2/RHBDF2 and prevents their degradation via the endolysosomal pathway. By acting on iRhoms, involved in ADAM17-mediated shedding of TNF, amphiregulin/AREG, HBEGF and TGFA from the cell surface. Negatively regulates Wnt signaling, possibly by antagonizing the recruitment of AXIN1 to LRP6.

**Summary**, from NCBI Gene [83786](https://www.ncbi.nlm.nih.gov/gene/83786):

> Involved in positive regulation of tumor necrosis factor production. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25462) · Entrez [83786](https://www.ncbi.nlm.nih.gov/gene/83786) · UniProt [Q9BZ67](https://www.uniprot.org/uniprotkb/Q9BZ67) · Ensembl [ENSG00000126391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126391)

## Data

Gene col 4732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4732); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4732]; `tensor/DDL_lfc|DDL_z.npy` [4732]; `embed/gene_vectors.npy` [4732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4732 or target_col == 4732). Every well: [[FRMD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
