---
symbol: "ZZEF1"
type: "gene"
col: 1091
ensembl_id: "ENSG00000074755"
name: "zinc finger ZZ-type and EF-hand domain containing 1"
location: "17p13.2"
module: 41
arm: "+"
pooled_cpm: 90.71
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ZZEF1

*zinc finger ZZ-type and EF-hand domain containing 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.05× (z +19.9, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.533× (z -10.7, q 7e-24, down in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.735× (z -8.0, q 1e-13, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMDN3]] (+0.58, fdr 1e-05), [[ZNF324]] (+0.56, fdr 2e-05), [[EMC7]] (+0.55, fdr 1e-05); moves opposite to [[CHRNA5]] (-0.56, fdr 1e-05), [[GNPNAT1]] (-0.52, fdr 1e-05), [[GPR63]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.05×** | +19.9 | 0e+00 | 47/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.28×** | +13.9 | 2e-41 | 47/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +10.8 | 8e-25 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +8.1 | 6e-14 | 42/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +7.7 | 2e-12 | 42/48 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +6.5 | 7e-09 | 40/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.81×** | +5.7 | 1e-06 | 42/49 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +5.3 | 6e-06 | 27/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +4.2 | 0.002 | 22/49 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 24/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.010 | 20/48 (PANC-1, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.061 | 18/49 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.061 | 20/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +3.0 | 0.095 | 16/50 (LoVo, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.533×** | -10.7 | 7e-24 | 40/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.580×** | -10.0 | 4e-21 | 39/49 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -8.8 | 3e-16 | 33/43 (SW48, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -8.0 | 1e-13 | 39/48 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -7.3 | 3e-11 | 35/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.677×** | -7.2 | 7e-11 | 42/49 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.814×** | -3.8 | 0.010 | 23/48 (Hs 766T, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **0.808×** | -3.8 | 0.010 | 26/47 (AsPC-1, RPMI-7951, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.820×** | -3.7 | 0.015 | 21/48 (LOX-IMVI, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -3.0 | 0.15 | 10/48 (HS-578T, HEC-1-A, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 82.1 | 6 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.4× (z +15.9) | [[Auranofin (drug)]] 5 µM 0.332× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 94.4 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +23.5) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -13.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 124 | 5 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.3× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -12.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 83.8 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.7× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -17.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 109 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 82.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 89.2 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.04× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 112 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.25× (z +12.3) | — |
| [[A-427 (line)]] | wt | 82.5 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.46× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -22.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 159 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -10.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 84.6 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.58× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 68.1 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.7× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -9.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 84.4 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.6× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 109 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.10× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0766× (z -29.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 65.4 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.91× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.347× (z -11.0) |
| [[BT-474 (line)]] | alt | 72.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 8.80× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 103 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 30.9× (z +14.7) | — |
| [[HS-578T (line)]] | alt | 119 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.83× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 93.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -12.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 125 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 63.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.48× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 78.5 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.21× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.572× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 71.4 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.8× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 144 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.88× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -14.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 69.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 58.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 93.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.70× (z +10.4) | — |
| [[LoVo (line)]] | wt | 103 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 72.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +10.4) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.104× (z -10.0) ⚠ toxic |
| [[A549 (line)]] | wt | 135 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.40× (z +13.0) | — |
| [[C-33 A (line)]] | alt | 83.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.9× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 44.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.20× (z +10.4) | — |
| [[H4 (line)]] | wt | 55.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 91.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.43× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 73.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 98.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.24× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 49.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.96× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 92.5 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.215× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 77.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.19× (z +8.6) | — |
| [[SW48 (line)]] | wt | 79.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMDN3]] | +0.58 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[EMC7]] | +0.55 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TMEM175]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ZSWIM8]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 | STRING 582 |
| [[ALDH6A1]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[BBOF1]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[RSPRY1]] | +0.53 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[TM9SF1]] | +0.52 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PRPF18]] | +0.52 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[MMUT]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TBC1D10B]] | +0.51 | +0.35 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRNA5]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GNPNAT1]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[GPR63]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PAQR3]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ULBP3]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[GLO1]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CACNB4]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SNX10]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[GLS]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[BTNL9]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[TEX10]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[FAM171B]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.2, -9.7); signed map (-8.9, -3.2). **Vector** length 95.7, 27.5% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.6 | +19.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.4 | +13.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +2.8 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +8.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.9 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.3 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.2 | -7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.2 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.7 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -1.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger ZZ-type and EF-hand domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,004,445-4,143,030 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0399, ZZZ4, FLJ10821 |
| Gene groups (HGNC) | Zinc fingers ZZ-type; EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43149](https://www.uniprot.org/uniprotkb/O43149) (Zinc finger ZZ-type and EF-hand domain-containing protein 1):

> Histone H3 reader which may act as a transcriptional coactivator for KLF6 and KLF9 transcription factors.

**Summary**, from NCBI Gene [23140](https://www.ncbi.nlm.nih.gov/gene/23140):

> Enables histone binding activity. Predicted to be involved in DNA-templated transcription. Predicted to act upstream of or within several processes, including glutamatergic synaptic transmission; regulation of peptidyl-tyrosine phosphorylation; and visual learning. Predicted to be located in cell surface; postsynapse; and presynaptic active zone. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29027) · Entrez [23140](https://www.ncbi.nlm.nih.gov/gene/23140) · UniProt [O43149](https://www.uniprot.org/uniprotkb/O43149) · Ensembl [ENSG00000074755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074755)

## Data

Gene col 1091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1091); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1091]; `tensor/DDL_lfc|DDL_z.npy` [1091]; `embed/gene_vectors.npy` [1091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1091 or target_col == 1091). Every well: [[ZZEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZZEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
