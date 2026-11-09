---
symbol: "TESMIN"
type: "gene"
col: 5366
ensembl_id: "ENSG00000132749"
name: "testis expressed metallothionein like protein"
location: "11q13.3"
module: 23
arm: "+"
pooled_cpm: 10.68
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 10
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TESMIN

*testis expressed metallothionein like protein* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.63× (z +6.1, q 6e-07, up in 8 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.37× (z +4.1, q 0.005, up in 15 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.66×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.308× (z -15.2, q 0e+00, down in 32 of 36 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLX6-AS1]] (+0.52, fdr 3e-05), [[RDM1P5]] (+0.52, fdr 1e-04), [[PRSS16]] (+0.51, fdr 3e-05); moves opposite to [[LTBP1]] (-0.48, fdr 3e-05), [[PLXNA2]] (-0.46, fdr 4e-05), [[SLC2A13]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RDM1P5]] → it (grade B ⚠); 10 go from it, the strongest it → [[SERPINE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5366.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.66×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.1 | 6e-07 | 8/13 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +5.1 | 9e-05 | 15/35 (Panc 03.27, NCI-H1573, …) | top dose only | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.3 | 0.004 | 10/26 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.1 | 0.005 | 10/30 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.005 | 15/36 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.9 | 0.009 | 3/37 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.079 | 8/28 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.2 | 0.10 | 6/34 (HT-29, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.308×** | -15.2 | 0e+00 | 32/36 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.346×** | -13.7 | 4e-40 | 25/33 (MIA PaCa-2, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.483×** | -13.2 | 9e-38 | 30/33 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.397×** | -11.9 | 2e-30 | 32/36 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -11.5 | 2e-28 | 26/33 (MIA PaCa-2, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.424×** | -11.0 | 2e-26 | 31/36 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.436×** | -10.7 | 1e-24 | 29/34 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.462×** | -9.9 | 2e-21 | 29/36 (PANC-1, HEC-1-A, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.497×** | -8.6 | 3e-16 | 24/35 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.287×** | -8.4 | 2e-15 | 25/35 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.529×** | -8.2 | 1e-14 | 22/34 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.572×** | -7.2 | 3e-11 | 22/36 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -6.8 | 5e-10 | 22/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.366×** | -6.8 | 6e-10 | 23/34 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.598×** | -6.6 | 1e-09 | 21/36 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.395×** | -6.2 | 2e-08 | 24/35 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.633×** | -5.9 | 1e-07 | 17/36 (SW480, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.653×** | -5.5 | 1e-06 | 18/35 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.678×** | -4.7 | 8e-05 | 16/34 (BT-474, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.9 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -21.5) |
| [[SW480 (line)]] | alt | 16.4 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -21.6) |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0856× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.134× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 27.2 | 1 (1 ⚠) | 5 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +11.9) ⚠ position not correctable | [[Belinostat (drug)]] 0.5 µM 0.134× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0662× (z -22.8) |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.3) |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 2 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0536× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0981× (z -12.4) |
| [[A-427 (line)]] | wt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -9.9) |
| [[A549 (line)]] | wt | 8.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -13.2) |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -8.7) |
| [[C32 (line)]] | wt | 3.25 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0370× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0868× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~68% of this change |
| [[HOP62 (line)]] | alt | 7.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -8.9) |
| [[HT-29 (line)]] | alt | 8.85 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -10.1) |
| [[LoVo (line)]] | wt | 8.12 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.196× (z -9.6) |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0309× (z -10.2) |
| [[SW48 (line)]] | wt | 9.39 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0734× (z -9.1) |
| [[A-172 (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLX6-AS1]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[RDM1P5]] | +0.52 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[PRSS16]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[DMTN]] | +0.51 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[FN3K]] | +0.49 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CDH26]] | +0.49 | +0.50 / +0.29 | both halves | 3e-04 |  |
| [[ZNF385C]] | +0.49 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[ANKRD20A21P]] | +0.49 | +0.42 / +0.32 | both halves | 2e-04 |  |
| [[SPATA24]] | +0.48 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[TTC12]] | +0.48 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[GPRASP3]] | +0.48 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[NOXA1]] | +0.48 | +0.53 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBP1]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PLXNA2]] | -0.46 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[SLC2A13]] | -0.46 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[JAK2]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[BICDL1]] | -0.44 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[EHD4]] | -0.44 | -0.26 / -0.44 | both halves | 3e-04 |  |
| [[TBC1D2]] | -0.43 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[SETBP1]] | -0.43 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[PTPN1]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[TIMP1]] | -0.42 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[LANCL3]] | -0.41 | -0.28 / -0.28 | both halves | 3e-04 |  |
| [[LINC03047]] | -0.41 | -0.43 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[C11orf24]] | -0.39 | -0.28 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | RDM1P5 activity raises TESMIN's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without RDM1P5 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises TESMIN's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without ANKRD20A21P | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[PLXNA2]] | B | PLXNA2 activity lowers TESMIN's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.87× higher at baseline in the lines without PLXNA2 | 0.033 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[TOP2A]] | B | TOP2A activity raises TESMIN's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GCAWKR]] | B | GCAWKR activity raises TESMIN's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.68× lower at baseline in the lines without GCAWKR | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[PRSS16]] | B | PRSS16 activity raises TESMIN's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without PRSS16 | 0.060 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |
| [[EPHA10]] | B | EPHA10 activity raises TESMIN's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without EPHA10 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[AP1G2]] | B | AP1G2 activity raises TESMIN's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without AP1G2 | 0.072 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[LINC01748]] | B | LINC01748 activity raises TESMIN's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 1.58× lower at baseline in the lines without LINC01748 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |
| [[GUCY1B2]] | C | GUCY1B2 activity raises TESMIN's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without GUCY1B2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE1]] | B | TESMIN activity lowers SERPINE1's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 4.83× higher at baseline in the lines without TESMIN | 0.012 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[MIR3936HG]] | B | TESMIN activity raises MIR3936HG's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without TESMIN | 0.022 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[AP1G2]] | B | TESMIN activity raises AP1G2's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without TESMIN | 0.037 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[TIMP1]] | B | TESMIN activity lowers TIMP1's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.19× higher at baseline in the lines without TESMIN | 0.044 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[WDFY2]] | B | TESMIN activity lowers WDFY2's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 1.43× higher at baseline in the lines without TESMIN | 0.046 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[NOXA1]] | B | TESMIN activity raises NOXA1's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without TESMIN | 0.068 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[ZNF385C]] | B | TESMIN activity raises ZNF385C's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without TESMIN | 0.070 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[PRSS16]] | B | TESMIN activity raises PRSS16's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.18× lower at baseline in the lines without TESMIN | 0.085 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[GUCY1B2]] | C | TESMIN activity raises GUCY1B2's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.94× lower at baseline in the lines without TESMIN | 0.017 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent; co-absent with the target |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | TESMIN's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | TESMIN's natural level across 37 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.491 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.299). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-1.0, 31.0); signed map (38.0, -12.0). **Vector** length 67.8, 13.5% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.4 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | -0.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.0 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -11.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed metallothionein like protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:68,707,440-68,751,520 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CXCDC2; previously MTL5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4I5](https://www.uniprot.org/uniprotkb/Q9Y4I5) (Tesmin):

> Essential for normal spermatogenesis and male fertility (By similarity). Required for the completion of meiosis in male germ cells (By similarity).

**Summary**, from NCBI Gene [9633](https://www.ncbi.nlm.nih.gov/gene/9633):

> Metallothionein proteins are highly conserved low-molecular-weight cysteine-rich proteins that are induced by and bind to heavy metal ions and have no enzymatic activity. They may play a central role in the regulation of cell growth and differentiation and are involved in spermatogenesis. This gene encodes a metallothionein-like protein which has been shown to be expressed differentially in mouse testis and ovary. Two transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:7446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7446) · Entrez [9633](https://www.ncbi.nlm.nih.gov/gene/9633) · UniProt [Q9Y4I5](https://www.uniprot.org/uniprotkb/Q9Y4I5) · Ensembl [ENSG00000132749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132749)

## Data

Gene col 5366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5366); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5366]; `tensor/DDL_lfc|DDL_z.npy` [5366]; `embed/gene_vectors.npy` [5366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5366 or target_col == 5366). Every well: [[TESMIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TESMIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
