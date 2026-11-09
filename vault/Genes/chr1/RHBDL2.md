---
symbol: "RHBDL2"
type: "gene"
col: 8152
ensembl_id: "ENSG00000158315"
name: "rhomboid like 2"
location: "1p34.3"
module: 8
arm: "+"
pooled_cpm: 10.66
n_lines_expressing: 28
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 27
direction_downstream: 24
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RHBDL2

*rhomboid like 2* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +9.7, q 1e-19, up in 6 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.398× (z -11.7, q 5e-29, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM31]] (+0.64, fdr 7e-06), [[PDZK1IP1]] (+0.61, fdr 1e-05), [[NECTIN4]] (+0.61, fdr 7e-06); moves opposite to [[RSU1]] (-0.48, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[LPAR5]] → it (grade B ⚠); 24 go from it, the strongest it → [[ATP1B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +9.7 | 1e-19 | 6/24 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.9 | 1e-16 | 0/12 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +8.9 | 1e-16 | 4/20 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +7.4 | 2e-11 | 6/24 (HS-578T, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.6 | 2e-06 | 8/23 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +5.6 | 2e-06 | 11/26 (Hs 766T, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 8e-04 | 10/26 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.001 | 8/25 (A498, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 15/25 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.006 | 12/26 (HOP62, SW 1088, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.006 | 13/26 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +3.7 | 0.008 | 1/21 (Panc 03.27) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.009 | 11/25 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.016 | 7/24 (A-427, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +3.5 | 0.016 | 12/26 (HOP62, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.028 | 8/26 (AsPC-1, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.028 | 9/26 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.035 | 8/26 (PANC-1, A549, …) | all doses, flat | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.042 | 5/26 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.044 | 9/25 (AsPC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.398×** | -11.7 | 5e-29 | 23/26 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.441×** | -10.4 | 6e-23 | 22/26 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.455×** | -10.0 | 2e-21 | 22/26 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.712×** | -4.3 | 0.002 | 14/26 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.715×** | -4.3 | 0.002 | 14/26 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -4.2 | 0.002 | 13/26 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.732×** | -4.0 | 0.006 | 10/26 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.755×** | -3.6 | 0.024 | 11/26 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.027 | 8/25 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.774×** | -3.3 | 0.063 | 10/24 (COLO 205, A-172, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.789× | -3.0 | 0.13 | 5/25 (HT-29, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 52.6 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -16.4) |
| [[KATO III (line)]] | alt | 23.4 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0691× (z -16.0) |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.251× (z -11.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.258× (z -11.0) |
| [[A-172 (line)]] | wt | 27.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -13.2) |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0536× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -13.0) |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0644× (z -14.3) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.192× (z -8.6) |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -10.0) |
| [[A498 (line)]] | wt | 27.2 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 8.36 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -9.3) |
| [[COLO 205 (line)]] | alt | 8.30 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0434× (z -11.0) |
| [[HOP62 (line)]] | alt | 9.03 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.185× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -9.4) |
| [[A-427 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM31]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PDZK1IP1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[NECTIN4]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PRRG4]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[STAP2]] | +0.58 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[RBM47]] | +0.58 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CRACDL]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NDRG2]] | +0.57 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SLC44A4]] | +0.57 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSU1]] | -0.48 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 18, C 9. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR5]] | B | LPAR5 activity raises RHBDL2's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without LPAR5 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[HSH2D]] | B | HSH2D activity raises RHBDL2's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.59× lower at baseline in the lines without HSH2D | 0.021 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[NECTIN4]] | B | NECTIN4 activity raises RHBDL2's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 1.99× lower at baseline in the lines without NECTIN4 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[STEAP3]] | B | STEAP3 activity lowers RHBDL2's level | lines that do not express STEAP3 (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without STEAP3 | 0.023 | ⚠ within organs, on part of the lines; also absent: GPR155; maybe low, not absent |
| [[FXYD3]] | B | FXYD3 activity raises RHBDL2's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without FXYD3 | 0.030 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[CGNL1]] | B | CGNL1 activity raises RHBDL2's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without CGNL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[RNF39]] | B | RNF39 activity raises RHBDL2's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 1.87× lower at baseline in the lines without RNF39 | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[TMPRSS2]] | B | TMPRSS2 activity raises RHBDL2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without TMPRSS2 | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[STAT5A]] | B | STAT5A activity raises RHBDL2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without STAT5A | 0.042 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[ANO9]] | B | ANO9 activity raises RHBDL2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without ANO9 | 0.043 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises RHBDL2's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without PLEKHG6 | 0.046 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[TMPRSS2]] | B | TMPRSS2 activity strengthens RHBDL2's drug response | lines that do not express TMPRSS2 (17) vs lines expressing it (9) | the lines without TMPRSS2 respond 1.38× as strongly (z diff -0.66); rises at some drug-doses, falls at others (28% from rises): Panobinostat 0.5 µM: 0.32x vs 0.16x (z diff +3.2); Panobinostat 5 µM: 0.38x vs 0.19x (z diff +3.1); Trametinib 0.5 µM: 1.33x vs 1.71x (z diff +1.7) | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 15, C 9. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | RHBDL2 activity raises ATP1B1's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without RHBDL2 | 0.040 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[TNFRSF14]] | B | RHBDL2 activity raises TNFRSF14's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without RHBDL2 | 0.050 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[PRRG4]] | B | RHBDL2 activity raises PRRG4's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without RHBDL2 | 0.058 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | RHBDL2 activity raises TNFRSF14-AS1's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without RHBDL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[CARD14]] | B | RHBDL2 activity raises CARD14's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without RHBDL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[LITAF]] | B | RHBDL2 activity raises LITAF's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without RHBDL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[STAT5A]] | B | RHBDL2 activity raises STAT5A's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without RHBDL2 | 0.064 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[MUC4]] | B | RHBDL2 activity raises MUC4's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without RHBDL2 | 0.072 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[CARD14]] | B | RHBDL2 activity strengthens CARD14's drug response | lines that do not express RHBDL2 (20) vs lines expressing it (25) | the lines without RHBDL2 respond 0.57× as strongly (z diff +0.54); rises at some drug-doses, falls at others (72% from rises): Tucidinostat 0.5 µM: 0.84x vs 1.65x (z diff +2.0); Ouabain (Octahydrate) 5 µM: 0.80x vs 0.48x (z diff +1.6); Tucidinostat 5 µM: 1.18x vs 1.65x (z diff +1.6) | 0.072 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[SEC16B]] | B | RHBDL2 activity raises SEC16B's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without RHBDL2 | 0.074 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[ATP1B1]] | B | RHBDL2 activity weakens ATP1B1's drug response | lines that do not express RHBDL2 (17) vs lines expressing it (24) | the lines without RHBDL2 respond 1.60× as strongly (z diff -1.93); strongest at Idarubicin (hydrochloride) 5 µM: 1.64x vs 0.89x (z diff -7.0) | 0.076 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CTSS]] | B | RHBDL2 activity raises CTSS's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without RHBDL2 | 0.079 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 55.0); signed map (55.4, 0.6). **Vector** length 73.4, 20.0% of its response variance represented; |z| ≥ 3 in 625 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +3.8 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +5.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | rhomboid like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:38,885,807-38,941,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20435 |
| Gene groups (HGNC) | Rhomboid family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX52](https://www.uniprot.org/uniprotkb/Q9NX52) (Rhomboid-related protein 2):

> Regulator of proteosome activity independent of enzymatic activity. Involved in regulated intramembrane proteolysis and the subsequent release of functional polypeptides from their membrane anchors. Known substrate: EFNB3.

**Summary**, from NCBI Gene [54933](https://www.ncbi.nlm.nih.gov/gene/54933):

> The protein encoded by this gene is a member of the rhomboid family of integral membrane proteins. This family contains proteins that are related to Drosophila rhomboid protein. Members of this family are found in both prokaryotes and eukaryotes and are thought to function as intramembrane serine proteases. The encoded protein is thought to release soluble growth factors by proteolytic cleavage of certain membrane-bound substrates, including ephrin B2 and ephrin B3. Two transcript variants …

**Accessions** — [HGNC:16083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16083) · Entrez [54933](https://www.ncbi.nlm.nih.gov/gene/54933) · UniProt [Q9NX52](https://www.uniprot.org/uniprotkb/Q9NX52) · Ensembl [ENSG00000158315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158315)

## Data

Gene col 8152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8152); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8152]; `tensor/DDL_lfc|DDL_z.npy` [8152]; `embed/gene_vectors.npy` [8152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8152 or target_col == 8152). Every well: [[RHBDL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHBDL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
