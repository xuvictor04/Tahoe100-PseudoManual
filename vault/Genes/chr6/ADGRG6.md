---
symbol: "ADGRG6"
type: "gene"
col: 3369
ensembl_id: "ENSG00000112414"
name: "adhesion G protein-coupled receptor G6"
location: "6q24.2"
module: 24
arm: "-"
pooled_cpm: 152.77
n_lines_expressing: 38
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ADGRG6

*adhesion G protein-coupled receptor G6* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.49× (z +5.0, q 3e-04, up in 20 of 34 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 4.77×, MIA PaCa-2 3.42×, A549 3.12×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 2.92×, A549 2.42×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 3.33×, COLO 205 3.23×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (C32 3.65×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.350× (z -14.4, q 4e-44, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBNL1]] (+0.62, fdr 1e-05), [[GNG12]] (+0.56, fdr 5e-05), [[BTBD1]] (+0.56, fdr 4e-05); moves opposite to [[TBC1D20]] (-0.58, fdr 1e-04), [[VEGFA]] (-0.56, fdr 4e-05), [[RBCK1]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFIB]] → it (grade B ⚠); 7 go from it, the strongest it → [[MED10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3369.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 4.77×, MIA PaCa-2 3.42×, A549 3.12×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 2.92×, A549 2.42×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 3.33×, COLO 205 3.23×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (C32 3.65×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +5.0 | 3e-04 | 20/34 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.27× | +3.3 | 0.26 | 17/37 (SK-MEL-2, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.26 | 17/36 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.25× | +3.0 | 0.30 | 14/36 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 1.52× | +3.0 | 0.30 | 15/35 (NCI-H1573, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.350×** | -14.4 | 4e-44 | 35/36 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.356×** | -14.2 | 4e-43 | 35/36 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.457×** | -10.8 | 1e-24 | 33/36 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -6.6 | 6e-09 | 30/36 (Hs 766T, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -5.3 | 1e-05 | 21/37 (C-33 A, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -5.3 | 1e-05 | 29/36 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.768×** | -5.1 | 3e-05 | 21/36 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.528×** | -4.6 | 3e-04 | 24/36 (HCT15, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -4.5 | 3e-04 | 22/36 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.541×** | -4.4 | 6e-04 | 26/36 (A549, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.563×** | -4.1 | 0.002 | 25/36 (HepG2/C3A, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.750×** | -3.9 | 0.004 | 22/36 (Hs 766T, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.585×** | -3.8 | 0.005 | 22/36 (A549, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.757×** | -3.8 | 0.006 | 21/36 (NCI-H23, BT-474, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.764×** | -3.7 | 0.008 | 26/37 (RKO, HOP62, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.684×** | -3.6 | 0.010 | 22/36 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.014 | 23/36 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.640×** | -3.2 | 0.043 | 21/36 (NCI-H2347, A549, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 203 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -15.9) |
| [[C-33 A (line)]] | alt | 1,238 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0901× (z -25.0) |
| [[A549 (line)]] | wt | 198 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -13.3) |
| [[RKO (line)]] | wt | 123 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -14.0) |
| [[CHP-212 (line)]] | wt | 474 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 241 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -16.4) |
| [[A-427 (line)]] | wt | 578 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -21.1) |
| [[CFPAC-1 (line)]] | alt | 237 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -17.9) |
| [[Hs 766T (line)]] | wt | 83.3 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -10.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -9.7) |
| [[HT-29 (line)]] | alt | 127 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -9.3) |
| [[KATO III (line)]] | alt | 157 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 92.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -13.3) |
| [[PANC-1 (line)]] | alt | 381 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -16.5) |
| [[A498 (line)]] | wt | 53.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.398× (z -9.3) |
| [[C32 (line)]] | wt | 46.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.65× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 56.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.292× (z -9.4) |
| [[HCT15 (line)]] | alt | 218 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 293 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 322 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 96.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.77× (z +12.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 137 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.338× (z -9.7) |
| [[LoVo (line)]] | wt | 108 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 416 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.42× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 73.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 228 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -9.2) |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.112× (z -8.6) |
| [[A-172 (line)]] | wt | 30.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL1]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[GNG12]] | +0.56 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[BTBD1]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[LPP]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[UTRN]] | +0.54 | +0.30 / +0.58 | both halves | 2e-04 | pathway: EGR2 and SOX10-mediated initiation of Schwann cell myelination |
| [[DDAH1]] | +0.52 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[ADAM9]] | +0.52 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[CDK6]] | +0.52 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[FAT4]] | +0.52 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[DR1]] | +0.51 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[RBMS2]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[PRKG1-AS1]] | +0.51 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D20]] | -0.58 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[VEGFA]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[RBCK1]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[SNHG7]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[RAB24]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[LIN7B]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SIRT7]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[CNNM4]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[VPS37D]] | -0.51 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[HSDL1]] | -0.51 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[CCDC127]] | -0.51 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[GOLGA6L9]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIB]] | B | NFIB activity raises ADGRG6's level | lines that do not express NFIB (7) vs lines expressing it (43) | 3.45× lower at baseline in the lines without NFIB | 0.071 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[UTRN]] | C | UTRN activity raises ADGRG6's level | lines that do not express UTRN (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without UTRN | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |
| [[RBMS2]] | C | RBMS2 activity raises ADGRG6's level | lines that do not express RBMS2 (3) vs lines expressing it (47) | 5.00× lower at baseline in the lines without RBMS2 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HOMER3, ARHGAP10, TMEM144; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MED10]] | B | ADGRG6 activity lowers MED10's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.46× higher at baseline in the lines without ADGRG6 | 0.011 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[TMEM255B]] | B | ADGRG6 activity lowers TMEM255B's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 2.18× higher at baseline in the lines without ADGRG6 | 0.052 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[FUCA2]] | B | ADGRG6 activity lowers FUCA2's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.74× higher at baseline in the lines without ADGRG6 | 0.060 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[ZIM2-AS1]] | B | ADGRG6 activity lowers ZIM2-AS1's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.99× higher at baseline in the lines without ADGRG6 | 0.061 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[ARAP2]] | B | ADGRG6 activity raises ARAP2's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without ADGRG6 | 0.063 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[DDAH1]] | B | ADGRG6 activity raises DDAH1's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without ADGRG6 | 0.068 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[LAMB1]] | B | ADGRG6 activity raises LAMB1's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without ADGRG6 | 0.090 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (6.3, -20.4); signed map (20.5, -38.0). **Vector** length 126, 36.9% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.9 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.4 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -5.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.3 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.1 | -6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor G6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:142,301,854-142,446,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14937; previously GPR126 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily G |
| Reactome | 2 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SQ4](https://www.uniprot.org/uniprotkb/Q86SQ4) (Adhesion G protein-coupled receptor G6):

> Adhesion G protein-coupled receptor (aGPCR) for steroid hormones, such as progesterone and 17alpha-hydroxyprogesterone (17OHP). Involved in many biological processes, such as myelination, sprouting angiogenesis, placenta, ear and cartilage development (By similarity). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. ADGRG6 is coupled to G(i) G …

**Summary**, from NCBI Gene [57211](https://www.ncbi.nlm.nih.gov/gene/57211):

> This gene, which is upregulated in human umbilical vein endothelial cells, encodes a G protein-coupled receptor. Variations in this gene can affect a person's stature. Multiple transcript variants encoding different proteins have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:13841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13841) · Entrez [57211](https://www.ncbi.nlm.nih.gov/gene/57211) · UniProt [Q86SQ4](https://www.uniprot.org/uniprotkb/Q86SQ4) · Ensembl [ENSG00000112414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112414)

## Data

Gene col 3369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3369); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3369]; `tensor/DDL_lfc|DDL_z.npy` [3369]; `embed/gene_vectors.npy` [3369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3369 or target_col == 3369). Every well: [[ADGRG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
