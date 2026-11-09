---
symbol: "ACOX3"
type: "gene"
col: 1475
ensembl_id: "ENSG00000087008"
name: "acyl-CoA oxidase 3, pristanoyl"
location: "4p16.1"
module: 210
arm: "+"
pooled_cpm: 24.93
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# ACOX3

*acyl-CoA oxidase 3, pristanoyl* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.48× (z +6.8, q 6e-09, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 3.80×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.533× (z -10.9, q 5e-25, down in 41 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.731× (z -7.7, q 9e-13, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP214]] (+0.67, fdr 1e-05), [[PEX16]] (+0.67, fdr 7e-06), [[TRMT44]] (+0.65, fdr 1e-05, ⚠ same locus), [[KRBOX4]] (+0.64, fdr 1e-05); moves opposite to [[NEO1]] (-0.63, fdr 2e-05), [[STIM2]] (-0.58, fdr 1e-05), [[CDH2]] (-0.58, fdr 1e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 3.80×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +6.8 | 6e-09 | 27/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +6.6 | 9e-09 | 30/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +3.5 | 0.074 | 8/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.21× | +3.3 | 0.13 | 4/48 (A498, NCI-H1573, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.22× | +3.2 | 0.13 | 7/48 (Panc 03.27, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.533×** | -10.9 | 5e-25 | 41/47 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.522×** | -10.4 | 5e-23 | 27/38 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.545×** | -9.8 | 2e-20 | 30/48 (SNU-423, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.571×** | -9.7 | 4e-20 | 34/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.553×** | -9.6 | 1e-19 | 33/46 (RPMI-7951, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.619×** | -8.3 | 8e-15 | 27/42 (A498, H4, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.637×** | -7.8 | 4e-13 | 33/48 (H4, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.640×** | -7.8 | 6e-13 | 30/48 (LS 180, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -7.7 | 9e-13 | 32/48 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -7.6 | 1e-12 | 33/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.634×** | -7.4 | 1e-11 | 21/35 (A-172, H4, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.750×** | -5.0 | 3e-05 | 22/48 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.754×** | -4.9 | 4e-05 | 21/46 (CFPAC-1, A498, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.756×** | -4.9 | 5e-05 | 19/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.619×** | -4.4 | 5e-04 | 20/48 (J82, SNU-423, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -4.3 | 7e-04 | 17/46 (SW48, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.051 | 13/48 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.724×** | -2.9 | 0.091 | 13/47 (CHP-212, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.846× | -2.9 | 0.093 | 6/48 (SW1417, NCI-H661, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 59.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 31.8 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 32.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 30.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Silodosin (drug)]] 5 µM 0.289× (z -8.5) |
| [[CHP-212 (line)]] | wt | 44.5 | 0 | 3 (2 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0825× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 75.0 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -12.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LoVo (line)]] | wt | 22.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -17.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 19.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.268× (z -8.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 34.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0428× (z -19.4) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0627× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0685× (z -18.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.2) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LS 180 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.295× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -8.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -10.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[A-427 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP214]] | +0.67 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[PEX16]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 | pathway: Protein localization; STRING 440 |
| [[TRMT44]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[KRBOX4]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[TM9SF4]] | +0.62 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.61 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[SLC30A6]] | +0.60 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ZNF761]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[DDX49]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CUL7]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RNF185]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SAMD4B]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[HGS]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEO1]] | -0.63 | -0.48 / -0.63 | both halves | 2e-05 | pathway: Protein localization |
| [[STIM2]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CDH2]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.55 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TMSB4X]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[GALNT7]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.53 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[CMTM6]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ADGRA3]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SINHCAF]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[KLF12]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SEPTIN11]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.6, -5.9); signed map (-19.3, -2.0). **Vector** length 75.6, 14.8% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +0.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | -0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -4.6 | -9.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.3 | -9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA oxidase 3, pristanoyl |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:8,366,282-8,440,723 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Acyl-CoA oxidase family |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Beta-oxidation of pristanoyl-CoA; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O15254](https://www.uniprot.org/uniprotkb/O15254) (Peroxisomal acyl-coenzyme A oxidase 3):

> Involved in peroxisomal beta-oxidation of branched-chain fatty acids (BCFAs). Catalyzes the initial and rate-limiting dehydrogenation step that removes two hydrogen molecules and introduces a trans double bond between the alpha and beta carbons of the acyl CoA molecules while generating hydrogen peroxide as a by-product. Metabolizes multi-methyl-branched fatty acyl-CoA esters such as (2S)-pristanoyl-CoA, displaying redundancy with ACOX3. Can oxidize straight-chain mono- and dicarboxylyl fatty …

**Summary**, from NCBI Gene [8310](https://www.ncbi.nlm.nih.gov/gene/8310):

> Acyl-Coenzyme A oxidase 3 also know as pristanoyl -CoA oxidase (ACOX3)is involved in the desaturation of 2-methyl branched fatty acids in peroxisomes. Unlike the rat homolog, the human gene is expressed in very low amounts in liver such that its mRNA was undetectable by routine Northern-blot analysis or its product by immunoblotting or by enzyme activity measurements. However the human cDNA encoding a 700 amino acid protein with a peroxisomal targeting C-terminal tripeptide S-K-L was isolated …

**Accessions** — [HGNC:121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:121) · Entrez [8310](https://www.ncbi.nlm.nih.gov/gene/8310) · UniProt [O15254](https://www.uniprot.org/uniprotkb/O15254) · Ensembl [ENSG00000087008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087008)

## Data

Gene col 1475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1475); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1475]; `tensor/DDL_lfc|DDL_z.npy` [1475]; `embed/gene_vectors.npy` [1475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1475 or target_col == 1475). Every well: [[ACOX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
