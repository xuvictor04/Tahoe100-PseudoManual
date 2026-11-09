---
symbol: "TRMT44"
type: "gene"
col: 7882
ensembl_id: "ENSG00000155275"
name: "tRNA methyltransferase 44 homolog"
location: "4p16.1"
module: 210
arm: "+"
pooled_cpm: 28.09
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# TRMT44

*tRNA methyltransferase 44 homolog* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.76× (z +11.4, q 2e-27, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.455× (z -12.5, q 4e-33, down in 26 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.747× (z -6.8, q 1e-09, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SNU-423 0.0455×, HEC-1-A 0.182×, KATO III 0.113×, SK-MEL-2 0.127×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.0600×, J82 0.238×, HOP62 0.222×, NCI-H1573 0.217×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.128×, LS 180 0.181×, Panc 03.27 0.212×, NCI-H2030 0.227×; ⚠ toxic; transcription drop); [[Relugolix (drug)]] 5 µM in 1 line (NCI-H2122 0.215×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0720×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0815×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP214]] (+0.68, fdr 1e-05), [[GAR1]] (+0.66, fdr 7e-06), [[ACOX3]] (+0.65, fdr 1e-05, ⚠ same locus), [[PMM2]] (+0.65, fdr 7e-06); moves opposite to [[MED13L]] (-0.56, fdr 2e-05), [[HYCC1]] (-0.55, fdr 5e-05), [[ENPP1]] (-0.55, fdr 7e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.76×** | +11.4 | 2e-27 | 44/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +8.2 | 1e-13 | 37/46 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +7.8 | 6e-13 | 39/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +7.8 | 6e-13 | 41/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.4 | 2e-11 | 33/47 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +7.3 | 3e-11 | 31/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.2 | 7e-11 | 34/48 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.6 | 1e-06 | 25/47 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.6 | 2e-06 | 30/48 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.5 | 2e-06 | 30/48 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.5 | 2e-06 | 28/47 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 1e-05 | 26/46 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.3 | 0.038 | 15/42 (A-172, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7882.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SNU-423 0.0455×, HEC-1-A 0.182×, KATO III 0.113×, SK-MEL-2 0.127×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.0600×, J82 0.238×, HOP62 0.222×, NCI-H1573 0.217×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.128×, LS 180 0.181×, Panc 03.27 0.212×, NCI-H2030 0.227×; ⚠ toxic; transcription drop); [[Relugolix (drug)]] 5 µM in 1 line (NCI-H2122 0.215×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0720×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0815×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -12.5 | 4e-33 | 26/37 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.554×** | -9.7 | 5e-20 | 35/44 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -9.2 | 1e-17 | 26/42 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -6.8 | 1e-09 | 33/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.746×** | -4.8 | 2e-04 | 24/47 (LS 180, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Thymol (drug)]] 5 µM |  | 0.863× | -3.4 | 0.051 | 12/48 (HEC-1-A, LoVo, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.813×** | -3.4 | 0.051 | 16/45 (HepG2/C3A, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.828× | -3.0 | 0.19 | 12/47 (J82, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -12.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -15.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.351× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 33.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 35.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0455× (z -22.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0678× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 40.3 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0815× (z -11.3) |
| [[H4 (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -15.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -11.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0720× (z -11.6) |
| [[LoVo (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0600× (z -21.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 1 | — | [[Relugolix (drug)]] 5 µM 0.215× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.331× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -12.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP214]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 | pathway: tRNA processing |
| [[GAR1]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ACOX3]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PMM2]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[AAR2]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[DDX49]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ZNF787]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[YRDC]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 | pathway: tRNA processing |
| [[GTF3C2]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[DRG1]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DDX51]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[TRMT1]] | +0.61 | +0.54 / +0.70 | both halves | 1e-05 | same gene group; pathway: tRNA modification in the nucleus and cytosol; STRING 531 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13L]] | -0.56 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[HYCC1]] | -0.55 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ENPP1]] | -0.55 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[PTBP3]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ITGAV]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[RFK]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[PEAK1]] | -0.53 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PDLIM3]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[PLEKHA5]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.5, -9.1); signed map (-14.5, -22.0). **Vector** length 73.2, 13.9% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.1 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | +5.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.1 | -9.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 44 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:8,436,140-8,493,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35725, TRM44; previously C4orf23, METTL19 |
| Gene groups (HGNC) | 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYL2](https://www.uniprot.org/uniprotkb/Q8IYL2) (Probable tRNA):

> Probable adenosyl-L-methionine (AdoMet)-dependent tRNA (uracil-O(2)-)-methyltransferase.

**Summary**, from NCBI Gene [152992](https://www.ncbi.nlm.nih.gov/gene/152992):

> The protein encoded by this gene is a putative tRNA methyltransferase found in the cytoplasm. Defects in this gene may be a cause of partial epilepsy with pericentral spikes (PEPS), but that has not been proven definitively. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:26653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26653) · Entrez [152992](https://www.ncbi.nlm.nih.gov/gene/152992) · UniProt [Q8IYL2](https://www.uniprot.org/uniprotkb/Q8IYL2) · Ensembl [ENSG00000155275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155275)

## Data

Gene col 7882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7882); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7882]; `tensor/DDL_lfc|DDL_z.npy` [7882]; `embed/gene_vectors.npy` [7882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7882 or target_col == 7882). Every well: [[TRMT44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
