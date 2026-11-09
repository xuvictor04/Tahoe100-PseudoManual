---
symbol: "CRLF3"
type: "gene"
col: 10709
ensembl_id: "ENSG00000176390"
name: "cytokine receptor like factor 3"
location: "17q11.2"
module: 159
arm: "+"
pooled_cpm: 45.88
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# CRLF3

*cytokine receptor like factor 3* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.66× (z +10.6, q 2e-23, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.813× (z -6.1, q 5e-07, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.201×, A-427 0.252×, AsPC-1 0.295×, HEC-1-A 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.514×, A-172 0.561×, LOX-IMVI 0.549×, NCI-H23 0.555×; ⚠ cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.150×, A-427 0.431×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cilostazol (drug)]] 0.05 µM in 1 line (SW 1271 0.0559×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.404×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.479×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERAC1]] (+0.75, fdr 7e-06), [[AP2A2]] (+0.75, fdr 7e-06), [[PACC1]] (+0.70, fdr 1e-05); moves opposite to [[LINC00571]] (-0.66, fdr 3e-05), [[MZF1-AS1]] (-0.66, fdr 5e-05), [[PCNX4-DT]] (-0.64, fdr 9e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RIMS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +10.6 | 2e-23 | 42/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +9.8 | 5e-20 | 43/48 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +8.7 | 7e-16 | 35/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.6 | 6e-09 | 29/47 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +6.2 | 7e-08 | 26/47 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 1e-06 | 28/48 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.5 | 2e-06 | 28/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.0 | 4e-05 | 23/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.9 | 5e-05 | 23/48 (HT-29, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.9 | 5e-05 | 16/48 (SW 900, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 4e-04 | 19/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 6e-04 | 19/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +4.1 | 0.001 | 18/48 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.1 | 0.001 | 19/47 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +4.0 | 0.003 | 20/47 (NCI-H2347, J82, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.032 | 7/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.201×, A-427 0.252×, AsPC-1 0.295×, HEC-1-A 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.514×, A-172 0.561×, LOX-IMVI 0.549×, NCI-H23 0.555×; ⚠ cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.150×, A-427 0.431×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cilostazol (drug)]] 0.05 µM in 1 line (SW 1271 0.0559×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.404×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.479×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -6.1 | 5e-07 | 21/48 (SW48, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.895× | -3.3 | 0.20 | 7/48 (A-172, NCI-H661, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.2 | 0.20 | 11/48 (A-427, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.861× | -3.1 | 0.20 | 19/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.900× | -3.1 | 0.20 | 18/48 (A-427, A-172, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 56.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.479× (z -8.5) |
| [[A-427 (line)]] | wt | 88.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 42.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.12× (z +18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 70.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.5) |
| [[SW480 (line)]] | alt | 41.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.15× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -9.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[RKO (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 1 | — | [[Cilostazol (drug)]] 0.05 µM 0.0559× (z -10.0) |
| [[A498 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERAC1]] | +0.75 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[AP2A2]] | +0.75 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[PACC1]] | +0.70 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[NR2C1]] | +0.68 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[BRF1]] | +0.68 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[CROCCP3]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[EPS15]] | +0.68 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.68 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[SGPP1]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.67 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[ACTR5]] | +0.66 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[PBX4]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00571]] | -0.66 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | -0.66 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[PCNX4-DT]] | -0.64 | -0.64 / -0.36 | both halves | 9e-05 |  |
| [[CCDC90B-AS1]] | -0.63 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[UBE3B]] | -0.63 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[MCPH1]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[RBM23]] | -0.62 | -0.69 / -0.35 | both halves | 1e-04 |  |
| [[ZNF747]] | -0.61 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[SON]] | -0.61 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | -0.61 | -0.60 / -0.29 | both halves | 3e-04 |  |
| [[AEBP2]] | -0.61 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ZNF764]] | -0.61 | -0.68 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMS3]] | B | RIMS3 activity raises CRLF3's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.23× lower at baseline in the lines without RIMS3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[LINC01252]] | B | LINC01252 activity lowers CRLF3's level | lines that do not express LINC01252 (17) vs lines expressing it (33) | 1.16× higher at baseline in the lines without LINC01252 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000275119, EPHB6, ABCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.7, 1.4); signed map (-42.1, -7.2). **Vector** length 97.7, 21.9% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +10.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -7.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.3 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +0.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cytokine receptor like factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,769,388-30,824,692 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CREME9, CYTOR4 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUI8](https://www.uniprot.org/uniprotkb/Q8IUI8) (Cytokine receptor-like factor 3):

> May play a role in the negative regulation of cell cycle progression.

**Summary**, from NCBI Gene [51379](https://www.ncbi.nlm.nih.gov/gene/51379):

> This gene encodes a cytokine receptor-like factor that may negatively regulate cell cycle progression at the G0/G1 phase. Studies of the related rat protein suggest that it may regulate neuronal morphology and synaptic vesicle biogenesis. This gene is one of several genes located in the neurofibromatosis type I tumor suppressor region on the q arm of chromosome 17, a region that is subject to microdeletions, duplications, chromosomal breaks and rearrangements. Alternative splicing of this gene …

**Accessions** — [HGNC:17177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17177) · Entrez [51379](https://www.ncbi.nlm.nih.gov/gene/51379) · UniProt [Q8IUI8](https://www.uniprot.org/uniprotkb/Q8IUI8) · Ensembl [ENSG00000176390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176390)

## Data

Gene col 10709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10709); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10709]; `tensor/DDL_lfc|DDL_z.npy` [10709]; `embed/gene_vectors.npy` [10709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10709 or target_col == 10709). Every well: [[CRLF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRLF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
