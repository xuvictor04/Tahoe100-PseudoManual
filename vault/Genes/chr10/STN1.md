---
symbol: "STN1"
type: "gene"
col: 2906
ensembl_id: "ENSG00000107960"
name: "STN1 subunit of CST complex"
location: "10q24.33"
module: 174
arm: "+"
pooled_cpm: 26.86
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# STN1

*STN1 subunit of CST complex* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.33× (z +5.4, q 5e-05, up in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.31× (z +5.1, q 1e-04, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 3.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -27.8, q 0e+00, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETHE1]] (+0.65, fdr 1e-05), [[TBC1D8]] (+0.63, fdr 1e-05), [[FLNB]] (+0.61, fdr 6e-05); moves opposite to [[TTC6]] (-0.59, fdr 3e-05), [[FBXL19-AS1]] (-0.58, fdr 2e-04), [[RUFY3]] (-0.57, fdr 4e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KRT15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 3.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +5.4 | 5e-05 | 21/47 (A-172, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.1 | 1e-04 | 23/47 (Hs 766T, A-172, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.26×** | +4.4 | 0.002 | 15/40 (HEC-1-A, A-427, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.3 | 0.002 | 19/47 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.25×** | +4.3 | 0.002 | 17/47 (A-172, A-427, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.019 | 12/47 (SNU-423, SW 900, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +3.3 | 0.078 | 16/47 (A-172, Hs 766T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.12 | 10/47 (Hs 766T, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -27.8 | 0e+00 | 35/46 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.360×** | -19.3 | 0e+00 | 44/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.360×** | -19.3 | 0e+00 | 41/46 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.414×** | -16.1 | 0e+00 | 39/46 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.442×** | -15.4 | 0e+00 | 33/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.489×** | -13.5 | 1e-39 | 39/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.495×** | -13.3 | 2e-38 | 41/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -12.0 | 4e-31 | 36/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.266×** | -10.5 | 9e-24 | 37/47 (LS 180, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -8.1 | 2e-14 | 25/46 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -8.1 | 2e-14 | 31/47 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.652×** | -7.6 | 1e-12 | 29/47 (H4, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -7.4 | 9e-12 | 25/47 (SNU-423, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -7.2 | 2e-11 | 29/44 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -7.1 | 6e-11 | 22/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.788×** | -4.3 | 5e-04 | 15/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.2) |
| [[PANC-1 (line)]] | alt | 38.8 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -17.5) |
| [[H4 (line)]] | wt | 31.7 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.6) |
| [[KATO III (line)]] | alt | 33.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -19.0) |
| [[A498 (line)]] | wt | 27.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -30.8) |
| [[C32 (line)]] | wt | 27.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.8) |
| [[LoVo (line)]] | wt | 46.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -14.3) |
| [[LS 180 (line)]] | wt | 44.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -19.5) |
| [[SW 900 (line)]] | alt | 20.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0446× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 30.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -17.4) |
| [[HOP62 (line)]] | alt | 20.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.2) |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -10.0) |
| [[SW480 (line)]] | alt | 25.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -12.5) |
| [[A-172 (line)]] | wt | 30.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Silodosin (drug)]] 5 µM 0.169× (z -9.8) |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 41.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -19.2) |
| [[A549 (line)]] | wt | 21.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.5) |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0421× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 36.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.9) |
| [[COLO 205 (line)]] | alt | 44.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.7) |
| [[Hs 766T (line)]] | wt | 73.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.5) |
| [[NCI-H1792 (line)]] | alt | 24.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.1000× (z -11.9) |
| [[A-427 (line)]] | wt | 22.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.5) |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.8) |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.227× (z -10.1) |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.8) |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETHE1]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FLNB]] | +0.61 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[MINK1]] | +0.60 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[HPCAL1]] | +0.59 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[ATG16L1]] | +0.58 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[CPOX]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NIBAN2]] | +0.58 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[PLEK2]] | +0.57 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[LPCAT4]] | +0.57 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[MLX]] | +0.57 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[SLC35A1]] | +0.56 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC6]] | -0.59 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[FBXL19-AS1]] | -0.58 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[RUFY3]] | -0.57 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ACYP2]] | -0.55 | -0.51 / -0.32 | both halves | 2e-04 | STRING 668 |
| [[KANSL1L]] | -0.55 | -0.53 / -0.24 | both halves | 4e-04 |  |
| [[ATXN7]] | -0.54 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[HDAC2-AS2]] | -0.54 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[MTUS1-DT]] | -0.54 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[PATL2]] | -0.54 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[TM9SF5P]] | -0.54 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[GRIP1]] | -0.54 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[ZFX]] | -0.53 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT15]] | B | KRT15 activity raises STN1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without KRT15 | 0.065 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[LINC02320]] | B | LINC02320 activity raises STN1's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without LINC02320 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises STN1's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.41× lower at baseline in the lines without TNFRSF6B | 0.088 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.0, 7.0); signed map (-5.3, 45.6). **Vector** length 90.2, 21.5% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.0 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.5 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.5 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | -0.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.0 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.3 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -3.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | STN1 subunit of CST complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,856,806-103,918,332 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22559, bA541N10.2; previously OBFC1 |
| Gene groups (HGNC) | CST complex |
| Reactome | 7 pathways, smallest: Telomere C-strand synthesis initiation; Polymerase switching on the C-strand of the telomere; Telomere C-strand (Lagging Strand) Synthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H668](https://www.uniprot.org/uniprotkb/Q9H668) (CST complex subunit STN1):

> Component of the CST complex proposed to act as a specialized replication factor promoting DNA replication under conditions of replication stress or natural replication barriers such as the telomere duplex. The CST complex binds single-stranded DNA with high affinity in a sequence-independent manner, while isolated subunits bind DNA with low affinity by themselves. Initially the CST complex has been proposed to protect telomeres from DNA degradation. However, the CST complex has been shown to …

**Summary**, from NCBI Gene [79991](https://www.ncbi.nlm.nih.gov/gene/79991):

> OBFC1 and C17ORF68 (MIM 613129) are subunits of an alpha accessory factor (AAF) that stimulates the activity of DNA polymerase-alpha-primase (see MIM 176636), the enzyme that initiates DNA replication (Casteel et al., 2009 [PubMed 19119139]). OBFC1 also appears to function in a telomere-associated complex with C17ORF68 and TEN1 (C17ORF106; MIM 613130) (Miyake et al., 2009 [PubMed 19854130]).[supplied by OMIM, Nov 2009]

**Accessions** — [HGNC:26200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26200) · Entrez [79991](https://www.ncbi.nlm.nih.gov/gene/79991) · UniProt [Q9H668](https://www.uniprot.org/uniprotkb/Q9H668) · Ensembl [ENSG00000107960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107960)

## Data

Gene col 2906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2906); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2906]; `tensor/DDL_lfc|DDL_z.npy` [2906]; `embed/gene_vectors.npy` [2906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2906 or target_col == 2906). Every well: [[STN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
