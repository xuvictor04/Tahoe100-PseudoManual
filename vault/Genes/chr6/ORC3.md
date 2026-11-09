---
symbol: "ORC3"
type: "gene"
col: 5685
ensembl_id: "ENSG00000135336"
name: "origin recognition complex subunit 3"
location: "6q15"
module: 40
arm: "+"
pooled_cpm: 52.9
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ORC3

*origin recognition complex subunit 3* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.64× (z +9.9, q 3e-20, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.388× (z -20.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A6]] (+0.69, fdr 7e-06), [[NUP43]] (+0.67, fdr 7e-06), [[TPRKB]] (+0.64, fdr 7e-06); moves opposite to [[WAC-AS1]] (-0.56, fdr 1e-04), [[RAP2C-AS1]] (-0.55, fdr 4e-05), [[AJUBA-DT]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +9.9 | 3e-20 | 40/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +9.8 | 4e-20 | 38/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.35×** | +6.4 | 2e-08 | 31/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.8 | 1e-06 | 23/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +5.3 | 2e-05 | 24/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.20×** | +3.9 | 0.008 | 20/48 (NCI-H460, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -20.1 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.564×** | -17.2 | 0e+00 | 40/48 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -14.1 | 1e-42 | 46/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -12.9 | 4e-36 | 37/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -12.9 | 5e-36 | 45/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.553×** | -12.6 | 2e-34 | 38/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.588×** | -11.3 | 2e-27 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -9.2 | 2e-18 | 33/47 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -9.1 | 7e-18 | 40/49 (A-427, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.644×** | -9.0 | 2e-17 | 37/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.662×** | -8.8 | 1e-16 | 36/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -7.8 | 3e-13 | 30/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.772×** | -7.7 | 4e-13 | 33/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.704×** | -7.4 | 4e-12 | 31/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.810×** | -6.3 | 9e-09 | 27/48 (A-427, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -6.2 | 2e-08 | 26/48 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.667×** | -4.5 | 2e-04 | 22/48 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.696×** | -4.0 | 0.002 | 20/48 (HEC-1-A, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.837× | -3.8 | 0.004 | 16/47 (CFPAC-1, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 71.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 35.6 | 2 | 6 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.42× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -13.7) |
| [[SW480 (line)]] | alt | 66.5 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -26.2) |
| [[PANC-1 (line)]] | alt | 89.8 | 1 | 5 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.29× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -18.8) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -18.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -11.1) |
| [[H4 (line)]] | wt | 52.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.149× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 60.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.1) |
| [[KATO III (line)]] | alt | 71.7 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 34.3 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.14× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.271× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 39.6 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -13.5) |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.240× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 43.7 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.59× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.279× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -10.0) |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.263× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.333× (z -9.2) |
| [[A-427 (line)]] | wt | 61.5 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0966× (z -12.5) |
| [[A498 (line)]] | wt | 43.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -13.9) |
| [[Hs 766T (line)]] | wt | 57.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -11.5) |
| [[LS 180 (line)]] | wt | 36.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 70.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.256× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 38.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.54× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 41.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.407× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 42.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.365× (z -9.3) |
| [[SW 900 (line)]] | alt | 47.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -10.9) |
| [[A-172 (line)]] | wt | 48.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -8.5) |
| [[A549 (line)]] | wt | 38.4 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 3.08× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -8.7) |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0717× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.326× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 78.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -8.6) |
| [[HS-578T (line)]] | alt | 63.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -8.7) |
| [[LoVo (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 66.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 62.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -11.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 39.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.3) |
| [[SW48 (line)]] | wt | 40.1 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0485× (z -16.0) |
| [[AN3 CA (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A6]] | +0.69 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[NUP43]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[TPRKB]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PSMD13]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 | pathway: Assembly of the pre-replicative complex |
| [[RARS2]] | +0.63 | +0.69 / +0.54 | both halves | 1e-05 | STRING 464; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ZCCHC17]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.61 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[ACTR6]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[IQCB1]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[ZW10]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 | pathway: Cell Cycle Checkpoints |
| [[ERI3]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CALCOCO2]] | +0.59 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[INTS10]] | +0.58 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAC-AS1]] | -0.56 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[RAP2C-AS1]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[AJUBA-DT]] | -0.55 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[CYP1B1-AS1]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ERF]] | -0.54 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[TSC22D1]] | -0.54 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[CPEB2]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[LINC01569]] | -0.52 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[TAFA2]] | -0.52 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[MIR1915HG]] | -0.52 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[HERPUD2-AS1]] | -0.52 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[KLF10]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ORC3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers ORC3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MCC]] | B | MCC activity lowers ORC3's level | lines that do not express MCC (14) vs lines expressing it (36) | 1.18× higher at baseline in the lines without MCC | 0.067 | ⚠ within organs, on part of the lines; also absent: CAMK4, EGFEM1P, DYNC1I1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.447). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-27.6, -47.9); signed map (-37.0, -31.4). **Vector** length 118, 34.8% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +10.4 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.8 | +9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.6 | +9.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.5 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Tomivosertib (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.9 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -6.9 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.8 | -17.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | origin recognition complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:87,590,067-87,667,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IMAGE50150, LATHEO; previously ORC3L |
| Gene groups (HGNC) | Origin recognition complex |
| Reactome | 19 pathways, smallest: CDC6 association with the ORC:origin complex; E2F-enabled inhibition of pre-replication complex formation; E2F mediated regulation of DNA replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBD5](https://www.uniprot.org/uniprotkb/Q9UBD5) (Origin recognition complex subunit 3):

> Component of the origin recognition complex (ORC) that binds origins of replication. DNA-binding is ATP-dependent. The specific DNA sequences that define origins of replication have not been identified yet. ORC is required to assemble the pre-replication complex necessary to initiate DNA replication. Binds histone H3 and H4 trimethylation marks H3K9me3, H3K27me3 and H4K20me3.

**Summary**, from NCBI Gene [23595](https://www.ncbi.nlm.nih.gov/gene/23595):

> The origin recognition complex (ORC) is a highly conserved six subunits protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of the ORC complex. Studies of a similar gene in Drosophila suggested a possible role of this protein …

**Accessions** — [HGNC:8489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8489) · Entrez [23595](https://www.ncbi.nlm.nih.gov/gene/23595) · UniProt [Q9UBD5](https://www.uniprot.org/uniprotkb/Q9UBD5) · Ensembl [ENSG00000135336](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135336)

## Data

Gene col 5685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5685); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5685]; `tensor/DDL_lfc|DDL_z.npy` [5685]; `embed/gene_vectors.npy` [5685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5685 or target_col == 5685). Every well: [[ORC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
