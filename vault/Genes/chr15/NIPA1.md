---
symbol: "NIPA1"
type: "gene"
col: 9905
ensembl_id: "ENSG00000170113"
name: "NIPA magnesium transporter 1"
location: "15q11.2"
module: 159
arm: "+"
pooled_cpm: 68.79
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# NIPA1

*NIPA magnesium transporter 1* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.31× (z +5.4, q 2e-05, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.486× (z -20.1, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBL]] (+0.64, fdr 1e-05), [[EXTL3]] (+0.61, fdr 1e-05), [[CRLF3]] (+0.60, fdr 2e-05); moves opposite to [[ZNF644]] (-0.55, fdr 1e-05), [[ZNF268]] (-0.54, fdr 5e-05), [[RBM23]] (-0.53, fdr 5e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00702]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 2e-05 | 25/46 (HOP62, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +5.4 | 2e-05 | 23/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.2 | 4e-05 | 30/47 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.002 | 22/47 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 0.002 | 20/47 (SW1417, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.486×** | -20.1 | 0e+00 | 39/47 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.602×** | -10.0 | 5e-21 | 34/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.596×** | -9.8 | 2e-20 | 32/40 (A549, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.598×** | -9.4 | 1e-18 | 30/43 (RKO, KATO III, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -8.6 | 6e-16 | 32/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.651×** | -8.5 | 3e-15 | 32/46 (NCI-H23, NCI-H460, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -7.4 | 1e-11 | 30/48 (NCI-H1792, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.777×** | -5.0 | 5e-05 | 22/47 (NCI-H460, AsPC-1, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.830×** | -3.7 | 0.015 | 19/47 (CFPAC-1, KATO III, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.877× | -3.7 | 0.015 | 8/47 (hTERT-HPNE, SNU-1, …) | top dose only |  |
| [[Allantoin (drug)]] 5 µM |  | 0.885× | -3.4 | 0.031 | 10/47 (NCI-H23, SHP-77, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.849× | -3.1 | 0.087 | 16/49 (SK-MEL-2, C32, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.857× | -3.0 | 0.10 | 12/47 (SW 1271, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 100 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -22.5) |
| [[NCI-H460 (line)]] | wt | 189 | 1 | 8 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.31× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -27.2) |
| [[AsPC-1 (line)]] | alt | 103 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.8) |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -21.4) |
| [[Hs 766T (line)]] | wt | 79.0 | 1 (1 ⚠) | 4 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.28× (z +10.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -18.1) |
| [[A549 (line)]] | wt | 83.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0448× (z -33.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 70.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -22.5) |
| [[RKO (line)]] | wt | 66.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 54.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -16.5) |
| [[A-172 (line)]] | wt | 55.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -14.1) |
| [[HOP62 (line)]] | alt | 34.5 | 2 | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.12× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 49.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -25.4) |
| [[LS 180 (line)]] | wt | 81.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 68.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 84.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -32.5) |
| [[NCI-H23 (line)]] | alt | 50.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.1) |
| [[SW480 (line)]] | alt | 71.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 56.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 97.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 42.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.3) |
| [[A498 (line)]] | wt | 47.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -8.9) |
| [[BT-474 (line)]] | alt | 79.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 69.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -20.0) |
| [[HepG2_C3A (line)]] | wt | 39.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0997× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[HS-578T (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.1) |
| [[HT-29 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -11.1) |
| [[J82 (line)]] | alt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.7) |
| [[KATO III (line)]] | alt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -16.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 80.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -19.9) |
| [[NCI-H2347 (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -12.2) |
| [[NCI-H596 (line)]] | alt | 72.7 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.141× (z -9.3) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 66.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.1) |
| [[PANC-1 (line)]] | alt | 82.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -10.6) |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.8) |
| [[SW 900 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBL]] | +0.64 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[EXTL3]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.60 | +0.74 / +0.46 | both halves | 2e-05 |  |
| [[DNAJC5]] | +0.58 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SGPP1]] | +0.57 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[CPOX]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[KYAT1]] | +0.55 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[HEBP1]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[TMEM65]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[SERAC1]] | +0.55 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[TSPAN17]] | +0.55 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[SLC27A4]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | -0.55 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.54 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[RBM23]] | -0.53 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[ASXL1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[HELQ]] | -0.52 | -0.71 / -0.32 | both halves | 2e-04 |  |
| [[FBXO38]] | -0.51 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[SRSF10]] | -0.51 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[LINC00702]] | -0.51 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[LINC00174]] | -0.50 | -0.65 / -0.29 | both halves | 2e-04 |  |
| [[EPC2]] | -0.50 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[ZFY]] | -0.50 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[HNRNPD]] | -0.50 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00702]] | B | LINC00702 activity lowers NIPA1's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 1.44× higher at baseline in the lines without LINC00702 | 0.056 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[CRACD]] | B | CRACD activity raises NIPA1's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without CRACD | 0.072 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, 3.4); signed map (-33.9, 18.7). **Vector** length 101, 24.6% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -20.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -10.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -8.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.8 | -1.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NIPA magnesium transporter 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q11.2 — chr15:22,773,063-22,829,789 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35570, SLC57A1; previously SPG6 |
| Gene groups (HGNC) | Solute carrier family 57, NIPA-like magnesium transporters |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTP0](https://www.uniprot.org/uniprotkb/Q7RTP0) (Magnesium transporter NIPA1):

> Acts as a Mg(2+) transporter. Can also transport other divalent cations such as Fe(2+), Sr(2+), Ba(2+), Zn(2+) and Co(2+) but to a much less extent than Mg(2+) (By similarity).

**Summary**, from NCBI Gene [123606](https://www.ncbi.nlm.nih.gov/gene/123606):

> This gene encodes a magnesium transporter that associates with early endosomes and the cell surface in a variety of neuronal and epithelial cells. This protein may play a role in nervous system development and maintenance. Multiple transcript variants encoding different isoforms have been found for this gene. Mutations in this gene have been associated with autosomal dominant spastic paraplegia 6. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:17043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17043) · Entrez [123606](https://www.ncbi.nlm.nih.gov/gene/123606) · UniProt [Q7RTP0](https://www.uniprot.org/uniprotkb/Q7RTP0) · Ensembl [ENSG00000170113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170113)

## Data

Gene col 9905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9905); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9905]; `tensor/DDL_lfc|DDL_z.npy` [9905]; `embed/gene_vectors.npy` [9905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9905 or target_col == 9905). Every well: [[NIPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
