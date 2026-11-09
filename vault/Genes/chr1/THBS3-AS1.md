---
symbol: "THBS3-AS1"
type: "gene"
col: 13776
ensembl_id: "ENSG00000231064"
name: "THBS3 antisense RNA 1"
location: "1q22"
module: 139
arm: "+"
pooled_cpm: 3.11
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# THBS3-AS1

*THBS3 antisense RNA 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 0.05 µM: 1.46× (z +4.4, q 0.004, up in 11 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.506× (z -5.7, q 3e-06, down in 12 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 0.493× (z -5.7, q 3e-06, down in 17 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC1]] (+0.54, fdr 3e-05, ⚠ same locus), [[AK7]] (+0.54, fdr 1e-05), [[LY6E-DT]] (+0.52, fdr 3e-05), [[FGG]] (+0.52, fdr 5e-05); moves opposite to [[FEZ2]] (-0.48, fdr 4e-05), [[CSGALNACT2]] (-0.46, fdr 8e-05), [[DENR]] (-0.45, fdr 4e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[AQP3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.05 µM |  | **1.46×** | +4.4 | 0.004 | 11/40 (AsPC-1, SHP-77, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.3 | 0.004 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 0.004 | 10/40 (NCI-H2030, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.005 | 9/39 (LOX-IMVI, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.007 | 9/38 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.8 | 0.016 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.062 | 5/40 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.064 | 8/42 (LoVo, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -5.7 | 3e-06 | 12/24 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.493×** | -5.7 | 3e-06 | 17/41 (AsPC-1, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.511×** | -5.7 | 3e-06 | 18/32 (Hs 766T, SHP-77, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.499×** | -5.4 | 1e-05 | 18/38 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.530×** | -5.3 | 1e-05 | 23/43 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.542×** | -5.2 | 2e-05 | 18/40 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.554×** | -4.7 | 2e-04 | 17/36 (SNU-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -4.5 | 5e-04 | 11/22 (KATO III, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.708×** | -4.1 | 0.002 | 18/41 (KATO III, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.610×** | -3.8 | 0.008 | 14/37 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -3.6 | 0.019 | 12/41 (SNU-1, A-427, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.681×** | -3.2 | 0.052 | 7/43 (NCI-H2030, H4, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.665×** | -3.2 | 0.052 | 6/40 (SHP-77, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.692×** | -3.1 | 0.078 | 9/30 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.674×** | -3.0 | 0.088 | 14/39 (NCI-H460, SNU-423, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 5.01 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0491× (z -10.0) |
| [[A498 (line)]] | wt | 3.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0584× (z -11.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 3.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0326× (z -15.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 1.83 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0678× (z -8.7) |
| [[A-172 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.876 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.964 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC1]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 | ⚠ same locus (2.1 kb: neighbours can correlate without regulation) |
| [[AK7]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LY6E-DT]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[FGG]] | +0.52 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[FGA]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SECTM1]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[STOM]] | +0.51 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[B4GALT1]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[TIPARP]] | +0.48 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[NFKBIA]] | +0.47 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[IRF1]] | +0.47 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SAA2]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[NNMT]] | +0.47 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEZ2]] | -0.48 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[CSGALNACT2]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[DENR]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TMEM158]] | -0.43 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[BCLAF3]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[SLC30A6]] | -0.42 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[TAF12]] | -0.40 | -0.22 / -0.34 | both halves | 6e-04 |  |
| [[SIKE1]] | -0.40 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[TM4SF19]] | -0.40 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[CCDC82]] | -0.40 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[MRPL52]] | -0.40 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[NRIP3]] | -0.40 | -0.35 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers THBS3-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds |
| [[ETS2]] | B | ETS2 activity lowers THBS3-AS1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.84× higher at baseline in the lines without ETS2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[AQP3]] | B | AQP3 activity lowers THBS3-AS1's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 1.43× higher at baseline in the lines without AQP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers THBS3-AS1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[CFH]] | B | CFH activity lowers THBS3-AS1's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.12× higher at baseline in the lines without CFH | 0.080 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[ROS1]] | B | ROS1 activity weakens THBS3-AS1's drug response | lines that do not express ROS1 (26) vs lines expressing it (17) | the lines without ROS1 respond 2.08× as strongly (z diff -1.14); strongest at Niclosamide (olamine) 5 µM: 0.29x vs 0.93x (z diff -3.3) | 0.091 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity weakens THBS3-AS1's drug response | lines that do not express TM4SF19, TM4SF19-DYNLT2B (18) vs lines expressing them (25) | the lines without TM4SF19, TM4SF19-DYNLT2B respond 1.49× as strongly (z diff -0.99); strongest at Niclosamide (olamine) 5 µM: 0.17x vs 0.72x (z diff -4.6) | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; target measured in part of the lines; artifact flags; co-absent genes |
| [[SOD2]] | C | SOD2 activity lowers THBS3-AS1's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 2.97× higher at baseline in the lines without SOD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | C | THBS3-AS1 activity lowers AQP3's level | lines that do not express THBS3-AS1 (3) vs lines expressing it (47) | 5.08× higher at baseline in the lines without THBS3-AS1 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: EFCAB6, ITGA2B, CYP46A1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 48.0); signed map (54.7, -3.3). **Vector** length 45.4, 5.67% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +4.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.5 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | THBS3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q22 — chr1:155,194,996-155,205,495 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40582) · Entrez [105371450](https://www.ncbi.nlm.nih.gov/gene/105371450) · Ensembl [ENSG00000231064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231064)

## Data

Gene col 13776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13776); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13776]; `tensor/DDL_lfc|DDL_z.npy` [13776]; `embed/gene_vectors.npy` [13776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13776 or target_col == 13776). Every well: [[THBS3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBS3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
