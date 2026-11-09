---
symbol: "CSGALNACT2"
type: "gene"
col: 9858
ensembl_id: "ENSG00000169826"
name: "chondroitin sulfate N-acetylgalactosaminyltransferase 2"
location: "10q11.21"
module: 227
arm: "+"
pooled_cpm: 84.18
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 23
n_dd_up_clean: 23
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# CSGALNACT2

*chondroitin sulfate N-acetylgalactosaminyltransferase 2* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +11.5, q 4e-28, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.905× (z -6.8, q 7e-09, down in 5 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.759× (z -6.3, q 8e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFL1]] (+0.66, fdr 1e-05), [[STX1A]] (+0.65, fdr 1e-05), [[STC1]] (+0.65, fdr 1e-05); moves opposite to [[GTF2I]] (-0.62, fdr 1e-05), [[HFE]] (-0.60, fdr 3e-05), [[ARID1A]] (-0.58, fdr 3e-05).
> It is in [[Module 227]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +11.5 | 4e-28 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +11.2 | 1e-26 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +10.9 | 2e-25 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +9.5 | 2e-19 | 36/48 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +8.4 | 8e-15 | 31/48 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.4 | 1e-11 | 31/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +6.5 | 5e-09 | 28/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 2e-07 | 30/49 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.0 | 2e-07 | 29/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.7 | 8e-07 | 32/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 9e-06 | 29/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +4.5 | 3e-04 | 22/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +4.5 | 3e-04 | 25/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.2 | 9e-04 | 22/47 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +4.2 | 9e-04 | 23/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.2 | 9e-04 | 23/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 9e-04 | 23/48 (NCI-H1573, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.003 | 22/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -6.8 | 7e-09 | 5/50 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.759×** | -6.3 | 8e-08 | 32/48 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.724×** | -6.1 | 2e-07 | 32/49 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.772×** | -5.5 | 6e-06 | 30/50 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.747×** | -5.4 | 7e-06 | 30/47 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.607×** | -5.0 | 4e-05 | 27/48 (SW 900, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.612×** | -5.0 | 6e-05 | 29/47 (SW 900, SW 1088, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.768×** | -4.9 | 7e-05 | 30/48 (NCI-H1573, SW 1088, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.779×** | -4.8 | 9e-05 | 28/47 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.822×** | -4.8 | 1e-04 | 21/48 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.793×** | -4.5 | 4e-04 | 27/49 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.848× | -4.4 | 6e-04 | 20/49 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.789×** | -4.3 | 7e-04 | 22/48 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.804×** | -4.2 | 0.001 | 21/48 (CFPAC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.860× | -4.1 | 0.002 | 20/48 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.826×** | -3.7 | 0.008 | 23/48 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 245 | 1 | 13 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.245× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 80.1 | 7 (4 ⚠) | 6 | [[Digitoxin (drug)]] 0.5 µM 4.64× (z +11.5) | [[Trametinib (drug)]] 5 µM 0.236× (z -11.9) |
| [[PANC-1 (line)]] | alt | 109 | 7 (3 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.18× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.7) | — |
| [[SW480 (line)]] | alt | 76.6 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 27.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.71× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 87.3 | 3 | 1 | [[Auranofin (drug)]] 5 µM 3.07× (z +11.8) | [[Binimetinib (drug)]] 0.5 µM 0.509× (z -8.6) |
| [[HT-29 (line)]] | alt | 27.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.8) | — |
| [[KATO III (line)]] | alt | 25.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 50.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.413× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 74.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 45.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +9.8) | — |
| [[LoVo (line)]] | wt | 25.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.27× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 55.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.13× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 65.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 218 | 0 | 2 | — | [[Trametinib (drug)]] 0.5 µM 0.491× (z -9.0) |
| [[A549 (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.314× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 56.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.1) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 75.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 114 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0867× (z -9.5) |
| [[SW48 (line)]] | wt | 42.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +8.6) | — |
| [[A-172 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 135 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 100.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 159 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFL1]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[STX1A]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[STC1]] | +0.65 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[RAC2]] | +0.64 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[HMGA1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SPIRE1]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ABTB1]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2I]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[HFE]] | -0.60 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ARID1A]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ZFX]] | -0.58 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[RPRD1B]] | -0.55 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[ZNF827]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MOV10]] | -0.54 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[MFSD14A]] | -0.54 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[FUBP1]] | -0.53 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[MEIS2]] | -0.52 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RAF1]] | -0.52 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[CNOT1]] | -0.52 | -0.40 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises CSGALNACT2's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.61× lower at baseline in the lines without BCL2A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[MAP2K1]] | B | MAP2K1 activity raises CSGALNACT2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 4.5% of all compounds | 0.014 | ⚠ off-target possible; 4 compounds |
| [[RAB3B]] | B | RAB3B activity raises CSGALNACT2's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without RAB3B | 0.064 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 2.2); signed map (1.6, 48.4). **Vector** length 118, 35.7% of its response variance represented; |z| ≥ 3 in 1,496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +10.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.2 | +3.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -5.7 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.6 | -5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.6 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.5 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.2 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin sulfate N-acetylgalactosaminyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:43,138,445-43,185,302 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GALNACT2, MGC40204, PRO0082, GALNACT-2 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6G5](https://www.uniprot.org/uniprotkb/Q8N6G5) (Chondroitin sulfate N-acetylgalactosaminyltransferase 2):

> Transfers 1,4-N-acetylgalactosamine (GalNAc) from UDP-GalNAc to the non-reducing end of glucuronic acid (GlcUA). Required for addition of the first GalNAc to the core tetrasaccharide linker and for elongation of chondroitin chains.

**Summary**, from NCBI Gene [55454](https://www.ncbi.nlm.nih.gov/gene/55454):

> This gene encodes a member of the chondroitin N-acetylgalactosaminyltransferase family. The encoded protein is involved in elongation during chondroitin sulfate synthesis. Alternative splicing of this gene results in multiple transcript variants. Two related pseudogenes have been identified on chromosome X. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:24292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24292) · Entrez [55454](https://www.ncbi.nlm.nih.gov/gene/55454) · UniProt [Q8N6G5](https://www.uniprot.org/uniprotkb/Q8N6G5) · Ensembl [ENSG00000169826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169826)

## Data

Gene col 9858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9858); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9858]; `tensor/DDL_lfc|DDL_z.npy` [9858]; `embed/gene_vectors.npy` [9858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9858 or target_col == 9858). Every well: [[CSGALNACT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSGALNACT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
