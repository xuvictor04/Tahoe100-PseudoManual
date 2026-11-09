---
symbol: "UNC5CL"
type: "gene"
col: 4550
ensembl_id: "ENSG00000124602"
name: "unc-5 family C-terminal like"
location: "6p21.1"
module: 8
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 13
direction_downstream: 1
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# UNC5CL

*unc-5 family C-terminal like* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.45× (z +9.9, q 4e-20, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +9.6, q 3e-19, up in 13 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.381× (z -8.0, q 8e-13, down in 26 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF1A-AS1]] (+0.65, fdr 1e-05), [[RNF183]] (+0.64, fdr 7e-06), [[SMIM2-AS1]] (+0.63, fdr 1e-05); moves opposite to [[CROCCP3-1]] (-0.48, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TNFSF14]] → it (grade B ⚠); 1 goes from it, the strongest it → [[OARD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +9.9 | 4e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.6 | 3e-19 | 13/25 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +5.6 | 3e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.46×** | +5.3 | 2e-05 | 6/16 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +4.9 | 9e-05 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.16×** | +4.6 | 5e-04 | 5/10 (COLO 205, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +3.8 | 0.011 | 1/2 (COLO 205) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.016 | 4/16 (COLO 205, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.5 | 0.034 | 3/23 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.54×** | +3.3 | 0.057 | 4/21 (HOP62, SW1417, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +3.2 | 0.057 | 1/11 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.057 | 2/19 (HEC-1-A, SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.48×** | +3.2 | 0.057 | 3/21 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.057 | 5/22 (COLO 205, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.068 | 1/25 (COLO 205) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.66×** | +3.0 | 0.098 | 2/19 (COLO 205, HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.66×** | +3.0 | 0.098 | 1/23 (COLO 205) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -8.0 | 8e-13 | 26/42 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.467×** | -6.3 | 8e-08 | 16/34 (KATO III, PANC-1, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.477×** | -6.1 | 2e-07 | 16/35 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.285×** | -5.4 | 8e-06 | 16/29 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -5.1 | 4e-05 | 20/31 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.609×** | -4.1 | 0.004 | 9/37 (COLO 205, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.649×** | -3.6 | 0.024 | 9/39 (A549, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -3.6 | 0.024 | 11/39 (A-427, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.652×** | -3.6 | 0.024 | 9/16 (HEC-1-A, COLO 205, …) | two highest doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.454×** | -3.4 | 0.034 | 14/23 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.647×** | -3.4 | 0.034 | 11/29 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.687×** | -3.1 | 0.088 | 7/37 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -3.1 | 0.092 | 12/33 (A498, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 68.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -21.6) |
| [[CFPAC-1 (line)]] | alt | 5.49 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0734× (z -8.9) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 4.48 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0517× (z -9.9) |
| [[A-172 (line)]] | wt | 0.921 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF1A-AS1]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[RNF183]] | +0.64 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[SMIM2-AS1]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MUC20]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[TNFRSF14-AS1]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[RORC]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PTPN22]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[MUC1]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PDZK1IP1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3-1]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF14]] | B | TNFSF14 activity raises UNC5CL's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.42× lower at baseline in the lines without TNFSF14 | 0.007 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[SLC34A2]] | B | SLC34A2 activity raises UNC5CL's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.51× lower at baseline in the lines without SLC34A2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[RNF183]] | B | RNF183 activity raises UNC5CL's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.20× lower at baseline in the lines without RNF183 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[MMP7]] | B | MMP7 activity raises UNC5CL's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 1.63× lower at baseline in the lines without MMP7 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[SMIM2-AS1]] | B | SMIM2-AS1 activity raises UNC5CL's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without SMIM2-AS1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[RORC]] | B | RORC activity raises UNC5CL's level | lines that do not express RORC (30) vs lines expressing it (20) | 1.73× lower at baseline in the lines without RORC | 0.059 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[DSCAML1]] | B | DSCAML1 activity raises UNC5CL's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without DSCAML1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises UNC5CL's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 1.95× lower at baseline in the lines without ST6GALNAC1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[PROM1]] | B | PROM1 activity raises UNC5CL's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.00× lower at baseline in the lines without PROM1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[ERBB3]] | B | ERBB3 activity raises UNC5CL's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without ERBB3 | 0.082 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[BCAS1]] | B | BCAS1 activity raises UNC5CL's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 1.65× lower at baseline in the lines without BCAS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[PRSS51]] | B | PRSS51 activity raises UNC5CL's level | lines that do not express PRSS51 (31) vs lines expressing it (19) | 1.35× lower at baseline in the lines without PRSS51 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, AK4P3, ASCL1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OARD1]] | C | UNC5CL activity raises OARD1's level | lines that do not express UNC5CL (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without UNC5CL | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MEGF11; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, 53.0); signed map (60.2, 0.4). **Vector** length 47.2, 6.71% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +5.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.3 | -4.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | unc-5 family C-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,026,895-41,039,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34763, ZUD |
| Gene groups (HGNC) | ZU5 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV45](https://www.uniprot.org/uniprotkb/Q8IV45) (UNC5C-like protein):

> Inhibits NF-kappa-B-dependent transcription by impairing NF-kappa-B binding to its targets.

**Summary**, from NCBI Gene [222643](https://www.ncbi.nlm.nih.gov/gene/222643):

> Enables peptidase activity. Acts upstream of or within positive regulation of JNK cascade and positive regulation of canonical NF-kappaB signal transduction. Located in cytosol and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21203) · Entrez [222643](https://www.ncbi.nlm.nih.gov/gene/222643) · UniProt [Q8IV45](https://www.uniprot.org/uniprotkb/Q8IV45) · Ensembl [ENSG00000124602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124602)

## Data

Gene col 4550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4550); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4550]; `tensor/DDL_lfc|DDL_z.npy` [4550]; `embed/gene_vectors.npy` [4550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4550 or target_col == 4550). Every well: [[UNC5CL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC5CL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
