---
symbol: "KAT7"
type: "gene"
col: 5872
ensembl_id: "ENSG00000136504"
name: "lysine acetyltransferase 7"
location: "17q21.33"
module: 25
arm: "+"
pooled_cpm: 48.04
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# KAT7

*lysine acetyltransferase 7* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.00× (z +8.5, q 7e-15, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.620× (z -10.1, q 5e-21, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLD]] (+0.59, fdr 1e-05), [[SNRNP200]] (+0.59, fdr 7e-06), [[NONO]] (+0.59, fdr 1e-05); moves opposite to [[CCNYL1]] (-0.58, fdr 1e-05), [[PPP1R14B-AS1]] (-0.57, fdr 1e-05), [[PPP1R14B]] (-0.56, fdr 4e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +8.5 | 7e-15 | 45/49 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +8.2 | 8e-14 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +7.2 | 1e-10 | 35/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +6.3 | 5e-08 | 37/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.6 | 3e-06 | 33/47 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 1e-04 | 33/48 (C32, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 2e-04 | 33/47 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.78×** | +4.5 | 5e-04 | 33/48 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.3 | 9e-04 | 29/48 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 9e-04 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +3.4 | 0.033 | 20/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.047 | 16/48 (NCI-H1792, SK-MEL-2, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.1 | 0.094 | 20/44 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.098 | 13/48 (SNU-423, RKO, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.098 | 15/48 (BT-474, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -10.1 | 5e-21 | 45/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -8.0 | 5e-13 | 38/48 (SNU-423, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -7.8 | 1e-12 | 40/49 (LS 180, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.649×** | -6.4 | 2e-08 | 40/48 (J82, H4, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.743×** | -6.2 | 5e-08 | 37/48 (A498, SW 900, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.673×** | -5.9 | 3e-07 | 35/48 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.770×** | -5.5 | 3e-06 | 30/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -4.8 | 1e-04 | 31/48 (CHP-212, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.734×** | -4.6 | 3e-04 | 28/46 (SNU-1, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.710×** | -4.5 | 4e-04 | 24/44 (NCI-H460, KATO III, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.772×** | -3.9 | 0.006 | 28/48 (hTERT-HPNE, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.006 | 24/48 (COLO 205, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.771×** | -3.7 | 0.009 | 22/42 (A-172, CHP-212, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.783×** | -3.6 | 0.011 | 23/48 (NCI-H2347, SW 1088, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.654×** | -3.5 | 0.019 | 23/48 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.672×** | -3.1 | 0.061 | 18/46 (HCT15, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.686×** | -3.1 | 0.061 | 21/48 (LOX-IMVI, AN3 CA, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.4 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.47× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.2) |
| [[HOP62 (line)]] | alt | 51.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.3) |
| [[LS 180 (line)]] | wt | 36.1 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.6) |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.3) |
| [[A-172 (line)]] | wt | 35.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.6) |
| [[SW480 (line)]] | alt | 52.2 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.30× (z +9.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.5) |
| [[A498 (line)]] | wt | 50.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -12.0) |
| [[A549 (line)]] | wt | 38.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 96.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0938× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[COLO 205 (line)]] | alt | 58.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 33.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 64.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -12.0) |
| [[PANC-1 (line)]] | alt | 51.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.116× (z -8.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 46.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -10.0) |
| [[SW 900 (line)]] | alt | 51.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.7) |
| [[A-427 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.59 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NONO]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[UNG]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TGOLN2]] | +0.58 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[TRRAP]] | +0.58 | +0.66 / +0.57 | both halves | 1e-05 | pathway: Chromatin modifying enzymes; STRING 696 |
| [[SP1]] | +0.57 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[RPP30]] | +0.56 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[NUMA1]] | +0.56 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[FAM98B]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[VPS11]] | +0.55 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[BAP1]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.58 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[PPP1R14B-AS1]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R14B]] | -0.56 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[S100A2]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[PHLDA2]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SLC9A1]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ACAP1]] | -0.53 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[RABGEF1]] | -0.52 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[PDGFA]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[BMAL2-AS1]] | -0.51 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[STK10]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[MSANTD3]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KAT7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C11orf91]] | B | C11orf91 activity lowers KAT7's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.34× higher at baseline in the lines without C11orf91 | 0.042 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.7, -23.1); signed map (-20.1, -37.2). **Vector** length 93.5, 24.7% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.9 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +4.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -0.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:49,788,624-49,835,026 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HBOA, HBO1; previously MYST2 |
| Gene groups (HGNC) | Zinc fingers C2H2C-type; MYST type domain containing lysine acetyltransferases; Zinc fingers MYST C2HC-type |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O95251](https://www.uniprot.org/uniprotkb/O95251) (Histone acetyltransferase KAT7):

> Catalytic subunit of histone acetyltransferase HBO1 complexes, which specifically mediate acetylation of histone H3 at 'Lys-14' (H3K14ac), thereby regulating various processes, such as gene transcription, protein ubiquitination, immune regulation, stem cell pluripotent and self-renewal maintenance and embryonic development. Some complexes also catalyze acetylation of histone H4 at 'Lys-5', 'Lys-8' and 'Lys-12' (H4K5ac, H4K8ac and H4K12ac, respectively), regulating DNA replication initiation, …

**Summary**, from NCBI Gene [11143](https://www.ncbi.nlm.nih.gov/gene/11143):

> The protein encoded by this gene is part of the multimeric HBO1 complex, which possesses histone H4-specific acetyltransferase activity. This activity is required for functional replication origins and is involved in transcriptional activation of some genes. In both cases, the acetylation of histone H4 helps unfold chromatin so that the DNA can be accessed and replicated or transcribed. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:17016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17016) · Entrez [11143](https://www.ncbi.nlm.nih.gov/gene/11143) · UniProt [O95251](https://www.uniprot.org/uniprotkb/O95251) · Ensembl [ENSG00000136504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136504)

## Data

Gene col 5872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5872); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5872]; `tensor/DDL_lfc|DDL_z.npy` [5872]; `embed/gene_vectors.npy` [5872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5872 or target_col == 5872). Every well: [[KAT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
