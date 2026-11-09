---
symbol: "PLOD3"
type: "gene"
col: 2755
ensembl_id: "ENSG00000106397"
name: "procollagen-lysine,2-oxoglutarate 5-dioxygenase 3"
location: "7q22.1"
module: 72
arm: "+"
pooled_cpm: 45.03
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PLOD3

*procollagen-lysine,2-oxoglutarate 5-dioxygenase 3* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.75× (z +9.8, q 5e-20, up in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.65× (z +8.7, q 4e-16, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.876× (z -8.2, q 2e-13, down in 5 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.680× (z -6.7, q 5e-09, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBOAT7]] (+0.65, fdr 7e-06), [[SERPINH1]] (+0.58, fdr 4e-05), [[UFD1]] (+0.56, fdr 1e-05); moves opposite to [[PPP4R2]] (-0.59, fdr 1e-05), [[TIGD2]] (-0.56, fdr 1e-05), [[YEATS4]] (-0.51, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[P3H3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +9.8 | 5e-20 | 37/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.74×** | +9.7 | 9e-20 | 33/47 (C32, KATO III, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +8.7 | 4e-16 | 38/48 (LoVo, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +8.4 | 7e-15 | 26/41 (C32, RKO, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.58×** | +7.6 | 2e-12 | 30/37 (KATO III, LoVo, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +6.8 | 9e-10 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.1 | 7e-08 | 30/48 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.0 | 2e-07 | 28/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 5e-06 | 25/48 (SW1417, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.32×** | +4.8 | 8e-05 | 25/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.8 | 8e-05 | 21/44 (SW1417, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +4.7 | 1e-04 | 20/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.5 | 3e-04 | 27/48 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.2 | 0.001 | 15/35 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.28×** | +4.1 | 0.001 | 22/47 (SW480, COLO 205, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.004 | 17/48 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.064 | 21/49 (SW1417, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | 1.19× | +3.0 | 0.081 | 10/48 (HS-578T, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.876× | -8.2 | 2e-13 | 5/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -6.7 | 5e-09 | 32/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.766×** | -6.6 | 1e-08 | 32/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.726×** | -5.6 | 3e-06 | 30/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -5.6 | 3e-06 | 25/48 (RPMI-7951, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.746×** | -4.8 | 2e-04 | 27/49 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.773×** | -4.5 | 6e-04 | 29/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.782×** | -4.1 | 0.003 | 23/47 (NCI-H2030, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.848× | -4.0 | 0.004 | 18/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.655×** | -3.9 | 0.006 | 17/49 (SK-MEL-2, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.805×** | -3.8 | 0.007 | 20/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.798×** | -3.8 | 0.007 | 23/48 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.844× | -3.7 | 0.009 | 19/48 (SW480, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.020 | 22/48 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.028 | 13/49 (SW480, NCI-H1792, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.816×** | -3.3 | 0.038 | 13/48 (SW480, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.3 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.72× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.56× (z +10.5) | — |
| [[LoVo (line)]] | wt | 33.3 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.49× (z +13.7) | — |
| [[C32 (line)]] | wt | 242 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 58.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.87× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 42.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -10.4) |
| [[KATO III (line)]] | alt | 56.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 41.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.93× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 34.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 86.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.122× (z -8.9) |
| [[A-427 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SERPINH1]] | +0.58 | +0.41 / +0.69 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[UFD1]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[BSCL2]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[STK35]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ECM1]] | +0.54 | +0.60 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TNPO3]] | +0.52 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[HSPE1-MOB4]] | +0.51 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[PLD5P1]] | +0.51 | +0.22 / +0.53 | both halves | 6e-04 |  |
| [[ABHD15-AS1]] | +0.51 | +0.20 / +0.43 | both halves | 7e-04 |  |
| [[ANKRD42]] | +0.50 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[CAPN15]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 | pathway: Extracellular matrix organization |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R2]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.56 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[YEATS4]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SAYSD1]] | -0.49 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[EXOSC9]] | -0.49 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[SAV1]] | -0.49 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[NUDCD2]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[RTL6]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ZSCAN9]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CRADD]] | -0.48 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[EXOC6]] | -0.48 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ZNF182]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H3]] | B | P3H3 activity raises PLOD3's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without P3H3 | 0.016 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[COL6A1]] | B | COL6A1 activity raises PLOD3's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without COL6A1 | 0.088 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[P3H1]] | C | P3H1 activity raises PLOD3's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without P3H1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.460). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.8, -9.4); signed map (-54.7, -11.3). **Vector** length 82.1, 17.9% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.5 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +5.0 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | procollagen-lysine,2-oxoglutarate 5-dioxygenase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,205,977-101,218,420 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LH3 |
| Gene groups (HGNC) | Procollagen-lysine,2-oxoglutarate 5-dioxygenase family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Collagen biosynthesis and modifying enzymes; Collagen formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O60568](https://www.uniprot.org/uniprotkb/O60568) (Multifunctional procollagen lysine hydroxylase and glycosyltransferase LH3):

> Multifunctional enzyme that catalyzes a series of essential post-translational modifications on Lys residues in procollagen. Plays a redundant role in catalyzing the formation of hydroxylysine residues in -Xaa-Lys-Gly- sequences in collagens. Plays a redundant role in catalyzing the transfer of galactose onto hydroxylysine groups, giving rise to galactosyl 5-hydroxylysine. Has an essential role by catalyzing the subsequent transfer of glucose moieties, giving rise to …

**Summary**, from NCBI Gene [8985](https://www.ncbi.nlm.nih.gov/gene/8985):

> The protein encoded by this gene is a membrane-bound homodimeric enzyme that is localized to the cisternae of the rough endoplasmic reticulum. The enzyme (cofactors iron and ascorbate) catalyzes the hydroxylation of lysyl residues in collagen-like peptides. The resultant hydroxylysyl groups are attachment sites for carbohydrates in collagen and thus are critical for the stability of intermolecular crosslinks. Some patients with Ehlers-Danlos syndrome type VIB have deficiencies in lysyl …

**Accessions** — [HGNC:9083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9083) · Entrez [8985](https://www.ncbi.nlm.nih.gov/gene/8985) · UniProt [O60568](https://www.uniprot.org/uniprotkb/O60568) · Ensembl [ENSG00000106397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106397)

## Data

Gene col 2755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2755); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2755]; `tensor/DDL_lfc|DDL_z.npy` [2755]; `embed/gene_vectors.npy` [2755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2755 or target_col == 2755). Every well: [[PLOD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLOD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
