---
symbol: "DNAJA3"
type: "gene"
col: 2365
ensembl_id: "ENSG00000103423"
name: "DnaJ heat shock protein family (Hsp40) member A3"
location: "16p13.3"
module: 1
arm: "+"
pooled_cpm: 24.09
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DNAJA3

*DnaJ heat shock protein family (Hsp40) member A3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.32× (z +16.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.659× (z -8.3, q 9e-14, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 0.273×, KATO III 0.260×, SW480 0.364×, LS 180 0.257×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (PANC-1 0.284×, SW480 0.350×, KATO III 0.362×, LS 180 0.327×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.131×, NCI-H23 0.238×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-1 0.0682×); [[Eplerenone (drug)]] 0.05 µM in 1 line (AN3 CA 0.0689×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFRD2]] (+0.67, fdr 7e-06), [[PINX1]] (+0.67, fdr 7e-06), [[PDCD11]] (+0.66, fdr 7e-06); moves opposite to [[GNAS]] (-0.66, fdr 7e-06), [[TXNDC16]] (-0.62, fdr 3e-05), [[PERP]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMSB4X]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +16.6 | 0e+00 | 45/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +16.3 | 0e+00 | 42/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +14.3 | 2e-44 | 44/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +10.8 | 4e-25 | 35/47 (A-172, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +10.4 | 2e-23 | 40/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.52×** | +7.9 | 3e-13 | 19/34 (LoVo, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +7.5 | 5e-12 | 27/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 2e-11 | 25/47 (Hs 766T, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.40×** | +6.6 | 2e-09 | 22/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 3e-07 | 20/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +5.4 | 3e-06 | 17/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.8 | 6e-05 | 24/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.57×** | +4.7 | 1e-04 | 19/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +4.6 | 1e-04 | 17/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +4.6 | 1e-04 | 13/46 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +4.4 | 3e-04 | 18/45 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 9e-04 | 18/48 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 6/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.008 | 12/48 (A549, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2365.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 0.273×, KATO III 0.260×, SW480 0.364×, LS 180 0.257×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (PANC-1 0.284×, SW480 0.350×, KATO III 0.362×, LS 180 0.327×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.131×, NCI-H23 0.238×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-1 0.0682×); [[Eplerenone (drug)]] 0.05 µM in 1 line (AN3 CA 0.0689×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -8.3 | 9e-14 | 27/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -7.4 | 5e-11 | 27/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -6.9 | 8e-10 | 22/46 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.5 | 0.079 | 17/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.1 | 0.25 | 5/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.8 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +11.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -13.3) |
| [[A-172 (line)]] | wt | 24.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.30× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +9.8) | — |
| [[KATO III (line)]] | alt | 42.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -9.7) |
| [[LS 180 (line)]] | wt | 21.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -8.9) |
| [[PANC-1 (line)]] | alt | 41.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -14.1) |
| [[A-427 (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 1 | — | [[Eplerenone (drug)]] 0.05 µM 0.0689× (z -8.6) |
| [[COLO 205 (line)]] | alt | 19.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.11× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.110× (z -10.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0682× (z -10.8) |
| [[A498 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFRD2]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PINX1]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LARS1]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[NLE1]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[REXO4]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[FARSB]] | +0.64 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[IMP4]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TRIM27]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TATDN1]] | +0.64 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SLX9]] | +0.63 | +0.49 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[TXNDC16]] | -0.62 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PERP]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 | STRING 448 |
| [[CTSV]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PTMS]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[B2M]] | -0.56 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[HLA-A]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ARL6IP1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ATP1B1]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ZNF821]] | -0.54 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMSB4X]] | B | TMSB4X activity lowers DNAJA3's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without TMSB4X | 0.072 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.3, -39.4); signed map (-4.0, -45.7). **Vector** length 83.4, 17.0% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +10.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +10.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,425,805-4,456,775 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hTid-1, Tid1-S, Tid1-L; previously TID1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EY1](https://www.uniprot.org/uniprotkb/Q96EY1) (DnaJ homolog subfamily A member 3, mitochondrial):

> Modulates apoptotic signal transduction or effector structures within the mitochondrial matrix. Affect cytochrome C release from the mitochondria and caspase 3 activation, but not caspase 8 activation. Isoform 1 increases apoptosis triggered by both TNF and the DNA-damaging agent mytomycin C; in sharp contrast, isoform 2 suppresses apoptosis. Can modulate IFN-gamma-mediated transcriptional activity. Isoform 2 may play a role in neuromuscular junction development as an effector of the MUSK …

**Summary**, from NCBI Gene [9093](https://www.ncbi.nlm.nih.gov/gene/9093):

> This gene encodes a member of the DNAJ/Hsp40 protein family. DNAJ/Hsp40 proteins stimulate the ATPase activity of Hsp70 chaperones and play critical roles in protein folding, degradation, and multimeric complex assembly. The encoded protein is localized to mitochondria and mediates several cellular processes including proliferation, survival and apoptotic signal transduction. The encoded protein also plays a critical role in tumor suppression through interactions with oncogenic proteins …

**Accessions** — [HGNC:11808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11808) · Entrez [9093](https://www.ncbi.nlm.nih.gov/gene/9093) · UniProt [Q96EY1](https://www.uniprot.org/uniprotkb/Q96EY1) · Ensembl [ENSG00000103423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103423)

## Data

Gene col 2365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2365); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2365]; `tensor/DDL_lfc|DDL_z.npy` [2365]; `embed/gene_vectors.npy` [2365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2365 or target_col == 2365). Every well: [[DNAJA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
