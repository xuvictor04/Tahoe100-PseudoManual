---
symbol: "KIF26A"
type: "gene"
col: 837
ensembl_id: "ENSG00000066735"
name: "kinesin family member 26A"
location: "14q32.33"
module: 82
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 33
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 35
direction_downstream: 38
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# KIF26A

*kinesin family member 26A* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.27× (z +8.6, q 4e-15, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +6.7, q 4e-09, up in 12 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.423× (z -9.4, q 3e-18, down in 18 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRSK2]] (+0.73, fdr 7e-06), [[PDZD4]] (+0.68, fdr 7e-06), [[KCNQ2]] (+0.66, fdr 7e-06); moves opposite to [[MCTS1]] (-0.48, fdr 1e-04), [[RFX3-DT]] (-0.46, fdr 3e-04), [[NDUFB5]] (-0.45, fdr 4e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); 38 go from it, the strongest it → [[JAG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +8.6 | 4e-15 | 3/6 (NCI-H2030, CHP-212, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.9 | 2e-09 | 4/12 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +6.7 | 4e-09 | 12/30 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.84×** | +6.7 | 4e-09 | 10/30 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.39×** | +5.1 | 4e-05 | 7/23 (A549, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +4.9 | 1e-04 | 11/30 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.8 | 1e-04 | 10/30 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +3.7 | 0.017 | 8/30 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.15 | 1/17 (SW480) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.423×** | -9.4 | 3e-18 | 18/30 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -6.9 | 1e-09 | 17/26 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.543×** | -6.7 | 5e-09 | 16/28 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -6.4 | 2e-08 | 14/29 (HOP62, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -6.3 | 2e-08 | 13/23 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -6.1 | 1e-07 | 11/27 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.633×** | -4.8 | 1e-04 | 10/24 (A-427, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.632×** | -4.7 | 2e-04 | 10/26 (CHP-212, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.644×** | -4.6 | 2e-04 | 10/28 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.742×** | -4.6 | 2e-04 | 7/30 (RKO, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.661×** | -4.4 | 7e-04 | 9/26 (AN3 CA, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.680×** | -4.2 | 0.001 | 8/30 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -4.2 | 0.001 | 13/21 (NCI-H23, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -3.7 | 0.008 | 10/22 (C-33 A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.717×** | -3.6 | 0.011 | 10/30 (A-427, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.737×** | -3.3 | 0.031 | 9/27 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 70.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0668× (z -13.0) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.275× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.154× (z -9.0) |
| [[A-427 (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.180× (z -9.3) |
| [[LoVo (line)]] | wt | 9.92 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.188× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 8.56 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.3) |
| [[A-172 (line)]] | wt | 2.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0642× (z -9.0) |
| [[A549 (line)]] | wt | 4.40 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0743× (z -9.0) |
| [[HOP62 (line)]] | alt | 2.08 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0474× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 9.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0761× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -14.1) |
| [[A498 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRSK2]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PDZD4]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[KCNQ2]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[DPYSL5]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[VASH1]] | +0.64 | +0.70 / +0.37 | both halves | 8e-05 |  |
| [[JAKMIP1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RADIL]] | +0.61 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[GNAZ]] | +0.61 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[RASGEF1C]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.59 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[RET]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 | STRING 536 |
| [[ADCY1]] | +0.58 | +0.61 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[RFX3-DT]] | -0.46 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[NDUFB5]] | -0.45 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[COPS5]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 22, C 13. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises KIF26A's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without MCOLN2 | 0.007 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[CHD5]] | B | CHD5 activity raises KIF26A's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without CHD5 | 0.011 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[CECR2]] | B | CECR2 activity raises KIF26A's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without CECR2 | 0.011 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[LHX2]] | B | LHX2 activity raises KIF26A's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without LHX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[ARHGAP44]] | B | ARHGAP44 activity raises KIF26A's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.89× lower at baseline in the lines without ARHGAP44 | 0.025 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[RNF220]] | B | RNF220 activity raises KIF26A's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 1.72× lower at baseline in the lines without RNF220 | 0.032 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[GNAO1]] | B | GNAO1 activity raises KIF26A's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.37× lower at baseline in the lines without GNAO1 | 0.033 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[FAM124A]] | B | FAM124A activity raises KIF26A's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without FAM124A | 0.038 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[PAX2]] | B | PAX2 activity raises KIF26A's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.02× lower at baseline in the lines without PAX2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[LMX1B]] | B | LMX1B activity raises KIF26A's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without LMX1B | 0.045 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[KCNK13]] | B | KCNK13 activity raises KIF26A's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 2.19× lower at baseline in the lines without KCNK13 | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[GRID1]] | B | GRID1 activity raises KIF26A's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without GRID1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 27, C 11. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | KIF26A activity raises JAG2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without KIF26A | 0.002 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SH2B2]] | B | KIF26A activity raises SH2B2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.56× lower at baseline in the lines without KIF26A | 0.005 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[FBXL16]] | B | KIF26A activity raises FBXL16's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.53× lower at baseline in the lines without KIF26A | 0.007 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[TCF7L1]] | B | KIF26A activity raises TCF7L1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.82× lower at baseline in the lines without KIF26A | 0.008 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SDC3]] | B | KIF26A activity raises SDC3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without KIF26A | 0.008 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[ABCA3]] | B | KIF26A activity raises ABCA3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.26× lower at baseline in the lines without KIF26A | 0.009 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[KIF3C]] | B | KIF26A activity raises KIF3C's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without KIF26A | 0.010 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SHANK3]] | B | KIF26A activity raises SHANK3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without KIF26A | 0.014 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[MCOLN2]] | B | KIF26A activity raises MCOLN2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without KIF26A | 0.022 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[GPSM1]] | B | KIF26A activity raises GPSM1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without KIF26A | 0.022 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[PAX2]] | B | KIF26A activity raises PAX2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without KIF26A | 0.026 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[MCF2L2]] | B | KIF26A activity raises MCF2L2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.94× lower at baseline in the lines without KIF26A | 0.027 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.5, 39.4); signed map (26.3, 27.1). **Vector** length 43.1, 6.43% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.3 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -4.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 26A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,136,454-104,180,894 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1236, DKFZP434N178 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 13 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULI4](https://www.uniprot.org/uniprotkb/Q9ULI4) (Kinesin-like protein KIF26A):

> Atypical kinesin that plays a key role in enteric neuron development. Acts by repressing a cell growth signaling pathway in the enteric nervous system development, possibly via its interaction with GRB2 that prevents GRB2-binding to SHC, thereby attenating the GDNF-Ret signaling (By similarity). Binds to microtubules but lacks microtubule-based motility due to the absence of ATPase activity (By similarity). Plays a critical role in cerebral cortical development. It probably acts as a …

**Summary**, from NCBI Gene [26153](https://www.ncbi.nlm.nih.gov/gene/26153):

> Predicted to enable microtubule binding activity. Involved in cerebral cortex development; regulation of neuron migration; and regulation of neuron projection development. Predicted to be located in cytosol. Implicated in complex cortical dysplasia with other brain malformations 11. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20226) · Entrez [26153](https://www.ncbi.nlm.nih.gov/gene/26153) · UniProt [Q9ULI4](https://www.uniprot.org/uniprotkb/Q9ULI4) · Ensembl [ENSG00000066735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066735)

## Data

Gene col 837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 837); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 837]; `tensor/DDL_lfc|DDL_z.npy` [837]; `embed/gene_vectors.npy` [837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 837 or target_col == 837). Every well: [[KIF26A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF26A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
