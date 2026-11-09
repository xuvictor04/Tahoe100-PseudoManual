---
symbol: "DUXAP10"
type: "gene"
col: 14401
ensembl_id: "ENSG00000244306"
name: "double homeobox A pseudogene 10"
location: "14q11.2"
module: 40
arm: "+"
pooled_cpm: 42.46
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 12
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# DUXAP10

*double homeobox A pseudogene 10* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.49× (z +7.9, q 1e-12, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -17.3, q 0e+00, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUXAP9]] (+0.81, fdr 7e-06), [[ELP2]] (+0.74, fdr 7e-06), [[TFB2M]] (+0.65, fdr 7e-06); moves opposite to [[SP2]] (-0.60, fdr 1e-05), [[FAM111A]] (-0.59, fdr 3e-05), [[TUG1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 12 go from it, the strongest it → [[ZNF169]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +7.9 | 1e-12 | 28/41 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +7.8 | 2e-12 | 32/41 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +5.0 | 1e-04 | 18/41 (A498, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 1e-04 | 22/41 (A-172, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 5e-04 | 18/41 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 15/41 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 11/41 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.1 | 0.14 | 7/28 (SW480, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.14 | 15/41 (BT-474, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.0 | 0.14 | 13/37 (SNU-423, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -17.3 | 0e+00 | 31/41 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.445×** | -16.0 | 0e+00 | 30/41 (SW48, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -12.7 | 2e-34 | 34/41 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -11.9 | 9e-31 | 28/41 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -11.2 | 6e-27 | 24/34 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.663×** | -7.5 | 7e-12 | 23/38 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -7.1 | 1e-10 | 6/41 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.704×** | -6.9 | 3e-10 | 22/41 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.749×** | -5.7 | 8e-07 | 20/41 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -5.3 | 6e-06 | 20/41 (HS-578T, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.787×** | -4.7 | 1e-04 | 18/39 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.793×** | -4.6 | 2e-04 | 14/41 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.790×** | -4.3 | 8e-04 | 17/40 (A549, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -4.0 | 0.003 | 16/41 (Hs 766T, SW 1271, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.820×** | -3.9 | 0.004 | 13/41 (HepG2/C3A, NCI-H460, …) | top dose only | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | 0.838× | -3.5 | 0.019 | 10/41 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.839× | -3.3 | 0.031 | 14/41 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.846× | -3.3 | 0.032 | 9/41 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.848× | -3.0 | 0.063 | 2/41 (SHP-77, A498) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.077 | 10/41 (SW 1088, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 173 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -20.3) |
| [[PANC-1 (line)]] | alt | 94.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -25.2) |
| [[A549 (line)]] | wt | 93.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.7) |
| [[RKO (line)]] | wt | 94.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -22.1) |
| [[A498 (line)]] | wt | 45.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.4) |
| [[HCT15 (line)]] | alt | 63.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0677× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.404× (z -8.8) |
| [[HS-578T (line)]] | alt | 85.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.340× (z -11.1) |
| [[LS 180 (line)]] | wt | 54.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.307× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 37.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.9) |
| [[SNU-1 (line)]] | wt | 98.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.3) |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 47.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.257× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 59.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 84.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 41.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.1) |
| [[SW48 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0934× (z -21.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 59.5 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0707× (z -10.1) |
| [[H4 (line)]] | wt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -16.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 83.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 94.9 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 5 µM 0.0429× (z -11.0) |
| [[A-172 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP9]] | +0.81 | +0.85 / +0.78 | both halves | 7e-06 | same gene group |
| [[ELP2]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TFB2M]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[C2orf27A]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SNU13]] | +0.63 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TOMM20]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[WDR59]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SHQ1]] | +0.62 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CCNB1IP1]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP2]] | -0.60 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.59 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[TUG1]] | -0.58 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SCAF1]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.57 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[LRRC57]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PHF19]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[GEN1]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[MIS12]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SKIL]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[HMGN2]] | -0.57 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PNRC2]] | -0.56 | -0.59 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DUXAP10's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SYCP2L]] | B | SYCP2L activity raises DUXAP10's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.82× lower at baseline in the lines without SYCP2L | 0.074 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[DUXAP9]] | C | DUXAP9 activity raises DUXAP10's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 6.24× lower at baseline in the lines without DUXAP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent; co-absent with the target |
| [[DUXAP8]] | C | DUXAP8 activity raises DUXAP10's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 6.13× lower at baseline in the lines without DUXAP8 | 0.002 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF169]] | B | DUXAP10 activity raises ZNF169's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without DUXAP10 | 0.018 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[EBPL]] | B | DUXAP10 activity raises EBPL's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without DUXAP10 | 0.024 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[UBE3D]] | B | DUXAP10 activity raises UBE3D's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without DUXAP10 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[CRYZL1]] | B | DUXAP10 activity raises CRYZL1's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without DUXAP10 | 0.035 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[SYCP2L]] | B | DUXAP10 activity raises SYCP2L's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without DUXAP10 | 0.051 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[TMEM107]] | B | DUXAP10 activity raises TMEM107's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without DUXAP10 | 0.054 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[ERI3]] | B | DUXAP10 activity raises ERI3's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without DUXAP10 | 0.055 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[FBXL4]] | B | DUXAP10 activity raises FBXL4's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without DUXAP10 | 0.073 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[WDR59]] | B | DUXAP10 activity raises WDR59's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without DUXAP10 | 0.084 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[MIS12]] | B | DUXAP10 activity raises MIS12's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.16× lower at baseline in the lines without DUXAP10 | 0.095 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[DUXAP8]] | C | DUXAP10 activity raises DUXAP8's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 4.91× lower at baseline in the lines without DUXAP10 | 0.001 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9; co-absent with the target |
| [[DUXAP9]] | C | DUXAP10 activity raises DUXAP9's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 5.84× lower at baseline in the lines without DUXAP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9; co-absent with the target |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (1.3, -19.3); signed map (-53.5, -1.5). **Vector** length 108, 27.1% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -5.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -4.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.1 | -3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | double homeobox A pseudogene 10 |
| Locus type | pseudogene |
| Location | 14q11.2 — chr14:19,295,306-19,295,921 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [503639](https://www.ncbi.nlm.nih.gov/gene/503639):

> Homeobox genes encode DNA-binding proteins, many of which are thought to be involved in early embryonic development. Homeobox genes encode a DNA-binding domain of 60 to 63 amino acids referred to as the homeodomain. This pseudogene is a member of the DUXA homeobox gene family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:32189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32189) · Entrez [503639](https://www.ncbi.nlm.nih.gov/gene/503639) · Ensembl [ENSG00000244306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244306)

## Data

Gene col 14401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14401); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14401]; `tensor/DDL_lfc|DDL_z.npy` [14401]; `embed/gene_vectors.npy` [14401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14401 or target_col == 14401). Every well: [[DUXAP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUXAP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
