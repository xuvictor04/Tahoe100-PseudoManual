---
symbol: "ARHGAP27"
type: "gene"
col: 8243
ensembl_id: "ENSG00000159314"
name: "Rho GTPase activating protein 27"
location: "17q21.31"
module: 31
arm: "+"
pooled_cpm: 28.33
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 55
direction_downstream: 5
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ARHGAP27

*Rho GTPase activating protein 27* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.27× (z +3.9, q 0.044, up in 17 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 6.14×, A-172 4.02×, MIA PaCa-2 2.31×, LOX-IMVI 3.45×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H460 7.05×, MIA PaCa-2 3.97×, A-172 5.06×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 3.09×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.627× (z -7.6, q 1e-11, down in 24 of 42 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.680× (z -6.3, q 5e-08, down in 26 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.407×, COLO 205 0.326×, AsPC-1 0.438×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.346×, NCI-H1573 0.309×, COLO 205 0.293×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (Hs 766T 0.113×, A549 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clofarabine (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0654×); [[Procainamide (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.0919×); [[Silodosin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.103×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP27P1-BPTFP1-KPNA2P3]] (+0.71, fdr 7e-06), [[PLEKHM1]] (+0.70, fdr 7e-06, ⚠ same locus), [[UNC13D]] (+0.69, fdr 7e-06), [[KPNA2P3]] (+0.69, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 5 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8243.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 6.14×, A-172 4.02×, MIA PaCa-2 2.31×, LOX-IMVI 3.45×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H460 7.05×, MIA PaCa-2 3.97×, A-172 5.06×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 3.09×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.044 | 17/42 (A-172, SNU-423, …) | two highest doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.050 | 10/43 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.11 | 17/42 (NCI-H460, A-172, …) | top dose only | composition shift |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.24× | +3.3 | 0.13 | 10/42 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.23× | +3.2 | 0.15 | 11/43 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 1.43× | +3.1 | 0.20 | 13/40 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8243.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.407×, COLO 205 0.326×, AsPC-1 0.438×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.346×, NCI-H1573 0.309×, COLO 205 0.293×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (Hs 766T 0.113×, A549 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clofarabine (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0654×); [[Procainamide (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.0919×); [[Silodosin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.627×** | -7.6 | 1e-11 | 24/42 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.665×** | -6.7 | 7e-09 | 23/41 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -6.3 | 5e-08 | 26/42 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -5.0 | 7e-05 | 19/43 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.752×** | -4.7 | 3e-04 | 21/42 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.765×** | -4.4 | 0.001 | 21/43 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.639×** | -3.8 | 0.009 | 11/40 (CFPAC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.785×** | -3.8 | 0.009 | 16/38 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.815×** | -3.4 | 0.048 | 18/35 (HT-29, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.097 | 13/43 (Hs 766T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.875× | -3.1 | 0.097 | 16/43 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.821× | -3.1 | 0.11 | 12/41 (A-172, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.825× | -3.0 | 0.11 | 14/42 (Hs 766T, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[AsPC-1 (line)]] | alt | 58.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 81.3 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.97× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.313× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 51.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[NCI-H460 (line)]] | wt | 8.58 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 2 | — | [[Clofarabine (drug)]] 0.05 µM 0.0654× (z -10.1) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.103× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 10.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0945× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.09× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[PLEKHM1]] | +0.70 | +0.61 / +0.78 | both halves | 7e-06 | same gene group; STRING 604; ⚠ same locus (1.5 kb, same strand: neighbours can correlate without regulation) |
| [[UNC13D]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[KPNA2P3]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[LSMEM2]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TMC6]] | +0.67 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PTK6]] | +0.66 | +0.59 / +0.73 | both halves | 7e-06 | same gene group |
| [[EPS8L1]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 | same gene group |
| [[PADI1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[GJB3]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.62 | +0.53 / +0.66 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[PLEKHM1P1]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RDH13]] | +0.62 | +0.61 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 55, C 0. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises ARHGAP27's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.96× lower at baseline in the lines without B3GNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[MROH3P]] | B | MROH3P activity raises ARHGAP27's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.79× lower at baseline in the lines without MROH3P | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[C1orf116]] | B | C1orf116 activity raises ARHGAP27's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without C1orf116 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ARHGAP27's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.12× lower at baseline in the lines without TMPRSS4 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[GJB3]] | B | GJB3 activity raises ARHGAP27's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.26× lower at baseline in the lines without GJB3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[LPAR5]] | B | LPAR5 activity raises ARHGAP27's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without LPAR5 | 5e-04 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[FAM83B]] | B | FAM83B activity raises ARHGAP27's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without FAM83B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[MISP]] | B | MISP activity raises ARHGAP27's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without MISP | 6e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[KLK10]] | B | KLK10 activity raises ARHGAP27's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.24× lower at baseline in the lines without KLK10 | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[ITGB4]] | B | ITGB4 activity raises ARHGAP27's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.90× lower at baseline in the lines without ITGB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[FA2H]] | B | FA2H activity raises ARHGAP27's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without FA2H | 0.001 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[MYO5B]] | B | MYO5B activity raises ARHGAP27's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without MYO5B | 0.002 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | ARHGAP27 activity raises EPHA2's level | lines that do not express ARHGAP27 (5) vs lines expressing it (45) | 4.44× lower at baseline in the lines without ARHGAP27 | 0.060 | ⚠ within organs, on part of the lines; also absent: TRIB3, LMNTD2, PLEKHN1; maybe low, not absent; its own permutation p |
| [[ADAP1]] | B | ARHGAP27 activity raises ADAP1's level | lines that do not express ARHGAP27 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without ARHGAP27 | 0.070 | ⚠ within organs, on part of the lines; also absent: TRIB3, LMNTD2, PLEKHN1; maybe low, not absent |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | ARHGAP27 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express ARHGAP27 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without ARHGAP27 | 0.077 | ⚠ within organs, on part of the lines; also absent: TRIB3, LMNTD2, PLEKHN1; maybe low, not absent |
| [[MKNK1]] | B | ARHGAP27 activity raises MKNK1's level | lines that do not express ARHGAP27 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without ARHGAP27 | 0.086 | ⚠ within organs, on part of the lines; also absent: TRIB3, LMNTD2, PLEKHN1; maybe low, not absent |
| [[PKD2]] | B | ARHGAP27 activity lowers PKD2's level | lines that do not express ARHGAP27 (5) vs lines expressing it (45) | 1.40× higher at baseline in the lines without ARHGAP27 | 0.089 | ⚠ within organs, on part of the lines; also absent: TRIB3, LMNTD2, PLEKHN1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.6, 53.6); signed map (1.0, 36.3). **Vector** length 104, 24.5% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -6.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.2 | -4.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.2 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,393,902-45,434,421 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAMGAP1, FLJ43547, SH3P20; previously SH3D20 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 5 pathways, smallest: CDC42 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZUM4](https://www.uniprot.org/uniprotkb/Q6ZUM4) (Rho GTPase-activating protein 27):

> Rho GTPase-activating protein which may be involved in clathrin-mediated endocytosis. GTPase activators for the Rho-type GTPases act by converting them to an inactive GDP-bound state. Has activity toward CDC42 and RAC1 (By similarity).

**Summary**, from NCBI Gene [201176](https://www.ncbi.nlm.nih.gov/gene/201176):

> This gene encodes a member of a large family of proteins that activate Rho-type guanosine triphosphate (GTP) metabolizing enzymes. The encoded protein may pay a role in clathrin-mediated endocytosis. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:31813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31813) · Entrez [201176](https://www.ncbi.nlm.nih.gov/gene/201176) · UniProt [Q6ZUM4](https://www.uniprot.org/uniprotkb/Q6ZUM4) · Ensembl [ENSG00000159314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159314)

## Data

Gene col 8243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8243); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8243]; `tensor/DDL_lfc|DDL_z.npy` [8243]; `embed/gene_vectors.npy` [8243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8243 or target_col == 8243). Every well: [[ARHGAP27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
