---
symbol: "AP1M2"
type: "gene"
col: 4969
ensembl_id: "ENSG00000129354"
name: "adaptor related protein complex 1 subunit mu 2"
location: "19p13.2"
module: 44
arm: "+"
pooled_cpm: 9.24
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 25
direction_downstream: 36
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# AP1M2

*adaptor related protein complex 1 subunit mu 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.67× (z +17.3, q 0e+00, up in 16 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.78× (z +4.1, q 0.002, up in 8 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.335×, LS 180 0.355×, HT-29 0.352×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.391×, NCI-H2347 0.510×, Panc 03.27 0.426×; ⚠ cell-cycle shift, explains ~45% of this change).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB25]] (+0.54, fdr 3e-05), [[TSPAN1]] (+0.51, fdr 3e-05), [[NUDT14]] (+0.50, fdr 6e-05); moves opposite to [[ADAMTS17]] (-0.45, fdr 2e-04), [[PTN]] (-0.42, fdr 1e-04), [[RMI2]] (-0.41, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[CLDN3]] → it (grade C ⚠); 36 go from it, the strongest it → [[KRTCAP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.67×** | +17.3 | 0e+00 | 16/19 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.49×** | +14.4 | 2e-44 | 11/14 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.65×** | +10.1 | 8e-22 | 10/15 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.81×** | +8.3 | 1e-14 | 6/22 (A-172, NCI-H2030, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.03×** | +7.0 | 2e-10 | 11/24 (A-172, SNU-1, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.83×** | +6.0 | 2e-07 | 7/24 (A-172, HepG2/C3A, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.1 | 2e-05 | 6/20 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.5 | 5e-04 | 2/10 (NCI-H2347, NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.52×** | +4.2 | 0.002 | 6/22 (A-172, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +4.1 | 0.002 | 8/20 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 5/22 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.041 | 8/20 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.40×** | +3.3 | 0.041 | 10/23 (A-172, A-427, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.2 | 0.065 | 1/24 (NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4969.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.335×, LS 180 0.355×, HT-29 0.352×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.391×, NCI-H2347 0.510×, Panc 03.27 0.426×; ⚠ cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 5 µM |  | 0.727× | -3.1 | 0.95 | 6/24 (HEC-1-A, SW48, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -12.1) |
| [[A-172 (line)]] | wt | 5.11 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +11.4) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 2.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HEC-1-A (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.4) |
| [[LS 180 (line)]] | wt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.980 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB25]] | +0.54 | +0.45 / +0.61 | both halves | 3e-05 | STRING 643 |
| [[TSPAN1]] | +0.51 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[NUDT14]] | +0.50 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[S100A14]] | +0.47 | +0.45 / +0.41 | both halves | 4e-05 | STRING 411 |
| [[BSPRY]] | +0.45 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[UCA1]] | +0.45 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[FXYD3]] | +0.45 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[HPGD]] | +0.44 | +0.36 / +0.36 | both halves | 9e-05 |  |
| [[KLK7]] | +0.44 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[MIR4307HG]] | +0.43 | +0.37 / +0.32 | both halves | 2e-04 |  |
| [[MAPRE3]] | +0.43 | +0.47 / +0.21 | both halves | 7e-04 |  |
| [[QPRT]] | +0.43 | +0.31 / +0.34 | both halves | 2e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS17]] | -0.45 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[PTN]] | -0.42 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[RMI2]] | -0.41 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[PAX2]] | -0.38 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[TEX30]] | -0.38 | -0.38 / -0.26 | both halves | 4e-04 |  |
| [[HMGB1]] | -0.38 | -0.34 / -0.29 | both halves | 3e-04 |  |
| [[DANT1]] | -0.37 | -0.35 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[CXCL10]] | -0.36 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[ADAMTS10]] | -0.36 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[SIAH2-AS1]] | -0.36 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[TLCD3B]] | -0.36 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[CKAP4]] | -0.35 | -0.17 / -0.32 | ⚠ not reproduced | 0.001 |  |
| [[USP1]] | -0.35 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[ATP10A]] | -0.35 | -0.34 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 0, C 25. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN3]] | C | CLDN3 activity raises AP1M2's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 5.91× lower at baseline in the lines without CLDN3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises AP1M2's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 6.27× lower at baseline in the lines without RAB25 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[CRB3]] | C | CRB3 activity raises AP1M2's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 5.93× lower at baseline in the lines without CRB3 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises AP1M2's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 5.40× lower at baseline in the lines without EPCAM | 2e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises AP1M2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 5.32× lower at baseline in the lines without BSPRY | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[CLDN7]] | C | CLDN7 activity raises AP1M2's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 5.36× lower at baseline in the lines without CLDN7 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises AP1M2's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 5.07× lower at baseline in the lines without MAL2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises AP1M2's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 5.28× lower at baseline in the lines without LCN2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises AP1M2's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 5.08× lower at baseline in the lines without S100A14 | 7e-04 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises AP1M2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 4.53× lower at baseline in the lines without LAD1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[BICDL2]] | C | BICDL2 activity raises AP1M2's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.51× lower at baseline in the lines without BICDL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises AP1M2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 5.00× lower at baseline in the lines without PRSS8 | 0.002 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 10, C 26. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRTCAP3]] | B | AP1M2 activity raises KRTCAP3's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without AP1M2 | 0.002 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[ELMO3]] | B | AP1M2 activity raises ELMO3's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 2.30× lower at baseline in the lines without AP1M2 | 0.004 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[NUDT14]] | B | AP1M2 activity raises NUDT14's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without AP1M2 | 0.014 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[POLE3]] | B | AP1M2 activity lowers POLE3's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 1.17× higher at baseline in the lines without AP1M2 | 0.027 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[PROM2]] | B | AP1M2 activity raises PROM2's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without AP1M2 | 0.031 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[ABHD11]] | B | AP1M2 activity raises ABHD11's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 2.18× lower at baseline in the lines without AP1M2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[SCG5]] | B | AP1M2 activity lowers SCG5's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 1.64× higher at baseline in the lines without AP1M2 | 0.051 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[QPRT]] | B | AP1M2 activity raises QPRT's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 2.15× lower at baseline in the lines without AP1M2 | 0.062 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | AP1M2 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express AP1M2 (24) vs lines expressing it (24) | the lines without AP1M2: 0.88× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| cells under [[Digitoxin (drug)]] 5 µM | B | AP1M2 activity raises the cells' numbers under Digitoxin 5 µM (protects the cells) | lines that do not express AP1M2 (24) vs lines expressing it (24) | the lines without AP1M2: 0.80× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[CRB3]] | C | AP1M2 activity raises CRB3's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 3.23× lower at baseline in the lines without AP1M2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7; co-absent with the target |
| [[EPCAM]] | C | AP1M2 activity raises EPCAM's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 6.95× lower at baseline in the lines without AP1M2 | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.301). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 58.1); signed map (71.2, 7.9). **Vector** length 44.4, 9.89% of its response variance represented; |z| ≥ 3 in 365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +17.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit mu 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,572,671-10,587,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSMU1B, mu2, AP1-mu2 |
| Gene groups (HGNC) | Adaptor related protein complex 1 |
| Reactome | 13 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Q5](https://www.uniprot.org/uniprotkb/Q9Y6Q5) (AP-1 complex subunit mu-2):

> Subunit of clathrin-associated adaptor protein complex 1 that plays a role in protein sorting in the trans-Golgi network (TGN) and endosomes. The AP complexes mediate the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules.

**Summary**, from NCBI Gene [10053](https://www.ncbi.nlm.nih.gov/gene/10053):

> This gene encodes a subunit of the heterotetrameric adaptor-related protein comlex 1 (AP-1), which belongs to the adaptor complexes medium subunits family. This protein is capable of interacting with tyrosine-based sorting signals. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:558](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:558) · Entrez [10053](https://www.ncbi.nlm.nih.gov/gene/10053) · UniProt [Q9Y6Q5](https://www.uniprot.org/uniprotkb/Q9Y6Q5) · Ensembl [ENSG00000129354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129354)

## Data

Gene col 4969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4969); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4969]; `tensor/DDL_lfc|DDL_z.npy` [4969]; `embed/gene_vectors.npy` [4969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4969 or target_col == 4969). Every well: [[AP1M2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1M2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
