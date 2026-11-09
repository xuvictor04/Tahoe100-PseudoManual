---
symbol: "PLIN3"
type: "gene"
col: 2587
ensembl_id: "ENSG00000105355"
name: "perilipin 3"
location: "19p13.3"
module: 192
arm: "+"
pooled_cpm: 84.35
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# PLIN3

*perilipin 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +5.1, q 2e-04, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -10.6, q 3e-23, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTN2]] (+0.72, fdr 7e-06), [[FAM89B]] (+0.72, fdr 7e-06), [[POLD4]] (+0.69, fdr 1e-05); moves opposite to [[NNT]] (-0.69, fdr 1e-05), [[MCCC2]] (-0.69, fdr 7e-06), [[ILF3]] (-0.68, fdr 7e-06).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LGALS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.1 | 2e-04 | 37/47 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.047 | 22/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.047 | 25/44 (LS 180, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.047 | 30/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.548×** | -10.6 | 3e-23 | 39/47 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.531×** | -7.5 | 1e-11 | 28/39 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.572×** | -6.4 | 3e-08 | 27/41 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -5.7 | 2e-06 | 35/47 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -5.2 | 3e-05 | 35/47 (MIA PaCa-2, A498, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -4.9 | 1e-04 | 30/48 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.757×** | -4.8 | 1e-04 | 28/47 (AsPC-1, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.783×** | -4.2 | 0.001 | 33/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.783×** | -4.2 | 0.001 | 37/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.701×** | -4.1 | 0.002 | 25/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -4.0 | 0.004 | 24/46 (A498, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.729×** | -3.9 | 0.005 | 29/47 (AsPC-1, BT-474, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.741×** | -3.7 | 0.010 | 32/47 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.755×** | -3.5 | 0.022 | 24/46 (SNU-1, LOX-IMVI, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -3.4 | 0.025 | 27/47 (HEC-1-A, SW480, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.026 | 25/47 (AsPC-1, HCT15, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.026 | 26/47 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.031 | 25/47 (HOP62, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.781×** | -3.0 | 0.065 | 24/47 (HOP62, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 138 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.15× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.9) |
| [[HOP62 (line)]] | alt | 80.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.2) |
| [[HS-578T (line)]] | alt | 115 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -13.3) |
| [[HCT15 (line)]] | alt | 174 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 74.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.6) |
| [[LoVo (line)]] | wt | 53.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.4) |
| [[LS 180 (line)]] | wt | 51.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 104 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -14.0) |
| [[A-172 (line)]] | wt | 155 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.1) |
| [[A-427 (line)]] | wt | 46.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -8.6) |
| [[A498 (line)]] | wt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -9.6) |
| [[BT-474 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 91.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.8) |
| [[KATO III (line)]] | alt | 39.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 82.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.152× (z -8.6) ⚠ toxic |
| [[RKO (line)]] | wt | 79.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -13.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.6) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -15.4) |
| [[SW 900 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN2]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[FAM89B]] | +0.72 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[POLD4]] | +0.69 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 | STRING 447 |
| [[GIPR]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.66 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MIDN]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[CIB1]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | -0.69 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[MCCC2]] | -0.69 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ILF3]] | -0.68 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[FUBP1]] | -0.68 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.67 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SNX5]] | -0.66 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[CNOT1]] | -0.66 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[EIF2D]] | -0.64 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[MBNL3]] | -0.64 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[U2AF2]] | -0.62 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[SRSF1]] | -0.62 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ADI1]] | -0.61 | -0.60 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS1]] | B | LGALS1 activity raises PLIN3's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.12× lower at baseline in the lines without LGALS1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[TUBB6]] | B | TUBB6 activity raises PLIN3's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without TUBB6 | 0.011 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[SLC16A3]] | B | SLC16A3 activity raises PLIN3's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without SLC16A3 | 0.047 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[GALC]] | B | GALC activity raises PLIN3's level | lines that do not express GALC (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without GALC | 0.048 | ⚠ within organs, on part of the lines; also absent: HERC5, TNFRSF1B, ZNF354C |
| [[A4GALT]] | B | A4GALT activity raises PLIN3's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without A4GALT | 0.049 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[DENND2C]] | B | DENND2C activity raises PLIN3's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.66× lower at baseline in the lines without DENND2C | 0.069 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[LRRC8E]] | B | LRRC8E activity raises PLIN3's level | lines that do not express LRRC8E (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without LRRC8E | 0.089 | ⚠ within organs, on part of the lines; also absent: ITPR3, SQOR, BIRC3; its own permutation p |
| [[TIMP1]] | C | TIMP1 activity raises PLIN3's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.886). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.3, 1.8); signed map (-22.9, 20.8). **Vector** length 142, 47.6% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.1 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.0 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.4 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.3 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | perilipin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,838,341-4,867,694 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIP47, PP17; previously M6PRBP1 |
| Gene groups (HGNC) | Perilipins |
| Reactome | 15 pathways, smallest: Lipophagy; RHOBTB3 ATPase cycle; Triglyceride catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60664](https://www.uniprot.org/uniprotkb/O60664) (Perilipin-3):

> Structural component of lipid droplets, which is required for the formation and maintenance of lipid storage droplets. Required for the transport of mannose 6-phosphate receptors (MPR) from endosomes to the trans-Golgi network.

**Summary**, from NCBI Gene [10226](https://www.ncbi.nlm.nih.gov/gene/10226):

> Mannose 6-phophate receptors (MPRs) deliver lysosomal hydrolase from the Golgi to endosomes and then return to the Golgi complex. The protein encoded by this gene interacts with the cytoplasmic domains of both cation-independent and cation-dependent MPRs, and is required for endosome-to-Golgi transport. This protein also binds directly to the GTPase RAB9 (RAB9A), a member of the RAS oncogene family. The interaction with RAB9 has been shown to increase the affinity of this protein for its cargo. …

**Accessions** — [HGNC:16893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16893) · Entrez [10226](https://www.ncbi.nlm.nih.gov/gene/10226) · UniProt [O60664](https://www.uniprot.org/uniprotkb/O60664) · Ensembl [ENSG00000105355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105355)

## Data

Gene col 2587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2587); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2587]; `tensor/DDL_lfc|DDL_z.npy` [2587]; `embed/gene_vectors.npy` [2587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2587 or target_col == 2587). Every well: [[PLIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
