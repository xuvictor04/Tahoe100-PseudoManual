---
symbol: "SRI"
type: "gene"
col: 1101
ensembl_id: "ENSG00000075142"
name: "sorcin"
location: "7q21.12"
module: 17
arm: "+"
pooled_cpm: 47.29
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SRI

*sorcin* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.46× (z +6.2, q 4e-07, up in 28 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 5 µM: 1.18× (z +3.9, q 0.013, up in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Cobimetinib (drug)]] 0.5 µM in 1 line (LoVo 2.64×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (LoVo 2.61×); [[Trametinib (drug)]] 5 µM in 1 line (LoVo 2.27×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 0.05 µM in 1 line (LoVo 1.99×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.419× (z -19.7, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC19]] (+0.61, fdr 1e-05), [[ZYG11B]] (+0.57, fdr 3e-05), [[PYURF]] (+0.57, fdr 4e-05); moves opposite to [[SLC9A5]] (-0.63, fdr 1e-05), [[PIPOX]] (-0.53, fdr 3e-05), [[DNAH1]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1101.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Cobimetinib (drug)]] 0.5 µM in 1 line (LoVo 2.64×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (LoVo 2.61×); [[Trametinib (drug)]] 5 µM in 1 line (LoVo 2.27×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 0.05 µM in 1 line (LoVo 1.99×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.2 | 4e-07 | 28/47 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.0 | 0.013 | 19/36 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | 1.18× | +3.9 | 0.013 | 16/48 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.013 | 21/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +3.5 | 0.048 | 17/42 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.090 | 16/45 (SW480, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | 1.44× | +3.1 | 0.16 | 11/45 (HEC-1-A, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.419×** | -19.7 | 0e+00 | 46/47 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -13.8 | 1e-40 | 44/48 (SK-MEL-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -9.4 | 1e-18 | 33/47 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.591×** | -8.4 | 6e-15 | 37/47 (LoVo, Panc 03.27, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -8.0 | 1e-13 | 34/47 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.622×** | -7.3 | 3e-11 | 33/47 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -6.4 | 2e-08 | 32/47 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -5.8 | 4e-07 | 36/48 (HOP62, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.694×** | -5.6 | 1e-06 | 31/47 (C32, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.705×** | -5.6 | 1e-06 | 30/47 (LoVo, Panc 03.27, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -5.3 | 5e-06 | 25/46 (CHP-212, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.729×** | -5.0 | 2e-05 | 26/47 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -5.0 | 2e-05 | 27/47 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.796×** | -3.5 | 0.020 | 22/48 (C32, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.041 | 22/47 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.677×** | -3.2 | 0.041 | 21/47 (HT-29, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 93.7 | 7 (1 ⚠) | 5 (4 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 2.64× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.361× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 68.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -16.9) |
| [[NCI-H2347 (line)]] | alt | 91.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -25.4) |
| [[Panc 03.27 (line)]] | alt | 125 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -22.6) |
| [[C32 (line)]] | wt | 115 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 26.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.7) |
| [[RKO (line)]] | wt | 46.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -10.1) |
| [[A-427 (line)]] | wt | 37.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.1) |
| [[A498 (line)]] | wt | 72.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -15.8) |
| [[A549 (line)]] | wt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.5) |
| [[BT-474 (line)]] | alt | 36.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.5) |
| [[H4 (line)]] | wt | 46.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 39.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.7) |
| [[HOP62 (line)]] | alt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -12.6) |
| [[J82 (line)]] | alt | 31.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 38.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0692× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -17.6) |
| [[SW1417 (line)]] | alt | 56.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.2) |
| [[SW480 (line)]] | alt | 33.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 74.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -16.7) |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0579× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.4) |
| [[LS 180 (line)]] | wt | 61.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 41.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.1) |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.2) |
| [[SNU-423 (line)]] | alt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.9) |
| [[A-172 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC19]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZYG11B]] | +0.57 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PYURF]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[COMMD2]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ESD]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ENPP4]] | +0.55 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[KRAS]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[MRPS31P4]] | +0.54 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[KIF3A]] | +0.52 | +0.50 / +0.31 | both halves | 2e-04 |  |
| [[DPY30]] | +0.52 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[RAB4A]] | +0.51 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[NT5C3A]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A5]] | -0.63 | -0.55 / -0.56 | both halves | 1e-05 | pathway: Metal ion SLC transporters |
| [[PIPOX]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[DNAH1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ABR]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[LINC03048]] | -0.52 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[INTS6]] | -0.51 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[PYY]] | -0.51 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GPR137]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[NPIPB11]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[LRP2BP]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[KIAA0753]] | -0.50 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[NLGN3]] | -0.50 | -0.53 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SRI's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENPP5]] | B | ENPP5 activity raises SRI's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.35× lower at baseline in the lines without ENPP5 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[ALOX5]] | B | ALOX5 activity raises SRI's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.49× lower at baseline in the lines without ALOX5 | 0.064 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.4, -3.8); signed map (-22.2, -13.5). **Vector** length 87.9, 20.9% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.4 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.2 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -13.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.6 | -5.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -2.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sorcin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:88,205,115-88,226,993 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, INTERFERON_GAMMA_RESPONSE |
| Reactome | 14 pathways, smallest: Sodium/Calcium exchangers; Reduction of cytosolic Ca++ levels; Platelet calcium homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P30626](https://www.uniprot.org/uniprotkb/P30626) (Sorcin):

> Calcium-binding protein that modulates excitation-contraction coupling in the heart. Contributes to calcium homeostasis in the heart sarcoplasmic reticulum. Modulates the activity of RYR2 calcium channels.

**Summary**, from NCBI Gene [6717](https://www.ncbi.nlm.nih.gov/gene/6717):

> This gene encodes a calcium-binding protein with multiple E-F hand domains that relocates from the cytoplasm to the sarcoplasmic reticulum in response to elevated calcium levels. In addition to regulating intracellular calcium homeostasis it also modulates excitation-contraction coupling in the heart. Alternative splicing results in multiple transcript variants encoding distinct proteins. Multiple pseudogenes exist for this gene. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:11292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11292) · Entrez [6717](https://www.ncbi.nlm.nih.gov/gene/6717) · UniProt [P30626](https://www.uniprot.org/uniprotkb/P30626) · Ensembl [ENSG00000075142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075142)

## Data

Gene col 1101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1101); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1101]; `tensor/DDL_lfc|DDL_z.npy` [1101]; `embed/gene_vectors.npy` [1101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1101 or target_col == 1101). Every well: [[SRI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
