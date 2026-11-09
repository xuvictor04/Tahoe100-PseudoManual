---
symbol: "GRK6"
type: "gene"
col: 12521
ensembl_id: "ENSG00000198055"
name: "G protein-coupled receptor kinase 6"
location: "5q35.3"
module: 2
arm: "+"
pooled_cpm: 19.53
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GRK6

*G protein-coupled receptor kinase 6* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.50× (z +16.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.669× (z -10.1, q 2e-21, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.572× (z -9.6, q 3e-19, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO7]] (+0.68, fdr 1e-05), [[TCF3]] (+0.68, fdr 1e-05), [[ODF2]] (+0.67, fdr 7e-06); moves opposite to [[HIKESHI]] (-0.66, fdr 1e-04), [[FUNDC1]] (-0.64, fdr 1e-05), [[PEX12]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +16.3 | 0e+00 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +14.6 | 1e-45 | 45/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +12.6 | 4e-34 | 43/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.71×** | +9.2 | 6e-18 | 22/30 (Panc 03.27, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.55×** | +7.8 | 8e-13 | 27/41 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.4 | 1e-11 | 25/46 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.45×** | +6.1 | 8e-08 | 18/35 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.36×** | +5.5 | 3e-06 | 18/42 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 4e-05 | 21/47 (SK-MEL-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.29×** | +4.6 | 3e-04 | 19/47 (NCI-H460, BT-474, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +4.3 | 9e-04 | 14/48 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +4.1 | 0.002 | 15/47 (BT-474, NCI-H460, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.23×** | +3.7 | 0.010 | 17/48 (NCI-H460, SW480, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.22×** | +3.6 | 0.015 | 16/46 (SW480, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.669×** | -10.1 | 2e-21 | 38/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.572×** | -9.6 | 3e-19 | 28/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.696×** | -9.2 | 1e-17 | 29/46 (HT-29, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -7.9 | 4e-13 | 26/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -6.9 | 7e-10 | 30/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.683×** | -6.8 | 1e-09 | 28/48 (Hs 766T, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -5.3 | 1e-05 | 21/48 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -5.0 | 3e-05 | 20/44 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -4.9 | 7e-05 | 22/47 (A498, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.753×** | -4.9 | 7e-05 | 21/46 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -3.9 | 0.005 | 15/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.008 | 10/47 (RKO, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.814×** | -3.7 | 0.010 | 16/48 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.832×** | -3.3 | 0.041 | 15/47 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.051 | 11/47 (SW480, C32, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.828×** | -3.2 | 0.052 | 14/47 (SW480, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -3.1 | 0.062 | 9/48 (LS 180, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.886× | -3.0 | 0.062 | 11/48 (CHP-212, SW480, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.062 | 11/47 (H4, LOX-IMVI, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.6 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 33.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.02× (z +9.0) | — |
| [[KATO III (line)]] | alt | 14.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.74× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.29× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 17.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.59× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 9.31 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0662× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0750× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.230× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO7]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TCF3]] | +0.68 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ODF2]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CHTF18]] | +0.67 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CEP131]] | +0.63 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[FARP2]] | +0.63 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[POC1A]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MAPKAPK2]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[FAM118A]] | +0.62 | +0.70 / +0.23 | both halves | 5e-04 |  |
| [[NPHP4]] | +0.62 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[AP2A1]] | +0.62 | +0.56 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIKESHI]] | -0.66 | -0.71 / -0.33 | both halves | 1e-04 |  |
| [[FUNDC1]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[PEX12]] | -0.64 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.61 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[TCEAL1]] | -0.61 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[RAD52]] | -0.60 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[UBQLN2]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PIGP]] | -0.59 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[AIMP1]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[METTL18]] | -0.59 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ARMCX5-GPRASP2]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PPCS]] | -0.58 | -0.61 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GRK6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PBX4]] | C | PBX4 activity raises GRK6's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without PBX4 | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-15.8, 7.7); signed map (-45.8, -8.2). **Vector** length 102, 23.1% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.3 | +14.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.1 | +16.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +4.7 | +7.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.5 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.9 | -6.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,403,204-177,442,901 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPRK6 |
| Gene groups (HGNC) | G protein-coupled receptor kinase family |
| Reactome | 3 pathways, smallest: G alpha (s) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [P43250](https://www.uniprot.org/uniprotkb/P43250) (G protein-coupled receptor kinase 6):

> Specifically phosphorylates the activated forms of G protein-coupled receptors. Such receptor phosphorylation initiates beta-arrestin-mediated receptor internalization, and signaling events leading to their desensitization. Seems to be involved in the desensitization of D2-like dopamine receptors in striatum and chemokine receptor CXCR4 which is critical for CXCL12-induced cell chemotaxis. Phosphorylates rhodopsin (RHO) (in vitro) and a non G protein-coupled receptor: LRP6 during Wnt signaling …

**Summary**, from NCBI Gene [2870](https://www.ncbi.nlm.nih.gov/gene/2870):

> This gene encodes a member of the guanine nucleotide-binding protein (G protein)-coupled receptor kinase subfamily of the Ser/Thr protein kinase family. The protein phosphorylates the activated forms of G protein-coupled receptors thus initiating their deactivation. Several transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4545) · Entrez [2870](https://www.ncbi.nlm.nih.gov/gene/2870) · UniProt [P43250](https://www.uniprot.org/uniprotkb/P43250) · Ensembl [ENSG00000198055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198055)

## Data

Gene col 12521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12521); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12521]; `tensor/DDL_lfc|DDL_z.npy` [12521]; `embed/gene_vectors.npy` [12521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12521 or target_col == 12521). Every well: [[GRK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
