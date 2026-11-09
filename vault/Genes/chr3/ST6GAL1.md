---
symbol: "ST6GAL1"
type: "gene"
col: 1063
ensembl_id: "ENSG00000073849"
name: "ST6 beta-galactoside alpha-2,6-sialyltransferase 1"
location: "3q27.3"
module: 18
arm: "+"
pooled_cpm: 37.15
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 43
n_dd_up_clean: 4
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ST6GAL1

*ST6 beta-galactoside alpha-2,6-sialyltransferase 1* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +4.8, q 8e-04, up in 13 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.189× (z -38.1, q 0e+00, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASGEF1C]] (+0.60, fdr 7e-06), [[PTPRZ1]] (+0.60, fdr 3e-05), [[ZNF704]] (+0.54, fdr 1e-05); moves opposite to [[CA9]] (-0.44, fdr 9e-05), [[SEC23B]] (-0.42, fdr 1e-04), [[RAB3GAP2]] (-0.42, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[B4GALNT4]] → it (grade B ⚠); 11 go from it, the strongest it → [[PCSK6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.8 | 8e-04 | 13/34 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.29×** | +4.1 | 0.008 | 9/34 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.008 | 8/34 (A-427, COLO 205, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.33×** | +3.9 | 0.012 | 12/34 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.018 | 6/33 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.189×** | -38.1 | 0e+00 | 32/34 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.189×** | -25.9 | 0e+00 | 34/34 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.280×** | -20.6 | 0e+00 | 34/34 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.284×** | -20.3 | 0e+00 | 30/34 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.367×** | -16.2 | 0e+00 | 30/32 (HepG2/C3A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.389×** | -15.2 | 0e+00 | 29/34 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.406×** | -14.5 | 0e+00 | 24/34 (HepG2/C3A, A-172, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.411×** | -14.4 | 7e-45 | 27/33 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.433×** | -13.5 | 1e-39 | 25/34 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.485×** | -11.7 | 1e-29 | 24/34 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.498×** | -11.2 | 2e-27 | 22/34 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.564×** | -9.2 | 1e-18 | 24/34 (LoVo, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.584×** | -8.7 | 2e-16 | 23/33 (HepG2/C3A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -8.5 | 8e-16 | 24/34 (A-427, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -8.5 | 9e-16 | 22/34 (SK-MEL-2, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -7.1 | 4e-11 | 22/34 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.546×** | -7.0 | 1e-10 | 25/34 (A-427, SW1417, …) | two highest doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.502×** | -5.8 | 2e-07 | 18/34 (SK-MEL-2, SW1417, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.699×** | -5.4 | 1e-06 | 19/34 (RKO, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 306 | 0 | 23 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0490× (z -35.8) |
| [[A-427 (line)]] | wt | 125 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0696× (z -39.3) |
| [[BT-474 (line)]] | alt | 120 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -21.0) |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -35.6) |
| [[SK-MEL-2 (line)]] | alt | 235 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0463× (z -43.7) |
| [[A-172 (line)]] | wt | 73.2 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0942× (z -35.1) |
| [[RKO (line)]] | wt | 78.6 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0392× (z -26.6) |
| [[NCI-H460 (line)]] | wt | 38.9 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -29.5) |
| [[SW480 (line)]] | alt | 37.7 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -24.8) |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -29.5) |
| [[LoVo (line)]] | wt | 44.1 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.2) |
| [[SW1417 (line)]] | alt | 81.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -23.6) |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -14.1) |
| [[LS 180 (line)]] | wt | 39.5 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0576× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.2) |
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0403× (z -19.2) |
| [[AN3 CA (line)]] | alt | 86.6 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.0820× (z -12.6) |
| [[H4 (line)]] | wt | 16.5 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0379× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -15.4) |
| [[A549 (line)]] | wt | 18.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.6) |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0827× (z -24.0) |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0760× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.166× (z -10.6) |
| [[A498 (line)]] | wt | 10.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0856× (z -15.0) |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0648× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.9) |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.99 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASGEF1C]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PTPRZ1]] | +0.60 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ZNF704]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LEF1]] | +0.54 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[TFAP4]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TMTC4]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[LINC01205]] | +0.52 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[PDE3B]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[LDLRAD3]] | +0.51 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[HS6ST2]] | +0.50 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TULP4]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[STOX2]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA9]] | -0.44 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[SEC23B]] | -0.42 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[RAB3GAP2]] | -0.42 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[C6orf89]] | -0.41 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[SENP2]] | -0.41 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[TRIQK]] | -0.41 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT4]] | B | B4GALNT4 activity strengthens ST6GAL1's drug response | lines that do not express B4GALNT4 (6) vs lines expressing it (28) | the lines without B4GALNT4 respond 0.43× as strongly (z diff +3.70); strongest at Homoharringtonine 0.5 µM: 0.68x vs 0.16x (z diff +6.1) | 0.002 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; target measured in part of the lines; artifact flags |
| [[PCSK6]] | B | PCSK6 activity raises ST6GAL1's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 2.42× lower at baseline in the lines without PCSK6 | 0.011 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[CMTM8]] | B | CMTM8 activity raises ST6GAL1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.94× lower at baseline in the lines without CMTM8 | 0.026 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[WNK2]] | B | WNK2 activity raises ST6GAL1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without WNK2 | 0.029 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[SNX10]] | B | SNX10 activity raises ST6GAL1's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without SNX10 | 0.073 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[RASGEF1C]] | B | RASGEF1C activity raises ST6GAL1's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without RASGEF1C | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[GLDC]] | B | GLDC activity raises ST6GAL1's level | lines that do not express GLDC (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without GLDC | 0.090 | ⚠ within organs, on part of the lines; also absent: PRAME, LRRC63, ZFP82; maybe low, not absent |
| [[PRTG]] | B | PRTG activity raises ST6GAL1's level | lines that do not express PRTG (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without PRTG | 0.091 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[B4GALNT4]] | C | B4GALNT4 activity raises ST6GAL1's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 4.34× lower at baseline in the lines without B4GALNT4 | 0.004 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK6]] | B | ST6GAL1 activity raises PCSK6's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without ST6GAL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[SNX10]] | B | ST6GAL1 activity raises SNX10's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 2.85× lower at baseline in the lines without ST6GAL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[RASGEF1C]] | B | ST6GAL1 activity raises RASGEF1C's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without ST6GAL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[ZNF704]] | B | ST6GAL1 activity raises ZNF704's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without ST6GAL1 | 0.037 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[APBA2]] | B | ST6GAL1 activity strengthens APBA2's drug response | lines that do not express ST6GAL1 (8) vs lines expressing it (22) | the lines without ST6GAL1 respond 0.63× as strongly (z diff +3.05); strongest at Digitoxin 5 µM: 0.77x vs 0.45x (z diff +4.2) | 0.042 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PRTG]] | B | ST6GAL1 activity raises PRTG's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without ST6GAL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[CMTM8]] | B | ST6GAL1 activity raises CMTM8's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.88× lower at baseline in the lines without ST6GAL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 5 µM | B | ST6GAL1 activity raises the cells' numbers under Digitoxin 5 µM (protects the cells) | lines that do not express ST6GAL1 (14) vs lines expressing it (34) | the lines without ST6GAL1: 0.77× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[SEC23B]] | B | ST6GAL1 activity lowers SEC23B's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.21× higher at baseline in the lines without ST6GAL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[GLDC]] | B | ST6GAL1 activity raises GLDC's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without ST6GAL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[B4GALNT4]] | C | ST6GAL1 activity raises B4GALNT4's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 3.75× lower at baseline in the lines without ST6GAL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (5.3, 43.0); signed map (27.9, 37.6). **Vector** length 92.7, 24.3% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +4.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.2 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.1 | -7.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -25.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -20.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ST6 beta-galactoside alpha-2,6-sialyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:186,930,325-187,078,553 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDw75; previously SIAT1 |
| Gene groups (HGNC) | Sialyltransferases |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 20 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; N-Glycan antennae elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P15907](https://www.uniprot.org/uniprotkb/P15907) (Beta-galactoside alpha-2,6-sialyltransferase 1):

> Transfers sialic acid from CMP-sialic acid to galactose-containing acceptor substrates. In B lymphocytes, generates neuraminidase-sensitive lymphocyte cell-surface differentiation antigens, such as CDw75, HB-6 and CD76. Sialylates complex-type N-glycans attached on the fragment crystallizable (Fc) of IgGs conferring anti-inflammatory effector functions. Preferentially monosialylates the alpha(1->3) mannose antenna of Fc glycoforms with subsequent disialylation occurring at a much slower rate.

**Summary**, from NCBI Gene [6480](https://www.ncbi.nlm.nih.gov/gene/6480):

> This gene encodes a member of glycosyltransferase family 29. The encoded protein is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to galactose-containing substrates. The protein, which is normally found in the Golgi but can be proteolytically processed to a soluble form, is involved in the generation of the cell-surface carbohydrate determinants and differentiation antigens HB-6, CD75, and CD76. This gene has been incorrectly referred to as CD75. …

**Accessions** — [HGNC:10860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10860) · Entrez [6480](https://www.ncbi.nlm.nih.gov/gene/6480) · UniProt [P15907](https://www.uniprot.org/uniprotkb/P15907) · Ensembl [ENSG00000073849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073849)

## Data

Gene col 1063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1063); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1063]; `tensor/DDL_lfc|DDL_z.npy` [1063]; `embed/gene_vectors.npy` [1063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1063 or target_col == 1063). Every well: [[ST6GAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
