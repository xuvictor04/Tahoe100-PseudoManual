---
symbol: "MUC20"
type: "gene"
col: 10770
ensembl_id: "ENSG00000176945"
name: "mucin 20, cell surface associated"
location: "3q29"
module: 8
arm: "+"
pooled_cpm: 14.35
n_lines_expressing: 36
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 24
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 65
direction_downstream: 24
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MUC20

*mucin 20, cell surface associated* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +10.0, q 1e-20, up in 19 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.573× (z -5.3, q 8e-05, down in 17 of 33 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.416× (z -4.3, q 0.003, down in 13 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD12-AS1]] (+0.71, fdr 8e-06), [[RAMP1]] (+0.71, fdr 7e-06), [[SPATA6L]] (+0.68, fdr 7e-06); moves opposite to [[CHD1L]] (-0.55, fdr 9e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 65 arrows point to it, the strongest [[ST14]] → it (grade B ⚠); 24 go from it, the strongest it → [[SMBD1P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +10.0 | 1e-20 | 19/29 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +9.4 | 2e-18 | 12/24 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +8.4 | 7e-15 | 16/31 (LoVo, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +7.2 | 8e-11 | 9/20 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +6.5 | 9e-09 | 7/15 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.0 | 2e-07 | 10/26 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.79×** | +5.3 | 1e-05 | 17/30 (HEC-1-A, LS 180, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.78×** | +5.2 | 1e-05 | 17/30 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.0 | 4e-05 | 10/33 (A-172, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.62×** | +4.6 | 3e-04 | 14/33 (HEC-1-A, LS 180, …) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.58×** | +4.3 | 9e-04 | 11/33 (A498, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.003 | 12/33 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.004 | 7/28 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.009 | 13/31 (HEC-1-A, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.015 | 12/33 (HEC-1-A, LS 180, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.022 | 6/32 (KATO III, COLO 205, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.022 | 9/30 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.024 | 14/30 (HEC-1-A, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.573×** | -5.3 | 8e-05 | 17/33 (BT-474, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.610×** | -4.7 | 8e-04 | 14/31 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -4.3 | 0.003 | 13/30 (SW 900, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.076 | 13/33 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.684×** | -3.4 | 0.076 | 5/30 (A-172, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.783×** | -3.3 | 0.093 | 8/32 (HS-578T, BT-474, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.713× | -3.2 | 0.11 | 5/31 (Panc 03.27, BT-474, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.719× | -3.1 | 0.12 | 12/28 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | 0.723× | -3.1 | 0.13 | 14/28 (BT-474, SW480, …) | all doses, flat |  |
| [[Ranolazine (drug)]] 5 µM |  | 0.726× | -3.0 | 0.13 | 10/33 (RPMI-7951, A-172, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.715× | -3.0 | 0.14 | 10/30 (COLO 205, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 271 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 61.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.7) |
| [[HT-29 (line)]] | alt | 38.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -19.8) |
| [[HEC-1-A (line)]] | alt | 41.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 7.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -8.8) |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.0) |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0887× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 3.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 48.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.4) |
| [[SNU-423 (line)]] | alt | 7.82 | 0 | 1 | — | [[Fenofibrate (drug)]] 0.05 µM 0.0414× (z -10.0) |
| [[A-172 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD12-AS1]] | +0.71 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[RAMP1]] | +0.71 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SPATA6L]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[MGAM2]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PTPN22]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[THBS4-AS1]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MUC4]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 974; ⚠ same locus (5.6 kb: neighbours can correlate without regulation) |
| [[LINC01504]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[STS]] | +0.64 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[UNC5CL]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD1L]] | -0.55 | -0.60 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 65, C 0. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST14]] | B | ST14 activity raises MUC20's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.77× lower at baseline in the lines without ST14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises MUC20's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 4.46× lower at baseline in the lines without PDZK1IP1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[FUT3]] | B | FUT3 activity raises MUC20's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.90× lower at baseline in the lines without FUT3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[ADGRF1]] | B | ADGRF1 activity raises MUC20's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.61× lower at baseline in the lines without ADGRF1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[WFDC2]] | B | WFDC2 activity raises MUC20's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 4.49× lower at baseline in the lines without WFDC2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[MROH3P]] | B | MROH3P activity raises MUC20's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 3.61× lower at baseline in the lines without MROH3P | 7e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[SLC44A4]] | B | SLC44A4 activity raises MUC20's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.22× lower at baseline in the lines without SLC44A4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[CLIC5]] | B | CLIC5 activity raises MUC20's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.84× lower at baseline in the lines without CLIC5 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[MACC1]] | B | MACC1 activity raises MUC20's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 4.38× lower at baseline in the lines without MACC1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[C11orf52]] | B | C11orf52 activity raises MUC20's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 3.20× lower at baseline in the lines without C11orf52 | 0.002 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[STEAP4]] | B | STEAP4 activity raises MUC20's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 4.50× lower at baseline in the lines without STEAP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[RNF39]] | B | RNF39 activity raises MUC20's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without RNF39 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 24, C 0. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMBD1P]] | B | MUC20 activity raises SMBD1P's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.30× lower at baseline in the lines without MUC20 | 0.005 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[MYO7A]] | B | MUC20 activity raises MYO7A's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without MUC20 | 0.017 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[ST14]] | B | MUC20 activity raises ST14's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 4.82× lower at baseline in the lines without MUC20 | 0.020 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[DNAH12]] | B | MUC20 activity raises DNAH12's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without MUC20 | 0.021 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[MACC1]] | B | MUC20 activity raises MACC1's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 4.02× lower at baseline in the lines without MUC20 | 0.031 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[ADCY4]] | B | MUC20 activity raises ADCY4's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without MUC20 | 0.031 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[UCA1]] | B | MUC20 activity raises UCA1's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 3.01× lower at baseline in the lines without MUC20 | 0.033 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[MROH3P]] | B | MUC20 activity raises MROH3P's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.79× lower at baseline in the lines without MUC20 | 0.033 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[RNF220]] | B | MUC20 activity lowers RNF220's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.49× higher at baseline in the lines without MUC20 | 0.035 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[ADGRF1]] | B | MUC20 activity raises ADGRF1's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 3.43× lower at baseline in the lines without MUC20 | 0.040 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[TMC4]] | B | MUC20 activity raises TMC4's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.75× lower at baseline in the lines without MUC20 | 0.041 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[CATSPERB]] | B | MUC20 activity raises CATSPERB's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 3.10× lower at baseline in the lines without MUC20 | 0.045 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 52.8); signed map (59.9, 1.0). **Vector** length 79.0, 18.3% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +3.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | +1.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -3.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mucin 20, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:195,720,884-195,741,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14408, KIAA1359 |
| Gene groups (HGNC) | Mucins |
| Reactome | 15 pathways, smallest: MET activates RAS signaling; Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N307](https://www.uniprot.org/uniprotkb/Q8N307) (Mucin-20):

> May regulate MET signaling cascade. Seems to decrease hepatocyte growth factor (HGF)-induced transient MAPK activation. Blocks GRB2 recruitment to MET thus suppressing the GRB2-RAS pathway. Inhibits HGF-induced proliferation of MMP1 and MMP9 expression.

**Summary**, from NCBI Gene [200958](https://www.ncbi.nlm.nih.gov/gene/200958):

> This gene encodes a member of the mucin protein family. Mucins are high molecular weight glycoproteins secreted by many epithelial tissues to form an insoluble mucous barrier. The C-terminus of this family member associates with the multifunctional docking site of the MET proto-oncogene and suppresses activation of some downstream MET signaling cascades. The protein features a mucin tandem repeat domain that varies between two and six copies in most individuals. Multiple variants encoding …

**Accessions** — [HGNC:23282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23282) · Entrez [200958](https://www.ncbi.nlm.nih.gov/gene/200958) · UniProt [Q8N307](https://www.uniprot.org/uniprotkb/Q8N307) · Ensembl [ENSG00000176945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176945)

## Data

Gene col 10770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10770); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10770]; `tensor/DDL_lfc|DDL_z.npy` [10770]; `embed/gene_vectors.npy` [10770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10770 or target_col == 10770). Every well: [[MUC20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
