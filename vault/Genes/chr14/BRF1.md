---
symbol: "BRF1"
type: "gene"
col: 11612
ensembl_id: "ENSG00000185024"
name: "BRF1 general transcription factor IIIB subunit"
location: "14q32.33"
module: 77
arm: "+"
pooled_cpm: 28.45
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# BRF1

*BRF1 general transcription factor IIIB subunit* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.54× (z +8.0, q 8e-13, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.718× (z -8.7, q 1e-15, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.733× (z -8.1, q 9e-14, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLRMT]] (+0.73, fdr 1e-05), [[TRABD]] (+0.72, fdr 1e-05), [[ANKRD27]] (+0.72, fdr 2e-05); moves opposite to [[THAP2]] (-0.68, fdr 4e-05), [[ERCC6L2-AS1]] (-0.66, fdr 3e-04), [[IFNAR1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +8.0 | 8e-13 | 33/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.4 | 2e-05 | 24/47 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 3e-05 | 26/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.005 | 19/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.23×** | +3.9 | 0.013 | 13/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.041 | 13/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.041 | 12/48 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.718×** | -8.7 | 1e-15 | 31/47 (J82, LOX-IMVI, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.626×** | -8.6 | 1e-15 | 27/43 (C32, A-427, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -8.1 | 9e-14 | 31/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.635×** | -7.8 | 1e-12 | 23/40 (SW48, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -7.4 | 2e-11 | 28/46 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -7.2 | 4e-11 | 26/48 (SNU-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.759×** | -7.2 | 6e-11 | 30/48 (HOP62, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.680×** | -6.8 | 5e-10 | 23/38 (LOX-IMVI, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.681×** | -6.8 | 6e-10 | 26/48 (NCI-H2347, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -6.4 | 8e-09 | 26/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -6.0 | 9e-08 | 27/47 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -4.9 | 5e-05 | 4/48 (AN3 CA, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -4.2 | 0.001 | 19/48 (MIA PaCa-2, SW480, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -4.2 | 0.001 | 24/47 (A-172, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.814×** | -3.8 | 0.006 | 21/47 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.880× | -3.3 | 0.032 | 12/48 (A498, RKO, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.843× | -3.0 | 0.081 | 8/47 (A549, C-33 A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.794×** | -2.9 | 0.097 | 17/45 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 30.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 4.87× (z +13.8) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.294× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -11.8) |
| [[A-172 (line)]] | wt | 16.2 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.167× (z -12.6) |
| [[A-427 (line)]] | wt | 52.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 29.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -14.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 28.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0709× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.0) |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 48.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 69.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0968× (z -17.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.7) |
| [[C-33 A (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.236× (z -9.7) |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.6) |
| [[J82 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 39.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -13.4) |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0694× (z -13.6) |
| [[SW480 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLRMT]] | +0.73 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TRABD]] | +0.72 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.72 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[BRAT1]] | +0.71 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TCF3]] | +0.71 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.70 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[CEP131]] | +0.70 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.69 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[PACC1]] | +0.69 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[MAST3]] | +0.69 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[EPHB4]] | +0.68 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[E4F1]] | +0.68 | +0.68 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.68 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6L2-AS1]] | -0.66 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[IFNAR1]] | -0.66 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.66 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MCTS1]] | -0.66 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ZNF341-AS1]] | -0.65 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.65 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[LINC00571]] | -0.64 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[LPXN]] | -0.64 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[TSGA10]] | -0.64 | -0.62 / -0.21 | both halves | 7e-04 |  |
| [[LINC01004]] | -0.63 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | -0.63 | -0.57 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BRF1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FLRT2]] | B | FLRT2 activity lowers BRF1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.22× higher at baseline in the lines without FLRT2 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[HDAC6]] | B | HDAC6 activity lowers BRF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DNMT3B]] | C | DNMT3B activity raises BRF1's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without DNMT3B | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.3, -0.7); signed map (-41.7, -7.4). **Vector** length 89.1, 18.1% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +8.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.9 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.2 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.0 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | BRF1 general transcription factor IIIB subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,209,286-105,315,589 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIIB90, BRF, hBRF; previously TAF3B2, TAF3C, GTF3B |
| Gene groups (HGNC) | General transcription factors; General transcription factor IIIB complex subunits |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92994](https://www.uniprot.org/uniprotkb/Q92994) (Transcription factor IIIB 90 kDa subunit):

> General activator of RNA polymerase which utilizes different TFIIIB complexes at structurally distinct promoters. The isoform 1 is involved in the transcription of tRNA, adenovirus VA1, 7SL and 5S RNA. Isoform 2 is required for transcription of the U6 promoter.

**Summary**, from NCBI Gene [2972](https://www.ncbi.nlm.nih.gov/gene/2972):

> This gene encodes one of the three subunits of the RNA polymerase III transcription factor complex. This complex plays a central role in transcription initiation by RNA polymerase III on genes encoding tRNA, 5S rRNA, and other small structural RNAs. The gene product belongs to the TF2B family. Several alternatively spliced variants encoding different isoforms, that function at different promoters transcribed by RNA polymerase III, have been identified. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:11551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11551) · Entrez [2972](https://www.ncbi.nlm.nih.gov/gene/2972) · UniProt [Q92994](https://www.uniprot.org/uniprotkb/Q92994) · Ensembl [ENSG00000185024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185024)

## Data

Gene col 11612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11612); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11612]; `tensor/DDL_lfc|DDL_z.npy` [11612]; `embed/gene_vectors.npy` [11612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11612 or target_col == 11612). Every well: [[BRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
