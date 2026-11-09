---
symbol: "DNAJB11"
type: "gene"
col: 1626
ensembl_id: "ENSG00000090520"
name: "DnaJ heat shock protein family (Hsp40) member B11"
location: "3q27.3"
module: 42
arm: "+"
pooled_cpm: 69.61
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# DNAJB11

*DnaJ heat shock protein family (Hsp40) member B11* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.32× (z +11.4, q 2e-27, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.755× (z -5.5, q 2e-05, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.776× (z -5.0, q 2e-04, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.270×, KATO III 0.459×, AN3 CA 0.289×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.460×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYOU1]] (+0.82, fdr 7e-06), [[RPN1]] (+0.76, fdr 7e-06), [[PDIA3]] (+0.75, fdr 7e-06); moves opposite to [[NBPF14]] (-0.59, fdr 1e-05), [[CMTR2]] (-0.58, fdr 2e-05), [[LRCH3]] (-0.58, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +11.4 | 2e-27 | 44/48 (SW480, LOX-IMVI, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.27×** | +11.1 | 2e-26 | 38/48 (A549, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.09×** | +9.6 | 9e-20 | 31/41 (A-427, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.09×** | +9.3 | 2e-18 | 37/45 (C32, A-427, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.48×** | +8.9 | 7e-17 | 43/49 (PANC-1, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.85×** | +8.4 | 4e-15 | 41/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.76×** | +7.7 | 1e-12 | 37/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +7.7 | 1e-12 | 41/48 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.71×** | +7.3 | 2e-11 | 40/48 (PANC-1, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.70×** | +7.2 | 3e-11 | 40/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +6.7 | 1e-09 | 39/48 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.40×** | +6.5 | 5e-09 | 29/49 (SNU-423, A-172, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.63×** | +6.4 | 7e-09 | 39/47 (Panc 03.27, A-427, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +6.0 | 8e-08 | 41/48 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.53×** | +5.7 | 4e-07 | 33/48 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 2e-06 | 33/48 (PANC-1, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +4.6 | 1e-04 | 27/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 24/48 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1626.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.270×, KATO III 0.459×, AN3 CA 0.289×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.460×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.755×** | -5.5 | 2e-05 | 32/48 (A-427, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | **0.776×** | -5.0 | 2e-04 | 33/48 (A-172, HS-578T, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.007 | 24/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.773×** | -3.6 | 0.052 | 24/48 (J82, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 75.3 | 8 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.45× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 47.3 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[PANC-1 (line)]] | alt | 69.6 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +11.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.70× (z +8.7) | — |
| [[C32 (line)]] | wt | 43.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.43× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.42× (z +10.5) | — |
| [[A-427 (line)]] | wt | 95.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.99× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.460× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 37.8 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.83× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 33.2 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 47.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[J82 (line)]] | alt | 98.5 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 69.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.66× (z +8.6) | — |
| [[A549 (line)]] | wt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[Panc 03.27 (line)]] | alt | 84.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A498 (line)]] | wt | 68.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[AN3 CA (line)]] | alt | 75.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 65.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 63.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 110 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.13× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[KATO III (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 76.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.85× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 87.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 104 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYOU1]] | +0.82 | +0.78 / +0.80 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 976 |
| [[RPN1]] | +0.76 | +0.78 / +0.78 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 561 |
| [[PDIA3]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 817 |
| [[PDIA6]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 | pathway: IRE1alpha activates chaperones; STRING 959 |
| [[TMED7]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | STRING 746 |
| [[STT3A]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 443 |
| [[DNAJC3]] | +0.72 | +0.78 / +0.70 | both halves | 7e-06 | same gene group; pathway: Dengue Virus Genome Translation and Replication; STRING 831 |
| [[SEC61A1]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 | STRING 805 |
| [[PDIA4]] | +0.71 | +0.74 / +0.66 | both halves | 7e-06 | STRING 986 |
| [[TMED2]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SEL1L]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 | STRING 535 |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF14]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[CMTR2]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[LRCH3]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[NBPF10]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TMEM265]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NBPF19]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TMEM70]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[TRIM47]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SNHG11]] | -0.55 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[RPP25L]] | -0.55 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[COIL]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[FNTA]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.8, -22.6); signed map (-55.5, 6.9). **Vector** length 112, 35.8% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.53 to 23); *Cargo concentration in the ER* (reactome, mean cos +0.58 to 7); *N-glycan trimming in the ER and Calnexin/Calreticulin cycle* (reactome, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +7.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +7.6 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +7.0 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.7 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.5 | -0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.6 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.3 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:186,567,403-186,585,800 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EDJ, HEDJ, ERdj3 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Reactome | 9 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Maturation of DENV proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBS4](https://www.uniprot.org/uniprotkb/Q9UBS4) (DnaJ homolog subfamily B member 11):

> As a co-chaperone for HSPA5 it is required for proper folding, trafficking or degradation of proteins. Binds directly to both unfolded proteins that are substrates for ERAD and nascent unfolded peptide chains, but dissociates from the HSPA5-unfolded protein complex before folding is completed. May help recruiting HSPA5 and other chaperones to the substrate. Stimulates HSPA5 ATPase activity. It is necessary for maturation and correct trafficking of PKD1.

**Summary**, from NCBI Gene [51726](https://www.ncbi.nlm.nih.gov/gene/51726):

> This gene encodes a soluble glycoprotein of the endoplasmic reticulum (ER) lumen that functions as a co-chaperone of binding immunoglobulin protein, a 70 kilodalton heat shock protein chaperone required for the proper folding and assembly of proteins in the ER. The encoded protein contains a highly conserved J domain of about 70 amino acids with a characteristic His-Pro-Asp (HPD) motif and may regulate the activity of binding immunoglobulin protein by stimulating ATPase activity. [provided by …

**Accessions** — [HGNC:14889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14889) · Entrez [51726](https://www.ncbi.nlm.nih.gov/gene/51726) · UniProt [Q9UBS4](https://www.uniprot.org/uniprotkb/Q9UBS4) · Ensembl [ENSG00000090520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090520)

## Data

Gene col 1626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1626); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1626]; `tensor/DDL_lfc|DDL_z.npy` [1626]; `embed/gene_vectors.npy` [1626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1626 or target_col == 1626). Every well: [[DNAJB11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
