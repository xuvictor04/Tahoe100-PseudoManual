---
symbol: "ASIC1"
type: "gene"
col: 3175
ensembl_id: "ENSG00000110881"
name: "acid sensing ion channel subunit 1"
location: "12q13.12"
module: 176
arm: "+"
pooled_cpm: 5.86
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# ASIC1

*acid sensing ion channel subunit 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.91× (z +8.3, q 5e-14, up in 15 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.81× (z +7.6, q 7e-12, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -18.1, q 0e+00, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCOLN2]] (+0.75, fdr 7e-06), [[CGREF1]] (+0.71, fdr 1e-05), [[GLB1L2]] (+0.69, fdr 7e-06); moves opposite to [[XRN1]] (-0.62, fdr 7e-06), [[GGPS1]] (-0.60, fdr 1e-05), [[C6orf62]] (-0.59, fdr 1e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); 8 go from it, the strongest it → [[PDPK1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.91×** | +8.3 | 5e-14 | 15/23 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +7.6 | 7e-12 | 22/37 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.84×** | +7.6 | 7e-12 | 4/9 (CFPAC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.79×** | +7.2 | 1e-10 | 8/27 (NCI-H23, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.1 | 1e-10 | 21/42 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.64×** | +5.9 | 4e-07 | 8/16 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.52×** | +5.4 | 5e-06 | 14/44 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.8 | 1e-04 | 17/44 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.43×** | +4.6 | 2e-04 | 15/42 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +4.1 | 0.003 | 4/38 (PANC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.0 | 0.003 | 10/43 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.003 | 7/44 (SW480, SW48, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.36×** | +3.9 | 0.003 | 15/44 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.004 | 2/41 (NCI-H460, NCI-H23) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.005 | 4/41 (RKO, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.017 | 1/40 (HT-29) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +3.1 | 0.063 | 2/31 (HEC-1-A, SW1417) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.371×** | -18.1 | 0e+00 | 27/35 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.274×** | -16.6 | 0e+00 | 28/35 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.587×** | -6.6 | 8e-09 | 18/41 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -6.4 | 3e-08 | 20/44 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -6.3 | 4e-08 | 15/43 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -5.7 | 1e-06 | 16/37 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -5.2 | 2e-05 | 20/34 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.678×** | -5.0 | 4e-05 | 15/41 (SNU-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -4.9 | 5e-05 | 16/42 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.675×** | -4.9 | 6e-05 | 14/37 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -4.7 | 1e-04 | 11/40 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.684×** | -4.6 | 2e-04 | 10/39 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.528×** | -4.3 | 8e-04 | 8/40 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.544×** | -4.1 | 0.002 | 13/38 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -4.0 | 0.003 | 15/41 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.744×** | -3.8 | 0.005 | 11/43 (SW480, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -21.3) |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 5.60 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -15.4) |
| [[RKO (line)]] | wt | 17.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0565× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0724× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.0) |
| [[HOP62 (line)]] | alt | 3.56 | 0 | 2 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0658× (z -10.6) ⚠ toxic; unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.216× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 6.50 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0754× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 8.27 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -15.6) |
| [[SW48 (line)]] | wt | 26.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -11.0) |
| [[SW480 (line)]] | alt | 8.59 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -15.8) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.2) |
| [[HT-29 (line)]] | alt | 3.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 5.86 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0662× (z -10.9) ⚠ cell-cycle shift, explains ~11% of this change |
| [[NCI-H23 (line)]] | alt | 9.11 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -8.5) |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0738× (z -10.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCOLN2]] | +0.75 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Ion channel transport |
| [[CGREF1]] | +0.71 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PODXL2]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CCDC88C]] | +0.67 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[ADAT2]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MEST]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[FXN]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LRRC20]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[KBTBD11]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[METAP1]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRN1]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[GGPS1]] | -0.60 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[C6orf62]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ZMAT2]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[GPS2]] | -0.58 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[GOLGB1]] | -0.58 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | -0.57 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[ASH1L]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | -0.56 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[N4BP2L2]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ANKHD1-EIF4EBP3]] | -0.55 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[BPTF]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises ASIC1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without MCOLN2 | 0.009 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[SEMA6B]] | B | SEMA6B activity raises ASIC1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without SEMA6B | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[WFDC10B]] | B | WFDC10B activity lowers ASIC1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.94× higher at baseline in the lines without WFDC10B | 0.027 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises ASIC1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without ARHGAP44 | 0.038 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises ASIC1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.71× lower at baseline in the lines without GNAZ | 0.060 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[PODXL2]] | B | PODXL2 activity raises ASIC1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without PODXL2 | 0.064 | ⚠ within organs, on part of the lines |
| [[NTN4]] | B | NTN4 activity lowers ASIC1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.16× higher at baseline in the lines without NTN4 | 0.065 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[ADCY3]] | B | ADCY3 activity raises ASIC1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without ADCY3 | 0.086 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[NT5M]] | B | NT5M activity raises ASIC1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without NT5M | 0.089 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[GPD1L]] | C | GPD1L activity raises ASIC1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without GPD1L | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[SMARCD3]] | C | SMARCD3 activity raises ASIC1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDPK1]] | C | ASIC1 activity lowers PDPK1's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 1.56× higher at baseline in the lines without ASIC1 | 0.017 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |
| [[DDHD1]] | C | ASIC1 activity raises DDHD1's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 3.76× lower at baseline in the lines without ASIC1 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391; co-absent with the target |
| [[ADCY3]] | C | ASIC1 activity raises ADCY3's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 4.06× lower at baseline in the lines without ASIC1 | 0.037 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |
| [[FGFR4]] | C | ASIC1 activity strengthens FGFR4's drug response | lines that do not express ASIC1 (3) vs lines expressing it (32) | the lines without ASIC1 respond 0.41× as strongly (z diff +1.86); strongest at Panobinostat 0.05 µM: 1.06x vs 2.36x (z diff +2.8) | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391; target measured in part of the lines; artifact flags |
| [[FAM234B]] | C | ASIC1 activity raises FAM234B's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without ASIC1 | 0.050 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |
| [[SCD5]] | C | ASIC1 activity raises SCD5's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 5.95× lower at baseline in the lines without ASIC1 | 0.050 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |
| [[PHC1]] | C | ASIC1 activity raises PHC1's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 2.84× lower at baseline in the lines without ASIC1 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |
| [[FGFR4]] | C | ASIC1 activity lowers FGFR4's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 2.93× higher at baseline in the lines without ASIC1 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.835). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.4, 41.7); signed map (-7.1, -57.3). **Vector** length 75.2, 13.5% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -16.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -18.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.2 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -6.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | acid sensing ion channel subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,057,548-50,083,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BNaC2, hBNaC2; previously ACCN2 |
| Gene groups (HGNC) | Acid sensing ion channel subunits |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P78348](https://www.uniprot.org/uniprotkb/P78348) (Acid-sensing ion channel 1):

> Forms voltage-independent, pH-gated trimeric sodium channels that act as postsynaptic excitatory receptors in the nervous system, playing a crucial role in regulating synaptic plasticity, learning, and memory. Upon extracellular pH drop this channel elicits transient, fast activating, and completely desensitizing inward currents. Displays high selectivity for sodium ions but can also permit the permeation of other cations. Regulates more or less directly intracellular calcium concentration and …

**Summary**, from NCBI Gene [41](https://www.ncbi.nlm.nih.gov/gene/41):

> This gene encodes a member of the acid-sensing ion channel (ASIC) family of proteins, which are part of the degenerin/epithelial sodium channel (DEG/ENaC) superfamily. Members of the ASIC family are sensitive to amiloride and function in neurotransmission. The encoded proteins function in learning, pain transduction, touch sensation, and development of memory and fear. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:100) · Entrez [41](https://www.ncbi.nlm.nih.gov/gene/41) · UniProt [P78348](https://www.uniprot.org/uniprotkb/P78348) · Ensembl [ENSG00000110881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110881)

## Data

Gene col 3175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3175); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3175]; `tensor/DDL_lfc|DDL_z.npy` [3175]; `embed/gene_vectors.npy` [3175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3175 or target_col == 3175). Every well: [[ASIC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASIC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
