---
symbol: "MTIF2"
type: "gene"
col: 1439
ensembl_id: "ENSG00000085760"
name: "mitochondrial translational initiation factor 2"
location: "2p16.1"
module: 1
arm: "+"
pooled_cpm: 51.23
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MTIF2

*mitochondrial translational initiation factor 2* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.14× (z +16.1, q 0e+00, up in 41 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.63× (z +7.2, q 9e-11, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.559× (z -8.5, q 1e-14, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD50]] (+0.75, fdr 7e-06), [[U2SURP]] (+0.73, fdr 7e-06), [[PPID]] (+0.71, fdr 7e-06); moves opposite to [[KMT5C]] (-0.59, fdr 1e-05), [[UBTD1]] (-0.57, fdr 2e-05), [[SSR4]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SOD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +16.1 | 0e+00 | 41/43 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +15.2 | 0e+00 | 45/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +8.6 | 2e-15 | 36/45 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +7.2 | 9e-11 | 37/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.5 | 8e-04 | 28/47 (LS 180, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.007 | 25/48 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.20× | +3.8 | 0.013 | 21/48 (HT-29, KATO III, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.016 | 24/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.016 | 23/48 (C32, NCI-H2030, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.17× | +3.3 | 0.048 | 13/48 (LoVo, HCT15, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.048 | 19/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.17× | +3.2 | 0.066 | 21/48 (LoVo, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +3.1 | 0.093 | 20/48 (COLO 205, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1439.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.559×** | -8.5 | 1e-14 | 40/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -8.1 | 2e-13 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -8.1 | 2e-13 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.628×** | -6.8 | 2e-09 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -4.7 | 3e-04 | 31/48 (SNU-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.727×** | -4.6 | 3e-04 | 27/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -4.3 | 0.001 | 30/49 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -3.6 | 0.026 | 20/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.789×** | -3.4 | 0.036 | 20/48 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.043 | 19/49 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.054 | 18/48 (SW 1088, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Isocorydine (drug)]] 5 µM |  | 0.858× | -3.2 | 0.076 | 8/48 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.860× | -3.1 | 0.085 | 9/48 (Hs 766T, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 71.4 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +16.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.378× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.404× (z -10.5) |
| [[PANC-1 (line)]] | alt | 67.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -13.0) |
| [[A-427 (line)]] | wt | 106 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.12× (z +11.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.355× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.378× (z -10.2) |
| [[LoVo (line)]] | wt | 53.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 60.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 97.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.52× (z +12.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.380× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 38.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 41.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 64.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 38.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 50.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 55.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 24.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 65.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +13.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 40.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 70.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +8.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.332× (z -9.4) |
| [[SW 900 (line)]] | alt | 36.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 39.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 63.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 60.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 53.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 40.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 54.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 54.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD50]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[U2SURP]] | +0.73 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PPID]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ICE2]] | +0.70 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[GTF2H3]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[GUF1]] | +0.69 | +0.75 / +0.57 | both halves | 1e-05 | same gene group; STRING 570 |
| [[NOL8]] | +0.67 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.67 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[RSL1D1]] | +0.65 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[LARS1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | STRING 550 |
| [[NOP14]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT5C]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[SSR4]] | -0.57 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[STK32C]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PDXP]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PTOV1]] | -0.55 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[GNB2]] | -0.55 | -0.63 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOD3]] | B | SOD3 activity lowers MTIF2's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 1.30× higher at baseline in the lines without SOD3 | 0.033 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20 |
| [[HDAC6]] | B | HDAC6 activity raises MTIF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.3, 7.6); signed map (8.5, -30.5). **Vector** length 95.5, 26.2% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +5.6 | +3.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.3 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -8.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -0.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -1.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.4 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial translational initiation factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,236,595-55,269,347 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IF-2mt |
| Gene groups (HGNC) | Translational GTPases |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 3 pathways, smallest: Mitochondrial translation initiation; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P46199](https://www.uniprot.org/uniprotkb/P46199) (Translation initiation factor IF-2, mitochondrial):

> Mitochondrial translation initiation factor that promotes binding of formylmethionyl-tRNA to the 30S ribosomal subunits (By similarity). Also involved in the hydrolysis of GTP during the formation of the 70S ribosomal complex (By similarity).

**Summary**, from NCBI Gene [4528](https://www.ncbi.nlm.nih.gov/gene/4528):

> During the initiation of protein biosynthesis, initiation factor-2 (IF-2) promotes the binding of the initiator tRNA to the small subunit of the ribosome in a GTP-dependent manner. Prokaryotic IF-2 is a single polypeptide, while eukaryotic cytoplasmic IF-2 (eIF-2) is a trimeric protein. Bovine liver mitochondria contain IF-2(mt), an 85-kD monomeric protein that is equivalent to prokaryotic IF-2. The predicted 727-amino acid human protein contains a 29-amino acid presequence. Human IF-2(mt) …

**Accessions** — [HGNC:7441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7441) · Entrez [4528](https://www.ncbi.nlm.nih.gov/gene/4528) · UniProt [P46199](https://www.uniprot.org/uniprotkb/P46199) · Ensembl [ENSG00000085760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085760)

## Data

Gene col 1439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1439); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1439]; `tensor/DDL_lfc|DDL_z.npy` [1439]; `embed/gene_vectors.npy` [1439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1439 or target_col == 1439). Every well: [[MTIF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTIF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
