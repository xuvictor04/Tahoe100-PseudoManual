---
symbol: "TMEM184A"
type: "gene"
col: 9015
ensembl_id: "ENSG00000164855"
name: "transmembrane protein 184A"
location: "7p22.3"
module: 27
arm: "+"
pooled_cpm: 7.0
n_lines_expressing: 42
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 64
direction_downstream: 7
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# TMEM184A

*transmembrane protein 184A* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +11.6, q 4e-28, up in 13 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +4.2, q 0.004, up in 8 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.480× (z -9.1, q 5e-17, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF14-AS1]] (+0.66, fdr 1e-05), [[ARHGEF38]] (+0.64, fdr 1e-05), [[TMC4]] (+0.62, fdr 1e-05); moves opposite to [[WDFY2]] (-0.49, fdr 3e-05), [[CEP170]] (-0.47, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 64 arrows point to it, the strongest [[LINC03040]] → it (grade B ⚠); 7 go from it, the strongest it → [[EPS8L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +11.6 | 4e-28 | 13/24 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +10.3 | 1e-22 | 7/12 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +8.1 | 7e-14 | 9/20 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.2 | 0.003 | 7/26 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.004 | 8/36 (PANC-1, A549, …) | top dose only |  |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.007 | 4/35 (NCI-H2030, HOP62, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.007 | 1/30 (BT-474) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.060 | 5/32 (A549, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.16 | 0/31 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -9.1 | 5e-17 | 22/36 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.486×** | -9.0 | 9e-17 | 26/36 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.543×** | -7.6 | 6e-12 | 21/37 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -5.9 | 4e-07 | 20/35 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -5.6 | 3e-06 | 17/36 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.700×** | -4.4 | 1e-03 | 16/31 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.758×** | -3.4 | 0.051 | 13/37 (SW480, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.773× | -3.2 | 0.11 | 12/35 (HT-29, KATO III, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.625× | -3.0 | 0.15 | 13/34 (HT-29, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.0 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.193× (z -11.8) |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0607× (z -14.3) |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.152× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.117× (z -11.4) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-427 (line)]] | wt | 7.31 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.121× (z -9.0) |
| [[COLO 205 (line)]] | alt | 8.20 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 6.89 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0764× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 5.92 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 4.10 | 0 | 1 | — | [[Ranolazine (drug)]] 5 µM 0.0759× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 5.80 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.103× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H460 (line)]] | wt | 4.13 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0809× (z -10.7) |
| [[A-172 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | +0.66 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF38]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[TMC4]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[IQANK1]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[RGS6]] | +0.62 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[LINC02253]] | +0.62 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ELF3-AS1]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ITGB6]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TNNT2]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[DENND2D]] | +0.58 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[MUC1]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ADAP1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDFY2]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CEP170]] | -0.47 | -0.52 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 64, C 0. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03040]] | B | LINC03040 activity raises TMEM184A's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.63× lower at baseline in the lines without LINC03040 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[LAD1]] | B | LAD1 activity raises TMEM184A's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without LAD1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[TMEM45B]] | B | TMEM45B activity raises TMEM184A's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.01× lower at baseline in the lines without TMEM45B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[SCNN1A]] | B | SCNN1A activity raises TMEM184A's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without SCNN1A | 7e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[TNNT2]] | B | TNNT2 activity raises TMEM184A's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without TNNT2 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[TMEM125]] | B | TMEM125 activity raises TMEM184A's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.03× lower at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[CLDN3]] | B | CLDN3 activity raises TMEM184A's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without CLDN3 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises TMEM184A's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without SPINT1-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[TSPAN1]] | B | TSPAN1 activity raises TMEM184A's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.73× lower at baseline in the lines without TSPAN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[MISP]] | B | MISP activity raises TMEM184A's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.85× lower at baseline in the lines without MISP | 0.002 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[ILDR1]] | B | ILDR1 activity raises TMEM184A's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without ILDR1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[ANXA3]] | B | ANXA3 activity raises TMEM184A's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without ANXA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L2]] | B | TMEM184A activity raises EPS8L2's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 3.46× lower at baseline in the lines without TMEM184A | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |
| [[ANO9]] | B | TMEM184A activity raises ANO9's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 3.05× lower at baseline in the lines without TMEM184A | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |
| [[TMC4]] | B | TMEM184A activity raises TMC4's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 2.78× lower at baseline in the lines without TMEM184A | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent |
| [[PPL]] | B | TMEM184A activity raises PPL's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 4.09× lower at baseline in the lines without TMEM184A | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent |
| [[ANXA3]] | B | TMEM184A activity raises ANXA3's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 2.83× lower at baseline in the lines without TMEM184A | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |
| [[FAAH]] | B | TMEM184A activity raises FAAH's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without TMEM184A | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |
| [[SLC44A5]] | B | TMEM184A activity raises SLC44A5's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 3.10× lower at baseline in the lines without TMEM184A | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.8, 53.7); signed map (58.2, 10.1). **Vector** length 64.7, 12.1% of its response variance represented; |z| ≥ 3 in 787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 184A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,542,235-1,560,821 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9712, SDMG1, SLC51C1 |
| Gene groups (HGNC) | Solute carrier family 51 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMB5](https://www.uniprot.org/uniprotkb/Q6ZMB5) (Transmembrane protein 184A):

> Acts as a heparin receptor in vascular cells (By similarity). May be involved in vesicle transport in exocrine cells and Sertoli cells (By similarity).

**Summary**, from NCBI Gene [202915](https://www.ncbi.nlm.nih.gov/gene/202915):

> Predicted to enable heparin binding activity and transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to act upstream of or within germ-line sex determination; regulation of protein localization; and regulation of secretion. Predicted to be located in cytoplasmic vesicle; perinuclear region of cytoplasm; and plasma membrane. Predicted to be active in early endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28797) · Entrez [202915](https://www.ncbi.nlm.nih.gov/gene/202915) · UniProt [Q6ZMB5](https://www.uniprot.org/uniprotkb/Q6ZMB5) · Ensembl [ENSG00000164855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164855)

## Data

Gene col 9015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9015); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9015]; `tensor/DDL_lfc|DDL_z.npy` [9015]; `embed/gene_vectors.npy` [9015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9015 or target_col == 9015). Every well: [[TMEM184A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM184A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
